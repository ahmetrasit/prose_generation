Focus: 100:5. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/OZTURK/_projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. No other command or tool is available.

===== _commentary/v16/prompts/r13/write.md =====
Write the Turkish reading of the focus Quranic ayah for a curious reader who
knows neither Arabic nor how lexical families work, and who already has the
plain meaning. Show what a translation cannot give: the supported latent
meanings and resonances of its words, heard through their attested senses, the
ayah's neighbours, its surah and the Quran. Work from the supplied evidence and
your own knowledge of Arabic and the Quran. This is your own
interpretation, not a catalogue: maps and readings by earlier readers are
proposals, and what their members reveal together is yours to find or correct.
A surprise is welcome when the evidence supports it. There is no length limit.

Themes lead; words serve them. First understand the ayah in its grammar and
situation. Then explore its words' attested senses within and across roots,
the chains they take part in, and Quran passages that share its words or stage
the same act, scene or stance without sharing a word; a partial finding may
gain its missing support from another. Let the themes emerge from what these
reveal together, not from the familiar reading. Write the reading as those
themes: a word, a family image or a Quran passage enters where it grounds,
expands, complicates or joins a theme, developed as far as that work needs.
Never list a family's senses for their own sake, but judge each attested sense
by what it does, not by the branch it is filed under. Where this ayah's words
take part in a surah chain, that chain can found a theme here even when
another ayah completes it, and so can a scene where two such chains meet.
Every image this ayah's own words take part in is developed here as far as the
word carries it: what the object is, how it works, what usage names it. The
scene it forms with other ayat's words belongs to the surah commentary; recall
it in a sentence, tied to the ayah whose words carry it, never as something
explained before.

Keep these guards:

- A family image is heard beside the word's meaning in this ayah, never in
  place of it; say so once, where the first one enters. Show where each
  image comes from: the word, the usage that carries the image, quoted in
  Arabic, then its work in the theme. Report usage as what speakers called
  or said, varying the grammar so that no formula recurs ("… denir",
  "Araplar … derlerdi"); never name a dictionary, and never make "the family"
  a speaker.
- Keep root identity, family images and your interpretive connections
  distinct. Same word, same root and analogy are different things; an echo
  root does not establish identity.
- Explain a concrete object or mechanism by its work before drawing its
  meaning; do not flatten it into a label.
- Never invent a sense, source, vowel, etymology, historical fact, citation or
  chronology.
- Where a key word lives in Turkish as a narrowed or shifted loanword, let the
  reader feel what the Turkish word no longer carries, once.
- When you use another Quran passage, assume the reader does not know it:
  give its speaker, its situation as the Quran itself tells it there and in
  the neighbouring ayat, and the wording the connection needs. Use no hadith, no exegetes' views and no
  report from outside the Quran (no occasion of revelation, no name the Quran
  does not give, no date): the Quran, the supplied dictionary and Arabic usage
  carry the reading.
- The prose never talks about its own sources or process and never hedges in
  the first person ("hafızadan", "bildiğim kadarıyla", "sözlük", the map, its
  chains, workflow language; branch IDs only in tag sources).
  A claim about Arabic that neither the supplied texts nor the Quran text can
  check goes in the ledger as memory.

Write continuous prose in `##` sections, one theme each, warm and direct:
explain, do not dramatize; no lists and no closing recap.

Every Arabic quotation (Quran or dictionary phrase) goes in the reader
tag, as normal prose, never in quotation marks or backticks, and every tag
ends with its source, so the reader can check it:
{ar:exact Arabic, tr:readable Turkish transliteration, gloss:Turkish meaning, source:…}
- a dictionary phrase or a branch's sense: source:"<root letters>,<branch id>",
  e.g. source:"ق و م,B016";
- a Quran quotation: source:<surah:ayah>, e.g. source:72:16, the one ayah that
  holds the quoted words, no ranges;
- Arabic from your own memory that is not in the supplied dictionary:
  source:"memory".
A branch's sense given in Turkish without its Arabic, and a Quran passage named
without quoting it, carry the source alone: {source:"ق و م,B016"},
{source:15:41}. Never write a Quran reference outside a tag; quote the
surah's own words in tags too, and name its ayat in words ("dördüncü ayet"). The gloss gives
the ayah's word by its meaning here, a family image by that image. Copy Quran
Arabic from the supplied text or the lookup.

Output: the prose; then a line containing only
=== LEDGER ===
then, in plain English, one short line per item, a few words each:
- memory: <a claim about Arabic the texts cannot check>
- not written: <finding> - <why it could not found, reshape or join a theme>


===== _commentary/v16/prompts/r13/additions.md =====
No additions: write.md is the whole brief.


===== _commentary/v16/work/100_5/D.r13/context.md =====
# 100:5 — focus

فَوَسَطْنَ بِهِۦ جَمْعًا

Anchor translation (canonical reading, reference only):

Ardından onunla bir topluluğun ortasına girenlere:

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَوَسَطْنَ | وَسَطْ | و س ط | CONJ;V;PRON |
| 2 | بِهِۦ |  |  | P;PRON |
| 3 | جَمْعًا | جَمْع | ج م ع | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 100 — full text (context; no pericope)

- 100:1 وَٱلْعَٰدِيَٰتِ ضَبْحًۭا
- 100:2 فَٱلْمُورِيَٰتِ قَدْحًۭا
- 100:3 فَٱلْمُغِيرَٰتِ صُبْحًۭا
- 100:4 فَأَثَرْنَ بِهِۦ نَقْعًۭا
- 100:5 ◀ focus فَوَسَطْنَ بِهِۦ جَمْعًا
- 100:6 إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ
- 100:7 وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ
- 100:8 وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ
- 100:9 ۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ
- 100:10 وَحُصِّلَ مَا فِى ٱلصُّدُورِ
- 100:11 إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ


===== _commentary/v16/work/100_5/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## و س ط (root_001646) — identity root of فَوَسَطْنَ (w1)

- **B001** adil ve seçkin orta olma — adil, seçkin ve aşırılıktan uzak ölçülü olma · en adil veya topluluğun en seçkinlerinden · topluluğunda soyu seçkin ve konumu yüksek kişi
  بناء صحيح يدل على العدل والنصف، وأعدل الشيء أوسطه (maqayis)؛ فلان وسيط الحسب في قومه (ayn)؛ الوسط من كل شيء أعدله، أمة وسطا أي عدلا (sihah)؛ وسطا عدلا، خيارا، أوسط قومه أي من خيارهم (tahdhib)؛ يستعمل استعمال القصد المصون عن الإفراط والتفريط، فيمدح به نحو السواء والعدل والنصفة (mufradat)
- **B002** uçlar veya parçalar arasındaki orta yer — iki uç veya parçalar arasındaki orta yer · kolyenin ortasındaki değerli taş · orta parmak · sıralamadaki yerine göre orta sayılan ibadet · iki kent arasındaki konumundan adını alan şehir
  النصف، ضربت وسط رأسه، وسط القوم (maqayis)؛ الوسط مخففا يكون موضعا للشيء، اسما لما بين طرفي كل شيء، واسطة القلادة جوهرة تكون في وسط الكرس المنظوم (ayn)؛ الأصبع الوسطى، واسطة القلادة، واسط بلد سمي بالقصر بين الكوفة والبصرة (sihah)؛ ما كان يبين جزء من جزء فهو وسط، وسط الدار، واسطة القلادة (tahdhib)؛ وسط الشيء ما له طرفان، الصلاة الوسطى بين الركعتين وبين الأربع أو بين صلاة الليل والنهار (mufradat)
- **B003** ortaya girme veya ortaya yerleştirme — topluluğun ortasına girip aralarında yer almak · bir şeyi ortaya yerleştirmek
  وسط فلان جماعة من الناس وهو يسطهم إذا صار في وسطهم (ayn)؛ وسطت القوم أسطهم وسطا وسطة أي توسطتهم، التوسيط أن تجعل الشيء في الوسط (sihah)؛ أوسطت القوم ووسطتهم وتوسطتهم بمعنى واحد إذا دخلت وسطهم (tahdhib)
- **B004** iyi ile kötü arasında orta nitelikte — iyi ile kötü arasında, kimi bağlamda iyinin altında
  شيء وسط أي بين الجيد والردئ (sihah)؛ يقال فيما له طرف محمود وطرف مذموم، ويكنى به عن الرذل، فلان وسط من الرجال تنبيها أنه قد خرج من حد الخير (mufradat)
- **B005** insanlar arasında aracılık etme [kalıp] — insanlar arasında aracılık etmek
  التوسط بين الناس، من الوساطة (sihah)
- **B006** ortasından kesip ikiye ayırma — bir şeyi ortasından kesip iki yarıya ayırmak
  التوسيط قطع الشيء نصفين (sihah)
