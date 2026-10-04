# zengin: one page's records (research, meal review and composition in one call)

You produce every enrichment block for ONE page, the target in the job header: the surah page or one ayah page. You
write records, not Markdown: afterwards a script checks each record, drops any record that fails a rule (it is not
sent back to you), inserts the rest into the frozen base after the paragraph each names, and builds the source
registry. Work through the steps in order. Notes you make along the way are yours (keep them in your call
directory if useful); only annotations.jsonl and gaps.json are read.

## Scope by target
- Ayah page (target S:A): everything an advanced reader needs about that ayah: its tafsir, readings, hadith,
  lexicon and sense inventory, grammar and rhetoric, occasion reports tied to it, the word-by-word meal review, and
  antecedents and counter-evidence for the claims of the ayah commentary. Every record's `ayet` includes the target
  ayah (a range such as 107:4-7 is right when the point concerns the group). Anchor to the paragraphs of
  PACK/numbered/S_A.md; a block about a v16 addition (`<!-- v16:augment … para=n … -->`) anchors to its ¶n, and its
  capa may quote the addition.
- Surah page (target surah): what belongs to the surah as a whole — names and merit, chronology and Makkī/Madanī,
  occasion reports for the whole surah, structure and naẓm, the surah's place among its neighbours, antecedents and
  counter-evidence for the claims of the surah commentary, and the meal verdict with the losses shared across the
  surah. Each ayah has its own page, written in its own call, which carries the per-ayah material (readings, the
  word-by-word meal review, hadith on a single ayah, the lexicon of single words): on the surah page give such
  detail only where a paragraph of the surah commentary is about it, and then only its most important point.
  Anchor to the paragraphs of PACK/numbered/surah.md.
- Every block sits right after the base paragraph it speaks to; there is no section at the end of the page.

## Step 1. Read
Read the target's numbered base page completely, once, and keep your own notes (paragraph numbers and claims) in
your call directory; do not read it again. Do not skim: a claim missed here is missing from the page.
- Ayah page: then PACK/ayah/S_A/*.md and the roots/ files of the ayah's bound roots.
- Surah page: then the meal files of all ayat (PACK/ayah/*/meals.md, for the verdict and the shared losses), and
  the other per-ayah files and roots/ only for the paragraphs of the surah commentary that discuss them; the ayah
  pages (PACK/numbered/S_A.md) only where you need to orient yourself.

## Step 2. Claims of the base
List for yourself every claim of the target page that a reader could check or that the literature could confirm,
extend or contradict, each with its paragraph number [¶n] (the `paragraf` of the blocks about it) and its kind: baglam (contextual meaning) | nahiv | belagat | lugat (sense, branch) | imge (latent lexical
image, resonance, family image) | ayet_ayet | nazm | tarih | kelam_fikih | sentez (the base's own synthesis joining
several of the above).

## Step 3. Research (all categories, whether or not the base mentions them)
Search and read. Use `corpus.py ayah S:A` for everything tied to an ayah, and `corpus.py search` over whole books
for antecedents elsewhere in the Qur'an. Cover, as the ayah or surah warrants:
1. Transmitted tafsir: TAB (aqwāl with transmitters), DURR, IBNKATHIR, BAGHAWI, early layer (MUQATIL, MUJAHID,
   ABDURRAZZAQ, IBNABIHATIM, YAHYA-SALLAM where present). Who said what; who repeats whom. Make sure the
   well-known direct explanations of each key word are on the page that carries that ayah's material (its ayah
   page; the surah page only when a paragraph of the surah commentary is about it), Prophetic or Companion, each
   with its grade handled by rule 4 of the shared core.
2. Analytical tafsir: KASHSHAF, RAZI, BAYDAWI, NASAFI, QURTUBI, IBNATIYYA, ABUHAYYAN, ALUSI, MAWARDI (numbered
   senses without choosing), IBNASHUR, TABRISI, BIQAI (naẓm), and the Turkish ELMALILI and KURANYOLU-TEFSIR;
   allusive QUSHAYRI, SULAMI, TUSTARI, BURSEVI (when the corpus has an ishārī reading for the page, include the
  one that adds most); ABDUH-AMMA; others the corpus lists for the ayah.
