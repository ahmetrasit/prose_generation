Focus: 87:8. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. No other command or tool is available.

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


===== _commentary/v16/work/87_8/D.r13/context.md =====
# 87:8 — focus

وَنُيَسِّرُكَ لِلْيُسْرَىٰ

Anchor translation (canonical reading, reference only):

Ve seni kolay olana yönelteceğiz.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَنُيَسِّرُكَ | يَسَّرَ | ي س ر | CONJ;V;PRON |
| 2 | لِلْيُسْرَىٰ | يُسْرَىٰ | ي س ر | P;DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 87 — full text (context; no pericope)

- 87:1 سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى
- 87:2 ٱلَّذِى خَلَقَ فَسَوَّىٰ
- 87:3 وَٱلَّذِى قَدَّرَ فَهَدَىٰ
- 87:4 وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ
- 87:5 فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ
- 87:6 سَنُقْرِئُكَ فَلَا تَنسَىٰٓ
- 87:7 إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ
- 87:8 ◀ focus وَنُيَسِّرُكَ لِلْيُسْرَىٰ
- 87:9 فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ
- 87:10 سَيَذَّكَّرُ مَن يَخْشَىٰ
- 87:11 وَيَتَجَنَّبُهَا ٱلْأَشْقَى
- 87:12 ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ
- 87:13 ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- 87:14 قَدْ أَفْلَحَ مَن تَزَكَّىٰ
- 87:15 وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ
- 87:16 بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- 87:17 وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- 87:18 إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ
- 87:19 صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ


===== _commentary/v16/work/87_8/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ي س ر (root_001694) — identity root of وَنُيَسِّرُكَ (w1)

- **B001** kolaylık; kolay ve hazır duruma gelme ya da getirme — kolaylık, güçlüğün karşıtı · kolay olan, güç olmayan · kolaylaşıp hazır duruma gelmek · kolaylaştırıp hazırlamak · birine anlayış gösterip kolaylık sağlamak · kolay olan · kolay, güç olmayan
  اليسر: ضد العسر (maqayis;mufradat)؛ الميسور: ضد المعسور، وتيسر واستيسر بمعنى تهيأ (sihah)؛ تيسر واستيسر أي تسهل وتهيأ، وأيسرت المرأة وتيسرت في كذا أي سهلته وهيأته (mufradat)؛ ياسره أي ساهله (sihah)
- **B002** az miktar veya kısa süre — az miktar veya kısa süre
  اليسير: القليل، وشيء يسير أي هين (sihah)؛ واليسير يقال في الشيء القليل (mufradat)
- **B003** maddi bolluk ve varlıklı olma — maddi bolluk ve varlıklılık · varlıklılık ve maddi güç · varlıklılık · varlıklı duruma gelmek
  الميسرة والميسرة: السعة والغنى؛ واليسار واليسارة: الغنى، وقد أيسر الرجل أي استغنى (sihah)؛ الميسرة واليسار عبارة عن الغنى (mufradat)
- **B004** sol el veya sol yön — sol el veya sol yön · soldaki, sağın karşıtı · sol taraf · sola yönelip ilerlemek · iki elini de kullanabilen kişi
  اليسار لليد، تياسروا إذ أخذوا ذات اليسار، وياسروا (maqayis)؛ الأيسر: نقيض الأيمن، والميسرة خلاف الميمنة، واليسار خلاف اليمين، والياسر نقيض اليامن، ورجل أعسر يسر للذي يعمل بكلتا يديه (sihah)
- **B005** yumuşak başlı ve harekette uyumlu olma — yumuşak başlı ve çabuk uyum gösteren · hafif bacaklar · hayvanın bacaklarını iyi aktarması
  اليسرات: القوائم الخفاف؛ فرس حسن التيسور أي حسن نقل القوائم؛ رجل يسر ويسر أي حسن الانقياد (maqayis)؛ ليسر خفيف ويسر أي لين الانقياد سريع المتابعة يوصف به الإنسان والفرس (ayn)؛ اليسرات: القوائم الخفاف، ودابة حسن التيسور أي حسن نقل القوائم (sihah)
- **B006** koyunların süt ve yavru bakımından çoğalması [kalıp] — koyunların sütü ve yavrusu çoğalmak
  يسرت الغنم إذا كثر لبنها ونسلها (maqayis;sihah)
- **B007** fal oklarıyla oynanan paylaştırmalı talih oyunu — fal oklarıyla oynanan geleneksel talih oyunu · fal okları oyununa katılmak için toplananlar · fal oklarıyla oynayan kişi · fal oklarıyla oynayan kişi · topluluğun deveyi kesip parçalarını paylaştırması · deveyi kesip oyun düzenine göre paylaştırmak
  الأيسار: القوم يجتمعون على الميسر، واحدهم يسر؛ والميسر: القمار (maqayis)؛ الميسر: قمار العرب بالأزلام؛ الياسر: اللاعب بالقداح؛ اليسر والياسر بمعنى والجمع أيسار؛ يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها (sihah)
- **B008** ayrı avuç çizgileri veya uyluk damgası — avuç içindeki birbirine bitişmeyen çizgiler · uyluklardaki damga
  اليسرة: أسرار الكف إذا كانت غير ملزقة (maqayis;sihah)؛ اليسرة أيضا: سمة في الفخذين (sihah)
- **B009** aşağı doğru burma veya yüz hizasına saplama — sağ eli gövdeye çekerek aşağı doğru burma · yüz hizasına yöneltilen saplama
  اليسر: الفتل إلى أسفل، وهو أن تمد يمينك نحو جسدك؛ والطعن اليسر: حذاء وجهك (sihah)
