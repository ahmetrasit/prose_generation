Focus: 91:5. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/91_5/D.r13/context.md =====
# 91:5 — focus

وَٱلسَّمَآءِ وَمَا بَنَىٰهَا

Anchor translation (canonical reading, reference only):

Göğe ve onu kurana,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَٱلسَّمَآءِ | سَمَآء | س م و | CONJ;DET;N |
| 2 | وَمَا | مَا |  | CONJ;REL |
| 3 | بَنَىٰهَا | بَنَىٰ | ب ن ي | V;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 91 — full text (context; no pericope)

- 91:1 وَٱلشَّمْسِ وَضُحَىٰهَا
- 91:2 وَٱلْقَمَرِ إِذَا تَلَىٰهَا
- 91:3 وَٱلنَّهَارِ إِذَا جَلَّىٰهَا
- 91:4 وَٱلَّيْلِ إِذَا يَغْشَىٰهَا
- 91:5 ◀ focus وَٱلسَّمَآءِ وَمَا بَنَىٰهَا
- 91:6 وَٱلْأَرْضِ وَمَا طَحَىٰهَا
- 91:7 وَنَفْسٍۢ وَمَا سَوَّىٰهَا
- 91:8 فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا
- 91:9 قَدْ أَفْلَحَ مَن زَكَّىٰهَا
- 91:10 وَقَدْ خَابَ مَن دَسَّىٰهَا
- 91:11 كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ
- 91:12 إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
- 91:13 فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا
- 91:14 فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا
- 91:15 وَلَا يَخَافُ عُقْبَٰهَا


===== _commentary/v16/work/91_5/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س م و (root_000745) — identity root of وَٱلسَّمَآءِ (w1)

- **B001** fiziksel ya da toplumsal yükselme — yükselme, yücelme · yükselmek, yücelmek · bakışı yukarı yönelmek · toplumdaki yeri ve değeri yükselmiş olmak · gururla başını ve bakışını kaldırmak
  أصل يدل على العلو؛ سموت إذا علوت (maqayis)؛ سما الشيء يسمو سموا أي ارتفع (ayn)؛ السمو الارتفاع والعلو (sihah)؛ سما الشيء يسمو سموا وهو ارتفاعه، ويقال للحسيب والشريف قد سما (tahdhib)؛ أصله من السمو وهو الذي به رفع ذكر المسمى (mufradat)
- **B002** yükselerek uzaktan beliren görünüş — uzakta yükselip görünür olmak · bir şeyin yüksekte görünen gövdesi veya dış çizgisi · ayın ince yayının ufuktan yükselen görünüşü
  سما لي شخص ارتفع حتى استثبته؛ سماوة الهلال وكل شيء شخصه (maqayis)؛ سما لي شيء؛ سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا (ayn)؛ سما لي شخص؛ سماوة كل شيء شخصه (sihah)؛ سما لي شيء؛ سماوته أي شخصه؛ سماوة الهلال شخصه (tahdhib)؛ السماوة الشخص العالي؛ وسما لي شخص (mufradat)
- **B003** erkek devenin dişi deve sürüsüne atılıp aralarına girmesi [kalıp] — erkek devenin dişi deve sürüsüne atılıp aralarına girmesi
  سما الفحل سطا على شوله سماوة (maqayis)؛ سما الفحل إذا تطاول على شوله (ayn;tahdhib)؛ سما الفحل إذا سطا على شوله سماوة (sihah)؛ سما الفحل على الشول سماوة لتخلله إياها (mufradat)
- **B004** üstteki gök veya örtü ve buna bağlı üstten gelen ya da üstte bulunan şeyler — gök, tavan veya bir şeyin üst yanı · yağmur · bulut · yağmurla çıkan veya yerden yükselen bitki · atın sırtı veya üst yanı · evin tavanı · her şeyin en üst yanı
  العرب تسمى السحاب سماء والمطر سماء؛ السماء سقف البيت وكل عال مطل سماء؛ يسموا النبات سماء (maqayis)؛ السماء كل ما علاك فأظلك؛ السماء المطر؛ السماء ظهر الفرس؛ سماوة البيت سقفه (sihah)؛ السماء سقف كل شيء وكل بيت؛ السماء السحاب؛ السماء المطر (tahdhib)؛ سماء كل شيء أعلاه؛ سمي المطر سماء؛ سمي النبات سماء (mufradat)
- **B005** ad, adlandırma ve ad ya da nitelik bakımından denklik — bir şeyi tanıtan ad · birine bir ad vermek veya onu o adla çağırmak · bir adı edinmek ve o adla anılmak · aynı adı taşıyan kişi, adaş · aynı adı veya niteliği hak eden denk · varlıkları tanıtan tekli veya birleşik sözler ve anlamlar
  أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى (maqayis)؛ الاسم أصل تأسيسه السمو؛ سميت وأسميت وتسميت (ayn)؛ سميت فلانا زيدا؛ هذا سمي فلان؛ الاسم مشتق من سموت لأنه تنويه ورفعة (sihah)؛ الاسم مشتق من السمو وهو الرفعة؛ تنويها على الدلالة على المعنى (tahdhib)؛ الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى؛ سميا أي نظيرا له يستحق اسمه (mufradat)
- **B006** av için ıssız araziye çıkma ve buna bağlı avcı kullanımları — avlanmak için kır ve çöl arazisine çıkmak · avcılar · av hayvanını bulup avlamak üzere aramak · avcının sıcak zeminde beklerken giydiği koruyucu çorap
  خرج القوم للصيد في قفار الأرض وصحاريها قلت سموا وهم السماة أي الصيادون (ayn;tahdhib)؛ السماة الصيادون؛ سموا واستموا إذا خرجوا للصيد (sihah)؛ يستمي الوحش أي يطلبها؛ المسماة جورب الصياد (tahdhib)
- **B007** yarışma, övünerek boy ölçüşme ve karşı koyma — birbiriyle yarışmak ve karşı koymak · övünerek yarışma, boy ölçüşme ve karşı koyma · kimsenin kendisiyle yarışamadığı veya boy ölçüşemediği kişi
  فلان لا يسامى؛ تساموا أي تباروا؛ قد علا من ساماه (sihah)؛ معنى تساميها تباريها وتعارضها؛ المساماة المفاخرة (tahdhib)
- **B008** insanlar arasında yayılan iyi ün — insanlar arasında yayılan iyi ün veya iyi söz
  ذهب صيته في الناس وسماه، أي صوته في الخير لا في الشر (tahdhib)

## ب ن ي (root_000156) — identity root of بَنَىٰهَا (w3)

