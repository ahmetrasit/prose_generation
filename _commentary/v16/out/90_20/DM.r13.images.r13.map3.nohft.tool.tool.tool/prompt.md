Focus: 90:20. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/90_20/D.r13/context.md =====
# 90:20 — focus

عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ

Anchor translation (canonical reading, reference only):

Üzerlerine kapatılmış bir ateş vardır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | عَلَيْهِمْ | عَلَىٰ |  | P;PRON |
| 2 | نَارٌ | نَار | ن و ر | N |
| 3 | مُّؤْصَدَةٌۢ | مُّؤْصَدَة | و ص د | ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 90 — full text (context; no pericope)

- 90:1 لَآ أُقْسِمُ بِهَٰذَا ٱلْبَلَدِ
- 90:2 وَأَنتَ حِلٌّۢ بِهَٰذَا ٱلْبَلَدِ
- 90:3 وَوَالِدٍۢ وَمَا وَلَدَ
- 90:4 لَقَدْ خَلَقْنَا ٱلْإِنسَٰنَ فِى كَبَدٍ
- 90:5 أَيَحْسَبُ أَن لَّن يَقْدِرَ عَلَيْهِ أَحَدٌۭ
- 90:6 يَقُولُ أَهْلَكْتُ مَالًۭا لُّبَدًا
- 90:7 أَيَحْسَبُ أَن لَّمْ يَرَهُۥٓ أَحَدٌ
- 90:8 أَلَمْ نَجْعَل لَّهُۥ عَيْنَيْنِ
- 90:9 وَلِسَانًۭا وَشَفَتَيْنِ
- 90:10 وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ
- 90:11 فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ
- 90:12 وَمَآ أَدْرَىٰكَ مَا ٱلْعَقَبَةُ
- 90:13 فَكُّ رَقَبَةٍ
- 90:14 أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ
- 90:15 يَتِيمًۭا ذَا مَقْرَبَةٍ
- 90:16 أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ
- 90:17 ثُمَّ كَانَ مِنَ ٱلَّذِينَ ءَامَنُوا۟ وَتَوَاصَوْا۟ بِٱلصَّبْرِ وَتَوَاصَوْا۟ بِٱلْمَرْحَمَةِ
- 90:18 أُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلْمَيْمَنَةِ
- 90:19 وَٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا هُمْ أَصْحَٰبُ ٱلْمَشْـَٔمَةِ
- 90:20 ◀ focus عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ


===== _commentary/v16/work/90_20/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن و ر (root_001564) — identity root of نَارٌ (w2)

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

## و ص د (root_001653) — identity root of مُّؤْصَدَةٌۢ (w3)

- **B001** bitiştirerek sıkıca kapatma — kapıyı örtüp sıkıca kapatmak · kapıyı örtüp sıkıca kapatmak · örtülmüş ve kapalı · örtülmüş ve sıkıca kapatılmış
  أصل يدل على ضم شيء إلى شيء (maqayis)؛ أوصدت الباب أغلقته والموصد المطبق (maqayis)؛ أوصدت الباب وآصدته إذا أغلقته فهو موصد ومطبقة (sihah)؛ أوصدت الباب وآصدته أي أطبقته وأحكمته ومؤصدة مطبقة (mufradat)
- **B002** eve bağlı avlu veya kapı — evin avlusu veya kapısı
  الوصيد الفناء لاتصاله بالربع (maqayis)؛ الوصيد فناء البيت والوصيد الباب (ayn)؛ الوصيد الفناء (sihah)
- **B003** dağdaki taş hayvan barınağı — dağda hayvanlar için yapılan taş oda veya çevirmelik · dağda böyle bir taş barınak kurmak
  الوصيدة كالحظيرة تتخذ للمال إلا أنها من الحجارة والحظيرة من الغصنة واستوصدت في الجبل (sihah)؛ الوصيدة حجرة تجعل للمال في الجبل (mufradat)
- **B004** kökleri birbirine yakın bitki — kökleri birbirine yakın bitki
  الوصيد النبت المتقارب الأصول (maqayis)؛ الوصيد النبات المتقارب الاصول (sihah)؛ الوصيد المتقارب الأصول (mufradat)

## ECHO ء ص د (root_000036) — for مُّؤْصَدَةٌۢ (w3): withheld observed target; not identity

- **B001** kuşatıp kapatma — kapatıp örten şey · kuşatıp kapatma · üzerlerine kapattı · kapıyı kapattı · üzerlerine kapatılmış ateş · kapatıp örten şey için kullanılan ad
  شيء يشتمل على الشيء (maqayis); الإِصد والإِصاد والوصاد بمنزلة المطبق (ayn); أصدت عليهم وأوصدته (ayn); نار مُؤصدة أي مطبقة (ayn); آصدت الباب إذا أغلقته (sihah)
- **B002** çevrili barınak — içindekileri çevreleyen barınak veya ağıl
  الحظيرة أُصيدة سميت بذلك لاشتمالها على ما فيها (maqayis); الأُصيدة كالحظيرة لغة في الوصيدة (sihah)
- **B003** kız çocuklarının giydiği küçük veya içe giyilen gömlek — kız çocuklarının giydiği küçük veya içe giyilen gömlek · küçük iç gömleği olan kız · ona küçük iç gömleğini giydirdi
  الأُصدة قميص صغير يلبسه الصبايا (maqayis); صبية ذات مُؤصد (maqayis); الأُصدة قميص يلبس تحت الثوب وتلبسه صغار الجواري (sihah); أصدته تأصيدا (sihah)
