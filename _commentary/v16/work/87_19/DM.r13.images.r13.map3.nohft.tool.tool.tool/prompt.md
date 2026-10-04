Focus: 87:19. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/87_19/D.r13/context.md =====
# 87:19 — focus

صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ

Anchor translation (canonical reading, reference only):

İbrahim'in ve Musa'nın sayfalarında.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | صُحُفِ | صُحُف | ص ح ف | N |
| 2 | إِبْرَٰهِيمَ | إِبْرَاهِيم |  | PN |
| 3 | وَمُوسَىٰ | مُوسَىٰ |  | CONJ;PN |


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
- 87:8 وَنُيَسِّرُكَ لِلْيُسْرَىٰ
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
- 87:19 ◀ focus صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ


===== _commentary/v16/work/87_19/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ص ح ف (root_000845) — identity root of صُحُفِ (w1)

- **B001** yayılmış geniş yüzey — yayılmış geniş yüzey · yeryüzünün görünen yüzü · yüz derisi
  أصل صحيح يدل على انبساط في شيء وسعة (maqayis); الصحيف وجه الأرض (maqayis); صحيفة الوجه بشرة جلده (ayn); الصحيفة المبسوط من الشيء كصحيفة الوجه (mufradat)
- **B002** yazı yaprağı veya kitap — yazı yazılan yaprak veya kitap · yazı yaprakları · yazı yaprakları · yazı yaprakları için seyrek bir çoğul biçim
  الصحيفة وهي التي يكتب فيها والجمع صحائف والصحف (maqayis); الصحف جمع الصحيفة (ayn); الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها (jamhara); الصحيفة الكتاب والجمع صحف وصحائف (sihah); الصحيفة التي يكتب فيها وجمعها صحائف وصحف (mufradat)
- **B003** iki kapak arasında toplanmış yazı yaprakları — iki kapak arasında toplanmış yazı yaprakları bütünü · yazı yapraklarını iki kapak arasında toplamak
  سمي المصحف مصحفا لأنه أصحف أي جعل جامعا للصحف المكتوبة بين الدفتين (ayn); المصحف لأنه صحف جمعت (jamhara); مصحف مأخوذة من أصحف أي جمعت فيه الصحف (sihah); المصحف ما جعل جامعا للصحف المكتوبة (mufradat)
- **B004** yayvan çanak; küçük su biriktirme çukuru — geniş ve yayvan çanak · geniş ve yayvan çanaklar · su için yapılmış küçük biriktirme çukurları
  الصحفة القصعة المسلنطحة (maqayis); الصحاف مناقع صغار تتخذ للماء (maqayis); الصحفة شبه القصعة المسلنطحة العريضة (ayn); الصحفة القصعة وتجمع صحافا (jamhara); الصحفة كالقصعة والجمع صحاف (sihah); الصحفة مثل قصعة عريضة (mufradat)
- **B005** harf benzerliğinden doğan yanlış okuma veya aktarım — benzer harfleri karıştırmaktan doğan yanlış okuma veya aktarım · benzer harfleri karıştırıp metni yanlış aktaran kişi
  الصحفي الذي يروي الخطأ عن قراءة الصحف بأشباه الحروف (ayn); التصحيف الخطأ في الصحيفة (sihah); التصحيف قراءة المصحف وروايته على غير ما هو لاشتباه حروفه (mufradat)

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 87:19, and ## Buluşmalar) =====
## Toplanan, tutulan, düşürülen: okuma, unutma ve sayfalar

