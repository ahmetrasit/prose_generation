Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 9 of 14 ("Su: toprağı büyüten bulut ve kuyunun ağzı"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 9 (prose paragraphs numbered) =====
[¶45] Su, bu surede iki yoldan gelir: gökten yağan yağmur ve yerden çekilen kuyu suyu. Gökte katman katman bir bulut belirir. Ona "Rab" kökünden bir ad verilir, çünkü bitkileri büyütür: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâbü's-sehâb, sümmiye bi-zâlike li-ennehû yerubbü'n-nebât, gloss:rabâb buluttur; bitkileri büyüttüğü için bu adı almıştır, source:"ر ب ب,B008"}. Bulutun katmanları da tarif edilir: {ar:الربابة: السحابة التي قد ركب بعضها بعضا, tr:er-rabâbetü's-sehâbetü'lletî kad rekibe ba'duhâ ba'dâ, gloss:rabâbe, katmanları üst üste binmiş buluttur, source:"ر ب ب,B008"}. Bulut ve güney rüzgârı bir yerde kalır: {ar:أربت الجنوب والسحابة أي دامت, tr:erabbeti'l-cenûbü ve's-sehâbe, gloss:güney rüzgârı ve bulut bir yerde kalıp sürdü, source:"ر ب ب,B007"}. Bu güney rüzgârının bir adı "en'amte" kelimesiyle aynı köktendir: {ar:النعامى ريح الجنوب لأنها أبل الرياح وأرطبها, tr:en-neâmâ rîhu'l-cenûb, li-ennehâ eballü'r-riyâhi ve ertabühâ, gloss:neâmâ güney rüzgârıdır, çünkü rüzgârların en ıslak ve en nemli olanıdır, source:"ن ع م,B009"}. Böylece ikinci ayetin "Rab" kelimesi ile yedinci ayetin "en'amte" kelimesi, aynı nemli rüzgârın iki adında buluşur. Gök, yağmur ve bitki aynı adla anılır: {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-Arabü tüsemmi's-sehâbe semâen ve'l-matara semâ', gloss:Araplar buluta da yağmura da sema derler, source:"س م و,B004"}, {ar:يسموا النبات سماء, tr:yüsemmû'n-nebâte semâ', gloss:bitkiye de sema derler, source:"س م و,B004"}. "Bism" için anılan ikinci kökte yılın ilk yağmuru toprağa damga vurur: {ar:الوسمي أول مطر السنة يسم الأرض بالنبات, tr:el-vesmiyyü evvelü matari's-sene, yesimü'l-arda bi'n-nebât, gloss:vesmî, yılın ilk yağmurudur; toprağı bitkiyle damgalar, source:"و س م,B003"}. Yağmurun bıraktığı yeşillik, dağlama izinin toprağa yazılmış halidir.

[¶46] Yağmurun sonuçları da aynı ailelerde anlatılır. Yazın bile solmayan körpe bir ot "Rab" köküyle anılır: {ar:الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف, tr:er-ribbetü bakletün nâime, gloss:ribbe, yazın solmayan birçok körpe bitkinin adıdır, source:"ر ب ب,B012"}. Toplanmış bol su da aynı köktendir: {ar:الربب، بالفتح: الماء الكثير، ويقال العذب, tr:er-rabab: el-mâü'l-kesîr, gloss:rabab bol sudur, tatlı su da denir, source:"ر ب ب,B013"}. Bu adın sebebi suyun bir araya gelmesidir: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabab... sümmiye bi-zâlike li'ctimâih, gloss:rabab bol sudur; toplandığı için bu adı almıştır, source:"ر ب ب,B013"}. Yedinci ayetteki "gayr" kelimesinin ailesinde yağmurla halkın durumunun düzelmesi vardır: {ar:غارهم الله تعالى بالغيث أي أصلح شأنهم ونفعهم, tr:gârahümullâhü bi'l-gays, gloss:Allah onlara yağmur verdi, yani durumlarını düzeltti ve onlara fayda verdi, source:"غ ي ر,B001"}. Aynı fiil su vermeyi de anlatır: {ar:سقاهم, tr:sekâhüm, gloss:onlara su verdi, source:"غ ي ر,B001"}. Hayatın tazeliği "nimet" kelimesiyle anılır: {ar:نعمة العيش حسنه وغضارته, tr:nu'metü'l-ayşi hüsnühû ve gadâratüh, gloss:hayatın nimeti onun güzelliği ve tazeliğidir, source:"ن ع م,B002"}. Toprak da beğenilir: {ar:أحمدت الأرض إذا رضيت سكناها أو مرعاها, tr:ahmedtü'l-ard, gloss:toprağı beğendim, orada oturmaktan ya da otlağından hoşnut kaldım, source:"ح م د,B002"}. Bu, ikinci ayetteki "hamd" kelimesinin toprağa yönelmiş halidir.

