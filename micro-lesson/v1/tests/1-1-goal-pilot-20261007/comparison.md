# Comparison, 2026-10-07

One run per model, same brief and packet. Linguistic issues below come from an
editorial reading, not the review prompt; the outputs are unchanged.

| | Haiku 5.5 | Sonnet 5.5 | Opus 5.5 |
|---|---:|---:|---:|
| Lessons p01/p02/p03/p04 | 3/3/3/5 = 14 | 2/4/6/7 = 19 | 3/5/6/7 = 21 |
| Subagent tokens | 142k | 79k | 92k |
| Elapsed | 5m 32s | 7m 17s | 5m 14s |
| Material errors found | 3 | 2 | 0 |

All Arabic in all three files is verbatim Quran text (after Unicode normalization),
and every second-sighting verse is attributed correctly.

## Against the earlier summary-like drafts

The goal brief removed the summary problem in all three. None restates the
commentary's bi- / missing-verb explanation; every lesson names a piece and gives
a second verse. All three converge on the same recurring features: mimmâ,
lam + jussive (112:3), lâ + noun and illâ, inna … la-, plural -û, attached pronouns,
ellezî, the case ending of ism.

## Issues

**Haiku**
- p01/2: says al- carries the meaning “olan”. al- is the definite article;
  “olan” comes from the Turkish rendering.
- p04/5: “the second noun always ends in -i”; its own example رَبِّ ٱلْعَٰلَمِينَ ends in -în.
- p04/2: reads وا۟ as “-û-â”; the final alif is silent.
- p02/1: “imperatives end in sukûn” is a weak cue (87:1 sebbihi, plural -û).
- Rejected the -hâ family of 11:41 for an incorrect reason.

**Sonnet**
- p04/2: “lem negates, the verb expresses the negative past” — gives the verb part of
  lem's contribution; the pilot's known error type.
- p04/3: glosses yelid as “doğurdu” and presents a u-i passive vowel pattern that
  does not fit yüzkar or yûled.
- p03/2: ٱعْبُدُوا۟ read as i'budû (u'budû); “p02'deki … ile karşılaştır” reads as an exercise.
- p03/1: drops the madda of مُرْسَىٰهَآ.

**Opus**
- p04/6: renders 22:36 عَلَيْهَا as “onların üzerine” and says it is the ship's -hâ,
  without explaining why a plural of animals takes -hâ. Not wrong, possibly confusing.

## Teaching quality

Opus most often connects form to Turkish: word order reversed against “Allah'ın
adı”, ism's -i/-u/-a mapped to ad-ıyla/ad-ı/ad-ını, zikir as a Turkish bridge to
ذ ك ر, assimilation in mimmâ, sun letters in er-rahmân, 87:1 without bi- versus
56:74 with it. Sonnet is close in coverage but less precise. Haiku is thinner and
carries the most errors.

Common gap against GOAL.md: most lessons still open with the form, not the meaning
the reader already has, and several read as compact grammar notes rather than
asides.
