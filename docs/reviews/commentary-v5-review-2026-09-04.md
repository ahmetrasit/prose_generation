**Commentary v5 review — 2026-09-04**

Review baseline: commit `7f1ac73c`. This is a review of code, assembled inputs,
prompts, and existing output, with 29:38 as the main comparison case. No new
semantic agents were launched and no workflow implementation was changed.

**Understanding of the intended workflow**

The objective is to make an ayah more intelligible through its wording and the
readings that become possible when independently supplied evidence activates a
particular meaning. The ordinary grammatical reading remains recoverable.
Grounded alternatives coexist; interpretive disagreement does not require a
winner. An available dictionary sense, retrieval label, or prior model finding
is a nomination, not proof of activation.

Micro examines the focus surface and contacts within it. Macro examines the
declared local context, with the host basmala and explicitly added ayat. Global
examines wider evidence that changes the focus reading through a specific word,
relation, or act. The code prepares the evidence; agents make semantic decisions.
Each scope agent first records findings, then writes prose in the same session.
A fresh consolidator combines the three prose drafts and performs its own
editorial follow-up. The final validator checks display format.

This division is useful. Its present weaknesses are in evidence preparation,
prompt consistency, and preservation of the explanation connecting a lexical
source to an unusual reading.

**Evolution visible in 29:38**

| Version or change | What the comparison shows |
| --- | --- |
| Earlier Layer 2 output | The archived 29:38 prose explicitly explains the same-root, red-veined eye-film resonance and its contact with sight, the spider, and weakness. It provides a useful comparison for the explanation a reader needs. |
| V3 | Broader scoped evidence and extensive review/repair machinery. The saved prose retains the eye-film and worked-road material, but also accumulates negative qualifications and repeated explanatory statements. |
| V4, especially `097b3e38` and `e86c67b2` | Stronger exact preservation and provenance. The current 29:38 editorial friction records 75 findings and 98 immutable branch sentences. The prose contains many repeated sentence frames and grammatical fragments. Exact preservation did not ensure good exposition or sound interpretation. |
| Initial V5, `fe7ccf8e` | Separates discovery from composition, while initially retaining a large preparation/validation implementation. |
| Simplification, `8c99bbf2` | Removes the state machine and much bookkeeping, but also removes semantic preparation functions still assumed by the discovery prompt. |
| Current V5 | More flexible prose and several useful uncandidate findings. The latest 29:38 run restores the red-veined detail lost in an earlier V5 consolidation, but still does not adequately explain its lexical origin. |

The historical outputs are comparison material for this review, not an approved
list of readings that future agents must reproduce. Different evidence contexts
and model runs prevent treating output differences as a controlled experiment.

**Findings, in priority order**

1. **Discovery asks for fields that preparation does not supply.**

   The [discovery prompt](../../_commentary/v5/prompts/discovery.md) expects
   `root_branch_options`, `semantic_obligations`, and
   `required_branch_facets`. None occurs on candidates in the saved or freshly
   generated 29:38 packets. Word-analysis candidates also have empty `root_ids`
   where the prompt describes normalized identities.

   This is a specific simplification regression. Immediately before
   `8c99bbf2`, V5 had `_normalize_word_analysis_root_ids`,
   `_candidate_semantic_obligations`, `_required_candidate_branch_facets`,
   `_candidate_root_branch_options`, and `_normalize_and_route_lane_packets`.
   Current [packet assembly](../../_commentary/v5/workflow.py) calls the v3
   projector and appends context units without these transformations. The agents
   explicitly mention the missing obligation identifiers in their discovery
   friction notes.

   Restore the small, useful preparation functions and test the real rendered
   packet against the prompt contract. Merely deleting the instructions would
   discard useful support for discovery and semantic preservation.

2. **Candidates can be rejected because they were sent to the wrong lane.**

   In the latest 29:38 micro discovery,
   `29:38:22:next-ayah-participle-echo` is rejected because its 29:39 echo is
   outside micro. Its support explicitly describes the movement from failed
   insight to failed escape through the repeated auxiliary-plus-participle
   construction. It is not handed to macro. Macro independently retains a
   related state construction, but this does not establish preservation of that
   specific insight/escape relation.

   All five reader-walk candidates are routed to global. The global discovery
   rejects them, citing focus-only anchors, non-citable legacy material, or
   unstructured context references. One retrospective explicitly names
   29:41–43 and relational reasoning through the parable; another names 29:61.
   The [v3 walk extractor](../../_commentary/v3/v3lib/prepare.py) gives these
   records only the focus anchor and marks their supports non-citable. V5 no
   longer normalizes the additional references and routes them by actual scope.

   Normalize references from these known source formats, attach available Arabic
   and typed occurrences, and route by required context. Preserve the legacy
   qualification. A failed evidence binding should be distinguishable from a
   semantic judgment that the reading has no payoff.

