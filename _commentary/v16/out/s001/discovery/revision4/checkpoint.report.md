# S1 revision4 checkpoint

Raw outputs and failed logs preserved. No new follow-ups or merges until user decision; already-running calls left undisturbed.

| Image | Model | Completed turns | State | Check |
|---|---|---:|---|---|
| 4 | luna | 2 | ok | findings |
| 4 | terra | 2 | ok | findings |
| 5 | luna | 2 | ok | findings |
| 5 | terra | 2 | ok | ok |
| 6 | luna | 2 | ok | findings |
| 6 | terra | 2 | partial | findings |
| 7 | luna | 2 | partial | findings |
| 7 | terra | 1 | awaiting_followup | pending |
| 8 | luna | 2 | ok | findings |
| 8 | terra | 1 | awaiting_followup | pending |
| 9 | luna | 2 | ok | findings |
| 9 | terra | 0 | initial_turn_running | pending |
| 10 | luna | 1 | awaiting_followup | pending |
| 10 | terra | 0 | initial_turn_running | pending |
| 11 | luna | 1 | awaiting_followup | pending |
| 11 | terra | 0 | initial_turn_running | pending |
| 12 | luna | 2 | ok | findings |
| 12 | terra | 0 | initial_turn_running | pending |
| 13 | luna | 1 | awaiting_followup | pending |
| 13 | terra | 0 | initial_turn_running | pending |
| 14 | luna | 2 | ok | findings |
| 14 | terra | 0 | initial_turn_running | pending |

## Repairs awaiting decision

- Image6 Terra:90:40–42 do not exist; explanations match80:40–42. Proposed file fixes only those three reference fields.
- Image7 Luna: follow-up lines44–45 swap reference/basis fields. Proposed file fixes only those two swaps.
- Both repair.proposed.json files record exact before/after rows; followup.tsv and partial run.log.json remain untouched.

## Findings

Native logs contain all automatic Arabic flags and recovered tool diagnostics. validation_review.json files distinguish reviewed flags, confirmed errors and unreviewed items. Findings include boundary slips at4:5 (image4 Luna),71:10/71:12 (image5 Terra),43:14 (image7 Luna), and wording mistakes at29:58/9:109 (image6 Luna),22:37/51:6 (image14 Luna),17:72 (image12 Luna). Relevance and English meaning were sampled, not exhaustively validated.

Image4 merged:193 candidates,107 named by both. Remaining merges held. Images1–3 retain completed revision3 selections. No Opus calls. Incremental discovery charge recorded as$0 on Codex subscription; usage remains in native logs.