- **B001** parçaları birleştirerek yapı kurma, kurulan yapı ve kurmaya olanak sağlama — parçaları birleştirip yapı kurmak · kurulmuş yapı; duvar, ev veya gök · çok sayıda saray yapmak · bir ev yapmak ve edinmek · birine ev yapması için ev ya da gerekli gereci vermek · keçi sürüsü çadır kurmaya yetecek kıl ve topluluk sağlamaz
  بناء الشيء بضم بعضه إلى بعض (maqayis)؛ بنى البناء يبني بنيا وبناء (ayn;tahdhib;mufradat)؛ بنى فلان بيتا من البنيان وبنى قصورا (sihah)؛ البنيان الحائط (sihah)؛ البناء اسم لما يبنى بناء (mufradat)؛ السماء بنيناها (mufradat)؛ أبنيت فلانا بيتا إذا أعطيته بيتا يبنيه (sihah;tahdhib)
- **B002** kuruluş biçimi ve doğuştan yapı — kuruluş biçimi; doğuştan beden yapısı
  فلان صحيح البنية أي الفطرة (sihah)؛ البنية الهيئة التي بني عليها (tahdhib)
- **B003** Kabe, Allah'ın Evi veya Mekke için özel ad — Kabe, Allah'ın Evi veya Mekke için kullanılan ad
  تسمى مكة البنية (maqayis)؛ البنية الكعبة (ayn;sihah;tahdhib)؛ البنية يعبر بها عن بيت الله (mufradat)
- **B004** deriden örtü, çadırımsı kap, yaygı veya saklama kabı — deriden çadırımsı örtü, yaygı, hasır ya da kap · yağmurdan korunmak ya da yere sermek için yaygı · otururken bacaklarını birbirinden ayırmak
  المبناة كهيئة الستر؛ كهيئة القبة تجلل بيتا عظيما (ayn)؛ المبناة النطع؛ ويقال هي العيبة (sihah;tahdhib)؛ المبناة قبة من أدم (tahdhib)؛ المبناة حصير أو نطع يبسطه التاجر على بيعه (tahdhib)؛ بسطنا له بناء أي نطعا (tahdhib)
- **B005** kirişine aşırı yapışan kusurlu yay — kirişine yapışıp onu kopma sınırına getiren kusurlu yay · kirişine yapışan kusurlu yay için bölgesel biçim
  قوس بانية وهي التي بنت على وترها (maqayis;sihah;tahdhib)؛ يكاد وترها ينقطع للصوقه بها (maqayis;tahdhib)؛ طيئ تقول قوس باناة (maqayis;tahdhib)؛ البائنة التي بانت من وترها وكلاهما عيب (tahdhib)
- **B006** gelini yeni evine götürme, eşle birleşme ve bunu yapan damat — gelini yeni evine götürmek veya eşiyle birleşmek · düğün sonrası eşiyle birleşen damat
  بنى على أهله بناء أي زفها (sihah)؛ الداخل بأهله كان يضرب عليها قبة ليلة دخوله بها (sihah)؛ الباني العروس الذي بنى على أهله (tahdhib)؛ بنى فلان على أهله وقد زفها (tahdhib)؛ العامة تقول بنى بأهله وليس من كلام العرب (sihah;tahdhib)
- **B007** oğul ve kız bağı, çocuk edinme ve kaynağa dayalı adlandırma — oğul; bir kaynaktan çıkan veya onun yetiştirdiği kimse · kız çocuk · oğullar, çocuklar ve kızlar · oğulluk ve çocukluk bağı · birini oğul edinmek veya oğulluğunu ileri sürmek · bir şeye kaynağı, yetişmesi, hizmeti ya da sürekli bağlılığı nedeniyle bağlanan kimse
  الابن أصله بنو (sihah;mufradat)؛ البنوة مصدر الابن (tahdhib)؛ تبنيت فلانا إذا اتخذته ابنا (sihah)؛ تبنيته إذا ادعيت بنوته (tahdhib)؛ سماه بذلك لكونه بناء للأب (mufradat)؛ كل ما يحصل من جهة شيء أو من تربيته أو بتفقده أو كثرة خدمته له أو قيامه بأمره هو ابنه (mufradat)؛ فلان ابن الحرب وابن السبيل وابن الليل وابن العلم (mufradat)؛ بنت فلان وابنة فلان وبنات (sihah;tahdhib;mufradat)
- **B008** küçük, dallanmış veya yerden çıkan şeylere çocuk adı verme — ana yoldan ayrılan küçük yollar · kız çocukların oynadığı küçük insan biçimli oyuncaklar · tapınma yerindeki çakıl taşları · bir çakıl taşı ile bir ot türü
  بنيات الطريق هي الطرق الصغار تتشعب من الجادة (sihah)؛ البنات التماثيل الصغار التي تلعب بها الجواري (sihah)؛ إحدى بنات مساجد الله كأنه جعله حصاة (sihah)؛ بنت الأرض الحصاة وابن الأرض ضرب من البقل (sihah)؛ يقال لكل ما يحصل من جهة شيء هو ابنه (mufradat)
- **B009** kaburgalar veya ev direkleri; yerleşip huzur bulma — göğüs kafesi kaburgaları veya ev direkleri · bir yere yerleşip huzur bulmak
  البواني أضلاع الزور؛ ألقى بوانيه إذا أقام بالمكان واطمأن؛ البوائن جمع البوان وهو اسم كل عمود في البيت
- **B010** yiyeceğin eti büyütüp besili kılması — yiyeceğin eti büyütüp besili kılması · otururken bacaklarını birbirinden ayırmak
  بنى لحم فلان طعامه يبنيه بناء إذا عظم من الأكل؛ بنى السويق لحمها؛ كما بنى بخت العراق القت

## ECHO و س م (root_001650) — for وَٱلسَّمَآءِ (w1): withheld observed target; not identity

- **B001** tanıtıcı fiziksel iz koyma, iz ve araç — bir şeyi tanıtıcı bir iz bırakarak işaretlemek · yakma veya kesme yoluyla bırakılmış tanıtıcı iz · tanınmayı sağlayan görünür işaret · üzerine tanıtıcı işaret konmuş · hayvan damgalamaya yarayan kızgın demir · kendine tanınacağı bir işaret edinmek · alt bölümü pirinçle süslenmiş zırh
  ووسمت الشيء وسما: أثرت فيه بسمة (maqayis;sihah)؛ الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي (ayn)؛ أثر كية، إما كية أو قطع في أذنه أو قرمة تكون علامة له (tahdhib)؛ الميسم المكواة أو الشيء الذي يوسم به الدواب (ayn;sihah;tahdhib)
