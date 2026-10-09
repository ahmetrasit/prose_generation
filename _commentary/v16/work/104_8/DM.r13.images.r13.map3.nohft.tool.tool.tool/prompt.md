Focus: 104:8. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. Run each command exactly as written, as the whole command: no cd, no && and no ; (such a command is refused and never runs). No other command or tool is available.

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


===== _commentary/v16/work/104_8/D.r13/context.md =====
# 104:8 — focus

إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ

Anchor translation (canonical reading, reference only):

Gerçekten o, üzerlerine kapatılmıştır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | إِنَّهَا | إِنّ |  | ACC;PRON |
| 2 | عَلَيْهِم | عَلَىٰ |  | P;PRON |
| 3 | مُّؤْصَدَةٌ | مُّؤْصَدَة | و ص د | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 104 — full text (context; no pericope)

- 104:1 وَيْلٌۭ لِّكُلِّ هُمَزَةٍۢ لُّمَزَةٍ
- 104:2 ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ
- 104:3 يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ
- 104:4 كَلَّا ۖ لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ
- 104:5 وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ
- 104:6 نَارُ ٱللَّهِ ٱلْمُوقَدَةُ
- 104:7 ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ
- 104:8 ◀ focus إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ
- 104:9 فِى عَمَدٍۢ مُّمَدَّدَةٍۭ


===== _commentary/v16/work/104_8/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## و ص د (root_001653) — identity root of مُّؤْصَدَةٌ (w3)

- **B001** bitiştirerek sıkıca kapatma — kapıyı örtüp sıkıca kapatmak · kapıyı örtüp sıkıca kapatmak · örtülmüş ve kapalı · örtülmüş ve sıkıca kapatılmış
  أصل يدل على ضم شيء إلى شيء (maqayis)؛ أوصدت الباب أغلقته والموصد المطبق (maqayis)؛ أوصدت الباب وآصدته إذا أغلقته فهو موصد ومطبقة (sihah)؛ أوصدت الباب وآصدته أي أطبقته وأحكمته ومؤصدة مطبقة (mufradat)
- **B002** eve bağlı avlu veya kapı — evin avlusu veya kapısı
  الوصيد الفناء لاتصاله بالربع (maqayis)؛ الوصيد فناء البيت والوصيد الباب (ayn)؛ الوصيد الفناء (sihah)
- **B003** dağdaki taş hayvan barınağı — dağda hayvanlar için yapılan taş oda veya çevirmelik · dağda böyle bir taş barınak kurmak
  الوصيدة كالحظيرة تتخذ للمال إلا أنها من الحجارة والحظيرة من الغصنة واستوصدت في الجبل (sihah)؛ الوصيدة حجرة تجعل للمال في الجبل (mufradat)
- **B004** kökleri birbirine yakın bitki — kökleri birbirine yakın bitki
  الوصيد النبت المتقارب الأصول (maqayis)؛ الوصيد النبات المتقارب الاصول (sihah)؛ الوصيد المتقارب الأصول (mufradat)

## ECHO ء ص د (root_000036) — for مُّؤْصَدَةٌ (w3): withheld observed target; not identity

- **B001** kuşatıp kapatma — kapatıp örten şey · kuşatıp kapatma · üzerlerine kapattı · kapıyı kapattı · üzerlerine kapatılmış ateş · kapatıp örten şey için kullanılan ad
  شيء يشتمل على الشيء (maqayis); الإِصد والإِصاد والوصاد بمنزلة المطبق (ayn); أصدت عليهم وأوصدته (ayn); نار مُؤصدة أي مطبقة (ayn); آصدت الباب إذا أغلقته (sihah)
- **B002** çevrili barınak — içindekileri çevreleyen barınak veya ağıl
  الحظيرة أُصيدة سميت بذلك لاشتمالها على ما فيها (maqayis); الأُصيدة كالحظيرة لغة في الوصيدة (sihah)
- **B003** kız çocuklarının giydiği küçük veya içe giyilen gömlek — kız çocuklarının giydiği küçük veya içe giyilen gömlek · küçük iç gömleği olan kız · ona küçük iç gömleğini giydirdi
  الأُصدة قميص صغير يلبسه الصبايا (maqayis); صبية ذات مُؤصد (maqayis); الأُصدة قميص يلبس تحت الثوب وتلبسه صغار الجواري (sihah); أصدته تأصيدا (sihah)
- **B004** avlu — avlu
  الأَصيد لغة في الوصيد وهو الفناء (sihah)
- **B005** dağlar arasındaki çukur alan — belirli bir yer adı · dağlar arasındaki çukur alan
  ذات الأَصاد موضع (sihah); الأَصاد ردهة بين أجبل (sihah)

===== _commentary/v16/out/s104/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 104:8, and ## Buluşmalar) =====
## Sürü: damgalanan, ağıla kapatılan, sürülen

