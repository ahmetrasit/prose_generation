Focus: 88:16. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_16/D.r13/context.md =====
# 88:16 — focus

وَزَرَابِىُّ مَبْثُوثَةٌ

Anchor translation (canonical reading, reference only):

Serilmiş halılar da vardır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَزَرَابِىُّ | زَرَابِىّ |  | CONJ;N |
| 2 | مَبْثُوثَةٌ | مَبْثُوثَة | ب ث ث | ADJ |


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
- 88:15 وَنَمَارِقُ مَصْفُوفَةٌۭ
- 88:16 ◀ focus وَزَرَابِىُّ مَبْثُوثَةٌ
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


===== _commentary/v16/work/88_16/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ب ث ث (root_000083) — identity root of مَبْثُوثَةٌ (w2)

- **B001** dagitip yaymak — bir seyi dagitip yaymak veya aciga cikarmak · atlari saldiriya yaymak veya av kopeklerini ava salmak · yayilip dagilmak · cok ve daginik; yayilmis veya savrulmus · toplanmamis, etrafa sacilmis hurma · yiyecegi veya hurmayi alt ust edip birbirinin ustune atmak · yaratilmislari veya hayvanlari yeryuzune yayip cogaltmak
  تفريق الشيء وإظهاره؛ بثوا الخيل؛ بث الصياد كلابه؛ خلق الخلق وبثهم في الأرض؛ وزرابي مبثوثة؛ تمر بث؛ بثثت الطعام والتمر (maqayis)؛ بث الخيل؛ كل شيء فرقته؛ انبث الجراد؛ كالفراش المبثوث؛ تمر بث (jamhara)؛ فانبث أي انتشر؛ تمر بث؛ منثورا متفرقا؛ الغبار إذا هيجته (sihah)؛ تفريقك الأشياء؛ بثوا الخيل؛ بث الصياد كلابه؛ بثت البسط؛ مبثوثة كثيرة؛ غبارا منتشرا؛ وبث منهما رجالا كثيرا ونساء أي نشر وكثر (tahdhib)؛ التفريق وإثارة الشيء كبث الريح التراب؛ بثثته فانبث؛ وبث فيها؛ كالفراش المبثوث (mufradat)
- **B002** icindekini acip dile getirmek — haberi veya sozu yaymak, duyurmak · birine sirrini acmak ve onu haberdar etmek · insanin icinde tasidigi keder, gam veya sikinti · yoksullugunu ve duskunlugunu birine sikayet etmek · gizli bir kusur, sevgi veya isin durumunu yoklayip anlamaya calisma
  بثثت الحديث أي نشرته؛ البث من الحزن؛ يشتكى ويبث ويظهر؛ أبث فلان شقوره وفقوره؛ وأبثثتك مكتومي (maqayis)؛ بثثته سري وأبثثته؛ البث ما يجده الرجل في نفسه من كرب أو غم (jamhara)؛ بث الخبر وأبثه؛ نشره؛ أبثثتك سري؛ أظهرته لك؛ البث الحال والحزن؛ أظهرت لك بثي (sihah)؛ البث الحزن الذي تفضي به إلى صاحبك؛ أبثثت فلانا سري؛ أطلعته عليه؛ لا يولج الكف ليعلم البث (tahdhib)؛ بث النفس ما انطوت عليه من الغم والسر؛ غمي الذي أبثه عن كتمان (mufradat)
- **B003** arastirip aciga cikarmak [kalıp] — haberi yaymak veya tozu kaldirip savurmak · bir isi arastirip yoklamak veya aciga cikarmak
  بثبثت الخبر بثبثة نشرته؛ وكذلك الغبار إذا هيجته (sihah)؛ بثبثت الأمر إذا فتشت عنه وتخبرته؛ بثبثوه أي كشفوه؛ الأصل فيه بثثوه فأبدلوا (tahdhib)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:16, and ## Buluşmalar) =====
## Döşenen oda, döşenen dünya

