Focus: 89:18. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_18/D.r13/context.md =====
# 89:18 — focus

وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ

Anchor translation (canonical reading, reference only):

Ayrıca birbirinizi yoksulu doyurmaya teşvik etmiyorsunuz.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَلَا | لَا |  | CONJ;NEG |
| 2 | تَحَٰٓضُّونَ | تَحَٰٓضُّ | ح ض ض | V;PRON |
| 3 | عَلَىٰ | عَلَىٰ |  | P |
| 4 | طَعَامِ | طَعَام | ط ع م | N |
| 5 | ٱلْمِسْكِينِ | مِسْكِين | س ك ن | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 89 — full text (context; no pericope)

- 89:1 وَٱلْفَجْرِ
- 89:2 وَلَيَالٍ عَشْرٍۢ
- 89:3 وَٱلشَّفْعِ وَٱلْوَتْرِ
- 89:4 وَٱلَّيْلِ إِذَا يَسْرِ
- 89:5 هَلْ فِى ذَٰلِكَ قَسَمٌۭ لِّذِى حِجْرٍ
- 89:6 أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ
- 89:7 إِرَمَ ذَاتِ ٱلْعِمَادِ
- 89:8 ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ
- 89:9 وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ
- 89:10 وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ
- 89:11 ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ
- 89:12 فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ
- 89:13 فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ
- 89:14 إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ
- 89:15 فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ
- 89:16 وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
- 89:17 كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ
- 89:18 ◀ focus وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 89:19 وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا
- 89:20 وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا
- 89:21 كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا
- 89:22 وَجَآءَ رَبُّكَ وَٱلْمَلَكُ صَفًّۭا صَفًّۭا
- 89:23 وَجِا۟ىٓءَ يَوْمَئِذٍۭ بِجَهَنَّمَ ۚ يَوْمَئِذٍۢ يَتَذَكَّرُ ٱلْإِنسَٰنُ وَأَنَّىٰ لَهُ ٱلذِّكْرَىٰ
- 89:24 يَقُولُ يَٰلَيْتَنِى قَدَّمْتُ لِحَيَاتِى
- 89:25 فَيَوْمَئِذٍۢ لَّا يُعَذِّبُ عَذَابَهُۥٓ أَحَدٌۭ
- 89:26 وَلَا يُوثِقُ وَثَاقَهُۥٓ أَحَدٌۭ
- 89:27 يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ
- 89:28 ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ
- 89:29 فَٱدْخُلِى فِى عِبَٰدِى
- 89:30 وَٱدْخُلِى جَنَّتِى


===== _commentary/v16/work/89_18/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ح ض ض (root_000334) — identity root of تَحَٰٓضُّونَ (w2)

- **B001** birini belli bir eyleme ısrarla yöneltme — birini bir şeyi yapmaya güçlü biçimde yöneltmek · birini belli bir şeyi yapmaya ısrarla yöneltmek · birbirini bir eyleme yöneltme · iki kişinin birbirini özendirmesi · bir eyleme güçlü biçimde yöneltme · ısrarlı özendirme adı veya biçimi
  حضضته على كذا إذا حضضته عليه وحرضته (maqayis)؛ وقد حض يحض حضا (ayn)؛ حضه على القتال حضا أي حثه وحضضه أي حرضه والتحاض التحاث والمحاضة أن يحث كل واحد منهما صاحبه (sihah)؛ حض يحض حضا وهو الحث على الخير ويقال حضضت القوم على القتال تحضيضا إذا حرضتهم (tahdhib)؛ الحض التحريض كالحث (mufradat)
- **B002** dağ eteğindeki alçak taban — dağ eteğinde veya dağın bitiminde bulunan alçak zemin · dağ eteğinde bulunan taş
  الحضيض وهو قرار الأرض (maqayis)؛ الحضيض قرار الأرض عند سفح الجبل (ayn;tahdhib)؛ الحضيض القرار من الأرض عند منقطع الجبل ويعني بالأرض (sihah)؛ الحضيض وهو قرار الأرض (mufradat)
- **B003** yapısı farklı aktarılan acı reçinemsi sağaltım maddesi — acı reçineye benzetilen bilinen sağaltım maddesi
  الحضض دواء يتخذ من أبوال الإبل (ayn;tahdhib)؛ الحُضُض والحُضَض دواء معروف وهو صمغ مر كالصبر (sihah)؛ الحُضُض والحُضَض صمغ من نحو الصبر والمر (tahdhib)
