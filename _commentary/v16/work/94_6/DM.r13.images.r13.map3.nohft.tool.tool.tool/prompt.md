Focus: 94:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/94_6/D.r13/context.md =====
# 94:6 — focus

إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا

Anchor translation (canonical reading, reference only):

Gerçekten zorluğun yanında bir kolaylık vardır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | إِنَّ | إِنّ |  | ACC |
| 2 | مَعَ | مَع2 |  | P |
| 3 | ٱلْعُسْرِ | عُسْر | ع س ر | DET;N |
| 4 | يُسْرًا | يُسْر | ي س ر | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 94 — full text (context; no pericope)

- 94:1 أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ
- 94:2 وَوَضَعْنَا عَنكَ وِزْرَكَ
- 94:3 ٱلَّذِىٓ أَنقَضَ ظَهْرَكَ
- 94:4 وَرَفَعْنَا لَكَ ذِكْرَكَ
- 94:5 فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا
- 94:6 ◀ focus إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا
- 94:7 فَإِذَا فَرَغْتَ فَٱنصَبْ
- 94:8 وَإِلَىٰ رَبِّكَ فَٱرْغَب


===== _commentary/v16/work/94_6/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ع س ر (root_001012) — identity root of ٱلْعُسْرِ (w3)

- **B001** güçlük ve çetinlik — güçlük, çetinlik; kolaylığın karşıtı · zorlaşmak, çetin hale gelmek · zor, çetin · zor ve çetin gün · kolaylaşmayan zor işler · zor olan veya kolay olanın karşıtı
  أصل صحيح واحد يدل على صعوبة وشدة (maqayis); العسر نقيض اليسر (maqayis;ayn;sihah;tahdhib;mufradat); أمر عسير ويوم عسير (maqayis;ayn;sihah;tahdhib;mufradat); العسرى الأمور التي تعسر ولا تتيسر (tahdhib)
- **B002** para darlığı — para darlığı, maddi sıkıntı · maddi darlık, parasızlık · maddi sıkıntı içinde olan kimse · varlıktan maddi darlığa düşmek
  الإقلال أيضا عسرة (maqayis); العسر قلة ذات اليد (ayn); العسرة قلة ذات اليد وكذلك الإعسار (tahdhib); العسرة تعسر وجود المال (mufradat); أعسر الرجل إذا صار من ميسرة إلى عسرة (maqayis)
- **B003** darlıktaki borçluyu sıkıştırmak — darlıktaki borçludan borcu katılıkla istemek · darlık zamanında benden bir şey istemek · alacak istemede ve işte katı davrananlar
  عسرته أنا أعسره إذا طالبته بدينك وهو معسر ولم تنظره إلى ميسرته (maqayis); عسرت الغريم أعسره إذا طلبت منه الدين على عسرته (sihah); عسرت الغريم أعسره عسرا إذا أخذته على عسرة ولم ترفق به (tahdhib); عسرني الرجل طالبني بشيء حين العسرة (mufradat)
- **B004** karşı çıkıp işi güçleştirmek — karşı çıkma ve dolambaçlılık · iş ona dolambaçlı ve güç gelmek · ona karşı çıkmak veya işi ona güçleştirmek · iş dolambaçlı ve güç hale gelmek · birbirlerine işi güçleştirmek · birinden elde edilmesi güç olan şeyi istemek
  العسر الخلاف والالتواء (maqayis;ayn); عسرت عليه تعسيرا إذا خالفته (maqayis); عسر عليه الأمر أي التاث (sihah); عسرت على فلان الأمر تعسيرا (tahdhib); استعسرت فلانا إذا طلبت معسوره (tahdhib); تعاسر القوم طلبوا تعسير الأمر (mufradat)
- **B005** sol taraf ve sola özgü olma — sol taraf · solak, sol eliyle çalışan · iki elini de kullanabilen · soluma gelmek · sol yanında fazla tüy veya beyazlık bulunan kartal · sol kanadında beyazlık bulunan güvercin
  العسرى خلاف اليسرى (maqayis;sihah); الذي يعمل بشماله أعسر (maqayis); رجل أعسر بين العسر وامرأة عسراء (sihah;tahdhib); عقاب عسراء ريشها من الجانب الأيسر أكثر من الأيمن (sihah); حمام أعسر وعقاب عسراء بجناحه من يساره بياض (sihah;tahdhib)
- **B006** güç doğum yapmak — kadının doğumu güçleşmek · doğumu güç olsun ve kız doğursun diye beddua etmek
  أعسرت المرأة إذا عسر عليها ولادها (maqayis;sihah;tahdhib); أعسرت وآنثت (maqayis;tahdhib); أيسرت وأذكرت (maqayis;tahdhib)
- **B007** o yıl gebe kalmayan deve — o yıl çiftleştiği halde gebe kalmayan deve
  العسير الناقة التي اعتاطت واعتاصت فلم تحمل عامها (maqayis); العسير الناقة إذا اعتاطت عامها فلم تحمل (sihah); تفسير الليث للعسير أنها الناقة التي اعتاطت غير صحيح (tahdhib)
- **B008** hazır olmadan zorlayıp kullanmak veya almak — eğitilmeden binilen deve · eğitilmeden önce binilen deve · zorla almak · oğlu istemediği halde malından almak · sözü hazırlamadan doğaçlama söylemek
  الناقة التي تركب قبل أن تراض عوسرانية (maqayis); العسير الناقة التي لم ترض وقد اعتسرتها إذا ركبتها قبل أن تراض (sihah); اعتسره مثل اقتسره (sihah); العسير الناقة التي ركبت قبل تذليلها (tahdhib); يعتسر الرجل من مال ولده معناه يأخذ من ماله وهو كاره (tahdhib); اعتسرت الكلام إذا اقتضبته قبل أن تزوره وتهيئه (tahdhib)
- **B009** koşarken kuyruğunu kaldırmak — koşarken kuyruğunu kaldırıp büken deve · koşarken kuyruğunu kaldıran deve · koşarken kuyruklarını kaldıran veya büken develer ya da kurtlar
  العاسر من النوق إذا عدت رفعت ذنبها (maqayis); عسرت الناقة بذنبها إذا شالت به (sihah); العاسرة من النوق فهي التي إذا عدت رفعت ذنبها (tahdhib); عواسر الذئاب التي تعسل في عدوها وتكسر أذنابها (tahdhib); ناقة عوسرانية إذا كان من دأبها تكسير ذنبها ورفعه إذا عدت (tahdhib)
- **B010** uğursuz gün [kalıp] — uğursuz gün
  يوم أعسر أي مشئوم (tahdhib)
- **B011** dağınık veya art arda ilerleme — dağınık halde veya birbiri ardınca
  ذهبت الإبل عساريات وعشاريات إذا انتشرت وتفرقت (tahdhib); جاءوا عساريات وعسارى أي بعضهم في إثر بعض (tahdhib)
- **B012** cin topluluğu veya yer adı — bir cin topluluğunun adı · cin topluluğu, cinlerin yaşadığı arazi veya yer adı
  العسرة قبيلة من قبائل الجن (tahdhib); عسر قبيلة من الجن (tahdhib); عسر أرض يسكنها الجن (tahdhib); عسر موضع (tahdhib)
- **B013** çubuk atıp dikili çubuğu çıkarma oyunu — dikili çubuğa başka çubuk atıp onu yerinden çıkarma oyunu
  العسر لعبة لهم ينصبون خشبة ثم ترمى بخشبة أخرى وتقلع (tahdhib)

## ي س ر (root_001694) — identity root of يُسْرًا (w4)

- **B001** kolaylık; kolay ve hazır duruma gelme ya da getirme — kolaylık, güçlüğün karşıtı · kolay olan, güç olmayan · kolaylaşıp hazır duruma gelmek · kolaylaştırıp hazırlamak · birine anlayış gösterip kolaylık sağlamak · kolay olan · kolay, güç olmayan
  اليسر: ضد العسر (maqayis;mufradat)؛ الميسور: ضد المعسور، وتيسر واستيسر بمعنى تهيأ (sihah)؛ تيسر واستيسر أي تسهل وتهيأ، وأيسرت المرأة وتيسرت في كذا أي سهلته وهيأته (mufradat)؛ ياسره أي ساهله (sihah)
- **B002** az miktar veya kısa süre — az miktar veya kısa süre
  اليسير: القليل، وشيء يسير أي هين (sihah)؛ واليسير يقال في الشيء القليل (mufradat)
- **B003** maddi bolluk ve varlıklı olma — maddi bolluk ve varlıklılık · varlıklılık ve maddi güç · varlıklılık · varlıklı duruma gelmek
  الميسرة والميسرة: السعة والغنى؛ واليسار واليسارة: الغنى، وقد أيسر الرجل أي استغنى (sihah)؛ الميسرة واليسار عبارة عن الغنى (mufradat)
