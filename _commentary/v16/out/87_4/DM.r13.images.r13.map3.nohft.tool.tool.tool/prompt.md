Focus: 87:4. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/87_4/D.r13/context.md =====
# 87:4 — focus

وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ

Anchor translation (canonical reading, reference only):

O, otlağı ortaya çıkardı.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَٱلَّذِىٓ | ٱلَّذِى |  | CONJ;REL |
| 2 | أَخْرَجَ | أَخْرَجَ | خ ر ج | V |
| 3 | ٱلْمَرْعَىٰ | مَرْعَىٰ | ر ع ي | DET;N |


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
- 87:4 ◀ focus وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ
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
- 87:19 صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ


===== _commentary/v16/work/87_4/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## خ ر ج (root_000400) — identity root of أَخْرَجَ (w2)

- **B001** bir yerden ya da durumdan dışarı çıkma — dışarı çıktı; bir yerden veya durumdan ayrıldı · dışarı çıkma; bir durumdan ayrılma · dışarı çıkan veya ayrılan · çıkış yeri veya çıkış yönü
  النفاذ عن الشيء (maqayis)؛ الخروج نقيض الدخول (ayn;jamhara;tahdhib)؛ خرج خروجا برز من مقره أو حاله (mufradat)
- **B002** bir şeyi çıkarma, elde etme veya yetiştirme — dışarı çıkardı veya ortaya koydu · nesneleri dışarı çıkarma veya görünür kılma · çıkarıp elde etti · işleyip ortaya çıkarma veya çeşitlere ayırma · eğitim görüp yetişti · birinin elinde yetişmiş öğrenci
  اخترجت الرجل واستخرجته سواء (ayn)؛ الاستخراج كالاستنباط (sihah)؛ الإخراج أكثر ما يقال في الأعيان (mufradat)؛ خريج فلان كأنه أخرجه من حد الجهل (maqayis)
- **B003** düzenli mali yükümlülük, getiri veya gider — mali ödeme, vergi veya ürün getirisi · ürün getirisi, vergi veya zorunlu ödeme · hizmetindeki kişiyle aylık ödeme üzerinde anlaştı · efendisine düzenli ödeme yapmakla yükümlü köle · sorumluluk karşılığında elde edilen ürün getirisi
  الخراج والخرج الإتاوة لأنه مال يخرجه المعطي (maqayis)؛ الخرج والخراج ما يخرج من المال في السنة بقدر معلوم (ayn;tahdhib)؛ الخراج الغلة (tahdhib)؛ الخرج بإزاء الدخل (mufradat)
- **B004** bedende çıkan irinli şişlik veya yara — bedende çıkan şişlik, çıban veya irinli yara
  الخراج بالجسد (maqayis)؛ الخراج ورم وقرح يخرج من ذاته (ayn)؛ ما خرج على الجسد من دمل ونحوه (jamhara)؛ ما يخرج في البدن من القروح (sihah)؛ ورم وقرح يخرج بدابة أو غيرها من الحيوان (tahdhib)
- **B005** bulutun ilk kez oluşup belirmesi [kalıp] — bulut oluşmaya veya belirmeye başladı · gökyüzü bulutlandıktan sonra açıldı
  الخروج خروج السحابة (maqayis)؛ الخروج السحاب أول ما يبدأ (ayn)؛ السحاب أول ما ينشأ (sihah)؛ أول ما ينشأ السحاب فهو نشء وقد خرج له خروج حسن (tahdhib)؛ الخرج أيضا من السحاب (mufradat)
- **B006** yerleşik konumdan ayrılarak öne çıkma veya itaatten kopma — kendi değeriyle seçkinleşen kimse · soyu seçkin olmadığı halde üstün çıkan at · yöneticinin itaatinden ayrılan topluluk · birinin yeteneğinin ve iş bilirliğinin ortaya çıkması
  الخارجي الرجل المسود بنفسه من غير أن يكون له قديم (maqayis)؛ الخارجي الذي لم يكن له شرف في آبائه فيخرج ويشرف بنفسه (ayn)؛ فرس خارجي إذا خرج جوادا بين مقرفين (jamhara)؛ الخارجية من الخيل التي ليس لها عرق في الجودة فتخرج سوابق (tahdhib)؛ الخوارج خارجين عن طاعة الإمام (mufradat)
- **B007** iki renkli ya da yer yer kesintili görünüm — bir işi çeşitlendirme veya yer yer farklılaştırma · iki renkli veya kesintili görünüm · siyahı beyazından çok olan iki renkli · iki renkli dişi hayvan veya iki renkli yer · bitkisi yer yer çıkan arazi · otlağın bir bölümünü yiyip bir bölümünü bıraktı · yazı yüzeyinde bazı yerleri boş bıraktı · verimli ve verimsiz yerleri bir arada bulunan yıl
  الخرج لونان بين سواد وبياض (maqayis)؛ الأخرج لون سواده أكثر من بياضه (ayn;tahdhib)؛ أرض مخرجة نبتها في مكان دون مكان (ayn;sihah;tahdhib;mufradat)؛ خرج الغلام لوحه إذا ترك فيه مواضع لم يكتبها (tahdhib)
- **B008** erkek deve yapısında doğmuş dişi deve [kalıp] — erkek deve yapısında doğmuş dişi deve
  ناقة مخترجة إذا خرجت على خلقة الجمل (maqayis;ayn;sihah)؛ المخترجة أنها جبلت على خلقة الجمل (tahdhib)
- **B009** iki gözlü taşıma torbası — iki gözlü taşıma torbası · iki gözlü taşıma torbaları
  الخرج والخرجة جمعه جوالق ذو أونين (ayn)؛ الخرج من الأوعية معروف والجمع خرجة (sihah)؛ الخرج هذا الوعاء ثلاثة خرجة وهو جوالق ذو أونين (tahdhib)
- **B010** özel çağrılı geleneksel çocuk oyunu — erkek çocukların oynadığı geleneksel oyun · çocukların oynadığı geleneksel oyun · oyunda eldekini çıkarmayı isteyen çağrı
  الخريج لعبة لفتيان العرب يقال فيها خراج خراج (maqayis;sihah)؛ الخراج والخريج مخارجة لعبة لفتيان العرب (ayn)؛ الخراج لعبة يلعب بها الصبيان (jamhara)؛ خراج اسم لعبة لهم معروفة (tahdhib)
- **B011** uyakta bağlantı sesinden sonraki elif harfi — uyakta bağlantı sesinden sonra gelen elif harfi
  الخروج الألف التي بعد الصلة في القافية (ayn;tahdhib)
- **B012** ortak payları karşılıklı bölüşüp tasfiye etme — karşılıklı katkı ve bölüşme · ortakların veya mirasçıların paylarını tasfiye etmesi · iki ortağın mal ve alacak üzerinde karşılıklı hesaplaşması
  المخارجة المناهدة بالأصابع والتخارج التناهد (sihah)؛ يتخارج الشريكان وأهل الميراث (tahdhib)؛ لا بأس أن يتخارجا يعني العين والدين (tahdhib)
- **B013** uzun boyunlu at niteliği — uzun boynuyla dizginin erişimini aşan at
  الخروج من صفات الخيل وهو الذي يطول عنقه (tahdhib)

## ر ع ي (root_000574) — identity root of ٱلْمَرْعَىٰ (w3)

- **B001** otlama, ot ve otlak — ot, otlak ve otlama · hayvanın otlaması · hayvanlar için ot bitirmek · başka hayvanlarla birlikte otlamak
  الرَّعي الكلأ؛ المرعى الرعي والموضع والمصدر (sihah)؛ الرعي مصدر رعى يرعى رعيا الكلأ ونحوه (tahdhib)؛ الرعي ما يرعاه والمرعى موضع الرعي (mufradat)
