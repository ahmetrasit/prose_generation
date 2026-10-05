Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 87; below is its section 14 of 18 ("Yol ve binek: önde giden, kolaylaşan, yana çekilen"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md section 14 (prose paragraphs numbered) =====
[¶54] Üçüncü, sekizinci ve on birinci ayetler bir yolculuğun izini sürer. هدى önden gidip yolu göstermektir: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytuhu't-tarîka ve'l-beyte hidâyeten ey arraftuh, gloss:ona yolu ve evi gösterdim yani tanıttım, source:"ه د ي,B001"}. {ar:التقدم للإرشاد, tr:et-tekaddumu li'l-irşâd, gloss:yol göstermek için öne geçmek, source:"ه د ي,B001"}. {ar:الدليل يسمى هاديا لتقدمه, tr:ed-delîlu yusemmâ hâdiyen li-tekaddumih, gloss:kılavuza önden gittiği için hâdî denir, source:"ه د ي,B003"}. Aynı kök zayıf birinin iki kişiye dayanarak yürümesini de anlatır: {ar:يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله, tr:yuhâdî beyne'sneyni iẕâ kâne yemşî beynehumâ mu'temiden aleyhimâ min da'fihî ve temâyulih, gloss:zayıflığından ve sendelemesinden iki kişinin arasında onlara dayanarak yürüdü, source:"ه د ي,B008"}. Telaşsız ve sakin bir yürüyüşü de anlatır: {ar:لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن, tr:lem yusri' isrâa'l-munhezimi ve lâkin alâ sukûnin ve hedyin hasen, gloss:kaçan biri gibi koşmadı; sakin ve güzel bir gidişle yürüdü, source:"ه د ي,B010"}. Sekizinci ayet {ar:وَنُيَسِّرُكَ لِلْيُسْرَىٰ, tr:ve nuyessiruke li'l-yusrâ, gloss:seni en kolaya kolaylaştıracağız, source:87:8} der. يسر hazır ve kolay olandır: {ar:الميسور: ضد المعسور، وتيسر واستيسر بمعنى تهيأ, tr:el-meysûr diddu'l-ma'sûr ve teyessera ve'steysera bi-ma'nâ teheyyee, gloss:meysûr zor olanın zıddıdır; teyessera hazır oldu demektir, source:"ي س ر,B001"}. Kök kolay güdülen bineği de anlatır: {ar:يسر أي لين الانقياد سريع المتابعة يوصف به الإنسان والفرس, tr:yesrun ey leyyinu'l-inkıyâdi serîu'l-mutâbaa yûsafu bihi'l-insânu ve'l-feres, gloss:yesr kolay güdülen ve çabuk ardından gelen demektir; insan ve at için söylenir, source:"ي س ر,B005"}. Hafif bacakları da anlatır: {ar:اليسرات: القوائم الخفاف, tr:el-yeserât el-kavâimu'l-hıfâf, gloss:yeserât hafif bacaklardır, source:"ي س ر,B005"}. Sekizinci ayetin fiili düz anlamında Peygamber'e verilen bir vaattir. Aile resmi bu vaade bir binek görüntüsü katar: üzerindekinin isteğine kolayca uyan ve yolu hafif adımlarla alan bir hayvan.