- **B004** sol el veya sol yön — sol el veya sol yön · soldaki, sağın karşıtı · sol taraf · sola yönelip ilerlemek · iki elini de kullanabilen kişi
  اليسار لليد، تياسروا إذ أخذوا ذات اليسار، وياسروا (maqayis)؛ الأيسر: نقيض الأيمن، والميسرة خلاف الميمنة، واليسار خلاف اليمين، والياسر نقيض اليامن، ورجل أعسر يسر للذي يعمل بكلتا يديه (sihah)
- **B005** yumuşak başlı ve harekette uyumlu olma — yumuşak başlı ve çabuk uyum gösteren · hafif bacaklar · hayvanın bacaklarını iyi aktarması
  اليسرات: القوائم الخفاف؛ فرس حسن التيسور أي حسن نقل القوائم؛ رجل يسر ويسر أي حسن الانقياد (maqayis)؛ ليسر خفيف ويسر أي لين الانقياد سريع المتابعة يوصف به الإنسان والفرس (ayn)؛ اليسرات: القوائم الخفاف، ودابة حسن التيسور أي حسن نقل القوائم (sihah)
- **B006** koyunların süt ve yavru bakımından çoğalması [kalıp] — koyunların sütü ve yavrusu çoğalmak
  يسرت الغنم إذا كثر لبنها ونسلها (maqayis;sihah)
- **B007** fal oklarıyla oynanan paylaştırmalı talih oyunu — fal oklarıyla oynanan geleneksel talih oyunu · fal okları oyununa katılmak için toplananlar · fal oklarıyla oynayan kişi · fal oklarıyla oynayan kişi · topluluğun deveyi kesip parçalarını paylaştırması · deveyi kesip oyun düzenine göre paylaştırmak
  الأيسار: القوم يجتمعون على الميسر، واحدهم يسر؛ والميسر: القمار (maqayis)؛ الميسر: قمار العرب بالأزلام؛ الياسر: اللاعب بالقداح؛ اليسر والياسر بمعنى والجمع أيسار؛ يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها (sihah)
- **B008** ayrı avuç çizgileri veya uyluk damgası — avuç içindeki birbirine bitişmeyen çizgiler · uyluklardaki damga
  اليسرة: أسرار الكف إذا كانت غير ملزقة (maqayis;sihah)؛ اليسرة أيضا: سمة في الفخذين (sihah)
- **B009** aşağı doğru burma veya yüz hizasına saplama — sağ eli gövdeye çekerek aşağı doğru burma · yüz hizasına yöneltilen saplama
  اليسر: الفتل إلى أسفل، وهو أن تمد يمينك نحو جسدك؛ والطعن اليسر: حذاء وجهك (sihah)
- **B010** yer ve kişi adı kullanımları — bir yerin adı · çöl bölgesindeki bir geçidin adı · anlatıda geçen bir kişinin adı
  يسر: مكان (maqayis)؛ اليسر أيضا: دخل لنبى يربوع بالدهناء (sihah)؛ يسار الكواعب هو اسم عبد (sihah)
- **B011** genç erkek — genç erkek, delikanlı
  اليسار: الفتى (maqayis)

===== _commentary/v16/out/s094/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 94:5, whose words 94:6 repeats, and ## Buluşmalar) =====
## Borçlunun darlığı ve indirilen borç

Beşinci ve altıncı ayetlerdeki iki kelime bir alacak verecek sahnesi de kurar. 'Usr, elde az şey bulunmasıdır: {ar:العسر قلة ذات اليد, tr:el-'usru kılletu zâti'l-yed, gloss:'usr elin darlığıdır, source:"ع س ر,B002"}. Kökün fiili bolluktan darlığa düşmeyi anlatır: {ar:أعسر الرجل إذا صار من ميسرة إلى عسرة, tr:e'sera'r-raculu izâ sâra min meysaratin ilâ 'usrah, gloss:adam bolluktan darlığa düşünce "a'sera" denir, source:"ع س ر,B002"}. Sahnenin ikinci kişisi alacaklıdır. Borçlunun durumu darken onu sıkıştıran alacaklının işi de aynı kökle söylenir: {ar:عسرته أنا أعسره إذا طالبته بدينك وهو معسر ولم تنظره إلى ميسرته, tr:'asartuhû ena a'suruhû izâ tâlebtehû bi-deynike ve huve mu'sirun ve lem tunzirhu ilâ meysaratih, gloss:borçlu darda iken alacağını istediğinde ve bolluğa çıkana kadar ona süre vermediğinde onu sıkıştırmış olursun, source:"ع س ر,B003"}. Karşı kelime genişlik ve zenginliktir: {ar:الميسرة والميسرة: السعة والغنى؛ واليسار واليسارة: الغنى، وقد أيسر الرجل أي استغنى, tr:el-meysera ve'l-meysura es-se'atu ve'l-ğinâ, ve kad eysera'r-raculu ey istağnâ, gloss:meysera genişlik ve zenginliktir, adam "eysera" oldu yani zenginleşti, source:"ي س ر,B003"}.

İkinci ayetteki fiil de bu sahneye girer. Vedî'a, sermayeden düşülen miktardır: {ar:الوضيعة الحطيطة من رأس المال, tr:el-vadî'atu'l-hatîtatu min ra'si'l-mâl, gloss:vadî'a sermayeden indirilen kısımdır, source:"و ض ع,B004"}. Ticarette zarar etmek de böyle söylenir: {ar:وضع في تجارته يوضع خسر, tr:vudi'a fî ticâratihî, gloss:ticaretinde zarara uğradı, source:"و ض ع,B004"}. Arapçada alacaklı borcun bir kısmını borçlunun üstünden düştüğünde {ar:وضع عنه, tr:veda'a 'anhu, gloss:onun üstünden indirdi, source:"memory"} denir. Bu kalıp ikinci ayetin {ar:وَضَعْنَا عَنكَ, tr:veda'nâ 'anke, gloss:senin üstünden indirdik, source:94:2} kalıbıyla aynıdır. Bu yankıyla dinlendiğinde ilk dört ayet ile sonraki iki ayet bir hesap defteri gibi de okunur. Önce borç düşülür, sonra darlığın yanında bolluk haber verilir. Alacağın yazılı senedine de zikir denir: {ar:ذكر الحق الصك, tr:zikru'l-hakkı's-sakk, gloss:hakkın zikri senettir, source:"ذ ك ر,B008"}. Gönülden verilen sadakanın ölçüsü de sırt kelimesiyle söylenir: {ar:ما كان عن ظهر غنى عن فضل عيال, tr:mâ kâne 'an zahri ğınâ, gloss:bakmakla yükümlü olunanlardan artanla, zenginliğin sırtından verilen, source:"ظ ه ر,B023"}.

