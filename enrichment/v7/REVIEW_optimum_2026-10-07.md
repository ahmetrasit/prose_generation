# Enrichment v7: the optimum design under the focus-ayah direction

2026-10-07, review written read-only. Every number below was measured for this review from `corpus.sqlite`, the v7 work
directories, the v16 readings and run logs, or `digest.py report` (read-only). The commands are listed in the appendix.
Saved plans and reports were treated as claims. Token figures are estimates at about 3 characters per token. That ratio
is loosely calibrated on the 100:1 Sol tier-2 run: 52k input characters plus 30k output characters peaked at 41k tokens.

## 0. Recommendation in one paragraph

Keep the two digest tiers you already have. Point everything after them at **the focus ayah only**. Then run one writer call
per ayah against the **un-augmented r13 reading**.

Per surah, the steps are:
1. Tier 1 (Luna max) on the surah's own-ayah material. This is already done for S1 and S87–114. A script-found
   "quotation packet" is added to it (see 5.3).
2. Tier 2 (Sol high): one agent per ayah, after the whole surah's tier 1 is in.
3. One writer per ayah (Opus 5.5 high). It reads three inputs, all small: the reading with numbered paragraphs, the
   ayah's tier-2 views, and the ayah's Turkish meals.
4. The writer attaches one block per *question*, after the first paragraph that raises that question. Questions no
   paragraph raises go into a closing group after the last paragraph.
5. One check: every view is either cited in a block or listed as omitted with a reason.

Cross-referenced verses get no digests and no blocks. They are covered only where the focus ayah's own sources link to
them; this happens for 8–18 of a page's cited verses (section 1.6).

Cost: about **$1.1 per ayah** API-equivalent with Opus, or about $2.3 with Astra. The work per ayah is about 20–40k tokens
of input and three agents. That ends the circling: the material per call is bounded by the ayah, not by the page's
cross-references.

## 1. What the data says

### 1.1 The readings (base r13, no augment)

| Ayah | Characters | Words (incl. inline quotes) | Paragraphs [¶] | Headings | Distinct verses cited | augment9 page |
|---|---|---|---|---|---|---|
| 103:1 | 25,899 | 3,371 | 22 | 7 | 37 (+103:2) | 47,278 chars; 203 verse refs |
| 103:2 | 24,116 | 3,023 | 25 | 5 | 52 | none |
| 103:3 | 38,369 | 4,982 | 38 | 7 | 55 | none |
| 100:1 | 16,451 | 2,155 | 22 | 6 | 13 | none |
| 87:6 | 20,111 | 2,660 | 17 | 4 | 32 | 37,140 chars; 179 verse refs |

- **Only 47 base readings exist:** S1 (7), S87 (19), S100 (11), S103 (3) and S107 (7). Across them, the median is
  22,138 characters and 22 paragraphs (max 38), with a median of 37 distinct cited verses (max 62). The other S88–114
  surahs have surah folders (map, images) but no ayah readings yet. **Enrichment writers can only run on these 47 now.**
- **The augment9 layer is what made pages cite ~170–200 verses.** The base readings cite 13–55.
- **What the reading's "findings" are.** The r13 reading is built from the dictionary (`source:"ع ص ر,B001"`, 52
  lexicon citations on 103:1) and from Qurʾānic intertexts. On 103:1, the sections are:
  1. the oath;
  2. late and shrinking time;
  3. squeezing;
  4. Yūsuf's prison;
  5. holding and giving;
  6. refuge;
  7. whirlwind.

  The exegetical tradition is absent from the reading. That is exactly the gap enrichment fills. I take "initial findings"
  to mean these numbered paragraphs and their section headings.

### 1.2 Tier 1 (Luna max): complete for the S1/S87–114 own ayat

| Run | Chunks | Source chars | Cost (API-eq) | Peak > 120k tokens | `check.json` problems |
|---|---|---|---|---|---|
| s103-1 | 478 | 18,908,180 | $26.24 | 135 chunks | 0 |
| s103-23 | 196 | 7,665,214 | $10.79 | (many; see `report.log`) | 0 |
| s1_87_114 | 264 | 10,289,573 | $13.60 | (many) | 0 |
| test-20261007 | 7 | 246,840 | $0.76 | | 1 chunk (2 anchors) |
| **Total** | 945 | 37.1M | **$51.39** | | |

- **Total output:** 23,775 segments and 139,951 rows. The digest is not smaller than its source: digest/source characters
  are 1.11–1.23.