3. **Declared context and inherited lane routing can disagree.**

   Reproduced with real inputs:

   ```text
   prepare --analysis-id review-split
     --segment a=29:38 --segment b=29:41 --ayah 29:38
   ```

   The selected 29:41 context unit is global, as the segment contract requires.
   The 29:41 connection remains macro because the inherited v3 projector uses
   the bundle's native 29:28–44 pericope.

   A second probe used `--add-ayat 44:32` with host 29:38–41. The added ayah
   appeared as macro context and remained a global connection. Thus “enters
   macro once” is true only of the appended context object, not of all evidence
   about that ayah. This also weakens the external-overlay procedure, which is
   supplied only to macro.

   Compute one effective context/routing map before projecting candidates,
   supports, connections, and context units. Test their agreement end to end.

4. **The prompt payload is substantially larger than the discovery task needs.**

   The saved latest 29:38 prompts contain:

   | Lane | UTF-8 bytes | Candidates | Branch records | Connections |
   | --- | ---: | ---: | ---: | ---: |
   | Micro | 848,090 | 62 | 97 | 0 |
   | Macro | 900,582 | 7 | 124 | 16 |
   | Global | 1,368,025 | 23 | 133 | 253 |

   The branch registry alone occupies approximately 580,000–621,000 characters.
   Every lane repeats the full focus atlas. Within each atlas, definitions,
   facets, glosses, boundaries, lexical distinctions, and source summaries often
   restate overlapping information. Neighbor distinctions account for about
   140,000 characters per lane and contextual glosses another 66,000. These
   fields can contain valuable distinctions, so their reduction must be semantic,
   not a blanket deletion.

   Four embedded governing documents add approximately 10,600 whitespace words
   per lane before the discovery wrapper. They include Layer 3 instructions,
   retired overlay procedures, worked Fatiha examples, and older four-artifact
   output requirements. V5 overrides some of these, but the agent still has to
   interpret the entire instruction stack. The Fatiha examples can also prime
   an interpretation before the explicit overlay procedure.

   The packet is serialized onto one JSON line. A normal bounded terminal read
   can truncate this evidence without giving useful record boundaries. The
   16 MB byte ceiling is not a model-token or evidence-reading budget. Real
   preparation for 24:31 produced a global prompt above 3.3 MB.

   Use a short V5-specific policy, one focus surface, one occurrence table, and
   one record per branch/facet or connection. Keep all distinct senses, unusual
   details, lexical-form restrictions, and counterevidence discoverable. An
   allowlisted evidence appendix can hold longer source excerpts; the compact
   discovery cards must expose the unusual facets so agents know to inspect
   them. Prefer record-sized pages to one huge line. Measure actual token size
   and verify that agents can read the complete required evidence.

5. **A preserved image can lose the explanation that makes it linguistic.**

   The latest [29:38 editorial prose](../../_commentary/v5/editorial/s029-38-41-with-fatiha/s029/29_38/29_38.prose.editorial.tr.md)
   retains the red-veined, web-like eye film. Its packet supplies a precise
   lexical witness for `root_000672/B010`, including the comparison to a spider's
   web. But the prose presents the film as something that can be imagined when
   road, perception, spider, and weakness meet. It does not clearly explain the
   separate lexical item in the same root family that licenses the association.

   Likewise, the thick edge and joining seam survive as architectural details,
   but their relationship to the supplied b-ṣ-r lexical branch disappears from
   the consolidated paragraph. The reader sees a building analogy without
   learning why this particular ayah's word made it available.

   This is semantic loss even when the nouns and images survive. Preserve the
   whole explanatory chain: focus carrier → attested lexical capacity and its
   form restrictions → independent contextual contact → changed understanding
   → boundary. Clearly distinguish local lexical meaning, a same-root resonance,
   and a contextual analogy. A same-root dictionary item is not automatically a
   sense of the focus form.

