Focus: 92:14. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/92_14/D.r13/context.md =====
# 92:14 — focus

فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ

Anchor translation (canonical reading, reference only):

Bu yüzden sizi alevlenen bir ateşe karşı uyardım.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَأَنذَرْتُكُمْ | أَنذَرَ | ن ذ ر | REM;V;PRON |
| 2 | نَارًا | نَار | ن و ر | N |
| 3 | تَلَظَّىٰ | تَلَظَّىٰ | ل ظ ي | V |


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
- 92:8 وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
- 92:9 وَكَذَّبَ بِٱلْحُسْنَىٰ
- 92:10 فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- 92:11 وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
- 92:12 إِنَّ عَلَيْنَا لَلْهُدَىٰ
- 92:13 وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- 92:14 ◀ focus فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- 92:15 لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- 92:16 ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- 92:17 وَسَيُجَنَّبُهَا ٱلْأَتْقَى
- 92:18 ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- 92:19 وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- 92:20 إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- 92:21 وَلَسَوْفَ يَرْضَىٰ


===== _commentary/v16/work/92_14/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن ذ ر (root_001488) — identity root of فَأَنذَرْتُكُمْ (w1)

- **B001** tehlikeyi bildirerek sakındırma — uyarı amacıyla korkulacak bir şeyi bildirme · bir topluluğa korkulacak bir durumu haber verip sakındırmak · uyaran kişi veya uyarının kendisi · uyaranlar ya da uyarılar · birbirini korkutucu bir tehlikeye karşı uyarmak · düşmandan haberdar olup hazırlık ve sakınma durumuna geçmek · ani tehlikeyi haber veren kişi için kullanılan temsil · önceden ceza veya sonuç bildiren kişinin gerekçesini tamamladığını anlatan söz · ordunun düşman durumunu bildiren öncü gözcüsü
  الإنذار الإبلاغ ولا يكاد يكون إلا في التخويف؛ تناذروا خوف بعضهم بعضا؛ النذير المنذر والجمع النذر (maqayis)؛ الانذار الابلاغ ولايكون إلا في التخويف؛ النذير المنذر؛ تناذر القوم كذا أي خوف بعضهم بعضا؛ نذر القوم بالعدو إذا علموا (sihah)؛ الإنذار الإعلام بالشيء الذي يحذر منه؛ أنذرت القوم مسير عدوهم إليهم فنذروا أي علموا فتحرزوا؛ أنا النذير العريان (tahdhib)؛ الإنذار إخبار فيه تخويف؛ النذير المنذر؛ النذر جمعه؛ وقد نذرت أي علمت ذلك وحذرت (mufradat)
- **B002** kendine adak yükümlülüğü koyma — kişinin kendi üzerine sonradan gerekli kıldığı adak yükümlülüğü · kendi üzerine bir şeyi gerekli kılmak veya şarta bağlı söz vermek · Tanrı için kendi üzerine bir yükümlülük almak · kendi üzerine adak yükümlülüğü almak · adak yoluyla ibadethane hizmetine ayrılan çocuk
  النذر وهو أنه يخاف إذا أخلف؛ النذر أيضا ما يجب كأنه نذر أي أوجب (maqayis)؛ النذر واحد النذور؛ نذرت لله كذا؛ نذر على نفسه نذرا (sihah)؛ النذر ما ينذره الإنسان فيجعله على نفسه نحبا واجبا؛ نذرت على نفسي أي أوجبت؛ النذر ما كان وعدا على شرط (tahdhib)؛ النذر أن توجب على نفسك ما ليس بواجب لحدوث أمر؛ نذرت لله أمرا (mufradat)
- **B003** yaralama için gereken tazminat — yaralamalarda ödenmesi gereken tazminat veya kan bedeli · kemiği açığa çıkaran yara için gereken tazminat
  نذر الموضحة في الحديث منه (maqayis)؛ ما يجب في الجراحات من الديات نذرا؛ أهل العراق يسمونه الأرش؛ النذور لا تكون إلا في الجراح صغارها وكبارها؛ لي قبل فلان نذر إذا كان جرحا واحدا له عقل؛ نصف نذر الموضحة (tahdhib)

## ن و ر (root_001564) — identity root of نَارًا (w2)

- **B001** ışık ve aydınlatma — ışık, aydınlık · ışık vermek, aydınlanmak veya aydınlatmak · aydınlatma; günün ağarması
  النور الضياء والفعل نار وأنار ونورا وإنارة واستنار أي أضاء (ayn)؛ النور: الضياء؛ أنار الشئ واستنار بمعنى أي أضاء؛ التنوير: الإنارة؛ التنوير: الإسفار (sihah)؛ أصل صحيح يدل على إضاءة واضطراب وقلة ثبات؛ النور والنار سميا بذلك من طريقة الإضاءة (maqayis)
- **B002** yanan ateş ve ateşle yapılan hayvan damgası — yanan ateş · ateşler · devenin ateşle yapılmış damgası · hayvanın soyu damgasından belli olur
  النار مؤنثة وهي من الواو؛ الجمع نور ونيران (sihah)؛ ما نار هذه الناقة أي ما سمتها؛ نجارها نارها؛ سماتها (sihah)؛ النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة (maqayis)
- **B003** ateşi uzaktan görüp ona yönelmek [kalıp] — ateşe doğru yönelmek · ateşi uzaktan görüp seçmek
  تنورت نارا قصدت إليها (ayn)؛ تنورت النار من بعيد: تبصرتها (sihah)؛ تنورت النار تبصرتها (maqayis)
- **B004** ağaç çiçeği ve çiçeklenme — ağaç çiçeği · ağaç çiçekleri; tek bir ağaç çiçeği · ağaç çiçek açtı · ağacın çiçek açması
  النور نور الشجر؛ تنوير الشجرة إزهارها؛ النوار نور الشجر (ayn)؛ تنوير الشجرة: إزهارها؛ نورت الشجرة وأنارت أي أخرجت نورها؛ النوار نور الشجر (sihah)؛ ومنه النور نور الشجر ونواره؛ أنارت الشجرة أخرجت النور (maqayis)
- **B005** yol gösteren belirgin işaret ve yüksek yapı — yol gösteren belirgin işaret · arazinin sınırları ve belirgin işaretleri · yol gösteren, üstünde ışık bulunan veya çağrı yapılan yüksek yapı
  المنارة مفعلة من الإنارة؛ كانوا ينورون في الجاهلية ليهتدى ويقتدى بها؛ المنارة الشمعة ذات السراج؛ المنارة ما يوضع عليه للمسرجة؛ المنارة للمؤذن (ayn)؛ المنار: علم الطريق؛ ضرب المنار على طريقه ليهتدى بها؛ المنارة التي يؤذن عليها؛ المنارة ما يوضع فوقها السراج (sihah)؛ المنارة مفعلة من الاستنارة؛ منار الأرض حدودها وأعلامها سميت لبيانها وظهورها (maqayis)
- **B006** ürkmek, kaçınmak ve uzaklaştırmak — kötülükten veya erkeklerden uzak duran iffetli kadın · ürkek ve insandan kaçan ceylanlar · kuşku verici durumdan uzak duran kadınlar · eşinden ürküp kaçınan kısrak veya inek · bir şeyden ürküp uzaklaşmak · birini söz veya davranışla ürkütüp uzaklaştırmak · ürkme, kaçınma ve uzaklaşma
  امرأة نوار وهي العفيفة النافرة عن الشر والقبيح؛ التي تكره الرجال؛ بقرة نوار تنفر من الفحل؛ نرت فلانا أي أنفرته (ayn)؛ النور أيضا: النفر من الظباء؛ نسوة نور أي نفر من الربية؛ الواحدة نوار وهي الفرور؛ فرس وديق نوار؛ نرت من الشئ؛ نرت غيري أي نفرته (sihah)؛ امرأة نوار أي عفيفة تنور أي تنفر من القبيح؛ نارت نفرت؛ نرت فلانا نفرته؛ النوار النفار (maqayis)