- **B007** özel adlandırma kümesi — benzer küçük bir çadırdan daha büyük kıl çadırı · sütüyle kabı dolduran deve
  الوسوط بيت من بيوت الشعر أكبر من المظلة، ويقال الوسوط من النوق كالصفوف تملأ الإناء (maqayis)

## ج م ع (root_000259) — identity root of جَمْعًا (w3)

- **B001** dağınık parçaları bir araya toplama — dağınık şeyi bir araya toplamak · mal biriktirmek ve saymak · ayrı yerlerdeki şeyleri bütünüyle bir araya getirmek · çeşitli yerlerden toplanmış şey · çeşitli yerlerden toplanıp götürülen yağma malı
  أصل واحد يدل على تضام الشيء (maqayis)؛ الجمع مصدر جمعت الشيء (ayn)؛ الجمع خلاف التفريق جمعت الشيء إذا ضممت بعضه إلى بعض (jamhara)؛ جمعت الشئ المتفرق فاجتمع (sihah)؛ الجمع أن تجمع شيئا إلى شيء (tahdhib)؛ الجمع ضم الشيء بتقريب بعضه من بعض (mufradat)
- **B002** bir araya gelmiş insan topluluğu — insan topluluğu veya çokluk · farklı boylardan karışık insan topluluğu · toplanmış topluluk veya ordu
  الجماع الأشابة من قبائل شتى (maqayis)؛ الجمع اسم لجماعة الناس والجموع اسم لجماعة الناس (ayn)؛ الجماع ما تجمع من أشابة الناس وأخلاطهم (jamhara)؛ جماع الناس أخلاطهم وهم الأشابة من قبائل شتى (sihah)؛ الجماع يقال في أقوام متفاوتة اجتمعوا (mufradat)
- **B003** düşünüp kesin bir tutuma bağlanma — bir işi yapmaya kesin biçimde karar vermek · hazırlık, kesin karar veya görüş birliği · işi veya düzeni sağlamlaştırıp kesinleştirmek
  أجمعت على الأمر إجماعا وأجمعته (maqayis)؛ أجمعت على الأمر إجماعا إذا عزمت عليه (jamhara)؛ أجمعت الأمر وعلى الأمر إذا عزمت عليه (sihah)؛ الإجماع الإعداد والعزيمة على الأمر (tahdhib)؛ أجمعت كذا فيما يكون جمعا يتوصل إليه بالفكرة (mufradat)
- **B004** toplanmayla belirlenen yer veya gün — insanların toplandığı yer · insanların bir araya geldiği kutsal yer veya günler için kullanılan ad · insanların ibadet veya yeniden diriliş için toplandığı gün · haftalık toplu ibadete katılıp namazı kılmak · halkı toplu ibadet için bir araya getiren ibadet yeri · ibadet için toplanma çağrısı · yolunu yitirme korkusuyla insanların ayrılmadığı ıssız alan
  جمع مكة سمي لاجتماع الناس به وكذلك يوم الجمعة (maqayis)؛ المجمع حيث يجمع الناس (ayn)؛ أيام جمع أيام منى والجمعة مشتقة من اجتماع الناس فيها للصلاة (jamhara)؛ يقال للمزدلفة جمع لاجتماع الناس فيها (sihah)؛ يوم الجمع ويوم يجمعكم ليوم الجمع (mufradat)
- **B005** sıkılmış avuç veya bir avuçluk miktar — sıkılmış avuç veya bu avuçla vurma · bir avuç dolusu
  ضربته بجمع كفي وجمع كفي (maqayis)؛ ضربته بجمع كفي وأعطيته من الدراهم جمع الكف (ayn)؛ ضربته بجمع يدي إذا ضممت كفك ثم ضربته بها (jamhara)؛ جمع الكف وهو حين تقبضها وجمعة من تمر أي قبضة منه (sihah)
- **B006** cinsel birleşme — cinsel birleşme için kullanılan örtülü söz · cinsel ilişkide bulunma
  الجماع كناية عن النكاح (jamhara)؛ المجامعة المباضعة (sihah)
- **B007** çocuğu karnındayken ölen veya el değmemiş kalan kadın — çocuğu karnındayken veya el değmemişken ölmek · kocasıyla cinsel birleşme yaşamamış kadın · ilk kez gebe kalan dişi eşek
  ماتت بجمع أي في بطنها ولد (maqayis)؛ ماتت المرأة بجمع أي مع ما في بطنها وكذلك إذا ماتت عذراء (ayn)؛ ماتت المرأة بجمع إذا ماتت وولدها في بطنها (jamhara)؛ أمر بني فلان بجمع أي لم يقتضها وماتت فلانة بجمع أي ماتت وولدها في بطنها (sihah)
- **B008** elleri boyna bağlayan kelepçe — elleri boyna bağlayan kelepçe veya demir bağ
  الجوامع الأغلال (maqayis)؛ الجوامع الأغلال الواحدة جامعة (jamhara)؛ الجامعة الغل لأنها تجمع اليدين إلى العنق (sihah)
- **B009** eksiksiz bütünlük — bedeni eksiksiz hayvan veya varlık · bedence derli toplu veya gelişimini tamamlamış adam · büyüyüp bütün dış giysileri giyecek çağa gelmek · bütünlük bildiren pekiştirme sözleri · dağılmamış bütün veya hepsi
  الجمعاء من البهائم وغيرها التي لم يذهب من بدنها شيء (maqayis)؛ رجل جميع أي مجتمع في خلقه (ayn)؛ الرجل المجتمع الذي بلغ أشده (sihah)؛ جميع لدينا محضرون (mufradat)
- **B010** parçaları toplanıp tamamlanma [kalıp] — koşusunu ve gücünü bütünüyle toplamak · çeşitli yerlerden birleşip büyümek · işlerin kişi için yoluna girip hazır duruma gelmesi
  استجمع الفرس جريا (maqayis)؛ استجمع للمرء أموره (ayn)؛ استجمع السيل اجتمع من كل موضع واستجمع الفرس جريا (sihah)
- **B011** adı bilinmeyen çekirdekten yetişme hurma ağacı — adı bilinmeyen çekirdekten yetişme hurma ağacı
  الجمع كل لون من النخل لا يعرف اسمه لنخل خرج من النوى (maqayis)؛ الجمع أيضا الدقل لنخل يخرج من النوى ولا يعرف اسمه (sihah)
- **B012** büyük kazan — büyük kazan
  قدر جماع وجامعة وهي العظيمة (maqayis)؛ قدر جامعة وهي العظيمة وقدر جماع أيضا للعظيمة (sihah)
- **B013** bir işte başkasıyla birleşip destek olma [kalıp] — bir işte başkasıyla birleşip ona destek olmak
  جامعت الرجل على الأمر مجامعة وجماعا إذا مالأته عليه (jamhara)؛ جامعه على أمر كذا أي اجتمع معه (sihah)

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 100:5, and ## Buluşmalar) =====
## Koşan at: soluk, adım, inceltilmiş beden