- **B004** bir kimse için kendinden daha fazlasını isteme [kalıp] — bir kimse için kendinden daha fazlasını istemek
  احتضضت نفسي لفلان وابتضضتها إذا استزدتها (tahdhib)

## ط ع م (root_000934) — identity root of طَعَامِ (w4)

- **B001** tatma, yeme ve yenilen besin — tat, lezzet · yemek veya tadına bakmak · yiyecek, besin · özellikle buğday · tadına bakma ve iştahını yoklama · doyuran ve besleyen yiyecek ya da su · yeme isteği veya iştah çekici şey · çok yiyen, obur
  أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء (maqayis)؛ الطعم ذوقه والطعام اسم جامع لكل ما يؤكل (ayn)؛ طعم إذا أكل أو ذاق ومن لم يطعمه أي لم يذقه (sihah)؛ الطعم تناول الغذاء ويستعمل في الشراب (mufradat)
- **B002** başkasını beslemek veya beslenmeyi istemek — yiyecek vermek, doyurmak · kendisini doyurmasını istemek
  الإطعام يقع في كل ما يطعم (maqayis)؛ استطعمه سأله أن يطعمه وأطعمته الطعام (sihah)؛ استطعمه فأطعمه وأطعموا القانع ويطعمون الطعام (mufradat)
- **B003** söz istemek veya takılan imama söz vermek [kalıp] — benden konuşmamı istedi · imam okuyuşta takılırsa sözü hatırlatın
  استطعمني فلان الحديث إذا أرادك على أن تحدثه وإذا استطعمكم الإمام فأطعموه (maqayis)؛ إذا استفتح فافتحوا عليه (sihah)؛ إذا استفتحكم عند الارتياج فلقنوه (mufradat)
- **B004** geçim, bol ikram ve tahsis edilmiş gelir — geçimi yerinde · rızkı açık, kazançlı · çok ikram eden · geçim veya kazanç kaynağı · kazancı temiz veya kötü · araziyi birine geçim payı olarak ayırdı
  رجل طاعم حسن الحال ومطعام كثير القرى ومطعم مرزوق والطعمة المأكلة (maqayis)؛ حسن المطعم وحسن الطعمة (ayn)؛ الطعمة وجه المكسب وجعلت الضيعة طعمة (sihah)؛ ناحية كذا طعمة والخراج والإتاوات والفيء والخراج (tahdhib)
- **B005** olgunlaşıp tat kazanmak [kalıp] — ağacın meyvesi olgunlaşıp tat kazandı · tulumda hoş tat kazanmış süt
  للنخلة إذا أدرك ثمرها قد أطعمت (maqayis)؛ أطعمت النخلة واطعمت البسرة صار لها طعم وأخذت الطعم (sihah)؛ الشجر المثمر الذي يؤكل ثمره واطعمت الثمرة أخذت الطعم (tahdhib)
- **B006** avı kazandıran araç, uzuv veya kişi — av getiren yay · avcı kuşun öndeki kalın parmağı · avdan yana talihli, avı bol
  قوس مطعمة تطعم صاحبها الصيد والإصبع المتقدمة من الجارحة مطعمة (maqayis)؛ المطعمة القوس والمطعمتان في رجل كل طائر (sihah)؛ مطعم للصيد وقوس مطعمة والمطعمة من الجوارح (tahdhib)
- **B007** ilikte yağı beliren, biraz semiz hayvan — iliğinde yağ bulunan deve · biraz semiz, orta yağlı
  المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن (maqayis)؛ جزور طعوم وطعيم بين الغثة والسمينة (sihah)؛ ناقة طعوم وجزور طعوم وطعيم (tahdhib)
- **B008** akıl, değer ve düzelmeye açıklık niteliği [kalıp] — akıllı ve sağlam yargılı · aklı, devinimi veya değeri yok · terbiye kabul etmez, uslanmaz
  ما فلان بذي طعم إذا كان غثا (sihah)؛ رجل ذو طعم أي ذو عقل وحزم وما بفلان طعم ولا نويص ولا يطعم أي لا يتأدب ولا يعقل (tahdhib)