- **B004** avlu — avlu
  الأَصيد لغة في الوصيد وهو الفناء (sihah)
- **B005** dağlar arasındaki çukur alan — belirli bir yer adı · dağlar arasındaki çukur alan
  ذات الأَصاد موضع (sihah); الأَصاد ردهة بين أجبل (sihah)

===== _commentary/v16/out/s090/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 90:20, and ## Buluşmalar) =====
## Boyun, düğüm ve kapak

On üçüncü ayet iki kelimedir: {ar:فَكُّ رَقَبَةٍ, tr:fekku rakabe, gloss:bir boynu çözmek, source:90:13}. Arapça bu ikiliyi hazır bir söz olarak bilir: {ar:فك الرهن وافتكه وفك الرقبة أي أعتقها, tr:fekke'r-rahne ve'fteke'h ve fekke'r-rakabe ey a'tekahâ, gloss:rehni çözdü ve boynu çözdü yani azat etti, source:"ف ك ك,B002"}. Daha ayrıntılı bir söyleyiş de vardır: {ar:فك الرقبة تخليصها من إسار الرق وفك الرهن وفكاكه تخليصه من غلق الرهن, tr:fekku'r-rakabeti tahlîsuhâ min isâri'r-rıkk ve fekku'r-rahni tahlîsuhû min ğalaki'r-rahn, gloss:boynu çözmek onu köleliğin bağından kurtarmak; rehni çözmek de onu rehnin kilidinden kurtarmaktır, source:"ف ك ك,B002"}. Kökün temeli açılmaktır: {ar:أصل صحيح يدل على تفتح وانفراج, tr:aslun sahîhun yedullu alâ tefettuhin ve'nfirâc, gloss:açılmayı ve aralanmayı bildiren sağlam bir kök, source:"ف ك ك,B001"}. Rehin için de {ar:فكاك الرهن وهو فتحه من الانغلاق, tr:fikâku'r-rahni ve huve fethuhû mine'l-inğılâk, gloss:rehnin fikâkı onu kapalılıktan açmaktır, source:"ف ك ك,B002"} denir. Kök bir av sahnesini de bilir: {ar:أفك الظبي من الحبالة إذا وقع فيه ثم انفلت, tr:efekke'z-zabyu mine'l-hıbâle izâ vaka'a fîh summe'nfelet, gloss:ceylan tuzağa düşüp sonra kurtulduğunda efekke denir, source:"ف ك ك,B002"}. Boyun kelimesi de iki ucu tek bir söyleyişte taşır: {ar:الرقبة معروفة وأعتق رقبة وفككت رقبة ورقبت الرجل والدابة إذا طرحت في رقبته حبلا, tr:er-rakabetu ma'rûfe ve a'teka rakabeten ve fekektu rakabeten ve rakabtu'r-racule ve'd-dâbbe izâ taraḥtu fî rakabetihî hablâ, gloss:boyun bilinir; bir boynu azat etti ve bir boynu çözdüm; adamın ya da hayvanın boynuna ip attığımda rakabtu derim, source:"ر ق ب,B004"}. Boyun, bağlanan bedenin yeridir. Kelime oradan bütün kişiye geçer: {ar:الرقبة اسم للعضو المعروف ثم يعبر بها عن الجملة واسما للمماليك, tr:er-rakabetu ismun li'l-udvi'l-ma'rûf summe yu'abbaru bihâ ani'l-cumle ve'sman li'l-memâlîk, gloss:rakabe bilinen organın adıdır, sonra bütün kişi ve sahip olunanlar için kullanılır, source:"ر ق ب,B004"}. İşleyiş açıktır: boyna ip atılır, rehin kilitlenir, ceylan tuzağa düşer. "Fekk" bu sıkı tutuşu açan harekettir.

Surenin başka kelimeleri de bu bağın çevresinde toplanır. Onuncu ayetin fiilinin ailesinde boyun, bir hayvanın önden giden yeridir: {ar:هادية الشاة الرقبة, tr:hâdiyetu'ş-şâti'r-rakabe, gloss:koyunun hâdiyesi boynudur, source:"ه د ي,B003"}. Bir başka söyleyiş de {ar:هوادي الخيل أعناقها, tr:hevâdi'l-hayli a'nâkuhâ, gloss:atların hevâdisi boyunlarıdır, source:"ه د ي,B003"}. Esir de aynı kökle anılır: {ar:يقال للأسير أيضا الهدي, tr:yukâlu li'l-esîri eydan el-hedî, gloss:esire de hedî denir, source:"ه د ي,B007"}. Geçidin kökü esirin fidyesini adlandırır: {ar:أخذت من أسيري عقبة إذا أخذت منه بدلا, tr:ehaztu min esîrî ukbeten izâ ehaztu minhu bedelâ, gloss:esirimden bir bedel aldığımda ondan ukbe aldım derim, source:"ع ق ب,B010"}. İkinci ayetin "hıll"i düğümü çözmektir: {ar:أصل الحل حل العقدة, tr:aslu'l-hall hallu'l-ukde, gloss:hallin aslı düğümü çözmektir, source:"ح ل ل,B001"}. Üçüncü ayetin "veled"i bebeği de köleyi de anar: {ar:الوليد الصبي والعبد والجمع ولدان وولدة, tr:el-velîdu's-sabiyyu ve'l-abd, gloss:velîd çocuk ve köledir, source:"و ل د,B004"}. On yedinci ayetin "sabr"ı da bağlamayı bilir: {ar:المصبورة المحبوسة على الموت, tr:el-masbûretu'l-mahbûsetu ale'l-mevt, gloss:masbûre ölmek için bağlanıp tutulan hayvandır, source:"ص ب ر,B002"}. Ama müminlerin sabrı bir başkasının boynunu değil, kendi nefsini tutar: {ar:صبرت نفسي أي حبستها, tr:sabertu nefsî ey habestuhâ, gloss:nefsimi tuttum, source:"ص ب ر,B001"}. Başkasını çözen, kendini tutar.

Surenin son ayeti bunun ters işlemini getirir: {ar:عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ, tr:aleyhim nârun mu'sade, gloss:üstlerine kapatılmış bir ateş vardır, source:90:20}. Fiil kapıyı kapamaktır: {ar:أوصدت الباب أغلقته والموصد المطبق, tr:evsadtu'l-bâbe ağlaktuh ve'l-mûsadu'l-mutbak, gloss:kapıyı kapattım yani kilitledim; mûsad üstü kapatılmış olandır, source:"و ص د,B001"}. Kapanış bir kapak gibidir: {ar:أوصدت الباب وآصدته أي أطبقته وأحكمته ومؤصدة مطبقة, tr:evsadtu'l-bâbe ve âsadtuhû ey etbaktuhû ve ahkemtuh ve mu'sadetun mutbaka, gloss:kapıyı kapattım yani üstüne kapak gibi kapadım ve sağlamlaştırdım; mu'sade üstü kapatılmış demektir, source:"و ص د,B001"}. Kökün temeli de birleştirmedir: {ar:أصل يدل على ضم شيء إلى شيء, tr:aslun yedullu alâ dammi şey'in ilâ şey', gloss:bir şeyi başka bir şeye kapatmayı bildiren kök, source:"و ص د,B001"}. Aynı kök evin önünü ve kapıyı ({ar:الوصيد فناء البيت والوصيد الباب, tr:el-vasîdu fenâu'l-beyt ve'l-vasîdu'l-bâb, gloss:vasîd evin önü ve kapıdır, source:"و ص د,B002"}), ayrıca mal için yapılmış taş ağılı adlandırır: {ar:الوصيدة حجرة تجعل للمال في الجبل, tr:el-vasîdetu hucretun tuc'alu li'l-mâli fi'l-cebel, gloss:vasîde dağda mal için yapılmış bir bölmedir, source:"و ص د,B003"}. Bir başka söyleyiş de {ar:الوصيدة كالحظيرة تتخذ للمال إلا أنها من الحجارة, tr:el-vasîdetu ke'l-hazîra, gloss:vasîde taştan bir ağıl gibidir, source:"و ص د,B003"}. Altıncı ayetin "mal"ı bu kökle duyulduğunda dağdaki taş ağıla kapatılmış bir sürüdür. Ateşin kapanışı da kendi kapattığı yerde kapanmaktır.

On dokuzuncu ayetin "keferû"su bu kapamayı örtmek olarak anlatır: {ar:كل شيء غطى شيئا فقد كفره, tr:kullu şey'in ğattâ şey'en fekad kefereh, gloss:bir şeyi örten her şey onu örtmüştür, source:"ك ف ر,B001"}. İnkâr da böyle tanımlanır: {ar:الكفر ضد الإيمان سمى لأنه تغطية الحق, tr:el-kufru diddu'l-îmân summiye li-ennehû tağtiyetu'l-hakk, gloss:küfür imanın zıddıdır ve hakkı örttüğü için bu adı aldı, source:"ك ف ر,B001"}. Gece bu yüzden "kâfir"dir: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylu kâfirun li-ennehû setera bi-zulmetih, gloss:gece karanlığıyla örttüğü için kâfirdir, source:"ك ف ر,B002"}. Çiftçi de öyle: {ar:يقال للزارع كافر لأنه يغطى الحب بتراب الأرض, tr:yukâlu li'z-zâri'i kâfirun li-ennehû yuğattı'l-habbe bi-turâbi'l-ard, gloss:ekinciye kâfir denir çünkü tohumu yerin toprağıyla örter, source:"ك ف ر,B008"}. Hurma çiçeğinin kını da bu kökle anılır: {ar:الكافور الطلع ووعاء طلع النخل وكذلك الكفرى, tr:el-kâfûru't-tal' ve vi'âu tal'i'n-nahl, gloss:kâfûr hurma çiçeği ve onu saran kındır, source:"ك ف ر,B010"}. Sabrın kökü bile bir şişenin ağzını tıkamayı bilir: {ar:أصبر سد رأس الحوجلة بالصبار وهو السداد, tr:asbara sedde ra'se'l-havcele bi's-sıbâr, gloss:şişenin ağzını tıpa ile tıkadı, source:"ص ب ر,B018"}. Sure böylece iki uç işlem arasında durur: on üçüncü ayette kapalı olanı açmak, yirminci ayette açık olanın üstünü kapamak. Örtenlerin üstü örtülür.

