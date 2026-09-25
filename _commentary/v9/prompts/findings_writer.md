# V9 findings lane — writer brief

You write one Turkish reading of one Quranic ayah from findings that a judge (Luna) recorded item by item.
You synthesize; you do not re-judge the whole package.

First read `_commentary/v9/prompts/writer_rules.md` completely: it defines what the reading is for, what
enters it, its shape, style, tags and the two checking commands. Everything below adds to it.

## Inputs (given in full in the launch message; the files live in the work directory)

1. `context.md` — the focus ayah with its words and anchor translation, the Fatiha, the whole host surah.
2. `findings.md` — every record Luna kept, grouped by focus word: readings (both keys, in Luna's
   judgement) with the trigger (Arabic and ayah), the image the reading hears, Luna's reason and, for
   dictionary branches, the branch sense; then notes (one key), one line each. The file ends with the full
   text of every cited ayah outside the surah and the Fatiha. Luna kept generously: many inter-ayah
   "readings" only restate the plain sense (the same people named elsewhere) — use those as whole-Quran
   evidence where they add a movement, not as latent readings.

You may open a worklist item (`W*.md` in the same directory, found by the record id) when you need a
record's full evidence. Do not read anything else.

## How to use the findings

- Luna finds well and judges unevenly. Verify every record against the Arabic before you use it: a reading
  whose trigger does not really call the branch becomes a note or is dropped (say why in the harvest).
- Every record marked reading must reach the prose unless you reject it on the evidence; notes may be used.
- Several records often carry one image from different sides (a pair, a concept path, a Fatiha pair on the
  same branch). Gather them into one thread; that is where synthesis happens.
- Concept-path records carry their image through a concept word (night, eye, road…): state that concept
  and the words it joins, per `writer_rules.md`.

## Outputs (the output directory is named in the launch message)

- `S_A.reading.tr.md` — the reading.
- `S_A.harvest.md` — every record id from `findings.md` with where it landed (section title) or why it was
  not used (rejected on evidence, with the reason; merged into another record; note left out).

Then run the two checking commands from `writer_rules.md`, using the work directory as the package
directory for `verify_ar.py`.
