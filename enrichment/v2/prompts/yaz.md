# Stage 3 — yaz: compose the blocks

You turn the evidence into the page's blocks. You write records, not Markdown: a script inserts them into the
frozen base, builds the source registry and renders the ayah pages.

## Inputs
STAGE harita: claim_map.json, evidence_matrix.json, gaps.json. STAGE meal: annotations.meal.jsonl (already
validated; include it unchanged unless it duplicates one of your blocks). PACK as before. Re-open any source you
cite (`corpus.py get`) to check the wording you rely on; the matrix is a guide, not a substitute.

## What a good page has
- For every ayah: its anchor meaning (dayanak) from the received tafsir; the real disagreements (ihtilaf, with who
  holds what); the sense range (anlam_alani) where the tradition is plural; occasions and chronology with grades
  and historicity; sahih hadith that explain or illuminate; readings that change meaning; the lexical and wujūh
  evidence behind the base's words; grammar and rhetoric where they decide something.
- For every claim of the base of kind imge or sentez: a yenilik block (klasik_tanik, taranan, tarama, guc), plus
  oncul blocks for the antecedents found and itiraz blocks for argued counter-evidence; tercih blocks where a source
  merely prefers another reading.
- duzeltme blocks for errors in the base (wrong source label, misquotation, wrong ayah, factual error, wrong
  rendering), each with `taban` (exact base words) and `hata`; check PACK/errata_candidates.json and the matrix.
- elenen blocks for connections you weighed and rejected that a researcher would ask about (kat:arastirma).
- The meal blocks.
Coverage without repetition: one block per point; a report repeated unchanged by later works is one block with
`tekrar`. Do not restate the base. Each block must add a distinct unit of value: a witness, a disagreement, a
grade, a sense, an antecedent, a counter-argument, a correction, a consequence.

## Record format (annotations.jsonl, one JSON object per line)
All schema fields as keys (see schema.json; enum values exactly as listed), plus placement:
- `capa`: an exact sentence of PACK/base/surah.md; the block goes after the paragraph containing it. Choose the
  paragraph the block speaks to. Without a capa the block goes to the end of the page: use that only for
  surah-level blocks that belong nowhere else.
- `capa_ayet`: an exact sentence of the ayah page PACK/base/S_A.md for the ayah the block is about (optional; without
  it the block goes into a closing section of that ayah page).
ids: S<sss>-<KOD>-<NNN> with the KOD of the block's tur (schema.json), numbered in page order per KOD.
Layers: kat:temel for what an advanced reader should see first at that point; ek for supporting detail;
arastirma for the audit trail (novelty detail, rejected candidates, technical source criticism).

## Finish
Write annotations.jsonl into your stage directory (your blocks plus the meal blocks). Then run
`python3 enrichment/v2/validate.py --surah N --annotations <stage>/annotations.jsonl --out /nonexistent`
and fix every error; then `python3 enrichment/v2/render.py --surah N --annotations <stage>/annotations.jsonl --out
<stage>/preview` and read the rendered surah page once from top to bottom as the reader would: remove repetition,
move blocks that sit at the wrong paragraph, tighten prose. Validate again. Final message: blocks by tur and kat,
novelty counts by klasik_tanik, number of oncul / itiraz / duzeltme blocks, and anything you could not do.
