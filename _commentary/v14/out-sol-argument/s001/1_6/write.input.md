===== write.md =====
# v14 — Turkish ayah commentary from a frozen synthesis handover

Write the finished commentary for a curious Turkish reader with almost no Arabic. Their Arabic loanwords have
narrowed or shifted. Anchor the reader in what the ayah says, then make its supported surprises intelligible.
The reader should be able to explain the connections and reread the ayah with a changed understanding.

## Use each input for its particular job

- `ayah.md`: the focus text, anchor translation, morphology and word notes. Notes are prior proposals; they do not
  select the only reading. Use grammar when it changes what the reader can hear.
- `window_text.md`: the actual surrounding Quranic text. Ground the ayah in the movement before and after it;
  do not rely on an image plan as a substitute for reading the local scene.
- `synthesis.md`: findings, QeQ annotations, additional QeQ findings and axis readings, relevant images and meetings.
  F/Q/A are source records; E_F is the QeQ annotation of that F; I is an image; I_M is a meeting of images.
  Navigation groups overlap and are not an outline. Every source record occurs once. A touch/meet entry singles
  out this ayah's member. Develop/assemble entries retain wider membership. Related source records supply the
  attested branch, trigger and concrete connection.
- `dictionary.md`: the complete focus-root branches, for the concept and what Turkish loses. `branches.md`: other
  cited branches, for cross-word connections and exact quotations. A first classical phrase is an excerpt, not the
  whole entry. Do not pretend an absent quotation was supplied.
- `concordance.md`: evidence for counts and recurring uses. State the scope correctly: root, lemma, form and stop-
  lemma exclusions differ. Frequent roots have counts only; do not claim a complete contextual survey from them.
  Do not copy a conflicting count from another record.
- `passages.md`: exact complete ayat for the supplied QeQ leads, concordance uses and local window. Use these
  to check the proposed connection and to copy Quranic quotations. This file has the same spelling as the verifier;
  remembered quotations inside analysis records or previous prose are not the quotation authority. Complete ayat
  are not a complete surrounding narrative. Do not invent missing context or claim it was retrieved.
- If `source_access.md` is supplied instead, use its lookup command before developing cross-references. Retrieve
  the cited ayat and enough adjacent context to understand them, then copy their exact Arabic when quoting.
- `variants.md`: supplied alternative readings. Explain a variant when it changes a consequential reading; phonetic
  differences alone need no tour. Do not invent a variant from memory.
- `previous.md`: the immediately preceding commentary as actually written, if available. Build on its delivered
  explanations and avoid retelling them. More distant, unsupplied prose cannot be assumed to have explained anything.
  The network's disclosure plan is an intention, not evidence of delivery.

## Compose explanations

First understand the plain sense and how the ayah follows its neighbours. Then choose a connected movement of
thought. Several findings, image members, meetings and Quranic passages can do one explanatory job. Group them
around that job. Do not translate the records one by one or write a paragraph for every ID.

Build an argument the reader can follow across the whole commentary. Use a few short, meaningful headings at its
real turning points. A heading identifies what is being understood, not a root or a list of images. Each section
should develop a question raised by the ayah or the preceding explanation; paragraphs should carry consequences
forward. Do not finish one isolated image and start another merely because it is next in the evidence index.

For each substantial reading, show the word and attested sense, activating detail, how the details work together,
and what this makes perceptible in the plain reading. Sustain the physical mechanism, place, action or relationship
until its consequence becomes visible. A thematic label alone does not explain it. An image meeting needs the
relationship between its images and what that relationship shows, rather than adjacent descriptions.

Space follows this payoff. There is no item cap and no word target. Compress repeated definitions, quotations and
parallel examples; retain the inferential bridge that lets a new reader follow. A small contribution can be one
clause inside a larger explanation. A dictionary sense of a related noun is not the translation of this verb.

Every image touching the ayah needs a meaningful local contribution or an explicit deferral. Follow meet, touch,
develop, assemble as depth and continuity guidance. Assembly shows members acting together; it does not require
reciting a list of every member. If several images form one mechanism, explain them together.
The plan's role is guidance for progressive disclosure, not a ban on explaining how this ayah's working part
actually works. Look for further supported relationships among the supplied branches and image meetings. Carry a
surprising connection through its physical or relational consequence instead of stopping at its label. A new
bridge must use an attested sense, a visible activating detail and a consequence for this ayah's primary reading.

Preserve Turkish lexical losses, grammar that matters, local resonance, loaded-word patterns and independent QeQ
axes as well as images. A finding outside an image remains eligible for full treatment. Bold or partial findings
are not weakened merely because they are unusual. Readings coexist and keep the primary reading intact.

QeQ passages serve explanations. Staging and same-word describe evidence; neither requires every passage to be
quoted or demotes it. A definition, construction, scene or consequence may be indispensable under either tag or
no tag. Use enough evidence to do the job; distinguish an unused finding from an unused parallel citation.
Support, expansion and shifts remain beside the latent reading; absent staging is not counter-evidence. Explain
actual contradictions and retain their evidence even if the associated reading is deferred.

Distinguish a repeated example from a distinct explanation inside the same source record. A record may combine
a traveller scene, a different application of a word, and a limiting case. Discussing one does not deliver the
others. Preserve consequential differences, or name the omitted component in the separate partial-use notes.
Do not add citations just to consume the reference list. Explain why a passage changes the reading wherever it
does work; similar parallels can share one explanation. Previous prose can carry a relationship already delivered,
but an intended network role cannot stand in for prose the reader has actually seen.

Natural, precise Turkish. No bullet inventories, numbered root tours, internal
IDs or workflow language in reader prose. Explain terminology on first use. End by rereading the ayah through
the developed connections. Avoid defensive paragraph endings and automatic qualifications.

## Checkable Arabic

Every Arabic quotation uses exactly `{ar:ARABIC, tr:transliteration, gloss:Türkçe karşılık, source:SOURCE}`.
SOURCE is a single Quranic ref or a spaced Arabic root plus branch ID. Several sources may be comma-separated.
Use exact Quranic Arabic and copy dictionary Arabic from supplied branch lines. No commas inside ar/tr, no colon
inside gloss, no other fields or curly braces in prose. Transliteration and gloss must not turn a resonance into
a claim about the contextual translation. Quote long passages in parts. Sources are checked.

Anchor the lexical hinges of the explanation, not just the opening ayah. When a paragraph depends on a word's
unfamiliar sense, a cross-root definition, or the wording of a Quranic construction, show the short exact phrase
doing that work in a source-bearing tag and explain it in Turkish. A bare reference cannot show a reader which
word carries the inference. Tags are local to the paragraph where the Arabic does interpretive work; an earlier
tag does not anchor a later new inference. Quote only the needed words, not a whole passage for every parallel.
For narrative context that adds no wording-dependent claim, a clear Turkish account with its reference can suffice.
There is no tag quota. Use readable Turkish transliteration (ş, ç, c, ğ, â, î, û as appropriate); avoid scholarly
letter symbols that this reader cannot sound out. Exact tags establish the wording, not the truth of an inference.

## Keep a compact trace after the prose

After the commentary, write `===== SYNTHESIS =====` on a line, then one JSON object (no code fence):

    {
      "schema": 3,
      "links": [
        {"items": ["F1", "I1"], "at": ["A short exact anchor identifying the paragraph"]}
      ],
      "partial": [
        {"items": ["E_F1"], "at": ["A short exact anchor locating the part actually used"],
         "remaining": "The distinct component left unexplained", "destination": "surah commentary"}
      ],
      "deferred": [
        {"items": ["F2"], "destination": "surah commentary", "reason": "The specific reason for deferral"},
        {"items": "remaining", "destination": "surah commentary review",
         "reason": "Explain why the remaining material was not developed here"}
      ]
    }

Use actual input IDs; the example supplies format only. Each ID occurs once across links, partial and deferred.
A link locates relevant prose for independent review; it does not rate its quality or certify completeness. Do not
write quality levels, self-evaluations or payoff summaries. The explanation belongs in the commentary.

Group related IDs at the same prose locations. Supply one to three exact anchors per row, each 20–120 characters
and found in only one prose paragraph. Use the shortest identifying span; the script retrieves the full paragraph.
Give additional anchors only where the explanation needs several paragraphs. Never copy whole paragraphs here.

Use partial when a multi-part record contributes one component while another consequential component remains
unexplained. Name that omitted component and where it should be reconsidered; its mere passage number is not an
explanation of what is missing. An image's distant members intentionally reserved for later ayat need not all be
repeated here. Judge partial use against this ayah's explanatory contribution. Omitted parallel citations that add
no distinct explanation are recorded automatically and need no model-written list.

Deferrals preserve wholly unused records, including real counter-evidence. Give specific reasons for significant
deferrals; remaining collects residual items, not unacknowledged omissions inside linked records. Keep each reason
or remaining note 10–240 characters. These are metadata limits, never prose limits. The entire source inventory
is retained, and the review may reject a fluent commentary even when every ID has a valid location.


===== ayah.md =====
# ayah.md — 1:6 (the focus ayah)

ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ

Anchor translation (canonical reading, reference only):

Bizi doğru yola ilet.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ٱهْدِنَا | هَدَى | ه د ي | V;PRON |
| 2 | ٱلصِّرَٰطَ | صِرَٰط | ص ر ط | DET;N |
| 3 | ٱلْمُسْتَقِيمَ | مُّسْتَقِيم | ق و م | DET;ADJ |

## Word notes (precomputed word analysis; support, not obligations)

- 1:6:1 ٱهْدِنَا: petitionary imperative for guided direction onto the named route; the local frame selects leading and showing the way while allowing bestowal pressure to color guidance as received direction — topics: silent addressee and object suffix reverse roles; recipient and route are compressed into one verb frame; right-direction sense is selected by the path object; gift branch colors guidance as bestowed direction; command morphology functions as supplication; rare imperative surface binds beneficiary to request; guidance immediately enters the path and uprightness field; prior declaration turns into a fresh petition; request creates need for path specification; short request opens into heavier nominal cadence
- 1:6:2 ٱلصِّرَٰطَ: the definite route or path governed by the guidance request; locally a road-like way and normative conduit, with swallowing or engulfing pressure retained as image rather than replacement sense — topics: definiteness makes the path identifiable; path and qualifier are locked together; accusative route answers the imperative; physical route image carries abstract guidance; swallowing image deepens the route without replacing it; indefinite variant exposes canonical definiteness; sound texture is pressured while reference remains stable; path belongs to a recurrent straight-path formula; middle word pivots request toward specification; straight-path wording joins wider references; dominant abstract path form retains road pressure; liaison and length make the route audible
- 1:6:3 ٱلْمُسْتَقِيمَ: the definite Form X active participial qualifier: upright, straight, established, and normatively right as the path's own qualifying standard — topics: agreement locks the adjective to the path; active participle gives uprightness property-force; standing image and rectitude stay together; wide root family narrows to upright quality; canonical adjective presents one definite standard; adjective completes the straight-path formula; uprightness closes the guidance request; final adjective gives closure weight; qualifier prepares fuller path identity; upright attribute resonates beyond this noun; standing-path wording shadows the surah horizon; sound texture tightens into closure


===== window_text.md =====
# window_text.md — 1:1–7

1:1|بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
1:2|ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
1:3|ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
1:4|مَٰلِكِ يَوْمِ ٱلدِّينِ
1:5|إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
1:6|ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
1:7|صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ


===== synthesis.md =====
# synthesis.md — evidence for 1:6

This is an evidence index, not an outline or a list to put into prose. Image groups overlap. Combine them into connected explanations where their relationships earn space. No item or tag is ranked.

## Image connections (navigation only)
- I1: I1, F22, F21, F1, F3, F39, F55, F2, F18, F19, F20, F23, F56, E_F22, E_F21, E_F1, E_F3, E_F39, E_F2, E_F18, E_F19, E_F20, E_F23, Q6, Q7, I1_M1, I1_M2, I1_M3, I1_M4, I1_M5, I1_M6; role here: develop
  - This ayah's member: 1:1:1 سمو B006 (departure into open land) [N-added, activated by 1:6:2 صرط]
  - This ayah's member: 1:6:1 هدي B001 B002 (guide
  - This ayah's member: 1:6:2 صرط B001 (the road, owned by the Lord and Praised, the same road as serving the Lord) [1:6 F2 F18 F19 F20 F23 F56]
  - This ayah's member: 1:6:3 قوم B008 (straightness) [1:6 F1 F2 F21]
- I2: I2, F4, F31, F49, F50, F24, E_F4, E_F31, E_F49, E_F24, Q4, Q9, I2_M1; role here: assemble
  - This ayah's member: 1:6:1 هدي B001 (guidance as gentle indication, the knower's credential) [1:6 F4 F31 F49]
  - This ayah's member: 1:6:1 هدي B009 (the dull reader who cannot hold the way) [1:6 F50]
  - This ayah's member: 1:6:3 قوم B021 (loss: an eye intact but sightless, 36:66) [1:1 F45
- I3: I3, F13, F38, E_F13, E_F38, Q4, Q5; role here: touch
  - This ayah's member: 1:6:1 هدي B003 (guide: the foremost one, neck first
  - This ayah's member: 1:6:3 قوم B020 (the legs it walks on) [1:6 F13]
- I4: I4; role here: touch
  - This ayah's member: 1:3:1/2 رحم B004 + 1:6:3 قوم B019 B020 + 1:7:6 غضب B006 (the cost: a ewe sick after lambing) [1:1 F18
  - This ayah's member: 1:6:1 هدي B001 (release: the one who knows the way leads the lost back) [1:1 F6]
- I5: I5, I5_M1, I5_M2; role here: assemble
  - This ayah's member: 1:6:3 قوم B011 B002 (finished stature, rising upright) [1:3 F12]
  - This ayah's member: 1:6:3 قوم B013 (release: rising) [1:1 F29
- I7: I7, F58, F62, E_F62, I7_M1; role here: develop
  - This ayah's member: 1:6:1 هدي B001 (the only imperative
  - This ayah's member: 1:7:3 نعم B001 (second person continues: "You favoured") [N-added, activated by 1:6:1]
- I8: I8, F40, F47, E_F40, E_F47, Q10, I8_M1; role here: touch
  - This ayah's member: 1:6:3 قوم B016 B012 (water standing frozen
  - This ayah's member: 1:6:2 صرط B002 (swallowed away) [1:6 F40]
- I9: I9, F6, F7, F29, F45, E_F6, E_F7, E_F29, E_F45, Q1, Q2, Q7, Q10, I9_M1; role here: develop
  - This ayah's member: 1:6:3 قوم B006 B009 (maqām
- I10: I10; role here: touch
  - This ayah's member: 1:6:1 هدي B001 B010 (gentle leading
- I11: I11, F28, E_F28, I11_M1; role here: touch
  - This ayah's member: 1:6:1 هدي B001 (guidance as the form favour takes, 48:2) [1:6 F28]
- I12: I12, F32, F44, E_F32, E_F44, Q3, I12_M1; role here: develop
  - This ayah's member: 1:6:3 قوم B010 B015 B018 B007 (valuation, the full-weight coin, the straight balance, the market, the substitute) [1:6 F32 F44]
- I13: I13, F44, E_F44, Q3, I13_M1; role here: touch
  - This ayah's member: 1:6:3 قوم B007 (one standing in another's place) [1:6 F44]
- I14: I14, F15, F16, F9, F25, F43, F48, F53, F57, F52, E_F15, E_F16, E_F9, E_F25, E_F43, E_F48, Q8, Q9, I14_M1, I14_M2, I14_M3; role here: assemble
  - This ayah's member: 1:6:1 هدي B008 (a swaying walk leaning on companions or a staff) [1:6 F15 F16]
  - This ayah's member: 1:6:3 قوم B009 B012 (the pillar
  - This ayah's member: 1:6:3 قوم B002 B003 B008 B011 (upright, resolve, evenness, stature
  - This ayah's member: 1:6:3 قوم B016 B019 B020 B021 (loss: standing arrested
- I15: I15, F35, E_F35, I15_M1, I15_M2; role here: assemble
  - This ayah's member: 1:6:1 هدي B006 B008 B010 B004 (conduit: the bride conveyed, swaying and unhurried
  - This ayah's member: 1:6:3 قوم B004 B001 (the guardian
- I16: I16, F34, F36, F10, F33, E_F34, E_F36, E_F10, E_F33, Q1, Q2, Q5, I16_M1, I16_M2, I16_M3; role here: assemble
  - This ayah's member: 1:6:1 هدي B004 B005 B007 B011 (conduit: gift, offering to the House, the sanctity it lends, presenting verse) [1:6 F10 F33 F36]
  - This ayah's member: 1:6:3 قوم B001 B006 B018 (companies, station, market) [1:6 F34]
- I17: I17, F37, E_F37, Q2, I17_M1, I17_M2; role here: assemble
  - This ayah's member: 1:6:1 هدي B007 (the protected refugee, or the captive) [1:2 F43
- I18: I18, F17, F27, F46, E_F17, E_F27, E_F46, I18_M1; role here: assemble
  - This ayah's member: 1:6:1 هدي B010 (the composed walker set against a frantic rout) [1:6 F17]
  - This ayah's member: 1:6:2 صرط B001 (one road against the ways that scatter, 6:153) [1:6 F27
  - This ayah's member: 1:6:3 قوم B001 B004 (the company
- I19: I19, F12, F26, E_F12, E_F26, I19_M1; role here: assemble
  - This ayah's member: 1:6:2 صرط B003 + 1:6:3 قوم B012 + 1:6:1 هدي B003 (blade, hilt, arrowhead) [1:6 F12]
  - This ayah's member: 1:6:2 صرط B001 (pressure: the road besieged by those who sit in wait, 7:16, 7:86) [1:6 F26]
  - This ayah's member: 1:6:3 قوم B014 (mutual resistance) [1:4 F22
- I20: I20, F41, E_F41, I20_M1; role here: develop
  - This ayah's member: 1:6:3 قوم B017 (the noon stand, when shadow nearly vanishes) [1:6 F41]
- I21: I21, F30, F8, F42, E_F30, E_F8, E_F42, Q3, I21_M1; role here: develop
  - This ayah's member: 1:2:4 علم B002 + 1:6:3 قوم B013 (a signpost for the Hour, 43:61) [1:6 F30]
  - This ayah's member: 1:4:1 ملك B009 + 1:6:3 قوم B013 B002 B016 (angels standing in rows
- I22: I22, F14, F11, F61, E_F14, E_F11, I22_M1; role here: develop
  - This ayah's member: 1:6:1 هدي B003 (the neck as channel) [1:6 F14]
  - This ayah's member: 1:6:2 صرط B001 B002 B003 (conduit: road, throat and blade as one passing-through) [1:6 F11
- I23: I23, I23_M1; role here: touch
  - This ayah's member: 1:6:1 هدي B001 B010 (guidance asked
  - This ayah's member: 1:6:3 قوم B008 (holding the course straight) [1:2 F19]
- I25: I25, F51, F5, E_F5; role here: touch
  - This ayah's member: 1:6:1 → 1:7:3 نعم B004 (a "yes" answering the petition) [1:6 F51]
  - This ayah's member: 1:6:3 قوم B007 (standing in another's place) [1:6 F5]

## Evidence (each source record appears once)

### F1 — local
F1 | local | words: 1:6:1 1:6:2 1:6:3 | branches: ه د ي B001; ص ر ط B001; ق و م B008 | trigger: 1:6:1 1:6:2 1:6:3 (ayah) | with: F2 F18 | image: A guide gently points out and leads onto a road whose line does not bend or tilt; the verb chooses the road sense of the noun, and the noun chooses the evenness sense of the adjective. | anchor: دلالة بلطف إلى الطريق والحق

### F2 — cross-definition
F2 | cross-definition | words: 1:6:2 1:6:3 | branches: ص ر ط B001; ق و م B008 | trigger: 1:6:3 (ayah) | with: F1 F18 | image: The dictionary defines the path noun through the adjective's own root, so ṣirāṭ already means "the upright road". The qualifier restates and hardens what the noun holds. | anchor: الطريق المستقيم; استقامة واعتدال واستواء

### F3 — cross-definition
F3 | cross-definition | words: 1:6:1 | branches: ه د ي B001; ض ل ل B001 | trigger: 1:7:9 (window) | with: F63 | image: Guidance and straying define each other in both directions. The surah's single petition-verb and its last word frame 1:6–1:7 as one road with its opposite. | anchor: الهدى نقيض الضلالة; الضلال عن الهدى والقصد

### F4 — cross-definition
F4 | cross-definition | words: 1:6:1 | branches: ه د ي B001; ع ل م B002 | trigger: 1:2:4 (window) | with: F23 F49 | image: The 'worlds' root has a branch defined as a mark that guides to a thing, so the landmark along the road is defined through the verb of 1:6. | anchor: أثر يميز الشيء ويهدي إليه; دلالة بلطف إلى الطريق والحق

### F5 — cross-definition
F5 | cross-definition | words: 1:6:3 | branches: ق و م B007; غ ي ر B005; غ ي ر B003 | trigger: 1:7:5 (window) | with: F39 F44 | image: One sense of 'standing' is defined as standing in another's place (غيره). 1:7 then sets the road of some people against "غير" others, so both substitution and exclusion are built on the same pair. | anchor: نيابة وقيام مقام غيره; السوى والخلاف والاستثناء والنفي

### F6 — cross-definition
F6 | cross-definition | words: 1:6:3 | branches: ق و م B006; ق و م B005; ر ب ب B007 | trigger: 1:2:3 (window) | with: F29 F7 | image: The dictionary defines one sense of rabb (staying, remaining) with iqāma, the standing root. The Lord who stays and the road that keeps standing share one term. | anchor: لزوم وإقامة ودوام; أقام الشيء أي أدامه

### F7 — cross-definition
F7 | cross-definition | words: 1:6:3 | branches: ق و م B006; ن ع م B011 | trigger: 1:7:3 (window) | with: F29 F35 | image: The favour verb of 1:7 has a branch defined as finding a place agreeable and pleasant to remain in (مقام). The favoured are those who found the station good, which is the standing root's place-of-staying. | anchor: موافقة المكان وطيب المقام; أقمت بالمكان إقامة ومقاما

### F8 — cross-definition
F8 | cross-definition | words: 1:6:3 | branches: ق و م B013; ي و م B003; د ي ن B002 | trigger: 1:4:2 1:4:3 (window) | with: F42 | image: The classical phrase for the Rising defines it as the day (يوم) on which creation stands before the Self-Subsisting. 1:4's 'Day of dīn' is described in the adjective's own root. | anchor: القيامة يوم البعث يقوم الخلق بين يدي القيوم (ayn)

### F9 — concept
F9 | concept | words: 1:6:3 | branches: ق و م B002; ق و م B011; ق و م B012; ق و م B008; ق و م B005; ق و م B006; ق و م B004; ق و م B009; ق و م B016; ق و م B021; ق و م B019; ق و م B020 | trigger: 1:6:2 (ayah) | with: F16 F24 F40 | image: One kinesthetic core, standing, covers:<br>- the upright body and its stature;<br>- the load-bearing member;<br>- the even line;<br>- keeping-going, staying and guardianship;<br>- the mainstay.<br>The same core also names arrested standing: frozen water, a halted mount, an eye that stands open but blind, and pain that "stands" in an organ. The Form X participle selects the standing that holds itself up and keeps moving. | anchor: انتصاب وقيام بالبدن; جمود ووقوف وكلال

### F10 — concept
F10 | concept | words: 1:6:1 | branches: ه د ي B001; ه د ي B003; ه د ي B004; ه د ي B005; ه د ي B006; ه د ي B007; ه د ي B008; ه د ي B010 | trigger: 1:6:2 (ayah) | with: F33 F34 F35 F36 | image: The branches collapse into one act: sending or conveying something toward a destination.<br>- a gift to a beloved;<br>- an offering to the House;<br>- a bride to her husband.<br>The same field holds the front that leads, the swaying gait of one conveyed, and the protected one who takes on the sanctity of what is sent. "Guide us" can be heard as "convey us". | anchor: الهادي من كل شيء أوله; العروس المهدية إلى زوجها

### F11 — concept
F11 | concept | words: 1:6:2 | branches: ص ر ط B001; ص ر ط B002; ص ر ط B003 | trigger: 1:6:1 (ayah) | with: F12 F14 | image: A single movement of passing-through-and-beyond underlies all three branches:<br>- the road carries the traveller out of sight;<br>- the throat swallows and the morsel vanishes;<br>- the sword goes on through what it strikes. | anchor: أصل صحيح واحد يدل على غيبة في مر وذهاب; السيف القاطع الماضي في الضربة

### F12 — local
F12 | local | words: 1:6:1 1:6:2 1:6:3 | branches: ص ر ط B003; ق و م B012; ق و م B008; ه د ي B003; ق و م B014 | trigger: 1:6:2 1:6:3 1:6:1 (ayah); 1:7:6 1:5:2 (window) | with: F11 | image: A complete weapon forms inside the ayah:<br>- a cutting blade that goes through (ṣirāṭ);<br>- held by its upright hilt (qāʾim, B012);<br>- beside a straight spear (رمح قويم);<br>- an arrowhead as the front part (hādī).<br>In the window it meets resistance: the shield-hide and rock of غ ض ب B008/B004 and the firmness of ع ب د B007. | anchor: رمح قويم ورجل قويم; السيف القاطع الماضي في الضربة

### F13 — local
F13 | local | words: 1:6:1 1:6:2 1:6:3 | branches: ه د ي B003; ق و م B012; ص ر ط B001; ق و م B020 | trigger: 1:6:1 1:6:3 (ayah); 1:4:1 1:7:9 (window) | with: F38 | image: A led animal walks the road in parts:<br>- the neck and forepart go first (hawādī, necks of horses, neck of the sheep);<br>- the legs stand under it (qawāʾim);<br>- a disease can seize those legs.<br>The animal body walks the road neck-first. | anchor: الهادي من كل شيء أوله; القوام داء يأخذ الشاة في قوائمها تقوم منه (sihah)

### F14 — local
F14 | local | words: 1:6:1 1:6:2 | branches: ص ر ط B002; ه د ي B003; ض ل ل B002 | trigger: 1:6:1 (ayah); 1:7:9 (window) | with: F11 F24 | image: A throat-road: the neck (hādī) is the channel through which the swallowed thing passes and vanishes. 1:7's ض ل ل B002 supplies the other vanishing, sinking into and dissolving in a medium. Remembered lexicon: the road is so named because it swallows those who pass along it. | anchor: الغيبة في المرور والبلع | memory: yes

### F15 — local
F15 | local | words: 1:6:1 1:6:3 | branches: ه د ي B003; ه د ي B008; ق و م B002 | trigger: 1:6:1 1:6:3 (ayah); 1:5:4 (window) | with: F16 | image: A weak walker sways and leans, on two companions or on the staff that goes ahead of its owner (a hādī), until he stands upright. 1:5's help sought is the support leaned on. | anchor: مشي التهادي مع الاعتماد والتمايل; القومة ما بين الركعتين من القيام

### F16 — chain
F16 | chain | words: 1:6:1 1:6:3 | branches: ق و م B016; ه د ي B008; ق و م B002; ق و م B003; ع ب د B011; ع و ن B001; ع و ن B005 | trigger: 1:5:2 1:5:4 (window) | with: F15 F9 | image: Channel 4D, halted and recovered movement. 1:6 supplies:<br>- the failure state (the mount that stops and cannot go on);<br>- the assisted swaying gait;<br>- the regained stance and resolve.<br>1:5 supplies the stranded rider (ع ب د B011) and the help that restores balanced strength (ع و ن B005). | anchor: قام الماء جمد; العطب والانقطاع

### F17 — window
F17 | window | words: 1:6:1 | branches: ه د ي B010; ن ع م B008; ع ب د B009; ع ب د B010 | trigger: 1:7:3 1:5:2 (window) | with: F27 | image: The definition of the calm gait is itself a contrast with a routed man's frantic flight. 1:7's أَنْعَمْتَ supplies that rout: the ostrich takes flight and the company scatters. The composed walker on one road is set against a band scattering fast down many ways. | anchor: هدي السكون وحسن الهيئة; طيران النعامة وتفرق القوم

