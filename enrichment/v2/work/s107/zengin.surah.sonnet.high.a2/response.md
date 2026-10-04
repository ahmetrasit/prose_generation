The surah page for S107 is finished and passes the validator: all 72 records are kept, with no errors or warnings. The preview renders with no placement errors. I checked each cited locator and quotation against the corpus text, and fixed several along the way.

**Blocks by type** (kat: 9 temel, 46 ek, 17 arastirma)
- meal 9; tefsir_dirayet 11; lugat 9; tefsir_rivayet 5; nahiv 5
- yenilik 4; hadis 3; anlam_tarihi 3; kaynak_notu 3; kiraat 3; modern 3; nazm 3
- esbab 2; ayet_ayet 2
- one each of nuzul, belagat, duzeltme, vucuh, kelam, elenen, isari

**Novelty:** all 4 yenilik blocks are `yapitaslari`. The ingredients (fabric, Suhā star, yatim=ghafla, ma'ūn senses) are attested separately, but the image combinations are not found in whole-tafsir searches. `bulunamadi` and `acik` appear only on oncul blocks. Counting oncul blocks by their `klasik_tanik`:
- 14 `acik` (including the early-tafsir antecedents for the water, obedience and Tūr 52:13 links)
- 8 `kismi`

**Counts**
- **oncul:** 22
- **itiraz:** 9. These argue that a base reading may not hold: Maqāyīs on the root's separate uṣūl and on onomatopoeic sounds, ʿAyn on the frozen "kadhaba ʿalaykum" idiom, Abū Ḥayyān on the derivation of mā'ūn, Corpus Coranicum on dīn as a loan, and one meal block on "yanılan".
- **duzeltme:** 1. The base's veyl gloss carries `source:"memory"`, which is not a corpus locator. The errata candidate for the single letter "fa" is a checker false positive and is not logged.

**Meal verdict:** no single best meal. Hayrat is best literal, because its additions are bracketed and it keeps din, ʿan and veyl. For explanation, the best meal depends on the term: DİB and İslamoğlu's deyn note for din, Esed for riya, Y. N. Öztürk for the mā'ūn range, Süleymaniye and Bilmen for "yoksulun yemeği". Shared losses are the Turkish drift of din, namaz and riyâ, the loss of the "yoksulun yemeği" construction, and mā'ūn narrowed to one sense.

**Not done** (full list in `gaps.json`)
- No sahih merit hadith for the surah, and no sahih hadith explaining mā'ūn, were found. The Prophet-attributed mā'ūn reports are ungraded, so they appear only as a source note.
- Ibn al-Jawzī's Zād al-masīr was not read: the locator for 107:1–2 returned NOT FOUND, even though the source lists surahs 103–114.
- The Imāmī Kāfī report is read only as Ṭabāṭabāʾī relays it.
- Several memory-only Western works were not used. Modern scholarship comes from the local Corpus Coranicum segments.

Files are in `/Volumes/aro/projects/prose_generation/enrichment/v2/work/s107/zengin.surah.sonnet.high.a2/`:
- annotations.jsonl
- gaps.json
- preview/surah.md
