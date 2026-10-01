Focus: 100:7. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/100_7/D.r13/context.md =====
# 100:7 — focus

وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ

Anchor translation (canonical reading, reference only):

O da buna gerçekten tanıktır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَإِنَّهُۥ | إِنّ |  | CONJ;ACC;PRON |
| 2 | عَلَىٰ | عَلَىٰ |  | P |
| 3 | ذَٰلِكَ | ذَٰلِك |  | DEM |
| 4 | لَشَهِيدٌ | شَهِيد | ش ه د | EMPH;N |


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
- 100:5 فَوَسَطْنَ بِهِۦ جَمْعًا
- 100:6 إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌۭ
- 100:7 ◀ focus وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌۭ
- 100:8 وَإِنَّهُۥ لِحُبِّ ٱلْخَيْرِ لَشَدِيدٌ
- 100:9 ۞ أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ
- 100:10 وَحُصِّلَ مَا فِى ٱلصُّدُورِ
- 100:11 إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍۢ لَّخَبِيرٌۢ


===== _commentary/v16/work/100_7/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ش ه د (root_000822) — identity root of لَشَهِيدٌ (w4)

- **B001** hazır bulunup görme — hazır bulunmak ve bizzat görmek · görerek hazır bulunma · bizzat görme ve gözle karşılaşma · insanların bulunduğu veya toplandığı yer · hac törenlerinin yapıldığı yerler · eşi yanında bulunan kadın
  أصل يدل على حضور (maqayis)؛ شهده شهودا أي حضره (sihah)؛ الشهود والشهادة الحضور مع المشاهدة (mufradat)؛ المشهد مجمع الناس (ayn;tahdhib)؛ امرأة مشهد إذا حضر زوجها (maqayis;sihah;mufradat;tahdhib)
- **B002** bilgiye dayalı tanıklık — bilgiye dayalı kesin tanıklık sözü · bildiğini tanık olarak açıklamak · tanıklık eden kişi · tanık olan veya başkası hakkında tanıklık eden kişi · birinden tanıklık etmesini istemek · birini bir konuda tanık kılmak · ilahi nitelik olarak güvenilir tanık veya bilgisine hiçbir şey uzak kalmayan
  الشهادة يجمع الحضور والعلم والإعلام (maqayis)؛ الشهادة خبر قاطع (sihah)؛ شهد فلان بحق فهو شاهد وشهيد (tahdhib)؛ الشهادة قول صادر عن علم (mufradat)؛ شهد علي فلان بكذا شهادة وهو شاهد وشهيد (ayn)
- **B003** tanıklık bildirme sözü — tanıklık sözüyle yemin etmek veya bildirmek · namazda okunan tanıklık ve selamlama bölümü
  التشهد في الصلاة من قولك أشهد (ayn)؛ قولهم أشهد بكذا أي احلف (sihah)؛ أشهد أن لا إله إلا الله وأبين (tahdhib)؛ التشهد هو أن يقول أشهد أن لا إله إلا الله (mufradat)
- **B004** Tanrı yolunda öldürülen kişi — Tanrı yolunda öldürülen veya ölüm anında bulunan kişi · bu özel ölüm statüsüyle ölmek
  الشهيد القتيل في سبيل الله (maqayis;sihah)؛ استشهد فلان فهو شهيد (ayn;sihah;tahdhib)؛ الشهيد هو المحتضر (mufradat)؛ الشهيد الحي (tahdhib)
- **B005** ifade eden dil — dil veya sahibini belli eden ifade · ne görünüşü ne de dili var
  الشاهد اللسان (maqayis;sihah;tahdhib)؛ ما لفلان رواء ولا شاهد أي ماله منظر ولا لسان (tahdhib)؛ لفلان شاهد حسن أي عبارة جميلة (tahdhib)
- **B006** doğum ve erginlik belirtisi — doğumda çocuğun başıyla ya da çocukla birlikte çıkan şey · devenin doğurduğu yerde kalan kan veya zar izi · erkek çocuğun salgıyla, kız çocuğun adetle erginleşmesi · meni öncesi salgı çıkarmak
  الشهود ما يخرج على رأس الصبي (maqayis;ayn;tahdhib)؛ الشاهد الذي يخرج مع الولد (sihah)؛ شهود الناقة آثار موضع منتجها من دم أو سلى (maqayis;sihah)؛ أشهد الغلام إذا أمذى وأدرك وأشهدت الجارية إذا حاضت وأدركت (tahdhib)
- **B007** petekli bal — petek içindeki süzülmemiş bal · petekli baldan bir parça · petekli ballar
  الشَّهْد العسل في شمعها (maqayis;sihah)؛ الشهد العسل ما لم يعصر من شمعه (ayn;tahdhib)؛ الواحدة شهدة وشهدة والجمع شهاد (ayn;sihah;tahdhib)
- **B008** durumu gösteren belirti — geceye işaret eden yıldız · akşam namazı için kullanılan ad · atın üstünlüğünü ve iyi koştuğunu gösteren koşu
  الشاهد النجم (tahdhib)؛ صلاة الشاهد صلاة المغرب (tahdhib)؛ الشاهد من جريه ما يشهد له على سبقه وجودته (tahdhib)

===== _commentary/v16/out/s100/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 100:7, and ## Buluşmalar) =====
## Koşan at: soluk, adım, inceltilmiş beden