3. Occasions and chronology: WAHIDI-ASBAB, SUYUTI-LUBAB, the tafsirs' reports, ITQAN/BURHAN lists, TDVIA surah
   article, CORPUSCORANICUM chronology. Keep Makkī/Madanī apart from occasion reports; record every competing
   attribution with its transmitter and grade information.
4. Hadith: on an ayah page, a direct prophetic explanation of the ayah's words, when one exists, then at most two
   thematic or counter-scene hadith, the ones that add most (a well-known hadith the reader expects adds little);
   on the surah page, merit (fazilet) reports and hadith a paragraph of the surah commentary is about. Sahih only
   for hadis (search with --sahih). A non-sahih report follows rule 4 of the shared core: esbab if it is an occasion
   report, the Companion's or Successor's own statement if a sound version exists, otherwise only as a warning in a
   kaynak_notu block with its grade and grader; never as hadis, never with islev:fazilet.
5. Readings: QIRAAT-ER, IBNMUJAHID, IBNKHALAWAYH-HUJJA, FARISI-HUJJA, IBNJINNI-MUHTASAB, ABUHAYYAN; what each
   reading does to meaning; canonical vs non-canonical vs Companion reading.
6. Lexicon and sense inventory: PACK dictionary.md and roots/ (PROJE + six lexica), LISAN, ASAS (literal vs
   figurative), FURUQ (near-synonyms), the maʿānī/gharīb works (MAJAZ, FARRA, ZAJJAJ, AKHFASH, IBNQUTAYBA-GHARIB,
   IBNQUTAYBA-MUSHKIL, NAHHAS, SAMIN-DURR, SAMIN-UMDA, WAHIDI-BASIT), and the wujūh books (MUQATIL-WUJUH,
   DAMGHANI, IBNJAWZI-NUZHA) with PACK usage.md.
7. Grammar and rhetoric that bear on meaning (ABUHAYYAN, SAMIN-DURR, KASHSHAF, IBNASHUR, JURJANI-*).
8. Qur'an by Qur'an: passages that explain, extend or contrast (TABATABAI is strong here; PACK usage.md).
9. Semantic history (pre-Qur'anic → Qur'anic → later Arabic → Turkish) and historical setting (IBNHISHAM, AZRAQI,
   KALBI-ASNAM, poetry: MUALLAQAT, MUFADDALIYYAT, ASMAIYYAT, HAMASA). PACK/ayah/S_A/turkish.md holds the Turkish
   dictionary entries (NISANYAN, TDK, KUBBEALTI) of the meals' key words: where a word's Turkish sense has drifted
   from the Arabic (din, riya, namaz, miskin …), write an anlam_tarihi block; the reader of this page is Turkish.
10. Modern scholarship: local where available; licensed Western works only as memory pointers (access hafiza).
Deduplicate as you go: a report repeated unchanged in later works is one point with `tekrar`; a later work that
changes, grades or narrows it is its own point.

## Step 4. Antecedents and counter-evidence for the base's own findings
For every claim of kind imge or sentez: search for antecedents (a source already stating the image or part of it)
in this order: the maʿānī/gharīb works and WAHIDI-BASIT; the wujūh books; MAWARDI and IBNJAWZI-ZAD enumerations;
lexica that cite ayat under a branch (LISAN, MUFRADAT, SAMIN-UMDA, ASAS); KASHSHAF and JURJANI for recognised
majāz; QUSHAYRI/SULAMI/BURSEVI; BINTSHATI, QUTB-ZILAL, IBNASHUR, ELMALILI; then the full tafsir texts (*-FULL)
across the Qur'an, especially at the other occurrences listed in usage.md. Then search for counter-evidence:
grammar or a reading that blocks the activation, a near-synonym distinction (FURUQ), Maqāyīs positing separate
uṣūl, a loan or homonymous root. Record what you searched even when nothing was found (`taranan`, `tarama`).

