# Root filter for the writer's input: evaluation (2026-10-08)

Pages: 103:1, 1:3, 95:1 (frozen v16 r13 readings, every paragraph). No model was called.

- **Scripts:** `rootlib.py` (QAC, paragraph roots, matching notes to roots), `eval.py` (configs, sizes, recall, samples), `analyze.py` (miss classes and the proposed menu), `tables.py`.
- **Outputs:** `results.json`, `improve.json`, `misses_95_1.tsv`, `sample_*_B.tsv`, `precision_judgments.tsv`, `tables.md` (per-paragraph tables).
- **To rerun:** gunzip QAC into `qac.sqlite` in this folder, then run `eval.py` (about 4 minutes) and `analyze.py`.

**Verdict.** As a gate, the root filter fails on both goals.
- It does not make the input small: it keeps 49–70% of notes on cited verses, up to 292k chars (103:1) or 525k chars (1:3) for a single paragraph.
- It is not complete: it finds 58% of the (paragraph, note) pairs the 95:1 reference used.

The root signal is still useful as a pointer: a mark on cells in a small menu that the writer reads and then pulls from. Used that way, the page preload is about 45–95k chars, every reference note appears on a menu, and the ¶11 / 12:49 case is solved.

## 1. What was implemented

**Roots of a paragraph:**
- `{ar:…, source:S:A}`: each quoted word is matched to its QAC word in S:A (skeletons without vowels or alif), and its root is taken. Every word counts, so quoting a whole phrase brings in all the phrase's roots.
- `source:"R,Bn"`, with or without `ar:`: R.
- Other Arabic words inside dictionary quotations (المنجاة, الحرز) are ignored. They are dictionary prose about R, not verse words.
- A bare `{source:S:A}` with no Arabic gives no roots (the method takes only roots that are mentioned).
- Turkish transliterations in the prose are ignored.
- Every Qurʾān-quotation word on the three pages matched a QAC word.

**Scope:** the notes on the verses `write.page()` gives for the paragraph, which always include the focus ayah. A note counts once even if it sits on several of those verses.

**Matching a note to a root (no tags exist yet).** Three detectors run over the anchor and over any Arabic inside the claim, after stripping clitics:
- `lex`: the word equals a QAC form of the root, from anywhere in the Qurʾān (word, stem or lemma).
- `pat`: the root letters appear in order and every other letter is an augment letter (سألتمونيها). Weak letters and hamza may be missing, and a doubled final letter may appear once. This catches forms that are not in the Qurʾān, such as اعتصاري, معصر, عصرة.
- `tr`: transliterated words in the English claim (words containing ā ī ū ḥ ṣ ʿ ʾ or an inner apostrophe) are converted to consonants, emphatics are folded, and `pat` is applied. This catches *yaʿṣirūn* and *ya'sirun*.

**Configurations:**

| config | what it does |
|---|---|
| A | lex detector only |
| **B** | **lex + pat + tr: the method as proposed** |
| C | B, plus the focus ayah's roots added to every paragraph |
| D | C, minus common roots (500 or more QAC occurrences) |
| T1 | simulated retag: a note's "verse words" are the words of its own verse that it names (in Arabic or in transliteration), with roots from QAC; notes naming no verse word are dropped |
| T2 | as T1, but notes naming no verse word are kept as the whole-verse cell `*` |
| X | T2 at page scope, limited to the paragraph's dictionary roots |

The simulation finds a verse word for 64%, 65% and 52% of notes on 103:1, 1:3 and 95:1.

**Measurement:** chars are the length of the q.py note line. Tokens are estimated at 2.0 chars per Arabic letter and 4.0 for everything else.

## 2. Size

Each cell reads: chars on cited verses summed over paragraphs (% of no-filter) · largest single paragraph · page union (% of all page notes) · focus-ayah notes per paragraph.

