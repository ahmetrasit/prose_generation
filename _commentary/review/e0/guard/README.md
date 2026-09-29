# Construction guard (E0)

A script that asks, for every Quranic occurrence of a root and every collocation-bound or non_bare branch of that
root: does the construction the dictionary names for this branch stand in the text here? It writes a verification
record for the user. **Nothing here is ever a model input**: no call, level or reason may be copied into a brief,
supply or prompt (the user's rule: scripts annotate and record; presence verdicts go only to the user).

## Files

| file | what it is |
|---|---|
| `detector.py` | the detector (construction parsing, grammar context, matching, calls) |
| `gdata.py` | loaders; decompresses the two quran-data databases into `./cache` (not committed) |
| `run_all.py` | runs the detector over every occurrence; writes `guard_calls.tsv`, `eval_by_branch.tsv`, `run_all_summary.json` |
| `guard_calls.tsv` | the verification record: one row per occurrence × guarded branch (call, level, reason, matched statement) |
| `eval_dossier.py` | compares calls with root-dossier's placements (the evaluation labels; the detector never reads them) |
| `build_audit.py` | writes `audit_sheet.md` (for the user to fill in) and `audit_key.tsv` (the hidden calls) |
| `*_v1_frozen.*` | the first version, kept for comparison |

## Version 2 (after the E0 review, `../review/fixes.md` M1, M2)

**M1: fewer wrong "present" calls.** In v1, 41% of the present calls came from a lexeme rule that matched
unvocalised homographs. Examples:

- ء ح د B006, Mount Uḥud, on أحدا;
- ش ي ء B007, an exclamation, on every شيء;
- ك ت م B005, the katam plant, on نكتم;
- ص ب ر B016, a clan, on صبروا.

A lexeme match now also needs:

- **The same word class.** The class is read from the branch's own image, definition and Turkish gloss.
  - A proper name (mountain, place, tribe, idol, river) needs a QAC proper noun.
  - A particle needs a particle.
  - An adverb (ظرف) needs a particle or a noun, since QAC tags مِنْ عِندِ as a noun.
  - A plant, animal or object name is "unknown": a noun tag cannot tell it from a common noun.
  - A unit written with the article is never a verb.
- **No vowel clash.** Where the dictionary vocalises the unit (جَنَد, المُدّ), its vowels must not differ from the
  QAC lemma's.
- **No shared lexeme.** When another branch of the same root names the same lexeme in its own text, the call is
  "unknown", because the lexeme alone cannot choose between them.

Partner and preposition matches changed in two ways:

- **Head class.** A match fails when the statement's head is a noun and the occurrence a verb (غروب العين "tear
  ducts" against تغرب في عين), or the reverse (نوّر على فلان against نار).
- **Next preposition.** The preposition after the word is read as governed by it only when the word has no grammar
  data. At 2:245, وإليه ترجعون belongs to the next verb, not to يبسط.

**Effect** (`run_all_summary.json`, `eval_dossier.json`):

| | v1 | v2 |
|---|---|---|
| present calls in the whole record | 2,553 | 1,597 |
| lexeme present calls | 1,042 | 218 (197 of them عند) |
| main set: placements found | 72.3% | 70.9% |
| main set: present precision at dossier placements | ≤ 64% (263 vs 146) | 70.1% (258 vs 110) |
| test half: present precision at dossier placements | — | 98.4% (124 vs 2) |

- **Hand check.** I read every remaining lexeme present call outside ع ن د (21), and all are right:
  - Hūd (7);
  - ينبغي (5);
  - أرنا (3);
  - أخلصناهم;
  - المزمل;
  - تسنيم;
  - ساهم;
  - the idols Suwāʿ and Nasr.
- **Caveat.** The rules were changed after looking at the evaluation sets and at the reviewer's samples, so these
  figures are optimistic. The clean estimate is the audit sheet's Part C. Until it is filled in, treat the
  "present" calls in `guard_calls.tsv` as unverified.

**M2: the audit sheet.**

- **Calls hidden.** The script's calls are no longer shown next to your answer column; they are in `audit_key.tsv`.
- **Positive questions.** Every question asks yes or no directly (✓ = yes).
- **Part B examples.** A branch is shown with an example only when root-dossier places it somewhere. Random
  occurrences of the root, usually of another branch, are gone.
- **Part C (new, 40 rows).** 30 seeded "present" calls away from dossier placements (10 lexeme or formula calls)
  mixed with 10 seeded "absent" calls, shuffled. Every row shows the same branch statements whatever the script
  matched. This part measures precision, which v1 could not.
- **Source tags.** Tags such as `(ayn;tahdhib)` are no longer cut.