## Step 5. Meal review
Two questions decide the reader's page: which meal conveys the meaning best (per strategy), and what the meals lose
in common. Inputs: PACK/ayah/S_A/words.md (every word's morphemes and the elements a faithful translation must
carry: prepositions, attached pronouns, number, definiteness, voice, emphasis, conjunctions); PACK/ayah/S_A/meals.md
(the 16-meal panel, the relay pair Asad EN → Esed TR, Arberry as a literal English control, the reference set);
PACK dictionary.md, usage.md, roots/; `corpus.py get MEAL-X:S:A` for any meal at any ayah of the Qur'an.
Panel lineage: MEAL-DIB, MEAL-TDV and MEAL-KURANYOLU share one lineage (diyanet): their agreement counts as one
witness. MEAL-ESED is translated from Asad's English (relay ASAD-EN), not from the Arabic.
Ayah page: steps 1–4 below, word by word. Surah page: no word-by-word alignment (the ayah pages carry it); from the
meal files of all ayat, find the losses shared across the surah (step 3) and give the surah verdict (step 4).
1. Expected elements: for each content word, what must be carried — the concept (from the dictionary and the
   tafsir range) and each grammatical element. Mark what Turkish cannot carry naturally (e.g. the Arabic definite
   article) as imposed by Turkish: no translator is blamed for it.
2. Alignment: for every panel meal, the Turkish words that render each Arabic word (or nothing), and for each
   expected element: kept | dropped | substituted | added (and whether an addition is marked by brackets or
   parentheses; keep the translator's brackets exactly). Merged verse groups: align the group text to the group's
   words and say so.
3. Losses and gains, typed with the schema `kayip` values:
   - kelime: a different concept (e.g. ṣudūr → "kalp": ṣadr is the chest, qalb the heart; 22:46 "al-qulūb allatī
     fī ṣ-ṣudūr" is the test where a translator who maps ṣadr to kalp must write "kalplerdeki kalpler" or change the
     verse — check it with `corpus.py get MEAL-X:22:46` for any term where this pattern matters);
   - eleman: a preposition, pronoun ("their" in -leri), number, emphasis, conjunction or voice that natural Turkish
     could have kept and the meal dropped (kalplerde vs kalplerinde: the first drops "their");
   - aralik: several live senses narrowed to one (from the tafsir range and the dictionary branches);
   - ekleme: the translator's own words presented as text (unmarked); marked additions are not a loss;
   - kayma: a loanword whose Turkish sense has shifted (namaz, din, ibadet, âlem) — the Turkish-history evidence
     (NISANYAN, KUBBEALTI, TDK, TDVIA term articles; PACK/ayah/S_A/turkish.md) goes to anlam_tarihi; here only its effect on the meal;
   - isaretleme: brackets, italics or notes changed so an addition no longer looks like one;
   - aktarma: relay drift — for MEAL-ESED compare with ASAD-EN (kiyas:ara_metin) as well as with the Arabic
     (kiyas:arapca); a relay step can lose against one pole and gain against the other (yon:kayip / yon:kazanc);
     likewise MEAL-TEFHIM (from Mawdudi's Urdu) and MEAL-FIZILAL (from Quṭb's paraphrase) when used.
   Judge patterns, not slips: for each translator and each key term, check its renderings across the term's other
   occurrences (usage.md lists them) before calling a choice a habit. Separate an outright error from a defensible
   narrowing, with the ground (Arabic, dictionary, early authorities). Use ARBERRY to tell Turkish-specific loss
   from loss any translation would suffer.
4. Verdict: never one best meal overall. Name the best literal and the best explanatory meal and, where they
   differ, the best per criterion (primary sense, range kept, additions marked, Turkish drift), each with its
   reason. Ayah page: the verdict for that ayah. Surah page: the verdict for the surah and the losses shared across
   its ayat, from the meal files of all ayat; do not repeat the word-by-word alignment there (the ayah pages carry
   it).

## Step 6. Compose the records
What a good page has:
- Ayah page: the ayah's anchor meaning (dayanak) from the received tafsir; the real disagreements (ihtilaf, with
  who holds what); the sense range (anlam_alani) where the tradition is plural; occasion reports tied to it, with
  grades and historicity; sahih hadith within the limit of step 3; readings that change meaning; the lexical and
  wujūh evidence behind the commentary's words; grammar and rhetoric where they decide something.
