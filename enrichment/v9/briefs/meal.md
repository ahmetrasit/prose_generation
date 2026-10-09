<!-- agent {AGENT} | model {MODEL} | effort {EFFORT} -->
# TASK: the meal block of the {AYAH} page

## ROLE
You write the translation (meal) part of the enrichment layer of a frozen Turkish commentary page, for an advanced reader. The page is final: you never change, grade, confirm or correct it. You place one short Turkish block (two at most) under its paragraphs. From the block the reader learns how the Turkish translations render {AYAH}: which reading of the tradition each rendering takes, which renderings are the best literal and the best explanatory for each key word, and what the translations lose. Do not spawn agents. Do not change the task.

## YOUR MATERIAL
Read with `cat`, each once, in order:
- `enrichment/v9/work/{RUN}/meal/inputs/page.pK.txt` (K = 0 … {LAST_PAGE}): the page, paragraphs numbered `[¶n]`.
- `enrichment/v9/work/{RUN}/meal/inputs/meals.pK.txt` (K = 0 … {LAST_MEALS}): every translation of {AYAH}. The panel of 16 comes first; `lineage` marks meals of one lineage (count them as one witness when you speak of agreement); `relay` marks a Turkish meal made from another translation (judge it against both the Arabic and its source); Arberry is the literal English control; the reference set follows.
- `enrichment/v9/work/{RUN}/meal/inputs/map.pK.txt` (K = 0 … {LAST_MAP}): the questions of the verse map of {AYAH}.

To see a question's positions in full, run `python3 -B enrichment/v9/q.py question <question id>`. Run each command alone, exactly as written: no `cd`, `&&` or `;`. Check with `python3 -B enrichment/v9/meal.py check {RUN}`. No other commands, files, web or repository search.

## WHAT TO WRITE
1. **Renderings against the tradition.** For each key word or phrase the translations disagree on, say which renderings take which position of the verse map (cite the position ids), naming the meals. Minor variants are counted, not listed one by one.
2. **Best by criterion, never one winner overall:** the best literal rendering and the best explanatory rendering of each key word, with the reason.
3. **Losses, typed:** wrong word (a different concept), dropped element (a suffix, particle or pronoun the Arabic has), collapsed range (a word with several senses narrowed to one without a mark), unmarked addition (words added without brackets), Turkish drift (a Turkish word whose present meaning differs from what the translator meant), marking change, relay drift (a relay meal departing from its source). Say which meals have each loss, and which losses the meals share.
4. **Placement:** after the paragraph where the page renders the verse or discusses its translation. Use the paragraph number.
5. **Length is a ceiling:** about 150 words per block. Turkish, plain and exact; meal names in Turkish usage (Diyanet, Elmalılı, Esed …). Arabic only where the exact word matters.
6. **Evidence:** every rendering you quote is copied from the translations file; every position you name is in the verse map. Your own knowledge helps you judge Turkish and Arabic; it never supplies a translator's wording.

## OUTPUT (one write)
`enrichment/v9/work/{RUN}/meal/out/{TAG}/blocks.jsonl`, one block per line:
```
{"p":<paragraph>,"topic":"kısa Türkçe başlık","text":"Türkçe metin","meals":["<MEAL ID>"],"positions":["<position id>"]}
```

## FINISH
Run the check until it prints `OK` (fix only what it names). Then stop and reply with one line: the number of blocks.
