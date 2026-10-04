Focus: 87:9. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/87_9/D.r13/context.md =====
# 87:9 — focus

فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ

Anchor translation (canonical reading, reference only):

Öyleyse öğüt yarar sağlarsa öğüt ver.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَذَكِّرْ | ذُكِّرَ | ذ ك ر | REM;V |
| 2 | إِن | إِن |  | COND |
| 3 | نَّفَعَتِ | نَفَعَ | ن ف ع | V |
| 4 | ٱلذِّكْرَىٰ | ذِكْرَىٰ | ذ ك ر | DET;N |


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
- 87:9 ◀ focus فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ
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


===== _commentary/v16/work/87_9/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ذ ك ر (root_000516) — identity root of فَذَكِّرْ (w1)

- **B001** erkek cinsiyet ve erkek yavru doğurma — erkek · erkek üreme organı · erkeğin üreme organı çevresindeki organlar · erkekler veya erkeklik · erkek yavru doğurdu · çoğunlukla erkek yavru doğuran dişi · erkek yapılı kadın veya dişi deve · gebe için kolay doğum ve erkek çocuk dileği
  الذكر خلاف الأنثى (sihah;tahdhib;mufradat)؛ الذكورة والذكور والذكران جمع الذكر (ayn;tahdhib;mufradat)؛ أذكرت ولدت ذكرا والمذكار تلد الذكور (maqayis;ayn;sihah;tahdhib;mufradat)
- **B002** sert, keskin ve güçlü olma — demirin en sert ve kuru türü · keskin ve sağlam kılıç · kılıcın veya erkeğin keskinliği · kalın ve sert otlar · güçlü, yiğit ve onurlu adam · çetin ve korkutucu gün, yol veya felaket · şiddetli yağmur, sağlam söz veya güçlü şiir · tehlikeli, yalnız erkeklerin geçtiği veya sert ot bitiren ıssız ova
  سيف مذكر ذو ماء وذو ذكر صارم (maqayis;sihah;mufradat)؛ الذكر من الحديد أيبسه وأشده (ayn;sihah;tahdhib)؛ ذكور البقل ما غلظ منه (maqayis;sihah;tahdhib;mufradat)؛ رجل ذكر قوي شجاع ويوم وطريق وداهية ومطر ذكر للشدة (tahdhib)
- **B003** akılda tutma ve yeniden hatırlama — hatırladı veya aklında tuttu · aklında · hatırlama · ezberlemek için çalışma · belleği güçlü, yiğit veya iyi anılan adam
  ذكرت الشيء خلاف نسيته (maqayis;sihah)؛ الذكر الحفظ للشيء وهو مني على ذكر (ayn;tahdhib)؛ ذكر بالقلب والتذكر طلب ما فات (ayn;tahdhib;mufradat)
- **B004** bir şeyi sözle anma [kalıp] — sözle anma · insanların arkasından kusurlarını söyleme
  ثم حمل عليه الذكر باللسان (maqayis)؛ الذكر جري الشيء على لسانك (ayn;tahdhib)؛ ذكرته بلساني وبقلبي (sihah)؛ كل قول يقال له ذكر وذكر باللسان (mufradat)؛ يذكر الناس أي يغتابهم ويذكر عيوبهم (tahdhib)
- **B005** Tanrı'yı kulluk amacıyla anma — kulluk amacıyla anma, yakarış, övgü, şükretme ve itaat · Tanrı'yı kulluk, övgü ve yakarışla anma
  الذكر الصلاة والدعاء والثناء (ayn;tahdhib)؛ الذكر قراءة القرآن والتسبيح والدعاء والشكر والطاعة (tahdhib)؛ ولذكر الله أكبر واذكروا الله (mufradat)
- **B006** indirildiğine inanılan kutsal kitap — dinin ayrıntılarını bildiren kutsal kitap
  الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر (ayn;tahdhib)؛ القرآن والكتب المتقدمة والزبور من بعد الذكر (mufradat)
- **B007** onur, iyi ün ve saygınlık — onur, iyi ün ve övgü · belleği güçlü, yiğit veya iyi anılan adam
  الذكر العلاء والشرف (maqayis)؛ الذكر الشرف والصوت (ayn;tahdhib)؛ الذكر الصيت والثناء وذي الذكر أي ذي الشرف (sihah)؛ وإنه لذكر لك ولقومك أي شرف (mufradat)
- **B008** hakkı gösteren yazılı belge [kalıp] — hakkı gösteren yazılı belge · yazılı hak belgeleri
  ذكر الحق الصك وجمعه ذكور حقوق (ayn;tahdhib)؛ يقال ذكور حق (ayn;tahdhib)
- **B009** hatırlatma, hatırlamayı sağlayan araç ve sıkça anma — hatırlatma, öğüt alma veya sıkça anma · hatırlatıcı · hatırlatma · ona o şeyi hatırlattı
  الذكرى اسم للتذكير والتذكير مجاوز (ayn)؛ التذكرة ما تستذكر به الحاجة (sihah)؛ الذكرى بمعنى الذكر وبمعنى التذكير (tahdhib)؛ التذكرة ما يتذكر به الشيء والذكرى كثرة الذكر (mufradat)

## ن ف ع (root_001536) — identity root of نَّفَعَتِ (w3)

- **B001** zararın karşıtı olan ve iyiliğe ulaştıran yarar — zararın karşıtı olan, iyiliğe ulaşmaya yardım eden yarar · ona yarar sağladı · ondan yararlandı · yarar · yarar · yararlı · insanlara sürekli yarar sağlayan ve zarar vermeyen kişi
  النون والفاء والعين كلمة تدل على خلاف الضر (maqayis)؛ النفع ضد الضر (ayn;sihah;tahdhib)؛ نفعه نفعا وانتفعت بكذا (ayn)؛ نفعه ينفعه نفعا ومنفعة وانتفع بكذا (maqayis)؛ ما يستعان به في الوصول إلى الخيرات (mufradat)؛ ما عندهم نفيعة أي منفعة (tahdhib)؛ رجل نفاع إذا كان ينفع الناس ولا يضرهم (tahdhib)
- **B002** deri su kabının iki yanındaki yarılmış deri parçalardan biri — deri yarılarak su kabının iki yanına yerleştirilen parçalardan biri
  النُّفعة في جانبي المزادة يشق الأديم فيجعل في كل جانب نفعة (ayn)؛ النفع في المزادة في جانبيها يشق الأديم فيجعل في جانبيها في كل جانب نفعة (tahdhib)
- **B003** değnek — değnek · değnek alıp satmak
  النَّفعة العصا وهي فعلة من النفع؛ أنفع الرجل إذا اتجر في النفعات وهي العصي

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 87:9, and ## Buluşmalar) =====
## Sel: köpük gider, su kalır

