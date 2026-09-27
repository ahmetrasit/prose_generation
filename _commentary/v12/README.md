# Commentary v12 — the existing chains in, Opus goes beyond them, fully automated

Target: `NORTH_STAR.md` (the reader; al-Khūlī + al-Biqāʿī + the Quran explaining the Quran; three layers; readings
explained and connected, never catalogued; checkable; no invention). v12 keeps V11's writer (one fresh Opus call
per ayah, a Turkish findings ledger, then the reading) and changes what it is given and what it is asked.

## What changed from V11, and why

| change | why (evidence) |
|---|---|
| **HFT in** (`hft.md`, read from `latent_activation/focus_trace/runs`, 90 surahs; `bundles/` holds only 64): the ayah's own HFT records in full, plus other ayat's records whose trace passes through it; every trace step resolved to its word and branch and **flagged by script** (no such branch / echo root / alternative root / root not the word's), and, where a root dossier exists, marked with the word's plain-reading branch and usage group | The image chains are already discovered (HFT, 90 surahs). V11 left HFT out (input size vs thinking, one test on 4:34), so its surah pass and the arm-S seed pass rediscovered it ($1.64 for S1; the seed sheet's members were ~all in HFT/channels). The seed pass also found broken HFT traces by hand; the script now flags them for every ayah. |
| **Channel review in** (`channels.md`): the surah's chain map (quran-data network-v3 review, 110 surahs), index + the sub-channels anchored in this ayah | Same: the map exists (S1's has the road, herd, water camp, even the well and pulley the seed pass missed). |
| **Neighbours' branches** (`neighbours.md`): every branch of the other roots of the surah (≤ 40 ayat) or of the ayah ± 7 | The gold findings V11 missed were cross-ayah coalitions (a member branch belongs to another ayah's root); new junctions (e.g. a sense of one ayah's word completing a scene in another) need both sides visible. |
| **Root dossiers** (`usage.md`, from `_projects/root-dossier`): a descriptive concordance — every occurrence of each root grouped by the context the ayat state, each group with its plain-reading branch; this ayah's group marked; ≤ 2 KB per root, ≤ 10 KB per ayah; `digest_v2.md`'s usage block for those roots becomes a pointer; `--no-usage` turns it off | al-Khūlī's *istiqrāʾ*: how the Quran uses a word everywhere, beyond the dictionary. V11's digest omits the occurrences of common forms ("common form, not listed"); a per-ayah agent cannot survey 100+ occurrences and repeats the survey for every ayah. The dossier only describes; the writer interprets. |
| **Brief** (`prompts/write.md`): the chains are known — ground, correct, connect, **go beyond**; the word through the Quran; ledger families `Usage`, `Chains` (each known chain through this ayah: holds / corrected / does not hold) and `New` (what the map lacked); a chain is developed where this ayah is its turning point, otherwise a clause or nothing; Turkish loss; the plain sense first | North star: layer 2 discloses mature chains through the word; the S100 run retold the raid in every ayah; the surprise must be connected, not catalogued; Opus should interpret, not only consolidate. |
| **Surah pass** (`prompts/surah.md`): plain walk → purpose → one section per core chain with explicit provenance → where the chains meet → develop chains → purpose and next surah; reads channels, HFT (compact), the branch table, every ledger | V11's S1 surah reading was 1,124 words of grammar chains; the user could not follow "what comes from where"; chains must interact, not sit in silos. |
| **Automation**: every step checks itself; commas, wrong sources (the quote occurs in exactly one place) and exact forms are fixed by script; the rest goes to a small repair call for the affected paragraphs (2 rounds); a tag that still cannot be verified becomes its gloss in plain Turkish (counted in `check.txt`); a call starts only when its estimate is below $5 and is never retried; `status.json` per ayah (estimate, cost, repair cost); a lock so a running write is never restarted | The orchestrator only reads `RUNBOOK.md` and starts/stops runs; nothing waits for hand fixes. |

No test surah's material appears in the briefs (their examples are 24:35, ن و ر B005, 2:255 …): S1, S29, S100 and
18:86 are test cases.

## Inputs per ayah (measured; Arabic ≈ 1 token per byte through `claude -p`)

| ayah | context | dictionary | digest v2 | hft | channels | neighbours | total |
|---|---|---|---|---|---|---|---|
| 1:7 | 6 KB | 34 KB | 29 KB | 47 KB | 39 KB | 20 KB | 176 KB |
| 100:1 | 3 KB | 33 KB | 14 KB | 28 KB | 18 KB | 28 KB | 123 KB |
| 29:45 | 27 KB | 124 KB | 54 KB | 28 KB | 14 KB | 91 KB | 337 KB |
| 18:86 | 38 KB | 148 KB | 32 KB | 26 KB | 13 KB | 75 KB | 332 KB |

V11 gave 88 KB (1:7) and 233 KB (18:86). The S1 surah pass gets ≈ 265 KB (channels 48, HFT 46, branch table 55,
seven ledgers). **Risk: input dilutes thinking** (V11's single 4:34 measurement). `check.txt` logs input bytes and
output tokens per ayah so the effect is measured, not assumed; knobs: `inputs.SPAN` (neighbours ± ayat in long
surahs), the HFT clips, dropping `channels.md` or `neighbours.md` for an arm.

**Cost (tests, `claude -p`, effort high):** estimated $2.7 (1:7) to $4.0 (29:45) per ayah at 1 token per byte (input
$8/M as a 1-hour cache write, output $20/M, both matching V11's 100:7 bill exactly); V11's 100:7 billed ≈ 0.6 tokens
per byte, so these are upper bounds until `run.py --estimate` calibrates on real calls; surah pass ≈ $3 for S1. Production (Messages API batch, shared cached surah
prefix) is expected at well under half of this (V11 README "Production").

## Commands (the orchestrator's procedure is `RUNBOOK.md`)

```
python3 _commentary/v12/inputs.py 29:45                  # evidence only (no model), prints sizes
python3 _commentary/v12/run.py ayah 29:39,29:41,29:45 --estimate   # cost estimate per ayah (no model)
python3 _commentary/v12/run.py ayah 29:39,29:41,29:45 --parallel 3
python3 _commentary/v12/run.py surah 1 --parallel 7      # every ayah, then the surah pass
python3 _commentary/v12/run.py chains 1                  # the surah pass alone (long surahs: per passage window)
python3 _commentary/v12/run.py status 1
```

Outputs: `out/sNNN/S_A/` (`S_A.reading.tr.md`, `S_A.ledger.md`, `S_A.md` = reading + Kur'an'ı Kur'an'la + Kur'an'da
bu kelimeler + Kelimeler ve okuyuşlar + Surenin bütününde, `check.txt`, `status.json`, `run.log.jsonl`),
`out/sNNN/surah/<window>/` (`chains.md`, `S.surah.tr.md`, `ayat.md`, `check.txt`). Evidence: `work/sNNN/S_A/`.

## Test plan (each run needs the user's go)

1. **Root-dossier micro run, then pilot** (`_projects/root-dossier`, Luna, run by the user): micro list with and without
   word analysis, scored by `eval/score_dossiers.py`; then the roots of 1:1–7, 18:86, 29:39, 29:41, 29:45 and their words' minor roots (54).
2. **S29 probe**: `run.py ayah 29:39,29:41,29:45` (estimate ≈ $11), with usage.md on and off (`--no-usage --tag
   nousage`). The pass criterion is in `eval/known_answers.md` (never a model input). Also compare `New` lines and
   output tokens with V11-style runs.
3. **S1**: `run.py surah 1` (≈ $21 + surah pass ≈ $3). Then an Opus judge and the user's blind read of 1:4, 1:6, 1:7
   and the surah reading against V11 and v5 (`_commentary/v11/eval/s001_anchors.md` as the regression guard).
4. **S100** (the horses becoming the surah's argument) if S1 passes.
