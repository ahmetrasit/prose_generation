Focus: 91:11. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/91_11/D.r13/context.md =====
# 91:11 — focus

كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ

Anchor translation (canonical reading, reference only):

Semud, azgınlığı yüzünden yalanladı.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | كَذَّبَتْ | كَذَّبَ | ك ذ ب | V |
| 2 | ثَمُودُ | ثَمُود |  | PN |
| 3 | بِطَغْوَىٰهَآ | طَغْوَىٰ | ط غ ي | P;N;PRON |


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
- 91:5 وَٱلسَّمَآءِ وَمَا بَنَىٰهَا
- 91:6 وَٱلْأَرْضِ وَمَا طَحَىٰهَا
- 91:7 وَنَفْسٍۢ وَمَا سَوَّىٰهَا
- 91:8 فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا
- 91:9 قَدْ أَفْلَحَ مَن زَكَّىٰهَا
- 91:10 وَقَدْ خَابَ مَن دَسَّىٰهَا
- 91:11 ◀ focus كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ
- 91:12 إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
- 91:13 فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا
- 91:14 فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا
- 91:15 وَلَا يَخَافُ عُقْبَٰهَا


===== _commentary/v16/work/91_11/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ك ذ ب (root_001290) — identity root of كَذَّبَتْ (w1)

- **B001** sözde veya davranışta doğruluğa aykırılık — sözde veya davranışta doğruluğa aykırılık; yalan · yalancı; çok yalan söyleyen kişi · uydurma söz; yalanlar · özürlere kaçınılmaz olarak yalan karışır
  الكذب خلاف الصدق (maqayis;jamhara); الكذاب لغة في الكذب (ayn); كذب كذبا فهو كاذب وكذاب وكذوب (sihah); يقال في المقال والفعال (mufradat)
- **B002** yalan sayma veya yalancı bulma — yalanlama; yalan sayma · birini yalancı saymak veya ona yalan söylediğini bildirmek · birini yalancı bulmak veya yalanını ortaya çıkarmak · seni yalancı saymıyorum
  كذبت فلانا نسبته إلى الكذب وأكذبته وجدته كاذبا (maqayis); كذبته جعلته كاذبا (ayn); كذبت بالحديث كذابا وتكذيبا (jamhara); أكذبت الرجل ألفيته كاذبا وكذبته إذا قلت له كذبت (sihah); كذبته نسبته إلى الكذب (mufradat)
- **B003** onu üstlen; sana düşer [kalıp] — şunu üstlen; sana düşer veya onu yapmalısın
  كذب عليك كذا بمعنى الإغراء أي عليك به أو قد وجب عليك (maqayis); كذب عليكم الحج أي وجب عليكم ودونكم الحج (ayn); كذب عليك كذا وكذا في معنى الإغراء (jamhara); كذب عليكم الحج أي وجب (sihah); كذب عليك الحج قيل معناه وجب فعليك به (mufradat)
- **B004** hamlede duraksamak; olumsuzda sonuna kadar ilerlemek [kalıp] — saldırıya geçti ama duraksadı veya korktu · saldırıya geçti ve vuruncaya kadar durmadı; korkmadı
  حمل فلان ثم كذب أي لم يصدق في الحملة (maqayis); حمل فلان على فلان فما كذب حتى طعن أو ضرب أي ما وقف (jamhara); حمل فلان فما كذب أي ما جبن (sihah); حمل فلان على قرنه فكذب (mufradat)
- **B005** gecikmeden yapmak [kalıp] — yapmakta gecikmedi; hemen yaptı
  ما كذب فلان أن فعل كذا أي ما لبث (maqayis;sihah)
- **B006** sütün kesilmesi veya beklenenden önce tükenmesi [kalıp] — dişi devenin sütü kesildi veya umulduğu kadar sürmedi
  كذب لبن الناقة ذهب وفيه نظر وقياسه صحيح (maqayis); كذب لبن الناقة أي ذهب (sihah); كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم (mufradat)
- **B007** koşup arkasına bakmak için durmak [kalıp] — yaban hayvanı bir mesafe koşup arkasına bakmak için durdu
  كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه (jamhara)
- **B008** iç benlik — iç benlik; kişinin kendisi
  الكذوب النفس (jamhara)
