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
    as the call's own final step. Placement refers to the page's own base (`capa_ayet` removed; see
    decision 12 for paragraph numbers).
11. **Bible and other non-Islamic scripture**: a separate, parallel enrichment pass after this one is in place, so
    that nothing from it contaminates the Islamic-literature page. Corpus Coranicum's intertexts are stored apart
    (`CORPUSCORANICUM-INTERTEXT`, kind `intertext`) and excluded from this pass's index.
12. **Schema 3.1 (user, 2026-10-03): one schema, three traditions, paragraph-anchored.** Every block carries
    `gelenek`: `islami` (stamped by the script in the Islamic pass), `tevrat` (Hebrew Bible in any witness, the
    Psalms included, Jewish pseudepigrapha, Mishnah, Talmud, midrash) or `incil` (New Testament in any witness,
    Christian apocrypha, Church Fathers, Syriac homilies). The user asked for Tevrat and İncil apart rather than one
    "ehl-i kitap" layer; a Hebrew Bible text read through Christian exegesis is two blocks. The field is `gelenek`,
    not `katman`, because `kat` is already labelled "Katman". Each `tur` lists the traditions it is valid in; Bible
    types: paralel, motif, karsi_anlati, soydas, yorum_gelenegi; shared: modern, elenen, kaynak_notu, yontem,
    duzeltme. Bible blocks require `bag` (benzerlik | ortak_havza | muhatap | etki_iddiasi: a parallel is not a
    dependence; the last two need a named scholar; no dependence claim for a text dated after the Qur'an),
    `tarihleme` and `nusha`. A block cites only sources of its own tradition (plus the Qur'an text and modern
    scholarship). Placement is required (user: outputs go "just after relevant paragraphs, instead of a dump at the
    end"), and by paragraph number (user: "why not to number frozen prose paragraphs and use it for anchoring"):
    `paragraf` = the prose paragraph's number, numbered as in v16's augment (from 1; headings and "Kaynaklar:"
    lines unnumbered; the pack's `numbered/` files show [¶n]), plus `capa`, at least three exact words of that
    paragraph, so a wrong number is caught instead of silently misplacing the block. A record whose number and
    words do not match is dropped. Both passes number the same frozen base, so they merge by paragraph number. A merged page shows, after each base paragraph, its islami,
    then tevrat, then incil blocks; the passes never read each other's records.

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

## S107 surah page, first call (Astra max, 2026-10-03) and schema 3.2
130 records, none dropped, 74 min, 14.6M input tokens (95% cached), 75.7k output. Read as a page (user: judge
whether blocks are "appropriate, to the point, useful, and flows naturally", not source fidelity): the blocks are
concise and concrete, the meal and counter-evidence blocks strongest; the page did not flow: 43 novelty blocks (a
third), 16 of them repeating the antecedent block above; "taban" in 40 blocks; 27 blocks closing on a disclaimer;
nine blocks after ¶1; a few low-value or misplaced blocks; an ungraded merit report filed as esbab; Saʿd b. Abī
Waqqāṣ's report on 107:5 (Prophetic attribution weak, Companion's sound) missing. Changes (schema 3.2, brief):
attested findings carry klasik_tanik on their oncul block, a yenilik block only when nothing was found (arastirma,
one per paragraph); no "taban" in metin (şerh); no closing disclaimers; each point once; one chronology block and
one names/merit block; at most five blocks per paragraph; merit reports only as sahih hadis; weak Prophetic
attributions of sound Companion statements reported as the Companion's; kat arastirma hidden by default. On the
Astra records the new rules drop 26 (25 attested yenilik, the merit report) and warn on 30 "taban" blocks.
Model trials (--model, --trial): Sol 6, Sol 6.1 (Codex); Opus 5.5, Sonnet 5.5 (claude -p). The first Claude
attempts were stopped after their Python calls were refused (an allow rule for a wrapper script that the agents
called by relative path); Claude calls now run in Claude Code's own sandbox (checked with Haiku: corpus tool runs,
writes inside only, no network). A Sonnet code review (2026-10-03) led to: blind trials (Claude cannot read out/,
other call directories or session stores), --max-budget-usd 40 and an 8-hour timeout per call, no non-trial
multi-model runs, errata written before the page, exclusive page write, paragraph numbers normalized in the
per-paragraph rules, a tighter "taban" warning.

## Cost changes after the six-model S107 trial (user agreed, 2026-10-03)
Reading by component (Opus/Sonnet S107 surah calls): base, schema and own preview 27–29% (overhead), tafsir 15–17%,
lexica 9–13%, meals 10–16%, hadith 7%, Turkish history 5–6%, naẓm 4–5%, Corpus Coranicum 2–7%, occasions/readings/
Sufi 0–2% each. No component was dropped; changes: agents read SCHEMA_CARD.md (9k chars, Islamic pass only) instead
of SCHEMA.md (24k); the numbered base once, with notes; corpus `get` batched; commands with absolute paths, no
loops, variables or cd (Claude refusals); hadith limited to a direct explanation plus at most two thematic ones;
the pack writes ayah/S_A/turkish.md (Nişanyan/TDK/Kubbealtı entries for the panel meals' key words) and lists
words still to fetch; one ishārī reading when the corpus has one; the surah page keeps surah-level material and
the meal verdict, the ayah pages the per-ayah material (word-by-word meal review, readings, single-ayah hadith,
lexicon); Claude calls use the 5-minute cache (FORCE_PROMPT_CACHING_5M; writes 1.25x input instead of 2x).

## Model decision (user, 2026-10-04)
Opus 5.5 high is the enrichment model. S107 surah page: Opus high 58 records, $7.46, 25 min; Sonnet high 72, $6.32
(one factual error); Sol 6.1 high 94 and Sol 6.1 max 103 (broadest, no or few Arabic quotes, Sol 6.1 high one false
correction, 61/106 min); Sol 6 max 62, Sol 6 high 36 (thin). S100 surah page (updated brief): Opus high 63 records,
$6.74, 26 min, best tafsir depth and meal analysis; Sol 6.1 high 79 (all 55 paragraphs, strongest counter-evidence,
no Arabic quotes); Astra max 79 (two corrections). Opus was chosen for page quality (verifiable quotes, depth,
sharper meal judgement, no false positives); its misses (untouched paragraphs, a base error both GPT runs found) are
the known gap. The S100 Opus page was accepted; the muğîrât root-label error found by Sol 6.1 and Astra was confirmed
against binding.json and logged by hand.

## The Bible pass, built (2026-10-04 evening)

The user asked whether the Bible enrichment pass (decision 11) was ready and to build it if not; and whether a
discovery session like the inter-ayah one should precede it (yes: Hebrew and Greek texts cannot be found from a
Turkish reading by search, and Corpus Coranicum covers few passages, so the page agent would otherwise work from
memory alone; the discovery list also tells the pack what to prefetch from Sefaria, since agents have no network).
Built: the intertext corpus (WLC, SBLGNT, KJV bulk; SEFARIA on demand; Corpus Coranicum intertexts) with its own
index (`corpus.py --intertext`), the Bible discovery (`_commentary/v16/discover_bible.py`, Luna and Terra, per ayah
and per image section, two turns, merged and prefetched), the pass in the orchestrator (`enrich.py --pass
ehlikitap`: own call dirs, own pages `<page>.ehlikitap.md`, validator in Bible mode, the discovery list in the
job header), the brief `prompts/ehlikitap.md`, and `enrich.py merge` (islami, tevrat, incil after each paragraph,
to `<page>.merged.md`). Not yet run on any page; no cost calibration. Gaps the corpus still has: Peshitta,
Septuagint, patristic and Syriac texts, a Turkish Bible.
