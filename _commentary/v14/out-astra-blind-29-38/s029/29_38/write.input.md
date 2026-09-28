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
# ayah.md — 29:38 (the focus ayah)

وَعَادًۭا وَثَمُودَا۟ وَقَد تَّبَيَّنَ لَكُم مِّن مَّسَٰكِنِهِمْ ۖ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ فَصَدَّهُمْ عَنِ ٱلسَّبِيلِ وَكَانُوا۟ مُسْتَبْصِرِينَ

Anchor translation (canonical reading, reference only):

Âd ve Semûd'u da yok ettik. Bu, yurtlarından size açıkça belli olmuştur. Şeytan onlara yaptıklarını güzel gösterdi ve anlayabilecek durumda oldukları halde onları yoldan alıkoydu.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَعَادًا | عَاد2 | ع و د | CONJ;PN |
| 2 | وَثَمُودَا۟ | ثَمُود |  | CONJ;PN |
| 3 | وَقَد | قَد |  | CONJ;CERT |
| 4 | تَّبَيَّنَ | تَبَيَّنَ | ب ي ن | V |
| 5 | لَكُم |  |  | P;PRON |
| 6 | مِّن | مِن |  | P |
| 7 | مَّسَٰكِنِهِمْ | مَسْكَن | س ك ن | N;PRON |
| 8 | وَزَيَّنَ | زَيَّنَ | ز ي ن | CONJ;V |
| 9 | لَهُمُ |  |  | P;PRON |
| 10 | ٱلشَّيْطَٰنُ | شَيْطَٰن | ش ط ن | DET;PN |
| 11 | أَعْمَٰلَهُمْ | عَمَل | ع م ل | N;PRON |
| 12 | فَصَدَّهُمْ | صَدَّ | ص د د | CONJ;V;PRON |
| 13 | عَنِ | عَن |  | P |
| 14 | ٱلسَّبِيلِ | سَبِيل | س ب ل | DET;N |
| 15 | وَكَانُوا۟ | كَانَ | ك و ن | CONJ;V;PRON |
| 16 | مُسْتَبْصِرِينَ | مُسْتَبْصِرِين | ب ص ر | N |

## Word notes (precomputed word analysis; support, not obligations)

- 29:38:1 وَ: opening conjunction that carries the named peoples into an already-running destruction frame — topics: opening connector carries prior governance
- 29:38:2 عَادًۭا: proper name for the people of ʿAd as an accusative carried object; tanwin keeps it fully declinable beside its paired name — topics: accusative tanwin marks carried object and full declension; paired proper name activates a known ruined-peoples field; return-root pressure creates cautious irony
- 29:38:3 وَ: coordinating conjunction that binds Thamud to ʿAd under the same recovered governance — topics: second conjunction locks the name-pair together
- 29:38:4 ثَمُودَ: proper name for Thamud as an accusative paired object; base diptote shape remains visible beside a leveling tanwin variant — topics: diptote base shape remains a live formal pressure point; proper name activates visible dwelling traditions; depletion image colors the ruin name cautiously
- 29:38:5 وَ: connector introducing the certified evidence parenthesis and the shift toward direct address — topics: connector opens the certified evidence parenthesis
- 29:38:6 قَدْ: certification particle before a perfect verb, marking the clarity as established rather than tentative — topics: certification particle fixes completed evidential clarity
- 29:38:7 تَبَيَّنَ: Form V perfect of becoming clear or distinct; the evidence has self-manifested to the audience from the ruins — topics: perfect verb and broad subject make evidence already clear; Form V makes clarity emerge from the evidence itself; clarity for the audience frames failed insight in the peoples
- 29:38:8 لَكُمْ: prepositional phrase routing the manifest evidence to the addressed audience as witnesses — topics: dative suffix turns audience into accountable witnesses
- 29:38:9 مِنْ: source preposition that makes the dwellings the origin, medium, or sample of the evidential clarity — topics: source preposition turns dwellings into evidence-channel; attachment ambiguity remains controlled by local syntax
- 29:38:10 مَسَاكِنِهِمْ: possessed plural dwelling-places governed by the source phrase; ruined habitation becomes visible evidence — topics: base source governance with variant agency pressure; dwelling-root becomes still ruin testimony; dwellings recur as the surviving witness after destruction
- 29:38:11 وَ: resumptive conjunction returning from the evidence parenthesis to the causal narrative — topics: resumptive conjunction returns to causal narration
- 29:38:12 زَيَّنَ: Form II active beautifying or adorning of deeds, with recipient and object separated and the agent named — topics: active verb separates agent, recipients, and object; Form II turns moral judgment into worked-over surface; beautification formula leads into path obstruction
- 29:38:13 لَهُمُ: prepositional recipient phrase for beautification, ironically marking the harmed group as those for whom the deeds were made attractive — topics: benefactive-looking lām marks harmful affectedness
- 29:38:14 هُمُ: bound plural pronoun carrying the named peoples forward as one affected group — topics: plural pronoun keeps one affected group across roles
- 29:38:15 ٱلشَّيْطَانُ: definite nominative adversarial agent who beautifies the deeds; remoteness pressure fits the later separation from the path — topics: definite nominative subject exposes the adversarial agent; remoteness root fits distance from the path; shaytan participates in recurring beautification and obstruction formula
- 29:38:16 أَعْمَالَهُمْ: their collected deeds or works as the object made attractive and the hinge toward diversion — topics: accusative plural construct gathers their practice-field; neutral action-root becomes dangerous under beautification; beautified deeds pivot into path obstruction
- 29:38:17 فَ: causal-sequential particle making the obstruction follow from the beautification — topics: fa turns beautification into immediate consequence
- 29:38:18 صَدَّهُمْ: completed transitive obstruction or turning-away of the named peoples from the path, without erasing the path itself — topics: attached object makes the peoples acted upon; blocking turns people away without destroying the way; causal sequence and way-collocation make diversion formulaic
- 29:38:19 عَنِ: separation preposition completing the obstruction frame by marking what they are turned away from — topics: preposition supplies the away-from target of obstruction
- 29:38:20 ٱلسَّبِيلِ: the definite singular way or proper course, governed after the separation preposition and targeted by obstruction — topics: definite singular path is the recognized course; genitive noun is locked under the away-from frame; path range carries course and flow pressure; path is the standard target of obstruction
- 29:38:21 وَ: final conjunction that adds the closing state and, in context, makes it concessive — topics: final conjunction joins and concessively sharpens the paradox
- 29:38:22 كَانُوا: past auxiliary/copular verb establishing the plural subjects in an already-held state of insight — topics: plural verb keeps the named doublet active; auxiliary plus participle marks a standing state; auxiliary-participle pattern carries into the next ayah
- 29:38:23 مُسْتَبْصِرِينَ: Form X masculine plural active participle of insight, seeking, possessing, or claiming clear perception in the ayah closing — topics: accusative participle names a shared perceptual state; Form X heightens insight while keeping multiple readings open; closing insight seals the clarity-versus-failure envelope; rare participle inversely recalls the shaytan encounter; fallen bodies contrast with insight-equipped minds


===== window_text.md =====
# window_text.md — 29:21–51

29:21|يُعَذِّبُ مَن يَشَآءُ وَيَرْحَمُ مَن يَشَآءُ ۖ وَإِلَيْهِ تُقْلَبُونَ
29:22|وَمَآ أَنتُم بِمُعْجِزِينَ فِى ٱلْأَرْضِ وَلَا فِى ٱلسَّمَآءِ ۖ وَمَا لَكُم مِّن دُونِ ٱللَّهِ مِن وَلِىٍّۢ وَلَا نَصِيرٍۢ
29:23|وَٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِ ٱللَّهِ وَلِقَآئِهِۦٓ أُو۟لَٰٓئِكَ يَئِسُوا۟ مِن رَّحْمَتِى وَأُو۟لَٰٓئِكَ لَهُمْ عَذَابٌ أَلِيمٌۭ
29:24|فَمَا كَانَ جَوَابَ قَوْمِهِۦٓ إِلَّآ أَن قَالُوا۟ ٱقْتُلُوهُ أَوْ حَرِّقُوهُ فَأَنجَىٰهُ ٱللَّهُ مِنَ ٱلنَّارِ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
29:25|وَقَالَ إِنَّمَا ٱتَّخَذْتُم مِّن دُونِ ٱللَّهِ أَوْثَٰنًۭا مَّوَدَّةَ بَيْنِكُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ ثُمَّ يَوْمَ ٱلْقِيَٰمَةِ يَكْفُرُ بَعْضُكُم بِبَعْضٍۢ وَيَلْعَنُ بَعْضُكُم بَعْضًۭا وَمَأْوَىٰكُمُ ٱلنَّارُ وَمَا لَكُم مِّن نَّٰصِرِينَ
29:26|۞ فَـَٔامَنَ لَهُۥ لُوطٌۭ ۘ وَقَالَ إِنِّى مُهَاجِرٌ إِلَىٰ رَبِّىٓ ۖ إِنَّهُۥ هُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
29:27|وَوَهَبْنَا لَهُۥٓ إِسْحَٰقَ وَيَعْقُوبَ وَجَعَلْنَا فِى ذُرِّيَّتِهِ ٱلنُّبُوَّةَ وَٱلْكِتَٰبَ وَءَاتَيْنَٰهُ أَجْرَهُۥ فِى ٱلدُّنْيَا ۖ وَإِنَّهُۥ فِى ٱلْءَاخِرَةِ لَمِنَ ٱلصَّٰلِحِينَ
29:28|وَلُوطًا إِذْ قَالَ لِقَوْمِهِۦٓ إِنَّكُمْ لَتَأْتُونَ ٱلْفَٰحِشَةَ مَا سَبَقَكُم بِهَا مِنْ أَحَدٍۢ مِّنَ ٱلْعَٰلَمِينَ
29:29|أَئِنَّكُمْ لَتَأْتُونَ ٱلرِّجَالَ وَتَقْطَعُونَ ٱلسَّبِيلَ وَتَأْتُونَ فِى نَادِيكُمُ ٱلْمُنكَرَ ۖ فَمَا كَانَ جَوَابَ قَوْمِهِۦٓ إِلَّآ أَن قَالُوا۟ ٱئْتِنَا بِعَذَابِ ٱللَّهِ إِن كُنتَ مِنَ ٱلصَّٰدِقِينَ
29:30|قَالَ رَبِّ ٱنصُرْنِى عَلَى ٱلْقَوْمِ ٱلْمُفْسِدِينَ
29:31|وَلَمَّا جَآءَتْ رُسُلُنَآ إِبْرَٰهِيمَ بِٱلْبُشْرَىٰ قَالُوٓا۟ إِنَّا مُهْلِكُوٓا۟ أَهْلِ هَٰذِهِ ٱلْقَرْيَةِ ۖ إِنَّ أَهْلَهَا كَانُوا۟ ظَٰلِمِينَ
29:32|قَالَ إِنَّ فِيهَا لُوطًۭا ۚ قَالُوا۟ نَحْنُ أَعْلَمُ بِمَن فِيهَا ۖ لَنُنَجِّيَنَّهُۥ وَأَهْلَهُۥٓ إِلَّا ٱمْرَأَتَهُۥ كَانَتْ مِنَ ٱلْغَٰبِرِينَ
29:33|وَلَمَّآ أَن جَآءَتْ رُسُلُنَا لُوطًۭا سِىٓءَ بِهِمْ وَضَاقَ بِهِمْ ذَرْعًۭا وَقَالُوا۟ لَا تَخَفْ وَلَا تَحْزَنْ ۖ إِنَّا مُنَجُّوكَ وَأَهْلَكَ إِلَّا ٱمْرَأَتَكَ كَانَتْ مِنَ ٱلْغَٰبِرِينَ
29:34|إِنَّا مُنزِلُونَ عَلَىٰٓ أَهْلِ هَٰذِهِ ٱلْقَرْيَةِ رِجْزًۭا مِّنَ ٱلسَّمَآءِ بِمَا كَانُوا۟ يَفْسُقُونَ
29:35|وَلَقَد تَّرَكْنَا مِنْهَآ ءَايَةًۢ بَيِّنَةًۭ لِّقَوْمٍۢ يَعْقِلُونَ
29:36|وَإِلَىٰ مَدْيَنَ أَخَاهُمْ شُعَيْبًۭا فَقَالَ يَٰقَوْمِ ٱعْبُدُوا۟ ٱللَّهَ وَٱرْجُوا۟ ٱلْيَوْمَ ٱلْءَاخِرَ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
29:37|فَكَذَّبُوهُ فَأَخَذَتْهُمُ ٱلرَّجْفَةُ فَأَصْبَحُوا۟ فِى دَارِهِمْ جَٰثِمِينَ
29:38|وَعَادًۭا وَثَمُودَا۟ وَقَد تَّبَيَّنَ لَكُم مِّن مَّسَٰكِنِهِمْ ۖ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ فَصَدَّهُمْ عَنِ ٱلسَّبِيلِ وَكَانُوا۟ مُسْتَبْصِرِينَ
29:39|وَقَٰرُونَ وَفِرْعَوْنَ وَهَٰمَٰنَ ۖ وَلَقَدْ جَآءَهُم مُّوسَىٰ بِٱلْبَيِّنَٰتِ فَٱسْتَكْبَرُوا۟ فِى ٱلْأَرْضِ وَمَا كَانُوا۟ سَٰبِقِينَ
29:40|فَكُلًّا أَخَذْنَا بِذَنۢبِهِۦ ۖ فَمِنْهُم مَّنْ أَرْسَلْنَا عَلَيْهِ حَاصِبًۭا وَمِنْهُم مَّنْ أَخَذَتْهُ ٱلصَّيْحَةُ وَمِنْهُم مَّنْ خَسَفْنَا بِهِ ٱلْأَرْضَ وَمِنْهُم مَّنْ أَغْرَقْنَا ۚ وَمَا كَانَ ٱللَّهُ لِيَظْلِمَهُمْ وَلَٰكِن كَانُوٓا۟ أَنفُسَهُمْ يَظْلِمُونَ
29:41|مَثَلُ ٱلَّذِينَ ٱتَّخَذُوا۟ مِن دُونِ ٱللَّهِ أَوْلِيَآءَ كَمَثَلِ ٱلْعَنكَبُوتِ ٱتَّخَذَتْ بَيْتًۭا ۖ وَإِنَّ أَوْهَنَ ٱلْبُيُوتِ لَبَيْتُ ٱلْعَنكَبُوتِ ۖ لَوْ كَانُوا۟ يَعْلَمُونَ
29:42|إِنَّ ٱللَّهَ يَعْلَمُ مَا يَدْعُونَ مِن دُونِهِۦ مِن شَىْءٍۢ ۚ وَهُوَ ٱلْعَزِيزُ ٱلْحَكِيمُ
29:43|وَتِلْكَ ٱلْأَمْثَٰلُ نَضْرِبُهَا لِلنَّاسِ ۖ وَمَا يَعْقِلُهَآ إِلَّا ٱلْعَٰلِمُونَ
29:44|خَلَقَ ٱللَّهُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ بِٱلْحَقِّ ۚ إِنَّ فِى ذَٰلِكَ لَءَايَةًۭ لِّلْمُؤْمِنِينَ
29:45|ٱتْلُ مَآ أُوحِىَ إِلَيْكَ مِنَ ٱلْكِتَٰبِ وَأَقِمِ ٱلصَّلَوٰةَ ۖ إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۗ وَلَذِكْرُ ٱللَّهِ أَكْبَرُ ۗ وَٱللَّهُ يَعْلَمُ مَا تَصْنَعُونَ
29:46|۞ وَلَا تُجَٰدِلُوٓا۟ أَهْلَ ٱلْكِتَٰبِ إِلَّا بِٱلَّتِى هِىَ أَحْسَنُ إِلَّا ٱلَّذِينَ ظَلَمُوا۟ مِنْهُمْ ۖ وَقُولُوٓا۟ ءَامَنَّا بِٱلَّذِىٓ أُنزِلَ إِلَيْنَا وَأُنزِلَ إِلَيْكُمْ وَإِلَٰهُنَا وَإِلَٰهُكُمْ وَٰحِدٌۭ وَنَحْنُ لَهُۥ مُسْلِمُونَ
29:47|وَكَذَٰلِكَ أَنزَلْنَآ إِلَيْكَ ٱلْكِتَٰبَ ۚ فَٱلَّذِينَ ءَاتَيْنَٰهُمُ ٱلْكِتَٰبَ يُؤْمِنُونَ بِهِۦ ۖ وَمِنْ هَٰٓؤُلَآءِ مَن يُؤْمِنُ بِهِۦ ۚ وَمَا يَجْحَدُ بِـَٔايَٰتِنَآ إِلَّا ٱلْكَٰفِرُونَ
29:48|وَمَا كُنتَ تَتْلُوا۟ مِن قَبْلِهِۦ مِن كِتَٰبٍۢ وَلَا تَخُطُّهُۥ بِيَمِينِكَ ۖ إِذًۭا لَّٱرْتَابَ ٱلْمُبْطِلُونَ
29:49|بَلْ هُوَ ءَايَٰتٌۢ بَيِّنَٰتٌۭ فِى صُدُورِ ٱلَّذِينَ أُوتُوا۟ ٱلْعِلْمَ ۚ وَمَا يَجْحَدُ بِـَٔايَٰتِنَآ إِلَّا ٱلظَّٰلِمُونَ
29:50|وَقَالُوا۟ لَوْلَآ أُنزِلَ عَلَيْهِ ءَايَٰتٌۭ مِّن رَّبِّهِۦ ۖ قُلْ إِنَّمَا ٱلْءَايَٰتُ عِندَ ٱللَّهِ وَإِنَّمَآ أَنَا۠ نَذِيرٌۭ مُّبِينٌ
29:51|أَوَلَمْ يَكْفِهِمْ أَنَّآ أَنزَلْنَا عَلَيْكَ ٱلْكِتَٰبَ يُتْلَىٰ عَلَيْهِمْ ۚ إِنَّ فِى ذَٰلِكَ لَرَحْمَةًۭ وَذِكْرَىٰ لِقَوْمٍۢ يُؤْمِنُونَ


===== synthesis.md =====
# synthesis.md — evidence for 29:38

This is an evidence index, not an outline or a list to put into prose. Image groups overlap. Combine them into connected explanations where their relationships earn space. No item or tag is ranked.

## Image connections (navigation only)

## Evidence (each source record appears once)

### F1 — concept
F1 | concept | words: 29:38:4 | branches: ب ي ن B001; ب ي ن B004 | trigger: 29:38:7 (ayah); 29:37:7 (window) | with: F2; F3; F84 | image: One root says both "to depart, be severed" and "to come into view". The dwellings are clear because their people have gone out of them, so the separation is itself the disclosure. | anchor: انفصال الشيء وافتراقه; ظهور الشيء وانكشافه

### F2 — local
F2 | local | words: 29:38:4; 29:38:7 | branches: ب ي ن B013; ب ي ن B001; س ك ن B002; غ ب ر B001; غ ب ر B004 | trigger: 29:38:7 (ayah); 29:32:16 (window); 29:33:23 (window) | with: F1; F37 | image: The classical ruin-scene sits inside تبيّن من مساكنهم: an abandoned camp whose people have parted, and the ill-omened raven of parting (غراب البين) over it. The window's غابرين (the remnant left behind, dust-coloured) completes the picture. | anchor: علامة الفراق المشؤومة; غراب البين يقال هو الأبقع

### F3 — cross-definition
F3 | cross-definition | words: 29:38:4; 29:38:16 | branches: ب ي ن B007; ب ص ر B001 | trigger: 29:38:16 (ayah) | with: F1; F45 | image: The dictionary measures a tract (بين) by the reach of البصر. The ruin-field laid out by تبيّن is as wide as the eye that looks across it, and the ayah's last word supplies that eye. | anchor: البين قطعة من الأرض قدر مد البصر; أبصرته إذا رأيته

### F4 — local
F4 | local | words: 29:38:10; 29:38:12; 29:38:4 | branches: ش ط ن B001; ب ي ن B006; ص د د B001 | trigger: 29:38:12 (ayah); 29:38:14 (ayah) | with: F5; F6 | image: The agent is "the far one", and his act opens a gap: he turns them so the distance between them and the road widens. Elsewhere the same blocking ends in "far error" (4:167 ضلالا بعيدا; 14:3 ضلال بعيد). | anchor: البعد والانقطاع; بعد المسافة واتساع الفجوة

### F5 — local
F5 | local | words: 29:38:10; 29:38:12; 29:38:14 | branches: ش ط ن B003; ص د د B001; س ب ل B001 | trigger: 29:38:12 (ayah); 29:38:14 (ayah) | with: F4; F6 | image: The agent's name defines his act: شطن is to turn a man aside from the direction his face intends, and فصدّهم عن السبيل tells the name as narrative. The same branch's crookedness (العوج) is what the Quran pairs with صدّ elsewhere (3:99, 7:45, 7:86, 11:19, 14:3 يبغونها عوجا). | anchor: شطنه يشطنه شطنا إذا خالفه عن نية وجهه; إعراض وصرف

### F6 — loaded
F6 | loaded | words: 29:38:12; 29:38:14 | branches: ص د د B001; س ب ل B001 | trigger: 29:38:8 (ayah); 29:38:10 (ayah) | with: F7; F8; F9; F66 | image: صدّ is a road-verb: 25 of 42 uses name سبيل as what one is turned from. The bare definite عن السبيل occurs 5 times (13:33, 27:24, 29:38, 40:37, 43:37); four stand beside زُيِّن/زيّن and the fifth beside devil-companions (43:36-37). Departures from the road pattern: sanctuary (5:2, 8:34, 48:25); ancestral worship (14:10, 27:43, 34:43); remembrance and prayer (5:91); the Hour (20:16); signs (28:87); guidance (34:32); intransitive turning away (4:55, 4:61, 63:5); the clamour reading (43:57); pus (14:16). This ayah sits in the tightest core (beautify → block → the road), and the anchor "yoldan alıkoydu" follows the pattern. | anchor: فَصَدَّهُمْ عَنِ ٱلسَّبِيلِ; إعراض وصرف

### F7 — loaded
F7 | loaded | words: 29:38:8; 29:38:10; 29:38:11 | branches: ز ي ن B002; ع م ل B001; ش ط ن B004 | trigger: 29:38:11 (ayah); 29:38:10 (ayah) | with: F6; F45; F50 | image: Of 26 uses of the verb زيّن, 13 take deeds as object (6:43, 6:108, 6:122, 8:48, 9:37, 10:12, 16:63, 27:4, 27:24, 29:38, 35:8, 40:37, 47:14). الشيطان is the named agent in 5 of them (6:43, 8:48, 16:63, 27:24, 29:38), plus Iblis's vow in 15:39. God is the agent in 5 sky uses (15:16, 37:6, 41:12, 50:6, 67:5) and in faith adorned in hearts (49:7). The adornment works through the eye (35:8 فرآه حسنا; 15:16 للناظرين). This ayah follows the deeds pattern; the anchor "güzel gösterdi" rightly keeps it as appearance, not real improvement. | anchor: وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ; إظهار الحسن وتحسين الشيء

### F8 — scene
F8 | scene | words: 29:38:8; 29:38:12; 29:38:16 | branches: ز ي ن B002; ص د د B001; ب ص ر B002 | trigger: 29:38:15 (ayah) | with: F7; F12 | image: The formula's twin in 27:24 (Sheba's people prostrating to the sun) matches word for word up to السبيل. It then closes on the outcome, "they are unguided"; 29:38 closes instead on the prior state, "they were clear-sighted". One text shows the blindness that results, the other the sight that was there before. | anchor: فَصَدَّهُمْ عَنِ ٱلسَّبِيلِ فَهُمْ لَا يَهْتَدُونَ

