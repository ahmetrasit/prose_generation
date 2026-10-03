# Stage 5 — denetim: independent audit

You did not write these blocks. Your job is to find what is wrong or missing before the page is accepted. You
change nothing; you report.

## Inputs
The rendered pages (OUT/surah.md, OUT/S_A.md), the records (annotations.jsonl), the validator report, the evidence
matrix and gaps of stage harita, PACK, the corpus.

## Checks
1. Every block, against its sources: open every locator (`corpus.py get`). Does the source say what the block says?
   Is the attribution right (who said it; transmitted or own view; which work)? Is the grade the source's or the
   corpus's, never inferred? Is iliski honest (thematic hadith not presented as direct)? Is tercih/itiraz used
   correctly? Is the memory rule kept?
2. Novelty: for each yenilik block, search again for antecedents with different spellings and in the works the
   composer did not list in `taranan` (especially the maʿānī/gharīb works, the wujūh books, MAWARDI, WAHIDI-BASIT,
   the *-FULL texts at the word's other occurrences). A found antecedent changes klasik_tanik.
3. Missing: important information a reader building their own tafsir would expect for these ayat and does not
   find (a known disagreement, a famous report, a reading that changes meaning, a hadith on the surah's merit, a
   decisive lexical fact, a base error). Check PACK/errata_candidates.json was handled.
4. Meal blocks: are the losses real (check the Arabic, words.md and the meal text), typed correctly, judged as
   patterns, and is the relay comparison against both poles?
5. Page quality: repetition; blocks at the wrong paragraph; blocks that restate the base; prose over the limit or
   off-register; blocks that adjudicate the base's readings instead of reporting evidence.

## Output (review.json in your stage directory)
{"accepted": true|false, "fixes":[{"id":"S107-TDR-003" or null for a missing block, "problem":…, "evidence":[LOC…],
 "fix": "exact instruction: what to change or the full new record"}], "errata":[{"taban":…, "hata":…, "fix":…,
 "kaynak":[…]}], "novelty_changes":[{"id":…, "from":…, "to":…, "antecedent":LOC}], "notes":…}
accepted is true only if no fix is needed. Final message: counts of fixes by kind and the three most serious.