Kur'an'da bu iki uç birçok sahnede görünür. "Fekk" kökü Kur'an'da bir yerde daha geçer, o da inkârla birlikte: {ar:لَمْ يَكُنِ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ مُنفَكِّينَ حَتَّىٰ تَأْتِيَهُمُ ٱلْبَيِّنَةُ, tr:lem yekuni'llezîne keferû min ehli'l-kitâbi ve'l-muşrikîne munfekkîne hattâ te'tiyehumu'l-beyyine, gloss:kitap ehlinden ve müşriklerden inkâr edenler apaçık delil gelinceye kadar ayrılıp çözülecek değildi, source:98:1}. Savaşta inkâr edenlerle karşılaşan müminlere Allah {ar:فَضَرْبَ ٱلرِّقَابِ, tr:fe-darbe'r-rikâb, gloss:boyunlara vurun, source:47:4} der, ardından {ar:فَشُدُّوا۟ ٱلْوَثَاقَ فَإِمَّا مَنًّۢا بَعْدُ وَإِمَّا فِدَآءً, tr:fe-şuddu'l-vesâka fe-immâ mennen ba'du ve immâ fidâen, gloss:bağı sıkı tutun; sonra ya karşılıksız bırakın ya fidye alın, source:47:4} der. Boyun, bağ ve çözülüş tek ayettedir. İyiliğin tanımı bu boyunları sayar: {ar:وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ, tr:ve âte'l-mâle alâ hubbihî zevi'l-kurbâ ve'l-yetâmâ ve'l-mesâkîn, gloss:sevdiği hâlde malı yakınlara ve yetimlere ve yoksullara verdi, source:2:177}. Aynı ayette {ar:وَفِى ٱلرِّقَابِ, tr:ve fi'r-rikâb, gloss:ve boyunlar için, source:2:177} ve {ar:وَٱلصَّٰبِرِينَ فِى ٱلْبَأْسَآءِ وَٱلضَّرَّآءِ, tr:ve's-sâbirîne fi'l-be'sâi ve'd-darrâ, gloss:darlıkta ve sıkıntıda sabredenler, source:2:177} geçer. Surenin on üçüncü ve on yedinci ayetleri arasındakilerin hepsi neredeyse tek bir ayette toplanmıştır. Sadakaların gideceği yerler arasında da {ar:وَفِى ٱلرِّقَابِ, tr:ve fi'r-rikâb, gloss:ve boyunlar için, source:9:60} vardır. Sahip olunanlar özgürlük için yazışma isterse Allah {ar:فَكَاتِبُوهُمْ إِنْ عَلِمْتُمْ فِيهِمْ خَيْرًۭا ۖ وَءَاتُوهُم مِّن مَّالِ ٱللَّهِ ٱلَّذِىٓ ءَاتَىٰكُمْ, tr:fe-kâtibûhum in alimtum fîhim hayrâ ve âtûhum min mâlillâhi'llezî âtâkum, gloss:onlarda bir hayır görürseniz onlarla yazışın ve Allah'ın size verdiği maldan onlara verin, source:24:33} der. Mal burada bir boynu çözmek için Allah'ın malı olarak anılır. Yanlışlıkla öldürmenin karşılığı da {ar:فَتَحْرِيرُ رَقَبَةٍۢ مُّؤْمِنَةٍۢ, tr:fe-tahrîru rakabetin mu'mine, gloss:mümin bir boynu özgür bırakmak, source:4:92} olarak konur. Doyurulanlar arasında esir de vardır: {ar:وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا, tr:ve yut'imûne't-taâme alâ hubbihî miskînen ve yetîmen ve esîrâ, gloss:sevdikleri hâlde yemeği yoksula ve yetime ve esire yedirirler, source:76:8}.

