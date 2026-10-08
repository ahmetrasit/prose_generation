Focus: 92:8. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/92_8/D.r13/context.md =====
# 92:8 — focus

وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ

Anchor translation (canonical reading, reference only):

Ama kim cimrilik eder ve kendini yeterli sayarsa,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَأَمَّا | أَمَّا |  | CONJ;EXL |
| 2 | مَنۢ | مَن |  | COND |
| 3 | بَخِلَ | بَخِلَ | ب خ ل | V |
| 4 | وَٱسْتَغْنَىٰ | ٱسْتَغْنَىٰ | غ ن ي | CONJ;V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 92 — full text (context; no pericope)

- 92:1 وَٱلَّيْلِ إِذَا يَغْشَىٰ
- 92:2 وَٱلنَّهَارِ إِذَا تَجَلَّىٰ
- 92:3 وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ
- 92:4 إِنَّ سَعْيَكُمْ لَشَتَّىٰ
- 92:5 فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
- 92:6 وَصَدَّقَ بِٱلْحُسْنَىٰ
- 92:7 فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
- 92:8 ◀ focus وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
- 92:9 وَكَذَّبَ بِٱلْحُسْنَىٰ
- 92:10 فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- 92:11 وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
- 92:12 إِنَّ عَلَيْنَا لَلْهُدَىٰ
- 92:13 وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- 92:14 فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- 92:15 لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- 92:16 ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- 92:17 وَسَيُجَنَّبُهَا ٱلْأَتْقَى
- 92:18 ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- 92:19 وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- 92:20 إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- 92:21 وَلَسَوْفَ يَرْضَىٰ


===== _commentary/v16/work/92_8/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ب خ ل (root_000089) — identity root of بَخِلَ (w3)

- **B001** eldeki varlıkları haksız yere esirgeme — cimrilik; eldeki varlıkları haksız yere esirgeme · cimrilik etmek; verilmesi gerekeni esirgemek · cimrilik eden kişi · sık sık cimrilik eden; cimri · cimriliği huy edinmiş kişi · cimri diye nitelenen kişi · tek bir cimrilik davranışı · kişinin kendi varlıklarını esirgemesi · başkasına ait varlıklar konusunda esirgeyici davranma; daha ağır kınanan biçim
  البخل والبخل؛ رجل بخيل وباخل؛ فهو بخال (maqayis); بخل بخلا وبخلا فهو بخيل بخال مبخل؛ والبخلة بخل مرة واحدة (ayn); البخل إمساك المقتنيات عما لا يحق حبسها عنه؛ ويقابله الجود؛ البخل ضربان بخل بقنيات نفسه وبخل بقنيات غيره (mufradat)

## غ ن ي (root_001110) — identity root of وَٱسْتَغْنَىٰ (w4)

- **B001** maddi bolluk ve ihtiyaçtan bağımsızlık — maddi zenginlik, bolluk ve ihtiyaçsızlık · varlıklı, zengin · zenginleşmek veya başkasına ihtiyaç duymayacak duruma gelmek · ona ihtiyaç duymamak · onunla yetinip başka bir şeye ihtiyaç duymamak · bir şeye ihtiyaç duymama durumu · zenginlik ve bolluk · gönül tokluğu ve az şeye ihtiyaç duyma · zengin etmek veya yoksunluğunu gidermek · Kur'an'la yetinip başka bir şeye ihtiyaç duymamak
  الغنى في المال (maqayis;tahdhib)؛ الغنى مقصور في المال واستغنى الرجل أصاب غنى (ayn;tahdhib)؛ الغنى مقصور اليسار وتغنى الرجل أي استغنى (sihah)؛ الغني ذو الوفر (ayn;tahdhib)؛ عدم الحاجات وقلة الحاجات وكثرة القنيات (mufradat)؛ تغنيت وتغانيت بمعنى استغنيت (maqayis;tahdhib)
- **B002** ihtiyacı karşılayıp yarar sağlama ve yerini tutma — yeterlilik, ihtiyacı karşılama ve yarar · onun yerine yetmek, ihtiyacını karşılamak ve yarar sağlamak · bu sana yetmez ve yarar sağlamaz · yeterli ve ihtiyacı karşılayan · birinin yerini tutan yeterlilik ve işlev · zararını benden uzak tut
  الغناء بالفتح الكفاية ولا يغني أي لا يكفي (maqayis)؛ الغناء الاستغناء والكفاية ورجل مغن أي مجزئ (ayn)؛ ما يغني عنك هذا أي ما يجزئ وما ينفع والغناء بالفتح النفع (sihah)؛ الإجزاء والكفاية ورجل مغن أي مجزئ كاف (tahdhib)؛ أغناني كذا وأغنى عنه كذا إذا كفاه (mufradat)
- **B003** sesle ezgi söyleme, dinleme ve ezgili okuma — şarkı söyleme, ezgili seslendirme ve dinleti · şarkı; ezgili söylenen parça · şarkı söylemek · şarkı söylemek veya sesi ezgili ve duygulu kullanmak · Kur'an'ı hüzünlü, yumuşak ve ezgili bir sesle okumak
  الغناء من الصوت والأغنية اللون من الغناء (maqayis)؛ الغناء ممدود في الصوت وغنى يغني أغنية وغناء (ayn)؛ الأغنية الغناء والجمع الأغاني والغناء بالكسر من السماع (sihah)؛ الغناء الصوت ممدود والتطريب وتحزين القراءة وترقيقها (tahdhib)؛ غنى أغنية وغناء (mufradat)