### F9 — window
F9 | window | words: 29:38:8; 29:38:11; 29:38:12; 29:38:14 | branches: ز ي ن B002; ع م ل B001; ص د د B001; س ب ل B001 | trigger: 29:39:2 (window) | with: F6; F52 | image: The next ayah names Pharaoh, of whom the Quran says the same thing in the passive (40:37). The mechanism of 29:38 runs forward into 29:39's group, where clear proofs meet arrogance. | anchor: وَكَذَٰلِكَ زُيِّنَ لِفِرْعَوْنَ سُوٓءُ عَمَلِهِۦ وَصُدَّ عَنِ ٱلسَّبِيلِ

### F10 — surah
F10 | surah | words: 29:38:10; 29:38:8 | branches: ش ط ن B004; و ل ي B004; و ه ن B001 | trigger: 29:41:7 (window); 29:41:13 (window); 29:22:15 (window) | with: F40; F56 | image: Where the formula recurs, the Quran names what the adorner becomes: their patron (16:63 فهو وليهم اليوم), or a boaster who promises "none overcomes you today" and then backs away (8:48). He is the ولي absent in 29:22 and the patron-house of 29:41, the weakest of houses. | anchor: فَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ فَهُوَ وَلِيُّهُمُ ٱلْيَوْمَ; محبة ونصرة وموالاة

### F11 — loaded
F11 | loaded | words: 29:38:4; 29:38:12 | branches: ب ي ن B004; ص د د B001 | trigger: 29:38:12 (ayah) | with: F6; F45 | image: Clarity and blocking stand together elsewhere too: in 47:32 people block the way "after guidance had become clear to them". In 47:25, again "after guidance had become clear", the shaytan embellishes (سوّل) for them. Here the clarity is for "you" and the embellishment for "them", in the same Quranic order. | anchor: وَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ وَشَآقُّوا۟ ٱلرَّسُولَ مِنۢ بَعْدِ مَا تَبَيَّنَ لَهُمُ | memory: yes

### F12 — grammar
F12 | grammar | words: 29:38:16; 29:38:15 | branches: ب ص ر B002; ب ص ر B001 | trigger: | with: F8; F13; F22 | image: مستبصرين is a hapax Form X participle. It can mean seeking sight, having clear sight, or counting oneself clear-sighted (compare 43:37: they block them from the road "and reckon that they are guided"). The anchor's "anlayabilecek durumda" turns it into a modal capacity and drops both the actual-insight and the self-assessment readings. | anchor: وَكَانُوا۟ مُسْتَبْصِرِينَ; وَيَحْسَبُونَ أَنَّهُم مُّهْتَدُونَ

### F13 — grammar
F13 | grammar | words: 29:38:15; 29:38:16 | branches: ك و ن B001; ب ص ر B002; س ب ق B004 | trigger: | with: F12; F71 | image: Consecutive ayat both close on كانوا + participle: "they were clear-sighted" (29:38) and "they could not outrun" (29:39). Sight was granted, escape denied. The pair's two Form X verbs, استبصر and استكبر (29:39:8), set seeing and self-magnifying side by side. | anchor: وَمَا كَانُوا۟ سَٰبِقِينَ; الفوت عن الطالب

### F14 — grammar
F14 | grammar | words: 29:38:1; 29:38:2 | branches: ع و د B012 | trigger: | with: F79 | image: عادًا وثمودَ are accusative with no verb in their own ayah. They hang on the seizing of 29:37 (فأخذتهم) or an understood "we destroyed / remember", and 29:40 (فكلًّا أخذنا) gathers them. The anchor supplies "yok ettik", so a Turkish reader cannot hear the two peoples left grammatically waiting for the seizure verb. | anchor: فَأَخَذَتْهُمُ ٱلرَّجْفَةُ; فَكُلًّا أَخَذْنَا بِذَنۢبِهِۦ

### F15 — grammar
F15 | grammar | words: 29:38:3; 29:38:4; 29:38:5 | branches: ب ي ن B004 | trigger: | with: F27; F81 | image: قد with a perfect certifies that the clarity is complete. Form V تبيّن is self-disclosure: the thing becomes clear of itself. لكم breaks the third-person history to address the listeners as witnesses who pass the sites. | anchor: وَقَد تَّبَيَّنَ لَكُم مِّن مَّسَٰكِنِهِمْ

### F16 — grammar
F16 | grammar | words: 29:38:9; 29:38:11; 29:38:12; 29:38:14 | branches: ع م ل B001; ص د د B001; س ب ل B001 | trigger: | with: F24 | image: The agent is external, but everything else is theirs: لهم (for them), أعمالهم (their works), the هم of صدّهم. The فـ makes the blocking follow at once from the beautification. السبيل is definite and bare, not سبيل الله: "the road", the known way. | anchor: وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ فَصَدَّهُمْ

### F17 — loss
F17 | loss | words: 29:38:10 | branches: ش ط ن B001; ش ط ن B002; ش ط ن B003 | trigger: | with: F4; F5 | image: Turkish "şeytan" is a bare name for the devil. It loses the root's distance, its long well-rope, and "turning a man from his intended direction", which is the very act the ayah narrates. | anchor: البعد والانقطاع; المخالفة والعوج والشدة

### F18 — loss
F18 | loss | words: 29:38:11 | branches: ع م ل B001; ع م ل B006; ع م ل B011 | trigger: | with: F24; F54 | image: The anchor's "yaptıklarını" and the loanword "amel" (narrowed to devotional deeds) lose the physical side of أعمال: labour of hands (digging, lining wells), built works, and the worn road. | anchor: الطريق المعمل; العملة العاملون بالأيدي

### F19 — loss
F19 | loss | words: 29:38:14 | branches: س ب ل B001; س ب ل B003; س ب ل B005 | trigger: | with: F62 | image: Turkish "yol" is flat. The Turkish loanword "sebil" means a charitable water fountain (from the endowment sense), so a Turkish ear can hear water in the word the anchor renders "yol". The Arabic word also holds falling rain and the traveller. | anchor: سبلت مالا في سبيل الله أي وقفته; مطر سابل بين السحاب والأرض

### F20 — loss
F20 | loss | words: 29:38:7 | branches: س ك ن B001; س ك ن B006; ج ث م B005 | trigger: 29:37:7 (window) | with: F33 | image: Turkish "mesken" keeps only residence. Turkish "miskin" (from مسكين) means sluggish, lying idle, which is the ج ث م picture of 29:37: the one who never leaves his house. Arabic binds dwelling, stillness and destitution in one root; Turkish splits them. | anchor: ذهاب الحركة; الجثامة للنؤوم أو اللبد

### F21 — loss
F21 | loss | words: 29:38:1 | branches: ع و د B004; ع و د B012; ع و د B001 | trigger: | with: F26; F28 | image: "Âd" in Turkish is a bare name. The Turkish reader who knows âdet (custom), iade (return) and maad (the return, the hereafter) is not told that the name shares a root with return and habit. | anchor: عاد وأعلام منسوبة إليها; عادة ودرَبة ومواظبة

### F22 — loss
F22 | loss | words: 29:38:16 | branches: ب ص ر B002; ب ص ر B001; ب ص ر B006 | trigger: | with: F12 | image: Turkish "basiret" (foresight, prudence) keeps inward sight. It loses the eye, the house-seam, and the Form X sense of seeking or claiming sight; "anlayabilecek" flattens it further into a mere ability. | anchor: بصيرة القلب; إبصار العين

### F23 — loss
F23 | loss | words: 29:38:8 | branches: ز ي ن B002; ز ي ن B003 | trigger: | with: F7; F52 | image: "güzel gösterdi" keeps the appearance but loses ziynet: adornment worn, possessions and status. That sense ties this verb to the dwellings and to Qārūn's adornment in the next ayah. | anchor: الزينة التي يتزين بها

### F24 — local
F24 | local | words: 29:38:14; 29:38:11; 29:38:12; 29:38:1 | branches: س ب ل B001; س ب ل B002; ع م ل B011; ع م ل B012; ع م ل B008; ع و د B009; ع و د B008; ص د د B002; ص د د B004; ص د د B005 | trigger: 29:38:14 (ayah); 29:38:11 (ayah); 29:38:12 (ayah) | with: F25; F62; F66 | image: A caravan scene: walkers on a worn old road run between valley walls toward water, with aged and hardy camels. A barrier-mountain (الصدّ) turns them off, and they become stranded travellers. "Their works" is also their own well-trodden road, beautified until it replaces the road. | anchor: طريق معمل أي لحب مسلوك; العود الطريق القديم; الصَّداد الطريق إلى الماء; جبل حاجز

### F25 — local
F25 | local | words: 29:38:1; 29:38:7 | branches: ع و د B012; ع و د B009; س ك ن B002 | trigger: 29:38:7 (ayah); 29:38:14 (ayah) | with: F24; F69 | image: The people's name gives Arabic its word for anything immemorially old: the ʿādī ruin, the ʿādī road. Their dwellings are ancient ruins by name, and the old road (العود) lies beside the path they were turned from. | anchor: عاد وأعلام منسوبة إليها; قدم وطريق عود

### F26 — local
F26 | local | words: 29:38:1; 29:38:11; 29:38:8 | branches: ع و د B004; ع م ل B001; ز ي ن B002 | trigger: 29:38:11 (ayah); 29:38:8 (ayah) | with: F21 | image: Beautified deeds are repeated until they become habit and second nature. Other صدّ scenes name this inherited custom: "from what our/your fathers worshipped" (14:10, 34:43). | anchor: العادة الدربة والتمادي في شيء حتى يصير له سجية; عادة ودرَبة ومواظبة

### F27 — window
F27 | window | words: 29:38:1; 29:38:5; 29:38:7 | branches: ع و د B005; س ك ن B002; ب ي ن B004 | trigger: 29:38:5 (ayah); 29:35:2 (window); 29:20:2 (surah) | with: F15; F81 | image: People come and go to a stricken house as condolence visitors. The listeners (لكم) who travel the land (29:20) and pass the sign-town (29:35) make a return-visit to a house of mourning. | anchor: عيادة ومعادة وزيارة راجعة

### F28 — chain
F28 | chain | words: 29:38:1 | branches: ع و د B001; ع و د B002 | trigger: 29:19:8 (surah); 29:21:8 (surah); 29:57:6 (surah) | with: F84; F70 | image: In the surah's origin-and-return chain (29:19 يعيده, 29:21 تقلبون, 29:57 ترجعون), the people named from the root of return play the reversal role. Bearing the name of return, they cannot return to their dwellings (compare 36:67 ولا يرجعون); their only return is the final مَعاد. | anchor: رجوع بعد انصراف وتثنية بعد بدء; مصير ومرجع ومعاد

### F29 — local
F29 | local | words: 29:38:1; 29:38:4 | branches: ع و د B003; ب ي ن B005 | trigger: 29:38:4 (ayah); 29:37:7 (window) | with: F1 | image: A people who "neither begin nor return a word" have fallen silent, yet their sites speak clearly: silent people, eloquent dwellings. | anchor: سكوت لا يبدئ ولا يعيد; كشف المعنى بالقول أو العلامة

### F30 — fragment
F30 | fragment | words: 29:38:1; 29:38:11 | branches: ع و د B008; ع م ل B008 | trigger: 29:38:11 (ayah) | with: F24 | image: The aged camel with strength left, and the camel built for work. Ad's proverbial strength (41:15 "who is stronger than us") is a residual power that does not save. | anchor: عود مسن فيه بقايا قوة; المطبوع على العمل | memory: yes

### F31 — fragment
F31 | fragment | words: 29:38:1 | branches: ع و د B010; ء ر ض B010 | trigger: 29:39:10 (window); 29:40:17 (window); 29:41:15 (window) | with: F36 | image: Timber (عود) beside the wood-eating termite, next to the spider's house: structural wood eaten from within. | anchor: عود من خشب وطيب وآلة; الأَرَضَة آكلة الخشب

### F32 — fragment
F32 | fragment | words: 29:38:1; 29:38:8 | branches: ع و د B007; ز ي ن B003 | trigger: 29:38:8 (ayah) | with: F52 | image: The recurring festival (عيد) beside the Quran's "day of adornment" (Pharaoh's feast, 20:59): a periodic public show of adornment. | anchor: عيد وحال يعاود; قَالَ مَوْعِدُكُمْ يَوْمُ ٱلزِّينَةِ

### F33 — window
F33 | window | words: 29:38:7 | branches: س ك ن B001; ر ج ف B001; ر ج ز B001; ج ث م B001 | trigger: 29:37:3 (window); 29:34:7 (window); 29:37:7 (window) | with: F20; F68 | image: A dwelling is named from stilled motion, and the punishment is violent shaking (الرجفة, رجز). Shaking enters the place of stillness and leaves bodies stuck to the ground; the stillness of settlement becomes the stillness of the dead. | anchor: خلاف الاضطراب والحركة; اضطراب شديد

### F34 — cross-definition
F34 | cross-definition | words: 29:38:7 | branches: س ك ن B002; س ك ن B003; د و ر B002; ء ه ل B001 | trigger: 29:37:6; 29:64:9; 29:33:18 | with: F35; F37 | image: The dictionary defines residing through the دار and the household through ahl and dār. So 29:37's دارهم, 29:64's الدار and the أهل of the Lot scenes define the dwellings of 29:38. | anchor: يسكنون الدار; السكن الأهل الذين يسكنون الدار

### F35 — chain
F35 | chain | words: 29:38:7 | branches: س ك ن B002; ب ي ت B001 | trigger: 29:37:6 (window); 29:41:11 (window); 29:58:5 (surah); 29:64:9 (surah) | with: F34; F36; F55 | image: The surah's dwelling chain has five stages: the house holding fallen bodies (29:37); the exposed, emptied dwellings (29:38); the weakest house (29:41); the lofty rooms God settles believers in (29:58); and the Final Abode that "is life itself" (29:64). 29:38 is the emptied-dwelling stage, the counter-image of the abode that lives. | anchor: وَإِنَّ ٱلدَّارَ ٱلْءَاخِرَةَ لَهِىَ ٱلْحَيَوَانُ; استيطان المنزل

### F36 — scene
F36 | scene | words: 29:38:7; 29:38:16 | branches: س ك ن B002; ب ص ر B006; ب ي ت B001; و ه ن B001 | trigger: 29:41:15 (window); 29:41:13 (window) | with: F74; F75; F54 | image: Partner scene for channel 10A. Ad's towers and Thamud's rock-cut houses (7:74, 26:128-129, 15:82) are the strongest of houses, yet stand empty; the spider's house is the weakest, yet still inhabited. Both are failed shelters: one by a hardness that outlives its people, one by frailty. | anchor: بصر الشيء غلظه والبصر هو أن يضم أديم إلى أديم يخاطان والبصيرة ما بين شقتي البيت; وَإِنَّ أَوْهَنَ ٱلْبُيُوتِ لَبَيْتُ ٱلْعَنكَبُوتِ | memory: yes

### F37 — scene
F37 | scene | words: 29:38:7 | branches: س ك ن B003; ء ه ل B001; غ ب ر B001 | trigger: 29:32:10 (window); 29:33:17 (window); 29:32:16 (window) | with: F34; F2 | image: Partner scene for channel 10B. In Lot's town the household is sorted: extracted, except the wife who stays with the remnant. Here no one is extracted, and the dwellings remain without residents (compare 28:58, dwellings "not lived in after them except a little"). | anchor: أهل الدار; بقاء البقية بعد مضي ما معها | memory: yes

### F38 — loaded
F38 | loaded | words: 29:38:7 | branches: س ك ن B002; ب ي ن B004 | trigger: 29:38:4 (ayah) | with: F79 | image: The Quran's مساكن of destroyed peoples recur as seen and walked-through remains. Of Ad itself: "nothing was seen but their dwellings" (46:25). Also 28:58; 32:26 and 20:128 ("they walk in their dwellings"); 14:45 ("you dwelt in the dwellings of those who wronged"). This ayah's "clear from their dwellings" follows that scene. | anchor: استيطان المنزل; موضع الاستقرار | memory: yes

### F39 — window
F39 | window | words: 29:38:7; 29:38:12; 29:38:14 | branches: س ك ن B008; ص د د B001; س ب ل B001 | trigger: 29:38:12 (ayah); 29:15:3 (surah); 29:65:4 (surah) | with: F24 | image: The ship's stern-rudder is named from the same root, because it steadies and steers. They had the steadying instrument of settled life, yet another hand steered them off course; the surah's ships (29:15, 29:65) carry this image. | anchor: سكان السفينة سمى لأنه يسكنها عن الاضطراب; إعراض وصرف

### F40 — window
F40 | window | words: 29:38:7; 29:38:8 | branches: س ك ن B004; ز ي ن B003; و ل ي B004 | trigger: 29:41:7 (window); 29:25:8 (window) | with: F10; F85 | image: A سكن is whatever one rests in and is comforted by. The beautified works, the affection of 29:25 and the patrons of 29:41 were what they rested in: a comforting refuge that is the spider's house. | anchor: كل ما سكنت إليه من محبوب; محبة ونصرة وموالاة

### F41 — window
F41 | window | words: 29:38:7; 29:38:8 | branches: س ك ن B006; ز ي ن B003 | trigger: 29:39:1 (window) | with: F52 | image: The dwelling root also holds destitution (المسكنة). Adorned residences are reduced to the maskana of emptiness, as Qārūn's adornment (29:39) sinks with his house. | anchor: ذل المسكنة; الزينة التي يتزين بها

### F42 — window
F42 | window | words: 29:38:7; 29:38:14 | branches: س ك ن B007; ج ث م B002; س ب ل B007 | trigger: 29:37:7 (window) | with: F33 | image: A slaughter scene: the knife named for stilling the victim, the tethered target-animal (مجثمة), and the throat-point of the beast. The people end pinned and still. | anchor: إسكان الذبيحة بالسكين; المجثمة المصبورة; حافة أو مخرج متقدم

### F43 — fragment
F43 | fragment | words: 29:38:7 | branches: س ك ن B010 | trigger: 29:17:18 (surah) | with: F62 | image: The provision that lets one stay in place, and the pasture that spares the herd migration. 29:17's رزق is the true condition of settlement. | anchor: قوت يثبت المقام

### F44 — fragment
F44 | fragment | words: 29:38:7 | branches: س ك ن B005 | trigger: 29:33:13 (window); 29:33:15 (window) | with: F37 | image: Calm replaces fear when Lot is told "fear not, grieve not" (29:33), just as the settled town is marked for ruin. The sakīna goes to the one extracted, not to those who stay. | anchor: طمأنينة الوقار

### F45 — local
F45 | local | words: 29:38:4; 29:38:8; 29:38:16 | branches: ب ي ن B004; ز ي ن B002; ب ص ر B001; ب ص ر B002 | trigger: 29:38:16 (ayah) | with: F3; F7; F11 | image: Two showings compete for one pair of eyes. The dwellings disclose what is true (تبيّن), while the shaytan displays beauty on their works (إظهار الحسن). The seeing eye (مستبصرين) receives both, and the display wins. | anchor: ظهور الشيء وانكشافه; إظهار الحسن وتحسين الشيء

### F46 — local
F46 | local | words: 29:38:12; 29:38:8; 29:38:16 | branches: ص د د B013; ز ي ن B003; ب ص ر B001 | trigger: 29:38:8 (ayah); 29:38:16 (ayah) | with: F45 | image: Kohl is rubbed on a mirror and painted on the eye, and the blocking root names this eye-paint. Adornment is applied to the organ of sight itself: the eye is made up, still open, still "seeing". | anchor: الصُّدود ما دلكته على مرآة ثم كحلت به عينا; الزينة التي يتزين بها

### F47 — local
F47 | local | words: 29:38:8; 29:38:10 | branches: ز ي ن B001; ش ط ن B005 | trigger: 29:38:10 (ayah) | with: F7 | image: Beauty is defined as the opposite of blemish, yet the adorner bears the name of the ugliest serpent, the fearful heads of 37:65. The ugly one sells beauty. | anchor: الزين نقيض الشين; القبيح المسمى شيطانا | memory: yes

### F48 — cross-definition
F48 | cross-definition | words: 29:38:8 | branches: ز ي ن B003; ص ن ع B004 | trigger: 29:45:21 | with: F54 | image: The dictionary names زينة inside ص ن ع: putting on a demeanour and adornment. The "what you make" of 29:45, which God knows, includes the cosmetic self-display that 29:38 assigns to the shaytan's work. | anchor: تصنع السمت والزينة; الزينة التي يتزين بها

### F49 — surah
F49 | surah | words: 29:38:8 | branches: ز ي ن B003; ح ي ي B001 | trigger: 29:25:11 (window); 29:64:6 (surah); 29:64:7 (surah) | with: F7 | image: The noun زينة ties to الحياة الدنيا in 8 of its 19 uses (10:88, 11:15, 18:28, 18:46, 28:60, 28:79, 33:28, 57:20). The triad "play, diversion and adornment" of 57:20 completes 29:64's "diversion and play". The beautified works belong to the worldly life of 29:25 and 29:64. | anchor: ٱعْلَمُوٓا۟ أَنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌ وَلَهْوٌ وَزِينَةٌ

### F50 — scene
F50 | scene | words: 29:38:8; 29:38:10 | branches: ز ي ن B002; س م و B004; ح ص ب B002 | trigger: 29:44:3 (window); 29:34:9 (window); 29:40:8 (window) | with: F7 | image: God adorns the sky, and its lamps are also missiles against the shayāṭīn. The shaytan adorns deeds below, while God's adorned sky pelts. The window's punishment from the sky (29:34) and its pelting (29:40) belong to this reverse adornment. | anchor: وَلَقَدْ زَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِمَصَٰبِيحَ وَجَعَلْنَٰهَا رُجُومًا لِّلشَّيَٰطِينِ

### F51 — scene
F51 | scene | words: 29:38:8; 29:38:7 | branches: ز ي ن B002; ص ب ح B010 | trigger: 29:37:4 (window) | with: F38 | image: The partner scene is 10:24. The land takes its finery and adorns itself, its people think they master it, then the command comes by night or day and it is as if it never flourished. An adorned settlement is erased overnight, like the morning of 29:37. | anchor: حَتَّىٰٓ إِذَآ أَخَذَتِ ٱلْأَرْضُ زُخْرُفَهَا وَٱزَّيَّنَتْ

### F52 — window
F52 | window | words: 29:38:8 | branches: ز ي ن B003 | trigger: 29:39:1 (window); 29:40:15 (window) | with: F41; F32; F9 | image: Qārūn, named next, is the Quran's figure who went out "in his adornment" (28:79). The adornment of 29:38 steps into 29:39-40 as a person, and it is swallowed by the earth. | anchor: فَخَرَجَ عَلَىٰ قَوْمِهِۦ فِى زِينَتِهِۦ

### F53 — fragment
F53 | fragment | words: 29:38:8 | branches: ز ي ن B002 | trigger: 29:36:15 (window); 29:39:10 (window) | with: F7 | image: Iblis vows "I will adorn for them in the earth" (15:39). Set against the window's corruption and arrogance "in the earth", the earth becomes the display-case of adornment. | anchor: لَأُزَيِّنَنَّ لَهُمْ فِى ٱلْأَرْضِ