Kur'an bu sahneyi faiz yasağından hemen sonra kurar: {ar:وَإِن كَانَ ذُو عُسْرَةٍۢ فَنَظِرَةٌ إِلَىٰ مَيْسَرَةٍۢ, tr:ve in kâne zû 'usratin fe-nazıratun ilâ meysarah, gloss:borçlu darlık içindeyse bolluğa çıkana kadar ona süre verilir, source:2:280}. Ayet devam eder: {ar:وَأَن تَصَدَّقُوا۟ خَيْرٌۭ لَّكُمْ, tr:ve en tesaddekû hayrun leküm, gloss:alacağı sadaka olarak bağışlamanız sizin için daha hayırlıdır, source:2:280}. Alacaklıya iki yol gösterilir: beklemek ya da düşmek. Hemen ardından borcun yazılması emredilir ve iki kadın tanık için {ar:فَتُذَكِّرَ إِحْدَىٰهُمَا ٱلْأُخْرَىٰ, tr:fe-tuzekkira ihdâhume'l-uhrâ, gloss:biri öbürüne hatırlatsın, source:2:282} denir. Zikir orada da borcun hatırda tutulmasıdır. Boşanma hükümlerinde geçim sağlama kuralı konur: {ar:لِيُنفِقْ ذُو سَعَةٍۢ مِّن سَعَتِهِۦ, tr:li-yunfik zû se'atin min se'atih, gloss:geniş olan genişliğinden harcasın, source:65:7}. Rızkı daraltılan da kendisine verilenden harcar. Ayet şöyle biter: {ar:سَيَجْعَلُ ٱللَّهُ بَعْدَ عُسْرٍۢ يُسْرًۭا, tr:seyec'alullâhu ba'de 'usrin yusrâ, gloss:Allah bir darlığın ardından bir genişlik verecek, source:65:7}. Bir önceki surede aynı muhataba şöyle denmişti: {ar:وَوَجَدَكَ عَآئِلًۭا فَأَغْنَىٰ, tr:ve vecedeke 'âilen fe-ağnâ, gloss:seni yoksul buldu ve zengin etti, source:93:8}. Bu görüntü, surenin darlık ve genişlik sözlerine elin boşalıp dolmasını ekler. Yükün indirilmesine de alacaklının borcu düşmesinin ölçülebilir somutluğunu verir.

Kaynaklar: 94:5 ٱلْعُسْرِ ع س ر B002; 94:5 ٱلْعُسْرِ ع س ر B003; 94:5 يُسْرًا ي س ر B003; 94:2 وَضَعْنَا و ض ع B004; 94:4 ذِكْرَكَ ذ ك ر B008; 94:3 ظَهْرَكَ ظ ه ر B023

## Taşınan ve doğurulan

Yükü indirmek anlamındaki fiil doğumu da adlandırır. Kadın taşıdığını bırakır: {ar:وضعت المرأة الحمل وضعا, tr:veda'ati'l-mer'etu'l-hamle vad'an, gloss:kadın taşıdığını bıraktı, yani doğurdu, source:"و ض ع,B002"}. Yük için kullanılan kalıp ile doğum için kullanılan kalıp aynıdır: bir şey taşınır ve sonunda yere bırakılır. Vizrin tarifinde geçen {ar:الوزر الحمل الثقيل من الإثم, tr:el-vizru'l-himlu's-sekîlu mine'l-ism, gloss:vizr, günahtan ağır yüktür, source:"و ز ر,B002"} cümlesindeki "himl" (yük) ile gebelik anlamındaki "haml" aynı harflerle yazılır. Surenin kelimesi ise bir yüktür, gebelik değildir. Bu yakınlık yalnızca iki sahnenin aynı biçimi paylaştığını gösterir.

Darlık ve genişlik de doğumda geçer. Zor doğum için {ar:أعسرت المرأة إذا عسر عليها ولادها, tr:e'serati'l-mer'etu izâ 'asura 'aleyhâ vilâduhâ, gloss:doğumu zor geçtiğinde kadın için "a'serat" denir, source:"ع س ر,B006"} denir. Kolay doğum için de {ar:أيسرت المرأة وتيسرت في كذا أي سهلته وهيأته, tr:eyserati'l-mer'etu ve teyesserat, gloss:kadının işi kolaylaştı ve hazır hâle geldi, source:"ي س ر,B001"} denir. Gebe kadına söylenen eski bir hayır duası ve bir beddua kalıbı, surenin iki kelimesini birleştirir: {ar:أيسرت وأذكرت, tr:eyserat ve ezkerat, gloss:kolay doğursun ve erkek doğursun, source:"ع س ر,B006"} ve karşıtı {ar:أعسرت وآنثت, tr:e'serat ve ânesat, gloss:zor doğursun ve kız doğursun, source:"ع س ر,B006"}. Dördüncü ayetteki zikrin kökü de erkek çocuk doğurmayı anlatır: {ar:أذكرت ولدت ذكرا والمذكار تلد الذكور, tr:ezkerat veledet zekeran ve'l-mizkâru teledu'z-zukûr, gloss:"ezkerat" erkek doğurdu demektir, hep erkek doğurana "mizkâr" denir, source:"ذ ك ر,B001"}. Sekizinci ayetteki Rab kelimesinin kökü yeni doğurmuş koyunu adlandırır: {ar:الربى: الشاة التي وضعت حديثا؛ قرب العهد بالولادة, tr:er-rubbâ eş-şâtu'lletî veda'at hadîsen, gloss:rubbâ, yeni doğurmuş koyundur, source:"ر ب ب,B009"}. Kök büyütmeyi de anlatır: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiyetu ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi aşama aşama tamamlanmaya kadar geliştirmektir, source:"ر ب ب,B002"}. Çocuğa bakan bakıcıyı da adlandırır: {ar:الربيبة: الحاضنة, tr:er-rabîbetu'l-hâdına, gloss:rabîbe, çocuğa bakan dadıdır, source:"ر ب ب,B005"}. Sürünün bereketi de genişlik kelimesiyle söylenir: {ar:يسرت الغنم إذا كثر لبنها ونسلها, tr:yeserati'l-ğanemu izâ kesura lebenuhâ ve nesluhâ, gloss:koyunların sütü ve yavrusu çoğalınca "yeserat" denir, source:"ي س ر,B006"}.

Kur'an bu kelimelerin çoğunu tek bir sahnede toplar. İmran'ın karısı karnındakini adamıştır. Ardından şöyle anlatılır: {ar:فَلَمَّا وَضَعَتْهَا قَالَتْ رَبِّ إِنِّى وَضَعْتُهَآ أُنثَىٰ, tr:felemmâ veda'athâ kâlet rabbi innî veda'tuhâ unsâ, gloss:onu doğurunca "Rabbim, ben onu kız doğurdum" dedi, source:3:36}. Araya giren söz şudur: {ar:وَلَيْسَ ٱلذَّكَرُ كَٱلْأُنثَىٰ, tr:ve leyse'z-zekeru ke'l-unsâ, gloss:erkek kız gibi değildir, source:3:36}. Ardından {ar:فَتَقَبَّلَهَا رَبُّهَا بِقَبُولٍ حَسَنٍۢ وَأَنۢبَتَهَا نَبَاتًا حَسَنًۭا وَكَفَّلَهَا زَكَرِيَّا, tr:fe-tekabbelehâ rabbuhâ bi-kabûlin hasenin ve enbetehâ nebâten hasenen ve keffelehâ zekeriyyâ, gloss:Rabbi onu güzel bir kabulle kabul etti, onu güzelce büyüttü ve Zekeriya'yı ona bakıcı yaptı, source:3:37} gelir. Doğurmak, erkek, Rab, büyütme ve bakıcılık bu sahnede bir aradadır. Eski kalıp kolay doğumu erkek doğumuna bağlıyordu. Kur'an'ın sahnesinde ise Rab, doğan kızı güzel bir kabulle karşılar ve onu aşama aşama büyütür.

Boşanma suresi doğumu, emzirmeyi, darlığı ve kolaylığı art arda koyar. Önce {ar:وَأُو۟لَٰتُ ٱلْأَحْمَالِ أَجَلُهُنَّ أَن يَضَعْنَ حَمْلَهُنَّ, tr:ve ulâtu'l-ahmâli eceluhunne en yeda'ne hamlehunn, gloss:gebelerin süresi taşıdıklarını bırakmalarıdır, source:65:4} denir. Aynı ayet {ar:وَمَن يَتَّقِ ٱللَّهَ يَجْعَل لَّهُۥ مِنْ أَمْرِهِۦ يُسْرًۭا, tr:ve men yettekıllâhe yec'al lehû min emrihî yusrâ, gloss:Allah'tan sakınana işinde bir kolaylık verir, source:65:4} diye biter. Sonra emzirme konusunda anlaşamayanlara şöyle denir: {ar:وَإِن تَعَاسَرْتُمْ فَسَتُرْضِعُ لَهُۥٓ أُخْرَىٰ, tr:ve in te'âsartum fe-seturdı'u lehû uhrâ, gloss:birbirinize güçlük çıkarırsanız onu başka bir kadın emzirir, source:65:6}. Ardından {ar:سَيَجْعَلُ ٱللَّهُ بَعْدَ عُسْرٍۢ يُسْرًۭا, tr:seyec'alullâhu ba'de 'usrin yusrâ, gloss:Allah bir darlığın ardından bir kolaylık verecek, source:65:7} gelir. Doğumun ağırlığı başka bir ayette de anılır: {ar:حَمَلَتْهُ أُمُّهُۥ كُرْهًۭا وَوَضَعَتْهُ كُرْهًۭا, tr:hamelethu ummuhû kurhen ve veda'athu kurhâ, gloss:annesi onu zahmetle taşıdı ve zahmetle doğurdu, source:46:15}. Meryem'i doğum sancısı bir hurma gövdesine götürür {source:19:23}. Kıyamet anında da {ar:وَتَضَعُ كُلُّ ذَاتِ حَمْلٍ حَمْلَهَا, tr:ve teda'u küllü zâti hamlin hamlehâ, gloss:her gebe taşıdığını bırakır, source:22:2} denir. Büyütme ise kibirli bir dille de söylenir. Firavun Musa'ya şöyle der: {ar:أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا, tr:elem nurabbike fînâ velîdâ, gloss:seni çocukken aramızda büyütmedik mi?, source:26:18}. Bu soru, birinci ayetin kalıbıyla aynıdır: "elem" ile başlar, ardından "biz" ve "sen" gelir. Bir önceki surede de aynı kalıp vardır: {ar:أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ, tr:elem yecidke yetîmen fe-âvâ, gloss:seni yetim bulup barındırmadı mı?, source:93:6}. Firavun yaptığı iyiliği başa kakmak için sorar. Bu surede ise Rab yaptığını, muhatabını darlığın içinde bir kolaylığa hazırlamak için hatırlatır.

Kaynaklar: 94:2 وَضَعْنَا و ض ع B002; 94:2 وِزْرَكَ و ز ر B002; 94:5 ٱلْعُسْرِ ع س ر B006; 94:5 يُسْرًا ي س ر B001; 94:5 يُسْرًا ي س ر B006; 94:4 ذِكْرَكَ ذ ك ر B001; 94:8 رَبِّكَ ر ب ب B009; 94:8 رَبِّكَ ر ب ب B002; 94:8 رَبِّكَ ر ب ب B005

## Yük devesi ve yol

Sırt kelimesi binek ve yük hayvanının kendisini de adlandırır: {ar:الظهر الركاب تحمل الأثقال في السفر, tr:ez-zahru'r-rikâbu tahmilu'l-eskâle fi's-sefer, gloss:zahr, yolculukta ağırlık taşıyan binek hayvanlarıdır, source:"ظ ه ر,B005"}. Bir adam {ar:ظهري معد للركوب, tr:zahrî mu'addun li'r-rukûb, gloss:sırtım (bineğim) binmeye hazırdır, source:"ظ ه ر,B005"} der. Bu yankıyla sure bir kervan sahnesine dönüşür. Ayakta duran deve, binicisi binebilsin diye boynunu eğer: {ar:اتضع فلان بعيره إذا كان قائما فطامن من عنقه ليركبه, tr:ittada'a fulânun ba'îrahû, gloss:biri ayaktaki devesinin boynunu binmek için eğdi, source:"و ض ع,B013"}. Deve yolculukta erir: {ar:البعير المهزول نقض كأن الأسفار نقضته, tr:el-ba'îru'l-mehzûlu nıkdun keenne'l-esfâra nekadateh, gloss:zayıflamış deveye nıkd denir, sanki yolculuklar onu söküp dağıtmıştır, source:"ن ق ض,B002"}. Semer ve mahfeler yük altında gıcırdar: {ar:النقيض صوت المحامل والرحال, tr:en-nakîdu savtu'l-mehâmili ve'r-rihâl, gloss:nakîd, mahfelerin ve semerlerin sesidir, source:"ن ق ض,B005"}. Binici genç deveyi diliyle şaklatarak sürer: {ar:الإنقاض زجر القعود, tr:el-inkâdu zecru'l-ku'ûd, gloss:inkâd, genç deveyi sürmek için çıkarılan sestir, source:"ن ق ض,B006"}. Üçüncü ayetin iki kelimesi bu sahnede yükünü taşıyıp yolda zayıflamış ve semeri gıcırdayan bir binek olur.

Yürüyüşün adları da surededir. Vad', kolay ve rahat bir yürüyüştür. Kendisinden daha yüksek tempolu yürüyüşün karşıtıdır: {ar:الدابة تضع في سيرها وضعا وهو سير سهل يخالف المرفوع, tr:ed-dâbbetu teda'u fî seyrihâ vad'an ve huve seyrun sehlun yuhâlifu'l-merfû', gloss:hayvan yürüyüşünde vad' eder, bu kolay bir yürüyüştür ve merfû'un karşıtıdır, source:"و ض ع,B003"}. Merfû' bunun bir üst basamağıdır: {ar:مرفوع الناقة في سيرها خلاف الموضوع, tr:merfû'u'n-nâkati fî seyrihâ hilâfu'l-mevdû', gloss:dişi devenin merfû' yürüyüşü mevdû'un karşıtıdır, source:"ر ف ع,B003"}. İkinci ve dördüncü ayetlerdeki iki fiil, bu kullanımla aynı hayvanın iki temposu gibi de duyulur. Konaklama da aynı kökle anlatılır: {ar:إبل واضعة أي مقيمة في الحمض, tr:ibilun vâdı'a, gloss:tuzlu otlakta duran develer, source:"و ض ع,B007"}. Beşinci ve altıncı ayetlerin karşıtlığı burada binek hayvanının karşıtlığıdır. Zor deve henüz alıştırılmamış devedir: {ar:العسير الناقة التي لم ترض وقد اعتسرتها إذا ركبتها قبل أن تراض, tr:el-'asîru'n-nâkatu'lletî lem turad, gloss:'asîr, alıştırılmamış devedir, onu alıştırılmadan bindiğinde "i'tesartuhâ" dersin, source:"ع س ر,B008"}. Kolay binek ise uysal ve ayağı düzgün olandır: {ar:ليسر خفيف ويسر أي لين الانقياد سريع المتابعة يوصف به الإنسان والفرس, tr:yeserun ey leyyinu'l-inkıyâdi serî'u'l-mutâba'a, gloss:yeser, kolay güdülen ve çabuk uyan demektir, insan ve at için söylenir, source:"ي س ر,B005"}. Bunun bir tarifi de {ar:دابة حسن التيسور أي حسن نقل القوائم, tr:dâbbetun hasenu't-teysûr, gloss:ayaklarını güzel atan hayvan, source:"ي س ر,B005"} şeklindedir.

Yedinci ayetteki fiilin kökü yolun kendisini anlatır. Kervan bütün gün sakin bir tempoyla yürür: {ar:نصب القوم ساروا يومهم وهو سير لين, tr:nasabe'l-kavmu sârû yevmehum, gloss:kavim bütün gün yürüdü, bu yumuşak bir yürüyüştür, source:"ن ص ب,B010"}. Tempo da yükseltilebilir: {ar:نصب القوم السير نصبا إذا رفعوه, tr:nasabe'l-kavmu's-seyra nasben izâ rafa'ûh, gloss:kavim yürüyüşü yükseltince "nasabû" denir, source:"ن ص ب,B010"}. Ayakta durmanın yorgunluğu da aynı köktendir: {ar:النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي, tr:en-nasabu'l-'anâu ve ma'nâhu enne'l-insâne lâ yezâlu muntesıben hattâ yu'yî, gloss:nasab yorgunluktur, anlamı insanın bitkin düşene kadar dimdik durmasıdır, source:"ن ص ب,B004"}. Binicilerin yolda söylediği türküye de nasb denir: {ar:نصب الراكب إذا غنى النصب, tr:nasabe'r-râkibu izâ ğannâ'n-nasb, gloss:binici nasb türküsünü söyleyince "nasabe" denir, source:"ن ص ب,B009"}. Geniş adımlı at ve geniş yol iki kökle anlatılır: {ar:فرس فريغ أي واسع المشي, tr:farasun ferîğ, gloss:geniş adımlı at, source:"ف ر غ,B003"} ve {ar:فرس رغيب الشحوة كثير الأخذ بقوائمه من الأرض, tr:farasun rağîbu'ş-şahve, gloss:adımı geniş, ayaklarıyla çok yer tutan at, source:"ر غ ب,B002"}. Su başı da surededir. Develer her gün öğle vakti suya getirilir: {ar:الظاهرة أن ترد كل يوم ظهرا, tr:ez-zâhiratu en terida külle yevmin zuhren, gloss:zâhira, her gün öğle vakti suya gelmektir, source:"ظ ه ر,B004"}. Sudan ayrılış da göğüs kelimesinin köküyle söylenir: {ar:صدرت الإبل عن الماء, tr:saderati'l-ibilu 'ani'l-mâ', gloss:develer sudan döndü, source:"ص د ر,B003"}. Yolun sonunda develerin ayrılmadan kaldığı yer gelir: {ar:أرب فلان بالمكان إذا أقام به فلم يبرحه, tr:erebbe fulânun bi'l-mekân, gloss:biri bir yerde kalıp ayrılmayınca "erebbe" denir, source:"ر ب ب,B007"}. Develerin kaldığı yere de {ar:مرب الإبل حيث لزمته, tr:merebbu'l-ibil, gloss:develerin ayrılmadan durduğu yer, source:"ر ب ب,B007"} denir.

Kur'an bu sahneyi hayvanlar üzerinden bir nimet olarak anlatır. Hayvanlar için şöyle denir: {ar:وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ, tr:ve tahmilu eskâleküm ilâ beledin lem tekûnû bâliğîhi illâ bi-şıkkı'l-enfus, gloss:canınız çıkmadan varamayacağınız bir ülkeye yüklerinizi onlar taşır, source:16:7}. Ayet {ar:إِنَّ رَبَّكُمْ لَرَءُوفٌۭ رَّحِيمٌۭ, tr:inne rabbekum le-raûfun rahîm, gloss:Rabbiniz çok şefkatli, çok merhametlidir, source:16:7} diye biter. Başka bir yerde gemiler ve hayvanlar şu amaçla verilmiştir: {ar:لِتَسْتَوُۥا۟ عَلَىٰ ظُهُورِهِۦ ثُمَّ تَذْكُرُوا۟ نِعْمَةَ رَبِّكُمْ, tr:li-testevû 'alâ zuhûrihî summe tezkurû ni'mete rabbikum, gloss:sırtlarına yerleşesiniz, sonra Rabbinizin nimetini anasınız diye, source:43:13}. Binicinin sözü de verilir: {ar:وَإِنَّآ إِلَىٰ رَبِّنَا لَمُنقَلِبُونَ, tr:ve innâ ilâ rabbinâ le-munkalibûn, gloss:biz Rabbimize döneceğiz, source:43:14}. Bu tek sahnede binek sırtı, zikir, Rab ve "Rabbimize" varan yolculuk bir aradadır. Rahat yürüyüş anlamındaki vad' fiili münafıkların davranışında da geçer: {ar:وَلَأَوْضَعُوا۟ خِلَٰلَكُمْ, tr:ve le-evda'û hilâleküm, gloss:aranızda hızla binek koştururlardı, source:9:47}. Yol yorgunluğunu Musa söyler. Genç arkadaşına {ar:لَآ أَبْرَحُ حَتَّىٰٓ أَبْلُغَ مَجْمَعَ ٱلْبَحْرَيْنِ, tr:lâ ebrahu hattâ ebluğa mecme'a'l-bahreyn, gloss:iki denizin birleştiği yere varmadan durmayacağım, source:18:60} demiştir. Buluşma yerini geçtikten sonra şöyle der: {ar:لَقَدْ لَقِينَا مِن سَفَرِنَا هَٰذَا نَصَبًۭا, tr:lekad lakînâ min seferinâ hâzâ nasabâ, gloss:bu yolculuğumuzdan gerçekten yorgunluk gördük, source:18:62}. Allah yolunda çıkanlar için de {ar:لَا يُصِيبُهُمْ ظَمَأٌۭ وَلَا نَصَبٌۭ وَلَا مَخْمَصَةٌۭ فِى سَبِيلِ ٱللَّهِ إِلَّا كُتِبَ لَهُم بِهِۦ عَمَلٌۭ صَٰلِحٌ, tr:lâ yusîbuhum zama'un ve lâ nasabun ve lâ mahmasatun fî sebîlillâhi illâ kutibe lehum bihî 'amelun sâlih, gloss:Allah yolunda onlara dokunan her susuzluk, yorgunluk ve açlık karşılığında salih bir amel yazılır, source:9:120} denir. Aynı ayet, elçinin canını kendi canlarından aşağı görmemelerini {ar:وَلَا يَرْغَبُوا۟ بِأَنفُسِهِمْ عَن نَّفْسِهِۦ, tr:ve lâ yerğabû bi-enfusihim 'an nefsih, gloss:onun canını bırakıp kendi canlarını tercih etmesinler, source:9:120} sözüyle ister. Varılan yurtta ise yorgunluk biter: {ar:لَا يَمَسُّنَا فِيهَا نَصَبٌۭ, tr:lâ yemessunâ fîhâ nasab, gloss:orada bize yorgunluk dokunmaz, source:35:35}. Kur'an deveye bakmayı da emreder: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:efelâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı, nasıl yaratıldı?, source:88:17}. Ardından gelen iki ayet surenin iki fiilini kullanır: gök {ar:كَيْفَ رُفِعَتْ, tr:keyfe rufi'at, gloss:nasıl yükseltildi, source:88:18}, dağlar {ar:كَيْفَ نُصِبَتْ, tr:keyfe nusıbet, gloss:nasıl dikildi, source:88:19}.

Bu görüntü surenin sözlerine bir yolculuk sırası verir. Yüklü sırt bir binektir, gıcırtı semerin sesidir. Zor ve kolay, alıştırılmamış ve uysal binektir. "Kalk ve emek ver" uzun bir günlük yürüyüştür. "Rabbine" de kervanın vardığı ve ayrılmadan kaldığı yerdir.

Kaynaklar: 94:3 ظَهْرَكَ ظ ه ر B005; 94:3 ظَهْرَكَ ظ ه ر B004; 94:3 أَنقَضَ ن ق ض B002; 94:3 أَنقَضَ ن ق ض B005; 94:3 أَنقَضَ ن ق ض B006; 94:2 وَضَعْنَا و ض ع B013; 94:2 وَضَعْنَا و ض ع B003; 94:2 وَضَعْنَا و ض ع B007; 94:4 رَفَعْنَا ر ف ع B003; 94:5 ٱلْعُسْرِ ع س ر B008; 94:5 يُسْرًا ي س ر B005; 94:7 فَرَغْتَ ف ر غ B003; 94:7 فَٱنصَبْ ن ص ب B010; 94:7 فَٱنصَبْ ن ص ب B004; 94:7 فَٱنصَبْ ن ص ب B009; 94:8 فَٱرْغَب ر غ ب B002; 94:1 صَدْرَكَ ص د ر B003; 94:8 رَبِّكَ ر ب ب B007

## Konan, yükseltilen, dikilen, sökülen

Surenin dört ana fiili aynı zamanda yapı fiilleridir. Vad' bir şeyi yerine koymaktır. "Yer" anlamındaki mevdı' da buradan gelir: {ar:الموضع المكان ومصدر وضعت الشيء من يدي, tr:el-mevdı'u'l-mekânu ve masdaru vada'tu'ş-şey'e min yedî, gloss:mevdı' yerdir, "şeyi elimden koydum" sözünün de masdarıdır, source:"و ض ع,B001"}. Ref' konmuş bir cismi oturduğu yerden yukarı kaldırmaktır: {ar:الرفع يقال في الأجسام الموضوعة إذا أعليتها عن مقرها, tr:er-ref'u yukâlu fi'l-ecsâmi'l-mevdû'ati izâ a'leytehâ 'an makarrihâ, gloss:ref', konmuş cisimleri yerlerinden yükselttiğinde söylenir, source:"ر ف ع,B001"}. Binada ise yükseltmektir: {ar:في البناء إذا طولته, tr:fi'l-binâi izâ tavveltah, gloss:binayı yükselttiğinde, source:"ر ف ع,B001"}. Nasb bir şeyi dışarı çıkıntı yapacak biçimde dikmektir: {ar:نصب الشيء وضعه وضعا ناتئا كنصب الرمح والبناء والحجر, tr:nasbu'ş-şey'i vad'uhû vad'an nâti'en ke-nasbi'r-rumhi ve'l-binâi ve'l-hacer, gloss:nasb, bir şeyi çıkıntılı biçimde koymaktır, mızrağı, binayı ve taşı dikmek gibi, source:"ن ص ب,B001"}. Bir başka tarif şudur: {ar:كل شيء رفعته فقد نصبته, tr:küllü şey'in rafa'tehû fekad nasabteh, gloss:kaldırdığın her şeyi dikmiş olursun, source:"ن ص ب,B001"}. Nakd ise sağlam yapılmış olanı sökmektir: {ar:إفساد ما أبرمت من حبل أو بناء, tr:ifsâdu mâ ebramte min hablin ev binâ', gloss:sağlam büktüğün ipi ya da kurduğun binayı bozmak, source:"ن ق ض,B001"}. Mecaz anlamı da buradan doğar: {ar:نقضت البناء والحبل والعقد؛ استعير نقض العهد, tr:nakadtu'l-binâe ve'l-hable ve'l-'akd, gloss:binayı, ipi ve düğümü söktüm, ahdi bozmak da buradan alınmıştır, source:"ن ق ض,B001"}.

Bu yankıyla üçüncü ayet yeni bir şey duyurur. Yük sırta yapının çatırdaması gibi bir şey yapmıştır. Gıcırtı, kurulu bir yapının sökülmek üzere olduğu anın sesidir. Ardından gelen fiiller ise birer kurma fiilidir. Önce yük yere konur, sonra ad yükseltilir. Yedinci ayette muhataba "dik dur" denir. Göğsün kökü dikilmiş mızrağın ucunu da adlandırır: {ar:صدر القناة أعلاها, tr:sadru'l-kanâti a'lâhâ, gloss:mızrak sapının sadrı onun en üst kısmıdır, source:"ص د ر,B002"}. Darlık sözcüğünün kökü ise dikilen bir kazığın sökülmesini adlandırır. Bu bir oyundur: {ar:العسر لعبة لهم ينصبون خشبة ثم ترمى بخشبة أخرى وتقلع, tr:el-'usru lu'betun lehum yensibûne haşebeten summe turmâ bi-haşebetin uhrâ ve tukla', gloss:'usr onların bir oyunudur, bir kazık dikerler, sonra ona başka bir tahta atılır ve kazık sökülür, source:"ع س ر,B013"}. Sekizinci ayetteki Rab kelimesinin kökü ise sağlam bağlanmış düğümü adlandırır: {ar:الربى: العقدة المحكمة, tr:er-rubbâ el-'ukdetu'l-muhkema, gloss:rubbâ sağlam düğümdür, source:"ر ب ب,B016"}. Bu, sökülen ipin karşıtıdır.

Kur'an bu fiilleri yapının ve yaratılışın sahnelerinde kullanır. İbrahim ile İsmail Beyt'in temellerini yükseltirken dua ederler: {ar:وَإِذْ يَرْفَعُ إِبْرَٰهِۦمُ ٱلْقَوَاعِدَ مِنَ ٱلْبَيْتِ وَإِسْمَٰعِيلُ رَبَّنَا تَقَبَّلْ مِنَّآ, tr:ve iz yerfe'u ibrâhîmu'l-kavâ'ide mine'l-beyti ve ismâ'îlu rabbenâ tekabbel minnâ, gloss:İbrahim ile İsmail Beyt'in temellerini yükseltirken "Rabbimiz, bizden kabul et" diyorlardı, source:2:127}. Aynı ev için {ar:إِنَّ أَوَّلَ بَيْتٍۢ وُضِعَ لِلنَّاسِ لَلَّذِى بِبَكَّةَ, tr:inne evvele beytin vudı'a li'n-nâsi lellezî bi-bekke, gloss:insanlar için konan ilk ev Bekke'deki evdir, source:3:96} denir. İkinci ve dördüncü ayetin iki fiili, konmak ve yükseltilmek, Kur'an'da aynı evin iki hâlidir. Gök için de bu fiiller kullanılır: {ar:ٱللَّهُ ٱلَّذِى رَفَعَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا, tr:allâhullezî rafe'a's-semâvâti bi-ğayri 'amedin teravnehâ, gloss:Allah gökleri gördüğünüz direkler olmadan yükseltendir, source:13:2}. Başka bir yerde {ar:رَفَعَ سَمْكَهَا فَسَوَّىٰهَا, tr:rafe'a semkehâ fe-sevvâhâ, gloss:tavanını yükseltti ve düzene koydu, source:79:28} denir. Rahman suresi iki fiili aynı ayette karşı karşıya koyar: {ar:وَٱلسَّمَآءَ رَفَعَهَا وَوَضَعَ ٱلْمِيزَانَ, tr:ve's-semâe rafe'ahâ ve veda'a'l-mîzân, gloss:göğü yükseltti ve teraziyi koydu, source:55:7}. Biraz sonra {ar:وَٱلْأَرْضَ وَضَعَهَا لِلْأَنَامِ, tr:ve'l-arda veda'ahâ li'l-enâm, gloss:yeri de canlılar için koydu, source:55:10} gelir. Deve, gök, dağlar ve yer sahnesinde gök "yükseltilmiş" ve dağlar "dikilmiş"tir {source:88:19}, sonra {ar:وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ, tr:ve ile'l-ardı keyfe sutıhat, gloss:yere bakmazlar mı, nasıl yayıldı?, source:88:20} denir. Ezilmiş sırt ile yükseltilmiş gök aynı fiil ailesinin iki ucunda durur.

Sökme fiilinin Kur'an'daki en somut sahnesi bir ip sahnesidir: {ar:وَلَا تَكُونُوا۟ كَٱلَّتِى نَقَضَتْ غَزْلَهَا مِنۢ بَعْدِ قُوَّةٍ أَنكَٰثًۭا, tr:ve lâ tekûnû kelletî nekadat ğazlehâ min ba'di kuvvetin enkâsâ, gloss:ipliğini sağlamca büktükten sonra çözüp lime lime eden kadın gibi olmayın, source:16:92}. Bu benzetme yeminler için yapılır. Bir önceki ayet {ar:وَلَا تَنقُضُوا۟ ٱلْأَيْمَٰنَ بَعْدَ تَوْكِيدِهَا, tr:ve lâ tenkudu'l-eymâne ba'de tevkîdihâ, gloss:yeminleri sağlamlaştırdıktan sonra bozmayın, source:16:91} der. Ahdi bozanlar için de {ar:ٱلَّذِينَ يَنقُضُونَ عَهْدَ ٱللَّهِ مِنۢ بَعْدِ مِيثَٰقِهِۦ, tr:ellezîne yenkudûne 'ahdallâhi min ba'di mîsâkıh, gloss:Allah'ın ahdini sağlamlaştırılmasından sonra bozanlar, source:2:27} denir. Surede ise sökme işini bir insan yapmaz, yük sırta yapar. Sökülmek üzere olan da bir ahit değil, taşıyıcının bedenidir. Musa'nın duasındaki düğüm ise çözülmesi istenen bir düğümdür: {ar:وَٱحْلُلْ عُقْدَةًۭ مِّن لِّسَانِى, tr:vahlul 'ukdeten min lisânî, gloss:dilimden bir düğümü çöz, source:20:27}. Orada düğümün çözülmesi bir kurtuluştur. Sağlam bükülmüş ipin sökülmesi ise yıkımdır. Surenin sonundaki Rab kelimesinin kökünde de sağlam düğüm vardır.

Kaynaklar: 94:2 وَضَعْنَا و ض ع B001; 94:3 أَنقَضَ ن ق ض B001; 94:4 رَفَعْنَا ر ف ع B001; 94:7 فَٱنصَبْ ن ص ب B001; 94:1 صَدْرَكَ ص د ر B002; 94:5 ٱلْعُسْرِ ع س ر B013; 94:8 رَبِّكَ ر ب ب B016

## Zorlukla birlikte kolaylık

Beşinci ve altıncı ayetler aynı cümleyi iki kez söyler: {ar:فَإِنَّ مَعَ ٱلْعُسْرِ يُسْرًا, tr:fe-inne me'a'l-'usri yusrâ, gloss:muhakkak ki zorlukla birlikte bir kolaylık vardır, source:94:5} ve {ar:إِنَّ مَعَ ٱلْعُسْرِ يُسْرًۭا, tr:inne me'a'l-'usri yusrâ, gloss:muhakkak ki zorlukla birlikte bir kolaylık vardır, source:94:6}. İki kelime her tarifte birbiriyle tanımlanır: {ar:العسر نقيض اليسر, tr:el-'usru nakîdu'l-yusr, gloss:zorluk kolaylığın karşıtıdır, source:"ع س ر,B001"}. Öbür yönden de {ar:اليسر: ضد العسر, tr:el-yusru diddu'l-'usr, gloss:kolaylık zorluğun karşıtıdır, source:"ي س ر,B001"} denir. Ama ikisinin işleyişi farklıdır. Zorluk bükülüp direnen bir şeydir: {ar:العسر الخلاف والالتواء, tr:el-'usru'l-hilâfu ve'l-iltivâ', gloss:zorluk aksilik ve bükülmedir, source:"ع س ر,B004"}. İşin karışıp düğümlenmesi de böyle söylenir: {ar:عسر عليه الأمر أي التاث, tr:'asura 'aleyhi'l-emru ey iltâs, gloss:iş ona zor geldi, yani karıştı, source:"ع س ر,B004"}. Kolaylık ise düzlenmiş ve hazır hâle getirilmiş olandır: {ar:تيسر واستيسر أي تسهل وتهيأ, tr:teyessere vesteysera ey tesehhele ve teheyye', gloss:kolaylaştı, yani düzlendi ve hazırlandı, source:"ي س ر,B001"}. Karşıdakine kolaylık göstermek de bu köktendir: {ar:ياسره أي ساهله, tr:yâserahû ey sâhelehû, gloss:ona kolaylık gösterdi, source:"ي س ر,B001"}. Kolay olan küçük ve hafiftir: {ar:اليسير: القليل، وشيء يسير أي هين, tr:el-yesîru'l-kalîl, ve şey'un yesîrun ey heyyin, gloss:yesîr azdır, kolay şey önemsiz şeydir, source:"ي س ر,B002"}. Zorluğun bir günü de vardır: {ar:أمر عسير ويوم عسير, tr:emrun 'asîrun ve yevmun 'asîr, gloss:zor iş, zor gün, source:"ع س ر,B001"}. Uğursuz gün de aynı kökle söylenir: {ar:يوم أعسر أي مشئوم, tr:yevmun a'sar, gloss:uğursuz gün, source:"ع س ر,B010"}.

Arapça bu iki kelimeyi bir bedende birleştirir: {ar:رجل أعسر يسر للذي يعمل بكلتا يديه, tr:raculun a'saru yesarun lillezî ya'melu bi-kiltâ yedeyh, gloss:iki eliyle de iş gören adama "a'sar yesar" denir, source:"ع س ر,B005"}. İki kelimenin adlandırdığı eller ayrı ayrı anılır: {ar:العسرى خلاف اليسرى, tr:el-'usrâ hilâfu'l-yusrâ, gloss:'usrâ, yusrânın karşıtıdır, source:"ي س ر,B004"}. "Birlikte" anlamındaki {ar:مَعَ, tr:me'a, gloss:ile, birlikte, source:94:5} edatı bu görüntüyle dinlendiğinde, iki elin aynı bedende ve aynı işte bir arada çalışmasına benzer. Surenin edatı "sonra" değil, "birlikte"dir. Kur'an başka bir yerde sırayı söyler: {ar:سَيَجْعَلُ ٱللَّهُ بَعْدَ عُسْرٍۢ يُسْرًۭا, tr:seyec'alullâhu ba'de 'usrin yusrâ, gloss:Allah bir zorluğun ardından bir kolaylık verecek, source:65:7}. Bu surede ise kolaylık zorluğun içinde, onunla aynı anda haber verilir. Beşinci ayetin başındaki {ar:فَ, tr:fe, gloss:işte, öyleyse, source:94:5} harfi de bu haberi önceki dört ayete bağlar. Göğüs açılmış, yük inmiş, ad yükselmiştir. Bunlar kolaylığın zorluğun içinde geldiğinin kanıtıdır. İki ayette de zorluk belirlilik takısıyla ("el-'usr"), kolaylık ise belirsiz ve tenvinli ("yusran") gelir. Arapçada belirli bir isim tekrarlandığında aynı şeyi gösterir, belirsiz isim tekrarlandığında ise yeni bir şey sayılabilir. Bu kullanımla tekrar, tek bir zorluğun yanında iki kez anılan kolaylık olarak duyulur.

Kur'an kolaylığı bir yol olarak sahneler. Veren ve sakınan için {ar:فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ, tr:fe-senuyessiruhû li'l-yusrâ, gloss:onu en kolay olana hazırlayacağız, source:92:7} denir. Cimrilik eden ve kendini yeterli görüp en güzeli yalanlayan için ise {ar:فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ, tr:fe-senuyessiruhû li'l-'usrâ, gloss:onu en zor olana hazırlayacağız, source:92:10} denir. Peygamber'e doğrudan şöyle söylenir: {ar:وَنُيَسِّرُكَ لِلْيُسْرَىٰ, tr:ve nuyessiruke li'l-yusrâ, gloss:seni en kolay olana hazırlayacağız, source:87:8}. Oruç hükmünde hasta ve yolcuya ruhsat tanındıktan sonra {ar:يُرِيدُ ٱللَّهُ بِكُمُ ٱلْيُسْرَ وَلَا يُرِيدُ بِكُمُ ٱلْعُسْرَ, tr:yurîdullâhu bikumu'l-yusra ve lâ yurîdu bikumu'l-'usr, gloss:Allah sizin için kolaylık ister, zorluk istemez, source:2:185} denir. Musa iki yerde aynı dileği dile getirir. Firavun'a gönderilirken {ar:وَيَسِّرْ لِىٓ أَمْرِى, tr:ve yessir lî emrî, gloss:işimi bana kolaylaştır, source:20:26} der. Yolda karşılaştığı kul ile giderken unuttuğu söz için özür dileyip şöyle der: {ar:وَلَا تُرْهِقْنِى مِنْ أَمْرِى عُسْرًۭا, tr:ve lâ turhiknî min emrî 'usrâ, gloss:bu işimde bana zorluk yükleme, source:18:73}. Zorluğun saati de anılır. Allah, Peygamber'i ve ona {ar:فِى سَاعَةِ ٱلْعُسْرَةِ, tr:fî sâ'ati'l-'usrah, gloss:zorluk saatinde, source:9:117} uyanları bağışlamıştır. Zor gün ise inkâr edenlerin günüdür: {ar:فَذَٰلِكَ يَوْمَئِذٍۢ يَوْمٌ عَسِيرٌ, tr:fe-zâlike yevmeizin yevmun 'asîr, gloss:o gün zor bir gündür, source:74:9}, {ar:عَلَى ٱلْكَٰفِرِينَ غَيْرُ يَسِيرٍۢ, tr:'ale'l-kâfirîne ğayru yesîr, gloss:inkâr edenler için kolay değildir, source:74:10}. Kolaylık zikirle de birleşir: {ar:وَلَقَدْ يَسَّرْنَا ٱلْقُرْءَانَ لِلذِّكْرِ, tr:ve lekad yessernâ'l-kur'âne li'z-zikr, gloss:Kur'an'ı zikir için kolaylaştırdık, source:54:17}. Peygamber'e de {ar:فَإِنَّمَا يَسَّرْنَٰهُ بِلِسَانِكَ, tr:fe-innemâ yessernâhu bi-lisânik, gloss:onu senin dilinle kolaylaştırdık, source:19:97} denir. Gece namazında da {ar:فَٱقْرَءُوا۟ مَا تَيَسَّرَ مِنَ ٱلْقُرْءَانِ, tr:fakra'û mâ teyessera mine'l-kur'ân, gloss:Kur'an'dan kolayınıza geleni okuyun, source:73:20} denir. Surede kolaylık hem yük indikten sonra açılan yol, hem de yükseltilen zikrin kolaylaştırılmasıdır.

Kaynaklar: 94:5 ٱلْعُسْرِ ع س ر B001; 94:5 ٱلْعُسْرِ ع س ر B004; 94:5 ٱلْعُسْرِ ع س ر B005; 94:5 ٱلْعُسْرِ ع س ر B010; 94:5 يُسْرًا ي س ر B001; 94:5 يُسْرًا ي س ر B002; 94:5 يُسْرًا ي س ر B004

## Dikili taşlar ve oklar

Surenin kökleri eski Arapların meysir sahnesini de kurar. Meysir, yay kökündendir: {ar:الميسر: قمار العرب بالأزلام, tr:el-meysiru kımâru'l-'arabi bi'l-ezlâm, gloss:meysir, Arapların fal oklarıyla oynadığı kumardır, source:"ي س ر,B007"}. Bir deve kesilir ve parçaları oklarla paylaştırılır: {ar:يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها, tr:yesera'l-kavmu'l-cezûra eyictezerûhâ vaktesemû a'dâehâ, gloss:topluluk deveyi meysirle paylaştı, yani kesti ve uzuvlarını bölüştü, source:"ي س ر,B007"}. Et kemikten kesilip ayrılır: {ar:الشرح والتشريح قطع اللحم على العظام والقطعة شرحة, tr:eş-şerhu ve't-teşrîhu kat'u'l-lahmi 'ale'l-'izâm, gloss:şerh ve teşrîh eti kemiklerin üstünden kesmektir, parçaya şerha denir, source:"ش ر ح,B002"}. Oklar bir torbada durur ve bu torba Rab kelimesinin köküyle adlandırılır: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر؛ جماعة السهام, tr:er-ribâbetu şebîhetun bi'l-kinâneti tucme'u fîhâ sihâmu'l-meysir, gloss:ribâbe, meysir oklarının toplandığı sadağa benzer torbadır, okların topluluğudur, source:"ر ب ب,B010"}. Herkesin payı da belirlenir: {ar:النصيب الحظ المنصوب أي المعين, tr:en-nasîbu'l-hazzu'l-mensûbu eyi'l-mu'ayyen, gloss:nasîb, dikilmiş yani belirlenmiş paydır, source:"ن ص ب,B005"}. Göğüs kelimesinin kökü de bir şeyin bir kısmını adlandırır: {ar:الصدر الطائفة من الشيء, tr:es-sadru't-tâifetu mine'ş-şey', gloss:sadr, bir şeyin bir kısmıdır, source:"ص د ر,B006"}. Kurbanlar dikili taşların üzerinde kesilir: {ar:حجر كان ينصب فيعبد وتصب عليه دماء الذبائح وجمعه أنصاب, tr:hacerun kâne yunsabu fe-yu'bedu ve tusabbu 'aleyhi dimâu'z-zebâih, gloss:dikilip tapılan ve üzerine kurban kanlarının döküldüğü taş, çoğulu ensâbdır, source:"ن ص ب,B002"}.

Kur'an bu sahnenin unsurlarını tek bir ayette toplar ve hepsini reddeder: {ar:إِنَّمَا ٱلْخَمْرُ وَٱلْمَيْسِرُ وَٱلْأَنصَابُ وَٱلْأَزْلَٰمُ رِجْسٌۭ مِّنْ عَمَلِ ٱلشَّيْطَٰنِ, tr:innemâ'l-hamru ve'l-meysiru ve'l-ensâbu ve'l-ezlâmu ricsun min 'ameli'ş-şeytân, gloss:şarap, meysir, dikili taşlar ve fal okları şeytan işi pisliklerdir, source:5:90}. Yasaklar arasında {ar:وَمَا ذُبِحَ عَلَى ٱلنُّصُبِ وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ, tr:ve mâ zubiha 'ale'n-nusubi ve en testaksimû bi'l-ezlâm, gloss:dikili taşlar üzerinde kesilen ve fal oklarıyla pay aramanız, source:5:3} de sayılır. Meysir hakkında sorulduğunda da şöyle denir: {ar:قُلْ فِيهِمَآ إِثْمٌۭ كَبِيرٌۭ وَمَنَٰفِعُ لِلنَّاسِ وَإِثْمُهُمَآ أَكْبَرُ مِن نَّفْعِهِمَا, tr:kul fîhimâ ismun kebîrun ve menâfi'u li'n-nâs ve ismuhumâ ekberu min nef'ihimâ, gloss:de ki: ikisinde büyük günah ve insanlar için bazı yararlar vardır, günahları yararlarından büyüktür, source:2:219}. Dikili taşa koşma görüntüsü kıyamette de vardır: {ar:يَوْمَ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ سِرَاعًۭا كَأَنَّهُمْ إِلَىٰ نُصُبٍۢ يُوفِضُونَ, tr:yevme yahrucûne mine'l-ecdâsi sirâ'an keennehum ilâ nusubin yûfidûn, gloss:o gün kabirlerden, dikili bir taşa koşar gibi hızla çıkarlar, source:70:43}. Bu görüntü surenin sözlerine bir karşıtlık ekler. Aynı kökler o sahnede kurayla çekilen bir payı ve kan dökülen taşları adlandırır. Surede ise kolaylık zorlukla birlikte verilir, kurayla çekilmez. Dik duruş da bir taşın önünde değil, "Rabbine" yönelerek yapılır.

Kaynaklar: 94:5 يُسْرًا ي س ر B007; 94:1 نَشْرَحْ ش ر ح B002; 94:8 رَبِّكَ ر ب ب B010; 94:7 فَٱنصَبْ ن ص ب B002; 94:7 فَٱنصَبْ ن ص ب B005; 94:1 صَدْرَكَ ص د ر B006

## Buluşmalar

İlk buluşma yaymak fiilinde olur. Yük yayılmış bir elbisedir: {ar:الوزر حمل الرجل إذا بسط ثوبه فجعل فيه المتاع وحمله, tr:el-vizru himlu'r-raculi izâ basata sevbehû, gloss:vizr, adamın elbisesini yayıp içine eşya koyarak taşıdığı yüktür, source:"و ز ر,B002"}. Göğsün açılması da yaymaktır: {ar:شرح الصدر أي بسطه بنور إلهي وسكينة, tr:şerhu's-sadri ey bastuhû bi-nûrin ilâhiyyin ve sekîne, gloss:göğsü açmak, onu ilahi bir ışık ve huzurla yaymaktır, source:"ش ر ح,B003"}. Böylece iki yayma birbirinin karşısına geçer. Biri elbiseyi yükle doldurup sırta bağlar, öbürü göğsü genişletip ona yer açar. Birinci ve ikinci ayetin sırası buradan anlaşılır: önce göğüs genişler, sonra bohça sırttan alınır. Aynı sahne Musa'nın duasında vezirle birlikte kurulur {source:20:25}. Göğsün açılması, işin kolaylaşması ve yükü taşıyan vezir art arda istenir {source:20:29}. Surede ise vezir yoktur. Yükü taşıyacak kişiyi adlandıran kökten gelen yük, konuşanın kendisi tarafından indirilir. Sığınak anlamı da sona kadar uzanır. Kıyamette {ar:لَا وَزَرَ, tr:lâ vezer, gloss:sığınak yok, source:75:11} denir ve hemen ardından {ar:إِلَىٰ رَبِّكَ, tr:ilâ rabbike, gloss:Rabbine, source:75:12} gelir. Sekizinci ayet aynı iki kelimeyle biter.

İkinci buluşma sırtın bükülmesi ile dik durmak arasında olur. Yapı, yük ve kervan görüntüleri bu noktada birleşir. Üçüncü ayette yük sırta bir sökülme yapmıştır: kemikler gıcırdar, yapı çatırdar, yolda erimiş deve semerinin altında inler. Bu gıcırtı yük ağırlaşınca duyulan sestir: {ar:الظهر إذا أثقله حمله سمع له نقيض, tr:ez-zahru izâ eskalehû himluhû sumi'a lehû nakîd, gloss:sırta yükü ağır gelince ondan gıcırtı işitilir, source:"ن ق ض,B005"}. Ardından gelen fiiller kurma fiilleridir. Yük konur, ad yükseltilir ve yedinci ayette muhataba "dik dur" denir. Nasb da bir şeyi kaldırıp dikmektir: {ar:كل شيء رفعته فقد نصبته, tr:küllü şey'in rafa'tehû fekad nasabteh, gloss:kaldırdığın her şeyi dikmiş olursun, source:"ن ص ب,B001"}. Yükü sırtından alınan kişiden istenen, dik durmaktır. Yük onu eğmişti, şimdi dimdik ayaktadır. Bu duruş yorgunluk da getirir, ama bu yorgunluk yük taşıyan bir sırtın yorgunluğu değildir. Rabbe dönük bir emeğin yorgunluğudur. Kur'an binek sırtından Rabbe doğru giden yolu aynı biçimde anlatır: {ar:لِتَسْتَوُۥا۟ عَلَىٰ ظُهُورِهِۦ ثُمَّ تَذْكُرُوا۟ نِعْمَةَ رَبِّكُمْ, tr:li-testevû 'alâ zuhûrihî summe tezkurû ni'mete rabbikum, gloss:sırtlarına yerleşesiniz, sonra Rabbinizin nimetini anasınız diye, source:43:13}. Binicinin sözü de verilir: {ar:وَإِنَّآ إِلَىٰ رَبِّنَا لَمُنقَلِبُونَ, tr:ve innâ ilâ rabbinâ le-munkalibûn, gloss:biz Rabbimize döneceğiz, source:43:14}. Sırt, zikir ve "Rabbine" bu sahnede de surede olduğu sırayla gelir.

Üçüncü buluşma zikir kelimesinde olur. Mertebe, ses ve hafıza burada birleşir. Zikir hem yüksekliktir hem sestir: {ar:الذكر الشرف والصوت, tr:ez-zikru'ş-şerefu ve's-savt, gloss:zikir şeref ve sestir, source:"ذ ك ر,B007"}. Yükseltmek hem onu duyurmak hem de yaymaktır: {ar:الرفع إذاعة الشيء وإظهاره, tr:er-ref'u izâ'atu'ş-şey'i ve izhâruh, gloss:ref' bir şeyi yaymak ve göstermektir, source:"ر ف ع,B005"}. Sırt ise hem yükü hem de unutulanı taşır. Dördüncü ayetteki tek bir ifade ({ar:رَفَعْنَا لَكَ ذِكْرَكَ, tr:rafa'nâ leke zikrek, gloss:senin için adını yükselttik, source:94:4}) bu üç anlamın hepsini birden karşılar. Sırtın arkasında unutulan ve yükle ezilen değil, yukarıda duran, duyulan ve akılda tutulan bir ad olur. Kur'an kitabı sırtın arkasına atanları anlatır {source:3:187}. Zikirden yüz çevireni de kıyamette yük taşıyan biri olarak gösterir {source:20:100}. Sure bunun tersini kurar: yük iner, zikir yükselir.

Dördüncü buluşma darlık ve genişlik çiftinin üç sahnesinde olur: borç, doğum ve binek. Talak suresi doğumu ve kolaylığı aynı ayette birleştirir {source:65:4}. Emzirmede birbirine güçlük çıkarmayı anar {source:65:6}. Varlıklı ile rızkı daraltılanın harcamasının ardından şöyle der: {ar:سَيَجْعَلُ ٱللَّهُ بَعْدَ عُسْرٍۢ يُسْرًۭا, tr:seyec'alullâhu ba'de 'usrin yusrâ, gloss:Allah bir zorluğun ardından bir kolaylık verecek, source:65:7}. Borç ayeti de darlık içindekine bolluğa kadar süre verilmesini emreder {source:2:280}. Üç sahnede de darlık, taşınan bir şeyin ağırlığıdır: düşülecek borç, doğurulacak çocuk, alıştırılacak binek. Kolaylık ise o ağırlığın yere bırakılmasıdır. İkinci ayetteki indirme fiili bu üç sahnede de kullanılır: borcu düşmek, çocuğu doğurmak, yükü indirmek. Böylece beşinci ve altıncı ayet ilk dört ayeti genelleştirir. Muhatabın yaşadığı bir yük indirme olayı, her ağırlıkta geçerli bir yasaya dönüşür. Bu yasa da "sonra" ile değil, "birlikte" ile söylenir.

Son buluşma boşalan kap ile yönelen işçi arasında olur. Yedinci ayetteki boşalma fiili hem kovanın boşalmasını hem de başka bir işe kasten yönelmeyi anlatır: {ar:فرغت إلى أمر كذا أي عمدت له, tr:ferağtu ilâ emri kezâ ey 'amedtu leh, gloss:şu işe yöneldim, yani ona kasten döndüm, source:"ف ر غ,B006"}. Sekizinci ayetteki rağbet de hem geniş kabı hem de yönelişi anlatır. İlk ayette genişletilen göğüs, son ayette genişlikten gelen bir istekle Rabbe dönük bir kap hâline gelir. Göğsün dünyaya yayılması da mümkündü {source:"ش ر ح,B005"}. Ama son ayetin yönü kesindir. Surenin yapısı da bu hareketi taşır. İlk dört ayette fiilleri "biz" yapar ve muhatap yalnızca alıcıdır: göğsü açılır, yükü indirilir, adı yükseltilir. Ortadaki iki ayet bunu bir yasa olarak söyler. Son iki ayette ise muhatap ilk kez emir alır ve kendisi harekete geçer. İşini bitirir, dik durur ve isteğini Rabbine yöneltir. Sırtından yük alınan kişi ayağa kalkar ve kendisine iyilik yapana döner. Sure açılan bir göğüsle başlar ve o göğsün isteğinin Rabbe yönelmesiyle biter.

