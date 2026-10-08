# Page 1:1, paragraphs p01–p04

Paths are relative to the repository root (`/Volumes/aro/projects/prose_generation`).

- Paragraph text (unchanged commentary): `micro-lesson/v1/tests/1-1-sol-high-vs-max/input/paragraphs/p01.md` … `p04.md`.
  Quotations appear as `{ar:…, tr:…, gloss:…, source:…}`; `tr` is the commentary's
  Turkish reading and `gloss` its Turkish rendering.
- Exact Arabic and QAC morphemes for the verses these paragraphs quote:
  `micro-lesson/v1/tests/1-1-sol-high-vs-max/input/ayat/<surah>-<ayah>.json`.
- Any other verse, for a second sighting: exact text in
  `../quran-data/data/text/quran-uthmani.tsv` (lines `surah:ayah|text`). Copy Arabic
  only from there or from the ayat files. Morphology for any verse:
  `sqlite3 /private/tmp/claude-502/-Volumes-aro-projects-prose-generation/953da07b-7270-4bb9-881f-d579aaf85e68/scratchpad/qac.sqlite "select qac_ref,surface_ar,lemma_ar,root_ar,pos,morph_features from qac_morphemes where surah=3 and ayah=8 order by word_index,morpheme_index"`.
  The same database can count how often a form recurs, e.g. `select count(*) from qac_morphemes where morph_features like '%PRON:1P%'`.

## Focus ayah

1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ (bismillâhi'r-rahmâni'r-rahîm). QAC: bi- (preposition)
+ ism (noun "name", root س م و, genitive); Allâh (proper noun, genitive); al- + rahmân and
al- + rahîm (adjectives, root ر ح م, genitive). No verb is written.

## Per paragraph

### p01 — quotes 1:1; mentions 1:2–7 as the six ayat that follow

Already explained by the commentary: bi- carries both "together with" and "by means
of", like Turkish -ile, so "adıyla" fits; the action is not said and the reader's act
fills it; there is "a preposition, a noun and three names attached to it".

Qualification: the understood action is context, not encoded in the words.

### p02 — quotes 96:1 ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ and 56:74 فَسَبِّحْ بِٱسْمِ رَبِّكَ ٱلْعَظِيمِ

Already explained by the commentary: in these verses the action is stated (oku,
tesbih et), with the name beside it as means or companion; at 1:1 it is not.

### p03 — quotes 11:41 ٱرْكَبُوا۟ فِيهَا بِسْمِ ٱللَّهِ مَجْر۪ىٰهَا وَمُرْسَىٰهَآ ۚ إِنَّ رَبِّى لَغَفُورٌۭ رَّحِيمٌۭ and 11:43 لَا عَاصِمَ ٱلْيَوْمَ مِنْ أَمْرِ ٱللَّهِ إِلَّا مَن رَّحِمَ; cites 11:40

Already explained by the commentary: the name is placed over the whole journey, both
its sailing and its stopping; the sentence ends with "rahîm"; the ship and the reach
of mercy are the same place.

Qualification: the journey is imagery; it does not give 1:1 an expanded meaning.

### p04 — quotes 6:118 فَكُلُوا۟ مِمَّا ذُكِرَ ٱسْمُ ٱللَّهِ عَلَيْهِ, 6:121 وَلَا تَأْكُلُوا۟ مِمَّا لَمْ يُذْكَرِ ٱسْمُ ٱللَّهِ عَلَيْهِ, 5:4 فَكُلُوا۟ مِمَّآ أَمْسَكْنَ عَلَيْكُمْ وَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهِ; cites 22:34, 22:36, 1:6

Already explained by the commentary: eating is tied to whether the name was
mentioned over the animal; the same meat becomes something else.

Qualification: in 6:121 the negation belongs to لَمْ and the prohibition to لَا, not
to the verbs themselves.