### F18 — loaded
F18 | loaded | words: 1:6:2 1:6:3 | branches: ص ر ط B001; ق و م B008; ه د ي B001 | trigger: | with: F2 F57 | image: ṣirāṭ occurs 45 times.<br>- Qualified مستقيم in 33 of 45.<br>- In 3 more by the evenness words سوي/سواء (19:43, 20:135, 38:22).<br>- In construct with God or a divine name in 7 (1:7, 6:126, 6:153, 14:1, 22:24, 34:6, 42:53).<br>- A ه د ي form stands in the clause in 24 of 45.<br>Departures: 7:86 (any road, sat upon by threateners), 23:74 (swerving from the road), 36:66 (the road raced to by the blinded), 37:23 (the road of Hell, with 'guide' used in irony).<br>1:6 is the central pattern. The anchor 'doğru yol' follows it. | anchor: وَهَدَيْنَٰهُمَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ

### F19 — loaded
F19 | loaded | words: 1:6:2 | branches: ص ر ط B001; ر ب ب B001; م ل ك B002; ح م د B001; ح م د B004 | trigger: 1:2:1 1:2:3 1:4:1 (window) | with: F20 F46 | image: The Quran names the road by its owner:<br>- road of your Lord (6:126), my road (6:153), your road (7:16);<br>- road of God, to whom belongs what is in the heavens and earth (42:53);<br>- road of the Mighty, the Praised (14:1, 34:6); road of the Praised (22:24).<br>Also 'my Lord is on a straight road' (11:56). So 1:2's ḥamd and rabb and 1:4's owner name the road's owner and its praised end (ح م د B004). | anchor: إِلَىٰ صِرَٰطِ ٱلْعَزِيزِ ٱلْحَمِيدِ; حماداك الغاية المحمودة

### F20 — loaded
F20 | loaded | words: 1:6:2 1:6:3 | branches: ص ر ط B001; ع ب د B003; ر ب ب B001 | trigger: 1:2:3 1:5:2 (window) | with: F19 F63 | image: Four times the Quran defines the straight road as serving the Lord: 3:51, 19:36 and 43:64 ('my Lord and your Lord, so serve Him: this is a straight road'), and 36:61. The Quran's own formula for 1:6's road is the rabb of 1:2 plus the naʿbudu of 1:5. | anchor: إِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ هَٰذَا صِرَٰطٌ مُّسْتَقِيمٌ

### F21 — loaded
F21 | loaded | words: 1:6:2 1:6:3 | branches: ص ر ط B001; ق و م B008; د ي ن B001; د ي ن B005; ه د ي B002 | trigger: 1:4:3 (window) | with: F23 | image: At 6:161 the Quran puts the straight road in apposition to 'a standing dīn' (قيما, the same ق و م root). 1:4's dīn, as obedience and customary way, is the road itself. It matches ه د ي B002, هدي as a person's way and manner. | anchor: هَدَىٰنِى رَبِّىٓ إِلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ دِينًا قِيَمًا

### F22 — loaded
F22 | loaded | words: 1:6:1 1:6:2 | branches: ه د ي B001; م ل ك B006; د ي ن B002 | trigger: 1:4:1 1:4:3 (window) | with: F23 F56 | image: The same imperative ٱهْدِنَا recurs once, at 38:22. There litigants before David ask 'judge between us with truth… and guide us to the middle of the road'. The request for guidance is a request for a just verdict. سواء, the middle of the road, is what مَلَك الطريق (1:4 مَٰلِكِ) names. | anchor: وَٱهْدِنَآ إِلَىٰ سَوَآءِ ٱلصِّرَٰطِ; مَلَك الطريق والوادي

### F23 — chain
F23 | chain | words: 1:6:1 1:6:2 1:6:3 | branches: ص ر ط B001; ق و م B008; ه د ي B002; ع ب د B005; م ل ك B006; ع ل م B002; د ي ن B005 | trigger: 1:5:2 1:4:1 1:2:4 1:4:3 (window) | with: F4 F22 F21 | image: Channel 4A, the marked and prepared road. 1:6 supplies the road, its evenness and its heading. The window supplies:<br>- the trodden, levelled surface (1:5);<br>- the centre-line (1:4);<br>- the landmarks (1:2);<br>- the habitual course (1:4 dīn).<br>38:22's 'middle of the road' closes the picture. | anchor: التذليل والتسوية; مَلَك الطريق والوادي

### F24 — loaded
F24 | loaded | words: 1:6:2 1:6:3 | branches: ق و م B021; ض ل ل B002; ص ر ط B002 | trigger: 1:7:9 (window) | with: F14 F41 | image: The Quran tells the scene at 36:66: had We effaced their eyes, they would race to the road, but how would they see? ق و م B021 is the eye that stands intact yet sightless. ض ل ل B002 is the road hidden from view. 5:16 and 14:1 set the road in the passage from darkness to light. | anchor: لَطَمَسْنَا عَلَىٰٓ أَعْيُنِهِمْ فَٱسْتَبَقُوا۟ ٱلصِّرَٰطَ فَأَنَّىٰ يُبْصِرُونَ; عين قائمة ذهب بصرها والحدقة صحيحة (ayn)

### F25 — loaded
F25 | loaded | words: 1:6:1 1:6:3 | branches: ق و م B002; ق و م B011; ه د ي B001; ه د ي B008 | trigger: 1:7:9 (window) | with: F15 F48 | image: At 67:22 the Quran draws the straight road as bodily posture: one walks bent over on his face, the other walks upright on a straight road, and 'better guided' (أهدى) is asked of the two gaits. The standing body of ق و م B002/B011 and the gait of ه د ي are the Quran's own picture. | anchor: أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ

### F26 — loaded
F26 | loaded | words: 1:6:2 1:6:3 | branches: ص ر ط B001; ق و م B014; ق و م B002; غ ض ب B003 | trigger: 1:7:6 (window) | with: F12 | image: The road is contested by those who sit on it. Iblis vows to sit in wait on 'Your straight road' (7:16), and threateners sit on every road barring the way (7:86). Sitting (قعد) ambushers stand against the standing road and its walkers, joining ق و م B014 (resistance) and 1:7's opposition (غ ض ب B003). | anchor: لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ

### F27 — loaded
F27 | loaded | words: 1:6:2 1:6:3 1:6:1 | branches: ص ر ط B001; ق و م B001; ع ب د B010; ن ع م B008 | trigger: 1:5:2 1:7:3 (window) | with: F17 | image: At 6:153 the Quran tells the scene of many paths: follow this straight road of Mine, not the ways that scatter you from His way. The scattered roads of ع ب د B010 and the dispersing company of ن ع م B008 are the alternative to one road walked by one people (ق و م B001, the plural نا). | anchor: وَلَا تَتَّبِعُوا۟ ٱلسُّبُلَ فَتَفَرَّقَ بِكُمْ عَن سَبِيلِهِۦ

### F28 — loaded
F28 | loaded | words: 1:6:1 1:6:2 | branches: ه د ي B001; ه د ي B004; ن ع م B001; ر ح م B001 | trigger: 1:7:3 1:1:3 1:3:1 (window) | with: F36 | image: The Quran binds favour to being guided on the straight road:<br>- 48:2: 'complete His favour upon you and guide you a straight road';<br>- 16:121: 'thankful for His favours… guided him';<br>- 4:175: 'into mercy from Him… and guide them a straight road'.<br>1:7's أَنْعَمْتَ and 1:1/1:3's mercy follow the Quran's own pairing. | anchor: وَيُتِمَّ نِعْمَتَهُۥ عَلَيْكَ وَيَهْدِيَكَ صِرَٰطًا مُّسْتَقِيمًا

### F29 — loaded
F29 | loaded | words: 1:6:2 1:6:3 | branches: ق و م B006; ن ع م B011; د ي ن B006; ر ب ب B007 | trigger: 1:7:3 1:4:3 1:2:3 (window) | with: F6 F7 | image: At 10:25 the road leads to a dwelling ('God calls to the abode of peace… guides to a straight road'). The standing root's station (مقام) is the end, completed by:<br>- 1:7's agreeable place to remain;<br>- 1:4's city of obedience;<br>- 1:2's staying and dwelling. | anchor: وَٱللَّهُ يَدْعُوٓا۟ إِلَىٰ دَارِ ٱلسَّلَٰمِ وَيَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ

### F30 — loaded
F30 | loaded | words: 1:6:2 1:6:3 | branches: ق و م B013; ع ل م B002; ص ر ط B001 | trigger: 1:2:4 1:4:2 (window) | with: F42 | image: At 43:61 the Quran calls someone knowledge (or, in another reading, a signpost, عَلَم) for the Hour, followed by 'follow me: this is a straight road'. The Hour of ق و م B013 stands at the road's end with a marker (ع ل م B002) pointing to it. | anchor: وَإِنَّهُۥ لَعِلْمٌ لِّلسَّاعَةِ فَلَا تَمْتَرُنَّ بِهَا وَٱتَّبِعُونِ هَٰذَا صِرَٰطٌ مُّسْتَقِيمٌ | memory: yes

### F31 — loaded
F31 | loaded | words: 1:6:1 1:6:2 | branches: ه د ي B001; ع ل م B001; ص ر ط B001 | trigger: 1:2:4 (window) | with: F4 | image: The Quran sets knowledge as what guides onto the road. Abraham says knowledge has come to him, so 'follow me, I will guide you an even road' (19:43). 'Those given knowledge see… it guides to the road of the Mighty, the Praised' (34:6). 1:2's ʿālamīn root in its knowing branch is the guide's credential. | anchor: إِنِّى قَدْ جَآءَنِى مِنَ ٱلْعِلْمِ مَا لَمْ يَأْتِكَ فَٱتَّبِعْنِىٓ أَهْدِكَ صِرَٰطًا سَوِيًّا

### F32 — loaded
F32 | loaded | words: 1:6:3 | branches: ق و م B008; ق و م B015; ق و م B010 | trigger: 1:4:3 (window) | with: F44 | image: The lemma مُّسْتَقِيم occurs 37 times, 33 of them qualifying ṣirāṭ. Remembered: the others include 'the straight balance' (القسطاس المستقيم, 17:35, 26:182), where straightness is exact weight. 16:76 puts the road-walker beside the one who 'commands justice' and asks 'are they equal?'. Straightness sounds as ق و م B015's untilted coin. | anchor: دنانير قوم وقيم ودينار قائم أي مثقال سواء لا يرجح (ayn); يَأْمُرُ بِٱلْعَدْلِ وَهُوَ عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ | memory: yes

### F33 — loaded
F33 | loaded | words: 1:6:1 | branches: ه د ي B005; ه د ي B004 | trigger: | with: F10 F34 | image: The root's own Quranic lemmas include هَدْي (7, the sacrificial offering driven to the sanctuary) and هَدِيَّة (2, a gift; remembered as the queen's gift to Solomon). The conveying and gift senses of the petition verb are in the Quran's own usage, not only the lexicon's. | anchor: الهدي والهدي ما أهديت إلى مكة | memory: yes

### F34 — window
F34 | window | words: 1:6:1 1:6:3 | branches: ه د ي B005; ه د ي B007; ق و م B001; ق و م B018; ق و م B006; و س م B004; ن ع م B005 | trigger: 1:1:1 1:7:3 (window) | with: F33 F10 | image: A pilgrimage season, pieced together from:<br>- a marked assembly time and place (موسم, 1:1 ~alt);<br>- companies of people travelling a road, driving livestock (1:7) as offerings to the House;<br>- the refugee who shares that offering's sanctity;<br>- markets that come alive;<br>- a station where they stay. | anchor: موسم معلم يجتمع إليه الناس; الرجل الذي له حرمة كحرمة هدي البيت

### F35 — window
F35 | window | words: 1:6:1 1:6:2 1:6:3 | branches: ه د ي B006; ه د ي B008; ه د ي B010; م ل ك B004; ر ح م B002; ن ع م B011; ق و م B006 | trigger: 1:4:1 1:1:3 1:7:3 (window) | with: F7 F10 | image: A bridal procession:<br>- a marriage contract (1:4) and kinship (1:1/1:3);<br>- the bride conveyed along a road to her husband with the swaying gait of women and laden camels, composed and unhurried;<br>- arrival at a house she finds good to stay in (1:7).<br>"Guide us" is heard as "convey us, as a bride is conveyed". | anchor: الهداء مصدر قولك هديت المرأة إلى زوجها; التهادي مشي في تمايل يمينا وشمالا كمشي النساء والإبل الثقال (ayn)

### F36 — window
F36 | window | words: 1:6:1 | branches: ه د ي B004; ه د ي B011; ح م د B001; ح م د B006; ع ب د B003; ن ع م B001 | trigger: 1:2:1 1:5:2 1:7:3 (window) | with: F28 F10 | image: An exchange of gifts (مهاداة). The speaker first presents praise addressed to God (1:2) and service (1:5), as one presents a poem (إهداء الشعر). Then the speaker asks for a gift sent in affection. 1:7 names the favour received. | anchor: الإهداء أن تهدي إلى إنسان مديحا أو هجاء شعرا (ayn); أحمد إليك الله

### F37 — window
F37 | window | words: 1:6:1 | branches: ه د ي B007; ع ب د B001; ع ب د B004; د ي ن B004; ر ب ب B011; ع و ن B001 | trigger: 1:5:2 1:4:3 1:2:3 1:5:4 (window) | with: F34 | image: The same noun names the protected client and, in some glosses, the captive. The speaker of 1:5, a slave and one under dominion, seeks help and asks to be taken in: either led as a captive or received as a refugee under covenant (1:2 ربابة عهد). | anchor: هدي الحرمة والأسير; ربابة عهد وميثاق

### F38 — chain
F38 | chain | words: 1:6:1 | branches: ه د ي B003; م ل ك B008; ض ل ل B005; ر ب ب B014; ع و ن B006 | trigger: 1:4:1 1:7:9 1:2:3 1:5:4 (window) | with: F13 | image: Channel 4B/8A: a herd (wild cattle, wild asses) with its leader in front (hādī and malak share المتقدم) and the stray camel that has left it. The Quran adds the herder's grip at 11:56: no creature but He holds it by the forelock, 'my Lord is on a straight road'. | anchor: المتقدم الهادي وأوائل الشيء; مَا مِن دَآبَّةٍ إِلَّا هُوَ ءَاخِذٌۢ بِنَاصِيَتِهَآ إِنَّ رَبِّى عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ

### F39 — window
F39 | window | words: 1:6:1 1:6:3 | branches: ه د ي B002; ق و م B007; ق و م B001 | trigger: 1:7:1 1:7:2 (window) | with: F5 | image: هدي also means following another's course and resembling him. 1:7 at once names the road as 'the road of those…'. Guidance is walking in predecessors' tracks, standing in their place (قيام مقام غيره) as a people. | anchor: خذ في هديتك أي فيما كنت فيه من الحديث أو العمل ولا تعدل عنه; جهة الأمر وسيرته وقصده

### F40 — window
F40 | window | words: 1:6:3 1:6:2 | branches: ق و م B016; و ل ه B003; ص ر ط B002; ض ل ل B002 | trigger: 1:1:2 1:2:2 1:7:9 (window) | with: F9 | image: Water fails two ways:<br>- it "stands" frozen and does not flow (قام الماء جمد);<br>- it is let loose and runs off to vanish in open ground (ماء مولَه, ~alt of the divine name).<br>ص ر ط B002 and ض ل ل B002 give the vanishing. Mustaqīm is the standing that still moves. | anchor: قام الماء جمد; ماء مُولَه ذاهب