- **B002** belirtiden karakter veya durum sezme — bir kimsede iyilik ya da kötülük belirtisi görüp niteliğini sezmek · duruma işaret eden belirtileri okuyup sonuç çıkaranlar · üzerinde iyilik ya da kötülük belirtisi bulunan
  الناظرين في السمة الدالة (maqayis)؛ توسمت فيه الخير والشر أي رأيت فيه أثرا (ayn)؛ فلان موسوم بالخير، وقد توسمت فيه الخير أي تفرست (sihah)؛ توسمت في فلان خيرا أي رأيت فيه أثرا منه، وتوسمت فيه الخير أي تفرست (tahdhib)
- **B003** toprağı bitkilendiren yılın ilk yağmuru — toprağı bitkilendiren yılın veya ilkbaharın ilk yağmuru · ilk yağmuru alıp etkisini taşıyan toprak · ilk yağmurun çıkardığı otu aramak
  الوسمى أول المطر لأنه يسم الأرض بالنبات (maqayis)؛ الوسمي أول مطر السنة يسم الأرض بالنبات، وأرض موسومة أصابها الوسمي (ayn)؛ الوسمي مطر الربيع الأول لأنه يسم الأرض بالنبات، والأرض موسومة (sihah)؛ سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة (tahdhib)
- **B004** belirlenmiş toplu buluşma zamanı ve yeri — kutsal ziyaret için belirlenmiş toplu buluşma zamanı ve yeri · eski Arap pazarlarının belirli toplanma zamanları ve yerleri · belirlenmiş toplu buluşmaya katılmak
  وسمى موسم الحاج موسما لأنه معلم يجتمع إليه الناس (maqayis)؛ موسم الحج موسما لأنه معلم يجتمع فيه وكذلك مواسم أسواق العرب (ayn;tahdhib)؛ موسم الحاج مجمعهم، سمي بذلك لأنه معلم يجتمع إليه (sihah)؛ وسم الناس: شهدوا الموسم (maqayis;sihah)
- **B005** kişide görünen yerleşik güzellik ve zarafet — güzellik; kişide görünen hoşluk · yüzü güzel ve hoş görünümlü · güzel ve hoş görünümlü kadın · üzerinde güzellik ve zarafet etkisi bulunan kadın · kişide görünen güzellik ve hoşluk · güzelleşmek ve hoş bir görünüş kazanmak · birini güzellikte geçmek
  فلانة ذات ميسم إذا كان عليها أثر الجمال، والوسامة الجمال (maqayis)؛ ذات ميسم وجمال وميسمها أثر الجمال فيها وهي وسيمة (ayn)؛ الميسم الجمال، وفلان وسيم أي حسن الوجه، ووسم الرجل وسامة ووساما (sihah)؛ فلانة لذات ميسم وميسمها أثر الجمال والعتق، والوسامة والميسم الحسن، والوسيم الثابت الحسن (tahdhib)
- **B006** yaprakları boya olarak kullanılan bitki — yaprakları boya olarak kullanılan bitki veya küçük ağaç
  الوسم والوسمة الواحدة شجرة ورقها خضاب (ayn;tahdhib)؛ الوسمة والعظلم يختضب به (sihah)

===== _commentary/v16/out/s091/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 91:5, and ## Buluşmalar) =====
## Gök ve yerden kurulan ev, içindeki üçüncü yapı: nefis

Beşinci, altıncı ve yedinci ayetler tek bir inşa işini üç fiille anlatır: {ar:وَٱلسَّمَآءِ وَمَا بَنَىٰهَا, tr:ve's-semâi ve mâ benâhâ, gloss:göğe ve onu kurana andolsun, source:91:5}; {ar:وَٱلْأَرْضِ وَمَا طَحَىٰهَا, tr:ve'l-ardı ve mâ tahâhâ, gloss:yere ve onu yayana andolsun, source:91:6}; {ar:وَنَفْسٍۢ وَمَا سَوَّىٰهَا, tr:ve nefsin ve mâ sevvâhâ, gloss:nefse ve onu düzenleyip dengeleyene andolsun, source:91:7}.