- **B009** dokuma bezemesi sanısı veren boyalı kumaş — dokuma bezemesi sanısı veren boyalı veya desenli kumaş
  الكذابة ثوب يصبغ بألوان الصبغ كأنه موشي (ayn); الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله (mufradat)

## ط غ ي (root_000937) — identity root of بِطَغْوَىٰهَآ (w3)

- **B001** itaatsizlikte veya ölçüde sınırı aşma — sınırı veya ölçüyü aşmak, azmak · itaatsizlikte sınırı aşan, azgın · itaatsizlikte sınır tanımazlık ve azgınlık · sınırı aşma ve azgınlık · sınırı aşma durumu, azgınlık · onu azdırdı veya sınır aşmaya sürükledi · inatçı, kibirli ve sınır tanımaz zorba · Roma hükümdarına verilen unvan
  مجاوزة الحد في العصيان (maqayis;mufradat); جاوز الحد وكل مجاوز حده في العصيان (sihah); كل شيء جاوز القدر فقد طغا (tahdhib); أطغاه المال أي جعله طاغيا (sihah); الطاغية الجبار العنيد (tahdhib)
- **B002** ölçüyü aşarak kabarıp bastırma [kalıp] — sel bol suyla geldi ve kabardı · su olağan düzeyi aşıp yükseldi · denizin dalgaları kabarıp yükseldi · kan kabarıp coştu · çığlık ya da rüzgar ölçüyü aşan güçle baskın geldi
  طغى السيل إذا جاء بماء كثير (maqayis;sihah); طغى الماء خروجه عن المقدار (maqayis); طغى البحر هاجت أمواجه (maqayis;sihah); طغى الدم تبيغ (maqayis;sihah); طغا البحر والماء إذا علا كل شيء فاجترفه (tahdhib); استعير الطغيان فيه لتجاوز الماء الحد (mufradat)
- **B003** yanlış yolun önderi, tapınılan sahte varlık veya saptırıcı zorba güç — yanlış yolun önderi, Tanrı dışında tapınılan varlık veya iyilikten saptıran zorba güç
  الطاغوت الكاهن والشيطان وكل رأس في الضلالة (sihah); كل معبود من دون الله جبت وطاغوت (tahdhib); الطاغوت الشيطان (tahdhib); الطاغوت عبارة عن كل متعد وكل معبود من دون الله (mufradat); الساحر والكاهن والمارد من الجن والصارف عن طريق الخير طاغوتا (mufradat)
- **B004** yıkıma götüren ezici olay veya sınır aşımı — yıkıcı yıldırım veya ceza çığlığı, büyük su baskını ya da yıkıma yol açan sınır aşımı
  الطاغية الصاعقة ويعني صيحة العذاب (sihah); أهلكوا بالطاغية أي بطغيانهم مصدر على فاعلة (tahdhib); فأهلكوا بالطاغية فإشارة إلى الطوفان (mufradat)
- **B005** pürüzsüz kaya yüzeyi, dağ doruğu veya yüksek yer — pürüzsüz ve kaygan kaya yüzeyi · dağın doruğu · yüksek yer
  الطغية الصفاة الملساء (maqayis;tahdhib); الطغية أعلى الجبل (sihah); كل مكان مرتفع طغوة (sihah); تنبي العقاب لملاستها (sihah)

## ECHO ط غ و (root_000936) — for بِطَغْوَىٰهَآ (w3): withheld observed target; not identity

- **B001** başkaldırıda sınırı aşma ve buna sürükleme — başkaldırıda sınırı aşmak · başkaldırıda sınırı aşan · başkaldırıda sınırı aşma · azdırmak; sınırı aşmaya sürüklemek
  مجاوزة الحد في العصيان (maqayis;sihah;mufradat)؛ كل شيء جاوز القدر فقد طغا (tahdhib)؛ أطغاه المال أي جعله طاغيا وأطغاه كذا حمله على الطغيان (sihah;mufradat)