- **B007** topluluklar arası düşmanlık ve kin — topluluklar arasında çıkan düşmanlık ve kin
  النائرة الكائنة تقع بين القوم (ayn)؛ بينهم نائرة أي عداوة وشحناء (sihah)
- **B008** göz boyası ve dövme için kullanılan duman karası — göz boyası veya dövme için kullanılan fitil ya da yağ dumanı karası · deriyi veya diş etini iğneleyip üzerine duman karası ya da göz boyası serpmek
  النؤور دخان الفتيلة يتخذ كحلا أو وشما (ayn)؛ النوور: النيلج، وهو دخان الشحم يعالج به الوشم؛ وقد نور ذراعه إذا غرزها بإبرة ثم ذر عليها النوور (sihah)؛ مما شذ عن هذا الأصل النؤور دخان الفتيلة يتخذ كحلا ووشما؛ نورت اللثة غرزتها بإبرة ثم جعلت في الغرز الإثمد (maqayis)
- **B009** bedene sürülen özel karışım ve onu sürünme — bedene sürülen özel karışım · özel karışımı bedenine sürmek
  النورة يطلى بها (ayn)؛ تنور الرجل: تطلى بالنورة (sihah)
- **B010** bir işi karışık gösterip yanıltmak [kalıp] — bir işi birine karışık gösterip onu yanıltmak
  فلان ينور على فلان إذا شبه عليه أمرا؛ ليست الكلمة بعربية محضة؛ امرأة كانت تسمى نورة (ayn)
- **B011** açıkça seçilen veya belirgin biçimde çıkan şey — yolun belirgin oluğu · kumaşın belirgin işareti veya çizgisi · çift hayvanının boynundaki boyunduruk ve takımı · gücü başkasının iki katı olan adam
  النون والياء والراء كلمة تدل على وضوح شيء وبروزه؛ أخدود الطريق الواضح منه نير؛ نير الثوب علمه؛ النير الخشبة على عنق الفدان؛ ما ننكر أن يكون أصل هذا كله الواو فيرجع إلى ما ذكرناه في باب النور والنار (maqayis)

## ل ظ ي (root_001357) — identity root of تَلَظَّىٰ (w3)

- **B001** saf alev ve ateşin alevlenip harlanması — ateş; saf alev · ateşin tutuşup alevlenmesi · alevlenmek, parlayıp harlanmak · ateş tutuşup alevlendi
  اللظى النار (sihah)؛ التظاء النار التهابها وتلظيها تلهبها (sihah)؛ تلظت النار تلظيا إذا التهبت (tahdhib)؛ اللظى اللهب الخالص (tahdhib;mufradat)؛ نارا تلظى أي تتوهج وتتوقد (tahdhib)؛ لظيت النار تلظى لظى (tahdhib)؛ لظيت النار وتلظت (mufradat)
- **B002** tam çekimlenmeyen, ateşin ve öte dünyadaki ateşli ceza yerinin özel adı — ateşin ya da öte dünyadaki ateşli ceza yerinin tam çekimlenmeyen özel adı
  لظى اسم من أسماء النار معرفة لا ينصرف (sihah)؛ لظى من أسماء النار وهي معرفة لا تنون لأنها لا تنصرف (tahdhib)؛ لظى غير مصروفة اسم لجهنم (mufradat)
- **B003** birine karşı öfkeden parlamak [kalıp] — birine karşı yoğun öfkeden parlamak
  فلان يتلظى على فلان تلظيا إذا توقد عليه من شدة الغضب (tahdhib)
- **B004** şiddetli sıcaklık — şiddetli sıcaklık
  جعل ذو الرمة اللظى شدة الحر (tahdhib)

===== _commentary/v16/out/s092/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 92:14, and ## Buluşmalar) =====
## Örten gece, yarılan gündüz

Surenin ilk iki ayeti iki vakit adı verir, ama asıl taşıdıkları şey iki işlemdir. Birinci ayetteki fiil {ar:يَغْشَىٰ, tr:yağşâ, gloss:örter, source:92:1} bir şeyin üstüne başka bir şeyin serilmesini anlatır. Kökün temel anlamı {ar:أصل صحيح يدل على تغطية شيء بشيء, tr:aslun sahîhun yedüllü alâ tağtiyeti şey'in bi-şey', gloss:bir şeyin başka bir şeyle örtülmesini gösteren sağlam kök, source:"غ ش و,B001"} diye verilir. Bu işin aleti de aynı köktendir: {ar:الغشاء الغطاء, tr:el-ğışâu'l-ğıtâ', gloss:ğışâ örtü demektir, source:"غ ش و,B001"}. Gece kendi başına değil, karşısındakiyle tanımlanır: {ar:الليل خلاف النهار, tr:el-leylü hılâfü'n-nehâr, gloss:gece gündüzün karşıtıdır, source:"ل ي ل,B001"}. Ayette gecenin neyi örttüğü söylenmez, fiilin nesnesi yoktur. Bir önceki surede aynı iki fiil nesneleriyle gelmişti: {ar:وَٱلنَّهَارِ إِذَا جَلَّىٰهَا, tr:ve'n-nehâri izâ cellâhâ, gloss:onu açığa çıkardığında gündüze andolsun, source:91:3} ve {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰهَا, tr:ve'l-leyli izâ yağşâhâ, gloss:onu örttüğünde geceye andolsun, source:91:4}. Orada örtülüp açılan şey güneşti. Burada nesne düşer ve örtü belli bir şeyin değil, görünen her şeyin üstüne serilir. Gündüzün fiili de değişir: {ar:وَٱلنَّهَارِ إِذَا تَجَلَّىٰ, tr:ve'n-nehâri izâ tecellâ, gloss:açılıp göründüğünde gündüze andolsun, source:92:2}. Gündüz artık başka bir şeyi göstermez, kendini gösterir.

Bu yazıda bir kelimenin kök ailesinden gelen görüntüler, kelimenin ayetteki anlamının yanında duyulur. O anlamın yerine geçmezler. Gündüzün işleyişi bu ailede üç katmanda görünür. İlk katmanda ışık yayılır: gündüz {ar:الوقت الذي ينتشر فيه الضوء, tr:el-vaktu'llezî yenteşiru fîhi'd-dav', gloss:ışığın yayıldığı vakit, source:"ن ه ر,B002"} diye tanımlanır. İkinci katmanda kökün genel resmi bir açılmadır: {ar:أصل صحيح يدل على تفتح شيء أو فتحه, tr:aslun sahîhun yedüllü alâ tefettuhi şey'in ev fethih, gloss:bir şeyin açılıvermesini ya da açılmasını gösteren sağlam kök, source:"ن ه ر,B003"}. Üçüncü katmanda nehir de adını buradan alır: {ar:سمي النهر لأنه ينهر الأرض أي يشقها, tr:sümmiye'n-nehru li-ennehû yenhuru'l-arda ey yeşukkuhâ, gloss:nehre bu ad verildi çünkü toprağı yarar, source:"ن ه ر,B001"}. Gündüzün fiilinin kökü ise {ar:انكشاف الشيء وبروزه, tr:inkişâfü'ş-şey'i ve burûzuh, gloss:bir şeyin üstünün açılması ve öne çıkması, source:"ج ل و,B001"} demektir. Aynı kökte {ar:الجلي نقيض الخفي, tr:el-celiyyu nakîdu'l-hafiyy, gloss:açık olan gizlinin zıddıdır, source:"ج ل و,B001"} denir ve bulutsuz gök için {ar:السماء جلواء أي مصحية, tr:es-semâu celvâu ey mushiye, gloss:gök açık yani bulutsuz, source:"ج ل و,B007"} kullanılır. Sahne böylece kurulur: Gece üstten serilen bir katmandır. Gündüz bu katmanı nehrin toprağı yarması gibi yarar, ışık yayılır ve altta kalan şey öne çıkıp seçilir hâle gelir. Düz bir anlatım "geceye ve gündüze yemin" deyip geçer. İşlem görülünce yemin, surenin geri kalanının modelini verir: İnsanların koşusu bir süre aynı örtünün altında birbirine benzer, sonra gün yarılınca {ar:إِنَّ سَعْيَكُمْ لَشَتَّىٰ, tr:inne sa'yeküm leşettâ, gloss:sizin koşunuz elbette dağınık ve ayrı ayrıdır, source:92:4} hükmü görünür olur.

