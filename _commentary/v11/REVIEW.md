# V11 review: what the ultimate reading needs, and how to get there from here

Reviewer: Opus (senior-review pass, 2026-09-26). No model pipeline was run for this review. The only things run
were local scripts: greps, byte and token counts, a QAC co-occurrence prototype and a dictionary cross-link
prototype. No existing file was changed.

## 0. Verdict in one page

1. **v11 is the best prose and the best Quran-explains-Quran engine the project has produced.** It is also
   **structurally unable to produce the gold's signature finding.** That finding is a coalition of non-primary
   branches drawn from the roots of *different* ayat: the traveller's road, the herd, the water system. The
   evidence:
   - The ayah writer sees only its own roots' dictionary.
   - The writer judges each branch alone and grades the inert-looking ones `note`, or skips them.
   - The chains pass sees only ledgers, and its brief forbids "dictionary senses the ledgers do not record".

   On the 26 eligible gold items (`quran-slm/reports/s1_ar3_v1_gold_ledger.jsonl`), v11 **develops 11**, gets 4
   partly, keeps 2 in the ledger only, and **misses 9**. Every miss needs a non-primary branch that lives in, or
   pairs with, *another* ayah (§2.1). v5 contains the ingredients of nearly all 26. It then refuses to assemble
   them. In 1:6 it writes: "Hayvan toplulukları ayrı sözlük örnekleri olarak kalır, tek gerçek sürüye
   birleştirilmez."
2. **The earlier verdict in `compare_s001_v5.md` has to be reversed on one point.** It says that "v5 finds [water
   systems, rain cycles, …] that v11 rightly drops". Measured against the north star, that is wrong. The water
   system and the traveller's prayer are the user's own examples of the "aha".
   - Most of their members are **identity-root** branches: ر ب ب B013, ع ل م B002/B005, م ل ك B006/B007/B008,
     ع ب د B005, ق و م B012, غ ي ر B001. None of these is a sound-alike.
   - Some are attested in words that name the traveller directly. Maqāyīs: «والملك الماء يكون مع المسافر لأنه إذا
     كان معه ملك أمره». Tahdhīb, for غ ي ر: «حط عنه رحله وأصلح من شأنه».
   - v11 did not drop these after judging them. Its architecture never put them side by side.
3. **The digest diagnosis is confirmed.**
   - Related passages are 78–93% of each S1 digest.
   - Every inter-ayah row carries a one-line reason, and some rows are typed `counterevidence`.
   - All 19 refs from the diagnosis are in the rows, with notes, e.g. 1:4→57:15 "refusal of ransom adds the
     irreversibility of final consequence".

   Fix it: ref + one-line reason + a counter flag, with no Arabic opening and no rows judged only "no value". This
   is cheap and necessary, but it is the *smaller* gain.
4. **The larger gain is architectural: a surah-level seed pass before the ayah writers.**
   - One Opus call reads the whole-surah branch table. For S1 that is 193 branches, 64 KB. It also reads the
     HFT hypotheses where they exist (90 surahs / 3,133 ayat), a scripted list of "Quran stages this scene on its
     surface" windows, and the dictionary's own cross-root definitions.
   - It writes a seed sheet of latent image systems.
   - Each ayah writer then gets the seeds that touch its words.
   - The chains pass gets the seeds and the branch table and may cite any branch in it.

   This is the only change that attacks the 9 misses. It is also what the user's layers ask for: layer 2
   discloses mature layer-3 channels.
5. **Pushbacks:**
   - The ledger is **not** a meaningful cost item. It is about 4–6.5k output tokens, ≈ $0.08–0.13 per ayah, 6–9%
     of the call. It carries recall, the chains pass and the published Quran-by-Quran chapter. Keep it, and add
     paragraph pointers by script.
   - A **Luna editorial pass on Opus prose is the wrong shape.** It is synthesis by the weaker writer, and it
     can only attach material to themes that already exist, whereas the misses are themes that never formed. Use
     Luna as a *miner before* Opus, and as an *auditor after* Opus, with Opus doing any rewrite.
   - "More input is fine" collides with the project's own measurement: the full package cut 4:34 thinking from
     45k to 9k tokens and anchors from 8 to 5. Add seeds, not packages.