- **B004** bir yerde uzun süre kalıp yaşama — bir yerde oturmak ve uzun süre kalmak · sanki daha dün orada hiç yaşamamıştı · bir topluluğun oturduğu evler ve yurtlar · oturma eylemi veya oturulan yer
  غني القوم في دارهم أقاموا ومغانيهم منازلهم (maqayis)؛ غني القوم في المحلة طال مقامهم فيها وكأن لم يغن بالأمس أي كأن لم يكن (ayn)؛ غنى بالمكان أي أقام وغني أي عاش والمغنى واحد المغاني (sihah)؛ غني القوم في دارهم إذا طال مقامهم والمغاني المنازل (tahdhib)؛ غنى في مكان كذا إذا طال مقامه فيه والمغنى للمصدر وللمكان (mufradat)
- **B005** süsten bağımsız sayılan; bazen genç, güzel veya evli kadın — eşi veya güzelliği sayesinde süse ihtiyaç duymadığı düşünülen; ayrıca genç, güzel ya da evli kadın · bu niteliklerle anılan kadınlar; bazı kullanımlarda genç, güzel, evli ya da genel olarak kadınlar
  الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي (maqayis)؛ الغانية الشابة المتزوجة غنيت بزوجها وغنيت بجمالها عن الزينة (ayn)؛ الغانية الجارية التي غنيت بزوجها وقد تكون التي غنيت بحسنها وجمالها (sihah)؛ الغواني ذوات الأزواج أو الشواب أو الجارية الحسناء أو كل امرأة (tahdhib)؛ الغانية المستغنية بزوجها عن الزينة أو بحسنها عن التزين (mufradat)
- **B006** evlenme ve evlendirme — evlenme; bekâr kişi için koruyucu sayılan evlilik · gelinleri evlendirme
  الأغناء إملاكات العرائس (tahdhib)؛ الغنى التزويج (tahdhib)؛ الغنى حصن للعزب أي التزويج (tahdhib)

===== _commentary/v16/out/s092/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 92:8, and ## Buluşmalar) =====
## Yetmeyen mal: bolluk, darlık, yeterlik

