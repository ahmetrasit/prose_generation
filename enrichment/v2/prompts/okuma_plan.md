# okuma (plan): the claims of one ayah page and the searches its reading needs

The project writes, around a frozen Turkish commentary on each ayah (the BASE), a page for an advanced reader that
holds every major information source. The work is staged. Readers will read, in full, every corpus segment tied to
this ayah and the classical lexica entries of its roots; one later call writes the page from what they find. Your
job is the plan for that reading: what the base claims, and what must be searched for because it is NOT tied to
this ayah in the corpus. You write no page content.

Read the material files completely: the numbered base (paragraphs marked [¶n]; blocks opening with
`<!-- v16:augment … para=n -->` are the base's own additions under ¶n), the ayah's words, the dictionary entries
of its roots, the Qur'anic usage of its lemmas, and the list of corpus sources.

## 1. Claims (iddialar)
List every claim of the base that a reader could check, or that the literature could confirm, extend or
contradict, in paragraph order. One claim per point; a paragraph usually holds several. For each:
- `paragraf`: its [¶n] (an augment block: the n of its para=n);
- `tur`: baglam (contextual meaning) | nahiv | belagat | lugat (a sense or branch) | imge (a latent lexical image,
  resonance, family image) | ayet_ayet | nazm | tarih | kelam_fikih | sentez (the base's own synthesis joining
  several of these);
- `ozet`: the claim in one Turkish sentence of at most 30 words, specific enough that a reader of a classical
  source can tell whether a passage bears on it;
- `anahtar`: the Arabic words (and Turkish words, for a Turkish-history claim) a search for it would use.

## 2. Searches (sorgular), at most 40
What the readers will not otherwise see, because the corpus ties it to no ayah or to other ayat:
- sahih hadith that explain the ayah's words or bear on a claim (`kind: "hadith"`, `sahih: true`): the direct
  Prophetic explanation first, then the hadith a paragraph is about;
- the wujūh books (MUQATIL-WUJUH, DAMGHANI, IBNJAWZI-NUZHA) for each content lemma;
- for every claim of tur imge or sentez: antecedents (a source already stating the image or part of it) in the
  maʿānī/gharīb works, WAHIDI-BASIT, MAWARDI, IBNJAWZI-ZAD, the lexica that cite ayat under a branch, KASHSHAF,
  JURJANI, the ishārī works, and the full tafsir texts at the lemma's other occurrences; and counter-evidence
  (FURUQ near-synonyms, a reading or grammar that blocks it) where one can be framed;
- Qur'an-by-Qur'an passages and readings at other ayat that a paragraph discusses;
- Turkish word history (NISANYAN, TDK, KUBBEALTI) for the meals' key words, when a paragraph or the meal review
  will turn on it;
- poetry or historical sources a paragraph's claim calls for.
Do not search for what is tied to this ayah already (its tafsir, maʿānī, readings and ishārī segments) or for the
lexica entries of its own roots: the readers get those in full.

Each search: `q` (words, all of which must occur; Arabic without diacritics is fine, each word matches as a
prefix), `src` (comma-separated source IDs from the list, or ""), `kind` (a kind from the list, or ""), `sahih`
(true only for hadith), `exact` (true to match whole words only), `n` (hits to keep, at most 10), `paragraf`
(list of ¶ numbers it serves), `neden` (why, one Turkish clause). Prefer several narrow searches over one broad
one: each hit is read in full, at a cost.

## Output
One JSON object, written to plan.json: `{"iddialar": [...], "sorgular": [...]}`. Nothing else.
