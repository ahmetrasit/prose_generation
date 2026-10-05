# S1 first-image discovery, revision 2

Prompt/code committed and pushed before the rerun: `977931b54`.
Only image section 1 was rerun, with fresh native Luna and Terra 5.6 agents at maximum effort, each followed up once in its own session. No Opus call was made. Original outputs remain under `discovery/sec1/`; this attempt is under `discovery/revision2/sec1/`.

## Results

| Model | Original initial + follow-up | Revised initial + follow-up | Revised total |
|---|---:|---:|---:|
| Luna | 262 + 192 | 59 + 13 | 72 |
| Terra 5.6 | 332 + 199 | 148 + 21 | 169 |

Merged candidates: **745 → 176 (76.4% fewer)**. The agents agree on 65 references. Follow-ups add 20 distinct references to the initial union of 156. The revised union retains 166 original candidates and adds 10 previously absent candidates. Merged labels: 95 strong, 75 medium, 2 weak, 4 contrast. Labels still use the best label either model supplied; they are not validated confidence scores.

Both models retain all 16 outside-S1 citations already supplied in the image prose. All rows have four fields, valid outside-S1 references, and no duplicate refs. Each final list preserves its first-turn file as an exact prefix. Session records confirm the requested model and effort for both turns. Tool review found no reads, retrieval or discovery scripts in either follow-up.

The dry augment build contains 223 passages (176 candidates + 47 contextual neighbours), about 50,598 input tokens, estimated $2.58. The original dry build was 775 passages, about 150,510 input tokens, estimated $7.82. These are estimates only; no Opus cost was incurred. Discovery estimate and actual charge are both $0 on the Codex subscription. Token usage is recorded in each run log and the ledger (Luna 370,049 total; Terra 481,464 total, including cached input).

## Assessment

The revised instructions substantially narrow the candidate pool and retain concrete links such as guide/follower relations, landmarks, traversable ground, opposed destinations, and Satan's footsteps. The prior forced or poorly supported entries at 103:1, 99:7, 77:25, and 107:1 are absent. The earlier wrong reference 79:18 has been replaced by the correct guidance verse 79:19. The 20:53 note now stays with actual paths in the verse.

Coverage remains incomplete: useful earlier candidates such as 25:34 (being gathered toward Hell and further astray from the way), 4:125 (following Abraham's religion), and 18:2 (uprightness paired with 18:1) are absent. Smaller output is not proof of better recall. The prompt now explicitly uses 2:108 and the rejected 103:1 explanation as examples, so those are not independent evaluation cases. `audit_sample_comparison.json` records retention for the original purposive sample; it is not a statistical error-rate measurement.

Both calls have status `ok` and check `findings`. The raw lists and merge remain as the agents wrote them. The following are validation findings, not silent corrections:

| Model | Reference | Finding |
|---|---|---|
| Luna | 26:63 | Quotes the dry-path wording from 20:77. The cited verse describes striking and splitting the sea. |
| Luna | 42:15 | Quotes فاستقم where this verse has واستقم; the former wording is at 11:112. |
| Terra | 19:43 | Changes the quoted noun phrase from accusative صراطًا سويًا to genitive صراطٍ سويٍ. |
| Terra | 23:74 | Reorders the quoted phrase; the verse has عن الصراط لناكبون. |
| Terra | 33:67 | Quotes عن السبيل, while the verse has فأضلونا السبيلا. |
| Terra | 4:51 | Compresses nonconsecutive words as أهدى سبيلا without marking the omission. |
| Terra | 18:1 | Attributes قيما to 18:1; it belongs to 18:2. |
| Terra | 40:28 | English summary misattributes Pharaoh's fear from 40:26 to the believing man, and changes the feared action. |

The wording checker initially overflagged ordinary versus Uthmani orthography. Its normalization was corrected and tested against the 79:18/79:19 and 26:63/20:77 errors plus matching Uthmani/ordinary forms. Remaining automated flags (Luna 13, Terra 18) were adjudicated in each `validation_review.json`: many are legitimate root/source-section forms or orthographic differences. The checker cannot validate English explanations or exhaustively judge relevance. The table above is an identified set of issues, not a claim that all other notes are error-free.

## Execution findings

- Both agents attempted to read their own TSV before it existed, producing a missing-file diagnostic, then successfully created it.
- Luna's first-turn sorting script raised a KeyError from an escaped-tab delimiter and was corrected in its next tool call. The saved first and final TSVs pass validation.
- Terra's completion message claimed 22 additions; the actual file has 21. All counts above use the file.
- The source commentary SHA-256 remains `782be8c16d10f4684dc7f79db8acefd312f3ca466c57cffa1c3ce02d6429dea7`; both input packages are identical to their original counterparts.
- Existing S1 status findings are unchanged: 1:2 reading has one source finding; 1:4 has one process line; 1:6 has two process lines. The existing $107.03 surah total is not the cost of this discovery rerun.

The workflow stops here, before Opus. This test supports the narrower inclusion rule while showing remaining recall and factual-accuracy limits.