Altıncı ayet {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız da unutmayacaksın, source:87:6} der. Yedinci ayet buna bir istisna ekler: {ar:إِلَّا مَا شَآءَ ٱللَّهُ, tr:illâ mâ şâallâh, gloss:Allah'ın dilediği hariç, source:87:7}. Kelimelerin aileleri hafızayı bir kaplar dizisi olarak gösterir. قرأ toplamaktır: {ar:قرأت الشيء قرآنا جمعته وضممت بعضه إلى بعض, tr:karaeu'ş-şey'e kur'ânen ceme'tuhû ve damamtu ba'dahû ilâ ba'd, gloss:bir şeyi okudum yani onu toplayıp parçalarını birbirine kattım, source:"ق ر ء,B001"}. Okuma harfleri ve kelimeleri birbirine eklemektir: {ar:القراءة ضم الحروف والكلمات بعضها إلى بعض في الترتيل, tr:el-kırâe dammu'l-hurûfi ve'l-kelimâti ba'dihâ ilâ ba'din fi't-tertîl, gloss:okuma harfleri ve kelimeleri tertil içinde birbirine eklemektir, source:"ق ر ء,B001"}. Ayetteki fiil başkasına bu toplamayı vermektir: {ar:أقرأت غيري أقرئه إقراء, tr:akra'tu ğayrî ukriuhû ikrâen, gloss:başkasına okuttum, source:"ق ر ء,B002"}. Unutmak ise emanet edilmiş bir şeyi tutamamaktır: {ar:ترك الإنسان ضبط ما استودع إما لضعف قلبه وإما عن غفلة وإما عن قصد, tr:terku'l-insâni dabta mâ'stûdia immâ li-da'fi kalbihî ve immâ an ğafletin ve immâ an kasd, gloss:insanın kendisine emanet edileni tutmayı bırakmasıdır; ya kalbinin zayıflığından ya gaflettendir ya da kasıtla, source:"ن س ي,B001"}. {ar:النسيان خلاف الذكر والحفظ, tr:en-nisyân hilâfu'ẕ-ẕikri ve'l-hıfz, gloss:unutmak anmanın ve korumanın zıddıdır, source:"ن س ي,B001"}. Unutmak bırakmak da demektir: {ar:النسيان الترك، نسوا الله فنسيهم, tr:en-nisyânu't-terk nesullâhe fe-nesiyehum, gloss:unutmak bırakmaktır; Allah'ı unuttular o da onları unuttu, source:"ن س ي,B002"}. Ve göç edenlerin geride bıraktığı döküntüdür: {ar:النسي ما سقط من منازل المرتحلين من رذال أمتعتهم, tr:en-nisy mâ sekata min menâzili'l-murtehilîne min ruẕâli emtiatihim, gloss:nisy göç edenlerin konak yerlerinden düşen değersiz eşyadır, source:"ن س ي,B003"}.

Dokuzuncu, onuncu ve on beşinci ayetlerdeki ذكر kökü bu düşüşün karşıtıdır: {ar:ذكرت الشيء خلاف نسيته, tr:ẕekertu'ş-şey'e hilâfu nesîtuh, gloss:bir şeyi andım unuttumun zıddıdır, source:"ذ ك ر,B003"}. {ar:الذكر الحفظ للشيء وهو مني على ذكر, tr:eẕ-ẕikru'l-hıfzu li'ş-şey'i ve huve minnî alâ ẕikr, gloss:zikir bir şeyi korumaktır; o benim aklımdadır, source:"ذ ك ر,B003"}. {ar:والتذكر طلب ما فات, tr:ve't-teẕekkuru talebu mâ fât, gloss:tezekkür kaçanı aramaktır, source:"ذ ك ر,B003"}. Öğüt bir şeyi akla getiren araçtır: {ar:التذكرة ما تستذكر به الحاجة, tr:et-teẕkira mâ tusteẕkeru bihi'l-hâce, gloss:teẕkira bir ihtiyacın hatırlandığı şeydir, source:"ذ ك ر,B009"}. Bir peygamberin kitabının adı da aynı köktendir: {ar:الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر, tr:eẕ-ẕikru'l-kitâbu'lleẕî fîhi tafsîlu'd-dîn ve kullu kitâbin min kutubi'l-enbiyâi ẕikr, gloss:zikir dinin ayrıntılarını içeren kitaptır ve peygamberlerin her kitabı bir zikirdir, source:"ذ ك ر,B006"}. Bu anlam dokuzuncu ayetteki öğüdü on sekizinci ve on dokuzuncu ayetlerdeki sayfalara bağlar. Sayfalar, üzerine yazı yazılan deri parçalarıdır: {ar:الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها, tr:es-suhuf vâhidetuhâ sahîfe ve hiye'l-kıtatu min edemin ebyada ev rakkın yuktebu fîhâ, gloss:suhuf sahîfenin çoğuludur; sahîfe üzerine yazılan ak deri ya da parşömen parçasıdır, source:"ص ح ف,B002"}. Mushaf bu sayfaları bir araya toplayandır: {ar:المصحف ما جعل جامعا للصحف المكتوبة, tr:el-mushaf mâ cuile câmian li's-suhufi'l-mektûbe, gloss:mushaf yazılı sayfaları toplamak için yapılmış şeydir, source:"ص ح ف,B003"}. "İlk" kelimesi bir şeyin başlangıcıdır: {ar:الأول وهو مبتدأ الشيء, tr:el-evvel ve huve mubtedeu'ş-şey', gloss:evvel bir şeyin başlangıcıdır, source:"ء و ل,B001"}. On altıncı ayetteki tercih fiilinin kökü de söz aktarmayı verir: {ar:أثرت الحديث إذا ذكرته عن غيرك وحديث مأثور, tr:eŝertu'l-hadîŝe iẕâ ẕekertehû an ğayrike ve hadîŝun me'ŝûr, gloss:bir sözü başkasından naklettiğinde eŝertu denir; aktarılan söze me'ŝûr denir, source:"ء ث ر,B002"}.

Bu aileler altıncı ayetle son ayet arasında bir yol çizer. Okutulan söz toplanır ve birbirine eklenir. Unutulmayınca tutulur. Unutulursa göç yerindeki döküntü gibi geride kalır. Anılarak geri çağrılır. Sonunda deriye yazılıp sayfa olur, sayfalar da bir arada toplanır. On sekizinci ayetteki {ar:إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:inne hâẕâ le-fi's-suhufi'l-ûlâ, gloss:bu elbette ilk sayfalarda vardır, source:87:18} cümlesi, okutulan sözün yalnız Peygamber'in hafızasında değil, İbrahim'in ve Musa'nın sayfalarında da toplanmış olduğunu söyler. Düz bir anlatımda "unutmayacaksın" bir vaattir. Aile resmi ise bu vaadin işleyişini gösterir: toplayan Allah'tır, ve toplanan şey düşürülmez.

Kur'an toplama ile okumayı aynı cümlede verir. Allah Peygamber'e vahyi acele ile tekrarlamamasını söyler: {ar:لَا تُحَرِّكْ بِهِۦ لِسَانَكَ لِتَعْجَلَ بِهِۦٓ, tr:lâ tuharrik bihî lisâneke li-ta'cele bih, gloss:onu aceleyle almak için dilini kıpırdatma, source:75:16}, {ar:إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ, tr:inne aleynâ cem'ahû ve kur'ânah, gloss:onu toplamak ve okutmak bize düşer, source:75:17}, {ar:فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ, tr:fe-iẕâ kara'nâhu fettebi' kur'ânah, gloss:onu okuduğumuzda sen okunuşunu izle, source:75:18}. Başka bir yerde de {ar:وَلَا تَعْجَلْ بِٱلْقُرْءَانِ مِن قَبْلِ أَن يُقْضَىٰٓ إِلَيْكَ وَحْيُهُۥ ۖ وَقُل رَّبِّ زِدْنِى عِلْمًۭا, tr:ve lâ ta'cel bi'l-kur'âni min kabli en yukdâ ileyke vahyuh ve kul rabbi zidnî ilmâ, gloss:sana vahyi tamamlanmadan Kur'an'ı okumakta acele etme ve Rabbim ilmimi artır de, source:20:114} denir. Hemen ardından unutmanın ilk örneği gelir: {ar:وَلَقَدْ عَهِدْنَآ إِلَىٰٓ ءَادَمَ مِن قَبْلُ فَنَسِىَ وَلَمْ نَجِدْ لَهُۥ عَزْمًۭا, tr:ve lekad ahidnâ ilâ âdeme min kablu fe-nesiye ve lem necid lehû azmâ, gloss:andolsun daha önce Adem'e söz vermiştik; o unuttu ve onda bir kararlılık bulmadık, source:20:115}. Firavun Musa'ya {ar:فَمَا بَالُ ٱلْقُرُونِ ٱلْأُولَىٰ, tr:fe-mâ bâlu'l-kurûni'l-ûlâ, gloss:ya önceki nesillerin durumu ne olacak, source:20:51} diye sorduğunda Musa şöyle cevap verir: {ar:عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى, tr:ilmuhâ inde rabbî fî kitâb lâ yadillu rabbî ve lâ yensâ, gloss:onların bilgisi Rabbimin katında bir kitaptadır; Rabbim ne yanılır ne unutur, source:20:52}. Bu cevapta "ilk" kelimesi, yazılı kitap ve unutmayan Rab bir aradadır. Unutmanın karşılığı da aynı kelimeyle verilir: {ar:كَذَٰلِكَ أَتَتْكَ ءَايَٰتُنَا فَنَسِيتَهَا ۖ وَكَذَٰلِكَ ٱلْيَوْمَ تُنسَىٰ, tr:keẕâlike etetke âyâtunâ fe-nesîtehâ ve keẕâlike'l-yevme tunsâ, gloss:ayetlerimiz sana geldi ama sen onları unuttun; bugün de sen öyle unutulursun, source:20:126}. Münafıklar için {ar:نَسُوا۟ ٱللَّهَ فَنَسِيَهُمْ, tr:nesullâhe fe-nesiyehum, gloss:Allah'ı unuttular o da onları unuttu, source:9:67} denir. Müminlere de {ar:وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ, tr:ve lâ tekûnû kelleẕîne nesullâhe fe-ensâhum enfusehum, gloss:Allah'ı unutan ve bu yüzden Allah'ın onlara kendilerini unutturduğu kimseler gibi olmayın, source:59:19} denir. Yedinci ayetteki istisnanın bir benzeri Peygamber'e verilen bir emirde de geçer: {ar:إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ وَٱذْكُر رَّبَّكَ إِذَا نَسِيتَ, tr:illâ en yeşâallâh veẕkur rabbeke iẕâ nesît, gloss:ancak Allah dilerse; unuttuğunda Rabbini an, source:18:24}. Unutmaya karşı çare anmaktır.

Sayfaların içeriği başka bir yerde kısmen verilir: {ar:أَمْ لَمْ يُنَبَّأْ بِمَا فِى صُحُفِ مُوسَىٰ, tr:em lem yunebbe' bi-mâ fî suhufi mûsâ, gloss:yoksa Musa'nın sayfalarındakiler ona haber verilmedi mi, source:53:36}, {ar:وَإِبْرَٰهِيمَ ٱلَّذِى وَفَّىٰٓ, tr:ve ibrâhîme'lleẕî veffâ, gloss:ve sözünü tam yerine getiren İbrahim'in sayfalarındakiler, source:53:37}. Sayfalarda yazanların ilki şudur: {ar:أَلَّا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ, tr:ellâ teziru vâziratun vizra uhrâ, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz, source:53:38}. Ardından {ar:وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ, tr:ve en leyse li'l-insâni illâ mâ seâ, gloss:insan için kendi çabasından başkası yoktur, source:53:39} gelir, ve dizi şöyle biter: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Her kişinin kendi payını taşıması, bu surenin iki kişiye ayrılan ortasıyla aynı konudur. Delil isteyenlere de {ar:أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:e-ve lem te'tihim beyyinetu mâ fi's-suhufi'l-ûlâ, gloss:ilk sayfalardakinin açık delili onlara gelmedi mi, source:20:133} denir. Başka bir yerde öğüt ve sayfa birlikte anılır: {ar:كَلَّآ إِنَّهَا تَذْكِرَةٌۭ, tr:kellâ innehâ teẕkira, gloss:hayır bu bir öğüttür, source:80:11}, {ar:فَمَن شَآءَ ذَكَرَهُۥ, tr:fe-men şâe ẕekerah, gloss:dileyen onu anar, source:80:12}, {ar:فِى صُحُفٍۢ مُّكَرَّمَةٍۢ, tr:fî suhufin mukerrame, gloss:değerli sayfalardadır, source:80:13}, {ar:مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ, tr:merfûatin mutahhara, gloss:yükseltilmiş ve arınmış, source:80:14}. Sayfalar yükseltilmiş ve arınmıştır. Bu iki sıfat surenin birinci ayetindeki yüksekliği ve on dördüncü ayetindeki arınmayı sayfalara taşır. Kur'an kendisi için de {ar:وَإِنَّهُۥ لَفِى زُبُرِ ٱلْأَوَّلِينَ, tr:ve innehû le-fî zuburi'l-evvelîn, gloss:o öncekilerin kitaplarında da vardır, source:26:196} der.

Kaynaklar: 87:6 سَنُقْرِئُكَ ق ر ء B001; 87:6 سَنُقْرِئُكَ ق ر ء B002; 87:6 تَنسَىٰٓ ن س ي B001; 87:6 تَنسَىٰٓ ن س ي B002; 87:6 تَنسَىٰٓ ن س ي B003; 87:9 ٱلذِّكْرَىٰ ذ ك ر B003; 87:10 يَذَّكَّرُ ذ ك ر B003; 87:9 ٱلذِّكْرَىٰ ذ ك ر B009; 87:9 ٱلذِّكْرَىٰ ذ ك ر B006; 87:18 ٱلصُّحُفِ ص ح ف B002; 87:19 صُحُفِ ص ح ف B003; 87:18 ٱلْأُولَىٰ ء و ل B001; 87:16 تُؤْثِرُونَ ء ث ر B002

## Buluşmalar

İmgelerin çoğu, surenin son ayetinde adı geçen Musa'nın hikâyesinde buluşur. Musa uzakta bir ateş görür ve {ar:أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ecidu ale'n-nâri hudâ, gloss:ateşin başında bir yol gösteren bulurum, source:20:10} umuduyla ona yönelir. Uzaktan görülen ateşin sahnesi ile yol sahnesi burada aynı cümlededir. Ateşin başında önce seçim gelir: {ar:وَأَنَا ٱخْتَرْتُكَ, tr:ve ene'htertuk, gloss:seni ben seçtim, source:20:13}. Sonra namaz ve anma gelir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14}. Sonra gizli olan gelir: {ar:أَكَادُ أُخْفِيهَا, tr:ekâdu uhfîhâ, gloss:onu neredeyse gizli tutuyorum, source:20:15}. Başka bir anlatımda ateşin başında tesbih söylenir: {ar:وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve subhânallâhi rabbi'l-âlemîn, gloss:Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu sahnede surenin on ikinci ve on beşinci ayetleri arasındaki karşıtlık bir kişinin yolculuğunda çözülür. Aynı ateşe yaklaşan biri onun içine sokulmaz. Ateş ona yol, seçilmişlik, namaz ve anma verir. Surede bu iki son iki ayrı kişiye düşer: on ikinci ayetteki kişi ateşe girer, on beşinci ayetteki kişi namaz kılar. Kelimelerin harf benzerliği bu ayrılığı kulakta da duyurur.

İkinci büyük buluşma selin sahnesidir. Gökten inen suyun vadilerde {ar:بِقَدَرِهَا, tr:bi-kaderihâ, gloss:kendi ölçülerince, source:13:17} akması, ölçüp biçme sahnesini çağırır. Selin taşıdığı köpük, otlağın vardığı döküntüdür. İnsanların {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâr, gloss:ateşte üzerine yaktıkları şeyden, source:13:17} çıkan köpük ise ateşin sahnesine girer. Faydalı olanın yerde kalması da öğüdün ve kalıcılığın sahnesidir. Kurumuş otun tencerenin köpüğüyle aynı adı taşıması, bu iki köpüğün Arapçada zaten tek bir kelimede birleştiğini gösterir. Bu ayet surenin beşinci ayetinden on yedinci ayetine uzanan çizgiyi tek bir manzaraya sığdırır. Bir yanda giden döküntü, öbür yanda kalan fayda vardır.

Üçüncü buluşma, Musa'nın karşısındaki sihirbazların sahnesidir. Sihirbazlar secdeye kapanır. Firavun kendi azabının daha çetin ve {ar:وَأَبْقَىٰ, tr:ve ebkâ, gloss:ve daha kalıcı, source:20:71} olduğunu söyler. Sihirbazlar da onu {ar:لَن نُّؤْثِرَكَ, tr:len nu'ŝirak, gloss:seni asla tercih etmeyiz, source:20:72} diye reddeder, yalnızca {ar:هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:hâẕihi'l-hayâte'd-dunyâ, gloss:bu dünya hayatı, source:20:72} üzerinde hüküm verebileceğini söyler ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Sonra suçlu için {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:20:74} der, iman edenler için {ar:ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:ed-derecâtu'l-ulâ, gloss:en yüce dereceler, source:20:75} der, ve hepsini {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76} sözüyle bağlar. Bu birkaç ayette seçim, kalıcı hayat, yükseklik ve yarılan tarlanın kelimeleri birlikte konuşur. Firavun'un "en yüce" iddiası da başka bir anlatımda bu sahneye eklenir. Surenin ikinci yarısı, on üçüncü ayetten on yedinci ayete kadar, neredeyse kelimesi kelimesine Musa'nın hikâyesindeki bir topluluğun ağzından gelmiştir. Son ayetin Musa'nın sayfalarını anması da bu yüzden önem taşır.

Dördüncü buluşma ot ile seçimdir. Dünya hayatının kuruyan ota benzetildiği ayetin hemen ardından kalıcı iyi işlerin daha hayırlı olduğu söylenir. Dünya hayatı başka bir yerde bir {ar:زَهْرَةَ, tr:zehrate, gloss:çiçek, source:20:131} olarak anılır, ve aynı ayet {ar:خَيْرٌۭ وَأَبْقَىٰ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:20:131} diye biter. Otlağın sahnesi seçimin sahnesine bu yolla girer. Beşinci ayetteki ot ile on altıncı ayetteki tercih edilen hayat aynı nesnedir. Kalıcı olan ise ayıklanıp seçilen şeydir. Tarlanın sahnesi bu iki uç arasında bir yol açar. Kalıcı iyilik anlamına gelen kurtuluş kelimesi on dördüncü ayette, toprağı yaran çiftçinin kelimesiyle söylenir. Yabani ot kendi haline kalınca kurur ve selle gider. İşlenen toprağın ürünü ise büyür, hakkı verilir ve geriye kalan bir pay bırakır. Biri dünya tarlası, öbürü ahiret tarlasıdır.

Beşinci buluşma, yaratma fiillerinde zanaat ile bedenin birleşmesidir. İkinci ayetteki ikili hem yontulmuş oku hem de ceninin biçimlenmesini anlatır. Rahimden başlayan ayetin toprağın yağmurla titreşmesiyle bitmesi, beden ile otlağı da birbirine bağlar. Aynı aile, üçüncü ayetteki ölçmeyi pay ölçmeye de taşır, ve on altıncı ayetteki tercih bir pay seçimine döner. Değneği ateşte doğrultmanın fiili on ikinci ayetin fiilidir. Bu fiil aynı ateşin düzelten bir işi ile içine düşenin katlandığı bir işi olduğunu duyurur. Bu son bağ dilin yankısıdır, ayetin sözü değildir.

Bu buluşmalar surenin hareketini taşır. Sure tesbih emriyle ve yükseklikle açılır. Ölçen, yontan ve yol gösteren Rabbin işiyle devam eder. Yağmurun çıkardığı ve selin götürdüğü ot ile sona gelen bir ömür gösterir. Sonra sözün toplanıp unutulmamasına, sunulan öğüde ve öğüt karşısında ikiye ayrılan insanlara geçer. Biri ateşe girer ve ne ölü ne diri kalır. Öbürü arınır, Rabbinin adını anar ve namaz kılar, yani surenin başındaki emri yerine getirir. Ardından seçim gelir: yakın olan öne konmuştur, ama arkadan gelen daha hayırlı ve daha kalıcıdır. Sure, bu sözün ilk sayfalarda, ateşin başında namaz ve anma emrini alan Musa'nın ve Rabbinden kendisini puttan uzak tutmasını isteyen İbrahim'in sayfalarında yazılı olduğunu söyleyerek kapanır.

