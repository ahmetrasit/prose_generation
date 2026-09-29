# Experiments after the review

2026-09-28. The user approved the experiments under $30 each; E3 and E6 are deferred (see below). Code and outputs are
in `experiments/`. Every call ran Opus 5.5 at effort high through `claude -p` in safe mode from a temp directory (no
CLAUDE.md, memory, skills or hooks). No call was rerun, and every call was logged.

## Spend

| experiment | calls | cost |
|---|---|---|
| E1 | 12 | $9.65 |
| E2 | 12 | $8.38 |
| total | 24 | $18.03 |

No failures.

## E1: memory permission without a ledger

**Question.** Phase 1 and 2 found that dictionary-fed runs cite almost no passages outside the surah. Is that because
they were told "work only from the supplied evidence"? Every dictionary-fed run that had permission also carried
v11's "collect every finding" ledger, so the two causes were mixed.

**Design.** The v9 dictionary arm rebuilt byte for byte: brief `write_v10.md` (md5 dddcd1b2), the same system
prompt, context.md and 01_dictionary.md. The only change is the evidence clause, which adds "and your own knowledge of
Arabic and the Quran", as the cold arm had it. Six ayat, 2 replicates each (`experiments/e1_permission.py`, scored by
`e1_score.py`).

**Results**, measured against the old runs on the same ayat:

| ayah | outside-surah refs: cold / dict / permitted (rep1, rep2) | dictionary-only quotations: dict / permitted | thinking (k tokens): cold / dict / permitted | cost: permitted |
|---|---|---|---|---|
| 1:2 | 19 / 0 / 3, 4 | 29 / 16, 17 | 14 / 22 / 8, 12 | $0.47, $0.54 |
| 1:6 | 12 / 0 / 15, 12 | 22 / 22, 16 | 9 / 16 / 13, 11 | $0.60, $0.55 |
| 4:34 | 6 / 0 / 6, 6 | 27 / (quoted outside tags) | 45 / 27 / 15, 16 | $1.52, $1.60 |
| 18:86 | 3 / 3 / 3, 3 | 13 / 10, 11 | 12 / 38 / 18, 13 | $1.30, $1.15 |
| 100:1 | 7 / 0 / 10, 1 | 12 / 13, 9 | 15 / 22 / 11, 11 | $0.50, $0.50 |
| 100:6 | 7 / 2 / 8, 4 | 15 / 11, 8 | 9 / 12 / 8, 10 | $0.46, $0.47 |

**Findings:**

1. **Permission alone largely restores outside-surah reach, to about the cold arm's level.** No ledger is needed.
   v11's "median 30" came from its ledger ("collect every finding"), not from permission.
2. **The dictionary stays in use.** Permitted runs still quote the dictionary's rare senses, somewhat less than the
   no-permission arm. On 4:34 they quoted it in plain quotation marks instead of `{ar:…}` tags, so the source
   checker cannot see those quotes. The brief must require the tag for dictionary quotations.
3. **Output shape and cost.** Permitted, no-ledger output is 15–30k tokens (median about 19k), not the 50k the cost
   critic assumed. A permitted call costs about $0.46–0.60 for short ayat and about $1.1–1.6 for long ones on the
   CLI. Phase 2 production estimates should use this shape.
4. **Noise.** The two replicates share 24–70% of their cited passages (median about 0.58). No single run can decide
   anything.
