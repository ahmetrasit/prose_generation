<!-- agent /root/v7d_s1_87_114_luna-max_c48 | model gpt-6-luna | effort max -->
# TASK: verse digest, chunk 48 (31 segments from 3 sources)

## ROLE
You take notes on the sources below, so that a later writer can build commentary prose from your notes without rereading the source. You do not write commentary. Do not spawn agents. Do not change the task.

## SOURCES IN THIS CHUNK
- IBNJINNI-MUHTASAB: al-Muḥtasab fī tabyīn wujūh shawādhdh al-qirāʾāt, Ibn Jinnī, d. 392 AH (qiraat)
- IBNKHALAWAYH-HUJJA: al-Ḥujja fī al-qirāʾāt al-sabʿ, Ibn Khālawayh (attr.), d. 370 AH (qiraat)
- IBNMUJAHID: Kitāb al-Sabʿa fī al-qirāʾāt, Ibn Mujāhid, d. 324 AH (qiraat)

What matters by kind of source:
- **qiraat**: A work on the variant readings. Record each reading, its readers, the argument (ḥujja) for it, and the difference in meaning the author draws.

Verses in scope for this run (your segments may also discuss neighbouring verses; record those too):
- 1:5: إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6: ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7: صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ
- 88:3: عَامِلَةٌۭ نَّاصِبَةٌۭ
- 88:4: تَصْلَىٰ نَارًا حَامِيَةًۭ
- 88:25: إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 89:6: أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ
- 89:7: إِرَمَ ذَاتِ ٱلْعِمَادِ
- 90:1: لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ
- 92:3: وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ
- 94:1: أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ
- 97:4: تَنَزَّلُ ٱلْمَلَٰٓئِكَةُ وَٱلرُّوحُ فِيهَا بِإِذْنِ رَبِّهِم مِّن كُلِّ أَمْرٍۢ
- 98:7: إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ
- 102:6: لَتَرَوُنَّ ٱلْجَحِيمَ
- 102:7: ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ
- 105:5: فَجَعَلَهُمْ كَعَصْفٍۢ مَّأْكُولٍۭ
- 107:2: فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ
- 111:5: فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ
- 1:4: مَٰلِكِ يَوْمِ ٱلدِّينِ
- 88:22: لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 89:16: وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
- 89:17: كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ
- 89:18: وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 89:19: وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا
- 89:20: وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
- 91:11: كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ
- 97:5: سَلَٰمٌ هِىَ حَتَّىٰ مَطْلَعِ ٱلْفَجْرِ
- 112:1: قُلْ هُوَ ٱللَّهُ أَحَدٌ
- 87:3: وَٱلَّذِى قَدَّرَ فَهَدَىٰ
- 96:7: أَن رَّءَاهُ ٱسْتَغْنَىٰٓ

## THE ONLY COMMANDS YOU MAY RUN
Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. **Run every command with 12,000 output tokens** (set the shell tool's maximum output to 12,000 tokens).

| Command | What it does |
|---|---|
| `cat enrichment/v7/work/s1_87_114/chunks/c48.pK.txt` (K = 0 … 3) | prints part K of your chunk (at most 10,000 characters) |
| `python3 -B enrichment/v7/digest.py check s1_87_114 --model luna-max --chunk 48` | checks your output file and lists every problem |

No other commands, files, web or repository search.

## PROCEDURE: follow in order, each step once
**Step 1.** Read parts 0 to 3 in order, each exactly once. Each segment starts with `=== SEGMENT <LOCATOR> | source <ID> | verses … | heading ===`; a segment may continue into the next part. If a part looks cut (no `<<part K ends …>>` or `<<end of chunk>>` line at its end), run that same part once more. Never treat text as missing because the display was clipped.

**Step 2.** For every segment, write down each distinct point the source makes (see WHAT TO RECORD).

**Step 3.** Write the whole output file `enrichment/v7/work/s1_87_114/out/luna-max/c48.jsonl` in one write with your file-writing tool, after you have read every part. Do not write it segment by segment, and do not check partial files.

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
