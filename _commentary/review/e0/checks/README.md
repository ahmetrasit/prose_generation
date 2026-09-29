# E0 checks: check.py, lint.py, scorecard.py

Built 2026-09-28 in E0, the free build step after the review (`../../PHASE2_REPORT.md` §3 S3 and §8 E0). Scripts only:
nothing here calls a model, and nothing here writes outside this directory.

**Nothing these scripts produce is ever a model input.** The check records, lint reports, scorecards and the two
`*.eval.json` files go to the user and to the verification record only. They hold construction framings, probe
answers and contamination lists that no brief, prompt or supply may carry.

## Files

| file | what it is |
|---|---|
| `check.py` | verification record for one finished commentary (JSON) |
| `lint.py` | contamination lint for briefs, prompts and supply files |
| `scorecard.py` | frozen mechanical diagnostics per commentary, set by set |
| `common.py` | shared loaders, Arabic folding, corpus search, cached index |
| `lint_terms.eval.json` | EVALUATION ONLY: the contamination list (named cases, answer phrases, verdict and cap patterns) |
| `probes.eval.json` | EVALUATION ONLY: watch probes per named case (diagnostics, decision 8) |
| `selftest.py` | 37 positive and negative controls; run it after any change |
| `smoke_check.sh`, `smoke_manifest.json` | the smoke tests, rerunnable |
| `FROZEN.sha256` | hashes of the frozen tool files (see the last section) |
| `cache/` | derived index, rebuilt automatically when a source changes (`cache/signature.json`) |
| `smoke/` | smoke-test outputs (check records, lint reports, scorecard) |

## Sources read (read-only, raw)

- the Quran text: `quran-data/data/text/quran-uthmani.tsv`;
- the dictionary: `quran-data/data/dictionary/tr/root_*_entry.json`. The scripts read branches, `branch_kind`, the
  scope note, image, what_is, and `source_phrase_ar` with its source tags. They also read the occurrence evidence:
  which root each Quran word carries;
- the six early sources in full: `dictionary/data/output/root_packets/root_*.json`, fields `entry_text_clean` and
  `lexical_senses`;
- Majāz al-Qurʾān, direct text only: `quran-roots/_corpus/lexicons/cache/openiti_context.sqlite`, table
  `quran_specialized_entries`, source `majaz_quran`;
- variant readings: `study/_project_corpus/qiraat.tsv`;
- the `[plain]` branch per word: `root-dossier/out/activation_map.tsv`, role `dominant`;
- root letters for 15 root ids that have no packet: `quran-slm/resources/source/furuq_full_branches_ar.tsv`.

Late compilations (Lisān, Lane, al-Qāmūs) are never read. The first run builds `cache/index.pkl.gz` in about 20
seconds. After that, one check takes about 5 seconds.

## check.py

```
python3 check.py <commentary.md> --ref S:A [--out record.json] [--quiet]
```

It never edits the commentary. The record contains the following.

1. **Every tagged quotation, resolved to a source.** Tags are `{ar:…, tr:…, gloss:…}` or `{{ar:…}}`. The possible
   sources:
   - `quran`, with the ayah or ayat;
   - `dictionary`: a branch text, with branch_ref, root, field, source tag and branch_kind;
   - `qiraat`;
   - `early_entry`: one of the six sources, with the root;
   - `majaz`: the entry id and heading;
   - `unsourced`.

   Two classes are not quotations and are kept out of the sourced share: `root_name` (a root written as spaced
   letters, «ق و م») and `too_short` (one letter or particle).

   Matching folds diacritics and Uthmani spelling. The strongest match wins, in this order:
   - `exact` or `clitic` (a proclitic or a pronoun suffix differs);
   - `article` (al- added or dropped);
   - `pieces` (split at ؛ or ۝, each piece resolved);
   - `gapped` (every word present, in order, with at most 4 words silently left out);
   - `loose` (consonant skeleton; Quran only, and only within the focus surah).

   At equal strength, place decides:
   1. the Quran near the focus (the ayah, its ±7 window, its surah);
   2. a dictionary branch of a focus or window root;
   3. a variant reading at the focus;
   4. the Quran elsewhere;
   5. any other branch;
   6. an early entry;
   7. Majāz.

   A multi-word quotation that is Quran text anywhere goes to the Quran. `also` lists every other source type the
   quotation matches.