5. **18:86** (contaminated: the old brief's example lists 15:26/28/33). Replicate 2 reached the observer framing:
   Iblīs refuses to prostrate to a human "from dark clay" (15:33), the moment returns in 18:50, and "the gaze that
   sees the human as nothing but the mud it's made of" is named as a live danger in the surah. Replicate 1 did not.

## E2: integrating two existing readings

**Question.** Can one Opus call compose a single commentary from two finished readings (the cold arm and the
dictionary arm) and keep what both found, without turning into a catalogue?

**Design.**

- A new integration brief (`experiments/prompts/e2_integrate.md`): the cold arm's writing rules, minus the two known
  leaks, plus integration rules, memory marked as [bellek], and the user's two rulings.
- Three ayat (18:86, 4:34, 1:6), 2 replicates each, with the reading order swapped.
- One return call per replicate that saw the script-computed sentences the commentary did not carry.
- Criteria fixed before the run (`e2_score.py`):
  - C1 recall ≥ the better input's + 0.10;
  - C2 form: words ≤ 1.5 × the longer input, longest paragraph ≤ 300 words, negation rate ≤ the inputs'. **Corrected
    after the run:** judging length breaks the user's no-caps rule ("checks report length and never judge it"), so
    C2 now judges only the negation rate and reports length;
  - C3 the user's blind read.

**Results:**

| ayah | pooled items | recall: cold / dict / integrated (rep1, rep2) | C1 | words: longer input / integrated | C2 |
|---|---|---|---|---|---|
| 18:86 | 120 | 0.65 / 0.82 / 0.93, 0.93 | pass, pass | 2,753 / 3,226, 3,302 | pass, pass |
| 4:34 | 138 | 0.70 / 0.71 / 0.98, 0.99 | pass, pass | 3,659 / 4,590, 4,795 | fail (negation 6.97 > 6.01), pass |
| 1:6 | 61 | 0.57 / 0.57 / 0.95, 0.97 | pass, pass | 1,643 / 2,542, 2,526 | pass, pass (the original "fail" was length only: retracted) |

- The integration call cost $0.41–1.11 and used only 2–6k thinking tokens.
- The return call changed nothing in 6 of 6 cases: the output was byte-identical to the draft. Only 1–5 sentences
  were left unselected in each case, and those calls cost $3.85 for no effect. **Drop the return turn**, or trigger
  it only when the unselected list is long.

**My reading of 1:6 (rep1).**

- It genuinely integrates. The cold arm's Quran web (37:118, 48:2, 6:153, 18:1–2, 11:112, 41:30, 7:16–17, 36:61,
  3:51) sits together with the dictionary arm's lexicon (the staff that goes ahead, hudiya fa-htadā, the swallowing
  road through Ibn Fāris, qawma, hedy as gait).
- It builds and resolves a tension neither input had. The guide leaves the walking to the walker; the swallowing road
  carries him; then Kitāb al-ʿAyn's istiqāma ("yedeğe girip gidişi kesintisiz süren") shows that a led mount still
  walks.
