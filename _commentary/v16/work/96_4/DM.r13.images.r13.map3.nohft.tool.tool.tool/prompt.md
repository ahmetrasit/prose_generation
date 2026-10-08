Focus: 96:4. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/96_4/D.r13/context.md =====
# 96:4 — focus

ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ

Anchor translation (canonical reading, reference only):

O, kalemle öğretendir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ٱلَّذِى | ٱلَّذِى |  | REL |
| 2 | عَلَّمَ | عَلَّمَ | ع ل م | V |
| 3 | بِٱلْقَلَمِ | قَلَم | ق ل م | P;DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 96 — full text (context; no pericope)

- 96:1 ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
- 96:2 خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
- 96:3 ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ
- 96:4 ◀ focus ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ
- 96:5 عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ
- 96:6 كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ
- 96:7 أَن رَّءَاهُ ٱسْتَغْنَىٰٓ
- 96:8 إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ
- 96:9 أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ
- 96:10 عَبْدًا إِذَا صَلَّىٰٓ
- 96:11 أَرَءَيْتَ إِن كَانَ عَلَى ٱلْهُدَىٰٓ
- 96:12 أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ
- 96:13 أَرَءَيْتَ إِن كَذَّبَ وَتَوَلَّىٰٓ
- 96:14 أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ
- 96:15 كَلَّا لَئِن لَّمْ يَنتَهِ لَنَسْفَعًۢا بِٱلنَّاصِيَةِ
- 96:16 نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ
- 96:17 فَلْيَدْعُ نَادِيَهُۥ
- 96:18 سَنَدْعُ ٱلزَّبَانِيَةَ
- 96:19 كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩


===== _commentary/v16/work/96_4/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع ل م (root_001040) — identity root of عَلَّمَ (w2)

- **B001** bilme ve gerçeğini kavrama — bilgi; bir şeyi gerçeğiyle kavrama · bir şeyi bilmek ve tanımak · haberinden haberdar olmak · bildirmek, haberdar etmek · öğretmek, öğrenmesini sağlamak · öğrenmek, kavramaya yönelmek · bilmek; buyrukta bil ki · bilgi yarışında yenmek · bilen ve bildiğine göre davranan kişi · bilgili, bilgi sahibi · çok bilgili, çok bilen · son derece bilgili kişi
  العلم نقيض الجهل (maqayis;ayn;tahdhib)؛ علمت الشيء عرفته (sihah;tahdhib)؛ إدراك الشيء بحقيقته (mufradat)؛ ما علمت بخبرك أي ما شعرت به (ayn;tahdhib)؛ أعلمته بكذا وعلمته تعليما (ayn)؛ التعليم تنبيه النفس لتصور المعاني (mufradat)؛ تعلم بمعنى اعلم (maqayis;sihah;tahdhib)؛ عالمت الرجل فعلمته (sihah;tahdhib)
- **B002** ayırt edici ve yol gösterici işaret — ayırt edici işaret · bayrak, sancak · yol gösteren belirgin dağ · kumaşın kenar işareti veya deseni · yol gösteren iz veya belirti · savaşta kendine ayırt edici işaret takmak · kumaşı işaretlemek · işaret olarak kullanılan kına · sarığı tanıtıcı bir biçimde sarmak · tanınmış ve öne çıkan kişi · son saatin yaklaştığını gösteren belirti
  أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره (maqayis)؛ العلامة وهي معروفة (maqayis)؛ العلم الراية والجمع أعلام (maqayis;sihah;tahdhib)؛ العلم الجبل الطويل والجميع الأعلام (ayn)؛ العلم الجبل (sihah;mufradat)؛ المعلم الأثر يستدل به على الطريق (sihah;tahdhib)؛ علم الثوب ورقمه في أطرافه (sihah;tahdhib;mufradat)؛ أعلم الفارس إذا كانت له علامة في الحرب (maqayis;sihah;tahdhib)؛ العلام الحناء (maqayis;sihah;tahdhib;mufradat)؛ علمت عمتي أعلمها علما (tahdhib)
- **B003** evren ve bütün yaratılmışlar — evren veya yaratılmışlar bütünü · bütün yaratıklar veya varlık sınıfları · evrenler, varlık dünyaları
  العالمون كل جنس من الخلق فهو في نفسه معلم وعلم (maqayis)؛ العالم الخلق والجمع العوالم (sihah)؛ العالمين رب الجن والإنس ورب الخلق كلهم (tahdhib)؛ العالم اسم للفلك وما يحويه وهو في الأصل اسم لما يعلم به (mufradat)؛ أصناف الخلائق (mufradat)
- **B004** üst dudak yarığı — üst dudaktaki yarık · üst dudağı yarık kişi veya deve · üst dudağını yarmak
  العلم الشق في الشفة العليا والرجل أعلم (maqayis)؛ الأعلم الذي انشقت شفته العليا (ayn)؛ علم الرجل يعلم علما إذا صار أعلم وهو المشقوق الشفة العليا (sihah)؛ علمت الرجل أعلمه علما إذا شققت شفته العليا (tahdhib)؛ البعير يقال له أعلم لعلم في مشفره الأعلى (tahdhib)؛ الشق في الشفة العليا علم (mufradat)
