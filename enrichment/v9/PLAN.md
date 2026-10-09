# Enrichment v9: verse maps once, page writers that match

Status 2026-10-08: plan agreed with the user; nothing built yet. Supersedes the open parts of `enrichment/v7/PLAN.md`
and the v8 sift. Keeps v7 tier 1 (`digest.py`) and the tier-2 work as inputs. Demonstration on the 103:1 page:
`demo-103_1.md`.

## Decisions (user, 2026-10-08)

- The v9 workflow above is agreed: verse maps once per verse, an Opus writer that matches page commitments to them,
  a separate meal step, a fixed test page (T0).
- **Verse map model: Sol high.** Chosen after the Luna max test (Luna failed) and the Opus high comparison on 12:49
  (equivalent for this step, 5.7× the cost). Opus 5.5 high stays the writer.
- **Codex usage counts toward the budget** (API-equivalent cost is real cost from now on).
- **Sources outside tier 1, 103:1 page (2026-10-08):** quotation packet tier 1 (69 chunks, 671 segments, 5,236
  notes, $3.53 Luna) and map updates for 35 verses (2,327 new notes → 323 additions, 46 new positions, 161 new
  questions; all checks OK; $5.13 Sol). Bint al-Shāṭiʾ's *al-Iʿjāz* now sits in 103:1/q02/p1. Meals: meal step;
  lexica: not used; surah-level segments: surah pages.
- **Volume is not a concern (2026-10-09):** blocks render as expand/collapse elements, so the reader shows or hides
  any detail; completeness wins over brevity. Ids never appear in reader text; uncited page verses a paragraph
  discusses get ledger lines like cited pairs.
- **When the tradition agrees with the page** (a consensus the page simply follows): a short block naming the
  classical witnesses (2026-10-08).
- **Sūra-wide questions** (place, count and order of revelation, reports on reciting the sūra): both on the ayah
  page's closing group and on the surah page (2026-10-08).
- **Sources outside tier 1 must be accounted for** on every page (meal, hadith, poetry, wujūh, translations, works
  without a verse index, surah-level segments): C1 lists each with its route; none is dropped silently (2026-10-08).