[¶55] On birinci ayetteki الأشقى'nın kökü zahmettir: {ar:أصل يدل على المعاناة وخلاف السهولة, tr:aslun yedullu ale'l-muânâti ve hilâfi's-suhûle, gloss:katlanmayı ve kolaylığın zıddını gösteren köktür, source:"ش ق و,B002"}. Ama aynı kök bir dağ sırtını da adlandırır, ve bu tanımda üç kök birden geçer: {ar:الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان, tr:eş-şâkî min huyûdi'l-cibâli't-tâliu't-tavîl ve mea tûlihî eyseru suûden ve akdaru mak'aden li'l-insân, gloss:şâkî dağ çıkıntılarından uzun yükselen sırttır; uzunluğuna rağmen tırmanması daha kolay ve insan için oturmaya daha elverişlidir, source:"ش ق و,B004"}. "Zahmet" kelimesinin kökü burada "daha kolay" ve "ölçüye daha uygun" kelimeleriyle aynı cümlededir. Bu yüzden yol aynı olabilir. Fark, yolcunun onu nasıl yürüdüğündedir. On birinci ayetin fiili ise yolculuğun bir başka hareketidir. جنب bir hayvanı yanında yedeğe almaktır: {ar:جنبت الدابة إذا قدتها إلى جنبك وكذلك جنبت الأسير, tr:cenebtu'd-dâbbete iẕâ kudtuhâ ilâ cenbike ve keẕâlike cenebtu'l-esîr, gloss:hayvanı yanında yedeğe aldım; esiri de öyle, source:"ج ن ب,B005"}. Ayetteki biçim ise bir şeyi yanında uzak tutmaktır: {ar:جانبه وتجانبه وتجنبه واجتنبه كله بمعنى وجنبته الشيء أي نحيته عنه, tr:cânebehû ve tecânebehû ve teceннebehû ve'ctenebehû kulluhû bi-ma'nâ ve cenebtuhu'ş-şey'e ey nahheytuhû anh, gloss:cânebe tecânebe tecennebe ictenebe hep aynı anlamdadır; onu bir şeyden uzak tuttum yani o şeyi ondan ayırdım, source:"ج ن ب,B003"}. En bedbaht kişi öğüdü reddetmez, onun yanından geçer ve onu kendi yolunun kenarında tutar.