- **B009** atın ağız bölümü ve koşma talebi — atın burun altı ve dudak çevresi · attan koşmasını istedi
  مستطعم الفرس جحافله (sihah)؛ مستطعم الفرس ما تحت مرسنه إلى أطراف جحافله واستطعمت الفرس إذا طلبت جريه (tahdhib)
- **B010** eklenen şeyin tutması [kalıp] — dala aşı yaptı ve aşı tuttu · gözüne küçük bir yabancı cisim girdi
  أطعمت الغصن إذا وصلت به غصنا فقبل الوصل وأطعمت عينه قذى فطعمته (tahdhib)
- **B011** gücü yetmek [kalıp] — ona gücü yetti
  الطعم أيضا القدرة يقال طعمت عليه أي قدرت عليه (tahdhib)
- **B012** boğazından yakalayıp sıkmak [kalıp] — boğazından yakalayıp sıktı
  أخذ فلان بمطعمة فلان إذا أخذ بحلقه يعصره ولا يقولونها إلا عند الخنق والقتال (tahdhib)
- **B013** ağız ağıza temas etmek — ağız ağıza temas etme
  التطاعم إدخال الفم في الفم كما يفعل الحمام عند التقبيل (tahdhib)
- **B014** oluşumu ardışık olmak [kalıp] — oluşumu birbirini izleyen bölümlerden kurulu
  متطاعم الخلق أي متتابع الخلق (tahdhib)

## س ك ن (root_000726) — identity root of ٱلْمِسْكِينِ (w5)

- **B001** hareketin dinip durulması — hareketin sona erip şeyin durması · hareketi veya çalkantısı dindi ve durdu · rüzgar, yağmur ya da öfke dindi · hareketsiz, yerinde duran veya dingin
  خلاف الاضطراب والحركة؛ سكن الشيء سكونا فهو ساكن؛ السكون ذهاب الحركة؛ استقر وثبت؛ هدأ بعد تحرك؛ ثبوت الشيء بعد تحرك
- **B002** bir yere yerleşip orada yaşama — bir yere yerleşip orada yaşadı · konut, ev veya yaşanan yer · bir evi kira almadan oturması için verme · onu bir evde veya yerde oturttu · konut olarak kullanılan ev veya yer
  يسكنون الدار؛ المنزل وهو المسكن؛ سكون البيت؛ سكنت داري وأسكنتها غيرى؛ سكنى المرأة المسكن؛ يستعمل في الاستيطان واسم المكان مسكن والجمع مساكن
- **B003** ev halkı ve orada yaşayanlar — ev halkı ve aile üyeleri · bir yerde yaşayanlar · evde yaşayanlar; özel anlatıda evde bulunduğu düşünülen görünmez varlıklar
  السكن الأهل الذين يسكنون الدار؛ السكن السكان؛ السكن جزم العيال وهم أهل البيت؛ السكن أهل الدار؛ سكان الدار
- **B004** insanı rahatlatıp içini yatıştıran dayanak — insanın yanında rahatlayıp içinin yatıştığı kişi veya şey · yanında oturulup rahatlık bulunan ateş · senin yakarışların onları rahatlatır · geceyi dinlenme ve dinginleşme zamanı yaptı · eğri sırığı ateş ve yağla doğrultma
  كل ما سكنت إليه من محبوب؛ السكن أيضا كل ما سكنت إليه؛ ما سكنت إليه؛ إن صلواتك سكن لهم؛ جعل الليل سكنا؛ السكن النار التي يسكن بها
- **B005** güven veren ağırbaşlı iç dinginlik — ağırbaşlılık, yumuşak başlılık, güven ve kalp dinginliği · sandıktaki, kalpleri yatıştırıp güven veren şey · inananların kalplerine güven ve dinginlik verdi
  السكينة وهو الوقار؛ السكينة الوداعة والوقار؛ لا يفرون عنه أبدا وتطمئن قلوبهم إليه؛ فيه ما تسكنون به؛ عليك الوقار والوداعة والأمن؛ أنزل السكينة في قلوب المؤمنين
