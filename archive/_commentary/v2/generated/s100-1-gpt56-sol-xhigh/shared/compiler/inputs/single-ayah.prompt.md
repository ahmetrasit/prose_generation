# Instantiated Commentary v2 Prompt

- run: `s100-1-gpt56-sol-xhigh`
- stage: `pericope-compiler`
- unit: `single-ayah`
- surah: 100
- target language: `tr`
- generated: `2026-07-29`
- expected outputs:
  - `_commentary/v2/generated/s100-1-gpt56-sol-xhigh/shared/compiler/outputs/single-ayah.editorial-plan.json`
  - `_commentary/v2/generated/s100-1-gpt56-sol-xhigh/shared/compiler/outputs/single-ayah.channel-registry.json`
  - `_commentary/v2/generated/s100-1-gpt56-sol-xhigh/shared/compiler/outputs/single-ayah.friction.md`
- inlined sources:
  - `_commentary/v2/shared/compiler/PROMPT.md` - 2,328 bytes - `906b05312c4274b53e1c9c64308dc5d266ddbd82dab4ba6f4d4680c7c2441aa8`
  - `_commentary/v2/shared/EDITORIAL_CONTRACT.md` - 3,625 bytes - `530b89dae5b574671250452dd788e77de3f83d01e949b5538b68c70030efe2f4`
  - `_commentary/v2/shared/schemas/pericope-editorial-plan.schema.json` - 7,031 bytes - `59cdebfbdc70df4a5da606fd02b621ec35e31554854fca65676f0af61b40728e`
  - `_commentary/v2/shared/schemas/channel-registry.schema.json` - 3,619 bytes - `880b78b01960ccb151aa19dec6ea6575f11c81600fba56f237197adfe218c817`
  - `s100-1-gpt56-sol-xhigh/single-ayah.compiler-input.json` - 225 bytes - `69bf3b96e9b95acc010447d6af20f6a5a4e0b392f2a0018c99accff11df9ce61`
  - `_commentary/v2/generated/s100-1-gpt56-sol-xhigh/layer_2/discovery/outputs/100_1.ledger.json` - 78,241 bytes - `b1a5096ab9d7ca5a0d9d152f2ab6f244767935755309d8aaf03f119ab8af0547`

**Hermeticity rule:** use only the material inlined below. Source paths are provenance identities, not instructions to browse.

**Response rule:** write exactly the expected output files. Do not add an unrequested artifact or place one artifact inside another.

---

## task: `_commentary/v2/shared/compiler/PROMPT.md`

```markdown
# Pericope Editorial Compiler Prompt

Read the inlined editorial contract and both output schemas. The attached
discovery ledgers cover one editorial pericope.

## Task

Produce:

1. `{PERICOPE}.editorial-plan.json`
2. `{PERICOPE}.channel-registry.json`
3. `{PERICOPE}.friction.md`

This is planning, not final prose.

## Editorial plan

Construct one ayah plan for every ayah in the pericope.

- Give each ayah a reachable primary floor and a governing movement.
- Arrange placements in reading order.
- Attach every carried finding ID to at least one placement.
- Merge repeated explanation only by placing all affected finding IDs together.
- Preserve contradictory or parallel pressures when the ledgers preserve them.
- Create editorial syntheses when several findings form a grounded new reading.
- Give every synthesis a local owner ayah, component finding IDs, evidence
  references, support level, and primary relation.
- Keep every ayah independently intelligible. A later ayah may activate a
  finding, but the plan must provide the triggering word or image rather than
  assume the reader knows it.

There is no target number of placements, findings, or syntheses. Density follows
the evidence.

## Channel registry

Nominate cross-ayah systems separately from the ayah plans.

- A channel candidate needs members from at least two ayahs.
- Each member points to a carried finding and states its contribution.
- State the invariant that makes the members one system.
- State the reasoning chain rather than merely listing motifs.
- Preserve counterevidence and uncertain joins.
- Do not remove a finding from Layer 2 because it also belongs to Layer 3.
- Do not force every finding into a channel.

## Coverage

The plan's `findingCoverage` must account for every discovery finding:

- `represented` for every `carry` finding, with an ayah and placement;
- `upstream-blocked` for every discovery finding already marked `blocked`.

The compiler may not create a new blocked disposition.

Copy the `sourceLedgers` array exactly from the compiler input descriptor into
both JSON outputs. Do not calculate, reorder, or normalize the hashes.

## Friction

Record unresolved duplicate identities, contradictory ledgers, uncertain
pericope boundaries, and channel candidates that may continue outside the
current pericope.
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

## schema: `_commentary/v2/shared/schemas/pericope-editorial-plan.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "commentary-v2-pericope-editorial-plan.schema.json",
  "title": "Commentary v2 pericope editorial plan",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schemaVersion",
    "surah",
    "pericopeId",
    "ayahRefs",
    "sourceLedgers",
    "ayahPlans",
    "findingCoverage",
    "editorialSyntheses"
  ],
  "properties": {
    "schemaVersion": {
      "const": "commentary-v2-pericope-editorial-plan-v1"
    },
    "surah": {
      "type": "integer",
      "minimum": 1,
      "maximum": 114
    },
    "pericopeId": {
      "$ref": "#/$defs/id"
    },
    "ayahRefs": {
      "type": "array",
      "minItems": 1,
      "uniqueItems": true,
      "items": {
        "$ref": "#/$defs/ayahRef"
      }
    },
    "sourceLedgers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "ayahRef",
          "sha256"
        ],
        "properties": {
          "ayahRef": {
            "$ref": "#/$defs/ayahRef"
          },
          "sha256": {
            "$ref": "#/$defs/sha256"
          }
        }
      }
    },
    "ayahPlans": {
      "type": "array",
      "minItems": 1,
      "items": {
        "$ref": "#/$defs/ayahPlan"
      }
    },
    "findingCoverage": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/findingCoverage"
      }
    },
    "editorialSyntheses": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/editorialSynthesis"
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
    "synthesisRef": {
      "type": "string",
      "pattern": "^editorial:[a-z0-9]+(?:-[a-z0-9]+)*$"
    },
    "sha256": {
      "type": "string",
      "pattern": "^[a-f0-9]{64}$"
    },
    "placement": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "placementId",
        "movementRole",
        "findingRefs",
        "synthesisRefs",
        "paragraphPurpose_tr",
        "localReturn_tr"
      ],
      "properties": {
        "placementId": {
          "$ref": "#/$defs/id"
        },
        "movementRole": {
          "enum": [
            "grounding",
            "development",
            "surprise-turn",
            "counterpressure",
            "return"
          ]
        },
        "findingRefs": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/findingRef"
          }
        },
        "synthesisRefs": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/synthesisRef"
          }
        },
        "paragraphPurpose_tr": {
          "type": "string",
          "minLength": 1
        },
        "beforeAfterTurn_tr": {
          "type": "string"
        },
        "localReturn_tr": {
          "type": "string",
          "minLength": 1
        },
        "groundedCrossAyahRefs": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/ayahRef"
          }
        }
      }
    },
    "ayahPlan": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "ayahRef",
        "primaryFloor_tr",
        "governingMovement_tr",
        "placements",
        "standaloneRequirement_tr",
        "layer3HandoffIds"
      ],
      "properties": {
        "ayahRef": {
          "$ref": "#/$defs/ayahRef"
        },
        "primaryFloor_tr": {
          "type": "string",
          "minLength": 1
        },
        "governingMovement_tr": {
          "type": "string",
          "minLength": 1
        },
        "placements": {
          "type": "array",
          "minItems": 1,
          "items": {
            "$ref": "#/$defs/placement"
          }
        },
        "standaloneRequirement_tr": {
          "type": "string",
          "minLength": 1
        },
        "layer3HandoffIds": {
          "type": "array",
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/id"
          }
        }
      }
    },
    "findingCoverage": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "findingRef",
        "sourceAyahRef",
        "disposition"
      ],
      "properties": {
        "findingRef": {
          "$ref": "#/$defs/findingRef"
        },
        "sourceAyahRef": {
          "$ref": "#/$defs/ayahRef"
        },
        "disposition": {
          "enum": [
            "represented",
            "upstream-blocked"
          ]
        },
        "ownerAyahRef": {
          "$ref": "#/$defs/ayahRef"
        },
        "placementId": {
          "$ref": "#/$defs/id"
        },
        "reason_tr": {
          "type": "string"
        }
      },
      "allOf": [
        {
          "if": {
            "properties": {
              "disposition": {
                "const": "represented"
              }
            }
          },
          "then": {
            "required": [
              "ownerAyahRef",
              "placementId"
            ]
          },
          "else": {
            "required": [
              "reason_tr"
            ]
          }
        }
      ]
    },
    "editorialSynthesis": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "synthesisId",
        "ownerAyahRef",
        "componentFindingRefs",
        "relation",
        "supportLevel",
        "claim_tr",
        "localReturn_tr",
        "evidenceRefs"
      ],
      "properties": {
        "synthesisId": {
          "$ref": "#/$defs/synthesisRef"
        },
        "ownerAyahRef": {
          "$ref": "#/$defs/ayahRef"
        },
        "componentFindingRefs": {
          "type": "array",
          "minItems": 2,
          "uniqueItems": true,
          "items": {
            "$ref": "#/$defs/findingRef"
          }
        },
        "relation": {
          "enum": [
            "supports-primary",
            "shifts-primary",
            "parallel-pressure"
          ]
        },
        "supportLevel": {
          "enum": [
            "local-inference",
            "contextual-inference",
            "remote-lexical",
            "synthetic"
          ]
        },
        "claim_tr": {
          "type": "string",
          "minLength": 1
        },
        "localReturn_tr": {
          "type": "string",
          "minLength": 1
        },
        "evidenceRefs": {
          "type": "array",
          "minItems": 1,
          "uniqueItems": true,
          "items": {
            "type": "string",
            "minLength": 1
          }
        }
      }
    }
  }
}
```

---

## schema: `_commentary/v2/shared/schemas/channel-registry.schema.json`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "commentary-v2-channel-registry.schema.json",
  "title": "Commentary v2 channel candidate registry",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schemaVersion",
    "surah",
    "pericopeId",
    "sourceLedgers",
    "channels"
  ],
  "properties": {
    "schemaVersion": {
      "const": "commentary-v2-channel-registry-v1"
    },
    "surah": {
      "type": "integer",
      "minimum": 1,
      "maximum": 114
    },
    "pericopeId": {
      "$ref": "#/$defs/id"
    },
    "sourceLedgers": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "ayahRef",
          "sha256"
        ],
        "properties": {
          "ayahRef": {
            "$ref": "#/$defs/ayahRef"
          },
          "sha256": {
            "$ref": "#/$defs/sha256"
          }
        }
      }
    },
    "channels": {
      "type": "array",
      "items": {
        "$ref": "#/$defs/channel"
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
    "member": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "memberId",
        "findingRef",
        "ayahRef",
        "localAnchor_tr",
        "contribution_tr",
        "evidenceRefs"
      ],
      "properties": {
        "memberId": {
          "$ref": "#/$defs/id"
        },
        "findingRef": {
          "$ref": "#/$defs/findingRef"
        },
        "ayahRef": {
          "$ref": "#/$defs/ayahRef"
        },
        "localAnchor_tr": {
          "type": "string",
          "minLength": 1
        },
        "contribution_tr": {
          "type": "string",
          "minLength": 1
        },
        "evidenceRefs": {
          "type": "array",
          "minItems": 1,
          "uniqueItems": true,
          "items": {
            "type": "string",
            "minLength": 1
          }
        }
      }
    },
    "channel": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "candidateId",
        "name_tr",
        "invariant_tr",
        "reasoningChain_tr",
        "members",
        "counterEvidence",
        "crossPericopeStatus"
      ],
      "properties": {
        "candidateId": {
          "$ref": "#/$defs/id"
        },
        "name_tr": {
          "type": "string",
          "minLength": 1
        },
        "invariant_tr": {
          "type": "string",
          "minLength": 1
        },
        "reasoningChain_tr": {
          "type": "array",
          "minItems": 1,
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "members": {
          "type": "array",
          "minItems": 2,
          "items": {
            "$ref": "#/$defs/member"
          }
        },
        "counterEvidence": {
          "type": "array",
          "items": {
            "type": "string",
            "minLength": 1
          }
        },
        "crossPericopeStatus": {
          "enum": [
            "self-contained",
            "may-continue",
            "known-continuation"
          ]
        }
      }
    }
  }
}
```