- **B010** yer ve kişi adı kullanımları — bir yerin adı · çöl bölgesindeki bir geçidin adı · anlatıda geçen bir kişinin adı
  يسر: مكان (maqayis)؛ اليسر أيضا: دخل لنبى يربوع بالدهناء (sihah)؛ يسار الكواعب هو اسم عبد (sihah)
- **B011** genç erkek — genç erkek, delikanlı
  اليسار: الفتى (maqayis)

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 87:8, and ## Buluşmalar) =====
## Ölçüp biçmek: ok, tulum ve kura

İkinci ve üçüncü ayet dört fiili sıralar: {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:elleẕî halaka fe-sevvâ, gloss:yaratıp düzene koyan, source:87:2}, {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:velleẕî kaddera fe-hedâ, gloss:ölçüp yol gösteren, source:87:3}. Arapçada bu fiiller bir zanaatkârın işinin adımlarıdır. خلق, kökünde ölçüp biçmektir: {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhû et-takdîru'l-mustakîm, gloss:halkın aslı doğru ölçüdür, source:"خ ل ق,B001"}. Bu tanım ikinci ayetin fiilini üçüncü ayetin fiiline bağlar. Ölçülüp yontulmuş ok da bu köktendir: {ar:سهم مخلق أملس مستو, tr:sehmun muhallakun emlesu mustevin, gloss:yontulmuş düzgün ve doğru ok, source:"خ ل ق,B008"}. Bu tanımda ikinci ayetin öbür fiili olan سوّى'nin kökü de vardır. سوّى eğri olanı doğrultmaktır: {ar:استوى من اعوجاج, tr:istevâ min i'vicâc, gloss:eğrilikten doğruldu, source:"س و ي,B002"}. قدّر, bir şeyi nasıl düzleyip hazır edeceğini düşünmektir: {ar:التروية والتفكير في تسوية أمر وتهيئته, tr:et-terviyetu ve't-tefkîru fî tesviyeti emrin ve teh'iyetih, gloss:bir işi nasıl düzleyip hazırlayacağını uzun uzun düşünmek, source:"ق د ر,B005"}. Aynı kök bir şeyin vardığı ölçüyü de bildirir: {ar:مبلغ الشيء وكنهه ونهايته, tr:mebleğu'ş-şey'i ve kunhuhû ve nihâyetuh, gloss:bir şeyin vardığı yer ve özü ve sonu, source:"ق د ر,B001"}. Sonra هدى gelir. Bu kelime okun önde giden ucudur: {ar:هادي السهم نصله, tr:hâdi's-sehmi naslu, gloss:okun hâdîsi temrenidir, source:"ه د ي,B003"}. Değnek de taşıyanın önünden gittiği için bu adı alır: {ar:العصا هاديا لأنها تتقدمه, tr:el-asâ hâdiyen li-ennehâ tetekaddemuh, gloss:değnek önünden gittiği için hâdî adını alır, source:"ه د ي,B003"}. Rab ise bir şeyi düzeltip adım adım tamamlayandır: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye bir şeyi halden hale geçirerek tamamlanma sınırına kadar oluşturmaktır, source:"ر ب ب,B002"}.

Değneği doğrultmanın bir yolu da ateştir. Bu işin fiili, on ikinci ayetteki "ateşe girer" fiilinin kendisidir: {ar:صلى عصاه إذا أدارها على النار يثقفها, tr:salâ asâhu iẕâ edârahâ ale'n-nâri yuŝakkıfuhâ, gloss:değneğini ateşin üstünde çevirip doğrulttu, source:"ص ل ي,B004"}. Ölçmek, doğrultmak ve uç takmak, ikinci ve üçüncü ayetin düz anlamının yanında bir yapım sahnesi kurar. Yapılan şey yalnızca var edilmez, bir yöne de çevrilir. "Yol gösterdi" fiili okun ucunun bir hedefe dönmesi gibi duyulur.

Aynı ölçüp biçme bir deri üzerinde de yapılır. خلق'in ilk örneği, su tulumu için deriyi kesmeden önce ölçmektir: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme iẕâ kaddertuhû kable'l-kat', gloss:deriyi kesmeden önce ölçtüğümde halaktu derim, source:"خ ل ق,B001"}. İkinci ayetin fiili ile üçüncü ayetin fiili burada tek bir hareketin iki adı olur. Bitmiş kabın yapısını dokuzuncu ayetteki نفع kökü anlatır: {ar:النفع في المزادة في جانبيها يشق الأديم فيجعل في جانبيها في كل جانب نفعة, tr:en-nif'u fi'l-mezâdeti fî cânibeyhâ yuşakku'l-edîmu fe-yuc'alu fî cânibeyhâ fî kulli cânibin nif'a, gloss:su kırbasının iki yanına deri yarılıp her yana nif'a denen bir parça konur, source:"ن ف ع,B002"}. Bu yanlar on birinci ayetteki kelimenin köküyle anılır: {ar:الجنبتان ناحيتا كل شيء, tr:el-canbetân nâhiyetâ kulli şey', gloss:her şeyin iki yanı, source:"ج ن ب,B001"}. Deri yağla terbiye edilir. Bu da "Rab" kelimesinin ailesindendir: {ar:رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب, tr:rabebtu'l-edîme bi's-semni ve'd-devâe bi'l-asel ve sikâun merbûb, gloss:deriyi yağla ilacı balla terbiye ettim; terbiye edilmiş tulum, source:"ر ب ب,B006"}. Tulum çalkalanır: {ar:جهرت السقاء مخضته, tr:cehertu's-sikâe mehadtuhû, gloss:tulumu çalkaladım, source:"ج ه ر,B010"}. Kullanıldıkça da aşınıp düzleşir: {ar:أخلق الشيء وخلق إذا بلي؛ إذا أخلق املاس وذهب زئبره, tr:ahleka'ş-şey'u ve haleka iẕâ beliye iẕâ ahleka imlâsse ve ẕehebe zi'biruh, gloss:bir şey eskiyince ahleka denir; eskiyince düzleşir ve tüyü gider, source:"خ ل ق,B009"}. Beş kök tek bir nesnede, ölçülen, yanları eklenen, terbiye edilen ve eskiyen bir tulumda buluşur. Kur'an bu nesneyi bir sahnede kullanmaz. Ama aynı kelime ailesi yaratılışı bir zanaat olarak duyurur, ve bu zanaatta ölçü kesmeden önce gelir.