- **B005** deniz ya da suyu bol kuyu — deniz · suyu bol kuyu
  العيلم يقال إنه البحر ويقال إنه البئر الكثيرة الماء (maqayis)؛ العيلم الركية الكثيرة الماء (sihah)؛ العيلم البئر الكثيرة الماء (tahdhib)
- **B006** doğan veya atmaca türü yırtıcı kuş — doğan veya atmaca · çevik ve zeki adam
  العلام الصقر؛ العلامي الرجل الخفيف الذكي مأخوذ من العلام؛ العلام الباشق (tahdhib)
- **B007** erkek sırtlan — erkek sırtlan
  العيلام الذكر من الضباع (sihah)؛ العيلام الضبعان وهو ذكر الضباع (tahdhib)

## ق ل م (root_001252) — identity root of بِٱلْقَلَمِ (w3)

- **B001** sert ucu kesip yontarak düzeltme ve çıkan parça — tırnağı kesmek; sert bir şeyi yontarak düzeltmek · kesilen tırnak parçası
  تسوية شيء عند بريه وإصلاحه (maqayis)؛ قلمت الظفر وقلمته (maqayis)؛ القلامة ما يسقط من الظفر إذا قلم (maqayis)؛ القلم قطع الظفر بالقلمين وبالقلم (ayn;tahdhib)؛ قلمت ظفري وقلمت أظفاري والقلامة ما سقط منه (sihah)؛ قلمت الشيء بريته (tahdhib)؛ أصل القلم القص من الشيء الصلب كالظفر وكعب الرمح والقصب (mufradat)
- **B002** tırnağı kesilmiş gibi güçsüz [kalıp] — tırnağı kesilmiş ya da körelmiş gibi güçsüz
  يقال للضعيف هو مقلوم الأظفار (maqayis)؛ يقال للضعيف مقلوم الظفر وكليل الظفر (sihah)
- **B003** yazı yazma aracı — yazı yazma aracı · yazı araçlarını taşıyan kap
  سمي القلم قلما لأنه يقلم منه كما يقلم من الظفر (maqayis)؛ الأقلام جماعة القلم (ayn)؛ أقلامهم التي كانوا يكتبون بها التوراة (ayn)؛ القلم الذي يكتب به (sihah)؛ المقلمة وعاء الأقلام (sihah)؛ القلم الذي يكتب به وإنما سمي قلما لأنه قلم مرة بعد مرة (tahdhib)؛ خص ذلك بما يكتب به وجمعه أقلام (mufradat)
- **B004** işaretli kura çubuğu veya oku — kura için kullanılan işaretli çubuk veya ok
  شبه القدح به فقيل قلم؛ يلقون أقلامهم (maqayis)؛ القلم السهم الذي يجال به بين القوم (ayn)؛ القلم الزلم (sihah)؛ الأقلام ها هنا القداح جعلوا عليها علامات على جهة القرعة (tahdhib)؛ بالقدح الذي يضرب به وجمعه أقلام (mufradat)
- **B005** özel adlandırma kümesi — erkek devenin üreme organının çengelli ucu · erkek devenin üreme organının kılıfı · mızrağın boğumları; mızrak veya kamışın dip bölümü
  المقلم طرف قنب البعير؛ مقالم الرمح كعوبه (maqayis)؛ المقلم طرف قضيب البعير (ayn)؛ المقلم وعاء قضيب البعير؛ مقالم الرمح كعوبه (sihah)؛ المقلم طرف قضيب البعير وفي طرفه حجنة (tahdhib)؛ كعب الرمح والقصب (mufradat)
- **B006** iki ağızlı kesme aracı — iki ağızlı kesme aracı
  القلم قطع الظفر بالقلمين وبالقلم (ayn)؛ القلم الجلم (sihah)؛ يقال للمقراض المقلام والقلمان والجلمان (tahdhib)
- **B007** gövdesiz tuzcul bir bitki türü — gövdesiz tuzcul bir bitki türü
  مما شذ عن هذا الأصل القلام وهو نبت (maqayis)؛ القلام بالتشديد القاقلى وهو من الحمض (sihah)؛ القلام القاقلى؛ القلام من الحمض لا ساق له (tahdhib)
- **B008** yeryüzünün büyük coğrafi bölümlerinden biri — yeryüzünün büyük coğrafi bölümlerinden biri
  الإقليم واحد أقاليم الأرض السبعة (sihah)؛ الإقليم واحد الأقاليم وأحسبه عربيا (tahdhib)؛ سمي إقليما لأنه مقلوم من الإقليم الذي يتاخمه أي مقطوع عنه (tahdhib)؛ الإقليم واحد الأقاليم السبعة؛ الدنيا مقسومة على سبعة أسهم (mufradat)
- **B009** eşi olmayan erkek ve kadınlar; kadının uzun süre eşsiz kalması — eşi olmayan erkek ve kadınlar; kadının uzun süre eşsiz kalması
  القلمة العزاب من الرجال الواحد قالم ونساء مقلمات؛ القلم طول أيمة المرأة وامرأة مقلمة أي أيم؛ مقلمات بغير أزواج
