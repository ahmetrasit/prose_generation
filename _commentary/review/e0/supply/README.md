# Supply v0 (E0)

Written 2026-09-28. This is the free script layer (S0 in `../../PHASE2_REPORT.md` §3). No model was run to build it.

## How to run

```
python3 build_supply.py                  # the 7 named probes and the 5 seeded blind ayat
python3 build_supply.py 2:255 88:3       # any ayah
python3 build_supply.py --rebuild-cache  # re-read every source (caches live in cache/)
python3 check_supply.py                  # evaluation only: watch-case ingredients and the forbidden-item grep
SUPPLY_OUT=/some/dir python3 build_supply.py ...   # write somewhere else (used for the determinism test)
```

Settings live in `supply_config.json`, which is written from `DEFAULT_CONFIG` on first run. Each link type,
each parallels lens and each relay can be switched off there. The numbers in it define what counts as a link or
a lens hit. None of them caps or trims a list.

Outputs for each ayah S:A:

| file | who reads it | what |
|---|---|---|
| `out/S_A.md` | the model | sections A–I below, then the paths of the files it may read |
| `out/S_A.pull.json` | the model, on demand (Read tool) | every full list behind the page: all branch fields and every early phrase, every link candidate, the collocation profiles, chain members, Majāz entries and unresolved mappings, qirāʾāt rows. It is kept as clean as the page. |
| `out/S_A.audit.json` | the user only | the internal numbers: significance, lens scores and thresholds, defining-vocabulary counts, config |
| `entries/<envelope>.md` | the model, on demand | the six early dictionary entries of a root, full text (from `root_packets/*.json` `entry_text_clean`) |
| `out/sizes.json` | the user | characters, calibrated tokens (4581 + 1.151 × Arabic + 0.366 × other), per-section tokens, pull size |

## What the page carries

- **A. The ayah, its words and its surah.**
  - Word table: ref, surface, root, lemma, POS. Pause marks are skipped, as in v15's `words.tsv`.
  - The whole surah, with the ayah marked. For surah 2 it shows the ±7 window plus a list of the other ayat of the
    surah that carry the ayah's roots.
