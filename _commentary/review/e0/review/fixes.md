# E0 review: consolidated fix list

Written 2026-09-28 by the adversarial reviewer of the four E0 outputs (supply, validate, checks, guard). I used local
scripts only: no model runs, no subagents, no commits. I wrote files only under `e0/review/`. I ran the authors'
tools from copies in `review/tools/`, so caches and outputs never landed in their folders. The copied caches were
deleted afterwards; `review/tools/supply/README.txt` says how to restore them.

## What I ran

| check | script / command | output |
|---|---|---|
| lint on every supply file (12 pages, 12 pull files, 128 entries files) | `tools/checks/lint.py <files> --kind supply` | `out/lint_supply.txt`, `out/lint_supply.json.gz` |
| [plain] marks vs root-dossier `activation_map.tsv` | `scripts/verify_plain.py` | `out/verify_plain.json` |
| Majāz mapping: header drift, a 25-entry sample, the oversized entry | `scripts/audit_majaz.py` | `out/audit_majaz.json` |
| supply rebuild (determinism, 2:282 size, 18:108) | `tools/supply/build_supply.py 88:7 29:38 2:282 18:108` | `tools/supply/sizes_measured.txt` |
| the supply's own bridge rule and pointer rule on the validator's HFT harness | `scripts/test_supply_bridge.py`, `scripts/test_supply_ptr.py` | `out/test_supply_bridge.json`, `out/test_supply_ptr.json` |
| check.py on E1 ×12, E2 ×6 and v15 (1:2, 1:6, 4:34) | `tools/checks/check.py` | `out/check/*.json` |
| check.py on synthetic quotes (edition footnotes, Majāz of S19) | `tests/*.md` | `out/check_synthetic*.json` |
| scorecard with the real E0 supply | `tools/checks/scorecard.py --ref 1:6 … --supply supply/out/1_6.md` | `out/scorecard_1_6.txt/.json` |
| guard: a 10-call hand sample, 24 random "present" calls, 30 lexeme "present" calls | `scripts/sample_guard.py`, `scripts/sample_guard_present.py [lexeme]` | `out/guard_*sample*.json` |
| checks selftest | `tools/checks/selftest.py` | 31/31 pass |

## Blockers (fix or decide before E3/E4)

