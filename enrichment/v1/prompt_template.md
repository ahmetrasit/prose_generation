# Surah enrichment agent prompt (S87–S114) — fill the {{VARS}} and send

You are producing an enriched commentary for Surah {{SURAH}} (ayah scope 1-{{N_AYAT}}) following a written protocol.
Workspace root: /Volumes/aro/projects/prose_generation (paths below are relative to it).

READ FIRST, COMPLETELY: enrichment/v1/Tafsir_Comprehensive_Annotation_Instructions.md (schema 2.0).
Read enrichment/v1/validate_output.py and run it at the end; fix every error.
(`python3 enrichment/v1/validate_output.py --base <BASE_MD> --output <OUTPUT_MD> --target {{SURAH}}`)

TARGET: {{SURAH}}  BASE_MD: {{BASE_MD}} (verify sha256 {{BASE_SHA256}}, read the ENTIRE file)
OUTPUT_MD: enrichment/v1/out/{{SURAH}}/{{SURAH}}_enriched.{{VARIANT}}.md
WORK_DIR: enrichment/v1/work/{{SURAH}}_{{VARIANT}}/   (all scratch here)
LANGUAGE: preserve base (Turkish). MODE: comprehensive. Schema 2.0.

## File rules
- Write ONLY inside WORK_DIR and OUTPUT_MD. Everything else is read-only: other runs' outputs/work dirs, manifest.json
  (the orchestrator updates it), the corpus, the dictionary repo.
- Independence: do NOT read other runs' annotations, evidence matrices or enriched .md files for this surah.
- Preserve base prose, headings, order and existing {ar:..., tr:..., gloss:..., source:...} tags byte-for-byte.

## Shared corpus (use it first; do not re-download what is already there)
1. Tafsir (per ayah, extracted text): enrichment/v1/corpus/tafsir/<book>/<surah>_<ayah>.txt
   Books: tabary katheer seoty zamakhshary alrazy baidawy beqaay qortoby atia hayyan alusy baghawy mawardy wahidy ashour nasafy.
   Index with URL + sha256: enrichment/v1/corpus/tafsir_index.jsonl. Neighbouring ayat/surahs are present for naẓm (86:17 .. 114:6).
   CAUTION: `seoty` may not be al-Durr al-manthur and `wahidy` is probably al-Wasit, not Asbab al-nuzul — open one page, check the
   title/author line before citing it under a given source name. If Durr/Asbab are not covered, say so; do not silently substitute.
2. Hadith (whole books, ara/eng/tur, FTS index): enrichment/v1/corpus/hadith/ — see README.md there.
   `python3 enrichment/v1/corpus/hadith/search.py 'رياء' [--book bukhari] [--lang ara|eng|tur] [--n 10]`;
   `search.py --get bukhari 6499`. Prefix match per word, not root match: try spelling variants. Dataset numbers are NOT
   sunnah.com numbers: cite collection + dataset number + opening words of the matn. Grades exist only for abudawud/tirmidhi/
   nasai/ibnmajah/malik and are per named grader — record the grader; Bukhari/Muslim have none => hadith_grade:not_assessed
   unless you verified one yourself. sunnah.com is Cloudflare-blocked; do not rely on it.
3. Lexicon = the project's own dictionary, NOT web lexica:
   enrichment/v1/corpus/dictionary_agent/agent/  (local build of /Volumes/aro/projects/dictionary; read START_HERE.md there).
   Ladder: aliases/by-initial shard -> root/<root_id>/card.md -> routes.min.json -> branches.select.min.json ->
   occurrences.compact.json. Arabic root identity is authoritative; ASCII/folded aliases are candidates only.
   Report EVERY candidate root_id you inspected and which matched. Open full packets
   (/Volumes/aro/projects/dictionary/data/output/root_packets/<root_id>.json) only if the compact files are insufficient.
   The agent copy is a snapshot; the repo at /Volumes/aro/projects/dictionary is the source of truth.
   Maqayis stays primary per the protocol (§13.H); say which lexicon an observation comes from.
4. Qur'an text: /Volumes/aro/projects/quran-data/data/text/quran-uthmani.tsv (the basmala is listed as ayah :1 of each surah
   except 1 and 9, so file ayah numbers are shifted by one — do not quote by file index).
5. Anything not in the corpus (e.g. Turkish meals, Durr al-manthur, Asbab al-nuzul, modern scholarship): fetch from the web,
   record URL + date, and keep only wordings you confirmed on two pages or on an official site. Never reconstruct a translator's
   wording from memory; list translators you could not retrieve as "not retrieved".

## Workflow and epistemic rules
Follow protocol §14/§21: claim map -> evidence matrix BEFORE annotations -> minimum corpus (§13) -> novelty audit with explicit
checked_sources -> rejected candidates -> dedupe -> local insertion -> registry + source-criticism note -> §18 QC.
Use only sources you actually opened. Never invent grades, quotations, page numbers or URLs. Say what you could not access.

## Turkish meal review (required)
Compare mainstream Turkish meals (Diyanet current + old, Okuyan, Yaşar Nuri Öztürk, Elmalılı, Bilmen, Ateş, Hayrat, Gölpınarlı,
Bulaç, Diyanet Vakfı, others if retrievable) on the surah's key terms. Flag wrong / misleading / range-collapsing renderings,
separating an outright error from a defensible narrowing, with grounds in the Arabic, dictionary and early authorities.
Encode with EXISTING enums only (e.g. type:semantic_history, relation:comparative, role:semantic_range|disagreement|constraint,
status:interpretive), `scope:"meal-review:<term>"`, `scholar:` = translator, ids S{{SURAH}}-MEAL-NNN. Add a reader_note
explaining how to filter them. Short key-term quotes only.

## Finish
Run the validator; confirm base preservation, unique IDs, every source ID resolves in the registry, every novelty block has
checked_sources. Write WORK_DIR/audit_summary.json (blocks by type, novelty count, contested reports, source count,
translations retrieved vs not, dictionary root_ids inspected, unresolved items).
Final reply (concise): output path + sha256, validator summary, counts, retrieved/not-retrieved translations, 5-10 translation
findings, unresolved items/deviations.
