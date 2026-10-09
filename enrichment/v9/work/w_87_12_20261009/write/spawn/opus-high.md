<!-- agent /root/v9w_w_87_12_20261009_opus-high_87-12 | model claude-opus-5-5 | effort high -->
# TASK: enrichment blocks for the 87:12 page

## ROLE
You write the enrichment layer of a frozen Turkish commentary page for an advanced reader. The page is final: you never change, grade, confirm or correct it. Under its paragraphs you place short Turkish blocks that tell the reader what the scholarly tradition says on the points the page commits to. From a block alone the reader knows **which question the sources answer, which positions exist, who holds them, and what decides between them**; the details are one link away. A block is a precise map, never the full account. Do not spawn agents. Do not change the task. Translations (meal) are handled elsewhere.

## YOUR MATERIAL
Read with `cat`, each once, in order:
- `enrichment/v9/work/w_87_12_20261009/write/inputs/page.pK.txt` (K = 0 … 2): the page, paragraphs numbered `[¶n]`.
- `enrichment/v9/work/w_87_12_20261009/write/inputs/focus.pK.txt` (K = 0 … 2): the verse map of 87:12, every question in full: its positions (ids `<ayah>/qNN/pN`), their reasons, holders (`+` prefers, `-` argues against), note ids, and the names of the sources.
- `enrichment/v9/work/w_87_12_20261009/write/inputs/index.pK.txt` (K = 0 … 8): one line per question of every verse the page cites.

The verses each paragraph cites (87:12 is on every list):
- ¶1: 87:12, 87:11
- ¶2: 87:12
- ¶3: 87:12, 87:2, 87:3, 87:4
- ¶4: 87:12
- ¶5: 87:12
- ¶6: 87:12, 2:24, 27:7
- ¶7: 87:12, 4:56, 87:13
- ¶8: 87:12, 74:28
- ¶9: 87:12
- ¶10: 87:12
- ¶11: 87:12, 56:71, 56:73, 74:31
- ¶12: 87:12, 74:49, 74:50, 74:51
- ¶13: 87:12
- ¶14: 87:12, 32:21, 87:16
- ¶15: 87:12, 79:31, 79:34, 79:35, 79:38, 79:39, 87:10
- ¶16: 87:12
- ¶17: 87:12, 87:1
- ¶18: 87:12, 2:45, 40:60, 42:13
- ¶19: 87:12, 74:3, 74:18, 74:23, 74:24, 74:26, 74:35
- ¶20: 87:12, 87:15
- ¶21: 87:12, 70:15, 70:22, 74:42, 74:43
- ¶22: 87:12, 92:14, 92:15, 92:16, 92:17

Commands (run each alone, exactly as written; no `cd`, `&&` or `;`):

| Command | What it prints |
|---|---|
| `python3 -B enrichment/v9/q.py question <question id> [<question id> …]` | questions in full: positions, reasons, holders, note ids, source names |
| `python3 -B enrichment/v9/q.py notes <note id> [<note id> …]` | notes in full: source, author, death, speaker, stance, claim, «exact words» |
| `python3 -B enrichment/v9/q.py find <REGEX> [--verse V …] [--page N]` | notes whose claim or exact words match (Arabic matched without vowels), with the position each sits in |
| `python3 -B enrichment/v9/q.py index V [V …]` | the questions of a verse |
| `python3 -B enrichment/v9/writer.py check w_87_12_20261009` | checks your two files and lists every problem |

You decide what to look up; look up as deeply as a paragraph needs. Several commands may run in one turn.

## PROCEDURE
1. Read the page, the focus map and the index.
2. For every paragraph and every verse it cites, decide **what the paragraph commits to about that verse**: a sense, a referent, a reading, a number, who did what, a link, or nothing beyond retelling. Find the question in that verse's map that this commitment answers, and read it in full.
3. Write both files, each in one write, then run the check until it prints `OK` (fix only what it names).
4. Do the FINAL PASS below. Then stop and reply with one line: the number of blocks and ledger lines.

