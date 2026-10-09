<!-- agent /root/v9m_map_s103w_20261009_sol-high_2-282 | model gpt-6-sol | effort high -->
# TASK: verse map for 2:282 (3098 notes from 61 sources)

## ROLE
Earlier readers took notes on every source that comments on 2:282. Many sources repeat the same point. Your job is to build the verse's **map**: the questions the sources answer about this verse, and under each question every distinct answer (position), with the notes that hold it, the reasons and evidence given for it, and which sources prefer it or argue against it. A later writer uses the map to tell an advanced reader, for any question, which positions exist, who holds them and what decides between them. You do not drop anything and you do not add anything. Do not spawn agents. Do not change the task.

The verse:
يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ ۚ وَلْيَكْتُب بَّيْنَكُمْ كَاتِبٌۢ بِٱلْعَدْلِ ۚ وَلَا يَأْبَ كَاتِبٌ أَن يَكْتُبَ كَمَا عَلَّمَهُ ٱللَّهُ ۚ فَلْيَكْتُبْ وَلْيُمْلِلِ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ وَلْيَتَّقِ ٱللَّهَ رَبَّهُۥ وَلَا يَبْخَسْ مِنْهُ شَيْـًۭٔا ۚ فَإِن كَانَ ٱلَّذِى عَلَيْهِ ٱلْحَقُّ سَفِيهًا أَوْ ضَعِيفًا أَوْ لَا يَسْتَطِيعُ أَن يُمِلَّ هُوَ فَلْيُمْلِلْ وَلِيُّهُۥ بِٱلْعَدْلِ ۚ وَٱسْتَشْهِدُوا۟ شَهِيدَيْنِ مِن رِّجَالِكُمْ ۖ فَإِن لَّمْ يَكُونَا رَجُلَيْنِ فَرَجُلٌۭ وَٱمْرَأَتَانِ مِمَّن تَرْضَوْنَ مِنَ ٱلشُّهَدَآءِ أَن تَضِلَّ إِحْدَىٰهُمَا فَتُذَكِّرَ إِحْدَىٰهُمَا ٱلْأُخْرَىٰ ۚ وَلَا يَأْبَ ٱلشُّهَدَآءُ إِذَا مَا دُعُوا۟ ۚ وَلَا تَسْـَٔمُوٓا۟ أَن تَكْتُبُوهُ صَغِيرًا أَوْ كَبِيرًا إِلَىٰٓ أَجَلِهِۦ ۚ ذَٰلِكُمْ أَقْسَطُ عِندَ ٱللَّهِ وَأَقْوَمُ لِلشَّهَٰدَةِ وَأَدْنَىٰٓ أَلَّا تَرْتَابُوٓا۟ ۖ إِلَّآ أَن تَكُونَ تِجَٰرَةً حَاضِرَةًۭ تُدِيرُونَهَا بَيْنَكُمْ فَلَيْسَ عَلَيْكُمْ جُنَاحٌ أَلَّا تَكْتُبُوهَا ۗ وَأَشْهِدُوٓا۟ إِذَا تَبَايَعْتُمْ ۚ وَلَا يُضَآرَّ كَاتِبٌۭ وَلَا شَهِيدٌۭ ۚ وَإِن تَفْعَلُوا۟ فَإِنَّهُۥ فُسُوقٌۢ بِكُمْ ۗ وَٱتَّقُوا۟ ٱللَّهَ ۖ وَيُعَلِّمُكُمُ ٱللَّهُ ۗ وَٱللَّهُ بِكُلِّ شَىْءٍ عَلِيمٌۭ

## THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens.**

| Command | What it does |
|---|---|
| `cat enrichment/v9/work/map_s103w_20261009/map/rows/2-282.pK.txt` (K = 0 … 65) | prints part K of the notes (at most 10,000 characters) |
| `python3 -B enrichment/v9/map.py check map_s103w_20261009 --model sol-high --ayah 2:282` | checks your output file and lists every problem |