6. **Something none of the three versions found.** The Quran itself stages the Fatiha's latent traveller, herd and
   water system on its surface.
   - **28:21–24.** Mūsā flees, asks «عَسَىٰ رَبِّىٓ أَن يَهْدِيَنِى سَوَآءَ ٱلسَّبِيلِ» ("the middle of the
     road", which is exactly what م ل ك B006 names), arrives at «مَآءَ مَدْيَنَ», finds shepherds (ٱلرِّعَآءُ)
     watering flocks, and ends «رَبِّ إِنِّى لِمَآ أَنزَلْتَ إِلَىَّ مِنْ خَيْرٍۢ فَقِيرٌۭ».
   - **16:5–16.** Livestock carry loads «إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ» and the verse closes «إِنَّ
     رَبَّكُمْ لَرَءُوفٌۭ رَّحِيمٌۭ»; then «قَصْدُ ٱلسَّبِيلِ وَمِنْهَا جَآئِرٌۭ»; water and pasture
     (تُسِيمُونَ); roads «لَّعَلَّكُمْ تَهْتَدُونَ»; and «وَعَلَٰمَٰتٍۢ» (ع ل م!).
   - **20:49–54.** «رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ», then «لَّا يَضِلُّ رَبِّى وَلَا
     يَنسَى» (ض ل ل right beside forgetting, the gold's G027 branch that v11 dismissed as "işlek değil"), then
     roads, water, and «كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ».

   None of the three versions reads these as whole passages. v11 cites 28:22 and 20:49–50, but not the water,
   the shepherds or the livestock that follow. A 30-line QAC script found all three (§2.5). This is what "the Quran explains the Quran", applied to *latent
   images*, looks like. It is the checkability guardrail and the "aha" in the same move.

---

## 1. The target: al-Khūlī, al-Biqāʿī and Quran-by-Quran, with this dictionary and agents

### 1.1 What each tradition would do today

**al-Khūlī / Bint al-Shāṭiʾ (al-tafsīr al-bayānī).** The method has four parts:
- *istiqrāʾ*: every Quranic occurrence of a word, read in its context;
- the word's concrete, sensory base (*al-aṣl al-ḥissī*) and how its abstract uses grew from it;
- no two Quranic words are exact synonyms (*furūq*);
- nothing imported that the text does not support.

Bint al-Shāṭiʾ could do this exhaustively for a few dozen words. With this dictionary and agents, every word of
every ayah gets a full **word dossier**:
- every attested branch with its classical phrase;
- every Quranic occurrence, and which branch is live in it;
- the near-synonym contrasts: ṣirāṭ / sabīl / ṭarīq; ḥamd / shukr / madḥ; ḍalāl / ghayy; ġaḍab / sukhṭ. The
  dictionary's `not:` field already holds many of these;
- for this reader, **what the Turkish loanword lost**: âlem, ibadet, din, nimet, hidayet, dalâlet, gazap, and
  *sırat*, which a Turkish reader hears as *sırat köprüsü*.

The dossier is not the reading. It is what makes every surprise *checkable*.

**al-Biqāʿī (Naẓm al-durar).** Every surah has a *maqṣūd*, and each ayah's place is explained by its *munāsaba*
to three things: its neighbours, the surah's purpose, and the surah's opening and closing. The surah's end also
meets the next surah's start: *ihdinā* is answered by «هُدًۭى لِّلْمُتَّقِينَ» in 2:2.

Today the *naẓm* can be read at the branch level: which latent images pass from word to word through a surah.
No classical *munāsaba* writer could do this systematically. It is the project's own discovery (the HFT image
chains) and exactly what the gold does. Biqāʿī with agents produces an explicit relation graph:
- ayah to neighbour;
- ayah to *maqṣūd*;
- opening to closing;
- surah to surah;
- **latent branch to latent branch**.

**Quran-explains-Quran (Ibn Kathīr's principle, al-Shinqīṭī's *Aḍwāʾ al-bayān*).** For every phrase, find the
places where the Quran:
- specifies it (*bayān al-mujmal*): «ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ» → 4:69;
- limits it (*taqyīd*, *takhṣīṣ*);
- or appears to contradict it (*dafʿ īhām al-iḍṭirāb*).

Agents make this exhaustive by word form, root and **concept**, where the inter-ayah network with its notes
already does the retrieval. They also make it possible along a fourth axis: **where does the Quran stage on its
surface a scene that a surah carries only latently?** That is §2.5.

### 1.2 The combined target, stated for this reader

An *ultimate* explanation would give each ayah a reading in which **every surprise is**:
- lexically grounded: a branch plus its classical phrase, one hover away through the `source` field;
- placed in the surah's naẓm: which chain it belongs to and what role it plays there;
- checked by the Quran's own usage: phrase, concept, counter-verse, and surface staging of the latent image;
- delivered through what the Turkish word loses.

Canonical meaning is the floor, not the measure. Readings coexist and each contains the primary reading. The
surah reading then does what no single ayah can, chain by chain with visible provenance: S100's horses becoming
the argument; the Fatiha as a traveller's prayer, with its road signs, the road's middle, the trodden road, the
swallowing *ṣirāṭ*, and the stray whose *rabb* is unknown.

### 1.3 How far each existing output is from this

| dimension | gold (`s1-bulgular-tr.md`) | v5 (quran-data prose) | v11 (current) |
|---|---|---|---|
| cross-word branch coalitions (latent naẓm) | **strong**: 5 channels, bold synthesis | ingredients present, **refuses to integrate** (hedges, "ayrı … kalır") | **weak**: only same-ayah coalitions |
| word dossier / sensory base | selective, vivid | broad, abstract | **strong** for focus roots (hamur/el in 1:4, muʿabbad in 1:5, hâdî-değnek in 1:6) |
| QeQ by phrase / formula | almost none (2–3 refs) | broad by concept | **strongest**: 63–90 refs per ayah, exact formula finds |
| counter- and limiting verses | none | **present** (57:15, 6:70, 2:256, 7:186) | mostly missing |
| QeQ for latent images (surface staging) | none | none | none |
| Turkish loanword loss | implicit | occasional | three touches in S1 (din, Rab, besmele); *sırat köprüsü* never addressed |
| grammar / particle naẓm | one item (repeated عليهم) | word-level, dense | **strong** (particles journey, person shift, agentless مغضوب) |
| prose: grounding, not a catalogue | tagged paragraphs (a findings list) | long, abstract, disclaimer-heavy | **best**: concrete, readable, rarely hedged |
| checkability | claims unanchored in text | anchored in apparatus | Arabic verified; source not declared per tag |

The gold is a *findings document*, not a reading. It has no Quran depth, and several of its claims are only as
good as its dictionary scan: its water paragraph is honestly marked "C-koşullu". v5 has the dictionary breadth
but the prose of an auditor. v11 has the reader's prose and the Quran, but not the surah's latent lexicon. The
target is v11's writer, fed what only the whole-surah branch view can see, and checked by the Quran's own
surface.

---

## 2. S1: v11 against the gold and v5

### 2.1 Gold anchors (26 eligible items)

v11 was scored by grep plus reading of the ledgers, readings, `chains.md` and `1.surah.tr.md`. Codes: **Y** =
developed in prose or the surah reading; **P** = partial; **L** = ledger only; **N** = absent. v5 was checked by
term search plus spot reading only. It is an approximation, and the test's judge must confirm it.

| id | gold relation | v11 | why v11 missed (if it did) | v5 |
|---|---|---|---|---|
| G001 | ع ل م way-marks → road request | **Y** (1:2 reading: dağ, taş, sancak → 1:6; 16:16) | — | Y |
| G002 | م ل ك B006 "road's middle" joins the route | **N** | focus branch present in 1:4's dictionary; skipped silently (ledger lists B001–B005, B009) | Y |
| G003 | ع ب د B005 muʿabbad road → ihdinā | **Y** (1:5; chain "boyun eğişin ipliği") | — | Y |
| G004 | رب care + ن ع م livestock (pastoral) | N | partner in 1:7 | P |
| G005 | ه د ي leader + herd | P (1:6: "yaban sürüsünün öncüleri", not tied to anʿām) | partner in 1:7 | Y |
| G006 | هدي sacrificial animals + anʿām | L (1:6 note) | pruned | P |
| G007 | م ل ك B008 lead animal | **N** | skipped; its source phrase «ملك الدابة قوائمها وهاديها» contains ه د ي and ق و م | Y |
| G008 | ḍālla "rabb unknown" ↔ rabb | **Y** (1:7, chain, surah reading) | — | Y |
| G009 | owner ↔ owned (م ل ك / ع ب د / madīn) | **Y** | — | Y |
| G010 | dīn as debt coming due | **Y** (1:4: 24:25, 2:281–282) | — | Y |
| G011 | ق و م dinar / valuation + reckoning | **Y** (1:6: «دينار قائم», 38:22, 1:4) | — | Y |
| G012 | ilāh defined as maʿbūd ↔ naʿbudu | **Y** (1:1, chain) | — | P |
| G013 | ḥamd ↔ anʿamta ring | **Y** (chain "Hamdin halkası") | — | ? |
| G014 | upright ق و م vs ض ل ل buried in earth | P (upright vs 67:22 face-down; burial branch unused) | pruned | Y |
| G015 | rahim softness vs غ ض ب rock / hide | **N** | 1:7 ledger: "ayete taşınması ancak ses rengi olarak mümkündür" | Y |
| G016 | ṣirāṭ swallowing vs ḍalla vanishing | **Y** (1:7 "iki kayboluş") | — | Y |
| G017 | ق و م qiyāma + dīn day | P (83:6, qawma) | — | P |
| G018 | ḥamd "found praiseworthy after trial" + route | P (1:2: land found good to settle) | route partner not joined | Y |
| G019 | ن ع م agreeable halt + route | **Y** (1:7) | — | Y |
| G020 | ن ع م going on foot + route | **Y** (1:7) | — | Y |
| G021 | هدية gift ↔ niʿma | L | pruned | Y |
| G022 | ربيب foster child ↔ rahim kinship | N | cross-ayah (1:2 × 1:1/1:3) | Y |
| G023 | six-root water coalition | **N** | cross-ayah; never assembled | Y |
| G024 | ع ب د B008 anger ↔ ġaḍab | N | cross-ayah; note that the ع ب د B008 source phrase itself contains الغضب | P |
| G025 | غ ي ر B001 mīra / watering ↔ niʿma | N | *same ayah*, pruned as a function word | Y |
| G026 | ع و ن wild-ass herd | N | cross-ayah | Y |

**v11: 11 Y, 4 P, 2 L, 9 N.** The misses are the gold's herd channel (G004–G007, G026), its water channel (G023,
G025), its texture axis (G015), its kinship pair (G022) and the "shadow" item (G024).

