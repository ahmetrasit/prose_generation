# Goal: learning Arabic without noticing

The reader should eventually read Quranic Arabic without having felt that they
were studying it. They read an ayah commentary for its meaning; the micro-lessons
beside its paragraphs show the Arabic doing that work, so that the same pieces
become familiar through repeated, understood encounters. Attention stays on
meaning; the language is picked up along the way.

This note states the goal for authoring lessons from a given ayah commentary.
Where a version's instructions conflict with it, this note decides.

## The test for a lesson

A lesson succeeds when the reader can read something in a verse they have not yet
seen, which the commentary paragraph did not already give them.

A statement about Arabic fails this test even when it is true: “Arabic puts the
owner second,” followed by another verse where the same holds, tells the reader
a fact but gives them nothing to do when they next see the form. So do restating
the commentary, translating a phrase without showing which part does what, and a
warning that something “does not mean” X when no reader is likely to think it did.

## What a lesson looks like

1. **Meaning hook.** Start from what the reader already understands in this verse.
2. **Cue.** Name what they can see on the page: a piece, an ending, an order.
3. **How to read it.** Say what to do on seeing the cue, and show it working here.
4. **A walk-through on a familiar phrase.** Apply the same move to a second phrase,
   one step at a time, so the reader decodes it while reading. Never ask the
   reader to stop, answer or write; the walk-through does the decoding with them.
5. **Term last, if at all.** A grammatical name comes only after the reader can
   already do what it names, and only if it helps.

About 40–60 words. For example, at 1:1:

> بِسْمِ ٱللَّهِ (bismillâhi) “Allah'ın adıyla” olur, çünkü arada *ve* olmadan yan
> yana duran isimler sondan okunur: Allâh-ın → ism-i. Fâtiha'daki مَٰلِكِ يَوْمِ ٱلدِّينِ
> (mâliki yevmi'd-dîn) de böyle açılır: dîn “din”, yevm “gün” → “din günü”;
> mâlik “sahip” → “din gününün sahibi”.

At 1:6:

> ٱهْدِنَا (ihdinâ) “bizi ilet” demektir; “bizi” ayrı bir kelime değil, fiilin
> sonundaki -nâ'dır. 3:8'deki duada aynı ek iki kez gelir: رَبَّنَا (rabbe-nâ)
> “Rabbimiz”, هَدَيْتَنَا (hedeyte-nâ) “bizi ilettin”. İsme eklenince “bizim”,
> fiile eklenince “bizi” olur.

## What to teach from one commentary

The commentary quotes the focus ayah and several other verses. Every quoted piece
of Arabic is a candidate, but value comes from what the reader will meet again.

- **High-frequency pieces first.** Attached pronouns; bi-, li-, fî, min, ʿalâ;
  wa-, fa-; al-; lâ, mâ, lam, illâ, inna; and a few reading moves such as nouns
  read from the end, the adjective after its noun, lâ … illâ. Root families come
  next. Rare forms and dictionary illustrations rarely build reading ability.
- **Familiar phrases for the walk-through.** Prefer verses the reader already
  knows or is about to read: the Fâtiha, short surahs, well-known prayers, and
  Quranic phrases Turkish readers already say, such as lâ ilâhe illallâh or
  in şâ'allâh, cited to their verses. Decoding a phrase they have said all their
  life is the reward that keeps the reader going.
- **Turkish as a bridge.** The reader already knows many Arabic words: kitap,
  kâtip, mektup; zikir, tezkere; ilim, âlim, âlem. A known word can open a root
  family. Turkish suffixes can make Arabic pronoun endings feel natural; Arabic
  prefixes such as bi- show the relation before the noun, which is worth pointing out.
- **Contrast over definition.** Show one part changing while the rest stays the
  same: rabbu-ka / rabbu-kum / rabbu-nâ; ihdi-nâ “bizi” / kul-nâ “biz”.
- **Go one step past the commentary.** If the paragraph already explains a piece,
  the lesson adds the next step. If there is no next step, there is no lesson.
- **Fade within the page.** When a feature returns in later paragraphs, the first
  lesson walks through it fully; later ones give the cue and a shorter walk-through,
  leaving more of the reading to the reader. Each lesson still makes sense alone.
- **Warn only about a likely misreading.** A boundary is worth stating when a
  reader would plausibly get it wrong, not as a reflex after every gloss.

## Proposed changes to v1

Not yet applied:

- Replace each engine's discovery question with the test above, and the lesson
  shape in common.md with the five steps and their length.
- Assembly rejects statements, restatements of the commentary and disclaimer-only
  candidates, and orders a feature's lessons so the help fades.
- Give semantics and mapping a positive example family like the
  [bi- family](v1/examples/bi-lesson-family.md), rewritten in this shape.
- Preparation marks which quoted pieces the commentary already explains.
- Authoring needs an Opus-grade model; see the
  [goal pilot](v1/tests/1-1-goal-pilot-20261007/comparison.md).
- The ontology stays as an annotation map; it does not shape how a lesson reads.

The minimal machinery and the linguistic correctness review are unchanged.