6. **The writing stages cannot reliably catch an analytical error.**

   The latest micro prose calls `mustabṣirīna` the object-position predicate in
   a transitive construction with `kānū`. This survives consolidation and
   editorial at line 49. It is an accusative predicate of kāna; accusative case
   does not make it a transitive object. The
   [Quranic Arabic Corpus explanation of kāna](https://corpus.quran.com/documentation/verbkaana.jsp)
   distinguishes subject/predicate dependencies from subject/object dependencies;
   its [29:38 morphology](https://corpus.quran.com/wordbyword.jsp?chapter=29&verse=38)
   identifies the closing participle as accusative.

   The prepared word-analysis support already describes a copular construction.
   The incorrect “transitive/object” explanation enters the scope prose. The
   current format validator correctly returns `ok`: grammar is outside its job.

   Consolidation receives prose without the discovery records or source checks,
   and is instructed to preserve every finding. Give it compact retained finding
   records and the source snippets needed to check consequential grammatical and
   lexical claims. Permit correction of demonstrable source misstatements while
   preserving grounded alternative readings. A bounded check within the existing
   sessions can do this without restoring the old review/repair state machine.

7. **Global evidence is broad, but often linguistically shallow at the target.**

   The global packet preserves 253 connection records, including weak and
   opposite-direction evidence, which is valuable for distributed discoveries.
   Their target evidence generally supplies exact Arabic but no target morphology.
   Context members added through the composition path receive lean root cues;
   ordinary global targets do not automatically receive the same data even when
   a local bundle is available.

   Keep Arabic-only comparison available, but provide typed target morphology and
   relevant lexical distinctions when a proposed reading depends on them. Preserve
   compact missing-data information. Current V5 removes the entire inherited
   `source_coverage` block, although some HFT-specific coverage remains elsewhere.
   Removing hashes need not remove knowledge of what evidence is absent.

8. **Uncertainty about evidence sometimes leaks into reader prose as machinery.**

   The latest editorial repeatedly says target morphology or trust levels were
   not established and refers to Fatiha as “explicitly added” context. Those are
   production facts. The reader needs the substantive boundary: what the analogy
   supports, what it leaves open, and what it does not establish. Keep operational
   qualifications in discovery friction; translate consequential uncertainty into
   ordinary reader language.

9. **Input readiness is uneven despite passing code tests.**

   Real preparation succeeded for native 29:38, 29:0, 1:1, 87:1, 100:1,
   24:31, 24:61, and 48:29. Existing 73:20 and 14:22 bundles failed because
   `word_morpheme_spans[0]` lacks required `morpheme_skip_count`. The current
   bundle builder emits this field. This is stale-input incompatibility; rejecting
   it is appropriate, but a bulk run needs a readiness check and rebuild list.
   Probes for 9:1 and 2:282 also encountered missing focus bundles.

   The S87:1 fix in `7f1ac73c` is useful: unresolved evidence can reach authoring
   instead of stopping preparation. Ambiguous root mappings should remain explicit
   alternatives, so expanding a citation does not imply that every alternative
   lexical identity has been established.

10. **Operational “passed” can be inferred without validation evidence.**

    In [monitor.py](../../_commentary/v5/operations/monitor.py), an editorial file
    can make canonical appear completed without a lifecycle event; canonical
    completion then synthesizes validator status `passed`. An isolated probe with
    an empty editorial file and no events returned task `completed` and validator
    `passed` at attempt zero.

    The runbook correctly reserves canonical `completed` for a successful
    validator run. Preserve that explicit event as the attestation. A discovered
    file with no such event should show an unverified state. This is a dashboard
    correctness issue, separate from semantic analysis.

**A leaner discovery and writing contract**

Keep the current three-scope architecture and separate discovery/composition
turns. Consolidate the instructions around this sequence:

1. Establish the focus's ordinary reading and grammatical relations.
2. Inspect all compact focus-branch cards and relevant context for uncandidate
   contacts. Do this before deciding supplied nominations; do not require a quota
   of new findings.
3. Test each proposed reading: exact carrier, independent evidence, lexical or
   analogical mechanism, material change, and containment. Ask what remains of
   the proposal if its claimed trigger is removed.
4. Decide every supplied candidate, preserving distinct supported obligations and
   recording bounded reasons for omissions. Keep unsupported evidence bindings
   separate from semantic rejections.
5. Preserve counter-readings without choosing a winner. Contextual analogy must
   remain distinguishable from lexical predication.
6. Write from compact retained findings, then check that the lexical link,
   contextual link, concrete detail, changed reading, and boundary all remain
   intelligible in prose.

The current latest micro run has 51 findings, all candidate-derived; its 12
branch activations belong to the three supplied HFT nominations. Macro and
global contain seven uncandidate findings between them. These counts show that
uncandidate discovery is possible, but do not demonstrate exhaustive discovery
or prove that micro missed a valid reading. They support testing a less
candidate-led order.

For prompt evaluation, use 29:38 as one case alongside short grammatical ayat,
long ayat, sparse-source cases, and split-root cases. Compare grammatical
accuracy, retained explanatory mechanisms, grounded new discoveries, semantic
loss during rewriting, and evidence-reading cost. Include a run without HFT or
channel nominations to see what the raw evidence can elicit. A blind control
requires genuinely separate evidence delivery; an instruction to quarantine
material already visible in the prompt is only a reasoning procedure.

**Verification and limits**

- 62 V5 workflow/composition/format tests passed.
- 31 operations-monitor tests passed.
- 73 inherited v3 preparation tests passed.
- Fresh prompt preparation and the routing probes used temporary output roots.
- The latest saved 29:38 editorial passes the mechanical prose validator.
- Candidate decision IDs cover every supplied candidate exactly once in all
  three latest 29:38 discovery files. A source-binding spot check found no unknown
  branch/facet IDs or mismatched copied gloss/facet text in their activations.
- No new model runs, cloud monitor session, or whole-corpus semantic audit were
  performed. The proposed prompt reductions have not yet been tested in an agent
  ablation study.

The implementation priorities are: restore evidence normalization and routing;
reduce duplicate instructions and payload while exposing every distinct facet;
then add compact semantic preservation and source-correction checks within the
existing agent sequence. These changes address the observed failures without
requiring the old orchestration machinery.
