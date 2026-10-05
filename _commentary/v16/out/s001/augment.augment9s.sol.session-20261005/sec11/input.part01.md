Follow the brief below (augment.md) exactly. The commentary is a surah commentary on the images of surah 1; below is its section 11 of 14 ("Dayanmak ve doğrulmak: destek isteyen yolcu"), with its paragraphs numbered as in the whole commentary; the commentary's ledger and the listed passages follow it. Return only the output augment.md specifies.

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

===== _commentary/v16/out/s001/images.r13.map3.nohft.tool.tool/images.md section 11 (prose paragraphs numbered) =====
[¶55] Bir yolcunun bineği yorulur ya da sakatlanır ve yolcu yolda kalır: {ar:أعبد بفلان بمعنى أبدع به إذا كلت راحلته أو عطبت, tr:u'bide bi-fülân, gloss:falanca yolda kaldı, yani bineği yoruldu ya da sakatlandı, source:"ع ب د,B011"}. Bu kelime beşinci ayetteki "na'büdü" ile aynı ailedendir. Altıncı ayetteki "müstakîm" kelimesinin ailesinde de aynı an vardır. Burada "kâme" fiili ayağa kalkmayı değil, olduğu yerde durup kalmayı anlatır: {ar:قامت لفلان دابته إذا كلت أو عيت فلم تسر, tr:kâmet li-fülânin dâbbetüh, gloss:falancanın bineği durdu kaldı, yani yorulup bitti ve yürümez oldu, source:"ق و م,B016"}. Yolcunun kendisi de güçsüzdür: {ar:الهداء الرجل البليد الضعيف, tr:el-hidâü'r-racülü'l-belîdü'd-da'îf, gloss:hidâ, ağır ve güçsüz adamdır, source:"ه د ي,B009"}. Bu adam iki kişinin arasında, onlara yaslanarak yürür: {ar:يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله, tr:yühâdâ beyne'sneyn, gloss:güçsüzlüğünden ve sendelemesinden dolayı iki kişinin arasında onlara dayanarak yürür, source:"ه د ي,B008"}. Bu yürüyüş şöyle tarif edilir: {ar:التهادي مشي في تمايل يمينا وشمالا, tr:et-tehâdî meşyün fî temâyülin yemînen ve şimâlâ, gloss:tehâdî, sağa sola sallanarak yürümektir, source:"ه د ي,B008"}. "İhdinâ" kelimesinin ailesi, yalnız önden giden kılavuzu değil, iki yandan tutulan güçsüz yolcuyu da içerir.

[¶56] Beşinci ayetteki {ar:نَسْتَعِينُ, tr:nesteînü, gloss:yardım dileriz, source:1:5} kelimesi bu durumda istenen şeydir. Yardım, insanın dayandığı her şeydir: {ar:كل شيء استعنت به أو أعانك فهو عونك, tr:küllü şey'in este'ante bihî ev eânek fe-hüve avnük, gloss:yardım istediğin ya da sana yardım eden her şey senin avnindir, source:"ع و ن,B001"}. Fiilin kalıbı istemeyi bildirir: {ar:الاستعانة طلب العون, tr:el-isti'ânetü talebü'l-avn, gloss:istiâne, yardım istemektir, source:"ع و ن,B001"}. Yardımın sonucu ise doğrulmaktır: {ar:قام قياما والقومة المرة الواحدة إذا انتصب, tr:kâme kıyâmen, gloss:kalktı, yani dikildi, source:"ق و م,B002"}. Ağaç da köklerinin üzerinde böyle dimdik durur: {ar:تركتموها قائمة على أصولها, tr:teraktümûhâ kâimeten alâ usûlihâ, gloss:onu kökleri üzerinde dikili bıraktınız, source:"ق و م,B002"}. Dayanağın kendisi de aynı köktendir: {ar:القيام العماد, tr:el-kıyâmü'l-imâd, gloss:kıyâm, direktir, source:"ق و م,B009"}. Doğrulan yolcu artık sakin adımlarla yürür: {ar:لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن, tr:lem yüsri' isrâ'a'l-münhezim, velâkin alâ sükûnin ve hedyin hasen, gloss:bozguna uğramış birinin telaşıyla koşmadı, sakin ve güzel bir yürüyüşle gitti, source:"ه د ي,B010"}. Burada "hedy" kelimesi "ihdinâ" ile aynı köktendir ve yürüyüşün kendisine ad verir. Dördüncü ayetteki "mâlik" kelimesinin ailesi bu dik duruşu bir duvar ve bir beden üzerinden anlatır. Duvarın bütünlüğü bu köktendir: {ar:حائط ليس له ملاك أي تماسك, tr:hâitun leyse lehû milâk, gloss:bir arada duracak tutunması olmayan duvar, source:"م ل ك,B001"}. Kökün temel anlamı da budur: {ar:أصل صحيح يدل على قوة في الشيء وصحة, tr:aslun sahîhun yedüllü alâ kuvvetin fi'ş-şey'i ve sıhha, gloss:bir şeydeki güce ve sağlamlığa işaret eden bir köktür, source:"م ل ك,B001"}. Kalp de bedeni bir arada tutan şeydir: {ar:القلب ملاك الجسد, tr:el-kalbü milâkü'l-cesed, gloss:kalp bedenin dayanağıdır, source:"م ل ك,B005"}. "Na'büdü" kelimesinin ailesinde, yolda kalan yolcunun tersi olan sağlamlık da vardır: {ar:العبدة وهي القوة والصلابة, tr:el-abede, ve hiye'l-kuvvetü ve's-salâbe, gloss:abede, güç ve sağlamlıktır, source:"ع ب د,B007"}.

[¶57] Bu görüntü, surenin beşinci ve altıncı ayetleri arasındaki geçişi görünür kılar. Kulluk ve yardım istemek aynı cümlede yan yana gelir. Ardından yol isteği gelir. Yolu isteyen kişi tek başına yürüyebilecek güçte değildir. Bineği durmuştur, kendisi sendelemektedir ve iki yanından tutulmayı ister. Düz bir meal "yardım dileriz" der. Görüntü ise bu yardımın bir bedene verildiğini gösterir: Dayanılan bir omuz, dikilen bir gövde ve telaşsız bir yürüyüş. "Müstakîm" kelimesi burada yolun düzlüğünün yanında yürüyenin dik duruşunu da duyurur.

[¶58] Kur'an bu sahneyi birçok yerde kurar. Musa ile Allah'ın katından rahmet ve ilim verilmiş bir kul {source:18:65}, kendilerini ağırlamayan bir kasabada yıkılmak üzere olan bir duvar bulur: {ar:فَوَجَدَا فِيهَا جِدَارًۭا يُرِيدُ أَن يَنقَضَّ فَأَقَامَهُۥ, tr:fe-vecedâ fîhâ cidâran yürîdü en yenkadda fe-ekâmeh, gloss:orada yıkılmak üzere olan bir duvar buldular, o da duvarı doğrulttu, source:18:77}. "Ekâmehû" fiili, "milâk"ı kalmamış bir duvarı ayağa diker. Zülkarneyn'den bir set yapması istenir {source:18:94}. O da bir ücret almaz ve yardım ister: {ar:فَأَعِينُونِى بِقُوَّةٍ أَجْعَلْ بَيْنَكُمْ وَبَيْنَهُمْ رَدْمًا, tr:fe-eînûnî bi-kuvvetin ec'al beyneküm ve beynehüm radmâ, gloss:bana güçle yardım edin ki aranıza sağlam bir set yapayım, source:18:95}. Yardım burada bir güç olarak verilir ve ortaya çıkan şey ayakta duran bir settir. Yakup, kanlı gömleği gördüğünde yardımı yalnızca Allah'tan bekler: {ar:فَصَبْرٌۭ جَمِيلٌۭ ۖ وَٱللَّهُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ, tr:fe-sabrun cemîl, vallâhü'l-müsteânü alâ mâ tesıfûn, gloss:artık bana güzel bir sabır düşer; anlattıklarınıza karşı yardımı istenecek olan Allah'tır, source:12:18}. Peygamberin sözü de aynı kelimeyi taşır: {ar:وَرَبُّنَا ٱلرَّحْمَٰنُ ٱلْمُسْتَعَانُ, tr:ve rabbüne'r-rahmânü'l-müsteân, gloss:Rabbimiz, yardımı istenecek olan Rahman'dır, source:21:112}. Bu cümlede surenin Rab, Rahman ve istiâne kelimeleri bir aradadır. Musa halkına şöyle der: {ar:ٱسْتَعِينُوا۟ بِٱللَّهِ وَٱصْبِرُوٓا۟, tr:ista'înû billâhi vasbirû, gloss:Allah'tan yardım isteyin ve sabredin, source:7:128}. Dayanılacak şeyler de sayılır: {ar:وَٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ, tr:vesta'înû bi's-sabri ve's-salâ, gloss:sabırla ve namazla yardım isteyin, source:2:45}. Müminler birbirlerinin dayanağı olur: {ar:وَتَعَاوَنُوا۟ عَلَى ٱلْبِرِّ وَٱلتَّقْوَىٰ, tr:ve teâvenû ale'l-birri ve't-takvâ, gloss:iyilik ve takva üzerinde yardımlaşın, source:5:2}. Bu sahnenin iki yürüyüşü bir soruda karşılaştırılır: {ar:أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ, tr:e-fe men yemşî mükibben alâ vechihî ehdâ em men yemşî seviyyen alâ sırâtın müstakîm, gloss:yüzüstü kapanarak yürüyen mi yolu daha iyi bulur, yoksa dosdoğru bir yolda dimdik yürüyen mi, source:67:22}. Rahman'ın kullarının yürüyüşü de anlatılır: {ar:وَعِبَادُ ٱلرَّحْمَٰنِ ٱلَّذِينَ يَمْشُونَ عَلَى ٱلْأَرْضِ هَوْنًۭا, tr:ve ibâdü'r-rahmâni'llezîne yemşûne ale'l-ardı hevnâ, gloss:Rahman'ın kulları yeryüzünde vakarla ve yumuşak adımlarla yürürler, source:25:63}. Bu, bozguna uğramış birinin telaşı olmayan "hedy-i hasen"in, yani güzel yürüyüşün Kur'an'daki karşılığıdır.

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

===== passages from the discovery list (269) =====
## strong (118)

- (2:38) [terra: strong (missing-ayat turn); basis: contrast+root+theme] قُلْنَا ٱهْبِطُوا۟ مِنْهَا جَمِيعًۭا ۖ فَإِمَّا يَأْتِيَنَّكُم مِّنِّى هُدًۭى فَمَن تَبِعَ هُدَاىَ فَلَا خَوْفٌ عَلَيْهِمْ وَلَا هُمْ يَحْزَنُونَ
  Unverified discovery rationale: terra: When divine guidance comes, whoever follows it will neither go astray nor grieve; the dependent traveller’s safety is made conditional on following guidance.
- (2:45) [luna: strong; terra: strong; basis: root+speaker+theme] [cited in ¶58] وَٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ ۚ وَإِنَّهَا لَكَبِيرَةٌ إِلَّا عَلَى ٱلْخَٰشِعِينَ
  Unverified discovery rationale: luna: The section's *nasta'in* is a request for aid; this command says وَاسْتَعِينُوا بِالصَّبْرِ وَالصَّلَاةِ, naming patience and prayer as supports to seek. | terra: “Seek help through patience and prayer” gives the section’s نَسْتَعِينُ concrete supports for a weakened traveller.
- (2:127) [luna: strong (missing-ayat turn); basis: scene+speaker+theme] وَإِذْ يَرْفَعُ إِبْرَٰهِۦمُ ٱلْقَوَاعِدَ مِنَ ٱلْبَيْتِ وَإِسْمَٰعِيلُ رَبَّنَا تَقَبَّلْ مِنَّآ ۖ إِنَّكَ أَنتَ ٱلسَّمِيعُ ٱلْعَلِيمُ
  Unverified discovery rationale: luna: Ibrahim and Ismail raise the House's foundations, يَرْفَعُ إِبْرَاهِيمُ الْقَوَاعِدَ, then ask God to accept their work; two people build a lasting support and turn to God for aid.
- (2:153) [luna: strong (missing-ayat turn); terra: strong; basis: root+speaker+theme] يَٰٓأَيُّهَا ٱلَّذِينَ ءَامَنُوا۟ ٱسْتَعِينُوا۟ بِٱلصَّبْرِ وَٱلصَّلَوٰةِ ۚ إِنَّ ٱللَّهَ مَعَ ٱلصَّٰبِرِينَ
  Unverified discovery rationale: luna: The section's root ع و ن appears again in وَاسْتَعِينُوا بِالصَّبْرِ وَالصَّلَاةِ; this repeated command names patience and prayer as aid to seek and adds God's presence with the patient. | terra: Again commands believers to seek help through patience and prayer, adding that God is with the patient when endurance is needed.
- (2:214) [terra: strong (missing-ayat turn); basis: speaker+theme] أَمْ حَسِبْتُمْ أَن تَدْخُلُوا۟ ٱلْجَنَّةَ وَلَمَّا يَأْتِكُم مَّثَلُ ٱلَّذِينَ خَلَوْا۟ مِن قَبْلِكُم ۖ مَّسَّتْهُمُ ٱلْبَأْسَآءُ وَٱلضَّرَّآءُ وَزُلْزِلُوا۟ حَتَّىٰ يَقُولَ ٱلرَّسُولُ وَٱلَّذِينَ ءَامَنُوا۟ مَعَهُۥ مَتَىٰ نَصْرُ ٱللَّهِ ۗ أَلَآ إِنَّ نَصْرَ ٱللَّهِ قَرِيبٌۭ
  Unverified discovery rationale: terra: Believers are shaken by adversity until they ask when God’s help will come; the answer that it is near gives requested aid a crisis scene.
- (2:250) [terra: strong; basis: scene+theme] وَلَمَّا بَرَزُوا۟ لِجَالُوتَ وَجُنُودِهِۦ قَالُوا۟ رَبَّنَآ أَفْرِغْ عَلَيْنَا صَبْرًۭا وَثَبِّتْ أَقْدَامَنَا وَٱنصُرْنَا عَلَى ٱلْقَوْمِ ٱلْكَٰفِرِينَ
  Unverified discovery rationale: terra: Facing Goliath, the believers ask for patience to be poured on them, firm feet, and help: a prayer for standing rather than collapsing.
- (2:256) [luna: strong; terra: strong; basis: scene+theme] لَآ إِكْرَاهَ فِى ٱلدِّينِ ۖ قَد تَّبَيَّنَ ٱلرُّشْدُ مِنَ ٱلْغَىِّ ۚ فَمَن يَكْفُرْ بِٱلطَّٰغُوتِ وَيُؤْمِنۢ بِٱللَّهِ فَقَدِ ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ لَا ٱنفِصَامَ لَهَا ۗ وَٱللَّهُ سَمِيعٌ عَلِيمٌ
  Unverified discovery rationale: luna: The section describes help as what one leans on; here the believer holds to an unbreakable handhold, الْعُرْوَةِ الْوُثْقَىٰ, an explicit image of dependable support. | terra: The unbreakable “firm handhold” supplies a visible support under the weak person’s grip.
- (3:52) [terra: strong (missing-ayat turn); basis: scene+theme] ۞ فَلَمَّآ أَحَسَّ عِيسَىٰ مِنْهُمُ ٱلْكُفْرَ قَالَ مَنْ أَنصَارِىٓ إِلَى ٱللَّهِ ۖ قَالَ ٱلْحَوَارِيُّونَ نَحْنُ أَنصَارُ ٱللَّهِ ءَامَنَّا بِٱللَّهِ وَٱشْهَدْ بِأَنَّا مُسْلِمُونَ
  Unverified discovery rationale: terra: Jesus asks who will be his helpers toward God, and the disciples answer that they are God’s helpers; aid becomes companions who stand with a messenger.
- (3:101) [luna: strong; terra: strong (missing-ayat turn); basis: root+theme] وَكَيْفَ تَكْفُرُونَ وَأَنتُمْ تُتْلَىٰ عَلَيْكُمْ ءَايَٰتُ ٱللَّهِ وَفِيكُمْ رَسُولُهُۥ ۗ وَمَن يَعْتَصِم بِٱللَّهِ فَقَدْ هُدِىَ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ
  Unverified discovery rationale: luna: The section's roots ع و ن (aid) and ه د ي (guidance) meet here: whoever holds fast to God is guided to a straight path, فَقَدْ هُدِيَ إِلَىٰ صِرَاطٍ مُّسْتَقِيمٍ. | terra: Holding fast to God is followed by being guided to a straight path, joining a secure grip to directed movement.
- (3:103) [terra: strong; basis: scene+theme] وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا وَلَا تَفَرَّقُوا۟ ۚ وَٱذْكُرُوا۟ نِعْمَتَ ٱللَّهِ عَلَيْكُمْ إِذْ كُنتُمْ أَعْدَآءًۭ فَأَلَّفَ بَيْنَ قُلُوبِكُمْ فَأَصْبَحْتُم بِنِعْمَتِهِۦٓ إِخْوَٰنًۭا وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍۢ مِّنَ ٱلنَّارِ فَأَنقَذَكُم مِّنْهَا ۗ كَذَٰلِكَ يُبَيِّنُ ٱللَّهُ لَكُمْ ءَايَٰتِهِۦ لَعَلَّكُمْ تَهْتَدُونَ
  Unverified discovery rationale: terra: Holding all together to God’s rope turns the two-sided support of the source’s walker into communal dependence that prevents division.
- (3:122) [terra: strong; basis: scene+theme] إِذْ هَمَّت طَّآئِفَتَانِ مِنكُمْ أَن تَفْشَلَا وَٱللَّهُ وَلِيُّهُمَا ۗ وَعَلَى ٱللَّهِ فَلْيَتَوَكَّلِ ٱلْمُؤْمِنُونَ
  Unverified discovery rationale: terra: Two groups are about to lose courage, but God is their protector; it stages a faltering body or community upheld before it gives way.
- (3:147) [terra: strong; basis: root+theme] وَمَا كَانَ قَوْلَهُمْ إِلَّآ أَن قَالُوا۟ رَبَّنَا ٱغْفِرْ لَنَا ذُنُوبَنَا وَإِسْرَافَنَا فِىٓ أَمْرِنَا وَثَبِّتْ أَقْدَامَنَا وَٱنصُرْنَا عَلَى ٱلْقَوْمِ ٱلْكَٰفِرِينَ
  Unverified discovery rationale: terra: The prophets’ followers ask for forgiveness, firm feet, and divine help, directly joining inner repair to upright footing.
- (3:160) [terra: strong; basis: theme] إِن يَنصُرْكُمُ ٱللَّهُ فَلَا غَالِبَ لَكُمْ ۖ وَإِن يَخْذُلْكُمْ فَمَن ذَا ٱلَّذِى يَنصُرُكُم مِّنۢ بَعْدِهِۦ ۗ وَعَلَى ٱللَّهِ فَلْيَتَوَكَّلِ ٱلْمُؤْمِنُونَ
  Unverified discovery rationale: terra: “If God helps you” no one can overcome you, and if He leaves you no one can help: the verse fixes the true source of support.
- (3:173) [luna: medium; terra: strong (missing-ayat turn); basis: speaker+theme] ٱلَّذِينَ قَالَ لَهُمُ ٱلنَّاسُ إِنَّ ٱلنَّاسَ قَدْ جَمَعُوا۟ لَكُمْ فَٱخْشَوْهُمْ فَزَادَهُمْ إِيمَٰنًۭا وَقَالُوا۟ حَسْبُنَا ٱللَّهُ وَنِعْمَ ٱلْوَكِيلُ
  Unverified discovery rationale: luna: After believers are warned that enemies have gathered, they say حَسْبُنَا اللَّهُ; their reliance on God under threat parallels the section's aid sought when human strength is insufficient. | terra: Threatened believers answer that God is sufficient and the best disposer of affairs, an enacted refusal to seek a less reliable support.
- (4:5) [terra: strong; basis: root+theme] وَلَا تُؤْتُوا۟ ٱلسُّفَهَآءَ أَمْوَٰلَكُمُ ٱلَّتِى جَعَلَ ٱللَّهُ لَكُمْ قِيَٰمًۭا وَٱرْزُقُوهُمْ فِيهَا وَٱكْسُوهُمْ وَقُولُوا۟ لَهُمْ قَوْلًۭا مَّعْرُوفًۭا
  Unverified discovery rationale: terra: The source’s q-w-m family calls qiyām a support; this ayah calls wealth qiyāman for people, a material means by which life stands.
- (4:28) [terra: strong; basis: theme] يُرِيدُ ٱللَّهُ أَن يُخَفِّفَ عَنكُمْ ۚ وَخُلِقَ ٱلْإِنسَٰنُ ضَعِيفًۭا
  Unverified discovery rationale: terra: God wants to lighten the burden because the human being was created weak, naming the bodily need that makes help necessary.
- (4:36) [luna: strong; basis: scene+theme] ۞ وَٱعْبُدُوا۟ ٱللَّهَ وَلَا تُشْرِكُوا۟ بِهِۦ شَيْـًۭٔا ۖ وَبِٱلْوَٰلِدَيْنِ إِحْسَٰنًۭا وَبِذِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينِ وَٱلْجَارِ ذِى ٱلْقُرْبَىٰ وَٱلْجَارِ ٱلْجُنُبِ وَٱلصَّاحِبِ بِٱلْجَنۢبِ وَٱبْنِ ٱلسَّبِيلِ وَمَا مَلَكَتْ أَيْمَٰنُكُمْ ۗ إِنَّ ٱللَّهَ لَا يُحِبُّ مَن كَانَ مُخْتَالًۭا فَخُورًا
  Unverified discovery rationale: luna: Among commands to treat others well, this ayah names both وَالصَّاحِبِ بِالْجَنبِ and وَابْنِ السَّبِيلِ, joining a companion at one's side with the traveler who needs care.
- (4:75) [luna: strong (missing-ayat turn); terra: strong; basis: scene+speaker+theme] وَمَا لَكُمْ لَا تُقَٰتِلُونَ فِى سَبِيلِ ٱللَّهِ وَٱلْمُسْتَضْعَفِينَ مِنَ ٱلرِّجَالِ وَٱلنِّسَآءِ وَٱلْوِلْدَٰنِ ٱلَّذِينَ يَقُولُونَ رَبَّنَآ أَخْرِجْنَا مِنْ هَٰذِهِ ٱلْقَرْيَةِ ٱلظَّالِمِ أَهْلُهَا وَٱجْعَل لَّنَا مِن لَّدُنكَ وَلِيًّۭا وَٱجْعَل لَّنَا مِن لَّدُنكَ نَصِيرًا
  Unverified discovery rationale: luna: Oppressed men, women, and children cry to God to bring them out and appoint a protector and helper; their explicit plea for rescue and backing closely matches the section's support-seeking traveler. | terra: The oppressed weak men, women, and children ask God for a guardian and a helper, a direct social form of the assisted traveller.
- (4:98) [luna: strong (missing-ayat turn); terra: strong (missing-ayat turn); basis: root+scene+theme] إِلَّا ٱلْمُسْتَضْعَفِينَ مِنَ ٱلرِّجَالِ وَٱلنِّسَآءِ وَٱلْوِلْدَٰنِ لَا يَسْتَطِيعُونَ حِيلَةًۭ وَلَا يَهْتَدُونَ سَبِيلًۭا
