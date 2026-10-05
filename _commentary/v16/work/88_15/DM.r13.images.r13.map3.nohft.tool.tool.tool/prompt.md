Focus: 88:15. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_15/D.r13/context.md =====
# 88:15 — focus

وَنَمَارِقُ مَصْفُوفَةٌۭ

Anchor translation (canonical reading, reference only):

Dizilmiş yastıklar da vardır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَنَمَارِقُ | نَمَارِق |  | CONJ;N |
| 2 | مَصْفُوفَةٌ | مَصْفُوفَة | ص ف ف | ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 88 — full text (context; no pericope)

- 88:1 هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ
- 88:2 وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ
- 88:3 عَامِلَةٌۭ نَّاصِبَةٌۭ
- 88:4 تَصْلَىٰ نَارًا حَامِيَةًۭ
- 88:5 تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
- 88:6 لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
- 88:7 لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
- 88:8 وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ
- 88:9 لِّسَعْيِهَا رَاضِيَةٌۭ
- 88:10 فِى جَنَّةٍ عَالِيَةٍۢ
- 88:11 لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ
- 88:12 فِيهَا عَيْنٌۭ جَارِيَةٌۭ
- 88:13 فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ
- 88:14 وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ
- 88:15 ◀ focus وَنَمَارِقُ مَصْفُوفَةٌۭ
- 88:16 وَزَرَابِىُّ مَبْثُوثَةٌ
- 88:17 أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ
- 88:18 وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ
- 88:19 وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- 88:20 وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- 88:21 فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- 88:22 لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 88:23 إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- 88:24 فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_15/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ص ف ف (root_000871) — identity root of مَصْفُوفَةٌ (w2)

- **B001** düz bir sıra oluşturma — düz çizgi üzerinde yan yana duran ögelerden oluşan sıra · yan yana sıraya dizmek · yan yana sıraya girmek · sıra halinde duran; kanatlarını açıp sabit tutan · savaş sırasının kurulduğu mevki · sıra halinde dizilmiş
  الصف معروف (ayn;tahdhib); الصف أن تجعل الشيء على خط مستو (mufradat); صففت القوم فاصطفوا (ayn;sihah;tahdhib); المصف الموقف والجمع المصاف (ayn;sihah;tahdhib); الصافات صفا يعني الملائكة (mufradat;tahdhib); الطير الصواف التي تصف أجنحتها فلا تحركها (ayn;tahdhib); البدن الصواف التي تصفف ثم تنحر (ayn;tahdhib)
- **B002** bir sağımda birden çok kabı dolduran ya da ön ayaklarını hizalayan dişi deve — bir sağımda birden çok kabı dolduran ya da ön ayaklarını hizalayan dişi deve · dişi deveyi tek sağımda iki veya üç kaba sağma
  الصفوف الناقة التي تجمع بين محلبين في حلبة (maqayis;tahdhib); الصف أن تحلب الناقة في محلبين أو ثلاثة تصف بينها (sihah); ناقة صفوف للتي تصف أقداحا من لبنها (sihah); الصفوف ناقة تصف بين محلبين فصاعدا لغزارتها (mufradat); الصفوف أيضا التي تصف يديها عند الحلب (maqayis;sihah;tahdhib)
- **B003** kurutmak ya da közlemek için sıra sıra serilmiş et — güneşte kurutulmak veya közde pişirilmek üzere sıra sıra serilmiş et · eti şeritlere ayırıp sıra sıra sermek · eti genişletip inceltecek biçimde dilimleme
  الصفيف قال قوم هو القديد (maqayis); اللحم يحمل في الأسفار طبيخا أو شواء فلا ينضج (maqayis); الصفيف القديد اذا شر في الشمس (ayn;tahdhib); الصفيف ما صف من اللحم على الجمر لينشوي (sihah); صففت اللحم قددته وألقيته صفا صفا (mufradat); التصفيف نحو التشريح (tahdhib)
- **B004** yapı ya da eyer bölümü — yapıda ya da eyerde bulunan bölüm veya düzenek · hayvan için eyer düzeneği yapmak
  الصفة من البنيان والسرج ايضا (ayn); صفة الدار والسرج واحدة الصفف (sihah); صفة السرج (tahdhib); صففت للدابة صفة أي عملتها له (tahdhib); الصفة من البنيان وصفة السرج (mufradat)
- **B005** düz ve pürüzsüz arazi — düz ve pürüzsüz, kimi kullanımda bitkisiz arazi · düz ve pürüzsüz araziler
  الصفصف وهو المستوي من الأرض (maqayis); الصفصف الفلاة المستوية الملساء (ayn); الصفصف المستوى من الأرض (sihah); الصفصف الذي لا نبات فيه (tahdhib); الصفصف القرعاء (tahdhib); الصفصف المستوي الأملس (tahdhib); الصفصف المستوي من الأرض كأنه على صف واحد (mufradat)
- **B006** söğüt ağacı — söğüt ağacı
  الصفصف شجر الخلاف الواحدة بالهاء (ayn); الصفصاف شجر الخلاف (sihah;mufradat); الصفصاف الخلاف (tahdhib); هو شجر الخلاف بلغة أهل الشام (tahdhib)
