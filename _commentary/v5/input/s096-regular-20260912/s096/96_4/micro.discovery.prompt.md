# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **96:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s096-regular-20260912/s096/96_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "96:4",
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
{"branch_registry":[{"boundary":"Çekirdek, bir şeyi bilme ve gerçeğiyle kavramadır; bildirme, öğretme, öğrenme ve bilgi yarışında yenme ayrı biçimlere bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B001","candidate_links":[{"candidate_id":"cand_8e4a96727f27458aa686","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:4:2:1","qac_word_ref":"96:4:2","surface_ar":"عَلَّمَ"}],"gloss":"bilme ve gerçeğini kavrama","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi bilme, tanıma ve gerçeğine uygun biçimde kavrama durumu bilgisizliğin karşıtıdır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir haberin farkına varmak veya ondan haberdar olmak, bilme çekirdeğinin belirli bir konuya uygulanmasıdır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bildirme, öğretme ve öğrenme biçimleri bilginin bir başkasına ulaştırılması ya da kişinin onu edinmesi süreçlerini anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Karşılıklı bilgi sınamasında birini yenmek, belirli bir kuruluşta ortaya çıkan rekabetçi kullanımdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bilgisizliğin karşıtı olan temel zihinsel edinimi, tanımayı ve gerçeğe uygun kavrayışı birlikte karşılar.","boundary_detail":"Çekirdek, bir şeyi bilme ve gerçeğiyle kavramadır; bildirme, öğretme, öğrenme ve bilgi yarışında yenme ayrı biçimlere bağlıdır.","branch_image_ar":"انكشاف الشيء للعارف","concept_gloss":"bilme ve gerçeğini kavrama","contextual_glosses":[{"applicability":"Bir olay veya gelişme hakkındaki haberin kişinin bilgisine ulaşması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Haberin farkına varma ve ondan bilgi edinme yönünü korur."},"facet_ids":["F002"],"text":"haberinden haberdar olmak","usage_role":"contextual"},{"applicability":"Bilginin tekrar ve yönlendirmeyle bir öğrenende yerleşmesini sağlayan öğretim bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilginin aktarılması ve öğrenende kalıcı bir sonuç oluşturması sürecini korur."},"facet_ids":["F003"],"text":"öğretmek ve öğrenmesini sağlamak","usage_role":"explanatory"},{"applicability":"İki kişi arasındaki bilgi sınamasında bir tarafın ötekini yenmesi bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bilgi alanındaki karşılaştırmayı ve üstün gelme sonucunu korur."},"facet_ids":["F004"],"text":"bilgide üstün gelmek","usage_role":"contextual"}],"definition":"Bir şeyi bilmek, tanımak ve onu gerçeğine uygun biçimde kavramak; böylece bilgisizlikten çıkmaktır. Haber verilmesi, öğretme, öğrenme ve bilgi bakımından üstün gelme bu çekirdekten hareket eden, belirli biçimlere bağlı kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi bilme, tanıma ve gerçeğine uygun biçimde kavrama durumu bilgisizliğin karşıtıdır."},{"facet_id":"F002","role":"extension","statement":"Bir haberin farkına varmak veya ondan haberdar olmak, bilme çekirdeğinin belirli bir konuya uygulanmasıdır."},{"facet_id":"F003","role":"associated_use","statement":"Bildirme, öğretme ve öğrenme biçimleri bilginin bir başkasına ulaştırılması ya da kişinin onu edinmesi süreçlerini anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Karşılıklı bilgi sınamasında birini yenmek, belirli bir kuruluşta ortaya çıkan rekabetçi kullanımdır."}],"identity_rationale":"Dalın bilme ve bilgisizliğin karşıtı olma yönündeki çekirdeği kaynak ifadesiyle uyumludur. Ancak haberden haberdar olma, öğretme, öğrenme ve bilgi bakımından üstün gelme kullanımları bu çekirdekle aynı düzeyde değil, belirli biçimlere bağlı uzantılar olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bilgi; bir şeyi gerçeğiyle kavrama"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şeyi bilmek ve tanımak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"haberinden haberdar olmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bildirmek, haberdar etmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"öğretmek, öğrenmesini sağlamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"öğrenmek, kavramaya yönelmek"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bilmek; buyrukta bil ki"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bilgi yarışında yenmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"bilen ve bildiğine göre davranan kişi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bilgili, bilgi sahibi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çok bilgili, çok bilen"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"son derece bilgili kişi"}],"lexicalization_note":"Tanım çıplak bilme çekirdeğini öne alır; haber, öğretim, öğrenim ve karşılıklı bilgi sınamasıyla ilgili anlamları yalnızca ilgili biçim ve kuruluşlara bağlar.","neighbor_coverage_note":"Bilme çekirdeğini en çok açıklayan yakın kavrayış dalı, açık karşıtı olan bilgisizlik dalı ve doğru kullanım boyutu taşıyan bilgelik dalı seçildi; öteki adaylar yalnızca uzak çağrışım veya ayrı kök içi anlam alanı sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Çekirdekleri yakın olsa da odak dalın biçime bağlı aktarım ve edinim süreçleri ile komşunun akletme ve hızlı anlama vurgusu karşılıklı değiştirilebilirliği sınırlar.","focus_only":"Odak dal, haberden haberdar etme, öğretme, öğrenme ve bilgi yarışında üstün gelme gibi biçime bağlı uzantıları da kapsar.","gloss":"bilmek ve anlamını kavramak","neighbor_only":"Komşu dal, anlamları doğrulama, akletme ve çabuk kavrama yönlerini ayrıca öne çıkarır.","neighbor_ref":"root_001182/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi bilme, tanıma ve zihnen kavrama alanında büyük ölçüde örtüşür."},{"boundary_match":"opposed","distinction":"Odak dal bilgiye erişmeyi ve kavramayı bildirirken komşu dal bu erişimin bulunmamasını ya da gerçeğin yanlış bilinmesini bildirir.","focus_only":"Bir şeyi tanıma, gerçeğine uygun kavrama ve bilgi sahibi olma bulunur.","gloss":"bilgi ile bilgisizlik karşıtlığı","neighbor_only":"Bilginin yokluğu, durumu tanımama veya gerçeğe aykırı bir kanaat bulunur.","neighbor_ref":"root_000271/B001","relation_type":"antonym","shared_zone":"İki dal aynı zihinsel erişim ekseninin olumlu ve olumsuz uçlarını gösterir."},{"boundary_match":"partial","distinction":"Bilmek tek başına odak dal için yeterli olabilir; komşu dal ise bilginin doğru yargı ve isabetli davranışla birleşmesini öne çıkarır.","focus_only":"Odak dalda yalın bilme ve tanıma, bilginin doğru kullanımından bağımsız olarak çekirdekte yer alabilir.","gloss":"bilgi ile bilgelik","neighbor_only":"Komşu dal doğruyu bulma, yerinde yargı ve bilgiyi isabetli kullanma niteliğini gerektirir.","neighbor_ref":"root_000348/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal bilgi sahibi olmayı ve zihinsel kavrayışı paylaşır."}],"source_phrase_ar":"العلم نقيض الجهل (maqayis;ayn;tahdhib)؛ علمت الشيء عرفته (sihah;tahdhib)؛ إدراك الشيء بحقيقته (mufradat)؛ ما علمت بخبرك أي ما شعرت به (ayn;tahdhib)؛ أعلمته بكذا وعلمته تعليما (ayn)؛ التعليم تنبيه النفس لتصور المعاني (mufradat)؛ تعلم بمعنى اعلم (maqayis;sihah;tahdhib)؛ عالمت الرجل فعلمته (sihah;tahdhib)","source_summary":"Kaynakların ortak çekirdeği, bilgiyi bilgisizliğin karşıtı sayar ve bir şeyi tanıyıp gerçeğiyle kavramayı öne çıkarır. Toplu tanıklık ayrıca haberden haberdar olmayı, bilgiyi aktarmayı, öğrenmeyi ve bilgiyle üstün gelmeyi biçime bağlı uzantılar olarak gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلم نقيض الجهل وإدراك الشيء ومعرفته والشعور بالخبر والتعلم والتعليم والإعلام والمغالبة بالعلم","what_is_not_ar":"ليس هو العلامة الحسية ولا الجبل ولا الراية ولا الشق في الشفة ولا اسم العالمين"},"support_links":["sup_9a6be11e6bf6a3ca03c4"]},{"boundary":"Dal bütün işaret türlerini sınırsızca kapsamaz; kaynakta anılan ayırt etme ve yol gösterme işlevli izlerle bunlara bağlı kullanımlarla sınırlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B002","candidate_links":[{"candidate_id":"cand_6b44d9e2df2e3f556c84","lane":"micro"},{"candidate_id":"cand_d720c120a6ca5240daf2","lane":"micro"},{"candidate_id":"cand_343c5ab6bc6f197cc5ae","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:4:2:1","qac_word_ref":"96:4:2","surface_ar":"عَلَّمَ"}],"gloss":"ayırt edici ve yol gösterici işaret","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir nesneyi veya kişiyi başkalarından ayırıp tanınır kılan belirgin iz ya da işaret çekirdeği oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bayrak, belirgin dağ, yol belirtisi ve kumaşın kenar deseni yön bulduran veya tanıtan somut gerçekleşmelerdir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Savaşçının, kumaşın veya sarığın ayırt edici bir işaretle donatılması belirli kuruluşlara bağlı eylemsel kullanımdır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Tanınmış bir kişinin belirgin bir bayrağa benzetilmesi ve yaklaşan son zamanı gösteren belirti, işaret çekirdeğinin uzantılarıdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyi tanınır kılan veya ona ulaşmayı sağlayan belirgin iz ve işaretlerin ortak çekirdeğini karşılar.","boundary_detail":"Dal bütün işaret türlerini sınırsızca kapsamaz; kaynakta anılan ayırt etme ve yol gösterme işlevli izlerle bunlara bağlı kullanımlarla sınırlıdır.","branch_image_ar":"أثر يميز الشيء ويهدي إليه","concept_gloss":"ayırt edici ve yol gösterici işaret","contextual_glosses":[{"applicability":"Askerlerin çevresinde toplandığı bayrak ya da yol bulmayı sağlayan belirgin dağ ve iz bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Görünürlük ile yöneltme ve tanıtma işlevini korur."},"facet_ids":["F002"],"text":"bayrak veya uzaktan seçilen kılavuz","usage_role":"contextual"},{"applicability":"Bir savaşçıya, kumaşa veya sarığa başkalarından ayıran görünür bir belirti ekleme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İşaretin sonradan konmasını ve ayırt etme amacını korur."},"facet_ids":["F003"],"text":"tanıtıcı işaret koymak","usage_role":"contextual"},{"applicability":"Belirli bir son zamanın yaklaştığını haber veren gösterge bağlamına özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir olayın yakınlığını gösterme işlevini korur."},"facet_ids":["F004"],"text":"yaklaşmayı gösteren belirti","usage_role":"explanatory"}],"definition":"Bir şeyi başkalarından ayıran, tanınmasını sağlayan veya ona götüren belirgin iz ya da işarettir. Bayrak, uzaktan seçilen dağ, yol belirtisi, kumaş kenarı ve sonradan konan tanıtıcı izler bu işlevin farklı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir nesneyi veya kişiyi başkalarından ayırıp tanınır kılan belirgin iz ya da işaret çekirdeği oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Bayrak, belirgin dağ, yol belirtisi ve kumaşın kenar deseni yön bulduran veya tanıtan somut gerçekleşmelerdir."},{"facet_id":"F003","role":"associated_use","statement":"Savaşçının, kumaşın veya sarığın ayırt edici bir işaretle donatılması belirli kuruluşlara bağlı eylemsel kullanımdır."},{"facet_id":"F004","role":"extension","statement":"Tanınmış bir kişinin belirgin bir bayrağa benzetilmesi ve yaklaşan son zamanı gösteren belirti, işaret çekirdeğinin uzantılarıdır."}],"identity_rationale":"Kaynak ifadesi, bir şeyi başkasından ayıran belirgin izi dalın ortak çekirdeği olarak açıkça destekler. Bayrak, belirgin dağ, yol belirtisi, kumaş deseni ve savaş işareti gibi örnekler bu çekirdeğin farklı gerçekleşmeleridir; tanınmış kişi ve son zaman belirtisi ise benzetme veya gösterme ilişkisine bağlı uzantılardır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ayırt edici işaret"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"bayrak, sancak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yol gösteren belirgin dağ"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"kumaşın kenar işareti veya deseni"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yol gösteren iz veya belirti"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"savaşta kendine ayırt edici işaret takmak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"kumaşı işaretlemek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"işaret olarak kullanılan kına"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"sarığı tanıtıcı bir biçimde sarmak"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"tanınmış ve öne çıkan kişi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"son saatin yaklaştığını gösteren belirti"}],"lexicalization_note":"Ayırt edici iz çıplak çekirdektir; savaşçı, kumaş, sarık ve belirli zaman göstergesiyle kurulan anlamlar kendi kuruluşlarına bağlı tutulur.","neighbor_coverage_note":"En yararlı karşılaştırmalar geçmişten kalan iz, bilerek konan tanıtıcı işaret ve fiziksel damga ile yapıldı; bayrak adayı yalnızca tek bir alt gerçekleşmeyi, öteki adaylar ise daha uzak renk veya biçim belirtilerini karşılar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda işaret önceden konabilir veya doğal bir kılavuz olabilir; komşu dalda iz, daha önceki bir varlık ya da olayın geride kalan sonucudur.","focus_only":"Odak dal, bilerek konan bayrak ve işaretlerin yanı sıra yön bulduran belirgin dağ gibi göstergeleri de kapsar.","gloss":"işaret ile kalıntı iz","neighbor_only":"Komşu dal, geçmişte var olmuş veya gerçekleşmiş bir şeyden geriye kalan izi özellikle gerektirir.","neighbor_ref":"root_000011/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da görünür bir izin başka bir şeyi tanıtması veya ona kanıt olması bakımından örtüşür."},{"boundary_match":"partial","distinction":"Komşu dalın çekirdeği işaretleme eylemine daha sıkı bağlıdır; odak dal ise konmuş işaretlerin yanında doğal kılavuzları ve bayrağı da adlandırır.","focus_only":"Odak dal doğal dağ işaretini, bayrağı, yol belirtisini ve kumaş kenarını da içine alan daha geniş bir gösterge alanına sahiptir.","gloss":"ayırt edici işaret koyma","neighbor_only":"Komşu dal özellikle atlara, varlıklara veya nesnelere tanıtma amacıyla işaret koyma eylemini öne çıkarır.","neighbor_ref":"root_000764/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığı başkalarından ayıracak görünür bir işaretle tanıtmayı kapsar."},{"boundary_match":"partial","distinction":"Damga bir yüzeye bilerek bırakılan fiziksel izdir; odak dalın işareti ise doğal veya yapılmış olabilir ve yön gösterme işlevi de taşıyabilir.","focus_only":"Odak dal işaret koyma dışında bayrak, dağ, yol kılavuzu ve kumaş deseni gibi bağımsız adları da kapsar.","gloss":"işaret ile damga","neighbor_only":"Komşu dal, hayvana veya nesneye yakma, kesme ya da benzeri yolla bırakılan bedensel ve maddi damgayı gerektirir.","neighbor_ref":"root_001650/B001","relation_type":"near_synonym","shared_zone":"Her iki dal görünür bir belirti aracılığıyla tanıtma ve ayırt etme işlevini paylaşır."}],"source_phrase_ar":"أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره (maqayis)؛ العلامة وهي معروفة (maqayis)؛ العلم الراية والجمع أعلام (maqayis;sihah;tahdhib)؛ العلم الجبل الطويل والجميع الأعلام (ayn)؛ العلم الجبل (sihah;mufradat)؛ المعلم الأثر يستدل به على الطريق (sihah;tahdhib)؛ علم الثوب ورقمه في أطرافه (sihah;tahdhib;mufradat)؛ أعلم الفارس إذا كانت له علامة في الحرب (maqayis;sihah;tahdhib)؛ العلام الحناء (maqayis;sihah;tahdhib;mufradat)؛ علمت عمتي أعلمها علما (tahdhib)","source_summary":"Kaynaklar ayırt edici izi ortak temel sayar ve bayrak, yüksek ya da belirgin dağ, yol göstergesi, kumaş kenarı, kına ve sonradan yerleştirilen tanıtıcı işaretleri bu temelde toplar. Tanınmış kişi ile yaklaşan son zamanın belirtisi de görünürlük ve gösterme işlevinden doğan uzantılardır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلامة والعلم والراية والجبل والمعلم ومعالم الطريق والحدود وعلم الثوب ورقمه وتعليم الفارس والثوب والقدح والعمامة والحناء إذا جعلت علامة","what_is_not_ar":"ليس هو إدراك العلم ولا اسم الخلق ولا شق الشفة العليا"},"support_links":["sup_4f20f93e3ae51afa3f14","sup_894d5ca19a5dfe791527","sup_bb89bebc77d2a2585d84"]},{"boundary":"Dal yaratılmış varlıkların bütünü veya sınıflarıyla sınırlıdır; bilme durumu ve bağımsız bir fiziksel işaret anlamına gelmez.","branch_kind":"bare","branch_ref":"root_001040/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:4:2:1","qac_word_ref":"96:4:2","surface_ar":"عَلَّمَ"}],"gloss":"evren ve bütün yaratılmışlar","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Evren ve içindeki yaratılmış varlıkların tamamı tek bir bütün olarak adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad, yaratılmışların tamamı yanında onların her bir cinsini veya sınıfını ayrı bir bütün olarak da gösterebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yaratılmış bütünün kendi yaratıcısına gösterge olması, adlandırmanın açıklayıcı dayanağı olarak sunulur."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yaratılmış varlıkların tümünü tek bir düzen veya bütün olarak anlatan temel kullanım için uygundur.","boundary_detail":"Dal yaratılmış varlıkların bütünü veya sınıflarıyla sınırlıdır; bilme durumu ve bağımsız bir fiziksel işaret anlamına gelmez.","branch_image_ar":"الخلق عالم يدل على صانعه","concept_gloss":"evren ve bütün yaratılmışlar","contextual_glosses":[{"applicability":"Sözün bütün evren yerine insan, görünmeyen varlıklar veya başka bir yaratık cinsi gibi ayrı sınıflara dağıtıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Her yaratık cinsinin ayrı bir bütün sayılması yönünü korur."},"facet_ids":["F002"],"text":"varlıkların her bir sınıfı","usage_role":"explanatory"}],"definition":"Yaratılmış olanların bütünü; bağlama göre evren ile içindekilerin tamamı veya yaratıkların ayrı ayrı sınıflarıdır. Bu bütünün yaratıcıyı gösteren bir belirti sayılması, adın açıklanan dayanağıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Evren ve içindeki yaratılmış varlıkların tamamı tek bir bütün olarak adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Ad, yaratılmışların tamamı yanında onların her bir cinsini veya sınıfını ayrı bir bütün olarak da gösterebilir."},{"facet_id":"F003","role":"associated_use","statement":"Yaratılmış bütünün kendi yaratıcısına gösterge olması, adlandırmanın açıklayıcı dayanağı olarak sunulur."}],"identity_rationale":"Kaynak ifadesi, dalı yaratılmışların bütünü, gök düzeni ve içindekiler ya da yaratıkların ayrı sınıfları olarak açıklar. Her sınıfın ve bütünün yaratıcıyı gösteren bir belirti sayılması adlandırmanın gerekçesidir; bilme eylemi veya somut işaret dalıyla özdeş değildir.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"evren veya yaratılmışlar bütünü"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bütün yaratıklar veya varlık sınıfları"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"evrenler, varlık dünyaları"}],"lexicalization_note":"Tanım, çıplak dalın evren, yaratılmışların bütünü ve varlık sınıfları anlamlarını verir; başka kuruluşlardan anlam aktarmaz.","neighbor_coverage_note":"Adayların çoğu hayvan bedenindeki renk ve işaretleri ya da ilgisiz özel adları anlatır; aynı kökün bilme ve işaret dalları adlandırma gerekçesini açıklasa da bu dalın yaratılmışlar bütünü sınırını keskinleştirecek bir karşıtlık oluşturmaz.","source_phrase_ar":"العالمون كل جنس من الخلق فهو في نفسه معلم وعلم (maqayis)؛ العالم الخلق والجمع العوالم (sihah)؛ العالمين رب الجن والإنس ورب الخلق كلهم (tahdhib)؛ العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به (mufradat)؛ أصناف الخلائق (mufradat)","source_summary":"Kaynaklar bu adı yaratılmışların bütünü için kullanır; kapsam bazen evren ve içindekilerin tamamı, bazen de yaratıkların her bir cinsi veya sınıfıdır. Bütünün kendi yaratıcısına işaret etmesi adlandırmayı açıklayan ortak bir düşüncedir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه العالم والعالمون بمعنى الخلق أو أصناف الخلائق أو كل جنس من الخلق لأنه معلم في نفسه ودال","what_is_not_ar":"ليس هو العلم بمعنى المعرفة ولا العلم بمعنى الراية أو الجبل"},"support_links":[]},{"boundary":"Belirti özellikle üst dudakta bulunur; genel çatlaklar, alt dudak ve ağız çevresindeki başka eğrilikler kapsam dışıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001040/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:4:2:1","qac_word_ref":"96:4:2","surface_ar":"عَلَّمَ"}],"gloss":"üst dudak yarığı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Üst dudakta bulunan yarık, dalın anatomik çekirdeğini oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Üst dudağı yarık insan veya üst dudak bölgesinde bu belirti bulunan deve, özelliği taşıyan varlık olarak nitelenir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Birinin üst dudağını yarmak, anatomik sonucun oluşturulmasını bildiren eylemsel kullanımdır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya devenin üst dudak bölgesindeki belirgin yarığı adlandıran temel kullanım için uygundur.","boundary_detail":"Belirti özellikle üst dudakta bulunur; genel çatlaklar, alt dudak ve ağız çevresindeki başka eğrilikler kapsam dışıdır.","branch_image_ar":"شق ظاهر في الشفة العليا","concept_gloss":"üst dudak yarığı","contextual_glosses":[{"applicability":"Bir insanı veya deveyi üst dudak bölgesindeki yarıkla niteleyen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Özelliğin taşıyıcıda bulunmasını ve anatomik yerini korur."},"facet_ids":["F002"],"text":"üst dudağı yarık","usage_role":"contextual"},{"applicability":"Bir kişinin üst dudağında yarık oluşturma eylemini anlatan kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemi, etkilenen kişiyi ve üst dudak sınırını korur."},"facet_ids":["F003"],"text":"üst dudağını yarmak","usage_role":"contextual"}],"definition":"İnsanın üst dudağında veya devenin üst dudak bölgesinde bulunan belirgin yarıktır. Aynı dal, bu özelliği taşıyanı niteleyen biçimi ve üst dudağı yarma eylemini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Üst dudakta bulunan yarık, dalın anatomik çekirdeğini oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Üst dudağı yarık insan veya üst dudak bölgesinde bu belirti bulunan deve, özelliği taşıyan varlık olarak nitelenir."},{"facet_id":"F003","role":"associated_use","statement":"Birinin üst dudağını yarmak, anatomik sonucun oluşturulmasını bildiren eylemsel kullanımdır."}],"identity_rationale":"Kaynak ifadesi dalı açıkça üst dudaktaki yarıkla sınırlar; insanın üst dudağının yarılmış olması, devenin üst dudak bölgesindeki aynı belirti ve üst dudağı yarma eylemi bu kimliği doğrular. Genel yarılma anlamı veya alt dudaktaki bir biçim bozukluğu bu dala dahil değildir.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"üst dudaktaki yarık"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"üst dudağı yarık kişi veya deve"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"üst dudağını yarmak"}],"lexicalization_note":"Üst dudak yarığı dalın temelidir; yarıklı kişi veya deve nitelemesi ile üst dudağı yarma eylemi ilgili biçimlere bağlı tutulur.","neighbor_coverage_note":"Genel yarılma dalı süreç ve kapsam farkını, ağız eğriliği dalı ise yakın anatomik karışmayı açıklar; öteki adaylar kırık iyileşmesi, hayvan yapısı veya daha uzak ayrılma türleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yer ve sonuç bakımından üst dudağa özelleşmiş anatomik bir addır; komşu dal ise nesne ve yüzey türü bakımından geniş bir yarılma eylemidir.","focus_only":"Odak dal belirli bir anatomik yerde, üst dudakta bulunan yarığı ve bu yarıkla niteleneni bildirir.","gloss":"üst dudak yarığı ile genel yarılma","neighbor_only":"Komşu dal nesne, deri, toprak, dağ ve başka yüzeylerdeki genel yarılma ve açılma sürecini kapsar.","neighbor_ref":"root_000807/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda bir yüzeyin ayrılmasıyla oluşan yarık düşüncesi bulunur."},{"boundary_match":"field_only","distinction":"Yarık, dokuda açılma veya ayrılmadır; eğrilik ise bir bölümün yana yönelmiş biçimidir ve üst dudakta bir açıklık gerektirmez.","focus_only":"Odak dalda üst dudak dokusunun yarılmış olması gerekir.","gloss":"dudak yarığı ile ağız eğriliği","neighbor_only":"Komşu dalda ağız, dudak veya gözün bir yana eğri oluşu vardır; doku yarığı gerekmez.","neighbor_ref":"root_000866/B003","relation_type":"same_field","shared_zone":"İki dal yüz ve ağız çevresindeki belirgin bir yapısal özelliği adlandırır."}],"source_phrase_ar":"العلم الشق في الشفة العليا والرجل أعلم (maqayis)؛ الأعلم الذي انشقت شفته العليا (ayn)؛ علم الرجل يعلم علما إذا صار أعلم وهو المشقوق الشفة العليا (sihah)؛ علمت الرجل أعلمه علما إذا شققت شفته العليا (tahdhib)؛ البعير يقال له أعلم لعلم في مشفره الأعلى (tahdhib)؛ الشق في الشفة العليا علم (mufradat)","source_summary":"Kaynaklar yarığın yerini üst dudak olarak ortak biçimde sınırlar ve yarıklı insanı bu özellikle niteler. Toplu tanıklık, devenin üst dudak bölgesindeki karşılığını ve üst dudağı yarma eylemini de aynı dalda gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه العلم والشق في الشفة العليا ووصف الرجل أو البعير بالأعلم إذا كان الشق أو العلم في الموضع الأعلى","what_is_not_ar":"ليس هو العلم بمعنى المعرفة ولا العلامة الموضوعة اختيارا ولا الشق في الشفة السفلى"},"support_links":[]},{"boundary":"Deniz ile suyu bol kuyu tek bir ara nesnede birleştirilmez; bunlar aynı biçimin kaynaklarda verilen iki ayrı sözlük karşılığıdır.","branch_kind":"bare","branch_ref":"root_001040/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:4:2:1","qac_word_ref":"96:4:2","surface_ar":"عَلَّمَ"}],"gloss":"deniz ya da suyu bol kuyu","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dal, aynı adın iki ayrı su varlığına verilen sözlük karşılıklarını birlikte kaydeder."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir kaynak karşılığında ad, geniş tuzlu su kütlesi olan denizi gösterir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Diğer ve daha yaygın kaynak karşılığında ad, suyu çok olan kuyuyu gösterir."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözlük biçiminin kaynaklarda verilen iki ayrı karşılığını eksiltmeden birlikte göstermek gerektiğinde kullanılır.","boundary_detail":"Deniz ile suyu bol kuyu tek bir ara nesnede birleştirilmez; bunlar aynı biçimin kaynaklarda verilen iki ayrı sözlük karşılığıdır.","branch_image_ar":"ماء كثير مجتمع في عيلم","concept_gloss":"deniz ya da suyu bol kuyu","contextual_glosses":[{"applicability":"Sözlük biçiminin geniş su kütlesi karşılığıyla kullanıldığı tanıklığa özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı biçim için tanıklanan suyu bol kuyu karşılığını dışarıda bırakır.","preserves":"Deniz karşılığını doğal ve doğrudan biçimde korur."},"facet_ids":["F002"],"text":"deniz","usage_role":"contextual"},{"applicability":"Sözlük biçiminin bol su içeren kuyu karşılığıyla kullanıldığı tanıklıklara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı biçim için tanıklanan deniz karşılığını dışarıda bırakır.","preserves":"Kuyu türünü ve suyunun çokluğu koşulunu korur."},"facet_ids":["F003"],"text":"suyu bol kuyu","usage_role":"contextual"}],"definition":"Aynı sözlük biçiminin bir kullanımda denizi, başka bir kullanımda ise suyu bol kuyuyu adlandırmasıdır. İki karşılık, genel bir su birikintisi anlamında kaynaştırılmaz.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dal, aynı adın iki ayrı su varlığına verilen sözlük karşılıklarını birlikte kaydeder."},{"facet_id":"F002","role":"source_variant","statement":"Bir kaynak karşılığında ad, geniş tuzlu su kütlesi olan denizi gösterir."},{"facet_id":"F003","role":"source_variant","statement":"Diğer ve daha yaygın kaynak karşılığında ad, suyu çok olan kuyuyu gösterir."}],"identity_rationale":"Kaynak ifadesi tek bir su birikimi türü tanımlamaz; aynı sözlük biçimi için deniz ve suyu bol kuyu olmak üzere iki ayrı karşılık verir. Dal korunabilir, ancak geçici çerçevedeki ortak su kütlesi görüntüsü yerine bu açık seçeneklilik tanıma yazılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"deniz"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"suyu bol kuyu"}],"lexicalization_note":"Tanım çıplak sözlük biçiminin deniz ve suyu bol kuyu karşılıklarını ayrı ayrı korur; bunlardan genel bir su birikintisi anlamı türetmez.","neighbor_coverage_note":"Deniz karşılığını açıklayan geniş su dalı ile kuyu çevresindeki bol su dalı seçildi; diğer adaylar gölet, artık su, taşkın veya su tutan arazi gibi farklı taşıyıcı ve süreçlere bağlıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Örtüşme yalnızca deniz karşılığındadır; odak dalın kuyu seçeneği komşuda bulunmaz, komşunun büyük ırmak ve genel su genişliği ise odak dalın tanımına girmez.","focus_only":"Odak dal aynı sözlük biçiminin suyu bol kuyu karşılığını da bağımsız bir seçenek olarak taşır.","gloss":"deniz ve geniş su","neighbor_only":"Komşu dal deniz yanında büyük ırmak ve farklı büyüklükte su alanlarına uzanan genel bir geniş su kapsamına sahiptir.","neighbor_ref":"root_000086/B001","relation_type":"near_synonym","shared_zone":"Odak dalın deniz karşılığı, komşu dalın geniş ve çok su çekirdeğiyle örtüşür."},{"boundary_match":"partial","distinction":"Odak dal suyu taşıyan kuyuyu niteler; komşu dal ise kuyudan dökülen suyu ve taşma sürecini merkez alır.","focus_only":"Odak dal kuyunun kendisini suyunun bol olması koşuluyla adlandırır.","gloss":"suyu bol kuyu ile kuyu suyu","neighbor_only":"Komşu dal kuyudaki kovadan dökülen veya havuza taşan suyu, kokusunu ve taşma olayını anlatır.","neighbor_ref":"root_001077/B003","relation_type":"near_neighbor","shared_zone":"İki dal kuyu çevresinde suyun çokluğu ve görünür birikimiyle ilişkilidir."}],"source_phrase_ar":"العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء (maqayis)؛ العيلم الركية الكثيرة الماء (sihah)؛ العيلم البئر الكثيرة الماء (tahdhib)","source_summary":"Toplu tanıklık iki karşılığı yan yana verir: bir aktarım sözcüğü deniz olarak açıklar, öteki tanıklıklar ise suyu bol kuyu anlamını destekler. Kaynaklara özgü ayrı claim kimlikleri bulunmadığı için bu karşıtlık ortak özet içinde, atıf uydurulmadan korunur.","sources":["MQ","SI","TA"],"what_is_ar":"يدخل فيه العيلم بمعنى البحر أو البئر الكثيرة الماء","what_is_not_ar":"ليس هو العالمين ولا العلم ولا العلامة ولا العيلم بمعنى آخر غير مائي"},"support_links":[]},{"boundary":"Çekirdek yırtıcı kuş adıdır; çevik ve zeki erkek nitelemesi yalnızca bu addan türeyen biçime bağlıdır.","branch_kind":"bare","branch_ref":"root_001040/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:4:2:1","qac_word_ref":"96:4:2","surface_ar":"عَلَّمَ"}],"gloss":"doğan veya atmaca türü yırtıcı kuş","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ad, doğan veya atmaca türünden avcı bir kuşu gösterir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuş adından türeyen insan nitelemesi, çevik ve zeki bir erkeği belirtir."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın temel kuş adını iki kaynak karşılığı arasındaki seçenekliliği koruyarak açıklamak için uygundur.","boundary_detail":"Çekirdek yırtıcı kuş adıdır; çevik ve zeki erkek nitelemesi yalnızca bu addan türeyen biçime bağlıdır.","branch_image_ar":"طائر جارح يسمى العلام","concept_gloss":"doğan veya atmaca türü yırtıcı kuş","contextual_glosses":[{"applicability":"Kuş adından türemiş insan nitelemesinin kullanıldığı bağlama özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan oluşu ile çeviklik ve zekâ niteliklerini birlikte korur."},"facet_ids":["F002"],"text":"çevik ve zeki adam","usage_role":"contextual"}],"definition":"Doğan veya atmaca türünden bir yırtıcı kuş adıdır. Bu kuş adından türetilen bir niteleme, çevik ve zeki bir erkeği anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ad, doğan veya atmaca türünden avcı bir kuşu gösterir."},{"facet_id":"F002","role":"associated_use","statement":"Kuş adından türeyen insan nitelemesi, çevik ve zeki bir erkeği belirtir."}],"identity_rationale":"Kaynak ifadesi temel adı doğan veya atmaca türünden yırtıcı kuş için verir ve geçici dal görüntüsünü doğrular. Çevik ve zeki erkek nitelemesi ise kuş adından türetilmiş ayrı bir biçimdir; kuşun tanımına doğrudan katılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"doğan veya atmaca"},{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"çevik ve zeki adam"}],"lexicalization_note":"Çıplak dal doğan veya atmaca türünden kuş adını tanımlar; insan nitelemesi türemiş bir sözcüksel uzantı olarak bağımlı tutulur.","neighbor_coverage_note":"Yırtıcı kuş sınıfında en yakın iki aday seçildi; diğer adaylar kanat çırpma, beslenme, farklı hayvan adları veya yalnızca uzak bir doğan ilişkisi taşır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Aynı kuş alanını paylaşsalar da komşu dal renk ve ara tür özellikleriyle daha dar bir kuşu adlandırır; odak dalın türemiş insan nitelemesi de komşuda yoktur.","focus_only":"Odak dal doğan veya atmaca karşılığı taşıyan kuş adını ve ondan türeyen insan nitelemesini içerir.","gloss":"yırtıcı kuş adları","neighbor_only":"Komşu dal mavi renkli, doğan ile atmaca arasında tanımlanan veya beyaz doğan sayılan daha özel bir kuş adıdır.","neighbor_ref":"root_000631/B002","relation_type":"same_field","shared_zone":"Her iki dal doğan ve atmaca çevresindeki avcı kuş adlandırmaları alanındadır."},{"boundary_match":"partial","distinction":"Odak dalda zekâ kuştan türetilen insan niteliğinde belirginleşir; komşuda ise doğrudan belirli doğanların özelliğidir.","focus_only":"Odak dal doğan veya atmaca türünü genel bir adla karşılar ve bu addan insan nitelemesi türetir.","gloss":"doğan adı ile zeki doğan nitelemesi","neighbor_only":"Komşu dal özellikle zeki ve keskin bakışlı doğanlara verilen bir adı belirtir.","neighbor_ref":"root_001375/B006","relation_type":"near_neighbor","shared_zone":"İki dal doğan türünden yırtıcı kuşları adlandırır ve zekâ çağrışımını paylaşır."}],"source_phrase_ar":"العلام الصقر؛ العلامي الرجل الخفيف الذكي مأخوذ من العلام؛ العلام الباشق (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık temel adı doğan veya atmaca türünden kuş için verir ve türemiş biçimi çevik, zeki erkek olarak açıklar."}],"source_summary":"Dal tek bir sözlük tanıklığında yırtıcı kuş adı ile bu addan türetilmiş çevik ve zeki erkek nitelemesini birlikte sunar.","sources":["TA"],"what_is_ar":"يدخل فيه العلام بمعنى الصقر أو الباشق وما نسب إليه من العلامي","what_is_not_ar":"ليس هو العلام بمعنى الحناء ولا العلامة ولا العالم"},"support_links":[]},{"boundary":"Dal yalnızca erkek sırtlanı adlandırır; başka erkek hayvan adları ve benzer sesli su veya kuş adları kapsam dışıdır.","branch_kind":"bare","branch_ref":"root_001040/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:4:2:1","qac_word_ref":"96:4:2","surface_ar":"عَلَّمَ"}],"gloss":"erkek sırtlan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırılan canlı, cinsiyeti erkek olan sırtlandır."}}],"root_ar":"ع ل م","root_id":"root_001040","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvanın türünü ve erkek oluşunu birlikte veren bütün bağlamlarda tam karşılıktır.","boundary_detail":"Dal yalnızca erkek sırtlanı adlandırır; başka erkek hayvan adları ve benzer sesli su veya kuş adları kapsam dışıdır.","branch_image_ar":"ذكر الضباع يسمى العيلام","concept_gloss":"erkek sırtlan","definition":"Erkek sırtlanı adlandıran yalın bir hayvan adıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırılan canlı, cinsiyeti erkek olan sırtlandır."}],"identity_rationale":"Kaynak ifadesinin iki tanıklığı da sözcüğü doğrudan erkek sırtlan olarak açıklar. Geçici dal görüntüsü bu yalın hayvan adıyla tam uyumludur ve başka bir tür, özellik veya mecaz eklemeyi gerektirmez.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"erkek sırtlan"}],"lexicalization_note":"Tanım çıplak hayvan adını erkek sırtlanla sınırlar ve başka türlere ya da bağlı kuruluşlara genişletmez.","neighbor_coverage_note":"Erkek sırtlanı aynı sınırlarla adlandıran aday tam eş anlamlı olarak seçildi; diğer adaylar kurt, erkek domuz, aslan, kuş veya daha geniş hayvan sınıflarıdır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Anlam çekirdeği, hayvan türü ve cinsiyet sınırı aynıdır; ayrım yalnızca kullanılan sözlük biçimindedir.","focus_only":null,"gloss":"erkek sırtlan","neighbor_only":null,"neighbor_ref":"root_001068/B007","relation_type":"synonym","shared_zone":"Her iki dal da hiçbir ek koşul getirmeden erkek sırtlanı adlandırır."}],"source_phrase_ar":"العيلام الذكر من الضباع (sihah)؛ العيلام الضبعان وهو ذكر الضباع (tahdhib)","source_summary":"Kaynaklar sözcüğün erkek sırtlanı adlandırdığı konusunda birleşir ve ek bir anlam ayrımı bildirmez.","sources":["SI","TA"],"what_is_ar":"يدخل فيه العيلام بمعنى ذكر الضباع","what_is_not_ar":"ليس هو العيلم البئر الكثيرة الماء ولا العلامة ولا العلم"},"support_links":[]},{"boundary":"Dal, genel kırma ya da her türlü kesme değil, sert bir ucu parça parça eksilterek biçimlendirme ve düzeltmeyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_001252/B001","candidate_links":[{"candidate_id":"cand_6b44d9e2df2e3f556c84","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَلَم","morph_features":"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:4:3:3","qac_word_ref":"96:4:3","surface_ar":"قَلَمِ"}],"gloss":"sert ucu kesip yontarak düzeltme ve çıkan parça","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sert bir şeyin ucundan parçalar art arda kesilir veya yontulur ve uç düzeltilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tırnağın ucundan kesilerek düşen küçük parça, işlemin ortaya çıkardığı sonuç olarak adlandırılır."}}],"root_ar":"ق ل م","root_id":"root_001252","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İşlemi, sert uç üzerindeki düzeltme amacını ve işlemle ayrılan parçayı birlikte anlatan kapsayıcı karşılıktır.","boundary_detail":"Dal, genel kırma ya da her türlü kesme değil, sert bir ucu parça parça eksilterek biçimlendirme ve düzeltmeyle sınırlıdır.","branch_image_ar":"قص الصلب وبريه للتسوية","concept_gloss":"sert ucu kesip yontarak düzeltme ve çıkan parça","contextual_glosses":[{"applicability":"Eylemin doğrudan tırnağa uygulandığı cümlelerde doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Başka sert şeylerin yontulmasını ve kesilen parçanın adını kapsamaz.","preserves":"Tırnağın ucundan keserek parça alma işlemini korur."},"facet_ids":["F001"],"text":"tırnağı kesmek","usage_role":"contextual"},{"applicability":"Tırnak dışındaki sert bir şeyin ucunun biçimlendirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tırnak örneğini ve işlem sonunda ayrılan parçanın adlandırılmasını kapsamaz.","preserves":"Parça parça eksilterek biçimi düzeltme işlemini korur."},"facet_ids":["F001"],"text":"yontarak düzeltmek","usage_role":"contextual"}],"definition":"Tırnak gibi sert bir şeyin ucundan küçük parçaları art arda kesip yontarak biçimini düzeltme işlemidir; işlem sonunda uçtan ayrılan küçük parça da bu dala bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sert bir şeyin ucundan parçalar art arda kesilir veya yontulur ve uç düzeltilir."},{"facet_id":"F002","role":"extension","statement":"Tırnağın ucundan kesilerek düşen küçük parça, işlemin ortaya çıkardığı sonuç olarak adlandırılır."}],"identity_rationale":"Kaynak ifadesi, tırnak gibi sert bir şeyin ucundan parçalar kesip yontarak onu düzeltme işlemini ve bu işlemle ayrılan küçük parçayı birlikte verir. Dal çerçevesi bu işlem, amaç ve sonuç ilişkisini doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tırnağı kesmek; sert bir şeyi yontarak düzeltmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kesilen tırnak parçası"}],"lexicalization_note":"Çıplak dal, sert bir şeyi kesip yontarak düzeltme anlamını taşır; yazı aracı, kura çubuğu veya özel araç adları bu tanıma katılmaz.","neighbor_coverage_note":"Adayların tümü değerlendirildi; en yakın karışma genel kesip artık ayırma dalıyla olduğundan yalnız bu sınır yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda kesme, sert bir ucu art arda eksiltip biçimlendirme amacına bağlıdır; karşı dalda ise kesip ayırma daha geniştir ve uç düzeltme koşulu yoktur.","focus_only":"Sert bir ucun küçük parçalar alınarak düzeltilmesi ve çıkan uç parçası bu dala özgüdür.","gloss":"kesip artık parçayı ayırma","neighbor_only":"Karşı dal, araç ya da dişle yapılan daha genel kesme ve artık ayırma işlemlerini kapsar.","neighbor_ref":"root_001217/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir şeyden parça kesilerek ana gövdeden ayrılır."}],"source_phrase_ar":"تسوية شيء عند بريه وإصلاحه (maqayis)؛ قلمت الظفر وقلمته (maqayis)؛ القلامة ما يسقط من الظفر إذا قلم (maqayis)؛ القلم قطع الظفر بالقلمين وبالقلم (ayn;tahdhib)؛ قلمت ظفري وقلمت أظفاري والقلامة ما سقط منه (sihah)؛ قلمت الشيء بريته (tahdhib)؛ أصل القلم القص من الشيء الصلب كالظفر وكعب الرمح والقصب (mufradat)","source_summary":"Kaynaklar, özellikle tırnak kesmeyi örnek vererek sert bir uçtan parçaları art arda alma, ucu yontup düzeltme ve kesilen parçayı adlandırma noktalarında birleşir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"قلم الظفر وبري الشيء وقطع الشيء شيئا بعد شيء والقلامة المقطوعة","what_is_not_ar":"القلم الذي يكتب به؛ القدح للقرعة؛ القَلّام النبت"},"support_links":["sup_bb89bebc77d2a2585d84"]},{"boundary":"Bu dal gerçek bir tırnak kesme eylemi değil, yalnızca belirli bir söz öbeğiyle kurulan güçsüzlük nitelemesidir.","branch_kind":"collocation","branch_ref":"root_001252/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَلَم","morph_features":"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:4:3:3","qac_word_ref":"96:4:3","surface_ar":"قَلَمِ"}],"gloss":"tırnağı kesilmiş gibi güçsüz","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güçsüz kişi, tırnağı kesilmiş veya körelmiş olma imgesi üzerinden nitelenir."}}],"root_ar":"ق ل م","root_id":"root_001252","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıbın tırnak imgesini ve kişi hakkındaki güçsüzlük yargısını birlikte koruyan karşılıktır.","boundary_detail":"Bu dal gerçek bir tırnak kesme eylemi değil, yalnızca belirli bir söz öbeğiyle kurulan güçsüzlük nitelemesidir.","branch_image_ar":"ظفر مقلوم يصير صورة للضعف","concept_gloss":"tırnağı kesilmiş gibi güçsüz","contextual_glosses":[{"applicability":"Tırnak imgesinin ayrıca açıklanmasının gerekmediği akıcı cümlelerde kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kesilmiş ya da körelmiş tırnak üzerinden kurulan özel benzetmeyi yitirir.","preserves":"Kişi hakkında verilen temel güçsüzlük yargısını korur."},"facet_ids":["F001"],"text":"güçsüz","usage_role":"contextual"}],"definition":"Bir kişiyi, tırnağı kesilmiş ya da körelmiş gibi tasarlayarak güçsüz ve etkisiz diye niteleyen kalıplaşmış bir anlatımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güçsüz kişi, tırnağı kesilmiş veya körelmiş olma imgesi üzerinden nitelenir."}],"identity_rationale":"Kaynak ifadesi güçsüz kişiyi, tırnağı kesilmiş veya keskinliğini yitirmiş gibi gösteren kalıpla niteler. Dal çerçevesi hem güçsüzlük yargısını hem de onu taşıyan tırnak imgesini korur.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tırnağı kesilmiş ya da körelmiş gibi güçsüz"}],"lexicalization_note":"Anlam yalnız verilen tırnaklı niteleme kalıbına bağlıdır; kökün tek başına genel olarak güçsüzlük bildirdiği sonucuna genişletilemez.","neighbor_coverage_note":"Zayıflık alanındaki bütün adaylar karşılaştırıldı; genel güç azalması dalı, özel tırnak imgesinin sınırını en açık gösteren adaydır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal kalıplaşmış ve imgeli bir kişi sıfatıdır; karşı dal ise imgeye bağlı olmayan genel güçsüzlük, gevşeme ve güçsüzleştirme alanına sahiptir.","focus_only":"Güçsüzlük yalnız kesilmiş veya körelmiş tırnak imgesi taşıyan özel bir kişi nitelemesiyle anlatılır.","gloss":"gücün azalması","neighbor_only":"Karşı dal insan, beden, kemik, iş ve tasarı gibi birçok şeyde güç azalmasını ve güçsüzleştirmeyi kapsar.","neighbor_ref":"root_001687/B001","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişi bakımından güç ve etkideki yetersizliği anlatabilir."}],"source_phrase_ar":"يقال للضعيف هو مقلوم الأظفار (maqayis)؛ يقال للضعيف مقلوم الظفر وكليل الظفر (sihah)","source_summary":"Kaynaklar aynı kalıbı güçsüz kişi için verir ve kesilmiş tırnak imgesini körelmiş tırnak anlatımıyla yan yana getirir.","sources":["MQ","SI"],"what_is_ar":"وصف الضعيف بمقلوم الظفر أو مقلوم الأظفار","what_is_not_ar":"قص الظفر الحقيقي إذا لم يكن وصف ضعف؛ القلم الكاتب؛ القدح"},"support_links":[]},{"boundary":"Merkez yazı yazmaya yarayan araçtır; araç kabı yalnız ilişkili türemiş bir ad, yazma eylemi ve yazı sıvısı ise ayrı kavramlardır.","branch_kind":"bare","branch_ref":"root_001252/B003","candidate_links":[{"candidate_id":"cand_8e4a96727f27458aa686","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَلَم","morph_features":"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:4:3:3","qac_word_ref":"96:4:3","surface_ar":"قَلَمِ"}],"gloss":"yazı yazma aracı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yontularak hazırlanmış araç, bir yüzeye yazı yazmak için kullanılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yazı araçlarını bir arada tutan kap, merkezdeki araç adına bağlı türemiş bir birimle adlandırılır."}}],"root_ar":"ق ل م","root_id":"root_001252","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın merkezindeki yazı aracını doğal biçimde karşılar; bu araçların kabı ayrı bir ilişkili kullanımdır.","boundary_detail":"Merkez yazı yazmaya yarayan araçtır; araç kabı yalnız ilişkili türemiş bir ad, yazma eylemi ve yazı sıvısı ise ayrı kavramlardır.","branch_image_ar":"عود الكتابة المبرّى","concept_gloss":"yazı yazma aracı","contextual_glosses":[{"applicability":"Aracın çubuk biçimi ile yontularak hazırlanmasını özellikle belirtmek gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yazma işlevini, çubuk biçimini ve yontulmuş olma özelliğini korur."},"facet_ids":["F001"],"text":"yontulmuş yazı çubuğu","usage_role":"explanatory"},{"applicability":"Yalnız türemiş kap adının geçtiği cümlelerde kullanılacak bağlama bağlı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kabın yazı araçlarını bir arada tutma işlevini açıkça korur."},"facet_ids":["F002"],"text":"yazı araçlarını taşıyan kap","usage_role":"contextual"}],"definition":"Yontularak hazırlanmış, yazı yazmaya yarayan bir çubuk veya araçtır. Bu araçların topluca konduğu kap için de ondan türemiş ayrı bir ad bulunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yontularak hazırlanmış araç, bir yüzeye yazı yazmak için kullanılır."},{"facet_id":"F002","role":"associated_use","statement":"Yazı araçlarını bir arada tutan kap, merkezdeki araç adına bağlı türemiş bir birimle adlandırılır."}],"identity_rationale":"Kaynak ifadesinin merkezi, yontularak hazırlanan ve yazıda kullanılan araçtır; aynı kanıt ayrıca bu araçları taşıyan kabın türemiş adını verir. Dal kullanılabilir, ancak kap anlamı yazı aracının kurucu özelliği değil, ona bağlı ayrı bir kullanım olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yazı yazma aracı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yazı araçlarını taşıyan kap"}],"lexicalization_note":"Çıplak dal yazı yazmaya yarayan aracı karşılar; kura çubuğu, kesici araç veya yalnız özel bir söz öbeğinde görülen anlamlar buna eklenmez.","neighbor_coverage_note":"Yazma, yazı sıvısı, yazdırma ve sivri araç alanındaki adaylar değerlendirildi; araç ile yazı sıvısı ayrımı en yararlı sınır olarak seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dal yazıyı taşıyıp yüzeye süren araçtır; karşı dal ise araç tarafından kullanılan sıvı ve bu sıvının kabıdır, dolayısıyla birbirlerinin yerine geçmezler.","focus_only":"Bu dal yazıyı yüzeye aktaran somut çubuk veya aracı adlandırır.","gloss":"yazı sıvısı","neighbor_only":"Karşı dal yazı aracına alınan ve yüzeyde iz bırakan yazı sıvısını ve onun kabını adlandırır.","neighbor_ref":"root_000287/B003","relation_type":"same_field","shared_zone":"Her iki dal yazı yazma etkinliğinde birlikte kullanılan araç ve gereçleri kapsar."}],"source_phrase_ar":"سمي القلم قلما لأنه يقلم منه كما يقلم من الظفر (maqayis)؛ الأقلام جماعة القلم (ayn)؛ أقلامهم التي كانوا يكتبون بها التوراة (ayn)؛ القلم الذي يكتب به (sihah)؛ المقلمة وعاء الأقلام (sihah)؛ القلم الذي يكتب به وإنما سمي قلما لأنه قلم مرة بعد مرة (tahdhib)؛ خص ذلك بما يكتب به وجمعه أقلام (mufradat)","source_summary":"Kaynaklar yazı aracının yontulup tekrar tekrar düzeltilmesinden hareketle adlandırıldığını, çoğul kullanımını ve yazı araçlarını taşıyan kap adını birlikte aktarır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"القلم الذي يكتب به والأقلام ومقلمة الأقلام","what_is_not_ar":"قداح القرعة؛ القلم بمعنى الجلم؛ القَلّام النبت"},"support_links":["sup_9a6be11e6bf6a3ca03c4"]},{"boundary":"Dal, yazı aracı ya da sıradan ok değil, seçim veya paylaştırma için kurada kullanılan işaretli nesneyle sınırlıdır.","branch_kind":"bare","branch_ref":"root_001252/B004","candidate_links":[{"candidate_id":"cand_343c5ab6bc6f197cc5ae","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَلَم","morph_features":"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:4:3:3","qac_word_ref":"96:4:3","surface_ar":"قَلَمِ"}],"gloss":"işaretli kura çubuğu veya oku","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İşaretli bir çubuk veya ok, kura yoluyla seçim ya da pay belirlemek için hareket ettirilir."}}],"root_ar":"ق ل م","root_id":"root_001252","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Nesnenin ayırt edici işaretini, çubuk ya da ok biçimini ve kura işlevini birlikte korur.","boundary_detail":"Dal, yazı aracı ya da sıradan ok değil, seçim veya paylaştırma için kurada kullanılan işaretli nesneyle sınırlıdır.","branch_image_ar":"قدح مبرّى يلقى للقرعة","concept_gloss":"işaretli kura çubuğu veya oku","contextual_glosses":[{"applicability":"Nesnenin ok biçiminin önemli olmadığı genel kura bağlamlarında doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Nesnenin ok veya başka bir kura payı biçiminde olabilmesini açıkça göstermez.","preserves":"Kurada kullanılan işaretli somut nesne olma özelliğini korur."},"facet_ids":["F001"],"text":"kura çubuğu","usage_role":"contextual"}],"definition":"Üzerine ayırt edici işaret konan ve insanlar arasında seçim ya da pay belirlemek amacıyla kurada kullanılan çubuk, ok veya benzeri nesnedir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İşaretli bir çubuk veya ok, kura yoluyla seçim ya da pay belirlemek için hareket ettirilir."}],"identity_rationale":"Kaynak ifadesi, üzerine işaret konup insanlar arasında kura çekmek için hareket ettirilen çubuk, ok veya benzeri pay nesnesini açıkça tanımlar. Dal çerçevesi nesnenin biçim çeşitlerini ve kura işlevini doğru biçimde birleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kura için kullanılan işaretli çubuk veya ok"}],"lexicalization_note":"Çıplak dal kura için kullanılan çubuk veya ok anlamını taşır; kura çekme eylemi, oyun oynayan kişi veya çubukları tutan kap bu anlama katılmaz.","neighbor_coverage_note":"Ok, oyun, kura kabı ve kura eylemi adayları karşılaştırıldı; nesne ile işlem ayrımını gösteren kura eylemi dalı en açıklayıcı komşudur.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal uygulamada kullanılan somut nesnedir; karşı dal ise nesneyle yürütülen kura işlemi ve ondan çıkan sonuçtur.","focus_only":"Bu dal kurada kullanılan işaretli çubuk, ok veya pay nesnesini adlandırır.","gloss":"kuraya başvurma","neighbor_only":"Karşı dal, kura çekme ve kuraya katılma eylemlerini, ayrıca kura sonucunda çıkan payı kapsar.","neighbor_ref":"root_000754/B003","relation_type":"near_neighbor","shared_zone":"İki dal da kişiler arasında kura yoluyla seçim veya paylaştırma yapılan aynı uygulamaya bağlıdır."}],"source_phrase_ar":"شبه القدح به فقيل قلم؛ يلقون أقلامهم (maqayis)؛ القلم السهم الذي يجال به بين القوم (ayn)؛ القلم الزلم (sihah)؛ الأقلام ها هنا القداح جعلوا عليها علامات على جهة القرعة (tahdhib)؛ بالقدح الذي يضرب به وجمعه أقلام (mufradat)","source_summary":"Kaynaklar nesneyi çubuk, ok ve kura payı biçimleriyle anlatır; ortak çekirdek, işaretlenip insanlar arasında kura için kullanılmasıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"القدح أو السهم أو الزلم المستعمل في القرعة والمساهمة","what_is_not_ar":"القلم الذي يكتب به إلا عند القول المختلف في أقلام آل عمران؛ القلم بمعنى الجلم"},"support_links":["sup_4f20f93e3ae51afa3f14"]},{"boundary":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_kind":"bare","branch_ref":"root_001252/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَلَم","morph_features":"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:4:3:3","qac_word_ref":"96:4:3","surface_ar":"قَلَمِ"}],"gloss":"özel adlandırma kümesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kullanım erkek devenin üreme organının çengelli ucunu adlandırır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başka bir kullanım aynı organı saran kılıfı adlandırır ve uç anlamıyla aynı referente sahip değildir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir başka kullanım mızrağın boğumlarını veya mızrak ile kamışın dip bölümünü adlandırır."}}],"root_ar":"ق ل م","root_id":"root_001252","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bu karşılık, kanıttaki sınırlı veya biçime bağlı adlandırma kümesini güvenli biçimde etiketler; tek ve birleşik bir sözlük anlamı değildir.","boundary_detail":"Bu kayıt genel kök anlamı gibi genişletilmemeli, içindeki öğeler birbirinin yerine geçen tek bir sözlük karşılığı sayılmamalı ve yalnız kanıtın verdiği adlandırma sınırı içinde kullanılmalıdır.","branch_image_ar":"طرف مقلوم وكعب مبرّى","concept_gloss":"özel adlandırma kümesi","definition":"Kanıt, tek bir referent vermek yerine erkek devenin üreme organının ucunu, bu organın kılıfını ve mızrak ya da kamışın boğum veya dip bölümünü ayrı anlamlar olarak sıralar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kullanım erkek devenin üreme organının çengelli ucunu adlandırır."},{"facet_id":"F002","role":"source_variant","statement":"Başka bir kullanım aynı organı saran kılıfı adlandırır ve uç anlamıyla aynı referente sahip değildir."},{"facet_id":"F003","role":"source_variant","statement":"Bir başka kullanım mızrağın boğumlarını veya mızrak ile kamışın dip bölümünü adlandırır."}],"identity_rationale":"Bu dal, kanıtta tek üretken kök çekirdeğine indirgenmeyen sınırlı adlandırma malzemesini taşır. Yapısal bölme şartı koşmadan, yalnız verilen biçim ve bağlam sınırı içinde kontrollü adlandırma kümesi olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"erkek devenin üreme organının çengelli ucu"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"erkek devenin üreme organının kılıfı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"mızrağın boğumları; mızrak veya kamışın dip bölümü"}],"lexicalization_note":"Kapsam verilen biçim, adlandırma veya özel kullanım sınırıyla bağlıdır; ortak bir yalın anlam ya da üretken genel kullanım varsayılmaz.","neighbor_coverage_note":"Dal yalnız sınırlı veya biçime bağlı adlandırma malzemesini tuttuğu için yayımlanacak güvenilir komşu ayrımı seçilmedi.","source_phrase_ar":"المقلم طرف قنب البعير؛ مقالم الرمح كعوبه (maqayis)؛ المقلم طرف قضيب البعير (ayn)؛ المقلم وعاء قضيب البعير؛ مقالم الرمح كعوبه (sihah)؛ المقلم طرف قضيب البعير وفي طرفه حجنة (tahdhib)؛ كعب الرمح والقصب (mufradat)","source_summary":"Kanıt, tek bir birleşik anlamdan çok sınırlı veya biçime bağlı adlandırmaları gösterir; dal bu kayıtları kontrollü biçimde görünür tutar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"طرف قضيب البعير أو وعاؤه ومقالم الرمح وكعب الرمح والقصب","what_is_not_ar":"القلم الكاتب؛ القدح للقرعة؛ القَلّام النبت"},"support_links":[]},{"boundary":"Bu dal kesme işleminin kendisi ya da her tür kesici değil, listelenmiş özel adlarla karşılanan iki ağızlı kesme aracıdır.","branch_kind":"non_bare","branch_ref":"root_001252/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَلَم","morph_features":"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:4:3:3","qac_word_ref":"96:4:3","surface_ar":"قَلَمِ"}],"gloss":"iki ağızlı kesme aracı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki karşılıklı kesici ağız, tırnak veya benzeri bir şeyi araya alıp keser."}}],"root_ar":"ق ل م","root_id":"root_001252","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel birimlerin ortak referenti olan karşılıklı ağızlarla kesen aracı doğal ve kapsayıcı biçimde karşılar.","boundary_detail":"Bu dal kesme işleminin kendisi ya da her tür kesici değil, listelenmiş özel adlarla karşılanan iki ağızlı kesme aracıdır.","branch_image_ar":"آلة تقص كالجلم","concept_gloss":"iki ağızlı kesme aracı","contextual_glosses":[{"applicability":"Aracın doğrudan tırnak kesmek için kullanıldığı cümlelerde doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Aynı iki ağızlı aracın başka şeyleri kesebilme kapsamını daraltır.","preserves":"Aracın tırnak üzerinde kullanılan somut bir kesici olmasını korur."},"facet_ids":["F001"],"text":"tırnak kesme aracı","usage_role":"contextual"}],"definition":"Tırnak veya benzeri şeyleri iki karşılıklı ağız arasında kesmeye yarayan, kanıtta özel ad biçimleriyle sözlükselleşmiş bir kesme aracıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki karşılıklı kesici ağız, tırnak veya benzeri bir şeyi araya alıp keser."}],"identity_rationale":"Kaynak ifadesi tırnak kesmede kullanılan iki ağızlı kesici aracı ve bu araç için kullanılan özel biçimleri verir. Dalın araç anlamı sağlamdır, ancak mekanik sözlükselleşme profili çıplak anlamı değil listelenmiş özel birimleri desteklediğinden tanım bu birimlerle sınırlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"iki ağızlı kesme aracı"}],"lexicalization_note":"Anlam yalnız kanıtta listelenen özel araç adlarına bağlı tutulur; kökün yalın biçimine genel bir kesici araç anlamı yüklenmez.","neighbor_coverage_note":"Kesici ağız, testere, sivriltilmiş uç ve kılıç adayları karşılaştırıldı; genel kesici araç dalı iki ağızlı yapı sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalın referenti iki ağızlı ve kapanarak kesen belirli araçtır; karşı dalın kapsamı yapı bakımından daha geniştir ve kılıç ile tek ağızlı uçları da içerir.","focus_only":"Bu dal, iki karşılıklı ağızla kapanarak kesen ve özel adlarla belirtilen araca özgüdür.","gloss":"genel kesici araç ve ağız","neighbor_only":"Karşı dal genel kesme araçlarını, keskin kılıçları ve kısa geniş bıçak ya da ok uçlarını kapsar.","neighbor_ref":"root_001240/B014","relation_type":"near_neighbor","shared_zone":"Her iki dal da keskin bir bölümle maddi bir şeyi kesmeye yarayan somut araçları içerebilir."}],"source_phrase_ar":"القلم قطع الظفر بالقلمين وبالقلم (ayn)؛ القلم الجلم (sihah)؛ يقال للمقراض المقلام والقلمان والجلمان (tahdhib)","source_summary":"Kaynaklar tırnak kesme bağlamında iki ağızlı bir kesme aracını gösterir ve araç için birden fazla özel ad biçimi aktarır.","sources":["AY","SI","TA"],"what_is_ar":"القلم أو القلمان أو المقلام إذا أريد به الجلم والمقراض","what_is_not_ar":"القلم الكاتب؛ القدح؛ القَلّام النبت"},"support_links":[]},{"boundary":"Dal genel olarak bitki ya da tuzcul bitki değil, kanıtta gövdesiz oluşuyla tanınan belirli bir tür adıdır.","branch_kind":"bare","branch_ref":"root_001252/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَلَم","morph_features":"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:4:3:3","qac_word_ref":"96:4:3","surface_ar":"قَلَمِ"}],"gloss":"gövdesiz tuzcul bir bitki türü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bitki, tuzlu topraklara uyumlu bir gruba girer ve belirgin bir gövde taşımaz."}}],"root_ar":"ق ل م","root_id":"root_001252","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkinin yaşam alanı grubunu ve ayırt edici gövdesizlik özelliğini birlikte veren açıklayıcı karşılıktır.","boundary_detail":"Dal genel olarak bitki ya da tuzcul bitki değil, kanıtta gövdesiz oluşuyla tanınan belirli bir tür adıdır.","branch_image_ar":"نبت شاذ عن الأصل","concept_gloss":"gövdesiz tuzcul bir bitki türü","contextual_glosses":[{"applicability":"Bitkinin kısa ve otsu görünümünün öne çıktığı betimleyici bağlamlarda kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bitkinin gövdesizliğini ve tuzlu çevreyle ilişkili niteliğini korur."},"facet_ids":["F001"],"text":"gövdesiz tuzcul ot","usage_role":"contextual"}],"definition":"Tuzlu topraklarda yetişen bitkiler grubundan, belirgin bir gövdesi bulunmayan belirli bir bitki türüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bitki, tuzlu topraklara uyumlu bir gruba girer ve belirgin bir gövde taşımaz."}],"identity_rationale":"Kaynak ifadesi, tuzlu toprak bitkileri arasında sayılan ve gövdesi bulunmayan belirli bir bitkiyi açıkça tanımlar. Dal çerçevesi bunun kökün kesme anlamından ayrı bir bitki adı olduğunu doğru biçimde belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"gövdesiz tuzcul bir bitki türü"}],"lexicalization_note":"Çıplak dal belirli gövdesiz tuzcul bitkiyi adlandırır; kesme, yazı aracı veya coğrafi bölge anlamları buna taşınmaz.","neighbor_coverage_note":"Bitki adaylarının tümü değerlendirildi; uzun kum bitkisi, gövdesizlik ve yetişme çevresi sınırlarını birlikte görünür kıldığı için seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Bu dalın ayırıcı özellikleri tuzcul gruba bağlılık ve gövdesizliktir; karşı dal ise kumlu ortam ve uzun büyüme özelliğiyle ayrılır.","focus_only":"Bu dal tuzcul gruba ait, belirgin gövdesi bulunmayan belirli bir bitkiyi gösterir.","gloss":"kumda yetişen uzun bitki","neighbor_only":"Karşı dal kumda yetişen, uzayan ve kimi anlatımda ağaç türü sayılan bir bitkiyi gösterir.","neighbor_ref":"root_000668/B004","relation_type":"same_field","shared_zone":"İki dal da yetişme çevresi ve yapısal görünümüyle tanımlanan bitki adlarıdır."}],"source_phrase_ar":"مما شذ عن هذا الأصل القلام وهو نبت (maqayis)؛ القلام بالتشديد القاقلى وهو من الحمض (sihah)؛ القلام القاقلى؛ القلام من الحمض لا ساق له (tahdhib)","source_summary":"Kaynaklar bunun ana kesme anlamından ayrı bir bitki adı olduğunu, tuzcul bitkiler arasında yer aldığını ve gövdesiz oluşunu aktarır.","sources":["MQ","SI","TA"],"what_is_ar":"القَلّام النبت والقاقلى من الحمض الذي لا ساق له","what_is_not_ar":"قلم الظفر والكتابة والقداح؛ الإقليم"},"support_links":[]},{"boundary":"Dal sıradan bir arazi parçası değil, yeryüzünün büyük ve düzenli coğrafi bölümlerinden biridir; kesilmişlik yalnız adlandırma açıklamasıdır.","branch_kind":"bare","branch_ref":"root_001252/B008","candidate_links":[{"candidate_id":"cand_d720c120a6ca5240daf2","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَلَم","morph_features":"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:4:3:3","qac_word_ref":"96:4:3","surface_ar":"قَلَمِ"}],"gloss":"yeryüzünün büyük coğrafi bölümlerinden biri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Referent, yeryüzünü oluşturan büyük coğrafi bölümlerden biri ve geleneksel yedili düzenin bir parçasıdır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adın, bölgenin komşu bölgeden kesilip ayrılmış sayılmasına bağlandığı bir türetim açıklaması verilir."}}],"root_ar":"ق ل م","root_id":"root_001252","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Referentin coğrafi bölüm niteliğini ve yeryüzü ölçeğindeki kapsamını doğal biçimde karşılar.","boundary_detail":"Dal sıradan bir arazi parçası değil, yeryüzünün büyük ve düzenli coğrafi bölümlerinden biridir; kesilmişlik yalnız adlandırma açıklamasıdır.","branch_image_ar":"قسم مقطوع من الأرض","concept_gloss":"yeryüzünün büyük coğrafi bölümlerinden biri","contextual_glosses":[{"applicability":"Geleneksel yedili coğrafya düzeninin özellikle açıklandığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Büyük bölgeyi ve yedili bölümleme içindeki yerini birlikte korur."},"facet_ids":["F001"],"text":"yedi yeryüzü bölgesinden biri","usage_role":"explanatory"}],"definition":"Yeryüzünün geleneksel olarak yediye ayrıldığı düşünülen büyük coğrafi bölümlerden biridir; komşu bölümden ayrılmış sayılması adın türetimine ilişkin bir açıklamadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Referent, yeryüzünü oluşturan büyük coğrafi bölümlerden biri ve geleneksel yedili düzenin bir parçasıdır."},{"facet_id":"F002","role":"source_variant","statement":"Adın, bölgenin komşu bölgeden kesilip ayrılmış sayılmasına bağlandığı bir türetim açıklaması verilir."}],"identity_rationale":"Kaynak ifadesinin referenti, yeryüzünün geleneksel olarak yediye ayrılan büyük bölümlerinden biridir. Komşu bölgeden kesilip ayrılmış sayılmasına dayanan açıklama bir türetim yorumudur; dalın doğrudan tanımı herhangi bir kesilmiş toprak parçasına genişletilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yeryüzünün büyük coğrafi bölümlerinden biri"}],"lexicalization_note":"Çıplak dal büyük coğrafi bölgeyi adlandırır; yerel toprak parçası, sınır çizgisi veya belirli bir özel yer adı bu kapsama alınmaz.","neighbor_coverage_note":"Arazi parçası, sınır, özel yer ve yönetim çevresi adayları değerlendirildi; yerel toprak parçası büyük coğrafi bölüm sınırını en iyi gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal büyük ve düzenli bir coğrafi sınıflandırma birimidir; karşı dal ise çevresinden farklı görünen herhangi bir yerel toprak parçasıdır.","focus_only":"Bu dal yeryüzü ölçeğinde kurulan geleneksel büyük bölümleme sisteminin bir birimini gösterir.","gloss":"çevresinden ayrılan toprak parçası","neighbor_only":"Karşı dal, çevresinden görünüşü veya üzerindeki oluşumlar bakımından ayrılan yerel bir toprak parçasını gösterir.","neighbor_ref":"root_000140/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da çevresindeki yerlerden ayırt edilen bir toprak alanını adlandırabilir."}],"source_phrase_ar":"الإقليم واحد أقاليم الأرض السبعة (sihah)؛ الإقليم واحد الأقاليم وأحسبه عربيا (tahdhib)؛ سمي إقليما لأنه مقلوم من الإقليم الذي يتاخمه أي مقطوع عنه (tahdhib)؛ الإقليم واحد الأقاليم السبعة؛ الدنيا مقسومة على سبعة أسهم (mufradat)","source_summary":"Kaynaklar referenti yeryüzünün yedi büyük bölümünden biri olarak tanımlar; ayrıca adın komşu bölümden ayrılmış olma düşüncesiyle açıklanabildiğini aktarır.","sources":["SI","TA","MU"],"what_is_ar":"الإقليم قسمة من الأرض أو واحد الأقاليم السبعة","what_is_not_ar":"القلم الكاتب؛ القدح؛ القَلّام النبت"},"support_links":["sup_894d5ca19a5dfe791527"]},{"boundary":"Dal genel yalnızlık değil, evlilik eşi bulunmama durumudur; kadına ilişkin kullanım bu durumun uzun sürmesini ayrıca belirtebilir.","branch_kind":"non_bare","branch_ref":"root_001252/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَلَم","morph_features":"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:4:3:3","qac_word_ref":"96:4:3","surface_ar":"قَلَمِ"}],"gloss":"eşi olmayan erkek ve kadınlar; kadının uzun süre eşsiz kalması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Erkek veya kadın, evlilik eşi bulunmayan kişi olarak adlandırılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kadının eşi olmadan geçirdiği dönemin uzun sürmesi ayrıca belirtilir."}}],"root_ar":"ق ل م","root_id":"root_001252","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel birimlerin kişi grubunu ve kadına özgü süre uzaması anlamını birlikte karşılayan açıklayıcı ifadedir.","boundary_detail":"Dal genel yalnızlık değil, evlilik eşi bulunmama durumudur; kadına ilişkin kullanım bu durumun uzun sürmesini ayrıca belirtebilir.","branch_image_ar":"انقطاع عن الزوج","concept_gloss":"eşi olmayan erkek ve kadınlar; kadının uzun süre eşsiz kalması","contextual_glosses":[{"applicability":"Erkek ve kadınların birlikte anıldığı, durumun süresinin öne çıkmadığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kadının bu durumda uzun süre kalmasına ilişkin özel anlamı kapsamaz.","preserves":"Her iki cinsiyet için evlilik eşi bulunmaması durumunu korur."},"facet_ids":["F001"],"text":"eşi olmayan kişiler","usage_role":"general"},{"applicability":"Kadının eşi olmadan geçirdiği dönemin uzunluğunun özellikle belirtildiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eşi olmayan erkekleri ve süre belirtilmeyen genel kişi grubunu kapsamaz.","preserves":"Kadına özgü uzun süren eşsizlik durumunu açıkça korur."},"facet_ids":["F002"],"text":"uzun süre eşsiz kalan kadın","usage_role":"contextual"}],"definition":"Evlilik eşi bulunmayan erkek ve kadınları adlandırır; kadın bakımından bu durumun uzun süre devam etmesini de özel olarak anlatabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Erkek veya kadın, evlilik eşi bulunmayan kişi olarak adlandırılır."},{"facet_id":"F002","role":"specialization","statement":"Kadının eşi olmadan geçirdiği dönemin uzun sürmesi ayrıca belirtilir."}],"identity_rationale":"Kaynak ifadesi eşi olmayan erkek ve kadınları, ayrıca bir kadının uzun süre eşsiz kalmasını açıkça verir. Dal çerçevesi kişi grubuyla süren eşsizlik durumunu doğru biçimde aynı özel söz varlığı altında toplar.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"eşi olmayan erkek ve kadınlar; kadının uzun süre eşsiz kalması"}],"lexicalization_note":"Anlam yalnız kanıtta listelenen özel kişi ve durum adlarına bağlıdır; kökün yalın biçimine genel bir eşsizlik anlamı yüklenmez.","neighbor_coverage_note":"Yalnızlık, eşten ayrılık, evlenmeme ve kadınlara özgü durum adayları değerlendirildi; iki cinsi kapsayan eşsizlik dalı en yakın karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Kişi durumunda iki dal büyük ölçüde örtüşür; bu dal kadının uzun süren eşsizliğini özelleştirirken karşı dal durumun eylem ve neden boyutlarına daha geniş açılır.","focus_only":"Bu dal özel ad biçimlerinin yanında kadının eşi olmadan geçirdiği sürenin uzamasını ayrıca belirtir.","gloss":"evlilik eşinden yoksun olma","neighbor_only":"Karşı dal eşsiz kalma eylemini, evlenmeden durmayı ve başkalarını eşsiz bırakmaya yol açan durumları da kapsar.","neighbor_ref":"root_000073/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da kadın veya erkeğin evlilik eşinin bulunmaması durumunu doğrudan anlatır."}],"source_phrase_ar":"القلمة العزاب من الرجال الواحد قالم ونساء مقلمات؛ القلم طول أيمة المرأة وامرأة مقلمة أي أيم؛ مقلمات بغير أزواج","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, eşi olmayan erkek ve kadın adlarını ve kadının uzun süre eşsiz kalması anlamını birlikte verir."}],"source_summary":"Bu dal için kaynaklar arasında paylaşılan ek bir özet bulunmamaktadır.","sources":["TA"],"what_is_ar":"العزاب من الرجال والنساء وطول أيمة المرأة","what_is_not_ar":"قلم الظفر؛ القلم الكاتب؛ القَلّام النبت"},"support_links":[]},{"boundary":"Dal her renkli ya da boyalı kumaşı değil, görünüşte birden çok renge dönüşen özel dokuma türünü adlandırır.","branch_kind":"non_bare","branch_ref":"root_001252/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَلَم","morph_features":"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:4:3:3","qac_word_ref":"96:4:3","surface_ar":"قَلَمِ"}],"gloss":"gözde farklı renklere bürünen yabancı kökenli dokuma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Özel kumaş, bakan gözde tek ve sabit bir renk yerine farklı renklere bürünür görünür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kumaşın kökeni kaynakta yabancı bir topluluğun dokuma geleneğine bağlanır."}}],"root_ar":"ق ل م","root_id":"root_001252","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kumaşın özel tür oluşunu, değişken renk görünümünü ve kaynakta belirtilen köken niteliğini birlikte korur.","boundary_detail":"Dal her renkli ya da boyalı kumaşı değil, görünüşte birden çok renge dönüşen özel dokuma türünü adlandırır.","branch_image_ar":"ثوب تتلون ألوانه","concept_gloss":"gözde farklı renklere bürünen yabancı kökenli dokuma","contextual_glosses":[{"applicability":"Kumaşın görsel etkisinin öne çıktığı ve köken bilgisinin ayrıca gerekmediği cümlelerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kaynakta kumaşa bağlanan yabancı köken bilgisini belirtmez.","preserves":"Kumaşın bakan gözde değişen renkler göstermesini korur."},"facet_ids":["F001"],"text":"bakıldıkça renk değiştiren kumaş","usage_role":"contextual"}],"definition":"Kaynakta yabancı bir topluluğun dokuması olarak tanıtılan, bakıldığında gözde birden çok renge bürünür görünen özel bir kumaş türüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Özel kumaş, bakan gözde tek ve sabit bir renk yerine farklı renklere bürünür görünür."},{"facet_id":"F002","role":"associated_use","statement":"Kumaşın kökeni kaynakta yabancı bir topluluğun dokuma geleneğine bağlanır."}],"identity_rationale":"Kaynak ifadesi belirli bir kumaş türünü, bakan gözde farklı renklere bürünür görünmesi ve yabancı kökenli sayılmasıyla tanımlar. Dal çerçevesi nesne türünü ve değişken renk görünümünü doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"gözde farklı renklere bürünen yabancı kökenli kumaş"}],"lexicalization_note":"Anlam yalnız kanıtta listelenen özel kumaş adına bağlıdır; kökün yalın biçimine renk değiştirme veya kumaş anlamı yüklenmez.","neighbor_coverage_note":"Boyalı, desenli, parlak, ince ve özel dokuma adayları değerlendirildi; sabit çok renklilik ile değişken görünüş karşıtlığı en yararlı sınırdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda renkler bakış sırasında değişir görünür; karşı dalda ise çok renklilik boya veya desen olarak kumaşın üzerinde sabittir.","focus_only":"Bu dalın kumaşı, bakan gözde farklı renklere bürünür görünen değişken bir görsel etki taşır.","gloss":"çok renkli veya desenli kumaş","neighbor_only":"Karşı dalın kumaşı sabit biçimde boyanmış, çok renkli veya desenlidir ve yanıltıcı görünüş benzetmesiyle adlandırılır.","neighbor_ref":"root_001290/B009","relation_type":"near_neighbor","shared_zone":"İki dal da birden çok rengin algılandığı özel kumaş türlerini anlatır."}],"source_phrase_ar":"أبو قلمون ضرب من ثياب الروم يتلون للعيون ألوانا","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, yabancı kökenli sayılan özel kumaşı gözde farklı renklere bürünmesiyle tanımlar."}],"source_summary":"Bu dal için kaynaklar arasında paylaşılan ek bir özet bulunmamaktadır.","sources":["SI"],"what_is_ar":"أبو قلمون ثوب رومي متلون للعيون","what_is_not_ar":"القلم الكاتب؛ القدح؛ القَلّام النبت"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["96:4:1"],"branch_refs":[],"candidate_id":"cand_496a6f74545bd8adda75","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:4:1:antecedent-and-relative-scope","source_type":"word_analysis","support_ids":["sup_36c400d4d111ef4c0e8a","sup_c44df8fb1c01190ef8eb"],"title":"relative pronoun carries 96:3 into the whole clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:1","qac_refs":["96:4:1:1"],"status":"accepted"}},{"anchor_refs":["96:4:1"],"branch_refs":[],"candidate_id":"cand_dbf9d7268bc4d74ffda2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:4:1:command-to-description-shift","source_type":"word_analysis","support_ids":["sup_36c400d4d111ef4c0e8a","sup_94aaca2fd4199dee1f6d"],"title":"imperative frame turns into divine characterization","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:1","qac_refs":["96:4:1:1"],"status":"accepted"}},{"anchor_refs":["96:4:1"],"branch_refs":[],"candidate_id":"cand_724dd87d277270a7d647","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:4:1:creation-teaching-relative-parallel","source_type":"word_analysis","support_ids":["sup_36c400d4d111ef4c0e8a","sup_a23499de1d68fae1917e"],"title":"same relative frame pairs creation and teaching","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:1","qac_refs":["96:4:1:1"],"status":"accepted"}},{"anchor_refs":["96:4:1"],"branch_refs":[],"candidate_id":"cand_f7ba6c330477d6b60096","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:4:1:identity-through-teaching","source_type":"word_analysis","support_ids":["sup_36c400d4d111ef4c0e8a","sup_bed3f8363d4f1b0d18b6"],"title":"empty relative receives identity from its ṣila","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:1","qac_refs":["96:4:1:1"],"status":"accepted"}},{"anchor_refs":["96:4:1"],"branch_refs":[],"candidate_id":"cand_2da4c3d9826149325be6","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"96:4:1:short-clause-sound-binding","source_type":"word_analysis","support_ids":["sup_24730529e87facec7f2b","sup_36c400d4d111ef4c0e8a"],"title":"lām-mīm texture binds the three-word clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:1","qac_refs":["96:4:1:1"],"status":"accepted"}},{"anchor_refs":["96:4:2"],"branch_refs":[],"candidate_id":"cand_c6ddf8c5f80dd7fcc610","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:4:2:epistemic-agency-with-open-recipient","source_type":"word_analysis","support_ids":["sup_32aa32e361bfcaa39ab3","sup_a6996e2e97439a69a043"],"title":"divine agency is foregrounded while recipient remains open","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:2","qac_refs":["96:4:2:1"],"status":"accepted"}},{"anchor_refs":["96:4:2"],"branch_refs":[],"candidate_id":"cand_a7b0037ebb9961f84560","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:4:2:form-ii-perfect-causative-teaching","source_type":"word_analysis","support_ids":["sup_a0dfb3d50868017ed366","sup_a6996e2e97439a69a043"],"title":"perfect Form II turns knowing outward as teaching","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:2","qac_refs":["96:4:2:1"],"status":"accepted"}},{"anchor_refs":["96:4:2"],"branch_refs":[],"candidate_id":"cand_8ccca8d6aa5cf119ab33","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:4:2:instrument-governance","source_type":"word_analysis","support_ids":["sup_1efc672dbe22e56b086a","sup_a6996e2e97439a69a043"],"title":"verb governs the pen as teaching means","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:2","qac_refs":["96:4:2:1"],"status":"accepted"}},{"anchor_refs":["96:4:2"],"branch_refs":[],"candidate_id":"cand_5fd232a833da1a731f29","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:4:2:knowledge-marking-pen-convergence","source_type":"word_analysis","support_ids":["sup_6c202ed351a7d032c367","sup_a6996e2e97439a69a043"],"title":"marking pressure survives through the governed pen","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:2","qac_refs":["96:4:2:1"],"status":"accepted"}},{"anchor_refs":["96:4:2"],"branch_refs":[],"candidate_id":"cand_194bba5ed9fa8079bc4e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:4:2:object-ellipsis-and-forward-uptake","source_type":"word_analysis","support_ids":["sup_865648907c9cf01f1573","sup_a6996e2e97439a69a043"],"title":"missing learner and content make 96:5 answer the gap","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:2","qac_refs":["96:4:2:1"],"status":"accepted"}},{"anchor_refs":["96:4:2"],"branch_refs":[],"candidate_id":"cand_8c49c2446f9eeafac284","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:4:2:relative-predicate-and-command-grounding","source_type":"word_analysis","support_ids":["sup_31b44e62e925656e2de4","sup_a6996e2e97439a69a043"],"title":"teaching specifies generosity and grounds the command","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:2","qac_refs":["96:4:2:1"],"status":"accepted"}},{"anchor_refs":["96:4:2"],"branch_refs":[],"candidate_id":"cand_52c7abbbc96de364aa3e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:4:2:sound-and-form-pressure","source_type":"word_analysis","support_ids":["sup_a6996e2e97439a69a043","sup_ca69b9cd66b189dc8c97"],"title":"geminated verb sounds its causative force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:2","qac_refs":["96:4:2:1"],"status":"accepted"}},{"anchor_refs":["96:4:2"],"branch_refs":[],"candidate_id":"cand_f891a7e470ecc598972f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:4:2:teaching-echoes-within-and-beyond-surah","source_type":"word_analysis","support_ids":["sup_4ec00ee79d7232ae101d","sup_a6996e2e97439a69a043"],"title":"local teaching opens a wider knowledge chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:2","qac_refs":["96:4:2:1"],"status":"accepted"}},{"anchor_refs":["96:4:3"],"branch_refs":[],"candidate_id":"cand_9adc39d8d5c651d68b82","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001252"],"scope":"focus_ayah","source_local_id":"96:4:3:cut-shaped-writing-instrument","source_type":"word_analysis","support_ids":["sup_6b53e800e3b60cfa5621","sup_dc2781d40f0d9281224e"],"title":"cutting root image survives inside the writing pen","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:3","qac_refs":["96:4:3:1","96:4:3:2","96:4:3:3"],"status":"accepted"}},{"anchor_refs":["96:4:3"],"branch_refs":[],"candidate_id":"cand_857050b9d6d58c319ee5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001252"],"scope":"focus_ayah","source_local_id":"96:4:3:definite-singular-scope","source_type":"word_analysis","support_ids":["sup_46e6062d1ee99b34390b","sup_6b53e800e3b60cfa5621"],"title":"definite singular keeps class and known-pen readings open","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:3","qac_refs":["96:4:3:1","96:4:3:2","96:4:3:3"],"status":"accepted"}},{"anchor_refs":["96:4:3"],"branch_refs":[],"candidate_id":"cand_4fc7977421d9fb61f254","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001252"],"scope":"focus_ayah","source_local_id":"96:4:3:ellipsis-and-final-instrument-focus","source_type":"word_analysis","support_ids":["sup_6b53e800e3b60cfa5621","sup_b9f6dd1db0cce035d2d7"],"title":"object ellipsis makes the final instrument load-bearing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:3","qac_refs":["96:4:3:1","96:4:3:2","96:4:3:3"],"status":"accepted"}},{"anchor_refs":["96:4:3"],"branch_refs":[],"candidate_id":"cand_a35ab4f4ca2a88abeb3e","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001252"],"scope":"focus_ayah","source_local_id":"96:4:3:instrumental-ba-and-case","source_type":"word_analysis","support_ids":["sup_6b53e800e3b60cfa5621","sup_e60af037612aae15e2db"],"title":"bāʾ layers medium over a fixed instrumental role","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:3","qac_refs":["96:4:3:1","96:4:3:2","96:4:3:3"],"status":"accepted"}},{"anchor_refs":["96:4:3"],"branch_refs":[],"candidate_id":"cand_4be1b76a8d6f598a7b93","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001252"],"scope":"focus_ayah","source_local_id":"96:4:3:local-lam-mim-sound-link","source_type":"word_analysis","support_ids":["sup_6b53e800e3b60cfa5621","sup_a4dfb19a704a0de69677"],"title":"pen echoes the teaching verb while keeping roles distinct","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:3","qac_refs":["96:4:3:1","96:4:3:2","96:4:3:3"],"status":"accepted"}},{"anchor_refs":["96:4:3"],"branch_refs":[],"candidate_id":"cand_d5783ad46946b01eeefe","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001252"],"scope":"focus_ayah","source_local_id":"96:4:3:rare-distribution-salience","source_type":"word_analysis","support_ids":["sup_6b53e800e3b60cfa5621","sup_9c23b840a332f39fad6c"],"title":"small q-l-m distribution makes this use inspectable","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:3","qac_refs":["96:4:3:1","96:4:3:2","96:4:3:3"],"status":"accepted"}},{"anchor_refs":["96:4:3"],"branch_refs":[],"candidate_id":"cand_1fad27b21605297cde2c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001252"],"scope":"focus_ayah","source_local_id":"96:4:3:rare-qalam-distribution","source_type":"word_analysis","support_ids":["sup_6b53e800e3b60cfa5621","sup_a7a0eeffbb1fe95f25db"],"title":"rare pen field includes oath, lots, and finite pens","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:3","qac_refs":["96:4:3:1","96:4:3:2","96:4:3:3"],"status":"accepted"}},{"anchor_refs":["96:4:3"],"branch_refs":[],"candidate_id":"cand_31876e265498c664e2a7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001252"],"scope":"focus_ayah","source_local_id":"96:4:3:reading-inscription-forward-bridge","source_type":"word_analysis","support_ids":["sup_524fe35876a66ebb5b79","sup_6b53e800e3b60cfa5621"],"title":"pen prepares readable knowledge and 96:5's content","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:3","qac_refs":["96:4:3:1","96:4:3:2","96:4:3:3"],"status":"accepted"}},{"anchor_refs":["96:4:3"],"branch_refs":[],"candidate_id":"cand_5a21d43f6a91b6538c43","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001252"],"scope":"focus_ayah","source_local_id":"96:4:3:visible-and-audible-prepositional-fusion","source_type":"word_analysis","support_ids":["sup_6b53e800e3b60cfa5621","sup_e0d83b04f05041704bb3"],"title":"attached bāʾ makes instrumentality one written word","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"96:4:3","qac_refs":["96:4:3:1","96:4:3:2","96:4:3:3"],"status":"accepted"}},{"anchor_refs":["96:4:2"],"branch_refs":[],"candidate_id":"cand_e45547873806032a38ef","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001040"],"scope":"focus_ayah","source_local_id":"96:4:2:1","source_type":"qac_morpheme","support_ids":["sup_557b04c7b589939f140b"],"title":"QAC root occurrence: ع ل م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["96:4:3"],"branch_refs":[],"candidate_id":"cand_583a3fd58143896fd809","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001252"],"scope":"focus_ayah","source_local_id":"96:4:3:3","source_type":"qac_morpheme","support_ids":["sup_2f53ae3b5e4c9f9c8623"],"title":"QAC root occurrence: ق ل م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["96:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:4","branch_refs":["root_001040/B001","root_001252/B003"],"candidate_id":"cand_8e4a96727f27458aa686","commentary_obligation":"review","hft_ref":"hft_de58eb56d4a19a851dfa","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_inscribed_clarity","source_type":"hft","support_ids":["sup_9a6be11e6bf6a3ca03c4"],"title":"baseline_inscribed_clarity","trust":"legacy_unbound"},{"anchor_refs":["96:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:4","branch_refs":["root_001040/B002","root_001252/B001"],"candidate_id":"cand_6b44d9e2df2e3f556c84","commentary_obligation":"review","hft_ref":"hft_079803999ac571ee384a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_differentiating_cuts","source_type":"hft","support_ids":["sup_bb89bebc77d2a2585d84"],"title":"baseline_differentiating_cuts","trust":"legacy_unbound"},{"anchor_refs":["96:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:4","branch_refs":["root_001040/B002","root_001252/B008"],"candidate_id":"cand_d720c120a6ca5240daf2","commentary_obligation":"review","hft_ref":"hft_9025ef9a7954f92a2657","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_partitioned_field","source_type":"hft","support_ids":["sup_894d5ca19a5dfe791527"],"title":"baseline_partitioned_field","trust":"legacy_unbound"},{"anchor_refs":["96:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"96:4","branch_refs":["root_001040/B002","root_001252/B004"],"candidate_id":"cand_343c5ab6bc6f197cc5ae","commentary_obligation":"review","hft_ref":"hft_c1fa9708b59df26304d0","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_cast_lot_pedagogy","source_type":"hft","support_ids":["sup_4f20f93e3ae51afa3f14"],"title":"outlier_cast_lot_pedagogy","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"96:4:1:1","qac_word_ref":"96:4:1","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:4:2:1","qac_word_ref":"96:4:2","root_ar":"ع ل م","surface_ar":"عَلَّمَ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"96:4:3:1","qac_word_ref":"96:4:3","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"96:4:3:2","qac_word_ref":"96:4:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"قَلَم","morph_features":"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:4:3:3","qac_word_ref":"96:4:3","root_ar":"ق ل م","surface_ar":"قَلَمِ"}],"word_analysis_qac_refs":[["96:4:1:1"],["96:4:2:1"],["96:4:3:1","96:4:3:2","96:4:3:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["96:4:1","96:4:2","96:4:3"]},"focus_surface_evidence":{"arabic_uthmani":"ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ","qac_morphemes":[{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"96:4:1:1","qac_word_ref":"96:4:1","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"عَلَّمَ","morph_features":"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"96:4:2:1","qac_word_ref":"96:4:2","root_ar":"ع ل م","surface_ar":"عَلَّمَ"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"96:4:3:1","qac_word_ref":"96:4:3","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"96:4:3:2","qac_word_ref":"96:4:3","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"قَلَم","morph_features":"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"96:4:3:3","qac_word_ref":"96:4:3","root_ar":"ق ل م","surface_ar":"قَلَمِ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["96:4:1:1"],["96:4:2:1"],["96:4:3:1","96:4:3:2","96:4:3:3"]],"word_analysis_refs":["96:4:1","96:4:2","96:4:3"],"word_rows":[{"analysis_record_ref":"96:4:1","analytic_gloss_range_en":"masculine singular relative pronoun that opens a dependent descriptive clause and carries its antecedent from 96:3","analytic_root_gloss_range_en":null,"qac_refs":["96:4:1:1"],"root":{},"surface":{"arabic":"ٱلَّذِى","transliteration":"alladhī"}},{"analysis_record_ref":"96:4:2","analytic_gloss_range_en":"Form II perfect causative teaching, with learner and content elided and the pen phrase stated as instrument","analytic_root_gloss_range_en":"knowledge, knowing, teaching, informing, and marking/sign branches are in the broader root family; local Form II selects caused knowing or teaching while the pen keeps sign-making pressure relevant","qac_refs":["96:4:2:1"],"root":{"arabic":"ع ل م","transliteration":"ʿ-l-m"},"surface":{"arabic":"عَلَّمَ","transliteration":"ʿallama"}},{"analysis_record_ref":"96:4:3","analytic_gloss_range_en":"instrumental bāʾ plus definite genitive noun: by, through, or with the pen, with the local role fixed as teaching means","analytic_root_gloss_range_en":"cutting, trimming, shaped writing reed or pen, lot-casting sticks, cutting tools, and other extended branches; local phrase selects the writing-instrument branch while preserving the shaped/cut tool background","qac_refs":["96:4:3:1","96:4:3:2","96:4:3:3"],"root":{"arabic":"ق ل م","transliteration":"q-l-m"},"surface":{"arabic":"بِٱلْقَلَمِ","transliteration":"bi-l-qalami"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["96:4"],"branch_refs":["root_001040/B001","root_001252/B003"],"candidate_id":"cand_8e4a96727f27458aa686","evidence_scope":"focus_ayah","hft_ref":"hft_de58eb56d4a19a851dfa","item_id":"baseline_inscribed_clarity","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_inscribed_clarity","support_id":"sup_9a6be11e6bf6a3ca03c4"},{"anchor_refs":["96:4"],"branch_refs":["root_001040/B002","root_001252/B001"],"candidate_id":"cand_6b44d9e2df2e3f556c84","evidence_scope":"focus_ayah","hft_ref":"hft_079803999ac571ee384a","item_id":"baseline_differentiating_cuts","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_differentiating_cuts","support_id":"sup_bb89bebc77d2a2585d84"},{"anchor_refs":["96:4"],"branch_refs":["root_001040/B002","root_001252/B008"],"candidate_id":"cand_d720c120a6ca5240daf2","evidence_scope":"focus_ayah","hft_ref":"hft_9025ef9a7954f92a2657","item_id":"baseline_partitioned_field","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_partitioned_field","support_id":"sup_894d5ca19a5dfe791527"},{"anchor_refs":["96:4"],"branch_refs":["root_001040/B002","root_001252/B004"],"candidate_id":"cand_343c5ab6bc6f197cc5ae","evidence_scope":"focus_ayah","hft_ref":"hft_c1fa9708b59df26304d0","item_id":"outlier_cast_lot_pedagogy","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_cast_lot_pedagogy","support_id":"sup_4f20f93e3ae51afa3f14"}],"diagnostics":[],"lane_counts":{"global":10,"macro":16,"micro":4},"packet_summary":{"ayah_count":19,"focus_ref":"96:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"س م و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000745","furuq_root_norm":"س م و","furuq_source_root_norm":"س م و","is_dominant":true,"target_occurrences":190,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001650","furuq_root_norm":"و س م","furuq_source_root_norm":"و س م","is_dominant":false,"target_occurrences":2,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000743","furuq_root_norm":"س م م","furuq_source_root_norm":"س م م","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ط غ ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000937","furuq_root_norm":"ط غ ي","furuq_source_root_norm":"ط غ ي","is_dominant":true,"target_occurrences":13,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000936","furuq_root_norm":"ط غ و","furuq_source_root_norm":"ط غ و","is_dominant":false,"target_occurrences":5,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ه د ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001583","furuq_root_norm":"ه د ي","furuq_source_root_norm":"ه د ي","is_dominant":true,"target_occurrences":251,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001580","furuq_root_norm":"ه د د","furuq_source_root_norm":"ه د د","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"د ع و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000478","furuq_root_norm":"د ع و","furuq_source_root_norm":"د ع و","is_dominant":true,"target_occurrences":77,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000477","furuq_root_norm":"د ع ع","furuq_source_root_norm":"د ع ع","is_dominant":false,"target_occurrences":22,"target_rank":2}]},{"qac_root":"ن د و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001487","furuq_root_norm":"ن د ي","furuq_source_root_norm":"ن د ي","is_dominant":true,"target_occurrences":33,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001486","furuq_root_norm":"ن د و","furuq_source_root_norm":"ن د و","is_dominant":false,"target_occurrences":10,"target_rank":2},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_001563","furuq_root_norm":"ن و د","furuq_source_root_norm":"ن و د","is_dominant":false,"target_occurrences":1,"target_rank":3}]},{"qac_root":"ط و ع","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000956","furuq_root_norm":"ط و ع","furuq_source_root_norm":"ط و ع","is_dominant":true,"target_occurrences":96,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000706","furuq_root_norm":"س ط ع","furuq_source_root_norm":"س ط ع","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["96:1","96:2","96:3","96:4","96:5","96:6","96:7","96:8","96:9","96:10","96:11","96:12","96:13","96:14","96:15","96:16","96:17","96:18","96:19"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"96:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":20,"unstructured_record_count":0},"identity":{"ayah_ref":"96:4","lane":"micro","linguistic_source_ref":"96:4","surface_ref":"96:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"96:4","target_tokens":[["O",["96:4:1"]],["kalemle",["96:4:3"]],["öğretendir",["96:4:2"]]],"text":"O, kalemle öğretendir."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":19,"id":"s096-p01-001-019","label":"Whole surah","number":1,"refs":["96:1","96:2","96:3","96:4","96:5","96:6","96:7","96:8","96:9","96:10","96:11","96:12","96:13","96:14","96:15","96:16","96:17","96:18","96:19"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:2:instrument-governance","source_type":"word_analysis","support_id":"sup_1efc672dbe22e56b086a","text":"{\"blocking_evidence\":null,\"headline\":\"verb governs the pen as teaching means\",\"reader_payoff\":\"The reader notices that the pen phrase is governed by the verb as the means of teaching, not appended as a loose image.\",\"reason\":\"Attachment evidence syntactically links {{ar:بِٱلْقَلَمِ}} ({{tr:bi-l-qalami}}) to {{ar:عَلَّمَ}} ({{tr:ʿallama}}) as a prepositional complement marking the instrument.\",\"representative_source_ids\":[\"QG-13ef5d44\",\"QT-48e6b0c2\",\"QH-f897e95b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:1:short-clause-sound-binding","source_type":"word_analysis","support_id":"sup_24730529e87facec7f2b","text":"{\"blocking_evidence\":null,\"headline\":\"lām-mīm texture binds the three-word clause\",\"reader_payoff\":\"The reader notices that the relative opener is not only syntactically joined to the clause; its sound texture also helps bind opener, teaching verb, and pen.\",\"reason\":\"The sound observation is modest and locally inspectable: lām is present across the relative, verb, and noun, with mīm recurring in the verb and closing noun.\",\"representative_source_ids\":[\"QP-08675966\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"96:4:3:3","source_type":"qac_morpheme","support_id":"sup_2f53ae3b5e4c9f9c8623","text":"{\"lemma_ar\":\"قَلَم\",\"morph_features\":\"STEM|POS:N|LEM:qalam|ROOT:qlm|M|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"96:4:3:3\",\"qac_word_ref\":\"96:4:3\",\"root_ar\":\"ق ل م\",\"surface_ar\":\"قَلَمِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:2:relative-predicate-and-command-grounding","source_type":"word_analysis","support_id":"sup_31b44e62e925656e2de4","text":"{\"blocking_evidence\":null,\"headline\":\"teaching specifies generosity and grounds the command\",\"reader_payoff\":\"The reader notices that the teaching verb gives substance to the relative description and makes the earlier command rest on a completed divine act.\",\"reason\":\"Inside the relative clause, the verb is the predicate that identifies the antecedent by action; after the imperative in 96:3, its perfect form supplies the grounding fact.\",\"representative_source_ids\":[\"QT-2706a0e3\",\"QI-0cda39b9\",\"QB-23512dec\",\"QB-cea47491\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:2:epistemic-agency-with-open-recipient","source_type":"word_analysis","support_id":"sup_32aa32e361bfcaa39ab3","text":"{\"blocking_evidence\":null,\"headline\":\"divine agency is foregrounded while recipient remains open\",\"reader_payoff\":\"The reader notices that the verb names epistemic transfer by the divine subject while leaving the receiving side open for the next ayah.\",\"reason\":\"The local form selects teaching or caused knowing rather than simple saying, notifying, or self-learning, while the elided objects keep the recipient unspecified.\",\"representative_source_ids\":[\"QS-974a4295\",\"QS-f675f777\",\"QF-2f1f85fb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:1","source_type":"word_analysis","support_id":"sup_36c400d4d111ef4c0e8a","text":"{\"gloss_range\":\"masculine singular relative pronoun that opens a dependent descriptive clause and carries its antecedent from 96:3\",\"prose\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}}) makes the whole ayah lean back into 96:3: the relative pronoun does not introduce a new actor but carries the prior Lord-description into the teaching clause. Because the word is semantically light until its ṣila is supplied, the following act of teaching becomes part of how the prior divine description is identified. The repeated relative pattern also recalls the creation relative in 96:1, so creation and teaching stand as paired divine actions rather than detached reports. At the discourse boundary, the command frame in 96:1 and 96:3 gives way to third-person characterization: the command is grounded by describing the one who teaches. Even the compact lām and mīm texture binds the relative opener into the verb and closing instrument, so the three-word clause sounds tightly joined.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:3:definite-singular-scope","source_type":"word_analysis","support_id":"sup_46e6062d1ee99b34390b","text":"{\"blocking_evidence\":null,\"headline\":\"definite singular keeps class and known-pen readings open\",\"reader_payoff\":\"The reader notices that the wording does not say merely a pen or many pens; the definite singular can carry the class of pens or a known exemplar.\",\"reason\":\"The local noun is definite singular after the preposition, and QAC explicitly allows generic or familiar-specific force for the article.\",\"representative_source_ids\":[\"QG-5e494a03\",\"MS-a1e60fdd\",\"QF-78562199\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:2:teaching-echoes-within-and-beyond-surah","source_type":"word_analysis","support_id":"sup_4ec00ee79d7232ae101d","text":"{\"blocking_evidence\":null,\"headline\":\"local teaching opens a wider knowledge chain\",\"reader_payoff\":\"The reader notices that this verb is part of a concrete chain: creation and teaching are paired in 96:1 and 96:4, the teaching-not-knowing sequence continues in 96:5 and 96:14, and wider teaching scenes in 2:31 and 55:2 illuminate content and text as comparison points.\",\"reason\":\"The rows supply concrete references for same-surah recurrence and wider teaching parallels; these are useful comparisons but do not override the local grammar of 96:4.\",\"representative_source_ids\":[\"QI-2490bbf5\",\"MI-31be32b1\",\"QE-29d54cc4\",\"ME-0d361404\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:3:reading-inscription-forward-bridge","source_type":"word_analysis","support_id":"sup_524fe35876a66ebb5b79","text":"{\"blocking_evidence\":null,\"headline\":\"pen prepares readable knowledge and 96:5's content\",\"reader_payoff\":\"The reader notices the transfer chain: the command to read in 96:1 and 96:3 meets the writing instrument in 96:4, and 96:5 then names the human unknown made teachable.\",\"reason\":\"The rows give concrete boundary links from the reading command to inscription and from the pen phrase to the knowledge content named in 96:5.\",\"representative_source_ids\":[\"QE-01496b5a\",\"QB-01a8ab3e\",\"QB-330a7cd8\",\"QB-83ff219b\",\"QB-bc3b35b0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"96:4:2:1","source_type":"qac_morpheme","support_id":"sup_557b04c7b589939f140b","text":"{\"lemma_ar\":\"عَلَّمَ\",\"morph_features\":\"STEM|POS:V|PERF|(II)|LEM:Eal~ama|ROOT:Elm|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"96:4:2:1\",\"qac_word_ref\":\"96:4:2\",\"root_ar\":\"ع ل م\",\"surface_ar\":\"عَلَّمَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:3","source_type":"word_analysis","support_id":"sup_6b53e800e3b60cfa5621","text":"{\"gloss_range\":\"instrumental bāʾ plus definite genitive noun: by, through, or with the pen, with the local role fixed as teaching means\",\"prose\":\"{{ar:بِٱلْقَلَمِ}} ({{tr:bi-l-qalami}}) is the only expressed complement after the teaching verb; its bāʾ can feel like by, through, or with the pen, while the local grammar fixes the pen as the means of teaching rather than the direct object. The genitive case keeps the noun governed by the preposition, and the bāʾ is fused to the definite noun so instrumentality is visible in writing and audible in recitation. The definite singular can point either to the class of writing instruments or to a familiar specific pen. The wider {{ar:ق ل م}} ({{tr:q-l-m}}) field reaches back to cutting and trimming, so the local pen is not an abstract tool: it is a shaped instrument that turns knowledge into marks. That broader field must be narrowed locally, because 96:4 selects the writing-instrument branch, though rare Quranic uses still matter: the pen is sworn by in 68:1, plural sticks decide guardianship in 3:44, and imagined pens remain finite before divine words in 31:27. Structurally, the ayah lands on this phrase; with learner and content absent, the final sound and surface space fall on the instrument that makes taught knowledge durable and readable, linking the prior reading command to inscription and preparing 96:5's unknown content. The supplied evidence treats this teaching-by-pen construction as a unique pairing, and the lām-mīm/-lam sound tie carries the pen's close toward knowing in 96:5.\",\"root_display\":\"{{ar:ق ل م}} ({{tr:q-l-m}})\",\"root_gloss_range\":\"cutting, trimming, shaped writing reed or pen, lot-casting sticks, cutting tools, and other extended branches; local phrase selects the writing-instrument branch while preserving the shaped/cut tool background\",\"surface_display\":\"{{ar:بِٱلْقَلَمِ}} ({{tr:bi-l-qalami}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:2:knowledge-marking-pen-convergence","source_type":"word_analysis","support_id":"sup_6c202ed351a7d032c367","text":"{\"blocking_evidence\":null,\"headline\":\"marking pressure survives through the governed pen\",\"reader_payoff\":\"The reader notices that teaching by the pen makes caused knowing feel like knowledge made legible through signs.\",\"reason\":\"The broader root family includes marking and signs, but the local Form II verb still selects teaching or causing knowledge; the governed pen licenses the marking resonance without changing the verb's sense.\",\"representative_source_ids\":[\"QS-4837ecfe\",\"QS-fe8ebfbc\",\"MS-5feda112\",\"QY-56cfef8b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:2:object-ellipsis-and-forward-uptake","source_type":"word_analysis","support_id":"sup_865648907c9cf01f1573","text":"{\"blocking_evidence\":null,\"headline\":\"missing learner and content make 96:5 answer the gap\",\"reader_payoff\":\"The reader notices the pause created when learner and content are omitted in 96:4, then hears 96:5 fill those opened slots.\",\"reason\":\"QAC states that this Form II verb normally takes learner and content objects but both are elided here, while the CRITICAL rows give the concrete uptake in 96:5.\",\"representative_source_ids\":[\"QG-56d6d5b7\",\"QG-d6335f2c\",\"MG-372cbf8b\",\"QE-35913830\",\"QY-82324333\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:1:command-to-description-shift","source_type":"word_analysis","support_id":"sup_94aaca2fd4199dee1f6d","text":"{\"blocking_evidence\":null,\"headline\":\"imperative frame turns into divine characterization\",\"reader_payoff\":\"The reader notices the boundary movement from being commanded to read to being shown the divine action that grounds the command.\",\"reason\":\"The ayah opens with third-person relative description after the earlier imperative {{ar:ٱقْرَأْ}} ({{tr:iqraʾ}}), so the register shift is locally visible.\",\"representative_source_ids\":[\"QI-c05c7723\",\"QB-a49ea450\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:3:rare-distribution-salience","source_type":"word_analysis","support_id":"sup_9c23b840a332f39fad6c","text":"{\"blocking_evidence\":null,\"headline\":\"small q-l-m distribution makes this use inspectable\",\"reader_payoff\":\"The reader notices that the phrase belongs to a small, inspectable Quranic distribution, making this bāʾ-bound teaching use unusually salient.\",\"reason\":\"The contextual profile marks the noun root as low-occurrence, and the CRITICAL row treats the exact prepositional form as a marked construction.\",\"representative_source_ids\":[\"QI-31f6df29\",\"QI-cc19a8f0\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:2:form-ii-perfect-causative-teaching","source_type":"word_analysis","support_id":"sup_a0dfb3d50868017ed366","text":"{\"blocking_evidence\":null,\"headline\":\"perfect Form II turns knowing outward as teaching\",\"reader_payoff\":\"The reader notices that the verb does not merely say the subject knows; it presents a completed act of causing knowledge in another.\",\"reason\":\"QAC identifies {{ar:عَلَّمَ}} ({{tr:ʿallama}}) as a 3ms perfect Form II verb, and the root branch includes knowledge, learning, teaching, and informing.\",\"representative_source_ids\":[\"QG-fc6a59d3\",\"QF-c3d051ef\",\"MF-508e411c\",\"QI-0a7dff2c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:1:creation-teaching-relative-parallel","source_type":"word_analysis","support_id":"sup_a23499de1d68fae1917e","text":"{\"blocking_evidence\":null,\"headline\":\"same relative frame pairs creation and teaching\",\"reader_payoff\":\"The reader notices the repeated relative frame linking the creator description in 96:1 with the teacher description in 96:4.\",\"reason\":\"The CRITICAL rows give a concrete same-surah parallel, and the local grammar supports another relative clause of divine action after {{ar:ٱلَّذِى خَلَقَ}} ({{tr:alladhī khalaqa}}) in 96:1.\",\"representative_source_ids\":[\"QT-792b5d8e\",\"MT-1a79973a\",\"QE-1aa8f1cf\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:3:local-lam-mim-sound-link","source_type":"word_analysis","support_id":"sup_a4dfb19a704a0de69677","text":"{\"blocking_evidence\":null,\"headline\":\"pen echoes the teaching verb while keeping roles distinct\",\"reader_payoff\":\"The reader notices that the pen word echoes the teaching verb in lām-mīm sound and also carries the -lam close toward 96:5, while its root and role remain distinct.\",\"reason\":\"The local sound relation is visible between {{ar:عَلَّمَ}} ({{tr:ʿallama}}), {{ar:ٱلْقَلَمِ}} ({{tr:al-qalami}}), and the next-ayah close in 96:5, but the distinct roots keep action and instrument separate.\",\"representative_source_ids\":[\"QE-16d5b37c\",\"QE-4de02eaa\",\"QP-1e718d2f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:2","source_type":"word_analysis","support_id":"sup_a6996e2e97439a69a043","text":"{\"gloss_range\":\"Form II perfect causative teaching, with learner and content elided and the pen phrase stated as instrument\",\"prose\":\"{{ar:عَلَّمَ}} ({{tr:ʿallama}}) is a perfect Form II verb, so the clause presents teaching as an accomplished act of causing knowledge, not merely divine possession of knowledge. Its normal double-object frame is striking here because both learner and content are withheld; the only expressed complement is {{ar:بِٱلْقَلَمِ}} ({{tr:bi-l-qalami}}), which shifts attention from what was taught to the means by which teaching happens. That openness is then taken up in 96:5, where the next ayah supplies human recipient and unknown content; the same-surah knowledge thread also continues at 96:14. The broader {{ar:ع ل م}} ({{tr:ʿ-l-m}}) field includes both knowing and marking, and the governed pen lets that sign-making pressure survive without replacing the local teaching sense. Within the relative clause, the verb supplies the deed that specifies supreme generosity from 96:3 and grounds the command to read. Wider teaching scenes sharpen the local axis: 2:31 foregrounds taught content, 55:2 foregrounds taught text, and 96:4 foregrounds the method by the pen. Its lām-mīm sound also locks it to the closing pen word.\",\"root_display\":\"{{ar:ع ل م}} ({{tr:ʿ-l-m}})\",\"root_gloss_range\":\"knowledge, knowing, teaching, informing, and marking/sign branches are in the broader root family; local Form II selects caused knowing or teaching while the pen keeps sign-making pressure relevant\",\"surface_display\":\"{{ar:عَلَّمَ}} ({{tr:ʿallama}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:3:rare-qalam-distribution","source_type":"word_analysis","support_id":"sup_a7a0eeffbb1fe95f25db","text":"{\"blocking_evidence\":null,\"headline\":\"rare pen field includes oath, lots, and finite pens\",\"reader_payoff\":\"The reader notices that this rare noun belongs to a small Quranic field where the pen can be elevated by oath in 68:1, broadened to lot-casting sticks in 3:44, and limited before divine words in 31:27.\",\"reason\":\"The contextual profile marks {{ar:ق ل م}} ({{tr:q-l-m}}) as low-occurrence, and the cited parallels are concrete; they widen the lexical field without making lot-casting or oath function the local parse in 96:4.\",\"representative_source_ids\":[\"QS-957ba2be\",\"MS-90850c0f\",\"QI-5ee8a28e\",\"QI-8cc916a7\",\"QI-f31caa0a\",\"MI-8d7f1553\",\"MI-cfbdf8a9\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:3:ellipsis-and-final-instrument-focus","source_type":"word_analysis","support_id":"sup_b9f6dd1db0cce035d2d7","text":"{\"blocking_evidence\":null,\"headline\":\"object ellipsis makes the final instrument load-bearing\",\"reader_payoff\":\"The reader notices that the ayah closes not on learner or content but on the only expressed complement, and that the supplied evidence treats this teaching-by-pen construction as a unique pairing.\",\"reason\":\"QAC confirms that both expected objects of the teaching verb are absent while the instrumental PP remains, and the CRITICAL rows preserve the final-position effect.\",\"representative_source_ids\":[\"QT-23c45cb2\",\"QT-6cf1c4e3\",\"QT-c64bdfca\",\"QH-556b9a44\",\"QH-817e50ac\",\"MH-2bb62df5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:1:identity-through-teaching","source_type":"word_analysis","support_id":"sup_bed3f8363d4f1b0d18b6","text":"{\"blocking_evidence\":null,\"headline\":\"empty relative receives identity from its ṣila\",\"reader_payoff\":\"The reader notices that the pronoun itself is not the lexical center; it makes the act of teaching supply the identifying content.\",\"reason\":\"The relative word is a grammatical connector whose identifying force is completed by the following clause, so the divine subject is characterized through deed.\",\"representative_source_ids\":[\"MG-c457524e\",\"QS-d0d03aa6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:1:antecedent-and-relative-scope","source_type":"word_analysis","support_id":"sup_c44df8fb1c01190ef8eb","text":"{\"blocking_evidence\":null,\"headline\":\"relative pronoun carries 96:3 into the whole clause\",\"reader_payoff\":\"The reader notices that 96:4 is not a standalone report; its first word makes the teaching clause grammatically depend on the prior Lord-description in 96:3.\",\"reason\":\"QAC and attachment evidence identify {{ar:ٱلَّذِى}} ({{tr:alladhī}}) as a relative pronoun whose antecedent is outside the ayah, specifically the prior divine referent in 96:3.\",\"representative_source_ids\":[\"QG-1d2f0b50\",\"QG-b3ead82b\",\"QG-ba42baa7\",\"QT-3960f490\",\"QB-25a1ddb6\",\"QY-8eaa7f4f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:2:sound-and-form-pressure","source_type":"word_analysis","support_id":"sup_ca69b9cd66b189dc8c97","text":"{\"blocking_evidence\":null,\"headline\":\"geminated verb sounds its causative force\",\"reader_payoff\":\"The reader notices that the verb's doubled lām audibly carries Form II pressure and links the teaching action to the pen's lām-mīm close.\",\"reason\":\"The shaddah belongs to the local Form II surface, and the lām-mīm recurrence across the verb and pen noun is a visible same-ayah sound relation.\",\"representative_source_ids\":[\"QE-ca1e188a\",\"QP-419a0b63\",\"QP-abf9e297\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:3:cut-shaped-writing-instrument","source_type":"word_analysis","support_id":"sup_dc2781d40f0d9281224e","text":"{\"blocking_evidence\":null,\"headline\":\"cutting root image survives inside the writing pen\",\"reader_payoff\":\"The reader notices that the pen is a material, shaped instrument: cutting and trimming background the tool that fixes knowledge into signs.\",\"reason\":\"V4 includes trimming, paring, and writing-pen branches for {{ar:ق ل م}} ({{tr:q-l-m}}), but the local bāʾ phrase selects the writing instrument, so the cutting image is retained as manufacture/background rather than a separate local action.\",\"representative_source_ids\":[\"QS-29e7e8a7\",\"QS-755a5026\",\"QS-c916f2c5\",\"MS-24751f75\",\"QP-2183f3dc\",\"QY-b5698bfc\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:3:visible-and-audible-prepositional-fusion","source_type":"word_analysis","support_id":"sup_e0d83b04f05041704bb3","text":"{\"blocking_evidence\":null,\"headline\":\"attached bāʾ makes instrumentality one written word\",\"reader_payoff\":\"The reader notices that the instrument marker is fused to the definite noun in writing and recitation, making the dependency immediately audible and visible.\",\"reason\":\"The prefixed bāʾ is orthographically attached to the noun and is the same preposition that governs the genitive complement.\",\"representative_source_ids\":[\"QF-55451be8\",\"QP-f3838081\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"96:4:3:instrumental-ba-and-case","source_type":"word_analysis","support_id":"sup_e60af037612aae15e2db","text":"{\"blocking_evidence\":null,\"headline\":\"bāʾ layers medium over a fixed instrumental role\",\"reader_payoff\":\"The reader notices that the phrase can feel like by, through, or with the pen, while grammar fixes the pen as the prepositional instrument of teaching.\",\"reason\":\"QAC and attachment evidence strongly identify bāʾ al-āliyya and genitive government, so cause or accompaniment nuances may be retained only as controlled medium-like readings under the instrumental local parse.\",\"representative_source_ids\":[\"QG-0c181139\",\"QG-4295748a\",\"QG-e7411fa8\",\"MG-2040b3f0\",\"QS-71afe555\",\"MS-06f8a626\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ","ayah_ref":"96:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001040/B001","root_001252/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001040","role":"The branch supplies a thing becoming clear to a knower, which is the result the causative teaching produces.","root":"ع ل م","source_ref":"96:4","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_001252","role":"The branch supplies the prepared writing reed, which serves as the external carrier of that produced clarity.","root":"ق ل م","source_ref":"96:4","source_word_indices":["3"]}],"changed_reading":{"after":"Teaching is the causal externalization of clarity into a transmissible written trace.","before":"Someone teaches while using a pen."},"confidence":"strong","focus_anchor":"Word 2's causative teaching verb is joined through the instrumental construction to word 3's pen.","mechanism":"Knowledge as disclosure into clarity is coupled to a prepared writing instrument. Teaching therefore externalizes an intelligible distinction into a medium that can carry it beyond the teacher's immediate presence.","model_id":"baseline_inscribed_clarity"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_inscribed_clarity","source_type":"hft","support_id":"sup_9a6be11e6bf6a3ca03c4","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ","ayah_ref":"96:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001040/B002","root_001252/B001"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001040","role":"The branch supplies a distinguishing mark that points onward, functioning as the teachable difference produced.","root":"ع ل م","source_ref":"96:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_001252","role":"The branch supplies incremental paring of resistant material, functioning as the selective operation that makes distinctions writable.","root":"ق ل م","source_ref":"96:4","source_word_indices":["3"]}],"changed_reading":{"after":"Teaching by the pen cuts, differentiates, and points, actively forming intelligibility rather than merely storing it.","before":"The pen deposits already formed information."},"confidence":"medium","focus_anchor":"The instrumental pen in word 3 is paired with causative teaching in word 2.","mechanism":"The pen is prepared by paring a hard thing bit by bit, while the teaching root can image a distinguishing mark that points. Their conjunction makes pedagogy a controlled segmentation of an undifferentiated field into legible, directional differences.","model_id":"baseline_differentiating_cuts"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_differentiating_cuts","source_type":"hft","support_id":"sup_bb89bebc77d2a2585d84","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ","ayah_ref":"96:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001040/B002","root_001252/B008"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001040","role":"The branch supplies the visible marker or landmark, functioning as the locator inside a divided field.","root":"ع ل م","source_ref":"96:4","source_word_indices":["2"]},{"branch_id":"B008","mapped_root_id":"root_001252","role":"The branch supplies a region cut off from a larger terrain, functioning as the bounded unit made teachable.","root":"ق ل م","source_ref":"96:4","source_word_indices":["3"]}],"changed_reading":{"after":"The pen makes knowledge tractable by partitioning a field and planting markers within it.","before":"The pen is a single object that conveys content."},"confidence":"exploratory","focus_anchor":"The focus makes the pen the means by which teaching occurs, leaving the instrument's partitioning branches available as secondary activation.","mechanism":"A cut-off region and a boundary-like distinguishing mark jointly image knowledge as a continuous field made navigable by divisions. The pen teaches by delimiting units, domains, and relations that can then be separately recognized.","model_id":"baseline_partitioned_field"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_partitioned_field","source_type":"hft","support_id":"sup_894d5ca19a5dfe791527","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ","ayah_ref":"96:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001040/B002","root_001252/B004"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001040","role":"The branch supplies the distinction that points to one option, functioning as the intelligible result of selection.","root":"ع ل م","source_ref":"96:4","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001252","role":"The branch supplies a pared casting stick used in drawing lots, functioning as a trial that discloses one path among co-present possibilities.","root":"ق ل م","source_ref":"96:4","source_word_indices":["3"]}],"changed_reading":{"after":"Teaching can stage bounded choices whose outcome makes a distinction newly visible to the learner.","before":"Teaching delivers a fixed answer already selected by the teacher."},"confidence":"exploratory","containment":"This is surprising because the casting-stick branch is remote from the ordinary writing-pen sense. It remains focus-anchored in the same noun and gains coherence from the teaching root's distinguishing-mark branch; downstream prose should render it only as a procedural analogy for learning under uncertainty, never as a replacement translation.","focus_anchor":"Word 3's instrument has a branch for a pared stick cast to select among alternatives, while word 2 can produce a distinguishing sign.","outlier_id":"outlier_cast_lot_pedagogy"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_cast_lot_pedagogy","source_type":"hft","support_id":"sup_4f20f93e3ae51afa3f14","trust":"legacy_unbound"}]}
</lane_packet_json>
