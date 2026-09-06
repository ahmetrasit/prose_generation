# 29:38 global: V5 semantics with V6 reading

Restoring the V5 semantic instructions did not recover the latest V5 global
analysis in this run. Discovery completed its reading plan and passed the
mechanical check, but nine of its fifteen finding records are generic attributed
placeholders. The same-agent composition carried that contraction into Turkish
prose. The agent outputs below are preserved without reviewer edits.

## Conditions and artifacts

- Prompt rollback commit: `cb7b2d55`, committed and pushed before this run.
  The two added semantic blocks were removed; V6 reading/checkpoint instructions
  and the inherited core/extension rule remained.
- Analysis: `pilot-29-38-global-r3-20260906130518`.
- Fresh GPT-5.6 Luna agent, max reasoning, global only; discovery followed by
  the standard composition template in the same agent. No desired findings,
  prior answers, or intervening semantic feedback were supplied by the reviewer.
- Preparation matches V5 `s029-p03-with-fatiha`: pericope 29:28–44, member
  surah 29, and added 1:2–7. Shared branch, support, context, and focus evidence
  match the V5 preparation. Version and analysis metadata differ.
- Frozen global packet: 2,061,437 bytes; instruction prompt: 20,103 bytes.
  There are 24 candidates, 133 branches, 253 connections, and 283 context ayat.
- Discovery: 13:06:29–13:51:53 UTC, 45m 24s. Composition:
  13:52:41–13:58:17 UTC, 5m 36s. Four natural discovery compactions occurred
  at 13:17:50, 13:27:05, 13:34:44, and 13:43:52 UTC. None was forced.
- The local pilot monitor ran through both phases and was stopped afterwards.
  The agent emitted an early completion event after discovery; the composition
  follow-up recorded a new started event and its final completion.
- The current R2 checkpoint and discovery were removed before launch as
  requested. Their originals remain in Git at `0327ba22`.

[Prompt](../input/pilot-29-38-global-r3-20260906130518/s029/29_38/global.discovery.prompt.md),
[packet](../input/pilot-29-38-global-r3-20260906130518/s029/29_38/global.packet.json),
[plan](../input/pilot-29-38-global-r3-20260906130518/s029/29_38/global.reading.json),
[checkpoint](../raw/pilot-29-38-global-r3-20260906130518/s029/29_38/global.work.json),
[discovery](../raw/pilot-29-38-global-r3-20260906130518/s029/29_38/global.discovery.json),
[Turkish prose](../raw/pilot-29-38-global-r3-20260906130518/s029/29_38/global.scope.tr.md).

The final discovery SHA-256 is
`8a376faf340b3708af90b7e93d8d0126aa2358ff4487666de87868fc857ecaa7`;
it was unchanged by composition. The prose SHA-256 is
`cf1a5356aa691b35722ce5cb9f16b4f87dbaaa0897641ce7288ae2c20c1b6b2e`.

## What the actual run establishes

An independent read-only comparison of transcript tool responses against the
reader's pages found all 125 scheduled pages exactly intact: 111 evidence
pages and 14 catalog pages. All 22 batch reviews persisted. The required
`discovery.py ... check` passed, and final discovery equals checkpoint discovery.
This verifies delivery and accounting, not the soundness of the findings.

Later retrievals were less reliable. Four discovery tool calls produced explicit
truncation warnings: 13:39:04, 13:39:43, 13:44:09, and 13:45:08 UTC. They included
bulk candidate projections, multi-branch dumps, and broad searches. Subsequent
targeted extractions recovered some material; those do not justify calling all
retrievals intact. The initial composition `cat` also truncated; the agent then
extracted the finding fields and the nine retained obligations separately.

The 13:44:09 search also returned other-lane prompts and part of the current
micro packet. This violated the assigned global evidence boundary. The inspected
response did not expose a previous agent answer, and no effect on particular
findings is established, but this is not a fully hermetic comparison run.

## Main semantic failure: scripted narrowing removes the reading

At 13:50:36 UTC, the producing agent's `narrowFinding(cid)` used:

```javascript
const c = candidates[cid], first = c.obligations[0];
```

For each of nine structured HFT candidates it kept that first obligation ID,
set `branch_activations` and `context_refs` to empty arrays, and generated the
same mechanism, payoff, containment, and exclusion wording. Its mechanism says
only that the source is retained as attribution. Its payoff addresses what the
composer can see, rather than what the focus ayah means differently.

This is more than mechanical serialization. The function chooses retained
semantic content by array position and substitutes a generic account of source
status for an interpretation. There are 57 identical branch-exclusion reasons,
23 identical context-exclusion reasons, and 94 identical exclusions of additional
HFT obligations. These state the result of exclusion without assessing the
particular semantic contact.

The retained IDs do not repair that loss. For the rival-path candidate, the
first retained obligation specifically describes turning another away as the
movement operationalized by a rival invitation. Its branch and 29:12–13 context
are nevertheless excluded. For field evidence, the retained obligation describes
manifest disclosure from the sites, while the available travel, looking, trace,
and sign context is discarded. These are references to obligations without
their full analytical realization.

