# zengin (dosya): one ayah page's records from a dossier, in one tool-free call

You produce every enrichment block for ONE ayah page, the target in the job header, exactly as the brief zengin.md
describes, with one difference: you use no tools. Everything you may read is in this message, in the DOSSIER after
the schema card: the numbered base, the pack's files for the ayah, its bound roots, every corpus segment tied to the
ayah, the lexica entries of its roots, the sahih hadith and the readings whose text holds the ayah's words, and the
errata candidates. A script gathered it; nothing outside it exists for this call.

The shared core (common.md) holds, except where it speaks of commands, searches, files to open, the validator or
the preview: there is none of that here. In particular:
- Cite only locators that appear in the dossier, exactly as printed after `==`. A locator not in the dossier does
  not exist for you; memory is allowed only as `kaynak:"hafiza"` with `durum:degerlendirilmedi`, under the core's
  limits (never for hadith, grades, chronology, Turkish word history).
- A segment cut at the dossier's limit is cited for what its shown part says; do not guess the rest.
- Antecedents and counter-evidence (zengin.md step 4): search within the dossier's full-text sources; write
  `tarama:dilim` and list in `taranan` the corpus IDs present in the dossier. Never write "not found in classical
  tafsir": write "not found in the dossier's sources: …".
- The meal review (step 5) uses the pack's words.md and meals.md in the dossier; other ayat's meals are not
  available: say so where a pattern across occurrences would have been checked.
- Step 7 (check and finish) is done by reading your own records against the dossier before you write them; the
  script validates afterwards and drops what fails, without sending it back.

Output: write the records to annotations.jsonl in your call directory with the Write tool, one JSON object per
line, in page order, all schema fields as keys (`gelenek` left out), with `paragraf` and `capa`; then a second file
gaps.json ({"missing_sources":[…], "not_found":[…], "unresolved":[…]}) naming what the dossier lacked. Nothing else
is written or read. Your reply in chat is one line.
