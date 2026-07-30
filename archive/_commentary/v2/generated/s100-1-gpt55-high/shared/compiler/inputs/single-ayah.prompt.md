# Instantiated Commentary v2 Prompt

- run: `s100-1-gpt55-high`
- stage: `pericope-compiler`
- unit: `single-ayah`
- surah: 100
- target language: `tr`
- generated: `2026-07-29`
- expected outputs:
  - `_commentary/v2/generated/s100-1-gpt55-high/shared/compiler/outputs/single-ayah.editorial-plan.json`
  - `_commentary/v2/generated/s100-1-gpt55-high/shared/compiler/outputs/single-ayah.channel-registry.json`
  - `_commentary/v2/generated/s100-1-gpt55-high/shared/compiler/outputs/single-ayah.friction.md`
- inlined sources:
  - `_commentary/v2/shared/compiler/PROMPT.md` - 2,328 bytes - `906b05312c4274b53e1c9c64308dc5d266ddbd82dab4ba6f4d4680c7c2441aa8`
  - `_commentary/v2/shared/EDITORIAL_CONTRACT.md` - 3,625 bytes - `530b89dae5b574671250452dd788e77de3f83d01e949b5538b68c70030efe2f4`
  - `_commentary/v2/shared/schemas/pericope-editorial-plan.schema.json` - 7,031 bytes - `59cdebfbdc70df4a5da606fd02b621ec35e31554854fca65676f0af61b40728e`
  - `_commentary/v2/shared/schemas/channel-registry.schema.json` - 3,619 bytes - `880b78b01960ccb151aa19dec6ea6575f11c81600fba56f237197adfe218c817`
  - `s100-1-gpt55-high/single-ayah.compiler-input.json` - 225 bytes - `02eb714e558a62fc161763ecca3c6a06b157e1a0082d06d89cd69d749cd26cdc`
  - `_commentary/v2/generated/s100-1-gpt55-high/layer_2/discovery/outputs/100_1.ledger.json` - 46,040 bytes - `4dbeb09b2dc3c4e63b88f061d48d7d196a666311137c5446c990d5c356baa00c`

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

## compiler-input: `s100-1-gpt55-high/single-ayah.compiler-input.json`

```json
{"schemaVersion":"commentary-v2-compiler-input-v1","surah":100,"pericopeId":"single-ayah","ayahRefs":["100:1"],"sourceLedgers":[{"ayahRef":"100:1","sha256":"413a137233cef872dcca92ad2ccf47565519c2d98c211aabde4828fa682c99bc"}]}
```

---

## discovery-ledger: `_commentary/v2/generated/s100-1-gpt55-high/layer_2/discovery/outputs/100_1.ledger.json`

