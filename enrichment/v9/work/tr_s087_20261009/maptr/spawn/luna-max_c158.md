<!-- agent /root/v9t_tr_s087_20261009_luna-max_c158 | model gpt-6-luna | effort max -->
# TASK: Turkish rendering of verse-map questions, chunk 158 (63 questions)

## ROLE
Verse maps record, in English, the questions the Islamic scholarly tradition answers about a Qur'an verse, and the positions (answers) the sources give, with their reasons. You render them in Turkish for an advanced Turkish reader. You translate; you never add, drop, merge, judge or explain. Do not spawn agents. Do not change the task.

## THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens.**

| Command | What it does |
|---|---|
| `cat enrichment/v9/work/tr_s087_20261009/maptr/chunks/c158.pK.txt` (K = 0 … 5) | prints part K of your questions, one JSON object per line |
| `python3 -B enrichment/v9/maptr.py check tr_s087_20261009 --chunk 158` | checks your output file and lists every problem |

No other commands, files, web or repository search.

## PROCEDURE
**Step 1.** Read parts 0 to 5 in order, each once. Each line is one question: `{"id","question","turns_on","positions":[{"id","position","reasons"}]}`. If a part looks cut (no `<<part K ends …>>` or `<<end of chunk>>` line at its end), run it once more.

**Step 2.** Write the whole file `enrichment/v9/work/tr_s087_20261009/maptr/out/luna-max/c158.jsonl` in one write: one line per question, same ids, every field rendered in Turkish.

**Step 3.** Run the check. If it lists problems, fix only what it names and run it again, until it prints `OK`. Then read your file once more as a Turkish reader would and fix spelling, grammar and unclear wording in place; run the check again if you changed anything. Then stop and reply with the number of questions.

## RULES
- **Everything, and only it.** Every sentence, name, number, verse reference and qualification of the English is in the Turkish. Nothing is added: no explanation, no gloss, no judgement. An empty English field stays empty.
- **Names in Turkish usage:** Taberî, Zemahşerî, Râzî, Kurtubî, İbn Kesîr, Bikāî, Bintü'ş-Şâti, İbn Abbas, Mücâhid, Katâde; works in italics are not needed. A name you do not know a Turkish form for keeps the transliteration of the English.
- **Arabic words and quoted Arabic stay as they are** (in Arabic script, or in the transliteration the English uses). Technical terms keep their usual Turkish form (kıraat, nüzul, nesih, mecaz).
- **Plain, exact Turkish.** Questions stay questions; a position stays one sentence or clause as in the English.
- **No ids in the text.** Ids appear only in the `id` fields.

## OUTPUT: one JSON object per line, one line per question
```
{"id":"<question id>","question":"Türkçe soru","turns_on":"","positions":[{"id":"<position id>","position":"Türkçe","reasons":"Türkçe"}]}
```