- It applies the echo ruling unprompted ("qāma l-māʾu … kalıplaşmış kullanımlardır ve burada ancak yankı olarak
  duyulur") and marks its one memory addition (ka'ada as the opposite of qāma) with [bellek].
- What it lacks: the surah chain (the trodden road in naʿbudu, the waymarks), because neither input had it.

**C3 (the user's blind read) is pending.** Three pairs are in `experiments/e2/blind/` (`<ayah>_A` / `_B`). Each pair
is the integrated commentary against the better input. The key is in `KEY_open_after_reading.json`.

## What E1 and E2 change

- **Integration from finished readings works mechanically.** It passed recall in 6 of 6 runs. On form (negation rate
  only, after the no-caps correction) it passed 5 of 6.
- **The permitted single reading (E1) already carries both slices on some ayat** (1:6: 15 outside refs and 22
  dictionary quotations). So the real contest is F1 (one permitted reading) against B (a memory reading plus a
  dictionary reading plus integration, with no return turn). That is E3.
- **Cost with the measured shapes, on the CLI:**

  | design | per ayah |
  |---|---|
  | F1 | about $0.5–1.6 |
  | B | about $1.3–4 |

  Production through Batch would be roughly half of each.

## E0: the free layer (supply, link validation, checks, construction guard)

**What was built** (`e0/`). Five agents wrote local scripts; no model read or wrote any commentary.

| part | folder | what it is |
|---|---|---|
| supply v0 | `e0/supply/` | a per-ayah page (sections A–I), a pull file with every full list, and an audit file for the user only; 12 ayat |
| link validator | `e0/validate/` | tests each link type on the HFT surprise set: does its path reach the word that activated a branch more often than chance? |
| checks | `e0/checks/` | `check.py` (source of every Arabic quotation), `lint.py` (contamination), a frozen `scorecard.py`, a self-test |
| construction guard | `e0/guard/` | for every occurrence of a root: does each collocation-bound branch's construction stand in the text? A record for the user only, plus an audit sheet |
| adversarial review | `e0/review/fixes.md` | three blockers, nine major and thirteen minor findings |

**What held up in the review:**

- the [plain] marks: 82 of 82 match root-dossier;
- the C/F tags: they match branch_kind;
- determinism;
- Majāz raw-text mapping: 25 of 25 sampled;
- no script-authored verdict, score or scene id anywhere a model reads;
- `check.py` on 21 real commentaries;
- all 6 watch ingredients and all 17 probe items on the pages.

**Fixed after the review** (details in each folder's README):

| finding | fix | effect |
|---|---|---|
| B3 Majāz entry 1308 held surahs 19–114 | sqlite entries end at the first surah header; checks read the supply's mapped index | 18:108's Majāz section: about 160k tokens → 133; surah-19 quotes resolve to their own entries (19:73) |
| M1 guard: most "present" calls wrong | lexeme matches need the same word class, no vowel clash and no sibling branch naming the same lexeme; partner/preposition matches need the same head class | present calls 2,553 → 1,597; lexeme presents 1,042 → 218 (all 21 outside عند right by hand); main-set precision at dossier placements ≤ 64% → 70%; recall 72.3% → 70.9% |
| M2 audit sheet anchored and had no precision part | script calls hidden; positive questions; a new Part C (30 present + 10 absent calls, shuffled); dossier examples only | ready for your read: `e0/guard/audit_sheet.md` |
| M3 bridge rule untested, focus counted | the supply's rule registered in the validator; focus ayah removed from k and n | full 2.24 [1.32, 4.05], test half 2.91 [1.39, 6.80], dev lower bound 0.75: positive but thin |
| M4 recommended links not wired | root co-occurrence (PMI > 2) added to the supply; a `_validation` map in `supply_config.json` | 0–8 co-occurrence lines per page (31 on 5:6) |
| M5, M6 thresholds read as "no signal" | the validator now says thresholds are push limits, and what "excluded" means | PMI > 1 still scores 1.28 [1.17, 1.42] |
| M7, m10 scorecard mis-parsed the page | explicit E0 section map; `[plain: …]` read | 1:6: 40 non-plain branches (was 125), 136 link lines (was 11) |
| M8 lens labels "echo", "loaded" | renamed `same-root-other-form`, `recurring-partner` | — |
| m1 lint | a `relay` context for the chain section; JSON lines classed by key | the 29:38 relay bundle now shows as `answer/relay` |
| m2, m3 late footnotes and markers in early entries | shared `e0/textclean.py`: 6 Ṣiḥāḥ edition notes (quoting Lisān, Tāj, Ibn Barrī, manuscripts) marked as omitted; OpenITI markers stripped | a late quote is no longer certified as early |
| m5 HFT relay order leaked its classes | sorted by branch | — |
| m8 folding joined حماة / وحماه to حمإ | a stem left ending in alif after suffix removal no longer joins a hamza root | the calf-muscle pointer to 15:26/28/33 is gone; bare حما (a true homograph) remains |
| m12 blind surahs in the validator's set | S19 and S88 held out (3,325 → 3,210 targets) | the push set is unchanged: pointer 3.05, neighbours 7.76, co-occurrence 2.02 |
| M9 plan gaps | 2:282 sized: 710k tokens; the 4:34 page is itself a Tier-3 page (surah 4 has no HFT); v5 relay left out on purpose (98% of its branches come from the sources the page relays) | — |

The checks are now scorecard version 2 (37 of 37 self-test controls pass, re-frozen). Nothing had been scored with
version 1 for a decision.

**Still open (your decisions):**

- **B1 push limits.** Pages run 39k–461k tokens, and 2:282 is 710k.
- **B2 answer-fed probes.** On the probe ayat, the chain and relay layers carry the answers (29:38's HFT relay line
  holds the whole eye-film bundle; the S1 channel review holds the Fatiha items).
- **Bridges.** Whether the supply keeps its bridge rule.
- **Pointer levels.** The unvalidated rare-anywhere level.

## Deferred and pending

- **E3** (F1 vs B on 29:38, 18:86, 18:96 and 4 seeded blind ayat, with replicates; about $40–70) and **E6** (one blind
  short surah end to end; about $40–80). Both come after the small experiments and need a separate approval.
- **E4 as specified cannot be reproduced faithfully.** The praised 29:38 pilot was written inside an interactive
  session with no saved brief. Approved replacement: the praised reading as the fixed reference, the compact supply
  run twice on 29:38 (about $3–5). E0 is built and fixed, but E4 waits for B1 (what the 137k-token 29:38 page pushes)
  and B2 (whether its HFT relay, which carries the eye-film bundle, stays on).
- **E5** needs an API key.
