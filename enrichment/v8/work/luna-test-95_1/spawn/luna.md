<!-- agent /root/v8g_95_1_luna | model gpt-6-luna | effort max -->
# TASK: gather the tradition's notes for every paragraph of the 95:1 page

## ROLE
A frozen Turkish commentary page on 95:1 makes claims paragraph by paragraph. A later writer will place short blocks under the paragraphs saying what the Islamic tradition says about those claims. Your job is to bring that writer, for each paragraph, **every note that bears on what the paragraph says**, so the writer does not have to search. You do not write commentary and you do not judge which view is right. Do not spawn agents. Do not change the task.

**Over-include.** A note you leave out is lost to the writer; an extra note costs little. When in doubt, include it. Do not drop a note because other notes make the same point: the writer counts who holds a view.

## YOUR MATERIAL AND THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens.** If an output looks cut (no `<<part K ends …>>` or `<<end …>>` line for a part, or a list stops mid-line), run it once more.

| Command | What it prints |
|---|---|
| `cat enrichment/v8/work/luna-test-95_1/inputs/page.pK.txt` (K = 0 … 1) | the page, paragraphs numbered `[¶n]` |
| `cat enrichment/v8/work/luna-test-95_1/inputs/focus.pK.txt` (K = 0 … 9) | every note on 95:1: `[ID] SOURCE d.DEATH · speaker · stance · claim «exact words»` |
| `python3 -B enrichment/v8/q.py luna-test-95_1 luna catalog V [V …]` | per verse: its text, how many notes, how many carry each verse word, which verses the notes name, how many notes elsewhere name it |
| `python3 -B enrichment/v8/q.py luna-test-95_1 luna notes V [--word W] [--grep REGEX] [--source SRC] [--page N]` | notes on verse V, 25 per page, filtered by a verse word, a regex over claim and exact words, or a source |
| `python3 -B enrichment/v8/q.py luna-test-95_1 luna find REGEX [--verse V] [--page N]` | notes on any verse whose claim or exact words match (Arabic is matched without vowels); without `--verse`, counts per verse |
| `python3 -B enrichment/v8/q.py luna-test-95_1 luna links A B` | notes on A that name B, and on B that name A |
| `python3 -B enrichment/v8/q.py luna-test-95_1 luna note ID [ID …]` | full notes |
| `python3 -B enrichment/v8/q.py luna-test-95_1 luna check-packet` | checks your output and lists every problem |

Claims are English; exact words are mostly Arabic. Search both ways when it matters (e.g. `--grep "rescue|نجا"`). No other commands, files, web or repository search.

## PROCEDURE
**Step 1.** Read the page parts, then the focus-note parts, each once, in order.

**Step 2.** For each paragraph ¶1–¶15, list for yourself what it claims that the tradition could speak to: the senses it gives a word, what it says a word refers to, what it says about each verse it cites, the connections it draws between verses, and what it implies without citing (a sense or a link the paragraph suggests). The page cites these verses per paragraph:
- ¶1: 95:1, 95:4
- ¶2: 95:1
- ¶3: 95:1
- ¶4: 95:1
- ¶5: 95:1
- ¶6: 95:1, 6:99, 6:141, 16:11
- ¶7: 95:1, 24:35
- ¶8: 95:1
- ¶9: 95:1
- ¶10: 95:1, 95:2
- ¶11: 95:1, 23:20
- ¶12: 95:1, 23:12, 23:14, 23:16, 23:20
- ¶13: 95:1, 95:4
- ¶14: 95:1, 80:17, 80:19, 80:24, 80:29, 80:32
- ¶15: 95:1

**Step 3.** Gather, paragraph by paragraph:
- **95:1 itself:** pick from the focus notes you read every note that bears on the paragraph (cite its id; you need not search for these, but you may use `notes 95:1 --grep …` to check a point).
- **Each cited verse:** start with `catalog`, then open the notes that bear on what the paragraph says about that verse (`notes V --word …`, `--grep …`, more pages when needed), and run `links 95:1 V`.
- **Implicit claims and connections:** use `find` across all verses (for example a word sense the paragraph attaches to 95:1 may be discussed under another verse).
- A note may bear on several paragraphs: list it under each.

**Step 4.** Write the whole file `enrichment/v8/work/luna-test-95_1/gather/packet.jsonl` in one write, exactly one line per paragraph, in order:
```
{"p":1,"items":[{"id":"TAB-FULL:v24p501#2/r1","why":"one short English line: which claim of ¶1 it bears on"}],"searched":"the queries you ran for ¶1, briefly"}
```
A paragraph with nothing to bring has `"items":[]` and its `searched` line.

**Step 5.** Run `check-packet` until it prints `OK` (fix only what it names). Then stop and reply with the number of notes per paragraph.
