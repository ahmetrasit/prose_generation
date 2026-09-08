# V5 agent input compatibility audit

Date: 2026-09-08

## Compatibility requirement

Preserve the established agent workflow, including evidence volume and shape,
lane ownership, discovery instructions, and downstream handoffs. Retain the QAC
alignment fixes and other small correctness fixes. A large change to the agent
input contract is not a minor bug fix merely because it preserves source data.

The user selected a production rollback to the compact early V5 input contract
at `41763703`, preserving QAC alignment and minor correctness fixes. The full
guidance experiment described below completed; it recovered some macro imagery
but did not consistently recover the earlier word-to-image explanations. Its
expanded data contract is not the selected production workflow.

## Implemented compact workflow

New preparation restores original candidate ownership and ordering, full source
supports and branches, lean context projections, compact JSON serialization,
and discovery v1. The four historical governing documents are frozen under
`_commentary/v5/guidance/` and embedded in discovery and consolidation. The
consolidator receives three scope drafts and guidance; the later discovery JSON
payload is no longer appended. Scope composition remains Turkish Markdown and
consolidation remains prose-only. Monitor lifecycle, paragraph-local tags,
editorial context references, and the prose validator are retained.

The later generated routing, obligation/review inventories, and bulk context
morphology registry are not inserted into new packets. Their underlying source
data, historical outputs, and packet utilities are preserved. The QAC bridge,
per-candidate alignment, sparse topic delivery checks, root-ID correction,
unresolved-branch preparation fixes, cache, and input validation remain.
Preparation identifies `agent_input_contract: early-v5-compact` and reports the
bulk registry as `context_morphology_status: not_requested`, not as complete.

Matched 29:38 p03 discovery preparations use the same analysis ID and context
`package=29:28-44`. The consolidation comparison reuses the exact same early
scope texts and focus/context brief; it is not a new authored commentary.

| Prompt | Early V5 bytes | Expanded bytes | Restored bytes | Restored KiB |
| --- | ---: | ---: | ---: | ---: |
| Micro discovery | 848,184 | 876,303 | 855,831 | 835.77 |
| Macro discovery | 994,284 | 1,043,776 | 996,901 | 973.54 |
| Global discovery | 1,368,119 | 2,076,949 | 1,370,609 | 1,338.49 |
| Consolidation, same historical scope texts | 168,935 | 346,236 | 170,875 | 166.87 |

The remaining consolidation overhead is 1,940 bytes (1.15%) for retained
prose-format and correctness instructions. The 29:38 packet comparison finds
exact equality with the early candidate order, support registries, branch
registries, connection registries, and selected context units in all three
lanes. Differences are confined to corrected candidate root IDs, QAC joins and
analysis namespaces, and the additive alignment fields. All 49 word topics
return to micro; total lane candidate counts return to 62 / 7 / 23.

Real package preparation also delivers all 102 / 106 / 80 source word topics
for 5:3 / 12:31 / 24:31, with exact candidate QAC links. Thus the 110 topics
restored by the bridge fix remain delivered. Regression tests cover those full
rendered packets, compact preparation, guidance snapshot identity, incomplete
topic detection, and the retained bridge/cache/prose-format behavior.

Verification: all 80 tests passed, including all nine QAC bridge regressions:

```text
python3 -B -m unittest _commentary.v5.tests.test_workflow _commentary.v5.tests.test_evidence_repairs _commentary.v5.tests.test_qac_cache _commentary.v5.tests.test_validate_prose scripts.test_qac_analysis_bridge
```

Fresh discovery inputs are saved under
`_commentary/v5/input/s029-p03-compact-20260908/s029/29_38/`. Their exact bytes
are 855,839 / 996,909 / 1,370,617; the eight-byte difference from the matched
comparison is the output analysis-ID length. The controlled consolidation
prompt and comparison details are under `/tmp/v5-compact-comparison/`.
No authoring agents have been run on this restored production contract yet.

The following sections preserve the investigation and rejected alternatives.

## Historical baseline and completed guidance experiment

The roughly 170 KiB historical inputs were consolidation prompts. The saved V5
29:38 p03 canonical prompt at `41763703` (September 3) is 168,935 bytes
(164.98 KiB); the preceding V4 example is 177,253 bytes (173.10 KiB).
Discovery prompts contain the source evidence and are substantially larger.

Using the same historical three scope prose files and discovery JSON files,
the pre-rollback consolidation template reconstructs to 346,236 bytes (338.12 KiB).
This is a controlled reconstruction, not a saved historical 338 KiB file.
Its main additions are 244,985 bytes of discovery JSON, while the four historical
project-guidance documents (69,650 bytes) were removed. Restoring those documents
would bring that consolidation example to roughly 406.14 KiB before wrappers.