- **B002** su, kan, ses ya da rüzgarın sınırını aşıp baskınlaşması [kalıp] — sel bol suyla taşmak · deniz kabarıp sürükleyici olmak · su olağan düzeyini aşmak · kan coşmak · ses ya da rüzgar baskın gelmek
  طغى السيل إذا جاء بماء كثير (maqayis;sihah)؛ طغى البحر هاجت أمواجه (maqayis;sihah)؛ طغا البحر والماء إذا علا كل شيء فاجترفه (tahdhib)؛ استعير الطغيان فيه لتجاوز الماء الحد (mufradat)
- **B003** hak sınırını aşan saptırıcı veya Tanrı dışında tapınılan varlık — hak sınırını aşan saptırıcı veya Tanrı dışında tapınılan varlık
  الطاغوت الكاهن والشيطان وكل رأس في الضلالة (sihah)؛ كل معبود من دون الله جبت وطاغوت (tahdhib)؛ عبارة عن كل متعد وكل معبود من دون الله والساحر والكاهن والمارد من الجن (mufradat)
- **B004** pervasız ve ezici zorba — pervasız, kendini büyük gören ve insanları ezen zorba
  الطاغية ملك الروم (sihah)؛ الطاغية الجبار العنيد (tahdhib)؛ الذي لا يبالي ما أتى يأكل الناس ويقهرهم (tahdhib)؛ الأحمق المستكبر الظالم (tahdhib)
- **B005** yıkıcı yıldırım ya da çığlık, sınır aşımı veya büyük sel — yıkıcı yıldırım ya da çığlık; sınır aşımı veya büyük sel
  الطاغية الصاعقة ويعني صيحة العذاب (sihah)؛ طغت الصيحة على ثمود (tahdhib)؛ أهلكوا بالطاغية أي بطغيانهم مصدر على فاعلة (tahdhib)؛ إشارة إلى الطوفان المعبر عنه بإنا لما طغى الماء (mufradat)
- **B006** düz ve pürüzsüz kaya, dağ doruğu ya da yüksek yer — düz ve pürüzsüz kaya ya da dağ doruğu · yüksek yer
  الطغية الصفاة الملساء (maqayis;tahdhib)؛ الطغية أعلى الجبل وكل مكان مرتفع طغوة (sihah)
- **B007** bir şeyden küçük parça — herhangi bir şeyden küçük parça
  الطغية من كل شيء نبذة منه (sihah)
- **B008** bir kimsenin ya da topluluğun sesi [kalıp] — bir kimsenin ya da topluluğun sesi
  سمعت طغي فلان أي صوته هذلية؛ سمعت طغي القوم وطهيهم ووغيهم أي صوتهم (tahdhib)
- **B009** yabani sığır yavrusu; bir aktarımda böğüren inek — yabani sığır yavrusu; bir aktarımda böğüren inek
  طغيا وهو الصغير من بقر الوحش (sihah)؛ يقال للبقرة الخائرة والطغيا (tahdhib)

===== _commentary/v16/out/s091/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 91:11, and ## Buluşmalar) =====
## Taşkın ve set

