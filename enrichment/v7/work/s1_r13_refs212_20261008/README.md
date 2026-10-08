# S1 original r13 references: Tier 1 completed

Scope: the 212 ayat missing Tier 1 coverage among references in S1's seven individual original v16 r13 ayah pages. Augmented pages are excluded. The frozen page paths and reference audit are in `scope.audit.json`.

All 1,075 chunks completed using native `gpt-6-luna` agents at `max` effort, with fresh contexts and at most 60 active agents. The existing 20,000-character chunk plan was retained. Repairs used the original assigned sessions.

Validation: 12,501 newly answered source segments, 101,310 rows, zero chunk problems, and zero missing eligible source segments across all 212 target ayat, including previously completed segments skipped by the build. `out/luna-max/check.json` records each chunk's validation; `completion.audit.json` records coverage per ayah.

The native-session usage report records 1,075/1,075 runs, 14,304 requests, $34.59 API-equivalent, and a maximum request input of 214,857 tokens. Twenty-eight chunks exceeded the 120k reporting cap; every output passed validation. All report warnings are preserved verbatim in `report.log`.

Forty-nine ISLAHI-TADABBUR segments have known source-index errors. Their note verse labels follow the source bodies, and each affected segment has an `index_warning`. Evidence and handling are documented in `source-index-issues.json`; the corpus index has not been edited. These warnings remain relevant when using the resulting notes.

The completed scope is Tier 1 only. No Tier 2 or page-writing work was launched for this run.