For the selected experiment, the exact four guidance documents embedded in
the `41763703` canonical prompt are restored to current discovery prompts for
29:38 with context `package=29:28-44`. The sentence treating those documents as
design history is replaced with an explicit instruction to apply their semantic
guidance within the current discovery role and evidence boundary.

| Lane | Current prompt bytes | Full-guidance prompt bytes | Full-guidance KiB |
| --- | ---: | ---: | ---: |
| Micro | 876,323 | 946,409 | 924.23 |
| Macro | 1,043,796 | 1,113,882 | 1,087.78 |

Both add 70,086 bytes (68.44 KiB), including wrappers and the applicability note.
The files are under
`_commentary/v5/input/s029-p03-full-guidance-20260908/s029/29_38/`.
The accompanying preparation manifest records hashes and checks: current inline
evidence is byte-identical, historical guidance content is exact, and current
preparation and context-morphology guards passed. Production templates were not
changed by that experiment. This was the pre-run checkpoint. Both scope agents subsequently completed
discovery and prose; the final production decision is recorded above.

The reproduction and rejected prototype below remain as investigative history,
not the selected implementation.

## Scope correction to the bridge handoff

`HANDOFF_V5_BRIDGE_ALIGNMENT_2026-09-08.md` correctly identifies `1a8df9b3`
as the sparse word-topic restoration and exact analysis/QAC bridge fix.
However, its size table measures source `bundles/.../*.ayah.json` files.
That table does not measure generated agent prompts and does not resolve the
reported change to agent behavior or performance.

Earlier September 4 commits changed the generated evidence and instructions.
Those changes must be assessed separately from the September 5 bridge fix.

## Reproduction

Historical Python modules and discovery templates were loaded from Git into
isolated Python processes. The checkout was not switched. Each process prepared
29:38 using that revision's
`bundles/s029-pericopes/p03_028-044/29_38.ayah.json`, with the explicit composition
`package=29:28-44` and analysis ID `payload-history-audit`.

All runs used the same currently available Quran text, inter-ayah source, QAC
data, and context bundle directory. The focus source's top-level fields were
hash-compared between successive revisions. Only `coverage` and
`word_morpheme_spans` changed, at the two September 5 revisions. No focus source
fields changed between the four September 4 revisions.

The audit intercepted rendering and stopped after all three prompts were
captured, before production prompt/output writes. Temporary code, prompt JSON,
and summaries are under `/tmp/v5-payload-history-audit`; the audit driver is
`/tmp/v5_payload_history_audit.py`.

Example invocation:

```text
python3 -B /tmp/v5_payload_history_audit.py 7f1ac73c
python3 -B /tmp/v5_payload_history_audit.py 45332231
python3 -B /tmp/v5_payload_history_audit.py 6f73a182
python3 -B /tmp/v5_payload_history_audit.py 90b02449
python3 -B /tmp/v5_payload_history_audit.py 928f4be8
python3 -B /tmp/v5_payload_history_audit.py 1a8df9b3
```

## Measured agent prompt sizes

These are UTF-8 bytes for the complete generated discovery prompt, including
instructions and its inline lane packet.

| Revision | Main change | Micro | Macro | Global |
| --- | --- | ---: | ---: | ---: |
| `7f1ac73c` | Before routing/evidence repair | 848,123 | 994,350 | 1,368,058 |
| `45332231` | Routing, obligations, shorter policy | 863,631 | 997,654 | 1,434,682 |
| `6f73a182` | Context morphology and reference encoding | 804,039 | 899,771 | 1,732,963 |
| `90b02449` | Full repeated records; QAC cache | 870,149 | 1,040,956 | 2,073,935 |
| `928f4be8` | Span migration and alignment qualifications | 871,631 | 1,042,438 | 2,075,417 |
| `1a8df9b3` | Verified bridge and candidate alignment | 876,303 | 1,043,776 | 2,076,949 |

From the provisional baseline to the bridge revision, the global prompt grew
1.52x. Micro grew 1.03x and macro 1.05x. This reproduces substantial growth in
one lane; it does not establish a 3x increase across all prompts or identify a
170 KB historical baseline.

The bridge commit alone added 4,672 / 1,338 / 1,532 bytes to micro / macro /
global. The preceding span migration added 1,482 bytes per lane. These changes
are small in this example.

