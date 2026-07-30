# Instantiated Commentary v2 Prompt

- run: `s100-1-gpt55-high`
- stage: `layer3-channel-authoring`
- unit: `single-ayah`
- surah: 100
- target language: `tr`
- generated: `2026-07-29`
- expected outputs:
  - `_commentary/v2/generated/s100-1-gpt55-high/layer_3/outputs/single-ayah.channels.prose.md`
  - `_commentary/v2/generated/s100-1-gpt55-high/layer_3/outputs/single-ayah.channels.evidence.md`
  - `_commentary/v2/generated/s100-1-gpt55-high/layer_3/outputs/single-ayah.channels.result.json`
  - `_commentary/v2/generated/s100-1-gpt55-high/layer_3/outputs/single-ayah.channels.friction.md`
- inlined sources:
  - `_commentary/v2/layer_3/PROMPT.md` - 1,820 bytes - `db7f01f02c572d77c8169e65504a835b6ac1047a7db32a8b197dfa750b4c96e1`
  - `_commentary/v2/shared/EDITORIAL_CONTRACT.md` - 3,625 bytes - `530b89dae5b574671250452dd788e77de3f83d01e949b5538b68c70030efe2f4`
  - `_commentary/v2/shared/schemas/layer3-result.schema.json` - 4,015 bytes - `3260cb381ecc1859adc540f7beaf4335dcba07fed4767027d940ce787c2f74a4`
  - `PRINCIPLES.md` - 9,198 bytes - `fe4c0397d275a0201b8803782011ab9281392c2f76dc5e7584e1bec827c0c62c`
  - `COMMENTARY_SPEC.md` - 9,877 bytes - `3bb66fcd73a2af760b979f0cfcfabbee167ae8efa11f3f684df6dfa3e5e88a5f`
  - `s100-1-gpt55-high/single-ayah.layer3-input.json` - 178 bytes - `b47be590fd6771ab163a273cccf001028dc3b200219be2cec0b478b66478caf1`
  - `_commentary/v2/generated/s100-1-gpt55-high/shared/compiler/outputs/single-ayah.channel-registry.json` - 220 bytes - `9a4e93b9d3775bbe685b96a992318ac8371031eee63cdcb1de70be87f1e20348`

**Hermeticity rule:** use only the material inlined below. Source paths are provenance identities, not instructions to browse.

**Response rule:** write exactly the expected output files. Do not add an unrequested artifact or place one artifact inside another.

---

## task: `_commentary/v2/layer_3/PROMPT.md`

```markdown
# Layer 3 Channel Authoring Prompt

Read the inlined editorial contract, result schema, and channel registry.

## Task

Write:

1. `{PERICOPE}.channels.prose.md`
2. `{PERICOPE}.channels.evidence.md`
3. `{PERICOPE}.channels.result.json`
4. `{PERICOPE}.channels.friction.md`

## Channel prose

Build the complete recurring images and meaning systems visible in this
pericope.

- State the invariant that makes the members one channel.
- Show how each member changes or extends the accumulated image.
- Distinguish the channel from the primary argument.
- Keep every member anchored to its ayah and local word.
- Make the whole feel like recognition of previously grounded local findings.
- Preserve counterevidence and weak joins at their real strength.
- Do not admit a channel merely because several findings share vocabulary.
- Do not impose a maximum or preferred number of channels.

Layer 3 may select for coherence. Rejected candidates remain accounted for in
the result and evidence; their Layer 2 findings remain valid local material.

## Result

Account for every registry candidate as:

- `accepted`;
- `merged`;
- `revised`;
- `rejected`.

Every accepted or revised channel must list its source candidates, member
finding IDs, ayah sequence, relation to the primary floor, and prose section.
Every merged or rejected candidate must state why.

In `result.json`, record output files only as sibling filenames such as
`{PERICOPE}.channels.prose.md`, not repo-relative or absolute paths.

Copy `sourceRegistrySha256` exactly from the inlined Layer 3 input descriptor.
Do not calculate or normalize the hash.

## Evidence and friction

Evidence maps channel claims to registry members and original evidence
references. Friction records unresolved joins, likely cross-pericope
continuations, and missing grounding.
```

---

## editorial-contract: `_commentary/v2/shared/EDITORIAL_CONTRACT.md`