- **Every own-ayah segment of S1 and S87–114 has a tier-1 line.** I ran `digest.gather` on all 295 own ayat: 9,734
  segments, 12.29M characters, **0 missing**.
- **S103's own material is only 148 segments (255,864 characters).** The two S103 runs digested 26.6M characters, about
  100× that. The excess is the cross-reference scope.
- **Luna rate:** about **$1.4 per million source characters** (1.39 / 1.41 / 1.32 across the three runs).

### 1.3 The focus ayah's tier-1 rows (all runs pooled, as `merge.tier1_rows` does)

| Ayah | Rows | Rows after edition rule* | Sources | Tier-2 input chars (no anchors) | ≈ tokens | With anchors | Biqāʿī rows | Bint al-Shāṭiʾ rows |
|---|---|---|---|---|---|---|---|---|
| 103:1 | 382 | 349 | 43 | 61,372 | 20k | 94,205 | 18 | 28 |
| 103:2 | 295 | 266 | 45 | 46,568 | 16k | 73,524 | 20 | 5 |
| 103:3 | 511 | 507 | 45 | 96,471 | 32k | 136,533 | 24 | 51 |
| 100:1 | 380 | 358 | 45 | 61,513 | 21k | 89,491 | 15 | 17 |
| 87:6 | 229 | 221 | 43 | 39,842 | 13k | 58,392 | 8 | 0 |
| 1:6 | 792 | 792 | 44 | 153,420 | 51k | | | |
| 1:1 | 2,324 | 2,324 | 37 | 457,663 | 153k | | | |

\* **Edition-rule leak.** `merge.tier1_rows` does not apply the edition rule. Rows from a short edition reach the ayah
through segments digested for other verses, for example RAZI next to RAZI-FULL on 103:2 (22 + 22 rows) and IBNASHUR next
to IBNASHUR-FULL on 103:1. Across the 295 own ayat, this is 1,948 rows (3%), and 8–10% on 103:1–2.

**For comparison, the raw own-ayah corpus** (tafsir-type kinds; segments tied to the ayah):

| Ayah | Raw chars |
|---|---|
| 103:1 | 166,932 |
| 103:2 | 148,066 |
| 103:3 | 198,195 |
| 100:1 | 142,205 |
| 87:6 | 129,941 |

**Distribution over the 295 own ayat (tier-2 input chars, after the edition rule):**
- total 11.39M;
- median 29.6k;
- p90 68.4k.

21 ayat are above 80k and 7 are above 120k: 1:1, 1:2, 1:4, 1:5, 1:6, 1:7 and 112:1.

### 1.4 Tier 2 (Sol high): what exists

| Ayah | Rows in | Input chars | Views | Topics | Readable `.md` | Cost | Peak | Still current? |
|---|---|---|---|---|---|---|---|---|
| 100:1 | 308 | 51,918 | 85 | 10 | 24,634 chars (≈8k tok) | $0.2835 | 40,959 tok | **No:** 380 rows exist now; 72 (19%) are not in any view |
| 87:6 | 205 | 37,633 | 88 | 14 | 22,823 chars | $0.2035 | 33,211 tok | **No:** 229 rows now |

- **Sol rate:** about **$5.4 per million input characters** ($5.46 and $5.41 in the two runs).
- **`work/s103-1/tier2` is built but has not run.**
  - It holds 202 verses (103:1 plus every verse its augment9 page cites): 42,313 rows and 7.96M characters, which is
    about **$43** at the Sol rate.
  - Its 103:1 row file is also stale: 363 rows, against 382 now.
  - This build is the "too much even after tier 2". Each of the 202 view lists is about 20–30k characters, so a writer
    would face about 4–6M characters.
- **Focus-ayah tier-2 output is small.** It is about 0.47–0.61 of the input. Estimated sizes:

  | Ayah | Estimated views |
  |---|---|
  | 103:1 | 29–37k chars |
  | 103:2 | 22–28k |
  | 103:3 | 45–59k |

### 1.5 Material outside tier 1

- **Meal (Turkish translations).** 82 segments per ayah from 80 translations, all Turkish; 16 are the panel. Size per
  ayah, with distinct renderings in brackets:

  | Ayah | Chars | Distinct renderings |
  |---|---|---|
  | 103:1 | 3,721 | 65 |
  | 103:2 | 5,692 | 79 |
  | 103:3 | 13,098 | 78 |
  | 100:1 | 6,111 | 73 |
  | 87:6 | 7,301 | 74 |

  The whole meal for one ayah is 1–4k tokens. No table model is needed; the writer can read it raw.
