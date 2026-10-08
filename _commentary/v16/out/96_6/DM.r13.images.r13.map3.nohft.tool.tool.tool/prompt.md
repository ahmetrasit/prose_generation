Focus: 96:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/96_6/D.r13/context.md =====
# 96:6 — focus

كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ

Anchor translation (canonical reading, reference only):

Hayır! İnsan gerçekten sınırı aşar.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | كَلَّآ | كَلَّا |  | AVR |
| 2 | إِنَّ | إِنّ |  | ACC |
| 3 | ٱلْإِنسَٰنَ | إِنسَٰن | ء ن س | DET;N |
| 4 | لَيَطْغَىٰٓ | طَغَىٰ | ط غ ي | EMPH;V |


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
- 96:4 ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ
- 96:5 عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ
- 96:6 ◀ focus كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ
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


===== _commentary/v16/work/96_6/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء ن س (root_000059) — identity root of ٱلْإِنسَٰنَ (w3)

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

## ط غ ي (root_000937) — identity root of لَيَطْغَىٰٓ (w4)

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

## ECHO ط غ و (root_000936) — for لَيَطْغَىٰٓ (w4): withheld observed target; not identity

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

===== _commentary/v16/out/s096/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 96:6, and ## Buluşmalar) =====
## Yontulan kamış, düzeltilen ok, kaygan kaya

Bu bölümdeki sahne sert malzeme üzerinde çalışan bir zanaatkârın sahnesidir. Zanaatkâr önce ölçer, sonra keser, yontar ve düzeltir. Birinci ve ikinci ayetlerdeki yaratma fiilinin kökü bu ilk adımı adlandırır: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme izâ kaddertuhû kable'l-katʿ, gloss:deriyi kesmeden önce ölçtüğümde onu "halk" ettim, source:"خ ل ق,B001"}; {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhu't-takdîru'l-mustakîm, gloss:halkın aslı doğru ölçmektir, source:"خ ل ق,B001"}. Kurân yaratmayı ölçmeyle yan yana koyar: {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe kaddarahû, gloss:onu bir damladan yarattı ve ölçüsünü verdi, source:80:19}.

Dördüncü ayetin kalemi, yontma işinden adını alır: {ar:أصل القلم القص من الشيء الصلب كالظفر وكعب الرمح والقصب, tr:aslu'l-kalemi'l-kassu mine'ş-şey'i's-sulb, gloss:kalemin aslı, tırnak, mızrak boğumu ve kamış gibi sert bir şeyden kesip almaktır, source:"ق ل م,B001"}; {ar:إنما سمي قلما لأنه قلم مرة بعد مرة, tr:innemâ summiye kalemen li ennehû kulime merraten baʿde merra, gloss:kalem denmesi, tekrar tekrar yontulduğu içindir, source:"ق ل م,B003"}. Öğreten Rab'bin aracı, defalarca yontulmuş bir kamıştır.

Yaratma kökü düzeltmeyi de adlandırır: {ar:السهم المصلح مخلق لأنه يصير أملس, tr:es-sehmu'l-muslahu muhallak, gloss:düzeltilmiş ok "muhallak"tır, çünkü pürüzsüz hale gelir, source:"خ ل ق,B008"}; {ar:المخلق القدح إذا لين, tr:el-muhallaku'l-kıdhu izâ luyyin, gloss:muhallak, yumuşatılmış kura okudur, source:"خ ل ق,B008"}. Kalem kökü de aynı nesneye varır: {ar:الأقلام ها هنا القداح جعلوا عليها علامات على جهة القرعة, tr:el-aklâmu hâhunâ el-kıdâh, gloss:buradaki kalemler, üzerine kura için işaret konmuş oklardır, source:"ق ل م,B004"}. Kurân bu nesneyi Meryem'in bakımı sahnesinde anar. Allah Peygamber'e, kendisinin orada olmadığı bir anı bildirir: {ar:إِذْ يُلْقُونَ أَقْلَٰمَهُمْ أَيُّهُمْ يَكْفُلُ مَرْيَمَ, tr:iz yulkûne aklâmehum eyyuhum yekfulu Meryem, gloss:Meryem'i hangisi üstlenecek diye kalemlerini atarlarken, source:3:44}. Cahiliye kura oklarıyla kısmet aramak ise yasaklanır: {ar:وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ ذَٰلِكُمْ فِسْقٌ, tr:ve en testaksimû bi'l-ezlâm, zâlikum fisk, gloss:fal oklarıyla pay aramanız da haram kılındı; bu yoldan çıkmaktır, source:5:3}. Bu okların toplandığı torbanın adı da rab kökündendir: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-rabâbe, gloss:rabâbe, kumar oklarının toplandığı sadağa benzer bir torbadır, source:"ر ب ب,B010"}.

