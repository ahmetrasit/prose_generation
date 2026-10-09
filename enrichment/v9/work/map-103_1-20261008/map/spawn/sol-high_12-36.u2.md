<!-- agent /root/v9u_map-103_1-20261008_sol-high_12-36_u2 | model gpt-6-sol | effort high -->
# TASK: update 2 of the verse map for 12:36 (158 new notes, 52 questions in the map)

## ROLE
12:36 already has a **map**: the questions the sources answer about this verse, each with its distinct answers (positions). New notes have arrived from sources that were read later. Your job: place every new note in the map. Add it to the position it supports, add a new position when it gives a different answer, or add a new question when it answers something the map does not ask. You never change, remove or renumber anything already in the map, and you add no knowledge that is not in the notes. Do not spawn agents. Do not change the task.

The verse:
وَدَخَلَ مَعَهُ ٱلسِّجْنَ فَتَيَانِ ۖ قَالَ أَحَدُهُمَآ إِنِّىٓ أَرَىٰنِىٓ أَعْصِرُ خَمْرًۭا ۖ وَقَالَ ٱلْءَاخَرُ إِنِّىٓ أَرَىٰنِىٓ أَحْمِلُ فَوْقَ رَأْسِى خُبْزًۭا تَأْكُلُ ٱلطَّيْرُ مِنْهُ ۖ نَبِّئْنَا بِتَأْوِيلِهِۦٓ ۖ إِنَّا نَرَىٰكَ مِنَ ٱلْمُحْسِنِينَ

## THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens.**

| Command | What it does |
|---|---|
| `cat enrichment/v9/work/map-103_1-20261008/map/rows/12-36.u2.pK.txt` (K = 0 … 7) | prints part K: first the current map, then the new notes |
| `python3 -B enrichment/v9/map.py check map-103_1-20261008 --model sol-high --ayah 12:36` | checks the map with your update and lists every problem |

No other commands, files, web or repository search.

## PROCEDURE
**Step 1.** Read parts 0 to 7 in order, each once. The map lists each question as `<question id> <question> [words · type]` and under it its positions as `<position id> <answer> — reasons: …`. The new notes are lines `[ID] SOURCE, d. … · speaker | stance | claim | mentions …`, oldest author first. `speaker` is the authority the source reports, or `author`. `stance` is the source author's attitude to the note's own point. If a part looks cut (no `<<part K ends …>>` or `<<end of input>>` line at its end), run it once more.

**Step 2.** Place every new note (see RULES).

**Step 3.** Write the whole file `enrichment/v9/work/map-103_1-20261008/map/out/sol-high/12-36.u2.raw.jsonl` in one write.

**Step 4.** Run the check. If it lists problems, fix only what it names and run it again, until it prints `OK`. Do not stop while it lists problems. Then stop and reply with the number of additions, new positions and new questions.

## RULES
- **Same answer, existing position.** When a new note gives the answer an existing position gives, add it to that position. If the note adds an argument, a piece of evidence (a verse, a report, a poetry line, a grammatical point, a reading) or a nuance that the position's reasons do not already state, say it in `reasons_add`, with who gives it.
- **Different answer, new position.** When the note answers an existing question differently from every position, add a new position under that question.
- **New question.** When the note answers something no question in the map asks about this verse, add a new question with its positions. A question is one thing a reader could ask about this verse that the sources answer; it gathers every answer to it, whatever kind of point the answer is.
- A note that bears on more than one question goes under each.
- `prefer`: new notes whose source chooses this position over the others. `against`: new notes that reject or argue against this position. Decide from the claim, not only from the stance label. A note in `prefer` is also in `rows`; a note is never in both `rows` and `against` of the same position.
- **Every new note at least once.** Use only the new notes' ids; never move or repeat notes already in the map.
- Do not judge which position is right.

## OUTPUT: one JSON object per line, of three kinds
```
{"position":"<existing position id>","rows":["<NOTE ID>"],"prefer":[],"against":[],"reasons_add":""}
{"question":"<existing question id>","position":"<the new answer>","reasons":"<arguments and evidence, with who gives them>","rows":["<NOTE ID>"],"prefer":[],"against":[]}
{"question":"<short English question>","words":["<verse word>"],"type":"<type>","positions":[{"position":"<the answer>","reasons":"","rows":["<NOTE ID>"],"prefer":[],"against":[]}],"turns_on":""}
```
- The first adds new notes to an existing position. The second adds a new position under an existing question. The third adds a new question.
- `words`: the word or words of the verse the question is about, copied from the verse text above; `["*"]` only for the whole verse. `type`: exactly one of:
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
- `position` text in English, at most 40 words; `turns_on`: what a disagreement turns on, if the notes say it, else "".