```json
{"schemaVersion":"commentary-v2-layer2-discovery-v1","surah":100,"ayahRef":"100:1","language":"tr","primaryFloor_tr":"Ayet, koşu halinde nefes nefese kalan belirli bir çoğulluk üzerine yemin ederek açılır: وَ yemin edatıdır, ٱلْعَٰدِيَٰتِ yemin edilen hareket sınıfıdır, ضَبْحًا da bu hareketin halini veya tarzını işitilir soluk olarak verir.","sourceObligations":[{"sourceRef":"text:quran-uthmani.tsv:100:1","disposition":"carry","findingRefs":["100:1:oath-launch","100:1:action-class","100:1:breath-manner"]},{"sourceRef":"qac_morphemes:100:1","disposition":"carry","findingRefs":["100:1:oath-launch","100:1:action-class","100:1:breath-manner","100:1:sound-chain"]},{"sourceRef":"word_analysis:100:1:1","disposition":"carry","findingRefs":["100:1:oath-launch"]},{"sourceRef":"word_analysis:100:1:2","disposition":"carry","findingRefs":["100:1:action-class","100:1:boundary-pressure","100:1:sound-chain","100:1:variant-contrast"]},{"sourceRef":"word_analysis:100:1:3","disposition":"carry","findingRefs":["100:1:breath-manner","100:1:sound-chain","100:1:ignition-heat","100:1:variant-contrast"]},{"sourceRef":"word_morpheme_spans:100:1","disposition":"carry","findingRefs":["100:1:oath-launch","100:1:action-class","100:1:breath-manner"]},{"sourceRef":"v12_focus_trace_hermetic:reader_hft_a:baseline_models","disposition":"carry","findingRefs":["100:1:kinetic-breath","100:1:boundary-pressure","100:1:prepared-counted","100:1:seasonal-route","100:1:ignition-heat","100:1:service-return"]},{"sourceRef":"v12_focus_trace_hermetic:reader_hft_a:context_deltas","disposition":"carry","findingRefs":["100:1:ignition-heat","100:1:temporal-threshold","100:1:trail-witness","100:1:coordinated-penetration","100:1:service-return","100:1:desire-charge","100:1:forward-return","100:1:interior-exhale"]},{"sourceRef":"v12_focus_trace_hermetic:reader_hft_a:surprising_valid_outliers","disposition":"carry","findingRefs":["100:1:redress-run","100:1:transmitted-fire","100:1:seasonal-route","100:1:useless-spark","100:1:prepared-counted","100:1:rising-breath-split"]},{"sourceRef":"v12_reader_walks:reader_b:100:1","disposition":"carry","findingRefs":["100:1:boundary-pressure","100:1:desire-charge","100:1:coordinated-penetration"]},{"sourceRef":"v12_reader_walks_wide:reader_a:100:1","disposition":"carry","findingRefs":["100:1:kinetic-breath","100:1:boundary-pressure","100:1:ignition-heat"]},{"sourceRef":"v12_cross_run_publication:100:1","disposition":"carry","findingRefs":["100:1:kinetic-breath","100:1:boundary-pressure","100:1:ignition-heat","100:1:desire-charge","100:1:coordinated-penetration"]},{"sourceRef":"butuncul_okuma_line:100:1","disposition":"carry","findingRefs":["100:1:boundary-pressure","100:1:desire-charge","100:1:coordinated-penetration"]},{"sourceRef":"channel_subchannels_anchored_here:100:1","disposition":"carry","findingRefs":["100:1:kinetic-breath","100:1:boundary-pressure","100:1:ignition-heat","100:1:coordinated-penetration","100:1:seasonal-route","100:1:redress-run","100:1:trail-witness","100:1:interior-exhale"]},{"sourceRef":"inter_ayah_rows:100:1","disposition":"carry","findingRefs":["100:1:boundary-pressure","100:1:ignition-heat","100:1:trail-witness","100:1:coordinated-penetration","100:1:desire-charge","100:1:forward-return","100:1:interior-exhale"]},{"sourceRef":"coverage:word_analysis_qac_alignment","disposition":"carry","findingRefs":["100:1:identity-caution"]}],"findings":[{"findingId":"100:1:oath-launch","disposition":"carry","kind":"ayah-function","relation":"primary-floor","supportLevel":"direct","localAnchors":[{"surface_ar":"وَ","surface_tr":"wa","function_tr":"Yemin edatı olarak sonraki yemin nesnesini yönetir; başlangıcı basit bağlaç değil sıkıştırılmış kasem yapar.","qacRefs":["100:1:1:1"],"evidenceRefs":["qac:100:1:1:1","topic:100:1:1:oath-governance","topic:100:1:1:compressed-delayed-qasam"]},{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"Yemin edatının genitif tamamlayıcısı olarak yemin edilen hareket sınıfını taşır.","qacRefs":["100:1:1:2","100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["qac:100:1:1:2","qac:100:1:1:3","word_morpheme_spans:word_index=1"]}],"primaryReading_tr":"Ayet yeminle açılır ve cevap daha sonra gelecek bir yemin dizisinin ilk halkasını kurar.","proseClaim_tr":"Okur ayeti ilk anda 'nefes nefese koşanlara andolsun' diye tutar; وَ bu sahneyi devam cümlesi değil yemin delili yapar ve cevabı 100:6'ya kadar bekletir.","readerPayoff_tr":"Açılışın bir harfle kurduğu baskı anlaşılır: sahne daha ilk kelimede delile dönüşür ve okur devamı bekler.","sourceClaimRefs":["100:1:1:oath-governance","100:1:1:compressed-delayed-qasam"],"evidenceRefs":["QG-df4c11b9","QS-27d02d8b","QT-d847139e","MG-f182b034","QI-65124881","QT-923d29b2"],"activationTriggers":[],"counterEvidence":[],"channelTags":["oath-sequence","delayed-answer"]},{"findingId":"100:1:action-class","disposition":"carry","kind":"grammar","relation":"primary-floor","supportLevel":"direct","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"Belirli dişil çoğul aktif ism-i fail, tür adı değil eylemle tanınan bir çoğulluğu yemin nesnesi yapar.","qacRefs":["100:1:1:2","100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["qac:100:1:1:3","topic:100:1:2:participial-oath-object","topic:100:1:2:referent-underdetermination"]}],"primaryReading_tr":"Yemin edilen şey, adı verilmiş bir hayvan veya birlik değil, koşma/akma eylemiyle tanınan çoğulluktur.","proseClaim_tr":"ٱلْعَٰدِيَٰتِ okuru önce hareketle karşılaştırır: referent açık bırakılır, fakat genitif aktif participle o hareket sınıfını yemin nesnesi olarak sabitler.","readerPayoff_tr":"Okur at, deve, savaşçı gibi erken bir seçim yapmak zorunda kalmadan ayetin kuvvetini hareketten alır.","sourceClaimRefs":["100:1:2:participial-oath-object","100:1:2:referent-underdetermination"],"evidenceRefs":["QG-710929bb","QG-d893a8fb","QT-fdda5be9","QG-b5328a58","QS-437bf911","QF-6ec900e2","MS-1e2cc65d"],"activationTriggers":[],"counterEvidence":["coverage:word_analysis_qac_alignment:word-analysis critical_w=2 aligns upstream to 100:1:2 although QAC word 100:1:2 is ضَبْحًا; word_morpheme_spans supplies the usable morpheme join."],"channelTags":["action-class","referent-open"]},{"findingId":"100:1:boundary-pressure","disposition":"carry","kind":"local-resonance","relation":"supports-primary","supportLevel":"local-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"Yerel anlam koşuyu seçer; kök alanı ise düşmanlık, saldırı ve sınırı aşma basıncı bırakır.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B001","evidenceRefs":["topic:100:1:2:kinetic-adversarial-root-pressure","focus:B02_BOUNDARY_OVERRUN"]}],"primaryReading_tr":"Koşanlar hızla ilerler.","readingBefore_tr":"Hızlı koşu tarafsız bir hareket gibi okunabilir.","readingAfter_tr":"Aynı koşu, sınır aşan ve karşı tarafa yönelen bir baskı gibi duyulur; düşmanlık mümkün kalır ama referenti belirlemez.","proseClaim_tr":"ٱلْعَٰدِيَٰتِ koşuyu yerinden etmez; fakat ع د و alanının sınır aşma ve düşmanlık kenarı, bu koşuyu nötr hızdan çıkarıp baskılı bir geçiş olarak hissettirir.","readerPayoff_tr":"Ayetin ilk hamlesi yalnız hızlı değil, bir hududa yüklenen hareket olarak okunur.","sourceClaimRefs":["100:1:2:kinetic-adversarial-root-pressure","focus:B02_BOUNDARY_OVERRUN","reader_b:activated_reading:1","reader_a:activated_reading:2","cross_run_publication:finding:boundary-crossing"],"evidenceRefs":["QS-0f57d3dc","QS-81fc23e4","QI-7946c04e","focus:B02:root_000993/B001","focus:B02:root_000993/B003","focus:B02:root_000993/B004","inter_ayah:20:123","inter_ayah:68:12","inter_ayah:9:10","inter_ayah:2:194","inter_ayah:4:14","inter_ayah:7:55"],"activationTriggers":[{"ayahRef":"100:3","wordSpan":"مُغِيرَٰتِ صُبْحًا","effect_tr":"Sabah baskını ve değişim alanı, 100:1'deki sınır aşma basıncını zamansal ve saldırımsı geçiş olarak güçlendirir.","evidenceRefs":["focus:C02_TEMPORAL_THRESHOLD","reader_a:retrospective_surprises","butuncul_okuma_line:100:1"]},{"ayahRef":"100:5","wordSpan":"فَوَسَطْنَ بِهِۦ جَمْعًا","effect_tr":"Orta yere giriş, 100:1'de başlayan koşuyu kenardan merkeze ilerleyen mekansal manevra olarak geri okutur.","evidenceRefs":["focus:C04_COORDINATED_PENETRATION","reader_b:activated_reading:3","cross_run_publication:finding:spatial-maneuver"]}],"counterEvidence":["reader_a:retrospective_surprises:100:6 negative diagnosis belongs to the human, so ع د و B001 remains exploratory boundary overlay rather than settled moral identity of the runners.","focus:O01_REDRESS_RUN preserves reparative redress as a contrary social direction."],"channelTags":["boundary-crossing","hostility","incursion"]},{"findingId":"100:1:breath-manner","disposition":"carry","kind":"grammar","relation":"primary-floor","supportLevel":"direct","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"dabhan","function_tr":"Belirsiz mansub mastar, koşanların soluğunu ikinci bir olay değil hareketin hali/tarzı yapar.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["qac:100:1:2:1","topic:100:1:3:accusative-manner-state","topic:100:1:3:unbounded-breath"]}],"primaryReading_tr":"Koşu nefes sesiyle, zorlanmış soluk halinde verilir.","proseClaim_tr":"ضَبْحًا ayete yeni bir aktör eklemez; mansub belirsiz mastar olarak koşunun nasıl gerçekleştiğini, yayılan ve sayılmayan zorlanmış solukla gösterir.","readerPayoff_tr":"Okur hareketi dıştan görmez sadece; bedensel maliyetini de işitir.","sourceClaimRefs":["100:1:3:accusative-manner-state","100:1:3:unbounded-breath","100:1:3:hapax-local-load"],"evidenceRefs":["QG-9c95286b","QG-c3502dbd","QF-7ed8dfc3","QG-ef5d44ec","QS-74781736","QI-f0250a3f","QH-1a291f76"],"activationTriggers":[],"counterEvidence":[],"channelTags":["breath","manner-state"]},{"findingId":"100:1:sound-chain","disposition":"carry","kind":"sound-form","relation":"supports-primary","supportLevel":"local-inference","localAnchors":[{"surface_ar":"وَٱلْعَٰدِيَٰتِ","surface_tr":"wa-l-'adiyati","function_tr":"Yemin edatı ve participle sesçe bitişerek koşu imgesini tek çıkış darbesi gibi başlatır.","qacRefs":["100:1:1:1","100:1:1:2","100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["topic:100:1:1:fused-audible-launch","topic:100:1:2:cadence-and-breath-contrast"]},{"surface_ar":"ضَبْحًا","surface_tr":"dabhan","function_tr":"Ayet kapanışı, uzun participial akışı kısa ve sert bir soluk kelimesine indirir.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["topic:100:1:3:final-audible-landing"]}],"primaryReading_tr":"Ayetin sesi yeminli koşuyu başlatır ve solukta kapatır.","proseClaim_tr":"Ses örgüsü anlamı taşır: baştaki وَ koşu kelimesine yapışır, uzun ٱلْعَٰدِيَٰتِ uzar, sonra ضَبْحًا kapanışta ayeti kaba bir nefes gibi indirir.","readerPayoff_tr":"Okur hareketi yalnız anlamdan değil ayetin akışından da hisseder.","sourceClaimRefs":["100:1:1:fused-audible-launch","100:1:2:cadence-and-breath-contrast","100:1:3:final-audible-landing","100:1:2:participial-oath-chain"],"evidenceRefs":["QF-df7e6be6","QP-8e720064","QY-af82e14c","QF-81ef9b4f","QP-d4e9ce3a","QP-ea88af62","QT-fcb03a32","QP-583159a8","QP-9cfc543a","QE-71fde5eb","QY-5f92804b"],"activationTriggers":[{"ayahRef":"100:2","wordSpan":"فَٱلْمُورِيَٰتِ قَدْحًا","effect_tr":"Aynı participle-artı-mansub-olay modeli 100:2'de sürer; 100:1 ilk şablonu öğretir.","evidenceRefs":["topic:100:1:2:participial-oath-chain"]},{"ayahRef":"100:3","wordSpan":"فَٱلْمُغِيرَٰتِ صُبْحًا","effect_tr":"Üçüncü participle devamı, 100:1'in açtığı dizinin biçimsel zincir olduğunu teyit eder.","evidenceRefs":["topic:100:1:2:participial-oath-chain"]}],"counterEvidence":[],"channelTags":["sound-form","participle-chain"]},{"findingId":"100:1:variant-contrast","disposition":"carry","kind":"counterpressure","relation":"parallel-pressure","supportLevel":"direct","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"Standart kök koşu/sınır basıncını öne alır; bildirilen ٱلْغَادِيَٰتِ varyantı sabah gidişine kaydırır.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["topic:100:1:2:dawn-variant-contrast"]},{"surface_ar":"ضَبْحًا","surface_tr":"dabhan","function_tr":"Standart soluk kökü ayeti duyusal nefeste bırakır; bildirilen صُبْحًا varyantı slotu zaman ifadesi yapardı.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["topic:100:1:3:dawn-variant-contrast"]}],"primaryReading_tr":"Standart lafız, sabah zamanını hemen adlandırmak yerine koşu ve solukla başlar.","proseClaim_tr":"Varyantlar standardı değiştirmez; aksine standardın neyi koruduğunu gösterir: ilk kelimede sabah değil charge, son kelimede zaman değil nefes.","readerPayoff_tr":"Okur, sonraki sabah unsurunun gecikerek geldiğini ve ilk ayetin duyusal çarpışmaya öncelik verdiğini fark eder.","sourceClaimRefs":["100:1:2:dawn-variant-contrast","100:1:3:dawn-variant-contrast"],"evidenceRefs":["QF-599acfe7","QE-6bbcddaa","QF-efea91d0","QI-baf059b0","QE-383139f7"],"activationTriggers":[{"ayahRef":"100:3","wordSpan":"صُبْحًا","effect_tr":"100:3'te açık sabah gelince, 100:1'deki standart ضَبْحًا'nın sabahı erteleyip solukta kaldığı daha görünür olur.","evidenceRefs":["topic:100:1:3:dawn-variant-contrast"]}],"counterEvidence":["The variant readings are contrast evidence only; they do not replace the aligned standard surface for this ledger."],"channelTags":["variant-contrast","dawn-delay"]},{"findingId":"100:1:kinetic-breath","disposition":"carry","kind":"local-resonance","relation":"supports-primary","supportLevel":"direct","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"Koşu/hızlanma ana hareketi sağlar.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["focus:B01:root_000993/B002"]},{"surface_ar":"ضَبْحًا","surface_tr":"dabhan","function_tr":"Soluk sesi ve uzatılmış koşu geometrisi görünmeyen eforu akustik ve bedensel hale getirir.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["focus:B01:root_000901/B001","focus:B01:root_000901/B002"]}],"primaryReading_tr":"Hızlı koşu zorlanmış solukla duyulur.","readingBefore_tr":"Belirsiz bir çoğulluk yalnız hareketle tanınır.","readingAfter_tr":"Öne uzanan hızlı bedenlerin eforu zorlanmış soluk olarak işitilir.","proseClaim_tr":"ٱلْعَٰدِيَٰتِ ve ضَبْحًا birlikte okunduğunda ayet hızın soyut adını değil, öne uzayan bedenin çıkardığı soluklu maliyeti verir.","readerPayoff_tr":"Okur, opening image'in motorunu ve bedensel maliyetini tek sahne olarak kavrar.","sourceClaimRefs":["focus:B01_KINETIC_BREATH","cross_run_publication:finding:kinetic-chain","reader_a:activated_reading:1"],"evidenceRefs":["focus:B01:root_000993/B002","focus:B01:root_000901/B001","focus:B01:root_000901/B002","cross_run_publication:grade=strong:anchors=root_000993/B002,root_000901/B001"],"activationTriggers":[{"ayahRef":"100:2","wordSpan":"فَٱلْمُورِيَٰتِ قَدْحًا","effect_tr":"Kıvılcım halkası, 100:1'deki eforu daha geniş hareket-etki zincirinin motoru olarak okutur.","evidenceRefs":["reader_a:activated_reading:1","cross_run_publication:finding:kinetic-chain"]},{"ayahRef":"100:4","wordSpan":"فَأَثَرْنَ بِهِۦ نَقْعًا","effect_tr":"Toz halkası, solukla başlayan bedensel maliyeti görünür izlere taşır.","evidenceRefs":["cross_run_publication:finding:kinetic-chain"]}],"counterEvidence":[],"channelTags":["kinetic-chain","embodied-exertion"]},{"findingId":"100:1:ignition-heat","disposition":"carry","kind":"context-activation","relation":"supports-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"dabhan","function_tr":"Birincil soluk anlamı korunurken kökün yakma, kararma ve kül dalları sonraki kıvılcım halkasına doğru ısı basıncı verir.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B003","evidenceRefs":["topic:100:1:3:heat-and-spark-pressure","focus:C01_STRIKE_IGNITION","focus:B05_MOTION_SCORCH"]}],"primaryReading_tr":"Ayet nefes nefese koşuyu söyler.","readingBefore_tr":"ضَبْحًا önce koşu soluğudur; ısı dalları tek başına zayıf ve yerel kalır.","readingAfter_tr":"100:2'nin vurma ve gizli ateşi gelince soluk, hareketten kıvılcıma uzanan sıcak temas zincirinin ilk basıncı gibi okunur.","proseClaim_tr":"Soluk anlamı yerinde kalır; fakat ض ب ح alanındaki yakma, kararma ve kül, 100:2'deki قدح ve إيراء ile birleşince ayetin nefesi sıcak, sürtünmeli bir başlangıca dönüşür.","readerPayoff_tr":"Okur kıvılcımı sonradan eklenen bağımsız resim değil, ilk soluktaki efor ve ısıdan açılan süreç olarak görür.","sourceClaimRefs":["100:1:3:heat-and-spark-pressure","focus:B05_MOTION_SCORCH","focus:C01_STRIKE_IGNITION","reader_a:activated_reading:3","cross_run_publication:finding:heat-blackening-ash"],"evidenceRefs":["QS-8a6bcd61","QS-e5bd85e7","QE-4d34399b","focus:C01:root_000901/B003","focus:C01:100:2:root_001642/B002","focus:C01:100:2:root_001203/B001","focus:B05:root_000901/B003","focus:B05:root_000901/B004","focus:B05:root_000901/B005","inter_ayah:72:8"],"activationTriggers":[{"ayahRef":"100:2","wordSpan":"مُورِيَٰتِ قَدْحًا","effect_tr":"Gizli ateşin vurmayla çıkması, 100:1'deki scorch dalını süreç modeline çevirir.","evidenceRefs":["focus:C01_STRIKE_IGNITION","channel:Ignition, Light, and Combustion Trace/A"]}],"counterEvidence":["focus:C01 notes the arrow from rapid contact or exertion to ignition is reader inference; ayah-level breath remains primary.","focus:B05 marks the motion-to-scorch direction as provisional."],"channelTags":["ignition","heat","combustion-trace"]},{"findingId":"100:1:temporal-threshold","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"Geçip aşma dalı, 100:3'teki değişim ve sabahla faz eşiği okumasına açılır.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B004","evidenceRefs":["focus:C02_TEMPORAL_THRESHOLD"]}],"primaryReading_tr":"Koşu bir ilerleme ve geçiştir.","readingBefore_tr":"Geçiş mekansal veya saldırımsı sınır aşma gibi durur.","readingAfter_tr":"100:3'te sabah ve değişim gelince hareket, sahneyi bir halden başka hale, gece eşiğinden sabaha taşıyan faz geçişi olarak da okunur.","proseClaim_tr":"ٱلْعَٰدِيَٰتِ'teki aşma basıncı, 100:3'teki صُبْحًا ile zamana taşınır: koşu hala koşudur, ama artık bir sahneyi sabah eşiğine geçiren hareket gibi de görünür.","readerPayoff_tr":"Okur sınır aşımının yalnız mekan veya saldırı değil, görünür zaman değişimi de olabileceğini fark eder.","sourceClaimRefs":["focus:C02_TEMPORAL_THRESHOLD"],"evidenceRefs":["focus:C02:root_000993/B004","focus:C02:100:3:root_001119/B003","focus:C02:100:3:root_000839/B001"],"activationTriggers":[{"ayahRef":"100:3","wordSpan":"مُغِيرَٰتِ صُبْحًا","effect_tr":"Değişim ve sabah, 100:1'deki geçmeyi zamansal eşik okumasına revize eder.","evidenceRefs":["focus:C02_TEMPORAL_THRESHOLD"]}],"counterEvidence":["focus:C02 alternatives: dawn may only date the action; change branch may resonate without defining the construction."],"channelTags":["temporal-threshold","dawn"]},{"findingId":"100:1:trail-witness","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"dabhan","function_tr":"Soluk, geçip giden hareketin ilk kısa ömürlü izi olur.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["focus:C03_RESIDUAL_TRAIL","focus:C06_EMBODIED_WITNESS"]}],"primaryReading_tr":"Koşu soluk sesiyle algılanır.","readingBefore_tr":"Soluk ve toz hızın duyusal etkileri gibi durur.","readingAfter_tr":"100:4'te toz, 100:7'de şahitlik gelince soluk ve iz, geçişi haber veren dağıtılmış tanıklık haline gelir.","proseClaim_tr":"ضَبْحًا sadece dekoratif ses değildir; 100:4'teki yükselen toz ve 100:7'deki şahitlik diliyle birleşince bedenin ve zeminin olayı açığa vuran izleri arasına girer.","readerPayoff_tr":"Okur hareketi yalnız anlık seyretmez; soluk ve tozdan geriye doğru okunan bir kanıt sahası görür.","sourceClaimRefs":["focus:C03_RESIDUAL_TRAIL","focus:C06_EMBODIED_WITNESS"],"evidenceRefs":["focus:C03:root_000901/B001","focus:C03:100:4:root_000210/B001","focus:C03:100:4:root_000011/B003","focus:C03:100:4:root_001544/B004","focus:C06:100:7:root_000822/B001","focus:C06:100:7:root_000822/B008"],"activationTriggers":[{"ayahRef":"100:4","wordSpan":"أَثَرْنَ بِهِۦ نَقْعًا","effect_tr":"Toz ve iz dili, 100:1'deki soluğu ilk akustik kalıntı gibi yeniden çerçeveler.","evidenceRefs":["focus:C03_RESIDUAL_TRAIL"]},{"ayahRef":"100:7","wordSpan":"لَشَهِيدٌ","effect_tr":"Şahitlik dili, soluk ve izi yalnız belirti değil tanıklık işlevi taşıyan yüzeyler olarak okutur.","evidenceRefs":["focus:C06_EMBODIED_WITNESS"]}],"counterEvidence":["focus:C03 alternatives: breath and dust may be independent descriptive details; non-dominant trace mapping may be form-distant echo."],"channelTags":["trace","witness","residue"]},{"findingId":"100:1:coordinated-penetration","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"Çoğul koşu, hazırlanmış ve ardışık bir ilerleyiş olarak okunabilir.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B008","evidenceRefs":["focus:B04_PREPARED_SUCCESSION","focus:C04_COORDINATED_PENETRATION"]}],"primaryReading_tr":"Koşan çoğulluk ileri hareket eder.","readingBefore_tr":"Çoğulluk dağınık bir kalabalık veya eşzamanlı koşu gibi okunabilir.","readingAfter_tr":"100:5'te orta yere giriş ve جمع gelince bu çoğulluk, parçaları biriken ve merkeze giren hazırlanmış bir formasyon gibi okunur.","proseClaim_tr":"Ayetin çoğul koşusu, 100:5'teki وسط ve جمع ile geri dönünce gelişigüzel kalabalık değil; ardışık parçalarını yoğunlaştırıp bir merkeze sokan koordineli hamle olur.","readerPayoff_tr":"Okur açılış hareketinin hedef ve geometri kazandığını görür: kenardan merkeze giren bir düzen.","sourceClaimRefs":["focus:B04_PREPARED_SUCCESSION","focus:C04_COORDINATED_PENETRATION","reader_b:activated_reading:3","cross_run_publication:finding:spatial-maneuver"],"evidenceRefs":["focus:B04:root_000989/B001","focus:B04:root_000989/B002","focus:B04:root_000993/B008","focus:C04:100:5:root_001646/B003","focus:C04:100:5:root_000259/B010","butuncul_okuma_line:و س ط B003"],"activationTriggers":[{"ayahRef":"100:5","wordSpan":"وَسَطْنَ بِهِۦ جَمْعًا","effect_tr":"Orta ve toplanma kökleri, 100:1'deki çoğul koşuyu hedefli içeri giriş olarak güçlendirir.","evidenceRefs":["focus:C04_COORDINATED_PENETRATION","reader_b:activated_reading:3"]}],"counterEvidence":[],"channelTags":["formation","penetration","gathered-force"]},{"findingId":"100:1:service-return","disposition":"carry","kind":"context-activation","relation":"parallel-pressure","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"Split mapping ع د و -> ع و د, tekrar, alışkanlık, dönüş ve geri dönen fayda alanını açar.","qacRefs":["100:1:1:3"],"rootId":"root_001058","branchId":"B004","evidenceRefs":["focus:B03_HABITUATED_RETURN","focus:C05_SERVICE_INGRATITUDE","focus:C10_KNOWN_SERVICE"]}],"primaryReading_tr":"Koşanlar efor harcar.","readingBefore_tr":"Koşu tek bir atılım gibi okunur.","readingAfter_tr":"100:6 ve 100:11'de rab, insan ve nankörlük gelince, efor tekrar eden hizmet ve geri dönmesi gereken fayda karşıtlığı içinde görünür.","proseClaim_tr":"Bu okuma koşuyu bırakmaz; ٱلْعَٰدِيَٰتِ'in split dönüş/habit alanı, ضَبْحًا'nın duyurduğu bedeli tekrar eden hizmet gibi gösterir ve 100:6'daki koparma/nankörlükle karşılaştırır.","readerPayoff_tr":"Okur dıştaki eforla insanın ilişkiyi kesen nankörlüğü arasındaki gerilimi taşır.","sourceClaimRefs":["focus:B03_HABITUATED_RETURN","focus:C05_SERVICE_INGRATITUDE","focus:C10_KNOWN_SERVICE"],"evidenceRefs":["focus:B03:root_001058/B001","focus:B03:root_001058/B004","focus:B03:root_001058/B008","focus:C05:root_001058/B006","focus:C05:100:6:root_000532/B002","focus:C05:100:6:root_001321/B001","focus:C05:100:6:root_001321/B002","focus:C10:100:11:root_000387/B001"],"activationTriggers":[{"ayahRef":"100:6","wordSpan":"إِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌ","effect_tr":"İnsan, rab ve koparma/nankörlük alanı, 100:1'deki alışmış eforu hizmet-karşılık gerilimi olarak okutur.","evidenceRefs":["focus:C05_SERVICE_INGRATITUDE"]},{"ayahRef":"100:11","wordSpan":"رَبَّهُم بِهِمْ يَوْمَئِذٍ لَّخَبِيرٌۢ","effect_tr":"Kapanıştaki Rab ve iç bilgi, görünen efor ile gizli yönelişi bilinen bir hizmet ilişkisine bağlar.","evidenceRefs":["focus:C10_KNOWN_SERVICE"]}],"counterEvidence":["focus:C10 says this does not identify the runners; it changes expenditure from spectacle into known service relation.","focus summary marks return and service readings as dependent on non-dominant or branch-distant mappings."],"channelTags":["service","return","ingratitude"]},{"findingId":"100:1:desire-charge","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"Dış koşu, 100:8'deki şiddetli sevgiyle iç arzunun kinetik modeli haline gelir.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B002","evidenceRefs":["focus:C07_DESIRE_AS_CHARGE"]}],"primaryReading_tr":"Dışta hızlı, soluklu bir hareket vardır.","readingBefore_tr":"Açılış koşusu dış sahne olarak durur.","readingAfter_tr":"100:8'de sevgi, hayır ve şiddet gelince dış koşu, insanın iç bağlılığının hızlanan ve tutan hareket şeması gibi okunur.","proseClaim_tr":"100:1'in koşusu dış sahne olarak kalır; fakat 100:8'deki حُبّ ve شديد, bu hareketi iç iştahın bedende kurduğu charge gibi geri okutur.","readerPayoff_tr":"Okur surenin dış savaş enerjisinin insanın mala bağlı iç sürüklenmesiyle nasıl temas ettiğini görür.","sourceClaimRefs":["focus:C07_DESIRE_AS_CHARGE","reader_b:activated_reading:2","cross_run_publication:finding:contagious-drive","butuncul_okuma_line:100:1"],"evidenceRefs":["focus:C07:root_000993/B002","focus:C07:100:8:root_000286/B002","focus:C07:100:8:root_000452/B001","focus:C07:100:8:root_000782/B001","focus:C07:100:8:root_000782/B003","focus:C07:100:8:root_000782/B006","butuncul_okuma_line:ح ب ب B002","butuncul_okuma_line:ش د د B002"],"activationTriggers":[{"ayahRef":"100:8","wordSpan":"لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ","effect_tr":"Kalbe yapışan sevgi ve koşuya özgü şiddet, 100:1'deki dış kinetiği iç arzu diyagramına çevirir.","evidenceRefs":["focus:C07_DESIRE_AS_CHARGE","reader_b:retrospective_surprises"]}],"counterEvidence":["focus:C07 marks the link as analogy inferred by the reader, not a lexical replacement of the opening words."],"channelTags":["desire","inner-drive","attachment"]},{"findingId":"100:1:forward-return","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"Split ع و د alanı, ileri koşuyu dönüş ve varış ufkuna büker.","qacRefs":["100:1:1:3"],"rootId":"root_001058","branchId":"B001","evidenceRefs":["focus:C08_FORWARD_RETURN"]}],"primaryReading_tr":"Açılış hareketi ileriye doğrudur.","readingBefore_tr":"Koşu tek yönlü dışarı atılım gibi görünür.","readingAfter_tr":"100:9'da gizli olanın çevrilip açığa çıkması gelince ileri hareket, dönüş ve açıklanmaya varan daha geniş bir döngünün outbound evresi gibi okunur.","proseClaim_tr":"İleri koşu yerinde kalır; fakat ع و د split alanı ve 100:9'un gizliyi açığa çıkaran dönüşü, bu ileri hamleyi sonunda varışa ve ifşaya bükülen hareket olarak da taşır.","readerPayoff_tr":"Okur açılışın sadece kaçan veya saldıran çizgi değil, gizlinin ortaya dönüşüne bağlanan bir yön taşıyabileceğini görür.","sourceClaimRefs":["focus:C08_FORWARD_RETURN"],"evidenceRefs":["focus:C08:root_001058/B001","focus:C08:root_001058/B002","focus:C08:100:9:root_001040/B001","focus:C08:100:9:root_000130/B001","focus:C08:100:9:root_001195/B002"],"activationTriggers":[{"ayahRef":"100:9","wordSpan":"بُعْثِرَ مَا فِى ٱلْقُبُورِ","effect_tr":"Gömülü olanın çevrilip açılması, 100:1'deki ileri hareketi dönüş ve ifşa döngüsüne katar.","evidenceRefs":["focus:C08_FORWARD_RETURN"]}],"counterEvidence":["focus:C08 depends on non-dominant return and destination branches; it should stay exploratory."],"channelTags":["return","disclosure"]},{"findingId":"100:1:interior-exhale","disposition":"carry","kind":"context-activation","relation":"shifts-primary","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"dabhan","function_tr":"Dışarı çıkan soluk, 100:10'da göğüs ve iç çekirdek diliyle içten dışa açılma olur.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["focus:C09_INTERIOR_EXHALES"]}],"primaryReading_tr":"Soluk koşuya eşlik eden dış ses gibi duyulur.","readingBefore_tr":"Nefes hızın dış belirtisidir.","readingAfter_tr":"100:10'da göğüsler ve iç çekirdeğin çıkarılması gelince nefes, hareketi doğuran iç kaynağın istemsiz dışa açılması gibi okunur.","proseClaim_tr":"ضَبْحًا yine koşu soluğudur; fakat 100:10'un صدور ve تحصيل dili onu iç basıncın beden sınırından geçerek dışarı duyulması olarak geri okutur.","readerPayoff_tr":"Okur sesin yüzey etkisi değil, iç kaynak ve dış hareket arasındaki açıklık olduğunu fark eder.","sourceClaimRefs":["focus:C09_INTERIOR_EXHALES"],"evidenceRefs":["focus:C09:root_000901/B001","focus:C09:100:10:root_000330/B002","focus:C09:100:10:root_000849/B001","focus:C09:100:10:root_000849/B004"],"activationTriggers":[{"ayahRef":"100:10","wordSpan":"وَحُصِّلَ مَا فِى ٱلصُّدُورِ","effect_tr":"Göğüs ve iç çekirdek dili, 100:1'deki soluğu içten dışa çıkan basınç olarak yeniden sınıflar.","evidenceRefs":["focus:C09_INTERIOR_EXHALES"]}],"counterEvidence":["focus:C09 says without chest/source branches breath still only signals fatigue."],"channelTags":["interior","breath","inside-outside"]},{"findingId":"100:1:prepared-counted","disposition":"carry","kind":"surprising-outlier","relation":"parallel-pressure","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"Non-dominant ع د د mapping, çoğulu sayılabilir darbeler veya hazırlanmış bir seri olarak duyurur.","qacRefs":["100:1:1:3"],"rootId":"root_000989","branchId":"B001","evidenceRefs":["focus:B04_PREPARED_SUCCESSION","focus:O05_COUNTED_PULSES"]}],"primaryReading_tr":"Çoğul koşu duyulur.","readingBefore_tr":"Koşanlar eşzamanlı bir kitle gibi görünür.","readingAfter_tr":"Sayım, hazırlık, zaman aralığı ve ardışık takip dallarıyla hareket, ritmik ve birike birike toplamı açıklanan bir seri gibi de okunur.","proseClaim_tr":"Bu okuma ٱلْعَٰدِيَٰتِ'i 'sayılanlar' diye çevirmemeli; ama split ع د د alanı çoğul koşunun bir dizi nefes, adım veya birim halinde toplamaya açık olduğunu gösterir.","readerPayoff_tr":"Okur kitle hareketini ritim, hazırlık ve sonradan açıklanan toplam olarak duyabilir.","sourceClaimRefs":["focus:B04_PREPARED_SUCCESSION","focus:O05_COUNTED_PULSES"],"evidenceRefs":["focus:B04:root_000989/B001","focus:B04:root_000989/B002","focus:B04:root_000993/B008","focus:O05:root_000989/B001","focus:O05:root_000989/B005","focus:O05:100:5:root_000259/B001","focus:O05:100:10:root_000330/B001"],"activationTriggers":[{"ayahRef":"100:5","wordSpan":"جَمْعًا","effect_tr":"Dağınık birimlerin toplanması, opening plural'i biriken darbeler olarak geri okutur.","evidenceRefs":["focus:O05_COUNTED_PULSES"]},{"ayahRef":"100:10","wordSpan":"حُصِّلَ","effect_tr":"Sonucun çıkarılması/toplamın görünmesi, sayılan darbeler okumasının dönüş yolunu tamamlar.","evidenceRefs":["focus:O05_COUNTED_PULSES"]}],"counterEvidence":["focus:O05 rendering caution: do not lexicalize عَٰدِيَٰتِ as 'the counted ones'."],"channelTags":["counting","preparedness","rhythm"]},{"findingId":"100:1:seasonal-route","disposition":"carry","kind":"surprising-outlier","relation":"parallel-pressure","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"Hard ground, summer herbage, and old-road branches turn motion into recurrent route through resistant terrain.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B010","evidenceRefs":["focus:B06_SEASONAL_HARD_ROUTE","focus:O03_WATERING_ROUTE"]},{"surface_ar":"ضَبْحًا","surface_tr":"dabhan","function_tr":"Soluk, kuru ve zorlu çevrede yolculuğun bedensel maliyetini kaydeder.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["focus:B06_SEASONAL_HARD_ROUTE","focus:O03_WATERING_ROUTE"]}],"primaryReading_tr":"Koşu soluklu bir hareket sahnesidir.","readingBefore_tr":"Sahne kısa ve şiddetli bir atılım gibi durur.","readingAfter_tr":"Düşük belirginlikli arazi, yaz otu, eski yol, su, verimsiz yer ve su başından dönüş dallarıyla hareket, kurak zeminde tekrar eden ekolojik rota olabilir.","proseClaim_tr":"Bu outlier baskın okumayı değiştirmez; fakat ٱلْعَٰدِيَٰتِ'in sert zemin ve yaz otu dalları, ضَبْحًا'nın soluğunu eski ve kuru bir yolda harcanan efor olarak geri taşıyabilir.","readerPayoff_tr":"Okur aynı koşunun savaş dışında çevre, mevsim ve kaynak arayışı basıncıyla da anlamlı bir rota kurabildiğini görür.","sourceClaimRefs":["focus:B06_SEASONAL_HARD_ROUTE","focus:O03_WATERING_ROUTE","channel:Terrain, Orientation, and Staying/A","channel:Cultivation, Harvest, and Prepared Nourishment/A"],"evidenceRefs":["focus:B06:root_000993/B010","focus:B06:root_000993/B011","focus:B06:root_001058/B009","focus:O03:root_000993/B010","focus:O03:root_000993/B011","focus:O03:100:4:root_001544/B002","focus:O03:100:6:root_001321/B003","focus:O03:100:10:root_000849/B003","focus:O03:100:11:root_000387/B003"],"activationTriggers":[{"ayahRef":"100:4","wordSpan":"نَقْعًا","effect_tr":"Su/susuzluk ve toz alanı rota okumasına çevresel çekim ve maliyet verir.","evidenceRefs":["focus:O03_WATERING_ROUTE"]},{"ayahRef":"100:10","wordSpan":"ٱلصُّدُورِ","effect_tr":"Su başından ayrılma dalı, rota döngüsünü gidiş-geliş olarak kapatır.","evidenceRefs":["focus:O03_WATERING_ROUTE"]}],"counterEvidence":["focus:O03 rendering caution: branch-distant ecological outlier; should not replace stronger kinetic, ignition, and penetration models."],"channelTags":["terrain","seasonal-route","ecology"]},{"findingId":"100:1:redress-run","disposition":"carry","kind":"surprising-outlier","relation":"parallel-pressure","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"ع د و B005, saldırı yönünü tersine çevirip haksızlığa karşı yardım veya giderim arayışını mümkün kılar.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B005","evidenceRefs":["focus:O01_REDRESS_RUN"]}],"primaryReading_tr":"Koşu sınır aşan acil hareket olarak duyulur.","readingBefore_tr":"Bu acil hareket saldırı veya overrun gibi görünür.","readingAfter_tr":"Redress dalı ve sonraki fayda/onarım dilleriyle aynı aciliyet, zarar vermek değil giderim aramak için mesafe aşma olarak da okunur.","proseClaim_tr":"ٱلْعَٰدِيَٰتِ'in sınır aşan koşusu korunur; outlier olarak, bu sınır aşma bir zalime karşı yardım veya onarım arayan acil geçiş de olabilir.","readerPayoff_tr":"Okur social valence'ın tek taraflı seçilmediğini görür: agresyon ve telafi yönleri aynı yerel kapıdan geçebilir.","sourceClaimRefs":["focus:O01_REDRESS_RUN","channel:Covenant, Opposition, and Settlement/C"],"evidenceRefs":["focus:O01:root_000993/B005","focus:O01:100:3:root_001119/B001","focus:O01:100:6:root_000532/B002","focus:O01:100:8:root_000452/B005"],"activationTriggers":[{"ayahRef":"100:6","wordSpan":"رَبِّهِۦ","effect_tr":"Onarma ve nurturing alanı, koşunun telafi arayışı olma ihtimaline sosyal hedef verir.","evidenceRefs":["focus:O01_REDRESS_RUN"]}],"counterEvidence":["focus:O01 rendering caution: packet does not resolve مُغِيرَٰتِ or focus participle to a beneficent referent.","Boundary/aggression readings remain live and are not displaced."],"channelTags":["redress","covenant","social-reversal"]},{"findingId":"100:1:transmitted-fire","disposition":"carry","kind":"surprising-outlier","relation":"parallel-pressure","supportLevel":"synthetic","localAnchors":[{"surface_ar":"ٱلْعَٰدِيَٰتِ","surface_tr":"al-'adiyati","function_tr":"ع د و B006 transmission branch gives the moving agents a contact-crossing topology.","qacRefs":["100:1:1:3"],"rootId":"root_000993","branchId":"B006","evidenceRefs":["focus:O02_TRANSMITTED_FIRE"]},{"surface_ar":"ضَبْحًا","surface_tr":"dabhan","function_tr":"Scorch branch makes the transferred state heat/contact rather than abstract influence.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B003","evidenceRefs":["focus:O02_TRANSMITTED_FIRE"]}],"primaryReading_tr":"Koşu ve soluk bedensel temaslı bir hareket sahnesidir.","readingBefore_tr":"Kıvılcım hareketle üretilen bir sonuç gibi okunur.","readingAfter_tr":"Transmission branch, gizli ateşin temasa geçtiği yere sıçraması gibi sentetik ama grounded bir mekanizma kurar.","proseClaim_tr":"Bu okuma ateşi hastalık yapmaz ve ٱلْعَٰدِيَٰتِ'i contagion diye çeviremez; yalnız hareketin taşıdığı durumun temas sınırını geçip 100:2'deki gizli ateşi açığa çıkarma modelini taşır.","readerPayoff_tr":"Okur ignition zincirinin yalnız sürtünme değil, bir halin taşıyıcıdan çevreye geçmesi olarak da düşünülebileceğini görür.","sourceClaimRefs":["focus:O02_TRANSMITTED_FIRE"],"evidenceRefs":["focus:O02:root_000993/B006","focus:O02:root_000901/B003","focus:O02:100:2:root_001642/B002","focus:O02:100:2:root_001203/B001"],"activationTriggers":[{"ayahRef":"100:2","wordSpan":"مُورِيَٰتِ قَدْحًا","effect_tr":"Latent fire and striking, transmission topology into contact-ignition mechanism.","evidenceRefs":["focus:O02_TRANSMITTED_FIRE"]}],"counterEvidence":["focus:O02 rendering caution: cross-domain mechanism, not literal disease or lexical replacement."],"channelTags":["transmission","ignition","outlier"]},{"findingId":"100:1:useless-spark","disposition":"carry","kind":"surprising-outlier","relation":"parallel-pressure","supportLevel":"contextual-inference","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"dabhan","function_tr":"Scorch and ash branches make intense expenditure assessable by what remains.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B005","evidenceRefs":["focus:O04_USELESS_SPARK"]}],"primaryReading_tr":"Soluklu koşu, güç ve enerji sahnesi kurar.","readingBefore_tr":"Sparks and scorching can look like unqualified power.","readingAfter_tr":"100:8 and 100:10 add useless spark, useful good, and residue/dross, so the opening expenditure can be judged by whether it yields benefit or only ash.","proseClaim_tr":"ضَبْحًا'nın ash/scorch arc, 100:8'de yararsız kıvılcım ve 100:10'da residue diliyle birleşince parlak harcamanın gerçekten hayır mı, yoksa kül mü bıraktığını sordurur.","readerPayoff_tr":"Okur gücün gösterisinden kalana geçer: intense motion may be impressive without being beneficial.","sourceClaimRefs":["focus:O04_USELESS_SPARK","channel:Ignition, Light, and Combustion Trace/C"],"evidenceRefs":["focus:O04:root_000901/B003","focus:O04:root_000901/B005","focus:O04:100:8:root_000286/B011","focus:O04:100:8:root_000452/B001","focus:O04:100:10:root_000330/B003"],"activationTriggers":[{"ayahRef":"100:8","wordSpan":"حُبِّ ٱلْخَيْرِ","effect_tr":"Useful good and useless spark contrast, bright expenditure's value question.","evidenceRefs":["focus:O04_USELESS_SPARK"]},{"ayahRef":"100:10","wordSpan":"حُصِّلَ","effect_tr":"Residue after separation asks what remains after fire and motion.","evidenceRefs":["focus:O04_USELESS_SPARK"]}],"counterEvidence":["focus:O04 says whether it evaluates the opening agents or only activates a later analogy remains unresolved."],"channelTags":["ash","utility","residue"]},{"findingId":"100:1:rising-breath-split","disposition":"carry","kind":"surprising-outlier","relation":"supports-primary","supportLevel":"remote-lexical","localAnchors":[{"surface_ar":"ضَبْحًا","surface_tr":"dabhan","function_tr":"Audible breath supplies the local phenomenon reclassified by a non-dominant ر ب و breath echo.","qacRefs":["100:1:2:1"],"rootId":"root_000901","branchId":"B001","evidenceRefs":["focus:O06_RISING_BREATH_SPLIT"]}],"primaryReading_tr":"Panting is mechanical cost of speed.","readingBefore_tr":"Soluk hızın bedensel gideridir.","readingAfter_tr":"100:6'daki non-dominant ر ب و rising/swelling breath echo makes the same panting evidence of a sustained dependent body and relation.","proseClaim_tr":"Bu split-map resonance رَبّ'i ordinary syntax içinde ر ب و diye çözmez; yalnız ضَبْحًا'daki yükselen soluğun, nurture ve separation diliyle bağımlı bedenin işareti gibi okunabileceğini taşır.","readerPayoff_tr":"Okur nefesin güç gösterisinden bağımlılık ve sürdürülen beden gerçeğine döndüğünü görür.","sourceClaimRefs":["focus:O06_RISING_BREATH_SPLIT"],"evidenceRefs":["focus:O06:root_000901/B001","focus:O06:100:6:root_000537/B004","focus:O06:100:6:root_000532/B002","focus:O06:100:6:root_001321/B001"],"activationTriggers":[{"ayahRef":"100:6","wordSpan":"لِرَبِّهِۦ لَكَنُودٌ","effect_tr":"Non-dominant rising-breath echo, dominant nurture and cutting branches with breath-dependence relation.","evidenceRefs":["focus:O06_RISING_BREATH_SPLIT"]}],"counterEvidence":["focus:O06 rendering caution: split-map resonance only; not an ordinary-syntax claim about رَبِّ."],"channelTags":["split-map","breath","dependence"]},{"findingId":"100:1:identity-caution","disposition":"carry","kind":"counterpressure","relation":"parallel-pressure","supportLevel":"direct","localAnchors":[{"surface_ar":"وَٱلْعَٰدِيَٰتِ ضَبْحًا","surface_tr":"wa-l-'adiyati dabhan","function_tr":"Word-analysis orthographic words and QAC words do not align one-to-one; use morpheme spans rather than silently renumbering.","qacRefs":["100:1:1:1","100:1:1:2","100:1:1:3","100:1:2:1"],"evidenceRefs":["coverage:word_analysis_qac_alignment","word_morpheme_spans:100:1"]}],"primaryReading_tr":"Ayet iki QAC word halinde ama üç orthographic/analysis unit halinde temsil edilir.","proseClaim_tr":"Kimlik uyarısı prose iddiası değil, downstream güvenliği içindir: aligned_qac_word_ref alanları aynen korunur, joins için word_morpheme_spans kullanılır.","readerPayoff_tr":"Kanıt yüzeyi yanlış kelime eşlemesiyle analiz üretmez; ضَبْحًا'nın dangling upstream word ref'i yerel morfem span ile korunur.","sourceClaimRefs":["coverage:word_analysis_qac_alignment","coverage:word_morpheme_spans"],"evidenceRefs":["coverage:word_analysis_qac_alignment:consistent=false","coverage:word_analysis_qac_alignment:dangling_refs=100:1:3","word_morpheme_spans:word_index=0","word_morpheme_spans:word_index=1","word_morpheme_spans:word_index=2"],"activationTriggers":[],"counterEvidence":["Upstream aligned_qac_word_ref is deliberately not corrected; renumbering would fabricate identities."],"channelTags":["identity","coverage"]}],"coverageNote_tr":"Ledger, inlined packetten çıkan primary floor, üç word-analysis unitinin bütün used/narrowed/candidate topic kümeleri, focus-trace baseline/context/outlier okumaları, reader-walk/cross-run/bütüncül okumada tekrar eden ana activations ve kanal/inter-ayah kanıtını carry olarak temsil eder. Prose-ready olmayan kimlik kusurları ve non-dominant/synthetic okumalar friction ve counterEvidence içinde korunmuştur; hiçbir finding blocked yapılmadı çünkü packet blocking evidence sağlamadı."}
```

---