- **B006** yoksulluk, güçsüzlük ve ezilmişlik — yoksul ya da ezilmiş ve güçsüz kişi · yoksulluk veya ezilmişlik durumu · yoksul duruma geldi ya da boyun eğip kendini alçalttı · boyun eğdi ve alçaldı · Tanrı onu yoksul duruma düşürdü
  المسكنة مصدر فعل المسكين؛ المسكين الفقير وقد يكون بمعنى الذلة والضعف؛ تمسكن إذا خضع لله وهي المسكنة للذلة؛ استكان أي خضع وذل
- **B007** kesici bıçak — kesici bıçak · bıçak yapan kimse
  السكين معروف؛ السكين المدية؛ السكين معروف يذكر ويؤنث؛ سمي سكينا لأنها تسكن الذبيحة؛ السكين سمي لإزالته حركة المذبوح
- **B008** geminin kıçındaki dengeleyici yöneltme aracı — geminin kıçındaki, onu dengede tutup yönelten bölüm veya araç · gemiyi dengede tutup çalkantısını azaltan kıç parçası
  سكان السفينة سمى لأنه يسكنها عن الاضطراب؛ السكان ذنب السفينة الذي به تعدل؛ السكان أيضا ذنب السفينة؛ السكان وهو الكوثل؛ سكان السفينة ما يسكن به
- **B009** sabit yer ve konum bildiren özel kullanımlar — başın boyuna oturduğu yer · yerlerinizde, konumlarınızda veya alışılmış düzeninizde · belirli bir bölgedeki özel yer adı
  موضع من أرض الكوفة؛ السكنة مقر الرأس من العنق؛ استقروا على سكناتكم أي على مواضعكم ومساكنكم؛ الناس على سكناتهم أي على استقامتهم؛ على طبقاتهم ومنازلهم
- **B010** yerinde kalmayı sağlayan geçimlik ve bol otlak — bulunduğu yerde geçinmeyi sağlayan yiyecekler · yerinde kalmayı sağlayan bir geçimlik · sürüyü göç ettirmeye gerek bırakmayacak kadar bol otlak
  الأسكان الأقوات واحدها سكن؛ قيل للقوت سكن لأن المكان به يسكن؛ مرعى مسكن إذا كان كثيرا لا يخرج إلى الظعن عنه

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:18, and ## Buluşmalar) =====
## Pay, sofra ve ağzına kadar dolan kap

