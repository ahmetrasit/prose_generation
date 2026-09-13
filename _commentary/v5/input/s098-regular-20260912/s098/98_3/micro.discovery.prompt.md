# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **98:3**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s098-regular-20260912/s098/98_3/micro.discovery.json` and modify nothing
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
  "ayah_ref": "98:3",
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
{"branch_registry":[{"boundary":"Temel kapsam erkekler topluluğudur; kadınların katılımı ve insan dışına aktarım ikincil kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001273/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"erkekler topluluğu ve yakın çevresi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderge, kadınlardan ayrı düşünülen erkekler topluluğudur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir erkeğin yandaşları ile yakın soy çevresi, kadınların bağlı olarak kapsanması ve insan dışına aktarım bu çekirdeğe bağlıdır."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Erkeklerden oluşan topluluğu ve buna bağlı yandaş ya da soy çevresini birlikte karşılayan en kısa açıklamadır.","boundary_detail":"Temel kapsam erkekler topluluğudur; kadınların katılımı ve insan dışına aktarım ikincil kullanımlardır.","branch_image_ar":"جماعة الناس والرجال","concept_gloss":"erkekler topluluğu ve yakın çevresi","contextual_glosses":[{"applicability":"Kadınların ikincil kapsanmadığı temel insan topluluğu bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Temel cinsiyet sınırını ve topluluk anlamını korur."},"facet_ids":["F001"],"text":"erkeklerden oluşan topluluk","usage_role":"contextual"}],"definition":"Temelde erkeklerden oluşan insan topluluğudur; bir erkeğin yandaş ve yakın soy çevresini de anlatabilir. Kadınların topluluğa bağlı olarak kapsanması ve sözün insan dışı varlıklara aktarılması ikincildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderge, kadınlardan ayrı düşünülen erkekler topluluğudur."},{"facet_id":"F002","role":"extension","statement":"Bir erkeğin yandaşları ile yakın soy çevresi, kadınların bağlı olarak kapsanması ve insan dışına aktarım bu çekirdeğe bağlıdır."}],"identity_rationale":"Kaynak ifadesi, sözcüğün temel olarak kadınlar dışındaki erkekler topluluğunu anlattığını, kadınların ancak ikincil biçimde kapsama girebildiğini ve insan dışı varlıklara aktarılabildiğini gösterir. Bu nedenle genel ve cinsiyetçe sınırsız bir topluluk adı olarak sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"aslen erkeklerden oluşan topluluk"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir erkeğin yandaşları ve yakın soy çevresi"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"topluluklar; çoğulun çoğulu"}],"lexicalization_note":"Tanım, temel topluluk anlamını bağlı anlatımlardaki yandaş ve soy çevresi anlamından ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; erkeklerle sınırlı çekirdeği en iyi açıklayan topluluk komşusu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırt edici yönü erkekler topluluğunu çekirdek almasıdır; komşu dal ise topluluğu aşiret, kabile veya ortak iş bağı üzerinden kurar.","focus_only":"Temel kapsamı erkeklerle sınırlar; kadınları ancak bağlı biçimde içeri alır ve insan dışına aktarılabilir.","gloss":"topluluk ve aşiret çevresi","neighbor_only":"Aşiret, kabile ve ortak işi bulunan topluluk türlerini cinsiyet sınırı koymadan adlandırır.","neighbor_ref":"root_001016/B013","relation_type":"near_synonym","shared_zone":"Her iki dal da insanlar arasındaki topluluk ve yakın çevre bağını anlatır."}],"source_phrase_ar":"القوم الرجال دون النساء؛ قوم كل رجل شيعته وعشيرته (ayn;tahdhib)؛ القوم الرجال دون النساء؛ ربما دخل النساء فيه على سبيل التبع (sihah)؛ القوم جماعة الرجال في الأصل دون النساء؛ وفي عامة القرآن أريدوا به والنساء جميعا (mufradat)؛ القوم جمع امرئ ولا يكون ذلك إلا للرجال؛ وربما استعير في غيرهم (maqayis)","source_summary":"Kaynakların ortak çekirdeği erkekler topluluğudur; bir erkeğin yandaşları ve yakın soy çevresi bu kapsamda yer alır. Kadınların bağlı biçimde kapsanması ile insan dışı varlıklara aktarım ayrıca kaydedilir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه القوم بمعنى الرجال دون النساء في الأصل، وجماعة الرجل وشيعته وعشيرته، وقد تدخل النساء تبعا أو يستعار اللفظ لغير الآدميين","what_is_not_ar":"ليس هو القيام والانتصاب ولا القوام والعماد"},"support_links":[]},{"boundary":"Bu dal fiziksel dikilme ve dik duruşla sınırlıdır; niyet, gözetim ve yerleşme anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001273/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"ayağa kalkma ve dik durma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlı ya da cansız bir varlık dik konuma gelir veya dik durumda bulunur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tek ayağa kalkış, ibadet duruşu, kökü üzerinde dik kalan bitki ve duran hayvan fiziksel çekirdeğin bağlama özgü görünümleridir."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel olarak dik konuma gelme ile o konumda bulunma aşamalarını birlikte karşılar.","boundary_detail":"Bu dal fiziksel dikilme ve dik duruşla sınırlıdır; niyet, gözetim ve yerleşme anlamlarını kapsamaz.","branch_image_ar":"انتصاب وقيام بالبدن","concept_gloss":"ayağa kalkma ve dik durma","contextual_glosses":[{"applicability":"Bitki veya başka bir varlığın kendi temeli üzerinde dik durumda kalmasını anlatır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dik duruşu ve bu duruşun sürmesini korur."},"facet_ids":["F002"],"text":"dikili kalmak","usage_role":"contextual"}],"definition":"Bir insanın ya da başka bir varlığın dik konuma gelmesi veya dik durumda bulunmasıdır. Tek seferlik ayağa kalkma, ibadetteki ayakta duruş, bitkinin kökü üzerinde kalması ve hayvanın durması bu fiziksel duruşun özel görünümleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlı ya da cansız bir varlık dik konuma gelir veya dik durumda bulunur."},{"facet_id":"F002","role":"specialization","statement":"Tek ayağa kalkış, ibadet duruşu, kökü üzerinde dik kalan bitki ve duran hayvan fiziksel çekirdeğin bağlama özgü görünümleridir."}],"identity_rationale":"Kaynak ifadesi bedeni dik konuma getirme ve dik durma çekirdeğini açıkça destekler. Tek seferlik ayağa kalkma, ibadet sırasındaki duruş, bitkinin kökü üzerinde dik kalması ve hayvanın durması bu fiziksel çekirdeğin farklı gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ayağa kalkmak veya dikilmek"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir kez ayağa kalkma; iki bölüm arasındaki ayakta duruş"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"kökleri üzerinde dikili kalmış"}],"lexicalization_note":"Fiziksel dik duruş çekirdeği korunur; belirli duruş ve kök üzerinde kalma anlatımları ona bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; fiziksel dik duruşla en doğrudan örtüşen aday sınır farkıyla yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hem dik konuma geçişi hem çeşitli bağlamlardaki duruşu içerir; komşu dalın kartı yalnız dik ve ayakta olma niteliğini bildirir.","focus_only":"Ayağa kalkma hareketini, tek seferlik kalkışı ve ibadet, bitki ile hayvan bağlamlarını da kapsar.","gloss":"dikilme ve dik duruş","neighbor_only":"Betimlenen varlığın dik ve ayakta olma niteliğini daha yalın biçimde öne çıkarır.","neighbor_ref":"root_000877/B008","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı bir varlığın dik ve ayakta bulunmasıdır."}],"source_phrase_ar":"القومة ما بين الركعتين من القيام؛ قمت قياما؛ منها هامد ومنها قائم (ayn;tahdhib)؛ قام الرجل قياما؛ القومة المرة الواحدة؛ قامت الدابة وقفت (sihah)؛ قيام بالشخص إما بتسخير أو اختيار؛ ساجدا وقائما؛ تركتموها قائمة على أصولها (mufradat)؛ قام قياما والقومة المرة الواحدة إذا انتصب (maqayis)","source_summary":"Kaynaklar dikilme ve dik durma çekirdeğinde birleşir; tek bir ayağa kalkışın yanı sıra ibadet, bitki ve hayvan bağlamlarını da bu çekirdeğe bağlar.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه قام قياما، والقومة مرة الانتصاب، والقيام في الصلاة أو الذكر، وقيام الشجر والنبت على أصله، ووقوف الدابة","what_is_not_ar":"ليس هو العزم على الأمر ولا حفظ الشيء ورعايته ولا إقامة المكان"},"support_links":[]},{"boundary":"Dal yalnız belirli bir işe yönelip onu üstlenme yapısında geçerlidir; fiziksel ayağa kalkma değildir.","branch_kind":"collocation","branch_ref":"root_001273/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"bir işe kararlılıkla girişme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi belirli bir işe kesin niyetle yönelir, işi üstlenir ve ona girişir."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Niyet, yönelme ve işi üstlenme bileşenlerini tek bir yapıda karşılar.","boundary_detail":"Dal yalnız belirli bir işe yönelip onu üstlenme yapısında geçerlidir; fiziksel ayağa kalkma değildir.","branch_image_ar":"عزم ونهوض إلى الأمر","concept_gloss":"bir işe kararlılıkla girişme","contextual_glosses":[{"applicability":"Kararın yalnız düşüncede kalmayıp belirli bir işin başlatıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Üstlenme ve eyleme geçiş aşamalarını korur."},"facet_ids":["F001"],"text":"işi üstlenip harekete geçmek","usage_role":"contextual"}],"definition":"Belirli bir işe kararlılıkla yönelmek, onu üstlenmek ve yapmaya girişmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi belirli bir işe kesin niyetle yönelir, işi üstlenir ve ona girişir."}],"identity_rationale":"Kaynak ifadesi, belirli bir işe yönelip onu üstlenme anlamındaki kararlı niyet ve girişimi destekler. Anlam yalnız zihinsel isteme değil, işe doğru yönelme ve onu üzerine alma aşamasına da bağlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"bu işi üstlenip kararlılıkla girişti"}],"lexicalization_note":"Tanım yalnız bir işe yönelme ve o işi üstlenme yapısına bağlanır; yalın eyleme genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; niyet ile fiilî giriş arasındaki sınırı en açık gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda kararlı niyet işe girişle gerçekleşir; komşu dalın çekirdeği ise kararın zihinde bağlanıp kesinleştirilmesidir.","focus_only":"Kararı belirli bir işi üstlenme ve o işe doğru harekete geçme aşamasına taşır.","gloss":"kesin karar ve işe giriş","neighbor_only":"Kararı zihinde kesinleştirmeyi, tereddüdü gidermeyi ve iradeyi sağlamlaştırmayı öne çıkarır.","neighbor_ref":"root_001010/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da belirli bir işi yapmaya yönelik sağlam ve kararlı niyeti içerir."}],"source_phrase_ar":"قام بمعنى العزيمة؛ قام بهذا الأمر إذا اعتنقه؛ قيام عزم (maqayis)؛ القيام الذي هو العزم؛ إذا قمتم إلى الصلاة (mufradat)","source_summary":"Kaynaklar, belirli bir işe yönelen kararlı niyetin o işi üstlenme ve başlatma aşamasına geçtiğini birlikte gösterir.","sources":["MQ","MU"],"what_is_ar":"يدخل فيه القيام بمعنى العزم على الشيء واعتناق الأمر والنهوض إليه","what_is_not_ar":"ليس هو مجرد انتصاب البدن ولا القوام بمعنى العماد"},"support_links":[]},{"boundary":"Çekirdek sürekli gözetim, koruma ve yönetimdir; salt işe girişme veya fiziksel duruş bu dala alınmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001273/B004","candidate_links":[{"candidate_id":"cand_1d1bf4fd781425b8e42c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"sürekli gözetip yönetme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sorumlu kişi ya da güç, bir işi veya topluluğu sürekli gözetir, korur ve yönetir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Her şeyi sürekli yönetip koruma ve bir düzenin ayakta kalmasını sağlama, aynı sorumluluğun en geniş uygulamasıdır."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Koruma, yönetme, sorumluluk ve düzeni sürdürme bileşenlerini birlikte karşılar.","boundary_detail":"Çekirdek sürekli gözetim, koruma ve yönetimdir; salt işe girişme veya fiziksel duruş bu dala alınmaz.","branch_image_ar":"رعاية وحفظ وولاية","concept_gloss":"sürekli gözetip yönetme","contextual_glosses":[{"applicability":"Belirli bir işin sorumluluğunu üstlenip düzenli biçimde yürütme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sorumluluk, koruma ve süreklilik bileşenlerini korur."},"facet_ids":["F001"],"text":"işin başında olup onu korumak","usage_role":"contextual"}],"definition":"Bir işi, topluluğu veya düzeni sorumluluk üstlenerek sürekli gözetmek, korumak, yönetmek ve işler durumda tutmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sorumlu kişi ya da güç, bir işi veya topluluğu sürekli gözetir, korur ve yönetir."},{"facet_id":"F002","role":"specialization","statement":"Her şeyi sürekli yönetip koruma ve bir düzenin ayakta kalmasını sağlama, aynı sorumluluğun en geniş uygulamasıdır."}],"identity_rationale":"Kaynak ifadesinin baskın çekirdeği bir işi, topluluğu ya da düzeni sürekli gözetmek, korumak ve yönetmektir. Aynı ifadede bir işi üstlenmeye değinen unsur önceki niyet dalıyla örtüştüğünden, burada ancak sürekli sorumluluk ve koruma doğurduğu ölçüde kullanılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"işi gözeten, koruyan ve yürüten kişi"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"topluluğun işlerini yöneten kişi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"her şeyi sürekli yöneten ve koruyan"},{"lexical_unit_id":"lu_037","rendering_kind":"ordinary","target_gloss":"onu taşıyamadı veya buna gücü yetmedi"}],"lexicalization_note":"Yalın yönetici ve koruyucu adları ile belirli işi gözetme yapıları ayrıştırılır; yetersizlik anlatımı yalnız kendi sözlük biriminde verilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; koruma ile sürekli yönetim arasındaki farkı en iyi gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal korumayı yönetim ve sürekli sorumlulukla birleştirir; komşu dal koruma ve gözetme görevini daha geniş ve yönetimden bağımsız verir.","focus_only":"Gözetim yanında yönetme, düzenleme ve bir işin ya da topluluğun sorumluluğunu sürekli yürütme vardır.","gloss":"gözetim, koruma ve yönetim","neighbor_only":"Koruma, bekçilik, emanet ve düzenli yoklama görevlerini yönetim zorunluluğu olmadan kapsar.","neighbor_ref":"root_000342/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir şeyi koruma, gözetme ve onunla düzenli olarak ilgilenme alanındadır."}],"source_phrase_ar":"قيم القوم من يسوس أمرهم ويقومهم؛ القائم في الملك ونحوه الحافظ؛ القيوم (ayn)؛ قوام أهل بيته وقيام أهل بيته؛ الذي يقيم شأنهم؛ القيوم اسم من أسماء الله (sihah)؛ قيم القوم الذي يقومهم ويسوس أمرهم؛ القائم بالأمر؛ القيوم القائم على كل شيء (tahdhib)؛ قيام للشيء هو المراعاة للشيء والحفظ له؛ قوامين لله؛ القيوم القائم الحافظ لكل شيء (mufradat)؛ قام بهذا الأمر إذا اعتنقه؛ قوام الدين والحق أي به يقوم (maqayis)","source_summary":"Ortak anlatım, bir işi veya topluluğu koruyup yönetme ve düzenini sürdürme sorumluluğudur. Bir işi üstlenme unsuru, yalnız bu kalıcı gözetim ilişkisine dönüştüğü ölçüde çekirdeğe bağlanır.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه القيام على الشيء أو بالأمر بمعنى الحفظ والمراعاة والمواظبة والسياسة والولاية، والقيم والقوام والقيوم","what_is_not_ar":"ليس هو مجرد القيام بالبدن ولا قيمة السلعة ولا القامة"},"support_links":["sup_6571f8bb4a6b2bb05ae0"]},{"boundary":"Dal, bir şeyi sürdürüp gereğini yerine getirmeye bağlıdır; bir yerde kalma veya fiyat belirleme değildir.","branch_kind":"collocation","branch_ref":"root_001273/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"sürdürüp gereğini yerine getirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey devam ettirilir, işler durumda tutulur veya kendisine düşen gerekler eksiksiz uygulanır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İbadetin ve kutsal kitabın gereklerini uygulamak, genel yerine getirme işleminin özel bağlamıdır."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Devam ettirme, işler halde tutma ve gerekli koşulları uygulama bileşenlerini birlikte karşılar.","boundary_detail":"Dal, bir şeyi sürdürüp gereğini yerine getirmeye bağlıdır; bir yerde kalma veya fiyat belirleme değildir.","branch_image_ar":"إقامة وإدامة وتوفية حق","concept_gloss":"sürdürüp gereğini yerine getirme","contextual_glosses":[{"applicability":"İbadet veya kitap gibi kurallı bir alanın bütün koşullarını yerine getirme bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koşulları ve yükümlülükleri uygulama anlamını korur."},"facet_ids":["F002"],"text":"gereklerini eksiksiz uygulamak","usage_role":"contextual"}],"definition":"Bir şeyi sürdürmek, işler ve düzgün durumda tutmak ya da gereğini ve koşullarını eksiksiz yerine getirmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey devam ettirilir, işler durumda tutulur veya kendisine düşen gerekler eksiksiz uygulanır."},{"facet_id":"F002","role":"specialization","statement":"İbadetin ve kutsal kitabın gereklerini uygulamak, genel yerine getirme işleminin özel bağlamıdır."}],"identity_rationale":"Kaynak ifadesi bir şeyi sürdürme, işler ve düzgün durumda tutma ile onun gereğini ve koşullarını eksiksiz yerine getirme anlamlarını destekler. İbadet ve kutsal kitap örnekleri çekirdeği tanımlamaz, bu genel yerine getirme işlemini özelleştirir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"bir şeyi sürdürmek, işler halde tutmak veya gereğini yerine getirmek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ibadetin ya da kitabın gereklerini eksiksiz uygulamak"}],"lexicalization_note":"Tanım yalnız bir şeyi sürdürme ve onun hakkını ya da koşullarını yerine getirme yapılarına bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; sürdürme işlemiyle sürekli gözetim arasındaki ayrımı açıklayan iç komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gereken işlemleri yerine getirmeye, komşu dal ise işin başında sürekli gözetip yönetmeye dayanır; bu yüzden birbirlerinin yerine geçmezler.","focus_only":"Bir şeyin gereklerini ve koşullarını uygulayarak onu devam ettirme işlemini anlatır.","gloss":"sürdürme ve sorumlu gözetim","neighbor_only":"Bir iş, topluluk veya düzen üzerinde sürekli koruma, gözetim ve yönetim sorumluluğu taşır.","neighbor_ref":"root_001273/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir işin veya düzenin devamını sağlama alanında buluşur."}],"source_phrase_ar":"أقام الشيء أي أدامه؛ يقيمون الصلاة (sihah)؛ أقمت الشيء وقومته فقام بمعنى استقام؛ إقام الصلاة (tahdhib)؛ إقامة الشيء توفية حقه؛ تقيموا التوراة والإنجيل؛ أقيموا الصلاة؛ مقيم الصلاة (mufradat)","source_summary":"Kaynaklar, bir şeyi devam ettirme ve düzgün durumda tutma ile ona ait gerekleri eksiksiz yerine getirmeyi aynı işlem alanında birleştirir. İbadet ve kitap bu işlemin özel nesneleridir.","sources":["SI","TA","MU"],"what_is_ar":"يدخل فيه إقامة الشيء وإدامته، وإقامة الصلاة أو الكتاب بمعنى توفية الحق والشرائط والعمل","what_is_not_ar":"ليس هو الإقامة في المكان ولا القيمة والتقويم"},"support_links":[]},{"boundary":"Çekirdek bir yerde kalma ile bunun yeri veya süresidir; oturum ve topluluk anlamı bağımlı genişlemedir.","branch_kind":"mixed_non_bare","branch_ref":"root_001273/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"bir yerde kalma ve kalınan yer","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi bir yerde kalır; kalınan yer, ayak basılan yer veya kalış süresi bu ilişki üzerinden adlandırılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Oturum ve o oturumda bir araya gelen insanlar, yerleşme çekirdeğinden gelişen adlaşmış uzantılardır."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalış eylemi ile bu eylemin yer ve süre adlarını birlikte karşılar.","boundary_detail":"Çekirdek bir yerde kalma ile bunun yeri veya süresidir; oturum ve topluluk anlamı bağımlı genişlemedir.","branch_image_ar":"مقام وإقامة في موضع","concept_gloss":"bir yerde kalma ve kalınan yer","contextual_glosses":[{"applicability":"Bir kişinin belirli bir yerde sabitlenip orada zaman geçirdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yerle ilişkiyi ve kalışın sürmesini korur."},"facet_ids":["F001"],"text":"yerleşip bir süre kalmak","usage_role":"contextual"}],"definition":"Bir yerde kalmak ve orayı geçici ya da sürekli durulan yer edinmektir; ayak basılan veya kalınan yer ile kalış süresi de bu çekirdekten adlandırılır. Oturum ve bir araya gelmiş topluluk anlamı bunun daha uzak uzantısıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi bir yerde kalır; kalınan yer, ayak basılan yer veya kalış süresi bu ilişki üzerinden adlandırılır."},{"facet_id":"F002","role":"extension","statement":"Oturum ve o oturumda bir araya gelen insanlar, yerleşme çekirdeğinden gelişen adlaşmış uzantılardır."}],"identity_rationale":"Kaynak ifadesi bir yerde kalma eylemini, kalınan ya da ayakta durulan yeri ve kalış zamanını destekler. Oturum ve toplanmış insanlar anlamı, yerleşme çekirdeğinden gelişmiş adlaşmış bir kullanım olarak ayrı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"bir yerde yerleşip kalmak"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ayak basılan veya kalınan yer ya da süre; oturum veya toplanmış topluluk"}],"lexicalization_note":"Bir yerde kalma yapısı ile yer, zaman, oturum ve topluluk bildiren adlaşmış biçimler ayrı facetlerde tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; eylem ile yer ve zaman adları arasındaki kapsam farkını gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kalıştan yer, zaman ve oturum adları da türetir; komşu dal ise kalma ve bekleme eylemiyle sınırlıdır.","focus_only":"Kalış eylemine ek olarak ayak basılan yer, kalınan yer, kalış zamanı, oturum ve topluluk adlarını kapsar.","gloss":"bir yerde kalma","neighbor_only":"Bir yerde bekleme, oyalanma ve o yeri bırakmama eylemini daha doğrudan ve yalın anlatır.","neighbor_ref":"root_001339/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin belirli bir yerde kalması ve oradan ayrılmaması alanında örtüşür."}],"source_phrase_ar":"أقمت بالمكان إقامة ومقاما؛ المقام موضع القدمين؛ المقام والمقامة الموضع الذي تقيم فيه (ayn;tahdhib)؛ المقامة الإقامة؛ المقامة المجلس والجماعة من الناس؛ المقام موضع القيام أو الإقامة (sihah)؛ المقام يكون مصدرا واسم مكان القيام وزمانه؛ المقامة الإقامة؛ لا مقام لكم أي لا مستقر لكم (mufradat)","source_summary":"Kaynaklar bir yerde kalma, kalınan veya ayakta durulan yer ve kalış süresi çevresinde birleşir. Oturum ve toplanmış insanlar anlamı da bu yerleşme alanına bağlı bir uzantı olarak verilir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الإقامة بالمكان، والمقام أو المقامة لموضع القدمين أو موضع الإقامة أو زمانها أو المجلس والجماعة المجتمعة","what_is_not_ar":"ليس هو النيابة بأن يقوم شيء مقام آخر ولا يوم القيامة"},"support_links":[]},{"boundary":"Dal, başkasının yerini ve işlevini üstlenme ilişkisidir; yalnız aynı yerde bulunmayı anlatmaz.","branch_kind":"collocation","branch_ref":"root_001273/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"başkasının yerini ve işlevini alma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yeni katılımcı öncekinin yerini alır ve onun görevini ya da işlevini üstlenir."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer değiştirme ile görev veya işlev üstlenmeyi birlikte karşılar.","boundary_detail":"Dal, başkasının yerini ve işlevini üstlenme ilişkisidir; yalnız aynı yerde bulunmayı anlatmaz.","branch_image_ar":"نيابة وقيام مقام غيره","concept_gloss":"başkasının yerini ve işlevini alma","contextual_glosses":[{"applicability":"Bir kişinin başka bir kişi adına görev yaptığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişisel yer değiştirme ve görev üstlenme ilişkisini korur."},"facet_ids":["F001"],"text":"onun yerine geçip görevini üstlenmek","usage_role":"contextual"}],"definition":"Bir kişi veya şeyin başka birinin ya da başka bir şeyin yerini alması, onun adına iş görmesi veya işlevini üstlenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yeni katılımcı öncekinin yerini alır ve onun görevini ya da işlevini üstlenir."}],"identity_rationale":"Kaynak ifadesi bir kişi veya şeyin başka birinin ya da başka bir şeyin yerini alması, onun adına iş görmesi ve işlevini üstlenmesi çekirdeğini doğrudan destekler. Değer kavramıyla kurulan köken açıklaması da bu yerini tutma ilişkisine dayanır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"onun yerine geçti veya adına görev yaptı"}],"lexicalization_note":"Tanım yalnız birinin veya bir şeyin başkasının yerini tutması yapısına bağlıdır; yalın duruş anlamına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kişisel temsil ile daha geniş yerini tutma kapsamını ayıran aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kişi dışındaki nesne ve karşılık ilişkilerine de açılır; komşu dal kişisel görevlendirme ve temsil ile sınırlıdır.","focus_only":"Kişilerin yanında bir şeyin başka bir şeyin yerini tutmasını ve işlevini üstlenmesini de kapsar.","gloss":"yerine geçip görev üstlenme","neighbor_only":"Özellikle bir kişinin başka biri adına belirli bir işte görev yapmasını anlatır.","neighbor_ref":"root_001571/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişinin başkasının yerinde bulunup onun adına iş görmesini içerir."}],"source_phrase_ar":"القيمة أصله الواو لأنه يقوم مقام الشيء (sihah)؛ قام فلان مقام فلان إذا ناب عنه؛ يقومان مقامهما (mufradat)؛ أصل القيمة الواو وأصله أنك تقيم هذا مكان ذاك (maqayis)","source_summary":"Kaynaklar, bir kişi ya da şeyin diğerinin yerine konması ve onun işlevini üstlenmesi çekirdeğinde birleşir; değer açıklaması da bir şeyin karşılığının onun yerini tutmasına bağlanır.","sources":["SI","MU","MQ"],"what_is_ar":"يدخل فيه قيام شخص أو شيء مقام غيره، وأن يجعل شيء مكان شيء أو يقوم مقامه","what_is_not_ar":"ليس هو مقام الإقامة بالمكان ولا ثمن السلعة نفسه"},"support_links":[]},{"boundary":"Çekirdek fiziksel veya davranışsal düzgünlük ve dengedir; geçim dayanağı, fiyat ve bedensel duruş değildir.","branch_kind":"bare","branch_ref":"root_001273/B008","candidate_links":[{"candidate_id":"cand_3c16643c7f1912f72400","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"düzgünlük, denge ve doğru yoldan sapmama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey fiziksel, davranışsal veya yargısal olarak düz çizgisini korur, dengeli olur ve sapmaz."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Doğru yolda kalma, doğru inanç düzeni ve adil söz, düzgünlük çekirdeğinin davranış ve değer alanına uzanmasıdır."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel düzgünlükten davranışsal doğruluğa uzanan ortak çekirdeği eksiksiz karşılar.","boundary_detail":"Çekirdek fiziksel veya davranışsal düzgünlük ve dengedir; geçim dayanağı, fiyat ve bedensel duruş değildir.","branch_image_ar":"استقامة واعتدال واستواء","concept_gloss":"düzgünlük, denge ve doğru yoldan sapmama","contextual_glosses":[{"applicability":"İnsan, davranış, söz veya işin ölçülü ve doğru olması bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Davranışsal doğruluk ve dengeyi korur."},"facet_ids":["F001","F002"],"text":"doğru ve dengeli olmak","usage_role":"contextual"}],"definition":"Bir yolun, nesnenin, kişinin davranışının, işin ya da sözün eğrilikten ve aşırılıktan uzak, düzgün, dengeli ve doğru olmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey fiziksel, davranışsal veya yargısal olarak düz çizgisini korur, dengeli olur ve sapmaz."},{"facet_id":"F002","role":"extension","statement":"Doğru yolda kalma, doğru inanç düzeni ve adil söz, düzgünlük çekirdeğinin davranış ve değer alanına uzanmasıdır."}],"identity_rationale":"Kaynak ifadesi yolun düz olması, insanın doğru yolu izlemesi, nesnenin düzgünlüğü, işin yoluna girmesi ve sözün adil olması gibi kullanımları ortak bir düzgünlük, denge ve sapmama çekirdeğinde toplar.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"düzgün ve dengeli olmak; doğru yoldan ayrılmamak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"düzgün, dengeli ve doğru"}],"lexicalization_note":"Yalın düzgünlük ve denge çekirdeği tanımlanır; başka dallardaki kalıplaşmış fiyat veya geçim anlamları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; durum, düzeltme işlemi ve davranışsal kapsam farkını gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal düzgünlük durumunu davranış ve doğruluk alanına genişletir; komşu dal düzeltme işlemini ve fiziksel denge örneklerini daha çok öne çıkarır.","focus_only":"Doğru yolda kalma, davranışsal doğruluk, sağlam inanç düzeni ve adil söz alanlarına uzanır.","gloss":"düzgün ve dengeli olma","neighbor_only":"Bir şeyi düzelterek düzgün hale getirme işlemini ve beden, organ, sıcaklık gibi alanlardaki dengeyi kapsar.","neighbor_ref":"root_000991/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da eğrilik ve aşırılıktan uzak düzgünlük ile denge durumunu anlatır."}],"source_phrase_ar":"رمح قويم ورجل قويم؛ القيمة الملة المستقيمة؛ إذا انقاد واستمرت طريقته فقد استقام (ayn)؛ الاستقامة الاعتدال؛ استقام له الأمر؛ قومت الشيء فهو قويم أي مستقيم؛ القوام العدل؛ دينا قيما (sihah)؛ الاستقامة على الطاعة؛ القيم هو المستقيم؛ أقوم كلاما أي أعدل كلاما (tahdhib)؛ الاستقامة في الطريق الذي يكون على خط مستو؛ استقامة الإنسان لزومه المنهج المستقيم؛ دينا قيما أي ثابتا (mufradat)","source_summary":"Kaynaklar fiziksel düzgünlük, dengelilik ve bir çizgiden sapmama çekirdeğini insan davranışına, işe, inanç düzenine ve söze genişletir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه استقامة الطريق أو الإنسان أو الأمر، والاعتدال والاستواء، والقويم والقيم والدين المستقيم وعدل الكلام","what_is_not_ar":"ليس هو قوام المعاش ولا مجرد القيام بالبدن ولا قيمة السلعة"},"support_links":["sup_1d442c9e1534d169a72d"]},{"boundary":"Dal, bir şeyin sürmesini sağlayan dayanak ve geçim temelidir; gözetim eylemi veya beden boyu değildir.","branch_kind":"bare","branch_ref":"root_001273/B009","candidate_links":[{"candidate_id":"cand_1d1bf4fd781425b8e42c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"ayakta tutan dayanak ve geçim temeli","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin varlığını ve düzenini sürdürmesini sağlayan temel dayanak veya düzenleyici unsur bulunur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yaşamı ve bedeni sürdüren yeterli geçim aracı, genel dayanak işlevinin özel gerçekleşmesidir."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Düzeni, bedeni veya yaşamı sürdüren temel unsur ve geçim aracını birlikte karşılar.","boundary_detail":"Dal, bir şeyin sürmesini sağlayan dayanak ve geçim temelidir; gözetim eylemi veya beden boyu değildir.","branch_image_ar":"قوام وعماد ومعاش","concept_gloss":"ayakta tutan dayanak ve geçim temeli","contextual_glosses":[{"applicability":"Bir işin veya düzenin varlığını sürdüren vazgeçilmez unsur bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Temel olma ve düzeni ayakta tutma işlevini korur."},"facet_ids":["F001"],"text":"işin temel dayanağı","usage_role":"contextual"}],"definition":"Bir işin, düzenin, bedenin veya yaşamın ayakta kalmasını sağlayan temel dayanak, düzenleyici unsur ya da yeterli geçim aracıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin varlığını ve düzenini sürdürmesini sağlayan temel dayanak veya düzenleyici unsur bulunur."},{"facet_id":"F002","role":"specialization","statement":"Yaşamı ve bedeni sürdüren yeterli geçim aracı, genel dayanak işlevinin özel gerçekleşmesidir."}],"identity_rationale":"Kaynak ifadesi bir şeyin ayakta kalmasını sağlayan dayanak, düzen, temel unsur ve geçim aracı çekirdeğini destekler. Bedenin bütünlüğü, işin düzeni ve dünya ile sonrası için geçim bu işlevsel dayanma ilişkisinin uygulamalarıdır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"bir şeyi ayakta tutan dayanak, düzen ve geçim temeli"}],"lexicalization_note":"Yalın dayanak ve sürdürme aracı tanımlanır; başka dallardaki yönetim, boy ve fiyat anlamları eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; temel dayanakla geçim kapsamı arasındaki farkı açıklayan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dayanak kavramını geçim ve bedenin sürmesi alanlarına genişletir; komşu dal işin ya da bedenin ana taşıyıcı unsuruna daha dar biçimde odaklanır.","focus_only":"Bedenin bütünlüğünü, yaşamın geçimini ve hem dünya hem sonrası için sürdürme araçlarını da kapsar.","gloss":"temel dayanak","neighbor_only":"Bir işin dayandığı ana unsur ile kalbin bedendeki merkezî rolünü özellikle örnekler.","neighbor_ref":"root_001444/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da bir işin veya bütünün ayakta kalmasını sağlayan ana unsuru anlatır."}],"source_phrase_ar":"هذا الأمر لا قومية له أي لا قوام له؛ القوام من العيش ما يقيمك ويغنيك؛ القيام العماد؛ قوام كل شيء ما استقام به (ayn)؛ قوام الأمر نظامه وعماده؛ قوام الأمر ملاكه؛ جعل الله لكم قياما (sihah)؛ قوام الأمر وملاكه؛ تقيمكم فتقومون بها؛ قوام الجسم تمامه؛ قوام كل شيء ما استقام به (tahdhib)؛ القيام والقوام اسم لما يقوم به الشيء؛ جعلها مما يمسككم؛ قياما للناس أي قواما لهم يقوم به معاشهم ومعادهم (mufradat)؛ قوام الدين والحق أي به يقوم (maqayis)","source_summary":"Kaynaklar bir işin veya varlığın ayakta kalmasını sağlayan dayanak, düzen ve temel unsurda birleşir; yaşamı ve bedeni sürdüren geçim de aynı işlev üzerinden açıklanır.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه القيام أو القوام لما يقوم به الشيء ويثبت، وعماد الأمر ونظامه وملاكه، وما يقيم العيش والجسم والمعاش","what_is_not_ar":"ليس هو الرعاية والولاية نفسها ولا الطول والقامة ولا ثمن السلعة"},"support_links":["sup_6571f8bb4a6b2bb05ae0"]},{"boundary":"Dal ekonomik değer biçme ve bedelle sınırlıdır; genel olarak başkasının yerini alma veya temel dayanak değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001273/B010","candidate_links":[{"candidate_id":"cand_e8ed5e9a123495502918","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"değer biçme ve belirlenen bedel","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir mala değer biçilir ve bu işlem sonucunda onun bedeli belirlenir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tarafların bir malın değeri üzerinde karşılıklı hesaplaşması, değer biçme çekirdeğine bağlı kullanımdır."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Değerlendirme işlemi ile bu işlemden çıkan parasal sonucu birlikte karşılar.","boundary_detail":"Dal ekonomik değer biçme ve bedelle sınırlıdır; genel olarak başkasının yerini alma veya temel dayanak değildir.","branch_image_ar":"قيمة وتقويم وتسعير","concept_gloss":"değer biçme ve belirlenen bedel","contextual_glosses":[{"applicability":"Bir malın parasal karşılığının değerlendirme yoluyla saptandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Mala değer biçme işlemini ve parasal sonucu korur."},"facet_ids":["F001"],"text":"malın bedelini belirlemek","usage_role":"contextual"}],"definition":"Bir malın parasal değerini belirlemek ve bu değerlendirme sonucunda ortaya çıkan bedeldir; tarafların değer üzerinde karşılıklı hesaplaşması da bu alana bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir mala değer biçilir ve bu işlem sonucunda onun bedeli belirlenir."},{"facet_id":"F002","role":"associated_use","statement":"Tarafların bir malın değeri üzerinde karşılıklı hesaplaşması, değer biçme çekirdeğine bağlı kullanımdır."}],"identity_rationale":"Kaynak ifadesi bir malın bedelini belirleme işlemini, bu işlemle ortaya çıkan değeri ve tarafların bu değer üzerinde hesaplaşmasını destekler. Bir şeyin yerini tutma düşüncesi kökensel açıklamadır; dalın güncel çekirdeği değer biçme ve belirlenen bedeldir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"değer biçmeyle belirlenen bedel"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"malın değerini belirlemek veya ulaştığı bedeli bildirmek"}],"lexicalization_note":"Belirlenen bedel ile mala değer biçme yapıları ayrılır; kapsam genel değiş tokuşa veya yerini tutmaya genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; değer biçme ile satış karşılığı arasındaki sınırı en iyi gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal değer biçme işlemi ve bunun sonucuna dayanır; komşu dal satış karşılığını ve bedelin yüksekliğini de kapsayan daha geniş bir alışveriş alanıdır.","focus_only":"Malın değerini değerlendirme yoluyla belirleme işlemini ve belirlenen değeri içerir.","gloss":"değer ve satış bedeli","neighbor_only":"Satışta alınan karşılığı, değiş tokuş bedelini, bedelin çokluğunu ve şeyin pahalı oluşunu da kapsar.","neighbor_ref":"root_000206/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da bir malın parasal değeri ve satışta karşılık olarak verilen bedel alanında örtüşür."}],"source_phrase_ar":"القيمة ثمن الشيء بالتقويم؛ تقاوموا فيما بينهم (ayn)؛ قومت السلعة؛ استقمت السلعة؛ القيمة واحدة القيم (sihah)؛ القيمة ثمن الشيء بالتقويم؛ تقاوموه فيما بينهم؛ استقمت المتاع أي قومته؛ قامت الأمة مائة دينار أي بلغت قيمتها (tahdhib)؛ تقويم السلعة بيان قيمتها (mufradat)؛ قومت الشيء تقويما؛ أصل القيمة الواو (maqayis)","source_summary":"Kaynaklar, malın bedelini değerlendirme yoluyla belirleme ve belirlenen değeri adlandırma çekirdeğinde birleşir; karşılıklı değer hesabı da buna bağlanır.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه القيمة ثمن الشيء، وتقويم السلعة أو المتاع، والتقاوم أو الاستقامة بمعنى بيان القيمة","what_is_not_ar":"ليس هو النيابة العامة ولا القوام بمعنى العماد"},"support_links":["sup_ffc9f173b9a085642696"]},{"boundary":"Dal insanın boyu ve düzgün beden yapısıyla sınırlıdır; kuyu aracı veya başka nesnelerin dik parçası değildir.","branch_kind":"bare","branch_ref":"root_001273/B011","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"insanın boyu ve düzgün beden yapısı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanın dik bedeni üzerinden belirlenen boyu ve dış beden yapısı anlatılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Boyun düzgün ve güzel olması, genel beden ölçüsünün olumlu nitelendirilmiş biçimidir."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Boy ölçüsü, dik duruş ve güzel uzunluk bileşenlerini birlikte karşılar.","boundary_detail":"Dal insanın boyu ve düzgün beden yapısıyla sınırlıdır; kuyu aracı veya başka nesnelerin dik parçası değildir.","branch_image_ar":"قامة وقوام الجسم والطول","concept_gloss":"insanın boyu ve düzgün beden yapısı","contextual_glosses":[{"applicability":"İnsanın beden uzunluğunun olumlu biçimde nitelendirildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Boyu, düzgünlüğü ve olumlu dış görünüşü korur."},"facet_ids":["F002"],"text":"düzgün ve güzel boy","usage_role":"contextual"}],"definition":"İnsanın ayakta dururken görülen boy ölçüsü, dik beden yapısı ve özellikle düzgün, güzel uzunluğudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanın dik bedeni üzerinden belirlenen boyu ve dış beden yapısı anlatılır."},{"facet_id":"F002","role":"specialization","statement":"Boyun düzgün ve güzel olması, genel beden ölçüsünün olumlu nitelendirilmiş biçimidir."}],"identity_rationale":"Kaynak ifadesi insan bedeninin dik duruşla ölçülen boyunu, beden yapısını ve özellikle düzgün, güzel boyu destekler. Bedenin bütünlüğüne değinen unsur burada uzunluk ve dış yapı açısından anlaşılmalı, geçim veya düzen dayanağıyla karıştırılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"insanın boyu ve beden uzunluğu"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"düzgün ve güzel boy; beden yapısı"}],"lexicalization_note":"İnsanın boy ve düzgün beden yapısı tanımlanır; araç parçaları ve geçim dayanağı anlamları dışarıda tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; boy ölçüsüyle genel dış görünüş arasındaki sınırı açıklayan aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği boy ölçüsü ve düzgün uzunluktur; komşu dal yüz ve genel görünüşü de içine alan daha geniş bir beden betimlemesidir.","focus_only":"Ayakta duruşla ölçülen boyu, dik beden yapısını ve özellikle düzgün uzunluğu öne çıkarır.","gloss":"boy ve dış görünüş","neighbor_only":"Boyun yanında bedenin, yüzün ve genel dış görünüşün güzel oluşunu daha geniş biçimde kapsar.","neighbor_ref":"root_000053/B006","relation_type":"near_synonym","shared_zone":"Her iki dal da insanın boyunu, beden yapısını ve dış görünüşünü anlatabilir."}],"source_phrase_ar":"القامة مقدار قيام الرجل؛ قوام الجسم تمامه وطوله (ayn)؛ قوام الرجل قامته وحسن طوله؛ قامة الإنسان قده (sihah)؛ القامة قامة الرجل؛ حسن القامة والقمة والقومية؛ قوام الجسم تمامه (tahdhib)؛ تقويم الإنسان في أحسن تقويم؛ انتصاب القامة (mufradat)؛ القوام الطول الحسن؛ القومية القوام والقامة (maqayis)","source_summary":"Kaynaklar insanın ayakta duruşla ölçülen boyu ve beden yapısında birleşir; düzgün ve güzel uzunluk bu ölçünün nitelendirilmiş biçimi olarak verilir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه القامة مقدار طول الإنسان أو قامته، والقوام والقومية وحسن الطول، وانتصاب القامة","what_is_not_ar":"ليس هو القامة بمعنى آلة البئر ولا قائمة السيف والدابة"},"support_links":[]},{"boundary":"Dal araç ve dik parça adlarıyla sınırlıdır; tartışmalı insan biçimli kuyu yapısı yalnız kaynak görüşü olarak belirtilir.","branch_kind":"mixed_non_bare","branch_ref":"root_001273/B012","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"düzeneğin dik, taşıyıcı veya tutulan parçası","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir araç veya varlığın dik duran, taşıyan ya da elle tutulan işlevsel parçası adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kuyu başında insan biçiminde yapılmış bir düzenek açıklaması aktarılmış, fakat başka bir kaynakça yorumunda yanlış sayılmıştır."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuyu aracı, sap, ayak ve tutma çubuğunun ortak işlevsel parça niteliğini karşılar.","boundary_detail":"Dal araç ve dik parça adlarıyla sınırlıdır; tartışmalı insan biçimli kuyu yapısı yalnız kaynak görüşü olarak belirtilir.","branch_image_ar":"آلة قائمة وجزء قائم","concept_gloss":"düzeneğin dik, taşıyıcı veya tutulan parçası","contextual_glosses":[{"applicability":"Suyun kuyudan çekilmesinde kullanılan makara ve ona bağlı düzenek bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kuyu aracı ile ona bağlı donanımın işlevini korur."},"facet_ids":["F001"],"text":"kuyu makarası ve donanımı","usage_role":"contextual"}],"definition":"Bir düzeneğin dik duran, taşıyan veya elle tutulan parçasıdır; kuyu makarası ve donanımı, kılıç sapı, yatak ya da hayvan ayağı ve çiftçinin tuttuğu ahşap parça bu alandadır. Kuyu başında insan biçimli yapı yorumu tartışmalıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir araç veya varlığın dik duran, taşıyan ya da elle tutulan işlevsel parçası adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Kuyu başında insan biçiminde yapılmış bir düzenek açıklaması aktarılmış, fakat başka bir kaynakça yorumunda yanlış sayılmıştır."}],"identity_rationale":"Kaynak ifadesi kuyu düzeneğini, kılıç sapını, yatak ve hayvan gibi varlıkların dik parçasını ve çiftçinin tuttuğu ahşap parçayı aynı araç-parça alanında toplar. Kuyu başında insan biçimli yapı açıklaması açıkça tartışmalıdır ve güvenilir çekirdek olarak sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kuyu makarası veya ona bağlı donanım"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kuyu başındaki insan biçimli yapı diye aktarılmış, fakat yanlış sayılmış yorum"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"kılıç sapı veya yatak, masa ve hayvanın dik duran parçası"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"çiftçinin elinde tuttuğu ahşap parça"}],"lexicalization_note":"Kuyu aracı, sap, ayak ve çiftçi çubuğu ayrı araç-parça görünümleri olarak tutulur; tartışmalı yorum genelleştirilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kuyu düzeneğindeki ortak alanı ve parça kapsamındaki farkı gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal farklı araçların işlevsel parçalarını bir araya getirir; komşu dal yalnız kuyunun iki desteği ve üzerindeki düzenek için belirli bir yapısal addır.","focus_only":"Kuyu makarası ve donanımının yanında kılıç sapı, mobilya ya da hayvan ayağı ve çiftçi çubuğunu kapsar.","gloss":"kuyu düzeneğinin parçaları","neighbor_only":"Kuyunun başındaki iki destek ile bunların taşıdığı yatay ahşap ve makaradan oluşan belirli yapıyı anlatır.","neighbor_ref":"root_000631/B006","relation_type":"same_field","shared_zone":"Her iki dal da kuyu başındaki taşıyıcı parçalar ve su çekme düzeneği alanına girer."}],"source_phrase_ar":"القامة مقدار قيام الرجل كهيئة الرجل يبنى على شفير بئر؛ قائم السيف مقبضه؛ قائمة السرير والخوان والدابة (ayn)؛ القامة البكرة بأداتها؛ قائم السيف وقائمته مقبضه؛ القائمة واحدة قوائم الدواب؛ المقوم الخشبة التي يمسكها الحراث (sihah)؛ القامة البكرة التي يستقى بها الماء؛ النعامة الخشبة المعترضة ثم تعلق القامة؛ قائم السيف مقبضه وما سوى ذلك فهو قائمة (tahdhib)؛ القامة البكرة بأداتها (maqayis)","source_summary":"Kanıt kuyu makarası ve donanımı, kılıç sapı, yatak veya hayvanın dik parçası ile çiftçinin tuttuğu ahşabı araç-parça alanında toplar. Kuyu başındaki insan biçimli yapı açıklaması aktarılırken buna karşı çıkan düzeltme de birlikte korunmalıdır.","sources":["AY","SI","TA","MQ"],"what_is_ar":"يدخل فيه القامة للبكرة أو أداتها عند البئر، وقائم السيف، وقائمة السرير والخوان والدابة، والخشبة التي يمسكها الحراث","what_is_not_ar":"ليس هو قامة الإنسان ولا القوم جماعة الناس"},"support_links":[]},{"boundary":"Dal yalnız son saatteki toplu diriliş ve yargılanma günüdür; sıradan kalkma veya yerleşme değildir.","branch_kind":"bare","branch_ref":"root_001273/B013","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"ölülerin diriltildiği ve insanların yargı için kalktığı gün","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Son saat gerçekleşir, ölüler diriltilir ve insanlar yargılanmak üzere ayağa kalkar."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Son saat, diriliş ve toplu yargılanma aşamalarını birlikte karşılar.","boundary_detail":"Dal yalnız son saatteki toplu diriliş ve yargılanma günüdür; sıradan kalkma veya yerleşme değildir.","branch_image_ar":"قيامة وبعث وقيام الساعة","concept_gloss":"ölülerin diriltildiği ve insanların yargı için kalktığı gün","contextual_glosses":[{"applicability":"Ölülerin yeniden yaşama döndürülüp insanların hesap vermek üzere toplandığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Diriliş ve yargılanma günü anlamını korur."},"facet_ids":["F001"],"text":"diriliş ve yargılanma günü","usage_role":"contextual"}],"definition":"Dünyanın sonundaki saatin gerçekleştiği, ölülerin diriltildiği ve insanların yargılanmak üzere ayağa kalktığı gündür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Son saat gerçekleşir, ölüler diriltilir ve insanlar yargılanmak üzere ayağa kalkar."}],"identity_rationale":"Kaynak ifadesi dünyanın sonundaki diriliş gününü, son saatin gerçekleşmesini ve insanların yargılanmak üzere ayağa kalkmasını aynı olay olarak tanımlar. Bu, sıradan ayağa kalkıştan ayrılmış zaman ve inanç alanına ait bir addır.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"ölülerin diriltildiği ve insanların yargı için ayağa kalktığı son gün"}],"lexicalization_note":"Yalın ad, son saatteki diriliş ve insanların yargı için ayağa kalktığı günle sınırlı tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; son gün ile genel yeniden yaşatma işlemi arasındaki sınırı gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli son gün ve toplu yargılanma olayıdır; komşu dal ise bir ölüyü ya da ölü yeri yeniden canlandırma işlemidir.","focus_only":"Son saati, bütün ölülerin diriltilmesini ve insanların yargı için ayağa kalktığı belirli günü anlatır.","gloss":"diriliş ve yeniden yaşatma","neighbor_only":"Ölü bir insanı veya ölü durumdaki bir yeri yeniden yaşama döndürme işlemini zaman sınırı olmadan anlatır.","neighbor_ref":"root_001503/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal da ölümden sonra yeniden yaşama dönme olayını içerir."}],"source_phrase_ar":"القيامة يوم البعث يقوم الخلق بين يدي القيوم (ayn)؛ يوم القيامة معروف (sihah)؛ القيامة يوم البعث يوم يقوم فيه الخلق بين يدي الحي القيوم (tahdhib)؛ القيامة عبارة عن قيام الساعة؛ يوم يقوم الناس لرب العالمين (mufradat)","source_summary":"Kaynaklar son saatin gerçekleşmesi, ölülerin diriltilmesi ve insanların yargılanmak üzere ayağa kalkmasını tek bir son gün anlatımında birleştirir.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه القيامة يوم البعث، وقيام الساعة، وقيام الخلق أو الناس لربهم","what_is_not_ar":"ليس هو القومة الواحدة في الصلاة ولا المقام موضع الإقامة"},"support_links":[]},{"boundary":"Dal karşılıklı karşı koyma ve mücadeleyle sınırlıdır; değer biçme veya koruyucu gözetim değildir.","branch_kind":"collocation","branch_ref":"root_001273/B014","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"karşılıklı direnip mücadele etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taraflar birbirine karşı durur, birbirini engeller ve üstünlük için karşılıklı mücadele eder."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Karşı durma, direnme ve üstünlük mücadelesini birlikte karşılar.","boundary_detail":"Dal karşılıklı karşı koyma ve mücadeleyle sınırlıdır; değer biçme veya koruyucu gözetim değildir.","branch_image_ar":"مقاومة ومنازلة","concept_gloss":"karşılıklı direnip mücadele etme","contextual_glosses":[{"applicability":"Güreş veya savaşta iki tarafın doğrudan karşı karşıya geldiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklı yüzleşme ve fiziksel mücadeleyi korur."},"facet_ids":["F001"],"text":"birbirine karşı durup dövüşmek","usage_role":"contextual"}],"definition":"İki tarafın bir işte, güreşte veya savaşta birbirine karşı durması, direnmesi ve üstün gelmek için mücadele etmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taraflar birbirine karşı durur, birbirini engeller ve üstünlük için karşılıklı mücadele eder."}],"identity_rationale":"Kaynak ifadesi iki tarafın bir işte, güreşte veya savaşta birbirine karşı durması, direnmesi ve mücadele etmesi çekirdeğini destekler. Anlam tek yanlı saldırıdan çok karşılıklı karşı koyma ve yüzleşmedir.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"ona karşı durup mücadele etmek; tarafların birbirine karşı koyması"}],"lexicalization_note":"Tanım yalnız birine karşı durma ve tarafların birbirine karşı koyması yapılarına bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel karşı koyma ile fiziksel çarpışma arasındaki sınırı gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal fiziksel dövüş dışındaki karşı koymayı da kapsar; komşu dalın çekirdeği savaş ve vuruşma bağlamındaki doğrudan çarpışmadır.","focus_only":"Savaş ve güreşin yanında herhangi bir işte karşılıklı direnme ve karşı durmayı da kapsar.","gloss":"karşılıklı mücadele","neighbor_only":"Savaşçıların birbirine vurduğu, denk rakiplerin doğrudan çarpıştığı fiziksel mücadeleyi öne çıkarır.","neighbor_ref":"root_001219/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da karşı karşıya gelen tarafların üstünlük için mücadele etmesini anlatır."}],"source_phrase_ar":"قاومته في كذا أي نازلته (ayn)؛ قاومه في المصارعة وغيرها؛ تقاوموا في الحرب أي قام بعضهم لبعض (sihah)؛ ما زلت أقاوم فلانا في هذا الأمر أي أنازله (tahdhib)","source_summary":"Kaynaklar bir iş, güreş veya savaş bağlamında tarafların birbirine karşı durması ve karşılıklı mücadele etmesi çekirdeğinde birleşir.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه قاومه في الأمر أو المصارعة، وتقاوموا في الحرب أو فيما بينهم بمعنى قام بعضهم لبعض أو نازله","what_is_not_ar":"ليس هو تقويم السلعة ولا القيام على الرعاية"},"support_links":[]},{"boundary":"Dal yalnız belirtilen para birimlerinin tam ve denk ağırlıkta oluşudur; fiyat veya genel ağırlık ölçümü değildir.","branch_kind":"non_bare","branch_ref":"root_001273/B015","candidate_links":[{"candidate_id":"cand_e8ed5e9a123495502918","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"tam ve denk ağırlıktaki para","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Para parçasının ağırlığı belirlenmiş ölçüye tam denk gelir ve fazlalık göstermez."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli para parçasının ölçün ağırlığa eşit ve fazlalıksız oluşunu karşılar.","boundary_detail":"Dal yalnız belirtilen para birimlerinin tam ve denk ağırlıkta oluşudur; fiyat veya genel ağırlık ölçümü değildir.","branch_image_ar":"وزن سواء ومقدار معتدل","concept_gloss":"tam ve denk ağırlıktaki para","contextual_glosses":[{"applicability":"Paranın ağırlığının belirlenmiş ölçüden ne eksik ne fazla olduğu bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ölçüye tam denkliği ve para kapsamını korur."},"facet_ids":["F001"],"text":"ölçün ağırlığa tam denk gelen para","usage_role":"explanatory"}],"definition":"Belirli bir para parçasının ölçün ağırlığa tam eşit olması ve terazide ağır basmamasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Para parçasının ağırlığı belirlenmiş ölçüye tam denk gelir ve fazlalık göstermez."}],"identity_rationale":"Kaynak ifadesi belirli para adlarıyla sınırlı olarak, bir para parçasının ölçün ağırlığa tam denk gelmesini ve ağır basmamasını anlatır. Genel ölçme işlemi veya parasal değer bu özel anlamın parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"ölçün ağırlığa tam denk gelen, ağır basmayan para"}],"lexicalization_note":"Tanım belirtilen para adları ve tam ölçün ağırlık niteliğiyle sınırlı tutulur; yalın kök anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel para niteliğiyle genel ağırlık ölçümü arasındaki farkı gösteren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli paranın ölçüye tam denk gelme niteliğidir; komşu dal genel ağırlık, ölçü ve tartma alanını anlatır.","focus_only":"Belirli para parçalarının ölçün ağırlığa tam eşit ve fazlalıksız olma niteliğini anlatır.","gloss":"ağırlık ve tam ölçü","neighbor_only":"Ağırlık ölçüsünü, tartı aracını ve bir şeye kendi ağırlığını verme işlemini genel olarak kapsar.","neighbor_ref":"root_000202/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da ağırlığın belirli bir ölçüyle karşılaştırılması alanına girer."}],"source_phrase_ar":"دنانير قوم وقيم ودينار قائم أي مثقال سواء لا يرجح (ayn)؛ دنانير قوم وقيم ودينار قائم إذا كان مثقالا سواء لا يرجح (tahdhib)","source_summary":"Kaynaklar belirli para adlarının ölçün ağırlığa tam denk gelmesi ve ağır basmaması konusunda aynı özel tanımı verir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه الدنانير القوم أو القيم، والدينار القائم إذا كان مثقالا سواء لا يرجح","what_is_not_ar":"ليس هو القيمة بمعنى الثمن ولا الاستقامة الأخلاقية"},"support_links":["sup_ffc9f173b9a085642696"]},{"boundary":"Dal yalnız belirtilen su ve hayvan yapılarında geçerlidir; donma ile yorgunluk ayrı alt görünümlerdir.","branch_kind":"collocation","branch_ref":"root_001273/B016","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"donup akmama veya yorulup ilerleyememe","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Su donduğu için akışını yitirir ve hareketsiz kalır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Binek hayvanı durur veya yorgunluk yüzünden yürümeyi sürdüremez."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Su ve binek hayvanına bağlı iki ayrı hareketsizlik sonucunu açıkça ayırarak karşılar.","boundary_detail":"Dal yalnız belirtilen su ve hayvan yapılarında geçerlidir; donma ile yorgunluk ayrı alt görünümlerdir.","branch_image_ar":"جمود ووقوف وكلال","concept_gloss":"donup akmama veya yorulup ilerleyememe","contextual_glosses":[{"applicability":"Binek hayvanının yorulup yoluna devam edemediği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan kapsamını, yorgunluk nedenini ve ilerleyememe sonucunu korur."},"facet_ids":["F002"],"text":"yorgunluktan yürüyemez hale gelmek","usage_role":"contextual"}],"definition":"Su için donarak akmaz duruma gelmek; binek hayvanı için durmak veya yorulup yürüyemez hale gelmektir. İki kullanımın ortak sonucu ilerleme ya da akışın kesilmesidir, nedenleri aynı değildir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Su donduğu için akışını yitirir ve hareketsiz kalır."},{"facet_id":"F002","role":"core","statement":"Binek hayvanı durur veya yorgunluk yüzünden yürümeyi sürdüremez."}],"identity_rationale":"Kaynak ifadesi aynı söz diziminde iki farklı sonuç verir: suyun donup akmaz olması ve hayvanın durması ya da yorgunluktan yürüyememesi. Bunlar ortak bir hareketsiz kalma sonucunda buluşsa da fiziksel nedenleri ayrıdır ve tanımda birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"su dondu veya akmaz halde kaldı"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"binek hayvanı durdu veya yorulup yürüyemedi"}],"lexicalization_note":"Su ve hayvanla kurulan iki yapı ayrı facetlerde tutulur; hareketsizlik yalın kök anlamı olarak genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; nedenli su ve hayvan kullanımlarıyla genel durgunluğu ayıran aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal suyun donması ve hayvanın yorulması gibi belirli nedenlere bağlıdır; komşu dal nedeni zorunlu kılmadan geniş bir durgunluk alanını kapsar.","focus_only":"Suyun donmasını ve binek hayvanının yorgunluk yüzünden ilerleyememesini belirli yapılarda anlatır.","gloss":"hareketsiz kalma","neighbor_only":"Rüzgâr, güneş, at ve makara gibi çeşitli varlıkların çalışmadan veya hareket etmeden yerinde kalmasını kapsar.","neighbor_ref":"root_000894/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da hareketin, akışın veya işleyişin durduğu bir hareketsizlik sonucunu anlatır."}],"source_phrase_ar":"قام الماء جمد؛ قامت الدابة وقفت (sihah)؛ قامت لفلان دابته إذا كلت أو عيت فلم تسر (tahdhib)","source_summary":"Kaynak kanıtı suyun donmasını ve hayvanın durmasını aynı kalıba bağlar; hayvan kullanımı ayrıca yorgunluk nedeniyle yürüyememeyi belirtir. Ortak sonuç hareketsizliktir, fakat nedenler ayrı tutulur.","sources":["SI","TA"],"what_is_ar":"يدخل فيه قيام الماء بمعنى جمود، وقيام الدابة بمعنى وقوفها أو كلالها وعجزها عن السير","what_is_not_ar":"ليس هو القيام المختار بالبدن ولا قيام الشجر على أصله"},"support_links":[]},{"boundary":"Dal günün tam ortasındaki güneş ve gölge durumuyla sınırlıdır; genel yükselme veya fiziksel ayağa kalkma değildir.","branch_kind":"non_bare","branch_ref":"root_001273/B017","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"güneşin tam tepede olduğu öğle ortası","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gün tam ortasına ulaşır; güneşin konumu dengelenir ve gölge çok kısalır."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Günün yarılanması, güneşin orta konumu ve kısa gölge belirtilerini birlikte karşılar.","boundary_detail":"Dal günün tam ortasındaki güneş ve gölge durumuyla sınırlıdır; genel yükselme veya fiziksel ayağa kalkma değildir.","branch_image_ar":"انتصاف النهار وقائم الظهيرة","concept_gloss":"güneşin tam tepede olduğu öğle ortası","contextual_glosses":[{"applicability":"Zamanın günün iki eşit yarısı arasındaki noktaya geldiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Günün ortası ve iki yarının dengelenmesi anlamını korur."},"facet_ids":["F001"],"text":"gün tam yarıya ulaştığında","usage_role":"contextual"}],"definition":"Güneşin göğün ortasında bulunduğu, günün iki yarısının dengelendiği ve gölgenin en kısa duruma yaklaştığı öğle ortasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gün tam ortasına ulaşır; güneşin konumu dengelenir ve gölge çok kısalır."}],"identity_rationale":"Kaynak ifadesi güneşin göğün ortasında bulunduğu, günün iki yarısının dengelendiği ve gölgenin en kısa duruma yaklaştığı öğle ortasını anlatır. Bu, yalnız belirli zaman anlatımlarında görülen bir zaman adlandırmasıdır.","lexical_glosses":[{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"güneşin ortada, günün iki yarısının dengede olduğu öğle vakti"}],"lexicalization_note":"Tanım yalnız öğle ortasını bildiren belirli zaman anlatımlarına bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı zaman noktasını daha dar bir anlatımla veren en yakın aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal zaman noktasını güneş ve gölge belirtileriyle birlikte verir; komşu dal yalnız günün yarılanmasını bildiren belirli anlatıma odaklanır.","focus_only":"Günün yarılanmasının yanında güneşin orta konumunu ve gölgenin çok kısalmasını da belirtir.","gloss":"günün tam ortası","neighbor_only":"Belirli bir gün terazisi anlatımının günün yarılanması anlamına gelmesiyle sınırlıdır.","neighbor_ref":"root_001645/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da günün iki yarısının birbirine denk geldiği öğle ortasını anlatır."}],"source_phrase_ar":"قام قائم الظهيرة إذا قامت الشمس وكاد الظل يعقل (ayn;tahdhib)؛ قام ميزان النهار إذا انتصف؛ قام ميزان النهار فاعتدل (tahdhib)","source_summary":"Kaynaklar güneşin gün ortasındaki konumunu, günün iki yarısının dengelenmesini ve gölgenin çok kısalmasını aynı öğle ortası anlatımında birleştirir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه قيام قائم الظهيرة أو ميزان النهار إذا قامت الشمس وانتصف النهار وكاد الظل يعقل","what_is_not_ar":"ليس هو قيام الشخص ولا قيام السوق"},"support_links":[]},{"boundary":"Dal yalnız pazarın canlanıp satışların artmasıdır; pazar yerinin kurulması veya durgunluk değildir.","branch_kind":"collocation","branch_ref":"root_001273/B018","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"pazarın canlanıp satışların artması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Alıcı ilgisi ve satışlar artar, böylece pazar canlı ve işler hale gelir."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Alıcı ilgisi, satış hareketi ve pazarın işler hale gelmesini birlikte karşılar.","boundary_detail":"Dal yalnız pazarın canlanıp satışların artmasıdır; pazar yerinin kurulması veya durgunluk değildir.","branch_image_ar":"نفاق السوق","concept_gloss":"pazarın canlanıp satışların artması","contextual_glosses":[{"applicability":"Satışların arttığı ve pazarın yeniden işler hale geldiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Alıcı bulma, satış ve pazar canlılığı sonuçlarını korur."},"facet_ids":["F001"],"text":"mallar alıcı bulup pazar canlandı","usage_role":"contextual"}],"definition":"Pazarın canlanması, malların alıcı bulması ve satışların hareketlenmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Alıcı ilgisi ve satışlar artar, böylece pazar canlı ve işler hale gelir."}],"identity_rationale":"Kaynak ifadesi pazarın canlı işlemesi, malların alıcı bulması ve alışverişin hareketlenmesi anlamını açıkça destekler. Aynı kanıtta pazarın uyuması karşıt olarak durgunlaşma anlamında verildiğinden canlılık sınırı belirgindir.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"pazar canlandı ve mallar alıcı buldu"}],"lexicalization_note":"Tanım yalnız pazar öznesiyle kurulan canlanma ve satışların hareketlenmesi yapısına bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; pazar canlılığının doğrudan karşıt kutbunu veren aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dal satış hareketinin artan, komşu dal ise azalan kutbudur; biri canlılığı, diğeri durgunluğu bildirir.","focus_only":"Alıcı ilgisinin ve satışların artmasıyla pazarın canlı ve işler hale gelmesini anlatır.","gloss":"pazarın canlanması ve durgunlaşması","neighbor_only":"İlginin azalmasıyla malın, satışın veya bütün pazarın durgunlaşıp alıcı bulamamasını anlatır.","neighbor_ref":"root_001297/B001","relation_type":"polarity_pair","shared_zone":"Her iki dal da alıcı ilgisine göre pazarın ve satışların durumunu anlatan aynı ekonomik eksendedir."}],"source_phrase_ar":"قامت السوق نفقت (sihah)؛ قامت السوق إذا نفقت ونامت إذا كسدت (tahdhib)","source_summary":"Kaynaklar pazarın canlanması ve malların alıcı bulması anlamında birleşir; durgunluk aynı anlatımda bunun karşıtı olarak belirtilir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه قامت السوق إذا نفقت وراجت","what_is_not_ar":"ليس هو قيام السوق بمعنى اجتماع الناس ولا كسادها"},"support_links":[]},{"boundary":"Dal yalnız bir beden bölümünün kişiye ağrı vermesi yapısında geçerlidir; belirli bir hastalık adı değildir.","branch_kind":"collocation","branch_ref":"root_001273/B019","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"bir beden bölümünün kişiye ağrı vermesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir beden bölümü ağrının kaynağı olur ve kişi o organda acı duyar."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ağrının kaynağı olan organı ve ağrıyı yaşayan kişiyi birlikte gösterir.","boundary_detail":"Dal yalnız bir beden bölümünün kişiye ağrı vermesi yapısında geçerlidir; belirli bir hastalık adı değildir.","branch_image_ar":"وجع قائم بالعضو","concept_gloss":"bir beden bölümünün kişiye ağrı vermesi","contextual_glosses":[{"applicability":"Ağrı kaynağının sırt olduğu doğal bir kişi anlatımında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sırtı, ağrı olayını ve ağrıyı yaşayan kişiyi korur."},"facet_ids":["F001"],"text":"sırtım ağrıdı","usage_role":"contextual"}],"definition":"Sırt, göz veya bedenin başka bir bölümünün kişiye ağrı vermesi ve o kişinin bu organda acı duymasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir beden bölümü ağrının kaynağı olur ve kişi o organda acı duyar."}],"identity_rationale":"Kaynak ifadesi sırt, göz veya bedenin herhangi bir bölümünün kişiye ağrı vermesini belirli bir dil yapısıyla anlatır. Dal bir hastalık adı değil, ağrıyan organ ile ağrıyı duyan kişi arasındaki olay ilişkisidir.","lexical_glosses":[{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"sırtım veya gözlerim ağrıdı"}],"lexicalization_note":"Tanım yalnız beden bölümünün kişiye ağrı vermesini bildiren belirli yapıya bağlı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel ağrı anlatımıyla adlandırılmış ağrı türünü ayıran aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel ağrı olayını belirli bir anlatım kalıbıyla verir; komşu dal ise kırık olmayan belirli bir ağrı türünün adıdır.","focus_only":"Herhangi bir beden bölümünün kişiye ağrı vermesini organ ile kişi arasındaki özel bir dil yapısıyla anlatır.","gloss":"beden bölümünde ağrı","neighbor_only":"Kırık derecesine ulaşmayan, organlarda görülen belirli bir ağrı türünü adlandırır.","neighbor_ref":"root_000417/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da bedenin bir bölümünde duyulan ve kırık olmak zorunda olmayan ağrıyı anlatır."}],"source_phrase_ar":"قام بي ظهري أي أوجعني؛ قامت بي عيناي؛ كل ما أوجعك من جسدك فقد قام بك (tahdhib)","source_qualifications":[{"kind":"sole_attestation","summary":"Sırt ve göz örnekleri, ağrı veren herhangi bir beden bölümüne genellenen bu özel anlatımı gösterir."}],"source_summary":"Kanıt, sırt ve göz örnekleri üzerinden bedenin herhangi bir bölümünün kişiye ağrı vermesini bildiren yapıyı tek başına tanıklar.","sources":["TA"],"what_is_ar":"يدخل فيه قام بي ظهري أو قامت بي عيناي، أي أوجعني العضو","what_is_not_ar":"ليس هو القوام داء الشاة ولا القيام بالبدن"},"support_links":[]},{"boundary":"Dal koyunda bacakları tutan özel hastalıkla sınırlıdır; genel hayvan duruşu veya başka bir organ hastalığı değildir.","branch_kind":"bare","branch_ref":"root_001273/B020","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"koyunun bacaklarını tutan hastalık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hastalık koyunun bacaklarını etkiler ve hayvan bu etki yüzünden ayağa kalkar."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvan türünü, etkilenen bacakları ve hastalık niteliğini açıkça karşılar.","boundary_detail":"Dal koyunda bacakları tutan özel hastalıkla sınırlıdır; genel hayvan duruşu veya başka bir organ hastalığı değildir.","branch_image_ar":"قوام في قوائم الشاة","concept_gloss":"koyunun bacaklarını tutan hastalık","contextual_glosses":[{"applicability":"Hastalığın etkilediği hayvanı, organı ve gözlenen sonucu açıklamak için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Koyunu, bacak etkisini ve ayağa kalkma sonucunu korur."},"facet_ids":["F001"],"text":"koyunu bacaklarından etkileyip ayağa kaldıran hastalık","usage_role":"explanatory"}],"definition":"Koyunun bacaklarını tutan ve hayvanın etkilenerek ayağa kalkmasına yol açan belirli bir hastalıktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hastalık koyunun bacaklarını etkiler ve hayvan bu etki yüzünden ayağa kalkar."}],"identity_rationale":"Kaynak ifadesi koyunun bacaklarını tutan ve hayvanın bu nedenle ayağa kalkmasına yol açan belirli bir hastalık adını destekler. Genel bacak rahatsızlığı, başka hayvan türleri veya bedenin dayanağı anlamı bu dar tanıma eklenmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_035","rendering_kind":"ordinary","target_gloss":"koyunun bacaklarını tutup onu ayağa kaldıran hastalık"}],"lexicalization_note":"Yalın hastalık adı yalnız koyun, bacaklar ve hastalık nedeniyle ayağa kalkma koşullarıyla tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hayvan, organ ve belirti sınırlarını en açık gösteren hastalık komşusu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız koyun bacaklarındaki ve ayağa kalkma sonucunu doğuran hastalıktır; komşu dal daha geniş hayvan ve organ kapsamıyla aksak yürüyüşe bağlanır.","focus_only":"Yalnız koyunun bacaklarını tutan ve onu ayağa kaldıran belirli hastalığı anlatır.","gloss":"küçükbaş hayvanda bacak hastalığı","neighbor_only":"Koyun ve keçilerde bel, yan, kalça ve uyluk bölgelerini etkileyip aksak yürüyüşe yol açan başka bir hastalığı anlatır.","neighbor_ref":"root_001541/B014","relation_type":"near_neighbor","shared_zone":"Her iki dal da küçükbaş hayvanların arka bölümünü veya bacaklarını etkileyen hastalık alanındadır."}],"source_phrase_ar":"القوام داء يأخذ الشاة في قوائمها تقوم منه (sihah)؛ أخذها قوام وهو داء يأخذها في قوائمها تقوم منه (tahdhib)","source_summary":"Kaynaklar, koyunun bacaklarını etkileyip hayvanı ayağa kaldıran belirli hastalık tanımında birleşir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه القوام داء يأخذ الشاة في قوائمها فتقوم منه","what_is_not_ar":"ليس هو قوام الأمر ولا قوائم الدواب أجزاءها"},"support_links":[]},{"boundary":"Dal, görme kaybına karşın göz bebeğinin sağlam kalması koşuluyla sınırlıdır; her türlü körlüğü kapsamaz.","branch_kind":"non_bare","branch_ref":"root_001273/B021","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","surface_ar":"قَيِّمَةٌ"}],"gloss":"göz bebeği sağlamken görme yetisinin kaybolması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Görme yetisi kaybolur, fakat göz bebeği ve gözün görünür yapısı sağlam kalır."}}],"root_ar":"ق و م","root_id":"root_001273","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Görme kaybı ile görünür göz yapısının sağlam kalması koşullarını birlikte karşılar.","boundary_detail":"Dal, görme kaybına karşın göz bebeğinin sağlam kalması koşuluyla sınırlıdır; her türlü körlüğü kapsamaz.","branch_image_ar":"عين قائمة ذاهبة البصر","concept_gloss":"göz bebeği sağlamken görme yetisinin kaybolması","contextual_glosses":[{"applicability":"Dış görünüşü korunmuş bir gözde görme yetisinin yitirildiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sağlam görünüş ile görme kaybı arasındaki karşıtlığı korur."},"facet_ids":["F001"],"text":"gözü sağlam görünse de artık görmeyen","usage_role":"contextual"}],"definition":"Göz bebeği ve gözün görünür yapısı sağlam kaldığı halde görme yetisinin bütünüyle kaybolduğu göz durumudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Görme yetisi kaybolur, fakat göz bebeği ve gözün görünür yapısı sağlam kalır."}],"identity_rationale":"Kaynak ifadesi göz bebeği ve gözün görünür yapısı sağlam kaldığı halde görme yetisinin kaybolduğu özel durumu açıkça tanımlar. Genel körlükten farklı olarak yapısal sağlamlık koşulu bu dalın kurucu sınırıdır.","lexical_glosses":[{"lexical_unit_id":"lu_036","rendering_kind":"ordinary","target_gloss":"göz bebeği sağlam kaldığı halde görmeyen göz"}],"lexicalization_note":"Tanım yalnız göz adıyla kurulan ve sağlam göz bebeğine rağmen görme kaybını bildiren özel birime bağlıdır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel körlükle sağlam göz bebeği koşullu özel durumu ayıran aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yalnız sağlam görünen göz bebeğine eşlik eden görme kaybıdır; komşu dal yapısal koşul koymayan genel körlük alanıdır.","focus_only":"Görme kaybına karşın göz bebeğinin ve görünür göz yapısının sağlam kalmasını zorunlu kılar.","gloss":"körlük ve sağlam görünümlü gözde görme kaybı","neighbor_only":"İki gözdeki genel körlüğü ve körlükle ilgili kişi nitelemelerini, göz yapısının durumunu şart koşmadan kapsar.","neighbor_ref":"root_001049/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da gözün görme yetisini bütünüyle yitirmesi alanında örtüşür."}],"source_phrase_ar":"عين قائمة ذهب بصرها والحدقة صحيحة (ayn)؛ العين القائمة أن يذهب بصرها والحدقة صحيحة (tahdhib)","source_summary":"Kaynaklar görme yetisinin kaybolması ile göz bebeğinin sağlam kalmasını birlikte zorunlu koşul olarak verir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه العين القائمة إذا ذهب بصرها وبقيت الحدقة صحيحة","what_is_not_ar":"ليس هو قيام البصر ولا قيام الشخص"},"support_links":[]},{"boundary":"Dal, yazı yazma ya da hüküm verme anlamını değil, fiziksel veya toplu birleştirme işlemini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001283/B001","candidate_links":[{"candidate_id":"cand_3c16643c7f1912f72400","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"98:3:2:1","qac_word_ref":"98:3:2","surface_ar":"كُتُبٌ"}],"gloss":"bir şeyi başka bir şeye katıp birleştirme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, bir şeyi başka bir şeye katarak ikisini bir bütün veya bağlı bir düzen içinde birleştirmektir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Deri parçalarını ya da bir su tulumunu dikişle birleştirmek, çekirdeğin el işi alanındaki özel gerçekleşmesidir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir hayvanın belirli uzuvlarını halka, kayış veya iple birbirine bağlamak ve bir kabın ağzını sıkıca kapatmak yapıya bağlı kullanımlardır."}},{"facet_id":"F004","role":"extension","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Atların veya askerlerin toplanıp ayrı ve düzenli bir birlik oluşturması, fiziksel birleştirmeden topluluk düzenine uzanan anlamdır."}},{"facet_id":"F005","role":"example","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Kayışın iki yüzünü bir arada tutan boncuk, ortaya çıkan bağın somut bir örneğidir."}}],"root_ar":"ك ت ب","root_id":"root_001283","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bütün özel kullanımlarının dayandığı genel birleştirme işlemi için uygundur.","boundary_detail":"Dal, yazı yazma ya da hüküm verme anlamını değil, fiziksel veya toplu birleştirme işlemini kapsar.","branch_image_ar":"ضم شيء إلى شيء","concept_gloss":"bir şeyi başka bir şeye katıp birleştirme","contextual_glosses":[{"applicability":"Deri parçalarının veya su tulumunun dikişle bir araya getirildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dikiş aracılığıyla gerçekleştirilen birleştirme işlemini tam olarak korur."},"facet_ids":["F002"],"text":"dikerek birleştirmek","usage_role":"contextual"},{"applicability":"Atların veya askerlerin ayrı ve düzenli topluluklar hâlinde toplandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Toplama sonucunda düzenli bir birlik oluşturma anlamını korur."},"facet_ids":["F004"],"text":"birlikler hâlinde düzenlemek","usage_role":"contextual"}],"definition":"Bir şeyi başka bir şeye katıp aralarında fiziksel ya da topluluk oluşturan bir bağ kurmaktır. Derileri dikme, açıklıkları bağlama veya kapatma ve insan ya da atları düzenli bir birlik hâline getirme bunun yapıya bağlı gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, bir şeyi başka bir şeye katarak ikisini bir bütün veya bağlı bir düzen içinde birleştirmektir."},{"facet_id":"F002","role":"specialization","statement":"Deri parçalarını ya da bir su tulumunu dikişle birleştirmek, çekirdeğin el işi alanındaki özel gerçekleşmesidir."},{"facet_id":"F003","role":"specialization","statement":"Bir hayvanın belirli uzuvlarını halka, kayış veya iple birbirine bağlamak ve bir kabın ağzını sıkıca kapatmak yapıya bağlı kullanımlardır."},{"facet_id":"F004","role":"extension","statement":"Atların veya askerlerin toplanıp ayrı ve düzenli bir birlik oluşturması, fiziksel birleştirmeden topluluk düzenine uzanan anlamdır."},{"facet_id":"F005","role":"example","statement":"Kayışın iki yüzünü bir arada tutan boncuk, ortaya çıkan bağın somut bir örneğidir."}],"identity_rationale":"Kaynak ifadesi, anlam çekirdeğini bir şeyi başka bir şeye katıp birleştirmek olarak açıkça kurar; deri dikme, hayvanın bazı uzuvlarını bağlama, boncukla tutturma ve birlik oluşturma kullanımları da bu çekirdeğin özelleşmiş gerçekleşmeleridir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"bir şeyi başka bir şeye katıp birleştirme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"su tulumunu dikerek birleştirmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"katırın üreme organının dudaklarını halka veya kayışla birleştirmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"dişi devenin burun deliklerini iplikle dikmek veya bağlamak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"dişi devenin memelerini bağlamak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"su tulumunun ağzını bağıyla sıkıca kapatmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"kayışın iki yüzünü birleştiren boncuk"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir arada duran atlı veya askerî birlik"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"atların toplanması"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"askerleri birlik birlik düzenlemek"}],"lexicalization_note":"Tanım ortak birleştirme çekirdeğini korur; dikme, bağlama, kapatma ve birlik düzenleme anlamlarını yalnızca tanıklanmış biçim ve yapılara bağlı özelleşmeler olarak verir.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; yayımlanan iki karşılaştırma genel birleştirme ve bağlama sınırındaki en güçlü karışma noktalarını gösterirken diğerleri yalnızca uzak alan veya dal içi çağrışım sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği yakın olsa da tanıklanmış sınırı belirli dikme, bağlama ve topluluk oluşturma kullanımlarıyla şekillenir; komşu dalın kapsama ve eşlik etme uzantıları odak dalın sınırına girmez.","focus_only":"Odak dalda dikiş, uzuv bağlama, kapatma ve askerî birlik oluşturma gibi kalıplaşmış özel gerçekleşmeler bulunur.","gloss":"katıp birleştirme","neighbor_only":"Komşu dal, eşlik etme ve bir şeyin başka bir şeyi içine alması gibi daha geniş kapsama uzanır.","neighbor_ref":"root_000915/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da ayrı unsurları bir araya getirip bağlı bir bütün oluşturma alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal için bağlama yalnızca birleştirmenin yollarından biridir; komşu dalda ise düğüm ve sıkı bağ kurma işlemin kendisini tanımlar.","focus_only":"Odak dal, katma ve birleştirmenin yanı sıra dikişle birleştirme ve topluluk oluşturmayı kapsar.","gloss":"bağlayarak birleştirme","neighbor_only":"Komşu dalın çekirdeği uçları sıkıca bağlama, düğümleme ve düğüm oluşumudur.","neighbor_ref":"root_001034/B001","relation_type":"near_neighbor","shared_zone":"İki dal, parçaların bir bağ aracılığıyla bir arada tutulduğu fiziksel işlemlerde yaklaşır."}],"source_phrase_ar":"أصل صحيح واحد يدل على جمع شيء إلى شيء (maqayis)؛ أصل الكتب ضمك الشيء إلى الشيء (jamhara)؛ ضم أديم إلى أديم بالخياطة (mufradat)؛ كتبت السقاء إذا خرزته (tahdhib)؛ كتبت البغلة إذا جمعت بين شفريها بحلقة (sihah;mufradat)؛ الكتيبة جماعة مستحيزة (sihah;tahdhib)","source_summary":"Kaynakların ortak çizgisi, katma ve birleştirme çekirdeğinin dikiş, bağlama, sıkıca kapatma ve düzenli topluluk oluşturma gibi somut uygulamalarda korunmasıdır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه أصل الجمع والضم، وخرز الأديم والسقاء، وضم شفري الدابة أو صر أخلافها، والخرزة المضمومة، واجتماع الخيل أو الكتيبة.","what_is_not_ar":"ليس المراد هنا الكتاب المكتوب، ولا الفرض والحكم، ولا عقد المكاتبة إلا من جهة أصل الجمع."},"support_links":["sup_1d442c9e1534d169a72d"]},{"boundary":"Dal, yazı üretimi ve yazılı ürünle sınırlıdır; yazının bağlayıcı hüküm için mecazlaşması ayrı dalda tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001283/B002","candidate_links":[{"candidate_id":"cand_3c16643c7f1912f72400","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"98:3:2:1","qac_word_ref":"98:3:2","surface_ar":"كُتُبٌ"}],"gloss":"yazma ve yazılı metin","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel işlem, harfleri yazıyla düzenleyip bir metin oluşturmak veya var olan metni kopyalamaktır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlemin ürünü, yazılmış metin veya üzerinde bu metnin bulunduğu sayfa ya da kitaptır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir metni başkasına söyleyerek yazdırmak ve birinden kendisi için yazmasını istemek yapıya bağlı ettirgen ve isteme kullanımlarıdır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yazmayı öğretmek, yazı öğretmeni ve öğretim yeri anlamları yazı edinimi alanındaki bağlı kullanımlardır."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Öğretim yerindeki çocuklar veya onların topluluğu için kullanılan biçim, yeri değil öğrencileri gösterir."}}],"root_ar":"ك ت ب","root_id":"root_001283","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem harflerden metin oluşturma işlemini hem de ortaya çıkan yazılı ürünü birlikte temsil eder.","boundary_detail":"Dal, yazı üretimi ve yazılı ürünle sınırlıdır; yazının bağlayıcı hüküm için mecazlaşması ayrı dalda tutulur.","branch_image_ar":"نظم الحروف واسم المكتوب","concept_gloss":"yazma ve yazılı metin","contextual_glosses":[{"applicability":"Bir metnin harflerle oluşturulduğu veya mevcut bir metnin yeniden yazıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yazılı metni üretme veya yeniden oluşturma işlemini eksiksiz korur."},"facet_ids":["F001"],"text":"yazmak veya kopyalamak","usage_role":"contextual"},{"applicability":"Metnin başkasına söylenerek yazıya geçirilmesinin sağlandığı yapıya bağlı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yazı eyleminin başka bir kişiye yaptırılması anlamını korur."},"facet_ids":["F003"],"text":"yazdırmak","usage_role":"contextual"}],"definition":"Harfleri çizgiyle düzenleyerek yazılı bir metin oluşturmak ve bu işlemin ürünü olan metin ya da yazılı sayfadır. Birine yazdırma, ondan yazmasını isteme ve yazmayı öğretme ise belirli yapılara bağlı uzantılardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel işlem, harfleri yazıyla düzenleyip bir metin oluşturmak veya var olan metni kopyalamaktır."},{"facet_id":"F002","role":"extension","statement":"İşlemin ürünü, yazılmış metin veya üzerinde bu metnin bulunduğu sayfa ya da kitaptır."},{"facet_id":"F003","role":"associated_use","statement":"Bir metni başkasına söyleyerek yazdırmak ve birinden kendisi için yazmasını istemek yapıya bağlı ettirgen ve isteme kullanımlarıdır."},{"facet_id":"F004","role":"associated_use","statement":"Yazmayı öğretmek, yazı öğretmeni ve öğretim yeri anlamları yazı edinimi alanındaki bağlı kullanımlardır."},{"facet_id":"F005","role":"source_variant","statement":"Öğretim yerindeki çocuklar veya onların topluluğu için kullanılan biçim, yeri değil öğrencileri gösterir."}],"identity_rationale":"Kaynak ifadesi harfleri çizgiyle düzenleyerek yazma işlemini, bunun ürünü olan yazılı metin veya sayfayı ve yazdırma, isteme ya da öğretme gibi yapıya bağlı kullanımları birlikte tanıklar.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"kitabı yazmak veya kopyalamak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"yazılı metin veya üzerinde yazı bulunan sayfa"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"yazma işi ve yazıcılık"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"kitabı yazmak veya kopyalamak"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"ona şiiri söyleyerek yazdırmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"birinden kendisi için bir şey yazmasını istemek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çocuğa yazmayı öğretmek"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"yazı öğretmeni veya yazı öğretilen yer"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"öğretim yerindeki çocuklar veya onların topluluğu"}],"lexicalization_note":"Yazma işlemi ve yazılı ürün dalın merkezindedir; dikte ettirme, başkasından yazmasını isteme ve yazmayı öğretme anlamları yalnızca ilgili yapılara bağlı olarak korunur.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; seçilen üçü yazı, yazılı nesne ve söyleyerek yazdırma sınırlarını doğrudan aydınlatır, kalanlar ise daha dar nesne türleri veya uzak dal içi ilişkiler sunar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Yazma çekirdeğinde güçlü biçimde örtüşürler; odak dal öğretim ve yazdırma yapılarına uzanırken komşu dal kazıma ve taş üzerine işleme alanına uzanır.","focus_only":"Odak dal, kopyalama, yazdırma, yazma isteği ve yazı öğretimiyle ilgili bağlı kullanımları da kapsar.","gloss":"yazı oluşturma","neighbor_only":"Komşu dal, sözün taşa kazınması ve yazıya ek olarak oyma işlemini açıkça kapsar.","neighbor_ref":"root_001633/B003","relation_type":"near_synonym","shared_zone":"İki dal da sözün görünür işaretlerle kayda geçirilmesini ve ortaya çıkan yazılı ürünü kapsar."},{"boundary_match":"field_only","distinction":"Komşu dal nesne türünü tanımlar; odak dal ise nesnenin yanı sıra yazı oluşturma işlemini de kurucu anlam olarak içerir.","focus_only":"Odak dal hem yazma işlemini hem yazılı ürünü ve yazıyla ilgili bağlı eylemleri kapsar.","gloss":"yazılı sayfa","neighbor_only":"Komşu dalın çekirdeği, üzerine yazı yazılan veya yazı taşıyan sayfanın kendisidir.","neighbor_ref":"root_000845/B002","relation_type":"same_field","shared_zone":"Her iki dal yazı taşıyan sayfa veya yazılı ürün alanında buluşur."},{"boundary_match":"partial","distinction":"Söyleme işlemi komşu dalın merkezidir; odak dalda ise yalnızca yazdırmayı sağlayan yapıya bağlı bir kullanım olup yazma eyleminin yerini almaz.","focus_only":"Odak dalın çekirdeği yazıyı fiilen oluşturma ve ortaya çıkan yazılı üründür.","gloss":"söyleyerek yazdırma","neighbor_only":"Komşu dalın çekirdeği, yazılacak sözleri yazara söyleme işlemidir.","neighbor_ref":"root_001447/B003","relation_type":"near_neighbor","shared_zone":"İki dal, bir metnin sözlü aktarım yoluyla yazıya geçirilmesi sürecinde kesişir."}],"source_phrase_ar":"الكتاب والكتابة يقال كتبت الكتاب أكتبه كتبا (maqayis)؛ وقد كتب الكتاب يكتبه كتبا إذا جمع حروفه (jamhara)؛ الكتاب معروف وقد كتبت كتبا وكتابا وكتابة (sihah)؛ كتبت الكتاب كتبا وكتابا فالكتاب اسم لما كتب مجموعا (tahdhib)؛ في التعارف ضم الحروف بعضها إلى بعض بالخط (mufradat)؛ أكتبني هذه القصيدة أي أملها علي (sihah)؛ استكتبه الشيء أي سأله أن يكتبه له (sihah;tahdhib)","source_summary":"Kaynaklar yazmayı harfleri çizgiyle bir araya getiren işlem olarak sunar; yazılı ürün, kopyalama, dikte ettirme, yazma isteği ve öğretimle ilgili kullanımlar bu merkeze bağlanır.","sources":["MQ","AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه كتب الكتاب وكتابته ونسخه، والكتاب اسما للمكتوب أو الصحيفة ذات الكتابة، والتعليم والإملاء والاستكتاب المتعلق بالكتابة.","what_is_not_ar":"ليس المراد هنا الفرض والحكم والقدر إلا إذا صارت الكتابة كناية عن الإيجاب أو الإثبات، ولا يدخل فيه سهم الصبيان الصغير."},"support_links":["sup_1d442c9e1534d169a72d"]},{"boundary":"Salt yazı yazmak bu dala girmez; belirleme işleminin yükümlülük, hüküm veya yazgı sonucu doğurması gerekir.","branch_kind":"mixed_non_bare","branch_ref":"root_001283/B003","candidate_links":[{"candidate_id":"cand_1d1bf4fd781425b8e42c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"98:3:2:1","qac_word_ref":"98:3:2","surface_ar":"كُتُبٌ"}],"gloss":"bağlayıcı olarak hükme bağlama ve belirleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir işi yapılması gereken bağlayıcı bir yükümlülük olarak belirlemek temel değerlerden biridir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir konuda geçerli ve kesinleşmiş hüküm vermek aynı belirleme çekirdeğinin yargısal yönüdür."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir olayın payını, ölçüsünü veya gelecekte gerçekleşecek sonucunu önceden belirlemek yazgı yönünü oluşturur."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Yazma anlatımı, belirlenen hükmün saptanmış, yürürlüğe konmuş ve kesinleşmiş olmasını ifade eder."}}],"root_ar":"ك ت ب","root_id":"root_001283","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yükümlülük, hüküm ve yazgı yönlerini tek bir kesin ve geçerli belirleme çekirdeğinde toplar.","boundary_detail":"Salt yazı yazmak bu dala girmez; belirleme işleminin yükümlülük, hüküm veya yazgı sonucu doğurması gerekir.","branch_image_ar":"إثبات يوجب حكما أو قدرا","concept_gloss":"bağlayıcı olarak hükme bağlama ve belirleme","contextual_glosses":[{"applicability":"Bir eylemin kişilere bağlayıcı yükümlülük olarak yüklendiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yapılması gereken işi bağlayıcı yükümlülük hâline getirme anlamını korur."},"facet_ids":["F001","F004"],"text":"zorunlu kılmak","usage_role":"contextual"},{"applicability":"Bir olayın gerçekleşmesini veya kişiye düşecek payı önceden belirleme bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gelecekteki olay veya payın önceden karara bağlanması anlamını korur."},"facet_ids":["F003","F004"],"text":"yazgı olarak belirlemek","usage_role":"contextual"}],"definition":"Bir şeyi bağlayıcı bir yükümlülük, hüküm veya gerçekleşmesi belirlenmiş pay ve yazgı olarak karara bağlamaktır. Yazma çağrışımı burada harf çizmekten çok kararın kesinleştirilip geçerli kılınmasını anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir işi yapılması gereken bağlayıcı bir yükümlülük olarak belirlemek temel değerlerden biridir."},{"facet_id":"F002","role":"core","statement":"Bir konuda geçerli ve kesinleşmiş hüküm vermek aynı belirleme çekirdeğinin yargısal yönüdür."},{"facet_id":"F003","role":"core","statement":"Bir olayın payını, ölçüsünü veya gelecekte gerçekleşecek sonucunu önceden belirlemek yazgı yönünü oluşturur."},{"facet_id":"F004","role":"associated_use","statement":"Yazma anlatımı, belirlenen hükmün saptanmış, yürürlüğe konmuş ve kesinleşmiş olmasını ifade eder."}],"identity_rationale":"Kaynak ifadesi, bir şeyi yükümlülük, hüküm, paylaştırılmış yazgı veya kesinleşmiş karar olarak belirleme alanını açıkça toplar; burada yazı, harf çizme eylemi değil bağlayıcı biçimde belirlemenin anlatım yoludur.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yükümlülük, hüküm veya yazgı"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"size zorunlu kılındı"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"Tanrı belirledi, karara bağladı veya zorunlu kıldı"}],"lexicalization_note":"Yükümlülük, hüküm ve yazgı değerleri birlikte korunur; birine zorunluluk yükleme ve Tanrı'nın belirlemesi anlamları yalnızca tanıklanmış yapılara bağlanır.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; seçilenler zorunluluk, kesin hüküm ve karar verme sınırlarındaki gerçek örtüşmeleri gösterir, diğerleri yalnızca kanıt, izin veya konu ortaklığı düzeyinde kalır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal kaçınılmaz kesin hükmü merkez alır; odak dal ise aynı ekseni yükümlülük ve yazgı belirleme yönlerine de açar.","focus_only":"Odak dal, zorunluluk ve kesin hükmün yanında pay veya yazgıyı önceden belirlemeyi de kapsar.","gloss":"kesin hükme bağlama","neighbor_only":"Komşu dal, kararın kaçınılmazlığına, sıkıca kesinleştirilmesine ve kişiye yüklenmesine özellikle yoğunlaşır.","neighbor_ref":"root_000292/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir kararın kesin, geçerli ve bağlayıcı hâle getirilmesi alanında güçlü biçimde örtüşür."},{"boundary_match":"partial","distinction":"Yükümlülük bağlamında yaklaşırlar; ancak odak dalın hüküm ve yazgı kapsamı komşuda yoktur, komşunun ödev ve hak odağı da daha dardır.","focus_only":"Odak dal, yükümlülüğe ek olarak hüküm ve önceden belirlenmiş yazgı anlamlarını taşır.","gloss":"zorunlu yükümlülük","neighbor_only":"Komşu dal, özellikle yerine getirilmesi gereken ödev ve vazgeçilmez hak türlerini öne çıkarır.","neighbor_ref":"root_001010/B005","relation_type":"near_synonym","shared_zone":"Her iki dal yapılması gereken işi bağlayıcı bir yükümlülük olarak gösterir."},{"boundary_match":"partial","distinction":"Komşu dal yargılama ve uyuşmazlığı ayırma eylemine dayanır; odak dalda ise bağlayıcı belirleme daha geniş olup bir uyuşmazlık gerektirmez.","focus_only":"Odak dal, hükmün yanında yükümlülük koyma ve olayları önceden belirleme yönlerini içerir.","gloss":"kesin karar verme","neighbor_only":"Komşu dal, taraflar arasında karar verme ve uyuşmazlığı kesin biçimde sonuçlandırma işlemini kapsar.","neighbor_ref":"root_001237/B001","relation_type":"near_neighbor","shared_zone":"İki dal, bir meseleyi geçerli ve kesin bir kararla sonuçlandırma alanında buluşur."}],"source_phrase_ar":"الكتاب وهو الفرض (maqayis)؛ يقال للحكم الكتاب (maqayis)؛ يقال للقدر الكتاب (maqayis)؛ الكتاب الفرض والحكم والقدر (sihah)؛ الكتاب يوضع موضع الفرض (tahdhib)؛ يعبر عن الإثبات والتقدير والإيجاب والفرض والعزم بالكتابة (mufradat)؛ يعبر بالكتابة عن القضاء الممضى (mufradat)","source_summary":"Kaynaklar yükümlülük, hüküm, yazgı, belirleme ve kesinleşmiş karar değerlerini aynı bağlayıcı saptama alanında birleştirir; yazma sözü bu saptamanın anlatım aracıdır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الكتاب بمعنى الفرض والحكم والقدر، والكتابة بمعنى الإثبات والتقدير والإيجاب والعزم والقضاء الممضى.","what_is_not_ar":"لا يدخل فيه مجرد خط الحروف إلا إذا كان المعنى المنقول هو الإيجاب أو الحكم أو التقدير."},"support_links":["sup_6571f8bb4a6b2bb05ae0"]},{"boundary":"Dal, genel yazma eylemini değil, adı kayda geçirerek kişiyi bir listeye veya belirli topluluğa dâhil etmeyi anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_001283/B004","candidate_links":[{"candidate_id":"cand_e8ed5e9a123495502918","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"98:3:2:1","qac_word_ref":"98:3:2","surface_ar":"كُتُبٌ"}],"gloss":"adını sicile yazma veya bir gruba dâhil etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişinin adını bir kayıt veya listeye geçirerek ona kayıtlı kişi konumu vermek dalın çekirdeğidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adı pay, geçim tahsisatı veya yönetim siciline yazdırmak resmî kayıt alanındaki özel gerçekleşmedir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kişiyi tanıklar gibi belirli bir topluluğun içinde saymak, sicile almadan üyelik vermeye uzanan kullanımdır."}}],"root_ar":"ك ت ب","root_id":"root_001283","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem resmî sicile alma hem de kişiyi belirli bir topluluğun üyesi sayma anlamlarını kapsar.","boundary_detail":"Dal, genel yazma eylemini değil, adı kayda geçirerek kişiyi bir listeye veya belirli topluluğa dâhil etmeyi anlatır.","branch_image_ar":"إدخال الاسم في سجل أو زمرة","concept_gloss":"adını sicile yazma veya bir gruba dâhil etme","contextual_glosses":[{"applicability":"Kişinin pay, geçim tahsisatı veya yönetim kaydına kendi adını geçirdiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin adını resmî kayda geçirerek kayıtlı konum kazanması anlamını korur."},"facet_ids":["F001","F002"],"text":"adını sicile yazdırmak","usage_role":"contextual"},{"applicability":"Bir kişinin tanıklar gibi adı belirli bir topluluğun üyesi sayıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye belirli topluluk içinde üyelik ve yer verilmesi anlamını korur."},"facet_ids":["F003"],"text":"aralarına katmak","usage_role":"contextual"}],"definition":"Bir kişinin adını resmî bir pay, geçim veya yönetim kaydına geçirerek onu kayıtlılar arasına almak ya da kişiyi belirli bir topluluğun üyesi saymaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişinin adını bir kayıt veya listeye geçirerek ona kayıtlı kişi konumu vermek dalın çekirdeğidir."},{"facet_id":"F002","role":"specialization","statement":"Adı pay, geçim tahsisatı veya yönetim siciline yazdırmak resmî kayıt alanındaki özel gerçekleşmedir."},{"facet_id":"F003","role":"extension","statement":"Bir kişiyi tanıklar gibi belirli bir topluluğun içinde saymak, sicile almadan üyelik vermeye uzanan kullanımdır."}],"identity_rationale":"Kaynak ifadesi, bir kişinin adını pay veya geçim kaydına ya da yönetim siciline geçirmek ile kişiyi tanıklar topluluğuna dâhil etmek arasında ortak bir kayıt ve üyelik çekirdeği kurar.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"pay veya geçim tahsisatı için kaydolma"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"adını pay kaydına veya yönetim siciline yazdırmak"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bizi tanıklar topluluğuna kat"}],"lexicalization_note":"Sicile alma ve topluluğa katma çekirdeği korunur; pay kaydı, yönetim sicili ve tanıklar arasına katılma anlamları kendi tanıklanmış yapılarıyla sınırlıdır.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; yayımlanan karşılaştırmalar kayıtla üyelik ile genel katma ve özel aidiyet arasındaki sınırı gösterir, kalan adaylar yalnızca grup veya yazı alanını uzaktan paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın ayırıcı özelliği adın kayda geçirilmesi veya üyelik verilmesidir; komşu dalda kayıt koşulu bulunmaz ve birleştirme kendi başına çekirdektir.","focus_only":"Odak dalda kişinin adı kayda geçirilir ve bunun sonucunda ona resmî veya toplumsal üyelik verilir.","gloss":"bir topluluğa katma","neighbor_only":"Komşu dal, ad kaydı olmadan nesneleri fiziksel olarak veya insanları düzenli topluluk olarak birleştirir.","neighbor_ref":"root_001283/B001","relation_type":"near_neighbor","shared_zone":"İki dal, ayrı bir kişiyi veya unsuru daha büyük bir bütünün içine katma düşüncesinde buluşur."},{"boundary_match":"field_only","distinction":"Odak dal katılma ve kayıt işlemini, komşu dal ise başkalarına kapalı özel aidiyet ve ayrışma durumunu merkez alır.","focus_only":"Odak dal, kişiyi adını kaydederek bir sicile veya topluluğa dâhil etme işlemini anlatır.","gloss":"gruba ait kılma","neighbor_only":"Komşu dal, bir şeyin belirli kişi veya topluluğa özel olmasını ve başkalarından ayrılmasını anlatır.","neighbor_ref":"root_000430/B004","relation_type":"same_field","shared_zone":"Her iki dal kişi veya şeyin belirli bir toplulukla ilişkili konum kazanması alanındadır."}],"source_phrase_ar":"الكتبة الاكتتاب في الفرض والرزق (ayn;tahdhib)؛ اكتتب فلان أي كتب اسمه في الفرض (ayn;tahdhib)؛ اكتتب الرجل إذا كتب نفسه في ديوان السلطان (sihah)؛ فاكتبنا مع الشاهدين أي اجعلنا في زمرتهم (mufradat)","source_summary":"Kaynakların ortak içeriği, adı kayda geçirmenin kişiyi pay alanlar, yönetim sicilindekiler veya belirli bir topluluğun üyeleri arasına sokmasıdır.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الاكتتاب في الفرض والرزق، وكتابة الاسم في ديوان السلطان، ومعنى اجعلنا في زمرة الشاهدين.","what_is_not_ar":"ليس هو مجرد تأليف كتاب، ولا حكم الفرض نفسه، بل إدخال اسم أو شخص في سجل أو جماعة."},"support_links":["sup_ffc9f173b9a085642696"]},{"boundary":"Dal, her türlü yazılı sözleşmeyi değil, bedelin ödenmesiyle özgürlüğe götüren bu özel sözleşme türünü kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_001283/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"98:3:2:1","qac_word_ref":"98:3:2","surface_ar":"كُتُبٌ"}],"gloss":"özgürlük bedelini ödemeye dayalı özgürleşme sözleşmesi","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sahip ile köleleştirilmiş kişi arasında, kişinin kendi özgürlük bedelini ödemesini konu alan özel bir sözleşme kurulur."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bedel belirlenmiş ödeme dilimlerine bağlanır ve köleleştirilmiş kişi bunu kendi kazancından karşılar."}},{"facet_id":"F003","role":"core","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kararlaştırılan bedelin tamamlanması sözleşmenin sonucu olarak köleleştirilmiş kişinin özgür olmasını sağlar."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"İlgili biçimler sözleşmenin kendisini, sözleşmeye bağlı köleleştirilmiş kişiyi ve bağlama göre sözleşmenin öteki tarafını gösterebilir."}}],"root_ar":"ك ت ب","root_id":"root_001283","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözleşmenin taraflarını, ödeme düzenini ve bedelin tamamlanmasıyla doğan özgürleşme sonucunu birlikte kapsar.","boundary_detail":"Dal, her türlü yazılı sözleşmeyi değil, bedelin ödenmesiyle özgürlüğe götüren bu özel sözleşme türünü kapsar.","branch_image_ar":"مكاتبة العبد على عتقه","concept_gloss":"özgürlük bedelini ödemeye dayalı özgürleşme sözleşmesi","contextual_glosses":[{"applicability":"Köleleştirilmiş kişinin kendi bedelini aşamalı ödeyerek özgürleşmesini açıklayan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin bedeli ödemesi, ödemelerin aşamalı oluşu ve özgürleşme sonucunu korur."},"facet_ids":["F001","F002","F003"],"text":"özgürlüğünü taksitle satın alma sözleşmesi","usage_role":"explanatory"},{"applicability":"Sahibin köleleştirilmiş kişiyle bu özel ödeme ve özgürleşme sözleşmesini kurduğu bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tarafların özgürlük bedelini konu alan özel sözleşmeyi kurması anlamını korur."},"facet_ids":["F001","F004"],"text":"özgürlük bedeli sözleşmesi yapmak","usage_role":"contextual"}],"definition":"Köleleştirilmiş kişinin, belirlenen bedeli kazancından ve kararlaştırılmış ödemelerle sahibine vererek özgürlüğünü kazanması için taraflar arasında yapılan özel sözleşmedir. Bedel tamamlandığında kişi özgür olur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sahip ile köleleştirilmiş kişi arasında, kişinin kendi özgürlük bedelini ödemesini konu alan özel bir sözleşme kurulur."},{"facet_id":"F002","role":"core","statement":"Bedel belirlenmiş ödeme dilimlerine bağlanır ve köleleştirilmiş kişi bunu kendi kazancından karşılar."},{"facet_id":"F003","role":"core","statement":"Kararlaştırılan bedelin tamamlanması sözleşmenin sonucu olarak köleleştirilmiş kişinin özgür olmasını sağlar."},{"facet_id":"F004","role":"associated_use","statement":"İlgili biçimler sözleşmenin kendisini, sözleşmeye bağlı köleleştirilmiş kişiyi ve bağlama göre sözleşmenin öteki tarafını gösterebilir."}],"identity_rationale":"Kaynak ifadesi, köleleştirilmiş kişinin kendi özgürlük bedelini kazancından ve belirlenmiş ödemelerle karşılaması için sahibiyle yaptığı özel sözleşmeyi, taraflarını ve özgürleşme sonucunu açıkça tanımlar.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"kölenin bedelini ödeyerek özgürlüğünü kazanma sözleşmesi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"özgürlük bedeli sözleşmesinin tarafı olan köle; bağlama göre sahibi"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"köleyle özgürlük bedeli ödemesine dayalı sözleşme yapmak"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"kölenin özgürlüğünü satın almak için yaptığı sözleşme"}],"lexicalization_note":"Tanım özel sözleşme türüne bağlı kalır; sözleşmenin adı, tarafı ve sözleşme yapma eylemi ayrı tanıklanmış biçimler olarak korunur ve genel sözleşme anlamına genişletilmez.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; seçilenler sözleşme, bedeli kazanma, özgürleşme sonucu ve ölüm sonrası özgür bırakma arasındaki temel sınırları gösterir, kalanlar yalnızca aynı hukuk alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hukuki ilişkiyi ve ödeme yükümlülüğünü kurar; komşu dal ise bu yükümlülüğü yerine getirmek için gösterilen çalışma ve kazanç sürecidir.","focus_only":"Odak dal, ödeme koşullarını ve özgürleşme sonucunu kuran sözleşmenin kendisini tanımlar.","gloss":"özgürlük bedelini kazanma","neighbor_only":"Komşu dal, köleleştirilmiş kişinin bedeli kazanmak için çalışmasını ve kalan payı tamamlama çabasını tanımlar.","neighbor_ref":"root_000709/B005","relation_type":"near_neighbor","shared_zone":"İki dal aynı özgürlük bedelinin ödenmesi ve kölelikten çıkma sürecinde yer alır."},{"boundary_match":"partial","distinction":"Özgürlük komşu dalın doğrudan çekirdeğidir; odak dalda ise özel bir sözleşme ve bedelin ödenmesiyle ulaşılan sonuçtur.","focus_only":"Odak dal, özgürlüğün ancak kararlaştırılan bedelin sözleşmeye göre ödenmesiyle kazanılmasını içerir.","gloss":"özgürleşme","neighbor_only":"Komşu dal, sözleşme veya bedel koşulu aramadan özgür olma ve kölelikten çıkarılma durumunu kapsar.","neighbor_ref":"root_000306/B002","relation_type":"near_neighbor","shared_zone":"İki dal kölelik durumunun sona ermesi ve kişinin özgürlüğe kavuşması sonucunda buluşur."},{"boundary_match":"field_only","distinction":"Odak dalın koşulu bedelin sözleşmeye göre ödenmesidir; komşu dalın koşulu ise sahibin ölümü olup ödeme sözleşmesi bulunmaz.","focus_only":"Odak dalda özgürleşme, kişinin kazancından yaptığı kararlaştırılmış ödemeleri tamamlamasına bağlıdır.","gloss":"koşula bağlı özgürleşme","neighbor_only":"Komşu dalda özgürleşme, sahibin ölümünden sonra gerçekleşmek üzere önceden verilmiş karara bağlıdır.","neighbor_ref":"root_000458/B007","relation_type":"same_field","shared_zone":"Her iki dal özgürlüğün gelecekteki bir koşul gerçekleşince doğmasını düzenler."}],"source_phrase_ar":"المكاتب العبد يكاتبه سيده على نفسه (maqayis)؛ المكاتب الذي يشتري نفسه ويكاتب عليها (jamhara)؛ المكاتب العبد يكاتب على نفسه بثمنه فإذا سعى وأداه عتق (sihah)؛ معنى الكتاب والمكاتبة أن يكاتب الرجل عبده أو أمته على مال ينجمه عليه (tahdhib)؛ كتابة العبد ابتياع نفسه من سيده بما يؤديه من كسبه (mufradat)","source_summary":"Kaynaklar, özgürlük bedelinin kararlaştırılıp ödemelere bölündüğü, köleleştirilmiş kişinin bunu kazancıyla ödediği ve tamamlandığında özgürleştiği özel sözleşmede birleşir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه عقد المكاتبة بين السيد والعبد أو الأمة على مال منجم، وكتابة الشرط والنجوم المؤدية إلى العتق.","what_is_not_ar":"لا يدخل فيه مطلق الكتابة ولا كل عقد مكتوب، بل هذا الباب الفقهي الخاص بالمكاتب والمكاتبة."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["98:3:1"],"branch_refs":[],"candidate_id":"cand_3ab254813c203bc35b45","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"98:3:1:boundary-to-nominal-content","source_type":"word_analysis","support_ids":["sup_c311da74abff27e0afc9","sup_ff064653479236f5533e"],"title":"boundary shifts from recitation to standing contents","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:1","qac_refs":["98:3:1:1","98:3:1:2"],"status":"accepted"}},{"anchor_refs":["98:3:1"],"branch_refs":[],"candidate_id":"cand_7503b22887f7196c80ba","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"98:3:1:feminine-suffix-antecedent","source_type":"word_analysis","support_ids":["sup_a381b48db9f7c4908bb1","sup_c311da74abff27e0afc9"],"title":"feminine suffix keeps two antecedents live","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:1","qac_refs":["98:3:1:1","98:3:1:2"],"status":"accepted"}},{"anchor_refs":["98:3:1"],"branch_refs":[],"candidate_id":"cand_24e556e87acfb65e8502","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"98:3:1:fronted-container-staging","source_type":"word_analysis","support_ids":["sup_8bc0fb17c52afa03818b","sup_c311da74abff27e0afc9"],"title":"fronting makes the container given and contents new","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:1","qac_refs":["98:3:1:1","98:3:1:2"],"status":"accepted"}},{"anchor_refs":["98:3:1"],"branch_refs":[],"candidate_id":"cand_246e4023324dd2dc9e98","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"98:3:1:locative-container-predicate","source_type":"word_analysis","support_ids":["sup_8558b715415dc29b236f","sup_c311da74abff27e0afc9"],"title":"locative predicate makes containment explicit","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:1","qac_refs":["98:3:1:1","98:3:1:2"],"status":"accepted"}},{"anchor_refs":["98:3:2"],"branch_refs":[],"candidate_id":"cand_8803af2fb2461f2f37fb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001283"],"scope":"focus_ayah","source_local_id":"98:3:2:delayed-indefinite-subject","source_type":"word_analysis","support_ids":["sup_971b43378e7603f5a832","sup_f2281f5b03b1c784219c"],"title":"delayed indefinite subject foregrounds qualitative writings","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:2","qac_refs":["98:3:2:1"],"status":"accepted"}},{"anchor_refs":["98:3:2"],"branch_refs":[],"candidate_id":"cand_8473336878e90cfa14bf","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001283"],"scope":"focus_ayah","source_local_id":"98:3:2:dominant-written-register","source_type":"word_analysis","support_ids":["sup_8a3a84a632bf6c35d874","sup_971b43378e7603f5a832"],"title":"noun distribution keeps the written-document register normal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:2","qac_refs":["98:3:2:1"],"status":"accepted"}},{"anchor_refs":["98:3:2"],"branch_refs":[],"candidate_id":"cand_605da7d9022837dce48e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001283"],"scope":"focus_ayah","source_local_id":"98:3:2:nominal-disclosure-and-boundary","source_type":"word_analysis","support_ids":["sup_971b43378e7603f5a832","sup_f6c1cf04bdcaed92eff3"],"title":"nominal placement makes writings a standing fact","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:2","qac_refs":["98:3:2:1"],"status":"accepted"}},{"anchor_refs":["98:3:2"],"branch_refs":[],"candidate_id":"cand_3f72c0a3e99122ba24fc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001283"],"scope":"focus_ayah","source_local_id":"98:3:2:noun-adjective-cadence","source_type":"word_analysis","support_ids":["sup_7b75eca1a07467f1b02d","sup_971b43378e7603f5a832"],"title":"paired tanwīn binds noun and adjective","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:2","qac_refs":["98:3:2:1"],"status":"accepted"}},{"anchor_refs":["98:3:2"],"branch_refs":[],"candidate_id":"cand_0b03b7d2cb4a7d2876d5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001283"],"scope":"focus_ayah","source_local_id":"98:3:2:plural-distributed-contents","source_type":"word_analysis","support_ids":["sup_1b085e9037707e0c6f9f","sup_971b43378e7603f5a832"],"title":"indefinite plural distributes the contents","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:2","qac_refs":["98:3:2:1"],"status":"accepted"}},{"anchor_refs":["98:3:2"],"branch_refs":[],"candidate_id":"cand_ec85db490850b3765b38","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001283"],"scope":"focus_ayah","source_local_id":"98:3:2:same-surah-book-thread","source_type":"word_analysis","support_ids":["sup_971b43378e7603f5a832","sup_ec56d1d863b1230cff33"],"title":"the plural answers the surah's book thread","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:2","qac_refs":["98:3:2:1"],"status":"accepted"}},{"anchor_refs":["98:3:2"],"branch_refs":[],"candidate_id":"cand_56dfefa7b78232f5bc23","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001283"],"scope":"focus_ayah","source_local_id":"98:3:2:textual-upright-root-pair","source_type":"word_analysis","support_ids":["sup_0618efc09ba666ea04e1","sup_971b43378e7603f5a832"],"title":"book-root and upright-root define each other","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:2","qac_refs":["98:3:2:1"],"status":"accepted"}},{"anchor_refs":["98:3:2"],"branch_refs":[],"candidate_id":"cand_12f9a6b0d10570f500f7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001283"],"scope":"focus_ayah","source_local_id":"98:3:2:written-prescriptive-records","source_type":"word_analysis","support_ids":["sup_971b43378e7603f5a832","sup_b4485af21def91f8fdb5"],"title":"writing, joining, and prescribing converge in written records","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:2","qac_refs":["98:3:2:1"],"status":"accepted"}},{"anchor_refs":["98:3:3"],"branch_refs":[],"candidate_id":"cand_3e125bb730273be13d21","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001273"],"scope":"focus_ayah","source_local_id":"98:3:3:adjective-agreement-to-kutub","source_type":"word_analysis","support_ids":["sup_1c53f3c89ff110bfed2f","sup_f3674a904b3ccdcb225d"],"title":"feminine singular adjective binds to the broken plural","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:3","qac_refs":["98:3:3:1"],"status":"accepted"}},{"anchor_refs":["98:3:3"],"branch_refs":[],"candidate_id":"cand_721f0b782d2c6d9c1b86","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001273"],"scope":"focus_ayah","source_local_id":"98:3:3:ayah-final-quality-closure","source_type":"word_analysis","support_ids":["sup_1c53f3c89ff110bfed2f","sup_358da71a9c2b8ccc25fb"],"title":"final adjective seals the ayah with quality","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:3","qac_refs":["98:3:3:1"],"status":"accepted"}},{"anchor_refs":["98:3:3"],"branch_refs":[],"candidate_id":"cand_9b51930638f666643be1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001273"],"scope":"focus_ayah","source_local_id":"98:3:3:constrained-upright-form-field","source_type":"word_analysis","support_ids":["sup_1c53f3c89ff110bfed2f","sup_244b2344e7a0157aad41"],"title":"qualitative q-w-m field is specialized","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:3","qac_refs":["98:3:3:1"],"status":"accepted"}},{"anchor_refs":["98:3:3"],"branch_refs":[],"candidate_id":"cand_1212cfe7f50d9ce9ab46","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001273"],"scope":"focus_ayah","source_local_id":"98:3:3:intensive-doubled-form","source_type":"word_analysis","support_ids":["sup_1c53f3c89ff110bfed2f","sup_8ae04805157e7c5519eb"],"title":"doubled form intensifies inherent correctness","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:3","qac_refs":["98:3:3:1"],"status":"accepted"}},{"anchor_refs":["98:3:3"],"branch_refs":[],"candidate_id":"cand_40ef74c86aecdb271fd7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001273"],"scope":"focus_ayah","source_local_id":"98:3:3:same-surah-text-to-practice","source_type":"word_analysis","support_ids":["sup_1c53f3c89ff110bfed2f","sup_eb05edb306f80409fd1b"],"title":"upright writings anticipate upright practice","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:3","qac_refs":["98:3:3:1"],"status":"accepted"}},{"anchor_refs":["98:3:3"],"branch_refs":[],"candidate_id":"cand_722ef4922d3eff485a2b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001273"],"scope":"focus_ayah","source_local_id":"98:3:3:textual-uprightness-pairing","source_type":"word_analysis","support_ids":["sup_1c53f3c89ff110bfed2f","sup_9e2aec062f6d2736d40e"],"title":"uprightness is attached to written contents","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:3","qac_refs":["98:3:3:1"],"status":"accepted"}},{"anchor_refs":["98:3:3"],"branch_refs":[],"candidate_id":"cand_b5636ab0f68fd4dd9df8","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001273"],"scope":"focus_ayah","source_local_id":"98:3:3:upright-corrective-value","source_type":"word_analysis","support_ids":["sup_1b2ad07b3a267ce91069","sup_1c53f3c89ff110bfed2f"],"title":"uprightness, correction, subsistence, and value converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:3","qac_refs":["98:3:3:1"],"status":"accepted"}},{"anchor_refs":["98:3:3"],"branch_refs":[],"candidate_id":"cand_46a86f6d5321096cfb66","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001273"],"scope":"focus_ayah","source_local_id":"98:3:3:verbless-quality-assertion","source_type":"word_analysis","support_ids":["sup_0815d6406f85cd238ea6","sup_1c53f3c89ff110bfed2f"],"title":"verbless adjective makes uprightness a standing assertion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"98:3:3","qac_refs":["98:3:3:1"],"status":"accepted"}},{"anchor_refs":["98:3:2"],"branch_refs":[],"candidate_id":"cand_a28dd40ada04b6e01736","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001283"],"scope":"focus_ayah","source_local_id":"98:3:2:1","source_type":"qac_morpheme","support_ids":["sup_610e88189aa193e91c3f"],"title":"QAC root occurrence: ك ت ب","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["98:3:3"],"branch_refs":[],"candidate_id":"cand_7b73f7f0181106dafe72","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001273"],"scope":"focus_ayah","source_local_id":"98:3:3:1","source_type":"qac_morpheme","support_ids":["sup_064409a4134715425088"],"title":"QAC root occurrence: ق و م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["98:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"98:3","branch_refs":["root_001273/B008","root_001283/B001","root_001283/B002"],"candidate_id":"cand_3c16643c7f1912f72400","commentary_obligation":"review","hft_ref":"hft_4ae5c7e508dde9e76266","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_integrated_upright_units","source_type":"hft","support_ids":["sup_1d442c9e1534d169a72d"],"title":"baseline_integrated_upright_units","trust":"legacy_unbound"},{"anchor_refs":["98:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"98:3","branch_refs":["root_001273/B004","root_001273/B009","root_001283/B003"],"candidate_id":"cand_1d1bf4fd781425b8e42c","commentary_obligation":"review","hft_ref":"hft_3eb945601ccc5772db89","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_binding_sustaining_order","source_type":"hft","support_ids":["sup_6571f8bb4a6b2bb05ae0"],"title":"baseline_binding_sustaining_order","trust":"legacy_unbound"},{"anchor_refs":["98:3"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"98:3","branch_refs":["root_001273/B010","root_001273/B015","root_001283/B004"],"candidate_id":"cand_e8ed5e9a123495502918","commentary_obligation":"review","hft_ref":"hft_67f214dcd84fdea2b6aa","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_appraised_register","source_type":"hft","support_ids":["sup_ffc9f173b9a085642696"],"title":"baseline_appraised_register","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فِيهَا كُتُبٌۭ قَيِّمَةٌۭ","qac_morphemes":[{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"98:3:1:1","qac_word_ref":"98:3:1","root_ar":"","surface_ar":"فِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"98:3:1:2","qac_word_ref":"98:3:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"98:3:2:1","qac_word_ref":"98:3:2","root_ar":"ك ت ب","surface_ar":"كُتُبٌ"},{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","root_ar":"ق و م","surface_ar":"قَيِّمَةٌ"}],"word_analysis_qac_refs":[["98:3:1:1","98:3:1:2"],["98:3:2:1"],["98:3:3:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["98:3:1","98:3:2","98:3:3"]},"focus_surface_evidence":{"arabic_uthmani":"فِيهَا كُتُبٌۭ قَيِّمَةٌۭ","qac_morphemes":[{"lemma_ar":"فِى","morph_features":"STEM|POS:P|LEM:fiY","morpheme_role":"STEM","pos":"P","qac_ref":"98:3:1:1","qac_word_ref":"98:3:1","root_ar":"","surface_ar":"فِي"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3FS","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"98:3:1:2","qac_word_ref":"98:3:1","root_ar":"","surface_ar":"هَا"},{"lemma_ar":"كِتَٰب","morph_features":"STEM|POS:N|LEM:kita`b|ROOT:ktb|MP|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"98:3:2:1","qac_word_ref":"98:3:2","root_ar":"ك ت ب","surface_ar":"كُتُبٌ"},{"lemma_ar":"قَيِّمَة","morph_features":"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM","morpheme_role":"STEM","pos":"ADJ","qac_ref":"98:3:3:1","qac_word_ref":"98:3:3","root_ar":"ق و م","surface_ar":"قَيِّمَةٌ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["98:3:1:1","98:3:1:2"],["98:3:2:1"],["98:3:3:1"]],"word_analysis_refs":["98:3:1","98:3:2","98:3:3"],"word_rows":[{"analysis_record_ref":"98:3:1","analytic_gloss_range_en":"fronted locative preposition plus feminine singular suffix, with the antecedent deliberately kept open between the clear proof and the purified pages","analytic_root_gloss_range_en":null,"qac_refs":["98:3:1:1","98:3:1:2"],"root":{},"surface":{"arabic":"فِيهَا","transliteration":"fīhā"}},{"analysis_record_ref":"98:3:2","analytic_gloss_range_en":"indefinite plural written contents or scriptures as the delayed nominative subject inside the locative frame","analytic_root_gloss_range_en":"joining, writing, copying, decreeing, prescribing, registering, and contracting are available root branches; the local plural noun selects written contents with ordered and prescriptive force","qac_refs":["98:3:2:1"],"root":{"arabic":"ك ت ب","transliteration":"k-t-b"},"surface":{"arabic":"كُتُبٌ","transliteration":"kutubun"}},{"analysis_record_ref":"98:3:3","analytic_gloss_range_en":"feminine singular qualitative adjective modifying the broken plural writings: upright, sound, corrective, valuable, and self-standing in local force","analytic_root_gloss_range_en":"the root ranges across people, standing, undertaking, guardianship, establishing, straightness, support, value, and other branches; the local adjective selects uprightness, correctness, establishment, and worth, not people or resurrection branches","qac_refs":["98:3:3:1"],"root":{"arabic":"ق و م","transliteration":"q-w-m"},"surface":{"arabic":"قَيِّمَةٌ","transliteration":"qayyimatun"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["98:3"],"branch_refs":["root_001273/B008","root_001283/B001","root_001283/B002"],"candidate_id":"cand_3c16643c7f1912f72400","evidence_scope":"focus_ayah","hft_ref":"hft_4ae5c7e508dde9e76266","item_id":"baseline_integrated_upright_units","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_integrated_upright_units","support_id":"sup_1d442c9e1534d169a72d"},{"anchor_refs":["98:3"],"branch_refs":["root_001273/B004","root_001273/B009","root_001283/B003"],"candidate_id":"cand_1d1bf4fd781425b8e42c","evidence_scope":"focus_ayah","hft_ref":"hft_3eb945601ccc5772db89","item_id":"baseline_binding_sustaining_order","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_binding_sustaining_order","support_id":"sup_6571f8bb4a6b2bb05ae0"},{"anchor_refs":["98:3"],"branch_refs":["root_001273/B010","root_001273/B015","root_001283/B004"],"candidate_id":"cand_e8ed5e9a123495502918","evidence_scope":"focus_ayah","hft_ref":"hft_67f214dcd84fdea2b6aa","item_id":"baseline_appraised_register","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_appraised_register","support_id":"sup_ffc9f173b9a085642696"}],"diagnostics":[],"lane_counts":{"global":8,"macro":9,"micro":3},"packet_summary":{"ayah_count":8,"focus_ref":"98:3","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ت ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000186","furuq_root_norm":"ت ل و","furuq_source_root_norm":"ت ل و","is_dominant":true,"target_occurrences":39,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000185","furuq_root_norm":"ت ل ل","furuq_source_root_norm":"ت ل ل","is_dominant":false,"target_occurrences":4,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ش ر ر","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000787","furuq_root_norm":"ش ر ر","furuq_source_root_norm":"ش ر ر","is_dominant":true,"target_occurrences":19,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000792","furuq_root_norm":"ش ر ي","furuq_source_root_norm":"ش ر ي","is_dominant":false,"target_occurrences":11,"target_rank":2}]},{"qac_root":"ج ز ي","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000244","furuq_root_norm":"ج ز ي","furuq_source_root_norm":"ج ز ي","is_dominant":true,"target_occurrences":97,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000242","furuq_root_norm":"ج ز ز","furuq_source_root_norm":"ج ز ز","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ب ب","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000532","furuq_root_norm":"ر ب ب","furuq_source_root_norm":"ر ب ب","is_dominant":true,"target_occurrences":970,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000537","furuq_root_norm":"ر ب و","furuq_source_root_norm":"ر ب و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ض و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000569","furuq_root_norm":"ر ض و","furuq_source_root_norm":"ر ض و","is_dominant":true,"target_occurrences":29,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000570","furuq_root_norm":"ر ض ي","furuq_source_root_norm":"ر ض ي","is_dominant":false,"target_occurrences":28,"target_rank":2}]}],"window":["98:1","98:2","98:3","98:4","98:5","98:6","98:7","98:8"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"98:3","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":8,"source_present":true,"structured_insight_count":12,"unstructured_record_count":0},"identity":{"ayah_ref":"98:3","lane":"micro","linguistic_source_ref":"98:3","surface_ref":"98:3","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"98:3","target_tokens":[["Onlarda",["98:3:1"]],["dosdoğru",["98:3:3"]],["yazılar",["98:3:2"]],["vardır",["98:3:1","98:3:2","98:3:3"]]],"text":"Onlarda dosdoğru yazılar vardır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":8,"id":"s098-p01-001-008","label":"Whole surah","number":1,"refs":["98:1","98:2","98:3","98:4","98:5","98:6","98:7","98:8"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:2:textual-upright-root-pair","source_type":"word_analysis","support_id":"sup_0618efc09ba666ea04e1","text":"{\"blocking_evidence\":null,\"headline\":\"book-root and upright-root define each other\",\"reader_payoff\":\"The reader sees that written content and uprightness are paired locally, so the adjective is not a decorative quality added after the noun.\",\"reason\":\"Attachment evidence binds {{ar:قَيِّمَةٌ}} ({{tr:qayyimatun}}) directly to {{ar:كُتُبٌ}} ({{tr:kutubun}}), and the CRITICAL rows supply the concrete 9:36 and 98:5 witnesses for the wider pairing.\",\"representative_source_ids\":[\"QI-35fd3301\",\"MI-88141822\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"98:3:3:1","source_type":"qac_morpheme","support_id":"sup_064409a4134715425088","text":"{\"lemma_ar\":\"قَيِّمَة\",\"morph_features\":\"STEM|POS:ADJ|LEM:qay~imap|ROOT:qwm|F|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"ADJ\",\"qac_ref\":\"98:3:3:1\",\"qac_word_ref\":\"98:3:3\",\"root_ar\":\"ق و م\",\"surface_ar\":\"قَيِّمَةٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:3:verbless-quality-assertion","source_type":"word_analysis","support_id":"sup_0815d6406f85cd238ea6","text":"{\"blocking_evidence\":null,\"headline\":\"verbless adjective makes uprightness a standing assertion\",\"reader_payoff\":\"The reader hears uprightness as a standing quality of the writings, not as something newly made or narrated.\",\"reason\":\"The clause is nominal and compressed, so the adjective completes the assertion without an event verb.\",\"representative_source_ids\":[\"QG-7d45f817\",\"QT-530d7854\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:2:plural-distributed-contents","source_type":"word_analysis","support_id":"sup_1b085e9037707e0c6f9f","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite plural distributes the contents\",\"reader_payoff\":\"The reader sees several written contents or prescriptions within one container rather than one collapsed book-title.\",\"reason\":\"The local form is plural and indefinite, so the multiplicity claim is grammatically grounded.\",\"representative_source_ids\":[\"QF-28de27e1\",\"QF-d5e21f7e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:3:upright-corrective-value","source_type":"word_analysis","support_id":"sup_1b2ad07b3a267ce91069","text":"{\"blocking_evidence\":null,\"headline\":\"uprightness, correction, subsistence, and value converge\",\"reader_payoff\":\"The reader sees the adjective judge the writings as upright, corrective, and worthy from within their own structure, while unrelated root branches stay outside the local sense.\",\"reason\":\"V4 supports straightness, establishing, support, and value branches for {{ar:ق و م}} ({{tr:q-w-m}}), but the local word is a qualitative adjective of writings, so the broader family is narrowed to textual uprightness, correction, subsistence, and worth.\",\"representative_source_ids\":[\"QS-092b3ed0\",\"QS-11f366cf\",\"QS-efe4c90f\",\"QS-f99b9a29\",\"MS-27be55df\",\"MS-7883d75d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:3","source_type":"word_analysis","support_id":"sup_1c53f3c89ff110bfed2f","text":"{\"gloss_range\":\"feminine singular qualitative adjective modifying the broken plural writings: upright, sound, corrective, valuable, and self-standing in local force\",\"prose\":\"{{ar:قَيِّمَةٌ}} ({{tr:qayyimatun}}) closes the ayah as the adjective of {{ar:كُتُبٌ}} ({{tr:kutubun}}), with feminine singular agreement attaching the quality to the broken plural writings rather than to the earlier suffix. The word does not merely say that the writings exist; in a verbless clause it evaluates them as a standing quality: upright, corrective, worthy, and internally sound. Its doubled intensive shape makes that uprightness inherent rather than a simple standing posture, and the central doubled sound makes that density audible. The local adjective also belongs to a constrained upright-religion formula field, with witnesses at 9:36, 12:40, and 30:30, while keeping the selected field away from unrelated {{ar:ق و م}} ({{tr:q-w-m}}) branches such as people, bodily rising, or resurrection. Within the surah, this quality anticipates the move from upright writings in 98:3 to upright religion and established practice in 98:5, so textual correctness becomes enacted order; its shared final tanwīn cadence with {{ar:كُتُبٌ}} ({{tr:kutubun}}) lets the ayah land as a balanced noun-and-quality phrase.\",\"root_display\":\"{{ar:ق و م}} ({{tr:q-w-m}})\",\"root_gloss_range\":\"the root ranges across people, standing, undertaking, guardianship, establishing, straightness, support, value, and other branches; the local adjective selects uprightness, correctness, establishment, and worth, not people or resurrection branches\",\"surface_display\":\"{{ar:قَيِّمَةٌ}} ({{tr:qayyimatun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:3:constrained-upright-form-field","source_type":"word_analysis","support_id":"sup_244b2344e7a0157aad41","text":"{\"blocking_evidence\":null,\"headline\":\"qualitative q-w-m field is specialized\",\"reader_payoff\":\"The reader recognizes a specialized upright-religion formula field, with witnesses such as 9:36, 12:40, and 30:30, applied here first to writings.\",\"reason\":\"The exact count in the CRITICAL row is less important than the supported constraint: this local adjective belongs to a specialized qualitative uprightness field rather than the root's unrelated people or resurrection branches.\",\"representative_source_ids\":[\"QI-53db80c8\",\"QE-9fecbb03\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:3:ayah-final-quality-closure","source_type":"word_analysis","support_id":"sup_358da71a9c2b8ccc25fb","text":"{\"blocking_evidence\":null,\"headline\":\"final adjective seals the ayah with quality\",\"reader_payoff\":\"The reader feels the short ayah land on the writings' upright quality rather than merely on the fact that writings exist.\",\"reason\":\"The adjective is the final word of the ayah, shares the nominative indefinite cadence with {{ar:كُتُبٌ}} ({{tr:kutubun}}), and marks the transition from externally purified pages in 98:2 to internally upright contents in 98:3.\",\"representative_source_ids\":[\"QT-74bebf01\",\"QP-57247225\",\"QB-678252cd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"98:3:2:1","source_type":"qac_morpheme","support_id":"sup_610e88189aa193e91c3f","text":"{\"lemma_ar\":\"كِتَٰب\",\"morph_features\":\"STEM|POS:N|LEM:kita`b|ROOT:ktb|MP|INDEF|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"98:3:2:1\",\"qac_word_ref\":\"98:3:2\",\"root_ar\":\"ك ت ب\",\"surface_ar\":\"كُتُبٌ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:2:noun-adjective-cadence","source_type":"word_analysis","support_id":"sup_7b75eca1a07467f1b02d","text":"{\"blocking_evidence\":null,\"headline\":\"paired tanwīn binds noun and adjective\",\"reader_payoff\":\"The reader can hear the noun and its quality land as one compact phrase before analysis separates subject and modifier.\",\"reason\":\"Both adjacent words are indefinite nominatives and attachment evidence makes the adjective modify the noun.\",\"representative_source_ids\":[\"QP-39046db7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:1:locative-container-predicate","source_type":"word_analysis","support_id":"sup_8558b715415dc29b236f","text":"{\"blocking_evidence\":null,\"headline\":\"locative predicate makes containment explicit\",\"reader_payoff\":\"The reader sees the writings as contents located within the carried proof or pages, not as a detached description after them.\",\"reason\":\"Attachment evidence makes {{ar:فِيهَا}} ({{tr:fīhā}}) the fronted locative predicate for {{ar:كُتُبٌ}} ({{tr:kutubun}}), licensing both page-containment and evidentiary inclusion.\",\"representative_source_ids\":[\"QG-b9682a19\",\"QS-2257f06a\",\"QS-f8c8c951\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:2:dominant-written-register","source_type":"word_analysis","support_id":"sup_8a3a84a632bf6c35d874","text":"{\"blocking_evidence\":null,\"headline\":\"noun distribution keeps the written-document register normal\",\"reader_payoff\":\"The reader treats the word as part of the familiar written-document field before adding the local plural and qualitative nuances.\",\"reason\":\"The contextual profile shows a large noun-concrete distribution for {{ar:ك ت ب}} ({{tr:k-t-b}}), while the local grammar supplies the narrowing to an indefinite plural subject.\",\"representative_source_ids\":[\"QI-60155b67\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:3:intensive-doubled-form","source_type":"word_analysis","support_id":"sup_8ae04805157e7c5519eb","text":"{\"blocking_evidence\":null,\"headline\":\"doubled form intensifies inherent correctness\",\"reader_payoff\":\"The reader hears and sees the adjective as denser than a simple standing participle, making correctness feel built into the writings.\",\"reason\":\"QAC marks the word as a qualitative adjective on an intensive doubled pattern, and the phonetic row is tied to the actual local form.\",\"representative_source_ids\":[\"QF-7f845a9e\",\"MF-ec613f6f\",\"QP-d413cbf6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:1:fronted-container-staging","source_type":"word_analysis","support_id":"sup_8bc0fb17c52afa03818b","text":"{\"blocking_evidence\":null,\"headline\":\"fronting makes the container given and contents new\",\"reader_payoff\":\"The reader enters the already supplied container before discovering the writings, so the word order stages disclosure rather than merely reporting existence.\",\"reason\":\"The local clause is a nominal construction with {{ar:فِيهَا}} ({{tr:fīhā}}) before the delayed subject, so the CRITICAL fronting and discovery claims match the syntax.\",\"representative_source_ids\":[\"QT-95b61df2\",\"QT-e99709d9\",\"MT-f3affc1f\",\"QY-a4028f40\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:2","source_type":"word_analysis","support_id":"sup_971b43378e7603f5a832","text":"{\"gloss_range\":\"indefinite plural written contents or scriptures as the delayed nominative subject inside the locative frame\",\"prose\":\"{{ar:كُتُبٌ}} ({{tr:kutubun}}) is the delayed nominative subject disclosed after {{ar:فِيهَا}} ({{tr:fīhā}}), so the writings are what the carried proof or pages contain. Its indefinite plural avoids naming one definite title and instead presents multiple written contents by kind and quality, preparing the closing adjective to define what sort of writings they are. The {{ar:ك ت ب}} ({{tr:k-t-b}}) family gives the noun more than a bare book-label: writing, joining, and binding decree converge here as recorded contents that also carry prescriptive order, while the local form remains a concrete plural noun, not an abstract verb. The word also belongs to the surah's book-thread around 98:1, 98:4, and 98:6, and its pairing with {{ar:قَيِّمَةٌ}} ({{tr:qayyimatun}}) makes written content and upright ordering mutually interpretive. Their shared final tanwīn cadence lets the noun and its quality land audibly as one compact phrase.\",\"root_display\":\"{{ar:ك ت ب}} ({{tr:k-t-b}})\",\"root_gloss_range\":\"joining, writing, copying, decreeing, prescribing, registering, and contracting are available root branches; the local plural noun selects written contents with ordered and prescriptive force\",\"surface_display\":\"{{ar:كُتُبٌ}} ({{tr:kutubun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:3:textual-uprightness-pairing","source_type":"word_analysis","support_id":"sup_9e2aec062f6d2736d40e","text":"{\"blocking_evidence\":null,\"headline\":\"uprightness is attached to written contents\",\"reader_payoff\":\"The reader sees correctness as a property of the texts themselves, not as a free-floating moral abstraction.\",\"reason\":\"The adjective is syntactically attached to {{ar:كُتُبٌ}} ({{tr:kutubun}}), preserving the CRITICAL claim that {{ar:ق و م}} ({{tr:q-w-m}}) uprightness is textual here.\",\"representative_source_ids\":[\"QI-a49f60dd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:1:feminine-suffix-antecedent","source_type":"word_analysis","support_id":"sup_a381b48db9f7c4908bb1","text":"{\"blocking_evidence\":null,\"headline\":\"feminine suffix keeps two antecedents live\",\"reader_payoff\":\"The reader notices that the short suffix carries reference across the ayah boundary while preserving both the clear proof of 98:1 and the purified pages of 98:2 as possible containers.\",\"reason\":\"QAC and attachment evidence both mark the suffix in {{ar:فِيهَا}} ({{tr:fīhā}}) as feminine singular and warn against forcing only one antecedent; rows that make the purified pages the sole antecedent are narrowed to the attested ambiguity.\",\"representative_source_ids\":[\"QG-98a81bd3\",\"MG-619f0694\",\"QF-faa547ac\",\"QB-7d647437\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:2:written-prescriptive-records","source_type":"word_analysis","support_id":"sup_b4485af21def91f8fdb5","text":"{\"blocking_evidence\":null,\"headline\":\"writing, joining, and prescribing converge in written records\",\"reader_payoff\":\"The reader hears the contents as recorded, composed, and norm-setting, while still reading the local word as written contents rather than replacing it with abstract ordinances alone.\",\"reason\":\"V4 supports joining, writing, and decree branches for {{ar:ك ت ب}} ({{tr:k-t-b}}), but QAC fixes the local surface as a concrete plural noun, so the prescriptive and stitching force is preserved as pressure within written contents.\",\"representative_source_ids\":[\"QS-28ca6841\",\"QS-50d37ea9\",\"QS-831d5db0\",\"QS-927bf9e8\",\"QS-f69ba02a\",\"MS-01405cfc\",\"MS-91cdd932\",\"QY-6716a9de\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:1","source_type":"word_analysis","support_id":"sup_c311da74abff27e0afc9","text":"{\"gloss_range\":\"fronted locative preposition plus feminine singular suffix, with the antecedent deliberately kept open between the clear proof and the purified pages\",\"prose\":\"{{ar:فِيهَا}} ({{tr:fīhā}}) opens the ayah by placing the reader inside a referent already carried from 98:1-2 before the writings are named. Its feminine suffix can resume the clear proof of 98:1 or the purified pages of 98:2, so the word should not force only one container where the grammar keeps both accessible. The preposition makes that carried referent a locative predicate for {{ar:كُتُبٌ}} ({{tr:kutubun}}): the point is not merely association or source, but contents found within the proof or pages. Because the locative comes first, the known container frames the new disclosure; the movement shifts from the recitation scene of 98:2 into a compressed nominal assertion about what those pages or that proof contain.\",\"root_display\":\"\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فِيهَا}} ({{tr:fīhā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:3:same-surah-text-to-practice","source_type":"word_analysis","support_id":"sup_eb05edb306f80409fd1b","text":"{\"blocking_evidence\":null,\"headline\":\"upright writings anticipate upright practice\",\"reader_payoff\":\"The reader notices that the quality attached to writings in 98:3 returns in 98:5 as religion and practice, moving from textual correctness to enacted order.\",\"reason\":\"The CRITICAL rows give the concrete same-surah recurrence at 98:5, and local syntax first anchors the quality in the writings of 98:3.\",\"representative_source_ids\":[\"QI-30a29dc2\",\"MI-84b879fb\",\"QE-70aa2bb1\",\"ME-1c346e95\",\"QB-f78fb171\",\"QY-d19bc06a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:2:same-surah-book-thread","source_type":"word_analysis","support_id":"sup_ec56d1d863b1230cff33","text":"{\"blocking_evidence\":null,\"headline\":\"the plural answers the surah's book thread\",\"reader_payoff\":\"The reader hears this plural as contents inside a surrounding evidence-and-book thread that includes 98:1, 98:4, and 98:6.\",\"reason\":\"The CRITICAL rows give concrete same-surah references, and the local noun supplies the internal-content specialization; broad book-declaration witnesses such as 2:2, 3:3, and 11:1 are useful as formulaic background only.\",\"representative_source_ids\":[\"QI-d05ccd37\",\"QE-b55dc92b\",\"QE-cd11f56f\",\"QB-864ccf25\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:2:delayed-indefinite-subject","source_type":"word_analysis","support_id":"sup_f2281f5b03b1c784219c","text":"{\"blocking_evidence\":null,\"headline\":\"delayed indefinite subject foregrounds qualitative writings\",\"reader_payoff\":\"The reader notices that the writings arrive as the clause's new subject inside the container, with quality foregrounded over a known title.\",\"reason\":\"QAC marks {{ar:كُتُبٌ}} ({{tr:kutubun}}) as an indefinite nominative delayed subject, and attachment evidence places it after the fronted predicate {{ar:فِيهَا}} ({{tr:fīhā}}).\",\"representative_source_ids\":[\"QG-7c0749ed\",\"QG-a9ce672d\",\"QG-ae6c090c\",\"MG-29e96190\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:3:adjective-agreement-to-kutub","source_type":"word_analysis","support_id":"sup_f3674a904b3ccdcb225d","text":"{\"blocking_evidence\":null,\"headline\":\"feminine singular adjective binds to the broken plural\",\"reader_payoff\":\"The reader sees the upright quality locked onto the writings themselves, not redirected to the earlier feminine suffix.\",\"reason\":\"QAC and attachment evidence identify {{ar:قَيِّمَةٌ}} ({{tr:qayyimatun}}) as a feminine singular qualitative adjective modifying the broken plural {{ar:كُتُبٌ}} ({{tr:kutubun}}).\",\"representative_source_ids\":[\"QG-743bd667\",\"MG-da801be8\",\"QF-9514be9f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:2:nominal-disclosure-and-boundary","source_type":"word_analysis","support_id":"sup_f6c1cf04bdcaed92eff3","text":"{\"blocking_evidence\":null,\"headline\":\"nominal placement makes writings a standing fact\",\"reader_payoff\":\"The reader notices the move from purified medium to authoritative contents as a stable disclosure rather than a narrated placement event.\",\"reason\":\"The clause has no finite verb and places the delayed subject after the fronted locative predicate, matching the standing-fact and medium-to-content rows.\",\"representative_source_ids\":[\"QT-788368dc\",\"QT-fbb99a8a\",\"QB-1d7fb9da\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"98:3:1:boundary-to-nominal-content","source_type":"word_analysis","support_id":"sup_ff064653479236f5533e","text":"{\"blocking_evidence\":null,\"headline\":\"boundary shifts from recitation to standing contents\",\"reader_payoff\":\"The reader feels the passage move from the active recitation of 98:2 to a stable statement about the nature of what is contained.\",\"reason\":\"The attachment layer identifies a compressed nominal clause with no overt copula, supporting the shift from event language to standing content.\",\"representative_source_ids\":[\"QB-a31b8a0a\",\"QB-ea55712a\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فِيهَا كُتُبٌۭ قَيِّمَةٌۭ","ayah_ref":"98:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001273/B008","root_001283/B001","root_001283/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001283","role":"Joining one thing to another makes the plural writings an integrated assembly rather than a loose heap.","root":"ك ت ب","source_ref":"98:3","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_001283","role":"Letters joined into a written object fixes the assembly specifically in textual form.","root":"ك ت ب","source_ref":"98:3","source_word_indices":["2"]},{"branch_id":"B008","mapped_root_id":"root_001273","role":"Straightness, balance, and just speech make coherence an upright normative arrangement.","root":"ق و م","source_ref":"98:3","source_word_indices":["3"]}],"changed_reading":{"after":"A plurality of written units whose joined components form a coherent, upright arrangement.","before":"Books that are simply good or correct."},"confidence":"strong","focus_anchor":"The plural writings at word 2 and their q-w-m adjective at word 3.","mechanism":"K-t-b supplies both assembled parts and letters joined as writing, while q-w-m supplies straightness and evenness. The phrase therefore presents multiple written units whose rightness includes coherent internal arrangement.","model_id":"baseline_integrated_upright_units"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_integrated_upright_units","source_type":"hft","support_id":"sup_1d442c9e1534d169a72d","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِيهَا كُتُبٌۭ قَيِّمَةٌۭ","ayah_ref":"98:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001273/B004","root_001273/B009","root_001283/B003"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001283","role":"Binding decree turns writing into an effective prescription or settled judgment.","root":"ك ت ب","source_ref":"98:3","source_word_indices":["2"]},{"branch_id":"B004","mapped_root_id":"root_001273","role":"Care, guardianship, and maintenance give the adjective an active order-preserving role.","root":"ق و م","source_ref":"98:3","source_word_indices":["3"]},{"branch_id":"B009","mapped_root_id":"root_001273","role":"Mainstay and subsistence make the writings supports by which a larger system remains standing.","root":"ق و م","source_ref":"98:3","source_word_indices":["3"]}],"changed_reading":{"after":"Binding inscriptions that actively maintain and support a durable order.","before":"Correct statements contained in writings."},"confidence":"medium","focus_anchor":"The same k-t-b noun can denote binding inscription, and the q-w-m adjective can denote guardianship and support.","mechanism":"An inscription that imposes judgment is paired with what maintains, governs, and keeps a thing standing. The writings are therefore potentially operative instruments that establish and sustain an order, not merely descriptions of one.","model_id":"baseline_binding_sustaining_order"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_binding_sustaining_order","source_type":"hft","support_id":"sup_6571f8bb4a6b2bb05ae0","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فِيهَا كُتُبٌۭ قَيِّمَةٌۭ","ayah_ref":"98:3"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001273/B010","root_001273/B015","root_001283/B004"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_001283","role":"Entry into a register supplies the documentary act of placing persons or matters into an ordered record.","root":"ك ت ب","source_ref":"98:3","source_word_indices":["2"]},{"branch_id":"B010","mapped_root_id":"root_001273","role":"Value and appraisal supply the scale by which registered entries receive standing.","root":"ق و م","source_ref":"98:3","source_word_indices":["3"]},{"branch_id":"B015","mapped_root_id":"root_001273","role":"Equal weight and exact measure constrain appraisal to a balanced standard.","root":"ق و م","source_ref":"98:3","source_word_indices":["3"]}],"changed_reading":{"after":"Writings functioning as an appraised register whose entries are set by exact measure.","before":"Writings possessing intrinsic worth."},"confidence":"exploratory","focus_anchor":"The plural k-t-b form can evoke registered entries, while q-w-m includes valuation and exact measure.","mechanism":"Registration, appraisal, and equal measure combine into a documentary mechanism: the writings can be read as records that assign standing according to a stable scale.","model_id":"baseline_appraised_register"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_appraised_register","source_type":"hft","support_id":"sup_ffc9f173b9a085642696","trust":"legacy_unbound"}]}
</lane_packet_json>