- **B002** gözetip koruma ve yönetme — hayvanı gözetip korumak · çoban veya yönetici · yönetilen halk veya topluluk · yöneticinin halkını yönetip koruması · gözetme ve koruma; çobanlık veya yönetim · sürü veya mal yönetiminde becerikli kimse · bir şeyi birinin gözetimine vermek
  الراعي الوالي (maqayis)؛ الراعي جمعه رعاة والراعي الوالي والرعية العامة (sihah)؛ الراعي يرعى الماشية أي يحوطها ويحفظها والوالي يرعى رعيته (tahdhib)؛ جعل الرعي والرعاء للحفظ والسياسة (mufradat)
- **B003** dikkatle izleme ve gidişatı gözetme — dikkatle gözleyip izlemek · işin nereye varacağını izlemek · yıldızları gözlemek · kimsenin sözüne kulak asmamak
  رعيت الشيء رقبته ورعيته إذا لاحظته؛ راعيت الأمر نظرت إلام يصير؛ رعيت النجوم رقبتها (maqayis)؛ راعيته لاحظته؛ رعيت النجوم رقبتها (sihah)؛ المراعاة المناظرة والمراقبة (tahdhib)؛ مراعاة الإنسان للأمر مراقبته إلى ماذا يصير (mufradat)
- **B004** kulak verip dinleme — ona kulak vermek; bana kulak ver · bizi dinle, sözümüze kulak ver
  أرعيته سمعي أصغيت إليه؛ أرعني سمعك (maqayis)؛ أرعيته سمعي أي أصغيت إليه؛ راعنا من المراعاة على معنى أرعنا سمعك (sihah)؛ راعنا سمعك أي اسمع منا؛ أرعنا سمعك وراعنا سمعك بمعنى واحد (tahdhib)؛ أرعيته سمعي؛ أرعني سمعك (mufradat)
- **B005** yanlıştan dönüp vazgeçme — çirkinlikten veya bilgisizlikten dönüp vazgeçmek · işlerden el çekmek · yanlışından güzelce dönme ve vazgeçme
  الأصل الآخر ارعوى عن القبيح إذا رجع (maqayis)؛ رعا يرعو أي كف عن الأمور؛ ارعوى عن القبيح (sihah)؛ ارعوى فلان عن الجهل وهو نزوعه وحسن رجوعه (tahdhib)
- **B006** esirgeyip koruma ve sözü gözetme — onu esirgemek veya ona acımak · esirgeme ve koruyup bırakma · esirgeme; verilen sözü gözetme · hakları ve verilen sözü gözetme · bana karşı daha gözetici ve koruyucu
  الإرعاء الإبقاء (maqayis)؛ أرعيت عليه إذا أبقيت عليه وترحمته (sihah)؛ الإرعاء الإبقاء على أخيك؛ الرعوى رعاية الحفاظ للعهد (tahdhib)؛ أرع على كذا أي أبق عليه (mufradat)
- **B007** iş develeri — işte kullanılan veya yerleşim çevresinde otlayan develer
  الرعاوى والرعاوى وهي الإبل التي يعتمل عليها (maqayis)؛ الرعاوى والرعاوى الإبل التي ترعى حوالي القوم وديارهم لأنها الإبل التي يعتمل عليها (sihah)؛ الرعاوى والرعاوى جميعا الإبل التي يعتمل عليها؛ لم أسمع الرعاوي بهذا المعنى إلا ها هنا (tahdhib)

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 87:4, and ## Buluşmalar) =====
## Gökten otlağa: bulut, ilk yağmur ve kararan ot

Surenin ilk beş ayeti bir bitkinin bütün ömrünü kısa tutarak anlatır. Dördüncü ayet {ar:وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ, tr:velleẕî ahrace'l-mer'â, gloss:otlağı çıkaran O'dur, source:87:4} der, beşinci ayet ise {ar:فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ, tr:fe-ce'alehû ğuŝâen ahvâ, gloss:sonra onu kapkara bir sel döküntüsüne çevirdi, source:87:5} diye biter. İki ayet arasında otu topraktan çıkaran şeyin, yani yağmurun adı geçmez. Bu eksik halkayı surenin başka kelimelerinin aileleri tamamlar. Burada ve sonraki bölümlerde, bir kelimenin kök ailesinden gelen görüntü kelimenin kendi ayetindeki anlamının yanında duyulur, hiçbir zaman onun yerine geçmez. Birinci ayetteki "ad" yine addır, "Rab" yine Rab'dir. Aile görüntüsü, bu anlamın arkasında Arapçayı bilen kulağa ayrıca ulaşan sahnedir.

