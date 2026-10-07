<!-- agent {AGENT} | model {MODEL} | effort {EFFORT} -->
# TASK: enrichment blocks for {AYAH}, paragraphs {PARAS} (group {G} of {GROUPS})

## ROLE
You write the enrichment layer of a frozen Turkish commentary page for an advanced reader. The page itself is final: you never change, grade, confirm or correct it. Under its paragraphs you place short, connected Turkish blocks that tell the reader what the tradition says about what each paragraph discusses: who holds which view, on what grounds, where they disagree, and how the verses the paragraph cites connect. Do not spawn agents. Do not change the task.

## YOUR MATERIAL (prepared by script; read it all, once, in order)
| Command | What it prints |
|---|---|
| `cat enrichment/v7/work/{RUN}/write/{GROUP}/page.pK.txt` (K = 0 … {LAST_PAGE}) | the frozen page, paragraphs numbered `[¶n]`; augment blocks under a paragraph belong to it |
| `cat enrichment/v7/work/{RUN}/write/{GROUP}/own.pK.txt` (K = 0 … {LAST_OWN}) | **{AYAH} in full**: every tier-1 note on this ayah, by source (oldest author first): `[ID] speaker \| stance \| claim` and the note's exact anchor `«…»` |
| `cat enrichment/v7/work/{RUN}/write/{GROUP}/cited.pK.txt` (K = 0 … {LAST_CITED}) | **the verses your paragraphs cite**: for each paragraph, its verses; for each verse, its consolidated views `- view (note) [holders]`, each view followed by its note ids |
| `python3 -B enrichment/v7/write.py check {RUN} --group {GROUP}` | checks your two files and lists every problem |

Run each command alone, exactly as written: no `cd`, no `&&`, no `;`. Run every command with 12,000 output tokens. If a part looks cut (no `<<part K ends …>>` or `<<end …>>` line), run it once more. No other commands, files, web or repository search.

## EVIDENCE RULE
Everything you attribute to a source must come from the notes and views you were given. Your own knowledge helps you understand and connect; it never supplies a position, a report, a grading, a quotation or a translator's wording. Every block lists the note ids it rests on. Arabic you quote must be copied from an anchor `«…»` of a note you cite.

## WHAT TO WRITE
For every paragraph {PARAS}, and for every verse that paragraph cites (the list in `cited`), decide:
- **written:** the views bear on what the paragraph says about that verse. Write a block.
- **no_match:** nothing in the views bears on it. Give a one-line reason. This says only that the material you had holds nothing for it.

Blocks:
- **Own ayah ({AYAH}):** the substance. For each topic the paragraph touches, one block: the positions with their holders and reasons, the disagreements and who prefers what, the minority readings that add something. Name author and work in Turkish usage (Taberî, *Câmiu'l-beyân*). Separate a report from the grading a source gives it; separate an author's analysis from your connection; a translation stays a translation (name the translator).
- **Cited verses:** short connection blocks: what the tradition says about that verse that bears on this paragraph's point, and, where the notes show it, how the sources themselves link it to {AYAH}. Connect across verses when the views support it; that is your main contribution.
- One block may serve several paragraphs (`p:[3,5]`) only if it addresses each.
- **Length (open decision, see PLAN):** own-ayah blocks about 120–350 words each; connection blocks about 40–120 words. Material decides; no filler, no bullet lists, no summary of the frozen paragraph.

## OUTPUT (write each file in one write, after reading everything)
`enrichment/v7/work/{RUN}/write/{GROUP}/blocks.jsonl`, one block per line:
```
{"id":"g{G}-b01","p":[3],"verse":"103:1","topic":"kısa Türkçe başlık","text":"Türkçe metin","rows":["TAB-FULL:v24p587/r2","RAZI-FULL:v32p84/r5"]}
```
`enrichment/v7/work/{RUN}/write/{GROUP}/ledger.jsonl`, exactly one line per (paragraph, cited verse) pair in `cited`:
```
{"p":3,"verse":"103:1","status":"written","blocks":["g{G}-b01"]}
{"p":3,"verse":"2:16","status":"no_match","reason":"one line"}
```
The script turns your note ids into source names, locators and anchors; do not type locators.

## FINISH
Run the check until it prints `OK` (fix only what it names; never stop while it lists problems). Then stop and reply with the number of blocks and of no_match rows.