Pürüzsüzleştirme sahnesinin bir de kaya hali vardır. Yaratma kökü kaygan kayayı adlandırır: {ar:صخرة خلقاء أي ملساء, tr:sahratun halkâ', gloss:halkâ kaya, yani kaygan kaya, source:"خ ل ق,B008"}. Altıncı ayetin {ar:لَيَطْغَىٰٓ, tr:le yatgâ, gloss:azar, source:96:6} fiilinin kökü de aynı kayayı adlandırır: {ar:الطغية الصفاة الملساء, tr:et-tugye es-safâtu'l-melsâ', gloss:tugye, kaygan kaya düzlüğüdür, source:"ط غ ي,B005"}. Kartalın pençesi bu kayada tutunamaz. Bu kayanın oyuklarında yağmur suyu birikir: {ar:الخليقة نقر في صخرة يجتمع فيه ماء السماء, tr:el-halîka nakrun fî sahra, gloss:halîka, kayada gök suyunun biriktiği oyuktur, source:"خ ل ق,B011"}. Böylece aynı kök hem ustaca işlenmiş nesneyi hem de üzerine tutunulamayan kayayı adlandırır. Azan insan, yontulup düzeltilmiş olduğunu unutup kendini hiçbir şeyin tutamadığı kaygan bir doruk sanır.

Kaynaklar: 96:1 خَلَقَ خ ل ق B001; 96:4 ٱلْقَلَمِ ق ل م B001; 96:4 ٱلْقَلَمِ ق ل م B003; 96:1 خَلَقَ خ ل ق B008; 96:4 ٱلْقَلَمِ ق ل م B004; 96:1 رَبِّكَ ر ب ب B010; 96:6 لَيَطْغَىٰٓ ط غ ي B005; 96:2 خَلَقَ خ ل ق B011

## Su: bulut, yağmur, taşkın ve gölet

Bu sahne suyun bütün yolculuğunu izler. Bulut yağmur getirir, ilk yağmur yeri bitkiyle işaretler, ardından ikinci yağmur gelir, yağmur döne döne yağar. Bazı yerler ise atlanır. Su bazen ölçüsünü aşar, taşar ve her şeyi sürükler, sonra yolunun sonundaki gölete varır ve orada durulur.

Üçüncü ayetteki en cömert sıfatının ailesinde yağmur getiren bulut ve verimli toprak vardır: {ar:كرم السحاب أتى بالغيث, tr:kerume's-sehâb, gloss:bulut cömert oldu, yani yağmur getirdi, source:"ك ر م,B002"}; {ar:أرض مكرمة للنبات, tr:ardun mekrame li'n-nebât, gloss:bitkiye cömert toprak, source:"ك ر م,B002"}. Rab kelimesinin ailesinde bitkileri büyüten bulut vardır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb, gloss:rabâb buluttur; bitkiyi büyüttüğü için böyle adlandırılmıştır, source:"ر ب ب,B008"}. Bu, rahimdeki cenini aşama aşama büyüten aynı terbiye işidir. Kayıtlı bir türetmeye göre ad kelimesinin ailesinde de yılın ilk yağmuru vardır: {ar:الوسمي أول مطر السنة يسم الأرض بالنبات, tr:el-vesmiyyu evvelu matari's-sene, gloss:vesmî, yeri bitkiyle işaretleyen yılın ilk yağmurudur, source:"و س م,B003"}. On üçüncü ayetteki {ar:وَتَوَلَّىٰٓ, tr:ve tevellâ, gloss:ve yüz çevirdi, source:96:13} fiilinin kökünde bu yağmuru izleyen yağmur bulunur: {ar:الولي المطر يجيء بعد الوسمي سمي بذلك لأنه يلي الوسمي, tr:el-veliyy el-matar yecî'u baʿde'l-vesmî, gloss:veliy, vesmîden sonra gelen yağmurdur; onu izlediği için böyle denir, source:"و ل ي,B010"}. Bu iki aile anlamı birer yankıdır; ayetlerdeki anlamlar "ad" ve "yüz çevirme"dir. Sekizinci ayetteki dönüş kelimesinin ailesinde ise dönüp duran yağmur vardır: {ar:الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث, tr:er-recʿu'l-gays, gloss:rec yağmurdur, çünkü yağar, sonra döner ve tekrar yağar, source:"ر ج ع,B006"}. Kurân göğe bu sıfatla yemin eder: {ar:وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ, tr:ve's-semâ'i zâti'r-recʿ, gloss:dönüp dönüp yağmur veren göğe andolsun, source:86:11}. On yedinci ayetin {ar:نَادِيَهُۥ, tr:nâdiyeh, gloss:meclisini, source:96:17} kelimesinin ailesinde nem ve cömertlik vardır: {ar:يعبر عن السخاء بالندى, tr:yuʿabbaru ʿani's-sehâ'i bi'n-nedâ, gloss:cömertlik "nem" ile ifade edilir, source:"ن د و,B004"}. On altıncı ayetin {ar:خَاطِئَةٍ, tr:hâti'e, gloss:günahkâr, source:96:16} kelimesinin ailesinde ise yağmurun atladığı toprak vardır: {ar:الخطيئة أرض يخطئها المطر ويصيب غيرها, tr:el-hatî'e ardun yuhti'uha'l-matar, gloss:hatîe, yağmurun ıskalayıp başka yere düştüğü topraktır, source:"خ ط ء,B003"}.