Üçüncü bir nesne, kura okudur. "Rab" kelimesinin ailesinde okların saklandığı torba vardır: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-ribâbe şebîhetun bi'l-kinâneti tucmeu fîhâ sihâmu'l-meysir, gloss:ribâbe meysir oklarının toplandığı sadağa benzer torbadır, source:"ر ب ب,B010"}. Bu tanım sekizinci ayetteki "kolaylaştırırız" fiilinin kökünü, meysiri, de içerir. Meysir bir oyundur ve adı paylaştırmadan gelir: {ar:يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها, tr:yasera'l-kavmu'l-cezûra ey ictezerûhâ ve'ktesemû a'dâehâ, gloss:topluluk deveyi kesip parçalarını paylaştı, source:"ي س ر,B007"}. Okların en büyük payı alanı birinci ayetteki "en yüce" kelimesinin kökündendir: {ar:المعلى السابع من القداح, tr:el-muallâ es-sâbiu mine'l-kıdâh, gloss:muallâ okların yedincisidir, source:"ع ل و,B009"}. Okun gövdesi yontulup yumuşatılır: {ar:المخلق القدح إذا لين, tr:el-muhallak el-kıdhu iẕâ luyyine, gloss:muhallak yumuşatılmış ok gövdesidir, source:"خ ل ق,B008"}. Pay da aynı köktendir: {ar:الخلاق النصيب لأنه قد قدر لكل أحد نصيبه, tr:el-halâk en-nasîb li-ennehû kad kuddira li-kulli ehadin nasîbuh, gloss:halâk paydır çünkü herkesin payı ölçülmüştür, source:"خ ل ق,B006"}. Her şeyin bir ölçüsü ve bir vadesi vardır: {ar:لكل شيء مقدار وأجل, tr:li-kulli şey'in mikdârun ve ecel, gloss:her şeyin bir miktarı ve süresi vardır, source:"ق د ر,B001"}. İkinci ve üçüncü ayetteki ölçüp biçme bu sahnede paylaştırmaya döner. On altıncı ve on yedinci ayetteki seçim de bir pay seçimidir.