Ters yüzde boyun kişinin kendi boynudur. Allah cimriyi kendi eli boynuna bağlanmış olarak anar: {ar:وَلَا تَجْعَلْ يَدَكَ مَغْلُولَةً إِلَىٰ عُنُقِكَ, tr:ve lâ tec'al yedeke mağlûleten ilâ unukik, gloss:elini boynuna bağlı kılma, source:17:29}. Kitabı sol eline verilen adam için {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe-ğullûh, gloss:onu tutun ve bağlayın, source:69:30} denir. Sebebi iki ayet sonra söylenir: {ar:إِنَّهُۥ كَانَ لَا يُؤْمِنُ بِٱللَّهِ ٱلْعَظِيمِ, tr:innehû kâne lâ yu'minu billâhi'l-azîm, gloss:o yüce Allah'a inanmıyordu, source:69:33} ve {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:ve yoksulun yemeğine teşvik etmiyordu, source:69:34}. Çözülmeyen boyun kişinin kendi bağlanmış boynuna döner. Yeniden yaratılmayı inkâr edenler için de aynı sahne kurulur: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ كَفَرُوا۟ بِرَبِّهِمْ ۖ وَأُو۟لَٰٓئِكَ ٱلْأَغْلَٰلُ فِىٓ أَعْنَاقِهِمْ ۖ وَأُو۟لَٰٓئِكَ أَصْحَٰبُ ٱلنَّارِ, tr:ulâike'llezîne keferû bi-rabbihim ve ulâike'l-ağlâlu fî a'nâkıhim ve ulâike ashâbu'n-nâr, gloss:onlar Rablerini inkâr edenlerdir ve onların boyunlarında halkalar vardır ve onlar ateşin halkıdır, source:13:5}. Aynı ayet onların sözünü de aktarır: {ar:أَءِذَا كُنَّا تُرَٰبًا, tr:e-izâ kunnâ turâbâ, gloss:biz toprak olduğumuzda mı, source:13:5}. İnkâr, toprak, boyundaki halka ve "ashâb" tek ayettedir. Allah'ın ayetleri hakkında tartışanlar için de {ar:إِذِ ٱلْأَغْلَٰلُ فِىٓ أَعْنَٰقِهِمْ وَٱلسَّلَٰسِلُ يُسْحَبُونَ, tr:izi'l-ağlâlu fî a'nâkıhim ve's-selâsilu yushabûn, gloss:boyunlarında halkalar ve zincirler olduğu hâlde sürüklenirler, source:40:71} denir. Yolun gösterildiği ayetin hemen ardından da {ar:إِنَّآ أَعْتَدْنَا لِلْكَٰفِرِينَ سَلَٰسِلَا۟ وَأَغْلَٰلًۭا وَسَعِيرًا, tr:innâ a'tednâ li'l-kâfirîne selâsile ve ağlâlen ve seîrâ, gloss:inkâr edenler için zincirler ve halkalar ve alevli bir ateş hazırladık, source:76:4} gelir. Bir başka surede kadının boynunda bir ip vardır: {ar:فِى جِيدِهَا حَبْلٌۭ مِّن مَّسَدٍۭ, tr:fî cîdihâ hablun min mesed, gloss:boynunda hurma lifinden bir ip, source:111:5}.