Kurân rahim ile yağmuru tek ayette birleştirir. Rahimdeki aşamalardan sonra {ar:وَتَرَى ٱلْأَرْضَ هَامِدَةً فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:ve tera'l-arda hâmideten fe izâ enzelnâ ʿaleyhe'l-mâ'e'htezzet ve rabet, gloss:yeri kupkuru görürsün; üzerine suyu indirince harekete geçer ve kabarır, source:22:5} denir. Bu ayet canlanmayı yaratılışla aynı kanıta bağlar. Dünya hayatı da yağmurla büyüyüp biçilen bir ekin olarak anlatılır: {ar:كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:keen lem tegne bi'l-ems, gloss:sanki dün orada hiç yokmuş gibi, source:10:24}. Bu ifadede, yedinci ayetin yeterlilik köküyle aynı kökten bir fiil, yerleşik yaşamın bir gecede silinmesini anlatır.

Su ölçüsünü de aşabilir. Altıncı ayetin azma fiili için {ar:طغى الماء خروجه عن المقدار, tr:tagâ'l-mâ' hurûcuhû ʿani'l-mikdâr, gloss:suyun azması ölçüsünden çıkmasıdır, source:"ط غ ي,B002"} ve {ar:طغا البحر والماء إذا علا كل شيء فاجترفه, tr:tagâ'l-bahru ve'l-mâ', gloss:deniz ve su her şeyin üstüne çıkıp onu sürükledi, source:"ط غ ي,B002"} denir. Kök genel olarak ölçüyü aşmaktır: {ar:كل شيء جاوز القدر فقد طغا, tr:kullu şey'in câveze'l-kadr fe kad tagâ, gloss:ölçüyü aşan her şey azmıştır, source:"ط غ ي,B001"}. Kurân bunu Nuh'un tufanı için kullanır: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tage'l-mâ'u hamelnâkum fi'l-câriye, gloss:su taştığında sizi akan gemide taşıdık, source:69:11}. Kuralı da teraziyle birlikte koyar: {ar:أَلَّا تَطْغَوْا۟ فِى ٱلْمِيزَانِ, tr:ellâ tatgav fi'l-mîzân, gloss:ölçüde aşırı gitmeyesiniz diye, source:55:8}. Böylece azma, yaratmanın ölçüsünün karşısına konur.

Taşkının sonu gölettir. On beşinci ayetin vazgeçme fiilinin ailesinde şu anlamlar bulunur: {ar:النهي والنهي الغدير لأن الماء ينتهي إليه, tr:en-nehy, el-gadîr, gloss:nehy göllenmiş sudur, çünkü su ona varıp durur, source:"ن ه ي,B004"}; {ar:تناهى الماء إذا وقف في الغدير وسكن, tr:tenâha'l-mâ', gloss:su gölette durup sakinleşti, source:"ن ه ي,B004"}. Dönüş kelimesinin ailesinde gölete de "rec" denir: {ar:سمي الغدير رجعا, tr:summiye'l-gadîru racʿan, gloss:gölete rec denmiştir, source:"ر ج ع,B006"}. Rab kelimesinin ailesinde de toplanmış bol su vardır: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabab el-mâ'u'l-kesîr, gloss:rabab, toplandığı için böyle denen bol sudur, source:"ر ب ب,B013"}. Böylece on beşinci ayetteki "vazgeçmezse" ifadesinin yanında, suyun durulduğu yerde durmaması da duyulur. Sekizinci ayet suyun varacağı yeri söyler. Kurân bunu ilahî adla birleştiren bir kardeş ayet içerir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Bu yapı sekizinci ayetle aynıdır; tek fark, dönüş yerine varış kökünün kullanılmasıdır.

Kaynaklar: 96:3 ٱلْأَكْرَمُ ك ر م B002; 96:1 رَبِّكَ ر ب ب B008; 96:1 بِٱسْمِ و س م B003; 96:13 وَتَوَلَّىٰٓ و ل ي B010; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B006; 96:17 نَادِيَهُۥ ن د و B004; 96:16 خَاطِئَةٍ خ ط ء B003; 96:6 لَيَطْغَىٰٓ ط غ ي B002; 96:6 لَيَطْغَىٰٓ ط غ ي B001; 96:15 يَنتَهِ ن ه ي B004; 96:8 رَبِّكَ ر ب ب B013

## Başın önü: perçem, alın ve yer

Bu sahne başın ön kısmında geçer. Saç çizgisinde perçem çıkar, altında alnın düz yüzü vardır. Azan adam bu kısmı yukarı kaldırır, bu kısımdan yakalanır ve derisi kararır. Kul ise aynı kısmı yere koyar.

On beşinci ve on altıncı ayetlerin {ar:ٱلنَّاصِيَةِ, tr:en-nâsiye, gloss:perçem, alnın üstündeki saç, source:96:15} kelimesi önce bir yeri adlandırır: {ar:الناصية منبت الشعر في مقدم الرأس, tr:en-nâsiyetu menbitu'ş-şaʿr fî mukaddemi'r-re's, gloss:nâsiye, başın önünde saçın bittiği yerdir, source:"ن ص ي,B001"}. Sonra bir tutuşu adlandırır: {ar:آخذ بناصيتها أي متمكن منها, tr:âhizun bi nâsiyetihâ, gloss:perçeminden tutan, yani ona tam hâkim olan, source:"ن ص ي,B001"}. On beşinci ayetin fiili bu tutuşun kendisidir: {ar:سفعت الفرس إذا أخذت بمقدم رأسه وهي ناصيته, tr:sefaʿtu'l-feres, gloss:atı başının önünden, yani perçeminden tuttum, source:"س ف ع,B001"}. Bu kalıp hem fiili hem perçemi tek cümlede birleştirir. Aynı fiil yüzün kararmasını da anlatır: {ar:سفعته النار والسموم إذا لفحته لفحا يسيرا فغيرت لون البشرة, tr:sefaʿathu'n-nâru ve's-semûm, gloss:ateş ya da kızgın rüzgâr onu hafifçe yalayıp deri rengini değiştirdi, source:"س ف ع,B003"}. Öfkeden kararan yüz için de {ar:به سفعة غضب, tr:bihî sufʿatu gadab, gloss:yüzünde öfke karası var, source:"س ف ع,B002"} denir. Kurân perçemden tutmayı her canlıya genelleştirir. Hud kavmine şöyle der: {ar:مَّا مِن دَآبَّةٍ إِلَّا هُوَ ءَاخِذٌۢ بِنَاصِيَتِهَآ, tr:mâ min dâbbetin illâ huve âhizun bi nâsiyetihâ, gloss:O'nun perçeminden tutmadığı hiçbir canlı yoktur, source:11:56}. Kurân bunu suçlular için de söyler: {ar:فَيُؤْخَذُ بِٱلنَّوَٰصِى وَٱلْأَقْدَامِ, tr:fe yu'hazu bi'n-nevâsî ve'l-akdâm, gloss:perçemlerinden ve ayaklarından tutulurlar, source:55:41}. Yüzün ateşte sürüklenmesi de anlatılır: {ar:يَوْمَ يُسْحَبُونَ فِى ٱلنَّارِ عَلَىٰ وُجُوهِهِمْ, tr:yevme yushabûne fi'n-nâri ʿalâ vucûhihim, gloss:ateşte yüzüstü sürüklenecekleri gün, source:54:48}. Cehennemin deriyi yakması da: {ar:لَوَّاحَةٌ لِّلْبَشَرِ, tr:levvâhatun li'l-beşer, gloss:deriyi kavurup karartan, source:74:29}.

Perçem aynı zamanda kavmin başıdır: {ar:فلان ناصية قومه, tr:fulânun nâsiyetu kavmih, gloss:falan kavminin perçemidir, yani önderidir, source:"ن ص ي,B003"}. Bu yüzden on altıncı ayetteki {ar:نَاصِيَةٍ كَٰذِبَةٍ خَاطِئَةٍ, tr:nâsiyetin kâzibetin hâti'e, gloss:yalancı, günahkâr bir perçem, source:96:16} ifadesinde hem adamın kendisi hem de on yedinci ayette çağırdığı meclisin başı duyulur. Sıfatlar perçeme yalan ve kasıtlı günah yükler: {ar:الخاطئ هو القاصد للذنب, tr:el-hâti'u huve'l-kâsidu li'z-zenb, gloss:hâti, günaha kasteden kişidir, source:"خ ط ء,B002"}.

Başın yükseltilmesi altıncı ayetin fiilinde de görülür: {ar:الطغية أعلى الجبل, tr:et-tugye aʿle'l-cebel, gloss:tugye dağın en yüksek yeridir, source:"ط غ ي,B005"}. Alnın düz yüzü de yaratma kökünden adlandırılır: {ar:خليقاء الجبهة مستواها, tr:halîkâ'u'l-cebhe, gloss:halîkâ, alnın düz yüzüdür, source:"خ ل ق,B008"}. Kurân başını en yükseğe kaldıranı Firavun'da gösterir: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe kâle ene rabbukumu'l-aʿlâ, gloss:"ben sizin en yüce rabbinizim" dedi, source:79:24}. Arkasından da {ar:فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ, tr:fe ehazehu'llâhu nekâle'l-âhirati ve'l-ûlâ, gloss:Allah onu ahiret ve dünya cezasıyla yakaladı, source:79:25} denir.

Son ayetin secde emri bu sahnenin karşı yüzüdür: {ar:سجد: خضع ومنه سجود الصلاة وهو وضع الجبهة على الأرض, tr:secede: hadaʿa, gloss:secde etti, yani boyun eğdi; namazdaki secde alnı yere koymaktır, source:"س ج د,B001"}; {ar:أسجد الرجل إذا طأطأ رأسه وانحنى, tr:escede'r-racul, gloss:adam başını eğip öne büküldü, source:"س ج د,B004"}. Yukarı kaldırılan ve yakalanıp karartılan alın ile yere konup secde izi taşıyan alın aynı organdır. Sure bu organı iki şekilde gösterir ve iki yol arasındaki farkı başın konumu üzerinden anlatır.

Kaynaklar: 96:15 ٱلنَّاصِيَةِ ن ص ي B001; 96:15 لَنَسْفَعًۢا س ف ع B001; 96:15 لَنَسْفَعًۢا س ف ع B002; 96:15 لَنَسْفَعًۢا س ف ع B003; 96:16 نَاصِيَةٍ ن ص ي B003; 96:16 خَاطِئَةٍ خ ط ء B002; 96:6 لَيَطْغَىٰٓ ط غ ي B005; 96:1 خَلَقَ خ ل ق B008; 96:19 وَٱسْجُدْ س ج د B001; 96:19 وَٱسْجُدْ س ج د B004

## Başından tutulan hayvan

Perçemden tutma sahnesi bir hayvanı da çağırır. Huysuz hayvan sağanı teper ya da insanlara direnir; perçeminden, burun ipinin ucundan tutulur. Dizgine uyan hayvan kolay yönetilir. Soylu at yakında tutulur ve değer görür.

On sekizinci ayetin {ar:ٱلزَّبَانِيَةَ, tr:ez-zebâniye, gloss:zebaniler, source:96:18} kelimesinin ailesinde, sağanı ya da yavrusunu ayağıyla iten deve vardır: {ar:ناقة زبون إذا زبنت حالبها أو ولدها عن ضرعها برجلها, tr:nâkatun zebûn, gloss:sağanı ya da yavrusunu ayağıyla memesinden iten deve, source:"ز ب ن,B001"}. Onuncu ayetin kul kelimesinin ailesinde iki zıt deve bulunur: {ar:بعير متعبد ومتأبد إذا امتنع على الناس صعوبة, tr:baʿîrun mutaʿabbid, gloss:insanlara direnen huysuz deve, source:"ع ب د,B011"} ve {ar:البعير المعبد المهنوء بالقطران المذلل, tr:el-baʿîru'l-muʿabbed, gloss:katranla bakılmış, alıştırılmış deve, source:"ع ب د,B005"}. On beşinci ayetin vazgeçme fiilinin ailesinde burun ipinin ucu vardır: {ar:النهاية طرف العران الذي في أنف البعير, tr:en-nihâye tarafu'l-ʿirân, gloss:nihâye, devenin burnundaki ipin ucudur, source:"ن ه ي,B002"}. Son ayetin {ar:تُطِعْهُ, tr:tutiʿhu, gloss:ona boyun eğme, source:96:19} fiilinin ailesinde de dizgine uyan at vardır: {ar:فرس طوع العنان, tr:ferasun tavʿu'l-ʿinân, gloss:dizgine uysal at, source:"ط و ع,B001"}.

Son ayetin {ar:وَٱقْتَرِب, tr:vakterib, gloss:ve yaklaş, source:96:19} emrinin ailesinde yakında tutulan at vardır: {ar:فرس مقربة وهي التي تدنى وتقرب ولا تترك أن ترود والمقربة المكرمة, tr:ferasun mukrabe … ve'l-mukrabetu'l-mukrame, gloss:mukrabe at, yakına alınıp otlamaya salınmayan attır; mukrabe, değer verilen demektir, source:"ق ر ب,B013"}. Bu ifade yakınlığı üçüncü ayetteki cömertlik köküyle birleştirir. Onuncu ayetin namaz fiilinin ailesinde de yarışta ikinci gelen at vardır: {ar:السابق الأول والمصلي الثاني, tr:es-sâbiku'l-evvel ve'l-musallî es-sânî, gloss:sâbık birincidir, musallî ikinci, source:"ص ل و,B006"}. İkinci atın başı öndekinin sağrısını izler. Kurân önde olanları yakınlıkla adlandırır: {ar:وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ, tr:ve's-sâbikûne's-sâbikûn, gloss:önde olanlar, önde olanlardır, source:56:10}, {ar:أُو۟لَٰٓئِكَ ٱلْمُقَرَّبُونَ, tr:ulâ'ike'l-mukarrabûn, gloss:onlar yakınlaştırılanlardır, source:56:11}. Atlar ile nankör insan da bir surede yan yana gelir: {ar:وَٱلْعَٰدِيَٰتِ ضَبْحًا, tr:ve'l-ʿâdiyâti dabhâ, gloss:soluk soluğa koşanlara andolsun, source:100:1}, {ar:إِنَّ ٱلْإِنسَٰنَ لِرَبِّهِۦ لَكَنُودٌ, tr:inne'l-insâne li rabbihî le kenûd, gloss:insan Rabbine karşı gerçekten nankördür, source:100:6}.

Bu sahnede azmak, dizgine direnmektir: {ar:مجاوزة الحد في العصيان, tr:mucâvezetu'l-hadd fi'l-ʿisyân, gloss:isyanda sınırı aşmak, source:"ط غ ي,B001"}. Yasaklayan adam huysuz hayvan gibi perçeminden tutulur. Kul ise yakında tutulan, değer gören at gibi yaklaşmaya çağrılır. "Ona boyun eğme" emri, hangi elin dizgine sahip olduğu sorusunu sorar.

Kaynaklar: 96:18 ٱلزَّبَانِيَةَ ز ب ن B001; 96:10 عَبْدًا ع ب د B011; 96:10 عَبْدًا ع ب د B005; 96:15 يَنتَهِ ن ه ي B002; 96:19 تُطِعْهُ ط و ع B001; 96:19 وَٱقْتَرِب ق ر ب B013; 96:10 صَلَّىٰٓ ص ل و B006; 96:6 لَيَطْغَىٰٓ ط غ ي B001

## Ateş: namaz kılan ve yanan

Onuncu ayetin {ar:صَلَّىٰٓ, tr:sallâ, gloss:namaz kıldı, source:96:10} fiilinin kökü iki tarafı birden adlandırır. Bir anlamı namazdır: {ar:الصلاة التي جاء بها الشرع من الركوع والسجود, tr:es-salâtu'lletî câ'e bihe'ş-şerʿ, gloss:şeriatın getirdiği rükû ve secdeli namaz, source:"ص ل و,B003"}. Öteki anlamı ateşe girmek ve sıcağına katlanmaktır: {ar:الصلا النار وصلى الكافر نارا, tr:es-salâ en-nâr, ve saliye'l-kâfiru nârâ, gloss:salâ ateştir; kâfir ateşe girdi, source:"ص ل و,B001"}; {ar:صليت العود بالنار, tr:salaytu'l-ʿûde bi'n-nâr, gloss:değneği ateşte tutup düzelttim, source:"ص ل و,B001"}. Kurân bu ikiliği kendi eşleştirmeleriyle kurar. Ateşe kimin gireceğini söylerken surenin on üçüncü ayetindeki ifadeyi kullanır: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}, {ar:ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ, tr:ellezî kezzebe ve tevellâ, gloss:ki yalanladı ve yüz çevirdi, source:92:16}, {ar:وَسَيُجَنَّبُهَا ٱلْأَتْقَى, tr:ve seyucennebuhe'l-etkâ, gloss:en çok sakınan ise ondan uzak tutulacak, source:92:17}. Bu ayetlerde ateşe girmek, yalanlamak, yüz çevirmek ve sakınmak bir aradadır; bunlar surenin on ikinci ve on üçüncü ayetlerinin kelimeleridir. Ölüm anındaki inkârcı için de namaz yalanlamanın karşısına konur: {ar:فَلَا صَدَّقَ وَلَا صَلَّىٰ, tr:fe lâ saddeka ve lâ sallâ, gloss:ne doğruladı ne namaz kıldı, source:75:31}, {ar:وَلَٰكِن كَذَّبَ وَتَوَلَّىٰ, tr:ve lâkin kezzebe ve tevellâ, gloss:ama yalanladı ve yüz çevirdi, source:75:32}. Musa ile Harun da Firavun'a aynı ifadeyle seslenir: {ar:أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ, tr:enne'l-ʿazâbe ʿalâ men kezzebe ve tevellâ, gloss:azap yalanlayıp yüz çevirenedir, source:20:48}. Cehennemdekiler ise kendilerini oraya getiren şeyi şöyle söyler: {ar:قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ, tr:kâlû lem neku mine'l-musallîn, gloss:"namaz kılanlardan değildik" dediler, source:74:43}.

Yakalamak ve ateşe atmak bir başka sahnede art arda gelir: {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe gullûh, gloss:tutun onu, bağlayın, source:69:30}, {ar:ثُمَّ ٱلْجَحِيمَ صَلُّوهُ, tr:summe'l-cahîme sallûh, gloss:sonra cehenneme atın, source:69:31}. Bu, yeterliliğinin işe yaramadığını söyleyen adamın sahnesidir. Ateş kendisi de çağırır: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Böylece on yedinci ve on sekizinci ayetlerin çağrısı ateşin çağrısıyla buluşur.

On beşinci ayetin fiili bu sahnede yüzün yanıp kararmasıdır: {ar:سفعته النار إذا لفحته لفحا يسيرا فسودت بشرته, tr:sefaʿathu'n-nâr, gloss:ateş onu hafifçe yaladı ve derisini kararttı, source:"س ف ع,B003"}. Altıncı ayetin fiilinin ailesinde yıldırım azabı vardır: {ar:الطاغية الصاعقة ويعني صيحة العذاب, tr:et-tâgiye es-sâʿika, gloss:tâgiye yıldırımdır, yani azap çığlığı, source:"ط غ ي,B004"}. Azgın için varılacak yer de söylenir: {ar:فَأَمَّا مَن طَغَىٰ, tr:fe emmâ men tagâ, gloss:azana gelince, source:79:37}, {ar:فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ, tr:fe inne'l-cahîme hiye'l-me'vâ, gloss:barınağı cehennemdir, source:79:39}. On ikinci ayetin {ar:بِٱلتَّقْوَىٰٓ, tr:bi't-takvâ, gloss:sakınmayı, source:96:12} kelimesi ise bu ateşe karşı bir kalkandır: {ar:التقوى جعل النفس في وقاية مما يخاف, tr:et-takvâ caʿlu'n-nefsi fî vikâye, gloss:takva, nefsi korkulan şeyden bir korunak içine almaktır, source:"و ق ي,B002"}. Kurân bu kökü ateşle birlikte kullanır: {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًا, tr:kû enfusekum ve ehlîkum nârâ, gloss:kendinizi ve ailenizi ateşten koruyun, source:66:6}.

Bu sahne, surenin kul ile yasaklayan arasında kurduğu karşıtlığı tek bir kökte toplar. Kul namazla ateşten korunur; yasaklayan, yasakladığı fiilin öteki anlamıyla karşılaşır.

Kaynaklar: 96:10 صَلَّىٰٓ ص ل و B003; 96:10 صَلَّىٰٓ ص ل و B001; 96:15 لَنَسْفَعًۢا س ف ع B003; 96:6 لَيَطْغَىٰٓ ط غ ي B004; 96:12 بِٱلتَّقْوَىٰٓ و ق ي B002

## Efendi, kul ve itaat

Bu sahnede bir sahip ve sahip olunan vardır. Rab kelimesi sahibi ve itaat edilen efendiyi adlandırır: {ar:يكون الرب: المالك؛ ويكون الرب: السيد المطاع, tr:yekûnu'r-rabb el-mâlik, ve yekûnu'r-rabb es-seyyidu'l-mutâʿ, gloss:rab sahip demektir; rab, itaat edilen efendi demektir de, source:"ر ب ب,B001"}. Bu tanım rabbi son ayetteki itaat fiiline bağlar. Onuncu ayetin kulu hem sahip olunandır hem de kulluğunu gösterendir: {ar:العبودية إظهار التذلل والعبادة غاية التذلل, tr:el-ʿubûdiyyetu izhâru't-tezellul, gloss:kulluk, alçakgönüllülüğü göstermektir; ibadet ise alçakgönüllülüğün en ileri derecesidir, source:"ع ب د,B003"}. Kulluk itaatle de birleşir: {ar:إياك نعبد إياك نطيع الطاعة التي نخضع معها, tr:iyyâke naʿbudu: iyyâke nutîʿ, gloss:"yalnız sana kulluk ederiz": yalnız sana, boyun eğerek itaat ederiz, source:"ع ب د,B003"}. Kökte çok yürünmüş, düzleşmiş yol da vardır: {ar:الطريق المعبد وهو المسلوك المذلل, tr:et-tarîku'l-muʿabbed, gloss:muabbed yol, çok yürünüp düzlenmiş yoldur, source:"ع ب د,B005"}.

Dokuzuncu ayetin {ar:يَنْهَىٰ, tr:yenhâ, gloss:men eder, source:96:9} fiili emrin zıddıdır: {ar:النهي خلاف الأمر, tr:en-nehyu hilâfu'l-emr, gloss:nehiy emrin zıddıdır, source:"ن ه ي,B001"}. On ikinci ayetin {ar:أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ, tr:ev emera bi't-takvâ, gloss:ya da sakınmayı emrettiyse, source:96:12} ifadesi, aynı kişinin aslında emredebilecek olduğunu söyler: {ar:الأمر الذي هو نقيض النهي, tr:el-emru'llezî huve nakîdu'n-nehy, gloss:nehyin zıddı olan emir, source:"ء م ر,B002"}. Aynı kök aklı da adlandırır: {ar:النهية العقل لأنه ينهى عن قبيح الفعل, tr:en-nuhye el-ʿakl, gloss:nuhye akıldır, çünkü çirkin işten alıkoyar, source:"ن ه ي,B003"}. Namazı yasaklayan adam, kendi aklının görevini tersine çevirir. Kurân namazın kendisinin yasakladığını söyler: {ar:إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ, tr:inne's-salâte tenhâ ʿani'l-fahşâ'i ve'l-munker, gloss:namaz hayâsızlıktan ve kötülükten alıkoyar, source:29:45}. Doğru yasaklama da nefsin kendisine yöneltilir: {ar:وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve nehe'n-nefse ʿani'l-hevâ, gloss:nefsini keyfî istekten alıkoyan, source:79:40}. Allah'ın mescitlerinde adının anılmasını engelleyen de anılır: {ar:وَمَنْ أَظْلَمُ مِمَّن مَّنَعَ مَسَٰجِدَ ٱللَّهِ أَن يُذْكَرَ فِيهَا ٱسْمُهُۥ, tr:ve men azlemu mimmen menaʿa mesâcida'llâhi en yuzkera fîhe'smuh, gloss:Allah'ın mescitlerinde adının anılmasını engelleyenden daha zalim kim olabilir, source:2:114}. Bu ayet, adla başlayan ve secdeyle biten surenin yasaklayanına yakındır.

Altıncı ayetin azma fiili itaatte sınırı aşmaktır; kök sahte mabudu da adlandırır: {ar:الطاغوت… كل معبود من دون الله, tr:et-tâgût … kullu maʿbûdin min dûni'llâh, gloss:tâgût, Allah'tan başka tapılan her şeydir, source:"ط غ ي,B003"}. Kurân bunun en açık örneği olarak Firavun'u gösterir: {ar:ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ, tr:izheb ilâ firʿavne innehû tagâ, gloss:Firavun'a git, çünkü o azdı, source:79:17}. Firavun sonunda kendini rab ilan eder. On dördüncü ayetteki Allah adının kökü ise tapılanı adlandırır: {ar:إله اسما لكل معبود… فالإله على هذا هو المعبود, tr:ilâh … el-maʿbûd, gloss:ilah, tapılan her şeyin adıdır; buna göre ilah tapılandır, source:"ء ل ه,B001"}.

Son ayetin {ar:لَا تُطِعْهُ, tr:lâ tutiʿhu, gloss:ona boyun eğme, source:96:19} emri, isteyerek boyun eğmeyi yasaklar: {ar:الطوع نقيض الكره, tr:et-tavʿu nakîdu'l-kerh, gloss:tav, zorlamanın zıddıdır, source:"ط و ع,B001"}. Kurân aynı yasağı Peygamber'e başka yerlerde de verir: {ar:فَلَا تُطِعِ ٱلْمُكَذِّبِينَ, tr:fe lâ tutiʿi'l-mukezzibîn, gloss:yalanlayanlara boyun eğme, source:68:8}; {ar:وَلَا تُطِعْ كُلَّ حَلَّافٍ مَّهِينٍ, tr:ve lâ tutiʿ kulle hallâfin mehîn, gloss:çok yemin eden aşağılık kimseye boyun eğme, source:68:10}. Bir başka yerde bu yasak, adı anmak ve secde etmekle aynı yerde geçer: {ar:وَلَا تُطِعْ مِنْهُمْ ءَاثِمًا أَوْ كَفُورًا, tr:ve lâ tutiʿ minhum âsimen ev kefûrâ, gloss:onlardan hiçbir günahkâra ya da nanköre boyun eğme, source:76:24}. Bundan hemen sonra adı anmak ve gece secde etmek emredilir. Bu, surenin son ayetinin yapısıyla aynıdır. Sahne surenin sorusunu açıkça ortaya koyar: kul kime itaat edecek? Sahibi Rab olan kul, kendini rab yerine koyan adama boyun eğmez.

Kaynaklar: 96:1 رَبِّكَ ر ب ب B001; 96:10 عَبْدًا ع ب د B003; 96:10 عَبْدًا ع ب د B005; 96:9 يَنْهَىٰ ن ه ي B001; 96:12 أَمَرَ ء م ر B002; 96:9 يَنْهَىٰ ن ه ي B003; 96:6 لَيَطْغَىٰٓ ط غ ي B003; 96:14 ٱللَّهَ ء ل ه B001; 96:19 تُطِعْهُ ط و ع B001

## Buluşmalar

İmgeler en açık şekilde baş sahnesinde buluşur. On beşinci ayetin fiili hem perçemden tutmak hem de yüzü karartmaktır. Böylece başın önü, avın yakalandığı yer, huysuz hayvanın tutulduğu yer ve ateşin yaladığı deri aynı noktada birleşir. Aynı alın son ayette yere konur ve secde izini taşır. İşaret imgesi buraya da uzanır: bir alın kararmış bir lekeyle işaretlenir, öteki secdenin iziyle. Kurân her iki tarafı da yüzlerindeki işaretle tanıtır: biri {ar:مِّنْ أَثَرِ ٱلسُّجُودِ, tr:min eseri's-sucûd, gloss:secdenin izinden, source:48:29}, öteki {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. Sure ad ile başlar ve iki işaretli alınla biter.

Göz ile yeterlilik imgeleri yedinci ayette buluşur. Kendini aynada gören adam ile süse ihtiyaç duymayan güzel kadın aynı kelime çiftinde birleşir: kendini görmek ve yeterli saymak. Su imgesi de buna bağlanır. Azan insan ölçüsünü aşan bir taşkın gibidir; on beşinci ayette durması istenir. Kökün göletteki duruluşu adlandırdığı hatırlanırsa, sekizinci ayet bu suyun nereye varacağını söyler. Kurân'ın varış ayeti bu iki imgeyi aynı yapıda birleştirir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Yol imgesi de bu dönüşe katılır, çünkü dönüş başlangıca dönmektir ve bu başlangıç rahimdeki ilk tutunuştur.

Rahim ile okuma, surenin ilk kelimesinde buluşur. Okumanın kökü hem rahmin bir şeyi toplayıp tutmasını hem de harflerin toplanmasını adlandırır. Pıhtıyı tutan kökle sözü toplayan kök aynıdır. İnsanın yaratılışı ve öğretilmesi bu yüzden aynı işin iki yüzü olarak duyulur. Kurân'daki benzer sıra da bunu destekler: Kurân'ı öğretmek, insanı yaratmak ve ona açıklamayı öğretmek. Okuma ile secde de buluşur: okuyucu aynı zamanda kulluk edendir ve sure, ilk emri okumak, son emri secde etmek olan bir eğri çizer. Kurân bu ikisini, okunduğunda secde edenler ile etmeyenler üzerinden birleştirir.

Ateş ile çağrı imgeleri onuncu, on yedinci ve on sekizinci ayetlerde buluşur. Namaz hem çağrıdır hem de kökü ateşe girmeyi adlandırır. Adam meclisini çağırır, Allah ateşe iten bekçileri çağırır ve kul yakın meclise çağrılır. Ateşin kendisinin de çağırdığı söylenir: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Bu yüz çevirme on üçüncü ayetin fiilidir.

İtaat ile hayvan imgeleri son ayette buluşur. Rab, itaat edilen efendidir; dizgine uyan at da itaatin bir figürüdür. Kul bu yüzden kendini rab ilan eden birine boyun eğmez, yakında tutulan ve değer gören at gibi yaklaşır. Yaratma ile uydurma da on altıncı ayette buluşur. Gerçek ölçüyle yaratan Rab'bin karşısında, yalanı içinde ölçen yalancı perçem durur.

Bu buluşmalar surenin hareketini taşır. Sure, rahimde toplanan ve tutunan bir varlıkla başlar; bu varlık sözü toplamayı ve kalemle yazmayı öğrenir. Sonra kendini aynada yeterli görür, taşkın su gibi ölçüsünü aşar, başını kaldırır ve namaz kılan kulu engellemeye çalışır. Dönüş ayeti ve Allah'ın görmesi bu yükselişin önüne bir sınır koyar. Yasaklayan perçeminden yakalanır, meclisi yerine bekçiler gelir. Kul ise yüz çevirmeden, başını yere koyarak, çağrılmış olduğu yakınlığa yürür.