İlk fiil parçaları birbirine katarak bir bütün kurmaktır: {ar:بناء الشيء بضم بعضه إلى بعض, tr:binâu'ş-şey'i bi-dammi ba'dihî ilâ ba'd, gloss:bir şeyi kurmak, parçalarını birbirine katmaktır, source:"ب ن ي,B001"}. Kurulan gök, evin tavanıdır: {ar:السماء سقف البيت وكل عال مطل سماء, tr:es-semâu sakfu'l-beyt, ve kullu âlin mutıllin semâ', gloss:semâ evin tavanıdır; yukarıda duran ve üstte sarkan her şey semâdır, source:"س م و,B004"}. Bir başka tanım da onun gölge veren yanını öne çıkarır: {ar:السماء كل ما علاك فأظلك, tr:es-semâu kullu mâ alâke fe-ezallek, gloss:semâ, üstüne yükselip seni gölgeleyen her şeydir, source:"س م و,B004"}. Kur'an göğe aynı adı verir: {ar:وَجَعَلْنَا ٱلسَّمَآءَ سَقْفًۭا مَّحْفُوظًۭا, tr:ve ce'alne's-semâe sakfen mahfûzâ, gloss:göğü korunmuş bir tavan yaptık, source:21:32}. Bir yeminde de onu böyle anar: {ar:وَٱلسَّقْفِ ٱلْمَرْفُوعِ, tr:ve's-sakfi'l-merfû', gloss:yükseltilmiş tavana andolsun, source:52:5}. Bina kökü yalnızca taş duvarı değil, deriden kurulan çadırı da adlandırır: {ar:المبناة قبة من أدم, tr:el-mebnâtu kubbetun min edem, gloss:mebnât, deriden yapılmış kubbeli çadırdır, source:"ب ن ي,B004"}. Aynı kök yere serilen bir deri sergiyi de anlatır: {ar:بسطنا له بناء أي نطعا, tr:basatnâ lehu binâen, ey nat'an, gloss:ona bir binâ serdik, yani deri bir sergi, source:"ب ن ي,B004"}.

Altıncı ayetteki yer, bu tavanın karşısındaki yüzdür: {ar:الأرض الجرم المقابل للسماء, tr:el-ardu'l-cirmu'l-mukâbilu li's-semâ', gloss:yer, göğün karşısındaki cisimdir, source:"ء ر ض,B001"}. Yerin kökü kalın bir yer döşemesini de adlandırır: {ar:الإراض بساط ضخم من وبر أو صوف, tr:el-irâdu bisâtun dahmun min veberin ev sûf, gloss:irâd, deve tüyünden ya da yünden kalın bir yaygıdır, source:"ء ر ض,B005"}. Yerin fiili de yaymaktır: {ar:الطحو كالدحو وهو البسط, tr:et-tahvu ke'd-dahv, ve huve'l-bast, gloss:tahv, dahv gibidir; yaymak demektir, source:"ط ح و,B001"}. Aynı kökte geniş bir gölgelik çadır da vardır: {ar:مظلة مطحوة ومطحية وطاحية وهو الضخم, tr:mizalletun mathuvvetun ve mathiyyetun ve tâhiyetun, ve huve'd-dahm, gloss:yayılmış, iri bir gölgelik çadır, source:"ط ح و,B005"}. Böylece iki ayet birlikte bir ev kurar: üstte kubbe gibi bir tavan, altta serilmiş bir yaygı.

Kur'an bu evi açıkça kurar. Allah bütün insanlara şöyle seslenir: {ar:جَعَلَ لَكُمُ ٱلْأَرْضَ فِرَٰشًۭا وَٱلسَّمَآءَ بِنَآءًۭ, tr:ce'ale lekumu'l-arda firâşen ve's-semâe binâen, gloss:yeri sizin için bir döşek, göğü bir bina yaptı, source:2:22}. Başka bir yerde aynı ikiliyi kendi ağzından anlatır: {ar:وَٱلسَّمَآءَ بَنَيْنَٰهَا بِأَيْي۟دٍۢ, tr:ve's-semâe beneynâhâ bi-eydin, gloss:göğü güçle kurduk, source:51:47}; {ar:وَٱلْأَرْضَ فَرَشْنَٰهَا فَنِعْمَ ٱلْمَٰهِدُونَ, tr:ve'l-arda ferasnâhâ fe-ni'me'l-mâhidûn, gloss:yeri döşedik; ne güzel döşeyicileriz, source:51:48}. Nûh kavmine yeri bir yaygı olarak hatırlatır: {ar:وَٱللَّهُ جَعَلَ لَكُمُ ٱلْأَرْضَ بِسَاطًۭا, tr:va'llâhu ce'ale lekumu'l-arda bisâtâ, gloss:Allah yeri sizin için bir yaygı yaptı, source:71:19}. Nebe' Suresi'ndeki iki ayet bu evi bir çadır gibi kurar: {ar:أَلَمْ نَجْعَلِ ٱلْأَرْضَ مِهَٰدًۭا, tr:e lem nec'ali'l-arda mihâdâ, gloss:yeri bir beşik döşeği yapmadık mı, source:78:6}; {ar:وَٱلْجِبَالَ أَوْتَادًۭا, tr:ve'l-cibâle evtâdâ, gloss:dağları da kazıklar, source:78:7}. Kazık, çadırı yere tutturan şeydir. İnkârcılara da bu tavanın kusursuzluğu gösterilir: {ar:كَيْفَ بَنَيْنَٰهَا وَزَيَّنَّٰهَا وَمَا لَهَا مِن فُرُوجٍۢ, tr:keyfe beneynâhâ ve zeyyennâhâ ve mâ lehâ min furûc, gloss:onu nasıl kurduk, nasıl süsledik; onda hiçbir yarık yok, source:50:6}. Nâziât Suresi'nde Allah dirilişi inkâr edenlere sorar ve bu surenin fiillerini aynı sırayla, aynı kafiyeyle dizer: {ar:ءَأَنتُمْ أَشَدُّ خَلْقًا أَمِ ٱلسَّمَآءُ ۚ بَنَىٰهَا, tr:e entum eşeddu halkan emi's-semâ', benâhâ, gloss:sizin yaratılışınız mı daha zor, yoksa göğün mü? Onu kurdu, source:79:27}; {ar:رَفَعَ سَمْكَهَا فَسَوَّىٰهَا, tr:rafe'a semkehâ fe-sevvâhâ, gloss:tavanını yükseltti ve onu düzenledi, source:79:28}; {ar:وَٱلْأَرْضَ بَعْدَ ذَٰلِكَ دَحَىٰهَآ, tr:ve'l-arda ba'de zâlike dehâhâ, gloss:yeri de ardından yaydı, source:79:30}.