**B1. The push/pull decision (the user's).** Pages as built:

| page | calibrated tokens |
|---|---|
| 88:7 | 39k |
| 29:38 | 137k |
| 19:73 | 155k |
| 18:96 | 167k |
| 18:86 | 198k |
| 4:34 | 336k |
| 5:6 | 460k |
| 2:282 (measured by me) | 708k (C 156k, D 160k, E 177k) |

- 18:86 alone is about one 200k context before the brief and thinking.
- The no-caps memory itself says push limits are a separate question.
- Decide the push set, or make runs read D, C and E from the pull file.

**B2. The probe ayat are answer-fed through the chain layers.** The agents missed this.

| page | line | what the chain data carries |
|---|---|---|
| 29:38 | 910 (HFT relay) | the whole watch-case bundle: «ٱلسَّبِيلِ وَكَانُوا مُسْتَبْصِرِينَ»: س ب ل B010 (eye film) + ب ص ر B001 + ع ن ك ب B001 (29:41) |
| 1:6 | F section (channel review) | the Fatiha aha: "the leading animal followed by the group" (م ل ك B008), "swallowing and disappearance through a passage" (ص ر ط B002, line 321), "an animal halted by fatigue" (ق و م B016) |
| 5:6 | F section | ك ع ب B002 (the Kaʿba) |
| 19:70, 19:75 (blind) | S19 channel review | "Waymarks, leading edge…", "second horse / musalli", "lead animal ahead of the train" |

- `check_supply.py` counts "6 of 6 ingredients present", which is trivially true on these pages.
- The lint marks line 910 only as `data-line`.
- **Fix:** decide whether the relays and channel reviews stay on for the probe ayat.
  - Option 1: a paired arm with `chains.hft_relay` and `chains.channel_reviews` off on probes.
  - Option 2: declare these probes non-blind, so they measure integration, not discovery.
  - Add a relay/chain context class to the lint.

**B3. One Majāz sqlite entry swallows the rest of the book.**

- Entry id 1308 ("لا يبغون عنها حولا", 18:108) holds 176,214 characters: all of surahs 19–114.
- **Supply:** the entry is mapped to 18:108. My rebuild of 18:108 gives G = 160,225 tokens of other surahs' text, attributed
  to 18:108.
- **check.py:** every Majāz quote from surahs 19–114 resolves to "entry 1308, heading لا يبغون عنها حولا". I tested the
  19:73 and 19:70 entries, which the E3 blind ayat show in G.
- **Fix:** cut entry 1308 at the surah-19 header. In `checks/common.py`, index the raw OpenITI entries with the same parser the
  supply uses, and report the mapped S:A.

## Major

**M1. Guard: most "present" calls in `guard_calls.tsv` are wrong.**

| sample | present calls correct |
|---|---|
| 24 random present calls (seed 7) | 9 (≈37%) |
| 30 lexeme present calls outside ع ن د (seed 11) | 5 |

- The lexeme rule for non_bare branches matches unvocalised homographs. It makes 1,042 of the 2,553 present calls (41%).
- Its errors:
  - ش ي ء B007 "longing/wonder" on every شيء;
  - ء ح د B006 Mount Uḥud on أحدا;
  - ء م م B016 particle أم on وأمه, ابن أم;
  - ك ت م B005 the katam plant on نكتم;
  - ش ك ر B007 the tribe on الشاكرين;
  - ص ب ر B016 a Ghassān clan on صبروا;
  - ج ع ل B011 the place al-Jaʿla on جعله (including 18:96);
  - ء ج ل B003 "ajal = yes" on أجلهم;
  - ل ي س B003 on every ليس.
- Partner and prep rules also misfire:
  - 18:86 غ ر ب B004 "tear ducts" on تغرب في عين;
  - 49:12 ء ك ل B014 "knife";
  - 90:20 ن و ر B010 on نار;
  - 2:245 ب س ط B004 with no يد.
- **The headline number misleads.** "False activation 0.55%" is a rate over 26,511 mostly trivial rows. It is not precision.
  - On the main eval set, presents are 263 true vs 146 other-branch calls, so precision is at most 64%.
  - The main-set denominator counts every dominant placement of any branch kind, while dev and test (776 and 427) count
    only collocation placements. The two are not comparable.
  - Non_bare branches never enter the false-activation denominator.
- **Fix:**
  - Lexeme matching must agree with the QAC lemma and POS, not the skeleton.
  - Block partner matches whose head form differs from the statement (غروب noun vs تغرب verb).
  - Report present-call precision.
  - Until then, label the file as unreliable for "present".

**M2. Guard audit sheet.**

- **Anchoring.** The script's call ("Betik: VAR/YOK/BELİRSİZ") sits in the same row as the user's ✓/✗, although the sheet is
  meant to give the clean estimate that the contaminated test split cannot. Hide the calls; `audit_key.tsv` already
  holds them.
- **No precision part.** The sheet has no rows from the detector's present calls outside dossier placements, so it
  cannot catch M1. Add a Part C: about 30 seeded present calls, including lexeme calls.
- **Part B question wording.** The questions are double negatives: "Kelime kalıpsız, tek başına bu anlamı taşıyamaz mı?
  Taşıyamazsa ✓" and "Bir kalıba bağlı değil mi? Değilse ✓".
- **Part B examples.** The example ayat are random occurrences of the root, usually of another branch (ك ف ل B007 "big
  beard" shown with 16:91 كفيلا). The "Betik (bu ayette)" column there is noise.
- **Formatting.** Some source tags are cut off: "(ayn", "(maqayis-v4".

**M3. Validator: the bridge exclusion does not test the rule the supply ships.**

- `links._bridge` accepts any single witness ayah (bridge30: 175 lines per ayah).
- The supply requires at least 2 co-occurring ayat and at least half of the lemma's ayat. On the same harness
  (`scripts/test_supply_bridge.py`, which reproduces ptr_card400 exactly at 3.25), the supply's rule scores:

  | part | lift | 95% CI |
  |---|---|---|
  | full, against a frequency-matched word | 1.99 | [1.22, 3.53] |
  | test half | 2.91 | [1.43, 6.52] |
  | dev half | 1.48 | [0.71, 3.16] |
  | against another branch of the same root | 1.54 | [1.05, 2.12] |

  Coverage is 1%.
- "At or below chance" and "contradicts Phase 2" are therefore unsupported for this rule. Its evidence is positive but
  thin. Under the validator's own dev-half rule it would still fail (dev lower bound 0.71).
- The supply's rule also has a flaw: 51 of 792 shown bridges reach "≥ 2 witness ayat" only by counting the focus ayah
  (for example حافظات + ق ن ت at 4:34, with only 33:35 listed).
- **Fix:** register the supply's rule as a variant and rerun `select_links.py`. Exclude the focus ayah from k and n.

**M4. The recommended config is not wired into the supply, and the two disagree.**

- `build_config.py` calls recommended_links.json "the supply builder's config", but `build_supply.py` reads only
  `supply_config.json`.

| link type | validator | supply |
|---|---|---|
| bridges | exclude | on |
| root co-occurrence (PMI > 2) | push | missing |
| D "rare pairings" (formula type) | excluded for within-ayah activation | shown |
| pointer levels: surah, rare-anywhere (≤ 12 ayat), inward | not validated | on |

- The rare-anywhere level alone takes 6.5k tokens at 29:38.
- The supply's own ayah-level pointer rule is fine. On the harness it scores 3.47 [2.42, 5.21], test half 3.40
  [2.13, 5.72], at least as good as ptr_card400.
- **Fix:** one config file that both read, or explicit switches in `supply_config.json` mapped to the validated variants.

**M5. Validator: "below the thresholds a type carries no signal" is false.**

| variant | lift | 95% CI |
|---|---|---|
| PMI > 1 | 1.29 | [1.18, 1.43] (test 1.25 [1.10, 1.43]) |
| quran-slm top 5% | 1.42 | [1.34, 1.51] |
| pointer with no card threshold | 2.34 | [1.83, 3.08] |

- The selection rule maximises the dev lower bound of lift, which is a precision criterion. The thresholds are
  therefore filters, not definitions.
- That is exactly the user's no-caps and no-premature-pruning question.
- **Fix:** present the thresholds as push limits (undecided), keep every candidate in the pull file, and correct the
  wording in `for_the_user`.

**M6. Validator: what "no signal" means.**

- Base (a) counts other words of the ayah as negatives, but HFT lists only the activators the readers cited. Unlabelled
  real activators sit in the base.
- A type that reaches many words scores near 1 even if it carries signal. For bridge30, lift against frequency-matched
  random roots is 1.25 [1.20, 1.30].
- "No signal" should read "does not single out the cited activator within the ayah".
- The formula null result is within-ayah only. Do not drop D's rare pairings on it: they carry the 18:96
  س و ي + ن ف خ formula.

**M7. The frozen scorecard mis-parses the E0 supply.**

- The pointer and neighbour headings contain "the window" and "the surah", so `TEXT_SECTION` excludes them.
- "Other surahs (N)" parallels and the F chain lines are not counted.
- `[plain: ref]` is not recognised, and the output claims "the supply carries no [plain] marks".
- On 1:6 it counts 11 link lines (only the bridge and same-surah sections) against 64 C lines plus 25 parallels, so
  "links used 7/11" is wrong.
- **Fix:** a new scorecard version with an explicit E0 section map; accept `[plain: …]`.

**M8. Script lens labels collide with the ruling's terms.**

- Section E labels a parallel "echo" (same root, other form) and "loaded" (a recurring partner, root level, no
  detector).
- A writer told to "mark echoes" and "state loaded words as usage" will read these script-computed labels as echo-tier
  or loadedness verdicts.
- **Fix:** rename them neutrally, for example `same-root-other-form` and `recurring-partner`.

**M9. E0 plan gaps (PHASE2 §3 and §8).**

- No Tier-3 digest was built.
- 2:282 was sized only for link lines. I sized the page: 708k tokens.
- The v5 relay listed in S0 ("HFT/v12/v5 relay") is absent. Say whether this is intentional.

## Minor

- **m1. Lint in supply mode.**
  - Pull-file JSON fields are classed as text lines (for example `"tr_gloss": "kırmızı damarlı ağsı göz perdesi"` →
    answer/text).
  - `data-line` lumps relay bundles with dictionary lines. Class JSON by key, and add a relay/chain context.
- **m2. Late material inside the "early" entries.**
  - About 15–20 entry texts (mostly Ṣiḥāḥ edition footnotes) carry "وفى اللسان", "لسان العرب وتاج العروس",
    "القاموس" or "قال ابن برى". They ship in `entries/*.md` (for example root_001077, root_000006).
  - check.py certifies such a quote as `early_entry exact` (synthetic test).
  - Strip the footnote apparatus in both tools.
- **m3. OpenITI markers.** `entries/*.md` keeps "PageV01P193", "ms0159" and "~~" in 127 files.
- **m4. Line and file shapes.** Page lines reach 23–25k characters (D partner lists), which the Read tool truncates at
  2,000 if a page is ever read rather than pushed. Pull files run 73k–322k lines, so runs need Grep.
- **m5. HFT relay order.** Relay lines keep HFT's section order (baseline → context_deltas → surprising_valid_outliers),
  which is an implicit class. Sort by branch or ref instead.
- **m6. Branches without guidance.** 20 branch lines have no branch_kind (Furūq-table fallbacks) and 7 are unresolved.
  The brief needs a default.
- **m7. Two Turkish glosses.** B (the TR entry's concept gloss) and H (the v2 result) can disagree for the same branch
  on one page.
- **m8. Pointer noise links the probe refs.** Wrong pointers repeat "15:26, 15:28, 15:33" on the 18:86 page: ح م و
  "in-law" وحماه and الحماة "calf muscle" are folded to ح م ء. Do not fold hamza when the lemma map disagrees.
- **m9. Inaccurate supply claims.**
  - "C[…] is often أصل يدل…": only 3 of 401 distinct C/F tags on the 12 pages start with أصل.
  - "Pages differ only in the pull-path line": the pull files also embed absolute paths.
- **m10. Scorecard denominator.** The "all branches" denominator counts every branch ref on the page (1:6: 125 against 43
  B lines).
- **m11. Validator frequency matching.** It uses 5 coarse bins. ء ل ه is excluded as a pointer target but kept among the
  base words, which slightly deflates the base.
- **m12. Blind surahs in the HFT set.** The HFT evaluation set includes S19 (71 cases) and S88 (44), 7 of them on the E3
  blind ayat themselves. Exclude them before freezing the thresholds.
- **m13. Guard unknowns.** Three unknown calls in my 10-call sample should be absent: 65:12 قدير, 3:112 كانوا,
  27:52 خاوية. This is conservative, but it inflates the unknown count.

## What held up

- **[plain] marks:** 82 of 82 equal the root-dossier dominant rows; none is missing and none is extra (`out/verify_plain.json`).
- **C/F tags:** they match branch_kind on all 1,370 B lines.
- **Sections:** all nine are present on every page.
- **Sizes:** they reproduce.
- **Determinism:** reproduced; only the paths differ.
- **Majāz raw-fallback mapping:** 25 of 25 sampled mappings are correct, and there is no surah-header drift (5 of 225
  unresolved phrases occur in a neighbouring surah, all explainable).
- **No forbidden labels:** no script-authored text carries a verdict, score, scene id or named example.
- **check.py:** no mis-resolution found in 21 real commentaries (960 tags; I hand-checked 14 sampled dictionary
  attributions and every non-exact or special case). The 2 unsourced quotes in v15 1:6 are really constructed Arabic.
- **Scorecard and check.py:** neither judges length.
- **Selftest:** 31/31 pass.

## The user's question 1: decisions that conflict (verified against NORTH_STAR, PHASE2 §10, memory and the E0 rules)

1. **Watch cases.**
   - The memory note `evaluation-depth-not-checklist.md` keeps 29:38, 18:86 and 18:96 as must-finds.
   - PHASE2 §10 row 8 and the E0 rules call every named example a probe.
   - Unresolved; the user must choose.
2. **Derived forms.**
   - Memory ruling 4: a derived form counts as the construction (tawallā without ʿan).
   - The E0 rule adds "when the dictionary's scope/what_is names that form or bare use".
   - The second is stricter, and PHASE2 §10 still lists derived forms as open.
3. **Plain sense.**
   - Memory ruling 6: "context alone doesn't count" governs latent readings only; the plain sense follows the canonical /
     root-dossier reading.
   - This is missing from PHASE2 §10 and the E0 rules. Read literally, the E0 echo rule turns dossier plain placements into
     echoes (ذ ك ر B004: 27 placements, none has لسان).
4. **Economics.**
   - No API and about $2 per ayah, against NORTH_STAR (Batch API, about $1 per ayah).
   - PHASE2 §3 routes 40+-word ayat, 2:282 and long-surah commentaries to the API. They now have no route.
5. **Use existing chains vs no answers in any supply.**
   - The chains *are* the answers on the S1, 29:38 and 5:6 pages (B2). The agents missed this.
6. **No caps vs one CLI call.**
   - Push limits are undecided while the pages run to 198k–708k tokens (B1).
7. **Link thresholds vs NORTH_STAR "no premature pruning; retrieval labels order and never filter"** (M5).
8. **Majāz "construction-level only".**
   - Most Majāz entries are sense glosses (زبر الحديد: قطع الحديد; عين حمئة: ذات حمأة). How the writer may use them is
     undefined.
9. **Dictionary order vs NORTH_STAR "branches have no order".**
   - Mild. Keep dictionary order and state in the brief that order carries no weight.
10. **Stale PHASE2 §10.**
    - It lacks the must-find exception and ruling 6, and marks derived forms as open.

**Not conflicts:**

- The E2 length "fails" were already retracted (EXPERIMENTS.md, commit bd72dd117).
- "[plain] vs dossiers-descriptive-only" is not a conflict: the dossier spec records "the dictionary branch of the plain
  reading", and ruling 6 relies on it.

## The user's question 2: the principle, as I understand it, and pushbacks

**The principle, in six points:**

1. The six-source dictionary alone decides where a sense lives.
2. A collocation or non_bare sense is the word's sense only where the construction the dictionary itself names is in the
   text: the partner, the preposition, the object slot, the formula, or a derived form the dictionary names.
3. For latent readings, context alone never licenses it. It may still be voiced as a marked echo with its basis ("in
   the phrase X this root means Y"), stretches named, nothing invented.
4. Plain readings follow the canonical / root-dossier reading even when they rest on context.
5. Construction-bound Quranic roles are stated as usage counts with refs.
6. Scripts annotate and record. Presence verdicts go only to the user, and nothing is deleted.

**Pushbacks:**

- **The early phrase is the evidence, not the scope note.** The model-written Turkish scope note and branch_kind are an
  index. The dictionary's own labels err: ح و ط B006 "passive only" vs the active أحاطت بـ; ج م ع B013 names Form III
  where the Quran has Form VIII. Audit before enforcing.
- **mixed_non_bare needs a rule.** It is the largest class (5,653 branches) and it is undefined. Say that the bare core
  is the sense and the bound facets are echoes unless their construction is present.
- **Semantic frames are a separate class.** Frame "collocations" (ذكر by the tongue, صلي fire-or-similar, أحاط complete
  knowledge) should be a frame-bound class tested by class (the partner's own dictionary definition), not by a literal
  partner.
- **"The dictionary names the form" is not checkable yet.** The statements are unvocalised (ولى I/II, يذكر I/V). The
  dictionary needs a form field. Until it has one, the writer judges, not a script. Sibling forms (جامع على / اجتمع على)
  need a ruling.
- **Echo governs statement, not chains.** It should govern how a sense is stated, not whether a chain may be built from
  it. Phrase echoes positively: the containment rule forbids "not X but Y".
- **Probes vs relays** (B2) and **thresholds vs pruning** (M5) need a decision before E3.