### F41 — window
F41 | window | words: 1:6:3 | branches: ق و م B017; ي و م B001; س م و B004; ض ل ل B002 | trigger: 1:4:2 1:1:1 1:7:9 (window) | with: F24 | image: The noon stand of the sun at the sky's midpoint, when shadow almost vanishes. It is the day's most visible moment, set against the hiding and sinking out of sight of 1:7. | anchor: قام قائم الظهيرة إذا قامت الشمس وكاد الظل يعقل (ayn

### F42 — chain
F42 | chain | words: 1:6:3 | branches: ق و م B013; ق و م B002; ي و م B003; د ي ن B002; م ل ك B003 | trigger: 1:4:1 1:4:2 1:4:3 (window) | with: F8 F30 | image: Channel 5C: the Day on which creation stands before the King for account. The adjective of 1:6 carries the Rising within it. The road's walkers are upright now, as they will stand at the reckoning named in 1:4. | anchor: قيامة وبعث وقيام الساعة; الحساب والجزاء

### F43 — surah
F43 | surah | words: 1:6:3 | branches: ق و م B002; ع ب د B003 | trigger: 1:5:2 (window) | with: F25 | image: The standing of ق و م B002 is the prayer-stance itself (the standing between two bowings). Remembered practice: al-Fātiḥa is recited standing in prayer, so the reciter asks for the upright road while bodily upright in the service of 1:5. | anchor: القومة ما بين الركعتين من القيام | memory: yes

### F44 — chain
F44 | chain | words: 1:6:3 | branches: ق و م B010; ق و م B015; ق و م B018; ق و م B007; د ي ن B002; د ي ن B003; غ ي ر B002; ض ل ل B003; ض ل ل B005 | trigger: 1:4:3 1:7:5 1:7:9 (window) | with: F32 F5 | image: Channels 6A/6B. 1:6 supplies:<br>- valuation;<br>- the exact coin;<br>- the busy market;<br>- the substitute that stands in another's place.<br>The window supplies debt and reckoning (1:4), blood-money (1:7 غير), and blood left unredressed and the stray asset (1:7 ضالين). | anchor: القيمة ثمن الشيء بالتقويم; الغَيْر في الدية

### F45 — chain
F45 | chain | words: 1:6:3 | branches: ق و م B009; م ل ك B005; م ل ك B007; غ ي ر B001; ر ب ب B002 | trigger: 1:4:1 1:7:5 1:2:3 (window) | with: F46 | image: A supplied road. What keeps life standing is:<br>- ق و م B009's mainstay, sharing عماد with 1:4's مِلاك;<br>- the water that commands the camp;<br>- provisions and repair of gear on the way (غ ي ر B001, ميرة);<br>- rabb's step-by-step nurture. | anchor: قوام وعماد ومعاش; مِلاك الأمر وعِماده

### F46 — chain
F46 | chain | words: 1:6:3 | branches: ق و م B004; ر ب ب B001; ر ب ب B002; م ل ك B003 | trigger: 1:2:3 1:4:1 (window) | with: F45 F19 | image: The qayyim of a people manages their affair and keeps them straight (يقومهم). Lord and King of 1:2 and 1:4 are that guardian of the road's company. | anchor: قيم القوم من يسوس أمرهم ويقومهم

### F47 — chain
F47 | chain | words: 1:6:3 | branches: ق و م B012; ع ل م B005; ن ع م B007; ر ب ب B013; م ل ك B007 | trigger: 1:2:4 1:7:3 1:2:3 1:4:1 (window) | with: F45 | image: Channel 10B: the well-head. 1:6 supplies its upright pulley-frame (the man-shaped structure on the well's rim). 1:7's ostrich-timber and 1:2's water-rich well and abundant water complete it. | anchor: القامة مقدار قيام الرجل كهيئة الرجل يبنى على شفير بئر

### F48 — window
F48 | window | words: 1:6:3 | branches: ق و م B011; ق و م B008; ع و ن B005; ع ب د B007; غ ض ب B005 | trigger: 1:5:4 1:5:2 1:7:6 (window) | with: F25 | image: The evenness of the road and the evenness of a grown body share one word, استواء (ق و م B008; ع و ن B005 استواء الخلقة). Together they draw a tall, balanced, firm body (1:5) standing in its full strength. | anchor: قامة وقوام الجسم والطول; استواء الخلقة وتلاحق القوة

### F49 — window
F49 | window | words: 1:6:1 | branches: ه د ي B001; س م و B005; ع ل م B003 | trigger: 1:1:1 1:2:4 (window) | with: F4 | image: Three roots are defined through indication (دلالة): the name (1:1) as indication, the created world (1:2) as indicating its Maker, and guidance as gentle indication. The name and the worlds point; 1:6 asks to be led along what they point to. | anchor: الاسم تنويه ودلالة; الخلق عالم يدل على صانعه

### F50 — fragment
F50 | fragment | words: 1:6:1 | branches: ه د ي B009; ض ل ل B004; ع ل م B001 | trigger: 1:7:9 1:2:4 (window) | with: | image: The dull, weak, heavy man of the guidance root stands beside the forgetting of 1:7 and the knowing of 1:2: one who cannot keep the way in mind. | anchor: الهداء الرجل البليد الضعيف (ayn)

### F51 — fragment
F51 | fragment | words: 1:6:1 | branches: ه د ي B001; ن ع م B004 | trigger: 1:7:3 (window) | with: | image: 1:7's root holds the answering "yes" (نعم). The petition of 1:6 is followed by a word that sounds like the granting. | anchor: الجواب بنعم والتصديق

### F52 — fragment
F52 | fragment | words: 1:6:3 | branches: ق و م B019; ق و م B020; غ ض ب B006; ر ح م B004 | trigger: 1:7:6 1:1:3 (window) | with: F9 | image: Ailments of the body in which something "stands" wrongly: pain lodged in back or eye, a disease in the sheep's legs, swelling around the eye (1:7), and a womb in pain after birth (1:1). | anchor: قام بي ظهري أي أوجعني

### F53 — fragment
F53 | fragment | words: 1:6:3 | branches: ق و م B003; ع ب د B003; ع و ن B001 | trigger: 1:5:2 1:5:4 (window) | with: F16 | image: Rising with resolve to a task, beside the service and sought help of 1:5. | anchor: قام بمعنى العزيمة

### F54 — fragment
F54 | fragment | words: 1:6:1 | branches: ه د ي B001 | trigger: 1:6:3 (ayah) | with: | image: pairs.md lists sound-family ه د د senses under ٱهْدِنَا that neither dictionary.md nor the scan attests: demolition, a tall man, rocking a child to sleep, heavy tread, a steep descent. With ق و م B011 (stature) and B002 (rising), the tall-man and descent senses would join a body-and-terrain picture. | anchor: دلالة بلطف إلى الطريق والحق | memory: yes

### F55 — grammar
F55 | grammar | words: 1:6:1 1:6:2 | branches: ه د ي B001; ص ر ط B001 | trigger: | with: F22 F18 | image: ٱهْدِنَا takes the road as a second direct object with no إلى (as in 4:68, 19:43, 37:118, 48:2, 48:20). 38:22's identical imperative adds إلى, and most uses have إلى. Remembered grammarians' distinction: the direct object means leading along or into the road; إلى means directing toward it. The anchor 'yola ilet' uses the dative and so hears the إلى pattern. | anchor: وَلَهَدَيْنَٰهُمْ صِرَٰطًا مُّسْتَقِيمًا | memory: yes

### F56 — grammar
F56 | grammar | words: 1:6:2 1:6:3 | branches: ص ر ط B001; ق و م B008 | trigger: | with: F18 | image: The road is definite: 'the road, the straight one', with the article on both noun and adjective. The Quran has that definite pair only at 1:6, 7:16 (the road Iblis besieges) and 37:118 (given to Moses and Aaron). Elsewhere it is 'a straight road'. 1:7 then defines it again by annexation. Turkish, which has no article, cannot mark this. | anchor: وَهَدَيْنَٰهُمَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ

### F57 — grammar
F57 | grammar | words: 1:6:3 | branches: ق و م B008; ق و م B002; ع و ن B001 | trigger: | with: F9 | image: مستقيم is a Form X active participle. It names a road that itself keeps holding upright, as an ongoing property, not a line drawn straight once. It rhymes with and mirrors 1:5's Form X نستعين: 'we seek help', answered by 'the self-upholding'. | anchor: استقامة واعتدال واستواء

### F58 — grammar
F58 | grammar | words: 1:6:1 | branches: ه د ي B001 | trigger: | with: F63 | image: This is the surah's only imperative, a command form used as a petition. Its object suffix نا continues 1:5's plural 'we', so the whole company, not a lone traveller, is to be led. The second-person address carries on into 1:7's أنعمتَ. | anchor: ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ

### F59 — loss
F59 | loss | words: 1:6:3 | branches: ق و م B002; ق و م B008; ق و م B013; ق و م B006 | trigger: | with: F9 | image: Turkish 'doğru' merges 'straight' with 'true/correct' and adds a truth-value judgement. It loses standing, the body, and keeping-upright. Turkish holds the root's loanwords (kıyam, kıyamet, kavim, ikamet, makam, kıymet, kayyum) but hears no link among them. 'İstikamet', the very noun of this adjective, means only 'direction' in Turkish. | anchor: انتصاب وقيام بالبدن

### F60 — loss
F60 | loss | words: 1:6:1 | branches: ه د ي B001; ه د ي B004; ه د ي B003 | trigger: | with: F10 | image: 'İlet' (convey) keeps the conveying of the bride or offering. It loses the gentleness (بلطف), the front that goes ahead, and the gift. Turkish 'hidayet' (narrowed to religious conversion) and 'hediye' (gift) come from this root but are heard as unrelated. | anchor: بعثة لطف وهدية إلى ذي مودة

### F61 — loss
F61 | loss | words: 1:6:2 | branches: ص ر ط B001; ص ر ط B002; ص ر ط B003 | trigger: | with: F11 F18 | image: 'Yol' is generic and loses the swallowing and the cutting blade. The Turkish loanword 'sırat' (remembered: 'sırat köprüsü', the bridge over Hell, thinner than a hair and sharper than a sword) adds a bridge that none of the 45 Quranic uses names. Its 'sharper than a sword' does echo the attested B003 blade. | anchor: السيف القاطع الماضي في الضربة | memory: yes

### F62 — chain
F62 | chain | words: 1:6:1 1:6:2 1:6:3 | branches: ه د ي B001; ع و ن B001; ص ر ط B001; ق و م B008 | trigger: 1:5:4 1:7:1 1:7:3 (window) | with: F3 F20 F58 | image: Channel 1C. 1:6 is the hinge of the petition:<br>- it turns 1:5's general 'we seek help' into one specific help, guidance;<br>- it names the road;<br>- 1:7 re-takes that road as its first word and fills it with the favoured, closing on straying, guidance's defined opposite. | anchor: الهدى نقيض الضلالة

### E_F1 — supports
F1 | supports | 28:22 [same-word] [staging], 20:10 [staging], 18:1, 18:2 | 28:22 openly shows a traveller asking his Lord to guide him along the even way, and 20:10 shows a man at night hoping to find at the fire someone who guides on the road. 18:1–2 describe a Book with no crookedness that is "upright" (ق و م), which gives the Quran's own wording for a line that does not bend.

### E_F2 — shifts
F2 | shifts | 37:23 [same-word], 7:86 [same-word], 20:135 [same-word] | The Quran lets the noun stand for the road of Hell (37:23) and for any road where threateners sit (7:86), so in Quranic usage uprightness is not locked inside the noun. The dictionary's "upright road" holds through the dominant collocation and the evenness variant (20:135), and the qualifier in 1:6 does real work rather than only repeating the noun.

### E_F3 — supports
F3 | supports | 93:7 [same-word], 6:71 [staging], 2:16, 16:9 | 93:7 turns straying straight into guiding, and 2:16 trades one for the other. 6:71 stages the bewildered one in open land whose companions call him to guidance. 16:9 sets the road's true aim (qaṣd) against the roads that swerve, which is the dictionary's own "straying from guidance and aim".

### E_F4 — supports
F4 | supports | 16:16, 43:10 | Landmarks (ʿalāmāt, the ʿālamīn root) and stars are what people are guided by (16:16), and roads are laid in the earth "so that you may be guided" (43:10). This is the waymark defined through the verb of 1:6.

### E_F5 — supports
F5 | supports | 47:38 [staging], 9:39 | "He will replace you with a people (qawm) other than you (ghayr)": the Quran tells substitution openly, using the standing root's people-noun, a Form X verb of exchange and 1:7's ghayr together. Standing-in-place and exclusion are built on the same pair.

### E_F6 — supports
F6 | supports | 55:27, 20:111 | All on earth passes away and the Face of your Lord remains (55:27). Faces are humbled before the Ever-Living, the Self-Subsisting (qayyūm, 20:111). The Lord who stays and the standing root meet in the divine names.

### E_F7 — supports
F7 | supports | 9:21, 25:76, 35:35 | The Lord gives tidings of gardens with lasting favour (naʿīm muqīm, the favour root and the staying root in one phrase, 9:21). Paradise is "good as a resting place and station" (25:76), the Abode of Staying (35:35). The favoured are those who found the station good.

### E_F8 — supports
F8 | supports | 83:6 [staging], 20:111 | "The day people stand for the Lord of the worlds" (83:6) tells the Rising openly with the adjective's root and 1:2's exact title. 20:111 puts faces before the Self-Subsisting on that Day.

### E_F9 — supports
F9 | supports | 2:20 [staging], 34:14 [staging], 95:4 | In 2:20, when darkness falls on the walkers "they stand" (qāmū), meaning they halt. This is the Quran's own use of the arrested standing. 34:14 shows Solomon's body standing upright though dead, held by a staff. 95:4 (best taqwīm) gives the upright form that holds itself.

### E_F10 — supports
F10 | supports | 37:23 [same-word], 19:85 [staging], 19:86, 57:12 [staging], 5:95 | "Lead them to the road of Hell" (37:23) uses the petition verb in its bare conveying sense. 19:85–86 set a delegation escorted to al-Raḥmān beside a herd driven thirsting to Hell. 57:12's light running ahead of the believers is the leading front. 5:95's offering "reaching the Kaʿba" is conveyance to a destination.

### E_F11 — expands
F11 | expands | 37:23 [same-word], 37:24, 19:71, 19:72, 23:74 [same-word] | The road-word carries its passers to a hidden end: to Hell, where they are halted for questioning (37:24). Every soul comes down to it and only the God-fearing are brought out beyond it (19:71–72). The passing-through reading is sharpened: whose road it is decides whether the passer vanishes or comes through.

### E_F12 — expands
F12 | expands | 57:25 | Iron "with mighty force" is sent down beside the Book and the balance "so that people may stand with justice". The blade and the upright stance are joined in one ayah, and force serves the standing.

### E_F13 — expands
F13 | expands | 11:56 [same-word], 55:41 | Every creature is held by its forelock beneath a Lord on a straight road (11:56). On the Day the guilty are seized "by the forelocks and the feet" (55:41). The Quran names the same two parts, front and legs, and shifts them from walking to being held.

### E_F14 — supports
F14 | supports | 32:10 [staging] | "When we are lost (ḍalalnā) in the earth" is ض ل ل B002 in the Quran's own usage: the dead dissolved and hidden in the ground. This is the vanishing the throat-road pairs with.

### E_F15 — supports
F15 | supports | 20:18 [staging], 34:14 [staging] | Moses leans on his staff and beats leaves for his sheep (20:18). Solomon's body is kept upright on his staff (34:14). Both show the staff as the support leaned on until stance holds or fails.

### E_F16 — supports
F16 | supports | 2:20 [staging], 48:25 | 2:20 tells halted and resumed movement openly: they walk while the lightning lights the way and stand still when it darkens. 48:25 gives the guidance root's own offering held back (maʿkūf) from reaching its place, a halted conveyance.

### E_F17 — supports
F17 | supports | 25:63, 31:19, 74:50 [staging], 74:51 | The servants of al-Raḥmān walk the earth gently (25:63), and the walker is told to be measured (qaṣd) in his gait (31:19). 74:50–51 tell the rout openly: startled wild asses fleeing a lion.

### E_F18 — supports
F18 | supports | 36:4 [same-word], 23:74 [same-word], 16:9 | 36:4 repeats the central formula ("on a straight road"). 23:74 and 16:9 confirm that the departures are named against it: turning off the road, and roads that swerve.

### E_F19 — supports
F19 | supports | 42:53 [same-word], 16:69 [staging] | The road of God, to whom belongs all in the heavens and earth, closes with all affairs journeying to God (42:53). 16:69 names "the ways of your Lord", made tractable, as walked by the bee.

### E_F20 — expands
F20 | expands | 36:60, 36:61 [same-word], 6:162 | 36:60–61 set the service that makes the straight road against serving Satan. 6:162, straight after the road of 6:161, spells the road as prayer, rite, life and death for the Lord of the worlds, 1:2's own title.

### E_F21 — supports
F21 | supports | 30:30, 42:13, 98:5 | "Set your face upright to the dīn … that is the standing dīn" (30:30). "Make the dīn stand, and do not scatter in it" (42:13). "That is the dīn of the upright" (98:5). Each ties dīn to the ق و م root.

### E_F22 — expands
F22 | expands | 38:26, 21:112 | After the plea of 38:22, David is told to judge between people with truth and not follow desire, "lest it lead you astray from the way of God" (38:26). Verdict and road are one. 21:112 has a prophet ask his Lord to judge with truth.

### E_F23 — supports
F23 | supports | 67:15 [staging], 16:69 [staging], 2:143, 16:16 | The earth is made tractable (dhalūl, the tadhlīl of 1:5) and people walk its shoulders (67:15). The bee is sent on the Lord's tractable ways (16:69). Those guided to the straight road are made a middle community (2:143), the centre-line. Landmarks mark the road (16:16).

### E_F24 — supports
F24 | supports | 7:179 [staging], 2:20 [staging], 22:46, 57:13 | "They have eyes they do not see with" (7:179) is ق و م B021 told openly. In 2:20 lightning nearly snatches the walkers' sight. 22:46 shifts the blindness from the intact eye to the heart. 57:13 sends the lightless back behind to seek light.

### E_F25 — supports
F25 | supports | 67:22 [staging] [same-word], 17:97 [staging] [same-word], 25:34 | The upright walker on the straight road is set against those gathered on the Day of Rising on their faces, blind, deaf and dumb (17:97). 25:34 calls those dragged on their faces "most astray in way", 1:7's root. The bent gait is the loss of the road.

### E_F26 — supports
F26 | supports | 7:16 [staging] [same-word], 7:17, 15:41 [same-word], 15:42 | The ambush is told openly, and 7:17 adds attack from before, behind, right and left. 15:41–42 bound it without reversing it: the road runs to God, and the ambusher has no authority over His servants, the ʿibād of 1:5.

### E_F27 — expands
F27 | expands | 6:153 [staging] [same-word], 3:101 [same-word], 3:103, 42:13 | Whoever holds fast to God is guided to a straight road (3:101). The next command is to hold God's rope together and not scatter (3:103). 42:13 joins making the dīn stand with not scattering. One road is walked by one gathered company.

### E_F28 — supports
F28 | supports | 93:7 [same-word], 93:11, 76:3 [same-word], 49:17 [same-word], 12:6 | Found straying, then guided, then told to proclaim the Lord's favour (93:7, 93:11). The way is shown to one who is thankful or ungrateful (76:3). Guidance is itself God's favour on the guided (49:17). Favour is completed as on predecessors (12:6).

### E_F29 — supports
F29 | supports | 10:9 [same-word], 10:10, 7:43 [same-word], 35:35 | The Lord guides the faithful into gardens of favour (naʿīm), and their last call there is 1:2's exact praise of the Lord of the worlds (10:9–10). At arrival they praise God who guided them (7:43), in the Abode of Staying (35:35).

### E_F30 — expands
F30 | expands | 43:61 [same-word], 47:18, 70:43 | Read canonically as "knowledge of the Hour", 43:61 already points to the Hour before naming the road. 47:18 says the Hour's signs (ashrāṭ) have come. On the Day, 70:43 has the dead rush from their graves as if racing to a set-up marker.

### E_F31 — supports
F31 | supports | 22:54 [same-word], 19:43 [same-word], 31:20 | Those given knowledge recognise the truth, and God guides the faithful to a straight road (22:54). Its opposite is disputing "without knowledge, guidance or illuminating Book" (31:20).

### E_F32 — supports
F32 | supports | 17:35 [same-word], 26:182 [same-word], 55:9, 16:76 [same-word] | "Weigh with the straight balance" (17:35, 26:182) is the adjective as exact weight. 55:9 has "make the weight stand with justice" (ق و م), which is the untilted coin.

### E_F33 — supports
F33 | supports | 5:95, 48:25, 27:35 | The Quran uses the offering driven to the Kaʿba (5:95, 48:25) and the queen's gift sent to Solomon (27:35). The conveying and gift senses are attested in its own lemmas.

### E_F34 — supports
F34 | supports | 22:27 [staging], 22:28, 22:26, 5:2, 2:198 | 22:27–28 tell the season openly. Pilgrims come on foot and on lean mounts along every deep ravine road and mention God's name on known days over livestock: the name of 1:1, the known root of 1:2, the days of 1:4 and the livestock root of 1:7. 22:26 has those standing at the House, 5:2 the inviolable offering, and 2:198 the trade in season.

### E_F35 — shifts
F35 | shifts | 28:22 [same-word], 28:25 [staging], 28:27 | The Quran's road-to-marriage scene runs the other way. The traveller asks to be guided the even way, a woman walks toward him with composure (28:25), and the road ends in a marriage contract and years of service (28:27). The conveying stays and its direction shifts.

### E_F36 — shifts
F36 | shifts | 27:36, 49:17 [same-word], 14:7 | Solomon refuses a gift because what God gave him is better (27:36), and guidance is God's favour, not a return for the recipients' submission (49:17). This bounds the exchange away from bargain, while thanks answered with increase (14:7) keeps the circuit.

### E_F37 — supports
F37 | supports | 9:6 [staging], 3:97, 23:88 | 9:6 tells the refugee openly: a seeker of protection is protected and then conveyed to his place of safety. Whoever enters the House is safe (3:97), and He protects while none protects against Him (23:88).

### E_F38 — supports
F38 | supports | 11:56 [same-word], 36:71, 36:72, 20:18 [staging] | God holds every creature by the forelock (11:56). People are owners (mālikūn, 1:4's root) of livestock made tractable for them (36:71–72). A herder leans on his staff over his sheep (20:18).

### E_F39 — shifts
F39 | shifts | 6:90 [same-word], 43:22 [staging], 18:64 [staging], 4:69 | "Those are whom God guided, so follow their guidance" (6:90) endorses walking in predecessors' tracks. 43:22 tells the scene openly ("we are guided on our fathers' tracks") and rejects it when the fathers were not guided. 18:64 is the literal retracing of footprints, and 4:69 names whose tracks count.

### E_F40 — expands
F40 | expands | 67:30, 72:16, 13:17 | Water can sink away into the ground (67:30). Holding straight on the road is answered with abundant water (72:16). In 13:17 the foam goes and what benefits stays in the earth. Standing that still flows is the watered road.

### E_F41 — supports
F41 | supports | 25:45 [staging], 25:46 | The Lord stretches the shadow, makes the sun its indicator, then draws it in little by little. This is the shrinking shade toward the sun's full stand.

### E_F42 — supports
F42 | supports | 83:6 [staging], 78:38, 39:68 | People stand for the Lord of the worlds (83:6), the Spirit and angels stand in rows (78:38), and the dead rise standing and looking (39:68). The Day is told through the adjective's root.

### E_F43 — supports
F43 | supports | 3:39 [staging], 2:238, 22:26 | Zechariah's petition is answered "while he stood praying in the sanctuary" (3:39). Believers are told to stand for God devoutly (2:238), and the House is kept for those who stand (22:26).

### E_F44 — supports
F44 | supports | 83:3, 83:6, 57:25 | Those who short the measure (83:3) are asked whether they do not expect the Day people stand for the Lord of the worlds (83:6). Weight, valuation and the reckoning are one passage. The balance and standing with justice meet in 57:25.

### E_F45 — supports
F45 | supports | 4:5, 5:97, 25:67, 2:197 | Wealth is what God made for you as a qiyām, a mainstay (4:5). The Kaʿba is made a qiyām for people (5:97). The mean between excess and stint is a qawām (25:67). 2:197 shifts the road's provision: the best provision is God-consciousness.

### E_F46 — supports
F46 | supports | 13:33, 3:18, 4:135 | God stands over every soul for what it earned (13:33) and maintains justice (qāʾiman bi-l-qisṭ, 3:18). Believers are to be constant upholders of justice (4:135). The qayyim who keeps a people straight is here divine and delegated.

### E_F47 — expands
F47 | expands | 12:19 [staging] | Travellers halt at a well and send their water-drawer, who lets down his bucket. The Quran adds the halt on the road and the find that the well yields.

### E_F48 — supports
F48 | supports | 95:4, 82:7, 28:14, 48:29 [staging] | The human is formed in the best taqwīm (95:4) and made even and balanced (82:7). Moses reaches full strength and becomes even (istawā, 28:14). 48:29 tells the growth openly: a plant strengthened by its shoot thickens and stands even on its stems.

### E_F49 — supports
F49 | supports | 16:16, 25:45, 20:120 | Landmarks and stars indicate the way (16:16), and the sun is made the shadow's indicator (dalīl, 25:45). 20:120 bounds this: Satan also offers to "point the way", so indication needs the guide of 1:6.

### E_F62 — supports
F62 | supports | 3:8 [same-word], 20:123 | Those already guided pray not to be made to swerve after being guided (3:8), a petition that follows service as 1:6 follows 1:5. Whoever follows the guidance "will not stray" (20:123), which closes the hinge on guidance's defined opposite.

### Q1 — qeq
Q1 | qeq | words: 1:6:1 1:6:3 | branches: ه د ي B005; ق و م B009 | trigger: 5:97 (qeq) | with: F33 F34 F45 | shows: God made the Kaʿba a qiyām, a standing-support, for people, and names the offering and the garlanded animals with it. The conveyed offering and the upholding standing are one sanctuary's two faces.

### Q2 — qeq
Q2 | qeq | words: 1:6:1 1:6:3 | branches: ه د ي B001; ه د ي B007; ق و م B006; ع ل م B001 | trigger: 3:96 3:97 (qeq) | with: F29 F34 F37 | shows: the first House is "guidance for the worlds" (1:2's word), holds the Station of Abraham, makes whoever enters it safe, and is reached by a way. Guidance, station and sanctuary meet in one destination.

### Q3 — qeq
Q3 | qeq | words: 1:6:3 | branches: ق و م B013; ق و م B015; ق و م B010; ر ب ب B001 | trigger: 83:3 83:6 (qeq) | with: F32 F42 F44 | shows: the short-weighed coin and the Rising before the Lord of the worlds stand in one passage. Straightness as exact weight is answered by standing at the reckoning.

### Q4 — qeq
Q4 | qeq | words: 1:6:3 | branches: ق و م B021; ن ع م B005; ض ل ل B001 | trigger: 7:179 (qeq) | with: F24 F38 | shows: eyes that do not see, "like livestock, rather more astray". The whole-but-sightless eye, 1:7's herd root and its last word meet in one ayah.

### Q5 — qeq
Q5 | qeq | words: 1:6:1 | branches: ه د ي B005; ه د ي B006; ر ح م B001; ن ع م B005 | trigger: 19:85 19:86 (qeq) | with: F10 F34 F38 | shows: two conveyances on one Day. The God-fearing are escorted as an honoured delegation to al-Raḥmān, and the guilty are driven like a thirsting herd to the watering of Hell.

### Q6 — qeq
Q6 | qeq | words: 1:6:2 | branches: ص ر ط B001; ع ب د B005; ر ب ب B001 | trigger: 16:69 (qeq) | with: F19 F23 | shows: "the ways of your Lord, made tractable" gives the owner-named road and the surface trodden level (1:5's tadhlīl) in one phrase, walked by a creature under inspiration (16:68).

### Q7 — qeq
Q7 | qeq | words: 1:6:3 | branches: ق و م B008; ق و م B009; م ل ك B006 | trigger: 25:67 (qeq) | with: F22 F23 F45 | shows: qawām, the standing mean "between that", is the middle of the road (38:22) made into conduct.

### Q8 — qeq
Q8 | qeq | words: 1:6:3 | branches: ق و م B008; ق و م B011; ق و م B020; ع و ن B005 | trigger: 48:29 (qeq) | with: F16 F48 F57 | shows: assisted growth ends upright. The shoot strengthens the plant, which thickens (a Form X verb, beside 1:5's and 1:6's) and stands even on its stems.

### Q9 — qeq
Q9 | qeq | words: 1:6:1 1:6:3 | branches: ق و م B016; ق و م B021; ه د ي B008; ه د ي B001 | trigger: 34:14 (qeq) | with: F9 F15 F49 | shows: a body stands upright on its staff though dead, and only the creature eating the staff "indicates" (dalla) the death. This is upright standing without life, the arrested standing set against mustaqīm.

### Q10 — qeq
Q10 | qeq | words: 1:6:2 1:6:3 | branches: ق و م B008; ص ر ط B001 | trigger: 72:16 (qeq) | with: F40 F45 | shows: had they held straight (Form X) on the road, they would be given abundant water. The walker's steadiness is answered with sustaining flow.

### A1 — axis
A1 | axis | 37:118 [same-word], 4:68 [same-word], 48:20 [same-word] | The road as the second direct object without "to". 37:118 repeats the definite pair exactly, given to Moses and Aaron with the clarifying Book.

### A2 — axis
A2 | axis | 17:9 [same-word], 6:161 [same-word], 90:10 [same-word] | The verb's three constructions: with "to" (the most upright, 17:9), with ilā (6:161) and with a direct object (the two highlands, 90:10). They set 1:6's bare accusative within the Quran's range.

### A3 — axis
A3 | axis | 38:22 [same-word] | The only other occurrence of the same imperative has "to" and "the middle of the road", inside a plea for a just verdict.

### A4 — axis
A4 | axis | 7:16 [same-word] | The only other definite noun-and-adjective pair, addressed to God as "Your straight road". The definite road of the petition is God's own.

### A5 — axis
A5 | axis | 4:68 [same-word], 4:69 | The Quran's own specification of 1:7's favoured follows guidance to a straight road directly: prophets, the truthful, witnesses and the righteous, "excellent as companions" on the way.

### A6 — axis
A6 | axis | 5:60 | Those incurring God's wrath are called "most astray from the level of the road". Both of 1:7's contrary groups are defined against the road of 1:6.

### A7 — axis
A7 | axis | 3:51 [same-word], 36:61 [same-word] | The Quran's definition of the straight road is serving the one Lord.

### A8 — axis
A8 | axis | 6:151, 6:152, 6:153 [same-word] | The road is specified by the commandments just listed, then called "My straight road".

### A9 — axis
A9 | axis | 28:56 [same-word], 42:52 [same-word] | The Prophet guides "to a straight road" in the sense of showing it, but cannot guide whom he loves in the sense of bringing in. This explains why the petition is addressed to God.

### A10 — axis
A10 | axis | 41:17 [same-word] | Guidance as the way shown, which can be refused ("they preferred blindness to guidance"). It limits the verb's sense of mere showing.

### A11 — axis
A11 | axis | 3:8 [same-word], 47:17 | The already guided ask to be kept and are given more guidance. The imperative asks for continuance, not a first finding.

### A12 — axis
A12 | axis | 41:30, 11:112, 81:28 | The Form X verb of the adjective means holding straight continuously after confessing the Lord. The participle names an ongoing property.

### A13 — axis
A13 | axis | 36:4 [same-word], 43:43 [same-word] | Being "on" the straight road stands beside being guided "to" it, which marks the road as a state walked in.

### A14 — axis
A14 | axis | 16:9 | The straight direction of the way is God's charge, and some roads swerve. This is the plain sense of one definite road among many.

### A15 — axis
A15 | axis | 7:43 [same-word] | The answer to the plural petition, in the same plural at arrival: "God who guided us".

### A16 — axis
A16 | axis | 92:12, 2:213 [same-word] | Guidance rests on God, and He guides whom He wills to a straight road through disagreement. This supplies the petition's agent and the need it answers.

### I1 — image
The guided road and its fork
Role here: develop
Members for this treatment: 1:1:1 سمو B002 (beacon, a figure raised on the horizon) [1:1 F23]; 1:1:1 سمو B006 (departure into open land) [N-added, activated by 1:6:2 صرط]; 1:1:2 وله B001 (pressure: ground that bewilders whoever enters) [1:1 F38; 1:2 F24]; 1:2:4 علم B002 (guide: landmark that "guides to" its thing) [1:2 F8 F48]; 1:3:1/2 رحم B001 (the manner of leading, gentle) [1:3 F25]; 1:4:1 ملك B006 (the road's centreline and middle track) [1:4 F10; 1:6 F22; 1:7 F17 F34]; 1:4:3 دين B005 (habitual course, the standing dīn) [1:4 F26; 1:6 F21]; 1:5:2 عبد B005 (surface trodden level by use) [1:5 F5]; 1:6:1 هدي B001 B002 (guide; heading, and following predecessors' tracks) [1:6 F1 F3 F39 F55]; 1:6:2 صرط B001 (the road, owned by the Lord and Praised, the same road as serving the Lord) [1:6 F2 F18 F19 F20 F23 F56]; 1:6:3 قوم B008 (straightness) [1:6 F1 F2 F21]; 1:7:1 صرط B001 (conduit: the road now owned by the people who walked it) [1:7 F30 F47 F49 F53]; 1:7:3 نعم B007 B012 (the road named niʿāma; soles that wore it already) [1:7 F4 F5]; 1:7:5 غير B005 (the switch at the fork) [1:7 F47 F53]; 1:7:6 غضب B001 (reversal: those who turn back on the way loaded with wrath) [1:7 F28]; 1:7:9 ضلل B001 (loss: swerving from aim and road) [1:7 F16 F32 F35]
Movement: a raised figure and landmarks make the way readable. A gentle guide leads onto a surface levelled by service, down its middle. The road holds itself straight. 1:7 shows it already worn by the favoured and owned by them. At غير it forks: one party turns back carrying wrath, the other swerves off and is lost. The petition's first word (guide) and the surah's last (strayers) define each other, so the unit closes as a ring
Purpose: the spine of 1:5–7. The petition is a journey request whose object is a road, its company and its end, with the two failures named. Landmarks at 1:2 and the centreline at 1:4 lay the road before it is asked for
Disclosure: 1:1 meet (بِسْمِ, ٱللَّهِ); 1:2 touch (ٱلْعَٰلَمِينَ); 1:3 touch (ٱلرَّحِيمِ); 1:4 develop (مَٰلِكِ, ٱلدِّينِ); 1:5 touch (نَعْبُدُ); 1:6 develop (ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ); 1:7 assemble (صِرَٰطَ … غَيْرِ … ٱلضَّآلِّينَ)

### I1_M1 — meeting
I14 at 1:6:3 — the road's straightness and the walker's upright body share استواء

### I1_M2 — meeting
I22 at 1:6:2/1:7:1 — the road-word also carries out of sight

### I1_M3 — meeting
I18 at 1:6:2 — one road against many scattering ways

### I1_M4 — meeting
I9 at 1:6:3 — the road ends in a maqām

### I1_M5 — meeting
I7 at 1:6:1 — the only imperative asks for this road

### I1_M6 — meeting
I19 at 1:6:2 — the road besieged by those who sit in ambush

### I2 — image
Mark and its reader
Role here: assemble
Members for this treatment: 1:1:1 سمو B005 + وسم B001 B002 (source: the name raised as a banner and burned in as a brand; dalāla) [1:1 F2 F14 F15]; 1:1:1 وسم B005 B006 (a face that carries its mark: grace, dye) [1:1 F16 F36]; 1:1:1 وسم B002 (the reader's discernment) [1:1 F45]; 1:2:4 علم B001 B002 B003 (the worlds as marks, the instrument of knowing; ʿālamīn/ḍāllīn rhyme) [1:2 F12 F32 F33 F52]; 1:2:3 ربب B003 (the rabbānī teacher who raises knowers) [1:2 F3 F44]; 1:4:2 يوم B004 (days kept in remembrance) [N-added, activated by 1:7:9 ضلل B004]; 1:5:4 عين~echo B003 (the guarding eye) [1:5 F35 F37]; 1:6:1 هدي B001 (guidance as gentle indication, the knower's credential) [1:6 F4 F31 F49]; 1:6:1 هدي B009 (the dull reader who cannot hold the way) [1:6 F50]; 1:6:3 قوم B021 (loss: an eye intact but sightless, 36:66) [1:1 F45; 1:6 F24]; 1:7:3 نعم B013 B007 (the eye's delight; niʿāma visible on the mountaintop) [1:7 F10 F39]; 1:7:6 غضب B005 B006 (a swollen lid, thick red skin) [1:7 F10 F44]; 1:7:9 ضلل B002 B004 (loss: gone from sight, gone from memory) [1:7 F10 F39]
Movement: the name and the worlds point. A seeing, knowing reader follows the pointing and is guided. The failures are the blind-but-whole eye, the dull man, the hidden thing and the forgotten. At the close, faces become marks to be read: delight, swelling, absence
Purpose: 1:1–2 set out two marks read in sequence. 1:6 asks to be led along what they point to. 1:7 sorts people by what is visible on them and by what has vanished
Disclosure: 1:1 meet (بِسْمِ); 1:2 develop (رَبِّ ٱلْعَٰلَمِينَ); 1:4 touch (يَوْمِ); 1:5 touch (نَسْتَعِينُ); 1:6 assemble (ٱهْدِنَا … ٱلْمُسْتَقِيمَ); 1:7 develop (أَنْعَمْتَ, ٱلْمَغْضُوبِ, ٱلضَّآلِّينَ)

### I2_M1 — meeting
I20 at 1:6:3 — noon's full visibility set against ḍalla's hiding

### I3 — image
The herd under its owner, and the stray whose lord is unknown
Role here: touch
Members for this treatment: 1:6:1 هدي B003 (guide: the foremost one, neck first; 1:6:3 قوم B020 (the legs it walks on) [1:6 F13]
Movement: the herd is gathered and owned, branded, and led from the front, and it follows. Hunt and flight scatter it. One animal falls out, its mark no longer read and its lord unknown. The brand and the owner are what could bring it back, and the mother's cry is the search
Purpose: gives the last word its picture. The lost are those who no longer know the Rabb that 1:2 named; the favoured are the kept herd
Disclosure: 1:1 meet (بِسْمِ); 1:2 develop (رَبِّ ٱلْعَٰلَمِينَ); 1:3 touch (ٱلرَّحِيمِ); 1:4 develop (مَٰلِكِ); 1:5 touch (نَعْبُدُ, نَسْتَعِينُ); 1:6 touch (ٱهْدِنَا); 1:7 assemble (أَنْعَمْتَ … ٱلضَّآلِّينَ)

### I4 — image
The womb that holds and the tie that can be cut
Role here: touch
Members for this treatment: 1:3:1/2 رحم B004 + 1:6:3 قوم B019 B020 + 1:7:6 غضب B006 (the cost: a ewe sick after lambing) [1:1 F18; 1:6:1 هدي B001 (release: the one who knows the way leads the lost back) [1:1 F6]
Movement: the womb holds, the kin bond is named from it, the heart softens and pays. The tie can be cut by sale, by captivity or by the Day. The young strays, the mother searches, and the guide leads it back. The mercy names are the mother's side of that search
Purpose: sets mercy at the opening as a holding, so that the strayers at the close are heard as young lost from the one who holds them
Disclosure: 1:1 meet (ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ); 1:2 touch (رَبِّ); 1:3 assemble (ٱلرَّحْمَٰنِ ٱلرَّحِيمِ); 1:4 touch (يَوْمِ); 1:6 touch (ٱهْدِنَا, ٱلْمُسْتَقِيمَ); 1:7 develop (أَنْعَمْتَ, ٱلْمَغْضُوبِ, ٱلضَّآلِّينَ)

### I5 — image
Formed, reared, stood up
Role here: assemble
Members for this treatment: 1:1:3 رحم B003 (container: the womb shapes the form, 3:6) [1:1 F29; 1:3 F12]; 1:1:1 سمو B005 + 1:4:2 يوم B002 (the named term of the stay) [1:3 F13]; 1:2:3 ربب B002 B009 B005 B003 (staged rearing from freshness to completion; rabā growth) [1:2 F14 F16 F37 F51]; 1:2:1 حمد B004 (the praised limit that completion reaches) [1:2 F16]; 1:5:4 عون B002 B005 B007 + 1:5:2 عبد B007 (the markers of maturity) [1:3 F28; 1:5 F21]; 1:7:5 غير B003 (form altered) [1:3 F12]; 1:6:3 قوم B011 B002 (finished stature, rising upright) [1:3 F12]; 1:4:2 يوم B003 (the Day as labour) [1:4 F30]; 1:6:3 قوم B013 (release: rising) [1:1 F29; 1:4 F30]; 1:7:9 ضلل B002 + 1:7:6 غضب B002 (burial; anger on behalf of the dead) [1:7 F42]
Movement: shaped in the womb, reared stage by stage, grown to an upright stature, buried, then brought up out of the earth on the Day as out of a womb
Purpose: binds the mercy names, the Day of 1:4 and the upright road of 1:6 into one life arc
Disclosure: 1:1 meet (ٱلرَّحِيمِ); 1:2 develop (رَبِّ); 1:3 develop (ٱلرَّحِيمِ); 1:4 touch (يَوْمِ); 1:5 touch (نَسْتَعِينُ); 1:6 assemble (ٱلْمُسْتَقِيمَ); 1:7 touch (ٱلضَّآلِّينَ)

### I5_M1 — meeting
I21 at 1:6:3 — the qiyāma

### I5_M2 — meeting
I14 at 1:6:3 — the standing body

### I7 — image
The name worshipped, turned to "You"
Role here: develop
Members for this treatment: 1:1:1 سمو B005 (a name whose verb is never spoken; name, worship and womb defining one another) [1:1 F13 F39]; 1:1:2 ءله B001 (source: the worshipped one, defined by taʿabbud) [1:1 F12; 1:2 F4]; 1:1:2 وله B001 (the yearning pull) [1:1 F4]; 1:1:2 ءله B002 (vocative allāhumma, the address the name permits) [1:1 F28 F41; 1:2 F39]; 1:2:1 حمد B006 (unowned praise that draws in a co-praiser) [1:2 F10 F31]; 1:2:3 ربب B001 (restating the name) [1:2 F1]; 1:3:1/2 رحم B001 (definite titles in the genitive chain; a ring from name to praised; mercy that makes asking possible) [1:3 F2 F3 F26]; 1:4:1 ملك (the last third-person link) [1:4 F44]; 1:4:3 دين B001 (obedience enacted now) [1:4 F36]; 1:5:1/3 إيّاك + 1:5:2 عبد B003 B002 + 1:5:4 عون B001 (fronted, repeated exclusivity; service; direct petition, open until filled) [1:5 F1 F11 F26 F29 F32 F34]; 1:6:1 هدي B001 (the only imperative; the plural نا) [1:6 F58 F62]; 1:7:3 نعم B001 (second person continues: "You favoured") [N-added, activated by 1:6:1]
Movement: a name is spoken with its verb withheld, and the name is the worshipped one. Praise, owned by no speaker, runs as one genitive chain through Rabb, Raḥmān, Raḥīm and Mālik. Then comes a sudden fronted "You". Service is given, then help is asked of Him directly, not as a means. The open request is filled by "guide us", and the address carries into "You favoured"
Purpose: carries the surah's turn from speaking of God to speaking to Him
Disclosure: 1:1 meet (بِسْمِ ٱللَّهِ); 1:2 develop (ٱلْحَمْدُ لِلَّهِ رَبِّ); 1:3 touch (ٱلرَّحْمَٰنِ ٱلرَّحِيمِ); 1:4 touch (مَٰلِكِ, ٱلدِّينِ); 1:5 assemble (إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ); 1:6 develop (ٱهْدِنَا); 1:7 touch (أَنْعَمْتَ)

### I7_M1 — meeting
I1 at 1:6:1

### I8 — image
Water held and water lost
Role here: touch
Members for this treatment: 1:6:3 قوم B016 B012 (water standing frozen; 1:6:2 صرط B002 (swallowed away) [1:6 F40]
Movement: sky, then cloud, then rain that marks the earth, gathered in a well, carried by the traveller, drawn up by the frame, watering the land into green. It fails two ways: let loose it runs off and vanishes; stopped, it stands frozen. At the close, "upon them" is shade and rain
Purpose: gives mercy and favour a weather body, and sets a sustaining flow against a flow that is lost
Disclosure: 1:1 meet (بِسْمِ, ٱللَّهِ); 1:2 develop (رَبِّ ٱلْعَٰلَمِينَ); 1:3 touch (ٱلرَّحْمَٰنِ ٱلرَّحِيمِ); 1:4 assemble (مَٰلِكِ); 1:5 touch (نَسْتَعِينُ); 1:6 touch (ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ); 1:7 develop (أَنْعَمْتَ … غَيْرِ … ٱلضَّآلِّينَ)

### I8_M1 — meeting
I14 at 1:6:3 — the standing that moves against the standing that freezes

### I9 — image
The station found good and stayed in
Role here: develop
Members for this treatment: 1:2:1 حمد B002 (verdict: the site found fit) [1:2 F17]; 1:2:3 ربب B007 (staying on, defined by iqāma) [1:2 F7 F17; 1:6 F6]; 1:2:4 علم B005 B002 (the well; the mountain steered by) [1:2 F17]; 1:4:1 ملك B006 B007 (the settlement's main quarter; water as mainstay) [1:2 F18; 1:4 F11]; 1:4:3 دين B006 (container: the city where obedience is made to stand) [1:4 F7 F11 F12]; 1:4:2 يوم B002 (the era of a reign) [1:4 F12]; 1:5:4 عون B008 (a named locality) [1:5 F23]; 1:6:3 قوم B006 B009 (maqām; what keeps life standing; the abode of peace, 10:25) [1:6 F7 F29 F45]; 1:7:3 نعم B011 (release: a place found agreeable to stay) [1:6 F7; 1:7 F6]; 1:7:5 غير B001 (provisioning) [1:2 F18; 1:6 F45]; 1:7:9 ضلل B003 B005 (loss: cannot find even a fixed place; the stray outside the camp) [1:2 F18; 1:7 F6]
Movement: travellers steer by a landmark to water, find the place good, and stay. The city is where obedience stands. The road's end is a dwelling, and the favoured are those who found the station good; the other ending cannot locate any place
Purpose: gives the road an arrival and gives 1:7's favoured a settled end
Disclosure: 1:2 meet (ٱلْحَمْدُ … رَبِّ ٱلْعَٰلَمِينَ); 1:4 develop (مَٰلِكِ يَوْمِ ٱلدِّينِ); 1:5 touch (نَسْتَعِينُ); 1:6 develop (ٱلْمُسْتَقِيمَ); 1:7 assemble (أَنْعَمْتَ … غَيْرِ … ٱلضَّآلِّينَ)

### I9_M1 — meeting
I1 at 1:6:3 — the straight road ends in the standing root's maqām

### I10 — image
Soft and hardened under the same "upon them"
Role here: touch
Members for this treatment: 1:6:1 هدي B001 B010 (gentle leading
Movement: tenderness is named in full as God's own and passes into gentle guidance and a smoothed road. At the close the same "upon them" lands on a yielding skin and on a hide thickened into a shield. Each side grows by accumulation, favour completed and wrath heaped. The agent of wrath is left unnamed
Purpose: bookends the surah between a soft pole named and a hardening left agentless, so the pull toward mercy is asymmetric
Disclosure: 1:1 meet (ٱلرَّحْمَٰنِ ٱلرَّحِيمِ); 1:3 develop (ٱلرَّحْمَٰنِ ٱلرَّحِيمِ); 1:4 touch (مَٰلِكِ); 1:5 touch (نَعْبُدُ); 1:6 touch (ٱهْدِنَا); 1:7 assemble (أَنْعَمْتَ عَلَيْهِمْ … ٱلْمَغْضُوبِ عَلَيْهِمْ)

### I11 — image
Favour's circuit: mercy out, praise back
Role here: touch
Members for this treatment: 1:6:1 هدي B001 (guidance as the form favour takes, 48:2) [1:6 F28]
Movement: mercy overflows and reaches its recipient. The Rabb tends it to completion, and it arrives as favour upon the guided. It returns as praise owned by Allah, so no creature keeps the credit. Forgetting breaks the return
Purpose: the surah's economy of good. 1:2's praise answers 1:7's favour before that favour is named
Disclosure: 1:1 meet (ٱلرَّحْمَٰنِ ٱلرَّحِيمِ); 1:2 develop (ٱلْحَمْدُ … رَبِّ); 1:3 develop (ٱلرَّحْمَٰنِ ٱلرَّحِيمِ); 1:4 touch (يَوْمِ); 1:5 touch (نَسْتَعِينُ); 1:6 touch (ٱهْدِنَا); 1:7 assemble (أَنْعَمْتَ)

### I11_M1 — meeting
I16 at 1:6:1 — praise presented and a gift asked

### I12 — image
Credit run to its named term
Role here: develop
Members for this treatment: 1:1:1 سمو B005 (a named term, ajal musammā, 2:282) [1:1 F26]; 1:2:1 حمد B005 + 1:2:3 ربب B016 + 1:7:3 نعم B001 B004 (favour as a claim; "yes" as a promise) [1:4 F25]; 1:4:1 ملك B002 (the creditor-owner) [1:4 F24]; 1:4:2 يوم B001 B002 (the span and the due date) [1:4 F24]; 1:4:3 دين B003 B002 (debt; requital, madīnūn) [1:4 F24 F33]; 1:5:4 عين~echo cash/credit + عون B001 + 1:5:2 عبد B001 (help sought from the creditor; the slave as a priced good) [1:5 F38]; 1:6:3 قوم B010 B015 B018 B007 (valuation, the full-weight coin, the straight balance, the market, the substitute) [1:6 F32 F44]; 1:7:5 غير B005 (ghayr madīnīn, 56:86) [1:4 F33]; 1:7:9 ضلل B003 B005 (loss: the stray asset, the claim unredressed) [1:6 F44]
Movement: a debt is contracted to a named term and the span runs. Value is fixed by a true coin, the due day arrives, and the owner settles. Help to pay is asked of the creditor himself, and favour conferred is what is repaid
Purpose: lets 1:4 be heard as a settlement of what was lent, so straightness also means exact weight
Disclosure: 1:1 meet (بِسْمِ); 1:2 touch (ٱلْحَمْدُ, رَبِّ); 1:4 assemble (مَٰلِكِ يَوْمِ ٱلدِّينِ); 1:5 touch (نَسْتَعِينُ); 1:6 develop (ٱلْمُسْتَقِيمَ); 1:7 touch (أَنْعَمْتَ, غَيْرِ, ٱلضَّآلِّينَ)

### I12_M1 — meeting
I13 at 1:6:3 — substitution, blood-money as payment

### I13 — image
Blood answered
Role here: touch
Members for this treatment: 1:6:3 قوم B007 (one standing in another's place) [1:6 F44]
Movement: a killing, then anger rising for the dead. Either a substitute is accepted or the blood stays lost, and the day of requital settles every open claim
Purpose: hears the tail of 1:7 as the outcomes of a feud, with unredressed loss answered on the Day
Disclosure: 1:4 meet (يَوْمِ ٱلدِّينِ); 1:5 touch (نَعْبُدُ); 1:6 touch (ٱلْمُسْتَقِيمَ); 1:7 assemble (صِرَٰطَ … غَيْرِ ٱلْمَغْضُوبِ … ٱلضَّآلِّينَ)

### I13_M1 — meeting
I12 at 1:6:3 — substitution as payment

### I14 — image
Halted, leaning, standing up again
Role here: assemble
Members for this treatment: 1:1:1 سمو B004 (the mount's back) [1:1 F37]; 1:2:3 ربب B016 + 1:4:1 ملك B001 + 1:5:2 عبد B007 (knot, cohesion, solidity) [1:2 F50; 1:5 F24]; 1:4:1 ملك B005 B008 (the pillar leaned on; the forelegs that steer) [1:4 F17 F28]; 1:5:2 عبد B011 (pressure: the mount breaks down and the rider is stranded) [1:5 F3 F4 F18]; 1:5:4 عون B001 B005 (release: help as strength that catches up, 18:95) [1:5 F2 F3 F30]; 1:5:2 عبد B005 B009 (levelled; the resumed quick pace) [1:5 F6 F42]; 1:6:1 هدي B008 (a swaying walk leaning on companions or a staff) [1:6 F15 F16]; 1:6:3 قوم B009 B012 (the pillar; the upright member) [1:4 F28; 1:5 F24]; 1:6:3 قوم B002 B003 B008 B011 (upright, resolve, evenness, stature; the prayer-stance; the upright gait of 67:22; the self-upholding Form X) [1:6 F9 F25 F43 F48 F53 F57]; 1:6:3 قوم B016 B019 B020 B021 (loss: standing arrested; halted, pained, lamed, blind) [1:6 F9 F16 F52]; 1:7:3 نعم B012 (going on foot) [1:7 F3]; 1:7:5 غير B001 (gear repaired at the halt) [1:7 F3]; 1:7:9 ضلل B005 (the mount gone) [1:7 F3]
Movement: the mount breaks down and the rider halts. He walks swaying, leaning on companions and a staff, and a pillar bears the weight. Help comes as strength catching up. The body evens out and stands. The road's own participle is a standing that holds itself up and keeps moving, answering nastaʿīn in the same verb form, and the reciter asks for it standing
Purpose: makes 1:5→1:6 one movement: stranded, leaning, set upright on a road that itself stands
Disclosure: 1:1 meet (بِسْمِ); 1:2 touch (رَبِّ); 1:4 develop (مَٰلِكِ); 1:5 develop (نَعْبُدُ نَسْتَعِينُ); 1:6 assemble (ٱهْدِنَا … ٱلْمُسْتَقِيمَ); 1:7 touch (أَنْعَمْتَ, غَيْرِ, ٱلضَّآلِّينَ)

### I14_M1 — meeting
I1 at 1:6:3 — the straight road and the upright walker

### I14_M2 — meeting
I8 at 1:6:3 — frozen water

### I14_M3 — meeting
I5 at 1:6:3 — stature

### I15 — image
The bride conveyed, the household formed and guarded
Role here: assemble
Members for this treatment: 1:1:3/1:3:1 رحم B002 B003 (the kin circle, the womb) [1:1 F32; 1:3 F5 F18]; 1:2:3 ربب B005 B002 (the foster carer; rearing) [1:2 F28; 1:3 F5]; 1:4:1 ملك B004 (source: the marriage contract) [1:3 F5; 1:4 F18]; 1:5:2 عبد B007 (the firmness of defence) [1:3 F18]; 1:5:4 عون B002 (a woman who has been married) [1:5 F44]; 1:6:1 هدي B006 B008 B010 B004 (conduit: the bride conveyed, swaying and unhurried; gifts) [1:4 F18; 1:6 F35; 1:7 F13]; 1:6:3 قوم B004 B001 (the guardian; the kin company) [1:1 F32; 1:2 F28]; 1:7:3 نعم B013 B011 (the eye's delight; a house she finds good to stay in) [1:6 F35; 1:7 F13]; 1:7:5 غير B004 B001 (jealous guarding of the boundary; provisioning) [1:3 F18; 1:7 F12]; 1:7:6 غضب B001 B007 (the heated anger of guarding) [1:7 F12]
Movement: a contract is made and the bride is conveyed along a road to a house. Kinship and the womb follow, then rearing and fostering. A guardian keeps the household, jealousy guards its boundary, and provision feeds it
Purpose: a domestic reading of the petition: "convey us, as a bride is conveyed," to a dwelling where one is kept
Disclosure: 1:1 meet (ٱلرَّحِيمِ); 1:2 touch (رَبِّ); 1:3 develop (ٱلرَّحْمَٰنِ ٱلرَّحِيمِ); 1:4 touch (مَٰلِكِ); 1:5 touch (نَعْبُدُ, نَسْتَعِينُ); 1:6 assemble (ٱهْدِنَا … ٱلْمُسْتَقِيمَ); 1:7 develop (أَنْعَمْتَ … غَيْرِ ٱلْمَغْضُوبِ)

### I15_M1 — meeting
I1 at 1:6:1 — guidance heard as conveyance along a road

### I15_M2 — meeting
I16 at 1:6:1 — sending

### I16 — image
Sent to its destination: gift, offering, season
Role here: assemble
Members for this treatment: 1:1:1 وسم B004 B001 (a marked season; livestock branded) [1:1 F10 F14; 1:6 F34]; 1:1:2 ءله B001 (the destination: the worshipped one) [1:1 F10]; 1:1:1 سمو B004 + 1:4:1 ملك B009 (a messenger sent from above) [1:1 F35; 1:4 F19]; 1:2:1 حمد B006 (praise presented like a poem) [1:6 F36]; 1:5:2 عبد B003 (worship fixes where the thing is sent) [1:5 F27]; 1:5:4 عون B001 (mutual help beside the offering, 5:2) [1:5 F47]; 1:6:1 هدي B004 B005 B007 B011 (conduit: gift, offering to the House, the sanctity it lends, presenting verse) [1:6 F10 F33 F36]; 1:6:3 قوم B001 B006 B018 (companies, station, market) [1:6 F34]; 1:7:3 نعم B005 (livestock driven) [1:6 F34]
Movement: things are selected and sent toward the one they are for: the offering to the House, the gift to the beloved, the messenger from above. People gather at the marked season. Praise is sent up and favour is asked down
Purpose: hears "guide us" also as "send us": the speakers ask to be conveyed where they belong
Disclosure: 1:1 meet (بِسْمِ ٱللَّهِ); 1:2 touch (ٱلْحَمْدُ); 1:4 touch (مَٰلِكِ); 1:5 develop (نَعْبُدُ … نَسْتَعِينُ); 1:6 assemble (ٱهْدِنَا … ٱلْمُسْتَقِيمَ); 1:7 touch (أَنْعَمْتَ)

### I16_M1 — meeting
I15 at 1:6:1 — bride and offering share one conveying verb

### I16_M2 — meeting
I11 at 1:6:1 — the exchange of gifts

### I16_M3 — meeting
I17 at 1:6:1 — the offering's sanctity reaches the protected client

### I17 — image
Bound by the name: oath, pact, protected client
Role here: assemble
Members for this treatment: 1:1:2 ءله B002 (source: the name sworn) [1:1 F42; 1:2 F43]; 1:2:3 ربب B011 B016 (the pact; the tight knot) [1:2 F43; 1:3 F27]; 1:3:1 رحم B002 (asking one another by God and by the wombs, 4:1) [1:3 F11]; 1:4:3 دين B007 (being left to one's own sworn word) [1:4 F41]; 1:5:4 عون B001 (release: not left to oneself) [1:4 F41]; 1:5:2 عبد B001 B004 (one under dominion asking to be taken in) [1:6 F37]; 1:6:1 هدي B007 (the protected refugee, or the captive) [1:2 F43; 1:6 F37]; 1:7:3 نعم B004 (the "yes" that seals) [1:4 F41]
Movement: the name is sworn and a pact binds. The speaker, instead of being left to his own word, asks for backing and is taken in, as a client under covenant rather than a captive led. Assent seals it
Purpose: the invocation of 1:1 binds, and the petition asks for protected standing
Disclosure: 1:1 meet (ٱللَّهِ); 1:2 develop (رَبِّ); 1:3 touch (ٱلرَّحِيمِ); 1:4 touch (ٱلدِّينِ); 1:5 touch (نَعْبُدُ نَسْتَعِينُ); 1:6 assemble (ٱهْدِنَا); 1:7 touch (أَنْعَمْتَ)

### I17_M1 — meeting
I6 at 1:6:1 — captive or client

### I17_M2 — meeting
I16 at 1:6:1 — sanctity

### I18 — image
One company held, or scattered
Role here: assemble
Members for this treatment: 1:2:3 ربب B004 B010 B013 B014 B016 (container: the many gathered and held; the ribbiyyūn) [1:2 F13 F47]; 1:2:3 ربب B015 (fewness set between two totalities) [1:2 F45]; 1:2:4 علم B003 (the kinds and peoples) [1:2 F47; 1:3 F29]; 1:3:1 رحم B002 (kinship widened to creation) [1:3 F29]; 1:5:2 عبد B002 B010 (God's people; bands scattering; the plural "we") [1:5 F16 F28 F33]; 1:5:4 عون B001 + عين~echo B015 (mutual aid; notables and brothers) [1:5 F16 F41]; 1:6:1 هدي B010 (the composed walker set against a frantic rout) [1:6 F17]; 1:6:2 صرط B001 (one road against the ways that scatter, 6:153) [1:6 F27; 1:7 F33]; 1:6:3 قوم B001 B004 (the company; the qayyim who keeps it straight) [1:6 F27 F46]; 1:7:3 نعم B008 (loss: ostrich-flight, the qawm scattering) [1:7 F18 F33]; 1:7:9 ضلل B001 (swerving off) [1:7 F33]
Movement: many kinds are gathered and held by the Rabb. A plural "we" speaks, held together by one addressee and mutual aid, and walks one road under a guardian. The danger is rout, with bands flying off down many ways
Purpose: the "we" of 1:5–6 is what the petition keeps together
Disclosure: 1:2 meet (رَبِّ ٱلْعَٰلَمِينَ); 1:3 touch (ٱلرَّحِيمِ); 1:5 develop (نَعْبُدُ نَسْتَعِينُ); 1:6 assemble (ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ); 1:7 develop (أَنْعَمْتَ … ٱلضَّآلِّينَ)

### I18_M1 — meeting
I1 at 1:6:2

### I19 — image
Contest: backing, blade against shield, ambush, rout
Role here: assemble
Members for this treatment: 1:1:1 سمو B007 (rivalry) [N-added, activated by 1:4:2 يوم B003]; 1:4:2 يوم B003 (the battle-day) [1:4 F22; 1:5 F19]; 1:5:4 عون B003 B001 (a war fought again; the backer standing behind) [1:4 F22; 1:5 F19]; 1:5:2 عبد B007 (the defender's firmness) [1:5 F43]; 1:6:2 صرط B003 + 1:6:3 قوم B012 + 1:6:1 هدي B003 (blade, hilt, arrowhead) [1:6 F12]; 1:6:2 صرط B001 (pressure: the road besieged by those who sit in wait, 7:16, 7:86) [1:6 F26]; 1:6:3 قوم B014 (mutual resistance) [1:4 F22; 1:6 F26]; 1:7:6 غضب B003 B004 B008 (defiance; rock; the shield-hide) [1:5 F19 F43; 1:6 F12]; 1:7:3 نعم B008 + 1:5:2 عبد B010 (loss: the rout) [1:4 F22]
Movement: rivalry turns into repeated war. Backing is sought, the blade meets the shield, ambushers sit on the road, and the losers are routed
Purpose: help is heard as backing in a fight, and the road as held against opposition
Disclosure: 1:1 meet (بِسْمِ); 1:4 develop (يَوْمِ); 1:5 develop (نَعْبُدُ نَسْتَعِينُ); 1:6 assemble (ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ); 1:7 touch (أَنْعَمْتَ, ٱلْمَغْضُوبِ)

### I19_M1 — meeting
I1 at 1:6:2 — the road is contested

### I20 — image
The day fixed by what stands overhead
Role here: develop
Members for this treatment: 1:1:1 سمو B002 B004 + وسم B004 (a crescent rising into view; the sky; the season it marks) [1:1 F24]; 1:1:2 ءله B001 (ilāha, the sun that was worshipped) [1:1 F34; 1:2 F25]; 1:2:4 علم B002 (a sign) [1:4 F38]; 1:4:2 يوم B001 B002 (container: bounded daylight) [1:4 F38]; 1:5:4 عين~echo B008 (the sun's disc) [1:5 F40]; 1:6:3 قوم B017 (the noon stand, when shadow nearly vanishes) [1:6 F41]; 1:7:9 ضلل B002 (hiding, set against noon's visibility) [1:6 F41]
Movement: the crescent rises and marks a season. The sun makes the day and stands at noon. Worship passes over the body standing overhead to its Rabb
Purpose: sets the Day of 1:4 among ordinary days and separates the worshipped from what shines
Disclosure: 1:1 meet (بِسْمِ ٱللَّهِ); 1:2 touch (لِلَّهِ … ٱلْعَٰلَمِينَ); 1:4 assemble (يَوْمِ); 1:5 touch (نَسْتَعِينُ); 1:6 develop (ٱلْمُسْتَقِيمَ); 1:7 touch (ٱلضَّآلِّينَ)

### I20_M1 — meeting
I2 at 1:6:3 — visibility against hiding

### I21 — image
The Day the King sits and creation stands
Role here: develop
Members for this treatment: 1:1:1 وسم B004 + 1:2:4 علم B001 (the appointed, known day of gathering, 56:50) [1:4 F40]; 1:2:4 علم B002 + 1:6:3 قوم B013 (a signpost for the Hour, 43:61) [1:6 F30]; 1:3:1/2 رحم B001 B002 (mercy frames the account; wombs will not avail; kingship that day belongs to al-Raḥmān) [1:3 F9 F10; 1:4 F34 F35]; 1:4:1 ملك B003 B002 (source: the king who sits; owner of the day and of its affairs; ownership withdrawn from all others, 82:19) [1:4 F1 F32 F45]; 1:4:2 يوم B003 B004 B005 (container: a day filled and named by its event; God's days of favour and of blows) [1:4 F4 F9; 1:7 F20]; 1:4:3 دين B002 [1:4 F1 F32]; 1:1:2 وله B002 (ties cut on that day) [1:4 F29]; 1:4:1 ملك B009 + 1:6:3 قوم B013 B002 B016 (angels standing in rows; the dead rising; a silent standing assembly) [1:4 F20 F21; 1:6 F8 F42]; 1:7:3 نعم B001 + 1:7:6 غضب B001 + 1:7:9 ضلل B003 (release/loss: the two outcomes, given as persons) [1:4 F9; 1:7 F20]
Movement: one day, named wholly by its content. The King sits, the dead rise and stand, and the angels stand in rows. Every other hand lets go and ties are cut, except mercy's. The day holds both favour and blows, and 1:7 fills them with persons
Purpose: the pivot. Third-person praise ends at the Owner of the Day and the speakers turn to address Him
Disclosure: 1:1 meet (بِسْمِ); 1:2 touch (ٱلْعَٰلَمِينَ); 1:3 develop (ٱلرَّحْمَٰنِ ٱلرَّحِيمِ); 1:4 assemble (مَٰلِكِ يَوْمِ ٱلدِّينِ); 1:6 develop (ٱلْمُسْتَقِيمَ); 1:7 touch (أَنْعَمْتَ … ٱلْمَغْضُوبِ … ٱلضَّآلِّينَ)

### I21_M1 — meeting
I5 at 1:6:3 — rising

### I22 — image
The passage that takes in and carries out of sight
Role here: develop
Members for this treatment: 1:3:1 رحم B003 (the one enclosure that holds in order to bring forth) [1:3 F14]; 1:6:1 هدي B003 (the neck as channel) [1:6 F14]; 1:6:2 صرط B001 B002 B003 (conduit: road, throat and blade as one passing-through) [1:6 F11; 1:7 F25]; 1:7:1 صرط B003 (the blade; Turkish sırat "sharper than a sword") [1:6 F61; 1:7 F50]; 1:7:3 نعم B006 (the ostrich of the open field) [1:3 F14]; 1:7:6 غضب B007 B003 (pressure: the great serpent across the road; Jonah going off contending, 21:87) [1:7 F9 F29]; 1:7:9 ضلل B002 B005 (loss: buried, dissolved, gone; the unhoused stray outside every enclosure) [1:3 F14; 1:6 F14; 1:7 F9 F29]
Movement: road, throat and blade all pass something through until it is out of sight. A serpent lying across the road swallows whoever passes. Jonah went off contending and was swallowed. ḍalla sinks the lost into earth or medium. Only the womb holds in order to bring forth
Purpose: the tail of 1:7 ends in disappearance; the owned road of the favoured is set against the passage that swallows
Disclosure: 1:3 meet (ٱلرَّحِيمِ); 1:6 develop (ٱهْدِنَا ٱلصِّرَٰطَ); 1:7 assemble (صِرَٰطَ … ٱلْمَغْضُوبِ … ٱلضَّآلِّينَ)

### I22_M1 — meeting
I1 at 1:6:2 — the danger lives inside the road-word itself, so whose road it is decides whether passing out of sight means arrival or loss

### I23 — image
The coated hull under its captain
Role here: touch
Members for this treatment: 1:6:1 هدي B001 B010 (guidance asked; 1:6:3 قوم B008 (holding the course straight) [1:2 F19]
Movement: the hull is coated and the gear mended. The captain steers over the sea by a mountain seen from afar, a soft wind carries the ship, guidance is asked, and the course is held straight
Purpose: a sea reading of 1:2 and 1:6, with the Rabb as the one who keeps and steers the vessel
Disclosure: 1:1 meet (بِسْمِ); 1:2 assemble (رَبِّ ٱلْعَٰلَمِينَ); 1:4 touch (مَٰلِكِ); 1:5 develop (نَعْبُدُ نَسْتَعِينُ); 1:6 touch (ٱهْدِنَا … ٱلْمُسْتَقِيمَ); 1:7 touch (أَنْعَمْتَ … غَيْرِ)

### I23_M1 — meeting
I1 at 1:6:3 — the course is the road

### I25 — image
Set apart from its other
Role here: touch
Members for this treatment: 1:6:1 → 1:7:3 نعم B004 (a "yes" answering the petition) [1:6 F51]; 1:6:3 قوم B007 (standing in another's place) [1:6 F5]
Movement: a mark sets a thing apart from its other. "You" is singled out, twice. The middle stands between excluded ends. At the close the hearer hears yes, then an exception, then no, and the Day does the final sorting
Purpose: carries the surah's operation of distinguishing, begun among the worlds and completed in 1:7
Disclosure: 1:2 meet (ٱلْعَٰلَمِينَ); 1:4 develop (مَٰلِكِ يَوْمِ ٱلدِّينِ); 1:5 develop (إِيَّاكَ … نَسْتَعِينُ); 1:6 touch (ٱهْدِنَا, ٱلْمُسْتَقِيمَ); 1:7 assemble (أَنْعَمْتَ … غَيْرِ … وَلَا)

QeQ tags describe evidence, not obligations. A same-word passage may provide a decisive definition; a staging passage may duplicate another. Preserve the explanatory job and real counter-evidence. The full source records above remain available even when a passage is not quoted.


===== dictionary.md =====
# dictionary.md — every branch of every root of 1:6's words

One line per branch: Bnnn | gloss | Arabic image | definition | first classical source phrase.
`~alt` = a cited alternative analysis of the word; `~echo` = a sound-family root (not the word's root).
Cite a branch as `root Bnnn`, e.g. `ر ب ب B007`; its Arabic may be quoted with that source.

### ه د ي — 1:6 w1 ٱهْدِنَا
- B001 doğru yolu gösterme ve doğruya yönelme | دلالة بلطف إلى الطريق والحق | Bir kimseye yolu, doğruyu ya da benimsenmesi gereken yönü incelikle göstermek ve tanıtmak; gösterilen yönü kabul ederek doğruya ulaşmak, ayrıca bunun ilahi başarı desteğiyle gerçekleşmesidir. | الهدى نقيض الضلالة
- B002 yön, izlenen yol ve tutum | جهة الأمر وسيرته وقصده | Bir işin yönü, amacı ve izlenen doğrultusu ile bir kimsenin gidişi, görünür tutumu ve yöntemidir. Belirli anlatımlarda yürütülen söz ya da işten sapmama, başkasının yolunu izleme, ona benzeme veya aynı karşılığı yineleme anlamı kazanır. | خذ في هديتك أي فيما كنت فيه من الحديث أو العمل ولا تعدل عنه
- B003 bir şeyin ilk veya öndeki bölümü | المتقدم الهادي وأوائل الشيء | Bir şeyin ilk, önde bulunan veya öne çıkan bölümü ya da üyesidir. Atların boyunları veya ilk sırası, yaban hayvanlarının öncüleri, okun ucu, koyunun boynu ve sahibinin önünde ilerleyen değnek bu konumsal çekirdeğin özel gerçekleşmeleridir. | الهادي من كل شيء أوله
- B004 incelik göstergesi armağan verme | بعثة لطف وهدية إلى ذي مودة | Sevgi veya yakınlık duyulan birine incelik ve iyilik göstergesi olarak bir şey gönderme ya da verme ve verilen şeydir. Karşılıklı armağanlaşma, sunma tabağı ve bunu sık yapan kişi bu çekirdeğe bağlı kullanımlardır. | الهدية ما أهديت إلى ذي مودة من بر (ayn)
- B005 kutsal yere adanan hayvan, mal veya eşya | الهدي المهدى إلى الحرم | Kutsal eve veya bölgeye yakınlık kazanma amacıyla ayrılıp gönderilen hayvan, mal ya da eşyadır. Kimi anlatımlar bunu özellikle büyükbaş hayvanlara bağlar; develerin genel olarak aynı adla anılması ise bu kullanımdan genişlemedir. | الهدي والهدي ما أهديت إلى مكة
- B006 gelini eşinin yanına götürme | العروس المهدية إلى زوجها | Bir gelini eşinin yanına götürmek, onunla bir araya getirip ona katmak ve bu götürülme olayıdır. Aynı alan, eşine götürülen gelinin kendisini de adlandırır. | الهداء مصدر قولك هديت المرأة إلى زوجها
- B007 dokunulmaz sığınmacı; kimi açıklamalarda tutsak | هدي الحرمة والأسير | Bir topluluktan sığınma veya güvence isteyen ve bu yüzden dokunulmaz sayılan erkektir. Bazı kaynak açıklamalarında aynı ad tutsak erkek için de kullanılır. | الرجل الذي له حرمة كحرمة هدي البيت
- B008 sallanarak, gerektiğinde başkalarına dayanarak yürüme | مشي التهادي مع الاعتماد والتمايل | Yürürken sağa sola sallanmak veya yalpalamaktır. Güçsüz bir kişinin iki kişi arasında ilerleyip ikisine dayanması bunun özel yapısıdır; kadınların ve ağır develerin yürüyüşü örneklenir. | التهادي مشي في تمايل يمينا وشمالا كمشي النساء والإبل الثقال (ayn)
- B009 bön, güçsüz ve ağır kimse | الهداء البليد الضعيف | Bön, güçsüz, ağır ve uyuşuk erkek için kullanılan olumsuz bir nitelemedir. | الهداء الرجل البليد الضعيف (ayn)
- B010 sakin, ölçülü ve düzgün ilerleyiş | هدي السكون وحسن الهيئة | Bozguna uğramış birinin telaşlı kaçışına benzemeyen sakin, ölçülü ve düzgün ilerleyiş ya da görünür tutumdur. | الهدي السكون
- B011 övgü veya yergi şiiri sunma ve şiirle yergileşme | إهداء الشعر ومهاداته | Bir kişiye övgü veya yergi içeren bir şiir sunmak ya da iki kişinin şiirle karşılıklı olarak birbirini yermesidir. | الإهداء أن تهدي إلى إنسان مديحا أو هجاء شعرا (ayn)

### ص ر ط — 1:6 w2 ٱلصِّرَٰطَ
- B001 yol, özellikle düz yol | الطريق المستقيم | Bir yerden başka bir yere gitmeye yarayan yol; bu genel anlam içinde özellikle doğrultusu düzgün olan yol. | الصراط والسراط والزراط: الطريق (sihah)
- B002 geçişte gözden kaybolmak; özellikle yiyeceği yutmak | الغيبة في المرور والبلع | Geçiş ve gidiş sırasında gözden kaybolmak; özellikle bir şeyi, başta yiyeceği, boğazdan geçirerek yutmak. Kolay yutulan yiyecek ve geniş boğaz nitelemeleri bu çekirdeğe bağlı kullanımlardır. | أصل صحيح واحد يدل على غيبة في مر وذهاب
- B003 vuruşta kesip ilerleyen kılıç | السيف القاطع الماضي في الضربة | Vuruş sırasında hedefi kesip içinde ilerleyen etkili kılıç. | والسراط السيف القاطع الماضي في الضريبة (maqayis 1774)

### ق و م — 1:6 w3 ٱلْمُسْتَقِيمَ
- B001 erkekler topluluğu ve yakın çevresi | جماعة الناس والرجال | Temelde erkeklerden oluşan insan topluluğudur; bir erkeğin yandaş ve yakın soy çevresini de anlatabilir. Kadınların topluluğa bağlı olarak kapsanması ve sözün insan dışı varlıklara aktarılması ikincildir. | القوم الرجال دون النساء
- B002 ayağa kalkma ve dik durma | انتصاب وقيام بالبدن | Bir insanın ya da başka bir varlığın dik konuma gelmesi veya dik durumda bulunmasıdır. Tek seferlik ayağa kalkma, ibadetteki ayakta duruş, bitkinin kökü üzerinde kalması ve hayvanın durması bu fiziksel duruşun özel görünümleridir. | القومة ما بين الركعتين من القيام
- B003 bir işe kararlılıkla girişme | عزم ونهوض إلى الأمر | Belirli bir işe kararlılıkla yönelmek, onu üstlenmek ve yapmaya girişmektir. | قام بمعنى العزيمة
- B004 sürekli gözetip yönetme | رعاية وحفظ وولاية | Bir işi, topluluğu veya düzeni sorumluluk üstlenerek sürekli gözetmek, korumak, yönetmek ve işler durumda tutmaktır. | قيم القوم من يسوس أمرهم ويقومهم
- B005 sürdürüp gereğini yerine getirme | إقامة وإدامة وتوفية حق | Bir şeyi sürdürmek, işler ve düzgün durumda tutmak ya da gereğini ve koşullarını eksiksiz yerine getirmektir. | أقام الشيء أي أدامه
- B006 bir yerde kalma ve kalınan yer | مقام وإقامة في موضع | Bir yerde kalmak ve orayı geçici ya da sürekli durulan yer edinmektir; ayak basılan veya kalınan yer ile kalış süresi de bu çekirdekten adlandırılır. Oturum ve bir araya gelmiş topluluk anlamı bunun daha uzak uzantısıdır. | أقمت بالمكان إقامة ومقاما
- B007 başkasının yerini ve işlevini alma | نيابة وقيام مقام غيره | Bir kişi veya şeyin başka birinin ya da başka bir şeyin yerini alması, onun adına iş görmesi veya işlevini üstlenmesidir. | القيمة أصله الواو لأنه يقوم مقام الشيء (sihah)
- B008 düzgünlük, denge ve doğru yoldan sapmama | استقامة واعتدال واستواء | Bir yolun, nesnenin, kişinin davranışının, işin ya da sözün eğrilikten ve aşırılıktan uzak, düzgün, dengeli ve doğru olmasıdır. | رمح قويم ورجل قويم
- B009 ayakta tutan dayanak ve geçim temeli | قوام وعماد ومعاش | Bir işin, düzenin, bedenin veya yaşamın ayakta kalmasını sağlayan temel dayanak, düzenleyici unsur ya da yeterli geçim aracıdır. | هذا الأمر لا قومية له أي لا قوام له
- B010 değer biçme ve belirlenen bedel | قيمة وتقويم وتسعير | Bir malın parasal değerini belirlemek ve bu değerlendirme sonucunda ortaya çıkan bedeldir; tarafların değer üzerinde karşılıklı hesaplaşması da bu alana bağlıdır. | القيمة ثمن الشيء بالتقويم
- B011 insanın boyu ve düzgün beden yapısı | قامة وقوام الجسم والطول | İnsanın ayakta dururken görülen boy ölçüsü, dik beden yapısı ve özellikle düzgün, güzel uzunluğudur. | القامة مقدار قيام الرجل
- B012 düzeneğin dik, taşıyıcı veya tutulan parçası | آلة قائمة وجزء قائم | Bir düzeneğin dik duran, taşıyan veya elle tutulan parçasıdır; kuyu makarası ve donanımı, kılıç sapı, yatak ya da hayvan ayağı ve çiftçinin tuttuğu ahşap parça bu alandadır. Kuyu başında insan biçimli yapı yorumu tartışmalıdır. | القامة مقدار قيام الرجل كهيئة الرجل يبنى على شفير بئر
- B013 ölülerin diriltildiği ve insanların yargı için kalktığı gün | قيامة وبعث وقيام الساعة | Dünyanın sonundaki saatin gerçekleştiği, ölülerin diriltildiği ve insanların yargılanmak üzere ayağa kalktığı gündür. | القيامة يوم البعث يقوم الخلق بين يدي القيوم (ayn)
- B014 karşılıklı direnip mücadele etme | مقاومة ومنازلة | İki tarafın bir işte, güreşte veya savaşta birbirine karşı durması, direnmesi ve üstün gelmek için mücadele etmesidir. | قاومته في كذا أي نازلته (ayn)
- B015 tam ve denk ağırlıktaki para | وزن سواء ومقدار معتدل | Belirli bir para parçasının ölçün ağırlığa tam eşit olması ve terazide ağır basmamasıdır. | دنانير قوم وقيم ودينار قائم أي مثقال سواء لا يرجح (ayn)
- B016 donup akmama veya yorulup ilerleyememe | جمود ووقوف وكلال | Su için donarak akmaz duruma gelmek; binek hayvanı için durmak veya yorulup yürüyemez hale gelmektir. İki kullanımın ortak sonucu ilerleme ya da akışın kesilmesidir, nedenleri aynı değildir. | قام الماء جمد
- B017 güneşin tam tepede olduğu öğle ortası | انتصاف النهار وقائم الظهيرة | Güneşin göğün ortasında bulunduğu, günün iki yarısının dengelendiği ve gölgenin en kısa duruma yaklaştığı öğle ortasıdır. | قام قائم الظهيرة إذا قامت الشمس وكاد الظل يعقل (ayn
- B018 pazarın canlanıp satışların artması | نفاق السوق | Pazarın canlanması, malların alıcı bulması ve satışların hareketlenmesidir. | قامت السوق نفقت (sihah)
- B019 bir beden bölümünün kişiye ağrı vermesi | وجع قائم بالعضو | Sırt, göz veya bedenin başka bir bölümünün kişiye ağrı vermesi ve o kişinin bu organda acı duymasıdır. | قام بي ظهري أي أوجعني
- B020 koyunun bacaklarını tutan hastalık | قوام في قوائم الشاة | Koyunun bacaklarını tutan ve hayvanın etkilenerek ayağa kalkmasına yol açan belirli bir hastalıktır. | القوام داء يأخذ الشاة في قوائمها تقوم منه (sihah)
- B021 göz bebeği sağlamken görme yetisinin kaybolması | عين قائمة ذاهبة البصر | Göz bebeği ve gözün görünür yapısı sağlam kaldığı halde görme yetisinin bütünüyle kaybolduğu göz durumudur. | عين قائمة ذهب بصرها والحدقة صحيحة (ayn)



===== branches.md =====
# branches.md — the dictionary lines of the branches the findings cite (focus roots: dictionary.md)

- ح م د B001 yermenin karşıtı olan, iyilik için teşekkürü de kapsayan övgü | الحمد خلاف الذم | Bir kişiyi ya da övülesi bir işi iyi sözlerle değerlendirme ve yermenin karşıtıdır; bir iyiliğe karşılık olduğunda teşekkür anlamını da kapsar, ancak bununla sınırlı değildir. Tanrı'yı güzel sözlerle sık sık anma, bu çekirdeğin belirli bir türemiş kullanımıdır. | الحمد نقيض الذم (maqayis
- ح م د B004 övülesi işin varılabilecek en ileri sınırı | حماداك الغاية المحمودة | Belirli bir kalıp, kişinin yapabileceği işin en ileri sınırını ve bu sınıra ulaşmanın övülesi oluşunu bildirir; kimi açıklamada doğrudan kişinin övgüsü anlamı öne çıkar. Çoğul bir kullanım, aktarılan sözde kadınlarda övülen niteliklerin en ileri derecesini belirtir. | حماداك أن تفعل كذا أي غايتك وفعلك المحمود (maqayis)
- ح م د B006 muhatabı katarak övme veya iyilikleri teşekkürle anma | أحمد إليك الله | Yalnız belirli yönelme kalıplarında, muhatabı kendine katarak Tanrı'yı birlikte övmeyi veya birinin iyiliklerini muhataba teşekkürle anmayı bildirir. | أحمد إليك الله أي معك (ayn
- د ي ن B001 boyun eğerek uyma ve buna dayalı inanç düzeni | الطاعة والانقياد | Bir üstün iradesine boyun eğerek buyruğuna uyma ve bağlı kalma; Tanrı'ya yöneldiğinde kulluk, bir inanç yolu ve onun kurallarına bağlılık biçimini alabilir. | أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل (maqayis)
- د ي ن B002 yargılayıp hesap görerek karşılığını verme | الحساب والجزاء | Bir eylemi veya kişiyi hükme bağlayıp hesabını görmek ve sonucuna göre karşılığını vermek; belirli bir gün adı olarak bu sürecin gerçekleşeceği zamanı anlatır. | يوم الدين أي يوم الحكم والحساب والجزاء (maqayis)
- د ي ن B003 borç alıp verme ve vadeli ödeme ilişkisi | الدين المالي | Bir mal veya paranın borç olarak alınıp verilmesiyle, taraflardan biri için ileride ödeme ya da geri verme yükümlülüğü doğuran mali ilişki; vadeli alışveriş de bu ilişkinin özel bir biçimidir. | الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء (maqayis)
- د ي ن B004 zorla alçaltıp egemenliği altına alma | الإذلال والملك | Birini zorla alçaltıp egemenlik altına almak, köleleştirmek veya mülk edinmek; bu işlemin sonucunda kişi bağımlı ve başkasının buyruğu altında sayılır. | العبد مدين كأنهما أذلهما العمل ويا دين قلبك أي أذل (maqayis)
- د ي ن B005 alışılmış davranış ve öteden beri bilinen hal | العادة والشأن | Bir kişinin veya topluluğun tekrarla yerleşmiş alışkanlığı, süregelen işi ya da öteden beri bilinen hali ve tutumu. | العادة يقال لها دين (maqayis)
- د ي ن B006 kent | مدينة الطاعة | İnsanların toplu yaşadığı büyük ve düzenli yerleşim, yani kent. Adlandırılması, o yerde yöneticilerin buyruklarına uyulmasıyla açıklanır; bu ilişki kentin zorunlu özelliği değildir. | المدينة كأنها مفعلة سميت بذلك لأنها تقام فيها طاعة ذوي الأمر (maqayis)
- ر ب ب B001 sahip olup yönetme | ربوبية وملك وسيادة | Bir varlık ya da şey üzerinde sahiplik, üstün yetke ve düzenleyici yönetim kurma niteliğidir. Mutlak kullanım Tanrı'yı gösterirken başka kullanımlar yönetilen veya sahip olunan şeyi açıkça belirtir. | الرب: الله تبارك وتعالى
- ر ب ب B002 adım adım yetiştirip tamamlama | إصلاح وتربية وإتمام | Bir şeyi sürekli gözetim altında düzeltmek, geliştirmek ve aşama aşama tamamlanmış durumuna ulaştırmaktır. | رب الرجل النعمة يربها ربا
- ر ب ب B007 bir yerde kalıp sürme | لزوم وإقامة ودوام | Bir yerde kalıp oradan ayrılmamak veya bir durumun kesilmeden sürmesidir. Hayvanın bir eşe bağlanması ve bir şeye yaklaşma anlamı bu kalıcılık çekirdeğinin özel uzantılarıdır. | رب بالمكان وأرب إذا أقام به (jamhara)
- ر ب ب B011 bağlayıcı söz ve güvence | ربابة عهد وميثاق | İnsanları karşılıklı bağlılık, güvence veya dayanışma içinde birleştiren sözleşme ve verilmiş sözdür. Bu sözleşmeye bağlı kişiler ile söz gibi bağlayıcı sayılan vergi payı da ilişkili kullanımlardır. | الربابة: العهد والمعاهدون أربة (jamhara)
- ر ب ب B013 bol ve toplanmış su | ماء رَبَب كثير | Bir yerde toplanmış ya da çok miktarda bulunan sudur; bazı kullanımlarda tatlı su olduğu ayrıca belirtilir. | الربب، بالفتح: الماء الكثير، ويقال العذب (sihah)
- ر ب ب B014 yaban sığırı sürüsü | رَبْرَب قطيع | Özellikle yaban sığırlarından oluşan sürüdür; bazı kullanımlarda genel sığır topluluğunu veya deve sürüsünü de kapsar. | الربرب: القطيع من بقر الوحش (sihah)
- ر ح م B001 acıma duygusuyla esirgeyip iyilik etme | الرَّحْمَة والرقة | Bir başkasına karşı yüreğin yumuşaması, ona acıma ve bu yönelişin onu esirgeyip ona iyilik etmeyi gerektirmesidir. Tanrı'ya uygulandığında insandaki duygulanmadan çok, kuşatıcı esirgeme ve iyilik sonucu öne çıkar. | أصل واحد يدل على الرقة والعطف والرأفة (maqayis)
- ر ح م B002 yakın soy bağı | الرَّحِم والقرابة | İnsanları ortak bir soydan gelmeleri yoluyla birbirine bağlayan yakın ilişkidir. Organ adı, birden çok kişinin aynı doğum kaynağından çıkması düşüncesiyle bu toplumsal bağa aktarılmıştır. | الرَّحِم علاقة القرابة (maqayis)
- ر ح م B004 döl yatağı hastalığı ve doğum sonrası bozukluk | وجع الرَّحِم بعد الولادة | Dişi deve, koyun veya kadında döl yatağının ağrıması ya da hastalanmasıyla; koyunda ise ayrıca şişmesiyle belirlenen durumdur. Bazı kullanımlar bunu doğum sonrasına bağlar. Koyunun doğumdan sonra yavru zarını atamaması da bu organ çevresindeki özel bir bozukluk olarak dala dahildir. | شاة رحوم إذا اشتكت رحمها بعد النتاج (maqayis)
- س م و B004 üstteki gök veya örtü ve buna bağlı üstten gelen ya da üstte bulunan şeyler | السماء وما علا فأظل | Bir şeyin üzerinde bulunan ve onu örten gök, tavan ya da genel üst yandır. Bu ad buluta, yukarıdan gelen yağmura, yağmurla çıkan veya yükselen bitkiye ve atın sırtına da aktarılır. | العرب تسمى السحاب سماء والمطر سماء
- س م و B005 ad, adlandırma ve ad ya da nitelik bakımından denklik | الاسم تنويه ودلالة | Bir şeyi tanıtan ad, bu adı verme veya edinme ve başka biriyle aynı adı taşıma ilişkisidir. Ayrıca aynı adı ya da niteliği hak edecek ölçüde denk olmayı anlatır; kaynaklar adlandırmayı anılmayı yükseltme düşüncesiyle açıklar. | أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى (maqayis)
- ض ل ل B001 doğru yoldan ve amaçtan sapma ya da başkasını saptırma | الضلال عن الهدى والقصد | Bir kimsenin amaçtan, doğru yoldan veya doğruluktan ayrılması, yolunu bulamaması ya da yanlış ve boş olana yönelmesidir. Ettirgen kullanımda başka biri bu doğrultudan uzaklaştırılır. | كل جائر عن القصد ضال
- ض ل ل B002 gizlenerek, karışıp eriyerek veya gömülerek gözden yitme | الغيبوبة والخفاء | Bir şeyin gizlenerek, toprağa karışarak ya da başka bir maddenin içinde seçilemez hale gelerek gözden yitmesidir. Ölüyü gömmek, onu görünmez kılan özel bir ettirgen kullanımdır. | أضل الميت إذا دفن
- ض ل ل B003 bir şeyi yitirme veya yerini bulamama; özel olarak kanın karşılıksız kalması | فقدان الشيء | Bir şeyin sahibinin elinden çıkması veya kişinin hareketli bir şeyi ya da sabit bir yerin konumunu bulamamasıdır. Özel bir kullanımda öldürülen kişinin kanı öç alınmadan ve karşılık aranmadan kalır. | أضللت بعيري إذا ذهب منك
- ض ل ل B004 bir şeyi unutmak veya bellekte tutamamak | ضياع الحفظ | Bir şeyi unutmak, yani onun bilgisini bellekte hazır tutamamak veya gerektiğinde hatırlayamamaktır. | ضللت الشيء أنسيته (jamhara)
- ض ل ل B005 sahibi bilinmeyen kayıp hayvan, özellikle deve | الضالّة في المضيعة | Sahibinden ayrılmış, ortada kalmış ve sahibinin kim olduğu bilinmeyen hayvandır; özellikle deve için kullanılır ve hayvanın erkek ya da dişi olması adı değiştirmez. | الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها الذكر والأنثى فيه سواء (ayn)
- ع ب د B001 özgür olmayan, sahip olunan kişi | الرق والملك | Özgür olmayan, bir başkasının mülkiyetinde sayılan ve eski hukuk düzeninde alınıp satılabilen insandır. | العبد وهو المملوك (maqayis)
- ع ب د B003 boyun eğerek itaat ve tapınma | العبادة والطاعة الخاضعة | Bir varlığa en ileri ölçüde boyun eğerek itaat etmek ve tapınma yönelişi göstermektir; dinsel kullanım Tanrı'ya, bazı özel söz öbekleri ise sahte tanrısal güçlere yönelir. | عبد يعبد عبادة فلا يقال إلا لمن يعبد الله (maqayis
- ع ب د B004 köleleştirmek veya köle gibi boyunduruk altına almak | التعبيد والاستعباد | Bir insanı köle edinmek, köle durumuna getirmek ya da özgür olsa bile köle gibi çalışacak ölçüde boyunduruk altına almaktır. | استعبدت فلانا اتخذته عبدا (maqayis
- ع ب د B005 düzleşmiş yol, katranlanmış deve veya kaplanmış gemi | التذليل والتسوية | Verilen yapılarda yolun çok geçilerek düzleşip kolay kullanılır olması, devenin derisinin katranla kaplanıp uysallaştırılması veya geminin katran, yağ ya da benzeri bir maddeyle kaplanması anlatılır. | الطريق المعبد وهو المسلوك المذلل (maqayis)
- ع ب د B007 güç, sağlamlık ve dayanıklılık | القوة والصلابة | Bir varlığın güçlü, sağlam ve zaman içinde dayanıklı olmasıdır; dişi deve bağlamında bu sağlamlığa semizlik de eşlik eder. | العبدة وهي القوة والصلابة (maqayis)
- ع ب د B009 gecikmeden yapmak veya koşuda biraz hızlanmak | قلة اللبث وسرعة العدو | Verilen bir söz öbeğinde bir işi yapmakta hiç gecikmemeyi, diğerinde ise koşarken bir ölçü hızlanmayı anlatır. | ما عبد أن فعل ذاك أي ما لبث (sihah
- ع ب د B010 her yana dağılmış kümeler, nesneler veya yollar | التفرق في الوجوه | İnsan kümelerinin, nesnelerin, uzak uçların veya yolların birbirinden ayrılarak çeşitli yönlere dağılmış olmasıdır. | العباديد الفرق من الناس الذاهبون في كل وجه وكذلك العبابيد (sihah)
- ع ب د B011 bineği yüzünden yolda kalma veya güçlükle direnen deve | العطب والانقطاع | Bir yapıda yolcunun bineği yorulduğu, zarar gördüğü veya elden çıktığı için yolda kalması; diğerinde ise devenin insanlara güçlük çıkararak direnmesi anlatılır. | أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت (sihah)
- ع ل م B001 bilme ve gerçeğini kavrama | انكشاف الشيء للعارف | Bir şeyi bilmek, tanımak ve onu gerçeğine uygun biçimde kavramak; böylece bilgisizlikten çıkmaktır. Haber verilmesi, öğretme, öğrenme ve bilgi bakımından üstün gelme bu çekirdekten hareket eden, belirli biçimlere bağlı kullanımlardır. | العلم نقيض الجهل (maqayis
- ع ل م B002 ayırt edici ve yol gösterici işaret | أثر يميز الشيء ويهدي إليه | Bir şeyi başkalarından ayıran, tanınmasını sağlayan veya ona götüren belirgin iz ya da işarettir. Bayrak, uzaktan seçilen dağ, yol belirtisi, kumaş kenarı ve sonradan konan tanıtıcı izler bu işlevin farklı gerçekleşmeleridir. | أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره (maqayis)
- ع ل م B003 evren ve bütün yaratılmışlar | الخلق عالم يدل على صانعه | Yaratılmış olanların bütünü; bağlama göre evren ile içindekilerin tamamı veya yaratıkların ayrı ayrı sınıflarıdır. Bu bütünün yaratıcıyı gösteren bir belirti sayılması, adın açıklanan dayanağıdır. | العالمون كل جنس من الخلق فهو في نفسه معلم وعلم (maqayis)
- ع ل م B005 deniz ya da suyu bol kuyu | ماء كثير مجتمع في عيلم | Aynı sözlük biçiminin bir kullanımda denizi, başka bir kullanımda ise suyu bol kuyuyu adlandırmasıdır. İki karşılık, genel bir su birikintisi anlamında kaynaştırılmaz. | العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء (maqayis)
- ع و ن B001 yardım, destek ve dayanışma | الإعانة والمظاهرة | Bir kişinin, topluluğun ya da aracın bir işi gerçekleştirmede başkasına güç, destek veya kolaylık sağlamasıdır. Bu çekirdek, yardım istemeyi, birlikte karşılıklı yardım etmeyi ve yardımsever kişi nitelemesini de türemiş kullanımlar olarak kapsar. | كل شيء استعنت به أو أعانك فهو عونك (ayn)
- ع و ن B005 bedensel denge ve güç olgunluğu | استواء الخلقة وتلاحق القوة | Belirli kadın ve yük atı nitelemelerinde bedenin yaşla birlikte dengeli ya da güçlü bir olgunluğa erişmesini anlatır. Kadında yaş alma, etlilik ve orantılı görünüş; hayvanda ise güç ile yaşın birbirine yetişmesi ayrı koşullardır. | المتعاونة من النساء التي طعنت في السن ولا تكون إلا مع كثرة اللحم (sihah)
- ع و ن B006 yaban eşeği sürüsü | العانة قطيع الحمر | Yaban eşeklerinden oluşan bir sürüyü adlandıran sözdür; aynı anlam için iki ayrı çoğul biçim kullanılır. | العانة القطيع من حمر الوحش وتجمع على عانات وعون (ayn)
- غ ض ب B003 karşı koyup muhalefet etmek | المراغمة والمخالفة | Birine karşı koyup onunla inatlaşarak muhalefet etmek, ayrıca bir topluluğa karşı çıkan durumda bulunmaktır. | غاضبه: راغمه
- غ ض ب B005 kalın derili ya da çok kızıl | غلظ الجسم وشدة الحمرة | Belirli kişi nitelemelerinde kalın derili olmayı, kızıl ve kalın görünümü ya da çok yoğun kızıllığı bildirir. Yalın biçim de çok kızıl olanı adlandırabilir. | رجل غضاب إذا كان غليظ الجلد
- غ ض ب B006 üst göz kapağı çıkıntısı veya göz çevresi şişliği | تورم العين وما حولها | Üst göz kapağındaki doğuştan çıkıntıyı veya gözün çevresinde, özellikle altında oluşan şişliği bildirir. | الغضب بخصة في الجفن الأعلى خلقة (ayn)
- غ ض ب B008 belirli hayvan derileri veya kalkan gibi katlanmış deri | جلد صلب أو مطوي كدرقة | Belirli hayvanların derisini veya üst üste katlanarak kalkana benzetilen bir deve derisi parçasını adlandırır. | الغضبة جلد المسن من الوعول حين يسلخ (ayn)
- غ ي ر B001 yarar sağlayıp durumunu iyileştirme | الصلاح والمنفعة بالميرة والسقي والإصلاح | Bir kimsenin ailesine geçimlik sağlayarak yarar dokundurmasıdır; belirli yapılarda yağmurun insanları ya da toprağı sulayıp durumlarını iyileştirmesini ve yük takımının indirilip düzeltilmesini de anlatır. | الغِيرة بالكسر: الميرة (sihah)
- غ ي ر B002 cana karşılık ceza yerine kabul edilen kan bedeli | الغَيْر في الدية | Öldürme ya da yaralama karşılığında hak sahibine ödenen kan bedeli ve bu bedelin cana karşılık uygulanacak cezanın yerine kabul edilmesidir. | غارني الرجل إذا وداك من الدية والاسم الغِيرة (sihah)
- غ ي ر B003 biçimini değiştirme veya yerine başkasını koyma | تغيير الصورة أو إبدال الشيء بغيره | Bir şeyin özü aynı kalsa da biçiminin ya da durumunun öncekinden farklı hale getirilmesi veya bir şeyin kaldırılıp yerine başka bir şeyin konmasıdır. Belirli yapılarda yanlış olanı doğru olanla giderme, alışverişte karşılıklı değiştirme ve cana karşılık cezadan kan bedeline dönme biçiminde gerçekleşir. | الاسم من قولك غيرت الشيء فتغير (sihah)
- غ ي ر B005 başka olma, dışta bırakma veya olumsuzlama | السوى والخلاف والاستثناء والنفي | Bir şeyin ötekinden ayrı, başka veya ona aykırı olmasıdır; bu ilişki dil içinde bir unsuru kümenin dışında bırakmak, bir niteliği ya da varlığı olumsuzlamak ve iki şeyin birbirinden farklı olduğunu bildirmek için de kullanılır. | هذا الشيء غير ذاك أي هو سواه وخلافه (maqayis)
- م ل ك B002 sahiplik ve tasarruf yetkisi | المِلْك والتصرف | Bir şeyin bir kişinin elinde veya hukuki alanında bulunması ve o kişinin onun üzerinde tasarruf yetkisi taşımasıdır. Bu yetki devredilebilir; tarihsel kullanımlarda köleleştirilmiş kişileri ve onlara ilişkin davranışı, belirli bir kalıpta ise boşanma kararının eşe bırakılmasını da kapsar. | ملك الإنسان الشيء يملكه ملكا (maqayis)
- م ل ك B003 hükümdarlık ve kamusal egemenlik | المُلك والسلطان | Bir hükümdarın halk üzerinde emir, yasak ve yönetim yetkisi kullanmasıyla kurulan kamusal hükümranlıktır. Bu alan hükümdarı, yönetim gücünü, hükmedilen ülkeyi ve ilahi bağlamda mutlak egemenliği kapsar. | والاسم الملك لأن يده فيه قوية صحيحة (maqayis)
- م ل ك B004 evlilik akdi kurma | الإملاك والتزويج | İki kişi arasında evlilik bağını sözleşmeyle kurmak veya bu akdin gerçekleşmesidir. Kullanım, birini evlendirmeyi, evlilik akdine tanıklığı ve bir erkeğin bir kadınla evlenmesini kapsar. | كنا في إملاك فلان أي أملكناه امرأته (maqayis)
- م ل ك B005 işi ayakta tutan temel dayanak | مِلاك الأمر وعِماده | Bir işin, düzenin veya bedenin ayakta kalmasını, düzgün işlemesini ve tamamlanmasını sağlayan temel dayanak unsurudur. Kalbin beden için bu işlevi görmesi verilen başlıca örnektir. | ملاك الأمر ما يعتمد عليه (ayn)
- م ل ك B006 yolun veya yerin orta ya da ana kesimi | مَلَك الطريق والوادي | Yolun, vadinin veya yerleşimin bağlama göre orta, ana ya da büyük kesimidir; vadi kullanımında sınır da bu adlandırmaya katılır. Söyleyişe göre bu kesim izlenecek bir güzergâh veya uzak durulacak bir yer olabilir. | ملك الطريق أيضا وسطه (sihah)
- م ل ك B007 işleri ve yaşamı sürdüren su kaynağı | الماء مَلَك الأمر | Su, yolcunun veya bir topluluğun işini denetim altında tutmasını, konaklamasını ve geçimini sürdürmesini sağlayan temel kaynaktır. Suyun bulunmaması bu yeterliğin yokluğu, çok sayıda su kaynağı ise güçlü yaşam imkânı olarak anlatılır. | والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره (maqayis)
- م ل ك B008 hayvanlarda önden gidip yön veren unsur | المتقدم القائد في الحيوان | Bir hayvan topluluğunda önden gidip geri kalanların izlediği önder canlı veya bir binek hayvanını önden yönelten beden bölümüdür. Arı topluluğunun önderi, sürünün öncüsü ve bineğin ön ayakları ile yönlendirici kısmı bu kalıba bağlı kullanımlardır. | مليك النحل يعسوبها (sihah)
- ن ع م B001 iyi yaşam durumu ve başkasına ulaştırılan iyilik | حسن الحال والنعمة | Kişinin rahat, iyi ve elverişli bir yaşam durumunda bulunması; ayrıca bir yararın bağış, yardım ya da iyilik olarak ona ulaşması veya başkasına ulaştırılmasıdır. | أصل واحد يدل على ترفه وطيب عيش وصلاح (maqayis)
- ن ع م B004 evet diyerek onaylamak veya söz vermek | الجواب بنعم والتصديق | Bir soruya olumlu cevap vermek, söylenen bir şeyi doğru diye onaylamak veya istenen bir iş için olumlu söz vermektir. | نعم جواب الواجب ضد لا (maqayis)
- ن ع م B005 develer ve geniş anlamda otlayan evcil hayvanlar | مال الأنعام والإبل | Dar kullanımda develeri, daha geniş topluluk adında ise deve, sığır ve koyun gibi otlayan evcil hayvanları gösteren hayvan varlığıdır. | النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم (maqayis)
- ن ع م B007 devekuşuna benzetilerek ad verilen şeyler | ما سمي نعامة تشبيها بالهيئة | Devekuşunun görünüşüne veya belirgin bir özelliğine benzetilerek aynı adın verildiği kuyu kirişi, dağ gölgeliği, ayak ya da bacak bölümü, yol ve Ay'ın konak yerleri gibi varlıklardır. | على معنى التشبيه النعامة وهي كالظلة تجعل على رءوس الجبل (maqayis)
- ن ع م B008 bir topluluğun dağılıp gücünü yitirmesi | طيران النعامة وتفرق القوم | Belirli kuş imgeli sözlerde bir topluluğun hızla dağılıp ayrılması, yol alması veya birliğini ya da gücünü yitirmesidir. | شالت نعامتهم إذا تفرقوا (maqayis)
- ن ع م B011 bir yeri kendine uygun bulup orada kalmak | موافقة المكان وطيب المقام | Bir yere geldikten sonra o yeri kendine uygun ve hoş bulup orada kalmak veya yerleşmektir. | أتيت أرض بني فلان فتنعمتني إذا وافقته (maqayis)
- و س م B004 belirlenmiş toplu buluşma zamanı ve yeri | موسم معلم يجتمع إليه الناس | İnsanların kutsal ziyaret, pazar veya benzeri ortak bir amaçla bir araya geldiği, önceden belirlenmiş zaman, yer ya da toplu buluşmadır. Bu belirlenmiş buluşmaya gidip katılmak da dala bağlı bir eylem olarak kullanılır. | وسمى موسم الحاج موسما لأنه معلم يجتمع إليه الناس (maqayis)
- و ل ه B003 salınan suyun açık arazide akıp kaybolması | ماء مُولَه ذاهب | Açık ve ıssız araziye salınan suyun orada akıp gözden yitmesi ve suyu bu biçimde salınmış kaynağın bu sonuçla nitelenmesidir. | عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)
- ي و م B001 güneşin doğuşundan batışına kadarki gün | وقت النهار المحدود | Güneşin doğuşundan batışına kadar uzanan bilinen zaman aralığı ve bu aralıklardan oluşan dizinin tek bir birimidir. | اليوم: الواحد من الأيام (maqayis)
- ي و م B003 büyük olayın yaşandığı çetin gün veya olay | كائنة اليوم وشدته | Büyük veya çetin bir olayın gerçekleştiği kritik günü ya da olayın kendisini anlatan aktarmalı kullanımdır. Bazı kalıplarda çok ağır bir gün, çoğul biçimde ise yaşanmış önemli olaylar anlamı taşır. | يستعيرونه في الأمر العظيم ويقولون نعم فلان في اليوم إذا نزل (maqayis)


===== concordance.md =====
# concordance.md — every use of the focus roots of 1:6 (roots with at most 60 uses; stop lemmas left out)

Each use: its word id S:A:W, its form, and its clause in the exact verifier spelling; the word ID identifies the focus. Larger roots: counts per lemma.

## ه د ي — 316 uses; here 1:6:1; lemmas: هَدَى 144; هُدًى 85; ٱهْتَدَىٰ 40; مُّهْتَدُون 17; هَدْي 7; أَهْدَىٰ 7; هَاد 7; مُّهْتَد 3; هَادِي 2; هَدِيَّة 2; مُهْتَدِى 1; هَٰدِى 1

## ص ر ط — 45 uses; here 1:6:2; lemmas: صِرَٰط 45
### صِرَٰط
- 1:6:2 [صِرَٰط N] ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7:1 [صِرَٰط N] صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ
- 2:142:20 [صِرَٰط N] … كَانُوا۟ عَلَيْهَا ۚ قُل لِّلَّهِ ٱلْمَشْرِقُ وَٱلْمَغْرِبُ ۚ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 2:213:48 [صِرَٰط N] … ٱخْتَلَفُوا۟ فِيهِ مِنَ ٱلْحَقِّ بِإِذْنِهِۦ ۗ وَٱللَّهُ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍ
- 3:51:7 [صِرَٰط N] إِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۗ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- 3:101:16 [صِرَٰط N] … ءَايَٰتُ ٱللَّهِ وَفِيكُمْ رَسُولُهُۥ ۗ وَمَن يَعْتَصِم بِٱللَّهِ فَقَدْ هُدِىَ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 4:68:2 [صِرَٰط N] وَلَهَدَيْنَٰهُمْ صِرَٰطًۭا مُّسْتَقِيمًۭا
- 4:175:14 [صِرَٰط N] … بِٱللَّهِ وَٱعْتَصَمُوا۟ بِهِۦ فَسَيُدْخِلُهُمْ فِى رَحْمَةٍۢ مِّنْهُ وَفَضْلٍۢ وَيَهْدِيهِمْ إِلَيْهِ صِرَٰطًۭا مُّسْتَقِيمًۭا
- 5:16:17 [صِرَٰط N] … سُبُلَ ٱلسَّلَٰمِ وَيُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِهِۦ وَيَهْدِيهِمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 6:39:16 [صِرَٰط N] … فِى ٱلظُّلُمَٰتِ ۗ مَن يَشَإِ ٱللَّهُ يُضْلِلْهُ وَمَن يَشَأْ يَجْعَلْهُ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 6:87:8 [صِرَٰط N] وَمِنْ ءَابَآئِهِمْ وَذُرِّيَّٰتِهِمْ وَإِخْوَٰنِهِمْ ۖ وَٱجْتَبَيْنَٰهُمْ وَهَدَيْنَٰهُمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 6:126:2 [صِرَٰط N] وَهَٰذَا صِرَٰطُ رَبِّكَ مُسْتَقِيمًۭا ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَذَّكَّرُونَ
- 6:153:3 [صِرَٰط N] وَأَنَّ هَٰذَا صِرَٰطِى مُسْتَقِيمًۭا فَٱتَّبِعُوهُ ۖ وَلَا تَتَّبِعُوا۟ ٱلسُّبُلَ فَتَفَرَّقَ بِكُمْ عَن سَبِيلِهِۦ ۚ ذَٰلِكُمْ …
- 6:161:6 [صِرَٰط N] قُلْ إِنَّنِى هَدَىٰنِى رَبِّىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ دِينًۭا قِيَمًۭا مِّلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۚ وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ
- 7:16:6 [صِرَٰط N] قَالَ فَبِمَآ أَغْوَيْتَنِى لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ
- 7:86:4 [صِرَٰط N] وَلَا تَقْعُدُوا۟ بِكُلِّ صِرَٰطٍۢ تُوعِدُونَ وَتَصُدُّونَ عَن سَبِيلِ ٱللَّهِ مَنْ ءَامَنَ بِهِۦ وَتَبْغُونَهَا عِوَجًۭا …
- 10:25:10 [صِرَٰط N] وَٱللَّهُ يَدْعُوٓا۟ إِلَىٰ دَارِ ٱلسَّلَٰمِ وَيَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 11:56:17 [صِرَٰط N] … مَّا مِن دَآبَّةٍ إِلَّا هُوَ ءَاخِذٌۢ بِنَاصِيَتِهَآ ۚ إِنَّ رَبِّى عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 14:1:14 [صِرَٰط N] … إِلَيْكَ لِتُخْرِجَ ٱلنَّاسَ مِنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِ رَبِّهِمْ إِلَىٰ صِرَٰطِ ٱلْعَزِيزِ ٱلْحَمِيدِ
- 15:41:3 [صِرَٰط N] قَالَ هَٰذَا صِرَٰطٌ عَلَىَّ مُسْتَقِيمٌ
- 16:76:28 [صِرَٰط N] … يَأْتِ بِخَيْرٍ ۖ هَلْ يَسْتَوِى هُوَ وَمَن يَأْمُرُ بِٱلْعَدْلِ ۙ وَهُوَ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 16:121:6 [صِرَٰط N] شَاكِرًۭا لِّأَنْعُمِهِ ۚ ٱجْتَبَىٰهُ وَهَدَىٰهُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 19:36:7 [صِرَٰط N] وَإِنَّ ٱللَّهَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- 19:43:12 [صِرَٰط N] … إِنِّى قَدْ جَآءَنِى مِنَ ٱلْعِلْمِ مَا لَمْ يَأْتِكَ فَٱتَّبِعْنِىٓ أَهْدِكَ صِرَٰطًۭا سَوِيًّۭا
- 20:135:8 [صِرَٰط N] قُلْ كُلٌّۭ مُّتَرَبِّصٌۭ فَتَرَبَّصُوا۟ ۖ فَسَتَعْلَمُونَ مَنْ أَصْحَٰبُ ٱلصِّرَٰطِ ٱلسَّوِىِّ وَمَنِ ٱهْتَدَىٰ
- 22:24:8 [صِرَٰط N] وَهُدُوٓا۟ إِلَى ٱلطَّيِّبِ مِنَ ٱلْقَوْلِ وَهُدُوٓا۟ إِلَىٰ صِرَٰطِ ٱلْحَمِيدِ
- 22:54:20 [صِرَٰط N] … بِهِۦ فَتُخْبِتَ لَهُۥ قُلُوبُهُمْ ۗ وَإِنَّ ٱللَّهَ لَهَادِ ٱلَّذِينَ ءَامَنُوٓا۟ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 23:73:4 [صِرَٰط N] وَإِنَّكَ لَتَدْعُوهُمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 23:74:7 [صِرَٰط N] وَإِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ عَنِ ٱلصِّرَٰطِ لَنَٰكِبُونَ
- 24:46:10 [صِرَٰط N] لَّقَدْ أَنزَلْنَآ ءَايَٰتٍۢ مُّبَيِّنَٰتٍۢ ۚ وَٱللَّهُ يَهْدِى مَن يَشَآءُ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 34:6:14 [صِرَٰط N] … ٱلْعِلْمَ ٱلَّذِىٓ أُنزِلَ إِلَيْكَ مِن رَّبِّكَ هُوَ ٱلْحَقَّ وَيَهْدِىٓ إِلَىٰ صِرَٰطِ ٱلْعَزِيزِ ٱلْحَمِيدِ
- 36:4:2 [صِرَٰط N] عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 36:61:4 [صِرَٰط N] وَأَنِ ٱعْبُدُونِى ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- 36:66:7 [صِرَٰط N] وَلَوْ نَشَآءُ لَطَمَسْنَا عَلَىٰٓ أَعْيُنِهِمْ فَٱسْتَبَقُوا۟ ٱلصِّرَٰطَ فَأَنَّىٰ يُبْصِرُونَ
- 37:23:6 [صِرَٰط N] مِن دُونِ ٱللَّهِ فَٱهْدُوهُمْ إِلَىٰ صِرَٰطِ ٱلْجَحِيمِ
- 37:118:2 [صِرَٰط N] وَهَدَيْنَٰهُمَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 38:22:23 [صِرَٰط N] … عَلَىٰ بَعْضٍۢ فَٱحْكُم بَيْنَنَا بِٱلْحَقِّ وَلَا تُشْطِطْ وَٱهْدِنَآ إِلَىٰ سَوَآءِ ٱلصِّرَٰطِ
- 42:52:26 [صِرَٰط N] … نُورًۭا نَّهْدِى بِهِۦ مَن نَّشَآءُ مِنْ عِبَادِنَا ۚ وَإِنَّكَ لَتَهْدِىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 42:53:1 [صِرَٰط N] صِرَٰطِ ٱللَّهِ ٱلَّذِى لَهُۥ مَا فِى ٱلسَّمَٰوَٰتِ وَمَا فِى ٱلْأَرْضِ ۗ أَلَآ …
- 43:43:7 [صِرَٰط N] فَٱسْتَمْسِكْ بِٱلَّذِىٓ أُوحِىَ إِلَيْكَ ۖ إِنَّكَ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
- 43:61:9 [صِرَٰط N] وَإِنَّهُۥ لَعِلْمٌۭ لِّلسَّاعَةِ فَلَا تَمْتَرُنَّ بِهَا وَٱتَّبِعُونِ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- 43:64:8 [صِرَٰط N] إِنَّ ٱللَّهَ هُوَ رَبِّى وَرَبُّكُمْ فَٱعْبُدُوهُ ۚ هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ
- 48:2:14 [صِرَٰط N] … مَا تَقَدَّمَ مِن ذَنۢبِكَ وَمَا تَأَخَّرَ وَيُتِمَّ نِعْمَتَهُۥ عَلَيْكَ وَيَهْدِيَكَ صِرَٰطًۭا مُّسْتَقِيمًۭا
- 48:20:17 [صِرَٰط N] … لَكُمْ هَٰذِهِۦ وَكَفَّ أَيْدِىَ ٱلنَّاسِ عَنكُمْ وَلِتَكُونَ ءَايَةًۭ لِّلْمُؤْمِنِينَ وَيَهْدِيَكُمْ صِرَٰطًۭا مُّسْتَقِيمًۭا
- 67:22:11 [صِرَٰط N] أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ

## ق و م — 660 uses; here 1:6:3; lemmas: قَوْم 383; قِيَٰمَة 70; أَقَامَ 54; مُّسْتَقِيم 37; قَامَ 33; قَآئِم 17; مَقَام 14; مُّقِيم 10; ٱسْتَقَٰمُ 10; قَآئِمَة 5; قَيِّم 5; أَقْوَم 4; قَيُّوم 3; قَوَّٰمِين 3; مُقَام 3; إِقَام 2; قَيِّمَة 2; قِيَم 1; إِقَامَت 1; قَوَام 1; مُقَامَة 1; تَقْوِيم 1



===== variants.md =====
## 1. Variant readings (qirāʾāt)

- word 2 · السِّرَاطَ (as-sirāṭa) · ibdāl · Sīn for ṣād — canonical phonetic substitution; emphatic→non-emphatic, semantic identical
- word 2 · الصؗرَاطَ (aṣᶻ-ṣᶻirāṭa) · ibdāl · Intermediate ṣ/z sound (ishmām) — phonetic blend between ṣād and zāy; same lexeme


===== source_access.md =====
# source_access.md — exact Quran passages on demand

Before developing a Quran cross-reference, retrieve its actual text and adjacent context. Use this command, replacing S:A,S:A with the references you need (up to 16 per request):

    python3 -B /Volumes/OZTURK/_projects/prose_generation/_commentary/v14/sources.py --tag sol-argument --ref 1:6 --refs S:A,S:A --context 1

The helper reads only the frozen Quran corpus and logs the returned references and bytes. It never calls a model. Context may be 0, 1, 2 or 3 ayat on each side; use further requests when a scene needs more context. Do not read the entire corpus or unrelated repository files. Copy Quran quotations from returned text or the normalized concordance. Retrieval is for checking and understanding the passages you develop, not for turning all candidates into obligatory quotations. The full preceding prose is reader context, not a quotation source.


===== previous.md =====
# Earlier prose actually available to the reader

This contains only the immediately preceding ayah's actual prose. More distant prose is not supplied; do not assume it explained a reading. A network disclosure plan is not proof of earlier delivery.

## 1:5 — frozen earlier baseline
Fâtiha'nın ilk dört ayeti Allah'tan "O" diye söz eder: hamd O'nundur, O âlemlerin Rabbi, Rahmân ve Rahîm'dir, din gününün sahibidir. Beşinci ayette aynı sesler, sözünü ettikleri kimseye doğrudan döner: {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyâke naʿbudu ve iyyâke nesteʿîn, gloss:yalnız sana kulluk ederiz ve yalnız senden yardım isteriz, source:1:5}. Ayet iki eş yarımdan kurulur. Her yarım "seni" anlamına gelen bir zamirle açılır ve bir fiille kapanır. Birinci fiil kulluk etmeyi, ikincisi yardım dilemeyi söyler. Konuşan tek bir kişi değil, bir "biz"dir. İki fiil de süren, her söylenişte yeniden yapılan bir eylemi anlatır. Kulluk önce gelir, yardım sonra; yardım, zaten verilmiş olan kulluk için istenir. Ayet önceki ayetten bir sahip devralır, {ar:مَٰلِكِ, tr:mâliki, gloss:sahibi, source:1:4}, yani din gününün sahibini. Sahibi olunanlar şimdi konuşur. Sonraki ayete de içi boş bir talep devreder: yardım isteriz, ama ne için? Hemen ardından gelen {ar:ٱهْدِنَا, tr:ihdinâ, gloss:bizi ilet, source:1:6} bu boşluğu doldurur. İstenen yardımın adı, dosdoğru yola iletilmektir.

Türkçe okur burada önemli bir şeyi duyamaz, çünkü Türkçede nesne zaten fiilden önce gelir: "sana kulluk ederiz" sıradan bir cümledir. Genel Arapça dilbilgisi bilgisine dayanarak söylersek, Arapçada olağan dizilişte fiil öne geçer ve "seni" fiilin sonuna ek olarak bitişir. Burada ise zamir fiilden koparılmış, ayrı bir kelime olarak başa alınmıştır: {ar:إِيَّاكَ, tr:iyyâke, gloss:yalnız seni, source:1:5}. Bu öne alış eylemi daraltır: seni, başkasını değil. Türkçe çeviri daraltmayı "yalnız" sözüyle karşılar, ama başa fırlayan "sen"in sarsıntısını karşılayamaz. Üç ayet boyunca üçüncü şahısla anılan birden karşıya geçer. Zamir ayrıca yinelenir. İkinci yarım onu düşürüp birinciye yaslanmaz, "seni" yeniden söyler; böylece daraltma yardım için ayrıca kurulur. Yalnız kulluk değil, yardım da tek muhataba bağlanır. Kur'an aynı kalıbı Allah'ın ağzından da kurar: {ar:فَإِيَّٰىَ فَٱعْبُدُونِ, tr:fe iyyâye faʿbudûn, gloss:öyleyse yalnız bana kulluk edin, source:29:56}. Fâtiha'daki cümle bu buyruğa ikinci şahısla verilmiş bir cevap gibi durur. 2:172 aynı daraltmayı üçüncü şahısla kurar ve onu rızık için şükre bağlar: {ar:إِن كُنتُمْ إِيَّاهُ تَعْبُدُونَ, tr:in kuntum iyyâhu taʿbudûn, gloss:eğer yalnız O'na kulluk ediyorsanız, source:2:172}. Fâtiha'da da hamd kulluktan önce gelmişti. Kulluk cümlesinin içinde muhatabın değişmesine bir örnek de 36:22'dedir: {ar:وَمَا لِىَ لَآ أَعْبُدُ ٱلَّذِى فَطَرَنِى وَإِلَيْهِ تُرْجَعُونَ, tr:ve mâ liye lâ aʿbudu'llezî fataranî ve ileyhi turceʿûn, gloss:beni yaratana neden kulluk etmeyeyim ve siz O'na döndürüleceksiniz, source:36:22}. Konuşan "ben"le başlar ve cümlenin sonunda "siz"e döner.

Bu dönüşün sahnesini görmek için sûrenin başına bakmak gerekir, çünkü "sen" birden gelmez. Ona yedi ayete yayılmış bir yaklaşmayla varılır. Sûre bir adla açılır, ama o adın bağlı olduğu fiil söylenmez: {ar:بِسْمِ, tr:bismi, gloss:adıyla, source:1:1}. Söz bir adın altına girer, ama henüz ne yaptığını söylemez. O ad {ar:ٱللَّهِ, tr:allâhi, gloss:Allah, source:1:1} adıdır. Sözlükte bu ada kaynaklık eden kök {ar:التعبد والمعبود, tr:et-teʿabbud ve'l-maʿbûd, gloss:tapınma ve tapınılan, source:ء ل ه B001} diye tanımlanır. Yani ad kendi içinde "kendisine kulluk edilen" demektir. Bu ad bir yönelişin, gönlün O'na çekilişinin adı olarak da okunur ve "Allâhümme", "ey Allah" diye seslenmeye izin verir; hitabın kapısı daha ilk kelimede aralıktır. Ardından {ar:ٱلْحَمْدُ, tr:el-hamdu, gloss:hamd, source:1:2} gelir. "Hamd ederim" denmez, yalnızca "hamd" denir. Sahibi söylenmemiş bu övgü, okuyan herkesi kendine ortak eder. Övgü {ar:رَبِّ, tr:rabbi, gloss:Rabbi, source:1:2} ile adı yeniden söyler. {ar:ٱلرَّحْمَٰنِ, tr:er-rahmâni, gloss:Rahmân, source:1:3} ve {ar:ٱلرَّحِيمِ, tr:er-rahîmi, gloss:Rahîm, source:1:3} ile sürer, {ar:مَٰلِكِ, tr:mâliki, gloss:sahibi, source:1:4} ile biter. Bunların hepsi Arapçada "Allah'a" sözüne bağlı tek bir tamlama zinciri olarak akar ve cümle nefes almadan sıfattan sıfata geçer. Merhamet dönüşten hemen önce, iki kez anılır; istemeyi mümkün kılan budur. Sahip zincirin son üçüncü şahıs halkasıdır. Onun yanındaki {ar:ٱلدِّينِ, tr:ed-dîni, gloss:din yani karşılık ve itaat, source:1:4} sözü de hesap gününü anlatırken, şimdi yerine getirilen itaati de içinde taşır. İtaat "şimdi"ye değdiği anda zincir kopar ve "sen" gelir: az önce "O" olan, karşıdaki olur. Önce kulluk verilir, sonra yardım hiçbir aracıya başvurulmadan doğrudan O'ndan istenir ve istenen şeyin adı konmaz. {ar:ٱهْدِنَا, tr:ihdinâ, gloss:bizi ilet, source:1:6} sûrenin tek buyruk kipidir ve "-nâ" ekiyle yine çoğuldur; açık bırakılan istek burada adını bulur. {ar:أَنْعَمْتَ, tr:enʿamte, gloss:nimet verdin, source:1:7} ile hitap sürer ve sûre sonuna kadar "sen"e konuşur. Sahne bir eşikte başlar: ad anılır, sıfatlar sayılır, "Sahip" denir. Sonra konuşan kendini Sahip'in önünde bulur ve ilk sözü kim olduğunu söylemek olur: "sana kulluk ederiz". Sahibi olunan kişi, sahibine sesini yöneltmiştir. Bir statünün adı olan kölelik, burada bir hitabın diline dönüşür.

Bu ilk fiil Türkçeye "kulluk ederiz" ya da "ibadet ederiz" diye geçer. İki karşılık da bir şeyi tutar: "kul" sahip olunan kişiyi, "ibadet" Tanrı'ya yönelen tapınmayı karşılar. Arapça sözlüğün bu koldaki tanımı da budur: {ar:العبادة والطاعة الخاضعة, tr:el-ʿibâde ve't-tâʿatu'l-hâdıʿa, gloss:tapınma ve boyun eğerek itaat, source:ع ب د B003}. Ama iki Türkçe kelime de daralmıştır. "İbadet" bugün çoğu zaman belli vakitlerde yapılan belli eylemlerin adıdır; "kulluk" ise bir unvan gibi durur. Arapça kökün bunlardan daha maddi, elle tutulur bir resmi vardır. Sözlük kökün pek çok kolunu tek bir işlemde birleştirir: {ar:التذليل والتسوية, tr:et-tezlîl ve't-tesviye, gloss:uysallaştırma ve düzleme, source:ع ب د B005}. Kastedilen, bir şeyi üzerinde çalışarak uysal, düz ve kullanılır hale getirmektir. Aynı kök sahip olunan insanı, boyun eğerek tapınmayı ve zorla boyunduruğa almayı adlandırır. Ayak altında düzleşmiş yolu, derisine katran sürülerek uysallaştırılmış deveyi, katranla ya da yağla kaplanıp suya dayanıklı kılınmış gemiyi de bu kök anlatır. Türkçe bu resmi yitirir. Kulluk, işlenmiş, düzlenmiş, artık yük taşıyabilen bir şeyin hali olarak duyulmaz. Aşağıdaki okumalar bu resmi geri getirir. Olağan anlam, yani Allah'a boyun eğip tapınmak, hepsinin altında yerinde durur.

Resmin en açık yüzü yoldur. Sözlük kökün bir kolunu şöyle kaydeder: {ar:الطريق المعبد وهو المسلوك المذلل, tr:et-tarîku'l-muʿabbed ve huve'l-meslûku'l-muzellel, gloss:çok yürünerek düzleşmiş yani çiğnenip kolaylaşmış yol, source:ع ب د B005}. Bu yol yapılarak değil, üzerinden geçilerek düzleşmiştir. Her ayak biraz toprağı bastırır, biraz taşı yerinden oynatır. Yeterince yürününce patika kendiliğinden yol olur. Tanımın iki kelimesi, "yürünen" ve "kolaylaştırılmış", Kur'an'da arıya verilen buyrukta yan yana geçer: {ar:فَٱسْلُكِى سُبُلَ رَبِّكِ ذُلُلًۭا, tr:feslukî subule rabbiki zululen, gloss:Rabbinin kolaylaştırılmış yollarında yürü, source:16:69}. Yollar "Rabbinin" yollarıdır. Düzlenmiş yol, kimse üzerinde yürümeden önce 1:2'de anılan Rabb'e aittir. Aynı düzleme işi hayvan üzerinde de anlatılır: {ar:وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ, tr:ve zellelnâhâ lehum fe minhâ rakûbuhum, gloss:onları kendilerine boyun eğdirdik de bir kısmına binerler, source:36:72}. Kur'an bir yerde meyve salkımlarının bile böyle alçaltılıp ele verildiğini söyler (76:14). Uysallaştırma burada Allah'ın yarattıkları üzerindeki kendi işidir. Böylece yol ile kul tek bir işlemin iki yüzü olur. Kulluk edenler, üzerinde yürüdükleri yolu yürüyüşleriyle düzleyenlerdir. Kulluk, yol açan bir yürüyüştür ve yolun kolaylığı yürüyenin uysallığından gelir. Kur'an bu bağı açıkça kurar. "Bana kulluk edin" buyruğunu {ar:هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ, tr:hâzâ sırâtun mustakîm, gloss:bu dosdoğru bir yoldur, source:36:61} izler. Îsâ da aynı cümleyi kulluk buyruğunun hemen ardından söyler (3:51, 43:64). Fâtiha'da bu yol bir sonraki ayette istenecektir. Sûrenin sonunda da yolun bir çatala vardığı görülecektir: bir yanda üzerinde nimet verilenlerin yürüdüğü yol, öbür yanda ondan dönenler ve sapıp kaybolanlar. "Kulluk ederiz" diyenler, istedikleri yolun zemini üzerinde çoktan yürümektedir.

Resmin ikinci yüzü sahipliktir. Sözlük kulu sahiplik kökünden tanımlar: {ar:العبد وهو المملوك, tr:el-ʿabdu ve huve'l-memlûk, gloss:kul yani sahip olunan, source:ع ب د B001}. "Memlûk", 1:4'teki "mâlik" ile aynı köktendir. Önceki ayet sahibi göstermişti, bu ayet sahip olunanı konuşturur; ikisi tek bir tanımın iki ucudur. Başka bir kökün sözlük satırı da aynı ilişkiyi din kelimesinin kökünden kurar: {ar:العبد مدين كأنهما أذلهما العمل, tr:el-ʿabdu medîn ke-ennehume'zellehume'l-ʿamel, gloss:kul boyunduruk altındadır sanki çalışmak ikisini de alçaltmıştır, source:د ي ن B004}. Kur'an kulu kendi sözleriyle de sahiplikle tanımlar: {ar:عَبْدًۭا مَّمْلُوكًۭا لَّا يَقْدِرُ عَلَىٰ شَىْءٍۢ, tr:ʿabden memlûken lâ yakdiru ʿalâ şey', gloss:hiçbir şeye gücü yetmeyen sahip olunan bir kul, source:16:75}. Kapsam da evrenseldir: göklerde ve yerde olan herkes Rahmân'a {ar:إِلَّآ ءَاتِى ٱلرَّحْمَٰنِ عَبْدًۭا, tr:illâ âti'r-rahmâni ʿabden, gloss:ancak Rahmân'a kul olarak gelir, source:19:93}. Ama kökün iki ucu vardır. Bir ucunda insanı köleye çevirmek durur: {ar:استعبدت فلانا اتخذته عبدا, tr:isteʿbedtu fulânen ittehaztuhu ʿabden, gloss:birini köle edindim, source:ع ب د B004}. Öbür ucunda ise saygı gösterilip yüceltilen kişi: {ar:المعبد المكرم والمعظم كأنه يعبد, tr:el-muʿabbedu'l-mukerrem ve'l-muʿazzam ke-ennehu yuʿbed, gloss:kendisine tapılıyormuş gibi ağırlanan ve yüceltilen kişi, source:ع ب د B006}. Hangi ucun kastedildiğini sûrenin açılışı belirler. Kendisine kulluk edilen, adı "tapınılan" olan ve övülendir; kulluk nesnesini yüceltir. Kur'an iki ucu da açıkça anlatır. Firavun İsrâiloğulları'nı köleleştirir ve bunu bir "nimet" diye başa kakar (26:22). Allah'ın kulları hakkında ise {ar:بَلْ عِبَادٌۭ مُّكْرَمُونَ, tr:bel ʿibâdun mukramûn, gloss:bilakis ağırlanmış kullardır, source:21:26} denir. Onur yalnız kulluk edilene değil, kulluk edene de düşer. Hiçbir peygamber insanlara {ar:كُونُوا۟ عِبَادًۭا لِّى مِن دُونِ ٱللَّهِ, tr:kûnû ʿibâden lî min dûni'llâh, gloss:Allah'ı bırakıp bana kul olun, source:3:79} diyemez. Firavun'dan da Allah'ın kulları geri istenir (44:18). Sahip–sahip olunan bağı, yalnız bu muhatapla kurulduğunda bir yüceltme olur.

Sahip olunan, eski dünyada fiyatı olan bir maldır. Kur'an bu çıplak gerçeği bir alışverişe çevirir: {ar:إِنَّ ٱللَّهَ ٱشْتَرَىٰ مِنَ ٱلْمُؤْمِنِينَ أَنفُسَهُمْ وَأَمْوَٰلَهُم, tr:inna'llâhe'şterâ mine'l-mu'minîne enfusehum ve emvâlehum, gloss:Allah müminlerden canlarını ve mallarını satın aldı, source:9:111}. Bedel cennettir. Satılanların listesi de hemen ardından {ar:ٱلتَّٰٓئِبُونَ ٱلْعَٰبِدُونَ ٱلْحَٰمِدُونَ, tr:et-tâ'ibûne'l-ʿâbidûne'l-hâmidûn, gloss:tövbe edenler kulluk edenler hamd edenler, source:9:112} diye açılır. Sahip olunan kul, tapınma ve 1:2'nin hamdı tek bir sözleşmede buluşur. Bu alışverişin ardında 1:4'ün din kelimesinin bir yüzü de durur: vadesi belli bir borç ve vadenin geldiği gün hesabı kapatan Sahip. Bu dinlemede "yardım isteriz", borcunu ödemek için yardımı alacaklının kendisinden istemek olur. Arapça kulak burada bir ses akrabalığı da duyabilir. İkinci fiilin sesi, "göz" ve "pınar" anlamlarıyla birlikte "peşin para" anlamını da taşıyan bir köke yakındır: {ar:النقد الحاضر, tr:en-nakdu'l-hâdır, gloss:elde hazır bulunan para, source:ع ي ن B011}. Bu, fiilin kökü değildir; aşağıda üzerinde durulacak bir çağrışımdır. Ama borcun karşısında elde hazır olanı hatırlatır. Aynı yerde bir güvence de vardır. Kendi başına bırakılan kişi yalnızca kendi verdiği sözle ayakta kalır. Yardım isteyen ise kendi sözüne terk edilmemeyi ister. Bir hükmün altında olan, esir gibi sürüklenmek yerine korunan bir sığınan olarak içeri alınmayı diler. Sûrenin başında anılan ad, bu isteği bağlayan bir yemin ve sözleşme gibi arka planda durur.

Bu kökte uysallığın karşısında başka bir şey de durur; yoksa kulluk yalnızca yumuşayıp ezilmek olurdu. Sözlük aynı kökten bir kol daha kaydeder: {ar:العبدة وهي القوة والصلابة, tr:el-ʿabedetu ve hiye'l-kuvvetu ve's-salâbe, gloss:güç ve sağlamlık, source:ع ب د B007}. Anlatılan, bir varlığın güçlü, sağlam ve zamana dayanıklı olmasıdır. Çiğnenen yol yumuşamaz, sertleşir. Katranlanan deve uysallaşır, ama yük taşıyacak kadar da güçlüdür. Uysallaştırma sağlamlığı yok etmez, onu işe yarar hale getirir. Kur'an bunu bir kulun adlandırılışında gösterir: {ar:وَٱذْكُرْ عَبْدَنَا دَاوُۥدَ ذَا ٱلْأَيْدِ, tr:vezkur ʿabdenâ dâvûde ze'l-eyd, gloss:kulumuz güç sahibi Dâvûd'u an, source:38:17}. Aynı kul için demir yumuşatılır (34:10) ve ona {ar:صَنْعَةَ لَبُوسٍۢ لَّكُمْ, tr:sanʿate lebûsin lekum, gloss:sizin için zırh yapımı, source:21:80} öğretilir. Sertlik, kulun elinde işlenip insanı koruyan bir kalkana döner. Kökte sıcak bir kol da vardır: {ar:العبد مثل الأنف والحمية, tr:el-ʿabed misle'l-enef ve'l-hamiyye, gloss:incinmiş gurur ve kendini koruyan öfke, source:ع ب د B008}. Bu, incinmiş gururla kabaran öfkedir, bazen de bu incinmenin getirdiği kederli sessizliktir. Kur'an kulluğun karşısına tam da böyle bir çekinmeyi koyar: {ar:لَّن يَسْتَنكِفَ ٱلْمَسِيحُ أَن يَكُونَ عَبْدًۭا لِّلَّهِ, tr:len yestenkife'l-mesîhu en yekûne ʿabden lillâh, gloss:Mesih Allah'a kul olmaktan asla çekinmez, source:4:172}. 43:81 ise ikisini tek kelimede buluşturur. "Rahmân'ın bir çocuğu olsaydı {ar:فَأَنَا۠ أَوَّلُ ٱلْعَٰبِدِينَ, tr:fe ene evvelu'l-ʿâbidîn, gloss:ilk kulluk eden ben olurdum, source:43:81}" der. Olağan okunuşta anlam budur; aktarılan bir yorumda ise "ilk öfkelenip reddeden ben olurdum" anlamına gelir. İki okuma bir arada durur: Rahmân'a ilk kulluk eden, O'na çocuk isnadına ilk öfkelenendir. Kök direnen deveyi, insanlara güçlük çıkaran hayvanı da bilir. Uysal binek ile idarecisiyle dövüşen hayvan aynı kökte yan yana durur. Kur'an bu iki kutbu yalnız bir seçim olarak değil, bir yön ayrımı olarak da gösterir: {ar:أَذِلَّةٍ عَلَى ٱلْمُؤْمِنِينَ أَعِزَّةٍ عَلَى ٱلْكَٰفِرِينَ, tr:ezilletin ʿale'l-mu'minîne eʿizzetin ʿale'l-kâfirîn, gloss:müminlere karşı alçakgönüllü inkarcılara karşı zorlu, source:5:54}. Aynı ikilik sûrenin sonunda "üzerlerine" sözünün iki yüzünde görünecektir: nimetin yumuşattığı bir deri ve öfkenin kalınlaştırdığı bir kabuk. Kökteki öfke ve keder bir şey daha bırakır. Bir kaybın ardından ölü için kabaran öfke, cevabı alınmamış bir kanın hararetidir. 1:7 "gazaba uğramışlar"ı andığında bu hararet başka bir yönden, inen bir öfke olarak geri döner.

Kökün bir kolu da dağılmayı anlatır: {ar:العباديد الفرق من الناس الذاهبون في كل وجه, tr:el-ʿabâbîd el-firaku mine'n-nâsi'z-zâhibûne fî kulli vech, gloss:her yöne dağılıp giden insan kümeleri, source:ع ب د B010}. "Kulluk ederiz" diyen çoğul ses, kendi kökünde kendi dağılışının adını da taşır. İkinci fiilin kökü de bir sürüyü adlandırır: {ar:العانة القطيع من حمر الوحش, tr:el-ʿâne el-katîʿu min humuri'l-vahş, gloss:yaban eşeklerinden bir sürü, source:ع و ن B006}. Yan yana konunca iki kelime bir av sahnesi kurar. Bir sürü birlikte otlar, avcılar çıkar ve sürü her yöne kaçar. Sürünün dağılışı ile insan topluluğunun dağılışı aynı kelimeyle söylenir. Kur'an bu sahneyi kendisi çizer. Öğütten yüz çevirenler {ar:كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ, tr:ke-ennehum humurun mustenfira, gloss:sanki ürkmüş yaban eşekleridir, source:74:50} ve bir aslandan kaçarlar. Sûrenin önceki ayetleri bu sürünün bir sahibi olduğunu söylemişti: Rabb ve Sahip. Sonunda da biri sürüden düşecektir. Sözlük "yolunu yitirenler" kelimesinin kökünden şunu kaydeder: {ar:الضالة من الإبل ما يبقى بمضيعة لا يعرف ربها, tr:ed-dâlle mine'l-ibil mâ yebkâ bi-madyeʿa lâ yuʿrafu rabbuhâ, gloss:ortada kalmış ve sahibinin kim olduğu bilinmeyen deve, source:ض ل ل B005}. "Biz"i bir arada tutan iki şeydir: tek bir muhatap ve bir destek. Yardımın kökü karşılıklı yardımlaşmayı da kapsar ve Kur'an bunu buyurur: {ar:وَتَعَاوَنُوا۟ عَلَى ٱلْبِرِّ وَٱلتَّقْوَىٰ, tr:ve teʿâvenû ʿale'l-birri ve't-takvâ, gloss:iyilik ve takva üzerinde yardımlaşın, source:5:2}. Dağılmanın karşısına tek yol konur: {ar:وَلَا تَتَّبِعُوا۟ ٱلسُّبُلَ فَتَفَرَّقَ بِكُمْ عَن سَبِيلِهِۦ, tr:ve lâ tettebiʿu's-subule fe teferraka bikum ʿan sebîlih, gloss:başka yollara uymayın yoksa sizi O'nun yolundan ayırıp dağıtır, source:6:153}. Allah'ın nimetiyle düşmanlar kardeş olur (3:103). Bu çoğul ses nesiller boyu da uzanır. Yakub'un oğulları {ar:نَعْبُدُ إِلَٰهَكَ وَإِلَٰهَ ءَابَآئِكَ, tr:naʿbudu ilâheke ve ilâhe âbâ'ik, gloss:senin ilahına ve atalarının ilahına kulluk ederiz, source:2:133} der. Aynı çoğul fiil, farklı topluluklar arasında ortak bir söz olarak da önerilir: {ar:أَلَّا نَعْبُدَ إِلَّا ٱللَّهَ, tr:ellâ naʿbude illa'llâh, gloss:Allah'tan başkasına kulluk etmememiz, source:3:64}. "Rahmân'ın kulları" da ortak bir yürüyüşü olan, adı konmuş bir topluluktur: {ar:وَعِبَادُ ٱلرَّحْمَٰنِ ٱلَّذِينَ يَمْشُونَ عَلَى ٱلْأَرْضِ هَوْنًۭا, tr:ve ʿibâdu'r-rahmâni'llezîne yemşûne ʿale'l-ardı hevnen, gloss:Rahmân'ın kulları yeryüzünde yumuşak yürüyenlerdir, source:25:63}. Fâtiha'daki "biz", dağılabilecek bir sürünün tek sahibine dönmüş sesidir.

Kökün en dramatik kolu bir yolcuyu yolda bırakır: {ar:أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت, tr:uʿbide bi-fulân bi-maʿnâ ubdiʿa bih izâ kellet râhilatuhû ev ʿatibet, gloss:bineği yorulup tükendiğinde ya da sakatlandığında biri yolda kaldı, source:ع ب د B011}. Sahneyi somut düşünmek gerekir. Çölde bir yolcunun devesi çöker. Su ve azık sırttadır ve varılacak yer uzaktır. Yolcu yürüyerek gidemez, beklese de kurtulamaz. Kur'an bu çaresizliği yük hayvanlarının nimetini anlatırken çizer. Onlar olmasaydı uzak bir diyara {ar:لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ, tr:lem tekûnû bâliğîhi illâ bi-şıkkı'l-enfus, gloss:canınızı parçalamadan varamayacaktınız, source:16:7}. Ayet Allah'ı "şefkatli, merhametli" diye anarak biter. Bineksiz kalanların sahnesi de vardır. Bazı adamlar savaşa gitmek için binek istemeye gelir, verecek binek bulunmaz ve {ar:تَوَلَّوا۟ وَّأَعْيُنُهُمْ تَفِيضُ مِنَ ٱلدَّمْعِ, tr:tevellev ve aʿyunuhum tefîdu mine'd-demʿ, gloss:gözlerinden yaşlar taşarak döndüler, source:9:92}. Sözlüğün tanımdaki "yorulup tükendi" fiili, 16:76'daki bir benzetmenin anahtar kelimesiyle aynı köktendir. O ayette dilsiz ve hiçbir şeye gücü yetmeyen biri anlatılır: {ar:وَهُوَ كَلٌّ عَلَىٰ مَوْلَىٰهُ, tr:ve huve kellun ʿalâ mevlâh, gloss:o efendisine bir yüktür, source:16:76}. Nereye gönderilse hayır getirmez. Karşısında adaleti emreden ve {ar:وَهُوَ عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:ve huve ʿalâ sırâtın mustakîm, gloss:dosdoğru bir yol üzerinde olan, source:16:76} biri durur. Ayet "bunlar eşit olur mu" diye sorar. Hemen önceki ayet sahip olunan ve hiçbir şeye gücü yetmeyen kulu anlatmıştı. Kur'an'ın kendi dizisi böylece sahip olunandan tükenmişe, tükenmişten dosdoğru yola gider. Fâtiha'da da aynı geçiş vardır. "Kulluk ederiz" diyenlerin kökü yolda kalışı bilir, "yardım isteriz" onları kaldırmayı ister, sonraki ayet de yolu adlandırır.

Kaldıran güç de ikinci fiilin kökündedir. Sözlük bir kolunu {ar:استواء الخلقة وتلاحق القوة, tr:istivâ'u'l-hılka ve telâhuku'l-kuvve, gloss:yapının dengelenmesi ve gücün yaşa yetişmesi, source:ع و ن B005} diye tanımlar. Bu, bir yük hayvanının ya da insanın yaşla birlikte olgun, dengeli bir güce erişmesidir. Bu dinlemede yardım dilemek, kulluk edene yetişen gücü dilemektir. Kur'an bu olgunlaşmayı Mûsâ için anlatır: gücüne erişip yapısı dengelendiğinde ona hüküm ve ilim verilir (28:14). Zülkarneyn de yardımı bir güç olarak ister: {ar:فَأَعِينُونِى بِقُوَّةٍ, tr:fe eʿînûnî bi-kuvve, gloss:bana güçle yardım edin, source:18:95}. Olgunlaşma bir hayat eğrisinin parçasıdır. 46:15 insanı rahimde taşınmış, sütten kesilmiş ve {ar:حَتَّىٰٓ إِذَا بَلَغَ أَشُدَّهُۥ وَبَلَغَ أَرْبَعِينَ سَنَةً, tr:hattâ izâ belağa eşuddehû ve belağa erbaʿîne sene, gloss:sonunda tam gücüne ve kırk yaşına erişince, source:46:15} diye izler. O zaman insan kendisine verilen nimete şükretmeyi diler; biçimlenen, yetiştirilen ve ayağa kalkan beden burada ayakta durur. "Dengelenme" terimi yol kelimesine de geçer. Sonraki ayetteki {ar:ٱلْمُسْتَقِيمَ, tr:el-mustakîm, gloss:dosdoğru, source:1:6} kelimesinin kökü sözlükte {ar:استقامة واعتدال واستواء, tr:istikâme ve iʿtidâl ve istivâ', gloss:dikliğini koruma denge ve düzlük, source:ق و م B008} diye tanımlanır. Kur'an yürüyüşü de aynı terimle anlatır: {ar:أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:em men yemşî seviyyen ʿalâ sırâtın mustakîm, gloss:yoksa dosdoğru yolda dengeli yürüyen mi, source:67:22}. Ara durumu da sonraki ayetin kökü verir: {ar:مشي التهادي مع الاعتماد والتمايل, tr:meşyu't-tehâdî maʿa'l-iʿtimâdi ve't-temâyul, gloss:sallanarak ve başkasına dayanarak yürüme, source:ه د ي B008}. Güçsüz biri iki kişi arasında, onlara yaslanarak ilerler. Yolun kelimesi bineğin durmasını da bilir: {ar:جمود ووقوف وكلال, tr:cumûd ve vukûf ve kelâl, gloss:donma durma ve yorgunluk, source:ق و م B016}. Böylece 1:5'ten 1:6'ya bir hareket akar: yolda kalmak, yaslanmak ve doğrulup ayağa kalkmak. Bu harekette bir ses de karşılık bulur. "Yardım isteriz" kelimesi, Arapçada bir şeyi istemeyi ya da kendine yöneltmeyi bildiren istefʿale kalıbındadır. "Dosdoğru" kelimesi de aynı kalıptan gelir; kendini dik tutan, ayakta kalarak ilerleyen bir duruşu anlatır. Aynı kalıbın iki kelimesi birbirine cevap verir: yardım isteyene verilen, kendini dik tutan bir yoldur. Bu dua da ayakta, namazın kıyamında okunur. Kök bir de hızı bilir: {ar:ما عبد أن فعل ذاك أي ما لبث, tr:mâ ʿabede en feʿale zâk ey mâ lebis, gloss:onu yapmakta hiç gecikmedi, source:ع ب د B009}. Aynı kol koşuda biraz hızlanmayı da anlatır; yolda kalan binek yeniden koşar. Kur'an bağışlanmaya koşmayı buyurur (3:133), ama Rahmân'ın kullarının yürüyüşü yumuşaktır. Çabukluk adımda değil, niyettedir.

Türkçe "yardım istemek" bu fiilin çekirdeğini tutar, ama üç şeyi yitirir. Birincisi sözlüğün koldaki imgesidir: {ar:الإعانة والمظاهرة, tr:el-iʿâne ve'l-muzâhera, gloss:yardım etme ve arka çıkma, source:ع و ن B001}. "Muzâhera", kavgada birinin sırtına geçip arkasında durmaktır; Türkçedeki "arka çıkmak" deyimi buna yakındır. Kur'an bu kelimeyi meleklerin desteği için kullanır: {ar:وَٱلْمَلَٰٓئِكَةُ بَعْدَ ذَٰلِكَ ظَهِيرٌ, tr:ve'l-melâ'iketu baʿde zâlike zahîr, gloss:melekler de bundan sonra arka çıkandır, source:66:4}. İkincisi, yardımın bir şey ya da kişi olarak düşünülmesidir: {ar:كل شيء استعنت به أو أعانك فهو عونك, tr:kullu şey'in isteʿanet bihî ev eʿâneke fe huve ʿavnuk, gloss:yardımına başvurduğun ya da sana yardım eden her şey senin yardımcındır, source:ع و ن B001}. Üçüncüsü dilbilgisindedir. Türkçe "senden" der ve Allah'ı yardımın çıkıp geldiği bir kaynak yapar. Arapçada ise muhatap doğrudan nesnedir, doğrudan kendisine başvurulandır. Kur'an bu fiili başka yerlerde çoğunlukla bir "ile" ekiyle kurar; bu ek aracı ya da başvurulanı gösterir. Mûsâ kavmine {ar:ٱسْتَعِينُوا۟ بِٱللَّهِ وَٱصْبِرُوٓا۟, tr:isteʿînû bi'llâhi vasbirû, gloss:Allah'tan yardım dileyin ve sabredin, source:7:128} der. Bu örnek, eki taşıyan kullanımların Allah'ı ille de bir araç yapmadığını gösterir. Fâtiha'yı ayıran, yalın ve başa alınmış nesnedir. Kur'an bunun karşılığını bir sıfatta da kurar: {ar:وَرَبُّنَا ٱلرَّحْمَٰنُ ٱلْمُسْتَعَانُ, tr:ve rabbuna'r-rahmânu'l-musteʿân, gloss:Rabbimiz Rahmân'dır yardımına başvurulandır, source:21:112}. Bu ayetteki dizi, Fâtiha'nın Rabb, Rahmân ve yardım istenen dizisiyle aynıdır. Aynı kalıp 12:18'de Yakub'un ağzında da geçer.

Bu fiil kalıbı Kur'an'da altı kez geçer ve Fâtiha dışındaki beş kullanımın dördünde sabırla birlikte gelir. Sabır ve namaz, yardımın kendisiyle istendiği şeylerdir: {ar:وَٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ, tr:vesteʿînû bi's-sabri ve's-salâ, gloss:sabır ve namazla yardım dileyin, source:2:45}. Aynı buyruk 2:153'te yinelenir. Fâtiha ise namazın içinde söylenir; yardım, istendiği yerde istenir. Sabır eşlemesi kulluk fiilinin kendisine de uzanır: {ar:فَٱعْبُدْهُ وَٱصْطَبِرْ لِعِبَٰدَتِهِۦ, tr:faʿbudhu vastabir li-ʿibâdetih, gloss:O'na kulluk et ve O'na kullukta sabırlı ol, source:19:65}. 7:128'de de yardım dileme buyruğunu, yeryüzünün Allah'ın "kullarından" dilediğine verileceği sözü izler; yardım ile kulluk orada da yan yanadır. Kulluk ile dayanma tek bir buyrukta, Fâtiha'daki sırayla da gelir: {ar:فَٱعْبُدْهُ وَتَوَكَّلْ عَلَيْهِ, tr:faʿbudhu ve tevekkel ʿaleyh, gloss:O'na kulluk et ve O'na dayan, source:11:123}. Önce kulluk, sonra dayanma gelir. Bu, tek bir ilişkinin iki yüzüdür: verilen bağlılık ve o bağlılığı taşıyan destek. Fiillerin süreklilik bildiren kipi de bir buyrukta açıkça söylenir: {ar:وَٱعْبُدْ رَبَّكَ حَتَّىٰ يَأْتِيَكَ ٱلْيَقِينُ, tr:vaʿbud rabbeke hattâ ye'tiyeke'l-yakîn, gloss:kesin olan gelinceye dek Rabbine kulluk et, source:15:99}. Başka bir ayette dua etmek ve kulluk etmek aynı iş sayılır: {ar:ٱدْعُونِىٓ أَسْتَجِبْ لَكُمْ, tr:udʿûnî estecib lekum, gloss:bana dua edin size cevap vereyim, source:40:60}. Ayet dua etmeyi reddedenleri "kulluğuma büyüklenenler" diye anar. Böylece ayetin iki yarımı birbirini açıklar: yardım dilemek bir kulluktur, kulluk ise süren bir yardım dileyişidir.

Arapça kulağa açık, Türkçede ise görünmez bir şey daha vardır. Genel dilbilgisi bilgisine dayanarak söylersek, ortası "v" olan bir kök ile ortası "y" olan bir kök bu kalıpta aynı sesi verir. Bu yüzden "yardım isteriz" kelimesinde "göz", "pınar", "bizzat kendi" anlamlarını taşıyan başka bir kök de çınlar. Bu kök kelimenin sözlük kökü değildir, bir ses akrabasıdır. Bu çağrışımla dinlenince yardım, bir gözün koruması altında olmaya dönüşür: {ar:عين الحفظ والرعاية, tr:ʿaynu'l-hıfz ve'r-riʿâye, gloss:koruyan ve gözeten göz, source:ع ي ن B003}. Sözlüğün bu kolda verdiği deyim "sen gözümün üstündesin"dir. Kur'an yardımla eşlenen sabrı tam bu göze dayandırır: {ar:وَٱصْبِرْ لِحُكْمِ رَبِّكَ فَإِنَّكَ بِأَعْيُنِنَا, tr:vasbir li-hukmi rabbike fe inneke bi-aʿyuninâ, gloss:Rabbinin hükmüne sabret çünkü sen gözlerimizin önündesin, source:52:48}. Sûrenin kendi resimlerinde de göz, işaretleri okuyan göz olarak durur. Âlemler işarettir ve onları okuyan yola iletilir. Sonraki ayetlerde bebeği sağlam ama görmeyen bir göz ve sevinçle dinginleşen bir göz belirir. Yardım isteyen, hem korunan hem de görmeye muhtaç olan bir gözün sahibidir.

Yardımın kökü bir savaşı da adlandırır: {ar:الحرب العوان التي كانت قبلها حرب بكر, tr:el-harbu'l-ʿavân elletî kânet kablehâ harbun bikr, gloss:kendisinden önce bir ilk savaş olmuş olan yinelenmiş savaş, source:ع و ن B003}. İlk değildir, arkasında bir başkası vardır. "Arka çıkma" imgesi burada yerine oturur: tekrar tekrar çarpışılan bir sahada, arkanızda durana ihtiyacınız vardır. Kur'an böyle bir ikinci kavgayı anlatır. Mûsâ bir gün birine yardım etmiştir. Ertesi gün {ar:فَإِذَا ٱلَّذِى ٱسْتَنصَرَهُۥ بِٱلْأَمْسِ يَسْتَصْرِخُهُۥ, tr:fe iza'llezi'stensarahû bi'l-emsi yestasrihuh, gloss:dün ondan yardım isteyen adam yine feryatla onu çağırıyordu, source:28:18}. Arada Mûsâ bir söz vermiştir: {ar:فَلَنْ أَكُونَ ظَهِيرًۭا لِّلْمُجْرِمِينَ, tr:fe len ekûne zahîran li'l-mucrimîn, gloss:artık suçlulara asla arka çıkmayacağım, source:28:17}. Bu sözü "bana verdiğin nimet hakkı için" diye, 1:7'nin "nimet verdin" fiiliyle kurar. İnsanlar arası yardım nesnesiyle yargılanır: iyiliğe yardım buyrulur, günaha yardım yasaklanır. İnkarcılar Peygamber için {ar:وَأَعَانَهُۥ عَلَيْهِ قَوْمٌ ءَاخَرُونَ, tr:ve eʿânehû ʿaleyhi kavmun âharûn, gloss:başka bir topluluk ona bunda yardım etti, source:25:4} diye suçlamada bulunur. Fâtiha'nın ikinci "yalnız sen"i, yardım yönünde bu kadar karışık bir dünyada yardımın adresini tek bir yere sabitler. Bedir'de bu yardım, arkadan birbirini izleyerek gelen melekler olarak görünür (8:9). Kulun sağlamlığı savaşta saf tutmaya da dönüşür. Kur'an savaşanları {ar:كَأَنَّهُم بُنْيَٰنٌۭ مَّرْصُوصٌۭ, tr:ke-ennehum bunyânun mersûs, gloss:sanki kenetlenmiş bir yapıdırlar, source:61:4} diye niteler. Aynı Kur'an en büyük yapının dayanağını görünür direklerden de alır: göklerin {ar:رَفَعَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا, tr:rafeʿa's-semâvâti bi-ğayri ʿamedin teravnehâ, gloss:gökleri gördüğünüz direkler olmadan yükseltti, source:13:2} diye yükseltildiğini söyler. Böylece kenetlenen safların sağlamlığı görünmeyen bir dayanağa bağlanır. Önceki ayetin "gün" kelimesi Arapların savaş günlerini de bilir: {ar:كائنة اليوم وشدته, tr:kâ'inetu'l-yevmi ve şiddetuh, gloss:günün büyük olayı ve çetinliği, source:ي و م B003}. Yardım isteyenler, çetin bir günün ve yolda pusuya yatmış olanların karşısında arkalarında duracak olanı çağırır.

Aynı kök ortadaki durumu da adlandırır: {ar:العوان البقرة النصف في سنها ويقال للمرأة النصف عوان, tr:el-ʿavân el-bakaratu'n-nasafu fî sinnihâ ve yukâlu li'l-mer'eti'n-nasafi ʿavân, gloss:yaşça orta çağdaki inek ve orta yaşlı kadın, source:ع و ن B002}. Kur'an bu kelimeyi bir kez kullanır ve hemen bir çerçeve kurar: {ar:لَّا فَارِضٌۭ وَلَا بِكْرٌ عَوَانٌۢ بَيْنَ ذَٰلِكَ, tr:lâ fâridun ve lâ bikrun ʿavânun beyne zâlik, gloss:ne yaşlı ne genç ikisinin arası orta yaşta, source:2:68}. "Ne o ne bu, arası" diye kurulan bu çerçeve, Fâtiha'nın son cümlesinde yankılanır: ne gazaba uğrayanlar ne de yolunu yitirenler. Bu dinlemede dosdoğru yol, dışarıda bırakılan iki ucun ortası olur. Kur'an aynı çerçeveyi başka yerlerde de kurar ve onu dosdoğru kelimesinin köküyle adlandırır: {ar:وَكَانَ بَيْنَ ذَٰلِكَ قَوَامًۭا, tr:ve kâne beyne zâlike kavâmen, gloss:bu ikisinin arasında dengeli bir ölçü olur, source:25:67}. Bu söz, Rahmân'ın kullarının harcayışını anlatan portrenin içindedir; kulluk kökü ile ortadaki durum orada tek bir portrede buluşur. Namazda da ne yüksek ne gizli bir ses istenir ve "bunun arasında bir yol" aranır (17:110). Ama bir sınır da vardır. Allah için seçilen ineğin ortada oluşu, uysallaştırılmamış oluşuyla da tanımlanır: {ar:لَّا ذَلُولٌۭ تُثِيرُ ٱلْأَرْضَ, tr:lâ zelûlun tusîru'l-ard, gloss:toprağı sürmek için boyunduruğa alınmamış, source:2:71}. Kulluğun uysallaştırma resmi sunağın önünde durur; orada seçilen, hiç boyunduruk görmemiş olandır. Ortadaki durum kadın için evlenmiş olmayı da çağrıştırabilir. Kur'an kulluk kökünü tam bu ölçeğin yanına koyar: {ar:عَٰبِدَٰتٍۢ سَٰٓئِحَٰتٍۢ ثَيِّبَٰتٍۢ وَأَبْكَارًۭا, tr:ʿâbidâtin sâ'ihâtin seyyibâtin ve ebkâren, gloss:kulluk eden oruç tutan dul ve bakire kadınlar, source:66:5}. Ayetin iki kökü burada bir evin kuruluşunda yan yana gelir. Kulluk kökündeki sağlamlık, böyle bir evin savunulmasında durur. Yardımın kökü de evlenip bir evin içine alınmış kadını adlandırır.

İlk kelimeye dönünce, bütün bu resimleri bir arada tutan işlemin ayırmak olduğu görülür. "Yalnız seni", bir şeyi kendi ötekisinden ayırır. Ses akrabası kök burada da bir şey söyler: {ar:عين الشيء نفسه, tr:ʿaynu'ş-şey'i nefsuh, gloss:şeyin bizzat kendisi, source:ع ي ن B013}. İki kez söylenen "seni", bizzat bu Olan'dır. Sûrenin sonundaki {ar:غَيْرِ, tr:ğayri, gloss:olmayan yani öteki, source:1:7} ise öteki, dışarıda bırakılandır. Onun sözlükteki tanımı {ar:السوى والخلاف والاستثناء والنفي, tr:es-sivâ ve'l-hilâf ve'l-istisnâ' ve'n-nefy, gloss:başkalık aykırılık istisna ve olumsuzlama, source:غ ي ر B005} şeklindedir. Kur'an "öteki"ni doğrudan kulluğun karşısına koyar: {ar:أَفَغَيْرَ ٱللَّهِ تَأْمُرُوٓنِّىٓ أَعْبُدُ, tr:e fe ğayra'llâhi te'murûnnî aʿbud, gloss:bana Allah'tan başkasına mı kulluk etmemi emrediyorsunuz, source:39:64}. Nûh da "Allah'a kulluk edin, O'ndan başka ilahınız yok" der (7:59). Bu çağrıda ilah ile kulluk birbirini tanımlar. Sözlük ise kulluk kökünün bu kolunu {ar:عبد يعبد عبادة فلا يقال إلا لمن يعبد الله, tr:ʿabede yaʿbudu ʿibâdeten fe lâ yukâlu illâ li-men yaʿbudu'llâh, gloss:bu söz ancak Allah'a kulluk eden için söylenir, source:ع ب د B003} diye daraltır. Kur'an bu daraltmayı sınırlar: aynı "kulluk ederiz" fiili putlara da yönelebilir, {ar:قَالُوا۟ نَعْبُدُ أَصْنَامًۭا فَنَظَلُّ لَهَا عَٰكِفِينَ, tr:kâlû naʿbudu asnâmen fe nezallu lehâ ʿâkifîn, gloss:putlara kulluk ederiz ve onlara bağlı kalırız dediler, source:26:71}. Fiil kendi başına nesnesini seçmez. Fâtiha'nın başa aldığı "seni" bu yüzden gereklidir. Aynı fiilin olumsuz aynası ise {ar:لَآ أَعْبُدُ مَا تَعْبُدُونَ, tr:lâ aʿbudu mâ taʿbudûn, gloss:sizin kulluk ettiğinize ben kulluk etmem, source:109:2} cümlesidir. Kulluğun Kur'an'daki adı da bu ayırmadır: {ar:فَٱعْبُدِ ٱللَّهَ مُخْلِصًۭا لَّهُ ٱلدِّينَ, tr:faʿbudi'llâhe muhlisan lehu'd-dîn, gloss:dini yalnız O'na has kılarak Allah'a kulluk et, source:39:2}. Bu ifade 1:4'ün din kelimesini kulluğa bağlar ve daraltmaya bir ad verir.

Neden yardımın da yalnız kulluk edilenden istendiğini İbrahim babasına sorar: {ar:لِمَ تَعْبُدُ مَا لَا يَسْمَعُ وَلَا يُبْصِرُ وَلَا يُغْنِى عَنكَ شَيْـًۭٔا, tr:lime taʿbudu mâ lâ yesmeʿu ve lâ yubsıru ve lâ yuğnî ʿanke şey'en, gloss:işitmeyen görmeyen sana hiçbir yarar sağlamayana neden kulluk ediyorsun, source:19:42}. Kulluk edilen yardım edemiyorsa, iki yarım birbirinden kopar. Fâtiha'nın iki "yalnız sen"i onları aynı muhatapta birleştirir. Kur'an bu daraltmayı bir hesap sahnesine de taşır. Mahşerde meleklere {ar:أَهَٰٓؤُلَآءِ إِيَّاكُمْ كَانُوا۟ يَعْبُدُونَ, tr:e hâ'ulâ'i iyyâkum kânû yaʿbudûn, gloss:bunlar size mi kulluk ediyorlardı, source:34:40} diye sorulur. Aynı başa alınmış zamir burada bir denetimin sorusudur: gerçekte kime kulluk edildi? Ortak koşulanlar da orada kendilerine kulluk edilmediğini söyleyerek kulluk edenlerden kopar (10:28). Yardım yönündeki daraltma ise darlık anında kendiliğinden ortaya çıkar. Denizde bir sıkıntı bastırınca {ar:ضَلَّ مَن تَدْعُونَ إِلَّآ إِيَّاهُ, tr:dalle men tedʿûne illâ iyyâh, gloss:O'ndan başka yalvardıklarınız kaybolur gider, source:17:67}. 6:41 de aynı anı "bilakis yalnız O'na yalvarırsınız" diye anlatır. "Kaybolur" diye çevrilen fiil, sûrenin son kelimesi {ar:ٱلضَّآلِّينَ, tr:ed-dâllîn, gloss:yolunu yitirenler, source:1:7} ile aynı köktendir. Başka muhataplar, fırtınada bir sisin içinde kaybolur gibi yok olur; yalnız başa alınmış olan kalır. Kulluğun kapsamı da en genişiyle söylenir: {ar:وَمَا خَلَقْتُ ٱلْجِنَّ وَٱلْإِنسَ إِلَّا لِيَعْبُدُونِ, tr:ve mâ halaktu'l-cinne ve'l-inse illâ li-yaʿbudûn, gloss:cinleri ve insanları ancak bana kulluk etsinler diye yarattım, source:51:56}. "Biz"in içine, bu amaçla yaratılmış olan herkes girer.

Kulluk bir şeyi yöneltir, bir şeyin nereye gönderildiğini belirler. Sonraki ayetin kökü, bir kutsal yere gönderilen adağı adlandırır: {ar:الهدي المهدى إلى الحرم, tr:el-hedy el-muhdâ ile'l-harem, gloss:kutsal bölgeye gönderilen adak, source:ه د ي B005}. Sürüden seçilen hayvan işaretlenir ve Beyt'e doğru sürülür. Ona hedefini veren, tapınmadır. Bu dinlemede "bizi ilet", "bizi gönder" diye de duyulur: konuşanlar ait oldukları yere götürülmek ister. Yardımlaşmayı buyuran ayet de adağa dokunmayı yasaklar: {ar:وَلَا ٱلشَّهْرَ ٱلْحَرَامَ وَلَا ٱلْهَدْىَ وَلَا ٱلْقَلَٰٓئِدَ, tr:ve le'ş-şehra'l-harâme ve le'l-hedye ve le'l-kalâ'id, gloss:ne haram ayı ne adağı ne de gerdanlıklı hayvanları, source:5:2}. Yardım ile adak aynı kutsal düzenin içindedir. Aynı sûre bu düzenin insanları ayakta tuttuğunu söyler: {ar:جَعَلَ ٱللَّهُ ٱلْكَعْبَةَ ٱلْبَيْتَ ٱلْحَرَامَ قِيَٰمًۭا لِّلنَّاسِ, tr:ceʿala'llâhu'l-kaʿbete'l-beyte'l-harâme kıyâmen li'n-nâs, gloss:Allah Kâbe'yi yani kutsal Evi insanlar için bir ayakta durma dayanağı kıldı, source:5:97}. Haram ay, adak ve gerdanlıklılar da bu dayanağın içindedir. "Ayakta durma dayanağı" diye çevrilen kelime de dosdoğru kelimesinin köküyle kurulmuştur. Oraya giden yolda yolda kalmış yolcu sahnesi yeniden görünür: insanlar {ar:يَأْتُوكَ رِجَالًۭا وَعَلَىٰ كُلِّ ضَامِرٍۢ, tr:ye'tûke ricâlen ve ʿalâ kulli dâmir, gloss:sana yaya olarak ve her zayıf binek üzerinde gelirler, source:22:27}. Uzak yollardan yürür, hayvanlarını Beyt'e sürerler. Hedef de tek bir yerde toplanır: {ar:قُلْ إِنَّ صَلَاتِى وَنُسُكِى وَمَحْيَاىَ وَمَمَاتِى لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:kul inne salâtî ve nusukî ve mahyâye ve memâtî lillâhi rabbi'l-ʿâlemîn, gloss:de ki namazım ibadetim hayatım ve ölümüm âlemlerin Rabbi Allah içindir, source:6:162}. Bu cümle 1:2'nin sözleriyle biter. Adaktan O'na ulaşan etin kendisi değil, sunanın takvasıdır (22:37). "Kulluk ederiz" diyen, kendini bir adak gibi hedefine yöneltir. "Yardım isteriz" diyen ise oraya varmak için taşınmayı diler.

Kulluk kökünün katran imgesi bir tersaneye de açılır. Aynı kol geminin katranla ya da yağla kaplanmasını anlatır. Tahtalar birbirine eklenir, aralar doldurulur, gövde suyu içeri almayacak hale gelir. Bu, işlenerek dayanıklı kılınmış bir teknedir. Kur'an böyle bir gemi yaptırır: {ar:وَٱصْنَعِ ٱلْفُلْكَ بِأَعْيُنِنَا وَوَحْيِنَا, tr:vasnaʿi'l-fulke bi-aʿyuninâ ve vahyinâ, gloss:gemiyi gözlerimizin önünde ve vahyimizle yap, source:11:37}. Gemi tahtalarla ve bağlarla anlatılır (54:13) ve gözetleyen gözün altında yapılır. 1:2'nin Rabb kelimesinde duyulan gemicilerin başı, {ar:رباني الملاحين, tr:rabbâniyyu'l-mellâhîn, gloss:gemicilerin başı, source:ر ب ب B017}, bu teknenin kaptanıdır. Kur'an'ın anlattığı gemide ise ayrıca bir kaptan yoktur; gemiyi taşıyan, onu gözetleyen gözdür. Katranlanmış gövde ile kaptanı, kul ile Rabb'in ilişkisini denize taşır. "Kulluk ederiz", tahtaları kenetlenip suya dayanıklı kılınmış bir tekne olmayı söyler. "Yardım isteriz" ise o teknenin rotasını tutacak olanı çağırır; rota da sonraki ayetin dosdoğru yoludur. Tersanenin yanında bir koku ve içki tezgahı da durur. Kulluk kökü güzel koku ezilen taşı adlandırır: {ar:العبدة صلاءة الطيب, tr:el-ʿabede salâ'etu't-tîb, gloss:güzel koku ezme taşı, source:ع ب د B012}. Yardımın kökü de şarabıyla anılan bir yeri: {ar:عانات موضع من ناحية الجزيرة تنسب إليه الخمر العانية, tr:ʿânât mevdiʿun min nâhiyeti'l-cezîre tunsebu ileyhi'l-hamru'l-ʿâniyye, gloss:Cezîre yöresinde bir yer ki şarap ona nispet edilir, source:ع و ن B008}. Bu yer adı, bir yolcunun konakladığı, konaklamayı iyi bulduğu bir durak olarak da okunabilir. Kur'an bu koku ve içkiyi bir sahneye çevirir: {ar:كَانَ مِزَاجُهَا كَافُورًا, tr:kâne mizâcuhâ kâfûran, gloss:karışımı kâfur olan, source:76:5}. Bu kadehin kaynağı da {ar:عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا, tr:ʿaynen yeşrabu bihâ ʿibâdu'llâhi yufeccirûnehâ tefcîran, gloss:Allah'ın kullarının içtiği ve fışkırttıkça fışkırttıkları bir pınar, source:76:6} diye anlatılır. Aynı sûre salkımları onların önüne eğer. Kulluk edenlere de hizmet edilir.

Bu son ayette ses akrabası kök ile Allah'ın kulları aynı cümlede buluşur. Ses akrabası kök akan pınarı da adlandırır: {ar:منبع الماء الجاري, tr:menbaʿu'l-mâ'i'l-cârî, gloss:akan suyun kaynağı, source:ع ي ن B006}. Yardım bu çağrışımla dinlenince, kendini yenileyen bir kaynağa dönüşür. Cennet {ar:فِيهَا عَيْنٌۭ جَارِيَةٌۭ, tr:fîhâ ʿaynun câriye, gloss:orada akan bir pınar vardır, source:88:12} diye anlatılır. Yeryüzünde de su isteyene pınar verilir. Mûsâ kavmi için su ister; bu fiil de yardım istemek gibi istefʿale kalıbındadır. Taşa vurulur ve {ar:فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا, tr:fenfeceret minhu'sneta ʿaşrete ʿaynen, gloss:ondan on iki pınar fışkırdı, source:2:60}. Her topluluk kendi içeceği yeri bilir; çok parçalı bir topluluk suya kavuşur ve dağılmaz. Yardımın kökü yaşlı bir hurmayı da adlandırır: {ar:النخلة العَوانة القديمة, tr:en-nahletu'l-ʿavânetu'l-kadîme, gloss:yaşlı eski hurma ağacı, source:ع و ن B004}. Meryem'e doğumdan sonra {ar:وَهُزِّىٓ إِلَيْكِ بِجِذْعِ ٱلنَّخْلَةِ, tr:ve huzzî ileyki bi-cizʿi'n-nahle, gloss:hurma gövdesini kendine doğru salla, source:19:25} denir. Ayağının altında bir su akar ve eski gövde taze hurma verir. Ses akrabası kök güneşin yuvarlağını da adlandırır: {ar:عين الشمس, tr:ʿaynu'ş-şems, gloss:güneş yuvarlağı, source:ع ي ن B008}. Kur'an güneş ile bu kelimeyi gerçekten birleştirir, ama başka türlü: Zülkarneyn güneşi {ar:وَجَدَهَا تَغْرُبُ فِى عَيْنٍ حَمِئَةٍ, tr:vecedehâ tağrubu fî ʿaynin hami'e, gloss:onu kara balçıklı bir pınarda batar buldu, source:18:86}. Orada bu kelime güneşin yuvarlağı değil, güneşin battığı bir pınardır. "Bana güçle yardım edin" diyen de aynı yolculuğun adamıdır. Tapınma kökünün sözlük satırı, güneşin bir zamanlar tapınıldığı için {ar:الإلاهة الشمس, tr:el-ilâhe eş-şems, gloss:güneşe tapınılan olarak verilen ad, source:ء ل ه B001} diye adlandırıldığını kaydeder. Tepede parlayan, günü belirleyen yuvarlak bir zamanlar kulluğa konu olmuştur. "Yalnız seni" onu aşar ve gözü, parlayanın Rabbine yöneltir.

İkinci fiil, sûrenin iyilik düzeninde de bir yer tutar. Rahmân ve Rahîm'de taşan merhamet, alıcısına ulaşmak ister. Rabb'in adım adım yetiştirmesi onu tamamlanmaya götürür ve 1:7'de yola iletilenlerin üzerine nimet olarak iner. Oradan hamd olarak geri döner. Hamd Allah'ındır, ve hiçbir yaratık bu iyiliğin payını kendine çıkaramaz. "Yardım isteriz", muhtacın bu döngünün işlemesini istediği yerdir: iyilik henüz adı konmadan istenir, iki ayet sonra "nimet verdin" diye adlandırılır. Kur'an kaynağı tek bir yere bağlar: {ar:وَمَا بِكُم مِّن نِّعْمَةٍۢ فَمِنَ ٱللَّهِ, tr:ve mâ bikum min niʿmetin fe mine'llâh, gloss:size ulaşan her nimet Allah'tandır, source:16:53}. Yardımın geldiği yer, nimetin geldiği yerdir. Nimeti unutmak ise dönüşü keser; sûrenin son kelimesinin kökünde "unutulmak, akıldan gitmek" de vardır.

Ayet yeniden okunduğunda {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyâke naʿbudu ve iyyâke nesteʿîn, gloss:yalnız sana kulluk ederiz ve yalnız senden yardım isteriz, source:1:5} cümlesi artık iki ayrı cümle gibi durmaz. Sahibi olunanların, sahiplerinin önüne çıkıp ilk kez "sen" dediği tek bir andır. "Seni" diye başlayan ses, önce kim olduğunu söyler: üzerinde çalışılmış, uysallaşmış ve bu uysallıkla sağlamlaşmış bir kul. Bu kul, yürüdükçe yolu düzleyen bir ayak, suya dayanıklı kılınmış bir tekne, hedefine gönderilen bir adaktır. Sonra aynı ses aynı muhataba yeniden döner ve yolda kalmış bir yolcunun, dağılabilecek bir sürünün, ikinci kavgasına girmiş bir savaşçının isteğini söyler: arkamızda dur, bize yetişen gücü ver, gözünün önünde tut. Neyin istendiği söylenmez. Cevap, bir sonraki ayette kendini dik tutan bir yol olarak gelecektir. "Yalnız sana kulluk ederiz ve yalnız senden yardım isteriz" demek, bu yolun üzerinde yürümeyi ve yürüyebilmek için O'na yaslanmayı aynı nefeste söylemektir.

