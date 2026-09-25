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

## CURRENT STEP (updated 2026-09-24 evening)

1. DONE: packager v2 + review fixes + reduction; cold Opus run (`pilot/29_38-v2/`); Opus brief fixed
   (`prompts/writer_rules.md` shared by all writers; `opus_reader.md` slimmed; `verify_ar.py`).
2. DONE: Luna findings lane built and run on 29:38 (section "Luna findings lane" below).
3. DONE: writers on Luna's findings — `pilot/29_38-gpt-6-sol/`, `pilot/29_38-gpt-6-luna/`,
   `pilot/29_38-opus-findings/` (Opus 5.5 subagent). NEXT: Opus 5.5 review of outputs and plan.
4. NEXT: compare the three readings (Opus cold, Sol, Luna) against the user's goal and the key findings;
   the user decides whether Sol/Luna come close enough to Opus. Quality verdict comes before more building.
5. THEN (user agreed): push → script pass → grep-based repair (below); shared-trigger index in merge.

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

### Cold Opus run on the v2 package (2026-09-24; `pilot/29_38-v2/`)
Opus 5.5 subagent, cold (read only the brief and the package). Interrupted once by the plan's session
limit and resumed with its context. Read every file to the end; the harvest accounts for all 15 HFT
records; `validate_prose` ok. Reading ≈ 4,500 words, 6 thread sections.
Usage: 46 calls, 736k cache write, 12.2M cache read, peak context 466k, 37k output (thinking ≈ 5–11k,
estimated) ≈ **$6.9 API-equivalent**. The cost is dominated by re-reading a 300–460k context every call:
about 30 Bash calls went to checking Arabic quotes.
Recall against the user's checks:
- Present: eye film (spider's-web veil), kohl in ص د د, the Ād ↔ ع د د sound echo (once, as echo),
  29:41 spider house, the سكن ⇐ night sense (جعل الليل سكنا).
- Missing: the 43:36 night-blindness ⇒ بيت night-dwelling ⇒ "sees by day, not at night" path
  (43:36 is cited only plainly); the salla second-horse link.
- Partial: the Fātiḥa road (its own section) and the worn-road section do not meet.
Cost levers: reading in bigger chunks (fewer calls); a cheap script to check Arabic quotes instead of
agent Bash loops; putting 09 earlier or splitting it off.

## Luna findings lane (built 2026-09-24; `luna/`, prompts `luna_worker.md`, `findings_writer.md`)

User rules for this lane: all GPT runs at max reasoning (Luna 6 max, Sol 6 max); do not squeeze input or
output for its own sake — only for attention (dilution, skipping); V9 may cost more than V5 if it performs
better. No trimming of Luna's inputs (concept paths stay): the risk is Luna skipping, not size.

- `worklists.py`: package → `context.md` (ayah, Fatiha, surah) + bundles ≤40 KB: W1 one item per focus
  branch (dictionary line + all its pairs, concept paths, Fatiha pairs, bridges as numbered lines) and one
  usage item per root; W2 HFT + leads; W3 inter-ayah targets (formula groups kept together).
  29:38: 397 items, 1,234 numbered lines, 17 bundles (W1 11, W2 1, W3 5), ≈190k tokens (o200k).
- Luna returns per item a verdict; per numbered line a code (- n r); every n/r line its own full record
  (`<item>.<k>`). "A miss costs more than a false alarm": the partner/concept word is the trigger; the
  other ayah need not spell the image out. Extra findings `X<n>`.
- `check_records.py`: every id, code counts, n/r sub-records, Arabic in the cited ayah, no repeated
  sentences. `merge.py`: compact `findings.md` (readings with image, reason, branch sense; notes one line;
  cited ayat) + `records_index.md`. `run.py`: discover / write / usage (Codex JSON logs).
- Pilot lesson: inlining brief + context + bundle in the prompt (stdin) cut a bundle from 966k to 184k
  input and from 16 to 2 tool steps, and (with the miss rule) turned the 43:36 night path from `-` into a
  reading.

Measured on 29:38 (Luna discovery, 17 sessions): 5.14M input (4.19M cached), 494k output (379k reasoning,
≈115k visible ≈ the records). Largest single request 92k (none near the 272k double-price threshold).
Luna-price cost (V8 COSTS.md rates, $0.20/$1.20; cached assumed 10%): ≈$0.87/ayah ($1.62 without cache
discount); W1 ≈70%. V5 S12 measured: discovery ≈$0.31/ayah, discovery+composition ≈$0.61/ayah.
Records: 627 (274 readings, 285 notes, 68 none). Caught: kohl (ص د د B013), عين قائمة ذاهبة البصر,
43:36 night-blindness → بيت, eye film / web veil, worn road (عمل B011), Ād ↔ ع د د; the four road branches
(عود B009, عمل B011, صدد B004, سبيل B001) all converge on ٱلسَّبِيلِ and ٱلصِّرَٰطَ (1:6) — found separately,
joined only in synthesis. Weakness: generous on inter-ayah (plain-sense "readings").

Writers (inlined: findings_writer + writer_rules + context + findings ≈85k tokens):
- gpt-6-sol: 31 calls, 4.58M input (4.41M cached), 40k output (12k reasoning), peak call 172k; Sol $4/$20
  → ≈$3.2 (cached at 10%), ≈$19 without discount. ~25 of 31 calls were mechanical self-repair
  (verify/validate/python edits/re-reading own file), each re-sending 100–170k.
- gpt-6-luna: 63 calls, 10.69M input (10.24M cached), 178k output (104k reasoning), peak call 243k
  (near the 272k threshold); ≈$0.50 at Luna prices (cached 10%). Prose: concordance essay, weakest.
- Opus 5.5 on the same findings (Claude Code subagent): 32 calls, 5.88M cache read, 594k cache write, peak
  context 341k, ≈$4.3–5; 9,289 words (cold Opus 4,518), 262 of 274 readings used, 22 of 285 notes.
- My assessment (prose): cold Opus > Sol > Luna writer. Sol: best recall of user-flagged items (night
  path, road join) but catalogue rhythm, forced weak links, repeated hedging; missed kohl, عين قائمة,
  grammar/irony insights. Luna writer: lists (history, زين concordance), weakest notes got paragraphs,
  scope errors (27:24 and 41:25 called "in this surah"), missed the night path and kohl.
- Cause (shared): 559 unranked records framed as obligations ("every reading must reach the prose");
  ~80–120 carry the reading (112 of 133 global readings are plain parallels); the pipeline's briefs are
  Opus-shaped (abstract rules) while GPT writers need concrete procedure and examples.

Effort test (one bundle, W1_branches_7 ص د د, single runs — production runs each bundle once): high kept
12 lines vs max 20 (agree on 139/150), ≈1/3 the tokens; dropped 5 weak links (ṣayḥa noise path, ifk,
bridge, mirror-water, veil-janna) but also 3 valuable ones (Fātiḥa ٱهْدِنَا → road-to-water; kohl →
إنسان العين pupil image; أَنْعَمْتَ → eye-joy) and upgraded 2 weak أولياء lines; demoted prayer تنهى ↔ صدّ.
Reading: max's extra is mostly notes; fix over-finding at ranking, not effort. xhigh test running.

### Next iteration (agreed with the user; build after the comparison)
- **Push, then script pass, then grep-based repair.** The first session (Luna judge or writer) gets everything pushed and returns its
  output as the final message (one call). The runner writes files, runs the mechanical fixers
  (`verify_ar.py --fix`, `validate_prose.py`, `check_records.py`), and sends only residual problems to a
  FRESH small repair session that greps the same content (worklist items by id, findings, package, Quran
  via scripts) instead of resuming the big session. Guards: readings — only flagged lines may change
  (diff check), unmatched quotes corrected from source, never dropped; records — codes never downgraded
  from r/n to -, coded lines never lose their record; judgement questions go back to the original session.
  Expected: Sol writer ≈0.2M input (≈$1.3), Luna discovery ≈0.8–1.0M input.
- **Shared-trigger index** in `merge.py` (pushed to the writer): triggers hit by records from ≥2 roots,
  with their records (e.g. ٱلسَّبِيلِ, ٱلصِّرَٰطَ). Writer brief: each cluster → a thread or an explicit join.
- Harvest: writer lists only used records (section) and rejected readings (reason); `records_index.md`
  covers the rest mechanically.
- Worklist: print a code template per item (`lines: ________ (16)`) to cut count errors.
- Luna records get a strength field (1–3) set at judging time.
- `merge.py` builds the writer input as ranked clusters: 8–12 threads from shared triggers/images; core =
  strength ≥2 readings + HFT + X + 15–25 representative global parallels; reserve (notes, strength 1, other
  parallels) pullable by id, not pushed.
- Recall checklist for 29:38 (script over any reading): night path, kohl, عين قائمة, eye film, worn road,
  road ↔ ṣirāṭ join, Ād/ع د د, 29:40 accusative resolution, تَبَيَّنَ/زَيَّنَ, zayn/shayn, 8:48 "I see
  what you do not see".
- Drop the Luna writer. Writer choice after review: Opus on findings vs Sol with a GPT-specific brief
  (explicit procedure: cluster → thesis → supporting records → write → drop images that do not meet the
  thesis, never hedge; one non-overfitting example paragraph from outside 29:38).
- W0 dictionary-only Luna bundle (user, 2026-09-24: cold Luna given dictionary entries performs better;
  balance script-generated pairs with the entries alone): Luna gets context (ayah, Fatiha, surah) + the full
  01_dictionary of all focus roots, no pairs; open discovery (cross-root contrasts/images, sound play,
  grammar that changes meaning, rare branches the ayah/surah calls) → X records. Compare which findings
  came only from W0 vs only from scripted pairs to set the balance.
- GPT briefs (Luna judge and Sol writer) must counter GPT conservatism explicitly: this is
  hypothesis-generating discovery prose — propose and develop bold readings when both keys hold, do not
  retreat to the safe plain sense, do not hedge a reading you keep (user, 2026-09-24).
- Test the selective framing ("most of this is noise; choose what carries the reading") with Sol and Luna
  writers again, on the ranked input (user, 2026-09-24).
- Verify: rerun 29:38 end to end (recall checklist, prose ≥ best so far, no call >~150k, token report),
  then a second, longer ayah from another surah.

### Opus 5.5 review of the four readings and the plan (2026-09-24 night)
Rank / checklist (14 items): cold Opus 12.5 > Opus-on-findings 10.5 > Sol 6.5 > Luna writer 4.
- Opus-on-findings: widest recall of Luna items (night path, kohl, eye film, roads ↔ ṣirāṭ, 8:48, صدّ ↔
  تنهى) + new finds (29:37 repeats Thamūd's formula 7:78/11:67; خسف = sunken eye; 3:99 عوجا ↔ شطن) but
  ~43% of words in 11 catalogue paragraphs (8–20 citations each).
- Sol and Luna writers actively REJECTED kohl / night path on literal grounds ("no mirror named", "no
  night cue") — writer re-judging undoes Luna's miss rule. Luna writer also has scope/attribution errors.
- CORRECTION to "Caught" above: عين قائمة is coded `-` in most places and survives only as note
  R08.B010.12; road-to-water (صدد B004) only notes; zayn/shayn serpent only a note; night sense of سكن a
  note. merge.py printed notes as one line without dictionary source phrase, so writers never saw them.
- Missing everywhere: the Fatiha eye cluster vs مستبصرين (ٱلْمُسْتَقِيمَ ق و م B021, أَنْعَمْتَ ن ع م
  B013, ٱلْمَغْضُوبِ غ ض ب B006, خسف eye sunk); "sees by day, not at night" vs 29:37 فَأَصْبَحُوا; kohl →
  إنسان العين via 29:43; عود B004 habit ↔ الدين (1:4) habit road; deep well in two roots (ب ي ن B006 بئر
  بائنة, ش ط ن B001 بئر شطون); ب ي ن B012 irrevocable divorce vs عاد "return"; 17:59 ثمود الناقة مبصرة —
  not in the package at all (no same-people × focus-root index).
- Plan risks: a Luna-set strength field + pull-only reserve would bury exactly the rare, low-confidence
  finds the user values. Rank on latency (rare branch vs plain restatement) × key strength; push all
  rare-branch notes compactly with their Arabic source phrase; collapse plain global parallels (112/133)
  into formula clusters; cluster by image as well as trigger.
- Remove writer re-judging ("verify every record … drop"): scripts verify Arabic; the writer rejects only
  for a stated factual error.
- Grammar/rhetoric insights (accusatives, لكم/لهم, تبين/زين, الزين نقيض الشين) come only from an
  ayah-internal pass: give the writer 00_ayah + focus roots' dictionary (source phrases) and require it.
- Replace "every reading must reach the prose" with "every cluster reaches the prose via representatives";
  add a catalogue detector (paragraphs with ≥8 citations), mechanical harvest (script maps tags to ids;
  writer lists only rejections), W3 formula clustering before Luna judges, same-people × focus-root index.
- Recommended: Luna (max) → merge clusters → Opus writer, one pushed call (~130–150k in, 30–40k out,
  estimated ≈$1.4–1.6) → script pass → fresh repair. ≈$2–2.7/ayah API-equivalent (estimate).
- Repair guards to add: a repair may fix the citation, not only the quote; diff-log verify_ar --fix
  rewrites; set output format/size for final-message outputs (Codex final-message length unverified).

## Pipeline v3 (built 2026-09-24 night; one command per ayah)

`python3 _commentary/v9/luna/run.py ayah S:A [--writer opus] [--writer gpt-6-sol]` runs every stage and
skips work already done: package (prepare.py, now with `11_people.md`) → worklists (archived and rebuilt
when the package changes) → Luna discovery (pushed prompt, records as final message, script check, fresh
guarded repair) → merge → writer(s) (Opus via headless Claude Code `claude -p`; GPT via Codex, output as
final message) → checks (verify_ar --fix, validate_prose, check_reading) → fresh guarded repair → usage.
Outputs: `output/sSSS/S_A/<writer>/`. `run.py usage S:A` reports tokens (Codex events + Claude JSON).

Changes in this build (from the Opus review and the user):
- Generic only: no 29:38 images or examples in any brief; no image lexicon; agents decide what joins.
- `11_people.md`: every other ayah naming the focus ayah's proper nouns (no filter; shared focus roots shown
  as a hint). 29:38: 115 ayat, 55 new → P items in W3.
- W0 dictionary-only bundle: all focus roots' full entries, no pairs; D items + X records (balance with
  scripted pairs; compare what only W0 finds).
- Luna brief: hypothesis-generating discovery, bold; generic miss rule; records returned as final message;
  `luna_repair.md` for fresh repair sessions (never downgrade or delete a finding).
- Worklists print a `codes:` template per item.
- merge.py: every kept record pushed (no reserve): ayah-level findings with reason (readings) and
  dictionary sense incl. Arabic source phrase (readings and notes); whole-Quran parallels compact; shared
  triggers across roots; cited ayat. 29:38 (old records): 92.6k tokens.
- Writer brief: reads 01_dictionary itself and starts from the ayah; Luna's material is support, the writer
  chooses; rejects only for a stated factual error; short harvest (sections → ids, rejections).
  `findings_writer_gpt.md`: bold, no hedging, explicit work order, output as final message.
- `check_reading.py`: catalogue report (paragraphs citing ≥10 ayat; report only) + automatic harvest.
- Kept outside the pipeline: the 29:38 recall checklist (a test, never shown to agents).

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