Kur'an iki işlemi başka yerlerde de yan yana sahneler. Allah gökleri ve yeri yaratan Rab olarak kendini anlatırken geceyi gündüzün üstüne çeker: {ar:يُغْشِى ٱلَّيْلَ ٱلنَّهَارَ يَطْلُبُهُۥ حَثِيثًا, tr:yuğşi'l-leyle'n-nehâra yatlubuhû hasîsâ, gloss:geceyi gündüzün üstüne örter ve gece onu hızla kovalar, source:7:54}. Aynı ayet {ar:أَلَا لَهُ ٱلْخَلْقُ وَٱلْأَمْرُ, tr:elâ lehu'l-halku ve'l-emr, gloss:bilin ki yaratmak da buyurmak da O'nundur, source:7:54} diye kapanır ve üçüncü ayetin fiilini, yaratmayı, örtünün hemen yanına koyar. Başka bir ayette işlem tersten görülür, gündüz gecenin üstünden soyulan bir deridir: {ar:ٱلَّيْلُ نَسْلَخُ مِنْهُ ٱلنَّهَارَ, tr:el-leylü neslehu minhü'n-nehâr, gloss:gece; ondan gündüzü soyarız, source:36:37}. Gündüzün fiilinin en ağır kullanımı Musa'nın sahnesindedir. Musa Rabbini görmek istemiş, ona dağa bakması söylenmiştir: {ar:فَلَمَّا تَجَلَّىٰ رَبُّهُۥ لِلْجَبَلِ, tr:fe-lemmâ tecellâ rabbuhû li'l-cebel, gloss:Rabbi dağa tecellî edince, source:7:143}. Ayetin devamında dağ dümdüz olur ve Musa bayılıp düşer. Açılmanın gücü, örtünün neyi koruduğunu da gösterir.

Aynı aile örtüyü göze de taşır. Gözün ya da kalbin üstündeki zar da bu köktendir: {ar:الغشاوة ما غشي القلب من رين الطبع, tr:el-ğışâve mâ ğaşiye'l-kalbe min reyni't-tab', gloss:ğışâve kalbi kaplayan mühür pasıdır, source:"غ ش و,B001"}. Karşı kök gözü temizleyen sürmeyi adlandırır: {ar:الجلا مقصور الإثمد لأنه يجلو البصر, tr:el-celâ maksûru'l-ismid li-ennehû yeclu'l-basar, gloss:celâ sürmedir çünkü gözü açar, source:"ج ل و,B002"}. Aynı kök cilacının kılıcı parlatmasını da adlandırır: {ar:جلا الصيقل السيف واجتلاه, tr:celâ's-saykalu's-seyfe ve'ctelâh, gloss:cilacı kılıcı parlattı, source:"ج ل و,B002"}. Temizlenmiş bakış ise hedefe fırlatılır: {ar:جلى ببصره تجلية إذا رمى به كما ينظر الصقر إلى الصيد, tr:cellâ bi-basarihî tecliyeten izâ remâ bihî kemâ yenzuru's-sakru ile's-sayd, gloss:doğanın avına baktığı gibi bakışını fırlattı, source:"ج ل و,B008"}. Kur'an zarı reddedenlerin gözüne yerleştirir: {ar:وَعَلَىٰٓ أَبْصَٰرِهِمْ غِشَٰوَةٌۭ, tr:ve alâ ebsârihim ğışâvetün, gloss:gözlerinin üstünde bir perde vardır, source:2:7}. Hevesini ilah edinen adamın durumu da şöyle anlatılır: {ar:وَجَعَلَ عَلَىٰ بَصَرِهِۦ غِشَٰوَةًۭ فَمَن يَهْدِيهِ مِنۢ بَعْدِ ٱللَّهِ, tr:ve ceale alâ basarihî ğışâveten fe-men yehdîhi min ba'di'llâh, gloss:gözüne perde çekti; Allah'tan sonra onu kim yola getirir, source:45:23}. Burada perdenin hemen ardından yol gösterme sorusu gelir. Önüne ve arkasına set çekilenler için {ar:فَأَغْشَيْنَٰهُمْ فَهُمْ لَا يُبْصِرُونَ, tr:fe-ağşeynâhüm fehüm lâ yubsirûn, gloss:onları örttük de görmüyorlar, source:36:9} denir. Tersi Diriliş gününde, dünyada gafil kalmış olana söylenir: {ar:فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ, tr:fe-keşefnâ anke ğıtâeke fe-basaruke'l-yevme hadîd, gloss:örtünü kaldırdık; bugün gözün demir gibi keskindir, source:50:22}.

Surenin devamı bu çifti adım adım işler. On ikinci ayet {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hüdâ, gloss:yol göstermek elbette bize düşer, source:92:12} der. Bu kelimenin ailesinde {ar:الهدى البيان, tr:el-hüdâ el-beyân, gloss:hidayet açıklığa kavuşturmaktır, source:"ه د ي,B001"} anlamı vardır. Böylece gündüzün işi olan açığa çıkarmayı Allah kendi üstüne alır. On dördüncü ayetin ateşi bu ailede gözü açan malzemeyi de verir: {ar:النؤور دخان الفتيلة يتخذ كحلا أو وشما, tr:en-neûr duhânu'l-fetîle yuttehazu kuhlen ev veşmâ, gloss:fitilin isi sürme ya da dövme yapılır, source:"ن و ر,B008"}. Uyarı ateşi, kendi kökünde, göze sürülen bir aydınlatmadır. Yirminci ayetteki yüzün ailesinde ise günün açılan ilk cephesi durur: {ar:وجه النهار أوله, tr:vechu'n-nehâri evvelüh, gloss:günün yüzü onun başlangıcıdır, source:"و ج ه,B007"}. Sure gecenin örtüsüyle başlar ve aranan bir yüzle biter. O yüz, kelimenin ailesinde, sabahın ilk açılan yüzünün yanında durur.

Örtünün en geniş biçimi bütün yaratılmışları saran olaydır: {ar:الغاشية القيامة لأنها تغشى الخلق بإفزاعها, tr:el-ğâşiyetü'l-kıyâme li-ennehâ tağşe'l-halka bi-ifzâıhâ, gloss:ğâşiye kıyamettir çünkü yaratılmışları dehşetiyle örter, source:"غ ش و,B002"}. Kur'an aynı adla sorar: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:sarıp kaplayanın haberi sana geldi mi, source:88:1}. Örtü yüzlere de düşer. En güzeli yapanlar için {ar:وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌۭ وَلَا ذِلَّةٌ, tr:ve lâ yerhaku vucûhehüm katerun ve lâ zille, gloss:yüzlerini ne toz ne aşağılanma kaplar, source:10:26} denir. Kötülük kazananlar için ise {ar:كَأَنَّمَآ أُغْشِيَتْ وُجُوهُهُمْ قِطَعًۭا مِّنَ ٱلَّيْلِ مُظْلِمًا, tr:keennemâ uğşiyet vucûhuhüm kıta'an mine'l-leyli muzlimâ, gloss:sanki yüzlerine gecenin karanlık parçaları örtülmüştür, source:10:27} denir. Ateş de aynı fiille yüzleri örter: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehümü'n-nâr, gloss:ateş yüzlerini örter, source:14:50}. Ama örtü kendiliğinden kötü değildir. Uhud'daki kederden sonra Allah müminlere bir güven indirmiştir: {ar:أَمَنَةًۭ نُّعَاسًۭا يَغْشَىٰ طَآئِفَةًۭ مِّنكُمْ, tr:emeneten nuâsen yağşâ tâifeten minküm, gloss:içinizden bir kesimi saran bir güven ve uyuklama, source:3:154}. Gece de böyledir: bir işarettir, dinlendirir. Tehlikeli olan, örtünün altında kalıp gün açıldığında da görmek istememektir.

Kaynaklar: 92:1 ٱلَّيْلِ ل ي ل B001; 92:1 يَغْشَىٰ غ ش و B001; 92:1 يَغْشَىٰ غ ش و B002; 92:2 ٱلنَّهَارِ ن ه ر B001; 92:2 ٱلنَّهَارِ ن ه ر B002; 92:2 ٱلنَّهَارِ ن ه ر B003; 92:2 تَجَلَّىٰ ج ل و B001; 92:2 تَجَلَّىٰ ج ل و B002; 92:2 تَجَلَّىٰ ج ل و B007; 92:2 تَجَلَّىٰ ج ل و B008; 92:12 لَلْهُدَىٰ ه د ي B001; 92:14 نَارًۭا ن و ر B008; 92:20 وَجْهِ و ج ه B007

## Yolu gösteren ateş, kervanın başı ve sonu

Ateş ile ışık aynı yerden adlandırılır: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûru ve'n-nâru sümmiyâ bi-zâlike min tarîkati'l-idâe, gloss:nur ve nar bu adı aydınlatma yönünden almıştır, source:"ن و ر,B001"}. Ateşin yol göstermede eski bir işi vardır: {ar:كانوا ينورون في الجاهلية ليهتدى ويقتدى بها, tr:kânû yünevvirûne fi'l-câhiliyyeti li-yühtedâ ve yuktedâ bihâ, gloss:cahiliyede yol bulunsun ve izlensin diye ateş yakarlardı, source:"ن و ر,B005"}. Bu işin bir de işareti vardır: {ar:المنار: علم الطريق؛ ضرب المنار على طريقه ليهتدى بها, tr:el-menâr alemü't-tarîk; darabe'l-menâra alâ tarîkıhî li-yühtedâ bihâ, gloss:menâr yolun işaretidir; yolu bulunsun diye yolunun üstüne işaret dikti, source:"ن و ر,B005"}. Yolcu bu ateşi uzaktan görür ve ona yönelir: {ar:تنورت النار من بعيد: تبصرتها, tr:tenevvertü'n-nâra min baîd: tebassartühâ, gloss:ateşi uzaktan gözledim, source:"ن و ر,B003"}; {ar:تنورت نارا قصدت إليها, tr:tenevvertü nâran kasadtü ileyhâ, gloss:bir ateşe doğru yöneldim, source:"ن و ر,B003"}. Hidayet de tam bu işi adlandırır: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytühü't-tarîka ve'l-beyte hidâyeten ey arraftüh, gloss:ona yolu ve evi gösterdim yani tanıttım, source:"ه د ي,B001"}. Başka bir tanım {ar:الهداية دلالة بلطف؛ تعريف الطرق, tr:el-hidâyetü delâletün bi-lutf; ta'rîfü't-turuk, gloss:hidayet incelikle yol göstermektir; yolları tanıtmaktır, source:"ه د ي,B001"} der. Sahne şöyle işler: Karanlıkta yüksek bir yere ateş yakılır, yolcu onu uzaktan görür, yönünü ona göre düzeltir ve ateş yolun nerede olduğunu bildirmiş olur. Gündüzün yaygın ışığında yol zaten görünür. Gece ise yolu ancak böyle bir ateş gösterir.