**How the misses split:**
- **Architecture (7 of 9):** a member branch belongs to another ayah's root, and neither the writer nor the
  chains pass can see it.
- **Instruction, or pruning in isolation (2 of 9, plus the L and P items):** the ingredient was in the writer's
  own dictionary, and was graded `note` or skipped: G002, G025; also G006, G015's rock, and G027's forgetting.

This is exactly the failure `latent_activation/main goal.txt` warned about: "the real risk is premature pruning
… each initial clue looks weak in isolation." v11's brief invites isolated judgement ("attested senses and images
that change, ground or complicate a reading"), and v9's two-key rule turns "branch alone" into "harvest note". For
cross-ayah coalitions the second key sits in another ayah, which the writer never sees.

### 2.2 What v11 does materially better than both gold and v5

These are real "aha" readings. They are grounded, contained, and new to both benchmarks:
- **1:1.** The rasm of بِسْمِ (the alif drops only where the verb is unsaid: 11:41, 27:30, against 96:1, 56:74).
- **1:1.** 27:30–31: the letter raises a name, then asks «أَلَّا تَعْلُوا۟ عَلَىَّ». The lexicon derives ism from
  ʿuluww.
- **1:1.** The ark as the shape of mercy (11:41–43).
- **1:1.** Raḥmān is never used of anyone else; raḥīm is shared with the Prophet (9:128).
- **1:4.** «يَوْمَ لَا تَمْلِكُ نَفْسٌۭ لِّنَفْسٍۢ شَيْـًۭٔا» (82:19) as the Quran's own definition of the day whose
  *mālik* is named. Also «غَيْرَ مَدِينِينَ» glossed «غير مملوكين» (56:86).
- **1:6.** 7:16: Iblīs sits on «صِرَٰطَكَ ٱلْمُسْتَقِيمَ». 38:22: «وَٱهْدِنَآ إِلَىٰ سَوَآءِ ٱلصِّرَٰطِ» in a
  courtroom. The istiqāma definition «إذا انقاد واستمرت طريقته» makes being guided and being upright one motion.
- **1:7.** One man says both «أَنْعَمْتَ عَلَىَّ» (28:17) and «وَأَنَا۠ مِنَ ٱلضَّآلِّينَ» (26:20). 6:77 gives the
  Fatiha's skeleton in Ibrāhīm's mouth. 15:56: ḍāllūn as the ones who despair of mercy. 20:81: ġaḍab "descends"
  and the one it falls on «هَوَىٰ».
- **Surah level.** The particles journey (bi- → li- → iyyā- → ʿalā → none), the person shift after mālik, and
  the ring of ḥamd with the saved (7:43, 10:10).

This is Biqāʿī's syntactic naẓm plus QeQ at a level neither the gold nor v5 reaches. **Any new arm must keep
it.** The main regression risk of every recommendation below is losing this, so the test counts it.