Sekizinci ayet nefse iki şey verir: önce bir fışkırma, sonra bir set. Fucûrun kökü suyun dışarı fırlamasını anlatır ve bunu on ikinci ayetin fiiliyle yapar: {ar:وانفجر الماء وغيره انفجارا إذا انبعث سائلا, tr:ve'nfecera'l-mâu ve ğayruhû inficâran izâ inbe'ase sâilen, gloss:su ve benzeri, akarak fırladığında "infecera" denir, source:"ف ج ر,B001"}. Ahlaktaki anlamı da aynı fiille tanımlanır: {ar:الانبعاث والتفتح في المعاصي فجورا, tr:el-inbi'âsu ve't-tefettuhu fi'l-meâsî fucûran, gloss:günaha atılıp açılmaya fucûr denir, source:"ف ج ر,B004"}. Kökün temelinde ise sapma vardır: {ar:كل مائل عن الحق فاجر, tr:kullu mâilin ani'l-hakkı fâcir, gloss:haktan sapan herkes fâcirdir, source:"ف ج ر,B004"}. Takvâ bunun karşısında, iki şeyin arasına konan bir engeldir: {ar:دفع شيء عن شيء بغيره, tr:def'u şey'in an şey'in bi-ğayrih, gloss:bir şeyi başka bir şey araya koyarak bir şeyden uzak tutmak, source:"و ق ي,B001"}. Engelin konduğu yer de bellidir: {ar:التقوى جعل النفس في وقاية مما يخاف, tr:et-takvâ ce'lu'n-nefsi fî vikâyetin mimmâ yuhâf, gloss:takvâ, nefsi korkulan şeye karşı bir siperin içine koymaktır, source:"و ق ي,B002"}; {ar:اتق الله توقه أي اجعل بينك وبينه كالوقاية, tr:ittaki'llâhe tevakkahu, ey ic'al beyneke ve beynehû ke'l-vikâye, gloss:Allah'tan sakın, yani seninle O'nun arasına bir siper gibi bir şey koy, source:"و ق ي,B002"}. Böylece nefse hem bentten taşan su hem de bendin kendisi bildirilir.

On birinci ayet Semûd'un hangi tarafı seçtiğini söyler: {ar:كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ, tr:kezzebet Semûdu bi-tağvâhâ, gloss:Semûd taşkınlığı yüzünden yalanladı, source:91:11}. Tağvâ, sınırı aşmaktır: {ar:مجاوزة الحد في العصيان, tr:mucâvezetu'l-haddi fi'l-isyân, gloss:isyanda sınırı aşmak, source:"ط غ ي,B001"}. Kökün ilk sahnesi ise sudur: {ar:طغى السيل إذا جاء بماء كثير, tr:tağa's-seylu izâ câe bi-mâin kesîr, gloss:sel, bol suyla geldiğinde "tağâ" denir, source:"ط غ ي,B002"}; {ar:طغا البحر والماء إذا علا كل شيء فاجترفه, tr:tağa'l-bahru ve'l-mâu izâ alâ kulle şey'in fe'cterafeh, gloss:deniz ve su her şeyin üstüne çıkıp onu sürükleyip götürdüğünde "tağâ" denir, source:"ط غ ي,B002"}. Kur'an bu fiziksel anlamı Nûh tufanında kullanır: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tağa'l-mâu hamelnâkum fi'l-câriye, gloss:su taştığında sizi akıp giden gemide taşıdık, source:69:11}. On ikinci ayette taşkın bir kişide yüzeye çıkar: {ar:إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا, tr:izi'nbe'ase eşkâhâ, gloss:en bedbahtları atılıp kalktığında, source:91:12}. Fiil bir şeyi harekete geçirip bir yöne sevk etmektir: {ar:أصل البعث إثارة الشيء وتوجيهه, tr:aslu'l-ba'si isâretu'ş-şey'i ve tevcîhuh, gloss:ba'sın aslı, bir şeyi kaldırıp bir yöne yöneltmektir, source:"ب ع ث,B001"}. Ardından başkalarının gelmesini de içerir: {ar:انبعث القوم في الخير والشر انبعاثا إذا تتابعوا, tr:inbe'ase'l-kavmu fi'l-hayri ve'ş-şerri inbi'âsen izâ tetâba'û, gloss:kavim iyilikte ya da kötülükte birbiri ardınca atıldığında "inbe'ase" denir, source:"ب ع ث,B004"}. Sekizinci ayetteki fucûru ve suyun fırlamasını tanımlayan fiil, on ikinci ayette en bedbahtın kalkışıdır. Nefse verilen fışkırma, Semûd'da bir adamın atılışı olur ve kavim onun ardından akar.