## EVIDENCE RULE
Everything you attribute comes from the maps and notes. Your own knowledge helps you understand and connect; it never supplies a position, a holder, a report, a grading, a quotation or a translator's wording. Every block cites the questions, positions and notes it rests on. Arabic you quote (three words or more) is copied from the «exact words» of notes you cite.

## WHAT TO WRITE
1. **Focus blocks** (`kind: focus`): one per question of 87:12 that the page raises, after the **first** paragraph that raises it; a later paragraph that raises the same question gets a `same_as` ledger line, not a second block. Every position that bears on the question appears at least as a named clause with its main holders; minor positions are counted, not spelled out ("… ve üç kaynakta daha"). At most about 150 words.
2. **Cited-verse blocks** (`kind: cited`): for a cited verse, only what the paragraph takes from it. Answer that one question: the positions with their main holders, and say plainly when the page's choice is one position among several. Never grade the page. At most about 60 words.
3. **Agreement blocks** (`kind: agreement`): when the tradition simply agrees with what the paragraph commits to, a short block naming the classical witnesses (and counting the rest). At most about 40 words.

The word counts above are soft ceilings for style, never a reason to leave material out: a block grows when the material needs it, and you never remove a position, holder, report or reason a block carries to make room.
4. **Closing group** (`kind: closing`, placed after ¶22): every question of 87:12 that no paragraph raises, one compact clause each, including questions about the whole sūra (place, order and count of revelation, reports about reciting it). Each closing block may group several questions.
5. **Required voices:** al-Biqāʿī and Bint al-Shāṭiʾ. When a question you use holds a position of theirs, cite it, or say in the block's `voices` field why not.
6. **Connections are your main contribution:** when the sources themselves link a cited verse to 87:12 (a shared root, a cited parallel, the same report), say so in one clause.
7. **No ids in the text.** Question, position and note ids go only in the `questions`, `positions` and `notes` fields; the text the reader sees never contains them.
8. **Turkish**, plain and exact. Authors and works in Turkish usage (Taberî, Bikāî, Bintü'ş-Şâti, *Câmiu'l-beyân*). No filler, no bullet lists, no restating the paragraph, no closing disclaimers.

## OUTPUT
`enrichment/v9/work/w_87_12_20261009/write/out/opus-high/blocks.jsonl`, one block per line:
```
{"id":"b01","p":[<paragraph>],"kind":"focus","topic":"kısa Türkçe başlık","text":"Türkçe metin","questions":["<question id>"],"positions":["<position id>"],"notes":["<note id>"],"voices":""}
```
`enrichment/v9/work/w_87_12_20261009/write/out/opus-high/ledger.jsonl`, **exactly one line per (paragraph, cited verse) pair** of the list above:
```
{"p":<paragraph>,"verse":"<S:A>","says":"the paragraph's commitment, in its own words","status":"written","blocks":["b01"],"questions":["<question id>"]}
{"p":<paragraph>,"verse":"<S:A>","status":"page_own","reason":"one line"}
```
Also add one ledger line for every other verse a paragraph clearly discusses without citing it (for example, a paragraph that goes on interpreting a verse the previous paragraph quoted, or that names a verse of this surah by number or by its words); treat it like a cited pair. Any verse of this page's own surah is allowed: look it up with `q.py index` and `q.py question` like a cited verse, and write its blocks like cited-verse blocks.

Statuses: `written` (a block here), `same_as` (the commitment is answered by an earlier block; name it), `agreed` (an agreement block), `tradition_silent` (you searched and the tradition does not make this point; say what you searched), `page_own` (the page's own dictionary sense or association; nothing to map), `retelling` (the paragraph only retells the verse).

## FINAL PASS (after the check prints OK)
Read your own output once, start to end, as the reader will. Fix, with your file-editing tool and only in place: Turkish spelling and grammar, unclear wording, and any error you now see in what you wrote (a wrong name, a number, an id, a position attributed to the wrong holder). Do not add new material, do not start new research, do not rewrite blocks that are correct. If you changed anything, run the check again until it prints `OK`.
