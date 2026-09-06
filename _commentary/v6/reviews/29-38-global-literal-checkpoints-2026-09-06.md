# 29:38 global: literal checkpoints and independent facet activation

V6 is closed as an experiment after this run. R4 recovers the nine wider-context
mechanisms reduced to placeholders in R3, but retains source-selection errors,
loses V5 material, and produces inconsistencies between discovery and prose.
V7 will start from V5; V6 is a reference for failure cases, not an implementation
base. No agent output was edited by the reviewer.

## Frozen conditions

The baseline `afa4ebb8` was pushed before implementation. Fix commit `bb0810d8`
was then committed and pushed before this pilot was prepared or launched.

- Analysis: `pilot-29-38-global-r4-20260906145008`.
- Fresh `gpt-5.6-luna`, `max`, no inherited conversation. Global discovery is
  followed by the standard composition template in the same agent.
- Preparation: pericope 29:28–44, member surah 29, added 1:2–7, matching R3 and
  the latest V5 global preparation. Required morphology is complete; all 23
  focus analysis units have resolved alignment.
- The global packet is 2,061,437 bytes. Its focus, focus-surface, candidate,
  support, branch, connection, context, and selected-context records equal R3
  exactly. There are 22 batches and 111 scheduled evidence pages, unchanged.
- The prompt is 21,725 bytes, up 1,622 bytes from R3. The changes remove the
  mandatory core-facet rule, prohibit semantic scripts and file projections,
  replace manual checkpoint rewriting with literal updates, and require bounded
  state/source reloads. Composition uses the same bounded reader.
- Only the global package and matching reader/helper files were staged in
  `/private/tmp/v6-2938-global-r4-20260906145008`, preserving relative paths and
  bytes. No other lane, earlier output, or review was staged. This is directory
  isolation, not an operating-system access restriction. Monitor commands use
  the main checkout.
- No desired finding list or intervening semantic coaching is supplied. Agent
  output files are copied back verbatim; reviewers do not edit them.

This is a combined intervention. It does not isolate paging from procedural
instructions, and a single run cannot establish reliability on 7 MB packets.

## Independent checks before launch

The R2 published discovery at `0327ba22` contains an intransitive F001 activation
for `root_000848/B001` inserted after the old core/extension gate rejected finish.
A temporary in-memory copy removing only that activation reproduces the failure
with the baseline validator: `root_000848/B001 retains an extension without a
core facet`. The revised validator accepts the same copy. The archived agent
output was not changed. Exact facet/source and candidate-accounting checks
remain in place.

The new state reader was also exercised against the full R3 work and discovery,
using temporary verification copies: five work pages preserve all 1,662 leaf
values; four discovery pages preserve all 1,157. Maximum page sizes were 22,916
and 22,328 bytes. Reading did not change output bytes. The 18 focused reader and
checkpoint checks pass, including failed-update atomicity, explicit revision,
finalization protection, and Unicode/string-fragment preservation.

## Review method

Check public tool calls and responses against deterministic source pages, then
review semantic claims against the frozen Arabic, morphology, facets, and
context. Distinguish a delivered page, a structurally valid record, and a
supported interpretation. Trace useful checkpoint observations into findings
or specific dispositions, and trace each retained movement into Turkish prose.
Use the latest V5 global as a coverage comparison with its known errors, not a
gold answer or a finding quota. Do not inspect private reasoning text or infer
model behavior from online descriptions.

## Completed run and comparison

Discovery finalized with 24 candidate decisions and 15 findings. The parent's
completion check passed. The same agent then completed Turkish composition and
recorded its terminal event. Both phases' artifacts were copied back verbatim;
composition did not change discovery or checkpoint bytes. The local monitor is
stopped.

| Discovery observation | V5 global | V6 R3 | V6 R4 |
| --- | ---: | ---: | ---: |
| Finding records | 16 | 15 | 15 |
| Findings with branch activations | 16 | 6 | 14 |
| Branch activations | 31 | 6 | 22 |
| Distinct retained context ayat | 43 | 24 | 30 |

These counts describe the discovery records, not prose coverage or a quality
score. All three outputs retain candidate origins; R4 does not demonstrate
additional discovery beyond the supplied docket.

R4 recovers developed readings of discernment under testing (29:2–4), rival-path
invitation and failed burden transfer (29:12–13), socialized obstruction
(29:17,25,29), investigation of surviving evidence (29:19–20,35), practice as
inhibition (29:45), nonbinding knowledge (29:47–49,61–63), crisis-dependent
salience (29:64–65), security versus allegiance (29:67), and effort opening paths
(29:69). These also reach the prose. Transitive ṣadda uses F002 without an
unsupported intransitive core activation.

Remaining losses and errors:

- The Thamud finding excludes all fourteen dossier contexts (15:80–84 and
  27:45–53), retaining only a headline without branch activations or context
  refs. This regresses from R3 as well as V5. A missing lexical branch for the
  proper name does not preclude a return through the available dwelling term.
  Composition reintroduces the excluded context ranges, partly recovering the
  topic but leaving discovery and prose inconsistent and less concrete than V5.
- V5's 29:61 cosmic-direction contrast—ordered sun and moon, correct recognition,
  and human reversal—is absent. Merely retaining 29:61 under nonbinding knowledge
  does not preserve that distinct movement.
- Visible-sign and road-cutting exclusion reasons claim missing registration or
  descriptors, although `root_000074/B003` and `root_001240/B023` have supplied
  `SOURCE_IMAGE` facets. The effect-left facet `root_000180/B002` is also not
  activated. Some of these ideas survive as contextual narrative, but their
  explicit lexical development is reduced from V5.
- Two dwelling findings use B009/F002 without arguing a bridge from ordinary
  *masākin* to the restricted *sakanāt* usage. B002/F002 directly supplies the
  dwelling-place sense. V5 also misused B009 in its investigative finding; R4
  extends that problem to the basic dwelling-witness finding. Prose retains
  the unsupported fixed-position framing.
- The path-thread discovery incorrectly calls the path the object of ṣadda.
  The object is the pronoun “them”; “from the path” is a prepositional phrase.
  Composition avoids repeating that grammatical error.
- The investigative finding's dwelling activation names 27:52 and 46:25 in its
  trigger wording but lists 29:19–20 and 29:35 in its trigger refs. Composition
  uses the investigative contexts, but the discovery record remains inconsistent.

The evidence behind these issues is present. Delivery and structural validation
do not establish correct selection, interpretation, or preservation. This run
shows meaningful recovery from R3, not a clean replacement for V5 or a controlled
estimate of any single procedural change's effect.

[R4 discovery](../raw/pilot-29-38-global-r4-20260906145008/s029/29_38/global.discovery.json),
[R4 prose](../raw/pilot-29-38-global-r4-20260906145008/s029/29_38/global.scope.tr.md),
[V5 discovery](../../v5/raw/s029-p03-with-fatiha/s029/29_38/global.discovery.json),
[V5 prose](../../v5/raw/s029-p03-with-fatiha/s029/29_38/global.scope.tr.md),
[R3 review](29-38-global-v5-semantics-2026-09-06.md).