Surenin kolaylık ve zorluk kelimeleri aynı zamanda varlık ve yoklukun adıdır. Yedinci ayetin kökü zenginliktir: {ar:الميسرة والميسرة: السعة والغنى؛ واليسار واليسارة: الغنى، وقد أيسر الرجل أي استغنى, tr:el-meysera ve'l-meysüra: es-seatü ve'l-ğınâ; ve'l-yesâru ve'l-yesâratü: el-ğınâ ve kad eysera'r-racülü ey isteğnâ, gloss:meysere bolluk ve zenginliktir; yesâr zenginliktir; adam eysera yani zenginleşti, source:"ي س ر,B003"}. Sekizinci ayetin fiili de aynı denklemi tersinden kurar: {ar:الغنى مقصور اليسار وتغنى الرجل أي استغنى, tr:el-ğınâ maksûru'l-yesâr ve teğannâ'r-racülü ey isteğnâ, gloss:ğınâ yesâr demektir; adam zenginleşti yani müstağni oldu, source:"غ ن ي,B001"}. Kelimenin iki yüzü bir arada verilir: {ar:عدم الحاجات وقلة الحاجات وكثرة القنيات, tr:ademü'l-hâcât ve kılletü'l-hâcât ve kesretü'l-kınyât, gloss:ihtiyaçların olmaması, azlığı ve edinilmiş malların çokluğu, source:"غ ن ي,B001"}. Onuncu ayetin kökü ise boş eldir: {ar:العسر قلة ذات اليد, tr:el-usru kılletü zâti'l-yed, gloss:usr elde olanın azlığıdır, source:"ع س ر,B002"}. Bir dalı bolluktan darlığa düşüşü anlatır: {ar:أعسر الرجل إذا صار من ميسرة إلى عسرة, tr:a'sera'r-racülü izâ sâra min meyseratin ilâ usra, gloss:adam bolluktan darlığa düşünce a'sera denir, source:"ع س ر,B002"}. Sekizinci ayetin öteki fiili de malı tutmaktır: {ar:البخل إمساك المقتنيات عما لا يحق حبسها عنه؛ ويقابله الجود, tr:el-buhlü imsâkü'l-muktenayâti ammâ lâ yehıkku habsühâ anh; ve yukâbilühü'l-cûd, gloss:cimrilik edinilen malları alıkonmaması gerekenden tutmaktır; karşıtı cömertliktir, source:"ب خ ل,B001"}. Böylece {ar:وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ, tr:ve emmâ men bahıle ve'steğnâ, gloss:cimrilik edip kendini yeterli görene gelince, source:92:8} ayetindeki adam, kelimelerin ailesinde, yesâr içindeki adamdır. Ona verilen yol ise onuncu ayetin zorluğudur, yani bolluktan darlığa düşüş. Surenin kolaylık ve zorluk ekseni, düz anlamın yanında, para kesesinin dolup boşalmasını da duyurur.

On birinci ayet bu ailenin düğümünü atar: {ar:وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ, tr:ve mâ yuğnî anhü mâlüh, gloss:malı ona bir şey kazandırmaz, source:92:11}. Fiil sekizinci ayetteki "kendini yeterli gördü" fiiliyle aynı köktendir ve burada yetmek demektir: {ar:الغناء بالفتح الكفاية ولا يغني أي لا يكفي, tr:el-ğanâu bi'l-feth el-kifâye ve lâ yuğnî ey lâ yekfî, gloss:ğanâ yeterliktir; lâ yuğnî yetmez demektir, source:"غ ن ي,B002"}. Aynı dalda {ar:ما يغني عنك هذا أي ما يجزئ وما ينفع, tr:mâ yuğnî anke hâzâ ey mâ yüczi'ü ve mâ yenfa', gloss:bu sana yetmez yani karşılamaz ve fayda vermez, source:"غ ن ي,B002"} de denir. Kendini yeterli sayan adamın kendini yeterli saymasını sağlayan şey, ona yetmez. Mal kelimesi de edinmeyi anlatır: {ar:تمول فلان مالا إذا اتخذ قنية من المال, tr:temevvele fülânün mâlen izet-tehaze kınyeten mine'l-mâl, gloss:biri kendine mal edindi, source:"م و ل,B001"}. Ayetin zaman kelimesi de düşüş anıdır. Ölümün yok edişi aynı kökten gelir: {ar:الردى وهو الهلاك؛ أرداه الله أهلكه, tr:er-redâ ve hüve'l-helâk; erdâhu'llâhu ehlekeh, gloss:redâ helaktır; Allah onu helak etti, source:"ر د ي,B003"}. Birinci ayetin örtme fiili de bu ana uzanır: {ar:غشي عليه فهو مغشي عليه وهي الغشية وكذلك غشية الموت, tr:ğuşiye aleyhi fehüve mağşiyyün aleyhi ve hiye'l-ğaşye ve kezâlike ğaşyetü'l-mevt, gloss:bayıldı, baygın oldu; ölüm baygınlığı da böyledir, source:"غ ش و,B005"}. Gecenin örtüsü insanın kendi üstüne inince ölümün baygınlığı olur ve elde tutulan mal o anda elden kayar. On dokuzuncu ayetin karşılık fiili de aynı yeterlik anlamını taşır: {ar:فلان ذو غناء وجزاء, tr:fülânün zû ğanâin ve cezâ', gloss:filan yeten ve karşılayan biridir, source:"ج ز ي,B002"}; {ar:الجزاء الغناء والكفاية؛ لا يجزي والد عن ولده, tr:el-cezâu'l-ğanâu ve'l-kifâye; lâ yeczî vâlidün an veledih, gloss:cezâ yetmek ve karşılamaktır; baba oğlunun yerine bir şey karşılamaz, source:"ج ز ي,B002"}. Cimrinin malı ona yetmez. Verenin ise kimseden bir karşılık beklemeye ihtiyacı yoktur, çünkü kimseye borcunu ödemek için vermez.

Kur'an kendini yeterli görmenin sonucunu açıkça gösterir: {ar:كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ, tr:kellâ inne'l-insâne le-yatğâ, gloss:hayır; insan gerçekten azar, source:96:6}; {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en raâhü'steğnâ, gloss:kendini yeterli gördüğünde, source:96:7}. Bir başka surede Peygamber, yanına gelen kör adamdan yüz çevirip kendini yeterli görenle ilgilendiği için uyarılır: {ar:أَمَّا مَنِ ٱسْتَغْنَىٰ, tr:emmâ meni'steğnâ, gloss:kendini yeterli görene gelince, source:80:5}; {ar:فَأَنتَ لَهُۥ تَصَدَّىٰ, tr:fe-ente lehû tesaddâ, gloss:sen onunla ilgileniyorsun, source:80:6}. On birinci ayetin cümlesi Ebu Leheb için de neredeyse kelimesi kelimesine söylenir: {ar:مَآ أَغْنَىٰ عَنْهُ مَالُهُۥ وَمَا كَسَبَ, tr:mâ ağnâ anhü mâlühû ve mâ keseb, gloss:ne malı ne de kazandığı ona bir şey kazandırdı, source:111:2}. Hemen ardından {ar:سَيَصْلَىٰ نَارًۭا ذَاتَ لَهَبٍۢ, tr:se-yaslâ nâran zâte leheb, gloss:alevli bir ateşe girecek, source:111:3} gelir. Kitabı sol elinden verilen adam da aynı cümleyi kendi ağzıyla söyler: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ, tr:mâ ağnâ annî mâliyeh, gloss:malım bana bir şey kazandırmadı, source:69:28}. Malın ölümsüzlük vereceğini sanan için {ar:يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ, tr:yahsebü enne mâlehû ahledeh, gloss:malının kendisini ölümsüz kılacağını sanır, source:104:3} denir. İbrahim'in duasında o gün şöyle anılır: {ar:يَوْمَ لَا يَنفَعُ مَالٌۭ وَلَا بَنُونَ, tr:yevme lâ yenfau mâlün ve lâ benûn, gloss:ne malın ne oğulların fayda verdiği gün, source:26:88}. Darlıktaki borçluya ise süre tanınır ve vermek önerilir: {ar:وَإِن كَانَ ذُو عُسْرَةٍۢ فَنَظِرَةٌ إِلَىٰ مَيْسَرَةٍۢ ۚ وَأَن تَصَدَّقُوا۟ خَيْرٌۭ لَّكُمْ, tr:ve in kâne zû usratin fe-nazıratün ilâ meyseratin ve en tesaddekû hayrun leküm, gloss:borçlu darlıktaysa bolluğa kadar beklemek gerekir; bağışlamanız sizin için daha hayırlıdır, source:2:280}. Bu ayette surenin iki kökü para anlamıyla geçer ve altıncı ayetin kökü de çözüm olarak sunulur. Harcamanın ölçüsü de bu iki kelimeyle verilir: {ar:لِيُنفِقْ ذُو سَعَةٍۢ مِّن سَعَتِهِۦ, tr:li-yünfik zû seatin min seatih, gloss:genişlik sahibi genişliğinden harcasın, source:65:7}. Aynı ayet {ar:سَيَجْعَلُ ٱللَّهُ بَعْدَ عُسْرٍۢ يُسْرًۭا, tr:se-yec'alu'llâhu ba'de usrin yüsrâ, gloss:Allah zorluktan sonra bir kolaylık verecektir, source:65:7} diye kapanır. Cimrilik ve yüz çevirme bir ayette birleşir: {ar:وَمَن يَبْخَلْ فَإِنَّمَا يَبْخَلُ عَن نَّفْسِهِۦ ۚ وَٱللَّهُ ٱلْغَنِىُّ وَأَنتُمُ ٱلْفُقَرَآءُ ۚ وَإِن تَتَوَلَّوْا۟, tr:ve men yebhal fe-innemâ yebhalü an nefsih va'llâhü'l-ğaniyyü ve entümü'l-fukarâ ve in tetevellev, gloss:cimrilik eden ancak kendine cimrilik eder; Allah zengindir, sizler yoksulsunuz; eğer yüz çevirirseniz, source:47:38}. Bu ayette surenin sekizinci ve on altıncı ayetlerinin üç kökü bir arada durur. Gerçek yeterliğin kime ait olduğunu da söyler. Darlık korkusunun kaynağı da adlandırılır: {ar:ٱلشَّيْطَٰنُ يَعِدُكُمُ ٱلْفَقْرَ, tr:eş-şeytânu yaıdükümü'l-fakr, gloss:şeytan size yoksulluk vaat eder, source:2:268}. Bir sonraki surede ise zenginleştiren Allah'tır: {ar:وَوَجَدَكَ عَآئِلًۭا فَأَغْنَىٰ, tr:ve vecedeke âilen fe-ağnâ, gloss:seni yoksul buldu ve zenginleştirdi, source:93:8}. Ölümün eşiğinde verilmemiş olanın pişmanlığı da sahnelenir: {ar:رَبِّ لَوْلَآ أَخَّرْتَنِىٓ إِلَىٰٓ أَجَلٍۢ قَرِيبٍۢ فَأَصَّدَّقَ, tr:rabbi levlâ ahhartenî ilâ ecelin karîbin fe-essaddaka, gloss:Rabbim beni yakın bir süreye kadar erteleseydin de sadaka verseydim, source:63:10}. Mal yetmediği anda istenen tek şey, onu vermek için bir süredir.

