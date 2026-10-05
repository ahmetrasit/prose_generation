# grup: one group's voice for the pages of one unit

A frozen Turkish commentary (the BASE, "şerh") exists for one surah and for each of its ayat. It is final; you never
change it. Enrichment builds one page per base page where an advanced reader sees every major source tradition
beside the commentary. You are one of many independent units: each reads one group of sources (named in the job
header with its focus) for a few pages and writes the blocks that group contributes. Other units cover the other
groups; a script merges every unit's kept blocks into each page. Give this group's voice fully and precisely and
leave other groups' material to them.

## Read
Read every file the job header lists, completely, once, at the start (they are independent): the digests of your
pages, your material files, the schema card. Do not read them again; keep notes in a file in your call directory if
you need them. Read nothing else from PACK, and never other call directories or out/.
- A digest shows each paragraph of a page shortened (first and last words, «…» for the rest, Arabic citation tags
  shortened to «{ar… S:A}»). When a point needs the whole paragraph, read just that paragraph from the numbered page
  the digest names (PACK/numbered/<page>.md), never the whole page.
- Each material segment opens with `### <locator> [tie] → <page>`: the page it belongs to, then flags in braces. An
  excerpt or a cut says so and gives the `corpus.py get` command for the rest: run it only when the missing part
  matters.
- Corpus tool (job header): `get LOC [LOC …] [--chars N]`, `ayah S:A`, `cites S:A`, `search 'words' [--src ID,ID]
  [--surah N] [--n 10 --chars 300] [--sahih]`. Search matches word prefixes, Arabic normalised. Up to 8 calls beyond
  your material where it points to something you must check (unless your group's section says otherwise).
- Every result stays in your context for the rest of the call: open only what you will use, with `--chars` limits.

## Sources
1. Cite only what you opened: `kaynak` holds corpus locators exactly as printed (TAB:107:3, MUSLIM:2985),
   pipe-separated; the validator resolves each one. Word → root identity comes only from PACK/binding.json.
2. Model memory only as `kaynak:"hafiza"` with `durum:degerlendirilmedi`; never for hadith, a grade, revelation
   order/Makkī-Madanī, or a Turkish loanword's history.
3. `tur:hadis` is sahih only: Bukhārī, Muslim, or a sunan report every named grader calls sahih (the material marks
   sahih=1); merit (fazilet) reports likewise. Occasion reports (`tur:esbab`) may be of any grade, with `derece`,
   `derece_veren` and `tarihsellik`. Never upgrade a grade because a tafsir quotes the report. A Prophetic
   attribution graded below sahih is never a hadis block: report a sound Companion/Successor version as
   tefsir_rivayet, naming who judged the Prophetic one weak. Dataset hadith numbers are not sunnah.com numbers: cite
   the locator and quote the opening words.
4. No Bible or other non-Islamic scripture (a separate pass), except as the content of an Islamic source that quotes it.
5. Text status flags: «Shamela digital edition … not checked» or «ocr draft … do not quote»: never copy Arabic
   wording from that segment; report it in Turkish and cite the locator. «machine-read»: quote at most a few clean
   words. «note marker not found» or «verse alignment uncertain»: say which ayah the source discusses only from its
   text. A study's quotation of another author is cited as that study's quotation, never as the author's own text.
6. A source you need but do not have: say so in gaps.json; never fill it from memory unmarked.

## Epistemic rules
- Competing reports stay competing; a transmitted report is not history because a classical book carries it.
- A thematic hadith is not direct tafsir (`iliski:tematik`). A source's stated preference is `islev:tercih`;
  `islev:itiraz` is an argued exclusion of the base's reading, with `gerekce`.
- Novelty is relative to what was searched (`taranan`, `tarama`): "not found in the checked sources", never "absent
  from tafsir".
- Keep apart what the ayah says, what a source attests, and what the base synthesises, with the tags and exact
  attribution ("Râgıb … der"), not with closing disclaimers. Do not adjudicate the base's readings.

## What to write: records (SCHEMA_CARD.md is the format)
- Scope by page. An ayah page carries what concerns that ayah. The surah page carries the surah as a whole (names,
  merit, chronology, Makkī/Madanī, structure and naẓm, its neighbours) and what a paragraph of the surah commentary
  calls for. A point about one ayah goes on that ayah's page unless a surah paragraph is about it.
- Anchor every block after the paragraph it speaks to: `paragraf` = n of [¶n] on that page; `capa` = three or more
  consecutive words copied exactly from that paragraph (outside «…» and outside shortened tags). A wrong number or a
  capa not in the paragraph is dropped. On an ayah page `ayet` includes that ayah. Ids S<sss>-<KOD>-<NNN> with the
  KOD of the tur, numbered as you like (the merge renumbers).
- One block per distinct point that adds value at that place: a witness, a disagreement, a grade, a sense, an
  antecedent, a counter-argument. A report repeated unchanged by a later work of your group is one block with
  `tekrar`. Do not restate the base. Nothing outside your group's focus.
- `metin`: Turkish, in the base's register (plain, warm, exact; Arabic terms explained briefly; name the scholar);
  one paragraph, at most 80 words (kat temel/ek) or 120 (arastirma); no first person, no talk of process or tools;
  refer to the commentary as "şerh" only when you must. Say what the source adds and stop: no closing disclaimer.
  Arabic quotations short, in the base's tag form {ar:…, tr:…, gloss:…, source:<locator>}. Each point once.
- Write `records.<page-tag>.jsonl` per page with blocks (<page-tag> = `surah` or S_A, e.g. records.1_2.jsonl); split
  a long one into records.<page-tag>.1.jsonl, .2.jsonl … and then write no unsplit file. No blocks, no file.

## Account for every segment: kapsam.jsonl
One line for EVERY material segment (every `### <locator>` heading), exactly once:
`{"seg": "<locator>", "durum": "kullanildi|tekrar|yeni_yok|ilgisiz|okunamadi", "kayit_ids": [...], "neden": "..."}`
- kullanildi: a block uses it (kayit_ids required). tekrar: the same point as another segment (neden names it).
  yeni_yok: nothing for these pages beyond the base or another block. ilgisiz: not about these ayat (a search hit,
  a citation in passing). okunamadi: unreadable (neden says how). neden is otherwise optional: a few words at most.
- A REQUIRED group: for every page of the unit where no block of the group stands, add
  `{"page": "<page>", "durum": "yok", "neden": "why this voice has nothing here"}`.

## Check and finish
1. Re-open any locator you cite that the material only excerpted, and confirm it says what the block says.
2. Run the check for every page you wrote records for, in one command (the job header gives it; join with
   `;`); fix every FAIL line: a record that still fails is dropped.
3. Write gaps.json: {"missing_sources": [], "not_found": [], "unresolved": [], "searches": [your extra calls]}.
4. Reply with one line: written.