Kur'an bu ölçmeyi yaratılışın kendisine uygular. Allah inkâr eden insan için {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe-kaddera, gloss:onu bir damladan yarattı ve ölçüsünü koydu, source:80:19} der, sonra {ar:ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ, tr:ŝumme's-sebîle yesserah, gloss:sonra yolu ona kolaylaştırdı, source:80:20} diye ekler. Bu iki ayet surenin ikinci, üçüncü ve sekizinci ayetlerinin fiillerini aynı sırayla verir. Başka bir yerde Allah {ar:وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا, tr:ve halaka kulle şey'in fe-kaddarahû takdîrâ, gloss:her şeyi yarattı ve ona tam ölçüsünü verdi, source:25:2} ve {ar:إِنَّا كُلَّ شَىْءٍ خَلَقْنَٰهُ بِقَدَرٍۢ, tr:innâ kulle şey'in halaknâhu bi-kader, gloss:biz her şeyi bir ölçüyle yarattık, source:54:49} der. Surenin son ayetinde adı geçen İbrahim, putları reddedip kavmine Âlemlerin Rabbini anlatırken bu ikiliyi kendi ağzından söyler: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:elleẕî halakanî fe-huve yehdîn, gloss:beni yaratan ve bana yol gösteren O'dur, source:26:78}. Pay kelimesi Kur'an'da tam bu surenin vardığı karşıtlıkla geçer. Hac ibadetleri anlatılırken yalnız bu dünyada verilmesini isteyen kişi için {ar:وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ, tr:ve mâ lehû fi'l-âhireti min halâk, gloss:onun ahirette hiçbir payı yoktur, source:2:200} denir. Önceki kavimler için {ar:فَٱسْتَمْتَعُوا۟ بِخَلَٰقِهِمْ, tr:fe'stemteû bi-halâkıhim, gloss:paylarından yararlandılar, source:9:69} denir, ayetin sonunda da yaptıkları dünyada ve ahirette boşa gider. Kura okları ve meysir müminlere yasaklanırken kullanılan kelimeler ise surenin iki kelimesini yan yana getirir: {ar:فَٱجْتَنِبُوهُ لَعَلَّكُمْ تُفْلِحُونَ, tr:fectenibûhu leallekum tuflihûn, gloss:ondan uzak durun ki kurtuluşa eresiniz, source:5:90}. On birinci ayetteki "uzak durmak" ve on dördüncü ayetteki "kurtuluşa ermek" burada aynı cümlededir. Başka bir yerde meysir için {ar:وَإِثْمُهُمَآ أَكْبَرُ مِن نَّفْعِهِمَا, tr:ve ismuhumâ ekberu min nef'ihimâ, gloss:günahları faydalarından büyüktür, source:2:219} denir. Oklarla kısmet aramak da sayılan yasaklar arasındadır: {ar:وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ, tr:ve en testaksimû bi'l-ezlâm, gloss:fal oklarıyla pay aramanız, source:5:3}. Kura okuyla alınan pay yasaklanır. Ölçüyü koyanın verdiği pay ise ahirette de geçerlidir.

Kaynaklar: 87:2 خَلَقَ خ ل ق B001; 87:2 خَلَقَ خ ل ق B008; 87:2 خَلَقَ خ ل ق B009; 87:2 خَلَقَ خ ل ق B006; 87:2 فَسَوَّىٰ س و ي B002; 87:3 قَدَّرَ ق د ر B005; 87:3 قَدَّرَ ق د ر B001; 87:3 فَهَدَىٰ ه د ي B003; 87:1 رَبِّ ر ب ب B002; 87:1 رَبِّ ر ب ب B006; 87:1 رَبِّ ر ب ب B010; 87:12 يَصْلَى ص ل ي B004; 87:9 نَّفَعَتِ ن ف ع B002; 87:11 يَتَجَنَّبُهَا ج ن ب B001; 87:7 ٱلْجَهْرَ ج ه ر B010; 87:1 ٱلْأَعْلَى ع ل و B009; 87:8 لِلْيُسْرَىٰ ي س ر B007

## Yol ve binek: önde giden, kolaylaşan, yana çekilen

Üçüncü, sekizinci ve on birinci ayetler bir yolculuğun izini sürer. هدى önden gidip yolu göstermektir: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytuhu't-tarîka ve'l-beyte hidâyeten ey arraftuh, gloss:ona yolu ve evi gösterdim yani tanıttım, source:"ه د ي,B001"}. {ar:التقدم للإرشاد, tr:et-tekaddumu li'l-irşâd, gloss:yol göstermek için öne geçmek, source:"ه د ي,B001"}. {ar:الدليل يسمى هاديا لتقدمه, tr:ed-delîlu yusemmâ hâdiyen li-tekaddumih, gloss:kılavuza önden gittiği için hâdî denir, source:"ه د ي,B003"}. Aynı kök zayıf birinin iki kişiye dayanarak yürümesini de anlatır: {ar:يهادي بين اثنين إذا كان يمشي بينهما معتمدا عليهما من ضعفه وتمايله, tr:yuhâdî beyne'sneyni iẕâ kâne yemşî beynehumâ mu'temiden aleyhimâ min da'fihî ve temâyulih, gloss:zayıflığından ve sendelemesinden iki kişinin arasında onlara dayanarak yürüdü, source:"ه د ي,B008"}. Telaşsız ve sakin bir yürüyüşü de anlatır: {ar:لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن, tr:lem yusri' isrâa'l-munhezimi ve lâkin alâ sukûnin ve hedyin hasen, gloss:kaçan biri gibi koşmadı; sakin ve güzel bir gidişle yürüdü, source:"ه د ي,B010"}. Sekizinci ayet {ar:وَنُيَسِّرُكَ لِلْيُسْرَىٰ, tr:ve nuyessiruke li'l-yusrâ, gloss:seni en kolaya kolaylaştıracağız, source:87:8} der. يسر hazır ve kolay olandır: {ar:الميسور: ضد المعسور، وتيسر واستيسر بمعنى تهيأ, tr:el-meysûr diddu'l-ma'sûr ve teyessera ve'steysera bi-ma'nâ teheyyee, gloss:meysûr zor olanın zıddıdır; teyessera hazır oldu demektir, source:"ي س ر,B001"}. Kök kolay güdülen bineği de anlatır: {ar:يسر أي لين الانقياد سريع المتابعة يوصف به الإنسان والفرس, tr:yesrun ey leyyinu'l-inkıyâdi serîu'l-mutâbaa yûsafu bihi'l-insânu ve'l-feres, gloss:yesr kolay güdülen ve çabuk ardından gelen demektir; insan ve at için söylenir, source:"ي س ر,B005"}. Hafif bacakları da anlatır: {ar:اليسرات: القوائم الخفاف, tr:el-yeserât el-kavâimu'l-hıfâf, gloss:yeserât hafif bacaklardır, source:"ي س ر,B005"}. Sekizinci ayetin fiili düz anlamında Peygamber'e verilen bir vaattir. Aile resmi bu vaade bir binek görüntüsü katar: üzerindekinin isteğine kolayca uyan ve yolu hafif adımlarla alan bir hayvan.