---

## compiler-input: `s100-1-gpt56-sol-xhigh/single-ayah.compiler-input.json`

```json
{"schemaVersion":"commentary-v2-compiler-input-v1","surah":100,"pericopeId":"single-ayah","ayahRefs":["100:1"],"sourceLedgers":[{"ayahRef":"100:1","sha256":"f32dceccacd4120e1f538c1001ebd451e6c598800d1c28a383cdd3f0e9f89cbe"}]}
```

---

## discovery-ledger: `_commentary/v2/generated/s100-1-gpt56-sol-xhigh/layer_2/discovery/outputs/100_1.ledger.json`

```json
{"schemaVersion":"commentary-v2-layer2-discovery-v1","surah":100,"ayahRef":"100:1","language":"tr","primaryFloor_tr":"Soluk soluğa koşanlara andolsun.","sourceObligations":[{"sourceRef":"text:quran-uthmani.tsv#100:1","disposition":"carry","findingRefs":["100:1:oath-evidence","100:1:action-defined-plural","100:1:breath-manner"]},{"sourceRef":"qac:morphemes#100:1","disposition":"carry","findingRefs":["100:1:oath-evidence","100:1:fused-launch","100:1:action-defined-plural","100:1:breath-manner","100:1:unbounded-panting"]},{"sourceRef":"word-morpheme-spans:100:1","disposition":"carry","findingRefs":["100:1:oath-evidence","100:1:action-defined-plural","100:1:breath-manner"]},{"sourceRef":"word-analysis:100:1","disposition":"carry","findingRefs":["100:1:oath-evidence","100:1:oath-suspense","100:1:fused-launch","100:1:action-defined-plural","100:1:referent-open","100:1:hostile-boundary-pressure","100:1:dawn-going-variant","100:1:participial-chain","100:1:rush-breath-cadence","100:1:breath-manner","100:1:unbounded-panting","100:1:hapax-local-load","100:1:rough-exhalation","100:1:dawn-time-variant","100:1:compact-oath-scene","100:1:scorch-arc","100:1:ignition-chain"]},{"sourceRef":"root-lexicon:root_000993","disposition":"carry","findingRefs":["100:1:embodied-exertion","100:1:hostile-boundary-pressure","100:1:prepared-succession","100:1:scorch-arc","100:1:seasonal-hard-route","100:1:ignition-chain","100:1:temporal-threshold","100:1:residual-trail","100:1:coordinated-penetration","100:1:desire-as-charge","100:1:causal-engine","100:1:contagious-desire","100:1:edge-to-center","100:1:redress-run","100:1:transmitted-fire","100:1:watering-route","100:1:counted-pulses"]},{"sourceRef":"root-lexicon:root_000989","disposition":"carry","findingRefs":["100:1:prepared-succession","100:1:coordinated-penetration","100:1:counted-pulses"]},{"sourceRef":"root-lexicon:root_001058","disposition":"carry","findingRefs":["100:1:habitual-return","100:1:seasonal-hard-route","100:1:service-ingratitude","100:1:forward-return","100:1:known-service","100:1:watering-route"]},{"sourceRef":"root-lexicon:root_000901","disposition":"carry","findingRefs":["100:1:embodied-exertion","100:1:scorch-arc","100:1:seasonal-hard-route","100:1:ignition-chain","100:1:residual-trail","100:1:service-ingratitude","100:1:embodied-witness","100:1:interior-exhales","100:1:causal-engine","100:1:transmitted-fire","100:1:watering-route","100:1:useless-spark","100:1:rising-breath"]},{"sourceRef":"branch-inventories:full-context-packet","disposition":"carry","findingRefs":["100:1:ignition-chain","100:1:temporal-threshold","100:1:residual-trail","100:1:coordinated-penetration","100:1:service-ingratitude","100:1:embodied-witness","100:1:desire-as-charge","100:1:forward-return","100:1:interior-exhales","100:1:known-service","100:1:redress-run","100:1:transmitted-fire","100:1:watering-route","100:1:useless-spark","100:1:counted-pulses","100:1:rising-breath"]},{"sourceRef":"focus-trace:reader_hft_a:100:1","disposition":"carry","findingRefs":["100:1:embodied-exertion","100:1:hostile-boundary-pressure","100:1:habitual-return","100:1:prepared-succession","100:1:scorch-arc","100:1:seasonal-hard-route","100:1:ignition-chain","100:1:temporal-threshold","100:1:residual-trail","100:1:coordinated-penetration","100:1:service-ingratitude","100:1:embodied-witness","100:1:desire-as-charge","100:1:forward-return","100:1:interior-exhales","100:1:known-service","100:1:redress-run","100:1:transmitted-fire","100:1:watering-route","100:1:useless-spark","100:1:counted-pulses","100:1:rising-breath"]},{"sourceRef":"reader-walk:reader_b:100:1","disposition":"carry","findingRefs":["100:1:hostile-boundary-pressure","100:1:contagious-desire","100:1:edge-to-center"]},{"sourceRef":"reader-walk-wide:reader_a:100:1","disposition":"carry","findingRefs":["100:1:embodied-exertion","100:1:ignition-chain","100:1:temporal-threshold","100:1:causal-engine"]},{"sourceRef":"cross-run-publication:100:1","disposition":"carry","findingRefs":["100:1:hostile-boundary-pressure","100:1:scorch-arc","100:1:causal-engine","100:1:contagious-desire","100:1:edge-to-center"]},{"sourceRef":"butuncul-okuma:100:1","disposition":"carry","findingRefs":["100:1:hostile-boundary-pressure","100:1:contagious-desire","100:1:edge-to-center"]},{"sourceRef":"inter-ayah:100:1","disposition":"carry","findingRefs":["100:1:oath-evidence","100:1:equine-frame","100:1:hostile-boundary-pressure","100:1:ignition-chain","100:1:causal-engine","100:1:edge-to-center"]},{"sourceRef":"channel-review:reader_a_pilot:100:1","disposition":"carry","findingRefs":["100:1:embodied-exertion","100:1:hostile-boundary-pressure","100:1:scorch-arc","100:1:ignition-chain","100:1:residual-trail","100:1:coordinated-penetration","100:1:service-ingratitude","100:1:embodied-witness","100:1:desire-as-charge","100:1:contagious-desire","100:1:edge-to-center","100:1:redress-run","100:1:watering-route"]},{"sourceRef":"v12-reader-responses:100:1","disposition":"blocked","findingRefs":[],"blockingEvidence":["coverage.v12_reader_responses.present=false","Per-ayah focus-run reader responses are retired from the default commentary workflow."]},{"sourceRef":"channel-generated-outputs:network-v3:s100","disposition":"blocked","findingRefs":[],"blockingEvidence":["Only an external-source manifest is inlined; generated file contents are absent from the prompt.","Hermeticity forbids opening the listed external paths.","coverage.channel_generated_outputs.missing_expected_files includes paths/path_families/semantic_path_families.jsonl.gz."]}],"findings":[{"findingId":"100:1:oath-evidence","disposition":"carry","kind":"ayah-function","relation":"primary-floor","supportLevel":"direct","localAnchors":[{"surface_ar":"وَ","surface_tr":"ve/andolsun","function_tr":"Basit bağlaç değil, ardından gelen mecrur öbeği yemin nesnesi yapan yemin edatıdır.","qacRefs":["100:1:1:1"],"evidenceRefs":["word-analysis:100:1:1:oath-governance","qac:100:1:1:1"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Ayet hızlı ve soluklu bir hareket görüntüsü verir.","readingAfter_tr":"Bu görüntü yalnız betimlenmez; surenin hükmüne delil olarak yemin alanına alınır.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında وَ, koşu görüntüsünü sıradan bir devam cümlesi olmaktan çıkarıp yemin deliline dönüştürür.","readerPayoff_tr":"Okur, ilk görüntünün neden bu kadar ağırlıklı sunulduğunu ve sonraki hükme nasıl kanıt taşıdığını görür.","sourceClaimRefs":["word-analysis:100:1:1:oath-governance","qac:morph:100:1:1:1"],"evidenceRefs":["QG-df4c11b9","QS-27d02d8b","QT-d847139e","100:1:1:1"],"activationTriggers":[],"counterEvidence":[],"channelTags":["oath-sequence"]},{"findingId":"100:1:oath-suspense","disposition":"carry","kind":"grammar","relation":"supports-primary","supportLevel":"direct","localAnchors":[{"surface_ar":"وَ","surface_tr":"andolsun","function_tr":"Söylenmeyen yemin fiilini tek harfte sıkıştırır ve cevabı geciktirir.","qacRefs":["100:1:1:1"],"evidenceRefs":["word-analysis:100:1:1:compressed-delayed-qasam"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"İlk ayet kendi başına tamamlanan kısa bir yemin gibi duyulur.","readingAfter_tr":"100:6'daki cevap gelene kadar ilk beş ayet tek harfin açtığı beklentiyi taşır.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması, وَ içinde sıkışmış yemin eylemi ve 100:6'ya dek geciken cevap sayesinde daha ilk anda ileriye dönük bir gerilim kurar.","readerPayoff_tr":"Okur, açılışın niçin tamamlanmamış bir vaat gibi ilerlediğini fark eder.","sourceClaimRefs":["word-analysis:100:1:1:compressed-delayed-qasam"],"evidenceRefs":["MG-f182b034","QI-65124881","QT-923d29b2"],"activationTriggers":[{"ayahRef":"100:6","wordSpan":"إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌ","effect_tr":"Geciktirilen yemin cevabını görünür kılar.","evidenceRefs":["word-analysis:100:1:1:compressed-delayed-qasam","focus-trace:C05_SERVICE_INGRATITUDE"]}],"counterEvidence":[],"channelTags":["oath-sequence","delayed-answer"]},{"findingId":"100:1:fused-launch","disposition":"carry","kind":"sound-form","relation":"supports-primary","supportLevel":"local-inference","localAnchors":[{"surface_ar":"وَٱلْعَٰدِيَٰتِ","surface_tr":"ve koşanlara","function_tr":"Yemin edatı yazı ve okuyuşta nesnesine bağlanarak görüntüyü tek hamlede başlatır.","qacRefs":["100:1:1:1","100:1:1:2","100:1:1:3"],"evidenceRefs":["word-analysis:100:1:1:fused-audible-launch"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Yemin edatı ile koşu adı iki ayrı dil birimi olarak görülebilir.","readingAfter_tr":"Bağlı yazım ve okuyuş, yemin ile koşuyu tek sesli fırlayış hâline getirir.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında وَٱلْعَٰدِيَٰتِ, yemin ile koşu görüntüsünü işitilir biçimde tek bir başlangıç hamlesinde birleştirir.","readerPayoff_tr":"Okur, ayetin hareketi anlatmadan önce ses düzeyinde başlattığını duyar.","sourceClaimRefs":["word-analysis:100:1:1:fused-audible-launch"],"evidenceRefs":["QF-df7e6be6","QP-8e720064","QY-af82e14c","100:1:1:1","100:1:1:2","100:1:1:3"],"activationTriggers":[],"counterEvidence":[],"channelTags":["audible-motion"]},{"findingId":"100:1:action-defined-plural","disposition":"carry","kind":"grammar","relation":"primary-floor","supportLevel":"direct","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Belirli dişil çoğul etken ortaç, topluluğu tür adıyla değil yaptığı koşu eylemiyle tanımlar ve yemin nesnesi yapar.","qacRefs":["100:1:1:2","100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["word-analysis:100:1:2:participial-oath-object","root_000993/B002"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Ayet, belirli bir hayvan veya topluluk adı anıyor gibi varsayılabilir.","readingAfter_tr":"Dilbilgisi, kimlikten önce eylemi verir: yemin edilenler koşmalarıyla tanınır.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında ٱلْعَٰدِيَٰتِ, yemin edilen çoğulu türüyle değil, sürmekte olan koşu eylemiyle görünür kılar.","readerPayoff_tr":"Okur, ayetin kim koşuyor sorusundan önce ne yaptıklarını ve nasıl tanındıklarını öne çıkardığını görür.","sourceClaimRefs":["word-analysis:100:1:2:participial-oath-object","qac:morph:100:1:1:3"],"evidenceRefs":["QG-710929bb","QG-d893a8fb","QT-fdda5be9","100:1:1:3","root_000993/B002"],"activationTriggers":[],"counterEvidence":[],"channelTags":["action-class","oath-sequence"]},{"findingId":"100:1:referent-open","disposition":"carry","kind":"counterpressure","relation":"parallel-pressure","supportLevel":"direct","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Belirli dişil çoğul biçim tanınabilir bir sınıf kurar, fakat ayette açık bir tür adı vermez.","qacRefs":["100:1:1:2","100:1:1:3"],"rootId":"root_000993","evidenceRefs":["word-analysis:100:1:2:referent-underdetermination"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşan çoğulun at, deve, insan veya başka bir varlık olduğu hemen seçilebilir sanılır.","readingAfter_tr":"Yerel biçim hareketi kesinleştirir, fakat türü açık bırakır.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması koşuyu korurken, ٱلْعَٰدِيَٰتِ'in açık bir tür adı taşımaması yemin edilen çoğulun kimliğini yerel düzeyde kapatmaz.","readerPayoff_tr":"Okur, görüntünün bedensel gücünü belirli bir zoolojik veya askerî kimliğe erken kilitlenmeden alabilir.","sourceClaimRefs":["word-analysis:100:1:2:referent-underdetermination"],"evidenceRefs":["QG-b5328a58","QS-437bf911","QF-6ec900e2","MS-1e2cc65d"],"activationTriggers":[],"counterEvidence":["Inter-ayah rows 38:31, 59:6, 8:60 and 16:8 make an equine or martial frame plausible but do not force it.","The focus-trace explicitly declines zoological, military, human, or cosmic identification."],"channelTags":["referent-openness"]},{"findingId":"100:1:equine-frame","disposition":"carry","kind":"local-resonance","relation":"supports-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ ضَبْحًا","surface_tr":"soluk soluğa koşanlar","function_tr":"Koşu ortacı ile koşan atın ağız/soluk sesini ve uzatılmış ön bacak yürüyüşünü birlikte taşır.","qacRefs":["100:1:1:3","100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["root_000993/B002","root_000901/B001","root_000901/B002"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Yerel dilbilgisi, koşan sınıfın türünü açık bırakır.","readingAfter_tr":"Yakın Kur'an içi at ve askerî hareket paralelleri, atlı koşu çerçevesini somut ve sınanabilir kılar; yine de tek referent yapmaz.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında açık kalan çoğul, 38:31, 59:6 ve 8:60'ın atlı hareket bağlamlarıyla birlikte at ve askerî koşu çerçevesinde somutlaşabilir, fakat yerel açıklık korunur.","readerPayoff_tr":"Okur, geleneksel atlı sahnenin metinsel dayanağını görürken onu ayetin tek mümkün kimliği sanmaz.","sourceClaimRefs":["inter-ayah:38:31","inter-ayah:59:6","inter-ayah:8:60","word-analysis:100:1:2:referent-underdetermination"],"evidenceRefs":["inter-ayah:38:31:strong","inter-ayah:59:6:strong","inter-ayah:8:60:strong","inter-ayah:16:8:medium","root_000901/B001","root_000901/B002"],"activationTriggers":[],"counterEvidence":["The local grammar supplies no overt species noun.","Contextual referent data is too distributed to force one referent."],"channelTags":["equine-frame","martial-motion"]},{"findingId":"100:1:hostile-boundary-pressure","disposition":"carry","kind":"local-resonance","relation":"shifts-primary","supportLevel":"local-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Koşu anlamı seçilirken aynı baskın kök alanındaki sınır aşma, saldırganlık ve düşmanlık hareketi nötr olmaktan çıkarır.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B001","evidenceRefs":["root_000993/B001","root_000993/B002","root_000993/B003","root_000993/B004","focus-trace:B02_BOUNDARY_OVERRUN"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşu yalnız hız ve yer değiştirme olarak duyulur.","readingAfter_tr":"Koşu, sınırı aşan ve düşman alana basınç uygulayan bedensel bir hamle olarak da duyulur; ahlaki ve salt mekânsal aşım birlikte kalır.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması korunurken, ٱلْعَٰدِيَٰتِ'in sınır aşma ve düşmanlık basıncı koşuyu nötr bir hızdan bedensel bir eşik ihlaline doğru genişletir.","readerPayoff_tr":"Okur, koşunun niçin yalnız sürat değil yönelmiş ve gerilimli bir kuvvet gibi duyulduğunu anlar.","sourceClaimRefs":["word-analysis:100:1:2:kinetic-adversarial-root-pressure","focus-trace:B02_BOUNDARY_OVERRUN","reader-walk:reader_b:reading-1","cross-run-publication:finding-2","butuncul-okuma:100:1"],"evidenceRefs":["QS-0f57d3dc","QS-81fc23e4","QI-7946c04e","root_000993/B001","root_000993/B002","root_000993/B003","root_000993/B004","inter-ayah:26:77:strong","inter-ayah:6:108:strong"],"activationTriggers":[],"counterEvidence":["100:6 assigns the explicit negative moral diagnosis to the human, not to the runners.","The focus-trace retains non-hostile spatial crossing beside aggressive overrun."],"channelTags":["boundary-crossing","martial-motion"]},{"findingId":"100:1:dawn-going-variant","disposition":"carry","kind":"counterpressure","relation":"parallel-pressure","supportLevel":"direct","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Standart yüzey, bildirilen ٱلْغَادِيَٰتِ varyantının doğan gidişine karşı koşu ve sınır basıncını öne çıkarır.","qacRefs":["100:1:1:2","100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["word-analysis:100:1:2:dawn-variant-contrast"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Açılış hareketi zaman bakımından belirsizdir.","readingAfter_tr":"Varyant doğan gidişi hemen öne çıkarabilecekken standart biçim önce koşu ve baskıyı seçer.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında standart ٱلْعَٰدِيَٰتِ, bildirilen ٱلْغَادِيَٰتِ varyantının doğan gidişi yerine hareket ve sınır basıncını öne alır.","readerPayoff_tr":"Okur, standart biçimin zaman adından önce hareketi neden duyurduğunu karşılaştırma yoluyla görür.","sourceClaimRefs":["word-analysis:100:1:2:dawn-variant-contrast"],"evidenceRefs":["QF-599acfe7","QE-6bbcddaa"],"activationTriggers":[],"counterEvidence":["The reported variant is contrastive evidence and does not replace the standard aligned surface."],"channelTags":["variant-pressure","dawn-motion"]},{"findingId":"100:1:participial-chain","disposition":"carry","kind":"context-activation","relation":"supports-primary","supportLevel":"direct","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"İlk dişil çoğul ortaç, 100:2 ve 100:3'te süren yemin ortaçlarının kalıbını kurar.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["word-analysis:100:1:2:participial-oath-chain"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"İlk ortaç tek bir koşan sınıfı adlandırır.","readingAfter_tr":"Sonraki ortaçlar bu ilk biçimin açtığı diziyi sürdürür; koşu, kıvılcım ve sabah hareketi aynı yemin zincirinde okunur.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasındaki ٱلْعَٰدِيَٰتِ, 100:2 ve 100:3'teki ortaçların izlediği biçimsel yemin zincirini başlatır.","readerPayoff_tr":"Okur, ilk ayetin sonraki görüntüleri yalnız konu bakımından değil biçim bakımından da öğrettiğini fark eder.","sourceClaimRefs":["word-analysis:100:1:2:participial-oath-chain"],"evidenceRefs":["QE-71fde5eb","QY-5f92804b"],"activationTriggers":[{"ayahRef":"100:2","wordSpan":"فَٱلْمُورِيَٰتِ","effect_tr":"İlk ortaç kalıbını kıvılcım çıkaran çoğulla sürdürür.","evidenceRefs":["QE-71fde5eb"]},{"ayahRef":"100:3","wordSpan":"فَٱلْمُغِيرَٰتِ","effect_tr":"Aynı kalıbı sabah hareketine taşır.","evidenceRefs":["QY-5f92804b"]}],"counterEvidence":[],"channelTags":["oath-sequence","participial-chain"]},{"findingId":"100:1:rush-breath-cadence","disposition":"carry","kind":"sound-form","relation":"supports-primary","supportLevel":"local-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ ضَبْحًا","surface_tr":"koşanlar, soluk soluğa","function_tr":"Uzun ortaç biçimi daha kısa nefes sözüne akarak uzatılmış koşu ile kesik soluk arasında işitsel karşıtlık kurar.","qacRefs":["100:1:1:3","100:1:2:1"],"evidenceRefs":["word-analysis:100:1:2:cadence-and-breath-contrast"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşu ve soluk iki sözlük anlamı olarak yan yana durur.","readingAfter_tr":"Uzayan koşu sözü kısa nefes sözüne çarpar; anlam ses dizilişinde bedenselleşir.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında uzun ٱلْعَٰدِيَٰتِ biçiminin kısa ضَبْحًا'ya akışı, uzayan koşuyu kesik soluğa işitsel olarak bağlar.","readerPayoff_tr":"Okur, hız ile soluk maliyetinin ayetin ritminde birbirine dönüştüğünü duyar.","sourceClaimRefs":["word-analysis:100:1:2:cadence-and-breath-contrast"],"evidenceRefs":["QF-81ef9b4f","QP-d4e9ce3a","QP-ea88af62"],"activationTriggers":[],"counterEvidence":[],"channelTags":["audible-motion","embodied-exertion"]},{"findingId":"100:1:breath-manner","disposition":"carry","kind":"grammar","relation":"primary-floor","supportLevel":"direct","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Belirsiz mansup mastar, soluklanmayı ikinci bir olay değil koşunun tarzı veya hâli yapar.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["word-analysis:100:1:3:accusative-manner-state","qac:100:1:2:1"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşu ve soluk iki ayrı olay gibi okunabilir.","readingAfter_tr":"Mansup mastar soluğu koşunun içine katıp onun nasıl gerçekleştiğini bildirir.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında ضَبْحًا, yeni bir olay eklemek yerine soluklanmayı koşunun hâli ve gerçekleşme tarzı yapar.","readerPayoff_tr":"Okur, ayetin koşanları dışarıdan değil, çabanın beden içindeki belirtisiyle tanıttığını görür.","sourceClaimRefs":["word-analysis:100:1:3:accusative-manner-state","qac:morph:100:1:2:1"],"evidenceRefs":["QG-9c95286b","QG-c3502dbd","QF-7ed8dfc3","100:1:2:1","root_000901/B001"],"activationTriggers":[],"counterEvidence":[],"channelTags":["embodied-exertion"]},{"findingId":"100:1:unbounded-panting","disposition":"carry","kind":"grammar","relation":"supports-primary","supportLevel":"local-inference","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"bir soluklanış hâlinde","function_tr":"Tenvin ve belirsizlik soluğu tek sayılmış ses olmaktan çıkarıp hareket boyunca yayılan hâl olarak duyurur.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["word-analysis:100:1:3:unbounded-breath"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"ضَبْحًا tek bir adlandırılmış ses olarak alınabilir.","readingAfter_tr":"Belirsiz biçim, nefesi koşu boyunca yinelenen ve sınırı çizilmemiş bir hâl yapar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında ضَبْحًا'nın belirsizliği, soluğu tek bir ses değil koşu boyunca yayılan bir beden hâli olarak işittirir.","readerPayoff_tr":"Okur, ayetin bir anı değil sürmekte olan eforu duyurduğunu kavrar.","sourceClaimRefs":["word-analysis:100:1:3:unbounded-breath"],"evidenceRefs":["QG-ef5d44ec","100:1:2:1"],"activationTriggers":[],"counterEvidence":[],"channelTags":["embodied-exertion","repeated-breath"]},{"findingId":"100:1:hapax-local-load","disposition":"carry","kind":"counterpressure","relation":"supports-primary","supportLevel":"direct","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Paket, bu kök-biçim için başka Kur'an içi kullanım vermediğinden anlam yükünü yerel dilbilgisi, ses, varyant ve dizi taşır.","qacRefs":["100:1:2:1"],"rootId":"root_000901","evidenceRefs":["word-analysis:100:1:3:hapax-local-load","coverage.root_lexicon:root_000901:occurrences=1"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Sözcüğün kayıtlı başka Kur'an örnekleri anlam alanını denetleyebilir sanılır.","readingAfter_tr":"Paket içindeki tek kullanım bu ayet olduğundan yerel bağ, biçim ve ses olağandışı ölçüde belirleyicidir.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasındaki ضَبْحًا, pakette tek Kur'an kullanımı olarak bulunduğu için anlamını özellikle bu ayetin dilbilgisi, sesi ve yakın dizisinden kazanır.","readerPayoff_tr":"Okur, nadir sözcüğün küçük biçim özelliklerinin niçin yorumda büyük ağırlık taşıdığını anlar.","sourceClaimRefs":["word-analysis:100:1:3:hapax-local-load"],"evidenceRefs":["QS-74781736","QI-f0250a3f","QH-1a291f76","coverage.root_lexicon:root_000901:occurrences=1"],"activationTriggers":[],"counterEvidence":["Per-occurrence concordance rows were intentionally trimmed from the packet, but the retained summary reports one occurrence."],"channelTags":["local-load"]},{"findingId":"100:1:rough-exhalation","disposition":"carry","kind":"sound-form","relation":"supports-primary","supportLevel":"local-inference","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Ayet sonundaki yoğun ünsüz dokusu, uzun koşu sözünün ardından kaba ve işitilir bir nefes inişi üretir.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["word-analysis:100:1:3:final-audible-landing"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Ayet hareketi adlandırıp sona erer.","readingAfter_tr":"Son sözcüğün sesi, hareketin ardından çıkan zorlanmış nefesi ayetin kapanışına bırakır.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması ضَبْحًا'nın kaba ünsüz inişiyle, koşunun ardından işitilen zorlanmış bir soluk üzerinde kapanır.","readerPayoff_tr":"Okur, ayetin son izleniminin görüntü değil bedenden çıkan ses olduğunu duyar.","sourceClaimRefs":["word-analysis:100:1:3:final-audible-landing"],"evidenceRefs":["QT-fcb03a32","QP-583159a8","QP-9cfc543a"],"activationTriggers":[],"counterEvidence":[],"channelTags":["audible-motion","rough-exhalation"]},{"findingId":"100:1:dawn-time-variant","disposition":"carry","kind":"counterpressure","relation":"parallel-pressure","supportLevel":"direct","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Bildirilen صُبْحًا varyantı aynı mansup konumu nefes hâlinden sabah zamanına çevirirken standart yüzey duyusal soluğu seçer.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["word-analysis:100:1:3:dawn-variant-contrast"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Ayetin son mansup sözü yalnız nefes tarzını bildirir.","readingAfter_tr":"Varyant aynı yeri sabah zamanı yapabilirdi; standart biçim sabahı geciktirip önce ses, çaba ve ısıyı bırakır.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında standart ضَبْحًا, bildirilen صُبْحًا varyantının sabah zamanını hemen adlandırması yerine önce duyusal nefesi ve çabayı seçer.","readerPayoff_tr":"Okur, sabahın 100:3'e bırakılmasının ilk ayeti nasıl bedensel ve işitsel tuttuğunu görür.","sourceClaimRefs":["word-analysis:100:1:3:dawn-variant-contrast"],"evidenceRefs":["QF-efea91d0","QI-baf059b0","QE-383139f7"],"activationTriggers":[],"counterEvidence":["The reported variant is contrastive evidence and does not control the standard local parse."],"channelTags":["variant-pressure","dawn-motion"]},{"findingId":"100:1:compact-oath-scene","disposition":"carry","kind":"ayah-function","relation":"supports-primary","supportLevel":"direct","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ ضَبْحًا","surface_tr":"soluk soluğa koşanlar","function_tr":"Ortaç başı ile ona bağlı hâl mastarı tam bir anlatı cümlesi değil, sıkıştırılmış bir yemin sahnesi kurar.","qacRefs":["100:1:1:3","100:1:2:1"],"evidenceRefs":["word-analysis:100:1:3:immediate-sequence-binding","word-analysis:100:1:2:participial-oath-object"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Ayet özne ve yüklemiyle tam bir koşu olayı anlatıyor gibi okunabilir.","readingAfter_tr":"Ortaç ile hâl mastarı, ayrıntılı anlatıdan önce tek bir yemin görüntüsü kurar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması, ٱلْعَٰدِيَٰتِ başı ile ضَبْحًا hâlini birleştirerek tam anlatı yerine sıkıştırılmış bir yemin sahnesi kurar.","readerPayoff_tr":"Okur, ayetin niçin olay örgüsü vermeden yoğun bir hareket anı sunduğunu anlar.","sourceClaimRefs":["word-analysis:100:1:3:immediate-sequence-binding"],"evidenceRefs":["QI-33c7f4f2","QT-58f8251b","QT-e27b73c1"],"activationTriggers":[],"counterEvidence":[],"channelTags":["oath-sequence","compressed-scene"]},{"findingId":"100:1:embodied-exertion","disposition":"carry","kind":"local-resonance","relation":"supports-primary","supportLevel":"local-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Hızlı ileri hareketi sağlar.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["root_000993/B002","focus-trace:B01_KINETIC_BREATH"]},{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Koşunun uzatılmış beden geometrisini ve işitilir nefes maliyetini verir.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B002","evidenceRefs":["root_000901/B001","root_000901/B002","focus-trace:B01_KINETIC_BREATH"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşu yalnız hızlı yer değiştirme olarak görülür.","readingAfter_tr":"İleri uzanan beden ve zorlanan nefes, hızın mekanizmasını ve maliyetini görünür kılar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında hızlı ileri uzanış, ضَبْحًا ile işitilir bedensel efora dönüşür; hız artık yalnız sonuç değil, nefes harcayan bir süreçtir.","readerPayoff_tr":"Okur, hareketin gücünü onun bedende bıraktığı zorlanma üzerinden kavrar.","sourceClaimRefs":["focus-trace:B01_KINETIC_BREATH","channel-review:Propulsive Force and Incursion/A","reader-walk-wide:reading-1"],"evidenceRefs":["root_000993/B002","root_000901/B001","root_000901/B002"],"activationTriggers":[],"counterEvidence":[],"channelTags":["embodied-exertion","propulsive-force"]},{"findingId":"100:1:habitual-return","disposition":"carry","kind":"surprising-outlier","relation":"shifts-primary","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Bölünmüş kök eşlemesinin baskın olmayan ع و د hedefi dönüş, alışkanlık ve kalan güçle süren hizmet basıncı verir.","qacRefs":["100:1:1:3"],"rootId":"root_001058","branchId":"B004","evidenceRefs":["root_001058/B001","root_001058/B004","root_001058/B008","focus-trace:B03_HABITUATED_RETURN"]},{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Tekrarlanan hizmetin bedensel maliyetini işitilir kılar.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["root_000901/B001"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşu tek seferlik ileri hareket olarak okunur.","readingAfter_tr":"Baskın olmayan eşleme, hareketi alışılmış dönüşler içinde kalan gücü harcayan tekrarlı hizmet olarak da duyurur.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması korunurken, bölünmüş ع و د eşlemesi koşuyu alışkanlığa dönüşmüş tekrarlı hizmet, soluğu da bu hizmetin biriken maliyeti olarak açar.","readerPayoff_tr":"Okur, tek patlama gibi görünen hareketin eğitim, devamlılık ve tükenen güç boyutunu fark eder.","sourceClaimRefs":["focus-trace:B03_HABITUATED_RETURN"],"evidenceRefs":["root_001058/B001","root_001058/B004","root_001058/B008","root_000901/B001","coverage.root_lexicon:split-mapping"],"activationTriggers":[],"counterEvidence":["This reading depends on a non-dominant split-root target and must not be normalized into the surface sense."],"channelTags":["habituated-service","return"]},{"findingId":"100:1:prepared-succession","disposition":"carry","kind":"local-resonance","relation":"shifts-primary","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşan çoğul","function_tr":"Baskın olmayan ع د د eşlemesindeki sayma ve hazırlık ile baskın kökteki peş peşe takip, çoğulu hazırlıklı bir dizi olarak açar.","qacRefs":["100:1:1:3"],"rootId":"root_000989","branchId":"B002","evidenceRefs":["root_000989/B001","root_000989/B002","root_000993/B008","focus-trace:B04_PREPARED_SUCCESSION"]},{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Ayrı birimleri tek uzatılmış koşu düzeninde eşzamanlar.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B002","evidenceRefs":["root_000901/B002"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Çoğul, eşzamanlı ve ayrışmamış bir koşucu kalabalığıdır.","readingAfter_tr":"Sayılabilir, hazırlanmış birimler peş peşe ve koordineli biçimde ilerler.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması korunurken, bölünmüş ع د د eşlemesi çoğulu hazırlıklı ve sayılabilir birimlerin peş peşe yürüttüğü koordineli koşu olarak açar.","readerPayoff_tr":"Okur, kalabalığın yalnız çokluk değil düzen, hazırlık ve ardışıklık taşıyabileceğini görür.","sourceClaimRefs":["focus-trace:B04_PREPARED_SUCCESSION"],"evidenceRefs":["root_000989/B001","root_000989/B002","root_000993/B008","root_000901/B002","coverage.root_lexicon:split-mapping"],"activationTriggers":[],"counterEvidence":["This formal reading must not lexicalize عَٰدِيَٰتِ as 'the counted ones'."],"channelTags":["prepared-formation","successive-motion"]},{"findingId":"100:1:scorch-arc","disposition":"carry","kind":"local-resonance","relation":"shifts-primary","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Birincil nefes dalının yanında yakma/doğrultma, kararma ve kül dallarını yerel olarak taşır.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B003","evidenceRefs":["root_000901/B003","root_000901/B004","root_000901/B005","focus-trace:B05_MOTION_SCORCH"]},{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Isı etkisine gidebilecek kinetik girdiyi sağlar.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["root_000993/B002"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"ضَبْحًا koşunun sesli nefesini bildirir.","readingAfter_tr":"Nefes birincil kalırken sözcük, ısı teması, kararma ve küle uzanan örtük bir maddi yay taşır.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında nefes anlamı korunurken, ضَبْحًا'nın yakma, kararma ve kül dalları hareketi ısı değen ve iz bırakan maddi bir süreç olarak da baskılar.","readerPayoff_tr":"Okur, ilk ayetin nefesini sonraki ateş ve kalıntı görüntülerine hazırlanmış duyusal bir eşik olarak görür.","sourceClaimRefs":["word-analysis:100:1:3:heat-and-spark-pressure","focus-trace:B05_MOTION_SCORCH","cross-run-publication:finding-3","channel-review:Ignition, Light, and Combustion Trace/C"],"evidenceRefs":["QS-8a6bcd61","QS-e5bd85e7","QE-4d34399b","root_000993/B002","root_000901/B003","root_000901/B004","root_000901/B005"],"activationTriggers":[],"counterEvidence":["The focus alone does not supply the causal arrow from motion to scorching.","Breath remains the locally selected sense."],"channelTags":["ignition-trace","combustion-residue"]},{"findingId":"100:1:seasonal-hard-route","disposition":"carry","kind":"surprising-outlier","relation":"shifts-primary","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Sert ve engebeli yer, yaz bitkisi ve eski yol dalları hareketi mevsimlik bir güzergâha yerleştirir.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B010","evidenceRefs":["root_000993/B010","root_000993/B011","root_001058/B009","focus-trace:B06_SEASONAL_HARD_ROUTE"]},{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Zorlu zeminde yolculuğun bedensel yükünü duyurur.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["root_000901/B001"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşu yeri ve zamanı belirsiz kısa bir hamledir.","readingAfter_tr":"Uzak dallar hareketi eski, sert bir güzergâhta yaz şartları altında tekrarlanan yolculuk olarak açar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması korunurken, ٱلْعَٰدِيَٰتِ'in sert zemin, yaz bitkisi ve eski yol dalları soluğu mevsimlik ve zorlu bir yolculuğun maliyeti olarak duyurur.","readerPayoff_tr":"Okur, ani baskın görüntüsünün yanında çevreye ve sürekliliğe bağlı bir hareket alanının da mümkün olduğunu görür.","sourceClaimRefs":["focus-trace:B06_SEASONAL_HARD_ROUTE"],"evidenceRefs":["root_000993/B010","root_000993/B011","root_001058/B009","root_000901/B001"],"activationTriggers":[],"counterEvidence":["The reading is form-distant and exploratory.","The packet does not identify the runners as seasonal travelers."],"channelTags":["terrain-route","seasonal-travel"]},{"findingId":"100:1:ignition-chain","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Nefes anlamını korurken yakma dalı 100:2'deki gizli ateş ve vurma görüntüsüne yerel köprü kurar.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B003","evidenceRefs":["root_000901/B003","focus-trace:C01_STRIKE_IGNITION"]},{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Ateşlenmeye giden süreç için hızlı kinetik girdiyi sağlar.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["root_000993/B002"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"ضَبْحًا'daki yakma ihtimali tek başına uzak ve nedensizdir.","readingAfter_tr":"100:2'nin vurma ile gizli ateşi açığa çıkarması, hareketten tutuşmaya giden süreci etkinleştirir; nefes ile ısı birlikte kalır.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında nefes korunur; 100:2'deki vurma ve gizli ateş, ضَبْحًا'nın yakma dalını hareketten tutuşmaya uzanan bir süreç olarak etkinleştirir.","readerPayoff_tr":"Okur, ilk soluk ile ikinci ayetin kıvılcımını ayrı süsler değil, eforun maddi sonuçları olarak birlikte görür.","sourceClaimRefs":["focus-trace:C01_STRIKE_IGNITION","reader-walk-wide:reading-1","cross-run-publication:finding-1","channel-review:Ignition, Light, and Combustion Trace/A"],"evidenceRefs":["100:1:root_000993/B002","100:1:root_000901/B003","100:2:root_001642/B002","100:2:root_001203/B001","inter-ayah:100:2:strong"],"activationTriggers":[{"ayahRef":"100:2","wordSpan":"فَٱلْمُورِيَٰتِ قَدْحًا","effect_tr":"Gizli ateşin vurmayla çıkışını vererek yerel yakma dalını kinetik tutuşma sürecine çevirir.","evidenceRefs":["100:2:root_001642/B002","100:2:root_001203/B001","focus-trace:C01_STRIKE_IGNITION"]}],"counterEvidence":["The arrow from motion or repeated contact to ignition is an explicit reader inference, not a supplied causal statement."],"channelTags":["ignition-trace","kinetic-causation"]},{"findingId":"100:1:temporal-threshold","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Geçip başka bir duruma yönelme dalı, 100:3'teki değişim ve ilk ışıkla zaman eşiğine dönüşür.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B004","evidenceRefs":["root_000993/B004","focus-trace:C02_TEMPORAL_THRESHOLD"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşanlar mekânsal veya ahlaki bir sınırı aşar.","readingAfter_tr":"100:3'ün sabahı, aşımı bir zaman ve hâl değişimi eşiği yapar; düşmanca aşım yine mümkün kalır.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması korunurken, 100:3'teki sabah hareketi ٱلْعَٰدِيَٰتِ'in aşımını sahneyi bir zamansal hâlden ötekine taşıyan eşik geçişi olarak da açar.","readerPayoff_tr":"Okur, koşunun yalnız araziyi değil karanlıktan sabaha geçişi de gerçekleştirdiğini görür.","sourceClaimRefs":["focus-trace:C02_TEMPORAL_THRESHOLD","reader-walk-wide:reading-2"],"evidenceRefs":["100:1:root_000993/B004","100:3:root_001119/B003","100:3:root_000839/B001","inter-ayah:100:3:strong"],"activationTriggers":[{"ayahRef":"100:3","wordSpan":"فَٱلْمُغِيرَٰتِ صُبْحًا","effect_tr":"Aşımı değişim ve ilk ışıkla zaman eşiğine dönüştürür.","evidenceRefs":["100:3:root_001119/B003","100:3:root_000839/B001","focus-trace:C02_TEMPORAL_THRESHOLD"]}],"counterEvidence":["The hostile overrun reading remains available and is not exhausted by the temporal reading."],"channelTags":["temporal-threshold","dawn-motion"]},{"findingId":"100:1:residual-trail","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Hareket eden bedenin ilk, kısa ömürlü dış izi olarak çalışır.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["root_000901/B001","focus-trace:C03_RESIDUAL_TRAIL"]},{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Nefes ve toz izini üreten geçişi sağlar.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["root_000993/B002"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşan bedenler geçiş anında doğrudan görülür ve soluk hızın eşlikçisidir.","readingAfter_tr":"100:4'teki yükselen toz ve kalıcı iz dalları, nefesi geçen bedenin ilk kalıntısı yapan bir iz zinciri kurar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında soluk, 100:4'te yükselen tozla birlikte, bedenler geçtikten sonra hareketi geriye doğru haber veren ilk kısa ömürlü iz olur.","readerPayoff_tr":"Okur, sahneyi yalnız hareket eden bedenlerden değil onların havada ve zeminde bıraktığı kanıttan okuyabilir.","sourceClaimRefs":["focus-trace:C03_RESIDUAL_TRAIL","channel-review:Propulsive Force and Incursion","channel-review:Ignition, Light, and Combustion Trace"],"evidenceRefs":["100:1:root_000993/B002","100:1:root_000901/B001","100:4:root_000210/B001","100:4:root_000011/B003","100:4:root_001544/B004","inter-ayah:100:4:strong"],"activationTriggers":[{"ayahRef":"100:4","wordSpan":"فَأَثَرْنَ بِهِۦ نَقْعًا","effect_tr":"Yükselme, yayılma, toz ve kalıcı iz dalları soluğu maddi bir iz zincirinin ilk halkası yapar.","evidenceRefs":["100:4:root_000210/B001","100:4:root_000011/B003","100:4:root_001544/B004","focus-trace:C03_RESIDUAL_TRAIL"]}],"counterEvidence":["The packet supplies motion, spread, dust and mark; their unification as one evidentiary trail is an inference."],"channelTags":["residual-trail","embodied-evidence"]},{"findingId":"100:1:coordinated-penetration","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşan çoğul","function_tr":"Hazırlık ve peş peşe takip dalları, çoğulu düzenli bir formasyon olarak açar.","qacRefs":["100:1:1:3"],"rootId":"root_000989","branchId":"B002","evidenceRefs":["root_000989/B002","root_000993/B008","focus-trace:C04_COORDINATED_PENETRATION"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Hazırlanmış birimler peş peşe koşar.","readingAfter_tr":"100:5, bu ardışıklığa hedef ve geometri verir: ayrı birimler güçlerini toplayıp bir topluluğun ortasına girer.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasındaki çoğul, 100:5'te parçalarını tek kuvvette toplayarak bir topluluğun ortasına giren zamanlanmış formasyon hâline gelir.","readerPayoff_tr":"Okur, koşunun rastgele hız değil hedefe yönelmiş düzen ve yoğunlaşma taşıdığını görür.","sourceClaimRefs":["focus-trace:C04_COORDINATED_PENETRATION","channel-review:Propulsive Force and Incursion/A"],"evidenceRefs":["100:1:root_000989/B002","100:1:root_000993/B008","100:5:root_001646/B003","100:5:root_000259/B010","inter-ayah:100:5:strong"],"activationTriggers":[{"ayahRef":"100:5","wordSpan":"فَوَسَطْنَ بِهِۦ جَمْعًا","effect_tr":"Ardışık hareketi toplanmış bir gücün merkeze girişi olarak tamamlar.","evidenceRefs":["100:5:root_001646/B003","100:5:root_000259/B010","focus-trace:C04_COORDINATED_PENETRATION"]}],"counterEvidence":[],"channelTags":["prepared-formation","center-penetration"]},{"findingId":"100:1:service-ingratitude","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Baskın olmayan dönüş, alışkanlık ve geri dönen yarar dalları, koşuyu eğitimli hizmet olarak açar.","qacRefs":["100:1:1:3"],"rootId":"root_001058","branchId":"B004","evidenceRefs":["root_001058/B004","root_001058/B006","focus-trace:C05_SERVICE_INGRATITUDE"]},{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Hizmetin görünür ve işitilir harcamasını verir.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["root_000901/B001"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşanlar belirsiz bir görevde kendilerini harcar.","readingAfter_tr":"100:6'nın yetiştirme, bağ kesme ve nimeti inkâr kutbu, eğitimli harcamayı insan nankörlüğüne karşıt bir hizmet görüntüsü yapar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasındaki işitilir harcama, 100:6 gelince alışılmış ve yarar taşıyan hizmetin, bağını kesip nimeti inkâr eden insana karşıt görüntüsü olarak da okunur.","readerPayoff_tr":"Okur, açılıştaki güçlü bedenlerin insanın ilişkisel kusurunu yalnız sözle değil karşıt bir eylemle görünür kıldığını fark eder.","sourceClaimRefs":["focus-trace:C05_SERVICE_INGRATITUDE","channel-review:Covenant, Opposition, and Settlement/B"],"evidenceRefs":["100:1:root_001058/B004","100:1:root_001058/B006","100:1:root_000901/B001","100:6:root_000059/B001","100:6:root_000532/B002","100:6:root_001321/B001","100:6:root_001321/B002"],"activationTriggers":[{"ayahRef":"100:6","wordSpan":"إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌ","effect_tr":"Alışılmış yarar ve harcamayı yetiştirme bağını kesen nankörlükle karşılaştırır.","evidenceRefs":["100:6:root_000532/B002","100:6:root_001321/B001","100:6:root_001321/B002","focus-trace:C05_SERVICE_INGRATITUDE"]}],"counterEvidence":["inter-ayah:100:6 is labelled 'no value' for clarifying the opening image, while the focus-trace records a strong change.","The contrast between visible service and ingratitude is an inference; it does not identify the runners."],"channelTags":["habituated-service","ingratitude-contrast"]},{"findingId":"100:1:embodied-witness","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"İradeden bağımsız bedensel belirti olarak hareketin gerçekleştiğine tanıklık eder.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["root_000901/B001","focus-trace:C06_EMBODIED_WITNESS"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Soluk ve toz hızın duyusal yan etkileridir.","readingAfter_tr":"100:4'ün izi ve 100:7'nin şahitliği, beden ile zeminin olup biteni açığa vurduğu dağılmış bir tanıklık kurar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasında soluk, 100:4'ün izi ve 100:7'nin şahitliğiyle birlikte, bedenin ve zeminin hareketi istemsizce açığa vurduğu bir tanıklığa dönüşür.","readerPayoff_tr":"Okur, yemin edilen sahnenin kendi kanıtını nefes ve iz üzerinden ürettiğini görür.","sourceClaimRefs":["focus-trace:C06_EMBODIED_WITNESS","channel-review:Covenant, Opposition, and Settlement/C"],"evidenceRefs":["100:1:root_000901/B001","100:4:root_000011/B003","100:7:root_000822/B001","100:7:root_000822/B008"],"activationTriggers":[{"ayahRef":"100:4","wordSpan":"فَأَثَرْنَ بِهِۦ نَقْعًا","effect_tr":"Bedenin soluğunu zeminde ve havada kalan iz ile eşler.","evidenceRefs":["100:4:root_000011/B003"]},{"ayahRef":"100:7","wordSpan":"وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌ","effect_tr":"Hazır tanıklık ve tanıklık eden işaret dalları duyusal kalıntıları delil statüsüne yükseltir.","evidenceRefs":["100:7:root_000822/B001","100:7:root_000822/B008","focus-trace:C06_EMBODIED_WITNESS"]}],"counterEvidence":["inter-ayah:100:7 is labelled weak and says the later witness theme does not clarify the opening image.","The unification of breath, trace and testimony is a reader inference."],"channelTags":["embodied-witness","residual-trail"]},{"findingId":"100:1:desire-as-charge","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Dışarıdaki hızlı ve yönelmiş hareket, 100:8'deki iç bağlılığın beden diyagramına dönüşür.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["root_000993/B002","focus-trace:C07_DESIRE_AS_CHARGE"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Dıştaki koşucular belirsiz bir hedefe yönelir.","readingAfter_tr":"100:8'de sevgi kalpte bağlanır, iyi görülen şey hedef olur ve şiddet takibi hızlandırıp tutmaya kadar götürür.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasındaki dış koşu, 100:8 gelince kalpteki bağlılığın algılanan iyiliğe doğru insanı hızlandıran ve sıkılaştıran bedensel diyagramı olarak da okunur.","readerPayoff_tr":"Okur, dış hareket ile iç arzu arasındaki ortak itici kuvveti görür.","sourceClaimRefs":["focus-trace:C07_DESIRE_AS_CHARGE","reader-walk:reader_b:retrospective-surprise","butuncul-okuma:100:1"],"evidenceRefs":["100:1:root_000993/B002","100:8:root_000286/B002","100:8:root_000452/B001","100:8:root_000782/B001","100:8:root_000782/B003","100:8:root_000782/B006"],"activationTriggers":[{"ayahRef":"100:8","wordSpan":"وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ","effect_tr":"Bağlılık, hedeflenen iyi ve şiddeti dış koşunun içsel itki modeline bağlar.","evidenceRefs":["100:8:root_000286/B002","100:8:root_000452/B001","100:8:root_000782/B003","focus-trace:C07_DESIRE_AS_CHARGE"]}],"counterEvidence":["inter-ayah:100:8 is labelled weak and says the wealth theme does not clarify 100:1 directly.","The physical-to-moral analogy is inferred and does not turn the runners into the human."],"channelTags":["desire-dynamics","propulsive-force"]},{"findingId":"100:1:forward-return","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Baskın olmayan ع و د eşlemesindeki dönüş ve son durak dalları ileri hareketi daha büyük bir geri dönüş çevrimine bağlar.","qacRefs":["100:1:1:3"],"rootId":"root_001058","branchId":"B001","evidenceRefs":["root_001058/B001","root_001058/B002","focus-trace:C08_FORWARD_RETURN"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Açılıştaki koşu tek yönlü dışarı hareketidir.","readingAfter_tr":"100:9'un gizliyi tersyüz edip açığa çıkarması, ileri koşuyu son durağa dönen daha büyük bir çevrimin dışa gidiş evresi yapar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasındaki ileri koşu, 100:9'un gizliyi açığa çıkaran dönüşüyle birlikte, son durağa yönelen daha büyük bir geri dönüş çevriminin dışa gidiş evresi olarak da görünür.","readerPayoff_tr":"Okur, açılıştaki kuvvetli ileri yönün surenin sonunda dönüş ve açığa çıkışa büküldüğünü fark eder.","sourceClaimRefs":["focus-trace:C08_FORWARD_RETURN"],"evidenceRefs":["100:1:root_001058/B001","100:1:root_001058/B002","100:9:root_001040/B001","100:9:root_000130/B001","100:9:root_001195/B002"],"activationTriggers":[{"ayahRef":"100:9","wordSpan":"إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ","effect_tr":"Gizli ve aşağıda olanı açığa çıkararak doğrusal hareketi dönüş çevrimine büker.","evidenceRefs":["100:9:root_000130/B001","100:9:root_001195/B002","focus-trace:C08_FORWARD_RETURN"]}],"counterEvidence":["inter-ayah:100:9 is labelled weak and says accountability does not explain the opening image.","This reading depends on a non-dominant split-root target."],"channelTags":["return-disclosure","direction-reversal"]},{"findingId":"100:1:interior-exhales","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"İçerideki bedensel hâli dışarıdan işitilir kılar.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["root_000901/B001","focus-trace:C09_INTERIOR_EXHALES"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Nefes koşuya dışarıdan eşlik eden sestir.","readingAfter_tr":"100:10'un göğüs, kaynak ve örtüden çıkarılan öz dalları nefesi, hareketi üreten iç durumun istemsiz dışa açılması yapar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasındaki ضَبْحًا, 100:10 gelince koşuya eklenmiş bir ses değil, hareketi doğuran iç kaynağın istemsizce dışarı duyulması olarak açılır.","readerPayoff_tr":"Okur, ayetin bedeni dış görünüşten iç kaynağa doğru okuduğunu görür.","sourceClaimRefs":["focus-trace:C09_INTERIOR_EXHALES"],"evidenceRefs":["100:1:root_000901/B001","100:10:root_000330/B002","100:10:root_000849/B001","100:10:root_000849/B004"],"activationTriggers":[{"ayahRef":"100:10","wordSpan":"وَحُصِّلَ مَا فِى ٱلصُّدُورِ","effect_tr":"Göğsü kaynak ve içeriği açığa çıkarılan örtülü öz olarak verip nefesi içerinin dışa çıkışı yapar.","evidenceRefs":["100:10:root_000330/B002","100:10:root_000849/B001","100:10:root_000849/B004","focus-trace:C09_INTERIOR_EXHALES"]}],"counterEvidence":["inter-ayah:100:10 is labelled 'no value' and says disclosure does not clarify the opening action.","The inside-to-outside reclassification is an inference."],"channelTags":["breath-interiority","disclosure"]},{"findingId":"100:1:known-service","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Baskın olmayan alışkanlık ve geri dönen yarar dalları, görünen harcamayı bilinen bir hizmet ilişkisine açar.","qacRefs":["100:1:1:3"],"rootId":"root_001058","branchId":"B004","evidenceRefs":["root_001058/B004","root_001058/B006","focus-trace:C10_KNOWN_SERVICE"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Görünür hizmet ile insan nankörlüğü arasındaki karşıtlığı okur kurar.","readingAfter_tr":"100:11'in yetiştiren ve iç yüzü bilen kutbu, dış harcama ile gizli yönelişi birlikte değerlendirilmiş bir hizmet ilişkisine dönüştürür.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasındaki görünür harcama, 100:11 gelince kaynağı, yönelişi ve dönüşü bütünüyle bilinen bir hizmet ilişkisi içinde okunabilir.","readerPayoff_tr":"Okur, gösterişli hareketin yalnız görünüş değil iç yönelişi de bilinen bir eylem olduğunu fark eder.","sourceClaimRefs":["focus-trace:C10_KNOWN_SERVICE"],"evidenceRefs":["100:1:root_001058/B004","100:1:root_001058/B006","100:11:root_000532/B002","100:11:root_000387/B001"],"activationTriggers":[{"ayahRef":"100:11","wordSpan":"إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍ لَّخَبِيرٌ","effect_tr":"Yetiştirme ile iç yüzü bilme dallarını birleştirerek görünür harcamayı değerlendirilmiş ilişki yapar.","evidenceRefs":["100:11:root_000532/B002","100:11:root_000387/B001","focus-trace:C10_KNOWN_SERVICE"]}],"counterEvidence":["inter-ayah:100:11 is labelled 'no value' and says divine knowledge does not explain the opening action.","This reading depends on non-dominant local mappings and an inferred service relation."],"channelTags":["known-service","interior-knowledge"]},{"findingId":"100:1:causal-engine","disposition":"carry","kind":"ayah-function","relation":"supports-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ ضَبْحًا","surface_tr":"soluk soluğa koşanlar","function_tr":"Koşu itici hareketi, soluk ise bu hareketin ölçülebilir bedensel maliyetini verir.","qacRefs":["100:1:1:3","100:1:2:1"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["root_000993/B002","root_000901/B001","cross-run-publication:finding-1"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Ayet hızlı koşanların durağan bir görüntüsüdür.","readingAfter_tr":"100:2-5'te kıvılcım, sabah varışı, toz ve merkeze giriş sıralanınca ilk koşu bütün etkileri iten motor, soluk da maliyeti olur.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması, 100:2-5'in kıvılcım, sabah, toz ve merkeze giriş dizisinde sonraki etkileri üreten hareket motoru; duyulan soluk da bu üretimin bedensel maliyeti olur.","readerPayoff_tr":"Okur, ilk ayetin bir hız fotoğrafı değil sonraki zinciri çalıştıran neden olduğunu görür.","sourceClaimRefs":["cross-run-publication:finding-1","reader-walk-wide:reading-1","inter-ayah:100:2","inter-ayah:100:3","inter-ayah:100:4","inter-ayah:100:5"],"evidenceRefs":["root_000993/B002","root_000901/B001","inter-ayah:100:2:strong","inter-ayah:100:3:strong","inter-ayah:100:4:strong","inter-ayah:100:5:strong"],"activationTriggers":[{"ayahRef":"100:2","effect_tr":"Koşunun ilk maddi etkisini kıvılcım olarak verir.","evidenceRefs":["inter-ayah:100:2:strong","cross-run-publication:finding-1"]},{"ayahRef":"100:3","effect_tr":"Hareketin zamanlanmış varışını sabah baskını olarak verir.","evidenceRefs":["inter-ayah:100:3:strong","cross-run-publication:finding-1"]},{"ayahRef":"100:4","effect_tr":"Hareketin havadaki maddi izini toz olarak verir.","evidenceRefs":["inter-ayah:100:4:strong","cross-run-publication:finding-1"]},{"ayahRef":"100:5","effect_tr":"Hareket zincirini merkeze girişle sonuçlandırır.","evidenceRefs":["inter-ayah:100:5:strong","cross-run-publication:finding-1"]}],"counterEvidence":["The ordered effects are supplied, but the claim that exertive motion causally enables every effect is an inference."],"channelTags":["causal-sequence","propulsive-force"]},{"findingId":"100:1:contagious-desire","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"synthetic","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Bulaşma dalı, dış koşunun sürükleyici kalıbını 100:8'deki iç bağlılığa aktarır.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B006","evidenceRefs":["root_000993/B006","reader-walk:reader_b:reading-2","cross-run-publication:finding-4"]},{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Sürüklenmenin tekrarlanan bedensel belirtisini verir.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["root_000901/B001"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Dış koşu ile insanın iç bağlılığı benzer yoğunlukta iki ayrı sahnedir.","readingAfter_tr":"Bulaşma dalı, yönelmiş sürüklenmenin dış koşudan iç iştaha geçen bir kalıp gibi okunmasını sağlar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması korunurken, ٱلْعَٰدِيَٰتِ'in bulaşma dalı 100:8'deki şiddetli bağlılığı dış koşunun insan içine geçen sürükleyici kalıbı olarak açar.","readerPayoff_tr":"Okur, arzunun yalnız duygu değil bedeni harekete geçiren ve kendini yeniden üreten bir yönelim olduğunu görür.","sourceClaimRefs":["reader-walk:reader_b:reading-2","cross-run-publication:finding-4","butuncul-okuma:100:1","channel-review:Bodily Interiors, Surfaces, and Health/D"],"evidenceRefs":["root_000993/B006","root_000901/B001","100:8:root_000286/B002","100:8:root_000782/B003"],"activationTriggers":[{"ayahRef":"100:8","wordSpan":"لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ","effect_tr":"Bağlılık ve yoğunluk, dıştaki yönelmiş hareketi iç iştahın bulaşıcı sürüklenmesine çevirir.","evidenceRefs":["reader-walk:reader_b:reading-2","cross-run-publication:finding-4"]}],"counterEvidence":["This is an explicit analogy, not a claim that عَٰدِيَٰتِ lexically means inner appetite.","inter-ayah:100:8 gives only weak marginal contribution."],"channelTags":["contagious-drive","desire-dynamics"]},{"findingId":"100:1:edge-to-center","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Kenar, kıyı veya yan boyunca uzanma dalı harekete başlangıç geometrisi verir.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B009","evidenceRefs":["root_000993/B009","reader-walk:reader_b:reading-3","cross-run-publication:finding-5"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşu yönü belirtilmemiş genel bir ilerlemedir.","readingAfter_tr":"100:5'te merkeze giriş belirince koşu, kenar boyunca yaklaşarak toplanmış yapının ortasına ulaşan mekânsal manevraya dönüşür.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasındaki hareket, ٱلْعَٰدِيَٰتِ'in kenar dalı ve 100:5'in orta noktasıyla, kıyı boyunca ilerleyip toplanmış yapının merkezine giren bir manevra olarak da okunur.","readerPayoff_tr":"Okur, koşunun yalnız hızını değil kenardan merkeze uzanan rotasını görür.","sourceClaimRefs":["reader-walk:reader_b:reading-3","cross-run-publication:finding-5","butuncul-okuma:100:1","channel-review:Terrain, Orientation, and Staying/B"],"evidenceRefs":["root_000993/B009","100:5:root_001646/B003","inter-ayah:36:20:medium","inter-ayah:28:20:medium"],"activationTriggers":[{"ayahRef":"100:5","wordSpan":"فَوَسَطْنَ بِهِۦ جَمْعًا","effect_tr":"Kenar boyunca hareketi toplanmış bir yapının ortasına girişle tamamlar.","evidenceRefs":["100:5:root_001646/B003","reader-walk:reader_b:reading-3","cross-run-publication:finding-5"]}],"counterEvidence":["The packet does not explicitly narrate an edge-first tactical route; that geometry is inferred from branch and endpoint."],"channelTags":["edge-to-center","spatial-maneuver"]},{"findingId":"100:1:redress-run","disposition":"carry","kind":"surprising-outlier","relation":"shifts-primary","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Aynı baskın kökün yetkiliden yardım ve hakkın alınmasını isteme dalı, koşunun toplumsal yönünü saldırıdan onarıma çevirebilir.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B005","evidenceRefs":["root_000993/B005","focus-trace:O01_REDRESS_RUN"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Sınırı aşan koşucular saldırgan bir alanı ihlal eder.","readingAfter_tr":"Hakkını isteme dalı ile sonraki yarar, onarım ve yetiştirme görüntüleri koşuyu acil telafi arayışına da açar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması korunurken, ٱلْعَٰدِيَٰتِ'in hakkını yetkiliden isteme dalı koşuyu saldırı kadar telafi, onarım veya yarar arayan acil bir geçiş olarak da açar.","readerPayoff_tr":"Okur, aynı yönelmiş gücün zarar vermek kadar hakkı geri istemek için de kullanılabileceğini görür.","sourceClaimRefs":["focus-trace:O01_REDRESS_RUN","channel-review:Covenant, Opposition, and Settlement/C"],"evidenceRefs":["100:1:root_000993/B005","100:3:root_001119/B001","100:6:root_000532/B002","100:8:root_000452/B005"],"activationTriggers":[{"ayahRef":"100:3","wordSpan":"فَٱلْمُغِيرَٰتِ صُبْحًا","effect_tr":"Yarar, sulama ve onarım dalıyla hareketin amacını saldırıdan düzeltmeye açar.","evidenceRefs":["100:3:root_001119/B001"]},{"ayahRef":"100:6","wordSpan":"لِرَبِّهِۦ","effect_tr":"Yetiştirme ve onarım kutbunu sağlar.","evidenceRefs":["100:6:root_000532/B002"]},{"ayahRef":"100:8","wordSpan":"ٱلْخَيْرِ","effect_tr":"Cömertlik ve yararı sahiplenici ele geçirmeden ayırır.","evidenceRefs":["100:8:root_000452/B005","focus-trace:O01_REDRESS_RUN"]}],"counterEvidence":["The packet permits the reversal branch-wise but does not resolve the focus or 100:3 participle to a beneficent referent.","Aggressive and reparative social valences remain plural."],"channelTags":["redress","social-reversal"]},{"findingId":"100:1:transmitted-fire","disposition":"carry","kind":"surprising-outlier","relation":"shifts-primary","supportLevel":"synthetic","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Bulaşma dalı, bir hâlin taşıyıcıdan başkasına geçiş topolojisini verir.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B006","evidenceRefs":["root_000993/B006","focus-trace:O02_TRANSMITTED_FIRE"]},{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Ateşin dokunduğu ve yaktığı madde köprüsünü sağlar.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B003","evidenceRefs":["root_000901/B003"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşanlar hareketleriyle kıvılcım üretir.","readingAfter_tr":"Bulaşma ve ateş teması birlikte, gizli etkinliği temas sınırından çevreye taşıyan hareketli aracılar görüntüsü kurar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması korunurken, bulaşma ve ateş teması dalları 100:2'de koşanları temas ettiği yere gizli etkinliği geçirip tutuşturan hareketli taşıyıcılar olarak da düşündürür.","readerPayoff_tr":"Okur, ateşlenmeyi yalnız üretim değil bir durumun temastan temasa geçişi olarak görür.","sourceClaimRefs":["focus-trace:O02_TRANSMITTED_FIRE"],"evidenceRefs":["100:1:root_000993/B006","100:1:root_000901/B003","100:2:root_001642/B002","100:2:root_001203/B001"],"activationTriggers":[{"ayahRef":"100:2","wordSpan":"فَٱلْمُورِيَٰتِ قَدْحًا","effect_tr":"Gizli ateş ve vurma, taşınan etkinliğin temasla dışarı geçmesini sağlar.","evidenceRefs":["100:2:root_001642/B002","100:2:root_001203/B001","focus-trace:O02_TRANSMITTED_FIRE"]}],"counterEvidence":["This is a cross-domain mechanism, not a claim that fire is disease.","It does not lexicalize عَٰدِيَٰتِ as contagion in the local syntax."],"channelTags":["transmission","ignition-trace"]},{"findingId":"100:1:watering-route","disposition":"carry","kind":"surprising-outlier","relation":"shifts-primary","supportLevel":"synthetic","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşanlar","function_tr":"Sert yer, yaz bitkisi ve eski yol dalları kuraklık içinde yinelenen güzergâhı kurar.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B010","evidenceRefs":["root_000993/B010","root_000993/B011","root_001058/B009","focus-trace:O03_WATERING_ROUTE"]},{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Kurak çevrimdeki yolculuk stresini bedende duyurur.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["root_000901/B001"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Sahne toz içindeki kısa ve şiddetli bir koşudur.","readingAfter_tr":"100:4, 100:6, 100:10 ve 100:11'in su, çoraklık, su başından ayrılma ve toprağı işleme dalları hareketi suya gidip dönen mevsimlik çevrime dönüştürür.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması korunurken, sert zemin ve yaz bitkisiyle açılan yol, sonraki su, çoraklık ve su başından ayrılma dallarıyla susuzluğu gideren kaynağa gidip dönen mevsimlik bir çevrim olarak da okunur.","readerPayoff_tr":"Okur, saldırı ağırlıklı sahnenin yanında hareketi kurak çevre ve su ihtiyacının örgütlediği ekolojik bir alan görür.","sourceClaimRefs":["focus-trace:O03_WATERING_ROUTE","channel-review:Terrain, Orientation, and Staying/A","channel-review:Cultivation, Harvest, and Prepared Nourishment/A"],"evidenceRefs":["100:1:root_000993/B010","100:1:root_000993/B011","100:1:root_001058/B009","100:1:root_000901/B001","100:4:root_001544/B002","100:6:root_001321/B003","100:10:root_000849/B003","100:11:root_000387/B003"],"activationTriggers":[{"ayahRef":"100:4","wordSpan":"نَقْعًا","effect_tr":"Susuzluğu gideren su dalıyla güzergâha ekolojik çekim merkezi verir.","evidenceRefs":["100:4:root_001544/B002"]},{"ayahRef":"100:6","wordSpan":"كَنُودٌ","effect_tr":"Bitmeyen toprağı hareketi zorlayan kıtlık kutbu yapar.","evidenceRefs":["100:6:root_001321/B003"]},{"ayahRef":"100:10","wordSpan":"ٱلصُّدُورِ","effect_tr":"Su başından ayrılma dalıyla gidiş-dönüş çevrimini kapatır.","evidenceRefs":["100:10:root_000849/B003"]},{"ayahRef":"100:11","wordSpan":"خَبِيرٌ","effect_tr":"Toprağı işleme dalıyla çoraklığın karşısına üretken bakım koyar.","evidenceRefs":["100:11:root_000387/B003","focus-trace:O03_WATERING_ROUTE"]}],"counterEvidence":["This reading is deliberately branch-distant and must not replace the stronger kinetic, ignition or penetration readings.","The packet does not identify a literal watering journey."],"channelTags":["watering-route","seasonal-travel","terrain-route"]},{"findingId":"100:1:useless-spark","disposition":"carry","kind":"surprising-outlier","relation":"shifts-primary","supportLevel":"synthetic","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Yakma ve kül dalları, yoğun enerji harcamasını sonucuyla değerlendirmeye açar.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B003","evidenceRefs":["root_000901/B003","root_000901/B005","focus-trace:O04_USELESS_SPARK"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Kıvılcım ve yanma güç gösterisidir.","readingAfter_tr":"100:8'in yararsız kıvılcımı, yararlı iyi ve 100:10'un ayrışma kalıntısı, yoğun harcamanın kül veya tortu üretip üretmediğini sorgulatır.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasındaki yoğun harcama, 100:8 ve 100:10'un yarar ile kalıntı baskısı altında, parlak kıvılcımı sonunda yalnız kül veya tortu bırakabilecek bir güç gösterisi olarak da uyarır.","readerPayoff_tr":"Okur, hareketin etkileyiciliğini otomatik olarak yararla eşitlememeyi öğrenir.","sourceClaimRefs":["focus-trace:O04_USELESS_SPARK"],"evidenceRefs":["100:1:root_000901/B003","100:1:root_000901/B005","100:8:root_000286/B011","100:8:root_000452/B001","100:10:root_000330/B003"],"activationTriggers":[{"ayahRef":"100:8","wordSpan":"حُبِّ ٱلْخَيْرِ","effect_tr":"Yarar sağlamayan kıvılcım ile gerçekten yararlı iyi arasında ölçüt kurar.","evidenceRefs":["100:8:root_000286/B011","100:8:root_000452/B001"]},{"ayahRef":"100:10","wordSpan":"وَحُصِّلَ","effect_tr":"Yoğun süreçten sonra kalan tortuyu görünür kılar.","evidenceRefs":["100:10:root_000330/B003","focus-trace:O04_USELESS_SPARK"]}],"counterEvidence":["The packet does not resolve whether this utility judgment evaluates the opening agents or only activates a later analogy."],"channelTags":["utility-test","combustion-residue"]},{"findingId":"100:1:counted-pulses","disposition":"carry","kind":"surprising-outlier","relation":"shifts-primary","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"koşan çoğul","function_tr":"Baskın olmayan ع د د eşlemesindeki sayma ve aralıklı tekrar ile baskın kökteki ardışık takip, çoğulu ritmik birimlere ayırır.","qacRefs":["100:1:1:3"],"rootId":"root_000989","branchId":"B001","evidenceRefs":["root_000989/B001","root_000989/B005","root_000993/B008","focus-trace:O05_COUNTED_PULSES"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Koşanlar aynı anda hareket eden bir kütledir.","readingAfter_tr":"Adımlar, soluklar veya koşucular sayılabilir ritmik darbeler olur; 100:5 ve 100:10 bunları toplayıp sonucu açığa çıkarır.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okuması korunurken, bölünmüş ع د د eşlemesi koşuyu sayılabilir adım ve soluk darbelerine ayırır; 100:5 ile 100:10 bu dağınık harcamaları toplanmış bir sonuca bağlar.","readerPayoff_tr":"Okur, çoğulu yalnız kalabalık değil biriken ve sonunda hesabı çıkan ritmik harcama olarak görür.","sourceClaimRefs":["focus-trace:O05_COUNTED_PULSES"],"evidenceRefs":["100:1:root_000989/B001","100:1:root_000989/B005","100:1:root_000993/B008","100:5:root_000259/B001","100:10:root_000330/B001"],"activationTriggers":[{"ayahRef":"100:5","wordSpan":"جَمْعًا","effect_tr":"Dağınık darbeleri toplanmış bütüne dönüştürür.","evidenceRefs":["100:5:root_000259/B001"]},{"ayahRef":"100:10","wordSpan":"حُصِّلَ","effect_tr":"Biriken dizinin ortaya çıkan toplamını verir.","evidenceRefs":["100:10:root_000330/B001","focus-trace:O05_COUNTED_PULSES"]}],"counterEvidence":["Do not lexicalize عَٰدِيَٰتِ as 'the counted ones'.","The reading uses a non-dominant split-root mapping as formal-temporal activation."],"channelTags":["counted-pulses","accumulation"]},{"findingId":"100:1:rising-breath","disposition":"carry","kind":"surprising-outlier","relation":"shifts-primary","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"soluk soluğa","function_tr":"Efor altındaki işitilir soluğu verir; 100:6'daki baskın olmayan ر ب و eşlemesinin yükselen ve şişen nefes imgesi bunu yeniden sınıflandırır.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["root_000901/B001","focus-trace:O06_RISING_BREATH_SPLIT"]}],"primaryReading_tr":"Soluk soluğa koşanlara andolsun.","readingBefore_tr":"Soluk hızın mekanik maliyetidir.","readingAfter_tr":"100:6'nın baskın olmayan yükselen nefes yankısı, soluğu güçlü hareketin bile yetiştirilen ve sürdürülen bir bedene bağımlı olduğunun kanıtı yapar.","proseClaim_tr":"“Soluk soluğa koşanlara andolsun” birincil okumasındaki ضَبْحًا, 100:6'nın baskın olmayan yükselen-nefes yankısıyla, güçlü hareketin bile sürdürülen bir bedene ve ilişkiye bağımlı olduğunu işittirir.","readerPayoff_tr":"Okur, görünürde özerk gücün her solukta taşıdığı bağımlılığı fark eder.","sourceClaimRefs":["focus-trace:O06_RISING_BREATH_SPLIT"],"evidenceRefs":["100:1:root_000901/B001","100:6:root_000537/B004","100:6:root_000532/B002","100:6:root_001321/B001"],"activationTriggers":[{"ayahRef":"100:6","wordSpan":"لِرَبِّهِۦ لَكَنُودٌ","effect_tr":"Yükselen nefes yankısını yetiştirme ve bağı kesme karşıtlığına yerleştirir.","evidenceRefs":["100:6:root_000537/B004","100:6:root_000532/B002","100:6:root_001321/B001","focus-trace:O06_RISING_BREATH_SPLIT"]}],"counterEvidence":["This must remain a split-map resonance.","It is not a claim that رَبِّ bears the ر ب و breath sense in ordinary syntax."],"channelTags":["rising-breath","embodied-dependence"]}],"coverageNote_tr":"Ledger, ayetin doğrudan yemin ve dilbilgisi tabanını, bütün word-analysis yükümlülüklerini, altı odak modeli, on bağlam değişimi, altı geçerli sıra dışı okumayı ve düzenli/geniş okur yürüyüşleri ile çapraz-koşu bulgularının ayrı getirilerini taşır. 122 inter-ayah satırı filtre olarak kullanılmadı; katkı sağlamayan 16 satır render edilmedi, ilgili zıt baskılar counterEvidence alanlarında korundu. Ayetteki iki kökün 35 dalı eksiksiz inlined lexicon içinde değerlendirildi; işlevsel geri dönüş yolu kurmayan özel ad, araç, diş, kap, bal ve benzeri dallardan yapay bulgu üretilmedi. Kanal incelemesi yalnız başka kanıtlarla yerel olarak kurulan bulgulara aday etiket sağladı. Baskın olmayan bölünmüş kök eşlemelerine dayanan okumalar remote-lexical veya synthetic olarak açıkça işaretlendi."}
```

---
