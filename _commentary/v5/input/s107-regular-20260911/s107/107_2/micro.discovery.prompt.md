# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **107:2**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s107-regular-20260911/s107/107_2/micro.discovery.json` and modify nothing
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
  "ayah_ref": "107:2",
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
{"analysis_context":{"analysis_id":"s107-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"107:2","host_surah":107,"lane_context_refs":[],"ordered_context_refs":["107:0","107:1","107:3","107:4","107:5","107:6","107:7","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Çekirdek fiziksel itmedir; sertlik ve azarlama bazı kullanımları daraltır, doldurma veya seslenme anlamları bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000477/B001","candidate_links":[{"candidate_id":"cand_da7fd8da1d0930765c71","lane":"micro"},{"candidate_id":"cand_ceecaf70ededba2ca837","lane":"micro"},{"candidate_id":"cand_09657578babde7b517f4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"itme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlığı bulunduğu yerden fiziksel güçle itme eylemidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eylem sertlik, kabalık ve azarlama eşliğinde gerçekleşebilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bazı yapılarda savunmasız birini itip azarlamayı veya bir yere zorla sürmeyi anlatır."}}],"root_ar":"د ع ع","root_id":"root_000477","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın bütün kullanımlarında bulunan temel fiziksel yer değiştirme eylemi için uygundur.","boundary_detail":"Çekirdek fiziksel itmedir; sertlik ve azarlama bazı kullanımları daraltır, doldurma veya seslenme anlamları bu dala girmez.","branch_image_ar":"الدَّعّ دفع شديد","concept_gloss":"itme","contextual_glosses":[{"applicability":"Sertliğin veya kaba davranışın açıkça öne çıktığı bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hem itme eylemini hem de eylemin sert gerçekleşmesini korur."},"facet_ids":["F001","F002"],"text":"sertçe itmek","usage_role":"contextual"},{"applicability":"Birinin belirli bir yöne veya yere şiddetle sevk edildiği yapılarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yön belirtmeyen yalın itme kullanımlarını kapsamaz.","preserves":"Zorlayıcı güç ve yönlü hareket özelliklerini korur."},"facet_ids":["F002","F003"],"text":"zorla sürmek","usage_role":"contextual"}],"definition":"Birini ya da bir şeyi itmek; belirli kullanımlarda bunu sertçe, kaba davranarak veya azarlayıcı biçimde yapmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlığı bulunduğu yerden fiziksel güçle itme eylemidir."},{"facet_id":"F002","role":"specialization","statement":"Eylem sertlik, kabalık ve azarlama eşliğinde gerçekleşebilir."},{"facet_id":"F003","role":"associated_use","statement":"Bazı yapılarda savunmasız birini itip azarlamayı veya bir yere zorla sürmeyi anlatır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Temasın sürmesi ve nesnenin çekilmesi anlamını ekler.","collision":"Türkçede çekerek ilerletme eylemiyle karışır.","fit":"displacement","loses":"Tek hamlelik itme ve azarlayıcı sertlik ayrımını kaybeder.","preserves":"Zor kullanılarak yer değiştirme düşüncesini kısmen korur."},"text":"sürükleme"}],"identity_rationale":"Yetkili kaynak ifadesi itme eyleminde birleşir; ancak sertlik, kabalık ve azarlama niteliği bütün aktarımlarda aynı ölçüde kurucu değildir. Bu yüzden dal, sıradan itme çekirdeğini koruyup sert ve kaba gerçekleşmeleri belirgin kullanımlar olarak ayırmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"sert ve kaba itme"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"sertçe itmek"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"yetimi itip azarlamak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ateşe doğru zorla sürmek"}],"lexicalization_note":"Tanım çıplak itme çekirdeğiyle yapıya bağlı sertçe sürme ve azarlama örneklerini ayırır; özel yapılar bütün dalın anlamı sayılmaz.","neighbor_coverage_note":"Sağlanan bütün adaylar değerlendirildi; itmenin güç ve sınır farklarını en açık gösteren iki komşu seçildi, yalnızca aynı olay alanını paylaşan uzak adaylar elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın sınırı itme ve onun kaba ya da azarlayıcı gerçekleşmesidir; komşu dal ise baskı kurma, delme ve güçle içeri sokma gibi daha geniş zorlayıcı işlemleri de içerir.","focus_only":"Bu dal, kaba davranış ve azarlama eşliğindeki itmeye kadar uzanır.","gloss":"sert itme ile zorlayıcı bastırma","neighbor_only":"Komşu dal zorlama, delme ve bir şeyi başka bir şeye güçle sokma kapsamını da taşır.","neighbor_ref":"root_000474/B001","relation_type":"near_synonym","shared_zone":"İki dal da güçlü ve sert bir fiziksel itme eylemini kapsar."},{"boundary_match":"partial","distinction":"Odak dal eylemin sert ve kaba biçimine yoğunlaşır; komşu dalın ayırıcı yönü bir şeyi uzak tutma, engelleme veya karşı koymadır.","focus_only":"Odak dal sertlik ve kaba azarlama niteliğini belirginleştirebilir.","gloss":"sert itme ile itip engelleme","neighbor_only":"Komşu dal itmenin yanında çarpma, engelleme ve kendini savunma yönlerini kapsar.","neighbor_ref":"root_000622/B001","relation_type":"near_neighbor","shared_zone":"Her iki dalda da bir varlığı güç uygulayarak geri veya yana itme bulunur."}],"source_phrase_ar":"الدَّعّ الدفع (maqayis;tahdhib)؛ دَعَعته أدَعُّه دَعًّا أي دفعته (sihah)؛ دفع في جفوة (ayn)؛ الدفع الشديد (mufradat)","source_summary":"Aktarımlar itme çekirdeğinde birleşir; bir bölümü eylemin sert, kaba ve azarlayıcı niteliğini ayrıca öne çıkarır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الدفع العنيف والجفوة والانتهار والدفع إلى الشيء أو عن الحق","what_is_not_ar":"ليس تحريك المكيال ولا النداء الصوتي ولا عدو الالتواء"},"support_links":["sup_16ff0b02a06e911120e2","sup_1aa923127a6d0edd8b45","sup_75c1600008d8b8b83ff4"]},{"boundary":"Ayırıcı özellik yalnızca doluluk değil, kabı hareket ettirerek kapasitesini kullanma veya içeriği sıkıştırma sürecidir.","branch_kind":"mixed_non_bare","branch_ref":"root_000477/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"sallayarak doldurma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kabın hareket ettirilmesi, içeriğin yerleşmesini ve kullanılabilir hacmin dolmasını sağlar."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İşlemden doğan tam doluluk veya sıkışık doluluk sonucu ayrıca adlandırılır."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Büyük bir çanağın ya da bir vadinin tamamen dolması sonuç kullanımına örnektir."}}],"root_ar":"د ع ع","root_id":"root_000477","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kabın hareketiyle içeriğin yerleşip kapasitenin dolduğu temel işlem için uygundur.","boundary_detail":"Ayırıcı özellik yalnızca doluluk değil, kabı hareket ettirerek kapasitesini kullanma veya içeriği sıkıştırma sürecidir.","branch_image_ar":"الدعدعة تحريك لامتلاء","concept_gloss":"sallayarak doldurma","contextual_glosses":[{"applicability":"Hareket biçiminden çok ortaya çıkan tam doluluğun anlatıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İçeriği yerleştiren sallama veya hareket ettirme işlemini belirtmez.","preserves":"Kabın tam dolu hale gelmesi sonucunu korur."},"facet_ids":["F002","F003"],"text":"ağzına kadar doldurmak","usage_role":"contextual"}],"definition":"Bir kabı hareket ettirerek içindekilerin yerleşmesini ve kabın dolmasını ya da sıkışık hale gelmesini sağlamak; uzantı olarak bir şeyi bütünüyle doldurmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kabın hareket ettirilmesi, içeriğin yerleşmesini ve kullanılabilir hacmin dolmasını sağlar."},{"facet_id":"F002","role":"extension","statement":"İşlemden doğan tam doluluk veya sıkışık doluluk sonucu ayrıca adlandırılır."},{"facet_id":"F003","role":"example","statement":"Büyük bir çanağın ya da bir vadinin tamamen dolması sonuç kullanımına örnektir."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İçeriğin hareketle yerleştirilmesi ve sıkıştırılması özelliğini kaybeder.","preserves":"Kabın veya yerin dolu hale gelmesi sonucunu korur."},"text":"doldurma"}],"identity_rationale":"Yetkili kaynak ifadesi, bir ölçek kabını veya başka bir taşıyıcıyı hareket ettirerek içindekini yerleştirme ve kabı dolu ya da sıkışık duruma getirme sürecini açıkça destekler. Sonuç bildiren doldurma kullanımları aynı işlemin doğal uzantısıdır.","lexical_glosses":[{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"kabı sallayarak doldurma"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"bir şeyi doldurmak veya hareket ettirerek sıkıştırmak"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ağzına kadar dolu büyük çanak"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"selin vadiyi doldurması"}],"lexicalization_note":"Çıplak doldurma sonucu ile kap, büyük çanak ve vadiye bağlı gerçekleşmeler ayrı tutulur; yapıya bağlı örnekler genel bir kök anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı; işlem biçimini genel doluluktan ve dolu kabın durumundan ayıran iki komşu yayımlandı, yalnızca aynı doluluk alanındaki tekrarlar dışarıda bırakıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalda kabın hareket ettirilmesi kurucu bir süreçtir; komşu dalda ise doluluk sonucu yeterlidir ve bu işlem biçimi zorunlu değildir.","focus_only":"Odak dal kabı hareket ettirerek içeriğin yerleşmesini ve sıkışmasını içerir.","gloss":"sallayarak doldurma ile genel doldurma","neighbor_only":"Komşu dal, özel bir yerleştirme hareketi gerektirmeden genel kap doldurmayı anlatır.","neighbor_ref":"root_000905/B003","relation_type":"near_synonym","shared_zone":"İki dalın ortak sonucu bir kabın kullanılabilir hacminin dolmasıdır."},{"boundary_match":"partial","distinction":"Odak dal süreçten sonuca gider; komşu dal ise işlemi değil, doluluğun ağırlığıyla sabit duran kabın durumunu öne çıkarır.","focus_only":"Odak dal doluluğu meydana getiren hareketli işlemi de adlandırır.","gloss":"doldurma işlemi ile dolu çanak","neighbor_only":"Komşu dal ağır ve sabit duran dolu büyük çanağın durumunu betimler.","neighbor_ref":"root_000590/B003","relation_type":"near_neighbor","shared_zone":"Her iki dal büyük bir kabın tam dolu oluşuyla ilişkilidir."}],"source_phrase_ar":"الدعدعة تحريك المكيال ليستوعب الشيء (maqayis)؛ دعدعت الشيء ملأته وجفنة مدعدعة (sihah)؛ دعدع مكيالا أو جوالقا حتى يكتنز (tahdhib)","source_summary":"Aktarımlar kabı hareket ettirerek içeriği yerleştirme ile doluluk sonucu arasında birleşir; örnekler ölçek kabından çanak ve vadiye uzanır.","sources":["MQ","SI","TA"],"what_is_ar":"تحريك المكيال أو الوعاء أو الجوالق حتى يستوعب الشيء أو يكتنز وامتلاء الجفنة أو الوادي","what_is_not_ar":"ليس الدفع العنيف ولا النداء ولا العدو البطيء"},"support_links":[]},{"boundary":"Bu dal sıradan yüksek ses değil, çobanın özellikle keçi veya küçükbaş sürüyü çağırmak ya da yönlendirmek için kullandığı sestir.","branch_kind":"mixed_non_bare","branch_ref":"root_000477/B003","candidate_links":[{"candidate_id":"cand_b6e61ee9d293635a85e0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"hayvanı seslenerek yönlendirme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sesleniş, sürüyü çağırma veya davranışını yönlendirme amacı taşır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kullanım özellikle keçilere yönelir, ancak daha geniş küçükbaş sürü aktarımı da vardır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Aynı geleneksel ses hem çağırma hem de azarlayıp sevk etme işlevi görebilir."}}],"root_ar":"د ع ع","root_id":"root_000477","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Çobanın küçükbaş hayvanı çağırma veya azarlama amacıyla ses kullandığı bütün dal için uygundur.","boundary_detail":"Bu dal sıradan yüksek ses değil, çobanın özellikle keçi veya küçükbaş sürüyü çağırmak ya da yönlendirmek için kullandığı sestir.","branch_image_ar":"الدعدعة نداء وزجر","concept_gloss":"hayvanı seslenerek yönlendirme","contextual_glosses":[{"applicability":"Seslenişin özellikle keçileri bir araya getirme amacı taşıdığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Azarlama işlevini ve daha geniş küçükbaş kapsamını dışarıda bırakır.","preserves":"Keçi muhatabını ve çağırma işlevini açık biçimde korur."},"facet_ids":["F001","F002"],"text":"keçileri çağırmak","usage_role":"contextual"},{"applicability":"Çağrının sürüyü durdurma, sevk etme veya davranışını düzeltme işlevinde uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Sürü muhatabını, azarlayıcı tonu ve yönlendirme işlevini korur."},"facet_ids":["F001","F003"],"text":"sürüyü azarlayarak yönlendirmek","usage_role":"contextual"}],"definition":"Çobanın küçükbaş hayvanları, özellikle keçileri, çağırmak veya azarlayarak yönlendirmek için geleneksel bir sesleniş kullanmasıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sesleniş, sürüyü çağırma veya davranışını yönlendirme amacı taşır."},{"facet_id":"F002","role":"specialization","statement":"Kullanım özellikle keçilere yönelir, ancak daha geniş küçükbaş sürü aktarımı da vardır."},{"facet_id":"F003","role":"associated_use","statement":"Aynı geleneksel ses hem çağırma hem de azarlayıp sevk etme işlevi görebilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Herhangi bir amaçla yüksek ses çıkarmayı kapsama alır.","collision":"Genel öfke veya yardım çağrısı anlamlarıyla kolayca karışır.","fit":"displacement","loses":"Çoban, sürü ve geleneksel yönlendirme işlevlerini kaybeder.","preserves":"Duyulabilir ve güçlü bir ses çıkarma özelliğini korur."},"text":"bağırma"}],"identity_rationale":"Yetkili kaynak ifadesi çobanın küçükbaş hayvanlara yönelttiği geleneksel sesi hem çağırma hem de azarlayıp yönlendirme işleviyle verir. Bazı aktarımlar koyunu genel olarak anarken bazıları özellikle keçiyi sınırlar; tanım bu kapsam farkını açık tutmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"küçükbaş hayvanı seslenerek çağırma veya azarlama"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"keçilere seslenip onları yönlendirmek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"çobanın keçileri yönlendirmek için çıkardığı geleneksel çağrı"}],"lexicalization_note":"Seslenme çekirdeği, keçiye yönelen yapı ve geleneksel çağrı biçiminden ayrılır; hayvana bağlı kullanımlar genel ses çıkarma anlamına taşınmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; en yakın genel çoban sesi ile farklı hayvana yönelen paralel ünlem seçildi, salt yüksek ses veya uzak hayvan çağrıları tekrar sayıldı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"İşlevler büyük ölçüde örtüşür; odak dal geleneksel söz kalıbı ve keçi muhatabıyla daralırken komşu dal çoban sesini daha genel çerçevede verir.","focus_only":"Odak dal özellikle keçiye yönelen geleneksel çağrı biçimini belirginleştirir.","gloss":"keçi çağrısı ile genel çoban sesi","neighbor_only":"Komşu dal çobanın koyun veya küçükbaş sürüye yönelttiği sesi daha genel adlandırır.","neighbor_ref":"root_001523/B001","relation_type":"near_synonym","shared_zone":"İki dal da çobanın sürüyü çağırmak ve azarlamak için çıkardığı sesi kapsar."},{"boundary_match":"field_only","distinction":"Ortak alan hayvan sevkidir; muhatap türü ve kullanılan geleneksel ses farklı olduğundan ifadeler birbirinin yerine geçmez.","focus_only":"Odak dal küçükbaş hayvanlara, özellikle keçilere yönelir.","gloss":"keçi çağrısı ile deve ünlemi","neighbor_only":"Komşu dal deveye yöneltilen farklı bir sürücü ünlemini adlandırır.","neighbor_ref":"root_001612/B007","relation_type":"same_field","shared_zone":"Her ikisi de hayvanı sesle yönlendiren geleneksel çoban kullanımlarıdır."}],"source_phrase_ar":"الدعدعة زجر الغنم (maqayis)؛ للمعز خاصة دعدعت بها إذا دعوتها (sihah)؛ يقول الراعي للمعزى داع داع وهو زجر لها (tahdhib)","source_summary":"Aktarımlar çoban sesinin sürüyü çağırma ve azarlayarak yönlendirme işlevinde birleşir; hayvan kapsamı genel küçükbaştan özellikle keçiye kadar değişir.","sources":["MQ","SI","TA"],"what_is_ar":"نداء المعز أو الغنم وزجرها بقول داع داع أو دع دع","what_is_not_ar":"ليس دعاء العاثر ولا الدفع الشديد ولا تحريك المكيال"},"support_links":["sup_409ffd3e1031524f93aa"]},{"boundary":"Anlam tökezleyen muhataba söylenen kalıpla sınırlıdır; genel ayağa kalkma, yardım etme veya teselli etme anlamına genişletilmez.","branch_kind":"non_bare","branch_ref":"root_000477/B004","candidate_links":[{"candidate_id":"cand_09657578babde7b517f4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"tökezleyeni ayağa kalkmaya çağırma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Söz doğrudan tökezleyen kişiye yöneltilir ve yeniden ayağa kalkmasını teşvik eder."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ayağa kalkma buyruğuna toparlanma teşviki eşlik eder."}}],"root_ar":"د ع ع","root_id":"root_000477","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli sözün tökezleyen kişiye yöneltilen teşvik işlevini eksiksiz karşılar.","boundary_detail":"Anlam tökezleyen muhataba söylenen kalıpla sınırlıdır; genel ayağa kalkma, yardım etme veya teselli etme anlamına genişletilmez.","branch_image_ar":"دع دع للعاثر","concept_gloss":"tökezleyeni ayağa kalkmaya çağırma","contextual_glosses":[{"applicability":"Tökezleyene doğrudan seslenilen ve eylem çağrısının öne çıktığı durumda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ayağa kalkma buyruğunu ve toparlanma teşvikini doğal Türkçeyle korur."},"facet_ids":["F001","F002"],"text":"Kalk, toparlan!","usage_role":"contextual"}],"definition":"Tökezleyen birine ayağa kalkmasını ve toparlanmasını söyleyen kalıplaşmış bir sesleniştir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Söz doğrudan tökezleyen kişiye yöneltilir ve yeniden ayağa kalkmasını teşvik eder."},{"facet_id":"F002","role":"associated_use","statement":"Ayağa kalkma buyruğuna toparlanma teşviki eşlik eder."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Hastalık veya yaralanma sonrasında kullanılan genel dileği ekler.","collision":"Türkçedeki hastalık ve kaza sonrası nezaket kalıbıyla karışır.","fit":"displacement","loses":"Ayağa kalkma ve hemen toparlanma çağrısını kaybeder.","preserves":"Muhatabın iyiliğini isteme ve esenlik dileme yönünü korur."},"text":"geçmiş olsun"}],"identity_rationale":"Yetkili kaynak ifadesi, tökezleyen kişiye yöneltilen ikili bir sözün ayağa kalkma ve toparlanma işlevini açıkça verir. Bu, genel bir itme ya da genel bir teselli değil, belirli durumda kullanılan sözlü bir teşviktir.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"tökezleyene söylenen 'kalk, toparlan' sözü"}],"lexicalization_note":"Dal yalnızca tökezleyen kişiye yöneltilen özel sözlü kalıbı açıklar; bundan çıplak bir kök anlamı çıkarılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı tökezleme durumunda kullanılan esenlik sözü tek yakın karşılaştırma olarak seçildi, yükselme ve iyileşme temalı uzak adaylar yayımlanmadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın kurucu yönü ayağa kalkma ve toparlanma çağrısıdır; komşu dal daha geniş bir durumda koruyucu esenlik dileği olarak kullanılabilir.","focus_only":"Odak dal tökezleyene ayağa kalkıp toparlanmasını söyleyen doğrudan bir teşviktir.","gloss":"ayağa kalkma teşviki ile esenlik dileği","neighbor_only":"Komşu dal tökezleme yanında başka bir sıkıntı veya felaket durumunda da esenlik dileği olabilir.","neighbor_ref":"root_000367/B004","relation_type":"near_synonym","shared_zone":"Her iki söz de tökezleyen kişiye yönelip onun iyi olmasını amaçlayabilir."}],"source_phrase_ar":"قولك للعاثر دع دع (maqayis)؛ أن تقول للعاثر دع دع أي قم فانتعش (sihah;tahdhib)؛ أصله أن يقال للعاثر دع دع (mufradat)","source_summary":"Aktarımlar sözün tökezleyene yönelmesinde ve ona ayağa kalkıp toparlanmasını söylemesinde birleşir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"قول دع دع للعاثر بمعنى قم وانتعش أو رفعك الله","what_is_not_ar":"ليس زجر الغنم ولا ملء المكيال ولا مطلق الدفع إلا من جهة الأصل عند بعض المصادر"},"support_links":["sup_75c1600008d8b8b83ff4"]},{"boundary":"Yavaşlık ve kıvrımlı ilerleyiş birlikte kurucudur; sıradan koşu, ağır yürüyüş veya yorgunluktan sendeleme bu dala girmez.","branch_kind":"bare","branch_ref":"root_000477/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"kıvrılarak yavaş koşma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hareket yürüyüş değil koşudur ve ilerleme görece yavaştır."}},{"facet_id":"F002","role":"core","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Koşunun yolu ya da beden hareketi kıvrımlı ve dolambaçlıdır."}}],"root_ar":"د ع ع","root_id":"root_000477","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem hareket türünü hem hızını hem de izlediği biçimi birlikte karşılar.","boundary_detail":"Yavaşlık ve kıvrımlı ilerleyiş birlikte kurucudur; sıradan koşu, ağır yürüyüş veya yorgunluktan sendeleme bu dala girmez.","branch_image_ar":"الدعدعة عدو ملتف بطيء","concept_gloss":"kıvrılarak yavaş koşma","contextual_glosses":[{"applicability":"İzlenen yolun veya beden hareketinin kıvrımlı oluşu bağlamda zaten belirginken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Koşunun görece yavaş temposunu açıkça belirtmez.","preserves":"Koşma eylemini ve düz olmayan ilerleyişi korur."},"facet_ids":["F002"],"text":"dolambaçlı biçimde koşmak","usage_role":"contextual"}],"definition":"Düz bir çizgide ilerlemeyip kıvrılarak veya dolambaçlı biçimde, görece yavaş koşmaktır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hareket yürüyüş değil koşudur ve ilerleme görece yavaştır."},{"facet_id":"F002","role":"core","statement":"Koşunun yolu ya da beden hareketi kıvrımlı ve dolambaçlıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Koşudan farklı olarak yürüme hareketini ekler.","collision":"Yavaş ve ölçülü yürüme anlamıyla karışır.","fit":"displacement","loses":"Koşma ve kıvrımlı hareket özelliklerini bütünüyle kaybeder.","preserves":"Yavaş ilerleme özelliğini kısmen korur."},"text":"ağır yürüyüş"}],"identity_rationale":"Yetkili kaynak ifadesi koşuyu iki eşzamanlı özellikle sınırlar: hareket doğrusal değil kıvrımlı veya dolambaçlıdır ve hızlı değil yavaştır. Dalın ayırıcı kimliği yalnızca koşma değil, bu özel hareket biçimidir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"kıvrıla kıvrıla yavaş koşma"}],"lexicalization_note":"Tanım çıplak dalın kıvrımlı ve yavaş koşma anlamıyla sınırlıdır; komşu hareket biçimleri veya özel yapılar eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; hız eksenindeki karşıt koşu ile yavaş yürüyüşe benzeyen komşu seçildi, yorgunluktan düşme ve sıradan hızlanma adayları sınırı daha az açıklıyordu.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Ortak eksen koşunun hızı ve seyir biçimidir; odak dal yavaş ve dolambaçlı, komşu dal hızlı ve güçlü ilerleyişi öne çıkarır.","focus_only":"Odak dal yavaş ve kıvrımlı koşmayı bildirir.","gloss":"yavaş kıvrımlı koşu ile hızlı koşu","neighbor_only":"Komşu dal çok hızlı, güçlü ve doğrultusunda süren koşuyu bildirir.","neighbor_ref":"root_000598/B007","relation_type":"polarity_pair","shared_zone":"İki dal da koşma biçimini hız ve ilerleyiş özellikleriyle tanımlar."},{"boundary_match":"partial","distinction":"Hız benzerliği yanıltıcıdır: odak dal yine koşudur ve kıvrımlıdır; komşu dal ise koşma içermeyen temkinli yürüyüştür.","focus_only":"Odak dal kıvrımlı bir koşma biçimidir.","gloss":"yavaş koşu ile ağır yürüyüş","neighbor_only":"Komşu dal ağır, temkinli ve ölçülü yürümeyi anlatır.","neighbor_ref":"root_001615/B002","relation_type":"near_neighbor","shared_zone":"Her iki dal yavaş ilerleme izlenimi verir."}],"source_phrase_ar":"الدعدعة عدو في التواء (maqayis)؛ عدا عدوا فيه بطء والتواء (sihah)؛ عدو في التواء وبطء (tahdhib)","source_summary":"Aktarımlar, koşunun kıvrımlı ilerleyişini ve yavaş temposunu birlikte kurucu özellikler olarak verir.","sources":["MQ","SI","TA"],"what_is_ar":"العدو أو السعي الذي فيه التواء وبطء","what_is_not_ar":"ليس الدفع ولا ملء الوعاء ولا النداء الصوتي"},"support_links":[]},{"boundary":"Dal kısa boylu erkek kişiyi adlandırır; biçimin kökeni ve bağımsızlığı belirsiz olduğu için genel kısalık anlamına genişletilmez.","branch_kind":"unresolved","branch_ref":"root_000477/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"kısa boylu adam","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Adlandırmanın gönderimi kısa boylu erkek kişidir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Biçimin başka bir kısa-boy adlandırmasından ses değişimiyle gelmiş olması mümkündür."}}],"root_ar":"د ع ع","root_id":"root_000477","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirsiz köken kaydını anlamın içine katmadan aktarılan kişi niteliğini karşılar.","boundary_detail":"Dal kısa boylu erkek kişiyi adlandırır; biçimin kökeni ve bağımsızlığı belirsiz olduğu için genel kısalık anlamına genişletilmez.","branch_image_ar":"الدعداع قصر الرجل","concept_gloss":"kısa boylu adam","contextual_glosses":[{"applicability":"Nadir adlandırmanın açıklayıcı ve doğal Türkçe karşılığı gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kişinin cinsiyetini ve boyca kısa oluşunu doğrudan korur."},"facet_ids":["F001"],"text":"kısa boylu erkek","usage_role":"explanatory"}],"definition":"Kısa boylu bir erkeği niteleyen, biçimsel doğruluğu ve başka bir sözcükten ses değişimiyle gelip gelmediği belirsiz bir adlandırmadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Adlandırmanın gönderimi kısa boylu erkek kişidir."},{"facet_id":"F002","role":"source_variant","statement":"Biçimin başka bir kısa-boy adlandırmasından ses değişimiyle gelmiş olması mümkündür."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":"İnsan dışındaki bitki ve nesnelere, ayrıca tıknazlığa uzanan kapsam ekler.","collision":"Türkçede kısa boy yanında gövdece sıkı veya gelişmemiş olma çağrışımı taşır.","fit":"broadening","loses":null,"preserves":"Boyca kısa olma niteliğini korur."},"text":"bodur"}],"identity_rationale":"Yetkili kaynak ifadesi sözcüğü kısa boylu adam için açıklar, fakat biçimin doğruluğunu koşullu verir ve başka bir biçimden ses değişimiyle gelmiş olabileceğini belirtir. Anlam korunabilir, ancak bağımsız ve üretken bir kök anlamı olduğu varsayılamaz.","lexicalization_note":"Kabul edilmiş sözcük birimi bulunmadığından dalın çıplak veya yapıya bağlı olduğu varsayılmaz; tanım yalnızca aktarılan kişi niteliğini kaydeder.","neighbor_coverage_note":"Bütün adaylar incelendi; genel kısalık ile kısa ve toplu beden adları sınırı en iyi açıkladı, uzunluk, incelik ve başka beden özellikleri yalnızca aynı betimleme alanındaydı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın gönderimi erkek kişiyle ve belirli bir adlandırmayla sınırlıdır; komşu dal ise kısalık niteliğini daha geniş varlık sınıflarında anlatır.","focus_only":"Odak dal kısa boylu erkek için özel ve kökeni belirsiz bir adlandırmadır.","gloss":"özel kısa-adam adı ile genel kısalık","neighbor_only":"Komşu dal kişi ve cisimlerde kısalığı genel bir nitelik olarak kapsar.","neighbor_ref":"root_001231/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir insanın boyca kısa oluşunu ifade edebilir."},{"boundary_match":"partial","distinction":"Odak dal için kısa boy yeterlidir; komşu dalın sınırında toplu beden yapısı ve boyun kesilmiş gibi oluşuna ilişkin ek bir tasarım vardır.","focus_only":"Odak dal yalnızca kısa boylu erkek gönderimini verir.","gloss":"kısa adam ile kısa ve toplu yapı","neighbor_only":"Komşu dal kısa olmanın yanında bedenin toplu ve yaratılışça kısalmış görünmesini içerir.","neighbor_ref":"root_000080/B006","relation_type":"near_synonym","shared_zone":"Her iki adlandırma kısa boylu bir erkeğe uygulanabilir."}],"source_phrase_ar":"دعداع فإن صح فهو من الإبدال من دحداح (maqayis)؛ الدعداع والدحداح الرجل القصير (tahdhib)","source_summary":"Aktarımlar kısa boylu erkek anlamını desteklerken biçimin bağımsızlığı konusunda ihtiyat kaydı taşır.","sources":["MQ","TA"],"what_is_ar":"الرجل القصير المسمى دعداعا","what_is_not_ar":"ليس عدو الدعداع ولا الدعدعة في الوعاء"},"support_links":[]},{"boundary":"Dal hurmaların seyrekliği veya iki hurma arasındaki açıklıkla sınırlıdır; küçük hurma, toplu hurmalık ya da genel ağaçlık anlamına gelmez.","branch_kind":"unresolved","branch_ref":"root_000477/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"iki hurma arasındaki açıklık veya seyrek hurmalar","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Hurma ağaçları bitişik bir topluluk değil, aralıklı ve seyrek durumdadır."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Adlandırma iki hurma ağacı arasında kalan boşluğa da uygulanır."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sözcüğün ilk ünsüzü başka bir sesle aktarılmış bir biçime ait olabilir."}}],"root_ar":"د ع ع","root_id":"root_000477","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın hem aralık hem de aralıklı ağaç topluluğu görünümünü birlikte karşılar.","boundary_detail":"Dal hurmaların seyrekliği veya iki hurma arasındaki açıklıkla sınırlıdır; küçük hurma, toplu hurmalık ya da genel ağaçlık anlamına gelmez.","branch_image_ar":"الدعاع تفرق النخل","concept_gloss":"iki hurma arasındaki açıklık veya seyrek hurmalar","contextual_glosses":[{"applicability":"Adlandırma tek bir aralıktan çok dağınık duran ağaç topluluğunu gösterdiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İki belirli hurma arasındaki açıklık kullanımını dışarıda bırakır.","preserves":"Hurma ağaçlarının aralıklı ve dağınık oluşunu korur."},"facet_ids":["F001"],"text":"seyrek hurma ağaçları","usage_role":"contextual"}],"definition":"Seyrek duran hurma ağaçlarını veya iki hurma ağacı arasında kalan açıklığı anlatan, ilk ünsüzü konusunda aktarım ayrılığı bulunan bir adlandırmadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Hurma ağaçları bitişik bir topluluk değil, aralıklı ve seyrek durumdadır."},{"facet_id":"F002","role":"extension","statement":"Adlandırma iki hurma ağacı arasında kalan boşluğa da uygulanır."},{"facet_id":"F003","role":"source_variant","statement":"Sözcüğün ilk ünsüzü başka bir sesle aktarılmış bir biçime ait olabilir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sık veya düzenli dikilmiş her türlü hurma bahçesini kapsar.","collision":"Toplu ve düzenli hurma bahçesi anlamıyla karışır.","fit":"broadening","loses":"Ağaçların seyrekliği ve iki ağaç arasındaki açıklık özelliklerini belirtmez.","preserves":"Birden çok hurma ağacının bulunduğu alanı ifade eder."},"text":"hurmalık"}],"identity_rationale":"Yetkili kaynak ifadesi iki yakın görünümü birlikte aktarır: iki hurma ağacı arasındaki açıklık ve seyrek duran hurma ağaçları. Ayrıca sözcüğün ilk ünsüzünün başka bir biçimde aktarılmış olabileceği belirtilir; bu nedenle dal hem yerleşim anlamını hem yazım belirsizliğini korumalıdır.","lexicalization_note":"Kabul edilmiş sözcük birimi bulunmadığından çıplaklık varsayılmaz; yalnızca seyrek hurmalar ve aralarındaki açıklık aktarılır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; toplu hurmalarla karşıtlık ve küçük hurmalarla ölçüt farkı seçildi, genel açıklık ve bahçe adayları hurmaya özgü sınırı daha az belirginleştirdi.","neighbor_distinctions":[{"boundary_match":"opposed","distinction":"Ortak düzen ekseninde odak dal aralık ve dağınıklığı, komşu dal ise ağaçların bir araya gelerek topluluk oluşturmasını öne çıkarır.","focus_only":"Odak dal hurmaların seyrek ve birbirinden ayrı durmasını anlatır.","gloss":"seyrek hurmalar ile toplu hurmalar","neighbor_only":"Komşu dal hurmaların bir topluluk veya küme halinde bulunmasını anlatır.","neighbor_ref":"root_000891/B005","relation_type":"polarity_pair","shared_zone":"İki dal da birden çok hurma ağacının mekansal düzenini adlandırır."},{"boundary_match":"field_only","distinction":"Odak dalın ölçütü ağaçlar arasındaki mesafedir; komşu dalın ölçütü ise ağaçların büyüklüğü veya gelişim evresidir.","focus_only":"Odak dal ağaçların birbirine göre seyrek yerleşimini bildirir.","gloss":"seyrek hurmalar ile küçük hurmalar","neighbor_only":"Komşu dal hurmaların yaşça veya gelişimce küçük oluşunu bildirir.","neighbor_ref":"root_000832/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal bir hurma ağacı topluluğunu betimleyebilir."}],"source_phrase_ar":"الدعاع ما بين النخلتين؛ الدعاع النخل المتفرق؛ رواه بعضهم في ذعاع النخل بالذال","source_qualifications":[{"kind":"sole_attestation","summary":"Seyrek hurmalar, aralarındaki açıklık ve olası ses varyantı bu tek tanıklıkta birlikte korunur."}],"source_summary":"Tek aktarım seyrek hurmalar ile iki hurma arasındaki açıklığı aynı adlandırmada birleştirir ve biçim için bir ses varyantı kaydeder.","sources":["TA"],"what_is_ar":"ما بين النخلتين أو النخل المتفرق المسمى دعاعا","what_is_not_ar":"ليس الدعاع عيال الرجل ولا حب الشجرة ولا الذعاع بالذال إذا ثبت"},"support_links":[]},{"boundary":"Dal herhangi bir sulak alanı veya genel yemi değil, yazın su barındıran ve sığırların yediği belirli bir bitkiyi anlatır.","branch_kind":"bare","branch_ref":"root_000477/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"yazın su barındıran, sığırların yediği bitki","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim belirli bir bitki türüdür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitki yazın bünyesinde su barındırmasıyla ayırt edilir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Sığırların bu bitkiyi yemesi onun aktarılan kullanım özelliğidir."}}],"root_ar":"د ع ع","root_id":"root_000477","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Bitkinin mevsimsel nemini ve hayvan yemi oluşunu birlikte belirten eksiksiz açıklayıcı karşılıktır.","boundary_detail":"Dal herhangi bir sulak alanı veya genel yemi değil, yazın su barındıran ve sığırların yediği belirli bir bitkiyi anlatır.","branch_image_ar":"الدعدع نبت مائي","concept_gloss":"yazın su barındıran, sığırların yediği bitki","contextual_glosses":[{"applicability":"Bitkinin yaz mevsimindeki nemli yapısının kısa biçimde açıklanması gerektiğinde kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sığırların bu bitkiyi yediği bilgisini dışarıda bırakır.","preserves":"Bitki oluşunu ve yazın su barındırma özelliğini korur."},"facet_ids":["F001","F002"],"text":"sulu yaz otu","usage_role":"explanatory"}],"definition":"Yaz mevsiminde bünyesinde su barındıran ve sığırlar tarafından yenen bir bitki türüdür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim belirli bir bitki türüdür."},{"facet_id":"F002","role":"specialization","statement":"Bitki yazın bünyesinde su barındırmasıyla ayırt edilir."},{"facet_id":"F003","role":"associated_use","statement":"Sığırların bu bitkiyi yemesi onun aktarılan kullanım özelliğidir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Her türlü sulak ortam bitkisini kapsama alır.","collision":"Bitkinin yetiştiği ortamı, bünyesinde su barındırmasıyla karıştırır.","fit":"broadening","loses":"Yaz mevsimi ve sığırlarca yenme özelliklerini belirtmez.","preserves":"Bitki ile su arasındaki ilişkiyi genel olarak korur."},"text":"sulak alan bitkisi"}],"identity_rationale":"Yetkili kaynak ifadesi bitkiyi üç birlikte bulunan özellikle tanımlar: yazın bünyesinde su barındırması, sığırlar tarafından yenmesi ve bir bitki türü olması. Provisional çerçeve bu sınırlı doğal-tür anlamını doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"yazın su tutan ve sığırların yediği bir bitki"}],"lexicalization_note":"Tanım çıplak bitki adını ve aktarılan ayırıcı özelliklerini korur; başka mera bitkileri veya suyla ilgili kullanımlar eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; nemli mera otu ve farklı hayvanın yediği ot sınırı en iyi gösterdi, genel ıslaklık ve otlatma eylemi adayları bitki kimliğini karşılamadı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yaz mevsimi, bünyedeki su ve sığır muhatabıyla sınırlıdır; komşu dalın odağı nemli mera bitkisi ve otlak değeridir.","focus_only":"Odak dal yazın su barındıran ve sığırların yediği özel bitkidir.","gloss":"sulu yaz bitkisi ile nemli mera otu","neighbor_only":"Komşu dal nemli bir mera bitkisini veya iyi otlağı daha genel biçimde anlatır.","neighbor_ref":"root_001512/B004","relation_type":"near_neighbor","shared_zone":"İki dal da nemli yapısıyla hayvan yemi olabilen bir bitkiyi gösterir."},{"boundary_match":"field_only","distinction":"Ortak alan mera bitkisidir; mevsimsel-su özelliği ve hayvan türü ayrıldığı için adlandırmalar birbirinin yerine kullanılamaz.","focus_only":"Odak bitkinin yazın su barındırmasını ve sığırlarca yenmesini belirtir.","gloss":"sığır bitkisi ile koyun otu","neighbor_only":"Komşu bitki yeşilken özellikle koyunların sevdiği bir mera otudur.","neighbor_ref":"root_000160/B007","relation_type":"same_field","shared_zone":"Her iki dal otlayan hayvanların yediği belirli bir bitkiyi adlandırır."}],"source_phrase_ar":"الدعدع نبت يكون فيه ماء في الصيف يأكله البقر","source_qualifications":[{"kind":"sole_attestation","summary":"Bitkinin yaz nemi ve sığır yemi oluşu bu tek tanıklıkta birlikte aktarılır."}],"source_summary":"Tek aktarım bitkinin yazın su barındırmasını ve sığırlarca yenmesini birlikte tanıtıcı özellikler olarak verir.","sources":["TA"],"what_is_ar":"نبت يكون فيه ماء في الصيف تأكله البقر","what_is_not_ar":"ليس حب الدعاع ولا عيال الرجل ولا تفرق النخل"},"support_links":[]},{"boundary":"Çekirdek küçük yaştaki çocuklar veya bağımlılardır; yetişkin aile üyeleri, hizmetliler ve genel hane halkı kendiliğinden kapsanmaz.","branch_kind":"bare","branch_ref":"root_000477/B009","candidate_links":[{"candidate_id":"cand_b6e61ee9d293635a85e0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"küçük çocuklar ve bakmakla yükümlü olunan küçükler","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Gönderim, bir erkeğe bakım bağıyla bağlı küçük yaştaki kimselerdir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Türemiş eylem, bu küçük bağımlı grubun sayıca artmasını anlatır."}}],"root_ar":"د ع ع","root_id":"root_000477","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın yaş küçüklüğü ile bakım bağı özelliklerini birlikte karşılayan açıklayıcı Türkçe ifadedir.","boundary_detail":"Çekirdek küçük yaştaki çocuklar veya bağımlılardır; yetişkin aile üyeleri, hizmetliler ve genel hane halkı kendiliğinden kapsanmaz.","branch_image_ar":"الدعاع عيال صغار","concept_gloss":"küçük çocuklar ve bakmakla yükümlü olunan küçükler","contextual_glosses":[{"applicability":"Bağlam bakım bağını zaten gösteriyor ve gönderim doğrudan çocuklarsa doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Çocuk olmayan fakat bakım altında bulunan küçükleri kapsamayabilir.","preserves":"Yaş küçüklüğünü ve aile içindeki bağlılığı korur."},"facet_ids":["F001"],"text":"küçük çocukları","usage_role":"contextual"},{"applicability":"Türemiş eylemin bağımlı küçüklerin sayıca artmasını bildirdiği cümlede kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bakım bağını, küçüklüğü ve sayısal artışı birlikte korur."},"facet_ids":["F001","F002"],"text":"bakmakla yükümlü olduğu küçükler çoğaldı","usage_role":"contextual"}],"definition":"Bir erkeğin küçük yaştaki çocukları veya onun bakımına bağlı küçüklerdir; türemiş kullanım bu grubun sayıca çoğalmasını bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Gönderim, bir erkeğe bakım bağıyla bağlı küçük yaştaki kimselerdir."},{"facet_id":"F002","role":"extension","statement":"Türemiş eylem, bu küçük bağımlı grubun sayıca artmasını anlatır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Eş, yetişkin akraba ve bağımsız aile üyelerini kapsama alır.","collision":"Türkçedeki bütün aile veya hane anlamıyla karışır.","fit":"broadening","loses":"Yaş küçüklüğü ve bakım bağı özelliklerini belirtmez.","preserves":"Kişiye bağlı yakın insan grubunu genel olarak korur."},"text":"aile"}],"identity_rationale":"Yetkili kaynak ifadesi bir erkeğin küçük yaştaki bakmakla yükümlü olduğu kimseleri adlandırır ve türemiş kullanımda bu grubun çoğalmasını bildirir. Dal, genel aile veya bütün hane halkı değil, küçüklük ve bakım bağıyla sınırlıdır.","lexical_glosses":[{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"bir erkeğin küçük çocukları ve bakımına bağlı küçükler"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"bakımına bağlı küçüklerin sayısı çoğalmak"}],"lexicalization_note":"Tanım çıplak dalın küçük bağımlılar anlamını ve onların sayıca çoğalması uzantısını korur; genel aile anlamı eklenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; genel bağımlılar ve geçimi üstlenilenler en açıklayıcı iki sınırı verdi, aile, hane ve hizmet ilişkileri yaş küçüklüğü koşulunu taşımadığı için elendi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal genel bağımlılar alanının yaşça küçük bölümüdür; komşu dal yetişkinleri de kapsayabildiği için sınırlar tam örtüşmez.","focus_only":"Odak dal bağımlıların küçük yaşta olmasını zorunlu kılar.","gloss":"küçük bağımlılar ile genel bağımlılar","neighbor_only":"Komşu dal yaş ayrımı yapmadan bir kişinin bakmakla yükümlü olduğu kimseleri kapsar.","neighbor_ref":"root_001068/B002","relation_type":"near_synonym","shared_zone":"İki dal da bir kişinin bakımına bağlı kimseleri adlandırır."},{"boundary_match":"partial","distinction":"Odak dalın kimliği yaşça küçük bağımlı grubudur; komşu dalın odağı ise yaş sınırından çok geçindirme ve bakım masrafını üstlenme ilişkisidir.","focus_only":"Odak dal bakım altındaki küçük kişilerin kendisini adlandırır.","gloss":"küçük bağımlılar ile geçimi sağlananlar","neighbor_only":"Komşu dal bu kişilerin geçimini sağlama ve yükünü taşıma ilişkisini de kurucu sayar.","neighbor_ref":"root_001062/B008","relation_type":"near_neighbor","shared_zone":"Her iki dal bir kişinin bakmakla yükümlü olduğu kimselerle ilgilidir."}],"source_phrase_ar":"الدعاع عيال الرجل الصغار؛ أدع الرجل إذا كثر دعاعه","source_qualifications":[{"kind":"sole_attestation","summary":"Küçük bağımlılar ile onların çoğalması bu tek tanıklıkta aynı anlam ailesi içinde aktarılır."}],"source_summary":"Tek aktarım küçük bağımlılar adını ve bu grubun sayıca çoğalmasını bildiren türemiş kullanımı birlikte verir.","sources":["TA"],"what_is_ar":"عيال الرجل الصغار وكثرة دعاعه","what_is_not_ar":"ليس النخل المتفرق ولا حب الشجرة ولا النملة السوداء"},"support_links":["sup_409ffd3e1031524f93aa"]},{"boundary":"Çekirdek yabani bitki tohumudur; siyah karınca benzerlik yoluyla, toplayıcı adam ise özel yapı içinde adlandırılır ve ikisi genel tohum anlamını değiştirmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000477/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"yabani bitki tohumu","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel gönderim yabani bir bitkinin tohumudur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Siyah taneli bir biçimi kıtlık veya kuraklık zamanında yiyecek olarak kullanılır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tohuma benzeyen siyah bir karınca benzerlik yoluyla aynı adla anılır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Özel bir kişi yapısı, bu tohumu ve başka bir yabani tohumu yemek için toplayan adamı anlatır."}}],"root_ar":"د ع ع","root_id":"root_000477","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dalın merkezindeki bitkisel gönderimi, bağımlı benzetme ve kişi kullanımlarını çekirdeğe katmadan karşılar.","boundary_detail":"Çekirdek yabani bitki tohumudur; siyah karınca benzerlik yoluyla, toplayıcı adam ise özel yapı içinde adlandırılır ve ikisi genel tohum anlamını değiştirmez.","branch_image_ar":"الدعاع حبة برية","concept_gloss":"yabani bitki tohumu","contextual_glosses":[{"applicability":"Siyah tanenin kıtlık yiyeceği olarak kullanımının öne çıktığı bağlamlarda uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Siyah tane niteliğini ve kuraklıkta yenme kullanımını korur."},"facet_ids":["F001","F002"],"text":"kuraklıkta yenen siyah tohum","usage_role":"contextual"},{"applicability":"Adın benzerlik yoluyla siyah karıncaya aktarıldığı kullanımda açıklayıcı karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Karınca gönderimini, siyah rengi ve tohuma benzerlik bağını korur."},"facet_ids":["F003"],"text":"tohuma benzeyen siyah karınca","usage_role":"explanatory"}],"definition":"Yabani bir bitkinin tohumu; özel bir biçimi kuraklıkta yiyecek olarak kullanılan siyah bir tanedir. Benzer siyah karınca bu taneye benzetilerek, onu başka bir yabani tohumla birlikte toplayan adam ise yapıya bağlı olarak adlandırılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel gönderim yabani bir bitkinin tohumudur."},{"facet_id":"F002","role":"specialization","statement":"Siyah taneli bir biçimi kıtlık veya kuraklık zamanında yiyecek olarak kullanılır."},{"facet_id":"F003","role":"extension","statement":"Tohuma benzeyen siyah bir karınca benzerlik yoluyla aynı adla anılır."},{"facet_id":"F004","role":"associated_use","statement":"Özel bir kişi yapısı, bu tohumu ve başka bir yabani tohumu yemek için toplayan adamı anlatır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Belirli ve farklı bir baklagil türü kimliği ekler.","collision":"Bilinen baklagil adıyla yanlış tür özdeşliği doğurur.","fit":"displacement","loses":"Yabani bitki kimliğini, kuraklık kullanımını ve benzerlik uzantılarını kaybeder.","preserves":"Yenebilen küçük bir bitki tohumu olma özelliğini korur."},"text":"mercimek"}],"identity_rationale":"Yetkili kaynak ifadesi yabani bir bitkinin tohumu çekirdeğine, kuraklıkta yenen siyah bir tohum biçimine, bu tohuma benzetilerek adlandırılan siyah karıncaya ve tohumu toplayan kişiye uzanır. Bunlar tek bir yalın tanımda eşit çekirdekler değildir; bitki tohumu merkezde, benzetme ve toplama kullanımları bağımlı tutulmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"yabani bir bitkinin tohumu"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"kuraklıkta yenen siyah tohum; ona benzeyen siyah karınca"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"bu tohumu ve başka bir yabani tohumu yemek için toplayan adam"}],"lexicalization_note":"Yalın tohum anlamı, benzerlikle adlandırılan karınca ve tohum toplayan adamı bildiren özel yapıdan ayrılır; yapıdaki kişi anlamı çıplak dala taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; başka tohum adları arasından tür karışmasını ve kıtlık yiyeceği bağlamını açıklayan iki aday seçildi, meyve rengi ve salkım yapısı gibi uzak benzerlikler elendi.","neighbor_distinctions":[{"boundary_match":"field_only","distinction":"Ortak alan tohumdur; odak dal yabani tür, kıtlık yiyeceği ve benzerlik uzantılarıyla sınırlıyken komşu dal başka belirli ürünlerin tanelerini gösterir.","focus_only":"Odak dal yabani bir bitki tohumu ile onun siyah tane ve benzetme uzantılarını kapsar.","gloss":"yabani tohum ile bilinen baharat taneleri","neighbor_only":"Komşu dal susam, kişniş veya başka belirli taneler için kullanılan farklı bir tohum adıdır.","neighbor_ref":"root_000255/B011","relation_type":"same_field","shared_zone":"İki dal da küçük bitki tanelerini veya tohumlarını adlandırır."},{"boundary_match":"thematic_only","distinction":"Odak dal somut bir bitki tohumu adıdır; komşu dal ise tür belirtmeyen, az miktarda geçim sağlayan yiyecek veya ot kavramıdır.","focus_only":"Odak dal kuraklıkta yenebilen belirli yabani tohumu adlandırır.","gloss":"kıtlık tohumu ile asgari geçimlik","neighbor_only":"Komşu dal yaşamı sürdürmeye yeten az miktardaki herhangi bir yiyecek veya otu anlatır.","neighbor_ref":"root_001039/B006","relation_type":"thematic","shared_zone":"Her ikisi de yiyecek kıtlığında yaşamı sürdürmeye yarayan besin bağlamında bulunabilir."}],"source_phrase_ar":"الدعاع حب شجرة برية؛ الدعاعة حبة سوداء؛ نملة سوداء تشاكل هذه الحبة؛ رجل دعاع فثاث","source_qualifications":[{"kind":"sole_attestation","summary":"Tohum, kıtlık yiyeceği, benzer siyah karınca ve toplayıcı kişi uzantıları bu tek tanıklıkta birlikte verilir."}],"source_summary":"Tek aktarım yabani tohumu çekirdek alır; yenilen siyah tane, ona benzeyen karınca ve tohum toplayan kişi kullanımlarını buna bağlar.","sources":["TA"],"what_is_ar":"حب شجرة برية وحبة سوداء تؤكل في القحط ونملة سوداء تشاكلها","what_is_not_ar":"ليس عيال الرجل ولا الدعدع النبت ولا تفرق النخل"},"support_links":[]},{"boundary":"Temel seslenme anlamı, yalnızca belirli yapılarda görülen yemeğe çağırma ve bir yere yönelme kullanımlarından ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000478/B001","candidate_links":[{"candidate_id":"cand_ceecaf70ededba2ca837","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"seslenerek kendine yöneltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ses ve söz, yöneltilen kişiyi ya da şeyi konuşana doğru çekmenin aracıdır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yemeğe çağırma, yöneltme çekirdeğinin belirli bir etkinliğe bağlı özel kullanımıdır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli bir yeri amaçlayıp oraya gitme, yerin kişiyi çağırdığı varsayımıyla anlatılan mecazlı bir uzantıdır."}}],"root_ar":"د ع ع","root_id":"root_000478","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sesli ve sözlü bir çağrının hedefi konuşana ya da onun belirlediği yöne çektiği temel anlam için uygundur.","boundary_detail":"Temel seslenme anlamı, yalnızca belirli yapılarda görülen yemeğe çağırma ve bir yere yönelme kullanımlarından ayrı tutulur.","branch_image_ar":"النداء والإمالة بالكلام","concept_gloss":"seslenerek kendine yöneltme","contextual_glosses":[{"applicability":"Bir kişiye seslenip onu konuşana veya belirlenen yere yöneltme bağlamlarında doğal bir karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yemeğe çağırma ile yerin çağırdığı varsayımına dayanan yönelme uzantılarını tek başına göstermez.","preserves":"Seslenme ve hedefi bir yöne çekme eylemini korur."},"facet_ids":["F001"],"text":"çağırmak","usage_role":"general"},{"applicability":"Yalnızca birini yemek için çağıran özel yapı söz konusu olduğunda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel çağırma çekirdeğini ve yer yönelimi uzantısını kapsamaz.","preserves":"Bir kişiyi ses ve sözle belirli bir etkinliğe yöneltme anlamını korur."},"facet_ids":["F002"],"text":"yemeğe çağırmak","usage_role":"contextual"},{"applicability":"Yalnızca kişinin belirtilen yeri hedefleyerek oraya yöneldiğini anlatan özel yapı için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yerin kişiyi çağırdığı varsayımını ve genel seslenme çekirdeğini açıkça taşımaz.","preserves":"Belirli bir yere yönelme ve o yeri amaçlama sonucunu korur."},"facet_ids":["F003"],"text":"o yeri amaçlayıp gitmek","usage_role":"explanatory"}],"definition":"Ses ve söz kullanarak birini ya da bir şeyi konuşana doğru yöneltmektir. Yemeğe çağırma ve bir yeri amaçlayıp oraya gitme, bu çekirdeğin yapıya bağlı özel gerçekleşmeleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ses ve söz, yöneltilen kişiyi ya da şeyi konuşana doğru çekmenin aracıdır."},{"facet_id":"F002","role":"specialization","statement":"Yemeğe çağırma, yöneltme çekirdeğinin belirli bir etkinliğe bağlı özel kullanımıdır."},{"facet_id":"F003","role":"extension","statement":"Belirli bir yeri amaçlayıp oraya gitme, yerin kişiyi çağırdığı varsayımıyla anlatılan mecazlı bir uzantıdır."}],"excluded_glosses":[{"category":"common_loanword","error_profile":{"adds":"Türkçede toplumsal veya resmî bir etkinliğe çağırma çağrışımını öne çıkarabilir.","collision":"Yalın seslenme ile yapıya bağlı yemeğe çağırma anlamlarının sınırını belirsizleştirir.","fit":"drifted_loanword","loses":"Ses ve sözle kendine yöneltme çekirdeğini ve yer yönelimi uzantısını kapsamaz.","preserves":"Birini belirli bir şeye yöneltme düşüncesini kısmen korur."},"text":"davet etmek"}],"identity_rationale":"Kaynak ifadesi, ses ve söz yoluyla bir şeyi konuşana doğru yöneltmeyi temel anlam olarak verir; yemeğe çağırmayı ve bir yere yönelmeyi de bu çekirdeğe bağlı özel kullanımlar olarak gösterir.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"seslenmek; çağırmak"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"yemeğe çağırma"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"belirtilen yeri amaçlayıp oraya gitmek"}],"lexicalization_note":"Tanım yalın seslenme çekirdeğini kapsar; yemeğe çağırma ile belirli bir yere yönelme anlamları yalnızca kendi yapıları içinde geçerlidir.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Yayınlanan üç komşu, çağırma eylemini yüksek ses, yaklaşma emri ve seslenme parçacığından ayırır; diğer adaylar ya daha uzak bir ortak sahne paylaşır ya da kardeş dallardaki ayrı anlamları yineler.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Bu dalda belirleyici unsur sözlü çağrıyla yöneltmedir; komşuda ise çağrının yüksek ve güçlü sesle yapılması başlı başına anlam çekirdeğidir.","focus_only":"Hedefi ses ve sözle konuşana doğru yöneltme ilişkisini kurar; sesin yüksek olması zorunlu değildir.","gloss":"yüksek sesle seslenme","neighbor_only":"Çağrının yönünden çok sesin yükseltilmesini ve güçlü biçimde duyurulmasını öne çıkarır.","neighbor_ref":"root_001484/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir kişiye sesle ulaşma ve onu çağırma alanında buluşur."},{"boundary_match":"field_only","distinction":"Odak dal genel çağırma eylemidir; komşu dal ise yaklaşma isteğini bildiren belirli bir emir ifadesidir.","focus_only":"Birini ses ve söz yoluyla kendine doğru yöneltme eylemini adlandırır.","gloss":"gelmeye çağıran emir","neighbor_only":"Yaklaşmayı isteyen kalıplaşmış bir emir ve ünlem işlevi taşır.","neighbor_ref":"root_000383/B009","relation_type":"same_field","shared_zone":"İki dal da bir muhatabı konuşana ya da belirtilen noktaya yaklaşmaya yöneltir."},{"boundary_match":"field_only","distinction":"Bu dal çağırma eyleminin kendisini tanımlar; komşu dal o eylemde kullanılan dil bilgisel seslenme araçlarını tanımlar.","focus_only":"Seslenme aracılığıyla muhatabın yönelmesini sağlayan eylemi anlatır.","gloss":"seslenme parçacığı","neighbor_only":"Yakın veya uzak muhataba seslenmede kullanılan çağrı parçacıklarını adlandırır.","neighbor_ref":"root_000074/B008","relation_type":"same_field","shared_zone":"Her ikisi de bir muhataba yöneltilen sözlü çağrı alanındadır."}],"source_phrase_ar":"أصل واحد وهو أن تميل الشيء إليك بصوت وكلام يكون منك؛ دعوت أدعو دعاء؛ الدعوة إلى الطعام بالفتح؛ دعا فلانا مكان كذا إذا قصد ذلك المكان كأن المكان دعاه","source_summary":"Tek kaynak iddiası, ses ve sözle kendine yöneltme çekirdeğini; yemeğe çağırmayı ve bir yeri amaçlayarak oraya gitmeyi bu çekirdeğe bağlı kullanımlar halinde birlikte sunar.","sources":["MQ"],"what_is_ar":"الدعاء والنداء والإمالة إلى الشيء بصوت وكلام والدعوة إلى الطعام وقصد المكان بدعائه مجازا","what_is_not_ar":"ليس ادعاء النسب ولا ادعاء الحق ولا تداعي السقوط ولا دواعي الدهر"},"support_links":["sup_16ff0b02a06e911120e2"]},{"boundary":"Hak ileri sürme, soy bağı kurma ve savaşta aidiyet bildirme ayrımları korunur; bunlar sıradan seslenme anlamına indirgenmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000478/B002","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"hak veya aidiyet ileri sürme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hak, kişinin kendisi ya da başka biri lehine ileri sürülür."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir çocuk veya kişi için soy bağı ileri sürülerek onu belirli bir babaya ya da soya bağlama anlamı vardır."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Savaş bağlamında kişi soyunu söyleyerek kendini ve bağlı olduğu topluluğu bildirir."}}],"root_ar":"د ع ع","root_id":"root_000478","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem bir hak talebini hem de soy veya topluluk bağı iddiasını ortak çekirdekte anlatmak için uygundur.","boundary_detail":"Hak ileri sürme, soy bağı kurma ve savaşta aidiyet bildirme ayrımları korunur; bunlar sıradan seslenme anlamına indirgenmez.","branch_image_ar":"ادعاء الحق والانتساب","concept_gloss":"hak veya aidiyet ileri sürme","contextual_glosses":[{"applicability":"Kişinin kendisi veya başkası adına bir hak ileri sürdüğü bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Soy bağı ve savaşta aidiyet bildirme kullanımlarını kapsamaz.","preserves":"Bir hakka sahip olunduğunu ileri sürme eylemini korur."},"facet_ids":["F001"],"text":"hak iddia etmek","usage_role":"general"},{"applicability":"Bir kişiyi belirli bir baba, soy veya toplulukla ilişkilendiren iddia için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Soy dışındaki hak iddialarını ve savaş bağlamındaki kendini tanıtma işlevini dışarıda bırakır.","preserves":"Soy ilişkisini iddia yoluyla kurma anlamını korur."},"facet_ids":["F002"],"text":"soy bağı ileri sürmek","usage_role":"contextual"},{"applicability":"Kişinin savaş sırasında hangi soydan geldiğini söyleyerek kendini tanıttığı özel kullanım içindir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel hak iddiasını ve başkasına soy bağı yükleme kullanımını kapsamaz.","preserves":"Savaş bağlamını, soy bildirimini ve kendini tanıtma işlevini korur."},"facet_ids":["F003"],"text":"savaşta soyunu bildirerek tanınmak","usage_role":"explanatory"}],"definition":"Kişinin kendisi veya başkası adına bir hak ya da aidiyet bağı ileri sürmesidir. Soy veya çocuk bağı kurma ve savaşta soyunu söyleyerek kendini tanıtma, bu iddia eyleminin özel biçimleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hak, kişinin kendisi ya da başka biri lehine ileri sürülür."},{"facet_id":"F002","role":"specialization","statement":"Bir çocuk veya kişi için soy bağı ileri sürülerek onu belirli bir babaya ya da soya bağlama anlamı vardır."},{"facet_id":"F003","role":"specialization","statement":"Savaş bağlamında kişi soyunu söyleyerek kendini ve bağlı olduğu topluluğu bildirir."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Sesli bir çağrı yapıldığı anlamını gereksiz yere ekler.","collision":"Aynı kökün çağırma dalıyla karışır ve bu dalın iddia sınırını bozar.","fit":"displacement","loses":"Hak veya aidiyet ileri sürme işlemini bütünüyle kaybeder.","preserves":"Bir kişiye yönelen eylem düşüncesini çok genel biçimde korur."},"text":"seslenme"}],"identity_rationale":"Kaynak ifadesi, kişinin kendisi veya başkası adına bir hak ileri sürmesini temel alır; soy ve çocuk bağı iddiası ile savaşta soyunu bildirerek kendini tanıtmayı aynı iddia alanında özel biçimler olarak verir.","lexical_glosses":[{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"soy bağı ileri sürme"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"kendisi veya başkası adına hak iddia etme"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"savaşta soyunu söyleyerek kendini tanıtma"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"öz babasından başkasına bağlanan kişi"}],"lexicalization_note":"Genel hak ileri sürme biçimi ile soy ve savaş bağlamlarına bağlı yapılar ayrı tutulur; özel kullanımlar yalın biçimin tamamına yayılmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. Seçilen komşular, soy iddiasını başka bir soya bağlama, aidiyet bildirme ve genel soy ilişkisi alanlarından ayırır; kalanlar daha dar tarihsel kullanımlar, uzak çağrışımlar veya kardeş dallardır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal daha geniş bir iddia alanına sahiptir; komşu dal özellikle kişinin başka bir soya ya da babaya bağlanması işlemiyle sınırlıdır.","focus_only":"Hak iddiasını, savaşta soy bildirimini ve kişinin kendisi veya başkası adına ileri sürülen bağı kapsar.","gloss":"başka bir soya bağlama","neighbor_only":"Bir kişinin bir topluluğa veya öz babası dışındaki birine eklenmesi sonucuna odaklanır.","neighbor_ref":"root_001347/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir kişinin soy veya topluluk bağına iddia yoluyla yerleştirilmesini kapsar."},{"boundary_match":"partial","distinction":"Bu dalda bağ bir iddia olarak ortaya konur; komşuda ağırlık, var olan aidiyeti bir baba veya topluluğa bağlayarak bildirmededir.","focus_only":"Bir hak veya soy bağı ileri sürme niteliğini taşır ve ileri sürülen bağ doğru ya da yanlış olabilir.","gloss":"soyunu ve aidiyetini bildirme","neighbor_only":"Bir kişiyi babasına ya da topluluğuna bağlama ve o aidiyeti bildirme eylemini iddia niteliği aramadan kapsar.","neighbor_ref":"root_001011/B001","relation_type":"near_neighbor","shared_zone":"Soy veya topluluk aidiyetini dile getirme ve savaşta bu bağla tanınma alanları ortaktır."},{"boundary_match":"field_only","distinction":"Odak dal iddia eylemini gerektirir; komşu dal ise iddia bulunmasa da soy ve nispet ilişkilerinin kendisini anlatır.","focus_only":"Soy bağını ileri sürülen bir hak veya iddia olarak ele alır.","gloss":"soy ve nispet ilişkisi","neighbor_only":"Akrabalık bağlarını, soy bilgisini ve kişi, yer ya da mesleğe nispeti geniş biçimde kapsar.","neighbor_ref":"root_001494/B001","relation_type":"same_field","shared_zone":"Her iki dal da kişilerin bir soya veya topluluğa bağlanması alanındadır."}],"source_phrase_ar":"الادعاء أن تدعي حقا لك أو لغيرك (maqayis)؛ الادعاء في الحرب الاعتزاء (maqayis)؛ الدعوة ادعاء الولد الدعي غير أبيه ويدعيه غير أبيه (ayn)؛ الدعوة في النسب بالكسر (maqayis)","source_summary":"Toplu iddia, hak ileri sürme çekirdeği yanında soy veya çocuk bağı kurmayı ve savaşta soy bildirerek kendini tanıtmayı birbirinden ayrılan özel gerçekleşmeler olarak kapsar.","sources":["MQ","AY"],"what_is_ar":"ادعاء حق للنفس أو للغير وادعاء النسب والولد والاعتزاء في الحرب","what_is_not_ar":"ليس مجرد النداء إلى الطعام ولا تداعي الحيطان ولا دواعي الدهر"},"support_links":[]},{"boundary":"Anlam yalnızca memede bırakılan sütün sonraki sütü çekmesi düşüncesine bağlıdır; genel süt kalıntısına yayılmaz.","branch_kind":"collocation","branch_ref":"root_000478/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"sütün devamını çekmek için memede bırakılan pay","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sağımda sütün bir bölümü memede bilerek bırakılır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bırakılan payın işlevi, ardından gelecek sütün akışını uyarmaktır."}}],"root_ar":"د ع ع","root_id":"root_000478","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Sağımda kalan sütün tesadüfi değil, sonraki sütün gelmesini uyarmak için bilerek bırakıldığı özel kavramı karşılar.","boundary_detail":"Anlam yalnızca memede bırakılan sütün sonraki sütü çekmesi düşüncesine bağlıdır; genel süt kalıntısına yayılmaz.","branch_image_ar":"داعية اللبن","concept_gloss":"sütün devamını çekmek için memede bırakılan pay","contextual_glosses":[{"applicability":"Sütçülük bağlamında, sonraki sütün akmasını sağlamak üzere memede bırakılan miktarı kısa biçimde anlatır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Payın özellikle memede bırakıldığını ve sonraki sütü çektiğini açıkça söylemez.","preserves":"Bırakılan payın sağımın devamını sağlama işlevini korur."},"facet_ids":["F001","F002"],"text":"sağımı sürdürme payı","usage_role":"explanatory"}],"definition":"Sonraki sütün gelmesini sağlamak için sağım sırasında memede bilerek bırakılan süt payıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sağımda sütün bir bölümü memede bilerek bırakılır."},{"facet_id":"F002","role":"specialization","statement":"Bırakılan payın işlevi, ardından gelecek sütün akışını uyarmaktır."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sütün bilerek bırakılmasını ve sonraki sütün gelmesini sağlama amacını kaybeder.","preserves":"Sağım sonrasında memede bir miktar süt bulunmasını korur."},"text":"süt kalıntısı"}],"identity_rationale":"Kaynak ifadesi, sonraki sütün gelmesini sağlamak amacıyla memede bilerek bırakılan süt miktarını açıkça tanımlar; hazırlanan dal çerçevesi bu amaç ve araç ilişkisini doğru korur.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"sonraki sütü çekmek için memede bırakılan süt payı"}],"lexicalization_note":"Tanım yalnızca verilen sütçülük yapısına bağlıdır ve kökün yalın biçimine bağımsız bir anlam olarak aktarılamaz.","neighbor_coverage_note":"Adayların tamamı incelendi. Seçilen komşular, amaçlı bırakılan süt payını az süt kalıntısından, memeyi sıvazlamaktan ve az az sağmaktan ayırır; öteki adaylar sağımın başka aşamalarına veya kardeş anlamlara aittir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal kalanın amacıyla tanımlanır; komşu dal ise miktarın azlığıyla tanımlanır ve sonraki sütü çekme işlevini gerektirmez.","focus_only":"Memede kalan sütün sonraki sütü getirmesi için bilerek bırakılmasını gerektirir.","gloss":"memede kalan az süt","neighbor_only":"Memede kalan sütün az ve yudumluk miktarda oluşunu anlatır; özel bir işlev şart koşmaz.","neighbor_ref":"root_000237/B003","relation_type":"near_synonym","shared_zone":"Her iki dal da sağım sonrasında memede bulunan küçük bir süt miktarını konu eder."},{"boundary_match":"partial","distinction":"Bu dalda uyarıcı araç memede bırakılan süt payıdır; komşuda araç memenin sıvazlanmasıdır.","focus_only":"Süt akışını uyarmak için memede bırakılan sütün kendisini adlandırır.","gloss":"memeyi uyararak süt indirme","neighbor_only":"Memeyi sıvazlayarak sütü indirme eylemini ve bu yolla süt veren hayvanı kapsar.","neighbor_ref":"root_001416/B001","relation_type":"near_neighbor","shared_zone":"İki dal da memeden yeni süt akışını başlatma veya sürdürme amacı taşır."},{"boundary_match":"field_only","distinction":"Odak dal sütü bırakır ve işlevini bekler; komşu dal az miktardaki sütü belirli bir sağım biçimiyle dışarı alır.","focus_only":"Bir miktar sütü sonraki akışı sağlamak üzere memede bırakmayı anlatır.","gloss":"az az ve uçlardan sağma","neighbor_only":"Parmak uçlarıyla az az sağmayı, yavaş akışı ve kalan sütü çekip almayı kapsar.","neighbor_ref":"root_001428/B001","relation_type":"same_field","shared_zone":"Her iki dal da memedeki az miktardaki süt ve sağımın sürdürülmesi alanındadır."}],"source_phrase_ar":"داعية اللبن ما يترك في الضرع ليدعو ما بعده","source_summary":"Tek iddia, memede süt bırakma işlemini ve bu işlemin sonraki sütün gelmesini sağlama amacını ayrılmaz biçimde birleştirir.","sources":["MQ"],"what_is_ar":"ما يترك في الضرع من اللبن ليدعو ما بعده","what_is_not_ar":"ليس دعوة الطعام ولا دعوة النسب ولا دعاء الصوت العام"},"support_links":[]},{"boundary":"Anlam, belirli yapıda Tanrı'nın istenmeyen bir şeyi kişinin başına getirmesidir; kötülük dileme eylemi değildir.","branch_kind":"collocation","branch_ref":"root_000478/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"Tanrı'nın birine istemediği bir sıkıntıyı vermesi","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tanrı, kişiye onun hoşlanmadığı bir şeyi yöneltir ve başına getirir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kaynak açıklaması sözlü bir kötülük isteğini değil, istenmeyen sonucun kişide gerçekleşmesini öne çıkarır."}}],"root_ar":"د ع ع","root_id":"root_000478","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tanrı'nın bir kişinin başına o kişinin hoşlanmadığı bir olay veya sıkıntı getirdiğini bildiren özel yapı için uygundur.","boundary_detail":"Anlam, belirli yapıda Tanrı'nın istenmeyen bir şeyi kişinin başına getirmesidir; kötülük dileme eylemi değildir.","branch_image_ar":"الدعاء بالمكروه النازل","concept_gloss":"Tanrı'nın birine istemediği bir sıkıntıyı vermesi","contextual_glosses":[{"applicability":"Eyleyeni geri planda bırakıp kişi açısından gerçekleşen istenmeyen sonucu anlatmak gerektiğinde kullanılabilir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Sonucu Tanrı'nın meydana getirdiğini açıkça belirtmez.","preserves":"Kişinin başına hoşlanmadığı bir sıkıntının gelmesi sonucunu korur."},"facet_ids":["F001"],"text":"başına istemediği bir sıkıntı gelmek","usage_role":"explanatory"}],"definition":"Belirli yapıda, Tanrı'nın bir kişinin başına onun hoşlanmadığı bir sıkıntıyı getirmesini anlatır. Odak, birinin kötülük dilemesi değil, istenmeyen olayın kişiye yönelip gerçekleşmesidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tanrı, kişiye onun hoşlanmadığı bir şeyi yöneltir ve başına getirir."},{"facet_id":"F002","role":"source_variant","statement":"Kaynak açıklaması sözlü bir kötülük isteğini değil, istenmeyen sonucun kişide gerçekleşmesini öne çıkarır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Bir insanın sözlü istekte bulunduğu ayrı bir konuşma eylemi ekler.","collision":"Sonucun gerçekleşmesini, o sonucun gerçekleşmesini isteme eylemiyle karıştırır.","fit":"displacement","loses":"Kaynakta bildirilen gerçekleşmiş ilahi yöneltme ve meydana gelme ilişkisini kaybeder.","preserves":"Bir kişiye yönelen istenmeyen sonuç düşüncesini korur."},"text":"kötülük dilemek"}],"identity_rationale":"Hazırlanan çerçeve bunu birine kötülük gelmesi için söz söyleme olarak sunarken kaynak ifadesi, Tanrı'nın kişinin başına hoşlanmadığı şeyi getirmesini ve olayın gerçekleşmesini anlatır. Dal korunabilir, ancak tanım sözlü dilekten gerçekleşen sıkıntıya kaydırılmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"Tanrı'nın birinin başına hoşlanmadığı bir sıkıntıyı getirmesi"}],"lexicalization_note":"Düzeltilen anlam yalnızca verilen Tanrı, kişi ve istenmeyen sonuç yapısında geçerlidir; yalın çağırma anlamına genellenmez.","neighbor_coverage_note":"Bütün adaylar karşılaştırıldı. Seçilenler gerçekleşen sıkıntıyı kötülük dileme, lanetleme ve sıkıntının kendisinden ayırır; kalanlar uzak sonuç türleri veya bu kökün başka dallarıdır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gerçekleşen ilahi yöneltmeyi bildirir; komşu dal ise kötü sonucun gerçekleşmesi için söylenen sözü anlatır.","focus_only":"Tanrı'nın istenmeyen şeyi kişinin başına getirmesi ve sonucun gerçekleşmesi anlatılır.","gloss":"birine kötülük dileme","neighbor_only":"Bir kişinin başkasına kötülük yönelten söz söylemesi öne çıkar.","neighbor_ref":"root_000792/B012","relation_type":"near_neighbor","shared_zone":"Her iki dal da belirli bir kişinin başına kötü bir şey gelmesi düşüncesini taşır."},{"boundary_match":"thematic_only","distinction":"Bu dal sonuç bildiren özel bir yapıdır; komşu dal sözlü lanetleme veya karşılıklı sınama eylemidir.","focus_only":"İstenmeyen sonucun Tanrı tarafından kişiye verilmesini bildirir.","gloss":"lanetleme ve karşılıklı kötülük isteme","neighbor_only":"Lanetleme ve karşılıklı olarak yalancının cezalandırılmasını isteme törenlerini kapsar.","neighbor_ref":"root_000159/B003","relation_type":"thematic","shared_zone":"İki dal da Tanrı ile ilişkilendirilen kötü bir sonucun kişiye yönelmesi sahnesini paylaşır."},{"boundary_match":"partial","distinction":"Odak dal sıkıntının kişiye yöneltilmesini anlatır; komşu dal yönelten bir eyleyen gerektirmeden sıkıntı durumunu adlandırır.","focus_only":"Sıkıntının belirli bir eyleyen tarafından kişiye getirilmesi ilişkisini içerir.","gloss":"şiddetli sıkıntı ve zarar","neighbor_only":"Sıkıntı, zarar veya güçlüğün kendisini ve onun yoğunluğunu anlatır.","neighbor_ref":"root_000102/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal da kişinin yaşadığı hoş olmayan ve zarar verici durumu kapsar."}],"source_phrase_ar":"دعا الله فلانا بما يكره أي أنزل به ذلك","source_summary":"Tek kaynak iddiası, Tanrı'nın bir kişiye hoşlanmadığı şeyi indirmesi veya başına getirmesi sonucunu bildirir; sözlü bir kötülük dileme işlemi belirtmez.","sources":["MQ"],"what_is_ar":"إنزال المكروه بأحد في قولهم دعا الله فلانا بما يكره","what_is_not_ar":"ليس دعاء العبادة ولا الدعوة إلى الطعام ولا ادعاء النسب"},"support_links":[]},{"boundary":"Birbiri ardından gerçekleşme her iki kullanımda da kurucudur; tek bir çökme veya tek seferde yıkma dalın tamamını karşılamaz.","branch_kind":"mixed_non_bare","branch_ref":"root_000478/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"birbiri ardından çökme veya yıkma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yapısal bozulma tek seferde değil, parçaların birbirini izlemesiyle gerçekleşir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Duvarlar veya yapı parçaları kendiliğinden birbiri ardından çöker."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir eyleyen, yapı parçalarını hedefin üzerine birbiri ardından yıkar."}}],"root_ar":"د ع ع","root_id":"root_000478","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hem yapı parçalarının sırayla çökmesini hem de bir eyleyenin onları sırayla yıkmasını kapsayan üst karşılıktır.","boundary_detail":"Birbiri ardından gerçekleşme her iki kullanımda da kurucudur; tek bir çökme veya tek seferde yıkma dalın tamamını karşılamaz.","branch_image_ar":"التداعي بالسقوط","concept_gloss":"birbiri ardından çökme veya yıkma","contextual_glosses":[{"applicability":"Duvar veya yapı parçalarının kendiliğinden ve sırayla düştüğü kullanım için doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bir eyleyenin parçaları birbiri ardından yıkması kullanımını kapsamaz.","preserves":"Yapı parçalarının ardışık biçimde çökmesini korur."},"facet_ids":["F001","F002"],"text":"birbiri ardınca çökmek","usage_role":"contextual"},{"applicability":"Bir eyleyenin yapı parçalarını hedefin üzerine sırayla yıktığı kullanım için uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Yapının kendiliğinden ardışık çökmesi kullanımını kapsamaz.","preserves":"Ettirgen yıkmayı ve parçaların sıra ile devrilmesini korur."},"facet_ids":["F001","F003"],"text":"birbiri ardınca yıkmak","usage_role":"contextual"}],"definition":"Bir yapının parçalarının birbiri ardından çökmesi veya bir eyleyenin onları birbiri ardından yıkmasıdır. Her iki durumda da tek olay değil, birbirini izleyen bir bozulma dizisi vardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yapısal bozulma tek seferde değil, parçaların birbirini izlemesiyle gerçekleşir."},{"facet_id":"F002","role":"specialization","statement":"Duvarlar veya yapı parçaları kendiliğinden birbiri ardından çöker."},{"facet_id":"F003","role":"specialization","statement":"Bir eyleyen, yapı parçalarını hedefin üzerine birbiri ardından yıkar."}],"excluded_glosses":[{"category":"alternative","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Parçaların birbiri ardından gelmesini ve ettirgen yıkma kullanımını kaybeder.","preserves":"Yapının ayakta kalma durumunu yitirerek düşmesini korur."},"text":"çökmek"}],"identity_rationale":"Kaynak ifadesi iki bağlı süreci açıkça verir: duvarların birbiri ardından çökmesi ve yapıların birbiri ardından yıkılması. Hazırlanan çerçeve, ardışıklığı ve çökme ile ettirgen yıkma ayrımını korur.","lexical_glosses":[{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"duvarların birbiri ardından çökmesi"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"yapıları üzerlerine birbiri ardından yıkmak"}],"lexicalization_note":"Kendiliğinden ardışık çöküş ile bir eyleyenin ardışık yıkması ayrı yapılara bağlı iki facet olarak korunur.","neighbor_coverage_note":"Tüm adaylar değerlendirildi. Yayınlanan komşular ardışıklık sınırını genel çökme, sonucu öne çıkan yıkım ve aşağı yönlü çöküşten ayırır; kalan adaylar kırma, zayıflama, düzleme veya kardeş anlam alanlarında daha uzaktır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal için ardışıklık kurucudur; komşu dal tek bir çöküşü de kapsar ve sıra ilişkisi gerektirmez.","focus_only":"Çöküşün veya yıkmanın parçalar arasında sıra halinde ilerlemesini ve ettirgen seçeneği kapsar.","gloss":"genel çökme ve yıkılma","neighbor_only":"Bir şeyin genel olarak düşmesi veya yıkılmasını, ayrıca ağacın kökünden çıkmasını kapsar.","neighbor_ref":"root_000450/B002","relation_type":"near_synonym","shared_zone":"Her iki dal da bir yapının ayakta kalma durumunu yitirip çökmesini anlatır."},{"boundary_match":"partial","distinction":"Bu dal olayların sırasıyla tanımlanır; komşu dal ise yıkımın dayanıklılığı ve düzeni yok eden sonucuyla tanımlanır.","focus_only":"Birbiri ardından çökme veya yıkma düzenini vurgular.","gloss":"dayanağı yok eden yıkılış","neighbor_only":"Yıkılmanın taşıyıcı düzeni, gücü veya itibarı ortadan kaldıran sonucunu da kapsar.","neighbor_ref":"root_000204/B004","relation_type":"near_synonym","shared_zone":"İki dal da yapıların yıkılması ve ayakta tutan düzenin bozulması alanında örtüşür."},{"boundary_match":"partial","distinction":"Odak dalın ayırıcı özelliği ardışık sıra, komşunun ayırıcı özelliği ise aşağıya veya derine doğru çöküş yönüdür.","focus_only":"Birden çok parçanın birbirini izleyerek çökmesini veya yıkılmasını gerektirir.","gloss":"aşağıya doğru çöküp dağılma","neighbor_only":"Bir yapının ya da kenarın yüksekten aşağıya veya çukura doğru çöküş yönünü öne çıkarır.","neighbor_ref":"root_001607/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da yapı parçalarının düşmesi ve bütünlüğün bozulması olayını kapsar."}],"source_phrase_ar":"تداعت الحيطان وذلك إذا سقط واحد وآخر بعده؛ داعيناها عليهم إذا هدمناها واحدا بعد آخر","source_summary":"Tek iddia, ardışık çöküşü ve ardışık ettirgen yıkmayı aynı sıra ilişkisi altında birleştirir; eyleyenin bulunup bulunmaması iki kullanımı ayırır.","sources":["MQ"],"what_is_ar":"سقوط بعض الشيء إثر بعض وهدمه واحدا بعد آخر","what_is_not_ar":"ليس النداء بالكلام ولا ادعاء الحق ولا دعوة الطعام"},"support_links":[]},{"boundary":"Tanım, insanın yönelmesini değil, dönemin olayların akışını başka yöne çeviren değişimlerini merkeze alır.","branch_kind":"collocation","branch_ref":"root_000478/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"dönemin olaylara yön veren değişimleri","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Dönem, değişen koşullar ve gelişmeler yoluyla olayların akışına yön verir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Olayların başka yöne çevrilmesi, temel yöneltme ilişkisini zamansal değişimlere taşıyan mecazlı bir uzantıdır."}}],"root_ar":"د ع ع","root_id":"root_000478","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dönemin getirdiği değişimlerin olayların seyrini etkilediğini anlatan özel kullanım için uygundur.","boundary_detail":"Tanım, insanın yönelmesini değil, dönemin olayların akışını başka yöne çeviren değişimlerini merkeze alır.","branch_image_ar":"دواعي الدهر","concept_gloss":"dönemin olaylara yön veren değişimleri","contextual_glosses":[{"applicability":"Yön verme benzetisini açmadan, dönem içinde meydana gelen değişim ve gelişmeleri doğal Türkçeyle anlatır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bu değişimlerin olayların yönünü çevirdiği mecazlı ilişkiyi açıkça göstermez.","preserves":"Dönemin değişkenliğini ve onunla birlikte ortaya çıkan olayları korur."},"facet_ids":["F001"],"text":"dönemin değişimleri ve getirdiği olaylar","usage_role":"explanatory"}],"definition":"Dönemin olayların akışını başka yöne çeviren değişimleri ve getirdiği gelişmelerdir. Yöneltme düşüncesi burada sesli bir çağrı değil, olayların seyrine etki eden mecazlı bir güçtür.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Dönem, değişen koşullar ve gelişmeler yoluyla olayların akışına yön verir."},{"facet_id":"F002","role":"extension","statement":"Olayların başka yöne çevrilmesi, temel yöneltme ilişkisini zamansal değişimlere taşıyan mecazlı bir uzantıdır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Kaynakta kurucu olmayan insan katılımcısını ve onun edilgin biçimde sürüklenmesini ekler.","collision":"Olayların yönünün değişmesi ile insanın olaylara kapılması birbirine karışır.","fit":"displacement","loses":"Dönemin değişimleri ile olayların seyrinin yön değiştirmesi arasındaki bağı zayıflatır.","preserves":"Olayların yön verici bir etkisi olduğu düşüncesini korur."},"text":"insanı sürükleyen olaylar"}],"identity_rationale":"Kaynak ifadesi dönemin değişimlerini ve olayların yönünü değiştirmelerini anlatır. Hazırlanan çerçevenin olaylar ve yön verme bölümü uygundur, ancak insanın bu olaylara eğilmesi kaynakta kurucu bir katılımcı olarak açıkça verilmez.","lexical_glosses":[{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"dönemin değişimleri ve getirdiği olaylar"}],"lexicalization_note":"Anlam yalnızca dönemin yön verici değişimleri yapısına bağlıdır; yalın biçime genel bir olay veya çağırma anlamı yüklenmez.","neighbor_coverage_note":"Adayların tümü karşılaştırıldı. İki yakın komşu, yön verici dönem değişimini genel dönem olaylarından ve kaygı uyandıran gelişmelerden ayırır; diğer adaylar ölüm, insanın durumu, yaklaşan sonuç veya kardeş anlamlarla daha dolaylı ilişkilidir.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yön verme benzetisiyle sınırlıdır; komşu dal daha genel olayları ve daha geniş zamansal kullanımları kapsar.","focus_only":"Dönemin değişimlerini olayların yönünü etkileyen bir güç olarak kavramlaştırır.","gloss":"dönemin değişimleri ve başa gelenler","neighbor_only":"Dönemin insanlar üzerinde gerçekleşen türlü olaylarını ve bazı kullanımlarda gece ile gündüzü de kapsar.","neighbor_ref":"root_000860/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da dönem içinde ortaya çıkan değişimleri ve olayların değişken seyrini anlatır."},{"boundary_match":"partial","distinction":"Bu dal genel yön değişimini anlatır; komşu dal değişimlerin kaygı, kuşku ve kötü beklenti doğuran yönüyle sınırlıdır.","focus_only":"Değişimleri, olumlu veya olumsuz değer yüklemeden olayların yönünü değiştirmeleri bakımından ele alır.","gloss":"kaygı uyandıran dönem olayları","neighbor_only":"Beklenen veya korkulan uğursuz gelişmeler ve belirsizlik duygusunu öne çıkarır.","neighbor_ref":"root_000616/B002","relation_type":"near_synonym","shared_zone":"İki dal da dönemin getirdiği değişimleri ve beklenmedik gelişmeleri kapsar."}],"source_phrase_ar":"دواعي الدهر صروفه كأنها تميل الحوادث","source_summary":"Tek iddia, dönemin değişimlerini olayların yönünü etkileyen güçler olarak sunar; insanın bu değişimlere çekilmesi kaynak ifadesinde zorunlu bir öğe değildir.","sources":["MQ"],"what_is_ar":"صروف الدهر وحوادثه التي تميل الإنسان إليها","what_is_not_ar":"ليس دعاء الصوت ولا ادعاء النسب ولا تداعي الحيطان"},"support_links":[]},{"boundary":"Dal sıradan anlaşılmaz sözü değil, gizlenmiş bir cevabı buldurmak üzere yöneltilen bilmece ve sınama eylemini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000478/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"gizli cevabı buldurmaya yönelik bilmeceleşme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Soru, cevabı doğrudan vermeyip onu örtülü ve çözülmesi gereken halde sunar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişiler bu tür soruları birbirlerine yönelterek karşılıklı bir sınama yürütür."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Eylem biçimi, muhataba bir bilmece sunup gizli cevabı ondan istemeyi anlatır."}}],"root_ar":"د ع ع","root_id":"root_000478","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Örtülü bir cevabı ortaya çıkarmak için kişilerin birbirine bilmece türü soru yönelttiği kavramı karşılar.","boundary_detail":"Dal sıradan anlaşılmaz sözü değil, gizlenmiş bir cevabı buldurmak üzere yöneltilen bilmece ve sınama eylemini kapsar.","branch_image_ar":"الأُدْعِيّة المعماة","concept_gloss":"gizli cevabı buldurmaya yönelik bilmeceleşme","contextual_glosses":[{"applicability":"Bir kişinin muhatabına örtülü cevabı bulması için soru yönelttiği eylem bağlamında doğaldır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Soruların karşılıklı yürütülmesini ve cevabı özellikle ortaya çıkarma benzetisini tek başına göstermez.","preserves":"Birine çözülmesi gereken örtülü bir soru yöneltme eylemini korur."},"facet_ids":["F001","F003"],"text":"bilmece sormak","usage_role":"contextual"},{"applicability":"Kişilerin birbirine örtülü sorular yönelterek cevap verme gücünü denediği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gizlenmiş cevabı muhataptan ortaya çıkarma yönünü açıkça söylemez.","preserves":"Karşılıklılığı, bilmece biçimini ve sınama işlevini korur."},"facet_ids":["F001","F002"],"text":"bilmeceyle karşılıklı sınamak","usage_role":"explanatory"}],"definition":"Gizlenmiş bir cevabı ortaya çıkarmak için birine yöneltilen bilmece türü soru veya böyle sorularla karşılıklı sınamadır. Soru, muhatabı örtülü cevabı bulup söylemeye çağırır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Soru, cevabı doğrudan vermeyip onu örtülü ve çözülmesi gereken halde sunar."},{"facet_id":"F002","role":"associated_use","statement":"Kişiler bu tür soruları birbirlerine yönelterek karşılıklı bir sınama yürütür."},{"facet_id":"F003","role":"specialization","statement":"Eylem biçimi, muhataba bir bilmece sunup gizli cevabı ondan istemeyi anlatır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Cevabı olmayan her türlü belirsiz veya bozuk sözü kapsayabilir.","collision":"Amaçlı bilmeceyi rastgele anlaşılmaz anlatımla karıştırır.","fit":"displacement","loses":"Soru biçimini, gizli cevabı buldurma amacını ve karşılıklı sınamayı kaybeder.","preserves":"İçeriğin hemen anlaşılmaması ve çözüm gerektirmesi yönünü kısmen korur."},"text":"anlaşılmaz söz"}],"identity_rationale":"Kaynak ifadesi, gizlenmiş cevabı ortaya çıkarmak için karşılıklı olarak sorulan bilmece türü soruları ve birine böyle bir soru yöneltme eylemini birlikte verir. Hazırlanan çerçeve bu soru, gizleme ve cevap çıkarma ilişkisini korur.","lexical_glosses":[{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"gizli cevabı buldurmak için karşılıklı sorulan bilmeceler"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"sana bir bilmece sorayım"}],"lexicalization_note":"Bilmece olarak kullanılan adlandırma ile birine bilmece yöneltme eylemi ayrı facetlerde korunur; anlam genel seslenmeye yayılmaz.","neighbor_coverage_note":"Tüm adaylar incelendi. Seçilen iki komşu bilmeceyi genel anlaşılmazlaştırmadan ve cevapsız kalma sonucundan ayırır; kalan adaylar doğrulama, bilgi, çelişki, karşı koyma veya kardeş anlamlarla yalnızca uzak bağ taşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal amaçlı bir bilmece ve cevap isteme eylemidir; komşu dal daha geniş biçimde sözü anlaşılmazlaştırmayı anlatır.","focus_only":"Örtülü soruyu bir muhataba yöneltir ve ondan gizli cevabı ortaya çıkarmasını ister.","gloss":"sözü anlaşılması güç kılma","neighbor_only":"Sözü veya nesneyi genel olarak anlaşılması güç hale getirmeyi, soru ve cevap düzeni aramadan kapsar.","neighbor_ref":"root_001070/B005","relation_type":"near_synonym","shared_zone":"Her iki dal da anlamı hemen erişilemez kılan örtme ve çözme gereksinimini taşır."},{"boundary_match":"thematic_only","distinction":"Bu dal soruyu yönelten sınama eylemidir; komşu dal ise sınanan kişinin cevapsız kalmasının sonucudur.","focus_only":"Muhatabı güç bir soruyla cevap vermeye ve örtülü çözümü bulmaya yöneltir.","gloss":"cevap bulamayınca susma","neighbor_only":"Kişinin cevap bulamadığı veya sözü tükendiği için susmasını anlatır.","neighbor_ref":"root_000149/B003","relation_type":"thematic","shared_zone":"İki dal, zor bir söz karşısında cevap verme veya cevap verememe sahnesinde birleşir."}],"source_phrase_ar":"لبنى فلان أدعية يتداعون بها وهي مثل الأغلوطة كأنه يدعو المسؤول إلى إخراج ما يعميه عليه","source_summary":"Tek iddia, bilmece niteliğindeki örtülü soruyu, bu sorularla karşılıklı sınamayı ve muhataptan gizli cevabı çıkarma amacını birlikte temellendirir.","sources":["MQ"],"what_is_ar":"الأُدْعِيّة التي يتداعون بها مثل الأغلوطة لإخراج الجواب المعمى","what_is_not_ar":"ليس دعاء العبادة ولا دعوة الطعام ولا ادعاء النسب"},"support_links":[]},{"boundary":"Anlam belirli olumsuz ev ifadesine bağlıdır ve genel olarak boşluk, sessizlik veya eşyasızlık bildirmez.","branch_kind":"non_bare","branch_ref":"root_000478/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","surface_ar":"يَدُعُّ"}],"gloss":"evde hiç kimsenin bulunmaması","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirtilen evde hiçbir insan bulunmaz."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan yokluğu, evde seslenebilecek veya bağırabilecek kimsenin bulunmamasıyla açıklanır."}}],"root_ar":"د ع ع","root_id":"root_000478","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli yapının bir evde tek bir insanın bile bulunmadığını bildiren tam anlamı için uygundur.","boundary_detail":"Anlam belirli olumsuz ev ifadesine bağlıdır ve genel olarak boşluk, sessizlik veya eşyasızlık bildirmez.","branch_image_ar":"خلو الدار من داع","concept_gloss":"evde hiç kimsenin bulunmaması","contextual_glosses":[{"applicability":"Güncel Türkçede evde hiçbir insan bulunmadığını doğal ve doğrudan biçimde bildirir.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Seslenip bağıracak birinin bile olmayışı üzerinden kurulan açıklayıcı benzetiyi göstermez.","preserves":"Evde hiçbir insanın bulunmadığı temel sonucu eksiksiz korur."},"facet_ids":["F001"],"text":"evde kimse yok","usage_role":"general"}],"definition":"Belirli bir olumsuz ev ifadesinde, içeride hiç kimsenin bulunmadığını bildirir. Açıklayıcı benzetme, seslenip bağıracak tek bir kişinin bile olmayışıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirtilen evde hiçbir insan bulunmaz."},{"facet_id":"F002","role":"extension","statement":"İnsan yokluğu, evde seslenebilecek veya bağırabilecek kimsenin bulunmamasıyla açıklanır."}],"excluded_glosses":[{"category":"confusable","error_profile":{"adds":"Eşya, kullanım veya yaşam belirtisi bulunmadığı anlamlarını da ekleyebilir.","collision":"İnsan yokluğunu evin eşyasız ya da kullanılmıyor olmasıyla karıştırır.","fit":"displacement","loses":"İfadenin yalnızca insan bulunmadığını kesin biçimde bildiren sınırını kaybeder.","preserves":"Evde insan bulunmaması olasılığını ve genel yokluk düşüncesini korur."},"text":"boş ev"}],"identity_rationale":"Kaynak ifadesi, belirli bir ev yapısında hiç kimsenin bulunmadığını, seslenebilecek tek bir kişinin bile olmaması üzerinden açıklar. Hazırlanan dal çerçevesi hem yokluk sonucunu hem de ses veren kimse benzetisini korur.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"evde hiç kimse yok"}],"lexicalization_note":"Hiç kimsenin bulunmadığı anlamı yalnızca verilen kalıplaşmış olumsuz yapıda geçerlidir; yalın biçime taşınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi. İki tam eşdeğer ve iki yakın komşu, evde insan yokluğunu başka kalıplaşmış yokluk ifadeleriyle karşılaştırır; diğer adaylar ikamet, ıssızlık, sessizlik, hazır bulunan topluluk veya kardeş anlamlar nedeniyle daha uzaktır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Kavramsal çekirdek ve sınır aynıdır; ayrım yalnızca bu anlamı taşıyan kalıplaşmış sözlerin farklı oluşudur.","focus_only":null,"gloss":"evde hiç kimse bulunmaması","neighbor_only":null,"neighbor_ref":"root_001617/B004","relation_type":"synonym","shared_zone":"Her iki dal da kalıplaşmış olumsuz bir ev ifadesiyle içeride tek bir kişinin bile bulunmadığını bildirir."},{"boundary_match":"exact","distinction":"Anlam ve kullanım sınırı örtüşür; yalnızca insan yokluğunu anlatmak için seçilen sözlü görüntü farklıdır.","focus_only":null,"gloss":"evde tek kişinin bile olmaması","neighbor_only":null,"neighbor_ref":"root_001529/B005","relation_type":"synonym","shared_zone":"İki dal da belirli bir evde hiçbir insan bulunmadığını kalıplaşmış olumsuz sözle anlatır."},{"boundary_match":"partial","distinction":"Odak dal ev ve seslenen kişi görüntüsüne bağlıdır; komşu dalın yer sınırı daha geneldir ve aynı açıklayıcı görüntüyü taşımaz.","focus_only":"İnsan yokluğunu evle sınırlı özel bir ifade ve seslenebilecek kimse benzetisiyle kurar.","gloss":"bir yerde hiç kimsenin olmaması","neighbor_only":"İnsan yokluğunu ev dışındaki bir yer için de kullanılabilen başka bir dar ifadeyle bildirir.","neighbor_ref":"root_000955/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da belirli bir yerde tek bir insanın bile bulunmadığını bildirir."},{"boundary_match":"partial","distinction":"Bu dal yalnızca evde insan yokluğudur; komşu dal yer sınırını genişletir ve insan dışında belirti yokluğuna da uzanabilir.","focus_only":"Belirli bir evde insan bulunmamasını ses verecek kimsenin yokluğuyla açıklar.","gloss":"mekanda insan veya belirti bulunmaması","neighbor_only":"Bir yerde hiç kimse veya hiçbir belirti bulunmamasını daha geniş bir yokluk alanında kapsayabilir.","neighbor_ref":"root_000075/B008","relation_type":"near_synonym","shared_zone":"İki dal da bir mekanın insanlardan yoksun oluşunu kalıplaşmış olumsuz ifadelerle bildirir."}],"source_phrase_ar":"ما بالدار دَعْوِيّ أي ما بها أحد كأنه ليس بها صائح يدعو بصياحه","source_summary":"Tek iddia, belirli olumsuz yapıdaki insan yokluğu anlamını, evde ses çıkarıp çağırabilecek kimsenin bulunmaması benzetisiyle açıklar.","sources":["MQ"],"what_is_ar":"نفي وجود أحد في الدار بقولهم ما بالدار دَعْوِيّ","what_is_not_ar":"ليس دعوة الطعام ولا ادعاء النسب ولا تداعي السقوط"},"support_links":[]},{"boundary":"İnsan çocuğu için baba kaybı ve ergenlik sınırı, hayvan yavrusu için anne kaybı esastır; genel yalnızlık bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B001","candidate_links":[{"candidate_id":"cand_da7fd8da1d0930765c71","lane":"micro"},{"candidate_id":"cand_09657578babde7b517f4","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:2:4:2","qac_word_ref":"107:2:4","surface_ar":"يَتِيمَ"}],"gloss":"babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu olma","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsanlarda durum, bir çocuğun ergenliğe ulaşmadan babasını yitirmesiyle oluşur."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İnsan dışındaki hayvanlarda karşılık gelen durum, yavrunun annesini yitirmesidir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Türemiş eylemler, bir çocuğu babasız bırakmayı veya çocukları topluca bu duruma düşürmeyi anlatır."}},{"facet_id":"F004","role":"associated_use","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Bazı türemiş kadın adları, çocukları babasız kalmış olan anneyi niteler."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve hayvan için farklı ebeveyn koşullarını birlikte belirtmek gereken genel açıklamada kullanılır.","boundary_detail":"İnsan çocuğu için baba kaybı ve ergenlik sınırı, hayvan yavrusu için anne kaybı esastır; genel yalnızlık bu dala girmez.","branch_image_ar":"انقطاع الولد عن كافله","concept_gloss":"babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu olma","contextual_glosses":[{"applicability":"Ergenliğe ulaşmadan babası ölen bir insan çocuğundan söz edilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan çocuğunu ve belirleyici baba kaybını açık biçimde korur."},"facet_ids":["F001"],"text":"babasını yitirmiş çocuk","usage_role":"contextual"},{"applicability":"İnsan dışındaki bir hayvanın annesini yitirmiş yavrusundan söz edilen bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Hayvan yavrusunu ve belirleyici anne kaybını açık biçimde korur."},"facet_ids":["F002"],"text":"annesini yitirmiş hayvan yavrusu","usage_role":"contextual"}],"definition":"İnsanlarda ergenliğe ulaşmadan babasını yitirmiş çocuk olma, öteki hayvanlarda ise annesini yitirmiş yavru olma durumudur. Bir çocuğu bu duruma düşürme ve çocukları babasız kalan kadını niteleme gibi türev kullanımlar bu çekirdeğe bağlıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsanlarda durum, bir çocuğun ergenliğe ulaşmadan babasını yitirmesiyle oluşur."},{"facet_id":"F002","role":"specialization","statement":"İnsan dışındaki hayvanlarda karşılık gelen durum, yavrunun annesini yitirmesidir."},{"facet_id":"F003","role":"extension","statement":"Türemiş eylemler, bir çocuğu babasız bırakmayı veya çocukları topluca bu duruma düşürmeyi anlatır."},{"facet_id":"F004","role":"associated_use","statement":"Bazı türemiş kadın adları, çocukları babasız kalmış olan anneyi niteler."}],"identity_rationale":"Kaynak ifadesi genel olarak bakımı üstlenen kişiden ayrılmayı değil, insan çocuğunda ergenlikten önce babanın, öteki hayvanlarda ise annenin ölümünü belirleyici sayar. Bu nedenle dal, bu iki katılımcı ayrımı açıkça korunarak tanımlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"insanda babasız, hayvanda annesiz kalma"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuk veya annesini yitirmiş hayvan yavrusu"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"çocuk babasını yitirip babasız kaldı"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"Tanrı onu babasız bıraktı"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"çocukları babasız bıraktı"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuklar"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuklar"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"çocukları babasız kalmış kadın"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"çocukları babasız kalmış kadın"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"onları babasız bıraktı"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"çocukken kendisini yetiştiren kişiye nispetle, büyüdüğünde de babasını yitirmiş çocuk diye anılan kişi"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"babasını yitirmiş çocuklar topluluğu"}],"lexicalization_note":"Tanım, yalın durum ve kişi adlandırmalarını temel alır; çocukları babasız kalan kadın ile büyüdükten sonra da sürdürülen adlandırma yalnız kendi kalıpları içinde tutulur.","neighbor_coverage_note":"Sunulan bütün komşu adaylar değerlendirildi; ebeveyn ölümü, bırakılma, bakım bağı ve tek kalma arasındaki sınırı en açık gösteren üç karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ölümden doğan ve türe göre baba ya da anne üzerinden tanımlanan statüdür; komşu dal ise ölüm gerektirmeyen bırakılma ve bulunma olayını anlatır.","focus_only":"Odak dalda ebeveynin ölümü, insan ve hayvan için ayrı ebeveyn rolleriyle belirleyicidir.","gloss":"ebeveynini yitirmiş yavru ile bırakılmış çocuk","neighbor_only":"Komşu dalda çocuk annesi tarafından bırakılır ve başka biri tarafından bulunur.","neighbor_ref":"root_001466/B007","relation_type":"near_neighbor","shared_zone":"Her ikisi de bir çocuğun veya yavrunun doğal ebeveyn bakımından yoksun kalabildiği durumları anlatır."},{"boundary_match":"field_only","distinction":"Bakıma muhtaçlık odak dalın tanımı değildir ve her bakmakla yükümlü olunan kişi ebeveynini yitirmiş değildir.","focus_only":"Odak dal, insan çocuğunda baba ve hayvan yavrusunda anne ölümüyle sınırlı bir durumdur.","gloss":"ebeveyn kaybı ile bakıma muhtaç olma","neighbor_only":"Komşu dal bakmakla yükümlü olunanları, yük sayılan kişileri ve çocuğu olmayanları da kapsar.","neighbor_ref":"root_001315/B002","relation_type":"same_field","shared_zone":"İki dal da başkasının bakımına veya desteğine ihtiyaç duyan kişilerin alanına değebilir."},{"boundary_match":"partial","distinction":"Odak dalın koşulları ebeveyn türü ve insanlarda ergenlik sınırıyla belirlenir; komşu dal bu koşulları taşımaz ve nadir nesnelere de uygulanır.","focus_only":"Odak dal canlılarda belirli bir ebeveynin ölümüne bağlı statüyü bildirir.","gloss":"ebeveyn kaybı ile tek kalma","neighbor_only":"Komşu dal canlı ya da cansız herhangi bir şeyin tek kalmasını veya benzerinin zor bulunmasını bildirir.","neighbor_ref":"root_001692/B002","relation_type":"near_neighbor","shared_zone":"Her iki dalda da önceki bir bağdan veya eşlikten yoksun kalma düşüncesi bulunabilir."}],"source_phrase_ar":"اليتم في الناس من قبل الأب وفي سائر الحيوان من جهة الأم (maqayis)؛ يتم الصبي إذا صار يتيما وأيتمه الله (jamhara)؛ أيتمت المرأة فهي موتم (jamhara;sihah)؛ يتمهم الله تيتيما (sihah)؛ اليتيم الذي مات أبوه حتى يبلغ (tahdhib)؛ انقطاع الصبي عن أبيه قبل بلوغه وفي سائر الحيوانات من قبل أمه (mufradat)","source_summary":"Kanıt bütünü, insan çocuğunda baba kaybını, hayvan yavrusunda anne kaybını ve bu durumla ilgili türemiş biçimleri verir. Ergenlik sınırı bazı aktarımlarda açıkça belirtilir; ettirgen ve topluluk bildiren biçimler ayrı tanıklamalar olarak bu çekirdeğe bağlanır.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه الصبي الذي مات أبوه قبل بلوغه، والبهيمة التي ماتت أمها، وجعل الأولاد أيتاما","what_is_not_ar":"ليس مجرد الانفراد في الأشياء النفيسة ولا الإبطاء في السير ولا الغفلة والتقصير"},"support_links":["sup_1aa923127a6d0edd8b45","sup_75c1600008d8b8b83ff4"]},{"boundary":"Dal, ebeveyn kaybını değil tekliği veya benzer azlığını anlatır; değerli nesne ve şiir örnekleri çekirdeğin kendisi değildir.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B002","candidate_links":[{"candidate_id":"cand_ceecaf70ededba2ca837","lane":"micro"},{"candidate_id":"cand_b6e61ee9d293635a85e0","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:2:4:2","qac_word_ref":"107:2:4","surface_ar":"يَتِيمَ"}],"gloss":"tek kalmış ya da benzeri zor bulunan şey","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Canlı ya da cansız bir varlık, başka bir eşlikçi olmadan tek başına bulunduğunda bu nitelemeyi alabilir."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Niteleme, benzeri veya dengi zor bulunan seçkin bir varlığa da uygulanabilir."}},{"facet_id":"F003","role":"example","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tek başına duran şiir dizesi, eşi zor bulunan inci ve ayrı kumluk kaynaklarda örneklenir."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Tek başına bulunma ile eşine az rastlanma kapsamlarının ikisini de taşıyan genel niteleme için kullanılır.","boundary_detail":"Dal, ebeveyn kaybını değil tekliği veya benzer azlığını anlatır; değerli nesne ve şiir örnekleri çekirdeğin kendisi değildir.","branch_image_ar":"انفراد الشيء وانقطاع نظيره","concept_gloss":"tek kalmış ya da benzeri zor bulunan şey","contextual_glosses":[{"applicability":"Varlığın eşlikçisiz veya çevresindekilerden ayrı bulunmasının öne çıktığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Varlığın başka bir eşlikçi olmadan tek kalması özelliğini korur."},"facet_ids":["F001"],"text":"tek başına kalmış","usage_role":"contextual"},{"applicability":"Bir nesnenin veya söz ürününün benzerinin az bulunması vurgulandığında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Benzer azlığını ve bundan doğan eşsizlik niteliğini korur."},"facet_ids":["F002"],"text":"eşi zor bulunan","usage_role":"contextual"}],"definition":"Bir varlığın tek başına kalması veya benzerinin zor bulunmasıdır; şiir dizesi, inci ve tek başına duran kumluk bu niteliğin özel örnekleridir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Canlı ya da cansız bir varlık, başka bir eşlikçi olmadan tek başına bulunduğunda bu nitelemeyi alabilir."},{"facet_id":"F002","role":"extension","statement":"Niteleme, benzeri veya dengi zor bulunan seçkin bir varlığa da uygulanabilir."},{"facet_id":"F003","role":"example","statement":"Tek başına duran şiir dizesi, eşi zor bulunan inci ve ayrı kumluk kaynaklarda örneklenir."}],"identity_rationale":"Kaynak ifadesi, tek başına kalan şeyi ve benzeri zor bulunan şeyi aynı dalda açıkça toplar; şiir dizesi, inci ve tek kumluk bu çekirdeğin örnekleridir. Geçici çerçeve bu kapsamı doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"tek başına veya eşi zor bulunan"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"tek başına duran veya benzeri olmayan şiir dizesi"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"tek ve eşi zor bulunan inci"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"tek başına duran kumluk veya dişil varlık"}],"lexicalization_note":"Yalın niteleme tekliği veya benzer azlığını bildirir; şiir dizesi ve inci okumaları yalnız tanıklanmış ad öbeklerinin özel uygulamalarıdır.","neighbor_coverage_note":"Bütün adaylar incelendi; genel teklik, nadirlik, belirli bir nitelikte rakipsizlik ve ebeveyn kaybı ile en güçlü sınırları kuran dört aday seçildi.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal tek kalmayı benzer azlığına kadar genişletirken komşu dal sayısal birlik ve tekleştirme işlemlerine de uzanır; bu yüzden kapsamları bütünüyle örtüşmez.","focus_only":"Odak dal, benzeri zor bulunan nesne ile şiir dizesi ve inci gibi kalıplaşmış uygulamaları özellikle kapsar.","gloss":"tek kalmış ve bir olan","neighbor_only":"Komşu dal bir olma, teklik, birer birer gelme ve tek başına gönderme gibi daha geniş işlemleri de kapsar.","neighbor_ref":"root_001141/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir varlığın tek başına ve eşlikçisiz bulunmasını doğrudan anlatabilir."},{"boundary_match":"partial","distinction":"Odak dalın çekirdeği tek kalmadır; komşu dalın çekirdeği ise kıtlık ve erişim güçlüğüdür, dolayısıyla yalnızlığın kendisini gerektirmez.","focus_only":"Odak dalda tek başına bulunma yeterlidir ve erişim güçlüğü gerekli değildir.","gloss":"eşi zor bulunan ile nadir ve güç erişilen","neighbor_only":"Komşu dal az bulunmanın yanında bir şeye erişmenin veya benzerini bulmanın güçlüğünü bildirir.","neighbor_ref":"root_001008/B003","relation_type":"near_neighbor","shared_zone":"Benzeri az bulunan bir nesne iki dalın kapsamına da girebilir."},{"boundary_match":"partial","distinction":"Komşu dal belirli insani niteliklerle sınırlı bir üstünlük veya uçluk bildirirken odak dal tek başına bulunmayı da kapsayan daha genel bir nesne niteliğidir.","focus_only":"Odak dal her tür canlı veya cansız varlığın tekliğine ve benzer azlığına uygulanabilir.","gloss":"genel eşsizlik ile bir nitelikte rakipsizlik","neighbor_only":"Komşu dal cömertlik, erdem, iyilik ya da kötülük gibi belirli değerlendirme alanlarında dengi olmayan kişiyi niteler.","neighbor_ref":"root_001240/B018","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir varlığın belli bakımdan denginin bulunmamasını anlatabilir."},{"boundary_match":"partial","distinction":"Bu çağrışım iki dalı özdeş kılmaz; odak dal genel teklik ve eşsizlik, komşu dal ise canlılara özgü ve koşulları belirli bir ebeveyn kaybı statüsüdür.","focus_only":"Odak dal ebeveyn ölümü olmadan da tek kalan veya benzeri az bulunan her şeye uygulanabilir.","gloss":"tek kalma ile ebeveynini yitirme","neighbor_only":"Komşu dal insan çocuğunda baba, hayvan yavrusunda anne ölümünü ve insan için ergenlik sınırını gerektirir.","neighbor_ref":"root_001692/B001","relation_type":"near_neighbor","shared_zone":"Ebeveynini yitiren çocuk veya yavru, tek kalma düşüncesiyle ilişkilendirilebilir."}],"source_phrase_ar":"لكل منفرد يتيم وبيت من الشعر يتيم (maqayis)؛ اليتيم الفرد (jamhara)؛ كل شيء مفرد يعز نظيره فهو يتيم ودرة يتيمة (sihah)؛ الرملة المنفردة وكل منفرد ومنفردة يتيم ويتيمة (tahdhib)؛ كل منفرد يتيم ودرة يتيمة وبيت يتيم (mufradat)","source_summary":"Kaynaklar tek kalma anlamında birleşir ve bir şeyin benzerinin az bulunmasını buna bağlı bir kapsam olarak verir. Şiir dizesi, inci ve kumluk bu ortak anlamı görünür kılan örneklerdir.","sources":["MQ","JA","SI","TA","MU"],"what_is_ar":"يدخل فيه كل منفرد أو منفردة، وما عز نظيره كالدرة اليتيمة وبيت الشعر اليتيم والرملة المنفردة","what_is_not_ar":"ليس خصوص موت الأب عن الصبي ولا موت الأم عن البهيمة ولا الإبطاء في السير"},"support_links":["sup_16ff0b02a06e911120e2","sup_409ffd3e1031524f93aa"]},{"boundary":"Buradaki anlam zihinsel dikkatsizlik ile görevde eksik bırakmayı birlikte kapsar; salt yavaşlama ayrı daldadır.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B003","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:2:4:2","qac_word_ref":"107:2:4","surface_ar":"يَتِيمَ"}],"gloss":"dalgınlık ve gerekeni eksik yapma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Anlam, dikkat göstermeme ile bir işi veya yükümlülüğü gerektiği kadar yerine getirmemeyi birlikte kapsar."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Yol alış hakkında kullanılan olumsuz kalıp, gidişte dalgınlık veya eksik davranış bulunmadığını bildirir."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dikkat eksikliği ile görevde yetersiz kalmanın birlikte anlatıldığı genel bağlamlarda kullanılır.","boundary_detail":"Buradaki anlam zihinsel dikkatsizlik ile görevde eksik bırakmayı birlikte kapsar; salt yavaşlama ayrı daldadır.","branch_image_ar":"غفلة وتقصير","concept_gloss":"dalgınlık ve gerekeni eksik yapma","contextual_glosses":[{"applicability":"Bir kişinin yol alışında dikkatsizlik veya kusurlu davranış bulunmadığını söyleyen tanıklanmış kalıpta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Olumsuzluğu, yol alış bağlamını ve iki kusurun yokluğunu korur."},"facet_ids":["F002"],"text":"gidişinde dalgınlık veya eksiklik yok","usage_role":"contextual"}],"definition":"Bir şeyi yeterince gözetmeyerek dalgın davranma ve yapılması gerekeni eksik bırakmadır; yol alışa ilişkin kalıpta bu özelliklerin bulunmadığı söylenir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Anlam, dikkat göstermeme ile bir işi veya yükümlülüğü gerektiği kadar yerine getirmemeyi birlikte kapsar."},{"facet_id":"F002","role":"associated_use","statement":"Yol alış hakkında kullanılan olumsuz kalıp, gidişte dalgınlık veya eksik davranış bulunmadığını bildirir."}],"identity_rationale":"Kaynak ifadesi dalı açıkça dalgınlık ve gerekeni eksik yapma olarak tanımlar; yol alış kalıbı da bu iki niteliğin bulunmadığını söyleyen bir uygulamadır. Geçici çerçeve kaynakla uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"dalgınlık ve gerekeni eksik yapma"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"gidişinde dalgınlık veya eksik davranış yok"}],"lexicalization_note":"Yalın biçim dalgınlık ve eksik davranmayı anlatır; yol alışa ilişkin olumsuz okuma yalnız tanıklanmış cümle kalıbının kapsamındadır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; dikkatsizlik, savsaklama, mazeretli eksiklik ve yavaşlama arasındaki ayrımları en iyi gösteren dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal dikkatsizlik ile kusuru birleştirir; komşu dal ise bilinçli oyalanma, tembellik ve güçsüz değerlendirme gibi nedenleri de kapsar.","focus_only":"Odak dal dalgınlığı ve eksik yapmayı yalın bir anlam olarak, ayrıca yol alış kalıbındaki olumsuz uygulamayla verir.","gloss":"dalgınlık ve eksik yapma ile savsaklama","neighbor_only":"Komşu dal işi savsaklama, oyalanma, tembellikten yatma ve görüş zayıflığı gibi daha geniş davranışları kapsar.","neighbor_ref":"root_000902/B003","relation_type":"near_synonym","shared_zone":"İki dal da kişinin üstlendiği işi yeterince yerine getirmemesini anlatabilir."},{"boundary_match":"partial","distinction":"Komşu dal dikkat dışına çıkma olayında yoğunlaşır; odak dal ise bunun yanında görev veya davranıştaki yetersizliği de kurucu sayar.","focus_only":"Odak dal dikkat eksikliğinin yanında yapılması gerekeni eksik bırakmayı da doğrudan içerir.","gloss":"dalgınlık ve eksik yapma ile gözden kaçırma","neighbor_only":"Komşu dal bir şeyi uyanıklık ve koruma azlığından dolayı unutma veya gözden kaçırma yönünü öne çıkarır.","neighbor_ref":"root_001097/B001","relation_type":"near_synonym","shared_zone":"Her iki dalın ortak alanı, yeterli dikkat göstermemektir."},{"boundary_match":"partial","distinction":"Odak dal dikkatsizlik ve eksikliktir; komşu dal ise eksikliği mazeret gösterme tavrıyla birlikte tanımlar.","focus_only":"Odak dalda sahte mazeret gösterme veya kendini haklı çıkarma koşulu yoktur.","gloss":"eksik yapma ile mazeretli savsaklama","neighbor_only":"Komşu dal eksik davranışa gerçek olmayan bir mazeret gösterme veya özür görüntüsü verme boyutunu ekler.","neighbor_ref":"root_000995/B005","relation_type":"near_neighbor","shared_zone":"İki dal da bir işin gerektiği gibi yerine getirilmemesini kapsayabilir."},{"boundary_match":"partial","distinction":"Ortak kalıp anlam özdeşliği yaratmaz; bu dal davranış kusurunu, komşu dal ise hızın düşmesini veya gecikmeyi anlatır.","focus_only":"Odak dal dikkatsizlik ve gerekeni eksik yapma kusurlarını bildirir.","gloss":"dikkatsizlik ile yavaşlama","neighbor_only":"Komşu dal hareketin veya yol alışın ağırlaşmasını ve iyiliğin gecikmesini bildirir.","neighbor_ref":"root_001692/B004","relation_type":"near_neighbor","shared_zone":"Aynı yol alış ifadesi kaynaklarda iki ayrı yorumun bağlamı olabilir."}],"source_phrase_ar":"اليتم الغفلة والتقصير وما في سيره يتم أي ما فيه غفلة ولا تقصير (jamhara)؛ أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره (tahdhib)","source_summary":"Kaynakların ortak alanı dalgınlıktır. Eksik davranma ve yol alışta dalgınlık ya da eksiklik bulunmadığını bildiren kalıp, bunları açıkça birlikte veren aktarımın ek ayrıntılarıdır.","sources":["JA","TA"],"what_is_ar":"يدخل فيه اليتم بمعنى الغفلة والتقصير، وما نفي عن السير في قولهم ما في سيره يتم عند من فسره بذلك","what_is_not_ar":"ليس اليتم بمعنى اليتيم الذي مات أبوه ولا الانفراد النفيس ولا الإبطاء الخالص"},"support_links":[]},{"boundary":"Çekirdek hareketin ağırlaşması veya gecikmesidir; çocuğa iyiliğin geç ulaşması yalnız açıklayıcı bir bağlantıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_001692/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:2:4:2","qac_word_ref":"107:2:4","surface_ar":"يَتِيمَ"}],"gloss":"yavaşlama veya gecikme","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Temel anlam, hareketin olağan hızından daha ağır ilerlemesi veya gecikmesidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tanıklanmış yol alış kalıbında, bir kimsenin gidişinde yavaşlama bulunduğu anlatılır."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Babasını yitirmiş çocuğa iyiliğin geç ulaşması, ebeveyn kaybı adlandırmasıyla kurulan açıklayıcı bağ olarak verilir."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Hareketin ya da ilerleyişin olağan hızından daha ağır sürmesini anlatan genel bağlamlarda kullanılır.","boundary_detail":"Çekirdek hareketin ağırlaşması veya gecikmesidir; çocuğa iyiliğin geç ulaşması yalnız açıklayıcı bir bağlantıdır.","branch_image_ar":"إبطاء السير والبر","concept_gloss":"yavaşlama veya gecikme","contextual_glosses":[{"applicability":"Tanıklanmış yol alış kalıbında kişinin ilerleyişinin ağır olduğunu belirtmek için kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yol alış bağlamını ve hareket hızının düşmesini açıkça korur."},"facet_ids":["F002"],"text":"gidişinde yavaşlama var","usage_role":"contextual"},{"applicability":"Babasını yitirmiş çocuğa gösterilen iyiliğin gecikmesini adlandırma gerekçesi olarak açıklarken kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İyilik alanını, gecikmeyi ve açıklayıcı bağlantının yönünü korur."},"facet_ids":["F003"],"text":"iyiliğin geç ulaşması","usage_role":"explanatory"}],"definition":"Bir şeyin yavaşlaması veya gecikmesidir. Yol alışın ağırlaşması bunun özel uygulamasıdır; babasını yitirmiş çocuğa iyiliğin geç ulaşması ise açıklayıcı bir bağlantıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Temel anlam, hareketin olağan hızından daha ağır ilerlemesi veya gecikmesidir."},{"facet_id":"F002","role":"specialization","statement":"Tanıklanmış yol alış kalıbında, bir kimsenin gidişinde yavaşlama bulunduğu anlatılır."},{"facet_id":"F003","role":"associated_use","statement":"Babasını yitirmiş çocuğa iyiliğin geç ulaşması, ebeveyn kaybı adlandırmasıyla kurulan açıklayıcı bağ olarak verilir."}],"identity_rationale":"Kaynak ifadesi yavaşlama anlamını ve yol alış uygulamasını doğrudan destekler; babasını yitirmiş çocuğa iyiliğin geç ulaşması ise adlandırmayı açıklayan bağımlı bir gerekçedir. Bu açıklama çekirdekle eş düzeye çıkarılmadan dal korunabilir.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"gidişinde yavaşlama var"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"yavaşlama ve gecikme"}],"lexicalization_note":"Yalın biçim yavaşlama anlamını taşır; yol alış okuması kendi kalıbında tutulur ve iyiliğin geç ulaşması bağımsız bir yalın anlam sayılmaz.","neighbor_coverage_note":"Bütün adaylar incelendi; çaba eksikliği, güçten düşme, isteksiz ağırlaşma ve dikkatsizlikten ayrımı en belirgin dört komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal hız ve zaman bakımından ağırlaşmayı temel alır; komşu dal ise görevde yetersiz çaba gösterme anlamına da uzanır.","focus_only":"Odak dal yalın yavaşlamayı ve babasını yitirmiş çocuğa iyiliğin geç ulaşmasına ilişkin açıklamayı içerir.","gloss":"yavaşlama ile çabada geri kalma","neighbor_only":"Komşu dal bir işte, özellikle öğüt vermede, gereken çabayı göstermeyip geri kalmayı da içerir.","neighbor_ref":"root_000048/B001","relation_type":"near_synonym","shared_zone":"İki dal da bir işin veya ilerleyişin beklenenden geç gerçekleşmesini anlatabilir."},{"boundary_match":"partial","distinction":"Odak dal gözlenen hız düşüşüdür; komşu dal ise hareketin altında yatan gevşeme ve güç azalması durumunu öne çıkarır.","focus_only":"Odak dal yavaşlamayı nedenine bakmadan bildirir ve iyiliğin gecikmesine ilişkin açıklayıcı bir bağlantı taşır.","gloss":"yavaşlama ile güçten düşme","neighbor_only":"Komşu dal işte veya yol alışta güç ve canlılığın azalmasından doğan gevşemeyi anlatır.","neighbor_ref":"root_001621/B006","relation_type":"near_neighbor","shared_zone":"Her iki dal yol alışın veya işin daha ağır sürmesine uygulanabilir."},{"boundary_match":"partial","distinction":"Odak dal sonucun hız boyutunu adlandırır; komşu dal bedensel veya ruhsal gevşekliği kurucu unsur yapar.","focus_only":"Odak dal gecikmeyi ve ilerleyişin ağırlaşmasını bedensel bir neden gerektirmeden anlatır.","gloss":"gecikme ile gevşek ve isteksiz davranma","neighbor_only":"Komşu dal tembellik, ateşli hastalık veya beden gevşekliğiyle bağlantılı isteksizlik ve ağır davranmayı kapsar.","neighbor_ref":"root_000392/B001","relation_type":"near_neighbor","shared_zone":"Ağır yürüyen veya işini yavaş yapan kişi iki alanın görünür sonucunu paylaşabilir."},{"boundary_match":"partial","distinction":"Bu dal zamansal ve devinimsel ağırlaşmadır; komşu dal ise davranış ve dikkat kusurudur.","focus_only":"Odak dal hareket hızının düşmesini veya bir şeyin geç ulaşmasını anlatır.","gloss":"yavaşlama ile dikkatsizlik","neighbor_only":"Komşu dal dikkat göstermemeyi ve yapılması gerekeni eksik bırakmayı anlatır.","neighbor_ref":"root_001692/B003","relation_type":"near_neighbor","shared_zone":"Yol alışa ilişkin aynı kalıp iki anlam için kaynaklarda yorumlanmıştır."}],"source_phrase_ar":"في سيره يتم أي إبطاء (sihah)؛ اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه (tahdhib)","source_summary":"Kaynakların ortak alanı genel yavaşlama ve gecikmedir. Yol alıştaki ağırlaşma bir aktarımdaki özel uygulama, iyiliğin babasını yitirmiş çocuğa geç ulaşması ise diğer aktarımdaki adlandırma açıklamasıdır.","sources":["SI","TA"],"what_is_ar":"يدخل فيه اليتم بمعنى الإبطاء، وخاصة قولهم في سيره يتم، وتعليل تسمية اليتيم بأن البر يبطئ عنه","what_is_not_ar":"ليس الغفلة والتقصير إلا حيث جعلها المصدر تفسيرا آخر، وليس الانفراد في الشيء"},"support_links":[]},{"boundary":"Kullanım yalnız kadınlara yönelik tanıklanmış adlandırma kalıplarıyla sınırlıdır; gerçek bir eş kaybı veya genel eşsizlik anlamı çıkarılamaz.","branch_kind":"collocation","branch_ref":"root_001692/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:2:4:2","qac_word_ref":"107:2:4","surface_ar":"يَتِيمَ"}],"gloss":"evlilikle sona erip ermediği tartışmalı kadın adlandırması","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kullanım, babasını yitirmiş çocuklara verilen adın kadın hakkında da söylenmesinden oluşur."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir aktarımda kadın evlenince bu adlandırma sona erer; karşıt aktarımda ise kadın bu adı hiçbir zaman yitirmez."}}],"root_ar":"ي ت م","root_id":"root_001692","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kadına yönelik bu özel adın evlilikten sonra sürüp sürmediğine ilişkin iki aktarımı birlikte özetlerken kullanılır.","boundary_detail":"Kullanım yalnız kadınlara yönelik tanıklanmış adlandırma kalıplarıyla sınırlıdır; gerçek bir eş kaybı veya genel eşsizlik anlamı çıkarılamaz.","branch_image_ar":"انفراد المرأة عن الزوج","concept_gloss":"evlilikle sona erip ermediği tartışmalı kadın adlandırması","contextual_glosses":[{"applicability":"Adlandırmanın kadının evlenmesiyle sona erdiğini kabul eden aktarımın bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına yönelik kullanımı ve evlilikte sona erme sınırını korur."},"facet_ids":["F001","F002"],"text":"evlenene dek bu adla anılan kadın","usage_role":"contextual"},{"applicability":"Adlandırmanın evlilikten sonra da sürdüğünü kabul eden karşıt aktarımın bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Kadına yönelik kullanımı ve evlilikten sonra sürme bilgisini korur."},"facet_ids":["F001","F002"],"text":"evlendikten sonra da bu adla anılan kadın","usage_role":"contextual"}],"definition":"Kadına, babasını yitirmiş çocuklara verilen adla seslenilen kalıplaşmış bir kullanımdır. Bir aktarım bu adın evlilikle sona erdiğini, diğeri ise evlilikten sonra da sürdüğünü bildirir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kullanım, babasını yitirmiş çocuklara verilen adın kadın hakkında da söylenmesinden oluşur."},{"facet_id":"F002","role":"source_variant","statement":"Bir aktarımda kadın evlenince bu adlandırma sona erer; karşıt aktarımda ise kadın bu adı hiçbir zaman yitirmez."}],"identity_rationale":"Kaynak ifadesi kocasından ayrılmış kadını tanımlamaz; kadına belirli bir adın verilmesini ve bu adın evlilikle sona erip ermediğine ilişkin iki karşıt aktarımı bildirir. Dal korunabilir, ancak tanımı eşten ayrılma yerine bu kalıplaşmış ve tartışmalı adlandırmaya bağlanmalıdır.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"evlenene dek, başka bir aktarıma göre ise evlendikten sonra da babasını yitirmiş çocuk adıyla anılan kadın"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"kadınların babasını yitirmiş çocuk adıyla anılabileceğini bildiren söz"}],"lexicalization_note":"Tanım yalnız kadın hakkında kullanılan iki tanıklanmış söz kalıbına bağlıdır; buradan yalın biçime genel bir evlenmemişlik veya eşten ayrılma anlamı aktarılamaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; özel kadın adlandırmasını eşsiz olma, eşten kopma, ebeveyn kaybı ve eş olma alanlarından ayıran dört aday yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal gerçek medeni durumu tanımlamak yerine özel bir adlandırmayı aktarır; komşu dal ise kişinin eşinin bulunmamasını cinsiyet ayrımı olmadan bildirir.","focus_only":"Odak dal kadınlara verilen özel bir addır ve bir aktarımda evlilikten sonra da sürebilir.","gloss":"kadına verilen özel ad ile eşsiz olma","neighbor_only":"Komşu dal kadın veya erkeğin fiilen eşsiz olmasını ve evlenmeden kalmasını doğrudan anlatır.","neighbor_ref":"root_000073/B001","relation_type":"near_neighbor","shared_zone":"Evlenmemiş kadın, bir aktarımda iki kullanımın ortak bağlamında bulunabilir."},{"boundary_match":"partial","distinction":"Odak dal eşten ayrılmayı gerektirmez; komşu dalın çekirdeği ise eş bağının bulunmaması veya kesilmesidir.","focus_only":"Odak dal evlilik öncesinde kullanılan ve bazı aktarımlarda evlilik sonrasında da süren bir kadın adlandırmasıdır.","gloss":"kadın adlandırması ile eşten kopma","neighbor_only":"Komşu dal eşten kopma, uzun süre eşsiz kalma ve evlenmeme durumunu anlatır.","neighbor_ref":"root_001252/B009","relation_type":"near_neighbor","shared_zone":"Her iki dal kadın ve evlilik durumu çevresinde kullanılabilir."},{"boundary_match":"partial","distinction":"Biçim ortaklığına rağmen odak dalda ebeveyn ölümü kurucu değildir; komşu dalda ise ebeveynin ölümü ve katılımcı ayrımı anlamın temelidir.","focus_only":"Odak dal kadın hakkındaki kalıplaşmış adlandırmayı ve süresine ilişkin aktarım ayrılığını içerir.","gloss":"kadına verilen ad ile ebeveyn kaybı","neighbor_only":"Komşu dal insan çocuğunun babasını ergenlikten önce, hayvan yavrusunun ise annesini yitirmesiyle oluşan gerçek durumu bildirir.","neighbor_ref":"root_001692/B001","relation_type":"near_neighbor","shared_zone":"Kadına verilen ad, babasını yitirmiş çocuk için kullanılan adlandırmayla biçimsel olarak ortaktır."},{"boundary_match":"thematic_only","distinction":"Odak dalın içeriği adlandırmanın süresidir; komşu dalın içeriği ise eşin kendisi ve eş olma bağıdır, bu nedenle anlamsal örtüşme çok sınırlıdır.","focus_only":"Odak dal, kadına yönelik özel bir adın evlilikle sona erip ermediğini tartışır.","gloss":"kadın adlandırması ve eş olma","neighbor_only":"Komşu dal eş olan erkeği, eş olan kadını ve eş olma ilişkisini doğrudan adlandırır.","neighbor_ref":"root_000134/B001","relation_type":"thematic","shared_zone":"İki dal da evlilik ilişkisini çevreleyen söz varlığında yer alır."}],"source_phrase_ar":"المرأة تدعى يتيما ما لم تتزوج فإذا تزوجت زال عنها اسم اليتم؛ يقال للمرأة يتيمة لا يزول عنها اسم اليتم أبدا (tahdhib)","source_qualifications":[{"kind":"disagreement","summary":"Bir aktarım adlandırmayı evlenene kadar sürdürürken diğeri evliliğin bu adı sona erdirmediğini bildirir."}],"source_summary":"Kanıt, kadınlara özgü bu kalıplaşmış adlandırmanın evlilikle ilişkili olduğunu, ancak kullanım süresinin tek biçimde aktarılmadığını gösterir.","sources":["TA"],"what_is_ar":"يدخل فيه إطلاق يتيمة على المرأة عند من يجعله قبل الزواج أو لا يزيله الزواج","what_is_not_ar":"ليس اليتيم من الصبيان ولا كل منفرد من الأشياء ولا أم الأيتام"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["107:2:1"],"branch_refs":[],"candidate_id":"cand_cb1f5519a8dcbc65eaa7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:2:1:answer-consequence","source_type":"word_analysis","support_ids":["sup_1994978ea24d57e13386","sup_e2c571f57a2f8dd9bd27"],"title":"answering connector turns denial into visible conduct","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:1","qac_refs":["107:2:1:1"],"status":"accepted"}},{"anchor_refs":["107:2:1"],"branch_refs":[],"candidate_id":"cand_16f79546f66e2fd3036f","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:2:1:dual-explanation-causation","source_type":"word_analysis","support_ids":["sup_264866edf40de563d8d4","sup_e2c571f57a2f8dd9bd27"],"title":"explanation and causation remain simultaneous","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:1","qac_refs":["107:2:1:1"],"status":"accepted"}},{"anchor_refs":["107:2:1"],"branch_refs":[],"candidate_id":"cand_d644f0145fe3a743cab4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:2:1:immediate-boundary-link","source_type":"word_analysis","support_ids":["sup_d8f257df60f488840d2c","sup_e2c571f57a2f8dd9bd27"],"title":"ayah boundary remains grammatically joined","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:1","qac_refs":["107:2:1:1"],"status":"accepted"}},{"anchor_refs":["107:2:1"],"branch_refs":[],"candidate_id":"cand_51cef3459b1497bbc1f9","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:2:1:proclitic-fusion","source_type":"word_analysis","support_ids":["sup_2f4be308e54053cae4ff","sup_e2c571f57a2f8dd9bd27"],"title":"bound form fuses hinge with pointing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:1","qac_refs":["107:2:1:1"],"status":"accepted"}},{"anchor_refs":["107:2:2"],"branch_refs":[],"candidate_id":"cand_c429ca85410d41bd11b4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:2:2:composite-deictic-force","source_type":"word_analysis","support_ids":["sup_993692ec174d789741a6","sup_c4bbe45b9fca1d8743ac"],"title":"form stacks pointing distance and address","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:2","qac_refs":["107:2:1:2"],"status":"accepted"}},{"anchor_refs":["107:2:2"],"branch_refs":[],"candidate_id":"cand_9f9b290de7ac68a43d7b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:2:2:definite-distant-pointing","source_type":"word_analysis","support_ids":["sup_5f225c7c6e62769359a9","sup_993692ec174d789741a6"],"title":"far demonstrative points while distancing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:2","qac_refs":["107:2:1:2"],"status":"accepted"}},{"anchor_refs":["107:2:2"],"branch_refs":[],"candidate_id":"cand_019091add70efe434aa9","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:2:2:nominal-identification-frame","source_type":"word_analysis","support_ids":["sup_30e4ad395acda067c59a","sup_993692ec174d789741a6"],"title":"nominal frame turns behavior into definition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:2","qac_refs":["107:2:1:2"],"status":"accepted"}},{"anchor_refs":["107:2:2"],"branch_refs":[],"candidate_id":"cand_3d53af5cc38bcd3dcef1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:2:2:question-to-identification-bridge","source_type":"word_analysis","support_ids":["sup_18f4b7a118915f55fd86","sup_993692ec174d789741a6"],"title":"prior question resolves into pointing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:2","qac_refs":["107:2:1:2"],"status":"accepted"}},{"anchor_refs":["107:2:3"],"branch_refs":[],"candidate_id":"cand_55ea9a1cad0269c60c7b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:2:3:agreement-chain","source_type":"word_analysis","support_ids":["sup_4d7697d1f435912c3270","sup_f3a7ae1be2bd7bead69f"],"title":"agreement keeps denier as agent","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:3","qac_refs":["107:2:2:1"],"status":"accepted"}},{"anchor_refs":["107:2:3"],"branch_refs":[],"candidate_id":"cand_ba740ff72a4b904ed2fb","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:2:3:defining-relative-predicate","source_type":"word_analysis","support_ids":["sup_4d7697d1f435912c3270","sup_faf92c7f7810a53764a1"],"title":"relative pronoun makes conduct defining","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:3","qac_refs":["107:2:2:1"],"status":"accepted"}},{"anchor_refs":["107:2:3"],"branch_refs":[],"candidate_id":"cand_615ca0c5e2ef3acc1986","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:2:3:parse-and-attachment-scope","source_type":"word_analysis","support_ids":["sup_4d7697d1f435912c3270","sup_78814a40e30cb1ffcce2"],"title":"predicate or attribute still binds the clause","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:3","qac_refs":["107:2:2:1"],"status":"accepted"}},{"anchor_refs":["107:2:3"],"branch_refs":[],"candidate_id":"cand_df775dec70d8af24fc99","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:2:3:repeated-relative-bridge","source_type":"word_analysis","support_ids":["sup_422939e4a933db411581","sup_4d7697d1f435912c3270"],"title":"matched relatives join the two accusations","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:3","qac_refs":["107:2:2:1"],"status":"accepted"}},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_83d20bad420710ec0fc4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:4:accepted-variant-abandonment","source_type":"word_analysis","support_ids":["sup_8bbbb8d4ba878b441f23","sup_aabcd314a2535d362ced"],"title":"variant opens abandonment beside pushing","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:4","qac_refs":["107:2:3:1"],"status":"accepted"}},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_e157198e0aa4f62b0898","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:4:active-habitual-agency","source_type":"word_analysis","support_ids":["sup_272d99f5f27505f85db5","sup_8bbbb8d4ba878b441f23"],"title":"active imperfect makes repulsion characteristic","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:4","qac_refs":["107:2:3:1"],"status":"accepted"}},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_4cd4642b6db4289be25f","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:4:composite-pressure-point","source_type":"word_analysis","support_ids":["sup_7529e905b5167e7e6948","sup_8bbbb8d4ba878b441f23"],"title":"form sense sound and recurrence converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:4","qac_refs":["107:2:3:1"],"status":"accepted"}},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_53a362bec88e7888c297","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:4:directed-force-role-frame","source_type":"word_analysis","support_ids":["sup_469352abce0e3209ada8","sup_8bbbb8d4ba878b441f23"],"title":"force moves from denier onto orphan","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:4","qac_refs":["107:2:3:1"],"status":"accepted"}},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_97f7425a292410dcda9b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:4:feeding-refusal-bridge","source_type":"word_analysis","support_ids":["sup_8bbbb8d4ba878b441f23","sup_b26d54accfd6d19ffcfe"],"title":"repulsion anticipates feeding refusal","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:4","qac_refs":["107:2:3:1"],"status":"accepted"}},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_f1f605807e1e0775d3c7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:4:geminate-rough-repulsion","source_type":"word_analysis","support_ids":["sup_63e4993bedfff840f536","sup_8bbbb8d4ba878b441f23"],"title":"geminate root selects forceful repulsion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:4","qac_refs":["107:2:3:1"],"status":"accepted"}},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_fd25eaeae7c7ca40175a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:4:passive-reversal-5213","source_type":"word_analysis","support_ids":["sup_8bbbb8d4ba878b441f23","sup_de52ccda1707d07150ac"],"title":"active pusher is set beside passive pushed","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:4","qac_refs":["107:2:3:1"],"status":"accepted"}},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_75b7b61ca285e060faa2","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:4:root-form-not-call","source_type":"word_analysis","support_ids":["sup_8bbbb8d4ba878b441f23","sup_e4d0efa10b4161681e66"],"title":"doubling blocks the call-root misread","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:4","qac_refs":["107:2:3:1"],"status":"accepted"}},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_660e61055c80cc1953a3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:4:sound-pressure","source_type":"word_analysis","support_ids":["sup_0bd1b7b4439c678c6bb4","sup_8bbbb8d4ba878b441f23"],"title":"doubled guttural makes force audible","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:4","qac_refs":["107:2:3:1"],"status":"accepted"}},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_700dde101d4edbf23b4a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:4:theology-to-bodily-harm","source_type":"word_analysis","support_ids":["sup_8bbbb8d4ba878b441f23","sup_a738a58b68447f4c8553"],"title":"denial becomes bodily repulsion","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:4","qac_refs":["107:2:3:1"],"status":"accepted"}},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_0f40ca0333fadd7542a4","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:4:variant-form-echo","source_type":"word_analysis","support_ids":["sup_19bc20b68c0f44a5fcf9","sup_8bbbb8d4ba878b441f23"],"title":"near sound changes root and event type","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:4","qac_refs":["107:2:3:1"],"status":"accepted"}},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_77396a38c4db9e5c2c0b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:4:variant-forsaking-echo","source_type":"word_analysis","support_ids":["sup_434e27c6a6d0b243edf3","sup_8bbbb8d4ba878b441f23"],"title":"variant recalls forsaking negated at 93:3","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:4","qac_refs":["107:2:3:1"],"status":"accepted"}},{"anchor_refs":["107:2:5"],"branch_refs":[],"candidate_id":"cand_7cb27911a2bc06af4c35","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"107:2:5:cadence-and-next-endpoint","source_type":"word_analysis","support_ids":["sup_0f511fe39ab62a3f285c","sup_aea2e6cac2fcdad538a1"],"title":"final cadence links orphan and needy endpoints","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:5","qac_refs":["107:2:4:1","107:2:4:2"],"status":"accepted"}},{"anchor_refs":["107:2:5"],"branch_refs":[],"candidate_id":"cand_cb0597d98628ae34a1d0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"107:2:5:converged-patient-indictment","source_type":"word_analysis","support_ids":["sup_aea2e6cac2fcdad538a1","sup_d2e941c9280266b285c6"],"title":"form role root and distribution converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:5","qac_refs":["107:2:4:1","107:2:4:2"],"status":"accepted"}},{"anchor_refs":["107:2:5"],"branch_refs":[],"candidate_id":"cand_329c984b44a2e9f65da4","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"107:2:5:cut-off-double-severance","source_type":"word_analysis","support_ids":["sup_9559835471ab669470f6","sup_aea2e6cac2fcdad538a1"],"title":"already cut-off one is pushed farther away","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:5","qac_refs":["107:2:4:1","107:2:4:2"],"status":"accepted"}},{"anchor_refs":["107:2:5"],"branch_refs":[],"candidate_id":"cand_ab79c6cb7ed6002d2131","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"107:2:5:definite-singular-class","source_type":"word_analysis","support_ids":["sup_a29fc7ef37e6d8da7293","sup_aea2e6cac2fcdad538a1"],"title":"definite singular focuses class through one figure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:5","qac_refs":["107:2:4:1","107:2:4:2"],"status":"accepted"}},{"anchor_refs":["107:2:5"],"branch_refs":[],"candidate_id":"cand_868646410f0eb9e68961","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"107:2:5:direct-object-patient","source_type":"word_analysis","support_ids":["sup_5070fed0300a83cc9fbf","sup_aea2e6cac2fcdad538a1"],"title":"orphan receives the verb's force directly","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:5","qac_refs":["107:2:4:1","107:2:4:2"],"status":"accepted"}},{"anchor_refs":["107:2:5"],"branch_refs":[],"candidate_id":"cand_490701733c096d988483","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"107:2:5:inverted-care-distribution","source_type":"word_analysis","support_ids":["sup_aea2e6cac2fcdad538a1","sup_c11cc8a72b824fbbb12e"],"title":"orphan-care word appears in a violence frame","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:5","qac_refs":["107:2:4:1","107:2:4:2"],"status":"accepted"}},{"anchor_refs":["107:2:5"],"branch_refs":[],"candidate_id":"cand_79ea9354f751330a636c","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"107:2:5:order-and-closure","source_type":"word_analysis","support_ids":["sup_5bac6215829d5fdd81cb","sup_aea2e6cac2fcdad538a1"],"title":"victim name lands after the force","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:5","qac_refs":["107:2:4:1","107:2:4:2"],"status":"accepted"}},{"anchor_refs":["107:2:5"],"branch_refs":[],"candidate_id":"cand_97c93c7f83b808f1da16","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"107:2:5:orphan-care-echoes","source_type":"word_analysis","support_ids":["sup_62d34e4d89ff214406a8","sup_aea2e6cac2fcdad538a1"],"title":"repulsion contrasts shelter and warning scenes","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:5","qac_refs":["107:2:4:1","107:2:4:2"],"status":"accepted"}},{"anchor_refs":["107:2:5"],"branch_refs":[],"candidate_id":"cand_2f3179bb8acb8ec439e1","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"107:2:5:qualitative-state","source_type":"word_analysis","support_ids":["sup_398fe81971885fcd6dfa","sup_aea2e6cac2fcdad538a1"],"title":"form names an enduring exposed condition","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:5","qac_refs":["107:2:4:1","107:2:4:2"],"status":"accepted"}},{"anchor_refs":["107:2:5"],"branch_refs":[],"candidate_id":"cand_70c833bc8dd01a781805","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"107:2:5:singular-value-pressure","source_type":"word_analysis","support_ids":["sup_aea2e6cac2fcdad538a1","sup_d6f4b5c6883fc2f3725c"],"title":"peerless-singular branch colors the harm","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:2:5","qac_refs":["107:2:4:1","107:2:4:2"],"status":"accepted"}},{"anchor_refs":["107:2:3"],"branch_refs":[],"candidate_id":"cand_36a8a39e34b023ef9fcc","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000477","root_000478"],"scope":"focus_ayah","source_local_id":"107:2:3:1","source_type":"qac_morpheme","support_ids":["sup_9ce92f435cebdf64f220"],"title":"QAC root occurrence: د ع ع","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["107:2:4"],"branch_refs":[],"candidate_id":"cand_a509d847c790bd02829b","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_001692"],"scope":"focus_ayah","source_local_id":"107:2:4:2","source_type":"qac_morpheme","support_ids":["sup_f260de83bb2f265b3931"],"title":"QAC root occurrence: ي ت م","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["107:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:2","branch_refs":["root_000477/B001","root_001692/B001"],"candidate_id":"cand_da7fd8da1d0930765c71","commentary_obligation":"review","hft_ref":"hft_4b2056fe2d46df191224","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_forceful_resevering","source_type":"hft","support_ids":["sup_1aa923127a6d0edd8b45"],"title":"b_forceful_resevering","trust":"legacy_unbound"},{"anchor_refs":["107:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:2","branch_refs":["root_000477/B001","root_000478/B001","root_001692/B002"],"candidate_id":"cand_ceecaf70ededba2ca837","commentary_obligation":"review","hft_ref":"hft_de4b86a3a378a93bf94d","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_summons_reversed","source_type":"hft","support_ids":["sup_16ff0b02a06e911120e2"],"title":"b_summons_reversed","trust":"legacy_unbound"},{"anchor_refs":["107:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:2","branch_refs":["root_000477/B003","root_000477/B009","root_001692/B002"],"candidate_id":"cand_b6e61ee9d293635a85e0","commentary_obligation":"review","hft_ref":"hft_0c7f3d14171820a3ccc6","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:b_herding_the_singular","source_type":"hft","support_ids":["sup_409ffd3e1031524f93aa"],"title":"b_herding_the_singular","trust":"legacy_unbound"},{"anchor_refs":["107:2"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:2","branch_refs":["root_000477/B001","root_000477/B004","root_001692/B001"],"candidate_id":"cand_09657578babde7b517f4","commentary_obligation":"review","hft_ref":"hft_6a1c694fa079d7985807","kind":"surprising_outlier","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:o_stumbler_recovery_reversed","source_type":"hft","support_ids":["sup_75c1600008d8b8b83ff4"],"title":"o_stumbler_recovery_reversed","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"107:2:1:1","qac_word_ref":"107:2:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"107:2:1:2","qac_word_ref":"107:2:1","root_ar":"","surface_ar":"ذَٰلِكَ"},{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"107:2:2:1","qac_word_ref":"107:2:2","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","root_ar":"د ع ع","surface_ar":"يَدُعُّ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"107:2:4:1","qac_word_ref":"107:2:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:2:4:2","qac_word_ref":"107:2:4","root_ar":"ي ت م","surface_ar":"يَتِيمَ"}],"word_analysis_qac_refs":[["107:2:1:1"],["107:2:1:2"],["107:2:2:1"],["107:2:3:1"],["107:2:4:1","107:2:4:2"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["107:2:1","107:2:2","107:2:3","107:2:4","107:2:5"]},"focus_surface_evidence":{"arabic_uthmani":"فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:CONJ+","morpheme_role":"PREFIX","pos":"CONJ","qac_ref":"107:2:1:1","qac_word_ref":"107:2:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"ذَٰلِك","morph_features":"STEM|POS:DEM|LEM:*a`lik|MS","morpheme_role":"STEM","pos":"DEM","qac_ref":"107:2:1:2","qac_word_ref":"107:2:1","root_ar":"","surface_ar":"ذَٰلِكَ"},{"lemma_ar":"ٱلَّذِى","morph_features":"STEM|POS:REL|LEM:{l~a*iY|MS","morpheme_role":"STEM","pos":"REL","qac_ref":"107:2:2:1","qac_word_ref":"107:2:2","root_ar":"","surface_ar":"ٱلَّذِى"},{"lemma_ar":"يَدُعُّ","morph_features":"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS","morpheme_role":"STEM","pos":"V","qac_ref":"107:2:3:1","qac_word_ref":"107:2:3","root_ar":"د ع ع","surface_ar":"يَدُعُّ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"107:2:4:1","qac_word_ref":"107:2:4","root_ar":"","surface_ar":"ٱلْ"},{"lemma_ar":"يَتِيم","morph_features":"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC","morpheme_role":"STEM","pos":"N","qac_ref":"107:2:4:2","qac_word_ref":"107:2:4","root_ar":"ي ت م","surface_ar":"يَتِيمَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["107:2:1:1"],["107:2:1:2"],["107:2:2:1"],["107:2:3:1"],["107:2:4:1","107:2:4:2"]],"word_analysis_refs":["107:2:1","107:2:2","107:2:3","107:2:4","107:2:5"],"word_rows":[{"analysis_record_ref":"107:2:1","analytic_gloss_range_en":"bound consequential and explanatory connector that makes 107:2 answer the prior question rather than begin an unrelated statement","analytic_root_gloss_range_en":null,"qac_refs":["107:2:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فَ","transliteration":"fa-"}},{"analysis_record_ref":"107:2:2","analytic_gloss_range_en":"far masculine singular demonstrative pointing back to the denier in 107:1 with definite recognition, listener involvement, and evaluative distance","analytic_root_gloss_range_en":null,"qac_refs":["107:2:1:2"],"root":{"note":"no lexical root"},"surface":{"arabic":"ذَٰلِكَ","transliteration":"dhālika"}},{"analysis_record_ref":"107:2:3","analytic_gloss_range_en":"definite masculine singular relative pronoun that turns the following verb-object clause into the identifying predicate of the pointed figure","analytic_root_gloss_range_en":null,"qac_refs":["107:2:2:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"ٱلَّذِى","transliteration":"alladhī"}},{"analysis_record_ref":"107:2:4","analytic_gloss_range_en":"active imperfect geminate verb of forceful pushing, thrusting, or repulsing directed at the orphan; accepted variant evidence adds abandonment as contrast, not as replacement of the canonical pushing sense","analytic_root_gloss_range_en":"root range includes rough thrusting and forceful driving plus other dictionary branches such as vessel-agitation, cries, movement, dependents, and plant or seed terms; the local verb selects the rough repulsion branch","qac_refs":["107:2:3:1"],"root":{"arabic":"د ع ع","transliteration":"d-ʿ-ʿ"},"surface":{"arabic":"يَدُعُّ","transliteration":"yaduʿʿu"}},{"analysis_record_ref":"107:2:5","analytic_gloss_range_en":"definite singular orphan as the direct object and patient of pushing, locally carrying class force, individual focus, prior deprivation of protection, and narrowed singular-value pressure","analytic_root_gloss_range_en":"root range includes orphanhood through loss of a protecting parent, isolated or peerless singleness, and other branches such as heedlessness, delay, and disputed marriage-related uses; the local noun selects the orphanhood and exposed-protection branch with singularity pressure","qac_refs":["107:2:4:1","107:2:4:2"],"root":{"arabic":"ي ت م","transliteration":"y-t-m"},"surface":{"arabic":"ٱلْيَتِيمَ","transliteration":"al-yatīma"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":5,"words_total":5,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["107:2"],"branch_refs":["root_000477/B001","root_001692/B001"],"candidate_id":"cand_da7fd8da1d0930765c71","evidence_scope":"focus_ayah","hft_ref":"hft_4b2056fe2d46df191224","item_id":"b_forceful_resevering","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_forceful_resevering","support_id":"sup_1aa923127a6d0edd8b45"},{"anchor_refs":["107:2"],"branch_refs":["root_000477/B001","root_000478/B001","root_001692/B002"],"candidate_id":"cand_ceecaf70ededba2ca837","evidence_scope":"focus_ayah","hft_ref":"hft_de4b86a3a378a93bf94d","item_id":"b_summons_reversed","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_summons_reversed","support_id":"sup_16ff0b02a06e911120e2"},{"anchor_refs":["107:2"],"branch_refs":["root_000477/B003","root_000477/B009","root_001692/B002"],"candidate_id":"cand_b6e61ee9d293635a85e0","evidence_scope":"focus_ayah","hft_ref":"hft_0c7f3d14171820a3ccc6","item_id":"b_herding_the_singular","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:b_herding_the_singular","support_id":"sup_409ffd3e1031524f93aa"},{"anchor_refs":["107:2"],"branch_refs":["root_000477/B001","root_000477/B004","root_001692/B001"],"candidate_id":"cand_09657578babde7b517f4","evidence_scope":"focus_ayah","hft_ref":"hft_6a1c694fa079d7985807","item_id":"o_stumbler_recovery_reversed","kind":"surprising_outlier","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:o_stumbler_recovery_reversed","support_id":"sup_75c1600008d8b8b83ff4"}],"diagnostics":[],"lane_counts":{"global":11,"macro":11,"micro":4},"packet_summary":{"ayah_count":7,"focus_ref":"107:2","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"د ع ع","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000477","furuq_root_norm":"د ع ع","furuq_source_root_norm":"د ع ع","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000478","furuq_root_norm":"د ع و","furuq_source_root_norm":"د ع و","is_dominant":false,"target_occurrences":1,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]}],"window":["107:1","107:2","107:3","107:4","107:5","107:6","107:7"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"107:2","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":11,"source_present":true,"structured_insight_count":15,"unstructured_record_count":0},"identity":{"ayah_ref":"107:2","lane":"micro","linguistic_source_ref":"107:2","surface_ref":"107:2","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"107:2","target_tokens":[["İşte",["107:2:1"]],["yetimi",["107:2:4"]],["itip",["107:2:3"]],["kakan",["107:2:2","107:2:3"]],["odur",["107:2:1","107:2:2"]]],"text":"İşte yetimi itip kakan odur."},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":7,"id":"s107-p01-001-007","label":"Whole surah","number":1,"refs":["107:1","107:2","107:3","107:4","107:5","107:6","107:7"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4:sound-pressure","source_type":"word_analysis","support_id":"sup_0bd1b7b4439c678c6bb4","text":"{\"blocking_evidence\":null,\"headline\":\"doubled guttural makes force audible\",\"reader_payoff\":\"The reader notices that the doubled guttural pressure makes the shove felt in recitation before the orphan is named.\",\"reason\":\"The local surface contains consonant doubling on the geminate consonant, and the following object provides the phonetic contrast described by the CRITICAL rows.\",\"representative_source_ids\":[\"QP-6d168889\",\"QP-7e3c4d00\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:5:cadence-and-next-endpoint","source_type":"word_analysis","support_id":"sup_0f511fe39ab62a3f285c","text":"{\"blocking_evidence\":null,\"headline\":\"final cadence links orphan and needy endpoints\",\"reader_payoff\":\"The reader notices that the orphan remains acoustically present at the close and is paired with the needy person endpoint in 107:3.\",\"reason\":\"The CRITICAL rows track the ayah-final position and adjacent vulnerable ending in 107:3; this is a forward bridge, not a new lexical sense.\",\"representative_source_ids\":[\"QP-5a5fcce6\",\"QP-f06e534a\",\"QB-4a84a738\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:2:question-to-identification-bridge","source_type":"word_analysis","support_id":"sup_18f4b7a118915f55fd86","text":"{\"blocking_evidence\":null,\"headline\":\"prior question resolves into pointing\",\"reader_payoff\":\"The reader notices the movement from being asked to look in 107:1 to being handed the identification in 107:2.\",\"reason\":\"The demonstrative reference is discourse-bound to the prior ayah, so the boundary bridge claimed by the CRITICAL rows is licensed.\",\"representative_source_ids\":[\"QB-4803c6a7\",\"QB-538e37c5\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:1:answer-consequence","source_type":"word_analysis","support_id":"sup_1994978ea24d57e13386","text":"{\"blocking_evidence\":null,\"headline\":\"answering connector turns denial into visible conduct\",\"reader_payoff\":\"The reader notices that 107:2 is the diagnostic answer to 107:1, making the treatment of the orphan the visible consequence of denial.\",\"reason\":\"QAC and attachment support the initial particle as a consequential or explanatory link from 107:1, so the CRITICAL claim that it answers the prior question is locally licensed.\",\"representative_source_ids\":[\"QG-1b6ce740\",\"QG-4bbf1958\",\"MG-0af98e77\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4:variant-form-echo","source_type":"word_analysis","support_id":"sup_19bc20b68c0f44a5fcf9","text":"{\"blocking_evidence\":null,\"headline\":\"near sound changes root and event type\",\"reader_payoff\":\"The reader notices that the near sound between the canonical and variant forms is interpretive: doubled force becomes lighter leaving in the variant.\",\"reason\":\"The CRITICAL rows describe a form contrast that is valid as apparatus, while local grammar keeps {{ar:يَدُعُّ}} ({{tr:yaduʿʿu}}) as the canonical analyzed surface.\",\"representative_source_ids\":[\"QF-113f041d\",\"QE-f1893938\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:1:dual-explanation-causation","source_type":"word_analysis","support_id":"sup_264866edf40de563d8d4","text":"{\"blocking_evidence\":null,\"headline\":\"explanation and causation remain simultaneous\",\"reader_payoff\":\"The reader notices that the particle both explains who the denier is and shows what denial produces.\",\"reason\":\"The QAC note allows a consequential function, while the CRITICAL row preserves the explanatory force of the same opening.\",\"representative_source_ids\":[\"QS-11bda0ee\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4:active-habitual-agency","source_type":"word_analysis","support_id":"sup_272d99f5f27505f85db5","text":"{\"blocking_evidence\":null,\"headline\":\"active imperfect makes repulsion characteristic\",\"reader_payoff\":\"The reader notices that the denier is grammatically responsible for an ongoing pattern of pushing, while the orphan is excluded from the subject role.\",\"reason\":\"QAC marks the verb as active imperfect 3ms with an explicit object, and attachment evidence controls the subject through the relative predicate.\",\"representative_source_ids\":[\"QG-b16cb736\",\"QG-c53b4a61\",\"QG-ec087c47\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:1:proclitic-fusion","source_type":"word_analysis","support_id":"sup_2f4be308e54053cae4ff","text":"{\"blocking_evidence\":null,\"headline\":\"bound form fuses hinge with pointing\",\"reader_payoff\":\"The reader notices that the connector is not a detached preface; it is fused to the demonstrative, so consequence and identification arrive together.\",\"reason\":\"The surface begins with the bound particle before the demonstrative, matching the CRITICAL rows that describe a consequence-identification unit.\",\"representative_source_ids\":[\"QF-c34c4aa9\",\"QT-9df252c5\",\"QB-9c87b62b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:2:nominal-identification-frame","source_type":"word_analysis","support_id":"sup_30e4ad395acda067c59a","text":"{\"blocking_evidence\":null,\"headline\":\"nominal frame turns behavior into definition\",\"reader_payoff\":\"The reader notices that the sentence first identifies the person and then defines him through the relative predicate, rather than merely narrating an event.\",\"reason\":\"Attachment evidence analyzes {{ar:ذَٰلِكَ}} ({{tr:dhālika}}) with {{ar:ٱلَّذِى}} ({{tr:alladhī}}) as a nominal identification, and the masculine singular concord keeps the relative predicate attached.\",\"representative_source_ids\":[\"QG-5213adc1\",\"QT-0f165b94\",\"QT-eebc1895\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:5:qualitative-state","source_type":"word_analysis","support_id":"sup_398fe81971885fcd6dfa","text":"{\"blocking_evidence\":null,\"headline\":\"form names an enduring exposed condition\",\"reader_payoff\":\"The reader notices that the object is marked as a stable vulnerable condition with audible definiteness, not a passing circumstance.\",\"reason\":\"QAC tags the form as a noun or substantivized qualitative adjective with the article, supporting the CRITICAL point about enduring status and definiteness.\",\"representative_source_ids\":[\"QF-4966e511\",\"QF-b415bfea\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:3:repeated-relative-bridge","source_type":"word_analysis","support_id":"sup_422939e4a933db411581","text":"{\"blocking_evidence\":null,\"headline\":\"matched relatives join the two accusations\",\"reader_payoff\":\"The reader notices that the repeated relative form binds the denier in 107:1 and the orphan-pusher in 107:2 into one referential profile.\",\"reason\":\"The current relative pronoun follows the discourse-linked demonstrative, so the CRITICAL bridge to the prior relative identification is coherent.\",\"representative_source_ids\":[\"QE-f58ce66a\",\"QB-6850bca3\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4:variant-forsaking-echo","source_type":"word_analysis","support_id":"sup_434e27c6a6d0b243edf3","text":"{\"blocking_evidence\":null,\"headline\":\"variant recalls forsaking negated at 93:3\",\"reader_payoff\":\"The reader notices a contrastive field: the variant's abandonment sense stands beside the denial of divine forsaking at 93:3.\",\"reason\":\"The reference is supplied by the CRITICAL row; it is kept as a variant-based echo, not as control over the canonical parse.\",\"representative_source_ids\":[\"QE-d8731680\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4:directed-force-role-frame","source_type":"word_analysis","support_id":"sup_469352abce0e3209ada8","text":"{\"blocking_evidence\":null,\"headline\":\"force moves from denier onto orphan\",\"reader_payoff\":\"The reader notices the moral relation inside the verb frame itself: force is applied by the denier and received by the vulnerable object.\",\"reason\":\"The direct-object frame and the accepted rough-thrusting branch support the CRITICAL claim that the act is directed, bodily, and morally loaded.\",\"representative_source_ids\":[\"QS-73573f87\",\"QS-cb903813\",\"QS-dd03c756\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:3","source_type":"word_analysis","support_id":"sup_4d7697d1f435912c3270","text":"{\"gloss_range\":\"definite masculine singular relative pronoun that turns the following verb-object clause into the identifying predicate of the pointed figure\",\"prose\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}}) is the hinge that converts a full action into an identifying predicate. It matches {{ar:ذَٰلِكَ}} ({{tr:dhālika}}) and prepares the 3ms verb, so the denier remains the acting subject while {{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}}) waits as the object. The repeated relative form also links this identification back to the one in 107:1: the one who denies and the one who pushes are not two figures, but one referent described by two actions.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ٱلَّذِى}} ({{tr:alladhī}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:5:direct-object-patient","source_type":"word_analysis","support_id":"sup_5070fed0300a83cc9fbf","text":"{\"blocking_evidence\":null,\"headline\":\"orphan receives the verb's force directly\",\"reader_payoff\":\"The reader notices that the orphan is the direct grammatical and semantic patient of force, not a remote topic of concern.\",\"reason\":\"QAC and attachment evidence mark {{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}}) as the accusative direct object of {{ar:يَدُعُّ}} ({{tr:yaduʿʿu}}).\",\"representative_source_ids\":[\"QG-11f060f8\",\"QG-4c633212\",\"QS-505f9314\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:5:order-and-closure","source_type":"word_analysis","support_id":"sup_5bac6215829d5fdd81cb","text":"{\"blocking_evidence\":null,\"headline\":\"victim name lands after the force\",\"reader_payoff\":\"The reader notices that the force is heard before the victim is named, and the ayah closes on the harmed object.\",\"reason\":\"The local word order places the verb before the object and makes {{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}}) the final word of the ayah.\",\"representative_source_ids\":[\"QT-89139420\",\"QT-eec3717f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:2:definite-distant-pointing","source_type":"word_analysis","support_id":"sup_5f225c7c6e62769359a9","text":"{\"blocking_evidence\":null,\"headline\":\"far demonstrative points while distancing\",\"reader_payoff\":\"The reader notices that the ayah points to a recognizable denier while also holding that figure at evaluative distance.\",\"reason\":\"QAC and attachment identify the demonstrative as masculine singular and discourse-linked to 107:1, while the CRITICAL rows press the far-deictic distance and recognition.\",\"representative_source_ids\":[\"QG-b374375d\",\"QS-aca00b75\",\"MS-b2f35f45\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:5:orphan-care-echoes","source_type":"word_analysis","support_id":"sup_62d34e4d89ff214406a8","text":"{\"blocking_evidence\":null,\"headline\":\"repulsion contrasts shelter and warning scenes\",\"reader_payoff\":\"The reader notices that 107:2 reverses the sheltering response to orphanhood at 93:6 and stands against the orphan-care warning at 93:9.\",\"reason\":\"The CRITICAL rows provide concrete references, and the local construction supplies the contrast between care and repulsion.\",\"representative_source_ids\":[\"QE-e354ec75\",\"QE-fb7a3cdb\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4:geminate-rough-repulsion","source_type":"word_analysis","support_id":"sup_63e4993bedfff840f536","text":"{\"blocking_evidence\":null,\"headline\":\"geminate root selects forceful repulsion\",\"reader_payoff\":\"The reader notices that the word is not a calling verb but a rough repulsion verb, so the charge is physical and contemptuous from the lexical choice itself.\",\"reason\":\"QAC distinguishes {{ar:د ع ع}} ({{tr:d-ʿ-ʿ}}) from the common calling root, and V4 branch B001 supports rough thrusting or forceful driving as the locally selected branch.\",\"representative_source_ids\":[\"QS-5648ed86\",\"QS-8f12a016\",\"QF-9346aa2f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4:composite-pressure-point","source_type":"word_analysis","support_id":"sup_7529e905b5167e7e6948","text":"{\"blocking_evidence\":null,\"headline\":\"form sense sound and recurrence converge\",\"reader_payoff\":\"The reader notices that morphology, rough sense, sound, variant contrast, and recurrence together make the verb the compact center of the accusation.\",\"reason\":\"The composite rows collect several independently supported local observations: active imperfect agency, geminate pushing, variant contrast, sound pressure, and the 52:13 recurrence.\",\"representative_source_ids\":[\"MF-5d05a81b\",\"QY-66713218\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:3:parse-and-attachment-scope","source_type":"word_analysis","support_id":"sup_78814a40e30cb1ffcce2","text":"{\"blocking_evidence\":null,\"headline\":\"predicate or attribute still binds the clause\",\"reader_payoff\":\"The reader notices that either local parse keeps the following action attached to the demonstrative rather than loose in the sentence.\",\"reason\":\"QAC allows the relative pronoun to introduce the clause after {{ar:ذَٰلِكَ}} ({{tr:dhālika}}), and attachment evidence strongly licenses the local relative clause.\",\"representative_source_ids\":[\"QG-22e4e48b\",\"QF-aadc2104\",\"QT-9c12265a\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4","source_type":"word_analysis","support_id":"sup_8bbbb8d4ba878b441f23","text":"{\"gloss_range\":\"active imperfect geminate verb of forceful pushing, thrusting, or repulsing directed at the orphan; accepted variant evidence adds abandonment as contrast, not as replacement of the canonical pushing sense\",\"prose\":\"{{ar:يَدُعُّ}} ({{tr:yaduʿʿu}}) is the ayah's pressure point. The active imperfect makes the denier the ongoing agent of force, not the witness to a one-time incident, and the object after it makes {{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}}) receive that force directly. Its geminate root {{ar:د ع ع}} ({{tr:d-ʿ-ʿ}}) selects rough repulsion and blocks the near-looking call root {{ar:د ع و}} ({{tr:d-ʿ-w}}): the orphan is not being called near but driven away. The accepted variant {{ar:يَدَعُ}} ({{tr:yadaʿu}}) broadens the accusation by contrast toward abandonment, with the forsaking field recalled at 93:3, while the canonical surface keeps bodily thrusting in front. The recurrence with the passive pushing scene at 52:13 sharpens the role reversal, and the doubled guttural sound makes the shove audible before the softer object arrives. Looking forward, the verb also begins the care-refusal chain that reaches feeding in 107:3: the root's concrete image of pushing food away turns bodily repulsion into the first sign of sustenance exclusion.\",\"root_display\":\"{{ar:د ع ع}} ({{tr:d-ʿ-ʿ}})\",\"root_gloss_range\":\"root range includes rough thrusting and forceful driving plus other dictionary branches such as vessel-agitation, cries, movement, dependents, and plant or seed terms; the local verb selects the rough repulsion branch\",\"surface_display\":\"{{ar:يَدُعُّ}} ({{tr:yaduʿʿu}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:5:cut-off-double-severance","source_type":"word_analysis","support_id":"sup_9559835471ab669470f6","text":"{\"blocking_evidence\":null,\"headline\":\"already cut-off one is pushed farther away\",\"reader_payoff\":\"The reader notices double severance: the one already deprived of primary protection is made the target of further social repulsion.\",\"reason\":\"V4 supports the orphanhood branch as loss of the protecting parent, and the local direct-object frame places that exposed figure under a force verb.\",\"representative_source_ids\":[\"QS-0b381516\",\"QS-13bbaccb\",\"QS-4684aacc\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:2","source_type":"word_analysis","support_id":"sup_993692ec174d789741a6","text":"{\"gloss_range\":\"far masculine singular demonstrative pointing back to the denier in 107:1 with definite recognition, listener involvement, and evaluative distance\",\"prose\":\"{{ar:ذَٰلِكَ}} ({{tr:dhālika}}) makes the answer pointed and definite: not an abstract sinner somewhere, but that recognizable figure from 107:1. Its far-deictic shape keeps the person at moral distance while still involving the listener in recognition, and the written long pointing form gives that reach audible extension rather than a flat pronominal resumption. The masculine singular agreement with {{ar:ٱلَّذِى}} ({{tr:alladhī}}) then locks the following relative clause onto this referent, so the act that follows becomes the person's defining identification.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:ذَٰلِكَ}} ({{tr:dhālika}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"107:2:3:1","source_type":"qac_morpheme","support_id":"sup_9ce92f435cebdf64f220","text":"{\"lemma_ar\":\"يَدُعُّ\",\"morph_features\":\"STEM|POS:V|IMPF|LEM:yaduE~u|ROOT:dEE|3MS\",\"morpheme_role\":\"STEM\",\"pos\":\"V\",\"qac_ref\":\"107:2:3:1\",\"qac_word_ref\":\"107:2:3\",\"root_ar\":\"د ع ع\",\"surface_ar\":\"يَدُعُّ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:5:definite-singular-class","source_type":"word_analysis","support_id":"sup_a29fc7ef37e6d8da7293","text":"{\"blocking_evidence\":null,\"headline\":\"definite singular focuses class through one figure\",\"reader_payoff\":\"The reader notices that the singular definite form keeps the scene individual while letting the orphan stand as a recognizable vulnerable class.\",\"reason\":\"The noun is definite, singular, and accusative; QAC allows generic, specific, or known-reference readings, so the generic class force is preserved without excluding individual focus.\",\"representative_source_ids\":[\"QG-303091e4\",\"QF-56f0c7e0\",\"QF-98deee13\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4:theology-to-bodily-harm","source_type":"word_analysis","support_id":"sup_a738a58b68447f4c8553","text":"{\"blocking_evidence\":null,\"headline\":\"denial becomes bodily repulsion\",\"reader_payoff\":\"The reader notices the surah's movement from invisible denial to visible bodily harm against the orphan.\",\"reason\":\"The opening boundary relation links 107:2 to 107:1, and the verb-object clause supplies the concrete conduct that answers the denial.\",\"representative_source_ids\":[\"QB-8e3c48ce\",\"QB-9f2d25f4\",\"QB-b04d3820\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4:accepted-variant-abandonment","source_type":"word_analysis","support_id":"sup_aabcd314a2535d362ced","text":"{\"blocking_evidence\":null,\"headline\":\"variant opens abandonment beside pushing\",\"reader_payoff\":\"The reader notices that accepted variant evidence widens the accusation from forceful expulsion to abandonment, while the canonical form still governs the local pushing sense.\",\"reason\":\"The variant preserves the same 3ms imperfect frame and object but changes the root, so it can serve as contrast without replacing the canonical local surface.\",\"representative_source_ids\":[\"QG-d4338de2\",\"QS-a2e8c53f\",\"QI-58301f32\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:5","source_type":"word_analysis","support_id":"sup_aea2e6cac2fcdad538a1","text":"{\"gloss_range\":\"definite singular orphan as the direct object and patient of pushing, locally carrying class force, individual focus, prior deprivation of protection, and narrowed singular-value pressure\",\"prose\":\"{{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}}) is not merely near the action; its accusative direct-object role makes the orphan the immediate patient of {{ar:يَدُعُّ}} ({{tr:yaduʿʿu}}), with the force heard before the victim is named. The definite singular lets one harmed figure stand for the recognizable class without dissolving the scene into an abstract plural, and its qualitative shape names orphanhood as an enduring exposed state rather than a passing circumstance. The root {{ar:ي ت م}} ({{tr:y-t-m}}) names a child cut off from primary protection, so the pushing creates double severance: the already exposed one is pushed farther out. The wider singular or peerless branch remains as narrowed image-pressure, making the harm fall on a vulnerable person whose singular value is not erased. This is distributionally inverted against the Quranic orphan-care field, including shelter at 93:6 and warning at 93:9, and the final-position cadence leaves the harmed object ringing into the next vulnerable endpoint, {{ar:ٱلْمِسْكِينِ}} ({{tr:al-miskīn}}), in 107:3.\",\"root_display\":\"{{ar:ي ت م}} ({{tr:y-t-m}})\",\"root_gloss_range\":\"root range includes orphanhood through loss of a protecting parent, isolated or peerless singleness, and other branches such as heedlessness, delay, and disputed marriage-related uses; the local noun selects the orphanhood and exposed-protection branch with singularity pressure\",\"surface_display\":\"{{ar:ٱلْيَتِيمَ}} ({{tr:al-yatīma}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4:feeding-refusal-bridge","source_type":"word_analysis","support_id":"sup_b26d54accfd6d19ffcfe","text":"{\"blocking_evidence\":null,\"headline\":\"repulsion anticipates feeding refusal\",\"reader_payoff\":\"The reader notices that the pushing verb begins a care-refusal sequence that reaches the feeding language of 107:3.\",\"reason\":\"The main local sense remains forceful repulsion, while the supplied food-pushing image and the next ayah's feeding language license a forward bridge rather than a replacement gloss.\",\"representative_source_ids\":[\"QS-216bd643\",\"QB-5c3a1aec\",\"QY-e0316b02\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:5:inverted-care-distribution","source_type":"word_analysis","support_id":"sup_c11cc8a72b824fbbb12e","text":"{\"blocking_evidence\":null,\"headline\":\"orphan-care word appears in a violence frame\",\"reader_payoff\":\"The reader notices the inversion: a word normally surrounded by care, charity, and protection is here governed by a force verb.\",\"reason\":\"Contextual evidence shows the orphan term in human-generic contexts and attachment evidence makes this occurrence the direct object of pushing, preserving the CRITICAL distributional inversion.\",\"representative_source_ids\":[\"MS-73afae8f\",\"QI-7a921a79\",\"QH-f1f1946b\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:2:composite-deictic-force","source_type":"word_analysis","support_id":"sup_c4bbe45b9fca1d8743ac","text":"{\"blocking_evidence\":null,\"headline\":\"form stacks pointing distance and address\",\"reader_payoff\":\"The reader notices that the demonstrative's form makes the pointing extended and listener-facing, not a flat pronoun.\",\"reason\":\"The surface form and QAC deictic analysis support the CRITICAL observation that the word carries more force than a simple pronominal resumption.\",\"representative_source_ids\":[\"QF-117cbb7c\",\"QF-36d691ff\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:5:converged-patient-indictment","source_type":"word_analysis","support_id":"sup_d2e941c9280266b285c6","text":"{\"blocking_evidence\":null,\"headline\":\"form role root and distribution converge\",\"reader_payoff\":\"The reader notices how singular definite form, patient role, root vulnerability, and distributional inversion converge on the orphan as the concentrated object of indictment.\",\"reason\":\"The synthesis row is supported by the local form, object role, root branch, and the care-frame inversion already preserved in separate topics.\",\"representative_source_ids\":[\"QY-8c863e7f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:5:singular-value-pressure","source_type":"word_analysis","support_id":"sup_d6f4b5c6883fc2f3725c","text":"{\"blocking_evidence\":null,\"headline\":\"peerless-singular branch colors the harm\",\"reader_payoff\":\"The reader notices that the root's singular-value pressure makes the harmed orphan individually weighty, while the local noun remains the orphan sense.\",\"reason\":\"V4 recognizes a branch of isolated or peerless singleness, but local grammar and QAC select the orphan noun; the branch survives as image-pressure rather than a replacement gloss.\",\"representative_source_ids\":[\"QS-76afbd07\",\"QS-924ec335\",\"QS-e91091bb\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:1:immediate-boundary-link","source_type":"word_analysis","support_id":"sup_d8f257df60f488840d2c","text":"{\"blocking_evidence\":null,\"headline\":\"ayah boundary remains grammatically joined\",\"reader_payoff\":\"The reader notices that the ayah break does not reset the argument; the opening particle carries the previous question forward without delay.\",\"reason\":\"The local word table and translation support warn against treating 107:2 as an unrelated new statement; the particle marks the continuation across the boundary.\",\"representative_source_ids\":[\"QG-b843314f\",\"QT-7338832b\",\"QB-370a3aef\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4:passive-reversal-5213","source_type":"word_analysis","support_id":"sup_de52ccda1707d07150ac","text":"{\"blocking_evidence\":null,\"headline\":\"active pusher is set beside passive pushed\",\"reader_payoff\":\"The reader notices the role reversal between the active pusher here and the passive pushed scene at 52:13.\",\"reason\":\"The supplied recurrence to 52:13 shares the pushing field and contrasts active and passive roles without changing the local parse.\",\"representative_source_ids\":[\"QI-c3f34f67\",\"QE-25ecd6f7\",\"QH-9082a928\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:1","source_type":"word_analysis","support_id":"sup_e2c571f57a2f8dd9bd27","text":"{\"gloss_range\":\"bound consequential and explanatory connector that makes 107:2 answer the prior question rather than begin an unrelated statement\",\"prose\":\"{{ar:فَ}} ({{tr:fa-}}) makes the ayah arrive as the answer to the question in 107:1. It does not merely add a next item; it carries explanation, consequence, and immediacy, so the denial named before is made visible at once in the behavior that follows. Because it is bound into {{ar:فَذَٰلِكَ}} ({{tr:fa-dhālika}}), the hinge and the pointing word are heard as one opening movement: the reader is pushed across the ayah boundary into an identification.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:4:root-form-not-call","source_type":"word_analysis","support_id":"sup_e4d0efa10b4161681e66","text":"{\"blocking_evidence\":null,\"headline\":\"doubling blocks the call-root misread\",\"reader_payoff\":\"The reader notices that a small formal difference prevents a major semantic mistake: the geminate form gives pushing, not calling.\",\"reason\":\"The local form is identified as a geminate root rather than a derived form of the common call root, so the near-sound alternative is excluded.\",\"representative_source_ids\":[\"QF-08b6fa93\",\"QF-f6244f05\",\"QI-9b85dede\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"107:2:4:2","source_type":"qac_morpheme","support_id":"sup_f260de83bb2f265b3931","text":"{\"lemma_ar\":\"يَتِيم\",\"morph_features\":\"STEM|POS:N|LEM:yatiym|ROOT:ytm|MS|ACC\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"107:2:4:2\",\"qac_word_ref\":\"107:2:4\",\"root_ar\":\"ي ت م\",\"surface_ar\":\"يَتِيمَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:3:agreement-chain","source_type":"word_analysis","support_id":"sup_f3a7ae1be2bd7bead69f","text":"{\"blocking_evidence\":null,\"headline\":\"agreement keeps denier as agent\",\"reader_payoff\":\"The reader notices that agreement keeps the denier as the verb's subject while the orphan remains the affected object.\",\"reason\":\"The 3ms subject of {{ar:يَدُعُّ}} ({{tr:yaduʿʿu}}) is syntactically controlled by the relative predicate linked to the demonstrative.\",\"representative_source_ids\":[\"QG-ed9fd4e8\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:2:3:defining-relative-predicate","source_type":"word_analysis","support_id":"sup_faf92c7f7810a53764a1","text":"{\"blocking_evidence\":null,\"headline\":\"relative pronoun makes conduct defining\",\"reader_payoff\":\"The reader notices that the action is not a side report; it is the defining predicate by which the pointed figure is known.\",\"reason\":\"Attachment evidence places the relative clause as the predicate of the nominal identification, matching the CRITICAL rows about definition through conduct.\",\"representative_source_ids\":[\"QG-00b532d2\",\"QS-b3a4590e\",\"QT-623fafa3\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ","ayah_ref":"107:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000477/B001","root_001692/B001"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000477","role":"Supplies rough, forceful thrusting and makes the predicate an enacted expulsion rather than passive neglect.","root":"د ع ع","source_ref":"107:2","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001692","role":"Supplies a child cut off from parental protection, so the thrust compounds an already broken protective relation.","root":"ي ت م","source_ref":"107:2","source_word_indices":["4"]}],"changed_reading":{"after":"He actively re-enacts orphaning: force is used to drive an already unprotected dependent farther from access, belonging, and protection.","before":"He is harsh to the orphan or sends the orphan away."},"confidence":"strong","focus_anchor":"The transitive focus verb at word 3 acts directly on the unprotected person named at word 4.","mechanism":"Forceful driving meets a person already defined by severance from a protector. The act therefore does more than fail to repair vulnerability: it actively repeats and intensifies the orphan's constitutive separation.","model_id":"b_forceful_resevering"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_forceful_resevering","source_type":"hft","support_id":"sup_1aa923127a6d0edd8b45","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ","ayah_ref":"107:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000477/B001","root_000478/B001","root_001692/B002"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000477","role":"Contributes outward force and supplies the expelling pole of the reversal.","root":"د ع ع","source_ref":"107:2","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000478","role":"Contributes calling that draws near and supplies the unrealized relational alternative to expulsion.","root":"د ع ع","source_ref":"107:2","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001692","role":"Contributes solitary disconnection, making nearness versus further isolation the mechanism's decisive axis.","root":"ي ت م","source_ref":"107:2","source_word_indices":["4"]}],"changed_reading":{"after":"The shove is the inverse of hospitality and summons: the isolated person who should be drawn into relation is deliberately driven out of it.","before":"The line depicts a one-directional shove."},"confidence":"medium","focus_anchor":"The focus verb's split mapping holds both forceful driving and speech that draws someone near, while its object is socially isolated.","mechanism":"The opposed branch directions create a relational reversal. A person who most needs to be called into proximity is instead propelled outward; exclusion becomes the corruption of an available summons.","model_id":"b_summons_reversed"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_summons_reversed","source_type":"hft","support_id":"sup_16ff0b02a06e911120e2","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ","ayah_ref":"107:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000477/B003","root_000477/B009","root_001692/B002"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000477","role":"Supplies the chiding call used to drive a herd and frames the action as coercive management by voice.","root":"د ع ع","source_ref":"107:2","source_word_indices":["3"]},{"branch_id":"B002","mapped_root_id":"root_001692","role":"Supplies isolated singularity, highlighting the violence of reducing an irreducible person to movable stock.","root":"ي ت م","source_ref":"107:2","source_word_indices":["4"]},{"branch_id":"B009","mapped_root_id":"root_000477","role":"Supplies small dependents as a branch image and keeps the coercive management attached to the focus object's dependency.","root":"د ع ع","source_ref":"107:2","source_word_indices":["3"]}],"changed_reading":{"after":"The orphan is coercively managed and de-personed: singular vulnerability is treated as a troublesome dependent category to be driven along.","before":"The orphan receives an isolated act of rough treatment."},"confidence":"exploratory","focus_anchor":"A chiding-herding branch of the focus verb converges with the object's branch of singular, peerless isolation.","mechanism":"The act can be carried as social reduction: a singular person is handled as a steerable unit, moved by rebuke rather than addressed as a claimant or relation. The reading coexists with literal bodily force but shifts attention to dehumanizing command.","model_id":"b_herding_the_singular"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:b_herding_the_singular","source_type":"hft","support_id":"sup_409ffd3e1031524f93aa","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ","ayah_ref":"107:2"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000477/B001","root_000477/B004","root_001692/B001"],"payload":{"activation_trace":[{"branch_id":"B004","mapped_root_id":"root_000477","role":"Supplies a restorative cry to a stumbler and creates the help-to-rise pole of the reversal.","root":"د ع ع","source_ref":"107:2","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_000477","role":"Supplies actual rough thrusting and turns potential restoration into renewed downfall.","root":"د ع ع","source_ref":"107:2","source_word_indices":["3"]},{"branch_id":"B001","mapped_root_id":"root_001692","role":"Supplies missing support and makes the failure to raise the fallen relationally exact.","root":"ي ت م","source_ref":"107:2","source_word_indices":["4"]}],"changed_reading":{"after":"Exploratorily, the line stages anti-rescue: the verbal space that could tell the unsupported person to rise is converted into the force that makes rising harder.","before":"The actor knocks or drives the orphan away."},"confidence":"exploratory","containment":"The recovery-call branch is surprising because it is formulaic and not the ordinary sense of the focus verb. It remains anchored in the same focus root and converges with the object's lost support: speech that should help a fallen person rise is inverted into force that keeps an unsupported person down. Render only as a contained reversal, not as a replacement lexical gloss.","focus_anchor":"The focus verb at word 3 carries both severe thrusting and a formula addressed to a stumbler, while word 4 names someone without ordinary support.","outlier_id":"o_stumbler_recovery_reversed"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:o_stumbler_recovery_reversed","source_type":"hft","support_id":"sup_75c1600008d8b8b83ff4","trust":"legacy_unbound"}]}
</lane_packet_json>