Arapların dilinde mal çoğu zaman sürüdür {ar:كانت أموال العرب أنعامهم, tr:kânet emvâlü'l-Arabi en'âmehüm, gloss:Arapların malları hayvanlarıydı, source:"م و ل,B001"}. Bu kapıdan surenin kelimeleriyle kurulmuş bir çoban sahnesi açılır. Sürü bir araya toplanır ve sayılır; ikinci ayetin iki fiili bunu yapar. Hayvanlar sahibinin ateş damgasını taşır: devenin "nâr"ı onun damgasıdır {ar:ما نار هذه الناقة أي ما سمتها, tr:mâ nâru hâzihi'n-nâka ey mâ simetühâ, gloss:bu devenin ateşi nedir, yani damgası nedir, source:"ن و ر,B002"}. Hayvanlar dağda taştan bir ağılda tutulur ve bu ağılın adı sekizinci ayetteki kelimenin kökündendir, tanımında da "mal" geçer {ar:الوصيدة حجرة تجعل للمال في الجبل, tr:el-vasîde hucratün tüc'alü li'l-mâli fi'l-cebel, gloss:vasîde, dağda mal için yapılan bir ağıldır, source:"و ص د,B003"}. Sesçe komşu bir kökte ağılın, içindekini kuşattığı için böyle adlandırıldığı söylenir {ar:الحظيرة أصيدة سميت بذلك لاشتمالها على ما فيها, tr:el-hazîra esîdetün summiyet bi-zâlike li-iştimâlihâ alâ mâ fîhâ, gloss:ağıla içindekini kuşattığı için "esîde" denir, source:"ء ص د,B002"}; bu komşu kök bir yankıdır, aynı kökün kanıtı değildir.