Kur'an aynı fiili Allah'ın istemediği bir çıkış için de kullanır. Savaşa çıkmayan münafıklar için şöyle der: {ar:وَلَٰكِن كَرِهَ ٱللَّهُ ٱنۢبِعَاثَهُمْ فَثَبَّطَهُمْ, tr:ve lâkin kerihe'llâhu'nbi'âsehum fe-sebbetahum, gloss:ama Allah onların harekete geçmesini istemedi ve onları alıkoydu, source:9:46}. İnsanın taşma eğilimini de açıkça adlandırır: {ar:بَلْ يُرِيدُ ٱلْإِنسَٰنُ لِيَفْجُرَ أَمَامَهُۥ, tr:bel yurîdu'l-insânu li-yefcura emâmeh, gloss:bilakis insan, önündeki günleri de yarıp taşmak ister, source:75:5}; {ar:كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ, tr:kellâ inne'l-insâne le-yatğâ, gloss:hayır, insan gerçekten taşar, source:96:6}; {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en raâhu'staÄŸnâ, gloss:kendini yeterli gördüğü için, source:96:7}. Nâziât Suresi'nde Allah, Mûsâ'yı taşan birine gönderir ve ona büyüme yolunu teklif ettirir: {ar:ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ, tr:izheb ilâ Fir'avne innehû tağâ, gloss:Firavun'a git, o taştı, source:79:17}; {ar:فَقُلْ هَل لَّكَ إِلَىٰٓ أَن تَزَكَّىٰ, tr:fe-kul hel leke ilâ en tezekkâ, gloss:de ki: arınıp büyümeye ne dersin, source:79:18}. Taşkın ile büyüme orada da karşı karşıya durur. Aynı surede iki sonuç yan yana sayılır: {ar:فَأَمَّا مَن طَغَىٰ, tr:fe-emmâ men tağâ, gloss:taşana gelince, source:79:37}; {ar:وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve emmâ men hâfe makâme rabbihî ve neha'n-nefse ani'l-hevâ, gloss:Rabbinin huzurunda durmaktan korkup nefsi arzudan alıkoyana gelince, source:79:40}. Nefsi alıkoymak, bendin işidir. Salih de Semûd'dan tam olarak bunu ister ve onları taşkınlara uymaktan alıkoymaya çalışır: {ar:فَٱتَّقُوا۟ ٱللَّهَ وَأَطِيعُونِ, tr:fe'ttakullâhe ve etî'ûn, gloss:Allah'tan sakının ve bana uyun, source:26:150}; {ar:وَلَا تُطِيعُوٓا۟ أَمْرَ ٱلْمُسْرِفِينَ, tr:ve lâ tutî'û emra'l-musrifîn, gloss:ölçüyü aşanların buyruğuna uymayın, source:26:151}.

Taşkın sonunda dönüp taşanı alır. Kök, Semûd'un neyle helak olduğunu kendi adıyla söyler: {ar:أهلكوا بالطاغية أي بطغيانهم, tr:uhlikû bi't-tâğıye, ey bi-tuğyânihim, gloss:tâğıye ile helak edildiler, yani kendi taşkınlıklarıyla, source:"ط غ ي,B004"}. Kur'an'daki karşılığı da aynı kelimedir: {ar:فَأَمَّا ثَمُودُ فَأُهْلِكُوا۟ بِٱلطَّاغِيَةِ, tr:fe-emmâ Semûdu fe-uhlikû bi't-tâğıye, gloss:Semûd'a gelince, o taşkın şeyle helak edildiler, source:69:5}. Fecr Suresi'nde Âd, Semûd ve Firavun için taşkının karşılığı yukarıdan dökülen bir azaptır: {ar:ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ, tr:ellezîne tağav fi'l-bilâd, gloss:ülkelerde taşanlar, source:89:11}; {ar:فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ, tr:fe-sabbe aleyhim rabbuke savte azâb, gloss:Rabbin de üstlerine bir azap kamçısı döktü, source:89:13}. Fucûr kelimesinin kendisi de bu dönüşü taşır: {ar:انفجرت عليهم الدواهي إذا جاءهم الكثير منها بغتة, tr:infecerat aleyhimu'd-devâhî izâ câehumu'l-kesîru minhâ bağteten, gloss:belalar ansızın ve çok sayıda geldiğinde "üstlerine fışkırdı" denir, source:"ف ج ر,B003"}. Düz bir anlatım "isyan ettiler, cezalandırıldılar" der. Bu imge ise cezayı suçun suyuyla gösterir: içte bent yıkılır, dışta sel gelir.

Kaynaklar: 91:8 فُجُورَهَا ف ج ر B001; 91:8 فُجُورَهَا ف ج ر B003; 91:8 فُجُورَهَا ف ج ر B004; 91:8 تَقْوَىٰهَا و ق ي B001; 91:8 تَقْوَىٰهَا و ق ي B002; 91:11 بِطَغْوَىٰهَآ ط غ ي B001; 91:11 بِطَغْوَىٰهَآ ط غ ي B002; 91:11 بِطَغْوَىٰهَآ ط غ ي B004; 91:12 ٱنۢبَعَثَ ب ع ث B001; 91:12 ٱنۢبَعَثَ ب ع ث B004

