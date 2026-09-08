# Handoff: V5 Bridge Alignment And Missing Data

Date: 2026-09-08
Repo: `prose_generation`
Branch checked: `main`

## Question

Identify which recent V5-related change fixed the builder/preparation path so
previously missing word-analysis data is included, and verify whether the same
change explains the 29:38 hermetic bundle changes.

## Follow-up: Agent Input Compatibility

The user clarified that the concern is the size, shape, and behavior of the
generated agent prompts, with the established workflow to be preserved alongside
QAC and other small correctness fixes. The follow-up audit records an initial
compatibility prototype, the subsequently identified historical consolidation
baseline, and the selected experiment: restoring full historical project guidance
in separate current micro and macro discovery prompts while retaining current
evidence and QAC fixes.

The source-bundle size table below does not measure generated agent prompts.
The follow-up [input compatibility audit](AUDIT_V5_INPUT_COMPATIBILITY_2026-09-08.md)
reproduces 29:38 p03 global prompt growth from 1,368,058 to 2,076,949 bytes and
identifies earlier September 4 changes to context morphology, repeated records,
candidate routing, review obligations, and discovery instructions. These changes
are separate from the small September 5 bridge/alignment deltas. Keep the bridge
fix; do not interpret this handoff as approval to keep every earlier change to
the agent input contract. The roughly 170 KiB historical input was a consolidation
prompt; it is not directly comparable to a discovery prompt containing source
evidence. The guidance experiment has not yet been evaluated by authoring agents.

## Short Answer

The reliable commit is:

`1a8df9b3d0e7ac037ca752ff865fffa453952e2c`
`Use accepted QAC bridge links and preserve sparse word-analysis topics`

This commit matches both the code change and the data change for missing
word-analysis delivery. It should be kept with the QAC analysis bridge stack.

`928f4be8aacd6983858c4c87d147db5634f35819`
`Migrate V5 bundle spans and audit corpus preparation`

is still important, but it is the prior scaffolding/migration/audit expansion.
It is not the commit that restores the missing word-analysis topics.

## Contract Checked

The relevant V5 preparation contract is:

- Every `word_analysis.words[*].topics[*].topic_id` from the source bundle must
  be delivered as a word-analysis candidate in the prepared lane packet.
- Bridge-backed bundles must carry exact candidate `word_alignment`.
- Discovery prompt instructions require agents to use candidate `word_alignment`
  because analysis refs and QAC refs are separate identities.

Relevant current code locations:

- `_commentary/v5/workflow.py`: checks exact word-topic delivery when
  `coverage.word_morpheme_spans.alignment_version == "qac-analysis-bridge-v1"`.
- `_commentary/v5/workflow.py`: injects `word_alignment` into each
  word-analysis candidate.
- `_commentary/v5/prompts/discovery.md`: tells discovery agents to use
  candidate `word_alignment` and not collapse shared morphemes into duplicate
  semantics.

## Measured Before/After For Missing Topics

Pinned comparison:

- Before: parent of `1a8df9b3`, which is `928f4be8`
- After: `1a8df9b3`

Results:

| Case | Before `1a8df9b3` | After `1a8df9b3` |
| --- | ---: | ---: |
| `5:3` package | 83 / 102 word-analysis topics delivered, 19 missing | 102 / 102 delivered |
| `12:31` package | 60 / 106 delivered, 46 missing | 106 / 106 delivered |
| `24:31` package | 35 / 80 delivered, 45 missing | 80 / 80 delivered |

Total restored topics: 19 + 46 + 45 = 110.

This matches the `1a8df9b3` commit message: "Restore 110 source topics across
5:3, 12:31 and 24:31".

## 29:38 Hermetic Bundle Check

The 29:38 topic count was already complete before `1a8df9b3`:

| Bundle | Before | After |
| --- | --- | --- |
| `bundles/s029/29_38.ayah.json` | 49 / 49 topics delivered | 49 / 49 topics delivered |
| `bundles/s029-pericopes/p03_028-044/29_38.ayah.json` | 49 / 49 topics delivered | 49 / 49 topics delivered |
| `bundles/s029-pericopes/p02_036-069/29_38.ayah.json` | 49 / 49 topics delivered | 49 / 49 topics delivered |