- **Surah-level segments (a IS NULL).**
  - S103: 31,050 chars (tafsir 20,368, modern 5,403, reference 3,247, ishārī 1,578, naẓm 451).
  - S100: 19,368 chars. S87: 44,453 chars. Corpus-wide: 16.73M chars.
  - **`digest.gather` drops these without a line**: the `a<=?` test never matches NULL, so they are neither digested nor
    listed as skipped. This is a silent skip.
- **Non-verse-tied kinds.** Hadith, poetry, wujūh, lexicon, grammar, most ulūm and reference, and some modern works (for
  example BINTSHATI-IJAZ, NOLDEKE-GDQ and EQ) have no verse keys.
  - I tested a script lookup: the ayah's words (normalised, unique windows) searched in those kinds.

    | Ayah | Hits |
    |---|---|
    | 103:1 | DAMGHANI, IBNJAWZI-NUZHA, ITQAN (3-word key, 5.3k chars). With the one-word key «والعصر» it also finds **6 passages of Bint al-Shāṭiʾ's *al-Iʿjāz al-bayānī*** (p244, p245, p251, p415, p416, p567). |
    | 103:2 | 15 hits, about 21k chars |
    | 100:1 | 16 hits, about 16k chars, 5 of them BINTSHATI-IJAZ |
    | 87:6 | 9 hits, about 12k chars |

  - **The Bint al-Shāṭiʾ passages match the reading's own sections.** They cover:
    - the oath wāw (p244–245);
    - "what al-ʿaṣr squeezes out of man" (p251);
    - the root ʿ-ṣ-r across 12:36, 12:49 and 78:14 (p415–416, p567).

    This is the major bayānī voice, missed today because the work has no verse key.
  - **Hadith had 0 hits** with 3-word keys on all five ayat. With one word, hadith hits are noise («والعصر» = the
    prayer). Hadith reaches the ayah through the tafsir reports already in tier 1: Durr, Ṭabarī, Ibn Kathīr with
    gradings.
  - Poetry had 1 hit in the five ayat (on 100:1, one-word key).
- **Major voices.**
  - **Biqāʿī (BIQAI-FULL)** has rows on every focus ayah.
  - **Bint al-Shāṭiʾ (BINTSHATI)** has rows on 103:1–3 and 100:1, and 0 on 87:6, which her tafsīr does not cover.
  - **al-Khūlī's own work is not held:** the KHULI source has 0 segments. Only works *about* him are held
    (YKHULI-TAJDID, RIFAI-KHULI).

### 1.6 How far the focus ayah's own material reaches into the reading's cross-references

The tier-1 rows about the focus ayah carry a `mentions` field. Matching it against the verses the reading cites:

| Ayah | Reading cites | Of these, mentioned by the focus ayah's own rows | Top links |
|---|---|---|---|
| 103:1 | 37 | 8 | 93:1 (9 rows), 89:1, 92:1, 2:266, 12:36, 12:49, 78:14 |
| 103:2 | 51 | 17 | 95:4–6, 102:1, 70:19–22 |
| 103:3 | 54 | 18 | 90:17 (8), 3:200, 31:17 |
| 100:1 | 12 | 2 | 16:8, 100:6 |
| 87:6 | 31 | 11 | 75:16 (16), 75:17–19, 20:114, 2:106 |

So the connections that the tradition itself draws between the focus ayah and the reading's cross-references are already
in the focus ayah's material, at no extra cost.

## 2. Why v7 circled

Material per page followed the page's cross-references:
- 103:1 → 202 verses → 42k tier-2 rows → about 4–6M characters of views for one writer.

The focus ayah alone is:
- 349 rows;
- 61k characters into tier 2;
- about 30k characters of views out.

That is 1–2% of the volume. Every later fix (groups, budgets, `no_match` ledgers, 60-word cross-reference blocks) was a way
of carrying the 98% that the user has now dropped. With the focus-ayah direction, the problem disappears instead of
needing to be managed.

## 3. The design

### 3.1 Calls per surah, in order