### F54 — window
F54 | window | words: 29:38:11; 29:38:7 | branches: ع م ل B006; ص ن ع B006; ب ص ر B007; س ك ن B002 | trigger: 29:45:21 (window); 29:38:7 (ayah) | with: F36; F48; F76 | image: Read as construction, their "works" are hand-labour: digging and lining, the cisterns and great buildings (مصانع, said of Ad in 26:129), houses cut in soft stone (Thamud, 7:74). The adorned works are the very dwellings that now testify. | anchor: العملة القوم يعملون بأيديهم ضروبا من العمل حفرا أو طيا أو نحوه; المصانع أحواض وأبنية | memory: yes

### F55 — surah
F55 | surah | words: 29:38:11 | branches: ع م ل B004; ء ج ر B001 | trigger: 29:27:11 (window); 29:58:16 (surah); 29:58:17 (surah) | with: F35 | image: Work earns a wage. Abraham receives his أجر in this world (29:27), and "excellent is the wage of the workers" (29:58) is paid in rooms. The beautified works of 29:38 are labour ending in unpaid ruin. | anchor: أجر العمل ورزق العامل; جزاء العمل والكراء

### F56 — fragment
F56 | fragment | words: 29:38:11; 29:38:15; 29:38:10 | branches: ع م ل B003; ك و ن B003; و ل ي B003 | trigger: 29:41:7 (window) | with: F10 | image: The shaytan is the appointed overseer of their work and a self-declared guarantor (8:48, "I am your protector"). He is the patron-manager of 29:41, who does not stand surety. | anchor: ولاية العمل والقيام عليه; الكفالة والقيام على فلان | memory: yes

### F57 — cross-definition
F57 | cross-definition | words: 29:38:11 | branches: ع م ل B012; ع م ل B010; ر ج ل B003 | trigger: 29:29:3; 29:55:8 | with: F24 | image: "Sons of work" are defined as travellers on their legs (أرجلهم), and a beast's "workers" as its legs, so work is walking. 29:55 closes with punishment "from beneath their feet" and "what you used to work". | anchor: المسافرون إذا مشوا على أرجلهم يسمون بني العمل; عوامل الدابة قوائمه واحدها عاملة

### F58 — fragment
F58 | fragment | words: 29:38:11 | branches: ع م ل B009; ق ر ي B012 | trigger: 29:34:6 (window) | image: The spear's forepart below its head sits beside the town-word's spear-point sense: a weapon image that forms no scene yet. | anchor: عامل الرمح; طرف حاد كقارية السنان

### F59 — fragment
F59 | fragment | words: 29:38:11 | branches: ع م ل B005 | trigger: 29:36:2 (window) | image: Mutual dealing and trade sit beside Midian (29:36), whose sin elsewhere is fraud in measure (11:85). | anchor: المعاملة بين الناس | memory: yes

### F60 — concept
F60 | concept | words: 29:38:12; 29:38:16 | branches: ص د د B001; ص د د B003 | trigger: 29:38:16 (ayah); 29:48:5 (window) | with: F45 | image: One root says both "facing, close at hand" and "turned away". The road lay before their seeing eyes, and they were turned from what faced them. The gloss of "facing" (الصدد ما استقبل) is built on the root of 29:48 قبله. | anchor: الصدد ما استقبل; إعراض وصرف

### F61 — window
F61 | window | words: 29:38:12 | branches: ص د د B006; ص د د B011 | trigger: 29:29:8 (window); 29:40:12 (window) | with: F66 | image: The blocking root also names clamour (43:57 يَصِدّون) and hand-clapping (8:35). These echo the loud assembly of 29:29 and the fatal Cry of 29:40. | anchor: ضجيج وجلبة; تصفيق | memory: yes

### F62 — window
F62 | window | words: 29:38:12; 29:38:14; 29:38:10; 29:38:2 | branches: ص د د B004; ص د د B010; س ب ل B005; س ب ل B007; ش ط ن B002; ذ ن ب B007; خ س ف B004; ق ل ب B007; ع ذ ب B001 | trigger: 29:40:3 (window); 29:40:15 (window); 29:21:8 (window); 29:21:1 (window) | with: F24; F19; F82 | image: A well scene is assembled here: a road to water and a named sweet well, the long rope (شطن), the bucket rim, the full bucket (ذنوب, heard in 29:40 بذنبه), an unlined well, a shaft reaching deep water, sweet water and rain. The people are turned off the road that leads to water. Thamud's name (ثمد, scant leftover water) and their camel's water-share (26:155) supply the drought side. | anchor: الصَّداد الطريق إلى الماء; الشطن الحبل وهو القياس لأنه بعيد ما بين الطرفين; الذنوب دلو ممتلئ | memory: yes

### F63 — fragment
F63 | fragment | words: 29:38:12 | branches: ص د د B007 | trigger: 29:25:23 (window) | image: Pus mixed with blood is the drink of hell (14:16). It sits beside "your refuge is the Fire" (29:25). | anchor: صديد الجرح; وَيُسْقَىٰ مِن مَّآءٍ صَدِيدٍ

### F64 — fragment
F64 | fragment | words: 29:38:12; 29:38:16 | branches: ص د د B012; ب ص ر B005; ك ف ر B001 | trigger: 29:23:2 (window) | with: F78 | image: A drawn screen, a worn shield, a covering: blocking read as veiling, protection read as armour, one surface for both. | anchor: ستر المرأة; بصيرة السلاح; ستر وتغطية

### F65 — fragment
F65 | fragment | words: 29:38:12 | branches: ص د د B008; ع ن ك ب B001; ء ر ض B010 | trigger: 29:41:9 (window); 29:40:17 (window) | with: F75 | image: The blocking root's small creature (دويبة) sits beside the weaving creature of 29:41 and the wood-eating termite: small beasts that ensnare or undermine. | anchor: دويبة صغيرة; العنكبوت الدويبة الناسجة

### F66 — scene
F66 | scene | words: 29:38:12; 29:38:14 | branches: ص د د B001; س ب ل B001; س ب ل B002; ق ط ع B023 | trigger: 29:29:4 (window); 29:29:5 (window) | with: F24; F6; F61 | image: This is the partner scene of channel 9A. Lot's people cut the road on travellers (29:29); here Ad and Thamud are the travellers whose road is cut, by an inner highwayman. The dictionary defines road-cutting by الصدّ, so 29:29's act and 29:38's verb are one operation with the roles reversed. | anchor: قطع الطريق بالغصب والصد; أهل الطريق وسالكوه

### F67 — fragment
F67 | fragment | words: 29:38:14 | branches: س ب ل B004; ن ز ل B002; س م و B004 | trigger: 29:34:2 (window); 29:34:9 (window) | image: The road-word's letting-down from above (curtain, rain, tears) answers "we send down on this town a punishment from the sky". | anchor: إرخاء من علو إلى سفل; إنزال الشيء وإيصاله

### F68 — cross-definition
F68 | cross-definition | words: 29:38:15 | branches: ك و ن B006; ب ي ت B004; ص ب ح B010 | trigger: 29:41:11; 29:37:4 | with: F33 | image: The dictionary's example for كينة is "he spent the night (بات) in a bad state". The night is passed in the house (29:41), then "by morning they became" fallen (29:37). كانوا reads as the bad night before the morning of ruin. | anchor: الكينة في قولهم بات فلان بكينة سوء أي بحال سوء; أصبح بمعنى صار

### F69 — fragment
F69 | fragment | words: 29:38:15; 29:38:1 | branches: ك و ن B005; ع و د B012 | trigger: 29:38:1 (ayah) | with: F25 | image: The old man who tells of his youth ("I was…"): the ancient people survive only as a كانوا, a past state reported by others. | anchor: الشيخ المنسوب إلى كُنْتُ; عاد وأعلام منسوبة إليها

### F70 — loaded
F70 | loaded | words: 29:38:15; 29:38:7; 29:38:11 | branches: ك و ن B002; س ك ن B009; ع م ل B001 | trigger: 29:38:7 (ayah); 29:38:14 (ayah); 29:36:2 (window) | with: F28 | image: The root's other lemmas مكان/مكانة are paired in the Quran with work and with the road. "Work according to your position" appears in 4 of 5 مكانة uses (6:135, 11:93 Shuʿayb to Midian, 11:121, 39:39). "Worse in place and further astray from the road" appears in 5:60 and 25:34. In 36:67 they are transfixed in their places, able neither to go on nor to return. Place, work and road form one field around كانوا and مساكن. | anchor: المكان والمكانة من الكون; قُلْ يَٰقَوْمِ ٱعْمَلُوا۟ عَلَىٰ مَكَانَتِكُمْ

### F71 — window
F71 | window | words: 29:38:15; 29:38:16 | branches: ك و ن B004; ك ب ر B006 | trigger: 29:39:8 (window) | with: F13; F86 | image: The root of كانوا yields استكانة, humble submission, which the arrogance of 29:39 refuses. 6:43 frames the adornment formula the same way: when calamity came they did not humble themselves, and the shaytan adorned their deeds. The self-seeing of 29:38 sits between submission and self-magnification. | anchor: الخضوع بالاستكانة; العظمة والكبرياء

### F72 — surah
F72 | surah | words: 29:38:16; 29:38:2 | branches: ب ص ر B003; ء ي ي B003 | trigger: 29:35:4 (window); 29:39:7 (window); 29:50:5 (window) | with: F73 | image: The seeing-root names a sign that makes people see, and Thamud were given exactly that: "the she-camel, sight-giving" (17:59). The clear-sighted Thamud had held an illuminating sign, and they join the chain of 29:35, 29:39 and 29:50. | anchor: المبصرة المضيئة تبصرهم أي تجعلهم بصراء والمبصرة بالفتح الحجة; علامة ظاهرة | memory: yes

### F73 — cross-definition
F73 | cross-definition | words: 29:38:16 | branches: ب ص ر B003; ء ي ي B003 | trigger: 29:35:4; 29:44:9 | with: F72 | image: The dictionary defines the root's clarifying sense through آية (آية مبصرة). The surah's signs are, by definition, things that give sight. | anchor: آية مبصرة; علامة ظاهرة

### F74 — cross-definition
F74 | cross-definition | words: 29:38:16 | branches: ب ص ر B006; ب ي ت B001 | trigger: 29:41:11; 29:41:15 | with: F36; F75 | image: بصيرة is defined as the join between the two panels of a house (tent). The insight-word names a seam of the بيت that 29:41 calls the weakest when a spider spins it. | anchor: بصر الشيء غلظه والبصر هو أن يضم أديم إلى أديم يخاطان والبصيرة ما بين شقتي البيت; المأوى والمسكن

### F75 — cross-definition
F75 | cross-definition | words: 29:38:14 | branches: س ب ل B010; ع ن ك ب B001 | trigger: 29:41:9; 29:41:16 | with: F74; F65 | image: The path-word's eye-disease is defined as a film "like a spider's weaving". Together with F74, the ayah's two closing nouns, road and sight, each carry 29:41's spider-house in their definitions: a web over the eye and a seam in the tent. | anchor: السبل داء في العين شبه غشاوة كأنها نسج العنكبوت بعروق حمر; العنكبوت الدويبة الناسجة

### F76 — window
F76 | window | words: 29:38:16; 29:38:7; 29:38:15 | branches: ب ص ر B007; ح ص ب B001; س ك ن B002 | trigger: 29:40:8 (window) | with: F54; F36 | image: Soft white stone that cuts easily is the kind Thamud carved into houses. 15:82 even closes on the same pattern as this ayah, وكانوا + participle: "they carved houses from mountains, secure". Pebbles are what 29:40's wind hurls: the stone of the dwellings and the stone of the punishment. | anchor: البصرة الحجارة الرخوة وبصر بكسر الباء من الأصل الثاني; الحَصْباء والحصى | memory: yes

### F77 — window
F77 | window | words: 29:38:16; 29:38:4 | branches: ب ص ر B004; ت ر ك B002 | trigger: 29:35:2 (window) | with: F27; F81 | image: A blood-spot fallen on the ground is the trace a tracker follows. The dwellings are that trace, making the event clear to whoever follows it. | anchor: البصيرة القطعة من الدم إذا وقعت بالأرض استدارت; إبقاء الأثر بعد الترك

### F78 — fragment
F78 | fragment | words: 29:38:16 | branches: ب ص ر B005; ج و ب B005; ع ج ز B002 | trigger: 29:24:3 (window); 29:22:3 (window) | with: F64 | image: Shield and armour (بصيرة) belong to armoured peoples who still could not slip away: "you cannot escape on earth" (29:22). | anchor: بصيرة السلاح; فوت وسبق وإفلات من الطلب

### F79 — scene
F79 | scene | words: 29:38:1; 29:38:2; 29:38:4; 29:38:7 | branches: ع و د B012; ح ص ب B003; ص ي ح B002; ب ي ن B004 | trigger: 29:40:8 (window); 29:40:12 (window) | with: F14; F38 | image: 29:40 gives the named peoples their mechanisms: the grit-bearing wind for Ad (69:6; 46:24-25, "nothing seen but their dwellings") and the Cry for Thamud (11:67). The wind strips the land until only the dwellings stand clear, which is تبيّن من مساكنهم. | anchor: الريح الحاصب; الصيحة المفزعة | memory: yes

### F80 — scene
F80 | scene | words: 29:38:7; 29:38:1 | branches: س ك ن B002; ء ي ي B003 | trigger: 29:35:4 (window); 29:44:9 (window) | with: F54; F72 | image: Ad built "a آية on every height" in idle play and made cisterns hoping to last forever (26:128-129). Their self-made landmarks are reversed: their dwellings are now the آية that is clear to others. | anchor: علامة ظاهرة | memory: yes

### F81 — scene
F81 | scene | words: 29:38:4; 29:38:5; 29:38:16 | branches: ب ي ن B004; ب ص ر B002; ت ر ك B002 | trigger: 29:35:2 (window); 29:35:5 (window); 29:35:7 (window) | with: F27; F45; F77 | image: This is the partner scene of channel 12A. A clear trace of Lot's town is left "for people who reason" (29:35), and here a trace is clear "for you". The ayah adds that the ruined were clear-sighted themselves: one sign, two sets of eyes, and sight did not save the first. | anchor: إبقاء الأثر بعد الترك; ظهور الشيء وانكشافه

### F82 — fragment
F82 | fragment | words: 29:38:10 | branches: ش ط ن B002; ع ق ل B002; ج د ل B001 | trigger: 29:35:7 (window); 29:43:6 (window); 29:46:2 (window) | with: F62 | image: A contest of ropes: the shaytan is the long twisted rope that draws out of the well. Against it stand the reason-tether of 29:35 and 29:43 and the tight-woven cord of 29:46. | anchor: الحبل الطويل والشد; عَقْل البعير بالعِقال; الفَتْل المحكم

### F83 — fragment
F83 | fragment | words: 29:38:1 | branches: ع د د B004; ع د د B005 | trigger: 29:38:12 (ayah); 29:38:14 (ayah) | with: F62 | image: As a sound-family echo of عادًا (from pairs.md, not the dictionary), it gives unfailing perennial water and recurrence at known times. It sits beside the ayah's road-to-water and rain. | anchor: الماء العد; عداد الوقت ومعاودته | memory: yes

### F84 — local
F84 | local | words: 29:38:1; 29:38:4; 29:38:12 | branches: ع و د B001; ب ي ن B012; ص د د B001 | trigger: 29:38:4 (ayah); 29:38:12 (ayah) | with: F28; F1 | image: The name of return stands beside a separation "that cuts off return" and beside a turning-away. The people called Return are turned from the road and parted irrevocably from their dwellings. | anchor: طلاق يقطع الرجعة; رجوع بعد انصراف وتثنية بعد بدء

### F85 — window
F85 | window | words: 29:38:4 | branches: ب ي ن B003; ب ي ن B001 | trigger: 29:25:9 (window) | with: F40 | image: The root both joins and severs. 29:25's "affection between you" is the bond; 29:38's تبيّن is the ruin after the parties have parted. Channel 4's movement from connection to separation is enacted on the dwellings. | anchor: الوصلة القائمة بين الأطراف; انفصال الشيء وافتراقه

