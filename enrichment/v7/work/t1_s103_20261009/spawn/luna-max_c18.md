<!-- agent /root/v7d_t1_s103_20261009_luna-max_c18 | model gpt-6-luna | effort max -->
# TASK: verse digest, chunk 18 (12 segments from 2 sources)

## ROLE
You take notes on the sources below, so that a later writer can build commentary prose from your notes without rereading the source. You do not write commentary. Do not spawn agents. Do not change the task.

## SOURCES IN THIS CHUNK
- NASHR: al-Nashr fī al-qirāʾāt al-ʿashr, Ibn al-Jazarī, d. 833 AH (qiraat)
- IBNHISHAM: al-Sīra al-nabawiyya, Ibn Hishām, d. 213 AH (sira)

What matters by kind of source:
- **qiraat**: A work on the variant readings. Record each reading, its readers, the argument (ḥujja) for it, and the difference in meaning the author draws.
- **sira**: A biography of the Prophet or a history. Record the events it ties to the verse, its sources and reports, and any dating or occasion it gives.

Verses in scope for this run (your segments may also discuss neighbouring verses; record those too):
- 28:29: ۞ فَلَمَّا قَضَىٰ مُوسَى ٱلْأَجَلَ وَسَارَ بِأَهْلِهِۦٓ ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا قَالَ لِأَهْلِهِ ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ جَذْوَةٍۢ مِّنَ ٱلنَّارِ لَعَلَّكُمْ تَصْطَلُونَ
- 29:58: وَٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ لَنُبَوِّئَنَّهُم مِّنَ ٱلْجَنَّةِ غُرَفًۭا تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ نِعْمَ أَجْرُ ٱلْعَٰمِلِينَ
- 30:60: فَٱصْبِرْ إِنَّ وَعْدَ ٱللَّهِ حَقٌّۭ ۖ وَلَا يَسْتَخِفَّنَّكَ ٱلَّذِينَ لَا يُوقِنُونَ
- 51:52: كَذَٰلِكَ مَآ أَتَى ٱلَّذِينَ مِن قَبْلِهِم مِّن رَّسُولٍ إِلَّا قَالُوا۟ سَاحِرٌ أَوْ مَجْنُونٌ
- 83:3: وَإِذَا كَالُوهُمْ أَو وَّزَنُوهُمْ يُخْسِرُونَ
- 2:14: وَإِذَا لَقُوا۟ ٱلَّذِينَ ءَامَنُوا۟ قَالُوٓا۟ ءَامَنَّا وَإِذَا خَلَوْا۟ إِلَىٰ شَيَٰطِينِهِمْ قَالُوٓا۟ إِنَّا مَعَكُمْ إِنَّمَا نَحْنُ مُسْتَهْزِءُونَ
- 9:6: وَإِنْ أَحَدٌۭ مِّنَ ٱلْمُشْرِكِينَ ٱسْتَجَارَكَ فَأَجِرْهُ حَتَّىٰ يَسْمَعَ كَلَٰمَ ٱللَّهِ ثُمَّ أَبْلِغْهُ مَأْمَنَهُۥ ۚ ذَٰلِكَ بِأَنَّهُمْ قَوْمٌۭ لَّا يَعْلَمُونَ
- 14:34: وَءَاتَىٰكُم مِّن كُلِّ مَا سَأَلْتُمُوهُ ۚ وَإِن تَعُدُّوا۟ نِعْمَتَ ٱللَّهِ لَا تُحْصُوهَآ ۗ إِنَّ ٱلْإِنسَٰنَ لَظَلُومٌۭ كَفَّارٌۭ
- 90:17: ثُمَّ كَانَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ وَتَوَاصَوْا۟ بِٱلصَّبْرِ وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ

## THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens** (set the shell tool's maximum output to 12,000 tokens).

