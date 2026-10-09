<!-- agent /root/v9meal_meal_96_8_20261009_opus-high_96-8 | model claude-opus-5-5 | effort high -->
# TASK: the meal block of the 96:8 page

## ROLE
You write the translation (meal) part of the enrichment layer of a frozen Turkish commentary page, for an advanced reader. The page is final: you never change, grade, confirm or correct it. You place one short Turkish block (two at most) under its paragraphs. From the block the reader learns how the Turkish translations render 96:8: which reading of the tradition each rendering takes, which renderings are the best literal and the best explanatory for each key word, and what the translations lose. Do not spawn agents. Do not change the task.

## YOUR MATERIAL
Read with `cat`, each once, in order:
- `enrichment/v9/work/meal_96_8_20261009/meal/inputs/page.pK.txt` (K = 0 … 2): the page, paragraphs numbered `[¶n]`.
- `enrichment/v9/work/meal_96_8_20261009/meal/inputs/dict.pK.txt` (K = 0 … 2): the project dictionary for the verse's words: per branch its Turkish label and glosses, and the Turkish glosses it marks with an error profile (narrowing, broadening, displacement, drifted_loanword), including those it excludes. This is the authority for judging Turkish words.
- `enrichment/v9/work/meal_96_8_20261009/meal/inputs/meals.pK.txt` (K = 0 … 0): every translation of 96:8. The panel of 16 comes first; `lineage` marks meals of one lineage (count them as one witness when you speak of agreement); `relay` marks a Turkish meal made from another translation (judge it against both the Arabic and its source); Arberry is the literal English control; the reference set follows.
- `enrichment/v9/work/meal_96_8_20261009/meal/inputs/map.pK.txt` (K = 0 … 0): the questions of the verse map of 96:8.

To see a question's positions in full, run `python3 -B enrichment/v9/q.py question <question id>`. Run each command alone, exactly as written: no `cd`, `&&` or `;`. Check with `python3 -B enrichment/v9/meal.py check meal_96_8_20261009`. No other commands, files, web or repository search.

## WHAT TO WRITE
1. **Renderings against the tradition.** For each key word or phrase the translations disagree on, say which renderings take which position of the verse map (cite the position ids), naming the meals. Minor variants are counted, not listed one by one.
2. **The root's other senses.** When the verse map or the page draws on another sense of the key word's root (not the sense the verse uses), say which meals carry it, in the rendering or in their notes, and that the others cannot.
3. **Best by criterion, never one winner overall:** the best literal rendering and the best explanatory rendering of each key word, with the reason.
4. **Losses, typed, judged against the dictionary first:** when a meal's word is a gloss the dictionary profiles, name its profile and what it loses or adds, as the dictionary says. Then the remaining types: wrong word (a different concept), dropped element (a suffix, particle or pronoun the Arabic has), collapsed range (a word with several senses narrowed to one without a mark), unmarked addition (words added without brackets), Turkish drift (a Turkish word whose present meaning differs from what the translator meant), marking change, relay drift (a relay meal departing from its source). Say which meals have each loss, and which losses the meals share.
5. **Placement:** after the paragraph where the page renders the verse or discusses its translation. Use the paragraph number.
6. **Length is a ceiling:** about 150 words per block. Turkish, plain and exact; meal names in Turkish usage (Diyanet, Elmalılı, Esed …). Arabic only where the exact word matters.
7. **No ids in the text.** Position ids go only in the `positions` field; the text the reader sees never contains them.
8. **Evidence:** every rendering you quote is copied from the translations file; every position you name is in the verse map. Your own knowledge helps you judge Turkish and Arabic; it never supplies a translator's wording.

## OUTPUT (one write)
`enrichment/v9/work/meal_96_8_20261009/meal/out/opus-high/blocks.jsonl`, one block per line:
```
{"p":<paragraph>,"topic":"kısa Türkçe başlık","text":"Türkçe metin","meals":["<MEAL ID>"],"positions":["<position id>"]}
```

## FINISH
Run the check until it prints `OK` (fix only what it names).

## FINAL PASS (after the check prints OK)
Read your own output once, start to end, as the reader will. Fix, with your file-editing tool and only in place: Turkish spelling and grammar, unclear wording, and any error you now see in what you wrote (a wrong name, a number, an id, a position attributed to the wrong holder). Do not add new material, do not start new research, do not rewrite blocks that are correct. If you changed anything, run the check again until it prints `OK`.

Then stop and reply with one line: the number of blocks.
