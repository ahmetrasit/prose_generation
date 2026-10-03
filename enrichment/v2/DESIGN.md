# Enrichment v2: design and decisions

Started 2026-10-03 from the user's decisions in conversation. v1 (`enrichment/v1/`, schema 2.0) stays as the record
of the first runs (S1, S100, S107 and the S107 model comparison); nothing there is changed or migrated.

## Purpose
The v16 output is frozen: the skeleton and flesh of the analysis. Enrichment builds around it one page per surah
(and per ayah) for an ADVANCED reader who wants every major information source at once — enough to write their
own tafsir or build a comprehensive understanding — with each paragraph concise, and the base's own findings
integrated with the literature (antecedents, counter-evidence, corrections). Non-mainstream traditions are welcome
when they add value (al-Biqāʿī, al-Khūlī/Bint al-Shāṭiʾ, ishārī, Muʿtazilī, Imāmī voices).

## Why v2 (what went wrong in v1)
- The dictionary lookup used a stale agent snapshot (`v1/corpus/dictionary_agent`, 1,679 roots, commit unknown)
  missing 47 roots the base cites (سهو root_003249, معن root_004706 in S107). Agents bound words to roots by hand
  through alias shards, reported "root does not exist", and flagged a correct base label as a "probable mislabel".
- Lexica, Turkish meals and several sources were fetched from the web per run (Hawramani, a page-summarising fetch
  tool for meals), so wordings and editions could not be verified.
- Agents edited the base Markdown directly; four parallel drafts per surah; a 990-line protocol mixed ontology,
  procedure and a stale "Codex" master prompt that disagreed with the real prompt template.
- The tag system had four overlapping axes (type, tradition, role, relation) filled mechanically.

## Decisions (user, 2026-10-03)
1. **Dictionary**: `../dictionary` is authoritative, read through v9's gateway (`quran-data/data/dictionary/tr`, a
   transfer pinned to the dictionary's HEAD commit; pack.py refuses to build if they differ). Word → root identity
   comes only from the gateway (QAC lemma/root → root ids, documented alternatives, echo roots) in `binding.json`.
2. **Local first**: every citable source is in `enrichment/corpus/` with provenance (`source.json`) and one index
   (`tools/corpus.py`). Workers run without network. Licensed works the project cannot hold are memory pointers.
3. **Hadith**: sahih only for `hadis` — Bukhārī and Muslim by collection; other books only when every named grader
   in the dataset says sahih ("hasan sahih", "sahih isnad" excluded). Occasion reports (`esbab`) may carry any
   grade, always shown with the grader and historicity.
4. **Memory** (model recall) is allowed when marked (`kaynak:hafiza`, `durum:degerlendirilmedi`), never for
   hadith, grades, revelation order or Turkish loanword history.
5. **All 16 tafsirs** of the per-ayah slice stay in the default research set (the dilution finding was about the
   v16 writer, not a reference page). Western academic books are memory pointers when not downloadable.
6. **Elmalılı, Hak Dini Kur'an Dili**: the YEK critical edition (Köksal & Kaya, 2021–23, 6 vols), official free
   PDFs with a text layer; converted to per-ayah segments (`ELMALILI`), his meal isolated (`MEAL-ELMALILI-HDKD`).
7. **Meals**: a fixed panel of 16 (Diyanet İşleri current and 1961; Diyanet Vakfı; Kur'an Yolu; Elmalılı original;
   Bilmen; Çantay; Ateş; Bulaç; Esed; Y. N. Öztürk; İslamoğlu; Okuyan; Gölpınarlı; Süleymaniye; Hayrat) plus a wide
   reference set. Diyanet İşleri, TDV and Kur'an Yolu share one lineage (one witness for consensus). Esed (TR) is a
   relay of Asad's English: compared against both the Arabic and ASAD-EN. Arberry is the literal English control.
   Edip Yüksel stays out of the panel (2026 court order on one host). Mustafa Öztürk, Hamidullah, Atay and Asad's
   notes are memory pointers (no licensed free text).
