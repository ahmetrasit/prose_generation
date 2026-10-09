# Bible enrichment: working rules

You add evidence from Jewish and Christian texts around a frozen Turkish commentary. Read the numbered base
named in the job header (the frozen r13 commentary, or an augment9 base in packs built before
2026-10-09). Preserve every word of it, including any v16 augment additions it holds. Every annotation names
one paragraph and an exact anchor within it. The script inserts annotations and builds the source registry.

## Inputs and tools
- All working inputs belong to `enrichment/bible/`. PACK in the job header contains `base/`, `numbered/`,
  `base.json`, `quran.json` and `pack.json`. There are no dictionary or word-binding files in this pack.
- Read `enrichment/bible/SCHEMA_BIBLE_CARD.md` completely. Consult its full `SCHEMA.md` only if necessary.
- Read the selected discovery list, its `.merged.json` review sidecar, and adjacent `prefetch.json`. Reader
  grades, reasons and wording flags are unverified. Prefetch gaps are gaps in available evidence. Distinct
  connections under one reference need distinct verdicts; a high grade or reader agreement is not proof.
- Use `python3 enrichment/bible/corpus.py sources`, `get LOC [LOC …]`, `ayah S:A`, or
  `search 'words' --src WLC` / `--src SBLGNT`. Search matches word prefixes after removing Hebrew pointing and
  Greek accents; it is not a morphological or root index. Try inflected forms and inspect the results.
- For roots and lemmas use `python3 enrichment/bible/hebrew.py root ROOT` (every WLC occurrence of a Hebrew or
  Aramaic root, with lexicon entries and BDB notes), `cognates 'ع ص ر'` (the corresponding Hebrew/Aramaic roots of
  an Arabic root) and `word WLC:Book.C.V` (each word of a verse with its lemma, root and gloss). BDB heads keep
  cognate glosses, but this edition shows Arabic or Syriac script only as a placeholder ([Arabic]).
- Use the absolute tool paths in the header. Bible tool commands run one at a time, without shell loops,
  variables, redirection, command substitution or command separators. Read-only shell (`cat`, `head`, `tail`,
  `ls`, `grep`, `wc`, `sed -n`, `python3 -I -c` that only reads JSON or TSV) may be used on your inputs and call
  directory, joined by pipes or `;` but with no redirection. Use the file tools to write your records.
- A helper script (for example one that summarises the discovery list or assembles verdicts.jsonl from your own
  judgement table) goes INSIDE your call directory, written with the file tools, run as `python3 -I SCRIPT`, and
  may name only your inputs and call directory; standard modules such as json, csv, re and collections only.
  Never write anywhere else (no session scratchpad). Your judgements stay yours: a script only formats them.
- Read each input once and retain notes in your call directory. Start searches with `--n 10 --chars 300` and
  lookups with `--chars 1500`; request more context when needed. Every cited passage must actually be opened.
- Save `annotations.jsonl`, `verdicts.jsonl`, `gaps.json` and `root_verdicts.jsonl` in your call directory. The verdict draft command
  checks structure during work; final acceptance also checks the native transcript's actual corpus get results.
- Write only in your call directory. Do not read accepted enrichment pages, other calls, or the Islamic
  enrichment workspace. Do not fetch sources, rebuild packs or indexes, or call models. Report missing texts.

## Evidence and prose
Every `kaynak` uses a locator returned by this corpus. Hebrew WLC and Greek SBLGNT are the primary biblical
texts. English KJV is a finding aid. Identify editions and resolve each edition's own verse numbering.

Memory must be explicit: `kaynak:"hafiza"` (or a source whose access is hafiza) and
`durum:degerlendirilmedi`. It cannot establish a quotation or verify a candidate. Report absent witnesses in
`gaps.json`; do not imply they were searched.

Keep the Qur'anic context, the other text's evidence and the commentary's synthesis distinct. Present parallels
as parallels. Attribute stronger historical claims to named scholarship, observe dating, and retain alternatives.
Report evidence for and against the commentary without choosing among its readings.

Write concise Turkish in the commentary's register: one paragraph, at most 80 words for temel/ek or 120 for
arastirma. Name the text or scholar and explain what the evidence adds at this location. Refer to the commentary
as “şerh” when necessary. No first person, process narration or repeated points. Use the schema's relationship
and status fields; explain a limitation in the prose only when it changes the reading.

## Semitic evidence (Hebrew, Biblical Aramaic and the Arabic roots of the page)
Arabic, Hebrew and Aramaic are sister languages, and their shared roots are evidence in their own right. Use them
both to explain the ayah and to show where the Bible's version differs from what the ayah says:
- The page's Semitic root table lists every Arabic root the frozen text cites, with the Hebrew and Biblical Aramaic
  roots that correspond to it by regular sound correspondences and exist in the lexicon. Work through each one.
- For a corresponding root, look at its semantic range across its Hebrew Bible occurrences (`hebrew.py root`),
  not only one verse: which senses it shares with the Arabic branch the page develops, which it lacks, and
  where the Bible uses it in a scene, formula or image comparable to the ayah's.
- Look for wordplay and paronomasia carried by a root (a Hebrew text that plays on the same consonants the ayah
  or its commentary turns on), for a Biblical Aramaic usage, and for a Hebrew passage whose wording makes the
  Qur'anic difference visible (karsi_anlati).
- Name the basis of every cognate claim: "BDB cites an Arabic cognate" (the lexicon's own note) or "sound
  correspondence only" (unverified by a lexicon), and quote the WLC wording verbatim from the corpus. A shared
  root is evidence of related vocabulary, not of borrowing or dependence; a loan claim needs named scholarship.
- A root may correspond in form and differ in meaning (a false friend): say so rather than force a link. A root
  the table does not list may still be proposed from knowledge, marked as such, and checked in the corpus.

Record one decision per Arabic root of the table in `root_verdicts.jsonl`, one JSON object per line:
{"root":"<the Arabic root as written in the table>","decision":"used","hebrew":["<Hebrew or Aramaic root>"],"reason":"…","paragraphs":[n],"annotations":["<kept annotation id>"]}
`decision` is `used` (it carries at least one kept annotation), `no_qualifying_parallel` (a corresponding root
exists but adds nothing specific here), `false_friend` (same consonants, unrelated sense) or `no_hebrew_cognate`
(nothing corresponds). Every root needs a specific reason; no root may be left without a line.