| config | 103:1 | 1:3 | 95:1 |
|---|---|---|---|
| no filter | 2,150k · max ¶ 395k · page 2,137k (~636k tok) | 3,945k · 660k · 4,048k (~1,219k tok) | 209k · 58k · 235k (~70k tok) |
| A lex | 1,265k (59%) · 248k · 1,267k (59%) · 120 | 1,884k (48%) · 476k · 1,956k (48%) · 125 | 93k (45%) · 35k · 134k (57%) · 86 |
| **B** | **1,509k (70%) · 292k · 1,513k (71%, ~459k tok) · 153** | **2,213k (56%) · 525k · 2,294k (57%, ~708k tok) · 152** | **102k (49%) · 38k · 152k (65%, ~46k tok) · 105** |
| C | 1,509k (70%) · 292k · 1,513k (71%) · 207 | 2,213k (56%) · 525k · 2,294k (57%) · 158 | 109k (52%) · 38k · 157k (67%) · 197 |
| D | 1,323k (62%) · 258k · 1,344k (63%) · 200 | 1,737k (44%) · 341k · 1,812k (45%) · 136 | 104k (50%) · 34k · 150k (64%) · 192 |
| T1 | 929k (43%) · 172k · 934k (44%) · 177 | 1,376k (35%) · 235k · 1,408k (35%) · 110 | 89k (42%) · 33k · 115k (49%) · 178 |
| T2 | 1,696k (79%) · 290k · 1,725k (81%) · 388 | 2,742k (70%) · 489k · 2,841k (70%) · 346 | 185k (88%) · 55k · 227k (97%) · 335 |

Per-paragraph numbers for B are in `tables.md`. Examples:
- 103:1 ¶12 keeps 1,306 of 1,704 notes, ¶19 keeps 1,330 of 1,928, and ¶21 keeps 1,184 of 1,657.
- 1:3 ¶5 keeps 2,157 of 2,811, and ¶2 keeps 1,529 of 2,585 (the basmala, 1:1).

Why so little is removed:
- Whole-phrase quotations bring in nearly all of the cited verse's roots.
- The heavy fiqh and hadith layers on verses such as 11:114, 2:264–266 and 1:1 name the same words.
- The focus root matches most notes on the focus ayah, regardless of the paragraph's point. On 103:1, ¶5 (time), ¶7 (pressing), ¶17 (refuge) and ¶20 (whirlwind) all get the same 179 notes that name العصر.

Paragraphs with no Arabic get nothing: 103:1 ¶3, 13, 18, 22; 1:3 ¶1; 95:1 ¶5, 8, 15. 103:1 ¶10 has only the tag `ص ب ر` and gets 10 notes.

## 3. Recall against the 95:1 reference

The reference is the opus-alone writer: 161 notes, 164 (paragraph, note) pairs, all on page verses.

| config | pairs found | of 102 on focus ayah | of 62 on cited verses | page ids found | share of pairs kept |
|---|---|---|---|---|---|
| A | 86 (52%) | 55 | 31 | 107 (66%) | 28% |
| **B** | **95 (58%)** | 62 | 33 | 120 (75%) | 33% |
| C | 106 (65%) | 68 | 38 | 123 (76%) | 57% |
| D | 103 (63%) | 66 | 37 | 120 (75%) | 56% |
| T1 | 90 (55%) | 59 | 31 | 95 (59%) | 51% |
| T2 | 156 (95%) | 102 | 54 | 159 (99%) | 97% |

B per paragraph (found / used by reference):

| ¶ | 1 | 2 | 3 | 6 | 7 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| found | 12/20 | 24/33 | 8/10 | 4/12 | 7/9 | 13/20 | 7/21 | 5/7 | 6/9 | 3/8 | 6/15 |

**Compared with random trimming:**
- Per paragraph, B keeps 33% of pairs and finds 58%, a 1.75× lift.
- At page level, B keeps 65% of chars and finds 75% of ids, only a 1.15× lift.

**Why B missed 69 pairs** (`misses_95_1.tsv`):

