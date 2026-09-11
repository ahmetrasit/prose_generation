# Commentary v5 scope discovery

You are the fresh **micro** scope discoverer for **107:4**. This is
the first of two planned turns for this lane. Decide what the supplied evidence
supports and persist the requested discovery JSON. Do not write polished commentary prose.

Write exactly one JSON object to `_commentary/v5/raw/s107-regular-20260911/s107/107_4/micro.discovery.json` and modify nothing
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
  "ayah_ref": "107:4",
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
{"analysis_context":{"analysis_id":"s107-regular-20260911","external_ayat_refs":["1:2","1:3","1:4","1:5","1:6","1:7"],"focus_ref":"107:4","host_surah":107,"lane_context_refs":[],"ordered_context_refs":["107:0","107:1","107:2","107:3","107:5","107:6","107:7","1:2","1:3","1:4","1:5","1:6","1:7"]},"branch_registry":[{"boundary":"Ateşle doğrudan karşılaşma çekirdektir; pişirme, yakma, düzeltme, yakacak ve zorluğa katlanma kullanımları ayrı tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000879/B001","candidate_links":[{"candidate_id":"cand_178a29fa5ddeaa3c187c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"ateşin yakıcı sıcaklığına maruz kalma ve ateşle işleme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir varlık ateşe girer, ateşin yanında kalır veya onun yakıcı sıcaklığını ve şiddetini çeker."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Kişi ateşin yanında durarak onun sıcaklığıyla ısınır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Belirli kuruluşlarda et ateşte pişirilir veya değnek ateşte yumuşatılıp düzeltilir."}},{"facet_id":"F004","role":"source_variant","source_fields":["distinctive_facets[F004]"],"statements":{"statement":"Ad biçimi ateşi tutuşturup sürdürmeye yarayan yakacağı, ayrıca ateşte pişirme işini belirtebilir."}},{"facet_id":"F005","role":"extension","source_fields":["distinctive_facets[F005]"],"statements":{"statement":"Ateşin yakıcılığı, bir işin ağırlığını ve sıkıntısını çekmeye aktarılır."}}],"root_ar":"ص ل و","root_id":"root_000879","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ateşe girme veya onun ısısını çekme çekirdeğini, ateşle pişirme, yakma ve biçim verme işlemleriyle birlikte temsil eder.","boundary_detail":"Ateşle doğrudan karşılaşma çekirdektir; pişirme, yakma, düzeltme, yakacak ve zorluğa katlanma kullanımları ayrı tutulur.","branch_image_ar":"ملاقاة النار وحرها","concept_gloss":"ateşin yakıcı sıcaklığına maruz kalma ve ateşle işleme","contextual_glosses":[{"applicability":"Canlının ateşin içine girdiği, orada kaldığı veya onun yakıcı sıcaklığını çektiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Ateş yanında ısınma, nesneyi ateşle işleme, yakacak ve zorluğa katlanma yönlerini dışarıda bırakır.","preserves":"Ateşe doğrudan maruz kalma ve yanıcı sıcaklığı çekme yönünü korur."},"facet_ids":["F001"],"text":"ateşe girip yanmak","usage_role":"contextual"},{"applicability":"Et ya da başka bir nesnenin ateşe tutulduğu veya başka birinin ateşe atıldığı geçişli kullanımlara uygundur.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Öznenin ateş sıcaklığını çekmesi, ısınması, yakacak anlamı ve sıkıntıya katlanması kaybolur.","preserves":"Ateşle bir nesne üzerinde pişirme veya yakma işlemi yapılmasını korur."},"facet_ids":["F003"],"text":"ateşte pişirmek veya yakmak","usage_role":"contextual"},{"applicability":"Ateşin yakıcılığının ağır bir işin eziyetine aktarıldığı mecazlı kuruluşlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Gerçek ateş, ısınma, pişirme, yakma, düzeltme ve yakacak anlamlarını dışarıda bırakır.","preserves":"Yakıcı şiddete katlanma düşüncesinin zorlu bir işe aktarılmasını korur."},"facet_ids":["F005"],"text":"bir işin sıkıntısını çekmek","usage_role":"contextual"}],"definition":"Ateşin içine girerek ya da yanında bulunarak onun yakıcı sıcaklığına maruz kalmayı anlatır; ateşte eti pişirme ile değneği ateşte yumuşatıp düzeltme gibi ateşle işleme anlamları belirli kuruluşlara bağlıdır. Ateşi besleyen yakacak adı ile bir işin ağır sıkıntısını çekme anlamı bu çekirdeğe bağlı özel kullanımlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir varlık ateşe girer, ateşin yanında kalır veya onun yakıcı sıcaklığını ve şiddetini çeker."},{"facet_id":"F002","role":"specialization","statement":"Kişi ateşin yanında durarak onun sıcaklığıyla ısınır."},{"facet_id":"F003","role":"extension","statement":"Belirli kuruluşlarda et ateşte pişirilir veya değnek ateşte yumuşatılıp düzeltilir."},{"facet_id":"F004","role":"source_variant","statement":"Ad biçimi ateşi tutuşturup sürdürmeye yarayan yakacağı, ayrıca ateşte pişirme işini belirtebilir."},{"facet_id":"F005","role":"extension","statement":"Ateşin yakıcılığı, bir işin ağırlığını ve sıkıntısını çekmeye aktarılır."}],"identity_rationale":"Kaynak ifadesi ateşin sıcaklığına maruz kalmayı, ateş yanında ısınmayı, bir şeyi ateşle pişirip yakmayı, ateşe atmayı, yakacağı ve zorluğa katlanma aktarımını birlikte doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ateşe girip onun yakıcı sıcaklığını çekmek"},{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"ateşin yanında ısınmak"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"eti ateşte pişirmek"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"ateşte pişirilmiş"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"birini ateşe atıp yakmak"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ateşi besleyen yakacak; ateşte pişirme"},{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"değneği ateşte yumuşatıp düzeltmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"bir işin güçlüğünü ve yorgunluğunu çekmek"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"onun sertliğine kimse yanaşamaz"}],"lexicalization_note":"Tanım, yalın biçimlerin ateş ve yakacak anlamlarını korurken yalnız belirli kuruluşlarda görülen ısınma, düzeltme ve zorluğa katlanma anlamlarını genelleştirmez.","neighbor_coverage_note":"İki yakın komşu, dalın ateşe maruz kalma ve ateşle işleme taraflarını ayrı ayrı sınırlar; öteki adaylar yalnız ateş alanını ya da uzak eşadlı dalları paylaşır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Komşu dal doğrudan ateşle karşılaşma ve ateşe sokma sınırında kalır; odun düzeltme, pişirme, yakacak ve sıkıntıya katlanma gibi ek kullanımlar yalnız odak dalda açıkça yer alır.","focus_only":"Odun ve yiyeceği ateşle işleme, yakacak ve zorluğa katlanma gibi bağlı kullanımları da kapsar.","gloss":"ateşe ve onun yakıcı sıcaklığına maruz kalma","neighbor_only":null,"neighbor_ref":"root_000880/B003","relation_type":"near_synonym","shared_zone":"İki dal da ateşe girme, ateş yanında bulunma ve onun yakıcı sıcaklığını çekme çekirdeğinde birleşir."},{"boundary_match":"partial","distinction":"Komşu dal ateşi yakma ve nesneyi ateşle işleme çevresinde toplanır; odak dal buna ek olarak ateşe maruz kalan kişinin yaşadığı ısı ve sıkıntıyı da kapsar.","focus_only":"Ateşe girme, ateşin sıcaklığını çekme ve ağır bir sıkıntıya katlanma yönlerini içerir.","gloss":"ateşi yakma ve ateşle düzeltme","neighbor_only":"Ateşi yakıp tutuşturma eylemi komşu dalda açıkça bulunur.","neighbor_ref":"root_000880/B004","relation_type":"near_synonym","shared_zone":"İki dal da yakacak, ateşte pişirme ve değneği ateşte yumuşatıp düzeltme kullanımlarını paylaşır."}],"source_phrase_ar":"صليت العود بالنار (maqayis); اصطليت بالنار (maqayis;sihah); الصلا النار وصلى الكافر نارا (ayn); صليت اللحم شويته (ayn;sihah;tahdhib); الصلاء يقال للوقود وللشواء (mufradat); صلي بالأمر إذا قاسى حره وشدته (sihah;tahdhib)","source_summary":"Ortak anlatım, ateşin sıcaklığını çekme ve ateşle işleme çekirdeğini; ısınma, pişirme, yakma, değnek düzeltme, yakacak ve ağır bir işe katlanma yönleriyle genişletir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الاصطلاء بالنار والشواء والإحراق والوقود ومقاساة الحر والشدة","what_is_not_ar":"ليس الدعاء ولا العبادة ولا مواضعها ولا الصَّلا من الظهر"},"support_links":["sup_1b8122426ce82bb829c9"]},{"boundary":"Özneye göre gerçekleşme biçimi değişir: insan ve melek diler, Tanrı ise esirger, över ve değer verir.","branch_kind":"mixed_non_bare","branch_ref":"root_000879/B002","candidate_links":[{"candidate_id":"cand_a8fe65f7aa32df6c2599","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"başkası için iyilik dileme; esirgeme, övme ve değer verme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir kişi başkası için iyilik, esenlik ve iyi sonuç diler."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özne Tanrı olduğunda eylem esirgeme, güzel sözle anma, bağışlama ve değer verme olarak gerçekleşir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Özne melekler olduğunda başkası için bağışlanma ve iyilik isteme anlamı öne çıkar."}}],"root_ar":"ص ل و","root_id":"root_000879","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve meleklerin dileğini, Tanrı'nın ise dilekten farklı olarak esirgeme, övme ve değer verme eylemini kapsayan üst anlatımdır.","boundary_detail":"Özneye göre gerçekleşme biçimi değişir: insan ve melek diler, Tanrı ise esirger, över ve değer verir.","branch_image_ar":"الدعاء والثناء والرحمة","concept_gloss":"başkası için iyilik dileme; esirgeme, övme ve değer verme","contextual_glosses":[{"applicability":"Bir insanın başka biri için iyi sonuç, esenlik veya bağışlanma istediği bağlamlarda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Tanrı'nın esirgeme, övme ve değer verme eylemini doğrudan anlatmaz.","preserves":"Bir başkası yararına sözle iyi sonuç isteme yönünü korur."},"facet_ids":["F001"],"text":"onun için iyilik dilemek","usage_role":"general"},{"applicability":"Öznenin Tanrı olduğu ve eylemin esirgeme, güzel sözle anma, bağışlama ya da değer verme bildirdiği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"İnsanların ve meleklerin başkası için iyilik ya da bağışlanma istemesini dışarıda bırakır.","preserves":"Tanrı'ya özgü esirgeme ve övgü yönlerini açık biçimde korur."},"facet_ids":["F002"],"text":"Tanrı'nın esirgemesi ve övmesi","usage_role":"explanatory"}],"definition":"Bir başkası için iyilik istemeyi anlatır; özne Tanrı olduğunda esirgeme, güzel sözle anma, bağışlama ve değerini onaylama, melekler olduğunda ise bağışlanma ve iyilik isteme anlamı kazanır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir kişi başkası için iyilik, esenlik ve iyi sonuç diler."},{"facet_id":"F002","role":"specialization","statement":"Özne Tanrı olduğunda eylem esirgeme, güzel sözle anma, bağışlama ve değer verme olarak gerçekleşir."},{"facet_id":"F003","role":"specialization","statement":"Özne melekler olduğunda başkası için bağışlanma ve iyilik isteme anlamı öne çıkar."}],"identity_rationale":"Kaynak ifadesi insanlar için başkasına iyilik dileme anlamını, Tanrı için esirgeme, övme, bağışlama ve değer verme anlamlarını, melekler içinse bağışlanma dileğini açıkça ayırır.","lexical_glosses":[{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"başkası için iyilik ve esenlik dileme"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"biri için iyilik dilemek, onu övmek veya esirgenmesini istemek"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"Tanrı'nın esirgemesi, övmesi, bağışlaması ve değer vermesi"},{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"meleklerin bağışlanma ve iyilik dilemesi"}],"lexicalization_note":"Yalın iyilik dileme anlamı korunur; Tanrı ve meleklerle kurulan özel özne yapılarının anlamları bütün dala yayılmaz.","neighbor_coverage_note":"Tam eşleşen komşu dal yayımlandı; diğer adaylar yalnız belirli dilek türlerini, iyi karşılamayı veya bağışlamayı paylaşır ve dal sınırını ayrıca keskinleştirmez.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sunulan kartlarda çekirdek, özne ayrımı ve kapsam bakımından anlamlı bir sınır farkı bulunmaz.","focus_only":null,"gloss":"iyilik dileme, esirgeme ve övme","neighbor_only":null,"neighbor_ref":"root_000880/B002","relation_type":"synonym","shared_zone":"Her iki dal da insan, melek ve Tanrı öznesine göre ayrılan iyilik dileme, esirgeme, övme ve bağışlanma anlamlarını kapsar."}],"source_phrase_ar":"الصلاة وهي الدعاء (maqayis;sihah); صلوات الرسول للمسلمين دعاؤه لهم (ayn); الصلاة من الله تعالى الرحمة (maqayis;sihah;tahdhib); صلوات الله حسن ثنائه عليهم وقيل مغفرته لهم (ayn); صلاة الملائكة الاستغفار (ayn;tahdhib;mufradat); صلاة الله للمسلمين تزكيته إياهم (mufradat)","source_summary":"Ortak anlatım başkası için iyilik dilemeyi temel alır ve özneye göre Tanrı'nın esirgemesi, övmesi, bağışlaması ve değer vermesi ile meleklerin bağışlanma istemesini ayırır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"يدخل فيه الدعاء للغير والتبريك والاستغفار وصلاة الله بمعنى الرحمة والثناء والتزكية","what_is_not_ar":"ليست العبادة ذات الركوع والسجود ولا مواضع العبادة ولا النار والشواء"},"support_links":["sup_2589583ad8cbc5c8f0a8"]},{"boundary":"Burada genel iyilik dileği değil, bölümleri ve yerine getirilmesi gereken koşulları bulunan belirli tapınma eylemi tanımlanır.","branch_kind":"mixed_non_bare","branch_ref":"root_000879/B003","candidate_links":[{"candidate_id":"cand_ff16b8e41fc921d3adfe","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"ayakta durma, eğilme ve yere kapanma bölümleri olan kurallı tapınma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Kuralları belirlenmiş tapınma, ayakta durma, eğilme, yere kapanma, dilek ve yüceltme bölümlerini içerir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bu tapınmanın yerine getirilmesi, ona ait bütün gerekleri ve koşulları eksiksiz gözetmeyi gerektirir."}}],"root_ar":"ص ل و","root_id":"root_000879","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli hareket, söz ve koşulları bulunan tapınma eyleminin tamamını belirtir; yalnız genel bir dileği anlatmaz.","boundary_detail":"Burada genel iyilik dileği değil, bölümleri ve yerine getirilmesi gereken koşulları bulunan belirli tapınma eylemi tanımlanır.","branch_image_ar":"العبادة المخصوصة","concept_gloss":"ayakta durma, eğilme ve yere kapanma bölümleri olan kurallı tapınma","contextual_glosses":[{"applicability":"Kuralları belirli, ayakta durma, eğilme ve yere kapanma bölümleri bulunan tapınmanın Türkçedeki doğal kısa adıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli bölümleri, kuralları ve bütün olarak yerine getirilişi bulunan tapınmayı doğal biçimde karşılar."},"facet_ids":["F001","F002"],"text":"namaz","usage_role":"general"}],"definition":"Ayakta durma, eğilme, yere kapanma, dilekte bulunma ve yüceltme gibi belirli bölümleri bulunan kurallı bir tapınma eylemidir. Onu yerine getirmek, yalnız hareketleri yapmak değil, bütün gerek ve koşullarını gözetmektir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Kuralları belirlenmiş tapınma, ayakta durma, eğilme, yere kapanma, dilek ve yüceltme bölümlerini içerir."},{"facet_id":"F002","role":"specialization","statement":"Bu tapınmanın yerine getirilmesi, ona ait bütün gerekleri ve koşulları eksiksiz gözetmeyi gerektirir."}],"identity_rationale":"Kaynak ifadesi ayakta durma, eğilme, yere kapanma, dilek ve yüceltme bölümleri bulunan, kuralları belirlenmiş tapınmayı ve bu tapınmanın bütün gereklerini yerine getirmeyi açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"namaz"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"namazı bütün gerek ve koşullarını yerine getirerek kılmak"}],"lexicalization_note":"Yalın biçimin kurallı tapınma anlamı korunur; bütün hak ve koşulları yerine getirme vurgusu yalnız bunu bildiren özel kuruluşta tutulur.","neighbor_coverage_note":"Tam eşleşen komşu dal yeterli karşılaştırmayı sağlar; öteki adaylar tapınmanın yalnız bir duruşunu, genel kulluğu, yerini veya aracını paylaşır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sunulan kartlar, eylemin türü, temel bölümleri veya yerine getirme sınırı bakımından bir ayrım göstermemektedir.","focus_only":null,"gloss":"kuralları belirli namaz ibadeti","neighbor_only":null,"neighbor_ref":"root_000880/B001","relation_type":"synonym","shared_zone":"İki dal da ayakta durma, eğilme ve yere kapanma bölümleri bulunan, gerekleri gözetilerek yerine getirilen namaz ibadetini tanımlar."}],"source_phrase_ar":"الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة (maqayis); الصلاة واحدة الصلوات المفروضة (sihah); الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib); الصلاة التي هي العبادة المخصوصة أصلها الدعاء (mufradat); إقامة الصلاة (mufradat)","source_summary":"Ortak anlatım, ayakta durma, eğilme ve yere kapanma başta olmak üzere belirli bölümleri bulunan kurallı tapınmayı ve onun gereklerini eksiksiz yerine getirmeyi bildirir.","sources":["MQ","SI","TA","MU"],"what_is_ar":"يدخل فيه الصلاة الشرعية ذات الركوع والسجود والقيام بحدودها وإقامتها","what_is_not_ar":"ليست مطلق الدعاء ولا صلاة الله والملائكة ولا الكنائس"},"support_links":["sup_3330730bb67908045dee"]},{"boundary":"Kurulan yakalama aracı çekirdektir; bir kişiyi zarara düşürmek için düzen kurma anlamı bu çekirdeğin insana aktarılmasıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000879/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"yakalamak için kurulan tuzak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir hedefin içine düşerek yakalanması için tuzak veya benzeri bir araç kurulur."}},{"facet_id":"F002","role":"extension","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Tuzak düşüncesi, bir kimseyi zarara veya yıkıma düşürmek için gizlice düzen kurmaya aktarılır."}}],"root_ar":"ص ل و","root_id":"root_000879","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Av veya başka bir hedefin içine düşerek yakalanacağı somut araç çekirdeğini doğal ve eksiksiz biçimde karşılar.","boundary_detail":"Kurulan yakalama aracı çekirdektir; bir kişiyi zarara düşürmek için düzen kurma anlamı bu çekirdeğin insana aktarılmasıdır.","branch_image_ar":"الشرك المنصوبة","concept_gloss":"yakalamak için kurulan tuzak","contextual_glosses":[{"applicability":"Somut av aracının bir kişiyi zarara veya yıkıma götürecek gizli girişime aktarıldığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Av veya başka bir hedef için kurulan somut yakalama aracını doğrudan adlandırmaz.","preserves":"Hedefi önceden hazırlanmış bir düzenle zarara düşürme düşüncesini korur."},"facet_ids":["F002"],"text":"birini tuzağa düşürmek için düzen kurmak","usage_role":"contextual"}],"definition":"Avın ya da başka bir hedefin içine düşüp yakalanması için kurulan tuzaktır. Bir kimseyi zarara veya yıkıma düşürmek amacıyla gizlice iş çevirme anlamı bu araçtan türeyen bağlı kullanımdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir hedefin içine düşerek yakalanması için tuzak veya benzeri bir araç kurulur."},{"facet_id":"F002","role":"extension","statement":"Tuzak düşüncesi, bir kimseyi zarara veya yıkıma düşürmek için gizlice düzen kurmaya aktarılır."}],"identity_rationale":"Kaynak ifadesi avı ya da başka bir şeyi yakalamak için kurulan tuzakları ve buradan türeyen, bir kimseyi yıkıma düşürmek amacıyla iş çevirme kullanımını birlikte destekler.","lexical_glosses":[{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"av için kurulan tuzak"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"avı veya başka hedefleri yakalayan tuzaklar"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"birini yıkıma düşürmek için gizlice düzen kurmak"}],"lexicalization_note":"Yalın biçimlerin tuzak adı korunur; bir kişi için gizlice düzen kurma anlamı yalnız onu bildiren özel kuruluşla sınırlı tutulur.","neighbor_coverage_note":"Tam eşleşen komşu dal yayımlandı; diğer adaylar belirli tuzak türlerini, tuzağa yakalanma sonucunu veya avlanma sahnesindeki başka araçları gösterir.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Odak daldaki kişiye yönelik düzen kurma, tuzak çekirdeğinden türeyen bağımlı bir kullanımdır ve kartların temel sınırını değiştirmez.","focus_only":null,"gloss":"yakalamak için kurulan tuzaklar","neighbor_only":null,"neighbor_ref":"root_000880/B005","relation_type":"synonym","shared_zone":"İki dal da avı veya başka bir hedefi içine düşürüp yakalamak için kurulan tuzakları temel anlam olarak taşır."}],"source_phrase_ar":"مصالي هي الأشراك واحدتها مصلاة (maqayis); المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد (ayn); المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib); صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة (tahdhib)","source_summary":"Ortak anlatım, avı veya başka bir hedefi yakalamak üzere kurulan tuzağı temel alır ve aynı yapıyı bir kişiyi yıkıma sürükleyecek düzen kurmaya taşır.","sources":["MQ","AY","TA"],"what_is_ar":"يدخل فيه المصالي والمصلاة التي تنصب شركا للصيد أو الإيقاع","what_is_not_ar":"ليست الصلاة الدعاء ولا النار ولا الصَّلا من الجسد"},"support_links":[]},{"boundary":"Anatomik bölge çekirdektir; doğum sırasında açılma ve yavrunun bu bölgeye inmesi aynı bölgeye bağlı durumları anlatır.","branch_kind":"mixed_non_bare","branch_ref":"root_000879/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"sırtın ortası ve kuyruk kökünün iki yanı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan ve dört ayaklılarda sırtın orta bölümü ile kuyruk kökünün iki yanı adlandırılır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişinin doğumunda bu bölge açılır; devede yavrunun buraya inmesi doğumun yaklaştığını gösterir."}}],"root_ar":"ص ل و","root_id":"root_000879","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan veya dört ayaklı hayvanın sırt ve kuyruk kökü çevresindeki anatomik bölgesini birlikte karşılar.","boundary_detail":"Anatomik bölge çekirdektir; doğum sırasında açılma ve yavrunun bu bölgeye inmesi aynı bölgeye bağlı durumları anlatır.","branch_image_ar":"الصَّلا من الظهر والجنب","concept_gloss":"sırtın ortası ve kuyruk kökünün iki yanı","contextual_glosses":[{"applicability":"Dişinin doğumu sırasında anatomik bölgenin gevşeyip açıldığı veya yavrunun oraya indiği bağlamlara özgüdür.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bölgenin insan ve hayvandaki genel anatomik adını bağımsız olarak karşılamaz.","preserves":"Anatomik bölgenin doğum sırasında açılması ve doğumun yaklaşmasıyla ilişkisini korur."},"facet_ids":["F002"],"text":"doğumda kuyruk kökü çevresinin açılması","usage_role":"explanatory"}],"definition":"İnsan veya dört ayaklı bir hayvanda sırtın orta bölümünü ve özellikle kuyruk kökünün iki yanını kapsayan anatomik bölgedir. Dişide doğum sırasında bu bölgenin açılması ve yavrunun oraya inerek doğumun yaklaşması, bölgeye bağlı durumlardır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan ve dört ayaklılarda sırtın orta bölümü ile kuyruk kökünün iki yanı adlandırılır."},{"facet_id":"F002","role":"associated_use","statement":"Dişinin doğumunda bu bölge açılır; devede yavrunun buraya inmesi doğumun yaklaştığını gösterir."}],"identity_rationale":"Kaynak ifadesi hem insan ve dört ayaklılarda sırtın orta bölümünü hem de kuyruğun iki yanındaki bölgeleri belirtir; dişinin doğumunda bu bölgenin açılması ve devenin doğuma yaklaşması da açıkça desteklenir.","lexical_glosses":[{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"sırtın orta bölümü veya kuyruk kökünün iki yanı"},{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"kuyruk kökünün iki yanı"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"doğum sırasında kuyruk kökü çevresinin açılması"}],"lexicalization_note":"Yalın anatomik adlar temel alınır; doğum sırasında bölgenin açılması ve devenin doğuma yaklaşması yalnız ilgili kuruluşlarda korunur.","neighbor_coverage_note":"Tam eşleşen komşu dal yayımlandı; diğer adaylar sırt, kuyruk sokumu, yan bölge veya doğumdaki gevşeme gibi yalnız tek bir parçayı paylaşır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sunulan kartlarda anatomik yer veya doğuma bağlı durum bakımından anlamlı bir kapsam farkı yoktur.","focus_only":null,"gloss":"sırtın ortası ve kuyruk kökü çevresi","neighbor_only":null,"neighbor_ref":"root_000880/B006","relation_type":"synonym","shared_zone":"İki dal da sırtın orta bölgesini, kuyruğun iki yanını ve bu bölgenin doğum sırasında açılmasını kapsar."}],"source_phrase_ar":"الصلا وسط الظهر لكل ذي أربع وللناس (ayn); كل أنثى إذا ولدت انفرج صلاها (ayn); الصلوين وهما مكتنفا الذنب من الناقة وغيرها (tahdhib); أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها وقرب نتاجها (tahdhib)","source_summary":"Ortak anlatım sırtın ortası ile kuyruk kökünün iki yanındaki anatomik bölgeyi tanımlar; doğum sırasında açılmayı ve yavrunun bu bölgeye inmesini ona bağlı durumlar olarak verir.","sources":["AY","TA"],"what_is_ar":"يدخل فيه وسط الظهر ومكتنفا الذنب وجانبا صلا الحيوان وما يتصل بولادة الأنثى عند انفرج الصلا","what_is_not_ar":"ليس الصلاة ولا النار ولا المصلي في السباق إلا من جهة الاشتقاق"},"support_links":[]},{"boundary":"Genel olarak önde gitme değil, birincinin hemen ardındaki ikinci sıra ve bu yakın takip konumu tanımlanır.","branch_kind":"mixed_non_bare","branch_ref":"root_000879/B006","candidate_links":[{"candidate_id":"cand_2c30bbf16a55841ccfd5","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"yarışta birincinin hemen ardındaki ikinci","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yarışmacı, birincinin hemen ardından gelerek yarışı ikinci sırada sürdürür veya bitirir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"At yarışında ikinci atın başı, öndeki atın kuyruk kökü hizasına gelecek kadar onu yakından izler."}}],"root_ar":"ص ل و","root_id":"root_000879","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Özellikle at yarışında lideri yakından izleyen ve sıralamada ikinci olan yarışmacıyı belirtir.","boundary_detail":"Genel olarak önde gitme değil, birincinin hemen ardındaki ikinci sıra ve bu yakın takip konumu tanımlanır.","branch_image_ar":"تلو السابق في السباق","concept_gloss":"yarışta birincinin hemen ardındaki ikinci","contextual_glosses":[{"applicability":"Atın bir yarışta öndeki atı yakından izleyerek ikinci sırada geldiğini anlatan eylem bağlamına uygundur.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yarış eylemini, ikinci sırayı ve liderin hemen ardından gelme ilişkisini eksiksiz korur."},"facet_ids":["F001","F002"],"text":"liderin hemen ardından ikinci gelmek","usage_role":"contextual"}],"definition":"Bir yarışta birincinin hemen ardından gelen ikinci yarışmacıdır; özellikle at yarışında başının öndeki atın kuyruk kökü hizasına gelmesi bu adı açıklayan yakın takip konumudur.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yarışmacı, birincinin hemen ardından gelerek yarışı ikinci sırada sürdürür veya bitirir."},{"facet_id":"F002","role":"associated_use","statement":"At yarışında ikinci atın başı, öndeki atın kuyruk kökü hizasına gelecek kadar onu yakından izler."}],"identity_rationale":"Kaynak ifadesi yarışta birincinin ardından gelen ikinciyi ve atın başının öndeki atın kuyruk kökü hizasına gelmesini adlandırmanın nedeni olarak açıkça belirtir.","lexical_glosses":[{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"yarışta birincinin ardından gelen ikinci"},{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"yarışta liderin hemen ardından ikinci gelmek"}],"lexicalization_note":"Yalın yarışçı adı ikinci sırayı belirtir; atın bu konumda gelmesini anlatan eylem yalnız ilgili kuruluşta tutulur.","neighbor_coverage_note":"Tam eşleşen dal ile ikinci ve sonuncu sıra karşıtlığını gösteren aday yayımlandı; diğerleri yarış, hız veya başlangıç düzenini paylaşsa da aynı sıra adını karşılamaz.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sunulan kartlarda sıra, katılımcı veya yakın takip koşulu bakımından bir sınır farkı bulunmaz.","focus_only":null,"gloss":"yarışta lideri izleyen ikinci","neighbor_only":null,"neighbor_ref":"root_000880/B007","relation_type":"synonym","shared_zone":"İki dal da yarışta birincinin hemen ardında bulunan ikinciyi ve atın başının öndeki atın kuyruk kökünü izlemesini tanımlar."},{"boundary_match":"field_only","distinction":"Odak dal liderin hemen ardındaki ikinciyi, komşu dal ise grubun en sonunda gelen atı belirtir; aynı yarış alanında karşıt uçlarda yer alırlar.","focus_only":"Birincinin hemen ardından gelen ikinci yarışmacıyı belirtir.","gloss":"yarışın sonundaki at","neighbor_only":"Yarış grubunun sonunda, bazı düzenlerde onuncu sırada gelen atı belirtir.","neighbor_ref":"root_000724/B006","relation_type":"same_field","shared_zone":"Her iki dal da at yarışındaki bitiriş sırasına göre belirlenen bir yarışmacıyı adlandırır."}],"source_phrase_ar":"قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه (ayn); المصلى تالي السابق (sihah); السابق الأول والمصلي الثاني (tahdhib); يكون عند صلا الأول (tahdhib)","source_summary":"Ortak anlatım yarıştaki ikinciyi, birincinin hemen ardındaki yarışmacı olarak tanımlar ve atın başının öndeki atın kuyruk kökü hizasında bulunmasını adın gerekçesi sayar.","sources":["AY","SI","TA"],"what_is_ar":"يدخل فيه المصلي من الخيل أو السابق الثاني الذي يأتي رأسه عند صلا السابق","what_is_not_ar":"ليس مطلق السبق ولا الصلاة ولا الشرك المنصوبة"},"support_links":["sup_d5df39040aa9e211758c"]},{"boundary":"Eylemin kendisi değil, tapınmaya ayrılmış yer adlandırılır; topluluğa özgü kilise kullanımı genel yer anlamına bağlıdır.","branch_kind":"bare","branch_ref":"root_000879/B007","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"tapınma yeri; kilise","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Bir din topluluğunun topluca veya düzenli biçimde tapındığı yer adlandırılır."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Ad özellikle Yahudilerin kiliseleri için verilir; bazı anlatımlarda Sabiilerin tapınma yerlerine de uygulanır."}}],"root_ar":"ص ل و","root_id":"root_000879","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel tapınma yeri anlamını ve özellikle belirli din topluluklarının kiliseleri için kullanılan yer adını birlikte karşılar.","boundary_detail":"Eylemin kendisi değil, tapınmaya ayrılmış yer adlandırılır; topluluğa özgü kilise kullanımı genel yer anlamına bağlıdır.","branch_image_ar":"مواضع الصلاة ودور العبادة","concept_gloss":"tapınma yeri; kilise","contextual_glosses":[{"applicability":"Çoğul biçimin özellikle Yahudi topluluğunun kiliselerini adlandırdığı tarihsel bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Genel tapınma yeri anlamını ve Sabiilerin tapınma yerlerine uzanan aktarımı dışarıda bırakır.","preserves":"Belirli bir topluluğa ait kiliseleri ve bunların tapınma yeri oluşunu korur."},"facet_ids":["F002"],"text":"Yahudilerin kiliseleri","usage_role":"contextual"}],"definition":"Bir topluluğun tapınmasına ayrılmış yerin adıdır; özellikle Yahudilerin kiliseleri için kullanılır, bazı anlatımlarda Sabiilerin tapınma yerlerini de kapsar.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Bir din topluluğunun topluca veya düzenli biçimde tapındığı yer adlandırılır."},{"facet_id":"F002","role":"source_variant","statement":"Ad özellikle Yahudilerin kiliseleri için verilir; bazı anlatımlarda Sabiilerin tapınma yerlerine de uygulanır."}],"identity_rationale":"Kaynak ifadesi sözcüğü bir din topluluğunun kiliseleri, başka bir topluluğun tapınma yerleri ve daha genel olarak tapınma yeri adı şeklinde verir; sağlanan çerçeve bu çeşitliliği doğru yansıtır.","lexical_glosses":[{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"Yahudilerin kiliseleri veya bir din topluluğunun tapınma yerleri"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"tapınma yeri"}],"lexicalization_note":"Dal yalnız yalın yer adlarını içerir ve başka dallardaki tapınma eylemi ya da dilek anlamlarını tanıma katmaz.","neighbor_coverage_note":"Tam eşleşen komşu dal yayımlandı; diğer adaylar kilisenin belirli bir türünü, tapınma yerindeki kişiyi veya genel din alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sunulan kartlar yer türü, topluluklara uzanım veya eylem ile yer ayrımı bakımından bir sınır farkı göstermez.","focus_only":null,"gloss":"tapınma yerleri ve kiliseler","neighbor_only":null,"neighbor_ref":"root_000880/B008","relation_type":"synonym","shared_zone":"İki dal da tapınma yerini, özellikle Yahudilerin kiliselerini ve bazı anlatımlarda Sabiilerin tapınma yerlerini kapsar."}],"source_phrase_ar":"صلوات اليهود كنائسهم واحدها صلاة (ayn); الصلوات كنائس اليهود (tahdhib); قيل إنها مواضع صلوات الصابئين (tahdhib); يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)","source_summary":"Ortak anlatım sözcüğü tapınma yeri adı olarak açıklar; topluluğa özgü kullanım Yahudi kiliselerini öne çıkarırken başka bir aktarım Sabiilerin tapınma yerlerini de kapsar.","sources":["AY","TA","MU"],"what_is_ar":"يدخل فيه الصلوات بمعنى كنائس اليهود أو مواضع صلوات الصابئين واسم موضع العبادة","what_is_not_ar":"ليست فعل الصلاة ولا الدعاء ولا الرحمة"},"support_links":[]},{"boundary":"Çekirdek, malzemenin üstünde dövüldüğü geniş taş yüzeyidir; genel olarak her taş veya her dövme aracı kastedilmez.","branch_kind":"bare","branch_ref":"root_000879/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"üzerinde dövme yapılan geniş taş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Geniş ve sert bir taş, malzemenin üstünde dövülüp ezildiği çalışma yüzeyi olarak kullanılır."}},{"facet_id":"F002","role":"example","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Taşın üzerinde güzel kokulu maddeler veya kurutulmuş yemiş dövülebilir."}},{"facet_id":"F003","role":"source_variant","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Nesne kaba ve kalın bir taş levha görünümüyle de betimlenir."}}],"root_ar":"ص ل و","root_id":"root_000879","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Malzemenin içine değil üstüne konup dövüldüğü geniş, sert ve çoğu kez kaba taş yüzeyi için kullanılır.","boundary_detail":"Çekirdek, malzemenin üstünde dövüldüğü geniş taş yüzeyidir; genel olarak her taş veya her dövme aracı kastedilmez.","branch_image_ar":"الصَّلاية حجر الدق","concept_gloss":"üzerinde dövme yapılan geniş taş","contextual_glosses":[{"applicability":"Güzel kokulu madde, kurutulmuş yemiş veya benzeri malzemenin üstünde ezildiği taş araç için doğal kısa karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Taşın malzemeyi dövüp ezmeye ayrılmış bir çalışma yüzeyi olmasını korur."},"facet_ids":["F001","F002"],"text":"dövme taşı","usage_role":"general"}],"definition":"Güzel kokulu maddeler veya kurutulmuş yemiş gibi malzemelerin üzerinde dövüldüğü geniş, kalın ve kaba taş yüzeyidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Geniş ve sert bir taş, malzemenin üstünde dövülüp ezildiği çalışma yüzeyi olarak kullanılır."},{"facet_id":"F002","role":"example","statement":"Taşın üzerinde güzel kokulu maddeler veya kurutulmuş yemiş dövülebilir."},{"facet_id":"F003","role":"source_variant","statement":"Nesne kaba ve kalın bir taş levha görünümüyle de betimlenir."}],"identity_rationale":"Kaynak ifadesi geniş bir dövme taşını, üzerinde güzel kokulu maddelerin veya kurutulmuş yemişin dövülmesini ve taşın kaba, kalın bir levha görünümünü açıkça destekler.","lexical_glosses":[{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"üzerinde malzeme dövülen geniş taş"},{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"dövme taşı"}],"lexicalization_note":"Dal yalın taş adlarıyla sınırlıdır; ateş, tapınma, anatomi veya yalnız başka bir araçta görülen dövme anlamları içeri alınmaz.","neighbor_coverage_note":"Tam eşleşen dal ve sık karışabilecek havan karşılaştırması yayımlandı; diğer adaylar yalnız geniş taş, sert taş veya belirli bir maddeyi dövme alanını paylaşır.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Komşu karttaki kaba ve geniş nesne benzetmesi, odak kaynağındaki kalın taş levha betiminden doğar ve temel sınırı değiştirmez.","focus_only":null,"gloss":"üzerinde malzeme dövülen geniş taş","neighbor_only":null,"neighbor_ref":"root_000880/B009","relation_type":"synonym","shared_zone":"İki dal da güzel kokulu madde veya kurutulmuş yemiş gibi malzemelerin üstünde dövüldüğü geniş ve kaba taşı tanımlar."},{"boundary_match":"partial","distinction":"Odak dal geniş taşın üst yüzeyini çalışma alanı yapar; komşu dal ise çoğunlukla malzemenin içine konduğu kap biçimli bir dövme aracıdır.","focus_only":"Malzemenin üstünde dövüldüğü geniş ve çoğunlukla düz bir taş yüzeyidir.","gloss":"havan","neighbor_only":"Malzemenin içine konarak dövüldüğü çukur kap biçimli aracı veya bazı anlatımlarda döven aracı belirtir.","neighbor_ref":"root_001608/B004","relation_type":"near_neighbor","shared_zone":"Her iki dal da bir malzemeyi vurarak ezme ve inceltme işinde kullanılan araçları adlandırır."}],"source_phrase_ar":"الصلاية الفهر (sihah); الصلاءة بالهمز مثله (sihah); الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib); الصلاية سريحة خشنة غليظة من القف (tahdhib)","source_summary":"Ortak anlatım, üzerinde malzeme dövülen geniş taşı tanımlar; güzel kokulu madde ve kurutulmuş yemiş örneklerini verir ve taşın kaba, kalın yüzeyini belirtir.","sources":["SI","TA"],"what_is_ar":"يدخل فيه الصلاية والصلاءة وهي حجر عريض أو فهر يدق عليه العطر أو الهبيد","what_is_not_ar":"ليس النار ولا الصلاة ولا الصَّلا من الظهر"},"support_links":[]},{"boundary":"Belirli bitki çekirdektir; develerin onu otlaması ve bu bitkinin yetiştiği arazi adı çekirdeğe bağlıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000879/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"iri başaklı, develerin otladığı bir bitki","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli bitki, kamış başına benzeyen iri bir başak veya belirgin bir tepe taşır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bitki develer tarafından otlanır ve onların yiyeceği sayılacak kadar bu hayvanlarla ilişkilendirilir."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bu bitkinin yetiştiği arazi, bitkinin varlığına göre ayrıca adlandırılır."}}],"root_ar":"ص ل و","root_id":"root_000879","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kamış başına benzeyen iri başağı veya tepesiyle ayırt edilen ve deve yemi olan belirli bitkiyi betimleyerek karşılar.","boundary_detail":"Belirli bitki çekirdektir; develerin onu otlaması ve bu bitkinin yetiştiği arazi adı çekirdeğe bağlıdır.","branch_image_ar":"الصِّليان نبت ترعاه الإبل","concept_gloss":"iri başaklı, develerin otladığı bir bitki","contextual_glosses":[{"applicability":"Arazinin söz konusu iri başaklı bitkiyi taşımasına göre adlandırıldığı yer bildiren kuruluşta kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"narrowing","loses":"Bitkinin kendisini, iri başaklı görünüşünü ve deve yemi oluşunu doğrudan adlandırmaz.","preserves":"Arazi ile orada yetişen belirli bitki arasındaki varlık ilişkisini korur."},"facet_ids":["F003"],"text":"bu bitkinin yetiştiği arazi","usage_role":"explanatory"}],"definition":"Kamış başına benzeyen iri bir başak veya tepe taşıyan ve develerin otladığı belirli bir bitkidir. Bu bitkinin yetiştiği araziyi belirten ad, bitki çekirdeğine bağlı bir yer kullanımıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli bitki, kamış başına benzeyen iri bir başak veya belirgin bir tepe taşır."},{"facet_id":"F002","role":"associated_use","statement":"Bitki develer tarafından otlanır ve onların yiyeceği sayılacak kadar bu hayvanlarla ilişkilendirilir."},{"facet_id":"F003","role":"extension","statement":"Bu bitkinin yetiştiği arazi, bitkinin varlığına göre ayrıca adlandırılır."}],"identity_rationale":"Kaynak ifadesi iri bir başak veya kamış başına benzeyen tepe taşıyan bitkiyi ve develerin onu otlaması nedeniyle verilen deve yiyeceği benzetmesini doğrular.","lexical_glosses":[{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"iri başaklı, develerin otladığı bir bitki"},{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"bu bitkinin yetiştiği arazi"}],"lexicalization_note":"Yalın biçim belirli bitkiyi adlandırır; o bitkinin bulunduğu arazi anlamı yalnız ilgili ad kuruluşuyla sınırlı tutulur.","neighbor_coverage_note":"Tam eşleşen komşu dal yayımlandı; diğer adaylar deve yemi, otlak veya benzer görünümlü bitki alanını paylaşır ancak aynı bitkiyi göstermez.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Sunulan kartlarda bitkinin görünüşü, otlayan hayvan veya kullanım kapsamı bakımından anlamlı bir sınır farkı yoktur.","focus_only":null,"gloss":"iri başaklı deve yemi bitkisi","neighbor_only":null,"neighbor_ref":"root_000880/B010","relation_type":"synonym","shared_zone":"İki dal da iri başağı veya tepesi bulunan, develerin otladığı ve onların yiyeceği sayılan aynı bitkiyi tanımlar."}],"source_phrase_ar":"الصليان نبت (ayn;tahdhib); له سنمة عظيمة كأنها رأس القصبة (ayn); له سبطة عظيمة كأنها رأس القصبة (tahdhib); تسميها العرب خبزة الإبل (ayn;tahdhib)","source_summary":"Ortak anlatım iri başaklı veya tepeli belirli bir bitkiyi tanımlar, kamış başına benzeyen görünüşünü belirtir ve develerin onu otlamasıyla kurulan yiyecek ilişkisini aktarır.","sources":["AY","TA"],"what_is_ar":"يدخل فيه الصليان وهو نبت له سنمة أو سبطة عظيمة وتسمية العرب له خبزة الإبل","what_is_not_ar":"ليس الصلاة ولا النار ولا الصلاية"},"support_links":[]},{"boundary":"Dal yalnızca belirli kuralları ve beden hareketleri olan tapınmayı kapsar; yalın yakarışı kapsamaz.","branch_kind":"bare","branch_ref":"root_000880/B001","candidate_links":[{"candidate_id":"cand_ff16b8e41fc921d3adfe","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"ayakta durma, eğilme ve yere kapanmalı yükümlü tapınma","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Belirli beden duruşları, yakarış ve yüceltme içeren özel ve yükümlü tapınmadır."}}],"root_ar":"ص ل و","root_id":"root_000880","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli beden hareketleriyle yerine getirilen özel ve yükümlü tapınmanın bütün çekirdeğini karşılar.","boundary_detail":"Dal yalnızca belirli kuralları ve beden hareketleri olan tapınmayı kapsar; yalın yakarışı kapsamaz.","branch_image_ar":"الصلاة عبادة لازمة","concept_gloss":"ayakta durma, eğilme ve yere kapanmalı yükümlü tapınma","contextual_glosses":[{"applicability":"Türkçede bu belirli ve kurallı tapınma eyleminin doğal bağlamsal karşılığıdır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Belirli duruşları olan özel tapınmayı doğal kullanım içinde korur."},"facet_ids":["F001"],"text":"namaz","usage_role":"contextual"}],"definition":"Ayakta durma, belden eğilme ve yere kapanma gibi belirli bölümlerle yerine getirilen, sınırları konmuş yükümlü bir tapınmadır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Belirli beden duruşları, yakarış ve yüceltme içeren özel ve yükümlü tapınmadır."}],"identity_rationale":"Kaynak sözü bu dalı, ayakta durma, belden eğilme, yere kapanma, yakarış ve yüceltme gibi belirli bölümleri olan yükümlü tapınma olarak açıkça tanımlar. Bu nedenle dal, yalın bir iyilik dileğinden ve kökün öteki anlamlarından ayrı tutulur.","lexical_glosses":[{"lexical_unit_id":"lu_001","rendering_kind":"ordinary","target_gloss":"ayakta durma, eğilme ve yere kapanma bölümleri olan yükümlü tapınma"}],"lexicalization_note":"Tanım yalın biçimin özel tapınma anlamıyla sınırlıdır ve başka yapılara bağlı anlamları içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; tam örtüşen dal en yararlı sınır karşılaştırması olarak yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve sınırlar örtüşür; iki dal da genel tapınmayı değil, belirli hareketlerle yerine getirilen özel eylemi gösterir.","focus_only":null,"gloss":"belirli kurallı tapınma","neighbor_only":null,"neighbor_ref":"root_000879/B003","relation_type":"synonym","shared_zone":"Her iki dal da ayakta durma, eğilme ve yere kapanma bölümleri olan özel tapınmayı anlatır."}],"source_phrase_ar":"الصلاة التي جاء بها الشرع من الركوع والسجود (maqayis)؛ الصلاة واحدة الصلوات المفروضة (sihah)؛ الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib)؛ الصلاة التي هي العبادة المخصوصة (mufradat)","source_summary":"Kaynakların ortak çekirdeği, bu eylemin belirli kuralları bulunan ve ayakta durma, eğilme ile yere kapanmayı içeren özel bir tapınma oluşudur.","sources":["MQ","SI","TA","MU"],"what_is_ar":"الصلاة المفروضة وما فيها من قيام وركوع وسجود وإقامة","what_is_not_ar":"ليست دعاء مجردا؛ وليست صليا بالنار؛ وليست موضعا ولا كنيسة"},"support_links":["sup_3330730bb67908045dee"]},{"boundary":"Bu dal belirli beden hareketleri olan tapınmayı değil, yöneltilmiş dilek, övgü, esirgeme ve aklamayı kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000880/B002","candidate_links":[{"candidate_id":"cand_a8fe65f7aa32df6c2599","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"iyilik dileme; özneye göre esirgeme, övme veya aklama","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İnsan sözünde bir başkasına yöneltilen iyilik dileği ve güzel anmadır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Göksel görevlilere yüklendiğinde iyilik ve bağışlanma dileme anlamına gelir."}},{"facet_id":"F003","role":"specialization","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Tanrı'ya yüklendiğinde esirgeme, övme ve aklama anlamına gelir."}}],"root_ar":"ص ل و","root_id":"root_000880","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan, göksel görevli ve Tanrı bakımından değişen katılımcı ayrımlarının tümünü birlikte karşılar.","boundary_detail":"Bu dal belirli beden hareketleri olan tapınmayı değil, yöneltilmiş dilek, övgü, esirgeme ve aklamayı kapsar.","branch_image_ar":"الدعاء والبركة والرحمة","concept_gloss":"iyilik dileme; özneye göre esirgeme, övme veya aklama","contextual_glosses":[{"applicability":"Bir insanın başka bir kişiye yönelttiği dilek ve güzel anma bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İnsan sözündeki yöneltilmiş iyilik dileğini ve güzel anmayı korur."},"facet_ids":["F001"],"text":"onun için iyilik dilemek","usage_role":"contextual"},{"applicability":"Eylemin Tanrı'ya yüklendiği bağlamdaki özel anlamı açıklar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tanrı'ya yüklenen esirgeme, övme ve aklama yönlerini korur."},"facet_ids":["F003"],"text":"onu esirgemek, övmek ve aklamak","usage_role":"explanatory"}],"definition":"Bir başkası için iyilik dileme anlamındadır; eylemi yapana göre bağışlanma dileme, esirgeme, övme ya da aklama biçimini alır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İnsan sözünde bir başkasına yöneltilen iyilik dileği ve güzel anmadır."},{"facet_id":"F002","role":"specialization","statement":"Göksel görevlilere yüklendiğinde iyilik ve bağışlanma dileme anlamına gelir."},{"facet_id":"F003","role":"specialization","statement":"Tanrı'ya yüklendiğinde esirgeme, övme ve aklama anlamına gelir."}],"identity_rationale":"Kaynak sözü, anlamın eylemi yapana göre değiştiğini açıkça gösterir: insanlar başkaları için iyilik diler, göksel görevliler bağışlanma diler, Tanrı ise esirger, över ve aklar. Dalın çok katmanlı çerçevesi bu katılımcı ayrımını doğru biçimde taşır.","lexical_glosses":[{"lexical_unit_id":"lu_002","rendering_kind":"ordinary","target_gloss":"iyilik dileme; özneye göre esirgeme, övme veya bağışlanma isteme"},{"lexical_unit_id":"lu_003","rendering_kind":"ordinary","target_gloss":"onun için iyilik dilemek, onu esirgemek ya da aklamak"},{"lexical_unit_id":"lu_004","rendering_kind":"ordinary","target_gloss":"Tanrı'nın kullarını esirgemesi, övmesi veya aklaması"},{"lexical_unit_id":"lu_005","rendering_kind":"ordinary","target_gloss":"göksel görevlilerin iyilik ve bağışlanma dilemesi"},{"lexical_unit_id":"lu_006","rendering_kind":"ordinary","target_gloss":"ölen kişi için iyilik dileme"}],"lexicalization_note":"Yalın anlam ile kime yöneltildiği ve kime yüklendiği belirli yapılara bağlı anlamlar ayrı katmanlar halinde tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı katılımcı ayrımlarını taşıyan tam karşılık yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve katılımcı sınırları örtüşür; ikisi de belirli tapınma eyleminden ayrı olan yöneltilmiş söz ve esirgeme alanını gösterir.","focus_only":null,"gloss":"iyilik dileme, esirgeme ve övme","neighbor_only":null,"neighbor_ref":"root_000879/B002","relation_type":"synonym","shared_zone":"Her iki dal da iyilik dileğini ve özneye göre esirgeme, övme, aklama ya da bağışlanma dileme ayrımını kapsar."}],"source_phrase_ar":"الصلاة وهي الدعاء (maqayis)؛ صلوات الرسول للمسلمين دعاؤه لهم وذكرهم (ayn)؛ الصلاة من الله تعالى الرحمة (sihah)؛ الصلاة من الملائكة دعاء واستغفار ومن الله سبحانه رحمة (tahdhib)؛ الصلاة الدعاء والتبريك والتمجيد (mufradat)","source_summary":"Ortak anlatım, başkasına yönelen iyilik dileğini temel alır ve konuşan özneye göre bağışlanma dileme, esirgeme, övme ya da aklama yönlerinin öne çıktığını belirtir.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"الدعاء للغير والتبريك والثناء والرحمة والاستغفار المنسوب إلى الله أو الملائكة أو الناس","what_is_not_ar":"ليست هيئة الصلاة المفروضة؛ وليست الصلي بالنار؛ وليست كنائس اليهود"},"support_links":["sup_2589583ad8cbc5c8f0a8"]},{"boundary":"Anlam ateş ya da ateşe benzetilen ağır durumla kurulan yapılara bağlıdır; yalın ve sınırsız bir kök anlamı değildir.","branch_kind":"collocation","branch_ref":"root_000880/B003","candidate_links":[{"candidate_id":"cand_178a29fa5ddeaa3c187c","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"ateşin veya benzer bir sıkıntının şiddetine uğramak; birini ateşe sokmak","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ateşe girmek, onda kalmak ve yakıcı şiddetine uğramaktır."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir başkasını ateşe sokup bu şiddete uğratmaktır."}},{"facet_id":"F003","role":"extension","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Ateşe benzetilen ağır bir işin veya kötülüğün sıkıntısını çekmektir."}}],"root_ar":"ص ل و","root_id":"root_000880","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Ateşle kurulan edilgen, ettirgen ve benzetmeli yapıların ortak anlam alanını kapsar.","boundary_detail":"Anlam ateş ya da ateşe benzetilen ağır durumla kurulan yapılara bağlıdır; yalın ve sınırsız bir kök anlamı değildir.","branch_image_ar":"ملاقاة النار وحرها","concept_gloss":"ateşin veya benzer bir sıkıntının şiddetine uğramak; birini ateşe sokmak","contextual_glosses":[{"applicability":"Bir kişinin ateşe girdiği, onda kaldığı veya yandığı doğrudan bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Ateşle doğrudan karşılaşmayı, içinde kalmayı ve yakıcı şiddeti çekmeyi korur."},"facet_ids":["F001"],"text":"ateşe girip yakıcı sıcağını çekmek","usage_role":"contextual"},{"applicability":"Ateş benzetmesiyle ağır bir işin veya kötülüğün çekildiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Yakıcı şiddetin ağır sıkıntıya aktarılan benzetmeli uzantısını korur."},"facet_ids":["F003"],"text":"bir sıkıntının ağırlığını çekmek","usage_role":"contextual"}],"definition":"Ateşe girip onda kalmak, ısısını ve şiddetini çekmek ya da bir başkasını ateşe sokmaktır; benzetmeli kullanımda ağır bir durumun sıkıntısını çekmeyi anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ateşe girmek, onda kalmak ve yakıcı şiddetine uğramaktır."},{"facet_id":"F002","role":"specialization","statement":"Bir başkasını ateşe sokup bu şiddete uğratmaktır."},{"facet_id":"F003","role":"extension","statement":"Ateşe benzetilen ağır bir işin veya kötülüğün sıkıntısını çekmektir."}],"identity_rationale":"Kaynak sözü ateşe girme, ateşte kalma, ısısını ve şiddetini çekme ile birini ateşe sokma ilişkilerini birlikte destekler; benzer biçimde ağır bir duruma uğrama da buna bağlı bir uzantıdır. Dal, ateşle nesne pişirme veya düzeltme eyleminden ayrıdır.","lexical_glosses":[{"lexical_unit_id":"lu_007","rendering_kind":"ordinary","target_gloss":"ateşe girip yakıcı sıcağını çekmek"},{"lexical_unit_id":"lu_008","rendering_kind":"ordinary","target_gloss":"onu ateşe sokmak"},{"lexical_unit_id":"lu_009","rendering_kind":"ordinary","target_gloss":"ateşin başında ısınmak"},{"lexical_unit_id":"lu_010","rendering_kind":"ordinary","target_gloss":"bir işin ağır sıkıntısını çekmek"},{"lexical_unit_id":"lu_011","rendering_kind":"ordinary","target_gloss":"birinin kötülüğüne uğramak"},{"lexical_unit_id":"lu_012","rendering_kind":"ordinary","target_gloss":"onun sertliğini ve gücünü göze alamamak"}],"lexicalization_note":"Tanım yalnızca ateş, ısı veya benzetilen ağır durumla kurulan yapılara bağlanır ve yalın köke genellenmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ateş alanını daha geniş tutan komşu, en açıklayıcı kısmi karşılaştırmadır.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal ateşin şiddetine uğrayan veya uğratılan katılımcıya bağlı yapılardır; komşu dal ise ateşin yakıt ve pişirme işlevlerini de kapsadığı için daha geniştir.","focus_only":"Odak dal, ateşte kalmayı ve birini ateşe sokmayı ayrı katılımcı yönleriyle belirginleştirir.","gloss":"ateşin şiddetine uğrama","neighbor_only":"Komşu dal yakıtı, ateş yakmayı ve ateşte yiyecek pişirmeyi de aynı geniş alan içinde toplar.","neighbor_ref":"root_000879/B001","relation_type":"near_synonym","shared_zone":"Her iki dal da ateşle karşılaşmayı, yakıcı sıcaklığı çekmeyi ve bundan doğan ağır durumu kapsar."}],"source_phrase_ar":"أحدهما النار وما أشبهها من الحمى (maqayis)؛ صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها (ayn)؛ صلي الرجل نارا إذا أدخلته النار (sihah)؛ من يصلى في النار أي يلزم النار (tahdhib)؛ صلي بالنار وبكذا أي بلي بها واصطلى بها (mufradat)","source_summary":"Kaynaklar ateşin içine girme, onda kalma ve yakıcı şiddetini çekme çekirdeğinde birleşir; ettirgen kullanım bir başkasını ateşe sokar, benzetmeli kullanım ise ağır sıkıntıya uğramayı anlatır.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"صلي النار واصطلى بها وقاسى حرها أو دخلها وأصلاه غيره فيها","what_is_not_ar":"ليس شوي اللحم ولا تثقيف العصا على النار؛ وليس الصلاة عبادة"},"support_links":["sup_1b8122426ce82bb829c9"]},{"boundary":"Yalın yakıt ve pişmiş yiyecek adları, eti pişirme ve değneği düzeltme yapılarından ayrı facetler olarak tutulur.","branch_kind":"mixed_non_bare","branch_ref":"root_000880/B004","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"ateş yakıtı; ateşte pişirme veya ısıyla düzeltme","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Ateşi tutuşturmak ve sürdürmek için kullanılan yakıt ya da ateşin kendisidir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Eti ateşte pişirme eylemi ve ateşte pişmiş yiyecektir."}},{"facet_id":"F003","role":"associated_use","source_fields":["distinctive_facets[F003]"],"statements":{"statement":"Bir değneği ateş üzerinde döndürerek yumuşatıp düzeltme işlemidir."}}],"root_ar":"ص ل و","root_id":"root_000880","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yalın nesne anlamlarıyla ateşe bağlı iki ayrı işlem türünün ortak kapsamını verir.","boundary_detail":"Yalın yakıt ve pişmiş yiyecek adları, eti pişirme ve değneği düzeltme yapılarından ayrı facetler olarak tutulur.","branch_image_ar":"إيقاد الصلاء وتسوية الشيء بالنار","concept_gloss":"ateş yakıtı; ateşte pişirme veya ısıyla düzeltme","contextual_glosses":[{"applicability":"Et veya hayvan gövdesinin ateşle pişirildiği yapıda doğal karşılıktır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Etin ateşle pişirilmesi işlemini ve sonucunu korur."},"facet_ids":["F002"],"text":"eti ateşte pişirmek","usage_role":"contextual"},{"applicability":"Değneğin ateş üstünde döndürülerek biçiminin düzeltildiği yapıyı açıklar.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Isıyla yumuşatma, döndürme ve doğrultma aşamalarını korur."},"facet_ids":["F003"],"text":"değneği ateşte yumuşatıp doğrultmak","usage_role":"explanatory"}],"definition":"Yalın biçimlerde ateşi tutuşturan yakıtı veya ateşte pişmiş yiyeceği gösterir; belirli yapılarda eti ateşte pişirmeyi ve değneği ateş üstünde döndürerek yumuşatıp doğrultmayı anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Ateşi tutuşturmak ve sürdürmek için kullanılan yakıt ya da ateşin kendisidir."},{"facet_id":"F002","role":"specialization","statement":"Eti ateşte pişirme eylemi ve ateşte pişmiş yiyecektir."},{"facet_id":"F003","role":"associated_use","statement":"Bir değneği ateş üzerinde döndürerek yumuşatıp düzeltme işlemidir."}],"identity_rationale":"Kaynak sözü ateşi canlandıran yakıtı, ateşte pişmiş yiyeceği, eti ateşte pişirmeyi ve değneği ateş üzerinde döndürerek düzeltmeyi açıkça bir araya getirir. Bunlar ateşin şiddetine uğramaktan farklı olarak ateşten yararlanılan nesne ve işlemlerdir.","lexical_glosses":[{"lexical_unit_id":"lu_013","rendering_kind":"ordinary","target_gloss":"ateşi tutuşturan ve başında ısınılan yakıt"},{"lexical_unit_id":"lu_014","rendering_kind":"ordinary","target_gloss":"ateşte pişirilmiş yiyecek"},{"lexical_unit_id":"lu_015","rendering_kind":"ordinary","target_gloss":"odun ya da ateş"},{"lexical_unit_id":"lu_016","rendering_kind":"ordinary","target_gloss":"eti ateşte pişirmek"},{"lexical_unit_id":"lu_017","rendering_kind":"ordinary","target_gloss":"ateşte pişmiş"},{"lexical_unit_id":"lu_018","rendering_kind":"ordinary","target_gloss":"değneği ateş üstünde döndürerek yumuşatıp doğrultmak"},{"lexical_unit_id":"lu_019","rendering_kind":"ordinary","target_gloss":"ateşin üstüne kurulan ocak taşları"}],"lexicalization_note":"Tanım yalın yakıt ve pişmiş yiyecek anlamlarını, belirli nesnelerle kurulan pişirme ve düzeltme eylemlerinden ayırır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; ortak pişirme alanına rağmen sınırları farklı olan en yararlı komşu yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dalın çekirdeği yakıt ile et pişirme ve değnek düzeltme işlemleridir; komşu dalın araç, yer, ekmek pişirme ve ateşli sıcaklık kapsamı daha geniştir.","focus_only":"Odak dal değneği ateş üstünde döndürerek yumuşatıp doğrultmayı ve özel yakıt adını kapsar.","gloss":"ateşle pişirme ve ısıtma","neighbor_only":"Komşu dal ateşli sıcaklığı, ekmek pişirmeyi, pişirme araçlarını ve ateş yerini de kapsar.","neighbor_ref":"root_001122/B001","relation_type":"near_neighbor","shared_zone":"İki dal da ateş yakma, ateşin sıcaklığı ve yiyeceği ateşle pişirme alanlarında kesişir."}],"source_phrase_ar":"الصلاء ما يصطلى به وما يذكى به النار ويوقد (maqayis)؛ صليت اللحم صليا شويته (ayn;sihah;tahdhib)؛ صلى عصاه إذا أدارها على النار يثقفها (ayn;tahdhib)؛ الصلاء يقال للوقود وللشواء (mufradat)","source_summary":"Ortak anlatım, ateşi besleyen yakıtı ve ateşten yararlanarak yiyecek pişirme ya da değnek düzeltme işlemlerini kapsar; ateşe uğrayan kişinin yaşantısını anlatmaz.","sources":["MQ","AY","SI","TA","MU"],"what_is_ar":"إيقاد النار وما يصطلى به من الصلاء والوقود، وشوي اللحم، وإدارة العصا على النار لتقويمها","what_is_not_ar":"ليس دخول النار وعذابها؛ وليس الصلاة والدعاء"},"support_links":[]},{"boundary":"Dalın çekirdeği kurulan kapan nesnesidir; birine karşı yıkıcı düzen kurma yalnızca ayrı yapının lexical karşılığıdır.","branch_kind":"mixed_non_bare","branch_ref":"root_000880/B005","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"av yakalamak için kurulan kapan","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Avı veya başka bir canlıyı yakalamak için kurulan kapan nesnesidir."}}],"root_ar":"ص ل و","root_id":"root_000880","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Kuş veya başka canlılar için kurulan kapan nesnesinin tam çekirdeğini karşılar.","boundary_detail":"Dalın çekirdeği kurulan kapan nesnesidir; birine karşı yıkıcı düzen kurma yalnızca ayrı yapının lexical karşılığıdır.","branch_image_ar":"المَصالي أشراك وفخوخ","concept_gloss":"av yakalamak için kurulan kapan","contextual_glosses":[{"applicability":"Kapanın av veya başka bir canlı için yerleştirildiği eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Bir canlıyı yakalamak üzere kapan yerleştirme eylemini korur."},"facet_ids":["F001"],"text":"tuzak kurmak","usage_role":"contextual"}],"definition":"Kuşları veya başka canlıları yakalamak üzere kurulan tuzak ya da kapandır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Avı veya başka bir canlıyı yakalamak için kurulan kapan nesnesidir."}],"identity_rationale":"Kaynak sözü dalın çekirdeğini kuş veya başka canlıları yakalamak için kurulan kapanlar olarak açıkça belirler. Ayrı bir yapıda birini yok oluşa düşürmek üzere düzen kurma anlamı lexical düzeyde kalır ve kapan adının çekirdeğine katılmaz.","lexical_glosses":[{"lexical_unit_id":"lu_020","rendering_kind":"ordinary","target_gloss":"av veya zararlı canlılar için kurulan kapanlar"},{"lexical_unit_id":"lu_021","rendering_kind":"ordinary","target_gloss":"av yakalamak için kurulan kapan"},{"lexical_unit_id":"lu_022","rendering_kind":"ordinary","target_gloss":"birini yok oluşa düşürecek bir düzen kurmak"}],"lexicalization_note":"Yalın kapan adları dal tanımını kurar; yıkıcı düzen kuran özel yapı bunlara genellenmeden ayrı tutulur.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı kapan nesnesini gösteren tam karşılık yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve sınırlar örtüşür; iki dalın da konusu yakalanan av değil, onu yakalamak üzere kurulan kapan nesnesidir.","focus_only":null,"gloss":"kurulmuş av kapanı","neighbor_only":null,"neighbor_ref":"root_000879/B004","relation_type":"synonym","shared_zone":"Her iki dal da avı veya başka bir canlıyı yakalamak üzere kurulan kapanı anlatır."}],"source_phrase_ar":"مصالي هي الأشراك واحدتها مصلاة (maqayis)؛ المصلاة أن تنصب شركا ونحوه (ayn)؛ المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib)","source_summary":"Kaynakların ortak çekirdeği, kuşlar ve başka canlılar için kurulan, tuzağa benzeyen kapan nesnesidir.","sources":["MQ","AY","TA"],"what_is_ar":"المصالي أشراك وفخوخ تنصب للصيد أو للآفات","what_is_not_ar":"ليست صلاة العبادة؛ وليست مصلى السباق؛ وليست الصلاء النار"},"support_links":[]},{"boundary":"Beden bölümü çekirdektir; doğum sırasında açılma ve yavrunun bu bölgeye inmesi ona bağlı özel kullanımlardır.","branch_kind":"mixed_non_bare","branch_ref":"root_000880/B006","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"sırtın ortası ve kuyruk dibinin iki yanı","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Sırtın orta bölgesi ile kuyruk dibinin iki yanı ve kuyruk sokumu çevresidir."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Dişide doğum sırasında açılan ve yavrunun doğum yaklaşınca indiği beden bölgesidir."}}],"root_ar":"ص ل و","root_id":"root_000880","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"İnsan ve dört ayaklıların ilgili sırt ve kuyruk çevresi için temel beden bölümü karşılığıdır.","boundary_detail":"Beden bölümü çekirdektir; doğum sırasında açılma ve yavrunun bu bölgeye inmesi ona bağlı özel kullanımlardır.","branch_image_ar":"الصَّلا موضع الظهر والذنب","concept_gloss":"sırtın ortası ve kuyruk dibinin iki yanı","contextual_glosses":[{"applicability":"Dişinin doğumu sırasında bölgenin açıldığı veya yavrunun buraya indiği bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Beden bölgesini ve doğum sırasında geçirdiği açılma durumunu korur."},"facet_ids":["F002"],"text":"doğumda açılan kuyruk dibi bölgesi","usage_role":"explanatory"}],"definition":"İnsan veya dört ayaklılarda sırtın orta bölgesi ve özellikle kuyruk dibinin iki yanı ile kuyruk sokumu çevresidir; doğumda açılan ya da yavrunun indiği bölge olarak da anılır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Sırtın orta bölgesi ile kuyruk dibinin iki yanı ve kuyruk sokumu çevresidir."},{"facet_id":"F002","role":"associated_use","statement":"Dişide doğum sırasında açılan ve yavrunun doğum yaklaşınca indiği beden bölgesidir."}],"identity_rationale":"Kaynak sözü sırtın orta bölgesini, kuyruk dibinin iki yanını ve kuyruk sokumu çevresini aynı beden alanında toplar. Doğumda bu bölgenin açılması veya yavrunun buraya inmesi, beden bölümünün kendisine bağlı özel durumlardır.","lexical_glosses":[{"lexical_unit_id":"lu_023","rendering_kind":"ordinary","target_gloss":"sırtın ortası veya kuyruk dibi ile kuyruk sokumunun iki yanı"},{"lexical_unit_id":"lu_024","rendering_kind":"ordinary","target_gloss":"kuyruk dibinin iki yanı"},{"lexical_unit_id":"lu_025","rendering_kind":"ordinary","target_gloss":"doğumda kuyruk dibi bölgesinin açılması"},{"lexical_unit_id":"lu_026","rendering_kind":"ordinary","target_gloss":"devenin yavrusunun kuyruk dibi bölgesine inmesi ve doğumun yaklaşması"}],"lexicalization_note":"Yalın beden bölümü ile doğuma bağlı yapılardaki durumlar birbirine karıştırılmadan ayrı facetlerde tanımlanır.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; anatomi ve doğum sınırları bütünüyle örtüşen karşılık yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve sınırlar örtüşür; her ikisi de kuyruk sokumu çevresindeki beden bölümünü ve ona bağlı doğum durumunu gösterir.","focus_only":null,"gloss":"sırt ve kuyruk dibi bölgesi","neighbor_only":null,"neighbor_ref":"root_000879/B005","relation_type":"synonym","shared_zone":"Her iki dal da sırtın orta bölgesini, kuyruk dibinin iki yanını ve doğumla ilgili açılmayı kapsar."}],"source_phrase_ar":"الصلا وسط الظهر لكل ذي أربع وللناس (ayn)؛ انفرج صلاها (ayn)؛ الصلوين مكتنفا الذنب (tahdhib)؛ أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها (tahdhib)","source_summary":"Ortak anlatım sırtın ortası ile kuyruk dibi ve kuyruk sokumu çevresini gösterir; doğumla ilgili kullanımlar bu beden bölgesinin açılmasını veya yavrunun buraya inmesini belirtir.","sources":["AY","TA"],"what_is_ar":"الصلا وسط الظهر أو جانبا الذنب ومكتنفا العصعص، وما ينفرج عند الولادة أو يقع فيه الولد","what_is_not_ar":"ليس الصلاة عبادة؛ وليس الصلاء النار؛ وليس المصلي في السباق إلا على جهة الاشتقاق"},"support_links":[]},{"boundary":"Dal yalnızca yarışta önderin hemen ardındaki ikinci atı veya onun bu sıraya gelişini kapsar.","branch_kind":"mixed_non_bare","branch_ref":"root_000880/B007","candidate_links":[{"candidate_id":"cand_2c30bbf16a55841ccfd5","lane":"micro"}],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"yarışta önderin hemen ardındaki ikinci at","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Yarışta ilk atın hemen ardındaki ikinci attır."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Bir atın öndeki atın izinden gelerek ikinci sırayı almasıdır."}}],"root_ar":"ص ل و","root_id":"root_000880","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Yarış sırasındaki konumu, öndeki atla yakın izleme ilişkisini ve ikinci sırayı birlikte karşılar.","boundary_detail":"Dal yalnızca yarışta önderin hemen ardındaki ikinci atı veya onun bu sıraya gelişini kapsar.","branch_image_ar":"المصلي يتلو السابق","concept_gloss":"yarışta önderin hemen ardındaki ikinci at","contextual_glosses":[{"applicability":"Atın yarış içinde öndeki atı yakından izleyerek ikinci sıraya geldiği eylem bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Öndeki atı yakından izleme hareketini ve yarış sırasını korur."},"facet_ids":["F002"],"text":"önder atın hemen ardından gelmek","usage_role":"contextual"}],"definition":"Bir yarışta öndeki atın hemen ardından gelen ve ikinci sırada bulunan attır; ayrıca atın bu konuma gelmesini anlatır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Yarışta ilk atın hemen ardındaki ikinci attır."},{"facet_id":"F002","role":"associated_use","statement":"Bir atın öndeki atın izinden gelerek ikinci sırayı almasıdır."}],"identity_rationale":"Kaynak sözü yarıştaki ilk atın hemen ardından gelen atı ve özellikle ikinci sırayı açıkça belirtir. Adlandırmanın, izleyen atın başının öndeki atın kuyruk dibi hizasına gelmesiyle açıklanması dal sınırını destekler.","lexical_glosses":[{"lexical_unit_id":"lu_027","rendering_kind":"ordinary","target_gloss":"yarışta önderin hemen ardındaki ikinci at"},{"lexical_unit_id":"lu_028","rendering_kind":"ordinary","target_gloss":"atın önder atın hemen ardından gelmesi"}],"lexicalization_note":"Yarışçının adı ile atın önderin ardına gelmesini anlatan yapı ayrı tutulur ve genel koşma anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı yarış sırasını ve izleme ilişkisini veren tam karşılık yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve sınırlar örtüşür; her iki dalda da genel hız değil, öndeki atı hemen izleyen belirli sıra konumu kurucudur.","focus_only":null,"gloss":"yarıştaki ikinci at","neighbor_only":null,"neighbor_ref":"root_000879/B006","relation_type":"synonym","shared_zone":"Her iki dal da yarışta ilk atın hemen ardından gelen ve ikinci sırada bulunan atı gösterir."}],"source_phrase_ar":"أتى الفرس على أثر الفرس السابق قيل قد صلى وجاء مصليا (ayn)؛ المصلى تالي السابق (sihah)؛ السابق الأول والمصلي الثاني (tahdhib)","source_summary":"Kaynaklar, ilk atın izinden gelen ve başı öndeki atın kuyruk dibi hizasında bulunan ikinci at üzerinde birleşir.","sources":["AY","SI","TA"],"what_is_ar":"المصلي في السباق هو التالي للسابق أو الثاني لأن رأسه يلي صلا السابق","what_is_not_ar":"ليس المصلي في العبادة؛ وليس الصلاء النار؛ وليس الصلا موضعا مجردا"},"support_links":["sup_d5df39040aa9e211758c"]},{"boundary":"Dal, tapınma eyleminin kendisini değil, genel bir tapınma yerini ve özellikle Yahudilerin tapınma yapısını gösterir.","branch_kind":"bare","branch_ref":"root_000880/B008","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"tapınma yeri, özellikle Yahudi tapınağı","lexicon_identity_status":"reframed","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Tapınma eyleminin yapıldığı, bu amaçla adlandırılmış yerdir."}},{"facet_id":"F002","role":"specialization","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Özel kullanımda Yahudilerin tapınma yapısını gösterir."}}],"root_ar":"ص ل و","root_id":"root_000880","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Genel yer anlamını ve kaynakların belirttiği topluluğa özgü yapı kullanımını birlikte karşılar.","boundary_detail":"Dal, tapınma eyleminin kendisini değil, genel bir tapınma yerini ve özellikle Yahudilerin tapınma yapısını gösterir.","branch_image_ar":"الصلوات مواضع عبادة","concept_gloss":"tapınma yeri, özellikle Yahudi tapınağı","contextual_glosses":[{"applicability":"Sözcüğün Yahudilere ait tapınma yapısını gösterdiği özel bağlamda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Tapınma yapısını ve topluluğa özgü yer anlamını korur."},"facet_ids":["F002"],"text":"Yahudi tapınağı","usage_role":"contextual"}],"definition":"Tapınma için ayrılmış yer, özellikle Yahudilerin tapınma yapısıdır.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Tapınma eyleminin yapıldığı, bu amaçla adlandırılmış yerdir."},{"facet_id":"F002","role":"specialization","statement":"Özel kullanımda Yahudilerin tapınma yapısını gösterir."}],"identity_rationale":"Yetkili kaynak sözü genel olarak tapınma yerini ve özel olarak Yahudilerin tapınma yapılarını destekler. Geçici çerçevedeki başka bir topluluğa ait yapı ayrıntısı kaynak sözünde bulunmadığından tanım bu ek kapsam çıkarılarak yeniden kurulmuştur.","lexical_glosses":[{"lexical_unit_id":"lu_029","rendering_kind":"ordinary","target_gloss":"Yahudi tapınakları veya genel olarak tapınma yerleri"},{"lexical_unit_id":"lu_030","rendering_kind":"ordinary","target_gloss":"tapınma yeri"}],"lexicalization_note":"Tanım yalnızca yalın biçimin yer bildiren anlamına dayanır ve tapınma eylemini ya da başka yapı anlamlarını içeri almaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; geçici ek kapsamı görünür kılan kısmi karşılaştırma yayımlandı.","neighbor_distinctions":[{"boundary_match":"partial","distinction":"Odak dal yetkili kaynak sözünün desteklediği genel yer ve Yahudi tapınağı sınırında kalır; komşu kart doğrulanmayan ek topluluk kapsamıyla daha geniştir.","focus_only":null,"gloss":"tapınma yeri","neighbor_only":"Komşu kart, kaynak sözünün bu dal için doğrulamadığı başka bir topluluğun tapınma yerlerini de kapsar.","neighbor_ref":"root_000879/B007","relation_type":"near_synonym","shared_zone":"Her iki dal da tapınma için ayrılmış yerleri ve Yahudilerin tapınma yapılarını kapsar."}],"source_phrase_ar":"صلوات اليهود كنائسهم واحدها صلاة (ayn)؛ الصلوات كنائس اليهود (tahdhib)؛ يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)","source_summary":"Kaynaklar sözcüğün tapınma eyleminden yere aktarıldığını ve özellikle Yahudilerin tapınma yapıları için kullanıldığını bildirir.","sources":["AY","TA","MU"],"what_is_ar":"الصلوات مواضع عبادة أو كنائس اليهود والصابئين","what_is_not_ar":"ليست نفس فعل الصلاة؛ وليست النار؛ وليست أشراك المصالي"},"support_links":[]},{"boundary":"Dal, dövme işinin üzerinde yapıldığı geniş taşı gösterir; döven el aletini veya sıradan geniş taşı göstermez.","branch_kind":"bare","branch_ref":"root_000880/B009","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"üzerinde madde dövülen geniş taş","lexicon_identity_status":"accepted","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"Maddelerin üzerinde dövüldüğü geniş taş ya da taş yüzeydir."}},{"facet_id":"F002","role":"source_variant","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"İri, kalın ve pürüzlü bir taş görünümü için de kullanılır."}}],"root_ar":"ص ل و","root_id":"root_000880","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Dövme yüzeyi işlevini, taş malzemeyi ve geniş biçimi birlikte karşılar.","boundary_detail":"Dal, dövme işinin üzerinde yapıldığı geniş taşı gösterir; döven el aletini veya sıradan geniş taşı göstermez.","branch_image_ar":"الصلاية حجر يدق عليه","concept_gloss":"üzerinde madde dövülen geniş taş","contextual_glosses":[{"applicability":"Koku maddelerinin geniş bir taş üzerinde dövüldüğü araç bağlamında kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"Geniş taş yüzeyi ve koku maddesi dövme işlevini korur."},"facet_ids":["F001"],"text":"koku maddesi dövme taşı","usage_role":"contextual"}],"definition":"Üzerinde koku maddesi veya başka maddeler dövülen geniş, kimi kullanımda iri ve pürüzlü taş yüzeydir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"Maddelerin üzerinde dövüldüğü geniş taş ya da taş yüzeydir."},{"facet_id":"F002","role":"source_variant","statement":"İri, kalın ve pürüzlü bir taş görünümü için de kullanılır."}],"identity_rationale":"Kaynak sözü nesneyi, üzerinde koku maddesi veya başka maddeler dövülen geniş bir taş olarak tanımlar ve iri, pürüzlü taş görünümünü de destekler. Dalın araç ve biçim sınırı geçici çerçeveyle uyumludur.","lexical_glosses":[{"lexical_unit_id":"lu_031","rendering_kind":"ordinary","target_gloss":"üzerinde koku maddesi veya başka maddeler dövülen geniş taş"},{"lexical_unit_id":"lu_032","rendering_kind":"ordinary","target_gloss":"üzerinde madde dövülen geniş taş"}],"lexicalization_note":"Tanım yalın taş ve dövme yüzeyi anlamıyla sınırlıdır; başka taş adları ya da dövme eylemi içeri alınmaz.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı taş yüzeyi ve dövme işlevini taşıyan tam karşılık yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve sınırlar örtüşür; iki dal da döven el aletini değil, dövme işleminin yapıldığı geniş taş yüzeyi gösterir.","focus_only":null,"gloss":"geniş dövme taşı","neighbor_only":null,"neighbor_ref":"root_000879/B008","relation_type":"synonym","shared_zone":"Her iki dal da üzerinde koku maddesi veya başka maddeler dövülen geniş taşı anlatır."}],"source_phrase_ar":"الصلاية الفهر (sihah)؛ الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib)؛ الصلاية سريحة خشنة غليظة من القف (tahdhib)","source_summary":"Kaynak anlatımı, üzerinde özellikle koku maddeleri ve başka maddeler dövülen geniş taşı temel alır; ayrıca iri ve pürüzlü taş görünümünü belirtir.","sources":["SI","TA"],"what_is_ar":"الصلاية أو الصلاءة حجر عريض يدق عليه عطر أو هبيد ويشبه به الشيء العريض الخشن","what_is_not_ar":"ليست صلاة؛ وليست صلاء النار؛ وليست الصلا موضع الظهر"},"support_links":[]},{"boundary":"Dal iri başaklı belirli bitkidir; genel otlak veya develerin yediği bütün bitkiler bu dala girmez.","branch_kind":"mixed_non_bare","branch_ref":"root_000880/B010","candidate_links":[],"focus_root_occurrences":[{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","surface_ar":"مُصَلِّينَ"}],"gloss":"iri başaklı deve yemi bitkisi","lexicon_identity_status":"qualified","registry":"focus","review_facets":[{"facet_id":"F001","role":"core","source_fields":["distinctive_facets[F001]"],"statements":{"statement":"İri ve belirgin bir başağı olan belirli bir bitki türüdür."}},{"facet_id":"F002","role":"associated_use","source_fields":["distinctive_facets[F002]"],"statements":{"statement":"Develer için besin değeri, develerin ekmeği biçimindeki adlandırmayla anlatılır."}}],"root_ar":"ص ل و","root_id":"root_000880","root_occurrence_qualification":"These are focus-ayah occurrences mapped to the same root. They identify possible surface carriers but do not prove that this branch sense is active. Activation still requires an independent linguistic or contextual trigger.","semantic_detail":{"applicability":"Belirli bitkiyi, ayırt edici iri başağını ve develer için besin oluşunu birlikte karşılar.","boundary_detail":"Dal iri başaklı belirli bitkidir; genel otlak veya develerin yediği bütün bitkiler bu dala girmez.","branch_image_ar":"الصِّليان نبت ترعاه الإبل","concept_gloss":"iri başaklı deve yemi bitkisi","contextual_glosses":[{"applicability":"Bitkinin görünüşünün ve develer için besin değerinin birlikte açıklandığı bağlamlarda kullanılır.","error_profile":{"adds":null,"collision":null,"fit":"none","loses":null,"preserves":"İri başaklı bitkiyi ve develerle ilgili geleneksel adlandırmayı korur."},"facet_ids":["F001","F002"],"text":"develerin ekmeği denen iri başaklı bitki","usage_role":"explanatory"}],"definition":"İri bir başağı bulunan ve develer için besin sayıldığı için develerin ekmeği diye anılan belirli bir bitkidir.","distinctive_facets":[{"facet_id":"F001","role":"core","statement":"İri ve belirgin bir başağı olan belirli bir bitki türüdür."},{"facet_id":"F002","role":"associated_use","statement":"Develer için besin değeri, develerin ekmeği biçimindeki adlandırmayla anlatılır."}],"identity_rationale":"Kaynak sözü iri bir başağa sahip bitkiyi ve ona develerin ekmeği denmesini açıkça destekler. Geçici çerçevedeki develerin bu bitkiyi otladığı sonucu bu adlandırmadan anlaşılabilse de doğrudan söylenmediği için tanım bitkinin görünüşü ve deve yemi oluşuyla sınırlandırılmıştır.","lexical_glosses":[{"lexical_unit_id":"lu_033","rendering_kind":"ordinary","target_gloss":"iri başaklı, develere yem olan bitki"},{"lexical_unit_id":"lu_034","rendering_kind":"ordinary","target_gloss":"bu iri başaklı bitkinin yetiştiği yer"}],"lexicalization_note":"Yalın bitki adı çekirdektir; bu bitkinin bulunduğu yeri bildiren yapı ayrı tutulur ve genel otlak anlamına genişletilmez.","neighbor_coverage_note":"Bütün adaylar değerlendirildi; aynı bitkiyi ve deve yemi sınırını taşıyan tam karşılık yayımlandı.","neighbor_distinctions":[{"boundary_match":"exact","distinction":"Çekirdek ve sınırlar örtüşür; iki dal da genel otlağı değil, iri başağı ve develerle besin ilişkisi bulunan belirli bitkiyi gösterir.","focus_only":null,"gloss":"iri başaklı deve yemi bitkisi","neighbor_only":null,"neighbor_ref":"root_000879/B009","relation_type":"synonym","shared_zone":"Her iki dal da iri başaklı belirli bitkiyi ve develerin ekmeği biçimindeki adlandırmayı kapsar."}],"source_phrase_ar":"الصليان نبت على فعلان ويقال فعليان له سنمة عظيمة (ayn)؛ الصليان نبت له سبطة عظيمة (tahdhib)؛ تسميها العرب خبزة الإبل (ayn;tahdhib)","source_summary":"Kaynaklar bitkinin iri başağını ve develerle besin ilişkisini anlatan develerin ekmeği adlandırmasını birlikte verir.","sources":["AY","TA"],"what_is_ar":"الصليان نبت عظيم السنمة أو السنبلة ترعاه الإبل وتسمية العرب خبزة الإبل","what_is_not_ar":"ليس الصلاء الوقود؛ وليس الصلاة؛ وليس الصلا موضع الظهر"},"support_links":[]}],"candidate_inventory":[{"anchor_refs":["107:4:1"],"branch_refs":[],"candidate_id":"cand_ed77f05c333e400c797a","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:1:consequential-verdict-hinge","source_type":"word_analysis","support_ids":["sup_897b95d36f102d27e10c","sup_da7d9ddfca4f4e24cbc4"],"title":"consequence and resumption meet at the verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:1","qac_refs":["107:4:1:1"],"status":"accepted"}},{"anchor_refs":["107:4:1"],"branch_refs":[],"candidate_id":"cand_463d7ca7258f3d2360f3","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:1:prefixed-form-compression","source_type":"word_analysis","support_ids":["sup_10fe224ff868f119dcc2","sup_da7d9ddfca4f4e24cbc4"],"title":"prefixed particle fuses with the verdict noun","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:1","qac_refs":["107:4:1:1"],"status":"accepted"}},{"anchor_refs":["107:4:2"],"branch_refs":[],"candidate_id":"cand_9f35e6c94e75f43b9797","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:2:boundary-from-failed-urging","source_type":"word_analysis","support_ids":["sup_41a742133cf72d54b2bb","sup_7984107e8fed14ed38dd"],"title":"failed urging turns into condemnation","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:2","qac_refs":["107:4:1:2"],"status":"accepted"}},{"anchor_refs":["107:4:2"],"branch_refs":[],"candidate_id":"cand_e140a28a973b927d6d6b","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:2:doom-lament-destination-range","source_type":"word_analysis","support_ids":["sup_41a742133cf72d54b2bb","sup_f05901702d2a6d438754"],"title":"doom verdict carries lament and destination overtones","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:2","qac_refs":["107:4:1:2"],"status":"accepted"}},{"anchor_refs":["107:4:2"],"branch_refs":[],"candidate_id":"cand_c2f0acae70dfecc60fa7","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:2:formula-redirected-to-prayers","source_type":"word_analysis","support_ids":["sup_41a742133cf72d54b2bb","sup_6539c40f7c18e27a55f9"],"title":"familiar woe formula receives a surprising target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:2","qac_refs":["107:4:1:2"],"status":"accepted"}},{"anchor_refs":["107:4:2"],"branch_refs":[],"candidate_id":"cand_0f99a5c61d4bb07c4d3c","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:2:nominal-verdict-frame","source_type":"word_analysis","support_ids":["sup_41a742133cf72d54b2bb","sup_539d994a3c379cedf59b"],"title":"verbless noun performs the verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:2","qac_refs":["107:4:1:2"],"status":"accepted"}},{"anchor_refs":["107:4:2"],"branch_refs":[],"candidate_id":"cand_0b4d2bc69b1827fd4ead","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:2:sounded-lament-cadence","source_type":"word_analysis","support_ids":["sup_0a51a530b8c078bd84b2","sup_41a742133cf72d54b2bb"],"title":"sound texture reinforces the lament field","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:2","qac_refs":["107:4:1:2"],"status":"accepted"}},{"anchor_refs":["107:4:2"],"branch_refs":[],"candidate_id":"cand_41323375e79096a75b8a","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:2:unbounded-woe-definite-target","source_type":"word_analysis","support_ids":["sup_41a742133cf72d54b2bb","sup_822a57ebca2ac2f6b20b"],"title":"indefinite woe faces a definite class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:2","qac_refs":["107:4:1:2"],"status":"accepted"}},{"anchor_refs":["107:4:3"],"branch_refs":[],"candidate_id":"cand_aea48fe8ab5f4dcaafd0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:3:active-participle-habitual-agents","source_type":"word_analysis","support_ids":["sup_bdb95ce29241fbcc9886","sup_d421b4e7b918651aeab3"],"title":"participle names a practitioner-class","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:3","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"status":"accepted"}},{"anchor_refs":["107:4:3"],"branch_refs":[],"candidate_id":"cand_16cbfacff403b733b853","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:3:blocked-direct-burner-forms","source_type":"word_analysis","support_ids":["sup_6d9aa62bd64eb6856e6c","sup_d421b4e7b918651aeab3"],"title":"form blocks direct burner identity","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:3","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"status":"accepted"}},{"anchor_refs":["107:4:3"],"branch_refs":[],"candidate_id":"cand_203733bce1cbcbeb1850","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:3:case-locks-target-role","source_type":"word_analysis","support_ids":["sup_28f0970dd1600a6d39be","sup_d421b4e7b918651aeab3"],"title":"genitive case prevents independent-subject reading","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:3","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"status":"accepted"}},{"anchor_refs":["107:4:3"],"branch_refs":[],"candidate_id":"cand_8032a2b1d43cabee6974","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:3:contested-bending-following-imagery","source_type":"word_analysis","support_ids":["sup_084a98da2534039efce2","sup_d421b4e7b918651aeab3"],"title":"bending and following images sharpen the label","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:3","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"status":"accepted"}},{"anchor_refs":["107:4:3"],"branch_refs":[],"candidate_id":"cand_c8c26dfe60959833da72","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:3:convergent-central-knot","source_type":"word_analysis","support_ids":["sup_1268796efec0411fe858","sup_d421b4e7b918651aeab3"],"title":"form, root pressure, and qualifier converge","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:3","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"status":"accepted"}},{"anchor_refs":["107:4:3"],"branch_refs":[],"candidate_id":"cand_f2f953000ae0123b51e0","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:3:definite-class-forward-restriction","source_type":"word_analysis","support_ids":["sup_d421b4e7b918651aeab3","sup_ed308b21c650103a8990"],"title":"definite class waits for 107:5","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:3","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"status":"accepted"}},{"anchor_refs":["107:4:3"],"branch_refs":[],"candidate_id":"cand_2b0e8cc0c227fd581cb5","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:3:delayed-final-target-shock","source_type":"word_analysis","support_ids":["sup_d421b4e7b918651aeab3","sup_ffcc13d90748f9a1e771"],"title":"target lands after the verdict","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:3","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"status":"accepted"}},{"anchor_refs":["107:4:3"],"branch_refs":[],"candidate_id":"cand_dd280f2c345fc55df258","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:3:lam-governed-harmful-assignment","source_type":"word_analysis","support_ids":["sup_bd68533a8183b2cd7cdb","sup_d421b4e7b918651aeab3"],"title":"lām assigns the woe to its target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:3","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"status":"accepted"}},{"anchor_refs":["107:4:3"],"branch_refs":[],"candidate_id":"cand_1ee1519c5057e4978b23","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:3:li-al-compressed-target-form","source_type":"word_analysis","support_ids":["sup_d0e5e5204f142b68d94f","sup_d421b4e7b918651aeab3"],"title":"designation and definiteness compress into one form","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:3","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"status":"accepted"}},{"anchor_refs":["107:4:3"],"branch_refs":[],"candidate_id":"cand_60a2302b9fedb90a1b16","commentary_obligation":"must_integrate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:3:positive-prayer-label-under-woe","source_type":"word_analysis","support_ids":["sup_0c3caad04b8d27b8ede5","sup_d421b4e7b918651aeab3"],"title":"positive prayer label becomes the condemned target","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:3","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"status":"accepted"}},{"anchor_refs":["107:4:3"],"branch_refs":[],"candidate_id":"cand_302a556b2de1f53f272e","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:3:prior-portrait-receives-label","source_type":"word_analysis","support_ids":["sup_4d24bef18117339736d0","sup_d421b4e7b918651aeab3"],"title":"the definite plural names the prior portrait","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:3","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"status":"accepted"}},{"anchor_refs":["107:4:3"],"branch_refs":[],"candidate_id":"cand_a5e1f78392365385fb8b","commentary_obligation":"candidate","focus_branch_refs":[],"kind":"word_topic","lane":"micro","nominated_branch_refs":[],"root_ids":[],"scope":"focus_ayah","source_local_id":"107:4:3:root-family-prayer-fire-pressure","source_type":"word_analysis","support_ids":["sup_d421b4e7b918651aeab3","sup_e063eec84dbd7c73a4c2"],"title":"prayer sense carries fire-family pressure","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[],"word_alignment":{"analysis_ref":"107:4:3","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"status":"accepted"}},{"anchor_refs":["107:4:2"],"branch_refs":[],"candidate_id":"cand_cbee1cbd700fbf585fba","commentary_obligation":"ledger_only","focus_branch_refs":[],"kind":"focus_root_occurrence","lane":"micro","nominated_branch_refs":[],"root_ids":["root_000879","root_000880"],"scope":"focus_ayah","source_local_id":"107:4:2:3","source_type":"qac_morpheme","support_ids":["sup_6828497e1550eccdb302"],"title":"QAC root occurrence: ص ل و","trust":"trusted","unresolved_branch_citations":[],"unresolved_branch_refs":[]},{"anchor_refs":["107:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:4","branch_refs":["root_000879/B003","root_000880/B001"],"candidate_id":"cand_ff16b8e41fc921d3adfe","commentary_obligation":"review","hft_ref":"hft_f576cf65f7d2b162e188","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base-prescribed-insider-warning","source_type":"hft","support_ids":["sup_3330730bb67908045dee"],"title":"base-prescribed-insider-warning","trust":"legacy_unbound"},{"anchor_refs":["107:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:4","branch_refs":["root_000879/B002","root_000880/B002"],"candidate_id":"cand_a8fe65f7aa32df6c2599","commentary_obligation":"review","hft_ref":"hft_6fcd4161dc73c6c06d48","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base-mercy-vector-reversed","source_type":"hft","support_ids":["sup_2589583ad8cbc5c8f0a8"],"title":"base-mercy-vector-reversed","trust":"legacy_unbound"},{"anchor_refs":["107:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:4","branch_refs":["root_000879/B001","root_000880/B003"],"candidate_id":"cand_178a29fa5ddeaa3c187c","commentary_obligation":"review","hft_ref":"hft_24a61cf7f41e4d47750f","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base-heat-encounter","source_type":"hft","support_ids":["sup_1b8122426ce82bb829c9"],"title":"base-heat-encounter","trust":"legacy_unbound"},{"anchor_refs":["107:4"],"authoring_origin":"lossless_raw_hft_projection","ayah_ref":"107:4","branch_refs":["root_000879/B006","root_000880/B007"],"candidate_id":"cand_2c30bbf16a55841ccfd5","commentary_obligation":"review","hft_ref":"hft_3593137ddce69297bc51","kind":"baseline_model","lane":"micro","lane_assignment_basis":"all explicit HFT anchors are the focus ayah","provenance_qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"scope":"focus_ayah","source_local_id":"reader_hft_a:base-second-runner","source_type":"hft","support_ids":["sup_d5df39040aa9e211758c"],"title":"base-second-runner","trust":"legacy_unbound"}],"connection_registry":[],"focus":{"arabic_uthmani":"فَوَيْلٌۭ لِّلْمُصَلِّينَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"107:4:1:1","qac_word_ref":"107:4:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"وَيْل","morph_features":"STEM|POS:N|LEM:wayol|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:1:2","qac_word_ref":"107:4:1","root_ar":"","surface_ar":"وَيْلٌ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"107:4:2:1","qac_word_ref":"107:4:2","root_ar":"","surface_ar":"لِّ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"107:4:2:2","qac_word_ref":"107:4:2","root_ar":"","surface_ar":"لْ"},{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","root_ar":"ص ل و","surface_ar":"مُصَلِّينَ"}],"word_analysis_qac_refs":[["107:4:1:1"],["107:4:1:2"],["107:4:2:1","107:4:2:2","107:4:2:3"]],"word_analysis_ref_namespace":"word-analysis","word_analysis_refs":["107:4:1","107:4:2","107:4:3"]},"focus_surface_evidence":{"arabic_uthmani":"فَوَيْلٌۭ لِّلْمُصَلِّينَ","qac_morphemes":[{"lemma_ar":"","morph_features":"PREFIX|f:REM+","morpheme_role":"PREFIX","pos":"REM","qac_ref":"107:4:1:1","qac_word_ref":"107:4:1","root_ar":"","surface_ar":"فَ"},{"lemma_ar":"وَيْل","morph_features":"STEM|POS:N|LEM:wayol|M|INDEF|NOM","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:1:2","qac_word_ref":"107:4:1","root_ar":"","surface_ar":"وَيْلٌ"},{"lemma_ar":"","morph_features":"PREFIX|l:P+","morpheme_role":"PREFIX","pos":"P","qac_ref":"107:4:2:1","qac_word_ref":"107:4:2","root_ar":"","surface_ar":"لِّ"},{"lemma_ar":"","morph_features":"PREFIX|Al+","morpheme_role":"PREFIX","pos":"DET","qac_ref":"107:4:2:2","qac_word_ref":"107:4:2","root_ar":"","surface_ar":"لْ"},{"lemma_ar":"مُصَلِّين","morph_features":"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN","morpheme_role":"STEM","pos":"N","qac_ref":"107:4:2:3","qac_word_ref":"107:4:2","root_ar":"ص ل و","surface_ar":"مُصَلِّينَ"}],"qualification":"These records preserve supplied Arabic, transliteration, analytic gloss boundaries, and morphology for accurate prose. Analysis and QAC coordinates are internal provenance and must not appear in reader prose. English gloss ranges require a natural Turkish rendering. These are surface evidence, not a finding list and not proof of any secondary branch activation.","word_analysis_qac_refs":[["107:4:1:1"],["107:4:1:2"],["107:4:2:1","107:4:2:2","107:4:2:3"]],"word_analysis_refs":["107:4:1","107:4:2","107:4:3"],"word_rows":[{"analysis_record_ref":"107:4:1","analytic_gloss_range_en":"prefixed consequential and resumptive particle linking the verdict to the preceding indictment while opening a new verdict clause","analytic_root_gloss_range_en":null,"qac_refs":["107:4:1:1"],"root":{"note":"no lexical root"},"surface":{"arabic":"فَ","transliteration":"fa-"}},{"analysis_record_ref":"107:4:2","analytic_gloss_range_en":"indefinite nominative verdict noun in a woe-to construction, locally assigning ruin or doom while retaining lament and destination overtones","analytic_root_gloss_range_en":"doom, destructive harm, punishment, calamity, disgrace, and lament; local syntax selects the woe-verdict formula, with lament and punishment-place imagery as secondary pressure","qac_refs":["107:4:1:2"],"root":{"arabic":"و ي ل","transliteration":"w-y-l"},"surface":{"arabic":"وَيْلٌۭ","transliteration":"waylun"}},{"analysis_record_ref":"107:4:3","analytic_gloss_range_en":"for or against the definite prayer-performers: a governed lām phrase naming a human active-participle class whose specific blame is restricted by 107:5","analytic_root_gloss_range_en":"ritual prayer as binding worship, supplication and blessing, exposure to fire, kindling, following close behind, bending/back imagery, and other lexical branches; local Form II active participle selects prayer-performers while some root-family pressures remain secondary","qac_refs":["107:4:2:1","107:4:2:2","107:4:2:3"],"root":{"arabic":"ص ل ي","transliteration":"ṣ-l-y"},"surface":{"arabic":"لِلْمُصَلِّينَ","transliteration":"lilmuṣallīna"}}]},"focus_word_alignment":{"alignment_version":"qac-analysis-bridge-v1","bridge":{"qac_source_sha256":"706a45d150251ca3114a13499e2b665fe5596b03b2272557574f0ed58eb29594","release_id":"2026.09.02","release_manifest_sha256":"10c30bf9e36c8efcf14ee1cc1d9005024d2eaf97190135ad25b8ef314ebe28b6","schema_version":"qac-masaq-bridge-v1","source":"quran-data/data/bridges/qac-masaq.sqlite.gz","source_sha256":"a3dabe8200c3e172bfd1ea8eff1c051a250ab65eb7bd4dc0cb5144c9117d7a2a","sqlite_user_version":4,"word_analysis_tree_sha256":"95529b40cf4cbcdd88e855ef8418eb465820507b1fd3497094fa5075ecbb7f7e"},"note":"Accepted bridge links preserve independent analysis identities. Several analysis entries may share canonical morphemes. Read their distinct semantic claims; shared morphology alone is not duplication. Legacy aligned_qac_word_ref values are source observations, not QAC joins. Excluded source entries remain available with their explicit qualification.","shared_morphemes":[],"source_namespace":"word-analysis","target_namespace":"qac-morpheme","unresolved":[],"words_resolved":3,"words_total":3,"words_unresolved":0},"hft_evidence":{"anchor_evidence_coverage":{"cited_unique_anchor_count":1,"missing_anchor_refs":[],"supplied_unique_anchor_count":1},"assigned_record_count":4,"assigned_records":[{"anchor_refs":["107:4"],"branch_refs":["root_000879/B003","root_000880/B001"],"candidate_id":"cand_ff16b8e41fc921d3adfe","evidence_scope":"focus_ayah","hft_ref":"hft_f576cf65f7d2b162e188","item_id":"base-prescribed-insider-warning","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base-prescribed-insider-warning","support_id":"sup_3330730bb67908045dee"},{"anchor_refs":["107:4"],"branch_refs":["root_000879/B002","root_000880/B002"],"candidate_id":"cand_a8fe65f7aa32df6c2599","evidence_scope":"focus_ayah","hft_ref":"hft_6fcd4161dc73c6c06d48","item_id":"base-mercy-vector-reversed","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base-mercy-vector-reversed","support_id":"sup_2589583ad8cbc5c8f0a8"},{"anchor_refs":["107:4"],"branch_refs":["root_000879/B001","root_000880/B003"],"candidate_id":"cand_178a29fa5ddeaa3c187c","evidence_scope":"focus_ayah","hft_ref":"hft_24a61cf7f41e4d47750f","item_id":"base-heat-encounter","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base-heat-encounter","support_id":"sup_1b8122426ce82bb829c9"},{"anchor_refs":["107:4"],"branch_refs":["root_000879/B006","root_000880/B007"],"candidate_id":"cand_2c30bbf16a55841ccfd5","evidence_scope":"focus_ayah","hft_ref":"hft_3593137ddce69297bc51","item_id":"base-second-runner","kind":"baseline_model","lane_basis":"all explicit HFT anchors are the focus ayah","owning_lane":"micro","qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"reader_id":"reader_hft_a","source_local_id":"reader_hft_a:base-second-runner","support_id":"sup_d5df39040aa9e211758c"}],"diagnostics":[],"lane_counts":{"global":9,"macro":13,"micro":4},"packet_summary":{"ayah_count":7,"focus_ref":"107:4","protocol":"focus-trace-hermetic-packet-v2","split_root_mappings":[{"qac_root":"ص ل و","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000879","furuq_root_norm":"ص ل و","furuq_source_root_norm":"ص ل و","is_dominant":true,"target_occurrences":7,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000880","furuq_root_norm":"ص ل ي","furuq_source_root_norm":"ص ل ي","is_dominant":false,"target_occurrences":7,"target_rank":2}]},{"qac_root":"ر ء ي","targets":[{"furuq_resolution":"root_norm_unique","furuq_root_id":"root_000531","furuq_root_norm":"ر ء ي","furuq_source_root_norm":"ر أ ي","is_dominant":true,"target_occurrences":145,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000615","furuq_root_norm":"ر و ي","furuq_source_root_norm":"ر و ي","is_dominant":false,"target_occurrences":2,"target_rank":2}]},{"qac_root":"د ع ع","targets":[{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000477","furuq_root_norm":"د ع ع","furuq_source_root_norm":"د ع ع","is_dominant":true,"target_occurrences":2,"target_rank":1},{"furuq_resolution":"source_root_norm","furuq_root_id":"root_000478","furuq_root_norm":"د ع و","furuq_source_root_norm":"د ع و","is_dominant":false,"target_occurrences":1,"target_rank":2}]}],"window":["107:1","107:2","107:3","107:4","107:5","107:6","107:7"]},"payload_location":"Each assigned record's exact raw payload and exact available anchor Arabic are in support_registry under its support_id.","policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"provenance":{"authoring_effect":"This is one neutral source qualification. It controls epistemic status and containment, never evidence visibility or presumptive acceptance/rejection.","legacy_docket_assessment":{"adjudicable":false,"packet":null,"status":"invalid"},"packet_scope_relation":"exact_declared_pericope","reader_identity":[{"focus_ref":"107:4","identity_status":"legacy_unbound","packet_identity":null,"protocol":"focus-trace-hermetic-response-v4","reader_id":"reader_hft_a","trace_kind":"reconstructed"}]},"reader_synthesis_count":9,"source_present":true,"structured_insight_count":17,"unstructured_record_count":0},"identity":{"ayah_ref":"107:4","lane":"micro","linguistic_source_ref":"107:4","surface_ref":"107:4","unit_kind":"numbered_ayah"},"primary_floor":{"source_ref":"107:4","target_tokens":[["Vay",["107:4:1"]],["namaz",["107:4:2"]],["kılanların",["107:4:2"]],["hâline",["107:4:1","107:4:2"]]],"text":"Vay namaz kılanların hâline!"},"schema_version":"commentary-v5-hermetic-scope-packet-v1","scope":{"hft":{"assigned_record_count":4,"authoring_policy":{"every_assigned_record_requires_explicit_review":true,"parseable_hft_is_always_visible_to_authoring":true,"provenance_affects_qualification_not_visibility":true,"scope_mismatch_affects_lane_assignment_not_visibility":true,"unresolved_branch_citations_do_not_suppress_records":true},"authoring_status":"visible_with_provenance_qualification"},"lane_contract":"focus ayah morphology, word analysis, and every available focus-root branch; unavailable dictionaries are explicit","pericope":{"ayah_from":1,"ayah_to":7,"id":"s107-p01-001-007","label":"Whole surah","number":1,"refs":["107:1","107:2","107:3","107:4","107:5","107:6","107:7"]},"readiness":{"authoring_effect":"Docket readiness is reported for source provenance. HFT visibility is governed by the authoring policy above.","docket_mode":"quarantine_without_hft","docket_ready":true}},"selected_context_units":[],"support_registry":[{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3:contested-bending-following-imagery","source_type":"word_analysis","support_id":"sup_084a98da2534039efce2","text":"{\"blocking_evidence\":null,\"headline\":\"bending and following images sharpen the label\",\"reader_payoff\":\"The reader notices that disputed root imagery of bending and close following can make the prayer label feel bodily and adherent without displacing ritual prayer as the sense.\",\"reason\":\"V4 includes back or haunch imagery and close-following branches for {{ar:ص ل ي}} ({{tr:ṣ-l-y}}), while QAC's local form still identifies the word as the Form II prayer-performing participle.\",\"representative_source_ids\":[\"QS-0fec9eb5\",\"QS-c25f9f6f\",\"QS-dc6e27ee\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:2:sounded-lament-cadence","source_type":"word_analysis","support_id":"sup_0a51a530b8c078bd84b2","text":"{\"blocking_evidence\":null,\"headline\":\"sound texture reinforces the lament field\",\"reader_payoff\":\"The reader notices that the recited movement from the short woe-word into the lām of the target lets lament and assignment be heard together.\",\"reason\":\"The lament branch is lexically supported, and the local sequence moves from final lām in {{ar:وَيْلٌۭ}} ({{tr:waylun}}) into the lām environment of {{ar:لِلْمُصَلِّينَ}} ({{tr:lilmuṣallīna}}); this supports sound texture as reinforcement, not as an independent sense.\",\"representative_source_ids\":[\"QS-5e523489\",\"QP-1e896223\",\"QE-9f22d139\",\"QP-1beb3576\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3:positive-prayer-label-under-woe","source_type":"word_analysis","support_id":"sup_0c3caad04b8d27b8ede5","text":"{\"blocking_evidence\":null,\"headline\":\"positive prayer label becomes the condemned target\",\"reader_payoff\":\"The reader notices the lexical shock: a label expected to praise worshippers is placed under the woe formula, unlike its positive recurrence in 70:22.\",\"reason\":\"The local construction attaches {{ar:لِلْمُصَلِّينَ}} ({{tr:lilmuṣallīna}}) to {{ar:وَيْلٌۭ}} ({{tr:waylun}}), while recurrence evidence contrasts this target with the positive occurrence of the same class label in 70:22.\",\"representative_source_ids\":[\"QS-99937cb3\",\"QS-78c851c9\",\"MS-5183c4ce\",\"QI-913fcf11\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:1:prefixed-form-compression","source_type":"word_analysis","support_id":"sup_10fe224ff868f119dcc2","text":"{\"blocking_evidence\":null,\"headline\":\"prefixed particle fuses with the verdict noun\",\"reader_payoff\":\"The reader notices that the linkage is not delayed; the first sounded unit already binds consequence to the woe-word.\",\"reason\":\"The surface places {{ar:فَ}} ({{tr:fa-}}) directly on {{ar:وَيْلٌۭ}} ({{tr:waylun}}), making the connector and verdict one written and recited opening.\",\"representative_source_ids\":[\"QF-4056eef6\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3:convergent-central-knot","source_type":"word_analysis","support_id":"sup_1268796efec0411fe858","text":"{\"blocking_evidence\":null,\"headline\":\"form, root pressure, and qualifier converge\",\"reader_payoff\":\"The reader notices why this word carries the ayah's central knot: morphology names the class, root history adds pressure, and 107:5 narrows the condemned prayer relation.\",\"reason\":\"The summary row coherently combines locally supported morphology, root-family range, and the forward qualifier supplied by 107:5.\",\"representative_source_ids\":[\"QY-f5573bd1\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3:case-locks-target-role","source_type":"word_analysis","support_id":"sup_28f0970dd1600a6d39be","text":"{\"blocking_evidence\":null,\"headline\":\"genitive case prevents independent-subject reading\",\"reader_payoff\":\"The reader notices that the group is not introduced as a new nominative subject; case locks it inside the woe-to construction.\",\"reason\":\"The form is majrūr under the prefixed lām, so the local parse keeps the prayer-performers as the governed target of {{ar:وَيْلٌۭ}} ({{tr:waylun}}).\",\"representative_source_ids\":[\"QG-9a9994f2\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:2","source_type":"word_analysis","support_id":"sup_41a742133cf72d54b2bb","text":"{\"gloss_range\":\"indefinite nominative verdict noun in a woe-to construction, locally assigning ruin or doom while retaining lament and destination overtones\",\"prose\":\"{{ar:وَيْلٌۭ}} ({{tr:waylun}}) is the ayah's verdict noun. Its nominative, verbless placement makes the judgment stand before any target is unpacked, while the following phrase {{ar:لِلْمُصَلِّينَ}} ({{tr:lilmuṣallīna}}) assigns that judgment to a definite group. The tanwin leaves the woe unbounded: the ruin is not measured, even though the recipient is named. Lexically, the word is more than a label for blame; it carries doom, calamity, a possible punishment-destination, and the sound-field of lament, though the local clause selects the formulaic verdict sense. Its falling ay-sound into final lām, then the lām environment of {{ar:لِلْمُصَلِّينَ}} ({{tr:lilmuṣallīna}}), lets the cry land and then be assigned. That familiar anti-blessing formula is redirected toward prayer-performers, making the target reversal part of the shock. Coming after the failed urging to feed, the prior verbal description hardens into nominal condemnation.\",\"root_display\":\"{{ar:و ي ل}} ({{tr:w-y-l}})\",\"root_gloss_range\":\"doom, destructive harm, punishment, calamity, disgrace, and lament; local syntax selects the woe-verdict formula, with lament and punishment-place imagery as secondary pressure\",\"surface_display\":\"{{ar:وَيْلٌۭ}} ({{tr:waylun}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3:prior-portrait-receives-label","source_type":"word_analysis","support_id":"sup_4d24bef18117339736d0","text":"{\"blocking_evidence\":null,\"headline\":\"the definite plural names the prior portrait\",\"reader_payoff\":\"The reader notices that the prayer label reaches back over the prior portrait of denial and social harm, rather than appearing as an isolated group name.\",\"reason\":\"The boundary rows tie the definite target to the preceding portrait, and the local evidence gives no pronoun; the relation is discourse identification rather than pronominal reference.\",\"representative_source_ids\":[\"QI-9e11c032\",\"QB-569f22b8\",\"QB-aada7fbd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:2:nominal-verdict-frame","source_type":"word_analysis","support_id":"sup_539d994a3c379cedf59b","text":"{\"blocking_evidence\":null,\"headline\":\"verbless noun performs the verdict\",\"reader_payoff\":\"The reader notices that the ayah does not narrate ruin with a verb; the noun itself stands as the judicial declaration.\",\"reason\":\"QAC and attachment evidence identify {{ar:وَيْلٌۭ}} ({{tr:waylun}}) as a nominative noun in a nominal clause, with {{ar:لِلْمُصَلِّينَ}} ({{tr:lilmuṣallīna}}) completing the predication rather than functioning as a direct object.\",\"representative_source_ids\":[\"QG-3bb2d7c2\",\"QG-8a210960\",\"QI-eb2f3828\",\"QT-059868df\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:2:formula-redirected-to-prayers","source_type":"word_analysis","support_id":"sup_6539c40f7c18e27a55f9","text":"{\"blocking_evidence\":null,\"headline\":\"familiar woe formula receives a surprising target\",\"reader_payoff\":\"The reader notices that a familiar condemnation formula is aimed here at a prayer-performing class, making the target itself startling.\",\"reason\":\"Contextual evidence shows recurrent {{ar:وَيْلٌۭ}} ({{tr:waylun}}) use as a condemnation formula, while the local lām complement assigns it to {{ar:لِلْمُصَلِّينَ}} ({{tr:lilmuṣallīna}}).\",\"representative_source_ids\":[\"QI-3fcf113d\",\"QI-af2bf10f\",\"QS-6d704e26\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"focus_occurrence","scope":"micro","source_local_id":"107:4:2:3","source_type":"qac_morpheme","support_id":"sup_6828497e1550eccdb302","text":"{\"lemma_ar\":\"مُصَلِّين\",\"morph_features\":\"STEM|POS:N|ACT|PCPL|(II)|LEM:muSal~iyn|ROOT:Slw|MP|GEN\",\"morpheme_role\":\"STEM\",\"pos\":\"N\",\"qac_ref\":\"107:4:2:3\",\"qac_word_ref\":\"107:4:2\",\"root_ar\":\"ص ل و\",\"surface_ar\":\"مُصَلِّينَ\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3:blocked-direct-burner-forms","source_type":"word_analysis","support_id":"sup_6d9aa62bd64eb6856e6c","text":"{\"blocking_evidence\":null,\"headline\":\"form blocks direct burner identity\",\"reader_payoff\":\"The reader notices that the wording condemns people under the name of prayer, not under a direct fire-causer or burner label.\",\"reason\":\"The local word is Form II active participle for prayer-performance; V4's fire branches can color the root family, but they do not override the selected prayer-performer form.\",\"representative_source_ids\":[\"QF-a84273c2\",\"QI-08f1645f\",\"QB-74c2793d\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:2:boundary-from-failed-urging","source_type":"word_analysis","support_id":"sup_7984107e8fed14ed38dd","text":"{\"blocking_evidence\":null,\"headline\":\"failed urging turns into condemnation\",\"reader_payoff\":\"The reader notices that the previous failure to press for feeding is converted into a fixed woe-verdict at the boundary.\",\"reason\":\"The input's boundary rows connect the preceding behavioral chain to {{ar:وَيْلٌۭ}} ({{tr:waylun}}), and QAC confirms the noun's nominal verdict role.\",\"representative_source_ids\":[\"QB-5d753d70\",\"QB-fb2a9956\",\"QT-db4780ce\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:2:unbounded-woe-definite-target","source_type":"word_analysis","support_id":"sup_822a57ebca2ac2f6b20b","text":"{\"blocking_evidence\":null,\"headline\":\"indefinite woe faces a definite class\",\"reader_payoff\":\"The reader notices the asymmetry: the woe is left indefinite and unmeasured while the target class is made definite.\",\"reason\":\"QAC marks {{ar:وَيْلٌۭ}} ({{tr:waylun}}) as indefinite with tanwin and marks {{ar:لِلْمُصَلِّينَ}} ({{tr:lilmuṣallīna}}) as definite, supporting the contrast without requiring a quantified gloss.\",\"representative_source_ids\":[\"QG-821be473\",\"QF-245a49db\",\"MS-33e1b1ea\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:1:consequential-verdict-hinge","source_type":"word_analysis","support_id":"sup_897b95d36f102d27e10c","text":"{\"blocking_evidence\":null,\"headline\":\"consequence and resumption meet at the verdict\",\"reader_payoff\":\"The reader notices that 107:4 is both a new verdict section and a consequence of the conduct described in 107:1-3.\",\"reason\":\"QAC allows {{ar:فَ}} ({{tr:fa-}}) as causative or immediate/resumptive, and attachment evidence treats the ayah as a nominal verdict clause connected to the preceding discourse.\",\"representative_source_ids\":[\"QG-5afa79bd\",\"QG-f2c6052f\",\"MG-a6b17d87\",\"QT-05dd0761\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3:lam-governed-harmful-assignment","source_type":"word_analysis","support_id":"sup_bd68533a8183b2cd7cdb","text":"{\"blocking_evidence\":null,\"headline\":\"lām assigns the woe to its target\",\"reader_payoff\":\"The reader notices that the preposition does not merely point toward the group; it grammatically assigns the woe to them as the affected target.\",\"reason\":\"QAC marks {{ar:لِلْمُصَلِّينَ}} ({{tr:lilmuṣallīna}}) as a lām-governed genitive phrase, and attachment evidence identifies it as the complement and predicate phrase relating the doom noun to the worshippers.\",\"representative_source_ids\":[\"QG-e5a5af66\",\"QG-ecf34ba1\",\"QG-f0fa8a10\",\"MG-e6653f62\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3:active-participle-habitual-agents","source_type":"word_analysis","support_id":"sup_bdb95ce29241fbcc9886","text":"{\"blocking_evidence\":null,\"headline\":\"participle names a practitioner-class\",\"reader_payoff\":\"The reader notices that the word names people by characteristic prayer-performance before the next ayah specifies the defect in that prayer relation.\",\"reason\":\"QAC identifies the word as a definite masculine plural active participle from Form II, and the contextual profile treats the referent class as human rather than abstract prayer itself.\",\"representative_source_ids\":[\"QG-0e3026a5\",\"QF-aa71f278\",\"QF-c8a83b77\",\"QF-3e03751c\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3:li-al-compressed-target-form","source_type":"word_analysis","support_id":"sup_d0e5e5204f142b68d94f","text":"{\"blocking_evidence\":null,\"headline\":\"designation and definiteness compress into one form\",\"reader_payoff\":\"The reader notices that assignment and identification are compressed in the same word-shape before the participial class is heard.\",\"reason\":\"The surface combines the prepositional lām, the definite article, and the active participle into {{ar:لِلْمُصَلِّينَ}} ({{tr:lilmuṣallīna}}).\",\"representative_source_ids\":[\"QF-395d0b09\",\"QP-da910ffd\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3","source_type":"word_analysis","support_id":"sup_d421b4e7b918651aeab3","text":"{\"gloss_range\":\"for or against the definite prayer-performers: a governed lām phrase naming a human active-participle class whose specific blame is restricted by 107:5\",\"prose\":\"{{ar:لِلْمُصَلِّينَ}} ({{tr:lilmuṣallīna}}) supplies the target of the verdict. The prefixed lām governs the phrase and assigns {{ar:وَيْلٌۭ}} ({{tr:waylun}}) to it, so the prayer-performers are grammatically dependent but semantically central as the affected recipients; the assignment is harmful, not neutral possession. Because the phrase comes after the woe and closes the ayah, the reader hears the verdict first and only then discovers that the named target is the praying class. The active participle names human agents by repeated or characteristic prayer-performance, and the definite plural makes them a recognizable class rather than a single act or an abstraction. The fused lām-plus-article form compresses assignment and definiteness into one target word. That class is shocking because the label is normally positive; the same label is exemptive in 70:22, while here it is placed under woe. It also reaches back over the prior portrait of denial and social harm, giving that accumulated figure a surprising prayer label. The next ayah restricts the target: 107:5 returns to their prayer and identifies heedlessness, so 107:4 does not condemn every worshipper without distinction. The broader {{ar:ص ل ي}} ({{tr:ṣ-l-y}}) family lets prayer, fire-exposure, following, and bending imagery press around the word, but the local Form II participle keeps prayer-performers as the selected surface sense rather than a direct burner or fire-causer label.\",\"root_display\":\"{{ar:ص ل ي}} ({{tr:ṣ-l-y}})\",\"root_gloss_range\":\"ritual prayer as binding worship, supplication and blessing, exposure to fire, kindling, following close behind, bending/back imagery, and other lexical branches; local Form II active participle selects prayer-performers while some root-family pressures remain secondary\",\"surface_display\":\"{{ar:لِلْمُصَلِّينَ}} ({{tr:lilmuṣallīna}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:1","source_type":"word_analysis","support_id":"sup_da7d9ddfca4f4e24cbc4","text":"{\"gloss_range\":\"prefixed consequential and resumptive particle linking the verdict to the preceding indictment while opening a new verdict clause\",\"prose\":\"{{ar:فَ}} ({{tr:fa-}}) makes the woe of 107:4 a consequence, not a detached cry. It carries the prior portrait in 107:1-3 into {{ar:وَيْلٌۭ}} ({{tr:waylun}}), so the verdict sounds like a ruling drawn from evidence. At the same time, it opens a fresh nominal sentence: the surah moves from describing conduct to pronouncing judgment. Because the particle is prefixed to the verdict noun, the first word-shape already fuses linkage and condemnation.\",\"root_display\":\"no lexical root\",\"root_gloss_range\":null,\"surface_display\":\"{{ar:فَ}} ({{tr:fa-}})\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3:root-family-prayer-fire-pressure","source_type":"word_analysis","support_id":"sup_e063eec84dbd7c73a4c2","text":"{\"blocking_evidence\":null,\"headline\":\"prayer sense carries fire-family pressure\",\"reader_payoff\":\"The reader notices that the prayer label remains the surface sense while the broader root family lets fire-exposure and burning imagery shadow the condemnation.\",\"reason\":\"V4 accepts both ritual-prayer and fire-exposure branches for {{ar:ص ل ي}} ({{tr:ṣ-l-y}}), but the local Form II active participle selects prayer-performers; fire language remains root-family pressure, not the selected local referent.\",\"representative_source_ids\":[\"QS-c43a359a\",\"QS-da2f39c0\",\"QF-e0e41c84\",\"QE-0731bfc8\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3:definite-class-forward-restriction","source_type":"word_analysis","support_id":"sup_ed308b21c650103a8990","text":"{\"blocking_evidence\":null,\"headline\":\"definite class waits for 107:5\",\"reader_payoff\":\"The reader notices that the definite class is not left unrestricted; 107:5 immediately explains which kind of prayer-performance is under woe.\",\"reason\":\"QAC marks the target as definite, while attachment translation support warns that 107:4 alone can overgeneralize before the descriptive material in 107:5-7 restricts the group.\",\"representative_source_ids\":[\"QG-2d702250\",\"QG-6069ed4c\",\"QB-b4ac25dd\",\"QE-5eff5a1f\"],\"status\":\"used\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:2:doom-lament-destination-range","source_type":"word_analysis","support_id":"sup_f05901702d2a6d438754","text":"{\"blocking_evidence\":null,\"headline\":\"doom verdict carries lament and destination overtones\",\"reader_payoff\":\"The reader notices that the word does not merely say blame; it gathers ruin, calamity, lament, and punishment-place pressure into the verdict.\",\"reason\":\"V4 supports doom/destructive harm and lament branches for {{ar:و ي ل}} ({{tr:w-y-l}}); local syntax selects the woe-to verdict formula, so place and lament senses remain secondary pressure rather than replacing the predicative doom.\",\"representative_source_ids\":[\"QS-4f15ab14\",\"QS-702ff2e0\",\"QS-ac87a6d7\",\"QY-3984cf2e\"],\"status\":\"narrowed\"}","trust":"trusted"},{"branch_refs":[],"citable":true,"role":"candidate_evidence","scope":"micro","source_local_id":"107:4:3:delayed-final-target-shock","source_type":"word_analysis","support_id":"sup_ffcc13d90748f9a1e771","text":"{\"blocking_evidence\":null,\"headline\":\"target lands after the verdict\",\"reader_payoff\":\"The reader notices that the ayah withholds the identity of the target until the final phrase, letting the woe arrive before the prayer-class is named.\",\"reason\":\"The local order places {{ar:وَيْلٌۭ}} ({{tr:waylun}}) before the lām phrase, and the target phrase closes the ayah.\",\"representative_source_ids\":[\"QT-2940fb1c\",\"QT-eccd6478\",\"QP-994d596c\"],\"status\":\"used\"}","trust":"trusted"},{"anchor_evidence":[{"arabic_uthmani":"فَوَيْلٌۭ لِّلْمُصَلِّينَ","ayah_ref":"107:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000879/B003","root_000880/B001"],"payload":{"activation_trace":[{"branch_id":"B003","mapped_root_id":"root_000879","role":"The prescribed-rite sense fixes the agent noun to embodied, rule-governed worship and makes the threat an insider address.","root":"ص ل و","source_ref":"107:4","source_word_indices":["2"]},{"branch_id":"B001","mapped_root_id":"root_000880","role":"The non-dominant mapped branch reinforces prayer as an obligation borne by the named practitioners rather than a loose devotional mood.","root":"ص ل و","source_ref":"107:4","source_word_indices":["2"]}],"changed_reading":{"after":"An insider warning: people can bear the agentive identity of prayer and still stand under the threat, so performance is evidence to examine rather than immunity.","before":"A bare and indiscriminate curse on everyone who prays."},"confidence":"strong","focus_anchor":"The threat is directed by the lamed to the plural agent noun built on the prayer root.","mechanism":"The focus does not attack an abstract rite from outside; it places liability inside the class named by performing a binding, embodied practice. Ritual membership therefore cannot itself close the moral question.","model_id":"base-prescribed-insider-warning"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base-prescribed-insider-warning","source_type":"hft","support_id":"sup_3330730bb67908045dee","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَوَيْلٌۭ لِّلْمُصَلِّينَ","ayah_ref":"107:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000879/B002","root_000880/B002"],"payload":{"activation_trace":[{"branch_id":"B002","mapped_root_id":"root_000879","role":"The branch supplies prayer as benefit directed toward another, making outward transmission a live function of the practitioner label.","root":"ص ل و","source_ref":"107:4","source_word_indices":["2"]},{"branch_id":"B002","mapped_root_id":"root_000880","role":"The split-root counterpart keeps blessing and mercy active beside formal worship, supporting a relational rather than merely procedural baseline.","root":"ص ل و","source_ref":"107:4","source_word_indices":["2"]}],"changed_reading":{"after":"The praying ones are also potential conduits of blessing; woe marks the possibility that the conduit has been occupied but functionally reversed or blocked.","before":"The praying ones are identified by possessing or completing a private rite."},"confidence":"medium","focus_anchor":"The same focus noun is branch-linked to supplication, blessing, praise, and mercy.","mechanism":"Prayer can be modeled as an outward relational vector rather than a self-contained possession. The collision of that vector with woe creates a reversal: a practitioner may occupy the form while blocking what should pass through it.","model_id":"base-mercy-vector-reversed"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base-mercy-vector-reversed","source_type":"hft","support_id":"sup_2589583ad8cbc5c8f0a8","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَوَيْلٌۭ لِّلْمُصَلِّينَ","ayah_ref":"107:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000879/B001","root_000880/B003"],"payload":{"activation_trace":[{"branch_id":"B001","mapped_root_id":"root_000879","role":"The dominant mapped branch contributes proximity to consuming or testing heat as a material shadow of entering prayer.","root":"ص ل و","source_ref":"107:4","source_word_indices":["2"]},{"branch_id":"B003","mapped_root_id":"root_000880","role":"The non-dominant mapped branch makes undergoing heat explicit and turns the worshipper label into a possible exposure-state.","root":"ص ل و","source_ref":"107:4","source_word_indices":["2"]}],"changed_reading":{"after":"The focus also admits a threshold reading: these practitioners repeatedly approach a transforming heat, and the threat lies in an encounter that does not transform.","before":"Woe is an external penalty simply attached to a surprising group."},"confidence":"exploratory","focus_anchor":"Both mapped inventories for the focus root retain an encounter-with-heat branch alongside prayer.","mechanism":"The split root lets the practitioner label carry a thermal shadow. Woe is no longer only a sentence imposed after worship; it can disclose that prayer is an exposure meant to affect the one who enters it, with danger concentrated in remaining unchanged at the threshold.","model_id":"base-heat-encounter"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base-heat-encounter","source_type":"hft","support_id":"sup_1b8122426ce82bb829c9","trust":"legacy_unbound"},{"anchor_evidence":[{"arabic_uthmani":"فَوَيْلٌۭ لِّلْمُصَلِّينَ","ayah_ref":"107:4"}],"anchor_evidence_coverage":{"boundary":"Exact Arabic verifies surface contact only. HFT-stated segmentation, word indices, roots, branches, and roles remain attributed nominations unless independently supplied elsewhere in this packet.","cited_anchor_count":1,"exact_arabic_is_surface_evidence_only":true,"missing_anchor_refs":[],"supplied_anchor_count":1,"target_morphology_supplied":false},"branch_refs":["root_000879/B006","root_000880/B007"],"payload":{"activation_trace":[{"branch_id":"B006","mapped_root_id":"root_000879","role":"The race image supplies a practitioner who is defined by close pursuit of a predecessor, activating ordered following within the plural.","root":"ص ل و","source_ref":"107:4","source_word_indices":["2"]},{"branch_id":"B007","mapped_root_id":"root_000880","role":"The split-root counterpart confirms the near-behind position and makes borrowed trajectory a stable exploratory mechanism.","root":"ص ل و","source_ref":"107:4","source_word_indices":["2"]}],"changed_reading":{"after":"The named group can also be heard as followers in formation; the focus leaves open whether they carry a worthy course onward or merely trail its visible form.","before":"Each praying person is an independent performer of the rite."},"confidence":"exploratory","focus_anchor":"The focus agent noun shares its form with a racer immediately following the leader.","mechanism":"The plural can carry a formation-image: practitioners as second runners positioned by another's course. That does not replace the prayer sense, but it raises a live question about derivative alignment, imitation, and whether following transmits the leader's motion or only preserves rank.","model_id":"base-second-runner"},"qualification":{"anchor_scope_complete":true,"authoring_effect":"Source qualifications affect epistemic status and containment, never visibility or presumptive outcome.","packet_scope_relation":"exact_declared_pericope","reader_identity_status":"legacy_unbound","record_warnings":[]},"role":"hft_nomination_evidence","scope":"micro","source_local_id":"reader_hft_a:base-second-runner","source_type":"hft","support_id":"sup_d5df39040aa9e211758c","trust":"legacy_unbound"}]}
</lane_packet_json>
