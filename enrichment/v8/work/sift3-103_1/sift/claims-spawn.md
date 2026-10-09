<!-- v8 claim map: enrichment/v8/work/sift3-103_1 | model claude-opus-5-5 -->
# TASK: write the claim map of the 103:1 page

## WHY THIS MATTERS
A frozen Turkish commentary page on 103:1 will be enriched: under its paragraphs a writer will place short blocks mapping what the Islamic tradition says about the page's claims (who holds which position, who contests it, on what ground). The tradition's material is about 9,000 short notes filed under the verses the page cites. Cheaper reader models will grade every one of those notes against **your list of claims**: a note that takes a position on one of your claims is graded core and reaches the writer in full; any other note does not. So your list decides what the writer sees.
- A claim that is too broad lets noise through. A claim that only retells what a cited verse says (its events, its wording) makes every note that explains a word of that verse look relevant, although the page never discusses that word.
- A claim that is missing, or merged into another, loses every note that bears only on it.
You write the list. You do not judge the claims, add claims of your own, or bring in what the tradition says. Do not spawn agents. Do not change the task.

## YOUR MATERIAL
Read with the Read tool or `cat`, each file once: `enrichment/v8/work/sift3-103_1/inputs/page.pK.txt` (K = 0 … 2), the whole page, paragraphs numbered `[¶n]`. Arabic quotations appear as `{ar:…, tr:…, gloss:…, source:S:A}` (a Qurʾān verse) or `source:"R,Bn"` (a dictionary entry for root R).

## WHAT A CLAIM IS
A point in a paragraph that a tradition note could support, contest, qualify, give the source of, or answer with a rival view:
- a sense of a word or root, a derivation, a usage of the Arabs, a grammatical or rhetorical point;
- a referent or identification (what a key word denotes, who is meant);
- the reading the paragraph gives a cited verse and what it uses that verse for;
- a connection the paragraph draws between verses, words or ideas;
- a question the paragraph raises or settles, including one it settles implicitly by choosing one sense over others (name the alternative it sets aside when the text shows it).
Claims made only in Turkish count too: a paragraph may discuss a word without quoting it in Arabic.

**A cited verse is not a claim; what the paragraph takes from it is.** For each cited verse, write what the paragraph reads in it and uses it for, with the words that reading turns on: of the form "the phrase P in S:A is cited as the Qurʾān's own instance of the sense/pair/image X that the paragraph describes", not "S:A says that …" or "in S:A, these events happen". When the paragraph retells a story across several verses, write one claim per point it draws from the story, naming the verses and words that point rests on; the events themselves are not claims. When the paragraph gives a verse a specific reading (a sense, a referent, a figure of speech), that reading is a claim.

**Test each claim before you keep it:** could a note take a position on it (agree, disagree, offer another sense, give its source)? If the only notes that would "bear on" it are ones explaining the verse's wording or narrative, it is a retelling: rewrite it as the point the paragraph draws, or drop it if the paragraph draws none.

One claim per distinct point; do not merge two points into one claim or split one point into several. Most paragraphs have two to six; a dense one more.

## OUTPUT
Write `enrichment/v8/work/sift3-103_1/sift/claims.jsonl`, one line per claim, paragraphs in order, every paragraph from ¶1 to ¶22 with at least one claim (a paragraph that only sets a scene still has the point it sets up):
```
{"id":"<n><letter>","p":<n>,"claim":"English, one or two sentences, precise enough to judge a note against","terms":["<Arabic term as the page writes it>","<its transliteration>"],"verses":["<S:A>"]}
```
- `id`: paragraph number + letter (a, b, c …).
- `claim`: English (the notes' claims are in English), with Arabic terms in transliteration.
- `terms`: the Arabic words and transliterations the claim turns on, as the page writes them; `[]` if none. List only the words the claim itself turns on, not every word of a quoted verse: a reader takes a listed term as a sign that notes on that word are relevant.
- `verses`: the verses the claim uses (`S:A`), from the paragraph's quotations and tags; `[]` if none.

## FINISH
Run `python3 -B enrichment/v8/sift.py check-claims sift3-103_1` until it prints `OK` (fix only what it names). Then stop and reply with one line: claims written, paragraphs covered.