[¶56] İkinci ayetin سوّى fiilinin ailesinde binicinin oturuşu vardır: {ar:استوى على ظهر دابته أي علا واستقر, tr:istevâ alâ zahri dâbbetihî ey alâ ve'stekarr, gloss:hayvanının sırtına oturdu yani üstüne çıkıp yerleşti, source:"س و ي,B003"}. Bu tanım birinci ayetteki yükseklik kökünü de içerir. Semere serilen örtü de bu ailedendir: {ar:السَّويّة كساء يلف ويجعل شبيها بالحوية يلقى على سنام البعير, tr:es-seviyye kisâun yuleffu ve yuc'alu şebîhen bi'l-haviyyeti yulkâ alâ senâmi'l-baîr, gloss:seviyye sarılıp haviyyeye benzetilerek devenin hörgücüne konan örtüdür, source:"س و ي,B010"}. Benzetildiği haviyye de beşinci ayetteki أحوى'nın kökündendir: {ar:الحوية كساء يحوي حول سنام البعير ثم يركب, tr:el-haviyye kisâun yahvî havle senâmi'l-baîri ŝumme yurkeb, gloss:haviyye devenin hörgücünü saran ve üstüne binilen örtüdür, source:"ح و ي,B004"}. Aynı kök yolun ortasını da adlandırır: {ar:مكان سوى أي عدل ووسط, tr:mekânun suven ey adlun ve vasat, gloss:dengeli ve orta bir yer, source:"س و ي,B006"}. Ama "cehennemin ortası" da bu kelimeyle söylenir: {ar:في سواء الجحيم, tr:fî sevâi'l-cahîm, gloss:cehennemin ortasında, source:"س و ي,B006"}.

[¶57] Kur'an bu yolu sahneler. Yeminlerle açılan bir surede verenler ile cimrilik edenler ayrılır: {ar:فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ, tr:fe-senuyessiruhû li'l-yusrâ, gloss:onu en kolaya kolaylaştıracağız, source:92:7}, {ar:فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ, tr:fe-senuyessiruhû li'l-usrâ, gloss:onu en zora kolaylaştıracağız, source:92:10}. Aynı fiil iki yöne çalışır. Birinin bineği kolaylığa, ötekininki zorluğa gider. Ardından {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hudâ, gloss:yol göstermek elbette bize düşer, source:92:12} denir. İnsan için {ar:ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ, tr:ŝumme's-sebîle yesserah, gloss:sonra yolu ona kolaylaştırdı, source:80:20} ve {ar:إِنَّا هَدَيْنَٰهُ ٱلسَّبِيلَ إِمَّا شَاكِرًۭا وَإِمَّا كَفُورًا, tr:innâ hedeynâhu's-sebîle immâ şâkiran ve immâ kefûrâ, gloss:biz ona yolu gösterdik; ister şükreden olsun ister nankör, source:76:3} denir. Bir başka yerde yol iki sırttır ve tırmanılmaz: {ar:وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ, tr:ve hedeynâhu'n-necdeyn, gloss:ona iki yüksek yolu gösterdik, source:90:10}, {ar:فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ, tr:fe-le'ktehame'l-akabe, gloss:ama o sarp yokuşa atılmadı, source:90:11}. Zahmet kelimesi Adem'in hikâyesinde geçer. Allah onu uyarır: {ar:فَلَا يُخْرِجَنَّكُمَا مِنَ ٱلْجَنَّةِ فَتَشْقَىٰٓ, tr:fe-lâ yuhricennekumâ mine'l-cenneti fe-teşkâ, gloss:sakın sizi cennetten çıkarmasın; yoksa zahmete düşersin, source:20:117}. Yere indirilirken de şöyle der: {ar:فَمَنِ ٱتَّبَعَ هُدَاىَ فَلَا يَضِلُّ وَلَا يَشْقَىٰ, tr:fe-meni't-tebea hudâye fe-lâ yadillu ve lâ yeşkâ, gloss:kim benim yol göstermemi izlerse ne yolunu şaşırır ne de bedbaht olur, source:20:123}. Peygamber'e de {ar:مَآ أَنزَلْنَا عَلَيْكَ ٱلْقُرْءَانَ لِتَشْقَىٰٓ, tr:mâ enzelnâ aleyke'l-kur'âne li-teşkâ, gloss:Kur'an'ı sana zahmet çekesin diye indirmedik, source:20:2} denir. Musa Firavun'a gönderilirken {ar:وَيَسِّرْ لِىٓ أَمْرِى, tr:ve yessir lî emrî, gloss:işimi bana kolaylaştır, source:20:26} diye dua eder. Kolaylık zorlukla birlikte gelir: {ar:فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا, tr:fe-inne mea'l-usri yusrâ, gloss:zorlukla birlikte bir kolaylık vardır, source:94:5}. Surenin son ayetinde adı geçen İbrahim, yana çekilmeyi kendisi için ister: {ar:وَٱجْنُبْنِى وَبَنِىَّ أَن نَّعْبُدَ ٱلْأَصْنَامَ, tr:vecnubnî ve beniyye en na'bude'l-esnâm, gloss:beni ve oğullarımı putlara tapmaktan uzak tut, source:14:35}. On birinci ayetin kökü burada tersine çalışır. Bedbaht öğüdü kendinden uzak tutar, İbrahim ise Rabbinden kendisini puttan uzak tutmasını ister. Yolun yanlış ucu da gösterilir. Cennetteki bir kişi dünyadaki arkadaşını hatırlar, aşağıya bakar ve {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettalea fe-raâhu fî sevâi'l-cahîm, gloss:baktı ve onu cehennemin ortasında gördü, source:37:55}.

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/ledger.md =====
- memory: حُوَّة as the colour noun behind أحوى
- memory: سبح's base sense of swimming in water
- memory: سيما (48:29) filed under a different root from وسم

===== passages from the discovery list (313) =====
## strong (192)

- (1:6) [luna: strong; terra: strong; basis: root+scene+speaker] ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
  Unverified discovery rationale: luna: The section's root ه د ي describes showing the way; the opening prayer asks God to guide its speaker onto the straight path, making guidance a request from the traveler. | terra: “Guide us to the straight path” is the direct prayer to be shown and led along the right road.
- (2:38) [terra: strong; basis: root+scene+theme] قُلْنَا ٱهْبِطُوا۟ مِنْهَا جَمِيعًۭا ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَن تَبِعَ هُدَاىَ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
  Unverified discovery rationale: terra: At the descent from the garden, following God’s guidance secures the travellers from fear and grief, paralleling the later Adamic promise in 20:123.
- (2:108) [luna: strong; terra: strong (missing-ayat turn); basis: contrast+root+scene+theme] أَمْ تُرِيدُونَ أَن تَسْـَٔلُوا۟ رَسُولَكُمْ كَمَا سُئِلَ مُوسَىٰ مِن قَبْلُ ۗ وَمَن يَتَبَدَّلِ ٱلْكُفْرَ بِٱلْإِيمَٰنِ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
  Unverified discovery rationale: luna: The section's dictionary form سَوَاءٌ names an even middle; this ayah says one who exchanges faith for disbelief has lost the سَوَاءَ السَّبِيلِ, joining the middle-place sense to a lost road. | terra: Whoever exchanges faith for unbelief “has strayed from the middle of the road,” directly joining سوء choice to سَوَاءَ السَّبِيلِ.
- (2:185) [luna: strong; terra: strong; basis: contrast+root+theme] شَهْرُ رَمَضَانَ ٱلَّذِىٓ أُنزِلَ فِيهِ ٱلْقُرْءَانُ هُدًۭى لِّلنَّاسِ وَبَيِّنَٰتٍۢ مِّنَ ٱلْهُدَىٰ وَٱلْفُرْقَانِ ۚ فَمَن شَهِدَ مِنكُمُ ٱلشَّهْرَ فَلْيَصُمْهُ ۖ وَمَن كَانَ مَرِيضًا أَوْ عَلَىٰ سَفَرٍۢ فَعِدَّةٌۭ مِّنْ أَيَّامٍ أُخَرَ ۗ يُرِيدُ ٱللَّهُ بِكُمُ ٱلْيُسْرَ وَلَا يُرِيدُ بِكُمُ ٱلْعُسْرَ وَلِتُكْمِلُوا۟ ٱلْعِدَّةَ وَلِتُكَبِّرُوا۟ ٱللَّهَ عَلَىٰ مَا هَدَىٰكُمْ وَلَعَلَّكُمْ تَشْكُرُونَ
  Unverified discovery rationale: luna: The section names root ي س ر for ease and contrasts it with difficulty; this ayah says God wants ease for people and does not want hardship, in a concrete rule about fasting. | terra: يُرِيدُ اللَّهُ بِكُمُ الْيُسْرَ وَلَا يُرِيدُ بِكُمُ الْعُسْر states the divine preference for ease over hardship in the same paired vocabulary.
- (2:196) [terra: strong; basis: root+scene] وَأَتِمُّوا۟ ٱلْحَجَّ وَٱلْعُمْرَةَ لِلَّهِ ۚ فَإِنْ أُحْصِرْتُمْ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۖ وَلَا تَحْلِقُوا۟ رُءُوسَكُمْ حَتَّىٰ يَبْلُغَ ٱلْهَدْىُ مَحِلَّهُۥ ۚ فَمَن كَانَ مِنكُم مَّرِيضًا أَوْ بِهِۦٓ أَذًۭى مِّن رَّأْسِهِۦ فَفِدْيَةٌۭ مِّن صِيَامٍ أَوْ صَدَقَةٍ أَوْ نُسُكٍۢ ۚ فَإِذَآ أَمِنتُمْ فَمَن تَمَتَّعَ بِٱلْعُمْرَةِ إِلَى ٱلْحَجِّ فَمَا ٱسْتَيْسَرَ مِنَ ٱلْهَدْىِ ۚ فَمَن لَّمْ يَجِدْ فَصِيَامُ ثَلَٰثَةِ أَيَّامٍۢ فِى ٱلْحَجِّ وَسَبْعَةٍ إِذَا رَجَعْتُمْ ۗ تِلْكَ عَشَرَةٌۭ كَامِلَةٌۭ ۗ ذَٰلِكَ لِمَن لَّمْ يَكُنْ أَهْلُهُۥ حَاضِرِى ٱلْمَسْجِدِ ٱلْحَرَامِ ۚ وَٱتَّقُوا۟ ٱللَّهَ وَٱعْلَمُوٓا۟ أَنَّ ٱللَّهَ شَدِيدُ ٱلْعِقَابِ
  Unverified discovery rationale: terra: فَمَا اسْتَيْسَرَ مِنَ الْهَدْيِ combines what is readily available from يسر with الهدي as sacrificial livestock, making the two root families meet in an actual led animal.
- (2:280) [terra: strong (missing-ayat turn); basis: contrast+root+theme] وَإِن كَانَ ذُو عُسْرَةٍۢ فَنَظِرَةٌ إِلَىٰ مَيْسَرَةٍۢ ۚ وَأَن تَصَدَّقُوا۟ خَيْرٌۭ لَّكُمْ ۖ إِن كُنتُمْ تَعْلَمُونَ
  Unverified discovery rationale: terra: A debtor in hardship is granted delay until مَيْسَرَةٍ, presenting ease as a reachable condition that answers present constriction.
- (4:28) [luna: weak (missing-ayat turn); terra: strong; basis: theme] يُرِيدُ ٱللَّهُ أَن يُخَفِّفَ عَنكُمْ ۚ وَخُلِقَ ٱلْإِنسَٰنُ ضَعِيفًۭا
  Unverified discovery rationale: luna: The section's root ه د ي also has a dictionary sense of a weak, swaying walker supported by two people; this ayah says human beings are weak and God wants to lighten their burden, a thematic echo rather than a walking scene. | terra: God wants to lighten the human being because humanity was created weak; lightness answers precisely to the section’s weak supported walker and light legs.
- (4:98) [terra: strong (missing-ayat turn); basis: root+scene+theme] إِلَّا ٱلْمُسْتَضْعَفِينَ مِنَ ٱلرِّجَالِ وَٱلنِّسَآءِ وَٱلْوِلْدَٰنِ لَا يَسْتَطِيعُونَ حِيلَةًۭ وَلَا يَهْتَدُونَ سَبِيلًۭا
  Unverified discovery rationale: terra: The truly helpless are those without a means and unable to find a way, joining human weakness to the practical inability to be guided onto a route.
- (5:12) [terra: strong (missing-ayat turn); basis: root+scene+theme] ۞ وَلَقَدْ أَخَذَ ٱللَّهُ مِيثَٰقَ بَنِىٓ إِسْرَٰٓءِيلَ وَبَعَثْنَا مِنْهُمُ ٱثْنَىْ عَشَرَ نَقِيبًۭا ۖ وَقَالَ ٱللَّهُ إِنِّى مَعَكُمْ ۖ لَئِنْ أَقَمْتُمُ ٱلصَّلَوٰةَ وَءَاتَيْتُمُ ٱلزَّكَوٰةَ وَءَامَنتُم بِرُسُلِى وَعَزَّرْتُمُوهُمْ وَأَقْرَضْتُمُ ٱللَّهَ قَرْضًا حَسَنًۭا لَّأُكَفِّرَنَّ عَنكُمْ سَيِّـَٔاتِكُمْ وَلَأُدْخِلَنَّكُمْ جَنَّٰتٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ ۚ فَمَن كَفَرَ بَعْدَ ذَٰلِكَ مِنكُمْ فَقَدْ ضَلَّ سَوَآءَ ٱلسَّبِيلِ
  Unverified discovery rationale: terra: After covenant obligations and a promise of support, disbelief is said to stray from سَوَاءَ السَّبِيلِ, the road’s balanced middle.
- (5:16) [terra: strong (missing-ayat turn); basis: root+theme] يَهْدِى بِهِ ٱللَّهُ مَنِ ٱتَّبَعَ رِضْوَٰنَهُۥ سُبُلَ ٱلسَّلَٰمِ وَيُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ بِإِذْنِهِۦ وَيَهْدِيهِمْ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
  Unverified discovery rationale: terra: Through revelation God guides seekers of His pleasure along paths of peace and onto a straight path, making the scripture an active route guide.
- (5:77) [terra: strong (missing-ayat turn); basis: root+scene+theme] قُلْ يَٰٓأَهْلَ ٱلْكِتَٰبِ لَا تَغْلُوا۟ فِى دِينِكُمْ غَيْرَ ٱلْحَقِّ وَلَا تَتَّبِعُوٓا۟ أَهْوَآءَ قَوْمٍۢ قَدْ ضَلُّوا۟ مِن قَبْلُ وَأَضَلُّوا۟ كَثِيرًۭا وَضَلُّوا۟ عَن سَوَآءِ ٱلسَّبِيلِ
  Unverified discovery rationale: terra: People who follow earlier desires are said to have gone astray from سَوَاءِ السَّبِيلِ, making the middle road something inherited error can leave.
- (6:97) [terra: strong; basis: root+scene] وَهُوَ ٱلَّذِى جَعَلَ لَكُمُ ٱلنُّجُومَ لِتَهْتَدُوا۟ بِهَا فِى ظُلُمَٰتِ ٱلْبَرِّ وَٱلْبَحْرِ ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَعْلَمُونَ
  Unverified discovery rationale: terra: The stars are made so people may find guidance through darkness on land and sea, identifying created signs that go before the traveller.
- (6:125) [luna: medium (missing-ayat turn); terra: strong; basis: contrast+root+scene+theme] فَمَن يُرِدِ ٱللَّهُ أَن يَهْدِيَهُۥ يَشْرَحْ صَدْرَهُۥ لِلْإِسْلَٰمِ ۖ وَمَن يُرِدْ أَن يُضِلَّهُۥ يَجْعَلْ صَدْرَهُۥ ضَيِّقًا حَرَجًۭا كَأَنَّمَا يَصَّعَّدُ فِى ٱلسَّمَآءِ ۚ كَذَٰلِكَ يَجْعَلُ ٱللَّهُ ٱلرِّجْسَ عَلَى ٱلَّذِينَ لَا يُؤْمِنُونَ
  Unverified discovery rationale: luna: The section names root ه د ي for guidance and pairs ease with difficulty; this ayah describes guidance as an opened heart and misguidance as constriction like climbing into the sky, joining direction to felt ease or strain. | terra: Guidance opens the chest, while misguidance makes it tight “as though climbing into the sky”; moral direction is felt as easy passage versus punishing ascent.
- (6:126) [luna: strong (missing-ayat turn); basis: neighbour+scene+theme] وَهَٰذَا صِرَٰطُ رَبِّكَ مُسْتَقِيمًۭا ۗ قَدْ فَصَّلْنَا ٱلْءَايَٰتِ لِقَوْمٍۢ يَذَّكَّرُونَ
  Unverified discovery rationale: luna: The section develops a route and the remembrance that distinguishes its traveler; this ayah names the Lord's straight path and says its signs are made clear for people who remember, continuing 6:125's guidance contrast.
- (6:142) [terra: strong (missing-ayat turn); basis: scene+theme] وَمِنَ ٱلْأَنْعَٰمِ حَمُولَةًۭ وَفَرْشًۭا ۚ كُلُوا۟ مِمَّا رَزَقَكُمُ ٱللَّهُ وَلَا تَتَّبِعُوا۟ خُطُوَٰتِ ٱلشَّيْطَٰنِ ۚ إِنَّهُۥ لَكُمْ عَدُوٌّۭ مُّبِينٌۭ
  Unverified discovery rationale: terra: The same ayah names livestock made for carrying loads and forbids following Satan’s footsteps, bringing the pack animal and the choice of whom to follow together.
- (6:153) [luna: strong; terra: strong; basis: contrast+scene+theme] وَأَنَّ هَٰذَا صِرَٰطِى مُسْتَقِيمًۭا فَٱتَّبِعُوهُ ۖ وَلَا تَتَّبِعُوا۟ ٱلسُّبُلَ فَتَفَرَّقَ بِكُمْ عَن سَبِيلِهِۦ ۚ ذَٰلِكُمْ وَصَّىٰكُم بِهِۦ لَعَلَّكُمْ تَتَّقُونَ
  Unverified discovery rationale: luna: The section says the road may be one while the traveler's response differs; this ayah commands following one straight path and warns against side paths that divide people from it. | terra: God’s straight path is to be followed, while following the other roads disperses travellers away from it; the journey forks by obedience.
