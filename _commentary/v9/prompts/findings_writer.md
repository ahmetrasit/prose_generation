# V9 findings lane — writer brief

You write one Turkish reading of one Quranic ayah. A judge (Luna) has already worked through every
candidate the package offers and recorded what she found; you read the ayah's own dictionary entries
yourself, choose, and synthesize.

First read `_commentary/v9/prompts/writer_rules.md` completely: it defines what the reading is for, what
enters it, its shape, style and tags. Everything below adds to it.

## Inputs (the paths are given in the launch message)

1. `context.md` — the focus ayah with its words and anchor translation, the Fatiha, the whole host surah.
2. `01_dictionary.md` (package) — every branch of every focus root, with the dictionaries' own Arabic
   phrases. Read it yourself: what the entries show together — within one root and across the ayah's
   roots — is yours to find, and Luna's records do not replace it.
3. `findings.md` (work directory) — what Luna kept: (1) findings on the ayah's words, by focus word, with
   the image, her reason and the branch's dictionary sense; (2) whole-Quran parallels, compact; (3) shared
   triggers — the same Arabic word in one ayah hit by records of several roots; (4) the full text of the
   cited ayat.

Read every input completely. You may open a worklist item (`W*.md` in the work directory, by record id)
when you need a record's full evidence. Do not read anything else.

## How to use them

- Start from the ayah itself: its words, their order and grammar, their sounds, and what the dictionary
  entries say side by side. Then bring in Luna's findings, the surah, the Fatiha and the other ayat.
- Luna judged generously on purpose: most of `findings.md` is support material, not a list to cover.
  You decide what carries the reading. Build threads; each thread reaches the prose through its strongest
  evidence, and the rest of its records stay out. Several records often carry one image from different
  sides; gathering them is the synthesis.
- A record's Arabic has been checked by script. Reject a record only for a factual error you can state
  (a misread word, a wrong reference, a sense the dictionary does not give). That the other ayah does not
  name the image is not a reason: a latent reading is exactly an image the text does not spell out.

## Outputs (the output directory is given in the launch message)

- `S_A.reading.tr.md` — the reading.
- `S_A.harvest.md` — short: each `##` section with the record ids it rests on, and every record you
  rejected with its factual reason. A script records the rest.

Then run, from the repository root, `python3 _commentary/v9/verify_ar.py <reading> <work dir> --fix` and
`python3 _commentary/v5/validate_prose.py <reading>`, fix what they report, and run them once more. If a
problem remains after that, list it in your final message instead of looping.