On üçüncü ayetten on altıncıya kadar bir oda döşenir. Dört eşya vardır ve her birine yapılmış bir işi gösteren bir sıfat verilir: {ar:فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ, tr:fîhâ sururun merfûa, gloss:orada kaldırılmış sedirler, source:88:13}; {ar:وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ, tr:ve ekvâbun mevdûa, gloss:konmuş kadehler, source:88:14}; {ar:وَنَمَارِقُ مَصْفُوفَةٌۭ, tr:ve nemâriku masfûfe, gloss:sıra sıra dizilmiş yastıklar, source:88:15}; {ar:وَزَرَابِىُّ مَبْثُوثَةٌ, tr:ve zerâbiyyu mebsûse, gloss:serilmiş halılar, source:88:16}. Bunlar kaldırmak, koymak, dizmek ve sermektir. On yedinci ayetten yirminciye kadar ise dünya döşenir: dört nesne ve edilgen dört fiil gelir. Deve yaratılmış, gök kaldırılmış, dağlar dikilmiş, yer düzlenmiştir. Aynı el hareketleri hem bir odayı hem bir dünyayı kurar.

Kaldırmak iki listede de geçer. Tanımı koymayı da içinde taşır: {ar:الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها, tr:er-ref'u yukâlü fi'l-ecsâmi'l-mevdûati izâ a'leytehâ an makarrihâ, gloss:konmuş cisimleri yerlerinden yukarı aldığında ref' denir, source:"ر ف ع,B001"}. Yapı için de kullanılır: {ar:في البناء إذا طولته, tr:fi'l-binâi izâ tavveltehû, gloss:binada yükselttiğinde, source:"ر ف ع,B001"}. Gök, bir evin tavanı gibi kaldırılmıştır: {ar:السماء سقف البيت وكل عال مطل سماء, tr:es-semâu sakfu'l-beyt ve küllü âlin mutıllin semâ', gloss:sema evin tavanıdır; yüksekten bakan her şey semadır, source:"س م و,B004"}. Dağların fiili olan dikmek, kadehlerin fiili olan koymak üzerinden tanımlanır: {ar:نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر, tr:nasbu'ş-şey'i vad'uhû vad'an nâti'en ke-nasbi'r-rumhi ve'l-binâi ve'l-hacer, gloss:bir şeyi dikmek onu çıkıntılı biçimde koymaktır; mızrak bina ve taş dikmek gibi, source:"ن ص ب,B001"}. Dikmenin aslında doğruluk vardır: {ar:أصل صحيح يدل على إقامة شيء وإهداف في استواء, tr:aslun sahîhun yedullü alâ ikâmeti şey'in ve ihdâfin fi'stivâ', gloss:bir şeyi dikip düzgünce yükseltmeyi gösteren kök, source:"ن ص ب,B001"}. Dağlar yerin kazıklarıdır: {ar:اسم لكل وتد من أوتاد الأرض إذا عظم وطال, tr:ismun li-külli vetedin min evtâdi'l-ardi izâ azume ve tâl, gloss:yerin kazıklarından büyüyüp uzayan her birinin adı, source:"ج ب ل,B001"}. Yer de düz bir dam gibi yayılmıştır: {ar:سطح الله الأرض سطحا بسطها, tr:satahallâhu'l-arda sathan besatahâ, gloss:Allah yeri düzledi yani yaydı, source:"س ط ح,B001"}; {ar:السطح ظهر البيت إذا كان مستويا, tr:es-sathu zahru'l-beyti izâ kâne müsteviyen, gloss:satıh evin düz olan damıdır, source:"س ط ح,B001"}; {ar:سطحت المكان جعلته في التسوية كسطح, tr:satahtü'l-mekâne cealtühû fi't-tesviyeti ke-sath, gloss:yeri bir dam gibi düz yaptım, source:"س ط ح,B001"}. Aynı kök çadır direğine de ad verir: {ar:المسطح عمود الخيمة الذي يجعل به لها سطحا, tr:el-mistahu amûdü'l-hayme'llezî yüc'alu bihî lehâ sathan, gloss:çadıra düz bir üst veren direk, source:"س ط ح,B003"}. Bu anlam ayetin yanında duyulduğunda dünya bir çadıra benzer: yükseltilmiş bir tavanı, kazıkları ve serilmiş bir zemini vardır.

İki listeyi birbirine bağlayan kelimeler de vardır. Yastıkların dizildiği sıra düz bir çizgidir: {ar:الصف أن تجعل الشيء على خط مستو, tr:es-saffu en tec'ale'ş-şey'e alâ hattın müstevin, gloss:saf bir şeyi düz bir çizgiye koymaktır, source:"ص ف ف,B001"}. Aynı kelime düz arazi için de kullanılır: {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsafu'l-müstevî mine'l-ardi keennehû alâ saffin vâhid, gloss:tek bir saf üstündeymiş gibi düz yer, source:"ص ف ف,B005"}. Halıların serilmesini anlatan fiil, canlıların yere yayılmasını da anlatır: {ar:بثت البسط, tr:bussetil-busut, gloss:halılar serildi, source:"ب ث ث,B001"}; {ar:خلق الخلق وبثهم في الأرض, tr:halaka'l-halka ve besse-hum fi'l-ard, gloss:yaratılmışları yarattı ve yeryüzüne yaydı, source:"ب ث ث,B001"}. Bu ikinci cümlede on yedinci ayetteki yaratma ile yirminci ayetteki yer bir aradadır. Yerin kökü kalın bir halıya da ad verir: {ar:الإراض بساط ضخم من وبر أو صوف, tr:el-irâdu bisâtun dahmun min veberin ev sûf, gloss:deve tüyünden ya da yünden kalın bir yaygı, source:"ء ر ض,B005"}. Bu, on altıncı ayetteki halıların hemen yanında duyulur.

Yaratmak da bir ustanın ilk hareketidir: ölçmek. {ar:خلقت الأديم للسقاء إذا قدرته, tr:halaktü'l-edîme li's-sikâi izâ kaddertüh, gloss:deriyi tulum yapmak için ölçtüm, source:"خ ل ق,B001"}; {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhû et-takdîru'l-müstakîm, gloss:yaratmanın aslı doğru ölçüdür, source:"خ ل ق,B001"}. Aynı kök düzleştirmeyi de anlatır: {ar:صخرة خلقاء ملساء, tr:sahratun halkâu melsâ', gloss:dümdüz ve kaygan kaya, source:"خ ل ق,B008"}. Böylece dört fiilin dördü de ölçüye ve düzlüğe dayanır: doğru ölçü, düzgünce dikmek, dam gibi düzlemek ve aynı ölçünün sırası. Kur'an da yaratmayı düzenlemeyle birlikte söyler. Önceki sure {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî halaka fe-sevvâ, gloss:yaratıp düzenleyen, source:87:2} der. İnsana da şöyle seslenilir: {ar:ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ, tr:ellezî halakake fe-sevvâke fe-adeleke, gloss:seni yaratıp düzenleyen ve dengeli kılan, source:82:7}.

Kur'an kaldırma ile koymayı yan yana koyar. Rahman nimetlerini sayarken şöyle der: {ar:وَٱلسَّمَآءَ رَفَعَهَا وَوَضَعَ ٱلْمِيزَانَ, tr:ve's-semâe rafeahâ ve vada'a'l-mîzân, gloss:göğü kaldırdı ve teraziyi koydu, source:55:7}; {ar:وَٱلْأَرْضَ وَضَعَهَا لِلْأَنَامِ, tr:ve'l-arda vada'ahâ li'l-enâm, gloss:yeri de yaratılmışlar için koydu, source:55:10}. Dirilişi inkâr edenlere sorulan soruda göğün yapısı şöyle anlatılır: {ar:رَفَعَ سَمْكَهَا فَسَوَّىٰهَا, tr:rafea semkehâ fe-sevvâhâ, gloss:tavanını yükseltip düzenledi, source:79:28}. Yerin döşenmesi de aynı resmi sürdürür: {ar:أَلَمْ نَجْعَلِ ٱلْأَرْضَ مِهَٰدًۭا, tr:e-lem nec'ali'l-arda mihâdâ, gloss:yeri bir döşek yapmadık mı, source:78:6}; {ar:وَٱلْجِبَالَ أَوْتَادًۭا, tr:ve'l-cibâle evtâdâ, gloss:dağları da kazıklar, source:78:7}; {ar:وَٱلْأَرْضَ فَرَشْنَٰهَا فَنِعْمَ ٱلْمَٰهِدُونَ, tr:ve'l-arda feraşnâhâ fe-ni'me'l-mâhidûn, gloss:yeri döşedik; ne güzel döşeyiciyiz, source:51:48}. Nuh da kavmine {ar:وَٱللَّهُ جَعَلَ لَكُمُ ٱلْأَرْضَ بِسَاطًۭا, tr:vallâhu ceale lekumu'l-arda bisâtâ, gloss:Allah yeri sizin için bir yaygı yaptı, source:71:19} der. Gök bir tavandır: {ar:وَجَعَلْنَا ٱلسَّمَآءَ سَقْفًۭا مَّحْفُوظًۭا ۖ وَهُمْ عَنْ ءَايَٰتِهَا مُعْرِضُونَ, tr:ve cealne's-semâe sakfen mahfûzan ve hum an âyâtihâ mu'ridûn, gloss:göğü korunmuş bir tavan yaptık; onlar ise onun işaretlerinden yüz çeviriyorlar, source:21:32}. Tur suresi de bir yemin olarak {ar:وَٱلسَّقْفِ ٱلْمَرْفُوعِ, tr:ve's-sakfi'l-merfû', gloss:yükseltilmiş tavana andolsun, source:52:5} der. Bu çadırın direği yoktur: {ar:ٱللَّهُ ٱلَّذِى رَفَعَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا, tr:Allâhullezî rafea's-semâvâti bi-ğayri amedin teravnehâ, gloss:gökleri görebileceğiniz direkler olmadan yükselten Allah, source:13:2}. Yayma fiili de iki yönde kullanılır: {ar:وَبَثَّ فِيهَا مِن كُلِّ دَآبَّةٍۢ, tr:ve besse fîhâ min külli dâbbe, gloss:orada her türlü canlıyı yaydı, source:31:10}. O gün ise yayılan insanlardır, halılar değil: {ar:يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ, tr:yevme yekûnu'n-nâsu ke'l-ferâşi'l-mebsûs, gloss:insanların saçılmış pervaneler gibi olacağı gün, source:101:4}. Bahçenin odası da başka yerlerde aynı kelimelerle döşenir: {ar:مُتَّكِـِٔينَ عَلَىٰ سُرُرٍۢ مَّصْفُوفَةٍۢ, tr:muttekiîne alâ sururin masfûfe, gloss:dizili sedirlere yaslanmış, source:52:20}; {ar:وَفُرُشٍۢ مَّرْفُوعَةٍ, tr:ve furuşin merfûa, gloss:yükseltilmiş döşekler, source:56:34}; {ar:إِخْوَٰنًا عَلَىٰ سُرُرٍۢ مُّتَقَٰبِلِينَ, tr:ihvânen alâ sururin mutekâbilîn, gloss:sedirler üstünde karşılıklı kardeşler olarak, source:15:47}.

Kaynaklar: 88:13 مَّرْفُوعَةٌ ر ف ع B001; 88:14 مَّوْضُوعَةٌ و ض ع B001; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:15 مَصْفُوفَةٌ ص ف ف B005; 88:16 مَبْثُوثَةٌ ب ث ث B001; 88:17 خُلِقَتْ خ ل ق B001; 88:17 خُلِقَتْ خ ل ق B008; 88:18 ٱلسَّمَآءِ س م و B004; 88:18 رُفِعَتْ ر ف ع B001; 88:19 نُصِبَتْ ن ص ب B001; 88:19 ٱلْجِبَالِ ج ب ل B001; 88:20 سُطِحَتْ س ط ح B001; 88:20 سُطِحَتْ س ط ح B003; 88:20 ٱلْأَرْضِ ء ر ض B005

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

