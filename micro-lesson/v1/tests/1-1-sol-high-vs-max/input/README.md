# Shared 1:1 pilot input

Page ID: `1:1`. Both conditions use this same packet. Focus ayah: 1:1.

Source: `_commentary/v16/out/1_1/DM.r13.images.r13.map3.nohft.tool.tool.tool/1_1.reading.tr.md`. The complete base reading is used (27 prose paragraphs); augment variants are not part of this pilot. Original wording is unchanged in `commentary.original.md` and `paragraphs.json`. Headings are context, not lesson targets. All paragraph IDs p01–p27 are assigned.

Read `paragraphs.json` for text and per-paragraph evidence scope; `paragraphs/pNN.md` is a convenient individual view. `ayat/S-A.json` supplies exact Arabic and QAC morphemes for focus and cited/discussed ayat (57 total). References 1:2–7 in p01 resolve its explicit discussion of the remaining six ayat; other implicit local references are listed alongside explicit ones. No automatic neighboring ayat are supplied.

The Quran text comes from `../quran-data/data/text/quran-uthmani.tsv`; morphology from `../quran-data/data/morphology/qac.sqlite.gz`. Quran source locators may be `1:1`, `qac:1:1:1:1`, etc.; packet locators may use relative file plus a named field or branch.

`word-root-analyses.json` preserves reviewed lexical selectors and documented alternatives. Apply each only to its stated lemma or morphemes. `root-source-index.json` maps the other attested QAC roots to local entry and gloss paths. These paths are relative to the repository root, not this input folder.

`dictionary/index.json` lists full semantic evidence for all branches of the six root families actually discussed by this page. Each branch file carries Arabic boundaries, source phrases, conceptual facets, Turkish glosses, applicability, error profiles, and source qualifications. It includes the upstream source and finalized projection where available, plus reviewed glosses. These are alternative views of evidence, not separate review passes. Where source versions disagree, inspect the exact discrepancy and qualify or defer only the affected claim. A source-entry `repair`/`editorial_review` flag is retained; the result being `reviewed` does not erase it. Some referenced review-response files are unavailable locally. For و ل ه, the quran-data export supplies the entry because a finalized local entry/gloss result is absent.

The dictionary public START_HERE URL returned HTTP 404 during preparation. Root identities instead follow the existing reviewed quran-data bridges, including the exact documented alternative و ل ه → root_005296; no broad full-packet search or dictionary rebuild was used. Consult `../dictionary/data/supplemental/registry.v1.json` before concluding an unlisted word has no entry. Agents may read relevant indexed source files; do not browse for new external evidence in this controlled comparison. Missing attestation is an opportunity-specific deferral.

Commentary's Turkish expressions are the quoted text of each paragraph. Dictionary gloss labels and their error profiles are evidence about those specific glosses, not automatic verdicts on either the commentary or the verse. No independent Turkish diachronic corpus is supplied.

Workflow instructions and ontology: `micro-lesson/v1/`. Use every paragraph; there is no lesson quota. Do not edit the input, commentary, ontology, workflow, or the other run's files.
