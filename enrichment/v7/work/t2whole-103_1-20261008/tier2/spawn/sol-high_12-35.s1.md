<!-- agent /root/v7m_t2whole-103_1-20261008_sol-high_12-35_s1 | model gpt-6-sol | effort high -->
# TASK: consolidated views for 12:35 (257 notes from 38 sources)

## ROLE
Earlier readers took notes on every source that comments on 12:35. Each note has an id, the source, the person who holds the view, the source author's stance, and a one-line claim. Many sources repeat the same view. Your job: group all the notes into **distinct views**, each view once, so a writer can see every position, who holds it, and where they disagree; and label every view with the verse words it is about and the kind of point it makes, so the writer can find it. You do not drop anything and you do not add anything. Do not spawn agents. Do not change the task.

The verse:
ثُمَّ بَدَا لَهُم مِّنۢ بَعْدِ مَا رَأَوُا۟ ٱلْءَايَٰتِ لَيَسْجُنُنَّهُۥ حَتَّىٰ حِينٍۢ

## THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens.**

| Command | What it does |
|---|---|
| `cat enrichment/v7/work/t2whole-103_1-20261008/tier2/rows/12-35.s1.pK.txt` (K = 0 … 5) | prints part K of your notes (at most 10,000 characters) |
| `python3 -B enrichment/v7/merge.py check t2whole-103_1-20261008 --model sol-high --ayah 12:35 --slice s1` | checks your output file and lists every problem |

No other commands, files, web or repository search.

## PROCEDURE
**Step 1.** Read parts 0 to 5 in order, each once. After one header line, the notes are lines `[ID] SOURCE, d. … · speaker | stance | claim | mentions …`, oldest author first. If a part looks cut (no `<<part K ends …>>` or `<<end of rows>>` line), run it once more.

**Step 2.** Group the notes into views and label each view (see RULES and LABELS).

**Step 3.** Write the whole file `enrichment/v7/work/t2whole-103_1-20261008/tier2/out/sol-high/12-35.s1.jsonl` in one write.

**Step 4.** Run the check. If it lists problems, fix them and run it again, until it prints `OK`. Then stop and reply with the number of views.

## RULES
- **Same point, same view.** Notes that make the same point go into one view, whatever source or transmitter they come from.
- **Different point, different view.** A note that adds a distinct detail, argument, reason or nuance gets its own view, or the view's text must state that detail. Never let a merge hide a detail. When in doubt, keep it separate.
- **One question per view.** A view answers one question about one part of the verse. Do not put a point about one word and a point about another word, or a point about meaning and a point about a narration, into one view.
- **Disagreements stay visible.** Competing views are separate views. When a source prefers or rejects a view, its note goes in that view (the script shows the stance); say in `note` what the disagreement turns on, when the notes give it.
- **Every id at least once.** An id may appear in more than one view when the note makes more than one point.
- **Do not judge** which view is right, and do not add knowledge that is not in the notes.

## LABELS
- `words`: the word or words of the verse the view is about, copied from the verse text above (a phrase is fine). Use `["*"]` only when the view concerns the whole verse rather than a word in it.
- `type`: exactly one of:
  - `meaning`: what a word means: lexicon, root, etymology, Arab usage and poetry cited for the sense
  - `grammar`: syntax, iʿrāb, morphology
  - `rhetoric`: balāgha: word choice, order, ellipsis, oath form, why this wording
  - `readings`: variant readings (qirāʾāt) and their arguments
  - `referent`: who or what the words refer to
  - `reports`: narrations, occasions of revelation, gradings
  - `sciences`: place and order of revelation, verse counting, virtues of the sūra, abrogation
  - `interpretation`: the meaning of the verse or phrase: the author's explanation, its point or wisdom
  - `theology`: creed and kalām
  - `law`: legal rulings
  - `links`: coherence with neighbouring verses or the sūra, and connections to other verses
  - `inward`: ishārī (Sufi) readings

When a view could take two types, choose the one its notes are mainly about.

## OUTPUT: one JSON object per line, one line per view
```
{"words":["<verse word>"],"type":"<type>","view":"<the point>","rows":["<NOTE ID>","<NOTE ID>"],"note":""}
```
| Field | Rule |
|---|---|
| `words` | see LABELS |
| `type` | see LABELS |
| `view` | the point in English, at most 60 words, with every detail the grouped notes share |
| `rows` | every note id this view covers, copied exactly |
| `note` | optional: what a disagreement turns on, or a detail some of the grouped notes add |
