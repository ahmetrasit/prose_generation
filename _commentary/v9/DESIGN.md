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

## Findings log

- **Luna-6 surah chain run** (`pilot/luna6-chains/`, ~38 min, redid S1 after compaction):
  opened all 69 ayah pages / 226 roots / 1,951 branches for S29, yet missed 29:38 eye-film
  (سبل B010), kohl (صدد B013) and 29:45 second horse (صلو B006). Found other real catalog
  activations (بيت B003 verse-line ↔ 29:43 أمثال; ندو B006 herd between water and pasture;
  غشو B005 fainting; حرم B005 sacred month). Chains are mostly contextual-sense thematic maps.
  → False negatives are attention, not access: supports precomputed pair lists + per-pair verdicts.
- **Root identity gateway** (quran-data origin/main e523a206c): 1,642 QAC root rows; 11 composite;
  103 rows with 116 withheld observational targets (policy: discovery evidence only, not identity).
  عود → root_001058 only (ع د د root_000989 withheld); اسم → سمو primary, وسم word-scoped alternative.
  Assessment: correct for identity; but consumers following the rule lose sound-family evidence
  that latent-reading work uses (classical ishtiqāq kabīr / jinās). Proposed fix: a separate typed,
  word-level, non-identity layer (e.g. `qac-root-sound-echoes.json`: selector qacRef|lemma, echo root,
  type = withheld_observed_target | shared_two_radicals_weak | metathesis | documented_jinas,
  evidence, status "resonance candidate, not identity"). V9 shows it in its own package section;
  writer may use it only as a sound-echo note unless a classical source supports a semantic link.
- **quran-data pulled** (2026-09-24, by user): HEAD 2a4e17469, level with origin/main. Gateway files
  are in the working tree (`data/bridges/qac-dictionary-root-resolutions.json`,
  `qac-dictionary-word-root-analyses.json`). Remaining uncommitted local work is the prefatory-alias
  set (112 TSVs + docs/schemas/scripts/tests); numbered `reciprocal/focus_S_A` files used by V9 are clean.

- **User review of 29:38 reading (2026-09-24): "great / excellent analysis and prose".** Gaps raised:
  1. بيت = night shelter (Tahdhīb: سمي بيتا لأنه يبات فيه; Mufradāt: مأوى الإنسان بالليل; B004 night
     action/raid; B007 grave) ↔ عشو B006 "sees by day, not at night" (43:36) ↔ مستبصرين. Missed in pilot.
     Global image network: عشو B006 → بصر B001 rank 10, but → بيت B001/B004 rank 399/371: the link is a
     shared component (night), not image similarity. Fix: **shared-concept (motif) links** — index content
     lemmas/concepts in branch definitions (ليل, عين, طريق, ماء, نسج…) with rarity weighting, plus a small
     complementary-relation table (ليل↔نهار/صبح); check quran-data `analysis/channels/network-v3` motifs as a source.
     Context support: 29:37 فَأَصْبَحُوا (morning), 15:83 مصبحين, 37:137-138 morning and night.
  2. Ād / ع د د: user wants it kept (gateway withholds root_000989 for عود). V9 packager v2: for each focus
     word, include withheld/observed targets from the occurrence map as **echo roots** with full branches,
     flagged as non-identity; recover all such cases, not only Ād.
  3. Fātiḥa road (اهدنا الصراط المستقيم / صراط الذين أنعمت عليهم / الضالين) should resonate with §3; missing
     because 29:38's inter-ayah rows contain no S1 target and the pair network is surah-local. User adds
     Fātiḥa to every ayah analysis (recited in ṣalāt). Fix: **Fātiḥa lens** as a standing package section
     (S1 text, focus×S1 branch pairs, context×S1 bridges, near-synonym سبيل↔صراط); writer weaves or gives a
     section. For 29:38: 29:45 prayer = daily recitation of اهدنا الصراط; 7:16 صراطك المستقيم; Fātiḥa asks for a
     road defined by who walked it (صراط الذين أنعمت عليهم) — a walked road, but of the favoured.

## Packager v2 (built 2026-09-24; `prepare.py`, output `input/v2/s029/29_38/`, ~844 KB)

