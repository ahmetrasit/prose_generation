Focus: 102:4. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/102_4/D.r13/context.md =====
# 102:4 — focus

ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ

Anchor translation (canonical reading, reference only):

Sonra da hayır! Bileceksiniz.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ثُمَّ | ثُمّ |  | CONJ |
| 2 | كَلَّا | كَلَّا |  | AVR |
| 3 | سَوْفَ | سَوْف |  | FUT |
| 4 | تَعْلَمُونَ | عَلِمَ | ع ل م | V;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 102 — full text (context; no pericope)

- 102:1 أَلْهَىٰكُمُ ٱلتَّكَاثُرُ
- 102:2 حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ
- 102:3 كَلَّا سَوْفَ تَعْلَمُونَ
- 102:4 ◀ focus ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ
- 102:5 كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ
- 102:6 لَتَرَوُنَّ ٱلْجَحِيمَ
- 102:7 ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ
- 102:8 ثُمَّ لَتُسْـَٔلُنَّ يَوْمَئِذٍ عَنِ ٱلنَّعِيمِ


===== _commentary/v16/work/102_4/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع ل م (root_001040) — identity root of تَعْلَمُونَ (w4)

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

===== _commentary/v16/out/s102/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 102:4, and ## Buluşmalar) =====
## Sayıca üstün gelme yarışı

{ar:ٱلتَّكَاثُرُ, tr:et-tekâsür, gloss:çokluk yarışı, source:102:1} kelimesinin kalıbı karşılıklıdır: iki taraf sayılarını ve mallarını birbirine karşı koyar, ta ki biri ötekini geçene kadar. Kalıbın yarış anlamı açıkça verilir: {ar:المكاثرة والتكاثر التباري في كثرة المال والعز, tr:el-mükâseretü ve't-tekâsürü't-tebârî fî kesreti'l-mâli ve'l-izz, gloss:mükâsere ve tekâsür mal ve itibar çokluğunda yarışmaktır, source:"ك ث ر,B002"}. Yarışın bir galibi bir de yenileni vardır: {ar:كاثرناهم فكثرناهم أي غلبناهم بالكثرة, tr:kâsernâhüm fe-kesernâhüm ey galebnâhüm bi'l-kesre, gloss:onlarla sayıca yarıştık ve onları geçtik; yani çoklukla onlara üstün geldik, source:"ك ث ر,B002"}; {ar:كاثر بنو فلان بني فلان فكثروهم إذا زادوا على عددهم, tr:kâsera benû fülânin benî fülânin fe-keserûhüm izâ zâdû alâ adedihim, gloss:filan oğulları falan oğullarıyla sayıca yarıştı ve sayıları onlarınkini aşınca onları geçtiler, source:"ك ث ر,B002"}; {ar:فلان مكثور أي مغلوب في الكثرة, tr:fülânun meksûrun ey maglûbun fi'l-kesre, gloss:filan meksûrdur; yani çoklukta yenilmiştir, source:"ك ث ر,B002"}. Birinci ayetin öznesi bu yarışın kendisidir: insanları oyalayan tek başına çokluk değil, çokluğu birbirine karşı ölçmektir.

Kökün ailesinde bu yarışı savaş alanına taşıyan bir imge vardır. Kalın ve yükselen toz, çokluğu ve kabarışı yüzünden bu kökten adlandırılır: {ar:الكوثر الغبار سمي بذلك لكثرته وثورانه, tr:el-kevserü'l-gubâru sümmiye bi-zâlike li-kesretihî ve sevarânih, gloss:kevser tozdur; çokluğu ve kabarması yüzünden bu adı almıştır, source:"ك ث ر,B005"}, ve bir şiir mısraı bu tozu ölümle birleştirir: {ar:ثار نقع الموت حتى تكوثرا, tr:sâra nak'u'l-mevti hattâ tekevserâ, gloss:ölümün tozu kalktı ve kabarıp yoğunlaştı, source:"ك ث ر,B005"}. Ateşin adı da savaşa uzanır: {ar:جاحم الحرب شدة القتل في معركتها, tr:câhimü'l-harbi şiddetü'l-katli fî ma'rakatihâ, gloss:savaşın câhimi savaş alanında öldürmenin en şiddetli hâlidir, source:"ج ح م,B002"}; {ar:الموت جاحم, tr:el-mevtü câhim, gloss:ölüm alev alevdir, source:"ج ح م,B002"}. Bu anlamlar ayetlerdeki kelimelerin anlamı değildir; birinci ayetin yarışını ve altıncı ayetin ateşini, sayı yarışının bir çarpışmaya, çarpışmanın ölüme döndüğü bir resimle yan yana duyurur.

