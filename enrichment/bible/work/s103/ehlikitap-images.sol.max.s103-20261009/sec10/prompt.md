# Bible image author: S103 sec10

You are the Sol agent at max effort. Verify and write the Bible enrichment for ONE image section.
Your call directory is /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap-images.sol.max.s103-20261009/sec10. Workspace: /Volumes/aro/projects/prose_generation.
Your permitted global paragraph numbers are 29, 30, 31. Keep these numbers; never renumber locally.
You have 264 distinct discovery connections. Account for every one, including weaker and unavailable ones.

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

    cat /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap-images.sol.max.s103-20261009/sec10/FILE
    sed -n '1,40p' /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap-images.sol.max.s103-20261009/sec10/FILE
    sed -n '/BC-070cebfd3237a3852597/p' /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap-images.sol.max.s103-20261009/sec10/candidates.jsonl
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext sources
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext ayah 103:1 --chars 1500
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext search 'Hebrew or Greek words' --src WLC --n 10 --chars 300
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/corpus.py --intertext get WLC:Gen.1.1 SBLGNT:Matt.1.1 --chars 1500
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/hebrew.py root HEBREWROOT
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/hebrew.py root HEBREWROOT --from 400
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/hebrew.py cognates 'ARABIC ROOT LETTERS'
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/hebrew.py word WLC:Gen.1.1
    python3 /Volumes/aro/projects/prose_generation/enrichment/bible/image_enrich.py check --dir /Volumes/aro/projects/prose_generation/enrichment/bible/work/s103/ehlikitap-images.sol.max.s103-20261009/sec10

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

== Arabic root ء م ن: 2 Hebrew/Aramaic correspondences found in the lexicon (regular sound correspondences; a candidate, not proof)
* Hebrew אמנ (ء→א م→מ ن→נ): sound correspondence only (unverified); 343 WLC occurrences; `hebrew.py root אמנ` lists them
  - אָמוֹן (ʾāmôn) N 'artificer' [H527; Hebrew; 1 WLC occurrence] Strong: a throng of people
  - אָמוֹן (ʾāmôn) N 'artificer' [H525; Hebrew; 1 WLC occurrence] Strong: skilled, i.e. an architect
  - אֱמוּנָה (ʾĕmûnâ) N 'firmness' [H530; Hebrew; 49 WLC occurrences] Strong: literally firmness; figuratively security; morally fidelity
  - אֵמֻן (ʾēmun) N 'trusting' [H529; Hebrew; 5 WLC occurrences] Strong: established, i.e. (figuratively) trusty; also (abstractly) trustworthiness
  - אָמֵן (ʾāmēn) D 'verily' [H543; Hebrew; 30 WLC occurrences] Strong: sure; abstract, faithfulness; adverb, truly
  - אָמַן (ʾāman) V 'confirm' [H539; Hebrew; 108 WLC occurrences] Strong: properly, to build up or support; to foster as a parent or nurse; figuratively to render (or be) firm or faithful, to trust or believe, to be permanent or quiet; morally to be true or certain;
  - אָמָּן (ʾāmmān) N 'master-workman' [H542; Hebrew; 1 WLC occurrence] Strong: an expert
  - אֹ֫מֶן (ʾōmen) N 'faithfulness' [H544; Hebrew; 1 WLC occurrence] Strong: verity
  - אֲמָנָה (ʾămānâ) N 'faith' [H548; Hebrew; 2 WLC occurrences] Strong: something fixed, i.e. a covenant. an allowance
  - אֹמְנָה (ʾōmĕnâ) N 'confirm' [H547; Hebrew; 1 WLC occurrence] Strong: a column
  - אׇמְנָה (ʾomnâ) D 'verily' [H546; Hebrew; 2 WLC occurrences] Strong: adverb, surely
  - אׇמְנָה (ʾomnâ) N 'bringing up' [H545; Hebrew; 1 WLC occurrence] Strong: tutelage
  - אֻמְנָם (ʾumnām) D 'verily' [H552; Hebrew; 5 WLC occurrences]
  - אׇמְנָם (ʾomnām) D 'verily' [H551; Hebrew; 9 WLC occurrences] Strong: verily
  - אֱמֶת (ʾĕmet) N 'firmness' [H571; Hebrew; 127 WLC occurrences] Strong: stability; (figuratively) certainty, truth, trustworthiness
* Aramaic אמנ (ء→א م→מ ن→נ): sound correspondence only (unverified); 3 WLC occurrences; `hebrew.py root אמנ` lists them
  - אֲמַן (ʾăman) V 'trust' [H540; Aramaic; 3 WLC occurrences]

== Arabic root ح ق ق: 1 Hebrew/Aramaic correspondence found in the lexicon (regular sound correspondences; a candidate, not proof)
* Hebrew חקק (ح→ח ق→ק ق→ק): sound correspondence only (unverified); 254 WLC occurrences; `hebrew.py root חקק` lists them
  - חֹק (ḥōq) N 'something prescribed' [H2706; Hebrew; 127 WLC occurrences] Strong: an enactment; hence, an appointment (of time, space, quantity, labor or usage)
  - חֻקָּה (ḥuqqâ) N 'something prescribed' [H2708; Hebrew; 105 WLC occurrences]
  - חֵקֶק (ḥēqeq) N 'something prescribed' [H2711; Hebrew; 2 WLC occurrences] Strong: an enactment, a resolution
  - חָקַק (ḥāqaq) V 'cut in' [H2710; Hebrew; 19 WLC occurrences] Strong: properly, to hack, i.e. engrave (Judges 5:14, to be a scribe simply); by implication, to enact (laws being cut in stone or metal tablets in primitive times) or (gen.) prescribe
  - חֻקֹֿק (ḥuqōq) Np 'Hukkok' [H2712a; Hebrew; 1 WLC occurrence] Strong: Chukkok or Chukok, a place in Palestine

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

== Arabic root و ص ي: 0 Hebrew/Aramaic correspondences found in the lexicon (regular sound correspondences; a candidate, not proof)
  no Hebrew or Aramaic root with these corresponding consonants is in the lexicon