- **B010** gözde farklı renklere bürünen yabancı kökenli dokuma — gözde farklı renklere bürünen yabancı kökenli kumaş
  أبو قلمون ضرب من ثياب الروم يتلون للعيون ألوانا

===== _commentary/v16/out/s096/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 96:4, and ## Buluşmalar) =====
## Harfleri toplamak: okuma, öğretme, kalem

Okumak, parçaları bir araya getirip bütün olarak söylemektir: {ar:قرأت الشيء قرآنا جمعته وضممت بعضه إلى بعض, tr:kara'tu'ş-şey'e kur'ânen: cemaʿtuhû ve damemtu baʿdahû ilâ baʿd, gloss:bir şeyi okudum, yani topladım ve parçalarını birbirine kattım, source:"ق ر ء,B001"}; {ar:القراءة ضم الحروف والكلمات بعضها إلى بعض, tr:el-kırâ'e: dammu'l-hurûfi ve'l-kelimât, gloss:okuma harfleri ve kelimeleri birbirine katmaktır, source:"ق ر ء,B001"}. Aynı kök, ezberden ya da sayfadan yüksek sesle söylemeyi ve başkasına okutmayı da kapsar: {ar:أقرأت غيري أقرئه إقراء, tr:akra'tu gayrî, gloss:başkasına okuttum, source:"ق ر ء,B002"}. Birinci ayetteki emir ile üçüncü ayetteki tekrarı bu toplama işini iki kez başlatır. Kurân aynı işi vahiy anında Peygamber'e anlatır: dilini acele ile oynatmamasını söyledikten sonra {ar:إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ, tr:inne ʿaleynâ cemʿahû ve kur'ânehû, gloss:onu toplamak ve okutmak bize aittir, source:75:17}, {ar:فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ, tr:fe izâ kara'nâhu fettebiʿ kur'ânehû, gloss:onu okuduğumuzda sen okunuşunu izle, source:75:18}. Toplamak ile okumak burada yan yana durur. Okutan da Allah'tır: {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:senukri'uke fe lâ tensâ, gloss:sana okutacağız, unutmayacaksın, source:87:6}. Kurân'ın parça parça okunmak üzere ayrıldığı da söylenir: {ar:وَقُرْءَانًا فَرَقْنَٰهُ لِتَقْرَأَهُۥ عَلَى ٱلنَّاسِ عَلَىٰ مُكْثٍ, tr:ve kur'ânen ferakna-hu li takra'ehû ʿale'n-nâsi ʿalâ muks, gloss:onu insanlara ağır ağır okuyasın diye bölümlere ayırdığımız bir Kurân, source:17:106}.