Son satırda gök için kullanılan "sevvâhâ", bu surede yedinci ayette nefis için gelir. Bitirme işi şudur: {ar:سويت الشيء فاستوى, tr:sevveytu'ş-şey'e fe'stevâ, gloss:şeyi düzledim, o da düzgün hale geldi, source:"س و ي,B002"}. Sonuç kusursuz bir biçimdir: {ar:السوي الذي سوى الله خلقه لا دمامة فيه ولا داء, tr:es-seviyyu'llezî sevva'llâhu halkahu, lâ demâmete fîhi ve lâ dâ', gloss:seviyy, Allah'ın yaratılışını düzgün kıldığı kişidir; onda ne çirkinlik ne hastalık vardır, source:"س و ي,B002"}. Bu üçüncü yapı canlı bir nefistir: {ar:النفس الروح الذي به حياة الجسد وكل إنسان نفس, tr:en-nefsu'r-rûhu'llezî bihî hayâtu'l-cesed, ve kullu insânin nefs, gloss:nefs, bedenin kendisiyle yaşadığı ruhtur; her insan bir nefistir, source:"ن ف س,B011"}. Bina kökü de nefse uzanır. İnsanın yaratılıştan gelen yapısının adı bu kökten gelir: {ar:البنية الهيئة التي بني عليها, tr:el-binyetu'l-hey'etu'lletî buniye aleyhâ, gloss:binye, kişinin üzerine kurulduğu yapıdır, source:"ب ن ي,B002"}; {ar:فلان صحيح البنية أي الفطرة, tr:fulânun sahîhu'l-binye, eyi'l-fıtra, gloss:falanın binyesi sağlam, yani yaratılışı, source:"ب ن ي,B002"}. Göğüs kafesinin kaburgaları da bu kökle anılır ve evin direkleri gibi görülür: {ar:البواني أضلاع الزور, tr:el-bevânî edlâ'u'z-zevr, gloss:bevânî, göğüs kafesinin kaburgalarıdır, source:"ب ن ي,B009"}; {ar:البوائن جمع البوان وهو اسم كل عمود في البيت, tr:el-bevâinu cem'u'l-buvân, ve huve'smu kulli amûdin fi'l-beyt, gloss:bevâin, buvânın çoğuludur; çadırdaki her direğin adıdır, source:"ب ن ي,B009"}.

Kur'an insanı aynı fiille anlatır. Allah insana döner ve şöyle der: {ar:ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ, tr:ellezî halekake fe-sevvâke fe-adelek, gloss:seni yaratan, seni düzenleyen ve dengeli kılan, source:82:7}. İnsanın yaratılışı anlatılırken de aynı fiil gelir: {ar:ثُمَّ سَوَّىٰهُ وَنَفَخَ فِيهِ مِن رُّوحِهِۦ, tr:summe sevvâhu ve nefaha fîhi min rûhih, gloss:sonra onu düzenledi ve ona kendi ruhundan üfledi, source:32:9}. Düz bir anlatımda yemin gökten insana atlıyormuş gibi görünür. Fiiller ise atlamanın olmadığını gösterir. Aynı usta, aynı sırayla, aynı bitirme fiiliyle üçüncü bir yapı kurar. Nefis bu evin üçüncü odasıdır ve tavanın "sevvâhâ"sı onun da "sevvâhâ"sıdır.

Kaynaklar: 91:5 ٱلسَّمَآءِ س م و B004; 91:5 بَنَىٰهَا ب ن ي B001; 91:5 بَنَىٰهَا ب ن ي B002; 91:5 بَنَىٰهَا ب ن ي B004; 91:5 بَنَىٰهَا ب ن ي B009; 91:6 ٱلْأَرْضِ ء ر ض B001; 91:6 ٱلْأَرْضِ ء ر ض B005; 91:6 طَحَىٰهَا ط ح و B001; 91:6 طَحَىٰهَا ط ح و B005; 91:7 نَفْسٍۢ ن ف س B011; 91:7 سَوَّىٰهَا س و ي B002

## Düzlenen: dengelenmiş nefis, yere serilen kavim

Aynı fiil surede iki kez geçer. Yedinci ayette "sevvâhâ" bir nefsi düzgün bir biçime getirir. On dördüncü ayette "fe-sevvâhâ" bir kavmi yerle bir eder: {ar:فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا, tr:fe-kezzebûhu fe-akarûhâ fe-demdeme aleyhim rabbuhum bi-zenbihim fe-sevvâhâ, gloss:onu yalanladılar ve deveyi ayaklarından kestiler; Rableri de günahları yüzünden üstlerine yıkım indirdi ve onu dümdüz etti, source:91:14}. Kökün bir kolu geniş, düz araziyi adlandırır: {ar:السِيّ الفضاء من الأرض الواسع, tr:es-siyyu'l-fadâu mine'l-ardi'l-vâsi', gloss:siyy, geniş, açık düzlüktür, source:"س و ي,B009"}. Bir başka kolu ise eşitliği: {ar:السِيّ المثل من قولهم سِيّان أي مثلان, tr:es-siyyu'l-mislu, min kavlihim siyyân, ey meslân, gloss:siyy, denk demektir; "siyyân", yani iki eş sözünden, source:"س و ي,B001"}. Birinci anlamda kavim düz bir yer gibi serilir. İkincisinde hiçbiri ayrı tutulmaz, hepsi bir olur.

Altıncı ayetteki yayılmış yer, bu düzlenmenin önceden kurulmuş biçimidir. "Tahâ" fiili yaymanın yanında vurulup yere uzanmayı da anlatır: {ar:ضربه ضربة طحا منها أي امتد, tr:darabehû darbeten tahâ minhâ, ey imtedde, gloss:ona bir darbe vurdu, adam o darbeyle yere serildi, yani boylu boyunca uzandı, source:"ط ح و,B006"}. Yere yapışıp kalan bir deve de bu fiille anılır: {ar:وطحى البعير إلى الأرض أي لزق بها, tr:ve tahâ'l-ba'îru ile'l-ard, ey lezika bihâ, gloss:deve yere tahâ etti, yani yere yapıştı, source:"ط ح و,B006"}. Fiil helak olmayı da adlandırır: {ar:طحا إذا هلك, tr:tahâ izâ heleke, gloss:helak olduğunda "tahâ" denir, source:"ط ح و,B007"}. Yerin kendi kökünde ise yere doğru ağırlaşıp çökmek vardır: {ar:التأرض أيضا التثاقل إلى الأرض, tr:et-te'arrudu eyzan et-tesâkulu ile'l-ard, gloss:te'arrud, yere doğru ağırlaşıp çökmek anlamına da gelir, source:"ء ر ض,B006"}. Arada iki devirme olur. Birincisi devenindir: {ar:عقرت الفرس أي كسعت قوائمه بالسيف, tr:akartu'l-ferese, ey kese'tu kavâimehû bi's-seyf, gloss:atı akr ettim, yani ayaklarını kılıçla biçtim, source:"ع ق ر,B002"}. İkincisi kavmindir ve kökten kazımadır: {ar:الدَّمْدَمَة: الاستئصال, tr:ed-demdeme: el-isti'sâl, gloss:demdeme, kökünden kazımaktır, source:"د م د م,B001"}.

Kur'an bu düzlenmeyi Semûd için yerinde gösterir. Salih kavmine şunu hatırlatır: {ar:تَتَّخِذُونَ مِن سُهُولِهَا قُصُورًۭا وَتَنْحِتُونَ ٱلْجِبَالَ بُيُوتًۭا, tr:tettehızûne min suhûlihâ kusûran ve tenhitûne'l-cibâle buyûtâ, gloss:ovalarında saraylar ediniyor, dağları oyup evler yapıyorsunuz, source:7:74}. Bina kökü bu sarayları da adlandırır: {ar:بنى فلان بيتا من البنيان وبنى قصورا, tr:benâ fulânun beyten mine'l-bunyân ve benâ kusûran, gloss:falan bina olarak bir ev kurdu, saraylar kurdu, source:"ب ن ي,B001"}. "Tahâ" kökü de bu ovaların adıdır: {ar:والطحا المنبسط من الأرض, tr:ve't-tahâ el-munbesitu mine'l-ard, gloss:tahâ, yerin yayvan düzlüğüdür, source:"ط ح و,B001"}. Suçun fiili "akr", bir köyün sığındığı yüksek binanın da adıdır: {ar:العقر القصر الذي يكون معتمدا لأهل القرية يلجؤون إليه, tr:el-ukru'l-kasru'llezî yekûnu mu'temeden li-ehli'l-karye, yelce'ûne ileyh, gloss:ukr, köy halkının dayandığı ve sığındığı saraydır, source:"ع ق ر,B015"}. Daha genel olarak da: {ar:العقر كل بناء مرتفع, tr:el-ukru kullu binâin murtefi', gloss:ukr, yükseltilmiş her yapıdır, source:"ع ق ر,B015"}. Yurdun ortası da bu kökle anılır: {ar:عقر الدار محلة القوم, tr:ukru'd-dâri mahalletu'l-kavm, gloss:yurdun ortası, kavmin oturduğu yerdir, source:"ع ق ر,B013"}. Kur'an, Semûd'un kayaları oyan bir halk olduğunu söyler: {ar:وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ, tr:ve Semûde'llezîne câbu's-sahra bi'l-vâd, gloss:vadide kayaları oyan Semûd, source:89:9}. Hicr halkı da bu evlerde kendini güvende sanmıştır: {ar:وَكَانُوا۟ يَنْحِتُونَ مِنَ ٱلْجِبَالِ بُيُوتًا ءَامِنِينَ, tr:ve kânû yenhitûne mine'l-cibâli buyûten âminîn, gloss:dağlardan güven içinde evler oyuyorlardı, source:15:82}.

Bu yapıların sonu düzlenmedir. Allah Semûd'un hikâyesini şöyle bitirir: {ar:فَأَصْبَحُوا۟ فِى دَارِهِمْ جَٰثِمِينَ, tr:fe-asbahû fî dârihim câsimîn, gloss:yurtlarında diz üstü çökmüş halde sabahladılar, source:7:78}; {ar:كَأَن لَّمْ يَغْنَوْا۟ فِيهَآ, tr:ke-en lem yağnev fîhâ, gloss:sanki orada hiç oturmamışlardı, source:11:68}. Bir başka anlatımda kuru ot gibi ezilirler: {ar:فَكَانُوا۟ كَهَشِيمِ ٱلْمُحْتَظِرِ, tr:fe-kânû ke-heşîmi'l-muhtezır, gloss:ağıl yapanın çiğnenmiş kuru otu gibi oldular, source:54:31}. Bir yerde de ayağa kalkamazlar: {ar:فَمَا ٱسْتَطَٰعُوا۟ مِن قِيَامٍۢ, tr:fe-mâ'steta'û min kıyâm, gloss:ayağa kalkmaya güçleri yetmedi, source:51:45}. Evleri boş kalır, yıkılır: {ar:فَتِلْكَ بُيُوتُهُمْ خَاوِيَةًۢ بِمَا ظَلَمُوٓا۟, tr:fe-tilke buyûtuhum hâviyeten bimâ zalemû, gloss:işte zulümleri yüzünden çökmüş, boş kalmış evleri, source:27:52}. Kur'an düzlemeyi dağlar için de sahneler. Kıyamette dağlar savrulur ve yer şöyle olur: {ar:فَيَذَرُهَا قَاعًۭا صَفْصَفًۭا, tr:fe-yezeruhâ kâ'an safsafâ, gloss:onları dümdüz bir alan olarak bırakır, source:20:106}; {ar:لَّا تَرَىٰ فِيهَا عِوَجًۭا وَلَآ أَمْتًۭا, tr:lâ terâ fîhâ ivecen ve lâ emtâ, gloss:orada ne bir eğrilik ne bir tümsek görürsün, source:20:107}. Aynı gün inkârcılar kendi üstlerine düzlenmeyi isterler: {ar:لَوْ تُسَوَّىٰ بِهِمُ ٱلْأَرْضُ, tr:lev tusevvâ bihimu'l-ard, gloss:keşke yer üstlerine düzlenseydi, source:4:42}. Fiil burada sevvâ fiilinin kendisidir.

Fiilin iki yüzü aynı kudrete aittir. Diriltmeyi inkâr edene Allah şunu söyler: {ar:بَلَىٰ قَٰدِرِينَ عَلَىٰٓ أَن نُّسَوِّىَ بَنَانَهُۥ, tr:belâ kâdirîne alâ en nusevviye benâneh, gloss:evet, parmak uçlarını bile yeniden düzenlemeye gücümüz yeter, source:75:4}. Ufacık bir şekli inceden inceye işleyen fiil, bir kavmi yere serer. Düz bir anlatım yalnızca "yok etti" der. Fiilin tekrarı ise yedinci ayetteki biçim verme ile on dördüncü ayetteki dümdüz etmeyi aynı elin iki işi olarak yan yana koyar. Ovaya saray, dağa ev kuran kavim, yaydığı yer kadar düz kalır.

Kaynaklar: 91:7 سَوَّىٰهَا س و ي B002; 91:14 فَسَوَّىٰهَا س و ي B009; 91:14 فَسَوَّىٰهَا س و ي B001; 91:6 طَحَىٰهَا ط ح و B001; 91:6 طَحَىٰهَا ط ح و B006; 91:6 طَحَىٰهَا ط ح و B007; 91:6 ٱلْأَرْضِ ء ر ض B006; 91:5 بَنَىٰهَا ب ن ي B001; 91:14 فَعَقَرُوهَا ع ق ر B002; 91:14 فَعَقَرُوهَا ع ق ر B013; 91:14 فَعَقَرُوهَا ع ق ر B015; 91:14 فَدَمْدَمَ د م د م B001

## Tarla: yarılan, sulanan, büyüyen toprak ve hiçbir şey bitirmeyen kum

Altıncı ayette yayılan yerin ailesinde verimli toprak vardır. Bu toprak dokuzuncu ayetin fiiliyle anılır: {ar:أرض أريضة أي زكية, tr:ardun erîdatun, ey zekiyye, gloss:erîde bir toprak, yani bereketle büyüyen toprak, source:"ء ر ض,B002"}. Bitkinin toprakta kök salıp çoğalması da yerin kökünden bir fiildir: {ar:تأرض النبت تمكن على الأرض فكثر, tr:te'arrada'n-nebtu: temekkene ale'l-ardı fe-kesura, gloss:bitki yere tutundu ve çoğaldı, source:"ء ر ض,B002"}. "Tahâ" fiili de toprağın yüzüne yayılmış bitkiyi anlatır: {ar:والبقلة المطحية النابتة على وجه الأرض قد افترشتها, tr:ve'l-baklatu'l-mathiyyetu en-nâbitetu alâ vechi'l-ard, kad efteraşethâ, gloss:yerin yüzünde biten ve onu döşek gibi kaplayan yayvan sebze, source:"ط ح و,B006"}. Göğün adı ise yağmurun da bitkinin de adıdır: {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tusemmi's-sehâbe semâen ve'l-matara semâ', gloss:Araplar buluta da yağmura da semâ der, source:"س م و,B004"}; {ar:سمي النبات سماء, tr:summiye'n-nebâtu semâ', gloss:bitkiye de semâ denmiştir, source:"س م و,B004"}. Bu adlarla beşinci ve altıncı ayetlerdeki ev bir tarlaya dönüşür. Tavandan su iner, döşeme yeşerir.

Tarlanın işlemesi suyun yolunu açmakla başlar. Üçüncü ayetteki gündüz kelimesi, toprağı yaran ırmakla aynı köktendir: {ar:سمي النهر لأنه ينهر الأرض أي يشقها, tr:summiye'n-nehru li-ennehû yenheru'l-ard, ey yeşukkuhâ, gloss:ırmağa nehr denmesi, toprağı yarmasındandır, source:"ن ه ر,B001"}. Sekizinci ayetteki fucûrun kökü suyun açıldığı yeri adlandırır: {ar:الفجرة موضع تفتح الماء, tr:el-fecretu mevdı'u tefettuhi'l-mâ', gloss:fecre, suyun açılıp aktığı yerdir, source:"ف ج ر,B001"}. Dokuzuncu ayetteki "efleha" fiili saban işidir: {ar:فلحت الأرض شققتها, tr:felahtu'l-arda: şakaktuhâ, gloss:toprağı sürdüm, yani yardım, source:"ف ل ح,B001"}. Çiftçinin adı da buradan gelir: {ar:سمي الأكار فلاحا لأنه يشق الأرض, tr:summiye'l-ekkâru fellâhan li-ennehû yeşukku'l-ard, gloss:çiftçiye fellâh denmesi, toprağı yarmasındandır, source:"ف ل ح,B003"}. Aynı ayetteki "zekkâhâ" ekinin büyümesidir: {ar:زكا الزرع يزكو زكاء ممدود أي نما, tr:zekâ'z-zer'u yezkû zekâen, ey nemâ, gloss:ekin zekâ etti, yani büyüdü, source:"ز ك و,B001"}; {ar:أصل الزكاة النمو الحاصل عن بركة الله تعالى, tr:aslu'z-zekâti'n-nemuvvu'l-hâsılu an bereketi'llâhi teâlâ, gloss:zekâtın aslı, Allah'ın bereketinden gelen büyümedir, source:"ز ك و,B001"}. On üçüncü ayetteki "sukyâ" bir tarlanın sudaki payıdır: {ar:كم سقى أرضك أي حظها من الشرب, tr:kem sakyu ardık, ey hazzuhâ mine'ş-şirb, gloss:toprağının sakyı ne kadar, yani su payı ne kadar, source:"س ق ي,B003"}. On dördüncü ayetteki "zenb" kelimesinin ailesinde yamaçlardaki su yolları vardır: {ar:المذانب مذانب التلاع وهي مسايل الماء فيها, tr:el-mezânibu mezânibu't-tilâ', ve hiye mesâyilu'l-mâi fîhâ, gloss:mezânib, yamaçlardaki su yataklarıdır, source:"ذ ن ب,B004"}. Aynı ayetteki "Rab" kelimesinin ailesinde ise bitkiyi besleyen bulut vardır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb: es-sehâb, summiye bi-zâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi beslediği için bu adı almıştır, source:"ر ب ب,B008"}. Kökün temel işi de budur: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi adım adım olgunluğa erdirmektir, source:"ر ب ب,B002"}.

Tarlanın tersi de surenin kelimelerinde durur. Onuncu ayetteki fiil, Arap dilinin açıkladığı türeyişle "dessese"ye götürür: toprağa itip gömmek. Kur'an'daki karşılığı, yukarıda anılan, toprağa gömme sahnesidir: {ar:أَمْ يَدُسُّهُۥ فِى ٱلتُّرَابِ, tr:em yedussuhû fi't-turâb, gloss:yoksa onu toprağa mı gömsün, source:16:59}. Çok derine itilen tohum filizlenmez. Fiil de büyümenin tam zıddı olarak tanımlanır: {ar:وهو نقيض زكا يزكو زكاء وزكاة وهو داس لا زاك, tr:ve huve nakîdu zekâ yezkû zekâen ve zekâten, ve huve dâsin lâ zâk, gloss:bu, büyümenin zıddıdır; o gömen biridir, büyüten değil, source:"د س و,B002"}. On dördüncü ayetteki suç fiili "akr", hiçbir şey bitirmeyen kumun adıdır: {ar:العاقر من الرمل ما لا ينبت شيئا, tr:el-âkiru mine'r-ramli mâ lâ yunbitu şey'â, gloss:âkir kum, hiçbir şey bitirmeyen kumdur, source:"ع ق ر,B017"}. Aynı fiil hurmanın büyüme noktasını kesip atmayı da anlatır: {ar:عقرت النخلة إذا قطعت رأسها كله مع الجمار, tr:ukırati'n-nahletu izâ kutı'a ra'suhâ kulluhû ma'a'l-cumâr, gloss:hurmanın başı, özüyle birlikte tümden kesilince "ukırat" denir, source:"ع ق ر,B007"}.

Kur'an bu tarlayı açıkça sahneler. Abese Suresi'nde Allah insana yemeğine bakmasını söyler: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:fe'l-yenzuri'l-insânu ilâ taâmih, gloss:insan yemeğine bir baksın, source:80:24}. Ardından üç adım sayılır: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:suyu bol bol döktük, source:80:25}; {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:summe şakakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26}; {ar:فَأَنۢبَتْنَا فِيهَا حَبًّۭا, tr:fe-enbetnâ fîhâ habbâ, gloss:orada tane bitirdik, source:80:27}. Dökmek, yarmak, bitirmek: dokuzuncu ayetteki sürme ve büyümenin adımları bunlardır. Nûh kavmine insanın kendisini bir bitki gibi anlatır: {ar:وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًۭا, tr:va'llâhu enbetekum mine'l-ardı nebâtâ, gloss:Allah sizi yerden bir bitki gibi bitirdi, source:71:17}. Bu yüzden nefsin büyütülmesi bir tarlanın büyümesiyle aynı işi görür. Kur'an iki toprağı yan yana koyar: {ar:وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ, tr:ve'l-beledu't-tayyibu yahrucu nebâtuhû bi-izni rabbih, gloss:iyi toprağın bitkisi Rabbinin izniyle çıkar, source:7:58}; {ar:وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًۭا, tr:ve'llezî habuse lâ yahrucu illâ nekidâ, gloss:kötü topraktan ise ancak cılız bir şey çıkar, source:7:58}. Mallarını harcayanlar için de iki örnek verir. Biri tepedeki bahçedir: {ar:كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ, tr:ke-meseli cennetin bi-rabvetin esâbehâ vâbilun fe-âtet ukulehâ dı'feyn, gloss:tepedeki bir bahçe gibi; sağanak ona isabet edince ürününü iki kat verir, source:2:265}. Öteki üzerinde biraz toprak olan kayadır: {ar:كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا, tr:ke-meseli safvânin aleyhi turâbun fe-esâbehû vâbilun fe-terakehû saldâ, gloss:üstünde toprak bulunan düz bir kaya gibi; sağanak onu çıplak bırakır, source:2:264}. Aynı yağmur bir yerde büyütür, öteki yerde altındaki kayayı ortaya çıkarır.

Semûd da bir tarla halkıdır. Salih onlara bunu hatırlatır: {ar:هُوَ أَنشَأَكُم مِّنَ ٱلْأَرْضِ وَٱسْتَعْمَرَكُمْ فِيهَا, tr:huve enşeekum mine'l-ardı ve'ste'marakum fîhâ, gloss:sizi yerden O yetiştirdi ve sizi orada imar ettirdi, source:11:61}. Onlar bahçelerin ve kaynakların içindedir: {ar:فِى جَنَّٰتٍۢ وَعُيُونٍۢ, tr:fî cennâtin ve uyûn, gloss:bahçeler ve pınarlar içinde, source:26:147}; {ar:وَزُرُوعٍۢ وَنَخْلٍۢ طَلْعُهَا هَضِيمٌۭ, tr:ve zurû'in ve nahlin tal'uhâ hedîm, gloss:ekinler ve tomurcukları yumuşacık hurmalar içinde, source:26:148}. Hurmalık içinde yaşayan bir kavmin suç fiili, hurmanın başını kesip atan fiille aynıdır. Kur'an büyümenin karşılığını da su yollarıyla anlatır: {ar:وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:ve zâlike cezâu men tezekkâ, gloss:işte bu, arınıp büyüyenin karşılığıdır, source:20:76}. Bu söz, Firavun'un tehdidi karşısında iman eden sihirbazların ağzındadır ve altından ırmaklar akan bahçeleri anlatır. Kalbin taşa dönmesi bile bu dille anlatılır: {ar:وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ, tr:ve inne mine'l-hicârati lemâ yetefecceru minhu'l-enhâr, gloss:taşların öylesi vardır ki içinden ırmaklar fışkırır, source:2:74}. Bu sözler İsrailoğullarına, kalpleri bu taşlardan da katı olduğu için söylenir. Düz bir anlatım dokuzuncu ve onuncu ayeti "nefsini arındıran" ve "nefsini kirleten" diye geçer. Fiillerin ailesi ise iki tarlayı gösterir: biri sürülmüş, sulanmış ve yeşermiş; öbürü gömülmüş ya da kum.

Kaynaklar: 91:3 ٱلنَّهَارِ ن ه ر B001; 91:5 ٱلسَّمَآءِ س م و B004; 91:6 ٱلْأَرْضِ ء ر ض B002; 91:6 طَحَىٰهَا ط ح و B006; 91:8 فُجُورَهَا ف ج ر B001; 91:9 أَفْلَحَ ف ل ح B001; 91:9 أَفْلَحَ ف ل ح B003; 91:9 زَكَّىٰهَا ز ك و B001; 91:10 دَسَّىٰهَا د س و B002; 91:13 وَسُقْيَٰهَا س ق ي B003; 91:14 بِذَنۢبِهِمْ ذ ن ب B004; 91:14 رَبُّهُم ر ب ب B002; 91:14 رَبُّهُم ر ب ب B008; 91:14 فَعَقَرُوهَا ع ق ر B007; 91:14 فَعَقَرُوهَا ع ق ر B017

## Buluşmalar

İlk buluşma sekizinci ayette olur. "Fucûr" kelimesi aynı kökten üç sahneyi bir arada tutar: geceyi yaran şafağı, bentten fırlayan suyu ve din perdesini yırtmayı. Gökte yarılma ışık getirir, nefiste ise koruyucu örtüyü yırtar ve bir taşkın başlatır. Takvâ aynı ayette hem bir örtüdür hem de bir settir. Tek bir kelime bu iki imgeyi birlikte taşır: örten ve alıkoyan. Böylece surenin başındaki düzenli nöbet nefsin içine taşınır. Gece güneşin üstünü sırası gelince örter ve sırası gelince açılır. Nefis ise ya kendi örtüsünü yerinde tutar ya da onu yırtıp taşar.

İkinci buluşma on ikinci ayetteki "inbe'ase" fiilindedir. Bu fiil üç imgeyi birden toplar. Fucûru tanımlayan atılıştır, deveyi köstekinden çözüp kaldırmanın sonucudur ve Allah'ın elçi gönderişinin eşi olan bir fiildir. Deve sürücüsünün dilinde biri kaldırır, deve kalkar. Bu ayette ise kaldıran yoktur. Adam kendi kendine, köstekinden kurtulmuş bir hayvan gibi kalkar ve Allah'ın gönderdiği deveye yönelir. Elçi gönderilmiştir, deve gönderilmiştir. Taşkın olan ise kendini gönderir.

Üçüncü buluşma, on dördüncü ayetten on beşinciye geçen bedenin arka ucudur. "Akr" topuk kirişini keser. O kirişin adı on beşinci ayetteki "ukbâ" kelimesinin kökündendir. Günahın adı olan "zenb" de hayvanın arka ucunun adıdır. Devenin imgesi ile suçun ardından gelen sonucun imgesi böylece aynı noktada birleşir. Kavim devenin arkasına vurur; karşılık da onların "arkalarından", yani günahlarının ardından gelir. Kova ile günahın aynı kökten gelmesi bunu ölçüye bağlar. Devenin su payını çiğneyenler kendi kova paylarını alırlar.

Dördüncü buluşma "sevvâ" fiilindedir. Bu fiil göğün ve nefsin bitirilişini Semûd'un yerle bir edilişine bağlar. Altıncı ayetteki yayılmış yer bu iki ucun arasında durur. Kavim ovaya saray kurmuştu. Yayılan yere kurulan sarayları yayılmış bir yer gibi dümdüz olur. Gökten yağan su, sürülen toprak ve büyüyen ekin bu yere bağlıdır. Hurmanın başını kesmeyi ve hiçbir şey bitirmeyen kumu anlatan "akr" fiili, kavmin tarlasını bir çorak yere çevirir.

Bu buluşmalar birlikte surenin hareketini taşır. Sure, her cismin yerini bildiği bir gökle başlar: ışık yayılır, ay onu izler, gündüz açar, gece örter. Ardından gök ve yerden bir ev kurulur ve aynı el nefsi bu evin üçüncü yapısı olarak düzenler. Nefse iki lokma yutturulur: hem yırtan ve taşan hem de örten ve alıkoyan. Dokuzuncu ve onuncu ayetler bu iki lokmanın sonucunu iki tarla gibi gösterir: biri sürülmüş ve büyümüş, öbürü gömülmüş. Semûd ise yanlış yolu seçer. Sınırı aşar, kendi en bedbahtının ardına düşer, gönderilen deveyi arkasından biçer. Karşılık gece gibi üstlerine kapanır ve evleri ile birlikte onları yayılmış bir yer gibi dümdüz eder. Sure, gece ile gündüzün nöbetleşmesini de adlandıran bir kelimeyle kapanır. Ama bu son nöbette, hükmün ardından gelecek ve onu geri çevirecek hiçbir şey yoktur.