Kaynaklar: 92:1 يَغْشَىٰ غ ش و B005; 92:7 لِلْيُسْرَىٰ ي س ر B003; 92:8 بَخِلَ ب خ ل B001; 92:8 وَٱسْتَغْنَىٰ غ ن ي B001; 92:10 لِلْعُسْرَىٰ ع س ر B002; 92:11 يُغْنِى غ ن ي B002; 92:11 مَالُهُۥٓ م و ل B001; 92:11 تَرَدَّىٰٓ ر د ي B003; 92:19 تُجْزَىٰٓ ج ز ي B002

## El: uzanan, sıkan, borç soran

Beşinci ayetin fiili bir el hareketidir: {ar:العطو التناول باليد, tr:el-atvü't-tenâvülü bi'l-yed, gloss:atv elle uzanıp almaktır, source:"ع ط و,B001"}. Örnek sahnesi bir ceylandır: {ar:الظبي العاطي الرافع يديه إلى الشجرة ليتناول من الورق, tr:ez-zabyü'l-âtı'r-râfiu yedeyhi ile'ş-şecerati li-yetenâvele mine'l-varak, gloss:âtî ceylan yaprak koparmak için ön ayaklarını ağaca kaldırandır, source:"ع ط و,B001"}. Vermek bu uzanmadan türer: {ar:منه اشتق الإعطاء والمعاطاة المناولة والعطاء اسم لما يعطى وهي العطية, tr:minhü'ştukka'l-i'tâu ve'l-muâtâtü'l-münâvele ve'l-atâu'smün limâ yu'tâ ve hiye'l-atıyye, gloss:vermek bundan türemiştir; muâtât elden ele vermektir; atâ verilen şeyin adıdır, source:"ع ط و,B002"}. Aynı uzanma eğriye de dönebilir: {ar:التعاطي تناول ما ليس له بحق, tr:et-teâtî tenâvülü mâ leyse lehû bi-hakk, gloss:teâtî hakkı olmayana uzanmaktır, source:"ع ط و,B004"}. Dilenen bir avuç da olur: {ar:يستعطي الناس بكفه وفي كفه استعطاء إذا سألهم وطلب إليهم, tr:yesta'tı'n-nâse bi-keffihî ve fî keffihi'sti'tâ' izâ seelehüm ve talebe ileyhim, gloss:avucuyla insanlardan dilenir, source:"ع ط و,B005"}. Tek kök, alan, veren, kapan ve dilenen eli bir arada tutar. Ayetteki el ise yalnızca uzatan eldir. On sekizinci ayetin fiili aynı hareketi tekrarlar: {ar:آتاه إيتاء أي أعطاه وآتاه أيضا أي أتى به, tr:âtâhu îtâen ey a'tâh ve âtâhu eyzan ey etâ bih, gloss:âtâ verdi demektir; bir şeyi getirdi demek de olur, source:"ء ت ي,B002"}. Veren eli getiren bir ayakla birleştirir. Altıncı ayetin kökü de verilen şeyi adlandırır: {ar:الصدقة ما يتصدق به المرء عن نفسه وماله, tr:es-sadakatü mâ yetesaddaku bihi'l-mer'ü an nefsihî ve mâlih, gloss:sadaka kişinin kendisi ve malı adına verdiğidir, source:"ص د ق,B006"}. Sekizinci ayetin cimriliği ise sıkı tutan avuçtur. Az önce geçen tanımın ilk kelimesi {ar:إمساك, tr:imsâk, gloss:tutma, source:"ب خ ل,B001"} idi.

On dokuzuncu ayet elin ikinci anlamını açar: {ar:وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ, tr:ve mâ li-ehadin indehû min ni'metin tüczâ, gloss:yanında hiç kimsenin karşılığı ödenecek bir iyiliği yoktur, source:92:19}. Nimet bir eldir: {ar:النعمة اليد والصنيعة والمنة وما أنعم به عليك, tr:en-ni'metü'l-yedü ve's-sanîatü ve'l-minnetü ve mâ en'ame bihî aleyk, gloss:nimet el, iyilik, minnet ve sana bağışlanan şeydir, source:"ن ع م,B001"}. Birinin sana bir eli varsa, sende onun bir alacağı vardır. Karşılık fiili de iki yöne işler: {ar:جزى يجزي جزاء أي كافأ بالإحسان وبالإساءة, tr:cezâ yeczî cezâen ey kâfee bi'l-ihsâni ve bi'l-isâe, gloss:cezâ iyilikle de kötülükle de karşılık vermektir, source:"ج ز ي,B001"}. Bir dalı borcun tahsilidir: {ar:تجازيت ديني على فلان إذا تقاضيته, tr:tecâzeytü deynî alâ fülânin izâ tekâdaytüh, gloss:filandaki alacağımı tahsil ettim, source:"ج ز ي,B003"}. Onuncu ayetin kökü de bu sahnede sert bir alacaklıdır: {ar:عسرته أنا أعسره إذا طالبته بدينك وهو معسر ولم تنظره إلى ميسرته, tr:asartühû ene a'suruhû izâ tâlebtehû bi-deynike ve hüve mu'sirun ve lem tünzirhu ilâ meyseratih, gloss:darlıktaki borçludan alacağını isteyip onu bolluğa kadar beklemezsen asartühû denir, source:"ع س ر,B003"}. On birinci ayetin cübbesi de bu ailede borçtur: {ar:يسمى الدين رداء, tr:yüsemma'd-deynü ridâen, gloss:borca cübbe denir, source:"ر د ي,B004"}. Sahne bir borç ve alacak dünyasıdır: her iyilik bir eldir, her el bir alacak bırakır ve alacak bir gün tahsil edilir. On dokuzuncu ayet veren kişiyi bu dünyanın dışına koyar. O malını, birinin ona uzattığı bir eli ödemek için vermez. Bu yüzden vermesi bir borç ödemesi değildir.

Dördüncü ve on altıncı ayetlerin kökleri bu el dünyasının en ağır sahnesini, köleliği taşır. Koşu kelimesinin bir dalı köleye aittir: {ar:سعاية العبد إذا كوتب أن يسعى فيما يفك رقبته, tr:siâyetü'l-abdi izâ kûtibe en yes'â fîmâ yefükkü rakabeteh, gloss:köle bir sözleşmeye bağlanınca boynunu çözecek bedel için çalışmasına siâye denir, source:"س ع ي,B005"}. Yüz çevirme fiilinin kökü azat edeni ve azat edileni adlandırır: {ar:المولى المعتق والحليف والولي؛ الولي ولي النعم, tr:el-mevle'l-mu'tiku ve'l-halîfü ve'l-veliyy; el-veliyyu veliyyü'n-niam, gloss:mevlâ azat eden, müttefik ve dosttur; velî nimetlerin sahibidir, source:"و ل ي,B005"}. Kısaca {ar:مولى النعمة, tr:mevla'n-ni'me, gloss:nimetin efendisi, source:"و ل ي,B005"} denir. Azat edilen, azat edene bir el borçludur. Yani nimet ile mevlâ kelimeleri azatlık bağıyla birbirine bağlanır. Karşılık da {ar:مكافأته إياه, tr:mükâfeetühû iyyâh, gloss:ona denk karşılık vermesi, source:"ج ز ي,B001"} diye tanımlanır. Surenin on altıncı ayeti bu kökün yüz çevirme anlamını kullanır. On dokuzuncu ayetin veren kişisi ise kimsenin mevlâsı olmayı istemez ve kimsenin eline borçlu değildir. Kur'an elin bu iki uç durumunu sahneler. Allah şunu buyurur: {ar:وَلَا تَجْعَلْ يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ وَلَا تَبْسُطْهَا كُلَّ ٱلْبَسْطِ, tr:ve lâ tec'al yedeke mağlûleten ilâ unukike ve lâ tebsuthâ külle'l-bast, gloss:elini boynuna bağlı tutma, onu büsbütün de açma, source:17:29}. Cimrilerin malı boyunlarına geçecektir: {ar:سَيُطَوَّقُونَ مَا بَخِلُوا۟ بِهِۦ يَوْمَ ٱلْقِيَٰمَةِ, tr:se-yutavvakûne mâ bahılû bihî yevme'l-kıyâme, gloss:cimrilik ettikleri şey kıyamet günü boyunlarına dolanacak, source:3:180}. Borç cübbesinin omza, cimrinin malının boyna geçmesi aynı yere düşer. Bağını kaybeden bahçe sahibinin eli de boş kalır: {ar:فَأَصْبَحَ يُقَلِّبُ كَفَّيْهِ عَلَىٰ مَآ أَنفَقَ فِيهَا, tr:fe-asbaha yükallibü keffeyhi alâ mâ enfeka fîhâ, gloss:ona harcadıkları için avuçlarını ovuşturur hâle geldi, source:18:42}. Bir iyiliği borç hâline getirmenin örneği Firavun'dur. Firavun Musa'ya şunu söyler: {ar:أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا, tr:elem nürabbike fînâ velîdâ, gloss:seni çocukken aramızda büyütmedik mi, source:26:18}. Musa şöyle cevap verir: {ar:وَتِلْكَ نِعْمَةٌۭ تَمُنُّهَا عَلَىَّ أَنْ عَبَّدتَّ بَنِىٓ إِسْرَٰٓءِيلَ, tr:ve tilke ni'metün temunnühâ aleyye en abbedte benî isrâîl, gloss:başıma kaktığın o iyilik, İsrailoğullarını köleleştirmiş olmandır, source:26:22}. Büyütme, nimet, minnet ve kölelik tek konuşmadadır. Verilen bir iyilik geri tahsil edilmek istenince kölelik zincirine dönüşür. Veren kişiye de aynı yasak konur: {ar:ثُمَّ لَا يُتْبِعُونَ مَآ أَنفَقُوا۟ مَنًّۭا وَلَآ أَذًۭى, tr:sümme lâ yütbiûne mâ enfekû mennen ve lâ ezâ, gloss:sonra harcadıklarının ardından başa kakmazlar ve incitmezler, source:2:262}. Bir başka ayette {ar:وَلَا تَمْنُن تَسْتَكْثِرُ, tr:ve lâ temnün testeksir, gloss:çoğunu umarak iyilik yapma, source:74:6} denir. İyilikle karşılık ise Allah'ın ölçüsüdür: {ar:هَلْ جَزَآءُ ٱلْإِحْسَٰنِ إِلَّا ٱلْإِحْسَٰنُ, tr:hel cezâu'l-ihsâni ille'l-ihsân, gloss:iyiliğin karşılığı iyilikten başka mıdır, source:55:60}. Kölenin azadı da açıkça buyrulur. Sözleşme isteyen köleler için {ar:وَٱلَّذِينَ يَبْتَغُونَ ٱلْكِتَٰبَ مِمَّا مَلَكَتْ أَيْمَٰنُكُمْ فَكَاتِبُوهُمْ, tr:ve'llezîne yebteğûne'l-kitâbe mimmâ meleket eymânüküm fe-kâtibûhüm, gloss:ellerinizin altındakilerden sözleşme isteyenlerle sözleşme yapın, source:24:33} denir ve aynı ayet {ar:وَءَاتُوهُم مِّن مَّالِ ٱللَّهِ ٱلَّذِىٓ ءَاتَىٰكُمْ, tr:ve âtûhüm min mâli'llâhi'llezî âtâküm, gloss:Allah'ın size verdiği maldan onlara verin, source:24:33} diye sürer. Arama fiili ve verme fiili surede olduğu gibi burada da yan yanadır. Bir kölenin hem Allah'ın hem de Peygamberin nimetine mazhar oluşu da anılır: {ar:لِلَّذِىٓ أَنْعَمَ ٱللَّهُ عَلَيْهِ وَأَنْعَمْتَ عَلَيْهِ, tr:li'llezî en'ama'llâhu aleyhi ve en'amte aleyh, gloss:Allah'ın ve senin nimet verdiğin kişiye, source:33:37}. Ayetin devamında adı Zeyd olarak geçer.

Kaynaklar: 92:4 سَعْيَكُمْ س ع ي B005; 92:5 أَعْطَىٰ ع ط و B001; 92:5 أَعْطَىٰ ع ط و B002; 92:5 أَعْطَىٰ ع ط و B004; 92:5 أَعْطَىٰ ع ط و B005; 92:6 وَصَدَّقَ ص د ق B006; 92:8 بَخِلَ ب خ ل B001; 92:10 لِلْعُسْرَىٰ ع س ر B003; 92:11 تَرَدَّىٰٓ ر د ي B004; 92:16 وَتَوَلَّىٰ و ل ي B005; 92:18 يُؤْتِى ء ت ي B002; 92:19 نِّعْمَةٍۢ ن ع م B001; 92:19 تُجْزَىٰٓ ج ز ي B001; 92:19 تُجْزَىٰٓ ج ز ي B003

## Buluşmalar

Görüntülerin en sık birleştiği yer, uçurum ile elin aynı sahnede durmasıdır. Cennet ehlinden biri dünyadaki arkadaşını anlatır. Arkadaşı ona alay ederek şöyle sormuştur: {ar:يَقُولُ أَءِنَّكَ لَمِنَ ٱلْمُصَدِّقِينَ, tr:yekûlü einneke le-mine'l-musaddikîn, gloss:sen de mi doğrulayanlardansın derdi, source:37:52}. Sonra adam aşağı bakar ve arkadaşını ateşin ortasında görür: {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettalea fe-raâhu fî sevâi'l-cahîm, gloss:eğilip baktı ve onu cehennemin ortasında gördü, source:37:55}. Ona şöyle der: {ar:تَٱللَّهِ إِن كِدتَّ لَتُرْدِينِ, tr:ta'llâhi in kidte le-türdîn, gloss:Allah'a andolsun beni de neredeyse yuvarlayacaktın, source:37:56}. Ardından ekler: {ar:وَلَوْلَا نِعْمَةُ رَبِّى لَكُنتُ مِنَ ٱلْمُحْضَرِينَ, tr:ve levlâ ni'metü rabbî le-küntü mine'l-muhdarîn, gloss:Rabbimin nimeti olmasaydı ben de oraya getirilenlerden olurdum, source:37:57}. Bu sahnede doğrulama, yuvarlanma, yüksekten bakış ve bir nimet bir aradadır. Surenin on dokuzuncu ayeti verenin yanında kimsenin bir nimeti olmadığını söyler. Cennet ehli ise kurtuluşunu tek bir nimete, Rabbinin nimetine bağlar. İnsanlar arasında karşılığı ödenecek bir el yoktur, ama Rabbin eli her şeyi taşır. Bir başka ayet aynı birleşmeyi müminlere hatırlatma olarak kurar: Allah'ın nimetiyle kardeş olmuşlardır ve {ar:وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍۢ مِّنَ ٱلنَّارِ فَأَنقَذَكُم مِّنْهَا, tr:ve küntüm alâ şefâ hufratin mine'n-nâri fe-enkazeküm minhâ, gloss:ateşten bir çukurun kenarındaydınız; sizi oradan kurtardı, source:3:103}. Ayet {ar:لَعَلَّكُمْ تَهْتَدُونَ, tr:leallekum tehtedûn, gloss:doğru yolu bulasınız diye, source:3:103} diye kapanır. Kuyunun kenarı, nimet ve yol gösterme tek ayettedir. Kenara çekilen, uyarı ateşini işaret ateşi olarak okuyandır.