2. **Arabic outside tags.** Each case is flagged with its context (quotation marks, italics, backticks, parentheses,
   bare) and resolved the same way.
3. **`[bellek]` marks.** For each mark: the sentence, its checkable items and whether each item is attested in the
   project sources. A sentence with no Arabic item is labelled "not checkable by script". Unsourced quotations that
   carry no mark are listed.
4. **Cited branches.** A cited branch is a quotation resolved to a branch of a focus or window root. For each one the
   record gives:
   - `branch_kind` and the scope note;
   - `bound` (true for `collocation` and `non_bare`);
   - the framing:
     - `echo marker in the sentence` or `in a neighbouring sentence`: the core markers are yankı, kalıp, söz öbeği
       and ifadede;
     - `no echo marker`: the prose may state it as the word's sense, or cite it as a lexical unit. The user reads the
       sentence.
   - extended markers (deyim, tabir, kuruluş, …), reported separately.

   This is for the record only. The script never decides whether the construction is present: detectors miss 44–79%
   of real constructions.
5. **Negation rate** per 1,000 words, with the E2 regex copied unchanged from `experiments/e2_score.py`, plus a
   breakdown and "not only" frames.

## lint.py

```
python3 lint.py <file>... [--kind auto|brief|supply] [--json out.json] [--strict] [--quiet]
```

**Categories:**

| category | what it catches |
|---|---|
| `known` | the example `(15:26, 15:28, 15:33)` |
| `named-ref` | refs of the named cases and of their answer passages; case names (Fatiha, S100, S103, …) |
| `answer` | North Star "aha" and example phrases and watch-case answers, in English and Turkish, plus five Arabic ones |
| `scene` | v15 scene ids, multi-word inventory roles and scene vocabulary. Roles are read live from `v15/data/frames_inventory.json`. |
| `role-term` | single-word roles that coincide with answers (stray, follower, …); `frame` and `beam` only next to a well word |
| `verdict` | no value, strong/moderate/weak labels, DEPARTS, withheld, present: no, [N readings], script echo-tier labels, confidence/grade fields, dominant-role ratios |
| `cap` | numeric caps, including template caps such as `up to {kwic_max} times` |
| `cap-review` | counts stated as form rules ("in one sentence") and cap vocabulary, for you to judge |

**Kinds:**

- `brief`: every hit counts.
- `supply`: a hit on a data line (a dictionary branch line, a Quran text line or a mostly Arabic line) is labelled
  `data-line`. Refs in a supply are data and are reported as `info`. A dictionary gloss naming the lead animal is
  data. The same words in the supply's own framing text are contamination.

`--kind auto` treats a file as a supply when its name says supply, packet, sheet, pull, dossier or dictionary.

Every file's calibrated size is reported (4581 + 1.151 × Arabic chars + 0.366 × other chars). Sizes are reported,
never judged, and supplies are not trimmed.

## scorecard.py

```
python3 scorecard.py --ref S:A [LABEL=]FILE ... [--supply SUPPLY] [--pool FILE ...] [--json out.json]
python3 scorecard.py --manifest smoke_manifest.json --json smoke/scorecard.json
```

The principle is depth first; named items are probes. **There is no pass/fail anywhere.** Lengths are reported and
never judged.

For each commentary:

- **form:** words, paragraphs, the longest and the mean paragraph, headings, `[bellek]` marks, negation rate.
- **sourcing:** from check.py.
- **reach:** refs in the window (±7), elsewhere in the surah, and in other surahs.
- **pooled:** the file's share of the pool. The pool is every ref and Arabic quotation across all files scored
  together, plus `--pool` files.
- **supply** (with `--supply`):
  - the supply's calibrated size;
  - the non-plain branches used, for focus roots and for all roots;
  - the typed-link lines used;
  - **candidate new findings**: refs, quotations and branches used that appear in no pooled input, listed for the
    user.
- **probes:** watch probes from `probes.eval.json`. Each probe is a hit or a miss with a snippet. They are
  diagnostics and never a total.
- **frozen:** the tool hashes against `FROZEN.sha256`.