### F86 — window
F86 | window | words: 29:38:10 | branches: ش ط ن B004; ع ث و B001; ك ب ر B006 | trigger: 29:36:13 (window); 29:39:8 (window) | with: F71 | image: The rebellious overreacher (عات, sound-near to 29:36's عثو) stands between the corruption in the earth forbidden in 29:36 and the arrogance in the earth of 29:39. The shaytan of 29:38 is the type of both. | anchor: كل عات متمرد من الجن والإنس والدواب شيطان; الفساد في الأرض

### E_F1 — supports
F1 | supports | 46:25 [staging, same-word], 14:45 [same-word], 11:68, 28:58 [same-word] | The Quran stages the disclosure-through-departure openly: after Ad's wind "nothing was seen but their dwellings" (46:25), and 14:45 joins تبيّن لكم with the dwellings of the wrongdoers. 11:68 and 28:58 add the other half of the root: the people are gone "as if they had never dwelt there", and the dwellings stand almost unlived in after them.

### E_F2 — supports
F2 | supports | 27:52 [staging], 22:45 [staging], 11:68, 37:135 | The abandoned camp is told openly: houses "fallen empty" (27:52), towns collapsed on their roofs with a disused well and a lofty palace (22:45). The غابرين of the window recurs for Lot's wife in 37:135. No passage names a raven of parting, and that silence says nothing against the finding.

### E_F3 — shifts
F3 | shifts | 22:46, 30:9 | The eye does range over the ruin-field: "have they not travelled in the land and looked" (30:9). 22:46 adds that the eyes crossing the field are not what fails; the hearts are blind. So the eye's reach is bounded by the heart, and the field's width is not reduced.

### E_F4 — supports
F4 | supports | 4:60 [same-word], 4:167 [same-word], 14:3 [same-word], 43:38 | The shaytan "wants to lead them into far error" (4:60), and blocking ends in far error (4:167, 14:3). 43:38 expands the gap. On arrival the man wishes "between me and you" were the distance of the two easts, so the widened distance finally opens between the man and the far one himself.

### E_F5 — supports
F5 | supports | 7:16 [staging, same-word], 7:17 [staging], 7:45 [same-word], 7:86 [same-word], 11:19 [same-word] | Iblis vows to sit on the straight path and to come at them from front, behind, right and left (7:16–17). This stages the turning of a man aside from the direction his face intends. The صدّ + seeking-it-crooked (عوج) pairing is confirmed in 7:45, 7:86 and 11:19.

### E_F6 — supports
F6 | supports | 43:62 [same-word], 43:36 [same-word], 43:37 [same-word], 5:91 [same-word], 13:33 [same-word] | The shaytan is the direct subject of صدّ in 43:62 and 5:91, and the devil-companion of 43:36 is the one who blocks "from the road" in 43:37. 13:33 confirms the bare definite السبيل beside passive adornment.

### E_F7 — supports
F7 | supports | 35:8 [same-word], 6:43 [same-word], 16:63 [same-word], 27:4 [same-word], 6:108 [same-word] | 35:8 defines the effect as seeing: "he sees it as good". 6:43 and 16:63 repeat the shaytan-as-agent pattern. 27:4 and 6:108 name God as the one who adorns deeds for them; this bounds the shaytan's agency beneath God's decree without undoing the appearance reading.

### E_F8 — expands
F8 | expands | 27:24 [same-word], 43:37 [same-word], 7:30 | Beside the twin's closing "they are unguided" (27:24), the Quran supplies a third closing: "and they reckon that they are guided" (43:37; also 7:30, where devils are taken as patrons). The "clear-sighted" state thus has a self-assessing counterpart in the same formula family.

### E_F9 — expands
F9 | expands | 40:37 [same-word], 10:88, 40:36 | Pharaoh's adornment-and-blocking (40:37) comes right after his tower built to look up at Moses' God (40:36–37). 10:88 says Pharaoh and his chiefs were given adornment (زينة) and wealth "to lead astray from Your way". The mechanism enters 29:39's group as both adornment worn and a built lookout.

### E_F10 — supports
F10 | supports | 16:63 [same-word], 8:48 [same-word], 59:16 [staging, same-word], 14:22 [staging, same-word], 4:119 [same-word], 7:27 | The adorner becomes patron (16:63; 4:119 "whoever takes the shaytan as walī apart from God"; 7:27). He then disowns them (59:16) and declares at the end that he had no authority and cannot come to their aid (14:22). This is the absent ولي and نصير of 29:22.

### E_F11 — supports
F11 | supports | 47:25 [same-word], 47:32 [same-word], 4:115 [same-word] | Clarity followed by turning is a set Quranic sequence. "After guidance had become clear to them, the shaytan embellished for them" (47:25; also 47:32). 4:115 joins تبيّن with choosing a road (سبيل) other than the believers'.

### E_F24 — shifts
F24 | shifts | 15:76 [staging, same-word], 37:137 [staging], 37:138, 26:128 | The Quran does stage a caravan road, but it puts the travellers on the listeners' side. The ruined town lies "on a road that still stands" (15:76), and "you pass by them in the morning and at night" (37:137–138). Ad's own road-side works are "a sign on every high place" (26:128). The ruined themselves are never staged as travellers.

### E_F25 — supports
F25 | supports | 53:50 [same-word], 89:7, 89:8 | The Quran itself calls them "Ad the first" (53:50). It names Iram of the pillars, "the like of which was not created in the lands" (89:7–8), marking Ad as the proverbially ancient.

### E_F26 — supports
F26 | supports | 26:137 [staging], 7:70 [staging], 11:62 [staging] | Ad themselves call their way "nothing but the custom (khuluq) of the ancients" (26:137) and refuse to leave what their fathers worshipped (7:70). Thamud say the same (11:62). Inherited habit is voiced by the very peoples named.

### E_F27 — shifts
F27 | shifts | 20:128 [same-word], 37:137, 44:29, 7:93 | The visit is real: the listeners "walk in their dwellings" (20:128) and pass them morning and night (37:137). The Quran refuses the mourning, though. Heaven and earth did not weep for the destroyed (44:29), and Shuʿayb asks how he could grieve for a disbelieving people (7:93). The return-visit is kept, and condolence is turned into a lesson.

### E_F28 — supports
F28 | supports | 36:31 [staging], 21:95, 21:13 [staging, same-word], 23:100 | "They will not return to them" (36:31) and it is forbidden to a destroyed town that they return (21:95). The mocking order to "return to your luxury and your dwellings" (21:13) stages the impossible return to the مساكن. Their only return is the final one, refused a way back (23:100).

### E_F29 — supports
F29 | supports | 19:98 [staging], 46:25 [same-word] | "Do you perceive any one of them or hear from them a whisper?" (19:98) stages the silenced people. Only their dwellings remain to be seen (46:25).

### E_F33 — supports
F33 | supports | 7:78 [staging], 11:67 [staging], 69:7 [staging] | Thamud were seized by the quake and "became prostrate in their homes" (7:78), or by the Cry, fallen in their homes (11:67). Ad lie "felled as if hollow palm-trunks" (69:7). The stillness of settlement becomes the stillness of the dead, told openly.

### E_F34 — supports
F34 | supports | 7:78, 11:67, 14:45 [same-word] | The Quran alternates دار/ديار (7:78, 11:67) and مساكن (14:45) for the same destroyed homes, which confirms the dictionary's cross-definition.

### E_F35 — expands
F35 | expands | 61:12 [same-word], 9:72 [same-word], 34:15 [same-word], 9:24 [same-word] | The chain gains its positive pole in "goodly dwellings in gardens of Eden" (61:12; 9:72). 34:15 shows a dwelling that was itself a sign of blessing before ruin. 9:24 warns of "dwellings you are pleased with" rivalling God.

### E_F36 — supports
F36 | supports | 7:74, 26:129, 26:149, 22:45 [staging], 41:15 | Thamud "take" palaces and carve mountain houses (7:74; 26:149), and Ad "take" great works (26:129), with the same verb as the spider that "took a house". 22:45's lofty palace stands empty. 41:15 answers Ad's "who is stronger than us": the one who created them is stronger.

### E_F37 — contradicts
F37 | contradicts | 41:18, 11:58, 11:66, 7:72, 28:58 [same-word] | The Quran states that Hud and Salih and those who believed with them were rescued (11:58, 11:66, 7:72), right after Ad and Thamud in 41:18. This contradicts the claim that here "no one is extracted". The other half, dwellings left almost unlived in (28:58), stands.

### E_F38 — supports
F38 | supports | 46:25 [same-word], 32:26 [same-word], 20:128 [same-word], 28:58 [same-word], 14:45 [same-word] | All five passages treat the مساكن of destroyed peoples as seen and walked-through remains. Two of them (46:25 and 14:45) come closest to 29:38's wording.

### E_F39 — shifts
F39 | shifts | 42:33 | The Quran places the stilling of ships with God, who "if He wills, stills the wind and they stand motionless on its back" (42:33). The steadying of the vessel is His, which sharpens the rudder image without reversing it.

### E_F40 — expands
F40 | expands | 30:21, 9:103, 7:189 | The true سكن is set out with the same words as 29:25: spouses "that you may rest in them, and He set between you affection and mercy" (30:21). The Prophet's prayer is also a سكن (9:103). The idol-bond "affection between you" of 29:25 is the counterfeit of this rest.

### E_F41 — expands
F41 | expands | 28:81 [staging], 28:82, 2:61 | Qārūn's adornment ends when "We caused the earth to swallow him and his house" (28:81), and those who envied his place recant the next morning (28:82). 2:61 attests the root's abasement-and-destitution sense (مسكنة) as a stamped punishment.

### E_F42 — shifts
F42 | shifts | 91:14 [staging], 11:65, 69:7 | In Thamud's own story the slaughter is theirs: they hamstrung the she-camel (11:65, 91:14), and their Lord then levelled them. Ad lie felled like palm trunks (69:7). The pinned victim is thus the slaughterer paid back.

### E_F45 — supports
F45 | supports | 47:14 [same-word], 35:8 [same-word] | 47:14 sets the two showings against each other in one sentence: "is one who stands on clear evidence (بيّنة) from his Lord like one to whom his evil deed is adorned?". 35:8 confirms that the adornment wins through the eye.

### E_F46 — expands
F46 | expands | 15:15, 2:7, 45:23 | The Quran does not name paint on the eye. It does say sight can be made to see wrongly while open, "our eyes have only been dazzled/drugged" (15:15), and it lays a covering on sight (2:7, 45:23).

### E_F47 — expands
F47 | expands | 37:65 [same-word], 7:20 [staging, same-word], 7:26, 7:27 | Shayāṭīn's heads are the Quran's image of hideousness (37:65). The adorner's first scene ends by exposing the shame (سوءات) he promised to cover (7:20). He strips the garment that God gave as covering and adornment (7:26–27). The ugly seller of beauty finally unmasks ugliness.

### E_F48 — supports
F48 | supports | 11:15, 11:16, 7:137 | Whoever wants the worldly life "and its adornment" (11:15) finds "what they made (ṣanaʿū) there has come to nothing" (11:16). 7:137 destroys "what Pharaoh and his people used to make". Adornment and making stand in one frame.

### E_F49 — expands
F49 | expands | 57:20, 28:60, 18:7, 18:8 [staging] | Beyond the worldly-life collocation (57:20, 28:60), 18:7–8 says what is on earth was made its adornment as a test and will be turned into barren ground. Adornment ends as bare land, as the dwellings did.

### E_F50 — supports
F50 | supports | 67:5 [same-word], 37:6 [same-word], 37:7, 15:17 | The adorned sky is guarded against every rebellious shaytan (37:6–7; 15:16–17). Its lamps are missiles against the shayāṭīn (67:5).

### E_F51 — supports
F51 | supports | 10:24 [staging], 7:4, 68:20 [staging] | The adorned land erased by a command at night or by day (10:24) is matched by towns struck by night or at midday (7:4) and by the garden "that became by morning like a stripped harvest" (68:20).

### E_F52 — supports
F52 | supports | 28:79, 28:81 [staging] | Qārūn goes out "in his adornment" (28:79), and he and his house are swallowed (28:81). Adornment steps into the next ayah as a person.

### E_F54 — supports
F54 | supports | 26:129, 7:74, 89:9, 34:13, 36:35 | The Quran uses the ʿ-m-l verb for building (the jinn "worked" sanctuaries and statues, 34:13) and speaks of "what their hands worked" (36:35). Ad's great works (26:129) and Thamud's carved rock (7:74, 89:9) are the adorned works that now testify.

### E_F55 — supports
F55 | supports | 29:58, 3:136, 18:104 [staging], 18:105 [same-word], 47:1 [same-word], 25:23 | Against "excellent is the wage of the workers" (29:58; 3:136), the Quran stages the unpaid labour of those "whose effort was lost while they reckoned they did well" (18:104–105). Of those who block from God's way it says, "He has led their works astray" (47:1). 25:23 turns works to scattered dust.

### E_F57 — expands
F57 | expands | 24:24, 36:65 | Legs testify against their owners "about what they used to work" (24:24) and to what they earned (36:65). The Quran binds legs and deeds as the dictionary does.

### E_F60 — expands
F60 | expands | 46:24 [staging] | Ad saw the punishment as a cloud "facing their valleys" and read it as rain-bearing (46:24). What faced them was seen and misread: the facing thing and the turning-away meet in the named people.

### E_F61 — supports
F61 | supports | 43:57 [same-word], 8:34 [same-word], 8:35 | 43:57 uses the root for clamour. In 8:34–35, "they block from the Sacred Mosque" is followed at once by prayer that is whistling and hand-clapping. Blocking and noise stand side by side.

### E_F62 — expands
F62 | expands | 54:28 [staging], 26:155, 91:13, 22:45 [staging] | Thamud's water is "divided between them" and the she-camel (54:28; 26:155; 91:13): their story is a water-dispute. 22:45 places "a disused well" among the ruins, completing the road-to-water scene.

### E_F66 — supports
F66 | supports | 7:86 [staging, same-word], 7:16 [staging] | Shuʿayb forbids sitting "on every road, threatening and blocking from God's way" (7:86): literal road-cutting and صدّ in one clause. Iblis sits on the straight path (7:16). Highwayman and blocker are the same figure.

### E_F68 — supports
F68 | supports | 69:7 [staging], 46:25 [same-word], 7:78 | Ad's wind blew "seven nights and eight days" (69:7), and "by morning" nothing was seen but their dwellings (46:25). Thamud likewise "became by morning" fallen (7:78). The bad night before the morning of ruin is told openly.

### E_F70 — supports
F70 | supports | 11:93, 25:34, 5:60, 36:67, 36:66 | The مكانة/مكان pairings with work and road stand as counted. 36:66–67 adds that, just before being transfixed in their places, eyes wiped out race for the road and cannot see it.

### E_F71 — supports
F71 | supports | 23:76 [staging], 6:43 [same-word], 3:146 | "They did not humble themselves (استكانوا) to their Lord nor implore" (23:76) confirms the root link. 6:43 sets adornment where humbling should have been. 3:146 shows the believers who "did not yield" in the opposite sense.

### E_F72 — supports
F72 | supports | 17:59 [staging], 41:17 [staging] | Thamud were given the she-camel "sight-giving" and wronged it (17:59). "As for Thamud, We guided them, and they preferred blindness to guidance" (41:17): the clear-sighted people chose blindness, told outright.

### E_F73 — supports
F73 | supports | 17:12, 27:13 | The daytime sign is "sight-giving" (17:12). Moses' sight-giving signs were called "clear magic" (27:13): the illuminating sign is refused in the next ayah's company.

### E_F74 — expands
F74 | expands | 16:80 | God made from your houses a سكن and from the hides of cattle houses light to carry (16:80). These leather tents are the kind whose panel-seam the dictionary calls بصيرة.

### E_F75 — expands
F75 | expands | 45:23, 2:7 | The Quran names the web-like film on sight غشاوة (2:7). In 45:23 it falls on one who "took" his desire as a god and was led astray "upon knowledge": sight covered while knowledge is present.

### E_F76 — supports
F76 | supports | 15:82, 54:34 | 15:82 closes with كانوا, their carving of houses, and the participle "secure", close to 29:38's closing. The Quran's own use of حاصب is for Lot's people (54:34), so the stone-of-punishment link is to 29:40's list, not to Thamud.

### E_F77 — expands
F77 | expands | 40:21, 40:82, 30:9, 18:64 [staging] | The Quran names the traces former peoples left in the land (آثار, 40:21, 40:82), to be looked at by travellers (30:9). It stages tracking back along footprints (18:64).

### E_F79 — shifts
F79 | shifts | 54:34, 51:41, 41:16, 69:6 [same-word], 11:67, 11:94, 46:25 [same-word] | The Quran's own حاصب is Lot's (54:34), and Ad's wind is the barren, roaring, overreaching wind (51:41, 41:16, 69:6). The Cry is Thamud's (11:67) and also Midian's (11:94). The wind that leaves only the dwellings visible (46:25) is fully supported; only the assignment of حاصب to Ad shifts.

### E_F80 — supports
F80 | supports | 26:128, 26:129, 26:139 [staging] | Ad built "a sign on every high place" in idle play (26:128–129). Three ayat later the Quran declares their destruction the sign (26:139): self-made landmark reversed into God's.

### E_F81 — supports
F81 | supports | 46:26 [staging], 51:37, 29:35 | Ad were given hearing, sight and hearts, "yet their hearing, their sight and their hearts availed them nothing" (46:26). A sign was left for those who fear (51:37). One sign serves two sets of eyes, and the first set's sight did not save it.

### E_F84 — supports
F84 | supports | 21:13 [staging, same-word], 36:31, 23:99, 23:100 | "Return to your dwellings" is a taunt at the moment of ruin (21:13). The destroyed do not return (36:31), and the plea "send me back" is refused (23:99–100).

### E_F85 — supports
F85 | supports | 6:94 [staging], 2:166, 10:28 | "Your bond (بين) has been severed" (6:94), "all ties cut" (2:166), and "We separated between them" (10:28). The Quran enacts the root's joining-then-severing on idolatrous bonds.

### E_F86 — expands
F86 | expands | 51:44 [staging], 7:77, 69:6 [same-word], 19:44 [same-word], 4:117 [same-word] | Thamud "overreached (عتوا) against their Lord's command" (51:44; 7:77), and Ad were destroyed by an overreaching (عاتية) wind (69:6). Shaytan is "rebellious" (19:44) and "defiant" (4:117). The shaytan's overreaching is theirs and is answered in kind.

### Q1 — qeq
Q1 | qeq | words: 29:38:16 | branches: ب ص ر B002; ز ي ن B002 | trigger: 40:37:3 (qeq); 40:37:11 (qeq); 40:37:15 (qeq) | with: F9; F12 | shows: Pharaoh builds a tower "that I may look up to Moses' God" just before "his evil deed was adorned and he was blocked from the road". The seeking-sight branch of مستبصرين is staged: a self-appointed seer whose looking ends in adornment and blocking.

### Q2 — qeq
Q2 | qeq | words: 29:38:16; 29:38:14; 29:38:15 | branches: ب ص ر B001; س ب ل B001; س ب ق B004 | trigger: 36:66:5 (qeq); 36:66:6 (qeq); 36:66:7 (qeq); 36:66:9 (qeq) | with: F70; F13 | shows: The inverse scene: eyes wiped out, they race for the road, "and how would they see?". 29:38's people kept eyes and road and were turned. 36:66's racing uses the root of 29:39's "they could not outrun".

### Q3 — qeq
Q3 | qeq | words: 29:38:4; 29:38:14 | branches: ب ي ن B004; س ب ل B001 | trigger: 15:76:2 (qeq); 15:79:5 (qeq) | with: F24; F81; F1 | shows: The ruined towns lie "on a standing road" and "on a clear highway". Road and clarity, the two words of 29:38, meet at the ruins: the road they were turned from runs past their remains for the listeners.

### Q4 — qeq
Q4 | qeq | words: 29:38:12; 29:38:14; 29:38:16 | branches: ص د د B003; س ب ل B005; ب ص ر B002 | trigger: 46:24:2 (qeq); 46:24:4 (qeq); 46:24:9 (qeq) | with: F60; F62; F12 | shows: Ad "saw" the cloud "facing their valleys" and said "this cloud brings us rain". The facing branch of صدّ, the rain branch of سبيل and a failed act of sight meet in the named people's last moment.

### Q5 — qeq
Q5 | qeq | words: 29:38:15; 29:38:16; 29:38:2 | branches: ب ص ر B001 | trigger: 51:44:1 (qeq); 51:44:8 (qeq) | with: F81; F72; F86 | shows: Thamud were seized by the thunderbolt "while they were looking on". The seeing state persists into the moment of seizure, a narrative echo of "and they were clear-sighted".

### Q6 — qeq
Q6 | qeq | words: 29:38:1; 29:38:7 | branches: ع و د B001; س ك ن B002 | trigger: 21:13:3 (qeq); 21:13:8 (qeq) | with: F28; F84 | shows: "Return to your luxury and your dwellings": the return-word and the dwelling-word are joined in a taunt to a destroyed town. This activates the return branch of عاد beside مساكن.

### Q7 — qeq
Q7 | qeq | words: 29:38:7; 29:38:4 | branches: س ك ن B004; ب ي ن B003 | trigger: 30:21:9 (qeq); 30:21:12 (qeq); 30:21:13 (qeq) | with: F40; F85 | shows: Rest (سكن) and "affection between you" stand in one ayah as God's sign. This is the true form of the dwelling-rest and bond that 29:25 counterfeits and 29:38's emptied dwellings end.

### Q8 — qeq
Q8 | qeq | words: 29:38:4 | branches: ب ي ن B003 | trigger: 54:28:3 (qeq); 54:28:5 (qeq) | with: F62; F85 | shows: "The water is divided between them": Thamud's test is a بين over water, a shared bond they broke by killing the she-camel.

### Q9 — qeq
Q9 | qeq | words: 29:38:1; 29:38:11 | branches: ع و د B004; ع م ل B001 | trigger: 26:137:4 (qeq) | with: F26 | shows: Ad's own word for their way, "the custom (khuluq) of the ancients", activates the habit branch of their name: their works defended as second nature.

### Q10 — qeq
Q10 | qeq | words: 29:38:16; 29:38:10 | branches: ب ص ر B001; ب ص ر B002 | trigger: 45:23:6 (qeq); 45:23:10 (qeq) | with: F12; F75 | shows: One "led astray upon knowledge" with a covering set on his sight. Knowledge present and sight covered: the concessive reading of مستبصرين given a Quranic formula.

### A1 — axis
A1 | axis | 14:45 [same-word] | The closest construction: "and it became clear to you how We dealt with them", beside living in the dwellings of wrongdoers. This specifies the unstated content of تبيّن لكم من مساكنهم: God's dealing with them.

### A2 — axis
A2 | axis | 25:38 [same-word], 25:39, 53:50 [same-word], 53:51 | The same accusative pair Ad and Thamud hangs on a surrounding verb (25:37–39, "all We destroyed utterly"). It appears with the verb explicit in "He destroyed Ad the first, and Thamud, and spared none" (53:50–51). This supplies the understood governing verb.

### A3 — axis
A3 | axis | 9:70 [same-word] | Ad and Thamud named among earlier peoples, closing "God did not wrong them, but they wronged themselves": the same judgment as 29:40, which gathers 29:38's pair.

### A4 — axis
A4 | axis | 32:26 [same-word], 20:128 [same-word], 37:137 [staging], 37:138 | Defines the addressees of لكم: listeners who walk through, or pass morning and night by, the dwellings of the destroyed.

### A5 — axis
A5 | axis | 27:24 [same-word], 40:37 [same-word], 13:33 [same-word] | The formula elsewhere: active with the shaytan as agent (27:24), passive (40:37, 13:33). Bare definite السبيل is the fixed target.

### A6 — axis
A6 | axis | 35:8 [same-word], 47:14 [same-word] | The Quran's own definition of زيّن for deeds: one "sees it as good". It is opposed to standing on a بيّنة from one's Lord.

### A7 — axis
A7 | axis | 6:43 [same-word] | Sets the adornment in time: calamity came, hearts hardened instead of humbling, and then the shaytan adorned their deeds.

### A8 — axis
A8 | axis | 14:22 [same-word], 15:42 | Limits the external agent. The shaytan has no authority except over those who follow him; he only invited. This explains why لهم, أعمالهم and the هم of صدّهم keep the responsibility with them.

### A9 — axis
A9 | axis | 43:36 [same-word], 43:37 [same-word] | Specifies how the shaytan blocks: an assigned companion who turns them "from the road while they reckon they are guided". This fixes the self-assessment reading of مستبصرين.

### A10 — axis
A10 | axis | 41:17 [staging], 46:26 [staging] | Plain sense of "they were clear-sighted": Thamud were guided and preferred blindness. Ad were given sight, hearing and hearts that did not avail them.

### A11 — axis
A11 | axis | 12:108 [same-word] | Road and insight paired positively: "this is my way (سبيلي); I call to God upon clear sight (بصيرة)". 29:38 is its negative.

### A12 — axis
A12 | axis | 7:201 | The one other shaytan-plus-sight construction: the God-fearing, touched by the shaytan, remember "and at once they see". Sight restored against the shaytan, where in 29:38 sight present did not hold.

### A13 — axis
A13 | axis | 22:46, 6:104 | Defines which sight fails: "it is not the eyes that go blind but the hearts". Insights come from the Lord, and whoever sees does so for himself.

### A14 — axis
A14 | axis | 2:256 [same-word], 4:115 [same-word] | The قد + تبيّن construction certifying completed clarity ("the right way has become clear from error"). 4:115 joins تبيّن to choosing a road.

### A15 — axis
A15 | axis | 11:59, 26:128, 26:130, 41:15, 7:77, 26:149 | Specifies "their deeds": Ad rejected signs, followed every tyrant, built idle landmarks, struck like tyrants and grew arrogant. Thamud carved houses exultantly, hamstrung the she-camel and overreached.

### A16 — axis
A16 | axis | 27:4 [same-word], 6:108 [same-word] | God named as the one who adorns their deeds for them. The shaytan's adorning in 29:38 works within God's decree; the anchor's single agent is not the Quran's whole account.

QeQ tags describe evidence, not obligations. A same-word passage may provide a decisive definition; a staging passage may duplicate another. Preserve the explanatory job and real counter-evidence. The full source records above remain available even when a passage is not quoted.


===== dictionary.md =====
# dictionary.md — every branch of every root of 29:38's words

One line per branch: Bnnn | gloss | Arabic image | definition | first classical source phrase.
`~alt` = a cited alternative analysis of the word; `~echo` = a sound-family root (not the word's root).
Cite a branch as `root Bnnn`, e.g. `ر ب ب B007`; its Arabic may be quoted with that source.

### ع و د — 29:38 w1 وَعَادًا
- B001 geri dönme ve yeniden yapma | رجوع بعد انصراف وتثنية بعد بدء | Bir yerden, nesneden ya da işten ayrıldıktan sonra ona geri yönelmek veya başlanmış bir şeyi bir kez daha yapmak; türemiş biçimlerde bir başkasına yeniden yaptırmak ya da tekrar istemektir. | أصل يدل على تثنية في الأمر (maqayis)
- B002 dönüş yeri ve son varış | مصير ومرجع ومعاد | Bir varlığın sonunda döneceği yer veya ulaşacağı son durak; bağlama göre dönüşün gerçekleştiği zaman ya da mekândır. | المعاد كل شيء إليه المصير (maqayis)
- B003 tek söz söylememek | سكوت لا يبدئ ولا يعيد | Belirli bir olumsuz anlatım içinde, kişinin ne konuşmayı başlatması ne de bir karşılık vermesi, yani hiçbir söz söylememesidir. | رأيت فلانا ما يبدئ وما يعيد أي ما يتكلم ببادية ولا عادية (ayn)
- B004 tekrarla alışkanlık ve yatkınlık kazanma | عادة ودرَبة ومواظبة | Bir eylemi tekrar tekrar yaparak onu kolay, yerleşik bir davranış veya yatkınlık hâline getirmek; bu yolla süreklilik, deneyim ve yapabilme gücü kazanmaktır. | العادة الدربة والتمادي في شيء حتى يصير له سجية (maqayis
- B005 hasta veya yas ziyareti | عيادة ومعادة وزيارة راجعة | Bir hastayı ziyaret etmek veya bir felaket ya da yas dolayısıyla insanların aynı haneye gidip gelmesi; türemiş adlarda bu ziyaretçiler ya da ziyaret edilen acı olay da anlatılır. | العيادة أن تعود مريضا (maqayis)
- B006 kişiye dönen yarar ve iyilik | عائدة ومعروف يرجع | Bir kimseye iyilik, bağış, şefkat, yarar veya kolaylık olarak ulaşan ve onun lehine sonuç veren şey; türemiş yapılarda daha yararlı olma ya da yapılan iyiliği artırma anlamıdır. | عاد فلان بمعروفه إذا أحسن ثم زاد (ayn)
- B007 yeniden gelen özel gün veya hâl | عيد وحال يعاود | Belirli aralıklarla yeniden gelen toplanma veya sevinç günü; ayrıca kişiye tekrar tekrar dönen kaygı, sevgi ya da başka bir durumdur. | العيد ما يعتاد من خيال أو هم (maqayis)
- B008 gücü kalmış yaşlı deve | عود مسن فيه بقايا قوة | İleri yaşa gelmiş fakat gücünden bir miktar kalmış deve; bazı aktarımlarda dişi koyunu da kapsar. Türemiş biçim yaşlanmayı, kalıplaşmış söyleyiş ise deneyimli yaşlılardan yardım almayı anlatır. | الجمل المسن فهو يسمى عودا (maqayis)
- B009 eski yol ve köklü geçmiş | قدم وطريق عود | Uzun zamandır var olan ve yolcuların tekrar tekrar kullandığı eski yol; belirli tamlamalarda geçmişten gelen köklü saygınlığı veya eski akrabalık bağını niteler. | العود الطريق القديم (ayn)
- B010 tahta parçası, tütsülük odun veya telli çalgı | عود من خشب وطيب وآلة | Bir tahta parçası veya ince dal; özel kullanımlarda yakılarak kokusundan yararlanılan odun ya da çalınan telli bir müzik aletidir. | الأصل الآخر فالعود وهو كل خشبة دقت (maqayis)
- B011 bağlayıcı eş sözünden ilgili davranışa dönüş | عود الظهار إلى ما قيل | Eş hakkında kurulmuş bağlayıcı bir sözden sonra, o sözle ilişkili davranışa dönmeyi bildiren özel hukukî yapıdır; dönüşün ne olduğu, sözü yineleme, cinsel birliktelik, evliliği sürdürme veya kaçınılacağı söylenen işi yapma biçimlerinde farklı yorumlanır. | ثم يعودون لما قالوا (mufradat)
- B012 biçime bağlı adlandırmalar | عاد وأعلام منسوبة إليها | Bu dal tek bir kavram değil, eski bir kavmin adı, o kavme bağlanan eskilik nitelemesi, bağımsız bir erkek adı ve kökeni tartışmalı bir soylu deve adından oluşan yapısal bir demettir. | عاد قبيلة وهم قوم هود (sihah)

### ب ي ن — 29:38 w4 تَّبَيَّنَ
- B001 ayrılıp kopma | انفصال الشيء وافتراقه | Bir şeyin ya da tarafların önceki bağlantı, birliktelik veya yakınlıktan ayrılması, kopması ve birbirinden uzak düşmesidir. | البين الفراق (maqayis
- B002 arada olma | الخلالة والوسط بين شيئين | İki veya daha çok taraf arasında kalan orta, aralık, mesafe ya da iç konumdur; bazı kalıplarda birine yakın veya bir topluluğun içinden olma anlamına bağlanır. | بين بمعنى وسط (sihah)
- B003 arayı bağlayan ilişki | الوصلة القائمة بين الأطراف | Taraflar arasında kopmayı değil, onları birleştiren bağ, ilişki, yakınlık veya dostluk durumunu anlatır. | البين الوصل (ayn
- B004 açığa çıkıp belirginleşme | ظهور الشيء وانكشافه | Bir şeyin gizlilikten veya belirsizlikten çıkıp görünür, anlaşılır ve açık hale gelmesidir; bu açıklık kanıt ya da açık işaret olarak da gerçekleşebilir. | بان الشيء وأبان إذا اتضح وانكشف (maqayis)
- B005 anlamı açıkça ortaya koyma | كشف المعنى بالقول أو العلامة | Bir anlamı söz, yazı, işaret veya düzgün anlatımla açığa çıkarıp anlaşılır kılmadır; kişide açık ve düzgün konuşma yetisi olarak da kullanılır. | أبين من فلان أي أوضح كلاما منه (maqayis)
- B006 geniş uzaklık | بعد المسافة واتساع الفجوة | İki nokta, taraf veya yüzey arasında büyük uzaklık ve geniş açıklık bulunmasıdır; kuyu gibi nesnelerde ağız ile dip arasındaki uzaklık olarak görünür. | أصل واحد وهو بعد الشيء (maqayis)
- B007 göz erimindeki arazi parçası | قطعة أرض تمتد في النظر | Gözün uzanabildiği ölçüde görülen bir arazi parçası, tarafı, yöresi veya yer yer kabarık bölgesidir. | البين قطعة من الأرض قدر مد البصر (maqayis)
- B008 bağlı yerinden ayrılma | انفراج العضو أو الشيء عن ملاصقه | Belirli cisimsel kalıplarda bir organın, yayın teli gibi bir parçanın ya da başın bağlı olduğu yerden ayrılması, açılması veya koparılmasıdır. | بانت يد الناقة عن جنبها (ayn)
- B009 sol yandan sağan kişi | الحالب من جهة مخصوصة | Sağımda iki sağandan biri, özellikle hayvanın sol tarafından gelen sağan kişidir; karşısında sağ taraftan gelen eş sağan bulunur. | البائن أحد الحالبين والآخر يسمى المستعلي (ayn)
- B010 o sırada | الوقت الواقع أثناء حال أو فعل | Bir durum veya eylem sürerken başka bir olayın gerçekleştiğini bildiren zaman bağlacı kullanımıdır. | قولك بينا فلان معناه بينما (ayn)
- B011 iki arada kalmış hal | حالة متوسطة بين طرفين | İki uç değer arasında kalan ara veya orta haldir; kimi örneklerde bu aralık zayıflık ve hesaba katılmama olarak görünür. | هذا الشيء بين بين أي بين الجيد والرديء (sihah)
- B012 geri dönüşsüz boşanma | طلاق يقطع الرجعة | Evlilik bağında, geri dönüş hakkını kesen ve ayrılığı kesinleştiren boşanma türüdür. | تطليقة بائنة وهي فاعلة بمعنى مفعولة (sihah)
- B013 ayrılık uğursuzu kuş | علامة الفراق المشؤومة | Ayrılık getireceği veya ayrılığa işaret edeceği düşünülen belirli kuş kalıbıdır; kaynakta görünüşü için farklı tarifler de aktarılır. | غراب البين يقال هو الأبقع (sihah)

### س ك ن — 29:38 w7 مَّسَٰكِنِهِمْ
- B001 hareketin dinip durulması | ذهاب الحركة | Bir şeyin hareketi veya çalkantısı sona ererek durması, yerinde kalması ya da dinginleşmesidir. Susma ile rüzgarın, yağmurun ve öfkenin dinmesi bu değişimin belirli bağlamlardaki görünüşleridir. | خلاف الاضطراب والحركة
- B002 bir yere yerleşip orada yaşama | استيطان المنزل | Bir yere yerleşip orada yaşama ve o yeri yaşanan yer edinmedir. Aynı alan, yaşanan yerin kendisini, birini oraya yerleştirmeyi ve bir evi kira almadan kullanımına vermeyi de kapsar. | يسكنون الدار
- B003 ev halkı ve orada yaşayanlar | أهل الدار | Bir evde yaşayan kişiler, özellikle aynı evin halkı ve aile yükümlülüğü içinde bulunan kimselerdir. Daha genel çoğul kullanım, belirli bir yerde oturanların tümünü gösterebilir. | السكن الأهل الذين يسكنون الدار
- B004 insanı rahatlatıp içini yatıştıran dayanak | مأنس السكون | Kişinin yakınlık duyup yanında rahatladığı, içinin yatıştığı kişi veya şeydir. Gece, destekleyici yakarış ve yanında oturulan ateş bu rahatlatıcı işlevle adlandırılabilir. | كل ما سكنت إليه من محبوب
- B005 güven veren ağırbaşlı iç dinginlik | طمأنينة الوقار | Korku ve taşkınlığın yerini güvenin, ağırbaşlılığın ve yumuşak bir iç dinginliğinin almasıdır. Kalbe verilen güven ile topluluğu bir arada tutan sandık içeriği bu durumun özel anlatımlarıdır. | السكينة وهو الوقار
- B006 yoksulluk, güçsüzlük ve ezilmişlik | ذل المسكنة | Geçim araçlarından yoksun olma veya güçsüz, ezilmiş ve aşağı durumda bulunmadır. Bu durumdan hareketle kişinin boyun eğmesi ya da kendini aşağı koyması da aynı söz ailesinde anlatılır. | المسكنة مصدر فعل المسكين
- B007 kesici bıçak | إسكان الذبيحة بالسكين | Kesmekte kullanılan ağızlı bıçaktır. Kaynaklar adını, kesilen hayvanın hareketini ölümle sona erdirmesi üzerinden açıklar; aracı yapan kişi de ayrı bir türemiş adla gösterilir. | السكين معروف
- B008 geminin kıçındaki dengeleyici yöneltme aracı | تسكين السفينة بالسكان | Geminin kıçında bulunan, gemiyi dengede tutmaya, yöneltmeye ve çalkantısını azaltmaya yarayan bölüm veya araçtır. Adlandırma doğrudan bu dengeleme işlevine bağlıdır. | سكان السفينة سمى لأنه يسكنها عن الاضطراب
- B009 sabit yer ve konum bildiren özel kullanımlar | موضع الاستقرار | Sabit yer veya konum düşüncesine bağlı birkaç özel kullanımdır: başın boyuna oturduğu nokta, çoğul kalıplarda kişilerin yerleri, konumları, düzeyleri ya da alışılmış düzenleri ve belirli bir yer adı. Bunlar genel yerleşip yaşama eylemi değildir. | موضع من أرض الكوفة
- B010 yerinde kalmayı sağlayan geçimlik ve bol otlak | قوت يثبت المقام | İnsanın geçimini sürdürüp bulunduğu yerde kalmasını sağlayan yiyecek veya geçimliktir. Hayvancılık bağlamında, sürünün başka yere göç etmesini gerektirmeyecek kadar bol otlak aynı işlevle nitelenir. | الأسكان الأقوات واحدها سكن

### ز ي ن — 29:38 w8 وَزَيَّنَ
- B001 ayıptan uzak güzellik | حسن الشيء ونقاؤه من الشين | Bir şeyin, güzelliğin onda belirmesiyle ayıp ve çirkinliğin karşıtı sayılan güzel bir nitelik taşımasıdır; gerçek sayılan süs de kişiyi hiçbir durumda ayıplı kılmama ölçüsüyle sınırlandırılır. | الزين نقيض الشين (maqayis
- B002 güzelleştirme ve güzelliğini görünür kılma | إظهار الحسن وتحسين الشيء | Bir şeyin güzelliğini eylemle ya da sözle ortaya çıkarmak, onu gerçekten güzelleştirmek veya birine güzel görünür hale getirmektir; yerin bitkiyle canlanması ve göğün ışıklarla bezenmesi bunun doğal ve görsel örnekleridir. | أصل صحيح يدل على حسن الشيء وتحسينه (maqayis)
- B003 bezenmeye yarayan nitelik ve şeylerin bütünü | الزينة التي يتزين بها | Bir kişinin ya da şeyin bezenmesine yarayan niteliklerin ve unsurların ortak adıdır; içsel yetkinlikleri, bedensel üstünlükleri, dışsal varlık ve saygınlığı, ayrıca mal, eşya ve konum gibi dünyalık unsurları kapsayabilir. | الزينة جامع لكل ما يتزين به (ayn)

### ش ط ن — 29:38 w10 ٱلشَّيْطَٰنُ
- B001 uzaklaşma ve uzaklaştırma | البعد والانقطاع | Bir yerden, kişiden ya da başlangıç noktasından uzağa düşme veya uzaklaşma; ettirgen biçimde de bir şeyi uzaklaştırmadır. Evin, ayrılığın, seferin ve kuyu dibinin uzaklığı bu çekirdeğin belirli bağlamlardaki görünümleridir. | أصل مطرد صحيح يدل على البعد (maqayis)
- B002 uzun kuyu ipi ve onunla bağlama | الحبل الطويل والشد | Su çekmede kullanılan, uzun ve sıkı bükülmüş bir iptir; aynı dal, bir şeyi bu iple bağlama eylemini de kapsar. İki iple kovayı kuyudan çeken kişi bu araç ve iş düzeninin özel bir katılımcısıdır. | الشطن الحبل وهو القياس لأنه بعيد ما بين الطرفين (maqayis)
- B003 yönünden ayırma ve bağlama göre eğrilik ya da çetinlik | المخالفة والعوج والشدة | Birini niyet ettiği yönden ayırmak veya izlediği doğrultuya ters düşmektir. Yana yatıklık, kıvrımlı eğrilik ve çetinlik ise yalnız belirli varlıkları niteleyen bağımlı anlamlardır. | شطنه يشطنه شطنا إذا خالفه عن نية وجهه (sihah)
- B004 azgın ve başkaldıran kötü varlık | الشيطان العاتي المتمرد | İnsanlar, görünmez varlıklar veya hayvanlar arasında azgınca başkaldıran, iyilikten uzaklaşan ve kötülükte ileri giden varlığa verilen addır. Bir kişinin böyle bir varlık gibi davranması ve kötü bir huyun onunla adlandırılması bu çekirdeğe bağlı uzantılardır. | كل عات متمرد من الجن والإنس والدواب شيطان (maqayis
- B005 çirkin yılan ve bitki adıyla ürkütücü baş benzetmesi | القبيح المسمى شيطانا | Çirkin ya da ürkütücü görünüşlü belirli bir yılanın ve bir bitkinin kötü varlık adıyla anılmasıdır. Bitkinin başlarını böyle bir yılanın veya düşlenen azgın kötü varlığın başlarına benzetme de bu görünüşe dayalı adlandırmanın özel bir uzantısıdır. | الحية تسمى شيطانا (maqayis)

### ع م ل — 29:38 w11 أَعْمَٰلَهُمْ
- B001 bilerek yapılan iş veya eylem | الفعل المقصود والعمل | Canlı bir yapanın bilerek gerçekleştirdiği iş veya eylemdir; iyi ya da kötü davranışları da kapsayabilir. Kendisi için çalışmak ya da işe yoğun biçimde girişmek bu çekirdeğin özel kullanımıdır. | أصل واحد صحيح وهو عام في كل فعل يفعل (maqayis)
- B002 işe koşmak veya kullanmak | إعمال الشيء واستعماله | Bir kişiyi, nesneyi, düşünce gücünü ya da aracı işe koşmak ve ondan yararlanmaktır; bazen birinden iş yapmasını istemeyi de kapsar. Anlam, kullanma ve çalıştırma yapılarında kalır. | يستعمل غيره ويعمل رأيه أو كلامه أو رمحه
- B003 işe görevli kılma veya görev üstlenme | ولاية العمل والقيام عليه | Bir kimseye belirli veya resmi bir iş üzerinde görev ve yetki verilmesi ya da onun bu işi yürütmesidir. Bağış toplama görevlileri bu anlamın özel bir alanıdır. | العاملين عليها هم السعاة الذين يأخذون الصدقات (tahdhib)
- B004 iş ücreti | أجر العمل ورزق العامل | Bir işin karşılığında çalışana verilen ücret, pay veya geçimliktir. Bu anlam işin kendisi ya da işi yapan kişilerin topluluğu değildir. | العمالة أجر ما عمل (maqayis)
- B005 karşılıklı işlem | المعاملة بين الناس | İki kişi arasında alışverişte veya benzeri işlerde karşılıklı işlem yürütmektir. Tek taraflı iş yapma ya da iş karşılığı ücret alma anlamı taşımaz. | المعاملة مصدر من قولك عاملته وأنا أعامله معاملة (maqayis)
- B006 el işçileri | العملة العاملون بالأيدي | El emeğiyle kazı, kuyu kaplama, çamur işi ve benzeri işleri yapan işçi topluluğudur. Anlam, ücret veya yalnızca yapılan iş değil, işi yapan insan grubudur. | العملة القوم يعملون بأيديهم ضروبا من العمل حفرا أو طيا أو نحوه (maqayis)
- B007 zahmete girmek | التعمل بمعنى التعني | Belirli anlatımlarda bir iş veya ihtiyaç için zahmete girme, kendini yorma anlamıdır. Bu kol genel çalışma ya da kendisi için iş yapma anlamına taşınmaz. | لا تتعمل في أمرك ذا كقولك لا تتعن (tahdhib)
- B008 işe yatkın ve dayanıklı | المطبوع على العمل | İşe yatkın veya çalışmaya yaratılıştan elverişli olma niteliğidir. İnsan için çalışkan yaradılış, deve için üstün ve işe dayanıklı dişi deve adı olarak görülür. | اليعملة من الإبل اسم لها اشتق من العمل (maqayis)
- B009 mızrak ucunun alt bölümü | عامل الرمح | Mızrağın sivri ucuna en yakın ön gövde bölümüdür; sivri uçtan ve uç dibindeki ayrı parçadan ayrılır. Anlam, mızrağın kullanılması değil mızraktaki konumdur. | عامل الرمح وعاملته وهو ما دون الثعلب قليلا مما يلي السنان وهو صدره (maqayis)
- B010 iş gören beden parçası | الجارحة العاملة | Belirli tamlamalarda bedenin iş gören parçasına verilen addır: hayvan için ayaklar, bir örnekte uzağı gören göz. Bunlar çıplak bir genel organ adı olarak genelleştirilemez. | عوامل الدابة قوائمه واحدها عاملة (tahdhib)
- B011 işlek yol | الطريق المعمل | Yürünerek belirginleşmiş, işlek ve açık yol anlamındaki kalıplı yol niteliğidir. Genel çalışma ya da işçi anlamı taşımaz. | طريق معمل أي لحب مسلوك (sihah)
- B012 yaya yolcular | بنو العمل من المشاة | Yolculukta binek kullanmadan yürüyen yolcuları adlandıran kalıplı topluluk ifadesidir. El işçileri ya da yolun kendisi anlamına gelmez. | المسافرون إذا مشوا على أرجلهم يسمون بني العمل (tahdhib)

### ص د د — 29:38 w12 فَصَدَّهُمْ
- B001 yüz çevirme ve alıkoyma | إعراض وصرف | Bir kimsenin bir şeyden yüz çevirerek uzaklaşması ya da bir başkasını bir işten alıkoyup ondan uzaklaştırmasıdır. | الصَّدّ الإعراض
- B002 vadinin iki yanı | جانبان مائلان | Bir vadi, yar veya dağın karşılıklı iki yanı ya da yamacıdır; bir kaynakta ayrıca birbirine karşı duran iki dağ biçiminde açıklanır. | الصَّدان جانبا الوادي
- B003 karşıda ve yakında bulunma | مقابلة وقرب | Bir şeyin karşısında veya yakınında bulunma durumudur; kişi yönelimli yapıda ise birinin karşısına çıkmayı, ona yönelmeyi ya da yaklaşmayı anlatır. | الصدد ما استقبل
- B004 suya giden yol | طريق إلى الماء | Bir su kaynağına ulaşan veya insanı doğrudan suya götüren yoldur. | الصَّداد الطريق إلى الماء (maqayis
- B005 engel oluşturan dağ | جبل حاجز | Bir dağ ya da dağın görüşü, yolu veya geçişi keserek araya giren bölümüdür. | الصَّدّ الجبل (maqayis
- B006 yaygara koparmak | ضجيج وجلبة | Yüksek, karışık ve topluca duyulan bir gürültü ya da yaygara çıkarmaktır; bazı kaynak bağlamlarında bu gürültü şiddetli gülme olarak yorumlanır. | صد يصد وذلك إذا ضج (maqayis)
- B007 kanlı irinli yara akıntısı | صديد الجرح | Yarada oluşan, kanla karışmış irinli veya ince akıntıdır. Özel anlatıda cehennem ehlinin kan ve irinli akıntısından oluşan içeceğe, bir yorumda ise kaynatılıp koyulaşmış sıvıya uygulanır. | الصديد الدم المختلط بالقيح
- B008 türü tartışmalı küçük hayvan | دويبة صغيرة | Kaynaklara göre ya sıçan benzeri küçük bir kara hayvanı ya da benekli kertenkele türünden bir hayvandır; kesin tür kimliği ortak değildir. | الصَّداد ضرب من الجرذان ويقال من دواب الأرض (ayn)
- B009 bir kadın adı | اسم امرأة | Kaynaklarda iki yazım görünümüyle aktarılan belirli bir kadın adıdır. | صد صد اسم امرأة (ayn)
- B010 tatlı sulu bir kuyunun adı | ماء مسمى | Bilinen bir suyun veya tatlı suyu olan belirli bir kuyunun özel adıdır. | صداء ماء معروف (jamhara)
- B011 alkışlamak | تصفيق | Elleri birbirine vurarak alkışlama eylemidir. | صدى يصدي تصدية إذا صفق
- B012 kadın örtüsü | ستر المرأة | Bir kadının bedenini veya görünmesini örtmek için kullandığı örtüdür. | الصَّداد ما اصطدت به المرأة وهو الستر (tahdhib)
- B013 aynada hazırlanmış göz boyası | كحل المرآة | Bir aynanın yüzeyine sürtülerek hazırlanan ve sonra gözün boyanmasında kullanılan maddedir. | الصُّدود ما دلكته على مرآة ثم كحلت به عينا (tahdhib)

### س ب ل — 29:38 w14 ٱلسَّبِيلِ
- B001 yol ve bir amaca ulaştıran yol | طريق ممتد يسلك | Üzerinde gidilen, uzanmış yol; ayrıca bir amaca erişmeyi sağlayan bağlantı, yöntem veya çıkış yoludur. Dinsel doğruluk ve iyiliğe yönelten yol anlamı yalnız ilgili söz öbeğinde belirginleşir. | السبيل وهو الطريق سمي بذلك لامتداده (maqayis)
- B002 yol kullanan kişi veya yolcu | أهل الطريق وسالكوه | Bir gereksinim için yollarda gidip gelen veya bir yolu izleyen kişi; belirli bir söz öbeğinde ise evinden uzaktaki ya da dönüş olanağı kesilmiş yolcudur. | السابلة المختلفة في السبل جائية وذاهبة (maqayis)
- B003 malı sürekli iyilik kullanımına ayırmak | مال مجعول في طريق البر | Bir malı ya da taşınmazı, kendisi veya geliri sürekli iyilik işlerinde kullanılmak üzere ayırmaktır. Ayrı bir söz öbeği, gerekli yolculuk giderini bulamayan savaş görevlisine ayrılan yardım payını belirtir. | سبلت مالا في سبيل الله أي وقفته (ayn)
- B004 aşağı doğru salmak | إرخاء من علو إلى سفل | Bir şeyi yukarıdaki konumundan aşağı doğru gevşeterek bırakmak, uzatmak veya akıtmaktır. Perde, giysi ve kuyrukta sarkıtma; bulut, yağmur ve gözyaşında aşağı akışa bırakma biçiminde gerçekleşir. | إرسال شيء من علو إلى سفل
- B005 yağan yağmur | مطر سابل بين السحاب والأرض | Yağmur, özellikle buluttan yere doğru düşmekte olan ve kimi kullanımlarda bol ya da geniş bir sağanak olarak nitelenen yağıştır. | السبل المطر الجود (maqayis)
- B006 üst dudak ve sakal önündeki sarkan kıl | شعر منسدل عند الفم واللحية | Üst dudakta bulunan bıyık kılı; bazı kullanımlarda bıyıktan sakala karışan bölüm, sakalın önü veya göğse doğru sarkan sakal kısmıdır. Uzunluğu ve belirli görünüş ya da tehdit davranışları ayrıca söz öbeklerinde anlatılır. | سبال الإنسان من هذا لأنه شعر منسدل (maqayis)
- B007 kap kenarı veya hayvanın boğaz kesim yeri | حافة أو مخرج متقدم | Belirli yapılarda kovanın dudakları ya da kabın dolum sınırı olan üst kenarıdır; başka bir yapıda büyükbaş hayvanın boğazındaki kesim noktası ve çevresidir. | لأعالي الدلو أسبال (maqayis)
- B008 tahıl başağı ve başak çıkarmak | سنبلة الزرع الممتدة | Tahıl bitkisinin taneleri taşıyan uzamış başağıdır; ayrıca bitkinin başak çıkarması veya başaklı duruma gelmesi sürecini belirtir. | سمي السنبل سنبلا لامتداده
- B009 eski pay oyunundaki beşinci veya altıncı çubuk | قدح الميسر المسمى المسبل | Payların ok ya da çubuklarla belirlendiği eski bir şans oyunundaki belirli çubuktur; kaynaklara göre beşinci veya altıncı sıradadır ve altıncı sayıldığında altı pay taşır. | المسبل اسم خامس سهام القداح (ayn)
- B010 kırmızı damarlı ağsı göz perdesi | غشاوة في العين تشبه النسج | Gözde, örümcek ağına benzeyen bir perde oluşturan ve kırmızı damarlarla belirginleşen bir hastalıktır. | السبل داء في العين شبه غشاوة كأنها نسج العنكبوت بعروق حمر (sihah)

### ك و ن — 29:38 w15 وَكَانُوا۟
- B001 gerçekleşme, bulunma ve olma bildirimi | وقوع الشيء وحضوره في زمان | Bu dal, bir şeyin gerçekleşip bulunur hale gelmesini ve bu olmanın geçmiş ya da şimdiki anda bildirilmesini anlatır. Olma adları, pekiştirme ya da ayırma işlevli bağlı sözler ve bir şeyi oldurup oluşmasını sağlama buna bağlıdır. | الكون الحدث يكون بين الناس ومصدر من كان يكون
- B002 bulunma yeri ve konum değeri | المكان والمكانة من الكون | Bu dal, olma kökünden türetilmiş sayılan bulunulan yeri, durulan noktayı ve kişinin başkası yanındaki konum değerini kapsar. Bazı türevlerde baştaki m sesi kökten sanıldığı için yerleşmiş biçimler ortaya çıkar. | المكان اشتقاقه من كان يكون
- B003 birini güvenceyle üstlenme | الكفالة والقيام على فلان | Bu dal, bir kişi için sorumluluğu üzerine almayı ve onun adına güvence vermeyi anlatır. Ad biçimi ve bağlı sözler aynı üstlenme çekirdeğini paylaşır. | الكيانة الكفالة
- B004 boyun eğme | الخضوع بالاستكانة | Bu dal, boyun eğme ve direnç göstermeden alçalma durumunu bildirir. | الاستكانة الخضوع (sihah)
- B005 gençliğini anan yaşlı kişi | الشيخ المنسوب إلى كُنْتُ | Bu dal, yaşlanan kişiye gençliğinde nasıl olduğunu anlatmasına bağlanarak verilen nitelemeyi bildirir. | يقال للرجل إذا شاخ كُنْتِيّ
- B006 kötü durumda gece geçirme | حالة السوء بكينة | Bu dal, belirli deyiş içinde bir kişinin geceyi kötü bir durum içinde geçirmesini bildirir. Kullanılan durum adı olma kökünden kurulmuş sayılır. | الكينة في قولهم بات فلان بكينة سوء أي بحال سوء فأصله الكون فعلة من الكون (maqayis)

### ب ص ر — 29:38 w16 مُسْتَبْصِرِينَ
- B001 gözle görme | إبصار العين | Gözle görme alanı: görme duyusu, bakan göz organı, bir şeyi gözle görmek ve gözün görmeye açılması. Dikkatle dikilerek bakma veya yavrunun gözünün açılması gibi kullanımlar bu çekirdeğe bağlı özel gerçekleşmelerdir. | أبصرته إذا رأيته (maqayis)
- B002 iç kavrayış | بصيرة القلب | Kalbin veya zihnin bir şeyi bilip kavraması, doğruluğa ermesi ve bunun delil, ibret ya da açıklayıcı kanıt olarak görünmesi. Din veya belirli bir iş konusunda bilinçli hale gelme bu çekirdeğe bağlı özel kullanımdır. | أحدهما العلم بالشيء وبصرت بالشيء إذا صرت به بصيرا عالما والبصيرة البرهان (maqayis)
- B003 aydınlatıcı açıklık | آية مبصرة | Bir şeyin aydınlık, açık veya açıklayıcı olup görmeyi ya da anlamayı mümkün kılması. Bu alan, işaretin insanları görür veya kavrar hale getirmesiyle tanımlanır. | المبصرة المضيئة تبصرهم أي تجعلهم بصراء والمبصرة بالفتح الحجة (sihah)
- B004 kan izi | بصيرة الدم | Yere veya bedene düşen kan parçası, kan lekesi ya da kan izi; bağlama göre bu izden hareketle kan bedeli veya öç konusu da anılır. Çekirdek, somut kan kalıntısı ve onun izleyici işaret oluşudur. | البصيرة القطعة من الدم إذا وقعت بالأرض استدارت (maqayis
- B005 koruyucu savaş gereci | بصيرة السلاح | Savaşta korunmak için kullanılan kalkan, zırh veya giyilen koruyucu silah donanımı. Parlaklık ya da şiirsel tanıklık, nesnenin kendisine bağlı ayrıntıdır. | البصيرة الترس فيما يقال (maqayis)
- B006 kalın kenar ve ek yeri | غلظ الحافة ووصل الشقتين | Bir şeyin kalın dış yanı, kenarı veya yüzeyi ve iki deri, kumaş ya da kap parçasını bir araya getirip dikilen ara bölüm. Dal, kalın kenar fikri ile parçaları ek yerinden birleştirme fikrini aynı maddi yüzey alanında tutar. | بصر الشيء غلظه والبصر هو أن يضم أديم إلى أديم يخاطان والبصيرة ما بين شقتي البيت (maqayis)
- B007 yumuşak parlak taş | حجارة بصرة رخوة | Yumuşak, parlak veya beyazımsı taşlar ve böyle taşları bulunan yer. Bu yer adından hareketle oraya gitme kullanımı çekirdeğe bağlı bir yönelme kullanımıdır. | البصرة الحجارة الرخوة وبصر بكسر الباء من الأصل الثاني (maqayis)



===== branches.md =====
# branches.md — the dictionary lines of the branches the findings cite (focus roots: dictionary.md)

- ء ج ر B001 iş veya anlaşma karşılığında sağlanan yarar | جزاء العمل والكراء | Bir işin yapılması veya bir anlaşmanın kurulması nedeniyle kişiye dönen yararlı karşılıktır; bu karşılık dünyalık bir ödeme ya da manevi ve öte dünyaya ilişkin bir ödül olabilir. Kiralama bedeli, ücretle çalıştırma ve evlilikte kadına verilen bedel bu çekirdeğin belirli ilişkilere bağlı gerçekleşmeleridir. | الأجر جزاء العمل (maqayis
- ء ر ض B010 odun yiyen küçük canlı | الأَرَضَة آكلة الخشب | Odun yiyen küçük bir canlıyı belirtir. İlgili eylem yapısı, bu canlının bir odunu yiyip zarar görmüş hale getirmesini anlatır. | الأرضة دويبة بيضاء تشبه النمل تأكل الخشب (ayn)
- ء ه ل B001 yakın çevre ve bağlı topluluk | جماعة القرب والانتماء | Bir kişiye, eve, dine, soya, işe, beldeye ya da ortak yaşama alanına yakınlık ve aidiyet bağıyla bağlı olan insan çevresidir. Eş ve en yakın kişiler çekirdekte durur; ev sakinleri ve ortak bağla birleşen topluluklar bu çekirdeğin genişlemeleridir. | أهل الرجل زوجه وأخص الناس به
- ء ي ي B003 gorunen belirti | علامة ظاهرة | Gorunen bir belirti veya isaret; bazi kalipli kullanimlarda kisinin sahsi, toplulugun butunu, kitapta harflerden olusan parca ya da gunesin isigi icin de kullanilir. | الآية العلامة
- ب ي ت B001 barınak mesken | المأوى والمسكن | Gece konaklanan, insana veya başka bir varlığa sığınak olan ve sakinlerini bir araya getiren mesken ya da barınak. | أصل واحد وهو المأوى والمآب ومجمع الشمل (maqayis)
- ب ي ت B004 geceleyin yapmak | عمل الليل وتدبيره | Bir işi gece yapmak, geceleyin tasarlayıp düzenlemek veya bir topluluğa gece gelip baskın yapmak. | بيت الأمر إذا دبره ليلا (maqayis
- ت ر ك B002 geride iz birakma | إبقاء الأثر بعد الترك | Bir kisinin ardinda iyi anilma gibi bir izin korunmasi veya seylerin sahiplerinden sonra geride kalmasi. | الترك الإبقاء وتركنا عليه أي أبقينا عليه ذكرا حسنا (tahdhib)
- ج ث م B001 yere çöküp bulunduğu yerde kalma | اللصوق بالأرض ولزوم المكان | Bir canlının yere göğsünü verip çökerek bulunduğu yere yapışmışçasına orada kalmasıdır. Aynı kalıcılık görüntüsü, midede ağırlaşan bal ve büyüyüp yerinde kalan salkımlar için aktarılır; çökmenin gerçekleştiği yer de konak ya da yuva olarak adlandırılabilir. | جثم يجثم جثوما أي لزم مكانا لا يبرح (ayn)
- ج ث م B002 bağlanıp atış hedefi yapılarak öldürülen hayvan | المجثمة المصبورة | Bir hayvanın bağlanarak veya tutulup kaçması engellenerek atış hedefi yapılması ve vurularak öldürülmesidir. Adlandırma özellikle kuş, tavşan ve benzerleri içindir; koyuna uygulanması aktarılmış bir kullanımdır. | نهي عن المجثمة وهي المصبورة (ayn
- ج ث م B005 çok uyuyan, tembel ve evinden ayrılmayan adam | الجثامة للنؤوم أو اللبد | Çok uyuyan, tembel davranan, yolculuğa çıkmayan veya evinden ayrılmayan adam için kullanılan nitelemedir. Ayrı bir kaynak varyantında ağırbaşlı ve yumuşak huylu bir önderi de niteler. | الجثامة الرجل البليد والسيد الحيلم (ayn)
- ج د ل B001 sıkıca bükme ve sağlam örgü | الفَتْل المحكم | Bir ipi ya da benzeri parçaları sıkıca bükerek sağlamlaştırmak ve bu sıkı büküm veya örgü sonucunda dayanıklı bir bağ ya da dokuma elde etmektir. | استحكام الشيء (maqayis)
- ج و ب B005 giysi, zırh veya kalkan; giysiyi üstüne geçirme | الجَوْب لباسا وترسا | Kadının giydiği zırh veya giysi, kesilmiş bir üstlük ya da savunmada kullanılan kalkan için kullanılan ad. Buna bağlı eylem, bir giysiyi bedene geçirip giymektir. | الجوب درع تلبسه المرأة وهو مجوب (maqayis)
- ح ص ب B001 çakıl taşı, çakıllı zemin ve çakılla döşeme | الحَصْباء والحصى | Küçük ya da büyük çakıl taşları ve bunların oluşturduğu taş malzemesidir; bağlı kullanımlarda çakıllı araziyi ve bir yerin bu taşlarla döşenmesini de belirtir. | الحَصْباء جنس من الحصى (maqayis)
- ح ص ب B002 çakıl atma, karşılıklı taşlama ve atın koşuda çakıl kaldırması | الرمي بالحصباء | Verilen yapılarda bir insana ya da yere küçük çakıl taşları atmayı, insanların birbirine çakıl fırlatmasını veya koşan bir atın yerdeki çakılları havalandırmasını anlatır. | حصبت الرجل بالحصباء (maqayis)
- ح ص ب B003 toz taşıyıp çakıl kaldıran sert rüzgar; ince dolu ve kar serpintisi | الريح الحاصب | Rüzgarla kullanılan biçim, toz taşıyan veya yüzeydeki çakılları kaldıracak kadar sert esintiyi belirtir; ayrı biçim ise saçılan ince dolu ve kar parçacıklarını anlatır. | ريح حاصب إذا أتت بالغبار (maqayis)
- ح ي ي B001 canlı olma, sürüp gitme ve canlandırma | الحياة في مقابل الموت | Ölümün karşıtı olarak canlı olma ve canlı kalma durumudur; bir varlığı canlı kılma ya da yeniden canlandırma işlemini de kapsar. Bitkisel, duyusal ve düşünsel yaşam ile dünyadaki, sonraki ve ölmez var oluş bu çekirdeğin farklı gerçekleşmeleridir. | خلاف الموت (maqayis)
- خ س ف B004 kuyuda derin ve sürekli su kaynağına ulaşma | غؤور البئر ومائها | Kuyu kazısında kaya katmanını delerek derindeki sürekli su kaynağına ulaşma ve böylece bir su çıkışı açma durumudur. Çoğu aktarım bol ve tükenmeyen suyu bildirirken bir aktarım aynı kuyu nitelemesini suyun kaybolup tükenmesi için kullanır. | بئر خسيف إذا كسر جيلها فانهار ولم ينتزح ماؤها (maqayis)
- د و ر B002 yerleşilen yer ve yurt | الدار والموضع المحيط بأهله | İnsanların yerleştiği yapı, çevrili alan veya daha geniş yurt ve bölgedir. Anlam, orada yaşayan topluluğa ve belirli yaşam ya da son durak alanlarını adlandıran yapılara da aktarılabilir. | الدار القبيلة
- ذ ن ب B007 kova; özellikle büyük, dolu veya kuyruk ipli olanı | الذنوب دلو ممتلئ | Kuyu veya su için kullanılan kova; kaynaklara göre özellikle büyük, suyla dolu ya da kuyruk benzeri çekme ipi bulunan kova olabilir. | الذنوب الدلو (jamhara)
- ر ج ز B001 sarsıntılı ve art arda süren hareket | الاضطراب وتتابع الحركة | Düzensiz, sarsıntılı veya art arda süren hareketi anlatır; özellikle devenin arka kısmı ya da uylukları etkilenince kalkışta veya yürüyüşte titremesi ve adımlarının sıklaşması bu kapsamdadır. Aynı hareket örüntüsü, belirli kullanımlarda gök gürültüsünün yinelenen sesine, su yüklü bulutun ağır ilerleyişine ve rüzgârın sürekli esmesine aktarılır. | أصل يدل على اضطراب (maqayis)
- ر ج ف B001 şiddetle sarsılıp çalkalanmak | اضطراب شديد | Bir şeyin yerinde duramayacak ölçüde şiddetle sarsılması ya da çalkalanmasıdır. Yürek söz konusu olduğunda korkunun doğurduğu çarpıp titremeyi, denizde dalgalı çalkantıyı, gök gürültüsünde ise sesin gökte ya da bulutta yinelenmesini anlatır. | أصل يدل على اضطراب (maqayis)
- ر ج ل B003 yaya giden kişi | المشي على الأرجل | Bir taşıta veya bineğe binmeden kendi bacaklarıyla yürüyen kişi ya da böyle kişiler topluluğudur. Özel yapılarda yürümeye dayanıklılığı, bineğinden inerek yaya olmayı ve yürünmesi güç taşlık araziyi de anlatır. | الرجل الرجالة (maqayis)
- س ب ق B004 yakalanmaktan kurtulacak kadar öne kaçma | الفوت عن الطالب | Aranan ya da takip edilen tarafın takip edenin erişimini aşarak yakalanmadan kurtulmasını anlatır. Olumsuz biçimlerde, böyle bir kaçışın ve takip edeni aciz bırakmanın mümkün olmadığını bildirir. | وما نحن بمسبوقين أي لا يفوتوننا
- س م و B004 üstteki gök veya örtü ve buna bağlı üstten gelen ya da üstte bulunan şeyler | السماء وما علا فأظل | Bir şeyin üzerinde bulunan ve onu örten gök, tavan ya da genel üst yandır. Bu ad buluta, yukarıdan gelen yağmura, yağmurla çıkan veya yükselen bitkiye ve atın sırtına da aktarılır. | العرب تسمى السحاب سماء والمطر سماء
- ص ب ح B010 bir duruma gelmek | أصبح بمعنى صار | Bir kişinin veya şeyin belirli bir nitelik ya da duruma geçmesi, o hale gelmesi. Fiil adı da bu duruma geçme eylemini adlandırır. | الإصباح مصدر أصبح إصباحا مثل قولهم أمسى إمساء (jamhara)
- ص ن ع B004 özenilmiş iyi görünüş sergileme | تصنع السمت والزينة | İyi bir duruşu, davranışı veya süslü görünüşü çabayla oluşturup dışarıya sergilemektir. Bu sergileme doğal olmayabilir ve iç durumla uyuşmayabilir. | التصنع حسن السمت (maqayis)
- ص ن ع B006 su tutakları ve büyük yapılar | المصانع أحواض وأبنية | Suyu toplamak, tutmak veya sulamaya vermek için yapılmış kuyu, havuz ve benzeri düzeneklerdir. Aynı ad kaleler, saraylar, köyler ve seçkin büyük yapılar için de genişletilmiştir. | المصانع ما يصنع من بئر وغيرها للسقى (maqayis)
- ص ي ح B002 çığlığa bağlı ceza, korku, baskın, ağıt ve ani kötülük kullanımları | الصيحة المفزعة | Bir çığlığın etkisi üzerinden ceza veya korkuyu adlandıran aktarılmış kullanımları kapsar; buna bağlı olarak baskın alarmı, ağıt çığlığı ve sahibini ansızın bulan kötülüğü anlatan özel kullanımlar da bu dalda yer alır. | الصيحة العذاب وصيحة الغارة والصائحة صيحة المناحة ومثل صيحة الحبلى أي سوء يعاجلهم (ayn)
- ع ث و B001 bozup düzenini çürütmek | الفساد في الأرض | Bir şeyi iyi ve düzenli durumundan çıkaracak biçimde bozmak, çürütmek veya düzenini yıkmaktır. Bu bozma kimi kullanımda ağır bir dereceye ulaşır, kimi kullanımda ise özellikle yeryüzündeki düzeni hedef alır. | كلمة تدل على فساد
- ع ج ز B002 takipten sıyrılıp erişilemez olma | فوت وسبق وإفلات من الطلب | Takip edilenin uzaklaşıp öne geçmesi yüzünden arayanın ona yetişememesi veya onu ele geçirememesi. Bazı biçimlerde yarışma, karşı koyma ya da kaçabileceğini sanma anlatılır; belirli bir söz öbeğinde ise güvenilen bir yere yönelme anlamı bulunur. | أعجزني فلان إذا عجزت عن طلبه وإدراكه (maqayis
- ع د د B004 kaynağı kesilmeyen kalıcı su ve su yeri | الماء العد | Doğal olarak birikmiş, eski veya besleyici kaynağı kesilmediği için çekmekle tükenmeyen sürekli su ve bu suyun bulunduğu kalıcı su yeridir. | العد مجتمع الماء وجمعه أعداد (maqayis
- ع د د B005 belirli zaman ve bilinen aralıklarla geri gelme | عداد الوقت ومعاودته | Bir şeyin belirli zamanı veya dönemi ile belli aralıklarda yeniden ortaya çıkmasıdır. Zehir ağrısının alevlenmesi bunun özel gerçekleşmesiyken yayın sesi ve titreşimi ile dağıtım ya da toplanma günü kalıba bağlı ilişkili kullanımlardır. | العداد اهتياج وجع اللديغ (maqayis
- ع ذ ب B001 tatlı ve kolay tüketilen yiyecek ya da içecek | العذوبة والطيب في الماء والمطعوم | Su başta olmak üzere bir yiyecek veya içeceğin tatlı, hoş ve kolay tüketilir olması; su için ayrıca tuzlu olmama niteliğini taşır. Bu niteliğe bağlı yapılar tatlı su edinmeyi, aramayı ya da bir şeyi tatlı saymayı anlatabilir. | عذب الماء عذوبة فهو عذب طيب (maqayis
- ع ق ل B002 devenin ön ayağını büküp bağlayarak tutma | عَقْل البعير بالعِقال | Devenin ön ayağının alt bölümünü üst bölüme doğru büküp ip veya bağla tutturma işlemidir; bu işte kullanılan bağın kendisini de kapsar. Saçı tarayıp toplama, benzer tutma düzenine dayanan özel bir uzantıdır. | عقلت البعير أعقله عقلا إذا شددت يده بعقاله وهو الرباط (maqayis)
- ع ن ك ب B001 örümcek | العنكبوت الدويبة الناسجة | İnce ve gevşek bir ağı havada, kuyu ağzında veya başka yerlerde ören küçük canlıyı belirtir. Bölgesel, çoğul ve küçültme biçimleri bu çekirdeğe bağlıdır; canlının evi sayılan ağın sıcağa ve soğuğa karşı koruma sağlamaması ise yapıya özgü bir kullanımdır. | العنكبوت بلغة أهل اليمن العنكبوه والعنكباه والجمع العناكب وهي دويبة تنسج نسجا بين الهواء وعلى رأس البئر وغيرها رقيقا متهلهلا (ayn)
- غ ب ر B001 geride kalma ve kalan son bölüm | بقاء البقية بعد مضي ما معها | Birlikte bulunanların bir bölümü geçip gittikten sonra geride kalmak veya onlardan arta kalan bölüm olmaktır. Bazı özel kullanımlarda bu son bölümün elde edilmesi de anlatılır. | غبر إذا بقي وتغبرت المرأة الشيخ أخذت بقية مائه (maqayis)
- غ ب ر B004 toz ve toz renkli görünüm | الغبار والغبرة وما صار بلون التراب | Havaya kalkmış ince toprak, onun bir yüzeye bulaşması ve oluşturduğu boz renkli görünümdür. Bu renk veya görünüş, yeryüzünün, bazı bitki, meyve ve içeceklerin, ağaçlı arazinin ve silinmiş bir ayak izinin adlandırılmasına da temel olur. | الغبار سمي لغبرته وهي لونه والأغبر كل لون لون غبار والغبراء الأرض والغبيراء نبيذ الذرة ولعل في لونه غبرة (maqayis)
- ق ر ي B012 mızrak ucunun sivri tepesi ve keskin kenar | طرف حاد كقارية السنان | Özellikle mızrak ucunun en üstteki sivri ve keskin bölümü, genişlemiş kullanımda ise kılıç veya başka bir nesnenin kesen kenarı ya da keskin ucudur. | مما شذ عن هذا الباب القارية طرف السنان
- ق ط ع B023 yol kesmek | قطع الطريق بالغصب والصد | Yoldan geçenlere saldırıp mal almak, onları geçişten alıkoymak veya insanların yolu kullanmasını engellemek anlamıdır. | قطاع الطرق الذين يعارضون أبناء السبيل فيقطعون بهم الطريق (tahdhib)
- ق ل ب B007 kaplanmamış kuyu | القليب البئر | Asıl çekirdeği, iç duvarı henüz örülmemiş veya kaplanmamış kuyudur. Bazı aktarımda kuyu ya da su kuyusu genel adı olarak da kullanılır. | القليب البئر قبل أن تطوى (maqayis
- ك ب ر B006 ululuk ve kendini üstün görme | العظمة والكبرياء | Ululuk ve üstünlük niteliği ya da kişinin kendisini başkalarından üstün görerek büyüklük taslaması ve boyun eğmemesidir. | الكبر العظمة وكذلك الكبرياء (maqayis)
- ك ف ر B001 örtmek, kapatmak | ستر وتغطية | Bir şeyi başka bir şeyle örterek görünmesini engellemek veya kapalı duruma getirmektir. Zırhın giysiyle, kişinin silahla ya da külün savrulan toprakla örtülmesi bu işlemin özel gerçekleşmeleridir. | الستر والتغطية (maqayis)
- ن ز ل B002 Tanrısal iyilik, ceza veya bildiriyi insanlara ulaştırma | إنزال الشيء وإيصاله | Tanrı'nın iyilikleri, cezaları, esirgemeyi veya bir bildiriyi insanlara ulaştırmasıdır; ulaştırma doğrudan şeyin kendisiyle ya da onu doğuran nedenlerin verilmesiyle gerçekleşebilir. Bildiri bölüm bölüm ve yinelenerek gelebilir. | تنزلت الرحمة عليهم (tahdhib)
- و ل ي B003 bir işi üstlenip yönetme | تولي الأمر والقيام عليه | Bir işin, yerin veya başkasına ait durumun sorumluluğunu üstlenip onu yönetmek ve yürütmektir. Bu, resmi yönetimden bakım ve gözetim sorumluluğuna kadar uzanır. | الولاية مصدر الوالي (ayn)
- و ل ي B004 yakın durup destek olma | محبة ونصرة وموالاة | Bir kişi veya topluluğa sevgi, dostluk, inanç ya da yardım bağıyla yakın durup onun yanında yer almaktır. Karşıtlık ekseninde düşmanın değil desteklenen tarafın yanında olma anlamı taşır. | المولى الحليف والولي
- و ه ن B001 gücün veya kararlılığın azalması ya da azaltılması | ضعف القوة وفتور العزم | Bir şeyin, bedenin, kemiğin, işin ya da durumun taşıdığı gücün azalması; insan bağlamında çaba ve kararlılığın gevşemesi veya geçişli kullanımda bir başkasının ya da bir düzenin gücünün azaltılmasıdır. | وهن الشيء يهن وهنا: ضعف، وأوهنته أنا (maqayis)


===== concordance.md =====
# concordance.md — every use of the focus roots of 29:38 (roots with at most 60 uses; stop lemmas left out)

Each use: its word id S:A:W, its form, and its clause in the exact verifier spelling; the word ID identifies the focus. Larger roots: counts per lemma.

## ع و د — 63 uses; here 29:38:1; lemmas: عَاد2 24; عَادَ 18; أُعِيدُ 18; عِيد 1; مَعَاد 1; عَآئِدُون 1

## ب ي ن — 523 uses; here 29:38:4; lemmas: بَيْن 266; مُّبِين 119; بَيِّنَة 71; بَيَّنُ 35; تَبَيَّنَ 18; بَيَان 3; مُّبَيِّنَة 3; مُّبَيِّنَٰت 3; تَسْتَبِينَ 1; تِبْيَٰن 1; بَيِّن 1; مُسْتَبِين 1; يُبِينُ 1

## س ك ن — 69 uses; here 29:38:7; lemmas: مِسْكِين 23; سَكَنَ 15; مَسْكَن 12; سَكِينَة 6; أَسْكَن 5; سَكَن 3; مَسْكَنَة 2; سِكِّين 1; مَسْكُونَة 1; سَاكِن 1

## ز ي ن — 46 uses; here 29:38:8; lemmas: زَيَّنَ 26; زِينَة 19; ٱزَّيَّنَتْ 1
### زَيَّنَ
- 2:212:1 [زَيَّنَ V II PERF PASS] زُيِّنَ لِلَّذِينَ كَفَرُوا۟ ٱلْحَيَوٰةُ ٱلدُّنْيَا وَيَسْخَرُونَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ ۘ وَٱلَّذِينَ ٱتَّقَوْا۟ …
- 3:14:1 [زَيَّنَ V II PERF PASS] زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ مِنَ ٱلنِّسَآءِ وَٱلْبَنِينَ وَٱلْقَنَٰطِيرِ ٱلْمُقَنطَرَةِ مِنَ ٱلذَّهَبِ …
- 6:43:9 [زَيَّنَ V II PERF] فَلَوْلَآ إِذْ جَآءَهُم بَأْسُنَا تَضَرَّعُوا۟ وَلَٰكِن قَسَتْ قُلُوبُهُمْ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ مَا كَانُوا۟ يَعْمَلُونَ
- 6:108:14 [زَيَّنَ V II PERF] … يَدْعُونَ مِن دُونِ ٱللَّهِ فَيَسُبُّوا۟ ٱللَّهَ عَدْوًۢا بِغَيْرِ عِلْمٍۢ ۗ كَذَٰلِكَ زَيَّنَّا لِكُلِّ أُمَّةٍ عَمَلَهُمْ ثُمَّ إِلَىٰ رَبِّهِم مَّرْجِعُهُمْ فَيُنَبِّئُهُم بِمَا كَانُوا۟ …
- 6:122:20 [زَيَّنَ V II PERF PASS] … فِى ٱلنَّاسِ كَمَن مَّثَلُهُۥ فِى ٱلظُّلُمَٰتِ لَيْسَ بِخَارِجٍۢ مِّنْهَا ۚ كَذَٰلِكَ زُيِّنَ لِلْكَٰفِرِينَ مَا كَانُوا۟ يَعْمَلُونَ
- 6:137:2 [زَيَّنَ V II PERF] وَكَذَٰلِكَ زَيَّنَ لِكَثِيرٍۢ مِّنَ ٱلْمُشْرِكِينَ قَتْلَ أَوْلَٰدِهِمْ شُرَكَآؤُهُمْ لِيُرْدُوهُمْ وَلِيَلْبِسُوا۟ عَلَيْهِمْ دِينَهُمْ …
- 8:48:2 [زَيَّنَ V II PERF] وَإِذْ زَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ وَقَالَ لَا غَالِبَ لَكُمُ ٱلْيَوْمَ مِنَ ٱلنَّاسِ …
- 9:37:23 [زَيَّنَ V II PERF PASS] … عَامًۭا لِّيُوَاطِـُٔوا۟ عِدَّةَ مَا حَرَّمَ ٱللَّهُ فَيُحِلُّوا۟ مَا حَرَّمَ ٱللَّهُ ۚ زُيِّنَ لَهُمْ سُوٓءُ أَعْمَٰلِهِمْ ۗ وَٱللَّهُ لَا يَهْدِى ٱلْقَوْمَ ٱلْكَٰفِرِينَ
- 10:12:23 [زَيَّنَ V II PERF PASS] … عَنْهُ ضُرَّهُۥ مَرَّ كَأَن لَّمْ يَدْعُنَآ إِلَىٰ ضُرٍّۢ مَّسَّهُۥ ۚ كَذَٰلِكَ زُيِّنَ لِلْمُسْرِفِينَ مَا كَانُوا۟ يَعْمَلُونَ
- 13:33:26 [زَيَّنَ V II PERF PASS] … بِمَا لَا يَعْلَمُ فِى ٱلْأَرْضِ أَم بِظَٰهِرٍۢ مِّنَ ٱلْقَوْلِ ۗ بَلْ زُيِّنَ لِلَّذِينَ كَفَرُوا۟ مَكْرُهُمْ وَصُدُّوا۟ عَنِ ٱلسَّبِيلِ ۗ وَمَن يُضْلِلِ ٱللَّهُ فَمَا …
- 15:16:6 [زَيَّنَ V II PERF] وَلَقَدْ جَعَلْنَا فِى ٱلسَّمَآءِ بُرُوجًۭا وَزَيَّنَّٰهَا لِلنَّٰظِرِينَ
- 15:39:5 [زَيَّنَ V II IMPF] قَالَ رَبِّ بِمَآ أَغْوَيْتَنِى لَأُزَيِّنَنَّ لَهُمْ فِى ٱلْأَرْضِ وَلَأُغْوِيَنَّهُمْ أَجْمَعِينَ
- 16:63:8 [زَيَّنَ V II PERF] تَٱللَّهِ لَقَدْ أَرْسَلْنَآ إِلَىٰٓ أُمَمٍۢ مِّن قَبْلِكَ فَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ فَهُوَ وَلِيُّهُمُ ٱلْيَوْمَ وَلَهُمْ عَذَابٌ أَلِيمٌۭ
- 27:4:6 [زَيَّنَ V II PERF] إِنَّ ٱلَّذِينَ لَا يُؤْمِنُونَ بِٱلْءَاخِرَةِ زَيَّنَّا لَهُمْ أَعْمَٰلَهُمْ فَهُمْ يَعْمَهُونَ
- 27:24:8 [زَيَّنَ V II PERF] وَجَدتُّهَا وَقَوْمَهَا يَسْجُدُونَ لِلشَّمْسِ مِن دُونِ ٱللَّهِ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ فَصَدَّهُمْ عَنِ ٱلسَّبِيلِ فَهُمْ لَا يَهْتَدُونَ
- 29:38:8 [زَيَّنَ V II PERF] وَعَادًۭا وَثَمُودَا۟ وَقَد تَّبَيَّنَ لَكُم مِّن مَّسَٰكِنِهِمْ ۖ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ فَصَدَّهُمْ عَنِ ٱلسَّبِيلِ وَكَانُوا۟ مُسْتَبْصِرِينَ
- 35:8:2 [زَيَّنَ V II PERF PASS] أَفَمَن زُيِّنَ لَهُۥ سُوٓءُ عَمَلِهِۦ فَرَءَاهُ حَسَنًۭا ۖ فَإِنَّ ٱللَّهَ يُضِلُّ مَن يَشَآءُ …
- 37:6:2 [زَيَّنَ V II PERF] إِنَّا زَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِزِينَةٍ ٱلْكَوَاكِبِ
- 40:37:11 [زَيَّنَ V II PERF PASS] أَسْبَٰبَ ٱلسَّمَٰوَٰتِ فَأَطَّلِعَ إِلَىٰٓ إِلَٰهِ مُوسَىٰ وَإِنِّى لَأَظُنُّهُۥ كَٰذِبًۭا ۚ وَكَذَٰلِكَ زُيِّنَ لِفِرْعَوْنَ سُوٓءُ عَمَلِهِۦ وَصُدَّ عَنِ ٱلسَّبِيلِ ۚ وَمَا كَيْدُ فِرْعَوْنَ إِلَّا …
- 41:12:11 [زَيَّنَ V II PERF] فَقَضَىٰهُنَّ سَبْعَ سَمَٰوَاتٍۢ فِى يَوْمَيْنِ وَأَوْحَىٰ فِى كُلِّ سَمَآءٍ أَمْرَهَا ۚ وَزَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِمَصَٰبِيحَ وَحِفْظًۭا ۚ ذَٰلِكَ تَقْدِيرُ ٱلْعَزِيزِ ٱلْعَلِيمِ
- 41:25:4 [زَيَّنَ V II PERF] وَقَيَّضْنَا لَهُمْ قُرَنَآءَ فَزَيَّنُوا۟ لَهُم مَّا بَيْنَ أَيْدِيهِمْ وَمَا خَلْفَهُمْ وَحَقَّ عَلَيْهِمُ ٱلْقَوْلُ فِىٓ …
- 47:14:8 [زَيَّنَ V II PERF PASS] أَفَمَن كَانَ عَلَىٰ بَيِّنَةٍۢ مِّن رَّبِّهِۦ كَمَن زُيِّنَ لَهُۥ سُوٓءُ عَمَلِهِۦ وَٱتَّبَعُوٓا۟ أَهْوَآءَهُم
- 48:12:11 [زَيَّنَ V II PERF PASS] بَلْ ظَنَنتُمْ أَن لَّن يَنقَلِبَ ٱلرَّسُولُ وَٱلْمُؤْمِنُونَ إِلَىٰٓ أَهْلِيهِمْ أَبَدًۭا وَزُيِّنَ ذَٰلِكَ فِى قُلُوبِكُمْ وَظَنَنتُمْ ظَنَّ ٱلسَّوْءِ وَكُنتُمْ قَوْمًۢا بُورًۭا
- 49:7:18 [زَيَّنَ V II PERF] … فِى كَثِيرٍۢ مِّنَ ٱلْأَمْرِ لَعَنِتُّمْ وَلَٰكِنَّ ٱللَّهَ حَبَّبَ إِلَيْكُمُ ٱلْإِيمَٰنَ وَزَيَّنَهُۥ فِى قُلُوبِكُمْ وَكَرَّهَ إِلَيْكُمُ ٱلْكُفْرَ وَٱلْفُسُوقَ وَٱلْعِصْيَانَ ۚ أُو۟لَٰٓئِكَ هُمُ ٱلرَّٰشِدُونَ
- 50:6:8 [زَيَّنَ V II PERF] أَفَلَمْ يَنظُرُوٓا۟ إِلَى ٱلسَّمَآءِ فَوْقَهُمْ كَيْفَ بَنَيْنَٰهَا وَزَيَّنَّٰهَا وَمَا لَهَا مِن فُرُوجٍۢ
- 67:5:2 [زَيَّنَ V II PERF] وَلَقَدْ زَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِمَصَٰبِيحَ وَجَعَلْنَٰهَا رُجُومًۭا لِّلشَّيَٰطِينِ ۖ وَأَعْتَدْنَا لَهُمْ عَذَابَ ٱلسَّعِيرِ
### زِينَة
- 7:31:4 [زِينَة N] يَٰبَنِىٓ ءَادَمَ خُذُوا۟ زِينَتَكُمْ عِندَ كُلِّ مَسْجِدٍۢ وَكُلُوا۟ وَٱشْرَبُوا۟ وَلَا تُسْرِفُوٓا۟ ۚ إِنَّهُۥ لَا يُحِبُّ …
- 7:32:4 [زِينَة N] قُلْ مَنْ حَرَّمَ زِينَةَ ٱللَّهِ ٱلَّتِىٓ أَخْرَجَ لِعِبَادِهِۦ وَٱلطَّيِّبَٰتِ مِنَ ٱلرِّزْقِ ۚ قُلْ هِىَ لِلَّذِينَ …
- 10:88:8 [زِينَة N] وَقَالَ مُوسَىٰ رَبَّنَآ إِنَّكَ ءَاتَيْتَ فِرْعَوْنَ وَمَلَأَهُۥ زِينَةًۭ وَأَمْوَٰلًۭا فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا رَبَّنَا لِيُضِلُّوا۟ عَن سَبِيلِكَ ۖ رَبَّنَا ٱطْمِسْ …
- 11:15:6 [زِينَة N] مَن كَانَ يُرِيدُ ٱلْحَيَوٰةَ ٱلدُّنْيَا وَزِينَتَهَا نُوَفِّ إِلَيْهِمْ أَعْمَٰلَهُمْ فِيهَا وَهُمْ فِيهَا لَا يُبْخَسُونَ
- 16:8:5 [زِينَة N] وَٱلْخَيْلَ وَٱلْبِغَالَ وَٱلْحَمِيرَ لِتَرْكَبُوهَا وَزِينَةًۭ ۚ وَيَخْلُقُ مَا لَا تَعْلَمُونَ
- 18:7:6 [زِينَة N] إِنَّا جَعَلْنَا مَا عَلَى ٱلْأَرْضِ زِينَةًۭ لَّهَا لِنَبْلُوَهُمْ أَيُّهُمْ أَحْسَنُ عَمَلًۭا
- 18:28:16 [زِينَة N] … رَبَّهُم بِٱلْغَدَوٰةِ وَٱلْعَشِىِّ يُرِيدُونَ وَجْهَهُۥ ۖ وَلَا تَعْدُ عَيْنَاكَ عَنْهُمْ تُرِيدُ زِينَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَلَا تُطِعْ مَنْ أَغْفَلْنَا قَلْبَهُۥ عَن ذِكْرِنَا وَٱتَّبَعَ …
- 18:46:3 [زِينَة N] ٱلْمَالُ وَٱلْبَنُونَ زِينَةُ ٱلْحَيَوٰةِ ٱلدُّنْيَا ۖ وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا وَخَيْرٌ أَمَلًۭا
- 20:59:4 [زِينَة N] قَالَ مَوْعِدُكُمْ يَوْمُ ٱلزِّينَةِ وَأَن يُحْشَرَ ٱلنَّاسُ ضُحًۭى
- 20:87:10 [زِينَة N] قَالُوا۟ مَآ أَخْلَفْنَا مَوْعِدَكَ بِمَلْكِنَا وَلَٰكِنَّا حُمِّلْنَآ أَوْزَارًۭا مِّن زِينَةِ ٱلْقَوْمِ فَقَذَفْنَٰهَا فَكَذَٰلِكَ أَلْقَى ٱلسَّامِرِىُّ
- 24:31:10 [زِينَة N] وَقُل لِّلْمُؤْمِنَٰتِ يَغْضُضْنَ مِنْ أَبْصَٰرِهِنَّ وَيَحْفَظْنَ فُرُوجَهُنَّ وَلَا يُبْدِينَ زِينَتَهُنَّ إِلَّا مَا ظَهَرَ مِنْهَا ۖ وَلْيَضْرِبْنَ بِخُمُرِهِنَّ عَلَىٰ جُيُوبِهِنَّ ۖ وَلَا يُبْدِينَ …
- 24:31:21 [زِينَة N] … إِلَّا مَا ظَهَرَ مِنْهَا ۖ وَلْيَضْرِبْنَ بِخُمُرِهِنَّ عَلَىٰ جُيُوبِهِنَّ ۖ وَلَا يُبْدِينَ زِينَتَهُنَّ إِلَّا لِبُعُولَتِهِنَّ أَوْ ءَابَآئِهِنَّ أَوْ ءَابَآءِ بُعُولَتِهِنَّ أَوْ أَبْنَآئِهِنَّ أَوْ …
- 24:31:70 [زِينَة N] … عَلَىٰ عَوْرَٰتِ ٱلنِّسَآءِ ۖ وَلَا يَضْرِبْنَ بِأَرْجُلِهِنَّ لِيُعْلَمَ مَا يُخْفِينَ مِن زِينَتِهِنَّ ۚ وَتُوبُوٓا۟ إِلَى ٱللَّهِ جَمِيعًا أَيُّهَ ٱلْمُؤْمِنُونَ لَعَلَّكُمْ تُفْلِحُونَ
- 24:60:16 [زِينَة N] … يَرْجُونَ نِكَاحًۭا فَلَيْسَ عَلَيْهِنَّ جُنَاحٌ أَن يَضَعْنَ ثِيَابَهُنَّ غَيْرَ مُتَبَرِّجَٰتٍۭ بِزِينَةٍۢ ۖ وَأَن يَسْتَعْفِفْنَ خَيْرٌۭ لَّهُنَّ ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌۭ
- 28:60:8 [زِينَة N] وَمَآ أُوتِيتُم مِّن شَىْءٍۢ فَمَتَٰعُ ٱلْحَيَوٰةِ ٱلدُّنْيَا وَزِينَتُهَا ۚ وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰٓ ۚ أَفَلَا تَعْقِلُونَ
- 28:79:5 [زِينَة N] فَخَرَجَ عَلَىٰ قَوْمِهِۦ فِى زِينَتِهِۦ ۖ قَالَ ٱلَّذِينَ يُرِيدُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا يَٰلَيْتَ لَنَا مِثْلَ مَآ أُوتِىَ …
- 33:28:10 [زِينَة N] يَٰٓأَيُّهَا ٱلنَّبِىُّ قُل لِّأَزْوَٰجِكَ إِن كُنتُنَّ تُرِدْنَ ٱلْحَيَوٰةَ ٱلدُّنْيَا وَزِينَتَهَا فَتَعَالَيْنَ أُمَتِّعْكُنَّ وَأُسَرِّحْكُنَّ سَرَاحًۭا جَمِيلًۭا
- 37:6:5 [زِينَة N] إِنَّا زَيَّنَّا ٱلسَّمَآءَ ٱلدُّنْيَا بِزِينَةٍ ٱلْكَوَاكِبِ
- 57:20:7 [زِينَة N] ٱعْلَمُوٓا۟ أَنَّمَا ٱلْحَيَوٰةُ ٱلدُّنْيَا لَعِبٌۭ وَلَهْوٌۭ وَزِينَةٌۭ وَتَفَاخُرٌۢ بَيْنَكُمْ وَتَكَاثُرٌۭ فِى ٱلْأَمْوَٰلِ وَٱلْأَوْلَٰدِ ۖ كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ …
### ٱزَّيَّنَتْ
- 10:24:22 [ٱزَّيَّنَتْ V V PERF] … ٱلْأَرْضِ مِمَّا يَأْكُلُ ٱلنَّاسُ وَٱلْأَنْعَٰمُ حَتَّىٰٓ إِذَآ أَخَذَتِ ٱلْأَرْضُ زُخْرُفَهَا وَٱزَّيَّنَتْ وَظَنَّ أَهْلُهَآ أَنَّهُمْ قَٰدِرُونَ عَلَيْهَآ أَتَىٰهَآ أَمْرُنَا لَيْلًا أَوْ نَهَارًۭا …

## ش ط ن — 88 uses; here 29:38:10; lemmas: شَيْطَٰن 88

## ع م ل — 360 uses; here 29:38:11; lemmas: عَمِلَ 276; عَمَل 71; عَٰمِل 12; عَامِلَة 1

## ص د د — 42 uses; here 29:38:12; lemmas: صَدَّ 37; صَدّ 2; صُدُود 1; صُدُّ 1; صَدِيد 1
### صَدّ
- 2:217:11 [صَدّ N] يَسْـَٔلُونَكَ عَنِ ٱلشَّهْرِ ٱلْحَرَامِ قِتَالٍۢ فِيهِ ۖ قُلْ قِتَالٌۭ فِيهِ كَبِيرٌۭ ۖ وَصَدٌّ عَن سَبِيلِ ٱللَّهِ وَكُفْرٌۢ بِهِۦ وَٱلْمَسْجِدِ ٱلْحَرَامِ وَإِخْرَاجُ أَهْلِهِۦ مِنْهُ …
- 4:160:10 [صَدّ N] فَبِظُلْمٍۢ مِّنَ ٱلَّذِينَ هَادُوا۟ حَرَّمْنَا عَلَيْهِمْ طَيِّبَٰتٍ أُحِلَّتْ لَهُمْ وَبِصَدِّهِمْ عَن سَبِيلِ ٱللَّهِ كَثِيرًۭا
### صَدَّ
- 3:99:5 [صَدَّ V IMPF] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ لِمَ تَصُدُّونَ عَن سَبِيلِ ٱللَّهِ مَنْ ءَامَنَ تَبْغُونَهَا عِوَجًۭا وَأَنتُمْ شُهَدَآءُ ۗ وَمَا …
- 4:55:7 [صَدَّ V PERF] فَمِنْهُم مَّنْ ءَامَنَ بِهِۦ وَمِنْهُم مَّن صَدَّ عَنْهُ ۚ وَكَفَىٰ بِجَهَنَّمَ سَعِيرًا
- 4:61:13 [صَدَّ V IMPF] … لَهُمْ تَعَالَوْا۟ إِلَىٰ مَآ أَنزَلَ ٱللَّهُ وَإِلَى ٱلرَّسُولِ رَأَيْتَ ٱلْمُنَٰفِقِينَ يَصُدُّونَ عَنكَ صُدُودًۭا
- 4:167:4 [صَدَّ V PERF] إِنَّ ٱلَّذِينَ كَفَرُوا۟ وَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ قَدْ ضَلُّوا۟ ضَلَٰلًۢا بَعِيدًا
- 5:2:32 [صَدَّ V PERF] … رَّبِّهِمْ وَرِضْوَٰنًۭا ۚ وَإِذَا حَلَلْتُمْ فَٱصْطَادُوا۟ ۚ وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ أَن صَدُّوكُمْ عَنِ ٱلْمَسْجِدِ ٱلْحَرَامِ أَن تَعْتَدُوا۟ ۘ وَتَعَاوَنُوا۟ عَلَى ٱلْبِرِّ وَٱلتَّقْوَىٰ ۖ وَلَا …
- 5:91:12 [صَدَّ V IMPF SUBJ] … يُرِيدُ ٱلشَّيْطَٰنُ أَن يُوقِعَ بَيْنَكُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ فِى ٱلْخَمْرِ وَٱلْمَيْسِرِ وَيَصُدَّكُمْ عَن ذِكْرِ ٱللَّهِ وَعَنِ ٱلصَّلَوٰةِ ۖ فَهَلْ أَنتُم مُّنتَهُونَ
- 7:45:2 [صَدَّ V IMPF] ٱلَّذِينَ يَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًۭا وَهُم بِٱلْءَاخِرَةِ كَٰفِرُونَ
- 7:86:6 [صَدَّ V IMPF] وَلَا تَقْعُدُوا۟ بِكُلِّ صِرَٰطٍۢ تُوعِدُونَ وَتَصُدُّونَ عَن سَبِيلِ ٱللَّهِ مَنْ ءَامَنَ بِهِۦ وَتَبْغُونَهَا عِوَجًۭا ۚ وَٱذْكُرُوٓا۟ إِذْ …
- 8:34:7 [صَدَّ V IMPF] وَمَا لَهُمْ أَلَّا يُعَذِّبَهُمُ ٱللَّهُ وَهُمْ يَصُدُّونَ عَنِ ٱلْمَسْجِدِ ٱلْحَرَامِ وَمَا كَانُوٓا۟ أَوْلِيَآءَهُۥٓ ۚ إِنْ أَوْلِيَآؤُهُۥٓ إِلَّا ٱلْمُتَّقُونَ …
- 8:36:6 [صَدَّ V IMPF SUBJ] إِنَّ ٱلَّذِينَ كَفَرُوا۟ يُنفِقُونَ أَمْوَٰلَهُمْ لِيَصُدُّوا۟ عَن سَبِيلِ ٱللَّهِ ۚ فَسَيُنفِقُونَهَا ثُمَّ تَكُونُ عَلَيْهِمْ حَسْرَةًۭ ثُمَّ يُغْلَبُونَ …
- 8:47:10 [صَدَّ V IMPF] وَلَا تَكُونُوا۟ كَٱلَّذِينَ خَرَجُوا۟ مِن دِيَٰرِهِم بَطَرًۭا وَرِئَآءَ ٱلنَّاسِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ ۚ وَٱللَّهُ بِمَا يَعْمَلُونَ مُحِيطٌۭ
- 9:9:6 [صَدَّ V PERF] ٱشْتَرَوْا۟ بِـَٔايَٰتِ ٱللَّهِ ثَمَنًۭا قَلِيلًۭا فَصَدُّوا۟ عَن سَبِيلِهِۦٓ ۚ إِنَّهُمْ سَآءَ مَا كَانُوا۟ يَعْمَلُونَ
- 9:34:13 [صَدَّ V IMPF] … ءَامَنُوٓا۟ إِنَّ كَثِيرًۭا مِّنَ ٱلْأَحْبَارِ وَٱلرُّهْبَانِ لَيَأْكُلُونَ أَمْوَٰلَ ٱلنَّاسِ بِٱلْبَٰطِلِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ ۗ وَٱلَّذِينَ يَكْنِزُونَ ٱلذَّهَبَ وَٱلْفِضَّةَ وَلَا يُنفِقُونَهَا فِى …
- 11:19:2 [صَدَّ V IMPF] ٱلَّذِينَ يَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًۭا وَهُم بِٱلْءَاخِرَةِ هُمْ كَٰفِرُونَ
- 14:3:7 [صَدَّ V IMPF] ٱلَّذِينَ يَسْتَحِبُّونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا عَلَى ٱلْءَاخِرَةِ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَيَبْغُونَهَا عِوَجًا ۚ أُو۟لَٰٓئِكَ فِى ضَلَٰلٍۭ بَعِيدٍۢ
- 14:10:26 [صَدَّ V IMPF SUBJ] … أَجَلٍۢ مُّسَمًّۭى ۚ قَالُوٓا۟ إِنْ أَنتُمْ إِلَّا بَشَرٌۭ مِّثْلُنَا تُرِيدُونَ أَن تَصُدُّونَا عَمَّا كَانَ يَعْبُدُ ءَابَآؤُنَا فَأْتُونَا بِسُلْطَٰنٍۢ مُّبِينٍۢ
- 16:88:3 [صَدَّ V PERF] ٱلَّذِينَ كَفَرُوا۟ وَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ زِدْنَٰهُمْ عَذَابًۭا فَوْقَ ٱلْعَذَابِ بِمَا كَانُوا۟ يُفْسِدُونَ
- 16:94:13 [صَدَّ V PERF] … أَيْمَٰنَكُمْ دَخَلًۢا بَيْنَكُمْ فَتَزِلَّ قَدَمٌۢ بَعْدَ ثُبُوتِهَا وَتَذُوقُوا۟ ٱلسُّوٓءَ بِمَا صَدَدتُّمْ عَن سَبِيلِ ٱللَّهِ ۖ وَلَكُمْ عَذَابٌ عَظِيمٌۭ
- 20:16:2 [صَدَّ V IMPF JUS] فَلَا يَصُدَّنَّكَ عَنْهَا مَن لَّا يُؤْمِنُ بِهَا وَٱتَّبَعَ هَوَىٰهُ فَتَرْدَىٰ
- 22:25:4 [صَدَّ V IMPF] إِنَّ ٱلَّذِينَ كَفَرُوا۟ وَيَصُدُّونَ عَن سَبِيلِ ٱللَّهِ وَٱلْمَسْجِدِ ٱلْحَرَامِ ٱلَّذِى جَعَلْنَٰهُ لِلنَّاسِ سَوَآءً ٱلْعَٰكِفُ …
- 27:24:12 [صَدَّ V PERF] … وَقَوْمَهَا يَسْجُدُونَ لِلشَّمْسِ مِن دُونِ ٱللَّهِ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ فَصَدَّهُمْ عَنِ ٱلسَّبِيلِ فَهُمْ لَا يَهْتَدُونَ
- 27:43:1 [صَدَّ V PERF] وَصَدَّهَا مَا كَانَت تَّعْبُدُ مِن دُونِ ٱللَّهِ ۖ إِنَّهَا كَانَتْ مِن قَوْمٍۢ …
- 28:87:2 [صَدَّ V IMPF] وَلَا يَصُدُّنَّكَ عَنْ ءَايَٰتِ ٱللَّهِ بَعْدَ إِذْ أُنزِلَتْ إِلَيْكَ ۖ وَٱدْعُ إِلَىٰ رَبِّكَ …
- 29:38:12 [صَدَّ V PERF] … وَثَمُودَا۟ وَقَد تَّبَيَّنَ لَكُم مِّن مَّسَٰكِنِهِمْ ۖ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ فَصَدَّهُمْ عَنِ ٱلسَّبِيلِ وَكَانُوا۟ مُسْتَبْصِرِينَ
- 34:32:7 [صَدَّ V PERF] قَالَ ٱلَّذِينَ ٱسْتَكْبَرُوا۟ لِلَّذِينَ ٱسْتُضْعِفُوٓا۟ أَنَحْنُ صَدَدْنَٰكُمْ عَنِ ٱلْهُدَىٰ بَعْدَ إِذْ جَآءَكُم ۖ بَلْ كُنتُم مُّجْرِمِينَ
- 34:43:13 [صَدَّ V IMPF SUBJ] … عَلَيْهِمْ ءَايَٰتُنَا بَيِّنَٰتٍۢ قَالُوا۟ مَا هَٰذَآ إِلَّا رَجُلٌۭ يُرِيدُ أَن يَصُدَّكُمْ عَمَّا كَانَ يَعْبُدُ ءَابَآؤُكُمْ وَقَالُوا۟ مَا هَٰذَآ إِلَّآ إِفْكٌۭ مُّفْتَرًۭى …
- 40:37:15 [صَدَّ V PERF PASS] … إِلَٰهِ مُوسَىٰ وَإِنِّى لَأَظُنُّهُۥ كَٰذِبًۭا ۚ وَكَذَٰلِكَ زُيِّنَ لِفِرْعَوْنَ سُوٓءُ عَمَلِهِۦ وَصُدَّ عَنِ ٱلسَّبِيلِ ۚ وَمَا كَيْدُ فِرْعَوْنَ إِلَّا فِى تَبَابٍۢ
- 43:37:2 [صَدَّ V IMPF] وَإِنَّهُمْ لَيَصُدُّونَهُمْ عَنِ ٱلسَّبِيلِ وَيَحْسَبُونَ أَنَّهُم مُّهْتَدُونَ
- 43:57:9 [صَدَّ V IMPF] وَلَمَّا ضُرِبَ ٱبْنُ مَرْيَمَ مَثَلًا إِذَا قَوْمُكَ مِنْهُ يَصِدُّونَ
- 43:62:2 [صَدَّ V IMPF] وَلَا يَصُدَّنَّكُمُ ٱلشَّيْطَٰنُ ۖ إِنَّهُۥ لَكُمْ عَدُوٌّۭ مُّبِينٌۭ
- 47:1:3 [صَدَّ V PERF] ٱلَّذِينَ كَفَرُوا۟ وَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ أَضَلَّ أَعْمَٰلَهُمْ
- 47:32:4 [صَدَّ V PERF] إِنَّ ٱلَّذِينَ كَفَرُوا۟ وَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ وَشَآقُّوا۟ ٱلرَّسُولَ مِنۢ بَعْدِ مَا تَبَيَّنَ لَهُمُ …
- 47:34:4 [صَدَّ V PERF] إِنَّ ٱلَّذِينَ كَفَرُوا۟ وَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ ثُمَّ مَاتُوا۟ وَهُمْ كُفَّارٌۭ فَلَن يَغْفِرَ ٱللَّهُ …
- 48:25:4 [صَدَّ V PERF] هُمُ ٱلَّذِينَ كَفَرُوا۟ وَصَدُّوكُمْ عَنِ ٱلْمَسْجِدِ ٱلْحَرَامِ وَٱلْهَدْىَ مَعْكُوفًا أَن يَبْلُغَ مَحِلَّهُۥ ۚ وَلَوْلَا رِجَالٌۭ …
- 58:16:4 [صَدَّ V PERF] ٱتَّخَذُوٓا۟ أَيْمَٰنَهُمْ جُنَّةًۭ فَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ فَلَهُمْ عَذَابٌۭ مُّهِينٌۭ
- 63:2:4 [صَدَّ V PERF] ٱتَّخَذُوٓا۟ أَيْمَٰنَهُمْ جُنَّةًۭ فَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ ۚ إِنَّهُمْ سَآءَ مَا كَانُوا۟ يَعْمَلُونَ
- 63:5:12 [صَدَّ V IMPF] … قِيلَ لَهُمْ تَعَالَوْا۟ يَسْتَغْفِرْ لَكُمْ رَسُولُ ٱللَّهِ لَوَّوْا۟ رُءُوسَهُمْ وَرَأَيْتَهُمْ يَصُدُّونَ وَهُم مُّسْتَكْبِرُونَ
### صُدُود
- 4:61:15 [صُدُود N] … إِلَىٰ مَآ أَنزَلَ ٱللَّهُ وَإِلَى ٱلرَّسُولِ رَأَيْتَ ٱلْمُنَٰفِقِينَ يَصُدُّونَ عَنكَ صُدُودًۭا
### صُدُّ
- 13:33:30 [صُدُّ V II PERF PASS] … ٱلْأَرْضِ أَم بِظَٰهِرٍۢ مِّنَ ٱلْقَوْلِ ۗ بَلْ زُيِّنَ لِلَّذِينَ كَفَرُوا۟ مَكْرُهُمْ وَصُدُّوا۟ عَنِ ٱلسَّبِيلِ ۗ وَمَن يُضْلِلِ ٱللَّهُ فَمَا لَهُۥ مِنْ هَادٍۢ
### صَدِيد
- 14:16:7 [صَدِيد ADJ] مِّن وَرَآئِهِۦ جَهَنَّمُ وَيُسْقَىٰ مِن مَّآءٍۢ صَدِيدٍۢ

## س ب ل — 176 uses; here 29:38:14; lemmas: سَبِيل 176

## ك و ن — 32 uses; here (stop lemma only); lemmas: مَّكَان 27; مَكَانَت 5
### مَّكَان
- 4:20:5 [مَّكَان N] وَإِنْ أَرَدتُّمُ ٱسْتِبْدَالَ زَوْجٍۢ مَّكَانَ زَوْجٍۢ وَءَاتَيْتُمْ إِحْدَىٰهُنَّ قِنطَارًۭا فَلَا تَأْخُذُوا۟ مِنْهُ شَيْـًٔا ۚ أَتَأْخُذُونَهُۥ بُهْتَٰنًۭا …
- 5:60:23 [مَّكَان N] … وَغَضِبَ عَلَيْهِ وَجَعَلَ مِنْهُمُ ٱلْقِرَدَةَ وَٱلْخَنَازِيرَ وَعَبَدَ ٱلطَّٰغُوتَ ۚ أُو۟لَٰٓئِكَ شَرٌّۭ مَّكَانًۭا وَأَضَلُّ عَن سَوَآءِ ٱلسَّبِيلِ
- 7:95:3 [مَّكَان N] ثُمَّ بَدَّلْنَا مَكَانَ ٱلسَّيِّئَةِ ٱلْحَسَنَةَ حَتَّىٰ عَفَوا۟ وَّقَالُوا۟ قَدْ مَسَّ ءَابَآءَنَا ٱلضَّرَّآءُ وَٱلسَّرَّآءُ …
- 7:143:21 [مَّكَان N] … إِلَيْكَ ۚ قَالَ لَن تَرَىٰنِى وَلَٰكِنِ ٱنظُرْ إِلَى ٱلْجَبَلِ فَإِنِ ٱسْتَقَرَّ مَكَانَهُۥ فَسَوْفَ تَرَىٰنِى ۚ فَلَمَّا تَجَلَّىٰ رَبُّهُۥ لِلْجَبَلِ جَعَلَهُۥ دَكًّۭا وَخَرَّ مُوسَىٰ …
- 10:22:25 [مَّكَان N] … طَيِّبَةٍۢ وَفَرِحُوا۟ بِهَا جَآءَتْهَا رِيحٌ عَاصِفٌۭ وَجَآءَهُمُ ٱلْمَوْجُ مِن كُلِّ مَكَانٍۢ وَظَنُّوٓا۟ أَنَّهُمْ أُحِيطَ بِهِمْ ۙ دَعَوُا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ لَئِنْ …
- 10:28:8 [مَّكَان N] وَيَوْمَ نَحْشُرُهُمْ جَمِيعًۭا ثُمَّ نَقُولُ لِلَّذِينَ أَشْرَكُوا۟ مَكَانَكُمْ أَنتُمْ وَشُرَكَآؤُكُمْ ۚ فَزَيَّلْنَا بَيْنَهُمْ ۖ وَقَالَ شُرَكَآؤُهُم مَّا كُنتُمْ إِيَّانَا تَعْبُدُونَ
- 12:77:20 [مَّكَان N] … فَأَسَرَّهَا يُوسُفُ فِى نَفْسِهِۦ وَلَمْ يُبْدِهَا لَهُمْ ۚ قَالَ أَنتُمْ شَرٌّۭ مَّكَانًۭا ۖ وَٱللَّهُ أَعْلَمُ بِمَا تَصِفُونَ
- 12:78:11 [مَّكَان N] قَالُوا۟ يَٰٓأَيُّهَا ٱلْعَزِيزُ إِنَّ لَهُۥٓ أَبًۭا شَيْخًۭا كَبِيرًۭا فَخُذْ أَحَدَنَا مَكَانَهُۥٓ ۖ إِنَّا نَرَىٰكَ مِنَ ٱلْمُحْسِنِينَ
- 14:17:9 [مَّكَان N] يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ وَيَأْتِيهِ ٱلْمَوْتُ مِن كُلِّ مَكَانٍۢ وَمَا هُوَ بِمَيِّتٍۢ ۖ وَمِن وَرَآئِهِۦ عَذَابٌ غَلِيظٌۭ
- 16:101:4 [مَّكَان N] وَإِذَا بَدَّلْنَآ ءَايَةًۭ مَّكَانَ ءَايَةٍۢ ۙ وَٱللَّهُ أَعْلَمُ بِمَا يُنَزِّلُ قَالُوٓا۟ إِنَّمَآ أَنتَ مُفْتَرٍۭ ۚ بَلْ …
- 16:112:13 [مَّكَان N] … مَثَلًۭا قَرْيَةًۭ كَانَتْ ءَامِنَةًۭ مُّطْمَئِنَّةًۭ يَأْتِيهَا رِزْقُهَا رَغَدًۭا مِّن كُلِّ مَكَانٍۢ فَكَفَرَتْ بِأَنْعُمِ ٱللَّهِ فَأَذَٰقَهَا ٱللَّهُ لِبَاسَ ٱلْجُوعِ وَٱلْخَوْفِ بِمَا كَانُوا۟ …
- 19:16:9 [مَّكَان LOC] وَٱذْكُرْ فِى ٱلْكِتَٰبِ مَرْيَمَ إِذِ ٱنتَبَذَتْ مِنْ أَهْلِهَا مَكَانًۭا شَرْقِيًّۭا
- 19:22:4 [مَّكَان LOC] فَحَمَلَتْهُ فَٱنتَبَذَتْ بِهِۦ مَكَانًۭا قَصِيًّۭا
- 19:57:2 [مَّكَان N] وَرَفَعْنَٰهُ مَكَانًا عَلِيًّا
- 19:75:23 [مَّكَان N] … مَا يُوعَدُونَ إِمَّا ٱلْعَذَابَ وَإِمَّا ٱلسَّاعَةَ فَسَيَعْلَمُونَ مَنْ هُوَ شَرٌّۭ مَّكَانًۭا وَأَضْعَفُ جُندًۭا
- 20:58:13 [مَّكَان N] … مِّثْلِهِۦ فَٱجْعَلْ بَيْنَنَا وَبَيْنَكَ مَوْعِدًۭا لَّا نُخْلِفُهُۥ نَحْنُ وَلَآ أَنتَ مَكَانًۭا سُوًۭى
- 22:26:4 [مَّكَان N] وَإِذْ بَوَّأْنَا لِإِبْرَٰهِيمَ مَكَانَ ٱلْبَيْتِ أَن لَّا تُشْرِكْ بِى شَيْـًۭٔا وَطَهِّرْ بَيْتِىَ لِلطَّآئِفِينَ وَٱلْقَآئِمِينَ …
- 22:31:20 [مَّكَان N] … خَرَّ مِنَ ٱلسَّمَآءِ فَتَخْطَفُهُ ٱلطَّيْرُ أَوْ تَهْوِى بِهِ ٱلرِّيحُ فِى مَكَانٍۢ سَحِيقٍۢ
- 25:12:4 [مَّكَان N] إِذَا رَأَتْهُم مِّن مَّكَانٍۭ بَعِيدٍۢ سَمِعُوا۟ لَهَا تَغَيُّظًۭا وَزَفِيرًۭا
- 25:13:4 [مَّكَان N] وَإِذَآ أُلْقُوا۟ مِنْهَا مَكَانًۭا ضَيِّقًۭا مُّقَرَّنِينَ دَعَوْا۟ هُنَالِكَ ثُبُورًۭا
- 25:34:9 [مَّكَان N] ٱلَّذِينَ يُحْشَرُونَ عَلَىٰ وُجُوهِهِمْ إِلَىٰ جَهَنَّمَ أُو۟لَٰٓئِكَ شَرٌّۭ مَّكَانًۭا وَأَضَلُّ سَبِيلًۭا
- 28:82:4 [مَّكَان N] وَأَصْبَحَ ٱلَّذِينَ تَمَنَّوْا۟ مَكَانَهُۥ بِٱلْأَمْسِ يَقُولُونَ وَيْكَأَنَّ ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ …
- 34:51:9 [مَّكَان N] وَلَوْ تَرَىٰٓ إِذْ فَزِعُوا۟ فَلَا فَوْتَ وَأُخِذُوا۟ مِن مَّكَانٍۢ قَرِيبٍۢ
- 34:52:8 [مَّكَان N] وَقَالُوٓا۟ ءَامَنَّا بِهِۦ وَأَنَّىٰ لَهُمُ ٱلتَّنَاوُشُ مِن مَّكَانٍۭ بَعِيدٍۢ
- 34:53:9 [مَّكَان N] وَقَدْ كَفَرُوا۟ بِهِۦ مِن قَبْلُ ۖ وَيَقْذِفُونَ بِٱلْغَيْبِ مِن مَّكَانٍۭ بَعِيدٍۢ
- 41:44:29 [مَّكَان N] … يُؤْمِنُونَ فِىٓ ءَاذَانِهِمْ وَقْرٌۭ وَهُوَ عَلَيْهِمْ عَمًى ۚ أُو۟لَٰٓئِكَ يُنَادَوْنَ مِن مَّكَانٍۭ بَعِيدٍۢ
- 50:41:6 [مَّكَان N] وَٱسْتَمِعْ يَوْمَ يُنَادِ ٱلْمُنَادِ مِن مَّكَانٍۢ قَرِيبٍۢ
### مَكَانَت
- 6:135:5 [مَكَانَت N] قُلْ يَٰقَوْمِ ٱعْمَلُوا۟ عَلَىٰ مَكَانَتِكُمْ إِنِّى عَامِلٌۭ ۖ فَسَوْفَ تَعْلَمُونَ مَن تَكُونُ لَهُۥ عَٰقِبَةُ ٱلدَّارِ ۗ إِنَّهُۥ …
- 11:93:4 [مَكَانَت N] وَيَٰقَوْمِ ٱعْمَلُوا۟ عَلَىٰ مَكَانَتِكُمْ إِنِّى عَٰمِلٌۭ ۖ سَوْفَ تَعْلَمُونَ مَن يَأْتِيهِ عَذَابٌۭ يُخْزِيهِ وَمَنْ هُوَ …
- 11:121:7 [مَكَانَت N] وَقُل لِّلَّذِينَ لَا يُؤْمِنُونَ ٱعْمَلُوا۟ عَلَىٰ مَكَانَتِكُمْ إِنَّا عَٰمِلُونَ
- 36:67:5 [مَكَانَت N] وَلَوْ نَشَآءُ لَمَسَخْنَٰهُمْ عَلَىٰ مَكَانَتِهِمْ فَمَا ٱسْتَطَٰعُوا۟ مُضِيًّۭا وَلَا يَرْجِعُونَ
- 39:39:5 [مَكَانَت N] قُلْ يَٰقَوْمِ ٱعْمَلُوا۟ عَلَىٰ مَكَانَتِكُمْ إِنِّى عَٰمِلٌۭ ۖ فَسَوْفَ تَعْلَمُونَ

## ب ص ر — 148 uses; here 29:38:16; lemmas: بَصِير 51; بَصَر 48; أَبْصَرَ 29; بَصِيرَة 7; مُبْصِر 4; مُبْصِرَة 3; بَصُرَتْ 3; مُسْتَبْصِرِين 1; تَبْصِرَة 1; يُبَصَّرُ 1



===== variants.md =====
## 1. Variant readings (qirāʾāt)

- word 4 · وَثَمُودًا (wa-Thamūdan) · Tnw · Canonical variant adding tanwīn to Thamūd — treats it as fully declinable (triptote), harmonizing with ʿĀdan; removes the morphological asymmetry between the paired names


===== source_access.md =====
# source_access.md — exact Quran passages on demand

Before developing a Quran cross-reference, retrieve its actual text and adjacent context. Use this command, replacing S:A,S:A with the references you need (up to 16 per request):

    python3 -B /Volumes/OZTURK/_projects/prose_generation/_commentary/v14/sources.py --tag astra-blind-29-38 --ref 29:38 --refs S:A,S:A --context 1

The helper reads only the frozen Quran corpus and logs the returned references and bytes. It never calls a model. Context may be 0, 1, 2 or 3 ayat on each side; use further requests when a scene needs more context. Do not read the entire corpus or unrelated repository files. Copy Quran quotations from returned text or the normalized concordance. Retrieval is for checking and understanding the passages you develop, not for turning all candidates into obligatory quotations. The full preceding prose is reader context, not a quotation source.


===== previous.md =====
# Earlier prose actually available to the reader

This contains only the immediately preceding ayah's actual prose. More distant prose is not supplied; do not assume it explained a reading. A network disclosure plan is not proof of earlier delivery.

## 29:37: no earlier prose available
