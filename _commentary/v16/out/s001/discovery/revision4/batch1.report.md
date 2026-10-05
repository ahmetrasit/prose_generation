# S1 revision4 batch 1

| Image | Model | Initial | Proposals | New | Repeats | Final | Check |
|---|---|---:|---:|---:|---:|---:|---|
| 4 | luna | 101 | 40 | 40 | 0 | 141 | findings |
| 4 | terra | 134 | 25 | 25 | 0 | 159 | findings |
| 5 | luna | 157 | 52 | 52 | 0 | 209 | findings |
| 5 | terra | 197 | 19 | 19 | 0 | 216 | ok |
| 6 | luna | 114 | 42 | 42 | 0 | 156 | findings |
| 6 | terra | 165 | 40 | 37 | 3 | 202 | findings |
| 7 | luna | 135 | 46 | 46 | 0 | 181 | findings |

Image 4 luna: 4 Arabic review flags; see sec4/luna/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].

Image 4 terra: 3 Arabic review flags; see sec4/terra/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].

Image 5 luna: 12 Arabic review flags; see sec5/luna/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].
Recovered diagnostic: Script failed
Recovered diagnostic: Script error:
Recovered diagnostic: apply_patch verification failed: Failed to find expected lines in /Volumes/aro/projects/prose_generation/_commentary/v16/out/s001/discovery/revision4/sec5/luna/list.tsv:

Image 5 terra: 0 Arabic review flags; see sec5/terra/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].

Image 6 luna: 21 Arabic review flags; see sec6/luna/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].
Recovered diagnostic: Script failed
Recovered diagnostic: Script error:
Recovered diagnostic: apply_patch verification failed: invalid patch: The last line of the patch must be '*** End Patch'

Image 6 terra: 65 Arabic review flags; see sec6/terra/validation.json. Repeated proposals: 3; see consolidation.json. Missing existing citations: [].
Recovered diagnostic: duplicate 28:13 2
Recovered diagnostic: duplicate 75:25 2
Recovered diagnostic: duplicate 39:74 2

Image 7 luna: 57 Arabic review flags; see sec7/luna/validation.json. Repeated proposals: 0; see consolidation.json. Missing existing citations: [].
Recovered diagnostic: SyntaxError: unterminated string literal (detected at line 10)

Image 4: 193 unique candidates; 107 named by both models. 25 separate context neighbours. Dry Opus estimate $2.96; no call.

Image 5: 291 unique candidates; 134 named by both models. 31 separate context neighbours. Dry Opus estimate $4.03; no call.

Image 6: 270 unique candidates; 88 named by both models. 29 separate context neighbours. Dry Opus estimate $3.93; no call.

Both turns completed for every job in this batch. Input hashes, model/effort, unchanged initial rows, schema, unique final references and follow-up delivery are checked in native logs. Tool calls were reviewed before finishing.

All raw proposals remain intact. Repeated references do not change original grades. Arabic flags are review aids, not error counts. See validation_review.json where present; English meaning and relevance are not exhaustively verified.

Recorded incremental discovery estimate/charge: $0 on the Codex subscription. Token usage and all recovered diagnostics are in the JSON and native logs.
