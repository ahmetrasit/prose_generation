# Review of the hybrid group workflow (grup.py), 2026-10-05

Scope: `enrichment/v2/grup.py`, `groups.json`, `prompts/{common,grup,grup_*}.md`, `SCHEMA_CARD.md`, the S1 plan
(`work/s001/grup/plan.json`, 44 units, $56.02) and the S87 plan (31 units, $45.59). I re-ran `plan` for S1 and S87
with no model calls and without `--write`, and ran `spawn --dry` for all 44 S1 units into `/tmp/grupreview`. I
measured everything below from the corpus index, the packs and the dry-run files. Scratch scripts are in the session
scratchpad. No project file was changed except this one.

## 0. Verdict

**Not ready for a calibration run as it stands.** Seven defects lose material silently or corrupt the merge, and
each one is cheap to fix (about a day of work in total):

1. Lines longer than 2,000 characters reach the agent truncated. This is **288k characters on S1** (4.1% of
   everything the units would read) and **37% of the hadis unit**.
2. The required bayānī voice is reported as "no material" on **all 20 pages of S87**, although Bint al-Shāṭiʾ and
   al-Sāmarrāʾī discuss 87:1, 87:2–5, 87:12–13, 87:14–15 and 87:17 in 12 segments. The `ayah` material type never
   reads segments that only *cite* an ayah.
3. Required voices are never enforced per page. `"unit": "surah"` in groups.json is ignored by grup.py, so 1:1 has
   no bayānī unit and no recorded reason.
4. The merge can resurrect records that failed validation and miscounts its drops (id collisions between units).
5. Meal surah verdicts: S1 gets two and S87 three, one per meal unit, each written from that unit's share of the
   ayat.
6. Whole sources with no ayah ties can never reach a unit. Examples: Itqān, Burhān, Nashr, Taʾwīl mushkil al-Qurʾān
   and Sībawayh. For S1 that is 147 segments (225k characters) that quote or name the surah. The reference 1:1 page
   cited NASHR twice.
7. The budget counts only the Arabic `text` field. The hadis unit is ~3× its budget (162k tokens of material from
   "86k chars").

The novelty audit (`oncul`) is also under-provisioned for what the user asked for. It has 15 searches in all, for all 8 S1
pages or all 20 S87 pages, and it sees only digests. The reference 1:1 page alone carried 16 novelty blocks (13 oncul + 3
yenilik).

**On cost:** the plan's model is uncalibrated and probably low. Applied to the dosya2 trial's own inputs, it predicts
$1.84 against the measured $5.14 (2.8×).

| scenario | S1 total | S1 per ayah | S87 total | S87 per ayah |
|---|---|---|---|---|
| plan model as written | $56 | $8.00 | $45.6 | $2.40 |
| realistic turns | $65 | $9.35 | $71 | $3.72 |
| realistic turns + thinking output | $99 | $14.08 | $98 | $5.17 |

S1 is the user's "now" target (<$10/ayah). S87 is the production target (<$5/ayah). Both are at risk.

**Where the money goes:** for production-sized surahs the money does not go to sources. In the plan's own model,
S87 = $17.5 re-reading digests (38%), plus $18.6 per-unit fixed overhead (41%), plus $9.5 source material (21%).

**Recommended order:**
1. Fix §1–§3's blocking items.
2. Recalibrate the cost model.
3. Run a mixed S1+S87 calibration batch of about 9 units (estimate ~$14; expect $20–35).
4. Run S1 in full: it has the reference page and four trials to compare against.
5. Then run S87 to confirm the production cost.

---

## 1. Silent losses (highest severity: the user's "no silent losses" rule)

### 1.1 Lines over 2,000 characters are cut by the Read tool. grup.py does not wrap them.
- The project already knows this trap. HYBRID_PLAN.md §1 says "Read cuts lines > 2,000 chars"; enrich.py:288–308
  `wrapped_base` breaks lines at 1,900 characters for exactly this reason.
- `grup.split_files` (grup.py:474–496) splits only at FILE_CHARS = 24,000 and never wraps.
- Dry-run of all 44 S1 units: 6.97M characters of digest and material files. **288,148 characters lie beyond
  column 2,000** of over-long lines, which is 4.1%.
- Worst units:
  - hadis.u01: 131k of 350k hidden (37%). The `en:` translation is one long line per hadith.
  - dirayet-cami.u01 (Ālūsī 1:1): 20%.
  - turkce.u01–u03: 10–11% each.
  - dirayet-cami.u05: 11%.
  - rivayet.u02: 7%.
- The finish audit cannot see this. `required_reads` (grup.py:558–561) lists `pages: [[1, n]]` and the audit checks
  line ranges, not line lengths.