**Supply contract.** A supply can be JSON: `{"branches":[{"branch_ref":"root_000583/B004","plain":false}],
"links":[{"type":"definitional join","refs":["5:95"]}]}`. It can also be Markdown:

- A branch is written as `root_nnnnnn/Bnnn` or `ر ف ق B004`, or as a `Bnnn` line under a line or heading that names
  the root.
- A `[plain]` mark belongs to the nearest branch before it on the same line. If the supply has no marks, the
  root-dossier's plain set is used, and the output says so.
- A typed link is a line with refs, under a heading that names a join, bridge, concordance, echo, parallel, partner,
  formula, cross-reference, loaded word, contrast, uses or path.

"Used" is a lower bound. A branch counts as used when a quotation resolves to it; a paraphrase with no Arabic does
not count. A link counts as used when any ref on its line is cited.

## Smoke tests (rerunnable)

```
python3 selftest.py                          # 31 controls
./smoke_check.sh                             # check.py on 38 commentaries -> smoke/check/*.json, smoke/check_summary.txt
python3 scorecard.py --manifest smoke_manifest.json --json smoke/scorecard.json > smoke/scorecard.txt
python3 lint.py ../../experiments/prompts/*.md ../../../v15/prompts/*.md --json smoke/lint_prompts.json
```

The inputs:

- v15 `out-nocap` 4:34 and 5:6;
- E1 readings (12);
- E2 finals (6);
- the v9 cold arms (18, including cold2);
- in the scorecard, also the v9 dictionary arms, the 29:38 pilots, and the three Phase 2 sample supplies. The samples
  were used only to test parsing: they still carry presence verdicts and are not E0 supplies.

Lint positive controls: v9 `write_v10.md` and `write_v11.md` (the known example), and the Phase 2 samples read as
supplies.

## Frozen-hash note

The scorecard is frozen so that arms scored on different days are scored by the same instrument. The frozen set is
listed in `FROZEN.sha256` (sha256 of each file):

- `common.py`, `check.py`, `lint.py`, `scorecard.py`: the metrics;
- `lint_terms.eval.json`, `probes.eval.json`: the evaluation lists;
- `../textclean.py`: the edition-footnote and OpenITI-marker cleaning shared with the supply builder (since v2).

`scorecard.py` prints `frozen tools: match` or `CHANGED [files]` on every run and writes the same status into its
JSON.

The rules:

1. **Do not edit a frozen file to score an arm.** A change, even to a probe regex, is a new scorecard version. Rerun
   `python3 selftest.py`, then `python3 scorecard.py --freeze`, and rescore every arm that will be compared with the
   new version.
2. **The cache is not frozen.** It is derived from the raw sources. `cache/signature.json` records each source's file
   count, size and newest mtime, and every check record carries that signature (`index_signature`). A changed
   dictionary is visible in the record without being mistaken for a tool change.
3. **Probes are evaluation-only.** They are diagnostics under decision 8: a miss is not a failure, and no total or
   weight is built from them. Keep both `*.eval.json` files out of every model input (lint.py skips them). Never copy
   their contents into a brief.

## Versions

- **v1** (2026-09-28, E0): the first frozen set.
- **v2** (2026-09-28, after the E0 review, `review/fixes.md`). Nothing had been scored with v1 for a decision, so no
  arm needs rescoring.
  - Majāz: the index comes from the supply builder's `out/majaz_index.json`: sqlite entries cut at surah headers, plus
    the raw OpenITI entries of surahs 19–114, each with its mapped ayah. Quotes from surahs 19–114 no longer resolve
    to entry 1308 (18:108). Hits report `mapped_ref` (B3).
  - Early entries: Ṣiḥāḥ edition footnotes that quote late works are replaced by `[edition footnote omitted]`, and
    OpenITI markers are stripped, so a late quote is no longer certified as `early_entry` (m2, m3).
  - Scorecard: an explicit map of the E0 page.
    - Branches, the denominator, come from section B's branch lines only.
    - Links are the lines with refs in C, D, E and F.
    - `[plain: …]` is read as a plain mark.
    - Branches mentioned anywhere count as on the page (M7, m10).
  - Lint: a `relay` context for the chain section `## F.` of an E0 page, and pull-file JSON lines classed by key (m1).
  - Selftest: 37 controls (6 new).
