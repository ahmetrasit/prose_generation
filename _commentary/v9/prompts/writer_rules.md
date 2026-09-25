# V9 writer rules (shared by every lane and writer model)

## What the reading is for

A reader who does not know Arabic should finally *hear* what the ayah's words carry. The canonical
meaning is available elsewhere; use it only as an anchor, to tell what is latent. The reading's substance
is the latent activations and resonances: senses the Arabic words carry in their roots, activated by
something in the ayah, in its surah, in the Fatiha, or elsewhere in the Quran — synthesized into
coherent prose, in the spirit of al-Khūlī / Bint al-Shāṭiʾ (a word's meaning by induction over its
Quranic usage) and al-Biqāʿī (how an ayah joins its neighbours and its surah).

Harvest every real finding, but integrate: no ledger, no paragraph per item, no particle-by-particle walk.

## What enters the reading

- **Two keys.** A rare branch becomes a reading only when (1) the dictionary gives the branch and (2) an
  independent trigger in the ayah, the surah, the Fatiha or the Quran activates it. A branch with no
  trigger is at most a harvest note, not an Ek Notlar line. Rare, surprising and multi-step readings are
  welcome when both keys hold; do not discard them for being unusual.
- **No length limit, and no length cuts.** Choose findings by what they add to the reading, never by how
  long the reading has become; a finding that adds something gets a thread or a sentence. "Too long" is
  not a valid reason to leave one out, and "it was in the list" is not a reason to put one in.
- **Say the image, not just the reference.** When a finding reaches another ayah through a shared image
  (a concept path, a pair, a row), the prose must state that image and the Arabic word that carries it.
  A bare citation of the other ayah is not use.
- **Join threads that share an image.** When two threads carry the same image or word, connect them
  explicitly, in one of the threads or in the Kapanış. Parallel sections that never meet lose the
  resonance.
- **Whole-Quran layer.** Show the actual Arabic of other ayat, not only their references. Many rows repeat
  one formula; pick the representative that adds a movement.
- **Echo roots** may appear as a sound-echo (never as etymology), stated once.

## Shape

1. A short opening paragraph with the plain meaning (anchor only; no heading).
2. Themed `##` sections. Each section is a thread with a thesis (what it reveals), developed across
   micro (the ayah's own words), macro (its surah and neighbours) and global (the Quran, the Fatiha)
   evidence woven together. Minor aspects attach to a thread as sentences, not paragraphs. An ayah that
   deserves many threads gets many sections.
3. `## Kapanış` — what the threads show together.
4. `## Ek Notlar` — one sentence per real finding (both keys hold) that fits no thread.

## Style

Fluent Turkish for a non-specialist; explain grammar only where it changes meaning. Convey certainty
through wording ("düşündürür", "yankılanır", "bu kökte duran bir imgedir"). State a real limit once, at
its first use, inside the sentence that makes the claim; never end a paragraph with a boundary disclaimer
. No internal IDs (root_…, B00x, row
numbers) in the prose.

Arabic doing interpretive work uses the tag `{ar:ARABIC, tr:transliteration, gloss:Turkish gloss}`,
repeated in each paragraph where the word works again. No commas inside `tr`, no colons inside `gloss`.
Cite every inter-ayah or contextual claim right after its quote as `(S:A)`; list ayat individually,
never ranges.

## Checking

Two scripts check every reading: `_commentary/v9/verify_ar.py` (every Arabic quote against its source and
its cited ayah; `--fix` restores near-miss quotes to the exact source form) and
`_commentary/v5/validate_prose.py` (tag and format rules). Your lane brief says whether you run them
yourself or the pipeline runs them after you.