| class | n | example |
|---|---|---|
| the Arabic anchor quotes the explanation, not the verse word (whole-verse, referent or purpose notes) | 30 | ¶2 QURTUBI-FULL:95:1/r14 (the ordinary fruits are the soundest reading); ¶1 JISHUMI:v10p7469/r8 (the oath is by the things themselves or by their Lord) |
| non-Arabic source (English or Turkish anchor) that names no verse word | 22 | ¶1 ISLAHI-TADABBUR:vol-9-english:p370/r1; ¶14 ISLAHI …p188/r5 |
| names a verse word the paragraph discusses only in Turkish | 15 | ¶13 TAB-FULL:v24p512/r4, FARRA:v3p276/r6, NAHHAS:v5p256/r6 on *aḥsan taqwīm*: ¶13 discusses "en güzel" but quotes only لقد خلقنا الإنسان; ¶6 ABUHAYYAN-FULL:v4p668/r4 (harvest right) names زيتون |
| outside the paragraph's scope | 1 | ¶11 SAMARRAI-ASRAR:r17/r18 sits on 95:2 but is about 23:20 (the Sinai tree is the olive) |
| detector failure | 1 | ¶9 KASHSHAF-FULL:v4p778/r6 |

## 4. The 103:1 must-find notes (12:49 *yaʿṣirūn* = "they are rescued")

The five notes are MAJAZ:v1p312/r7 and /r8, IBNQUTAYBA-GHARIB:v1p218#5/r3, TAB-FULL:v13p197/r1 and SAMIN-DURR:12:49/r8.

- **¶12:** all five are selected in every configuration, but some matches are fragile.
  - In A, Ṭabarī's rejection (TAB r1) matches only through قول. In B it matches through the transliteration *ya'sirun*.
  - In A, MAJAZ r8 matches only through قلل and قول. Its معصر is caught only by `pat`.
  - All five sit among 1,306 kept notes (328k chars).
- **¶11:** none are selected in any paragraph-scoped configuration, because ¶11 does not cite 12:49.
  - Config X (page scope, limited to dictionary roots) gets all five.
  - The menu in §8 gets all five through "↗ 12:49 يعصرون". The same pointer also lists 2:266 عصر and 78:14 معصرت.

## 5. Precision (B)

I read 30 randomly selected pairs per page against the paragraph text: 20 on cited verses and 10 on the focus ayah. The judgments are in `precision_judgments.tsv`.

| page | cited-verse notes on point | focus-ayah notes on point | weighted by kept share |
|---|---|---|---|
| 103:1 | 11/20 | 3/10 | ≈46% |
| 1:3 | 8/20 | 3/10 | ≈38% |
| 95:1 | 16/20 | 2/10 | ≈32% |