İkinci büyük buluşma bir sarayda geçer. Musa ile Harun'a Firavun'a ne diyecekleri öğretilir: {ar:وَٱلسَّلَٰمُ عَلَىٰ مَنِ ٱتَّبَعَ ٱلْهُدَىٰٓ, tr:ve's-selâmü alâ meni't-tebea'l-hüdâ, gloss:esenlik yol göstericiye uyanadır, source:20:47}. Ardından {ar:أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ, tr:enne'l-azâbe alâ men kezzebe ve tevellâ, gloss:azap yalanlayıp yüz çevirenedir, source:20:48} gelir. Firavun {ar:قَالَ فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:kâle fe-men rabbükümâ yâ mûsâ, gloss:ey Musa, sizin Rabbiniz kim dedi, source:20:49} diye sorar. Musa şöyle cevap verir: {ar:قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:kâle rabbüne'llezî a'tâ külle şey'in halkahû sümme hedâ, gloss:Rabbimiz her şeye yaratılışını verip sonra yol gösterendir dedi, source:20:50}. Bu cevapta surenin üç fiili aynı cümlededir: üçüncü ayetin yaratması, beşinci ayetin vermesi ve on ikinci ayetin yol göstermesi. Bir ayet önce de on altıncı ayetin iki fiili geçmiştir. Aynı Firavun başka bir surede yüceliği kendine mal eder: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe-kâle ene rabbükümü'l-a'lâ, gloss:ben sizin en yüce rabbinizim dedi, source:79:24}. Ardından {ar:فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ, tr:fe-ehazehu'llâhu nekâle'l-âhirati ve'l-ûlâ, gloss:Allah onu sonranın ve öncenin cezasıyla yakaladı, source:79:25} gelir. Elin, yolun, yüz çevirmenin, yüceliğin ve mülkün görüntüleri burada tek bir karşılaşmada birleşir. Veren Rab ile tutan kral karşı karşıya gelir. Yüceliği iddia eden kral, surenin "son da ilk de bizimdir" sözüyle düşürülür.