- Surah page: the surah-level material of the scope, and for each paragraph of the surah commentary the evidence
  it calls for; per-ayah detail only as the scope allows.
- For every claim of the base of kind imge or sentez: when an antecedent exists, one oncul block that carries the
  attestation itself (klasik_tanik, taranan, tarama, guc on the oncul block); a separate yenilik block only when no
  antecedent was found (klasik_tanik bulunamadi or yapitaslari), at most one per paragraph, always kat:arastirma.
  itiraz blocks for argued counter-evidence; tercih blocks where a source merely prefers another reading.
- Surah page, surah-level facts in few blocks: one nuzul block for Makkī/Madanī and chronology (competing reports
  and the modern dating together); one kaynak_notu block for the names (and, as a warning with its grade, a
  non-sahih merit report); a sahih merit report as its own hadis block with islev:fazilet. On an ayah page, a
  chronology point only when it concerns that ayah (e.g. a split-revelation view). Leave out what does not change
  meaning (a reading that differs only in pronunciation, a method note that restates the rules).
- Place each block where its topic is discussed (a hadith on showing off goes after the paragraph on showing off),
  and spread them: at most five blocks after any one paragraph.
- duzeltme blocks for errors in the target's base (wrong source label, misquotation, wrong ayah, factual error,
  wrong rendering), each with `taban` (exact base words) and `hata`; check PACK/errata_candidates.json.
- elenen blocks for connections you weighed and rejected that a researcher would ask about (kat:arastirma).
- Meal blocks (tur:meal; required mutercim, terim, kayip; yon and kiyas where relevant; kaynak lists the meal
  locators and the Arabic-side evidence): one per shared loss (mutercim:"ortak") and one verdict block
  (islev:sonuc); on an ayah page also one per significant translator-specific finding. Short quotations of meals
  only.
Coverage without repetition: one block per point; a report repeated unchanged by later works is one block with
`tekrar`. Do not restate the base. Each block must add a distinct unit of value: a witness, a disagreement, a
grade, a sense, an antecedent, a counter-argument, a correction, a consequence.

Record format (annotations.jsonl, one JSON object per line): all schema fields as keys (see SCHEMA_CARD.md; enum
values exactly as listed; `gelenek` is added by the script, leave it out), plus the placement, both required:
`paragraf`, the number n of the prose paragraph [¶n] the block speaks to (the block goes right after it), and
`capa`, at least three consecutive words copied exactly from that paragraph (or from its v16 additions), which confirm the number. Surah-wide
points (names, chronology, merit, the meal verdict) anchor to the paragraph that introduces the topic or the ayah.
A block whose number is missing or out of range, or whose capa is not in that paragraph or its additions, is dropped.
ids: S<sss>-<KOD>-<NNN> with the KOD of the block's tur (SCHEMA_CARD.md), numbered in page order per KOD.
Layers: kat:temel for what an advanced reader should see first at that point; ek for supporting detail;
arastirma for the audit trail (novelty detail, rejected candidates, technical source criticism).

## Step 7. Check and finish
1. Re-open every locator you cite (`corpus.py get`) and confirm the source says what the block says, the
   attribution is right (who said it; transmitted or own view; which work), any grade is the source's or the
   corpus's and never inferred, and `iliski` is honest (a thematic hadith is not direct).
2. Run the validator from the job header and fix every error and warning: a record that still fails when you
   finish is dropped.
3. Render the preview (job header) and read the page once from top to bottom as the reader would: remove
   repetition, move blocks that sit at the wrong paragraph, tighten prose. Validate again.
4. Write gaps.json: {"missing_sources":[corpus IDs you needed that are absent or empty], "not_found":[searches with
   no result that matter], "unresolved":[…]}.
Final message: blocks by tur and kat, novelty counts by klasik_tanik, number of oncul / itiraz / duzeltme blocks,
the meal verdict in one line, and anything you could not do.
