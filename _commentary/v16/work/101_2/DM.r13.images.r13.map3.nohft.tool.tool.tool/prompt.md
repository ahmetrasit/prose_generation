Focus: 101:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/101_2/D.r13/context.md =====
# 101:2 — focus

مَا ٱلْقَارِعَةُ

Anchor translation (canonical reading, reference only):

Çarpan felaket nedir?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | مَا | مَا |  | INTG |
| 2 | ٱلْقَارِعَةُ | قَارِعَة | ق ر ع | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 101 — full text (context; no pericope)

- 101:1 ٱلْقَارِعَةُ
- 101:2 ◀ focus مَا ٱلْقَارِعَةُ
- 101:3 وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ
- 101:4 يَوْمَ يَكُونُ ٱلنَّاسُ كَٱلْفَرَاشِ ٱلْمَبْثُوثِ
- 101:5 وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ ٱلْمَنفُوشِ
- 101:6 فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ
- 101:7 فَهُوَ فِى عِيشَةٍۢ رَّاضِيَةٍۢ
- 101:8 وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ
- 101:9 فَأُمُّهُۥ هَاوِيَةٌۭ
- 101:10 وَمَآ أَدْرَىٰكَ مَا هِيَهْ
- 101:11 نَارٌ حَامِيَةٌۢ


===== _commentary/v16/work/101_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق ر ع (root_001219) — identity root of ٱلْقَارِعَةُ (w2)

- **B001** bir şeye vurmak veya çarpmak — vurmak, çarpmak veya vurarak uyarmak · kaptakini sonuna kadar içince kabın alnına değmesi · hayvana vurmak için kullanılan değnek · taş kırmaya yarayan balta benzeri araç · ateş yakmak için kullanılan çakma aracı
  القاف والراء والعين معظم الباب ضرب الشيء (maqayis)؛ كل شيء ضربته فقد قرعته (ayn)؛ قرعت الباب أقرعه قرعا (sihah)؛ قرع راحلته أي ضربها بسوطه (tahdhib)؛ القرع ضرب شيء على شيء (mufradat)
- **B002** kılıçlarla karşılıklı çarpışmak — savaşta kılıçlarla karşılıklı dövüşme · dövüşte karşı karşıya gelen rakip
  مقارعة الأبطال قرع بعضهم بعضا (maqayis)؛ المقارعة والقراع المضاربة بالسيف في الحرب (ayn)؛ قريعك الذي يقارعك (sihah)؛ القراع والمقارعة المضاربة بالسيوف (tahdhib)
- **B003** damızlık erkeğin dişiyle çiftleşmesi ve dişinin erkeği istemesi — erkek hayvanın dişiye çiftleşmek için çıkması · çiftleşme için ayrılmış damızlık erkek · dişi deve veya sığırın çiftleşmek istemesi
  القريع الفحل لأنه يقرع الناقة (maqayis)؛ القريع من الإبل الفحل (ayn)؛ قرع الفحل الناقة يقرعها قرعا وقراعا (sihah)؛ استقرعت الناقة إذا اشتهت الضراب (tahdhib)
- **B004** kura çekmek ve kurayla paylaştırmak — kura veya kurada çıkan pay · aralarında kura çektirmek · kura çekerek seçmek veya paylaştırmak
  الإقراع والمقارعة هي المساهمة (maqayis)؛ أقرع القوم وتقارعوا بينهم والاسم القرعة (ayn)؛ أقرعت بينهم من القرعة واقترعوا وتقارعوا بمعنى (sihah)؛ أقرعت بين الشركاء في شيء يقتسمونه فاقترعوا عليه (tahdhib)
- **B005** sarsıcı büyük felaket veya dünyanın sonundaki hesap günü — büyük felaket veya dünyanın sonundaki hesap günü · Kuran'dan korkuya karşı okunan koruyucu bölümler
  القارعة الشديدة من شدائد الدهر والقارعة القيامة (maqayis)؛ القارعة القيامة والقارعة الشدة (ayn)؛ القارعة الشديدة من شدائد الدهر وهي الداهية (sihah)؛ النازلة الشديدة تنزل عليهم بأمر عظيم (tahdhib)؛ القارعة ما القارعة (mufradat)
- **B006** öğütle yola gelmek; durdurmak veya azarlamak — öğüt dinleyip vazgeçmek · doğru olana geri dönüp boyun eğmek · alıkoymak ve caydırmak · sertçe azarlama ve kınama · pişmanlıktan dişine vurmak
  رجل قرع إذا كان يقبل مشورة المشير (maqayis)؛ أقرعت إلى الحق إقراعا رجعت (maqayis)؛ فلان لا يقرع إقراعا إذا كان لا يقبل المشورة والنصيحة (sihah)؛ التقريع التعنيف (sihah)؛ فلان لا يقرع أي لا يرتدع (tahdhib)؛ أقرعته إذا كففته (tahdhib)
- **B007** seçilmiş önder veya bir şeyin en iyi bölümü; en iyisini vermek — güvenilen önder veya başkan · seçilmiş kişi veya önder · malın en iyi ve seçkin bölümü · evin sıcak veya soğukta en iyi yeri · ona malının en iyi bölümünü vermek
  القريع وهو السيد سمى بذلك لأنه يعول عليه في الأمور (maqayis)؛ أقرع فلان فلانا أعطاه خير ماله وخيار المال قرعته (maqayis)؛ القريعة وهو خير بيت في الربع (maqayis)؛ المقروع المختار للفحلة والمقروع السيد (sihah)؛ قريعة البيت خير موضع فيه (tahdhib)؛ القريعة والقرعة خيار المال (tahdhib)
- **B008** saç ya da örtü kaybı; bir yerin boş veya bitkisiz kalması — bir hastalık yüzünden saçların dökülmesi · saçı hastalık nedeniyle dökülmüş; kel · deri veya tüy hastalığına tutulmuş yavru deve · avlu veya hayvan barınağının boş kalması · bitki yetiştirmeyen veya otlatılıp çıplak kalmış arazi · açıkta kalan cinsel bölge · başında tüy bulunmayan iri yılan
  مما شذ عن هذا الأصل القرع وفصيل مقرع والقرع أيضا ذهاب الشعر من الرأس (maqayis)؛ القرع ذهاب شعر الرأس من داء (ayn)؛ الأقرع الذي ذهب شعر رأسه من آفة (sihah)؛ قرع الفناء إذا خلا من الغاشية (sihah)؛ أرض قرعة لا تنبت شيئا (tahdhib)؛ أصبحت الرياض قرعا قد جردتها المواشي (tahdhib)
- **B009** kabak meyvesi — kabak meyvesi
  القرع حمل اليقطين الواحدة قرعة (ayn)؛ القرع حمل اليقطين الواحدة قرعة (sihah)؛ القرع حمل اليقطين (tahdhib)
- **B010** yolun açık üst kesimi veya evin önü — yolun açık veya üst kesimi; evin önündeki açık alan
  قارعة الدار ساحتها وقارعة الطريق أعلاه (sihah)؛ قرعاء الدار ساحتها (tahdhib)؛ قارعة الطريق ساحتها وقارعة الطريق أعلاه (tahdhib)
