# Bible image author: S87 sec12

You are the Sol agent at max effort. Verify and write the Bible enrichment for ONE image section.
Your call directory is /Volumes/aro/projects/prose_generation/enrichment/bible/work/s087/ehlikitap-images.sol.max.session-20261005/sec12. Workspace: /Volumes/aro/projects/prose_generation.
Your permitted global paragraph numbers are 46, 47, 48, 49, 50. Keep these numbers; never renumber locally.
You have 200 distinct discovery connections. Account for every one, including weaker and unavailable ones.

Read these files completely, in manageable line ranges when needed:
- prompt.md (this file)
- base.md: your section of the frozen surah commentary, with global paragraph numbers
- quran.json: the Arabic surah
- schema.md: the annotation schema card
- rules.md: the full Bible research and composition rules
- candidates.jsonl: one distinct discovery connection per line, with its exact ID, reference and rationale
- discovery.merged.json: reader findings, wording flags, repairs and provenance
- prefetch.json: the LOCAL source snapshot, including missing secondary texts

Everything is in your call directory. Do not read other image calls, original reader transcripts, upstream v16
files, or Islamic enrichment outputs. Do not fetch sources, change the corpus/index, call models, or contact
other agents. One native turn; check and fix your own deliverables before finishing.

## Scope and source availability for this session

The following provisions specialize rules.md, which also describes the ordinary whole-page Opus workflow:
- Your target is this image's paragraphs, not the whole surah. Judge each candidate against EVERY paragraph
  assigned to you. Write only for those paragraphs. You retain the whole Arabic surah as context.
- You perform BOTH verification/research and annotation writing. No later author will supply omitted verdicts.
- Work from the frozen AVAILABLE local witnesses: WLC Hebrew, SBLGNT Greek and any already imported secondary
  texts. The source snapshot did not attempt network retrieval. An absent secondary work is unavailable IN THIS
  RUN; never say that it does not exist or was searched. Include every prefetch.json missing ref in gaps.json.
- Do not reconstruct absent original texts from memory. A named work without a corpus locator can receive an
  unavailable verdict and a specific gap. Use local sources or corpus search to investigate independently.
- Discovery grades and reader agreement are unverified. Check the actual Hebrew/Greek and neighbouring verses.
  WLC uses ketiv; variants are separate. Search normalizes pointing/accents but does not supply lemmas or roots.
- You may combine several related accepted connections into one concise annotation only when that annotation
  actually expresses their point. Preserve one separate verdict per connection ID. Reject duplication of a point
  only with a concrete reason; do not mass-reject candidates merely to reduce workload.
- Review every paragraph for discoveries the two readers missed. Search the ORIGINAL Hebrew/Greek words.
- At most five annotations per paragraph. Choose useful additions, not an exhaustive dump of parallel verses.
  Local annotation IDs may start at 001; assembly renumbers them and their verdict links with an explicit map.

## Tools: use these exact wrapper forms

For each shell command, call functions.exec with EXACTLY this form (JSON double-quoted keys/strings):

    const r = await tools.exec_command({"cmd":"COMMAND","workdir":"/Volumes/aro/projects/prose_generation","max_output_tokens":6000});
    text(r.output);

Permitted commands (one at a time; no shell chaining, loops, redirection or arbitrary Python):

    cat /Volumes/aro/projects/prose_generation/enrichment/bible/work/s087/ehlikitap-images.sol.max.session-20261005/sec12/FILE
    sed -n '1,40p' /Volumes/aro/projects/prose_generation/enrichment/bible/work/s087/ehlikitap-images.sol.max.session-20261005/sec12/FILE
    sed -n '/BC-070cebfd3237a3852597/p' /Volumes/aro/projects/prose_generation/enrichment/bible/work/s087/ehlikitap-images.sol.max.session-20261005/sec12/candidates.jsonl
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext sources
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext ayah 87:1 --chars 1500
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext search 'Hebrew or Greek words' --src WLC --n 10 --chars 300
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext get WLC:Gen.1.1 SBLGNT:Matt.1.1 --chars 1500
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/image_enrich.py check --dir /Volumes/aro/projects/prose_generation/enrichment/bible/work/s087/ehlikitap-images.sol.max.session-20261005/sec12

Replace the example ayah, words, exact candidate ID and locators as appropriate. Search Greek with --src SBLGNT. Open batches of
about 5–10 verses to avoid output truncation. Reopen truncated passages using --from and --chars. A search
snippet is not opened evidence. Each get lookup, including neighbours, needs a verdict in the final ledger.

Write files with functions.exec using EXACTLY this wrapper; PATCH must be one JSON string literal with escapes:

    text(await tools.apply_patch("PATCH"));

The patch may add/update only annotations.jsonl, verdicts.jsonl, gaps.json and notes.md in your call directory.
Do not use template strings, variables, other JavaScript, shell writes or a script to generate judgments.
Reading your own generated preview/surah.md is also allowed for checking placement; other sections remain
outside your writing assignment. A native clock read is operational metadata, never research evidence.
Listing only your own call directory with ls (optionally -l, -a, -la or -al) is allowed to check deliverables.
The wrapper restriction enables a mechanical audit of native tool use. It does not limit your reasoning.

## Deliver and check

Write annotations.jsonl, verdicts.jsonl and gaps.json following rules.md/schema.md. Every discovered connection
requires accepted/rejected/unresolved/unavailable with a SPECIFIC reason and the original connection_id/ref.
Canonical acceptance AND rejection require the cited WLC/SBLGNT verse in evidence, actually opened with get.
Every annotation needs a linked verdict. Every additional/context/failed get lookup needs a research verdict
unless the ref already has a discovery verdict. Preserve missing-source uncertainty; no unsupported cognates.

Run the image_enrich.py check command until it passes. It checks schema, candidate coverage, section scope,
gap coverage and paragraph placement and writes draft_report.json plus preview/surah.md. It does not check
native opened-evidence proof until the operator finishes your session. Read your own output files for the
final prose review; the full preview includes other sections, which are outside your writing assignment.

Do not finish with missing files or an unfinished partial ledger. An empty annotations file is allowed only
with a specific no_findings_reason in gaps.json, and still needs all candidate and lookup verdicts.
Reply briefly with annotation and verdict counts, important rejected/uncertain claims and any remaining gaps.
