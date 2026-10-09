<!-- agent /root/v9w_w_103_3_20261009_opus-high_103-3 | model claude-opus-5-5 | effort high -->
# TASK: enrichment blocks for the 103:3 page

## ROLE
You write the enrichment layer of a frozen Turkish commentary page for an advanced reader. The page is final: you never change, grade, confirm or correct it. Under its paragraphs you place short Turkish blocks that tell the reader what the scholarly tradition says on the points the page commits to. From a block alone the reader knows **which question the sources answer, which positions exist, who holds them, and what decides between them**; the details are one link away. A block is a precise map, never the full account. Do not spawn agents. Do not change the task. Translations (meal) are handled elsewhere.

## YOUR MATERIAL
Read with `cat`, each once, in order:
- `enrichment/v9/work/w_103_3_20261009/write/inputs/page.pK.txt` (K = 0 … 3): the page, paragraphs numbered `[¶n]`.
- `enrichment/v9/work/w_103_3_20261009/write/inputs/focus.pK.txt` (K = 0 … 5): the verse map of 103:3, every question in full: its positions (ids `<ayah>/qNN/pN`), their reasons, holders (`+` prefers, `-` argues against), note ids, and the names of the sources.
- `enrichment/v9/work/w_103_3_20261009/write/inputs/index.pK.txt` (K = 0 … 15): one line per question of every verse the page cites.

The verses each paragraph cites (103:3 is on every list):
- ¶1: 103:3, 103:2
- ¶2: 103:3
- ¶3: 103:3, 84:25, 95:5, 95:6
- ¶4: 103:3
- ¶5: 103:3, 9:6
- ¶6: 103:3, 6:80, 6:81, 6:82
- ¶7: 103:3
- ¶8: 103:3, 33:72
- ¶9: 103:3, 12:16, 12:17, 12:18
- ¶10: 103:3
- ¶11: 103:3, 29:57, 29:58, 29:59
- ¶12: 103:3, 18:103, 18:104, 18:105
- ¶13: 103:3
- ¶14: 103:3, 18:45, 18:46
- ¶15: 103:3, 2:27
- ¶16: 103:3
- ¶17: 103:3
- ¶18: 103:3
- ¶19: 103:3
- ¶20: 103:3, 2:132, 2:133, 6:151, 6:153
- ¶21: 103:3, 51:52, 51:53, 90:13, 90:17
- ¶22: 103:3
- ¶23: 103:3, 2:282, 2:283
- ¶24: 103:3, 6:152
- ¶25: 103:3, 10:32, 21:18
- ¶26: 103:3
- ¶27: 103:3, 69:1, 69:3
- ¶28: 103:3, 70:19, 70:20, 70:21, 70:22
- ¶29: 103:3
- ¶30: 103:3, 2:250, 7:124, 7:126
- ¶31: 103:3
- ¶32: 103:3
- ¶33: 103:3, 3:200, 18:28
- ¶34: 103:3, 2:175
- ¶35: 103:3, 39:10
- ¶36: 103:3, 30:60, 40:55
- ¶37: 103:3, 31:13, 31:14, 31:17
- ¶38: 103:3, 41:34, 41:35

Commands (run each alone, exactly as written; no `cd`, `&&` or `;`):

| Command | What it prints |
|---|---|
| `python3 -B enrichment/v9/q.py question <question id> [<question id> …]` | questions in full: positions, reasons, holders, note ids, source names |
| `python3 -B enrichment/v9/q.py notes <note id> [<note id> …]` | notes in full: source, author, death, speaker, stance, claim, «exact words» |
| `python3 -B enrichment/v9/q.py find <REGEX> [--verse V …] [--page N]` | notes whose claim or exact words match (Arabic matched without vowels), with the position each sits in |
| `python3 -B enrichment/v9/q.py index V [V …]` | the questions of a verse |
| `python3 -B enrichment/v9/writer.py check w_103_3_20261009` | checks your two files and lists every problem |

You decide what to look up; look up as deeply as a paragraph needs. Several commands may run in one turn.