The loss is not explained by missing initial evidence or erased checkpoints.
The `candidates-002` note explicitly recognizes failed burden transfer,
socialized obstruction, field observation, inhibitory practice, and nonbinding
knowledge with their context refs. `candidates-003` recognizes crisis-dependent
salience, security, and committed effort. Those notes survived; the later
synthesis reduced the proposals according to their `legacy_unbound` status.
The inherited prompt says source trust controls qualification rather than
automatic acceptance or rejection.

Six word-based resonances remain recognizable. The anatomical dwelling facet
and the previous invented intransitive activation are absent. However, the
core/extension validator is unchanged; avoiding those activations does not
establish that its underlying defect is fixed.

## Comparison with the latest V5 global

The comparison uses
[V5 discovery](../../v5/raw/s029-p03-with-fatiha/s029/29_38/global.discovery.json)
and [V5 prose](../../v5/raw/s029-p03-with-fatiha/s029/29_38/global.scope.tr.md).
V5 has its own facet and morphological wording problems and is not a gold
standard. These counts describe retention, not an automatic quality score.

| Observation | V5 global | This V6 run |
| --- | ---: | ---: |
| Finding records | 16 | 15 |
| Findings with branch activations | 16 | 6 |
| Branch activations | 31 | 6 |
| Distinct retained context ayat | 43 | 24 |
| Retained semantic-obligation IDs | 87 | 27 |
| Excluded semantic-obligation IDs | 43 | 103 |
| Prose bytes | 18,841 | 8,894 |

V5 explains the false burden-transfer promise in 29:12–13, travel and inspection
meeting a surviving sign in 29:19–20 and 29:35, and the tension between available
knowledge and continuing denial in 29:47–49 and 29:61–63. V6's corresponding
paragraphs retain small attributed possibilities while repeatedly saying their
independent triggers were not retained. The contexts remain in the frozen
packet; discovery discarded their use in these findings.

Composition did recover the wording of the nine first obligations and express
them in Turkish. It also preserved the transitive wording of `ṣaddahum`. It did
not reconstruct the discarded global mechanisms. Its nine-proposal sequence
discusses retained triggers and branch activation as workflow matters, and its
first six readings provide fewer concrete contextual and grammatical details
than V5. A paragraph count and literal presence of context references did not
establish the composition contract's required semantic landings.

All final findings have candidate origins. That does not justify imposing a
quota, but this run supplies no positive demonstration of independent discovery.
It also does not establish performance on a 7 MB packet.

## Assessment of the procedural-overhead review

The review correctly identifies additional model work: scheduled paging,
checkpoint maintenance, a second catalog pass, exact retrieval after compaction,
and completion checks. Initial verification protected source delivery more
thoroughly than it evaluated the cost and semantic outcome of using that source.

Several qualifications matter:

- V5 also supplies a prompt-file path and asks for bounded reads and ID joins.
  Inlining the packet in a file did not automatically put it all in model context.
- V6 still computes batches, dependency groups, pointers, and progress. The HFT
  inventory changes described in the review are separate from this V6 reader.
- The finding schema and exact facet wording were already present in V5.
  V6's hard core/extension gate enforces an inherited prompt requirement.
  The prior run directly showed that gate inducing a bad activation; paging
  overhead is not needed to explain that specific defect.
- Tool and token totals establish work performed, not how much analysis it
  displaced. No matched local V5 scope trace establishes Luna–Sol parity or
  deliberate economizing. This review draws no online model-behavior inference.
- The evidence is substantively matched, not byte-identical across all version
  and preparation metadata. Lossless delivery alone does not establish sound
  interpretation or reliable large-packet operation.

Discovery used 233 orchestration tool calls and 75,552 output tokens, including
18,400 reasoning tokens. Cumulative input was 28,797,819 tokens, of which
27,664,896 were cached. Through composition there were 247 calls and 91,185
output tokens, including 26,327 reasoning tokens; cumulative input was
30,489,524, including 29,310,720 cached. These input totals repeatedly count
conversation history, not unique evidence. They are observations of this run,
not a controlled measure of the cost of V6 relative to V5.

## Assessment of the proposed script restriction

The sibling repository's `focus_trace/prompts/focus_trace_hermetic.md:31`
explicitly says: "Do not write scripts, helper programs, parsers, workflow files,
or patches." Current V6 has no blanket script ban. It already prohibits
filtering or projecting evidence before reading it; that rule was added after
the initial pilot's lossy `statements.statement` projection.

The initial `facet_for()` default and this run's `narrowFinding()` are direct
examples of scripts making semantic choices. A short restriction addresses that
pattern without promising to eliminate unsupported judgments made without code.
A literal blanket ban would also conflict with V6's present requirement to load,
preserve, and atomically update checkpoint fields.

A proposed procedural addition, not applied to this run or the current template:

> Use the supplied reader. Do not write scripts that select facets or carriers,
> decide interpretations, or reduce evidence. Code may only save your explicit
> judgments and copy exact source fields by identities you have already selected.

This is a small next intervention worth evaluating. It does not fix the
core/extension rule, guarantee compliance with intact retrieval, or replace
independent semantic review. Further reader improvements should reduce repeated
retrieval and serialization work while preserving exact evidence and full
discovery opportunities. They should be judged on retained mechanisms and
accurate source use, alongside delivery and operational cost.