The existing saved `s029-p03` prompts remain packet schema v1 through all these
commits. Their bytes are 848,158 / 994,258 / 1,368,093. They were not regenerated
by the repair commits. Reading saved prompts alone therefore misses the change
in what a fresh preparation now generates.

## What changed beyond data addition

### `45332231`: different organization and instructions

The source bundle was unchanged, and all 92 candidates remained available across
the three lanes. Their ownership and review instructions changed:

- Fourteen candidates moved between lanes. Ten word-analysis topics moved from
  micro: four to macro and six to global. Four reader-walk items also moved.
- Word-topic distribution changed from `49 / 0 / 0` to `39 / 4 / 6` across
  micro / macro / global. This is redistribution, not topic loss.
- 329 semantic-obligation records were materialized. The prior discovery prompt
  already described `semantic_obligations`, but the rendered candidates had
  none. This repair made that review burden concrete.
- Candidate-specific support links, required context refs, root branch options,
  explicit facet obligations, review inventories, and authoritative routing
  records were added. Root IDs changed on 33 candidate records.
- The full `PRINCIPLES.md`, `COMMENTARY_SPEC.md`, `docs/CHANNELS.md`, and
  `_ayah_commentary/v2/PROMPT.md` were removed from discovery prompts and replaced
  by a new compact `discovery-policy.md`. Non-packet prompt content dropped from
  about 77 KB to about 13 KB per lane.
- Discovery gained `evidence_facts`; consolidation began receiving discovery
  JSON as well as scope prose. Composition and editorial prompts gained factual
  correction instructions.

Concrete ownership changes include
`29:38:23:inverse-rare-echo` (micro to global, citing 7:201) and
`29:38:22:next-ayah-participle-echo` (micro to macro, citing 29:39).
An agent with only its assigned packet now encounters a different set of topics
and supports even though the total source topic count is unchanged.

### `6f73a182`: new context data and revised record meanings

- Added `context_evidence`, `context_morpheme_columns`, and coverage records.
  Macro received 17 context ayat; global received 283 context ayat with 6,323
  QAC morphemes. The new context registry contributed about 40 KB to macro and
  639 KB to global before transport encoding.
- Added recursive `$v5_ref` lookups and an inline shared-value table to encode
  repeated evidence. Evidence remained inline, but reading it now required
  resolving another representation.
- Rewrote all candidates' `scope` fields to their effective lane, preserving the
  old value under `upstream_scope`; similarly updated connection relation scope
  and HFT ownership/scope metadata.
- Moved one previously published focus-only finding from global to micro.
  This brings the total ownership changes from the provisional baseline to 15.
- Expanded Quran-reference parsing and semantic-obligation extraction. The
  final obligation count is 330.
- Added ordinary-reading preservation and same-root lexical/form-restriction
  instructions to discovery and later writing stages.

The newly supplied context morphology can change what an agent can establish,
and the rewritten scope/qualification fields can change how it interprets
existing evidence. Neither effect is described by source topic counts alone.

### `90b02449`: transport expansion without new candidate content

Removed the `$v5_ref` encoder and its instructions; generated prompts again
contain complete repeated records. This alone increased prompt bytes by:

- Micro: 66,110.
- Macro: 141,185.
- Global: 340,972.

Across this transition, decoded packet content changed only in context evidence
provenance/coverage (113 additional serialized bytes per lane). Candidate fields
did not change. Most growth at this step is repeated wording, not new evidence.

The same commit added the QAC cache and production morphology checks. Those
infrastructure changes are separable from the decision to repeat full records.

### `928f4be8` and `1a8df9b3`: alignment corrections

In this 29:38 comparison, these revisions changed source alignment spans and
coverage, focus alignment information, and candidate `word_alignment`.
The bridge revision supplied exact links on all 49 word-analysis candidates;
it did not change their lane assignment or restore additional 29:38 topics.

The shared V3 preparation changes that preserve sparse analysis identities and
the verified bridge machinery remain dependencies of this correction. The
restored 110 topics in other packages documented by the earlier handoff are a
separate, valid effect.

## What did not change in the inspected source material

Across these six versions of the 29:38 p03 source bundle, every top-level field
other than `coverage` and `word_morpheme_spans` was byte-equivalent after
canonical JSON serialization. The repairs did not rewrite its word-analysis,
lexical, HFT, or reader-walk source content.

Across the provisional baseline and final prepared packets, the combined unique
inventories still contain 131 support IDs and 156 branch IDs. Shared supports'
text/payload content and branch semantic fields stayed unchanged. Changes were
to routing, links, structured context refs, and evidence qualifications. Some
records consequently appear in different lanes or are repeated in more lanes.

