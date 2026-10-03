# Stage 2 — meal: Turkish translation review

You judge how Turkish translations carry this surah, word by word, against the Arabic. Two questions decide the
reader's page: which meal conveys the meaning best (per strategy), and what the meals lose in common.

## Inputs
PACK/ayah/S_A/words.md (every word's morphemes and the elements a faithful translation must carry: prepositions,
attached pronouns, number, definiteness, voice, emphasis, conjunctions); PACK/ayah/S_A/meals.md (the 16-meal panel,
the relay pair Asad EN → Esed TR, Arberry as a literal English control, the reference set); PACK dictionary.md,
usage.md, roots/; `corpus.py get MEAL-X:S:A` for any meal at any ayah of the Qur'an.
Panel lineage: MEAL-DIB, MEAL-TDV and MEAL-KURANYOLU share one lineage (diyanet): their agreement counts as one
witness. MEAL-ESED is translated from Asad's English (relay ASAD-EN), not from the Arabic.

## Step 1. Expected elements (no judgement yet)
For each ayah and each content word, list from words.md what must be carried: the concept (from the dictionary
and the tafsir range), and each grammatical element. Mark what Turkish cannot carry naturally (e.g. the Arabic
definite article) as "imposed by Turkish": no translator is blamed for it.

## Step 2. Alignment table (meal_table.json)
For every panel meal, every ayah: the Turkish words that render each Arabic word (or "—" if nothing does), and
for each expected element: kept | dropped | substituted | added (an addition the Arabic does not have; note whether
it is marked by brackets/parentheses). Keep the translator's brackets exactly. Merged verse groups: align the group
text to the group's words; say so.

## Step 3. Losses and gains
Type each finding with the schema `kayip` values:
- kelime: a different concept (e.g. ṣudūr → "kalp": ṣadr is the chest, qalb the heart; 22:46 "al-qulūb allatī
  fī ṣ-ṣudūr" is the test where a translator who maps ṣadr to kalp must write "kalplerdeki kalpler" or change the
  verse — check it with `corpus.py get MEAL-X:22:46` for any term where this pattern matters);
- eleman: a preposition, pronoun ("their" in -leri), number, emphasis, conjunction or voice that natural Turkish
  could have kept and the meal dropped (kalplerde vs kalplerinde: the first drops "their");
- aralik: several live senses narrowed to one (from the tafsir range and the dictionary branches);
- ekleme: the translator's own words presented as text (unmarked); marked additions are not a loss;
- kayma: a loanword whose Turkish sense has shifted (namaz, din, ibadet, âlem) — the Turkish-history evidence
  (NISANYAN, KUBBEALTI, TARAMA, TDK, TDVIA term articles) goes to anlam_tarihi; here only its effect on the meal;
- isaretleme: brackets, italics or notes changed so an addition no longer looks like one;
- aktarma: relay drift — for MEAL-ESED compare with ASAD-EN (kiyas:ara_metin) as well as with the Arabic
  (kiyas:arapca); a relay step can lose against one pole and gain against the other (yon:kayip / yon:kazanc);
  likewise MEAL-TEFHIM (from Mawdudi's Urdu) and MEAL-FIZILAL (from Quṭb's paraphrase) when used.
Judge patterns, not slips: for each translator and each key term, check its renderings across the term's other
occurrences (usage.md lists them) before calling a choice a habit. Separate an outright error from a defensible
narrowing, with the ground (Arabic, dictionary, early authorities). Use ARBERRY to tell Turkish-specific loss from
loss any translation would suffer.

## Step 4. Verdicts (meal_review.json)
{"terms":[{"terim":…, "ayet":…, "expected":…, "renderings":{MEAL-ID: "…"}, "findings":[{"mutercim":…, "kayip":[…],
 "yon":…, "kiyas":…, "ground":…, "kaynak":[…]}]}],
 "shared_losses":[{"terim":…, "what all (or nearly all) panel meals lose", "exceptions":[…]}],
 "best":{"literal":{"id":…, "why":…}, "explanatory":{"id":…, "why":…}, "by_criterion":{"primary_sense":…,
 "range_kept":…, "additions_marked":…, "turkish_drift":…}}, "relay":[…], "gaps":[…]}
Verdicts are per surah. Never declare a single best meal overall; name the best literal and the best explanatory
meal and the best per criterion, each with its reason.

## Step 5. Blocks (annotations.meal.jsonl)
Write meal blocks as schema records (tur:meal; required mutercim, terim, kayip; yon and kiyas where relevant; kaynak
lists the meal locators and the Arabic-side evidence; capa = the exact base sentence the term is discussed in, if
any). One block per shared loss (mutercim:"ortak"), one per significant translator-specific finding, one surah
verdict block (islev:sonuc) on the ayah where the decisive term stands. Use ids S<sss>-MEL-NNN. Respect the word
limits. Short quotations of meals only.

## Finish
Write meal_table.json, meal_review.json, annotations.meal.jsonl into your stage directory. Run
`python3 enrichment/v2/validate.py --surah N --annotations <your annotations.meal.jsonl> --out /nonexistent` and fix
every error. Final message: the shared losses, the best literal/explanatory meals with one-line reasons, the relay
findings, and gaps.
