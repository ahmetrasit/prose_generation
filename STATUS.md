# Status

Per-surah production state. Updated by hand; last checked 2026-07-27.

Upstream evidence coverage is a different question — see
[`docs/DATA_AVAILABILITY.md`](docs/DATA_AVAILABILITY.md). What to do next, as
numbered actions, is [`PLAN.md`](PLAN.md).

---

## Summary

| | S1 | S103 | everything else |
| --- | --- | --- | --- |
| branch anchors (language-neutral) | seeded | seeded | — |
| layer 1 — spine, `tr` | 3 test artifacts, none accepted | drafted | — |
| layer 1 — spine, `en` | drafted | — | — |
| layer 2 — ayah commentary | not started | not started | not started |
| layer 3 — surah commentary | not started | not started | not started |
| commentary bundles buildable | **yes** | yes | yes, 114/114 |
| channel review available | yes (13 parents / 44 subchannels) | yes (12 / 31) | 110 / 114 |

**Nothing has yet been written under the current `COMMENTARY_SPEC.md`.** The
spec was derived from rejected S103 attempts, not from a passing one. Layers 2
and 3 are specified and unexercised.

**S1 is the layer-2/3 pilot, not S103.** S1 has complete branch inventories, both
reader walks, a whole-surah reading, 7/7 inter-ayah outputs, full Turkish gloss
coverage with error profiles, and the richest channel review in the corpus —
including both reference channels. S103's only advantage is the one focus run
with staged reader responses.

---

## S1 — al-Fātiḥa

The furthest-developed surah, and the reference case for the path and water
channels ([`docs/CHANNELS.md`](docs/CHANNELS.md)).

**Layer 1.** `source/s001.primary-anchors.json` holds the language-neutral
branch selection. English has `output/en/s001.json`. Turkish has three test
artifacts — `s001.cold-test.json`, `s001.v2-cold-test.json`,
`s001.v3-gloss-test.json` — and **no accepted `output/tr/s001.json`**. The v3
artifact was generated from the reviewed gloss results by an isolated cold
agent.

**Layers 2–3.** Not started, but the bundle now builds:

```
branch_inventories : 18 roots, surah-scope fallback (no focus run exists)
butuncul_okuma     : present for every ayah
reader walks       : reader_a + reader_b
channel review     : 13 parent channels, 44 subchannels
inter-ayah 1:6     : 143 rows (48 strong / 65 medium / 9 weak / 21 no value)
v12 responses      : none — S1 has no focus run
```

**Upstream evidence.** Complete: 7 ayahs, 29 QAC words, 48 morphemes, 33
word-analysis records with an explicit v2 crosswalk, 7 V12 publication rows (21
strong / 13 weak / 2 reject findings), 18 activated root anchors with full
Turkish dictionary and reviewed English gloss coverage, 7/7 inter-ayah outputs
totalling 1,096 reviewed rows (267 strong / 521 medium / 220 weak / 88 no
value), 94 grammar rows and 18 roots with 151 branch records in the app evidence
pack.

**Basmalah handling.** Reader `1:1` maps to V12 publication `1:0`. This stays an
explicit boundary mapping and is never repaired by hidden renumbering.

**Application pilot.** A working web and iOS contract demo consumes S1 with a
shared reader contract, explicit QAC-to-analysis and QAC-to-Furuq crosswalks,
Turkish target-token-to-morpheme mappings, and a pinned source lock. It remains
a demo: the catalog is unsigned, the multilingual-pack contract is not frozen,
English has no accepted fluent translation, and audio publication is incomplete.

---

## S103 — al-ʿAṣr

The shortest vertical slice, and the surah the commentary spec was developed
against.

**Layer 1.** `source/s103.primary-anchors.json` seeded; `output/tr/s103.json`
drafted. No English.

**Layers 2–3.** Bundles built (`bundles/s103/`: three ayah bundles plus the
surah bundle). No commentary written.

**Bundle contents, verified.**

```
103:1 -> 152 inter-ayah rows (28 strong / 51 medium / 60 weak / 13 no value)
103:2 -> 114 inter-ayah rows (31 strong / 39 medium / 28 weak / 16 no value)
103:3 -> 202 inter-ayah rows (58 strong / 93 medium / 40 weak / 11 no value)
word analysis:  3 ayah records, 18 words[] entries (2 + 4 + 12)
v12 responses:  9 files for focus_103_1 (readers d/e/f x stages 00/01/02)
                0 for focus_103_2 and focus_103_3
branch inventory (ع ص ر, focus_103_1 stage_00): B001-B015
```

**Known-missing, expected.** `focus_103_2` and `focus_103_3` have packets and
manifests but zero reader responses. Reader B's walk has no Turkish Prose
Synthesis section. Both are recorded in bundle coverage, not silently empty.

**Finding carried forward.** The eight `ع ص ر` branches collapse to *retention
under compression*, which makes `خسر` legible as leakage and the closing `صبر`
structurally necessary. See `PRINCIPLES.md` §8.

---

## Follow-on candidates

**S100** is the priority. It is the case that makes layer 3 non-optional: the
running horses of the opening oath are unattached under the primary reading and
only the channel attaches them. Prior prose-planning and channel work exists.

**S96** offers a larger, more varied curriculum and lexical test, and is the
natural place to exercise the `iqra'` error-profile problem directly.

Both have useful V12, word-analysis, and network coverage, and substantially
less dictionary-gloss and inter-ayah coverage than S1.

---

## First output ever produced

`bundles/s001/1_6.layer2-baseline.{prose,evidence,friction}.md`, 2026-07-27 —
layer 2 on 1:6, written by a cold agent after the bug-1/bug-2 fixes, State B.
1,516 words of Turkish for a three-word ayah, plus a 16-item friction report.

Quality is high; size and shape are wrong, and the run is contaminated for
evaluation purposes because the governing docs contain worked answers for 1:6.
**S100 is the evaluation surah.** Full analysis in [`PLAN.md`](PLAN.md).

---

## Cross-cutting gaps

- No **adjudicated channel ledger**. Discovery is complete and reviewed once;
  what is missing is a second reader, accept/reject, per-ayah maturity, and a
  machine-readable form. Layer 3 is gated on that, not on discovery.
- **Maturity is computed nowhere.** It is the interface between layers 2 and 3
  and no artifact carries it.
- **`mNN` motif identity does not join** to anything downstream.
- The **staged before/after** exists for five ayahs corpus-wide. Layer 2's
  prompt still treats it as a normal section.
- No source artifact evidences the surah **argument**; those claims stay
  inference.
- The **assemble-step inversion** for layer 1 landed 2026-07-27
  (`_translation/v1/tools/assemble.py`), so the writer no longer transcribes
  identities and long surahs are viable. Layer 1's stage 0 — branch selection —
  is now a tool plus a prompt plus a check rather than hand authoring.
- `consideredNotPrimary` **exists but no seed carries it yet.** Both live seeds
  are `primary-anchor-seed-v1` and fail `check_anchors.py`; re-seeding recovers
  up to 83 rejections for S1 and 62 for S103. Until they are re-run, layer 1
  still destroys the rejections layers 2 and 3 depend on.
- **Layer 1's new stages have never been run by an agent.** Every tool, prompt,
  schema, and check is in place and exercised mechanically; no cold agent has
  authored either an anchor seed or an authored translation file under them.
- German has no dictionary gloss results, so a German layer-1 run has no
  controlled lexical evidence.
- Whole-surah readings exist for 30 of 114 surahs.