```markdown
# Commentary v2 Editorial Contract

## Layer boundaries

Layer 2 answers what one ayah does, how its words build it, and what local or
context-activated readings it carries. Layer 2 preserves the full admitted
field. It may consolidate expression, but it does not select a preferred subset.

Layer 3 builds cross-ayah systems: recurring images, meaning chains, argument
structures, and their development through a surah or pericope. Layer 3 may
adjudicate channel coherence, but it may not erase Layer 2 findings.

The shared compiler plans both surfaces without turning either into the other.

## No count-based selection

Do not impose:

- a surprise budget;
- a maximum number of findings;
- a fixed number of paragraphs;
- a preferred number of secondary readings;
- a quota based on ayah length.

An ayah with one grounded finding may remain short. An ayah with many distinct,
grounded findings may remain long.

Compression applies to repetition and wording, never to the number of distinct
reader payoffs. Two findings may share one movement only when their separate
payoffs remain recoverable and both finding IDs remain attached to the planned
placement.

## Coverage preservation

Every discovery finding has a `disposition`:

- `carry`: it must be represented in the editorial plan and final Layer 2
  result;
- `blocked`: it may not enter prose and must carry explicit blocking evidence.

The compiler does not change `carry` to `blocked`.

The editorial plan may combine multiple `carry` findings in one placement. It
must list every combined finding ID. The final Layer 2 result must report every
represented finding ID so coverage can be checked mechanically.

## Global plan, local writing

The compiler reads all ledgers in a pericope. It may:

- detect repeated explanations;
- identify before/after activations;
- assign a finding to the ayah whose own word grounds it;
- plan an arc across paragraphs;
- create a new synthesis from existing findings;
- nominate cross-ayah channel candidates.

The Layer 2 writer receives only its ayah ledger and its plan slice. It does not
receive the complete channel registry or a surah thesis. Its prose must remain
understandable when read independently.

The Layer 3 writer receives the channel registry. It develops complete chains
without forcing every member's full explanation back into every ayah.

## New syntheses

The compiler and final writers may discover a synthesis not stated in any one
input ledger. A new synthesis must:

1. name every component finding;
2. enter through a local anchor;
3. state whether it supports or shifts the primary reading;
4. record its support level;
5. map to evidence references;
6. preserve a return path to the ayah's direct meaning.

Synthetic novelty is allowed. Untraceable novelty is not.

## Reader movement

The edited Layer 2 prose should make the reading change perceptible:

- what the ayah yields before the activation;
- which word or later context activates the change;
- what becomes newly visible;
- how the reader returns to the original ayah with altered understanding.

This is an editorial movement, not a fixed template. Do not force an ayah into a
before/after shape when its evidence does not support one.

## Evidence economy

Planning prompts consume compact ledgers rather than complete evidence prose.
Evidence is represented by stable references. When a ledger lacks enough detail
to write safely, the downstream writer records the gap instead of reopening
arbitrary repository files or inventing support.

All instantiated prompts record byte counts and SHA-256 hashes for their exact
inputs.
```

---

## schema: `_commentary/v2/shared/schemas/layer3-result.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "commentary-v2-layer3-result.schema.json",
  "title": "Commentary v2 Layer 3 channel result",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schemaVersion",
    "surah",
    "pericopeId",
    "sourceRegistrySha256",
    "outputs",
    "channels",
    "candidateCoverage"
  ],
  "properties": {
    "schemaVersion": {
      "const": "commentary-v2-layer3-result-v1"
    },
    "surah": {
      "type": "integer",
      "minimum": 1,
      "maximum": 114
    },
    "pericopeId": {
      "$ref": "#/$defs/id"
    },
    "sourceRegistrySha256": {
      "$ref": "#/$defs/sha256"
    },
    "outputs": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "prose",
        "evidence",
        "friction"
      ],
      "properties": {
        "prose": {
          "type": "string",
          "minLength": 1
        },
        "evidence": {
          "type": "string",
          "minLength": 1
        },
        "friction": {
          "type": "string",
          "minLength": 1
        }
      }
    },
    "channels": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/channel"
      }
    },
    "candidateCoverage": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/candidateCoverage"
      }
    }
  },
  "$defs": {
    "id": {
      "type": "string",
      "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$"
    },
    "ayahRef": {
      "type": "string",
      "pattern": "^[1-9][0-9]{0,2}:[1-9][0-9]{0,2}$"
    },
    "findingRef": {
      "type": "string",
      "pattern": "^[1-9][0-9]{0,2}:[1-9][0-9]{0,2}:[a-z0-9]+(?:-[a-z0-9]+)*$"
    },
    "sha256": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$"
    },
    "channel": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "channelId",
        "sourceCandidateIds",
        "status",
        "name_tr",
        "statement_tr",
        "primaryRelation",
        "memberFindingRefs",
        "ayahSequence",
        "proseSectionId"
      ],
      "properties": {
        "channelId": {
          "$ref": "#/$defs/id"
        },
        "sourceCandidateIds": {
          "type": "array",
          "minItems": 1,
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/id"
          }
        },
        "status": {
          "enum": [
            "accepted",
            "revised"
          ]
        },
        "name_tr": {
          "type": "string",
          "minLength": 1
        },
        "statement_tr": {
          "type": "string",
          "minLength": 1
        },
        "primaryRelation": {
          "enum": [
            "supports-primary",
            "shifts-primary",
            "parallel-pressure"
          ]
        },
        "memberFindingRefs": {
          "type": "array",
          "minItems": 2,
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/findingRef"
          }
        },
        "ayahSequence": {
          "type": "array",
          "minItems": 2,
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/ayahRef"
          }
        },
        "proseSectionId": {
          "$ref": "#/$defs/id"
        }
      }
    },
    "candidateCoverage": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "candidateId",
        "disposition",
        "reason_tr"
      ],
      "properties": {
        "candidateId": {
          "$ref": "#/$defs/id"
        },
        "disposition": {
          "enum": [
            "accepted",
            "merged",
            "revised",
            "rejected"
          ]
        },
        "resultChannelIds": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/id"
          }
        },
        "reason_tr": {
          "type": "string",
          "minLength": 1
        }
      }
    }
  }
}
```

---

## governing: `PRINCIPLES.md`

```markdown
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
```

---

## governing: `COMMENTARY_SPEC.md`

```markdown
# Commentary Specification