| Command | What it does |
|---|---|
| `cat enrichment/v7/work/t1_s103_20261009/chunks/c18.pK.txt` (K = 0 … 1) | prints part K of your chunk (at most 10,000 characters) |
| `python3 -B enrichment/v7/digest.py check t1_s103_20261009 --model luna-max --chunk 18` | checks your output file and lists every problem |

No other commands, files, web or repository search.

## PROCEDURE: follow in order, each step once
**Step 1.** Read parts 0 to 1 in order, each exactly once. Each segment starts with `=== SEGMENT <LOCATOR> | source <ID> | verses … | heading ===`; a segment may continue into the next part. If a part looks cut (no `<<part K ends …>>` or `<<end of chunk>>` line at its end), run that same part once more. Never treat text as missing because the display was clipped.

**Step 2.** For every segment, write down each distinct point the source makes (see WHAT TO RECORD).

**Step 3.** Write the whole output file `enrichment/v7/work/t1_s103_20261009/out/luna-max/c18.jsonl` in one write with your file-writing tool, after you have read every part. Do not write it segment by segment, and do not check partial files.

**Step 4.** Run the check command. If it lists problems, fix only the lines it names (for an anchor problem, copy the words again exactly from the segment; for a word problem, copy the word again from the verse text, or use `["*"]`) and run it again, until it prints `OK`. Do not stop while it still lists problems.

**Step 5.** Stop. Reply with the number of segments and the number of rows.

## WHAT TO RECORD
One row per distinct point. Cover the whole segment, not only the verses in scope.
- The author's own explanation of the verse, and each argument he gives for it.
- Every view he reports, with who holds it. When views differ: each view as its own row, and which one the author prefers or rejects.
- Reports and narrations: who the report goes back to (Companion, Successor, the Prophet), the gist, and any grading the author states. Do not list whole chains.
- Language: word meanings, grammar, rhetoric, readings (qirāʾāt), with the authorities and the poetry cited as evidence (poet, the word the line witnesses).
- Legal, theological, historical and coherence points, and every other verse the source links to this one.

Do not record: the verse text itself, chains with no content, editors' footnotes, page apparatus. Do not copy passages: the claim is a short paraphrase, the anchor a short exact quote.

## OUTPUT: one JSON object per line, one line for EVERY segment, in chunk order
```
{"loc":"EXACT_LOCATOR","rows":[{"verses":["87:6"],"words":["فَلَا تَنسَىٰٓ"],"type":"interpretation","speaker":"مجاهد","stance":"reports","claim":"one-line paraphrase in English","anchor":"exact words copied from the segment","mentions":["2:106"]}]}
{"loc":"EXACT_LOCATOR","rows":[],"none":"short reason, e.g. verse text only"}
```
| Field | Rule |
|---|---|
| `loc` | the locator exactly as in the segment header |
| `verses` | the verse(s) the point is about, as `S:A` |
| `words` | the word or words of the verse this point is about, copied from the verse text under "Verses in scope" (a phrase is fine); `["*"]` when the point concerns the whole verse rather than a word. For a neighbouring verse not listed there, copy its words as the segment quotes them, or use `["*"]` |
| `type` | exactly one of the types below: what kind of point this is |
| `speaker` | who holds the view, as named in the source and in its own script (e.g. `مجاهد`, `Asad`); `author` when it is the author's own view |
| `stance` | the author's attitude to the point: `holds`, `prefers`, `reports`, `rejects` |
| `claim` | the point in one English line, at most 40 words; name the disagreement or preference when there is one |
| `anchor` | 5 to 25 words copied exactly from the segment (same letters, same order; vowel marks may be left out) that carry the point; when the speaker is not the author, include the words that name him |
| `mentions` | other verses this point quotes or names, as `S:A`; `[]` when none |

Types (pick the one that fits best):
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

`none` is only for segments with nothing to record (verse text only, a bare heading, apparatus). If the source text itself is broken, say so in `none`.

## CHECKLIST BEFORE STOPPING
- [ ] every segment has exactly one line
- [ ] every row has verses, words, type, speaker, stance, claim and anchor
- [ ] the check command prints `OK`