[¶47] Kuyu da aynı aileleri bir araya getirir. Derin ve dolu kuyu "âlem" kelimesinin ailesindendir: {ar:العيلم الركية الكثيرة الماء, tr:el-ayleme'r-rakiyyetü'l-kesîretü'l-mâ', gloss:aylem, suyu bol kuyudur, source:"ع ل م,B005"}. Kuyunun ağzında iki direğin üstüne bir kiriş konur. Bu kirişin adı yedinci ayetteki "en'amte" kelimesiyle aynı köktendir: {ar:النعامة الخشبة المعترضة على الزرنوقين, tr:en-neâmetü'l-haşebetü'l-mu'terıdatü ale'z-zürnûkayn, gloss:neâme, iki direğin üstüne enlemesine konan kiriştir, source:"ن ع م,B007"}. Aynı kelime kuyunun başındaki gölgeliği de anlatır: {ar:النعامة المظلة في الجبل وعلى رأس البئر تشبيها بالنعامة في الهيئة, tr:en-neâmetü'l-mizalletü fi'l-cebeli ve alâ re'si'l-bi'r, gloss:neâme, dağda ve kuyu başında, devekuşuna benzeyen gölgeliktir, source:"ن ع م,B007"}. Kirişten makara sarkar. Makaranın adı da altıncı ayetteki "müstakîm" kelimesiyle aynı köktendir: {ar:القامة البكرة التي يستقى بها الماء؛ النعامة الخشبة المعترضة ثم تعلق القامة, tr:el-kâmetü'l-bekretü'lletî yüsteka bihe'l-mâ', en-neâmetü'l-haşebetü'l-mu'terıdatü sümme tu'allaku'l-kâme, gloss:kâme, su çekilen makaradır; neâme enlemesine kiriştir, sonra kâme ona asılır, source:"ق و م,B012"}. Böylece surenin iki kelimesi tek bir cümlede tek bir alet olarak kuyunun ağzında birbirine bağlanır: kiriş ve ondan sarkan makara. Su, işleri ayakta tutan şeydir: {ar:الماء ملك أمر أي يقوم به الأمر, tr:el-mâü milâku emrin, ey yekûmü bihi'l-emr, gloss:su işin dayanağıdır, yani iş onunla ayakta durur, source:"م ل ك,B007"}. Yolcunun yanındaki su onun işini elinde tutar: {ar:والملك الماء يكون مع المسافر لأنه إذا كان معه ملك أمره, tr:ve'l-melk el-mâü yekûnü mea'l-müsâfir, gloss:melk, yolcunun yanındaki sudur, çünkü su yanındaysa işini elinde tutar, source:"م ل ك,B007"}. Bir kabile kuyularını hükümdarları olarak anar: {ar:مياهنا ملوكنا, tr:miyâhunâ mülûkünâ, gloss:sularımız bizim hükümdarlarımızdır, source:"م ل ك,B007"}. "Kıvâm" ile "milâk" kelimeleri birbirini açıklar: {ar:قوام الأمر ملاكه, tr:kıvâmü'l-emri milâkuh, gloss:işin dayanağı onu bir arada tutan şeydir, source:"ق و م,B009"}. Geçim de böyle tanımlanır: {ar:القوام من العيش ما يقيمك ويغنيك, tr:el-kıvâmü mine'l-ayşi mâ yukîmuke ve yuğnîk, gloss:geçimden kıvâm, seni ayakta tutan ve ihtiyacını karşılayan şeydir, source:"ق و م,B009"}. Dördüncü ayetteki "mâlik" ve altıncı ayetteki "müstakîm" kelimeleri suyun yaptığı işte birleşir. İkisi de bir şeyi ayakta tutmayı anlatır.

[¶48] Düz bir meal bu kelimelerde su görmez. Görüntü ise surenin büyüten Rabbini, bitkiyi büyüten bulutun yanında duyurur. Dosdoğru yolu da ayakta tutan bir makaranın yanında duyurur. Yol yürünürken susuz kalınmaz. Yolcunun işi, yanında taşıdığı su sayesinde ayakta durur.

[¶49] Kur'an'da yağmur ile rahmet birlikte anılır: {ar:وَهُوَ ٱلَّذِى يُنَزِّلُ ٱلْغَيْثَ مِنۢ بَعْدِ مَا قَنَطُوا۟ وَيَنشُرُ رَحْمَتَهُۥ ۚ وَهُوَ ٱلْوَلِىُّ ٱلْحَمِيدُ, tr:ve hüvellezî yünezzilü'l-gayse min ba'di mâ kanetû ve yenşüru rahmeteh, ve hüve'l-veliyyü'l-hamîd, gloss:umutlarını kestikten sonra yağmuru indiren ve rahmetini yayan O'dur; dost ve övülmeye layık olan O'dur, source:42:28}. Bu ayette yağmur, rahmet ve hamd yan yanadır. Rüzgâr, rahmetin önünden müjdeci olarak gelir: {ar:يُرْسِلُ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۖ حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًۭا ثِقَالًۭا, tr:yürsilü'r-riyâha büşran beyne yedey rahmetih, hattâ izâ ekallet sehâben sikâlâ, gloss:rüzgârları rahmetinin önünden müjdeci gönderir; sonunda ağır bulutları yüklendiklerinde, source:7:57}. Ayetin sonu dirilişe bağlanır: {ar:كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ, tr:kezâlike nuhricu'l-mevtâ, gloss:ölüleri de böyle çıkarırız, source:7:57}. Rüzgâr bulutu gökte yayar: {ar:فَتُثِيرُ سَحَابًۭا فَيَبْسُطُهُۥ فِى ٱلسَّمَآءِ, tr:fe-tüsîru sehâben fe-yebsutuhû fi's-semâ', gloss:rüzgârlar bulutu harekete geçirir, Allah da onu gökte yayar, source:30:48}. Ardından izlere bakmak istenir: {ar:فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ, tr:fenzur ilâ âsâri rahmetillâhi keyfe yuhyi'l-arda ba'de mevtihâ, gloss:Allah'ın rahmetinin izlerine bak: toprağı ölümünden sonra nasıl diriltiyor, source:30:50}. Toprağı damgalayan yağmurun izi burada rahmetin izidir. İnsana yemeğine bakması söylenir: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânü ilâ taâmih, gloss:insan yemeğine bir baksın, source:80:24}, {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:suyu bol bol döktük, source:80:25}. Sayım şöyle biter: {ar:مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ, tr:metâan leküm ve li-en'âmiküm, gloss:size ve hayvanlarınıza bir geçim olarak, source:80:32}. Su kurak toprağa sürülür: {ar:أَنَّا نَسُوقُ ٱلْمَآءَ إِلَى ٱلْأَرْضِ ٱلْجُرُزِ, tr:ennâ nesûku'l-mâe ile'l-ardı'l-cüruz, gloss:suyu çorak toprağa sürüyoruz, source:32:27}.

[¶50] Kuyunun Kur'an'daki sahnesi Musa'nın yolculuğudur. Musa Medyen'e yönelir, yolun ortasına iletilmeyi diler {source:28:22} ve sonra suya varır: {ar:وَلَمَّا وَرَدَ مَآءَ مَدْيَنَ وَجَدَ عَلَيْهِ أُمَّةًۭ مِّنَ ٱلنَّاسِ يَسْقُونَ, tr:ve lemmâ verade mâe Medyene vecede aleyhi ümmeten mine'n-nâsi yeskûn, gloss:Medyen suyuna varınca, orada hayvanlarını sulayan bir insan topluluğu buldu, source:28:23}. Sürülerini sulayamayan iki kadına yardım eder: {ar:فَسَقَىٰ لَهُمَا ثُمَّ تَوَلَّىٰٓ إِلَى ٱلظِّلِّ فَقَالَ رَبِّ إِنِّى لِمَآ أَنزَلْتَ إِلَىَّ مِنْ خَيْرٍۢ فَقِيرٌۭ, tr:fe-sekâ lehümâ sümme tevellâ ile'z-zıll, fe-kâle rabbi innî li-mâ enzelte ileyye min hayrin fakîr, gloss:onlar için suladı, sonra gölgeye çekildi ve "Rabbim, bana indireceğin her hayra muhtacım" dedi, source:28:24}. Yol, kuyu, su vermek ("sekâhüm"), gölge ve "Rab" bu tek sahnede yan yanadır. Yusuf'un kardeşleri onu kuyunun dibine atmayı konuşur: {ar:وَأَلْقُوهُ فِى غَيَٰبَتِ ٱلْجُبِّ يَلْتَقِطْهُ بَعْضُ ٱلسَّيَّارَةِ, tr:ve elkûhü fî gayâbeti'l-cübbi yeltekıthü ba'du's-seyyâra, gloss:onu kuyunun karanlık dibine atın, yolculardan biri onu alır, source:12:10}. Gerçekten de bir kervan gelir ve kuyudan su çekilirken çocuk ortaya çıkar: {ar:فَأَرْسَلُوا۟ وَارِدَهُمْ فَأَدْلَىٰ دَلْوَهُۥ ۖ قَالَ يَٰبُشْرَىٰ هَٰذَا غُلَٰمٌۭ, tr:fe-erselû vâridehüm fe-edlâ delveh, kâle yâ büşrâ hâzâ gulâm, gloss:sucularını gönderdiler, o da kovasını sarkıttı ve "müjde, bu bir oğlan" dedi, source:12:19}. Suyun yitirilmesi de sorulur: {ar:قُلْ أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًۭا فَمَن يَأْتِيكُم بِمَآءٍۢ مَّعِينٍۭ, tr:kul e-raeytüm in asbaha mâüküm gavran fe-men ye'tîküm bi-mâin maîn, gloss:de ki: suyunuz yerin dibine çekilse, size akan bir suyu kim getirir, source:67:30}. İbrahim, âlemlerin Rabbini anlatırken yola iletmeyle su vermeyi art arda sayar: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:ellezî halakanî fe-hüve yehdîn, gloss:beni yaratan, bana yolu gösteren O'dur, source:26:78}, {ar:وَٱلَّذِى هُوَ يُطْعِمُنِى وَيَسْقِينِ, tr:ve'llezî hüve yut'imunî ve yeskîn, gloss:beni yediren ve içiren O'dur, source:26:79}.

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/ledger.md =====
- not developed: و ل ه members of ٱللَّهِ (road, womb, herd, well, passing) - alternative derivation, root identity not established
- not developed: hadith items in womb, herd and leaning chains - outside the Quran
- not developed: ن ع م B012 walking on soles - too remote
- not developed: ع و ن B005 strength matching age - adds nothing
- not developed: ق و م B012 ayn reading of qāma - recorded as wrong
- not developed: Debt and scale chain - merged into Day of reckoning
- not developed: Well-head chain - merged into Rain as water
- memory: dīn (kasra) vs dayn (fatha) are distinct words of one root
- memory: maghḍūb is a passive participle naming no agent; anʿamta names "you" as agent
- memory: fronted iyyāka marks exclusivity ("only you")
- memory: qāma also means "stopped dead" (beast), as well as "stood up"

===== passages from the discovery list (178) =====
## strong (88)

- (2:22) [luna: medium; terra: strong; basis: root+scene+theme] ٱلَّذِى جَعَلَ لَكُمُ ٱلْأَرْضَ فِرَٰشًۭا وَٱلسَّمَآءَ بِنَآءًۭ وَأَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجَ بِهِۦ مِنَ ٱلثَّمَرَٰتِ رِزْقًۭا لَّكُمْ ۖ فَلَا تَجْعَلُوا۟ لِلَّهِ أَندَادًۭا وَأَنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: luna: The section's cloud grows plants and rain leaves food on earth; this ayah links water sent from the sky with fruits provided for people. | terra: God makes the sky a canopy and sends water down from it to produce fruits as provision. The S-M-W word of the source is joined to rain and edible earth.
- (2:60) [luna: medium; terra: strong; basis: scene+theme] ۞ وَإِذِ ٱسْتَسْقَىٰ مُوسَىٰ لِقَوْمِهِۦ فَقُلْنَا ٱضْرِب بِّعَصَاكَ ٱلْحَجَرَ ۖ فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ ۖ كُلُوا۟ وَٱشْرَبُوا۟ مِن رِّزْقِ ٱللَّهِ وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ
  Unverified discovery rationale: luna: The section includes Moses at water, helping people water their flocks; this ayah has Moses strike a rock and twelve springs gush out for his people to drink. | terra: Moses asks for water for his people; twelve springs burst from the rock, and every group knows its drinking place. It makes water a shared order that keeps a community supplied.
- (2:164) [luna: medium; terra: strong; basis: scene+theme] إِنَّ فِى خَلْقِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَٱخْتِلَٰفِ ٱلَّيْلِ وَٱلنَّهَارِ وَٱلْفُلْكِ ٱلَّتِى تَجْرِى فِى ٱلْبَحْرِ بِمَا يَنفَعُ ٱلنَّاسَ وَمَآ أَنزَلَ ٱللَّهُ مِنَ ٱلسَّمَآءِ مِن مَّآءٍۢ فَأَحْيَا بِهِ ٱلْأَرْضَ بَعْدَ مَوْتِهَا وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ وَتَصْرِيفِ ٱلرِّيَٰحِ وَٱلسَّحَابِ ٱلْمُسَخَّرِ بَيْنَ ٱلسَّمَآءِ وَٱلْأَرْضِ لَءَايَٰتٍۢ لِّقَوْمٍۢ يَعْقِلُونَ
  Unverified discovery rationale: luna: The section's layered cloud and rain image is echoed by this ayah's clouds held between heaven and earth, rain sent down, and earth revived with it. | terra: The signs include sky-water reviving dead earth, creatures dispersed through it, changing winds, and cloud held between sky and earth. It gathers the section's rain, wind, cloud, life, and ordered world in one ayah.
- (2:265) [luna: medium (missing-ayat turn); terra: strong; basis: scene+theme] وَمَثَلُ ٱلَّذِينَ يُنفِقُونَ أَمْوَٰلَهُمُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ وَتَثْبِيتًۭا مِّنْ أَنفُسِهِمْ كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ فَإِن لَّمْ يُصِبْهَا وَابِلٌۭ فَطَلٌّۭ ۗ وَٱللَّهُ بِمَا تَعْمَلُونَ بَصِيرٌ
  Unverified discovery rationale: luna: The section links rain to growth on earth; this ayah compares good giving to a garden on high ground that yields twice when heavy rain falls, with even light rain sufficient. | terra: A garden on high ground yields double produce when struck by a heavy rain; even dew suffices. It closely parallels the source's soft plant that continues through summer and the productive effect of moisture.
- (6:99) [luna: medium; terra: strong; basis: root+scene+theme] وَهُوَ ٱلَّذِىٓ أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَأَخْرَجْنَا بِهِۦ نَبَاتَ كُلِّ شَىْءٍۢ فَأَخْرَجْنَا مِنْهُ خَضِرًۭا نُّخْرِجُ مِنْهُ حَبًّۭا مُّتَرَاكِبًۭا وَمِنَ ٱلنَّخْلِ مِن طَلْعِهَا قِنْوَانٌۭ دَانِيَةٌۭ وَجَنَّٰتٍۢ مِّنْ أَعْنَابٍۢ وَٱلزَّيْتُونَ وَٱلرُّمَّانَ مُشْتَبِهًۭا وَغَيْرَ مُتَشَٰبِهٍ ۗ ٱنظُرُوٓا۟ إِلَىٰ ثَمَرِهِۦٓ إِذَآ أَثْمَرَ وَيَنْعِهِۦٓ ۚ إِنَّ فِى ذَٰلِكُمْ لَءَايَٰتٍۢ لِّقَوْمٍۢ يُؤْمِنُونَ
  Unverified discovery rationale: luna: The section says rain-grown green is the mark left on soil; this ayah shows water from the sky bringing out varied crops, grain, dates, grapes, olives, and pomegranates. | terra: Water comes down from al-samāʾ and brings out vegetation, green growth, grain, palms, vines, olives, and pomegranates. It realizes the source's S-M-W dictionary meeting of sky, rain, and plant.
- (7:57) [luna: strong; terra: strong; basis: scene+theme] [cited in ¶49] وَهُوَ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ بُشْرًۢا بَيْنَ يَدَىْ رَحْمَتِهِۦ ۖ حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًۭا ثِقَالًۭا سُقْنَٰهُ لِبَلَدٍۢ مَّيِّتٍۢ فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ
  Unverified discovery rationale: luna: The section joins a wet south wind, cloud, rain, and mercy; this ayah sends winds as glad tidings before mercy, then has them carry heavy clouds, and closes by comparing rain-revived land with resurrection. | terra: The verse stages the section's whole weather sequence: winds announce mercy, bear heavy cloud, carry it to dead land, and rain brings fruit and the dead forth. It makes the growing Lord visible through rain's work on earth.
- (7:58) [luna: strong; terra: contrast; basis: contrast+neighbour+root+scene+theme] وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ ۖ وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًۭا ۚ كَذَٰلِكَ نُصَرِّفُ ٱلْءَايَٰتِ لِقَوْمٍۢ يَشْكُرُونَ
  Unverified discovery rationale: luna: The section's ر ب ب gloss says a cloud grows plants; here good land brings forth its vegetation by its Lord's permission, while the preceding ayah (7:57) supplies the wind and heavy cloud that precede this scene. | terra: Good land brings out vegetation by its Lord's permission, while bad land yields only scant growth. It gives the fertile earth of the source its explicit contrary soil.
