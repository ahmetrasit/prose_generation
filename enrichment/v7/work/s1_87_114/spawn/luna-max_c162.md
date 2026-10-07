<!-- agent /root/v7d_s1_87_114_luna-max_c162 | model gpt-6-luna | effort max -->
# TASK: verse digest, chunk 162 (33 segments from 1 sources)

## ROLE
You take notes on the sources below, so that a later writer can build commentary prose from your notes without rereading the source. You do not write commentary. Do not spawn agents. Do not change the task.

## SOURCES IN THIS CHUNK
- RAZI: Mafātīḥ al-ghayb, Fakhr al-Dīn al-Rāzī, d. 606 AH (tafsir)

What matters by kind of source:
- **tafsir**: A Qurʾān commentary. Record the author's own explanation of each verse, every view it reports with who holds it, reports and narrations (the authority at the end of the chain, the gist, any grading the author states), occasions of revelation, linguistic, grammatical, rhetorical, qirāʾa, legal and theological points, disagreements and the view the author prefers, and links it draws to other verses.

Verses in scope for this run (your segments may also discuss neighbouring verses; record those too):
- 87:7: إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ
- 88:16: وَزَرَابِىُّ مَبْثُوثَةٌ
- 88:22: لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 88:26: ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم
- 89:2: وَلَيَالٍ عَشْرٍۢ
- 89:3: وَٱلشَّفْعِ وَٱلْوَتْرِ
- 89:7: إِرَمَ ذَاتِ ٱلْعِمَادِ
- 89:8: ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ
- 89:10: وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ
- 89:11: ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ
- 89:12: فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ
- 89:13: فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ
- 89:14: إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
- 89:18: وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 89:19: وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا
- 89:20: وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
- 89:22: وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- 90:2: وَأَنتَ حِلٌّۢ بِهَٰذَا ٱلْبَلَدِ
- 90:3: وَوَالِدٍۢ وَمَا وَلَدَ
- 90:7: أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ
- 90:18: أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ
- 91:12: إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
- 92:13: وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- 94:4: وَرَفَعْنَا لَكَ ذِكْرَكَ
- 95:2: وَطُورِ سِينِينَ
- 95:3: وَهَٰذَا ٱلْبَلَدِ ٱلْأَمِينِ
- 96:10: عَبْدًا إِذَا صَلَّىٰٓ
- 96:14: أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ
- 98:3: فِيهَا كُتُبٌۭ قَيِّمَةٌۭ
- 99:5: بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
- 99:8: وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ
- 100:5: فَوَسَطْنَ بِهِۦ جَمْعًا
- 101:2: مَا ٱلْقَارِعَةُ

## THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens** (set the shell tool's maximum output to 12,000 tokens).

| Command | What it does |
|---|---|
| `cat enrichment/v7/work/s1_87_114/chunks/c162.pK.txt` (K = 0 … 4) | prints part K of your chunk (at most 10,000 characters) |
| `python3 -B enrichment/v7/digest.py check s1_87_114 --model luna-max --chunk 162` | checks your output file and lists every problem |

No other commands, files, web or repository search.

## PROCEDURE: follow in order, each step once
**Step 1.** Read parts 0 to 4 in order, each exactly once. Each segment starts with `=== SEGMENT <LOCATOR> | source <ID> | verses … | heading ===`; a segment may continue into the next part. If a part looks cut (no `<<part K ends …>>` or `<<end of chunk>>` line at its end), run that same part once more. Never treat text as missing because the display was clipped.

**Step 2.** For every segment, write down each distinct point the source makes (see WHAT TO RECORD).

**Step 3.** Write the whole output file `enrichment/v7/work/s1_87_114/out/luna-max/c162.jsonl` in one write with your file-writing tool, after you have read every part. Do not write it segment by segment, and do not check partial files.

**Step 4.** Run the check command. If it lists problems, fix only the lines it names (for an anchor problem, copy the words again exactly from the segment) and run it again, until it prints `OK`. Do not stop while it still lists problems.

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
{"loc":"EXACT_LOCATOR","rows":[{"verses":["87:6"],"speaker":"مجاهد","stance":"reports","claim":"one-line paraphrase in English","anchor":"exact words copied from the segment","mentions":["2:106"]}]}
{"loc":"EXACT_LOCATOR","rows":[],"none":"short reason, e.g. verse text only"}
```
| Field | Rule |
|---|---|
| `loc` | the locator exactly as in the segment header |
| `verses` | the verse(s) the point is about, as `S:A` |
| `speaker` | who holds the view, as named in the source and in its own script (e.g. `مجاهد`, `Asad`); `author` when it is the author's own view |
| `stance` | the author's attitude to the point: `holds`, `prefers`, `reports`, `rejects` |
| `claim` | the point in one English line, at most 40 words; name the disagreement or preference when there is one |
| `anchor` | 5 to 25 words copied exactly from the segment (same letters, same order; vowel marks may be left out) that carry the point; when the speaker is not the author, include the words that name him |
| `mentions` | other verses this point quotes or names, as `S:A`; `[]` when none |

`none` is only for segments with nothing to record (verse text only, a bare heading, apparatus). If the source text itself is broken, say so in `none`.

## CHECKLIST BEFORE STOPPING
- [ ] every segment has exactly one line
- [ ] every row has verses, speaker, stance, claim and anchor
- [ ] the check command prints `OK`
