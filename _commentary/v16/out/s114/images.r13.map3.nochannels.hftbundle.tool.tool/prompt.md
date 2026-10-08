Surah: 114. Follow the brief below (surah_images.md) exactly. The evidence is text.md (the surah) and map.md (an earlier reader's map of the surah's image chains, with the dictionary phrases of their members, Quran passages and interactions; a proposal, not an authority) and your own knowledge of Arabic and the Quran. Return the prose and then the ledger, as surah_images.md specifies.

When your discovery is complete and before you write your final output, run this command once for each ayah of the surah (114:1 to 114:6), each time with every Quran reference outside this surah that your output will use: `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py <ayah> <refs separated by spaces>`. Each run lists refs from that ayah's earlier cross-reference list, by tier, that your refs do not include. That list is not authoritative and may be incomplete: judge each passage yourself, add it only where it supports or sharpens what you are writing, and leave the rest. To read a passage's Arabic before judging it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). Also add any other passage you now recall that belongs, whether listed or not. Then write your final output. No other command or tool is available.

===== _commentary/v16/prompts/r13/surah_images.md =====
Write the Turkish commentary on the images of this surah for a curious reader
who knows neither Arabic nor how lexical families work, and who already has the
plain meaning. The map is an earlier reader's proposal: its chains, members,
passages and interactions are your material, not your verdicts. Correct a
member that does not hold, merge chains that are one image, and add what the
map missed from your own knowledge of Arabic and the Quran.

For each image:

- Show the scene through its operation: what the objects are, how they work,
  what the act does. Never flatten a mechanism into a label.
- Say what it makes perceptible in the surah that a plain paraphrase could not.
- Go through the surah in order and show what each ayah's words add to it.
- Bring in the Quran passages that stage it, with the speaker, the situation
  as the Quran itself tells it there and in the neighbouring ayat, and the
  wording the connection needs.

Then show where the images meet: a scene that holds two of them, and how
together they carry the surah's movement.

Develop every chain of the map, unless its members fail; a chain you leave out
goes in the ledger with its reason. A family image is heard beside the word's
meaning in its ayah, never in place of it; say so once. Keep root identity,
family images and your own connections distinct; an echo root does not
establish identity. Never invent a sense, source, citation or chronology. Use
no hadith, no exegetes' views and no report from outside the Quran (no occasion
of revelation, no name the Quran does not give, no date): the Quran, the map's
dictionary phrases and Arabic usage carry the commentary. Name
no dictionary or lexicographer in the prose, never mention the dictionary
("sözlük"), the map, its chains or your own process, and do not hedge in the
first person.

Write continuous prose: one `##` section per image, then a `## Buluşmalar`
section for the meetings; explain, do not dramatize; no lists and no closing
recap. Every Arabic quotation goes in the reader tag, and every tag ends with
its source, so the reader can check it:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning, source:…}
- a dictionary phrase or a branch's sense: source:"<root letters>,<branch id>",
  e.g. source:"ق و م,B016";
- a Quran quotation: source:<surah:ayah>, e.g. source:72:16, the one ayah that
  holds the quoted words, no ranges;
- Arabic from your own memory that is not in the map's dictionary phrases:
  source:"memory".
A branch's sense given in Turkish without its Arabic, and a Quran passage named
without quoting it, carry the source alone: {source:"ق و م,B016"},
{source:15:41}. Outside the `Kaynaklar:` lines, never write a Quran reference
outside a tag; quote the surah's own words in tags too, and name its ayat in
words ("dördüncü ayet"). End each image section with one line, `Kaynaklar:`, giving its
members as ayah, word, root and branch (e.g. 1:6 ٱلْمُسْتَقِيمَ ق و م B012).

Output: the prose; then a line containing only
=== LEDGER ===
then, in plain English, one short line per item, a few words each:
- not developed: <chain> - <why>
- memory: <a claim about Arabic that neither the map nor the Quran text can check>

===== _commentary/v16/work/s114/surah.r2.nochannels/text.md =====
# Surah 114

- 114:1 قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ
- 114:2 مَلِكِ ٱلنَّاسِ
- 114:3 إِلَٰهِ ٱلنَّاسِ
- 114:4 مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ
- 114:5 ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ
- 114:6 مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ


