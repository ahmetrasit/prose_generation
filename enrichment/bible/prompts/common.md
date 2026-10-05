# Bible enrichment: working rules

You add evidence from Jewish and Christian texts around a frozen Turkish commentary. Read the numbered base
named in the job header. Preserve every word of it, including its v16 augment9 additions. Every annotation names
one paragraph and an exact anchor within it. The script inserts annotations and builds the source registry.

## Inputs and tools
- All working inputs belong to `enrichment/bible/`. PACK in the job header contains `base/`, `numbered/`,
  `base.json`, `quran.json` and `pack.json`. There are no dictionary or word-binding files in this pack.
- Read `enrichment/bible/SCHEMA_BIBLE_CARD.md` completely. Consult its full `SCHEMA.md` only if necessary.
- Read the selected discovery list and its adjacent `prefetch.json`. Candidates are suggestions to verify;
  prefetch gaps are gaps in available evidence.
- Use `python3 enrichment/bible/corpus.py sources`, `get LOC [LOC …]`, `ayah S:A`, or
  `search 'words' --src WLC` / `--src SBLGNT`. Search matches word prefixes after removing Hebrew pointing and
  Greek accents; it is not a morphological or root index. Try inflected forms and inspect the results.
- Use the absolute tool paths in the header. Run one command at a time, without shell loops, variables,
  redirection, pipelines, command substitution or command separators. Use the file tools to write your records.
- Read each input once and retain notes in your call directory. Start searches with `--n 10 --chars 300` and
  lookups with `--chars 1500`; request more context when needed. Every cited passage must actually be opened.
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
