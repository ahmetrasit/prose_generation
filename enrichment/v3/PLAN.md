# Ayah enrichment v3: lean rewrite plan

Status: the initial 1:6 pilot was interrupted after scope corrections. Both tracks restart from scratch with the finalized prompts, independently with Sol max and Astra xhigh. Earlier outputs are excluded from the clean run and model comparison; their incurred cost remains separate. Shared helpers retrieve material and report native usage; they do not spawn agents. A general batch runner is not implemented. Input: v16 r13 plus existing augment9 when available; otherwise bare r13. Enrichment does not rerun augmentation.

Execution preference: Standard only; Fast is forbidden. Manual CLI launches explicitly set `service_tier="default"` and `features.fast_mode=false`.

## Decision

Rewrite the research sequence and reuse the corpus, source metadata, retrieval utilities and useful paragraph handling. Patching validators alone cannot repair research that never sees the prose's claims. Rebuilding the corpus would add unnecessary work.

The [independent assessment](../v2/audits/2026-10-06-ayah-independent/assessment.md) demonstrates the omissions. The [Sol max review](REVIEW_SOL_MAX_2026-10-06.md) supports the focused rewrite. Its scholarly coverage recommendations are retained; its proposed bookkeeping is reduced here to respect the user's latest instruction. This plan takes precedence over the review's more elaborate proposals.

**No hashes, fingerprints, provenance manifests, delivery/exclusion ledgers, claim-by-source matrices, custom acceptance framework or bookkeeping passes.** Keep only the information needed to understand a claim, research it and attach a useful source note.

Finalize the instructions before launching a run. Do not change instructions for running agents or resume their contexts under revised instructions when earlier directions may affect the output. Stop the affected work, finalize the change, and restart it in fresh contexts from the original inputs, regenerating any dependent inventory or notes. Keep prior outputs out of the replacement run. Native usage logs distinguish interrupted and clean-run costs; no separate restart ledger is needed.

## 1. Read the frozen page and identify its claims

Follow [INVENTORY_BRIEF.md](INVENTORY_BRIEF.md). Read the complete page, including augmentations. Produce a compact list containing a claim ID, its paragraph/addition location and a short description of the proposition. Use existing paragraph markers; do not ask the model to calculate offsets or transcribe the prose.

Capture every substantive finding, relationship and qualification in neutral wording. Keep research instructions out of claim descriptions: no requests to test an inference, verify an entry or decide whether the prose is justified. Repeated findings can share a claim with links to each occurrence; distinct inferences in one paragraph stay distinct. Do not turn incidental wording into unnecessary research assignments.

Consider learned knowledge across this claim set and record useful remembered sources or differing interpretations. Memory supplies leads, not verified attributions. Later researchers may add leads; an empty initial list does not close discovery.

The frozen prose supplies the findings to enrich. Collect literature that supports, conflicts with, expands on, or shifts the perspective on each finding. Report the external author's position, the relevant relationship and a recoverable pointer. These are relationships in the literature, not assistant confirmation or criticism of the prose. Do not verify, validate, correct or re-establish its statements, inferences or premises. Existing prose and documentation do not establish what an external source says; the source itself supplies that attribution.

No dictionary checking or dictionary pass: the user has already checked the entries upstream. Do not reopen entries, trace branches, validate mappings or substitute learned/later/modern definitions. Lexical explanations encountered in external commentaries can be reported as those authors' views. The operational boundary is in [RESEARCH_BRIEF.md](RESEARCH_BRIEF.md).

## 2. Research the claims and write the reader's notes directly

Use the claim list across tafsir traditions, hadith and meal passes. Each specialist gets the compact page-wide claim list, the actual paragraphs relevant to its current assignment, and source material. It can request another paragraph when a connection emerges. This prevents context selection from hiding claims while avoiding repeated delivery of the whole page.

Attention quality takes priority over reducing call count, even at equal or higher total cost. Start with roughly 25–50K input tokens per research call and split before about 60K; these are pilot settings, not proven safe thresholds. Split earlier when numerous claims or conflicting positions make a packet dense. Use fresh contexts and coherent claim/source groups; do not inherit unrelated conversations or compress away necessary context to meet a size target.

Read the available, in-scope commentary tied to the target ayah, including overlapping ayah ranges. Do not replace these passages with a ranked keyword search. Include the relevant meal panel and its substantive notes. Combine small compatible source groups when useful, preserving different authors and schools.

Broader searches follow the claims: cross-referenced ayahs, concepts, spelling variants, known reports and memory leads. Hadith searches must work even when a report does not quote the target ayah. Split them into coherent finding groups; use `corpus.py search/get --no-translations` for primary text and relevant attribution/grade metadata, adding a translation only when needed. The flag matters for previews as well as full reports. Do not load three languages by default or import every commentary on every cited ayah automatically. Save gathered notes before a context becomes crowded and move unfinished discovery to a fresh assignment. A search limit or unavailable source remains a limitation, never evidence of novelty.

Read a shared passage once for the claims it can address. Exact duplicate text may be reused with all source identities retained; similarity must not erase a contrary position or additional argument. Previously written notes may help discovery but do not establish completeness for new claims.

Write concise Turkish awareness notes directly. Each note needs only its claim link(s), an attributed external position and a recoverable source location. Usually one sentence per distinct position suffices; preserve useful reasons, objections and qualifications. Make supporting, conflicting, expanding or shifting relationships clear where useful without mandatory labels or four-way checklists. Do not repeat the finding, judge its validity or append routine statements about what each source does not prove or discuss. Do not produce intermediate source essays, placement drafts or ranked translation reviews.