Sure, kim olduklarını adlarıyla değil, yalnızca yaptıklarıyla bildiren bir topluluk üzerine yeminle açılır: {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًا, tr:ve'l-âdiyâti dabhâ, gloss:soluk soluğa koşanlara andolsun, source:100:1}. Surenin hiçbir yerinde "at" kelimesi geçmez. Hayvan koşusundan, soluğundan, taşa vuran ayağından ve kaldırdığı tozdan tanınır. Kur'an başka yerlerde de yemini böyle açar: işiyle tanımlanan dişil çoğul bir topluluk getirir ve her yeni hareketi "fe" ile bir öncekinin hemen ardına bağlar. Bir örnek {ar:وَٱلصَّٰٓفَّٰتِ صَفًّا, tr:ve's-sâffâti saffâ, gloss:saf saf dizilenlere andolsun, source:37:1} ile {ar:فَٱلزَّٰجِرَٰتِ زَجْرًا, tr:fe'z-zâcirâti zecrâ, gloss:derken sürüp önlerine katanlara, source:37:2} çiftidir. Bir başkası {ar:وَٱلْمُرْسَلَٰتِ عُرْفًا, tr:ve'l-murselâti urfâ, gloss:ardı ardına gönderilenlere andolsun, source:77:1} ile {ar:فَٱلْعَٰصِفَٰتِ عَصْفًا, tr:fe'l-âsıfâti asfâ, gloss:derken fırtına gibi esenlere, source:77:2} çiftidir. Bu surede "fe" bağları koşuyu, kıvılcımı, sabahı, tozu ve kalabalığın ortasını tek bir hareketin ardışık aşamaları olarak dizer. Aşağıda bir kelimenin akrabalarından gelen görüntüler, o kelimenin ayetteki anlamının yanında duyulan ikinci bir ses olarak okunur. Bu görüntüler o anlamın yerine geçmez.

Birinci ayetin ilk kelimesinin kökü, koşunun en hızlısını adlandırır: {ar:العَدْو هو الحضر, tr:el-advu huve'l-hudr, gloss:adv dörtnala koşmaktır, source:"ع د و,B002"}. İyi ve çok koşan ata da aynı kökten bir sıfat verilir: {ar:يقال من عدو الفرس عدوان أي جيد العدو وكثيره, tr:yukâlu min advi'l-ferasi advân, ey ceyyidu'l-advi ve kesîruh, gloss:atın koşusundan "advân" denir, yani iyi ve çok koşan, source:"ع د و,B002"}. Ardından gelen kelime bu koşunun sesidir: {ar:صوت أنفاس الخيل إذا عدون وليس بصهيل ولا حمحمة, tr:savtu enfâsi'l-hayli izâ adevne ve leyse bi-sahîlin ve lâ hamhame, gloss:atların koşarken çıkardığı soluk sesi; ne kişneme ne homurtu, source:"ض ب ح,B001"}. Kişneme, hayvanın kendi sesidir. Burada duyulan ise zorlanan göğüsten dışarı itilen nefestir, yani kelime bir çabayı kulağa duyurur. Aynı kelime bir adım biçimini de adlandırır: {ar:ضبح الفرس وضبع إذا حرك ضبعيه في مشيه, tr:dabaha'l-ferasu ve daba'a izâ harreke dab'ayhi fî meşyih, gloss:at yürürken ön kollarını ileri atıp oynatınca "dabaha" denir, source:"ض ب ح,B002"}. Bu, {ar:هو عدو فوق التقريب وأصله ضبع, tr:huve advun fevka't-takrîbi ve asluhû dab', gloss:tırıştan hızlı bir koşudur, aslı "dab'"dır, source:"ض ب ح,B002"}. Böylece tek kelimede hem ileri uzanan ön ayaklar görülür hem de göğüsten çıkan nefes işitilir.

İkinci ayetin {ar:قَدْحًا, tr:kadhâ, gloss:çakarak, source:100:2} kelimesi ateşi anlatır. Ama bu kökün kalıplaşmış bir söyleyişi atın bedenini de gösterir: {ar:قدح الفرس تقديحا إذا ضمر حتى يصير مثل القدح, tr:kaddaha'l-ferasu takdîhan izâ damura hattâ yasîra misle'l-kıdh, gloss:at, ok çubuğu gibi oluncaya dek inceltildiğinde "kaddaha" denir, source:"ق د ح,B008"}. Koşu için yetiştirilen at fazlasından arındırılır ve gövdesi bir ok çubuğu kadar inceltilir. Beşinci ayetin {ar:جَمْعًا, tr:cem'â, gloss:bir topluluğu, source:100:5} kelimesinin yanında da aynı kökten bir at deyimi duyulur: {ar:استجمع الفرس جريا, tr:isteceme'a'l-ferasu cerye, gloss:at bütün koşusunu tek bir atılışta topladı, source:"ج م ع,B010"}.

Atın kökleri, insanı anlatan ayetlerde de geri gelir. Altıncı ayetteki {ar:ٱلْإِنسَٰنَ, tr:el-insân, gloss:insan, source:100:6} kelimesinin kökü, bineğin bir yanını adlandırır: {ar:إنسي الدابة للجانب الذي يلي الراكب, tr:insiyyu'd-dâbbeti li'l-cânibi'llezî yelî'r-râkib, gloss:hayvanın "insî" yanı, binicinin bulunduğu taraftır, source:"ء ن س,B004"}. Hayvanın bir yanı insana dönüktür ve insan onun sırtındadır. Yedinci ayetteki {ar:لَشَهِيدٌ, tr:le-şehîd, gloss:elbette tanıktır, source:100:7} kelimesinin kökünde ise atın koşusu kendi kendinin tanığıdır: {ar:الشاهد من جريه ما يشهد له على سبقه وجودته, tr:eş-şâhidu min caryihî mâ yeşhedu lehû alâ sebkıhî ve cevdetih, gloss:koşusunun "tanığı", öne geçtiğine ve iyi cins olduğuna tanıklık eden kısımdır, source:"ش ه د,B008"}. Sekizinci ayetteki {ar:لَشَدِيدٌ, tr:le-şedîd, gloss:pek düşkündür, source:100:8} kelimesinin kökü de koşunun adıdır: {ar:الشد العدو والفعل اشتد, tr:eş-şeddu'l-advu ve'l-fi'lu iştedde, gloss:"şedd" koşudur, fiili "iştedde"dir, source:"ش د د,B003"}. Bu söyleyiş "şedd"i birinci ayetin "adv"ıyla aynı tanımda birleştirir. Onuncu ayetin {ar:ٱلصُّدُورِ, tr:es-sudûr, gloss:göğüsler, source:100:10} kelimesinin kökünde de yarışı göğsüyle kazanan at vardır: {ar:صدر الفرس إذا جاء قد سبق بصدره, tr:sadera'l-ferasu izâ câe kad sebeka bi-sadrih, gloss:at göğsüyle öne geçerek gelince "sadera" denir, source:"ص د ر,B002"}.

Bu görüntü sureye bir karşılaştırma katar. At soluğunu, bacaklarını, inceltilmiş bedenini ve bütün koşusunu sahibinin işine verir. Koşusu öne geçtiğine tanıklık eder, yarışı göğsüyle kazanır. Hemen ardından insan gelir ve onun hakkında söylenen ilk şey, Rabbine karşı {ar:لَكَنُودٌ, tr:le-kenûd, gloss:pek nankördür, source:100:6} olmasıdır. Atın tanığı kendi lehinedir, insanın tanıklığı ise kendi nankörlüğü üzerinedir. Atın "şedd"i koşusudur, insanınki ise malı sevmesidir. Göğüs at için yarışın kazanıldığı yerdir, insan için ise içindekilerin ayıklanacağı yerdir.

Kur'an atları, sevilen malı ve Rab sözünü başka bir sahnede de bir araya getirir. Akşamüstü Süleyman'a soylu, çevik atlar sunulur: {ar:إِذْ عُرِضَ عَلَيْهِ بِٱلْعَشِىِّ ٱلصَّٰفِنَٰتُ ٱلْجِيَادُ, tr:iz uride aleyhi bi'l-aşiyyi's-sâfinâtu'l-ciyâd, gloss:akşamüstü ona durup bekleyen soylu atlar sunulduğunda, source:38:31}. Süleyman şöyle der: {ar:إِنِّىٓ أَحْبَبْتُ حُبَّ ٱلْخَيْرِ عَن ذِكْرِ رَبِّى, tr:innî ahbebtu hubbe'l-hayri an zikri rabbî, gloss:ben "hayır" sevgisini Rabbimin anılmasına bağlı olarak sevdim, source:38:32}. Arapçada "an" edatı hem "-den ötürü" hem "-den uzaklaşarak" anlamını taşıyabildiği için bu cümle iki yöne açıktır. Ama sözün devamı sabittir: {ar:حَتَّىٰ تَوَارَتْ بِٱلْحِجَابِ, tr:hattâ tevârat bi'l-hicâb, gloss:ta ki perdenin ardına gizleninceye dek, source:38:32}. Ardından {ar:رُدُّوهَا عَلَىَّ ۖ فَطَفِقَ مَسْحًا بِٱلسُّوقِ وَٱلْأَعْنَاقِ, tr:ruddûhâ aleyye, fe-tafika meshan bi's-sûkı ve'l-a'nâk, gloss:"Onları bana geri getirin" dedi ve bacaklarını, boyunlarını meshetmeye koyuldu, source:38:33}. Sekizinci ayetin "hubbu'l-hayr" ifadesi burada bir peygamberin ağzında, atlarla ve "Rabbim" sözüyle birlikte geçer. Bizim surede aynı ifade atların koşusundan hemen sonra, Rabbine nankör olan insanın bağlılığını adlandırır. Kur'an, insanlara süslü gösterilen sevgilerin listesine atları da koyar: {ar:زُيِّنَ لِلنَّاسِ حُبُّ ٱلشَّهَوَٰتِ, tr:zuyyine li'n-nâsi hubbu'ş-şehevât, gloss:arzulanan şeylerin sevgisi insanlara süslü gösterildi, source:3:14}. O listede altın ve gümüş yığınlarının yanında {ar:وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ, tr:ve'l-hayli'l-musevveme, gloss:salma, damgalı atlar, source:3:14} de sayılır. Böylece at hem koşan bir hayvan hem de sevilen bir maldır. Surenin karşılaştırması bu iki yüzün arasında kurulur.

Kaynaklar: 100:1 ٱلْعَٰدِيَٰتِ ع د و B002; 100:1 ضَبْحًا ض ب ح B001; 100:1 ضَبْحًا ض ب ح B002; 100:2 قَدْحًا ق د ح B008; 100:5 جَمْعًا ج م ع B010; 100:6 ٱلْإِنسَٰنَ ء ن س B004; 100:7 لَشَهِيدٌ ش ه د B008; 100:8 لَشَدِيدٌ ش د د B003; 100:10 ٱلصُّدُورِ ص د ر B002; 37:1; 37:2; 77:1; 77:2; 38:31; 38:32; 38:33; 3:14

## Yetiştiren Rab, kesilen şükür, bitirmeyen toprak

Altıncı ayet yeminin cevabıdır: {ar:إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌ, tr:inne'l-insâne li-rabbihî le-kenûd, gloss:şüphesiz insan Rabbine karşı pek nankördür, source:100:6}. Cümlede "Rabbine" kelimesi nitelikten önce gelir. Böylece nankörlüğün kime karşı olduğu, nankörlüğün kendisinden önce duyulur. "Rab" kelimesi önce sahibi adlandırır: {ar:ورب كل شيء مالكه, tr:ve rabbu kulli şey'in mâlikuh, gloss:her şeyin rabbi onun sahibidir, source:"ر ب ب,B001"}. Aynı kelime sözü dinlenen efendiyi ve bir şeyi düzeltip iyileştireni de anlatır: {ar:يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح, tr:yekûnu'r-rabbu'l-mâlik, ve yekûnu'r-rabbu's-seyyide'l-mutâ', ve yekûnu'r-rabbu'l-muslih, gloss:rab sahip olur, itaat edilen efendi olur, ıslah eden olur, source:"ر ب ب,B001"}. Kökün işleyişi bir yetiştirmedir: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi halden hale geçirerek tamamlanma sınırına kadar oluşturmaktır, source:"ر ب ب,B002"}. Verilen bir iyilik de bu kökle tamamlanır: {ar:رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها, tr:rabbe'r-raculu'n-ni'mete yerubbuhâ rabben ve rabâbeten izâ temmemehâ, gloss:adam bir nimeti tamamladığında "rabbe" denir, source:"ر ب ب,B002"}. Kökün ailesinde bir bulut da vardır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâbu's-sehâb, summiye bi-zâlike li-ennehû yerubbu'n-nebât, gloss:"rabâb" buluttur; bitkiyi yetiştirdiği için bu adı almıştır, source:"ر ب ب,B008"}. Bir yerde toplanan bol su da aynı köktendir: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabab, ve huve'l-mâu'l-kesîr, summiye bi-zâlike li-ictimâ'ih, gloss:"rabab" bol sudur; toplandığı için bu adı almıştır, source:"ر ب ب,B013"}.

"Kenûd" kelimesi bu bakıma verilen karşılığı bir ip görüntüsüyle anlatır: {ar:كند الحبل يكنده كندا, tr:kenede'l-hable yeknuduhû kenden, gloss:ipi kesti, source:"ك ن د,B001"}. Şükrün kesilmesi de bu kelimeyle söylenir: {ar:يكند الشكر أي يقطعه, tr:yeknudu'ş-şukra, ey yakta'uh, gloss:şükrü "kened" eder, yani keser, source:"ك ن د,B001"}. Veren ile alan arasında bir ip uzanır. İyilik o ipten bir yöne akar, şükür öbür yöne döner. Kenûd olan kişi ipi kendi ucundan keser. Kelime bu kesişin nasıl işlediğini de anlatır: {ar:الكنود الكفور للنعمة, tr:el-kenûdu'l-kefûru li'n-ni'me, gloss:kenûd, nimete nankörlük edendir, source:"ك ن د,B002"}. Kenûd olan kişi {ar:يعد المصائب وينسى النعم, tr:ye'uddu'l-mesâibe ve yense'n-ni'am, gloss:musibetleri sayar, nimetleri unutur, source:"ك ن د,B002"}. Kelime bağı sürdürmemeyi de adlandırır: {ar:امرأة كند وكنود أي كفور للمواصلة, tr:imraetun kundun ve kenûd, ey kefûrun li'l-muvâsala, gloss:"kund" ya da "kenûd" kadın, yakınlığa nankörlük eden, bağı sürdürmeyendir, source:"ك ن د,B002"}. Kelimenin topraktaki karşılığı ise şudur: {ar:أرض كنود لا تنبت شيئا, tr:ardun kenûdun lâ tunbitu şey'â, gloss:kenûd toprak, hiçbir şey bitirmeyen topraktır, source:"ك ن د,B003"}.

Toprak görüntüsünü surenin başka kelimeleri tamamlar. Dördüncü ayetin fiili bulutu kaldıran rüzgârda da toprağı süren elde de kullanılır: {ar:فتثير سحابا... وأثاروا الأرض, tr:fe-tusîru sehâben... ve esârû'l-ard, gloss:bulutu kaldırır... toprağı sürdüler, source:"ث و ر,B002"}. "Nak'", sel suyunun durup toplandığı yerdir: {ar:نقع الماء في منقعة السيل اجتمع فيها وطال مكثه, tr:neka'a'l-mâu fî menka'ati's-seyl, ictema'a fîhâ ve tâle muksuh, gloss:su, selin göllendiği yerde toplandı ve uzun süre kaldı, source:"ن ق ع,B001"}. "Nak'" aynı zamanda iyi topraktır: {ar:النقاع واحدها نقع وهي الأرض الحرة الطين الطيبة التي لا حزونة فيها ولا ارتفاع ولا انهباط, tr:en-nikâ'u vâhiduhâ nak', ve hiye'l-ardu'l-hurratu't-tîni't-tayyibetu'lletî lâ huzûnete fîhâ ve lâ irtifâ'a ve lâ inhibât, gloss:"nikâ'" (tekili "nak'"), sertliği, tümseği, çukuru olmayan, saf ve iyi balçıklı topraktır, source:"ن ق ع,B007"}. Surenin son kelimesinin ailesinde de yağmur suyunu toplayan alçak toprak vardır: {ar:الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء, tr:el-habrâu'l-ardu's-sehletu'l-munhafidatu yectemi'u fîhâ mâu's-semâ', gloss:"habrâ", gökten inen suyun toplandığı yumuşak, alçak topraktır, source:"خ ب ر,B002"}. Aynı ailede toprağı işleyen de vardır: {ar:الخبير الأكار, tr:el-habîru'l-ekkâr, gloss:"habîr", çiftçidir, source:"خ ب ر,B003"}. Sekizinci ayetteki sevgi kelimesinin yanında, toprağın vermesi beklenen tane durur: {ar:الحب والحبة في الحنطة والشعير, tr:el-habbu ve'l-habbetu fi'l-hıntati ve'ş-şa'îr, gloss:buğday ve arpada tane, source:"ح ب ب,B001"}. Yemin cümlesi böylece bir tarla sahnesi kurar. Bulut bitkiyi yetiştirir, rüzgâr bulutu kaldırır, su alçak toprakta toplanır, iyi balçık suyu tutar ve çiftçi toprağı işler. Bütün bu bakıma karşın kenûd toprak hiçbir şey bitirmez. Düz bir anlatım "insan nankördür" demekle yetinirdi. Görüntü ise nankörlüğün neye karşı olduğunu gösterir: adım adım yetiştirmeye, tamamlanmış bir iyiliğe, yağmura.

Sekizinci ayetteki "hayr" kelimesinin bir yüzü de bu bakımın ta kendisidir: {ar:الخير الهبة, tr:el-hayru'l-hibe, gloss:hayır, bağıştır, source:"خ ي ر,B005"}. Kelime cömertlik de demektir: {ar:والخير الكرم, tr:ve'l-hayru'l-kerem, gloss:hayır, cömertliktir, source:"خ ي ر,B005"}. İnsan bağışa şiddetle düşkündür ama bağışı vereni unutur. Yedinci ayet bu nankörlüğün tanığını getirir: {ar:وَإِنَّهُۥ عَلَىٰ ذَٰلِكَ لَشَهِيدٌ, tr:ve innehû alâ zâlike le-şehîd, gloss:ve şüphesiz o buna tanıktır, source:100:7}. Tanıklık bilgiye dayanan sözdür: {ar:الشهادة قول صادر عن علم, tr:eş-şehâdetu kavlun sâdirun an ilm, gloss:şahitlik, bilgiden kaynaklanan sözdür, source:"ش ه د,B002"}. Ayetteki zamir bir önceki cümlede anılan insana da Rabbine de dönebilecek konumdadır. Hangisine dönerse dönsün, tanıklık aynı şeyin, kesilen ipin üzerindedir. On birinci ayet aynı Rabbi bir kez daha anar, ama bu kez çoğul bir zamirle: {ar:إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍ لَّخَبِيرٌ, tr:inne rabbehum bihim yevme'izin le-habîr, gloss:şüphesiz Rableri o gün onlardan tamamen haberdardır, source:100:11}. İpi kesenler O'nun bilgisinin dışına çıkmış olmazlar.

Kur'an bu toprak sahnesini açıkça kurar. Allah rüzgârları rahmetinin önünde müjdeci olarak gönderir, ağır bulutları ölü bir toprağa sürer, oraya su indirir ve her türlü ürünü çıkarır. Sonra şöyle der: {ar:وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ ۖ وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًا ۚ كَذَٰلِكَ نُصَرِّفُ ٱلْءَايَٰتِ لِقَوْمٍ يَشْكُرُونَ, tr:ve'l-beledu't-tayyibu yahrucu nebâtuhû bi-izni rabbih, ve'llezî habuse lâ yahrucu illâ nekidâ, kezâlike nusarrifu'l-âyâti li-kavmin yeşkurûn, gloss:iyi toprağın bitkisi Rabbinin izniyle çıkar; kötü olanınki ise ancak kıt ve cılız çıkar; şükreden bir kavim için ayetleri böyle çeşitli biçimlerde açıklarız, source:7:58}. Toprak, onun Rabbi, kıt ürün ve şükür tek bir ayette bir aradadır. Rüzgârın bulutu kaldırması da bizim dördüncü ayetin fiiliyle anlatılır: {ar:ٱللَّهُ ٱلَّذِى يُرْسِلُ ٱلرِّيَٰحَ فَتُثِيرُ سَحَابًا, tr:Allâhu'llezî yursilu'r-riyâha fe-tusîru sehâben, gloss:Allah, rüzgârları gönderen ve onların bulutu kaldırdığı kimsedir, source:30:48}. İnsanın nankörlüğü Kur'an'da sayma üzerinden de anlatılır: {ar:وَإِن تَعُدُّوا۟ نِعْمَتَ ٱللَّهِ لَا تُحْصُوهَآ ۗ إِنَّ ٱلْإِنسَٰنَ لَظَلُومٌ كَفَّارٌ, tr:ve in teuddû ni'meta'llâhi lâ tuhsûhâ, inne'l-insâne le-zalûmun keffâr, gloss:Allah'ın nimetini saymaya kalksanız sayamazsınız; şüphesiz insan çok zalim, çok nankördür, source:14:34}. Kenûd musibetleri sayıp nimetleri unutur. Bu ayet ise sayılmaya kalkılsa tükenmeyecek olanın nimet olduğunu söyler. Denizde sıkışan insanlar yalnız O'na yalvarır, sonra: {ar:فَلَمَّا نَجَّىٰكُمْ إِلَى ٱلْبَرِّ أَعْرَضْتُمْ ۚ وَكَانَ ٱلْإِنسَٰنُ كَفُورًا, tr:fe-lemmâ neccâkum ile'l-berri a'radtum, ve kâne'l-insânu kefûrâ, gloss:sizi karaya çıkarıp kurtarınca yüz çevirdiniz; insan pek nankördür, source:17:67}. Başka bir yerde de {ar:كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ, tr:kellâ inne'l-insâne le-yatğâ, gloss:hayır, insan gerçekten azar, source:96:6} ve {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en reâhu'steğnâ, gloss:kendini kimseye muhtaç görmediğinde, source:96:7} denir. İnsana Rabbinin adıyla yöneltilen soru da aynı iki kelimeyi yan yana koyar: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ مَا غَرَّكَ بِرَبِّكَ ٱلْكَرِيمِ, tr:yâ eyyuhe'l-insânu mâ ğarrake bi-rabbike'l-kerîm, gloss:ey insan, seni o cömert Rabbine karşı ne aldattı, source:82:6}. Yol gösterildikten sonra iki seçenek bırakılır: {ar:إِمَّا شَاكِرًا وَإِمَّا كَفُورًا, tr:immâ şâkiran ve immâ kefûrâ, gloss:ya şükreden ya da nankör olarak, source:76:3}. Tanıklık ile Rab sözü de en baştaki bir sahnede bir araya gelir. Rabbin Âdem oğullarının sırtlarından soylarını aldığı anlatılır ve şöyle denir: {ar:وَأَشْهَدَهُمْ عَلَىٰٓ أَنفُسِهِمْ أَلَسْتُ بِرَبِّكُمْ ۖ قَالُوا۟ بَلَىٰ ۛ شَهِدْنَآ, tr:ve eşhedehum alâ enfusihim e-lestu bi-rabbikum, kâlû belâ şehidnâ, gloss:onları kendilerine karşı tanık tuttu: "Ben sizin Rabbiniz değil miyim?" "Evet, tanık olduk" dediler, source:7:172}.

Kaynaklar: 100:6 لِرَبِّهِۦ ر ب ب B001; 100:6 لِرَبِّهِۦ ر ب ب B002; 100:6 لِرَبِّهِۦ ر ب ب B008; 100:6 لِرَبِّهِۦ ر ب ب B013; 100:6 لَكَنُودٌ ك ن د B001; 100:6 لَكَنُودٌ ك ن د B002; 100:6 لَكَنُودٌ ك ن د B003; 100:4 فَأَثَرْنَ ث و ر B002; 100:4 نَقْعًا ن ق ع B001; 100:4 نَقْعًا ن ق ع B007; 100:11 لَّخَبِيرٌ خ ب ر B002; 100:11 لَّخَبِيرٌ خ ب ر B003; 100:8 لِحُبِّ ح ب ب B001; 100:8 ٱلْخَيْرِ خ ي ر B005; 100:7 لَشَهِيدٌ ش ه د B002; 100:11 رَبَّهُم ر ب ب B001; 7:58; 30:48; 14:34; 17:67; 96:6; 96:7; 82:6; 76:3; 7:172

## Toplanmış kalabalık ve toplanma günü

Beşinci ayetin {ar:جَمْعًا, tr:cem'â, gloss:bir topluluğu, source:100:5} kelimesi baskına uğrayan kalabalıktır: {ar:الجمع اسم لجماعة الناس, tr:el-cem'u ismun li-cemâ'ati'n-nâs, gloss:"cem'", insan topluluğunun adıdır, source:"ج م ع,B002"}. Aynı kök insanların toplandığı yeri ve günü de adlandırır: {ar:المجمع حيث يجمع الناس, tr:el-mecma'u haysu yucma'u'n-nâs, gloss:"mecma'", insanların toplandığı yerdir, source:"ج م ع,B004"}. Bu yerin ve günün en büyüğü de bu kökle anılır: {ar:يوم الجمع ويوم يجمعكم ليوم الجمع, tr:yevmu'l-cem'i ve yevme yecme'ukum li-yevmi'l-cem', gloss:"toplanma günü" ve "sizi toplanma günü için toplayacağı gün", source:"ج م ع,B004"}. Beşinci ayetin fiili, bir şeyin iki kenarı arasında kalan yeri adlandıran bir köke dayanır: {ar:اسما لما بين طرفي كل شيء, tr:isman li-mâ beyne tarafey kulli şey', gloss:her şeyin iki ucu arasındakinin adı, source:"و س ط,B002"}. Atlar kalabalığın iki kenarı arasında, tam ortasında durur. Yedinci ayetin tanık kelimesinin kökü de bir toplanma yerinin adıdır: {ar:المشهد مجمع الناس, tr:el-meşhedu mecma'u'n-nâs, gloss:"meşhed", insanların toplandığı yerdir, source:"ش ه د,B001"}. Fiil hazır bulunmayı anlatır: {ar:شهده شهودا أي حضره, tr:şehidehû şuhûden, ey hadarah, gloss:"şehidehû", yani orada hazır bulundu, source:"ش ه د,B001"}. Onuncu ayetin fiili de bir toplamadır: {ar:أصل واحد منقاس وهو جمع الشيء, tr:aslun vâhidun munkâs, ve huve cem'u'ş-şey', gloss:tek ve kuralı işleyen bir köktür; bir şeyi toplamaktır, source:"ح ص ل,B001"}. On birinci ayetteki {ar:يَوْمَئِذٍ, tr:yevme'izin, gloss:o gün, source:100:11} ise bütün bunları bir güne bağlar.

Bu görüntünün sureye kattığı şey bir ölçek değişimidir. Beşinci ayette atlar bir obanın, belki birkaç çadırlık bir halkın ortasına dalar. Surenin sonundaki gün ise bütün insanların toplandığı gündür. Önce bir kalabalık şaşkınlıkla yakalanır, sonra herkes bir araya getirilir. Düz bir anlatım baskının yalnızca bir savaş sahnesi olduğunu söylerdi. Kökler ise aynı kelimeyi o büyük toplanmaya doğru açık tutar.

Kur'an bu toplanmayı beşinci ayetin kelimesiyle, aynı biçimde anlatır. Bir seddin yerle bir edileceği vaadinin ardından şöyle denir: {ar:وَنُفِخَ فِى ٱلصُّورِ فَجَمَعْنَٰهُمْ جَمْعًا, tr:ve nufiha fi's-sûri fe-cema'nâhum cem'â, gloss:sura üfürüldü ve onları hep birlikte topladık, source:18:99}. Yok edilen kavimlerin hikâyeleri anlatıldıktan sonra da o gün iki kökle birden anılır: {ar:ذَٰلِكَ يَوْمٌ مَّجْمُوعٌ لَّهُ ٱلنَّاسُ وَذَٰلِكَ يَوْمٌ مَّشْهُودٌ, tr:zâlike yevmun mecmû'un lehu'n-nâsu ve zâlike yevmun meşhûd, gloss:o, insanların kendisi için toplandığı bir gündür; o, herkesin hazır bulunduğu bir gündür, source:11:103}. Bu ayette beşinci ayetin kökü ile yedinci ayetin kökü yan yana durur. O günün adı da verilir: {ar:يَوْمَ يَجْمَعُكُمْ لِيَوْمِ ٱلْجَمْعِ ۖ ذَٰلِكَ يَوْمُ ٱلتَّغَابُنِ, tr:yevme yecme'ukum li-yevmi'l-cem', zâlike yevmu't-teğâbun, gloss:sizi toplanma günü için toplayacağı gün; o, kazancın ve kaybın ortaya çıktığı gündür, source:64:9}. Toplanmanın nasıl olacağı da anlatılır: {ar:وَنُفِخَ فِى ٱلصُّورِ فَإِذَا هُم مِّنَ ٱلْأَجْدَاثِ إِلَىٰ رَبِّهِمْ يَنسِلُونَ, tr:ve nufiha fi's-sûri fe-izâ hum mine'l-ecdâsi ilâ rabbihim yensilûn, gloss:sura üfürülür ve onlar kabirlerinden Rablerine doğru akın akın koşarlar, source:36:51}. Bu ayette de "Rableri" kelimesi geçer, tıpkı on birinci ayette olduğu gibi. Toplanış tek bir sesle tamamlanır: {ar:إِن كَانَتْ إِلَّا صَيْحَةً وَٰحِدَةً فَإِذَا هُمْ جَمِيعٌ لَّدَيْنَا مُحْضَرُونَ, tr:in kânet illâ sayhaten vâhideten fe-izâ hum cemî'un ledeynâ muhdarûn, gloss:yalnızca tek bir çığlık olur ve hepsi birden huzurumuza getirilir, source:36:53}.

Kaynaklar: 100:5 جَمْعًا ج م ع B002; 100:5 جَمْعًا ج م ع B004; 100:5 فَوَسَطْنَ و س ط B002; 100:7 لَشَهِيدٌ ش ه د B001; 100:10 وَحُصِّلَ ح ص ل B001; 18:99; 11:103; 64:9; 36:51; 36:53

## Görmek, bilmek, içini bilmek

Surenin ikinci yarısı üç bilme biçimini sırayla dizer. Yedinci ayette insan tanıktır, dokuzuncu ayette bilip bilmediği sorulur, on birinci ayette ise Rabbinin onlardan haberdar olduğu söylenir. Tanıklığın kökü hazır bulunmak ve görmektir: {ar:الشهود والشهادة الحضور مع المشاهدة, tr:eş-şuhûdu ve'ş-şehâdetu'l-huzûru me'a'l-muşâhede, gloss:"şuhûd" ve "şehâdet", görerek hazır bulunmaktır, source:"ش ه د,B001"}. Tanıklık üç şeyi bir arada tutar: {ar:الشهادة يجمع الحضور والعلم والإعلام, tr:eş-şehâdetu yecma'u'l-huzûra ve'l-ilme ve'l-i'lâm, gloss:şahitlik, hazır bulunmayı, bilmeyi ve bildirmeyi bir araya getirir, source:"ش ه د,B002"}. Tanıklık aynı zamanda bir haberdir: {ar:الشهادة خبر قاطع, tr:eş-şehâdetu haberun kâtı', gloss:şahitlik kesin bir haberdir, source:"ش ه د,B002"}. Kökün ailesinde tanığın aleti de vardır: {ar:الشاهد اللسان, tr:eş-şâhidu'l-lisân, gloss:"şâhid", dildir, source:"ش ه د,B005"}. Dokuzuncu ayetin bilme fiili ise bir şeyi gerçeğiyle kavramaktır: {ar:إدراك الشيء بحقيقته, tr:idrâku'ş-şey'i bi-hakîkatih, gloss:bir şeyi hakikatiyle kavramak, source:"ع ل م,B001"}. Bu fiil de haberle bağlantılıdır: {ar:ما علمت بخبرك أي ما شعرت به, tr:mâ alimtu bi-haberik, ey mâ şa'artu bih, gloss:"haberini bilmedim", yani farkına varmadım, source:"ع ل م,B001"}. Son ayetin kelimesi bu iki bilgiyi bir araya getirir: {ar:الخبير العالم, tr:el-habîru'l-âlim, gloss:"habîr", bilendir, source:"خ ب ر,B001"}.Bu bilgi deneyerek kazanılır: {ar:الخبرة الاختبار, tr:el-hibratu'l-ihtibâr, gloss:"hibre", sınayarak denemektir, source:"خ ب ر,B001"}. Ulaştığı yer de işin iç yüzüdür: {ar:الخبرة المعرفة ببواطن الأمر, tr:el-hibratu'l-ma'rifetu bi-bevâtıni'l-emr, gloss:"hibre", işin iç yüzünü bilmektir, source:"خ ب ر,B001"}. Altıncı ayetteki insan kelimesinin kökü de bu sıralamanın başına bir duyu ekler: {ar:آنست الشيء إذا رأيته وآنسته إذا سمعته, tr:ânestu'ş-şey'e izâ raeytehû ve ânestuhû izâ semi'teh, gloss:bir şeyi gördüğünde de işittiğinde de "ânestu" dersin, source:"ء ن س,B002"}. Kök görmekten bilmeye kadar uzanır: {ar:آنست منه رشدا علمته, tr:ânestu minhu ruşden, alimtuh, gloss:"ondan bir olgunluk sezdim", yani onu öğrendim, source:"ء ن س,B002"}. Su başı deyimi de aynı yolu izler. Çok göletten içen kişi, işleri deneye deneye {ar:حتى خبرها, tr:hattâ haberahâ, gloss:sonunda iç yüzlerini öğrendi, source:"ن ق ع,B008"} diye anılır.

Bu yolun sure içinde aldığı biçim şöyledir. Yedinci ayette insan hazırdır ve görmektedir. Kendi nankörlüğüne tanıktır, yani bilgisi gözünün önündedir. Dokuzuncu ayet buna rağmen bir soru sorar: {ar:أَفَلَا يَعْلَمُ, tr:e-fe-lâ ya'lem, gloss:bilmez mi, source:100:9}. Bu soru, görmekle bilmek arasındaki boşluğu açığa çıkarır. İnsan kendi halini görür ama bu halin nereye varacağını hakikatiyle kavramaz. Sure soruya cevap vermez. Cevabın yerine Rabbin bilgisini koyar: {ar:إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍ لَّخَبِيرٌ, tr:inne rabbehum bihim yevme'izin le-habîr, gloss:şüphesiz Rableri o gün onlardan tamamen haberdardır, source:100:11}. Ayet "yaptıklarından" demez, "onlardan" der. Bilginin konusu insanın kendisidir. "Habîr" kelimesi görünüşe değil iç yüze bakar. Böylece surenin bilgi sırası, insanın kendi dışını görmesinden Rabbin onun içini bilmesine doğru ilerler.

Kur'an aynı kuruluşu bir başka surede de kullanır. Allah sözü gizlenen ile açığa vurulanı bir tutar: {ar:وَأَسِرُّوا۟ قَوْلَكُمْ أَوِ ٱجْهَرُوا۟ بِهِۦٓ ۖ إِنَّهُۥ عَلِيمٌ بِذَاتِ ٱلصُّدُورِ, tr:ve esirrû kavlekum evi'cherû bih, innehû alîmun bi-zâti's-sudûr, gloss:sözünüzü gizleyin ya da açığa vurun; O, göğüslerin içindekini bilendir, source:67:13}. Ardından bir soru gelir: {ar:أَلَا يَعْلَمُ مَنْ خَلَقَ وَهُوَ ٱللَّطِيفُ ٱلْخَبِيرُ, tr:e-lâ ya'lemu men halak, ve huve'l-latîfu'l-habîr, gloss:yaratan bilmez mi? O, en ince şeyi bilen ve her şeyden haberdar olandır, source:67:14}. Göğüsler, "bilmez mi" sorusu ve "habîr" bu iki ayette de bu sırayla dizilir. Ancak soru orada yaratanın bilgisi üzerine sorulur, bizim surede ise insanın bilgisi üzerine. Bir başka yerde insan kendi kendisinin tanığıdır: {ar:يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍ بِمَا قَدَّمَ وَأَخَّرَ, tr:yunebbeu'l-insânu yevme'izin bimâ kaddeme ve ahhar, gloss:o gün insana öne sürdüğü ve geride bıraktığı bildirilir, source:75:13}; {ar:بَلِ ٱلْإِنسَٰنُ عَلَىٰ نَفْسِهِۦ بَصِيرَةٌ, tr:beli'l-insânu alâ nefsihî basîra, gloss:aslında insan kendi kendine karşı bir göz, bir tanıktır, source:75:14}; {ar:وَلَوْ أَلْقَىٰ مَعَاذِيرَهُۥ, tr:ve lev elkâ meâzîreh, gloss:mazeretlerini ortaya dökse bile, source:75:15}. Kökün "dil" anlamı da o günün tanıklığında yer alır: {ar:يَوْمَ تَشْهَدُ عَلَيْهِمْ أَلْسِنَتُهُمْ وَأَيْدِيهِمْ وَأَرْجُلُهُم بِمَا كَانُوا۟ يَعْمَلُونَ, tr:yevme teşhedu aleyhim elsinetuhum ve eydîhim ve erculuhum bimâ kânû ya'melûn, gloss:o gün dilleri, elleri ve ayakları yaptıklarına dair aleyhlerine tanıklık eder, source:24:24}. Bedenin kendi derisine sorduğu soru da kaydedilir: {ar:وَقَالُوا۟ لِجُلُودِهِمْ لِمَ شَهِدتُّمْ عَلَيْنَا ۖ قَالُوٓا۟ أَنطَقَنَا ٱللَّهُ ٱلَّذِىٓ أَنطَقَ كُلَّ شَىْءٍ, tr:ve kâlû li-culûdihim lime şehidtum aleynâ, kâlû entakanâ'llâhu'llezî entaka kulle şey', gloss:derilerine "neden aleyhimize tanıklık ettiniz" derler; onlar da "her şeyi konuşturan Allah bizi konuşturdu" der, source:41:21}. İnsanın içine dair bilgi en yakın yerden gelir: {ar:وَلَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ وَنَعْلَمُ مَا تُوَسْوِسُ بِهِۦ نَفْسُهُۥ ۖ وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ, tr:ve le-kad halakna'l-insâne ve na'lemu mâ tuvesvisu bihî nefsuh, ve nahnu akrabu ileyhi min habli'l-verîd, gloss:insanı biz yarattık ve nefsinin ona ne fısıldadığını biliriz; biz ona şah damarından daha yakınız, source:50:16}. Görünüşte iman edip sıkıntı gelince dönen kişi için de şu sorulur: {ar:أَوَلَيْسَ ٱللَّهُ بِأَعْلَمَ بِمَا فِى صُدُورِ ٱلْعَٰلَمِينَ, tr:e-ve-leysa'llâhu bi-a'leme bimâ fî sudûri'l-âlemîn, gloss:Allah, âlemlerin göğüslerinde olanı en iyi bilen değil midir, source:29:10}. Yerin kendisi de o gün bir haberci olur: {ar:يَوْمَئِذٍ تُحَدِّثُ أَخْبَارَهَا, tr:yevme'izin tuhaddisu ahbârahâ, gloss:o gün yer haberlerini anlatır, source:99:4}. Haberlerini anlatan bu yer, kabirleri altüst edilen yerdir. "Ahbâr" kelimesi de surenin son kelimesiyle aynı köktendir.

Kaynaklar: 100:7 لَشَهِيدٌ ش ه د B001; 100:7 لَشَهِيدٌ ش ه د B002; 100:7 لَشَهِيدٌ ش ه د B005; 100:9 يَعْلَمُ ع ل م B001; 100:11 لَّخَبِيرٌ خ ب ر B001; 100:6 ٱلْإِنسَٰنَ ء ن س B002; 100:4 نَقْعًا ن ق ع B008; 67:13; 67:14; 75:13; 75:14; 75:15; 24:24; 41:21; 50:16; 29:10; 99:4

## Buluşmalar

İlk buluşma, surenin açılış sahnesinde koşan at ile şafak baskını arasındadır. Koşanların tanımı zaten baskın yapanlardır: {ar:العادية الخيل المغيرة, tr:el-âdiyetu'l-haylu'l-muğîra, gloss:"âdiye", baskın yapan atlardır, source:"ع د و,B001"}. Sekizinci ayetin "şedd" kelimesi de iki görüntüyü aynı anda taşır. Bir yanda koşudur, öbür yanda düşmana saldırıdır: {ar:شد على العدو إذا حمل عليه, tr:şedde ale'l-aduvvi izâ hamele aleyh, gloss:düşmana saldırdığında "şedde" denir, source:"ش د د,B003"}. Aynı sahnede ateş görüntüsü de yer alır. Soluk soluğa koşan hayvanların ayakları taşlara çarparak kıvılcım çıkarır. Birinci ayetin kelimesi bir yandan bu soluğu, bir yandan da yanmış çakmak taşını adlandırır. Koşu, kıvılcım ve sabah tek bir hareketin ardışık parçalarıdır.

Surenin iki yarısını birbirine bağlayan asıl buluşma, dördüncü ayetin tozu ile dokuzuncu ayetin kabirleri arasındadır. Toynakların toprağı kaldırması ile kabirlerin altüst edilmesi aynı fiille açıklanır: "bu'sira", "usîra" demektir. Böylece surenin ilk yarısındaki sabah baskını, ikinci yarısındaki altüst oluşun bir ön provası olur. Kur'an da kabirlerden çıkışı bir koşu olarak anlatır: {ar:يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًا كَأَنَّهُمْ إِلَىٰ نُصُبٍ يُوفِضُونَ, tr:yevme yahrucûne mine'l-ecdâsi sirâ'an ke-ennehum ilâ nusubin yûfidûn, gloss:kabirlerden hızla çıkacakları, sanki dikili bir hedefe koşuyorlarmış gibi seğirtecekleri gün, source:70:43}. Bir başka yerde de {ar:يَوْمَ تَشَقَّقُ ٱلْأَرْضُ عَنْهُمْ سِرَاعًا, tr:yevme teşakkaku'l-ardu anhum sirâ'â, gloss:yerin yarılıp onların hızla çıktığı gün, source:50:44} denir. Surenin başında koşanlar atlardır. Sonunda ise koşanlar kabirlerden çıkan insanlardır. Bu insanların gittiği yer de beşinci ayetteki gibi bir topluluğun ortasıdır, ama bu kez bütün insanların toplandığı yerdir.

Ateş ile kabir de aynı kökte buluşur. İkinci ayetin "ateşi çıkarmak" fiili ile gömmenin "örtmek" fiili aynı köktendir. Kur'an ateşi dirilişe delil olarak da kullanır. Çakılan ateşe dair soru dirilişi inkâr edenlere sorulur. Yeşil ağaçtan çıkan ateş de çürümüş kemikleri kimin dirilteceğini soran kişiye verilen cevaptır. Tahtanın içinde gizli duran ateş çakılınca dışarı çıkar, toprağın içinde gizli duran insan da altüst edilince dışarı çıkar. Yağmur sahnesi de aynı yere varır. İyi toprak ile kıt ürün veren toprağı karşılaştıran ayetten hemen önce şöyle denir: {ar:كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:kezâlike nuhrici'l-mevtâ le'allekum tezekkerûn, gloss:ölüleri de böyle çıkarırız; belki düşünüp öğüt alırsınız, source:7:57}. Kenûd toprak bitki bitirmez. Ama sonunda kabirleri altüst edilecek olan da aynı topraktır.

Biriktirilen mal ile göğsün ayıklanması da bir sahnede buluşur. Onuncu ayetin fiilinin aslı, altını maden toprağından ayırmaktır. Biriktirenin malı ise toplanmış altın ve gümüştür. Kur'an bu iki şeyi ateşte birleştirir: {ar:وَٱلَّذِينَ يَكْنِزُونَ ٱلذَّهَبَ وَٱلْفِضَّةَ وَلَا يُنفِقُونَهَا فِى سَبِيلِ ٱللَّهِ, tr:ve'llezîne yeknizûne'z-zehebe ve'l-fiddate ve lâ yunfikûnehâ fî sebîli'llâh, gloss:altın ve gümüşü yığıp Allah yolunda harcamayanlar, source:9:34}; {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhuhum ve cunûbuhum ve zuhûruhum, gloss:o gün bunlar cehennem ateşinde kızdırılır ve alınları, yanları ve sırtları onlarla dağlanır, source:9:35}. Malın bağlılığı ile göğsün içindekinin çıkarılması da tek bir ayette bir aradadır: {ar:إِن يَسْـَٔلْكُمُوهَا فَيُحْفِكُمْ تَبْخَلُوا۟ وَيُخْرِجْ أَضْغَٰنَكُمْ, tr:in yes'elkumûhâ fe-yuhfikum tebhalû ve yuhric adğânekum, gloss:onları (mallarınızı) sizden isteyip ısrar etseydi cimrilik ederdiniz ve O da kinlerinizi dışarı çıkarırdı, source:47:37}. Sevgi kelimesinin "kalbin tanesi" anlamı da bu buluşmayı kelimenin içinden kurar. İnsanın şiddetle bağlandığı mal göğsün içindeki tanedir, harman savrulduğunda ayrılacak olan da odur. Beşinci ayetin kökü de aynı sahnede iki yönde işler. Mal toplayan, yumruğunu sıkan kişi sonunda toplanma gününde toplananlardan biri olur. Onuncu ayetin fiili de bir toplamadır.

Sabah baskını ile malı esirgeme de bir Kur'an sahnesinde birleşir. Bir bahçenin sahipleri ürünü sabahleyin devşireceklerine yemin ederler: {ar:إِذْ أَقْسَمُوا۟ لَيَصْرِمُنَّهَا مُصْبِحِينَ, tr:iz aksemû le-yasrimunnehâ musbihîn, gloss:onu sabaha girerken mutlaka devşireceklerine yemin ettiklerinde, source:68:17}. Onlar uyurken {ar:فَطَافَ عَلَيْهَا طَآئِفٌ مِّن رَّبِّكَ وَهُمْ نَآئِمُونَ, tr:fe-tâfe aleyhâ tâifun min rabbike ve hum nâimûn, gloss:onlar uykudayken Rabbinden bir bela bahçeyi sardı, source:68:19}. Bahçe {ar:فَأَصْبَحَتْ كَٱلصَّرِيمِ, tr:fe-asbahat ke's-sarîm, gloss:sabaha kapkara kesilmiş halde girdi, source:68:20}. Habersiz sahipler ise {ar:فَتَنَادَوْا۟ مُصْبِحِينَ, tr:fe-tenâdev musbihîn, gloss:sabaha girerken birbirlerine seslendiler, source:68:21}. Konuştukları şey şudur: {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌ, tr:en lâ yedhulennehe'l-yevme aleykum miskîn, gloss:bugün oraya hiçbir yoksul yanınıza girmesin, source:68:24}. Bu sahnede bir sabah seferi, yoksula kapanan bir el ve Rabbin cevabı vardır. Sabah baskını yapan, sonunda baskına uğrayan olur. Bizim surede de "yalnız yiyen" kenûd, "sabah" sözüyle başlayan bir surenin sonunda Rabbinin bilgisi karşısında durur.

Su başı ile toprağın altüst edilmesi aynı günün anlatımında buluşur. Yerin sarsıldığı ve ağırlıklarını dışarı attığı gün, insanların {ar:يَصْدُرُ, tr:yasduru, gloss:sudan döner gibi döner, source:99:6} günüdür. Fiil onuncu ayetin göğüs kelimesiyle aynı köktendir. Kabirden çıkış, gömülü olanın açılması ve sudan dönüş tek bir anda birleşir. İnsanlar amellerini görmek için bölük bölük döner.

Tanıklık ile Rab sözü ise yedinci ayetin iki okumasını bir araya getirir. Âdem oğullarının "Rabbiniz değil miyim" sorusuna "evet, tanık olduk" diye cevap verdiği sahnede, insan kendi Rabbine dair kendisi üzerine tanıktır. Bizim surede de aynı insan, Rabbine karşı nankörlüğü üzerine tanıktır. Birinci ayetin atının tanığı ise koşusudur ve onun öne geçtiğine tanıklık eder. Aynı kelime atta lehte, insanda aleyhte işler.

Bu buluşmalar surenin hareketini dışarıdan içeriye doğru taşır. Sure, gözle görülen ve kulakla işitilen şeylerle başlar: soluk, kıvılcım, sabah ışığı, toz ve kalabalık. Sonra göze görünmeyen bir yere, göğüsteki taneye ulaşır. Toynakların kaldırdığı toprak kabirlerin toprağına, baskının sabahı toplanma gününe, yağmurun beklendiği tarla kabirlerini açan yere dönüşür. Malın düğümü ve yumulmuş el de toplanıp ayıklanan bir göğse dönüşür. Bu yolun her aşamasında bilgi de derinleşir: önce hazır bulunan ve gören bir tanık vardır, sonra sorulan ama cevaplanmayan bir bilgi, en sonda da içini bilen bir Rab.