| Step | Unit | Model, effort | Input per call (measured or estimated) | Output | Calls |
|---|---|---|---|---|---|
| T1 | 20k-char chunk of the surah's own-ayah segments plus its quotation packet | Luna max | ≤ 20k chars + brief | rows (existing format) | own material ÷ 20k (**0 for S1/S87–114 except quotation packets**) |
| T2 | one ayah (slices of ≤ 100k chars when the input exceeds 120k) | Sol high | rows of the ayah, edition rule applied: 103:1 61k chars ≈ 20k tok; 103:3 96k ≈ 32k tok; median 30k ≈ 10k tok | views (existing format) | 1 per ayah (7 exceptions of 2–5 slices in S1/S87–114) |
| W | one ayah | **Opus 5.5 high** (or Astra high) | reading [¶] + views `.md` + meal + brief (see 3.2) | `blocks.jsonl`, `omitted.jsonl` | 1 per ayah |
| R | script | none | | enriched page + `views/<ayah>.md` + notes | |

T2 runs only after the whole surah's T1 is complete. Neighbour-verse segments add rows to an ayah (100:1 grew from 308
to 380 rows), so tier 2 must wait for them.

### 3.2 Writer input, per ayah (one context, one pass)

| Ayah | Reading chars | Views chars | Meal chars | Brief | Total chars | ≈ tokens (+ ~12k agent overhead) |
|---|---|---|---|---|---|---|
| 103:1 | 25,899 | 29–37k (est.) | 3,721 | ~6k | 65–73k | 22–24k |
| 103:2 | 24,116 | 22–28k (est.) | 5,692 | ~6k | 58–64k | 19–21k |
| 103:3 | 38,369 | 45–59k (est.) | 13,098 | ~6k | 103–117k | 34–39k |
| 100:1 | 16,451 | ~30k (refreshed; 24.6k today) | 6,111 | ~6k | ~59k | ~20k |
| 87:6 | 20,111 | ~25k (refreshed; 22.8k today) | 7,301 | ~6k | ~58k | ~19k |

- **Reading:** the base r13 file with `[¶n]` numbers. Augment9 is not used.
- **Views:** the readable `.md` that merge.py already renders: view id, text, note and holders, with `+`/`−` for
  prefers/rejects. Add one script field per view: `→ verses`, the union of its rows' `mentions`. The writer then sees
  which views touch verses its paragraphs cite.
- **Meal:** all renderings grouped by identical text, translator names attached, panel members marked.
- **Not given to the writer:**
  - the tier-1 notes and anchors (they are one link away, on the views page);
  - other verses' views;
  - augment blocks;
  - the dictionary (the reading already used it).
- **Delivery:** for Opus, one prompt file read whole. The 10k-character parts are only a Codex clipping workaround, kept
  for Astra.

### 3.3 Where blocks attach, and how they stay short

- **One block answers one question** that the views answer. Examples:
  - "ʿAṣr: zaman mı, ikindi mi, namaz mı, çağ mı?"
  - "Yemin neden zamanla?"
  - "Âdiyât: atlar mı, develer mi?"

  Each block names every position as a clause: who holds it and the deciding reason, with `+`/`−` made visible. Minor
  variants are counted, not spelled out ("… ve beş kaynakta daha"). It cites view ids only.
- **Attach** after the first paragraph whose point the question bears on. On 103:1, the likely placements are:

  | Topic | Paragraph(s) | Basis |
  |---|---|---|
  | the referent of al-ʿaṣr | ¶2, which itself asks "günün ikindisi mi, çağ mı, zamanın kendisi mi" | 141 of 382 rows touch it |
  | the oath | ¶1 | 94 rows |
  | time as capital / loss | ¶5–6 | 26 rows |
  | Bint al-Shāṭiʾ's root analysis | squeezing and Yūsuf sections | quotation packet |