Beşinci ayetteki غثاء yalnızca kurumuş ot değildir, selin yüzünde yüzen şeydir de. Arapça onu iki ayrı kaba birden koyar: {ar:الغثاء غثاء السيل والقدر، ما يطفح ويتفرق من النبات اليابس وزبد القدر, tr:el-ğuŝâu ğuŝâu's-seyli ve'l-kıdr mâ yatfahu ve yetefarraku mine'n-nebâti'l-yâbisi ve zebedi'l-kıdr, gloss:ğuŝâ selin de tencerenin de ğuŝâsıdır; kuru bitkiden ve tencere köpüğünden yüzeye taşıp dağılandır, source:"غ ث و,B001"}. Kelime bir atasözü değeri de taşır: {ar:يضرب به المثل فيما يضيع ويذهب غير معتد به, tr:yudrabu bihi'l-meŝelu fî mâ yadîu ve yeẕhebu ğayra mu'teddin bih, gloss:kaybolup giden ve hesaba katılmayan şey için örnek olarak anılır, source:"غ ث و,B004"}. Selin öbür yüzü sudur. Surenin kelimelerinin aileleri suyun nerede toplanıp kaldığını gösterir.

İkinci ayetteki "yarattı" fiilinin ailesinde kayalardaki oyuklar vardır: {ar:الخليقة نقر في صخرة يجتمع فيه ماء السماء, tr:el-halîka nakrun fî sahratin yectemiu fîhi mâu's-semâ, gloss:halîka kayada gök suyunun toplandığı oyuktur, source:"خ ل ق,B011"}. Bu oyuklar şöyle de anlatılır: {ar:قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها تسميها العرب الخلائق, tr:kılâten tumsiku mâe's-sehâbi fî safâtin halakahallâhu fîhâ tusemmîhe'l-arabu'l-halâik, gloss:Allah'ın düz kayada yarattığı ve bulut suyunu tutan çukurlar; Araplar onlara halâik der, source:"خ ل ق,B011"}. Beşinci ayetteki أحوى'nın ailesinde selin doldurduğu kıvrımlı çukurlar vardır: {ar:الحوايا التي تكون في القيعان والرياض حفائر ملتوية يملؤها ماء السيل, tr:el-havâyâ elletî tekûnu fi'l-kîâni ve'r-riyâdi hafâiru multeviyetun yemleuhâ mâu's-seyl, gloss:havâyâ düzlüklerde ve çayırlarda selin doldurduğu kıvrımlı çukurlardır, source:"ح و ي,B008"}. "Rab" kelimesinin ailesinde bol su, toplandığı için bu adı alır: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabeb ve huve'l-mâu'l-keŝîr sumiye bi-ẕâlike li-ictimâih, gloss:rabeb boldur ve toplandığı için bu adı almıştır, source:"ر ب ب,B013"}. Yedinci ayetteki "açık" kelimesinin ailesinde kuyu temizlenir: {ar:جهرت الركية إذا كان ماؤها قد غطى الطين فنقى ذلك حتى يظهر الماء ويصفو, tr:cehertu'r-rakiyye iẕâ kâne mâuhâ kad ğattâhu't-tînu fe-nakkâ ẕâlike hattâ yezhera'l-mâu ve yesfû, gloss:suyunu çamur örtmüş kuyuyu su görünüp duruluncaya kadar temizledim, source:"ج ه ر,B008"}. Aynı ayetteki "bilir" fiilinin ailesinde de suyu bol kuyu vardır: {ar:العيلم البئر الكثيرة الماء, tr:el-aylem el-bi'ru'l-keŝîratu'l-mâ, gloss:aylem suyu bol kuyudur, source:"ع ل م,B005"}.

Dokuzuncu ayet öğütten "fayda verirse" diye söz eder, on yedinci ayet ahireti "daha kalıcı" diye niteler. Fayda, {ar:ما يستعان به في الوصول إلى الخيرات, tr:mâ yusteânu bihî fi'l-vusûli ile'l-hayrât, gloss:iyiliklere ulaşmak için yardım alınan şey, source:"ن ف ع,B001"} diye tanımlanır. Bu tanım on yedinci ayetteki "hayırlı" kelimesinin kökünü de taşır. Kalıcılık ise şudur: {ar:البقاء ثبات الشيء على حاله الأولى وهو يضاد الفناء, tr:el-bekâu ŝebâtu'ş-şey'i alâ hâlihi'l-ûlâ ve huve yudâddu'l-fenâ, gloss:bekâ bir şeyin ilk halinde sabit durmasıdır ve yok olmanın zıddıdır, source:"ب ق ي,B001"}. Bu tanımda on sekizinci ayetteki "ilk" kelimesi de vardır.

Kur'an'da bu iki yüzü bir sahnede toplayan benzetmeyi Allah verir. Gökten su iner, vadiler {ar:فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا, tr:fe-sâlet evdiyetun bi-kaderihâ, gloss:vadiler kendi ölçülerince akar, source:13:17}. Burada üçüncü ayetteki "ölçtü" fiilinin kökü geçer. Sel kabarık bir köpük taşır. İnsanların süs ya da eşya için ateşte erittikleri madenin de benzer bir köpüğü vardır. Sonra ayırım gelir: {ar:فَأَمَّا ٱلزَّبَدُ فَيَذْهَبُ جُفَآءًۭ ۖ وَأَمَّا مَا يَنفَعُ ٱلنَّاسَ فَيَمْكُثُ فِى ٱلْأَرْضِ, tr:fe-emme'z-zebedu fe-yeẕhebu cufâen ve emmâ mâ yenfau'n-nâse fe-yemkuŝu fi'l-ard, gloss:köpük atılıp gider; insanlara fayda veren ise yerde kalır, source:13:17}. Kelime farklıdır, orada غثاء değil زبد geçer. Ama sahne aynıdır. Surenin beşinci, dokuzuncu ve on yedinci ayetlere dağıttığı döküntü, fayda ve kalıcılık bu ayette tek bir selin içinde bir aradadır. Bu yan yana koyuş surenin kendi sözü değildir, ama bu ayet ona Kur'an'dan bir dayanak verir. Fayda verirse sunulan öğüt, kayadaki oyukta tutulan suya benzer. Çerçöp ise akıntıyla gidip hesaba katılmayan şeydir.

Kaynaklar: 87:5 غُثَآءً غ ث و B001; 87:5 غُثَآءً غ ث و B004; 87:9 نَّفَعَتِ ن ف ع B001; 87:17 أَبْقَىٰٓ ب ق ي B001; 87:2 خَلَقَ خ ل ق B011; 87:5 أَحْوَىٰ ح و ي B008; 87:1 رَبِّ ر ب ب B013; 87:7 ٱلْجَهْرَ ج ه ر B008; 87:7 يَعْلَمُ ع ل م B005

## Ölçüp biçmek: ok, tulum ve kura

İkinci ve üçüncü ayet dört fiili sıralar: {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:elleẕî halaka fe-sevvâ, gloss:yaratıp düzene koyan, source:87:2}, {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:velleẕî kaddera fe-hedâ, gloss:ölçüp yol gösteren, source:87:3}. Arapçada bu fiiller bir zanaatkârın işinin adımlarıdır. خلق, kökünde ölçüp biçmektir: {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhû et-takdîru'l-mustakîm, gloss:halkın aslı doğru ölçüdür, source:"خ ل ق,B001"}. Bu tanım ikinci ayetin fiilini üçüncü ayetin fiiline bağlar. Ölçülüp yontulmuş ok da bu köktendir: {ar:سهم مخلق أملس مستو, tr:sehmun muhallakun emlesu mustevin, gloss:yontulmuş düzgün ve doğru ok, source:"خ ل ق,B008"}. Bu tanımda ikinci ayetin öbür fiili olan سوّى'nin kökü de vardır. سوّى eğri olanı doğrultmaktır: {ar:استوى من اعوجاج, tr:istevâ min i'vicâc, gloss:eğrilikten doğruldu, source:"س و ي,B002"}. قدّر, bir şeyi nasıl düzleyip hazır edeceğini düşünmektir: {ar:التروية والتفكير في تسوية أمر وتهيئته, tr:et-terviyetu ve't-tefkîru fî tesviyeti emrin ve teh'iyetih, gloss:bir işi nasıl düzleyip hazırlayacağını uzun uzun düşünmek, source:"ق د ر,B005"}. Aynı kök bir şeyin vardığı ölçüyü de bildirir: {ar:مبلغ الشيء وكنهه ونهايته, tr:mebleğu'ş-şey'i ve kunhuhû ve nihâyetuh, gloss:bir şeyin vardığı yer ve özü ve sonu, source:"ق د ر,B001"}. Sonra هدى gelir. Bu kelime okun önde giden ucudur: {ar:هادي السهم نصله, tr:hâdi's-sehmi naslu, gloss:okun hâdîsi temrenidir, source:"ه د ي,B003"}. Değnek de taşıyanın önünden gittiği için bu adı alır: {ar:العصا هاديا لأنها تتقدمه, tr:el-asâ hâdiyen li-ennehâ tetekaddemuh, gloss:değnek önünden gittiği için hâdî adını alır, source:"ه د ي,B003"}. Rab ise bir şeyi düzeltip adım adım tamamlayandır: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye bir şeyi halden hale geçirerek tamamlanma sınırına kadar oluşturmaktır, source:"ر ب ب,B002"}.

Değneği doğrultmanın bir yolu da ateştir. Bu işin fiili, on ikinci ayetteki "ateşe girer" fiilinin kendisidir: {ar:صلى عصاه إذا أدارها على النار يثقفها, tr:salâ asâhu iẕâ edârahâ ale'n-nâri yuŝakkıfuhâ, gloss:değneğini ateşin üstünde çevirip doğrulttu, source:"ص ل ي,B004"}. Ölçmek, doğrultmak ve uç takmak, ikinci ve üçüncü ayetin düz anlamının yanında bir yapım sahnesi kurar. Yapılan şey yalnızca var edilmez, bir yöne de çevrilir. "Yol gösterdi" fiili okun ucunun bir hedefe dönmesi gibi duyulur.

Aynı ölçüp biçme bir deri üzerinde de yapılır. خلق'in ilk örneği, su tulumu için deriyi kesmeden önce ölçmektir: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme iẕâ kaddertuhû kable'l-kat', gloss:deriyi kesmeden önce ölçtüğümde halaktu derim, source:"خ ل ق,B001"}. İkinci ayetin fiili ile üçüncü ayetin fiili burada tek bir hareketin iki adı olur. Bitmiş kabın yapısını dokuzuncu ayetteki نفع kökü anlatır: {ar:النفع في المزادة في جانبيها يشق الأديم فيجعل في جانبيها في كل جانب نفعة, tr:en-nif'u fi'l-mezâdeti fî cânibeyhâ yuşakku'l-edîmu fe-yuc'alu fî cânibeyhâ fî kulli cânibin nif'a, gloss:su kırbasının iki yanına deri yarılıp her yana nif'a denen bir parça konur, source:"ن ف ع,B002"}. Bu yanlar on birinci ayetteki kelimenin köküyle anılır: {ar:الجنبتان ناحيتا كل شيء, tr:el-canbetân nâhiyetâ kulli şey', gloss:her şeyin iki yanı, source:"ج ن ب,B001"}. Deri yağla terbiye edilir. Bu da "Rab" kelimesinin ailesindendir: {ar:رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب, tr:rabebtu'l-edîme bi's-semni ve'd-devâe bi'l-asel ve sikâun merbûb, gloss:deriyi yağla ilacı balla terbiye ettim; terbiye edilmiş tulum, source:"ر ب ب,B006"}. Tulum çalkalanır: {ar:جهرت السقاء مخضته, tr:cehertu's-sikâe mehadtuhû, gloss:tulumu çalkaladım, source:"ج ه ر,B010"}. Kullanıldıkça da aşınıp düzleşir: {ar:أخلق الشيء وخلق إذا بلي؛ إذا أخلق املاس وذهب زئبره, tr:ahleka'ş-şey'u ve haleka iẕâ beliye iẕâ ahleka imlâsse ve ẕehebe zi'biruh, gloss:bir şey eskiyince ahleka denir; eskiyince düzleşir ve tüyü gider, source:"خ ل ق,B009"}. Beş kök tek bir nesnede, ölçülen, yanları eklenen, terbiye edilen ve eskiyen bir tulumda buluşur. Kur'an bu nesneyi bir sahnede kullanmaz. Ama aynı kelime ailesi yaratılışı bir zanaat olarak duyurur, ve bu zanaatta ölçü kesmeden önce gelir.

Üçüncü bir nesne, kura okudur. "Rab" kelimesinin ailesinde okların saklandığı torba vardır: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-ribâbe şebîhetun bi'l-kinâneti tucmeu fîhâ sihâmu'l-meysir, gloss:ribâbe meysir oklarının toplandığı sadağa benzer torbadır, source:"ر ب ب,B010"}. Bu tanım sekizinci ayetteki "kolaylaştırırız" fiilinin kökünü, meysiri, de içerir. Meysir bir oyundur ve adı paylaştırmadan gelir: {ar:يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها, tr:yasera'l-kavmu'l-cezûra ey ictezerûhâ ve'ktesemû a'dâehâ, gloss:topluluk deveyi kesip parçalarını paylaştı, source:"ي س ر,B007"}. Okların en büyük payı alanı birinci ayetteki "en yüce" kelimesinin kökündendir: {ar:المعلى السابع من القداح, tr:el-muallâ es-sâbiu mine'l-kıdâh, gloss:muallâ okların yedincisidir, source:"ع ل و,B009"}. Okun gövdesi yontulup yumuşatılır: {ar:المخلق القدح إذا لين, tr:el-muhallak el-kıdhu iẕâ luyyine, gloss:muhallak yumuşatılmış ok gövdesidir, source:"خ ل ق,B008"}. Pay da aynı köktendir: {ar:الخلاق النصيب لأنه قد قدر لكل أحد نصيبه, tr:el-halâk en-nasîb li-ennehû kad kuddira li-kulli ehadin nasîbuh, gloss:halâk paydır çünkü herkesin payı ölçülmüştür, source:"خ ل ق,B006"}. Her şeyin bir ölçüsü ve bir vadesi vardır: {ar:لكل شيء مقدار وأجل, tr:li-kulli şey'in mikdârun ve ecel, gloss:her şeyin bir miktarı ve süresi vardır, source:"ق د ر,B001"}. İkinci ve üçüncü ayetteki ölçüp biçme bu sahnede paylaştırmaya döner. On altıncı ve on yedinci ayetteki seçim de bir pay seçimidir.

Kur'an bu ölçmeyi yaratılışın kendisine uygular. Allah inkâr eden insan için {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe-kaddera, gloss:onu bir damladan yarattı ve ölçüsünü koydu, source:80:19} der, sonra {ar:ثُمَّ ٱلسَّبِيلَ يَسَّرَهُۥ, tr:ŝumme's-sebîle yesserah, gloss:sonra yolu ona kolaylaştırdı, source:80:20} diye ekler. Bu iki ayet surenin ikinci, üçüncü ve sekizinci ayetlerinin fiillerini aynı sırayla verir. Başka bir yerde Allah {ar:وَخَلَقَ كُلَّ شَىْءٍۢ فَقَدَّرَهُۥ تَقْدِيرًۭا, tr:ve halaka kulle şey'in fe-kaddarahû takdîrâ, gloss:her şeyi yarattı ve ona tam ölçüsünü verdi, source:25:2} ve {ar:إِنَّا كُلَّ شَىْءٍ خَلَقْنَٰهُ بِقَدَرٍۢ, tr:innâ kulle şey'in halaknâhu bi-kader, gloss:biz her şeyi bir ölçüyle yarattık, source:54:49} der. Surenin son ayetinde adı geçen İbrahim, putları reddedip kavmine Âlemlerin Rabbini anlatırken bu ikiliyi kendi ağzından söyler: {ar:ٱلَّذِى خَلَقَنِى فَهُوَ يَهْدِينِ, tr:elleẕî halakanî fe-huve yehdîn, gloss:beni yaratan ve bana yol gösteren O'dur, source:26:78}. Pay kelimesi Kur'an'da tam bu surenin vardığı karşıtlıkla geçer. Hac ibadetleri anlatılırken yalnız bu dünyada verilmesini isteyen kişi için {ar:وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ, tr:ve mâ lehû fi'l-âhireti min halâk, gloss:onun ahirette hiçbir payı yoktur, source:2:200} denir. Önceki kavimler için {ar:فَٱسْتَمْتَعُوا۟ بِخَلَٰقِهِمْ, tr:fe'stemteû bi-halâkıhim, gloss:paylarından yararlandılar, source:9:69} denir, ayetin sonunda da yaptıkları dünyada ve ahirette boşa gider. Kura okları ve meysir müminlere yasaklanırken kullanılan kelimeler ise surenin iki kelimesini yan yana getirir: {ar:فَٱجْتَنِبُوهُ لَعَلَّكُمْ تُفْلِحُونَ, tr:fectenibûhu leallekum tuflihûn, gloss:ondan uzak durun ki kurtuluşa eresiniz, source:5:90}. On birinci ayetteki "uzak durmak" ve on dördüncü ayetteki "kurtuluşa ermek" burada aynı cümlededir. Başka bir yerde meysir için {ar:وَإِثْمُهُمَآ أَكْبَرُ مِن نَّفْعِهِمَا, tr:ve ismuhumâ ekberu min nef'ihimâ, gloss:günahları faydalarından büyüktür, source:2:219} denir. Oklarla kısmet aramak da sayılan yasaklar arasındadır: {ar:وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ, tr:ve en testaksimû bi'l-ezlâm, gloss:fal oklarıyla pay aramanız, source:5:3}. Kura okuyla alınan pay yasaklanır. Ölçüyü koyanın verdiği pay ise ahirette de geçerlidir.

Kaynaklar: 87:2 خَلَقَ خ ل ق B001; 87:2 خَلَقَ خ ل ق B008; 87:2 خَلَقَ خ ل ق B009; 87:2 خَلَقَ خ ل ق B006; 87:2 فَسَوَّىٰ س و ي B002; 87:3 قَدَّرَ ق د ر B005; 87:3 قَدَّرَ ق د ر B001; 87:3 فَهَدَىٰ ه د ي B003; 87:1 رَبِّ ر ب ب B002; 87:1 رَبِّ ر ب ب B006; 87:1 رَبِّ ر ب ب B010; 87:12 يَصْلَى ص ل ي B004; 87:9 نَّفَعَتِ ن ف ع B002; 87:11 يَتَجَنَّبُهَا ج ن ب B001; 87:7 ٱلْجَهْرَ ج ه ر B010; 87:1 ٱلْأَعْلَى ع ل و B009; 87:8 لِلْيُسْرَىٰ ي س ر B007

## Toplanan, tutulan, düşürülen: okuma, unutma ve sayfalar

Altıncı ayet {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız da unutmayacaksın, source:87:6} der. Yedinci ayet buna bir istisna ekler: {ar:إِلَّا مَا شَآءَ ٱللَّهُ, tr:illâ mâ şâallâh, gloss:Allah'ın dilediği hariç, source:87:7}. Kelimelerin aileleri hafızayı bir kaplar dizisi olarak gösterir. قرأ toplamaktır: {ar:قرأت الشيء قرآنا جمعته وضممت بعضه إلى بعض, tr:karaeu'ş-şey'e kur'ânen ceme'tuhû ve damamtu ba'dahû ilâ ba'd, gloss:bir şeyi okudum yani onu toplayıp parçalarını birbirine kattım, source:"ق ر ء,B001"}. Okuma harfleri ve kelimeleri birbirine eklemektir: {ar:القراءة ضم الحروف والكلمات بعضها إلى بعض في الترتيل, tr:el-kırâe dammu'l-hurûfi ve'l-kelimâti ba'dihâ ilâ ba'din fi't-tertîl, gloss:okuma harfleri ve kelimeleri tertil içinde birbirine eklemektir, source:"ق ر ء,B001"}. Ayetteki fiil başkasına bu toplamayı vermektir: {ar:أقرأت غيري أقرئه إقراء, tr:akra'tu ğayrî ukriuhû ikrâen, gloss:başkasına okuttum, source:"ق ر ء,B002"}. Unutmak ise emanet edilmiş bir şeyi tutamamaktır: {ar:ترك الإنسان ضبط ما استودع إما لضعف قلبه وإما عن غفلة وإما عن قصد, tr:terku'l-insâni dabta mâ'stûdia immâ li-da'fi kalbihî ve immâ an ğafletin ve immâ an kasd, gloss:insanın kendisine emanet edileni tutmayı bırakmasıdır; ya kalbinin zayıflığından ya gaflettendir ya da kasıtla, source:"ن س ي,B001"}. {ar:النسيان خلاف الذكر والحفظ, tr:en-nisyân hilâfu'ẕ-ẕikri ve'l-hıfz, gloss:unutmak anmanın ve korumanın zıddıdır, source:"ن س ي,B001"}. Unutmak bırakmak da demektir: {ar:النسيان الترك، نسوا الله فنسيهم, tr:en-nisyânu't-terk nesullâhe fe-nesiyehum, gloss:unutmak bırakmaktır; Allah'ı unuttular o da onları unuttu, source:"ن س ي,B002"}. Ve göç edenlerin geride bıraktığı döküntüdür: {ar:النسي ما سقط من منازل المرتحلين من رذال أمتعتهم, tr:en-nisy mâ sekata min menâzili'l-murtehilîne min ruẕâli emtiatihim, gloss:nisy göç edenlerin konak yerlerinden düşen değersiz eşyadır, source:"ن س ي,B003"}.

Dokuzuncu, onuncu ve on beşinci ayetlerdeki ذكر kökü bu düşüşün karşıtıdır: {ar:ذكرت الشيء خلاف نسيته, tr:ẕekertu'ş-şey'e hilâfu nesîtuh, gloss:bir şeyi andım unuttumun zıddıdır, source:"ذ ك ر,B003"}. {ar:الذكر الحفظ للشيء وهو مني على ذكر, tr:eẕ-ẕikru'l-hıfzu li'ş-şey'i ve huve minnî alâ ẕikr, gloss:zikir bir şeyi korumaktır; o benim aklımdadır, source:"ذ ك ر,B003"}. {ar:والتذكر طلب ما فات, tr:ve't-teẕekkuru talebu mâ fât, gloss:tezekkür kaçanı aramaktır, source:"ذ ك ر,B003"}. Öğüt bir şeyi akla getiren araçtır: {ar:التذكرة ما تستذكر به الحاجة, tr:et-teẕkira mâ tusteẕkeru bihi'l-hâce, gloss:teẕkira bir ihtiyacın hatırlandığı şeydir, source:"ذ ك ر,B009"}. Bir peygamberin kitabının adı da aynı köktendir: {ar:الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر, tr:eẕ-ẕikru'l-kitâbu'lleẕî fîhi tafsîlu'd-dîn ve kullu kitâbin min kutubi'l-enbiyâi ẕikr, gloss:zikir dinin ayrıntılarını içeren kitaptır ve peygamberlerin her kitabı bir zikirdir, source:"ذ ك ر,B006"}. Bu anlam dokuzuncu ayetteki öğüdü on sekizinci ve on dokuzuncu ayetlerdeki sayfalara bağlar. Sayfalar, üzerine yazı yazılan deri parçalarıdır: {ar:الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها, tr:es-suhuf vâhidetuhâ sahîfe ve hiye'l-kıtatu min edemin ebyada ev rakkın yuktebu fîhâ, gloss:suhuf sahîfenin çoğuludur; sahîfe üzerine yazılan ak deri ya da parşömen parçasıdır, source:"ص ح ف,B002"}. Mushaf bu sayfaları bir araya toplayandır: {ar:المصحف ما جعل جامعا للصحف المكتوبة, tr:el-mushaf mâ cuile câmian li's-suhufi'l-mektûbe, gloss:mushaf yazılı sayfaları toplamak için yapılmış şeydir, source:"ص ح ف,B003"}. "İlk" kelimesi bir şeyin başlangıcıdır: {ar:الأول وهو مبتدأ الشيء, tr:el-evvel ve huve mubtedeu'ş-şey', gloss:evvel bir şeyin başlangıcıdır, source:"ء و ل,B001"}. On altıncı ayetteki tercih fiilinin kökü de söz aktarmayı verir: {ar:أثرت الحديث إذا ذكرته عن غيرك وحديث مأثور, tr:eŝertu'l-hadîŝe iẕâ ẕekertehû an ğayrike ve hadîŝun me'ŝûr, gloss:bir sözü başkasından naklettiğinde eŝertu denir; aktarılan söze me'ŝûr denir, source:"ء ث ر,B002"}.

Bu aileler altıncı ayetle son ayet arasında bir yol çizer. Okutulan söz toplanır ve birbirine eklenir. Unutulmayınca tutulur. Unutulursa göç yerindeki döküntü gibi geride kalır. Anılarak geri çağrılır. Sonunda deriye yazılıp sayfa olur, sayfalar da bir arada toplanır. On sekizinci ayetteki {ar:إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:inne hâẕâ le-fi's-suhufi'l-ûlâ, gloss:bu elbette ilk sayfalarda vardır, source:87:18} cümlesi, okutulan sözün yalnız Peygamber'in hafızasında değil, İbrahim'in ve Musa'nın sayfalarında da toplanmış olduğunu söyler. Düz bir anlatımda "unutmayacaksın" bir vaattir. Aile resmi ise bu vaadin işleyişini gösterir: toplayan Allah'tır, ve toplanan şey düşürülmez.

Kur'an toplama ile okumayı aynı cümlede verir. Allah Peygamber'e vahyi acele ile tekrarlamamasını söyler: {ar:لَا تُحَرِّكْ بِهِۦ لِسَانَكَ لِتَعْجَلَ بِهِۦٓ, tr:lâ tuharrik bihî lisâneke li-ta'cele bih, gloss:onu aceleyle almak için dilini kıpırdatma, source:75:16}, {ar:إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ, tr:inne aleynâ cem'ahû ve kur'ânah, gloss:onu toplamak ve okutmak bize düşer, source:75:17}, {ar:فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ, tr:fe-iẕâ kara'nâhu fettebi' kur'ânah, gloss:onu okuduğumuzda sen okunuşunu izle, source:75:18}. Başka bir yerde de {ar:وَلَا تَعْجَلْ بِٱلْقُرْءَانِ مِن قَبْلِ أَن يُقْضَىٰٓ إِلَيْكَ وَحْيُهُۥ ۖ وَقُل رَّبِّ زِدْنِى عِلْمًۭا, tr:ve lâ ta'cel bi'l-kur'âni min kabli en yukdâ ileyke vahyuh ve kul rabbi zidnî ilmâ, gloss:sana vahyi tamamlanmadan Kur'an'ı okumakta acele etme ve Rabbim ilmimi artır de, source:20:114} denir. Hemen ardından unutmanın ilk örneği gelir: {ar:وَلَقَدْ عَهِدْنَآ إِلَىٰٓ ءَادَمَ مِن قَبْلُ فَنَسِىَ وَلَمْ نَجِدْ لَهُۥ عَزْمًۭا, tr:ve lekad ahidnâ ilâ âdeme min kablu fe-nesiye ve lem necid lehû azmâ, gloss:andolsun daha önce Adem'e söz vermiştik; o unuttu ve onda bir kararlılık bulmadık, source:20:115}. Firavun Musa'ya {ar:فَمَا بَالُ ٱلْقُرُونِ ٱلْأُولَىٰ, tr:fe-mâ bâlu'l-kurûni'l-ûlâ, gloss:ya önceki nesillerin durumu ne olacak, source:20:51} diye sorduğunda Musa şöyle cevap verir: {ar:عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى, tr:ilmuhâ inde rabbî fî kitâb lâ yadillu rabbî ve lâ yensâ, gloss:onların bilgisi Rabbimin katında bir kitaptadır; Rabbim ne yanılır ne unutur, source:20:52}. Bu cevapta "ilk" kelimesi, yazılı kitap ve unutmayan Rab bir aradadır. Unutmanın karşılığı da aynı kelimeyle verilir: {ar:كَذَٰلِكَ أَتَتْكَ ءَايَٰتُنَا فَنَسِيتَهَا ۖ وَكَذَٰلِكَ ٱلْيَوْمَ تُنسَىٰ, tr:keẕâlike etetke âyâtunâ fe-nesîtehâ ve keẕâlike'l-yevme tunsâ, gloss:ayetlerimiz sana geldi ama sen onları unuttun; bugün de sen öyle unutulursun, source:20:126}. Münafıklar için {ar:نَسُوا۟ ٱللَّهَ فَنَسِيَهُمْ, tr:nesullâhe fe-nesiyehum, gloss:Allah'ı unuttular o da onları unuttu, source:9:67} denir. Müminlere de {ar:وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ, tr:ve lâ tekûnû kelleẕîne nesullâhe fe-ensâhum enfusehum, gloss:Allah'ı unutan ve bu yüzden Allah'ın onlara kendilerini unutturduğu kimseler gibi olmayın, source:59:19} denir. Yedinci ayetteki istisnanın bir benzeri Peygamber'e verilen bir emirde de geçer: {ar:إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ وَٱذْكُر رَّبَّكَ إِذَا نَسِيتَ, tr:illâ en yeşâallâh veẕkur rabbeke iẕâ nesît, gloss:ancak Allah dilerse; unuttuğunda Rabbini an, source:18:24}. Unutmaya karşı çare anmaktır.

Sayfaların içeriği başka bir yerde kısmen verilir: {ar:أَمْ لَمْ يُنَبَّأْ بِمَا فِى صُحُفِ مُوسَىٰ, tr:em lem yunebbe' bi-mâ fî suhufi mûsâ, gloss:yoksa Musa'nın sayfalarındakiler ona haber verilmedi mi, source:53:36}, {ar:وَإِبْرَٰهِيمَ ٱلَّذِى وَفَّىٰٓ, tr:ve ibrâhîme'lleẕî veffâ, gloss:ve sözünü tam yerine getiren İbrahim'in sayfalarındakiler, source:53:37}. Sayfalarda yazanların ilki şudur: {ar:أَلَّا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ, tr:ellâ teziru vâziratun vizra uhrâ, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz, source:53:38}. Ardından {ar:وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ, tr:ve en leyse li'l-insâni illâ mâ seâ, gloss:insan için kendi çabasından başkası yoktur, source:53:39} gelir, ve dizi şöyle biter: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Her kişinin kendi payını taşıması, bu surenin iki kişiye ayrılan ortasıyla aynı konudur. Delil isteyenlere de {ar:أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:e-ve lem te'tihim beyyinetu mâ fi's-suhufi'l-ûlâ, gloss:ilk sayfalardakinin açık delili onlara gelmedi mi, source:20:133} denir. Başka bir yerde öğüt ve sayfa birlikte anılır: {ar:كَلَّآ إِنَّهَا تَذْكِرَةٌۭ, tr:kellâ innehâ teẕkira, gloss:hayır bu bir öğüttür, source:80:11}, {ar:فَمَن شَآءَ ذَكَرَهُۥ, tr:fe-men şâe ẕekerah, gloss:dileyen onu anar, source:80:12}, {ar:فِى صُحُفٍۢ مُّكَرَّمَةٍۢ, tr:fî suhufin mukerrame, gloss:değerli sayfalardadır, source:80:13}, {ar:مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ, tr:merfûatin mutahhara, gloss:yükseltilmiş ve arınmış, source:80:14}. Sayfalar yükseltilmiş ve arınmıştır. Bu iki sıfat surenin birinci ayetindeki yüksekliği ve on dördüncü ayetindeki arınmayı sayfalara taşır. Kur'an kendisi için de {ar:وَإِنَّهُۥ لَفِى زُبُرِ ٱلْأَوَّلِينَ, tr:ve innehû le-fî zuburi'l-evvelîn, gloss:o öncekilerin kitaplarında da vardır, source:26:196} der.

Kaynaklar: 87:6 سَنُقْرِئُكَ ق ر ء B001; 87:6 سَنُقْرِئُكَ ق ر ء B002; 87:6 تَنسَىٰٓ ن س ي B001; 87:6 تَنسَىٰٓ ن س ي B002; 87:6 تَنسَىٰٓ ن س ي B003; 87:9 ٱلذِّكْرَىٰ ذ ك ر B003; 87:10 يَذَّكَّرُ ذ ك ر B003; 87:9 ٱلذِّكْرَىٰ ذ ك ر B009; 87:9 ٱلذِّكْرَىٰ ذ ك ر B006; 87:18 ٱلصُّحُفِ ص ح ف B002; 87:19 صُحُفِ ص ح ف B003; 87:18 ٱلْأُولَىٰ ء و ل B001; 87:16 تُؤْثِرُونَ ء ث ر B002

## Sunulan öğüt: korkanın aldığı, bedbahtın yanından geçtiği

Dokuzuncu ve on birinci ayet arasında bir öğüt sunulur, biri onu alır, biri onun yanından geçer: {ar:فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ, tr:fe-ẕekkir in nefeati'ẕ-ẕikrâ, gloss:öğüt ver; eğer öğüt fayda verirse, source:87:9}, {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:se-yeẕẕekkeru men yahşâ, gloss:içi titreyen öğüt alacaktır, source:87:10}, {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebuhe'l-eşkâ, gloss:en bedbaht ise ondan uzak duracaktır, source:87:11}. Öğüt, başkasına yönelen bir hatırlatmadır: {ar:الذكرى اسم للتذكير والتذكير مجاوز, tr:eẕ-ẕikrâ ismun li't-teẕkîr ve't-teẕkîru mucâviz, gloss:zikrâ hatırlatmanın adıdır ve hatırlatma başkasına geçen bir iştir, source:"ذ ك ر,B009"}. Fayda zararın zıddıdır: {ar:النفع ضد الضر, tr:en-nef'u diddu'd-darr, gloss:fayda zararın zıddıdır, source:"ن ف ع,B001"}. Onuncu ayetteki korku bilgiden doğar: {ar:الخشية خوف يشوبه تعظيم وأكثر ما يكون ذلك عن علم, tr:el-haşye havfun yeşûbuhû ta'zîmun ve ekŝeru mâ yekûnu ẕâlike an ilm, gloss:haşyet içine saygı karışmış bir korkudur ve çoğunlukla bilgiden doğar, source:"خ ش ي,B001"}. Bu tanım yedinci ayetteki "bilir" fiilinin kökünü içerir. Aynı fiil "bildim" anlamında da kullanılır: {ar:خشيت بأن من تبع الهدى معناه علمت, tr:haşîtu bi-enne men tebia'l-hudâ ma'nâhu alimtu, gloss:yol göstermeyi izleyenin hakkında haşîtu bildim anlamındadır, source:"خ ش ي,B002"}. Bu ifadede üçüncü ayetteki "yol gösterdi" fiilinin kökü de geçer. On birinci ayetteki kök uzaklıktır: {ar:الأصل الآخر البعد والجنابة, tr:el-aslu'l-âhar el-bu'du ve'l-cenâbe, gloss:öbür kök anlamı uzaklıktır, source:"ج ن ب,B003"}. Bu kök bir durumu da adlandırır: {ar:الجنب الذي يجامع أهله مشتق من هذا لأنه يبعد عن الصلاة والمسجد, tr:el-cunubu'lleẕî yucâmiu ehlehû muştakkun min hâẕâ li-ennehû yeb'udu ani's-salâti ve'l-mescid, gloss:cünüp bu kökten türemiştir çünkü namazdan ve mescitten uzak kalır, source:"ج ن ب,B004"}. Bedbahtlık da mutluluğun zıddıdır: {ar:الشقوة خلاف السعادة, tr:eş-şikve hilâfu's-seâde, gloss:şikve mutluluğun zıddıdır, source:"ش ق و,B001"}.

Düz bir anlatım bu üç ayeti "bazıları kabul eder, bazıları reddeder" diye özetler. Kök aileleri iki tutumun işleyişini gösterir. Korku bilgiden gelir ve öğüdü alır. Bedbaht ise öğüde karşı çıkmaz, onu kendi yanında, uzakta tutar. Aynı kökün namazdan ve mescitten uzak kalmayı da adlandırması, bu uzak durmanın on beşinci ayetteki namazın da uzağında kalmak olduğunu duyurur. Bu son bağ dilin bir yankısıdır, ayetin kendi sözü değildir.

Kur'an bu sahneyi Peygamber'in kendi durumu üzerinden kurar. Peygamber yüzünü ekşitip döner, çünkü yanına gözleri görmeyen bir adam gelmiştir. Ona şöyle denir: {ar:وَمَا يُدْرِيكَ لَعَلَّهُۥ يَزَّكَّىٰٓ, tr:ve mâ yudrîke leallehû yezzekkâ, gloss:ne bilirsin belki o arınacak, source:80:3}, {ar:أَوْ يَذَّكَّرُ فَتَنفَعَهُ ٱلذِّكْرَىٰٓ, tr:ev yeẕẕekkeru fe-tenfeahu'ẕ-ẕikrâ, gloss:ya da öğüt alacak da öğüt ona fayda verecek, source:80:4}. Adam için {ar:وَهُوَ يَخْشَىٰ, tr:ve huve yahşâ, gloss:o içi titreyerek gelmiştir, source:80:9} denir. Peygamber'e ise {ar:فَأَنتَ عَنْهُ تَلَهَّىٰ, tr:fe-ente anhu telehhâ, gloss:sen ise onunla ilgilenmiyorsun, source:80:10} denir. Bu birkaç ayette surenin dokuzuncu, onuncu ve on dördüncü ayetlerinin kelimeleri bir arada bulunur. Öğüdün faydası da şöyle söylenir: {ar:وَذَكِّرْ فَإِنَّ ٱلذِّكْرَىٰ تَنفَعُ ٱلْمُؤْمِنِينَ, tr:ve ẕekkir fe-inne'ẕ-ẕikrâ tenfeu'l-mu'minîn, gloss:öğüt ver; çünkü öğüt müminlere fayda verir, source:51:55}. Öğütçünün sınırı da: {ar:فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ, tr:fe-ẕekkir innemâ ente muẕekkir, gloss:öğüt ver; sen yalnızca bir öğütçüsün, source:88:21}. Kime öğüt verileceği de: {ar:فَذَكِّرْ بِٱلْقُرْءَانِ مَن يَخَافُ وَعِيدِ, tr:fe-ẕekkir bi'l-kur'âni men yehâfu vaîd, gloss:tehdidimden korkana Kur'an ile öğüt ver, source:50:45}. Peygamber'e indirilen hitabın başı surenin dokuzuncu, onuncu ve on birinci ayetlerini birlikte verir: {ar:إِلَّا تَذْكِرَةًۭ لِّمَن يَخْشَىٰ, tr:illâ teẕkiraten li-men yahşâ, gloss:ancak içi titreyen için bir öğüt olarak indirdik, source:20:3}. Bu ayetten hemen önce ise Kur'an'ın Peygamber'in zahmet çekmesi için indirilmediği söylenir. Allah Musa ile Harun'u Firavun'a gönderirken {ar:فَقُولَا لَهُۥ قَوْلًۭا لَّيِّنًۭا لَّعَلَّهُۥ يَتَذَكَّرُ أَوْ يَخْشَىٰ, tr:fe-kûlâ lehû kavlen leyyinen leallehû yeteẕekkeru ev yahşâ, gloss:ona yumuşak bir söz söyleyin; belki öğüt alır ya da korkar, source:20:44} der. Başka bir anlatımda Musa'ya Firavun'a şöyle demesi söylenir: {ar:فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ, tr:fe-kul hel leke ilâ en tezekkâ, gloss:arınmaya niyetin var mı de, source:79:18}, {ar:وَأَهْدِيَكَ إِلَىٰ رَبِّكَ فَتَخْشَىٰ, tr:ve ehdiyeke ilâ rabbike fe-tahşâ, gloss:seni Rabbine götüreyim de içini bir korku kaplasın, source:79:19}. Firavun'a sunulan öğüt, arınma, yol gösterme ve korkuyu birlikte içerir. Firavun ise bu öğüdü reddeder. Bilgi ile korku arasındaki bağı Kur'an şöyle söyler: {ar:إِنَّمَا يَخْشَى ٱللَّهَ مِنْ عِبَادِهِ ٱلْعُلَمَٰٓؤُا۟, tr:innemâ yahşallâhe min ibâdihi'l-ulemâ, gloss:kulları içinde Allah'tan ancak bilenler korkar, source:35:28}. Uyarının kime yaradığını da söyler: {ar:إِنَّمَا تُنذِرُ ٱلَّذِينَ يَخْشَوْنَ رَبَّهُم بِٱلْغَيْبِ وَأَقَامُوا۟ ٱلصَّلَوٰةَ ۚ وَمَن تَزَكَّىٰ فَإِنَّمَا يَتَزَكَّىٰ لِنَفْسِهِۦ, tr:innemâ tunẕiru'lleẕîne yahşevne rabbehum bi'l-ğaybi ve ekâmu's-salâh ve men tezekkâ fe-innemâ yetezekkâ li-nefsih, gloss:sen ancak Rablerinden görmeden korkan ve namazı kılanları uyarırsın; arınan kendisi için arınır, source:35:18}. Bu ayet surenin onuncu, on dördüncü ve on beşinci ayetlerini tek bir cümlede verir. Öğütten uzak durmanın sonucu da anlatılır: {ar:وَمَنْ أَعْرَضَ عَن ذِكْرِى فَإِنَّ لَهُۥ مَعِيشَةًۭ ضَنكًۭا, tr:ve men a'rada an ẕikrî fe-inne lehû maîşeten danka, gloss:kim beni anmaktan yüz çevirirse onun dar bir geçimi olur, source:20:124}. Bir başka yerde öğütten yüz çeviren {ar:إِلَّا مَن تَوَلَّىٰ وَكَفَرَ, tr:illâ men tevellâ ve kefer, gloss:yüz çevirip inkâr eden müstesna, source:88:23} diye anılır ve en büyük azaba çarptırılır.

Kaynaklar: 87:9 فَذَكِّرْ ذ ك ر B009; 87:9 نَّفَعَتِ ن ف ع B001; 87:10 يَخْشَىٰ خ ش ي B001; 87:10 يَخْشَىٰ خ ش ي B002; 87:11 يَتَجَنَّبُهَا ج ن ب B003; 87:11 يَتَجَنَّبُهَا ج ن ب B004; 87:11 ٱلْأَشْقَى ش ق و B001

## Buluşmalar

İmgelerin çoğu, surenin son ayetinde adı geçen Musa'nın hikâyesinde buluşur. Musa uzakta bir ateş görür ve {ar:أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ecidu ale'n-nâri hudâ, gloss:ateşin başında bir yol gösteren bulurum, source:20:10} umuduyla ona yönelir. Uzaktan görülen ateşin sahnesi ile yol sahnesi burada aynı cümlededir. Ateşin başında önce seçim gelir: {ar:وَأَنَا ٱخْتَرْتُكَ, tr:ve ene'htertuk, gloss:seni ben seçtim, source:20:13}. Sonra namaz ve anma gelir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14}. Sonra gizli olan gelir: {ar:أَكَادُ أُخْفِيهَا, tr:ekâdu uhfîhâ, gloss:onu neredeyse gizli tutuyorum, source:20:15}. Başka bir anlatımda ateşin başında tesbih söylenir: {ar:وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve subhânallâhi rabbi'l-âlemîn, gloss:Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu sahnede surenin on ikinci ve on beşinci ayetleri arasındaki karşıtlık bir kişinin yolculuğunda çözülür. Aynı ateşe yaklaşan biri onun içine sokulmaz. Ateş ona yol, seçilmişlik, namaz ve anma verir. Surede bu iki son iki ayrı kişiye düşer: on ikinci ayetteki kişi ateşe girer, on beşinci ayetteki kişi namaz kılar. Kelimelerin harf benzerliği bu ayrılığı kulakta da duyurur.

İkinci büyük buluşma selin sahnesidir. Gökten inen suyun vadilerde {ar:بِقَدَرِهَا, tr:bi-kaderihâ, gloss:kendi ölçülerince, source:13:17} akması, ölçüp biçme sahnesini çağırır. Selin taşıdığı köpük, otlağın vardığı döküntüdür. İnsanların {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâr, gloss:ateşte üzerine yaktıkları şeyden, source:13:17} çıkan köpük ise ateşin sahnesine girer. Faydalı olanın yerde kalması da öğüdün ve kalıcılığın sahnesidir. Kurumuş otun tencerenin köpüğüyle aynı adı taşıması, bu iki köpüğün Arapçada zaten tek bir kelimede birleştiğini gösterir. Bu ayet surenin beşinci ayetinden on yedinci ayetine uzanan çizgiyi tek bir manzaraya sığdırır. Bir yanda giden döküntü, öbür yanda kalan fayda vardır.

Üçüncü buluşma, Musa'nın karşısındaki sihirbazların sahnesidir. Sihirbazlar secdeye kapanır. Firavun kendi azabının daha çetin ve {ar:وَأَبْقَىٰ, tr:ve ebkâ, gloss:ve daha kalıcı, source:20:71} olduğunu söyler. Sihirbazlar da onu {ar:لَن نُّؤْثِرَكَ, tr:len nu'ŝirak, gloss:seni asla tercih etmeyiz, source:20:72} diye reddeder, yalnızca {ar:هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:hâẕihi'l-hayâte'd-dunyâ, gloss:bu dünya hayatı, source:20:72} üzerinde hüküm verebileceğini söyler ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Sonra suçlu için {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:20:74} der, iman edenler için {ar:ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:ed-derecâtu'l-ulâ, gloss:en yüce dereceler, source:20:75} der, ve hepsini {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76} sözüyle bağlar. Bu birkaç ayette seçim, kalıcı hayat, yükseklik ve yarılan tarlanın kelimeleri birlikte konuşur. Firavun'un "en yüce" iddiası da başka bir anlatımda bu sahneye eklenir. Surenin ikinci yarısı, on üçüncü ayetten on yedinci ayete kadar, neredeyse kelimesi kelimesine Musa'nın hikâyesindeki bir topluluğun ağzından gelmiştir. Son ayetin Musa'nın sayfalarını anması da bu yüzden önem taşır.

Dördüncü buluşma ot ile seçimdir. Dünya hayatının kuruyan ota benzetildiği ayetin hemen ardından kalıcı iyi işlerin daha hayırlı olduğu söylenir. Dünya hayatı başka bir yerde bir {ar:زَهْرَةَ, tr:zehrate, gloss:çiçek, source:20:131} olarak anılır, ve aynı ayet {ar:خَيْرٌۭ وَأَبْقَىٰ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:20:131} diye biter. Otlağın sahnesi seçimin sahnesine bu yolla girer. Beşinci ayetteki ot ile on altıncı ayetteki tercih edilen hayat aynı nesnedir. Kalıcı olan ise ayıklanıp seçilen şeydir. Tarlanın sahnesi bu iki uç arasında bir yol açar. Kalıcı iyilik anlamına gelen kurtuluş kelimesi on dördüncü ayette, toprağı yaran çiftçinin kelimesiyle söylenir. Yabani ot kendi haline kalınca kurur ve selle gider. İşlenen toprağın ürünü ise büyür, hakkı verilir ve geriye kalan bir pay bırakır. Biri dünya tarlası, öbürü ahiret tarlasıdır.

Beşinci buluşma, yaratma fiillerinde zanaat ile bedenin birleşmesidir. İkinci ayetteki ikili hem yontulmuş oku hem de ceninin biçimlenmesini anlatır. Rahimden başlayan ayetin toprağın yağmurla titreşmesiyle bitmesi, beden ile otlağı da birbirine bağlar. Aynı aile, üçüncü ayetteki ölçmeyi pay ölçmeye de taşır, ve on altıncı ayetteki tercih bir pay seçimine döner. Değneği ateşte doğrultmanın fiili on ikinci ayetin fiilidir. Bu fiil aynı ateşin düzelten bir işi ile içine düşenin katlandığı bir işi olduğunu duyurur. Bu son bağ dilin yankısıdır, ayetin sözü değildir.

Bu buluşmalar surenin hareketini taşır. Sure tesbih emriyle ve yükseklikle açılır. Ölçen, yontan ve yol gösteren Rabbin işiyle devam eder. Yağmurun çıkardığı ve selin götürdüğü ot ile sona gelen bir ömür gösterir. Sonra sözün toplanıp unutulmamasına, sunulan öğüde ve öğüt karşısında ikiye ayrılan insanlara geçer. Biri ateşe girer ve ne ölü ne diri kalır. Öbürü arınır, Rabbinin adını anar ve namaz kılar, yani surenin başındaki emri yerine getirir. Ardından seçim gelir: yakın olan öne konmuştur, ama arkadan gelen daha hayırlı ve daha kalıcıdır. Sure, bu sözün ilk sayfalarda, ateşin başında namaz ve anma emrini alan Musa'nın ve Rabbinden kendisini puttan uzak tutmasını isteyen İbrahim'in sayfalarında yazılı olduğunu söyleyerek kapanır.

