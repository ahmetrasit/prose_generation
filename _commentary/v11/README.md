# Commentary v11 — one Opus call per ayah, script evidence, findings ledger

Goal (the user's): readings that help one understand an ayah through supported, non-canonical surprise readings —
al-Biqāʿī (the ayah through its neighbours and its surah), al-Khūlī (a word through all its Quranic uses and its
root's attested senses), the Quran explaining the Quran — in Opus-quality Turkish prose, with the breadth of
findings kept, under $5 per ayah.

## Workflow (`run.py`)

1. **prep (scripts, no model)**: V9 input package (`01_dictionary.md`: every attested branch of every root of the
   ayah with the classical source phrases), `context.md` (ayah, words, word notes, Fatiha, whole surah), and
   `digest.md` (`_commentary/v9/lines/digest.py`: the ayah's qirāʾāt from `study/_project_corpus/qiraat.tsv`, every
   root's Quranic occurrences as refs + word, the reciprocal inter-ayah candidates as refs + opening words).
2. **write (one Opus call, effort high, no tools, no MCP)**: evidence first, brief last (`prompts/write.md`). Quran
   from memory is allowed (every quotation is verified against the canonical text); non-Quran Arabic only from the
   dictionary; unanchored lexical claims and unlisted readings are marked `[recall]` in the ledger. The answer is a
   **findings ledger** (Turkish, one line per finding with refs, roots and core/develop/note, in the order Surah →
   Quran → Dictionary → Readings and grammar → Fatiha), then the **reading**, which develops the core findings.
3. **check**: `verify_ar --fix` (Quran + dictionary quotes), tag validation, mechanical tag repair, metrics, cost.
4. **render**: `S_A.md` = the reading + **Kur'an'ı Kur'an'la** (ledger Surah/Quran/Fatiha entries, each ref with its
   ayah text) + **Kelimeler ve okuyuşlar** (ledger Dictionary/Readings).

5. **chains (once per surah, after all ayat)**: one Opus call over the surah text and every ayah ledger
   (`prompts/surah.md`) → `out/sNNN/surah/chains.md` (chains across ayat: members, roles, movement, what the surah
   says through the chain that no single ayah says), `S.surah.tr.md` (a reading of the whole surah) and `ayat.md`
   (one note per ayah, rendered into each `S_A.md` as **Surenin bütününde**). This recovers what S1's HFT image
   chains got from analysing all ayat together, at one call per surah.

`python3 _commentary/v11/run.py all S:A` · `python3 _commentary/v11/run.py surah 100` → `out/sNNN/S_A/` · `python3 _commentary/v11/run.py chains 100`.

## Why this shape (evidence: `_commentary/v9/lines/work/*/synth/`, 2026-09-25/26)

Anchor recall (findings any earlier setup found; reading / reading + ledger):

| setup (4:34, 12 anchors) | reading | + ledger | cost |
|---|---|---|---|
| cold Opus (context only) | 8 | 8 | $1.58 |
| cold Opus, repeat | 6 | 6 | $1.50 |
| + dictionary | 5 | 5 | $1.88 |
| + full Luna package | 5 | 5 | $2.93 |
| + dictionary + slim Luna | 9 | 9 | ~$2.2 |
| **v11: dictionary + script digest, ledger** | **9** | **11** | $2.49 |
| v11 with slim Luna instead of the digest | 5 | 9 | $2.50 |

18:86 (10 anchors): v11-script 8/9, v11-luna 9/10, cold 8/8, full package 9/9. 1:2 (7): v11-luna 6/7, cold 6/6,
dictionary 1/1 (the dictionary arm had been told "only the supplied evidence" while the context held only surah 1).

- **Sampling variance is large** (cold vs repeat cold: different anchors each time); a ledger written before the
  prose captures most of the union in one call.
- **Luna's judgment did not beat its own unjudged candidates**: the script digest gives the writer the same reach
  at no discovery cost (Luna discovery was ~20–35 sessions and ~1M tokens per ayah). Luna stays available in V9.
- **Input size costs thinking** (4:34 thinking tokens: cold 45k → full package 9k), so the writer's input is kept
  to context + dictionary + digest; HFT, the network pass and full packages are left out.
- The earlier "dictionary crowds out Quran reach" was mostly an instruction artefact (fixed in `write.md`).

Cost so far: 100:1 $0.86; 4:34 $2.49; 18:86 $1.81; 1:2 $2.34 (long ledger). `claude -p` bills input as a
1-hour cache write; direct API or batch calls would cut this for a large run.

## S100 (al-ʿĀdiyāt), the first full run

11 ayat, $11.14 ($0.77–1.30 per ayah); ledgers 40–66 findings, readings 1,450–2,040 words; validator errors 0.
Chains pass: $1.21, 16 chains (e.g. the struck stone that gives fire ↔ the *kanūd* who gives nothing ↔ the breasts
opened, 100:2/6/10; breath from the chest ↔ what is in the breasts, 100:1/10), a 1,133-word surah reading, notes for
all 11 ayat. Total ≈ $12.35, about $1.12 per ayah.
Validation (100:1, 100:6, 100:10): cold and dictionary-only Opus readings cite almost nothing the v11 ledger lacks
(missed: 2:36, 81:18 on 100:1; 47:4 on 100:6).

## Production: API batch with a shared cached prefix (decided 2026-09-26, not built)

`claude -p` sends each ayah's input as one message with its own cache point at the end, so ayat of one surah share
no cache (every run shows cache_read 0 on its first call) and overlapping content is paid once per ayah. For
production, call the Messages API directly in **batch mode** (half price) and order each ayah's input as
**shared prefix first** — system + brief + whole surah + surah branch table + seed sheet, byte-identical for every
ayah of the surah — then an explicit **cache_control marker**, then the ayah-specific part (its dictionary, digest
v2, its seed lines). The first ayah writes the prefix, the others read it at ~1/10 of the price. Keep one fresh
call per ayah (parallel, clean context); one agent walking the surah turn by turn is not cheaper enough to pay for
its growing context (~500k tokens by ayah 20), homogenisation and serial run time. Rough, 20-ayah surah: no reuse
≈ $38; shared cached prefix ≈ $30; + batch ≈ $15. Output (mostly thinking) is ~80% of the cost either way.

## Open

- The user's blind read of v11 vs the best earlier setup on a few ayat.