Sürüyü kırıcının adı taşıyan acımasız çoban sürer: hayvanlara merhameti az olan, onları birbirine çarptırıp ezen kişiye "hutame" denir ve çobanların en kötüsü odur {ar:شر الرعاء الحُطَمَة, tr:şerru'r-ri'â'i'l-hutame, gloss:çobanların en kötüsü hutamedir, source:"ح ط م,B004"}, {ar:رجل حَطِم وحُطَمَة إذا كان قليل الرحمة للماشية يهشم بعضها ببعض, tr:racülün hatimün ve hutame izâ kâne kalîle'r-rahmeti li'l-mâşiye, gloss:hayvana merhameti az olup onları birbirine vurarak ezen adam, source:"ح ط م,B004"}. Önüne geleni çiğneyen yoğun deve sürüsüne de, aslanın sürü içinde yaptığı kırıma da aynı ad verilir {ar:حُطَمَة الأسد في المال عيثه وفرسه, tr:hutametü'l-esedi fi'l-mâl, gloss:aslanın maldaki hutamesi, onun yaptığı kırım ve parçalamadır, source:"ح ط م,B006"}. Binicinin topuğundaki demir mahmuz birinci ayetin kökündendir {ar:والمهمز والمهماز حديدة في مؤخر خف الرائض, tr:ve'l-mihmez ve'l-mihmâz hadîdetün fî mu'ahhari huffi'r-râid, gloss:mahmuz, at terbiyecisinin ayakkabısının arkasındaki demirdir, source:"ه م ز,B003"}; sürülen hayvanın bitkin düşmesi de surenin ilk kelimesinin kökündendir {ar:الكال المعيي, tr:el-kâll el-mu'yî, gloss:yorgun düşen, source:"ك ل ل,B001"}. Kökte kalabalık bölükler de vardır {ar:الكلاكل من الجماعات كالكراكر من الخيل, tr:el-kelâkil mine'l-cemâ'ât, gloss:kalabalık topluluklar, at bölükleri gibi, source:"ك ل ل,B009"}. Sahipleri tarafından ihmal edilmiş zayıf koyuna da atılma kökünden ad verilir {ar:يقال للشاة المهزولة التي يهملها أهلها نبيذة, tr:yükâlü li'ş-şâti'l-mehzûle nebîze, gloss:sahiplerinin ihmal ettiği zayıf koyuna "nebîze" denir, source:"ن ب ذ,B009"}. Sürü sahipleri de çadır halkıdır, otlağa göçerler {ar:كانوا أهل عمد ينتقلون إلى الكلأ, tr:kânû ehle amedin yentekılûne ile'l-kele', gloss:otlağa göçen direk, yani çadır halkıydılar, source:"ع م د,B004"}.

Sure bu sahneyi sahibine çevirir. Malı sürü olan adam atılır, üzerine ateş kapanır ve kapatılır. Damgalayan damgalanır, ağıl kuran ağıla kapatılır, sürüsünü ezerek süren çobanın adı ateşin adıdır. Kuran sürmeyi cehenneme yürüyüş olarak anlatır. Meryem suresinde Allah {ar:وَنَسُوقُ ٱلْمُجْرِمِينَ إِلَىٰ جَهَنَّمَ وِرْدًۭا, tr:ve nesûku'l-mücrimîne ilâ cehenneme virdâ, gloss:suçluları susuz bir sürü gibi cehenneme süreriz, source:19:86} der; "vird", suya inen sürüdür. Zümer suresinde {ar:وَسِيقَ ٱلَّذِينَ كَفَرُوٓا۟ إِلَىٰ جَهَنَّمَ زُمَرًا, tr:ve sîka'llezîne keferû ilâ cehenneme zümerâ, gloss:inkâr edenler bölük bölük cehenneme sürülür, source:39:71}, Kaf suresinde {ar:وَجَآءَتْ كُلُّ نَفْسٍۢ مَّعَهَا سَآئِقٌۭ وَشَهِيدٌۭ, tr:ve câet küllü nefsin me'ahâ sâikun ve şehîd, gloss:her can yanında bir sürücü ve bir tanıkla gelir, source:50:21}. Damga da Kuran'da vardır: Kalem suresinde mal ve oğullar sahibi hemmâz için Allah {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:se-nesimühû ale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16} der; "hurtum" bir hayvanın burnu için kullanılan kelimedir. Tevbe suresinde altın ve gümüş biriktirip infak etmeyenler için Allah kızdırılmış hazineyi damgaya çevirir: {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhühüm ve cünûbühüm ve zuhûruhüm, gloss:o gün bunlar cehennem ateşinde kızdırılır da alınları, yanları ve sırtları onlarla dağlanır, source:9:35}, {ar:هَٰذَا مَا كَنَزْتُمْ لِأَنفُسِكُمْ, tr:hâzâ mâ kenaztüm li-enfüsiküm, gloss:işte kendiniz için biriktirdiğiniz, source:9:35}. Al-i İmran suresinde dünyanın cazip kılınan şeyleri arasında {ar:وَٱلْخَيْلِ ٱلْمُسَوَّمَةِ وَٱلْأَنْعَٰمِ وَٱلْحَرْثِ, tr:ve'l-hayli'l-müsevvemeti ve'l-en'âmi ve'l-hars, gloss:salma ve nişanlı atlar, hayvanlar ve ekinler, source:3:14} sayılır. Neml suresinde ise ezip geçen kalabalık bir ordudur: karınca ötekilere {ar:لَا يَحْطِمَنَّكُمْ سُلَيْمَٰنُ وَجُنُودُهُۥ وَهُمْ لَا يَشْعُرُونَ, tr:lâ yahtımenneküm Süleymânü ve cünûdühû ve hüm lâ yeş'urûn, gloss:Süleyman ve orduları farkında olmadan sizi ezmesin, source:27:18} der; ezici kalabalığın fiili ateşin adıyla aynı köktendir.

Kaynaklar: 104:2 مَالًا م و ل B001; 104:2 جَمَعَ ج م ع B001; 104:2 وَعَدَّدَهُۥ ع د د B001; 104:6 نَارُ ن و ر B002; 104:8 مُّؤْصَدَةٌۢ و ص د B003; 104:8 مُّؤْصَدَةٌۢ ء ص د B002; 104:4 ٱلْحُطَمَةِ ح ط م B004; 104:4 ٱلْحُطَمَةِ ح ط م B006; 104:1 هُمَزَةٍ ه م ز B003; 104:1 لِّكُلِّ ك ل ل B001; 104:1 لِّكُلِّ ك ل ل B009; 104:4 لَيُنۢبَذَنَّ ن ب ذ B009; 104:9 عَمَدٍ ع م د B004

## Aşağı atılan, yukarı çıkan ve hedefini bulan ateş

Surenin dikey bir sahnesi vardır ve bir avcının nişanı ile aynı hareketi paylaşır. Adam aşağı atılır; atma kökünün özü fırlatıp bırakmaktır {ar:أصل صحيح يدل على طرح وإلقاء, tr:aslün sahîhun yedüllü alâ tarhin ve ilkâ', gloss:atıp bırakmayı gösterir, source:"ن ب ذ,B001"}. Ateş ise yukarı çıkar. {ar:تَطَّلِعُ, tr:tattali'u, gloss:çıkıp vurur, üstüne tırmanır, source:104:7} fiilinin kökü güneşin ve yıldızın doğuşudur {ar:طلعت الشمس والكوكب طلوعا ومطلعا, tr:tala'ati'ş-şemsü ve'l-kevkeb, gloss:güneş ve yıldız doğdu, source:"ط ل ع,B001"}; görünmek ve belirmek {ar:أصل واحد صحيح يدل على ظهور وبروز, tr:aslün vâhidün sahîhun yedüllü alâ zuhûrin ve burûz, gloss:görünüp ortaya çıkmayı gösterir, source:"ط ل ع,B001"}. Bir dağın tepesine tırmanmak ve tepeden aşağıya bakılan yerin dehşeti de bu köktendir {ar:طلعت الجبل أي علوته, tr:tala'tü'l-cebele ey alevtüh, gloss:dağa çıktım, yani üstüne yükseldim, source:"ط ل ع,B006"}, {ar:هول المطلع, tr:hevlü'l-muttala', gloss:tepeden bakılan yerin dehşeti, source:"ط ل ع,B006"}. Bir kabı ağzına kadar doldurmak da {ar:قدح طلاع ممتلىء, tr:kadahun tılâ'un mümteli', gloss:ağzına kadar dolu kap, source:"ط ل ع,B007"}. Ayetteki yapı da önemlidir: fiil "alâ" edatıyla gelir ve Arapçada aynı yapı bir topluluğun üstüne baskın yapmak için kullanılır {ar:طلع علينا فلان يطلع طلوعا إذا هجم, tr:tala'a aleynâ fülânün izâ hecem, gloss:falan üstümüze çıkageldi, yani baskın yaptı, source:"ط ل ع,B002"}. Ateş doğan bir güneş gibi belirir, bir tırmanıcı gibi yükselir, bir baskıncı gibi üstlerine gelir ve kabı doldurur gibi yükselir. Ateşin kökünde de kararsızca kıpırdayan ışık vardır {ar:أصل صحيح يدل على إضاءة واضطراب وقلة ثبات, tr:aslün sahîhun yedüllü alâ idâetin ve ıdtırâbin ve kılleti sebât, gloss:aydınlanma, çalkalanma ve sabit durmamayı gösterir, source:"ن و ر,B001"}.

Bu yükseliş bir hedefe yöneliktir. Beşinci ayetin {ar:أَدْرَىٰكَ, tr:edrâke, gloss:sana bildirdi, source:104:5} fiilinin kökü avcının ustalığını da taşır: avın yerini daha görmeden kollamak ve onu bir siper hayvanının ardından gizlice yaklaşarak aldatmak {ar:تدريت الصيد إذا نظرت أين هو ولم تره بعد ودريته ختلته, tr:tedarreytü's-sayde izâ nazartü eyne hüve ve lem erahü ba'd, gloss:avı henüz görmeden nerede olduğunu kolladım ve ona sinsice yaklaştım, source:"د ر ي,B003"}, {ar:الدرية الدابة التي يستتر بها الذي يرمي الصيد, tr:ed-dariyye ed-dâbbetü'lletî yesteteru bihe'llezî yermi's-sayd, gloss:avcının ardına saklandığı hayvan, source:"د ر ي,B003"}, nişan alıştırması yapılan halka {ar:الدريئة الحلقة التي يتعلم عليها الطعن, tr:ed-darî'e el-halkatü'lletî yute'allemu aleyhe't-ta'n, gloss:mızrak atmanın öğrenildiği halka, source:"د ر ي,B005"} ve bir yeri seçip baskın için ona yönelmek {ar:ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة, tr:iddarâ benû fülânin mekâne kezâ ey i'temedûhü bi-ğazvin ev ğâra, gloss:falan oğulları bir yeri seçip baskınla ona yöneldiler, source:"د ر ي,B002"}. Bu açıklamadaki "i'temedûhü", son ayetteki direklerin köküdür; o kökte kasten yönelmek de vardır {ar:العمد والتعمد خلاف السهو, tr:el-amd ve't-ta'ammüd hilâfü's-sehv, gloss:kasıt, yanılmanın zıddıdır, source:"ع م د,B001"}. İlk ayetin kökü güçlü atan yayı adlandırır {ar:قوس همزي شديدة الدفع للسهم, tr:kavsün hemezâ şedîdetü'd-def'i li's-sehm, gloss:oku güçlü iten yay, source:"ه م ز,B003"}; yedinci ayetin kökü düşmanı gözetlemek için önden gönderilen öncüleri {ar:الطليعة قوم يبعثون ليطلعوا طلع العدو, tr:et-talî'a kavmün yüb'asûne li-yattali'û tal'a'l-adüvv, gloss:düşmanın durumunu gözetlemek için gönderilen topluluk, source:"ط ل ع,B004"}; yüreklerin kökü avı kalbinden vurmayı {ar:فأدت الصيد إذا أصبت فؤاده, tr:fe'edtü's-sayde izâ esabtü fuâdeh, gloss:avı kalbinden vurdum, source:"ف ء د,B003"}. Aynı kökün bir dalı tersini de söyler: atıcının oku hedefin üstünden aşıp gider {ar:وأطلع الرامي أي جاز سهمه من فوق الغرض, tr:ve atla'a'r-râmî ey câze sehmühû min fevki'l-ğaraz, gloss:atıcı "atla'a" etti, yani oku hedefin üstünden geçti, source:"ط ل ع,B010"}. Surenin yükselişi aşmaz: {ar:عَلَى ٱلْأَفْـِٔدَةِ, tr:ale'l-ef'ide, gloss:yüreklerin üzerine, source:104:7} durur. Bunlar fiilin ayetteki anlamının yanında duyulan aile imgeleridir; ayetin kendisi ateşin yüreklere ulaştığını söyler.

Yükseliş, sekizinci ayette yukarıdan kapanan örtüyle biter: {ar:إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ, tr:innehâ aleyhim mü'sade, gloss:o, üzerlerine kapatılmıştır, source:104:8}; "aleyhim" yedinci ayetteki "alâ"yı tekrar eder. Kökün anlamı kapıyı kapatıp sıkıca örtmektir {ar:أوصدت الباب وآصدته أي أطبقته وأحكمته ومؤصدة مطبقة, tr:evsadtü'l-bâbe ve âsadtühû ey atbaktühû ve ahkemtüh, gloss:kapıyı kapadım, sıkıca örttüm; mü'sade üstü kapatılmış demektir, source:"و ص د,B001"}.

Kuran ateşe atılmayı ve ateşin onlara yönelişini başka yerlerde canlandırır. Furkan suresinde Allah {ar:إِذَا رَأَتْهُم مِّن مَّكَانٍۭ بَعِيدٍۢ سَمِعُوا۟ لَهَا تَغَيُّظًۭا وَزَفِيرًۭا, tr:izâ raethüm min mekânin ba'îdin semi'û lehâ teğayyuzan ve zefîrâ, gloss:onları uzaktan görünce, onun öfkeyle köpürüşünü ve uğultusunu duyarlar, source:25:12} der; ateş görür ve hedefine yönelir, ardından {ar:وَإِذَآ أُلْقُوا۟ مِنْهَا مَكَانًۭا ضَيِّقًۭا مُّقَرَّنِينَ دَعَوْا۟ هُنَالِكَ ثُبُورًۭا, tr:ve izâ ülkû minhâ mekânen dayyikan mukarranîne de'av hünâlike sübûrâ, gloss:bağlanmış olarak onun dar bir yerine atıldıklarında orada yok olmayı dilerler, source:25:13}. Mülk suresinde {ar:إِذَآ أُلْقُوا۟ فِيهَا سَمِعُوا۟ لَهَا شَهِيقًۭا وَهِىَ تَفُورُ, tr:izâ ülkû fîhâ semi'û lehâ şehîkan ve hiye tefûr, gloss:oraya atıldıklarında onun hırıltısını duyarlar, o kaynar, source:67:7}, {ar:تَكَادُ تَمَيَّزُ مِنَ ٱلْغَيْظِ, tr:tekâdü temeyyezü mine'l-ğayz, gloss:öfkeden neredeyse çatlayacaktır, source:67:8}. Yukarı yol kapalıdır: Hac suresinde {ar:كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَا مِنْ غَمٍّ أُعِيدُوا۟ فِيهَا, tr:küllemâ erâdû en yahrucû minhâ min ğammin u'îdû fîhâ, gloss:kederden oradan çıkmak istedikçe oraya geri döndürülürler, source:22:22}, Secde suresinde de aynı söz {source:32:20}. Atılmanın kendisi Kasas suresinde Firavun ve ordusu için anlatılır: {ar:فَأَخَذْنَٰهُ وَجُنُودَهُۥ فَنَبَذْنَٰهُمْ فِى ٱلْيَمِّ, tr:fe-ehaznâhü ve cünûdehû fe-nebeznâhüm fi'l-yemm, gloss:onu ve ordularını yakalayıp denize attık, source:28:40}. Aynı surede Firavun yükselmeyi ve tutuşturmayı tek cümlede ister: {ar:فَأَوْقِدْ لِى يَٰهَٰمَٰنُ عَلَى ٱلطِّينِ فَٱجْعَل لِّى صَرْحًۭا لَّعَلِّىٓ أَطَّلِعُ إِلَىٰٓ إِلَٰهِ مُوسَىٰ, tr:fe-evkıd lî yâ Hâmânü ale't-tîni fec'al lî sarhan le'allî ettali'u ilâ ilâhi Mûsâ, gloss:Haman, benim için çamurun üstünde ateş yak, bana bir kule yap; belki Musa'nın ilahına çıkıp bakarım, source:28:38}. İnsanın yaktığı ateşle kurulan kule yukarı çıkmak içindir; bu surede ise tutuşturulmuş ateşin kendisi yükselir. Saffat suresinde cennetteki bir kişi dünyadaki arkadaşını arar: {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettala'a fe-raâhü fî sevâi'l-cahîm, gloss:yukarıdan baktı ve onu cehennemin ortasında gördü, source:37:55}. Aynı fiil orada tepeden aşağı bakmaktır.

Kaynaklar: 104:4 لَيُنۢبَذَنَّ ن ب ذ B001; 104:7 تَطَّلِعُ ط ل ع B001; 104:7 تَطَّلِعُ ط ل ع B002; 104:7 تَطَّلِعُ ط ل ع B006; 104:7 تَطَّلِعُ ط ل ع B007; 104:7 تَطَّلِعُ ط ل ع B010; 104:7 تَطَّلِعُ ط ل ع B004; 104:6 نَارُ ن و ر B001; 104:5 أَدْرَىٰكَ د ر ي B003; 104:5 أَدْرَىٰكَ د ر ي B005; 104:5 أَدْرَىٰكَ د ر ي B002; 104:9 عَمَدٍ ع م د B001; 104:1 هُمَزَةٍ ه م ز B003; 104:7 ٱلْأَفْـِٔدَةِ ف ء د B003; 104:8 مُّؤْصَدَةٌۢ و ص د B001

## Kapatılmış yapı: kuşatma, kapı, direkler, bukağı

Sure bir kuşatma kelimesiyle açılır. {ar:لِّكُلِّ, tr:li-külli, gloss:her birine, source:104:1}, kökünde kuşatmanın adıdır {ar:كل اسم موضوع للإحاطة مضاف أبدا, tr:küllün ismün mevdû'un li'l-ihâta, gloss:"küll" kuşatma için konmuş bir isimdir, source:"ك ل ل,B003"}; bir şeyin parçalarını bir araya toplar {ar:لفظ كل هو لضم أجزاء الشيء ويفيد معنى التمام, tr:lafzu küllin hüve li-dammi eczâi'ş-şey', gloss:"küll" bir şeyin parçalarını birleştirir ve tamlık bildirir, source:"ك ل ل,B003"}. Aynı kök bir şeyin çevresine geçirilen halkayı ve bir yeri çevreleyen bulutu {ar:الإكليل سمي بذلك لإطافته بالرأس, tr:el-iklîl summiye bi-zâlike li-itâfetihî bi'r-re's, gloss:taç, başı çevrelediği için böyle adlanmıştır, source:"ك ل ل,B005"}, ev gibi dikilen ince bir perdeyi de adlandırır {ar:الكلة الستر الرقيق يخاط كالبيت يتوقى فيه من البق, tr:el-kille es-sitrü'r-rakîk yuhâtu ke'l-beyt, gloss:sivrisinekten korunmak için ev gibi dikilen ince perde, source:"ك ل ل,B006"}. Kökte barınak olan şey, surede kuşatmaya döner. İlk kelimenin "her" anlamı yerinde durur; aile imgesi, kimsenin dışarıda kalmadığı bir halkanın sesini getirir.

Sure bir yapıyla kapanır. {ar:مُّؤْصَدَةٌۭ, tr:mü'sade, gloss:kapatılmış, source:104:8} kökü bir şeyi bir şeye kapatmaktır {ar:أصل يدل على ضم شيء إلى شيء, tr:aslün yedüllü alâ dammi şey'in ilâ şey', gloss:bir şeyi bir şeye kapatmayı gösterir, source:"و ص د,B001"}: kapı kapanır, kapak bastırılır {ar:أوصدت الباب أغلقته والموصد المطبق, tr:evsadtü'l-bâbe ağlaktühû ve'l-mûsad el-mutbak, gloss:kapıyı kapattım; mûsad üstü örtülmüş olandır, source:"و ص د,B001"}. Kök evin eşiğini ve kapısını da adlandırır {ar:الوصيد فناء البيت والوصيد الباب, tr:el-vasîd finâü'l-beyt ve'l-vasîd el-bâb, gloss:vasîd evin avlusu ve kapısıdır, source:"و ص د,B002"}. Sesçe komşu bir kökte surenin kendi birleşimi geçer {ar:نار مُؤصدة أي مطبقة, tr:nârun mü'sadetün ey mutbaka, gloss:üstü kapatılmış ateş, source:"ء ص د,B001"}; bu komşuluk yalnızca bir yankıdır.

Son ayette direkler dikilir. {ar:عَمَدٍۢ, tr:amed, gloss:direkler, source:104:9} çadırın ortasındaki direktir, evin direğidir, mermer sütunlardır {ar:عمود الخباء من خشب قائم في الوسط, tr:amûdü'l-hibâ' min haşebin kâimin fi'l-vasat, gloss:çadırın ortasında duran tahta direk, source:"ع م د,B003"}, {ar:العمد أساطين الرخام وفي عمد من النار, tr:el-amed esâtînü'r-ruhâm ve fî amedin mine'n-nâr, gloss:amed mermer sütunlardır; "ateşten direkler içinde", source:"ع م د,B003"}. {ar:مُّمَدَّدَةٍۭ, tr:mümeddede, gloss:uzatılmış, source:104:9} uzunlamasına çekmek, bir ipi germektir {ar:مددت الشيء ومددت الحبل فامتد, tr:medadtü'ş-şey'e ve medadtü'l-habla fe'mtedd, gloss:şeyi çektim, ipi gerdim, gerildi, source:"م د د,B001"}; çadır da direklerle ve gerilen iplerle kurulur. Sahne kapanmış bir çadır ya da evdir; barınağın kelimeleri, sinek perdesi, eşik ve direk, bir hapishaneye çevrilmiştir. Toplayan ellerin de kökte bir sonu vardır: bukağıya, elleri boyna topladığı için "câmia" denir {ar:الجامعة الغل لأنها تجمع اليدين إلى العنق, tr:el-câmi'a el-ğull li-ennehâ tecme'u'l-yedeyni ile'l-unuk, gloss:câmia, elleri boyna topladığı için bukağıdır, source:"ج م ع,B008"}. İkinci ayetin "topladı"sı, bu ailede ellerin boyna toplanmasını da duyurur.

Kuran bu kapalı ateşi aynı sözlerle anar. Beled suresinde Allah sol tarafın halkı için {ar:عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ, tr:aleyhim nârun mü'sade, gloss:üzerlerinde kapatılmış bir ateş vardır, source:90:20} der; aynı sure, gördüğümüz gibi, "eyahsebü" ve malla açılır. Kehf suresinde Allah {ar:إِنَّآ أَعْتَدْنَا لِلظَّٰلِمِينَ نَارًا أَحَاطَ بِهِمْ سُرَادِقُهَا, tr:innâ a'tednâ li'z-zâlimîne nâran ehâta bihim surâdikuhâ, gloss:zalimler için çadır duvarı onları kuşatan bir ateş hazırladık, source:18:29} der; "surâdık" bir çadırın çevresindeki perde duvarıdır ve kuşatma burada da bir çadır biçimindedir. Ankebut suresinde {ar:وَإِنَّ جَهَنَّمَ لَمُحِيطَةٌۢ بِٱلْكَٰفِرِينَ, tr:ve inne cehenneme le-muhîtatün bi'l-kâfirîn, gloss:cehennem inkârcıları kuşatmıştır, source:29:54}. Hicr suresinde cehennemin kapıları vardır: {ar:لَهَا سَبْعَةُ أَبْوَٰبٍۢ, tr:lehâ seb'atü ebvâb, gloss:onun yedi kapısı vardır, source:15:44}. Hakka suresinde malının işe yaramadığını söyleyen adam için emir gelir: {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhü fe-ğullûh, gloss:tutun onu ve bukağılayın, source:69:30}, {ar:ثُمَّ فِى سِلْسِلَةٍۢ ذَرْعُهَا سَبْعُونَ ذِرَاعًۭا فَٱسْلُكُوهُ, tr:sümme fî silsiletin zer'uhâ seb'ûne zirâ'an feslükûh, gloss:sonra onu yetmiş arşın uzunluğunda bir zincire geçirin, source:69:32}. Malına güvenen bağlanır ve uzun bir zincire geçirilir. İsra suresinde Allah cimriliği bağlı bir elle anlatır: {ar:وَلَا تَجْعَلْ يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:ve lâ tec'al yedeke mağlûleten ilâ unukik, gloss:elini boynuna bağlı kılma, source:17:29}. Al-i İmran suresinde cimrilerin esirgediği mal boyunlarına geçirilir: {ar:سَيُطَوَّقُونَ مَا بَخِلُوا۟ بِهِۦ يَوْمَ ٱلْقِيَٰمَةِ, tr:se-yutavvakûne mâ bahilû bihî yevme'l-kıyâme, gloss:esirgedikleri şey kıyamet günü boyunlarına dolanacak, source:3:180}. Yasin suresinde {ar:إِنَّا جَعَلْنَا فِىٓ أَعْنَٰقِهِمْ أَغْلَٰلًۭا فَهِىَ إِلَى ٱلْأَذْقَانِ, tr:innâ ce'alnâ fî a'nâkıhim ağlâlen fe-hiye ile'l-ezkân, gloss:boyunlarına çenelerine kadar bukağılar geçirdik, source:36:8}. Direklerin karşısında Ra'd suresi gökleri direksiz yükseltilmiş olarak anar: {ar:ٱللَّهُ ٱلَّذِى رَفَعَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا, tr:allâhüllezî refe'a's-semâvâti bi-ğayri amedin teravnehâ, gloss:Allah gökleri görebileceğiniz direkler olmadan yükseltendir, source:13:2}. Göğün görünür direği yoktur; ateşin ise direkleri vardır ve uzatılmıştır. Fecr suresindeki direkler sahibi İrem de {source:89:7} kalıcılık için dikilmiş direkleri hatırlatır. Kehf suresinde ise eşik bir sığınağın eşiğidir: mağaradakilerin köpeği {ar:وَكَلْبُهُم بَٰسِطٌۭ ذِرَاعَيْهِ بِٱلْوَصِيدِ, tr:ve kelbühüm bâsitun zirâ'ayhi bi'l-vasîd, gloss:köpekleri eşikte ön ayaklarını uzatmış yatıyordu, source:18:18}. Aynı ayette {ar:لَوِ ٱطَّلَعْتَ عَلَيْهِمْ لَوَلَّيْتَ مِنْهُمْ فِرَارًۭا, tr:levi'ttala'te aleyhim le-vellayte minhüm firârâ, gloss:üstlerine bakıp görseydin onlardan kaçarak dönerdin, source:18:18} denir; bir önceki ayette doğan güneş mağaralarından sağa doğru sapar {ar:وَتَرَى ٱلشَّمْسَ إِذَا طَلَعَت تَّزَٰوَرُ عَن كَهْفِهِمْ ذَاتَ ٱلْيَمِينِ, tr:ve tere'ş-şemse izâ tala'at tezâveru an kehfihim zâte'l-yemîn, gloss:güneşi doğduğunda mağaralarından sağa doğru eğilirken görürsün, source:18:17}. Mağarada eşik korur ve doğan güneş sığınanlardan sapar; bu surede kapı kapanır ve yükselen ateş yüreklerin üstüne çıkar.

Kaynaklar: 104:1 لِّكُلِّ ك ل ل B003; 104:1 لِّكُلِّ ك ل ل B005; 104:1 لِّكُلِّ ك ل ل B006; 104:8 مُّؤْصَدَةٌۢ و ص د B001; 104:8 مُّؤْصَدَةٌۢ و ص د B002; 104:8 مُّؤْصَدَةٌۢ ء ص د B001; 104:9 عَمَدٍ ع م د B003; 104:9 مُّمَدَّدَةٍۭ م د د B001; 104:2 جَمَعَ ج م ع B008

## Buluşmalar

İlk ayetteki iki kelime iki imgeyi aynı anda taşır: el ve dil. İtme ifadesi ile gıyap ve huzur ifadesi aynı iki kelimeyi birleştirir. Mümtehine suresindeki ayet, ellerin ve dillerin birlikte kötülükle uzatılmasını {source:60:2} söyleyerek bu ikisini tek sahnede toplar. Sıkan, iten, kusur arayan ve arkadan dürten kişi, ikinci ayette malın üstüne kapanan yumruğa dönüşür. Kökte o yumruğun sonu bukağıdır, ellerin boyna toplanması {source:"ج م ع,B008"}. Hakka suresinde malının işe yaramadığını söyleyen adam bukağılanır {source:69:30}. Toplayan el ile bağlanan el, aynı kökün iki ucudur.

Sayma ile yaslanma üçüncü ayetin bir tek fiilinde buluşur: "yahsebü" hem saymanın hem yeterliğin köküdür, kalıcılık fiili de sanarak yaslanmak diye açıklanır. Tevbe suresindeki {ar:خَٰلِدِينَ فِيهَا ۚ هِىَ حَسْبُهُمْ, tr:hâlidîne fîhâ, hiye hasbühüm, gloss:orada kalıcı olarak; o onlara yeter, source:9:68} sözü, adamın mala yüklediği iki şeyi, kalıcılığı ve yeterliği, ateşe verir. Aynı iki imge su sahnesiyle de buluşur: sayma kökündeki kesilmeyen su, adamın sandığı süreklilik; kırıcının kökündeki tükenen mal, bu sürekliliğin sonu. Kehf suresindeki bahçe sahibi bu yolu baştan sona yürür: bahçesinin arasından nehir akar, bahçenin yok olmayacağını sanır, sanma fiiliyle aynı kökten bir "husban" bahçeyi vurur ve avuçları boş kalır {source:18:40}. Hadid suresi aynı yolu mal çoğaltma yarışının benzetmesi yapar ve "hutam" ile bitirir {source:57:20}.

Kalıcılık ile ocak arasında bir buluşma daha vardır: kalıcılık kökünde "kalıcılar" diye anılan tek şey ocak taşlarıdır. Kendini kalıcı sanan adam, ateşin altında yıllarca kalan taşların adını taşıyan bir fiille konuşur. Kalıcılık kökünün bir dalı da kalbe gider: sanı, kalpte yerleşik olan gönüle düşer. Ocak ile yürek de iki kez birleşir: yürek tutuşmayla adlandırılır ve yüreklerin kökü ateş yakmanın fiiliyle açıklanır. Altıncı ve yedinci ayetler bu yüzden bir sıfat ile onun yerini ardı ardına söyler: tutuşturulmuş ateş, tutuşmayla adlanan yüreğe çıkar. Sanının oturduğu yer, ateşin vardığı yerdir.

Sürü ile kapalı yapı sekizinci ayetin kelimesinde buluşur: aynı kök mal için dağda yapılan taş ağılı ve üstü kapatılmış ateşi adlandırır. Sürüyü ağıla kapatan adam, kapatılmış bir ateşin içindedir. Sürü ile ateş damgada buluşur: devenin ateşi damgasıdır, Tevbe suresinde biriktirilen hazine kızdırılıp alınlara basılır {source:9:35}, Kalem suresinde mal ve oğullar sahibi hemmâz burnundan damgalanır {source:68:16}. Bu son ayet ilk imge ile sürüyü birbirine bağlar: iğneleyen dil, mal ve damga aynı adamdadır.

Yükselen ateş ile avcı, aynı kökün iki dalında buluşur: ateşin yükselişini anlatan fiil, okun hedefin üstünden aşmasını da adlandırır ve bu ateş aşmaz, yüreklerin üstünde durur. Avcının kolladığı yer yürektir; yüreklerin kökü avı kalbinden vurmaktır. Bilmek ile avcılık da beşinci ayetin fiilinde aynı köktür: görmeden kollamak ve bilmek. Sanan adam ile içini bilen ateş arasındaki mesafeyi, "ne bildirdi" sorusu kapatır ve cevabı Allah'ın ateşi olarak verir.

Surenin hareketi bu buluşmalarla taşınır. İlk iki ayette her şey adamın elindedir: sıkan, iten, toplayan, sayan bir el ve onu yaralayan bir dil. Üçüncü ayette bu el bir sanıya dayanır ve kalbe yerleşir. Dördüncü ayetten sonra yön tersine döner: el açılır ve atılan adamın kendisidir; topladığı malın adı kırıntı olur, saydığı sayı onu saymaz, dayandığı direkler onu tutar, sürüsünü kapattığı ağıl üzerine kapanır. Ateş aşağıdan yükselir ve sanının oturduğu yüreğe ulaşır. İlk ayetteki kuşatma kelimesinden son ayetteki direklere kadar sure, dışarıya uzanan bir elden içeriye kapanan bir yapıya doğru ilerler.

