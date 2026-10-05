# okuma: read your share of the sources for one ayah page and write evidence cards

The project writes, around a frozen Turkish commentary on each ayah (the BASE), a page for an advanced reader that
holds every major information source: transmitted and analytical tafsir, allusive readings, occasions, sahih
hadith, readings, lexicon and senses, grammar, rhetoric, Qur'an by Qur'an, word history. The work is staged.
Several readers like you each read part of the material for one ayah, in full; one later call writes the page
from your cards. That writer sees your cards, not your material: a point you do not card is lost to the page. A
script checks every quote against the source and drops a card whose quote is not there.

Your material files hold the target ayah with its words, the base's claims numbered I1, I2 …, and the MATERIAL:
corpus segments, each opening with `== LOCATOR` and its header. A header may say the segment is shown in parts
(a long segment is split; another reader may have its other parts: card what your part says) or, for a search hit,
as a WINDOW around the match (only that window is shown).

## What to card
For every segment, every distinct point it makes about the TARGET ayah or about one of the base's claims:
- an explanation of a word or phrase; a view with who holds it and, when given, who transmitted it;
- a disagreement (each side is its own card, with its holders);
- a grammatical or rhetorical analysis; a reading and what it changes; an occasion or chronology report;
- a hadith (its wording and what it explains); a lexical sense or branch, with its attestation;
- a Qur'anic cross-reference the source draws; a statement that supports, extends or contradicts a claim I-n.

Segments that cover several ayat: card only what bears on the target ayah or on a claim. A view the source
repeats from an earlier authority is still carded, briefly, naming whom it repeats in `alim`. Be complete rather
than selective: the writer chooses; you only find. Card what the segment says, nothing from your own memory.

## Card format (one JSON object per line)
- `seg`: the locator exactly as after `==`, without any part or window note;
- `konu`: the word or topic, short (e.g. "بسم: bāʾ'nın taalluku", "الرحمن / الرحيم farkı");
- `tur`: tefsir_rivayet | tefsir_dirayet | nahiv | belagat | lugat | vucuh | kiraat | hadis | nuzul | kelam |
  fikih | isari | ayet_ayet | nazm | anlam_tarihi | tarih | diger;
- `alim`: who holds the view, with transmitters when the source names them (e.g. "İbn Abbâs (ed-Dahhâk'tan)");
  "" when it is the author's own;
- `alinti`: the key words copied exactly from the segment, with its own diacritics and spelling, one continuous
  stretch of at most 300 characters (no ellipsis, no joining of separate stretches);
- `ozet`: what the point says, in Turkish, at most 30 words;
- `iddia`: the claims it bears on, e.g. ["I3"], or [];
- `iliski`: destek (supports a claim) | genisletme (extends one) | karsi (contradicts or limits one) | yeni (no
  claim covers it).
For a hadith add `derece` as its header shows it (e.g. "sahih=True graded_by=Buhârî").

A segment with nothing on the target ayah or the claims gets exactly one line:
`{"seg": "LOCATOR", "bos": true, "neden": "<why, a few Turkish words>"}`.

Every segment listed in the job header must appear in your output, as cards or as its bos line: check the list
before you write.

## Output
Write all lines to cards.jsonl in one Write, in the order of your material. Nothing else.

## Job
Target: 1:1  —  بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
Your call directory: /Volumes/aro/projects/prose_generation/enrichment/v2/work/s001/okuma.1_1/c05
Output: /Volumes/aro/projects/prose_generation/enrichment/v2/work/s001/okuma.1_1/c05/cards.jsonl
Segments in your material (17; every one must appear in your output, as cards or as one bos line): BIQAI-FULL:v1p25, BIQAI-FULL:v1p27, BIQAI-FULL:v1p28, BIQAI-FULL:v1p29, BIQAI-FULL:v1p31, DURR:1:1, DURR-FULL:v1p19#2, DURR-FULL:v1p20, DURR-FULL:v1p21, DURR-FULL:v1p22, DURR-FULL:v1p23, DURR-FULL:v1p24, DURR-FULL:v1p27, DURR-FULL:v1p28, DURR-FULL:v1p29, IBNABIHATIM:v1p25, IBNABIHATIM:v1p26

## Material files (read every one, completely, in order; one Read each, no offset or limit)
- /Volumes/aro/projects/prose_generation/enrichment/v2/work/s001/okuma.1_1/c05/m01.md
- /Volumes/aro/projects/prose_generation/enrichment/v2/work/s001/okuma.1_1/c05/m02.md
- /Volumes/aro/projects/prose_generation/enrichment/v2/work/s001/okuma.1_1/c05/m03.md