## Gönderilen ve peşine düşülen

Surenin başında doğru bir izleme vardır: ay güneşi izler. İzleme fiilinin bir kolu, vahyedilmiş kitabı izlemeyi anlatır: {ar:التلاوة تختص باتباع كتب الله المنزلة تارة بالقراءة وتارة بالارتسام, tr:et-tilâvetu tahtessu bi'ttibâ'i kutubi'llâhi'l-munzele, târeten bi'l-kırâe ve târeten bi'l-irtisâm, gloss:tilâvet, Allah'ın indirdiği kitapları izlemeye mahsustur; bazen okuyarak, bazen izine uyarak, source:"ت ل و,B002"}. İkinci ayetteki ayın işi, on üçüncü ayette elçinin getirdiği sözü izlemenin ölçüsü olur.

Elçinin adının kökü, salıvermeyi ve uzanmayı anlatır: {ar:أصل واحد يدل على الانبعاث والامتداد, tr:aslun vâhidun yedullu ale'l-inbi'âsi ve'l-imtidâd, gloss:harekete geçmeyi ve uzanmayı gösteren tek bir kök, source:"ر س ل,B001"}; {ar:الإرسال يقابل الإمساك, tr:el-irsâlu yukâbilu'l-imsâk, gloss:irsâl, tutmanın karşıtıdır, source:"ر س ل,B001"}. Elçi taşıdığı sözün adıyla da anılır: {ar:الرسول يقال للقول المتحمل وتارة لمتحمل القول والرسالة, tr:er-rasûlu yukâlu li'l-kavli'l-mutehammel, ve târeten li-mutehammili'l-kavli ve'r-risâle, gloss:resûl, taşınan söze de, sözü ve mesajı taşıyana da denir, source:"ر س ل,B002"}. Gönderme fiili ile on ikinci ayetin fiili aynı aileye bağlanır: {ar:ولقد بعثنا في كل أمة رسولا نحو أرسلنا رسلنا, tr:ve le-kad ba'asnâ fî kulli ummetin rasûlen, nahvu erselnâ rusulenâ, gloss:"her ümmete bir elçi ba'as ettik" sözü, "elçilerimizi irsâl ettik" gibidir, source:"ب ع ث,B002"}. Kur'an'daki karşılığı bir ayette göndermeyi, inkârı ve sonucu birlikte toplar: {ar:وَلَقَدْ بَعَثْنَا فِى كُلِّ أُمَّةٍۢ رَّسُولًا, tr:ve le-kad ba'asnâ fî kulli ummetin rasûlen, gloss:andolsun, her ümmete bir elçi gönderdik, source:16:36}. Aynı ayet şöyle biter: {ar:فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ, tr:fe'nzurû keyfe kâne âkıbetu'l-mukezzibîn, gloss:yalanlayanların sonunun nasıl olduğuna bakın, source:16:36}. On ikinci ayette ise fiil, göndereni olmayan bir kalkış biçiminde gelir. Allah'ın göndermesine karşılık bir adam kendini gönderir.

Bu adam kavmin başındadır ve kavmin en bedbahtıdır: {ar:الشقوة خلاف السعادة, tr:eş-şikvetu hılâfu's-seâde, gloss:şikve, mutluluğun karşıtıdır, source:"ش ق و,B001"}. Kavim de onun peşine düşer. On dördüncü ayetteki "zenb" kelimesinin bir kolu bu izleyenlerin adıdır: {ar:ذنب الرجل أتباعه وأذناب القوم أتباع الرؤساء, tr:zenebu'r-raculi etbâ'uh, ve ezenâbu'l-kavmi etbâ'u'r-ruesâ', gloss:adamın kuyruğu, ona uyanlardır; kavmin kuyrukları, reislere uyanlardır, source:"ذ ن ب,B003"}. On beşinci ayetteki kelimenin kökü de birinin izinden gelmeyi anlatır: {ar:العاقب الذي يجيء في أثر صاحبه, tr:el-âkıbu'llezî yecîu fî eseri sâhibih, gloss:âkıb, arkadaşının izinden gelendir, source:"ع ق ب,B005"}. İzlenmesi gereken elçi ise yalanlanır: {ar:كذبته نسبته إلى الكذب, tr:kezzebtuhû: nesebtuhû ile'l-kezib, gloss:onu yalanladım, yani ona yalan isnat ettim, source:"ك ذ ب,B002"}. Kavmin elçiye cevabı söze karşı söz olarak gelir. Elçi "ve kâle", "dedi ki" diye konuşur: {ar:القول من النطق, tr:el-kavlu mine'n-nutk, gloss:kavl, konuşmadan gelir, source:"ق و ل,B001"}.

Kur'an Semûd'un bu reddini kendi sözleriyle aktarır. Bir insanı izlemeyi küçümserler: {ar:أَبَشَرًۭا مِّنَّا وَٰحِدًۭا نَّتَّبِعُهُۥٓ, tr:e beşeren minnâ vâhiden nettebi'uh, gloss:aramızdan tek bir insana mı uyacağız, source:54:24}. Ve onu yalancılıkla suçlarlar: {ar:بَلْ هُوَ كَذَّابٌ أَشِرٌۭ, tr:bel huve kezzâbun eşir, gloss:hayır, o şımarık bir yalancıdır, source:54:25}. Aynı sure, tek bir adamın ardına düşüldüğü sahneyle sürer: {ar:فَنَادَوْا۟ صَاحِبَهُمْ فَتَعَاطَىٰ فَعَقَرَ, tr:fe-nâdev sâhibehum fe-teâtâ fe-akar, gloss:arkadaşlarını çağırdılar; o da eline aldı ve ayaklarını biçti, source:54:29}. Elçiye uymayı reddedenler, kendi seçtikleri adamı izler. A'râf Suresi'nde de büyüklenen ileri gelenler müminlere sorar: {ar:أَتَعْلَمُونَ أَنَّ صَٰلِحًۭا مُّرْسَلٌۭ مِّن رَّبِّهِۦ, tr:e ta'lemûne enne Sâlihan murselun min rabbih, gloss:Salih'in Rabbi tarafından gönderildiğini mi biliyorsunuz, source:7:75}. Deveyi biçtikten sonra da alay ederler: {ar:إِن كُنتَ مِنَ ٱلْمُرْسَلِينَ, tr:in kunte mine'l-murselîn, gloss:eğer gönderilenlerdensen, source:7:77}. Şuarâ Suresi'nde de anlatım bir yalanlamayla açılır: {ar:كَذَّبَتْ ثَمُودُ ٱلْمُرْسَلِينَ, tr:kezzebet Semûdu'l-murselîn, gloss:Semûd gönderilenleri yalanladı, source:26:141}. Salih'in kendini tanıtması da şudur: {ar:إِنِّى لَكُمْ رَسُولٌ أَمِينٌۭ, tr:innî lekum rasûlun emîn, gloss:ben size gönderilmiş güvenilir bir elçiyim, source:26:143}. Neml Suresi bu izleyiciliğin içindeki bir çekirdekten bahseder: {ar:وَكَانَ فِى ٱلْمَدِينَةِ تِسْعَةُ رَهْطٍۢ, tr:ve kâne fi'l-medîneti tis'atu rahtin, gloss:şehirde dokuz kişilik bir çete vardı, source:27:48}. Elçinin son sözü, taşıdığı yükü teslim ettiğidir: {ar:لَقَدْ أَبْلَغْتُكُمْ رِسَالَةَ رَبِّى, tr:le-kad eblağtukum risâlete rabbî, gloss:Rabbimin mesajını size ulaştırdım, source:7:79}. Düz bir anlatım "yalanladılar" der. Bu imge ise iki izleme hattı çizer: biri gökte ve doğru, ay güneşin ardından gider; öteki yerde ve yanlış, kavim kendi en bedbahtının ardından gider. Birinde sıra korunur, ötekinde başa geçen, peşindekileri yıkıma götürür.

Kaynaklar: 91:2 تَلَىٰهَا ت ل و B001; 91:2 تَلَىٰهَا ت ل و B002; 91:11 كَذَّبَتْ ك ذ ب B002; 91:12 ٱنۢبَعَثَ ب ع ث B002; 91:12 أَشْقَىٰهَا ش ق و B001; 91:13 فَقَالَ ق و ل B001; 91:13 رَسُولُ ر س ل B001; 91:13 رَسُولُ ر س ل B002; 91:14 فَكَذَّبُوهُ ك ذ ب B002; 91:14 بِذَنۢبِهِمْ ذ ن ب B003; 91:15 عُقْبَٰهَا ع ق ب B005

## Buluşmalar

İlk buluşma sekizinci ayette olur. "Fucûr" kelimesi aynı kökten üç sahneyi bir arada tutar: geceyi yaran şafağı, bentten fırlayan suyu ve din perdesini yırtmayı. Gökte yarılma ışık getirir, nefiste ise koruyucu örtüyü yırtar ve bir taşkın başlatır. Takvâ aynı ayette hem bir örtüdür hem de bir settir. Tek bir kelime bu iki imgeyi birlikte taşır: örten ve alıkoyan. Böylece surenin başındaki düzenli nöbet nefsin içine taşınır. Gece güneşin üstünü sırası gelince örter ve sırası gelince açılır. Nefis ise ya kendi örtüsünü yerinde tutar ya da onu yırtıp taşar.

İkinci buluşma on ikinci ayetteki "inbe'ase" fiilindedir. Bu fiil üç imgeyi birden toplar. Fucûru tanımlayan atılıştır, deveyi köstekinden çözüp kaldırmanın sonucudur ve Allah'ın elçi gönderişinin eşi olan bir fiildir. Deve sürücüsünün dilinde biri kaldırır, deve kalkar. Bu ayette ise kaldıran yoktur. Adam kendi kendine, köstekinden kurtulmuş bir hayvan gibi kalkar ve Allah'ın gönderdiği deveye yönelir. Elçi gönderilmiştir, deve gönderilmiştir. Taşkın olan ise kendini gönderir.

Üçüncü buluşma, on dördüncü ayetten on beşinciye geçen bedenin arka ucudur. "Akr" topuk kirişini keser. O kirişin adı on beşinci ayetteki "ukbâ" kelimesinin kökündendir. Günahın adı olan "zenb" de hayvanın arka ucunun adıdır. Devenin imgesi ile suçun ardından gelen sonucun imgesi böylece aynı noktada birleşir. Kavim devenin arkasına vurur; karşılık da onların "arkalarından", yani günahlarının ardından gelir. Kova ile günahın aynı kökten gelmesi bunu ölçüye bağlar. Devenin su payını çiğneyenler kendi kova paylarını alırlar.

Dördüncü buluşma "sevvâ" fiilindedir. Bu fiil göğün ve nefsin bitirilişini Semûd'un yerle bir edilişine bağlar. Altıncı ayetteki yayılmış yer bu iki ucun arasında durur. Kavim ovaya saray kurmuştu. Yayılan yere kurulan sarayları yayılmış bir yer gibi dümdüz olur. Gökten yağan su, sürülen toprak ve büyüyen ekin bu yere bağlıdır. Hurmanın başını kesmeyi ve hiçbir şey bitirmeyen kumu anlatan "akr" fiili, kavmin tarlasını bir çorak yere çevirir.

Bu buluşmalar birlikte surenin hareketini taşır. Sure, her cismin yerini bildiği bir gökle başlar: ışık yayılır, ay onu izler, gündüz açar, gece örter. Ardından gök ve yerden bir ev kurulur ve aynı el nefsi bu evin üçüncü yapısı olarak düzenler. Nefse iki lokma yutturulur: hem yırtan ve taşan hem de örten ve alıkoyan. Dokuzuncu ve onuncu ayetler bu iki lokmanın sonucunu iki tarla gibi gösterir: biri sürülmüş ve büyümüş, öbürü gömülmüş. Semûd ise yanlış yolu seçer. Sınırı aşar, kendi en bedbahtının ardına düşer, gönderilen deveyi arkasından biçer. Karşılık gece gibi üstlerine kapanır ve evleri ile birlikte onları yayılmış bir yer gibi dümdüz eder. Sure, gece ile gündüzün nöbetleşmesini de adlandıran bir kelimeyle kapanır. Ama bu son nöbette, hükmün ardından gelecek ve onu geri çevirecek hiçbir şey yoktur.