On birinci ayetteki الأشقى'nın kökü zahmettir: {ar:أصل يدل على المعاناة وخلاف السهولة, tr:aslun yedullu ale'l-muânâti ve hilâfi's-suhûle, gloss:katlanmayı ve kolaylığın zıddını gösteren köktür, source:"ش ق و,B002"}. Ama aynı kök bir dağ sırtını da adlandırır, ve bu tanımda üç kök birden geçer: {ar:الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان, tr:eş-şâkî min huyûdi'l-cibâli't-tâliu't-tavîl ve mea tûlihî eyseru suûden ve akdaru mak'aden li'l-insân, gloss:şâkî dağ çıkıntılarından uzun yükselen sırttır; uzunluğuna rağmen tırmanması daha kolay ve insan için oturmaya daha elverişlidir, source:"ش ق و,B004"}. "Zahmet" kelimesinin kökü burada "daha kolay" ve "ölçüye daha uygun" kelimeleriyle aynı cümlededir. Bu yüzden yol aynı olabilir. Fark, yolcunun onu nasıl yürüdüğündedir. On birinci ayetin fiili ise yolculuğun bir başka hareketidir. جنب bir hayvanı yanında yedeğe almaktır: {ar:جنبت الدابة إذا قدتها إلى جنبك وكذلك جنبت الأسير, tr:cenebtu'd-dâbbete iẕâ kudtuhâ ilâ cenbike ve keẕâlike cenebtu'l-esîr, gloss:hayvanı yanında yedeğe aldım; esiri de öyle, source:"ج ن ب,B005"}. Ayetteki biçim ise bir şeyi yanında uzak tutmaktır: {ar:جانبه وتجانبه وتجنبه واجتنبه كله بمعنى وجنبته الشيء أي نحيته عنه, tr:cânebehû ve tecânebehû ve teceннebehû ve'ctenebehû kulluhû bi-ma'nâ ve cenebtuhu'ş-şey'e ey nahheytuhû anh, gloss:cânebe tecânebe tecennebe ictenebe hep aynı anlamdadır; onu bir şeyden uzak tuttum yani o şeyi ondan ayırdım, source:"ج ن ب,B003"}. En bedbaht kişi öğüdü reddetmez, onun yanından geçer ve onu kendi yolunun kenarında tutar.