### 2.3 What v11 misses, by type

1. **The traveller's prayer as a whole.** v11 has ʿālamīn way-marks → ihdinā (1:2), the muʿabbad road (1:5), the
   swallowing ṣirāṭ (1:6/1:7), the agreeable halt and going on foot (1:7), and the lost camel (1:7). It never has
   mālik as the road's middle or the lead animal. No chain or surah paragraph assembles the axis. The surah
   reading's road section is about kulluk = yol (36:61) and the balance.
2. **The water system.** Absent. The words are all in the dictionary:
   - ر ب ب B013 ماء ربب;
   - ع ل م B005 عيلم;
   - م ل ك B007 «الماء يكون مع المسافر»;
   - ق و م B012 «القامة البكرة بأداتها» (the pulley is attested; the gold did not invent it);
   - غ ي ر B001 «غارهم الله بالغيث … سقاهم»;
   - و س م B003 first rain.
3. **The herd channel** (see G004–G007, G026).
4. **Counter- and limiting verses.** Also missing: 57:15 / 6:70 against the dīn-as-debt reading, 2:256, and
   7:186 / 18:17 against ḍāllīn as purely self-caused. v11's 1:7 even states "ed-dâllîn etken … kişinin kendi
   hareketi", which 7:186 «مَن يُضْلِلِ ٱللَّهُ» complicates.
5. **Concept-level Quran search:** mercy in practice (3:159, 30:21), book-of-deeds verses (18:49, 21:47,
   99:7). This is input: the digest dropped the "why".
6. **Layer 1, the Turkish loss.** The brief never mentions loanwords, and the S1 prose touches it three times.
   The gloss error profiles exist (`quran-data/data/translation/glosses/locales/tr/root_*.json`: `loses_facet_ids`,
   `collision`), but they are not in the input.
7. **Biqāʿī's maqṣūd and surah-to-surah link.** 2:2 appears only in a 1:6 ledger line. The surah pass has no
   "purpose" or "next surah" instruction.

**Attribution:**
- items 1–3: architecture, plus instruction for the in-dictionary cases;
- items 4–5: input (digest);
- item 6: input plus instruction;
- item 7: instruction.

### 2.4 Checks of earlier claims

- **Digest composition:** related passages are 80, 88, 93, 89, 89, 78 and 84% of the 1:1…1:7 digests (bytes).
  Every row in every `09_inter_ayah.md` has a note, so the reasons are free to use.
- **All-"no value" rows:** 38, 27, 17, 15, 10, 21 and 33 rows per ayah. They are safe to drop, in line with
  PRINCIPLES §9: "retain, do not render".
- **`counterevidence` rows exist**, e.g. «from 39:49→1:7 (counterevidence …)». The digest currently erases the
  type.
- **Diagnosis refs:** all found with notes, in 1_3 (3:159, 30:21, 16:64, 17:82, 42:28), 1_4 (57:15, 6:70,
  2:256, 18:49, 21:47, 99:7), 1_5 (36:74, 25:43), 1_6 (2:255, 4:5, 18:17) and 1_7 (7:186, 38:26, 39:49,
  18:17). **Confirmed.**
- **Why the labels were dropped.** `digest.py` says the labels "have suppressed good links before". Keep them
  out of print, then: order by label, show the reason, and flag counter rows.
- **HFT coverage is much wider than NOTES says.** `latent_activation/focus_trace/runs` has HFT readers for
  **90 surahs / 3,133 ayat**:
  - S1, S5, S12–14, S17–19, S22, S24, S29, S31–32, S34–36, S40–42, S44–114.
  - Missing: S2–4, S6–11, S15–16, S20–21, S23, S25–28, S30, S33, S37–39 and S43. Those are mostly the long
    surahs.

  The design must therefore not *depend* on HFT, but HFT seeds are available for about half the Quran.
- **The output cap is removed** (`CLAUDE_CODE_MAX_OUTPUT_TOKENS=128000` in `run.py`). The second turns on
  1:4/1:6/1:7 cost ≈ $0.5 each in re-billed input, so current S1 costs would be ≈ $1.2–1.8 per ayah.
- **Cost anatomy** (from `run.log.jsonl`). `claude -p` bills input at ≈ $8/M (1-hour cache write) and output at
  $20/M. Output is ≈ 84% of cost. For 1:1: 58k output, of which ≈ 11.7k is text and ≈ 46k thinking.

### 2.5 The Quran stages the latent scene: a prototype that found what nobody found

**The prototype.** I tagged QAC stems into 8 surface fields:
- road: سبل, طرق, صرط, سلك;
- guidance: هدي;
- water: موه, مطر, سقي, نهر;
- herd: the lemma أنعام, رعي, سوم;
- rabb: ربب;
- mercy: رحم;
- stray: ضلل;
- sign: عَلَامات.

I then scored every 6-ayah window by the number of fields present. The top windows included **16:5–10, 20:49–54
and 7:48–53** (7 fields), and **28:18–23** among those with 5. The texts are in §0.6. Several of these passages
are, on the surface, the scene the Fatiha carries in its branches:
- *rabb* who guides (هَدَىٰ);
- the traveller asking for the road's *middle* (سَوَآءَ ٱلسَّبِيلِ ↔ م ل ك B006 «ملك الطريق»; and 38:22
  «سَوَآءِ ٱلصِّرَٰطِ»);
- water and shepherds, herds that carry loads to a land otherwise unreachable, *raʾūf raḥīm*;
- deviating roads (جَآئِرٌۭ, 16:9);
- way-marks (عَلَٰمَٰتٍۢ, 16:16);
- a *rabb* who «لَا يَضِلُّ … وَلَا يَنسَى» (20:52).

**Coverage.** None of the three reads any of these as one passage.
- Gold: none of these refs.
- v5: 16:5, 43:10 and 20:50, one at a time.
- v11 has pieces:
  - 16:16, with 16:15 paraphrased, in 1:2;
  - 16:9 in 1:7;
  - 20:49–50 in 1:2 and 1:6, but not 20:52–54;
  - 28:22 in 1:6, but not 28:23–24.