Birinci ayet {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:yüce Rabbinin adını tesbih et, source:87:1} der. "Ad" anlamındaki اسم kelimesi س م و kökündendir ve bu kök gökyüzünü de verir. Araplar için {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tusemmi's-sehâbe semâen ve'l-matara semâen, gloss:Araplar buluta da yağmura da semâ der, source:"س م و,B004"}, ve aynı ad yağmurun bitirdiği ota da verilir: {ar:يسموا النبات سماء, tr:yusemmû'n-nebâte semâen, gloss:bitkiye de semâ derler, source:"س م و,B004"}. Ölçüt basittir: {ar:السماء كل ما علاك فأظلك, tr:es-semâu kullu mâ alâke fe-ezalleke, gloss:semâ senin üstüne çıkıp sana gölge salan her şeydir, source:"س م و,B004"}. Tek bir kök böylece başın üstündeki örtüden buluta, buluttan yağmura, yağmurdan topraktan çıkan ota kadar uzanan bütün dikey sütunu kapsar. "Rab" kelimesinin ailesi bu sütunun içinde belirli bir bulutu gösterir: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb sumiye bi-ẕâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi besleyip büyüttüğü için bu adı almıştır, source:"ر ب ب,B008"}. Bu, ötekilerin altında sarkan alçak buluttur: {ar:السحاب المتعلق دون السحاب, tr:es-sehâbu'l-muteallaku dûne's-sehâb, gloss:bulutların altında asılı duran bulut, source:"ر ب ب,B008"}. Aynı kök bulutun bir yerde durup gitmemesini de söyler: {ar:أربت السحابة: دامت, tr:erabbeti's-sehâbe dâmet, gloss:bulut durdu ve sürdü, source:"ر ب ب,B007"}. Aynı kalıp güney rüzgârı için de kullanılır: {ar:أربت الجنوب والسحابة أي دامت, tr:erabbeti'l-cenûbu ve's-sehâbe ey dâmet, gloss:güney rüzgârı da bulut da sürdü, source:"ر ب ب,B007"}. Bulutu süren bu rüzgârın adı olan cenûb, on birinci ayetteki يَتَجَنَّبُهَا kelimesiyle aynı köktendir: {ar:الجنوب ريح تجيء عن يمين القبلة, tr:el-cenûbu rîhun tecîu an yemîni'l-kıble, gloss:cenûb kıblenin sağ yanından gelen rüzgârdır, source:"ج ن ب,B006"}.

Bulut ilk belirdiğinde Arapça ona dördüncü ayetin fiilinden bir ad verir: {ar:الخروج السحاب أول ما يبدأ, tr:el-hurûc es-sehâbu evvele mâ yebdeu, gloss:hurûc bulutun ilk belirişidir, source:"خ ر ج,B005"}. Bulutun kenarlarında zayıf bir şimşek çakar. Bunu anlatan fiil, yedinci ayetteki يَخْفَىٰ ile aynı köktendir: {ar:خفا البرق يخفو خفوا ويخفى خفيا إذا لمع لمعا ضعيفا معترضا في نواحى الغيم, tr:hafe'l-berku yahfû hufuvven ve yahfî hafyen iẕâ leme'a lem'an daîfen mu'teridan fî nevâhi'l-ğaym, gloss:şimşek bulutun kenarlarında yan yan zayıfça parladığında hafâ denir, source:"خ ف ي,B004"}. Bu ışığı bütün gece gözleyen kişiyi ise on yedinci ayetteki أَبْقَىٰٓ kelimesinin kökü anlatır: {ar:بات فلان يبقي البرق أي ينظر إليه من أين يلمع, tr:bâte fulânun yubkı'l-berka ey yenzuru ileyhi min eyne yelma', gloss:falanca şimşeğin nereden çakacağına bakarak geceyi geçirdi, source:"ب ق ي,B005"}. Sonunda yağmur gelir ve adını verdiği hayattan alır: {ar:يسمى المطر حيا لأن به حياة الأرض, tr:yusemme'l-mataru hayâen li-enne bihî hayâte'l-ard, gloss:yağmura hayâ denir çünkü yerin hayatı onunladır, source:"ح ي ي,B002"}. On üçüncü ayetteki يَحْيَىٰ fiili ve on altıncı ayetteki ٱلْحَيَوٰةَ kelimesi bu köktendir. Yağmur yuvalarındaki fareleri de dışarı sürer. Bu sürüş yine "gizli" kökünden bir fiille söylenir, açıklaması da dördüncü ayetin fiiliyle yapılır: {ar:وخفا المطر الفأر من حجرتهن أخرجهن, tr:ve hafe'l-mataru'l-fe'ra min hucurâtihinne ahracehunne, gloss:yağmur fareleri deliklerinden çıkardı, source:"خ ف ي,B003"}.

اسم kelimesi için Arapçada kayıtlı ikinci bir türetme vardır. Bu türetme kelimeyi "damga" anlamındaki وسم köküne bağlar. Bu, kök kimliği değil, kayıtlı bir alternatiftir. Ama bu yoldan da aynı sahneye varılır, çünkü yılın ilk yağmurunun adı bu köktendir: {ar:سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة, tr:sumiye'l-vesmiyyu mine'l-matari vesmiyyen li-ennehû yesimu'l-arda bi'n-nebâti fe-yasîru fîhâ eseran fî evveli's-sene, gloss:ilk yağmura vesmî denir çünkü yeri bitkiyle damgalar ve yılın başında yerde bir iz olur, source:"و س م,B003"}. Yağmur toprağa yeşil bir iz basar.

Dördüncü ayetin fiili أخرج, somut bir şeyin bulunduğu yerden dışarı alınmasıdır: {ar:الإخراج أكثر ما يقال في الأعيان, tr:el-ihrâcu ekŝeru mâ yukâlu fi'l-a'yân, gloss:ihrâc çoğunlukla somut şeyler için söylenir, source:"خ ر ج,B002"}. Ot gerçekten topraktan çekilip çıkarılan bir şeydir. Aynı kökün ailesi ilk çıkışın görünüşünü de verir: {ar:أرض مخرجة نبتها في مكان دون مكان, tr:ardun muhrecetun nebtuhâ fî mekânin dûne mekân, gloss:otu bir yerde bitip başka yerde bitmeyen toprak, source:"خ ر ج,B007"}. İlk yeşil, toprağa yama yama düşer. Aynı ailede bir renk adı da vardır: {ar:الأخرج لون سواده أكثر من بياضه, tr:el-ahrecu levnun sevâduhû ekŝeru min beyâdih, gloss:karası akından çok olan renk, source:"خ ر ج,B007"}. المرعى ise tek kelimede otu, otlağın yerini ve otlamanın kendisini birlikte taşır: {ar:المرعى الرعي والموضع والمصدر, tr:el-mer'â er-ra'yu ve'l-mevdiu ve'l-masdar, gloss:mer'â hem ot hem yer hem otlamadır, source:"ر ع ي,B001"}.

Beşinci ayetteki جعل, bir şeyi bir halden başka bir hale çevirmektir: {ar:جعل صير, tr:ce'ale sayyera, gloss:ce'ale bir şeyi başka bir hale soktu demektir, source:"ج ع ل,B002"}. Otun çevrildiği şey olan غثاء, otun sonunu üç adımda anlatır: ot kurur, tadını yitirir, sel onu yığıp götürür. {ar:غثا السيل المرتع إذا جمع بعضه إلى بعض وأذهب حلاوته, tr:ğaŝe's-seylu'l-merte'a iẕâ ceme'a ba'dahû ilâ ba'din ve eẕhebe halâvetehû, gloss:sel otlağı üst üste yığıp tadını giderdiğinde ğaŝâ denir, source:"غ ث و,B002"}. Ot bu noktada {ar:يابسا بعد خضرته, tr:yâbisen ba'de hudratihî, gloss:yeşilliğinden sonra kurumuş olarak, source:"غ ث و,B002"} kalır. غثاء de {ar:الغثاء ما جاء به السيل من نبات قد يبس, tr:el-ğuŝâu mâ câe bihi's-seylu min nebâtin kad yebise, gloss:ğuŝâ selin getirdiği kurumuş bitkidir, source:"غ ث و,B001"}. Ardından gelen أحوى bir renktir: {ar:الأحوى الأسود من الخضرة, tr:el-ahvâ el-esvedu mine'l-hudra, gloss:ahvâ yeşilden kararmış olandır, source:"ح و ي,B006"}. Bir deve için de {ar:بعير أحوى إذا خالط خضرته سواد وصفرة, tr:baîrun ahvâ iẕâ hâlata hudratehû sevâdun ve sufra, gloss:yeşiline kara ve sarı karışmış deveye ahvâ denir, source:"ح و ي,B006"}. Rengin adı {ar:حُوَّة, tr:huvve, gloss:yeşile çalan koyu renk, source:"memory"} kelimesidir. Ayette kelime غثاء'nın sıfatı olarak durur. Ama tanımı hem gür yeşilin koyuluğunu hem de çürüyen otun kararmasını kapsar. Bu yüzden tek kelime otun iki ucunu, taze koyuluğu ve kapkara döküntüyü yan yana tutar. Kur'an gür yeşilin koyuluğunu başka bir yerde tek kelimeyle, cennet bahçeleri için verir: {ar:مُدْهَآمَّتَانِ, tr:müdhâmmetân, gloss:yeşillikten koyu kara görünen iki bahçe, source:55:64}.

Bu sahne surenin geri kalanında karşılık bulur. On üçüncü ayetteki "yaşamak" fiilinin ailesi diri otu {ar:الحي من النبات ما كان طريا يهتز, tr:el-hayyu mine'n-nebâti mâ kâne tariyyen yehtezzu, gloss:bitkinin dirisi taze olup titreşenidir, source:"ح ي ي,B002"} diye tanımlar. "Ölmek" fiilinin ailesi de {ar:الموتان الأرض لم تحي بعد بزرع ولا إصلاح, tr:el-mevtân el-ardu lem tuhye ba'du bi-zer'in ve lâ islâh, gloss:mevtân ekinle ya da bakımla henüz diriltilmemiş topraktır, source:"م و ت,B003"}. Otun yolculuğu böylece ölü topraktan titreşen yeşile, oradan kuru döküntüye uzanır. On üçüncü ayetin ateşteki adam için söylediği şey ise bu uçlardan hiçbirinde olmamaktır. "Rab" kelimesinin ailesinde bu yolculuğun karşısında duran bir bitki adı da vardır: {ar:اسم لعدة من النبات لا تهيج في الصيف, tr:ismun li-iddetin mine'n-nebâti lâ tehîcu fi's-sayf, gloss:yazın sararıp kurumayan birkaç bitkinin adı, source:"ر ب ب,B012"}. Kur'an dünya hayatı benzetmesinde tam da bu "sararıp kurumak" fiilini kullanır. Rab adının ailesindeki sararmayan ot bu sayede otlağın kaderinin karşısına konabilir. Bu bağı dil değil, okuma kurar.

Kur'an bu yolculuğu kendi sözleriyle sahneler. Allah kendini, rüzgârları rahmetinin önünde müjdeci olarak gönderen ve ağır bulutları ölü bir beldeye süren olarak anlatır, sonra şöyle der: {ar:فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ ۚ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:fe-enzelnâ bihi'l-mâe fe-ahracnâ bihî min kulli'ŝ-ŝemerât keẕâlike nuhrici'l-mevtâ leallekum teẕekkerûn, gloss:oraya suyu indirdik ve onunla her türlü üründen çıkardık; ölüleri de böyle çıkarırız; belki düşünüp hatırlarsınız, source:7:57}. Çıkarmak fiili burada hem bitkiye hem ölülere, sonunda da hatırlamaya bağlanır. Sure de dördüncü ayetteki çıkarmadan dokuzuncu ayetteki hatırlatmaya aynı yolla uzanır. Hemen sonraki ayet, iyi toprağın bitkisini {ar:بِإِذْنِ رَبِّهِۦ, tr:bi-izni rabbih, gloss:Rabbinin izniyle, source:7:58} çıkardığını söyler. Başka bir yerde Allah gökten bereketli su indirip onunla ölü bir beldeyi dirilttiğini anlatır ve {ar:كَذَٰلِكَ ٱلْخُرُوجُ, tr:keẕâlike'l-hurûc, gloss:çıkış da böyledir, source:50:11} der. Firavun Musa'ya {ar:فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:fe-men rabbukumâ yâ mûsâ, gloss:ikinizin Rabbi kimdir ey Musa, source:20:49} diye sorduğunda Musa'nın cevabı bu surenin ilk ayetlerindeki sırayı izler: {ar:رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:rabbunelleẕî a'tâ kulle şey'in halkahû ŝumme hedâ, gloss:Rabbimiz her şeye yaratılışını veren sonra yol gösterendir, source:20:50}. Birkaç ayet sonra gökten su indirilir ve {ar:فَأَخْرَجْنَا بِهِۦٓ أَزْوَٰجًۭا مِّن نَّبَاتٍۢ شَتَّىٰ, tr:fe-ahracnâ bihî ezvâcen min nebâtin şettâ, gloss:onunla çeşit çeşit bitkiden çiftler çıkardık, source:20:53}. Surenin son ayetinde sayfaları anılan Musa, Rabbini tanıtırken aynı yaratma, yol gösterme ve çıkarma sırasını kullanır. Bir başka yerde yeryüzü için {ar:أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا, tr:ahrace minhâ mâehâ ve mer'âhâ, gloss:ondan suyunu ve otlağını çıkardı, source:79:31} denir.

Kur'an otun ikinci yarısını, yani kuruyup savrulmasını, dünya hayatının benzetmesi yapar. İki bahçe sahibinin hikâyesinden sonra Allah Peygamber'e şöyle der: {ar:وَٱضْرِبْ لَهُم مَّثَلَ ٱلْحَيَوٰةِ ٱلدُّنْيَا كَمَآءٍ أَنزَلْنَٰهُ مِنَ ٱلسَّمَآءِ, tr:vadrib lehum meŝele'l-hayâti'd-dunyâ ke-mâin enzelnâhu mine's-semâ, gloss:onlara dünya hayatının örneğini ver; gökten indirdiğimiz bir su gibidir, source:18:45}. Yerin bitkisi o suyla karışır, sonra {ar:هَشِيمًۭا تَذْرُوهُ ٱلرِّيَٰحُ, tr:heşîmen teẕrûhu'r-riyâh, gloss:rüzgârların savurduğu kuru çöp, source:18:45} olur. Hemen sonraki ayet karşı kefeyi koyar: {ar:وَٱلْبَٰقِيَٰتُ ٱلصَّٰلِحَٰتُ خَيْرٌ عِندَ رَبِّكَ ثَوَابًۭا, tr:ve'l-bâkıyâtu's-sâlihâtu hayrun inde rabbike sevâben, gloss:kalıcı iyi işler ise Rabbinin katında karşılık bakımından daha hayırlıdır, source:18:46}. Bu iki ayet, beşinci ayetteki döküntüyü on altıncı ve on yedinci ayetteki "dünya hayatı" ile "daha hayırlı ve daha kalıcı" ayrımına bağlayan köprüyü Kur'an'ın kendi ağzından kurar. Aynı benzetme başka bir yerde şu sözlerle gelir: {ar:ثُمَّ يَهِيجُ فَتَرَىٰهُ مُصْفَرًّۭا ثُمَّ يَكُونُ حُطَٰمًۭا, tr:ŝumme yehîcu fe-terâhu musferran ŝumme yekûnu hutâmâ, gloss:sonra kurur da onu sapsarı görürsün sonra çer çöp olur, source:57:20}. Bir başka yerde aynı süreç {ar:ثُمَّ يَجْعَلُهُۥ حُطَٰمًا ۚ إِنَّ فِى ذَٰلِكَ لَذِكْرَىٰ, tr:ŝumme yec'aluhû hutâmâ inne fî ẕâlike le-ẕikrâ, gloss:sonra onu çer çöpe çevirir; bunda elbette bir öğüt vardır, source:39:21} sözleriyle anlatılır. Bu cümle beşinci ayetteki "çevirdi" fiilini ve dokuzuncu ayetteki "öğüt" kelimesini bir arada tutar. Başka bir yerde yeryüzü süslenir, sahipleri ona güç yetirdiklerini sanır, sonra buyruk gelir: {ar:فَجَعَلْنَٰهَا حَصِيدًۭا كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:fe-ce'alnâhâ hasîden ke-en lem teğne bi'l-ems, gloss:onu dün hiç yokmuş gibi biçilmiş hale getirdik, source:10:24}. Kelimenin kendisi de Kur'an'da bir topluluk için kullanılır. Bir önceki kavimden sonra yaratılan bir neslin hikâyesinde, onları yakalayan çığlığın ardından şöyle denir: {ar:فَجَعَلْنَٰهُمْ غُثَآءًۭ, tr:fe-ce'alnâhum ğuŝâen, gloss:onları sel döküntüsüne çevirdik, source:23:41}. Fiil de kelime de aynıdır, ama burada ot yerine insanlar vardır.

Kaynaklar: 87:1 ٱسْمَ س م و B004; 87:1 ٱسْمَ و س م B003; 87:1 رَبِّ ر ب ب B008; 87:1 رَبِّ ر ب ب B007; 87:1 رَبِّ ر ب ب B012; 87:11 يَتَجَنَّبُهَا ج ن ب B006; 87:4 أَخْرَجَ خ ر ج B005; 87:4 أَخْرَجَ خ ر ج B002; 87:4 أَخْرَجَ خ ر ج B007; 87:4 ٱلْمَرْعَىٰ ر ع ي B001; 87:5 فَجَعَلَهُۥ ج ع ل B002; 87:5 غُثَآءً غ ث و B002; 87:5 غُثَآءً غ ث و B001; 87:5 أَحْوَىٰ ح و ي B006; 87:7 يَخْفَىٰ خ ف ي B004; 87:7 يَخْفَىٰ خ ف ي B003; 87:17 أَبْقَىٰٓ ب ق ي B005; 87:13 يَحْيَىٰ ح ي ي B002; 87:13 يَمُوتُ م و ت B003

## Sürü ve otlak: sahip, öncü, çoban

Birinci ayetle dördüncü ayet arasında üç kelime sırayla gelir: Rab, "yol gösterdi" ve otlak. Arapçada bu üç kelime bir sürü sahnesi kurar. Rab sahiptir, yönetendir, düzeltendir: {ar:رب كل شئ: مالكه, tr:rabbu kulli şey'in mâlikuhû, gloss:her şeyin rabbi onun sahibidir, source:"ر ب ب,B001"}, {ar:رببت القوم: سستهم, tr:rabebtu'l-kavme sustuhum, gloss:topluluğu yönettim, source:"ر ب ب,B001"}, {ar:ويكون الرب: المصلح, tr:ve yekûnu'r-rabbu el-muslih, gloss:rab düzeltici anlamına da gelir, source:"ر ب ب,B001"}. Develerin bağlı kaldığı yer {ar:مرب الإبل حيث لزمته, tr:merabbu'l-ibil haysu lezimethu, gloss:develerin ayrılmadığı yer, source:"ر ب ب,B007"} diye anılır. Yaban sığırı sürüsü de bu köktendir: {ar:الربرب: القطيع من بقر الوحش, tr:er-rabrab el-katîu min bakari'l-vahş, gloss:rabrab yaban sığırı sürüsüdür, source:"ر ب ب,B014"}. Üçüncü ayetin هدى fiilinin ailesinde sürünün önündekiler bulunur: {ar:هوادي الوحش متقدماتها الهادية لغيرها, tr:hevâdi'l-vahşi mutekaddimâtuhe'l-hâdiyetu li-ğayrihâ, gloss:yaban hayvanlarının hevâdîsi ötekilere yol gösteren öndekileridir, source:"ه د ي,B003"}. Dördüncü ayetin otlağının ailesinde çoban vardır: {ar:الراعي يرعى الماشية أي يحوطها ويحفظها والوالي يرعى رعيته, tr:er-râî yer'a'l-mâşiye ey yehûtuhâ ve yahfazuhâ ve'l-vâlî yer'â raiyyetehû, gloss:çoban hayvanları kuşatıp korur; yönetici de halkını böyle gözetir, source:"ر ع ي,B002"}. Aynı ailede uzağa bakan bir gözetleme de vardır: {ar:راعيت الأمر نظرت إلام يصير؛ رعيت النجوم رقبتها, tr:râaytu'l-emra nazartu ilâme yasîr raaytu'n-nucûme rakabtuhâ, gloss:işin nereye varacağına baktım; yıldızları gözledim, source:"ر ع ي,B003"}. Obanın çevresinde otlayan iş develeri de bu köktendir: {ar:الإبل التي ترعى حوالي القوم وديارهم, tr:el-ibilu'lletî ter'â havâleyi'l-kavmi ve diyârihim, gloss:topluluğun ve yurtlarının çevresinde otlayan develer, source:"ر ع ي,B007"}.

Sahnede sahip, önde giden hayvanlar ve korunan bir otlak vardır. Düz bir okuma, ilk dört ayette yalnızca birbirinin ardına dizilmiş eylemler görür. Bu sahne ise o eylemleri tek bir işin parçaları olarak gösterir: sahip olan, sürüyü otlağa götüren ve otlağı yetiştirendir. Sonra beşinci ayet otlağı döküntüye çevirir. Çobanın kelimesinin ailesindeki "işin nereye varacağına bakmak" anlamı burada işe yarar. Otlağı çıkaran, onun neye dönüşeceğini de gören konumdadır. On beşinci ayetteki رَبِّهِۦ ise kişinin bu sahibi kendi Rabbi olarak anmasıdır.

Musa'nın Firavun'a cevabında bu sahne açıkça kurulur. Bitkiler çıkarıldıktan sonra {ar:كُلُوا۟ وَٱرْعَوْا۟ أَنْعَٰمَكُمْ ۗ إِنَّ فِى ذَٰلِكَ لَءَايَٰتٍۢ لِّأُو۟لِى ٱلنُّهَىٰ, tr:kulû ver'av en'âmekum inne fî ẕâlike le-âyâtin li-uli'n-nuhâ, gloss:yiyin ve hayvanlarınızı otlatın; bunda akıl sahipleri için işaretler vardır, source:20:54} denir. Otlak kelimesi bir başka yerde de dağların yerleştirilişi yanında geçer ve bunların hepsi {ar:مَتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ, tr:metâan lekum ve li-en'âmikum, gloss:sizin ve hayvanlarınız için bir geçimlik, source:79:33} diye bağlanır. Aynı kapanış, Allah'ın insana yemeğine bakmasını söylediği yerde de gelir. Orada meyvenin yanında hayvan otu da sayılır: {ar:وَفَٰكِهَةًۭ وَأَبًّۭا, tr:ve fâkiheten ve ebbâ, gloss:meyve ve hayvan otu, source:80:31}. "Geçimlik" diye çevrilen متاع, bir süre yararlanılan şeydir. Kelime otlağın kendisinden on altıncı ayetteki dünya hayatına giden yolu sezdirir.

Kaynaklar: 87:1 رَبِّ ر ب ب B001; 87:1 رَبِّ ر ب ب B007; 87:1 رَبِّ ر ب ب B014; 87:3 فَهَدَىٰ ه د ي B003; 87:4 ٱلْمَرْعَىٰ ر ع ي B002; 87:4 ٱلْمَرْعَىٰ ر ع ي B003; 87:4 ٱلْمَرْعَىٰ ر ع ي B007

## Yarılan tarla: büyüme ve hakkı verilen ürün

On dördüncü ayet {ar:قَدْ أَفْلَحَ مَن تَزَكَّىٰ, tr:kad eflaha men tezekkâ, gloss:arınan kurtuluşa ermiştir, source:87:14} der. Ayetin iki fiilinin aileleri bir tarla sahnesi kurar. فلح toprağı yarmaktır: {ar:فلحت الأرض شققتها, tr:felahtu'l-arda şakaktuhâ, gloss:toprağı sürdüm ve yardım, source:"ف ل ح,B001"}. Toprağı süren de bu adı alır: {ar:سمي الأكار فلاحا لأنه يشق الأرض, tr:sumiye'l-ekkâru fellâhan li-ennehû yeşukku'l-ard, gloss:çiftçiye toprağı yardığı için fellâh denmiştir, source:"ف ل ح,B003"}. Kökün başarı anlamı ise kalıcılık üzerinden tanımlanır: {ar:الفلاح والفلح البقاء في الخير, tr:el-felâhu ve'l-felahu el-bekâu fi'l-hayr, gloss:felâh iyilik içinde kalmaktır, source:"ف ل ح,B005"}. {ar:الفلاح الفوز والنجاة والبقاء, tr:el-felâh el-fevzu ve'n-necâtu ve'l-bekâ, gloss:felâh kazanmak kurtulmak ve kalıcı olmaktır, source:"ف ل ح,B005"}. Bu tanım on dördüncü ayeti, on yedinci ayetteki iki kelimeye, "hayırlı" ve "kalıcı" kelimelerine bağlar. زكا ekinin büyüyüp çoğalmasıdır: {ar:زكا الزرع يزكو زكاء ازداد ونما, tr:zekâ'z-zer'u yezkû zekâen izdâde ve nemâ, gloss:ekin artıp büyüdü, source:"ز ك و,B001"}. {ar:أصل الزكاة النمو الحاصل عن بركة الله تعالى, tr:aslu'z-zekâti en-nemuvvu'l-hâsılu an bereketi'llâh, gloss:zekâtın aslı Allah'ın bereketinden gelen büyümedir, source:"ز ك و,B001"}. Aynı kök üründen verilen payı da anlatır: {ar:زكى ماله تزكية أي أدى عنه زكاته؛ وتزكى أي تصدق, tr:zekkâ mâlehû tezkiyeten ey eddâ anhu zekâtehû ve tezekkâ ey tesaddaka, gloss:malının zekâtını verdi; tezekkâ sadaka verdi demektir, source:"ز ك و,B003"}. Bu pay geri kalanı temizler: {ar:الطهارة زكاة المال؛ زكاة لأنها طهارة, tr:et-tahâretu zekâtu'l-mâl zekâtun li-ennehâ tahâra, gloss:temizlik malın zekâtıdır; temizlik olduğu için zekât denmiştir, source:"ز ك و,B002"}.

Sahnenin öbür parçaları surenin başka kelimelerindedir. Dördüncü ayetin fiili hasılatın adını verir: {ar:الخرج والخراج ما يخرج من المال في السنة بقدر معلوم, tr:el-harcu ve'l-harâcu mâ yahrucu mine'l-mâli fi's-seneti bi-kaderin ma'lûm, gloss:harâc maldan her yıl bilinen bir ölçüyle çıkandır, source:"خ ر ج,B003"}. Bu tanım üçüncü ayetin kökünü de içerir. Rab, çiftliğe bakıp onu tamamlayandır: {ar:رب فلان ضيعته إذا قام على إصلاحها, tr:rabbe fulânun day'atehû iẕâ kâme alâ islâhihâ, gloss:falanca çiftliğinin bakımını üstlendi, source:"ر ب ب,B002"}. On yedinci ayetteki "kalıcı" kelimesinin ailesinde, hasılattan geriye kalan şey vardır: {ar:الباقي حاصل الخراج ونحوه, tr:el-bâkî hâsılu'l-harâci ve nahvih, gloss:bâkî hasılattan ve benzerinden kalan miktardır, source:"ب ق ي,B002"}.

Düz bir anlatım on dördüncü ayeti "arınan kurtuldu" diye özetler. Tarla sahnesi bu cümleye bir işleyiş ekler: toprak yarılır, ekin büyür, büyüyen üründen bir pay verilir, verilen pay geri kalanı temizler, ve bu büyüme iyilik içinde kalıcı olur. Böylece tarla, beşinci ayetteki yabani otlağın karşısına geçer. Aynı toprakta biri kuruyup selle gider, öbürü işlenir, verimi alınır ve hakkı ödenir.

Kur'an bu tarlayı açıkça sahneler. Allah insandan yemeğine bakmasını ister: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:biz suyu bol bol döktük, source:80:25}, {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:ŝumme şakakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26}. Yarmak fiili tarlanın sürülmesini de verir. Başka bir yerde Allah sorar: {ar:أَفَرَءَيْتُم مَّا تَحْرُثُونَ, tr:e-fe-raeytum mâ tahruŝûn, gloss:ektiğinizi gördünüz mü, source:56:63}. Ardından {ar:لَوْ نَشَآءُ لَجَعَلْنَٰهُ حُطَٰمًۭا, tr:lev neşâu le-cealnâhu hutâmâ, gloss:dileseydik onu çer çöp yapardık, source:56:65} diye ekler. Tarla da otlağın kaderine düşebilir. Ayrım ekimin hangi tarlaya yapıldığındadır: {ar:مَن كَانَ يُرِيدُ حَرْثَ ٱلْءَاخِرَةِ نَزِدْ لَهُۥ فِى حَرْثِهِۦ ۖ وَمَن كَانَ يُرِيدُ حَرْثَ ٱلدُّنْيَا نُؤْتِهِۦ مِنْهَا وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِن نَّصِيبٍ, tr:men kâne yurîdu harŝe'l-âhireti nezid lehû fî harŝih ve men kâne yurîdu harŝe'd-dunyâ nu'tihî minhâ ve mâ lehû fi'l-âhireti min nasîb, gloss:ahiret tarlasını isteyenin tarlasını artırırız; dünya tarlasını isteyene ondan veririz ama onun ahirette payı yoktur, source:42:20}. Bu ayet, on altıncı ve on yedinci ayetteki karşıtlığı tarlanın diliyle söyler. Ürünün hakkı için {ar:وَءَاتُوا۟ حَقَّهُۥ يَوْمَ حَصَادِهِۦ, tr:ve âtû hakkahû yevme hasâdih, gloss:hasat günü hakkını verin, source:6:141} denir. Malını veren kişi için {ar:ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ, tr:elleẕî yu'tî mâlehû yetezekkâ, gloss:arınmak için malını veren, source:92:18} denir. Can üzerine yemin edilen ayetlerde iki ayrı son yan yana konur: {ar:قَدْ أَفْلَحَ مَن زَكَّىٰهَا, tr:kad eflaha men zekkâhâ, gloss:onu arıtan kurtuluşa erdi, source:91:9}, {ar:وَقَدْ خَابَ مَن دَسَّىٰهَا, tr:ve kad hâbe men dessâhâ, gloss:onu gömüp örten ise hüsrana uğradı, source:91:10}. Tarlanın dilinde arıtmanın karşıtı, tohumu toprağın altında boğmaktır. Peygamber'in arkadaşları ise bir ekine benzetilir: {ar:كَزَرْعٍ أَخْرَجَ شَطْـَٔهُۥ فَـَٔازَرَهُۥ فَٱسْتَغْلَظَ فَٱسْتَوَىٰ عَلَىٰ سُوقِهِۦ, tr:ke-zer'in ahrace şat'ehû fe-âzerahû fe'steğleza fe'stevâ alâ sûkıh, gloss:filizini çıkaran sonra onu güçlendiren sonra kalınlaşıp sapları üzerinde doğrulan bir ekin gibi, source:48:29}. Bu ayet, surenin dördüncü ayetindeki "çıkardı" fiilini ve ikinci ayetindeki "düzene koydu" fiilinin kökünü, kurumayan bir ekinde buluşturur. Bir başka yerde kurtuluşa erenler sayılırken {ar:قَدْ أَفْلَحَ ٱلْمُؤْمِنُونَ, tr:kad eflaha'l-mu'minûn, gloss:müminler kurtuluşa ermiştir, source:23:1} denir ve onlar arasında {ar:وَٱلَّذِينَ هُمْ لِلزَّكَوٰةِ فَٰعِلُونَ, tr:velleẕîne hum li'z-zekâti fâilûn, gloss:zekâtı yerine getirenler, source:23:4} anılır. Musa'nın karşısındaki sihirbazlar da sözlerini cennet bahçelerini anarak bitirir: {ar:وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:ve ẕâlike cezâu men tezekkâ, gloss:bu arınanın karşılığıdır, source:20:76}.

Kaynaklar: 87:14 أَفْلَحَ ف ل ح B001; 87:14 أَفْلَحَ ف ل ح B003; 87:14 أَفْلَحَ ف ل ح B005; 87:14 تَزَكَّىٰ ز ك و B001; 87:14 تَزَكَّىٰ ز ك و B003; 87:14 تَزَكَّىٰ ز ك و B002; 87:4 أَخْرَجَ خ ر ج B003; 87:1 رَبِّ ر ب ب B002; 87:17 أَبْقَىٰٓ ب ق ي B002

## Açık ve gizli: ses ve örtüden çıkan

Yedinci ayetin sonu {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ, tr:innehû ya'lemu'l-cehra ve mâ yahfâ, gloss:O açığa vurulanı da gizli kalanı da bilir, source:87:7} der. Bu cümle iki ayrı sahnede duyulur. Birincisi sestir. جهر sesi yükseltmektir: {ar:جهر بالقول رفع به صوته, tr:cehera bi'l-kavli rafea bihî savtah, gloss:sözü açıktan söyledi yani sesini yükseltti, source:"ج ه ر,B001"}. {ar:الجهر ضد السر, tr:el-cehru diddu's-sirr, gloss:cehr gizlinin zıddıdır, source:"ج ه ر,B001"}. Bu kök tek bir harfin söylenişine kadar iner: {ar:سمي الحرف مجهورا لأنه أشبع الاعتماد في موضعه ومنع النفس أن يجري معه, tr:sumiye'l-harfu mechûran li-ennehû eşbea'l-i'timâde fî mevdiihî ve menea'n-nefese en yecriye meah, gloss:harfe mechûr denir çünkü çıkış yerine tam dayanır ve nefesin onunla akmasını engeller, source:"ج ه ر,B011"}. خفي sesi kısmaktır: {ar:أخفيت الصوت إخفاء ... والخافية ضد العلانية ولقيته خفيا أي سرا, tr:ahfeytu's-savte ihfâen ve'l-hâfiyetu diddu'l-alâniye ve lekîtuhû hafiyyen ey sirran, gloss:sesi kıstım; hâfiye açıklığın zıddıdır; onunla gizlice karşılaştım, source:"خ ف ي,B001"}. On beşinci ayetteki anma iki yerde yaşar: {ar:ذكرته بلساني وبقلبي, tr:ẕekertuhû bi-lisânî ve bi-kalbî, gloss:onu dilimle ve kalbimle andım, source:"ذ ك ر,B004"}. Okuma da ezberden yapılır: {ar:قرأت القرآن عن ظهر قلب أو نظرت فيه, tr:kara'tu'l-kur'âne an zahri kalbin ev nazartu fîh, gloss:Kur'an'ı ezberden ya da bakarak okudum, source:"ق ر ء,B002"}. Bilmek de söylenenin farkında olmaktır: {ar:ما علمت بخبرك أي ما شعرت به, tr:mâ alimtu bi-haberike ey mâ şaartu bih, gloss:haberini bilmedim yani farkına varmadım, source:"ع ل م,B001"}. Bu sahnede yedinci ayet, altıncı ayetteki okumanın iki halini, yüksek sesle ve içten okumayı birlikte kucaklar. Okutulan söz dilde de olsa kalpte de olsa bilinir.

İkinci sahne örtüden çıkmaktır. "Gizli" kökü, Arapçada zıt anlamları birlikte taşıyan kelimelerden biridir: {ar:خفيت الشيء بغير ألف إذا أظهرته, tr:hafeytu'ş-şey'e bi-ğayri elifin iẕâ azhartah, gloss:elifsiz hafeytu bir şeyi açığa çıkardım demektir, source:"خ ف ي,B003"}. {ar:استخفيت الشئ أي استخرجته, tr:istahfeytu'ş-şey'e ey istahrectuh, gloss:bir şeyi çıkardım, source:"خ ف ي,B003"}. Bu ikinci açıklama dördüncü ayetin "çıkarmak" kökünü kullanır, ki o kökün temel anlamı şudur: {ar:خرج خروجا برز من مقره أو حاله, tr:harace hurûcen beraze min makarrihî ev hâlih, gloss:yerinden ya da halinden dışarı belirdi, source:"خ ر ج,B001"}. Örtülü olanın somut örnekleri de vardır: {ar:الخوافي سعفات يلين قلب النخلة, tr:el-havâfî saafâtun yelîne kalbe'n-nahle, gloss:havâfî hurmanın göbeğine yakın dallardır, source:"خ ف ي,B002"}. {ar:الخوافي جمع خافية وهي ما دون القوادم من الريش, tr:el-havâfî cem'u hâfiye ve hiye mâ dûne'l-kavâdimi mine'r-rîş, gloss:havâfî kanadın ön tüylerinin altında kalan tüylerdir, source:"خ ف ي,B002"}. Öbür uçta açık olan vardır: {ar:كل شيء بدا فقد جهر, tr:kullu şey'in bedâ fe-kad cehera, gloss:ortaya çıkan her şey açığa çıkmıştır, source:"ج ه ر,B002"}, ve temizlenip suyu görünen kuyu bu kökle anılır. Açıklığın bir tersi de vardır: {ar:العين الجهراء التي لا تبصر في الشمس, tr:el-aynu'l-cehrâ elletî lâ tubsiru fi'ş-şems, gloss:cehrâ göz güneşte göremeyen gözdür, source:"ج ه ر,B004"}. Fazla ışık da bir örtü olabilir. Dördüncü ayetle birlikte okununca yedinci ayetin ikilisi sabit iki durum olmaktan çıkar ve bir harekete dönüşür: yağmurla topraktan ot çıkar, deliklerden fareler çıkar. Gizli olan, Rabbin bildiği ve dilediğinde açığa çıkardığı şeydir.

Kur'an bu iki sahneyi açıkça kurar. Peygamber'e indirilen hitabın başında şöyle denir: {ar:وَإِن تَجْهَرْ بِٱلْقَوْلِ فَإِنَّهُۥ يَعْلَمُ ٱلسِّرَّ وَأَخْفَى, tr:ve in techer bi'l-kavli fe-innehû ya'lemu's-sirra ve ahfâ, gloss:sözü yüksek sesle söylesen de O gizliyi ve daha gizlisini bilir, source:20:7}. Bu, Musa'nın ateşi gördüğü sahneye geçmeden önceki ayetlerdendir. Aynı hikâyede ateşin başında {ar:إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا, tr:inne's-sâate âtiyetun ekâdu uhfîhâ, gloss:o saat gelecektir; onu neredeyse gizli tutuyorum, source:20:15} denir. Sesin ölçüsü bir emirle verilir: {ar:وَلَا تَجْهَرْ بِصَلَاتِكَ وَلَا تُخَافِتْ بِهَا وَٱبْتَغِ بَيْنَ ذَٰلِكَ سَبِيلًۭا, tr:ve lâ techer bi-salâtike ve lâ tuhâfit bihâ vebteğı beyne ẕâlike sebîlâ, gloss:namazında sesini ne yükselt ne de kıs; ikisinin arasında bir yol tut, source:17:110}. Anmanın sesi de belirlenir: {ar:وَٱذْكُر رَّبَّكَ فِى نَفْسِكَ تَضَرُّعًۭا وَخِيفَةًۭ وَدُونَ ٱلْجَهْرِ مِنَ ٱلْقَوْلِ, tr:veẕkur rabbeke fî nefsike tedarruan ve hîfeten ve dûne'l-cehri mine'l-kavl, gloss:Rabbini içinden yalvararak ve korkarak ve yüksek olmayan bir sesle an, source:7:205}. Duanın sesi de: {ar:ٱدْعُوا۟ رَبَّكُمْ تَضَرُّعًۭا وَخُفْيَةً, tr:ud'û rabbekum tedarruan ve hufye, gloss:Rabbinize yalvararak ve gizlice dua edin, source:7:55}. Allah için {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ مِنَ ٱلْقَوْلِ وَيَعْلَمُ مَا تَكْتُمُونَ, tr:innehû ya'lemu'l-cehra mine'l-kavli ve ya'lemu mâ tektumûn, gloss:O sözün açığını da bilir gizlediğinizi de bilir, source:21:110} ve {ar:يَعْلَمُ سِرَّكُمْ وَجَهْرَكُمْ, tr:ya'lemu sirrakum ve cehrakum, gloss:gizlinizi de açığınızı da bilir, source:6:3} denir. Örtüden çıkarma sahnesini ise Süleyman'a haber getiren hüdhüd anlatır. Hüdhüd bir kavmin güneşe secde ettiğini, şeytanın onları yoldan çevirdiğini söyler ve şöyle ekler: {ar:أَلَّا يَسْجُدُوا۟ لِلَّهِ ٱلَّذِى يُخْرِجُ ٱلْخَبْءَ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَيَعْلَمُ مَا تُخْفُونَ وَمَا تُعْلِنُونَ, tr:ellâ yescudû lillâhi'lleẕî yuhricu'l-hab'e fi's-semâvâti ve'l-ardi ve ya'lemu mâ tuhfûne ve mâ tu'linûn, gloss:göklerde ve yerde saklı olanı çıkaran ve gizlediğinizi de açıkladığınızı da bilen Allah'a secde etmesinler diye, source:27:25}. Bu tek ayette dördüncü ayetteki "çıkarmak" ile yedinci ayetteki gizli ve açık bir arada bulunur.

Kaynaklar: 87:7 ٱلْجَهْرَ ج ه ر B001; 87:7 ٱلْجَهْرَ ج ه ر B011; 87:7 ٱلْجَهْرَ ج ه ر B002; 87:7 ٱلْجَهْرَ ج ه ر B004; 87:7 يَخْفَىٰ خ ف ي B001; 87:7 يَخْفَىٰ خ ف ي B003; 87:7 يَخْفَىٰ خ ف ي B002; 87:15 وَذَكَرَ ذ ك ر B004; 87:6 سَنُقْرِئُكَ ق ر ء B002; 87:7 يَعْلَمُ ع ل م B001; 87:4 أَخْرَجَ خ ر ج B001

## Buluşmalar

İmgelerin çoğu, surenin son ayetinde adı geçen Musa'nın hikâyesinde buluşur. Musa uzakta bir ateş görür ve {ar:أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ecidu ale'n-nâri hudâ, gloss:ateşin başında bir yol gösteren bulurum, source:20:10} umuduyla ona yönelir. Uzaktan görülen ateşin sahnesi ile yol sahnesi burada aynı cümlededir. Ateşin başında önce seçim gelir: {ar:وَأَنَا ٱخْتَرْتُكَ, tr:ve ene'htertuk, gloss:seni ben seçtim, source:20:13}. Sonra namaz ve anma gelir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14}. Sonra gizli olan gelir: {ar:أَكَادُ أُخْفِيهَا, tr:ekâdu uhfîhâ, gloss:onu neredeyse gizli tutuyorum, source:20:15}. Başka bir anlatımda ateşin başında tesbih söylenir: {ar:وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve subhânallâhi rabbi'l-âlemîn, gloss:Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu sahnede surenin on ikinci ve on beşinci ayetleri arasındaki karşıtlık bir kişinin yolculuğunda çözülür. Aynı ateşe yaklaşan biri onun içine sokulmaz. Ateş ona yol, seçilmişlik, namaz ve anma verir. Surede bu iki son iki ayrı kişiye düşer: on ikinci ayetteki kişi ateşe girer, on beşinci ayetteki kişi namaz kılar. Kelimelerin harf benzerliği bu ayrılığı kulakta da duyurur.

İkinci büyük buluşma selin sahnesidir. Gökten inen suyun vadilerde {ar:بِقَدَرِهَا, tr:bi-kaderihâ, gloss:kendi ölçülerince, source:13:17} akması, ölçüp biçme sahnesini çağırır. Selin taşıdığı köpük, otlağın vardığı döküntüdür. İnsanların {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâr, gloss:ateşte üzerine yaktıkları şeyden, source:13:17} çıkan köpük ise ateşin sahnesine girer. Faydalı olanın yerde kalması da öğüdün ve kalıcılığın sahnesidir. Kurumuş otun tencerenin köpüğüyle aynı adı taşıması, bu iki köpüğün Arapçada zaten tek bir kelimede birleştiğini gösterir. Bu ayet surenin beşinci ayetinden on yedinci ayetine uzanan çizgiyi tek bir manzaraya sığdırır. Bir yanda giden döküntü, öbür yanda kalan fayda vardır.

Üçüncü buluşma, Musa'nın karşısındaki sihirbazların sahnesidir. Sihirbazlar secdeye kapanır. Firavun kendi azabının daha çetin ve {ar:وَأَبْقَىٰ, tr:ve ebkâ, gloss:ve daha kalıcı, source:20:71} olduğunu söyler. Sihirbazlar da onu {ar:لَن نُّؤْثِرَكَ, tr:len nu'ŝirak, gloss:seni asla tercih etmeyiz, source:20:72} diye reddeder, yalnızca {ar:هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:hâẕihi'l-hayâte'd-dunyâ, gloss:bu dünya hayatı, source:20:72} üzerinde hüküm verebileceğini söyler ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Sonra suçlu için {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:20:74} der, iman edenler için {ar:ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:ed-derecâtu'l-ulâ, gloss:en yüce dereceler, source:20:75} der, ve hepsini {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76} sözüyle bağlar. Bu birkaç ayette seçim, kalıcı hayat, yükseklik ve yarılan tarlanın kelimeleri birlikte konuşur. Firavun'un "en yüce" iddiası da başka bir anlatımda bu sahneye eklenir. Surenin ikinci yarısı, on üçüncü ayetten on yedinci ayete kadar, neredeyse kelimesi kelimesine Musa'nın hikâyesindeki bir topluluğun ağzından gelmiştir. Son ayetin Musa'nın sayfalarını anması da bu yüzden önem taşır.

Dördüncü buluşma ot ile seçimdir. Dünya hayatının kuruyan ota benzetildiği ayetin hemen ardından kalıcı iyi işlerin daha hayırlı olduğu söylenir. Dünya hayatı başka bir yerde bir {ar:زَهْرَةَ, tr:zehrate, gloss:çiçek, source:20:131} olarak anılır, ve aynı ayet {ar:خَيْرٌۭ وَأَبْقَىٰ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:20:131} diye biter. Otlağın sahnesi seçimin sahnesine bu yolla girer. Beşinci ayetteki ot ile on altıncı ayetteki tercih edilen hayat aynı nesnedir. Kalıcı olan ise ayıklanıp seçilen şeydir. Tarlanın sahnesi bu iki uç arasında bir yol açar. Kalıcı iyilik anlamına gelen kurtuluş kelimesi on dördüncü ayette, toprağı yaran çiftçinin kelimesiyle söylenir. Yabani ot kendi haline kalınca kurur ve selle gider. İşlenen toprağın ürünü ise büyür, hakkı verilir ve geriye kalan bir pay bırakır. Biri dünya tarlası, öbürü ahiret tarlasıdır.

Beşinci buluşma, yaratma fiillerinde zanaat ile bedenin birleşmesidir. İkinci ayetteki ikili hem yontulmuş oku hem de ceninin biçimlenmesini anlatır. Rahimden başlayan ayetin toprağın yağmurla titreşmesiyle bitmesi, beden ile otlağı da birbirine bağlar. Aynı aile, üçüncü ayetteki ölçmeyi pay ölçmeye de taşır, ve on altıncı ayetteki tercih bir pay seçimine döner. Değneği ateşte doğrultmanın fiili on ikinci ayetin fiilidir. Bu fiil aynı ateşin düzelten bir işi ile içine düşenin katlandığı bir işi olduğunu duyurur. Bu son bağ dilin yankısıdır, ayetin sözü değildir.

Bu buluşmalar surenin hareketini taşır. Sure tesbih emriyle ve yükseklikle açılır. Ölçen, yontan ve yol gösteren Rabbin işiyle devam eder. Yağmurun çıkardığı ve selin götürdüğü ot ile sona gelen bir ömür gösterir. Sonra sözün toplanıp unutulmamasına, sunulan öğüde ve öğüt karşısında ikiye ayrılan insanlara geçer. Biri ateşe girer ve ne ölü ne diri kalır. Öbürü arınır, Rabbinin adını anar ve namaz kılar, yani surenin başındaki emri yerine getirir. Ardından seçim gelir: yakın olan öne konmuştur, ama arkadan gelen daha hayırlı ve daha kalıcıdır. Sure, bu sözün ilk sayfalarda, ateşin başında namaz ve anma emrini alan Musa'nın ve Rabbinden kendisini puttan uzak tutmasını isteyen İbrahim'in sayfalarında yazılı olduğunu söyleyerek kapanır.