- **B007** su başında toplanma [kalıp] — su başında toplanmak · su başında toplanmak
  تضافوا على الماء وتصافوا عليه بمعنى واحد إذا اجتمعوا عليه (tahdhib)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:15, and ## Buluşmalar) =====
## Döşenen oda, döşenen dünya

On üçüncü ayetten on altıncıya kadar bir oda döşenir. Dört eşya vardır ve her birine yapılmış bir işi gösteren bir sıfat verilir: {ar:فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ, tr:fîhâ sururun merfûa, gloss:orada kaldırılmış sedirler, source:88:13}; {ar:وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ, tr:ve ekvâbun mevdûa, gloss:konmuş kadehler, source:88:14}; {ar:وَنَمَارِقُ مَصْفُوفَةٌۭ, tr:ve nemâriku masfûfe, gloss:sıra sıra dizilmiş yastıklar, source:88:15}; {ar:وَزَرَابِىُّ مَبْثُوثَةٌ, tr:ve zerâbiyyu mebsûse, gloss:serilmiş halılar, source:88:16}. Bunlar kaldırmak, koymak, dizmek ve sermektir. On yedinci ayetten yirminciye kadar ise dünya döşenir: dört nesne ve edilgen dört fiil gelir. Deve yaratılmış, gök kaldırılmış, dağlar dikilmiş, yer düzlenmiştir. Aynı el hareketleri hem bir odayı hem bir dünyayı kurar.

