# S95 image discovery — session 2026-10-05

All 12 sections completed with Luna max and Terra (GPT-5.6-Sol max), including one follow-up per selected agent. The runs were reviewed, consolidated, and merged.

Total: **3486 image–ayah candidate pairs**. These are discovery candidates, not confirmed relevant additions. No augment adjudication has run for this surah.

| Image | Title | Candidates | Selected attempt |
|---|---|---:|---|
| 1 | Dikilen boy, yere indirilen beden | 319 | session-20261005 |
| 2 | Bir ömrün evreleri | 221 | session-20261005 |
| 3 | Ustanın elinden çıkan iş | 326 | session-20261005 |
| 4 | Değer biçmek, tartmak, ödemek | 320 | session-20261005 |
| 5 | Kesilmeyen ücret | 189 | session-20261005 |
| 6 | Yük taşıyan, yolda kalan | 309 | session-20261005 |
| 7 | Yaratılış ve dosdoğru din | 311 | session-20261005 |
| 8 | Güvenilen söz ve yerleşik kalp | 377 | session-20261005 |
| 9 | Hâkim: alıkoymak, karar vermek, geri döndürmek | 315 | session-20261005 |
| 10 | Yeminin yerleri: dağlar, Tûr ve güvenli belde | 216 | session-20261005 |
| 11 | Meyve, yağ ve rızık | 184 | session-20261005 |
| 12 | Buluşmalar | 399 | session-20261005 |

Raw first-turn lists, follow-up proposals, duplicate audits, and accuracy concerns remain beside each model run. Initial formatting issues corrected before snapshots are retained in the tool audit. All selected final deliverables passed the existing output checks; the two explicit process exceptions below remain part of the record. Arabic quotation flags are review aids, not measured error rates.

The merged tier is the best label proposed by the readers, not validated confidence. Relevance and precise wording still require canonical-text and paragraph-level judgment. Parent review covered workflow compliance and reported issues, not an independent assessment of every candidate.

Runbook and production defaults are unchanged. S96 remains excluded.

Session exceptions and accuracy notes:

Section 3 Luna ran an awk row count immediately after writing followup.tsv. This departed from the no-read/no-script follow-up instruction. The public tool audit shows a count of its own output, with no new source lookup or extra candidate pass. The output was accepted with this explicit exception; see sec3/luna/protocol-exception.json.

Section 8 Luna supplied 166 first-turn rows with two entries for 81:25. Before the snapshot, the parent preserved list.raw-before-dedup.tsv, kept the first occurrence unchanged, and removed the repeated occurrence into the format-correction.json audit. The normal 165-row snapshot and fixed follow-up then proceeded. This parent correction is an explicit departure from the strict retry protocol; both original labels remain inspectable.

Section 1 Luna had several failed local patches before its first-turn snapshot; the final list passed formatting checks. These attempts remain in tool_calls.json.

Accuracy notes remain provisional: section 10 Terra distinguishes 26:146 from the cultivated setting in 26:147–148; section 11 Luna notes that 12:49 mentions pressing produce without specifying olives; section 1 Luna marks sky and mountain support parallels as interpretive. The section 2 Luna root label for 17:51 also needs downstream checking. None of these lists has received independent all-candidate relevance adjudication.