Every assigned claim must be considered, even after a supporting source is found. Capture materially different positions in the material read. Record useful unresolved leads or a scoped no-match briefly where needed, not a row for every claim/source combination. The source passes produce notes and research exceptions, not separate coverage ledgers.

Support the enrichment's own report attributions with source pointers and attribute grading judgments to their sources. A tafsir passage can establish that a scholar used a report. Preserve that reception even if the report is weak, disputed or ungraded; do not imply that reception proves authenticity or conduct a new authenticity investigation. Unverified memory pointers must be labelled.

## 3. Review once, repair only substantive gaps, then render

The final review is one substantive stage, split into paragraph groups if the full page, notes and supporting excerpts would be crowded. Each group receives its actual prose and additions, relevant notes/evidence, the compact page-wide claim list and context needed for cross-paragraph inferences. Review each paragraph once; do not add another whole-page reread afterward. It checks the work itself:

- Does every substantive claim and augmentation have an adequate note or an explicit unresolved/scoped-negative explanation?
- Do the notes address the actual findings, represent their sources faithfully and retain supporting, conflicting, expanding and shifting perspectives where found?
- Do they report attributed external positions without assistant verdicts about the prose, and describe historical novelty only within the research actually performed?

The reviewer can inspect fuller external passages where an omission, compression or novelty judgment warrants it. It reviews the enrichment's coverage and source fidelity, not the frozen prose or dictionary. It does not routinely repeat every source pass or produce another ledger. Newly noticed findings or missing source relationships trigger focused enrichment; unchanged notes stay unchanged. This review does not prove that every possible historical source has been exhausted.

Historical novelty concerns whether earlier treatment was located, never whether the finding is valid. When useful, distinguish discussion of components from treatment of their synthesis, and consolidate a scoped no-match statement after the relevant discovery. Do not repeat that statement for each author. A credible unresolved lead keeps the historical question open. Supporting literature does not cancel a conflicting reading or an unfinished search.

Unfinished assigned work stays unfinished. An inaccessible external lead may remain visibly unresolved beside useful established notes; do not retry it indefinitely. Readers must see material limitations and must never have to infer novelty from silence.

Place notes after their paragraph and its augmentation using a simple script. Preserve the original text and separators rather than rebuilding the page from normalized paragraphs. Reuse source metadata for readable citations. There is no model placement/composition pass or additional acceptance stage. Ordinary missing-output, broken-reference and rendering errors are handled where they occur; they are not a substitute for scholarly review.

## Keep the working material small

Use the existing frozen file, one compact claim list, direct research notes with source pointers, and the rendered page. Keep only useful research exceptions with those notes. Source text stays in the existing corpus; native runner logs suffice for troubleshooting and usage totals.

- Deliver a packet inline or by file, never both. Batch reads and do not reread material successfully received within a task.
- Send only relevant paragraph context and source passages. The small claim index is the deliberate safeguard against missing connections.
- Use short task instructions. Do not include design documents, full schemas, unrelated source metadata or unused dictionaries.
- Bound packet size and leave room for reasoning and output. Split at meaningful boundaries; no whole-surah or final-review exceptions. Necessary overlap that preserves an argument is not redundant reading.
- Write usable notes once. The final review returns corrections and additions only; scripts handle placement and citation formatting.
- Reuse existing findings where the claim and source still apply, without a cache-fingerprint system. If the base or material changes, rerun the affected work explicitly.
- Measure total tokens and repair work from native usage logs. Do not invent percentage savings from character counts or incomplete earlier runs.

## Implementation and pilot

1. Add the r13/augment9 input selection, compact claim/note format and simple rendering. Reuse working corpus access and source identities.
2. Implement claim-aware source passes, overlapping-range retrieval, useful spelling/concept searches and bounded packets. Remove the old source-first extraction, placement and residual-gap sequence.
3. Complete the user-requested parallel 1:6 pilot with one substantive final review per track. Then exercise the known 1:1 omissions, 87:1/87:6 and bare-r13 input before broader use. Keep pilot output separate from existing enriched pages.

Use the already demonstrated failures to assess the pilot: 1:1 paragraphs 4, 14 and 23 with their additions; omitted hadith; multi-ayah passages; a contrary position inside an already used source; unsupported paraphrases; and an unresolved memory lead. Also inspect the rest of the pilot page—recovering known examples is not enough. Use focused mechanical checks for the changed input/rendering behavior, not a new testing or acceptance framework.

The pilot must give the tafsir writer useful source awareness for every claim, preserve material disagreement and show uncertainty honestly. Inspect dense passages for missed secondary findings even when packets fit the token target; packet size alone cannot establish attention quality. Expand only after inspecting that actual output. Optimize packet grouping after quality is demonstrated, keeping the least expensive approach that still achieves it.

## Response to the Sol max review

Retain claim-aware research, direct ayah/range reading, bounded historical novelty statements, source fidelity and preservation of the original text. The user's clarified scope excludes verification, confirmation or criticism of the prose and its dictionary foundation; the research and review briefs implement that boundary.

Do not implement its delivery/exclusion accounting, extra completion machinery or per-passage inspection records. Do not require a fresh grading investigation merely to report that a scholar cited a tradition. These additions would either duplicate work or confuse different evidentiary questions. The compact claim list, usable notes and one substantive final review are the working core.