## PROCEDURE
1. Read the page, the focus map and the index.
2. For every paragraph and every verse it cites, decide **what the paragraph commits to about that verse**: a sense, a referent, a reading, a number, who did what, a link, or nothing beyond retelling. Find the question in that verse's map that this commitment answers, and read it in full.
3. Write both files, each in one write, then run the check until it prints `OK` (fix only what it names).
4. Do the FINAL PASS below. Then stop and reply with one line: the number of blocks and ledger lines.

## EVIDENCE RULE
Everything you attribute comes from the maps and notes. Your own knowledge helps you understand and connect; it never supplies a position, a holder, a report, a grading, a quotation or a translator's wording. Every block cites the questions, positions and notes it rests on. Arabic you quote (three words or more) is copied from the «exact words» of notes you cite.

## WHAT TO WRITE
1. **Focus blocks** (`kind: focus`): one per question of 103:3 that the page raises, after the **first** paragraph that raises it; a later paragraph that raises the same question gets a `same_as` ledger line, not a second block. Every position that bears on the question appears at least as a named clause with its main holders; minor positions are counted, not spelled out ("… ve üç kaynakta daha"). At most about 150 words.
2. **Cited-verse blocks** (`kind: cited`): for a cited verse, only what the paragraph takes from it. Answer that one question: the positions with their main holders, and say plainly when the page's choice is one position among several. Never grade the page. At most about 60 words.
3. **Agreement blocks** (`kind: agreement`): when the tradition simply agrees with what the paragraph commits to, a short block naming the classical witnesses (and counting the rest). At most about 40 words.
4. **Closing group** (`kind: closing`, placed after ¶38): every question of 103:3 that no paragraph raises, one compact clause each, including questions about the whole sūra (place, order and count of revelation, reports about reciting it). Each closing block may group several questions.
5. **Required voices:** al-Biqāʿī and Bint al-Shāṭiʾ. When a question you use holds a position of theirs, cite it, or say in the block's `voices` field why not.
6. **Connections are your main contribution:** when the sources themselves link a cited verse to 103:3 (a shared root, a cited parallel, the same report), say so in one clause.
7. **No ids in the text.** Question, position and note ids go only in the `questions`, `positions` and `notes` fields; the text the reader sees never contains them.
8. **Turkish**, plain and exact. Authors and works in Turkish usage (Taberî, Bikāî, Bintü'ş-Şâti, *Câmiu'l-beyân*). No filler, no bullet lists, no restating the paragraph, no closing disclaimers.

## OUTPUT
`enrichment/v9/work/w_103_3_20261009/write/out/opus-high/blocks.jsonl`, one block per line:
```
{"id":"b01","p":[<paragraph>],"kind":"focus","topic":"kısa Türkçe başlık","text":"Türkçe metin","questions":["<question id>"],"positions":["<position id>"],"notes":["<note id>"],"voices":""}
```
`enrichment/v9/work/w_103_3_20261009/write/out/opus-high/ledger.jsonl`, **exactly one line per (paragraph, cited verse) pair** of the list above:
```
{"p":<paragraph>,"verse":"<S:A>","says":"the paragraph's commitment, in its own words","status":"written","blocks":["b01"],"questions":["<question id>"]}
{"p":<paragraph>,"verse":"<S:A>","status":"page_own","reason":"one line"}
```
Also add one ledger line for every other page verse a paragraph clearly discusses without citing it (for example, a paragraph that goes on interpreting a verse the previous paragraph quoted); treat it like a cited pair.

Statuses: `written` (a block here), `same_as` (the commitment is answered by an earlier block; name it), `agreed` (an agreement block), `tradition_silent` (you searched and the tradition does not make this point; say what you searched), `page_own` (the page's own dictionary sense or association; nothing to map), `retelling` (the paragraph only retells the verse).

## FINAL PASS (after the check prints OK)
Read your own output once, start to end, as the reader will. Fix, with your file-editing tool and only in place: Turkish spelling and grammar, unclear wording, and any error you now see in what you wrote (a wrong name, a number, an id, a position attributed to the wrong holder). Do not add new material, do not start new research, do not rewrite blocks that are correct. If you changed anything, run the check again until it prints `OK`.