Sure, kim olduklarını adlarıyla değil, yalnızca yaptıklarıyla bildiren bir topluluk üzerine yeminle açılır: {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًا, tr:ve'l-âdiyâti dabhâ, gloss:soluk soluğa koşanlara andolsun, source:100:1}. Surenin hiçbir yerinde "at" kelimesi geçmez. Hayvan koşusundan, soluğundan, taşa vuran ayağından ve kaldırdığı tozdan tanınır. Kur'an başka yerlerde de yemini böyle açar: işiyle tanımlanan dişil çoğul bir topluluk getirir ve her yeni hareketi "fe" ile bir öncekinin hemen ardına bağlar. Bir örnek {ar:وَٱلصَّٰٓفَّٰتِ صَفًّا, tr:ve's-sâffâti saffâ, gloss:saf saf dizilenlere andolsun, source:37:1} ile {ar:فَٱلزَّٰجِرَٰتِ زَجْرًا, tr:fe'z-zâcirâti zecrâ, gloss:derken sürüp önlerine katanlara, source:37:2} çiftidir. Bir başkası {ar:وَٱلْمُرْسَلَٰتِ عُرْفًا, tr:ve'l-murselâti urfâ, gloss:ardı ardına gönderilenlere andolsun, source:77:1} ile {ar:فَٱلْعَٰصِفَٰتِ عَصْفًا, tr:fe'l-âsıfâti asfâ, gloss:derken fırtına gibi esenlere, source:77:2} çiftidir. Bu surede "fe" bağları koşuyu, kıvılcımı, sabahı, tozu ve kalabalığın ortasını tek bir hareketin ardışık aşamaları olarak dizer. Aşağıda bir kelimenin akrabalarından gelen görüntüler, o kelimenin ayetteki anlamının yanında duyulan ikinci bir ses olarak okunur. Bu görüntüler o anlamın yerine geçmez.

Birinci ayetin ilk kelimesinin kökü, koşunun en hızlısını adlandırır: {ar:العَدْو هو الحضر, tr:el-advu huve'l-hudr, gloss:adv dörtnala koşmaktır, source:"ع د و,B002"}. İyi ve çok koşan ata da aynı kökten bir sıfat verilir: {ar:يقال من عدو الفرس عدوان أي جيد العدو وكثيره, tr:yukâlu min advi'l-ferasi advân, ey ceyyidu'l-advi ve kesîruh, gloss:atın koşusundan "advân" denir, yani iyi ve çok koşan, source:"ع د و,B002"}. Ardından gelen kelime bu koşunun sesidir: {ar:صوت أنفاس الخيل إذا عدون وليس بصهيل ولا حمحمة, tr:savtu enfâsi'l-hayli izâ adevne ve leyse bi-sahîlin ve lâ hamhame, gloss:atların koşarken çıkardığı soluk sesi; ne kişneme ne homurtu, source:"ض ب ح,B001"}. Kişneme, hayvanın kendi sesidir. Burada duyulan ise zorlanan göğüsten dışarı itilen nefestir, yani kelime bir çabayı kulağa duyurur. Aynı kelime bir adım biçimini de adlandırır: {ar:ضبح الفرس وضبع إذا حرك ضبعيه في مشيه, tr:dabaha'l-ferasu ve daba'a izâ harreke dab'ayhi fî meşyih, gloss:at yürürken ön kollarını ileri atıp oynatınca "dabaha" denir, source:"ض ب ح,B002"}. Bu, {ar:هو عدو فوق التقريب وأصله ضبع, tr:huve advun fevka't-takrîbi ve asluhû dab', gloss:tırıştan hızlı bir koşudur, aslı "dab'"dır, source:"ض ب ح,B002"}. Böylece tek kelimede hem ileri uzanan ön ayaklar görülür hem de göğüsten çıkan nefes işitilir.

İkinci ayetin {ar:قَدْحًا, tr:kadhâ, gloss:çakarak, source:100:2} kelimesi ateşi anlatır. Ama bu kökün kalıplaşmış bir söyleyişi atın bedenini de gösterir: {ar:قدح الفرس تقديحا إذا ضمر حتى يصير مثل القدح, tr:kaddaha'l-ferasu takdîhan izâ damura hattâ yasîra misle'l-kıdh, gloss:at, ok çubuğu gibi oluncaya dek inceltildiğinde "kaddaha" denir, source:"ق د ح,B008"}. Koşu için yetiştirilen at fazlasından arındırılır ve gövdesi bir ok çubuğu kadar inceltilir. Beşinci ayetin {ar:جَمْعًا, tr:cem'â, gloss:bir topluluğu, source:100:5} kelimesinin yanında da aynı kökten bir at deyimi duyulur: {ar:استجمع الفرس جريا, tr:isteceme'a'l-ferasu cerye, gloss:at bütün koşusunu tek bir atılışta topladı, source:"ج م ع,B010"}.

Atın kökleri, insanı anlatan ayetlerde de geri gelir. Altıncı ayetteki {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan, source:100:6} kelimesinin kökü, bineğin bir yanını adlandırır: {ar:إنسي الدابة للجانب الذي يلي الراكب, tr:insiyyu'd-dâbbeti li'l-cânibi'llezî yelî'r-râkib, gloss:hayvanın "insî" yanı, binicinin bulunduğu taraftır, source:"ء ن س,B004"}. Hayvanın bir yanı insana dönüktür ve insan onun sırtındadır. Yedinci ayetteki {ar:لَشَهِيدٌ, tr:le-şehîd, gloss:elbette tanıktır, source:100:7} kelimesinin kökünde ise atın koşusu kendi kendinin tanığıdır: {ar:الشاهد من جريه ما يشهد له على سبقه وجودته, tr:eş-şâhidu min caryihî mâ yeşhedu lehû alâ sebkıhî ve cevdetih, gloss:koşusunun "tanığı", öne geçtiğine ve iyi cins olduğuna tanıklık eden kısımdır, source:"ش ه د,B008"}. Sekizinci ayetteki {ar:لَشَدِيدٌ, tr:le-şedîd, gloss:pek düşkündür, source:100:8} kelimesinin kökü de koşunun adıdır: {ar:الشد العدو والفعل اشتد, tr:eş-şeddu'l-advu ve'l-fi'lu iştedde, gloss:"şedd" koşudur, fiili "iştedde"dir, source:"ش د د,B003"}. Bu söyleyiş "şedd"i birinci ayetin "adv"ıyla aynı tanımda birleştirir. Onuncu ayetin {ar:ٱلصُّدُورِ, tr:es-sudûr, gloss:göğüsler, source:100:10} kelimesinin kökünde de yarışı göğsüyle kazanan at vardır: {ar:صدر الفرس إذا جاء قد سبق بصدره, tr:sadera'l-ferasu izâ câe kad sebeka bi-sadrih, gloss:at göğsüyle öne geçerek gelince "sadera" denir, source:"ص د ر,B002"}.

Bu görüntü sureye bir karşılaştırma katar. At soluğunu, bacaklarını, inceltilmiş bedenini ve bütün koşusunu sahibinin işine verir. Koşusu öne geçtiğine tanıklık eder, yarışı göğsüyle kazanır. Hemen ardından insan gelir ve onun hakkında söylenen ilk şey, Rabbine karşı {ar:لَكَنُودٌ, tr:le-kenûd, gloss:pek nankördür, source:100:6} olmasıdır. Atın tanığı kendi lehinedir, insanın tanıklığı ise kendi nankörlüğü üzerinedir. Atın "şedd"i koşusudur, insanınki ise malı sevmesidir. Göğüs at için yarışın kazanıldığı yerdir, insan için ise içindekilerin ayıklanacağı yerdir.

Kur'an atları, sevilen malı ve Rab sözünü başka bir sahnede de bir araya getirir. Akşamüstü Süleyman'a soylu, çevik atlar sunulur: {ar:إِذْ عُرِضَ عَلَيْهِ بِٱلْعَشِىِّ ٱلصَّٰفِنَٰتُ ٱلْجِيَادُ, tr:iz uride aleyhi bi'l-aşiyyi's-sâfinâtu'l-ciyâd, gloss:akşamüstü ona durup bekleyen soylu atlar sunulduğunda, source:38:31}. Süleyman şöyle der: {ar:إِنِّىٓ أَحْبَبْتُ حُبَّ ٱلْخَيْرِ عَن ذِكْرِ رَبِّى, tr:innî ahbebtu hubbe'l-hayri an zikri rabbî, gloss:ben "hayır" sevgisini Rabbimin anılmasına bağlı olarak sevdim, source:38:32}. Arapçada "an" edatı hem "-den ötürü" hem "-den uzaklaşarak" anlamını taşıyabildiği için bu cümle iki yöne açıktır. Ama sözün devamı sabittir: {ar:حَتَّىٰ تَوَارَتْ بِٱلْحِجَابِ, tr:hattâ tevârat bi'l-hicâb, gloss:ta ki perdenin ardına gizleninceye dek, source:38:32}. Ardından {ar:رُدُّوهَا عَلَىَّ ۖ فَطَفِقَ مَسْحًا بِٱلسُّوقِ وَٱلْأَعْنَاقِ, tr:ruddûhâ aleyye, fe-tafika meshan bi's-sûkı ve'l-a'nâk, gloss:"Onları bana geri getirin" dedi ve bacaklarını, boyunlarını meshetmeye koyuldu, source:38:33}. Sekizinci ayetin "hubbu'l-hayr" ifadesi burada bir peygamberin ağzında, atlarla ve "Rabbim" sözüyle birlikte geçer. Bizim surede aynı ifade atların koşusundan hemen sonra, Rabbine nankör olan insanın bağlılığını adlandırır. Kur'an, insanlara süslü gösterilen sevgilerin listesine atları da koyar: {ar:زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ, tr:zuyyine li'n-nâsi hubbu'ş-şehevât, gloss:arzulanan şeylerin sevgisi insanlara süslü gösterildi, source:3:14}. O listede altın ve gümüş yığınlarının yanında {ar:وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ, tr:ve'l-hayli'l-musevveme, gloss:salma, damgalı atlar, source:3:14} de sayılır. Böylece at hem koşan bir hayvan hem de sevilen bir maldır. Surenin karşılaştırması bu iki yüzün arasında kurulur.

Kaynaklar: 100:1 ٱلْعَٰدِيَٰتِ ع د و B002; 100:1 ضَبْحًا ض ب ح B001; 100:1 ضَبْحًا ض ب ح B002; 100:2 قَدْحًا ق د ح B008; 100:5 جَمْعًا ج م ع B010; 100:6 ٱلْإِنسَٰنَ ء ن س B004; 100:7 لَشَهِيدٌ ش ه د B008; 100:8 لَشَدِيدٌ ش د د B003; 100:10 ٱلصُّدُورِ ص د ر B002; 37:1; 37:2; 77:1; 77:2; 38:31; 38:32; 38:33; 3:14

## Şafak baskını

Koşan atların yaptığı iş üçüncü ayette adını alır: {ar:فَٱلْمُغِيرَٰتِ صُبْحًا, tr:fe'l-muğîrâti subhâ, gloss:derken sabahleyin baskın yapanlara, source:100:3}. Kelime baskın fiilinden gelir: {ar:أغار على القوم, tr:eğâra ale'l-kavm, gloss:kavmin üzerine baskın yaptı, source:"memory"}. Birinci ayetin kelimesi zaten bu işle tanımlanır: {ar:العادية الخيل المغيرة, tr:el-âdiyetu'l-haylu'l-muğîra, gloss:"âdiye", baskın yapan atlardır, source:"ع د و,B001"}. Yani koşan at, tanımı gereği baskına koşan attır. Aynı kökte saldırının ahlaki adı da vardır: {ar:العدوان الظلم الصراح, tr:el-udvânu'z-zulmu's-surâh, gloss:"udvân" apaçık haksızlıktır, source:"ع د و,B001"}. Saldırının hedefi de bu köktendir: {ar:العَدُوّ ضد الولي والجمع الأعداء, tr:el-aduvvu ziddu'l-veliyyi ve'l-cem'u'l-a'dâ', gloss:düşman, dostun karşıtıdır; çoğulu "a'dâ"dır, source:"ع د و,B003"}.

Baskının işleyişi saatine bağlıdır. Baskıncılar geceyi yolda geçirir ve ilk ışıkta konağa varır. O saatte konaklayanlar ya uykudadır ya da yeni uyanmaktadır, silahlanacak vakitleri yoktur. Bu yüzden sabah, baskının kendi adı olmuştur: {ar:يوم الصباح يوم الغارة, tr:yevmu's-sabâhi yevmu'l-ğâra, gloss:"sabah günü", baskın günüdür, source:"ص ب ح,B004"}. Aynı kökten fiil ile baskına uğrayanların çığlığı da tek bir söyleyişte birleşir: {ar:في الحرب صبحناهم أي غاديناهم بالخيل ونادوا يا صباحاه إذا استغاثوا, tr:fi'l-harbi sabbahnâhum, ey ğâdeynâhum bi'l-hayl, ve nâdev yâ sabâhâh izâ isteğâsû, gloss:savaşta "onlara sabahladık" yani atlarla sabah erkenden üstlerine vardık denir; yardım isteyenler de "Vay sabah!" diye bağırır, source:"ص ب ح,B004"}. Kelimenin sade kullanımı da aynı yöndedir: {ar:صبحته إذا أتيته صباحا, tr:sabahtuhû izâ eteytuhû sabâhan, gloss:birine sabahleyin vardığında "onu sabahladım" denir, source:"ص ب ح,B002"}.

Dördüncü ayet baskının görüntüsünü verir: {ar:فَأَثَرْنَ بِهِۦ نَقْعًا, tr:fe-eserne bihî nak'â, gloss:derken orada toz kaldırdılar, source:100:4}. Fiil havalanan toza gider: {ar:ثار الغبار يثور ثورا وثورانا أي سطع, tr:sâra'l-ğubâru yesûru sevren ve sevarânen, ey sata'a, gloss:toz kalktı, yani yükselip yayıldı, source:"ث و ر,B001"}. Fiilin kökü birinin üstüne çullanmayı da adlandırır: {ar:ثار به الناس أي وثبوا عليه, tr:sâra bihi'n-nâsu, ey vesebû aleyh, gloss:insanlar onun üstüne atıldı, source:"ث و ر,B003"}. "Nak'", yükselen tozdur: {ar:النقع الغبار المرتفع, tr:en-nak'u'l-ğubâru'l-murtefi', gloss:"nak'" yükselen tozdur, source:"ن ق ع,B004"}. Aynı kelimenin yanında bir ses de duyulur: {ar:النقع رفع الصوت, tr:en-nak'u ref'u's-savt, gloss:"nak'" sesi yükseltmektir, source:"ن ق ع,B005"}. Bu ses kesintisiz sürer: {ar:نقع بصوته وأنقع صوته إذا تابعه, tr:neka'a bi-savtihî ve enka'a savtehû izâ tâbe'ah, gloss:sesini ardı ardına sürdürdüğünde "neka'a" denir, source:"ن ق ع,B005"}. Yükselen toz bulutunun yanında, baskına uğrayan konağın "Vay sabah!" çığlığı duyulur. Ayetteki "bihî" zamiri tozu az önce anılan o sabaha ve o hamleye bağlar. Toz, baskının anında ve yerinde kalkar.

Beşinci ayet hamlenin nerede bittiğini söyler: {ar:فَوَسَطْنَ بِهِۦ جَمْعًا, tr:fe-vasatne bihî cem'â, gloss:derken orada bir topluluğun ortasına daldılar, source:100:5}. Fiil, bir kalabalığın içine girip ortasında durmaktır: {ar:وسط فلان جماعة من الناس وهو يسطهم إذا صار في وسطهم, tr:vasata fulânun cemâ'aten mine'n-nâs, ve huve yesıtuhum, izâ sâra fî vasatihim, gloss:biri bir topluluğun ortasına vardığında "onları ortaladı" denir, source:"و س ط,B003"}. "Cem'" bir araya gelmiş insan topluluğudur: {ar:الجمع اسم لجماعة الناس, tr:el-cem'u ismun li-cemâ'ati'n-nâs, gloss:"cem'" insan topluluğunun adıdır, source:"ج م ع,B002"}. Bu topluluk çoğu zaman karışıktır: {ar:الجماع ما تجمع من أشابة الناس وأخلاطهم, tr:el-cimâ'u mâ tecemma'a min uşâbeti'n-nâsi ve ahlâtihim, gloss:"cimâ'", karışık, derme çatma bir halk kalabalığıdır, source:"ج م ع,B002"}. Hamle kalabalığın kenarında durmaz, toplanmış bir halkın tam merkezinde biter. Bu, kaçacak yerin kalmadığı anı gösterir. Sekizinci ayetin kelimesi bu sahneye yeniden döner: {ar:شد على العدو إذا حمل عليه, tr:şedde ale'l-aduvvi izâ hamele aleyh, gloss:düşmana saldırdığında "şedde" denir, source:"ش د د,B003"}. Baskının ardından gelen paylaşım da dördüncü ayetin kelimesinde durur: {ar:النقيعة ما نحر من النهب قبل القسم, tr:en-nakî'atu mâ nuhira mine'n-nehbi kable'l-kasm, gloss:"nakî'a", ganimet bölüşülmeden önce boğazlanan hayvandır, source:"ن ق ع,B003"}.

Düz bir anlatım, atların hızla koşup baskın yaptığını söylemekle yetinirdi. Kelimeler ise başka şeyleri de duyurur. Saldırının tanımında "apaçık haksızlık" vardır, baskının adı bir saattir, toz ve çığlık aynı kelimededir ve hamle kalabalığın ortasında biter. Bu ani, kaçışsız sabah surenin sonundaki güne bir ön hazırlıktır. Kur'an azabın gelişini de bir şafak baskını gibi anlatır. Azabı acele isteyenlere Allah önce {ar:أَفَبِعَذَابِنَا يَسْتَعْجِلُونَ, tr:e-fe-bi-azâbinâ yesta'cilûn, gloss:azabımızı mı acele istiyorlar, source:37:176} diye sorar, sonra şöyle der: {ar:فَإِذَا نَزَلَ بِسَاحَتِهِمْ فَسَآءَ صَبَاحُ ٱلْمُنذَرِينَ, tr:fe-izâ nezele bi-sâhatihim fe-sâe sabâhu'l-munzerîn, gloss:o, avlularına indiğinde, uyarılmışların sabahı ne kötüdür, source:37:177}. Azap yurdun avlusuna iner ve bunun vakti "sabah"tır. Lut'a gelen elçiler ona ailesiyle geceleyin yola çıkmasını söyler ve {ar:إِنَّ مَوْعِدَهُمُ ٱلصُّبْحُ ۚ أَلَيْسَ ٱلصُّبْحُ بِقَرِيبٍ, tr:inne mev'idehumu's-subh, e-leyse's-subhu bi-karîb, gloss:onların buluşma vakti sabahtır; sabah yakın değil mi, source:11:81} diye ekler. Hicr halkı için {ar:فَأَخَذَتْهُمُ ٱلصَّيْحَةُ مُصْبِحِينَ, tr:fe-ehazethumu's-sayhatu musbihîn, gloss:sabaha girerlerken onları o çığlık yakaladı, source:15:83} denir. Lut kavmi için aynı fiil kullanılır: {ar:وَلَقَدْ صَبَّحَهُم بُكْرَةً عَذَابٌ مُّسْتَقِرٌّ, tr:ve le-kad sabbahahum bukraten azâbun mustakır, gloss:andolsun, erkenden kalıcı bir azap onlara sabahladı, source:54:38}. Kur'an atlı akın görüntüsünü İblis'e verilen izinde de kullanır: {ar:وَأَجْلِبْ عَلَيْهِم بِخَيْلِكَ وَرَجِلِكَ, tr:ve eclib aleyhim bi-haylike ve recilik, gloss:atlılarınla ve yayalarınla üzerlerine yaygarayla yürü, source:17:64}. Müminlere verilen buyrukta ise atlar ile "düşman" kelimesi aynı ayette durur: {ar:وَمِن رِّبَاطِ ٱلْخَيْلِ تُرْهِبُونَ بِهِۦ عَدُوَّ ٱللَّهِ وَعَدُوَّكُمْ, tr:ve min ribâti'l-hayli turhibûne bihî aduvva'llâhi ve aduvvekum, gloss:bağlanıp hazır tutulan atlardan; onlarla Allah'ın düşmanını ve sizin düşmanınızı caydırırsınız, source:8:60}.

Kaynaklar: 100:1 ٱلْعَٰدِيَٰتِ ع د و B001; 100:1 ٱلْعَٰدِيَٰتِ ع د و B003; 100:3 فَٱلْمُغِيرَٰتِ غ و ر (memory); 100:3 صُبْحًا ص ب ح B004; 100:3 صُبْحًا ص ب ح B002; 100:4 فَأَثَرْنَ ث و ر B001; 100:4 فَأَثَرْنَ ث و ر B003; 100:4 نَقْعًا ن ق ع B004; 100:4 نَقْعًا ن ق ع B005; 100:4 نَقْعًا ن ق ع B003; 100:5 فَوَسَطْنَ و س ط B003; 100:5 جَمْعًا ج م ع B002; 100:8 لَشَدِيدٌ ش د د B003; 37:176; 37:177; 11:81; 15:83; 54:38; 17:64; 8:60

## Sıkılmış el ve ortak kazan

Sekizinci ayet insanın neye bağlandığını söyler: {ar:وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ, tr:ve innehû li-hubbi'l-hayri le-şedîd, gloss:ve şüphesiz o, hayrı sevmekte pek şiddetlidir, source:100:8}. Bu ayetteki "hayr" mal olarak açıklanır: {ar:وإنه لحب الخير لشديد أي المال الكثير, tr:ve innehû li-hubbi'l-hayri le-şedîd, ey el-mâlu'l-kesîr, gloss:"hayrı sevmekte şiddetlidir", yani çok malı, source:"خ ي ر,B004"}. Ama her mala bu ad verilmez: {ar:لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب, tr:lâ yukâlu li'l-mâli hayrun hattâ yekûne kesîran ve min mekânin tayyib, gloss:mal çok olmadıkça ve temiz bir yerden gelmedikçe ona "hayır" denmez, source:"خ ي ر,B004"}. Bu ad {ar:ما كان مجموعا من المال من وجه محمود, tr:mâ kâne mecmû'an mine'l-mâli min vechin mahmûd, gloss:övülen bir yoldan toplanmış mal, source:"خ ي ر,B004"} için kullanılır. Kur'an kelimeyi bu anlamda vasiyet hükmünde de kullanır: {ar:إِن تَرَكَ خَيْرًا ٱلْوَصِيَّةُ لِلْوَٰلِدَيْنِ وَٱلْأَقْرَبِينَ, tr:in teraka hayran el-vasiyyetu li'l-vâlideyni ve'l-akrabîn, gloss:geride mal bırakacaksa anne babaya ve yakınlara vasiyet, source:2:180}. Kelime iyi bir şeyi adlandırır, ama sevgi bu iyi şeye takıldığında onu tutsak eder.

Sevgi kelimesinin kendisi de bu takılmayı gösterir. Önce bir tanımı vardır: {ar:المحبة إرادة ما تراه أو تظنه خيرا, tr:el-mahabbetu irâdetu mâ terâhu ev tezunnuhû hayran, gloss:sevgi, hayır olarak gördüğün ya da sandığın şeyi istemektir, source:"ح ب ب,B002"}. Bu tanım "sevgi" ile "hayr"ı tek bir cümlede birleştirir. Ardından bir yapışma anlamı gelir: {ar:الحب والمحبة اشتقاقه من أحبه إذا لزمه, tr:el-hubbu ve'l-mahabbetu iştikâkuhû min ehabbehû izâ lezimeh, gloss:sevgi kelimesi, bir şeye yapışıp ondan ayrılmamak anlamındaki "ehabbe"den türer, source:"ح ب ب,B002"}. Bu yapışmanın bir hayvan görüntüsü de vardır: {ar:أحب البعير إذا حرن ولزم مكانه, tr:ehabbe'l-ba'îru izâ harune ve lezime mekânehû, gloss:deve inat edip yerinden kıpırdamadığında "ehabbe" denir, source:"ح ب ب,B005"}. Birinci ayette at bütün gücüyle ileri atılır. Sekizinci ayetin sevgisinin yanında ise yerine çakılıp kalan deve duyulur.

"Şedîd" kelimesi de bu ayette cimri olarak açıklanır: {ar:لشديد أي لبخيل, tr:le-şedîd, ey le-bahîl, gloss:"şedîd" yani cimri, source:"ش د د,B006"}. Kelimenin bir başka kullanımı da aynı yöndedir: {ar:الشديد والمتشدد البخيل, tr:eş-şedîdu ve'l-muteşeddidu'l-bahîl, gloss:"şedîd" ve "muteşeddid" cimridir, source:"ش د د,B006"}. Kökün aslı bağlamaktır: {ar:شده أي أوثقه, tr:şeddehû, ey evsekah, gloss:onu sıkıca bağladı, source:"ش د د,B001"}; {ar:الشد العقد القوي, tr:eş-şeddu'l-akdu'l-kaviyy, gloss:"şedd" sağlam düğümdür, source:"ش د د,B001"}. Kese sıkıca bağlanır, düğüm çözülmez. Beşinci ayetin kelimesinin ailesi aynı eli gösterir: {ar:جمع الكف وهو حين تقبضها, tr:cum'u'l-keff, ve huve hîne takbiduhâ, gloss:"cum'", avucun yumulmuş halidir, source:"ج م ع,B005"}. Aynı ailede yumruğun en ağır biçimi de vardır: {ar:الجامعة الغل لأنها تجمع اليدين إلى العنق, tr:el-câmi'atu'l-ğull, li-ennehâ tecma'u'l-yedeyni ile'l-unuk, gloss:"câmi'a" bukağıdır, çünkü elleri boyuna toplar, source:"ج م ع,B008"}. Kökün genel anlamı bir araya çekmektir: {ar:الجمع ضم الشيء بتقريب بعضه من بعض, tr:el-cem'u dammu'ş-şey'i bi-takrîbi ba'dıhî min ba'd, gloss:toplamak, bir şeyin parçalarını birbirine yaklaştırarak bir araya getirmektir, source:"ج م ع,B001"}. Kenûd olan kişi de bu el ile tarif edilir: {ar:يأكل وحده ويضرب عبده ويمنع رفده, tr:ye'kulu vahdehû ve yadribu abdehû ve yemne'u rifdeh, gloss:yalnız yer, kölesini döver, yardımını esirger, source:"ك ن د,B002"}.

Bu yumulmuş elin karşısında aynı köklerden kurulan bir sofra durur. Beşinci ayetin kelimesinin ailesinde büyük bir kazan vardır: {ar:قدر جماع وجامعة وهي العظيمة, tr:kıdrun cimâ'un ve câmi'atun, ve hiye'l-azîme, gloss:"cimâ'" ve "câmi'a" kazan, büyük kazandır, source:"ج م ع,B012"}. İkinci ayetin kelimesinin ailesinde bu kazandan yemek kepçeyle alınır: {ar:قدحت القدر غرفت ما فيها, tr:kadahtu'l-kıdr, ğaraftu mâ fîhâ, gloss:kazanı "kadh" ettim, yani içindekini kepçeledim, source:"ق د ح,B005"}. Kepçe kazanın dibine kadar iner: {ar:القديح ما يبقى في أسفل القدر فيغرف بجهد, tr:el-kadîhu mâ yebkâ fî esfeli'l-kıdri fe-yuğrafu bi-cehd, gloss:"kadîh", kazanın dibinde kalıp güçlükle kepçelenen yemektir, source:"ق د ح,B005"}. Aynı ailede içki kabı da vardır: {ar:القدح واحد الأقداح التي للشرب, tr:el-kadahu vâhidu'l-akdâhi'lletî li'ş-şurb, gloss:"kadah", içmek için kullanılan kaplardan biridir, source:"ق د ح,B006"}. Paylar ise kura oklarıyla dağıtılır: {ar:القدح الواحد من قداح الميسر, tr:el-kıdhu'l-vâhidu min kıdâhi'l-meysir, gloss:"kıdh", meysir oklarından biridir, source:"ق د ح,B007"}. Bu okların durduğu kabın adı, altıncı ve on birinci ayetteki Rab kelimesinin ailesindendir: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-rıbâbetu şebîhetun bi'l-kinâneti tucma'u fîhâ sihâmu'l-meysir, gloss:"rıbâbe", meysir oklarının toplandığı, ok kılıfına benzer bir kaptır, source:"ر ب ب,B010"}. Dördüncü ayetin kelimesinin ailesinde de kesilen hayvan ve yolcuya sunulan yemek vardır: {ar:النقيعة الجزور تنقع عن عدة إبل, tr:en-nakî'atu'l-cezûru tunka'u an iddeti ibil, gloss:"nakî'a", birkaç deve arasından ayrılıp kesilen devedir, source:"ن ق ع,B003"}; {ar:النقيعة الطعام يتخذ للقادم من السفر, tr:en-nakî'atu't-ta'âmu yuttehazu li'l-kâdimi mine's-sefer, gloss:"nakî'a", yolculuktan dönen için hazırlanan yemektir, source:"ن ق ع,B003"}. Son ayetin kelimesinin ailesinde ise ortaklaşa alınıp bölüşülen et vardır: {ar:تخبر القوم بينهم خبرة إذا اشتروا شاة فذبحوها واقتسموا لحمها, tr:tehabbera'l-kavmu beynehum hubreten izâ işterev şâten fe-zebehûhâ ve'ktesemû lahmehâ, gloss:bir koyunu birlikte satın alıp kesen ve etini bölüşen topluluk için "tehabbera" denir, source:"خ ب ر,B006"}. Bütün bu sofranın adı da hayırdır: {ar:والخير الكرم, tr:ve'l-hayru'l-kerem, gloss:hayır, cömertliktir, source:"خ ي ر,B005"}. Böylece kelimeler, kenûdun "yalnız yer" tanımının tam karşısına büyük kazanı, kepçeyi, kabı, payları, kesilen hayvanı ve bölüşülen eti koyar.

Onuncu ayetin fiili bu biriktirmeyi biriktirenin üzerine çevirir: {ar:أصل واحد منقاس وهو جمع الشيء, tr:aslun vâhidun munkâs, ve huve cem'u'ş-şey', gloss:tek ve kuralı işleyen bir köktür; bir şeyi toplamaktır, source:"ح ص ل,B001"}. Yumruğunu sıkıp malını toplayan kişi, sonunda göğsündekilerin toplanıp ortaya konduğu kişi olur. Düz bir anlatım "insan mala düşkündür" demekle kalırdı. Görüntü ise bu düşkünlüğün bedenini gösterir: yumulmuş avuç, boyna bağlanmış eller, yerinden kıpırdamayan deve ve tek başına yenen yemek.

Kur'an biriktireni hem sözle hem de bu el görüntüsüyle anar. Ayıplayıp çekiştirenler için {ar:ٱلَّذِى جَمَعَ مَالًا وَعَدَّدَهُۥ, tr:ellezî ceme'a mâlen ve addedeh, gloss:mal toplayıp onu tekrar tekrar sayan, source:104:2} ve {ar:يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ, tr:yahsebu enne mâlehû ahledeh, gloss:malının kendisini ölümsüz kıldığını sanır, source:104:3} denir. Cehennem ateşi yüz çevireni çağırır: {ar:وَجَمَعَ فَأَوْعَىٰٓ, tr:ve ceme'a fe-ev'â, gloss:toplayıp kaba doldurup saklayanı, source:70:18}. Aynı yerde insanın yaratılışı anlatılır: {ar:إِنَّ ٱلْإِنسَٰنَ خُلِقَ هَلُوعًا, tr:inne'l-insâne hulika helû'â, gloss:insan pek sabırsız yaratıldı, source:70:19}; {ar:وَإِذَا مَسَّهُ ٱلْخَيْرُ مَنُوعًا, tr:ve izâ messehu'l-hayru menû'â, gloss:kendisine hayır dokununca da pek esirgeyici olur, source:70:21}. Bu ayette "insan" ve "hayr", bizim suredeki gibi yan yana ve aynı esirgeme anlamında geçer. Rabbinin kendisini aşağıladığını söyleyen insana şu cevap verilir: {ar:كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ, tr:kellâ bel lâ tukrimûne'l-yetîm, gloss:hayır, siz yetime ikram etmiyorsunuz, source:89:17}; {ar:وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ tehâddûne alâ ta'âmi'l-miskîn, gloss:yoksulu doyurmaya birbirinizi teşvik etmiyorsunuz, source:89:18}; {ar:وَتُحِبُّونَ ٱلْمَالَ حُبًّا جَمًّا, tr:ve tuhibbûne'l-mâle hubben cemmâ, gloss:malı yığın yığın bir sevgiyle seviyorsunuz, source:89:20}. Boyna bağlı el görüntüsü bir buyrukta açıkça yer alır: {ar:وَلَا تَجْعَلْ يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:ve lâ tec'al yedeke mağlûleten ilâ unukik, gloss:elini boynuna bağlı kılma, source:17:29}. Buyruğun hemen ardından gelen ayet, bizim surenin son kelimesiyle biter: {ar:إِنَّ رَبَّكَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ ۚ إِنَّهُۥ كَانَ بِعِبَادِهِۦ خَبِيرًا بَصِيرًا, tr:inne rabbeke yebsutu'r-rızka li-men yeşâu ve yakdir, innehû kâne bi-ibâdihî habîran basîrâ, gloss:Rabbin rızkı dilediğine bol verir, dilediğine daraltır; O kullarından haberdar olandır, onları görendir, source:17:30}. Aynı surede insanın tutumu şöyle özetlenir: {ar:قُل لَّوْ أَنتُمْ تَمْلِكُونَ خَزَآئِنَ رَحْمَةِ رَبِّىٓ إِذًا لَّأَمْسَكْتُمْ خَشْيَةَ ٱلْإِنفَاقِ ۚ وَكَانَ ٱلْإِنسَٰنُ قَتُورًا, tr:kul lev entum temlikûne hazâine rahmeti rabbî izen le-emsektum haşyete'l-infâk, ve kâne'l-insânu katûrâ, gloss:de ki: Rabbimin rahmet hazinelerine siz sahip olsaydınız, harcamaktan korkup elinizde tutardınız; insan pek eli sıkıdır, source:17:100}. Cimrilerin tuttukları şey sonunda boyunlarına dolanır: {ar:سَيُطَوَّقُونَ مَا بَخِلُوا۟ بِهِۦ يَوْمَ ٱلْقِيَٰمَةِ, tr:se-yutavvakûne mâ bahılû bihî yevme'l-kıyâme, gloss:cimrilik ettikleri şey kıyamet günü boyunlarına dolanacak, source:3:180}. Bu ayet de {ar:وَٱللَّهُ بِمَا تَعْمَلُونَ خَبِيرٌ, tr:va'llâhu bimâ ta'melûne habîr, gloss:Allah yaptıklarınızdan haberdardır, source:3:180} sözüyle biter.

Ortak kazan görüntüsü de Kur'an'da karşılığını bulur. Davud'un ailesi için yapılanlar arasında {ar:وَجِفَانٍ كَٱلْجَوَابِ وَقُدُورٍ رَّاسِيَٰتٍ, tr:ve cifânin ke'l-cevâbi ve kudûrin râsiyât, gloss:havuz gibi çanaklar ve yerinden kalkmayan kazanlar, source:34:13} sayılır. Hemen ardından {ar:ٱعْمَلُوٓا۟ ءَالَ دَاوُۥدَ شُكْرًا ۚ وَقَلِيلٌ مِّنْ عِبَادِىَ ٱلشَّكُورُ, tr:i'melû âle dâvûde şukrâ, ve kalîlun min ibâdiye'ş-şekûr, gloss:ey Davud ailesi, şükür olarak çalışın; kullarımdan şükredenler azdır, source:34:13} denir. Büyük kazan ile şükür aynı ayette durur. Sevdiği şeyi verenler de anılır: {ar:وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًا وَيَتِيمًا وَأَسِيرًا, tr:ve yut'imûne't-ta'âme alâ hubbihî miskînen ve yetîmen ve esîrâ, gloss:ona olan sevgilerine rağmen yemeği yoksula, yetime ve esire yedirirler, source:76:8}. İyiliğin tarifinde de aynı kalıp kullanılır: {ar:وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ, tr:ve âte'l-mâle alâ hubbih, gloss:malı, sevgisine rağmen verdi, source:2:177}. Hüküm de açıktır: {ar:لَن تَنَالُوا۟ ٱلْبِرَّ حَتَّىٰ تُنفِقُوا۟ مِمَّا تُحِبُّونَ, tr:len tenâlû'l-birra hattâ tunfikû mimmâ tuhibbûn, gloss:sevdiğiniz şeylerden harcamadıkça iyiliğe erişemezsiniz, source:3:92}. Sevgi bu ayetlerde de vardır, ama tutan elde değil veren eldedir. Yalnız yiyenin tarifi de Kur'an'da geçer: {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ ta'âmi'l-miskîn, gloss:yoksulu doyurmaya teşvik etmezdi, source:69:34}; {ar:وَيَمْنَعُونَ ٱلْمَاعُونَ, tr:ve yemne'ûne'l-mâ'ûn, gloss:en küçük yardımı bile esirgerler, source:107:7}. Göğüs bu sahnede de belirir. Göç edenleri yurtlarında karşılayanlar için {ar:وَلَا يَجِدُونَ فِى صُدُورِهِمْ حَاجَةً مِّمَّآ أُوتُوا۟ وَيُؤْثِرُونَ عَلَىٰٓ أَنفُسِهِمْ, tr:ve lâ yecidûne fî sudûrihim hâceten mimmâ ûtû ve yu'sirûne alâ enfusihim, gloss:onlara verilenden ötürü göğüslerinde bir istek duymazlar ve onları kendilerine tercih ederler, source:59:9} denir. Ayet şöyle sürer: {ar:وَمَن يُوقَ شُحَّ نَفْسِهِۦ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ, tr:ve men yûka şuhha nefsihî fe-ulâike humu'l-muflihûn, gloss:kim nefsinin hırsından korunursa, işte onlar kurtuluşa erenlerdir, source:59:9}.

Kaynaklar: 100:8 ٱلْخَيْرِ خ ي ر B004; 100:8 ٱلْخَيْرِ خ ي ر B005; 100:8 لِحُبِّ ح ب ب B002; 100:8 لِحُبِّ ح ب ب B005; 100:8 لَشَدِيدٌ ش د د B006; 100:8 لَشَدِيدٌ ش د د B001; 100:5 جَمْعًا ج م ع B005; 100:5 جَمْعًا ج م ع B008; 100:5 جَمْعًا ج م ع B001; 100:5 جَمْعًا ج م ع B012; 100:6 لَكَنُودٌ ك ن د B002; 100:10 وَحُصِّلَ ح ص ل B001; 100:2 قَدْحًا ق د ح B005; 100:2 قَدْحًا ق د ح B006; 100:2 قَدْحًا ق د ح B007; 100:6 لِرَبِّهِۦ ر ب ب B010; 100:4 نَقْعًا ن ق ع B003; 100:11 لَّخَبِيرٌ خ ب ر B006; 2:180; 104:2; 104:3; 70:18; 70:19; 70:21; 89:17; 89:18; 89:20; 17:29; 17:30; 17:100; 3:180; 34:13; 76:8; 2:177; 3:92; 69:34; 107:7; 59:9

## Toplanmış kalabalık ve toplanma günü

Beşinci ayetin {ar:جَمْعًا, tr:cem'â, gloss:bir topluluğu, source:100:5} kelimesi baskına uğrayan kalabalıktır: {ar:الجمع اسم لجماعة الناس, tr:el-cem'u ismun li-cemâ'ati'n-nâs, gloss:"cem'", insan topluluğunun adıdır, source:"ج م ع,B002"}. Aynı kök insanların toplandığı yeri ve günü de adlandırır: {ar:المجمع حيث يجمع الناس, tr:el-mecma'u haysu yucma'u'n-nâs, gloss:"mecma'", insanların toplandığı yerdir, source:"ج م ع,B004"}. Bu yerin ve günün en büyüğü de bu kökle anılır: {ar:يوم الجمع ويوم يجمعكم ليوم الجمع, tr:yevmu'l-cem'i ve yevme yecme'ukum li-yevmi'l-cem', gloss:"toplanma günü" ve "sizi toplanma günü için toplayacağı gün", source:"ج م ع,B004"}. Beşinci ayetin fiili, bir şeyin iki kenarı arasında kalan yeri adlandıran bir köke dayanır: {ar:اسما لما بين طرفي كل شيء, tr:isman li-mâ beyne tarafey kulli şey', gloss:her şeyin iki ucu arasındakinin adı, source:"و س ط,B002"}. Atlar kalabalığın iki kenarı arasında, tam ortasında durur. Yedinci ayetin tanık kelimesinin kökü de bir toplanma yerinin adıdır: {ar:المشهد مجمع الناس, tr:el-meşhedu mecma'u'n-nâs, gloss:"meşhed", insanların toplandığı yerdir, source:"ش ه د,B001"}. Fiil hazır bulunmayı anlatır: {ar:شهده شهودا أي حضره, tr:şehidehû şuhûden, ey hadarah, gloss:"şehidehû", yani orada hazır bulundu, source:"ش ه د,B001"}. Onuncu ayetin fiili de bir toplamadır: {ar:أصل واحد منقاس وهو جمع الشيء, tr:aslun vâhidun munkâs, ve huve cem'u'ş-şey', gloss:tek ve kuralı işleyen bir köktür; bir şeyi toplamaktır, source:"ح ص ل,B001"}. On birinci ayetteki {ar:يَوْمَئِذٍ, tr:yevme'izin, gloss:o gün, source:100:11} ise bütün bunları bir güne bağlar.

Bu görüntünün sureye kattığı şey bir ölçek değişimidir. Beşinci ayette atlar bir obanın, belki birkaç çadırlık bir halkın ortasına dalar. Surenin sonundaki gün ise bütün insanların toplandığı gündür. Önce bir kalabalık şaşkınlıkla yakalanır, sonra herkes bir araya getirilir. Düz bir anlatım baskının yalnızca bir savaş sahnesi olduğunu söylerdi. Kökler ise aynı kelimeyi o büyük toplanmaya doğru açık tutar.

Kur'an bu toplanmayı beşinci ayetin kelimesiyle, aynı biçimde anlatır. Bir seddin yerle bir edileceği vaadinin ardından şöyle denir: {ar:وَنُفِخَ فِى ٱلصُّورِ فَجَمَعْنَٰهُمْ جَمْعًا, tr:ve nufiha fi's-sûri fe-cema'nâhum cem'â, gloss:sura üfürüldü ve onları hep birlikte topladık, source:18:99}. Yok edilen kavimlerin hikâyeleri anlatıldıktan sonra da o gün iki kökle birden anılır: {ar:ذَٰلِكَ يَوْمٌ مَّجْمُوعٌ لَّهُ ٱلنَّاسُ وَذَٰلِكَ يَوْمٌ مَّشْهُودٌ, tr:zâlike yevmun mecmû'un lehu'n-nâsu ve zâlike yevmun meşhûd, gloss:o, insanların kendisi için toplandığı bir gündür; o, herkesin hazır bulunduğu bir gündür, source:11:103}. Bu ayette beşinci ayetin kökü ile yedinci ayetin kökü yan yana durur. O günün adı da verilir: {ar:يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ, tr:yevme yecme'ukum li-yevmi'l-cem', zâlike yevmu't-teğâbun, gloss:sizi toplanma günü için toplayacağı gün; o, kazancın ve kaybın ortaya çıktığı gündür, source:64:9}. Toplanmanın nasıl olacağı da anlatılır: {ar:وَنُفِخَ فِى ٱلصُّورِ فَإِذَا هُم مِّنَ ٱلْأَجْدَاثِ إِلَىٰ رَبِّهِمْ يَنسِلُونَ, tr:ve nufiha fi's-sûri fe-izâ hum mine'l-ecdâsi ilâ rabbihim yensilûn, gloss:sura üfürülür ve onlar kabirlerinden Rablerine doğru akın akın koşarlar, source:36:51}. Bu ayette de "Rableri" kelimesi geçer, tıpkı on birinci ayette olduğu gibi. Toplanış tek bir sesle tamamlanır: {ar:إِن كَانَتْ إِلَّا صَيْحَةً وَٰحِدَةً فَإِذَا هُمْ جَمِيعٌ لَّدَيْنَا مُحْضَرُونَ, tr:in kânet illâ sayhaten vâhideten fe-izâ hum cemî'un ledeynâ muhdarûn, gloss:yalnızca tek bir çığlık olur ve hepsi birden huzurumuza getirilir, source:36:53}.

Kaynaklar: 100:5 جَمْعًا ج م ع B002; 100:5 جَمْعًا ج م ع B004; 100:5 فَوَسَطْنَ و س ط B002; 100:7 لَشَهِيدٌ ش ه د B001; 100:10 وَحُصِّلَ ح ص ل B001; 18:99; 11:103; 64:9; 36:51; 36:53

## Buluşmalar

İlk buluşma, surenin açılış sahnesinde koşan at ile şafak baskını arasındadır. Koşanların tanımı zaten baskın yapanlardır: {ar:العادية الخيل المغيرة, tr:el-âdiyetu'l-haylu'l-muğîra, gloss:"âdiye", baskın yapan atlardır, source:"ع د و,B001"}. Sekizinci ayetin "şedd" kelimesi de iki görüntüyü aynı anda taşır. Bir yanda koşudur, öbür yanda düşmana saldırıdır: {ar:شد على العدو إذا حمل عليه, tr:şedde ale'l-aduvvi izâ hamele aleyh, gloss:düşmana saldırdığında "şedde" denir, source:"ش د د,B003"}. Aynı sahnede ateş görüntüsü de yer alır. Soluk soluğa koşan hayvanların ayakları taşlara çarparak kıvılcım çıkarır. Birinci ayetin kelimesi bir yandan bu soluğu, bir yandan da yanmış çakmak taşını adlandırır. Koşu, kıvılcım ve sabah tek bir hareketin ardışık parçalarıdır.

Surenin iki yarısını birbirine bağlayan asıl buluşma, dördüncü ayetin tozu ile dokuzuncu ayetin kabirleri arasındadır. Toynakların toprağı kaldırması ile kabirlerin altüst edilmesi aynı fiille açıklanır: "bu'sira", "usîra" demektir. Böylece surenin ilk yarısındaki sabah baskını, ikinci yarısındaki altüst oluşun bir ön provası olur. Kur'an da kabirlerden çıkışı bir koşu olarak anlatır: {ar:يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًا كَأَنَّهُمْ إِلَىٰ نُصُبٍ يُوفِضُونَ, tr:yevme yahrucûne mine'l-ecdâsi sirâ'an ke-ennehum ilâ nusubin yûfidûn, gloss:kabirlerden hızla çıkacakları, sanki dikili bir hedefe koşuyorlarmış gibi seğirtecekleri gün, source:70:43}. Bir başka yerde de {ar:يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًا, tr:yevme teşakkaku'l-ardu anhum sirâ'â, gloss:yerin yarılıp onların hızla çıktığı gün, source:50:44} denir. Surenin başında koşanlar atlardır. Sonunda ise koşanlar kabirlerden çıkan insanlardır. Bu insanların gittiği yer de beşinci ayetteki gibi bir topluluğun ortasıdır, ama bu kez bütün insanların toplandığı yerdir.

Ateş ile kabir de aynı kökte buluşur. İkinci ayetin "ateşi çıkarmak" fiili ile gömmenin "örtmek" fiili aynı köktendir. Kur'an ateşi dirilişe delil olarak da kullanır. Çakılan ateşe dair soru dirilişi inkâr edenlere sorulur. Yeşil ağaçtan çıkan ateş de çürümüş kemikleri kimin dirilteceğini soran kişiye verilen cevaptır. Tahtanın içinde gizli duran ateş çakılınca dışarı çıkar, toprağın içinde gizli duran insan da altüst edilince dışarı çıkar. Yağmur sahnesi de aynı yere varır. İyi toprak ile kıt ürün veren toprağı karşılaştıran ayetten hemen önce şöyle denir: {ar:كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:kezâlike nuhrici'l-mevtâ le'allekum tezekkerûn, gloss:ölüleri de böyle çıkarırız; belki düşünüp öğüt alırsınız, source:7:57}. Kenûd toprak bitki bitirmez. Ama sonunda kabirleri altüst edilecek olan da aynı topraktır.

Biriktirilen mal ile göğsün ayıklanması da bir sahnede buluşur. Onuncu ayetin fiilinin aslı, altını maden toprağından ayırmaktır. Biriktirenin malı ise toplanmış altın ve gümüştür. Kur'an bu iki şeyi ateşte birleştirir: {ar:وَٱلَّذِينَ يَكْنِزُونَ ٱلذَّهَبَ وَٱلْفِضَّةَ وَلَا يُنفِقُونَهَا فِى سَبِيلِ ٱللَّهِ, tr:ve'llezîne yeknizûne'z-zehebe ve'l-fiddate ve lâ yunfikûnehâ fî sebîli'llâh, gloss:altın ve gümüşü yığıp Allah yolunda harcamayanlar, source:9:34}; {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhuhum ve cunûbuhum ve zuhûruhum, gloss:o gün bunlar cehennem ateşinde kızdırılır ve alınları, yanları ve sırtları onlarla dağlanır, source:9:35}. Malın bağlılığı ile göğsün içindekinin çıkarılması da tek bir ayette bir aradadır: {ar:إِن يَسْـَٔلْكُمُوهَا فَيُحْفِكُمْ تَبْخَلُوا۟ وَيُخْرِجْ أَضْغَٰنَكُمْ, tr:in yes'elkumûhâ fe-yuhfikum tebhalû ve yuhric adğânekum, gloss:onları (mallarınızı) sizden isteyip ısrar etseydi cimrilik ederdiniz ve O da kinlerinizi dışarı çıkarırdı, source:47:37}. Sevgi kelimesinin "kalbin tanesi" anlamı da bu buluşmayı kelimenin içinden kurar. İnsanın şiddetle bağlandığı mal göğsün içindeki tanedir, harman savrulduğunda ayrılacak olan da odur. Beşinci ayetin kökü de aynı sahnede iki yönde işler. Mal toplayan, yumruğunu sıkan kişi sonunda toplanma gününde toplananlardan biri olur. Onuncu ayetin fiili de bir toplamadır.

Sabah baskını ile malı esirgeme de bir Kur'an sahnesinde birleşir. Bir bahçenin sahipleri ürünü sabahleyin devşireceklerine yemin ederler: {ar:إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ, tr:iz aksemû le-yasrimunnehâ musbihîn, gloss:onu sabaha girerken mutlaka devşireceklerine yemin ettiklerinde, source:68:17}. Onlar uyurken {ar:فَطَافَ عَلَيْهَا طَآئِفٌ مِّن رَّبِّكَ وَهُمْ نَآئِمُونَ, tr:fe-tâfe aleyhâ tâifun min rabbike ve hum nâimûn, gloss:onlar uykudayken Rabbinden bir bela bahçeyi sardı, source:68:19}. Bahçe {ar:فَأَصْبَحَتْ كَٱلصَّرِيمِ, tr:fe-asbahat ke's-sarîm, gloss:sabaha kapkara kesilmiş halde girdi, source:68:20}. Habersiz sahipler ise {ar:فَتَنَادَوْا۟ مُصْبِحِينَ, tr:fe-tenâdev musbihîn, gloss:sabaha girerken birbirlerine seslendiler, source:68:21}. Konuştukları şey şudur: {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌ, tr:en lâ yedhulennehe'l-yevme aleykum miskîn, gloss:bugün oraya hiçbir yoksul yanınıza girmesin, source:68:24}. Bu sahnede bir sabah seferi, yoksula kapanan bir el ve Rabbin cevabı vardır. Sabah baskını yapan, sonunda baskına uğrayan olur. Bizim surede de "yalnız yiyen" kenûd, "sabah" sözüyle başlayan bir surenin sonunda Rabbinin bilgisi karşısında durur.

Su başı ile toprağın altüst edilmesi aynı günün anlatımında buluşur. Yerin sarsıldığı ve ağırlıklarını dışarı attığı gün, insanların {ar:يَصْدُرُ, tr:yasduru, gloss:sudan döner gibi döner, source:99:6} günüdür. Fiil onuncu ayetin göğüs kelimesiyle aynı köktendir. Kabirden çıkış, gömülü olanın açılması ve sudan dönüş tek bir anda birleşir. İnsanlar amellerini görmek için bölük bölük döner.

Tanıklık ile Rab sözü ise yedinci ayetin iki okumasını bir araya getirir. Âdem oğullarının "Rabbiniz değil miyim" sorusuna "evet, tanık olduk" diye cevap verdiği sahnede, insan kendi Rabbine dair kendisi üzerine tanıktır. Bizim surede de aynı insan, Rabbine karşı nankörlüğü üzerine tanıktır. Birinci ayetin atının tanığı ise koşusudur ve onun öne geçtiğine tanıklık eder. Aynı kelime atta lehte, insanda aleyhte işler.

Bu buluşmalar surenin hareketini dışarıdan içeriye doğru taşır. Sure, gözle görülen ve kulakla işitilen şeylerle başlar: soluk, kıvılcım, sabah ışığı, toz ve kalabalık. Sonra göze görünmeyen bir yere, göğüsteki taneye ulaşır. Toynakların kaldırdığı toprak kabirlerin toprağına, baskının sabahı toplanma gününe, yağmurun beklendiği tarla kabirlerini açan yere dönüşür. Malın düğümü ve yumulmuş el de toplanıp ayıklanan bir göğse dönüşür. Bu yolun her aşamasında bilgi de derinleşir: önce hazır bulunan ve gören bir tanık vardır, sonra sorulan ama cevaplanmayan bir bilgi, en sonda da içini bilen bir Rab.