**Why it matters for the north star:**
- **Checkable aha.** The reader is not asked to trust a dictionary scan. The Quran tells the same scene out loud
  elsewhere, and that is exactly how the gold's "water: needs a shuffle test" worry should be answered.
- **It is Quran-by-Quran, not a list of parallels.** A surface passage explains why the latent image is not an
  accident of the lexicon.
- **It costs nothing.** The script is deterministic. The noise (generic "guidance + mercy + rabb" windows) is
  easy for Opus, or for a Luna worklist, to filter.

A second prototype shows the dictionary tying the surah's roots to each other in its own definitions (the gold's
"ring" findings):
- م ل ك B008 «ملك الدابة قوائمها وهاديها» (three Fatiha roots in one phrase);
- ض ل ل B005 «لا يعرف ربها» / «مالك»;
- ع ب د B001 «المملوك»;
- ع ب د B008 «الغضب»;
- ه د ي B005 «النعم»;
- ء ل ه B001 «معبود»;
- ر ب ب B002 «النعمة»;
- ق و م B015 «دينار».

A naive regex matcher is too noisy for weak roots (ي و م hits everything). A proper lemma lookup, or a Luna
per-branch extraction, makes it precise.

---

## 3. Recommended path (ranked)

Costs use the observed rates: input ≈ $8/M through `claude -p`, output $20/M. "Per ayah" includes surah passes
amortised over the surah (S1 = 7 ayat).

### R1. Surah-first seeds: one whole-surah discovery call before the ayah writers *(highest gain)*

**What changes.** These are proposals. Nothing is applied until the user agrees.

1. **`seeds_input.py`** (script, no model) builds `out/sNNN/surah/seeds_input.md` from five parts:
   - (a) The **surah branch table**: every branch of every identity root, one line each: root Bnnn | gloss |
     Arabic image | the first classical phrase. Echo and alternative roots are flagged `~`. S1: 193 branches,
     64 KB ≈ 20k tokens. S100: 217 branches, 71 KB. Long surahs use pericope windows
     (`quran-data/.../network-v3/pericopes/surah_pericopes.jsonl`).
   - (b) **HFT, compacted where it exists:** record name, `after:` and the trace as word → root Bnnn, without
     the English prose. The whole-surah records are the ones with cross-ayah traces, e.g.
     `d_guiding_owner_of_approach` (م ل ك B006/B008 + ه د ي B003 + ṣirāṭ), `c5_worlds_as_navigable_signs`,
     `o1_ecological_water_cycle` and `out_hydrological_way`.
   - (c) **Surface-staging windows:** the §2.5 script, with field lexica per surah generated from its branch
     table, not hand-made.
   - (d) **Definitional cross-root links:** a branch's classical phrase that contains another surah root's word.
   - (e) The `03_pairs.md` near/surah partners, restricted to non-primary branches.
2. **`prompts/seeds.md`** (one Opus call per surah or window) asks for **latent image systems**, not themes:
   - members, as S:A word → root Bnnn → role (source / conduit / guide / obstacle / loss …);
   - the mechanism;
   - a **containment sentence** with the primary reading intact;
   - "what this makes perceptible in the plain reading" (the main-goal test);
   - surface-staging refs;
   - counter- and limiting verses;
   - maturity (mature = role-complete, three or more members, and either surface staging or a definitional link);
   - the per-ayah disclosure note: what this ayah's word contributes, in one or two sentences.

   The prompt's discovery rule is `main goal.txt` almost verbatim: coalition before judgement, no early pruning,
   and a formed image may re-evaluate weak members.
3. **The ayah writer** gets `seeds.md` restricted to its words (≈ 2–4k tokens) and three brief lines:
   - "before grading a branch `note`, check it against the seeds and the other ayat's words";
   - "disclose *mature* seeds through this word's contribution in 1–3 sentences; the surah reading develops the
     whole chain; do not retell it";
   - "seeds are proposals; judge them; no coverage obligation".
4. **The chains pass** gets the seed sheet and the branch table, and may use any tabled branch (source-tagged).
   This replaces "do not introduce dictionary senses the ledgers do not record". It must write one section per
   chain naming its ayat, words and roles (NOTES item 2), plus a Biqāʿī *maqṣūd* paragraph and the link to the
   next surah.

**Expected gain.** This is the only change that can produce G002, G004–G007, G015 and G022–G026, the traveller's
prayer and the water system, in the form the user sketched ("yol imgesi … naʿbudu … ʿālamīn ile birleşerek").
It also turns the surah reading from mostly grammatical chains into image chains with provenance. Target: gold
recall ≥ 22/26 at surah level and ≥ 18/26 in the ayah prose.

**Regression risks and guards.**

