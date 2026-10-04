# Job

- Surah: 107 (ayat 1–7); ids use S107
- Target: surah — the surah page of S107 (base PACK/numbered/surah.md; all ayat 1–7)
- Workspace root: /Volumes/aro/projects/prose_generation
- PACK: /Volumes/aro/projects/prose_generation/enrichment/v2/work/s107/pack
- Your call directory (write only here): /Volumes/aro/projects/prose_generation/enrichment/v2/work/s107/zengin.surah.opus.high.a2
- Schema: /Volumes/aro/projects/prose_generation/enrichment/v2/SCHEMA.md (read it once; schema.json is the same content as data for the scripts)
- Corpus tool: python3 /Volumes/aro/projects/prose_generation/enrichment/v2/tools/corpus.py
- Validator: python3 /Volumes/aro/projects/prose_generation/enrichment/v2/validate.py --surah 107 --target surah --annotations /Volumes/aro/projects/prose_generation/enrichment/v2/work/s107/zengin.surah.opus.high.a2/annotations.jsonl
- Renderer (preview): python3 /Volumes/aro/projects/prose_generation/enrichment/v2/render.py --surah 107 --target surah --annotations /Volumes/aro/projects/prose_generation/enrichment/v2/work/s107/zengin.surah.opus.high.a2/annotations.jsonl --out /Volumes/aro/projects/prose_generation/enrichment/v2/work/s107/zengin.surah.opus.high.a2/preview


# Enrichment: shared core (read completely; the brief that follows builds on it)

## What this work is
A frozen Turkish commentary on one surah (and one commentary per ayah) already exists: the BASE, written by this
project from a dictionary of every attested branch of every root. The base develops latent and secondary lexical
images of the Qur'an's words without choosing one reading over another. It is final; you never change it.

Enrichment builds, around the base, one page where an ADVANCED reader sees every major information source at
once: transmitted and analytical tafsir (including allusive/Sufi, Muʿtazilī, Imāmī, naẓm and bayānī voices),
occasions of revelation, sahih hadith, readings, lexicon and the sense inventory of words across the Qur'an, grammar,
rhetoric, Qur'an-by-Qur'an, semantic history, historical setting, Turkish translations and what they lose, modern
scholarship, and an audit of what in the base is already attested in the literature, partly attested, or not found.
Each block is concise and says why it matters at that point. The base is the skeleton and flesh; enrichment builds
the knowledge around it and integrates the base's findings with the literature.

