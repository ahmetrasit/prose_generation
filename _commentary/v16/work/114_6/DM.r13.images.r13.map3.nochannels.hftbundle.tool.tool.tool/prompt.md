Focus: 114:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/114_6/D.r13/context.md =====
# 114:6 — focus

مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ

Anchor translation (canonical reading, reference only):

Cinlerden ve insanlardan.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | مِنَ | مِن |  | P |
| 2 | ٱلْجِنَّةِ | جِنَّة | ج ن ن | DET;N |
| 3 | وَٱلنَّاسِ | نَّاس | ن و س | CONJ;DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 114 — full text (context; no pericope)

- 114:1 قُلْ أَعُوذُ بِرَبِّ ٱلنَّاسِ
- 114:2 مَلِكِ ٱلنَّاسِ
- 114:3 إِلَٰهِ ٱلنَّاسِ
- 114:4 مِن شَرِّ ٱلْوَسْوَاسِ ٱلْخَنَّاسِ
- 114:5 ٱلَّذِى يُوَسْوِسُ فِى صُدُورِ ٱلنَّاسِ
- 114:6 ◀ focus مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ


===== _commentary/v16/work/114_6/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ج ن ن (root_000266) — identity root of ٱلْجِنَّةِ (w2)

- **B001** örtme ve duyulardan gizleme — örtmek; gizleyecek bir örtü sağlamak; içinde saklamak · bir şeyin arkasına gizlenmek · insanı örten giysi veya örtü
  الجيم والنون أصل واحد وهو الستر والتستر (maqayis)؛ أصل الجن ستر الشيء عن الحاسة (mufradat)؛ استجن فلان إذا استتر بشيء (ayn;tahdhib)؛ أجننت الشيء في صدري أكننته (sihah)؛ ما علي جنان إلا ما ترى أي ثوب يواريني (sihah;tahdhib)
- **B002** gecenin karartıp örtmesi — gecenin kararıp üzerini örtmesi · gecenin koyu karanlığı ve nesneleri örtmesi
  جنان الليل سواده وستره الأشياء (maqayis)؛ أجنه الليل وجن عليه الليل إذا أظلم حتى يستره بظلمته (ayn)؛ جن عليه الليل يجن بالضم جنونا (sihah)؛ جن عليه الليل وأجنه الليل إذا أظلم حتى يستره بظلمته (tahdhib)؛ جنه الليل وأجنه وجن عليه (mufradat)
- **B003** zemini ağaçlarla örtülü bahçe — zemini ağaçlarla örtülü bahçe veya koruluk
  الجنة البستان (maqayis;sihah)؛ الجنة الحديقة وهي بستان ذات شجر ونزهة (ayn)؛ العرب تسمي النخيل جنة (sihah)؛ كل بستان ذي شجر يستر بأشجاره الأرض (mufradat)
- **B004** ölüm sonrası gizli nimetler yurdu — ölüm sonrası ödül ve gizli nimetler yurdu
  الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم (maqayis)؛ سميت الجنة إما تشبيها بالجنة في الأرض وإما لستره نعمها عنا (mufradat)
- **B005** gözle görülmeyen ruhani varlıklar topluluğu — gözle görülmeyen ruhani varlıklar · görünmeyen varlıkların atası veya bir bireyi · görünmeyen ruhani varlıkların topluluğu · görünmeyen ruhani varlıkların çok bulunduğu yer
  الجن سموا بذلك لأنهم متسترون عن أعين الخلق (maqayis)؛ الجن جماعة ولد الجان وجمعهم الجنة والجنان (ayn;tahdhib)؛ الجن خلاف الإنس والواحد جني (sihah)؛ الجنة جماعة الجن (mufradat)؛ أرض مجنة كثيرة الجن (ayn;sihah;tahdhib)
- **B006** aklı örten akıl yitimi — aklını yitirmek; aklını yitirmiş duruma getirmek · akıl yitimi; benlik ile akıl arasındaki engel · aklını yitirmiş gibi davranmak
  الجنة الجنون وذلك أنه يغطي العقل (maqayis)؛ المجنة الجنون وجن الرجل وأجنه الله فهو مجنون (ayn)؛ جن الرجل جنونا وأجنه الله فهو مجنون (sihah)؛ به جنون وجنة ومجنة (tahdhib)؛ الجنون حائل بين النفس والعقل (mufradat)
- **B007** ana rahmindeki doğmamış çocuk — ana rahmindeki doğmamış çocuk · rahminde çocuk taşımak; çocuğun rahimde saklı kalması
  الجنين الولد في بطن أمه (maqayis)؛ أجنت الحامل الجنين أي الولد في بطنها (ayn)؛ الجنين الولد ما دام في البطن (sihah)؛ الجنين الولد في الرحم (tahdhib)؛ الجنين الولد ما دام في بطن أمه (mufradat)
- **B008** koruyucu siper veya savaş donanımı — koruyucu örtü, siper veya savaş donanımı · kalkan
  المجن الترس وكل ما استتر به من السلاح فهو جنة (maqayis)؛ المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك (ayn)؛ الجنة ما استترت به من سلاح والجنة السترة والمجن الترس (sihah)؛ المجن الترس (tahdhib)؛ المجن والمجنة الترس الذي يجن صاحبه (mufradat)
- **B009** ölüyü örtüp gömme — ölüyü örtmek ve gömmek · gömüt; ölü örtüsü; gömülmüş kişi
  الجنين المقبور (maqayis)؛ الجنن القبر وقيل للكفن أيضا (ayn)؛ جننت الميت وأجننته أي واريته والجنن القبر (sihah)؛ جننته في القبر وأجننته والجنن القبر والجنن الكفن (tahdhib)؛ الجنين القبر (mufradat)
- **B010** duyulardan saklı yürek ve gizli yön — yürek veya yüreğin saklı iç yönü · gizli iş veya görünmeyen yön
  الجنان القلب (maqayis)؛ الجنان روع القلب (ayn;tahdhib)؛ أراد بالجن القلب (sihah)؛ الجنان القلب لكونه مستورا عن الحاسة (mufradat)؛ الجنان الأمر الخفي (tahdhib)
- **B011** bitkinin güçlenip boylanması ve sıklaşması — bitkinin güçlenmesi, boylanması, sıklaşması veya çiçek açması · uzun ağaç; bol otlu ve henüz otlanmamış arazi
  جن النبت جنونا إذا اشتد وخرج زهره (maqayis)؛ جن النبت جنونا أي طال والتف وخرج زهره ونخلة مجنونة أي طويلة (sihah)؛ للنبت الملتف الكثيف مجنون وجنت الرياض جنونا إذا اعتم نبتها (tahdhib)؛ جن التلاع والآفاق أي كثر عشبها (mufradat)
- **B012** yılan, özellikle beyaz bir tür — yılan, beyaz yılan veya belirli bir yılan türü
  الحية الذي يسمى الجان فهو تشبيه له بالواحد من الجان (maqayis)؛ الجان حية بيضاء (ayn)؛ الجان أيضا حية بيضاء (sihah)؛ الجان الحية وجمعها جوان (tahdhib)؛ الجان ضرب من الحيات (mufradat)
- **B013** halkın büyük kitlesi — insanların çoğunluğu veya halkın büyük kitlesi
  جنان الناس معظمهم ويسمى السواد (maqayis)؛ جنان الناس دهماؤهم (sihah)؛ جنانهم جماعتهم وسوادهم (tahdhib)
- **B014** bir şeyin ilk ve yeni dönemi — gençliğin, çocukluğun veya bir dönemin ilk başlangıcı
  كان ذلك في جن شبابه أي في أول شبابه (sihah)؛ كان ذلك في جن صباه أي في حداثته وكذلك جن كل شيء أول ابتدائه (tahdhib)
- **B015** uçuş sırasında çoğalan sinek vızıltısı — sineğin vızıltısının veya sesinin çoğalması · böcekse uçuş vızıltısının artması; bitkiyse sıklaşıp dolaşması
  جن الذباب أي كثر صوته (sihah)؛ جن الخازباز به جنونا يحتمل هذين الوجهين (sihah)؛ قيل هو ذباب وجنونه كثرة ترنمه في طيرانه وقيل هو نبت وجنون النبت التفافه (tahdhib)
- **B016** göğüs kemikleri ve kaburga uçları — göğüs kemikleri veya kaburgaların göğse yakın uçları
  الجناجن عظام الصدر (maqayis)؛ الجنجن والجناجن أطراف الأضلاع مما يلي الصدر وعظم القلب (ayn)؛ الجناجن عظام الصدر الواحد جنجن (sihah)
- **B017** içine girilip saklanılan yer — saklanılan yer; ayrıca kaynakta belirli bir eski pazar yerinin adı
  المجنة اسم موضع على أميال من مكة؛ كانت مجنة وذو المجاز وعكاظ أسواقا في الجاهلية؛ المجنة أيضا الموضع الذي يستتر فيه (sihah)

## ء ن س (root_000059) — identity root of وَٱلنَّاسِ (w3)

- **B001** insan türü ve bu türden bir kişi — insanlar; insan topluluğu · insan; insan türü · insan topluluğunun bir üyesi; insana veya insanlara ait · insanlar; insan toplulukları · insanlar; halk · evde hiç kimse yok · belirli bir ağızda insan ve onun çoğulu
  الإنس خلاف الجن وسموا لظهورهم (maqayis;mufradat)؛ الإنس البشر والواحد إنسي والجمع أناسي (sihah)؛ الإنس جماعة الناس والأناسي جماع (tahdhib)
- **B002** görerek fark etme; bağlama göre işitme, sezme ve bakıp araştırma — bir şeyi görmek ve fark etmek · sesi işitmek · onda olgunluk belirtisi görmek ve bunu anlamak · ürken yabani hayvanın birini sezip çevreye bakınması · çevreye bakıp birinin olup olmadığını araştırmak
  آنست الشيء إذا رأيته وآنسته إذا سمعته (maqayis)؛ آنسته أبصرته وآنست الصوت سمعته وآنست منه رشدا علمته (sihah)؛ آنس من جانب يعني أبصر نارا والاستئناس النظر وأحس بما رابه (tahdhib)؛ فإن آنستم منهم رشدا أي أبصرتم وآنست نارا (mufradat)
