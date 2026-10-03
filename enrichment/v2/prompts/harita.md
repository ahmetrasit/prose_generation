# Stage 1 — harita: claim map and evidence matrix

You research; you do not write blocks yet. Your output is the evidence the composing stage will turn into blocks,
so it must be complete, exact and traceable. Work through the steps in order.

## Step 1. Read
Read PACK/base/surah.md completely, then every PACK/base/S_A.md, then for each ayah PACK/ayah/S_A/*.md and the
roots/ files of its bound roots. Do not skim: a claim missed here is missing from the page.

## Step 2. Claim map (claim_map.json)
List every claim of the base that a reader could check or that the literature could confirm, extend or contradict.
One row per claim:
{"cid":"C001", "ayet":"107:1", "where":"surah.md ¶3 | 107_1.md ¶2", "anchor":"exact sentence of surah.md that
 carries it", "anchor_ayet":"exact sentence of the ayah page, if any", "claim":"one line", "kind": one of
 "baglam" (contextual meaning) | "nahiv" | "belagat" | "lugat" (sense, branch) | "imge" (latent lexical image,
 resonance, family image) | "ayet_ayet" | "nazm" | "tarih" | "kelam_fikih" | "sentez" (the base's own synthesis
 joining several of the above), "tags":["base reader tags it rests on, as written"]}
Anchors must be copied exactly from the base (the renderer places blocks after the paragraph that contains them).

## Step 3. Research per ayah (all categories, whether or not the base mentions them)
For each ayah, search and read. Use `corpus.py ayah S:A` for everything tied to the ayah, and `corpus.py search`
over whole books for antecedents elsewhere in the Qur'an. Cover, as the ayah warrants:
1. Transmitted tafsir: TAB (aqwāl with transmitters), DURR, IBNKATHIR, BAGHAWI, early layer (MUQATIL, MUJAHID,
   ABDURRAZZAQ, IBNABIHATIM, YAHYA-SALLAM where present). Who said what; who repeats whom.
2. Analytical tafsir: KASHSHAF, RAZI, BAYDAWI, NASAFI, QURTUBI, IBNATIYYA, ABUHAYYAN, ALUSI, MAWARDI (numbered
   senses without choosing), IBNASHUR, TABRISI, BIQAI (naẓm), and the Turkish ELMALILI and KURANYOLU-TEFSIR;
   allusive QUSHAYRI, SULAMI, TUSTARI, BURSEVI; ABDUH-AMMA; others the corpus lists for the ayah.
3. Occasions and chronology: WAHIDI-ASBAB, SUYUTI-LUBAB, the tafsirs' reports, ITQAN/BURHAN lists, TDVIA surah
   article, CORPUSCORANICUM chronology. Keep Makkī/Madanī apart from occasion reports; record every competing
   attribution with its transmitter and grade information.
4. Hadith: direct prophetic explanation; hadith using the same key expression; strong thematic or counter-scene
   hadith; merit (fazilet) reports. Sahih only for hadis (search with --sahih); note non-sahih reports you saw
   only if they matter for esbab.
5. Readings: QIRAAT-ER, IBNMUJAHID, IBNKHALAWAYH-HUJJA, FARISI-HUJJA, IBNJINNI-MUHTASAB, ABUHAYYAN; what each
   reading does to meaning; canonical vs non-canonical vs Companion reading.
6. Lexicon and sense inventory: PACK dictionary.md and roots/ (PROJE + six lexica), LISAN, ASAS (literal vs
   figurative), FURUQ (near-synonyms), the maʿānī/gharīb works (MAJAZ, FARRA, ZAJJAJ, AKHFASH, IBNQUTAYBA-GHARIB,
   IBNQUTAYBA-MUSHKIL, NAHHAS, SAMIN-DURR, SAMIN-UMDA, WAHIDI-BASIT), and the wujūh books (MUQATIL-WUJUH,
   DAMGHANI, IBNJAWZI-NUZHA) with PACK usage.md.
7. Grammar and rhetoric that bear on meaning (ABUHAYYAN, SAMIN-DURR, KASHSHAF, IBNASHUR, JURJANI-*).
8. Qur'an by Qur'an: passages that explain, extend or contrast (TABATABAI is strong here; PACK usage.md).
9. Semantic history (pre-Qur'anic → Qur'anic → later Arabic → Turkish) and historical setting (IBNHISHAM, AZRAQI,
   KALBI-ASNAM, poetry: MUALLAQAT, MUFADDALIYYAT, ASMAIYYAT, HAMASA).
10. Modern scholarship: local where available; licensed Western works only as memory pointers (access hafiza).

## Step 4. Antecedents and counter-evidence for the base's own findings
For every claim of kind imge or sentez: search for antecedents (a source already stating the image or part of it)
in this order: the maʿānī/gharīb works and WAHIDI-BASIT; the wujūh books; MAWARDI and IBNJAWZI-ZAD enumerations;
lexica that cite ayat under a branch (LISAN, MUFRADAT, SAMIN-UMDA, ASAS); KASHSHAF and JURJANI for recognised
majāz; QUSHAYRI/SULAMI/BURSEVI; BINTSHATI, QUTB-ZILAL, IBNASHUR, ELMALILI; then the full tafsir texts (*-FULL)
across the Qur'an, especially at the other occurrences listed in usage.md. Then search for counter-evidence:
grammar or a reading that blocks the activation, a near-synonym distinction (FURUQ), Maqāyīs positing separate
uṣūl, a loan or homonymous root. Record what you searched even when nothing was found.

## Step 5. Evidence matrix (evidence_matrix.json)
One row per piece of evidence you will want on the page:
{"eid":"E001", "cid":"C003 or null (ayah-level evidence not tied to a base claim)", "ayet":"107:2",
 "tur": a schema tur value, "islev": a schema islev value, "iliski": a schema iliski value,
 "kaynak":["LOC", …], "alim":"named authority if any", "ozet":"what the source says, 1–3 lines, in English or
 Turkish", "alinti":"the decisive words verbatim from the source (short)", "tekrar":["later works repeating it
 unchanged"], "derece": for hadis/esbab, "derece_veren":…, "tarihsellik":…, "kiraat_turu":…, "sozluk":[…],
 "klasik_tanik"/"taranan"/"tarama": for antecedent rows, "not":"caveats: attribution doubts, edition, OCR"}
Deduplicate: a report repeated unchanged in later works is one row with `tekrar`, not several rows. A later work
that changes, grades or narrows it gets its own row.

## Step 6. Gaps (gaps.json)
{"missing_sources":[…corpus IDs you needed that are absent or empty…], "not_found":[…searches with no result that
matter…], "unresolved":[…]}

## Finish
Write claim_map.json, evidence_matrix.json, gaps.json into your stage directory. Final message: counts (claims by
kind, evidence rows by tur), the five most important antecedents or counter-evidence found, and the gaps.
