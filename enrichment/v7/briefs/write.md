<!-- agent {AGENT} | model {MODEL} | effort {EFFORT} -->
{MARK}
# TASK: enrichment blocks for {AYAH}, paragraphs {PARAS} (group {G} of {GROUPS})

## ROLE
You write the enrichment layer of a frozen Turkish commentary page for an advanced reader. The page is final: you never change, grade, confirm or correct it. Under its paragraphs you place short Turkish blocks. The page is the reader's one-stop shop: from each block alone the reader must know **which question the sources answer, which positions exist, who holds them, and the deciding reason or disagreement**, and then decide whether that is enough or open the details. The details are one click away (each block links to the views it cites, the views to every source's note and exact words). So a block is a precise map, never the full account. Do not spawn agents. Do not change the task.

## YOUR MATERIAL (prepared by script; read all of it, once, in order)
| Command | What it prints |
|---|---|
| `cat enrichment/v7/work/{RUN}/write/inputs/{GG}/page.pK.txt` (K = 0 … {LAST_PAGE}) | the frozen page, paragraphs numbered `[¶n]`; augment blocks under a paragraph belong to it |
| `cat enrichment/v7/work/{RUN}/write/inputs/{GG}/own.pK.txt` (K = 0 … {LAST_OWN}) | **{AYAH} in full**: every source note `[NOTE-ID] speaker \| stance \| claim «exact words»`, oldest author first; then {AYAH}'s consolidated views `- VIEW-ID view (note) [holders]` |
| `cat enrichment/v7/work/{RUN}/write/inputs/{GG}/cited.pK.txt` (K = 0 … {LAST_CITED}) | which verses each of your paragraphs cites, then each cited verse's consolidated views `- VIEW-ID view (note) [holders]` |
| `python3 -B enrichment/v7/write.py check {RUN} --model {TAG} --group {G}` | checks your two files and lists every problem |

In holders, `SOURCE+` means the source prefers the view and `SOURCE-` that it rejects it; a name before a colon is the authority the source reports. Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. Run every command with 12,000 output tokens. If a part looks cut (no `<<part K ends …>>` or `<<end …>>` line), run it once more. No other commands, files, web or repository search.

## EVIDENCE RULE
Everything you attribute comes from the notes and views you were given. Your own knowledge helps you understand and connect; it never supplies a position, report, grading, quotation or translator's wording. Every block cites the view ids and/or note ids it rests on. Arabic you quote must be copied from the «exact words» of a note you cite (directly, or through a view you cite).

## WHAT TO WRITE
For every paragraph {PARAS} and every verse that paragraph cites (the list in `cited`; {AYAH} itself is always on it), decide once:
- **written:** the views bear on what the paragraph says about that verse. Write a block, or point to a block you already wrote for this paragraph that covers it.
- **no_match:** nothing in the views bears on it; give a one-line reason. It is recorded, never shown to the reader, and says only that your material holds nothing for it.

Rules for blocks:
1. **Topic, not school.** One block answers one question the paragraph raises (e.g. "Âdiyât: atlar mı, develer mi?"), with every source that weighs in, whatever its tradition.
2. **A complete map, briefly.** Every position that bears on the paragraph's point appears at least as a named clause: who holds it, and its reason when the reason decides. Minor variants are counted, not spelled out ("… ve dört kaynakta daha ayrıntı"). Leaving a relevant position out is a silent loss; spelling out its details is bloat; the views carry the details.
3. **Disagreement and preference stay visible**: who prefers or rejects what, and on what ground. A report is not its grading; an author's analysis is not your connection; a translation stays a translation (name the translator).
4. **Connections are your main contribution.** For a cited verse: in one to three sentences, what the tradition says about it that bears on this paragraph's point, and how the sources themselves link it to {AYAH} when the views show it.
5. **Length is a ceiling, not a target:** own-ayah blocks at most about 150 words; cited-verse blocks at most about 60 words. No filler, no bullet lists, no restating the frozen paragraph.
6. **Turkish**, plain and exact. Authors and works in Turkish usage (Taberî, *Câmiu'l-beyân*); Arabic only where the exact words matter, copied from the notes.

## OUTPUT (write each file in one write, after reading everything)
`enrichment/v7/work/{RUN}/write/{TAG}/{GG}/blocks.jsonl`, one block per line:
```
{"id":"g{G}-b01","p":[3],"verse":"{AYAH}","topic":"kısa Türkçe başlık","text":"Türkçe metin","views":["{AYAH}/v007","{AYAH}/v008"],"rows":[]}
```
`views` are view ids, `rows` note ids from your own-ayah notes; cite at least one of either. One block may serve several paragraphs (`"p":[3,5]`) only if it addresses each.

`enrichment/v7/work/{RUN}/write/{TAG}/{GG}/ledger.jsonl`, exactly one line per (paragraph, cited verse) pair:
```
{"p":3,"verse":"{AYAH}","status":"written","blocks":["g{G}-b01"]}
{"p":3,"verse":"2:16","status":"no_match","reason":"one line"}
```
The script turns ids into source names, locators, anchors and links; never type locators.

## FINISH
Run the check until it prints `OK` (fix only what it names; never stop while it lists problems). Then stop and reply with the number of blocks and of no_match rows.