- **B003** yabancılık duymadan yakınlık ve rahatlık hissetme — yakınlık ve rahatlık; yabancılık duymama · birine alışıp onun yanında sevinmek · biriyle yakınlık kurmak ve onsuz kendini yalnız hissetmek · yakın arkadaş; rahatlık veren kişi veya şey · yakınlıktan ve söyleşiden hoşlanan genç kadın · insana alışık, saldırgan olmayan köpek · gece yolcusuna veya konaklayana güven veren ateş · sahibine güven veren bütün silahlar; zırh, miğfer, koruyucu örtü ve kalkan gibi savunma donanımları
  الأنس أنس الإنسان بالشيء إذا لم يستوحش منه (maqayis)؛ الإيناس خلاف الإيحاش والإنس خلاف الوحشة والأنيس المؤانس وكل ما يؤنس به (sihah)؛ أنست بفلان أي فرحت به والأنس والاستئناس هو التأنس وكلب أنوس نقيض العقور (tahdhib)؛ الأنس خلاف النفور ولكل ما يؤنس به (mufradat)
- **B004** insana dönük yan — bir şeyin insana bakan veya en yakın olan yanı · yayın okçuya bakan yüzü · hayvanın biniciye yakın olan yanı
  الإنسي الأيسر من كل شيء وقيل الأيمن وما أقبل منهما على الإنسان فهو إنسي وإنسي القوس ما أقبل عليك منها (sihah)؛ الإنسي من الدواب الجانب الأيسر الذي منه يركب ويحتلب ومن الإنسان الجانب الذي يلي الرجل الأخرى (tahdhib)؛ إنسي الدابة للجانب الذي يلي الراكب وإنسي القوس للجانب الذي يقبل على الرامي (mufradat)
- **B005** göz bebeğinde görülen küçük yansıma — göz bebeğinde görülen küçük görüntü veya yansıma · göz bebeklerinde görülen küçük görüntüler · parmak ucu; eldeki parmak ucunu anlatan kullanım
  إنسان العين صبيها الذي في السواد (maqayis)؛ إنسان العين المثال الذي يرى في السواد أي سواد العين (sihah)؛ الإنسان أيضا إنسان العين وجمعه أناسي والإنسان الأنملة (tahdhib)
- **B006** belirli sözlerde kişinin kendisi veya seçilmiş yakını — kendin; kendi durumun nasıl · onun seçkin yakını ve sırdaşı · yakınım, içten dostum ve görüşme arkadaşım
  كيف ابن إنسك إذا سأله عن نفسه (maqayis)؛ كيف ابن إنسك يعني نفسه وفلان ابن إنس فلان أي صفيه وخاصته وهذا خدني وإنسي وخلصي وجلسي (sihah)؛ كيف ترى ابن إنسك إذا خاطبت الرجل عن نفسه وفلان ابن أنس فلان أي صفيه وأنيسه (tahdhib)؛ قيل ابن إنسك للنفس (mufradat)
- **B007** girişten önce izin ve kabul arama — 
  حتى تستأنسوا معناه حتى تستأذنوا وإنما هو حتى تسلموا وتستأنسوا السلام عليكم أأدخل (tahdhib)؛ حتى تستأنسوا أي تجدوا إيناسا (mufradat)