- **B011** sert ve dayanıklı; kazınıp pürüzsüzleştirilmiş — sert ve dayanıklı · çakılla ovulmuş kap veya kabuğu soyulmuş dal · sertleşmiş toynak veya işkembe
  القراع الصلب الشديد (sihah)؛ ترس أقرع إذا كان صلبا وهو القراع أيضا (tahdhib)؛ قدح أقرع وهو الذي حك بالحصى (tahdhib)؛ مكان أقرع شديد صلب (tahdhib)
- **B012** yiyecek veya hurma konan torba ya da kap — yiyecek koymaya yarayan küçük veya geniş torba · hurma toplamak için kullanılan kap
  القرعة الجراب الواسع يلقى فيه الطعام (tahdhib)؛ القرعة الجراب الصغير وجمعها قرع (tahdhib)؛ المقرع وعاء يجبى فيه التمر (tahdhib)؛ قرع فلان في مقرعه كله السقاء والزق (tahdhib)

===== _commentary/v16/out/s101/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 101:1, whose words 101:2 repeats, and ## Buluşmalar) =====
## Vuruş: sıkı olanın dağılması

Surenin ilk kelimesi bir şeyi adıyla değil, yaptığı işle anar. {ar:ٱلْقَارِعَةُ, tr:el-kâria, gloss:vuran, çarpan, source:101:1} kelimesinin kökünde yatan iş, sert bir şeyin başka bir şeyin üstüne indirilmesidir: {ar:القرع ضرب شيء على شيء, tr:el-kar' darbu şey'in alâ şey', gloss:kar', bir şeyin bir şeye vurulmasıdır, source:"ق ر ع,B001"}. Binicinin hayvanını kamçıyla dürtmesi de aynı fiille söylenir: {ar:قرع راحلته أي ضربها بسوطه, tr:karaa râhilatehû, gloss:bineğini kamçısıyla vurdu, source:"ق ر ع,B001"}. Aynı kelime, insanların başına inen ağır belanın da adıdır: {ar:القارعة الشديدة من شدائد الدهر وهي الداهية, tr:el-kâria eş-şedîde min şedâidi'd-dehr, gloss:kâria, zamanın ağır sıkıntılarından biri, büyük felakettir, source:"ق ر ع,B005"}. Bir aile imgesi, kelimenin ayetteki anlamının yerine geçmez; o anlamın yanında duyulur. Burada kelimenin anlamı kıyamettir, duyulan imge ise bir darbenin inişi.

Bu darbe imgesini yalın bir açıklamadan ayıran şey, sonrasında olanlardır. Bir vuruş, sıkı ve bütün olan şeyi çözer; parçaları havaya kaldırır. Dördüncü ayet insanları {ar:ٱلْمَبْثُوثِ, tr:el-mebsûs, gloss:saçılmış, source:101:4} diye niteler. Bu kökün temel işi, rüzgârın toprağı kaldırıp dağıtması gibi bir dağıtmadır: {ar:التفريق وإثارة الشيء كبث الريح التراب, tr:et-tefrîk ve isâratu'ş-şey', gloss:ayırmak ve bir şeyi rüzgârın toprağı savurduğu gibi kaldırmak, source:"ب ث ث,B001"}; kışkırtılan toza da bu adla bakılır {source:"ب ث ث,B001"}. Beşinci ayetin dağları {ar:ٱلْمَنفُوشِ, tr:el-menfûş, gloss:didilmiş, atılmış, source:101:5} yündür. Yünün atılması da bir dövme işidir: {ar:نفش الصوف وهو أن يطرق حتى يتنفش, tr:nefşu's-sûf ve hüve en yutraka hattâ yetenaffeş, gloss:yünü atmak, kabarıp açılıncaya kadar onu dövmektir, source:"ن ف ش,B001"}. Yani dağların sonunu gösteren benzetme de darbelerle kurulmuştur. Yünü anlatan {ar:ٱلْعِهْنِ, tr:el-ıhn, gloss:boyalı yün, source:101:5} kelimesinin kökü, ayrıca kuvvetle kırılmış ama kopmamış, sarkıp kalmış bir dalı da adlandırır: {ar:أصل العاهن أن يتقصف القضيب من الشجرة ولا يبين منها فيبقى معلقا مسترخيا, tr:aslu'l-âhin en yetekassafe'l-kadîb, gloss:âhin, ağaçtan kırılıp ayrılmayan, asılı ve gevşek kalan daldır, source:"ع ه ن,B002"}. Sert bir biçim boyun eğmiş, ama yerinden kopmadan sallanıp kalmıştır.

Dokuzuncu ayetin {ar:هَاوِيَةٌ, tr:hâviye, gloss:düşülen derin çukur, source:101:9} kelimesinin kökü, darbenin öbür yarısını, vuran kolun inişini ve yukarıdan aşağı fırlatmayı da taşır: {ar:أهويت له بالسيف, tr:ehveytu lehû bi's-seyf, gloss:kılıcı ona doğru indirdim, source:"ه و ي,B003"}; {ar:أهويته إذا ألقيته من فوق, tr:ehveytuhû izâ elkaytuhû min fevk, gloss:onu yukarıdan attım, source:"ه و ي,B003"}. Böylece sure vuruştan saçılmaya, saçılmadan çukura atılışa doğru ilerler: önce iniş, sonra dağılma, en sonda hafif olanın aşağı fırlatılması.

Aynı kökler başa inen bir darbeyi de adlandırır. Kafatasının ince kemikleri {ar:فراش الرأس عظام رقاق تلي القحف, tr:ferâşu'r-re's izâmun rikâk, gloss:başın ferâşı, kafatasına bitişik ince kemiklerdir, source:"ف ر ش,B010"} diye anılır ve bir deyim, bu kemikleri uçuran vuruşu anlatır: {ar:ضربة فأطار فراش رأسه, tr:darbeten fe-etâra ferâşe re'sih, gloss:bir vuruş ki başının ince kemiklerini uçurdu, source:"ف ر ش,B011"}. Beynin zarına {ar:أم الرأس وهو الدماغ, tr:ummu'r-re's, gloss:başın anası, yani beyin, source:"ء م م,B003"} denir; ağzını açan yara için de {ar:هوت الطعنة إذا فتحت فاها, tr:hevet et-ta'ne, gloss:mızrak yarası ağzını açtı, source:"ه و ي,B007"} söylenir. Surenin kelimeleri bu dizilişte birbirini izler: birinci ayette vuruş, dördüncüde ferâş, dokuzuncuda ümm ve hâviye. Bu dizi bir aile imgesidir; ayetlerin anlamı kıyamet, insanlar, dağlar ve varılacak yerdir.

Kur'an bu darbeyi başka yerlerde de sahneler. Hâkka suresinde Allah, geçmiş kavimleri anlatırken {ar:كَذَّبَتْ ثَمُودُ وَعَادٌۢ بِٱلْقَارِعَةِ, tr:kezzebet Semûdu ve Âdun bi'l-kâria, gloss:Semûd ve Âd o çarpanı yalanladı, source:69:4} der; aynı surede yer ve dağlar kaldırılır ve {ar:فَدُكَّتَا دَكَّةًۭ وَٰحِدَةًۭ, tr:fe-dukketâ dekketen vâhide, gloss:bir tek çarpışla ezilip düzlendiler, source:69:14}. Ra'd suresinde Allah, inkâr edenler hakkında Peygamberine, onlara yaptıkları yüzünden {ar:قَارِعَةٌ أَوْ تَحُلُّ قَرِيبًۭا مِّن دَارِهِمْ, tr:kâriatun ev tehullu karîben min dârihim, gloss:bir çarpan, ya da yurtlarının yakınına inen bir bela, source:13:31} isabet etmeye devam edeceğini söyler; aynı ayet, Kur'an ile dağların yürütülmesini de anar. Vâkıa suresinde dağlar {ar:وَبُسَّتِ ٱلْجِبَالُ بَسًّۭا, tr:ve bussetil-cibâlu bessâ, gloss:dağlar ufalanıp un ufak edilir, source:56:5} ve {ar:فَكَانَتْ هَبَآءًۭ مُّنۢبَثًّۭا, tr:fe-kânet hebâen munbessâ, gloss:saçılmış toz olur, source:56:6}; buradaki "saçılmış", dördüncü ayetteki mebsûs ile aynı köktendir. Darbe ile dağılmanın arka arkaya gelişi, böylece Kur'an'ın kendi sahnesinde de görülür.

Kaynaklar: 101:1 ٱلْقَارِعَةُ ق ر ع B001; 101:1 ٱلْقَارِعَةُ ق ر ع B005; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:5 ٱلْمَنفُوشِ ن ف ش B001; 101:5 كَٱلْعِهْنِ ع ه ن B002; 101:9 هَاوِيَةٌ ه و ي B003; 101:4 كَٱلْفَرَاشِ ف ر ش B010; 101:4 كَٱلْفَرَاشِ ف ر ش B011; 101:9 فَأُمُّهُۥ ء م م B003; 101:9 هَاوِيَةٌ ه و ي B007

## Kapı çalınır, içeriden soru gelir

Aynı fiil kapının çalınmasını da anlatır: {ar:قرعت الباب أقرعه قرعا, tr:kara'tu'l-bâbe, gloss:kapıyı çaldım, source:"ق ر ع,B001"}. Kelime, evin önündeki açık alanın, yani vuruşun indiği yerin adıdır da: {ar:قارعة الدار ساحتها, tr:kâriatu'd-dâr sâhatuhâ, gloss:evin kâriası, onun avlusudur, source:"ق ر ع,B010"}. Bu imgeyle surenin ilk üç ayeti bir kapı sahnesi gibi işler. Önce vuruş gelir: tek kelime. Sonra içeriden bir ses sorar: {ar:مَا ٱلْقَارِعَةُ, tr:me'l-kâria, gloss:nedir o çarpan, source:101:2}. Ardından soru katlanır: {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْقَارِعَةُ, tr:ve mâ edrâke me'l-kâria, gloss:o çarpanın ne olduğunu sana ne bildirdi, source:101:3}. Kapıyı çalanın kim olduğu söylenmez; cevap bir isim olarak değil, dördüncü ve beşinci ayetlerdeki sahne olarak gelir.

"Bildirmek" fiilinin kökü, kişinin kendi çabasıyla vardığı bir bilgiyi anlatır: {ar:الدراية المعرفة المدركة بضرب من الحيل, tr:ed-dirâye el-ma'rifetu'l-mudreke, gloss:dirâye, bir tür çabayla ulaşılan bilgidir, source:"د ر ي,B001"}; aynı kökte bilmek ile bildirilmek yan yanadır: {ar:دريته ودريت به أي علمت به وأدريته أي أعلمته, tr:dereytuhû... ve edreytuhû, gloss:onu bildim; ona bildirdim, source:"د ر ي,B001"}. Üçüncü ayetteki soru, bu bilginin çabayla ulaşılamayacağını, ancak dışarıdan verilebileceğini hissettirir. Dördüncü ayetin mebsûs kelimesi bu imgeye bir anlam daha katar: aynı kök, haberin yayılmasını ve gizlinin açığa vurulmasını da adlandırır: {ar:أبثثتك سري؛ أظهرته لك, tr:ebsestuke sirrî, gloss:sırrımı sana açtım, source:"ب ث ث,B002"}. Sorunun cevabı, her şeyin açığa saçıldığı bir sahne olarak gelir.

Kelimenin bir anlamı daha, kapıyı çalmanın amacını gösterir: uyarı, onu dinleyeni geri döndürür; dinlemeyen için ise azardır. {ar:أقرعت إلى الحق إقراعا رجعت, tr:akra'tu ile'l-hakk, gloss:hakka döndüm, source:"ق ر ع,B006"}; {ar:فلان لا يقرع أي لا يرتدع, tr:fulânun lâ yukra', gloss:filan kişi uyarıdan geri durmaz, source:"ق ر ع,B006"}. Sure bir vuruşla açılır, çünkü vuruş içerideki kişiyi uyandırmak içindir.

Onuncu ayette aynı soru kalıbı geri döner, bu kez çukur için: {ar:وَمَآ أَدْرَىٰكَ مَا هِيَهْ, tr:ve mâ edrâke mâ hiyeh, gloss:onun ne olduğunu sana ne bildirdi, source:101:10}. Bu sefer cevap bekletilmez; on birinci ayet tek bir ifadeyle karşılık verir: {ar:نَارٌ حَامِيَةٌۢ, tr:nârun hâmiye, gloss:kızgın bir ateş, source:101:11}. Surenin başındaki soru bir sahneyle, sonundaki soru bir ateşle cevaplanır.

Kur'an bu soru kalıbını birçok yerde kullanır. Hâkka suresi aynı üç adımla açılır: {ar:ٱلْحَآقَّةُ, tr:el-hâkka, gloss:gerçekleşecek olan, source:69:1}, {ar:مَا ٱلْحَآقَّةُ, tr:me'l-hâkka, gloss:nedir o gerçekleşecek olan, source:69:2}, {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْحَآقَّةُ, tr:ve mâ edrâke me'l-hâkka, gloss:onun ne olduğunu sana ne bildirdi, source:69:3}; hemen ardından Semûd ile Âd'ın kâriayı yalanladığı anlatılır {source:69:4}. Hümeze suresinde Allah, kusur arayanın {ar:لَيُنۢبَذَنَّ فِى ٱلْحُطَمَةِ, tr:le-yunbezenne fi'l-hutame, gloss:o mutlaka ezip kırana atılacak, source:104:4} olduğunu söyler, sonra sorar: {ar:وَمَآ أَدْرَىٰكَ مَا ٱلْحُطَمَةُ, tr:ve mâ edrâke me'l-hutame, gloss:ezip kıranın ne olduğunu sana ne bildirdi, source:104:5} ve cevap yine bir ateştir: {ar:نَارُ ٱللَّهِ ٱلْمُوقَدَةُ, tr:nâru'llâhi'l-mûkade, gloss:Allah'ın tutuşturulmuş ateşi, source:104:6}. Müddessir suresinde {ar:وَمَآ أَدْرَىٰكَ مَا سَقَرُ, tr:ve mâ edrâke mâ sekar, gloss:sekarın ne olduğunu sana ne bildirdi, source:74:27} sorusuna {ar:لَا تُبْقِى وَلَا تَذَرُ, tr:lâ tubkî ve lâ tezer, gloss:ne bırakır ne geri koyar, source:74:28} diye cevap verilir. İnfitâr suresinde soru iki kez sorulur, {ar:ثُمَّ مَآ أَدْرَىٰكَ مَا يَوْمُ ٱلدِّينِ, tr:summe mâ edrâke mâ yevmu'd-dîn, gloss:sonra, ceza gününün ne olduğunu sana ne bildirdi, source:82:18}, ve cevap {ar:يَوْمَ لَا تَمْلِكُ نَفْسٌۭ لِّنَفْسٍۢ شَيْـًۭٔا, tr:yevme lâ temliku nefsun li-nefsin şey'â, gloss:hiçbir canın bir başka can için hiçbir şeye güç yetiremediği gün, source:82:19} olur. Târık suresinde gece gelen yolcu da aynı soruyla anılır: {ar:وَمَآ أَدْرَىٰكَ مَا ٱلطَّارِقُ, tr:ve mâ edrâke me't-târık, gloss:gece gelenin ne olduğunu sana ne bildirdi, source:86:2}, cevap {ar:ٱلنَّجْمُ ٱلثَّاقِبُ, tr:en-necmu's-sâkıb, gloss:delip geçen yıldız, source:86:3}. Arapçada târık, gece kapıyı çalarak gelen kişidir {source:"memory"}; kökü kâriadan farklıdır, ama sahne aynı türden bir kapı vuruşudur.

Kaynaklar: 101:1 ٱلْقَارِعَةُ ق ر ع B001; 101:1 ٱلْقَارِعَةُ ق ر ع B010; 101:1 ٱلْقَارِعَةُ ق ر ع B006; 101:3 أَدْرَىٰكَ د ر ي B001; 101:10 أَدْرَىٰكَ د ر ي B001; 101:4 ٱلْمَبْثُوثِ ب ث ث B002

## Savaş günü

Araplar savaşlarına "gün" adını verirdi. Aynı kökte gün, olup biten olayın kendisidir: {ar:الأيام في معنى الوقائع, tr:el-eyyâm fî ma'ne'l-vekâi', gloss:günler, vakalar, çarpışmalar anlamında, source:"ي و م,B003"}. Bu tanım dördüncü ayetin fiilini de içine alır: {ar:اليوم: الكون، الكائنة من الكون إذا نزلت أو حدثت, tr:el-yevm: el-kevn, el-kâine, gloss:gün, olan şey, inip meydana gelen olaydır, source:"ي و م,B003"}. Fiilin kendi kökünde ise {ar:الكون الحدث يكون بين الناس, tr:el-kevnu el-hadesu yekûnu beyne'n-nâs, gloss:kevn, insanlar arasında olan olaydır, source:"ك و ن,B001"} denir. Dördüncü ayetin {ar:يَوْمَ يَكُونُ ٱلنَّاسُ, tr:yevme yekûnu'n-nâs, gloss:insanların ... olacağı gün, source:101:4} ifadesi, bu tanımın kelimelerini taşır.

Kâria kelimesinin bir kolu da kılıç çarpışmasıdır: {ar:المقارعة والقراع المضاربة بالسيف في الحرب, tr:el-mukâra'a ve'l-kırâ', gloss:savaşta kılıçla karşılıklı vuruşmak, source:"ق ر ع,B002"}. Surenin öbür kelimeleri, aynı meydanın birer parçasını adlandırır. Mebsûs atların akına dağıtılmasıdır: {ar:بثوا الخيل, tr:besse'l-hayl, gloss:atları yaydılar, source:"ب ث ث,B001"}. "Bildirmek" fiilinin bir kalıp kullanımı, bir yerin baskın hedefi olarak seçilmesini anlatır: {ar:ادرى بنو فلان مكان كذا أي اعتمدوه بغزو أو غارة, tr:iddarâ benû fulân mekâne kezâ, gloss:filan oğulları falan yeri baskın için hedef aldı, source:"د ر ي,B002"}. Sekizinci ayetin "hafif geldi" fiili, obanın aceleyle göçmesini de anlatır: {ar:خف القوم إذا ارتحلوا مسرعين, tr:haffe'l-kavm, gloss:topluluk aceleyle göçtü, source:"خ ف ف,B002"}. On birinci ayetin ateşi, kabile içinde parlayan düşmanlığın da adıdır: {ar:النائرة الكائنة تقع بين القوم, tr:en-nâira el-kâine, gloss:nâira, topluluk arasında patlak veren olaydır, source:"ن و ر,B007"}; burada yine kâine kelimesi, yani gün ve olmak kelimelerinin kökü geçer. Hâmiye ise savaşta ailesini koruyanı {ar:حمى أهله في القتال حماية, tr:hamâ ehlehû fi'l-kıtâl, gloss:savaşta ailesini korudu, source:"ح م ي,B002"} ve öfkesi kızışan savaşçıyı {ar:حميت عليه غضبت, tr:hamîtu aleyh, gloss:ona öfkelendim, source:"ح م ي,B003"} anlatır.

Bu imge, düz bir anlatımın veremeyeceği bir şeyi duyurur: kıyamet uzak bir tarih değil, bir topluluğun başına gelen bir gündür, tıpkı tarihte anılan savaş günleri gibi. Kelimenin bir kalıp kullanımı da bunu Kur'an'a bağlar: {ar:وذكرهم بأيام الله: بما نزل بعاد وثمود وغيرهم من العذاب, tr:ve zekkirhum bi-eyyâmi'llâh, gloss:onlara Allah'ın günlerini hatırlat, yani Âd'a, Semûd'a ve başkalarına inen azabı, source:"ي و م,B004"}. İbrâhîm suresinde Allah, Mûsâ'yı kavmine gönderirken ona {ar:وَذَكِّرْهُم بِأَيَّىٰمِ ٱللَّهِ, tr:ve zekkirhum bi-eyyâmi'llâh, gloss:onlara Allah'ın günlerini hatırlat, source:14:5} diye emreder; birkaç ayet sonra Mûsâ, kavmine Nûh, Âd ve Semûd kavimlerinin haberini hatırlatır {source:14:9}. Hâkka suresinde ise kâriayı yalanlayanlar tam da bu iki kavimdir {source:69:4}: {ar:فَأَمَّا ثَمُودُ فَأُهْلِكُوا۟ بِٱلطَّاغِيَةِ, tr:fe-emmâ Semûdu fe-uhlikû bi't-tâğiye, gloss:Semûd, haddi aşan bir sarsıntıyla yok edildi, source:69:5}, {ar:وَأَمَّا عَادٌۭ فَأُهْلِكُوا۟ بِرِيحٍۢ صَرْصَرٍ عَاتِيَةٍۢ, tr:ve emmâ Âdun fe-uhlikû bi-rîhin sarsarin âtiye, gloss:Âd ise azgın, uğuldayan bir rüzgârla yok edildi, source:69:6}. Bu iki ayetin "fe-emmâ ... ve emmâ" kalıbı, Kâria suresinin altıncı ve sekizinci ayetlerinde tekrarlanır.

Kaynaklar: 101:1 ٱلْقَارِعَةُ ق ر ع B002; 101:4 يَوْمَ ي و م B003; 101:4 يَوْمَ ي و م B004; 101:4 يَكُونُ ك و ن B001; 101:5 وَتَكُونُ ك و ن B001; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:3 أَدْرَىٰكَ د ر ي B002; 101:10 أَدْرَىٰكَ د ر ي B002; 101:8 خَفَّتْ خ ف ف B002; 101:11 نَارٌ ن و ر B007; 101:11 حَامِيَةٌ ح م ي B002; 101:11 حَامِيَةٌ ح م ي B003

## Atılmış yüne dönen dağlar

Beşinci ayet {ar:وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ ٱلْمَنفُوشِ, tr:ve tekûnu'l-cibâlu ke'l-ıhni'l-menfûş, gloss:dağlar atılmış boyalı yün gibi olur, source:101:5} der. Dağ, yukarıya doğru toplanmış kütledir ve yeryüzüne çakılmış büyük bir kazıktır: {ar:تجمع الشيء في ارتفاع, tr:tecemmu'u'ş-şey' fi'rtifâ', gloss:bir şeyin yükseklikte toplanması, source:"ج ب ل,B001"}; {ar:اسم لكل وتد من أوتاد الأرض إذا عظم وطال, tr:ismun li-kulli vetedin min evtâdi'l-ard, gloss:yeryüzünün büyük ve uzun kazıklarından her birinin adı, source:"ج ب ل,B001"}. Aynı kök kalın, sert ve kuru olanı da adlandırır: {ar:شيء جبل غليظ جاف, tr:şey'un cebl, gloss:kalın ve kuru şey, source:"ج ب ل,B003"}. Kâria kelimesinin bir kolu da sert, sarsılmaz yeri anlatır: {ar:مكان أقرع شديد صلب, tr:mekânun akra', gloss:sert, katı yer, source:"ق ر ع,B011"}; darbe gelmeden önceki hal budur.

Dağın kökünün bir kalıp kullanımı, iyi eğrilmiş, bükülmüş ve dokunmuş kumaşı anlatır: {ar:الثوب الجيد النسج والغزل والفتل جيد الجبلة, tr:es-sevbu'l-ceyyidu'n-nesc, gloss:dokuması, ipliği ve bükümü iyi olan kumaş, iyi yaratılışlıdır, source:"ج ب ل,B007"}. Yün atmak ise bu işin tersidir. Lifler, birbirinden ayrılıncaya kadar ezilip açılır: {ar:النفش مدك الصوف حتى ينتفش بعضه عن بعض, tr:en-nefş meddu's-sûf, gloss:nefş, yünü birbirinden ayrılıncaya kadar ezmektir, source:"ن ف ش,B001"}. Sonunda ortaya çıkan şey yayılmış, gevşek ve içi boştur: {ar:كل شيء تراه منتشرا رخو الجوف فهو منتفش, tr:kullu şey'in terâhu munteşiran rihve'l-cevf, gloss:yayılmış ve içi gevşek gördüğün her şey kabarıktır, source:"ن ف ش,B002"}. Yün boyalıdır, çeşitli renklerdedir: {ar:العهن الصوف المصبوغ ألوانا, tr:el-ıhn es-sûfu'l-masbûğ, gloss:ıhn, çeşitli renklere boyanmış yündür, source:"ع ه ن,B003"}; kelimenin seçilmesi, rengi içinde taşımasındandır {source:"ع ه ن,B003"}.

Bu imge, düz bir "dağlar yok olur" anlatımının veremediği bir süreci görünür kılar: toplanmış olandan ayrılmışa, sıkıdan havadara, yapılmış olandan bozulmuşa. Dağı yapan şey, liflerin sıkıca bir araya gelmesiyse, kıyamet o lifleri teker teker ayırır. Kur'an dağların renklerini de anar: Fâtır suresinde Allah, yaratılıştaki işaretleri gösterirken {ar:وَمِنَ ٱلْجِبَالِ جُدَدٌۢ بِيضٌۭ وَحُمْرٌۭ مُّخْتَلِفٌ أَلْوَٰنُهَا وَغَرَابِيبُ سُودٌۭ, tr:ve mine'l-cibâli cudedun bîdun ve humrun muhtelifun elvânuhâ ve ğarâbîbu sûd, gloss:dağlarda da beyaz, kırmızı, renkleri çeşitli yollar ve simsiyah kayalar vardır, source:35:27} der. Renkli dağlar ile renkli yün arasındaki bağ, buradaki kendi bağlantımızdır; boyalı yün benzetmesi, dağların renginin dağıldıktan sonra da sürdüğünü düşündürür.

Kur'an dağların sonunu başka sahnelerde de anlatır. Meâric suresinde Allah, azabı isteyen bir soruya cevap verirken {source:70:1} surenin beşinci ayetinin hemen hemen aynı sözlerini kullanır: {ar:يَوْمَ تَكُونُ ٱلسَّمَآءُ كَٱلْمُهْلِ, tr:yevme tekûnu's-semâu ke'l-muhl, gloss:göğün erimiş maden gibi olacağı gün, source:70:8}, {ar:وَتَكُونُ ٱلْجِبَالُ كَٱلْعِهْنِ, tr:ve tekûnu'l-cibâlu ke'l-ıhn, gloss:ve dağlar boyalı yün gibi olur, source:70:9}. Tâhâ suresinde insanlar Peygambere dağları sorar ve Allah ona cevabı bildirir: dağları savurup dağıtacak {source:20:105}, {ar:فَيَذَرُهَا قَاعًۭا صَفْصَفًۭا, tr:fe-yezeruhâ kâ'an safsafâ, gloss:onları dümdüz bir alan olarak bırakacak, source:20:106}. Neml suresinde dağlar {ar:تَحْسَبُهَا جَامِدَةًۭ وَهِىَ تَمُرُّ مَرَّ ٱلسَّحَابِ, tr:tahsebuhâ câmideten ve hiye temurru merra's-sehâb, gloss:onları donmuş sanırsın, oysa bulutların geçişi gibi geçerler, source:27:88}. Müzzemmil suresinde {ar:وَكَانَتِ ٱلْجِبَالُ كَثِيبًۭا مَّهِيلًا, tr:ve kâneti'l-cibâlu kesîben mehîlâ, gloss:dağlar akıp dağılan bir kum yığını olur, source:73:14}; Nebe' suresinde {ar:وَسُيِّرَتِ ٱلْجِبَالُ فَكَانَتْ سَرَابًا, tr:ve suyyireti'l-cibâlu fe-kânet serâbâ, gloss:dağlar yürütülür ve serap olur, source:78:20}. Vâkıa suresinde dağlar saçılmış toza döner {source:56:6}. Her sahnede aynı hareket vardır: en katı olan, en gevşek olana dönüşür.

Kaynaklar: 101:5 ٱلْجِبَالُ ج ب ل B001; 101:5 ٱلْجِبَالُ ج ب ل B003; 101:5 ٱلْجِبَالُ ج ب ل B007; 101:1 ٱلْقَارِعَةُ ق ر ع B011; 101:5 كَٱلْعِهْنِ ع ه ن B003; 101:5 ٱلْمَنفُوشِ ن ف ش B001; 101:5 ٱلْمَنفُوشِ ن ف ش B002

## Çobansız sürü, seyrelen kalabalık

Menfûş kelimesinin kökü, yünün yanında bir sürü sahnesini de taşır: develerin ve koyunların geceleyin, çobansız, otlağa yayılması: {ar:نفشت الإبل والغنم أي رعت ليلا بلا راع ولا يكون النفش إلا بالليل, tr:nefeşeti'l-ibilu ve'l-ğanem, gloss:develer ve koyunlar geceleyin çobansız otladı; nefş ancak gece olur, source:"ن ف ش,B003"}; {ar:نفشت الإبل ترددت وانتشرت بلا راع, tr:nefeşeti'l-ibil, gloss:develer çobansız oraya buraya gidip yayıldı, source:"ن ف ش,B003"}. Ferâş kökü sürünün genç hayvanlarını ve yere yayılan ekini adlandırır: {ar:الفرش صغار الإبل, tr:el-ferş sığâru'l-ibil, gloss:ferş, küçük develerdir, source:"ف ر ش,B004"}; {ar:الفرش الزرع إذا فرش, tr:el-ferş ez-zer', gloss:ferş, yayıldığında ekindir, source:"ف ر ش,B008"}. Aynı açıklama, ferşi beşş ile, yani dördüncü ayetin iki kelimesini birbiriyle anlatır: {ar:يحتمل أن يكون مصدرا من فرشها الله أي بثها بثا, tr:ferşehâ'llâhu ey besse-hâ bessâ, gloss:Allah onları yaydı, yani saçıp dağıttı, source:"ف ر ش,B004"}. Kâria kökü ise otlakların sürülerce soyulup çıplak kalmasını ve ziyaretçisiz kalan avluyu anlatır: {ar:أصبحت الرياض قرعا قد جردتها المواشي, tr:asbahati'r-riyâdu kur'â, gloss:çayırlar hayvanların soyduğu çıplak yerler oldu, source:"ق ر ع,B008"}; {ar:قرع الفناء إذا خلا من الغاشية, tr:kari'a'l-finâ', gloss:avlu gelip gidenlerden boşaldı, source:"ق ر ع,B008"}. Hâviye kökü gecenin bir dilimini de adlandırır {source:"ه و ي,B006"}; sürünün başıboş kaldığı vakit.

İnsanların kendisi de bir topluluktur: {ar:الإنس جماعة الناس, tr:el-ins cemâ'atu'n-nâs, gloss:ins, insanların topluluğudur, source:"ء ن س,B001"}. Dağın kökü büyük bir insan kalabalığını da adlandırır: {ar:الجبل الجماعة العظيمة الكثيرة, tr:el-cibl el-cemâ'atu'l-azîme, gloss:cibl, büyük ve kalabalık topluluk, source:"ج ب ل,B002"}. Sekizinci ayetin fiili, bu kalabalığın seyrelmesini anlatır: {ar:خف القوم خفوفا أي قلوا وقد خفت زحمتهم, tr:haffe'l-kavmu hufûfen, gloss:topluluk azaldı, kalabalıkları hafifledi, source:"خ ف ف,B003"}; ve evlerinden hafifçe göçmelerini: {ar:خفوا عن منازلهم ارتحلوا منها في خفة, tr:haffû an menâzilihim, gloss:evlerinden hafifçe göçtüler, source:"خ ف ف,B002"}. Mebsûs bütün bunları tek kelimede toplar: {ar:كل شيء فرقته, tr:kullu şey'in ferraktehû, gloss:ayırıp dağıttığın her şey, source:"ب ث ث,B001"}. Bu aile imgesinde dördüncü ayetin insanları başıboş, gece dağılmış bir sürü gibidir; geride çıplak bir yer kalır.

Kur'an'da nefş fiili tam da bu sahnede geçer. Enbiyâ suresinde Allah, Dâvûd ile Süleymân'ın bir ekin hakkında hüküm verişini anlatır: {ar:إِذْ نَفَشَتْ فِيهِ غَنَمُ ٱلْقَوْمِ, tr:iz nefeşet fîhi ğanemu'l-kavm, gloss:o topluluğun koyunları geceleyin ona dağılıp otladığında, source:21:78}. En'âm suresinde Allah {ar:وَمِنَ ٱلْأَنْعَٰمِ حَمُولَةًۭ وَفَرْشًۭا, tr:ve mine'l-en'âmi hamûleten ve ferşâ, gloss:hayvanlardan yük taşıyanları ve küçükleri, source:6:142} yarattığını hatırlatır. Kalabalığın dağılışı da Kur'an'ın kıyamet sahnelerindedir: Zilzâl suresinde {ar:يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:yevmeizin yasduru'n-nâsu eştâten li-yurav a'mâlehum, gloss:o gün insanlar amellerini görmek için dağınık gruplar halinde çıkarlar, source:99:6}; Hac suresinde ise kıyametin sarsıntısında {ar:وَتَرَى ٱلنَّاسَ سُكَٰرَىٰ وَمَا هُم بِسُكَٰرَىٰ, tr:ve tere'n-nâse sukârâ ve mâ hum bi-sukârâ, gloss:insanları sarhoş görürsün, oysa sarhoş değillerdir, source:22:2}.

Kaynaklar: 101:5 ٱلْمَنفُوشِ ن ف ش B003; 101:4 كَٱلْفَرَاشِ ف ر ش B004; 101:4 كَٱلْفَرَاشِ ف ر ش B008; 101:4 ٱلْمَبْثُوثِ ب ث ث B001; 101:1 ٱلْقَارِعَةُ ق ر ع B008; 101:9 هَاوِيَةٌ ه و ي B006; 101:4 ٱلنَّاسُ ء ن س B001; 101:5 ٱلْجِبَالُ ج ب ل B002; 101:4 يَكُونُ ك و ن B001; 101:8 خَفَّتْ خ ف ف B003; 101:8 خَفَّتْ خ ف ف B002

## Terazi: ağır kefe, hafif kefe

Altıncı ve sekizinci ayetler iki kefeyi karşı karşıya koyar: {ar:فَأَمَّا مَن ثَقُلَتْ مَوَٰزِينُهُۥ, tr:fe-emmâ men sekulet mevâzînuhû, gloss:tartıları ağır gelen kimseye gelince, source:101:6} ve {ar:وَأَمَّا مَنْ خَفَّتْ مَوَٰزِينُهُۥ, tr:ve emmâ men haffet mevâzînuhû, gloss:tartıları hafif gelen kimseye gelince, source:101:8}. Tartmanın tanımı, bir şeyin ağırlığını benzeriyle karşılaştırmaktır: {ar:الوزن ثقل شيء بشيء مثله, tr:el-vezn siklu şey'in bi-şey'in mislih, gloss:vezn, bir şeyin ağırlığını benzeri olan bir şeyle ölçmektir, source:"و ز ن,B001"}. Ağır olan kefe aşağı iner: {ar:الثقل رجحان الثقيل, tr:es-sikal rüchânu's-sakîl, gloss:ağırlık, ağır olanın basıp inmesidir, source:"ث ق ل,B001"}. Miskal, benzerine karşı konan bilinen bir ağırlıktır {source:"ث ق ل,B004"}. Mîzân ise hem alet hem adalettir: {ar:الآلة التي يوزن بها الأشياء ميزان؛ الميزان العدل, tr:el-âletu elletî yûzenu bihe'l-eşyâ', gloss:şeylerin tartıldığı alet mîzândır; mîzân adalettir, source:"و ز ن,B002"}.

Bu imgenin düz anlatımın ötesinde gösterdiği şey, ağırlığın değer olmasıdır. Değerli ve korunan her şey ağır sayılır: {ar:كل شيء نفيس مصون ثقل, tr:kullu şey'in nefîsin masûnin sekal, gloss:değerli, korunan her şey sekaldir, source:"ث ق ل,B005"}; insanlar ve cinler "iki ağırlık" diye anılır: {ar:سمي الجن والإنس الثقلين, tr:summiye'l-cinnu ve'l-insu's-sekaleyn, gloss:cinler ve insanlar iki ağırlık diye adlandırıldı, source:"ث ق ل,B005"}. Yerin ağırlıkları, onun hazineleri ve Âdemoğullarının bedenleridir {source:"ث ق ل,B002"}. Hafiflik ise tersine değersizliktir: {ar:ما لفلان عندنا وزن أي قدر لخسته, tr:mâ li-fulânin indenâ vezn, gloss:filanın yanımızda bir ağırlığı yok, yani değeri yok, source:"و ز ن,B007"}. Hafif gelmek hem ağırlıkta hem halde hafifliktir, {ar:الخفة خفة الوزن وخفة الحال, tr:el-hiffe hiffetu'l-vezn ve hiffetu'l-hâl, gloss:hafiflik, ağırlığın ve halin hafifliğidir, source:"خ ف ف,B001"}, iyi amellerin azlığıdır {source:"خ ف ف,B003"}, akıl hafifliğidir, {ar:وخفة الرجل طيشه, tr:ve hiffetu'r-raculi tayşuh, gloss:adamın hafifliği onun savrukluğudur, source:"خ ف ف,B004"}, ve hafife alınmaktır: {ar:استخف به أهانه, tr:istehaffe bihî, gloss:onu hafife aldı, aşağıladı, source:"خ ف ف,B005"}. Hafif olan kolayca yerinden oynatılır ve peşe takılır: {ar:استخفه فلان إذا استجهله فحمله على اتباعه في غيه, tr:istehaffehû fulân, gloss:onu cahil yerine koydu ve sapkınlığında kendisine uymaya sürükledi, source:"خ ف ف,B004"}.

Surenin öbür kelimeleri bu teraziyi önceden kurar. Dördüncü ayetin pervanesi hafifliğinden dolayı bu adı almıştır: {ar:الفراش هذا الذي يطير وسمي بذلك لخفته؛ الفراشة الرجل الخفيف, tr:sumiye bi-zâlike li-hiffetih; el-ferâşe er-raculu'l-hafîf, gloss:pervane hafifliğinden ötürü böyle adlandırıldı; ferâşe hafif adamdır, source:"ف ر ش,B005"}; {ar:أطيش من فراشة, tr:etyaşu min ferâşe, gloss:pervaneden daha savruk, source:"ف ر ش,B005"}. Burada geçen savrukluk, sekizinci ayetin hafifliğini anlatan kelimenin ta kendisidir. Beşinci ayetin yünü içi boş liftir {source:"ن ف ش,B002"}; dağ ise iri, kalın gövdedir: {ar:ذو جبلة إذا كان غليظ الجسم, tr:zû cebeletin izâ kâne ğalîza'l-cism, gloss:iri gövdeli olan, source:"ج ب ل,B003"}. Yeryüzünün en ağır şeyi, en hafif şeye dönüşür. Dokuzuncu ayetin fiili hem hızlı bir düşüşü hem hızlı bir yükselişi anlatır: {ar:الهوي السريع إلى أسفل والهوي السريع إلى فوق, tr:el-huviyy es-serî' ilâ esfel ve'l-heviyy es-serî' ilâ fevk, gloss:aşağıya hızlı iniş ve yukarıya hızlı çıkış, source:"ه و ي,B002"}. Bir terazide hafif kefe yukarı kalkar; dokuzuncu ayette ise hafif kefenin sahibi aşağı düşer.

Kâria kelimesinin bir anlamı da ortaklar arasında paylaşılacak bir şey için kura çekmektir: {ar:أقرعت بين الشركاء في شيء يقتسمونه فاقترعوا عليه, tr:akra'tu beyne'ş-şurakâ', gloss:paylaşacakları bir şey için ortaklar arasında kura çektim, source:"ق ر ع,B004"}; {ar:الإقراع والمقارعة هي المساهمة, tr:el-ikrâ' ve'l-mukâra'a hiye'l-musâheme, gloss:kura çekmek, pay için ok atmaktır, source:"ق ر ع,B004"}. Bu adı taşıyan sureden sonra insanlar "fe-emmâ ... ve emmâ" ile iki paya ayrılır. Ama ayırma kura ile değil, iki şeyi karşı karşıya koyarak yapılır: {ar:وازنت بين الشيئين, tr:vâzentu beyne'ş-şey'eyn, gloss:iki şeyi tarttım, birbiriyle karşılaştırdım, source:"و ز ن,B003"}. Payı belirleyen tesadüf değil, ölçüdür. Kur'an'da kura çekilen iki sahne vardır: Sâffât suresinde Yûnus yüklü gemide {ar:فَسَاهَمَ فَكَانَ مِنَ ٱلْمُدْحَضِينَ, tr:fe-sâheme fe-kâne mine'l-mudhadîn, gloss:kura çekti ve kaybedenlerden oldu, source:37:141}; Âl-i İmrân suresinde Allah, Peygambere Meryem'in kimin himayesine gireceği için {ar:إِذْ يُلْقُونَ أَقْلَٰمَهُمْ أَيُّهُمْ يَكْفُلُ مَرْيَمَ, tr:iz yulkûne eklâmehum eyyuhum yekfulu Meryem, gloss:hangisinin Meryem'e bakacağı için kalemlerini atarlarken, source:3:44} orada olmadığını söyler.

Kur'an'da teraziyi açıkça kuran ayetler surenin kelimelerini aynen tekrarlar. A'râf suresinde Allah {ar:وَٱلْوَزْنُ يَوْمَئِذٍ ٱلْحَقُّ ۚ فَمَن ثَقُلَتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ, tr:ve'l-veznu yevmeizini'l-hakk, fe-men sekulet mevâzînuhû fe-ulâike humu'l-muflihûn, gloss:o gün tartı haktır; kimin tartıları ağır gelirse işte onlar kurtuluşa erenlerdir, source:7:8} ve {ar:وَمَنْ خَفَّتْ مَوَٰزِينُهُۥ فَأُو۟لَٰٓئِكَ ٱلَّذِينَ خَسِرُوٓا۟ أَنفُسَهُم, tr:ve men haffet mevâzînuhû fe-ulâike'llezîne hasirû enfusehum, gloss:kimin tartıları hafif gelirse, işte onlar kendilerini kaybedenlerdir, source:7:9} der. Mü'minûn suresi aynı çifti verir {source:23:102} ve hafif gelenlerin {ar:فِى جَهَنَّمَ خَٰلِدُونَ, tr:fî cehenneme hâlidûn, gloss:cehennemde ebedî kalıcıdırlar, source:23:103} olduğunu ekler. Enbiyâ suresinde Allah {ar:وَنَضَعُ ٱلْمَوَٰزِينَ ٱلْقِسْطَ لِيَوْمِ ٱلْقِيَٰمَةِ, tr:ve neda'u'l-mevâzîne'l-kıst li-yevmi'l-kıyâme, gloss:kıyamet günü için adalet terazilerini kurarız, source:21:47} der ve hardal tanesi ağırlığında bir şeyi bile getireceğini söyler. Kehf suresinde, ağırlıksızlığın değersizlik olduğu açıkça söylenir: {ar:فَلَا نُقِيمُ لَهُمْ يَوْمَ ٱلْقِيَٰمَةِ وَزْنًۭا, tr:fe-lâ nukîmu lehum yevme'l-kıyâmeti veznâ, gloss:kıyamet günü onlar için hiçbir tartı kurmayız, source:18:105}. Zilzâl suresinde yer {ar:وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا, tr:ve ahraceti'l-ardu eskâlehâ, gloss:yer ağırlıklarını dışarı çıkarır, source:99:2}, ve zerre ağırlığındaki her iyilik görülür: {ar:فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ, tr:fe-men ya'mel miskâle zerratin hayran yerah, gloss:kim zerre ağırlığında bir iyilik yaparsa onu görür, source:99:7}. Hafifliğin peşe takılmak olduğunu da Kur'an sahneler: Zuhruf suresinde Firavun {ar:فَٱسْتَخَفَّ قَوْمَهُۥ فَأَطَاعُوهُ, tr:fe'stehaffe kavmehû fe-etâûh, gloss:kavmini hafife aldı, onlar da ona uydular, source:43:54}; Rûm suresinde Allah Peygambere, kesin inanmayanların onu hafifletip yerinden oynatmamasını söyler {source:30:60}.

Kaynaklar: 101:6 ثَقُلَتْ ث ق ل B001; 101:6 ثَقُلَتْ ث ق ل B002; 101:6 ثَقُلَتْ ث ق ل B004; 101:6 ثَقُلَتْ ث ق ل B005; 101:6 مَوَٰزِينُهُۥ و ز ن B001; 101:6 مَوَٰزِينُهُۥ و ز ن B002; 101:6 مَوَٰزِينُهُۥ و ز ن B003; 101:8 مَوَٰزِينُهُۥ و ز ن B007; 101:8 خَفَّتْ خ ف ف B001; 101:8 خَفَّتْ خ ف ف B003; 101:8 خَفَّتْ خ ف ف B004; 101:8 خَفَّتْ خ ف ف B005; 101:4 كَٱلْفَرَاشِ ف ر ش B005; 101:5 ٱلْمَنفُوشِ ن ف ش B002; 101:5 ٱلْجِبَالُ ج ب ل B003; 101:9 هَاوِيَةٌ ه و ي B002; 101:1 ٱلْقَارِعَةُ ق ر ع B004

## Buluşmalar

İmgelerin ilk buluşma yeri dördüncü ve beşinci ayetlerdir. Bir darbe iner ve sıkı olanı dağıtır; bu dağılmanın iki yüzü vardır. Yünün atılması bir dövmedir {source:"ن ف ش,B001"}, dolayısıyla dağların yüne dönmesi, birinci ayetin vuruşunun eseridir. Aynı kelime, menfûş, geceleyin çobansız yayılan sürüyü de anlatır {source:"ن ف ش,B003"}; dağılan dağ ile dağılan sürü tek kelimede birleşir. Dördüncü ayetin ferâşı da hem serili yeri hem saçılan sürüyü taşır; bu iki anlamı bağlayan açıklama, ferşi beşş ile anlatır {source:"ف ر ش,B004"}. Yeryüzünü döşeyen serme işi ile kıyametteki saçılma aynı iki kelimeyle söylenir.

İkinci buluşma, pervane ile terazidir. Pervane hafifliğinden ötürü bu adı almıştır ve savruk adama ferâşe denir {source:"ف ر ش,B005"}; sekizinci ayetin hafifliği de akıl savrukluğudur {source:"خ ف ف,B004"}. Dördüncü ayetin pervane insanları, sekizinci ayetin tartıları hafif gelenleridir. Bu iki imge birlikte surenin hareketini taşır: hafif olan, ışığa doğru savrulur ve ateşe düşer. Pervanenin birbiri ardınca kandile düşüşü {source:"ف ر ش,B005"} ile topluluğun birbiri ardınca çukura düşüşü {source:"ه و ي,B002"} aynı hareketi verir; dokuzuncu ayetin ümm kelimesi hedefe yönelmeyi {source:"ء م م,B012"}, on birinci ayetin ateşi de o hedefin kendisini adlandırır. Böylece dördüncü ayetteki saçılma ile on birinci ayetteki ateş, surenin iki ucunda aynı sahnenin başı ve sonudur. Hâmiye kelimesinin insanların sakındığı korunmuş şeyi anlatan kolu {source:"ح م ي,B002"}, pervanenin yaptığının tersini gösterir.

Üçüncü buluşma, ana ile çukurdur ve bu ikisi yaşayışın karşısında durur. "Anası düştü" deyimi dokuzuncu ayetin iki kelimesini birlikte taşır {source:"ه و ي,B002"}; ümm kelimesinin toplayan, kendine katan anlamı {source:"ء م م,B002"} çukuru, düşeni içine alan yer yapar. Yedinci ayetin yaşayışı ise hayattır {source:"ع ي ش,B001"}; evladını yitirmiş ananın karşısında yaşayan biri. Nâziât suresinin iki sığınağı {source:79:39} {source:79:41} bu karşıtlığı Kur'an'ın kendi sözleriyle kurar.

Dördüncü buluşma çukur ile terazi, ve çukur ile dağlar arasındadır. Hâmiye kuyunun duvarını ören ağır taşlardır {source:"ح م ي,B011"}; içine düşen ise tartısı hafif gelendir. Dağlar en ağır, en kalın kütleydi {source:"ج ب ل,B003"} ve atılmış yünün içi boşluktur {source:"ن ف ش,B002"}; hâviyenin kökü de boşluktur {source:"ه و ي,B001"}. Kazıcıyı durduran kaya {source:"ج ب ل,B005"} yok olunca, çukurun dibi de yoktur. Terazide ağırlık değerse, dağların ağırlığının yüne dönmesi, kıyamet günü dünyanın ağır saydığı şeylerin ağırlıksızlaştığını, tek ağırlığın tartının kefesinde kaldığını gösterir.

Son buluşma, kapı ile ateş arasındadır. Surenin başındaki vuruş üç kez sorulur ve bir sahneyle cevaplanır; onuncu ayetteki soru ise hemen, kızgın bir ateşle cevaplanır. Hümeze suresi aynı soru ile aynı türden cevabı verir {source:104:5} {source:104:6}. Savaş günü imgesi de bu iki ucu birleştirir: başta kılıçların çarpışması {source:"ق ر ع,B002"}, sonda topluluk içinde patlak veren düşmanlık ve kızışan öfke {source:"ن و ر,B007"} {source:"ح م ي,B003"}. Böylece sure bir kapı vuruşuyla, bir uyarıyla açılır ve bir ateşle kapanır; aradaki her kelime, o vuruşun neyi dağıttığını, neyi tarttığını ve hafif olanı nereye düşürdüğünü gösterir.

