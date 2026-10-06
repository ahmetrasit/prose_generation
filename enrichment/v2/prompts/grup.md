# grup, stage 1: extract one group's positions, one line each

A frozen Turkish commentary (the "şerh") exists for one surah and for each of its ayat. Enrichment shows an advanced
reader, after each paragraph of it, every point the sources discuss there, one sentence each, with pointers
(corpus locators) to the details. You are one of many independent units: you read one group of sources (named in
the job header with its focus) and write down every position they take on this surah's ayat. You do not see the
commentary; a later call places your lines after its paragraphs, gathers the same position from other groups, and
keeps all pointers. So write every position your sources take, including ones the commentary may already state:
the reader is shown where it has been said.

## Read
Your material is in this prompt (or in the files the job header lists): read all of it, once. Each segment opens
with `### <locator> [tie] → <page(s)>`, then flags in braces. An excerpt or a cut says so and gives the
`corpus.py get` command for the rest: run it only when the missing part matters. Corpus tool: `get LOC [LOC …]
[--chars N]`, `search 'words' [--src ID,ID] [--surah N] [--n 10 --chars 300] [--sahih]`; up to 8 calls in all
(unless your group's section says otherwise), each with `--chars` limits: every result stays in your context.

## Write lines.jsonl: one line per position
`{"id":"L1","pg":"1:2","w":["1:2:1"],"t":"tefsir_dirayet","f":"aciklama","k":"KASHSHAF:1:2|BAYDAWI:1:2","a":"Zemahşerî; Beyzâvî","m":"…"}`
- pg: the page (`surah` or S:A) the position concerns; one of the pages in the job header.
- w: the ayah words it concerns, as refs S:A:W from PACK/binding.json (e.g. ["1:2:1"]); "ayah" for the ayah as a
  whole; "surah" for the surah as a whole.
- t, f: tur and islev (SCHEMA_CARD.md). k: the locators, exactly as the material headings print them,
  pipe-separated. a: the holders, `;`-separated. m: the position in ONE Turkish sentence (at most ~40 words).
- Other fields only when the type needs them or the default is wrong: hadis `derece`, `derece_veren`; esbab
  `derece`, `derece_veren`, `tarihsellik`; nuzul `tarihsellik`; kiraat `kiraat_turu`; meal `mutercim`, `terim`,
  `kayip`; vucuh `guc`, `terim`; `ravi`, `koken`, `gerekce` (for itiraz), `not`; `l` (iliski) when it is not
  dogrudan; `d` (durum) when it is not the default (aktarilan for transmitted reports and allusive readings,
  tartismali for ihtilaf, acik otherwise); `kat` temel for a primary point (default ek).
- One line per position: two holders or two reasons are two lines, even when they agree in outline. The same
  position in a later source of your group adds that locator to k (and the holder to a), not a new line. A
  distinctive argument for a position is a clause of its sentence, or its own line.
- m says who holds what and stops: no disclaimers, no first person, no talk of tools; name the scholar; Arabic
  terms explained briefly; a short Arabic quotation only in the tag form {ar:…, tr:…, gloss:…, source:<locator>}.

## Sources
1. Cite only what you opened. Word → root identity only from PACK/binding.json.
2. Model memory only as k "hafiza" with d "degerlendirilmedi"; never for hadith, a grade, revelation order or
   Makkī/Madanī, or a Turkish loanword's history.
3. `t:hadis` is sahih only (the material marks sahih=True): Bukhārī, Muslim, or a sunan report every named grader
   calls sahih; merit (fazilet) reports likewise. Occasion reports (`esbab`) may be of any grade, with the grade and
   who gave it. Never upgrade a grade because a tafsir quotes the report. A Prophetic attribution graded below
   sahih is never hadis: give a sound Companion/Successor version as tefsir_rivayet and say in a clause who judged
   the Prophetic one weak. Dataset hadith numbers are not sunnah.com numbers.
4. No Bible or other non-Islamic scripture except as the content of an Islamic source that quotes it.
5. Text status flags: «Shamela digital edition … not checked» or «ocr draft … do not quote»: never copy Arabic
   wording from that segment; report it in Turkish. «machine-read»: quote at most a few clean words. «note marker not
   found» or «verse alignment uncertain»: say which ayah the source discusses only from its text. A study quoting
   another author is cited as that study's quotation.
6. Competing reports stay competing; a source's stated preference is f tercih; f itiraz needs gerekce.

## kapsam.jsonl: every segment once
`{"seg":"<locator>","durum":"kullanildi","satir":["L1","L4"]}` — kullanildi: the lines whose k carries this
locator; `{"seg":…,"durum":"ilgisiz"}` — not about these ayat (a search hit, a citation in passing);
`{"seg":…,"durum":"okunamadi","neden":"…"}` — unreadable. A REQUIRED group: a page of the job header with no line
of yours gets `{"page":"<page>","durum":"yok","neden":"why this voice has nothing here"}`.

## Finish
Run the check from the job header and fix every FAIL (a line that still fails is dropped). Write gaps.json:
{"missing_sources": [], "not_found": [], "searches": [your corpus calls]}. Reply with one line: written.