Kapanan ateş de Kur'an'da bir kez daha geçer. Mal toplayıp sayan için {ar:إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ, tr:innehâ aleyhim mu'sade, gloss:o onların üstüne kapatılmıştır, source:104:8} ve {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış direkler içinde, source:104:9} denir. Aynı kökün eşik anlamı mağara sahnesinde geçer. Allah uyuyanları anlatırken {ar:وَكَلْبُهُم بَٰسِطٌۭ ذِرَاعَيْهِ بِٱلْوَصِيدِ, tr:ve kelbuhum bâsitun zirâ'ayhi bi'l-vasîd, gloss:köpekleri de iki ön ayağını eşiğe uzatmıştı, source:18:18} der. Kapalılık gözlerin üstünde de vardır: {ar:خَتَمَ ٱللَّهُ عَلَىٰ قُلُوبِهِمْ وَعَلَىٰ سَمْعِهِمْ ۖ وَعَلَىٰٓ أَبْصَٰرِهِمْ غِشَٰوَةٌۭ, tr:hatemallâhu alâ kulûbihim ve alâ sem'ihim ve alâ ebsârihim ğışâve, gloss:Allah kalplerini ve kulaklarını mühürlemiştir ve gözlerinin üstünde bir perde vardır, source:2:7}. Bir başka yerde perde yol göstermeyi keser: {ar:وَجَعَلَ عَلَىٰ بَصَرِهِۦ غِشَٰوَةًۭ فَمَن يَهْدِيهِ مِنۢ بَعْدِ ٱللَّهِ, tr:ve ce'ale alâ basarihî ğışâveten fe-men yehdîhi min ba'dillâh, gloss:gözünün üstüne bir perde koydu; Allah'tan sonra ona kim yol gösterir, source:45:23}. Ayetleri yalanlayanlar için kapılar açılmaz: {ar:لَا تُفَتَّحُ لَهُمْ أَبْوَٰبُ ٱلسَّمَآءِ, tr:lâ tufettehu lehum ebvâbu's-semâ, gloss:onlara göğün kapıları açılmaz, source:7:40}. Kapalı ateşin içinden çıkış da yoktur: {ar:كُلَّمَآ أَرَادُوٓا۟ أَن يَخْرُجُوا۟ مِنْهَآ أُعِيدُوا۟ فِيهَا, tr:kullemâ erâdû en yahrucû minhâ u'îdû fîhâ, gloss:oradan çıkmak istedikçe oraya geri döndürülürler, source:32:20}.

Kaynaklar: 90:13 فَكُّ ف ك ك B001, B002; 90:13 رَقَبَةٍ ر ق ب B004; 90:10 وَهَدَيْنَٰهُ ه د ي B003, B007; 90:11 ٱلْعَقَبَةَ ع ق ب B010; 90:2 حِلٌّۢ ح ل ل B001; 90:3 وَلَدَ و ل د B004; 90:17 بِٱلصَّبْرِ ص ب ر B001, B002, B018; 90:20 مُّؤْصَدَةٌۢ و ص د B001, B002, B003; 90:19 كَفَرُوا۟ ك ف ر B001, B002, B008, B010

## Uzaktan görülen ateş

Sure ateşle biter: {ar:عَلَيْهِمْ نَارٌۭ مُّؤْصَدَةٌۢ, tr:aleyhim nârun mu'sade, gloss:üstlerine kapatılmış bir ateş vardır, source:90:20}. Ama ateşin kökü onu önce bir ışık yapar: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûru ve'n-nâru summiyâ bi-zâlike min tarîkati'l-idâe, gloss:nur ve nar aydınlatma yolundan ötürü bu adları aldı, source:"ن و ر,B001"}. Eskiden ateş yüksek yerlerde yol gösterilsin diye yakılırdı: {ar:كانوا ينورون في الجاهلية ليهتدى ويقتدى بها, tr:kânû yunevvirûne fi'l-câhiliyyeti li-yuhtedâ ve yuktedâ bihâ, gloss:cahiliyede onunla yol bulunsun ve ona uyulsun diye ateş yakarlardı, source:"ن و ر,B005"}. Yolun işareti de bu köktendir: {ar:المنار: علم الطريق, tr:el-menâr: alemu't-tarîk, gloss:menar yolun işaretidir, source:"ن و ر,B005"}. Bir başka söyleyiş de {ar:ضرب المنار على طريقه ليهتدى بها, tr:darabe'l-menâra alâ tarîkıhî li-yuhtedâ bihâ, gloss:yol bulunsun diye yolunun üstüne işaret dikti, source:"ن و ر,B005"}. Ateş uzaktan seçilir: {ar:تنورت النار من بعيد: تبصرتها, tr:tenevvertu'n-nâra min ba'îd: tebessartuhâ, gloss:ateşi uzaktan seçtim yani gözümle aradım, source:"ن و ر,B003"}. Dördüncü ayetin "insân" kelimesinin ailesi tam bu görüşü adlandırır: {ar:آنس من جانب يعني أبصر نارا, tr:ânese min cânib ya'nî ebsara nârâ, gloss:bir yandan ânese yani bir ateş gördü, source:"ء ن س,B002"}. Bir başka söyleyiş de {ar:فإن آنستم منهم رشدا أي أبصرتم وآنست نارا, tr:fe-in ânestum minhum ruşden ey ebsartum ve ânestu nârâ, gloss:onlarda olgunluk sezerseniz yani görürseniz; ve bir ateş sezdim, source:"ء ن س,B002"}. On altıncı ayetin kökü ateşi yanında dinlenilen bir şey olarak da bilir: {ar:السكن النار التي يسكن بها, tr:es-seken en-nâru'lletî yuskenu bihâ, gloss:seken yanında dinlenilen ateştir, source:"س ك ن,B004"}. Ateşin görüldüğü karanlık da on dokuzuncu ayetin köküyle anılır: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylu kâfirun li-ennehû setera bi-zulmetih, gloss:gece karanlığıyla örttüğü için kâfirdir, source:"ك ف ر,B002"}.

