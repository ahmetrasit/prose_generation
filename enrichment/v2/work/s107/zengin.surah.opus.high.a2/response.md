The surah page for S107 is finished. All 58 records in `annotations.jsonl` pass the validator, with no records dropped and no warnings. The preview rendered with 0 placement errors, and `gaps.json` is written.

**Blocks by type (58):** 11 analytical tafsir, 8 lexicon, 6 transmitted tafsir, 6 Qur'an-by-Qur'an, 6 meal, 4 readings, 3 hadith (all sahih: Muslim 1412 and 7476, Bukhārī 6005), 3 naẓm, 3 novelty audit, 2 grammar. There is one block each for chronology, occasion reports, source note, modern scholarship, semantic history and rhetoric.

**By layer:** 9 core (temel), 43 extended (ek), 6 research (arastirma).

**Novelty (klasik_tanik):**
- **Fully attested (açık):** 9. Examples: Zamakhsharī on the two-sided verb form of yurāʾūn, the ʿan/fī distinction, Mūqatil/Farrāʾ/Māwardī on māʿūn as water, and Māwardī/Qurṭubī tying 107:3 to 36:47.
- **Partly attested (kısmî):** 11. Examples: Biqāʿī's analysis of the k-dh-b root (the "lying" she-camel, the wild animal that stops), al-Rāghib deriving ḥaḍḍ from ḥaḍīḍ, ṣalāt derived from straightening wood by fire, māʿūn as submission, and Ibn Fāris putting water, a right and a dwelling under one root.
- **Building blocks only (yapıtaşları):** 1, the orphan's name meaning heedlessness linked to sāhūn.
- **Not found (bulunamadı):** 2, the painted-cloth image, and the Suhā star with the opening/closing ring of the root r-ʾ-y. The ring was checked only in the commentaries on this surah, not the whole corpus; the block says so.

**Antecedents, counter-evidence and corrections:** 20 blocks name an earlier source for the commentary's points. Two blocks argue against its readings, both from Ibn Fāris: ḥaḍḍ and ḥaḍīḍ are separate roots, and fire and worship are separate roots in ṣ-l-y. There are no corrections.

**Meal verdict:** Hayrat is the best literal translation: it keeps fa and ʿan, marks its glosses in brackets and keeps the word māʿūn. Ateş is the best explanatory translation: all additions are bracketed, though he drops the fa of 107:4. Only Süleymaniye keeps the poor man's right in "ṭaʿām al-miskīn". The losses shared across the panel are:
- dīn losing its sense of judgment and reckoning;
- the poor man's right in "ṭaʿām al-miskīn";
- māʿūn losing its sense of borrowed household utensils.

**What I could not do or changed:**
- **Merit report:** the only merit report for this surah is Ubayy's, which Zarkashī (following Ibn al-Ṣalāḥ) calls fabricated. The validator dropped my first version, which was filed as a merit block outside the hadith type, so it now stands as a source note together with the surah's names.
- **TDV citation:** TDV renders 107:6–7 as one text, which the corpus files under `MEAL-TDV:107:6`. I corrected the citation to that.
- **Missing texts:** Ṭabrisī has nothing for this surah. Birkeland and Paret are known only through Corpus Coranicum and the TDV encyclopedia.
- **No sahih Prophetic explanation of māʿūn:** none was found. Ibn Masʿūd's report (Abū Dāwūd 1657) has no grader in the corpus, so it is presented as his own statement.
- **Flagged base issues:** the error checker's flag on "فَ" in ¶10 looks like a false positive, since it is the first letter of فَذَٰلِكَ in 107:2. The base's "veyl" in ¶30, which it sources to memory, is now backed by lexicon sources in a separate block. Both are recorded in `gaps.json`.

Files are in `enrichment/v2/work/s107/zengin.surah.opus.high.a2`:
- annotations.jsonl
- gaps.json
- preview/surah.md
