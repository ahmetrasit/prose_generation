{MARK}
# TASK: enrichment blocks for the whole {AYAH} page

## ROLE
You write the enrichment layer of a frozen Turkish commentary page for an advanced reader. The page is final: you never change, grade, confirm or correct it. Under its paragraphs you place short Turkish blocks. From each block alone the reader must know **which question the sources answer, which positions exist, who holds them, and the deciding reason or disagreement**; the details are one click away (each block links to the notes it cites). So a block is a precise map, never the full account. Do not spawn agents. Do not change the task. Turkish translations (meal) are out of scope for this run.

## YOUR MATERIAL
Read with the Read tool or `cat`, each once, in order:
- `enrichment/v8/work/{RUN}/inputs/page.pK.txt` (K = 0 … {LAST_PAGE}): the page, paragraphs numbered `[¶n]`.
- `enrichment/v8/work/{RUN}/sift/claims.txt`: the page's claims by id (`4a` = paragraph 4, first claim), with their terms and verses.
- `enrichment/v8/work/{RUN}/inputs/focus-sifted.pK.txt` (K = 0 … {LAST_FOCUS}): **every** note on {AYAH}: `[ID] SOURCE d.DEATH · speaker · stance · claim «exact words»  → grade`. A speaker shown is the authority the source reports; none shown means the author's own view.
- `enrichment/v8/work/{RUN}/inputs/sifted.pK.txt` (K = 0 … {LAST_SIFTED}): every note filed under the verses the page cites (and notes elsewhere that name {AYAH}) that a first reader graded **core**, each once, in full, by verse.

**About the grades.** A cheaper model read every note on every cited verse against the page and the claim map and graded it: `→ core 4a 17b` (bears on those claims), `→ context ¶4` (same passage or word, but no position on any claim), `→ off: reason` (touches no claim). You receive core notes in full; context and off notes are reachable through the search commands, whose results show each note's grade. The grades and the claim map are pointers, not decisions: you may use a note under any paragraph, ignore a grade, and search for what you miss, in particular where a claim has few or one-sided core notes. Focus notes graded context or off are notes on {AYAH} that no claim covers; they are not dropped (see rule 7).

Search commands (run each alone, exactly as written; no `cd`, `&&` or `;`):

| Command | What it prints |
|---|---|
| `python3 -B enrichment/v8/q.py {RUN} {ARM} catalog V [V …]` | per verse: its text, how many notes, how many carry each verse word, which verses the notes name, how many notes elsewhere name it |
| `python3 -B enrichment/v8/q.py {RUN} {ARM} notes V [--word W] [--grep REGEX] [--source SRC] [--page N]` | notes on verse V, 25 per page, filtered by a verse word, a regex over claim and exact words, or a source |
| `python3 -B enrichment/v8/q.py {RUN} {ARM} find REGEX [--verse V] [--page N]` | notes on any verse whose claim or exact words match (Arabic matched without vowels); without `--verse`, counts per verse |
| `python3 -B enrichment/v8/q.py {RUN} {ARM} links A B` | notes on A that name B, and on B that name A |
| `python3 -B enrichment/v8/q.py {RUN} {ARM} note ID [ID …]` | full notes |
| `python3 -B enrichment/v8/q.py {RUN} {ARM} check-write` | checks your two files and lists every problem |

Claims are English; exact words are mostly Arabic. The sifted notes are your starting point, not your limit. You decide what to search; search as deeply as a paragraph needs, in particular when a paragraph's question has few or one-sided notes. Several commands may run in one turn.

The page cites these verses per paragraph ({AYAH} is always on each list):
{CITES}

## EVIDENCE RULE
Everything you attribute comes from the notes. Your own knowledge helps you understand and connect; it never supplies a position, report, grading, quotation or translator's wording. Every block cites the note ids it rests on. Arabic you quote must be copied from the «exact words» of a note you cite.

## WHAT TO WRITE
1. **One block per question, for the whole page.** A block answers one question the page raises (e.g. "Tîn ve zeytûn: meyve mi, yer mi?"), with every source that weighs in, whatever its tradition. Place it after the **first** paragraph that raises the question; a later paragraph that raises the same question points to that block in its ledger line, it does not get a second block. Never say the same thing in two blocks.
2. **A complete map, briefly.** Every position that bears on the paragraph's point appears at least as a named clause: who holds it, and its reason when the reason decides. Minor variants are counted, not spelled out ("… ve dört kaynakta daha"). Leaving a relevant position out is a silent loss; spelling out its details is bloat.
3. **Disagreement and preference stay visible**: who prefers or rejects what, and on what ground. A report is not its grading; an author's analysis is not your connection.
4. **Connections are your main contribution.** For a cited verse: in one to three sentences, what the tradition says about it that bears on the paragraph's point, and how the sources themselves link it to {AYAH} when the notes show it.
5. **Length is a ceiling, not a target:** blocks on {AYAH} at most about 150 words; blocks on a cited verse at most about 60 words. No filler, no bullet lists, no restating the frozen paragraph.
6. **Turkish**, plain and exact. Authors and works in Turkish usage (Taberî, *Câmiu'l-beyân*); Arabic only where the exact words matter.
7. **What the tradition says that the page does not.** After the paragraph blocks, place one to three closing blocks after the last paragraph (`"p":[{LASTP}]`, `"topic"` starting with `Sayfanın dışında:`) for the positions on {AYAH} that no block has covered: focus notes graded context or off and any source on {AYAH} you have not cited. Same map rule: question, positions, holders, in a few sentences. When you finish, every source with notes on {AYAH} has at least one of its notes cited in some block (`check-write` lists the sources still missing); a source that only repeats a position already mapped is cited in that position's clause, not described again.

## OUTPUT (write each file in one write, after you have gathered what you need)
`enrichment/v8/work/{RUN}/write/{ARM}/blocks.jsonl`, one block per line:
```
{"id":"b01","p":[3],"verse":"{AYAH}","topic":"kısa Türkçe başlık","text":"Türkçe metin","notes":["TAB-FULL:v24p501#2/r1"]}
```
`p` is the paragraph the block is placed after (a block may list more paragraphs only if it addresses each).

`enrichment/v8/work/{RUN}/write/{ARM}/ledger.jsonl`, exactly one line per (paragraph, cited verse) pair:
```
{"p":3,"verse":"{AYAH}","status":"written","blocks":["b01"]}
{"p":7,"verse":"24:35","status":"no_match","reason":"one line: what you searched and why nothing bears"}
```
"written" may point to a block placed after an earlier paragraph.

## FINISH
Run `check-write` until it prints `OK` (fix only what it names). Then stop and reply with one line: the number of blocks and of no_match rows.