- **Fix:** wrap at 1,900 characters on spaces inside `split_files` (copy the logic of enrich.py:297–301), and assert
  that no line exceeds 2,000 characters. Effort: 15 minutes. Cost: $0.

### 1.2 Sources and passages that only *cite* an ayah never reach `ayah`-material groups. The S87 bayānī voice is lost.
- `ayah_items` (grup.py:153–182) reads only segments whose tie (`seg.s`) is the surah.
- SOURCES_STATUS.md shows several sources of the required group with zero ties:
  - BINTSHATI-IJAZ: 0 tied, 389 citing.
  - SAMARRAI-ASRAR-MUH: 0 tied, 97 citing.
  - SAMARRAI-LAMASAT: 179 tied, 240 citing.
  - SAMARRAI-LAMASAT-HALAQAT: 377 tied, 874 citing.
  - CUYPERS-COMPOSITION (nazm-islahi): 0 tied, 122 citing.
- From the `ref` table, the bayānī segments that cite S87 are 12 segments, about 26k characters:
  - BINTSHATI v1p152 on 87:2–5 (al-marʿā; the asymmetry of raʿy), v2p22 on al-aʿlā (87:1), v2p115 on 87:12–13,
    v1p156 on 87:17.
  - BINTSHATI-IJAZ p271 and p419.
  - SAMARRAI-LAMASAT p33, p138 and p141 on 87:14–15 (zakāt/tazakkā).
  - SAMARRAI-LAMASAT-HALAQAT p117 on «sabbiḥ isma rabbika» against «sabbiḥhu».
- The plan nevertheless prints for S87: `beyani-huli: … no material for this surah: no unit (required voice: merge
  records its absence on every page)`. This is the user's top-two voice, declared absent when it is present.
- The same mechanism drops CUYPERS-COMPOSITION p118, which is his analysis of Sura 87/88 (S87: 7 segments, 24k
  characters; S1: 10 segments, 32k), and BINTSHATI-IJAZ/SAMARRAI-ASRAR on S1 (6 segments).
- **Fix:** add `"cites": true` (the `cites_items` path, with excerpts) to beyani-huli and nazm-islahi, and probably
  to nazm-bikai and modern-bati. Cost: S87 gets one beyani-huli unit (≈$1.8 with today's 20-page digest; ≈$0.8 if
  §4.2 is adopted); S1 about +$0.3 inside the existing unit.

### 1.3 Sources with no ayah ties can never reach a unit in any surah
- Several groups with `material: "ayah"` (groups.json:145, 203, 115) contain sources that have no ties at all:
  ITQAN, BURHAN (ulum-nuzul), NASHR (kiraat), and IBNQUTAYBA-MUSHKIL, KHATTABI, SIBAWAYH (meani-nahiv).
- The plan prints "no material for this surah" every time. That reads as a fact about the surah, but it is a fact
  about the design: these sources will be empty for all 114 surahs.
- An FTS check found segments of these sources that quote a three-word sequence of the surah or name it:
  - **S1: 147 segments, 225k characters** (ITQAN 63/80k, BURHAN 42/60k, NASHR 32/53k, SIBAWAYH 8/31k).
  - **S87: 66 segments, 91k characters.**
- These hold the Fātiḥa's names and merits (Itqān, Burhān), Makkī/Madanī lists, and the readings of 1:4, 1:6 and
  1:7 (Nashr). The single-agent reference page 1:1 cites NASHR twice, so the hybrid would lose evidence the old
  design found.
