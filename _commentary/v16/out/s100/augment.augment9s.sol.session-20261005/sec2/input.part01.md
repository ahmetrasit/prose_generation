Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 100; below is its section 2 of 11 ("Şafak baskını"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md section 2 (prose paragraphs numbered) =====
[¶8] Koşan atların yaptığı iş üçüncü ayette adını alır: {ar:فَٱلْمُغِيرَٰتِ صُبْحًا, tr:fe'l-muğîrâti subhâ, gloss:derken sabahleyin baskın yapanlara, source:100:3}. Kelime baskın fiilinden gelir: {ar:أغار على القوم, tr:eğâra ale'l-kavm, gloss:kavmin üzerine baskın yaptı, source:"memory"}. Birinci ayetin kelimesi zaten bu işle tanımlanır: {ar:العادية الخيل المغيرة, tr:el-âdiyetu'l-haylu'l-muğîra, gloss:"âdiye", baskın yapan atlardır, source:"ع د و,B001"}. Yani koşan at, tanımı gereği baskına koşan attır. Aynı kökte saldırının ahlaki adı da vardır: {ar:العدوان الظلم الصراح, tr:el-udvânu'z-zulmu's-surâh, gloss:"udvân" apaçık haksızlıktır, source:"ع د و,B001"}. Saldırının hedefi de bu köktendir: {ar:العَدُوّ ضد الولي والجمع الأعداء, tr:el-aduvvu ziddu'l-veliyyi ve'l-cem'u'l-a'dâ', gloss:düşman, dostun karşıtıdır; çoğulu "a'dâ"dır, source:"ع د و,B003"}.

[¶9] Baskının işleyişi saatine bağlıdır. Baskıncılar geceyi yolda geçirir ve ilk ışıkta konağa varır. O saatte konaklayanlar ya uykudadır ya da yeni uyanmaktadır, silahlanacak vakitleri yoktur. Bu yüzden sabah, baskının kendi adı olmuştur: {ar:يوم الصباح يوم الغارة, tr:yevmu's-sabâhi yevmu'l-ğâra, gloss:"sabah günü", baskın günüdür, source:"ص ب ح,B004"}. Aynı kökten fiil ile baskına uğrayanların çığlığı da tek bir söyleyişte birleşir: {ar:في الحرب صبحناهم أي غاديناهم بالخيل ونادوا يا صباحاه إذا استغاثوا, tr:fi'l-harbi sabbahnâhum, ey ğâdeynâhum bi'l-hayl, ve nâdev yâ sabâhâh izâ isteğâsû, gloss:savaşta "onlara sabahladık" yani atlarla sabah erkenden üstlerine vardık denir; yardım isteyenler de "Vay sabah!" diye bağırır, source:"ص ب ح,B004"}. Kelimenin sade kullanımı da aynı yöndedir: {ar:صبحته إذا أتيته صباحا, tr:sabahtuhû izâ eteytuhû sabâhan, gloss:birine sabahleyin vardığında "onu sabahladım" denir, source:"ص ب ح,B002"}.

[¶10] Dördüncü ayet baskının görüntüsünü verir: {ar:فَأَثَرْنَ بِهِۦ نَقْعًا, tr:fe-eserne bihî nak'â, gloss:derken orada toz kaldırdılar, source:100:4}. Fiil havalanan toza gider: {ar:ثار الغبار يثور ثورا وثورانا أي سطع, tr:sâra'l-ğubâru yesûru sevren ve sevarânen, ey sata'a, gloss:toz kalktı, yani yükselip yayıldı, source:"ث و ر,B001"}. Fiilin kökü birinin üstüne çullanmayı da adlandırır: {ar:ثار به الناس أي وثبوا عليه, tr:sâra bihi'n-nâsu, ey vesebû aleyh, gloss:insanlar onun üstüne atıldı, source:"ث و ر,B003"}. "Nak'", yükselen tozdur: {ar:النقع الغبار المرتفع, tr:en-nak'u'l-ğubâru'l-murtefi', gloss:"nak'" yükselen tozdur, source:"ن ق ع,B004"}. Aynı kelimenin yanında bir ses de duyulur: {ar:النقع رفع الصوت, tr:en-nak'u ref'u's-savt, gloss:"nak'" sesi yükseltmektir, source:"ن ق ع,B005"}. Bu ses kesintisiz sürer: {ar:نقع بصوته وأنقع صوته إذا تابعه, tr:neka'a bi-savtihî ve enka'a savtehû izâ tâbe'ah, gloss:sesini ardı ardına sürdürdüğünde "neka'a" denir, source:"ن ق ع,B005"}. Yükselen toz bulutunun yanında, baskına uğrayan konağın "Vay sabah!" çığlığı duyulur. Ayetteki "bihî" zamiri tozu az önce anılan o sabaha ve o hamleye bağlar. Toz, baskının anında ve yerinde kalkar.

[¶11] Beşinci ayet hamlenin nerede bittiğini söyler: {ar:فَوَسَطْنَ بِهِۦ جَمْعًا, tr:fe-vasatne bihî cem'â, gloss:derken orada bir topluluğun ortasına daldılar, source:100:5}. Fiil, bir kalabalığın içine girip ortasında durmaktır: {ar:وسط فلان جماعة من الناس وهو يسطهم إذا صار في وسطهم, tr:vasata fulânun cemâ'aten mine'n-nâs, ve huve yesıtuhum, izâ sâra fî vasatihim, gloss:biri bir topluluğun ortasına vardığında "onları ortaladı" denir, source:"و س ط,B003"}. "Cem'" bir araya gelmiş insan topluluğudur: {ar:الجمع اسم لجماعة الناس, tr:el-cem'u ismun li-cemâ'ati'n-nâs, gloss:"cem'" insan topluluğunun adıdır, source:"ج م ع,B002"}. Bu topluluk çoğu zaman karışıktır: {ar:الجماع ما تجمع من أشابة الناس وأخلاطهم, tr:el-cimâ'u mâ tecemma'a min uşâbeti'n-nâsi ve ahlâtihim, gloss:"cimâ'", karışık, derme çatma bir halk kalabalığıdır, source:"ج م ع,B002"}. Hamle kalabalığın kenarında durmaz, toplanmış bir halkın tam merkezinde biter. Bu, kaçacak yerin kalmadığı anı gösterir. Sekizinci ayetin kelimesi bu sahneye yeniden döner: {ar:شد على العدو إذا حمل عليه, tr:şedde ale'l-aduvvi izâ hamele aleyh, gloss:düşmana saldırdığında "şedde" denir, source:"ش د د,B003"}. Baskının ardından gelen paylaşım da dördüncü ayetin kelimesinde durur: {ar:النقيعة ما نحر من النهب قبل القسم, tr:en-nakî'atu mâ nuhira mine'n-nehbi kable'l-kasm, gloss:"nakî'a", ganimet bölüşülmeden önce boğazlanan hayvandır, source:"ن ق ع,B003"}.

[¶12] Düz bir anlatım, atların hızla koşup baskın yaptığını söylemekle yetinirdi. Kelimeler ise başka şeyleri de duyurur. Saldırının tanımında "apaçık haksızlık" vardır, baskının adı bir saattir, toz ve çığlık aynı kelimededir ve hamle kalabalığın ortasında biter. Bu ani, kaçışsız sabah surenin sonundaki güne bir ön hazırlıktır. Kur'an azabın gelişini de bir şafak baskını gibi anlatır. Azabı acele isteyenlere Allah önce {ar:أَفَبِعَذَابِنَا يَسْتَعْجِلُونَ, tr:e-fe-bi-azâbinâ yesta'cilûn, gloss:azabımızı mı acele istiyorlar, source:37:176} diye sorar, sonra şöyle der: {ar:فَإِذَا نَزَلَ بِسَاحَتِهِمْ فَسَآءَ صَبَاحُ ٱلْمُنذَرِينَ, tr:fe-izâ nezele bi-sâhatihim fe-sâe sabâhu'l-munzerîn, gloss:o, avlularına indiğinde, uyarılmışların sabahı ne kötüdür, source:37:177}. Azap yurdun avlusuna iner ve bunun vakti "sabah"tır. Lut'a gelen elçiler ona ailesiyle geceleyin yola çıkmasını söyler ve {ar:إِنَّ مَوْعِدَهُمُ ٱلصُّبْحُ ۚ أَلَيْسَ ٱلصُّبْحُ بِقَرِيبٍ, tr:inne mev'idehumu's-subh, e-leyse's-subhu bi-karîb, gloss:onların buluşma vakti sabahtır; sabah yakın değil mi, source:11:81} diye ekler. Hicr halkı için {ar:فَأَخَذَتْهُمُ ٱلصَّيْحَةُ مُصْبِحِينَ, tr:fe-ehazethumu's-sayhatu musbihîn, gloss:sabaha girerlerken onları o çığlık yakaladı, source:15:83} denir. Lut kavmi için aynı fiil kullanılır: {ar:وَلَقَدْ صَبَّحَهُم بُكْرَةً عَذَابٌ مُّسْتَقِرٌّ, tr:ve le-kad sabbahahum bukraten azâbun mustakır, gloss:andolsun, erkenden kalıcı bir azap onlara sabahladı, source:54:38}. Kur'an atlı akın görüntüsünü İblis'e verilen izinde de kullanır: {ar:وَأَجْلِبْ عَلَيْهِم بِخَيْلِكَ وَرَجِلِكَ, tr:ve eclib aleyhim bi-haylike ve recilik, gloss:atlılarınla ve yayalarınla üzerlerine yaygarayla yürü, source:17:64}. Müminlere verilen buyrukta ise atlar ile "düşman" kelimesi aynı ayette durur: {ar:وَمِن رِّبَاطِ ٱلْخَيْلِ تُرْهِبُونَ بِهِۦ عَدُوَّ ٱللَّهِ وَعَدُوَّكُمْ, tr:ve min ribâti'l-hayli turhibûne bihî aduvva'llâhi ve aduvvekum, gloss:bağlanıp hazır tutulan atlardan; onlarla Allah'ın düşmanını ve sizin düşmanınızı caydırırsınız, source:8:60}.

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/ledger.md =====
- not developed: chain 7 (rain on the land) as its own section - merged into chain 6 as one image of kenûd
- not developed: chain 9 (shared pot) as its own section - merged into chain 8 as the counter-scene of the closed hand
- not developed: غ ي ر B001 "God's rain/provision" member in chains 6 and 7 - wrong root for al-mughīrāt, dropped
- not developed: ضبح as owl and echo calls (chain 4) - relies on pre-Islamic lore outside the Quran, dropped
- not developed: ربيون "great crowds" (chain 11) - too loose a link to rabb, dropped
- not developed: the map's meysir lore (chain 9) and its commentators remark (chain 6) - reports from outside the Quran, dropped
- memory: al-mughīrāt is the form IV participle of أغار "to raid", root غ و ر
- memory: غار يغير "to provide rain" is a separate verb and not the root of al-mughīrāt
- memory: the preposition عن in 38:32 can mean both "because of" and "away from"

===== passages from the discovery list (211) =====
## strong (140)

- (2:190) [luna: strong; terra: strong; basis: contrast+root+theme] وَقَٰتِلُوا۟ فِى سَبِيلِ ٱللَّهِ ٱلَّذِينَ يُقَٰتِلُونَكُمْ وَلَا تَعْتَدُوٓا۟ ۚ إِنَّ ٱللَّهَ لَا يُحِبُّ ٱلْمُعْتَدِينَ
  Unverified discovery rationale: luna: The command “do not transgress” (تَعْتَدُوا) uses the aggression root named in the section's gloss of ʿudwān as manifest injustice, and sets a clear limit on fighting even in a military encounter. | terra: The battle command is bounded by ولا تعتدوا; it names transgression with the section's ع د و root and distinguishes fighting aggressors from the raid's “plain injustice.”
- (2:193) [luna: strong (missing-ayat turn); basis: contrast+neighbour+root] وَقَٰتِلُوهُمْ حَتَّىٰ لَا تَكُونَ فِتْنَةٌۭ وَيَكُونَ ٱلدِّينُ لِلَّهِ ۖ فَإِنِ ٱنتَهَوْا۟ فَلَا عُدْوَٰنَ إِلَّا عَلَى ٱلظَّٰلِمِينَ
  Unverified discovery rationale: luna: Continuing the fighting rules near 2:190, it says that if opponents cease there is to be no aggression (عُدْوَانَ) except against wrongdoers; this gives the section's ʿudwān root a precise boundary in a combat context.
- (3:152) [luna: medium (missing-ayat turn); terra: strong (missing-ayat turn); basis: contrast+scene+theme] وَلَقَدْ صَدَقَكُمُ ٱللَّهُ وَعْدَهُۥٓ إِذْ تَحُسُّونَهُم بِإِذْنِهِۦ ۖ حَتَّىٰٓ إِذَا فَشِلْتُمْ وَتَنَٰزَعْتُمْ فِى ٱلْأَمْرِ وَعَصَيْتُم مِّنۢ بَعْدِ مَآ أَرَىٰكُم مَّا تُحِبُّونَ ۚ مِنكُم مَّن يُرِيدُ ٱلدُّنْيَا وَمِنكُم مَّن يُرِيدُ ٱلْءَاخِرَةَ ۚ ثُمَّ صَرَفَكُمْ عَنْهُمْ لِيَبْتَلِيَكُمْ ۖ وَلَقَدْ عَفَا عَنكُمْ ۗ وَٱللَّهُ ذُو فَضْلٍ عَلَى ٱلْمُؤْمِنِينَ
  Unverified discovery rationale: luna: At Uhud, the fighting group falters and divides between desire for this world and the Hereafter; this is a battle-context counterpoint to the section's link from a cavalry charge and spoils to intense attachment to worldly “good.” | terra: During battle some believers desire this world and disobey after seeing what they love; the resulting reversal connects martial advance and spoil-desire to the section's transition from raid to intense love of goods.
- (3:155) [terra: strong (missing-ayat turn); basis: contrast+root+scene] إِنَّ ٱلَّذِينَ تَوَلَّوْا۟ مِنكُمْ يَوْمَ ٱلْتَقَى ٱلْجَمْعَانِ إِنَّمَا ٱسْتَزَلَّهُمُ ٱلشَّيْطَٰنُ بِبَعْضِ مَا كَسَبُوا۟ ۖ وَلَقَدْ عَفَا ٱللَّهُ عَنْهُمْ ۗ إِنَّ ٱللَّهَ غَفُورٌ حَلِيمٌۭ
  Unverified discovery rationale: terra: Some believers turn away on the day التقى الجمعان; the repeated “two hosts met” wording shows a gathered battle collision from the viewpoint of those who flee it.
- (3:166) [terra: strong (missing-ayat turn); basis: root+scene+theme] وَمَآ أَصَٰبَكُمْ يَوْمَ ٱلْتَقَى ٱلْجَمْعَانِ فَبِإِذْنِ ٱللَّهِ وَلِيَعْلَمَ ٱلْمُؤْمِنِينَ
  Unverified discovery rationale: terra: What struck the believers on the day التقى الجمعان occurred by God's permission; the meeting of two gathered forces becomes an occasion of disclosure and judgment.
- (4:45) [terra: strong; basis: contrast+root] وَٱللَّهُ أَعْلَمُ بِأَعْدَآئِكُمْ ۚ وَكَفَىٰ بِٱللَّهِ وَلِيًّۭا وَكَفَىٰ بِٱللَّهِ نَصِيرًۭا
  Unverified discovery rationale: terra: Allah knows the believers' enemies and is sufficient وليا and نصيرا; enemy and protecting ally occur together, clarifying the relational opposition named in the section.
- (4:94) [terra: strong (missing-ayat turn); basis: contrast+scene+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوٓا۟ إِذَا ضَرَبْتُمْ فِى سَبِيلِ ٱللَّهِ فَتَبَيَّنُوا۟ وَلَا تَقُولُوا۟ لِمَنْ أَلْقَىٰٓ إِلَيْكُمُ ٱلسَّلَٰمَ لَسْتَ مُؤْمِنًۭا تَبْتَغُونَ عَرَضَ ٱلْحَيَوٰةِ ٱلدُّنْيَا فَعِندَ ٱللَّهِ مَغَانِمُ كَثِيرَةٌۭ ۚ كَذَٰلِكَ كُنتُم مِّن قَبْلُ فَمَنَّ ٱللَّهُ عَلَيْكُمْ فَتَبَيَّنُوٓا۟ ۚ إِنَّ ٱللَّهَ كَانَ بِمَا تَعْمَلُونَ خَبِيرًۭا
  Unverified discovery rationale: terra: Those setting out are told to investigate and not treat a peace-greeting person as an enemy out of desire for worldly gain; it directly binds battlefield identification and booty to the section's moral warning about aggression.
- (4:101) [terra: strong (missing-ayat turn); basis: neighbour+scene] وَإِذَا ضَرَبْتُمْ فِى ٱلْأَرْضِ فَلَيْسَ عَلَيْكُمْ جُنَاحٌ أَن تَقْصُرُوا۟ مِنَ ٱلصَّلَوٰةِ إِنْ خِفْتُمْ أَن يَفْتِنَكُمُ ٱلَّذِينَ كَفَرُوٓا۟ ۚ إِنَّ ٱلْكَٰفِرِينَ كَانُوا۟ لَكُمْ عَدُوًّۭا مُّبِينًۭا
  Unverified discovery rationale: terra: Travelers may shorten prayer when fearing that hostile unbelievers will attack them; it states the mobile party's vulnerability that the armed formation in 4:102 is designed to answer.
- (4:102) [terra: strong; basis: contrast+scene] وَإِذَا كُنتَ فِيهِمْ فَأَقَمْتَ لَهُمُ ٱلصَّلَوٰةَ فَلْتَقُمْ طَآئِفَةٌۭ مِّنْهُم مَّعَكَ وَلْيَأْخُذُوٓا۟ أَسْلِحَتَهُمْ فَإِذَا سَجَدُوا۟ فَلْيَكُونُوا۟ مِن وَرَآئِكُمْ وَلْتَأْتِ طَآئِفَةٌ أُخْرَىٰ لَمْ يُصَلُّوا۟ فَلْيُصَلُّوا۟ مَعَكَ وَلْيَأْخُذُوا۟ حِذْرَهُمْ وَأَسْلِحَتَهُمْ ۗ وَدَّ ٱلَّذِينَ كَفَرُوا۟ لَوْ تَغْفُلُونَ عَنْ أَسْلِحَتِكُمْ وَأَمْتِعَتِكُمْ فَيَمِيلُونَ عَلَيْكُم مَّيْلَةًۭ وَٰحِدَةًۭ ۚ وَلَا جُنَاحَ عَلَيْكُمْ إِن كَانَ بِكُمْ أَذًۭى مِّن مَّطَرٍ أَوْ كُنتُم مَّرْضَىٰٓ أَن تَضَعُوٓا۟ أَسْلِحَتَكُمْ ۖ وَخُذُوا۟ حِذْرَكُمْ ۗ إِنَّ ٱللَّهَ أَعَدَّ لِلْكَٰفِرِينَ عَذَابًۭا مُّهِينًۭا
  Unverified discovery rationale: terra: The enemy wishes believers to become heedless of weapons and baggage so it can fall on them ميلة واحدة, in one assault; this directly explains the tactical advantage of catching the camp unarmed, while the prayer guard provides the defensive reversal.
- (5:2) [luna: strong; terra: strong; basis: contrast+root+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ لَا تُحِلُّوا۟ شَعَٰٓئِرَ ٱللَّهِ وَلَا ٱلشَّهْرَ ٱلْحَرَامَ وَلَا ٱلْهَدْىَ وَلَا ٱلْقَلَٰٓئِدَ وَلَآ ءَآمِّينَ ٱلْبَيْتَ ٱلْحَرَامَ يَبْتَغُونَ فَضْلًۭا مِّن رَّبِّهِمْ وَرِضْوَٰنًۭا ۚ وَإِذَا حَلَلْتُمْ فَٱصْطَادُوا۟ ۚ وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ أَن صَدُّوكُمْ عَنِ ٱلْمَسْجِدِ ٱلْحَرَامِ أَن تَعْتَدُوا۟ ۘ وَتَعَاوَنُوا۟ عَلَى ٱلْبِرِّ وَٱلتَّقْوَىٰ ۖ وَلَا تَعَاوَنُوا۟ عَلَى ٱلْإِثْمِ وَٱلْعُدْوَٰنِ ۚ وَٱتَّقُوا۟ ٱللَّهَ ۖ إِنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
  Unverified discovery rationale: luna: The verse forbids hostility over being barred from the Sacred Mosque from turning into transgression; it gives a concrete moral boundary for the section's assault-and-injustice reading. | terra: Hatred of a people must not drive believers أن تعتدوا; the ayah directly prevents an enemy relation from turning into the section's morally named aggression.
- (5:8) [luna: strong; terra: contrast; basis: contrast+root+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ كُونُوا۟ قَوَّٰمِينَ لِلَّهِ شُهَدَآءَ بِٱلْقِسْطِ ۖ وَلَا يَجْرِمَنَّكُمْ شَنَـَٔانُ قَوْمٍ عَلَىٰٓ أَلَّا تَعْدِلُوا۟ ۚ ٱعْدِلُوا۟ هُوَ أَقْرَبُ لِلتَّقْوَىٰ ۖ وَٱتَّقُوا۟ ٱللَّهَ ۚ إِنَّ ٱللَّهَ خَبِيرٌۢ بِمَا تَعْمَلُونَ
  Unverified discovery rationale: luna: Even hatred of a people must not lead believers away from justice; this checks the slide from identifying someone as an enemy to treating them unjustly, a distinction raised by the section's ʿaduww/ʿudwān note. | terra: Enmity toward a people must not make believers abandon justice; this supplies the ethical reversal of the section's definition of عدوان as manifest wrongdoing.
- (6:31) [terra: strong; basis: theme] قَدْ خَسِرَ ٱلَّذِينَ كَذَّبُوا۟ بِلِقَآءِ ٱللَّهِ ۖ حَتَّىٰٓ إِذَا جَآءَتْهُمُ ٱلسَّاعَةُ بَغْتَةًۭ قَالُوا۟ يَٰحَسْرَتَنَا عَلَىٰ مَا فَرَّطْنَا فِيهَا وَهُمْ يَحْمِلُونَ أَوْزَارَهُمْ عَلَىٰ ظُهُورِهِمْ ۚ أَلَا سَآءَ مَا يَزِرُونَ
  Unverified discovery rationale: terra: The Hour comes بغتة and its deniers immediately bear their burdens in regret; the sudden transition from denial to irreversible reckoning matches the section's preparatory function.
- (6:44) [terra: strong; basis: scene+theme] فَلَمَّا نَسُوا۟ مَا ذُكِّرُوا۟ بِهِۦ فَتَحْنَا عَلَيْهِمْ أَبْوَٰبَ كُلِّ شَىْءٍ حَتَّىٰٓ إِذَا فَرِحُوا۟ بِمَآ أُوتُوٓا۟ أَخَذْنَٰهُم بَغْتَةًۭ فَإِذَا هُم مُّبْلِسُونَ
  Unverified discovery rationale: terra: After every gate of plenty is opened and the people rejoice, they are seized بغتة; apparent ease immediately before capture parallels the sleeping camp's false security.
- (6:47) [luna: medium; terra: strong; basis: contrast+scene+theme] قُلْ أَرَءَيْتَكُمْ إِنْ أَتَىٰكُمْ عَذَابُ ٱللَّهِ بَغْتَةً أَوْ جَهْرَةً هَلْ يُهْلَكُ إِلَّا ٱلْقَوْمُ ٱلظَّٰلِمُونَ
  Unverified discovery rationale: luna: It asks who besides wrongdoers would be destroyed if God's punishment came suddenly or openly; the two modes clarify the section's sudden dawn assault as one form of an openly destructive arrival. | terra: The address asks about punishment arriving بغتة أو جهرة and says only the wrongdoing people are destroyed; it joins surprise arrival to the section's moral concern with injustice.
- (7:4) [luna: strong; terra: strong; basis: scene+theme] وَكَم مِّن قَرْيَةٍ أَهْلَكْنَٰهَا فَجَآءَهَا بَأْسُنَا بَيَٰتًا أَوْ هُمْ قَآئِلُونَ
  Unverified discovery rationale: luna: Destroyed towns are struck at night or while their people sleep at midday; the verse supplies the broader Qur'anic image of punishment reaching a settlement during vulnerable hours. | terra: Divine might comes upon a town بياتا أو هم قائلون, by night or while its people rest at midday; an inhabited place is struck precisely when repose leaves it unready.
