# Bible image author: S103 sec4

You are the Sol agent at max effort. Verify and write the Bible enrichment for ONE image section.
Your call directory is /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap-images.sol.max.s103-20261009/sec4. Workspace: /Volumes/aro/projects/prose_generation.
Your permitted global paragraph numbers are 13, 14, 15. Keep these numbers; never renumber locally.
You have 280 distinct discovery connections. Account for every one, including weaker and unavailable ones.

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
  WLC uses ketiv; variants are separate. Search normalizes pointing/accents; hebrew.py supplies lemmas and roots.
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

    cat /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap-images.sol.max.s103-20261009/sec4/FILE
    sed -n '1,40p' /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap-images.sol.max.s103-20261009/sec4/FILE
    sed -n '/BC-070cebfd3237a3852597/p' /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap-images.sol.max.s103-20261009/sec4/candidates.jsonl
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext sources
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext ayah 103:1 --chars 1500
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext search 'Hebrew or Greek words' --src WLC --n 10 --chars 300
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext get WLC:Gen.1.1 SBLGNT:Matt.1.1 --chars 1500
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/hebrew.py root HEBREWROOT
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/hebrew.py root HEBREWROOT --from 400
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/hebrew.py cognates 'ARABIC ROOT LETTERS'
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/hebrew.py word WLC:Gen.1.1
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/image_enrich.py check --dir /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap-images.sol.max.s103-20261009/sec4

Replace the example ayah, words, exact candidate ID and locators as appropriate. Search Greek with --src SBLGNT. Open batches of
about 5–10 verses to avoid output truncation. Reopen truncated passages using --from and --chars. A search
snippet is not opened evidence. Each get lookup, including neighbours, needs a verdict in the final ledger.

Write files with functions.exec using EXACTLY this wrapper; PATCH must be one JSON string literal with escapes:

    text(await tools.apply_patch("PATCH"));

The patch may add/update only annotations.jsonl, verdicts.jsonl, gaps.json, root_verdicts.jsonl and notes.md in
your call directory.
Do not use template strings, variables, other JavaScript, shell writes or a script to generate judgments.
Reading your own generated preview/surah.md is also allowed for checking placement; other sections remain
outside your writing assignment. A native clock read is operational metadata, never research evidence.
Listing only your own call directory with ls (optionally -l, -a, -la or -al) is allowed to check deliverables.
The wrapper restriction enables a mechanical audit of native tool use. It does not limit your reasoning.

## Deliver and check

Write annotations.jsonl, verdicts.jsonl, gaps.json and root_verdicts.jsonl following rules.md/schema.md (the
Semitic root table of your section is at the end of this prompt; rules.md says how to use it and record it). Every discovered connection
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

# Semitic root table of this page

The Arabic roots this page cites, with the Hebrew and Biblical Aramaic roots that correspond to them by regular sound correspondences and exist in the lexicon (hebrew.py). Each root needs one line in root_verdicts.jsonl (Step 3b).

== Arabic root ء ن س: 4 Hebrew/Aramaic correspondences found in the lexicon (regular sound correspondences; a candidate, not proof)
* Hebrew אנש (ء→א ن→נ س→ש): BDB cites an Arabic cognate; 1275 WLC occurrences; `hebrew.py root אנש` lists them
  - אֱנוֹשׁ (ʾĕnôš) N 'man' [H582; Hebrew; 42 WLC occurrences] Strong: properly, a mortal (and thus differing from the more dignified 120); hence, a man in general (singly or collectively)
  - אָנַשׁ (ʾānaš) V 'be weak' [H605; Hebrew; 9 WLC occurrences] Strong: to be frail, feeble, or (figuratively) melancholy
  - אֵשׁ (ʾēš) N 'fire' [H784; Hebrew; 376 WLC occurrences] Strong: fire (literally or figuratively)
  - אֶשְׁדָּת (ʾešdāt) N 'fire' [H799; Hebrew; 1 WLC occurrence] Strong: a fire-law
  - אִשֶּׁה (ʾiššeh) N 'an offering made by fire' [H801; Hebrew; 65 WLC occurrences] Strong: properly, a burnt-offering; but occasionally of any sacrifice
  - אִשָּׁה (ʾiššâ) N 'woman' [H802; Hebrew; 781 WLC occurrences] Strong: a woman
  - אֶשָּׁה (ʾeššâ) N 'from their fire' [H800; Hebrew; 1 WLC occurrence] Strong: fire
* Aramaic אנש (ء→א ن→נ س→ש): sound correspondence only (unverified); 26 WLC occurrences; `hebrew.py root אנש` lists them
  - אֱנָשׁ (ʾĕnāš) N 'man' [H606; Aramaic; 25 WLC occurrences] Strong: a man
  - נְשִׁין (nĕšîn) N 'wives' [H5389; Aramaic; 1 WLC occurrence]
* Hebrew אנס (ء→א ن→נ س→ס): sound correspondence only (unverified); 1 WLC occurrences; `hebrew.py root אנס` lists them
  - אָנַס (ʾānas) V 'compel' [H597; Hebrew; 1 WLC occurrence] Strong: to insist
* Aramaic אנס (ء→א ن→נ س→ס): sound correspondence only (unverified); 1 WLC occurrences; `hebrew.py root אנס` lists them
  - אֲנַס (ʾănas) V 'oppress' [H598; Aramaic; 1 WLC occurrence] Strong: figuratively, to distress

== Arabic root ص ب ر: 1 Hebrew/Aramaic correspondence found in the lexicon (regular sound correspondences; a candidate, not proof)
* Hebrew צבר (ص→צ ب→ב ر→ר): sound correspondence only (unverified); 8 WLC occurrences; `hebrew.py root צבר` lists them
  - צִבּוּר (ṣibbûr) N 'heap' [H6652; Hebrew; 1 WLC occurrence] Strong: a pile
  - צָבַר (ṣābar) V 'heap up' [H6651; Hebrew; 7 WLC occurrences] Strong: to aggregate

== Arabic root ع ص ر: 1 Hebrew/Aramaic correspondence found in the lexicon (regular sound correspondences; a candidate, not proof)
* Hebrew עצר (ع→ע ص→צ ر→ר): sound correspondence only (unverified); 63 WLC occurrences; `hebrew.py root עצר` lists them
  - מַעְצוֹר (maʿṣôr) N 'restraint' [H4622; Hebrew; 1 WLC occurrence] Strong: objectively, a hindrance
  - מַעְצָר (maʿṣār) N 'restraint' [H4623; Hebrew; 1 WLC occurrence] Strong: subjectively, control
  - עֶ֫צֶר (ʿeṣer) N 'restraint' [H6114; Hebrew; 1 WLC occurrence] Strong: restraint
  - עָצַר (ʿāṣar) V 'restrain' [H6113; Hebrew; 46 WLC occurrences] Strong: to inclose; by analogy, to hold back; also to maintain, rule, assemble
  - עֹ֫צֶר (ʿōṣer) N 'restraint' [H6115; Hebrew; 3 WLC occurrences] Strong: closure; also constraint
  - עֲצָרָה (ʿăṣārâ) N 'assembly' [H6116; Hebrew; 11 WLC occurrences] Strong: an assembly, especially on a festival or holiday