The 29:38 gain from `1a8df9b3` is not missing topic count. It is bridge-backed
word/QAC resolution and candidate-level `word_alignment`.

Before `1a8df9b3`, all three 29:38 hermetic bundle variants had:

- `coverage.word_morpheme_spans.alignment_version`:
  `ordered-morpheme-spans-v2`
- `span_count`: 23
- `resolved_span_count`: 22
- one unresolved item:

```json
{
  "word_index": 13,
  "surface_ar": "هُمُ",
  "reason": "no compatible span in the best ordered source alignment"
}
```

After `1a8df9b3`, all three 29:38 variants had:

- `coverage.word_morpheme_spans.alignment_version`:
  `qac-analysis-bridge-v1`
- `span_count`: 23
- `resolved_span_count`: 23
- `candidate_word_alignment_count`: 49
- the previously unresolved item mapped as:

```json
{
  "word_index": 13,
  "analysis_ref": "29:38:14",
  "surface_ar": "هُمُ",
  "qac_refs": ["29:38:9:2"]
}
```

## 29:38 Bundle Size Check

The `1a8df9b3` size delta is small and does not explain any earlier large
170 KB to 900 KB prompt/bundle jump:

| Bundle | Before bytes | After bytes |
| --- | ---: | ---: |
| `bundles/s029/29_38.ayah.json` | 1,027,065 | 1,027,265 |
| `bundles/s029-pericopes/p03_028-044/29_38.ayah.json` | 1,027,085 | 1,027,285 |
| `bundles/s029-pericopes/p02_036-069/29_38.ayah.json` | 1,597,295 | 1,597,622 |

## Code Change That Corresponds To The Data

`1a8df9b3` introduced and connected these pieces:

- `_commentary/qac_analysis_bridge.py`
  - New release-owned many-to-many bridge from word-analysis units to QAC
    morphemes.
  - Verifies `quran-data` checksums, release metadata, QAC source, bridge
    schema, and all 114 word-analysis shards.
  - Preserves analysis identities separately from QAC identities.
  - Allows accepted overlaps where a whole expression and component share a
    canonical morpheme.
  - Keeps source exclusions as explicit unresolved entries with
    `excluded-source-defect`.

- `scripts/build_bundle.py`
  - Adds `build_word_qac_alignment()`.
  - Replaces ordered surface matching with bridge-backed alignment for normal
    ayah bundles and prefatory basmala bundles.

- `scripts/migrate_bundle_spans.py`
  - Regenerates saved bundle `word_morpheme_spans` and coverage from
    `build_word_qac_alignment()`.
  - Updates legacy notes so upstream `aligned_qac_word_ref` is preserved as a
    source observation, not treated as the QAC join.

- `_commentary/v5/workflow.py`
  - Validates bridge-backed bundles.
  - Fails preparation if delivered word-analysis candidate topics do not exactly
    equal the source bundle's word-analysis topics.
  - Adds per-candidate `word_alignment` to prepared lane packets.

- `_commentary/v5/prompts/discovery.md`
  - Updates the prompt contract to use `word_alignment`.
  - Clarifies that shared morphemes do not make semantic claims duplicates.

## Regression Test

The added regression suite is `scripts/test_qac_analysis_bridge.py`.

Important tests:

- `test_preparation_delivers_every_topic_and_the_exact_pronoun_link`
  - Confirms 29:38 prepares every word-analysis topic.
  - Confirms `29:38:14:pronoun-chain` carries:

```json
{
  "analysis_ref": "29:38:14",
  "qac_refs": ["29:38:9:2"],
  "status": "accepted"
}
```

- `test_sparse_analysis_ids_preserve_all_late_topics`
  - Confirms `5:3` package delivery has 102 expected topics and receives all
    102, including sparse late analysis ids up to `5:3:80`.

Verification run on 2026-09-08:

```text
python3 -m unittest scripts.test_qac_analysis_bridge
........
Ran 8 tests in 5.386s
OK
```

## Conclusion

Keep `1a8df9b3` and its related QAC analysis bridge machinery. The missing data
fix depends on the bridge, bundle migration, V5 exact topic-delivery validation,
candidate `word_alignment` injection, and prompt contract update together.

`928f4be8` should be understood as the preceding V5 package/audit expansion,
not the actual missing-topic restoration.