8. **Meal review**: which meal conveys the meaning best (best literal, best explanatory, best per criterion — never
   one overall winner) and what the meals lose in common. Losses typed: wrong word (ṣudūr → kalp), dropped element
   (kalplerde drops "their"), collapsed range, unmarked addition, Turkish drift, marking change, relay drift; judged
   as patterns across the Qur'an (22:46 is the decisive test for ṣadr/qalb), with what Turkish forces kept apart.
9. **Tags**: schema 3.0 in ASCII-folded Turkish with tr/en/de labels (`schema.json`, `SCHEMA.md` generated).
10. **Orchestration**: v16-like (`enrich.py`), after v16's augment step: one agent call per page (the surah page,
    each ayah page), never rerun; the call writes records grounded in the saved files, scripts check, render and
    accept. A record that fails a rule is dropped and listed, not repaired. Model: GPT-6 Astra (subscription; USD
    not reported). Revised the same day (user: "i'm having only a single run per surah/ayah (called augment) and it
    normally takes care of everything. the only difference is now we'll ground everything to saved files"): the
    first version ran a research map ‖ meal review → compose → independent audit → up to two repair rounds per
    surah (4–8 calls). Its briefs (`prompts/harita.md`, `meal.md`, `yaz.md`, `denetim.md`, `onarim.md`) are kept
    as the record and are not used; `prompts/zengin.md` merges harita, meal and yaz, plus the audit's source check
    as the call's own final step. Placement is one field, `capa`, a sentence of the page's own base
    (`capa_ayet` removed).
11. **Bible and other non-Islamic scripture**: a separate, parallel enrichment pass after this one is in place, so
    that nothing from it contaminates the Islamic-literature page. Corpus Coranicum's intertexts are stored apart
    (`CORPUSCORANICUM-INTERTEXT`, kind `intertext`) and excluded from this pass's index.

## Schema 3.0 against 2.0
Removed: `tradition` (folded into `tur`), ten roles that repeated a type, five relations that repeated a type,
`confidence`, `priority`+`audience` (merged into `kat`), the hadith-grade enum (sahih only), `reader_note` (the
reader app renders the legend). Added types: `tefsir_rivayet`/`tefsir_dirayet` split, `isari`, `vucuh`, `lugat`,
`nahiv`, `belagat`, `meal`, `elenen`, `duzeltme`; roles `oncul` (antecedent of a base finding), `itiraz` (argued
counter-evidence, with `gerekce`), `tercih` (a source's preference), `tasnif` (enumeration without choosing),
`fazilet`, `yapi`; fields `tarama` (slice vs whole texts), `derece`/`derece_veren`, `kayip`/`yon`/`kiyas`,
`taban`/`hata`, `sozluk`. Source IDs are corpus locators resolved by the validator; the registry is generated.

## Resource review
`REVIEW_resources_fable.md` (Fable 5.1, 2026-10-03): the plan was deep in redundant later tafsir and thin where the
project's method has its roots. Adopted: maʿānī/gharīb works, wujūh wa-naẓāʾir books and al-Furūq as the first
place to look for antecedents; Itqān/Burhān for chronology; ḥujja and shādhdh qirāʾāt works; Bint al-Shāṭiʾ
(pointer), Ṭabrisī, ʿAbduh's juzʾ ʿAmma; ishārī works; TDV İA; Turkish loanword dictionaries; Elmalılı; lineage and
relay marking; Arberry control. Rejected: making 8 of the 16 tafsirs on-demand (decision 5).

## Corrections to earlier assumptions
- quran-uthmani.tsv lists the basmala as `:0`; ayah numbers are not shifted (v1's prompt template says otherwise).
- quran-tafsir.net `seoty` is al-Durr al-manthūr; `wahidy` is al-Wāḥidī's al-Wajīz (`WAHIDI-QT`; the site's book list
  names it), not his Asbāb or al-Basīṭ (both fetched separately from OpenITI).
- al-Rāghib's tafsir does not reach the late surahs; his Mufradāt is the relevant work. Nursi's İşârâtü'l-İ'câz
  covers only S1–S2:33.