Böylece surenin başındaki yol sahnesine bir ışık da düşer. "Necd" yol kendi başına yol gösterir {source:"ن ج د,B002"}, ve ateşin yakılma sebebi de yol göstermektir. İkisi aynı işi görür. Gece yolcusu tepedeki ateşi uzaktan görür ve ona doğru yürür. Yirminci ayetteki ateş ise yolun üstünde bir işaret değildir. Üstü kapatılmıştır, uzaktan görülmez, içindekilerin üstüne kapanır. Düz bir anlatımın veremeyeceği şey bu tersine dönüştür: yolda yol gösterecek olan ateş, yolu görmezden gelenlerin üstüne kapak olur. Beşinci ve yedinci ayetlerin "yahsebu"su da gökten inen bir yangını bilir: {ar:حسبانا من السماء أي نارا تحرقها, tr:husbânen mine's-semâ ey nâran tuhrikuhâ, gloss:gökten bir husbân yani onu yakan bir ateş, source:"ح س ب,B007"}. Sanının kökünde bile bir ateş vardır.

Kur'an'da bu ateşin en açık sahnesi Musa'nındır. Allah elçisine {ar:وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ, tr:ve hel etâke hadîsu mûsâ, gloss:Musa'nın haberi sana geldi mi, source:20:9} diye sorar ve anlatır: {ar:إِذْ رَءَا نَارًۭا فَقَالَ لِأَهْلِهِ ٱمْكُثُوٓا۟ إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:iz reâ nâran fe-kâle li-ehlihi'mkusû innî ânestu nâran le'allî âtîkum minhâ bi-kabesin ev ecidu ale'n-nâri hudâ, gloss:hani bir ateş görmüştü de ailesine kalın, ben bir ateş seçtim; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösterici bulurum demişti, source:20:10}. Görmek, "ânestu" ve hidayet tek ayettedir: surenin yedinci, dördüncü ve onuncu ayetlerinin kökleri. Aynı sahne başka yerde ısınmayla da anlatılır: {ar:إِنِّىٓ ءَانَسْتُ نَارًۭا سَـَٔاتِيكُم مِّنْهَا بِخَبَرٍ أَوْ ءَاتِيكُم بِشِهَابٍۢ قَبَسٍۢ لَّعَلَّكُمْ تَصْطَلُونَ, tr:innî ânestu nâran se-âtîkum minhâ bi-haberin ev âtîkum bi-şihâbin kabesin le'allekum tastalûn, gloss:ben bir ateş seçtim; size ondan bir haber ya da ısınasınız diye yanan bir kor getireceğim, source:27:7}. Üçüncü anlatım ateşin bir dağın yanında görüldüğünü söyler: {ar:ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا, tr:ânese min cânibi't-tûri nârâ, gloss:dağın yanından bir ateş seçti, source:28:29}. Ateşi yaratan da kendini anar: {ar:أَفَرَءَيْتُمُ ٱلنَّارَ ٱلَّتِى تُورُونَ, tr:e-fe-raeytumu'n-nâra'lletî tûrûn, gloss:yaktığınız ateşi gördünüz mü, source:56:71}. Ardından {ar:نَحْنُ جَعَلْنَٰهَا تَذْكِرَةًۭ وَمَتَٰعًۭا, tr:nahnu ce'alnâhâ tezkiraten ve metâ'â, gloss:onu bir hatırlatma ve bir yararlanma kıldık, source:56:73} der. Ateş bir hatırlatmadır. Ama ışığı kaybetmenin sahnesi de anlatılır: {ar:مَثَلُهُمْ كَمَثَلِ ٱلَّذِى ٱسْتَوْقَدَ نَارًۭا فَلَمَّآ أَضَآءَتْ مَا حَوْلَهُۥ ذَهَبَ ٱللَّهُ بِنُورِهِمْ وَتَرَكَهُمْ فِى ظُلُمَٰتٍۢ لَّا يُبْصِرُونَ, tr:meseluhum ke-meseli'llezi'stevkade nâran fe-lemmâ edâet mâ havlehû zehebellâhu bi-nûrihim ve terakehum fî zulumâtin lâ yubsırûn, gloss:onların durumu ateş yakan kişinin durumu gibidir; ateş çevresini aydınlatınca Allah ışıklarını alıp götürdü ve onları görmez hâlde karanlıklarda bıraktı, source:2:17}. Mal yığanın ateşi ise kalplere kadar yükselir: {ar:ٱلَّتِى تَطَّلِعُ عَلَى ٱلْأَفْـِٔدَةِ, tr:elletî tattali'u ale'l-ef'ide, gloss:yüreklerin üstüne çıkıp onları saran, source:104:7}. Ardından {ar:إِنَّهَا عَلَيْهِم مُّؤْصَدَةٌۭ, tr:innehâ aleyhim mu'sade, gloss:o onların üstüne kapatılmıştır, source:104:8} gelir. Bir başka ateş de yüz çevirip biriktireni çağırır: {ar:كَلَّآ ۖ إِنَّهَا لَظَىٰ, tr:kellâ innehâ lezâ, gloss:hayır, o alevli bir ateştir, source:70:15}, {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:ted'û men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17} ve {ar:وَجَمَعَ فَأَوْعَىٰٓ, tr:ve ceme'a fe-ev'â, gloss:ve toplayıp kaba koyup saklayanı, source:70:18}. İki çaba anlatıldıktan sonra da uyarı ateşledir: {ar:فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ, tr:fe-enzertukum nâran telezzâ, gloss:sizi alev alev yanan bir ateşle uyardım, source:92:14}. Bu ateşe yalnızca {ar:ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ, tr:ellezî kezzebe ve tevellâ, gloss:yalanlayıp yüz çeviren, source:92:16} girer. Kapanmışlığın son sözü de çıkışsızlıktır: {ar:وَمَا هُم بِخَٰرِجِينَ مِنَ ٱلنَّارِ, tr:ve mâ hum bi-hâricîne mine'n-nâr, gloss:onlar ateşten çıkacak değildir, source:2:167}.

Kaynaklar: 90:20 نَارٌۭ ن و ر B001, B003, B005; 90:20 مُّؤْصَدَةٌۢ و ص د B001; 90:4 ٱلْإِنسَٰنَ ء ن س B002; 90:7 يَرَهُۥٓ ر ء ي B001; 90:10 ٱلنَّجْدَيْنِ ن ج د B002; 90:10 وَهَدَيْنَٰهُ ه د ي B001; 90:16 مِسْكِينًۭا س ك ن B004; 90:19 كَفَرُوا۟ ك ف ر B002; 90:5 أَيَحْسَبُ ح س ب B007; 90:17 بِٱلصَّبْرِ ص ب ر B013

## Buluşmalar

Görüntülerin en sık buluştuğu sahne yoldur. Onuncu ayetteki "necd" yolu kendi kendine yol gösterir, ateşin kökü de yüksek yerde yol gösterilsin diye yakılan ateşi anlatır. Sırt ile işaret ateşi aynı işi görür: gece yolcusuna nereye çıkacağını göstermek. Musa'nın sahnesi bu iki görüntüyü tek bir ayette taşır: dağın yanında görülen ateş ve {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidu ale'n-nâri hudâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10} umudu. Bu surede ise yolun sonundaki ateş bir işaret değildir, üstü kapatılmıştır. Yol sahnesiyle ateş sahnesi arasındaki fark, bir yolculuğun nasıl tersine döndüğünü gösterir. Atılmayan geçidin karşısında, içine dalınan bir ateş vardır: {ar:هَٰذَا فَوْجٌۭ مُّقْتَحِمٌۭ مَّعَكُمْ, tr:hâzâ fevcun muktehimun meakum, gloss:bu sizinle birlikte içeri dalan bir kalabalıktır, source:38:59}. Sabrın kökü de bu iki sahne arasında ikiye bölünür. Yokuşta kendini panikten tutan sabır vardır. Bir de kitabı gizleyenlerin {ar:فَمَآ أَصْبَرَهُمْ عَلَى ٱلنَّارِ, tr:fe-mâ asberahum ale'n-nâr, gloss:ateşe karşı ne kadar dayanıklılar, source:2:175} sözündeki ateşe cüret vardır.

İkinci büyük buluşma boyunla kapak arasındadır. On üçüncü ayetin fiili Arapçada kapalıyı açmak olarak tanımlanır: {ar:فكاك الرهن وهو فتحه من الانغلاق, tr:fikâku'r-rahni ve huve fethuhû mine'l-inğılâk, gloss:rehnin fikâkı onu kapalılıktan açmaktır, source:"ف ك ك,B002"}. Yirminci ayetin fiili de kapamak olarak tanımlanır: {ar:أوصدت الباب أغلقته, tr:evsadtu'l-bâbe ağlaktuh, gloss:kapıyı kapattım yani kilitledim, source:"و ص د,B001"}. Sure açılan bir boyundan kapanan bir ateşe doğru ilerler, ve iki fiil birbirinin tam tersidir. Bu iki ucu Kur'an'da tek bir sahne birleştirir. Kitabı sol eline verilen adamın boynu bağlanır ve bunun sebebi yoksulun yemeğine teşvik etmemesidir: {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:ve yoksulun yemeğine teşvik etmiyordu, source:69:34}. Sol taraf, boyundaki halka ve doyurulmayan yoksul bir aradadır. Malının bir işe yaramadığını söyleyen ve gücünün yok olup gittiğini gören de aynı adamdır. Bu sahnede sağ ile sol, harcanan mal, kıtlık ve boyun görüntüleri aynı yerde durur. Altıncı ayetteki "tükettim" orada şu söze döner: {ar:هَلَكَ عَنِّى سُلْطَٰنِيَهْ, tr:heleke annî sultâniyeh, gloss:gücüm benden yok olup gitti, source:69:29}.

Üçüncü buluşma yeminle geçit arasındadır. Yeminin kefareti ayeti, surenin on üçüncü ve on dördüncü ayetlerini birlikte sayar. Yeminler düğümlenir, sonra on yoksul doyurulur ya da bir boyun çözülür. Birinci ayetin yemini, ikinci ayetin "hıll"i, geçidin iki işi, on sekizinci ayetin sağ eli ve on dokuzuncu ayetin örtme kökü, bir yeminin bağlanıp çözülmesinin bütün aşamalarını taşır. Kur'an'ın bahçe sahipleri ise yemini ters yönde kullanır: yoksulu dışarıda bırakmak için yemin ederler. Bu ikisinin karşı karşıya gelmesi, surenin açılış yemininin neye açıldığını gösterir. Bu yemin bir şehirle başlar, şehirdeki yoksulun ağzıyla devam eder.

Gözetleyen göz ile harcanan mal, gösteriş kelimesinde buluşur. Gösteriş için harcayan, insanların görmesini ister ama Allah'ın görmediğini sanır. Bu çelişki tek bir ayette sahnelenir: malını {ar:رِئَآءَ ٱلنَّاسِ, tr:riâe'n-nâs, gloss:insanlara gösteriş için, source:2:264} harcayanın emeği kayanın üstündeki toprak gibi yıkanır gider. Aynı misal yere yapışma görüntüsünü de taşır: toprak, kaya ve yağmurla çıplak kalan taş. Ölçme görüntüsü de aynı ayete girer: {ar:لَّا يَقْدِرُونَ عَلَىٰ شَىْءٍۢ مِّمَّا كَسَبُوا۟, tr:lâ yakdirûne alâ şey'in mimmâ kesebû, gloss:kazandıklarından hiçbir şeye güç yetiremezler, source:2:264}. "Kimse bana güç yetiremez" sanısı, kendi kazancına güç yetirememekle biter. Ölçme ile yol da Kur'an'da tek bir dizide buluşur, ve bu dizi surenin sırasıdır: yaratan, ölçen, yol gösteren.

Soy ile kıtlık "yetim" kelimesinde buluşur. Babasından kopan çocuk, iyiliğin geç ulaştığı ve açlık gününde açlık çeken çocuktur. Dil bu ikisini tek bir örnekte birleştirir: {ar:يتيم ذو مسغبة أي ذو مجاعة, tr:yetîmun zû mesğabe ey zû mecâa, gloss:açlık sahibi yetim yani kıtlık içindeki yetim, source:"س غ ب,B001"}. Şehir ile kıtlık da kıtlık yılının tanımında buluşur: yıl bedevileri şehirlere atar. Kur'an'da doyurulan şehrin sahnesi de buradadır: {ar:ٱلَّذِىٓ أَطْعَمَهُم مِّن جُوعٍۢ وَءَامَنَهُم مِّنْ خَوْفٍۭ, tr:ellezî at'amehum min cû'in ve âmenehum min havf, gloss:onları açlıktan doyuran ve korkudan güvenliğe kavuşturan, source:106:4}. Yere yapışma ile geçit, yükselme ile saplanmanın aynı ayette karşı karşıya geldiği sahnede buluşur: ayetlerle yükseltilebilecekken yere saplanan adam. Bu da on dokuzuncu ayetin ayetleri inkâr edenlerine bağlanır.

Bütün bu görüntüler birlikte surenin hareketini taşır. Hareket yere oturmuş bir şehirde başlar. İnsan zorluğun ortasında yaratılmıştır. Malı keçeleşmiştir, kendini görülmez ve ölçülmez sanır. Ona gözler, dil ve dudaklar verilmiş, önüne görünen iki sırt konmuştur. İstenen şey yukarıya atılmaktır. Bu atılış da yere yapışmış olana eğilmek, bir boynun düğümünü çözmek ve aç bir ağza yemek koymaktır. Böyle atılanlar bitkiler gibi birbirine bitişir, aynı rahimden çıkmış gibi birbirine acır ve sağ tarafa yerleşir. Ayetleri örtenlerin üstü ise, yolda yol gösterebilecek bir ateşle kapatılır. Mağara sahnesindeki eşikte köpek ön ayaklarını uzatmış yatar: {ar:وَكَلْبُهُم بَٰسِطٌۭ ذِرَاعَيْهِ بِٱلْوَصِيدِ, tr:ve kelbuhum bâsitun zirâ'ayhi bi'l-vasîd, gloss:köpekleri iki ön ayağını eşiğe uzatmıştı, source:18:18}. Aynı ayette uyuyanlar sağa ve sola çevrilir. Yirminci ayetin kökü, sağ ve sol ile o eşiği orada tek bir sahnede bir araya getirir.

