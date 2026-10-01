Focus: 107:7. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/107_7/D.r13/context.md =====
# 107:7 — focus

وَيَمْنَعُونَ ٱلْمَاعُونَ

Anchor translation (canonical reading, reference only):

Yardımı da esirgerler.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَيَمْنَعُونَ | مَّنَعَ | م ن ع | CONJ;V;PRON |
| 2 | ٱلْمَاعُونَ | مَاعُون | م ع ن | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 107 — full text (context; no pericope)

- 107:1 أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ
- 107:2 فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ
- 107:3 وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 107:4 فَوَيْلٌۭ لِّلْمُصَلِّينَ
- 107:5 ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ
- 107:6 ٱلَّذِينَ هُمْ يُرَآءُونَ
- 107:7 ◀ focus وَيَمْنَعُونَ ٱلْمَاعُونَ


===== _commentary/v16/work/107_7/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## م ن ع (root_001448) — identity root of وَيَمْنَعُونَ (w1)

- **B001** vermeme ve esirgeme — vermenin karşıtı olarak vermeme ve esirgeme · vermeyen veya verilecek şeyi elinde tutan · iyiliği sürekli esirgeyen çok cimri kişi · başkasına vermeyen, cimrice elinde tutan kişi · yalnızca vermemeyi hak edenden esirgeyen ve adaletle veren
  خلاف الإعطاء (maqayis;sihah)؛ ضد العطية (mufradat)؛ رجل منوع ومناع إذا كان بخيلا ممسكا (tahdhib)؛ مناع للخير (tahdhib;mufradat)
- **B002** isteğinden alıkoyma — onu istediği şeyden alıkoymak · seni bunu yapmaktan ne alıkoydu? · önüne engel çıkınca geri durmak
  منعته أمنعه منعا فامتنع أي حلت بينه وبين إرادته (ayn)؛ منعت الرجل عن الشئ فامتنع منه (sihah)؛ المنع أن تحول بين الرجل وبين الشيء الذي يريده (tahdhib)؛ ما الذي صدك وحملك على ترك ذلك (mufradat)
- **B003** erişilmez kılan koruyucu güç — inananları çevreleyip koruyan ve destekleyen · gücü ve koruması sayesinde erişilemez · koruyucu güç, saygınlık ve destekçiler · saygınlık ve güçlü koruma içinde
  مكان منيع وهو في عز ومنعة (maqayis)؛ رجل منيع لا يخلص إليه وهو في عز ومنعة (ayn)؛ مكان منيع وقد منع مناعة؛ المنعة جمع مانع أي من يمنعه من عشيرته (sihah)؛ يحوطهم وينصرهم؛ في قوم يمنعونه ويحمونه (tahdhib)؛ يقال في الحماية ومنه مكان منيع وفلان ذو منعة (mufradat)
- **B004** cinsel ahlaksızlığa yanaşmayan kadın [kalıp] — cinsel ahlaksızlığa yanaşmayan, kendini sakınan kadın · ahlak dışı cinsel ilişkiyi kabul etmeyen kadın
  امرأة منيعة متمنعة لا تؤاتى على فاحشة (ayn)؛ امرأة منعة متمنعة لا تؤاتى على فاحشة (tahdhib)؛ امرأة منيعة كناية عن العفيفة (mufradat)
- **B005** Engelle! — Engelle!
  مناع بمعنى امنع (ayn)؛ مناع أي امنع كقولهم نزال أي انزل (mufradat)
- **B006** bir şey üzerinde karşılıklı engelleşme — bir şey üzerinde onunla karşılıklı engelleşmek
  مانعته الشئ ممانعة (sihah)
- **B007** çetin yıla direnen genç dişi deve ile dişi oğlak — gençlikleriyle çetin yıla direnen ve yetişkin hayvanlardan önce doyan genç dişi deve ile dişi oğlak · çetin yıla karşı koyan ve yetişkin hayvanlardan önce doyan genç dişi deve ile dişi oğlak
  المتمنعان البكرة والعناق تمتنعان على السنة بفتائهما (sihah)؛ المتمنعتان البكرة والعناق تمنعان على السنة لفنائهما (tahdhib)؛ المقاتلتان للزمان عن أنفسهما (sihah;tahdhib)

## م ع ن (root_004706) — identity root of ٱلْمَاعُونَ (w2)

- **B001** akan su ve suyun akışı — 
  معن الماء جرى (maqayis;tahdhib)؛ ماء معين أي جار (maqayis;sihah;tahdhib)؛ المعنة ماء قليل يجري (maqayis)؛ المعنان مجاري الماء في الوادي (maqayis;sihah)؛ أمعنت الأرض رويت وكلأ ممعون جرى فيه الماء (maqayis;sihah;tahdhib)؛ معن الوادي كثر فيه الماء المعين (maqayis)
- **B002** atın veya benzeri hayvanın koşarak uzaklaşması — 
  أمعن الفرس في عدوه (maqayis)؛ أمعن الفرس ونحوه إمعانا إذا تباعد يعدو (ayn)؛ أمعن الفرس تباعد في عدوه (sihah;tahdhib)
- **B003** kolaylık ve hafiflik; bağlama göre azlık ya da çokluk — 
  رجل معن في حاجته سهل (maqayis;sihah)؛ ضياع مالك غير معن أي غير سهل (maqayis)؛ المعن الشيء اليسير الهين (sihah)؛ ماله سعنة ولا معنة أي شيء (sihah)؛ المعن القليل والمعن الكثير (tahdhib)
- **B004** hakkı alıp götürmek; hak sahibine yönelince hakkı tanıyıp boyun eğmek — 
  أمعن بحقي ذهب به (maqayis;sihah)؛ أمعن لي بحقي إذا أقر به وانقاد (tahdhib)
- **B005** sağlanan yarar veya kullanıma sunulan ev eşyası — 
  الماعون يفسر بالزكاة والصدقة ويقال هو أسقاط البيت نحو الفأس والقدر والدلو (ayn)؛ الماعون اسم جامع لمنافع البيت (sihah)؛ يسمى الماء أيضا ماعونا (sihah)؛ الماعون في الجاهلية كل منفعة وعطية وفي الإسلام الطاعة والزكاة (sihah)؛ الماعون المعروف كله والقصعة والقدر والفأس (tahdhib)؛ كل ما يستعار من قدوم وسفرة وشفرة (tahdhib)؛ الماعون الطاعة (tahdhib)
- **B006** barınılan yer — 
  قولهم للمنزل معان وجمعه معن (maqayis)؛ المعان المباءة والمنزل ومعان موضع بالشأم (sihah)

## ECHO ع و ن (root_001064) — for ٱلْمَاعُونَ (w2): withheld observed target; not identity

- **B001** yardım, destek ve dayanışma — yardım, destek veya işe yarayan yardımcı şey · yardım etme, destek sağlama · yardım etti, destek oldu · yardımlaştı veya destek verdi · birinden yardım istedi · birbirine yardım etti, dayanıştı · çok yardımsever, sıkça yardım eden · yardım, destek · yardım anlamındaki tekil biçim veya yardım sözünün çoğulu
  كل شيء استعنت به أو أعانك فهو عونك (ayn); العون الظهيرة على الأمر والمعونة الإعانة واستعنت بفلان فأعانني وعاونني وتعاون القوم (sihah); كل شيء أعانك فهو عون لك وأعنته إعانة واستعنت به وعاونته وقد تعاونا (tahdhib); العون المعاونة والمظاهرة والتعاون التظاهر والاستعانة طلب العون (mufradat)