## Paths (relative to the workspace root /Volumes/aro/projects/prose_generation)
- PACK = enrichment/v2/work/sNNN/pack/ (built by script; read-only for you)
  - base/surah.md, base/S_A.md: the frozen base pages; base.json: their sha256
  - numbered/surah.md, numbered/S_A.md: the same pages with each prose paragraph numbered [¶n] (headings and
    "Kaynaklar:" lines are not numbered); read these, and anchor blocks by these numbers
  - ayah/S_A/{words.md, dictionary.md, usage.md, meals.md, sources.md}; roots/<root_id>.md; binding.json
  - errata_candidates.json (problems the base's own tag checker reported); pack.json (manifest, gaps)
- Schema: enrichment/v2/SCHEMA.md (types, fields, values, rules). Read it once, completely. schema.json holds the
  same content as data for the scripts; do not read it.
- Corpus tool: `python3 enrichment/v2/tools/corpus.py` with `sources [--kind K]`, `get LOC [LOC …]`,
  `ayah S:A [--kind tafsir,meal]`, `search 'words' [--src ID,ID] [--kind K] [--surah N] [--n 20] [--sahih]`.
  Search matches word prefixes; Arabic is normalised (no tashkīl, unified alef/yāʾ/tāʾ marbūṭa). Try variants.
- Your call directory (the only place you write) is given in the job header.

## Sources: what is authoritative, what is allowed
1. Word → root identity comes ONLY from PACK/binding.json (QAC + the project's root gateway). Never resolve a root
   by spelling, folding or memory. The project dictionary (corpus ID PROJE; PACK dictionary.md and roots/) is
   authoritative for senses; the six classical lexica it is built from (AYN, JAMHARA, TAHDHIB, SIHAH, MAQAYIS,
   MUFRADAT) are in the corpus in full; LISAN, LANE, ASAS, QAMUS, TAJ are further lexica. VASIT, MUHIT, HANSWEHR
   are modern Arabic: use them only inside anlam_tarihi, as evidence of later drift, never as attestation.
2. Cite only what you opened. Every block's `kaynak` holds corpus locators exactly as the corpus prints them
   (TAB:107:3, MUSLIM:2985, MAQAYIS:سهو, ELMALILI:107:2). A locator must resolve; the validator checks it.
3. Model memory is allowed only when marked: `kaynak:"hafiza"` (or a corpus pointer whose access is hafiza, e.g. a
   licensed Western book) together with `durum:degerlendirilmedi`. Memory is never allowed for hadith, for a grade,
   for revelation order/Makkī-Madanī, or for the history of a Turkish loanword.
4. Hadith blocks (`tur:hadis`) are sahih only: Bukhārī, Muslim, or a sunan report every named grader calls sahih
   (search with `--sahih`; the corpus marks each report). Occasion reports (`tur:esbab`) may be of any grade; give
   `derece`, `derece_veren` (as the source or the corpus records it, else derece:degerlendirilmedi) and
   `tarihsellik`. Never upgrade a grade because a tafsir quotes the report. Merit (fazilet) reports are hadith:
   sahih only, as tur:hadis; never file them under esbab. A report attributed to the Prophet but graded below
   sahih is never a hadis block; when the same words are soundly attributed to a Companion or Successor, report
   them as tefsir_rivayet and say in one clause that the Prophetic attribution is weak, naming who judged it.
5. Dataset hadith numbers are not sunnah.com numbers: cite the corpus locator and quote the opening words.
6. Bible and other non-Islamic scripture are handled in a separate pass (gelenek tevrat and incil). Do not cite
   them here; a Bible passage that an Islamic source itself quotes (al-Biqāʿī, for instance) is reported as that
   source's content.
7. If a source you need is missing, say so (in gaps.json); never fill the gap from memory
   without marking it.

## Epistemic rules
- Never present a report as history because a classical book transmits it; competing reports stay competing.
- A thematic hadith is not direct tafsir (`iliski:tematik`, not `dogrudan`).
- A source's stated preference ("the correct view is X") is `islev:tercih`. `islev:itiraz` is an argued exclusion:
  why the base's reading cannot hold here (grammar, near-synonymy, root identity, a reading), with `gerekce`.
- Novelty is always relative to what you searched: `taranan` lists the corpus IDs, `tarama` says whether you
  searched only the per-ayah slice (`dilim`) or whole texts (`tam`). Never write "this is absent from classical
  tafsir"; write "not found in the checked sources: …".
- Keep three levels apart in every block: what the ayah says in context; what a source attests; what the base
  synthesises. A root-family image can be real without being what the ayah means.
- Do not adjudicate the base's readings. Report evidence for and against them; the base's readings coexist.

## Block text (`metin`)
Turkish, in the register of the base: plain, warm, exact; explain Arabic terms briefly; name the scholar, not
"the scholars"; no first person, no talk about your process or tools. One paragraph; at most 80 words (layers
temel/ek) or 120 (arastirma). Short quotations only; Arabic quotations go in the base's reader-tag form
{ar:…, tr:…, gloss:…, source:…} with the corpus locator as source.
- The block is read right after a paragraph of the commentary, by a reader who has just read that paragraph. Call
  the commentary "şerh" when you must refer to it (never "taban", "base" or "the project"); usually just state the
  point.
- Say what the source adds and stop. Do not end with a disclaimer about what the source does not prove or what the
  block is not: the tags already say whether a link is direct, thematic or reported. State a limit only when it
  changes the reading, as its own itiraz or sinir block.
- Say each thing once on the page: a point made in one block is not repeated in another.


# zengin: one page's records (research, meal review and composition in one call)

You produce every enrichment block for ONE page, the target in the job header: the surah page or one ayah page. You
write records, not Markdown: afterwards a script checks each record, drops any record that fails a rule (it is not
sent back to you), inserts the rest into the frozen base after the paragraph each names, and builds the source
registry. Work through the steps in order. Notes you make along the way are yours (keep them in your call
directory if useful); only annotations.jsonl and gaps.json are read.

## Scope by target
- Ayah page (target S:A): everything an advanced reader needs about that ayah. Every record's `ayet` includes the
  target ayah (a range such as 107:4-7 is right when the point concerns the group). Anchor to the paragraphs of
  PACK/numbered/S_A.md.
- Surah page (target surah): the surah as a whole and the points its commentary makes — names, occasions and
  chronology, Makkī/Madanī, structure and naẓm, merit reports, the surah's place among its neighbours, the claims of
  the surah commentary, and the surah's meal verdict (shared losses; best literal and best explanatory meal).
  Each ayah has its own page, written in its own call: on the surah page give per-ayah detail only where a paragraph
  of the surah commentary speaks to it. Anchor to the paragraphs of PACK/numbered/surah.md.
- Every block sits right after the base paragraph it speaks to; there is no section at the end of the page.

## Step 1. Read
Read the target's numbered base page completely (for the surah page: PACK/numbered/surah.md, then every
PACK/numbered/S_A.md for orientation). Then, for each ayah in scope, PACK/ayah/S_A/*.md and the roots/ files of its bound roots. Do not
skim: a claim missed here is missing from the page.

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
   well-known direct explanations of each key word are on the page, Prophetic or Companion, each with its grade
   handled by rule 4 of the shared core (a weak Prophetic attribution of a sound Companion statement is reported
   as the Companion's).
2. Analytical tafsir: KASHSHAF, RAZI, BAYDAWI, NASAFI, QURTUBI, IBNATIYYA, ABUHAYYAN, ALUSI, MAWARDI (numbered
   senses without choosing), IBNASHUR, TABRISI, BIQAI (naẓm), and the Turkish ELMALILI and KURANYOLU-TEFSIR;
   allusive QUSHAYRI, SULAMI, TUSTARI, BURSEVI; ABDUH-AMMA; others the corpus lists for the ayah.
3. Occasions and chronology: WAHIDI-ASBAB, SUYUTI-LUBAB, the tafsirs' reports, ITQAN/BURHAN lists, TDVIA surah
   article, CORPUSCORANICUM chronology. Keep Makkī/Madanī apart from occasion reports; record every competing
   attribution with its transmitter and grade information.
4. Hadith: direct prophetic explanation; hadith using the same key expression; strong thematic or counter-scene
   hadith; merit (fazilet) reports. Sahih only for hadis (search with --sahih); non-sahih reports only as esbab,
   with their grade.
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
     (NISANYAN, KUBBEALTI, TARAMA, TDK, TDVIA term articles) goes to anlam_tarihi; here only its effect on the meal;
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
   its ayat.

## Step 6. Compose the records
What a good page has:
- For every ayah in scope: its anchor meaning (dayanak) from the received tafsir; the real disagreements (ihtilaf,
  with who holds what); the sense range (anlam_alani) where the tradition is plural; occasions and chronology with
  grades and historicity; sahih hadith that explain or illuminate; readings that change meaning; the lexical and
  wujūh evidence behind the base's words; grammar and rhetoric where they decide something.
- For every claim of the base of kind imge or sentez: when an antecedent exists, one oncul block that carries the
  attestation itself (klasik_tanik, taranan, tarama, guc on the oncul block); a separate yenilik block only when no
  antecedent was found (klasik_tanik bulunamadi or yapitaslari), at most one per paragraph, always kat:arastirma.
  itiraz blocks for argued counter-evidence; tercih blocks where a source merely prefers another reading.
- Surah-level facts in few blocks: one nuzul block for Makkī/Madanī and chronology (competing reports and the
  modern dating together), one block for the names and merit. Leave out what does not change meaning (a reading
  that differs only in pronunciation, a method note that restates the rules).
- Place each block where its topic is discussed (a hadith on showing off goes after the paragraph on showing off),
  and spread them: at most five blocks after any one paragraph.
- duzeltme blocks for errors in the target's base (wrong source label, misquotation, wrong ayah, factual error,
  wrong rendering), each with `taban` (exact base words) and `hata`; check PACK/errata_candidates.json.
- elenen blocks for connections you weighed and rejected that a researcher would ask about (kat:arastirma).
- Meal blocks (tur:meal; required mutercim, terim, kayip; yon and kiyas where relevant; kaynak lists the meal
  locators and the Arabic-side evidence): one per shared loss (mutercim:"ortak"), one per significant
  translator-specific finding, and one verdict block (islev:sonuc). Short quotations of meals only.
Coverage without repetition: one block per point; a report repeated unchanged by later works is one block with
`tekrar`. Do not restate the base. Each block must add a distinct unit of value: a witness, a disagreement, a
grade, a sense, an antecedent, a counter-argument, a correction, a consequence.

Record format (annotations.jsonl, one JSON object per line): all schema fields as keys (see SCHEMA.md; enum
values exactly as listed; `gelenek` is added by the script, leave it out), plus the placement, both required:
`paragraf`, the number n of the prose paragraph [¶n] the block speaks to (the block goes right after it), and
`capa`, at least three consecutive words copied exactly from that paragraph, which confirm the number. Surah-wide
points (names, chronology, merit, the meal verdict) anchor to the paragraph that introduces the topic or the ayah.
A block whose number is missing or out of range, or whose capa is not in that paragraph, is dropped.
ids: S<sss>-<KOD>-<NNN> with the KOD of the block's tur (SCHEMA.md), numbered in page order per KOD.
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