===== _commentary/v16/out/s114/images.r13.map3.nochannels.hftbundle.tool.tool/images.md (only the images that cite 114:6, and ## Buluşmalar) =====
## Görünen ve örtülü

Surenin son ayeti iki kelimeyi yan yana koyar: {ar:ٱلْجِنَّةِ, tr:el-cinne, gloss:cinler, source:114:6} ve {ar:ٱلنَّاسِ, tr:en-nâs, gloss:insanlar, source:114:6}. Bu iki kelimenin kökleri birbirine karşı tanımlanır. İnsan, görünür olduğu için bu adı alır: {ar:الإنس خلاف الجن وسموا لظهورهم, tr:el-ins hilâfu'l-cinn ve summû li-zuhûrihim, gloss:ins cinnin karşıtıdır, görünür oldukları için bu adı almışlardır, source:"ء ن س,B001"}. Cin ise gözden örtülü olduğu için: {ar:الجن سموا بذلك لأنهم متسترون عن أعين الخلق, tr:el-cinn summû bi-zâlike li-ennehum mütesettirûne an a'yuni'l-halk, gloss:cinler yaratılmışların gözlerinden örtülü oldukları için böyle adlandırıldı, source:"ج ن ن,B005"}. Kökün işleyişi tek bir harekettir: {ar:أصل الجن ستر الشيء عن الحاسة, tr:aslu'l-cenn setru'ş-şey'i ani'l-hâsse, gloss:cenn kökünün aslı bir şeyi duyudan örtmektir, source:"ج ن ن,B001"}. Bu kök imgeleri her yerde kelimenin ayetteki anlamının yanında duyulur, onun yerine geçmez: ayette "insanlar" ve "cinler" kastedilir, imge bu anlamın arkasından gelen yankıdır.

Bu karşıtlık geriye doğru okunur. "Rab", "Melik", "İlah" diye üç kez anılan ve beşinci ayette göğüsleri hedef alınan "insanlar", altıncı ayete gelince görünenler olarak belirir. Aynı kök görmeyi ve işitmeyi de adlandırır: {ar:آنسته أبصرته وآنست الصوت سمعته, tr:âneston-hu ebsartu-hû ve âneste's-savte semi'tu-hû, gloss:onu fark ettim, gördüm; sesi fark ettim, işittim, source:"ء ن س,B002"}. Görünenler aynı zamanda algılayanlardır. Onlara işleyen ise algının hemen altında durur. Dördüncü ayetin {ar:ٱلْوَسْوَاسِ, tr:el-vesvâs, gloss:fısıldayan, source:114:4} kelimesi gizli bir sestir: {ar:الوسواس الصوت الخفي من ريح تهز قصبا ونحوه, tr:el-vesvâsu's-savtu'l-hafiyyu min rîhin tehuzzu kasaben, gloss:vesvas, kamışı sallayan rüzgârın gizli sesidir, source:"و س و س,B002"}; yalnızca bir kıpırtı olarak duyulur. Yanındaki {ar:ٱلْخَنَّاسِ, tr:el-hannâs, gloss:sinip çekilen, source:114:4} saklanmayı ve örtünmeyi söyler {source:"خ ن س,B001"}. Kötülüğün kendi kelimesi {ar:شَرِّ, tr:şerr, gloss:kötülük, source:114:4} ise ters yönü taşır: {ar:أشررت الشيء إذا أبرزته وأظهرته, tr:eşertu'ş-şey'e izâ ebraztuhû ve azhartuhû, gloss:bir şeyi ortaya çıkarıp görünür kıldığımda "eşrartu" derim, source:"ش ر ر,B008"} ve {ar:الشر بسطك الشيء في الشمس, tr:eş-şerru bastuke'ş-şey'e fi'ş-şems, gloss:şerr, bir şeyi güneşe sermendir, source:"ش ر ر,B002"}. Kötülük bir açığa çıkarma kökünden adlandırılır, ama saklanan birine aittir.

Kuran bu sahneyi bahçede kurar. Şeytan Âdem'le eşine fısıldar ve fısıltının amacı açıkça söylenir: {ar:فَوَسْوَسَ لَهُمَا ٱلشَّيْطَٰنُ لِيُبْدِىَ لَهُمَا مَا وُۥرِىَ عَنْهُمَا مِن سَوْءَٰتِهِمَا, tr:fe-vesvese lehume'ş-şeytânu li-yubdiye lehumâ mâ vûriye anhumâ min sev'âtihimâ, gloss:şeytan onlara örtülü kalan çıplaklıklarını açmak için fısıldadı, source:7:20}. İki ayet sonra iş tamamlanır: {ar:بَدَتْ لَهُمَا سَوْءَٰتُهُمَا, tr:bedet lehumâ sev'âtuhumâ, gloss:çıplaklıkları kendilerine göründü, source:7:22}. Saklananın işi açığa çıkarmakla biter. Hemen ardından Allah Âdemoğullarına seslenir ve gözün dengesizliğini adlandırır: {ar:إِنَّهُۥ يَرَىٰكُمْ هُوَ وَقَبِيلُهُۥ مِنْ حَيْثُ لَا تَرَوْنَهُمْ, tr:innehû yerâkum huve ve kabîluhû min haysu lâ terevnehum, gloss:o ve onun takımı, sizin onları göremediğiniz yerden sizi görür, source:7:27}. Surenin görünen insanları, görülmeden gören birine karşı korunmaktadır. Kuran'da cinlerin kendi anlatımı ise sığınmanın yanlış yöne döndüğü bir durumu bildirir: {ar:رِجَالٌۭ مِّنَ ٱلْإِنسِ يَعُوذُونَ بِرِجَالٍۢ مِّنَ ٱلْجِنِّ فَزَادُوهُمْ رَهَقًۭا, tr:ricâlun mine'l-insi yeûzûne bi-ricâlin mine'l-cinni fe-zâdûhum rehakâ, gloss:insten bazı adamlar cinden bazı adamlara sığınırdı, bu da onların azgınlığını artırdı, source:72:6}. Surenin "insanların Rabbine sığınırım" sözü bu sapmanın düzeltilmiş halidir: sığınma görünmeyen tarafa değil, iki tarafın da Rabbine yönelir.

Altıncı ayet fısıldayanın iki sınıftan çıkabileceğini söyler. Kuran aynı ikiliyi peygambere düşmanlık bağlamında verir: {ar:شَيَٰطِينَ ٱلْإِنسِ وَٱلْجِنِّ يُوحِى بَعْضُهُمْ إِلَىٰ بَعْضٍۢ زُخْرُفَ ٱلْقَوْلِ غُرُورًۭا, tr:şeyâtîne'l-insi ve'l-cinni yûhî ba'duhum ilâ ba'din zuhrufe'l-kavli gurûrâ, gloss:ins ve cin şeytanları aldatmak için birbirlerine yaldızlı söz fısıldar, source:6:112}. Yani görünenler de örtülü bir iş yapabilir. Surenin son ifadesi, Kuran'da başka yerde de aynı sözcüklerle durur: {ar:لَأَمْلَأَنَّ جَهَنَّمَ مِنَ ٱلْجِنَّةِ وَٱلنَّاسِ أَجْمَعِينَ, tr:le-emleenne cehenneme mine'l-cinneti ve'n-nâsi ecmaîn, gloss:cehennemi cinlerden ve insanlardan dolduracağım, source:11:119}, {source:32:13}. Yaratılışları da yan yana konur: insan kuru balçıktan {source:55:14}, cann ateşten {source:55:15}. Sonunda yoldan çıkmış olanlar, görmedikleri saptırıcıları görmek ister: {ar:رَبَّنَآ أَرِنَا ٱلَّذَيْنِ أَضَلَّانَا مِنَ ٱلْجِنِّ وَٱلْإِنسِ, tr:rabbenâ erine'llezeyni edallânâ mine'l-cinni ve'l-ins, gloss:Rabbimiz, bizi saptıran cin ve insi bize göster, source:41:29}. Görünmezlik orada biter.

Kaynaklar: 114:1–3, 5, 6 ٱلنَّاسِ ء ن س B001; 114:5, 6 ٱلنَّاسِ ء ن س B002; 114:6 ٱلْجِنَّةِ ج ن ن B005; 114:6 ٱلْجِنَّةِ ج ن ن B001; 114:4 ٱلْوَسْوَاسِ و س و س B002; 114:4 ٱلْخَنَّاسِ خ ن س B001; 114:4 شَرِّ ش ر ر B008; 114:4 شَرِّ ش ر ر B002

## Göğüs ve içinde saklanan

Beşinci ayet fısıltının yerini adlandırır: {ar:فِى صُدُورِ ٱلنَّاسِ, tr:fî sudûri'n-nâs, gloss:insanların göğüslerinde, source:114:5}. Göğüs bedenin bir odasıdır, önü yükselen bir kafestir: {ar:الصدرة من الإنسان ما أشرف من أعلى صدره, tr:es-sudretu mine'l-insâni mâ eşrafe min a'lâ sadrih, gloss:insanın sudresi göğsünün üstünde yükselen kısmıdır, source:"ص د ر,B001"}. Altıncı ayetin {ar:ٱلْجِنَّةِ, tr:el-cinne, gloss:cinler, source:114:6} kelimesinin kökü bu odanın parçalarını da adlandırır: {ar:الجناجن عظام الصدر, tr:el-cenâcin izâmu's-sadr, gloss:cenâcin göğüs kemikleridir, source:"ج ن ن,B016"}. Odanın içindeki kalp de aynı kökten, gizli olduğu için adını alır: {ar:الجنان القلب لكونه مستورا عن الحاسة, tr:el-cenânu'l-kalbu li-kevnihî mestûran ani'l-hâsse, gloss:cenân kalptir, duyudan örtülü olduğu için, source:"ج ن ن,B010"}. Ve kök bir şeyi göğüste saklamayı söyler: {ar:أجننت الشيء في صدري أكننته, tr:ecnentu'ş-şey'e fî sadrî ekenentuh, gloss:o şeyi göğsümde gizledim, source:"ج ن ن,B001"}. Böylece saldıranın adı ile saldırının yapıldığı odanın kemikleri ve içindeki kalp aynı köke bağlanır: örtülü olan, örtülü bir odaya girer.

Fısıltı tam bu odaya yerleştirilir: {ar:وسوس إلي ووسوس في صدري, tr:vesvese ileyye ve vesvese fî sadrî, gloss:bana fısıldadı, göğsümde fısıldadı, source:"و س و س,B001"}. Ve fısıltı, kişinin kendi kendine konuşmasına benzer: {ar:الوسوسة حديث النفس, tr:el-vesvesetu hadîsu'n-nefs, gloss:vesvese nefsin kendi kendine konuşmasıdır, source:"و س و س,B001"}. İnsan kökü de kendine döner: {ar:كيف ابن إنسك يعني نفسه, tr:keyfe'bnu insik, gloss:"insinin oğlu nasıl" yani kendisi nasıl, source:"ء ن س,B006"}. Bu yüzden fısıltı dışarıdan gelen bir ses gibi değil, kişinin kendi sesi gibi duyulur; tehlikeyi görünmez kılan budur. İkinci ayetin {ar:مَلِكِ, tr:melik, gloss:hükümdar, source:114:2} kelimesinin kökü kalbi bedenin dayanağı sayar: {ar:القلب ملاك الجسد, tr:el-kalbu milâku'l-ced, gloss:kalp bedenin ayakta tutanıdır, source:"م ل ك,B005"}. Fısıltı bedeni ayakta tutan noktaya gider. İlk ayetin {ar:قُلْ, tr:kul, gloss:de, source:114:1} kelimesinin kökü de içte tutulan sözü bilir: {ar:في نفسي قول لم أظهره, tr:fî nefsî kavlun lem uzhirh, gloss:içimde açığa vurmadığım bir söz var, source:"ق و ل,B012"}. Göğüs iki sözün de yeridir: emredilen sığınma sözü oradan çıkar, fısıltı oraya girer.

İnsan kökü bir eve girmeden önce izin istemeyi de adlandırır {source:"ء ن س,B007"}. Kuran bunu emreder: {ar:لَا تَدْخُلُوا۟ بُيُوتًا غَيْرَ بُيُوتِكُمْ حَتَّىٰ تَسْتَأْنِسُوا۟ وَتُسَلِّمُوا۟ عَلَىٰٓ أَهْلِهَا, tr:lâ tedhulû buyûten gayra buyûtikum hattâ teste'nisû ve tusellimû alâ ehlihâ, gloss:kendi evlerinizden başka evlere, izin alıp halkına selam vermeden girmeyin, source:24:27}. Fısıldayan bu kuralın tersini yapar: göğüs odasına izin almadan girer.

Kuran göğsün içini bilen yakınlığı aynı fiille gösterir: {ar:وَنَعْلَمُ مَا تُوَسْوِسُ بِهِۦ نَفْسُهُۥ ۖ وَنَحْنُ أَقْرَبُ إِلَيْهِ مِنْ حَبْلِ ٱلْوَرِيدِ, tr:ve na'lemu mâ tuvesvisu bihî nefsuh, ve nahnu akrabu ileyhi min habli'l-verîd, gloss:nefsinin ona ne fısıldadığını biliriz; biz ona şah damarından daha yakınız, source:50:16}. Fısıltının girdiği yerden daha derinde bir yakınlık vardır; sığınılan Rab bu yakınlıktadır. Göğsünü saklamak için bükenler de anlatılır: {ar:يَثْنُونَ صُدُورَهُمْ لِيَسْتَخْفُوا۟ مِنْهُ, tr:yesnûne sudûrahum li-yestahfû minh, gloss:ondan gizlenmek için göğüslerini bükerler, source:11:5}; elbiselerine bürünseler de {ar:إِنَّهُۥ عَلِيمٌۢ بِذَاتِ ٱلصُّدُورِ, tr:innehû alîmun bi-zâti's-sudûr, gloss:o göğüslerin özünü bilir, source:11:5}. Sözlükteki "göğüste gizlemek" fiilinin kardeşi Kuran'da da göğüslere söylenir: {ar:وَرَبُّكَ يَعْلَمُ مَا تُكِنُّ صُدُورُهُمْ, tr:ve rabbuke ya'lemu mâ tukinnu sudûruhum, gloss:Rabbin göğüslerinin gizlediğini bilir, source:28:69}. Kalp göğsün içindedir: {ar:ٱلْقُلُوبُ ٱلَّتِى فِى ٱلصُّدُورِ, tr:el-kulûbu'lletî fi's-sudûr, gloss:göğüslerdeki kalpler, source:22:46}. Göğüste oturan bir şeye karşı ilaç da sığınmadır: {ar:إِن فِى صُدُورِهِمْ إِلَّا كِبْرٌۭ مَّا هُم بِبَٰلِغِيهِ ۚ فَٱسْتَعِذْ بِٱللَّهِ, tr:in fî sudûrihim illâ kibrun mâ hum bi-bâliğîh, festeiz billâh, gloss:göğüslerinde yalnızca ulaşamayacakları bir büyüklenme var; Allah'a sığın, source:40:56}. Sonunda göğüslerdekinin hepsi dışarı çıkarılır: {ar:وَحُصِّلَ مَا فِى ٱلصُّدُورِ, tr:ve hussile mâ fi's-sudûr, gloss:göğüslerde olan ortaya dökülür, source:100:10}. Göğüs, Kuran'ın açıp genişlettiği bir oda olarak da görünür: {ar:رَبِّ ٱشْرَحْ لِى صَدْرِى, tr:rabbi'şrah lî sadrî, gloss:Rabbim, göğsümü aç, source:20:25}.

Kaynaklar: 114:5 صُدُورِ ص د ر B001; 114:6 ٱلْجِنَّةِ ج ن ن B016; 114:6 ٱلْجِنَّةِ ج ن ن B010; 114:6 ٱلْجِنَّةِ ج ن ن B001; 114:5 يُوَسْوِسُ و س و س B001; 114:2 مَلِكِ م ل ك B005; 114:5 ٱلنَّاسِ ء ن س B006; 114:1 قُلْ ق و ل B012; 114:5 ٱلنَّاسِ ء ن س B007

## Söz: içte kurulan, dile çıkan, insanlar arasında yayılan

Sure bir emirle açılır: {ar:قُلْ, tr:kul, gloss:de, source:114:1}. Söz, telaffuzla dışarı çıkarılan şeydir: {ar:المركب من الحروف المبرز بالنطق, tr:el-murakkabu mine'l-hurûfi'l-mubrazu bi'n-nutk, gloss:harflerden kurulup konuşmayla dışarı çıkarılan, source:"ق و ل,B001"}. Ama aynı kök sözün içteki halini de söz sayar: {ar:المتصور في النفس قبل الإبراز باللفظ قول, tr:el-mutasavveru fi'n-nefsi kable'l-ibrâzi bi'l-lafz kavl, gloss:lafızla dışarı çıkarılmadan önce nefiste kurulan şey de sözdür, source:"ق و ل,B012"}. Sözün organı da adını kökten alır: {ar:المقول اللسان, tr:el-mikvel el-lisân, gloss:mikvel dildir, source:"ق و ل,B002"}. "De" emri bu yolu tarif eder: sığınma içte kurulur, dile gelir, dışarı söylenir.

Fısıltı aynı yolu ters yönde yürür. O da bir konuşmadır ama dışarı çıkmaz: {ar:الوسوسة حديث النفس؛ وسوست إليه نفسه, tr:el-vesvesetu hadîsu'n-nefs; vesveset ileyhi nefsuh, gloss:vesvese nefsin konuşmasıdır; nefsi ona fısıldadı, source:"و س و س,B001"}. Sesi bir mırıltıya indirilmiştir: {ar:صوت الحلي والهمس الخفي, tr:savtu'l-huliyyi ve'l-hemsu'l-hafiyy, gloss:takıların sesi ve gizli fısıltı, source:"و س و س,B002"}. Biri içten dışa çıkan söz, öbürü dıştan göğse giren söz. Kök iki şeyi daha bilir: iyi ya da kötü bir sözü kendi üstüne çekmek, {ar:اقتال قولا أي اجتر إلى نفسه قولا من خير أو شر, tr:iktâle kavlen ey icterra ilâ nefsihî kavlen min hayrin ev şerr, gloss:iyi ya da kötü bir sözü kendine çekti, source:"ق و ل,B006"}, ve hiçbir hitap gelmediği halde içe düşen ilhamı söz diye adlandırmak {source:"ق و ل,B017"}. Fısıltının iyi ikizi budur: o da sessiz bir sözdür.

Kök sözün insanlar arasında yayılmasını da adlandırır: {ar:القالة القول الفاشي في الناس, tr:el-kâletu'l-kavlu'l-fâşî fi'n-nâs, gloss:kâle insanlar arasında yayılan sözdür, source:"ق و ل,B007"}. Karşılıklı konuşmayı {source:"ق و ل,B009"} ve birine yalan söz yüklemeyi de {source:"ق و ل,B005"}. Altıncı ayetin "insanlardan da" demesi bu kanalı açar: fısıltı insan dilinden insan kulağına da gelir. Son halka işiten insandır: {ar:آنست الصوت سمعته, tr:âneste's-savte semi'tuh, gloss:sesi fark ettim, işittim, source:"ء ن س,B002"}.

Kuran bu çerçeveyi aynı kalıpla verir. Peygambere emredilir: {ar:وَقُل رَّبِّ أَعُوذُ بِكَ مِنْ هَمَزَٰتِ ٱلشَّيَٰطِينِ, tr:ve kul rabbi eûzu bike min hemezâti'ş-şeyâtîn, gloss:de ki: Rabbim, şeytanların dürtmelerinden sana sığınırım, source:23:97}. Okunan söz de sığınmayla başlar: {ar:فَإِذَا قَرَأْتَ ٱلْقُرْءَانَ فَٱسْتَعِذْ بِٱللَّهِ مِنَ ٱلشَّيْطَٰنِ ٱلرَّجِيمِ, tr:fe-izâ kara'te'l-kur'âne festeiz billâhi mine'ş-şeytâni'r-racîm, gloss:Kuran okuduğunda kovulmuş şeytandan Allah'a sığın, source:16:98}. Bahçede fısıltı açık söze döner: {ar:وَقَالَ مَا نَهَىٰكُمَا رَبُّكُمَا, tr:ve kâle mâ nehâkumâ rabbukumâ, gloss:ve dedi: Rabbiniz sizi ancak şunun için yasakladı, source:7:20}, ardından yemine {source:7:21}. Başka bir anlatımda fısıltı bir teklif biçimini alır: {ar:فَوَسْوَسَ إِلَيْهِ ٱلشَّيْطَٰنُ قَالَ يَٰٓـَٔادَمُ هَلْ أَدُلُّكَ, tr:fe-vesvese ileyhi'ş-şeytânu kâle yâ âdemu hel edulluke, gloss:şeytan ona fısıldadı, dedi: Ey Âdem, sana göstereyim mi, source:20:120}. Gizli söz insan tartışmasına da çıkar: {ar:وَإِنَّ ٱلشَّيَٰطِينَ لَيُوحُونَ إِلَىٰٓ أَوْلِيَآئِهِمْ لِيُجَٰدِلُوكُمْ, tr:ve inne'ş-şeyâtîne le-yûhûne ilâ evliyâihim li-yucâdilûkum, gloss:şeytanlar sizinle tartışsınlar diye dostlarına fısıldar, source:6:121}. İnsanlar arasındaki gizli konuşma da aynı kaynaktandır: {ar:إِنَّمَا ٱلنَّجْوَىٰ مِنَ ٱلشَّيْطَٰنِ, tr:innema'n-necvâ mine'ş-şeytân, gloss:gizli konuşma şeytandandır, source:58:10}. Dilden dile yayılan söz de anlatılır: {ar:إِذْ تَلَقَّوْنَهُۥ بِأَلْسِنَتِكُمْ وَتَقُولُونَ بِأَفْوَاهِكُم مَّا لَيْسَ لَكُم بِهِۦ عِلْمٌۭ, tr:iz telakkavnehû bi-elsinetikum ve tekûlûne bi-efvâhikum mâ leyse lekum bihî ilm, gloss:onu dillerinizle birbirinizden alıyor, bilmediğiniz şeyi ağızlarınızla söylüyordunuz, source:24:15}. Karşı tedbir de sözdür: {ar:وَقُل لِّعِبَادِى يَقُولُوا۟ ٱلَّتِى هِىَ أَحْسَنُ ۚ إِنَّ ٱلشَّيْطَٰنَ يَنزَغُ بَيْنَهُمْ, tr:ve kul li-ibâdî yekûlu'lletî hiye ahsen, inne'ş-şeytâne yenzeğu beynehum, gloss:kullarıma söyle, en güzel olanı söylesinler; şeytan aralarına girip kışkırtır, source:17:53}. Ve indirilen söz şeytanın sözü değildir: {ar:وَمَا هُوَ بِقَوْلِ شَيْطَٰنٍۢ رَّجِيمٍۢ, tr:ve mâ huve bi-kavli şeytânin racîm, gloss:o kovulmuş bir şeytanın sözü değildir, source:81:25}; {ar:إِنَّهُۥ لَقَوْلُ رَسُولٍۢ كَرِيمٍۢ, tr:innehû le-kavlu rasûlin kerîm, gloss:o şerefli bir elçinin sözüdür, source:81:19}. "Yalan söz yüklemek" anlamı ise Kuran'da elçiye yöneltilen suçlamada görünür: {ar:أَمْ يَقُولُونَ تَقَوَّلَهُۥ, tr:em yekûlûne tekavveleh, gloss:yoksa "onu kendisi uydurdu" mu diyorlar, source:52:33}, {source:69:44}.

Kaynaklar: 114:1 قُلْ ق و ل B001; 114:1 قُلْ ق و ل B012; 114:1 قُلْ ق و ل B002; 114:1 قُلْ ق و ل B007; 114:1 قُلْ ق و ل B006; 114:1 قُلْ ق و ل B017; 114:1 قُلْ ق و ل B009; 114:1 قُلْ ق و ل B005; 114:4, 5 ٱلْوَسْوَاسِ / يُوَسْوِسُ و س و س B001; 114:4 ٱلْوَسْوَاسِ و س و س B002; 114:4 شَرِّ ش ر ر B008; 114:6 وَٱلنَّاسِ ء ن س B002

## Sığınma: okunan muska ve bedenin örtüleri

{ar:أَعُوذُ, tr:eûzu, gloss:sığınırım, source:114:1} birine sığınıp ona tutunmaktır, ve fiil kendi Rabbiyle tek ifadede durur: {ar:عاذ فلان بربه يعوذ عوذا إذا لجأ إليه واعتصم به, tr:âze fulânun bi-rabbihî yeûzu avzen izâ lecee ileyhi va'tesame bih, gloss:Rabbine sığındı, ona kaçıp tutundu, source:"ع و ذ,B001"}. Sığınılan bir kaçış yeridir: {ar:وهو عياذي أي ملجئي, tr:ve huve iyâzî ey melceî, gloss:o benim sığınağım, kaçtığım yerdir, source:"ع و ذ,B001"}. Kök kişinin sığındığı nesneyi de adlandırır: okunan söz ve takılan muska, {ar:العوذة ما يعاذ به من الشيء ومنه قيل للتميمة والرقية عوذة, tr:el-ûzetu mâ yuâzu bihî ve minhu kîle li't-temîmeti ve'r-rukyeti ûze, gloss:ûze sığınılan şeydir; muskaya ve okunan duaya da bu yüzden ûze denir, source:"ع و ذ,B002"}; yazılıp bedene asılan {source:"ع و ذ,B002"}; ve özellikle {ar:العوذة والمعاذة التي يعوذ بها الإنسان من فزع أو جنون, tr:el-ûzetu ve'l-meâzetu'lletî yeûzu bihe'l-insânu min fezain ev cunûn, gloss:insanın korkuya ya da deliliğe karşı sığındığı şey, source:"ع و ذ,B002"}. Atın boynunda gerdanlığın asıldığı yer de bu köktendir {source:"ع و ذ,B005"}. Böylece "de: sığınırım" emri, dilde taşınan bir korunak olur; muskayı taşıyan organ dildir {source:"ق و ل,B002"}. Sığınılan Rab sahip olan, itaat edilen ve düzelten olarak tanımlanır {source:"ر ب ب,B001"}.

Surenin öbür kelimeleri bedenin başka örtülerini getirir. Altıncı ayetin kelimesinin kökü kalkanı ve zırhı adlandırır: {ar:المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك, tr:el-micennu't-tursu ve'l-cunnetu'd-dir'u ve kullu mâ vakâke fe-huve cunnetuk, gloss:micenn kalkandır, cunne zırhtır; seni koruyan her şey senin cunnendir, source:"ج ن ن,B008"}; insanı örten elbiseyi, {ar:ما علي جنان إلا ما ترى أي ثوب يواريني, tr:mâ aleyye cenânun illâ mâ terâ, gloss:üstümde gördüğünden başka beni örten bir giysi yok, source:"ج ن ن,B001"}; ve saklanılacak yeri {source:"ج ن ن,B017"}. Beşinci ayetin kelimesinin kökü göğsü örten bir giysiyi bilir: {ar:الصدار ثوب يغطي الصدر, tr:es-sidâru sevbun yugattî's-sadr, gloss:sidâr göğsü örten giysidir, source:"ص د ر,B001"}. Bütün bu örtüler dıştadır; fısıltı ise göğsün içinde, her örtünün altında işler. Zırh ve kalkan dışardan gelen saldırıya yarar; içerden fısıldayana karşı tek örtü, söylenen sığınmadır. Ayrıca aynı kelime iki tarafı adlandırır: örtülü saldıran (cinne) ve kalkan (cunne).

Kuran sığınmayı hep söylenen bir söz olarak verir. İmran'ın karısı doğumdan sonra şöyle der: {ar:وَإِنِّىٓ أُعِيذُهَا بِكَ وَذُرِّيَّتَهَا مِنَ ٱلشَّيْطَٰنِ ٱلرَّجِيمِ, tr:ve innî uîzuhâ bike ve zurriyyetehâ mine'ş-şeytâni'r-racîm, gloss:onu ve soyunu kovulmuş şeytandan sana sığındırırım, source:3:36}. Yusuf kapıları kapalı evde: {ar:مَعَاذَ ٱللَّهِ ۖ إِنَّهُۥ رَبِّىٓ أَحْسَنَ مَثْوَاىَ, tr:meâza'llâh, innehû rabbî ahsene mesvây, gloss:Allah'a sığınırım; o benim efendimdir, bana güzel bir yer verdi, source:12:23}. Meryem ruha karşı: {ar:إِنِّىٓ أَعُوذُ بِٱلرَّحْمَٰنِ مِنكَ, tr:innî eûzu bi'r-rahmâni mink, gloss:senden Rahman'a sığınırım, source:19:18}. Musa kavmine: {ar:إِنِّى عُذْتُ بِرَبِّى وَرَبِّكُم, tr:innî uztu bi-rabbî ve rabbikum, gloss:ben benim de sizin de Rabbinize sığındım, source:40:27}, {source:44:20}. Peygambere öğretilen dua da Rabbe bağlanır: {ar:وَأَعُوذُ بِكَ رَبِّ أَن يَحْضُرُونِ, tr:ve eûzu bike rabbi en yahdurûn, gloss:Rabbim, onların yanıma gelmesinden de sana sığınırım, source:23:98}. İkiz sure de aynı sözle açılır: {ar:قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ, tr:kul eûzu bi-rabbi'l-felak, gloss:de ki: sabahın Rabbine sığınırım, source:113:1}. Kalkan anlamı Kuran'da yanlış kullanılır: münafıklar {ar:ٱتَّخَذُوٓا۟ أَيْمَٰنَهُمْ جُنَّةًۭ فَصَدُّوا۟ عَن سَبِيلِ ٱللَّهِ, tr:ittehazû eymânehum cunneten fe-saddû an sebîli'llâh, gloss:yeminlerini kalkan edinip Allah'ın yolundan alıkoydular, source:58:16}, {source:63:2}. Giysi ve soyulması da yan yana durur: {ar:لِبَاسًۭا يُوَٰرِى سَوْءَٰتِكُمْ, tr:libâsen yuvârî sev'âtikum, gloss:çıplaklıklarınızı örten bir giysi, source:7:26}, {ar:وَلِبَاسُ ٱلتَّقْوَىٰ ذَٰلِكَ خَيْرٌۭ, tr:ve libâsu't-takvâ zâlike hayr, gloss:takva giysisi ise daha hayırlıdır, source:7:26}; sonra şeytan giysiyi çekip alır {source:7:27}. Dış giysi soyulabilir; takva giysisi içtedir.

Kaynaklar: 114:1 أَعُوذُ ع و ذ B001; 114:1 أَعُوذُ ع و ذ B002; 114:1 أَعُوذُ ع و ذ B005; 114:1 أَعُوذُ ع و ذ B007; 114:1 قُلْ ق و ل B002; 114:1 بِرَبِّ ر ب ب B001; 114:6 ٱلْجِنَّةِ ج ن ن B008; 114:6 ٱلْجِنَّةِ ج ن ن B001; 114:6 ٱلْجِنَّةِ ج ن ن B017; 114:5 صُدُورِ ص د ر B001

## Ana ve yavru: rahimde gizli, doğan, yanında tutulan, olgunluğa yetiştirilen

İlk ayetin iki kelimesi, {ar:أَعُوذُ, tr:eûzu, gloss:sığınırım, source:114:1} ve {ar:بِرَبِّ, tr:bi-rabbi, gloss:Rabbine, source:114:1}, kökleriyle yeni doğurmuş anneyi adlandırır. Birincisinde: {ar:كل أنثى عائذ إذا وضعت مدة سبعة أيام والجميع عوذ, tr:kullu unsâ âizun izâ vada'at muddete seb'ati eyyâm, gloss:her dişi doğurduktan sonra yedi gün âiz'dir, çoğulu ûz, source:"ع و ذ,B003"}; ceylanlar, develer ve atlar için söylenir. İkincisinde: {ar:الشاة الربي التي تحتبس في البيت للبن, tr:eş-şâtu'r-rubbâ elletî tuhtebesu fi'l-beyti li'l-leben, gloss:rubbâ, sütü için evde tutulan koyundur, source:"ر ب ب,B009"}. Aynı kök bakıcıyı ve yetiştirmeyi bilir: üvey babayı ve çocuğu kucağında büyüten kadını {ar:الربيبة: الحاضنة, tr:er-rabîbe el-hâdına, gloss:rabîbe bakıcıdır, source:"ر ب ب,B005"}, ve bir şeyi aşama aşama tamamlanmaya götürmeyi: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi halden hale tamlık sınırına kadar inşa etmektir, source:"ر ب ب,B002"}. Altıncı ayetin kelimesinin kökü de karnındaki çocuğu adlandırır: {ar:الجنين الولد ما دام في البطن, tr:el-cenînu'l-veledu mâ dâme fi'l-batn, gloss:cenin karında olduğu sürece çocuktur, source:"ج ن ن,B007"}. İki kök gençliğin ilk tazeliğini de adlandırır {source:"ج ن ن,B014"} {source:"ر ب ب,B009"}.

Sahne şudur: gizli çocuk doğar, anne yanında kalır, bir bakıcı onu aşama aşama büyütür. Bu imge "Rab" kelimesinin yanında duyulunca, sığınma yavrunun kendisini doğuran ve büyütene yapışması gibi görünür; insanların Rabbi, onları bu sırayla büyütendir.

Aynı kök yetiştirmeyi bitki büyütmeye de taşır, bu yüzden bulut, su ve korunan bitki bu imgeye aittir. Bulut, bitkiyi büyüttüğü için bu adı alır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb, summiye bi-zâlike li-ennehû yurabbi'n-nebât, gloss:rabâb buluttur; bitkiyi yetiştirdiği için böyle denmiştir, source:"ر ب ب,B008"}; süren bulut {source:"ر ب ب,B007"}; bol tatlı su {source:"ر ب ب,B013"}; yazın solmayan narin bitki {source:"ر ب ب,B012"}; ve tamamlanana dek bakılan arazi, {ar:رب الضيعة أي أصلحها وأتمها, tr:rabbe'd-day'a ey aslahahâ ve etemmehâ, gloss:araziyi düzeltip tamamladı, source:"ر ب ب,B002"}. Altıncı ayetin kökü ağaçlarıyla yeri örten bahçedir, {ar:كل بستان ذي شجر يستر بأشجاره الأرض, tr:kullu bustânin zî şecerin yesturu bi-eşcârihi'l-ard, gloss:ağaçlarıyla yeri örten her bahçe, source:"ج ن ن,B003"}; uzayıp sarmaşan ve çiçek açan bitki {source:"ج ن ن,B011"}; bugün gizli olan ödül bahçesi {source:"ج ن ن,B004"}. Sığınma kökü de dikenlerin dibinde, otlayanların erişemediği bitkiyi bilir: {ar:العوذ النبت في أصل الشوك أو في المكان الحزن لا يكاد المال يناله, tr:el-ûzu'n-nebtu fî asli'ş-şevk, gloss:ûz dikenin dibinde, hayvanların ulaşamadığı bitkidir, source:"ع و ذ,B004"}.

Kuran ana, sığınma, Rab ve büyütmeyi tek sahnede toplar. İmran'ın karısı karnındakini adar: {ar:رَبِّ إِنِّى نَذَرْتُ لَكَ مَا فِى بَطْنِى مُحَرَّرًۭا, tr:rabbi innî nezertu leke mâ fî batnî muharrarâ, gloss:Rabbim, karnımdakini sana adadım, source:3:35}; doğumdan sonra onu Rabbine sığındırır {source:3:36}; sonra {ar:فَتَقَبَّلَهَا رَبُّهَا بِقَبُولٍ حَسَنٍۢ وَأَنۢبَتَهَا نَبَاتًا حَسَنًۭا وَكَفَّلَهَا زَكَرِيَّا, tr:fe-tekabbelehâ rabbuhâ bi-kabûlin hasenin ve enbetehâ nebâten hasenen ve keffelehâ zekeriyyâ, gloss:Rabbi onu güzelce kabul etti, güzel bir bitki gibi büyüttü ve Zekeriya'yı ona bakıcı yaptı, source:3:37}. Rahim, sığınma, Rab, bitki gibi büyütme ve bakıcı tek sahnededir. Rahimdeki oluşum da Rab, mülk ve ilahlıkla bağlanır: {ar:يَخْلُقُكُمْ فِى بُطُونِ أُمَّهَٰتِكُمْ خَلْقًۭا مِّنۢ بَعْدِ خَلْقٍۢ فِى ظُلُمَٰتٍۢ ثَلَٰثٍۢ ۚ ذَٰلِكُمُ ٱللَّهُ رَبُّكُمْ لَهُ ٱلْمُلْكُ ۖ لَآ إِلَٰهَ إِلَّا هُوَ, tr:yahlukukum fî butûni ummehâtikum halkan min ba'di halkın fî zulumâtin selâs, zâlikumu'llâhu rabbukum lehu'l-mulk, lâ ilâhe illâ hû, gloss:sizi annelerinizin karınlarında üç karanlık içinde yaratılıştan yaratılışa geçirir; işte Rabbiniz Allah budur, mülk onundur, ondan başka ilah yoktur, source:39:6}. Surenin ilk üç ayetinin üç ilişkisi bu ayette rahimdeki oluşumun ardından sıralanır. Ceninin çoğulu da Rab ile aynı ayettedir: {ar:وَإِذْ أَنتُمْ أَجِنَّةٌۭ فِى بُطُونِ أُمَّهَٰتِكُمْ, tr:ve iz entum ecinnetun fî butûni ummehâtikum, gloss:siz annelerinizin karnında ceninler iken, source:53:32}. Kucaktaki rabîbe yasada geçer {source:4:23}. Rakip bir büyütücü de vardır: Firavun Musa'ya {ar:أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا, tr:e-lem nurabbike fînâ velîdâ, gloss:seni çocukken aramızda büyütmedik mi, source:26:18} der. Musa'nın annesinden ayrılması ise geri alınır: {ar:فَرَدَدْنَٰهُ إِلَىٰٓ أُمِّهِۦ كَىْ تَقَرَّ عَيْنُهَا, tr:fe-radednâhu ilâ ummihî key tekarra aynuhâ, gloss:gözü aydın olsun diye onu annesine geri verdik, source:28:13}. Çocuğun duası da bu fiili kullanır: {ar:رَّبِّ ٱرْحَمْهُمَا كَمَا رَبَّيَانِى صَغِيرًۭا, tr:rabbi'rhamhumâ kemâ rabbeyânî sağîrâ, gloss:Rabbim, onlar beni küçükken büyüttükleri gibi sen de onlara merhamet et, source:17:24}. Bahçe imgesinin bir yüzü de vardır: ilk fısıltı bir bahçede oldu {source:7:20} ve bahçenin yaprakları örtü oldu {source:7:22}; iki bahçe sahibinin arkadaşı ise bahçe karşısında {ar:لَّٰكِنَّا۠ هُوَ ٱللَّهُ رَبِّى, tr:lâkinnâ huva'llâhu rabbî, gloss:ama o Allah benim Rabbimdir, source:18:38} der.

Kaynaklar: 114:6 ٱلْجِنَّةِ ج ن ن B007; 114:1 أَعُوذُ ع و ذ B003; 114:1 بِرَبِّ ر ب ب B009; 114:1 بِرَبِّ ر ب ب B005; 114:1 بِرَبِّ ر ب ب B002; 114:6 ٱلْجِنَّةِ ج ن ن B014; 114:1 بِرَبِّ ر ب ب B008; 114:1 بِرَبِّ ر ب ب B007; 114:1 بِرَبِّ ر ب ب B013; 114:1 بِرَبِّ ر ب ب B012; 114:6 ٱلْجِنَّةِ ج ن ن B003; 114:6 ٱلْجِنَّةِ ج ن ن B011; 114:6 ٱلْجِنَّةِ ج ن ن B004; 114:1 أَعُوذُ ع و ذ B004

## Bir arada tutmak ve parçalamak

{ar:مَلِكِ, tr:melik, gloss:hükümdar, source:114:2} kelimesinin kökü sağlamlıktan başlar: sıkıca yoğrulmuş hamur, {ar:ملكت العجين إذا شددت عجنه, tr:melektu'l-acîne izâ şedettu acneh, gloss:hamuru sıkıca yoğurdum, source:"م ل ك,B001"}; bir arada duran duvar, {ar:حائط ليس له ملاك أي تماسك, tr:hâitun leyse lehû milâk, gloss:tutarlılığı olmayan duvar, source:"م ل ك,B001"}; ve krallık, elin tuttuğunda güçlü olmasından: {ar:والاسم الملك لأن يده فيه قوية صحيحة, tr:ve'l-ismu'l-mulk li-enne yedehû fîhi kaviyyetun sahîha, gloss:mülk denir, çünkü eli onun üzerinde güçlü ve sağlamdır, source:"م ل ك,B003"}. {ar:بِرَبِّ, tr:bi-rabbi, gloss:Rabbine, source:114:1} kelimesinin kökü toplar: kumar oklarını bir arada tutan kese {source:"ر ب ب,B010"}; binlerce insan ve tek olmak için toplanmış beş kabile, {ar:الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا, tr:er-ribbî vâhidu'r-ribbiyyîn, ve humu'l-ulûfu mine'n-nâs, gloss:ribbî, binlerce insan demek olan ribbiyyûn'un tekilidir; rabâb, bir araya gelmiş beş kabiledir, source:"ر ب ب,B004"}; sıkı düğüm {source:"ر ب ب,B016"}; tarafları bağlayan ahit, {ar:الربابة: العهد والميثاق, tr:er-ribâbe el-ahdu ve'l-mîsâk, gloss:ribâbe ahit ve sözleşmedir, source:"ر ب ب,B011"}; toplandığı için adını alan bol su {source:"ر ب ب,B013"}. Beş kez tekrar eden {ar:ٱلنَّاسِ, tr:en-nâs, gloss:insanlar, source:114:1} de bir topluluktur {source:"ء ن س,B001"}. Altıncı ayetin kökü ise halkın kalabalık yığınını adlandırır, ki orada tek tek kişiler kaybolur: {ar:جنان الناس معظمهم ويسمى السواد, tr:cenânu'n-nâsi mu'zamuhum ve yusemma's-sevâd, gloss:insanların cenânı onların büyük kısmıdır, karaltı da denir, source:"ج ن ن,B013"}.

Buna karşı kötülük kökü parçalar: {ar:شرشرة الشيء تشقيقه وتقطيعه, tr:şerşeretu'ş-şey'i teşkîkuhû ve takti'uh, gloss:bir şeyin şerşeresi onu yarıp parçalamaktır, source:"ش ر ر,B004"}; ve çekişmeyi adlandırır {source:"ش ر ر,B011"}. Sure şu süreci duyurur: çok olan bir bağlayıcı tarafından tek tutulur ya da parçalanır. İnsanlar birlikte anıldıkları üç ayette tek bir Rabbe, tek bir Meliğe, tek bir İlaha bağlıdır; fısıldayan bu bağı içeriden çözer.

Kuran'da sığınmanın sözlükteki açıklaması olan tutunmak fiili topluluğa emredilir: {ar:وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا وَلَا تَفَرَّقُوا۟, tr:va'tesımû bi-habli'llâhi cemîan ve lâ teferrakû, gloss:hep birlikte Allah'ın ipine tutunun, dağılmayın, source:3:103}, ve aynı ayette {ar:فَأَلَّفَ بَيْنَ قُلُوبِكُمْ, tr:fe-ellefe beyne kulûbikum, gloss:kalplerinizi birleştirdi, source:3:103}. Şeytanın amacı tersidir: {ar:إِنَّمَا يُرِيدُ ٱلشَّيْطَٰنُ أَن يُوقِعَ بَيْنَكُمُ ٱلْعَدَٰوَةَ وَٱلْبَغْضَآءَ فِى ٱلْخَمْرِ وَٱلْمَيْسِرِ, tr:innemâ yurîdu'ş-şeytânu en yûkia beynekumu'l-adâvete ve'l-bağdâe fi'l-hamri ve'l-meysir, gloss:şeytan içki ve kumarla aranıza düşmanlık ve kin sokmak ister, source:5:91}; kesenin bir arada tuttuğu kumar okları, bölen bir oyun olur. Toplanmış binler peygamberlerin yanında çarpışır: {ar:قَٰتَلَ مَعَهُۥ رِبِّيُّونَ كَثِيرٌۭ فَمَا وَهَنُوا۟, tr:kâtele meahû ribbiyyûne kesîrun fe-mâ vehenû, gloss:onunla birlikte pek çok ribbî savaştı ve gevşemediler, source:3:146}. Çok ilah, dünyanın parçalanmasıdır: {ar:لَوْ كَانَ فِيهِمَآ ءَالِهَةٌ إِلَّا ٱللَّهُ لَفَسَدَتَا, tr:lev kâne fîhimâ âlihetun illa'llâhu le-fesedetâ, gloss:yerde ve gökte Allah'tan başka ilahlar olsaydı ikisi de bozulurdu, source:21:22}; {ar:إِذًۭا لَّذَهَبَ كُلُّ إِلَٰهٍۭ بِمَا خَلَقَ, tr:izen le-zehebe kullu ilâhin bimâ halak, gloss:o zaman her ilah kendi yarattığını alıp giderdi, source:23:91}. Bağlayan ahit ise Rab sorusuyla kurulur: {ar:أَلَسْتُ بِرَبِّكُمْ ۖ قَالُوا۟ بَلَىٰ, tr:e-lestu bi-rabbikum, kâlû belâ, gloss:ben sizin Rabbiniz değil miyim? Evet, dediler, source:7:172}. Şeytan buna karşı yemin eder {source:7:21}. İkiz surede düğümlere üfleyenler anılır {source:113:4}; Rab kökünün sıkı düğümü bunun karşısında durur.

Kaynaklar: 114:2 مَلِكِ م ل ك B001; 114:2 مَلِكِ م ل ك B003; 114:1 بِرَبِّ ر ب ب B010; 114:1 بِرَبِّ ر ب ب B004; 114:1 بِرَبِّ ر ب ب B016; 114:1 بِرَبِّ ر ب ب B011; 114:1 بِرَبِّ ر ب ب B013; 114:1–6 ٱلنَّاسِ ء ن س B001; 114:6 ٱلْجِنَّةِ ج ن ن B013; 114:4 شَرِّ ش ر ر B004; 114:4 شَرِّ ش ر ر B011

## Gece, saklanan yıldızlar, güneş ve karanlıkta görülen ateş

{ar:ٱلْخَنَّاسِ, tr:el-hannâs, gloss:sinip çekilen, source:114:4} kökü yürüyen, gündüz güneş ışığı onları örtünce gizlenen ve batan gezegenleri adlandırır: {ar:الخنس الكواكب الخمسة التي تجري وتخنس في مجراها حتى يخفى ضوء الشمس وخنوسها اختفاؤها بالنهار, tr:el-hunnesu'l-kevâkibu'l-hamsetu'lletî tecrî ve tahnisu fî mecrâhâ, gloss:hunnes, akan ve akışında gizlenen beş yıldızdır; gizlenmeleri gündüz kaybolmalarıdır, source:"خ ن س,B002"}. Altıncı ayetin kökü gecenin her şeyi örtmesini söyler: {ar:أجنه الليل وجن عليه الليل إذا أظلم حتى يستره بظلمته, tr:ecennehu'l-leylu ve cenne aleyhi'l-leyl, gloss:gece onu örttü; karanlığıyla örtecek kadar karardı, source:"ج ن ن,B002"}. Üçüncü ayetin kökü güneşi adlandırır, çünkü ona tapılmıştır: {ar:والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها, tr:ve'l-ilâhetu'ş-şems, summiyet bi-zâlike li-enne kavmen kânû ya'budûnehâ, gloss:ilâhe güneştir; bir topluluk ona taptığı için böyle denmiştir, source:"ء ل ه,B001"}. Kötülük kökü güneşe sermeyi {source:"ش ر ر,B002"} ve ateşten uçan kıvılcımı adlandırır: {ar:الشرر ما تطاير من النار, tr:eş-şereru mâ tetâyera mine'n-nâr, gloss:şerer ateşten uçuşandır, source:"ش ر ر,B003"}. İnsan kökü ateşi uzaktan görmeyi, {ar:آنس من جانب يعني أبصر نارا, tr:ânese min cânib, gloss:bir yandan ateş gördü, source:"ء ن س,B002"}, ve gözbebeğinin karasında görünen küçük sureti adlandırır: {ar:إنسان العين المثال الذي يرى في السواد, tr:insânu'l-ayn el-misâlu'lledî yurâ fi's-sevâd, gloss:gözün insanı, gözün karasında görünen surettir, source:"ء ن س,B005"}. İnsan kökü kişiye eşlik eden her şeyi de bilir {source:"ء ن س,B003"}. Rab kökü yerinden ayrılmayanı {source:"ر ب ب,B007"}, Melik kökü de Allah'ın melekûtunu söyler {source:"م ل ك,B003"}.

Sahne şudur: gece her şeyi örter; gezegenler görünür, akar, gizlenir ve döner; bir zamanlar tapılan güneş doğar; bir ateş görülür, kıvılcımlar uçar; bir göz bakar; ve batan ışıklar arasında hangisinin Rab olduğu sorulur. Surenin üç unvanı bu soruya cevaptır: batmayan.

Kuran bu sahneyi İbrahim'in gecesinde kurar. Önce putlar ilah olarak anılır {source:6:74}, sonra {ar:وَكَذَٰلِكَ نُرِىٓ إِبْرَٰهِيمَ مَلَكُوتَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:ve kezâlike nurî ibrâhîme melekûte's-semâvâti ve'l-ard, gloss:böylece İbrahim'e göklerin ve yerin melekûtunu gösteriyorduk, source:6:75}, ve: {ar:فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ رَءَا كَوْكَبًۭا ۖ قَالَ هَٰذَا رَبِّى ۖ فَلَمَّآ أَفَلَ قَالَ لَآ أُحِبُّ ٱلْءَافِلِينَ, tr:fe-lemmâ cenne aleyhi'l-leylu raâ kevkeben, kâle hâzâ rabbî, fe-lemmâ efele kâle lâ uhibbu'l-âfilîn, gloss:gece onu örtünce bir yıldız gördü, "bu benim Rabbim" dedi; batınca "batanları sevmem" dedi, source:6:76}. Güneşte aynı tekrarlanır: {ar:فَلَمَّا رَءَا ٱلشَّمْسَ بَازِغَةًۭ قَالَ هَٰذَا رَبِّى هَٰذَآ أَكْبَرُ, tr:fe-lemmâ raa'ş-şemse bâzigaten kâle hâzâ rabbî hâzâ ekber, gloss:güneşi doğarken görünce "bu benim Rabbim, bu daha büyük" dedi, source:6:78}; o da batar, ve İbrahim yüzünü gökleri ve yeri yaratana çevirir {source:6:79}. Örten gece (cenne), bir yıldız, batmak ve Rab sorusu tek pasajdadır. Kuran güneşe secdeyi yasaklar {source:41:37}, ve Sebe halkının güneşe tapmasını şeytanın süslemesine bağlar: {ar:يَسْجُدُونَ لِلشَّمْسِ مِن دُونِ ٱللَّهِ وَزَيَّنَ لَهُمُ ٱلشَّيْطَٰنُ أَعْمَٰلَهُمْ, tr:yescudûne li'ş-şemsi min dûni'llâhi ve zeyyene lehumu'ş-şeytânu a'mâlehum, gloss:Allah'ı bırakıp güneşe secde ediyorlar; şeytan onlara işlerini süslemiş, source:27:24}. Yıldızlar şeytanlara karşı bekçidir: {ar:وَحِفْظًۭا مِّن كُلِّ شَيْطَٰنٍۢ مَّارِدٍۢ, tr:ve hifzan min kulli şeytânin mârid, gloss:ve her inatçı şeytana karşı koruma, source:37:7}; kulak hırsızını {ar:شِهَابٌۭ ثَاقِبٌۭ, tr:şihâbun sâkıb, gloss:delip geçen bir alev, source:37:10} izler. Cinler de bunu anlatır {source:72:9}. Karanlıkta görülen ateş Musa'nındır: {ar:إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:innî ânestu nâran lealli âtîkum minhâ bi-kabesin ev ecidu ale'n-nâri hudâ, gloss:ben bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösteren bulurum, source:20:10}. Kıvılcım ise cehennemin ateşinde büyür {source:77:32}. Sure-kardeşindeki oluk da gecedir: yemin {ar:وَٱلَّيْلِ إِذَا عَسْعَسَ, tr:ve'l-leyli izâ as'as, gloss:kararmaya başlayan geceye, source:81:17} ile sürer.

Kaynaklar: 114:4 ٱلْخَنَّاسِ خ ن س B002; 114:6 ٱلْجِنَّةِ ج ن ن B002; 114:3 إِلَٰهِ ء ل ه B001; 114:4 شَرِّ ش ر ر B002; 114:4 شَرِّ ش ر ر B003; 114:1–6 ٱلنَّاسِ ء ن س B002; 114:1–6 ٱلنَّاسِ ء ن س B005; 114:1–6 ٱلنَّاسِ ء ن س B003; 114:1 بِرَبِّ ر ب ب B007; 114:2 مَلِكِ م ل ك B003

## Av: mırıltı, sığınak, tetikteki hayvan, korunan bitki

{ar:ٱلْوَسْوَاسِ, tr:el-vesvâs, gloss:fısıldayan, source:114:4} avcının ve köpeklerinin hafif sesidir: {ar:همس الصائد والكلاب وأصوات الحلى وسواس, tr:hemsu's-sâidi ve'l-kilâbi ve asvâtu'l-hulî vesvâs, gloss:avcının ve köpeklerin fısıltısı, takıların sesleri vesvastır, source:"و س و س,B002"}; ve avın yattığı sazlıktaki hışırtıdır {source:"و س و س,B002"}. {ar:ٱلْخَنَّاسِ, tr:el-hannâs, gloss:sinip çekilen, source:114:4} kökü ceylanların sığınağını ve ceylanların kendisini adlandırır: {ar:الخنس مأوى الظباء؛ الخنس الظباء أنفسها, tr:el-hunnes me'vâ'z-zıbâ; el-hunnesu'z-zıbâu enfusuhâ, gloss:hunnes ceylanların sığınağıdır; hunnes ceylanların kendisidir, source:"خ ن س,B004"}; bütün sığırlar da basık burunludur {source:"خ ن س,B003"}. Rab kökü yaban sığırı sürüsünü {source:"ر ب ب,B014"}, sığınma kökü yeni doğurmuş ceylanları {source:"ع و ذ,B003"} ve dikenlerin dibinde otlayanların erişemediği bitkiyi bilir {source:"ع و ذ,B004"}. İnsan kökü korkutan bir şeyi sezip etrafına bakan hayvanı adlandırır: {ar:والاستئناس النظر وأحس بما رابه, tr:ve'l-isti'nâsu'n-nazar ve ehasse bimâ râbeh, gloss:isti'nâs bakmak ve kuşkulandıran şeyi sezmektir, source:"ء ن س,B002"}; ve evcili yabaninin karşısına koyar, ısırmayan köpeği ısıranın karşısına {source:"ء ن س,B003"}. Altıncı ayetin kökü saklanma yeridir {source:"ج ن ن,B017"}.

Sahne şudur: bir avcı alçak bir mırıltıyla sokulur; av sığınağında durur; tetikteki hayvan sezer ve etrafına bakar; bir bitki dikenler arasında erişilmez büyür. Fısıldayan mırıldanan avcıdır, ama adıyla sığınağında duran av gibi de saklanır. İnsanlar sezmesi gerekenlerdir. Sığınma, erişilemeyen yerdir.

Kuran avcıyı İblis'in ağzından verir: {ar:لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ, tr:le-ak'udenne lehum sırâtake'l-mustakîm, gloss:senin dosdoğru yolunun üstünde onları bekleyeceğim, source:7:16}, sonra {ar:ثُمَّ لَءَاتِيَنَّهُم مِّنۢ بَيْنِ أَيْدِيهِمْ وَمِنْ خَلْفِهِمْ وَعَنْ أَيْمَٰنِهِمْ وَعَن شَمَآئِلِهِمْ, tr:summe le-âtiyennehum min beyni eydîhim ve min halfihim ve an eymânihim ve an şemâilihim, gloss:sonra onlara önlerinden, arkalarından, sağlarından ve sollarından geleceğim, source:7:17}. Pusuya yatmak, sonra her yandan kuşatmak. Allah İblis'e seslenir: {ar:وَٱسْتَفْزِزْ مَنِ ٱسْتَطَعْتَ مِنْهُم بِصَوْتِكَ وَأَجْلِبْ عَلَيْهِم بِخَيْلِكَ وَرَجِلِكَ, tr:vestefziz meni'stata'te minhum bi-savtike ve eclib aleyhim bi-hayli-ke ve racilik, gloss:onlardan gücünün yettiğini sesinle ürküt, atlıların ve yayalarınla üstlerine sür, source:17:64}. Ses ile ürkütmek ve sürmek, avcının işidir. Kaçan av da Kuran'da görülür: {ar:كَأَنَّهُمْ حُمُرٌۭ مُّسْتَنفِرَةٌۭ, tr:keennehum humurun mustenfira, gloss:sanki ürkmüş yaban eşekleri, source:74:50}, {ar:فَرَّتْ مِن قَسْوَرَةٍۭ, tr:ferrat min kasvera, gloss:arslandan kaçan, source:74:51}.

Kaynaklar: 114:4 ٱلْوَسْوَاسِ و س و س B002; 114:4 ٱلْخَنَّاسِ خ ن س B004; 114:4 ٱلْخَنَّاسِ خ ن س B003; 114:1 بِرَبِّ ر ب ب B014; 114:1 أَعُوذُ ع و ذ B003; 114:1 أَعُوذُ ع و ذ B004; 114:5 ٱلنَّاسِ ء ن س B002; 114:5 ٱلنَّاسِ ء ن س B003; 114:6 ٱلْجِنَّةِ ج ن ن B017

## Yüzün çevresindeki sürü ve kıvılcım

{ar:شَرِّ, tr:şerr, gloss:kötülük, source:114:4} kökü sivrisineğe benzeyen, insanın yüzünü kaplayan ama ısırmayan bir böceği adlandırır: {ar:الشران شبيه بالبعوض يغشى وجه الإنسان ولا يعض وربما سموه الأذى, tr:eş-şirrân şebîhun bi'l-baûd yağşâ vechu'l-insâni ve lâ yeuddu ve rubbemâ semmevhu'l-ezâ, gloss:şirrân sivrisineğe benzer, insanın yüzünü kaplar, ısırmaz; ona bazen "eza" derler, source:"ش ر ر,B009"}. Kök ateşten uçuşan kıvılcımı da bilir {source:"ش ر ر,B003"}. Altıncı ayetin kökü uçarken vızıltısı artan sinekleri adlandırır: {ar:جن الذباب أي كثر صوته, tr:cenne'z-zubâb ey kesura savtuh, gloss:sinek "cenne" etti, yani sesi çoğaldı, source:"ج ن ن,B015"}. Fısıltı da hafif bir hışırtıdır {source:"و س و س,B002"}. Melik kökü arıların beyini bilir: {ar:مليك النحل يعسوبها, tr:melîku'n-nahli ya'sûbuhâ, gloss:arıların meliki onların beyidir, source:"م ل ك,B008"}.

Sahne şudur: küçük şeyler yüzün çevresinde dolaşır; onu kaplar, vızıldar, parlar, hışırdar ve ısırmaz. Fısıltı bu boyda bir zarardır: yer kaplar, örter, ama yaralamaz. Kişiyi meşgul eden ama kendiliğinden yaralayamayan bir şey olduğu için ona karşı sığınmak yeterlidir.

Kuran bu ölçüyü açıkça verir: {ar:إِنَّمَا ٱلنَّجْوَىٰ مِنَ ٱلشَّيْطَٰنِ لِيَحْزُنَ ٱلَّذِينَ ءَامَنُوا۟ وَلَيْسَ بِضَآرِّهِمْ شَيْـًٔا إِلَّا بِإِذْنِ ٱللَّهِ, tr:innema'n-necvâ mine'ş-şeytâni li-yahzune'llezîne âmenû ve leyse bi-dârrihim şey'en illâ bi-izni'llâh, gloss:gizli konuşma, inananları üzmek için şeytandandır; ama Allah'ın izni olmadan onlara hiçbir zarar veremez, source:58:10}. Ezanın zarar sayılmayan ölçüsü de geçer: {ar:لَن يَضُرُّوكُمْ إِلَّآ أَذًۭى, tr:len yedurrûkum illâ ezâ, gloss:size eziyetten başka zarar veremezler, source:3:111}. Sözlükteki böceğin adı "eza", Kuran'daki ifadede de zararın altındaki rahatsızlıktır.

Kaynaklar: 114:4 شَرِّ ش ر ر B009; 114:4 شَرِّ ش ر ر B003; 114:6 ٱلْجِنَّةِ ج ن ن B015; 114:4 ٱلْوَسْوَاسِ و س و س B002; 114:2 مَلِكِ م ل ك B008

## Örtülen akıl

Altıncı ayette duran biçim, {ar:ٱلْجِنَّةِ, tr:el-cinne, gloss:cinler, source:114:6}, aynı zamanda deliliğin adıdır: {ar:الجنة الجنون وذلك أنه يغطي العقل, tr:el-cinnetu'l-cunûn, ve zâlike ennehû yuğattı'l-akl, gloss:cinne deliliktir, çünkü aklı örter, source:"ج ن ن,B006"}; {ar:الجنون حائل بين النفس والعقل, tr:el-cunûnu hâilun beyne'n-nefsi ve'l-akl, gloss:delilik nefisle akıl arasına giren bir perdedir, source:"ج ن ن,B006"}. Sığınma kökünün muskası da "korkuya ya da deliliğe karşı" takılır {source:"ع و ذ,B002"}. Fısıltı kötü bir geçici düşüncedir: {ar:الوسوسة الخطرة الرديئة, tr:el-vesvesetu'l-hatratu'r-radîe, gloss:vesvese kötü bir düşüncedir, source:"و س و س,B001"}. Söz kökü birine yalan söz yüklemeyi adlandırır {source:"ق و ل,B005"}.

Sahne şudur: bir akıl örtülür ya da bir perde ile nefsinden ayrılır; ona karşı bir sığınma söylenir. Ayetin anlamı "cinler"dir; ama aynı biçimde aklı örten şey de duyulur, ve fısıltının en uç sonucu bu olur: kişiyle aklı arasına giren bir perde.

Kuran bu biçimi elçinin savunmasında kullanır: {ar:مَا بِصَاحِبِهِم مِّن جِنَّةٍ ۚ إِنْ هُوَ إِلَّا نَذِيرٌۭ مُّبِينٌ, tr:mâ bi-sâhibihim min cinne, in huve illâ nezîrun mubîn, gloss:arkadaşlarında hiçbir delilik yoktur; o yalnızca apaçık bir uyarıcıdır, source:7:184}; {ar:أَمْ يَقُولُونَ بِهِۦ جِنَّةٌۢ, tr:em yekûlûne bihî cinne, gloss:yoksa "onda delilik var" mı diyorlar, source:23:70}. Delilik ve yalan isnadı yan yana sorulur: {ar:أَفْتَرَىٰ عَلَى ٱللَّهِ كَذِبًا أَم بِهِۦ جِنَّةٌۢ, tr:efterâ ala'llâhi keziben em bihî cinne, gloss:Allah'a karşı yalan mı uydurdu, yoksa onda delilik mi var, source:34:8}. Aynı ret tek bir pasajda hannâs yıldızlarının yeminiyle başlar {source:81:15}, {ar:وَمَا صَاحِبُكُم بِمَجْنُونٍۢ, tr:ve mâ sâhibukum bi-mecnûn, gloss:arkadaşınız deli değildir, source:81:22} der, ve {source:81:25} ile şeytanın sözünü reddeder. Bir başka yerde: {ar:فَمَآ أَنتَ بِنِعْمَتِ رَبِّكَ بِكَاهِنٍۢ وَلَا مَجْنُونٍ, tr:fe-mâ ente bi-ni'meti rabbike bi-kâhinin ve lâ mecnûn, gloss:sen Rabbinin nimeti sayesinde ne kâhinsin ne deli, source:52:29}. Şeytanların ayarttığı kişi de şaşkındır {source:6:71}.

Kaynaklar: 114:6 ٱلْجِنَّةِ ج ن ن B006; 114:1 أَعُوذُ ع و ذ B002; 114:4 ٱلْوَسْوَاسِ و س و س B001; 114:1 قُلْ ق و ل B005

## Buluşmalar

İlk buluşma göğüstedir. Örten kök göğsün içinde çalışır: {ar:أجننت الشيء في صدري أكننته, tr:ecnentu'ş-şey'e fî sadrî, gloss:o şeyi göğsümde gizledim, source:"ج ن ن,B001"}. Görünen ve örtülü imgesi ile göğüs imgesi burada tek sahne olur: görünen insanların içinde, kemik kafesin altında, gizli kalp vardır; örtülü olan, örtülü odaya girer. Kuran'ın göğüslerini bükerek saklananları {source:11:5} da bu sahneye aittir: ne kadar örtünseler de göğüslerin özü bilinir. Sığınma imgesindeki bütün dış örtüler (göğüs giysisi, zırh, kalkan) bu odanın dışında kalır; içerdeki fısıltıya karşı yalnız söylenen söz işler.

İkinci buluşma sözdedir. Sözlük, söylenen sözü "telaffuzla dışarı çıkarılan" diye tanımlarken kullandığı fiili {source:"ق و ل,B001"} kötülük kökünün "ortaya çıkarmak" anlamında da kullanır {source:"ش ر ر,B008"}. Sure böylece iki çıkarma arasında kurulur: sığınma sözü içten dışa çıkar, fısıltının amacı ise örtülüyü açığa çıkarmaktır {source:7:20}. Söz ile çekilme de buluşur: {ar:الشيطان يوسوس فإذا ذكر الله خنس, tr:eş-şeytânu yuvesvisu fe-izâ zukira'llâhu hanes, gloss:şeytan fısıldar, Allah anılınca çekilir, source:"خ ن س,B001"}. "De" emri bu anmayı dile getirir; "sinip çekilen" sıfatı onun sonucunu adlandırır. Söz ile sığınma okunan muskada birleşir {source:"ع و ذ,B002"}: emredilen cümle, dilde taşınan korunaktır.

Üçüncü buluşma gece ile çekilmededir. Hannâs kökü hem geri çekilmeyi hem gündüz gizlenip yörüngesinde dönen yıldızları adlandırır; Kuran onlara yemin eden pasajda deliliği ve şeytan sözünü reddeder {source:81:15}. İbrahim'in gecesinde batanlara karşı {source:6:76} Rab kökünün "yerinden ayrılmayan" anlamı {source:"ر ب ب,B007"} durur. Fısıldayan gidip gelir; Rab batmaz.

Dördüncü buluşma unvanlar ile sığınmadadır: {ar:عاذ فلان بربه, tr:âze fulânun bi-rabbih, gloss:Rabbine sığındı, source:"ع و ذ,B001"}. Fiil ile unvan tek ifadede durur. Ana ve yavru imgesi bu bağa sıcaklık verir: aynı iki kök yeni doğurmuş anneyi adlandırır, ve Kuran'da bir anne yeni doğan kızını Rabbine sığındırır, Rab da onu bir bitki gibi büyütür {source:3:37}. Bağlama imgesi aynı sığınmayı topluluğa genişletir: sığınmanın açıklaması olan tutunmak {source:3:103} bütün insanları tek ipte toplar; kötülük kökü ise parçalar.

Surenin hareketi bu buluşmalarla taşınır. İlk üç ayet aynı insanları üç unvan altında, bir arada ve görünür olarak toplar; dördüncü ayet görünmeyen ve gidip gelen bir fısıltıyı adlandırır; beşinci ayet onu en içteki odaya, göğse yerleştirir; altıncı ayet kaynağını hem örtülülere hem görünenlere açar. Sığınma sözü bu yolun tersinden ilerler: içten dışa, dilde söylenir, ve yerinden ayrılmayan bir Rabbe tutunur.