İkinci ayet yarışın ulaştığı yeri adlandırır. Arapça kullanım ikinci ayetin bütününü ölümün dolaylı bir anlatımı olarak okur: {ar:حتى زرتم المقابر كناية عن الموت, tr:hattâ zürtümü'l-mekâbira kinâyetün ani'l-mevt, gloss:"kabirleri ziyaret edinceye kadar" ölümü dolaylı olarak anlatır, source:"ق ب ر,B005"}. Kabristan da düz anlamıyla kabirlerin yeridir: {ar:المقبرة موضع القبور, tr:el-makberetü mevdiu'l-kubûr, gloss:mezarlık kabirlerin yeridir, source:"ق ب ر,B001"}, ölülerin yan yana yattığı ve sayılabildiği bir alan. Ziyaret kelimesi topluca gidenleri de tek bir bütün olarak adlandırabilir: {ar:الزور الذي يزورك واحدا كان أو جميعا, tr:ez-zevru'llezî yezûruke vâhiden kâne ev cemîâ, gloss:zevr seni ziyaret edendir; tek de olsa topluca da olsa, source:"ز و ر,B003"}. Yarışanlar kabristana bir topluluk olarak varır; sayı yarışının son alanı, sayılanların artık konuşmadığı bir alandır. Fiilin geçmiş zamanı da bu yolu tamamlanmış bir şey olarak gösterir.

