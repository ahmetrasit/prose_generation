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
- Schema: enrichment/v2/schema.json and enrichment/v2/SCHEMA.md (types, fields, values, rules)
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
   `tarihsellik`. Never upgrade a grade because a tafsir quotes the report.
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
