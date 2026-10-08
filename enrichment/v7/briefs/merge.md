<!-- agent {AGENT} | model {MODEL} | effort {EFFORT} -->
# TASK: consolidated views for {AYAH}, slice {SLICE} ({ROWS} notes in {NCELLS} cells from {SOURCES} sources)

## ROLE
Earlier readers took notes on every source that comments on {AYAH} ({VERSE}). Each note has an id, the source, the person who holds the view, the source author's stance, and a one-line claim. The notes are grouped into **cells**: one word of the verse (or the whole verse) × one kind of point (meaning, grammar, rhetoric, readings, referent, reports, sciences, interpretation, theology, law, links, inward). Many sources repeat the same view. Your job: inside each cell, group the notes into **distinct views**, each view once, so a writer can see every position, who holds it, and where they disagree. You do not drop anything and you do not add anything. Do not spawn agents. Do not change the task.

## THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens.**

| Command | What it does |
|---|---|
| `cat enrichment/v7/work/{RUN}/tier2/rows/{KEY}.{SLICE}.pK.txt` (K = 0 … {LAST}) | prints part K of your notes (at most 10,000 characters) |
| `python3 -B enrichment/v7/merge.py check {RUN} --model {TAG} --ayah {AYAH} --slice {SLICE}` | checks your output file and lists every problem |

No other commands, files, web or repository search.

## PROCEDURE
**Step 1.** Read parts 0 to {LAST} in order, each once. Each cell starts with `### cell <CELL-ID> · word · type · N notes`, then lines `[ID] SOURCE, d. … · speaker | stance | claim | mentions …`, oldest author first. If a part looks cut (no `<<part K ends …>>` or `<<end of rows>>` line), run it once more.

**Step 2.** Group each cell's notes into views (see RULES).

**Step 3.** Write the whole file `enrichment/v7/work/{RUN}/tier2/out/{TAG}/{KEY}.{SLICE}.jsonl` in one write.

**Step 4.** Run the check. If it lists problems, fix them and run it again, until it prints `OK`. Then stop and reply with the number of views.

## RULES
- **Views stay inside their cell.** Every view names one cell and takes notes only from that cell. Never merge notes of different cells, even when they make a similar point; the writer sees the cells side by side.
- **Same point, same view.** Notes in a cell that make the same point go into one view, whatever source or transmitter they come from.
- **Different point, different view.** A note that adds a distinct detail, argument, reason or nuance gets its own view, or the view's text must state that detail. Never let a merge hide a detail. When in doubt, keep it separate.
- **Disagreements stay visible.** Competing views are separate views. When a source prefers or rejects a view, its note goes in that view (the script shows the stance); say in `note` what the disagreement turns on, when the notes give it.
- **Every id at least once.** An id may appear in more than one view of its cell when the note makes more than one point. A note that seems to sit in the wrong cell stays in its cell; you may say so in `note`.
- **Do not judge** which view is right, and do not add knowledge that is not in the notes.

## OUTPUT: one JSON object per line, one line per view, cell by cell
```
{"cell":"w1-referent","view":"The fig and olive are the familiar fruits people eat and press for oil.","rows":["TAB-FULL:v24p501#2/r1","THALABI:v10p238#3/r1"],"note":""}
```
| Field | Rule |
|---|---|
| `cell` | the cell id exactly as in its header |
| `view` | the point in English, at most 60 words, with every detail the grouped notes share |
| `rows` | every note id this view covers, copied exactly |
| `note` | optional: what a disagreement turns on, or a detail some of the grouped notes add |