===== _commentary/v16/out/s114/surah.map3.nochannels.hftbundle.tool/map.md (without ## Not carried) =====
## Chains

Passages marked (recalled) come from memory and were not read through the lookup. Every other passage was read through it.

### Visible and hidden: the people who appear, the beings who are covered

The surah ends on a pair that the dictionary defines by visibility. الإنس are named for appearing and الجن for being covered from eyes, and the dictionary states each against the other. ٱلنَّاسِ is said five times. The last time it stands beside ٱلْجِنَّةِ, and that contrast reflects back onto the four earlier ٱلنَّاسِ: the protected are the visible ones. The same human root also names perceiving by sight and by hearing, so the visible ones are also the perceivers. What works on them sits just below perception: a sound at the edge of hearing (ٱلْوَسْوَاسِ), and a mover who hides and contracts out of view (ٱلْخَنَّاسِ). The harm's own word, شَرِّ, holds in its root the reversal: spreading a thing out in the sun, and bringing a thing out into view. The evil is named by a root of exposure, and it belongs to one who hides.

- 114:1–3, 5, 6 ٱلنَّاسِ — ء ن س B001 — «الإنس خلاف الجن وسموا لظهورهم» (maqayis;mufradat) — the dictionary joins the surah's last two nouns in one phrase: the people are the ones who appear.
- 114:6 ٱلْجِنَّةِ — ج ن ن B005 — «الجن سموا بذلك لأنهم متسترون عن أعين الخلق» (maqayis); «الجن خلاف الإنس والواحد جني» (sihah); «الجنة جماعة الجن» (mufradat) — the counter-phrase: covered from created eyes. «الجنة» is the collective, the form that stands in the text.
- 114:6 ٱلْجِنَّةِ — ج ن ن B001 — «أصل الجن ستر الشيء عن الحاسة» (mufradat) — the root's operation: covering from the senses.
- 114:5, 6 ٱلنَّاسِ — ء ن س B002 — «آنست الشيء إذا رأيته وآنسته إذا سمعته» (maqayis); «آنسته أبصرته وآنست الصوت سمعته» (sihah) — the visible ones are also the ones who see and hear. The whisper is what they do not catch.
- 114:4 ٱلْوَسْوَاسِ — و س و س B002 — «الوسواس الصوت الخفي من ريح تهز قصبا ونحوه» (ayn); «وسوسة الشيء إذا سمعت حركته» (jamhara) — a hidden sound, heard only as a movement.
- 114:4 ٱلْخَنَّاسِ — خ ن س B001 — «أصل واحد يدل على استخفاء وتستر» (maqayis;mufradat;tahdhib) — hiding and taking cover.
- 114:4 شَرِّ — ش ر ر B008 — «أشررت الشيء إذا أبرزته وأظهرته» (maqayis) — bringing out and making visible: the reverse of the hider.
- 114:4 شَرِّ — ش ر ر B002 — «الشر بسطك الشيء في الشمس» (maqayis;ayn) — laying a thing out in the sun: exposure to light.

Quran:
- 7:20–22: the garden story (the scene opens at 7:19). The whisper works to bring out what was hidden (فَوَسْوَسَ لَهُمَا ٱلشَّيْطَٰنُ لِيُبْدِىَ لَهُمَا مَا وُۥرِىَ عَنْهُمَا). Then بَدَتْ لَهُمَا سَوْءَٰتُهُمَا: the hidden one's work ends in exposure.
- 7:27: God to the children of Adam. إِنَّهُۥ يَرَىٰكُمْ هُوَ وَقَبِيلُهُۥ مِنْ حَيْثُ لَا تَرَوْنَهُمْ: the covered one sees, and the visible ones do not see him.
- 72:6: the jinn who heard the Quran, reporting (the scene opens at 72:1). رِجَالٌۭ مِّنَ ٱلْإِنسِ يَعُوذُونَ بِرِجَالٍۢ مِّنَ ٱلْجِنِّ: ins, jinn and refuge in one ayah, with the refuge turned toward the hidden side.
- 6:112: God to the Prophet. شَيَٰطِينَ ٱلْإِنسِ وَٱلْجِنِّ يُوحِى بَعْضُهُمْ إِلَىٰ بَعْضٍۢ زُخْرُفَ ٱلْقَوْلِ: both classes are sources, as in 114:6.
- 11:119; 32:13 (recalled): God's decree, مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ أَجْمَعِينَ. The same pair in the same wording.
- 55:14–15 (recalled): the creation of الإنسان and الجان set side by side.
- 6:128 (recalled): God at the gathering, يَا مَعْشَرَ ٱلْجِنِّ قَدِ ٱسْتَكْثَرْتُم مِّنَ ٱلْإِنسِ.
- 41:29 (recalled): the deniers in the fire, أَرِنَا ٱلَّذَيْنِ أَضَلَّانَا مِنَ ٱلْجِنِّ وَٱلْإِنسِ. They ask to see the ones who led them astray.

### The chest and what is hidden in it

صُدُورِ in 114:5 is, in the dictionary, a bodily chamber. The root of ٱلْجِنَّةِ supplies the parts of that chamber: the chest's bones and rib-ends, the heart, and the act of hiding something in one's chest. The dictionary places whispering there in so many words: in the chest and in the heart. The root of مَلِكِ calls the heart the body's mainstay. The whisper is also defined as the self speaking to itself, and the human root has a phrase in which "son of your ins" means your own self. The human root also names asking leave before entering a house. The whisperer enters this chamber without asking.

- 114:5 صُدُورِ — ص د ر B001 — «الصدر للإنسان والجمع صدور» (maqayis); «الصدرة من الإنسان ما أشرف من أعلى صدره» (ayn;sihah;tahdhib) — the chamber and its raised front.
- 114:6 ٱلْجِنَّةِ — ج ن ن B016 — «الجناجن عظام الصدر» (maqayis); «الجنجن والجناجن أطراف الأضلاع مما يلي الصدر وعظم القلب» (ayn) — the dictionary joins this root with صدر: the rib-cage of the chest.
- 114:6 ٱلْجِنَّةِ — ج ن ن B010 — «الجنان القلب لكونه مستورا عن الحاسة» (mufradat); «الجنان روع القلب» (ayn;tahdhib) — the heart, named for being hidden from the senses.
- 114:6 ٱلْجِنَّةِ — ج ن ن B001 — «أجننت الشيء في صدري أكننته» (sihah) — the dictionary joins the root with صدر: hiding a thing in one's own chest.
- 114:5 يُوَسْوِسُ — و س و س B001 — «وسوس إلي ووسوس في صدري» (ayn); «الوسوسة ما يلقيه الشيطان في القلب» (jamhara) — the dictionary joins the whisper with the chest and the heart.
- 114:5 يُوَسْوِسُ — و س و س B001 — «الوسوسة حديث النفس» (ayn;sihah) — the voice inside speaks as the self speaks.
- 114:2 مَلِكِ — م ل ك B005 — «القلب ملاك الجسد» (ayn;sihah;mufradat) [fixed expression] — the heart is what holds the body up. The whisper goes for that point.
- 114:5 ٱلنَّاسِ — ء ن س B006 — «كيف ابن إنسك يعني نفسه» (sihah) — the human word folding back into one's own self.
- 114:1 قُلْ — ق و ل B012 — «في نفسي قول لم أظهره» (mufradat) [fixed expression] — a saying kept inside, not yet shown.
- 114:5 ٱلنَّاسِ — ء ن س B007 — «حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل» (tahdhib) — the asking of leave at the door. The whisperer's entry into the chests is the reverse.

Quran:
- 50:16: God on the creation of man. وَنَعْلَمُ مَا تُوَسْوِسُ بِهِۦ نَفْسُهُۥ ۖ وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ: the self's own whisper, and a nearness that is deeper still.
- 11:5: about those who hide. يَثْنُونَ صُدُورَهُمْ لِيَسْتَخْفُوا۟ … يَسْتَغْشُونَ ثِيَابَهُمْ … عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ: a chest folded to hide, a garment drawn over it, and what lies inside known all the same.
- 28:69 (recalled): مَا تُكِنُّ صُدُورُهُمْ وَمَا يُعْلِنُونَ. The dictionary's أكننته, said of chests.
- 22:46 (recalled): ٱلْقُلُوبُ ٱلَّتِى فِى ٱلصُّدُورِ. The heart inside the chest.
- 3:154 (recalled): after Uhud, God tests مَا فِى صُدُورِكُمْ and purifies مَا فِى قُلُوبِكُمْ.
- 40:56: إِن فِى صُدُورِهِمْ إِلَّا كِبْرٌۭ … فَٱسْتَعِذْ بِٱللَّهِ. What sits in the chests, answered by refuge.
- 100:10: وَحُصِّلَ مَا فِى ٱلصُّدُورِ. At the end, what is in the chests is brought out.
- 24:27: the command not to enter houses حَتَّىٰ تَسْتَأْنِسُوا۟ وَتُسَلِّمُوا۟.

### Speech: formed inside, brought out on the tongue, spread among people, whispered back in

The surah opens with قُلْ. The dictionary defines a saying as what is "brought out by pronunciation", and defines the same root's inner side as what is formed in the self before being brought out. The root also names the tongue, talk spreading among people, drawing a saying of good or evil onto oneself, a false saying laid on someone, a back-and-forth of talk, and an inner prompting that is called a saying although nothing was said aloud. Against all this stands the whisper: self-talk, a hidden sound, half-voiced. Speech in this surah moves along one path in two directions. The refuge is formed inside and brought out on the tongue. The whisper comes in the other way, into chests, and 114:6 says it comes from people as well as from jinn: the talk that spreads among people.

- 114:1 قُلْ — ق و ل B001 — «المركب من الحروف المبرز بالنطق» (mufradat) — speech brought out by uttering it: the commanded refuge is spoken.
- 114:1 قُلْ — ق و ل B012 — «المتصور في النفس قبل الإبراز باللفظ قول» (mufradat) [fixed expression] — the same saying while it is still inside, before it is brought out.
- 114:1 قُلْ — ق و ل B002 — «المقول اللسان» (maqayis;ayn;sihah) — the organ of the saying.
- 114:1 قُلْ — ق و ل B007 — «القالة القول الفاشي في الناس» (ayn); «كثرت قالة الناس» (sihah) — the dictionary joins قول with الناس: talk spreading among people, the human channel of 114:6.
- 114:1 قُلْ — ق و ل B006 — «اقتال قولا أي اجتر إلى نفسه قولا من خير أو شر» (ayn) [fixed expression] — the dictionary joins قول with شر: drawing a saying of good or of evil onto oneself.
- 114:1 قُلْ — ق و ل B017 — «في الإلهام فإن ذلك لم يكن بخطاب ورد عليه بل كان ذلك إلهاما فسماه قولا» (mufradat) — an inward prompting called a saying although no address came. It is the good twin of the whisper.
- 114:1 قُلْ — ق و ل B009 — «قاولته في أمره وتقاولنا أي تفاوضنا» (sihah) [fixed expression] — talk going back and forth. The whisper in the Quran comes as a dialogue with an offer (7:20–21, 20:120).
- 114:1 قُلْ — ق و ل B005 — «تقول عليه أي كذب عليه» (sihah) [fixed expression] — a false saying laid on someone.
- 114:4, 5 ٱلْوَسْوَاسِ / يُوَسْوِسُ — و س و س B001 — «الوسوسة حديث النفس؛ وسوست إليه نفسه» (sihah) — speech that stays inside.
- 114:4 ٱلْوَسْوَاسِ — و س و س B002 — «صوت الحلي والهمس الخفي» (mufradat) — speech reduced to a murmur.
- 114:4 شَرِّ — ش ر ر B008 — «أشررت الشيء أظهرته» (sihah) — bringing out. The dictionary uses the same verb of bringing out (إبراز) for the spoken word in ق و ل B001 and B012 and for this root in maqayis («أبرزته»).
- 114:6 وَٱلنَّاسِ — ء ن س B002 — «آنست الصوت سمعته» (sihah) — the hearer at the far end of the path.

Quran:
- 23:97–98: God to the Prophet. وَقُل رَّبِّ أَعُوذُ بِكَ مِنْ هَمَزَٰتِ ٱلشَّيَٰطِينِ: the same frame as 114:1, a command to say, refuge, and رب.
- 16:98–100: فَإِذَا قَرَأْتَ ٱلْقُرْءَانَ فَٱسْتَعِذْ بِٱللَّهِ. Recited speech opens with refuge, and the satan's سلطان follows in the next two ayat.
- 6:112–113: God to the Prophet. Devils of ins and jinn inspire one another with زُخْرُفَ ٱلْقَوْلِ, and the hearts of those who disbelieve incline to it.
- 6:121: وَإِنَّ ٱلشَّيَٰطِينَ لَيُوحُونَ إِلَىٰٓ أَوْلِيَآئِهِمْ لِيُجَٰدِلُوكُمْ. Hidden speech coming out as human argument.
- 81:25: وَمَا هُوَ بِقَوْلِ شَيْطَٰنٍۢ رَّجِيمٍۢ. The revealed saying is not a satan's saying. The scene opens at the oath by the خُنَّس (81:15), and 81:19 (recalled) has إِنَّهُۥ لَقَوْلُ رَسُولٍۢ كَرِيمٍۢ.
- 7:20–21: the whisper turns into speech (وَقَالَ مَا نَهَىٰكُمَا) and into a sworn exchange (وَقَاسَمَهُمَآ).
- 20:120: فَوَسْوَسَ إِلَيْهِ ٱلشَّيْطَٰنُ قَالَ يَٰٓـَٔادَمُ هَلْ أَدُلُّكَ. The whisper takes the form of an offer.
- 69:44 (recalled) and 52:33 (recalled): وَلَوْ تَقَوَّلَ عَلَيْنَا and أَمْ يَقُولُونَ تَقَوَّلَهُۥ. ق و ل B005 in the Quran, as an accusation against the messenger.
- 58:10: إِنَّمَا ٱلنَّجْوَىٰ مِنَ ٱلشَّيْطَٰنِ. Secret talk among people.
- 17:53 (recalled): وَقُل لِّعِبَادِى يَقُولُوا۟ ٱلَّتِى هِىَ أَحْسَنُ إِنَّ ٱلشَّيْطَٰنَ يَنزَغُ بَيْنَهُمْ. Speech among people, and the devil working between them.
- 24:15 (recalled): the slander, إِذْ تَلَقَّوْنَهُۥ بِأَلْسِنَتِكُمْ وَتَقُولُونَ بِأَفْوَاهِكُم. Talk spreading tongue to tongue.

### Withdrawal and return; the one who stays

ٱلْخَنَّاسِ is the one who draws back. He contracts, falls behind, and slips away unseen. The dictionary joins him to the whisper in one phrase: he whispers, and when God is remembered he draws back. The stars of the same root hide by day and come back in their courses, so his withdrawal is a phase, not an ending. The verb يُوَسْوِسُ is reduplicated (و س و س). That is a sound made of a repeated movement; this is from my own knowledge of the form, and the dictionary gives the movement-sound in B002. Against the one who comes and goes stand two things. The root of the Lord's title holds staying in a place and not leaving it, and a cloud that lasts. The refuge root holds what clings to a thing and keeps to it, like meat on the bone. Refuge also turns, in reverse, into leaving someone out of aversion, and into escaping an attack that frightened or struck but did not kill.

- 114:4 ٱلْخَنَّاسِ — خ ن س B001 — «الخنوس الانقباض والاستخفاء؛ الشيطان يوسوس فإذا ذكر الله خنس» (ayn;tahdhib;mufradat) — the dictionary joins the surah's two words: whispering, then drawing back at remembrance.
- 114:4 ٱلْخَنَّاسِ — خ ن س B001 — «خنس عنه يخنس أي تأخر؛ خنسته فخنس أي أخرته فتأخر وقبضته فانقبض» (sihah;tahdhib) — falling back and contracting.
- 114:4 ٱلْخَنَّاسِ — خ ن س B001 — «خنس الرجل عن القوم إذا مضى في خفية» (jamhara) — leaving the company unseen.
- 114:4 ٱلْخَنَّاسِ — خ ن س B002 — «الكواكب التي تخنس بالنهار؛ تخنس في مجراها أي ترجع» (mufradat) — hiding, then turning back in its course: the return.
- 114:4–5 ٱلْوَسْوَاسِ / يُوَسْوِسُ — و س و س B002 — «وسوسة الشيء إذا سمعت حركته» (jamhara) — a movement heard as sound. The doubled root (my own knowledge) makes it a repeated movement.
- 114:1 بِرَبِّ — ر ب ب B007 — «رب بالمكان وأرب إذا أقام به» (jamhara); «أرب فلان بالمكان إذا أقام به فلم يبرحه» (tahdhib) — the one who stays and does not leave.
- 114:1 بِرَبِّ — ر ب ب B007 — «أربت الجنوب والسحابة أي دامت» (sihah) — lasting.
- 114:1 أَعُوذُ — ع و ذ B004 — «كل شيء لصق بشيء أو لازمه» (maqayis); «أطيب اللحم عوذه وهو ما عاذ بالعظم ولزمه» (sihah) — the seeker clings and keeps close.
- 114:1 أَعُوذُ — ع و ذ B008 — «ما تركت فلانا إلا عوذا منه بالتحريك وعواذا منه أي كراهة» (sihah) [fixed expression] — the seeker's turning away, out of dislike.
- 114:1 أَعُوذُ — ع و ذ B006 — «أفلت منه فلان عوذا إذا خوفه ولم يضربه أو ضربه وهو يريد قتله فلم يقتله» (sihah) [fixed expression] — the attack that frightens or strikes but does not kill. The refuge is an escape, not the attacker's end.

Quran:
- 81:15–17: God's oath. فَلَآ أُقْسِمُ بِٱلْخُنَّسِ ٱلْجَوَارِ ٱلْكُنَّسِ وَٱلَّيْلِ إِذَا عَسْعَسَ: those that draw back, run and go into their covert.
- 7:200–201: refuge commanded, then إِذَا مَسَّهُمْ طَٰٓئِفٌۭ مِّنَ ٱلشَّيْطَٰنِ تَذَكَّرُوا۟ فَإِذَا هُم مُّبْصِرُونَ. The dictionary's "when God is remembered he draws back", staged.
- 41:36: the same command, وَإِمَّا يَنزَغَنَّكَ مِنَ ٱلشَّيْطَٰنِ نَزْغٌۭ فَٱسْتَعِذْ بِٱللَّهِ.
- 8:48: Satan at Badr. He says إِنِّى جَارٌۭ لَّكُمْ, then نَكَصَ عَلَىٰ عَقِبَيْهِ وَقَالَ إِنِّى بَرِىٓءٌۭ مِّنكُمْ. He draws back at the moment of meeting.
- 59:16 (recalled): Satan tells man اكْفُرْ, then says إِنِّى بَرِىٓءٌۭ مِّنكَ.
- 14:22: Satan's speech after judgment. وَمَا كَانَ لِىَ عَلَيْكُم مِّن سُلْطَٰنٍ إِلَّآ أَن دَعَوْتُكُمْ: he called, and he steps back.
- 43:36–37: whoever turns from the remembrance of the Merciful gets a satan as قَرِين. The reverse case: without remembrance the whisperer stays.
- 58:19: ٱسْتَحْوَذَ عَلَيْهِمُ ٱلشَّيْطَٰنُ فَأَنسَىٰهُمْ ذِكْرَ ٱللَّهِ. Where remembrance is gone, he takes hold.

### Refuge: the spoken charm and the coverings of the body

أَعُوذُ is taking shelter with someone and holding on to him. The dictionary joins the verb to the Lord in one phrase: عاذ فلان بربه. The same root names the charm a person takes shelter in, whether a spoken incantation or a written amulet hung on the person, "against fright or madness". It also names the spot on the horse's neck where the necklace hangs. The surah's other words supply the other coverings: a garment that hides a person, a mail coat and shield, a garment over the chest, and a place to hide in. The commanded saying is itself the spoken charm. The attacker sits inside the chest, under every cover. ٱلْجِنَّةِ names both sides: the covered attacker and the shield.

- 114:1 أَعُوذُ — ع و ذ B001 — «عاذ فلان بربه يعوذ عوذا إذا لجأ إليه واعتصم به» (tahdhib) — the dictionary joins أعوذ and رب: taking shelter with one's Lord and holding fast.
- 114:1 أَعُوذُ — ع و ذ B001 — «عذت بفلان واستعذت به أي لجأت إليه وهو عياذي أي ملجئي» (sihah) — the protector as the place one runs to.
- 114:1 أَعُوذُ — ع و ذ B002 — «العوذة ما يعاذ به من الشيء ومنه قيل للتميمة والرقية عوذة» (mufradat) — the spoken incantation as a refuge. قُلْ أَعُوذُ is one.
- 114:1 أَعُوذُ — ع و ذ B002 — «التعاويذ التي تكتب وتعلق على الإنسان من العين تسمى المعاذات» (tahdhib) — the written charm hung on the body.
- 114:1 أَعُوذُ — ع و ذ B002 — «العوذة والمعاذة التي يعوذ بها الإنسان من فزع أو جنون» (maqayis) — the dictionary joins the charm with جنون, the root of ٱلْجِنَّةِ.
- 114:1 أَعُوذُ — ع و ذ B005 — «معوذ الفرس موضع القلادة» (sihah) — the place on the body where the necklace or charm is worn.
- 114:1 أَعُوذُ — ع و ذ B007 — «تعاوذ القوم في الحرب إذا تواكلوا وعاذ بعضهم ببعض» (tahdhib) — fighters leaning on one another for shelter, refuge given sideways instead of upward (compare 72:6).
- 114:1 قُلْ — ق و ل B002 — «المقول اللسان» (maqayis;ayn;sihah) — the tongue that carries the charm.
- 114:1 بِرَبِّ — ر ب ب B001 — «يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح» (tahdhib) — the one sheltered with owns, is obeyed, and sets things right.
- 114:6 ٱلْجِنَّةِ — ج ن ن B008 — «المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك» (ayn) — shield and mail: whatever protects you is your جنة.
- 114:6 ٱلْجِنَّةِ — ج ن ن B001 — «ما علي جنان إلا ما ترى أي ثوب يواريني» (sihah;tahdhib) — the garment that covers a person.
- 114:6 ٱلْجِنَّةِ — ج ن ن B017 — «المجنة أيضا الموضع الذي يستتر فيه» (sihah) — a place to hide in.
- 114:5 صُدُورِ — ص د ر B001 — «الصدار ثوب يغطي الصدر» (maqayis;ayn;tahdhib;mufradat) — the garment over the chest: an outer cover over the chamber where the whisper works.

Quran:
- 23:97–98: God to the Prophet. وَقُل رَّبِّ أَعُوذُ بِكَ … وَأَعُوذُ بِكَ رَبِّ أَن يَحْضُرُونِ: a spoken refuge with its Lord.
- 113:1 (recalled): the twin surah, قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ.
- 3:36: the wife of Imran at the birth (the scene opens at 3:35). وَإِنِّىٓ أُعِيذُهَا بِكَ وَذُرِّيَّتَهَا مِنَ ٱلشَّيْطَٰنِ ٱلرَّجِيمِ.
- 12:23: Yusuf in the house with its doors shut. مَعَاذَ ٱللَّهِ ۖ إِنَّهُۥ رَبِّىٓ أَحْسَنَ مَثْوَاىَ: refuge, رب and a dwelling in one reply.
- 19:18 (recalled): Maryam to the spirit, إِنِّىٓ أَعُوذُ بِٱلرَّحْمَٰنِ مِنكَ.
- 72:6: men of ins taking refuge with men of jinn, and it only increased their burden. Refuge pointed the wrong way.
- 8:48: Satan offering himself as protector (إِنِّى جَارٌۭ لَّكُمْ), then drawing back.
- 58:16; 63:2: the hypocrites ٱتَّخَذُوٓا۟ أَيْمَٰنَهُمْ جُنَّةًۭ. Oaths used as a shield (ج ن ن B008), and with them فَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ.
- 7:26–27: God to the children of Adam. A garment that covers (لِبَاسًۭا يُوَٰرِى سَوْءَٰتِكُمْ) and لِبَاسُ ٱلتَّقْوَىٰ, then the satan stripping the garment, seeing from where he is not seen.

### Mother and young: hidden in the womb, born, kept close, raised to completion

Two words of the opening ayah, أَعُوذُ and بِرَبِّ, each name in the dictionary the mother who has just given birth. عائذ is any female for seven days after delivery, and the dictionary names the young of gazelles, camels and horses. ربّى is the ewe that has just delivered and is kept at home for her milk. The root of بِرَبِّ also names the foster parent and the stage-by-stage raising of a thing to completion. The root of ٱلْجِنَّةِ names the child hidden in the belly and the first beginning of youth. The root cited as a documented alternative for إِلَٰهِ (و ل ه, Abū'l-Haytham via Azharī) names the mother camel's grief for her young and forbids separating a mother from her child. The scene runs: the hidden child, the birth, the mother who stays by it, separation forbidden, and the carer who raises it stage by stage. Heard this way, "I take refuge" is the young keeping to the one who bore and raises it. From memory, not from this dictionary: classical explanations of عائذ say the young takes refuge with her, or that she keeps to her young.

- 114:6 ٱلْجِنَّةِ — ج ن ن B007 — «الجنين الولد في بطن أمه» (maqayis); «الجنين الولد ما دام في البطن» (sihah) — the child hidden in the womb.
- 114:1 أَعُوذُ — ع و ذ B003 — «كل أنثى عائذ إذا وضعت مدة سبعة أيام والجميع عوذ» (ayn); «العوذ الحديثات النتاج من الظباء والإبل والخيل واحدتها عائذ» (sihah); «الناقة إذا وضعت ولدها فهي عائذ أياما» (tahdhib) — the mother just delivered, staying with her young.
- 114:1 بِرَبِّ — ر ب ب B009 — «الربى: الشاة التي وضعت حديثا؛ قرب العهد بالولادة» (sihah); «الشاة الربي التي تحتبس في البيت للبن» (maqayis) — the same moment, under the Lord's root: the newly delivered ewe, kept at home for milk.
- 114:1 بِرَبِّ — ر ب ب B005 — «الراب: زوج الأم؛ الرابة: امرأة الأب؛ ربيب الرجل: ابن امرأته من غيره؛ الربيبة: الحاضنة» (sihah); «الراب والرابة بأحد الزوجين إذا تولى تربية الولد» (mufradat) — the carer who takes on a child's raising.
- 114:1 بِرَبِّ — ر ب ب B002 — «التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام» (mufradat); «رب فلان ولده؛ رباه» (sihah) — raising stage by stage to completion.
- 114:6 ٱلْجِنَّةِ — ج ن ن B014 — «كان ذلك في جن شبابه أي في أول شبابه» (sihah); 114:1 بِرَبِّ — ر ب ب B009 — «الربى: أول الشباب» (tahdhib) — both roots name the first freshness of youth.
- 114:3 إِلَٰهِ — و ل ه B002 (documented alternative) — «لا توله والدة عن ولدها» (maqayis;tahdhib); «كل أنثى فارقت ولدها فهي واله» (tahdhib) — the separation that is forbidden.
- 114:3 إِلَٰهِ — و ل ه B001 (documented alternative) — «ناقة واله إذا اشتد وجدها على ولدها» (sihah); «ولهت إليه تله أن تحن إليه» (tahdhib) — the mother's yearning, and yearning toward someone.

Quran:
- 3:35–37: the wife of Imran (رَبِّ إِنِّى نَذَرْتُ لَكَ مَا فِى بَطْنِى). At the birth she seeks refuge for the newborn, أُعِيذُهَا بِكَ. Then فَتَقَبَّلَهَا رَبُّهَا … وَأَنۢبَتَهَا نَبَاتًا حَسَنًۭا وَكَفَّلَهَا زَكَرِيَّا: womb, refuge, رب, raising and a guardian in one scene.
- 39:6: God. يَخْلُقُكُمْ فِى بُطُونِ أُمَّهَٰتِكُمْ … فِى ظُلُمَٰتٍۢ ثَلَٰثٍۢ ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ لَهُ ٱلْمُلْكُ ۖ لَآ إِلَٰهَ إِلَّا هُوَ. Formation hidden in darkness, followed by the three relations of 114:1–3.
- 53:32: وَإِذْ أَنتُمْ أَجِنَّةٌۭ فِى بُطُونِ أُمَّهَٰتِكُمْ. The plural of جنين, with إِنَّ رَبَّكَ in the same ayah.
- 4:23: وَرَبَٰٓئِبُكُمُ ٱلَّٰتِى فِى حُجُورِكُم. The ربيبة in the lap.
- 26:18: Pharaoh to Musa, أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا. A rival raiser, who also claims lordship (79:24).
- 28:7, 12–13 (recalled): Musa's mother. Separation, then فَرَدَدْنَٰهُ إِلَىٰٓ أُمِّهِۦ كَىْ تَقَرَّ عَيْنُهَا: the forbidden separation undone.
- 17:24 (recalled): رَّبِّ ٱرْحَمْهُمَا كَمَا رَبَّيَانِى صَغِيرًۭا.

### Lord, King, God and their lesser holders

114:1–3 stacks three titles over one unchanging object. In the dictionary, each title's root also covers lesser or false holders. رب is the owner of anything, and was said of a king in the Jahiliyya. مَلِك is what people make someone over themselves. The root of the surah's first word, قُلْ, holds the قَيْل, a Himyarite king "below the greatest king", called so because his word is carried out. إله is any object of worship, including idols and the sun. The dictionary itself narrows each title to God: the absolute رب, the ملك that belongs to God. Against this the whisperer offers a counterfeit kingship (20:120), and the evil's root holds the self thrown wholesale onto what it wants. The scene is a court of claimants (owners, petty kings, idols, the sun) and the one who holds all three titles over the people.

- 114:1 بِرَبِّ — ر ب ب B001 — «رب كل شئ: مالكه؛ وقد قالوه في الجاهلية للملك» (sihah) — the dictionary joins رب and ملك: the title given to human kings.
- 114:1 بِرَبِّ — ر ب ب B001 — «لا يقال الرب مطلقا إلا لله؛ رب الدار ورب الفرس» (mufradat) — lord of a house or a horse in lesser use. Unqualified, only God.
- 114:1 بِرَبِّ — ر ب ب B001 — «رببت القوم: سستهم» (sihah) — managing a people.
- 114:2 مَلِكِ — م ل ك B003 — «الملك لله المالك المليك» (ayn); «المملكة سلطان الملك في رعيته» (ayn;tahdhib); «الملك هو المتصرف بالأمر والنهي في الجمهور» (mufradat) — sovereignty as سلطان over subjects, commanding and forbidding.
- 114:2 مَلِكِ — م ل ك B003 — «ملك القوم فلانا وأملكوه على أنفسهم أي صيروه ملكا» (tahdhib) — kings that people make for themselves.
- 114:2 مَلِكِ — م ل ك B002 — «الملك ما ملكت اليد من مال وخول» (ayn;tahdhib) — what the hand owns.
- 114:1 قُلْ — ق و ل B004 — «القيل ملك من ملوك حمير دون الملك الأعظم والمرأة قيلة» (sihah); «كأنه الذي له قول أي ينفذ قوله» (sihah) — the dictionary joins قول and ملك: a lesser king, named for the word that is carried out.
- 114:3 إِلَٰهِ — ء ل ه B001 — «لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس» (tahdhib); «إله اسما لكل معبود» (mufradat) — the title held by idols and the sun.
- 114:3 إِلَٰهِ — ء ل ه B002 — «الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى» (mufradat) — the common noun made particular.
- 114:4 شَرِّ — ش ر ر B007 — «ألقى عليه شراشره إذا ألقى عليه نفسه حرصا ومحبة» (maqayis); «جمع ما انتشر من هممه لهذا الشيء وشغل همومه كلها به» (maqayis) — the whole self gathered and thrown onto one object: what worship asks for, and what a rival claims.

Quran:
- 79:24: Pharaoh, أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ.
- 28:38: Pharaoh, مَا عَلِمْتُ لَكُم مِّنْ إِلَٰهٍ غَيْرِى.
- 26:18: Pharaoh's claim to have raised Musa.
- 12:39: Yusuf to his two prison companions, ءَأَرْبَابٌۭ مُّتَفَرِّقُونَ خَيْرٌ أَمِ ٱللَّهُ ٱلْوَٰحِدُ ٱلْقَهَّارُ.
- 9:31 (recalled): ٱتَّخَذُوٓا۟ أَحْبَارَهُمْ وَرُهْبَٰنَهُمْ أَرْبَابًۭا مِّن دُونِ ٱللَّهِ.
- 3:64: the address to the People of the Book, وَلَا يَتَّخِذَ بَعْضُنَا بَعْضًا أَرْبَابًۭا.
- 2:258 (recalled): Ibrahim and the one to whom God gave ٱلْمُلْك. رَبِّىَ ٱلَّذِى يُحْىِۦ وَيُمِيتُ, then the sun from the east.
- 25:43: مَنِ ٱتَّخَذَ إِلَٰهَهُۥ هَوَىٰهُ. A god inside the self.
- 20:120: the whisper's offer, شَجَرَةِ ٱلْخُلْدِ وَمُلْكٍۢ لَّا يَبْلَىٰ. A counterfeit kingship.
- 7:20: إِلَّآ أَن تَكُونَا مَلَكَيْنِ, the whisper again bending toward the م ل ك word.
- 16:99–100: إِنَّهُۥ لَيْسَ لَهُۥ سُلْطَٰنٌ عَلَى ٱلَّذِينَ ءَامَنُوا۟ وَعَلَىٰ رَبِّهِمْ يَتَوَكَّلُونَ. The whisperer's سلطان, the dictionary's word for a king's reach over his subjects, denied over those who rely on their رب.
- 17:65: God to Iblis (the scene opens at 17:61), إِنَّ عِبَادِى لَيْسَ لَكَ عَلَيْهِمْ سُلْطَٰنٌۭ ۚ وَكَفَىٰ بِرَبِّكَ وَكِيلًۭا.
- 36:60: أَلَمْ أَعْهَدْ إِلَيْكُمْ … أَن لَّا تَعْبُدُوا۟ ٱلشَّيْطَٰنَ. The whisperer as a would-be object of worship.
- 1:2–4 (recalled): رَبِّ ٱلْعَٰلَمِينَ … مَٰلِكِ يَوْمِ ٱلدِّينِ. The opening surah's pair of titles.
- 20:114 (recalled): فَتَعَٰلَى ٱللَّهُ ٱلْمَلِكُ ٱلْحَقُّ.
- 59:23 (recalled): ٱلْمَلِكُ ٱلْقُدُّوسُ.
- 40:16 (recalled): لِّمَنِ ٱلْمُلْكُ ٱلْيَوْمَ.

### Binding into one, and cutting apart

The root of مَلِكِ starts from firmness: dough kneaded tight, a wall that holds together, and kingship named from a hand that is strong in what it holds. The root of بِرَبِّ gathers: a pouch that holds the arrows together, five tribes gathered into one, thousands of people, much water named for its gathering, a tight knot, a covenant that binds parties. ٱلنَّاسِ is "the gathering of people". ٱلْجِنَّةِ names the bulk of the people, in which each person disappears. Against this, the evil's root cuts a thing into pieces, and names a quarrel. The process: many held as one by a binder, or cut apart.

- 114:2 مَلِكِ — م ل ك B001 — «ملكت العجين إذا شددت عجنه» (sihah); «حائط ليس له ملاك أي تماسك» (mufradat); «أصل صحيح يدل على قوة في الشيء وصحة» (maqayis) — tight dough, a wall that coheres.
- 114:2 مَلِكِ — م ل ك B003 — «والاسم الملك لأن يده فيه قوية صحيحة» (maqayis) — kingship as a hand that holds firm.
- 114:1 بِرَبِّ — ر ب ب B010 — «الربابة شبيهة بالكنانة تجمع فيها سهام الميسر؛ جماعة السهام» (sihah) — the pouch gathering the arrows.
- 114:1 بِرَبِّ — ر ب ب B004 — «الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا» (sihah) — the dictionary joins this root with الناس: thousands of people, tribes gathered into one.
- 114:1 بِرَبِّ — ر ب ب B016 — «الربى: العقدة المحكمة» (tahdhib) — the tight knot.
- 114:1 بِرَبِّ — ر ب ب B011 — «الربابة: العهد والميثاق؛ الأربة أهل الميثاق» (sihah); «العقد في موالاة الغير: الربابة» (mufradat) — the covenant that binds.
- 114:1 بِرَبِّ — ر ب ب B013 — «الربب وهو الماء الكثير سمي بذلك لاجتماعه» (maqayis) — water named for being gathered.
- 114:1–6 ٱلنَّاسِ — ء ن س B001 — «الإنس جماعة الناس والأناسي جماع» (tahdhib) — the people as a gathering.
- 114:6 ٱلْجِنَّةِ — ج ن ن B013 — «جنان الناس معظمهم ويسمى السواد» (maqayis); «جنان الناس دهماؤهم» (sihah) — the dictionary joins this root with الناس: the dark bulk of the people, in which individuals are covered.
- 114:4 شَرِّ — ش ر ر B004 — «شرشر الشيء إذا قطعه» (maqayis); «شرشرة الشيء تشقيقه وتقطيعه» (sihah) — splitting and cutting into pieces.
- 114:4 شَرِّ — ش ر ر B011 — «المشارة المخاصمة» (sihah) — quarrel.

Quran:
- 3:103: وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا وَلَا تَفَرَّقُوا۟ … فَأَلَّفَ بَيْنَ قُلُوبِكُمْ. اعتصم is the dictionary's own gloss of عاذ (عاذ … بربه … واعتصم به).
- 5:90 (recalled) and 5:91: the ميسر and the divining arrows are the satan's work. إِنَّمَا يُرِيدُ ٱلشَّيْطَٰنُ أَن يُوقِعَ بَيْنَكُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ: the arrows the ربابة holds together become the game that divides.
- 3:146: رِبِّيُّونَ كَثِيرٌۭ fighting beside prophets, and they did not weaken. The gathered thousands of B004.
- 12:39: أَرْبَابٌۭ مُّتَفَرِّقُونَ against ٱلْوَٰحِد.
- 21:22: لَوْ كَانَ فِيهِمَآ ءَالِهَةٌ إِلَّا ٱللَّهُ لَفَسَدَتَا.
- 23:91: إِذًۭا لَّذَهَبَ كُلُّ إِلَٰهٍۭ بِمَا خَلَقَ. Many gods, a world pulled apart.
- 7:172: the covenant. أَلَسْتُ بِرَبِّكُمْ ۖ قَالُوا۟ بَلَىٰ.
- 36:60–61: the covenant (أَلَمْ أَعْهَدْ إِلَيْكُمْ) against worshipping the satan.
- 7:21: the satan's counter-oath, وَقَاسَمَهُمَآ.
- 113:4 (recalled): ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ in the twin surah. Knots blown on, set against the tight knot of ر ب ب B016.

### Night, the hiding stars, the sun, and the fire seen in the dark

الخُنَّس are the planets that run, hide by day when the sun's light covers them, set, and come back. The root of ٱلْجِنَّةِ names night's black covering of things. The root of إِلَٰهِ names the sun, called إلاهة because some people worshipped it. The evil's root names spreading a thing in the sun, and the sparks flying from a fire. The human root names glimpsing a fire, and the small figure seen in the black of the eye. The root of بِرَبِّ names staying without leaving. The scene: night covers everything; planets appear, run, hide and return; the sun rises; a fire is glimpsed and sparks fly; an eye watches; and among the lights that set, one asks which is Lord. The Quran stages exactly this in Ibrahim's night (6:76–79). The dictionary uses السواد for three of the surah's words: the black of the eye where the إنسان appears, the black of night (جنان الليل), and the dark bulk of people (جنان الناس).

- 114:4 ٱلْخَنَّاسِ — خ ن س B002 — «الخنس الكواكب الخمسة التي تجري وتخنس في مجراها حتى يخفى ضوء الشمس وخنوسها اختفاؤها بالنهار» (ayn); «الخنس النجوم تخنس في المغيب» (maqayis;jamhara) — planets that run, hide in daylight, set.
- 114:6 ٱلْجِنَّةِ — ج ن ن B002 — «جنان الليل سواده وستره الأشياء» (maqayis); «أجنه الليل وجن عليه الليل إذا أظلم حتى يستره بظلمته» (ayn) — night covering everything.
- 114:3 إِلَٰهِ — ء ل ه B001 — «والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها» (maqayis) — the sun, named for having been worshipped.
- 114:4 شَرِّ — ش ر ر B002 — «شررت الثوب بسطته في الشمس» (sihah) — spreading a garment in the sun.
- 114:4 شَرِّ — ش ر ر B003 — «الشرر ما تطاير من النار الواحدة شررة» (maqayis) — sparks flying from a fire.
- 114:1–6 ٱلنَّاسِ — ء ن س B002 — «آنس من جانب يعني أبصر نارا» (tahdhib); «فإن آنستم منهم رشدا أي أبصرتم وآنست نارا» (mufradat) — glimpsing a fire in the dark.
- 114:1–6 ٱلنَّاسِ — ء ن س B005 — «إنسان العين المثال الذي يرى في السواد أي سواد العين» (sihah) — the small figure in the black of the eye: the watcher.
- 114:1–6 ٱلنَّاسِ — ء ن س B003 — «الأنيس المؤانس وكل ما يؤنس به» (sihah) — whatever gives company. The branch label's gloss counts among these the fire that reassures the night traveller. The Arabic phrase quoted here is general.
- 114:1 بِرَبِّ — ر ب ب B007 — «أرب فلان بالمكان إذا أقام به فلم يبرحه» (tahdhib) — the one who does not set.
- 114:2 مَلِكِ — م ل ك B003 — «الملكوت ملك الله وملكوت الله سلطانه» (ayn) — the ملكوت that is shown to Ibrahim before his night (6:75).

Quran:
- 6:74–79: Ibrahim and his father and people. 6:74 is about idols as آلهة, and 6:75 shows him مَلَكُوتَ ٱلسَّمَٰوَٰتِ. Then فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ رَءَا كَوْكَبًۭا ۖ قَالَ هَٰذَا رَبِّى ۖ فَلَمَّآ أَفَلَ قَالَ لَآ أُحِبُّ ٱلْءَافِلِينَ, the moon, the sun بَازِغَةًۭ, and the turn to the one who made the heavens. The Quran joins جن الليل, a planet, setting and the question of the رب.
- 81:15–18: God's oath by ٱلْخُنَّسِ ٱلْجَوَارِ ٱلْكُنَّسِ, by night as it closes in and dawn as it breathes. The same passage goes on to مَجْنُون (81:22) and قَوْلِ شَيْطَٰن (81:25).
- 41:37 (recalled): لَا تَسْجُدُوا۟ لِلشَّمْسِ وَلَا لِلْقَمَرِ.
- 27:24 (recalled): the hoopoe on Sheba. يَسْجُدُونَ لِلشَّمْسِ … وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ فَصَدَّهُمْ عَنِ ٱلسَّبِيلِ: sun-worship led by the satan.
- 37:7–10: stars as a guard against every rebel satan. Whoever snatches a hearing is followed by شِهَابٌۭ ثَاقِبٌۭ: hidden listeners and fire in the night sky.
- 72:8–9: the jinn speaking. The sky مُلِئَتْ حَرَسًۭا شَدِيدًۭا وَشُهُبًۭا.
- 67:5 (recalled) and 15:17–18: the same guard.
- 20:10: Musa, إِنِّىٓ ءَانَسْتُ نَارًۭا … أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى. ء ن س B002 itself, a fire glimpsed in the dark.
- 28:29 (recalled): ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا.
- 77:32 (recalled): إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ. Sparks.

### The hunt: the murmur, the covert, the wary animal, the sheltered plant

The dictionary's وسواس is the hunter's murmur and the sounds of his dogs, the jingle of ornaments, wind shaking reeds. الخنس is the gazelles' covert, and the gazelles themselves. All cattle are snub-nosed (خنس), and the root of بِرَبِّ names a herd of wild cattle. The refuge root names the does that have just given birth, and a plant at the root of the thorns where grazing animals cannot reach it. The human root names the wary animal looking about when it senses what alarms it, and sets the tame against the wild. The scene: a hunter creeps up with a low murmur; game keeps to its covert; the wary one senses and looks about; the plant grows safe among thorns. The whisperer is the murmuring hunter, and by his name also the one who keeps to the covert. The people are the ones who must sense. The refuge is the place out of reach.

- 114:4 ٱلْوَسْوَاسِ — و س و س B002 — «همس الصائد والكلاب وأصوات الحلى وسواس» (sihah); «همس الصائد وكلامه» (ayn) — the hunter's murmur and his dogs.
- 114:4 ٱلْوَسْوَاسِ — و س و س B002 — «الوسواس الصوت الخفي من ريح تهز قصبا ونحوه» (ayn) — the rustle in the reeds where game lies.
- 114:4 ٱلْخَنَّاسِ — خ ن س B004 — «الخنس مأوى الظباء؛ الخنس الظباء أنفسها» (tahdhib) — the gazelles' covert, and the gazelles.
- 114:4 ٱلْخَنَّاسِ — خ ن س B003 — «البقر كلها خنس» (maqayis;jamhara) — the snub face of cattle.
- 114:1 بِرَبِّ — ر ب ب B014 — «الربرب: القطيع من بقر الوحش» (sihah) — the herd of wild cattle.
- 114:1 أَعُوذُ — ع و ذ B003 — «العوذ الحديثات النتاج من الظباء والإبل والخيل» (sihah) — the does that have just given birth: the gazelles again, with their young.
- 114:1 أَعُوذُ — ع و ذ B004 — «العوذ النبت في أصل الشوك أو في المكان الحزن لا يكاد المال يناله» (sihah) — the plant safe among thorns, out of the grazers' reach.
- 114:5 ٱلنَّاسِ — ء ن س B002 — «والاستئناس النظر وأحس بما رابه» (tahdhib) — looking about and sensing what alarms: the wary animal.
- 114:5 ٱلنَّاسِ — ء ن س B003 — «الإيناس خلاف الإيحاش والإنس خلاف الوحشة» (sihah); «كلب أنوس نقيض العقور» (tahdhib) — tame against wild, the dog that does not bite against the one that does.
- 114:6 ٱلْجِنَّةِ — ج ن ن B017 — «المجنة أيضا الموضع الذي يستتر فيه» (sihah) — the hiding place.

Quran:
- 7:16–17: Iblis to God. لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ ثُمَّ لَءَاتِيَنَّهُم مِّنۢ بَيْنِ أَيْدِيهِمْ وَمِنْ خَلْفِهِمْ وَعَنْ أَيْمَٰنِهِمْ وَعَن شَمَآئِلِهِمْ: lying in wait, then closing in from every side.
- 17:64: God to Iblis (the scene opens at 17:61). وَٱسْتَفْزِزْ مَنِ ٱسْتَطَعْتَ مِنْهُم بِصَوْتِكَ وَأَجْلِبْ عَلَيْهِم بِخَيْلِكَ وَرَجِلِكَ: startling with the voice and driving with riders.
- 74:50–51 (recalled): كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ فَرَّتْ مِن قَسْوَرَةٍۭ. Wild asses bolting from a hunter, or a lion.

### Horse and rider

Five of the surah's words name a horse's parts or its running. The rider mounts and milks from the إنسي side. The horse's legs and neck are what lead it, its ملك. The معوذ is the whorl at its neck where the necklace hangs. A خنوس horse veers right and left while galloping straight. A horse wins by arriving first with its chest. The mares that have just foaled are among the عوذ. The whisperer is the swerve inside a straight run, and refuge is worn where the necklace hangs. The Quran gives the satan horsemen (17:64), and swears by charging horses that strike sparks before naming what is in the chests (100:1–10).

- 114:1–6 ٱلنَّاسِ — ء ن س B004 — «الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب» (tahdhib); «إنسي الدابة للجانب الذي يلي الراكب» (mufradat) — the near side, from which one mounts.
- 114:2 مَلِكِ — م ل ك B008 — «ملك الدابة قوائمها وهاديها» (sihah;tahdhib); «جاءنا تقوده ملكه يعني قوائمه وهاديه» (tahdhib) [fixed expression] — legs and neck as what leads the mount.
- 114:1 أَعُوذُ — ع و ذ B005 — «معوذ الفرس موضع القلادة ودائرة المعوذ تستحب» (sihah) — the neck-whorl where the necklace sits.
- 114:4 ٱلْخَنَّاسِ — خ ن س B005 — «فرس خنوس وهو الذي يعدل وهو مستقيم في حضره ذات اليمين وذات الشمال» (tahdhib) [fixed expression] — the swerve right and left inside a straight gallop.
- 114:5 صُدُورِ — ص د ر B002 — «صدر الفرس إذا جاء قد سبق بصدره» (sihah;tahdhib;mufradat) — winning by the chest.
- 114:1 أَعُوذُ — ع و ذ B003 — «العوذ الحديثات النتاج من الظباء والإبل والخيل» (sihah) — mares just foaled.

Quran:
- 7:17: عَنْ أَيْمَٰنِهِمْ وَعَن شَمَآئِلِهِمْ. Iblis's approach, from right and left, matching the dictionary's ذات اليمين وذات الشمال.
- 17:64: أَجْلِبْ عَلَيْهِم بِخَيْلِكَ وَرَجِلِكَ.
- 100:1–2 and 100:10: God's oath by the charging horses (وَٱلْعَٰدِيَٰتِ, recalled), فَٱلْمُورِيَٰتِ قَدْحًۭا, the hooves striking sparks. The same surah ends with وَحُصِّلَ مَا فِى ٱلصُّدُورِ.

### The road to water and back

The root of مَلِكِ names the middle of the road, the animal that goes in front with the herd following, and the water a traveller carries that keeps him going. The root of صُدُورِ names turning back from the watering place, the road that leads a people back from the water, and the place and time of that return. The root of بِرَبِّ names the place where camels stay. The root of ٱلْخَنَّاسِ names slipping away from the company unseen. The documented alternative for إِلَٰهِ names water let loose in the desert until it is lost. The scene: a herd follows its leader along the middle of the road to water, drinks, and turns back by the return road; one slips off from the group; water let loose is lost. From memory, not from this dictionary: صُدُور is also the verbal noun of صدر in the sense "turning back from water", so the plural "chests" and the "turnings-back" share one form.

- 114:2 مَلِكِ — م ل ك B006 — «الزم ملك الطريق أي وسطه» (tahdhib); «ملك الطريق أيضا وسطه» (sihah) — keep to the middle of the road.
- 114:2 مَلِكِ — م ل ك B008 — «ملك الإبل والشاء ما يتقدم ويتبعه سائره» (mufradat) [fixed expression] — the leader the herd follows.
- 114:2 مَلِكِ — م ل ك B007 — «والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره» (maqayis); «مياهنا ملوكنا» (tahdhib) [fixed expression] — the traveller's water.
- 114:5 صُدُورِ — ص د ر B003 — «الصدر الانصراف عن الورد وعن كل أمر» (ayn;tahdhib); «طريق صادر يصدر بأهله عن الماء» (ayn;sihah;tahdhib); «صدرت الإبل عن الماء» (mufradat) — turning back from the water, along the return road.
- 114:5 صُدُورِ — ص د ر B004 — «المصدر في الحقيقة صدر عن الماء ولموضع المصدر ولزمانه» (mufradat) — the place and time of that return.
- 114:1 بِرَبِّ — ر ب ب B007 — «مرب الإبل حيث لزمته» (sihah) — the camels' station.
- 114:4 ٱلْخَنَّاسِ — خ ن س B001 — «خنس الرجل عن القوم إذا مضى في خفية» (jamhara) — slipping away from the company.
- 114:3 إِلَٰهِ — و ل ه B003 (documented alternative) — «ماء موله وموله أرسل في الصحراء فذهب» (sihah) — water let loose in the desert and lost.

Quran:
- 28:22–24: Musa going toward Madyan, عَسَىٰ رَبِّىٓ أَن يَهْدِيَنِى سَوَآءَ ٱلسَّبِيلِ. At the water he finds أُمَّةًۭ مِّنَ ٱلنَّاسِ, and the women say حَتَّىٰ يُصْدِرَ ٱلرِّعَآءُ. Then رَبِّ إِنِّى لِمَآ أَنزَلْتَ إِلَىَّ مِنْ خَيْرٍۢ فَقِيرٌۭ: road, water, الناس, the return from water and رب.
- 99:6: يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ. The surah's صدر and الناس in one clause: the people turning back, scattered.
- 7:16: Iblis sitting on the straight road.
- 43:37: وَإِنَّهُمْ لَيَصُدُّونَهُمْ عَنِ ٱلسَّبِيلِ وَيَحْسَبُونَ أَنَّهُم مُّهْتَدُونَ. The satan-companions bar them from the road.
- 6:71: كَٱلَّذِى ٱسْتَهْوَتْهُ ٱلشَّيَٰطِينُ فِى ٱلْأَرْضِ حَيْرَانَ لَهُۥٓ أَصْحَٰبٌۭ يَدْعُونَهُۥٓ إِلَى ٱلْهُدَى ٱئْتِنَا. Lured off by devils, lost apart from his company.
- 36:61: هَٰذَا صِرَٰطٌۭ مُّسْتَقِيمٌۭ.
- 1:6 (recalled): ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ.

### Cloud, water and sheltered growth

The root of بِرَبِّ names the hanging cloud, called رباب because it raises the plants; a cloud that lasts; much water; a tender plant that does not wither in summer; and an estate tended to completion. The root of ٱلْجِنَّةِ names the garden whose trees cover the ground, palms, plants growing tall, thick and in flower, and the hidden reward-garden. The refuge root names the plant at the root of the thorns. The scene: a lasting cloud raises the plants, water gathers, a garden thickens and covers its ground, and a growth stands safe among thorns. The raising of 114:1 is heard as a cultivation. The garden is also where the first whisper happened (7:20–22).

- 114:1 بِرَبِّ — ر ب ب B008 — «الرباب: السحاب، سمي بذلك لأنه يرب النبات» (mufradat); «السحاب المتعلق دون السحاب يكون أبيض ويكون أسود» (maqayis) — the cloud that raises the plants.
- 114:1 بِرَبِّ — ر ب ب B007 — «أربت السحابة: دامت» (mufradat) — the cloud that stays.
- 114:1 بِرَبِّ — ر ب ب B013 — «الربب، بالفتح: الماء الكثير، ويقال العذب» (sihah) — much sweet water.
- 114:1 بِرَبِّ — ر ب ب B012 — «الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف» (tahdhib) — the tender plant that does not wither.
- 114:1 بِرَبِّ — ر ب ب B002 — «رب الضيعة أي أصلحها وأتمها» (sihah) — tending an estate to completion.
- 114:6 ٱلْجِنَّةِ — ج ن ن B003 — «كل بستان ذي شجر يستر بأشجاره الأرض» (mufradat); «العرب تسمي النخيل جنة» (sihah) — the garden whose trees cover the ground.
- 114:6 ٱلْجِنَّةِ — ج ن ن B011 — «جن النبت جنونا أي طال والتف وخرج زهره» (sihah) — plants growing tall, tangled and in flower.
- 114:6 ٱلْجِنَّةِ — ج ن ن B004 — «الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم» (maqayis) — the garden still hidden today.
- 114:1 أَعُوذُ — ع و ذ B004 — «العوذ النبت في أصل الشوك» (sihah) — growth sheltered by thorns.

Quran:
- 2:265: the parable of spending. كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ: a garden and the rain on it.
- 3:37: وَأَنۢبَتَهَا نَبَاتًا حَسَنًۭا. The Lord raising a child as one grows a plant.
- 18:32–38 (recalled): the two gardens. The owner enters his garden, and his companion answers لَّٰكِنَّا۠ هُوَ ٱللَّهُ رَبِّى.
- 7:22: the leaves of the garden used as a covering, after the whisper.

### The swarm and the sparks around the face

The evil's root names a gnat-like insect that covers a person's face and does not bite, which the Arabs sometimes call الأذى, and the sparks that fly off a fire. The root of ٱلْجِنَّةِ names flies whose hum swells as they fly. The whisper is a faint rustle. The root of مَلِكِ names the king of the bees. The scene: small things hover about the face. They cover it, hum, flare and rustle, and do not bite. The whisper is harm of that size: it occupies and covers without wounding.

- 114:4 شَرِّ — ش ر ر B009 — «الشران شبيه بالبعوض يغشى وجه الإنسان ولا يعض وربما سموه الأذى» (sihah) — the dictionary joins this root with الإنسان: gnats covering the face, not biting, called "harm".
- 114:6 ٱلْجِنَّةِ — ج ن ن B015 — «جن الذباب أي كثر صوته» (sihah); «قيل هو ذباب وجنونه كثرة ترنمه في طيرانه» (tahdhib) — flies humming more and more as they fly.
- 114:4 شَرِّ — ش ر ر B003 — «الشرارة والشرر ما تطاير من النار» (ayn) — sparks flying off.
- 114:4 ٱلْوَسْوَاسِ — و س و س B002 — «الوسواس الصوت الخفي من ريح تهز قصبا ونحوه» (ayn) — the faint rustle.
- 114:2 مَلِكِ — م ل ك B008 — «مليك النحل يعسوبها» (sihah) [fixed expression] — the king of the swarm.

Quran:
- 58:10: إِنَّمَا ٱلنَّجْوَىٰ مِنَ ٱلشَّيْطَٰنِ لِيَحْزُنَ ٱلَّذِينَ ءَامَنُوا۟ وَلَيْسَ بِضَآرِّهِمْ شَيْـًٔا إِلَّا بِإِذْنِ ٱللَّهِ. A whisper that grieves but does not harm.
- 3:111 (recalled): لَن يَضُرُّوكُمْ إِلَّآ أَذًۭى. أذى as harm short of damage, the dictionary's name for the gnat.
- 100:2: sparks struck.

### The covered mind

The form ٱلْجِنَّةِ that stands in 114:6 is, in the dictionary, also madness: what covers the intellect and stands between the self and its reason. The refuge root's charm is worn "against fright or madness". The documented alternative for إِلَٰهِ names the mind going out of a person from intense grief or love, and lands that bewilder. The whisper is a bad passing thought. The scene: a mind covered or carried off, a charm worn against it, and the Quran defending the messenger's word as neither a madman's nor a satan's.

- 114:6 ٱلْجِنَّةِ — ج ن ن B006 — «الجنة الجنون وذلك أنه يغطي العقل» (maqayis); «الجنون حائل بين النفس والعقل» (mufradat) — the same word form as the text, naming the covering of the mind.
- 114:1 أَعُوذُ — ع و ذ B002 — «العوذة والمعاذة التي يعوذ بها الإنسان من فزع أو جنون» (maqayis) — the dictionary joins the charm with جنون.
- 114:3 إِلَٰهِ — و ل ه B001 (documented alternative) — «الوله ذهاب العقل والتحير من شدة الوجد» (sihah); «البلاد التي توله الإنسان أي تحيره» (sihah) — the mind going out of a person, bewilderment.
- 114:4 ٱلْوَسْوَاسِ — و س و س B001 — «الوسوسة الخطرة الرديئة» (mufradat) — the bad passing thought.
- 114:1 قُلْ — ق و ل B005 — «تقول عليه أي كذب عليه» (sihah) [fixed expression] — the false saying, the companion charge to madness in the Quran.

Quran:
- 7:184 (recalled): مَا بِصَاحِبِهِم مِّن جِنَّةٍ.
- 23:70 (recalled): أَمْ يَقُولُونَ بِهِۦ جِنَّةٌۢ.
- 34:8 (recalled): أَفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَم بِهِۦ جِنَّةٌۢ. جِنَّة as madness, in the form of 114:6, beside a false saying.
- 34:46 (recalled): مَا بِصَاحِبِكُم مِّن جِنَّةٍ.
- 81:22–25: وَمَا صَاحِبُكُم بِمَجْنُونٍۢ … وَمَا هُوَ بِقَوْلِ شَيْطَٰنٍۢ رَّجِيمٍۢ. The scene opens at the oath by the خُنَّس, 81:15.
- 52:29–33 (recalled): neither كَاهِن nor مَجْنُون, and أَمْ يَقُولُونَ تَقَوَّلَهُۥ.
- 6:71: حَيْرَانَ. Bewildered by devils.

## Interactions

- Visible/hidden × Chest: «أجننت الشيء في صدري أكننته» (ج ن ن B001, sihah). The covering root works inside the chest; 11:5.
- Visible/hidden × Speech: the dictionary's verb of bringing out ties three phrases: «المبرز بالنطق» and «قبل الإبراز باللفظ» (ق و ل B001, B012) and «أشررت الشيء إذا أبرزته» (ش ر ر B008). It is the same verb for the spoken refuge and for the evil's root.
- Speech × Withdrawal: «الشيطان يوسوس فإذا ذكر الله خنس» (خ ن س B001). The spoken remembrance makes the whisperer draw back; 7:200–201.
- Speech × Titles: «القيل ملك من ملوك حمير دون الملك الأعظم» and «كأنه الذي له قول أي ينفذ قوله» (ق و ل B004). The first word of the surah holds a lesser king whose word is carried out.
- Speech × Refuge: «ومنه قيل للتميمة والرقية عوذة» (ع و ذ B002). The commanded saying is the spoken charm; 23:97–98; 16:98.
- Refuge × Titles: «عاذ فلان بربه يعوذ عوذا إذا لجأ إليه واعتصم به» (ع و ذ B001, tahdhib) joins أعوذ and رب in one phrase; 12:23.
- Refuge × Covered mind: «من فزع أو جنون» (ع و ذ B002) joins the charm with the madness sense of ٱلْجِنَّةِ.
- Refuge × Mother and young: عائذ is the newly delivered mother (ع و ذ B003); 3:36, where a mother seeks refuge for her newborn with her رب.
- Refuge × Visible/hidden: ٱلْجِنَّةِ names both the covered attacker (B005) and the shield (B008); 58:16 and 63:2 turn oaths into a جُنَّة; 72:6 turns refuge toward the jinn.
- Refuge × Chest: «الصدار ثوب يغطي الصدر» and «الجنة الدرع» are coverings outside the chest, while the whisper is inside it; 7:26–27 has the garment and its stripping.
- Mother and young × Titles: 39:6 (formation in the womb, then ربكم, له الملك, لا إله إلا هو); 26:18 and 79:24 (Pharaoh as rival raiser and rival lord).
- Mother and young × Garden: ر ب ب B002 (raising) and B008 («يرب النبات»); 3:37 (أنبتها نباتا حسنا).
- Mother and young × Hunt: «العوذ الحديثات النتاج من الظباء» (ع و ذ B003) and «الخنس الظباء أنفسها» (خ ن س B004). The gazelle stands under two of the surah's words.
- Chest × Titles: «القلب ملاك الجسد» (م ل ك B005) and «المملكة سلطان الملك في رعيته» (B003). Which king the heart obeys; 16:99–100; 17:65.
- Chest × Road to water: صُدُورِ (chests) and صَدَر عن الماء (turning back, ص د ر B003); 99:6 يَصْدُرُ ٱلنَّاسُ; 100:10. The shared form صُدُور is from memory.
- Withdrawal × Night: خ ن س B001 (drawing back) and B002 (planets hiding and returning); 81:15–17; 6:76 (أَفَلَ), set against «أرب فلان بالمكان إذا أقام به فلم يبرحه» (ر ب ب B007).
- Withdrawal × Horse: «يعدل … ذات اليمين وذات الشمال» (خ ن س B005); 7:17 عَنْ أَيْمَٰنِهِمْ وَعَن شَمَآئِلِهِمْ.
- Horse × Road: the swerve away from «ملك الطريق أي وسطه» (م ل ك B006); 7:16.
- Hunt × Horse: 17:64 joins the startling voice (بِصَوْتِكَ) with the riders (بِخَيْلِكَ وَرَجِلِكَ).
- Hunt × Withdrawal: «الخنس مأوى الظباء» and «خنس الرجل عن القوم إذا مضى في خفية». The whisperer murmurs like the hunter and keeps to cover like the game.
- Night × Binding × Visible/hidden: السواد in «إنسان العين … في السواد» (ء ن س B005), «جنان الليل سواده» (ج ن ن B002) and «جنان الناس معظمهم ويسمى السواد» (ج ن ن B013).
- Night × Titles: «الإلاهة الشمس» (ء ل ه B001); 6:74–79; 27:24 (sun-worship led by the satan); 2:258.
- Binding × Titles: 12:39 (أرباب متفرقون); 21:22; 23:91.
- Binding × Refuge: «واعتصم به» (ع و ذ B001) and 3:103 (وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا); «تعاوذ القوم في الحرب» (ع و ذ B007).
- Binding × Speech: the back-and-forth of talk («قاولته في أمره وتقاولنا أي تفاوضنا», ق و ل B009) against the covenant («الربابة: العهد والميثاق», ر ب ب B011); 7:20–21 (whisper and counter-oath); 7:172; 36:60.
- Binding × Swarm: «مليك النحل يعسوبها» (م ل ك B008). The king who holds a swarm together.
- Swarm × Visible/hidden: «يغشى وجه الإنسان» (ش ر ر B009). A covering that hovers over the face.
- Covered mind × Speech × Night: 81:15–25 (the خُنَّس, مَجْنُون, قَوْل شَيْطَٰن); 52:29–33; 34:8.
- Garden × Visible/hidden × Refuge: «يستر بأشجاره الأرض» (ج ن ن B003); 7:20–27 (the whisper in the garden, leaves of the garden as covering, the garment stripped, the unseen seer).
- Road to water × Covered mind: «ماء موله … أرسل في الصحراء فذهب» and «الوله ذهاب العقل والتحير» (و ل ه B003, B001); 6:71 (حَيْرَانَ in the land).

## Ayat

### 114:1 قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ
- Speech: قُلْ is the saying brought out by uttering it, the saying still inside before that, the tongue, talk spread among people, drawing a saying of good or evil onto oneself, and an inward prompting called a saying. Whole scene: a saying formed inside and brought out on the tongue as the refuge; talk spreading among people; a half-voiced whisper going the other way, into chests, from jinn and from people.
- Refuge: أَعُوذُ is taking shelter with one's Lord («عاذ فلان بربه»), and the spoken charm against fright or madness. Whole scene: a person takes shelter with his Lord by a spoken charm; amulet, chest-garment, mail and shield cover the body; the attacker is in the chest, under every cover; and ٱلْجِنَّةِ names both the hidden attacker and the shield.
- Withdrawal: أَعُوذُ clings like meat to the bone, and turns away out of dislike. بِرَبِّ stays in place and does not leave. Whole scene: the whisperer speaks, draws back at remembrance, slips away unseen, and returns like a planet in its course; the Lord stays, and the seeker clings.
- Mother and young: أَعُوذُ (عائذ) and بِرَبِّ (ربّى) both name the mother just delivered; بِرَبِّ also names the foster carer and the raising to completion. Whole scene: a child hidden in the womb is born, the mother stays with it, separation is forbidden, and a carer raises it stage by stage.
- Titles: بِرَبِّ is owner, master and repairer, a title also given to human kings. قُلْ holds the lesser Himyarite king whose word runs. Whole scene: owners, petty kings, idols and the sun hold the titles in lesser ways; the one Lord, King and God of the people holds them absolutely; the whisperer offers a counterfeit kingship.
- Binding: بِرَبِّ is the pouch of arrows, the gathered thousands, the tight knot, the covenant. ٱلنَّاسِ is the gathering. Whole scene: many held as one (tight dough, arrows in their pouch, gathered tribes, a knot, a covenant); the evil's root cuts into pieces and quarrels; the bulk of the people is where persons disappear.
- Night: ٱلنَّاسِ glimpses a fire and is the small figure in the eye; بِرَبِّ does not set. Whole scene: night covers everything; planets appear, run, hide by day and return; the sun, once worshipped, rises; a fire is glimpsed and sparks fly; an eye watches; which of these is Lord.
- Hunt: أَعُوذُ is the does with new young and the plant safe among thorns; بِرَبِّ is the herd of wild cattle; ٱلنَّاسِ is the wary one sensing, and the tame against the wild. Whole scene: a hunter creeps with a low murmur and dogs; gazelles keep to cover; the wary animal senses and looks about; a plant grows out of reach among thorns.
- Horse: ٱلنَّاسِ is the near side for mounting; أَعُوذُ is the neck-whorl where the necklace hangs, and the mares just foaled. Whole scene: the rider mounts from the near side; legs and neck lead the horse; the charm hangs at its neck; one horse veers right and left in its straight gallop; the winner arrives first by its chest.
- Road to water: بِرَبِّ is the camels' station. Whole scene: a herd follows its leader along the middle of the road to water, carries water as what keeps it going, drinks, and turns back by the return road; one slips away from the company; water let loose in the desert is lost.
- Garden: بِرَبِّ is the cloud that raises plants, the lasting cloud, much water, the plant that does not wither, the tended estate; أَعُوذُ is the growth sheltered by thorns. Whole scene: a lasting cloud raises the plants, water gathers, a garden thickens and covers its ground, and a growth stands safe among thorns.
- Visible/hidden: ٱلنَّاسِ is the ones who appear, and who see and hear. Whole scene: the visible people perceive by sight and hearing; a covered being and a sound at the edge of hearing work on them and withdraw; the evil's root itself is bringing out into the sun.
- Chest: قُلْ is the saying kept inside; ٱلنَّاسِ folds back into one's own self. Whole scene: a ribbed chamber with the heart hidden in it; a thing its owner hides there; a voice inside speaking as the self speaks; the heart that holds the body up; entry made without asking leave.
- Covered mind: أَعُوذُ is the charm against madness; قُلْ is the false saying. Whole scene: a mind covered or carried off, a charm worn against it, and the messenger's word defended as no madman's and no satan's.

### 114:2 مَلِكِ ٱلنَّاسِ
- Titles: مَلِكِ is God's own kingship, سلطان over subjects, commanding and forbidding, and the kings people make for themselves. Whole scene: as in 114:1.
- Binding: مَلِكِ is firmness, tight-kneaded dough, a wall that holds together, a hand that holds firm. Whole scene: as in 114:1.
- Chest: مَلِكِ names the heart as the body's mainstay («القلب ملاك الجسد»). Whole scene: as in 114:1.
- Road to water: مَلِكِ is the middle of the road, the herd's leader, and the traveller's water. Whole scene: as in 114:1.
- Horse: مَلِكِ is the legs and neck that lead the mount. Whole scene: as in 114:1.
- Swarm: مَلِكِ is the king of the bees. Whole scene: small things hover about the face (gnats that cover it and do not bite, flies whose hum swells, sparks flying off a fire, a faint rustle), and a king leads the swarm.
- Night: مَلِكِ is the ملكوت shown to Ibrahim before his night. Whole scene: as in 114:1.
- ٱلنَّاسِ carries its 114:1 roles in Visible/hidden, Hunt, Horse and Binding.

### 114:3 إِلَٰهِ ٱلنَّاسِ
- Titles: إِلَٰهِ is any object of worship (idols, the sun), and the noun made particular for God. Whole scene: as in 114:1.
- Night: إِلَٰهِ names the sun, called إلاهة because it was worshipped. Whole scene: as in 114:1, with the sun among the lights that set.
- Mother and young: through the documented alternative و ل ه, the mother camel's yearning, the forbidden separation, and yearning toward someone. Whole scene: as in 114:1.
- Covered mind: و ل ه is the mind going out of a person from grief or love, and bewilderment. Whole scene: as in 114:1.
- Road to water: و ل ه is water let loose in the desert and lost. Whole scene: as in 114:1.
- ٱلنَّاسِ, said for the third time, keeps one object under three relations (Binding, Visible/hidden).

### 114:4 مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ
- Visible/hidden: شَرِّ is bringing out and spreading in the sun; ٱلْوَسْوَاسِ is a hidden sound; ٱلْخَنَّاسِ is hiding. Whole scene: as in 114:1.
- Withdrawal: ٱلْخَنَّاسِ draws back at remembrance, falls back, slips away, and returns like a planet; ٱلْوَسْوَاسِ is a repeated movement-sound. Whole scene: as in 114:1.
- Speech: ٱلْوَسْوَاسِ is self-talk and murmur; شَرِّ joins قول in «قولا من خير أو شر». Whole scene: as in 114:1.
- Night: ٱلْخَنَّاسِ is the planets hiding by day; شَرِّ is spreading in the sun and sparks from fire. Whole scene: as in 114:1.
- Hunt: ٱلْوَسْوَاسِ is the hunter's murmur, his dogs, and the rustle in the reeds; ٱلْخَنَّاسِ is the gazelles' covert, the gazelles, and the snub-nosed cattle. Whole scene: as in 114:1.
- Horse: ٱلْخَنَّاسِ is the horse veering right and left. Whole scene: as in 114:1.
- Road to water: ٱلْخَنَّاسِ slips away from the company. Whole scene: as in 114:1.
- Binding: شَرِّ cuts into pieces and quarrels. Whole scene: as in 114:1.
- Titles: شَرِّ is the whole self thrown onto one object. Whole scene: as in 114:1.
- Swarm: شَرِّ is gnats covering the face without biting, and sparks; ٱلْوَسْوَاسِ is the faint rustle. Whole scene: as in 114:2.
- Chest: ٱلْوَسْوَاسِ is placed in the chest and heart by the dictionary. Whole scene: as in 114:1.
- Covered mind: ٱلْوَسْوَاسِ is the bad passing thought. Whole scene: as in 114:1.

### 114:5 ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ
- Chest: صُدُورِ is the chamber and its raised front; يُوَسْوِسُ is the whisper in the chest and heart, the self speaking to itself; ٱلنَّاسِ is one's own self, and the asking of leave that this entry skips. Whole scene: as in 114:1.
- Speech: يُوَسْوِسُ is speech that stays inside, coming in against the commanded saying. Whole scene: as in 114:1.
- Withdrawal: يُوَسْوِسُ repeats the root as an action, so the cycle goes on. Whole scene: as in 114:1.
- Road to water: صُدُورِ is turning back from water, the return road, and the place and time of return. The shared form صُدُور is from memory. Whole scene: as in 114:1.
- Horse: صُدُورِ is the chest by which a horse wins. Whole scene: as in 114:1.
- Refuge: صُدُورِ is covered by the chest-garment, while the whisper works under it. Whole scene: as in 114:1.
- Hunt: يُوَسْوِسُ is the murmur; ٱلنَّاسِ is the wary one sensing. Whole scene: as in 114:1.
- Visible/hidden: ٱلنَّاسِ is the visible ones, who see and hear. Whole scene: as in 114:1.

### 114:6 مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ
- Visible/hidden: ٱلْجِنَّةِ is the beings covered from eyes and the covering itself; وَٱلنَّاسِ is the ones who appear. The dictionary defines each against the other. Whole scene: as in 114:1, closed here by both classes as sources.
- Chest: ٱلْجِنَّةِ is the chest's bones and rib-ends, the hidden heart, and hiding a thing in one's chest. Whole scene: as in 114:1.
- Refuge: ٱلْجِنَّةِ is shield, mail, the covering garment and the hiding place. Whole scene: as in 114:1.
- Mother and young: ٱلْجِنَّةِ is the child in the womb, and the first beginning of youth. Whole scene: as in 114:1.
- Night: ٱلْجِنَّةِ is night's black covering. Whole scene: as in 114:1.
- Binding: ٱلْجِنَّةِ is the dark bulk of the people. Whole scene: as in 114:1.
- Garden: ٱلْجِنَّةِ is the garden that covers its ground, plants thickening and flowering, and the hidden reward-garden. Whole scene: as in 114:1.
- Swarm: ٱلْجِنَّةِ is flies humming more and more. Whole scene: as in 114:2.
- Covered mind: ٱلْجِنَّةِ in this very form is madness, the covering of the mind. Whole scene: as in 114:1.
- Hunt: ٱلْجِنَّةِ is the hiding place. Whole scene: as in 114:1.
- Speech: وَٱلنَّاسِ is the human channel of whispering, the talk that spreads among people. Whole scene: as in 114:1.

