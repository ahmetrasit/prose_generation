# v15 summary (2026-09-28)

This is the short version of `STATUS.md`, which gives the detail, where each number comes from, and how it was
measured.

## Where we are

- v15 has run end to end on all of Fatiha (under the old caps), and on 4:34 and 5:6 both with and without caps.
- Spend so far is 30 Opus calls for $23.86, plus 247 Luna calls. No call failed.
- An ayah costs about $1.25 in Fatiha and $2.3–2.5 in long surahs without caps.
- Without caps, v15 roughly matches the cold arm's depth at 55–70% of its length. It is ahead on sourcing,
  dictionary-backed surprises and the Turkish layer.

## Findings

- **The caps were why v15 was thin.** The readings behind the prose barely changed; only what reached the prose did.
- **Most links come from the ayah reading.** Of the 25 passages the uncapped 4:34 cites, 18 come from its reading, 4
  only from Luna's evidence and 3 only from the window. For 5:6 it is 18 of 19 from the reading.
- **Misses are of two kinds.**
  - Some never came up at all: 4:3, 4:81, 4:90, 5:89, 5:91 and 35:10.
  - Others came up but the writer left them out: 4:129–130, which Luna flagged, and the *qiyāman* of 5:97.

## What we miss

- **Not yet tested:**
  - blind ayat;
  - a comparison with v5, which the North Star sets as the bar (v5's Fatiha prose exists, so no runs are needed);
  - the other named cases (S100, 29:39–45, 18:86 and 18:96, S103);
  - a real reader's judgement;
  - a surah commentary for a long surah.
- **A data defect:** 11 roots, including ق ر ء (the root of *iqraʾ*) and ج ي ء, have two dictionary entries, both
  numbered from B001. For them, "root Bnnn" anchors and source links are ambiguous. No output has cited these roots
  yet.
- **Scattered scenes:** Luna added 704 scene ids, and 587 of them hold a single branch. 494 branches therefore can
  never join a coalition.
- **Luna data coverage:** loanword cards and use profiles exist only for Fatiha, 4:34 and 5:6. Any other ayah needs
  about 3 hours of Luna jobs first (for the whole Quran).
- **Cost:** the whole Quran would cost about $14k at today's CLI rates. The North Star aims at about $1 per ayah,
  which needs the Batch API and caching.

## What adding or removing data does

Measured with dry builds, with no model calls.

**Lifting the input limits** makes the packets much larger. An earlier estimate of about 250k characters predates the
whole-Quran scene tags.

| Packet | Now | Without limits |
|---|---|---|
| 4:34 window | 117k characters | 514k |
| 5:6 window | 111k | 480k |
| 4:34 reading | 135k | 377k |
| 5:6 reading | 152k | 420k |

- **The gate:** as it stands, it would stop the window call at an estimated $7.3.
- **Where the growth is:** mostly mechanical scene lists about far words. That is the dilution the North Star warns
  about.
- **Middle path:** restore full definitions in long windows (about +90k characters, where rare senses live) and keep
  the lists of far scenes limited.

**A list of passages sharing the ayah's rarer roots**, added before the reading:

- A dry ranking puts 5:89, 5:91, 5:97 and 5:8 in 5:6's top 30 within the surah, and 35:10 in the whole-Quran top 12.
- For 4:34 it catches 4:3 and 4:129, but not 4:90 or 4:81. Those echo by phrase, so a phrase match is needed too.
- It would add about $0.1 per ayah. The risk is that it turns into a worklist.

## Decisions open

1. **Input limits:** keep them, lift them all, or restore only the full definitions in long windows.
2. **Fatiha:** rerun it without caps, for about $10–12 of Opus.
3. **Next test:** blind ayat, the v5 comparison, or S100.
4. **The 11-root fix:** the script needs no approval; re-tagging needs about 2 Luna jobs.
5. **The parallels list:** build it and test it on 4:34 and 5:6, for about $5–8 of Opus.