- Maps for the whole 103:1 page approved as the test run (`work/map-103_1-20261008`, 36 verses, ≈ $11–14).
  **Done 2026-10-08:** 36/36 completed and checked, $11.34 Sol (API-equivalent, counted), 809 questions, 1,938
  positions; with 12:49 and 6:52 from `maptest-20261008` every verse of the 103:1 page has a map. On 103:1 itself
  "what does al-ʿaṣr designate?" is now one question with 12 positions (the demo's Q1).

## What enrichment is for

The r13 ayah page is frozen Turkish prose built from the project dictionary and Qur'anic intertexts; the exegetical
tradition is absent from it. Enrichment places short blocks under its paragraphs. From a block alone the reader knows
which question the sources answer, every position and who holds it, and what decides between them; details are one
link away (block → verse map → views → notes → source passage). The page is never graded, confirmed or corrected.
Required: no silent loss, Biqāʿī and the bayānī school on every page (cited or a recorded reason), the meal review,
under $5 per ayah in production.

## Why v4–v8 circled

1. **No artifact held the questions.** A block answers a question; tier 2 stopped at positions (views), and the
   page's commitments were never written down. Every version redid the join between page and corpus at write time
   (Luna gatherer, three sift passes, root filter, menus).
2. **Per-verse work was done per page.** Gathering and sifting consolidated material for one page and could not be
   reused.
3. **The cited-verse scope changed** (focus only, then every cited verse, then option B). Option B is decided: a
   cited-verse block maps only what the paragraph takes from that verse, links to that verse's map.
4. **No fixed test.** Each version was judged on a different page with a different measure.

## The workflow

Two independent sides. The verse side runs once per verse and is reused by every page; the page side runs once per
page.

| # | Step | Unit | Who | Output | Status 2026-10-08 |
|---|---|---|---|---|---|
| C1 | Material | verse | script | manifest: every source with its disposition | verse-tied done; quotation packet only 103:1 |
| C2 | Notes (tier 1) | segment | Luna max | rows with words, type, anchor | S1/S87–114 own ayat; 212 S1 cited verses |
| C3+C4 | Verse map (tier 2 with questions) | verse | Sol high or Luna max (test decides) | questions → positions → notes | views only: 103:1 page (36 + 78:14, 18:19) |
| C5 | Meal table | verse | script | distinct renderings → translators | mostly exists |
| P1 | Page prep | page | script | numbered page, cited verses per ¶, readiness, question index | partly (v8 inputs) |
| P2 | Writer | page | Opus 5.5 high, one agent | plan, blocks, ledger | to build |
| P3 | Meal block | ayah | one agent | one block on the translations | to design |
| P4 | Render | page | script | page with linked blocks; strip check | `v7/write.py` render, needs map links |
| T0 | Test standard | test page | user + orchestrator, once | expected commitments and positions | seeded by `demo-103_1.md` |

### C1 Material (script)
Per verse: verse-tied segments (full-edition rule), range-tied segments, and the quotation packet (works without a
verse index that quote the verse's words: modern bayānī works, ulūm, wujūh, poetry, hadith matn). Surah-level
segments are listed for the surah page, never dropped without a line. The manifest marks each required voice as
present or "no text on this verse".

### C2 Notes (tier 1, unchanged)
`v7/digest.py`, Luna max, 20k-character chunks. Checks: every segment answered; anchors verbatim.

### C3+C4 Verse map (tier 2 with questions)
One call per verse turns its notes into questions, each with positions:
```
{"q":"q03","question":"one English line","words":["<verse words>"],"type":"<type>",
 "positions":[{"position":"…","rows":["<note id>",…],"reasons":"…","prefers":[…],"rejects":[…]}],
 "turns_on":"what the disagreement turns on","agreed":false}
```
- A question is something a reader could ask about the verse; tags (word × type) are filing labels, not questions
  (on 103:1 one question, "what is al-ʿaṣr?", spans three tags and 20+ views).
- Positions keep their reasons and arguments (the 2026-10-07 Luna failure buried arguments inside a broad view).
- Weight is independent holders, not compilers copying each other.
- No knowledge added; no note dropped. Check: every note sits under at least one position.
- The map is the writer's material, the link target of cited-verse blocks, and most of the verse's own page later.
- **Model test first** (6 agents, ≈$1.2 API-equivalent): Luna max vs Sol high, same brief, on 100:1 (the 26 notes
  Luna buried on 2026-10-07 are the known trap), 12:49 and 6:52. Judge: distinct positions and reasons kept,
  attribution, sensible question boundaries. Luna passes → it builds every map (about 6× cheaper) and the 103:1
  page's verses are redone with it. Luna fails → Sol; the existing 103:1 views get the question layer on top.

### Model test result (2026-10-08, run `work/maptest-20261008`)

| Verse (notes) | Luna max | Sol high |
|---|---|---|
| 100:1 (358) | 11 questions, 27 positions, $0.055 | 17 questions, 49 positions, $0.52 |
| 12:49 (235) | 12 / 32, $0.061 | 19 / 43, $0.31 |
| 6:52 (529) | 33 / 42, $0.052 | 23 / 63, $0.69 |

All six passed the check. **Sol high is chosen.** Luna failed on three counts:
- **Arguments lose their holders:** on 100:1 the horse arguments survive only as a generic list; Sol keeps al-Ṭabarī
  (camels do not pant), al-Rāzī (iron shoes spark, dawn raids) and Abū Ṣāliḥ preferring ʿAlī's authority.
- **`against` misused:** Luna lists notes that merely hold the rival position (including authors who wrote before
  the view existed) and misplaces al-Ṭabarī's rejection of the milking report under the pressing position. Sol's
  `against` entries are explicit rejections (including ʿAlī's correction of the active reading, which Luna missed).
- **Structure breaks on the largest verse:** on 6:52 Luna wrote seven duplicate questions (q27–q33 repeat
  q01–q18) for leftover notes instead of placing them.

**Opus 5.5 high on 12:49, same brief (2026-10-08):** 16 questions, 45 positions, $1.76 (Sol $0.31, 5.7×). Same
questions and positions as Sol, essentially one for one (yaʿṣirūn: the same nine senses; the same readings,
referents and rhetoric points). Opus is slightly richer: longer chains of who reports whom in `reasons`, three
further justified `against` marks (al-Rāzī, the Kashshāf, al-Manār arguing the detailed forecast cannot come from the
dream), and one extra catch (al-Ṣādiq's reading set against the relief sense). One Opus slip: al-Balkhī's challenge
filed as `against` its own position with no holder. No Sol error found on 12:49. **Sol high stays the map model**:
quality equivalent for this step at about a sixth of the cost; Opus judgement is spent in the writer.

Sol's map costs about 1.4–1.8× its flat tier 2 on the same verses (more output): ≈ $0.35–0.7 per verse. Revised verse
side ≈ $0.16 + ≈ $0.45 ≈ **$0.6 per verse**, whole Qur'an ≈ $3.8k API-equivalent ($0 cash on Codex).

### C5 Meal table (script)
Distinct renderings per verse with their translators, panel first, lineages grouped.

### P1 Page prep (script)
Numbers the paragraphs, lists cited verses per paragraph, refuses (and names what is missing) when a cited verse has
no map, builds the question index: one line per question of every cited verse.

### P2 Writer (Opus 5.5 high, one run; the agent decides what to look up)
- Preloaded: the page; the focus ayah's full map; the question index.
- Tools: a question in full, a view, notes by id, a free-text search over notes (when no question fits).
- Phases: **plan** (per paragraph: what it is built around; each commitment it makes about a verse, in the page's
  own words; matched question id or a status) → **pull** → **write**.
- Blocks: focus ayah ≤ about 150 words, after the first paragraph that raises the question; cited verse ≤ about 60
  words, only what the paragraph takes from it, plus a link to the verse map; a closing group for focus-ayah
  questions no paragraph raises.
- Ledger, one line per (paragraph, cited verse): `written` / `same_as` / `tradition_silent` (what was searched) /
  `page_own` (the page's own dictionary sense or association) / `retelling` (link only).
- Checks: ledger covers every pair; cited ids exist; quoted Arabic is in cited anchors; every focus question is in a
  block or the closing group.
- The writer gets no dictionary lookup; dictionary-sense claims are `page_own`.

### P3 Meal block
Input: the meal table and the paragraph that glosses the verse words. One block: best literal and best explanatory
rendering per word, losses the meals share, by loss type. Kept out of P2 so the writer's context stays clean.

### P4 Render (script)
Blocks after their paragraphs; links block → verse map page → views → notes → locator; removing the blocks gives
the frozen page back byte for byte.

### T0 Test standard
For 103:1 (the only page with full coverage of its cited verses): per paragraph the commitments and expected
positions, from `demo-103_1.md`, confirmed by the user. Score: commitments matched, positions present,
misattributions, cost. Every design change is scored on the same page. Test only, not a production check.

## Languages (recommendation, 2026-10-08)

One pivot language, English, for the whole verse side (notes, views, maps), with Arabic kept in `words`, anchors
and speakers. Per target language only: the writer's blocks, the meal step (its own translation panel), a display
table for names and terms built by script from source ids, and the rendered verse-map pages. Writers take key terms
from the Arabic, never by translating the English claim. A German page that translates the Turkish base with the
same paragraph numbers can take translated blocks; a page written independently runs its own writer on the same
English maps.

## Cost (API-equivalent at published rates; Codex runs cost $0 cash)

Measured:
- Tier 1, Luna max: $34.59 for 212 verses (S1 cited verses, 101k rows) = **$0.16 per verse**.
- Tier 2, Sol high, whole verse: $8.88 for 36 verses (103:1 page, about 8.6k rows) = **$0.25 per verse** (range
  $0.08–0.48, scales with rows).

Estimated:

| Item | Per unit | Notes |
|---|---|---|
| Verse side, Sol map | ≈ $0.6 per verse (measured on 3 verses) | tier 1 + map; once per verse; whole Qur'an ≈ $3.8k API-equivalent |
| Writer, Opus high | ≈ $3–5 per page | start context ≈ 50k tokens, ≈ 25 lookups, 30–40 turns; heavy pages (1:1) ≈ $5–7 |
| Meal block | ≈ $0.3–0.6 per ayah | small input |
| **Cash per ayah (Claude)** | **≈ $3.5–5.5** | the <$5 target holds at the low end; measured on 103:1 first |

For comparison: v2 1:1 one Opus agent ≈ $12.5–14; the v8 sift writer estimate $13–17.

103:1 test from here: question layer or map test ≈ $1.2–4 (Codex), writer ≈ $3–5 and meal ≈ $0.5 (Claude cash).

## Next (each spawn needs the user's go)

1. Verse-map brief (generic, no ayah examples) and `map.py` build/check; show the brief to the user.
2. Model test on 100:1, 12:49, 6:52.
3. Maps for the 103:1 page's 38 verses.
4. T0 written from the demo with the user.
5. P1, writer brief and query tool; one writer run on 103:1, scored against T0; then the meal block.

## Open

- When the tradition simply agrees with the page (e.g. a consensus gloss): a one-line block naming the classical
  witnesses, or no block.
- English pivot: recommended, not yet confirmed by the user.

## Review of the 103:1 test (2026-10-09): is every step worth it?

| Step | Cost (103:1 page) | What reached the final page | Verdict |
|---|---|---|---|
| Tier 1, verse-tied (Luna max) | ≈ $6 (38 verses × ≈ $0.16, earlier runs) | 396 of the 427 notes the blocks cite; 50 sources named; Biqāʿī 30 notes, Bint al-Shāṭiʾ's tafsīr 15 | essential |
| Quotation packet tier 1 + map updates | $3.53 + $5.13 | 15 of 44 blocks; 31 notes: Itqān 15, Bint al-Shāṭiʾ's *al-Iʿjāz* 13 (the antecedent of the page's thesis), Burhān 4, Nashr 4 | worth it; in-run from now on (≈ $0.09 per verse, no separate update) |
| Verse maps (Sol high) | $11.34 (+ $1.83 tests) | every block cites map questions; 2,076 notes stand behind the cited positions while the writer read 427 | essential; reused by every page |
| Writer (Opus high) | $4.03 + $3.27 final pass by resume | 44 blocks, 70 ledger lines, all 22 paragraphs | worth it; the resume was waste (cache expired, 417k-token context re-read); the final pass is now in-run |
| Meal (Opus high) | $0.42 + $0.38 for two fix resumes | 2 blocks: renderings against the tradition's positions, Turkish drift ("asır" read as century), collapsed ranges, relay source, the root's squeeze sense in only three meals | worth it; dictionary profiles yielded nothing on this verse but cost ≈ 5k characters |

Open after the review: 103:3 has no map (the page discusses its exception; the writer's lines were rejected); the
short editions now kept (33 new notes on 103:1 alone) and 37 excerpt-only segments need tier 1 and map updates;
the augment9 decision; writer start context (index of 37 cited verses preloaded, 112k characters) is the main cost
driver to test next.