Surede on ikinci ayet {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hüdâ, gloss:yol göstermek elbette bize düşer, source:92:12} der. İki ayet sonra bir ateş yakılır: {ar:فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ, tr:fe-enzertüküm nâran telezzâ, gloss:sizi alev alev yanan bir ateşle uyardım, source:92:14}. Ayetteki anlam, kaçınılacak alevdir. Kelimenin ailesi ise aynı ateşin bir işaret ateşi olarak da duyulmasını sağlar: Uyarı ateşi yolun nerede bittiğini bildirerek yol gösterir. Yirminci ayetin yüzü de bu sahneye girer: {ar:الوجهة كل موضع استقبلته, tr:el-vichetü küllü mevdıın istakbeltehû, gloss:vicheti yöneldiğin her yerdir, source:"و ج ه,B002"}. Aynı dalda yolun ayakla açılması da anlatılır: {ar:وجهوا للناس الطريق إذا وطئوه وسلكوه, tr:vecchehû li'n-nâsi't-tarîka izâ vetıûhü ve selekûh, gloss:yolu çiğneyip yürüyerek insanlara açtılar, source:"و ج ه,B002"}. Rabbinin yüzünü arayan, o yüze dönük yürüyerek yolu belirgin kılar.

Kur'an bu sahneyi Musa ile kurar. Musa ailesiyle yolculuk ederken bir ateş görür ve onlara şöyle der: {ar:إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:innî ânestü nâran leallî âtîküm minhâ bi-kabesin ev ecidü ale'n-nâri hüdâ, gloss:bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösterici bulurum, source:20:10}. Ateş, yol bulma ve getirip vermek aynı cümlede durur. Başka bir anlatımda Musa süreyi doldurmuş, ailesiyle yola çıkmıştır ve ateşi {ar:ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا, tr:ânese min cânibi't-tûri nârâ, gloss:Tur'un yanından bir ateş gördü, source:28:29} diye görür. "Yan" kelimesi on yedinci ayetin köküdür. Üçüncü anlatımda ateşin bir başka işi söylenir: {ar:لَّعَلَّكُمْ تَصْطَلُونَ, tr:leallekum tastalûn, gloss:belki ısınırsınız, source:27:7}. Isınmak fiili on beşinci ayetteki {ar:يَصْلَىٰهَآ, tr:yaslâhâ, gloss:ona girip yanar, source:92:15} fiiliyle aynı köktendir. Musa'nın ateşi yanına yaklaşılan, ısıtan ve yol gösteren ateştir. Surenin ateşi ise içine girilen ateştir. Aynı kök iki mesafeyi ayırır. Gece yolculuğunda Kur'an başka işaretler de koyar: {ar:لِتَهْتَدُوا۟ بِهَا فِى ظُلُمَٰتِ ٱلْبَرِّ وَٱلْبَحْرِ, tr:li-tehtedû bihâ fî zulümâti'l-berri ve'l-bahr, gloss:karanın ve denizin karanlıklarında onlarla yol bulasınız diye, source:6:97}; {ar:وَعَلَٰمَٰتٍۢ ۚ وَبِٱلنَّجْمِ هُمْ يَهْتَدُونَ, tr:ve alâmâtin ve bi'n-necmi hüm yehtedûn, gloss:işaretler de koydu; onlar yıldızla yol bulurlar, source:16:16}.

Hidayetin ailesi yolu gösteren ateşin yanına bir yürüyüş düzeni de koyar. Öndeki şey hâdîdir: {ar:الهادي من كل شيء أوله, tr:el-hâdî min külli şey'in evveluh, gloss:her şeyin hâdîsi onun önüdür, source:"ه د ي,B003"}. Aynı tanım {ar:هوادي الخيل أعناقها أو أول رعيل, tr:hevâdi'l-hayli a'nâkuhâ ev evvelü raîl, gloss:atların hâdîleri boyunları ya da ilk bölüktür, source:"ه د ي,B003"} ve {ar:الدليل يسمى هاديا لتقدمه, tr:ed-delîlü yüsemmâ hâdiyen li-tekaddumih, gloss:kılavuza önde yürüdüğü için hâdî denir, source:"ه د ي,B003"} diye sürer. Sürünün önündeki deve için {ar:ناقة أولة وجمل أول إذا تقدما الإبل, tr:nâkatün evvelatün ve cemelün evvelü izâ tekaddeme'l-ibil, gloss:develerin önüne geçen dişi ve erkek deveye evvel denir, source:"ء و ل,B001"} denir. Arkada kalanlar için {ar:أخرى القوم أي من كان في آخرهم, tr:uhra'l-kavmi ey men kâne fî âhirihim, gloss:topluluğun sonu, en arkada olanlardır, source:"ء خ ر,B001"} denir. Semerin de bir ön ve bir arka direği vardır: {ar:آخرة الرحل وقادمته ومؤخر الرحل ومقدمه, tr:âhiratü'r-rahli ve kâdimetühû ve muahhiru'r-rahli ve mukaddimuh, gloss:semerin arka ve ön kaşı, source:"ء خ ر,B003"}. Gece ve gündüz yürüyüşün iki ayrı düzenidir: {ar:لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل, tr:lestü bi-leyliyyin ve lâkinnî neharun ey esîru bi'n-nehâri ve lâ utîku sura'l-leyl, gloss:gececi değilim, gündüzcüyüm; gündüz yürürüm, gece yürüyüşüne dayanamam, source:"ل ي ل,B002"}; {ar:رجل نهر صاحب نهار, tr:racülün neharun sâhibu nehâr, gloss:gündüz adamı, source:"ن ه ر,B002"}. On ikinci ve on üçüncü ayet bu düzende birlikte işitilir: {ar:وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ, tr:ve inne lenâ le'l-âhirete ve'l-ûlâ, gloss:sonuncu da ilki de elbette bizimdir, source:92:13}. Kervanın önündeki kılavuzu Allah üstlenir, baştaki deveden en arkadaki yolcuya kadar bütün dizi de O'nundur. Kur'an böyle bir gece yürüyüşünü Lut'a gönderilen elçilerin ağzından anlatır: {ar:فَأَسْرِ بِأَهْلِكَ بِقِطْعٍۢ مِّنَ ٱلَّيْلِ وَٱتَّبِعْ أَدْبَٰرَهُمْ وَلَا يَلْتَفِتْ مِنكُمْ أَحَدٌۭ, tr:fe-esri bi-ehlike bi-kıt'ın mine'l-leyli ve't-tebi' edbârahüm ve lâ yeltefit minküm ehad, gloss:gecenin bir bölümünde ailenle yola çık; onların arkasından yürü; hiçbiriniz arkasına dönüp bakmasın, source:15:65}. Lut dizinin en arkasında yürür ve kimse dönüp bakmaz. Surenin yalanlayanı ise bir sonraki bölümde görüleceği gibi, tam da arkasına bakan hayvanın fiilini taşır.

Kaynaklar: 92:1 ٱلَّيْلِ ل ي ل B002; 92:2 ٱلنَّهَارِ ن ه ر B002; 92:12 لَلْهُدَىٰ ه د ي B001; 92:12 لَلْهُدَىٰ ه د ي B003; 92:13 لَلْءَاخِرَةَ ء خ ر B001; 92:13 لَلْءَاخِرَةَ ء خ ر B003; 92:13 وَٱلْأُولَىٰ ء و ل B001; 92:14 نَارًۭا ن و ر B001; 92:14 نَارًۭا ن و ر B003; 92:14 نَارًۭا ن و ر B005; 92:20 وَجْهِ و ج ه B002

## Uyarılan ateş ve araya konan siper

On dördüncü ayet bir alarmla başlar: {ar:فَأَنذَرْتُكُمْ, tr:fe-enzertüküm, gloss:sizi uyardım, source:92:14}. Kökün anlamı {ar:الإنذار الإبلاغ ولا يكاد يكون إلا في التخويف, tr:el-inzâru'l-iblâğu ve lâ yekâdü yekûnü illâ fi't-tahvîf, gloss:inzâr haber ulaştırmaktır ve neredeyse hep korkutmak için olur, source:"ن ذ ر,B001"} diye verilir. Örnek sahnesi bir düşman baskınıdır: {ar:أنذرت القوم مسير عدوهم إليهم فنذروا أي علموا فتحرزوا, tr:enzertü'l-kavme mesîra adüvvihim ileyhim fe-nezirû ey alimû fe-teharrazû, gloss:kavmi düşmanın üzerlerine yürüdüğüne karşı uyardım; öğrendiler ve tedbir aldılar, source:"ن ذ ر,B001"}. Uyarının en çıplak biçimi {ar:أنا النذير العريان, tr:ene'n-nezîru'l-uryân, gloss:ben çıplak uyarıcıyım, source:"ن ذ ر,B001"} sözüdür: Elbisesini sıyırıp sallayan adam, görenlerin uzaktan anlayacağı bir işaret verir. Uyarının işi bitmiş sayılmaz, uyarılanlar tedbir aldığında tamamlanır. Ayet uyarılan şeyi de adlandırır: {ar:نَارًۭا تَلَظَّىٰ, tr:nâran telezzâ, gloss:alev alev yanan bir ateş, source:92:14}. Ateşin adı titreyen ışıktır: {ar:ولأن ذلك يكون مضطربا سريع الحركة, tr:ve li-enne zâlike yekûnü muzdariben serîa'l-hareke, gloss:çünkü o çırpınan ve hızlı hareket eden bir şeydir, source:"ن و ر,B002"}. Fiil ise saf alevdir: {ar:اللظى اللهب الخالص, tr:el-lezâ'l-lehebü'l-hâlis, gloss:lezâ katışıksız alevdir, source:"ل ظ ي,B001"}. Bu ayetin kendisi de {ar:نارا تلظى أي تتوهج وتتوقد, tr:nâran telezzâ ey tetevehhecu ve tetevakkadu, gloss:alev alev yanan ateş yani parlayıp tutuşan ateş, source:"ل ظ ي,B001"} diye açıklanır. Aynı kelime cehennemin özel adıdır: {ar:لظى غير مصروفة اسم لجهنم, tr:lezâ ğayru masrûfetin ismün li-cehennem, gloss:Lezâ cehennemin adıdır, source:"ل ظ ي,B002"}. Ayrıca öfkeyle yanmayı da anlatır: {ar:فلان يتلظى على فلان تلظيا إذا توقد عليه من شدة الغضب, tr:fülânün yetelezzâ alâ fülânin telezziyen izâ tevakkade aleyhi min şiddeti'l-ğadab, gloss:biri öfkenin şiddetinden ötekine karşı tutuşursa ona yetelezzâ denir, source:"ل ظ ي,B003"}. Ateş yalnızca sıcak değil, kızgındır.

On beşinci ayet içeri girişi anlatır: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girip yanmaz, source:92:15}. Fiil {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:saliye'l-kâfiru nâran fehüve yaslâhâ ey kâsâ harrahâ ve şiddetehâ, gloss:inkârcı ateşe girdi yani onun sıcağına ve şiddetine katlandı, source:"ص ل ي,B003"} diye açıklanır. Ateşe girmek ve orada kalmak da anlatılır: {ar:صلي الرجل نارا إذا أدخلته النار, tr:suliye'r-racülü nâran izâ edhaltehü'n-nâr, gloss:adam ateşe sokuldu, source:"ص ل ي,B003"}; {ar:من يصلى في النار أي يلزم النار, tr:men yuslâ fi'n-nâri ey yelzemü'n-nâr, gloss:ateşe atılan, ateşten ayrılmayan, source:"ص ل ي,B003"}. Aynı kökün bir zanaat anlamı da vardır: {ar:صلى عصاه إذا أدارها على النار يثقفها, tr:salâ asâhü izâ edârahâ ale'n-nâri yüsakkıfuhâ, gloss:değneğini düzeltmek için ateşin üstünde çevirdi, source:"ص ل ي,B004"}. Et kızartmak da bu köktendir: {ar:صليت اللحم صليا شويته, tr:saleytü'l-lahme salyen şeveytüh, gloss:eti kızarttım, source:"ص ل ي,B004"}. Onuncu ayette yolun adı {ar:العسر الخلاف والالتواء, tr:el-usru'l-hılâfu ve'l-iltivâ', gloss:ters gitmek ve kıvrılmak, source:"ع س ر,B004"} idi. Ateşin yanındaki zanaatkâr ise eğri değneği ateşin üstünde çevirerek doğrultur. Kıvrık yolu seçen, eğrinin doğrultulduğu ateşe varır. Bu, iki kök arasında kurulan bir bağdır, aynı kökten gelen bir kimlik değildir. Yanan kişinin adı da sahneye girer: {ar:الشقوة خلاف السعادة, tr:eş-şıkvetü hılâfü's-saâde, gloss:bedbahtlık mutluluğun karşıtıdır, source:"ش ق و,B001"}. Kelimenin bir dalı onu doğrudan onuncu ayete bağlar: {ar:الشقاء: الشدة والعسر, tr:eş-şekâ': eş-şiddetü ve'l-usr, gloss:şekâ sıkıntı ve zorluktur, source:"ش ق و,B002"}. En bedbaht kişi, en zora kolaylaştırılan kişidir.

Karşı tarafta bir siper vardır. Beşinci ve on yedinci ayetlerin kökü {ar:دفع شيء عن شيء بغيره, tr:def'u şey'in an şey'in bi-ğayrih, gloss:bir şeyi bir şeyden başka bir şeyle savmak, source:"و ق ي,B001"} demektir. Sakınma bir ara katman kurmaktır: {ar:اتق الله توقه أي اجعل بينك وبينه كالوقاية, tr:itteki'llâhe tevakkahû ey ic'al beyneke ve beynehû ke'l-vikâye, gloss:Allah'tan sakın yani seninle O'nun arasına bir siper koy, source:"و ق ي,B002"}. Takva da {ar:التقوى جعل النفس في وقاية مما يخاف, tr:et-takvâ ca'lü'n-nefsi fî vikâyetin mimmâ yuhâf, gloss:takva insanın kendini korkulan şeye karşı bir siperin içine koymasıdır, source:"و ق ي,B002"} diye tanımlanır. On yedinci ayetin fiili ise başkasının yaptığı bir savmadır: {ar:جنبته عن كذا فاجتنب أي تجنبه وجنبته أي دفعت عنه مكروها, tr:cenebtühû an kezâ fe'ctenebe ey tecennebehû ve cenebtühû ey defa'tü anhü mekrûhâ, gloss:onu şundan uzaklaştırdım o da kaçındı; ondan kötülüğü savdım, source:"ج ن ب,B003"}. Savma fiili iki kökte de geçer: sakınan kişi kendi tarafında bir siper kurar ve Allah onun üzerinden kötülüğü savar. İnsanın yanında da bir kalkan durur, {ar:سمي الترس مجنبا لأنه إلى جنب الإنسان, tr:sümmiye't-tursu micnenben li-ennehû ilâ cenbi'l-insân, gloss:kalkana mıcneb denir çünkü insanın yanında durur, source:"ج ن ب,B011"}. Sahnenin sırası şöyledir. Beşinci ayette siper önceden kurulur. On dördüncü ayette alarm verilir. On beşinci ayette alarmı duymayan ateşe girer. On altıncı ayet onun alarmı nasıl karşıladığını söyler: yalanladı ve yüz çevirdi. Uyarı sahnesindeki "öğrendiler ve tedbir aldılar" adımını hiç atmadı. On yedinci ayette tedbir alan kenara çekilir. On ikinci ve on üçüncü ayetlerde "biz" diye konuşan ses, on dördüncü ayette "ben" der: alarmı veren tek bir sestir.

Kur'an bu sahnenin her parçasını başka yerlerde de kurar. Bir önceki surenin sonunda Semud kavmi peygamberini yalanlamıştır: {ar:إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا, tr:izi'nbease eşkâhâ, gloss:içlerinden en bedbahtı kalkıp gittiğinde, source:91:12}. Ardından {ar:فَكَذَّبُوهُ فَعَقَرُوهَا, tr:fe-kezzebûhu fe-akarûhâ, gloss:onu yalanladılar ve deveyi kestiler, source:91:14} gelir. En bedbahtın adı ve yalanlamanın fiili yan yanadır. Bir başka surede aynı kelimeler rolleri değişerek gelir: {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:seyezzekkeru men yahşâ, gloss:korkan öğüt alacak, source:87:10}, {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebühe'l-eşkâ, gloss:en bedbaht ondan kaçınacak, source:87:11}, {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâra'l-kübrâ, gloss:o ki en büyük ateşe girecek, source:87:12}. Orada en bedbaht öğütten kaçınır. Bu surede ise en sakınan kişi ateşten uzak tutulur. Kaçınma fiili iki surede iki ayrı şeye yönelir. Lezâ'nın kimi çağırdığı da söylenir: {ar:كَلَّآ ۖ إِنَّهَا لَظَىٰ, tr:kellâ innehâ lezâ, gloss:hayır; o Lezâ'dır, source:70:15}, {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:ted'û men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}, {ar:وَجَمَعَ فَأَوْعَىٰٓ, tr:ve cemea fe-ev'â, gloss:ve toplayıp yığanı, source:70:18}. Ateşin öfkesi de anlatılır: {ar:تَكَادُ تَمَيَّزُ مِنَ ٱلْغَيْظِ ۖ كُلَّمَآ أُلْقِىَ فِيهَا فَوْجٌۭ سَأَلَهُمْ خَزَنَتُهَآ أَلَمْ يَأْتِكُمْ نَذِيرٌۭ, tr:tekâdü temeyyezü mine'l-ğayz küllemâ ulkıye fîhâ fevcün seelehüm hazenetühâ elem ye'tiküm nezîr, gloss:öfkeden neredeyse çatlayacaktır; içine her bölük atıldığında bekçileri onlara size bir uyarıcı gelmedi mi diye sorar, source:67:8}. Cevap şudur: {ar:قَالُوا۟ بَلَىٰ قَدْ جَآءَنَا نَذِيرٌۭ فَكَذَّبْنَا, tr:kâlû belâ kad câenâ nezîrun fe-kezzebnâ, gloss:evet bize bir uyarıcı geldi ama yalanladık dediler, source:67:9}. Uyarı, yalanlama ve ateş tek konuşmada durur. Siper de defalarca buyrulur: {ar:فَٱتَّقُوا۟ ٱلنَّارَ ٱلَّتِى وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:fe'ttekû'n-nâra'lletî vekûduhe'n-nâsu ve'l-hicâra, gloss:yakıtı insanlar ve taşlar olan ateşten sakının, source:2:24}; {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا, tr:kû enfüseküm ve ehlîküm nârâ, gloss:kendinizi ve ailenizi bir ateşten koruyun, source:66:6}. Kenara çekilme ise bir kurtarmadır: {ar:ثُمَّ نُنَجِّى ٱلَّذِينَ ٱتَّقَوا۟, tr:sümme nünecci'llezîne't-tekav, gloss:sonra sakınanları kurtarırız, source:19:72}; {ar:فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ, tr:fe-men zuhziha ani'n-nâri ve udhıle'l-cennete fe-kad fâz, gloss:kim ateşten uzaklaştırılır ve cennete sokulursa kurtulmuştur, source:3:185}. Allah'ın yüzü için yedirenler de korunur: {ar:فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ, tr:fe-vekâhumu'llâhu şerra zâlike'l-yevm, gloss:Allah onları o günün kötülüğünden korudu, source:76:11}. Uyarıcının kendisi de konuşur. Peygambere şunu demesi buyrulur: {ar:إِنْ هُوَ إِلَّا نَذِيرٌۭ لَّكُم بَيْنَ يَدَىْ عَذَابٍۢ شَدِيدٍۢ, tr:in hüve illâ nezîrun leküm beyne yedey azâbin şedîd, gloss:o şiddetli bir azabın önünde sizin için bir uyarıcıdır yalnızca, source:34:46}. Surenin birinci tekil uyarısı da şöyle yankılanır: {ar:إِنَّآ أَنذَرْنَٰكُمْ عَذَابًۭا قَرِيبًۭا يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ, tr:innâ enzernâküm azâben karîben yevme yenzuru'l-mer'ü mâ kaddemet yedâh, gloss:sizi yakın bir azaba karşı uyardık; o gün kişi ellerinin önden gönderdiğine bakar, source:78:40}.

Kaynaklar: 92:5 وَٱتَّقَىٰ و ق ي B001; 92:5 وَٱتَّقَىٰ و ق ي B002; 92:10 لِلْعُسْرَىٰ ع س ر B004; 92:14 فَأَنذَرْتُكُمْ ن ذ ر B001; 92:14 نَارًۭا ن و ر B002; 92:14 تَلَظَّىٰ ل ظ ي B001; 92:14 تَلَظَّىٰ ل ظ ي B002; 92:14 تَلَظَّىٰ ل ظ ي B003; 92:15 يَصْلَىٰهَآ ص ل ي B003; 92:15 يَصْلَىٰهَآ ص ل ي B004; 92:15 ٱلْأَشْقَى ش ق و B001; 92:15 ٱلْأَشْقَى ش ق و B002; 92:17 ٱلْأَتْقَى و ق ي B001; 92:17 ٱلْأَتْقَى و ق ي B002; 92:17 وَسَيُجَنَّبُهَا ج ن ب B003; 92:17 وَسَيُجَنَّبُهَا ج ن ب B011

## Buluşmalar

Görüntülerin en sık birleştiği yer, uçurum ile elin aynı sahnede durmasıdır. Cennet ehlinden biri dünyadaki arkadaşını anlatır. Arkadaşı ona alay ederek şöyle sormuştur: {ar:يَقُولُ أَءِنَّكَ لَمِنَ ٱلْمُصَدِّقِينَ, tr:yekûlü einneke le-mine'l-musaddikîn, gloss:sen de mi doğrulayanlardansın derdi, source:37:52}. Sonra adam aşağı bakar ve arkadaşını ateşin ortasında görür: {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettalea fe-raâhu fî sevâi'l-cahîm, gloss:eğilip baktı ve onu cehennemin ortasında gördü, source:37:55}. Ona şöyle der: {ar:تَٱللَّهِ إِن كِدتَّ لَتُرْدِينِ, tr:ta'llâhi in kidte le-türdîn, gloss:Allah'a andolsun beni de neredeyse yuvarlayacaktın, source:37:56}. Ardından ekler: {ar:وَلَوْلَا نِعْمَةُ رَبِّى لَكُنتُ مِنَ ٱلْمُحْضَرِينَ, tr:ve levlâ ni'metü rabbî le-küntü mine'l-muhdarîn, gloss:Rabbimin nimeti olmasaydı ben de oraya getirilenlerden olurdum, source:37:57}. Bu sahnede doğrulama, yuvarlanma, yüksekten bakış ve bir nimet bir aradadır. Surenin on dokuzuncu ayeti verenin yanında kimsenin bir nimeti olmadığını söyler. Cennet ehli ise kurtuluşunu tek bir nimete, Rabbinin nimetine bağlar. İnsanlar arasında karşılığı ödenecek bir el yoktur, ama Rabbin eli her şeyi taşır. Bir başka ayet aynı birleşmeyi müminlere hatırlatma olarak kurar: Allah'ın nimetiyle kardeş olmuşlardır ve {ar:وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍۢ مِّنَ ٱلنَّارِ فَأَنقَذَكُم مِّنْهَا, tr:ve küntüm alâ şefâ hufratin mine'n-nâri fe-enkazeküm minhâ, gloss:ateşten bir çukurun kenarındaydınız; sizi oradan kurtardı, source:3:103}. Ayet {ar:لَعَلَّكُمْ تَهْتَدُونَ, tr:leallekum tehtedûn, gloss:doğru yolu bulasınız diye, source:3:103} diye kapanır. Kuyunun kenarı, nimet ve yol gösterme tek ayettedir. Kenara çekilen, uyarı ateşini işaret ateşi olarak okuyandır.

İkinci büyük buluşma bir sarayda geçer. Musa ile Harun'a Firavun'a ne diyecekleri öğretilir: {ar:وَٱلسَّلَٰمُ عَلَىٰ مَنِ ٱتَّبَعَ ٱلْهُدَىٰٓ, tr:ve's-selâmü alâ meni't-tebea'l-hüdâ, gloss:esenlik yol göstericiye uyanadır, source:20:47}. Ardından {ar:أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ, tr:enne'l-azâbe alâ men kezzebe ve tevellâ, gloss:azap yalanlayıp yüz çevirenedir, source:20:48} gelir. Firavun {ar:قَالَ فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:kâle fe-men rabbükümâ yâ mûsâ, gloss:ey Musa, sizin Rabbiniz kim dedi, source:20:49} diye sorar. Musa şöyle cevap verir: {ar:قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:kâle rabbüne'llezî a'tâ külle şey'in halkahû sümme hedâ, gloss:Rabbimiz her şeye yaratılışını verip sonra yol gösterendir dedi, source:20:50}. Bu cevapta surenin üç fiili aynı cümlededir: üçüncü ayetin yaratması, beşinci ayetin vermesi ve on ikinci ayetin yol göstermesi. Bir ayet önce de on altıncı ayetin iki fiili geçmiştir. Aynı Firavun başka bir surede yüceliği kendine mal eder: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe-kâle ene rabbükümü'l-a'lâ, gloss:ben sizin en yüce rabbinizim dedi, source:79:24}. Ardından {ar:فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ, tr:fe-ehazehu'llâhu nekâle'l-âhirati ve'l-ûlâ, gloss:Allah onu sonranın ve öncenin cezasıyla yakaladı, source:79:25} gelir. Elin, yolun, yüz çevirmenin, yüceliğin ve mülkün görüntüleri burada tek bir karşılaşmada birleşir. Veren Rab ile tutan kral karşı karşıya gelir. Yüceliği iddia eden kral, surenin "son da ilk de bizimdir" sözüyle düşürülür.

Yüz ile elin buluşması iyiliğin tanımında görülür. İyilik yüzü doğuya ya da batıya çevirmek değildir: {ar:لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ, tr:leyse'l-birra en tüvellû vucûheküm kıbele'l-meşriki ve'l-mağrib, gloss:iyilik yüzlerinizi doğu ve batı yönüne çevirmeniz değildir, source:2:177}. Aynı ayet iyiliği şöyle sayar: {ar:وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ, tr:ve âte'l-mâle alâ hubbih, gloss:malı sevmesine rağmen verdi, source:2:177}. Malın gittiği yerler arasında {ar:وَفِى ٱلرِّقَابِ, tr:ve fi'r-rikâb, gloss:boyunları çözmek için, source:2:177} de vardır. Ayet şöyle biter: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ, tr:ülâike'llezîne sadakû ve ülâike hümü'l-müttekûn, gloss:işte doğru olanlar onlardır ve sakınanlar da onlardır, source:2:177}. Yüzü çevirmek, malı vermek, boyun çözmek, hücumu sonuna kadar götüren doğruluk ve siper olan sakınma tek ayette bir araya gelir. Yüz çevirmek iyiliğin kendisi değildir, iyilik eldedir. Ama surenin yirminci ayeti eli tekrar yüze bağlar: veren el, aranan yüz için uzanır. Aynı bağ yoksulları doyuranların sözünde görülür: {ar:إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءًۭ وَلَا شُكُورًا, tr:innemâ nut'imüküm li-vechi'llâhi lâ nürîdü minküm cezâen ve lâ şükûrâ, gloss:sizi yalnızca Allah'ın yüzü için doyuruyoruz; sizden ne karşılık ne teşekkür istiyoruz, source:76:9}. Sözün sonunda {ar:إِنَّا نَخَافُ مِن رَّبِّنَا يَوْمًا عَبُوسًۭا قَمْطَرِيرًۭا, tr:innâ nehâfü min rabbinâ yevmen abûsen kamtarîrâ, gloss:biz Rabbimizden asık suratlı, çetin bir günden korkarız, source:76:10} derler. Sonra {ar:فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ, tr:fe-vekâhumu'llâhu şerra zâlike'l-yevm, gloss:Allah onları o günün kötülüğünden korudu, source:76:11} gelir. El, yüz, karşılığın reddi ve siper bu ayetlerde surenin sırasıyla dizilir. Bunun tam tersi de bir sahne olarak anlatılır. Bir adam Allah'a söz vermiştir: {ar:لَئِنْ ءَاتَىٰنَا مِن فَضْلِهِۦ لَنَصَّدَّقَنَّ, tr:lein âtânâ min fadlihî le-nessaddakanne, gloss:bize lütfundan verirse mutlaka sadaka vereceğiz, source:9:75}. Sonra şu olur: {ar:فَلَمَّآ ءَاتَىٰهُم مِّن فَضْلِهِۦ بَخِلُوا۟ بِهِۦ وَتَوَلَّوا۟ وَّهُم مُّعْرِضُونَ, tr:fe-lemmâ âtâhüm min fadlihî bahılû bihî ve tevellev ve hüm mu'ridûn, gloss:lütfundan verince cimrilik ettiler ve yüz çevirdiler; zaten dönüp gidiyorlardı, source:9:76}. Sıkan el ile dönülen sırt aynı kişidedir. Sekizinci ve on altıncı ayetler tek bir hikâyede birleşir.