Rızık bir paydır: {ar:الرزق يقال للعطاء الجاري وللنصيب, tr:er-rızku yukâlu li'l-atâi'l-câri ve li'n-nasîb, gloss:rızık, akıp gelen bağış için de pay için de söylenir, source:"ر ز ق,B001"}. Her şeyin bir ölçüsü vardır: {ar:لكل شيء مقدار وأجل, tr:li-kulli şey'in mikdârun ve ecel, gloss:her şeyin bir ölçüsü ve bir süresi vardır, source:"ق د ر,B001"}. Kur'an da geçimi kendisinin bölüştürdüğünü söyler: {ar:نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ, tr:nahnu kasemnâ beynehum maîşetehum, gloss:aralarında geçimlerini biz bölüştürdük, source:43:32}, {ar:ٱللَّهُ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ وَيَقْدِرُ, tr:Allâhu yebsutu'r-rızka li-men yeşâu ve yakdir, gloss:Allah rızkı dilediğine genişletir ve daraltır, source:13:26}. Beşinci ayetteki kasem kelimesinin kökü bu bölüştürmeyi adlandırır, mirasın sahiplerine ayrılmasını da içine alarak: {ar:إفراز النصيب وقسمة الميراث والغنيمة تفريقهما على أربابهما, tr:ifrâzu'n-nasîbi ve kısmetu'l-mîrâsi ve'l-ğanîmeti tefrîkuhumâ alâ erbâbihimâ, gloss:payı ayırmak; miras ve ganimeti bölmek, onları sahiplerine dağıtmaktır, source:"ق س م,B003"}. Kur'an'ın miras hükmü surenin sofrasını tek bir ayette kurar: {ar:وَإِذَا حَضَرَ ٱلْقِسْمَةَ أُو۟لُوا۟ ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينُ فَٱرْزُقُوهُم مِّنْهُ, tr:ve izâ hadara'l-kısmete ulu'l-kurbâ ve'l-yetâmâ ve'l-mesâkînu ferzukûhum minh, gloss:paylaştırmada akrabalar, yetimler ve yoksullar hazır bulunursa onlara da ondan rızık verin, source:4:8}. Paylaştırma, yetim, yoksul ve rızık: on altıncı ayetle on dokuzuncu ayet arasındaki bütün öğeler buradadır. Payın kendisi de konmuştur: {ar:نَصِيبًۭا مَّفْرُوضًۭا, tr:nasîben mefrûdâ, gloss:belirlenmiş bir pay, source:4:7}.

On sekizinci ayet bu sofraya kimin çağrılmadığını söyler: {ar:وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ tehâddûne alâ taâmi'l-miskîn, gloss:yoksulu doyurmaya birbirinizi teşvik etmiyorsunuz, source:89:18}. Fiilin kalıbı karşılıklıdır: {ar:والمحاضة أن يحث كل واحد منهما صاحبه, tr:ve'l-muhâdda en yehusse kullu vâhidin minhumâ sâhibeh, gloss:muhâdda, ikisinden her birinin ötekini teşvik etmesidir, source:"ح ض ض,B001"}. Kınanan şey yalnız tek tek kişilerin cimriliği değildir. Topluluğun birbirini yoksula yöneltmeyi bırakmasıdır. Yemek, birinin istediği şeydir: {ar:استطعمه سأله أن يطعمه, tr:istat'amehû seelehû en yut'imeh, gloss:ondan yemek istedi, source:"ط ع م,B002"}. Yoksul da zayıf düşmüş kişidir: {ar:المسكين الفقير وقد يكون بمعنى الذلة والضعف, tr:el-miskînu'l-fakîr, ve kad yekûnu bi-ma'ne'z-zilleti ve'd-da'f, gloss:miskin fakirdir; düşkünlük ve zayıflık anlamına da gelir, source:"س ك ن,B006"}. Aynı kök azığı, insanın yerinde kalabilmesini sağlayan şey olarak adlandırır: {ar:قيل للقوت سكن لأن المكان به يسكن, tr:kîle li'l-kûti sekenun li-enne'l-mekâne bihî yusken, gloss:azığa seken denir, çünkü bir yerde onunla oturulur, source:"س ك ن,B010"}. Yoksulun payını vermek, onun yerinde durabilmesini sağlamaktır. Kur'an aynı cümleyi başka iki sahnede tekrarlar. Biri dini yalanlayanın tarifidir: {ar:فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ, tr:fe-zâlike'llezî yeduu'l-yetîm, gloss:işte o, yetimi itip kakandır, source:107:2}, {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ taâmi'l-miskîn, gloss:yoksulu doyurmaya teşvik etmez, source:107:3}. Öteki kitabı sol eline verilen kişinin zincirlenme sebebidir {source:69:34}. Sarp yokuş da açlık gününde yakın bir yetimi ya da toprağa düşmüş bir yoksulu doyurmaktır: {ar:أَوْ إِطْعَٰمٌۭ فِى يَوْمٍۢ ذِى مَسْغَبَةٍۢ, tr:ev it'âmun fî yevmin zî mesğabeh, gloss:ya da açlık gününde doyurmak, source:90:14}, {ar:يَتِيمًۭا ذَا مَقْرَبَةٍ, tr:yetîmen zâ makrabeh, gloss:yakını olan bir yetimi, source:90:15}, {ar:أَوْ مِسْكِينًۭا ذَا مَتْرَبَةٍۢ, tr:ev miskînen zâ metrabeh, gloss:ya da toprağa düşmüş bir yoksulu, source:90:16}.

On dokuzuncu ayet sofranın öbür ucunu gösterir: {ar:وَتَأْكُلُونَ ٱلتُّرَاثَ أَكْلًۭا لَّمًّۭا, tr:ve te'kulûne't-turâse eklen lemmâ, gloss:mirası silip süpürerek yiyorsunuz, source:89:19}. Miras, bir topluluğa ait olanın başkalarına geçmesidir: {ar:أن يكون الشيء لقوم ثم يصير إلى آخرين بنسب أو سبب, tr:en yekûne'ş-şey'u li-kavmin summe yasîra ilâ âharîne bi-nesebin ev sebeb, gloss:bir şeyin bir topluluğa ait olup sonra soy ya da başka bir sebeple başkalarına geçmesi, source:"و ر ث,B001"}. Miras geçerken paylara ayrılmalıdır. Lemm ise ayırmadan hepsini toplamaktır: {ar:لممته أجمع حتى أتيت على آخره, tr:lememtuhû ecmaa hattâ eteytu alâ âhirih, gloss:sonuna kadar hepsini toplayıp aldım, source:"ل م م,B001"}. Yemek fiili zayıfların malını yemeyi de anlatır: {ar:فلان يستأكل الضعفاء أي يأخذ أموالهم, tr:fulânun yeste'kilu'd-duafâe ey ye'huzu emvâlehum, gloss:falanca zayıfları yiyor, yani mallarını alıyor, source:"ء ك ل,B004"}. Kur'an yetimlerin malı için şöyle uyarır: {ar:وَلَا تَأْكُلُوٓا۟ أَمْوَٰلَهُمْ إِلَىٰٓ أَمْوَٰلِكُمْ, tr:ve lâ te'kulû emvâlehum ilâ emvâlikum, gloss:onların mallarını kendi mallarınıza katarak yemeyin, source:4:2}. O malın aslında ne olduğunu da gösterir: {ar:إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا, tr:innemâ ye'kulûne fî butûnihim nârâ, gloss:onlar karınlarına ancak ateş yerler, source:4:10}. Aynı fiil ateşin işidir: {ar:أكلت النار الحطب, tr:ekeleti'n-nâru'l-hatab, gloss:ateş odunu yedi, source:"ء ك ل,B005"}. Yiyen, yirmi üçüncü ayette getirilen ateşle karşılaşır. Miras da sonunda asıl sahibine döner: {ar:يبقى ويفنى من سواه فيرجع ما كان ملك العباد إليه, tr:yebkâ ve yefnâ men sivâhu fe-yerciu mâ kâne milke'l-ibâdi ileyh, gloss:O kalır, O'ndan başkası yok olur ve kulların mülkü O'na döner, source:"و ر ث,B004"}. Kur'an bunu şöyle söyler: {ar:إِنَّا نَحْنُ نَرِثُ ٱلْأَرْضَ وَمَنْ عَلَيْهَا وَإِلَيْنَا يُرْجَعُونَ, tr:innâ nahnu neriçu'l-arda ve men aleyhâ ve ileynâ yurceûn, gloss:yere ve üzerindekilere biz varis oluruz ve onlar bize döndürülür, source:19:40}. Bir başka ayet de göklerin ve yerin mirasının Allah'a ait olduğunu hatırlatarak harcamaya çağırır {source:57:10}.

Yirminci ayet yığılan malı bir kaba koyar: {ar:وَتُحِبُّونَ ٱلْمَالَ حُبًّۭا جَمًّۭا, tr:ve tuhibbûne'l-mâle hubben cemmâ, gloss:malı aşırı bir sevgiyle seviyorsunuz, source:89:20}. Cemm bir ölçeğin ağzına kadar dolmasıdır: {ar:أعطيته جمام المكوك وجمامه إذا قارب أن يمتلئ, tr:a'taytuhû cumâme'l-mekkûki ve cimâmehû izâ kâraba en yemtelî', gloss:ölçeği ağzına kadar, neredeyse taşacak kadar doldurup verdim, source:"ج م م,B001"}. Suyun yığılmış kütlesi de böyle adlandırılır: {ar:جمة الماء معظمه ومجتمعه, tr:cemmetu'l-mâi mu'zamuhû ve muctemeuh, gloss:suyun cemmesi, en büyük ve toplanmış kısmıdır, source:"ج م م,B001"}. Sevgi kelimesinin kökü de dolmayı ve kabı adlandırır: {ar:وحببته فتحبب إذا ملأته للسقاء وغيره, tr:ve habebtuhû fe-tehabbebe izâ mele'tuhû li's-sikâi ve ğayrih, gloss:su tulumunu ve benzerini doldurdum, doldu, source:"ح ب ب,B006"}, {ar:الحب الجرة الضخمة, tr:el-hubb el-cerratu'd-dahme, gloss:hubb, iri küptür, source:"ح ب ب,B007"}. Aynı harfler tahılı da adlandırır: {ar:الحب والحبة في الحنطة والشعير, tr:el-habbu ve'l-habbe fi'l-hıntati ve'ş-şaîr, gloss:habb, buğday ve arpa tanesidir, source:"ح ب ب,B001"}. Ayette anlam aşırı sevgidir. Yanında ağzına kadar dolmuş bir küp duyulur, hem de yoksulun istediği tahılla dolu bir küp. On ikinci ayetteki çoğaltma fiili de bu yarışı taşır: {ar:المكاثرة والتكاثر التباري في كثرة المال والعز, tr:el-mukâsera ve't-tekâsur et-tebârî fî kesreti'l-mâli ve'l-izz, gloss:mal ve itibar çokluğunda yarışmak, source:"ك ث ر,B002"}. Kur'an bu dolduranı birkaç sahnede gösterir: {ar:أَلْهَىٰكُمُ ٱلتَّكَاثُرُ, tr:elhâkumu't-tekâsur, gloss:çoğaltma yarışı sizi oyaladı, source:102:1}. Bir diğeri malı toplayıp sayandır: {ar:ٱلَّذِى جَمَعَ مَالًۭا وَعَدَّدَهُۥ, tr:ellezî cemea mâlen ve addedeh, gloss:mal toplayıp onu sayan, source:104:2}, {ar:يَحْسَبُ أَنَّ مَالَهُۥٓ أَخْلَدَهُۥ, tr:yahsebu enne mâlehû ahledeh, gloss:malının kendisini ölümsüz kılacağını sanır, source:104:3}. Ateş de toplayıp istifleyeni çağırır: {ar:وَجَمَعَ فَأَوْعَىٰٓ, tr:ve cemea fe-ev'â, gloss:toplayıp kaba istifleyen, source:70:18}. Sevginin sofraya dönen biçimi de Kur'an'dadır: {ar:وَيُطْعِمُونَ ٱلطَّعَامَ عَلَىٰ حُبِّهِۦ مِسْكِينًۭا وَيَتِيمًۭا وَأَسِيرًا, tr:ve yut'imûne't-taâme alâ hubbihî miskînen ve yetîmen ve esîrâ, gloss:yemeği, ona olan sevgilerine rağmen yoksula, yetime ve esire yedirirler, source:76:8}. Malın da: {ar:وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ ذَوِى ٱلْقُرْبَىٰ وَٱلْيَتَٰمَىٰ وَٱلْمَسَٰكِينَ, tr:ve âte'l-mâle alâ hubbihî zevi'l-kurbâ ve'l-yetâmâ ve'l-mesâkîn, gloss:malı, ona olan sevgisine rağmen akrabalara, yetimlere ve yoksullara veren, source:2:177}. Sevgi aynıdır, ama burada kap dolmaz, boşaltılır. Ağzına kadar dolmuş küpün sonu da Kur'an'da gösterilir. Kitabı sol eline verilen şöyle der: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ ۜ, tr:mâ ağnâ annî mâliyeh, gloss:malım bana hiçbir yarar sağlamadı, source:69:28}. Cehennem ise hiç dolmayan bir kaptır: {ar:يَوْمَ نَقُولُ لِجَهَنَّمَ هَلِ ٱمْتَلَأْتِ وَتَقُولُ هَلْ مِن مَّزِيدٍۢ, tr:yevme nekûlu li-cehenneme heli'mtele'ti ve tekûlu hel min mezîd, gloss:o gün cehenneme "doldun mu?" deriz, o da "daha yok mu?" der, source:50:30}.

Kaynaklar: 89:5 قَسَمٌۭ ق س م B003; 89:12 فَأَكْثَرُوا۟ ك ث ر B002; 89:16 فَقَدَرَ ق د ر B001; 89:16 رِزْقَهُۥ ر ز ق B001; 89:18 تَحَٰٓضُّونَ ح ض ض B001; 89:18 طَعَامِ ط ع م B002; 89:18 ٱلْمِسْكِينِ س ك ن B006; 89:18 ٱلْمِسْكِينِ س ك ن B010; 89:19 وَتَأْكُلُونَ ء ك ل B004; 89:19 وَتَأْكُلُونَ ء ك ل B005; 89:19 ٱلتُّرَاثَ و ر ث B001; 89:19 ٱلتُّرَاثَ و ر ث B004; 89:19 لَّمًّۭا ل م م B001; 89:20 حُبًّۭا ح ب ب B001; 89:20 وَتُحِبُّونَ ح ب ب B006; 89:20 حُبًّۭا ح ب ب B007; 89:20 جَمًّۭا ج م م B001

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