- **B. Every branch of every root of the ayah,** in dictionary order and keyed by branch_ref.
  - Each line holds the image, the definition (what_is), the first phrase of the first two early sources with their
    tags, the Turkish concept gloss, and the `branch_kind` with its Turkish scope note.
  - `C[…]` marks the first early phrase of a collocation-bound branch; `F[…]` does the same for a non_bare branch.
  - `[plain: word]` appears where root-dossier assigns that branch to that word.
  - Alternative roots are listed, each with its basis:
    - documented analyses (`qac-dictionary-word-root-analyses.json`);
    - canonical-reading letter exchanges (v15's rule);
    - a variant reading spelled like a Quranic word of another root (for example ḥāmiya at 18:86 → ح م ي);
    - root-dossier "minor" placements (for example ṣalāh → ص ل ي).
  - Roots with no Turkish entry fall back to the Furūq table and are labelled as such. The 11 merged envelopes (for
    example `root_000831--root_000832`) keep their own branch_refs.
- **C. Typed links,** each with its path in words and no score.
  - **Definitional pointers (on).** A branch's own text names, as a whole word after clitic stripping, a word of
    another root. The pointer is kept when:
    - that root stands in this ayah or the window, and the word is not general defining vocabulary (defining
      document frequency ≤ 100 branches) and the root is in ≤ 400 ayat; or
    - the root stands elsewhere in the surah (df ≤ 40, root ≤ 100 ayat); or
    - the root is rare anywhere (≤ 12 ayat).

    The inward direction (a window root's branch names a word of this ayah) is on too.
  - **Rare-lemma bridges (on).** A lemma named in a branch text, found in ≤ 30 ayat, that the Quran puts beside a
    neighbouring root (in this ayah or the ±7 window) in at least half of its ayat, and in at least two ayat. The
    witness ayat are listed.
    - Random branch–root pairs pass this 1.35% of the time (10,150 sampled pairs).
    - A significance threshold calibrated to random pairs (p99, −log10 p ≥ 5.6) was tried first and dropped: a lemma
      found in two ayat can never reach it, and ghishāwa-type bridges are exactly that class.
  - **Dictionary neighbour relations (on).** The dictionary's own `neighbor_distinctions` whose other branch has a
    root in this ayah or the window. Antonym and polarity_pair relations also count at surah level.
  - **Root co-occurrence (on, added after the review).** Two roots of this ayah that the Quran puts together in at
    least two other ayat with ln PMI > 2, this ayah removed from every count (the validator's `root_cooccurrence`
    rule), with those ayat listed. The pull file keeps every positively associated pair.
  - **quran-slm branch pairs (off).** Mutual near neighbours (NeoAraBERT directional rank ≤ 10 both ways) between
    this ayah's branches and the window's branches. Tested: 13 pairs for 29:38.
- **D. Quran usage.**
  - **Roots with ≤ 40 uses:** every use with a keyword-in-context line, grouped by lemma, voice and construction.
    The construction is read from the dictionary's aligned occurrence attachments, or else from the quran-data
    grammar attachments of that ayah (`~` stands for the word).
  - **Other roots:** partners by form, from `collocation_profiles_v2.tsv`. Every row is kept, sorted by form tag and
    then by partner root. No list is sorted by count.
  - **Rare pairings:** root pairs of this ayah that share 2–8 ayat, with the refs. These are the formula echoes.
  - **Same-surah occurrences** of each root.
- **E. Parallels.** The union of six lenses. For each ayah the page names the lenses that include it and the words
  it shares. Same-surah ayat come first, then the rest in Quran order. Other-surah ayat carry their text.
  - The lenses:
    - root and lemma IDF overlap;
    - phrase n-grams, with pronoun-on-particle normalisation;
    - `same-root-other-form`: the same root in a different lemma;
    - `recurring-partner`: recurring partners of a root across its ayat, root level, with no construction detector;
    (renamed after the review: "echo" and "loaded" are the user's ruling terms, and a script lens must not read as
    an echo-tier or loaded-word verdict);
    - the quran-slm ayah text map.
  - A lens includes an ayah when its lens score beats the 99.9th percentile of that lens over random ayah pairs.
    The thresholds come from 400 random foci and are cached. Membership is decided by evidence, not by a count.
- **F. Existing chains.**
  - **Channel-review subchannels** (the reader_a pilot reviews): those whose anchors include the ayah or whose
    members use a branch of its roots, plus cross-surah channels that place one of them.
    - Each shows the parent invariant, the scene or process, the synthesis, the members (with branch_ref,
      branch_kind, scope note and `C[…]`) and the anchors.
    - "Reading type" is dropped.
  - **HFT focus-trace relay lines:** the ayah phrase and the branches activated together, sorted by branch. Section
    names, ids, confidence, mechanism and containment prose are dropped; HFT's own section order (baseline, context
    delta, surprising outlier) is not kept, since it is a class.
  - **v12 cross-run anchor lines:** grades are dropped, and every finding is kept, including those graded reject.
  - Relay prose stays off (`chains.relay_text`).
- **G. Majāz al-Qurʾān.** Quoted from the Majāz text: the sqlite table where it has the entry, otherwise the OpenITI
  text itself (see decisions). OpenITI page and manuscript markers are removed. How each entry is mapped to its
  ayah is recorded in the pull file, and entries of the surah that could not be mapped are listed there.
- **H. Turkish gloss losses.**
  - The dictionary v2 gloss results for each branch: concept and contextual glosses whose profile records a fit
    other than none, a lost facet (given as the facet's own Turkish statement), an addition, a collision or a
    reason.
  - Lexical-unit glosses go to the pull file only.
  - v15 loanword cards appear where they exist.
- **I. Variant readings** from `qiraat.tsv`. Each record is matched to the ayah's word by spelling, because the
  corpus numbers words differently (29:38:4 in the corpus is Thamūd, word 2).

## Test results

- **Watch-case ingredients (`check_supply.py`, evaluation only): 6 of 6 present.**
  - 29:38: the `root_000672/B010` line carries its Ṣiḥāḥ phrase «…نسج العنكبوت…».
  - 29:38: `root_000672/B010` names «العنكبوت» → ع ن ك ب, found in the window at 29:41.
  - 18:86: ح م ء is grouped as حَمَإ [~ مَسْنُونٍ · صَلْصَالٍ مِن ~] — 15:26, 15:28, 15:33, beside حَمِئَة [عَيْنٍ ~] — 18:86.
  - 18:96: ن ف خ has a passive group [~ فِي الصُّورِ (ص و ر)] of 10 uses and a group [~ فِيهِ · ~ مِن رُوحِي (ر و ح)] of 5
    (15:29, 21:91, 32:9, 38:72, 66:12), and D lists "س و ي + ن ف خ: 4 ayat — 15:29, 18:96, 32:9, 38:72".
  - Informative items from the Phase 2 probe list: 17 of 17 present. Among them are the ghishāwa bridge beside
    ب ص ر (2:7, 45:23), ص د د B013, ḥāmiya as an alternative root, ḍaraba B002 with `C[…]`, 4:128 and 5:97 in the text.
- **Forbidden-item grep: 0 hits in script-authored text** (headings and legends), in the pages or the pull files.
  - Scene ids: 0 of the v15 inventory's ids.
  - The known brief string "(15:26, 15:28, 15:33)": 0.
  - 57 page hits are ordinary words inside quoted channel-review prose or motif labels ("departure", "weak support",
    "withheld", "rank", "verdict", "confidence"). They are listed with context in `checks.json`.
  - Two North Star-like phrases occur in existing S19 chain data: a subchannel titled "Waymarks, leading edge, and
    followed tracks", and the motif label "lead animal ahead of the train". They come from the channel review, not
    from this script.
- **Determinism.** Two builds in separate processes (different string-hash seeds) give byte-identical pull and
  audit files for all 12 ayat. The pages are identical except for the pull-file path line when `SUPPLY_OUT`
  differs. Iteration over sets was sorted to reach this.

## Sizes (calibrated tokens; the total includes the 4,581-token prefix; no trimming)

| ayah | chars | calibrated tokens | A | B | C | D | E | F | G | H | I | pull file |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1:6 | 150,201 | 78,113 | 517 | 10,726 | 5,009 | 10,547 | 4,970 | 37,525 | 293 | 3,519 | 188 | 0.5 MB |
| 4:34 | 584,436 | 337,436 | 39,241 | 54,974 | 69,755 | 71,608 | 39,816 | 31,922 | 180 | 24,171 | 212 | 3.8 MB |
| 5:6 | 782,667 | 461,108 | 30,409 | 84,355 | 133,471 | 96,274 | 53,664 | 30,710 | 1,125 | 24,922 | 265 | 6.7 MB |
| 18:86 | 360,315 | 197,837 | 16,297 | 41,342 | 39,109 | 46,151 | 7,054 | 35,389 | 352 | 6,805 | 130 | 2.1 MB |
| 18:96 | 299,297 | 167,391 | 16,172 | 32,624 | 28,765 | 43,499 | 8,614 | 28,817 | 442 | 2,609 | 712 | 1.6 MB |
| 19:70 | 98,853 | 58,340 | 9,748 | 8,377 | 8,104 | 10,408 | 197 | 16,249 | 141 | 248 | 47 | 0.5 MB |
| 19:73 | 286,332 | 155,522 | 10,105 | 33,455 | 26,742 | 43,251 | 9,462 | 25,570 | 267 | 1,521 | 47 | 1.9 MB |
| 19:75 | 266,573 | 144,615 | 10,314 | 26,694 | 18,417 | 58,216 | 6,089 | 17,467 | 43 | 2,155 | 47 | 1.7 MB |
| 29:38 | 247,159 | 136,905 | 10,680 | 23,316 | 25,573 | 30,147 | 11,125 | 29,287 | 43 | 1,519 | 149 | 1.6 MB |
| 29:45 | 345,949 | 189,942 | 10,821 | 34,849 | 33,268 | 47,048 | 15,736 | 29,138 | 43 | 13,786 | 47 | 2.0 MB |
| 88:7 | 69,533 | 39,012 | 1,169 | 5,477 | 2,461 | 2,183 | 1,758 | 19,854 | 43 | 1,201 | 47 | 0.2 MB |
| 88:17 | 124,665 | 64,309 | 1,207 | 9,000 | 5,031 | 5,094 | 480 | 37,671 | 43 | 915 | 47 | 0.3 MB |

2:282 (built for sizing only, not in `out/`): 710,059 tokens (C 157k, D 160k, E 179k).

`sizes_breakdown.txt` splits C, D, E and F into their parts. The largest single part on most pages is D's
partners-by-form lists for frequent roots. On 18:96 that is about 35k tokens (about 22k if only partners attached
at least twice were kept; this is reported, not applied). After it come the pointers at window and surah level,
and the chain members with their repeated scope notes.

## Decisions I made (open to the user)

1. **The construction phrase `C[…]` is the first early phrase of the branch,** as in D's prototype. The dictionary
   has no structured construction field. (Corrected by the review: only 3 of the 401 distinct C/F tags on the 12
   pages start with Ibn Fāris's abstract "أصل…", not "many".)
2. **Majāz entries not in the sqlite table are quoted from the OpenITI Majāz file itself** (`majaz.raw_fallback`,
   on).
   - From surah 19 onward the text writes entries as `" phrase "` without ayah numbers, and the sqlite segmenter
     never captured them.
   - The raw file is the Majāz text, not a late compilation.
   - Mapping: an entry with a marker is mapped by its marker plus the phrase occurring in that ayah's text (within
     ±5 of the marker, the nearest ayah when that is unique). An unnumbered entry is mapped by its phrase: when the
     phrase is in only one ayah of the surah, or in only one ayah that lies between the neighbouring mapped entries.
   - Counts: 1,102 of 1,308 sqlite entries and 1,081 of 1,317 raw entries are mapped. The rest are listed as
     unresolved in the pull file.
   - The surah boundaries come from the file's own headers. A quoted "سورة أنزلناها" (24:1) is recognised as an
     entry, not a header. Surah 76 has only a quoted header.
3. **v12 findings graded "reject" are relayed like the others, without the grade.** Filtering by grade would apply a
   verdict.
4. **H shows the dictionary v2 gloss results** (the source the brief names). They sometimes differ from the concept
   gloss embedded in the Turkish entry, which B shows. H drops lexical-unit glosses, which narrow by design.
5. **"Uses" means word occurrences** (QAC), not ayat.
6. **The parallels lens depth is evidence-based** (random-pair 99.9th percentile), not a top-K. One result: 19:70
   has no parallel at all.

## Known problems

- **Size.**
  - 5:6 is about 461k tokens, 4:34 about 337k and 2:282 about 710k. 18:86, 29:45 and 19:73 are about 155–198k.
  - The push/pull split is still undecided: nothing was trimmed. A decision is needed before any run, or the run
    must rely on pulling from the pull file.
- **Pointer noise.**
  - Whole-word matching still makes errors. Hamza folding confuses وآبل with وابل. Vocalisation is lost (الحمى
    fever is read as ح م ي). A few lemma mappings are wrong (باصرا → إِصْر). The unsuffixed حما (in-law, ح م و)
    still reads as حمإ (ح م ء), a true homograph once folded; the suffixed forms (الحماة, وحماه) no longer do.
  - The "rare root anywhere" level (≤ 12 ayat) adds many off-topic pointers, for example «والبعير» → ب ع ر (12:65).
    It is part of the spec, and the link validator can switch it off by setting `pointer.rare_root_max_ayat` to 0.
- **Rare pairings grow with ayah length.** 5:6 has 289 pairs, 4:34 has 114.
- **The loaded-role lens misses some cases.** For 18:96 it scores 15:29 and 38:72 (ن ف خ with س و ي) at 10.2,
  just under the random threshold of 10.33, so E shows only 32:9 (through the root lens). The pairing is still on
  the page in D, and the threshold was not moved for this case.
- **ك ي ف (83 uses) and ن و س (al-nās, 241 uses) have no Turkish entry.** ن و س falls back to the Furūq table.
- **Majāz is uneven across surahs.** Abū ʿUbayda comments selectively. No entry maps to 29:38, 29:45, 19:75, 88:7 or
  88:17. The mapped index for the checks is `out/majaz_index.json`. 236 raw and 206 sqlite entries are unresolved, mainly through spelling differences, typos in the OpenITI
  text, or markers that are not ayah numbers.
- **The qirāʾāt-to-word matching is heuristic** (by spelling). I checked the 13 records on the probe ayat by eye;
  all attach to the right word. The one record for 18:96:15, qāla ītūnī, spans words 15–16 and is attached to 16.
- **The channel reviews carry drift and their own vocabulary.** Members are shown with scope notes. Nothing is
  filtered.
- **No construction-presence verdict is computed anywhere.** A form-aware verification record (QAC measure and
  voice plus the governed preposition) is still to be built, for the user only.

## Changes after the E0 review (`../review/fixes.md`)

- **B3 Majāz.** The sqlite table appends the next surah's header to the last entry of each surah, and its entry
  1308 (18:108) ran on through surahs 19–114 (176k characters). An sqlite entry now ends at the first surah header or
  volume end inside it. 18:108's G section fell from about 160k tokens to 133. The mapped index is written to
  `out/majaz_index.json` for the checks.
- **M3 bridges.** The focus ayah no longer counts as its own witness: k and n count only the other ayat.
- **M4 wiring.** `supply_config.json` now carries the validator's `root_cooccurrence` rule (new C block) and a
  `_validation` map from each switch to the validator's verdict and the review's measurements. Which types are
  pushed is still the user's decision.
- **M8 labels.** The parallels lenses "echo" and "loaded" are shown as `same-root-other-form` and
  `recurring-partner`.
- **m2, m3 entries.** Ṣiḥāḥ edition footnotes that quote late works (Lisān, Tāj, al-Qāmūs, Ibn Barrī) or manuscripts
  are replaced by `[edition footnote omitted]` (6 notes in 4 entries: root_000006, 000710, 001077, 001559), and
  OpenITI markers are removed. The cleaning lives in `../textclean.py`, shared with the checks.
- **m5 relay order.** HFT relay lines are sorted by branch.
- **m8 pointers.** A stem left ending in alif by removing a suffix no longer joins a hamza root. That was how الحماة
  (calf muscle) and وحماه (in-law) read as حمإ and linked the 18:86 page to 15:26, 15:28 and 15:33. A stricter rule
  that kept ة was tried and dropped: it lost correct feminine-noun joins (البدنة → ب د ن, الخشبة → خ ش ب).
- **Not changed, waiting for the user:** push limits (B1), the chain and relay layers on probe ayat (B2), the
  bridge decision, and the rare-anywhere pointer level (not validated).
- **Tier 3 and v5.** Surah 4 has no HFT, so the 4:34 page is itself a Tier-3 page: F carries the channel review
  (32k tokens) and the v12 relay but no HFT relay. The v5 relay is left out on purpose: Phase 2 found that a script
  union of HFT, the channel reviews and v12 reproduces 98% of v5's branches, and the page relays those sources.

## Code reused (adapted, verdicts and scores removed)

| source | what was taken |
|---|---|
| D `kapacket.py` | packet shape, the `C[…]`/`F[…]` tag, the calibrated token estimate, the probe ingredient list (now in `check_supply.py`) |
| B `supply.py` / `construction.py` | the full branch index with phrases, the definitional cross-references and their defining-vocabulary filter, qirāʾāt |
| C1 `common.py` / `metrics2.py` / `harvest2.py` | whole-word token-to-root and token-to-lemma matching, rare-lemma bridges, the construction-grouped concordance. Neighbour-activation ordering and "N kinds" are dropped. |
| C2 `parallels.py` / `loaded.py` / `common.py` | the lenses and the particle normalisation. The scene lens, departure flags and loaded verdicts are dropped. The loaded lens is root level with no construction detector. |
| A `s05_digest.py` / `pseudo.py` | the channel-review and HFT/v12 relay adapters. Readings counts and "(not used above)" are dropped. |
| v15 `lib.py` / `build.py` | the alternative-root rule and the channel-review block parser (rewritten to keep branch_refs and never trim) |