Files: 00_ayah, 01_dictionary (identity / documented alternative / ECHO roots), 02_hft, 03_pairs (±7),
04_bridges, 05_usage (concordance, rare-lemma occurrences + co-occurring roots, hapax, near-synonyms),
06_concepts (concept paths), 07_fatiha, 08_surah (whole surah), 09_inter_ayah (formula groups ≥2), 10_leads.
Affinities are computed from the global quran-slm rank maps (rows only; fusion 0.35 E5 / 0.35 Neo / 0.30 char)
over gateway-based activations — the old surah views and their alignment table are no longer used.
Verified on 29:38: ECHO ع د د for عادا; eye-film → spider still first near partner; new same-ayah عمل B010
(working organ / far-seeing eye); Fatiha: سبيل B001 → صراط B001 (1:6), اهدنا, ملك B006 "middle of the road";
مستبصرين hapax; concept path 43:36 عشو B006 ⇒ [ليل] 29:41 بيت B001, [نهار] 29:37 فأصبحوا, [ضعف] 29:41 أوهن.
Weak spots: concepts file is large (262 KB) and noisy; bridges noisy; formula grouping by exact root
signature barely groups (needs similarity clustering). Opus-lane brief: `prompts/opus_reader.md`.

## CURRENT STEP (2026-09-24, before compaction)

1. Sonnet code-review agent is reviewing `prepare.py` (launched in-session; handle saved in session scratchpad
   `reviewer.txt`). When it reports: fix findings, send the patch to the SAME reviewer for re-review.
2. DONE: reduce package (below), regenerate 29:38 v2. NEXT: commit **and push** (user: push before the cold run).
3. Then: cold-instance Opus run (Agent tool, model opus, fresh) with `prompts/opus_reader.md` on
   `input/v2/s029/29_38/`, outputs to `pilot/29_38-v2/` (notes.md, 29_38.reading.tr.md, 29_38.harvest.md).
   **Monitor its token usage** (user request) and report it.
4. User reviews; compare with `pilot/29_38/` (in-session reading).

### Cost estimate (Opus 5.5: $4/M in, $20/M out, cache reads $0.20/M, cache writes ~1.25× input)
Package 844 KB ≈ 370k tokens (Arabic/Turkish ≈ 2.3 bytes/token). Agent reads in ~25k chunks (~15-20 steps),
re-sending growing context: ≈ 370k cache-write (~$1.9) + ~4M cache-read (~$0.8) + ~60k output incl. thinking
(~$1.2) ≈ **$4 per ayah** API-equivalent (≈ $8k for 2,000 ayat). Reduced package (~450 KB) ≈ $2.3/ayah.

### Package reduction (done 2026-09-24; 844 KB → 600 KB ≈ 260k tokens ≈ $3/ayah)
Measured, not the planned figures:
- 06_concepts 262 → 106 KB. Root grouping and deduping alone saved only ~10%, because each branch finds
  different targets. The real savings came from two changes: definitional filler added to `_GENERIC`
  (اسم معروف حال بعد جمع…), and ranking rows by summed concept idf, `CONCEPT_TARGETS = 10` per root.
  Ranking by affinity instead dropped the عشو path. Hits per concept went 3 → 5, so 29:41 بيت stays on
  the [ليل] hit list. Invariant: بصر → 43:36 يعش ع ش و B006 ⇒ [ليل] … 29:41 بيت B001.
- 09_inter_ayah 239 → 167 KB. Neighbour ayat were first kept for strong+medium rows, but those are 263 of
  350 rows, so that saved only 26 KB. Neighbours are now kept only for targets with a strong row.
- 04_bridges 39 → 19 KB (`BRIDGES_MAX = 60`). 01_dictionary (91 KB) and 03_pairs (98 KB) are unchanged.
Code-review fixes: rank-0 sentinel in `top_fast`; identity-first dictionary; vectorised reverse ranks
(runtime 20 s → 5 s); deduped `top_distinct` pool labelled by nearest occurrence; tighter `is_root_form`;
one-letter proclitics via `_lemma_form`.

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
