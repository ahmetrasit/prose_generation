# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **107:7**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s107-regular-20260911/s107/107_7/micro.discovery.json` and modify nothing
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
  "ayah_ref": "107:7",
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
{"analysis_context":{"analysis_id":"s107-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"107:7","host_surah":107,"lane_context_refs":[],"ordered_context_refs":["107:0","107:1","107:2","107:3","107:4","107:5","107:6","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Bu dal yaş, savaş, ağaç, hayvan sürüsü, beden bölgesi veya yer adı anlamlarını kapsamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001064/B001","candidate_links":[{"candidate_id":"cand_1ada1cb61f24493b6fb0","lane":"micro"},{"candidate_id":"cand_404e78531ed488d25bde","lane":"micro"},{"candidate_id":"cand_130dc8603b8ab2890b85","lane":"micro"},{"candidate_id":"cand_d2a97663f2abb528cc27","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَاعُون","morph_features":"STEM|POS:N|LEM:maAEuwn|ROOT:mEn|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:7:2:2","qac_word_ref":"107:7:2","surface_ar":"مَاعُونَ"}],"gloss":"yardım, destek ve dayanışma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi, topluluk veya şey, başka birinin işini yapmasına destek olur ya da o işte kullanılabilecek bir destek oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yapıya bağlı kullanımlarda kişi başkasından yardım ister veya taraflar birbirlerine yardım ederek birlikte hareket eder."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı anlam alanı, insanlara çok yardım eden kişiyi ve yardım etme eylemini adlandıran türemiş biçimleri de içerir."}}],"root_ar":"م ع ن","root_id":"root_001064","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yardım sağlama çekirdeği ile karşılıklı yardımlaşma yönünü birlikte veren genel kavram karşılığıdır.","boundary_detail":"Bu dal yaş, savaş, ağaç, hayvan sürüsü, beden bölgesi veya yer adı anlamlarını kapsamaz.","branch_image_ar":"الإعانة والمظاهرة","concept_gloss":"yardım, destek ve dayanışma","contextual_glosses":[{"applicability":"Bir kişinin belirli birinden destek talep ettiği yapıya bağlı kullanımda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Destek talep eden kişi ile yardım kaynağı arasındaki yönü korur."},"facet_ids":["F002"],"text":"yardım istemek","usage_role":"contextual"},{"applicability":"Birden çok tarafın karşılıklı destek vererek birlikte hareket ettiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklılık ve ortak hareket etme özelliklerini eksiksiz biçimde korur."},"facet_ids":["F002"],"text":"birbirine yardım etmek","usage_role":"contextual"}],"definition":"Bir kişinin, topluluğun ya da aracın bir işi gerçekleştirmede başkasına güç, destek veya kolaylık sağlamasıdır. Bu çekirdek, yardım istemeyi, birlikte karşılıklı yardım etmeyi ve yardımsever kişi nitelemesini de türemiş kullanımlar olarak kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi, topluluk veya şey, başka birinin işini yapmasına destek olur ya da o işte kullanılabilecek bir destek oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Yapıya bağlı kullanımlarda kişi başkasından yardım ister veya taraflar birbirlerine yardım ederek birlikte hareket eder."},{"facet_id":"F003","role":"extension","statement":"Aynı anlam alanı, insanlara çok yardım eden kişiyi ve yardım etme eylemini adlandıran türemiş biçimleri de içerir."}],"identity_rationale":"Dalın kaynak ifadesi, yardım sağlayan kişi ya da şeyi, yardım etme eylemini, yardım istemeyi ve karşılıklı yardımlaşmayı aynı anlam alanında açıkça toplar. Geçici çerçeve bu çekirdeği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"yardım, destek veya işe yarayan yardımcı şey"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yardım etme, destek sağlama"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yardım etti, destek oldu"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"yardımlaştı veya destek verdi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"birinden yardım istedi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"birbirine yardım etti, dayanıştı"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"çok yardımsever, sıkça yardım eden"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"yardım, destek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"yardım anlamındaki tekil biçim veya yardım sözünün çoğulu"}],"lexicalization_note":"Tanım, yalın yardım ve destek çekirdeğini korurken yardım isteme ve karşılıklı yardımlaşma gibi yapıya bağlı kullanımları ayrı yönler olarak sınırlar.","neighbor_coverage_note":"Bütün aday komşular değerlendirildi; en yararlı sınırlar maddi yardım, yardım ile izleme birlikteliği ve acil kurtarma üzerinden gösterildi, kalanlar daha uzak senaryo ortaklıkları veya bu kökün ayrı dallarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel yardım alanıdır; komşu dal ise bu desteğin verme ve bağış gibi belirli maddi gerçekleşmelerini öne çıkarır.","focus_only":"Odak dal, maddi olmayan desteği, yardım istemeyi ve karşılıklı yardımlaşmayı da kapsar.","gloss":"vererek yardım etme","neighbor_only":"Komşu dal, yardımın özellikle verme, bağış veya yolcuya gereç sağlama yoluyla gerçekleşmesini kapsar.","neighbor_ref":"root_000580/B001","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir kişinin başkasının işini kolaylaştıran bir destek sağlaması vardır."},{"boundary_match":"partial","distinction":"Komşu dalın izleme ve kalıplaşmış bağlılık yönleri odak dalın çekirdeğinde yoktur; odak dalın yardım isteme ve karşılıklılık kapsamı da daha geniştir.","focus_only":"Odak dal, yardımcı şeyleri, yardım talebini ve tarafların karşılıklı desteğini açıkça içerir.","gloss":"yardım etme ve izleme","neighbor_only":"Komşu dal, bir işte peşinden gitme ve belirli bir bağlılık ya da dua kalıbını da içerir.","neighbor_ref":"root_000707/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir kişiye veya işe destek olma anlamında belirgin biçimde kesişir."},{"boundary_match":"partial","distinction":"İmdat dalı çağrı ve acil kurtarma durumunu gerektirir; odak dalda böyle bir aciliyet koşulu bulunmaz.","focus_only":"Odak dal olağan işlerde sağlanan desteği, yardım istemeyi ve dayanışmayı kapsar.","gloss":"imdat ve kurtarma","neighbor_only":"Komşu dal, çağrı üzerine sıkıntıdan kurtarma veya acil imdada yetişme koşuluyla sınırlıdır.","neighbor_ref":"root_000855/B003","relation_type":"near_synonym","shared_zone":"Her iki dalda da ihtiyaç içindeki birine etkili destek sağlama bulunur."}],"source_phrase_ar":"كل شيء استعنت به أو أعانك فهو عونك (ayn); العون الظهيرة على الأمر والمعونة الإعانة واستعنت بفلان فأعانني وعاونني وتعاون القوم (sihah); كل شيء أعانك فهو عون لك وأعنته إعانة واستعنت به وعاونته وقد تعاونا (tahdhib); العون المعاونة والمظاهرة والتعاون التظاهر والاستعانة طلب العون (mufradat)","source_summary":"Kaynakların ortak çekirdeği yardım, destek sağlama, başkasından destek isteme ve tarafların birbirine yardım etmesidir; yardım sağlayan şey de bu alanın içinde değerlendirilir.","sources":["AY","SI","TA","MU"],"what_is_ar":"العون والمعونة والإعانة والاستعانة والتعاون والتظاهر على الأمر","what_is_not_ar":"ليس العوان في السن ولا العانة"},"support_links":["sup_56bae57de5724874af19","sup_6d79827585e756defcb3","sup_dcb50e4cfd223759194e","sup_f01fe84a10b06f030164"]},{"boundary":"Anlam sayısal bir yaş ortalaması değil, gençlik ile ileri yaşlılık arasındaki göreli evredir.","branch_kind":"mixed_non_bare","branch_ref":"root_001064/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَاعُون","morph_features":"STEM|POS:N|LEM:maAEuwn|ROOT:mEn|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:7:2:2","qac_word_ref":"107:7:2","surface_ar":"مَاعُونَ"}],"gloss":"yaşça orta evrede olan","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlı, kendi türünün gençlik ve ileri yaşlılık uçları arasında bulunan orta yaş evresindedir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kadın kullanımında orta yaş niteliğine evlenmiş olma veya yaşlılığa yaklaşmış olma çağrışımı eklenebilir."}}],"root_ar":"م ع ن","root_id":"root_001064","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Gençlik ile ileri yaşlılık arasındaki göreli evreyi türden bağımsız biçimde anlatan çekirdek karşılıktır.","boundary_detail":"Anlam sayısal bir yaş ortalaması değil, gençlik ile ileri yaşlılık arasındaki göreli evredir.","branch_image_ar":"العَوان بين السنين","concept_gloss":"yaşça orta evrede olan","contextual_glosses":[{"applicability":"Özellikle bir hayvanın iki yaş ucu arasındaki konumunu açıklamak için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki yaş ucu arasında bulunma koşulunu açıkça korur."},"facet_ids":["F001"],"text":"ne genç ne yaşlı","usage_role":"explanatory"},{"applicability":"Kadın için kullanılan özel yapıda temel yaş değerini verir; bağlam ek çağrışımları belirleyebilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bazı tanıklıklardaki evlenmişlik veya yaşlılığa yaklaşma çağrışımını tek başına göstermez.","preserves":"Kadının gençlik ile ileri yaşlılık arasındaki yaş konumunu korur."},"facet_ids":["F001","F002"],"text":"orta yaşlı kadın","usage_role":"contextual"}],"definition":"Bir canlıyı yaş bakımından küçük ya da genç olmayan, fakat henüz ileri yaşlı da sayılmayan orta evrede nitelemektir. Kadın için kullanılan özel biçim, bağlama göre evlenmiş olmayı veya daha ileri bir yaş çağrışımını da taşıyabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlı, kendi türünün gençlik ve ileri yaşlılık uçları arasında bulunan orta yaş evresindedir."},{"facet_id":"F002","role":"source_variant","statement":"Kadın kullanımında orta yaş niteliğine evlenmiş olma veya yaşlılığa yaklaşmış olma çağrışımı eklenebilir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Yaş dışındaki gelişim ve yetkinlik alanlarını da gereksiz biçimde anlama ekler.","collision":null,"fit":"broadening","loses":null,"preserves":"Gençlikten çıkmış olma düşüncesini kısmen korur."},"text":"tam olgun"}],"identity_rationale":"Kaynak ifadesinin ortak çekirdeği küçük ile ileri yaşlı arasındaki orta yaş evresidir ve sığır, at ile kadın örnekleri bunu destekler. Bununla birlikte kadın kullanımında evlilik durumu veya ileri yaş çağrışımı da bulunduğundan geçici çerçeve bu özel sınırla nitelendirilmelidir.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yaşça orta evrede olan"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"ne genç ne yaşlı sığır"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"orta yaşlı veya evlenmiş kadın"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"orta yaşlı at"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"orta yaşta olanlar"}],"lexicalization_note":"Tanım genel orta yaş niteliğini hayvan ve insanla kurulan özel yapılardan ayırır; bu yapıların koşulları yalın kullanıma genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; orta konum, yaşın tamamlanması ve kadına özgü yaş eşiği en açıklayıcı karşılaştırmalardır, öteki adaylar farklı gelişim aşamalarını veya ayrı kök dallarını gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal türün yaş evresine bağlı bir nitelemedir; komşu dal ise yaşla sınırlı olmayan genel bir ölçü, zaman veya konum ortalığıdır.","focus_only":"Odak dal yalnızca canlıların yaş bakımından genç ile ileri yaşlı arasındaki evresini belirtir.","gloss":"yarıya veya ortaya ulaşma","neighbor_only":"Komşu dal miktar, zaman veya yer bakımından herhangi bir şeyin yarısına ya da ortasına ulaşmasını kapsar.","neighbor_ref":"root_001511/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da iki uç arasında bir orta konum düşüncesi vardır."},{"boundary_match":"field_only","distinction":"Orta evre ile gelişimin tamamlanması aynı sınır değildir; biri iki uç arasındaki konumu, diğeri belirli bir sona erişmeyi anlatır.","focus_only":"Odak dal, canlıyı henüz ileri yaşlı olmadan orta yaş evresinde gösterir.","gloss":"yaşın tamamlanması","neighbor_only":"Komşu dal, hayvanın yaş ve gelişim bakımından belirli bir tamamlanma noktasına varmasını belirtir.","neighbor_ref":"root_000517/B004","relation_type":"same_field","shared_zone":"İki dal da hayvanın yaşına bağlı gelişim evrelerini sınıflandırır."},{"boundary_match":"partial","distinction":"Odak dal göreli ve türler arası bir orta evredir; komşu dal kadınla ve yaklaşık belirli bir yaş eşiğiyle sınırlıdır.","focus_only":"Odak dal kadın dışında sığır ve atı da kapsayan göreli bir orta yaş niteliğidir.","gloss":"yaklaşık kırk beş yaşındaki kadın","neighbor_only":"Komşu dal yalnızca kadını ve yaklaşık belirli bir ileri yaşı adlandırır.","neighbor_ref":"root_000733/B012","relation_type":"near_neighbor","shared_zone":"Her iki dal kadınların gençlik sonrasındaki yaş evresini niteleyebilir."}],"source_phrase_ar":"العوان البقرة النصف في سنها ويقال للمرأة النصف عوان (ayn); العوان النصف في سنها من كل شيء وبقرة عوان لا فارض مسنة ولا بكر صغيرة (sihah); العوان النصف التي بين الفارض وهي المسنة وبين البكر وهي الصغيرة ويقال فرس عوان وخيل عون (tahdhib); العوان المتوسط بين السنين وجعل كناية عن المسنة من النساء (mufradat)","source_summary":"Kaynaklar niteliği genç ile ileri yaşlı arasındaki orta yaş olarak ortaklaştırır; sığır ve at örnekleri açıkken kadın kullanımında orta yaş, evlenmişlik veya yaşlılığa yaklaşma yorumları yan yana bulunur.","sources":["AY","SI","TA","MU"],"what_is_ar":"العوان لما كان نصفا أو متوسطا في السن كالبقرة والمرأة والفرس","what_is_not_ar":"ليس العون بمعنى الإعانة ولا الحرب العوان"},"support_links":[]},{"boundary":"Bu anlam yalnızca savaş nitelemesinde geçerlidir; genel tekrar ya da genel savaş adı değildir.","branch_kind":"collocation","branch_ref":"root_001064/B003","candidate_links":[{"candidate_id":"cand_5cb51a061dcac9e3a68c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَاعُون","morph_features":"STEM|POS:N|LEM:maAEuwn|ROOT:mEn|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:7:2:2","qac_word_ref":"107:7:2","surface_ar":"مَاعُونَ"}],"gloss":"yinelenmiş veya öncülü olan savaş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Savaşın öncesinde başka bir savaş vardır ya da aynı savaşta çatışma birden çok kez gerçekleşmiştir."}}],"root_ar":"م ع ن","root_id":"root_001064","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Daha önceki bir savaşın ardından gelen ya da çatışması tekrar eden savaş nitelemesini tam olarak verir.","boundary_detail":"Bu anlam yalnızca savaş nitelemesinde geçerlidir; genel tekrar ya da genel savaş adı değildir.","branch_image_ar":"الحرب العَوان","concept_gloss":"yinelenmiş veya öncülü olan savaş","contextual_glosses":[{"applicability":"Öncesinde başka bir savaş bulunduğunun açık olduğu bağlamlarda doğal ve kısa bir açıklamadır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tek bir savaş içindeki çatışmanın defalarca yinelenmesi seçeneğini tek başına belirtmez.","preserves":"Savaşın başlangıç niteliğinde olmadığını açıkça korur."},"facet_ids":["F001"],"text":"ilk olmayan savaş","usage_role":"explanatory"}],"definition":"Daha önce bir savaşın yaşandığı veya çatışmanın birden çok kez yinelendiği, bu nedenle ilk ve yeni olmayan savaştır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Savaşın öncesinde başka bir savaş vardır ya da aynı savaşta çatışma birden çok kez gerçekleşmiştir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynakta zorunlu olmayan uzun süre koşulunu anlama ekler.","collision":"Süre bakımından uzun olan fakat ilk kez yaşanan bir savaşla karışır.","fit":"displacement","loses":"Önceki savaş veya tekrarlanan çatışma koşulunu ortadan kaldırır.","preserves":"Savaşın sürmüş olabileceği izlenimini sınırlı biçimde taşır."},"text":"uzun savaş"}],"identity_rationale":"Kaynak ifadesi bu niteliği daha önce bir savaşın yaşanmış olması veya aynı savaşın defalarca sürdürülmesiyle açıklar. Geçici çerçeve hem öncül savaş hem yinelenmiş çatışma koşulunu doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"daha önce yaşanmış ya da yinelenmiş savaş"}],"lexicalization_note":"Tanım yalnızca belirtilen savaş nitelemesine bağlıdır ve tekrarlanma anlamını kökün yalın bir anlamı olarak genellemez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel tekrar, başlangıçtan sonra yeniden yapma ve genel savaş alanı sınırı en yararlı üç karşılaştırmadır, kalanlar savaşın yeri, şiddeti veya başlaması gibi başka yönlerdir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal genel tekrar kavramıdır; odak dal ise bu yapıyı savaşın ilk olmaması koşuluna bağlayan özel bir nitelemedir.","focus_only":"Odak dal tekrarı yalnızca savaşın geçmişi veya yinelenmiş çatışması içinde belirtir.","gloss":"bir şeyi tekrar tekrar yapma","neighbor_only":"Komşu dal alma, kınama, iyilik ve başka eylemlerde bir şeyin defalarca yapılmasını kapsar.","neighbor_ref":"root_000208/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir olayın veya eylemin birden çok kez gerçekleşmesi bulunur."},{"boundary_match":"partial","distinction":"Odak dal savaşla ve ilk olmama niteliğiyle sınırlıdır; komşu dal ise farklı eylem ve oluşlardaki başlangıç ile dönüş düzenini anlatır.","focus_only":"Odak dal, bir savaşın öncülü bulunmasını veya savaş içindeki çatışmanın yinelenmesini bildirir.","gloss":"başlangıç ve yeniden yapma","neighbor_only":"Komşu dal başlangıç ile geri dönüşü veya yeniden yapmayı aynı genel süreçte birleştirir.","neighbor_ref":"root_000090/B002","relation_type":"near_neighbor","shared_zone":"İki dal da ilk gerçekleşmeden sonra bir yeniden oluş düşüncesi taşıyabilir."},{"boundary_match":"field_only","distinction":"Genel savaş adı, savaşın ilk mi yoksa yinelenmiş mi olduğunu söylemez; odak dalın ayırt edici koşulu tam olarak bu geçmiş ve tekrar bilgisidir.","focus_only":"Odak dal savaşın daha önce yaşanmış veya yinelenmiş olması şartını taşır.","gloss":"savaş ve düşmanlık","neighbor_only":"Komşu dal savaş, düşmanlık, savaşma ve savaşla ilgili yer ya da kişileri genel olarak kapsar.","neighbor_ref":"root_000302/B002","relation_type":"same_field","shared_zone":"Her iki dalın merkezinde savaş ve çatışma alanı bulunur."}],"source_phrase_ar":"الحرب العوان التي كانت قبلها حرب بكر (ayn); العوان من الحروب التي قوتل فيها مرة بعد مرة (sihah); استعير للحرب التي قد تكررت وقدمت (mufradat)","source_summary":"Kaynaklar savaşın ilk olmadığında birleşir; bunu kimi anlatımlar önceki bir savaşla, kimileri ise çatışmanın defalarca yinelenmesi ve eskimesiyle açıklar.","sources":["AY","SI","MU"],"what_is_ar":"الحرب العوان التي قوتل فيها مرة بعد مرة أو سبقتها حرب أولى","what_is_not_ar":"ليس العوان في سن البقرة ولا العون بمعنى النصرة"},"support_links":["sup_16c5a1546ecc239a9f6c"]},{"boundary":"Bu dal genel yaşlılık adı değil, yaşlı hurma ağacını adlandıran yalın bir sözlük birimidir.","branch_kind":"bare","branch_ref":"root_001064/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَاعُون","morph_features":"STEM|POS:N|LEM:maAEuwn|ROOT:mEn|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:7:2:2","qac_word_ref":"107:7:2","surface_ar":"مَاعُونَ"}],"gloss":"yaşlı hurma ağacı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, yaşı ilerlemiş ve eski sayılan bir hurma ağacıdır."}}],"root_ar":"م ع ن","root_id":"root_001064","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın birimin ağaç türünü ve yaşlılık niteliğini birlikte koruyan doğrudan karşılıktır.","boundary_detail":"Bu dal genel yaşlılık adı değil, yaşlı hurma ağacını adlandıran yalın bir sözlük birimidir.","branch_image_ar":"النخلة العَوانة القديمة","concept_gloss":"yaşlı hurma ağacı","contextual_glosses":[{"applicability":"Ağacın yaşı ve eskiliği bağlamdan açıkça anlaşıldığında daha kısa bir karşılık olarak kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hurma türünü ve eskilik niteliğini doğal bağlam içinde korur."},"facet_ids":["F001"],"text":"eski hurma","usage_role":"contextual"}],"definition":"Yaşı ilerlemiş, eski bir hurma ağacını adlandıran sözdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, yaşı ilerlemiş ve eski sayılan bir hurma ağacıdır."}],"identity_rationale":"Tek kaynak ifadesi sözü doğrudan yaşlı bir hurma ağacı için verir. Geçici çerçeve hem varlığı hem de ağaç türüne bağlı sınırı değiştirmeden yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"yaşlı hurma ağacı"}],"lexicalization_note":"Tanım yalın birimin yaşlı hurma ağacı anlamıyla sınırlıdır ve komşu yaş, bitki ya da eskilik anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel eskilik, genç hurma karşıtlığı ve genel yaşlanma en belirgin sınırları verir, öteki adaylar ağacın bölümü, ürünü veya gelişim kusuruyla ilgilidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın hurma ağacına bağlı sözlüksel sınırı vardır; komşu dal ise tür ayrımı yapmadan genel eskiliği bildirir.","focus_only":"Odak dal yalnızca yaşlı bir hurma ağacını adlandırır.","gloss":"eskimiş ve köklü","neighbor_only":"Komşu dal uzun zaman geçmiş her tür şeyi, yiyeceği, içeceği, aracı veya yapıyı kapsar.","neighbor_ref":"root_000979/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da zaman geçmesi sonucunda eski sayılma niteliği vardır."},{"boundary_match":"opposed","distinction":"Aynı bitki türünün yaş ekseninde odak dal yaşlı ucu, komşu dal genç ucu gösterir.","focus_only":"Odak dal yaşı ilerlemiş tek bir hurma ağacını belirtir.","gloss":"genç hurma ağaçları","neighbor_only":"Komşu dal küçük ve genç hurma ağaçlarını toplu bir adla belirtir.","neighbor_ref":"root_000832/B006","relation_type":"antonym","shared_zone":"İki dal da hurma ağacını yaşam evresine göre adlandırır."},{"boundary_match":"partial","distinction":"Komşu dal genel yaşlanma ve eskime alanıdır; odak dal ise yalnızca hurma ağacına ait tek bir adlandırmadır.","focus_only":"Odak dal yaşlılığı hurma ağacına özgü bir adla ifade eder.","gloss":"yaşlanıp eski olma","neighbor_only":"Komşu dal insanın yaşlanmasını ve eskilik nedeniyle yaşlı sayılan başka nesneleri de kapsar.","neighbor_ref":"root_000985/B003","relation_type":"near_neighbor","shared_zone":"İki dal yaş ilerlemesi veya uzun zaman geçmesi sonucu eski sayılmayı paylaşır."}],"source_phrase_ar":"وقيل العوانة للنخلة القديمة (mufradat)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, bu birimi yalnızca yaşlı ve eski bir hurma ağacının adı olarak verir."}],"source_summary":"Bu dal için kaynaklar arası ortak bir özet yoktur; anlam tek bir sözlük tanıklığına dayanır.","sources":["MU"],"what_is_ar":"العوانة للنخلة القديمة","what_is_not_ar":"ليس العوان في سن الحيوان ولا الحرب العوان"},"support_links":[]},{"boundary":"Bu dal genel iş birliği anlamı değildir ve kadın ile hayvana özgü koşullar ayrı tutulmalıdır.","branch_kind":"collocation","branch_ref":"root_001064/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَاعُون","morph_features":"STEM|POS:N|LEM:maAEuwn|ROOT:mEn|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:7:2:2","qac_word_ref":"107:7:2","surface_ar":"مَاعُونَ"}],"gloss":"bedensel denge ve güç olgunluğu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yapıya bağlı niteleme, bedenin yaşla birlikte belirli bir denge veya güç olgunluğuna ulaşmasını bildirir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kadın için yaşın ilerlemesi, bedenin etli olması ve yapının ölçülü görünerek belirgin çıkıntı göstermemesi öne çıkar."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Yük atı için hayvanın gücü ile yaşının birbirine yetişip uyumlu bir olgunluğa ulaşması belirtilir."}}],"root_ar":"م ع ن","root_id":"root_001064","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kanıtta verilen kadın ve yük atı nitelemelerinin ortak, soyut çekirdeğini ifade eder.","boundary_detail":"Bu dal genel iş birliği anlamı değildir ve kadın ile hayvana özgü koşullar ayrı tutulmalıdır.","branch_image_ar":"استواء الخلقة وتلاحق القوة","concept_gloss":"bedensel denge ve güç olgunluğu","contextual_glosses":[{"applicability":"Kadının yaşı ilerlerken bedeninin etli ve ölçülü görünmesini anlatan özel yapıda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına özgü yaş, etlilik ve dengeli görünüş koşullarını korur."},"facet_ids":["F002"],"text":"bedeni dengeli ve etli kadın","usage_role":"contextual"},{"applicability":"Hayvanın gücü ile yaşının birbirine yetiştiği özel niteleme için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvanda güç ile yaşın birbirini yakalaması koşulunu korur."},"facet_ids":["F003"],"text":"gücü yaşına yetişmiş yük atı","usage_role":"contextual"}],"definition":"Belirli kadın ve yük atı nitelemelerinde bedenin yaşla birlikte dengeli ya da güçlü bir olgunluğa erişmesini anlatır. Kadında yaş alma, etlilik ve orantılı görünüş; hayvanda ise güç ile yaşın birbirine yetişmesi ayrı koşullardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yapıya bağlı niteleme, bedenin yaşla birlikte belirli bir denge veya güç olgunluğuna ulaşmasını bildirir."},{"facet_id":"F002","role":"specialization","statement":"Kadın için yaşın ilerlemesi, bedenin etli olması ve yapının ölçülü görünerek belirgin çıkıntı göstermemesi öne çıkar."},{"facet_id":"F003","role":"specialization","statement":"Yük atı için hayvanın gücü ile yaşının birbirine yetişip uyumlu bir olgunluğa ulaşması belirtilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"İnsanların birlikte çalışma davranışını yanlış biçimde anlama ekler.","collision":"Yardımlaşma dalındaki karşılıklı destek anlamıyla karışır.","fit":"displacement","loses":"Yaş, beden yapısı ve güç olgunluğu koşullarının tamamını siler.","preserves":"Birden çok unsurun uyumu düşüncesini yalnızca çağrışım düzeyinde taşır."},"text":"iş birlikçi"}],"identity_rationale":"Kaynak ifadesi kadın ve yük atı için iki ayrı yapıya bağlı nitelik verir: kadında yaş alma, etlilik ve beden oranı; hayvanda ise güç ile yaşın birbirine yetişmesi. Geçici çerçeve bunları ortak bir bedensel olgunlaşma altında kullanabilir, ancak iki uygulamanın koşulları birbirine aktarılmamalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"bedeni dengeli kadın veya yaş almış, etli kadın"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"gücü ile yaşı birbirine yetişmiş yük atı"}],"lexicalization_note":"Tanım yalnızca kadın ve yük atıyla kurulan iki niteleme yapısına bağlıdır; buradan yalın ve genel bir bedensel denge anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; orantılı beden, hayvanda durumun tamamlanması ve genel güç olgunluğu en yakın sınırları verir, kalanlar irilik, kalınlık veya tek bir organın yapısıyla ilgilidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal biçim oranına odaklanır; odak dal ise belirli yapılarda yaş, etlilik veya güç olgunluğu koşullarını da zorunlu kılar.","focus_only":"Odak dal kadında yaş ve etliliği, yük atında ise güç ile yaşın birbirine yetişmesini içerir.","gloss":"orantılı beden yapısı","neighbor_only":"Komşu dal genel olarak benzer, orantılı ve düzgün bir beden biçimini yaş koşulu olmadan kapsar.","neighbor_ref":"root_001240/B019","relation_type":"near_neighbor","shared_zone":"İki dal özellikle bedenin dengeli ve ölçülü görünmesi yönünde kesişir."},{"boundary_match":"partial","distinction":"Odak dalın hayvan kullanımı güç ile yaşın uyumuna bağlıdır; komşu dal semizlik ve çiftleşme yeterliği gibi başka tamamlanma ölçütleri taşır.","focus_only":"Odak dal kadın bedenini de kapsar ve yük atında güç ile yaşın birbirine yetişmesini belirtir.","gloss":"hayvanın durum ve güççe tamamlanması","neighbor_only":"Komşu dal hayvanın semizlik, çiftleşme yeterliği veya genel durum bakımından tamamlanmasını kapsar.","neighbor_ref":"root_000347/B013","relation_type":"near_neighbor","shared_zone":"İki dal hayvan bedeninin güç ve gelişim bakımından olgun bir duruma gelmesini paylaşır."},{"boundary_match":"partial","distinction":"Komşu dal insanda genel gençlik tamamlanmasıdır; odak dal ise kadın ve yük atına özgü iki ayrı niteleme koşuluyla sınırlıdır.","focus_only":"Odak dal belirli kadın ve yük atı yapılarında beden oranı, etlilik veya güç ile yaş uyumunu anlatır.","gloss":"gençliğin ve gücün tamamlanması","neighbor_only":"Komşu dal insanın gençliğinin, gücünün, bedeninin ve aklının genel tamamlanmasını kapsar.","neighbor_ref":"root_000766/B005","relation_type":"near_neighbor","shared_zone":"Her iki dal yaşla birlikte beden ve gücün olgunlaşmasını konu edinir."}],"source_phrase_ar":"المتعاونة من النساء التي طعنت في السن ولا تكون إلا مع كثرة اللحم (sihah); امرأة متعاونة إذا اعتدل خلقها فلم يبد حجمها وبرذون متعاون إذا لحقت قوته وسنه (tahdhib)","source_summary":"Toplu kanıt, kadın için yaş alma, etlilik ve ölçülü beden görünüşünü; yük atı için güç ile yaşın birbirine yetişmesini aynı yapıya bağlı dalda yan yana verir.","sources":["SI","TA"],"what_is_ar":"المتعاونة في المرأة أو البرذون إذا اعتدل الخلق أو لحقت القوة والسن","what_is_not_ar":"ليس التعاون بمعنى إعانة بعضهم بعضا ولا العوان بين السنين"},"support_links":[]},{"boundary":"Bu dal genel sürü adı veya eşek adı değildir; özellikle yaban eşeklerinden oluşan topluluğu belirtir.","branch_kind":"bare","branch_ref":"root_001064/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَاعُون","morph_features":"STEM|POS:N|LEM:maAEuwn|ROOT:mEn|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:7:2:2","qac_word_ref":"107:7:2","surface_ar":"مَاعُونَ"}],"gloss":"yaban eşeği sürüsü","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, üyeleri yaban eşeği olan bir hayvan sürüsüdür."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Sürü adının kaynaklarda iki ayrı çoğul biçimi bulunur."}}],"root_ar":"م ع ن","root_id":"root_001064","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hayvan türünü ve topluluk olma özelliğini eksiksiz veren doğrudan kavram karşılığıdır.","boundary_detail":"Bu dal genel sürü adı veya eşek adı değildir; özellikle yaban eşeklerinden oluşan topluluğu belirtir.","branch_image_ar":"العانة قطيع الحمر","concept_gloss":"yaban eşeği sürüsü","contextual_glosses":[{"applicability":"Bir anlatıda topluluğu doğal Türkçe söz dizimiyle belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sürü miktarını ve yaban eşeği üyelerini açık biçimde korur."},"facet_ids":["F001"],"text":"bir sürü yaban eşeği","usage_role":"contextual"}],"definition":"Yaban eşeklerinden oluşan bir sürüyü adlandıran sözdür; aynı anlam için iki ayrı çoğul biçim kullanılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, üyeleri yaban eşeği olan bir hayvan sürüsüdür."},{"facet_id":"F002","role":"extension","statement":"Sürü adının kaynaklarda iki ayrı çoğul biçimi bulunur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Evcil eşekleri ve sürü oluşturmayan bireyleri de kapsama ekler.","collision":"Genel eşek adıyla ve evcil eşek topluluğuyla karışır.","fit":"broadening","loses":null,"preserves":"Hayvan türünün eşek olma yönünü kısmen korur."},"text":"eşekler"}],"identity_rationale":"Kaynak ifadesi birimi tutarlı biçimde yaban eşeklerinden oluşan bir sürü olarak tanımlar ve iki çoğul biçim bildirir. Geçici çerçeve hayvan türü ile topluluk anlamını doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yaban eşeği sürüsü"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"yaban eşeği sürüleri"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"yaban eşeği sürüleri"}],"lexicalization_note":"Tanım yalın birimin yaban eşeği sürüsü anlamıyla sınırlıdır; başka hayvan toplulukları veya kökün öteki dalları içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yaban sığırı, az sayıdaki deve ve deve kuşu toplulukları tür sınırını en açık biçimde gösterir, kalanlar da başka hayvanları veya dağınık topluluk yapısını belirtir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Topluluk yapısı ortak olsa da hayvan türü sınırı farklıdır; bu nedenle iki sürü adı birbirinin yerine kullanılamaz.","focus_only":"Odak dal yalnızca yaban eşeklerinden oluşan sürüyü belirtir.","gloss":"yaban sığırı sürüsü","neighbor_only":"Komşu dal yaban sığırı sürüsünü, bazı kullanımlarda ise sığır veya deve topluluğunu belirtir.","neighbor_ref":"root_000532/B014","relation_type":"near_neighbor","shared_zone":"Her iki dal belirli büyük otçul hayvanlardan oluşan bir sürüyü adlandırır."},{"boundary_match":"partial","distinction":"Odak dalda belirleyici özellik yaban eşeği türüdür; komşu dalda deve türüne ek olarak azlık ve bazen dişilik sınırı bulunur.","focus_only":"Odak dal yaban eşeği türüne bağlıdır ve belirli bir küçük sayı koşulu taşımaz.","gloss":"az sayıda deve topluluğu","neighbor_only":"Komşu dal çoğunlukla dişi olan az sayıdaki develerden oluşan bir topluluğu belirtir.","neighbor_ref":"root_000524/B002","relation_type":"near_neighbor","shared_zone":"İki dal da hayvanlardan oluşan sayılabilir bir topluluğa özel ad verir."},{"boundary_match":"partial","distinction":"Sürü olma özelliği ortaktır, fakat biri yaban eşeklerine, diğeri deve kuşlarına özgüdür.","focus_only":"Odak dal yaban eşeği sürüsünü adlandırır.","gloss":"deve kuşu sürüsü","neighbor_only":"Komşu dal deve kuşlarından oluşan sürüyü adlandırır.","neighbor_ref":"root_000453/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal vahşi hayvanlardan oluşan bir sürü için özel topluluk adıdır."}],"source_phrase_ar":"العانة القطيع من حمر الوحش وتجمع على عانات وعون (ayn); العانة القطيع من حمر الوحش والجمع عون (sihah); العانة قطيع من حمر الوحش وجمع على عانات وعون (mufradat)","source_summary":"Kaynaklar yalın birimi yaban eşeği sürüsü olarak ortak biçimde tanımlar ve bu sürü adı için iki çoğul biçimi birlikte bildirir.","sources":["AY","SI","MU"],"what_is_ar":"العانة للقطيع من حمر الوحش وجمعها عانات وعون","what_is_not_ar":"ليس عانة الرجل ولا عانة الموضع"},"support_links":[]},{"boundary":"Gönderge organın kendisi veya bütün kasık bölgesi değil, o bölgede çıkan kıllardır.","branch_kind":"mixed_non_bare","branch_ref":"root_001064/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَاعُون","morph_features":"STEM|POS:N|LEM:maAEuwn|ROOT:mEn|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:7:2:2","qac_word_ref":"107:7:2","surface_ar":"مَاعُونَ"}],"gloss":"erkekte kasık kılları","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderge, erkeğin üreme organı çevresinde ve kasık bölgesinde çıkan kıllardır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kıl adının aynı göndergeyi küçük gösteren bir küçültme biçimi vardır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı biçim ailesindeki bir eylem, kişinin kasık kıllarını tıraş etmesini bildirir."}}],"root_ar":"م ع ن","root_id":"root_001064","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kıl göndergesini, beden bölgesini ve erkekle kurulan sınırı birlikte veren çekirdek karşılıktır.","boundary_detail":"Gönderge organın kendisi veya bütün kasık bölgesi değil, o bölgede çıkan kıllardır.","branch_image_ar":"عانة الرجل","concept_gloss":"erkekte kasık kılları","contextual_glosses":[{"applicability":"Türemiş eylem biçiminin kişinin söz konusu kılları kesmesini anlattığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Eylemin nesnesini ve tıraş etme işlemini açıkça korur."},"facet_ids":["F003"],"text":"kasık kıllarını tıraş etmek","usage_role":"contextual"}],"definition":"Erkeğin üreme organı çevresinde ve kasık bölgesinde çıkan kılları adlandırır. Aynı dalda bu adın küçültme biçimi ile söz konusu kılları tıraş etmeyi bildiren bir eylem biçimi de bulunur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderge, erkeğin üreme organı çevresinde ve kasık bölgesinde çıkan kıllardır."},{"facet_id":"F002","role":"extension","statement":"Kıl adının aynı göndergeyi küçük gösteren bir küçültme biçimi vardır."},{"facet_id":"F003","role":"associated_use","statement":"Aynı biçim ailesindeki bir eylem, kişinin kasık kıllarını tıraş etmesini bildirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kıllar yerine bölgenin tamamını ve çevredeki dokuları kapsama ekler.","collision":"Beden bölgesi adıyla o bölgede çıkan kılların adı birbirine karışır.","fit":"broadening","loses":null,"preserves":"İlgili beden bölgesini genel olarak korur."},"text":"kasık"}],"identity_rationale":"Kaynak ifadesi çekirdeği erkeğin üreme organı çevresinde çıkan kıl olarak verir, ayrıca küçültme biçimini ve bu kılları tıraş etme eylemini bildirir. Geçici çerçeve göndergenin kıl olduğunu doğru biçimde korur.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"erkeğin kasık kılları"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"kasık kıllarını küçülterek söyleyen biçim"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kasık kıllarını tıraş etti"}],"lexicalization_note":"Tanım kıl göndergesini çekirdek tutar; erkeğe bağlı adlandırma, küçültme biçimi ve tıraş eylemi birbirine karıştırılmadan ayrı yönler olarak verilir.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; kasık bölgesinin kendisi, gövdedeki kıl çizgisi ve sakal kılları gönderge sınırını en iyi açıklar, kalanlar organ, sünnet derisi veya başka beden bölümleridir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın göndergesi kıldır; komşu dalın göndergesi bölge, doku veya dolaylı olarak organdır.","focus_only":"Odak dal erkeğin ilgili bölgesinde çıkan kılları belirtir.","gloss":"kasık bölgesi veya dokusu","neighbor_only":"Komşu dal kasık bölgesini, o bölgenin etini veya kadın üreme organını dolaylı biçimde belirtir.","neighbor_ref":"root_000589/B006","relation_type":"near_neighbor","shared_zone":"İki dal aynı genel beden bölgesine gönderimde bulunabilir."},{"boundary_match":"partial","distinction":"Komşu dal çizgi biçimindeki bir uzanışı ve başka yol izlerini içerir; odak dal ise kasık bölgesindeki kıl topluluğudur.","focus_only":"Odak dal erkeğin üreme organı çevresindeki kılları bir bütün olarak adlandırır.","gloss":"gövdedeki kıl çizgisi","neighbor_only":"Komşu dal göğsün ortasından göbeğe veya kasığa uzanan kıl çizgisini ve başka iz yollarını kapsar.","neighbor_ref":"root_000691/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal gövdenin alt bölümüne uzanan beden kıllarıyla ilişkilidir."},{"boundary_match":"field_only","distinction":"Ortak alan beden kılıdır, ancak beden bölgesi ve ilişkili eylemler farklıdır; biri kasık, diğeri yüz bölgesine aittir.","focus_only":"Odak dal kasık bölgesindeki kılları ve bunların tıraş edilmesini kapsar.","gloss":"sakal kılları","neighbor_only":"Komşu dal yüzde çıkan sakal kıllarını, bunların uzunluğunu ve sakallanmayı kapsar.","neighbor_ref":"root_001350/B002","relation_type":"same_field","shared_zone":"İki dal insan bedenindeki belirli bir bölgede çıkan kılları adlandırır."}],"source_phrase_ar":"عانة الرجل إسبه من الشعر على فرجه وتصغيره عوينة (ayn); العانة شعر الركب واستعان فلان حلق عانته (sihah); عانة الرجل شعره النابت على فرجه وتصغيره عوينة (mufradat)","source_summary":"Kaynaklar çekirdeği erkeğin üreme organı çevresindeki kıllar olarak ortaklaştırır ve küçültme biçimini destekler; toplu kanıt ayrıca bu kılları tıraş etmeyi bildiren eylemi içerir.","sources":["AY","SI","MU"],"what_is_ar":"عانة الرجل للشعر النابت على فرجه وما يتصل بحلقه","what_is_not_ar":"ليس العانة قطيع الحمر ولا عانة الموضع"},"support_links":[]},{"boundary":"Dal hem yer adını hem o yere bağlanan şarap adını kapsar; iki yer anlatımının özdeşliği kesin sayılmaz.","branch_kind":"mixed_non_bare","branch_ref":"root_001064/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَاعُون","morph_features":"STEM|POS:N|LEM:maAEuwn|ROOT:mEn|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:7:2:2","qac_word_ref":"107:7:2","surface_ar":"مَاعُونَ"}],"gloss":"bir yer adı ve o yere bağlanan şarap adı","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki yakın ad biçimi, biri bir bölgenin yöresindeki yer, diğeri bir ırmak üzerindeki köy olarak tanımlanan coğrafi göndergeleri adlandırır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Şarap, söz konusu yerden geldiği belirtilerek o yere bağlı bir nitelemeyle adlandırılır."}}],"root_ar":"م ع ن","root_id":"root_001064","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yer göndergesini ve şarabın o yerden geldiğini bildiren bağlı adlandırmayı birlikte veren açıklayıcı karşılıktır.","boundary_detail":"Dal hem yer adını hem o yere bağlanan şarap adını kapsar; iki yer anlatımının özdeşliği kesin sayılmaz.","branch_image_ar":"النسبة إلى عانة","concept_gloss":"bir yer adı ve o yere bağlanan şarap adı","contextual_glosses":[{"applicability":"Şarabın söz konusu coğrafi yerle köken ilişkisi içinde anıldığı bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Şarap ile belirtilen yer arasındaki köken ilişkisini korur."},"facet_ids":["F002"],"text":"o yöreden gelen şarap","usage_role":"contextual"}],"definition":"Dal, iki yakın yer adı biçimi ile bunlardan geldiği belirtilen şarap adlandırmasını birlikte kapsar. Kanıt, bir bölgenin yöresindeki yer ile bir ırmak üzerindeki köy anlatımının aynı coğrafi noktayı gösterdiğini kesinleştirmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki yakın ad biçimi, biri bir bölgenin yöresindeki yer, diğeri bir ırmak üzerindeki köy olarak tanımlanan coğrafi göndergeleri adlandırır."},{"facet_id":"F002","role":"associated_use","statement":"Şarap, söz konusu yerden geldiği belirtilerek o yere bağlı bir nitelemeyle adlandırılır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Herhangi bir yerde üretilen bütün yerel şarapları kapsama ekler.","collision":"Belirli yer adına bağlı olmayan genel bölgesel şaraplarla karışır.","fit":"broadening","loses":null,"preserves":"Şarap ile bir yer arasındaki bağlantıyı genel olarak korur."},"text":"yerel şarap"}],"identity_rationale":"Kaynak ifadesi iki yakın yer adı biçimini ve bu yere bağlanarak adlandırılan şarabı aynı dalda toplar. Ancak anlatımlardan biri yeri bir bölgenin yöresinde, diğeri bir ırmak üzerindeki köy olarak gösterdiğinden bunların aynı coğrafi nokta olduğu kanıttan kesinleşmez.","lexical_glosses":[{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"şarabıyla ilişkilendirilen bir yer veya köy adı"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"aynı yer adıyla ilişkili değişken ad biçimi"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"söz konusu yerden geldiği belirtilen şarap"}],"lexicalization_note":"Tanım yer adı birimlerini ve yalnızca şarapla kurulan köken bildiren yapıyı ayırır; şaraba özgü değer yalın yer adına genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; yer adı ile ürünü ilişkilendiren mızrak, kumaş ve şehir ürünü dalları en yararlı karşılaştırmalardır, kalanlar yalnızca yer adı taşır veya farklı bir coğrafi adlandırma yapısı gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İlişki düzeni benzer olsa da coğrafi gönderge ve bağlı ürün farklıdır; odak dal şarapla, komşu dal mızrakla sınırlıdır.","focus_only":"Odak dal belirli bir yer adı ile o yere bağlanan şarap adını kapsar.","gloss":"yer adı ve oraya bağlanan mızrak","neighbor_only":"Komşu dal başka bir bölge veya yöre adı ile o yere bağlanan mızrakları kapsar.","neighbor_ref":"root_000422/B004","relation_type":"near_neighbor","shared_zone":"İki dalda da bir coğrafi ad ve o coğrafyaya köken yoluyla bağlanan ürün bulunur."},{"boundary_match":"partial","distinction":"Odak dalın bağlı ürünü şaraptır ve yer anlatımı belirsizlik taşır; komşu dal başka bir yer ile birden çok ürün ve hayvan türünü kapsar.","focus_only":"Odak dal yakın biçimli iki yer adı anlatımıyla ve şarap nitelemesiyle sınırlıdır.","gloss":"yer kökenli ürün ve hayvan adları","neighbor_only":"Komşu dal başka bir yere bağlanan kumaş, binek hayvanı ve deve kuşu adlarını kapsar.","neighbor_ref":"root_001238/B013","relation_type":"near_neighbor","shared_zone":"Her iki dal bir yer adından hareketle nesne veya ürünün coğrafi kökenini bildirir."},{"boundary_match":"partial","distinction":"Yapısal benzerliğe karşın yerler ve ürün türleri ayrıdır; odak dal şarap, komşu dal taş ve odunla ilişkilidir.","focus_only":"Odak dal bir yer adı biçimlerini ve o yere bağlanan şarabı içerir.","gloss":"şehir adı ve oraya bağlanan ürünler","neighbor_only":"Komşu dal başka bir şehir adını ve o şehre bağlanan taş ya da güzel kokulu odun adlarını içerir.","neighbor_ref":"root_000965/B012","relation_type":"near_neighbor","shared_zone":"İki dal coğrafi ad ile o coğrafyadan geldiği belirtilen ürün adlarını birlikte taşır."}],"source_phrase_ar":"عانات موضع من ناحية الجزيرة تنسب إليه الخمر العانية (ayn); عانة قرية على الفرات تنسب إليها الخمر فيقال عانية (sihah)","source_summary":"Toplu kanıt yakın biçimli bir yer adını ve o yere bağlanan şarap nitelemesini ortaklaştırır; yerin bir bölge yöresi mi yoksa bir ırmak kıyısındaki köy mü olduğu anlatımlar arasında kesinleşmez.","sources":["AY","SI"],"what_is_ar":"عانة موضع أو قرية وينسب إليها بالخمر العانية","what_is_not_ar":"ليس العانة قطيع الحمر ولا عانة الرجل"},"support_links":[]},{"boundary":"Dalın odağı, bir yararı ya da verilebilecek şeyi başkasına vermemektir; genel engelleme ve koruma bu sınıra girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001448/B001","candidate_links":[{"candidate_id":"cand_1ada1cb61f24493b6fb0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّنَعَ","morph_features":"STEM|POS:V|IMPF|LEM:m~anaEa|ROOT:mnE|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"107:7:1:2","qac_word_ref":"107:7:1","surface_ar":"يَمْنَعُ"}],"gloss":"vermeme ve esirgeme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir şeyi vermenin karşıtı olarak onu elde tutma ve başkasına vermeme eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İyiliği sürekli vermeyen kişi bakımından cimrilik ve esirgeyicilik özelliğine dönüşür."}}],"root_ar":"م ن ع","root_id":"root_001448","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Verilebilecek bir şeyin ya da iyiliğin elde tutulduğu bütün çekirdek kullanımlarda uygundur.","boundary_detail":"Dalın odağı, bir yararı ya da verilebilecek şeyi başkasına vermemektir; genel engelleme ve koruma bu sınıra girmez.","branch_image_ar":"كف اليد عن العطاء","concept_gloss":"vermeme ve esirgeme","contextual_glosses":[{"applicability":"Bir malın ya da yararın istekliye verilmemesini anlatan akıcı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Verme fırsatı bulunduğu halde şeyi elde tutma ve vermeme yönünü korur."},"facet_ids":["F001"],"text":"vermekten kaçınma","usage_role":"contextual"},{"applicability":"Bir kişinin iyiliği sürekli vermeyen niteliğinin açıklanması gereken bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişiye yüklenen sürekli esirgeme ve cimrice elde tutma özelliğini korur."},"facet_ids":["F002"],"text":"iyiliği esirgeyen cimrilik","usage_role":"explanatory"}],"definition":"Verilebilecek bir şeyi ya da iyiliği başkasına vermemek, elde tutmak veya esirgemektir. Kişiye uygulandığında bu tutum, iyiliği sürekli engelleyen cimrice bir özellik olarak belirginleşir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir şeyi vermenin karşıtı olarak onu elde tutma ve başkasına vermeme eylemidir."},{"facet_id":"F002","role":"specialization","statement":"İyiliği sürekli vermeyen kişi bakımından cimrilik ve esirgeyicilik özelliğine dönüşür."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Vermeyle ilgisi olmayan her türlü eylem ve amaç engelini kapsama ekler.","collision":"Birini istediği şeyden alıkoyma dalıyla karışır.","fit":"broadening","loses":null,"preserves":"Bir şeyin karşı tarafa ulaşmaması sonucunu kısmen korur."},"text":"engelleme"},{"category":"alternative","error_profile":{"adds":"Yararlı savunma ve güvenlik amacı ekler.","collision":"Koruyucu güç ve erişilmezlik dalıyla karışır.","fit":"displacement","loses":"Vermenin karşıtı olan esirgeme ve cimrilik çekirdeğini kaybeder.","preserves":"Dışarıdan erişimi önleme gibi uzak bir sonuç benzerliğini korur."},"text":"koruma"}],"identity_rationale":"Kaynak sözü, dalı vermenin karşıtı olan esirgeme ve özellikle iyiliği vermeyen kişinin cimrice tutumu olarak açıkça kurar. Bu çerçeve, birini istediği şeyden alıkoyma ya da koruyucu güç yoluyla erişimi önleme anlamlarından ayrıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"vermenin karşıtı olarak vermeme ve esirgeme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"vermeyen veya verilecek şeyi elinde tutan"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"iyiliği sürekli esirgeyen çok cimri kişi"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"başkasına vermeyen, cimrice elinde tutan kişi"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"yalnızca vermemeyi hak edenden esirgeyen ve adaletle veren"}],"lexicalization_note":"Tanım, vermemenin genel çekirdeği ile kişiyi sürekli esirgeyen ya da cimri gösteren türemiş kullanımları ayırarak kapsar.","neighbor_coverage_note":"Adayların tümü değerlendirildi; en yararlı karşılaştırmalar cimrilik ve vermeme komşularıyla, ardından genel alıkoyma dalıyla kuruldu.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalının sınırı verme karşıtlığı ve iyiliği esirgeme üzerine kuruludur; komşu dal ise nesneyi saklama anlamına da uzandığı için tam olarak birbirinin yerine geçmez.","focus_only":"Bu dal, özellikle vermenin karşıtı olarak iyiliği başkasından esirgemeyi öne çıkarır.","gloss":"cimrice esirgeme","neighbor_only":"Komşu dal, bir şeyi cimrilikle vermemenin yanında onu gizlemeyi de kapsar.","neighbor_ref":"root_000917/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da kişinin elindeki şeyi başkasına vermemesi ve cimrice tutması alanında örtüşür."},{"boundary_match":"partial","distinction":"Komşu dal istek karşısındaki somut vermeme durumuna daha sıkı bağlıdır; odak dalı ise genel verme karşıtlığını ve yerleşik cimrilik niteliğini birlikte taşır.","focus_only":"Bu dal, genel verme karşıtlığını ve sürekli iyilik esirgeyen kişi niteliğini de kapsar.","gloss":"isteneni vermeme","neighbor_only":"Komşu dal, özellikle kendisinden istenen şeyi vermeyen kişi görünümünü öne çıkarır.","neighbor_ref":"root_000877/B004","relation_type":"near_synonym","shared_zone":"İki dal da bir kişinin verebileceği şeyi vermeyip elinde tutmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalı verme karşıtlığından hareket eder; komşu dal ise kişinin iyilik üretmeyen katılığını ve hak vermedeki cimriliğini daha belirgin bir nitelik olarak sunar.","focus_only":"Bu dalın çekirdeği, verilecek şeyi elde tutarak verme eylemini gerçekleştirmemektir.","gloss":"iyiliği vermeyen cimrilik","neighbor_only":"Komşu dal, iyilik azlığını ve verilmesi gereken hakkı esirgemeyi ayrıca belirginleştirir.","neighbor_ref":"root_000258/B003","relation_type":"near_synonym","shared_zone":"Her ikisi de iyiliği esirgeme ve cimrilik gösterme alanında büyük ölçüde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalı verme ilişkisine bağlı bir esirgemedir; komşu dal ise verme ilişkisi bulunmadan da kişiyi amacından alıkoyan genel bir engellemedir.","focus_only":"Bu dalda engellenen aktarım, verilebilecek bir şeyin ya da iyiliğin başkasına verilmesidir.","gloss":"vermemek ile alıkoymak","neighbor_only":"Komşu dal, kişinin istediği herhangi bir nesneye ya da eyleme ulaşmasının önüne geçer.","neighbor_ref":"root_001448/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir tarafın istediği sonuca ulaşamaması ve bir şeyden yoksun kalması söz konusudur."}],"source_phrase_ar":"خلاف الإعطاء (maqayis;sihah)؛ ضد العطية (mufradat)؛ رجل منوع ومناع إذا كان بخيلا ممسكا (tahdhib)؛ مناع للخير (tahdhib;mufradat)","source_summary":"Kaynakların ortak çizgisi, anlamı vermenin karşıtına yerleştirir; iyiliği vermeyen kişi için de elde tutma ve cimrilik niteliğini öne çıkarır.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه المنع ضد الإعطاء والعطية، والبخل والإمساك، ووصف الرجل بمانع ومناع ومنوع إذا منع الخير أو أمسكه.","what_is_not_ar":"ليس هو الحماية والمنعة إذا كان المقصود قوة تمنع الوصول لا مجرد ضد العطاء."},"support_links":["sup_f01fe84a10b06f030164"]},{"boundary":"Engelleme, kişinin istediği şeye ya da eyleme yönelişini kesmelidir; yalnızca vermemek veya korunaklı olmak yeterli değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001448/B002","candidate_links":[{"candidate_id":"cand_404e78531ed488d25bde","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّنَعَ","morph_features":"STEM|POS:V|IMPF|LEM:m~anaEa|ROOT:mnE|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"107:7:1:2","qac_word_ref":"107:7:1","surface_ar":"يَمْنَعُ"}],"gloss":"isteğinden alıkoyma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kişi ile istediği nesne ya da eylem arasına girerek onun erişimini veya yönelişini keser."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Engel, kişiyi eylemi bırakmaya yöneltebilir ve istediği şeyden geri durmasıyla sonuçlanabilir."}}],"root_ar":"م ن ع","root_id":"root_001448","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bir kişinin istediği nesneye ulaşması veya amaçladığı eylemi yapması engellendiğinde kullanılır.","boundary_detail":"Engelleme, kişinin istediği şeye ya da eyleme yönelişini kesmelidir; yalnızca vermemek veya korunaklı olmak yeterli değildir.","branch_image_ar":"حاجز بين المرء وما يريد","concept_gloss":"isteğinden alıkoyma","contextual_glosses":[{"applicability":"Bir kişinin belirli bir amaca ilerleyişinin doğrudan durdurulduğu bağlamlarda doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişi ile amacı arasına girerek ilerleyişi durdurma yönünü korur."},"facet_ids":["F001"],"text":"önünü kesme","usage_role":"contextual"},{"applicability":"Bir engelin kişiyi amaçladığı eylemi bırakmaya yönelttiği sonuç odaklı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Engelin kişiyi eylemden geri döndürmesi ve bırakmaya yöneltmesi sonucunu korur."},"facet_ids":["F002"],"text":"vazgeçirmeye yol açma","usage_role":"explanatory"}],"definition":"Bir kişiyle ulaşmak istediği şey veya yapmak istediği eylem arasına girerek onu durdurmak, ondan uzaklaştırmak ya da vazgeçmesine yol açmaktır. Engelleme sonucunda kişi istediği şeyden geri durabilir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kişi ile istediği nesne ya da eylem arasına girerek onun erişimini veya yönelişini keser."},{"facet_id":"F002","role":"extension","statement":"Engel, kişiyi eylemi bırakmaya yöneltebilir ve istediği şeyden geri durmasıyla sonuçlanabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Vermenin karşıtı olan esirgeme dalıyla karışır.","fit":"narrowing","loses":"Nesne ve eylem amaçlarının önüne geçme biçimindeki genel engelleme ilişkisini kaybeder.","preserves":"Bir tarafın istediği şeye ulaşamaması sonucunu kısmen korur."},"text":"vermeme"},{"category":"alternative","error_profile":{"adds":"Bir istek ya da yönelişi engellemeyen her türlü fiziksel ayrımı kapsama ekler.","collision":"İki şeyi bir engelle birbirinden ayıran komşu dallarla karışır.","fit":"broadening","loses":null,"preserves":"İki taraf arasına bir sınır girmesi görünümünü korur."},"text":"ayırma"}],"identity_rationale":"Kaynak sözü, bir kişiyle istediği nesne veya eylem arasına girerek onu durdurmayı ve bırakmaya yöneltmeyi açıkça belirtir. Dalın kimliği, vermeme anlamından ve erişilmezlik sağlayan koruyucu güçten bağımsız bir amaç engelleme ilişkisine dayanır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"onu istediği şeyden alıkoymak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"seni bunu yapmaktan ne alıkoydu?"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"önüne engel çıkınca geri durmak"}],"lexicalization_note":"Tanım, genel alıkoyma çekirdeğini korurken nesneden uzaklaştıran yapıları, bırakma sebebi soran kalıbı ve engel sonrası geri durma sonucunu ayrı tutar.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; amaçtan alıkoymaya en yakın engelleme dalları, ayırıcı koyma ve karşıt serbest bırakma kutbu sınırı en iyi açıklayan karşılaştırmalar olarak seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalının sınırı istek ile amaç arasına girme ilişkisidir; komşu dal ise engelin yanı sıra geciktirme ve oyalama biçimlerini de kapsadığı için daha geniştir.","focus_only":"Bu dal, kişiyle istediği şey arasına girmeyi ve onu eylemi bırakmaya yöneltmeyi birlikte kapsar.","gloss":"amaçtan alıkoyma","neighbor_only":"Komşu dal, geciktirme, ağırdan aldırma ve özellikle iyilikten oyalama yönlerine de uzanır.","neighbor_ref":"root_001061/B001","relation_type":"near_synonym","shared_zone":"İki dal da kişinin amaçladığı şeye ulaşmasını engelleyip onu hareketinden geri bırakır."},{"boundary_match":"partial","distinction":"Odak dalı insanın isteği ve amacı üzerinden kurulur; komşu dal ise engellenen şeyi bir yönden çevirme biçimindeki daha özel harekete bağlıdır.","focus_only":"Bu dal, kişinin istediği nesneye veya eyleme ulaşmasını genel olarak kesebilir.","gloss":"engelleme ve yönünden çevirme","neighbor_only":"Komşu dal, bir şeyi belirli bir yönden çevirme ya da o yönde ilerlemesini önleme görünümüne bağlıdır.","neighbor_ref":"root_000252/B013","relation_type":"near_synonym","shared_zone":"Her iki dalda da bir yöneliş durdurulur ve hedefe doğru ilerleyiş kesilir."},{"boundary_match":"partial","distinction":"Odak dalı amaçlı yönelişin kesilmesini gerektirir; komşu dalda ise ayırma gerçekleşmesi yeterlidir ve engellenmiş bir istek bulunmayabilir.","focus_only":"Bu dalda kurulan engel, kişinin istediği şeye ulaşmasını veya eylemi sürdürmesini önler.","gloss":"alıkoyma ve araya ayırıcı koyma","neighbor_only":"Komşu dalın çekirdeği, iki şeyi ya da kişiyi bir ayırıcıyla birbirinden ayrı tutmaktır.","neighbor_ref":"root_000297/B001","relation_type":"near_neighbor","shared_zone":"İki dalda da tarafların arasına giren bir engel veya ayırıcı bulunabilir."},{"boundary_match":"opposed","distinction":"Odak dalı erişimi kısıtlayan kutuptadır; komşu dal ise engeli kaldırıp hareketi veya erişimi mümkün kılan karşı kutuptadır.","focus_only":"Bu dal, kişinin amacına ilerleyişini keser ve onu geri bırakır.","gloss":"alıkoyma ile serbest bırakma","neighbor_only":"Komşu dal, bağı çözüp yolu açar, kolaylaştırır veya serbest bırakır.","neighbor_ref":"root_000694/B001","relation_type":"polarity_pair","shared_zone":"Her iki dal da bir kişinin veya şeyin hareket ve erişim imkanının nasıl düzenlendiğiyle ilgilidir."},{"boundary_match":"partial","distinction":"Odak dalında asıl ilişki bir kişiyi amacından alıkoymaktır; komşu dalda ise korunana ait güç ve destek, ona erişilememesini sağlayan bir durum oluşturur.","focus_only":"Bu dal, belirli bir kişinin istediği şeye ya da eyleme ulaşmasını etkin olarak engeller.","gloss":"engelleme ve koruyucu erişilmezlik","neighbor_only":"Komşu dal, kişi veya yeri güçlü koruma ve destek sayesinde erişilmez durumda tutar.","neighbor_ref":"root_001448/B003","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir hedefe erişim önlenir ve dışarıdan gelen yöneliş sonuçsuz kalır."}],"source_phrase_ar":"منعته أمنعه منعا فامتنع أي حلت بينه وبين إرادته (ayn)؛ منعت الرجل عن الشئ فامتنع منه (sihah)؛ المنع أن تحول بين الرجل وبين الشيء الذي يريده (tahdhib)؛ ما الذي صدك وحملك على ترك ذلك (mufradat)","source_summary":"Kaynaklar, kişinin isteğiyle amacı arasına girme çekirdeğinde birleşir; bunu nesneden uzaklaşma, eylemi bırakma ve engel karşısında geri durma sonuçlarıyla açıklar.","sources":["AY","SI","TA","MU"],"what_is_ar":"يدخل فيه أن يحول المانع بين الإنسان والشيء أو الفعل الذي يريده، وأن يصده ويحمله على تركه، ومنه منعته الشيء أو منعته عن الشيء فامتنع.","what_is_not_ar":"ليس هو مجرد البخل بالعطية إذا لم يذكر صد أو حيلولة، وليس هو المنعة بمعنى العز والحماية."},"support_links":["sup_6d79827585e756defcb3"]},{"boundary":"Koruyucu güç, destek veya çevre korunana erişimi önlemelidir; yalnızca bir şeyi vermemek ya da kişinin kendi geri duruşu bu dal değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001448/B003","candidate_links":[{"candidate_id":"cand_404e78531ed488d25bde","lane":"micro"},{"candidate_id":"cand_d2a97663f2abb528cc27","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّنَعَ","morph_features":"STEM|POS:V|IMPF|LEM:m~anaEa|ROOT:mnE|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"107:7:1:2","qac_word_ref":"107:7:1","surface_ar":"يَمْنَعُ"}],"gloss":"erişilmez kılan koruyucu güç","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Güç, saygınlık veya destekçiler bir kişi ya da yere ulaşılmasını önleyen koruyucu bir durum oluşturur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Korunaklı yer ve güçlü kişi, dışarıdan gelenin kolayca erişemediği somut örneklerdir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir topluluğu çevreleyerek korumak, savunmak ve desteklemek aynı koruyucu güç çekirdeğinin eylem görünümüdür."}}],"root_ar":"م ن ع","root_id":"root_001448","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kişi ya da yerin güç, destek ve koruma sayesinde dış müdahaleye kapalı olduğu çekirdek kullanımlarda uygundur.","boundary_detail":"Koruyucu güç, destek veya çevre korunana erişimi önlemelidir; yalnızca bir şeyi vermemek ya da kişinin kendi geri duruşu bu dal değildir.","branch_image_ar":"قوة تحمي فلا يخلص إليها","concept_gloss":"erişilmez kılan koruyucu güç","contextual_glosses":[{"applicability":"Bir kişi veya topluluğun koruyucuları ve gücü sayesinde kendisine ulaşılamadığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Destek ve güç altında bulunma ile dış erişimin engellenmesi yönlerini korur."},"facet_ids":["F001"],"text":"güçlü koruma altında olma","usage_role":"contextual"},{"applicability":"Bir yerin veya yapının koruyucu gücü nedeniyle içine girilemediği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Somut yerin korunaklılığını ve dışarıdan erişilemez oluşunu korur."},"facet_ids":["F002"],"text":"aşılamaz derecede korunaklı","usage_role":"contextual"},{"applicability":"Bir topluluğa dış tehdit karşısında savunma ve yardım sağlama eylemi açıklandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Korunan topluluğu çevreleme, savunma ve destekleme eylemlerini birlikte korur."},"facet_ids":["F003"],"text":"çevreleyip koruma ve destekleme","usage_role":"explanatory"}],"definition":"Bir kişi ya da yeri güç, saygınlık, destekçiler veya koruyucu çevre sayesinde dışarıdan erişilemez ve saldırıya kapalı durumda tutan korumadır. Aynı çekirdek, bir topluluğu çevreleyip savunma ve destekleme eyleminde de görünür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Güç, saygınlık veya destekçiler bir kişi ya da yere ulaşılmasını önleyen koruyucu bir durum oluşturur."},{"facet_id":"F002","role":"specialization","statement":"Korunaklı yer ve güçlü kişi, dışarıdan gelenin kolayca erişemediği somut örneklerdir."},{"facet_id":"F003","role":"extension","statement":"Bir topluluğu çevreleyerek korumak, savunmak ve desteklemek aynı koruyucu güç çekirdeğinin eylem görünümüdür."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":null,"collision":"Kişiyi amacından alıkoyan genel engelleme dalıyla karışır.","fit":"narrowing","loses":"Erişilmezliği sağlayan koruyucu güç, saygınlık ve destekçi çevresini kaybeder.","preserves":"Dışarıdan erişimin önlenmesi sonucunu korur."},"text":"engel"},{"category":"alternative","error_profile":{"adds":null,"collision":"Korunaklı yapının kendisini anlatan komşu dallarla karışır.","fit":"narrowing","loses":"Kişi, topluluk, destekçiler ve soyut koruyucu güç kapsamını kaybeder.","preserves":"Korunaklı ve kolay erişilemeyen yer örneğini korur."},"text":"kale"},{"category":"alternative","error_profile":{"adds":"Hukuki veya kurumsal ayrıcalık anlamını gereksiz biçimde ekleyebilir.","collision":"Yasal statü bildiren çağdaş kullanımlarla karışır.","fit":"broadening","loses":null,"preserves":"Kişiye erişilememesi ve dış müdahaleden korunması sonucunu korur."},"text":"dokunulmazlık"}],"identity_rationale":"Kaynak sözü, yerin veya kişinin güç, saygınlık ve destekçiler sayesinde erişilemez olmasını; ayrıca koruyup destekleme eylemini aynı koruma ekseninde birleştirir. Dalın çekirdeği sıradan engelleme değil, korunana dışarıdan ulaşılamamasını sağlayan güç ve çevredir.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"inananları çevreleyip koruyan ve destekleyen"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"gücü ve koruması sayesinde erişilemez"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"koruyucu güç, saygınlık ve destekçiler"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"saygınlık ve güçlü koruma içinde"}],"lexicalization_note":"Tanım, kişi ve yer için erişilmezlik bildiren biçimleri, koruyucu güç ve destekçi anlamını ve sabit saygınlık-koruma birlikteliğini ayrı görünümler olarak korur.","neighbor_coverage_note":"Adayların tümü değerlendirildi; koruma ve savunma çekirdeğine en yakın dallar ile somut sığınak, güçlü dayanak ve genel engelleme arasındaki sınırlar yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı koruyucu güçten doğan erişilmez durum ve desteğe bağlıdır; komşu dal daha geniş bir savunma, uzak tutma ve sakınma alanına uzanır.","focus_only":"Bu dal, korunan kişi veya yerin güç, saygınlık ve destekçilerle erişilmez oluşunu öne çıkarır.","gloss":"koruma ve erişimi önleme","neighbor_only":"Komşu dal, etkin savunmanın yanında yasak bölge ve yiyecekten sakınma gibi başka uzantılar da taşır.","neighbor_ref":"root_000358/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da dışarıdan yaklaşmayı önleyen savunma ve koruma eyleminde güçlü biçimde örtüşür."},{"boundary_match":"partial","distinction":"Odak dalında erişilmezlik kurucu sonuçtur; komşu dalda koruyucu gözetimle birlikte rahatlık ve yaşam iyiliği de yer alabilir.","focus_only":"Bu dal, dışarıdan ulaşılamamayı sağlayan güç, saygınlık ve koruyucu topluluğu merkez alır.","gloss":"güvenli koruma","neighbor_only":"Komşu dal, gözetme ve korumanın yanında gönenç ve rahat yaşam durumuna da uzanır.","neighbor_ref":"root_000966/B004","relation_type":"near_synonym","shared_zone":"İki dal da kişiyi koruyucu bir çevre altında güvenli ve güçlü durumda gösterir."},{"boundary_match":"partial","distinction":"Odak dalının çekirdeği koruyucu güç ve toplumsal destektir; komşu dalın çekirdeği ise çevreleyen somut yapının içinde güvenle saklamaktır.","focus_only":"Bu dal, somut yerlerin yanında kişi ve topluluk için koruyucu güç ve destekçi çevresini de kapsar.","gloss":"koruyucu güç ve sağlam sığınak","neighbor_only":"Komşu dal, bir şeyi çevreleyen sağlam yapı, zırh veya güvenli yer içinde saklamaya odaklanır.","neighbor_ref":"root_000331/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da dış tehdide karşı güvenlik sağlanır ve erişim güçleştirilir."},{"boundary_match":"field_only","distinction":"Odak dalı gücü erişilmezlik ve koruma sonucuyla sınırlar; komşu dal ise yapısal dayanak ve kişilik özellikleri dahil daha geniş bir güç alanını kapsar.","focus_only":"Bu dalda güç, korunana dışarıdan erişilmesini önleyen savunucu bir çevre olarak işler.","gloss":"koruyan güç ve dayanılan güçlü yan","neighbor_only":"Komşu dal, dayanılan güçlü yanın yanı sıra yapı temeli, önderlik, ağırbaşlılık ve kalıcılık anlamlarına uzanır.","neighbor_ref":"root_000596/B001","relation_type":"same_field","shared_zone":"Her iki dal güç, destekçi topluluk ve kişinin dayanabileceği sağlam dayanak alanını paylaşır."},{"boundary_match":"partial","distinction":"Odak dalı korunan tarafın güç ve desteğinden doğan bir erişilmezlik durumudur; komşu dal ise engelleyen tarafın kişiyi amacından uzaklaştırdığı eylemdir.","focus_only":"Bu dal, korunana ait güç ve destek sayesinde dış erişimin sonuçsuz kalmasını anlatır.","gloss":"korunaklılık ve etkin engelleme","neighbor_only":"Komşu dal, belirli bir kişiyi istediği nesne veya eylemden etkin biçimde alıkoyar.","neighbor_ref":"root_001448/B002","relation_type":"near_neighbor","shared_zone":"İki dalın ortak sonucunda bir hedefe erişim veya yaklaşma önlenir."}],"source_phrase_ar":"مكان منيع وهو في عز ومنعة (maqayis)؛ رجل منيع لا يخلص إليه وهو في عز ومنعة (ayn)؛ مكان منيع وقد منع مناعة؛ المنعة جمع مانع أي من يمنعه من عشيرته (sihah)؛ يحوطهم وينصرهم؛ في قوم يمنعونه ويحمونه (tahdhib)؛ يقال في الحماية ومنه مكان منيع وفلان ذو منعة (mufradat)","source_summary":"Kaynaklar, güçlü yer ve erişilemeyen kişi örneklerini saygınlık, koruyucu topluluk ve etkin savunma altında birleştirir; ortak sonuç korunana dışarıdan kolayca ulaşılamamasıdır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه المكان والحصن والرجل ذو المنعة، والعز الذي معه من يحمي ويمنع، ومنع الله أهل دينه بمعنى حاطهم ونصرهم.","what_is_not_ar":"ليس هو الامتناع عن الفاحشة خاصة، ولا صيغة الأمر مناع بمعنى امنع."},"support_links":["sup_56bae57de5724874af19","sup_6d79827585e756defcb3"]},{"boundary":"Anlam yalnızca kadını cinsel ahlaksızlığa yanaşmayan biri olarak niteleyen söz öbeklerine bağlıdır ve genel sakınmayı kapsamaz.","branch_kind":"collocation","branch_ref":"root_001448/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّنَعَ","morph_features":"STEM|POS:V|IMPF|LEM:m~anaEa|ROOT:mnE|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"107:7:1:2","qac_word_ref":"107:7:1","surface_ar":"يَمْنَعُ"}],"gloss":"cinsel ahlaksızlığa yanaşmayan kadın","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kadın, cinsel ahlaksızlığa yanaşmayan ve böyle bir davranışı kabul etmeyen biri olarak nitelenir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu niteleme, kadının kendini sakınan ve cinsel davranışında ölçülü oluşunu dolaylı biçimde anlatır."}}],"root_ar":"م ن ع","root_id":"root_001448","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kanıtta verilen kadın nitelemelerinin özel anlamını, genel erişilmezliğe genişletmeden karşılar.","boundary_detail":"Anlam yalnızca kadını cinsel ahlaksızlığa yanaşmayan biri olarak niteleyen söz öbeklerine bağlıdır ve genel sakınmayı kapsamaz.","branch_image_ar":"تعفف يمتنع عن الفاحشة","concept_gloss":"cinsel ahlaksızlığa yanaşmayan kadın","contextual_glosses":[{"applicability":"Kadının uygunsuz bir cinsel ilişki teklifini kabul etmediği doğrudan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadının cinsel ahlaksızlığa yanaşmaması ve teklifi reddetmesi yönünü korur."},"facet_ids":["F001"],"text":"ahlak dışı cinsel ilişkiyi reddeden kadın","usage_role":"contextual"},{"applicability":"Dolaylı nitelemenin kadının ölçülü ve sakınan tutumuyla açıklanması gereken yerlerde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına bağlı kendini sakınma ve uygunsuz ilişkiye yanaşmama niteliğini korur."},"facet_ids":["F002"],"text":"cinsel davranışında kendini sakınan kadın","usage_role":"explanatory"}],"definition":"Kadını cinsel ahlaksızlığa yanaşmayan, böyle bir ilişki teklifini kabul etmeyen ve kendini sakınan biri olarak niteleyen kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kadın, cinsel ahlaksızlığa yanaşmayan ve böyle bir davranışı kabul etmeyen biri olarak nitelenir."},{"facet_id":"F002","role":"associated_use","statement":"Bu niteleme, kadının kendini sakınan ve cinsel davranışında ölçülü oluşunu dolaylı biçimde anlatır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Toplumsal konum, fiziksel uzaklık veya genel ulaşılmazlık gibi ilgisiz nedenleri ekler.","collision":"Koruyucu güç sayesinde erişilemez olma dalıyla karışır.","fit":"broadening","loses":null,"preserves":"Kadının istenmeyen bir yakınlaşmayı kabul etmemesi görünümünü kısmen korur."},"text":"erişilmez kadın"},{"category":"alternative","error_profile":{"adds":"Yer ve fiziksel savunma anlamlarını ekler.","collision":"Koruyucu erişilmezlik dalıyla karışır.","fit":"displacement","loses":"Kadınla, cinsel davranışla ve ahlaksızlığı reddetmeyle ilgili bütün kurucu özellikleri kaybeder.","preserves":"Dış yaklaşmaya kapalı olma biçimindeki uzak görüntüyü korur."},"text":"korunaklı yer"}],"identity_rationale":"Kaynak sözü, belirli kadın nitelemelerini cinsel ahlaksızlığa yanaşmayan, kendini sakınan kadın anlamında açıklar. Dal bu kadınla sınırlı söz öbeklerine bağlıdır; yerin veya kişinin genel erişilmezliği bu özel ahlaki ve cinsel sınırı karşılamaz.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"cinsel ahlaksızlığa yanaşmayan, kendini sakınan kadın"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ahlak dışı cinsel ilişkiyi kabul etmeyen kadın"}],"lexicalization_note":"Tanım yalnızca kanıtta verilen kadın nitelemelerine bağlıdır; sıfatların tek başına genel bir ahlak veya erişilmezlik anlamı taşıdığı ileri sürülmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; cinsel sakınmışlıkla en çok örtüşen dallar ve evlilikten uzaklık ile genel koruyucu erişilmezlik arasındaki sınırlar seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı belirli kadın nitelemelerine ve teklifi kabul etmeme görünümüne bağlıdır; komşu dal ise daha geniş bir cinsel sakınmışlık alanını kapsar.","focus_only":"Bu dal, belirli kadın söz öbeklerinde uygunsuz cinsel ilişkiye yanaşmama niteliğini bildirir.","gloss":"cinsel davranışta kendini sakınma","neighbor_only":"Komşu dal, kadın dışında bedenin cinsel yönünü ve çeşitli biçimleri de sakınmışlık kapsamında anlatır.","neighbor_ref":"root_000331/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da kadının cinsel ahlaksızlıktan uzak durmasını ve kendini sakınmasını anlatır."},{"boundary_match":"partial","distinction":"Odak dalı kadın nitelemesi ve cinsel teklifin reddiyle sınırlıdır; komşu dal cinsiyet ve belirli söz öbeği sınırı olmadan daha genel özdenetimi anlatır.","focus_only":"Bu dal, kadına bağlı özel bir niteleme olarak cinsel ahlaksızlığa yanaşmamayı anlatır.","gloss":"yasak cinsel davranıştan sakınma","neighbor_only":"Komşu dal, herhangi bir kişinin yasak olandan ve baskın istekten kendini tutmasını genel olarak kapsar.","neighbor_ref":"root_001031/B001","relation_type":"near_synonym","shared_zone":"İki dal da kişinin uygunsuz cinsel davranıştan kendini geri tutması alanında örtüşür."},{"boundary_match":"field_only","distinction":"Odak dalı kadın hakkında doğrudan bir nitelemedir; komşu dal ise beden veya giysi üzerinden kurulan dolaylı anlatıma bağlıdır.","focus_only":"Bu dal, kadını doğrudan uygunsuz cinsel ilişkiyi kabul etmeyen biri olarak niteler.","gloss":"doğrudan ve dolaylı cinsel sakınmışlık","neighbor_only":"Komşu dal, giysi veya beden bölgesi üzerinden dolaylı bir anlatımla cinsel temizliği belirtir.","neighbor_ref":"root_000297/B007","relation_type":"same_field","shared_zone":"Her iki dal da cinsel ahlaksızlıktan uzak durma ve temiz davranış alanını paylaşır."},{"boundary_match":"partial","distinction":"Odak dalı ahlak dışı ilişkiyi reddeder fakat evliliği dışlamaz; komşu dalın çekirdeği ise eş ve evlilik ilişkisinden kesilmektir.","focus_only":"Bu dal, kadının uygunsuz cinsel ilişkiye yanaşmamasını ahlaki bir tutum olarak bildirir.","gloss":"cinsel sakınma ve evlilikten uzaklık","neighbor_only":"Komşu dal, eşlerden ve evlilikten uzak kalma veya hiç evlenmeme durumunu anlatır.","neighbor_ref":"root_000082/B003","relation_type":"near_neighbor","shared_zone":"İki dalda da kadın ile cinsel veya evlilik ilişkisi arasında bir uzak duruş bulunabilir."},{"boundary_match":"partial","distinction":"Odak dalı kadına ve cinsel davranışa bağlı özdenetimdir; komşu dal ise kişi ya da yerin dış güçle korunmasıdır.","focus_only":"Bu dalın erişime kapalı görünümü, kadının cinsel ahlaksızlığı kabul etmeyen tutumundan doğar.","gloss":"ahlaki sakınma ve koruyucu erişilmezlik","neighbor_only":"Komşu dalın erişilmezliği, dış koruma, güç, saygınlık ve destekçilerden doğar.","neighbor_ref":"root_001448/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal dışarıdan gelen bir yönelişin hedefe ulaşamaması görünümünü paylaşır."}],"source_phrase_ar":"امرأة منيعة متمنعة لا تؤاتى على فاحشة (ayn)؛ امرأة منعة متمنعة لا تؤاتى على فاحشة (tahdhib)؛ امرأة منيعة كناية عن العفيفة (mufradat)","source_summary":"Kaynaklar, iki yakın kadın nitelemesini cinsel ahlaksızlığı kabul etmeme ve kendini sakınma ekseninde birleştirir; kullanım kadına bağlı özel bir söz öbeğidir.","sources":["AY","TA","MU"],"what_is_ar":"يدخل فيه وصف المرأة بمنيعة أو منعة أو العفيفة التي تتمنع ولا تؤاتى على فاحشة.","what_is_not_ar":"لا يدخل فيه منيع المكان والحصن إلا من جهة الصورة العامة للامتناع والحماية."},"support_links":[]},{"boundary":"Dal yalnızca muhataba engel olmasını söyleyen kalıplaşmış buyruk sözüdür; kişi niteliği veya genel engelleme adı değildir.","branch_kind":"non_bare","branch_ref":"root_001448/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مَّنَعَ","morph_features":"STEM|POS:V|IMPF|LEM:m~anaEa|ROOT:mnE|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"107:7:1:2","qac_word_ref":"107:7:1","surface_ar":"يَمْنَعُ"}],"gloss":"Engelle!","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Muhataba bir şeyi engellemesi ya da önlemesi yönünde doğrudan buyruk verir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Buyruk, sıradan çekimli eylem yerine kalıplaşmış tek sözcüklü özel bir sözle kurulur."}}],"root_ar":"م ن ع","root_id":"root_001448","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kalıplaşmış sözün muhataba doğrudan engel olma buyruğu verdiği özel kullanımın tam karşılığıdır.","boundary_detail":"Dal yalnızca muhataba engel olmasını söyleyen kalıplaşmış buyruk sözüdür; kişi niteliği veya genel engelleme adı değildir.","branch_image_ar":"مناع صيحة أمر بالمنع","concept_gloss":"Engelle!","contextual_glosses":[{"applicability":"Bir olayın gerçekleşmesini durdurma buyruğu verilen kısa ve doğrudan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir olayın gerçekleşmesine engel olma ve muhataba doğrudan buyruk verme yönünü korur."},"facet_ids":["F001"],"text":"Önle!","usage_role":"contextual"},{"applicability":"Bir kişinin veya hareketin ilerleyişini durdurma buyruğu verilen bağlamlarda doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Muhataptan ilerleyen bir kişi veya eyleme engel olmasını isteme yönünü korur."},"facet_ids":["F001"],"text":"Önünü kes!","usage_role":"contextual"}],"definition":"Muhataba bir şeyi önlemesini veya birine engel olmasını söyleyen, kalıplaşmış tek sözcüklü bir buyruk ifadesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Muhataba bir şeyi engellemesi ya da önlemesi yönünde doğrudan buyruk verir."},{"facet_id":"F002","role":"specialization","statement":"Buyruk, sıradan çekimli eylem yerine kalıplaşmış tek sözcüklü özel bir sözle kurulur."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Genel engel ve alıkoyma adlarıyla karışır.","fit":"narrowing","loses":"Muhataba yönelen doğrudan buyruk işlevini kaybeder.","preserves":"Engelleme kavramını ad düzeyinde korur."},"text":"engel"},{"category":"confusable","error_profile":{"adds":"Kişinin iyiliği vermeyen kalıcı niteliğini ekler.","collision":"İyiliği esirgeyen kişi dalıyla karışır.","fit":"displacement","loses":"Buyruk işlevini ve muhataptan eylem isteme anlamını bütünüyle kaybeder.","preserves":"Engel olma köküyle bağlantılı uzak bir biçim benzerliğini korur."},"text":"cimri"},{"category":"alternative","error_profile":{"adds":"Bir hedefi yararlı biçimde savunma amacını ekler.","collision":"Koruyucu güç dalıyla karışır.","fit":"displacement","loses":"Doğrudan engel olma eylemini kaybeder.","preserves":"Bir tehlikenin sonucunu önleme olasılığını kısmen korur."},"text":"Koru!"}],"identity_rationale":"Kaynak sözü, bir kişiye engel olmasını buyuran kalıplaşmış tek sözcüklü bir buyruk kullanımını açıkça tanımlar. Bu kimlik, aynı ses yapısındaki cimri kişi nitelemesinden bütünüyle ayrıdır ve yalnızca bu özel buyruk işlevinde geçerlidir.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"Engelle!"}],"lexicalization_note":"Tanım, kanıtta verilen özel buyruk sözüyle sınırlıdır ve bu işlevi kökün yalın, genel anlamı olarak genişletmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; anlamsal eşdeğer bulunmadığından kalıplaşmış buyruk sözleri ve genel buyruk alanıyla yapı temelli, sınır açıklayıcı karşılaştırmalar seçildi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Yapı türleri ortaktır fakat eylem çekirdekleri ayrıdır: odak dalı engel olmayı, komşu dal bırakmayı buyurur ve anlamca birbirlerinin yerine geçmez.","focus_only":"Bu dalın kalıplaşmış buyruğu muhataptan bir şeyi engellemesini ister.","gloss":"kalıplaşmış engelle ve bırak buyrukları","neighbor_only":"Komşu dalın kalıplaşmış buyruğu muhataptan bir şeyi bırakmasını ister.","neighbor_ref":"root_000180/B004","relation_type":"same_field","shared_zone":"Her ikisi de tek sözcükle doğrudan buyruk veren kalıplaşmış sözlerdir."},{"boundary_match":"field_only","distinction":"Ortaklık yalnızca buyruk sözünün yapısındadır; odak dalı önlemeyi, komşu dal hazır bulunmayı istediği için anlamsal çekirdekleri farklıdır.","focus_only":"Bu dal, muhataba engel olma eylemini buyurur.","gloss":"kalıplaşmış eylem buyrukları","neighbor_only":"Komşu dal, muhataba hazır bulunma veya gelme eylemini buyurur.","neighbor_ref":"root_000333/B013","relation_type":"same_field","shared_zone":"İki dal da kalıplaşmış tek sözcüklü buyruk sözleri alanına girer."},{"boundary_match":"partial","distinction":"Odak dalı tek bir kalıplaşmış engelleme buyruğudur; komşu dal ise eylemin içeriğinden bağımsız genel buyruk ve yükümlülük kavramıdır.","focus_only":"Bu dal, yalnızca engel olma anlamındaki belirli kalıplaşmış buyruk sözünü kapsar.","gloss":"özel engelle buyruğu ve genel buyruk","neighbor_only":"Komşu dal, her türlü eylem isteme, yükümlü kılma ve buyruğa uyma alanını genel olarak kapsar.","neighbor_ref":"root_000051/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da konuşan kişi muhataptan bir eylemi yapmasını ister."},{"boundary_match":"field_only","distinction":"Odak dalı engelleme yönünde doğrudan buyruktur; komşu dal ise alma veya bağlı kalma yönünde isteklendirme taşıdığı için ne eylem ne de söyleyiş gücü aynıdır.","focus_only":"Bu dalda muhataba bir şeyi engellemesi yönünde kesin bir buyruk verilir.","gloss":"buyruk ve eyleme yöneltme","neighbor_only":"Komşu dalda muhatap elde etme, alma veya bir şeye bağlı kalma yönünde isteklendirilir.","neighbor_ref":"root_001052/B006","relation_type":"same_field","shared_zone":"İki dal da kısa bir sözle muhatabı belirli bir eyleme yönelten anlatım alanındadır."}],"source_phrase_ar":"مناع بمعنى امنع (ayn)؛ مناع أي امنع كقولهم نزال أي انزل (mufradat)","source_summary":"Kaynaklar, bu özel sözü aynı biçimde engel olma buyruğu olarak açıklar ve onun kalıplaşmış buyruk sözleri düzeninde bulunduğunu gösterir.","sources":["AY","MU"],"what_is_ar":"يدخل فيه مناع إذا أريد بها صيغة أمر بمعنى امنع، على مثال نزال بمعنى انزل.","what_is_not_ar":"لا يدخل فيه مناع وصفا للبخيل أو مانع الخير."},"support_links":[]},{"boundary":"Eylem iki taraflı olmalı ve taraflar aynı şey üzerinde birbirine direnmelidir; tek yönlü engelleme bu dala girmez.","branch_kind":"non_bare","branch_ref":"root_001448/B006","candidate_links":[{"candidate_id":"cand_130dc8603b8ab2890b85","lane":"micro"},{"candidate_id":"cand_5cb51a061dcac9e3a68c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّنَعَ","morph_features":"STEM|POS:V|IMPF|LEM:m~anaEa|ROOT:mnE|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"107:7:1:2","qac_word_ref":"107:7:1","surface_ar":"يَمْنَعُ"}],"gloss":"bir şey üzerinde karşılıklı engelleşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İki taraf aynı konu veya şey üzerinde birbirine karşı koyar ve karşılıklı direnç gösterir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Her iki taraf da ötekinin hareketini veya isteğini engellediği için ilişki tek yönlü değildir."}}],"root_ar":"م ن ع","root_id":"root_001448","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İki tarafın aynı şey üzerinde birbirine karşı koyduğu ve birbirini durdurduğu özel kullanımda uygundur.","boundary_detail":"Eylem iki taraflı olmalı ve taraflar aynı şey üzerinde birbirine direnmelidir; tek yönlü engelleme bu dala girmez.","branch_image_ar":"ممانعة في الشيء","concept_gloss":"bir şey üzerinde karşılıklı engelleşme","contextual_glosses":[{"applicability":"İki tarafın aynı konuda birbirinin hareketine direnç gösterdiği akıcı cümlelerde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki taraflı direnme ve karşılıklı hareketi durdurma çekirdeğini korur."},"facet_ids":["F001","F002"],"text":"birbirine karşı koyma","usage_role":"contextual"},{"applicability":"Tarafların aynı şey üzerinde birbirini durdurduğu daha kısa anlatımlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karşılıklılığı ve her iki tarafın ötekine direnç göstermesini korur."},"facet_ids":["F001"],"text":"karşılıklı direnme","usage_role":"general"}],"definition":"İki tarafın belirli bir şey üzerinde birbirine karşı koyması, birbirinin ilerleyişini engellemesi ve karşılıklı direnmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İki taraf aynı konu veya şey üzerinde birbirine karşı koyar ve karşılıklı direnç gösterir."},{"facet_id":"F002","role":"specialization","statement":"Her iki taraf da ötekinin hareketini veya isteğini engellediği için ilişki tek yönlü değildir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":"Tek yönlü alıkoyma dalıyla karışır.","fit":"narrowing","loses":"İki taraflı ve karşılıklı direnme ilişkisini kaybeder.","preserves":"Bir tarafın ötekinin hareketini durdurması yönünü korur."},"text":"engelleme"},{"category":"confusable","error_profile":{"adds":"Taraflardan birinin kesin üstünlük kurduğu sonucu ekler.","collision":"Üstün gelme ve boyun eğdirme dallarıyla karışır.","fit":"displacement","loses":"Süren karşılıklı engelleşme ve direnme ilişkisini kaybeder.","preserves":"İki karşıt tarafın bulunduğu mücadele görünümünü korur."},"text":"yenme"},{"category":"alternative","error_profile":{"adds":null,"collision":"Sözlü anlaşmazlık ve çekişme kullanımlarıyla karışır.","fit":"narrowing","loses":"Sözlü olmayan karşı koyma ve birbirinin hareketini engelleme kapsamını kaybeder.","preserves":"İki tarafın aynı konu üzerinde karşı karşıya gelmesini korur."},"text":"tartışma"}],"identity_rationale":"Kaynak sözü, iki taraf arasında belirli bir şey üzerinde gerçekleşen karşılıklı direnme ve engelleşmeyi gösterir. Karşılıklılık bu dalın kurucu özelliğidir; bir tarafın ötekini tek yönlü olarak alıkoyması aynı anlamı vermez.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bir şey üzerinde onunla karşılıklı engelleşmek"}],"lexicalization_note":"Tanım yalnızca kanıtta verilen karşılıklı eylem biçimine bağlıdır ve bunu yalın kökün tek taraflı engelleme anlamına yaymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; karşılıklı mücadele ve çekişme dallarıyla, üstün gelme sonucu ve tek yönlü engelleme arasındaki temel sınırlar seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı aynı şey üzerindeki karşılıklı engelleşmeyi gerektirir; komşu dal ise daha geniş mücadele ve karşılaşma durumlarını kapsar.","focus_only":"Bu dal, iki tarafın belirli bir şey üzerinde birbirini engellemesine bağlı özel bir karşılıklı eylemdir.","gloss":"karşılıklı direnme ve mücadele","neighbor_only":"Komşu dal, savaş, güreş veya başka karşılaşmalarda birbirinin karşısına dikilme ve mücadele etme kapsamına uzanır.","neighbor_ref":"root_001273/B014","relation_type":"near_synonym","shared_zone":"Her iki dalda da iki taraf birbirinin karşısına çıkar ve ötekinin ilerleyişine direnç gösterir."},{"boundary_match":"partial","distinction":"Odak dalı engel olma ve direnme çekirdeğine bağlıdır; komşu dalın çekişme alanı sözlü, törensel veya nesne alışverişine dayalı çeşitli eylemleri de içerir.","focus_only":"Bu dalın çekirdeği, bir şey üzerinde iki tarafın birbirinin hareketini engellemesidir.","gloss":"karşılıklı engelleşme ve çekişme","neighbor_only":"Komşu dal, sözlü çekişme, kanıt yarıştırma, kapışma ve başka karşılıklı alışveriş biçimlerine uzanır.","neighbor_ref":"root_001489/B006","relation_type":"near_synonym","shared_zone":"İki dal da tarafların aynı nesne veya konu üzerinde karşılıklı biçimde birbirine karşı çıkmasını kapsar."},{"boundary_match":"partial","distinction":"Odak dalında karşılıklı engelleme kurucudur; komşu dalda ise karşılık verme benzer davranış, yarışma veya oyalama biçiminde gerçekleşebilir.","focus_only":"Bu dalda iki taraf aynı şey üzerinde birbirinin ilerleyişini doğrudan engeller.","gloss":"karşılıklı direnme ve yarışmalı karşılık","neighbor_only":"Komşu dal, oyalama, tartışmada karşılık verme, yarışma ve başkasının eylemini yineleme biçimlerine uzanır.","neighbor_ref":"root_001396/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal, iki tarafın birbirine karşılık verdiği ve ötekinin hareketine göre konum aldığı durumları paylaşır."},{"boundary_match":"partial","distinction":"Odak dalı karşılıklı engelleşme aşamasında kalır; komşu dal ise bu karşılaşmanın bir tarafın üstünlüğüyle sonuçlanmasını kurucu anlam yapar.","focus_only":"Bu dal, üstünlük sonucu gerektirmeyen ve süren iki taraflı direnme ilişkisini anlatır.","gloss":"direnme ve üstün gelme","neighbor_only":"Komşu dal, karşı tarafı yenip ona üstün gelme ve boyun eğdirme sonucuna odaklanır.","neighbor_ref":"root_001008/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda karşı karşıya gelen taraflar arasında güç ve karşı koyma ilişkisi bulunur."},{"boundary_match":"partial","distinction":"Odak dalı iki taraflı karşı koymayı zorunlu kılar; komşu dalın çekirdeğinde karşılıklılık yoktur ve tek bir engelleyen yeterlidir.","focus_only":"Bu dalda her iki taraf da ötekine direnerek karşılıklı biçimde engel olur.","gloss":"karşılıklı ve tek yönlü engelleme","neighbor_only":"Komşu dalda bir taraf diğerini istediği şeyden tek yönlü olarak alıkoyabilir.","neighbor_ref":"root_001448/B002","relation_type":"near_neighbor","shared_zone":"İki dal da bir tarafın hareket veya amacının başka bir direnç yüzünden kesilmesini anlatır."}],"source_phrase_ar":"مانعته الشئ ممانعة (sihah)","source_qualifications":[{"kind":"sole_attestation","summary":"Tek tanıklık, belirli bir şey üzerinde iki taraflı karşı koyma ve engelleşme kullanımını kaydeder."}],"source_summary":"Dal için kaynaklar arasında ortaklaştırılacak ayrı bir iddia yoktur; kullanım tek bir sözlük tanıklığıyla sınırlıdır.","sources":["SI"],"what_is_ar":"يدخل فيه مانعته الشيء ممانعة، أي وقع بينهما دفع وممانعة متبادلة في الشيء.","what_is_not_ar":"لا يدخل فيه منع واحد لآخر من الشيء بلا صيغة مفاعلة."},"support_links":["sup_16c5a1546ecc239a9f6c","sup_dcb50e4cfd223759194e"]},{"boundary":"Dal yalnızca adı verilen iki genç dişi hayvanın yıl veya zaman karşısındaki dayanma tasviridir; genel gençlik ya da her türlü direnme anlamına genişletilemez.","branch_kind":"non_bare","branch_ref":"root_001448/B007","candidate_links":[{"candidate_id":"cand_d2a97663f2abb528cc27","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مَّنَعَ","morph_features":"STEM|POS:V|IMPF|LEM:m~anaEa|ROOT:mnE|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"107:7:1:2","qac_word_ref":"107:7:1","surface_ar":"يَمْنَعُ"}],"gloss":"çetin yıla direnen genç dişi deve ile dişi oğlak","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Özel adlandırma, genç dişi deve ile dişi oğlağı tek bir hayvan ikilisi olarak gösterir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İki hayvan, çetin yıla veya zamana karşı kendilerini savunan varlıklar gibi benzetmeli biçimde tasvir edilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Dayanmanın gençlikten geldiği açıklaması tanıklıklardan birinde açıkken toplu neden anlatımı tam bir birlik göstermez."}}],"root_ar":"م ن ع","root_id":"root_001448","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalnızca kanıtta birlikte adlandırılan iki genç dişi hayvanın zamana dayanma tasvirini karşılar.","boundary_detail":"Dal yalnızca adı verilen iki genç dişi hayvanın yıl veya zaman karşısındaki dayanma tasviridir; genel gençlik ya da her türlü direnme anlamına genişletilemez.","branch_image_ar":"فتاء يقاوم السنة","concept_gloss":"çetin yıla direnen genç dişi deve ile dişi oğlak","contextual_glosses":[{"applicability":"Özel adlandırmanın iki hayvanı zaman karşısında birlikte dayanır gösteren benzetmesi açıklanırken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İki genç dişi hayvanı ve zaman karşısındaki ortak dayanma tasvirini korur."},"facet_ids":["F001","F002"],"text":"zamana direnen genç dişi hayvan ikilisi","usage_role":"explanatory"},{"applicability":"Dayanmanın gençliğe bağlandığı tanıklığın özellikle izlendiği bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Gençliği dayanma nedeni yapan kaynak değişkenini ve iki hayvanın ortak tasvirini korur."},"facet_ids":["F001","F002","F003"],"text":"gençlikleriyle çetin yıla dayanan iki hayvan","usage_role":"contextual"}],"definition":"Genç dişi deve ile dişi oğlağı, çetin yılın veya zamanın etkisine karşı kendilerini savunan iki genç hayvan olarak birlikte adlandıran özel bir kullanımdır. Gençlikleri bu dayanmanın bir açıklaması olarak verilir, ancak neden anlatımı kaynaklar arasında tam olarak birleşmez.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Özel adlandırma, genç dişi deve ile dişi oğlağı tek bir hayvan ikilisi olarak gösterir."},{"facet_id":"F002","role":"associated_use","statement":"İki hayvan, çetin yıla veya zamana karşı kendilerini savunan varlıklar gibi benzetmeli biçimde tasvir edilir."},{"facet_id":"F003","role":"source_variant","statement":"Dayanmanın gençlikten geldiği açıklaması tanıklıklardan birinde açıkken toplu neden anlatımı tam bir birlik göstermez."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"Tür ve cinsiyet ayrımı olmadan bütün genç hayvanları kapsama ekler.","collision":"Genel hayvan gençliği dalıyla karışır.","fit":"broadening","loses":null,"preserves":"Adlandırılan iki hayvanın genç oluşunu korur."},"text":"genç hayvanlar"},{"category":"alternative","error_profile":{"adds":"İnsanlar ve başka bütün direnç gösteren varlıkları kapsama ekler.","collision":"Genel karşı koyma ve direnme dallarıyla karışır.","fit":"broadening","loses":null,"preserves":"Zaman karşısında dayanma ve karşı koyma tasvirini korur."},"text":"direnenler"},{"category":"confusable","error_profile":{"adds":"Kuraklıkta yaşayan her hayvanı kapsayan bir sınıf anlamı ekler.","collision":"Kıtlık yılı ve zayıf hayvan dallarıyla karışır.","fit":"displacement","loses":"Belirli genç dişi deve ile dişi oğlak ikilisini ve zamana karşı savunma benzetmesini kaybeder.","preserves":"Çetin yıl koşullarında bulunan hayvanlar görünümünü korur."},"text":"kuraklık hayvanları"}],"identity_rationale":"Kaynak sözü, genç dişi deve ile dişi oğlağı birlikte adlandırır ve onları zamana ya da çetin yıla karşı kendilerini savunan iki hayvan olarak açıklar. Ancak toplu tanıklık, bu dayanmanın nedenini bir yerde açıkça gençliğe bağlarken başka bir yerde farklı bir neden sözü verir; bu yüzden gençlik açıklaması ortak çekirdeğin zorunlu parçası değil, kaynak değişkeni olarak tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"gençlikleriyle çetin yıla direnen ve yetişkin hayvanlardan önce doyan genç dişi deve ile dişi oğlak"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"çetin yıla karşı koyan ve yetişkin hayvanlardan önce doyan genç dişi deve ile dişi oğlak"}],"lexicalization_note":"Tanım, adı verilen hayvan ikilisine özgü kalıplaşmış kullanımı korur; bunu yalın kökün genel direnme veya gençlik anlamı saymaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel hayvan gençliği, kıtlık yılı, uzun süreli hayvan dayanıklılığı ve kaynak tükenmesiyle kurulan karşılaştırmalar özel ikilinin sınırını en açık biçimde gösterir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalı iki belirli dişi hayvan ve zamana dayanma tasviriyle sınırlıdır; komşu dal ise türler arasında genel gençlik evresini anlatır.","focus_only":"Bu dal, belirli genç dişi deve ile dişi oğlağı çetin yıla direnen özel bir ikili olarak adlandırır.","gloss":"özel genç hayvan ikilisi ve genel hayvan gençliği","neighbor_only":"Komşu dal, farklı hayvan türlerinde gelişimini tamamlamamış olma durumunu genel olarak anlatır.","neighbor_ref":"root_000143/B003","relation_type":"near_neighbor","shared_zone":"İki dal da henüz tam yetişmemiş genç hayvanları konu edinir."},{"boundary_match":"thematic_only","distinction":"Odak dalının göndergesi bu koşula direnen iki hayvandır; komşu dalın göndergesi ise zorlu ve verimsiz yılın kendisidir, bu nedenle anlamsal örtüşme değil senaryo ortaklığı vardır.","focus_only":"Bu dal, genç hayvanların çetin yıl karşısındaki dayanışını ve savunmasını anlatır.","gloss":"çetin yıla dayanan hayvanlar ve çetin yıl","neighbor_only":"Komşu dal, bitki örtüsü bulunmayan beyaz ve kıtlık getiren yılın kendisini anlatır.","neighbor_ref":"root_000821/B007","relation_type":"thematic","shared_zone":"İki dal aynı kıtlık ve zorlu yıl görünümünde yer alır."},{"boundary_match":"partial","distinction":"Odak dalı iki türden genç hayvanın özel ortak adıdır ve benzetmeli direniş taşır; komşu dal ise dişi devenin süreklilik ve süt verme özelliğini kurucu anlam yapar.","focus_only":"Bu dal, iki genç dişi hayvanı zamanla savaşır gibi gösteren özel bir adlandırmadır.","gloss":"gençlikle direnme ve kalıcı dayanıklılık","neighbor_only":"Komşu dal, dişi devenin soğuk ve kıtlık boyunca süt vermeyi sürdürmesi ve kalıcı dayanıklılığına odaklanır.","neighbor_ref":"root_000882/B007","relation_type":"near_neighbor","shared_zone":"Her iki dal da dişi hayvanların zorlu mevsim veya kıtlık koşullarında dayanmasını anlatır."},{"boundary_match":"thematic_only","distinction":"Odak dalının çekirdeği belirli genç hayvanların dayanmasıdır; komşu dalın çekirdeği ise su veya sütün kesilmesi olduğundan yalnızca konu çevresi ortaktır.","focus_only":"Bu dalda genç dişi hayvanlar zorlu yıl karşısında dayanabilen varlıklar olarak sunulur.","gloss":"zorlu yılda dayanma ve kaynak tükenmesi","neighbor_only":"Komşu dal, suyun veya sütün azalması, kesilmesi ve hayvanın memesinin kurumasını anlatır.","neighbor_ref":"root_000227/B011","relation_type":"thematic","shared_zone":"İki dal, kıtlık ve hayvanların beslenme koşullarının zorlaştığı aynı çevresel senaryoda buluşur."}],"source_phrase_ar":"المتمنعان البكرة والعناق تمتنعان على السنة بفتائهما (sihah)؛ المتمنعتان البكرة والعناق تمنعان على السنة لفنائهما (tahdhib)؛ المقاتلتان للزمان عن أنفسهما (sihah;tahdhib)","source_summary":"Kaynaklar aynı genç dişi hayvan ikilisini zamanla savaşır gibi dayanma tasviri altında birleştirir; dayanmanın gençlikten kaynaklandığı açıklamasının söylenişi ise toplu tanıklıkta değişkenlik gösterir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه المتمنعتان: البكرة والعناق، لأنهما تمتنعان على السنة بفتائهما وتشبعان قبل الجلة، كأنهما تقاتلان الزمان عن أنفسهما.","what_is_not_ar":"لا يدخل فيه كل امتناع عام ولا كل منعة حماية بشرية."},"support_links":["sup_56bae57de5724874af19"]}],"candidate_inventory":[{"anchor_refs":["107:7:1"],"branch_refs":[],"candidate_id":"cand_83114590ae5bd36b0f86","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:7:1:accusation-chain-continuation","source_type":"word_analysis","support_ids":["sup_a9a8881493d0d377836f","sup_d721f7eaad2f02278dc2"],"title":"connector keeps the final clause in the accusation chain","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:1","qac_refs":["107:7:1:1"],"status":"accepted"}},{"anchor_refs":["107:7:1"],"branch_refs":[],"candidate_id":"cand_eec57f242d3da35a22b1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:7:1:coda-like-resumption","source_type":"word_analysis","support_ids":["sup_a9a8881493d0d377836f","sup_edb54af48034149d5209"],"title":"final connector can feel like a closing coda","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:1","qac_refs":["107:7:1:1"],"status":"accepted"}},{"anchor_refs":["107:7:1"],"branch_refs":[],"candidate_id":"cand_7d9eb0cf82042c634d5b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:7:1:fused-proclitic-flow","source_type":"word_analysis","support_ids":["sup_49b69aded7d23cccddfa","sup_a9a8881493d0d377836f"],"title":"attached onset makes continuation audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:1","qac_refs":["107:7:1:1"],"status":"accepted"}},{"anchor_refs":["107:7:2"],"branch_refs":[],"candidate_id":"cand_90758bec0b1c5a7b7564","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001448"],"scope":"focus_ayah","source_local_id":"107:7:2:barrier-withholding-image","source_type":"word_analysis","support_ids":["sup_52756ee6e0537b6e0cbf","sup_b27f0c5ba7290385ddcc"],"title":"withholding becomes barrier-making against aid","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:2","qac_refs":["107:7:1:2","107:7:1:3"],"status":"accepted"}},{"anchor_refs":["107:7:2"],"branch_refs":[],"candidate_id":"cand_c84e595756f42610c466","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001448"],"scope":"focus_ayah","source_local_id":"107:7:2:compact-final-verdict","source_type":"word_analysis","support_ids":["sup_39f36d84ddf421456761","sup_b27f0c5ba7290385ddcc"],"title":"single verbal clause closes without padding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:2","qac_refs":["107:7:1:2","107:7:1:3"],"status":"accepted"}},{"anchor_refs":["107:7:2"],"branch_refs":[],"candidate_id":"cand_e0fe59b1f83ef416271b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001448"],"scope":"focus_ayah","source_local_id":"107:7:2:compressed-withholding-frame","source_type":"word_analysis","support_ids":["sup_075260331ca6407aae46","sup_b27f0c5ba7290385ddcc"],"title":"named object and unnamed recipient compress the harm","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:2","qac_refs":["107:7:1:2","107:7:1:3"],"status":"accepted"}},{"anchor_refs":["107:7:2"],"branch_refs":[],"candidate_id":"cand_33bf4240d57aea6b22bd","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001448"],"scope":"focus_ayah","source_local_id":"107:7:2:display-to-obstruction-pivot","source_type":"word_analysis","support_ids":["sup_607c9e93807813e8914e","sup_b27f0c5ba7290385ddcc"],"title":"boundary shifts from public display to direct refusal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:2","qac_refs":["107:7:1:2","107:7:1:3"],"status":"accepted"}},{"anchor_refs":["107:7:2"],"branch_refs":[],"candidate_id":"cand_61c031a0676dd5f28b82","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001448"],"scope":"focus_ayah","source_local_id":"107:7:2:ongoing-active-plural","source_type":"word_analysis","support_ids":["sup_b27f0c5ba7290385ddcc","sup_b33afc3c0ab1e1c7adbe"],"title":"imperfect plural makes withholding habitual and agentive","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:2","qac_refs":["107:7:1:2","107:7:1:3"],"status":"accepted"}},{"anchor_refs":["107:7:2"],"branch_refs":[],"candidate_id":"cand_3723b9f9797c24dd543b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001448"],"scope":"focus_ayah","source_local_id":"107:7:2:preventer-character-profile","source_type":"word_analysis","support_ids":["sup_8b1b8831191a5714a59b","sup_b27f0c5ba7290385ddcc"],"title":"finite verb participates in a preventer character field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:2","qac_refs":["107:7:1:2","107:7:1:3"],"status":"accepted"}},{"anchor_refs":["107:7:2"],"branch_refs":[],"candidate_id":"cand_9907a15d448f5dfd1d77","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001448"],"scope":"focus_ayah","source_local_id":"107:7:2:sound-bound-to-object","source_type":"word_analysis","support_ids":["sup_a58875d7ff7e972d3ade","sup_b27f0c5ba7290385ddcc"],"title":"verb sound collides with the aid noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:2","qac_refs":["107:7:1:2","107:7:1:3"],"status":"accepted"}},{"anchor_refs":["107:7:3"],"branch_refs":[],"candidate_id":"cand_74b4fc96366e2b3d92bc","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:7:3:circulation-and-due-aid","source_type":"word_analysis","support_ids":["sup_473cac397203d99c0964","sup_a092e25661615026fdb6"],"title":"aid is imagined as circulating and due","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:3","qac_refs":["107:7:2:1","107:7:2:2"],"status":"accepted"}},{"anchor_refs":["107:7:3"],"branch_refs":[],"candidate_id":"cand_44b10cefcdea1796d4ef","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:7:3:concrete-and-broad-aid-range","source_type":"word_analysis","support_ids":["sup_245cd9b485a31f48c87f","sup_a092e25661615026fdb6"],"title":"concrete utilities and broader assistance stay together","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:3","qac_refs":["107:7:2:1","107:7:2:2"],"status":"accepted"}},{"anchor_refs":["107:7:3"],"branch_refs":[],"candidate_id":"cand_9f54975df6291e7301c4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:7:3:definite-aid-category","source_type":"word_analysis","support_ids":["sup_61b2780b880100e01bca","sup_a092e25661615026fdb6"],"title":"definite singular gathers aid into one known class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:3","qac_refs":["107:7:2:1","107:7:2:2"],"status":"accepted"}},{"anchor_refs":["107:7:3"],"branch_refs":[],"candidate_id":"cand_99cb0d090ddef3d595da","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:7:3:direct-object-visible","source_type":"word_analysis","support_ids":["sup_a092e25661615026fdb6","sup_e86791c75cc04393dcba"],"title":"object slot fixes what is blocked","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:3","qac_refs":["107:7:2:1","107:7:2:2"],"status":"accepted"}},{"anchor_refs":["107:7:3"],"branch_refs":[],"candidate_id":"cand_a047317ebf672c2bf58a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:7:3:help-root-social-inversion","source_type":"word_analysis","support_ids":["sup_618522178f6a78696a31","sup_a092e25661615026fdb6"],"title":"help-family meaning is inverted by withholding","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:3","qac_refs":["107:7:2:1","107:7:2:2"],"status":"accepted"}},{"anchor_refs":["107:7:3"],"branch_refs":[],"candidate_id":"cand_82c864c6f633a66a052e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:7:3:instrumental-help-means","source_type":"word_analysis","support_ids":["sup_1d5e2770189485780daf","sup_a092e25661615026fdb6"],"title":"aid appears as a usable means","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:3","qac_refs":["107:7:2:1","107:7:2:2"],"status":"accepted"}},{"anchor_refs":["107:7:3"],"branch_refs":[],"candidate_id":"cand_4cbfaae30e1983af7113","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:7:3:social-denial-return","source_type":"word_analysis","support_ids":["sup_9bb9c7f9653c88593999","sup_a092e25661615026fdb6"],"title":"final object returns the surah's social-denial motif","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:3","qac_refs":["107:7:2:1","107:7:2:2"],"status":"accepted"}},{"anchor_refs":["107:7:3"],"branch_refs":[],"candidate_id":"cand_6acd155178269a90a98d","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:7:3:sound-and-rhyme-closure","source_type":"word_analysis","support_ids":["sup_453f03fda28c00e25463","sup_a092e25661615026fdb6"],"title":"final cadence ties aid to withholding and display","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:3","qac_refs":["107:7:2:1","107:7:2:2"],"status":"accepted"}},{"anchor_refs":["107:7:3"],"branch_refs":[],"candidate_id":"cand_76f1be66cd99e5283b0b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:7:3:surah-closing-seal","source_type":"word_analysis","support_ids":["sup_584447b6725a844718c8","sup_a092e25661615026fdb6"],"title":"final noun bears the closing load","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:7:3","qac_refs":["107:7:2:1","107:7:2:2"],"status":"accepted"}},{"anchor_refs":["107:7:1"],"branch_refs":[],"candidate_id":"cand_d66f7b84cc3cb5513c32","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001448"],"scope":"focus_ayah","source_local_id":"107:7:1:2","source_type":"qac_morpheme","support_ids":["sup_03deea50b42f5723dcbf"],"title":"QAC root occurrence: م ن ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["107:7:2"],"branch_refs":[],"candidate_id":"cand_e3d22767cbc87ad7752a","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001064"],"scope":"focus_ayah","source_local_id":"107:7:2:2","source_type":"qac_morpheme","support_ids":["sup_625a10197e525b759d66"],"title":"QAC root occurrence: م ع ن","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["107:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:7","branch_refs":["root_001064/B001","root_001448/B001"],"candidate_id":"cand_1ada1cb61f24493b6fb0","commentary_obligation":"review","hft_ref":"hft_4e1186614a38e7e8ca9b","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_blocked_transfer","source_type":"hft","support_ids":["sup_f01fe84a10b06f030164"],"title":"baseline_blocked_transfer","trust":"legacy_unbound"},{"anchor_refs":["107:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:7","branch_refs":["root_001064/B001","root_001448/B002","root_001448/B003"],"candidate_id":"cand_404e78531ed488d25bde","commentary_obligation":"review","hft_ref":"hft_0b996d17590ce4033c71","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_gatekept_access","source_type":"hft","support_ids":["sup_6d79827585e756defcb3"],"title":"baseline_gatekept_access","trust":"legacy_unbound"},{"anchor_refs":["107:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:7","branch_refs":["root_001064/B001","root_001448/B006"],"candidate_id":"cand_130dc8603b8ab2890b85","commentary_obligation":"review","hft_ref":"hft_d5a8138ecba6ed83c933","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_contested_mutuality","source_type":"hft","support_ids":["sup_dcb50e4cfd223759194e"],"title":"baseline_contested_mutuality","trust":"legacy_unbound"},{"anchor_refs":["107:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:7","branch_refs":["root_001064/B001","root_001448/B003","root_001448/B007"],"candidate_id":"cand_d2a97663f2abb528cc27","commentary_obligation":"review","hft_ref":"hft_ac06480434d4ed64350a","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:baseline_protective_reserve","source_type":"hft","support_ids":["sup_56bae57de5724874af19"],"title":"baseline_protective_reserve","trust":"legacy_unbound"},{"anchor_refs":["107:7"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:7","branch_refs":["root_001064/B003","root_001448/B006"],"candidate_id":"cand_5cb51a061dcac9e3a68c","commentary_obligation":"review","hft_ref":"hft_c0b893207a1e468da9ff","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:outlier_cooperation_becomes_repeated_war","source_type":"hft","support_ids":["sup_16c5a1546ecc239a9f6c"],"title":"outlier_cooperation_becomes_repeated_war","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"وَيَمْنَعُونَ ٱلْمَاعُونَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"107:7:1:1","qac_word_ref":"107:7:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَّنَعَ","morph_features":"STEM|POS:V|IMPF|LEM:m~anaEa|ROOT:mnE|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"107:7:1:2","qac_word_ref":"107:7:1","root_ar":"م ن ع","surface_ar":"يَمْنَعُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"107:7:1:3","qac_word_ref":"107:7:1","root_ar":"","surface_ar":"ونَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"107:7:2:1","qac_word_ref":"107:7:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مَاعُون","morph_features":"STEM|POS:N|LEM:maAEuwn|ROOT:mEn|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:7:2:2","qac_word_ref":"107:7:2","root_ar":"م ع ن","surface_ar":"مَاعُونَ"}],"word_analysis_qac_refs":[["107:7:1:1"],["107:7:1:2","107:7:1:3"],["107:7:2:1","107:7:2:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["107:7:1","107:7:2","107:7:3"]},"focus_surface_evidence":{"arabic_uthmani":"وَيَمْنَعُونَ ٱلْمَاعُونَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|w:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"107:7:1:1","qac_word_ref":"107:7:1","root_ar":"","surface_ar":"وَ"},{"lemma_ar":"مَّنَعَ","morph_features":"STEM|POS:V|IMPF|LEM:m~anaEa|ROOT:mnE|3MP","morpheme_role":"STEM","pos":"V","qac_ref":"107:7:1:2","qac_word_ref":"107:7:1","root_ar":"م ن ع","surface_ar":"يَمْنَعُ"},{"lemma_ar":"","morph_features":"SUFFIX|PRON:3MP","morpheme_role":"SUFFIX","pos":"PRON","qac_ref":"107:7:1:3","qac_word_ref":"107:7:1","root_ar":"","surface_ar":"ونَ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"107:7:2:1","qac_word_ref":"107:7:2","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"مَاعُون","morph_features":"STEM|POS:N|LEM:maAEuwn|ROOT:mEn|M|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:7:2:2","qac_word_ref":"107:7:2","root_ar":"م ع ن","surface_ar":"مَاعُونَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["107:7:1:1"],["107:7:1:2","107:7:1:3"],["107:7:2:1","107:7:2:2"]],"word_analysis_refs":["107:7:1","107:7:2","107:7:3"],"word_rows":[{"analysis_record_ref":"107:7:1","analytic_gloss_range_en":"coordinating conjunction that carries the final verbal clause forward from the preceding accusation chain, with a possible coda-like rhetorical force","analytic_root_gloss_range_en":null,"qac_refs":["107:7:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"وَ","transliteration":"wa"}},{"analysis_record_ref":"107:7:2","analytic_gloss_range_en":"they withhold, prevent, or block access; locally an active plural imperfect governing the basic aid as its direct object","analytic_root_gloss_range_en":"root field includes withholding, barring access, protective inaccessibility, and intensive preventer traits; the local clause selects active withholding of aid while allowing barrier imagery and character pressure","qac_refs":["107:7:1:2","107:7:1:3"],"root":{"arabic":"م ن ع","transliteration":"m-n-ʿ"},"surface":{"arabic":"يَمْنَعُونَ","transliteration":"yamnaʿūna"}},{"analysis_record_ref":"107:7:3","analytic_gloss_range_en":"the basic aid, useful assistance, lendable utility, or small due help withheld as the direct object","analytic_root_gloss_range_en":"helping and backing is the locally relevant root branch; broader homonymous or unrelated branches in the dictionary do not control this noun","qac_refs":["107:7:2:1","107:7:2:2"],"root":{"arabic":"ع و ن","transliteration":"ʿ-w-n"},"surface":{"arabic":"ٱلْمَاعُونَ","transliteration":"al-māʿūna"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":5,"assigned_records":[{"anchor_refs":["107:7"],"branch_refs":["root_001064/B001","root_001448/B001"],"candidate_id":"cand_1ada1cb61f24493b6fb0","evidence_scope":"focus_ayah","hft_ref":"hft_4e1186614a38e7e8ca9b","item_id":"baseline_blocked_transfer","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_blocked_transfer","support_id":"sup_f01fe84a10b06f030164"},{"anchor_refs":["107:7"],"branch_refs":["root_001064/B001","root_001448/B002","root_001448/B003"],"candidate_id":"cand_404e78531ed488d25bde","evidence_scope":"focus_ayah","hft_ref":"hft_0b996d17590ce4033c71","item_id":"baseline_gatekept_access","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_gatekept_access","support_id":"sup_6d79827585e756defcb3"},{"anchor_refs":["107:7"],"branch_refs":["root_001064/B001","root_001448/B006"],"candidate_id":"cand_130dc8603b8ab2890b85","evidence_scope":"focus_ayah","hft_ref":"hft_d5a8138ecba6ed83c933","item_id":"baseline_contested_mutuality","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_contested_mutuality","support_id":"sup_dcb50e4cfd223759194e"},{"anchor_refs":["107:7"],"branch_refs":["root_001064/B001","root_001448/B003","root_001448/B007"],"candidate_id":"cand_d2a97663f2abb528cc27","evidence_scope":"focus_ayah","hft_ref":"hft_ac06480434d4ed64350a","item_id":"baseline_protective_reserve","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:baseline_protective_reserve","support_id":"sup_56bae57de5724874af19"},{"anchor_refs":["107:7"],"branch_refs":["root_001064/B003","root_001448/B006"],"candidate_id":"cand_5cb51a061dcac9e3a68c","evidence_scope":"focus_ayah","hft_ref":"hft_c0b893207a1e468da9ff","item_id":"outlier_cooperation_becomes_repeated_war","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:outlier_cooperation_becomes_repeated_war","support_id":"sup_16c5a1546ecc239a9f6c"}],"diagnostics":[],"lane_counts":{"global":10,"macro":13,"micro":5},"packet_summary":{"ayah_count":7,"focus_ref":"107:7","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"د ع ع","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000477","furuq_root_norm":"د ع ع","furuq_source_root_norm":"د ع ع","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000478","furuq_root_norm":"د ع و","furuq_source_root_norm":"د ع و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]}],"window":["107:1","107:2","107:3","107:4","107:5","107:6","107:7"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"107:7","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":10,"source_present":true,"structured_insight_count":18,"unstructured_record_count":0},"identity":{"ayah_ref":"107:7","lane":"micro","linguistic_source_ref":"107:7","surface_ref":"107:7","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"107:7","target_tokens":[["Yardımı",["107:7:2"]],["da",["107:7:1"]],["esirgerler",["107:7:1"]]],"text":"Yardımı da esirgerler."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":5,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":7,"id":"s107-p01-001-007","label":"Whole surah","number":1,"refs":["107:1","107:2","107:3","107:4","107:5","107:6","107:7"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"107:7:1:2","source_type":"qac_morpheme","support_id":"sup_03deea50b42f5723dcbf","text":"{\"lemma_ar\":\"مَّنَعَ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:m~anaEa|ROOT:mnE|3MP\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"107:7:1:2\",\"qac_word_ref\":\"107:7:1\",\"root_ar\":\"م ن ع\",\"surface_ar\":\"يَمْنَعُ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:2:compressed-withholding-frame","source_type":"word_analysis","support_id":"sup_075260331ca6407aae46","text":"{\"blocking_evidence\":null,\"headline\":\"named object and unnamed recipient compress the harm\",\"reader_payoff\":\"The reader notices that the clause specifies the aid being blocked while leaving the denied person open-ended, widening the social harm.\",\"reason\":\"Attachment evidence syntactically forces {{ar:ٱلْمَاعُونَ}} ({{tr:al-māʿūna}}) as the explicit direct object, while no overt recipient is supplied.\",\"representative_source_ids\":[\"QG-0a4836b5\",\"QG-132ca8f8\",\"QS-7c989101\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:3:instrumental-help-means","source_type":"word_analysis","support_id":"sup_1d5e2770189485780daf","text":"{\"blocking_evidence\":null,\"headline\":\"aid appears as a usable means\",\"reader_payoff\":\"The reader notices that the final object is not just the idea of help but the usable means by which another person is actually helped.\",\"reason\":\"QAC describes the noun as a concrete noun on a useful or given-help pattern, and the local object role makes that utility the thing withheld.\",\"representative_source_ids\":[\"QF-2d2565b9\",\"QF-f50bd52a\",\"QS-7d5ebf1b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:3:concrete-and-broad-aid-range","source_type":"word_analysis","support_id":"sup_245cd9b485a31f48c87f","text":"{\"blocking_evidence\":null,\"headline\":\"concrete utilities and broader assistance stay together\",\"reader_payoff\":\"The reader notices that the noun can hold small tools, ordinary kindness, useful assistance, and due aid together under the local core of help that should circulate.\",\"reason\":\"The help-and-backing branch is locally relevant, but the broad lexicographic range is narrowed to the shared aid core selected by the governing withholding verb; speculative modern extensions are not carried into the prose.\",\"representative_source_ids\":[\"QS-20c0b396\",\"QS-76d183dd\",\"MS-8dde158c\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:2:compact-final-verdict","source_type":"word_analysis","support_id":"sup_39f36d84ddf421456761","text":"{\"blocking_evidence\":null,\"headline\":\"single verbal clause closes without padding\",\"reader_payoff\":\"The reader notices how little syntax is needed for the closing verdict: connector, withholding verb, and object.\",\"reason\":\"Attachment evidence treats 107:7 as one coordinated verbal clause whose verb governs one explicit object.\",\"representative_source_ids\":[\"QT-ac253339\",\"QB-fbff44ab\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:3:sound-and-rhyme-closure","source_type":"word_analysis","support_id":"sup_453f03fda28c00e25463","text":"{\"blocking_evidence\":null,\"headline\":\"final cadence ties aid to withholding and display\",\"reader_payoff\":\"The reader notices that the final aid noun answers the withholding verb and the prior ayah ending in sound, so the last two accusations close together.\",\"reason\":\"The adjacent verb-object pair and the prior ayah ending share long-vowel and final-n cadence, making the closure audible without changing the lexical sense.\",\"representative_source_ids\":[\"QE-09e75a20\",\"QE-33b60e0c\",\"QP-d89be4ad\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:3:circulation-and-due-aid","source_type":"word_analysis","support_id":"sup_473cac397203d99c0964","text":"{\"blocking_evidence\":null,\"headline\":\"aid is imagined as circulating and due\",\"reader_payoff\":\"The reader notices that the offense sharpens because the withheld thing is small, useful, and socially expected to move toward need.\",\"reason\":\"The circulation, smallness, and obligatory-aid notes are kept as semantic pressure inside the aid range, but narrowed so they do not replace the local direct-object sense with a single specialized definition.\",\"representative_source_ids\":[\"QS-208fa0e2\",\"QS-411adf24\",\"QS-bcb4df55\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:1:fused-proclitic-flow","source_type":"word_analysis","support_id":"sup_49b69aded7d23cccddfa","text":"{\"blocking_evidence\":null,\"headline\":\"attached onset makes continuation audible\",\"reader_payoff\":\"The reader notices that the connector is not visually or audibly detached from the action; it enters the final verb as a linked opening.\",\"reason\":\"The written proclitic and the coordinated clause structure both support the sense of a carried-forward action.\",\"representative_source_ids\":[\"QF-c1f60a11\",\"QP-65407155\",\"QT-cf1b8666\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:2:barrier-withholding-image","source_type":"word_analysis","support_id":"sup_52756ee6e0537b6e0cbf","text":"{\"blocking_evidence\":null,\"headline\":\"withholding becomes barrier-making against aid\",\"reader_payoff\":\"The reader notices that the action is not mere non-generosity; the verb pictures aid being made inaccessible by the withholders.\",\"reason\":\"V4 accepts withholding and barring-access branches for {{ar:م ن ع}} ({{tr:m-n-ʿ}}); the protective or fortifying branch is retained only as irony because the local object relation selects withholding basic aid.\",\"representative_source_ids\":[\"QS-65f155e7\",\"QS-c0270ab0\",\"QS-c58b2d0e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:3:surah-closing-seal","source_type":"word_analysis","support_id":"sup_584447b6725a844718c8","text":"{\"blocking_evidence\":null,\"headline\":\"final noun bears the closing load\",\"reader_payoff\":\"The reader notices that the surah closes not on a general accusation but on the marked aid word that names the denied object.\",\"reason\":\"{{ar:ٱلْمَاعُونَ}} ({{tr:al-māʿūna}}) is the final word of the ayah and surah, and the exact lexeme is marked by the CRITICAL rows as the surah-naming close.\",\"representative_source_ids\":[\"QT-5b7d2ac4\",\"QT-b8a3a710\",\"QH-5d88433b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:2:display-to-obstruction-pivot","source_type":"word_analysis","support_id":"sup_607c9e93807813e8914e","text":"{\"blocking_evidence\":null,\"headline\":\"boundary shifts from public display to direct refusal\",\"reader_payoff\":\"The reader notices the movement from visible performance in 107:6 to the smaller but sharper act of blocking everyday aid in 107:7.\",\"reason\":\"The final predicate continues the prior plural characterization, and the Form I verb contrasts with the preceding display predicate as a plain act of refusal.\",\"representative_source_ids\":[\"QT-1b442541\",\"QB-0242ba7d\",\"QB-d346dc55\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:3:help-root-social-inversion","source_type":"word_analysis","support_id":"sup_618522178f6a78696a31","text":"{\"blocking_evidence\":null,\"headline\":\"help-family meaning is inverted by withholding\",\"reader_payoff\":\"The reader notices the irony that a help-root noun is placed under a withholding verb, turning cooperation into blocked help.\",\"reason\":\"The local syntax places the help-root noun as the object of withholding, while the accepted V4 branch centers on assistance and backing.\",\"representative_source_ids\":[\"QS-8c934916\",\"QI-3c0a9cf5\",\"QI-dd342423\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:3:definite-aid-category","source_type":"word_analysis","support_id":"sup_61b2780b880100e01bca","text":"{\"blocking_evidence\":null,\"headline\":\"definite singular gathers aid into one known class\",\"reader_payoff\":\"The reader notices that the verse condemns withholding the recognized category of basic aid as such, not only refusing one unspecified item.\",\"reason\":\"QAC marks the noun as definite and accusative, and the CRITICAL rows coherently read the article and singular form as gathering the aid field into one category.\",\"representative_source_ids\":[\"QG-1fa70e52\",\"QG-a5d1168d\",\"QF-41fcf114\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"107:7:2:2","source_type":"qac_morpheme","support_id":"sup_625a10197e525b759d66","text":"{\"lemma_ar\":\"مَاعُون\",\"morph_features\":\"STEM|POS:N|LEM:maAEuwn|ROOT:mEn|M|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"107:7:2:2\",\"qac_word_ref\":\"107:7:2\",\"root_ar\":\"م ع ن\",\"surface_ar\":\"مَاعُونَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:2:preventer-character-profile","source_type":"word_analysis","support_id":"sup_8b1b8831191a5714a59b","text":"{\"blocking_evidence\":null,\"headline\":\"finite verb participates in a preventer character field\",\"reader_payoff\":\"The reader notices that the finite action is locally verbal, yet it resonates with a wider Quranic character profile of habitual preventing.\",\"reason\":\"The local surface remains a Form I imperfect verb, so intensive preventer forms inform character pressure without replacing the grammar of {{ar:يَمْنَعُونَ}} ({{tr:yamnaʿūna}}).\",\"representative_source_ids\":[\"QS-c58c48ca\",\"MS-a1308540\",\"QI-4f2bab64\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:3:social-denial-return","source_type":"word_analysis","support_id":"sup_9bb9c7f9653c88593999","text":"{\"blocking_evidence\":null,\"headline\":\"final object returns the surah's social-denial motif\",\"reader_payoff\":\"The reader notices that the final blocked aid restates the surah's earlier social denial in a smaller everyday form.\",\"reason\":\"The final noun is both the direct object of withholding and the surah-closing aid term, so it links the last accusation back to the earlier social field without requiring lexical repetition.\",\"representative_source_ids\":[\"QE-dfcd483e\",\"QB-f0eb7755\",\"QY-b4b68cb5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:3","source_type":"word_analysis","support_id":"sup_a092e25661615026fdb6","text":"{\"gloss_range\":\"the basic aid, useful assistance, lendable utility, or small due help withheld as the direct object\",\"prose\":\"{{ar:ٱلْمَاعُونَ}} ({{tr:al-māʿūna}}) is the named thing withheld and the final word of the surah. Its definiteness turns the object into a known category of basic help, not one isolated favor. Its range can include concrete lendable utilities such as a pot, bucket, or tool, small kindnesses, useful assistance, flowing-resource pressure, and aid treated as due; the local verb selects the shared core of benefit that should be available to others. Because the noun is singular and object-like, the accusation closes on a usable means of help rather than on an abstract virtue, so the thing withheld already carries beneficiary pressure inside it. Its final position seals the discourse on the denied aid itself. The similar sound of the aid noun and the withholding verb creates a sense-shift, while the long-u and final-n cadence answers the prior ayah ending, tying the final social refusal to the previous display.\",\"root_display\":\"{{ar:ع و ن}} ({{tr:ʿ-w-n}})\",\"root_gloss_range\":\"helping and backing is the locally relevant root branch; broader homonymous or unrelated branches in the dictionary do not control this noun\",\"surface_display\":\"{{ar:ٱلْمَاعُونَ}} ({{tr:al-māʿūna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:2:sound-bound-to-object","source_type":"word_analysis","support_id":"sup_a58875d7ff7e972d3ade","text":"{\"blocking_evidence\":null,\"headline\":\"verb sound collides with the aid noun\",\"reader_payoff\":\"The reader notices that the withholding verb and the aid noun are acoustically coupled, making the act sound inseparable from what it blocks.\",\"reason\":\"The adjacent words share nasal, long-vowel, and guttural texture while standing in a forced verb-object relation.\",\"representative_source_ids\":[\"QE-4b1c73e5\",\"QE-65bf2eb8\",\"QY-f35a3d29\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:1","source_type":"word_analysis","support_id":"sup_a9a8881493d0d377836f","text":"{\"gloss_range\":\"coordinating conjunction that carries the final verbal clause forward from the preceding accusation chain, with a possible coda-like rhetorical force\",\"prose\":\"{{ar:وَ}} ({{tr:wa}}) makes the last ayah begin as continuation before the withholding verb even appears. It links {{ar:يَمْنَعُونَ ٱلْمَاعُونَ}} ({{tr:yamnaʿūna al-māʿūna}}) to the preceding portrait, so the refusal of aid is not an isolated afterthought but another predicate in the same indictment. The live attachment range matters: the final clause can be heard as a tight continuation of the preceding predicate or as the closing predicate of the broader characterization chain. At the same time, because this is the surah's final ayah, the connector can also feel like a closing coda: the chain continues, then lands on the concrete object withheld. Its written attachment to {{ar:يَمْنَعُونَ}} ({{tr:yamnaʿūna}}) lets the syntax and recited flow move in one breath from the prior charge into the final one.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:وَ}} ({{tr:wa}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:2","source_type":"word_analysis","support_id":"sup_b27f0c5ba7290385ddcc","text":"{\"gloss_range\":\"they withhold, prevent, or block access; locally an active plural imperfect governing the basic aid as its direct object\",\"prose\":\"{{ar:يَمْنَعُونَ}} ({{tr:yamnaʿūna}}) names active, ongoing withholding. The imperfect plural form keeps the same group from 107:4-6 in motion, so the final charge is a practiced conduct rather than a single refusal. It remains a finite verb, but the wider preventer-character field gives that repeated action trait-like pressure without turning it into an adjective. The verb takes {{ar:ٱلْمَاعُونَ}} ({{tr:al-māʿūna}}) as its explicit object while leaving the denied recipient unnamed; the clause fixes what is blocked and lets the harmed party remain open to anyone who needed that aid. The {{ar:م ن ع}} ({{tr:m-n-ʿ}}) field makes the act more than neglect: they make basic help inaccessible, almost fortifying it against circulation and guarding themselves against giving. After the preceding display predicate, the bare Form I verb shifts from public display to direct obstruction. Together with the opening connector and object, it gives the closing verdict no padding. Its repeated m/n texture, long-u cadence, and guttural pressure are tied to {{ar:ٱلْمَاعُونَ}} ({{tr:al-māʿūna}}), so the act and the aid it negates are heard together.\",\"root_display\":\"{{ar:م ن ع}} ({{tr:m-n-ʿ}})\",\"root_gloss_range\":\"root field includes withholding, barring access, protective inaccessibility, and intensive preventer traits; the local clause selects active withholding of aid while allowing barrier imagery and character pressure\",\"surface_display\":\"{{ar:يَمْنَعُونَ}} ({{tr:yamnaʿūna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:2:ongoing-active-plural","source_type":"word_analysis","support_id":"sup_b33afc3c0ab1e1c7adbe","text":"{\"blocking_evidence\":null,\"headline\":\"imperfect plural makes withholding habitual and agentive\",\"reader_payoff\":\"The reader notices that the verb portrays an ongoing practice by active agents, not a completed incident or passive absence of help.\",\"reason\":\"QAC marks the verb as active imperfect third masculine plural, and attachment evidence identifies the implicit plural subject as continuing the prior discourse group.\",\"representative_source_ids\":[\"QG-19be4c9e\",\"QG-f57c301b\",\"QF-8c3c24aa\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:1:accusation-chain-continuation","source_type":"word_analysis","support_id":"sup_d721f7eaad2f02278dc2","text":"{\"blocking_evidence\":null,\"headline\":\"connector keeps the final clause in the accusation chain\",\"reader_payoff\":\"The reader notices that the final refusal of aid continues the same behavioral profile rather than standing as a detached closing note.\",\"reason\":\"QAC identifies {{ar:وَ}} ({{tr:wa}}) as coordination joining this clause to the preceding accusations, and attachment evidence treats the final span as a coordinated verbal clause.\",\"representative_source_ids\":[\"QG-319b877b\",\"QT-5a4c1218\",\"QB-699c078a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:3:direct-object-visible","source_type":"word_analysis","support_id":"sup_e86791c75cc04393dcba","text":"{\"blocking_evidence\":null,\"headline\":\"object slot fixes what is blocked\",\"reader_payoff\":\"The reader notices that the clause does not end with vague stinginess; it names the precise blocked object while leaving the denied recipient open.\",\"reason\":\"Attachment evidence forces {{ar:ٱلْمَاعُونَ}} ({{tr:al-māʿūna}}) as the accusative direct object of {{ar:يَمْنَعُونَ}} ({{tr:yamnaʿūna}}).\",\"representative_source_ids\":[\"QG-3e28e35e\",\"QG-935e0777\",\"QT-7f43dda1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:7:1:coda-like-resumption","source_type":"word_analysis","support_id":"sup_edb54af48034149d5209","text":"{\"blocking_evidence\":null,\"headline\":\"final connector can feel like a closing coda\",\"reader_payoff\":\"The reader notices that the same connector can carry closing force: the last accusation is coordinated, yet it also arrives as the surah's terminal social coda.\",\"reason\":\"The coda reading is retained as rhetorical force, but narrowed because the local grammar strongly licenses coordination rather than a fully separate new topic.\",\"representative_source_ids\":[\"QG-3be62a33\",\"MG-9b71882a\",\"QT-bb05a39a\"],\"status\":\"narrowed\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"وَيَمْنَعُونَ ٱلْمَاعُونَ","ayah_ref":"107:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001064/B001","root_001448/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_001448","role":"A hand held back from giving supplies the action of stopping an outward transfer.","root":"م ن ع","source_ref":"107:7","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001064","role":"Helping and backing supply the withheld object's function as practical support.","root":"م ع ن","source_ref":"107:7","source_word_indices":["2"]}],"changed_reading":{"after":"They actively stop usable help from crossing from their control into another's use.","before":"They do not give the ma'un."},"confidence":"strong","focus_anchor":"Focus word 1, rooted in م ن ع, governs focus word 2, rooted in م ع ن.","mechanism":"An agent who could let assistance pass instead arrests its transfer at the point of giving.","model_id":"baseline_blocked_transfer"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_blocked_transfer","source_type":"hft","support_id":"sup_f01fe84a10b06f030164","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَيَمْنَعُونَ ٱلْمَاعُونَ","ayah_ref":"107:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001064/B001","root_001448/B002","root_001448/B003"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_001448","role":"The interposed barrier turns refusal into control of another person's access.","root":"م ن ع","source_ref":"107:7","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001448","role":"Protected inaccessibility supplies the enclosed reserve that the gatekeeper keeps beyond reach.","root":"م ن ع","source_ref":"107:7","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001064","role":"Assistance remains the thing enclosed, so the spatial model stays anchored in the focus object.","root":"م ع ن","source_ref":"107:7","source_word_indices":["2"]}],"changed_reading":{"after":"They act as gatekeepers, placing accessible help behind a barrier of control.","before":"They retain a small benefit."},"confidence":"strong","focus_anchor":"The transitive withholding at focus word 1 is directed at assistance named by focus word 2.","mechanism":"Withholding can operate spatially and institutionally: the holders interpose themselves between a seeker and available support, making aid inaccessible without necessarily destroying it.","model_id":"baseline_gatekept_access"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_gatekept_access","source_type":"hft","support_id":"sup_6d79827585e756defcb3","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَيَمْنَعُونَ ٱلْمَاعُونَ","ayah_ref":"107:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001064/B001","root_001448/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001448","role":"Reciprocal resistance over an object supplies the adversarial handling of the resource.","root":"م ن ع","source_ref":"107:7","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001064","role":"Mutual help supplies the cooperative relation that is being converted into contention.","root":"م ع ن","source_ref":"107:7","source_word_indices":["2"]}],"changed_reading":{"after":"They turn a potential relation of mutual aid into a struggle over who controls the useful thing.","before":"They refuse an isolated request for help."},"confidence":"medium","focus_anchor":"The object at focus word 2 activates mutual assistance while the verb at word 1 can activate contention over a thing.","mechanism":"A resource whose proper logic is cooperation is recoded as an object of resistance and possession; mutuality becomes a contest.","model_id":"baseline_contested_mutuality"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_contested_mutuality","source_type":"hft","support_id":"sup_dcb50e4cfd223759194e","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَيَمْنَعُونَ ٱلْمَاعُونَ","ayah_ref":"107:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001064/B001","root_001448/B003","root_001448/B007"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_001448","role":"Protective strength supplies the possibility that inaccessibility guards rather than merely hoards.","root":"م ن ع","source_ref":"107:7","source_word_indices":["1"]},{"branch_id":"B007","mapped_root_id":"root_001448","role":"Resilience through a hard year supplies a scarcity-management motive for temporary restraint.","root":"م ن ع","source_ref":"107:7","source_word_indices":["1"]},{"branch_id":"B001","mapped_root_id":"root_001064","role":"Assistance supplies the reserve's proposed communal purpose.","root":"م ع ن","source_ref":"107:7","source_word_indices":["2"]}],"changed_reading":{"after":"In focus-only isolation, a minority reading can hear guarded help preserved against a lean period.","before":"Every withholding here is necessarily miserly."},"confidence":"exploratory","focus_anchor":"Focus word 1 can describe protective inaccessibility and resistance to scarcity, while word 2 remains assistance.","mechanism":"Read without context, withholding could preserve an aid-stock against depletion: a protective enclosure rather than selfish non-giving.","model_id":"baseline_protective_reserve"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:baseline_protective_reserve","source_type":"hft","support_id":"sup_56bae57de5724874af19","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"وَيَمْنَعُونَ ٱلْمَاعُونَ","ayah_ref":"107:7"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_001064/B003","root_001448/B006"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_001448","role":"Mutual resistance over an object supplies the contested exchange.","root":"م ن ع","source_ref":"107:7","source_word_indices":["1"]},{"branch_id":"B003","mapped_root_id":"root_001064","role":"Seasoned, recurring conflict supplies the temporal pattern into which repeated failures of mutual aid can harden.","root":"م ع ن","source_ref":"107:7","source_word_indices":["2"]}],"changed_reading":{"after":"Repeated contest over useful support can harden the helping relation into a seasoned social war.","before":"A single small refusal interrupts cooperation once."},"confidence":"exploratory","containment":"This is surprising because the repeated-war branch is formally distant from the focus noun's ordinary helping activation. It remains anchored entirely in the two focus roots: contention acts on a term whose mapped inventory also carries seasoned conflict. Downstream prose should preserve it as an adversarial exchange model, not identify ma'un with war.","focus_anchor":"Both activators occur in the focus ayah: resistance over a thing at word 1 and a repeated-conflict branch under the mapped inventory of word 2.","outlier_id":"outlier_cooperation_becomes_repeated_war"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:outlier_cooperation_becomes_repeated_war","source_type":"hft","support_id":"sup_16c5a1546ecc239a9f6c","trust":"legacy_unbound"}]}
</lane_packet_json>