Yüz ile elin buluşması iyiliğin tanımında görülür. İyilik yüzü doğuya ya da batıya çevirmek değildir: {ar:لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ, tr:leyse'l-birra en tüvellû vucûheküm kıbele'l-meşriki ve'l-mağrib, gloss:iyilik yüzlerinizi doğu ve batı yönüne çevirmeniz değildir, source:2:177}. Aynı ayet iyiliği şöyle sayar: {ar:وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ, tr:ve âte'l-mâle alâ hubbih, gloss:malı sevmesine rağmen verdi, source:2:177}. Malın gittiği yerler arasında {ar:وَفِى ٱلرِّقَابِ, tr:ve fi'r-rikâb, gloss:boyunları çözmek için, source:2:177} de vardır. Ayet şöyle biter: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ, tr:ülâike'llezîne sadakû ve ülâike hümü'l-müttekûn, gloss:işte doğru olanlar onlardır ve sakınanlar da onlardır, source:2:177}. Yüzü çevirmek, malı vermek, boyun çözmek, hücumu sonuna kadar götüren doğruluk ve siper olan sakınma tek ayette bir araya gelir. Yüz çevirmek iyiliğin kendisi değildir, iyilik eldedir. Ama surenin yirminci ayeti eli tekrar yüze bağlar: veren el, aranan yüz için uzanır. Aynı bağ yoksulları doyuranların sözünde görülür: {ar:إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءًۭ وَلَا شُكُورًا, tr:innemâ nut'imüküm li-vechi'llâhi lâ nürîdü minküm cezâen ve lâ şükûrâ, gloss:sizi yalnızca Allah'ın yüzü için doyuruyoruz; sizden ne karşılık ne teşekkür istiyoruz, source:76:9}. Sözün sonunda {ar:إِنَّا نَخَافُ مِن رَّبِّنَا يَوْمًا عَبُوسًۭا قَمْطَرِيرًۭا, tr:innâ nehâfü min rabbinâ yevmen abûsen kamtarîrâ, gloss:biz Rabbimizden asık suratlı, çetin bir günden korkarız, source:76:10} derler. Sonra {ar:فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ, tr:fe-vekâhumu'llâhu şerra zâlike'l-yevm, gloss:Allah onları o günün kötülüğünden korudu, source:76:11} gelir. El, yüz, karşılığın reddi ve siper bu ayetlerde surenin sırasıyla dizilir. Bunun tam tersi de bir sahne olarak anlatılır. Bir adam Allah'a söz vermiştir: {ar:لَئِنْ ءَاتَىٰنَا مِن فَضْلِهِۦ لَنَصَّدَّقَنَّ, tr:lein âtânâ min fadlihî le-nessaddakanne, gloss:bize lütfundan verirse mutlaka sadaka vereceğiz, source:9:75}. Sonra şu olur: {ar:فَلَمَّآ ءَاتَىٰهُم مِّن فَضْلِهِۦ بَخِلُوا۟ بِهِۦ وَتَوَلَّوا۟ وَّهُم مُّعْرِضُونَ, tr:fe-lemmâ âtâhüm min fadlihî bahılû bihî ve tevellev ve hüm mu'ridûn, gloss:lütfundan verince cimrilik ettiler ve yüz çevirdiler; zaten dönüp gidiyorlardı, source:9:76}. Sıkan el ile dönülen sırt aynı kişidedir. Sekizinci ve on altıncı ayetler tek bir hikâyede birleşir.