- **Questions no paragraph raises go to one closing group after the last paragraph** ("Ayet üzerine kaynaklarda").
  Surah-wide topics (dating, name, merits such as al-Shāfiʿī's saying) go only on the surah's first ayah page.
- **Ceilings:**
  - about 150 words per block;
  - about 900 words per ayah (the readings run 2,155–4,982 words);
  - in practice 5–9 blocks per ayah. Tier 2 gave 10 and 14 topics on 100:1 and 87:6.
- **Arabic only as terms already present in the views.** Exact Arabic words live on the linked notes. This removes the
  verbatim-quote check from the writer stage.
- **Major voices:** when Biqāʿī, Bint al-Shāṭiʾ or the bayānī moderns (Sāmarrāʾī) hold a position, the block names them.
  The views page lists which major voices have no material for the ayah, so their absence is stated, not silent.
- **Placement in the published page:** blocks sit after the paragraph, and after its augment blocks if the augment9 page
  is the one published. They are delimited by the existing `<!-- v7:enrich -->` markers, and the strip check gives the
  frozen page back byte for byte.

### 3.4 Reused, dropped, still needed

| Item | Decision |
|---|---|
| Tier 1, all 139,951 rows | **Reused as is.** Rows about other verses become those verses' own-ayah rows when their surahs come. Nothing is redone. |
| Tier-1 brief and checks | Unchanged |
| Tier 2 | **Still needed, focus ayah only.** It is the middle link of the one-stop-shop chain (block → views → notes → source). It cuts the writer's input by about half, and it is cheap ($0.21/ayah average). Letting the writer read 349–507 raw rows instead was considered and rejected: the writer would then do two jobs, there would be no views page to link to, and Fatiha ayat (150–460k chars) would not fit. |
| Tier 2 for 100:1, 87:6 | Re-run when their surahs are written: 19% and 10% of today's rows are not covered |
| `s103-1/tier2` (202 verses) | **Do not run** (≈ $43 avoided) |
| `merge.py` | Two small edits: apply the edition rule in `tier1_rows` (print a NOTE with the count); slice inputs over 120k chars (whole sources, oldest first) |
| `write.py` | Focus mode: one group; inputs reading + views + meal; outputs blocks + omitted; drop `cited.pK`, `--budget` groups, the (¶ × verse) ledger and the Arabic-quote check; keep `render` and the strip check |
| `briefs/write.md` | Rewrite for focus-only, using sections 3.3 and 3.5. About 5k characters, as now |

### 3.5 Cross-references, surah level, non-verse families: what and in what order

1. **Cross-referenced verses: no digests, no blocks.**
   - They are covered where the focus ayah's sources link to them (section 1.6), through the `→ verses` field.
   - Optional later, at zero model cost: the render adds one link line per paragraph to the cited verses whose own views
     page already exists. Every verse gets its own page when its surah is done.
2. **Meal:** in the writer's input from the first test on. One block on how the translators render the key word(s),
   naming translators and counting the rest.
3. **Quotation packet** (non-verse-tied kinds, found by script):
   - **Key:** the ayah's normalised text, plus its word windows that occur in no other ayah. Diacritics, alif/yā
     variants, verse numbers and brackets are stripped. The window minimum is 1 word for ulūm, wujūh, modern and
     reference, and 3 words for hadith, sīra and poetry.
   - Each hit (the whole segment, or ±1,500 chars) is added to that surah's tier-1 chunks with the ayah as its verse.
   - Luna marks irrelevant hits `none`.
   - Cost: about 5–40k chars per ayah, about $0.01–0.06.
   - This brings in Bint al-Shāṭiʾ's *Iʿjāz*, al-Burhān, al-Itqān, Bāqillānī and wujūh by the same path as everything
     else.
4. **Hadith beyond the tafsir reports, poetry witnesses for words, EQ/Sinai/TDV term articles:** a later "word stage",
   keyed by term or root. It is not in this design. The views page footer states "not consulted: hadith collections,
   poetry, term encyclopaedias" until that stage exists.
5. **Surah-level segments:** these belong to the surah-commentary page's enrichment (images.md), a different page. For now
   the build prints them as `NOTE surah-level: N segments, X chars, reserved for the surah page` and records them in the
   manifest. Today they are silently dropped.

### 3.6 No silent failures, kept simple

| Stage | Check (script, a few lines) | Already exists? |
|---|---|---|
| T1 | every segment answered; every anchor verbatim | yes |
| T2 | every row id in at least one view | yes |
| W | (1) every view id of the ayah is cited by a block or listed in `omitted.jsonl` with a one-line reason; (2) every block names an existing ¶ (or `end`), cites existing view ids and is under about 180 words | replaces the current two |
| R | strip check (frozen page back byte for byte) | yes |

Every build also prints, and records in its manifest:
- NOTE lines for short-edition rows dropped, slices, surah-level segments reserved and families not consulted;
- the count of omitted views per ayah;
- tier-1 rows that arrive after an ayah's tier 2, listed and never merged silently.

Nothing else is added: no hashes, no second model, no review pass.

## 4. Cost

### 4.1 Per ayah (API-equivalent at the saved rates)

| Step | Basis | Per ayah |
|---|---|---|
| T1 own material (new surahs) | 247.4M verse-tied tier-1 chars corpus-wide × $1.4/M ÷ 6,236 ayat | ≈ $0.06 (**$0 for S1/S87–114, sunk**) |
| Quotation packet | 5–40k chars × $1.4/M | ≈ $0.01–0.06 |
| T2 Sol high | 11.39M chars × $5.44/M over 295 ayat | **≈ $0.21 average**: 103:1 $0.33, 103:2 $0.25, 103:3 $0.52, 100:1 $0.33, 87:6 $0.22; Fatiha ayat $0.8–2.5 |
| W Opus 5.5 high | ≈ 45k-token context written once to cache ($5/M), about 6 turns of cache reads ($0.20/M), 15–30k output tokens including thinking ($20/M) | **≈ $0.8** (range $0.5–1.3) |
| W Astra high (alternative) | same profile at $10 / $1 / $50 | ≈ $2.0 |
| **Total** | | **≈ $1.1 (Opus) or ≈ $2.3 (Astra)** |

- **Opus reference point:** the v16 103:1 reading writer (`run.log.json`) had 7 turns, wrote 93.6k tokens to cache, read
  355k from cache and produced 26–48k output tokens, for $1.06–1.50. The enrichment writer has about half that context.
- **Fatiha ayat:** writers about $1.5 each, because their views are larger.
- **Whole Quran at this design:** about $6.6k.

### 4.2 Sunk vs remaining

| | Amount |
|---|---|
| **Sunk, v7 tier 1** | $51.39. 12.29M of the 37.1M digested characters (33%, ≈ $17) is S1/S87–114 own material. About $34 digested other verses, which is prepaid tier 1 for future surahs and not wasted. |
| **Sunk, v7 tier 2** | $0.56 (Sol $0.48 and Luna $0.08 on 100:1 and 87:6) |
| **Avoided** | s103-1 cross-reference tier 2 ≈ $43. Cross-reference writers for 103:1 were never costed and are now not needed. |
| **S103 remaining** | T2 $1.10 + quotation packets ≈ $0.05 + 3 writers ≈ $2.4–3.0 = **≈ $3.6–4.2 for the surah (≈ $1.3/ayah)** |
| **S1/S87–114, the 47 ayat with readings now** | T2 ≈ $15.5 (S1 alone $8.6) + writers ≈ $40 + packets ≈ $1 = **≈ $57** |
| **S1/S87–114, all 295 ayat** | T2 ≈ $62 + writers ≈ $240 + packets ≈ $5 = **≈ $305 (≈ $1.03/ayah)**. Writers for the other 248 wait for their readings. |

Actual cash is $0 (Codex and Max subscriptions). The binding limit is Codex usage: about 295 Sol tier-2 agents for S1 and
S87–114, mostly small.

## 5. What to stop

1. **Scope expansion by page:** no `--page` builds in digest, merge or write.
   - Do not run `work/s103-1/tier2` (202 spawn files).
   - Do not run `s12_17_19` or `s12_17_19_20k_exact` (862 chunks, 16.0M chars, ≈ $22) until S12 and S17–19 have
     readings.
2. **Cited-verse machinery:** the (paragraph × cited verse) ledger, `cited.pK` inputs, `--budget` groups and 60-word
   cited-verse blocks.
3. **Giving the writer full tier-1 notes and anchors,** and the Arabic-quote verbatim check that came with them.
4. **Writing against augment9.** Paragraph numbering comes from the base r13 reading.
5. **New design rounds on tiers 1 and 2.** Their briefs, formats and checks stay as they are. Only the two `merge.py`
   edits in 3.4 are made.

## 6. Risks

1. **Attachment on a lexical reading.**
   - 103:1 is mostly a root meditation, and the tradition's material clusters on ¶1–2 and ¶5–6.
   - Risk: the writer stretches a block onto a paragraph it does not fit.
   - Mitigations: the closing group, a brief that says "never stretch", and the user judging the 103:1 test.
2. **Stale tier 2.** Views made before a surah's tier 1 finishes miss rows (100:1: 19%). The rule is that T2 waits for
   the surah, and late rows are printed.
3. **Heavy ayat.** Seven ayat over 120k chars (six in Fatiha, plus 112:1) need slicing, and views can then overlap
   across slices. If the sliced views exceed about 120k chars (likely only 1:1, 1:2 and 1:7), one extra Sol pass over
   the views (same brief) may be needed. Decide this at Fatiha, not now.
4. **Writer omits too much, or writes too long.** The check prints the count of omitted views and the words per block;
   the user sees both. A third to a half of tier-2 views are singletons (100:1: 28/85; 87:6: 46/88). Most should be counted
   inside a block, not omitted.
5. **Major-voice gaps that are real:**
   - al-Khūlī's own work is not held;
   - Bint al-Shāṭiʾ's tafsīr covers few surahs (0 rows on 87:6).

   The quotation packet recovers her *Iʿjāz*. The footer states the gaps.
6. **Tier-1 context overruns** (135 of 478 s103-1 chunks peaked over 120k tokens). The 20k-char default for new builds
   addresses this; outputs passed the checks.
7. **Estimates.** Token counts use about 3 chars per token. The test below gives the real writer figures.

## 7. The smallest decisive test: 103:1

**Steps:**
1. Quotation packet for 103:1, run through tier 1: 1 Luna max agent, about 40k chars, about $0.06. It includes the six
   Bint al-Shāṭiʾ *Iʿjāz* passages.
2. Tier 2 for 103:1 in a new run (e.g. `s103-focus`), with the edition rule: 1 Sol high agent, about 61k chars in,
   about $0.33.
3. Writer: 1 Opus 5.5 high agent on the base reading (22 ¶), the views and the meal (3.7k chars), about $0.8.
4. Check, then render: `103_1.enriched.tr.md` plus `views/103-1.md`.

**Total about $1.2 API-equivalent** ($0 actual). Optionally, an Astra high writer on the identical input decides the
writer model, for about $2.0 more.

**What the test decides:**
- whether the blocks read as a complete map at the right length on the hardest attachment case, a lexical reading;
- whether the closing group is acceptable;
- whether the views page works as the "details" link.

**If it passes:** 103:2–3 (about $2.5), then the remaining 44 ayat with readings (about $55), surah by surah.

Code needed before the test, all small:
- the `merge.py` edition rule;
- the quotation-packet option in `digest.py build`, plus the surah-level NOTE;
- `write.py` focus mode, with the new two-item check;
- the rewritten `briefs/write.md`.

## Appendix: how the numbers were obtained

- **Readings:** `wc`, and a paragraph and `source:` regex count over
  `_commentary/v16/out/<S>_<A>/DM.r13.images.r13.map3.nohft.tool.tool.tool/<S>_<A>.reading.tr.md` (and over the
  `augment.augment9.opus/` copies). Existing readings were found by globbing `_commentary/v16/out/*_*`.
- **Tier-1 rows:**
  - All `work/*/out/luna-max/c*.jsonl` loaded once, deduplicated by `loc` (as `merge.tier1_rows` does), and indexed by
    `verses`.
  - Sources come from `seg.src`; the edition rule drops X when X-FULL has rows on the same ayah.
  - Characters are rendered as `[id] speaker | stance | claim` plus about 45 chars of id, which matches
    `merge.py`'s 68,113 for 103:1 before the edition rule.
- **Coverage:** `digest.gather()` over the 295 own ayat, compared with every `loc` in the tier-1 outputs.
- **Costs:**
  - `python3 -B enrichment/v7/digest.py report s103-1` (read-only; $26.24, 135 chunks over 120k).
  - `report.log` of s103-23 and s1_87_114.
  - `test-20261007/tier2/run-sol.log`.
  - Saved rates: `enrichment/v5/common.py` RATES and `_commentary/v16/agentrun.py` RATES.
  - v16 writer usage: `103_1/.../run.log.json`.
- **Tier 2:** `test-20261007/tier2/manifest.json` and `out/sol-high/*.jsonl|.md`; `s103-1/tier2/manifest.json` (202
  verses, 42,313 rows, 7,964,468 chars; `out/sol-high` empty).
- **Corpus:**
  - `corpus.sqlite`, opened read-only: segments per kind tied to each ayah; surah-level `a IS NULL` sums.
  - The verse-tied tier-1 total of 247,443,153 chars excludes short editions that have a FULL sibling.
  - Meal segments by `kind='meal'`, panel from `meta.panel`.
  - Quotation tests: diacritic-stripped substring search over the 292,703 non-verse-tied segments.
- **Mentions overlap:** tier-1 `mentions` of the focus ayah's rows, intersected with the reading's `source:S:A` set.