- **Fix:** for sources without ties, use phrase-search material (the existing `search_items` "phrase" mode plus the
  surah's name) inside their own group. Cost: about +$2–3 on S1 and +$1–1.5 on S87.
- Task A3 (untied segments of Jishumī, Ibn ʿĀshūr FULL, Durr FULL, Bursevī) is the same problem for sources that do
  have ties. Across the tafsir/ulum/maʿānī/qirāʾāt/naẓm/ishārī kinds, 551–606 segments not tied to S1/S87 quote a
  four-word sequence of their ayat (~1M characters each). Most are cross-quotations, but this is where the oncul
  group's whole-Qurʾān search has to look.

### 1.4 Required voices are not enforced per page
- groups.json:86, 99 and 233 say `"unit": "surah"` for nazm-bikai, beyani-huli and meal. **grup.py never reads the
  key** (`grep '"unit"'` finds only result dicts).
- A unit's pages are the pages of its items (grup.py:434–436). As a result:
  - S1 beyani-huli covers surah and 1:2–1:7 but **not 1:1**. No kapsam `{page, durum: yok}` line can be written for
    1:1, and the merge records an absence only when the group has zero items (grup.py:715).
  - So 1:1 lacks the required voice with no recorded reason.
- `finish` (grup.py:622–641) checks that every planned segment has a kapsam line. It never checks that each page of
  a required group has either a block or a `yok` line.
- **Fix:**
  - Required groups get all pages: honor `unit: surah`, or add every page to `covered`.
  - `finish` warns per page that has neither a kept record from the group nor a `yok` line.
  - `merge` writes the per-page status of each required voice: cited, yok with reason, or no unit.

### 1.5 Silent or near-silent cuts in the search groups
- `print_plan` (grup.py:464) prints "too common" only when `q.get("skipped")` is set. `search_items` never sets
  `skipped`; it records `too_common_in` (grup.py:295, 303). The too-common notice is therefore never printed.
- Hits beyond the per-source cap (SEARCH_TOP 6, or 3 and 4) are recorded only in plan.json. Neither the plan printout
  nor the agent is told:
  - S1: hadis 208 hits, siir 130, vucuh 34, siyer 89.
  - S87: hadis 318, siir 221, vucuh 187.
  - Example: S87 «اسم ربك الاعلي» has 35 Nasāʾī hits (6 kept) and 39 in the Musnad.
  - Hits in too-common sources: S1 siir 2,479, siyer 2,196; S87 siir 4,384.
- **Fix:** print both counts per group, and give the agent a short list of the capped (query, source, n) pairs so it
  can spend its extra calls on them.

### 1.6 Smaller silent gaps
- **`meal_items` file list:** it reads only words.md and meals.md (grup.py:336), but grup_meal.md:3 tells the agent
  its material includes turkish.md.
- **Per-ayah content routed to the surah page.** A segment with `s` set and `a` NULL goes to the surah page
  (grup.py:180).
  - S1: 281k characters of tied-group material lands on the surah page. Much of it is per-ayah: FARISI-HUJJA 29
    segments/43k (e.g. v1p15 on mālik/malik, 1:4), WAHIDI-BASIT 26/32k, IBNMUJAHID 15/13.5k, BURSEVI 13/24k,
    THALABI 11/17k.
  - S87: 122k characters.
  - A unit can write only to its listed pages. Readings for an ayah whose page is not in the kiraat unit's list can
    therefore go only to the surah page, against the brief, or into kapsam as `yeni_yok`. Example: kiraat.u01 has
    surah and 1:4–1:7; 1:1–1:3 are in no kiraat unit.
  - **Fix:** route a NULL-`a` segment to the ayah it quotes (the `ref` table or a phrase match), else to the surah.
    Always give the surah-routed units every page.
- **Nobody reads usage.md** (S1 108k, S87 111k characters: the Qurʾān-wide occurrences). Ayet_ayet and the
  usage-table half of vucuh therefore have no owner. Only grup_oncul.md:10 mentions it, as a pointer.
- **Nobody reads errata_candidates.json** (S87: **133 candidates**; S1: 1). No group writes duzeltme blocks, although
  zengin.md Step 6 requires them and the reference 1:1 page had one.
- **Units marked `error` are still merged.** `finish` sets `status` from `is_error` only (grup.py:658), not from
  kapsam completeness, and `merge` merges any unit with a run.log.json (grup.py:682).
- **Stale whole file.** If an agent writes `records.<t>.jsonl` and later fixes a part, `finish` keeps the stale whole
  file (grup.py:648–649 joins parts only when the whole is absent). grup.md:66 invites both paths.
- **Records outside the unit's pages.** Records written for a page outside `u["pages"]` are ignored by `finish`'s
  check but merged by `merge` if a joined file exists. Parts for such pages are dropped silently.

## 2. Redundant work (what is paid for more than once)

### 2.1 Digests: the largest redundancy
| | S1 | S87 |
|---|---|---|
| digest tokens, each page once | 74.7k | 169.4k |
| digest tokens summed over units | **1.64M (21.9×)** | **2.82M (16.6×)** |
| share of all unit context | 34% | **62%** |
| $ in the plan model (write + 6 reads) | $10.1 | **$17.5 (38% of the plan)** |

- **Units that are mostly digest.** Many S87 units span 16–20 pages with little material. Each pays 140–170k digest
  tokens to process 2–40k tokens of sources:
  - dirayet-kesşaf.u01: 19 pages, 18.9k material.
  - ulum-nuzul.u01: 18 pages, 18.8k.
  - modern-bati.u01: 17 pages, 8.3k.
  - meani-nahiv.u01: 16 pages, 16.2k.
  - turkce-sozluk.u01: 19 pages, 20.1k.
  - oncul.u01: 20 pages, 0.
- **The digest is not small.** It shows 47–49% of the prose words (543 S1 paragraphs averaging 71 words; 84–86% of
  paragraphs cut). It is about ⅓ of the full numbered page only because the Arabic tags are shortened. Prose with
  tags shortened but nothing cut is about 2× the digest (S1 146k, S87 321k tokens). A 12-word paragraph index is
  0.36× (S1 27k, S87 62k).
- **It is the worst of both.** It costs half the prose, yet a unit cannot see what a paragraph claims. "Do not
  restate the base", the lugat rule "do not restate what the commentary already says" (grup_lugat.md:6), destek,
  itiraz and oncul all need the claim, and the agent must either guess or Read full paragraphs. Those Reads add turns
  and context the model does not count.

### 2.2 Per-unit fixed overhead
- Every unit pays harness 5.3k + brief 13.0k (`brief_tokens`) of context and an assumed 19k of output (4k records +
  15k thinking) before it reads anything: about **$0.60 per unit**. That is $26.4 of S1's $56 and $18.6 of S87's
  $45.6.
- **Small "tail" units** are created by greedy packing (grup.py:353–367). They exist only because a group exceeded
  the budget by a few thousand characters:
  - S1: kiraat.u02 (3.8k tokens, $0.71), dirayet-kesşaf.u02 (4.4k, $0.71), beyani-huli.u02 (5.1k, $0.72),
    akademik.u04 (8.5k, $0.74), meal.u02 (12k, $0.84). That is $3.7 for about 34k tokens of material.
  - S87: dirayet-cami.u02 ($0.84, 8.4k), akademik.u03 ($0.82, 6.2k).
  - S87 also has whole groups that are tiny: icaz-belagat.u01 ($0.72 for 2 hits, 1.7k tokens), kiraat.u01 ($0.88,
    5.8k), nazm-islahi.u01 ($0.79).
- **Greedy packing splits a page across units of the same group.** S1 dirayet-cami has 1:1 in 5 units: u01 is Ālūsī
  1:1 alone, u03 and u04 are Rāzī FULL. Since Ālūsī summarises Rāzī, two agents write the same points for the same
  page, and the group's own rule "shared points once, with who repeats whom" (groups.json:56) cannot hold.
  - Pages in more than one unit of the same group, S1: rivayet 1:1 and 1:5; dirayet-cami 1:1, 1:2, 1:5, 1:7;
    turkce 1:2 and 1:5; beyani-huli, kiraat and akademik 1:7.

### 2.3 Duplicate editions and copying works: checked, small
- **The FULL-in-short rule (grup.py:160–176) is sound.** It uses character 5-grams at ≥80% containment. Against
  unrelated works of the same surah it flags 0 of 313 S1 test segments and 3 of 66 S87 segments, all ≤164 characters.
- **It removes the right things:**
  - S1: every TAB-FULL, BAGHAWI-FULL, BAYDAWI-FULL, ABUHAYYAN-FULL and IBNASHUR-FULL segment, 74 of 75 ALUSI-FULL.
  - S87: every IBNASHUR-FULL and RAZI-FULL segment.
- **RAZI vs RAZI-FULL on S1 is not a duplicate pair.** They share 0.6% of word 5-grams (the short edition is a
  different text), so reading both is right. RAZI-FULL S1 is 188 segments, 380k characters, 114 of them on 1:1.
- **One gap: the reverse direction.** When the short edition is the part inside FULL, both are read. Example: BIQAI
  S1 is 41% inside FULL; 6 FULL segments (14.7k) are kept, about 7k of them overlapping. Small.
- **Unpaired editions:**
  - WAHIDI-QT and WAHIDI-WAJIZ are one work (60–81% shared word 5-grams) but not named X/X-FULL, so they are not
    deduped. Only 227–291 shingles: negligible. Add an explicit `editions` pair list to groups.json.
  - SAMARRAI-LAMASAT against -HALAQAT: 8%, so not duplicates.
- **Cross-work copying is low at the text level.** Word 5-gram containment ≥25% was found only for Nasafī←Kashshāf
  on S87 (33%). Ibn Kathīr←Ṭabarī is 5–12%, Ālūsī←Rāzī 1–3%.
- **Conclusion:** textual duplication is not where money is lost. Semantic duplication is (the same aqwāl reported
  by 6–8 groups); see 3.4.

### 2.4 Material the base already contains
- **lugat reads the dictionary the base was written from.** It reads the project dictionary's per-ayah sections:
  S1 83k characters, S87 **200k characters, 2 units, $3.16**. Its brief then forbids restating what the commentary
  takes from them.
- The new lexical information sits in the lexica it opens only on demand, within 8 calls.
- Asās is small enough to read whole. Bound-root entries: S1 18 roots, 13k characters; S87 43 roots, 29k
  characters. LISAN, LANE and TAJ are 200–570k characters per surah: on demand is right for those. FURUQ and
  SAMIN-UMDA are not keyed by root, so the root lookup finds nothing for them.

### 2.5 Search noise
- **Bug at grup.py:287.** `any(x in pos for x in ("N","V","ADJ"))` tests substrings, so `CONJ;REL`, `REM;NEG`,
  `ACC;PRON` and `P;PRON` all pass. «والذي», «فلا», «انه», «فيها», «وما», «ولا» and «اياك» are searched as rare
  content words:
  - S87: 10 of 58 queries, 40 hits.
  - S1: 6 of 26 queries, 23 hits.
  - Example: «اسم» for 87:1 matches «يا أسم» (a woman's name) in ʿĀmir b. al-Ṭufayl's poem, twice (MUFADDALIYYAT
    v1p363 and ASMAIYYAT v1p219#2, the same poem in two anthologies).
- **Formula phrases.** In S87 hadis, «ما شاء الله» (87:7) brings 33 of the 63 kept items, all unrelated to the ayah.
  In S1, «بسم الله الرحمن» brings 16 (letters and invocations).
- **Poetry single-word search is mostly noise by construction.** Pre-Islamic poems never quote the ayah. The
  shawāhid that bear on an ayah are the verses the tafsir and maʿānī works cite, and those are already in the
  rivayet and meani-nahiv material.
  - siir-sahid costs S1 $1.31 and S87 **$3.06 (2 units, 163 items)**.
  - The single-agent reference page used no poetry anthology.

## 3. Robustness

### 3.1 Cost-model risk (grup.py:58–60, 370–374)
- **Validation against the closest trial.** zengin-dosya2.1_1.opus.high pre-loaded its material, like a grup unit.
  On that trial's own inputs (160k estimated tokens) the formula gives **$1.84; measured $5.14**.
  - Output: 31.8k predicted, 131.7k measured.
  - Cache reads: 1.09M predicted, 3.43M measured.
  - Turns: 6 assumed, 14 measured.
- **Turns.** TURNS = 6 is unrealistic for multi-page units. The brief requires a Write per page (in parts of ≤25
  records) and a check.py run per page (check.py takes one `--target`), plus kapsam and gaps. A 20-page unit is
  realistically 40+ turns at 200–300k context. S87 rivayet.u01 alone: 45 × 260k × $0.20/M ≈ $2.3 of cache reads,
  against $0.31 modelled.
- **Output.** 15k thinking + 8% of material is far below the trial (about 0.7 output tokens per material token).
  kapsam lines are not modelled at all: 1,258 S1 items and 1,105 S87 items at about 70 tokens each.
- **Tool results.** Up to 8 corpus calls (15 for oncul), each up to ~24 KB, plus full-paragraph Reads, enter the
  context. They are not modelled.
- Sensitivity on the actual plans:

| assumption | S1 | S87 |
|---|---|---|
| as written | $56.0 | $45.6 |
| turns = 6 + 2·pages | $65.4 | $70.7 |
| output = 19k + 0.5·material + 1.5k/page | $88.1 | $70.7 |
| both | **$98.6** | **$98.2** |

- **Cache expiry.** A unit that thinks for more than 5 minutes between calls (≈15–20k output tokens at Opus speed)
  loses its 5-minute cache and rewrites 150–300k of context, about $1–1.5 per expiry. The 1:1 page already paid this
  once ($2.32, COST_PLAN.md §1). It is worth testing the 1-hour cache write ($8/M) for units over 150k context.
- **Contexts at spawn.** 16 S87 units and 6 S1 units start above 150k context; 5 S87 units start above 200k
  (rivayet.u01 259k, dirayet-cami.u01 240k). The model accepts it (the 1:1 page reached 512k), but turn-1 reading of
  17+ files of 250k tokens is where recall drops.

### 3.2 Unit-agent failure modes
- **Anchoring from digests.** A capa must be three consecutive words outside «…» and outside shortened tags. The
  digest keeps the first 24 and last 10 words, so anchoring works mechanically. Placement ("after the paragraph it
  speaks to") is a guess when the paragraph's middle (on average 37 hidden words) is where the point is made.
- **Budget accounting by `chars`.** grup.py:181 and grup.py:313 use `len(row[6])`, the source text only. `item_text`
  adds the `en`, `tr` and `notes` fields (grup.py:147–149). As a result:
  - hadis.u01 S1 is "86,445 chars" but 162.5k tokens, about 280k characters of material files: **≈3× its budget**.
  - Its context of 213k is the largest in S1.
  - **Fix:** budget on `len(item["text"])`, or on tokens.
- **kapsam with 83–135 items per unit** is bookkeeping the model will get wrong at scale: missed lines, guessed
  `tekrar` against segments in *other* units. The `yeni_yok` definition ("adds nothing beyond … another block") is
  unknowable for an independent unit.
- **`finish` checks only that every segment is listed** and that `durum` is valid. It should also check:
  - `kullanildi` lines name `kayit_ids` that exist among the kept records;
  - a kept record cites the segment (or its family);
  - a required group has a block or a `yok` line on every page.
- **Brief conflict.** common.md says "Read a pack file once, with the Read tool, one file per call". grup.md says to
  read every listed file in parallel in turn 1. The second governs in practice, but resolve the conflict explicitly
  (HYBRID_PLAN C7 says it is "overridden").
- **The oncul unit cannot do its job as written.** It has 8–20 pages of digests, no full claims, and 15 searches.
  Most imge/sentez claims will go unsearched. The yenilik blocks will then say "not found in the checked sources"
  for sources that were never checked.

### 3.3 finish/merge defects (grup.py:606–721)
- **Id collision.** Units "number ids as they like" (grup.md:41), so S001-TDR-001 will exist in several units.
  `merge` validates all records together. `check_records` drops every second occurrence as "duplicate id"
  (validate.py:101–102).
  - Then `kept_full = [r for r in recs if r["id"] in ids]` (grup.py:690–691) **re-admits every record that shares an
    id with a kept one**. That includes records that failed for real reasons (bad capa, non-sahih hadis, ayet not
    covering the page).
  - `dropped_at_merge = len(recs) - len(kept)` (grup.py:712) counts the collision drops that were re-admitted.
  - **Fix:** prefix ids with the unit before validation (or renumber first), filter by object identity, and write
    the dropped list with reasons to merge.json.
- **One-yenilik-per-paragraph across units.** The rule is enforced in unit-directory alphabetical order, so which
  yenilik survives is arbitrary.
- **Near-duplicate detection is too narrow** (grup.py:700–704). It requires the same paragraph and the same locator.
  The same point reported via TAB (rivayet), QURTUBI (dirayet-cami), KASHSHAF (dirayet-kesşaf), IBNASHUR
  (modern-arap), ELMALILI (turkce) and TABRISI (mezhep) is not detected.
- **kapsam `kayit_ids` point to pre-renumbering ids.** provenance.json maps new id → unit, not old id → new id.
- **Corpus index changes are not detected.** `spawn` stops on a missing segment and checks the pack hash, but a
  rebuilt index (Task A2/A3) can silently change a segment's text under the same locator. Record the index's
  checksum in plan.json.

### 3.4 Per-page coherence does not survive independent units
- The single-agent page enforced:
  - one block per point and "each point once on the page" (common.md);
  - at most five blocks after a paragraph;
  - one meal verdict;
  - novelty logic (oncul on the attested finding, yenilik only when none).
- With 18–23 groups writing to one page, none of these can be enforced by a unit:
  - The ≤5 rule is now only a warning.
  - The meal verdict is duplicated: S1 meal.u02 writes a surah verdict from the meals of 1:7 alone; S87 has three
    surah verdicts.
  - Received meanings ("al-ʿālamīn" = all created worlds, Ibn ʿAbbās) will appear in up to six groups' blocks.
- The user accepts independence ("their sequence doesn't matter"), but not repetition: "say each thing once on the
  page" is a rule of the shared core.

## 4. Improvements, ranked by (money saved or risk removed) / effort

$ effects use the plan's own model so they compare with $56.02 and $45.59; real effects scale with §3.1.

| # | Change | Effort | S1 $ | S87 $ | Risk removed |
|---|---|---|---|---|---|
| 1 | Wrap lines at 1,900 characters in `split_files`; assert ≤2,000 | 15 min | 0 | 0 | 288k characters silently cut (S1) |
| 2 | Merge: unit-prefixed ids before validation, filter by identity, dropped list with reasons | 30 min | 0 | 0 | invalid records rendered |
| 3 | Budget on full item text (or tokens), not `text` only | 10 min | +0.8 (hadis → 2 units) | ≈0 | 3×-oversized hadis unit |
| 4 | Required voices: all pages, honor `unit: surah`; `finish`/`merge` check block-or-yok per page | 1 h | ≈+0.3 | ≈0 | required voice missing without reason (1:1) |
| 5 | `cites` material for beyani-huli, nazm-islahi (and nazm-bikai, modern-bati) | 30 min | +0.3 | +1.8 (+0.8 with #9) | **bayānī voice declared absent on S87** |
| 6 | Meal: units write ayah pages only; one surah verdict (small unit over the ayah meal records, or the composer #11) | 1 h | ≈0 (−0.3) | +0.6 | 2–3 conflicting surah verdicts |
| 7 | POS fix (split on `;`, set membership); drop function words and formulae; phrase must contain a content lemma | 30 min | −0.3 | −0.8 | noise |
| 8 | Phrase-search material for untied sources (ITQAN, BURHAN, NASHR, MUSHKIL, SIBAWAYH) | 1 h | +2–3 | +1–1.5 | names, merit, chronology and Nashr readings unreachable |
| 9 | Page view: 12-word paragraph index + a per-page claims list (built once per page) instead of the 24/10 digest | 0.5 day | −6.5 digest +2.4 claims = **−4** | −11.2 +6 = **−5** | units can see claims (destek, itiraz, oncul, no restating) |
| 10 | Families: merge small groups of one surah into ≤13 units (e.g. dil = kesşaf + meani-nahiv + kiraat + icaz; modern = modern-arap + modern-bati + islahi), material kept in labelled sections | 2 h | **−5.5** | **−10.4** | fewer units, less digest |
| 11 | Per-page composer (anchors, near-dup merge by point, ≤5/paragraph, single verdicts, base-restatement check); units then need no digest at all | 1 day | ≈0 (−10 digest +7) | ≈0 (−17.5 +16) | restores single-page coherence |
| 12 | Balanced splitting: n = ⌈total/budget⌉ split at page boundaries; ≤15% overflow instead of a tail unit | 1 h | −2.0 | −1.1 | same page in two units of one group |
| 13 | Fewer turns: check.py takes all pages and parts in one call; one records file per page in ≤2 Writes | 1 h | −3 to −5 vs realistic | −8 to −12 vs realistic | the turns half of §3.1 |
| 14 | oncul with real capacity: per 2–3 pages, full prose or claims, script pre-searches of the claim lemmas, 25+ calls | 0.5 day | +5 to +10 | +10 to +20 | novelty audit actually done |
| 15 | lugat reads Asās entries + claims instead of dictionary.md; LISAN/LANE/TAJ on demand | 30 min | −0.3 | −1.5 | reads new evidence, not the base's own source |
| 16 | siir-sahid: search only words ≤5 hits per source, or only verify verses that tafsir material cites | 30 min | −0.8 | −2.0 | noise (user decision: "every source read") |
| 17 | Owners for usage.md (ayet_ayet / vucuh) and errata_candidates (duzeltme) | 1 h | +1.5 | +2.0 | two block kinds with no writer |
| 18 | Cost model: TURNS = 6 + 2·pages; output from the calibration fit; kapsam 70 tokens/item; tool results | 30 min | — | — | honest estimates before each run |
| 19 | Print too-common and capped-hit counts; give the agent the capped pairs | 20 min | 0 | 0 | near-silent caps |

Net, if 1–10 and 12–19 are adopted (without the composer) and costs are taken at the realistic level of §3.1: S1 is
about $75–90 ($11–13/ayah) and S87 about $65–80 ($3.4–4.2/ayah). The Fātiḥa is the heaviest surah (3.0M unique
characters against a whole-Qurʾān mean of 124k per ayah), so the S1 "now" target is tight. S87 should meet the
production target with margin only if the calibration confirms the output ratio.

### Assessments the review was asked for
- **Larger vs smaller units.** The budget is the wrong lever. Material is only 21% of S87's cost: the digest and
  fixed overhead are 79%. Larger units (families, #10) help because they cut repetitions of the digest and of the
  overhead, not because of material size. Keep material ≤75k tokens per unit, but budget on *total context*
  (material + page view) of about 120k, not on material characters.
- **Per-ayah vs per-surah units.** For production surahs (S87 ≈ 58k material tokens per ayah over all groups),
  per-ayah units would repeat the overhead 19× per group. Per-surah group or family units are right. Per-ayah
  splitting is right only for the Fātiḥa-scale pages (S1 1:1 alone fills 5 dirayet-cami units).
- **Digests vs full paragraphs.** Neither as is. Full prose (tags shortened) doubles the S87 page cost (+$17).
  Digests cost half that and still hide the claims. The best ratio is a 12-word paragraph index for anchoring plus a
  per-page claims list (zengin.md Step 2 done once, not 30 times), or the composer (#11) with no page view in the
  units at all.
- **Cheap pre-pass for RAZI-FULL.** Not now. RAZI-FULL contributes nothing on S87 after the duplicate rule (26 of 26
  segments are duplicates). On S1 it is about 5½ units (≈$7). A routing pass saves perhaps $3–4 there, but brings
  back the failure the okuma pilot measured (compression 1.6:1, 1.94× over estimate). It would need its routing
  verdicts audited as kapsam ("no silent losses"). Revisit for the long surahs (2, 3, 4) after calibration.
- **The proposed calibration batch** was nazm-bikai.u01, beyani-huli units, meal.u01, rivayet.u01, lugat.u01,
  akademik.u01 and hadis.u01: 8 S1 units, est. $10.9. Two of these units are blocked:
  - hadis.u01 S1: 37% of its characters are truncated, and it is at 3× budget.
  - meal.u01: surah-verdict conflict.

  Two are weak tests:
  - rivayet.u01 S1 is surah + 1:1, mostly Thaʿlabī: not typical.
  - akademik.u01 S1 is surah-only EQ passing citations.

  And the batch misses the three cases that decide cost and quality:
  - a digest-dominated wide unit, for production: S87 rivayet.u01 (20 pages, 259k context) or S87
    dirayet-kesşaf.u01 (19 pages, 19k material);
  - a material-heavy Arabic unit, for the output/thinking ratio: S1 dirayet-cami.u03 (pure RAZI-FULL);
  - oncul.u01, the riskiest design.

  **Proposed batch (after the fixes, re-plan first):**
  - S1: nazm-bikai.u01, beyani-huli.u01, meal (ayah-only), dirayet-cami.u03, hadis (re-split), oncul.u01,
    rivayet.u03.
  - S87: rivayet.u01, dirayet-kesşaf.u01.
  - lugat only if the user keeps the dictionary design.
  - About 9–10 units, ≈$14 by the old model; expect $20–35.

  **Measure per unit:**
  - measured cost split (cache write, cache read, output estimate) against each model term, then refit TURNS,
    thinking and output per material token;
  - turns against pages;
  - kapsam `durum` shares per group (ilgisiz = noise rate; kullanildi per 10k material tokens = yield);
  - drops and their reasons at check and at merge (anchoring failures from the page view);
  - the number of full-paragraph Reads;
  - wall-clock per turn (cache expiry);
  - transcript-audit coverage (should be 100% after #1);
  - for 1:1, recall against the reference page and the dosya2 trial, by locator family and by point;
  - cross-unit duplicate points on the shared pages (1:1, 1:7, S87 pages).

## 5. Decisions for the user
1. **Families or strict traditions.** May small groups of one surah share a unit, as labelled sections (#10: S1
   −$5.5, S87 −$10.4)? Or must every tradition have its own agent?
2. **What units see of the base:**
   - digest (now);
   - paragraph index + claims list (#9);
   - per-page composer and no page view in the units (#11).

   The composer is the only option that restores "each point once" and "≤5 per paragraph".
3. **oncul scope and budget** (#14). How many antecedent searches per claim, and per page or per surah? This is
   +$5–20 per surah but is the "antecedents of the base's own claims" requirement.
4. **Search-based groups** (poetry, wujūh by words, EQ passing citations). Is a scripted search plus the agent
   marking hits ilgisiz "reading the source", or should these be restricted or verified on demand (#16)?
5. **lugat** (#15). Dictionary sections (which the base already used), or Asās + on-demand lexica + claims?
6. **Untied ʿulūm and qirāʾāt sources via phrase search** (#8): +$1–3 per surah.
7. **Ayet_ayet and duzeltme owners** (#17): fold into vucuh and a small errata unit, or the composer?
8. **First full run.** S1 first (has the reference and trials; tests the "now" target), then S87 (the production
   cost), or S87 first because it is cheaper per page and representative.

## 6. Smaller code notes
- grup.py:396 runs the `SELECT id FROM src` query once per group (24 times). Harmless.
- `ayah_items` has an `n_ayat` parameter that it does not use. `root_items` (grup.py:241–264) is dead code since the
  lugat change.
- `no_material_sources` (grup.py:420) lists sources whose segments were all deduplicated as having "no material"
  (e.g. IBNASHUR-FULL, TAB-FULL on S1). Say "all segments duplicates of X" instead.
- turkce-sozluk lists KUBBEALTI, TDK, NISANYAN and PROJE as "no material" although it reads them through
  turkish.md.
- `est_tokens` uses Arabic/1.3 and other/2.0. HYBRID_PLAN C9 states /1.45 and /2.2. Either is conservative; pick one
  and fit it in the calibration.
- `excerpt` (grup.py:214) matches any "S:N" pattern, so for s = 1 it also matches volume or page references such as
  "Bd. 1: 45" in Nöldeke. The whole-page fallback keeps this from losing text, but the windows may centre on the
  wrong place.