Büyüme ile yükseklik, yüksekteki bahçede buluşur. Allah'ın hoşnutluğunu arayarak harcayanların durumu {ar:كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ, tr:ke-meseli cennetin bi-rabvetin esâbehâ vâbilün fe-âtet ükulehâ dı'feyn, gloss:yüksekçe bir yerdeki bahçe gibidir; ona sağanak isabet eder ve ürününü iki kat verir, source:2:265} diye anlatılır. Bu bahçe kuyunun tam karşıtıdır. Aşağıda değil yüksektedir. Yağmur onu süpürmez, büyütür. Verme fiili de bahçenin kendi fiilidir. Aynı yükseklik ateşe dönük bir eğiklikle karşılaşır: Bir yanda takva ve hoşnutluk üzerine kurulmuş yapı, öbür yanda {ar:عَلَىٰ شَفَا جُرُفٍ هَارٍۢ فَٱنْهَارَ بِهِۦ فِى نَارِ جَهَنَّمَ, tr:alâ şefâ cürufin hârin fenhâra bihî fî nâri cehennem, gloss:çökmek üzere olan bir yarın kenarına kurulmuş, onunla birlikte cehennem ateşine yıkılmış yapı, source:9:109} vardır. Biri takva ve hoşnutluk üzerine kurulur, öteki çöküp ateşe düşer. Cimrinin malı da düştüğü yerde onun yanına yapışır: {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhühüm ve cünûbühüm ve zuhûruhüm, gloss:o gün onlar cehennem ateşinde kızdırılır ve alınları, yanları ve sırtları onlarla dağlanır, source:9:35}. Sakınanın yanında bir kalkan durur ve o yanından kötülükten uzak tutulur. Biriktirenin yanı ise biriktirdiğiyle dağlanır. Sırtı da yüz çevirdiği için dönmüş olan sırttır.