No other commands, files, web or repository search.

## PROCEDURE
**Step 1.** Read parts 0 to 65 in order, each once. The notes are lines `[ID] SOURCE, d. … · speaker | stance | claim | mentions …`, oldest author first. `speaker` is the authority the source reports, or `author` for the source author's own view. `stance` is the source author's attitude to the note's own point: holds, prefers, reports or rejects. If a part looks cut (no `<<part K ends …>>` or `<<end of notes>>` line at its end), run it once more.

**Step 2.** Find the questions, then group each question's notes into positions (see RULES).

**Step 3.** Write the whole file `enrichment/v9/work/map_s103w_20261009/map/out/sol-high/2-282.raw.jsonl` in one write, after you have read every part.

**Step 4.** Run the check. If it lists problems, fix only what it names and run it again, until it prints `OK`. Do not stop while it lists problems. Then stop and reply with the number of questions and positions.

## RULES: QUESTIONS
- A question is one thing a reader could ask about this verse that the sources answer: what a word means, who or what a phrase refers to, how a word is read, how a construction works, why this wording, what the verse teaches on a matter, what a report says happened, how the verse connects to another verse or to its sūra. Write it as one short English question.
- **One question gathers every answer to it, whatever kind of point the answer is.** A lexical answer, a referent answer and an interpretive answer to the same question belong under the same question. Never split one question by the kind of note.
- **Different questions stay apart.** A question about one word and a question about another word are two questions; so are "what happened" and "what it teaches".
- A note that answers more than one question goes under each.
- Order the questions as the words they concern appear in the verse; questions about the whole verse come last.

## RULES: POSITIONS
- A position is one answer to the question. Notes that give the same answer form one position, whatever source or transmitter they come from.
- **Never let grouping hide a detail.** Every argument, piece of evidence (a verse, a report, a poetry line, a grammatical point, a reading) or nuance that a note adds goes into the position's `reasons`, with who gives it. When two notes give the same answer on different grounds, it is one position and both grounds are in `reasons`.
- A different answer is a different position, even when only a few notes hold it. Differing reports (different numbers, names, places) are separate positions. Trivial variants of one answer (spelling of a name, slightly different wording) stay in one position; say in `reasons` that they vary.
- `prefer`: notes whose source chooses this position over the other positions. `against`: notes that reject or argue against this position. A note that chooses one position and rejects another is in `prefer` of the first and in `against` of the second. Decide from the claim, not only from the stance label: the label describes the note's own point, which may be the rejection of another answer.
- `rows`: every note that states, reports, holds or prefers this position. A note in `prefer` must also be in `rows`; a note is never in both `rows` and `against` of the same position.
- Order positions by how many different sources hold them, most first.
- `turns_on`: when a question has more than one position, what the disagreement turns on, if the notes say it; otherwise "".
- **Every note at least once**, in `rows` or `against` of some position.
- Do not judge which position is right, and add no knowledge that is not in the notes.

## LABELS
- `words`: the word or words of the verse the question is about, copied from the verse text above (a phrase is fine). Use `["*"]` only when the question concerns the whole verse.
- `type`: the main kind of the question, exactly one of:
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

## OUTPUT: one JSON object per line, one line per question
```
{"question":"<short English question>","words":["<verse word>"],"type":"<type>","positions":[{"position":"<the answer>","reasons":"<arguments and evidence, with who gives them>","rows":["<NOTE ID>"],"prefer":[],"against":[]}],"turns_on":""}
```
| Field | Rule |
|---|---|
| `question` | one short English question |
| `words`, `type` | see LABELS |
| `position` | the answer in English, at most 40 words |
| `reasons` | the arguments and evidence for it, with who gives them; "" when the notes give none |
| `rows`, `prefer`, `against` | note ids copied exactly |
| `turns_on` | see RULES |