Kaldırmak iki listede de geçer. Tanımı koymayı da içinde taşır: {ar:الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها, tr:er-ref'u yukâlü fi'l-ecsâmi'l-mevdûati izâ a'leytehâ an makarrihâ, gloss:konmuş cisimleri yerlerinden yukarı aldığında ref' denir, source:"ر ف ع,B001"}. Yapı için de kullanılır: {ar:في البناء إذا طولته, tr:fi'l-binâi izâ tavveltehû, gloss:binada yükselttiğinde, source:"ر ف ع,B001"}. Gök, bir evin tavanı gibi kaldırılmıştır: {ar:السماء سقف البيت وكل عال مطل سماء, tr:es-semâu sakfu'l-beyt ve küllü âlin mutıllin semâ', gloss:sema evin tavanıdır; yüksekten bakan her şey semadır, source:"س م و,B004"}. Dağların fiili olan dikmek, kadehlerin fiili olan koymak üzerinden tanımlanır: {ar:نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر, tr:nasbu'ş-şey'i vad'uhû vad'an nâti'en ke-nasbi'r-rumhi ve'l-binâi ve'l-hacer, gloss:bir şeyi dikmek onu çıkıntılı biçimde koymaktır; mızrak bina ve taş dikmek gibi, source:"ن ص ب,B001"}. Dikmenin aslında doğruluk vardır: {ar:أصل صحيح يدل على إقامة شيء وإهداف في استواء, tr:aslun sahîhun yedullü alâ ikâmeti şey'in ve ihdâfin fi'stivâ', gloss:bir şeyi dikip düzgünce yükseltmeyi gösteren kök, source:"ن ص ب,B001"}. Dağlar yerin kazıklarıdır: {ar:اسم لكل وتد من أوتاد الأرض إذا عظم وطال, tr:ismun li-külli vetedin min evtâdi'l-ardi izâ azume ve tâl, gloss:yerin kazıklarından büyüyüp uzayan her birinin adı, source:"ج ب ل,B001"}. Yer de düz bir dam gibi yayılmıştır: {ar:سطح الله الأرض سطحا بسطها, tr:satahallâhu'l-arda sathan besatahâ, gloss:Allah yeri düzledi yani yaydı, source:"س ط ح,B001"}; {ar:السطح ظهر البيت إذا كان مستويا, tr:es-sathu zahru'l-beyti izâ kâne müsteviyen, gloss:satıh evin düz olan damıdır, source:"س ط ح,B001"}; {ar:سطحت المكان جعلته في التسوية كسطح, tr:satahtü'l-mekâne cealtühû fi't-tesviyeti ke-sath, gloss:yeri bir dam gibi düz yaptım, source:"س ط ح,B001"}. Aynı kök çadır direğine de ad verir: {ar:المسطح عمود الخيمة الذي يجعل به لها سطحا, tr:el-mistahu amûdü'l-hayme'llezî yüc'alu bihî lehâ sathan, gloss:çadıra düz bir üst veren direk, source:"س ط ح,B003"}. Bu anlam ayetin yanında duyulduğunda dünya bir çadıra benzer: yükseltilmiş bir tavanı, kazıkları ve serilmiş bir zemini vardır.

İki listeyi birbirine bağlayan kelimeler de vardır. Yastıkların dizildiği sıra düz bir çizgidir: {ar:الصف أن تجعل الشيء على خط مستو, tr:es-saffu en tec'ale'ş-şey'e alâ hattın müstevin, gloss:saf bir şeyi düz bir çizgiye koymaktır, source:"ص ف ف,B001"}. Aynı kelime düz arazi için de kullanılır: {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsafu'l-müstevî mine'l-ardi keennehû alâ saffin vâhid, gloss:tek bir saf üstündeymiş gibi düz yer, source:"ص ف ف,B005"}. Halıların serilmesini anlatan fiil, canlıların yere yayılmasını da anlatır: {ar:بثت البسط, tr:bussetil-busut, gloss:halılar serildi, source:"ب ث ث,B001"}; {ar:خلق الخلق وبثهم في الأرض, tr:halaka'l-halka ve besse-hum fi'l-ard, gloss:yaratılmışları yarattı ve yeryüzüne yaydı, source:"ب ث ث,B001"}. Bu ikinci cümlede on yedinci ayetteki yaratma ile yirminci ayetteki yer bir aradadır. Yerin kökü kalın bir halıya da ad verir: {ar:الإراض بساط ضخم من وبر أو صوف, tr:el-irâdu bisâtun dahmun min veberin ev sûf, gloss:deve tüyünden ya da yünden kalın bir yaygı, source:"ء ر ض,B005"}. Bu, on altıncı ayetteki halıların hemen yanında duyulur.

Yaratmak da bir ustanın ilk hareketidir: ölçmek. {ar:خلقت الأديم للسقاء إذا قدرته, tr:halaktü'l-edîme li's-sikâi izâ kaddertüh, gloss:deriyi tulum yapmak için ölçtüm, source:"خ ل ق,B001"}; {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhû et-takdîru'l-müstakîm, gloss:yaratmanın aslı doğru ölçüdür, source:"خ ل ق,B001"}. Aynı kök düzleştirmeyi de anlatır: {ar:صخرة خلقاء ملساء, tr:sahratun halkâu melsâ', gloss:dümdüz ve kaygan kaya, source:"خ ل ق,B008"}. Böylece dört fiilin dördü de ölçüye ve düzlüğe dayanır: doğru ölçü, düzgünce dikmek, dam gibi düzlemek ve aynı ölçünün sırası. Kur'an da yaratmayı düzenlemeyle birlikte söyler. Önceki sure {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî halaka fe-sevvâ, gloss:yaratıp düzenleyen, source:87:2} der. İnsana da şöyle seslenilir: {ar:ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ, tr:ellezî halakake fe-sevvâke fe-adeleke, gloss:seni yaratıp düzenleyen ve dengeli kılan, source:82:7}.

Kur'an kaldırma ile koymayı yan yana koyar. Rahman nimetlerini sayarken şöyle der: {ar:وَٱلسَّمَآءَ رَفَعَهَا وَوَضَعَ ٱلْمِيزَانَ, tr:ve's-semâe rafeahâ ve vada'a'l-mîzân, gloss:göğü kaldırdı ve teraziyi koydu, source:55:7}; {ar:وَٱلْأَرْضَ وَضَعَهَا لِلْأَنَامِ, tr:ve'l-arda vada'ahâ li'l-enâm, gloss:yeri de yaratılmışlar için koydu, source:55:10}. Dirilişi inkâr edenlere sorulan soruda göğün yapısı şöyle anlatılır: {ar:رَفَعَ سَمْكَهَا فَسَوَّىٰهَا, tr:rafea semkehâ fe-sevvâhâ, gloss:tavanını yükseltip düzenledi, source:79:28}. Yerin döşenmesi de aynı resmi sürdürür: {ar:أَلَمْ نَجْعَلِ ٱلْأَرْضَ مِهَٰدًۭا, tr:e-lem nec'ali'l-arda mihâdâ, gloss:yeri bir döşek yapmadık mı, source:78:6}; {ar:وَٱلْجِبَالَ أَوْتَادًۭا, tr:ve'l-cibâle evtâdâ, gloss:dağları da kazıklar, source:78:7}; {ar:وَٱلْأَرْضَ فَرَشْنَٰهَا فَنِعْمَ ٱلْمَٰهِدُونَ, tr:ve'l-arda feraşnâhâ fe-ni'me'l-mâhidûn, gloss:yeri döşedik; ne güzel döşeyiciyiz, source:51:48}. Nuh da kavmine {ar:وَٱللَّهُ جَعَلَ لَكُمُ ٱلْأَرْضَ بِسَاطًۭا, tr:vallâhu ceale lekumu'l-arda bisâtâ, gloss:Allah yeri sizin için bir yaygı yaptı, source:71:19} der. Gök bir tavandır: {ar:وَجَعَلْنَا ٱلسَّمَآءَ سَقْفًۭا مَّحْفُوظًۭا ۖ وَهُمْ عَنْ ءَايَٰتِهَا مُعْرِضُونَ, tr:ve cealne's-semâe sakfen mahfûzan ve hum an âyâtihâ mu'ridûn, gloss:göğü korunmuş bir tavan yaptık; onlar ise onun işaretlerinden yüz çeviriyorlar, source:21:32}. Tur suresi de bir yemin olarak {ar:وَٱلسَّقْفِ ٱلْمَرْفُوعِ, tr:ve's-sakfi'l-merfû', gloss:yükseltilmiş tavana andolsun, source:52:5} der. Bu çadırın direği yoktur: {ar:ٱللَّهُ ٱلَّذِى رَفَعَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا, tr:Allâhullezî rafea's-semâvâti bi-ğayri amedin teravnehâ, gloss:gökleri görebileceğiniz direkler olmadan yükselten Allah, source:13:2}. Yayma fiili de iki yönde kullanılır: {ar:وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ, tr:ve besse fîhâ min külli dâbbe, gloss:orada her türlü canlıyı yaydı, source:31:10}. O gün ise yayılan insanlardır, halılar değil: {ar:يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ, tr:yevme yekûnu'n-nâsu ke'l-ferâşi'l-mebsûs, gloss:insanların saçılmış pervaneler gibi olacağı gün, source:101:4}. Bahçenin odası da başka yerlerde aynı kelimelerle döşenir: {ar:مُتَّكِـِٔينَ عَلَىٰ سُرُرٍۢ مَّصْفُوفَةٍۢ, tr:muttekiîne alâ sururin masfûfe, gloss:dizili sedirlere yaslanmış, source:52:20}; {ar:وَفُرُشٍۢ مَّرْفُوعَةٍ, tr:ve furuşin merfûa, gloss:yükseltilmiş döşekler, source:56:34}; {ar:إِخْوَٰنًا عَلَىٰ سُرُرٍۢ مُّتَقَٰبِلِينَ, tr:ihvânen alâ sururin mutekâbilîn, gloss:sedirler üstünde karşılıklı kardeşler olarak, source:15:47}.

Kaynaklar: 88:13 مَّرْفُوعَةٌ ر ف ع B001; 88:14 مَّوْضُوعَةٌ و ض ع B001; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:15 مَصْفُوفَةٌ ص ف ف B005; 88:16 مَبْثُوثَةٌ ب ث ث B001; 88:17 خُلِقَتْ خ ل ق B001; 88:17 خُلِقَتْ خ ل ق B008; 88:18 ٱلسَّمَآءِ س م و B004; 88:18 رُفِعَتْ ر ف ع B001; 88:19 نُصِبَتْ ن ص ب B001; 88:19 ٱلْجِبَالِ ج ب ل B001; 88:20 سُطِحَتْ س ط ح B001; 88:20 سُطِحَتْ س ط ح B003; 88:20 ٱلْأَرْضِ ء ر ض B005

## Deve: sürü, süt ve yolculuk

Bakılacak dört şeyin ilki devedir. Gök, dağlar ve yer uzaktadır. Deve ise insanın yanındadır, insan onun üstündedir. Arapçada deve bir servettir: {ar:الإبل معروفة ورجل آبل ومال مؤبل, tr:el-ibilu ma'rûfetun ve racülün âbilün ve mâlün muebbel, gloss:deve bilinir; develi adam ve deveden oluşan mal, source:"ء ب ل,B001"}. Kökün bir kolu devenin suya muhtaç kalmadan yaşı otla yetinmesini anlatır: {ar:أبلت الإبل والوحش اجتزأت بالرطب عن الماء, tr:ebeleti'l-ibilu ve'l-vahşu'ctezeet bi'r-ratbi ani'l-mâ', gloss:develer ve yaban hayvanları sudan vazgeçip yaş otla yetindi, source:"ء ب ل,B002"}. Altıncı ve yedinci ayetlerde hiçbir şeyin yetmediği insanlar vardır. On yedinci ayette ise azla yetinen bir hayvana bakılması istenir.

Surenin önceki kelimelerinde de devenin bedeni yan anlam olarak duyulur. Nâime'nin kökü sürüye ad verir: {ar:النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم, tr:en-neamu'l-ibilu limâ fîhi mine'l-hayri ve'n-ni'meti ve'l-en'âmu'l-behâim, gloss:neam devedir; içindeki hayır ve nimetten dolayı; en'âm hayvanlardır, source:"ن ع م,B005"}. Hâşia, yorgun düşmüş bir devenin hörgücünü anlatır: {ar:خشع سنام البعير إذا أنضي فذهب شحمه وتطأطأ شرفه, tr:haşaa senâmü'l-baîri izâ undiye fe-zehebe şahmuhû ve teta'tae şerefuh, gloss:yorulan devenin hörgücünün yağı gidip tepesi çöktü, source:"خ ش ع,B004"}. Âmile, çalışmaya yatkın soylu dişi deveye ad verir: {ar:اليعملة الناقة النجيبة المطبوعة على العمل, tr:el-ya'meletü'n-nâkatü'n-necîbetü'l-matbûatu ale'l-amel, gloss:çalışmaya yaratılışça yatkın soylu dişi deve, source:"ع م ل,B008"}. Ateşe girme fiilinin kökü bir bitkiye de ad verir: {ar:تسميها العرب خبزة الإبل, tr:tüsemmîhe'l-arabu hubzete'l-ibil, gloss:Araplar ona develerin ekmeği der, source:"ص ل ي,B010"}. Yemek, yağ ve deve tek bir cümlede birleşir: {ar:المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن, tr:el-mut'imu mine'l-ibili'llezî yûcedu fî muhhihî ta'mu'ş-şahm ve şâtun taûmun fîhâ ba'du's-simen, gloss:iliğinde yağ tadı bulunan deve; biraz semizliği olan koyun, source:"ط ع م,B007"}. Mevdûa'nın kökü tuzlu otlakta yayılan develeri anlatır: {ar:الواضعات الإبل تأكل الخلة, tr:el-vâdiâtü'l-ibilu te'kulu'l-hulle, gloss:vâdiât hulle otunu yiyen develerdir, source:"و ض ع,B007"}. Masfûfe ise kurban için sıraya dizilen develeri anlatır: {ar:البدن الصواف التي تصفف ثم تنحر, tr:el-budnü's-savâffu'lletî tusaffefu summe tunhar, gloss:sıraya dizilip sonra kesilen kurbanlık develer, source:"ص ف ف,B001"}. Kur'an aynı kelimeyi kurbanlık develer için kullanır: {ar:فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ, tr:fezkurusmallâhi aleyhâ savâff, gloss:sıraya dizilmişken üzerlerine Allah'ın adını anın, source:22:36}. O ayette sıra, anma ve doyurma bir aradadır. Ayet ardından {ar:وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ, tr:ve at'imu'l-kânia ve'l-mu'terr, gloss:yetineni ve isteyeni doyurun, source:22:36} der.

Süt de aynı kelimelerden geçer. Darî'in kökü memedir: {ar:الضرع لكل ذات خف أو ظلف, tr:ed-dar'u li-külli zâti huffin ev zılf, gloss:dar' tabanlı ve tırnaklı her hayvanın memesidir, source:"ض ر ع,B001"}. Merfûa'nın kökü sütünü memesinde tutan deveye ad verir: {ar:ناقة رافع إذا رفعت اللبأ في ضرعها, tr:nâkatun râfiun izâ rafeati'l-lebee fî dar'ihâ, gloss:ağız sütünü memesinde tutan dişi deveye râfi' denir, source:"ر ف ع,B007"}. Masfûfe'nin kökü tek sağımda kadehleri sıra sıra dolduran deveye ad verir: {ar:ناقة صفوف للتي تصف أقداحا من لبنها, tr:nâkatun safûfun li'lletî tesuffu akdâhan min lebenihâ, gloss:sütünden kadehleri sıra sıra dolduran dişi deve, source:"ص ف ف,B002"}. On dördüncü ayetteki kevb de böyle bir kadehtir. Besleme kelimesinin kökü sütten çıkan yağa ad verir: {ar:السمن سلاء اللبن, tr:es-semnu sulâü'l-leben, gloss:semn sütten eritilen yağdır, source:"س م ن,B002"}. Sulamanın kökü ise hem su hem süt taşıyan kırbayı anlatır: {ar:السقاء القربة للماء واللبن, tr:es-sikâü'l-kırbetü li'l-mâi ve'l-leben, gloss:su ve süt için kırba, source:"س ق ي,B004"}. Kur'an bu içirmeyi bir ibret olarak anlatır: {ar:نُّسْقِيكُم مِّمَّا فِى بُطُونِهِۦ مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:nuskîkum mimmâ fî butûnihî min beyni fersin ve demin lebenen hâlisan sâiğan li'ş-şâribîn, gloss:karınlarındakinden; fışkı ile kan arasından içenlerin boğazından kolayca geçen arı bir süt içiririz, source:16:66}. Buradaki fiil, beşinci ayetteki "içirilir" fiiliyle aynıdır. Kolay yutulan süt, cehennemdeki içeceğin tersidir: {ar:يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ, tr:yetecerrauhû ve lâ yekâdu yusîğuh, gloss:yudum yudum içer ama yutamaz, source:14:17}. "Kolayca geçen" ve "yutamaz" aynı köktendir.

Yolculuk da aynı kelimelerden duyulur. Surenin ilk fiili, yürüyen bir devenin ön ayaklarının salınımını anlatır: {ar:ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير, tr:mâ ahsene etve yedey hâzihi'n-nâka ey rac'a yedeyhâ fi's-seyr, gloss:bu devenin ön ayaklarını yürürken geri atışı ne güzel, source:"ء ت ي,B009"}. Son ayetten bir önceki ayetteki dönüş kelimesi de aynı salınımı ve gün boyu yürüyüşü anlatır: {ar:الأوب سرعة تقليب اليدين والرجلين في السير والتأويب أن تسير النهار أجمع وتنزل الليل, tr:el-evbü sur'atü taklîbi'l-yedeyni ve'r-ricleyni fi's-seyr ve't-te'vîbü en tesîra'n-nehâra ecmea ve tenzile'l-leyl, gloss:yürüyüşte el ve ayakları çabuk oynatmak; bütün gün yürüyüp gece konmak, source:"ء و ب,B003"}; {ar:كل راجع مع الليل فهو آئب, tr:küllü râciin mea'l-leyli fe-huve âib, gloss:gece olunca dönen herkes âibdir, source:"ء و ب,B006"}. Aradaki kelimeler de yürüyüşün türlerini adlandırır: {ar:نصب القوم ساروا يومهم وهو سير لين, tr:nasaba'l-kavmu sârû yevmehum ve huve seyrun leyyin, gloss:topluluk bütün gün yumuşak bir yürüyüşle yürüdü, source:"ن ص ب,B010"}; {ar:السعي عدو ليس بشديد, tr:es-sa'yu adven leyse bi-şedîd, gloss:sa'y şiddetli olmayan koşudur, source:"س ع ي,B001"}; {ar:مرفوع الناقة في سيرها خلاف الموضوع, tr:merfûu'n-nâkati fî seyrihâ hılâfu'l-mevdû', gloss:devenin yürüyüşünde merfû mevdûun zıddıdır, source:"ر ف ع,B003"}; {ar:وضع البعير وغيره أي أسرع في سيره, tr:vadaa'l-baîru ve ğayruhû ey esraa fî seyrih, gloss:deve hızlandı, source:"و ض ع,B003"}. Bunlar yan anlamlardır ve ayetlerin anlamının yerine geçmez. Ama surenin "geldi mi" ile başlayıp "dönüşleri" ile biten yolu, deve sürücülerinin bir günlük yürüyüşü anlattığı kelimelerle kurulmuştur.

Kur'an deveyi yaratılmış ve insana boyun eğdirilmiş bir nimet olarak anlatır: {ar:وَٱلْأَنْعَٰمَ خَلَقَهَا ۗ لَكُمْ فِيهَا دِفْءٌۭ وَمَنَٰفِعُ وَمِنْهَا تَأْكُلُونَ, tr:ve'l-en'âme halakahâ lekum fîhâ dif'un ve menâfiu ve minhâ te'kulûn, gloss:hayvanları yarattı; onlarda sizin için ısınma ve faydalar vardır ve onlardan yersiniz, source:16:5}; {ar:وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ, tr:ve tahmilu eskâlekum ilâ beledin lem tekûnû bâliğîhi illâ bi-şıkkı'l-enfus, gloss:ancak canınızı tüketerek varabileceğiniz bir yere yüklerinizi taşırlar, source:16:7}. Başka bir ayette Allah'ın kendi işi anlatılır: {ar:أَوَلَمْ يَرَوْا۟ أَنَّا خَلَقْنَا لَهُم مِّمَّا عَمِلَتْ أَيْدِينَآ أَنْعَٰمًۭا, tr:e-ve-lem yerav ennâ halaknâ lehum mimmâ amilet eydînâ en'âmen, gloss:ellerimizin işinden onlar için hayvanlar yarattığımızı görmediler mi, source:36:71}; {ar:وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ وَمِنْهَا يَأْكُلُونَ, tr:ve zellelnâhâ lehum fe-minhâ rakûbuhum ve minhâ ye'kulûn, gloss:onları kendilerine boyun eğdirdik; bir kısmına biner bir kısmından yerler, source:36:72}. Bu ayetteki "iş" kelimesi, üçüncü ayetteki âmile ile aynı köktendir, ama burada iş Allah'ındır. Boyun eğdirme fiili de aşağılanma kelimesiyle aynı köktendir, ama burada bir lütuf olarak hayvana uygulanır. Deve, surenin döşediği odayı da döşer: {ar:وَجَعَلَ لَكُم مِّن جُلُودِ ٱلْأَنْعَٰمِ بُيُوتًۭا, tr:ve ceale lekum min cülûdi'l-en'âmi buyûten, gloss:hayvanların derilerinden size evler yaptı, source:16:80}; {ar:وَمِنْ أَصْوَافِهَا وَأَوْبَارِهَا وَأَشْعَارِهَآ أَثَٰثًۭا وَمَتَٰعًا, tr:ve min asvâfihâ ve evbârihâ ve eş'ârihâ esâsen ve metâan, gloss:yünlerinden yapağılarından ve kıllarından ev eşyası ve kullanılacak şeyler, source:16:80}. Allah İbrahim'e insanları hacca çağırmasını söylerken develer de gelişin aracıdır: {ar:يَأْتُوكَ رِجَالًۭا وَعَلَىٰ كُلِّ ضَامِرٍۢ يَأْتِينَ مِن كُلِّ فَجٍّ عَمِيقٍۢ, tr:ye'tûke ricâlen ve alâ külli dâmirin ye'tîne min külli feccin amîk, gloss:yaya olarak ve her uzak yoldan gelen arık develer üstünde sana gelsinler, source:22:27}. Bakmanın yiyeceğe yöneltildiği yerde de hayvanlar anılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bu bakış {ar:مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ, tr:metâan lekum ve li-en'âmikum, gloss:size ve hayvanlarınıza bir yararlanma olarak, source:80:32} diye biter.

Kaynaklar: 88:1 أَتَىٰكَ ء ت ي B009; 88:2 خَٰشِعَةٌ خ ش ع B004; 88:3 عَامِلَةٌ ع م ل B008; 88:3 نَّاصِبَةٌ ن ص ب B010; 88:4 تَصْلَىٰ ص ل ي B010; 88:5 تُسْقَىٰ س ق ي B004; 88:6 ضَرِيعٍ ض ر ع B001; 88:6 طَعَامٌ ط ع م B007; 88:7 يُسْمِنُ س م ن B002; 88:8 نَّاعِمَةٌ ن ع م B005; 88:9 لِّسَعْيِهَا س ع ي B001; 88:13 مَّرْفُوعَةٌ ر ف ع B003; 88:13 مَّرْفُوعَةٌ ر ف ع B007; 88:14 مَّوْضُوعَةٌ و ض ع B003; 88:14 مَّوْضُوعَةٌ و ض ع B007; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:15 مَصْفُوفَةٌ ص ف ف B002; 88:17 ٱلْإِبِلِ ء ب ل B001; 88:17 ٱلْإِبِلِ ء ب ل B002; 88:25 إِيَابَهُمْ ء و ب B003; 88:25 إِيَابَهُمْ ء و ب B006

## Hatırlatıcı, gözetmen değil

Yirmi birinci ayet Peygamber'in işini tek bir kelimeye indirir: hatırlatmak. "Ancak" sözü bu işin sınırını çizer. Hatırlatma, bir şeyin akla getirilmesini sağlayan şeydir ve tekrar edilir: {ar:التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر, tr:et-tezkiretü mâ yütezekkeru bihi'ş-şey' ve'z-zikrâ kesretü'z-zikr, gloss:tezkire bir şeyin hatırlandığı araçtır; zikra çok anmaktır, source:"ذ ك ر,B009"}. Yirmi ikinci ayet de bu işin olmadığı şeyi söyler: {ar:لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ, tr:leste aleyhim bi-musaytır, gloss:sen onların üstünde bir gözetmen değilsin, source:88:22}. Musaytır, bir şeyin başına konup onu gözeten ve yaptığını yazan kişidir: {ar:المسيطر والمصيطر المسلط على الشيء ليشرف عليه ويتعهد أحواله ويكتب عمله, tr:el-museytıru ve'l-musaytıru'l-musallatu ale'ş-şey'i li-yuşrife aleyhi ve yeteahhede ahvâlehû ve yektübe amelehû, gloss:bir şeyin başına konup onu gözeten halini kollayan ve işini yazan kişi, source:"س ط ر,B003"}; {ar:السيطرة مصدر المسيطر وهو كالرقيب الحافظ المتعهد للشيء, tr:es-saytaratu masdaru'l-museytır ve huve ke'r-rakîbi'l-hâfızı'l-müteahhidi li'ş-şey', gloss:bir şeyi bekleyen ve koruyan gözcü gibi olan, source:"س ط ر,B003"}. Bu yetkinin asıl sahipleri efendilerdir: {ar:المسيطرون الأرباب المسلطون, tr:el-museytırûne'l-erbâbü'l-musallatûn, gloss:başa geçirilmiş efendiler, source:"س ط ر,B003"}. Kökün aslı satırdır: {ar:أصل مطرد يدل على اصطفاف الشيء كالكتاب والشجر, tr:aslun muttaridun yedullü ale'stıfâfi'ş-şey'i ke'l-kitâbi ve'ş-şecer, gloss:yazı ve ağaç gibi şeylerin dizilişini gösteren kök, source:"س ط ر,B001"}; {ar:السطر سطر من كتب وسطر من شجر مغروس, tr:es-satru satrun min kütübin ve satrun min şecerin mağrûs, gloss:satır yazıdan bir satır ve dikilmiş ağaçtan bir sıradır, source:"س ط ر,B001"}. Gözetmen, kayıtları satır satır tutan kişidir. Bu kökün tanımında geçen diziliş kelimesi, on beşinci ayette yastıkların dizilişini anlatan kelimedir. Bu bağ kök birliğinden değil, kelimelerin açıklamasından gelir. Bahçede yastıkları dizen bir el vardır. Amelleri satıra dizen el de vardır, ama Peygamber'in eli değildir.

Kur'an bu kaydı Allah'a bağlar. Önceki kavimlerin anlatıldığı surenin sonunda şöyle denir: {ar:وَكُلُّ صَغِيرٍۢ وَكَبِيرٍۢ مُّسْتَطَرٌ, tr:ve küllü sağîrin ve kebîrin mustatar, gloss:küçük büyük her şey satır satır yazılmıştır, source:54:53}. Buradaki "yazılmış" kelimesi musaytır ile aynı köktendir. Kur'an'da bu kelimenin geçtiği tek başka yer, inkârcılara sorulan bir sorudur: {ar:أَمْ عِندَهُمْ خَزَآئِنُ رَبِّكَ أَمْ هُمُ ٱلْمُصَۣيْطِرُونَ, tr:em indehum hazâinu rabbike em humu'l-musaytırûn, gloss:yoksa Rabbinin hazineleri onların yanında mı, yoksa gözetmenler onlar mı, source:52:37}. Gözetmenlik ne Peygamber'indir ne de onu reddedenlerin.

Kur'an bu sınırı başka yerlerde de çizer. Kaf suresinin sonunda Allah şöyle der: {ar:وَمَآ أَنتَ عَلَيْهِم بِجَبَّارٍۢ ۖ فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ, tr:ve mâ ente aleyhim bi-cebbârin fe-zekkir bi'l-Kur'âni men yehâfu vaîd, gloss:sen onları zorlayan değilsin; tehdidimden korkana Kur'an ile hatırlat, source:50:45}. Başka yerlerde de {ar:فَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ حَفِيظًا ۖ إِنْ عَلَيْكَ إِلَّا ٱلْبَلَٰغُ, tr:fe-mâ erselnâke aleyhim hafîzan in aleyke ille'l-belâğ, gloss:seni onların üstüne bekçi göndermedik; sana düşen yalnızca duyurmaktır, source:42:48} ve {ar:وَمَا جَعَلْنَٰكَ عَلَيْهِمْ حَفِيظًۭا ۖ وَمَآ أَنتَ عَلَيْهِم بِوَكِيلٍۢ, tr:ve mâ cealnâke aleyhim hafîzan ve mâ ente aleyhim bi-vekîl, gloss:seni onlara bekçi yapmadık; sen onların vekili de değilsin, source:6:107} denir. Cezalandırmak da Allah'ın işidir: {ar:إِن يَشَأْ يَرْحَمْكُمْ أَوْ إِن يَشَأْ يُعَذِّبْكُمْ ۚ وَمَآ أَرْسَلْنَٰكَ عَلَيْهِمْ وَكِيلًۭا, tr:in yeşe' yerhamkum ev in yeşe' yuazzibkum ve mâ erselnâke aleyhim vekîlâ, gloss:dilerse size merhamet eder, dilerse azap eder; seni onlara vekil göndermedik, source:17:54}. Zorlama da sorunun içinde reddedilir: {ar:أَفَأَنتَ تُكْرِهُ ٱلنَّاسَ حَتَّىٰ يَكُونُوا۟ مُؤْمِنِينَ, tr:e-fe-ente tukrihu'n-nâse hattâ yekûnû mu'minîn, gloss:inanan olsunlar diye insanları sen mi zorlayacaksın, source:10:99}.

Yirmi üçüncü ayetteki istisna bu sınırın içinden çıkar: {ar:إِلَّا مَن تَوَلَّىٰ وَكَفَرَ, tr:illâ men tevellâ ve kefer, gloss:ancak yüz çevirip inkâr eden, source:88:23}. Yüz çevirme fiilinin kökü bir göreve geçmeyi de anlatır: {ar:تولى العمل أي تقلد, tr:tevelle'l-amele ey tekalled, gloss:işi üstlendi yani göreve geçti, source:"و ل ي,B003"}. Ayetteki anlam sırt dönmektir: {ar:ولى الرجل أي أدبر, tr:vellâ'r-raculu ey edbar, gloss:adam arkasını döndü, source:"و ل ي,B007"}. Yanında ise başa geçme anlamı duyulur. Peygamber'e verilmeyen göreve karşılık, yüz çeviren kendisi için yüz çevirmeyi üstlenmiştir. Yirmi dördüncü ayet cezayı Peygamber'e değil Allah'a verir: {ar:فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ, tr:fe-yuazzibuhullâhu'l-azâbe'l-ekber, gloss:Allah da onu en büyük azapla cezalandırır, source:88:24}. Allah'ın adı kulluk edilenin adıdır: {ar:فالإله الله تعالى لأنه معبود, tr:fe'l-ilâhu'llâhu teâlâ li-ennehû ma'bûd, gloss:ilah Allah'tır çünkü kulluk edilendir, source:"ء ل ه,B001"}. Son iki ayette konuşan "Biz" olur ve iş bölümü tamamlanır: {ar:إِنَّ إِلَيْنَآ إِيَابَهُمْ, tr:inne ileynâ iyâbehum, gloss:dönüşleri şüphesiz Bize'dir, source:88:25}; {ar:ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم, tr:summe inne aleynâ hısâbehum, gloss:sonra hesapları da şüphesiz Bize düşer, source:88:26}. Kur'an aynı bölüşümü tek bir cümlede söyler. Allah Peygamber'e, vaat edilenin bir kısmını ona göstersin ya da canını alsın, şunu der: {ar:فَإِنَّمَا عَلَيْكَ ٱلْبَلَٰغُ وَعَلَيْنَا ٱلْحِسَابُ, tr:fe-innemâ aleyke'l-belâğu ve aleyne'l-hısâb, gloss:sana düşen yalnızca duyurmaktır, hesap ise Bize düşer, source:13:40}. Önceki sure de aynı sırayı izler: önce {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-zekkir in nefeati'z-zikrâ, gloss:hatırlatma fayda verirse hatırlat, source:87:9}, sonra {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yezzekkeru men yahşâ, gloss:içi titreyen öğüt alacak, source:87:10}, sonra {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht ondan kaçınacak, source:87:11} ve en büyük ateş gelir. Başka yerlerde de şöyle denir: {ar:وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ, tr:ve zekkir fe-inne'z-zikrâ tenfeu'l-mu'minîn, gloss:hatırlat; hatırlatma inananlara fayda verir, source:51:55}; {ar:كَلَّآ إِنَّهَا تَذْكِرَةٌۭ, tr:kellâ innehâ tezkira, gloss:hayır; bu bir hatırlatmadır, source:80:11}; {ar:فَمَن شَآءَ ذَكَرَهُۥ, tr:fe-men şâe zekerah, gloss:dileyen onu anar, source:80:12}.

Kaynaklar: 88:21 فَذَكِّرْ ذ ك ر B009; 88:21 مُذَكِّرٌ ذ ك ر B003; 88:22 لَّسْتَ ل ي س B001; 88:22 بِمُصَيْطِرٍ س ط ر B001; 88:22 بِمُصَيْطِرٍ س ط ر B003; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:23 تَوَلَّىٰ و ل ي B003; 88:23 تَوَلَّىٰ و ل ي B007; 88:23 وَكَفَرَ ك ف ر B003; 88:24 ٱللَّهُ ء ل ه B001; 88:26 حِسَابَهُم ح س ب B001

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

