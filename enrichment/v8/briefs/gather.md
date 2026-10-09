<!-- agent {AGENT} | model {MODEL} | effort {EFFORT} -->
# TASK: gather the tradition's notes for every paragraph of the {AYAH} page

## ROLE
A frozen Turkish commentary page on {AYAH} makes claims paragraph by paragraph. A later writer will place short blocks under the paragraphs saying what the Islamic tradition says about those claims. Your job is to bring that writer, for each paragraph, **every note that bears on what the paragraph says**, so the writer does not have to search. You do not write commentary and you do not judge which view is right. Do not spawn agents. Do not change the task.

**Over-include.** A note you leave out is lost to the writer; an extra note costs little. When in doubt, include it. Do not drop a note because other notes make the same point: the writer counts who holds a view.

## YOUR MATERIAL AND THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens.** If an output looks cut (no `<<part K ends …>>` or `<<end …>>` line for a part, or a list stops mid-line), run it once more.

| Command | What it prints |
|---|---|
| `cat enrichment/v8/work/{RUN}/inputs/page.pK.txt` (K = 0 … {LAST_PAGE}) | the page, paragraphs numbered `[¶n]` |
| `cat enrichment/v8/work/{RUN}/inputs/focus.pK.txt` (K = 0 … {LAST_FOCUS}) | every note on {AYAH}: `[ID] SOURCE d.DEATH · speaker · stance · claim «exact words»` |
| `python3 -B enrichment/v8/q.py {RUN} luna catalog V [V …]` | per verse: its text, how many notes, how many carry each verse word, which verses the notes name, how many notes elsewhere name it |
| `python3 -B enrichment/v8/q.py {RUN} luna notes V [--word W] [--grep REGEX] [--source SRC] [--page N]` | notes on verse V, 25 per page, filtered by a verse word, a regex over claim and exact words, or a source |
| `python3 -B enrichment/v8/q.py {RUN} luna find REGEX [--verse V] [--page N]` | notes on any verse whose claim or exact words match (Arabic is matched without vowels); without `--verse`, counts per verse |
| `python3 -B enrichment/v8/q.py {RUN} luna links A B` | notes on A that name B, and on B that name A |
| `python3 -B enrichment/v8/q.py {RUN} luna note ID [ID …]` | full notes |
| `python3 -B enrichment/v8/q.py {RUN} luna check-packet` | checks your output and lists every problem |

Claims are English; exact words are mostly Arabic. Search both ways when it matters (e.g. `--grep "rescue|نجا"`). No other commands, files, web or repository search.

## PROCEDURE
**Step 1.** Read the page parts, then the focus-note parts, each once, in order.

**Step 2.** For each paragraph ¶1–¶{LASTP}, list for yourself what it claims that the tradition could speak to: the senses it gives a word, what it says a word refers to, what it says about each verse it cites, the connections it draws between verses, and what it implies without citing (a sense or a link the paragraph suggests). The page cites these verses per paragraph:
{CITES}

**Step 3.** Gather, paragraph by paragraph:
- **{AYAH} itself:** pick from the focus notes you read every note that bears on the paragraph (cite its id; you need not search for these, but you may use `notes {AYAH} --grep …` to check a point).
- **Each cited verse:** start with `catalog`, then open the notes that bear on what the paragraph says about that verse (`notes V --word …`, `--grep …`, more pages when needed), and run `links {AYAH} V`.
- **Implicit claims and connections:** use `find` across all verses (for example a word sense the paragraph attaches to {AYAH} may be discussed under another verse).
- A note may bear on several paragraphs: list it under each.

**Step 4.** Write the whole file `enrichment/v8/work/{RUN}/gather/packet.jsonl` in one write, exactly one line per paragraph, in order:
```
{"p":1,"items":[{"id":"<note id>","why":"one short English line: which claim of ¶1 it bears on"}],"searched":"the queries you ran for ¶1, briefly"}
```
A paragraph with nothing to bring has `"items":[]` and its `searched` line.

**Step 5.** Run `check-packet` until it prints `OK` (fix only what it names). Then stop and reply with the number of notes per paragraph.