- **B002** yaşça orta evrede olan — yaşça orta evrede olan · ne genç ne yaşlı sığır · orta yaşlı veya evlenmiş kadın · orta yaşlı at · orta yaşta olanlar
  العوان البقرة النصف في سنها ويقال للمرأة النصف عوان (ayn); العوان النصف في سنها من كل شيء وبقرة عوان لا فارض مسنة ولا بكر صغيرة (sihah); العوان النصف التي بين الفارض وهي المسنة وبين البكر وهي الصغيرة ويقال فرس عوان وخيل عون (tahdhib); العوان المتوسط بين السنين وجعل كناية عن المسنة من النساء (mufradat)
- **B003** yinelenmiş veya öncülü olan savaş [kalıp] — daha önce yaşanmış ya da yinelenmiş savaş
  الحرب العوان التي كانت قبلها حرب بكر (ayn); العوان من الحروب التي قوتل فيها مرة بعد مرة (sihah); استعير للحرب التي قد تكررت وقدمت (mufradat)
- **B004** yaşlı hurma ağacı — yaşlı hurma ağacı
  وقيل العوانة للنخلة القديمة (mufradat)
- **B005** bedensel denge ve güç olgunluğu [kalıp] — bedeni dengeli kadın veya yaş almış, etli kadın · gücü ile yaşı birbirine yetişmiş yük atı
  المتعاونة من النساء التي طعنت في السن ولا تكون إلا مع كثرة اللحم (sihah); امرأة متعاونة إذا اعتدل خلقها فلم يبد حجمها وبرذون متعاون إذا لحقت قوته وسنه (tahdhib)
- **B006** yaban eşeği sürüsü — yaban eşeği sürüsü · yaban eşeği sürüleri · yaban eşeği sürüleri
  العانة القطيع من حمر الوحش وتجمع على عانات وعون (ayn); العانة القطيع من حمر الوحش والجمع عون (sihah); العانة قطيع من حمر الوحش وجمع على عانات وعون (mufradat)
- **B007** erkekte kasık kılları — erkeğin kasık kılları · kasık kıllarını küçülterek söyleyen biçim · kasık kıllarını tıraş etti
  عانة الرجل إسبه من الشعر على فرجه وتصغيره عوينة (ayn); العانة شعر الركب واستعان فلان حلق عانته (sihah); عانة الرجل شعره النابت على فرجه وتصغيره عوينة (mufradat)
- **B008** bir yer adı ve o yere bağlanan şarap adı — şarabıyla ilişkilendirilen bir yer veya köy adı · aynı yer adıyla ilişkili değişken ad biçimi · söz konusu yerden geldiği belirtilen şarap
  عانات موضع من ناحية الجزيرة تنسب إليه الخمر العانية (ayn); عانة قرية على الفرات تنسب إليها الخمر فيقال عانية (sihah)

===== _commentary/v16/out/s107/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 107:7, and ## Buluşmalar) =====
## Zayıfın üstündeki eller: itmek, teşvik etmek, kaldırmak, önüne geçmek

İkinci ve üçüncü ayetler zayıfların bedenleri üzerinde bir dizi hareket kurar. İlki itmektir: {ar:يَدُعُّ, tr:yedu‘‘u, gloss:itip kakar, source:107:2}. Kök bu hareketi kabalığıyla birlikte tanımlar: {ar:الدفع الشديد, tr:ed-def‘u'ş-şedîd, gloss:sert itiş, source:"د ع ع,B001"}; {ar:دفع في جفوة, tr:def‘un fî cefve, gloss:kabalıkla itmek, source:"د ع ع,B001"}. Bu bir dürtme değildir. İten bedenin çocuğun bedenine çarpıp onu kapıdan uzaklaştırmasıdır. Aynı kök hayvan sürmeyi de adlandırır: {ar:الدعدعة زجر الغنم, tr:ed-da‘da‘atu zecru'l-ġanem, gloss:"da‘da‘a", koyunu bağırarak sürmektir, source:"د ع ع,B003"}. Yetim bir sürü gibi kovulur. Ama aynı ses yukarı doğru da çağırır: {ar:أن تقول للعاثر دع دع أي قم فانتعش, tr:en tekûle li'l-âsiri da‘ da‘, ey kum fe'nte‘iş, gloss:sürçüp düşene "da‘ da‘" demek, yani kalk ve kendine gel, source:"د ع ع,B004"}. Bir kök hem düşüren itişi hem kaldıran çağrıyı barındırır.

Üçüncü ayetin fiili ters yöndeki itiştir: {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ ta‘âmi'l-miskîn, gloss:yoksulun yemeğine teşvik etmez, source:107:3}. Kök bunu {ar:حض يحض حضا وهو الحث على الخير, tr:hadda yehuddu haddan, ve huve'l-hassu ale'l-hayr, gloss:"hadd", hayra doğru sürmektir, source:"ح ض ض,B001"} diye tanımlar. Karşılıklı biçimi de vardır: {ar:والمحاضة أن يحث كل واحد منهما صاحبه, tr:ve'l-muhâddatu en yehusse küllü vâhidin minhumâ sâhibeh, gloss:"muhâdda", ikisinden her birinin ötekini sürmesidir, source:"ح ض ض,B001"}. Aynı kök yeryüzünün en alt yerini de adlandırır: {ar:الحضيض قرار الأرض عند سفح الجبل, tr:el-hadîdu karâru'l-ardı inde safhi'l-cebel, gloss:"hadîd", dağ eteğinde yerin en dip noktasıdır, source:"ح ض ض,B002"}. Bu anlam fiilin anlamının yanında duyulur. Teşvik, en dipte yatana doğru yapılan bir itiştir.

