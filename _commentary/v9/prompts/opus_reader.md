# V9 whole-package lane — ayah reading brief

You write one Turkish reading of one Quranic ayah from a prepared package. You work alone and in one
session: you read the whole package, discover, synthesize and write. Nothing else is supplied.

First read `_commentary/v9/prompts/writer_rules.md` completely: it defines what the reading is for, what
enters it, its shape, style, tags and the two checking commands. Everything below adds to it.

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
  concept words shared with branches in nearby ayat. Components, not images.
- `07_fatiha.md` — the Fatiha (recited in every salah) with focus × Fatiha branch pairs. A standing lens.
- `08_surah.md` — the whole host surah.
- `09_inter_ayah.md` — earlier reviewed inter-ayah rows (labels are not decisions), with target text.
- `10_leads.md` — reader walks when present.
- `11_people.md` — every other ayah naming the same people (proper nouns of the focus ayah).

Read long files in consecutive chunks with `offset`, each as large as the Read tool allows, until the
end. Do not skip parts. Do not read anything outside the package directory, the two brief files and the
Quran text you are given; do not consult earlier commentary outputs in this repository.

## Working notes (few tool calls)

Every tool call re-sends your whole context, so calls are the main cost. Keep notes in your head while
reading and write `notes.md` twice only: once after `05_usage.md` and once after `10_leads.md` (the second
write replaces the file with the full notes). The notes list candidate findings with their two keys, the
threads you plan, and which images join which threads.

## Outputs (paths given in the launch message)

- `notes.md` — the working notes above.
- `S_A.reading.tr.md` — the reading.
- `S_A.harvest.md` — accountability: every HFT record, the pairs/concepts/rows you used (with the section
  they landed in and the image the prose states), notes-only items, and not-used items grouped by reason.

Then run, from the repository root, `python3 _commentary/v9/verify_ar.py <reading> <package dir> --fix` and
`python3 _commentary/v5/validate_prose.py <reading>`, fix what they report, and run them once more. If a
problem remains after that, list it in your final message instead of looping.