## Implication for restoring compatibility

Restoring the earlier workflow requires identifying the preferred historical
run and preserving its actual prompt contract, including instructions and
ownership. Shrinking JSON alone cannot restore it. The QAC bridge and small
alignment corrections can be kept separately from bulk context insertion,
candidate rerouting, policy replacement, and transport changes.

No production workflow, prompt template, or saved agent output was changed by
this audit. No model-based authoring A/B was run. The preparation differences
above are measured; their separate contributions to the reported behavioral and
performance regression have not been experimentally isolated.

## Proof of preserving data with earlier reception

A second temporary audit driver, `/tmp/v5_reception_compatibility_proof.py`,
captures current packets before the newer routing/obligation transformation and
builds an alternative discovery prompt. It changes no production code.

The prototype:

- Retains current source bundles, exact source topics, accepted QAC links, and
  corrected root identities.
- Restores original lane ownership and the earlier candidate/support/branch
  record organization. It omits the generated semantic-obligation and review
  inventories; their underlying claims remain in the unchanged source supports.
- Restores the full historical governing documents and discovery v1 output
  contract, with short notes explaining exact QAC alignment and the additional
  inline context data. It adds no external evidence reads or recursive string
  lookup scheme.
- Keeps every additional context-evidence record inline. It places these records
  with the agents that own the relevant candidates/connections under the earlier
  assignments. Evidence availability qualifications are updated to match those
  placements; they do not falsely say supplied morphology is absent.

This preserves factual evidence with an additive context section; it cannot
make the packet byte-identical to an earlier packet that lacked that evidence.

Measured 29:38 p03 prompt bytes:

| Lane | Earlier baseline | Current | Prototype, all factual additions retained |
| --- | ---: | ---: | ---: |
| Micro | 848,123 | 876,303 | 911,993 |
| Macro | 994,350 | 1,043,776 | 1,037,388 |
| Global | 1,368,058 | 2,076,949 | 1,990,406 |
| Total | 3,210,531 | 3,997,028 | 3,939,787 |

The prototype lowers total bytes by only 1.4% relative to current preparation.
Its global prompt remains about 45.5% larger than the earlier baseline. Restoring
the evaluation contract therefore does not by itself remove the additional
input burden. Micro grows because its original topics return with their newly
supplied context evidence.

Measured inventories for 29:38:

| Inventory | Earlier baseline | Current | Prototype |
| --- | --- | --- | --- |
| All candidates, micro / macro / global | 62 / 7 / 23 | 55 / 13 / 24 | 62 / 7 / 23 |
| Word topics, micro / macro / global | 49 / 0 / 0 | 39 / 4 / 6 | 49 / 0 / 0 |
| Generated semantic-obligation records | 0 | 330 | 0 |
| Distinct added context-evidence ayat, all lanes combined | No new registry | 298 | 298 |
| Distinct context-morpheme rows, all lanes combined | No new registry | 6,675 | 6,675 |

The prototype checks equality of candidate source identities and candidate IDs,
source topic IDs, candidate QAC links, corrected root IDs, unique context records,
support text/payload content, branch semantic fields, and connection IDs.

Concrete example: `29:38:23:inverse-rare-echo` returns from global to micro. It
keeps the exact source explanation linking the insight language to 7:201,
the newly supplied 7:201 Arabic/morphology in micro, and its accepted alignment:

```json
{
  "analysis_ref": "29:38:23",
  "qac_refs": ["29:38:16:1"],
  "status": "accepted"
}
```

The 29:38 pronoun fix also survives exactly:
`29:38:14` maps to `29:38:9:2` with status `accepted`.

The 5:3 p01 package was checked independently: the prototype delivers all 102
source word topics, including the 19 previously lost topics, and preserves all
304 distinct added context ayat / 8,795 context-morpheme rows. Its proposed
micro / macro / global prompt sizes are 2,295,977 / 2,305,602 / 3,476,320 bytes.

Example commands:

```text
python3 -B /tmp/v5_reception_compatibility_proof.py --case 29:38
python3 -B /tmp/v5_reception_compatibility_proof.py --case 5:3
```

Reviewable prototype prompts and summaries are under
`/tmp/v5-reception-compatibility-proof/29_38` and
`/tmp/v5-reception-compatibility-proof/5_3`.

For an implementation, the restored discovery contract and the corresponding
composition/consolidation/editorial handoffs must be kept consistent. The proof
above renders discovery only. A matched authoring comparison using the same
model/settings is still needed to assess whether restoring the contract recovers
the desired behavior despite the remaining increase in input size.