| risk | guard |
|---|---|
| Homogenisation: every ayah retells the surah image (already seen in S100's raid) | disclosure rule; judge criterion R6; script counts seed words per reading |
| Anchoring: the writer becomes an accountant (v9 "task drift", 9,289 words and 184 cites) | seeds are proposals; no coverage rule; the judge counts the current v11 finds that are kept |
| Input dilution of thinking (4:34: 45k → 9k) | ayah writers get only 2–4k tokens of seeds, and the branch table goes only to the seed and chains passes; log thinking tokens per arm; if they fall more than 30%, cut |
| Base-rate illusion (the gold's own water caveat) | surface staging and definitional links are maturity criteria; immature seeds stay in the seed sheet and the surah reading's "notes" |
| PRINCIPLES §6 says layer 2 is not written with layer-3 knowledge | the user's own layer design asks for mature channels in layer 2; record this as an explicit user decision that supersedes §6, while the post-ayah chains pass still runs |

**Cost.**
- Seed call: input ≈ 45–55k tokens (≈ $0.4); output ≈ 35–50k, mostly thinking (≈ $0.8–1.0). ≈ $1.3 per surah
  or window.
- Ayah writers: +3k input ≈ +$0.03.
- Chains pass: +30k input ≈ +$0.25.
- S1 total ≈ $1.6 extra ≈ **+$0.23 per ayah**.

### R2. Digest v2: reasons, counter flags, no openings *(cheap, necessary)*

**What changes** (`lines/digest.py`, as a new version):
- related-passage lines become `- S:A — note [counter]`;
- rows ordered strong → medium → weak → unlabelled, **labels not printed**;
- all-"no value" rows dropped;
- the 60-character Arabic opening dropped;
- formula groups keep their shared roots.

Size: ≈ 10–32 KB per S1 ayah, about the same as now.

**Brief:** add a ledger family `### Limits` for counter- and limiting verses. The digest's counter rows seed it,
plus the writer's own knowledge. `render()` must then include "limits" in the Quran-by-Quran chapter.

**Expected gain:**
- recovers v5's concept-level refs (mercy in practice, book-of-deeds) and its counter-verses (57:15, 6:70,
  7:186, 2:256);
- sharpens v11's own bolder analogies (dīn-as-debt, ḍāllīn as self-motion) instead of weakening them.

**Risks and guards:**

| risk | guard |
|---|---|
| English notes carry earlier reviewers' framing | brief: notes are hints; the writer verifies against the Quran it recalls |
| The writer misremembers a ref without the opening | `verify_ar` wrong-ayah check; the note says what the ayah does |

**Cost:** ≈ $0.

### R3. Writer brief deltas beyond R1 and R2

- **Anti-pruning:** the sentence in R1, plus "a branch with no job in this ayah may have one in the surah: say
  so, do not bury it". This fixes G002, G025 and G015's rock.
- **Layer 1:** a small gloss sheet per focus word, from the gloss results: the selected Turkish gloss, fit,
  `loses`, `collision`, ≈ 1–2 KB. Instruction: when the Turkish loanword has drifted (âlem, ibadet, din, nimet,
  hidayet, dalâlet, gazap, sırat), the reading must say, where the word first appears, what the Turkish word
  loses or adds. For example, *sırat* is not first the bridge over hell; *âlem* is not "the world" but each
  "thing by which one knows"; *ibadet* is not only ritual.
- **Biqāʿī:** in the ayah brief, "why this ayah stands here: what the previous ayah leaves open and the next one
  answers". v11 already does this well; make it explicit so it is not sampled away.

**Gain:** layer 1 of the north star becomes systematic. **Risk:** preachy glossary paragraphs. **Guard:** "once,
where the word first carries weight, in one or two sentences". **Cost:** ≈ $0.

### R4. The `source` field and source-checked verification (user decision 3)

**Tag:** `{ar:…, tr:…, gloss:…, source:…}`. The source is S:A, or a root with its branch (`م ل ك B006`). Echo or
alternative roots take a `~` prefix, so the reader is never told an echo is the word's root (`~ع ي ن B006` for the
spring behind *nastaʿīn*). Several sources are comma-delimited.

**Verification** (a new v11 checker; do not edit the frozen v5 validator):
- **S:A source:** the quote must occur, loose-normalised, in that ayah.
- **Branch source:** the quote must occur in that branch's classical phrases, image or definition, from the
  **surah branch table**. Seeds let the prose quote other ayat's roots, so the verify scope must widen from the
  focus package to the surah.
- **Single vocalised words the writer forms itself** (e.g. دَيْن): pass if the consonants match the declared
  root and the branch exists; report as `root-form`.
- **`--fix`** may correct a wrong source when the quote is found in exactly one place.

**Required code changes before any run:**
- `run.py:repair_tags` has regex `gloss:([^{}]*?)\}`. It would swallow `, source:…` into the gloss and
  **silently corrupt every tag**.
- `_commentary/v5/validate_prose.py` rejects unknown field names, so every tag would fail.
- The app's tag parser must parse by field name, not split on commas, because `source` may contain commas. Forbid
  `source:` inside a gloss.

**Gain:** "every unusual claim checkable" becomes mechanical, and the hover links the root to the dictionary.
**Cost:** ≈ 600 output tokens per reading, ≈ $0.01.

### R5. Keep the ledger; make it point, not repeat

**Measured cost.** The S1 ledgers are 12.7–19.7 KB, i.e. ≈ 4.2–6.6k tokens, i.e. **$0.08–0.13 per ayah**. That is
≈ 6–9% of the call. Thinking is ≈ 75–80% of output.

**Value:**
- 4:34 recall was 11 with the ledger against 9 in the prose alone, and the ledger-first order is part of *why*;
- it is the chains pass's only view of each ayah;
- it is the published Quran-by-Quran chapter (`render()`);
- it is what a Luna audit reads.

An inventory kept in thinking is invisible to all of these.

**Recommendation:**
- Keep it in the tests unchanged, so there is one variable less.
- Add **paragraph pointers by script**: map each ledger line to the reading paragraphs that share its refs or
  roots. That costs nothing.
- Later, test a terse ledger (one clause per line; dictionary lines cite `root Bnnn` instead of re-quoting the
  Arabic). This might save ≈ $0.04 per ayah and is not worth a recall risk now.

### R6. Luna: miner before, auditor after, never editor

**The user's idea**, a Luna pass that expands the v11 prose from HFT and network pairs, plus a Luna editorial
insertion, has three problems:
- The material it would attach can only hang on themes Opus already formed. The S1 misses are themes that
  **never formed** (herd, water, road through mālik), so the pass would bolt fragments onto the wrong chains
  ("hesap günü ve yoldaki ayrışma").
- "Luna follows worklists well, synthesises poorly" (v9 DESIGN). Luna and Sol writers *rejected* kohl and the
  night path on literal grounds and made attribution errors. An inserted paragraph or an appendix is the
  catalogue the user rejects.
- It spends Luna tokens to lower the quality of the one layer that is already best.

**Better roles:**