Büyüme ile yükseklik, yüksekteki bahçede buluşur. Allah'ın hoşnutluğunu arayarak harcayanların durumu {ar:كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ, tr:ke-meseli cennetin bi-rabvetin esâbehâ vâbilün fe-âtet ükulehâ dı'feyn, gloss:yüksekçe bir yerdeki bahçe gibidir; ona sağanak isabet eder ve ürününü iki kat verir, source:2:265} diye anlatılır. Bu bahçe kuyunun tam karşıtıdır. Aşağıda değil yüksektedir. Yağmur onu süpürmez, büyütür. Verme fiili de bahçenin kendi fiilidir. Aynı yükseklik ateşe dönük bir eğiklikle karşılaşır: Bir yanda takva ve hoşnutluk üzerine kurulmuş yapı, öbür yanda {ar:عَلَىٰ شَفَا جُرُفٍ هَارٍۢ فَٱنْهَارَ بِهِۦ فِى نَارِ جَهَنَّمَ, tr:alâ şefâ cürufin hârin fenhâra bihî fî nâri cehennem, gloss:çökmek üzere olan bir yarın kenarına kurulmuş, onunla birlikte cehennem ateşine yıkılmış yapı, source:9:109} vardır. Biri takva ve hoşnutluk üzerine kurulur, öteki çöküp ateşe düşer. Cimrinin malı da düştüğü yerde onun yanına yapışır: {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhühüm ve cünûbühüm ve zuhûruhüm, gloss:o gün onlar cehennem ateşinde kızdırılır ve alınları, yanları ve sırtları onlarla dağlanır, source:9:35}. Sakınanın yanında bir kalkan durur ve o yanından kötülükten uzak tutulur. Biriktirenin yanı ise biriktirdiğiyle dağlanır. Sırtı da yüz çevirdiği için dönmüş olan sırttır.

