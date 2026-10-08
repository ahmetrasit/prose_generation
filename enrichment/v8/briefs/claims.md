<!-- agent /root/{AGENT} | model gpt-6-luna | effort max -->
# TASK: map every claim the {AYAH} page makes, paragraph by paragraph

## ROLE
A frozen Turkish commentary page on {AYAH} will be enriched: under its paragraphs a writer will say what the Islamic tradition says about the page's claims. Before that, cheaper readers will go through thousands of tradition notes and decide which claim each note bears on. They need a precise list of the claims to judge against. You write that list. You do not judge the claims and you do not add claims of your own. Do not spawn agents. Do not change the task.

## YOUR MATERIAL
Read with `cat`, each file once: `enrichment/v8/work/{RUN}/inputs/page.pK.txt` (K = 0 … {LAST_PAGE}), the whole page, paragraphs numbered `[¶n]`. Arabic quotations appear as `{ar:…, tr:…, gloss:…, source:S:A}` (a Qurʾān verse) or `source:"R,Bn"` (a dictionary entry for root R).

## WHAT A CLAIM IS
Anything in a paragraph that a tradition note could support, contest, qualify, source or answer:
- a sense of a word or root, a derivation, a usage of the Arabs, a grammatical or rhetorical point;
- a referent or identification (what "al-ʿaṣr" denotes, who is meant);
- a reading of a cited verse and the use the paragraph makes of it (what the verse is cited **for**);
- a connection the paragraph draws between verses, words or ideas;
- a question the paragraph raises or settles, including one it settles only implicitly by choosing one sense over others (name the alternative it sets aside when the text shows it).
Write claims made only in Turkish too: a paragraph may discuss a word without quoting it in Arabic.
One claim per distinct point. A paragraph usually has two to six; a dense one more. Do not merge two points into one claim and do not split one point into several.

## OUTPUT
Write `enrichment/v8/work/{RUN}/sift/claims.jsonl`, one line per claim, paragraphs in order, every paragraph from ¶1 to ¶{LASTP} with at least one claim:
```
{"id":"4a","p":4,"claim":"English, one or two sentences, precise enough to judge a note against","terms":["العصران","al-ʿaṣrān"],"verses":["6:52","11:114"]}
```
- `id`: paragraph number + letter (a, b, c …).
- `claim`: in English (the notes' claims are in English), with Arabic terms in transliteration.
- `terms`: the Arabic words and transliterations the claim turns on, as the page writes them; `[]` if none.
- `verses`: the verses the claim uses (`S:A`), from the paragraph's quotations and tags; `[]` if none.
Your first write creates the file anew (`>`); later writes append (`>>`).

## FINISH
Run `python3 -B enrichment/v8/sift.py check-claims {RUN}` until it prints `OK` (fix only what it names). Then stop and reply with one line: claims written, paragraphs covered.
