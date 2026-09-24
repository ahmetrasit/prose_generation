# Commentary V9 — design and working state

Status: design agreed in discussion (2026-09-24); packager v1 + 29:38 Opus pilot built
(`prepare.py`, `pilot/29_38/`). This file is the durable plan; update it as decisions change.

## Goal (user's words, condensed)

A Turkish reading of each ayah that a non-Arabic reader can finally *hear*: not the
canonical meaning (available elsewhere; used only as an anchor to tell what is latent),
but the latent activations and resonances, **synthesized** into coherent prose.
Model: al-Khūlī / Bint al-Shāṭiʾ (word meaning by induction over its Quranic usage)
and al-Biqāʿī (connection of ayah to its neighbours and the surah's purpose).
Harvest every information, but integrated and coherent: no semantic ledger, no
paragraph-per-item. No word limit; long ayat get more themed sections.

## Lessons that constrain the design (from V5–V8 and the 29:38 inspection)

- Agents skip what they choose not to read. Packages must be small enough to be read
  whole (raise Codex `tool_output_token_limit`; each file under it; one parallel read).
  Many-small-files and paged reading (V6) failed; single-explanation schemas (V7) lost findings.
- Luna follows worklists well, synthesizes poorly. Give Luna per-item lists; synthesis
  goes to a capable writer. Luna also benefits from per-item records (anti-skipping), but
  single free-text explanations become generic → records need specific, checkable fields.
- V5 global lane used 0 of 253 inter-ayah rows for 29:38; the final editorial cited one
  non-S29 ayah. The whole-Quran layer must be a worklist (the rows), not background.
- HFT records are strong, precomputed discovery. Treat them as hypotheses to verify and
  articulate, resolved to actual context words; never gate them by registry metadata.
- Word-analysis topics are canonical-level support, not obligations (no particle walk).
- Canonical-reading bias: agents distrust rare senses. Make rare senses *data-proposed*
  (pair lists), and apply the two-key rule: dictionary branch + independent trigger in
  text/context = reading; branch alone = harvest note.
- Pericopes were only a context-size shortcut; drop them. Use whole-surah context.
- Compaction loses in-context work (Luna redid S1). Write per-item records to disk as you go.

## Package (per ayah; all deterministic; each file read whole)

1. `00_ayah` — Arabic, QAC words, anchor translation, word notes (support only).
2. `01_dictionary` — every branch of every focus root: gloss | Arabic image | definition |
   facets | not | source phrase. Prose-only fields (contextual glosses, error profiles,
   lexical glosses) go to the writer's gloss sheet only.
3. `02_hft` — every HFT record; each trace step resolved to the actual word (surface,
   root, branch gloss + Arabic image).
4. `03_pairs` — quran-slm surah network: for every focus branch, top-3 partners by
   *distinct partner root*: same ayah / near window / surah-wide.
5. `04_surah` — whole surah text (no pericope).
6. `05_inter_ayah` — reciprocal rows (quran-data `inter-ayah/reciprocal/`), grouped by target,
   with target ayah ± 1 neighbour text.
7. `06_leads` — reader walks / cross-run publication when present.

### Packager v2 changes (agreed / proposed, not yet built)

- Roots from quran-data gateway: `data/bridges/qac-dictionary-root-resolutions.json`
  (+ word-scoped `qac-dictionary-word-root-analyses.json`); morphology from
  `data/morphology/qac.sqlite.gz` (not quran-slm's TSV).
- Near window ±7 (not ±3): 29:41's Pharaoh (29:39 سابقين) ↔ prayer (29:45 ص ل و B006
  second horse) needs +4. Measured: bridge appears at ±5.
- Context↔context **bridges**: mutual top-2 cross-ayah pairs within ±7, ranked by their
  link to a focus branch (focus-anchored two-step paths). ±5 ≈ 300 bridges for 29:41.
- **Per-root concordance** (surah + Quran): network excludes same-root pairs, so echoes
  like 29:19 يُعِيدُهُ (ع و د) and سبيل in 29:12/29:29/29:69 were missing.
- **Usage profile** (al-Khūlī istiqrāʾ) per focus root/lemma/form: all Quran occurrences for
  rare lemmas (≤ ~20), co-occurring roots across them, hapax/rare-form flags.
  Test: حمأ = 4 occurrences, 3 human creation (خلق, صلصل, سنن, بشر) + 18:86; مستبصرين hapax.
- **Near-synonym contrast**: nearest cross-root branches (corpus network) with their usage
  profiles (e.g., حمأ vs طين/تراب/صلصال) so "loaded beyond the dictionary" becomes visible.
- **Pair ordering**: rare focus sense × partner's contextual sense first; rare×rare capped.
  Needs a per-occurrence contextual-sense tag (one pass per surah).
- Inter-ayah: cluster formula repeats (e.g. "Satan beautified… barred from the path") into
  one representative + member list.
- Sound-echo layer (see root-identity note below) shown separately from root identity.

## Lanes

- **Opus lane** (capable model, single pass): reads the whole package, writes the reading
  + harvest record. 29:38 pilot: ~350k tokens incl. building; ≈ $1.7/ayah API-equivalent.
- **Luna lane** (Luna-6): worklists, per-item records written to disk:
  - A. micro: focus words × all branches (dictionary + same-ayah pairs + usage profile).
  - B. macro: HFT items + near/surah pairs + bridges (surrounding ayat activating focus).
  - C. global: inter-ayah rows (chunks ≤ ~80 targets) → per-row verdict, then theme grouping.
  - Record fields: focus word (Arabic), trigger word (Arabic), branch, before, after, reason.
    Checker: quoted Arabic must occur in the cited ayah; repeated sentences flagged; every
    item has a verdict ("none" uses short codes).
  - Writer: outline turn (themes with thesis + item ids; checker: every kept item placed
    once) → prose turn → self-review turn. Writer model configurable (Luna default for cost;
    compare with Opus).
- Middle layer: decide after a real run. Invitation: unchanged downstream consumer.

## Output shape (reading)

Short anchor (canonical, reference only) → themed `##` sections, each a thread with a
thesis; micro/macro/global woven, actual Arabic words tagged `{ar:…, tr:…, gloss:…}`,
citations `(S:A)` beside claims (no ranges) → closing → `## Ek Notlar` (one sentence per real
but unthreaded finding). Certainty by wording; limits stated once where they matter.
Validator: `_commentary/v5/validate_prose.py` (no commas in tr fields, no colons in gloss).

## Open items / next steps

1. Pull quran-data (user allowed; ask on conflicts); build packager v2.
2. Review Luna-6 chain outputs (`pilot/luna6-chains/s001.chains.md`, `s029.chains.md`).
3. User reviews `pilot/29_38/29_38.reading.tr.md`; possible cold-instance Opus rerun
   (needs a written Opus-lane brief) to control for my exposure to earlier 29:38 outputs.
4. 29:38 sample §6 ("counting" via ع د د) relied on the old split mapping; the gateway now
   withholds root_000989 for عود → drop or reduce to a sound-echo note.
5. quran-slm: rebuild surah views from the gateway; add per-occurrence sense tags,
   concordance, bridges/paths, usage profiles, near-synonym contrasts, optional TR/EN
   channels; build a small recall set of known links (HFT outliers, 29:38 eye-film + kohl,
   29:41 second-horse) and measure every change on false negatives.