İkinci ayetin سوّى fiilinin ailesinde binicinin oturuşu vardır: {ar:استوى على ظهر دابته أي علا واستقر, tr:istevâ alâ zahri dâbbetihî ey alâ ve'stekarr, gloss:hayvanının sırtına oturdu yani üstüne çıkıp yerleşti, source:"س و ي,B003"}. Bu tanım birinci ayetteki yükseklik kökünü de içerir. Semere serilen örtü de bu ailedendir: {ar:السَّويّة كساء يلف ويجعل شبيها بالحوية يلقى على سنام البعير, tr:es-seviyye kisâun yuleffu ve yuc'alu şebîhen bi'l-haviyyeti yulkâ alâ senâmi'l-baîr, gloss:seviyye sarılıp haviyyeye benzetilerek devenin hörgücüne konan örtüdür, source:"س و ي,B010"}. Benzetildiği haviyye de beşinci ayetteki أحوى'nın kökündendir: {ar:الحوية كساء يحوي حول سنام البعير ثم يركب, tr:el-haviyye kisâun yahvî havle senâmi'l-baîri ŝumme yurkeb, gloss:haviyye devenin hörgücünü saran ve üstüne binilen örtüdür, source:"ح و ي,B004"}. Aynı kök yolun ortasını da adlandırır: {ar:مكان سوى أي عدل ووسط, tr:mekânun suven ey adlun ve vasat, gloss:dengeli ve orta bir yer, source:"س و ي,B006"}. Ama "cehennemin ortası" da bu kelimeyle söylenir: {ar:في سواء الجحيم, tr:fî sevâi'l-cahîm, gloss:cehennemin ortasında, source:"س و ي,B006"}.

Kur'an bu yolu sahneler. Yeminlerle açılan bir surede verenler ile cimrilik edenler ayrılır: {ar:فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ, tr:fe-senuyessiruhû li'l-yusrâ, gloss:onu en kolaya kolaylaştıracağız, source:92:7}, {ar:فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ, tr:fe-senuyessiruhû li'l-usrâ, gloss:onu en zora kolaylaştıracağız, source:92:10}. Aynı fiil iki yöne çalışır. Birinin bineği kolaylığa, ötekininki zorluğa gider. Ardından {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hudâ, gloss:yol göstermek elbette bize düşer, source:92:12} denir. İnsan için {ar:ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ, tr:ŝumme's-sebîle yesserah, gloss:sonra yolu ona kolaylaştırdı, source:80:20} ve {ar:إِنَّا هَدَيْنَٰهُ ٱلسَّبِيلَ إِمَّا شَاكِرًۭا وَإِمَّا كَفُورًا, tr:innâ hedeynâhu's-sebîle immâ şâkiran ve immâ kefûrâ, gloss:biz ona yolu gösterdik; ister şükreden olsun ister nankör, source:76:3} denir. Bir başka yerde yol iki sırttır ve tırmanılmaz: {ar:وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ, tr:ve hedeynâhu'n-necdeyn, gloss:ona iki yüksek yolu gösterdik, source:90:10}, {ar:فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ, tr:fe-le'ktehame'l-akabe, gloss:ama o sarp yokuşa atılmadı, source:90:11}. Zahmet kelimesi Adem'in hikâyesinde geçer. Allah onu uyarır: {ar:فَلَا يُخْرِجَنَّكُمَا مِنَ ٱلْجَنَّةِ فَتَشْقَىٰٓ, tr:fe-lâ yuhricennekumâ mine'l-cenneti fe-teşkâ, gloss:sakın sizi cennetten çıkarmasın; yoksa zahmete düşersin, source:20:117}. Yere indirilirken de şöyle der: {ar:فَمَنِ ٱتَّبَعَ هُدَاىَ فَلَا يَضِلُّ وَلَا يَشْقَىٰ, tr:fe-meni't-tebea hudâye fe-lâ yadillu ve lâ yeşkâ, gloss:kim benim yol göstermemi izlerse ne yolunu şaşırır ne de bedbaht olur, source:20:123}. Peygamber'e de {ar:مَآ أَنزَلْنَا عَلَيْكَ ٱلْقُرْءَانَ لِتَشْقَىٰٓ, tr:mâ enzelnâ aleyke'l-kur'âne li-teşkâ, gloss:Kur'an'ı sana zahmet çekesin diye indirmedik, source:20:2} denir. Musa Firavun'a gönderilirken {ar:وَيَسِّرْ لِىٓ أَمْرِى, tr:ve yessir lî emrî, gloss:işimi bana kolaylaştır, source:20:26} diye dua eder. Kolaylık zorlukla birlikte gelir: {ar:فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا, tr:fe-inne mea'l-usri yusrâ, gloss:zorlukla birlikte bir kolaylık vardır, source:94:5}. Surenin son ayetinde adı geçen İbrahim, yana çekilmeyi kendisi için ister: {ar:وَٱجْنُبْنِى وَبَنِىَّ أَن نَّعْبُدَ ٱلْأَصْنَامَ, tr:vecnubnî ve beniyye en na'bude'l-esnâm, gloss:beni ve oğullarımı putlara tapmaktan uzak tut, source:14:35}. On birinci ayetin kökü burada tersine çalışır. Bedbaht öğüdü kendinden uzak tutar, İbrahim ise Rabbinden kendisini puttan uzak tutmasını ister. Yolun yanlış ucu da gösterilir. Cennetteki bir kişi dünyadaki arkadaşını hatırlar, aşağıya bakar ve {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettalea fe-raâhu fî sevâi'l-cahîm, gloss:baktı ve onu cehennemin ortasında gördü, source:37:55}.

Kaynaklar: 87:3 فَهَدَىٰ ه د ي B001; 87:3 فَهَدَىٰ ه د ي B003; 87:3 فَهَدَىٰ ه د ي B008; 87:3 فَهَدَىٰ ه د ي B010; 87:8 نُيَسِّرُكَ ي س ر B001; 87:8 لِلْيُسْرَىٰ ي س ر B005; 87:11 ٱلْأَشْقَى ش ق و B004; 87:11 ٱلْأَشْقَى ش ق و B002; 87:11 يَتَجَنَّبُهَا ج ن ب B005; 87:11 يَتَجَنَّبُهَا ج ن ب B003; 87:2 فَسَوَّىٰ س و ي B003; 87:2 فَسَوَّىٰ س و ي B010; 87:5 أَحْوَىٰ ح و ي B004; 87:2 فَسَوَّىٰ س و ي B006

## Koşan dizi: önde, ardında, sonda

On altıncı ve on yedinci ayetteki zaman kelimeleri, hareket halindeki bir at ya da deve dizisinde yer de bildirir. Birinci ayetteki tesbih fiilinin kökünde koşan at vardır: {ar:السابح من الخيل يمد يديه في الجري؛ النجوم تسبح في الفلك, tr:es-sâbihu mine'l-hayli yemuddu yedeyhi fi'l-cerî en-nucûmu tesbehu fi'l-felek, gloss:sâbih koşarken ön ayaklarını uzatan attır; yıldızlar yörüngelerinde yüzer, source:"س ب ح,B004"}. Kökün temel anlamı suda yüzmektir: {ar:سَبَحَ فِي ٱلْمَاءِ, tr:sebeha fi'l-mâ, gloss:suda yüzdü, source:"memory"}. Dizinin başında öncüler vardır: {ar:هوادي الخيل أعناقها أو أول رعيل, tr:hevâdi'l-hayli a'nâkuhâ ev evvelu racîl, gloss:atların hevâdîsi boyunlarıdır ya da ilk bölüktür, source:"ه د ي,B003"}. On beşinci ayetteki namaz kökü ikinci atı adlandırır: {ar:قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه, tr:kad sallâ ve câe musalliyen li-enne ra'sehû yetlu's-salâ'lleẕî beyne yedeyh, gloss:musallî olarak geldi çünkü başı öndekinin sağrısını izler, source:"ص ل و,B006"}. {ar:السابق الأول والمصلي الثاني, tr:es-sâbiku'l-evvel ve'l-musallî es-ŝânî, gloss:sâbık birinci musallî ikincidir, source:"ص ل و,B006"}. Sekizinci ayetin kökü düzgün adımı verir: {ar:دابة حسن التيسور أي حسن نقل القوائم, tr:dâbbetun hasenu't-teysûr ey hasenu nakli'l-kavâim, gloss:ayaklarını güzel atan hayvan, source:"ي س ر,B005"}. On altıncı ayetteki tercih kökü, öne koymaktır: {ar:له أصل تقديم الشيء, tr:lehû aslu takdîmi'ş-şey', gloss:bir şeyi öne koyma anlamında bir kökü vardır, source:"ء ث ر,B001"}. Ama aynı kök birinin izinden gitmek de demektir: {ar:جاء فلان على إثري وأثري وجاء في أثره وإثره, tr:câe fulânun alâ isrî ve eserî ve câe fî eserihî ve isrih, gloss:falanca peşimden geldi; onun izinden geldi, source:"ء ث ر,B004"}. Dünya yakın kıyıdır: {ar:العدوة الدنيا والعدوة القصوى, tr:el-udvetu'd-dunyâ ve'l-udvetu'l-kusvâ, gloss:yakın yamaç ve uzak yamaç, source:"د ن و,B002"}. Ahiret kökü topluluğun arkasında kalanları adlandırır: {ar:أخرى القوم أي من كان في آخرهم, tr:uhra'l-kavmi ey men kâne fî âhirihim, gloss:topluluğun uhrâsı en arkada olandır, source:"ء خ ر,B001"}. Semerin arka direği de bu köktendir: {ar:آخرة الرحل وقادمته ومؤخر الرحل ومقدمه, tr:âhiratu'r-rahli ve kâdimetuhû ve muahharu'r-rahli ve mukaddemuh, gloss:semerin arka ve ön direği, source:"ء خ ر,B003"}. On yedinci ayetteki "kalıcı" kelimesinin ailesinde koşusunun bir kısmını saklayan atlar vardır: {ar:المبقيات من الخيل التي تبقي بعض جريها تدخره, tr:el-mubkıyâtu mine'l-hayli elletî tubkî ba'da cerîhâ teddehıruh, gloss:mubkıyât koşusunun bir kısmını saklayıp biriktiren atlardır, source:"ب ق ي,B004"}. On sekizinci ayetin "ilk" kelimesi de dizinin önündeki deveyi verir: {ar:ناقة أولة وجمل أول إذا تقدما الإبل, tr:nâkatun evvelatun ve cemelun evvelu iẕâ tekaddeme'l-ibil, gloss:develerin önüne geçen dişi deve ve erkek deve, source:"ء و ل,B001"}.

Bu dizi içinde on altıncı ve on yedinci ayet bir koşu olarak okunur. Öne koyduğunuz şey yakın olandır. Arkada gelen ise daha hayırlıdır ve daha uzun dayanır, tıpkı koşusunu sona saklayan at gibi. Düz bir anlatım yalnızca iki hayatı karşılaştırır. Bu sahne karşılaştırmaya bir zaman sırası ekler: ilk gelen yarışı kazanan değildir. On beşinci ayetteki "namaz kıldı" fiilinin ailesinde öncünün hemen ardından gelen ikinci at vardır. Bu, bir izleme hareketi olarak duyulur. Ama bu bağ kelimenin namaz anlamının yerine geçmez.

Kur'an yemin ettiği koşucularla bir sureyi açar: {ar:وَٱلسَّٰبِحَٰتِ سَبْحًۭا, tr:ve's-sâbihâti sebhâ, gloss:yüzdükçe yüzenlere andolsun, source:79:3}. Bu, Firavun'un "en yüce rabbinizim" dediği ve dünya hayatını tercih edenin anıldığı suredir. Bir başka yerde öndekiler {ar:وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ, tr:ve's-sâbikûne's-sâbikûn, gloss:öne geçenler ise öne geçenlerdir, source:56:10} diye anılır. Yakın ve uzak yamaç, iki topluluğun karşılaştığı günün tasvirinde geçer: {ar:إِذْ أَنتُم بِٱلْعُدْوَةِ ٱلدُّنْيَا وَهُم بِٱلْعُدْوَةِ ٱلْقُصْوَىٰ, tr:iẕ entum bi'l-udveti'd-dunyâ ve hum bi'l-udveti'l-kusvâ, gloss:o gün siz yakın yamaçtaydınız onlar uzak yamaçtaydı, source:8:42}. On altıncı ayetin cümle yapısı başka bir yerde neredeyse aynen tekrarlanır. Orada "yakın" yerine "acele gelen" kelimesi kullanılır: {ar:كَلَّا بَلْ تُحِبُّونَ ٱلْعَاجِلَةَ, tr:kellâ bel tuhibbûne'l-âcile, gloss:hayır; siz acele geleni seviyorsunuz, source:75:20}, {ar:وَتَذَرُونَ ٱلْءَاخِرَةَ, tr:ve teẕerûne'l-âhira, gloss:ve sonra geleni bırakıyorsunuz, source:75:21}. Önce geleni tutup arkadan geleni bırakmak, bu dizideki yanlış sıralamadır.

Kaynaklar: 87:1 سَبِّحِ س ب ح B004; 87:3 فَهَدَىٰ ه د ي B003; 87:15 فَصَلَّىٰ ص ل و B006; 87:8 لِلْيُسْرَىٰ ي س ر B005; 87:16 تُؤْثِرُونَ ء ث ر B001; 87:16 تُؤْثِرُونَ ء ث ر B004; 87:16 ٱلدُّنْيَا د ن و B002; 87:17 وَٱلْءَاخِرَةُ ء خ ر B001; 87:17 وَٱلْءَاخِرَةُ ء خ ر B003; 87:17 أَبْقَىٰٓ ب ق ي B004; 87:18 ٱلْأُولَىٰ ء و ل B001

## Buluşmalar

İmgelerin çoğu, surenin son ayetinde adı geçen Musa'nın hikâyesinde buluşur. Musa uzakta bir ateş görür ve {ar:أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ecidu ale'n-nâri hudâ, gloss:ateşin başında bir yol gösteren bulurum, source:20:10} umuduyla ona yönelir. Uzaktan görülen ateşin sahnesi ile yol sahnesi burada aynı cümlededir. Ateşin başında önce seçim gelir: {ar:وَأَنَا ٱخْتَرْتُكَ, tr:ve ene'htertuk, gloss:seni ben seçtim, source:20:13}. Sonra namaz ve anma gelir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14}. Sonra gizli olan gelir: {ar:أَكَادُ أُخْفِيهَا, tr:ekâdu uhfîhâ, gloss:onu neredeyse gizli tutuyorum, source:20:15}. Başka bir anlatımda ateşin başında tesbih söylenir: {ar:وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve subhânallâhi rabbi'l-âlemîn, gloss:Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu sahnede surenin on ikinci ve on beşinci ayetleri arasındaki karşıtlık bir kişinin yolculuğunda çözülür. Aynı ateşe yaklaşan biri onun içine sokulmaz. Ateş ona yol, seçilmişlik, namaz ve anma verir. Surede bu iki son iki ayrı kişiye düşer: on ikinci ayetteki kişi ateşe girer, on beşinci ayetteki kişi namaz kılar. Kelimelerin harf benzerliği bu ayrılığı kulakta da duyurur.

İkinci büyük buluşma selin sahnesidir. Gökten inen suyun vadilerde {ar:بِقَدَرِهَا, tr:bi-kaderihâ, gloss:kendi ölçülerince, source:13:17} akması, ölçüp biçme sahnesini çağırır. Selin taşıdığı köpük, otlağın vardığı döküntüdür. İnsanların {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâr, gloss:ateşte üzerine yaktıkları şeyden, source:13:17} çıkan köpük ise ateşin sahnesine girer. Faydalı olanın yerde kalması da öğüdün ve kalıcılığın sahnesidir. Kurumuş otun tencerenin köpüğüyle aynı adı taşıması, bu iki köpüğün Arapçada zaten tek bir kelimede birleştiğini gösterir. Bu ayet surenin beşinci ayetinden on yedinci ayetine uzanan çizgiyi tek bir manzaraya sığdırır. Bir yanda giden döküntü, öbür yanda kalan fayda vardır.

Üçüncü buluşma, Musa'nın karşısındaki sihirbazların sahnesidir. Sihirbazlar secdeye kapanır. Firavun kendi azabının daha çetin ve {ar:وَأَبْقَىٰ, tr:ve ebkâ, gloss:ve daha kalıcı, source:20:71} olduğunu söyler. Sihirbazlar da onu {ar:لَن نُّؤْثِرَكَ, tr:len nu'ŝirak, gloss:seni asla tercih etmeyiz, source:20:72} diye reddeder, yalnızca {ar:هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:hâẕihi'l-hayâte'd-dunyâ, gloss:bu dünya hayatı, source:20:72} üzerinde hüküm verebileceğini söyler ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Sonra suçlu için {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:20:74} der, iman edenler için {ar:ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:ed-derecâtu'l-ulâ, gloss:en yüce dereceler, source:20:75} der, ve hepsini {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76} sözüyle bağlar. Bu birkaç ayette seçim, kalıcı hayat, yükseklik ve yarılan tarlanın kelimeleri birlikte konuşur. Firavun'un "en yüce" iddiası da başka bir anlatımda bu sahneye eklenir. Surenin ikinci yarısı, on üçüncü ayetten on yedinci ayete kadar, neredeyse kelimesi kelimesine Musa'nın hikâyesindeki bir topluluğun ağzından gelmiştir. Son ayetin Musa'nın sayfalarını anması da bu yüzden önem taşır.

Dördüncü buluşma ot ile seçimdir. Dünya hayatının kuruyan ota benzetildiği ayetin hemen ardından kalıcı iyi işlerin daha hayırlı olduğu söylenir. Dünya hayatı başka bir yerde bir {ar:زَهْرَةَ, tr:zehrate, gloss:çiçek, source:20:131} olarak anılır, ve aynı ayet {ar:خَيْرٌۭ وَأَبْقَىٰ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:20:131} diye biter. Otlağın sahnesi seçimin sahnesine bu yolla girer. Beşinci ayetteki ot ile on altıncı ayetteki tercih edilen hayat aynı nesnedir. Kalıcı olan ise ayıklanıp seçilen şeydir. Tarlanın sahnesi bu iki uç arasında bir yol açar. Kalıcı iyilik anlamına gelen kurtuluş kelimesi on dördüncü ayette, toprağı yaran çiftçinin kelimesiyle söylenir. Yabani ot kendi haline kalınca kurur ve selle gider. İşlenen toprağın ürünü ise büyür, hakkı verilir ve geriye kalan bir pay bırakır. Biri dünya tarlası, öbürü ahiret tarlasıdır.

Beşinci buluşma, yaratma fiillerinde zanaat ile bedenin birleşmesidir. İkinci ayetteki ikili hem yontulmuş oku hem de ceninin biçimlenmesini anlatır. Rahimden başlayan ayetin toprağın yağmurla titreşmesiyle bitmesi, beden ile otlağı da birbirine bağlar. Aynı aile, üçüncü ayetteki ölçmeyi pay ölçmeye de taşır, ve on altıncı ayetteki tercih bir pay seçimine döner. Değneği ateşte doğrultmanın fiili on ikinci ayetin fiilidir. Bu fiil aynı ateşin düzelten bir işi ile içine düşenin katlandığı bir işi olduğunu duyurur. Bu son bağ dilin yankısıdır, ayetin sözü değildir.

Bu buluşmalar surenin hareketini taşır. Sure tesbih emriyle ve yükseklikle açılır. Ölçen, yontan ve yol gösteren Rabbin işiyle devam eder. Yağmurun çıkardığı ve selin götürdüğü ot ile sona gelen bir ömür gösterir. Sonra sözün toplanıp unutulmamasına, sunulan öğüde ve öğüt karşısında ikiye ayrılan insanlara geçer. Biri ateşe girer ve ne ölü ne diri kalır. Öbürü arınır, Rabbinin adını anar ve namaz kılar, yani surenin başındaki emri yerine getirir. Ardından seçim gelir: yakın olan öne konmuştur, ama arkadan gelen daha hayırlı ve daha kalıcıdır. Sure, bu sözün ilk sayfalarda, ateşin başında namaz ve anma emrini alan Musa'nın ve Rabbinden kendisini puttan uzak tutmasını isteyen İbrahim'in sayfalarında yazılı olduğunu söyleyerek kapanır.