Dördüncü ve beşinci ayetler öğretmeyi getirir. {ar:عَلَّمَ, tr:ʿalleme, gloss:öğretti, source:96:4} zihni anlamları kavramaya uyandırmaktır: {ar:التعليم تنبيه النفس لتصور المعاني, tr:et-taʿlîm tenbîhu'n-nefsi li tasavvuri'l-meʿânî, gloss:öğretmek, nefsi anlamları kavramaya uyandırmaktır, source:"ع ل م,B001"}. Öğretme {ar:بِٱلْقَلَمِ, tr:bi'l-kalem, gloss:kalemle, source:96:4} olur: {ar:القلم الذي يكتب به, tr:el-kalemu'llezî yuktebu bih, gloss:kalem, onunla yazılan şeydir, source:"ق ل م,B003"}. Kalem, toplanıp söyleneni kalıcı kılar. Kurân kaleme yemin eder: {ar:نٓ وَٱلْقَلَمِ وَمَا يَسْطُرُونَ, tr:nûn, ve'l-kalemi ve mâ yesturûn, gloss:Nun. Kaleme ve yazdıklarına andolsun, source:68:1}. Allah'ın yazmayı öğrettiği borç sözleşmesi ayetinde de söylenir: {ar:وَلَا يَأْبَ كَاتِبٌ أَن يَكْتُبَ كَمَا عَلَّمَهُ ٱللَّهُ, tr:ve lâ ye'be kâtibun en yektube kemâ ʿallemehu'llâh, gloss:yazıcı, Allah'ın ona öğrettiği gibi yazmaktan kaçınmasın, source:2:282}. Kalemin gücü, Allah'ın sözlerinin yanında küçülür: {ar:وَلَوْ أَنَّمَا فِى ٱلْأَرْضِ مِن شَجَرَةٍ أَقْلَٰمٌ, tr:ve lev ennemâ fi'l-ardı min şeceratin aklâm, gloss:yeryüzündeki ağaçlar kalem olsa, source:31:27}, deniz mürekkep olsa bile o sözler tükenmez.

Surenin ilk beş ayetindeki sıra Kurân'da bir kez daha geçer: {ar:عَلَّمَ ٱلْقُرْءَانَ, tr:ʿallemel-kur'ân, gloss:Kurân'ı öğretti, source:55:2}, {ar:خَلَقَ ٱلْإِنسَٰنَ, tr:halaka'l-insân, gloss:insanı yarattı, source:55:3}, {ar:عَلَّمَهُ ٱلْبَيَانَ, tr:ʿallemehu'l-beyân, gloss:ona açıklamayı öğretti, source:55:4}. Öğretilen şeyin insanın bilmediği şey olduğu da söylenir: {ar:وَيُعَلِّمُكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ, tr:ve yuʿallimukum mâ lem tekûnû taʿlemûn, gloss:size bilmediğinizi öğretir, source:2:151}.

Rab kelimesinin ailesinde öğreten de vardır: {ar:الرباني… العالم المعلم الذي يغذو الناس بصغار العلوم, tr:er-rabbânî … el-ʿâlimu'l-muʿallim, gloss:rabbânî, insanları küçük bilgilerden başlayarak besleyen bilgin öğretmendir, source:"ر ب ب,B003"}. Üçüncü ayetin {ar:ٱلْأَكْرَمُ, tr:el-ekrem, gloss:en cömert, source:96:3} sıfatı da öğretme ile bağlantılıdır. Kurân bu kökü kendisi için kullanır: {ar:إِنَّهُۥ لَقُرْءَانٌ كَرِيمٌ, tr:innehû le kur'ânun kerîm, gloss:o elbette değerli bir Kurân'dır, source:56:77}; sayfaları {ar:فِى صُحُفٍ مُّكَرَّمَةٍ, tr:fî suhufin mukerrame, gloss:değerli sayfalardadır, source:80:13} ve {ar:كِرَامٍۭ بَرَرَةٍ, tr:kirâmin berara, gloss:değerli ve iyi, source:80:16} yazıcıların elindedir. Aynı köke, aldanmış insana sorulan soruda da rastlanır: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ مَا غَرَّكَ بِرَبِّكَ ٱلْكَرِيمِ, tr:yâ eyyuhe'l-insânu mâ garraka bi rabbike'l-kerîm, gloss:ey insan, seni cömert Rabbine karşı ne aldattı, source:82:6}.

Okuyucu, toplayan ve şahitlik edendir: {ar:يقرون الأشياء حتى يجمعوها علما ثم يشهدون بها, tr:yakrûne'l-eşyâ'e hattâ yecmeʿûhâ ʿilmen summe yeşhedûne bihâ, gloss:şeyleri bilgi olarak toplayana dek izlerler, sonra onlara şahitlik ederler, source:"ق ر ء,B012"}. Aynı kökte okuyucu kulluk edendir: {ar:رجل قارئ عابد ناسك, tr:raculun kâri'un ʿâbidun nâsik, gloss:okuyucu, kulluk eden, ibadet eden adam, source:"ق ر ء,B006"}. Bu, onuncu ayetteki {ar:عَبْدًا, tr:ʿabden, gloss:bir kulu, source:96:10} kelimesine ve son ayetin secdesine ulaşır. Kurân okumayı secdeyle birleştirir: inkârcılar için {ar:وَإِذَا قُرِئَ عَلَيْهِمُ ٱلْقُرْءَانُ لَا يَسْجُدُونَ, tr:ve izâ kuri'e ʿaleyhimu'l-kur'ânu lâ yescudûn, gloss:onlara Kurân okununca secde etmezler, source:84:21}; daha önce bilgi verilenler için {ar:إِذَا يُتْلَىٰ عَلَيْهِمْ يَخِرُّونَ لِلْأَذْقَانِ سُجَّدًا, tr:izâ yutlâ ʿaleyhim yahirrûne li'l-ezkâni succedâ, gloss:onlara okununca çeneleri üstüne secdeye kapanırlar, source:17:107}. Sekizinci ayetteki dönüş kelimesinin ailesinde okuyan sesin kendi üzerine dönmesi de vardır: {ar:الترجيع ترديد الصوت باللحن في القراءة, tr:et-terciʿ terdîdu's-savti bi'l-lahni fi'l-kırâ'e, gloss:tercî, okumada sesi ezgiyle tekrar tekrar döndürmektir, source:"ر ج ع,B007"}. Aynı ilk emir, hesap gününde her nefse kendi kaydı için verilir: {ar:ٱقْرَأْ كِتَٰبَكَ كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًا, tr:ikra' kitâbeke kefâ bi nefsike'l-yevme ʿaleyke hasîbâ, gloss:kitabını oku, bugün hesap sorucu olarak sana kendin yetersin, source:17:14}.

Bu sahne okumayı bir eylemler zinciri olarak gösterir: toplamak, söylemek, öğretmek, yazıyla sabitlemek ve sonunda secdeye varmak.

Kaynaklar: 96:1 ٱقْرَأْ ق ر ء B001; 96:1 ٱقْرَأْ ق ر ء B002; 96:1 ٱقْرَأْ ق ر ء B012; 96:1 ٱقْرَأْ ق ر ء B006; 96:4 عَلَّمَ ع ل م B001; 96:4 بِٱلْقَلَمِ ق ل م B003; 96:1 رَبِّكَ ر ب ب B003; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B007; 96:3 ٱلْأَكْرَمُ ك ر م B001

## Yontulan kamış, düzeltilen ok, kaygan kaya

Bu bölümdeki sahne sert malzeme üzerinde çalışan bir zanaatkârın sahnesidir. Zanaatkâr önce ölçer, sonra keser, yontar ve düzeltir. Birinci ve ikinci ayetlerdeki yaratma fiilinin kökü bu ilk adımı adlandırır: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme izâ kaddertuhû kable'l-katʿ, gloss:deriyi kesmeden önce ölçtüğümde onu "halk" ettim, source:"خ ل ق,B001"}; {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhu't-takdîru'l-mustakîm, gloss:halkın aslı doğru ölçmektir, source:"خ ل ق,B001"}. Kurân yaratmayı ölçmeyle yan yana koyar: {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe kaddarahû, gloss:onu bir damladan yarattı ve ölçüsünü verdi, source:80:19}.

Dördüncü ayetin kalemi, yontma işinden adını alır: {ar:أصل القلم القص من الشيء الصلب كالظفر وكعب الرمح والقصب, tr:aslu'l-kalemi'l-kassu mine'ş-şey'i's-sulb, gloss:kalemin aslı, tırnak, mızrak boğumu ve kamış gibi sert bir şeyden kesip almaktır, source:"ق ل م,B001"}; {ar:إنما سمي قلما لأنه قلم مرة بعد مرة, tr:innemâ summiye kalemen li ennehû kulime merraten baʿde merra, gloss:kalem denmesi, tekrar tekrar yontulduğu içindir, source:"ق ل م,B003"}. Öğreten Rab'bin aracı, defalarca yontulmuş bir kamıştır.

Yaratma kökü düzeltmeyi de adlandırır: {ar:السهم المصلح مخلق لأنه يصير أملس, tr:es-sehmu'l-muslahu muhallak, gloss:düzeltilmiş ok "muhallak"tır, çünkü pürüzsüz hale gelir, source:"خ ل ق,B008"}; {ar:المخلق القدح إذا لين, tr:el-muhallaku'l-kıdhu izâ luyyin, gloss:muhallak, yumuşatılmış kura okudur, source:"خ ل ق,B008"}. Kalem kökü de aynı nesneye varır: {ar:الأقلام ها هنا القداح جعلوا عليها علامات على جهة القرعة, tr:el-aklâmu hâhunâ el-kıdâh, gloss:buradaki kalemler, üzerine kura için işaret konmuş oklardır, source:"ق ل م,B004"}. Kurân bu nesneyi Meryem'in bakımı sahnesinde anar. Allah Peygamber'e, kendisinin orada olmadığı bir anı bildirir: {ar:إِذْ يُلْقُونَ أَقْلَٰمَهُمْ أَيُّهُمْ يَكْفُلُ مَرْيَمَ, tr:iz yulkûne aklâmehum eyyuhum yekfulu Meryem, gloss:Meryem'i hangisi üstlenecek diye kalemlerini atarlarken, source:3:44}. Cahiliye kura oklarıyla kısmet aramak ise yasaklanır: {ar:وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ ذَٰلِكُمْ فِسْقٌ, tr:ve en testaksimû bi'l-ezlâm, zâlikum fisk, gloss:fal oklarıyla pay aramanız da haram kılındı; bu yoldan çıkmaktır, source:5:3}. Bu okların toplandığı torbanın adı da rab kökündendir: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-rabâbe, gloss:rabâbe, kumar oklarının toplandığı sadağa benzer bir torbadır, source:"ر ب ب,B010"}.

Pürüzsüzleştirme sahnesinin bir de kaya hali vardır. Yaratma kökü kaygan kayayı adlandırır: {ar:صخرة خلقاء أي ملساء, tr:sahratun halkâ', gloss:halkâ kaya, yani kaygan kaya, source:"خ ل ق,B008"}. Altıncı ayetin {ar:لَيَطْغَىٰٓ, tr:le yatgâ, gloss:azar, source:96:6} fiilinin kökü de aynı kayayı adlandırır: {ar:الطغية الصفاة الملساء, tr:et-tugye es-safâtu'l-melsâ', gloss:tugye, kaygan kaya düzlüğüdür, source:"ط غ ي,B005"}. Kartalın pençesi bu kayada tutunamaz. Bu kayanın oyuklarında yağmur suyu birikir: {ar:الخليقة نقر في صخرة يجتمع فيه ماء السماء, tr:el-halîka nakrun fî sahra, gloss:halîka, kayada gök suyunun biriktiği oyuktur, source:"خ ل ق,B011"}. Böylece aynı kök hem ustaca işlenmiş nesneyi hem de üzerine tutunulamayan kayayı adlandırır. Azan insan, yontulup düzeltilmiş olduğunu unutup kendini hiçbir şeyin tutamadığı kaygan bir doruk sanır.

Kaynaklar: 96:1 خَلَقَ خ ل ق B001; 96:4 ٱلْقَلَمِ ق ل م B001; 96:4 ٱلْقَلَمِ ق ل م B003; 96:1 خَلَقَ خ ل ق B008; 96:4 ٱلْقَلَمِ ق ل م B004; 96:1 رَبِّكَ ر ب ب B010; 96:6 لَيَطْغَىٰٓ ط غ ي B005; 96:2 خَلَقَ خ ل ق B011

## Ad, iz, işaret

Bir şey, üzerine yükseltilen ya da içine bastırılan bir işaretle tanınır. Sure {ar:بِٱسْمِ, tr:bismi, gloss:adıyla, source:96:1} diye başlar. Ad kelimesinin kökü yüksekliktir: {ar:أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى, tr:aslu ismin sumuvvun ve huve mine'l-ʿuluvv, gloss:ismin aslı yükselmedir; çünkü anlamı ortaya çıkarır ve ona işaret eder, source:"س م و,B005"}. Kayıtlı bir başka türetmeye göre ise ad bir damgadır: {ar:ووسمت الشيء وسما: أثرت فيه بسمة, tr:ve vesemtu'ş-şey'e vesmen, gloss:bir şeye damga vurarak iz bıraktım, source:"و س م,B001"}. İlk anlamda ad, yükseğe kaldırılan bir işarettir; ikinci anlamda bir şeye bastırılan izdir. Kurân Rab'bin adını yükseklikle ve yaratmayla birlikte anar: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-aʿlâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1}, {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî halaka fe sevvâ, gloss:ki yarattı ve düzenledi, source:87:2}. Bu yapı surenin ilk ayetine çok yakındır. Adı anmak secdeye de bağlanır: {ar:وَٱذْكُرِ ٱسْمَ رَبِّكَ بُكْرَةً وَأَصِيلًا, tr:vezkuri'sme rabbike bukraten ve asîlâ, gloss:sabah akşam Rabbinin adını an, source:76:25}, {ar:وَمِنَ ٱلَّيْلِ فَٱسْجُدْ لَهُۥ, tr:ve mine'l-leyli fescud leh, gloss:gecenin bir kısmında O'na secde et, source:76:26}.

Öğretme kökü de işarettir: {ar:أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره, tr:aslun sahîhun vâhidun yedullu ʿalâ eserin bi'ş-şey', gloss:bir şeyi diğerlerinden ayıran bir ize delalet eden tek bir asıl, source:"ع ل م,B002"}. Bu kök sancağı ve kumaşın kenar nakışını da adlandırır: {ar:العلم الراية, tr:el-ʿalemu'r-râye, gloss:alem sancaktır, source:"ع ل م,B002"}. Görme kökü de bu sancağa varır: {ar:الراية العلامة المنصوبة للرؤية, tr:er-râyetu'l-ʿalâmetu'l-mensûbetu li'r-ru'ye, gloss:sancak, görülmek için dikilmiş işarettir, source:"ر ء ي,B011"}. On ikinci ayetteki {ar:أَمَرَ, tr:emera, gloss:emretti, source:96:12} fiilinin ailesinde yol işareti vardır: {ar:الأمارة العلامة، والأمار أمار الطريق معالمه, tr:el-emâretu'l-ʿalâme, gloss:emâre işarettir; emâr, yolun belirtileridir, source:"ء م ر,B005"}. Sekizinci ayetin dönüş kelimesinin ailesinde, yazının çizgilerinin tekrar tekrar mürekkeplenmesi bulunur: {ar:أن يعاد عليه السواد مرة بعد أخرى, tr:en yuʿâde ʿaleyhi's-sevâdu merraten baʿde uhrâ, gloss:üzerine siyahın tekrar tekrar geçirilmesi, source:"ر ج ع,B009"}.

Sure bu işaretleri yüze taşır. On beşinci ayetin {ar:لَنَسْفَعًۢا, tr:le nesfaʿan, gloss:mutlaka yakalarız, source:96:15} fiilinin ailesinde koyu bir leke vardır: {ar:السفعة بالضم سواد مشرب حمرة, tr:es-sufʿa sevâdun uşribe humra, gloss:sufʿa, kırmızıya çalan siyahlıktır, source:"س ف ع,B002"}. Son ayetin secdesinin ailesinde ise alındaki iz vardır: {ar:المسجد بالفتح جبهة الرجل حيث يصيبه ندب السجود, tr:el-mesced cebhetu'r-racul, gloss:mesced, adamın secde izinin düştüğü alnıdır, source:"س ج د,B003"}. Kurân iki tarafın da yüzüne iz koyar. Müminler için {ar:سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ, tr:sîmâhum fî vucûhihim min eseri's-sucûd, gloss:secde izinden belirtileri yüzlerindedir, source:48:29} denir. Çok yemin eden iftiracı için {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16} denir. Suçlular da yüzlerindeki işaretle tanınır: {ar:يُعْرَفُ ٱلْمُجْرِمُونَ بِسِيمَٰهُمْ فَيُؤْخَذُ بِٱلنَّوَٰصِى وَٱلْأَقْدَامِ, tr:yuʿrafu'l-mucrimûne bi sîmâhum fe yu'hazu bi'n-nevâsî ve'l-akdâm, gloss:suçlular belirtilerinden tanınır, perçemlerinden ve ayaklarından yakalanırlar, source:55:41}. Yazılı kayıt da işaretlenmiştir: {ar:كِتَٰبٌ مَّرْقُومٌ, tr:kitâbun merkûm, gloss:işaretlenmiş bir kitap, source:83:20}, {ar:يَشْهَدُهُ ٱلْمُقَرَّبُونَ, tr:yeşheduhu'l-mukarrabûn, gloss:ona yakınlaştırılanlar şahit olur, source:83:21}.

Böylece sure Rab'bin adıyla başlar, işaret koyan bir araçla öğretir ve iki işaretli alınla biter: biri yakalanıp karartılan alın, öteki secdenin iz bıraktığı alın.

Kaynaklar: 96:1 بِٱسْمِ س م و B005; 96:1 بِٱسْمِ و س م B001; 96:4 عَلَّمَ ع ل م B002; 96:7 رَّءَاهُ ر ء ي B011; 96:12 أَمَرَ ء م ر B005; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B009; 96:15 لَنَسْفَعًۢا س ف ع B002; 96:19 وَٱسْجُدْ س ج د B003

## Ölçerek yaratmak ve uydurmak

Yaratmak doğru ölçmektir. Aynı kök uydurmayı da adlandırır: {ar:الخلق خلق الكذب وهو اختلاقه واختراعه وتقديره في النفس, tr:el-halku halku'l-kezib, gloss:halk, yalanı uydurmak, icat etmek ve onu nefiste ölçüp biçmektir, source:"خ ل ق,B007"}. Bu tanım yaratma kökünü yalan köküyle birleştirir. Rab gerçeği ölçerek yaratır; yalancı ise yalanı içinde ölçüp biçer. Kurân bu anlamı İbrahim'in kavmine söylediği sözde kullanır: {ar:إِنَّمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ أَوْثَٰنًا وَتَخْلُقُونَ إِفْكًا, tr:innemâ taʿbudûne min dûni'llâhi evsânen ve tahlukûne ifkâ, gloss:siz Allah'ı bırakıp putlara tapıyor ve yalan uyduruyorsunuz, source:29:17}. Mekkeli ileri gelenler de vahyi bu kelimeyle niteler: {ar:إِنْ هَٰذَآ إِلَّا ٱخْتِلَٰقٌ, tr:in hâzâ ille'htilâk, gloss:bu bir uydurmadan başka bir şey değil, source:38:7}. Gerçek yaratıcının övgüsü de aynı kökle yapılır: {ar:فَتَبَارَكَ ٱللَّهُ أَحْسَنُ ٱلْخَٰلِقِينَ, tr:fe tebâreka'llâhu ahsenu'l-hâlikîn, gloss:yaratanların en güzeli Allah ne yücedir, source:23:14}.

On üçüncü ayetin yalanlama fiili ile on altıncı ayetin yalancı sıfatı aynı köktendir: {ar:الكذب خلاف الصدق, tr:el-kezibu hilâfu's-sidk, gloss:yalan doğruluğun zıddıdır, source:"ك ذ ب,B001"}. Kökte görünüşüyle yalan söyleyen bir kumaş da vardır: {ar:الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله, tr:el-kezzâbe sevbun yunkaşu bi levni sıbg, gloss:kezzâbe, boyayla nakışlı gibi gösterilen kumaştır; çünkü haliyle yalan söyler, source:"ك ذ ب,B009"}. Öğretme kökündeki gerçek dokuma kenarı bunun karşısında durur: {ar:علم الثوب ورقمه في أطرافه, tr:ʿalemu's-sevb, gloss:kumaşın alemi, kenarlarındaki dokuma nakışıdır, source:"ع ل م,B002"}. Kökte beklenenden önce kesilen süt de yer alır: {ar:كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم, tr:kezebe lebenu'n-nâka, gloss:devenin sütü bir süre süreceği sanıldığı halde kesildi, source:"ك ذ ب,B006"}. Görüntü ile sürekliliğin çatıştığı bir figürdür bu. Yedinci ayetin görme kökünde güzel görünüş de vardır: {ar:الرواء حسن المنظر, tr:er-ruvâ' husnu'l-manzar, gloss:ruvâ, görünüş güzelliğidir, source:"ر ء ي,B006"}.

On altıncı ayetin sıfatı kasıtlı günahı seçer: {ar:الخطأ ما لم يتعمد … الخطيئة الذنب على عمد, tr:el-hata'u mâ lem yutaʿammad … el-hatî'etu'z-zenbu ʿalâ ʿamd, gloss:hata kasıtsız olandır; hatîe kasıtlı günahtır, source:"خ ط ء,B002"}. Kurân bu kelimeyi helak edilmiş toplumlar için kullanır: {ar:وَجَآءَ فِرْعَوْنُ وَمَن قَبْلَهُۥ وَٱلْمُؤْتَفِكَٰتُ بِٱلْخَاطِئَةِ, tr:ve câ'e firʿavnu ve men kablehû ve'l-mu'tefikâtu bi'l-hâti'e, gloss:Firavun, ondan öncekiler ve altı üstüne getirilen şehirler o günahı işlediler, source:69:9}, {ar:فَأَخَذَهُمْ أَخْذَةً رَّابِيَةً, tr:fe ehazehum ahzeten râbiye, gloss:O da onları şiddetli bir yakalayışla yakaladı, source:69:10}. Günahın ardından gelen yakalama, on beşinci ayetteki perçemden yakalamayla aynı yapıdadır.

Bu sahne şunu gösterir: on altıncı ayetteki yalancı perçem, olmadığı bir şeyi iddia eden yüksek baştır, boyanmış ama dokunmamış bir kumaş gibidir. Gerçek ölçüyü yaratan Rab'bin karşısında, uydurma bir ölçüyle kendini yeterli görür.

Kaynaklar: 96:1 خَلَقَ خ ل ق B001; 96:1 خَلَقَ خ ل ق B007; 96:13 كَذَّبَ ك ذ ب B001; 96:16 كَٰذِبَةٍ ك ذ ب B009; 96:16 كَٰذِبَةٍ ك ذ ب B006; 96:4 عَلَّمَ ع ل م B002; 96:7 رَّءَاهُ ر ء ي B006; 96:16 خَاطِئَةٍ خ ط ء B002

## Buluşmalar

İmgeler en açık şekilde baş sahnesinde buluşur. On beşinci ayetin fiili hem perçemden tutmak hem de yüzü karartmaktır. Böylece başın önü, avın yakalandığı yer, huysuz hayvanın tutulduğu yer ve ateşin yaladığı deri aynı noktada birleşir. Aynı alın son ayette yere konur ve secde izini taşır. İşaret imgesi buraya da uzanır: bir alın kararmış bir lekeyle işaretlenir, öteki secdenin iziyle. Kurân her iki tarafı da yüzlerindeki işaretle tanıtır: biri {ar:مِّنْ أَثَرِ ٱلسُّجُودِ, tr:min eseri's-sucûd, gloss:secdenin izinden, source:48:29}, öteki {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. Sure ad ile başlar ve iki işaretli alınla biter.

Göz ile yeterlilik imgeleri yedinci ayette buluşur. Kendini aynada gören adam ile süse ihtiyaç duymayan güzel kadın aynı kelime çiftinde birleşir: kendini görmek ve yeterli saymak. Su imgesi de buna bağlanır. Azan insan ölçüsünü aşan bir taşkın gibidir; on beşinci ayette durması istenir. Kökün göletteki duruluşu adlandırdığı hatırlanırsa, sekizinci ayet bu suyun nereye varacağını söyler. Kurân'ın varış ayeti bu iki imgeyi aynı yapıda birleştirir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Yol imgesi de bu dönüşe katılır, çünkü dönüş başlangıca dönmektir ve bu başlangıç rahimdeki ilk tutunuştur.

Rahim ile okuma, surenin ilk kelimesinde buluşur. Okumanın kökü hem rahmin bir şeyi toplayıp tutmasını hem de harflerin toplanmasını adlandırır. Pıhtıyı tutan kökle sözü toplayan kök aynıdır. İnsanın yaratılışı ve öğretilmesi bu yüzden aynı işin iki yüzü olarak duyulur. Kurân'daki benzer sıra da bunu destekler: Kurân'ı öğretmek, insanı yaratmak ve ona açıklamayı öğretmek. Okuma ile secde de buluşur: okuyucu aynı zamanda kulluk edendir ve sure, ilk emri okumak, son emri secde etmek olan bir eğri çizer. Kurân bu ikisini, okunduğunda secde edenler ile etmeyenler üzerinden birleştirir.

Ateş ile çağrı imgeleri onuncu, on yedinci ve on sekizinci ayetlerde buluşur. Namaz hem çağrıdır hem de kökü ateşe girmeyi adlandırır. Adam meclisini çağırır, Allah ateşe iten bekçileri çağırır ve kul yakın meclise çağrılır. Ateşin kendisinin de çağırdığı söylenir: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Bu yüz çevirme on üçüncü ayetin fiilidir.

İtaat ile hayvan imgeleri son ayette buluşur. Rab, itaat edilen efendidir; dizgine uyan at da itaatin bir figürüdür. Kul bu yüzden kendini rab ilan eden birine boyun eğmez, yakında tutulan ve değer gören at gibi yaklaşır. Yaratma ile uydurma da on altıncı ayette buluşur. Gerçek ölçüyle yaratan Rab'bin karşısında, yalanı içinde ölçen yalancı perçem durur.

Bu buluşmalar surenin hareketini taşır. Sure, rahimde toplanan ve tutunan bir varlıkla başlar; bu varlık sözü toplamayı ve kalemle yazmayı öğrenir. Sonra kendini aynada yeterli görür, taşkın su gibi ölçüsünü aşar, başını kaldırır ve namaz kılan kulu engellemeye çalışır. Dönüş ayeti ve Allah'ın görmesi bu yükselişin önüne bir sınır koyar. Yasaklayan perçeminden yakalanır, meclisi yerine bekçiler gelir. Kul ise yüz çevirmeden, başını yere koyarak, çağrılmış olduğu yakınlığa yürür.