**Off-point notes on cited verses:** about 15 of the 25 are law, hadith reports, grammar or theology on a quoted word. Examples:
- QURTUBI-FULL:12:42/r7 (calling one's master "my lord"), under 103:1 ¶12;
- IBNJAWZI-ZAD:v4p168/r4 (ablution expiates sins, 11:114), under ¶4;
- NAHHAS:v5p137/r9 (the grammar of مَن in 78:38), under 1:3 ¶15.

**Off-point notes on the focus ayah:**
- DURR-FULL:v8p621/r9 ("al-ʿaṣr is an hour of the day"), under 103:1 ¶17 (refuge);
- RAZI-FULL:v32p9#2/r5 (figs in dream interpretation), under 95:1 ¶2.

## 6. The planned retag, simulated

- **Cleaner but smaller.** When a note matches only through its own verse words, incidental Arabic stops counting: Ṭabarī now matches through *yaʿṣirūn*, not through قول. Cited-verse load falls to 35–43% (T1), but recall falls to 55%.
- **Keeping untagged notes restores recall but removes the saving.** T2 recalls 95% but keeps 97% of pairs.
- **Tags won't fix the gate.** The notes the writer needs are disproportionately the ones with no verse word: whole-verse, referent and purpose notes.
- **Type tags would help with precision.** Most off-point cited-verse notes are of a type the paragraph does not treat.
- **Caveats.**
  - A real retag reads the English claims, so T1's recall is a lower bound and T2's size an upper bound.
  - The real retag output (`enrichment/v7/work/retag-1_3-20261008/retag/out/luna-max`) is empty.

## 7. Pros and cons

**Pros:**
- Deterministic, cheap and explainable: every kept note carries the root that kept it.
- Strong where the paragraph quotes a short, specific piece: on 95:1, 16/20 of cited-verse notes are on point, and ¶10 keeps only 15%.
- The dictionary-tag root links a paragraph to same-root verses elsewhere on the page (¶11 → 12:49).
- Transliteration matching finds positions written only in the English claim (TAB-FULL:v13p197/r1).

**Cons:**
- **Not small.** It keeps 49–70% of cited-verse notes. Single paragraphs reach 292k chars (~90k tokens) on 103:1 and 525k (~160k tokens) on 1:3.
- **Not complete.** It finds 58% of pairs. 52 of the 69 misses have no verse word in Arabic, and 15 are words discussed only in Turkish.
- **Blind across paragraphs.** ¶11 cannot reach 12:49.
- **No help on the focus ayah.** Focus notes are the same for every paragraph, and a paragraph with no Arabic gets nothing.
- **Fragile.** The lex detector alone loses 9 more pairs. Common roots (قول, رب, الله) produce false hits, and removing them (D) costs 3 pairs.
- **Hides the needle.** The five 12:49 notes are "found" for ¶12, but among 1,306.

## 8. Improvement: pointers, not a gate (menu first; the writer pulls)

What the writer gets:

1. **Once per page:**
   - the page itself;
   - the focus ayah's tier 2, with tier 1 behind ids;
   - link notes: focus notes that name a cited verse, plus cited-verse notes that name the focus ayah.
2. **Per paragraph, a menu.** One line per cell (verse word × type, once the retag exists) of each cited verse, with counts, sources and stances. Three kinds of pointer:
   - ★ on cells whose word root the paragraph quotes;
   - ↗ to same-dictionary-root cells on other page verses;
   - one "named elsewhere: n notes" line per cited verse.
3. **Pulls:** the writer pulls a cell's tier-2 view, then tier-1 notes by id. Nothing is trimmed.

Measured with simulated cells (verse word only; no types yet):

| | 103:1 | 1:3 | 95:1 |
|---|---|---|---|
| menu lines on cited verses (chars), whole page | 365 (18k) | 445 (23k) | 106 (5k) |
| ↗ pointer lines (chars) | 84 (4k) | 544 (28k) | 70 (3k) |
| largest paragraph menu | 3.7k | 5.0k | 1.7k |
| link notes preloaded | 31 (7k) | 29 (8k) | 23 (7k) |
| focus ayah, tier 1 / tier 2 | 97k / 32.5k (measured, 0.33×) | 103k / ~34k (estimated) | 90k / ~30k (estimated) |
| **page preload** | **~62k** | **~93k** | **~45k** |
| B page union, for comparison | 1,513k | 2,294k | 152k |
| ★ pull per paragraph: tier 1 average → tier 2 at 0.33× | 42k → ~14k | 77k → ~25k | 6k → ~2k |

The 0.33× tier-2 ratio is measured on 103:1 only (32.5k / 97.3k). v7's tier 2 for 100:1 and 87:6 shows 0.28–0.40.

**Reach on 95:1:**
- Focus-ayah pairs: 102/102, because the focus ayah is loaded whole.
- Cited-verse pairs: all 62 are on a paragraph menu.
  - ★ cells and link notes alone reach 33, the same as B.
  - Starring the whole-verse `*` cells as well reaches 54, at about twice the pull (14k vs 6k chars per paragraph).
  - The SAMARRAI miss appears as a "named elsewhere" line under 23:20.

**The 103:1 must-find:** ¶12 has all five notes in a ★ cell. ¶11 has all five behind "↗ 12:49 يعصرون".

**Why this is better than the gate:**
- The preload is 15–40× smaller than B's page union.
- Completeness comes from visibility rather than from a filter.
- The root signal and the cross-paragraph root link are kept, as pointers.
- Type cells from the retag would let the writer skip law, report and grammar cells, which cause most of B's off-point notes.

## 9. What I could not measure

- **Writer behaviour.** No model was run, so the menu's recall means "on the menu", not "used".
- **Real retag and type cells.** No retag output exists. Cells here are (verse, word) only, and the `*` cells are large.
- **Tier-2 size for cited verses.** I applied 0.33× rather than measuring it.
- **Recall on 103:1 and 1:3.** There is no reference set for them beyond 12:49.
- **Precision beyond one judge.** Only config B was judged, 90 pairs, by me alone. The T1 samples were written but not judged.
- **Heuristic detectors.** The false-positive rate of `pat` and `tr` was not measured separately.
- **Token counts** are estimates only.
- **Small count mismatch.** The index count for 1:3 is 15,149 notes on page verses, against 15,172 in the brief.
