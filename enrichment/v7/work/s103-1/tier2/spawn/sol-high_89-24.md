<!-- agent /root/v7m_s103-1_sol-high_89-24 | model gpt-6-sol | effort high -->
# TASK: consolidated views for 89:24 (76 notes from 32 sources)

## ROLE
Earlier readers took notes on every source that comments on 89:24 (يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى). Each note has an id, the person who holds the view, the source author's stance, and a one-line claim. Many sources repeat the same view. Your job: group the notes into **distinct views**, each view once, so a writer can see every position, who holds it, and where they disagree. You do not drop anything and you do not add anything. Do not spawn agents. Do not change the task.

## THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens** (set the shell tool's maximum output to 12,000 tokens).

| Command | What it does |
|---|---|
| `cat enrichment/v7/work/s103-1/tier2/rows/89-24.pK.txt` (K = 0 … 1) | prints part K of the notes (at most 10,000 characters) |
| `python3 -B enrichment/v7/merge.py check s103-1 --model sol-high --ayah 89:24` | checks your output file and lists every problem |

No other commands, files, web or repository search.

## PROCEDURE: follow in order
**Step 1.** Read parts 0 to 1 in order, each exactly once. Notes are grouped by source, oldest author first: `## SOURCE: author, d. … AH`, then lines `[ID] speaker | stance | claim | mentions …`. If a part looks cut (no `<<part K ends …>>` or `<<end of rows>>` line), run that same part once more.

**Step 2.** Group the notes into views (see RULES).

**Step 3.** Write the whole output file `enrichment/v7/work/s103-1/tier2/out/sol-high/89-24.jsonl` in one write with your file-writing tool.

**Step 4.** Run the check command. If it lists problems, fix them and run it again, until it prints `OK`. Do not stop while it still lists problems.

**Step 5.** Stop. Reply with the number of views.

## RULES
- **Same point, same view.** Notes that make the same point go into one view, whatever source or transmitter they come from. "Horses" from Ibn ʿAbbās in eight sources is one view with eight-plus ids.
- **Different point, different view.** A note that adds a distinct detail, argument, reason or nuance gets its own view, or the view's text must state that detail. Never let a merge hide a detail. When in doubt, keep it separate.
- **Disagreements stay visible.** Competing views are separate views under the same topic. When a source prefers or rejects a view, its note goes in that view (the script shows the stance); say in `note` what the disagreement turns on, when the notes give it.
- **Every id at least once.** An id may appear in more than one view when the note makes more than one point.
- **Topics:** short English labels that group related views, for example: meaning of the word, referent, grammar and syntax, readings (qirāʾāt), occasion and reports, inward (ishārī) readings, coherence with neighbouring verses, theology, law, modern readings, links to other verses. Use what fits the notes; keep views of one topic together and in a sensible order.
- **Do not judge** which view is right, and do not add knowledge that is not in the notes.

## OUTPUT: one JSON object per line, one line per view
```
{"topic":"referent","view":"The chargers are war horses running in battle.","rows":["TAB:100:1/r1","QURTUBI-FULL:v20p154/r3"],"note":""}
```
| Field | Rule |
|---|---|
| `topic` | short English label |
| `view` | the point in English, at most 60 words, with every detail the grouped notes share |
| `rows` | every note id this view covers, copied exactly |
| `note` | optional: what a disagreement turns on, or a detail some of the grouped notes add |

## CHECKLIST BEFORE STOPPING
- [ ] every note id appears in at least one view
- [ ] no detail was lost in a merge
- [ ] the check command prints `OK`