Governs ayah-level (layer 2) and surah-level (layer 3) commentary. Both consume
the same input bundle and obey the same evidence rules; they differ in what
question they answer and in whether they are allowed to select.

[`PRINCIPLES.md`](PRINCIPLES.md) governs this file. Sources and formats are in
[`docs/SOURCES.md`](docs/SOURCES.md); channel rules in
[`docs/CHANNELS.md`](docs/CHANNELS.md).

Status: draft, 2026-07-27. Derived from rejected S103 attempts; **not yet
validated against a passing output.**

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
| selection | **must select** — a thesis excludes | **must not select** — carries the full field |
| time | none; the whole is present at once | **has a before and an after** |
| pass condition | says something no ayah-by-ayah reading could produce | holds what the surah thesis had to drop |

These are not two sizes of one output. A surah reading that decomposes back into
its ayahs has failed. An ayah reading that is a slice of the surah thesis has
failed.

The split is also where no-disambiguation is structurally guaranteed. Building a
thesis requires excluding readings. With one level, excluded readings would be
lost. With two, the thesis lives at surah level and the complete field survives
at ayah level. Neither cancels the other; they answer different questions.

### 2.1 The surah argument rests on the primary reading

An argument that holds only under latent readings is not yet an argument. State
it from the primary reading first; latent readings then perturb, deepen, or
recolour it. If removing every latent reading collapses the thesis, the thesis is
not ready.

This does not demote channels — see `docs/CHANNELS.md` §4. The argument and the
channels are separate outputs on separate axes, and for some surahs (S100) the
channel is the more valuable finding.

### 2.2 Local surprise is not a channel increment

Layer 2 states the **local surprise reading** made visible by this ayah's own
words: the secondary resonance, what it does to the recoverable primary reading,
and what becomes newly legible. This requires no claim that the image recurs
elsewhere.

A **surah-channel increment** is different. It says how a reviewed recurring
system has matured by this position in the surah. The isolated layer-2 writer
cannot know that. The combined Layer 3 + 2.5 pass consumes the reviewed system
and adds its maturity-bounded increment without rewriting the local reading into
a thesis slice.

Layer 2 may **not** carry the surah's thesis or name a recurring surah channel.
The distinction is testable: a local surprise is fully anchored in this ayah;
a channel increment depends on members already encountered elsewhere; a thesis
is visible only from the assembly.

Disclosure rules and the interim state: `docs/CHANNELS.md` §3 and §3.1.

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
  primary instead of asking layer 3 to reconstruct that relation;
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

The combined Layer 3 + 2.5 lane additionally emits:

- **thesis** — one sentence;
- **reviewed channel plan** — stable channel/member IDs, exact lexical anchors,
  focus-ayah and whole-surah effects, and reviewed maturity in reading order,
  compiled from the upstream reviewed channels;
- **exclusions** — activated readings the thesis could not carry, recorded
  against Layer 2's already-preserved full field. They do not trigger a
  thesis-aware rewrite of the cold ayah prose.

The same pass emits structured ayah overlays whose insertion points refer to the
unchanged Layer-2 prose. The channel plan and overlays share member IDs and
maturity, so the completed prose and gradual disclosure are designed together.
Schemas:
`schemas/surah-channel-plan-v1.schema.json` and
`schemas/ayah-channel-overlays-v1.schema.json`.

---

## 6. Input bundle

One bundle per ayah; a surah bundle is the ordered set of its ayah bundles plus
surah-scope material. Built by `scripts/build_bundle.py`; shape in
`bundles/schema.json`; sources, formats, gotchas, and the coverage requirement in
[`docs/SOURCES.md`](docs/SOURCES.md).
```

---

## compiler-input: `s100-1-gpt55-high/single-ayah.layer3-input.json`

```json
{"schemaVersion":"commentary-v2-layer3-input-v1","surah":100,"pericopeId":"single-ayah","sourceRegistrySha256":"95c0d3b2806747a1c33235ad04969c5dfef69c7fdb5be19f8bf3a27786fa9a51"}
```

---

## channel-registry: `_commentary/v2/generated/s100-1-gpt55-high/shared/compiler/outputs/single-ayah.channel-registry.json`

```json
{"schemaVersion":"commentary-v2-channel-registry-v1","surah":100,"pericopeId":"single-ayah","sourceLedgers":[{"ayahRef":"100:1","sha256":"413a137233cef872dcca92ad2ccf47565519c2d98c211aabde4828fa682c99bc"}],"channels":[]}
```

---
