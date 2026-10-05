**Source efficiency audit snapshot — 2026-10-05**

The [audit and recommendations](../../REVIEW_source_efficiency_2026-10-05.md) explain the measurements, limitations, and proposed workflow and data fixes. This directory preserves the measured state; it is not regenerated during normal enrichment runs.

| Files | Contents |
|---|---|
| `islamic_ayah.csv`, `intertext_ayah.csv` | All 6,236 ayat, ranked by attached primary-text characters; notes/translation sizes are separate |
| `islamic_surah.csv`, `intertext_surah.csv` | Per-surah totals, averages and shared-range expansion |
| `islamic_sources.csv`, `intertext_sources.csv` | Source identity, coverage, quality notes, segment counts and sizes |
| `islamic_summary.json`, `intertext_summary.json` | Aggregate measurements, database modification times, leading results and largest segments |
| `formats.json`, `packs.json` | Physical formats and existing pack sizes |
| `retrieval_proofs.json` | Captured cap/quality-flag reproduction, locator-family expansion, search-prefix examples and independent SQL checks |
| `edition_overlap_sample.json` | Sample normalized seven-word overlap; a diagnostic, not proof of equivalent content |
| `lexicon_markup.json` | Counts of retained OpenITI layout markers in selected lexical/grammar sources |

Characters are Unicode code points, not model tokens. An ayah includes each segment once when `s` matches and `a <= ayah <= coalesce(a_end, a)`. Surah totals can count a shared passage at several ayat; `unique_segment_chars` counts each attached segment once per surah. The Islamic and intertext indexes share some sources, so their totals are not additive. Zero directly attached intertext material does not mean no relevant Bible passage exists.

The scan is read-only and makes no model or network calls. Reproduce the inventory from the repository root with local corpus databases and packs present:

```bash
python3 -B enrichment/v2/tools/audit_sources.py --out .scratch/source-audit-new
```

Choose a new or empty output directory. The scan writes rankings, summaries and larger intermediate inventories there (about 140 MiB in the original run). Keep those intermediates local; this snapshot contains only the compact review evidence. The scan reproduces the inventory, format and pack measurements. The three separately captured diagnostic files (`retrieval_proofs.json`, `edition_overlap_sample.json`, `lexicon_markup.json`) document the additional inspections made during this audit.

The corpus is not frozen by this command. Later scans reflect the current source data; compare them with this dated snapshot instead of overwriting it. Source texts and databases are not bundled here.
