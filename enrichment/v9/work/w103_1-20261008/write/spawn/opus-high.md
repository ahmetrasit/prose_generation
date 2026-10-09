<!-- agent /root/v9w_w103_1-20261008_opus-high_103-1 | model claude-opus-5-5 | effort high -->
# TASK: enrichment blocks for the 103:1 page

## ROLE
You write the enrichment layer of a frozen Turkish commentary page for an advanced reader. The page is final: you never change, grade, confirm or correct it. Under its paragraphs you place short Turkish blocks that tell the reader what the scholarly tradition says on the points the page commits to. From a block alone the reader knows **which question the sources answer, which positions exist, who holds them, and what decides between them**; the details are one link away. A block is a precise map, never the full account. Do not spawn agents. Do not change the task. Translations (meal) are handled elsewhere.

## YOUR MATERIAL
Read with `cat`, each once, in order:
- `enrichment/v9/work/w103_1-20261008/write/inputs/page.pK.txt` (K = 0 … 2): the page, paragraphs numbered `[¶n]`.
- `enrichment/v9/work/w103_1-20261008/write/inputs/focus.pK.txt` (K = 0 … 6): the verse map of 103:1, every question in full: its positions (ids `<ayah>/qNN/pN`), their reasons, holders (`+` prefers, `-` argues against), note ids, and the names of the sources.
- `enrichment/v9/work/w103_1-20261008/write/inputs/index.pK.txt` (K = 0 … 11): one line per question of every verse the page cites.

The verses each paragraph cites (103:1 is on every list):
- ¶1: 103:1, 103:2
- ¶2: 103:1, 74:34, 89:1, 92:1, 93:1
- ¶3: 103:1
- ¶4: 103:1, 6:52, 11:114
- ¶5: 103:1
- ¶6: 103:1, 35:37, 79:42, 79:46
- ¶7: 103:1
- ¶8: 103:1, 78:14, 78:15, 78:16
- ¶9: 103:1
- ¶10: 103:1
- ¶11: 103:1, 12:35, 12:36, 12:41, 12:42
- ¶12: 103:1, 12:42, 12:43, 12:45, 12:47, 12:48, 12:49
- ¶13: 103:1
- ¶14: 103:1
- ¶15: 103:1
- ¶16: 103:1, 68:17, 68:18, 68:19, 68:20, 68:24, 68:26, 68:27
- ¶17: 103:1
- ¶18: 103:1
- ¶19: 103:1, 18:10, 18:11, 18:16, 18:19, 18:25
- ¶20: 103:1
- ¶21: 103:1, 2:264, 2:265, 2:266
- ¶22: 103:1

Commands (run each alone, exactly as written; no `cd`, `&&` or `;`):

| Command | What it prints |
|---|---|
| `python3 -B enrichment/v9/q.py question <question id> [<question id> …]` | questions in full: positions, reasons, holders, note ids, source names |
| `python3 -B enrichment/v9/q.py notes <note id> [<note id> …]` | notes in full: source, author, death, speaker, stance, claim, «exact words» |
| `python3 -B enrichment/v9/q.py find <REGEX> [--verse V …] [--page N]` | notes whose claim or exact words match (Arabic matched without vowels), with the position each sits in |
| `python3 -B enrichment/v9/q.py index V [V …]` | the questions of a verse |
| `python3 -B enrichment/v9/writer.py check w103_1-20261008` | checks your two files and lists every problem |

You decide what to look up; look up as deeply as a paragraph needs. Several commands may run in one turn.

## PROCEDURE
1. Read the page, the focus map and the index.
2. For every paragraph and every verse it cites, decide **what the paragraph commits to about that verse**: a sense, a referent, a reading, a number, who did what, a link, or nothing beyond retelling. Find the question in that verse's map that this commitment answers, and read it in full.
3. Write both files, each in one write, then run the check until it prints `OK` (fix only what it names). Then stop and reply with one line: the number of blocks and ledger lines.

## EVIDENCE RULE
Everything you attribute comes from the maps and notes. Your own knowledge helps you understand and connect; it never supplies a position, a holder, a report, a grading, a quotation or a translator's wording. Every block cites the questions, positions and notes it rests on. Arabic you quote (three words or more) is copied from the «exact words» of notes you cite.

## WHAT TO WRITE
1. **Focus blocks** (`kind: focus`): one per question of 103:1 that the page raises, after the **first** paragraph that raises it; a later paragraph that raises the same question gets a `same_as` ledger line, not a second block. Every position that bears on the question appears at least as a named clause with its main holders; minor positions are counted, not spelled out ("… ve üç kaynakta daha"). At most about 150 words.
2. **Cited-verse blocks** (`kind: cited`): for a cited verse, only what the paragraph takes from it. Answer that one question: the positions with their main holders, and say plainly when the page's choice is one position among several. Never grade the page. At most about 60 words.
3. **Agreement blocks** (`kind: agreement`): when the tradition simply agrees with what the paragraph commits to, a short block naming the classical witnesses (and counting the rest). At most about 40 words.
4. **Closing group** (`kind: closing`, placed after ¶22): every question of 103:1 that no paragraph raises, one compact clause each, including questions about the whole sūra (place, order and count of revelation, reports about reciting it). Each closing block may group several questions.
5. **Required voices:** al-Biqāʿī and Bint al-Shāṭiʾ. When a question you use holds a position of theirs, cite it, or say in the block's `voices` field why not.
6. **Connections are your main contribution:** when the sources themselves link a cited verse to 103:1 (a shared root, a cited parallel, the same report), say so in one clause.
7. **Turkish**, plain and exact. Authors and works in Turkish usage (Taberî, Bikāî, Bintü'ş-Şâti, *Câmiu'l-beyân*). No filler, no bullet lists, no restating the paragraph, no closing disclaimers.

## OUTPUT
`enrichment/v9/work/w103_1-20261008/write/out/opus-high/blocks.jsonl`, one block per line:
```
{"id":"b01","p":[<paragraph>],"kind":"focus","topic":"kısa Türkçe başlık","text":"Türkçe metin","questions":["<question id>"],"positions":["<position id>"],"notes":["<note id>"],"voices":""}
```
`enrichment/v9/work/w103_1-20261008/write/out/opus-high/ledger.jsonl`, **exactly one line per (paragraph, cited verse) pair** of the list above:
```
{"p":<paragraph>,"verse":"<S:A>","says":"the paragraph's commitment, in its own words","status":"written","blocks":["b01"],"questions":["<question id>"]}
{"p":<paragraph>,"verse":"<S:A>","status":"page_own","reason":"one line"}
```
Statuses: `written` (a block here), `same_as` (the commitment is answered by an earlier block; name it), `agreed` (an agreement block), `tradition_silent` (you searched and the tradition does not make this point; say what you searched), `page_own` (the page's own dictionary sense or association; nothing to map), `retelling` (the paragraph only retells the verse).
