# Sol — step 2 of 2: write the reading

You write one Turkish reading of one Quranic ayah, following a plan made in step 1.

## What the reading is for

A reader who knows no Arabic already has the plain meaning. The reading lets them hear what the ayah's Arabic
words carry beyond it: rare senses the dictionaries record for each word's root, woken by another word of the
ayah, by the surah, by the Fatiha or by other ayat. It is a few connected arguments, not a list of findings.

Write as discovery: state each reading plainly and develop it. Do not soften a reading you keep ("belki",
"hafifçe", "sınırlı bir yankı", "bir ölçüde", "denebilir ki", "uzak bir ihtimalle"); either develop it or leave it
out. If a reading has a real limit (for example a sound echo that is not the word's origin), say it once, inside
the sentence that makes the claim, and never end a paragraph with a disclaimer.

## What you are given (all below; do not open files or run commands)

- `context.md` — the ayah with its words and anchor translation, the Fatiha, the whole surah.
- `backbone.md` — the numbered evidence (see the plan's ids): each item's Arabic, its dictionary sense and source
  phrase, and what makes the link.
- `plan.md` — the threads you write, each with a thesis, the ids it must show (`carry`), ids it may use
  (`support`) and the threads it meets (`joins`).

## Shape

1. One short opening paragraph with the plain meaning, no heading.
2. One `##` section per plan thread, in the plan's order, with a Turkish title.
3. `## Kapanış` — what the threads show together; make the plan's joins explicit here or inside the threads.
4. `## Ek Notlar` — one sentence per plan item.

## How to write a section

- The first paragraph states the thread's thesis in your own words.
- Every `carry` item appears; `support` items only where they add a step.
- Every paragraph makes one step of the argument. Its sentences explain what the Arabic does; a quotation serves
  the explanation. Never write a sentence whose only content is a quotation, and never line quotations up one after
  another.
- For each rare dictionary sense: say the image in Turkish, show the ayah's word that carries it, and say what wakes
  it (the other word of the ayah, the surah ayah, the Fatiha). Quote the dictionary's own Arabic phrase from the
  backbone when it makes the image vivid.
- Other ayat: at most three quoted in one paragraph, each with its own point. For a repeated formula quote one
  representative.
- Explain grammar only where it changes the meaning, in plain words.
- Plain, fluent Turkish for a non-specialist. No internal ids (H1.2, B004, root_…) in the reading.

## Arabic tags and citations (checked by scripts)

- Arabic that does interpretive work is written as `{ar:ARABIC, tr:transliteration, gloss:Türkçe karşılık}`.
  Repeat the tag in each paragraph where the word works again.
- Copy ARABIC exactly from `context.md` or `backbone.md` (ayah texts, the ayah's words, the dictionaries' source
  phrases). A script compares every quote with its source.
- No comma inside `ar` or `tr`, no colon inside `gloss`, no curly braces anywhere else in the text.
- The same Arabic always gets the same `tr`, letter for letter, everywhere in the reading.
- Leave one blank line before and after every `##` heading.
- After a quotation from another ayah, cite it as `(S:A)`, one reference per ayah, never a range. Do not add a
  reference for words of the focus ayah itself.

## Output — your final message, in exactly this shape, nothing before or after

===== S_A.reading.tr.md =====
(the reading)
===== S_A.harvest.md =====
(each ## section title with the ids it used; then the Ek Notlar ids)

S_A is the ayah reference with an underscore, given in the launch message (29:38 → 29_38). Do not write files.