Musa'nın ateşi ise işaret ateşi ile yakan ateşi bir arada tutar. Musa ailesine {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidü ale'n-nâri hüdâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10} der. Başka bir anlatımda {ar:لَّعَلَّكُمْ تَصْطَلُونَ, tr:leallekum tastalûn, gloss:belki ısınırsınız, source:27:7} der. Isınmak on beşinci ayetin yanmasıyla aynı köktendir. Yanına yaklaşılan ateş ısıtır ve yol gösterir. İçine girilen ateş ise yakar. Surenin hareketi bu iki mesafe arasında kurulur. İlk iki ayette gece serilir ve gün yarılır. Gece insanların koşusunu örter, gün o koşunun dağıldığını gösterir. Yol ayrılır ve her yol yürüyenine göre düzlenir. Biri verir, siper kurar ve vaadi kendi eliyle doğrular. Öteki malını tutar, ona cübbe gibi bürünür ve vaadi yalanlayıp sırtını döner. Sonra gece yolunda bir ateş yakılır ve bir ses "uyardım" der. Uyarıyı işaret olarak okuyan, dizgini tutulan bir binek gibi kenara çekilir. Yüzü kendisine bir nimet borcu olanlara değil, yüceliğe dönüktür. Uyarıyı duymayan, yuvarlandığı anda elindeki malın ona yetmediğini görür ve ateşin içine girer. Surenin son kelimesi, kayıp devesini arayan adamın onu bulduğu anın kelimesidir: hoşnutluk. Bu hoşnutluk, ilk ayetteki gecenin örtüsünden sonra gelen yüzün açılmasıdır.

