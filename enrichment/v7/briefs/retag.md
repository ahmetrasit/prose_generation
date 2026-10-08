<!-- agent {AGENT} | model {MODEL} | effort {EFFORT} -->
# TASK: tag tier-1 notes, chunk {N} ({ROWS} notes on {NVERSES} verses)

## ROLE
Earlier readers took notes on Qurʾān commentaries: each note is one point a source makes about a verse, with an English claim and the source's exact words. Your job is to add two tags to every note, so a later writer can find notes by the verse word they concern and by kind of point. You do not change, judge or rewrite the notes. Do not spawn agents. Do not change the task.

## THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens.**

| Command | What it does |
|---|---|
| `cat enrichment/v7/work/{RUN}/retag/chunks/c{NN}.pK.txt` (K = 0 … {LAST}) | prints part K of your chunk (at most 10,000 characters) |
| `python3 -B enrichment/v7/retag.py check {RUN} --model {TAG} --chunk {N}` | checks your output file and lists every problem |

No other commands, files, web or repository search.

## PROCEDURE
**Step 1.** Read parts 0 to {LAST} in order, each once. The chunk starts with the text of every verse it concerns, then the notes, grouped by verse: `[ID] verses … | claim «exact words»`. If a part looks cut (no `<<part K ends …>>` or `<<end of chunk>>` line), run it once more.

**Step 2.** For every note, decide:
- `words`: the word or words of the verse the point is about, copied from the verse text at the top of the chunk (a phrase is fine). Use `["*"]` when the point concerns the whole verse rather than a word, or when you cannot tell. A note about several verses: copy words from the verse the point concerns.
- `type`: exactly one of:
{TYPES}

**Step 3.** Write the whole file `enrichment/v7/work/{RUN}/retag/out/{TAG}/c{NN}.jsonl` in one write, one line per note, in chunk order:
```
{"id":"TAB-FULL:v24p510#2/r6","words":["أَحْسَنِ تَقْوِيمٍۢ"],"type":"meaning"}
```

**Step 4.** Run the check. Fix only the lines it names (for a word problem, copy the word again from the verse text, or use `["*"]`) until it prints `OK`. Then stop and reply with the number of notes.
