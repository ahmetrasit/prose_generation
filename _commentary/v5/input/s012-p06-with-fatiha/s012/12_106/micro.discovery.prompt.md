# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **12:106**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s012-p06-with-fatiha/s012/12_106/micro.discovery.json` and modify nothing
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
  "ayah_ref": "12:106",
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
{"analysis_context":{"analysis_id":"s012-p06-with-fatiha","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"12:106","host_surah":12,"lane_context_refs":[],"ordered_context_refs":["12:94","12:95","12:96","12:97","12:98","12:99","12:100","12:101","12:102","12:103","12:104","12:105","12:107","12:108","12:109","12:110","12:111","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B001","candidate_links":[{"candidate_id":"cand_6f1a237e763c488b60b8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"12:106:4:2","qac_word_ref":"12:106:4","surface_ar":"ٱللَّهِ"}],"gloss":"tapınma ve tapınılan varlık","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."}},{"facet_id":"F004","role":"example","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Eylem çekirdeğiyle ondan türeyen tapınılan varlık anlamının birlikte temsil edilmesi gereken genel açıklamalarda kullanılır.","boundary_detail":"Dal, tapınma eylemi ile bundan türeyen tapınılan veya tapınılır kılınan varlık anlamlarını kapsar; şaşkınlık, yoğun üzüntü ve salt özel ad kullanımları bu sınırın dışındadır.","branch_image_ar":"التعبد والمعبود","concept_gloss":"tapınma ve tapınılan varlık","contextual_glosses":[{"applicability":"Bir kişinin tapınma eylemini veya kendini tapınmaya vermesini bildiren eylem bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylem olarak tapınma çekirdeğini eksiksiz korur."},"facet_ids":["F001"],"text":"tapınmak","usage_role":"general"},{"applicability":"Bir topluluğun kendisine tapındığı varlık veya nesneden söz edilen ad bağlamlarında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tapınmanın yöneldiği varlık veya nesne anlamını korur."},"facet_ids":["F002"],"text":"tapınılan varlık","usage_role":"contextual"},{"applicability":"Bir varlığın başkalarına tapınma konusu olarak benimsetilmesini anlatan ettirgen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir varlığı tapınma konusu durumuna getirme işlemini korur."},"facet_ids":["F003"],"text":"tapınılır kılmak","usage_role":"explanatory"}],"definition":"Bir varlığa tapınma eylemini ve kişinin kendini tapınmaya vermesini anlatır. Türemiş kullanımlarda bir varlığı tapınılır kılmayı, tapınılan varlığı ve tapınma konusu sayılan varlıkları da adlandırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel eylem, bir varlığa tapınmak ve kişinin kendini bu tapınmaya vermesidir."},{"facet_id":"F002","role":"extension","statement":"Eylemden türeyen varlık anlamı, kendisine tapınılan varlığı veya tapınma konusu sayılan nesneyi gösterir."},{"facet_id":"F003","role":"specialization","statement":"Ettirgen kullanım, bir varlığı başkalarınca tapınılır duruma getirme veya öyle sunma işlemini bildirir."},{"facet_id":"F004","role":"example","statement":"Güneşe kimi topluluklarca tapınılması nedeniyle ona tapınılan varlık anlamındaki bir ad verilmesi, varlık anlamının tarihsel bir örneğidir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Yalnızca belirli bir varlık türünü adlandırdığı için bütün dalın karşılığı sanılabilir.","fit":"narrowing","loses":"Tapınma eylemini, kişinin tapınmaya yönelmesini ve tapınılır kılma işlemini karşılamaz.","preserves":"Tapınılan varlık anlamını kısa ve doğal biçimde korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi tapınma eylemini, kişinin kendini tapınmaya vermesini, bir varlığı tapınılır kılmayı ve tapınılan varlığı aynı anlam örgüsü içinde açıkça birleştirir. Geçici dal çerçevesi bu çekirdeği ve ondan türeyen varlık adlarını doğru biçimde temsil eder.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"tapınmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"kendini tapınmaya vermek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"tapınılır kılmak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"tapınılan varlık, tanrı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"tapınılan varlık"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tanrılar, tapınılan nesneler"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tapınma"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"kimi toplulukların tapındığı için bu adla anılan güneş"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"senin tapınman"}],"lexicalization_note":"Tanım, yalın eylem çekirdeğini türemiş eylem ve varlık adlarından ayırır; türemiş biçimlerin kapsamı yalın eylemin tamamına aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Tapınma eylemi, korkuya bağlı özel tapınma yaşayışı ve aynı kökün özel ad dalı sınırı keskinleştirdi; peygamberlik, büyücülük, belirli tapınma nesneleri, sahiplik ve tarihsel hizmet grubu adayları ise yalnızca aynı dinsel alana veya tekil örneklere temas ettiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal eylem ve yaklaşma yönünde yoğunlaşırken bu dal aynı çekirdekten tapınılan varlık ile ettirgen kılma anlamlarını da türetir; bu yüzden yalnızca eylem bağlamında yakınlaşırlar.","focus_only":"Tapınılan varlığı ve bir varlığı tapınılır kılma işlemini de adlandırır.","gloss":"tapınma ve yaklaşarak yönelme","neighbor_only":"Tapınmayla birlikte yaklaşma ve kendini bu işe verme yönünü öne çıkarır.","neighbor_ref":"root_001498/B001","relation_type":"near_synonym","shared_zone":"İki dal da tapınma eylemini ve kişinin bu eyleme yönelmesini kapsar."},{"boundary_match":"partial","distinction":"Bu dal genel tapınma çekirdeğini ve ondan türeyen varlık anlamlarını kapsar; komşu dal ise korku, inziva ve olağanın üstündeki uygulamalarla sınırlı özel bir yaşayışı anlatır.","focus_only":"Tapınmayı korku, inziva veya aşırı uygulama koşuluna bağlamaz ve tapınılan varlığı da adlandırabilir.","gloss":"korkuyla yoğunlaşan özel tapınma yaşayışı","neighbor_only":"Korkudan doğan, inziva veya ek yüklenme biçimindeki özel bir tapınma yaşayışını bildirir.","neighbor_ref":"root_000604/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da kişinin kendini tapınmaya vermesi bulunur."},{"boundary_match":"partial","distinction":"Bu dal genel anlam örgüsünü verir; komşu dal ise o örgüden türemiş özel adı ve adın belirli söz kalıplarındaki kullanımını ayrı bir biçim alanı olarak sınırlar.","focus_only":"Genel tapınma eylemini, tapınılan varlığı ve tapınılır kılmayı kapsar.","gloss":"Yaratıcıya özgü ad ve kullanım kalıpları","neighbor_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek ve ant kalıplarını kapsar.","neighbor_ref":"root_000047/B002","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlık düşüncesi üzerinden bu dalın varlık anlamıyla bağlantılıdır."}],"source_phrase_ar":"أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)","source_summary":"Kaynakların ortak çizgisi, tapınmayı anlamın temeli sayar; kişinin tapınmaya yönelmesini, tapınılan varlığı ve tapınılır kılma işlemini bu temelden türetir. Tapınma konusu sayılan yontular ve güneş örneği, varlık anlamının belirli uygulamalarıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أله وتأله بمعنى عبد وتنسك، والتأليه بمعنى التعبيد، والإله والآلهة والإلاهة لما جعل معبودا.","what_is_not_ar":"لا يدخل فيه أله بمعنى تحير، ولا ألهت على فلان بمعنى اشتد جزعي عليه، ولا أسماء المواضع أو الحية أو الهلال إلا من جهة التسمية لا معنى العبادة."},"support_links":["sup_d26586b0c72196ec6a72"]},{"boundary":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000047/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"12:106:4:2","qac_word_ref":"12:106:4","surface_ar":"ٱللَّهِ"}],"gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."}},{"facet_id":"F005","role":"source_variant","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}}],"root_ar":"ء ل ه","root_id":"root_000047","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özel adın kendisiyle ona bağlı seslenme, dilek ve ant kullanımlarının birlikte açıklanması gereken dal düzeyinde kullanılır.","boundary_detail":"Dal, özel ad ile bu ada bağlı seslenme, dilek, şaşma ve ant biçimleriyle sınırlıdır; herhangi bir tapınılan varlığı gösteren genel ad anlamına genişletilmez.","branch_image_ar":"اسم الله في القسم والنداء","concept_gloss":"Yaratıcıya özgü ad ile seslenme ve ant biçimleri","contextual_glosses":[{"applicability":"Söz konusu adın yalnız Yaratıcıyı gösteren yalın ad olarak ele alındığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Adın Yaratıcıya özgü olmasını ve ayırt edici ad işlevini korur."},"facet_ids":["F001"],"text":"Yaratıcı'nın özel adı","usage_role":"general"},{"applicability":"Yakarış veya dilek sırasında Yaratıcıya doğrudan seslenilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya yöneltilen doğrudan seslenme işlevini doğal biçimde korur."},"facet_ids":["F004"],"text":"ey Tanrı","usage_role":"contextual"},{"applicability":"Özel adın bir bildirimin doğruluğunu pekiştiren ant değeri taşıdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yaratıcıya dayanarak ant verme işlevini açık biçimde korur."},"facet_ids":["F003"],"text":"Tanrı adına ant olsun","usage_role":"contextual"},{"applicability":"Özel adın ses veya parçaları düşürülmüş tarihsel kalıplarının işlevini açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kısaltılma biçimini ve şaşma ya da ant işlevini birlikte korur."},"facet_ids":["F005"],"text":"kısaltılmış şaşma veya ant sözü","usage_role":"explanatory"}],"definition":"Yaratıcıya özgü adın kendisini ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar. Bu biçimler doğrudan seslenme, adın ant değeriyle kullanılması veya ses ve parçaların düşürülmesiyle kısaltılma yollarını gösterir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dalın merkezinde, Yaratıcıyı başkalarından ayırarak gösteren ve yalnız ona özgü sayılan özel ad bulunur."},{"facet_id":"F002","role":"source_variant","statement":"Özel adın, tapınılan varlığı bildiren genel addan ses düşmesi ve belirleyici unsur eklenmesiyle oluştuğu açıklanır."},{"facet_id":"F003","role":"associated_use","statement":"Özel ad, sözün başında ant değeri taşıyarak ardından gelen yapmama bildirimini güçlendirebilir."},{"facet_id":"F004","role":"associated_use","statement":"Özel adın doğrudan ya da seslenme öğesi yerine geçen bir sonla kullanılması, yakarma ve dilek bildiren seslenme biçimleri kurar."},{"facet_id":"F005","role":"source_variant","statement":"Ses veya parçaların düşürüldüğü kısalmış biçimler, şaşma ve ant anlatan kalıplarda kullanılır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Genel tür adı olarak başka tapınılan varlıklar için de kullanılabildiğinden özel adla karışır.","fit":"narrowing","loses":"Adın tek bir varlığa özgü özel ad oluşunu ve seslenme ile ant biçimlerini karşılamaz.","preserves":"Yüce bir tapınılan varlığa gönderimde bulunma yönünü korur."},"text":"tanrı"}],"identity_rationale":"Kaynak ifadesi Yaratıcıya özgü adın kendisini, genel tapınılan-varlık adından türetiliş açıklamasını ve bu özel adla kurulan seslenme ile ant biçimlerini birlikte verir. Geçici çerçeve kullanılabilir, ancak dal yalnızca seslenme ve ant kalıpları değildir; özel adın yalın kullanımı da çekirdekte tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"Yaratıcıya özgü ad"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"Tanrı adına ant olsun, bunu yapmadım"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"ey Tanrı; yakarma seslenişi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ey Tanrı; doğrudan seslenme"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"Tanrı adına sen veya baban; şaşma ya da ant kalıbı"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları"}],"lexicalization_note":"Yalın özel ad, doğrudan seslenme biçimleri ve ant ya da şaşma kalıpları ayrı tutulur; kalıplara özgü işlevler özel adın her kullanımına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Genel tapınma dalı, yaşam üzerine ant, genel seslenme, kısaltılmış kişi seslenmesi ve yakarışa karşılık sözü gerçek sınır karşılaştırmaları sağladı; baba hitapları, genel dışlama yapıları, başka ant sözleri ve sesçe eşlik eden kalıplar daha zayıf ya da yalnızca biçimsel temas gösterdiği için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal belirli bir özel adın biçim ve kullanım alanıdır; komşu dal ise özel adla sınırlanmayan genel tapınma eylemini ve tapınılan varlık anlamını verir.","focus_only":"Yaratıcıya özgü adı ve bu adla kurulan seslenme, dilek, şaşma ve ant biçimlerini kapsar.","gloss":"tapınma ve tapınılan varlık","neighbor_only":"Genel tapınma eylemini, tapınılan varlığı ve bir varlığı tapınılır kılma işlemini kapsar.","neighbor_ref":"root_000047/B001","relation_type":"near_neighbor","shared_zone":"Özel ad, tapınılan yüce varlığı göstermesi bakımından genel varlık anlamına dayanır."},{"boundary_match":"partial","distinction":"Ortak işlev ant vermedir, fakat bu dalın dayanağı Yaratıcıya özgü addır; komşu dal yaşam süresini bildiren sözleri kullanır ve ayrıca ısrarlı istemeye uzanabilir.","focus_only":"Ant işlevini Yaratıcıya özgü adın yalın veya kısalmış biçimleriyle kurar.","gloss":"ömür üzerine ant ve ısrarlı isteme","neighbor_only":"Ant veya ısrarlı isteme işlevini yaşam süresini bildiren sözlerle kurar.","neighbor_ref":"root_001044/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir sözü güçlendiren ant işlevli kalıplar içerir."},{"boundary_match":"field_only","distinction":"Bu dal belirli bir muhatabın özel adı çevresinde oluşur; komşu dal ise muhatabın kimliğinden bağımsız genel seslenme araçlarını ve uzaklık ayrımını konu edinir.","focus_only":"Belirli bir özel adı ve o adın yakarma ile ant kullanımlarını içerir.","gloss":"genel seslenme öğeleri","neighbor_only":"Yakın veya uzaktaki muhataba yöneltilen genel seslenme öğelerini bildirir.","neighbor_ref":"root_000074/B008","relation_type":"same_field","shared_zone":"Her iki dal da doğrudan seslenme sırasında kullanılan biçimlerle ilgilidir."},{"boundary_match":"field_only","distinction":"Bu dalın kısalmaları belirli özel adın dinsel seslenme ve ant işlevlerine bağlıdır; komşu dalın kısalmaları ise belirsiz bir kişiye seslenmenin dilbilgisel biçimleridir.","focus_only":"Yaratıcıya özgü adı ve ona bağlı seslenme ile ant biçimlerini kapsar.","gloss":"kişiye yönelik kısaltılmış seslenme","neighbor_only":"Belirsiz bir kişiye yönelen kısaltılmış seslenme biçimlerini kapsar.","neighbor_ref":"root_001178/B003","relation_type":"same_field","shared_zone":"Her iki dalda da seslenme sırasında biçimsel kısalma görülebilir."},{"boundary_match":"thematic_only","distinction":"Bu dal bir muhataba seslenir; komşu dal ise söylenmiş yakarışa kabul dileği veya onayla karşılık verir. Aynı sahnede bulunsalar da anlam çekirdekleri örtüşmez.","focus_only":"Yakarışın yöneltildiği Yaratıcıyı özel adıyla çağırır.","gloss":"yakarışın kabulünü isteyen karşılık","neighbor_only":"Yakarışın kabul edilmesini isteyen veya söyleneni onaylayan karşılık sözünü bildirir.","neighbor_ref":"root_000054/B003","relation_type":"thematic","shared_zone":"İki dal da yakarış ortamında kullanılan kısa söz biçimlerine katılır."}],"source_phrase_ar":"فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)","source_summary":"Kaynaklar özel adı Yaratıcıya özgü bir ad olarak tanımlar ve onu tapınılan varlığı gösteren genel adla köken bakımından ilişkilendirir. Aynı adın doğrudan seslenmede, yakarmada, ant bildiriminde ve parçaları düşürülmüş kalıplarda kullanıldığı birlikte gösterilir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه اسم الله والقول في أصله من إله، وصيغ الاستعمال مثل الله ما فعلت بمعنى والله، واللهم، ويا الله، ولاه أبوك أو لاه أنت ونحوها.","what_is_not_ar":"ليس فرعا مستقلا عن معنى الإله المعبود من جهة الاشتقاق، ولا يدخل فيه إطلاق إله أو آلهة على كل معبود إذا لم يكن الكلام على صيغة الاسم أو النداء أو القسم."},"support_links":[]},{"boundary":"Bu dal inanma ya da dua cevabi degil; korkudan emin olma, guven verme ve guvenilir sayilma alanidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000054/B001","candidate_links":[{"candidate_id":"cand_e7f07309c07dd908a75a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ءَامَنَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:'aAmana|ROOT:Amn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"12:106:2:1","qac_word_ref":"12:106:2","surface_ar":"يُؤْمِنُ"}],"gloss":"guven ve guvenilirlik","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel cekirdek korkuya karsi guven, ic yatiskinligi ve tehlikeden emin olma halidir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Guven verme, birini kendi koruma ve teminat alani icine alma olarak kullanilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Guvenilirlik, ihanete karsi sadakat, emanet edilen sey ve kendisine guvenilen kisi anlamlarini dogurur."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Guvenin bulundugu yer, bir kimsenin emniyet icinde oldugu mesken veya siginak olarak adlandirilir."}},{"facet_id":"F005","role":"example","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Dayanikli ve aksamasindan korkulmayan deve kullanimi, guvenilirlik niteligini canli bir ornege uygular."}}],"root_ar":"ء م ن","root_id":"root_000054","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Korkunun kalkmasi, kalbin yatismasi, guven verme ve guvenilir sayilma alanlarini birlikte tasiyan en kisa genel karsiliktir.","boundary_detail":"Bu dal inanma ya da dua cevabi degil; korkudan emin olma, guven verme ve guvenilir sayilma alanidir.","branch_image_ar":"سكون القلب في أمن وثقة","concept_gloss":"guven ve guvenilirlik","contextual_glosses":[{"applicability":"Korkunun giderilmesi ve ic yatiskinligi onde oldugunda dogal karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Emanet, guvenilirlik ve guven verme boyutlarini disarida birakir.","preserves":"Korku karsiti guven halini korur."},"facet_ids":["F001"],"text":"korkudan emin olma","usage_role":"contextual"},{"applicability":"Birinin baskasini koruma ve teminat altina almasi anlatildiginda kullanilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Guven icinde bulunma ve guvenilirlik adlandirmalarini kapsamaz.","preserves":"Bir baskasina guven saglama iliskisini korur."},"facet_ids":["F002"],"text":"guven verme","usage_role":"contextual"},{"applicability":"Kisi, emanet ya da dayanikli nesne guvenilirlik niteliginde anlatildiginda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Korkudan emin olma halini ve guven verme eylemini kapsamaz.","preserves":"Guvenilir sayilma ve emanet edilebilir olma tarafini korur."},"facet_ids":["F003","F005"],"text":"kendisine guvenilen","usage_role":"contextual"}],"definition":"Korkunun kalkmasiyla kalbin yatismasi, birine guven verilmesi veya bir kimsenin ya da seyin guvenilir kabul edilmesidir. Bu alan guvenli yer, emanet edilen sey, kendisine guvenilen kisi ve dayanilir binek gibi bagimli uygulamalari da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel cekirdek korkuya karsi guven, ic yatiskinligi ve tehlikeden emin olma halidir."},{"facet_id":"F002","role":"extension","statement":"Guven verme, birini kendi koruma ve teminat alani icine alma olarak kullanilir."},{"facet_id":"F003","role":"extension","statement":"Guvenilirlik, ihanete karsi sadakat, emanet edilen sey ve kendisine guvenilen kisi anlamlarini dogurur."},{"facet_id":"F004","role":"associated_use","statement":"Guvenin bulundugu yer, bir kimsenin emniyet icinde oldugu mesken veya siginak olarak adlandirilir."},{"facet_id":"F005","role":"example","statement":"Dayanikli ve aksamasindan korkulmayan deve kullanimi, guvenilirlik niteligini canli bir ornege uygular."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Tasdik ve dinî kabul alanini ekler.","collision":"Ayni kokun ayri tasdik daliyla karisir.","fit":"displacement","loses":"Korkudan guvende olma, emanet ve guvenilirlik alanlarini kaybettirir.","preserves":"Kalpte yonelme ya da kabul unsurunu ancak cok dolayli korur."},"text":"inanma"}],"identity_rationale":"Kaynak ifadeleri bu dali yalniz korkunun kalkmasi olarak degil, kalbin yatismasi, guven verme, guvenilirlik, emanet edilen sey, guvenli yer ve dayanilir nitelik alanlariyla birlikte verir. Bu nedenle dalin cercevesi, guvenlik ve guvenilirlik ekseninde hem yalın hem de yapimli ve baglamli kullanislari ayirt ederek korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ihanetin karsiti olan guvenilirlik ve emanet edilen sey"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"korkunun kalkmasi ve ic yatiskinligi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"guven, eminlik ve yatiskinlik hali"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"guven verme, guven hali veya guvenceye birakilan sey"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"guven icinde olmak ve korkusu kalkmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"birini guven icine almak ve ona guven saglamak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"guven icinde duruma gelmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"kendisine guvenilen emin kisi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"emanet edilen veya kendisine guvenilen kisi"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"guven icinde olan, emin"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"guvenilir veya emanet edilebilir olan"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kendisine bir sey emanet edilen kisi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"guven icinde, tehlikeden uzak ve yatiskin"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"insanlarin zararindan korkmadigi guvenilir kimse"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"herkese guvenen ve duydugunu dogru sayan kisi"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"kisinin en degerli ve icinin yatistigi mali"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"guvenli yer veya guven icindeki mesken"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"birinin guvencesi altina girmek"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"bir seyi birine emanet etmek ve onu guvenilir saymak"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"zayiflamasindan veya surcmesinden korkulmayan saglam deve"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"kullarini veya dostlarini zulümden ve azaptan guvende kilan"}],"lexicalization_note":"Yalin guven ve korkusuzluk anlamlari ile belirli yapimli ya da soz obegi kullanislari birlikte vardir; tanim bunlari tek bir dar kaliba indirgemez.","neighbor_coverage_note":"Adaylar arasinda en yararli ayrimlar guven, ic yatiskinligi, koruma ve ayni kokteki tasdik daliyla ilgilidir; digerleri uzak tematik senaryolar oldugu icin yayina alinmadi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda yatiskinlik korkudan emin olma ve guvenilirlik sonucudur; komsu dalda yatiskinlik dogru sayma ve kabul etme iliskisine baglidir.","focus_only":"Guvenlik, korkunun kalkmasi, emanet ve guvenilirlik alanlarini kurar.","gloss":"guven ile tasdik ayrimi","neighbor_only":"Bir haberin, vaadin veya hakikatin dogru sayilmasi alanini kurar.","neighbor_ref":"root_000054/B002","relation_type":"near_neighbor","shared_zone":"Ikisinde de kalbin yatismasi ve guven hissi bulunabilir."},{"boundary_match":"partial","distinction":"Komsu dal ic yakinlik ve dayanma tarafinda yogunlasir; bu dal ise korkusuzluk, teminat ve guvenilirlik kurumunu da semantik cekirdege alir.","focus_only":"Korku karsiti guvenligi, guven vermeyi ve emanet iliskisini de kapsar.","gloss":"guven ile icten dayanma","neighbor_only":"Bir seye alisma, yakinlik duyma ve ona icten dayanma tarafini one cikarir.","neighbor_ref":"root_001568/B005","relation_type":"near_synonym","shared_zone":"Her iki dalda da kalbin bir seye karsi yatismasi ve guven duymasi vardir."},{"boundary_match":"partial","distinction":"Bu dal guvenin nesnel veya iliskisel teminatini anlatabilir; komsu dal ise rahat gonullu ve genis ic durumunu anlatir.","focus_only":"Emanet, guven verme ve guvenilir sayilma gibi iliskileri de tasir.","gloss":"eminlik ile ic genisligi","neighbor_only":"Nefis, aile veya kalp genisligi ve sakin mizac alaninda durur.","neighbor_ref":"root_000691/B006","relation_type":"near_neighbor","shared_zone":"Her ikisi kisinin ic dunyasinda guven ve rahatlik tasvir edebilir."},{"boundary_match":"field_only","distinction":"Komsu dal guvenin sebebi olabilecek koruyucu yapida durur; bu dal ise guvenin hali, verilmesi ve guvenilirlik vasfini adlandirir.","focus_only":"Guven hali, guven verme ve guvenilirlik adlandirmalaridir.","gloss":"guven ile koruyucu dayanak","neighbor_only":"Koruyan engel, dayanak veya cevreden gelen himaye unsurudur.","neighbor_ref":"root_000071/B002","relation_type":"same_field","shared_zone":"Guvenli olma durumu koruma fikriyle ayni senaryoda bulusabilir."}],"source_phrase_ar":"الأمن ضد الخوف (ayn;sihah)؛ أصل الأمن طمأنينة النفس وزوال الخوف (mufradat)؛ الأمانة ضد الخيانة ومعناها سكون القلب (maqayis)؛ الأمان إعطاء الأمنة (maqayis;ayn)؛ أمن فلان يأمن أمنا وأمانا وأمنة فهو آمن (tahdhib)؛ استأمن إليه دخل في أمانه (sihah)؛ مأمنه منزله الذي فيه أمنه (mufradat)؛ الأمون الناقة الأمينة الوثيقة أو التي يؤمن فتورها وعثورها (ayn;sihah;mufradat)","source_summary":"Kaynaklar ortak olarak bu dali korkunun ziddi olan guven, kalbin yatismasi ve guven verme alaninda toplar. Ayni iddia guvenilir kisi, emanet, guvenli yer ve dayanilir binek gibi turemis ya da baglamli kullanislari da cekirdege baglar.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الأمن ضد الخوف، والأمان وإعطاء الأمنة، والأمانة ضد الخيانة وما اؤتمن عليه، والآمن والمأمن والاستئمان، والأمين والمأمون وما يوثق به، ومنه وثاقة الناقة الأمون.","what_is_not_ar":"ليس تصديق الإيمان من حيث هو تصديق، ولا صيغة آمين في الدعاء، ولا أمن المركبة من أم ومن في قوله أمن هو قانت."},"support_links":["sup_d6286bd3523f9c526fce"]},{"boundary":"Bu dal guvenlik hali degil; bir soz, haber, vaat veya hakikati dogru kabul etme alanidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000054/B002","candidate_links":[{"candidate_id":"cand_6f1a237e763c488b60b8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"ءَامَنَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:'aAmana|ROOT:Amn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"12:106:2:1","qac_word_ref":"12:106:2","surface_ar":"يُؤْمِنُ"}],"gloss":"dogru sayip kabul etme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel cekirdek bir haberin, sozun veya hakikatin dogru sayilmasidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Hakka yonelik ic kabul, yalniz bilmekten ziyade boyun egme ve kabullenme bicimi alir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dini alanlarda bu kabul, bildirilen yola girme ve ona baglanma adi olarak kullanilir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Ilahi sifat kullaniminda vaat edilen odulu dogrulama veya guvenceyle bildirme boyutu one cikar."}}],"root_ar":"ء م ن","root_id":"root_000054","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Haber, vaat, hakikat ve dini baglanma kullanimlarini tasdik cekirdegi etrafinda birlestirir.","boundary_detail":"Bu dal guvenlik hali degil; bir soz, haber, vaat veya hakikati dogru kabul etme alanidir.","branch_image_ar":"تصديق يطمئن إليه القلب","concept_gloss":"dogru sayip kabul etme","contextual_glosses":[{"applicability":"Haber veya sozun dogrulanmasi anlatildiginda en dogal karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dini boyun egme ve davranisla baglanma tarafini tam tasimaz.","preserves":"Tasdik cekirdegini korur."},"facet_ids":["F001"],"text":"dogru kabul etmek","usage_role":"contextual"},{"applicability":"Dini ve icten kabullenme baglamlarinda tasdikten daha genis sureci aciklar.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sade haber tasdiki icin fazla agir ve ozel kalir.","preserves":"Tasdikle birlikte ic kabul ve baglanma tarafini korur."},"facet_ids":["F002","F003"],"text":"hakka boyun egerek kabul etmek","usage_role":"explanatory"},{"applicability":"Vaat edilen seyin gercek ve guvenilir kilinmasi baglaminda kullanilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel tasdik ve dini kabullenme alanlarini kapsamaz.","preserves":"Vaatle ilgili dogrulama tarafini korur."},"facet_ids":["F004"],"text":"vaadini dogrulamak","usage_role":"contextual"}],"definition":"Bir haber, vaat veya hakikati dogru sayip ona icten kabul ile yonelmektir. Dini kullanista bu kabul, kalp, dil ve davranisla baglanan bir boyun egme ya da seriate girme anlami kazanabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel cekirdek bir haberin, sozun veya hakikatin dogru sayilmasidir."},{"facet_id":"F002","role":"specialization","statement":"Hakka yonelik ic kabul, yalniz bilmekten ziyade boyun egme ve kabullenme bicimi alir."},{"facet_id":"F003","role":"extension","statement":"Dini alanlarda bu kabul, bildirilen yola girme ve ona baglanma adi olarak kullanilir."},{"facet_id":"F004","role":"associated_use","statement":"Ilahi sifat kullaniminda vaat edilen odulu dogrulama veya guvenceyle bildirme boyutu one cikar."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Korkudan emin olma ve guvenli yer alanlarini ekler.","collision":"Ayni kokun guven daliyla karisir.","fit":"displacement","loses":"Tasdik, haberin dogru sayilmasi ve dini kabul cekirdegini kaybettirir.","preserves":"Kalbin yatismasiyla baglantili bir yan anlam kalabilir."},"text":"guvenlik"}],"identity_rationale":"Kaynak ifadeleri bu dali acikca tasdik, haber ya da vaadi dogru sayma ve bazi dini kullanislarda hakka boyun egme olarak verir. Provisional cerceve guvene dokunan yanini not eder, fakat dal kimligi korkusuzluk degil tasdik ve kabul iliskisidir.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ozellikle haber veya hakikati dogru kabul etme"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"herkese guvenen ve duydugunu dogru sayan kisi"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kuluna vaat ettigi odulu dogrulayan"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"bizi dogru sayan veya bize inanan"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"bildirilen dine girme ve onu kabul etme adi"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"hakka kalp, dil ve davranisla baglanarak dogru kabul etme"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"iyi amel anlaminda namaz veya ibadet"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"guven vermeyen batil seylere guven duymak diye yerilen tutum"}],"lexicalization_note":"Hem genel tasdik adlari hem de belirli soz obekleri ve dini kullanislar vardir; tanim bunlari yalin guven anlamina genisletmez.","neighbor_coverage_note":"Yayinlanan komsular tasdik, kesin kanaat, inkar ve guvenlik ayrimlarini netlestirir; kalan adaylar cevap, bildirme, yalan, aciklama veya uzak tematik baglar olarak daha az yararli bulundu.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Bu dal dogrulama ve kabullenme kutbunda, komsu dal ise hakikati reddetme veya ortme kutbundadir; bu nedenle ayni eksende karsit dururlar.","focus_only":"Haber, hakikat veya bildirilen yolu dogru sayip kabul eder.","gloss":"kabul ile inkar","neighbor_only":"Hakikati orter, inkar eder veya yalanlar.","neighbor_ref":"root_001307/B003","relation_type":"antonym","shared_zone":"Ikisi de hakikat, bildiri ve dogruluk karsisindaki tutumu adlandirir."},{"boundary_match":"partial","distinction":"Komsu dal kesinlik derecesini ve belirtiye dayali bilgiyi vurgular; bu dal ise kabul etme ve dogrulama eylemine odaklanir.","focus_only":"Bir haber veya hakikate kabul ve tasdikle yonelir.","gloss":"tasdik ile kesin kanaat","neighbor_only":"Belirtiye dayanarak kesin bilme veya kuvvetli kanaat alanindadir.","neighbor_ref":"root_000969/B001","relation_type":"near_neighbor","shared_zone":"Her ikisi de zihinsel kabul ve dogru sayma alanina yaklasir."},{"boundary_match":"partial","distinction":"Komsu dal kanaatin baglanmis ve sabit hale gelmesini anlatir; bu dal dogrulama ve kabul iliskisini esas alir.","focus_only":"Dogru sayma, haber ya da hakikati kabul etme eylemidir.","gloss":"tasdik ile yerlesik kanaat","neighbor_only":"Kalpte veya goruste karar kilma ve sabit kanaat olusturma alanidir.","neighbor_ref":"root_001034/B006","relation_type":"near_neighbor","shared_zone":"Ikisi de kalpte tutulan kabul veya gorusle ilgili olabilir."},{"boundary_match":"partial","distinction":"Bu dalda yatiskinlik dogru sayma ve kabullenmeden gelir; komsu dalda yatiskinlik korku ve tehlike ihtimalinin kalkmasindan gelir.","focus_only":"Tasdik, haberin veya hakikatin dogru kabul edilmesidir.","gloss":"tasdik ile guvenlik","neighbor_only":"Korkudan emin olma, guven verme ve emanet guvenilirligi alanidir.","neighbor_ref":"root_000054/B001","relation_type":"near_neighbor","shared_zone":"Kalbin yatismasi iki dalda da eslik edebilir."}],"source_phrase_ar":"الإيمان التصديق (ayn;sihah)؛ وما أنت بمؤمن لنا أي مصدق لنا (maqayis;ayn;mufradat)؛ إذعان النفس للحق على سبيل التصديق (mufradat)؛ المؤمن في صفات الله يصدق ما وعد عبده (maqayis)","source_summary":"Kaynaklar dalin ortak cekirdegini tasdik olarak verir ve bir sozun dogru sayilmasini temsil eden ornegi buna baglar. Ayni iddia, daha ozel dini kullanimlarda hakka icten boyun egme, yola girme ve vaatle ilgili dogrulama boyutlarinin eklendigini de gosterir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه الإيمان بمعنى التصديق، وتصديق الخبر أو الوعد، والإيمان على سبيل الشريعة أو إذعان النفس للحق حيث نصت المصادر، واستعمال مؤمن بمعنى مصدق الوعد.","what_is_not_ar":"ليس مجرد الأمن ضد الخوف، ولا الأمانة ضد الخيانة، ولا قول آمين في الدعاء، إلا حيث يصرح المصدر بأن التصديق معه أمن."},"support_links":["sup_d26586b0c72196ec6a72"]},{"boundary":"Bu dal guvenlik ya da tasdik degil; duada kabul talebini bildiren sabit sozdur.","branch_kind":"mixed_non_bare","branch_ref":"root_000054/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"ءَامَنَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:'aAmana|ROOT:Amn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"12:106:2:1","qac_word_ref":"12:106:2","surface_ar":"يُؤْمِنُ"}],"gloss":"duada kabul istegi sozu","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel cekirdek, duada kabul istegini bildiren sabit cevap sozudur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynaklar sozun anlamini 'kabul et', 'oyle olsun' veya 'bunu yap' seklinde aciklar."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu sozu soyleme eylemi de ayni dal icinde adlandirilir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bazi aktarimlarda bu sozun ilahi bir ad oldugu yorumu da dalin yan rivayeti olarak bulunur."}}],"root_ar":"ء م ن","root_id":"root_000054","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dua sonunda soylenen sabit kabul talebi ve onu soyleme eylemi icin genel karsiliktir.","boundary_detail":"Bu dal guvenlik ya da tasdik degil; duada kabul talebini bildiren sabit sozdur.","branch_image_ar":"قول آمين طلبا للاستجابة","concept_gloss":"duada kabul istegi sozu","contextual_glosses":[{"applicability":"Sozun dua icindeki anlamini eylemli bicimde cevirmek gerektiginde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sabit soz ve onu soyleme eylemi olma tarafini eksiltir.","preserves":"Duanin kabul edilmesini isteme tarafini korur."},"facet_ids":["F001","F002"],"text":"kabul et","usage_role":"contextual"},{"applicability":"Duanin sonucuna katilma ve gerceklesmesini dileme baglaminda dogal karsiliktir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ilahi muhataba yonelen talep kuvvetini ve sozu soyleme eylemini tam tasimaz.","preserves":"Kabul ve gerceklesme istegini korur."},"facet_ids":["F001","F002"],"text":"oyle olsun","usage_role":"contextual"},{"applicability":"Eylem adi olan kullanimda, yani bu sozu telaffuz etme anlatildiginda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sozun tek basina anlamini ve ad yorumu yanini kapsamaz.","preserves":"Sozu soyleme eylemini ve dua baglamini korur."},"facet_ids":["F003"],"text":"duada kabul sozu soylemek","usage_role":"explanatory"}],"definition":"Dua sonunda kabul edilme istegini bildiren ve 'kabul et', 'oyle olsun' ya da 'bunu yap' anlaminda aciklanan sabit sozdur. Dal ayrica bu sozu soyleme eylemini ve kaynaklarda aktarılan ad yorumunu da kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel cekirdek, duada kabul istegini bildiren sabit cevap sozudur."},{"facet_id":"F002","role":"source_variant","statement":"Kaynaklar sozun anlamini 'kabul et', 'oyle olsun' veya 'bunu yap' seklinde aciklar."},{"facet_id":"F003","role":"associated_use","statement":"Bu sozu soyleme eylemi de ayni dal icinde adlandirilir."},{"facet_id":"F004","role":"source_variant","statement":"Bazi aktarimlarda bu sozun ilahi bir ad oldugu yorumu da dalin yan rivayeti olarak bulunur."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Korkudan emin olma ve guvenilirlik alanlarini ekler.","collision":"Ayni kokun guven daliyla karisir.","fit":"displacement","loses":"Dua formulu, kabul talebi ve sozu soyleme eylemini kaybettirir.","preserves":"Ayni kokle bicimsel bag disinda anlam cekirdegi korumaz."},"text":"guven"},{"category":"confusable","error_profile":{"adds":"Tasdik ve dini kabul alanlarini ekler.","collision":"Ayni kokun tasdik daliyla karisir.","fit":"displacement","loses":"Dua icindeki sabit cevap sozunu ve kabul dilegini kaybettirir.","preserves":"Kabul fikrine cok dolayli temas edebilir."},"text":"inanma"}],"identity_rationale":"Kaynak ifadeleri bu dali dua icinde soylenen bir kabul istegi sozu ve bu sozu soyleme eylemi olarak verir. Cerceve, guven ve tasdik dallarindan ayrildigi ve sadece dua cevabi formuluyle ilgili oldugu icin uygundur.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"duada 'kabul et' veya 'oyle olsun' anlamina gelen soz"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"ilahi ad oldugu aktarilan dua sozu"},{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"duada kabul istegi bildiren sozu soyleme"}],"lexicalization_note":"Dal belirli bir dua sozu ve onu soyleme eylemiyle sinirlidir; buradan genel guven ya da tasdik anlami cikarilmaz.","neighbor_coverage_note":"Yayinlanan ayrimlar dua, dua cevabi, yalvarma ve ayni kokteki iki ayri dali kapsar; kalan adaylar ibadet, kehanet araci veya uzak dua sozleri olarak daha az dogrudan sinir bilgisi verdi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Komsu dal dua edenin duskun ve isteyen halini anlatir; bu dal ise duaya eklenen kabul dilegi sozunu adlandirir.","focus_only":"Dua sonunda soylenen sabit kabul istegi sozudur.","gloss":"cevap sozu ile yalvarma","neighbor_only":"Yalvarma, ihtiyac gostermek ve alttan yakarma halidir.","neighbor_ref":"root_000908/B002","relation_type":"same_field","shared_zone":"Ikisi de dua ve talep sahnesinde yer alabilir."},{"boundary_match":"field_only","distinction":"Komsu dal belirli sosyal durumda birine iyi dilek yoneltir; bu dal ise yapilmis duanin kabul edilmesi icin soylenen formulu anlatir.","focus_only":"Duanin kabul edilmesini isteyen sabit sozdur.","gloss":"kabul sozu ile hayir duası","neighbor_only":"Aksirana iyi dilekte bulunma ve ona hayir duasidir.","neighbor_ref":"root_000816/B003","relation_type":"same_field","shared_zone":"Ikisi de kisa dua veya dua cevabi soylemleri alanindadir."},{"boundary_match":"partial","distinction":"Komsu dal birden cok soz islevine yayilir; bu dal tekil olarak dua kabul istegi formulune baglidir.","focus_only":"Dua icinde kabul istegini bildiren belirli sozdur.","gloss":"dua onayi sozleri","neighbor_only":"Dua onayi, pekistirme ve kinama gibi daha daginik soz islevlerini kapsar.","neighbor_ref":"root_000118/B006","relation_type":"near_neighbor","shared_zone":"Ikisi de kisa sozlerle dua, onay veya pekistirme islevi gorebilir."},{"boundary_match":"field_only","distinction":"Bu dal sabit dua sozunu ve onu soylemeyi anlatir; komsu dal korkunun kalkmasi ve guvenilirlik iliskilerini anlatir.","focus_only":"Dua cevabi olarak kabul istegi bildiren sozdur.","gloss":"dua sozu ile guven","neighbor_only":"Guven, korkusuzluk, emanet ve guvenilirlik alanidir.","neighbor_ref":"root_000054/B001","relation_type":"other","shared_zone":"Ayni kok ailesinde yer alsalar da normal anlam alanlari ayridir."},{"boundary_match":"field_only","distinction":"Bu dal bir soylem formuludur; komsu dal bir haberin veya hakikatin dogrulanmasi ve benimsenmesidir.","focus_only":"Dua sonunda kabul istegi bildiren sozdur.","gloss":"dua sozu ile tasdik","neighbor_only":"Haber, vaat veya hakikati dogru sayip kabul etmektir.","neighbor_ref":"root_000054/B002","relation_type":"other","shared_zone":"Kabul fikri cok genel duzeyde ikisine de temas edebilir."}],"source_phrase_ar":"قولنا في الدعاء آمين وتفسيره اللهم افعل (maqayis)؛ التأمين من قولك آمين (ayn)؛ آمين في الدعاء يمد ويقصر ومعناه كذلك فليكن (sihah)؛ آمين يقال بالمد والقصر وهو اسم للفعل ومعناه استجب وأمن فلان إذا قال آمين (mufradat)","source_summary":"Kaynaklar ortak olarak dali dua icinde soylenen ve kabul istegi tasiyan sabit bir soz olarak anlatir. Ayni iddia, bu sozu soyleme eylemini ve sozun anlamina dair 'kabul et' ya da 'oyle olsun' aciklamalarini da icerir; ad yorumu ise bu ortak malzemenin yan aktarimidir.","sources":["MQ","AY","SI","MU"],"what_is_ar":"يدخل فيه آمين في الدعاء بالمد والقصر، والتأمين بمعنى قول آمين، وتفسيرها باستجب أو اللهم افعل أو كذلك فليكن، مع ذكر قول من جعلها اسما من أسماء الله.","what_is_not_ar":"ليس الأمن ضد الخوف، ولا الأمانة، ولا الإيمان بمعنى التصديق، ولا أمن التي هي أم من وليست من الباب."},"support_links":[]},{"boundary":"Anlam, insanlar arasındaki ortaklıkla sınırlıdır; dinsel ortak koşma, sandal kayışı, yol yapısı ve av kapanı bu dala girmez.","branch_kind":"bare","branch_ref":"root_000791/B001","candidate_links":[{"candidate_id":"cand_6f1a237e763c488b60b8","lane":"micro"},{"candidate_id":"cand_e7f07309c07dd908a75a","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُشْرِك","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mu$orik|ROOT:$rk|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:7:1","qac_word_ref":"12:106:7","surface_ar":"مُّشْرِكُونَ"}],"gloss":"ortaklık ve ortak olma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şey, hak veya iş en az iki taraf arasında ortaktır ve taraflardan yalnız birine ait değildir."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ortaklık, tarafların aynı mülkiyet veya anlam ilişkisi içinde birleşmesini ve birbirine katılmasını içerir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir kimse bir başkasını işe, satışa veya mirasa kendisiyle birlikte dahil ederek ortak yapabilir."}}],"root_ar":"ش ر ك","root_id":"root_000791","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin, hakkın veya işin iki ya da daha çok tarafça paylaşılması ve tarafların aynı ilişkiye katılması için kullanılır.","boundary_detail":"Anlam, insanlar arasındaki ortaklıkla sınırlıdır; dinsel ortak koşma, sandal kayışı, yol yapısı ve av kapanı bu dala girmez.","branch_image_ar":"الشَّرِكة والمشاركة","concept_gloss":"ortaklık ve ortak olma","contextual_glosses":[{"applicability":"Tarafların aynı şey veya iş üzerinde karşılıklı olarak ortak hale geldiği cümlelerde doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ortak şeyin taraflardan hiçbirine tek başına ait olmaması ayrıntısını açıkça söylemez.","preserves":"Tarafların aynı ilişkiye birlikte girmesi anlamını korur."},"facet_ids":["F001","F002"],"text":"birlikte ortak olmak","usage_role":"general"},{"applicability":"Bir tarafın başka bir kişiyi satış, miras veya benzeri bir işe kendisiyle birlikte dahil ettiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendiliğinden oluşan ortaklıkları ve genel ortak mülkiyet durumunu kapsamaz.","preserves":"Başka bir kişiyi mevcut ilişkiye ortak olarak katma işlemini korur."},"facet_ids":["F003"],"text":"birini işe ortak etmek","usage_role":"contextual"}],"definition":"Bir şeyin, hakkın ya da işin iki veya daha çok taraf arasında bulunması ve hiçbir tarafın onda tek başına olmamasıdır. Taraflardan biri diğerine katılabilir ya da onu aynı iş veya mülkiyet ilişkisine katabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şey, hak veya iş en az iki taraf arasında ortaktır ve taraflardan yalnız birine ait değildir."},{"facet_id":"F002","role":"core","statement":"Ortaklık, tarafların aynı mülkiyet veya anlam ilişkisi içinde birleşmesini ve birbirine katılmasını içerir."},{"facet_id":"F003","role":"specialization","statement":"Bir kimse bir başkasını işe, satışa veya mirasa kendisiyle birlikte dahil ederek ortak yapabilir."}],"identity_rationale":"Kaynak ifadesi, bir şeyin iki ya da daha çok kişi arasında bulunmasını, tarafların birbirine karışmasını ve bir kişinin bir işe başkasıyla birlikte girmesini aynı ortaklık çekirdeğinde birleştirir. Bu nedenle dalın ortak olma ve ortaklaşa sahiplik çerçevesi kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ortaklık ve ortak olma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ortak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"ortak olmak veya birini ortak etmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"karşılıklı olarak ortaklaşmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"herkesin ortak olduğu veya eşit yararlandığı şey"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ortaklık payı"}],"lexicalization_note":"Dal yalın anlamı temsil eder; tanım, belirli bir kalıba bağlı özel kullanımları bu genel ortaklık anlamına katmaz.","neighbor_coverage_note":"Sağlanan bütün komşu adayları karşılaştırıldı; yalnız ortaklığın sınırını bölünmemiş paydan ve daha geniş karışma alanından ayıran iki aday yayımlandı, diğerleri farklı alanlarda kaldığı için ek açıklık sağlamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dal genel ortak olma ilişkisini ve katılma işlemini anlatır; komşu dal ise bölüşülmemiş mülkiyet payını daha dar bir hukuki durum olarak öne çıkarır.","focus_only":"İş veya anlam ortaklığı ile birini ortak bir ilişkiye katmayı da kapsar.","gloss":"ortaklık ile bölünmemiş ortak pay","neighbor_only":"Özellikle bölünmemiş taşınmaz mülkiyetindeki paya odaklanır.","neighbor_ref":"root_000836/B004","relation_type":"near_synonym","shared_zone":"Her iki dal da bir malın birden çok kişiye ortaklaşa ait olabildiği alanı kapsar."},{"boundary_match":"partial","distinction":"Odak dalında ortak hak veya katılım belirleyicidir; komşu dalda ise karışma ve birlikte bulunma, ortak hak doğurmayan durumlara kadar genişleyebilir.","focus_only":"Bir şeyin taraflar arasında ortak olması ve birinin diğerini ortaklığa alması çekirdektir.","gloss":"ortaklık ile karışıp birleşme","neighbor_only":"İnsanların karışması, komşuluk ve hayvanlara ilişkin özel hukuki karışım alanlarını da içerir.","neighbor_ref":"root_000431/B002","relation_type":"near_synonym","shared_zone":"İki dal, kişilerin veya malların ortak bir ilişki içinde birleşmesi bakımından örtüşür."}],"source_phrase_ar":"الشركة أن يكون الشيء بين اثنين لا ينفرد به أحدهما (maqayis)؛ الشركة مخالطة الشريكين (ayn;tahdhib)؛ شاركت فلانا صرت شريكه (sihah)؛ شركه في الأمر إذا دخل معه فيه (tahdhib)؛ خلط الملكين أو شيء لاثنين فصاعدا (mufradat)","source_summary":"Kaynakların ortak çekirdeği, bir şeyin birden çok taraf arasında bulunması, tarafların ortak hale gelmesi ve birinin diğerini aynı ilişkiye katmasıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه كون الشيء بين اثنين فأكثر؛ مخالطة الشريكين؛ إدخال غيره معه في أمر أو بيع أو ميراث؛ النصيب المشترك؛ اشتراك الناس في مورد أو فريضة","what_is_not_ar":"ليس هو إثبات شريك لله؛ ولا شراك النعل؛ ولا شرك الطريق؛ ولا حبالة الصائد"},"support_links":["sup_d26586b0c72196ec6a72","sup_d6286bd3523f9c526fce"]},{"boundary":"Dal, Tanrı'ya ortak tanıma anlamındadır; insanlar arasındaki ortaklık ve aynı kökün nesne adları bu dinsel anlama dahil değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000791/B002","candidate_links":[{"candidate_id":"cand_6f1a237e763c488b60b8","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُشْرِك","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mu$orik|ROOT:$rk|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:7:1","qac_word_ref":"12:106:7","surface_ar":"مُّشْرِكُونَ"}],"gloss":"Tanrı'ya ortak koşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Başka bir varlık, yalnız Tanrı'ya ait kabul edilen yetki veya nitelikte ona ortak sayılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu ortak sayma, dinsel değerlendirmede ağır bir yanlış ve inançtan ayrılma olarak adlandırılır."}}],"root_ar":"ش ر ك","root_id":"root_000791","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız Tanrı'ya ait sayılan yetki veya nitelikte başka bir varlığı ona ortak ya da denk kabul etme anlamının tamamını karşılar.","boundary_detail":"Dal, Tanrı'ya ortak tanıma anlamındadır; insanlar arasındaki ortaklık ve aynı kökün nesne adları bu dinsel anlama dahil değildir.","branch_image_ar":"الشِّرك بالله","concept_gloss":"Tanrı'ya ortak koşma","contextual_glosses":[{"applicability":"Bir kişinin başka bir varlığı Tanrı'nın yetki veya niteliğine ortak kabul ettiği cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Başka bir varlığı Tanrı'ya ortak sayma işlemini açık biçimde korur."},"facet_ids":["F001"],"text":"Tanrı'ya ortak tanımak","usage_role":"general"},{"applicability":"Eylemin dinsel hükmünün ağır yanlış ve inançtan ayrılma olarak vurgulandığı açıklayıcı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hem ortak koşma eylemini hem de ona bağlanan dinsel değerlendirmeyi korur."},"facet_ids":["F001","F002"],"text":"inançtan ayrılma sayılan ortak koşma","usage_role":"explanatory"}],"definition":"Dinsel kullanımda Tanrı'nın tek olması gereken yetki ve niteliğinde başka bir varlığı ona ortak saymak veya onunla denk tutmaktır. Bu eylem ağır bir yanlış ve inançtan ayrılma olarak nitelenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Başka bir varlık, yalnız Tanrı'ya ait kabul edilen yetki veya nitelikte ona ortak sayılır."},{"facet_id":"F002","role":"associated_use","statement":"Bu ortak sayma, dinsel değerlendirmede ağır bir yanlış ve inançtan ayrılma olarak adlandırılır."}],"identity_rationale":"Kaynak ifadesi, Tanrı'ya yönetme ve yaratılmışlar üzerindeki yetkisinde bir ortak tanımayı bu dinsel anlamın kurucu işlemi olarak verir; ağır yanlış ve inançsızlık nitelemeleri bu çekirdeğin değerlendirmeleridir. Dalın dinsel ortak koşma kimliği bu sınır içinde doğrudur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"Tanrı'ya ortak koşma"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"Tanrı'ya ortak koşmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"Tanrı'ya ortak koşan kimse"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"büyük ve küçük ortak koşma türleri"}],"lexicalization_note":"Dal hem dinsel eylemin adı olan kullanımı hem de Tanrı'yı açıkça tümleyen kalıpları içerir; tanım bu iki görünümü ayırır ve genel ortaklığa yayılmaz.","neighbor_coverage_note":"Bütün adaylar denetlendi; karşıt tek Tanrı inancı ile daha geniş inanç reddi alanı sınırı doğrudan aydınlattığı için yayımlandı, öteki adaylar ya yalnız tematik kaldı ya da bu ayrımları yineledi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Odak dalı bu eksende ortaklığı kabul eden kutuptur; komşu dal Tanrı'nın ortak kabul etmeyen tekliğini bildiren karşıt kutuptur.","focus_only":"Tanrı'ya başka bir varlığı ortak veya denk sayar.","gloss":"ortak koşma ile Tanrı'nın tekliği","neighbor_only":"Tanrı'nın tekliğini bildirir ve her türlü ortaklığı ondan uzak tutar.","neighbor_ref":"root_001631/B004","relation_type":"antonym","shared_zone":"İki dal da Tanrı'nın tekliği ve ona ortak bulunup bulunmadığı ekseninde yer alır."},{"boundary_match":"partial","distinction":"Odak dalı belirli bir ortak tanıma eylemidir; komşu dal bunun yanında ortak tanımayı gerektirmeyen başka inkâr ve karşı çıkma biçimlerini de içerir.","focus_only":"İnançtan ayrılmayı özellikle Tanrı'ya ortak tanıma işlemiyle sınırlar.","gloss":"ortak koşma ile inancı inkâr","neighbor_only":"Gerçeği örtme, inkâr, karşı gelme ve farklı inanç reddi biçimlerini de kapsar.","neighbor_ref":"root_001307/B003","relation_type":"near_synonym","shared_zone":"Tanrı'ya ortak koşma, daha geniş inanç reddi alanının içinde değerlendirilebilir."}],"source_phrase_ar":"الشرك ظلم عظيم (ayn)؛ الشرك أيضا الكفر (sihah)؛ أن تجعل لله شريكا في ربوبيته (tahdhib)؛ إثبات شريك لله تعالى (mufradat)","source_summary":"Ortak içerik, Tanrı'ya bir ortak tanımak veya başka bir varlığı onunla denk tutmaktır; ağır yanlış ve inançsızlık nitelemeleri bu eyleme bağlanır.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه جعل شريك لله؛ العدل به غيره؛ الكفر المسمى شركا؛ الشرك العظيم والصغير في الدين","what_is_not_ar":"ليس هو مطلق الشركة بين الناس؛ ولا المصاهرة؛ ولا الحبالة"},"support_links":["sup_d26586b0c72196ec6a72"]},{"boundary":"Kullanım eşlik ve evlilik yoluyla hısımlığa bağlıdır; sırf yakınlık, komşuluk veya mal ortaklığı bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000791/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُشْرِك","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mu$orik|ROOT:$rk|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:7:1","qac_word_ref":"12:106:7","surface_ar":"مُّشْرِكُونَ"}],"gloss":"eş veya evlilik yoluyla hısım","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişinin eşi, evlilik ilişkisi bakımından onun ortağı diye adlandırılır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Birinin kızı veya kız kardeşiyle evlenen erkek, o kişiyle evlilik yoluyla hısım olan ortak diye anılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir söz kalıbı, karşı taraftan evlilik yoluyla hısımlık istemeyi bildirir."}}],"root_ar":"ش ر ك","root_id":"root_000791","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ortaklık bildiren sözün eşe ya da bir evlilik nedeniyle hısım olan kişiye özel ad olarak yöneltildiği tarihsel kullanım alanını karşılar.","boundary_detail":"Kullanım eşlik ve evlilik yoluyla hısımlığa bağlıdır; sırf yakınlık, komşuluk veya mal ortaklığı bu dala girmez.","branch_image_ar":"شِرك المصاهرة","concept_gloss":"eş veya evlilik yoluyla hısım","contextual_glosses":[{"applicability":"Söz doğrudan bir erkeğin karısını veya evlilikteki taraflardan birini gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Evlilik yoluyla kurulan daha geniş hısımlık kullanımını kapsamaz.","preserves":"Evlilikteki eşlik ilişkisini doğal ve kısa biçimde korur."},"facet_ids":["F001"],"text":"eş","usage_role":"contextual"},{"applicability":"Bir aileyle evlenme üzerinden hısımlık kurma veya böyle bir ilişki isteme bağlamlarında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Eşin doğrudan ortak diye adlandırılması kullanımını içermez.","preserves":"Evliliğin iki taraf arasında hısımlık kurması anlamını korur."},"facet_ids":["F002","F003"],"text":"evlilik yoluyla hısım olmak","usage_role":"contextual"}],"definition":"Bir kişiyi eş olarak veya birinin kızı ya da kız kardeşiyle evlenme sonucu oluşan hısımlık ilişkisi içinde ortak diye adlandıran özel kullanımdır. Ayrıca bir aileden evlilik yoluyla hısımlık isteme kalıbında görülür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişinin eşi, evlilik ilişkisi bakımından onun ortağı diye adlandırılır."},{"facet_id":"F002","role":"extension","statement":"Birinin kızı veya kız kardeşiyle evlenen erkek, o kişiyle evlilik yoluyla hısım olan ortak diye anılır."},{"facet_id":"F003","role":"associated_use","statement":"Belirli bir söz kalıbı, karşı taraftan evlilik yoluyla hısımlık istemeyi bildirir."}],"identity_rationale":"Kaynak ifadesi, sözcüğün eş için ve iki erkek arasında kız ya da kız kardeşle evlenme yoluyla kurulan hısımlık için kullanılmasını doğrular. Geçici çerçevedeki yakın komşuluk ise yetkili ifadede bulunmadığından dal yalnız evlilik ve evlilikten doğan hısımlıkla sınırlandırılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"eş veya evlilik yoluyla hısım"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"sizinle evlilik yoluyla hısım olmak istedik"}],"lexicalization_note":"Dal, eş veya evlilik hısmı bildiren adlandırmalarla hısımlık isteme kalıbını birlikte taşır; bunlar yalın ortaklık anlamına genellenmez.","neighbor_coverage_note":"Tüm adaylar karşılaştırıldı; genel eş adı ve daha geniş evlilik hısımlığı alanı bu özel kullanımın iki temel sınırını gösterdi, kalan adaylar aynı alanı daha uzaktan paylaştığı için yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal, ortaklık söz varlığının eş ve evlilik hısmı için özel kullanımını verir; komşu dal ise eş kavramının genel ve doğrudan adlandırmasıdır.","focus_only":"Eş adının yanında, kız veya kız kardeşle evlenme sonucu oluşan erkekler arası hısımlığı da kapsar.","gloss":"özel ortak adı ile genel eş adı","neighbor_only":"Evlilik sözleşmesindeki kadın ve erkeği doğrudan eş olarak adlandıran genel alandır.","neighbor_ref":"root_000652/B002","relation_type":"near_synonym","shared_zone":"Her iki dalda kadın ve erkek arasındaki evlilik ilişkisi temel ortak alandır."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği ortak sözünün eşe veya belirli bir evlilik hısmına aktarılmasıdır; komşu dal ortaklık çağrışımı taşımadan hısımlık sınıfını adlandırır.","focus_only":"Eşi ve belirli evlilik bağlantısıyla oluşan ortağı adlandırır.","gloss":"evlilik ortağı ile evlilik hısmı","neighbor_only":"Kadın veya erkek tarafındaki daha geniş evlilik hısımları ve onların genel adlarını kapsar.","neighbor_ref":"root_000394/B002","relation_type":"near_neighbor","shared_zone":"İki dal da evliliğin kişiler ve aileler arasında kurduğu hısımlık alanındadır."}],"source_phrase_ar":"في المصاهرة رغبنا في شرككم وصهركم (ayn;tahdhib)؛ فلان شريك فلان إذا تزوج بابنته أو بأخته (tahdhib)؛ امرأة الرجل شريكته (tahdhib)","source_summary":"Kaynak ifadesi, eşin ortak diye adlandırılmasını ve bir kız ya da kız kardeşle evlilik üzerinden iki taraf arasında hısımlık kurulmasını aynı özel kullanım alanında toplar.","sources":["AY","TA"],"what_is_ar":"يدخل فيه إطلاق الشريك والشريكة على جهة المصاهرة والزوجية والجوار القريب","what_is_not_ar":"ليس هو الشركة في مال أو ميراث؛ ولا الشرك بالله"},"support_links":[]},{"boundary":"Dal sandal kayışı ve sandala bu kayışı takmakla sınırlıdır; her türlü sandal onarımı veya genel deri kayışı anlamına gelmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000791/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُشْرِك","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mu$orik|ROOT:$rk|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:7:1","qac_word_ref":"12:106:7","surface_ar":"مُّشْرِكُونَ"}],"gloss":"sandal kayışı ve sandala kayış takma","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Nesne, sandalı ayağa bağlamaya yarayan kayıştır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İlgili eylem, sandala bu kayışı yapmak veya takmak anlamına gelir."}}],"root_ar":"ش ر ك","root_id":"root_000791","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem sandalın ayağı tutan parçasını hem de bu parçayı sandala yerleştirme eylemini birlikte temsil eden açıklayıcı karşılıktır.","boundary_detail":"Dal sandal kayışı ve sandala bu kayışı takmakla sınırlıdır; her türlü sandal onarımı veya genel deri kayışı anlamına gelmez.","branch_image_ar":"شِراك النعل","concept_gloss":"sandal kayışı ve sandala kayış takma","contextual_glosses":[{"applicability":"Söz bir nesne olarak sandalın ayağı tutan deri veya benzeri kayışını gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sandala kayış takma eylemini kapsamaz.","preserves":"Nesnenin sandal üzerindeki bağlama parçası olmasını korur."},"facet_ids":["F001"],"text":"sandal kayışı","usage_role":"contextual"},{"applicability":"Söz sandala bağlama kayışı yapma veya yerleştirme eylemini bildirdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kayışın bağımsız nesne adı olarak kullanımını kapsamaz.","preserves":"Kayışı sandala yerleştirme işlemini ve nesnenin işlevini korur."},"facet_ids":["F002"],"text":"sandala kayış takmak","usage_role":"contextual"}],"definition":"Sandalı ayağa bağlayan kayış ve sandala bu işlevde bir kayış takma eylemidir. Eylem, genel bir onarımı değil bu parçayı yapma veya yerleştirme işlemini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Nesne, sandalı ayağa bağlamaya yarayan kayıştır."},{"facet_id":"F002","role":"associated_use","statement":"İlgili eylem, sandala bu kayışı yapmak veya takmak anlamına gelir."}],"identity_rationale":"Kaynak ifadesi hem sandalın ayağa tutunmasını sağlayan kayışı hem de sandala böyle bir kayış takma eylemini açıkça destekler. Geçici çerçevedeki genel onarım anlamı ise kaynakta bağımsız bir işlem değildir; yalnız kayış takarak yapılan iş olarak anlaşılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"sandal kayışı"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"sandala kayış takmak"}],"lexicalization_note":"Dal nesne adını ve sandala kayış takma yapısını birlikte içerir; bu özel ayakkabı bağı yalın kökün genel anlamı olarak sunulmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; genel deri kayış alanı bu dalın sandal işlevine bağlı sınırını doğrudan gösterdi, diğer bağlama ve dikme adayları yalnız araç veya iş alanını paylaştığından ek bir ayrım yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kullanım yerini sandalla sınırlar ve kayışı takma eylemini de içerir; komşu dal ise kayışın malzeme ve biçim sınıfını daha genel verir.","focus_only":"Kayışın sandalı ayağa bağlama işlevini ve sandala takılması eylemini belirtir.","gloss":"sandal kayışı ile genel deri kayış","neighbor_only":"Deri şerit ve kayışları kullanım yerinden bağımsız daha geniş bir nesne sınıfı olarak kapsar.","neighbor_ref":"root_000769/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda da uzun ve dar bir deri kayış nesnesi bulunabilir."}],"source_phrase_ar":"شراك النعل مشبه بهذا (maqayis)؛ الشراك سير النعل (ayn;tahdhib)؛ أشركت نعلي جعلت لها شراكا (sihah)؛ شركت النعل وأشركتها إذا جعلت لها شراكا (tahdhib)","source_summary":"Ortak kanıt, sandalın bağlama kayışını nesne olarak tanımlar ve aynı söz ailesindeki eylemi sandala bu kayışı takmakla sınırlar.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه سير النعل وجعل الشراك للنعل وإصلاحه","what_is_not_ar":"ليس هو الطريق؛ ولا حبالة الصائد؛ ولا الشركة بين اثنين"},"support_links":[]},{"boundary":"Dal, yolun ana yatağı, izleri ve küçük kolları gibi yapısal bölümlerle sınırlıdır; her tür yol veya otlakta bulunan her patika bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000791/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُشْرِك","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mu$orik|ROOT:$rk|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:7:1","qac_word_ref":"12:106:7","surface_ar":"مُّشْرِكُونَ"}],"gloss":"yolun ana yatağı, izleri ve küçük kolları","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz, yolun belirgin oluklarını, geniş izlerini veya geçiş şeritlerini adlandırabilir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı anlatımlarda yolun ana, büyük veya orta bölümü öne çıkar."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ana yoldan ayrılıp bir süre sonra sona eren küçük yol kolları da aynı ad ailesiyle ifade edilir."}}],"root_ar":"ش ر ك","root_id":"root_000791","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yolun kendisinden çok ana kesimi, üzerindeki belirgin geçiş izleri ve ondan ayrılan küçük yolları birlikte açıklamak için uygundur.","boundary_detail":"Dal, yolun ana yatağı, izleri ve küçük kolları gibi yapısal bölümlerle sınırlıdır; her tür yol veya otlakta bulunan her patika bu dala girmez.","branch_image_ar":"شِرك الطريق","concept_gloss":"yolun ana yatağı, izleri ve küçük kolları","contextual_glosses":[{"applicability":"Söz yolun büyük ya da orta bölümünü veya bu bölümdeki belirgin oluk ve şeritleri gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ana yoldan ayrılan küçük kolları kapsamaz.","preserves":"Yolun ana kesimi ile belirgin yüzey izlerini korur."},"facet_ids":["F001","F002"],"text":"yolun ana yatağı ve izleri","usage_role":"contextual"},{"applicability":"Söz ana yolun küçük, dallanan ve sonunda kesilebilen kollarını gösterdiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ana yolun kendisini, orta kesimini ve yüzey oluklarını kapsamaz.","preserves":"Ana yoldan ayrılan küçük kol yollarını açık biçimde korur."},"facet_ids":["F003"],"text":"ana yoldan ayrılan küçük yollar","usage_role":"contextual"}],"definition":"Bir yolun ana veya orta kesimini, belirgin oluk ve geniş izlerini ve ana yoldan ayrılan küçük kollarını adlandıran yol yapısı anlamıdır. Kaynak anlatımları tek bir geometrik parçadan çok bu bağlantılı yol bölümleri arasında değişir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz, yolun belirgin oluklarını, geniş izlerini veya geçiş şeritlerini adlandırabilir."},{"facet_id":"F002","role":"source_variant","statement":"Bazı anlatımlarda yolun ana, büyük veya orta bölümü öne çıkar."},{"facet_id":"F003","role":"extension","statement":"Ana yoldan ayrılıp bir süre sonra sona eren küçük yol kolları da aynı ad ailesiyle ifade edilir."}],"identity_rationale":"Kaynak ifadesi aynı yol söz varlığı altında yolun belirgin izlerini veya geniş şeritlerini, ana ya da orta bölümünü ve ondan ayrılan küçük kolları bir araya getirir. Geçici çerçevedeki otlak yolları yalnız ayrı bir sözcük biriminde bulunur ve dal iddiasını belirlemediği için ana tanımdan çıkarılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"yolun ana yatağı, ortası veya izleri"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"ana yoldan ayrılan küçük yollar"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"otlağın yollar veya izler halinde uzanması"}],"lexicalization_note":"Dal, yol bağlamına bağlı adları ve özel yol bölümü kullanımlarını içerir; bunlar yalın kökün bağımsız genel anlamı olarak birleştirilmez.","neighbor_coverage_note":"Tüm yol ve kök içi adaylar değerlendirildi; yol izleriyle en yakın örtüşen dal ve yolun bütününü anlatan dal yayımlandı, kalan adaylar yalnız genel güzergâh veya uzak yüzey özellikleri sundu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal izlerden ana yol kesimine ve küçük kollara uzanan daha geniş bir yapısal kümeyi taşır; komşu dalın ortak bölgesi daha çok yol ve yol izleridir.","focus_only":"Yolun ana veya orta kesimini ve ondan ayrılan küçük kolları da adlandırır.","gloss":"yol bölümleri ile yol izleri","neighbor_only":"Yol sözüyle birlikte özellikle yolun iz ve oluklarını başka bir ad altında öne çıkarır.","neighbor_ref":"root_000395/B006","relation_type":"near_synonym","shared_zone":"Her iki dal yolun görünür izlerini ve oluklarını adlandırma alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dal yolun iç yapısını ve kollarını gösterir; komşu dal ise yolun kendisini, özellikle açık ve amaçlanan güzergâhı gösterir.","focus_only":"Yolun ana yatağındaki izleri, orta bölümünü ve küçük dallarını bölüm olarak adlandırır.","gloss":"yolun bölümleri ile yolun bütünü","neighbor_only":"Gidilmek istenen açık veya belirgin yolu bütün olarak adlandırır.","neighbor_ref":"root_000295/B002","relation_type":"near_neighbor","shared_zone":"İki dal da belirgin ve yürünebilir bir yol alanına ilişkindir."}],"source_phrase_ar":"الشرك لقم الطريق وهو شراكه (maqayis)؛ الشرك أخاديد الطريق الواضح (ayn)؛ الشركة معظم الطريق ووسطه (sihah)؛ شرك الطريق أنساع الطريق (tahdhib)؛ أم الطريق معظمه وبنياته أشراك صغار (tahdhib)","source_summary":"Toplu kaynak ifadesi yolun oluk ve şeritleri, ana ya da orta bölümü ve bu ana bölümden ayrılan küçük kollar arasında değişen, fakat yolun yapısına bağlı bir anlam alanı gösterir.","sources":["MQ","AY","SI","TA"],"what_is_ar":"يدخل فيه لقم الطريق وشراكه؛ أخاديد الطريق؛ أنساع الطريق؛ معظمه وبنياته؛ طرائق الكلإ","what_is_not_ar":"ليس هو شراك النعل؛ ولا حبالة الصائد؛ ولا الشركة في ملك"},"support_links":[]},{"boundary":"Çekirdek, avın yakalandığı bağ veya ağ biçimli kapan; genişleme ise bunun tuzak anlamındaki benzetmesidir. Belirli bir av türü zorunlu değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_000791/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُشْرِك","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mu$orik|ROOT:$rk|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:7:1","qac_word_ref":"12:106:7","surface_ar":"مُّشْرِكُونَ"}],"gloss":"avın dolandığı kapan ve tuzak benzetmesi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Avcı, avın içine dolanıp yakalandığı bağ veya ağ biçimli bir kapan kurar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Fiziksel kapan görüntüsü, insanı yakalayıp kendine bağlayan dünya için benzetmeli olarak kullanılır."}}],"root_ar":"ش ر ك","root_id":"root_000791","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Fiziksel av kapanını ve bu kapanın insanı kendine çeken bir şeye benzetilmesini birlikte temsil eden açıklayıcı karşılıktır.","boundary_detail":"Çekirdek, avın yakalandığı bağ veya ağ biçimli kapan; genişleme ise bunun tuzak anlamındaki benzetmesidir. Belirli bir av türü zorunlu değildir.","branch_image_ar":"شَرَك الصائد","concept_gloss":"avın dolandığı kapan ve tuzak benzetmesi","contextual_glosses":[{"applicability":"Söz, avcının kurduğu ve avın içine dolanarak yakalandığı fiziksel aracı gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Dünya için kullanılan benzetmeli tuzak anlamını kapsamaz.","preserves":"Avcının kurduğu yakalama aracını ve avın yakalanma sonucunu korur."},"facet_ids":["F001"],"text":"av kapanı","usage_role":"contextual"},{"applicability":"Fiziksel kapanın yakalayıcı niteliği dünyaya veya dünya hayatına benzetme yoluyla aktarıldığında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gerçek av aracının biçimini ve avcılık bağlamını doğrudan karşılamaz.","preserves":"Bir şeyin insanı yakalayıp kendine bağlaması yönündeki benzetmeyi korur."},"facet_ids":["F002"],"text":"dünyanın tuzağı","usage_role":"contextual"}],"definition":"Avcının kurduğu, avın içine dolanarak veya takılarak kurtulamadığı bağ ya da ağ biçimli kapandır. Aynı yakalama görüntüsü, insanı içine çeken dünya tuzağı için benzetme yoluyla kullanılabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Avcı, avın içine dolanıp yakalandığı bağ veya ağ biçimli bir kapan kurar."},{"facet_id":"F002","role":"extension","statement":"Fiziksel kapan görüntüsü, insanı yakalayıp kendine bağlayan dünya için benzetmeli olarak kullanılır."}],"identity_rationale":"Kaynak ifadesi avın içine dolanıp kaldığı avcı kapanını açıkça tanımlar ve dünya için kurulan tuzak benzetmesini buna bağlar. Geçici çerçevedeki belirli bir kuş için kurulma ayrıntısı yetkili dal ifadesinde bulunmadığından tanıma alınmamıştır.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"avın dolandığı av kapanı"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"tek bir av kapanı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"dünyanın tuzağı"}],"lexicalization_note":"Dal avcı kapanının adını ve bu nesneden türeyen dünya tuzağı kullanımını ayırır; mecaz fiziksel kapanın kurucu tanımına dönüştürülmez.","neighbor_coverage_note":"Bütün kapan, avlanma ve kök içi adaylar incelendi; en yakın genel kapan alanları sınır karşılaştırması için seçildi, yalnız avlanma aracını veya yakalanma olayını uzaktan paylaşan adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dolanma biçimli belirli kapan görüntüsüne bağlıdır; komşu dal araç, avlanma ve benzetmeli kullanım bakımından daha geniştir.","focus_only":"Avın içine dolandığı bağ veya ağ biçimli kapanı ve dünya tuzağı benzetmesini taşır.","gloss":"özel av ağı ile genel av kapanı","neighbor_only":"Av kapanlarının daha geniş sınıfını, avlanma eylemini ve ölüm ya da kötülük nedenlerine uzanan başka benzetmeleri kapsar.","neighbor_ref":"root_000291/B005","relation_type":"near_synonym","shared_zone":"Her iki dal avcının kurduğu ve avı yakalayan kapan alanında doğrudan örtüşür."},{"boundary_match":"partial","distinction":"Odak dalda avın bağlara dolanması belirgindir ve mecaz dünyaya uzanır; komşu dal daha genel kurulmuş kapan kavramında kalır.","focus_only":"Dolanma veya takılma yoluyla yakalayan bağ ya da ağ yapısını ve dünya benzetmesini belirtir.","gloss":"dolanmalı av kapanı ile genel tuzak","neighbor_only":"Av için kurulmuş kapanı biçimini ayrıntılandırmadan genel bir tuzak olarak adlandırır.","neighbor_ref":"root_000932/B013","relation_type":"near_synonym","shared_zone":"İki dal da avı yakalamak üzere önceden kurulan bir kapanı gösterir."}],"source_phrase_ar":"شرك الصائد سمي بذلك لامتداده (maqayis)؛ الشرك حبالة يرتبك فيها الصيد (ayn)؛ الشرك بالتحريك حبالة الصائد (sihah)؛ شرك الصائد حبالته يرتبك فيها الصيد (tahdhib)؛ شرك الدنيا أي حبالتها (mufradat)","source_summary":"Ortak çekirdek, avın dolanarak yakalandığı avcı kapanıdır; toplu ifade ayrıca bu kapan görüntüsünün dünyaya ilişkin tuzak benzetmesine genişlediğini gösterir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه حبالة الصائد التي يرتبك فيها الصيد؛ وما ينصب للحمام؛ الاستعمال المجازي للحبالة","what_is_not_ar":"ليس هو شراك النعل؛ ولا شرك الطريق؛ ولا الشرك بالله إلا من جهة المجاز المذكور"},"support_links":[]},{"boundary":"Anlam yalnız belirtilen tokatlama ve geliş sırası kullanımlarında art ardalığı bildirir; yalın ve genel bir süreklilik sözü olarak genişletilmez.","branch_kind":"non_bare","branch_ref":"root_000791/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُشْرِك","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mu$orik|ROOT:$rk|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:7:1","qac_word_ref":"12:106:7","surface_ar":"مُّشْرِكُونَ"}],"gloss":"özel yapılarda hızlı ve art arda oluş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Benzer olaylar biri diğerinin ardından art arda gerçekleşir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tokatlama bağlamında vuruşların peş peşe gelmesine hızlılık niteliği de eklenir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Başka bir özel kullanımda bir suya gelişin ardından yeni bir gelişin gelmesi anlatılır."}}],"root_ar":"ش ر ك","root_id":"root_000791","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Peş peşe tokatları ve birbiri ardından gerçekleşen gelişleri ortak ardışıklık niteliği altında açıklamak için kullanılır.","boundary_detail":"Anlam yalnız belirtilen tokatlama ve geliş sırası kullanımlarında art ardalığı bildirir; yalın ve genel bir süreklilik sözü olarak genişletilmez.","branch_image_ar":"تتابع شَرْكي","concept_gloss":"özel yapılarda hızlı ve art arda oluş","contextual_glosses":[{"applicability":"Tokatların kısa aralıklarla peş peşe geldiği özel vuruş nitelemesinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir gelişin ardından başka gelişin olması kullanımını kapsamaz.","preserves":"Tokatların hızlı ve peş peşe gelmesini tam olarak korur."},"facet_ids":["F001","F002"],"text":"hızlı ve art arda tokatlamak","usage_role":"contextual"},{"applicability":"Bir suya gelişin ardından başka bir gelişin gerçekleştiği sıra bağlamında uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tokatlama bağlamını ve oradaki hızlılık niteliğini kapsamaz.","preserves":"Olayların biri diğerini izleyerek art arda gerçekleşmesini korur."},"facet_ids":["F001","F003"],"text":"birbiri ardından gelmek","usage_role":"contextual"}],"definition":"Belirli niteleme yapılarında bir vuruşun veya gelişin ardından benzerinin peş peşe gelmesini anlatır. Tokatlarda hızlılık da bu ardışıklığa eşlik eder.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Benzer olaylar biri diğerinin ardından art arda gerçekleşir."},{"facet_id":"F002","role":"specialization","statement":"Tokatlama bağlamında vuruşların peş peşe gelmesine hızlılık niteliği de eklenir."},{"facet_id":"F003","role":"example","statement":"Başka bir özel kullanımda bir suya gelişin ardından yeni bir gelişin gelmesi anlatılır."}],"identity_rationale":"Kaynak ifadesi iki özel yapıda aynı ardışıklık niteliğini verir: hızlı ve peş peşe gelen tokatlar ile bir gelişin ardından gelen başka geliş. Dalın art arda oluş kimliği, bu yapılara bağlı tutulduğu sürece kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"hızlı ve art arda tokatlar"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"suya birbiri ardından geliş"}],"lexicalization_note":"Dal yalnız belirli niteleme yapılarında tanıklanmıştır; tanım art ardalık çekirdeğini korurken onu yalın kökün bağımsız anlamı saymaz.","neighbor_coverage_note":"Bütün ardışıklık adayları ve kök içi dallar değerlendirildi; genel kesintisiz sıra ile bölük bölük geliş en yararlı iki sınırı verdi, diğer adaylar aynı art ardalık karşılaştırmasını tekrarladı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal belirli söz yapıları ve olay örnekleriyle sınırlıdır; komşu dal ise ara vermeden birbirini izlemeyi genel bir süreç olarak adlandırır.","focus_only":"Art ardalığı hızlı tokat ve peş peşe geliş bildiren özel yapılarda ifade eder.","gloss":"özel art ardalık ile genel kesintisiz sıra","neighbor_only":"Nesne ve eylemlerin ara vermeden sürmesini yapı veya olay türünden bağımsız genel olarak anlatır.","neighbor_ref":"root_000175/B004","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir olayın ardından benzer bir olayın gelmesi temel ortak alandır."},{"boundary_match":"partial","distinction":"Odak dal olayların doğrudan ardışıklığını niteler; komşu dal ise birbirini izleyen ayrı topluluk veya sürü kümelerini öne çıkarabilir.","focus_only":"Tek tek vuruş veya gelişlerin peş peşe olmasını özel niteleme olarak bildirir.","gloss":"peş peşe oluş ile bölük bölük geliş","neighbor_only":"Hayvan, insan veya toplulukların bölük bölük ve kafileler halinde gelmesini de kapsar.","neighbor_ref":"root_000563/B005","relation_type":"near_neighbor","shared_zone":"İki dal, birden çok gelişin zaman içinde birbirini izlemesi bakımından örtüşür."}],"source_phrase_ar":"لطمه لطما شركيا أي سريعا متتابعا (sihah)؛ لطمه لطما شركيا أي متتابعا (tahdhib)؛ ورد بعد ورد متتابع (sihah)","source_summary":"Kaynak ifadesi art arda gelme niteliğini hızlı tokat dizisi ve bir gelişten sonra gelen başka geliş örnekleriyle sınırlandırılmış biçimde sunar.","sources":["SI","TA"],"what_is_ar":"يدخل فيه اللطم الشركي أي المتتابع؛ ورد بعد ورد متتابع","what_is_not_ar":"ليس هو المشاركة؛ ولا شراك النعل؛ ولا الطريق"},"support_links":[]},{"boundary":"Dal, kişi için kaygılı iç konuşma ve görüş için tek olmama niteliklerini ayırır; insanlarca birlikte benimsenen ortak görüş anlamını taşımaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000791/B008","candidate_links":[{"candidate_id":"cand_dd9df6c0d0e3bda0b076","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُشْرِك","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mu$orik|ROOT:$rk|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:7:1","qac_word_ref":"12:106:7","surface_ar":"مُّشْرِكُونَ"}],"gloss":"kaygılı iç konuşma veya bölünmüş görüş","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi, kaygılı biri gibi kendi kendine konuşur ve iç düşüncesiyle meşgul görünür."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Görüşe uygulandığında söz, görüşün tek ve birleşik olmayıp birden çok yöne bölünmüş olduğunu bildirir."}}],"root_ar":"ش ر ك","root_id":"root_000791","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi yüklemindeki kendi kendine konuşma ile görüş yüklemindeki tek olmama anlamını birbirine karıştırmadan birlikte gösteren açıklayıcı karşılıktır.","boundary_detail":"Dal, kişi için kaygılı iç konuşma ve görüş için tek olmama niteliklerini ayırır; insanlarca birlikte benimsenen ortak görüş anlamını taşımaz.","branch_image_ar":"رأي مشترك","concept_gloss":"kaygılı iç konuşma veya bölünmüş görüş","contextual_glosses":[{"applicability":"Söz, düşünceli veya kaygılı görünerek kendi kendine konuşan bir kişiyi nitelediğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Görüşün tek olmayıp bölünmesi kullanımını kapsamaz.","preserves":"Kişinin kaygılı görünümünü ve kendi kendine konuşmasını korur."},"facet_ids":["F001"],"text":"kaygıyla kendi kendine konuşan","usage_role":"contextual"},{"applicability":"Söz bir kişinin görüşünün tek ve tutarlı bir yönde birleşmediğini bildirdiğinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Kendi kendine konuşan kişi kullanımını kapsamaz.","preserves":"Görüşün tek olmaması ve farklı yönlere ayrılması niteliğini korur."},"facet_ids":["F002"],"text":"görüşü bölünmüş","usage_role":"contextual"}],"definition":"Kişi hakkında kullanıldığında kaygılı biri gibi kendi kendine konuşup iç düşüncesiyle meşgul olmayı; görüş hakkında kullanıldığında ise görüşün tek ve birleşik olmayıp bölünmesini anlatır. İki kullanım aynı değildir ve bağlamlarına göre ayrılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi, kaygılı biri gibi kendi kendine konuşur ve iç düşüncesiyle meşgul görünür."},{"facet_id":"F002","role":"source_variant","statement":"Görüşe uygulandığında söz, görüşün tek ve birleşik olmayıp birden çok yöne bölünmüş olduğunu bildirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Birden çok kişinin aynı görüşü paylaştığı anlamını ekler.","collision":"Çağdaş kullanımda insanlarca birlikte benimsenen görüş anlamıyla karışır.","fit":"displacement","loses":"Görüşün tek olmayıp bölünmüş olması ve kişinin kendi kendine konuşması anlamlarını yitirir.","preserves":"Görüşle ilgili bir niteleme bulunduğu izlenimini kısmen korur."},"text":"ortak görüş"}],"identity_rationale":"Kaynak ifadesi tek bir ortak görüşü değil, kaygılı biri gibi kendi kendine konuşan kişiyi ve tek çizgide olmayan, bölünmüş görüşü anlatan iki kullanımı birlikte verir. Bu nedenle dal, paylaşılan görüş olarak değil iç konuşma ve görüş birliğinin bozulmasıyla ilişkili iki yapı olarak yeniden çerçevelenmiştir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kaygılı biçimde kendi kendine konuşan"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"görüşü tek olmayan veya bölünmüş"}],"lexicalization_note":"Dal kişi ve görüş hakkında kullanılan iki bağlı yapıyı ayırır; ikisi de yalın kökün genel ortaklık anlamına dönüştürülmez.","neighbor_coverage_note":"Bütün görüş, düşünme, şaşkınlık ve kök içi adaylar incelendi; genel görüş alanı ile doğrudan şaşkınlık en yararlı sınırları sağladı, diğer adaylar yalnız dolaylı çağrışım taşıdı.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal zihinsel içeriğin bölünmesi veya dışa vurulan iç konuşmayla ilgilidir; komşu dal ise görüş ve düşünme yetisini olumlu ya da nötr biçimde genel olarak adlandırır.","focus_only":"Kaygılı kendi kendine konuşmayı veya görüşün tek olmayıp bölünmesini bildirir.","gloss":"bölünmüş görüş ile düşünülmüş görüş","neighbor_only":"Görüş oluşturma, düşünme, bilme, tasarlama ve danışma süreçlerinin genel alanını kapsar.","neighbor_ref":"root_000531/B002","relation_type":"same_field","shared_zone":"Her iki dal kişinin zihinsel uğraşı ve görüşüyle ilişkilidir."},{"boundary_match":"partial","distinction":"Odak dal davranış ve görüş niteliği üzerinden tanımlanır; komşu dalın çekirdeği ise kişinin doğrudan şaşırıp ne yapacağını bilememesidir.","focus_only":"Kendi kendine konuşma davranışını ve görüşün tek olmamasını ayrı yapılarla belirtir.","gloss":"bölünmüş görüş ile şaşkınlık","neighbor_only":"Belirli bir konuşma veya görüş yapısı gerektirmeden doğrudan şaşkınlık ve kararsızlık durumunu anlatır.","neighbor_ref":"root_000485/B012","relation_type":"near_neighbor","shared_zone":"Kaygılı iç konuşma veya bölünmüş görüş, kararsızlık ve şaşkınlıkla birlikte görülebilir."}],"source_phrase_ar":"رأيت فلانا مشتركا إذا كان يحدث نفسه كالمهموم (sihah;tahdhib)؛ رأيه مشترك ليس بواحد (tahdhib)","source_summary":"Toplu ifade iki bağlama bağlı görünüm sunar: kaygılı biçimde kendi kendine konuşan kişi ve tek bir çizgide birleşmeyen, bölünmüş görüş.","sources":["SI","TA"],"what_is_ar":"يدخل فيه وصف من يحدث نفسه كالمهموم؛ والرأي الذي ليس بواحد","what_is_not_ar":"ليس هو الاشتراك في مال؛ ولا الشرك بالله؛ ولا الشراك الحسي"},"support_links":["sup_7e8cdb3dc1726a583d23"]},{"boundary":"Çekirdek anlam yalın çokluktur; yarışma, övünme ve kalıplaşmış özel adlandırmalar bu sınırın dışında tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B001","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْثَر","morph_features":"STEM|POS:N|LEM:>akovar|ROOT:kvr|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:3:1","qac_word_ref":"12:106:3","surface_ar":"أَكْثَرُ"}],"gloss":"çokluk ve sayıca artma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çokluk, azlığın karşıtıdır ve özellikle sayılabilen varlıklarda sayının yüksekliğini ya da artışını bildirir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir şey çok duruma gelebilir, bir başkası onu çok duruma getirebilir veya kişi ondan çokça edinebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Az ve çok, malın ya da içinde bulunulan durumun iki karşıt ölçüsünü birlikte anan kalıpta kullanılabilir."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin çok bulunmasını ve sayısının artmasını birlikte anlatan genel çekirdek için uygundur.","boundary_detail":"Çekirdek anlam yalın çokluktur; yarışma, övünme ve kalıplaşmış özel adlandırmalar bu sınırın dışında tutulur.","branch_image_ar":"الكثرة ونماء العدد","concept_gloss":"çokluk ve sayıca artma","contextual_glosses":[{"applicability":"Bir şeyin kendiliğinden ya da süreç içinde sayıca çok duruma gelmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir şeyin çok duruma gelme sürecini korur."},"facet_ids":["F002"],"text":"çoğalmak","usage_role":"contextual"},{"applicability":"Bir kişinin ya da etkenin bir şeyi çok duruma getirdiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Dışarıdan yapılan çoklaştırma işlemini korur."},"facet_ids":["F002"],"text":"çoğaltmak","usage_role":"contextual"},{"applicability":"Malın veya bir durumun az ve çok miktarlarını birlikte karşılayan kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşıt iki miktarın birlikte anılmasını korur."},"facet_ids":["F003"],"text":"azı ve çoğu","usage_role":"contextual"}],"definition":"Bir şeyin ya da ayrık bir niceliğin az olmayacak ölçüde bulunması veya sayıca artmasıdır. Buna bir şeyi çok duruma getirme ve ondan çokça edinme gibi bu çekirdekten türeyen işlemler de bağlanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çokluk, azlığın karşıtıdır ve özellikle sayılabilen varlıklarda sayının yüksekliğini ya da artışını bildirir."},{"facet_id":"F002","role":"extension","statement":"Bir şey çok duruma gelebilir, bir başkası onu çok duruma getirebilir veya kişi ondan çokça edinebilir."},{"facet_id":"F003","role":"associated_use","statement":"Az ve çok, malın ya da içinde bulunulan durumun iki karşıt ölçüsünü birlikte anan kalıpta kullanılabilir."}],"identity_rationale":"Kaynak ifadesi, çokluğu azlığın karşıtı ve sayının artması olarak kurar; ayrıca bir şeyin çok duruma gelmesini, çok duruma getirilmesini ve ondan çokça edinilmesini de açıkça kapsar.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"çokluk; sayının artması ve azlığın karşıtı"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"bir şey çoğaldı, sayısı arttı"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çok, sayıca fazla"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"bir şeyi çoğaltmak"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"bir şeyden çokça edinmek veya onu çok saymak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"malın ya da durumun azı ve çoğu"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"pek çok, çok büyük sayıda"}],"lexicalization_note":"Tanım yalın çokluk çekirdeğini öne alır; artırma, çokça edinme ve azıyla çoğunu birlikte anan kalıp ayrı bağımlı kullanımlar olarak korunur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel artış, çokluk yarışı ve koyuna özgü çoğalma, çekirdek sınırı en açık biçimde gösterdikleri için yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Artış bir miktara eklenme işlemini öne çıkarırken odak dal, herhangi bir karşılaştırmalı ekleme gerektirmeden çok olma durumunu da anlatır.","focus_only":"Odak dal, bir şeyin çok bulunmasını ve azlığın karşıtı olan durumu da kapsar.","gloss":"artış ve çokluk","neighbor_only":"Komşu dal, var olan ölçünün üzerine belirli bir ekleme yapılmasını çekirdek edinir.","neighbor_ref":"root_000558/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal da sayının veya miktarın başlangıçtakinden daha yüksek olabildiği durumlarda buluşur."},{"boundary_match":"partial","distinction":"Odak dal yalın çokluk ve çoğalmadır; komşu dal ise çokluğu taraflar arasındaki yarışın ve üstün gelmenin ölçüsü yapar.","focus_only":"Odak dalda başka bir tarafı geçme ya da övünme koşulu bulunmaz.","gloss":"çokluk ve çokluk yarışı","neighbor_only":"Komşu dal iki tarafın çokluk bakımından yarışmasını, övünmesini veya birinin ötekini geçmesini gerektirir.","neighbor_ref":"root_001286/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da sayının, malın veya başka bir varlığın çokluğu belirleyici olabilir."},{"boundary_match":"partial","distinction":"Komşu dalın kapsamı koyunla sınırlıyken odak dal nesne türüne bağlı olmayan genel çokluk çekirdeğidir.","focus_only":"Odak dal her tür sayılabilir varlıkta ve nicelikte genel çokluğu kapsar.","gloss":"genel çokluk ve koyun çokluğu","neighbor_only":"Komşu dal yalnız koyun sürüsünün çoğalmasına bağlı özel bir kullanımdır.","neighbor_ref":"root_000900/B002","relation_type":"near_neighbor","shared_zone":"İki dal da sayılabilir varlıkların sayıca çok olmasını anlatabilir."}],"source_phrase_ar":"الكثرة نماء العدد (ayn;tahdhib)؛ الكثير ضد القليل (jamhara)؛ الكثرة نقيض القلة (sihah)؛ أصل صحيح يدل خلاف القلة (maqayis)؛ الكثرة والقلة يستعملان في الكمية المنفصلة كالأعداد (mufradat)؛ كثر الشيء كثرة فهو كثير (ayn;sihah;tahdhib)؛ أكثرت الشيء وكثرته جعلته كثيرا (ayn;tahdhib)؛ استكثرت من الشيء أي أكثرت منه (sihah)؛ عدد كثار وكثير وكاثر (jamhara;sihah;mufradat;maqayis)","source_summary":"Kaynaklar çokluğu azlığın karşıtı, sayının artması ve bir şeyin çok olması diye ortaklaştırır; ayrıca çoklaştırma, çokça edinme ve çokluk bildiren niteleme biçimlerini aynı anlam alanına bağlar.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه كثرة الشيء والعدد والمال، وضد القلة، والوصف بكثير وكثار وكاثر، وجعل الشيء كثيرا أو الاستكثار منه.","what_is_not_ar":"ليس هو التفاخر أو الغلبة بالكثرة من حيث هي منافسة، ولا كوثر النهر أو الخير الكثير بوصفه اسما مخصوصا، ولا جمار النخل."},"support_links":[]},{"boundary":"Yalın biçimde çok olma bu dala yetmez; karşılaştırma, yarışma, övünme veya çoklukla üstün gelme gerekir.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B002","candidate_links":[{"candidate_id":"cand_dd9df6c0d0e3bda0b076","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"أَكْثَر","morph_features":"STEM|POS:N|LEM:>akovar|ROOT:kvr|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:3:1","qac_word_ref":"12:106:3","surface_ar":"أَكْثَرُ"}],"gloss":"çokluk yarışı ve çoklukla üstün gelme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Taraflar çokluğu bir karşılaştırma ve yarışma ölçüsü yapar."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yarışın sonucu, bir tarafın sayıca daha çok olup öteki tarafa üstün gelmesi olabilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yarışma ve övünme yalnız kişi sayısında değil, malda ve saygınlık sağlayan güçte de gerçekleşebilir."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tarafların çokluğu yarıştırdığı, bununla övündüğü veya birinin daha çok olarak ötekini geçtiği bağlamlar için uygundur.","boundary_detail":"Yalın biçimde çok olma bu dala yetmez; karşılaştırma, yarışma, övünme veya çoklukla üstün gelme gerekir.","branch_image_ar":"المكاثرة والغلبة بالعدد","concept_gloss":"çokluk yarışı ve çoklukla üstün gelme","contextual_glosses":[{"applicability":"Bir topluluğun öteki topluluktan daha çok olduğu ve onu bu bakımdan geçtiği durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sayı karşılaştırmasını ve üstün gelen tarafı korur."},"facet_ids":["F002"],"text":"sayıca geçmek","usage_role":"contextual"},{"applicability":"Mal, sayı veya saygınlık gücü üzerinden karşılıklı övünme ve yarışma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yarışma alanlarını ve övünme yönünü korur."},"facet_ids":["F001","F003"],"text":"çoklukla övünme yarışı","usage_role":"contextual"}],"definition":"İki tarafın sayı, mal veya saygınlık sağlayan güç bakımından çokluk yarıştırması, bununla övünmesi ya da bir tarafın daha çok olarak ötekini geçmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Taraflar çokluğu bir karşılaştırma ve yarışma ölçüsü yapar."},{"facet_id":"F002","role":"specialization","statement":"Yarışın sonucu, bir tarafın sayıca daha çok olup öteki tarafa üstün gelmesi olabilir."},{"facet_id":"F003","role":"extension","statement":"Yarışma ve övünme yalnız kişi sayısında değil, malda ve saygınlık sağlayan güçte de gerçekleşebilir."}],"identity_rationale":"Kaynak ifadesi iki tarafın sayı, mal veya güç sayılan bir üstünlük alanında yarışmasını ve bir tarafın çoklukla ötekini geçmesini açıkça bildirir; yenilen tarafı adlandıran biçim de aynı karşıt ilişkiyi doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"onlarla çokluk yarışına girdik ve onları sayıca geçtik"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"mal, sayı veya güç bakımından çokluk yarışı ve övünme"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"çokluk yarışında yenilmiş"}],"lexicalization_note":"Tanım, yarışma ve üstün gelme bildiren yapılara bağlıdır; yalın çokluk anlamı bu yapılardan bağımsız biçimde dala aktarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yalın çokluk, cömertlik yarışı ve genel övünme, bu dalın çokluk ölçüsüne bağlı yarış sınırını en iyi gösteren karşılaştırmalardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda çokluk karşılaştırmalı bir yarışın aracıdır; komşu dalda ise kendi başına bir nicelik durumu veya artma sürecidir.","focus_only":"Odak dal, taraflar arasında yarışma veya üstün gelme ilişkisini zorunlu kılar.","gloss":"çokluk yarışı ve yalın çokluk","neighbor_only":"Komşu dal, başka bir taraf bulunmadan yalın çokluğu ve çoğalmayı da kapsar.","neighbor_ref":"root_001286/B001","relation_type":"near_neighbor","shared_zone":"İki dal da sayının, malın veya başka bir ölçünün çok olmasına dayanır."},{"boundary_match":"partial","distinction":"İlişki düzeni benzese de üstünlüğün ölçüsü ayrıdır: odak dal çokluğu, komşu dal cömertliği temel alır.","focus_only":"Odak dalın yarış ölçüsü sayı, mal veya toplumsal güç gibi çokluk alanlarıdır.","gloss":"çoklukta ve cömertlikte yarış","neighbor_only":"Komşu dalın yarış ölçüsü cömertlik ve eli açıklıktır.","neighbor_ref":"root_001294/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal karşılıklı övünme ve bir tarafın belirli bir ölçütte ötekini geçmesi düzenini taşır."},{"boundary_match":"partial","distinction":"Odak dal, üstünlük iddiasını sayı veya mal gibi çoğaltılabilir değerlere bağlarken komşu dal daha genel bir övünme üstünlüğüdür.","focus_only":"Odak dal övünmeyi özellikle çokluk ölçüsüne bağlar.","gloss":"çoklukla övünmek ve genel övünme","neighbor_only":"Komşu dal övünme alanını belirli bir çokluk ölçüsüyle sınırlamaz.","neighbor_ref":"root_001135/B002","relation_type":"near_neighbor","shared_zone":"İki dalda da karşılıklı övünme ve bir tarafın üstün sayılması bulunabilir."}],"source_phrase_ar":"كاثرناهم فكثرناهم (ayn;sihah;tahdhib)؛ كاثر بنو فلان بني فلان فكثروهم إذا زادوا على عددهم (jamhara)؛ كاثر بنو فلان بني فلان فكثروهم أي كانوا أكثر منهم (maqayis)؛ كاثرناهم فكثرناهم أي غلبناهم بالكثرة (sihah)؛ التكاثر المكاثرة (sihah)؛ التفاخر بكثرة العدد والمال (tahdhib)؛ المكاثرة والتكاثر التباري في كثرة المال والعز (mufradat)؛ فلان مكثور أي مغلوب في الكثرة (mufradat)","source_summary":"Kaynaklar, çokluk bakımından karşılıklı yarışmayı sayıca geçme ve üstün gelme sonucuyla birlikte verir; yarışın mal ve toplumsal güç üzerinden övünmeye uzanabildiğini de belirtir.","sources":["AY","JA","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه كاثرناهم فكثرناهم، ومكاثرة القوم إذا غلبوا غيرهم بالعدد، والتكاثر والتفاخر أو التباري بكثرة العدد والمال والعز.","what_is_not_ar":"ليس هو مجرد كون الشيء كثيرا بلا مقابلة أو مفاخرة، ولا المكثر بمعنى كثير المال وحده."},"support_links":["sup_7e8cdb3dc1726a583d23"]},{"boundary":"Her anlam kendi kalıbına bağlıdır; mal çokluğu, çok konuşma, çok sayıda istemle karşılaşma ve başkasının malıyla çok görünme birbirinin yerine geçmez.","branch_kind":"collocation","branch_ref":"root_001286/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْثَر","morph_features":"STEM|POS:N|LEM:>akovar|ROOT:kvr|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:3:1","qac_word_ref":"12:106:3","surface_ar":"أَكْثَرُ"}],"gloss":"kişiye bağlı çokluk nitelemeleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli kişi ve durum kalıpları, malın, sözün, isteklerin veya hakların bir kişiye bağlı çokluğunu bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Başka bir kişi kalıbı, kadın veya erkeğin çok konuştuğunu bildirir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Edilgen yapı, kişiden iyilik isteyenlerin veya onun üzerindeki hakların çokluğunu bildirir."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bir başka kalıp, kişinin başkasının malına dayanarak kendini çok malı varmış gibi göstermesini anlatır."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnız mal, konuşma, istem veya hak çokluğunu belirli kişi kalıplarında toplayan üst açıklama olarak uygundur.","boundary_detail":"Her anlam kendi kalıbına bağlıdır; mal çokluğu, çok konuşma, çok sayıda istemle karşılaşma ve başkasının malıyla çok görünme birbirinin yerine geçmez.","branch_image_ar":"كثرة في صاحب أو كلام أو مطالب","concept_gloss":"kişiye bağlı çokluk nitelemeleri","contextual_glosses":[{"applicability":"Bir kişinin varlığının ve malının çok olduğunu bildiren kişi kalıbında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yüklenen mal çokluğunu korur."},"facet_ids":["F001"],"text":"malı çok kişi","usage_role":"contextual"},{"applicability":"Kadın veya erkek için sözün çokluğunu bildiren niteleme kalıbında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Konuşmanın çokluğu ve kişi niteliğini korur."},"facet_ids":["F002"],"text":"çok konuşan kişi","usage_role":"contextual"},{"applicability":"Kendisinden iyilik isteyenlerin veya üzerindeki hakların çok olduğu kişi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çok sayıda isteyen veya hak sahibinin kişiye yönelmesini korur."},"facet_ids":["F003"],"text":"istek ve hak yükü altında","usage_role":"explanatory"},{"applicability":"Kişinin kendisine ait olmayan mala dayanarak çok malı varmış gibi görünmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Malın başkasına ait oluşunu ve görünüş yaratmayı korur."},"facet_ids":["F004"],"text":"başkasının malıyla varlıklı görünmek","usage_role":"contextual"}],"definition":"Belirli kalıplarda bir kişinin malının ya da sözünün çok olması, kendisinden iyilik isteyenlerin veya üzerindeki hakların çoğalması yahut başkasının malıyla kendini varlıklı göstermesidir. Bu kullanımlar yalnız bağlı oldukları kalıp içinde geçerlidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli kişi ve durum kalıpları, malın, sözün, isteklerin veya hakların bir kişiye bağlı çokluğunu bildirir."},{"facet_id":"F002","role":"specialization","statement":"Başka bir kişi kalıbı, kadın veya erkeğin çok konuştuğunu bildirir."},{"facet_id":"F003","role":"specialization","statement":"Edilgen yapı, kişiden iyilik isteyenlerin veya onun üzerindeki hakların çokluğunu bildirir."},{"facet_id":"F004","role":"associated_use","statement":"Bir başka kalıp, kişinin başkasının malına dayanarak kendini çok malı varmış gibi göstermesini anlatır."}],"identity_rationale":"Kaynak ifadesi tek bir yalın anlamdan çok, belirli kişi ve durum kalıplarında malı veya sözü çok olma, üzerinde çok sayıda istek ya da hak bulunma ve başkasının malıyla çok görünme kullanımlarını toplar. Dal korunabilir, ancak bu kullanımlar ortak bir yalın kök anlamı gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"malı çok kişi"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çok konuşan kadın veya erkek"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"iyilik isteyenleri veya üzerindeki haklar çoğalmış kişi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"başkasının malıyla kendini varlıklı göstermek"}],"lexicalization_note":"Tanım yalnız verilen kişi ve durum kalıplarının anlam alanını düzenler; bunlardan bağımsız bir yalın çokluk anlamı çıkarmaz.","neighbor_coverage_note":"Bütün adaylar gözden geçirildi; genel çokluk, hak isteme ve çokluk yarışı, kalıba bağlı kişi nitelemelerinin sınırını en belirgin biçimde açığa çıkarır.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Odak dal, çokluk öğesini farklı kalıpların kişi nitelemelerine dağıtır; komşu dal ise çokluğu kendi başına tanımlar.","focus_only":"Odak dalda her anlam belirli bir kişi veya durum kalıbına bağlıdır.","gloss":"kalıba bağlı ve genel çokluk","neighbor_only":"Komşu dal, kalıptan bağımsız yalın çokluğu ve sayıca artmayı kapsar.","neighbor_ref":"root_001286/B001","relation_type":"same_field","shared_zone":"Her iki dalın kullanımlarında da bir varlığın, sözün, malın veya istemin çokluğu bulunur."},{"boundary_match":"partial","distinction":"Odak dalda belirleyici olan isteyenlerin ya da hakların çokluğudur; komşu dalda ise tek bir istem bile olsa hakkın peşine düşme ilişkisidir.","focus_only":"Odak dal, istem veya hak sahiplerinin çokluğunu ve bunların bir kişinin üzerinde birikmesini bildirir.","gloss":"çok sayıda istem ve hak isteme","neighbor_only":"Komşu dal, istemin sayısından bağımsız olarak bir hakkı veya alacağı isteme eylemini çekirdek edinir.","neighbor_ref":"root_000175/B005","relation_type":"near_neighbor","shared_zone":"İki dal da bir kişiye yönelen hak veya iyilik istemleri bağlamında buluşabilir."},{"boundary_match":"field_only","distinction":"Odak dalın kişi nitelemeleri karşılıklı yarışma gerektirmez; komşu dalın çekirdeği karşılaştırma ve üstün gelmedir.","focus_only":"Odak dal kişide bulunan mal, söz veya yük çokluğunu kalıplaşmış biçimde niteler.","gloss":"çokluk niteliği ve çokluk yarışı","neighbor_only":"Komşu dal iki tarafın çokluğu yarıştırmasını ve birinin üstün gelmesini anlatır.","neighbor_ref":"root_001286/B002","relation_type":"same_field","shared_zone":"Her iki dalda mal veya sayı gibi çokluk ölçüleri kişilere bağlanabilir."}],"source_phrase_ar":"رجل مكثر كثير المال (ayn;tahdhib)؛ أكثر الرجل أي كثر ماله (sihah)؛ رجل كاثر إذا كان كثير المال (mufradat)؛ رجل مكثار وامرأة مكثار وهما الكثيرا الكلام (ayn)؛ رجل مكثار وامرأة مكثار إذا كانا كثيري الكلام (tahdhib)؛ المكثار متعارف في كثرة الكلام (mufradat)؛ رجل مكثور عليه أي كثر من يطلب إليه معروفه (ayn;tahdhib)؛ مكثور عليه إذا نفد ما عنده وكثرت عليه الحقوق (sihah)؛ فلان يتكثر بمال غيره (sihah)","source_summary":"Kaynaklar, kalıba göre mal çokluğu, çok konuşma, iyilik isteyenlerin veya hak sahiplerinin çoğalması ve başkasının malıyla varlıklı görünme anlamlarını verir; bunlar ortak çokluk öğesine rağmen ayrı kullanımlardır. Bir açıklamada hakların çoğalmasına kişinin elindekinin tükenmesi eşlik eder.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه مكثر أو كاثر بمعنى كثير المال، ومكثار في كثرة الكلام، ومكثور عليه لكثرة طالبي المعروف أو الحقوق عليه، ويتكثر بمال غيره.","what_is_not_ar":"ليس هو المكاثرة بين جماعتين، ولا كوثر بمعنى السيد الكثير الخير أو النهر."},"support_links":[]},{"boundary":"Irmak, bol iyilik ve cömert kişi ayrı sözlüksel gerçekleşmelerdir; ortak bağları olağanüstü bolluk düşüncesidir.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْثَر","morph_features":"STEM|POS:N|LEM:>akovar|ROOT:kvr|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:3:1","qac_word_ref":"12:106:3","surface_ar":"أَكْثَرُ"}],"gloss":"özel ırmak veya bol iyilik","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"specialization","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sözlük birimi cennette bulunan ve başka ırmakların kendisinden ayrıldığı özel bir ırmağı adlandırır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözlük biriminin ortak çekirdeği, ırmak, iyilik ve kişi kullanımlarını olağanüstü bolluk düşüncesine bağlar."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Kişi kalıbında iyiliği ve bağışı çok, cömert ve önder bir erkek nitelenir."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sözlük biriminin iki temel açıklamasını birlikte gösterir; kişi nitelemesi ayrıca bağlama bağlıdır.","boundary_detail":"Irmak, bol iyilik ve cömert kişi ayrı sözlüksel gerçekleşmelerdir; ortak bağları olağanüstü bolluk düşüncesidir.","branch_image_ar":"الكوثر: خير كثير وفيض مخصوص","concept_gloss":"özel ırmak veya bol iyilik","contextual_glosses":[{"applicability":"Başka ırmakların kendisinden ayrıldığı bildirilen cennet ırmağı anlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Irmak oluşunu ve cennete özgü gönderimi korur."},"facet_ids":["F001"],"text":"cennetteki özel ırmak","usage_role":"contextual"},{"applicability":"Birine verilmiş çok geniş ve büyük iyiliği anlatan açıklamada kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyiliğin hem bolluğunu hem büyüklüğünü korur."},"facet_ids":["F002"],"text":"bol ve büyük iyilik","usage_role":"contextual"},{"applicability":"Cömertliği, iyiliği ve çok bağışta bulunmasıyla öne çıkan erkek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin cömertliğini, önderliğini ve bağış bolluğunu korur."},"facet_ids":["F003"],"text":"iyiliği ve bağışı bol önder","usage_role":"contextual"}],"definition":"Olağanüstü bolluk bildiren özel bir sözlük birimi, cennetteki bir ırmağı veya bol ve büyük iyiliği adlandırır; kişi kalıbında ise iyiliği ve bağışı bol, cömert bir önderi niteler.","distinctive_facets":[{"facet_id":"F001","role":"specialization","statement":"Sözlük birimi cennette bulunan ve başka ırmakların kendisinden ayrıldığı özel bir ırmağı adlandırır."},{"facet_id":"F002","role":"core","statement":"Sözlük biriminin ortak çekirdeği, ırmak, iyilik ve kişi kullanımlarını olağanüstü bolluk düşüncesine bağlar."},{"facet_id":"F003","role":"extension","statement":"Kişi kalıbında iyiliği ve bağışı çok, cömert ve önder bir erkek nitelenir."}],"identity_rationale":"Kaynak ifadesi aynı sözlük birimini cennetteki özel ırmak, bol ve büyük iyilik, ayrıca iyiliği ve bağışı bol cömert önder için kullanır. Dal bu sözlüksel çokanlamlılık olarak korunabilir; bu üç gönderim tek bir varlık tanımıymış gibi birleştirilmemelidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"cennetteki özel ırmak"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bol veya büyük iyilik"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"iyiliği ve bağışı bol, cömert önder"}],"lexicalization_note":"Tanım, yalın bir çokluk anlamı kurmak yerine verilen sözcük ve kişi kalıbına bağlı üç özel kullanımı ayrı tutar.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel çokluk, aynı kökteki yoğun toz kullanımı ve bastıran çokluk, özel bolluk anlamlarının sınırını en yararlı biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal bolluğu belirli bir ırmak, iyilik veya cömert kişi adı ve nitelemesi içinde özelleştirir; komşu dal genel nicelik çekirdeğidir.","focus_only":"Odak dal belirli bir sözlük biriminin ırmak, bol iyilik ve cömert kişi kullanımlarına bağlıdır.","gloss":"özel bolluk kullanımı ve genel çokluk","neighbor_only":"Komşu dal varlık türünden bağımsız yalın çokluğu ve sayıca artmayı anlatır.","neighbor_ref":"root_001286/B001","relation_type":"near_neighbor","shared_zone":"İki dal da azlığın karşıtı olan bolluk düşüncesini taşıyabilir."},{"boundary_match":"field_only","distinction":"Ortak bolluk bağına karşın gönderimler ayrıdır: odak dal iyilik, ırmak ve kişiyi; komşu dal tozu ve aşırı çoğalmayı anlatır.","focus_only":"Odak dal ırmak, iyilik ve cömert kişiyle ilgili özel kullanımları kapsar.","gloss":"bol iyilik ve yoğun toz","neighbor_only":"Komşu dal kabarıp yükselen yoğun tozu ve bir şeyin aşırı derecede çoğalmasını kapsar.","neighbor_ref":"root_001286/B005","relation_type":"same_field","shared_zone":"İki dalın sözlük birimleri olağanüstü çokluk ve bolluk düşüncesiyle açıklanır."},{"boundary_match":"partial","distinction":"Odak dalda baskın gelme koşulu yoktur; komşu dalda çokluğun yükselerek başka şeyleri örtmesi veya yenmesi belirleyicidir.","focus_only":"Odak dalda bolluk özel olarak iyilik, bağış, kişi veya ırmakla sözlükselleşir.","gloss":"bolluk ve bastıran çokluk","neighbor_only":"Komşu dal çokluğun yükselip çevresindekileri bastırmasını çekirdek edinir.","neighbor_ref":"root_000952/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal olağan ölçüyü aşan bir çokluğu anlatabilir."}],"source_phrase_ar":"الكوثر نهر في الجنة يتشعب منه أكثر أنهار الجنة (ayn)؛ الكوثر الخير الكثير الذي أعطاه النبي (ayn)؛ الكوثر من الرجال السيد الكثير الخير (sihah)؛ الكوثر نهر في الجنة وأراد الخير الكثير (maqayis)؛ الكوثر هو الخير الكثير (tahdhib)؛ الكوثر فوعل من الكثرة ومعناه الخير الكثير (tahdhib)؛ الكوثر الرجل الكثير العطاء والخير والسيد (tahdhib)؛ قيل هو نهر في الجنة وقيل الخير العظيم (mufradat)؛ يقال للرجل السخي كوثر (mufradat)","source_summary":"Kaynaklar özel sözlük birimini cennetteki bir ırmak ve bol ya da büyük iyilik olarak açıklar; kişi için kullanıldığında cömertliği, önderliği, iyilik ve bağış bolluğunu bildirir. Bir açıklamada cennet ırmaklarının çoğunun ondan ayrıldığı, bir diğerinde ise bol iyiliğin Peygamber'e verildiği belirtilir.","sources":["AY","SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الكوثر بوصفه نهر الجنة، أو الخير الكثير العظيم، أو الرجل السيد السخي الكثير الخير والعطاء، وكل ذلك من فوعل الكثرة.","what_is_not_ar":"ليس هو مطلق الكثرة العددية، ولا جمار النخل، ولا غبار الكوثر إلا من جهة صيغة المبالغة في الكثرة."},"support_links":[]},{"boundary":"Toz kullanımı yükselme veya kabarma görüntüsüne bağlıdır; genel biçim ise yalnız aşırı derecede çoğalmayı bildirir.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْثَر","morph_features":"STEM|POS:N|LEM:>akovar|ROOT:kvr|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:3:1","qac_word_ref":"12:106:3","surface_ar":"أَكْثَرُ"}],"gloss":"kabarıp yükselen yoğun toz","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Çekirdek olağanüstü çokluktur; toz kalıbında bu çokluk kabarıp havada yükselen yoğun bir görünüm alır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Toz dışındaki bir şey için kullanılan biçim, onun aşırı ve son sınıra varan ölçüde çoğalmasını bildirir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ölüm sahnesindeki tozun kabarıp çoklaşması, yoğun toz kullanımına örnek oluşturur."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın görüntü bakımından belirgin toz çekirdeğini karşılar; genel aşırı çoğalma ayrıca bağlama göre çevrilir.","boundary_detail":"Toz kullanımı yükselme veya kabarma görüntüsüne bağlıdır; genel biçim ise yalnız aşırı derecede çoğalmayı bildirir.","branch_image_ar":"كوثر الغبار وتكوثره","concept_gloss":"kabarıp yükselen yoğun toz","contextual_glosses":[{"applicability":"Çok miktarda tozun kabarıp havada görünür duruma geldiği bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tozun çokluğunu ve havada toplanmış görünümünü korur."},"facet_ids":["F001","F003"],"text":"yoğun toz bulutu","usage_role":"contextual"},{"applicability":"Tozla sınırlı olmayan biçimde bir şeyin aşırı ölçüde çok duruma gelmesi için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Çoğalmanın aşırı dereceye varmasını korur."},"facet_ids":["F002"],"text":"son derece çoğalmak","usage_role":"contextual"}],"definition":"Toz kalıbında, çok olup kabaran veya havada belirgin biçimde yükselen yoğun tozu anlatır. Ayrı bir biçimde ise herhangi bir şeyin son derece çoğalmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Çekirdek olağanüstü çokluktur; toz kalıbında bu çokluk kabarıp havada yükselen yoğun bir görünüm alır."},{"facet_id":"F002","role":"extension","statement":"Toz dışındaki bir şey için kullanılan biçim, onun aşırı ve son sınıra varan ölçüde çoğalmasını bildirir."},{"facet_id":"F003","role":"example","statement":"Ölüm sahnesindeki tozun kabarıp çoklaşması, yoğun toz kullanımına örnek oluşturur."}],"identity_rationale":"Kaynak ifadesi yoğunlaşıp yükselen tozu adlandıran özel kullanımla bir şeyin son derece çoğalmasını bildiren biçimi birlikte verir. Ortak aşırı çokluk bağı dalı korur, ancak toz görüntüsü genel çoğalma anlamının zorunlu parçası değildir.","lexical_glosses":[{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kabarıp yükselen yoğun toz"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"son derece çoğalmak"}],"lexicalization_note":"Tanım, toza bağlı kalıbı ve genel aşırı çoğalma biçimini ayrı yüzler olarak tutar; toz özelliğini yalın çoğalma anlamına taşımaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yükselmiş toz, havadaki görünür toz ve genel çokluk, dalın yoğunluk, kabarma ve aşırılık sınırlarını en açık biçimde karşılaştırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Toz bağlamında anlamlar büyük ölçüde örtüşür; odak dal çokluk ve kabarmayı belirginleştirir ve ayrıca toz dışı aşırı çoğalma kullanımına sahiptir.","focus_only":"Odak dal, yoğun toz yanında bir şeyin aşırı çoğalmasını bildiren ayrı bir biçimi de kapsar.","gloss":"yoğun kabaran toz ve yükselmiş toz","neighbor_only":"Komşu dal tozu genel olarak, özellikle kaldırılmış veya yükselmiş toz olarak adlandırır.","neighbor_ref":"root_001544/B004","relation_type":"near_synonym","shared_zone":"İki dal da havaya kalkmış, görünür ve yoğun tozu anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeğinde yoğunluk ve çokluk vardır; komşu dal görünürlük ve havada uçuşan toz görüntüsüne daha geniş yer verir.","focus_only":"Odak dal tozun çokluğunu ve kabarmasını, ayrıca genel aşırı çoğalmayı bildirir.","gloss":"kabarık yoğun toz ve havadaki toz","neighbor_only":"Komşu dal havada parlayan veya ışıkta belirginleşen ince toz parçalarını da kapsar.","neighbor_ref":"root_001576/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da tozun havaya yükselip görünür olması bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal çokluğun son dereceye ulaşmasını veya yoğun toz olarak görünmesini gerektirirken komşu dal derece bakımından nötrdür.","focus_only":"Odak dal aşırı çoğalmayı ve toza özgü kabarıp yükselme görüntüsünü taşır.","gloss":"aşırı çoğalma ve genel çokluk","neighbor_only":"Komşu dal herhangi bir aşırılık ya da toz görüntüsü gerektirmeyen genel çokluktur.","neighbor_ref":"root_001286/B001","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir şeyin çok olması veya çoğalması durumunu anlatabilir."}],"source_phrase_ar":"الكوثر من الغبار الكثير وقد تكوثر (sihah)؛ يقال للغبار إذا سطع وكثر كوثر (tahdhib)؛ الكوثر الغبار سمي بذلك لكثرته وثورانه (maqayis)؛ تكوثر الشيء كثر كثرة متناهية (mufradat)؛ ثار نقع الموت حتى تكوثرا (sihah;mufradat)","source_summary":"Kaynaklar, çokluğu yüzünden kabarıp yükselen yoğun tozu ve bir şeyin son derece çoğalmasını aynı aşırılık alanında birleştirir; kabaran ölüm tozu bu kullanıma örnek verilir.","sources":["SI","TA","MU","MQ"],"what_is_ar":"يدخل فيه الكوثر من الغبار إذا كثر وثار أو سطع، وتكوثر الشيء إذا كثر كثرة متناهية.","what_is_not_ar":"ليس هو الكوثر بمعنى نهر الجنة أو الخير العظيم، ولا مطلق كثير بلا صورة ثوران أو إفراط."},"support_links":[]},{"boundary":"Temel gönderim hurma ağacının iç göbeğidir; çiçek salkımının ilk oluşumu kaynaklarda verilen daha geniş bir açıklamadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001286/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْثَر","morph_features":"STEM|POS:N|LEM:>akovar|ROOT:kvr|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:3:1","qac_word_ref":"12:106:3","surface_ar":"أَكْثَرُ"}],"gloss":"hurma ağacının iç göbeği","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim, hurma ağacının tepesindeki yumuşak ve yenilebilir iç göbektir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bazı açıklamalar aynı adı hurmanın çiçek salkımının ilk oluşumuna da verir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir ceza sözünde bu hurma ürünü, meyveyle birlikte el kesme cezasının uygulanmadığı şeyler arasında anılır."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kaynakların ortak temel gönderimini, hurma ağacının yumuşak iç bölümü olarak karşılar.","boundary_detail":"Temel gönderim hurma ağacının iç göbeğidir; çiçek salkımının ilk oluşumu kaynaklarda verilen daha geniş bir açıklamadır.","branch_image_ar":"الكثر جمار النخل","concept_gloss":"hurma ağacının iç göbeği","contextual_glosses":[{"applicability":"Ağacın tepe kısmından çıkarılan yumuşak iç göbek yiyecek olarak söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hurmaya ait oluşu, iç konumu ve yenilebilirliği korur."},"facet_ids":["F001"],"text":"hurmanın yenilebilir iç bölümü","usage_role":"explanatory"},{"applicability":"Adın hurma ağacındaki çiçek salkımının ilk oluşumu için kullanıldığı açıklamaya uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hurma ağacını ve çiçeklenmenin ilk oluşumunu korur."},"facet_ids":["F002"],"text":"hurmanın ilk çiçek sürgünü","usage_role":"contextual"}],"definition":"Hurma ağacının tepe bölümündeki yumuşak ve yenilebilir iç göbeğini adlandırır; bazı açıklamalarda çiçek salkımının ilk oluşumuna da uzanır. Aynı birim belirli bir ceza sözünde meyveyle birlikte anılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim, hurma ağacının tepesindeki yumuşak ve yenilebilir iç göbektir."},{"facet_id":"F002","role":"source_variant","statement":"Bazı açıklamalar aynı adı hurmanın çiçek salkımının ilk oluşumuna da verir."},{"facet_id":"F003","role":"associated_use","statement":"Bir ceza sözünde bu hurma ürünü, meyveyle birlikte el kesme cezasının uygulanmadığı şeyler arasında anılır."}],"identity_rationale":"Kaynak ifadesinin ortak ağırlığı hurma ağacının yenilebilir iç göbeğindedir; bazı açıklamalar bunu ağacın çekilen öz bölümü veya çiçek salkımının ilk oluşumu olarak genişletir. Dal korunabilir, fakat bu ikinci açıklama kesin eşdeğer gibi sunulmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"hurma ağacının iç göbeği; bazı açıklamalarda ilk çiçek sürgünü"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"meyve veya hurma göbeği için el kesme cezası yoktur"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"hurma ağacı çiçek sürgünü verdi"}],"lexicalization_note":"Tanım, bitki adını çekirdek alır; söz içindeki kullanım ve ağacın çiçeklenmesini bildiren biçim ayrı bağlı kullanımlar olarak korunur.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel ağaç göbeği, hurma salkımı ve zararlı sert sürgün, bitkinin aynı bölgesindeki karışabilecek gönderimleri en iyi ayırır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Hurma göbeği bağlamında büyük ölçüde örtüşürler; odak dalın bitki kapsamı daha dar, çiçek sürgünü açıklaması ise ona özgüdür.","focus_only":"Odak dal hurma ağacına özgüdür ve bazı açıklamalarda ilk çiçek sürgününe uzanır.","gloss":"hurma göbeği ve ağaç göbeği","neighbor_only":"Komşu dal hurma yanında başka ağaçların yumuşak iç göbeklerini de kapsar.","neighbor_ref":"root_001248/B003","relation_type":"near_synonym","shared_zone":"İki dal da hurma ağacının tepesindeki yumuşak iç bölümü adlandırır."},{"boundary_match":"field_only","distinction":"Odak dal yumuşak iç dokuya veya ilk sürgüne, komşu dal ise gelişmiş meyveleri taşıyan salkıma gönderir.","focus_only":"Odak dal ağacın iç göbeğini ve bazı açıklamalarda ilk çiçek oluşumunu anlatır.","gloss":"hurma göbeği ve meyve salkımı","neighbor_only":"Komşu dal hurmanın üzerinde meyveler bulunan bütün salkımını adlandırır.","neighbor_ref":"root_001264/B004","relation_type":"same_field","shared_zone":"İki dal da hurma ağacının tepe ve ürün oluşumu alanıyla ilgilidir."},{"boundary_match":"field_only","distinction":"Odak dal yumuşak ve yenilebilir iç bölümü öne çıkarır; komşu dal sertliği ve ağaca zarar verme sonucuyla ayrılır.","focus_only":"Odak dal yenilebilir iç göbeği veya ilk çiçek sürgününü adlandırır.","gloss":"yumuşak göbek ve zararlı sert sürgün","neighbor_only":"Komşu dal bırakıldığında ağaca zarar veren uzun ve sert bir sürgünü anlatır.","neighbor_ref":"root_000489/B003","relation_type":"same_field","shared_zone":"Her iki dal hurma ağacının kalbinden veya tepesinden çıkan bir oluşumla ilgilidir."}],"source_phrase_ar":"الكثر والكثر جمار النخل ويقال الكثر الجذب وهو الجمار أيضا (ayn)؛ الكثر الجمار وقال قوم هو الكثر بفتح الثاء (jamhara)؛ لا قطع في ثمر ولا كثر (jamhara;sihah;tahdhib;mufradat)؛ الكثر جمار النخل ويقال طلعها (sihah)؛ الكثر جمار النخل في كلام الأنصار وهو الجذب أيضا (tahdhib)؛ الكثر الجمار الكثير وحكي بتسكين الثاء (mufradat)","source_summary":"Kaynaklar adı çoğunlukla hurma ağacının iç göbeği ve çekilen öz bölümü için verir; bir açıklama çiçek salkımının ilk oluşumunu da kapsar ve yaygın bir sözde meyveyle birlikte anılır. Ad için kaynaklarda birden fazla harekeleme ve okunuş biçimi de aktarılır.","sources":["AY","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الكثر أو الكثر بمعنى جمار النخل، والجذب، وطلع النخل عند بعض المصادر، وما ورد في لا قطع في ثمر ولا كثر.","what_is_not_ar":"ليس هو الكثرة العددية، ولا الكوثر، ولا المال الكثير."},"support_links":[]},{"boundary":"Dal yalnız bir şeyin bir araya gelmesi anlamındadır; genel çokluk, hurma bölümü veya özel bolluk adlandırmaları buna katılmaz.","branch_kind":"bare","branch_ref":"root_001286/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"أَكْثَر","morph_features":"STEM|POS:N|LEM:>akovar|ROOT:kvr|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:3:1","qac_word_ref":"12:106:3","surface_ar":"أَكْثَرُ"}],"gloss":"bir araya toplanma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyin öğeleri bir araya gelir ve toplu duruma geçer."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sözcük yapısındaki ek ses, birimin çokluk anlam ailesine bağlı oluşunu açıklamak için belirtilir."}}],"root_ar":"ك ث ر","root_id":"root_001286","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir şeyin öğelerinin birleşerek toplu duruma gelmesini anlatan yalın anlam için uygundur.","boundary_detail":"Dal yalnız bir şeyin bir araya gelmesi anlamındadır; genel çokluk, hurma bölümü veya özel bolluk adlandırmaları buna katılmaz.","branch_image_ar":"الكمثرة اجتماع الشيء","concept_gloss":"bir araya toplanma","contextual_glosses":[{"applicability":"Bir şeyin ayrı öğelerinin aynı yerde veya bütün içinde birleşmesi bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayrı öğelerin birleşme sürecini korur."},"facet_ids":["F001"],"text":"toplanıp bir araya gelmek","usage_role":"contextual"}],"definition":"Bir şeyin parçalarının veya öğelerinin bir araya gelerek toplanmasıdır; sözlük biriminin yapısındaki ek ses, bu anlamın çokluk ailesiyle bağlantısı olarak açıklanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyin öğeleri bir araya gelir ve toplu duruma geçer."},{"facet_id":"F002","role":"associated_use","statement":"Sözcük yapısındaki ek ses, birimin çokluk anlam ailesine bağlı oluşunu açıklamak için belirtilir."}],"identity_rationale":"Tek kaynak ifadesi, bir şeyin bir araya toplanması anlamını doğrudan verir ve sözcük yapısındaki ek sesin çokluk ailesiyle bağlantısını ayrıca belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"bir şeyin bir araya toplanması; yapısına m sesi eklenmiştir"}],"lexicalization_note":"Tanım, kanıtta verilen yalın sözlük biriminin bir araya toplanma anlamıyla sınırlıdır ve herhangi bir kalıp anlamı eklemez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; genel toplama, yönlerden bir araya getirme ve doluluk yaratan birikme, bu yalın toplanma anlamının kapsamını en iyi sınırlar.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Ortak çekirdek güçlüdür; komşu dalın eylem, katılımcı ve kullanım kapsamı odak daldan daha geniştir.","focus_only":"Odak dal yalnız bir şeyin öğelerinin bir araya toplanmasını bildirir.","gloss":"bir araya toplanma ve genel toplama","neighbor_only":"Komşu dal hem toplama eylemini hem insanların, suyun, yemeğin ve başka varlıkların çeşitli birleşme biçimlerini kapsar.","neighbor_ref":"root_001210/B001","relation_type":"near_synonym","shared_zone":"İki dal da ayrı öğelerin birleşerek toplu duruma gelmesini anlatır."},{"boundary_match":"partial","distinction":"Odak dal sonuçlanan bir araya gelişi bildirirken komşu dal toplama işlemini, yön çeşitliliğini ve türemiş kullanımları daha geniş biçimde taşır.","focus_only":"Odak dal yalın biçimde bir şeyin bir araya toplanmasını anlatır.","gloss":"toplanma ve yönlerden toplama","neighbor_only":"Komşu dal farklı yönlerden toplama, birbirine katma ve bundan türetilen adlandırmaları da kapsar.","neighbor_ref":"root_001216/B001","relation_type":"near_synonym","shared_zone":"İki dalda da dağınık öğelerin bir araya gelmesi temel görüntüdür."},{"boundary_match":"partial","distinction":"Odak dal nicelik derecesi belirtmez; komşu dal birikimin çok ve doluluk yaratacak ölçüde olmasını çekirdek edinir.","focus_only":"Odak dal için öğelerin bir araya gelmesi yeterlidir; çokluk veya doluluk zorunlu değildir.","gloss":"toplanma ve dolacak kadar birikme","neighbor_only":"Komşu dal toplanmanın yanında çokluğu ve dolacak ölçüde birikmeyi gerektirir.","neighbor_ref":"root_000261/B001","relation_type":"near_neighbor","shared_zone":"İki dal da öğelerin aynı yerde birikmesi veya birleşmesi durumunda buluşur."}],"source_phrase_ar":"الكمثرة اجتماع الشيء؛ زيدت فيه الميم وهو من الكثرة (maqayis)","source_summary":"Tek kaynak, sözlük birimini bir şeyin bir araya toplanması diye açıklar ve yapısına eklenen m sesiyle birlikte onu çokluk anlam ailesine bağlar.","sources":["MQ"],"what_is_ar":"يدخل فيه الكمثرة بمعنى اجتماع الشيء، مع تصريح Maqāyīs بأن الميم زائدة وأنه من الكثرة.","what_is_not_ar":"ليس هو استعمالا عاديا للثلاثي كثر، ولا الجمار أو الكوثر."},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["12:106:10"],"branch_refs":[],"candidate_id":"cand_0efb5229148bc1a450cc","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000791"],"scope":"focus_ayah","source_local_id":"12:106:10:belief-shirk-opposition-and-echoes","source_type":"word_analysis","support_ids":["sup_bd1863335182d950f784","sup_ded6e1e77078aa405f92"],"title":"belief-shirk opposition and same-surah echoes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:10","qac_refs":["12:106:7:1"],"status":"accepted"}},{"anchor_refs":["12:106:10"],"branch_refs":[],"candidate_id":"cand_8d64573bcbfc95aad558","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000791"],"scope":"focus_ayah","source_local_id":"12:106:10:group-bound-participial-form","source_type":"word_analysis","support_ids":["sup_bd1863335182d950f784","sup_c76782e3ea2f64283cf5"],"title":"group-bound participial form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:10","qac_refs":["12:106:7:1"],"status":"accepted"}},{"anchor_refs":["12:106:10"],"branch_refs":[],"candidate_id":"cand_e3d364ebd9b0c0103dcd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000791"],"scope":"focus_ayah","source_local_id":"12:106:10:nominal-predicate-identity-state","source_type":"word_analysis","support_ids":["sup_aae64b2ee109340d8645","sup_bd1863335182d950f784"],"title":"nominal predicate identity-state","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:10","qac_refs":["12:106:7:1"],"status":"accepted"}},{"anchor_refs":["12:106:10"],"branch_refs":[],"candidate_id":"cand_17a2a0e199ce391fcaf7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000791"],"scope":"focus_ayah","source_local_id":"12:106:10:partner-allocation-root-image","source_type":"word_analysis","support_ids":["sup_bd1863335182d950f784","sup_dc973887020a547cc0c0"],"title":"partner-allocation root image","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:10","qac_refs":["12:106:7:1"],"status":"accepted"}},{"anchor_refs":["12:106:10"],"branch_refs":[],"candidate_id":"cand_5b1e7e54df356e1d9e8f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000791"],"scope":"focus_ayah","source_local_id":"12:106:10:sound-and-boundary-pressure","source_type":"word_analysis","support_ids":["sup_6f56acdaa2a6dd9cc43d","sup_bd1863335182d950f784"],"title":"sound and boundary pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:10","qac_refs":["12:106:7:1"],"status":"accepted"}},{"anchor_refs":["12:106:1"],"branch_refs":[],"candidate_id":"cand_ccc176ba2c1527014f5d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:1:paired-waw-functions","source_type":"word_analysis","support_ids":["sup_9af68330e43307fc3f38","sup_cce57876515591a7bc0c"],"title":"paired waw functions","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:1","qac_refs":["12:106:1:1"],"status":"accepted"}},{"anchor_refs":["12:106:1"],"branch_refs":[],"candidate_id":"cand_a6a2fb5e2db8647912fa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:1:resumptive-diagnostic-pivot","source_type":"word_analysis","support_ids":["sup_cce57876515591a7bc0c","sup_f51fe0510efafb8fed09"],"title":"resumptive pivot into diagnosis","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:1","qac_refs":["12:106:1:1"],"status":"accepted"}},{"anchor_refs":["12:106:2"],"branch_refs":[],"candidate_id":"cand_2531cfada4b334c981f5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:2:ma-illa-restriction","source_type":"word_analysis","support_ids":["sup_60d12cc3d51f2aaa2ad3","sup_eea741b775b3b80227cd"],"title":"negation-exception restriction","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:2","qac_refs":["12:106:1:2"],"status":"accepted"}},{"anchor_refs":["12:106:2"],"branch_refs":[],"candidate_id":"cand_796401fddfb00a838531","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:2:present-negation-of-belief","source_type":"word_analysis","support_ids":["sup_60d12cc3d51f2aaa2ad3","sup_73dbbae9d8a110522223"],"title":"present negation over imperfect belief","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:2","qac_refs":["12:106:1:2"],"status":"accepted"}},{"anchor_refs":["12:106:3"],"branch_refs":[],"candidate_id":"cand_c930cb11f1495090d881","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:3:collective-subject-agreement","source_type":"word_analysis","support_ids":["sup_503f7efc8f65ad501a20","sup_8795b7386a7878badd05"],"title":"singular verb with collective majority subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:3","qac_refs":["12:106:2:1"],"status":"accepted"}},{"anchor_refs":["12:106:3"],"branch_refs":[],"candidate_id":"cand_165d48f54132085eca53","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:3:directed-imperfect-belief","source_type":"word_analysis","support_ids":["sup_503f7efc8f65ad501a20","sup_ab84f17fba8c2ac2dcfe"],"title":"directed imperfect belief clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:3","qac_refs":["12:106:2:1"],"status":"accepted"}},{"anchor_refs":["12:106:3"],"branch_refs":[],"candidate_id":"cand_ace3e2f1edf3ea9760fa","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:3:formula-and-forward-echo","source_type":"word_analysis","support_ids":["sup_503f7efc8f65ad501a20","sup_eecf61dab7069bab3373"],"title":"belief formula complicated and carried forward","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:3","qac_refs":["12:106:2:1"],"status":"accepted"}},{"anchor_refs":["12:106:3"],"branch_refs":[],"candidate_id":"cand_1f8bdb934b34358c4d07","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:3:trust-root-pressure","source_type":"word_analysis","support_ids":["sup_503f7efc8f65ad501a20","sup_b254db745982f75f6422"],"title":"trust and security root pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:3","qac_refs":["12:106:2:1"],"status":"accepted"}},{"anchor_refs":["12:106:4"],"branch_refs":[],"candidate_id":"cand_4e553f3ed0b0a451b408","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"12:106:4:abundance-pressure","source_type":"word_analysis","support_ids":["sup_0ee6dec4f43c0e6646db","sup_86cb6665df9fb6aa11ee"],"title":"abundance root pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:4","qac_refs":["12:106:3:1","12:106:3:2"],"status":"accepted"}},{"anchor_refs":["12:106:4"],"branch_refs":[],"candidate_id":"cand_39fc33f7d0ac47c4c177","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"12:106:4:majority-refrain-and-boundary","source_type":"word_analysis","support_ids":["sup_0ee6dec4f43c0e6646db","sup_c98ce80c50d87519b1b9"],"title":"majority refrain and boundary chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:4","qac_refs":["12:106:3:1","12:106:3:2"],"status":"accepted"}},{"anchor_refs":["12:106:4"],"branch_refs":[],"candidate_id":"cand_ea0c5b0d9ef4657229ab","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"12:106:4:partitive-majority-subject","source_type":"word_analysis","support_ids":["sup_0ee6dec4f43c0e6646db","sup_e875a100c772f574a330"],"title":"partitive majority as subject","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:4","qac_refs":["12:106:3:1","12:106:3:2"],"status":"accepted"}},{"anchor_refs":["12:106:5"],"branch_refs":[],"candidate_id":"cand_b5a76097459f7de3d886","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:5:fused-attachment-and-boundary","source_type":"word_analysis","support_ids":["sup_1f66b8b724e36b06e951","sup_d973303611d5c5752c62"],"title":"fused attachment and sign boundary","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:5","qac_refs":["12:106:4:1"],"status":"accepted"}},{"anchor_refs":["12:106:5"],"branch_refs":[],"candidate_id":"cand_d40c7ed9c1ec35120e01","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:5:governed-belief-target","source_type":"word_analysis","support_ids":["sup_1f66b8b724e36b06e951","sup_d8959642929c8bb949f7"],"title":"governed belief target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:5","qac_refs":["12:106:4:1"],"status":"accepted"}},{"anchor_refs":["12:106:6"],"branch_refs":[],"candidate_id":"cand_cd94139e71101efbdc72","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:6:belief-shirk-relational-center","source_type":"word_analysis","support_ids":["sup_1b385d63674db62e56e6","sup_2f00f76296d0f29dde89"],"title":"belief and shirk meet at the divine name","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:6","qac_refs":["12:106:4:2"],"status":"accepted"}},{"anchor_refs":["12:106:6"],"branch_refs":[],"candidate_id":"cand_653c7542b99c7cf0411f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:6:proper-divine-target","source_type":"word_analysis","support_ids":["sup_2f00f76296d0f29dde89","sup_4cb566a076c143f100df"],"title":"proper divine target of belief","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:6","qac_refs":["12:106:4:2"],"status":"accepted"}},{"anchor_refs":["12:106:6"],"branch_refs":[],"candidate_id":"cand_d0ed426be99703821eb7","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:6:worship-awe-name-pressure","source_type":"word_analysis","support_ids":["sup_2f00f76296d0f29dde89","sup_a5d8885864138a0df637"],"title":"worship and awe pressure in the name","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:6","qac_refs":["12:106:4:2"],"status":"accepted"}},{"anchor_refs":["12:106:7"],"branch_refs":[],"candidate_id":"cand_367668c7c9db5b06030e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:7:controlled-parse-ambiguity","source_type":"word_analysis","support_ids":["sup_7576fd0039c6ed51c7e6","sup_7ee6731272bcd2b81959"],"title":"exception versus restrictive manner","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:7","qac_refs":["12:106:5:1"],"status":"accepted"}},{"anchor_refs":["12:106:7"],"branch_refs":[],"candidate_id":"cand_77da697849a3e92af3fa","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:7:restrictive-haal-hinge","source_type":"word_analysis","support_ids":["sup_7b6d1701af36fc5a46ae","sup_7ee6731272bcd2b81959"],"title":"restrictive circumstantial hinge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:7","qac_refs":["12:106:5:1"],"status":"accepted"}},{"anchor_refs":["12:106:8"],"branch_refs":[],"candidate_id":"cand_ea4ff0065536239f432e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:8:repeated-waw-boundary-frame","source_type":"word_analysis","support_ids":["sup_1dd5e56d2513bae5f35a","sup_d65de5975d158f699044"],"title":"repeated waw and boundary frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:8","qac_refs":["12:106:6:1"],"status":"accepted"}},{"anchor_refs":["12:106:8"],"branch_refs":[],"candidate_id":"cand_a7f2a25ed5bd82cbabf5","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:8:waw-al-haal-simultaneity","source_type":"word_analysis","support_ids":["sup_1dd5e56d2513bae5f35a","sup_57b7d20ca044d90d5728"],"title":"waw al-haal simultaneity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:8","qac_refs":["12:106:6:1"],"status":"accepted"}},{"anchor_refs":["12:106:9"],"branch_refs":[],"candidate_id":"cand_358bbb019ec345736526","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:9:explicit-same-subject","source_type":"word_analysis","support_ids":["sup_03fd88b1a4a7b0c72d57","sup_d6a448b665fb20ee5d33"],"title":"explicit same subject of state clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:9","qac_refs":["12:106:6:2"],"status":"accepted"}},{"anchor_refs":["12:106:9"],"branch_refs":[],"candidate_id":"cand_7a31ee2bdad637748e00","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"12:106:9:suffix-to-independent-echo","source_type":"word_analysis","support_ids":["sup_03fd88b1a4a7b0c72d57","sup_13d395f2354b42e5b4cb"],"title":"suffix returns as independent pronoun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"12:106:9","qac_refs":["12:106:6:2"],"status":"accepted"}},{"anchor_refs":["12:106:2"],"branch_refs":[],"candidate_id":"cand_06c7e9785dbdd7316c45","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000054"],"scope":"focus_ayah","source_local_id":"12:106:2:1","source_type":"qac_morpheme","support_ids":["sup_a892bf53d8c506defbf6"],"title":"QAC root occurrence: ء م ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["12:106:3"],"branch_refs":[],"candidate_id":"cand_5e23a6abe9393db73f3b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001286"],"scope":"focus_ayah","source_local_id":"12:106:3:1","source_type":"qac_morpheme","support_ids":["sup_fae92d43e1057315d172"],"title":"QAC root occurrence: ك ث ر","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["12:106:4"],"branch_refs":[],"candidate_id":"cand_8a04801edf13db63abcf","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000047"],"scope":"focus_ayah","source_local_id":"12:106:4:2","source_type":"qac_morpheme","support_ids":["sup_a10a3004c97b9e5b8cea"],"title":"QAC root occurrence: ء ل ه","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["12:106:7"],"branch_refs":[],"candidate_id":"cand_1fd9e0acace6691dd30d","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000791"],"scope":"focus_ayah","source_local_id":"12:106:7:1","source_type":"qac_morpheme","support_ids":["sup_74e7789a797b6b568dff"],"title":"QAC root occurrence: ش ر ك","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["12:106"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"12:106","branch_refs":["root_000047/B001","root_000054/B002","root_000791/B001","root_000791/B002"],"candidate_id":"cand_6f1a237e763c488b60b8","commentary_obligation":"review","hft_ref":"hft_3238300fd3b693c9b5a5","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-partitioned-assent","source_type":"hft","support_ids":["sup_d26586b0c72196ec6a72"],"title":"baseline-partitioned-assent","trust":"legacy_unbound"},{"anchor_refs":["12:106"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"12:106","branch_refs":["root_000054/B001","root_000791/B001"],"candidate_id":"cand_e7f07309c07dd908a75a","commentary_obligation":"review","hft_ref":"hft_fcd4864862e7c95c91c3","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-distributed-security","source_type":"hft","support_ids":["sup_d6286bd3523f9c526fce"],"title":"baseline-distributed-security","trust":"legacy_unbound"},{"anchor_refs":["12:106"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"12:106","branch_refs":["root_000791/B008","root_001286/B002"],"candidate_id":"cand_dd9df6c0d0e3bda0b076","commentary_obligation":"review","hft_ref":"hft_83996f35d14d7ed254c6","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline-majority-mirrors-multiplicity","source_type":"hft","support_ids":["sup_7e8cdb3dc1726a583d23"],"title":"baseline-majority-mirrors-multiplicity","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَمَا يُؤْمِنُ أَكْثَرُهُم بِٱللَّهِ إِلَّا وَهُم مُّشْرِكُونَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"12:106:1:1","qac_word_ref":"12:106:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:NEG|LEM:maA","morpheme_role":"STEM","pos":"NEG","qac_ref":"12:106:1:2","qac_word_ref":"12:106:1","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"ءَامَنَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:'aAmana|ROOT:Amn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"12:106:2:1","qac_word_ref":"12:106:2","root_ar":"ء م ن","surface_ar":"يُؤْمِنُ"},{"lemma_ar":"أَكْثَر","morph_features":"STEM|POS:N|LEM:>akovar|ROOT:kvr|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:3:1","qac_word_ref":"12:106:3","root_ar":"ك ث ر","surface_ar":"أَكْثَرُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"12:106:3:2","qac_word_ref":"12:106:3","root_ar":"","surface_ar":"هُم"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"12:106:4:1","qac_word_ref":"12:106:4","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"12:106:4:2","qac_word_ref":"12:106:4","root_ar":"ء ل ه","surface_ar":"ٱللَّهِ"},{"lemma_ar":"إِلَّا","morph_features":"STEM|POS:RES|LEM:<il~aA","morpheme_role":"STEM","pos":"RES","qac_ref":"12:106:5:1","qac_word_ref":"12:106:5","root_ar":"","surface_ar":"إِلَّا"},{"lemma_ar":"","morph_features":"PREFIX|w:CIRC+","morpheme_role":"PREFIX","pos":"CIRC","qac_ref":"12:106:6:1","qac_word_ref":"12:106:6","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MP","morpheme_role":"STEM","pos":"PRON","qac_ref":"12:106:6:2","qac_word_ref":"12:106:6","root_ar":"","surface_ar":"هُم"},{"lemma_ar":"مُشْرِك","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mu$orik|ROOT:$rk|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:7:1","qac_word_ref":"12:106:7","root_ar":"ش ر ك","surface_ar":"مُّشْرِكُونَ"}],"word_analysis_qac_refs":[["12:106:1:1"],["12:106:1:2"],["12:106:2:1"],["12:106:3:1","12:106:3:2"],["12:106:4:1"],["12:106:4:2"],["12:106:5:1"],["12:106:6:1"],["12:106:6:2"],["12:106:7:1"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["12:106:1","12:106:2","12:106:3","12:106:4","12:106:5","12:106:6","12:106:7","12:106:8","12:106:9","12:106:10"]},"focus_surface_evidence":{"arabic_uthmani":"وَمَا يُؤْمِنُ أَكْثَرُهُم بِٱللَّهِ إِلَّا وَهُم مُّشْرِكُونَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"12:106:1:1","qac_word_ref":"12:106:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَا","morph_features":"STEM|POS:NEG|LEM:maA","morpheme_role":"STEM","pos":"NEG","qac_ref":"12:106:1:2","qac_word_ref":"12:106:1","root_ar":"","surface_ar":"مَا"},{"lemma_ar":"ءَامَنَ","morph_features":"STEM|POS:V|IMPF|(IV)|LEM:'aAmana|ROOT:Amn|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"12:106:2:1","qac_word_ref":"12:106:2","root_ar":"ء م ن","surface_ar":"يُؤْمِنُ"},{"lemma_ar":"أَكْثَر","morph_features":"STEM|POS:N|LEM:>akovar|ROOT:kvr|MS|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:3:1","qac_word_ref":"12:106:3","root_ar":"ك ث ر","surface_ar":"أَكْثَرُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"12:106:3:2","qac_word_ref":"12:106:3","root_ar":"","surface_ar":"هُم"},{"lemma_ar":"","morph_features":"PREFIX|bi+","morpheme_role":"PREFIX","pos":"P","qac_ref":"12:106:4:1","qac_word_ref":"12:106:4","root_ar":"","surface_ar":"بِ"},{"lemma_ar":"ٱللَّه","morph_features":"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN","morpheme_role":"STEM","pos":"PN","qac_ref":"12:106:4:2","qac_word_ref":"12:106:4","root_ar":"ء ل ه","surface_ar":"ٱللَّهِ"},{"lemma_ar":"إِلَّا","morph_features":"STEM|POS:RES|LEM:<il~aA","morpheme_role":"STEM","pos":"RES","qac_ref":"12:106:5:1","qac_word_ref":"12:106:5","root_ar":"","surface_ar":"إِلَّا"},{"lemma_ar":"","morph_features":"PREFIX|w:CIRC+","morpheme_role":"PREFIX","pos":"CIRC","qac_ref":"12:106:6:1","qac_word_ref":"12:106:6","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"","morph_features":"STEM|POS:PRON|3MP","morpheme_role":"STEM","pos":"PRON","qac_ref":"12:106:6:2","qac_word_ref":"12:106:6","root_ar":"","surface_ar":"هُم"},{"lemma_ar":"مُشْرِك","morph_features":"STEM|POS:N|ACT|PCPL|(IV)|LEM:mu$orik|ROOT:$rk|MP|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"12:106:7:1","qac_word_ref":"12:106:7","root_ar":"ش ر ك","surface_ar":"مُّشْرِكُونَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["12:106:1:1"],["12:106:1:2"],["12:106:2:1"],["12:106:3:1","12:106:3:2"],["12:106:4:1"],["12:106:4:2"],["12:106:5:1"],["12:106:6:1"],["12:106:6:2"],["12:106:7:1"]],"word_analysis_refs":["12:106:1","12:106:2","12:106:3","12:106:4","12:106:5","12:106:6","12:106:7","12:106:8","12:106:9","12:106:10"],"word_rows":[{"analysis_record_ref":"12:106:1","analytic_gloss_range_en":"resumptive conjunction opening a fresh but connected diagnostic assertion","analytic_root_gloss_range_en":null,"qac_refs":["12:106:1:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"12:106:2","analytic_gloss_range_en":"negating particle governing the imperfect belief verb and preparing restriction","analytic_root_gloss_range_en":null,"qac_refs":["12:106:1:2"],"root":{"note":"— (no root)"},"surface":{"arabic":"مَا","transliteration":"mā"}},{"analysis_record_ref":"12:106:3","analytic_gloss_range_en":"Form IV imperfect belief/trust directed by a bā-governed complement and qualified by the exception frame","analytic_root_gloss_range_en":"safety, trust, security, and affirming belief; here narrowed to Form IV directed belief/trust toward God","qac_refs":["12:106:2:1"],"root":{"arabic":"أ م ن","transliteration":"ʾ-m-n"},"surface":{"arabic":"يُؤْمِنُ","transliteration":"yuʾminu"}},{"analysis_record_ref":"12:106:4","analytic_gloss_range_en":"elative majority with attached plural suffix, serving as the subject of the belief verb","analytic_root_gloss_range_en":"abundance, increase, outnumbering, and majority; here narrowed to the greater part of an unnamed referent group","qac_refs":["12:106:3:1","12:106:3:2"],"root":{"arabic":"ك ث ر","transliteration":"k-th-r"},"surface":{"arabic":"أَكْثَرُهُمْ","transliteration":"aktharuhum"}},{"analysis_record_ref":"12:106:5","analytic_gloss_range_en":"preposition attaching the belief verb to its named object and preserving the target before restriction","analytic_root_gloss_range_en":null,"qac_refs":["12:106:4:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"بِ","transliteration":"bi-"}},{"analysis_record_ref":"12:106:6","analytic_gloss_range_en":"proper divine name as the governed target of belief, made sharper by the later shirk predicate","analytic_root_gloss_range_en":"proper divine naming with worship and awe associations; local sense is the proper name, not a generic deity noun","qac_refs":["12:106:4:2"],"root":{"arabic":"أ ل ه","transliteration":"ʾ-l-h"},"surface":{"arabic":"اللَّهُ","transliteration":"Allāh"}},{"analysis_record_ref":"12:106:7","analytic_gloss_range_en":"exception and restriction particle introducing the circumstantial state clause","analytic_root_gloss_range_en":null,"qac_refs":["12:106:5:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"إِلَّا","transliteration":"illā"}},{"analysis_record_ref":"12:106:8","analytic_gloss_range_en":"circumstantial conjunction attaching the nominal state to the belief clause as simultaneous","analytic_root_gloss_range_en":null,"qac_refs":["12:106:6:1"],"root":{"note":"— (no root)"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"12:106:9","analytic_gloss_range_en":"independent plural pronoun starting the nominal state clause and repeating the earlier suffix referent","analytic_root_gloss_range_en":null,"qac_refs":["12:106:6:2"],"root":{"note":"— (no root)"},"surface":{"arabic":"هُمْ","transliteration":"hum"}},{"analysis_record_ref":"12:106:10","analytic_gloss_range_en":"Form IV active participle predicate naming an ongoing partner-assigning identity-state","analytic_root_gloss_range_en":"sharing, partnership, association, partner-attribution, and related concrete branches; here narrowed to theological partner-assignment with partnership imagery still felt","qac_refs":["12:106:7:1"],"root":{"arabic":"ش ر ك","transliteration":"sh-r-k"},"surface":{"arabic":"مُشْرِكُونَ","transliteration":"mushrikūn"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":10,"words_total":10,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":3,"assigned_records":[{"anchor_refs":["12:106"],"branch_refs":["root_000047/B001","root_000054/B002","root_000791/B001","root_000791/B002"],"candidate_id":"cand_6f1a237e763c488b60b8","evidence_scope":"focus_ayah","hft_ref":"hft_3238300fd3b693c9b5a5","item_id":"baseline-partitioned-assent","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-partitioned-assent","support_id":"sup_d26586b0c72196ec6a72"},{"anchor_refs":["12:106"],"branch_refs":["root_000054/B001","root_000791/B001"],"candidate_id":"cand_e7f07309c07dd908a75a","evidence_scope":"focus_ayah","hft_ref":"hft_fcd4864862e7c95c91c3","item_id":"baseline-distributed-security","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-distributed-security","support_id":"sup_d6286bd3523f9c526fce"},{"anchor_refs":["12:106"],"branch_refs":["root_000791/B008","root_001286/B002"],"candidate_id":"cand_dd9df6c0d0e3bda0b076","evidence_scope":"focus_ayah","hft_ref":"hft_83996f35d14d7ed254c6","item_id":"baseline-majority-mirrors-multiplicity","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline-majority-mirrors-multiplicity","support_id":"sup_7e8cdb3dc1726a583d23"}],"diagnostics":[],"lane_counts":{"global":9,"macro":8,"micro":3},"packet_summary":{"ayah_count":18,"focus_ref":"12:106","protocol":"focus-trace-pericope-lean-v1","split_root_mappings":[],"window":["12:94","12:95","12:96","12:97","12:98","12:99","12:100","12:101","12:102","12:103","12:104","12:105","12:106","12:107","12:108","12:109","12:110","12:111"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"valid_pericope_packet_unbound_response"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"12:106","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":11,"unstructured_record_count":0},"identity":{"ayah_ref":"12:106","lane":"micro","linguistic_source_ref":"12:106","surface_ref":"12:106","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"12:106","target_tokens":[["Onların",["12:106:1"]],["çoğu",["12:106:2"]],["Allah'a",["12:106:3"]],["ancak",["12:106:4"]],["ortak",["12:106:5"]],["koşarak",["12:106:6"]],["inanır",["12:106:7"]]],"text":"Onların çoğu Allah'a ancak ortak koşarak inanır."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":3,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":94,"ayah_to":111,"id":"s012-p06-094-111","label":"Family reunion and lessons of the story","number":6,"refs":["12:94","12:95","12:96","12:97","12:98","12:99","12:100","12:101","12:102","12:103","12:104","12:105","12:106","12:107","12:108","12:109","12:110","12:111"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:9","source_type":"word_analysis","support_id":"sup_03fd88b1a4a7b0c72d57","text":"{\"gloss_range\":\"independent plural pronoun starting the nominal state clause and repeating the earlier suffix referent\",\"prose\":\"{{ar:هُمْ}} ({{tr:hum}}) makes the subject of the ḥāl clause explicit. The same group first appeared as the suffix in {{ar:أَكْثَرُهُمْ}} ({{tr:aktharuhum}}), then returns as an independent pronoun before the final predicate. That shift matters: the ayah does not assign belief to one group and shirk to another; it makes the same majority stand visibly under both descriptions.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:هُمْ}} ({{tr:hum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:4","source_type":"word_analysis","support_id":"sup_0ee6dec4f43c0e6646db","text":"{\"gloss_range\":\"elative majority with attached plural suffix, serving as the subject of the belief verb\",\"prose\":\"{{ar:أَكْثَرُهُمْ}} ({{tr:aktharuhum}}) does more than count. The elative with its suffix makes the subject the greater part of an already implied group, and the singular verb treats that majority as one collective actor. Its abundance-root pressure makes the compromised belief feel prevailing, while the majority refrain (12:21; 12:38; 12:103) moves from not knowing and not thanking to the sharper diagnosis here: most believe only under the condition of shirk.\",\"root_display\":\"{{ar:ك ث ر}} ({{tr:k-th-r}})\",\"root_gloss_range\":\"abundance, increase, outnumbering, and majority; here narrowed to the greater part of an unnamed referent group\",\"surface_display\":\"{{ar:أَكْثَرُهُمْ}} ({{tr:aktharuhum}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:9:suffix-to-independent-echo","source_type":"word_analysis","support_id":"sup_13d395f2354b42e5b4cb","text":"{\"blocking_evidence\":null,\"headline\":\"suffix returns as independent pronoun\",\"reader_payoff\":\"The reader hears and sees the earlier suffix become an overt pronoun, tightening the identity chain.\",\"reason\":\"The retained pronoun visibly repeats the earlier suffix referent and helps bind the circumstantial clause to the main clause.\",\"representative_source_ids\":[\"QF-243bb254\",\"QE-018779a1\",\"QP-22901111\",\"QB-6d4cb77d\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:6:belief-shirk-relational-center","source_type":"word_analysis","support_id":"sup_1b385d63674db62e56e6","text":"{\"blocking_evidence\":null,\"headline\":\"belief and shirk meet at the divine name\",\"reader_payoff\":\"The reader notices God as the relational center: the object of belief, the violated exclusivity, and the destination of the later call.\",\"reason\":\"The CRITICAL rows cite concrete same-surah relations at 12:38 and 12:108, and the local clause places belief in God before the shirk state.\",\"representative_source_ids\":[\"QI-0924b6c6\",\"QI-462db49d\",\"QI-70a99ab0\",\"QY-aa6bfffb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:8","source_type":"word_analysis","support_id":"sup_1dd5e56d2513bae5f35a","text":"{\"gloss_range\":\"circumstantial conjunction attaching the nominal state to the belief clause as simultaneous\",\"prose\":\"The second {{ar:وَ}} ({{tr:wa}}) is the ayah's simultaneity marker. It carries the following nominal sentence as a ḥāl state, so belief and shirk are not sequential stages but co-present conditions in the same subject. Its repeated sound also answers the opening {{ar:وَ}} ({{tr:wa}}): the first joins the ayah to the prior discourse, while this one binds the inner diagnosis to the belief claim.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:5","source_type":"word_analysis","support_id":"sup_1f66b8b724e36b06e951","text":"{\"gloss_range\":\"preposition attaching the belief verb to its named object and preserving the target before restriction\",\"prose\":\"{{ar:بِ}} ({{tr:bi-}}) makes the belief relation explicit by fastening the verb to {{ar:اللَّهُ}} ({{tr:Allāh}}) as its governed object phrase. That matters because the ayah does not erase the claimed relation to God; it lets the relation stand and then qualifies its condition through the exception clause. The fused phrase {{ar:بِٱللَّهِ}} ({{tr:bi-llāhi}}) also turns the signs of 12:105 toward the God they claim to acknowledge.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:بِ}} ({{tr:bi-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:6","source_type":"word_analysis","support_id":"sup_2f00f76296d0f29dde89","text":"{\"gloss_range\":\"proper divine name as the governed target of belief, made sharper by the later shirk predicate\",\"prose\":\"{{ar:اللَّهُ}} ({{tr:Allāh}}) fixes the belief relation on the proper divine name. The grammar makes the name the governed object of {{ar:بِ}} ({{tr:bi-}}), not part of the later predicate, so the shock is precise: the named One is acknowledged while partner-assignment still defines the same group. Worship and awe associations may color the name, but the local form remains the proper name rather than a common class noun. Same-surah links sharpen the contrast: non-association with God is declared in 12:38, and the call to God with disavowal of associators follows in 12:108.\",\"root_display\":\"{{ar:أ ل ه}} ({{tr:ʾ-l-h}})\",\"root_gloss_range\":\"proper divine naming with worship and awe associations; local sense is the proper name, not a generic deity noun\",\"surface_display\":\"{{ar:اللَّهُ}} ({{tr:Allāh}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:6:proper-divine-target","source_type":"word_analysis","support_id":"sup_4cb566a076c143f100df","text":"{\"blocking_evidence\":null,\"headline\":\"proper divine target of belief\",\"reader_payoff\":\"The reader sees that the ayah is not about generic deity-belief but about acknowledgment of the proper divine name under a compromised state.\",\"reason\":\"The noun is the governed complement of the preposition and is treated in the evidence as the proper divine name.\",\"representative_source_ids\":[\"QG-4f88cb21\",\"QG-a1e3a4af\",\"QS-5ae42a7b\",\"MS-402dda77\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:3","source_type":"word_analysis","support_id":"sup_503f7efc8f65ad501a20","text":"{\"gloss_range\":\"Form IV imperfect belief/trust directed by a bā-governed complement and qualified by the exception frame\",\"prose\":\"{{ar:يُؤْمِنُ}} ({{tr:yuʾminu}}) is the ayah's hinge. As a Form IV imperfect, it presents belief as an ongoing directed act, with {{ar:بِٱللَّهِ}} ({{tr:bi-llāhi}}) preserving the target and the later exception qualifying the mode. Because the singular verb agrees with the collective head {{ar:أَكْثَرُهُمْ}} ({{tr:aktharuhum}}), the majority is first heard as one grammatical actor before the final plural predicate distributes the diagnosis. The root field adds trust and security pressure, but local form and grammar keep the selected sense at directed belief; that trust-bond is then exposed as compromised by simultaneous partner-assignment. The same root also turns forward in 12:107, where claimed belief is answered by a question about false security.\",\"root_display\":\"{{ar:أ م ن}} ({{tr:ʾ-m-n}})\",\"root_gloss_range\":\"safety, trust, security, and affirming belief; here narrowed to Form IV directed belief/trust toward God\",\"surface_display\":\"{{ar:يُؤْمِنُ}} ({{tr:yuʾminu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:8:waw-al-haal-simultaneity","source_type":"word_analysis","support_id":"sup_57b7d20ca044d90d5728","text":"{\"blocking_evidence\":null,\"headline\":\"waw al-haal simultaneity\",\"reader_payoff\":\"The reader sees that the state of shirk is simultaneous with belief, not a later event.\",\"reason\":\"The particle introduces the nominal ḥāl sentence, and the attachment evidence explicitly analyzes the clause as circumstantial exception scope.\",\"representative_source_ids\":[\"QG-6e8a59fe\",\"MG-f2191e1b\",\"MT-8447cbc9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:2","source_type":"word_analysis","support_id":"sup_60d12cc3d51f2aaa2ad3","text":"{\"gloss_range\":\"negating particle governing the imperfect belief verb and preparing restriction\",\"prose\":\"{{ar:مَا}} ({{tr:mā}}) denies an unqualified reading of the ongoing belief verb before the exception arrives. Its force is not simple absence: with {{ar:إِلَّا}} ({{tr:illā}}), it builds a restriction frame in which belief is acknowledged only under the later state of being {{ar:مُشْرِكُونَ}} ({{tr:mushrikūn}}).\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:مَا}} ({{tr:mā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:10:sound-and-boundary-pressure","source_type":"word_analysis","support_id":"sup_6f56acdaa2a6dd9cc43d","text":"{\"blocking_evidence\":null,\"headline\":\"sound and boundary pressure\",\"reader_payoff\":\"The reader hears the final predicate arrive with heavier articulation and as an acoustic closure linked to the prior ayah.\",\"reason\":\"The sound rows are concrete and locally tied to the pronoun-predicate boundary and adjacent participial closures, so they survive as a secondary payoff.\",\"representative_source_ids\":[\"MS-26626a3f\",\"QF-011fd1b3\",\"QP-3b6ef6e0\",\"QP-acfddac7\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:2:present-negation-of-belief","source_type":"word_analysis","support_id":"sup_73dbbae9d8a110522223","text":"{\"blocking_evidence\":null,\"headline\":\"present negation over imperfect belief\",\"reader_payoff\":\"The reader sees that the negation targets the ongoing quality of belief, not a closed past report.\",\"reason\":\"The particle directly negates the imperfect verb in the main clause, supporting the CRITICAL claim about present, evaluated belief.\",\"representative_source_ids\":[\"QG-8f65c2aa\",\"QG-eb9ea75a\",\"QS-1cc12bda\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"12:106:7:1","source_type":"qac_morpheme","support_id":"sup_74e7789a797b6b568dff","text":"{\"lemma_ar\":\"مُشْرِك\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|(IV)|LEM:mu$orik|ROOT:$rk|MP|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"12:106:7:1\",\"qac_word_ref\":\"12:106:7\",\"root_ar\":\"ش ر ك\",\"surface_ar\":\"مُّشْرِكُونَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:7:controlled-parse-ambiguity","source_type":"word_analysis","support_id":"sup_7576fd0039c6ed51c7e6","text":"{\"blocking_evidence\":null,\"headline\":\"exception versus restrictive manner\",\"reader_payoff\":\"The reader can register the parse tension without letting it unsettle the local conclusion that belief is qualified by simultaneous shirk.\",\"reason\":\"The rows preserve a real parse nuance, but both routes are narrowed by the same locally licensed circumstantial clause.\",\"representative_source_ids\":[\"QF-56dc5e11\",\"QY-725d102b\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:7:restrictive-haal-hinge","source_type":"word_analysis","support_id":"sup_7b6d1701af36fc5a46ae","text":"{\"blocking_evidence\":null,\"headline\":\"restrictive circumstantial hinge\",\"reader_payoff\":\"The reader notices that the exception particle changes the issue from whether belief exists to what condition defines it.\",\"reason\":\"The attachment evidence strongly licenses the following nominal sentence as the exception scope, supporting the CRITICAL restriction and ḥāl claims.\",\"representative_source_ids\":[\"QG-e1f6b5fa\",\"MG-a469b31e\",\"QI-6de40d1b\",\"QT-5af6b044\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:7","source_type":"word_analysis","support_id":"sup_7ee6731272bcd2b81959","text":"{\"gloss_range\":\"exception and restriction particle introducing the circumstantial state clause\",\"prose\":\"{{ar:إِلَّا}} ({{tr:illā}}) is the hinge that prevents the first clause from settling as simple nonbelief or simple belief. With the earlier {{ar:مَا}} ({{tr:mā}}), it restricts the surviving belief to one condition: belief occurs while the same people are {{ar:مُشْرِكُونَ}} ({{tr:mushrikūn}}). The particle can be heard through exception or restrictive manner, but the local ḥāl clause keeps the payoff stable: the ayah defines the quality of belief.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:إِلَّا}} ({{tr:illā}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:4:abundance-pressure","source_type":"word_analysis","support_id":"sup_86cb6665df9fb6aa11ee","text":"{\"blocking_evidence\":null,\"headline\":\"abundance root pressure\",\"reader_payoff\":\"The reader feels the majority as a swelling prevailing condition, while local form keeps the sense at “most of them.”\",\"reason\":\"V4 preserves abundance and outnumbering branches for the root, but the local elative construction selects majority rather than wealth, boasting, or other branch senses.\",\"representative_source_ids\":[\"QS-601abe20\",\"QS-b80d7b69\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:3:collective-subject-agreement","source_type":"word_analysis","support_id":"sup_8795b7386a7878badd05","text":"{\"blocking_evidence\":null,\"headline\":\"singular verb with collective majority subject\",\"reader_payoff\":\"The reader sees the majority handled as one grammatical subject before its members are diagnosed by the final plural predicate.\",\"reason\":\"The attachment evidence identifies the following majority word as subject, and the singular verb agreement coheres with the collective elative head.\",\"representative_source_ids\":[\"QG-4ddd7613\",\"MG-45004a88\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:1:paired-waw-functions","source_type":"word_analysis","support_id":"sup_9af68330e43307fc3f38","text":"{\"blocking_evidence\":null,\"headline\":\"paired waw functions\",\"reader_payoff\":\"The reader notices that the repeated conjunction sound does two jobs: this one resumes the discourse, while the later one internalizes the state.\",\"reason\":\"The first conjunction belongs to the main clause, while the later conjunction is analyzed as circumstantial; the contrast is locally supported by clause structure.\",\"representative_source_ids\":[\"MT-af8be16a\",\"QE-5ccef955\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"12:106:4:2","source_type":"qac_morpheme","support_id":"sup_a10a3004c97b9e5b8cea","text":"{\"lemma_ar\":\"ٱللَّه\",\"morph_features\":\"STEM|POS:PN|LEM:{ll~ah|ROOT:Alh|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"PN\",\"qac_ref\":\"12:106:4:2\",\"qac_word_ref\":\"12:106:4\",\"root_ar\":\"ء ل ه\",\"surface_ar\":\"ٱللَّهِ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:6:worship-awe-name-pressure","source_type":"word_analysis","support_id":"sup_a5d8885864138a0df637","text":"{\"blocking_evidence\":null,\"headline\":\"worship and awe pressure in the name\",\"reader_payoff\":\"The reader feels why divided allegiance is jarring, while local grammar keeps the word as the proper divine name.\",\"reason\":\"The derivational dispute and worship/awe field can color the name, but they do not replace the locally selected proper-name function.\",\"representative_source_ids\":[\"QS-1964b29c\",\"QS-65e4cd4a\",\"QF-27846d33\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"12:106:2:1","source_type":"qac_morpheme","support_id":"sup_a892bf53d8c506defbf6","text":"{\"lemma_ar\":\"ءَامَنَ\",\"morph_features\":\"STEM|POS:V|IMPF|(IV)|LEM:'aAmana|ROOT:Amn|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"12:106:2:1\",\"qac_word_ref\":\"12:106:2\",\"root_ar\":\"ء م ن\",\"surface_ar\":\"يُؤْمِنُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:10:nominal-predicate-identity-state","source_type":"word_analysis","support_id":"sup_aae64b2ee109340d8645","text":"{\"blocking_evidence\":null,\"headline\":\"nominal predicate identity-state\",\"reader_payoff\":\"The reader sees the final word as a stable state qualifying belief, not as a separate action or object.\",\"reason\":\"The word is the nominative predicate of the nominal ḥāl sentence, and the active participle supports ongoing state rather than completed past event.\",\"representative_source_ids\":[\"QG-c139f491\",\"QG-c6ed608c\",\"MG-d8cf18c0\",\"MF-45c6e7a8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:3:directed-imperfect-belief","source_type":"word_analysis","support_id":"sup_ab84f17fba8c2ac2dcfe","text":"{\"blocking_evidence\":null,\"headline\":\"directed imperfect belief clause\",\"reader_payoff\":\"The reader notices that belief is an ongoing act with a named target and an immediate restriction, not a vague religious label.\",\"reason\":\"The verb is an IV imperfect with a bā-governed complement and an exception scope, so the CRITICAL grammar and valency claims are locally licensed.\",\"representative_source_ids\":[\"QG-4b304d1d\",\"QG-ab84d201\",\"MS-1fb427e5\",\"QT-8c028748\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:3:trust-root-pressure","source_type":"word_analysis","support_id":"sup_b254db745982f75f6422","text":"{\"blocking_evidence\":null,\"headline\":\"trust and security root pressure\",\"reader_payoff\":\"The reader feels belief as a trust-bond toward God, while the local Form IV prevents replacing that with a bare safety sense.\",\"reason\":\"The CRITICAL root-family rows preserve real trust and security pressure, but local morphology selects Form IV directed belief rather than the bare Form I sense of being safe.\",\"representative_source_ids\":[\"QS-163dac06\",\"QS-cef4b955\",\"QF-b8612966\",\"MF-d6b2fcc4\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:10","source_type":"word_analysis","support_id":"sup_bd1863335182d950f784","text":"{\"gloss_range\":\"Form IV active participle predicate naming an ongoing partner-assigning identity-state\",\"prose\":\"{{ar:مُشْرِكُونَ}} ({{tr:mushrikūn}}) is the diagnostic seal of the ayah. As a nominative plural active participle, it completes the nominal ḥāl clause as a standing identity-state, not a second event or an object of the belief verb. The root keeps the concrete image of sharing or partnership in the background, but local form and context narrow it to theological partner-assignment against the named relation to God. The ending also makes the state distributed across the majority, while same-surah echoes sharpen the indictment: 12:38 denies association with God, and 12:108 answers this label with disavowal of being among the associators.\",\"root_display\":\"{{ar:ش ر ك}} ({{tr:sh-r-k}})\",\"root_gloss_range\":\"sharing, partnership, association, partner-attribution, and related concrete branches; here narrowed to theological partner-assignment with partnership imagery still felt\",\"surface_display\":\"{{ar:مُشْرِكُونَ}} ({{tr:mushrikūn}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:10:group-bound-participial-form","source_type":"word_analysis","support_id":"sup_c76782e3ea2f64283cf5","text":"{\"blocking_evidence\":null,\"headline\":\"group-bound participial form\",\"reader_payoff\":\"The reader notices the predicate applied across the collective as an ongoing plural identity, not as an abstract noun.\",\"reason\":\"The masculine plural nominative participle agrees with the explicit pronoun and fits the active-participle profile rather than a completed finite form.\",\"representative_source_ids\":[\"QG-82a2341a\",\"QF-732c15bb\",\"QF-e22dd4f4\",\"QI-760e6526\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:4:majority-refrain-and-boundary","source_type":"word_analysis","support_id":"sup_c98ce80c50d87519b1b9","text":"{\"blocking_evidence\":null,\"headline\":\"majority refrain and boundary chain\",\"reader_payoff\":\"The reader notices the majority-failure refrain (12:21; 12:38; 12:103) concentrating here into compromised belief.\",\"reason\":\"The CRITICAL rows cite concrete same-surah and cross-surah majority patterns, and the local suffix keeps the boundary plural connected to this subject.\",\"representative_source_ids\":[\"QI-93ac4f86\",\"QE-040e533d\",\"QB-0bf3cc09\",\"QY-f6cdd36c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:1","source_type":"word_analysis","support_id":"sup_cce57876515591a7bc0c","text":"{\"gloss_range\":\"resumptive conjunction opening a fresh but connected diagnostic assertion\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) carries the discourse over from the sign-scene of 12:105 into a fresh theological diagnosis. It joins the new clause to the prior censure, but its payoff is not merely additive: the same opening sound will be answered by the later circumstantial {{ar:وَ}} ({{tr:wa}}), so the ayah moves from resumed observation to an internal state.\",\"root_display\":\"— (no root)\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:8:repeated-waw-boundary-frame","source_type":"word_analysis","support_id":"sup_d65de5975d158f699044","text":"{\"blocking_evidence\":null,\"headline\":\"repeated waw and boundary frame\",\"reader_payoff\":\"The reader hears the repeated conjunction as cohesion while its function changes from discourse resumption to state-linking.\",\"reason\":\"The two conjunctions occupy different licensed clause functions, and the boundary rows coherently connect the prior visible aversion to this inner state diagnosis.\",\"representative_source_ids\":[\"QE-58abd90d\",\"QB-f10813db\",\"QY-38365937\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:9:explicit-same-subject","source_type":"word_analysis","support_id":"sup_d6a448b665fb20ee5d33","text":"{\"blocking_evidence\":null,\"headline\":\"explicit same subject of state clause\",\"reader_payoff\":\"The reader notices that believers and associators are grammatically the same set.\",\"reason\":\"The pronoun is the subject of the nominal ḥāl clause and is syntactically tied back to the majority subject.\",\"representative_source_ids\":[\"QG-ba8f8c62\",\"MG-322fd562\",\"QS-54d8a55d\",\"MT-4614d19e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:5:governed-belief-target","source_type":"word_analysis","support_id":"sup_d8959642929c8bb949f7","text":"{\"blocking_evidence\":null,\"headline\":\"governed belief target\",\"reader_payoff\":\"The reader notices that the target of belief is grammatically explicit before the ayah exposes the compromised mode.\",\"reason\":\"The preposition is syntactically forced as the governor of the divine-name complement, preserving the belief target while the exception qualifies the state.\",\"representative_source_ids\":[\"QG-0fce2be5\",\"MG-5b7fe0bf\",\"MS-7dd2ed60\",\"QT-a014a853\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:5:fused-attachment-and-boundary","source_type":"word_analysis","support_id":"sup_d973303611d5c5752c62","text":"{\"blocking_evidence\":null,\"headline\":\"fused attachment and sign boundary\",\"reader_payoff\":\"The reader hears and sees the object phrase as tightly attached, while the prior signs become evidence pointing toward that named object.\",\"reason\":\"The proclitic attachment is visible in the surface phrase, and the boundary row coherently links the prior signs to the present belief object without changing the local grammar.\",\"representative_source_ids\":[\"QF-d1d8e662\",\"QP-b4412eac\",\"QB-2eea2149\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:10:partner-allocation-root-image","source_type":"word_analysis","support_id":"sup_dc973887020a547cc0c0","text":"{\"blocking_evidence\":null,\"headline\":\"partner-allocation root image\",\"reader_payoff\":\"The reader feels shirk as assigning a share or partner, while local context keeps the theological association sense selected.\",\"reason\":\"V4 supports partnership and associating-with-God branches; the local participle selects theological partner-attribution while preserving the divided-allocation image.\",\"representative_source_ids\":[\"QS-4ec566ca\",\"QS-6b763a6b\",\"QS-9847d911\",\"MS-20696509\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:10:belief-shirk-opposition-and-echoes","source_type":"word_analysis","support_id":"sup_ded6e1e77078aa405f92","text":"{\"blocking_evidence\":null,\"headline\":\"belief-shirk opposition and same-surah echoes\",\"reader_payoff\":\"The reader sees the final predicate as the ayah’s closing indictment and as the foil for the non-shirk declarations at 12:38 and 12:108.\",\"reason\":\"The rows provide concrete references and the local structure pairs belief and shirk inside one subject, making the intertextual and structural payoff coherent.\",\"representative_source_ids\":[\"QI-eeb48f85\",\"QI-edb3c1f0\",\"QI-c657bc5a\",\"QY-705f5d20\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:4:partitive-majority-subject","source_type":"word_analysis","support_id":"sup_e875a100c772f574a330","text":"{\"blocking_evidence\":null,\"headline\":\"partitive majority as subject\",\"reader_payoff\":\"The reader sees that the ayah speaks about the dominant part of a referent group, not an undefined “many.”\",\"reason\":\"The word is tagged as an elative subject, and the suffix is locally tied to the later independent pronoun.\",\"representative_source_ids\":[\"QG-07c4ae82\",\"QG-16f5f441\",\"MG-369a22fb\",\"QT-65dbacaa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:2:ma-illa-restriction","source_type":"word_analysis","support_id":"sup_eea741b775b3b80227cd","text":"{\"blocking_evidence\":null,\"headline\":\"negation-exception restriction\",\"reader_payoff\":\"The reader recognizes that the ayah is defining the only surviving mode of belief, not merely saying that most people do not believe.\",\"reason\":\"The later exception particle and circumstantial clause are strongly licensed, so the negation prepares a restrictive architecture rather than a stand-alone denial.\",\"representative_source_ids\":[\"QI-ab0ad7a3\",\"QT-b9b3d36c\",\"MT-a6b4a451\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:3:formula-and-forward-echo","source_type":"word_analysis","support_id":"sup_eecf61dab7069bab3373","text":"{\"blocking_evidence\":null,\"headline\":\"belief formula complicated and carried forward\",\"reader_payoff\":\"The reader notices that familiar belief-in-God language is reused in a marked way and then reopened as false-security language in 12:107.\",\"reason\":\"The rows give concrete same-surah and cross-surah references, and the local clause indeed combines the familiar belief construction with the shirk qualifier.\",\"representative_source_ids\":[\"QI-28c798cd\",\"QI-bdc661e7\",\"QE-c29f7040\",\"QB-6243715e\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"12:106:1:resumptive-diagnostic-pivot","source_type":"word_analysis","support_id":"sup_f51fe0510efafb8fed09","text":"{\"blocking_evidence\":null,\"headline\":\"resumptive pivot into diagnosis\",\"reader_payoff\":\"The reader hears the ayah begin as a connected answer to the prior sign-censure, not as a disconnected maxim.\",\"reason\":\"The particle is licensed as a conjunction opening the negated verbal clause, and the CRITICAL rows converge on resumption from 12:105 into a universal diagnostic frame.\",\"representative_source_ids\":[\"QG-f28b59bd\",\"MG-ff447030\",\"QT-88c56ac9\",\"QB-fd1e0ff9\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"12:106:3:1","source_type":"qac_morpheme","support_id":"sup_fae92d43e1057315d172","text":"{\"lemma_ar\":\"أَكْثَر\",\"morph_features\":\"STEM|POS:N|LEM:>akovar|ROOT:kvr|MS|NOM\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"12:106:3:1\",\"qac_word_ref\":\"12:106:3\",\"root_ar\":\"ك ث ر\",\"surface_ar\":\"أَكْثَرُ\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا يُؤْمِنُ أَكْثَرُهُم بِٱللَّهِ إِلَّا وَهُم مُّشْرِكُونَ","ayah_ref":"12:106"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000047/B001","root_000054/B002","root_000791/B001","root_000791/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000054","role":"Heart-settling assent supplies a genuinely affirmative component rather than total unbelief.","root":"ء م ن","source_ref":"12:106","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000047","role":"The worship-and-object relation fixes God as the acknowledged divine referent.","root":"ء ل ه","source_ref":"12:106","source_word_indices":["4"]},{"branch_id":"B001","mapped_root_id":"root_000791","role":"Participation in a jointly held matter supplies the functional split of allegiance.","root":"ش ر ك","source_ref":"12:106","source_word_indices":["7"]},{"branch_id":"B002","mapped_root_id":"root_000791","role":"The theological branch bounds the sharing mechanism within association with God.","root":"ش ر ك","source_ref":"12:106","source_word_indices":["7"]}],"changed_reading":{"after":"Most retain real God-directed assent, but it operates inside a concurrently shared allocation of worship, reliance, or agency.","before":"Most simply lack belief in God because they are associators."},"confidence":"strong","focus_anchor":"The exception construction holds God-directed belief at word 2 and association at word 7 together as concurrent states.","mechanism":"Heart-settling assent is present, but the divine relation is organized as shared participation. The focus diagnoses partitioned allegiance rather than simple absence of acknowledgment.","model_id":"baseline-partitioned-assent"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-partitioned-assent","source_type":"hft","support_id":"sup_d26586b0c72196ec6a72","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا يُؤْمِنُ أَكْثَرُهُم بِٱللَّهِ إِلَّا وَهُم مُّشْرِكُونَ","ayah_ref":"12:106"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000054/B001","root_000791/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000054","role":"Settled safety and trust turn belief into an operative placement of security.","root":"ء م ن","source_ref":"12:106","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000791","role":"Joint participation distributes that security relation among multiple claimants.","root":"ش ر ك","source_ref":"12:106","source_word_indices":["7"]}],"changed_reading":{"after":"Belief is also entrusted safety, and its defect is diversification across God and retained backups.","before":"Belief is only propositional acknowledgment, with association added as a separate doctrine."},"confidence":"medium","focus_anchor":"The belief verb at word 2 also carries security and trust, while word 7 names participation with another.","mechanism":"The focus can be heard as a trust arrangement: God is a source of safety, but not the sole source. Association keeps supplementary guarantors inside the security system.","model_id":"baseline-distributed-security"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-distributed-security","source_type":"hft","support_id":"sup_d6286bd3523f9c526fce","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَمَا يُؤْمِنُ أَكْثَرُهُم بِٱللَّهِ إِلَّا وَهُم مُّشْرِكُونَ","ayah_ref":"12:106"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000791/B008","root_001286/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001286","role":"Numerical overpowering makes majority status capable of functioning as social proof.","root":"ك ث ر","source_ref":"12:106","source_word_indices":["3"]},{"branch_id":"B008","mapped_root_id":"root_000791","role":"A judgment that is not one supplies the internal analogue to the external multitude.","root":"ش ر ك","source_ref":"12:106","source_word_indices":["7"]}],"changed_reading":{"after":"Numerical mass can itself become a co-authority that keeps judgment divided.","before":"The majority expression is only a statistic about how many associate."},"confidence":"exploratory","focus_anchor":"The majority quantifier at word 3 stands in the same clause as the shared-allegiance predicate at word 7.","mechanism":"External numerical plurality and internal plurality of authority echo one another. Mass can stabilize a non-unitary judgment instead of evidencing truth.","model_id":"baseline-majority-mirrors-multiplicity"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline-majority-mirrors-multiplicity","source_type":"hft","support_id":"sup_7e8cdb3dc1726a583d23","trust":"legacy_unbound"}]}
</lane_packet_json>