- **R6a. Luna as miner, once and reusable: branch image tagging for the whole dictionary.**
  - For every branch of every root, Luna records the concrete object or scene (well, pulley, halt, lead animal,
    trodden road, rock, hide …), its image fields (water / road / herd / body / texture / light …), and the other
    roots named in its classical phrase.
  - This is the "per-item, specific, checkable fields" worklist that v9 found Luna good at. It replaces the
    noisy regexes of §2.5 (in the prototype, "ماء" hit سماء and أسماء).
  - A script can then compute, for every surah or window: (i) coalition candidates (fields shared by ≥ 3 roots'
    non-primary branches); (ii) **base rates** against random windows with a similar root count. This answers
    the gold's "shuffle test" and informs presentation, not inclusion. (iii) Precise surface-staging retrieval
    for R1c.
  - Cost: a one-time batch over the dictionary. It is cheap per branch and amortised over the whole Quran.
    Priority: after the S1 test, because R1 works on S1 without it.
- **R6b. Luna as auditor after the Opus draft.**
  - Worklist: seed members, HFT traces, counter rows and pairs not reflected in the ledger or prose. Output: a
    short gap list with the classical phrase or ref for each item.
  - Then **one Opus patch call** (prose + ledger + gap list → replacement paragraphs only; "integrate only what
    changes the reading; never append").
  - Cost ≈ $0.5–0.8 per ayah for Opus, plus Luna. Run it only when the audit finds more than N items, and test it
    as an optional arm.
- **R6c. Luna for filtering surface staging and mining counter-verses**, per seed (both are worklist-shaped).

### R7. Remove what does not earn its place

- **Do not add the raw** `02_hft.md` (31–34 KB per ayah), `03_pairs.md`, `04_bridges.md`, `06_concepts.md` or
  `10_leads.md` to the ayah writer. Distil them into the seed input (R1). The raw package is what cut thinking
  on 4:34.
- **In context.md, the "Word notes (… topics: …)" lines** are canonical-level v5 topics ("sound texture tightens
  into closure"). Test removing them later. They are small, but they may pull the writer toward v5's
  word-analysis catalogue.

### R8. Cost at scale (toward $1 per ayah)

**Where the money goes.** Output is 84% of cost, and thinking is most of the output. The levers, in order:
1. **Batch API** instead of `claude -p`: half price on input and output, and no 1-hour cache-write surcharge on
   input. That alone brings ≈ $1.9 to ≈ $0.9–1.0.
2. **Seeds may reduce thinking waste.** Some thinking currently rediscovers the surah from scratch in every
   ayah. Measure it.
3. **Effort "medium" for short ayat.** Test only after quality is fixed.

---

## 4. Other pushbacks and corrections

- **"weak-root imagery" in decision 4 must be defined narrowly.**
  - It should mean echo or withheld mappings (the `ECHO` sections: ر ب و, ع ي ن, ه د د in S1), split mappings,
    and documented-alternative roots (و س م), *when they are used as if identity*.
  - It must **not** mean identity-root non-primary branches. Those are the target. Otherwise the bar would
    exclude the very water and herd findings the user named.
- **Stop scoring v11 by ref counts.** 525 ledger refs against v5's 357 prose refs says nothing about the
  reader's aha. The S1 comparison's headline "v11 ≥ v5 on depth" is true for QeQ and grammar and false for the
  latent lexicon.
- **The gold is not the ceiling, and not the model of prose.** Its tag-per-paragraph apparatus (GÜÇLÜ/A…) and
  its unanchored parallels ("başka bir surede … unuttular" with no ref) are what PRINCIPLES §12 and §1 forbid.
  Match its *findings and synthesis*, not its form.
- **Chronology.** Bint al-Shāṭiʾ reads words in revelation order. The v11 brief forbids inferring chronology from
  surah order, which is correct. If a chronological order is ever used, it must come from a declared source, not
  the model's memory.

---

## 5. Test plan (S1, within $5 per ayah)

### 5.1 Arms

| arm | what runs | ayat | est. cost |
|---|---|---|---|
| **B**: baseline | current v11 outputs (exist) | all 7 + chains | $0 |
| **D**: digest v2 + Limits family (R2) | ayah writer only | 1:3, 1:4, 1:7 (where the diagnosis refs live) | ≈ $5 |
| **S**: seeds (R1 + R2 + R3 + R4) | seed pass → 7 ayah writers → chains pass | all 7 | ≈ 1.3 + 7 × 1.7 + 1.4 ≈ **$15** (≈ $2.1 per ayah) |
| **S0**: seed pass without HFT | seed call only; compare the sheet with the gold channels | — | ≈ $1.2 |
| **S-rep**: seed pass repeated | second seed call (sampling variance) | — | ≈ $1.3 |
| **S+A** (optional): Luna audit + Opus patch (R6b) | on S outputs | 1:4, 1:6, 1:7 | ≈ $2.5 + Luna |
| **Judging** | Opus judge (below) | all | ≈ $8–12 |

**Total ≈ $35–40.** The highest single arm is ≈ $2.1 per ayah plus judging ≈ $1.5 per ayah, which is under $5.
S0 tests whether the design works for the half of the Quran without HFT. Most long surahs lack it.

### 5.2 Frozen anchor set (built before any run, by script plus one human pass)

- **G** (26): the gold ledger's eligible items, with its `acceptable_equivalent_relations`, plus G027–G032 as
  bonus items. These may use Quran knowledge.
- **V5** (≈ 40–60): the substantive "v5-only" items in `compare_s001_v5.md`, minus weak-root items as defined in
  §4. This includes the **limits subset**: 57:15, 6:70, 2:256, 7:186, 18:17, 9:115, 17:15.
- **V11** (≈ 40): the current v11's distinctive finds (§2.2 and the compare doc's "v11-only" lists, plus the 14
  new chains). This is the regression guard.
- **N** (north-star examples): the traveller axis (ʿālamīn signs, mālik road-middle and lead animal, muʿabbad,
  hādī, ṣirāṭ swallowing, halt and walking in anʿamta and ġayr, the stray whose *rabb* is unknown), the water
  system, and the surface staging in 28:21–24, 16:5–16 and 20:49–54 (new; not required, but credited).

### 5.3 Scoring

**Anchor recall.** A fresh Opus judge sees one arm at a time, with arm labels removed and file names neutral,
plus the anchor list. For each anchor it assigns one of:
- *absent*;
- *ledger-only*;
- *mentioned*: stated, not connected;
- ***integrated***: explained to a non-Arabic reader, connected to the primary reading and to at least one other
  finding, and its source is visible.

The judge must quote the sentence. Report the counts per set and per layer (ayah prose / surah reading / ledger).

**Blind pairwise reader judgement** (S against B, and S against v5), per ayah, randomised A/B. The rubric follows
the north star, scored 1–5 with quotes:
1. **Grounding.** After reading, can the reader restate what the ayah says? Is there any point where they would
   be lost?
2. **Loss.** Does the reading show what the key Turkish words lose or add?
3. **Aha.** How many non-canonical, supported readings change understanding, and how good are they? Are they
   explained and connected, or catalogued?
4. **Containment and coexistence.** No "not X but Y"; nothing ranked; no defensive disclaimers.
5. **Checkability.** Every unusual claim has a visible anchor: a Quran ref or a source-tagged branch.
6. **Surah integration.** Mature chains are disclosed through this ayah's word, not retold. For the surah
   reading: each chain has explicit provenance.
7. **Economy.** No padding. Paragraphs with ≥ 8 citations are flagged by script (`check_reading.py`).

After the judge: **the user reads 1:4, 1:6 and 1:7 blind** (S against B against v5), which is the final word.

**Mechanical checks per arm:**
- `verify_ar` with sources: 0 missing, 0 wrong-source;
- validator: 0 errors;
- thinking tokens per ayah;
- cost;
- seed-word count per reading (homogenisation).

### 5.4 The bar for "materially and significantly exceeds v5"

Arm S passes only if **all** of the following hold:

1. **G:** ≥ 22/26 integrated across ayah prose plus the surah reading, and ≥ 18/26 in the ayah prose. B: 11 Y.
2. **V5:** ≥ 85% of the substantive non-weak-root anchors at least *mentioned*, and ≥ 60% *integrated*. The
   limits subset: ≥ 5 of 7 present, at the point where they limit a reading.
3. **V11:** ≥ 90% of the current v11's distinctive finds retained (the regression guard).
4. **New:** ≥ 3 substantive findings per ayah that neither v5 nor the gold has, judged substantive, e.g. surface
   staging or definitional links.
5. **Reader judgement:** S beats v5 on ≥ 6 of 7 ayat and ties or beats B on ≥ 6 of 7. No ayah may score below 4
   on grounding (1) or containment (4).
6. **Cost:** ≤ $5 per ayah including amortised passes (expected ≈ $2.1). Thinking tokens should not fall more
   than 30% below B.

If S passes on S1, run S on **S100** (the seed pass plus 100:1, 100:6 and 100:10, ≈ $7). This checks that the
horses chain, already excellent in B, survives. Then decide on Arm D alone for surahs where R1 adds nothing.

### 5.5 Order of work (each step needs the user's go-ahead, per NOTES)

1. Scripts, at no model cost:
   - digest v2;
   - `seeds_input.py` (branch table, HFT compaction, surface staging, definitional links);
   - the source-aware tag repair and validator and `verify_ar` scope;
   - ledger paragraph pointers;
   - the anchor-set file.
2. S0 and S-rep seed calls (≈ $2.5). **Read the seed sheets against the gold before spending on ayat.** If the
   sheet has no traveller, herd or water systems, R1's prompt is wrong. Fix it cheaply here.
3. Arm D (≈ $5), then Arm S (≈ $15), then the judges (≈ $10).
4. The user's blind read. Optionally S+A.

---

## 6. Appendix: files and numbers behind this review

**Files:**
- **v11 outputs:** `_commentary/v11/out/s001/1_N/{1_N.ledger.md,1_N.reading.tr.md}` and
  `out/s001/surah/{chains.md,1.surah.tr.md}`.
- **Pruning examples in the v11 ledgers:**
  - 1:4 has no B006/B007/B008 line and says "Alışkanlık ve kent dalları bu ayette çalışmaz";
  - 1:7 on the rock: "ayete taşınması ancak ses rengi olarak mümkündür";
  - 1:7 on forgetting: "Bu anlam 1:7'de işlek değildir".
- **Inputs:**
  - `_commentary/v9/input/v2/s001/1_N/01_dictionary.md` (focus roots only; e.g. م ل ك B006–B008 with their
    phrases);
  - `02_hft.md` (e.g. `1_4 d_guiding_owner_of_approach`, `1_2 c5_worlds_as_navigable_signs`,
    `1_2 o1_ecological_water_cycle`, `1_7 out_hydrological_way`);
  - `03_pairs.md` (1:4: م ل ك B006 ↔ ص ر ط B001 and ه د ي B002; B007 ↔ غ ي ر B001; B008 ↔ ه د ي B003 and
    ض ل ل B005);
  - `09_inter_ayah.md` (the notes).
- **v5 hedging example:** `quran-data/data/commentary/ayah/detailed/tr/s001/1_6.prose.tr.md`, section "Birinin
  Ardından Yürümek".

**Numbers:**

| ayah | cost | cache-write in | out | ledger | reading |
|---|---|---|---|---|---|
| 1:1 | $1.39 | 27.9k | 58.3k | 12.7 KB | 22.3 KB |
| 1:4 | $2.29 (2 turns) | 95.2k | 76.2k | | |
| 1:6 | $2.20 (2 turns) | | | | |
| 1:7 | $2.20 (2 turns) | | | | |
| surah pass | $1.06 | 59.7k | 28.9k | | |

**Surah branch tables (compact):**

| surah | branches | size |
|---|---|---|
| S1 | 193 | 64 KB |
| S100 | 217 | 71 KB |
| S18 (2 ayat packaged) | 271 | 87 KB |
