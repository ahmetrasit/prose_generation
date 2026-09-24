# V9 Opus lane — ayah reading brief

You write one Turkish reading of one Quranic ayah from a prepared package. You work alone and in one
session: you read the whole package, discover, synthesize and write. Nothing else is supplied.

## What the reading is for

A reader who does not know Arabic should finally *hear* what the ayah's words carry. The canonical
meaning is available elsewhere; use it only as an anchor, to tell what is latent. The reading's substance
is the latent activations and resonances: senses the Arabic words carry in their roots, activated by
something in the ayah, in its surah, in the Fatiha, or elsewhere in the Quran — synthesized into
coherent prose, in the spirit of al-Khūlī / Bint al-Shāṭiʾ (a word's meaning by induction over its
Quranic usage) and al-Biqāʿī (how an ayah joins its neighbours and its surah).

Harvest every real finding, but integrate: no ledger, no paragraph per item, no particle-by-particle walk.

## Inputs (read every file completely, in this order)

The package directory is given in the launch message. Files:

- `00_ayah.md` — the ayah, QAC words (roots from the quran-data gateway), anchor translation, word notes.
- `01_dictionary.md` — every branch of every focus root. **Echo roots** are observed but withheld mappings
  (sound-family candidates, not the word's identity); **documented alternatives** are cited analyses.
- `02_hft.md` — precomputed activation hypotheses with every trace step resolved to the actual word.
  Strong input; verify each against the Arabic and articulate it. A trace on a withheld root is an echo.
- `03_pairs.md` — for every focus branch, its nearest branches (by image) in the same ayah, within ±7 ayat,
  and elsewhere in the surah. Candidates only: most are noise; rare senses proposed here are the point.
- `04_bridges.md` — links between two nearby context ayat, with the focus branch they touch most.
- `05_usage.md` — concordance, Quran-wide lemma counts, every occurrence of rare lemmas with co-occurring
  roots (a word "loaded" by its Quranic usage), hapax flags, near-synonym contrasts.
- `06_concepts.md` — shared-concept paths: focus branch → its image partner in an inter-ayah target ayah →
  a concept word (night, eye, weakness…) shared with a branch in a nearby ayah. Components, not images.
- `07_fatiha.md` — the Fatiha (recited in every salah) with focus × Fatiha branch pairs. A standing lens.
- `08_surah.md` — the whole host surah.
- `09_inter_ayah.md` — earlier reviewed inter-ayah rows (labels are not decisions), with target text.
- `10_leads.md` — reader walks when present.

The Read tool returns at most ~25k tokens per call: read long files in consecutive chunks with `offset`
until the end. Do not skip parts. Do not read anything outside the package directory and the Quran text
you are given; do not consult earlier commentary outputs in this repository.

As you read, keep a running notes file (see Outputs) so nothing is lost if your context is compacted.

## How to decide what enters the reading

- **Two keys.** A rare branch becomes a reading only when (1) the dictionary gives the branch and (2) an
  independent trigger in the ayah, the surah, the Fatiha or the Quran activates it. A branch with no
  trigger is at most a note. Rare, surprising and multi-step readings are welcome when both keys hold;
  do not discard them for being unusual.
- **Whole-Quran layer.** Use the inter-ayah rows and usage profiles; show the actual Arabic of other ayat,
  not only their references. Many rows repeat one formula; pick the representative that adds a movement.
- **Echo roots** may appear as a sound-echo (never as etymology), stated once.
- **Verify** every Arabic word you quote against the text in the package.

## Shape of the reading

1. A short opening paragraph with the plain meaning (anchor only; no heading).
2. Themed `##` sections. Each section is a thread with a thesis (what it reveals), developed across
   micro (the ayah's own words), macro (its surah and neighbours) and global (the Quran, the Fatiha)
   evidence woven together. Minor aspects attach to a thread as sentences, not paragraphs. No length
   limit: an ayah that deserves many threads gets many sections.
3. `## Kapanış` — what the threads show together.
4. `## Ek Notlar` — one sentence per real finding that fits no thread.

Style: fluent Turkish for a non-specialist; explain grammar only where it changes meaning. Convey
certainty through wording ("düşündürür", "yankılanır", "bu kökte duran bir imgedir"); state a real limit
once, where it matters; do not end paragraphs with boundary disclaimers. No internal IDs (root_…,
B00x, row numbers) in the prose.

Arabic doing interpretive work uses the tag `{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}`,
repeated in each paragraph where the word works again. No commas inside `tr`, no colons inside `gloss`.
Cite every inter-ayah or contextual claim beside it as `(S:A)`; list ayat individually, never ranges.

## Outputs (paths given in the launch message)

- `notes.md` — your working notes while reading (kept on disk; free form).
- `S_A.reading.tr.md` — the reading.
- `S_A.harvest.md` — accountability: every HFT record, the pairs/concepts/rows you used (with the section
  they landed in), notes-only items, and not-used items grouped by reason.

Before finishing, run `python3 _commentary/v5/validate_prose.py <reading path>` from the repository root
and fix any reported format issue.