Musa'nın ateşi ise işaret ateşi ile yakan ateşi bir arada tutar. Musa ailesine {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidü ale'n-nâri hüdâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10} der. Başka bir anlatımda {ar:لَّعَلَّكُمْ تَصْطَلُونَ, tr:leallekum tastalûn, gloss:belki ısınırsınız, source:27:7} der. Isınmak on beşinci ayetin yanmasıyla aynı köktendir. Yanına yaklaşılan ateş ısıtır ve yol gösterir. İçine girilen ateş ise yakar. Surenin hareketi bu iki mesafe arasında kurulur. İlk iki ayette gece serilir ve gün yarılır. Gece insanların koşusunu örter, gün o koşunun dağıldığını gösterir. Yol ayrılır ve her yol yürüyenine göre düzlenir. Biri verir, siper kurar ve vaadi kendi eliyle doğrular. Öteki malını tutar, ona cübbe gibi bürünür ve vaadi yalanlayıp sırtını döner. Sonra gece yolunda bir ateş yakılır ve bir ses "uyardım" der. Uyarıyı işaret olarak okuyan, dizgini tutulan bir binek gibi kenara çekilir. Yüzü kendisine bir nimet borcu olanlara değil, yüceliğe dönüktür. Uyarıyı duymayan, yuvarlandığı anda elindeki malın ona yetmediğini görür ve ateşin içine girer. Surenin son kelimesi, kayıp devesini arayan adamın onu bulduğu anın kelimesidir: hoşnutluk. Bu hoşnutluk, ilk ayetteki gecenin örtüsünden sonra gelen yüzün açılmasıdır.