Yoksulun kökü onu bu dipte, hareketsiz yatar hâlde gösterir: {ar:السكون ذهاب الحركة, tr:es-sükûnu zehâbu'l-hareke, gloss:sükûn, hareketin gitmesidir, source:"س ك ن,B001"}; {ar:المسكين الفقير وقد يكون بمعنى الذلة والضعف, tr:el-miskînu'l-fakîr, ve kad yekûnu bi-ma‘ne'z-zilleti ve'd-da‘f, gloss:miskin fakirdir; düşkünlük ve güçsüzlük anlamına da gelir, source:"س ك ن,B006"}; {ar:تمسكن إذا خضع لله وهي المسكنة للذلة, tr:temeskene izâ hada‘a li'llâh, ve hiye'l-meskenetu li'z-zille, gloss:Allah'a boyun eğdiğinde "temeskene" denir; meskenet düşkünlük içindir, source:"س ك ن,B006"}. Yoksul, ihtiyacın durdurduğu kişidir. Beşinci ayetin kelimesi de bu durgunlukla tanımlanır: {ar:السهو السكون, tr:es-sehvu's-sükûn, gloss:sehv durgunluktur, source:"س ه و,B002"}. Böylece sahnede iki durgunluk yan yana durur. Biri yerde yatan yoksulun bedeni, öteki namazda kıpırtısız kalmış kalptir. Yedinci ayet son hareketi ekler: {ar:وَيَمْنَعُونَ, tr:ve yemne‘ûne, gloss:ve engel olurlar, alıkoyarlar, source:107:7}. Kök bunu bir bedenin araya girmesi olarak tanımlar: {ar:المنع أن تحول بين الرجل وبين الشيء الذي يريده, tr:el-men‘u en tehûle beyne'r-racüli ve beyne'ş-şey'i'llezî yurîdüh, gloss:men‘, adamla istediği şeyin arasına girmektir, source:"م ن ع,B002"}. Aynı kök, araya girmenin iyi yüzünü de taşır: {ar:المنعة جمع مانع أي من يمنعه من عشيرته, tr:el-men‘atu cem‘u mâni‘, ey men yemne‘uhû min aşîretih, gloss:"men‘a", koruyucuların çoğuludur; yani soyundan onu koruyanlar, source:"م ن ع,B003"}; {ar:يحوطهم وينصرهم, tr:yehûtuhum ve yensuruhum, gloss:onları çepeçevre sarar ve onlara yardım eder, source:"م ن ع,B003"}. Babasını yitiren çocuk bu koruyucu halkayı da yitirmiştir. Onun halkası olabilecek adamlar ise aynı kökün fiilini, onunla istediği şey arasına girmek için kullanır.

Sahne surenin sırasıyla kurulur. İkinci ayetteki geniş zaman itmeyi bir alışkanlık olarak gösterir. Üçüncü ayet en küçük yükümlülüğü bile düşürür. Adam kendi elinden vermeyi bırakmak bir yana, başkasını doyurmaya yönelten tek bir söz de söylemez. Beşinci ayet durgunluğu namaz kılanın içine taşır. Yedinci ayet itilen yetimden sonra bir duvar diker.

Kuran itişi itenin üzerine çevirir. Tûr suresinde Allah hüküm gününü anlatır: {ar:يَوْمَ يُدَعُّونَ إِلَىٰ نَارِ جَهَنَّمَ دَعًّا, tr:yevme yuda‘‘ûne ilâ nâri cehenneme da‘‘â, gloss:cehennem ateşine itildikçe itilecekleri gün, source:52:13}. Ardından onlara {ar:هَٰذِهِ ٱلنَّارُ ٱلَّتِى كُنتُم بِهَا تُكَذِّبُونَ, tr:hâzihi'n-nâru'lletî kuntum bihâ tükezzibûn, gloss:işte yalanladığınız ateş budur, source:52:14} denir. Fecr suresinde Allah, rızkı daraltılınca Rabbi kendisini aşağıladı diyen insanı azarlar {source:89:16}. Azar, surenin çiftini çoğul ve karşılıklı biçimde verir: {ar:كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ, tr:kellâ bel lâ tükrimûne'l-yetîm, gloss:hayır, asıl siz yetime ikram etmiyorsunuz, source:89:17}, {ar:وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ tehâddûne alâ ta‘âmi'l-miskîn, gloss:yoksulun yemeği için birbirinizi teşvik etmiyorsunuz, source:89:18}. Duhâ suresi iki yasakla aynı elleri durdurur: {ar:فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ, tr:fe-emme'l-yetîme fe-lâ takhar, gloss:yetimi ezme, source:93:9}, {ar:وَأَمَّا ٱلسَّآئِلَ فَلَا تَنْهَرْ, tr:ve emme's-sâile fe-lâ tenhar, gloss:isteyeni azarlama, source:93:10}. Teşvikin tersine dönmüş hâli Nisâ suresindedir: {ar:ٱلَّذِينَ يَبْخَلُونَ وَيَأْمُرُونَ ٱلنَّاسَ بِٱلْبُخْلِ, tr:ellezîne yebhalûne ve ye'mürûne'n-nâse bi'l-buhl, gloss:cimrilik eden ve insanlara cimriliği emredenler, source:4:37}. Kalem suresindeki bahçe sahipleri ürünü sabah erkenden devşirmeye yemin eder {source:68:17}. Sonra fısıldaşarak yola çıkarlar: {ar:فَٱنطَلَقُوا۟ وَهُمْ يَتَخَٰفَتُونَ, tr:fe'ntalekû ve hum yetehâfetûn, gloss:fısıldaşarak yola koyuldular, source:68:23}. Fısıldaştıkları şey kapıya konan bir engeldir: {ar:أَن لَّا يَدْخُلَنَّهَا ٱلْيَوْمَ عَلَيْكُم مِّسْكِينٌۭ, tr:en lâ yedhulenne'hâ'l-yevme aleykum miskîn, gloss:bugün oraya hiçbir yoksul yanınıza girmesin, source:68:24}. Karşılıklı teşvik burada yoksula karşı bir fısıltıya dönmüştür. Aynı surede Allah Peygamber'e boyun eğmemesi gereken kişiyi bu kökle niteler: {ar:مَّنَّاعٍۢ لِّلْخَيْرِ مُعْتَدٍ أَثِيمٍ, tr:mennâ‘in li'l-hayri mu‘tedin esîm, gloss:hayra hep engel olan, sınırı aşan, günahkâr, source:68:12}. Beled suresinde sarp yokuş {ar:فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ, tr:fe-le'ktehame'l-akabe, gloss:ama o sarp yokuşa atılmadı, source:90:11} ile açılır. Yokuşun içinde surenin iki zayıfı yere en yakın hâlleriyle durur: {ar:يَتِيمًۭا ذَا مَقْرَبَةٍ, tr:yetîmen zâ makrabe, gloss:yakınlığı olan bir yetim, source:90:15}, {ar:أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ, tr:ev miskînen zâ metrabe, gloss:ya da toprağa düşmüş bir yoksul, source:90:16}. Yokuş karşılıklı bir sürmeyle tamamlanır: {ar:وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ, tr:ve tevâsav bi'l-merhame, gloss:birbirlerine merhameti öğütlediler, source:90:17}.

Kaynaklar: 107:2 يَدُعُّ د ع ع B001; 107:2 يَدُعُّ د ع ع B003; 107:2 يَدُعُّ د ع ع B004; 107:3 يَحُضُّ ح ض ض B001; 107:3 يَحُضُّ ح ض ض B002; 107:3 ٱلْمِسْكِينِ س ك ن B001; 107:3 ٱلْمِسْكِينِ س ك ن B006; 107:5 سَاهُونَ س ه و B002; 107:7 وَيَمْنَعُونَ م ن ع B002; 107:7 وَيَمْنَعُونَ م ن ع B003

## Evin içi: küçükler, ev halkı, raftaki kaplar

Surenin altında bir ev durur. İtişi adlandıran kök bir adamın küçük çocuklarını da adlandırır: {ar:الدعاع عيال الرجل الصغار, tr:ed-di‘â‘u iyâlu'r-racüli's-sıġâr, gloss:"di‘â‘", adamın küçük çoluk çocuğudur, source:"د ع ع,B009"}; {ar:أدع الرجل إذا كثر دعاعه, tr:edea'r-racül izâ kesüra di‘â‘uh, gloss:adamın küçükleri çoğaldığında "edea" denir, source:"د ع ع,B009"}. Yetim, böyle bir evin bakıcısını yitirmiş çocuktur: {ar:اليتيم الذي مات أبوه حتى يبلغ, tr:el-yetîmu'llezî mâte ebûhu hattâ yebluġ, gloss:yetim, ergenliğe erinceye kadar babası ölmüş olandır, source:"ي ت م,B001"}. Yoksulun kökü oturulan evi, ev halkını ve evi ayakta tutan erzakı adlandırır: {ar:سكنت داري وأسكنتها غيرى, tr:sekentü dârî ve eskentuhâ ġayrî, gloss:evimde oturdum ve onu başkasına oturttum, source:"س ك ن,B002"}; {ar:السكن أهل الدار, tr:es-sekenu ehlu'd-dâr, gloss:"seken", evin halkıdır, source:"س ك ن,B003"}; {ar:قيل للقوت سكن لأن المكان به يسكن, tr:kîle li'l-kûti seken, li-enne'l-mekâne bihî yuskan, gloss:azığa "seken" denmiştir, çünkü bir yerde onunla oturulur, source:"س ك ن,B010"}. Beşinci ayetin kökü evin önünü ve eşya rafını verir: {ar:السهوة وهي كالصفة تكون أمام البيت, tr:es-sehve ve hiye ke's-suffe tekûnu emâme'l-beyt, gloss:"sehve", evin önündeki sundurma gibi bir yerdir, source:"س ه و,B004"}; {ar:السهوة أربعة أعواد أو ثلاثة يعارض بعضها على بعض يوضع عليها شيء من الأمتعة, tr:es-sehvetu erba‘atu a‘vâdin ev selâsetun yu‘âradu ba‘duhâ alâ ba‘d, yûda‘u aleyhâ şey'un mine'l-emti‘a, gloss:"sehve", birbirine çaprazlanmış üç dört sopadır, üstüne eşya konur, source:"س ه و,B004"}.

Yedinci ayetin kelimesi bu rafta duran şeylerin adıdır: {ar:ٱلْمَاعُونَ, tr:el-mâ‘ûn, gloss:gündelik yardım eşyası, ufak iyilik, source:107:7}. Kök onu tek tek sayar: {ar:ويقال هو أسقاط البيت نحو الفأس والقدر والدلو, tr:ve yukâlu huve eskâtu'l-beyt, nahve'l-fe'si ve'l-kıdri ve'd-delv, gloss:evin ufak tefek eşyası olduğu da söylenir: balta, tencere, kova gibi, source:"م ع ن,B005"}; {ar:الماعون اسم جامع لمنافع البيت, tr:el-mâ‘ûnu'smun câmi‘un li-menâfi‘i'l-beyt, gloss:mâûn, evin işe yarar şeylerinin toplu adıdır, source:"م ع ن,B005"}; {ar:كل ما يستعار من قدوم وسفرة وشفرة, tr:küllü mâ yusta‘âru min kadûmin ve sufratin ve şefra, gloss:keser, sofra bezi, bıçak gibi ödünç istenen her şey, source:"م ع ن,B005"}. Aynı kök evin kendisini de adlandırır: {ar:المعان المباءة والمنزل, tr:el-ma‘ânu'l-mebâetu ve'l-menzil, gloss:"me‘ân", konaklanan yer ve evdir, source:"م ع ن,B006"}. Bu eşyanın küçüklüğünü de söyler: {ar:المعن الشيء اليسير الهين, tr:el-ma‘nu'ş-şey'u'l-yesîru'l-heyyin, gloss:"ma‘n", az ve kolay şeydir, source:"م ع ن,B003"}. Bunlar komşunun kapıya gelip istediği şeylerdir: bir tencere, bir kova, bir bıçak. Verilince evden bir şey eksilmez, çoğu zaman geri de gelir. Onları esirgeyen el kökte adıyla anılır: {ar:رجل منوع ومناع إذا كان بخيلا ممسكا, tr:racülun menû‘un ve mennâ‘un izâ kâne bahîlen mümsikâ, gloss:cimri ve eli sıkı olan adama "menû‘" ve "mennâ‘" denir, source:"م ن ع,B001"}.

Bu evin kapları doldurmak içindir. İtişi adlandıran kök aynı zamanda bir ölçeği sarsarak doldurmayı da adlandırır: {ar:الدعدعة تحريك المكيال ليستوعب الشيء, tr:ed-da‘da‘atu tahrîku'l-mikyâli li-yesta‘ibe'ş-şey', gloss:"da‘da‘a", ölçeği sarsmaktır ki konan şey içine sığsın, source:"د ع ع,B002"}; {ar:دعدع مكيالا أو جوالقا حتى يكتنز, tr:da‘da‘a mikyâlen ev cuvâlikan hattâ yektenize, gloss:ölçeği ya da çuvalı iyice dolup sıkışıncaya kadar sarstı, source:"د ع ع,B002"}; {ar:دعدعت الشيء ملأته وجفنة مدعدعة, tr:da‘da‘tu'ş-şey'e mele'tühû, ve cefnetun müda‘da‘a, gloss:şeyi doldurdum; ağzına kadar dolu büyük tabak, source:"د ع ع,B002"}. İşleyiş şudur: Tahıl ölçeğe dökülür, ölçek sallanır, taneler yerleşir, açılan boşluğa daha fazlası girer. Tabak kenarına kadar dolar. Kabın içine giren de üçüncü ayetin kelimesidir: {ar:الطعم ذوقه والطعام اسم جامع لكل ما يؤكل, tr:et-ta‘mu zevkuhû ve't-ta‘âmu'smun câmi‘un li-külli mâ yü'kel, gloss:tat onun tadılmasıdır; yemek, yenen her şeyin toplu adıdır, source:"ط ع م,B001"}. Kök isteyeni ve vereni yan yana koyar: {ar:استطعمه سأله أن يطعمه وأطعمته الطعام, tr:istat‘amehû se'elehû en yut‘imeh, ve et‘amtühu't-ta‘âm, gloss:ondan yemek istedi, yani doyurmasını diledi; ona yemek yedirdim, source:"ط ع م,B002"}. Ev sahibini de adlandırır: {ar:رجل طاعم حسن الحال ومطعام كثير القرى, tr:racülun tâ‘imun hasenu'l-hâl, ve mit‘âmun kesîru'l-kırâ, gloss:"tâ‘im" hâli vakti yerinde adamdır; "mit‘âm" konuğunu çokça ağırlayandır, source:"ط ع م,B004"}. Mâûn bu kapları ödenmesi gereken bir iyilik olarak da sayar: {ar:الماعون المعروف كله والقصعة والقدر والفأس, tr:el-mâ‘ûnu'l-ma‘rûfu küllühû ve'l-kas‘atu ve'l-kıdru ve'l-fe's, gloss:mâûn bütün iyiliktir; çanak, tencere ve baltadır, source:"م ع ن,B005"}. Esirgemek ise vermenin tersidir: {ar:خلاف الإعطاء, tr:hılâfu'l-i‘tâ’, gloss:vermenin karşıtı, source:"م ن ع,B001"}.

Ayetler sırasıyla okununca evin kurulduğu görülür. İkinci ayette bir kök iki şey söyler. Duyulan anlam "iter"dir, ama aynı harfler küçük çocukları ve ağzına kadar sarsılarak doldurulan tabağı da adlandırır. Ölçeği sarsıp doldurabilecek el, babasız çocuğu kapıdan iter. Üçüncü ayette yemek ve yoksul gelir. Yoksulun kökü ev ve ev halkıdır. Evi ayakta tutan azık, evi olmayana ulaşmaz. Beşinci ayetin kökünde, kullanılmayan eşyanın üstünde durduğu raf duyulur. Yedinci ayet o raftaki şeylerin adını verir.

Kuran bu kapları doldurulmuş hâlde gösterir. İnsan suresinde Allah iyileri anlatır: {ar:وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا, tr:ve yut‘imûne't-ta‘âme alâ hubbihî miskînen ve yetîmen ve esîrâ, gloss:yemeği, kendileri ona düşkünken yoksula, yetime ve esire yedirirler, source:76:8}. Yâsîn suresinde kapların bir gerekçeyle reddedildiği görülür. Kâfirlere Allah'ın verdiği rızıktan harcamaları söylenince, inananlara şu cevabı verirler: {ar:أَنُطْعِمُ مَن لَّوْ يَشَآءُ ٱللَّهُ أَطْعَمَهُۥٓ, tr:e-nut‘imu men lev yeşâu'llâhu et‘ameh, gloss:Allah dileseydi doyuracağı kimseyi biz mi doyuracağız, source:36:47}. Kehf suresinde Mûsâ ile Allah'ın kullarından biri {ar:عَبْدًۭا مِّنْ عِبَادِنَآ, tr:abden min ibâdinâ, gloss:kullarımızdan bir kul, source:18:65} bir kasabaya varır: {ar:ٱسْتَطْعَمَآ أَهْلَهَآ فَأَبَوْا۟ أَن يُضَيِّفُوهُمَا, tr:istat‘amâ ehlehâ fe-ebev en yudayyifûhumâ, gloss:halkından yemek istediler, onlar ise ikisini konuk etmeye yanaşmadılar, source:18:77}. Kul, yıkılmak üzere olan bir duvarı ücretsiz doğrultur. Sonra sebebini açıklar: {ar:وَأَمَّا ٱلْجِدَارُ فَكَانَ لِغُلَٰمَيْنِ يَتِيمَيْنِ فِى ٱلْمَدِينَةِ وَكَانَ تَحْتَهُۥ كَنزٌۭ لَّهُمَا وَكَانَ أَبُوهُمَا صَٰلِحًۭا, tr:ve emme'l-cidâru fe-kâne li-ġulâmeyni yetîmeyni fi'l-medîne, ve kâne tahtehû kenzun lehumâ, ve kâne ebûhumâ sâlihâ, gloss:duvara gelince, şehirde iki yetim oğlanındı; altında onlara ait bir hazine vardı ve babaları iyi bir adamdı, source:18:82}. Kimseyi doyurmayan bir kasabada iki yetimin malı Allah tarafından saklanmıştır. Bu, surenin adamlarının kendi rafını sakladığı sahnenin tersidir. Yûsuf suresinde, kökün fiilinin bir ölçeğin üzerine düştüğü bir cümle vardır. Kardeşler babalarına dönüp şöyle der: {ar:يَٰٓأَبَانَا مُنِعَ مِنَّا ٱلْكَيْلُ, tr:yâ ebânâ müni‘a minne'l-keyl, gloss:babamız, ölçek bizden esirgendi, source:12:63}. Mutaffifîn suresi dolu ölçeğin karşıtını aynı beddua kelimesiyle anar: {ar:وَيْلٌۭ لِّلْمُطَفِّفِينَ, tr:veylun li'l-mutaffifîn, gloss:ölçüyü eksik tutanların vay hâline, source:83:1}. Bunlar {ar:ٱلَّذِينَ إِذَا ٱكْتَالُوا۟ عَلَى ٱلنَّاسِ يَسْتَوْفُونَ, tr:ellezîne izektâlû ale'n-nâsi yestevfûn, gloss:insanlardan ölçüp aldıklarında tam alanlar, source:83:2}, {ar:وَإِذَا كَالُوهُمْ أَو وَّزَنُوهُمْ يُخْسِرُونَ, tr:ve izâ kâlûhum ev vezenûhum yuhsirûn, gloss:onlara ölçüp tarttıklarında ise eksik verenlerdir, source:83:3}. Nisâ suresi mirasın bölüşüldüğü anda evin kapısını açık tutar. Bölüşüme yakınlar, yetimler ve yoksullar geldiğinde {ar:فَٱرْزُقُوهُم مِّنْهُ وَقُولُوا۟ لَهُمْ قَوْلًۭا مَّعْرُوفًۭا, tr:fe'rzukûhum minhu ve kûlû lehum kavlen ma‘rûfâ, gloss:ondan onlara da verin ve onlara güzel söz söyleyin, source:4:8} denir. Buradaki "ma‘rûf", mâûnun "bütün iyilik" diye açıklandığı kelimedir.

Kaynaklar: 107:2 يَدُعُّ د ع ع B009; 107:2 يَدُعُّ د ع ع B002; 107:2 ٱلْيَتِيمَ ي ت م B001; 107:3 طَعَامِ ط ع م B001; 107:3 طَعَامِ ط ع م B002; 107:3 طَعَامِ ط ع م B004; 107:3 ٱلْمِسْكِينِ س ك ن B002; 107:3 ٱلْمِسْكِينِ س ك ن B003; 107:3 ٱلْمِسْكِينِ س ك ن B010; 107:5 سَاهُونَ س ه و B004; 107:7 ٱلْمَاعُونَ م ع ن B005; 107:7 ٱلْمَاعُونَ م ع ن B006; 107:7 ٱلْمَاعُونَ م ع ن B003; 107:7 وَيَمْنَعُونَ م ن ع B001

## Akan su

Mâûnun kökü suyu akarken adlandırır: {ar:ماء معين أي جار, tr:mâun ma‘în, ey câr, gloss:"ma‘în" su, akan sudur, source:"م ع ن,B001"}. Suyun yolunu da adlandırır: {ar:المعنان مجاري الماء في الوادي, tr:el-mu‘nânu mecâri'l-mâi fi'l-vâdî, gloss:"mu‘nân", vadide suyun aktığı yataklardır, source:"م ع ن,B001"}. Suyun vardığı yeri de adlandırır: {ar:أمعنت الأرض رويت وكلأ ممعون جرى فيه الماء, tr:em‘aneti'l-ardu ruviyet, ve kele'un mem‘ûnun cerâ fîhi'l-mâ', gloss:toprak suya kandı; içinden su akmış ota "mem‘ûn" denir, source:"م ع ن,B001"}. Suyun kendisi de bu adla anılır: {ar:يسمى الماء أيضا ماعونا, tr:yusemme'l-mâu eyden mâ‘ûnâ, gloss:suya da mâûn denir, source:"م ع ن,B005"}. İşleyiş şöyledir: Su vadinin yataklarından aşağı iner, toprağı kandırır, ot bitirir. Ot bitince hayvan oradan ayrılmaz. Yoksulun kökü bu durmayı da bilir: {ar:مرعى مسكن إذا كان كثيرا لا يخرج إلى الظعن عنه, tr:mer‘an müskinun izâ kâne kesîran lâ yuhracu ile'z-za‘ni anh, gloss:otlak, terk edip göçmeyi gerektirmeyecek kadar boldur, source:"س ك ن,B010"}. Üçüncü ayetteki yemek de suya kadar uzanır: {ar:والإطعام يقع حتى الماء, tr:ve'l-it‘âmu yeka‘u hatte'l-mâ’, gloss:yedirmek suya kadar varır, source:"ط ع م,B001"}. Kuran bu fiili ırmak suyu için kullanır. Tâlût askerlerine bir ırmakla sınanacaklarını söyler: {ar:وَمَن لَّمْ يَطْعَمْهُ فَإِنَّهُۥ مِنِّىٓ, tr:ve men lem yat‘amhu fe-innehû minnî, gloss:ondan tatmayan benimdir, source:2:249}.

Üçüncü ayetin yemeği ve yoksulu, ayetin anlamının yanında suyu ve yerleşmeyi de duyurur. Yedinci ayetin son kelimesinin yanında ise su akar. Esirgeyen el, aynı kökün diliyle {ar:مناع للخير, tr:mennâ‘un li'l-hayr, gloss:hayra hep engel olan, source:"م ن ع,B001"} olan kişi, bu sahnede bir yatağı tıkar. Akması kendi elinden çıkmamış bir suyu tutar.

Kuran "gördün mü" sorusunu tam bu suya yöneltir. Mülk suresinde Allah Peygamber'e şunu söylemesini emreder: {ar:قُلْ أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًۭا فَمَن يَأْتِيكُم بِمَآءٍۢ مَّعِينٍۭ, tr:kul eraeytum in asbaha mâukum ġavran fe-men ye'tîkum bi-mâin ma‘în, gloss:de ki: söyleyin bana, suyunuz yerin dibine çekiliverse size akan suyu kim getirir, source:67:30}. Surenin ilk kelimesi ile son kelimesinin kökü burada tek ayette buluşur. Bakış, akan suyun kimden geldiğine çevrilir. Mü'minûn suresinde Allah, Meryem oğlu ile annesine verdiği barınağı anlatır: {ar:وَءَاوَيْنَٰهُمَآ إِلَىٰ رَبْوَةٍۢ ذَاتِ قَرَارٍۢ وَمَعِينٍۢ, tr:ve âveynâhumâ ilâ rabvetin zâti karârin ve ma‘în, gloss:onları yerleşmeye elverişli, akarsuyu olan bir tepeye yerleştirdik, source:23:50}. "Barındırmak" fiili, yetime söylenen {ar:فَـَٔاوَىٰ, tr:fe-âvâ, gloss:barındırdı, source:93:6} ile aynıdır. Barınak, yerleşmeyle akan suyun bir arada bulunduğu yer olarak anlatılır.

Kaynaklar: 107:3 طَعَامِ ط ع م B001; 107:3 ٱلْمِسْكِينِ س ك ن B010; 107:7 ٱلْمَاعُونَ م ع ن B001; 107:7 ٱلْمَاعُونَ م ع ن B005; 107:7 وَيَمْنَعُونَ م ن ع B001

## Borç, hesap ve boyun eğiş

Birinci ayetin nesnesi bir alacak verecek ilişkisi kurar: {ar:بِٱلدِّينِ, tr:bi'd-dîn, gloss:dini, hesap ve karşılık gününü, source:107:1}. Kök hesabın görülüp ödenmesini adlandırır: {ar:يوم الدين أي يوم الحكم والحساب والجزاء, tr:yevmü'd-dîn, ey yevmü'l-hukmi ve'l-hisâbi ve'l-cezâ’, gloss:din günü; hüküm, hesap ve karşılık günü, source:"د ي ن,B002"}; {ar:الدين الجزاء والمكافأة, tr:ed-dînu'l-cezâu ve'l-mükâfee, gloss:din karşılık ve ödemedir, source:"د ي ن,B002"}. İnsanlar arasındaki borcu da adlandırır: {ar:داينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء, tr:dâyentü fülânen izâ âmeltehû deynen, immâ ahzen ve immâ i‘tâ’, gloss:biriyle borç alarak ya da vererek iş gördüğünde "dâyentü" dersin, source:"د ي ن,B003"}; {ar:دنت الرجل أقرضته, tr:dintü'r-racüle akradtüh, gloss:adama borç verdim, source:"د ي ن,B003"}. Bütün bunların altında bir boyun eğiş vardır: {ar:أصل واحد إليه يرجع فروعه كلها وهو جنس من الانقياد والذل, tr:aslun vâhidun ileyhi yerci‘u furû‘uhû küllühâ, ve huve cinsun mine'l-inkıyâdi ve'z-züll, gloss:bütün kollarının döndüğü tek bir asıl vardır; o da bir tür boyun eğiş ve alçalıştır, source:"د ي ن,B001"}; {ar:فالدين الطاعة, tr:fe'd-dînu't-tâ‘a, gloss:din itaattir, source:"د ي ن,B001"}. Fiil ise bu hesabı getireni yalancı saymaktır: {ar:كذبت فلانا نسبته إلى الكذب, tr:kezzebtü fülânen nesebtühû ile'l-kezib, gloss:filanı yalanladım, yani onu yalana nispet ettim, source:"ك ذ ب,B002"}. Yalanlayanın kendi fiilinin içinde, kalıplaşmış bir deyim olarak, tam tersi bir söz de durur: {ar:كذب عليكم الحج أي وجب, tr:kezebe aleykumu'l-hacc, ey vecebe, gloss:hac size borç oldu, yani üzerinize vacip oldu, source:"ك ذ ب,B003"}; {ar:كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك, tr:kezebe aleyke kezâ, bi-ma‘ne'l-iġrâ’, ey aleyke bih, ev kad vecebe aleyk, gloss:"kezebe aleyke" şunu yapmaya teşvik anlamındadır; yani ona sarıl ya da o sana vacip oldu, source:"ك ذ ب,B003"}. Borcu yalanlamak için kullanılan fiil, kendi içinde "bu senin üzerine borçtur" sözünü saklar.

Surenin son kelimesi de aynı hesabın içine girer: {ar:الماعون في الجاهلية كل منفعة وعطية وفي الإسلام الطاعة والزكاة, tr:el-mâ‘ûnu fi'l-câhiliyye küllü menfe‘atin ve atıyye, ve fi'l-islâmi't-tâ‘atu ve'z-zekât, gloss:mâûn cahiliyede her türlü yarar ve bağıştı, İslâm'da itaat ve zekâttır, source:"م ع ن,B005"}; {ar:الماعون الطاعة, tr:el-mâ‘ûnu't-tâ‘a, gloss:mâûn itaattir, source:"م ع ن,B005"}; {ar:الماعون يفسر بالزكاة والصدقة, tr:el-mâ‘ûnu yufesseru bi'z-zekâti ve's-sadaka, gloss:mâûn zekât ve sadaka diye açıklanır, source:"م ع ن,B005"}. Bir hakkın karşısında yapılabilecek iki şey aynı fiilde durur: {ar:أمعن بحقي ذهب به, tr:em‘ane bi-hakkî, zehebe bih, gloss:hakkımı alıp götürdü, source:"م ع ن,B004"}; {ar:أمعن لي بحقي إذا أقر به وانقاد, tr:em‘ane lî bi-hakkî izâ akarra bihî ve'nkâd, gloss:hakkımı tanıyıp boyun eğdiğinde "em‘ane lî bi-hakkî" denir, source:"م ع ن,B004"}. Bu son tanımdaki boyun eğiş, dinin kökünü tanımlayan boyun eğişle aynı kelimedir. Böylece surenin ilk nesnesi ile son nesnesi itaatte buluşur. Esirgemek de vermenin tersi olarak bu hesaba yazılır: {ar:ضد العطية, tr:ziddu'l-atıyye, gloss:bağışın karşıtı, source:"م ن ع,B001"}.

Sahne iki taraf arasında tutulan bir hesap defteridir. Borç alınır ve verilir, bir gün hesap kapatılıp ödenir. Birinci ayet, defteri getireni yalancı sayan adamı gösterir. İkinci ve üçüncü ayetlerde defterin satırları açılır: Yetimin hakkı kapıdan itilir, yoksulun payı hiç anılmaz. Yedinci ayetteki küçük borç da ödenmez. Hesabı inkâr eden, sonunda en ucuz borcunu da inkâr eder. Kuran sure boyunca bu hesabı açık tutar. İnfitâr suresinde Allah insana seslenir: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ مَا غَرَّكَ بِرَبِّكَ ٱلْكَرِيمِ, tr:yâ eyyühe'l-insânu mâ ġarraka bi-rabbike'l-kerîm, gloss:ey insan, seni cömert Rabbine karşı ne aldattı, source:82:6}. Birkaç ayet sonra bu surenin ifadesi aynen geçer: {ar:كَلَّا بَلْ تُكَذِّبُونَ بِٱلدِّينِ, tr:kellâ bel tükezzibûne bi'd-dîn, gloss:hayır, siz dini yalanlıyorsunuz, source:82:9}. Hesabın sahibi Fâtiha'da adlandırılır: {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:mâliki yevmi'd-dîn, gloss:din gününün sahibi, source:1:4}. Meâric suresi bu sureyi madde madde tersine çevirir. İnsan hırslı yaratılmıştır {ar:إِنَّ ٱلْإِنسَٰنَ خُلِقَ هَلُوعًا, tr:inne'l-insâne hulika helû‘â, gloss:insan hırslı yaratıldı, source:70:19}. Hayra dokunulunca {ar:وَإِذَا مَسَّهُ ٱلْخَيْرُ مَنُوعًا, tr:ve izâ messehu'l-hayru menû‘â, gloss:ona bir hayır dokununca esirgeyendir, source:70:21}. Ardından istisna gelir: {ar:إِلَّا ٱلْمُصَلِّينَ, tr:ille'l-musallîn, gloss:namaz kılanlar hariç, source:70:22}. Bunlar namazlarını sürdürenlerdir {source:70:23}. Mallarında bir hak bulunur: {ar:وَٱلَّذِينَ فِىٓ أَمْوَٰلِهِمْ حَقٌّۭ مَّعْلُومٌۭ, tr:ve'llezîne fî emvâlihim hakkun ma‘lûm, gloss:mallarında belirli bir hak bulunanlar, source:70:24}, {ar:لِّلسَّآئِلِ وَٱلْمَحْرُومِ, tr:li's-sâili ve'l-mahrûm, gloss:isteyen ve yoksun kalan için, source:70:25}. Ve {ar:وَٱلَّذِينَ يُصَدِّقُونَ بِيَوْمِ ٱلدِّينِ, tr:ve'llezîne yusaddikûne bi-yevmi'd-dîn, gloss:din gününü doğrulayanlar, source:70:26}. Esirgemek, namaz kılanlar, sürdürülen namaz, maldaki hak ve dini doğrulamak: Bu surede dağılan her parça orada yerine oturur. Fussilet suresinde Peygamber'e şunu söylemesi emredilir: "Ben de sizin gibi bir insanım." Aynı ayet şöyle biter: {ar:وَوَيْلٌۭ لِّلْمُشْرِكِينَ, tr:ve veylun li'l-müşrikîn, gloss:vay hâline ortak koşanların, source:41:6}. Ortak koşanlar {ar:ٱلَّذِينَ لَا يُؤْتُونَ ٱلزَّكَوٰةَ وَهُم بِٱلْءَاخِرَةِ هُمْ كَٰفِرُونَ, tr:ellezîne lâ yü'tûne'z-zekâte ve hum bi'l-âhireti hum kâfirûn, gloss:zekâtı vermeyenler ve ahireti inkâr edenlerdir, source:41:7}. İsrâ suresi yoksulun payını hak diye anar: {ar:وَءَاتِ ذَا ٱلْقُرْبَىٰ حَقَّهُۥ وَٱلْمِسْكِينَ وَٱبْنَ ٱلسَّبِيلِ, tr:ve âti ze'l-kurbâ hakkahû ve'l-miskîne ve'bne's-sebîl, gloss:yakına hakkını ver, yoksula ve yolda kalmışa da, source:17:26}. Zâriyât suresi de aynısını yapar: {ar:وَفِىٓ أَمْوَٰلِهِمْ حَقٌّۭ لِّلسَّآئِلِ وَٱلْمَحْرُومِ, tr:ve fî emvâlihim hakkun li's-sâili ve'l-mahrûm, gloss:mallarında isteyen ve yoksun kalan için bir hak vardı, source:51:19}.

Kaynaklar: 107:1 بِٱلدِّينِ د ي ن B002; 107:1 بِٱلدِّينِ د ي ن B003; 107:1 بِٱلدِّينِ د ي ن B001; 107:1 يُكَذِّبُ ك ذ ب B002; 107:1 يُكَذِّبُ ك ذ ب B003; 107:7 ٱلْمَاعُونَ م ع ن B005; 107:7 ٱلْمَاعُونَ م ع ن B004; 107:7 وَيَمْنَعُونَ م ن ع B001

## Dışa dönük namaz: huzur veren dua

Namazın kökü iki yön taşır. Birincisi belirli sınırları olan bir ibadettir: {ar:الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة, tr:es-salâtu'lletî câe bihe'ş-şer‘u mine'r-rükû‘i ve's-sücûdi ve sâiri hudûdi's-salâh, gloss:şeriatın getirdiği namaz; rükû, secde ve namazın öteki sınırları, source:"ص ل و,B003"}. İkincisi bir insandan ötekine giden bir dilektir: {ar:الصلاة وهي الدعاء, tr:es-salâtu ve hiye'd-du‘â’, gloss:salât, yani dua, source:"ص ل و,B002"}; {ar:صلوات الرسول للمسلمين دعاؤه لهم, tr:salavâtu'r-resûli li'l-müslimîn du‘âuhû lehum, gloss:Peygamber'in Müslümanlar için salâtı, onlara duasıdır, source:"ص ل و,B002"}; {ar:صلاة الله للمسلمين تزكيته إياهم, tr:salâtu'llâhi li'l-müslimîn tezkiyetuhû iyyâhum, gloss:Allah'ın Müslümanlara salâtı, onları arındırmasıdır, source:"ص ل و,B002"}. Yoksulun kökünün bir kolu bu ikinci yönü bir ayetle birleştirir: {ar:إن صلواتك سكن لهم, tr:inne salavâtike sekenun lehum, gloss:senin duan onlar için bir huzurdur, source:"س ك ن,B004"}. Aynı kol huzuru da tanımlar: {ar:كل ما سكنت إليه من محبوب, tr:küllü mâ sekente ileyhi min mahbûb, gloss:sevilen şeylerden yanında huzur bulduğun her şey, source:"س ك ن,B004"}.

İşleyiş Tevbe suresinde tam bir döngü olarak verilir. Allah Peygamber'e şöyle der: {ar:خُذْ مِنْ أَمْوَٰلِهِمْ صَدَقَةًۭ تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا وَصَلِّ عَلَيْهِمْ ۖ إِنَّ صَلَوٰتَكَ سَكَنٌۭ لَّهُمْ, tr:huz min emvâlihim sadakaten tutahhiruhum ve tüzekkîhim bihâ ve salli aleyhim, inne salâteke sekenun lehum, gloss:onların mallarından, kendilerini temizleyip arındıracağın bir sadaka al ve onlar için dua et; senin duan onlara huzur verir, source:9:103}. Maldan bir pay ayrılır, o pay vereni temizler, alan veren için dua eder ve dua verenin içini yatıştırır. Namaz, mal ve huzur tek bir hareketin halkalarıdır. Mâûnun zekât diye de açıklanması {source:"م ع ن,B005"} bu halkanın son ayetteki ucunu verir.

Surenin adamları bu halkayı ortasından koparır. Dördüncü ayet onlara namaz kılanlar der; görünen ibadet yerindedir. Beşinci ayet kalbin o ibadetten gittiğini söyler. Üçüncü ayetteki yoksulun kökü, namazın başkasına vermesi gereken huzuru duyurur. Bu huzur hiçbir yere ulaşmaz, çünkü yedinci ayette pay ayrılmaz. Namazın başkasına yönelen yüzü kapanmış, yalnızca seyirciye dönük yüzü kalmıştır.

Kuran bu iki şeyin birbirinden ayrılmadığını başka ağızlardan da söyletir. Şuayb'in kavmi ona alayla şöyle sorar: {ar:أَصَلَوٰتُكَ تَأْمُرُكَ أَن نَّتْرُكَ مَا يَعْبُدُ ءَابَآؤُنَآ أَوْ أَن نَّفْعَلَ فِىٓ أَمْوَٰلِنَا مَا نَشَٰٓؤُا۟, tr:e-salâtuke te'muruke en netruke mâ ya‘budu âbâunâ ev en nef‘ale fî emvâlinâ mâ neşâ’, gloss:namazın mı sana emrediyor, atalarımızın taptığını bırakmamızı ya da mallarımız hakkında dilediğimizi yapmaktan vazgeçmemizi, source:11:87}. Karşı çıkanlar bile namazın malın kullanılışına uzandığını görmektedir. Meryem suresinde beşikteki çocuk, yani Îsâ, kendisi hakkında şöyle der: {ar:وَأَوْصَٰنِى بِٱلصَّلَوٰةِ وَٱلزَّكَوٰةِ مَا دُمْتُ حَيًّۭا, tr:ve evsânî bi's-salâti ve'z-zekâti mâ dumtu hayyâ, gloss:yaşadıkça bana namazı ve zekâtı emretti, source:19:31}. Bakara suresinde İsrâiloğulları'ndan alınan söz bu surenin kişilerini sayar: anne baba, yakınlar, yetimler, yoksullar, güzel söz, namaz ve zekât. Ardından şu gelir: {ar:ثُمَّ تَوَلَّيْتُمْ إِلَّا قَلِيلًۭا مِّنكُمْ وَأَنتُم مُّعْرِضُونَ, tr:summe tevelleytum illâ kalîlen minkum ve entum mu‘ridûn, gloss:sonra pek azınız dışında yüz çevirdiniz; zaten dönüp gidenlersiniz, source:2:83}. Tevbe suresinde Allah münafıkların sadakalarının neden kabul edilmediğini açıklar: {ar:وَمَا مَنَعَهُمْ أَن تُقْبَلَ مِنْهُمْ نَفَقَٰتُهُمْ, tr:ve mâ mene‘ahum en tukbele minhum nefekâtuhum, gloss:harcamalarının kabul edilmesine engel olan şey, source:9:54}. Sebeplerden ikisi bu surenin ikilisidir: {ar:وَلَا يَأْتُونَ ٱلصَّلَوٰةَ إِلَّا وَهُمْ كُسَالَىٰ وَلَا يُنفِقُونَ إِلَّا وَهُمْ كَٰرِهُونَ, tr:ve lâ ye'tûne's-salâte illâ ve hum küsâlâ, ve lâ yünfikûne illâ ve hum kârihûn, gloss:namaza ancak üşenerek gelirler, ancak isteksizce harcarlar, source:9:54}. Ankebût suresi namazın insanın içinde nasıl iş gördüğünü söyler: {ar:إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ, tr:inne's-salâte tenhâ ani'l-fahşâi ve'l-münker, gloss:namaz hayâsızlıktan ve kötülükten alıkoyar, source:29:45}. Meryem suresi de bırakılan namazı anlatır: {ar:أَضَاعُوا۟ ٱلصَّلَوٰةَ وَٱتَّبَعُوا۟ ٱلشَّهَوَٰتِ, tr:edâu's-salâte ve'ttebeu'ş-şehevât, gloss:namazı yitirdiler ve arzularının peşine düştüler, source:19:59}.

Kaynaklar: 107:4 لِّلْمُصَلِّينَ ص ل و B003; 107:4 لِّلْمُصَلِّينَ ص ل و B002; 107:5 صَلَاتِهِمْ ص ل و B003; 107:5 صَلَاتِهِمْ ص ل و B002; 107:3 ٱلْمِسْكِينِ س ك ن B004; 107:7 ٱلْمَاعُونَ م ع ن B005

## Buluşmalar

Görme imgesi ile gözden kaçma imgesi tek bir cümlede buluşur: Suhâ yıldızı {ar:خفي جدا فيسهى عن رؤيته, tr:hafiyyun ciddâ fe-yushâ an ru'yetih, gloss:pek gizlidir, onu görmekten gaflet edilir, source:"س ه و,B005"}. Surenin beşinci ayetindeki kökle altıncı ayetindeki kök bu cümlede yan yana durur. Gözden kaçırmak ile göze görünmek tek bir görme alanının iki ucudur. Adamlar sönük olanı, yani yetimi, yoksulu ve kendi namazlarındaki kalbi atlar. Kendilerinin ise atlanmamasını isterler. Alak suresindeki sahne bu buluşmaya namazı ve yarıda kalan yolu ekler. Bir "gördün mü" ile açılır, namaz kılan bir kulu engelleyeni gösterir, onun yalanlayıp yüz çevirdiğini söyler ve görenin Allah olduğunu hatırlatarak kapanır {source:96:9} {source:96:13} {source:96:14}. Burada bakış imgesi ile yalanın yüzey ve yol imgesi birbirinin içindedir. İnsanların gözü için kılınan namaz, gözü hiç ayrılmayan birinin önünde kılınmaktadır.

İtiş ile ateş Tûr suresinde tek harekette birleşir. Yetimi iten, ateşe itilir {source:52:13}, ve ona yalanladığı ateşin bu olduğu söylenir {source:52:14}. Böylece birinci ve ikinci ayetin iki fiili, yalanlamak ve itmek, dördüncü ayetin ateşini taşıyan kökle bir araya gelir. Hâkka suresinde ateş fiili ile teşvik etmeme aynı kişinin hesabında yan yana yazılır {source:69:31} {source:69:34}. Bu kez evin ocağı ile zayıfın üstündeki eller birbirine bağlanır. Teşvik edilmeyen yemek, pişirilmeyen ocağın karşılığında ateşe katlanmaya dönüşür.

Bütün imgeleri tek bir ağızdan dile getiren sahne Müddessir suresindedir. Cennet halkı suçlulara sorar: {ar:مَا سَلَكَكُمْ فِى سَقَرَ, tr:mâ selekekum fî sakar, gloss:sizi Sakar'a ne soktu, source:74:42}. Cevap bu surenin kelime dizisini ateşin içinden verir: {ar:قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ, tr:kâlû lem neku mine'l-musallîn, gloss:dediler ki: namaz kılanlardan değildik, source:74:43}, {ar:وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ, tr:ve lem neku nut‘imu'l-miskîn, gloss:yoksulu doyurmazdık, source:74:44}, {ar:وَكُنَّا نَخُوضُ مَعَ ٱلْخَآئِضِينَ, tr:ve künnâ nehûdu ma‘a'l-hâidîn, gloss:dalıp gidenlerle birlikte biz de dalardık, source:74:45}, {ar:وَكُنَّا نُكَذِّبُ بِيَوْمِ ٱلدِّينِ, tr:ve künnâ nükezzibu bi-yevmi'd-dîn, gloss:din gününü yalanlardık, source:74:46}. Namaz, doyurmak, gaflete dalmak ve hesabı yalanlamak burada tek bir itirafta toplanır ve bu itiraf ateşin içinden yapılır. Bu suredeki boş namaz, kapalı kap, gözden kaçırılan yoksul ve inkâr edilen hesap, orada bir hikâyenin sırası olarak geri döner.

Ev, su ve borç imgeleri tek bir kelimede, mâûnda buluşur. Aynı ad tencereyi ve kovayı {source:"م ع ن,B005"}, vadiden akan suyu {source:"م ع ن,B001"} ve itaatle zekâtı {source:"م ع ن,B005"} taşır. Rafta duran kap, yataktan akan su ve ödenmesi gereken pay tek bir şeyin üç görünüşüdür. Barındırma fiili de bu buluşmayı Kuran'da iki kez kurar. Yetim için {source:93:6}, Meryem oğlu ve annesi için kullanılır; ikincisinde barınak yerleşme ile akan suyun bir arada olduğu yerdir {source:23:50}. İtişin kökü de evle ellerin buluştuğu yerdir. Aynı harfler bir adamın küçük çocuklarını {source:"د ع ع,B009"}, sarsılarak doldurulan tabağı {source:"د ع ع,B002"} ve kapıdan kovan itişi {source:"د ع ع,B001"} taşır. Esirgemenin kökü de eli sıkı adamı {source:"م ن ع,B001"} ve babasız çocuğun yitirdiği koruyucu halkayı {source:"م ن ع,B003"} birlikte taşır.

Borç imgesi ile dışa dönük namaz imgesi Meâric suresinde birlikte sahnelenir. Esirgeyen insan, namazını sürdürenler, malındaki bilinen hak ve din gününü doğrulamak aynı dizide yer alır {source:70:21} {source:70:24} {source:70:26}. Tevbe suresindeki döngüde de pay, dua ve huzur birbirine bağlanır {source:9:103}. Bu sure, aynı halkaların çözülmüş hâlidir.

Surenin hareketi bu buluşmalarla taşınır. Sure bir bakış emriyle ve yalanlanan bir hesapla başlar. Bakışı önce bir evin kapısına götürür: Yetimi iten el, yoksulun yemeği için açılmayan ağız. Sonra namaz yerine geçer ve orada ateşi de taşıyan bir ada beddua düşer. Ardından seyircinin gözüne, en sonunda yeniden evin rafındaki küçük kaplara döner. Bir uçta "gördün mü" ile gösteriş vardır, yani bakış ve bakılmak. Öbür uçta din ile mâûn vardır, yani hesap ve küçük borç. İki uç da itaatte buluşur. Ortadaki ad, namaz kılanlar, hem halkayı kuracak ibadeti hem de halka kopunca gelen ateşi kökünde taşır.

