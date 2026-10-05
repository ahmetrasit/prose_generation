Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 11 of 18 ("Tesbih, anma, namaz: sureyi açan ve kapayan iş"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

Discovery rationales and accuracy flags are unverified. Judge each against canonical Arabic, including speaker, negation and ayah boundaries.

===== _commentary/v16/prompts/augment9s/augment.md =====
You are completing a finished Turkish commentary on the images of a surah,
written by another reader, with what the Quran itself says about it: the Quran
explaining the Quran. Below are one image section of that commentary, with its
prose paragraphs numbered [¶n] as in the whole commentary; the commentary's
ledger; and Quran passages from an image-based discovery list (two readers'
judgements of which ayat this image activates), each with its Arabic, its tier,
the bases given for it, and the paragraphs of the section that already cite it,
if any. A tier is that list's own judgement, not yours; the list is not
authoritative and may be incomplete.

Read the section first. Then judge every listed passage, one by one, against
every paragraph of the section: is it relevant to what that paragraph says? A passage is
relevant to a paragraph when it explains, completes, extends or contrasts
something the paragraph says, or names what the ayat the paragraph reads leave
unnamed. A shared word or root alone
does not make it relevant; the link must hold in what the passage says. A
passage is never added to a paragraph that already cites it. Judge it against
every other paragraph as if it were new: "already cited" is never a reason for
"not relevant". A paragraph that points to a passage without citing it ("başka
bir surede") takes that passage as a reference. If a passage shows that
something a paragraph says is wrong, do not add it: give it the verdict
"conflict ¶n" with what it shows. A passage that qualifies what a paragraph says
without showing it wrong is a reference whose link says what it adds.

The commentary's ledger names what its writer weighed and left out, and why.
Such a passage may still be added when it is relevant; its verdict then answers
the writer's reason.

Then go through the section paragraph by paragraph and ask your own
knowledge of the Quran, exhaustively, which ayat, in neither the list nor that
paragraph, are relevant to it in the same sense, and treat them the same way.
For each paragraph weigh at least: the other places of the key words and
constructions of the ayat it quotes; the other places where the image's scene,
object or act is staged, with or without a shared word; ayat that state the same thing in other
words; passages that stage the same act, scene, speaker or stance without
sharing a word; the neighbouring ayat (within two) of every passage it cites
(the list includes the nearest of them as a tier of their own) and of every
passage you add; and the passages the ledger names as weighed and left out.
Every ayah you look up gets a verdict.

There is no limit on the number of additions. Leaving out what is not relevant
is part of the work; adding what is not relevant weakens the commentary.

Every relevant passage is added to its paragraph in one of two forms.
- Prose, when the passage changes how the paragraph is understood: give its
  speaker and its situation only as the Quran itself tells them there and in
  the neighbouring ayat; the mechanism of the link (a shared root used in the
  same sense, the same construction, the same scene or speaker, a contrast, a
  completion, an order of events, a name for what the paragraph leaves
  unnamed); and what it adds. As long as the link needs and no longer.
- Reference, when the passage supports or parallels the paragraph without
  changing it: its source with the link in a few words, gathered in the
  paragraph's one reference line. The link names its mechanism: what in the
  passage meets what in the paragraph ("korkan için indirilen hatırlatma",
  not "aynı ifade", "aynı emir" or "aynı soru"). The test of relevance holds
  for references as for prose: a passage that shares only a word with the
  paragraph is not relevant. A wording the Quran repeats in several ayat (a
  refrain) is one reference: all its places together, then one link, e.g.
  {source:54:17} {source:54:22} {source:54:32} {source:54:40} <the link>.
  Consecutive ayat that one link covers are one reference too:
  {source:88:21} {source:88:22} <the link>.
A passage relevant to several paragraphs gets its prose once, where it changes
the understanding most, and a reference in the others. A passage the
commentary already explains in one of its paragraphs is a reference in any
other paragraph it is relevant to.

The additions are placed by the script after their paragraph, each prose
addition as a paragraph of its own and the reference line last; the
commentary's paragraphs are not touched, and the additions can be shown or
hidden together. So each prose addition opens from the paragraph it serves,
without repeating it, and stands on its own: it never leans on another
addition. It stops when the link is made: no formula opener such as "Kur'an bu … başka bir yerde de …", and no
closing sentence that sums up or draws the lesson.

Where the Quran does not name the speaker, or who is meant is disputed (the
speaker of 12:52-53; the two told to go down in 20:123), say only what the ayah
says, without naming anyone. Name another surah by its name ("Tâhâ
suresinde"); "aynı sure" and "bu sure" mean only the surah of the commentary.

Never change or contradict the commentary, and never restate its explanations:
citing a passage the commentary cites in another paragraph is not restating,
repeating what the commentary says about it is. Turkish prose in the commentary's register, warm and direct; explain, do
not dramatize; no first person and no talk about sources or process (no
"sözlük", "harita", "zincir", "liste", no mention of the list or the commentary
itself). Every Arabic quotation goes in the reader tag with its source, the one
ayah that holds the quoted words:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning, source:<surah:ayah>}
A passage named without quoting it gets the source alone: {source:<surah:ayah>}.
For a listed passage, copy its Arabic letter for letter from the list; for any
other passage, read its Arabic with the lookup described above the brief before
you quote it, or name it by its source alone. Never
invent a sense, source, speaker, situation or citation. Use no hadith, no
exegetes' views and no report from outside the Quran (no occasion of
revelation, no name the Quran does not give, no date).

Output only this, with no preamble, notes or summary. For each prose addition, a block:
=== ADD ===
paragraph: <n>
ref: <surah:ayah>
text: <the addition, on one line>
For each paragraph that has references, one block:
=== REFS ===
paragraph: <n>
text: Ayrıca: {source:<surah:ayah>} <the link, naming its mechanism>; {source:<surah:ayah>} {source:<surah:ayah>} <one link for a refrain>; …
Then a line containing only
=== VERDICTS ===
then one line for every listed passage, in the list's order, and one for every
passage from your own knowledge that you weighed, marked "own". Paragraph
numbers are the ones shown: only this section's paragraphs may be served.
- <surah:ayah>: prose ¶n[, ref ¶m …] - <the mechanism in a few words>
- <surah:ayah>: ref ¶n[, ¶m …] - <the link in a few words>
- <surah:ayah>: context ¶n (in <surah:ayah>) - <quoted or named inside that prose addition>
- <surah:ayah>: conflict ¶n - <what it shows against the paragraph>
- <surah:ayah>: cited ¶n; ref ¶m | prose ¶m | nowhere else - <why, for a passage the commentary already cites>
- <surah:ayah>: not relevant - <reason in a few words>
- <surah:ayah> own: prose ¶n | ref ¶n | context ¶n (in <surah:ayah>) | conflict ¶n | not relevant - <…>

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 11 (prose paragraphs numbered) =====
[¶43] Birinci ayetin emri olan {ar:سَبِّحِ ٱسْمَ رَبِّكَ, tr:sebbihi'sme rabbik, gloss:Rabbinin adını tesbih et, source:87:1} on beşinci ayette bir kişinin yaptığı iş olarak geri döner: {ar:وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ, tr:ve ẕekera'sme rabbihî fe-sallâ, gloss:Rabbinin adını anıp namaz kıldı, source:87:15}. Arapça bu üç fiili, tesbihi, anmayı ve namazı, tek bir uygulama olarak ele alır. Tesbih nafile anma ve namazdır: {ar:السبحة التطوع من الذكر والصلاة, tr:es-subha et-tetavvuu mine'ẕ-ẕikri ve's-salât, gloss:subha nafile anma ve namazdır, source:"س ب ح,B001"}. {ar:التسبيح عاما في العبادات قولا كان أو فعلا أو نية, tr:et-tesbîhu âmmen fi'l-ibâdâti kavlen kâne ev fi'len ev niyye, gloss:tesbih söz iş ya da niyet olarak bütün ibadetler için genel bir addır, source:"س ب ح,B001"}. Anma namaz, dua ve övgüdür: {ar:الذكر الصلاة والدعاء والثناء, tr:eẕ-ẕikru's-salâtu ve'd-duâu ve's-senâ, gloss:zikir namaz dua ve övgüdür, source:"ذ ك ر,B005"}. Kur'an okumak da anmadır: {ar:الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة, tr:eẕ-ẕikru kırâetu'l-kur'âni ve't-tesbîhu ve'd-duâu ve'ş-şukru ve't-tâa, gloss:zikir Kur'an okumak tesbih dua şükür ve itaattir, source:"ذ ك ر,B005"}. Bu tanım altıncı ayetteki "okutacağız" fiilinin kökünü de içerir. Anma dilde dolaşan addır: {ar:الذكر جري الشيء على لسانك, tr:eẕ-ẕikru cerayu'ş-şey'i alâ lisânik, gloss:zikir bir şeyin dilinde dolaşmasıdır, source:"ذ ك ر,B004"}. Namazın kendisi bir dizi harekettir: {ar:الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح, tr:es-salâtu mine'l-mahlûkîn el-kıyâmu ve'r-rukûu ve's-sucûdu ve'd-duâu ve't-tesbîh, gloss:yaratılmışlar için namaz kıyam rükû secde dua ve tesbihtir, source:"ص ل و,B003"}. Namaz dua da demektir: {ar:الصلاة وهي الدعاء, tr:es-salâtu ve hiye'd-duâ, gloss:salât duadır, source:"ص ل و,B002"}. Aynı kök, Allah'ın kullarına yönelişini de anlatır: {ar:صلاة الله للمسلمين تزكيته إياهم, tr:salâtullâhi li'l-muslimîne tezkiyetuhû iyyâhum, gloss:Allah'ın Müslümanlara salâtı onları arındırmasıdır, source:"ص ل و,B002"}. Bu tanım on beşinci ayeti on dördüncü ayete bağlar. Kişinin namazı ile Allah'ın arındırması aynı kökün iki yönüdür.

[¶44] Namaz bedensel bir iştir ve kelimelerin aileleri bedeni gösterir. Tesbih kökü secde yerlerini adlandırır: {ar:السبحات مواضع السجود, tr:es-subuhât mevâdiu's-sucûd, gloss:subuhât secde yerleridir, source:"س ب ح,B003"}. Namaz kökü sırtın ortasını adlandırır: {ar:الصلا وسط الظهر لكل ذي أربع وللناس, tr:es-salâ vasatu'z-zahri li-kulli ẕî erbain ve li'n-nâs, gloss:salâ dört ayaklının ve insanın sırtının ortasıdır, source:"ص ل و,B005"}. Yedinci ayetteki "açık" kelimesinin kökü sesli kılınan namazı ve okumayı anlatır: {ar:جهر بكلامه وصلاته وقراءته, tr:cehera bi-kelâmihî ve salâtihî ve kırâetih, gloss:sözünü namazını ve okumasını açıktan yaptı, source:"ج ه ر,B001"}. Böylece sure ibadeti iki uçta kurar. Birinci ayette bir emir olarak başlar, on beşinci ayette bir insanın hareketleri olarak tamamlanır. Arada okuma, öğüt ve unutmama vardır. Bunların hepsi aynı uygulamanın parçalarıdır.

[¶45] Kur'an bu üçlüyü sık sık birlikte sahneler. Yükseltilmiş evlerde adın anılıp tesbih edildiği ayetin hemen ardından şöyle denir: {ar:رِجَالٌۭ لَّا تُلْهِيهِمْ تِجَٰرَةٌۭ وَلَا بَيْعٌ عَن ذِكْرِ ٱللَّهِ وَإِقَامِ ٱلصَّلَوٰةِ وَإِيتَآءِ ٱلزَّكَوٰةِ, tr:ricâlun lâ tulhîhim ticâratun ve lâ bey'un an ẕikrillâhi ve ikâmi's-salâti ve îtâi'z-zekât, gloss:ne ticaretin ne alışverişin Allah'ı anmaktan namazı kılmaktan ve zekâtı vermekten alıkoymadığı adamlar, source:24:37}. Bu ayette surenin on dördüncü ve on beşinci ayetlerindeki üç kelime aynı sırayla bulunur. Musa ateşin başında {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14} emrini alır. Aynı konuşmada kardeşini yardımcı olarak isterken amacını şöyle söyler: {ar:كَىْ نُسَبِّحَكَ كَثِيرًۭا, tr:key nusebbihake keŝîrâ, gloss:seni çokça tesbih edelim diye, source:20:33}, {ar:وَنَذْكُرَكَ كَثِيرًا, tr:ve neẕkurake keŝîrâ, gloss:ve seni çokça analım diye, source:20:34}. Peygamber'e de {ar:وَسَبِّحْ بِحَمْدِ رَبِّكَ قَبْلَ طُلُوعِ ٱلشَّمْسِ وَقَبْلَ غُرُوبِهَا, tr:ve sebbih bi-hamdi rabbike kable tulûi'ş-şemsi ve kable ğurûbihâ, gloss:güneş doğmadan ve batmadan önce Rabbini överek tesbih et, source:20:130} denir. Müminlere cuma günü namaza çağrıldıklarında {ar:فَٱسْعَوْا۟ إِلَىٰ ذِكْرِ ٱللَّهِ, tr:fe's'av ilâ ẕikrillâh, gloss:Allah'ı anmaya koşun, source:62:9} denir. Namaz bitince de {ar:وَٱذْكُرُوا۟ ٱللَّهَ كَثِيرًۭا لَّعَلَّكُمْ تُفْلِحُونَ, tr:veẕkurullâhe keŝîran leallekum tuflihûn, gloss:Allah'ı çokça anın ki kurtuluşa eresiniz, source:62:10} denir. Bu emirde on beşinci ayetteki anma, on dördüncü ayetteki kurtuluşa bağlanır. Başka bir yerde namazın işi şöyle anlatılır: {ar:إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ ۗ وَلَذِكْرُ ٱللَّهِ أَكْبَرُ, tr:inne's-salâte tenhâ ani'l-fahşâi ve'l-munker ve le-ẕikrullâhi ekber, gloss:namaz hayâsızlıktan ve kötülükten alıkoyar; Allah'ı anmak ise elbette en büyüktür, source:29:45}. Bu ayette "en büyük" sıfatı anmaya verilir. Surede ise aynı kökten gelen "en büyük" sıfatı ateşe verilir. Namaz kılanlar arasında bile bir ayrım vardır: {ar:فَوَيْلٌۭ لِّلْمُصَلِّينَ, tr:fe-veylun li'l-musallîn, gloss:yazıklar olsun o namaz kılanlara, source:107:4}, {ar:ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ, tr:elleẕîne hum an salâtihim sâhûn, gloss:onlar ki namazlarından gafildirler, source:107:5}. Gaflet, altıncı ayetteki unutmanın bir türüdür.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (244) =====
## strong (138)

- (2:3) [terra: strong (missing-ayat turn); basis: neighbour+root+theme] ٱلَّذِينَ يُؤْمِنُونَ بِٱلْغَيْبِ وَيُقِيمُونَ ٱلصَّلَوٰةَ وَمِمَّا رَزَقْنَٰهُمْ يُنفِقُونَ
  Unverified discovery rationale: terra: The God-conscious establish prayer as an identifying act; 2:5 names this community as the successful, reproducing the section's prayer-to-success relation.
- (2:5) [terra: strong (missing-ayat turn); basis: neighbour+theme] أُو۟لَٰٓئِكَ عَلَىٰ هُدًۭى مِّن رَّبِّهِمْ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ
  Unverified discovery rationale: terra: “These are the successful” supplies the outcome of the prayer and faithful response described in 2:3-4.
- (2:43) [luna: strong; terra: medium; basis: root+scene] وَأَقِيمُوا۟ ٱلصَّلَوٰةَ وَءَاتُوا۟ ٱلزَّكَوٰةَ وَٱرْكَعُوا۟ مَعَ ٱلرَّٰكِعِينَ
  Unverified discovery rationale: luna: This command joins establishing prayer and giving zakat with bowing among those who bow, a concrete bodily act in the section's definition of human salat. | terra: The command to establish prayer is immediately embodied as وَٱرْكَعُوا۟ مَعَ ٱلرَّٰكِعِينَ, displaying bowing as part of communal salat.
- (2:44) [terra: strong (missing-ayat turn); basis: contrast+neighbour+theme] ۞ أَتَأْمُرُونَ ٱلنَّاسَ بِٱلْبِرِّ وَتَنسَوْنَ أَنفُسَكُمْ وَأَنتُمْ تَتْلُونَ ٱلْكِتَٰبَ ۚ أَفَلَا تَعْقِلُونَ
  Unverified discovery rationale: terra: People recite the Book yet forget themselves while ordering others to righteousness; 2:45 turns immediately to prayer, exposing the failure to convert recitation into embodied practice.
- (2:45) [luna: medium; terra: strong (missing-ayat turn); basis: neighbour+root+theme] وَٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ ۚ وَإِنَّهَا لَكَبِيرَةٌ إِلَّا عَلَى ٱلْخَٰشِعِينَ
  Unverified discovery rationale: luna: Believers are told to seek help through patience and prayer, which is difficult except for the humble who expect to meet their Lord; this connects salat to the section's humility and fear. | terra: Seeking help through patience and prayer follows the rebuke of reciters who forget themselves in 2:44; prayer is the difficult enacted answer except for the humble.
- (2:125) [luna: medium (missing-ayat turn); terra: strong; basis: root+scene+theme] وَإِذْ جَعَلْنَا ٱلْبَيْتَ مَثَابَةًۭ لِّلنَّاسِ وَأَمْنًۭا وَٱتَّخِذُوا۟ مِن مَّقَامِ إِبْرَٰهِۦمَ مُصَلًّۭى ۖ وَعَهِدْنَآ إِلَىٰٓ إِبْرَٰهِۦمَ وَإِسْمَٰعِيلَ أَن طَهِّرَا بَيْتِىَ لِلطَّآئِفِينَ وَٱلْعَٰكِفِينَ وَٱلرُّكَّعِ ٱلسُّجُودِ
  Unverified discovery rationale: luna: Abraham and Ishmael are commanded to purify the House for those who circle it, stay there, bow, and prostrate; this links sacred place, purification, and the bodily acts in the section's prayer definition. | terra: God's house is purified for circumambulation, retreat, bowing, and prostration; a purified place gathers the bodily acts that the section's prayer definition enumerates.
- (2:151) [luna: strong; basis: root+scene+theme] كَمَآ أَرْسَلْنَا فِيكُمْ رَسُولًۭا مِّنكُمْ يَتْلُوا۟ عَلَيْكُمْ ءَايَٰتِنَا وَيُزَكِّيكُمْ وَيُعَلِّمُكُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَيُعَلِّمُكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ
  Unverified discovery rationale: luna: The Messenger recites God's verses, purifies the believers, and teaches them the Book and wisdom; this directly joins recitation and purification as the section does across 87:14-15.
- (2:152) [luna: strong; terra: medium; basis: root+speaker+theme] فَٱذْكُرُونِىٓ أَذْكُرْكُمْ وَٱشْكُرُوا۟ لِى وَلَا تَكْفُرُونِ
  Unverified discovery rationale: luna: Remember Me; I will remember you, and be grateful to Me. The ayah directly connects dhikr with gratitude, another sense listed in the section's dictionary entry. | terra: فَٱذْكُرُونِىٓ أَذْكُرْكُمْ joins commanded remembrance to reciprocal divine remembrance and immediately to gratitude, one of the acts included in the section's dictionary definition of dhikr.
- (2:200) [luna: strong (missing-ayat turn); basis: root+scene] فَإِذَا قَضَيْتُم مَّنَٰسِكَكُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَذِكْرِكُمْ ءَابَآءَكُمْ أَوْ أَشَدَّ ذِكْرًۭا ۗ فَمِنَ ٱلنَّاسِ مَن يَقُولُ رَبَّنَآ ءَاتِنَا فِى ٱلدُّنْيَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ
  Unverified discovery rationale: luna: After completing the rites, people are told to remember Allah with abundant remembrance; it makes remembrance the continuation of bodily worship, as 87:15 joins remembrance and prayer.
- (2:238) [luna: strong; terra: medium; basis: root+scene] حَٰفِظُوا۟ عَلَى ٱلصَّلَوَٰتِ وَٱلصَّلَوٰةِ ٱلْوُسْطَىٰ وَقُومُوا۟ لِلَّهِ قَٰنِتِينَ
  Unverified discovery rationale: luna: The command to guard the prayers and stand قانتين makes the standing posture explicit, matching the section's bodily definition of salat. | terra: Guarding the prayers is followed by وَقُومُوا۟ لِلَّهِ قَٰنِتِينَ, making upright bodily standing an element of sustained prayer.
- (2:239) [luna: strong (missing-ayat turn); terra: medium; basis: contrast+root+scene+theme] فَإِنْ خِفْتُمْ فَرِجَالًا أَوْ رُكْبَانًۭا ۖ فَإِذَآ أَمِنتُمْ فَٱذْكُرُوا۟ ٱللَّهَ كَمَا عَلَّمَكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ
  Unverified discovery rationale: luna: In fear, prayer may be performed on foot or riding; when safe, believers are told to remember Allah. This ayah's own contribution is the bodily adaptation of salat and its transition to remembrance in safety. | terra: Under fear prayer may be performed walking or riding; once safe, remembrance resumes, joining bodily adaptation of salat to taught dhikr.
- (3:39) [luna: strong; terra: strong; basis: neighbour+root+scene] فَنَادَتْهُ ٱلْمَلَٰٓئِكَةُ وَهُوَ قَآئِمٌۭ يُصَلِّى فِى ٱلْمِحْرَابِ أَنَّ ٱللَّهَ يُبَشِّرُكَ بِيَحْيَىٰ مُصَدِّقًۢا بِكَلِمَةٍۢ مِّنَ ٱللَّهِ وَسَيِّدًۭا وَحَصُورًۭا وَنَبِيًّۭا مِّنَ ٱلصَّٰلِحِينَ
  Unverified discovery rationale: luna: Zakariya is standing in prayer in the sanctuary when the angels call to him; the verse shows the bodily stance included in the section's definition of salat. | terra: Zechariah is قَآئِمٌۭ يُصَلِّى فِى ٱلْمِحْرَابِ when the angels call; this embodies prayer as standing and follows his supplication in 3:38.
- (3:41) [luna: strong; terra: strong; basis: neighbour+root+scene+speaker+theme] قَالَ رَبِّ ٱجْعَل لِّىٓ ءَايَةًۭ ۖ قَالَ ءَايَتُكَ أَلَّا تُكَلِّمَ ٱلنَّاسَ ثَلَٰثَةَ أَيَّامٍ إِلَّا رَمْزًۭا ۗ وَٱذْكُر رَّبَّكَ كَثِيرًۭا وَسَبِّحْ بِٱلْعَشِىِّ وَٱلْإِبْكَٰرِ
  Unverified discovery rationale: luna: Zakariya is told to remember his Lord much and glorify Him morning and evening, combining the section's linked roots in a single prophetic instruction. | terra: Zechariah is commanded to remember his Lord much and glorify at evening and morning, extending the prayer and supplication scene of 3:38-39 into dhikr and tasbih.
- (3:113) [terra: strong; basis: root+scene] ۞ لَيْسُوا۟ سَوَآءًۭ ۗ مِّنْ أَهْلِ ٱلْكِتَٰبِ أُمَّةٌۭ قَآئِمَةٌۭ يَتْلُونَ ءَايَٰتِ ٱللَّهِ ءَانَآءَ ٱلَّيْلِ وَهُمْ يَسْجُدُونَ
  Unverified discovery rationale: terra: An upright community recites God's signs during the night وَهُمْ يَسْجُدُونَ, joining voiced recitation with the bodily movement of prayer.
- (3:164) [luna: strong; basis: root+scene+theme] لَقَدْ مَنَّ ٱللَّهُ عَلَى ٱلْمُؤْمِنِينَ إِذْ بَعَثَ فِيهِمْ رَسُولًۭا مِّنْ أَنفُسِهِمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِهِۦ وَيُزَكِّيهِمْ وَيُعَلِّمُهُمُ ٱلْكِتَٰبَ وَٱلْحِكْمَةَ وَإِن كَانُوا۟ مِن قَبْلُ لَفِى ضَلَٰلٍۢ مُّبِينٍ
  Unverified discovery rationale: luna: The Messenger recites verses, purifies believers, and teaches them the Book and wisdom; it makes the section's Quran-recitation and purification link explicit.
- (3:191) [luna: medium; terra: strong (missing-ayat turn); basis: root+scene+theme] ٱلَّذِينَ يَذْكُرُونَ ٱللَّهَ قِيَٰمًۭا وَقُعُودًۭا وَعَلَىٰ جُنُوبِهِمْ وَيَتَفَكَّرُونَ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ رَبَّنَا مَا خَلَقْتَ هَٰذَا بَٰطِلًۭا سُبْحَٰنَكَ فَقِنَا عَذَابَ ٱلنَّارِ
  Unverified discovery rationale: luna: These believers remember God standing, sitting, and on their sides, postures that overlap the section's bodily account of prayer while showing remembrance continuing through ordinary positions. | terra: These believers remember God standing, sitting, and on their sides, then voice a supplication; dhikr, bodily positions, reflection, and dua form one continuous worship scene.
- (4:101) [luna: strong (missing-ayat turn); basis: neighbour+root+scene] وَإِذَا ضَرَبْتُمْ فِى ٱلْأَرْضِ فَلَيْسَ عَلَيْكُمْ جُنَاحٌ أَن تَقْصُرُوا۟ مِنَ ٱلصَّلَوٰةِ إِنْ خِفْتُمْ أَن يَفْتِنَكُمُ ٱلَّذِينَ كَفَرُوٓا۟ ۚ إِنَّ ٱلْكَٰفِرِينَ كَانُوا۟ لَكُمْ عَدُوًّۭا مُّبِينًۭا
  Unverified discovery rationale: luna: This ayah permits shortening prayer during travel when believers fear attack; 4:102 supplies the following bodily arrangement for prayer in danger.
- (4:102) [luna: strong; terra: strong; basis: root+scene] وَإِذَا كُنتَ فِيهِمْ فَأَقَمْتَ لَهُمُ ٱلصَّلَوٰةَ فَلْتَقُمْ طَآئِفَةٌۭ مِّنْهُم مَّعَكَ وَلْيَأْخُذُوٓا۟ أَسْلِحَتَهُمْ فَإِذَا سَجَدُوا۟ فَلْيَكُونُوا۟ مِن وَرَآئِكُمْ وَلْتَأْتِ طَآئِفَةٌ أُخْرَىٰ لَمْ يُصَلُّوا۟ فَلْيُصَلُّوا۟ مَعَكَ وَلْيَأْخُذُوا۟ حِذْرَهُمْ وَأَسْلِحَتَهُمْ ۗ وَدَّ ٱلَّذِينَ كَفَرُوا۟ لَوْ تَغْفُلُونَ عَنْ أَسْلِحَتِكُمْ وَأَمْتِعَتِكُمْ فَيَمِيلُونَ عَلَيْكُم مَّيْلَةًۭ وَٰحِدَةًۭ ۚ وَلَا جُنَاحَ عَلَيْكُمْ إِن كَانَ بِكُمْ أَذًۭى مِّن مَّطَرٍ أَوْ كُنتُم مَّرْضَىٰٓ أَن تَضَعُوٓا۟ أَسْلِحَتَكُمْ ۖ وَخُذُوا۟ حِذْرَكُمْ ۗ إِنَّ ٱللَّهَ أَعَدَّ لِلْكَٰفِرِينَ عَذَابًۭا مُّهِينًۭا
  Unverified discovery rationale: luna: The battle prayer divides worshippers into groups, with one group prostrating while another stands guard. The section's dictionary defines creaturely salat through bodily acts including standing and prostration. | terra: The prayer under danger is enacted by standing with the Prophet, taking arms, prostrating, and yielding place to another group; salat is visibly a coordinated sequence of bodily acts.
- (4:103) [luna: strong; terra: strong; basis: root+scene+theme] فَإِذَا قَضَيْتُمُ ٱلصَّلَوٰةَ فَٱذْكُرُوا۟ ٱللَّهَ قِيَٰمًۭا وَقُعُودًۭا وَعَلَىٰ جُنُوبِكُمْ ۚ فَإِذَا ٱطْمَأْنَنتُمْ فَأَقِيمُوا۟ ٱلصَّلَوٰةَ ۚ إِنَّ ٱلصَّلَوٰةَ كَانَتْ عَلَى ٱلْمُؤْمِنِينَ كِتَٰبًۭا مَّوْقُوتًۭا
  Unverified discovery rationale: luna: After prayer, believers are told to remember Allah standing, sitting, and lying on their sides; it connects salat and dhikr while showing remembrance continues beyond the bodily prayer. | terra: When prayer is completed, remembrance continues standing, sitting, and lying down; the verse binds salat, dhikr, and bodily positions before prayer is re-established in safety.
- (5:91) [luna: contrast; terra: strong; basis: contrast+root+scene+theme] إِنَّمَا يُرِيدُ ٱلشَّيْطَٰنُ أَن يُوقِعَ بَيْنَكُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ فِى ٱلْخَمْرِ وَٱلْمَيْسِرِ وَيَصُدَّكُمْ عَن ذِكْرِ ٱللَّهِ وَعَنِ ٱلصَّلَوٰةِ ۖ فَهَلْ أَنتُم مُّنتَهُونَ