Üçüncü ayetten itibaren sure başka bir yarış koyar. Bilmek fiili de aynı karşılıklı kalıba girer: {ar:عالمت الرجل فعلمته, tr:âlemtü'r-racüle fe-alemtüh, gloss:adamla bilgide yarıştım ve onu bilgide geçtim, source:"ع ل م,B001"}. Bu kalıp {ar:كاثرناهم فكثرناهم, tr:kâsernâhüm fe-kesernâhüm, gloss:onlarla sayıca yarıştık ve onları geçtik, source:"ك ث ر,B002"} ile birebir aynı yapıdadır. Surede bu biçim kullanılmaz; ama kök ailelerinin bu paralelliği, üçüncü, dördüncü ve beşinci ayetlerdeki bilmeyi birinci ayetteki sayı yarışının yerine konan bir ölçü olarak duyurur: sayıca geçmenin yerine bilgide geçilmek.

Kur'an sayı yarışını konuşan ağızlarla sahneler. İki bahçe sahibi, arkadaşıyla konuşurken der ki: {ar:أَنَا۠ أَكْثَرُ مِنكَ مَالًۭا وَأَعَزُّ نَفَرًۭا, tr:ene ekseru minke mâlen ve eazzu neferâ, gloss:ben senden malca daha çok ve adamca daha güçlüyüm, source:18:34}. Bu, mal ve itibar çokluğunda yarışmanın tam ifadesidir. Hemen ardından bahçesine girer ve onun asla yok olmayacağını sandığını söyler {source:18:35}; sonunda ürünü kuşatılır ve harcadıklarına ellerini ovuşturarak bakar {source:18:42}. Başka bir yerde Allah, her kasabaya gönderilen uyarıcıya o kasabanın refah içindekilerinin karşı çıktığını anlatır {source:34:34} ve onların sözünü aktarır: {ar:نَحْنُ أَكْثَرُ أَمْوَٰلًۭا وَأَوْلَٰدًۭا وَمَا نَحْنُ بِمُعَذَّبِينَ, tr:nahnü ekseru emvâlen ve evlâden ve mâ nahnü bi-muazzebîn, gloss:biz mal ve evlatça daha çoğuz ve biz azaba uğratılacak değiliz, source:34:35}. Çokluk burada bir güvenceye dönüşür.

Kur'an bu yarışın sonucunu bu surenin dizisine benzeyen bir dizide verir: önce görme, sonra bilme, sonra tersine dönen sayı. Allah elçiye karşı gelenler hakkında der ki: {ar:حَتَّىٰٓ إِذَا رَأَوْا۟ مَا يُوعَدُونَ فَسَيَعْلَمُونَ مَنْ أَضْعَفُ نَاصِرًۭا وَأَقَلُّ عَدَدًۭا, tr:hattâ izâ raev mâ yûadûne fe-seya'lemûne men ad'afu nâsıran ve ekallü adedâ, gloss:sonunda kendilerine vaat edileni gördüklerinde kimin yardımcısının daha zayıf ve sayısının daha az olduğunu bilecekler, source:72:24}. "-e kadar", görme, bilme ve sayı aynı cümlededir. Ayetler okunduğunda "iki topluluktan hangisinin makamı daha iyi, meclisi daha güzel" diye soran inkârcılara {source:19:73} Allah aynı yapıyla cevap verir: kendilerine vaat edileni gördüklerinde {ar:فَسَيَعْلَمُونَ مَنْ هُوَ شَرٌّۭ مَّكَانًۭا وَأَضْعَفُ جُندًۭا, tr:fe-seya'lemûne men hüve şerrun mekânen ve ad'afu cündâ, gloss:kimin yerinin daha kötü ve ordusunun daha zayıf olduğunu bilecekler, source:19:75}. Karun'un sözü aynı yarışın bilgi iddiasıdır: kendisine verileni {ar:إِنَّمَآ أُوتِيتُهُۥ عَلَىٰ عِلْمٍ عِندِىٓ, tr:innemâ ûtîtühû alâ ilmin indî, gloss:bu bana ancak bende olan bir bilgi sayesinde verildi, source:28:78} diye açıklar, ve Allah sorar: {ar:أَوَلَمْ يَعْلَمْ أَنَّ ٱللَّهَ قَدْ أَهْلَكَ مِن قَبْلِهِۦ مِنَ ٱلْقُرُونِ مَنْ هُوَ أَشَدُّ مِنْهُ قُوَّةًۭ وَأَكْثَرُ جَمْعًۭا, tr:e-ve lem ya'lem enna'llâhe kad ehleke min kablihî mine'l-kurûni men hüve eşeddü minhü kuvveten ve ekseru cem'â, gloss:bilmedi mi ki Allah ondan önce kendisinden daha güçlü ve topluluğu daha çok nesilleri helak etmişti, source:28:78}. Çokluğunu bilgiye dayandıran adama bilmediği şey hatırlatılır: daha çok olanlar da yok edilmiştir.

Savaş tozu ve kabirler de bir surede yan yana durur. Allah soluk soluğa koşan atlara yemin eder ve onların {ar:فَأَثَرْنَ بِهِۦ نَقْعًۭا, tr:fe-eserne bihî nak'â, gloss:orada toz kaldırdılar, source:100:4} diye anılan tozunu anar; birkaç ayet sonra insanın mal sevgisinde aşırı olduğunu söyler {source:100:8} ve sorar: {ar:أَفَلَا يَعْلَمُ إِذَا بُعْثِرَ مَا فِى ٱلْقُبُورِ, tr:e-felâ ya'lemu izâ bu'sira mâ fi'l-kubûr, gloss:kabirlerde olanlar dışarı saçıldığında bilmez mi, source:100:9}. Toz, mal sevgisi, kabirler ve bilme orada da bu sırayla gelir.

Bu imgenin kattığı şudur: "çokluk" yerine "çoklukta yarış" duyulduğunda ikinci ayetin kabristanı yarışın son turu, üçüncü ayetten itibaren bilme de yarışın yer değiştirmiş ölçüsü olur.

Kaynaklar: 102:1 ٱلتَّكَاثُرُ ك ث ر B002; 102:1 ٱلتَّكَاثُرُ ك ث ر B005; 102:6 ٱلْجَحِيمَ ج ح م B002; 102:2 ٱلْمَقَابِرَ ق ب ر B005; 102:2 ٱلْمَقَابِرَ ق ب ر B001; 102:2 زُرْتُمُ ز و ر B003; 102:3 تَعْلَمُونَ ع ل م B001; 102:4 تَعْلَمُونَ ع ل م B001; 102:5 عِلْمَ ع ل م B001

## İzden şeyin kendisine

Surenin ortası bir merdiven gibi yükselir: {ar:كَلَّا سَوْفَ تَعْلَمُونَ, tr:kellâ sevfe ta'lemûn, gloss:hayır; yakında bileceksiniz, source:102:3}; {ar:ثُمَّ كَلَّا سَوْفَ تَعْلَمُونَ, tr:sümme kellâ sevfe ta'lemûn, gloss:sonra hayır; yakında bileceksiniz, source:102:4}; {ar:كَلَّا لَوْ تَعْلَمُونَ عِلْمَ ٱلْيَقِينِ, tr:kellâ lev ta'lemûne ilme'l-yakîn, gloss:hayır; kesin bilgiyle bilseydiniz, source:102:5}; {ar:لَتَرَوُنَّ ٱلْجَحِيمَ, tr:leteravünne'l-cahîm, gloss:cehennemi mutlaka göreceksiniz, source:102:6}; {ar:ثُمَّ لَتَرَوُنَّهَا عَيْنَ ٱلْيَقِينِ, tr:sümme leteravünnehâ ayne'l-yakîn, gloss:sonra onu kesinliğin gözüyle mutlaka göreceksiniz, source:102:7}. Kelimelerin aileleri bu merdivenin basamaklarını tek tek adlandırır.

Bilmek kökünün ilk anlamı bir izdir: bir şeyin üstünde taşıdığı ve onu başkasından ayıran işaret, {ar:أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره, tr:aslun sahîhun vâhidun yedüllü alâ eserin bi'ş-şey'i yetemeyyezü bihî an gayrih, gloss:bir şeydeki ve onu başkasından ayıran bir izi gösteren tek sağlam kök, source:"ع ل م,B002"}, ve kendisinden yolun çıkarıldığı yol işareti, {ar:المعلم الأثر يستدل به على الطريق, tr:el-ma'lemü'l-eserü yüstedellü bihî ale't-tarîk, gloss:ma'lem yola delil tutulan izdir, source:"ع ل م,B002"}. Bilmenin bir hâli de haberle bilmektir: {ar:ما علمت بخبرك أي ما شعرت به, tr:mâ alimtü bi-haberike ey mâ şeartü bih, gloss:haberini bilmedim; yani ondan haberim olmadı, source:"ع ل م,B001"}. Üçüncü ve dördüncü ayetlerdeki "bileceksiniz" bu ilk basamaktadır: bir haber duyulur, bir iz gösterilir. Basamak iki kez söylenir ve araya {ar:ثُمَّ, tr:sümme, gloss:sonra, source:102:4} girer; tekrar, aynı yerde durmak değil bir sonraki adıma geçmektir.

Beşinci ayet bilgiyi şeyin hakikatine bağlar. Bilgi {ar:إدراك الشيء بحقيقته, tr:idrâkü'ş-şey'i bi-hakîkatih, gloss:şeyi hakikatiyle kavramak, source:"ع ل م,B001"}, yakîn ise şüphesi giderilmiş bilgidir: {ar:اليقين العلم وزوال الشك, tr:el-yakînü'l-ilmü ve zevâlü'ş-şekk, gloss:yakîn bilgidir ve şüphenin kalkmasıdır, source:"ي ق ن,B001"}. Kulağın da bir yakîni vardır: {ar:رجل أذن يقن وهو الذي لا يسمع بشيء إلا أيقن به, tr:racülün ezenün yekanün ve hüve'llezî lâ yesmeu bi-şey'in illâ eykane bih, gloss:kulağı kesin adam; bir şey duyduğunda ona kesin inanan, source:"ي ق ن,B001"}. Sure dinleyicisine görmeden önce bu kulak basamağını sunar: beşinci ayet {ar:لَوْ, tr:lev, gloss:eğer -seydi, source:102:5} ile kurulmuştur, "kesin bilgiyle bilseydiniz". Duyduğu şeye kesin inanan kulak, görmeye gerek kalmadan bilir; ayetin dilek kipi, bu basamağın henüz kullanılabilir olduğunu gösterir.

Altıncı ayette görme gelir. Görme gözle de iç görüyle de olur: {ar:نظر وإبصار بعين أو بصيرة, tr:nazarun ve ibsârun bi-aynin ev basîra, gloss:gözle ya da basiretle bakmak ve görmek, source:"ر ء ي,B001"}; {ar:الرؤية إدراك المرئي بالحاسة, tr:er-ru'yetü idrâkü'l-mer'iyyi bi'l-hâsse, gloss:görme görüleni duyuyla kavramaktır, source:"ر ء ي,B001"}. Bu ikinci açıklamadaki "kavramak", bilginin açıklamasındaki kelimeyle aynıdır: görmek de bir kavrayıştır, ama duyuyla. Görmek fiili kalbin görmesi olarak bilmek anlamına da gelir: {ar:الرأي رأي القلب, tr:er-ra'yü ra'yü'l-kalb, gloss:re'y kalbin görmesidir, source:"ر ء ي,B002"}; {ar:بمعنى العلم تتعدى إلى مفعولين, tr:bi-ma'na'l-ilmi teteaddâ ilâ mef'ûleyn, gloss:bilmek anlamında iki nesne alır, source:"ر ء ي,B002"}. Bu yüzden altıncı ayetin "göreceksiniz"i, "bileceksiniz"in bir sonraki basamağı olarak duyulur. Görme başka birinin göstermesiyle de olur: {ar:أريته الشيء فرآه, tr:ereytühü'ş-şey'e fe-raâh, gloss:ona şeyi gösterdim ve o gördü, source:"ر ء ي,B012"}; görmenin ardında bir gösteren vardır.

Yedinci ayet merdivenin tepesidir. {ar:رأيت بعيني رؤية ورأيته رأي العين, tr:raeytü bi-aynî ru'yeten ve raeytühû ra'ye'l-ayn, gloss:kendi gözümle gördüm; onu göz görüşüyle gördüm, source:"ر ء ي,B001"} ifadesi yedinci ayetin fiilini ve ismini tam bu sırayla birleştirir. Gözle görmek aracısız görmektir: {ar:رأيت الشيء عيانا أي معاينة, tr:raeytü'ş-şey'e ıyânen ey muâyeneten, gloss:şeyi gözle gördüm; yani bizzat, source:"ع ي ن,B002"}, ve göz görünce iz aranmaz: {ar:لا أطلب أثرا بعد عين أي بعد معاينة, tr:lâ atlubu eseran ba'de aynin ey ba'de muâyene, gloss:gözle gördükten sonra iz aramam, source:"ع ي ن,B002"}. Bu deyim merdivenin başını ve sonunu birleştirir: bilgi bir iz olarak başlamıştı; göz gelince iz gereksiz kalır. Göz kelimesinin bir anlamı da şeyin kendisidir: {ar:عين الشيء نفسه, tr:aynü'ş-şey'i nefsüh, gloss:şeyin ayn'ı onun kendisidir, source:"ع ي ن,B013"}; {ar:خذ درهمك بعينه, tr:huz dirhemeke bi-aynih, gloss:dirhemini aynen al, source:"ع ي ن,B013"}. {ar:عَيْنَ ٱلْيَقِينِ, tr:ayne'l-yakîn, gloss:kesinliğin gözü; kesinliğin kendisi, source:102:7} böylece iki şekilde duyulur: kesinliğe gözle varmak ve kesinliğin bizzat kendisi; yerine konan bir şey değil, kendisi.

Kur'an aynı merdivenin parçalarını başka yerlerde kurar. Büyük haber hakkında tartışanlar için Allah aynı ikili yapıyı kullanır: {ar:كَلَّا سَيَعْلَمُونَ, tr:kellâ seya'lemûn, gloss:hayır; bilecekler, source:78:4} {ar:ثُمَّ كَلَّا سَيَعْلَمُونَ, tr:sümme kellâ seya'lemûn, gloss:sonra hayır; bilecekler, source:78:5}. Haberin bir yerleşme zamanı olduğunu da söyler: {ar:لِّكُلِّ نَبَإٍۢ مُّسْتَقَرٌّۭ ۚ وَسَوْفَ تَعْلَمُونَ, tr:li-külli nebein müstekarrun ve sevfe ta'lemûn, gloss:her haberin bir yerleşme zamanı vardır; yakında bileceksiniz, source:6:67}; haber bilgi olarak yerine oturur. Bir üst basamağın adı da Kur'an'da geçer: ölüm sahnesi {ar:إِنَّ هَٰذَا لَهُوَ حَقُّ ٱلْيَقِينِ, tr:inne hâzâ le-hüve hakku'l-yakîn, gloss:işte bu kesin bilginin ta kendisidir, source:56:95} ile kapanır, ve Kur'an kendisini de {ar:وَإِنَّهُۥ لَحَقُّ ٱلْيَقِينِ, tr:ve innehû le-hakku'l-yakîn, gloss:ve o elbette kesin bilginin hakkıdır, source:69:51} diye anar.

Kur'an ölümün kendisini de yakîn diye adlandırır. Allah Peygamber'e {ar:وَٱعْبُدْ رَبَّكَ حَتَّىٰ يَأْتِيَكَ ٱلْيَقِينُ, tr:va'bud rabbeke hattâ ye'tiyeke'l-yakîn, gloss:sana yakîn gelinceye kadar Rabbine ibadet et, source:15:99} der; cehennemdekiler de kendilerini oraya neyin soktuğu sorulduğunda {source:74:42} sözlerini şöyle bitirirler: {ar:حَتَّىٰٓ أَتَىٰنَا ٱلْيَقِينُ, tr:hattâ etâne'l-yakîn, gloss:sonunda bize yakîn geldi, source:74:47}. İki ayette de "-e kadar" ölüme varır ve ölümün adı yakîndir. İkinci ayetin {ar:حَتَّىٰ زُرْتُمُ ٱلْمَقَابِرَ, tr:hattâ zürtümü'l-mekâbir, gloss:ta kabirleri ziyaret edinceye kadar, source:102:2} ifadesi bu ayetlerin yanında beşinci ve yedinci ayetlerin yakînine bağlanır: kabirlere varış, kesin bilginin de geldiği yerdir.

İbrahim'in sahnesi gösterilmenin kesinliğe götürdüğünü anlatır: {ar:وَكَذَٰلِكَ نُرِىٓ إِبْرَٰهِيمَ مَلَكُوتَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَلِيَكُونَ مِنَ ٱلْمُوقِنِينَ, tr:ve kezâlike nürî İbrâhîme melekûte's-semâvâti ve'l-ardı ve li-yekûne mine'l-mûkınîn, gloss:böylece İbrahim'e göklerin ve yerin melekûtunu gösteriyorduk; kesin bilenlerden olsun diye, source:6:75}. Başka bir sahnede İbrahim Rabbinden ölüleri nasıl dirilttiğini kendisine göstermesini ister; Allah "İnanmadın mı" diye sorunca {ar:بَلَىٰ وَلَٰكِن لِّيَطْمَئِنَّ قَلْبِى, tr:belâ ve lâkin li-yatmeinne kalbî, gloss:evet; ama kalbim yatışsın diye, source:2:260} der. Bilmenin üstünde bir görme basamağı vardır ve konusu ölülerdir. Ama Kur'an aynı görmenin geç kaldığı sahneleri de gösterir: suçlular Rablerinin huzurunda başları eğik {ar:رَبَّنَآ أَبْصَرْنَا وَسَمِعْنَا فَٱرْجِعْنَا نَعْمَلْ صَٰلِحًا إِنَّا مُوقِنُونَ, tr:rabbenâ ebsarnâ ve semi'nâ fe'rci'nâ na'mel sâlihan innâ mûkınûn, gloss:Rabbimiz; gördük ve işittik; bizi geri döndür de iyi iş yapalım; artık kesin inanıyoruz, source:32:12} derler. Ateşin başında durdurulduklarında {ar:وَلَوْ تَرَىٰٓ إِذْ وُقِفُوا۟ عَلَى ٱلنَّارِ فَقَالُوا۟ يَٰلَيْتَنَا نُرَدُّ, tr:ve lev terâ iz vükıfû ale'n-nâri fe-kâlû yâ leytenâ nüraddü, gloss:onları ateşin başında durdurulduklarında bir görsen; "Keşke geri döndürülsek" derler, source:6:27}, ve Allah ekler: {ar:بَلْ بَدَا لَهُم مَّا كَانُوا۟ يُخْفُونَ مِن قَبْلُ, tr:bel bedâ lehüm mâ kânû yuhfûne min kabl, gloss:hayır; daha önce gizledikleri şey onlara göründü, source:6:28}. Göz yakîni ancak geri dönüş kapandığında gelir. Suçluların ateşi görüp yine de {ar:فَظَنُّوٓا۟ أَنَّهُم مُّوَاقِعُوهَا, tr:fe-zannû ennehüm müvâkıûhâ, gloss:ona düşeceklerini sandılar, source:18:53} denmesi, görmenin ilk anında bile dilin henüz zan dili olduğunu gösterir; yedinci ayetin "kesinliğin gözü" bu zannın da bittiği yerdir. Allah'ın {ar:سَنُرِيهِمْ ءَايَٰتِنَا فِى ٱلْءَافَاقِ وَفِىٓ أَنفُسِهِمْ حَتَّىٰ يَتَبَيَّنَ لَهُمْ أَنَّهُ ٱلْحَقُّ, tr:senürîhim âyâtinâ fi'l-âfâkı ve fî enfüsihim hattâ yetebeyyene lehüm ennehü'l-hakk, gloss:ayetlerimizi onlara ufuklarda ve kendi içlerinde göstereceğiz; ta ki onun hak olduğu kendilerine açıkça belli olana kadar, source:41:53} vaadi aynı merdiveni dünyada kurar: gösterme, belirginleşene kadar sürer. Kıyamet anlatılırken de {ar:وَإِذَا ٱلْجَحِيمُ سُعِّرَتْ, tr:ve ize'l-cahîmü suıırat, gloss:cehennem alevlendirildiğinde, source:81:12} anından sonra {ar:عَلِمَتْ نَفْسٌۭ مَّآ أَحْضَرَتْ, tr:alimet nefsün mâ ahdarat, gloss:her can ne hazırladığını bilir, source:81:14} gelir: cehennem görünür ve bilgi gelir.

Bu imgenin kattığı, surenin ortasındaki tekrarların bir yükseliş olduğudur. Sade bir özet "bileceksiniz, göreceksiniz" deyip geçer; ama bilginin izden başlayıp gözde bittiği duyulduğunda her ayet bir öncekinden daha yakın bir bilmeyi anlatır, ve en sonunda iz aranmayan, şeyin kendisinin görüldüğü yere varılır.

Kaynaklar: 102:3 تَعْلَمُونَ ع ل م B002; 102:3 تَعْلَمُونَ ع ل م B001; 102:4 تَعْلَمُونَ ع ل م B001; 102:5 عِلْمَ ع ل م B001; 102:5 ٱلْيَقِينِ ي ق ن B001; 102:7 ٱلْيَقِينِ ي ق ن B001; 102:6 لَتَرَوُنَّ ر ء ي B002; 102:6 لَتَرَوُنَّ ر ء ي B001; 102:6 لَتَرَوُنَّ ر ء ي B012; 102:7 لَتَرَوُنَّهَا ر ء ي B001; 102:7 عَيْنَ ع ي ن B002; 102:7 عَيْنَ ع ي ن B013

## Buluşmalar

Birkaç Kur'an sahnesi bu imgelerden ikisini ya da daha fazlasını aynı anda taşır. Atların kaldırdığı tozla açılan ve mal sevgisinden kabirlere ve göğüslere uzanan sahne {source:100:10} sayı yarışını, gömülü olanın açılışını ve bilme merdivenini birlikte tutar: toz savaşın, saçılan kabirler ve ortaya dökülen göğüsler örtünün, "bilmez mi" sorusu da izden şeyin kendisine yükselen bilginin sahnesidir; ve hepsi "o gün" Rablerinin onlardan haberdar olmasıyla kapanır {source:100:11}. Ölüm anının sahnesi {source:56:95} ziyaretin konaklarını, serinlik ile sıcaklığı ve bilmenin üst basamağını bir arada tutar: nimet cenneti ve cehennem birer ağırlama olarak sunulur, ve hepsine kesin bilginin hakkı denir. Cennet halkından birinin cehennemin ortasındaki arkadaşını gördüğü sahne {source:37:55} göz imgesini sorgu imgesiyle birleştirir: sahne karşılıklı bir soruşmayla açılır {source:37:50}, cehennem nimetin içinden görülür, ve konuşan kurtuluşunu nimetin adıyla anar {source:37:57}. Mal toplayıp sayanın Hutame'ye atıldığı sahne {source:104:4} değirmen ağzını sayı yarışıyla birleştirir: sayılan yığın, kırıp parçalayan bir ateşe döner. Cehennemdekilere "sizi Sekar'a ne soktu" diye sorulan sahne {source:74:47} sorguyu bilme merdiveniyle birleştirir: sorguya verilen cevap ölümün adını yakîn koyar. Cehennemin kâfirlere sunulduğu sahne {source:18:101} göz imgesini oyalanmayla birleştirir: anmaya karşı örtülü gözler, o gün sunulanı görür. Ve cehennemin getirildiği gün {source:89:23} oyalanmayı hesapla birleştirir: oyalanmanın düşürdüğü anma, nimetin ve mal sevgisinin hesabıyla birlikte geri gelir.

Kelimelerin kendisinde de buluşmalar vardır. Oyalanmayı anlatan "meşgul etmek" fiili değirmenin yemini de anlatır; yüz çevirten oyalanma ile doymayan değirmen tek bir kelimenin iki yüzüdür, ve aynı kelimenin ailesi bağışı da adlandırdığı için değirmene atılan avuç, sonunda hakkında sorulacak bir armağandır. Yedinci ayetin göz kelimesi aynı anda yüz yüze gelmeyi, merdivenin tepesini, sayılan altını, akan pınarı ve peşin ödemeyi adlandırır; bu yüzden yedinci ayet imgelerin çoğunun düğümlendiği yerdir. Sekizinci ayetin nimet kelimesi sayılan develeri, varılıp kalınan yurdu, nemli rüzgârı, gözün serinliğini ve bir verenin bağışını taşır; sorgunun konusu birinci ayetin sayılan nesneleridir. Altıncı ayetin cehennemi çukurdaki doymayan ateş, savaşın en sıcak anı, alev alev bakan göz ve çok sıcak bir varış yeridir. İkinci ayetin iki kelimesi ise yol ile örtüyü birleştirir: ziyaret fiili sapmayı, ziyareti ve göğsü, kabir kelimesi konağı ve örtüyü taşır.

Bu buluşmalar surenin hareketini taşır. Birinci ayette insan bir şeyle tutulur, yüzünü kendisini ilgilendirenden çevirir, çokluğunu başkalarına karşı sayar ve gösterir; değirmen beslendikçe döner. İkinci ayette bu yol kabirlerde biter, ama kabir bir ziyarettir ve bir örtüdür: geçilen bir konak ve içindekini bir gün gösterecek bir kın. Üçüncü ayetten yedinci ayete kadar bilgi izden kesinliğe, kesinlikten göze yükselir; bu yükselişte gösteren seyirci olur, yüz çeviren yüz yüze getirilir, örtü kalkar ve görülen ateş de geri bakar. Sekizinci ayette sayılan şeyler bir verenin bağışı ve ateşin karşısındaki serinlik olarak adlandırılır, ve sayan, sorulan olur.

