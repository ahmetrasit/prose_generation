v8-test-run: enrichment/v8/work/luna-test-95_1/write/opus-packet
# TASK: enrichment blocks for the whole 95:1 page

## ROLE
You write the enrichment layer of a frozen Turkish commentary page for an advanced reader. The page is final: you never change, grade, confirm or correct it. Under its paragraphs you place short Turkish blocks. From each block alone the reader must know **which question the sources answer, which positions exist, who holds them, and the deciding reason or disagreement**; the details are one click away (each block links to the notes it cites). So a block is a precise map, never the full account. Do not spawn agents. Do not change the task. Turkish translations (meal) are out of scope for this run.

## YOUR MATERIAL
Read with the Read tool or `cat`, each once, in order:
- `enrichment/v8/work/luna-test-95_1/inputs/page.pK.txt` (K = 0 … 1): the page, paragraphs numbered `[¶n]`.
- `enrichment/v8/work/luna-test-95_1/inputs/focus.pK.txt` (K = 0 … 9): every note on 95:1: `[ID] SOURCE d.DEATH · speaker · stance · claim «exact words»`. A speaker shown is the authority the source reports; none shown means the author's own view.
- `enrichment/v8/work/luna-test-95_1/gather/packet.pK.txt` (K = 0 … 17): **the gatherer's packet.** Before you, a gatherer read the same page and notes and listed, per paragraph, the notes it judged relevant (part A: ids), then printed every non-focus note it chose, once (part B; focus notes are in your focus notes). It may have missed notes or brought notes that do not bear. Start from it, and search for anything you judge missing.

Search commands (run each alone, exactly as written; no `cd`, `&&` or `;`):

| Command | What it prints |
|---|---|
| `python3 -B enrichment/v8/q.py luna-test-95_1 opus-packet catalog V [V …]` | per verse: its text, how many notes, how many carry each verse word, which verses the notes name, how many notes elsewhere name it |
| `python3 -B enrichment/v8/q.py luna-test-95_1 opus-packet notes V [--word W] [--grep REGEX] [--source SRC] [--page N]` | notes on verse V, 25 per page, filtered by a verse word, a regex over claim and exact words, or a source |
| `python3 -B enrichment/v8/q.py luna-test-95_1 opus-packet find REGEX [--verse V] [--page N]` | notes on any verse whose claim or exact words match (Arabic matched without vowels); without `--verse`, counts per verse |
| `python3 -B enrichment/v8/q.py luna-test-95_1 opus-packet links A B` | notes on A that name B, and on B that name A |
| `python3 -B enrichment/v8/q.py luna-test-95_1 opus-packet note ID [ID …]` | full notes |
| `python3 -B enrichment/v8/q.py luna-test-95_1 opus-packet check-write` | checks your two files and lists every problem |

Claims are English; exact words are mostly Arabic. You decide what to search; search as deeply as a paragraph needs. Several commands may run in one turn.

The page cites these verses per paragraph (95:1 is always on each list):
- ¶1: 95:1, 95:4
- ¶2: 95:1
- ¶3: 95:1
- ¶4: 95:1
- ¶5: 95:1
- ¶6: 95:1, 6:99, 6:141, 16:11
- ¶7: 95:1, 24:35
- ¶8: 95:1
- ¶9: 95:1
- ¶10: 95:1, 95:2
- ¶11: 95:1, 23:20
- ¶12: 95:1, 23:12, 23:14, 23:16, 23:20
- ¶13: 95:1, 95:4
- ¶14: 95:1, 80:17, 80:19, 80:24, 80:29, 80:32
- ¶15: 95:1

## EVIDENCE RULE
Everything you attribute comes from the notes. Your own knowledge helps you understand and connect; it never supplies a position, report, grading, quotation or translator's wording. Every block cites the note ids it rests on. Arabic you quote must be copied from the «exact words» of a note you cite.

## WHAT TO WRITE
1. **One block per question, for the whole page.** A block answers one question the page raises (e.g. "Tîn ve zeytûn: meyve mi, yer mi?"), with every source that weighs in, whatever its tradition. Place it after the **first** paragraph that raises the question; a later paragraph that raises the same question points to that block in its ledger line, it does not get a second block. Never say the same thing in two blocks.
2. **A complete map, briefly.** Every position that bears on the paragraph's point appears at least as a named clause: who holds it, and its reason when the reason decides. Minor variants are counted, not spelled out ("… ve dört kaynakta daha"). Leaving a relevant position out is a silent loss; spelling out its details is bloat.
3. **Disagreement and preference stay visible**: who prefers or rejects what, and on what ground. A report is not its grading; an author's analysis is not your connection.
4. **Connections are your main contribution.** For a cited verse: in one to three sentences, what the tradition says about it that bears on the paragraph's point, and how the sources themselves link it to 95:1 when the notes show it.
5. **Length is a ceiling, not a target:** blocks on 95:1 at most about 150 words; blocks on a cited verse at most about 60 words. No filler, no bullet lists, no restating the frozen paragraph.
6. **Turkish**, plain and exact. Authors and works in Turkish usage (Taberî, *Câmiu'l-beyân*); Arabic only where the exact words matter.

## OUTPUT (write each file in one write, after you have gathered what you need)
`enrichment/v8/work/luna-test-95_1/write/opus-packet/blocks.jsonl`, one block per line:
```
{"id":"b01","p":[3],"verse":"95:1","topic":"kısa Türkçe başlık","text":"Türkçe metin","notes":["TAB-FULL:v24p501#2/r1"]}
```
`p` is the paragraph the block is placed after (a block may list more paragraphs only if it addresses each).

`enrichment/v8/work/luna-test-95_1/write/opus-packet/ledger.jsonl`, exactly one line per (paragraph, cited verse) pair:
```
{"p":3,"verse":"95:1","status":"written","blocks":["b01"]}
{"p":7,"verse":"24:35","status":"no_match","reason":"one line: what you searched and why nothing bears"}
```
"written" may point to a block placed after an earlier paragraph.

## FINISH
Run `check-write` until it prints `OK` (fix only what it names). Then stop and reply with one line: the number of blocks and of no_match rows.
