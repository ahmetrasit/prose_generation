Focus: 98:1. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/98_1/D.r13/context.md =====
# 98:1 — focus

لَمْ يَكُنِ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ مُنفَكِّينَ حَتَّىٰ تَأْتِيَهُمُ ٱلْبَيِّنَةُ

Anchor translation (canonical reading, reference only):

Kitap ehlinden inkâr edenler ve Allah'a ortak koşanlar, kendilerine açık kanıt gelinceye kadar ayrılacak değillerdi.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | لَمْ | لَم |  | NEG |
| 2 | يَكُنِ | كَانَ | ك و ن | V |
| 3 | ٱلَّذِينَ | ٱلَّذِى |  | REL |
| 4 | كَفَرُوا۟ | كَفَرَ | ك ف ر | V;PRON |
| 5 | مِنْ | مِن |  | P |
| 6 | أَهْلِ | أَهْل | ء ه ل | N |
| 7 | ٱلْكِتَٰبِ | كِتَٰب | ك ت ب | DET;N |
| 8 | وَٱلْمُشْرِكِينَ | مُشْرِك | ش ر ك | CONJ;DET;N |
| 9 | مُنفَكِّينَ | مُنفَكِّين | ف ك ك | N |
| 10 | حَتَّىٰ | حَتَّىٰ |  | P |
| 11 | تَأْتِيَهُمُ | أَتَى | ء ت ي | V;PRON |
| 12 | ٱلْبَيِّنَةُ | بَيِّنَة | ب ي ن | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 98 — full text (context; no pericope)

- 98:1 ◀ focus لَمْ يَكُنِ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ مُنفَكِّينَ حَتَّىٰ تَأْتِيَهُمُ ٱلْبَيِّنَةُ
- 98:2 رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ
- 98:3 فِيهَا كُتُبٌۭ قَيِّمَةٌۭ
- 98:4 وَمَا تَفَرَّقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ إِلَّا مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَةُ
- 98:5 وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ
- 98:6 إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ
- 98:7 إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ
- 98:8 جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ


===== _commentary/v16/work/98_1/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ك و ن (root_001332) — identity root of يَكُنِ (w2)

- **B001** gerçekleşme, bulunma ve olma bildirimi — gerçekleşip ortaya çıkmak veya hazır bulunmak · geçmişte bir durumu bildirmek · oluş; gerçekleşme · olma, oluş · sonradan gerçekleşen iş · yüklemi pekiştiren ek söz · birini geliş kapsamı dışında tutan bağlı söz · var edip gerçekleşmesini sağlamak
  الكون الحدث يكون بين الناس ومصدر من كان يكون؛ الكينونة في مصدر كان؛ الكائنة الأمر الحادث (ayn); كان عبارة عما مضى من الزمان؛ حدوث الشيء ووقوعه؛ كان الأمر أي مذ خلق؛ تقع زائدة للتوكيد؛ لا يكون زيدا تعني الاستثناء؛ كونه فتكون أحدثه فحدث (sihah); أصل يدل على الإخبار عن حدوث شيء إما في زمان ماض أو زمان راهن؛ كان الشيء يكون كونا إذا وقع وحضر (maqayis)
- **B002** bulunma yeri ve konum değeri — bulunulan yer · yerler · konum, düzey veya bulunulan yer · birinin yanında güçlü konumu olan · yerleşmek veya güç kazanmak · birinin yanında şu yer veya düzeyde bulunmak
  المكان اشتقاقه من كان يكون؛ تمكن (ayn;maqayis); فلان مني مكان هذا؛ موضع العمامة (ayn); المكانة المنزلة؛ مكين عند فلان بين المكانة؛ المكان والمكانة الموضع؛ تمكن (sihah)
- **B003** birini güvenceyle üstlenme — başkası için güvence üstlenme · birini üstlenmek · birine güvence olmak
  الكيانة الكفالة؛ كنت على فلان أكون كونا أي تكفلت به؛ اكتنت به اكتيانا مثله (sihah); كنت على فلان أكون عليه إذا كفلت به؛ اكتنت أيضا اكتيانا (maqayis)
- **B004** boyun eğme — boyun eğme
  الاستكانة الخضوع (sihah)
- **B005** gençliğini anan yaşlı kişi — gençken şöyleydim diye anlatan yaşlı kişi
  يقال للرجل إذا شاخ كُنْتِيّ؛ كأنه نسب إلى قوله كُنْتُ في شبابي كذا وكذا (sihah)
- **B006** kötü durumda gece geçirme [kalıp] — geceyi kötü durumda geçirmek
  الكينة في قولهم بات فلان بكينة سوء أي بحال سوء فأصله الكون فعلة من الكون (maqayis)

## ك ف ر (root_001307) — identity root of كَفَرُوا۟ (w4)

- **B001** örtmek, kapatmak — bir şeyi örtmek ve kapatmak · zırhının üstüne bir giysi geçirmek · silahlarıyla örtünmek veya silah kuşanmak · rüzgârın savurduğu toprakla örtülmüş kül · güneşin yıldızları görünmez kılması
  الستر والتغطية (maqayis)؛ كل شيء غطى شيئا فقد كفره (ayn;sihah;tahdhib)؛ كفرت الشيء أي سترته ورماد مكفور (sihah)؛ تكفر في السلاح (mufradat)؛ كفرت الشمس النجوم (mufradat)
- **B002** örten karanlık veya enginlik — karanlık gece, deniz, büyük ırmak, gün batımı veya bulut
  الكافر مغيب الشمس ويقال بل البحر والنهر العظيم كافر (maqayis)؛ الكافر الليل والبحر ومغيب الشمس والكافر النهر العظيم (ayn)؛ الكافر الليل المظلم والكافر البحر والنهر العظيم (sihah)؛ الليل كافر لأنه ستر بظلمته (tahdhib)؛ وصف الليل بالكافر لستره الأشخاص والكافر للسحاب (mufradat)
- **B003** dinî gerçeği reddetme — dinî gerçeği veya inancı reddetme · kalben bildiği gerçeği diliyle kabul etmeme · gerçeği bildiği hâlde inatla kabul etmemek · kalben reddederken diliyle inanmış görünmek · gerçeği hem kalple hem dille inkâr etmek
  الكفر ضد الإيمان سمى لأنه تغطية الحق (maqayis)؛ الكفر نقيض الإيمان والكفر أربعة أنحاء كفر الجحود وكفر المعاندة وكفر النفاق وكفر الإنكار (ayn)؛ الكفر ضد الإيمان (sihah)؛ الكفر نقيض الإيمان وكفر إنكار وكفر جحود وكفر معاندة وكفر نفاق وكفر هو شرك وكفر بكتاب الله ورسوله والتكذيب بالله (tahdhib)؛ أعظم الكفر جحود الوحدانية أو الشريعة أو النبوة (mufradat)
- **B004** nimeti yadsıma — nimeti yadsımak ve şükrünü yerine getirmemek · nimeti yadsıma ve şükretmeme · nimetleri aşırı biçimde yadsıyan kimse · iyilikleri karşılıksız ve teşekkürsüz kalan cömert adam
  كفران النعمة جحودها وسترها (maqayis)؛ الكفر نقيض الشكر كفر النعمة أي لم يشكرها (ayn)؛ الكفر أيضا جحود النعمة وهو ضد الشكر (sihah)؛ الكفر كفر النعمة وهو نقيض الشكر (tahdhib)؛ كفر النعمة وكفرانها سترها بترك أداء شكرها (mufradat)
- **B005** bağını reddedip uzaklaşmak — bir şeyle bağını reddedip ondan uzaklaşmak
  يكون الكفر أيضا بمعنى البراءة (tahdhib)؛ قد يعبر عن التبري بالكفر (mufradat)
- **B006** inançsız saymak — birini inançsız saymak veya öyle adlandırmak
  أكفرت الرجل أي دعوته كافرا لا تكفر أحدا (sihah)؛ أكفره إكفارا حكم بكفره (mufradat)
- **B007** itaatsizliğe zorlamak — itaat eden birini itaatsizliğe zorlamak
  إذا ألجأت مطيعك إلى أن يعصيك فقد أكفرته (ayn;tahdhib)
- **B008** tohumu örten çiftçi — tohumu toprakla örten çiftçi · tohumları toprakla örten çiftçiler
  يقال للزارع كافر لأنه يغطى الحب بتراب الأرض (maqayis)؛ الكافر الزارع لأنه يغطي البذر بالتراب (sihah)؛ الزراع لستره البذر في الأرض (mufradat)؛ الكفار الزراع (mufradat)
- **B009** günah yükünü giderme — günahı veya bozulan yeminin yükünü gideren karşılık · bozulan yeminin gerektirdiği yükümlülüğü yerine getirme · günahları örtüp etkisini silme
  الكفارة ما يكفر به من الخطيئة واليمين فيمحى به (ayn)؛ تكفير اليمين فعل ما يجب بالحنث فيها والاسم الكفارة والتكفير في المعاصي (sihah)؛ الكفارة ما يغطي الإثم والتكفير ستره وتغطيته حتى يصير بمنزلة ما لم يعمل (mufradat)
- **B010** çiçek veya meyve kılıfı — üzüm salkımının veya hurma çiçeğinin kılıfı · hurma çiçeğinin ya da meyvenin kılıfı · hurma ağacından çıkan kapalı çiçek kılıfları
  الكافور كم العنب قبل أن ينور وسمى كافورا لأنه كفر الوليع أي غطاه (maqayis)؛ الكافور كم العنب قبل أن ينور وكافوره ورقة الذي يستره والكافور الطلع والكفرى والكوافير (ayn)؛ الكافور الطلع ووعاء طلع النخل وكذلك الكفرى (sihah)؛ الكافور اسم أكمام الثمرة التي تكفرها والكافور أكمام الثمرة (mufradat)
- **B011** koku maddesi, su kaynağı veya bitki — güzel kokulu karışımlarda kullanılan madde · cennetteki bir su kaynağı · çiçeği papatyaya benzeyen bir bitki
  الكافور شيء من أخلاط الطيب والكافور عين ماء في الجنة والكافور نبات نوره كنور الأقحوان (ayn)؛ الكافور من الطيب (sihah)؛ الكافور الذي هو من الطيب (mufradat)
- **B012** uzak arazi; köy, uzak yer halkı veya mezar — insanlardan uzak, pek uğranmayan arazi · köy veya mezar · köyler veya uzak yerlerin halkı
  الكفر من الأرض ما بعد من الناس وأهل الكفور والقرى (maqayis)؛ الكافر من الأرض ما بعد عن الناس والكفور القرى (ayn)؛ الكفر أيضا القرية والكفر أيضا القبر (sihah)؛ الكافر من الأرض ما بعد عن الناس (tahdhib)
- **B013** dağ geçidi; iri dağ veya alçak duvar — dağ geçitleri · dağ geçidi veya iri dağ · alçak duvar
  الكفرات والكفر الثنايا من الجبال (maqayis)؛ الكفر الثنايا من الجبال (ayn)؛ الكفر العظيم من الجبال (sihah)؛ الكافر الحائط الواطىء (tahdhib)
- **B014** eğilerek boyun eğme gösterisi — başını eğmek veya elini göğsüne koyup eğilmek
  التكفير إيماء الذمي برأسه لا يقال سجد له وإنما يقال كفر له (ayn)؛ التكفير أن يخضع الإنسان لغيره يضع يده على صدره ويتطامن له (sihah)
- **B015** hükümdara taç giydirme veya taç — hükümdara taç giydirme veya tacın kendisi
  التكفير تتويج الملك بتاج والتكفير ههنا التاج نفسه (ayn)

## ء ه ل (root_000064) — identity root of أَهْلِ (w6)

- **B001** yakın çevre ve bağlı topluluk — yakınlık, ev, din veya başka bir bağla birleşen insan çevresi · bir erkeğin eşi ve en yakın insanları · evin sakinleri ve eve bağlı sayılan kişiler · Islam'a bağlı olan kişiler · yakın çevre veya ev halkı için çoğul biçimler
  أهل الرجل زوجه وأخص الناس به؛ أهل البيت سكانه؛ أهل الإسلام من يدين به (maqayis;ayn;tahdhib)؛ أهل الرجل من يجمعه وإياهم نسب أو دين أو صناعة وبيت وبلد (mufradat)؛ أهل الرجال وأهل الدار (sihah)
- **B002** evlenip yakın çevre edinmek — evlenmek ve eş edinmek · bir kadını eş olarak almak · Allah sana cennette eş ve yakın çevre versin
  التأهل التزوج (maqayis;ayn)؛ أهل فلان يأهل أهولا أي تزوج وكذلك تأهل (sihah)؛ أهل الرجل يأهل أهولا إذا تزوج للأنس الذي بين الزوجين (tahdhib)؛ تأهل إذا تزوج ومنه آهلك الله في الجنة أي زوجك فيها وجعل لك فيها أهلا (mufradat)
- **B003** uygun ve layık olmak — bir şey için uygun ve yaraşır olmak · saygı gösterilmeye ve bağışlamaya layık olan · onu bu iş için uygun ve hazır hale getirdi · bu işi hak etmiş sayılan kimse; kullanımı tartışmalı
  أهلته لهذا الأمر تأهيلا (maqayis;ayn;tahdhib)؛ فلان أهل كذا أو كذا (ayn;tahdhib)؛ هو أهل التقوى وأهل المغفرة أي أهل لأن يتقى وأهل لمغفرة من اتقاه (ayn;tahdhib)؛ فلان أهل لكذا أي خليق به (mufradat)؛ فلان أهل لكذا ولا تقل مستأهل (sihah)
- **B004** sakinli ve alışılmış yerleşiklik — sakinleri bulunan yer · içinde yaşayanları olan yer · eskiden içinde yaşanmış konaklama yerleri · insanlara ve yerleşim yerlerine alışmış, evcil · onunla yakınlık duydum ve yabancılık çekmedim · insanları ve sakinleri bulunan hale geldi
  مكان آهل مأهول (maqayis)؛ مكان مأهول فيه أهل ومكان آهل له أهل (ayn;tahdhib)؛ منزل آهل أي به أهله (sihah)؛ كل شيء من الدواب وغيرها إذا ألف مكانا فهو آهل وأهلي (maqayis;tahdhib)؛ كل دابة ألف مكانا يقال أهل وأهلي (mufradat)؛ أهلت به إذا استأنست به (sihah;tahdhib)
- **B005** rahatlatan karşılama sözü — geniş yer ve yakın insanlar buldun; rahat ol, yabancılık çekme
  مرحبا وأهلا أي أتيت سعة وأتيت أهلا فاستأنس ولا تستوحش (sihah)؛ مرحبا وأهلا ومعناه نزلت رحبا أي سعة وأتيت أهلا لا غرباء (tahdhib)؛ مرحبا وأهلا في التحية للنازل بالإنسان أي وجدت سعة مكان عندنا (mufradat)
- **B006** eritilmiş yemeklik yağ — kuyruk yağı, iç yağı, don yağı, sıvı yağ veya katık yapılan yağlı madde · bu yağlı maddeden alan veya onu yiyen kimse · bu yağlı maddeyi yemeğe katık yaptı
  الأصل الآخر الإهالة وهي الألية ونحوها يؤخذ فيقطع ويذاب (maqayis)؛ الإهالة الودك والمستأهل الذي يأخذ الإهالة أو يأكلها (sihah)؛ الإهالة هي الشحم والزيت قط؛ كل ما اؤتدم به من زبد وودك شحم ودهن سمسم وغيره فهو إهالة؛ استأهل الرجل إذا ائتدم بالإهالة (tahdhib)

## ك ت ب (root_001283) — identity root of ٱلْكِتَٰبِ (w7)

- **B001** bir şeyi başka bir şeye katıp birleştirme — bir şeyi başka bir şeye katıp birleştirme · su tulumunu dikerek birleştirmek · katırın üreme organının dudaklarını halka veya kayışla birleştirmek · dişi devenin burun deliklerini iplikle dikmek veya bağlamak · dişi devenin memelerini bağlamak · su tulumunun ağzını bağıyla sıkıca kapatmak · kayışın iki yüzünü birleştiren boncuk · bir arada duran atlı veya askerî birlik · atların toplanması · askerleri birlik birlik düzenlemek
  أصل صحيح واحد يدل على جمع شيء إلى شيء (maqayis)؛ أصل الكتب ضمك الشيء إلى الشيء (jamhara)؛ ضم أديم إلى أديم بالخياطة (mufradat)؛ كتبت السقاء إذا خرزته (tahdhib)؛ كتبت البغلة إذا جمعت بين شفريها بحلقة (sihah;mufradat)؛ الكتيبة جماعة مستحيزة (sihah;tahdhib)
- **B002** yazma ve yazılı metin — kitabı yazmak veya kopyalamak · yazılı metin veya üzerinde yazı bulunan sayfa · yazma işi ve yazıcılık · kitabı yazmak veya kopyalamak · ona şiiri söyleyerek yazdırmak · birinden kendisi için bir şey yazmasını istemek · çocuğa yazmayı öğretmek · yazı öğretmeni veya yazı öğretilen yer · öğretim yerindeki çocuklar veya onların topluluğu
  الكتاب والكتابة يقال كتبت الكتاب أكتبه كتبا (maqayis)؛ وقد كتب الكتاب يكتبه كتبا إذا جمع حروفه (jamhara)؛ الكتاب معروف وقد كتبت كتبا وكتابا وكتابة (sihah)؛ كتبت الكتاب كتبا وكتابا فالكتاب اسم لما كتب مجموعا (tahdhib)؛ في التعارف ضم الحروف بعضها إلى بعض بالخط (mufradat)؛ أكتبني هذه القصيدة أي أملها علي (sihah)؛ استكتبه الشيء أي سأله أن يكتبه له (sihah;tahdhib)
- **B003** bağlayıcı olarak hükme bağlama ve belirleme — yükümlülük, hüküm veya yazgı · size zorunlu kılındı · Tanrı belirledi, karara bağladı veya zorunlu kıldı
  الكتاب وهو الفرض (maqayis)؛ يقال للحكم الكتاب (maqayis)؛ يقال للقدر الكتاب (maqayis)؛ الكتاب الفرض والحكم والقدر (sihah)؛ الكتاب يوضع موضع الفرض (tahdhib)؛ يعبر عن الإثبات والتقدير والإيجاب والفرض والعزم بالكتابة (mufradat)؛ يعبر بالكتابة عن القضاء الممضى (mufradat)
- **B004** adını sicile yazma veya bir gruba dâhil etme — pay veya geçim tahsisatı için kaydolma · adını pay kaydına veya yönetim siciline yazdırmak · bizi tanıklar topluluğuna kat
  الكتبة الاكتتاب في الفرض والرزق (ayn;tahdhib)؛ اكتتب فلان أي كتب اسمه في الفرض (ayn;tahdhib)؛ اكتتب الرجل إذا كتب نفسه في ديوان السلطان (sihah)؛ فاكتبنا مع الشاهدين أي اجعلنا في زمرتهم (mufradat)
- **B005** özgürlük bedelini ödemeye dayalı özgürleşme sözleşmesi — kölenin bedelini ödeyerek özgürlüğünü kazanma sözleşmesi · özgürlük bedeli sözleşmesinin tarafı olan köle; bağlama göre sahibi · köleyle özgürlük bedeli ödemesine dayalı sözleşme yapmak · kölenin özgürlüğünü satın almak için yaptığı sözleşme
  المكاتب العبد يكاتبه سيده على نفسه (maqayis)؛ المكاتب الذي يشتري نفسه ويكاتب عليها (jamhara)؛ المكاتب العبد يكاتب على نفسه بثمنه فإذا سعى وأداه عتق (sihah)؛ معنى الكتاب والمكاتبة أن يكاتب الرجل عبده أو أمته على مال ينجمه عليه (tahdhib)؛ كتابة العبد ابتياع نفسه من سيده بما يؤديه من كسبه (mufradat)

## ش ر ك (root_000791) — identity root of وَٱلْمُشْرِكِينَ (w8)

- **B001** ortaklık ve ortak olma — ortaklık ve ortak olma · ortak · ortak olmak veya birini ortak etmek · karşılıklı olarak ortaklaşmak · herkesin ortak olduğu veya eşit yararlandığı şey · ortaklık payı
  الشركة أن يكون الشيء بين اثنين لا ينفرد به أحدهما (maqayis)؛ الشركة مخالطة الشريكين (ayn;tahdhib)؛ شاركت فلانا صرت شريكه (sihah)؛ شركه في الأمر إذا دخل معه فيه (tahdhib)؛ خلط الملكين أو شيء لاثنين فصاعدا (mufradat)
- **B002** Tanrı'ya ortak koşma — Tanrı'ya ortak koşma · Tanrı'ya ortak koşmak · Tanrı'ya ortak koşan kimse · büyük ve küçük ortak koşma türleri
  الشرك ظلم عظيم (ayn)؛ الشرك أيضا الكفر (sihah)؛ أن تجعل لله شريكا في ربوبيته (tahdhib)؛ إثبات شريك لله تعالى (mufradat)
- **B003** eş veya evlilik yoluyla hısım — eş veya evlilik yoluyla hısım · sizinle evlilik yoluyla hısım olmak istedik
  في المصاهرة رغبنا في شرككم وصهركم (ayn;tahdhib)؛ فلان شريك فلان إذا تزوج بابنته أو بأخته (tahdhib)؛ امرأة الرجل شريكته (tahdhib)
- **B004** sandal kayışı ve sandala kayış takma — sandal kayışı · sandala kayış takmak
  شراك النعل مشبه بهذا (maqayis)؛ الشراك سير النعل (ayn;tahdhib)؛ أشركت نعلي جعلت لها شراكا (sihah)؛ شركت النعل وأشركتها إذا جعلت لها شراكا (tahdhib)
- **B005** yolun ana yatağı, izleri ve küçük kolları — yolun ana yatağı, ortası veya izleri · ana yoldan ayrılan küçük yollar · otlağın yollar veya izler halinde uzanması
  الشرك لقم الطريق وهو شراكه (maqayis)؛ الشرك أخاديد الطريق الواضح (ayn)؛ الشركة معظم الطريق ووسطه (sihah)؛ شرك الطريق أنساع الطريق (tahdhib)؛ أم الطريق معظمه وبنياته أشراك صغار (tahdhib)
- **B006** avın dolandığı kapan ve tuzak benzetmesi — avın dolandığı av kapanı · tek bir av kapanı · dünyanın tuzağı
  شرك الصائد سمي بذلك لامتداده (maqayis)؛ الشرك حبالة يرتبك فيها الصيد (ayn)؛ الشرك بالتحريك حبالة الصائد (sihah)؛ شرك الصائد حبالته يرتبك فيها الصيد (tahdhib)؛ شرك الدنيا أي حبالتها (mufradat)
- **B007** özel yapılarda hızlı ve art arda oluş — hızlı ve art arda tokatlar · suya birbiri ardından geliş
  لطمه لطما شركيا أي سريعا متتابعا (sihah)؛ لطمه لطما شركيا أي متتابعا (tahdhib)؛ ورد بعد ورد متتابع (sihah)
- **B008** kaygılı iç konuşma veya bölünmüş görüş — kaygılı biçimde kendi kendine konuşan · görüşü tek olmayan veya bölünmüş
  رأيت فلانا مشتركا إذا كان يحدث نفسه كالمهموم (sihah;tahdhib)؛ رأيه مشترك ليس بواحد (tahdhib)

## ف ك ك (root_001173) — identity root of مُنفَكِّينَ (w9)

- **B001** kapalıyı açıp iç içe geçmişi ayırma — kapalı şeyi açmak, kurtarmak veya serbest bırakmak · birbirine geçmiş iki şeyi ayırma · iki çeneyi birbirinden ayırmak
  أصل صحيح يدل على تفتح وانفراج (maqayis)؛ فككت الشيء فانفك ككتاب مختوم تفك خاتمه وكما تفك الحنكين تفصل بينهما (ayn;tahdhib)؛ فككت الشئ خلصته وكل مشتبكين فصلتهما فقد فككتهما (sihah)؛ الفكك التفريج (mufradat)؛ كل شيء أطلقته فقد فككته (tahdhib)
- **B002** rehni veya esaret altındakini bağından kurtarma — rehni bağlılığından kurtarmak · rehni çözme veya onu çözmek için verilen şey · rehni ya da tutsağı kurtarmaya yarayan şey · kölelikten özgürlüğüne kavuşturmak · ceylanın tuzağa düştükten sonra kurtulması
  فكاك الرهن وهو فتحه من الانغلاق (maqayis)؛ الفكاك الشيء الذي تفك به رهنا أو أسيرا وفككت رقبة فلان أعتقته (ayn)؛ فك الرهن وافتكه وفك الرقبة أي أعتقها (sihah)؛ فك الرقبة تخليصها من إسار الرق وفك الرهن وفكاكه تخليصه من غلق الرهن (tahdhib)؛ فك الرهن تخليصه وفك الرقبة عتقها (mufradat)؛ أفك الظبي من الحبالة إذا وقع فيه ثم انفلت (tahdhib)
- **B003** ayrılma; olumsuz yapıda sürüp gitme — bir şeyden ayrılmak veya uzaklaşmak · ayrılan, uzaklaşan veya sona erenler · yapmayı sürdürmek, bırakmamak
  لا ينفك يفعل ذلك بمعنى لا يزال (maqayis)؛ ما انفك فلان قائما أي ما زال قائما (sihah)؛ منفكين أي منتهين أو زائلين أو مفارقين (tahdhib)؛ منفكين أي لم يكونوا متفرقين وما انفك يفعل كذا نحو ما زال (mufradat)
- **B004** çene kemiği ve çenelerin birleşme bölgesi — çene kemiği · iki çene ve ağzın iki yanındaki birleşme bölgeleri · ağız-burun çıkıntısında iki çenenin birleştiği yer · yaşlılıktan çeneleri ayrılmış ihtiyar
  الفكان ملتقى الشدقين (maqayis;ayn;mufradat)؛ الفك اللحي (sihah)؛ انكسر أحد فكيه أي لحييه (tahdhib)؛ الأفك مجمع الخطم وهو مجمع الفكين (ayn;tahdhib)
- **B005** eklemin gevşeyip yerinden ayrılması — ayağı ekleminden ayrıldı · omuz ekleminin gevşeyip ayrılması veya ayağın çıkması · elini ekleminden çıkardım · omzu gevşeyip ekleminden ayrılmış kimse
  انفكت قدمه أي انفرجت (maqayis)؛ الفك انفراج المنكب عن مفصله ضعفا (maqayis)؛ الفكك انفراج المنكب عن مفصله ضعفا أو استرخاء (ayn)؛ انفكت قدمه أو إصبعه إذا انفرجت وزالت والفكك انفساخ القدم (sihah)؛ فككت يده فكا إذا أزال المفصل (tahdhib)؛ الفكك انفراج المنكب عن مفصله ضعفا (mufradat)
- **B006** düşünce ve davranışta gevşek, tutarsız aptallık — onda kadınsı sayılan bir gevşeklik var · düşünce veya tavırda gevşeklik ve aptallık · aptal · aptalca ve tutarsız davranmak · bilip bilmeden konuşan, yanlışı doğrusundan çok aptal
  في فلان فكك أي أناثة واستراخاء (ayn)؛ الفكة الحمق والاسترخاء وما كنت فاكا فأنت فاك تاك أي أحمق (sihah)؛ فلان فكة أي استرخاء في رأيه وأحمق فاك وهاك (tahdhib)
- **B007** hayvanda doğum, çiftleşme isteği veya zayıflığa bağlı çözülme [kalıp] — doğumu yaklaşmış, sağrı bağları gevşeyip memesi büyümüş dişi deve · çiftleşmeye istekli olup aygırı geri çevirmeyen kısrak · zayıflıktan bitkin dişi veya erkek deve
  ناقة متفككة إذا أقربت فاسترخى صلواها وعظم ضرعها ودنا نتاجها؛ ذهب بعضهم بتفكك الناقة إلى شدة ضبعتها؛ المتفككة من الخيل الوديق التي لا تمتنع على الفحل؛ الفاك المعيي هزالا ناقة فاكة وجمل فاك
- **B008** Yoksulların Tası denen yuvarlak yıldız kümesi — Yoksulların Tası denen yuvarlak yıldız kümesi
  الفكة النجوم المستديرة التي إلى جانب بنات نعش وهي قصعة المساكين (ayn)؛ الفكة كواكب مستديرة خلف السماك الرامح (sihah)؛ الفكة النجوم المستديرة التي يسميها الصبيان قصعة المساكين (tahdhib)
- **B009** çocuğun ağzına ilaç koyma [kalıp] — çocuğun ağzına ilaç koymak
  فككت الصبي جعلت الدواء في فيه

## ء ت ي (root_000009) — identity root of تَأْتِيَهُمُ (w11)

- **B001** gelmek, ulaşmak — gelmek veya ulaşmak · ona gitmek veya yanına varmak · geciktiğini düşünüp gelmesini istemek
  أتى يأتي أتيا (jamhara)؛ الإتيان المجئ (sihah)؛ أتاني فلان إتيانا وأتيا وأتية وأتوة (tahdhib;maqayis)؛ الإتيان مجيء بسهولة (mufradat)
- **B002** vermek; getirip sunmak — vermek; bir şeyi getirip sunmak
  آتى يؤتي إيتاء في معنى أعطى (jamhara)؛ آتاه إيتاء أي أعطاه وآتاه أيضا أي أتى به (sihah)؛ الإتياء الإعطاء (tahdhib)؛ الإيتاء الإعطاء (mufradat;maqayis)
- **B003** uygun yoldan ele almak ve elverişli hale gelmek — işin uygun yönü ve tutulacak yolu · uyma ve razı olma · bir şeyin ona elverişli hale gelmesi · ihtiyacını uygun yoldan ve incelikle yürütmek
  أتيت الأمر من مأتاته (sihah;maqayis)؛ آتيته على ذلك الأمر مواتاة إذا وافقته وطاوعته (sihah)؛ آتيت فلانا على أمره مؤاتاة وهو حسن المطاوعة (maqayis)؛ تأتى له الشيء أي تهيأ (sihah)؛ تأتى فلان لحاجته إذا ترفق لها (tahdhib)
- **B004** su kanalı açmak ve akışı yönlendirmek — su kanalı; suyu tutan odun ve yaprak birikintisi · bu suya yol açıp akışını yönlendirmek
  أت لمائك أي سهل له سبيلا وذلك السبيل الأتي (jamhara)؛ الأتي الجدول يؤتيه الرجل إلى أرضه (sihah)؛ كل جدول ماء أتي (tahdhib)؛ أت لهذا الماء أي سهل جريه (maqayis)؛ الأتي ما وقع في النهر من خشب أو ورق مما يحبس الماء (maqayis)
- **B005** başka bölgeden gelen sel [kalıp] — yağmur alan başka bir bölgeden gelen sel
  الأتي السيل بعينه يأتيك من بلد مطر من غير بلدك (jamhara)؛ سيل أتي وأتاوي إذا جاءك ولم يصبك مطره (sihah)؛ المسيل الذي يأتي من بلد قد مطر فيه إلى بلد لم يمطر فيه أتي (tahdhib)؛ السيل المار على وجهه أتي وأتاوي (mufradat)؛ الأتي أيضا السيل الذي يأتي من بلد غير بلدك (maqayis)
- **B006** topluluğa yabancı kimse [kalıp] — içinde bulunduğu topluluğa mensup olmayan yabancı adam
  رجل أتي وأتاوي وهو الغريب (jamhara)؛ الاتي أيضا والاتاوى الغريب (sihah)؛ إنما هو أتي فينا (tahdhib)؛ به شبه الغريب فقيل أتاوي (mufradat)؛ رجل أتي أي غريب في قوم ليس منهم وأتاوي كذلك (maqayis)
- **B007** gelişip bol ürün vermek — ekin ve hurmanın gelişmesi, ürünü ve bol verimi · çalkalanan tulumun yağının ortaya çıkması
  أتاء هذا النخل أي ثمره وكذلك الزرع (jamhara)؛ الاتاء البركة والنماء وحمل النخل (sihah)؛ جاء أتوه (sihah;mufradat)؛ إتاء النخلة ريعها وزكاؤها وكثرة ثمارها (tahdhib)؛ الإتاء نماء الزرع والنخل وأتى الماء إتاء أي كثر (maqayis)
- **B008** ödenen vergi; rüşvet — vergi veya baş vergisi; rüşvet · ona rüşvet vermek
  الإتاوة الخراج أو الجزية يؤديه القوم إلى الملك (jamhara)؛ الاتاوة الخراج والجمع الاتاوي (sihah)؛ الإتاوة الخراج وجمعها الأتاوى والإتاوات (tahdhib)؛ أتوته أتوة إذا رشوته إتاوة وهي الرشوة (tahdhib)
- **B009** devenin ön ayaklarını geri getirişi [kalıp] — devenin yürürken ön ayaklarını geri getirişi
  ما أحسن أتو قوائم الناقة وأتيها في السير (jamhara)؛ ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير (sihah)؛ ما أحسن أتو يديها وأتي يديها يعني رجع يديها (tahdhib)
- **B010** işlek ana yol, son sınır ve karşı hizası — yarışın son sınırı; işlek ana yol veya yol kavşağı · yarışın son sınırı veya yolun ana kesimi · bir evin karşısında veya aynı hizasında
  الميتاء والميداء آخر الغاية حيث ينتهي إليه جري الخيل (sihah)؛ الميتاء الطريق العامر ومجتمع الطريق (sihah)؛ داري بميتاء دار فلان وميداء دار فلان أي تلقاء داره ومحاذية لها (sihah)؛ طريق ميتاء مسلوك وميتاء الطريق وميداؤه محجته (tahdhib)
- **B011** felakete uğramak, kaybetmek veya düşmanca ele geçirilmek [kalıp] — ölüm, ağır hastalık, bela veya kırığa uğramak · malı yok olmak · uğruna öldürülmek, götürülmek veya yenilmek · düşman yaklaşmış olmak
  أتى على فلان أتو أي موت أو بلاء أصابه (tahdhib)؛ الأتو المرض الشديد أو كسر يد أو رجل أو موت (tahdhib)؛ أتي على يد فلان إذا هلك له مال (tahdhib)؛ يؤتى دونه أي يذهب به ويغلب عليه (tahdhib)؛ أتي فلان إذا أطل عليه العدو (tahdhib)؛ الإتيان يقال في الخير وفي الشر (mufradat)
- **B012** dişi devenin çiftleşmek istemesi [kalıp] — dişi devenin çiftleşmek için erkek deve istemesi
  استأتت الناقة استئتاء مهموز أي ضبعت وأرادت الفحل (sihah)
- **B013** etkili ve işini yürüten adam [kalıp] — etkili ve işini yürütebilen adam
  رجل أتي إذا كان نافذا (maqayis)

## ب ي ن (root_000170) — identity root of ٱلْبَيِّنَةُ (w12)

- **B001** ayrılıp kopma — ayrılık ve kopuş · ayrılmak, kopmak, kesilip ayrılmak · karşılıklı ayrılma ve uzaklaşma
  البين الفراق (maqayis;sihah)؛ البينونة مصدر بأن يبين بينا وبينونة أي قطع (ayn)؛ البين مصدر بان يبين بينا (jamhara)؛ بان كذا أي انفصل (mufradat)
- **B002** arada olma — iki veya daha çok şey arasındaki orta ve aralık · önünde, yanında veya yakınında · topluluğun içinden veya topluluğa dahil
  بين بمعنى وسط (sihah)؛ بين موضوع للخلالة بين الشيئين ووسطهما (mufradat)؛ لا يستعمل بين إلا فيما كان له مسافة أو له عدد ما اثنان فصاعدا (mufradat)
- **B003** arayı bağlayan ilişki — taraflar arasındaki bağ ve bağlantı · aranızdaki akrabalık, yakınlık ve sevgi durumları
  البين الوصل (ayn;sihah)؛ لقد تقطع بينكم أي وصلكم (mufradat)؛ ذات بينكم أي الأحوال التي تجمعكم من القرابة والوصلة والمودة (mufradat)
- **B004** açığa çıkıp belirginleşme — görünmek, açığa çıkmak, belirginleşmek · açık hale getirmek ve ortaya koymak · açık kanıt veya açık tanıklık · açık veya açıklayıcı işaretler
  بان الشيء وأبان إذا اتضح وانكشف (maqayis)؛ البيان معروف وبان الشيء وأبان وتبين وبين واستبان (ayn)؛ بان الشيء بيانا اتضح فهو بين (sihah)؛ البينة الدلالة الواضحة (mufradat)
- **B005** anlamı açıkça ortaya koyma — anlamı söz, yazı veya işaretle açıkça ortaya koyma · açık ve düzgün konuşan adam
  أبين من فلان أي أوضح كلاما منه (maqayis)؛ البين من الرجال الفصيح (ayn)؛ البيان الفصاحة واللسن (sihah)؛ البيان الكشف عن الشيء وهو أعم من النطق (mufradat)
- **B006** geniş uzaklık — ikisi arasında büyük uzaklık · dibi uzak veya geniş kuyu
  أصل واحد وهو بعد الشيء (maqayis)؛ البائنة البئر البعيدة القعر الواسعة (sihah)؛ بيون لبعد ما بين الشفير والقعر (mufradat)
- **B007** göz erimindeki arazi parçası — göz erimindeki arazi parçası, yöre veya kabarık yer
  البين قطعة من الأرض قدر مد البصر (maqayis)؛ البين الغلظ من الأرض (jamhara)؛ البين بالكسر القطعة من الأرض قدر منتهى البصر (sihah)؛ البين أيضا الناحية (sihah)
- **B008** bağlı yerinden ayrılma [kalıp] — devenin ayağının yanından açılması · teli gövdesinden uzak duran yay · başını gövdesinden kesip ayırmak
  بانت يد الناقة عن جنبها (ayn)؛ قوس بائن وهي التي بان وترها عن كبدها (ayn)؛ ضربه فأبان رأسه من جسده وفصله (sihah)؛ البائنة القوس التي بانت عن وترها كثيرا (sihah)
- **B009** sol yandan sağan kişi — sağımda hayvanın sol yanından gelen sağan
  البائن أحد الحالبين والآخر يسمى المستعلي (ayn)؛ البائن الذي يأتي الحلوبة من قبل شمالها والمعلى من قبل يمينها (sihah)
- **B010** o sırada — o sırada, bir şey olurken
  قولك بينا فلان معناه بينما (ayn)؛ بينا نحن نرقبه أتانا أي أتانا بين أوقات رقبتنا إياه (sihah)؛ يزاد في بين ما أو الألف فيجعل بمنزلة حين (mufradat)
- **B011** iki arada kalmış hal — iki uç arasında kalan orta veya zayıf hal
  هذا الشيء بين بين أي بين الجيد والرديء (sihah)؛ الهمزة المخففة تسمى بين بين (sihah)؛ يسقط بين بينا أي يتساقط ضعيفا غير معتد به (sihah)
- **B012** geri dönüşsüz boşanma [kalıp] — geri dönüş hakkını kesen boşanma
  تطليقة بائنة وهي فاعلة بمعنى مفعولة (sihah)
- **B013** ayrılık uğursuzu kuş [kalıp] — ayrılığı uğursuz biçimde haber verdiği sayılan kuş
  غراب البين يقال هو الأبقع (sihah)؛ غراب البين هو الأحمر المنقار والرجلين (sihah)؛ يحتم بالفراق (sihah)

===== _commentary/v16/out/s098/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 98:1, and ## Buluşmalar) =====
## Tuzak ve ondan sıyrılan av

Aşağıdaki imgelerin hepsi, kelimenin kendi ayetindeki anlamının yanında duyulur, o anlamın yerine geçmez: kök ailesinin taşıdığı sahne, ayetin söylediğini değiştirmez, ona arka plan verir.

Surenin ilk ayetinde iki kelime yan yana durur: {ar:وَٱلْمُشْرِكِينَ, tr:ve'l-müşrikîn, gloss:ve ortak koşanlar, source:98:1} ve {ar:مُنفَكِّينَ, tr:münfekkîn, gloss:ayrılıp çözülenler, source:98:1}. İlk kelimenin kökü avcının kurduğu ipi adlandırır: {ar:الشرك حبالة يرتبك فيها الصيد, tr:eş-şerek hibâletün yertebiku fîhe's-sayd, gloss:şerek, avın içinde dolanıp kaldığı tuzak ipidir, source:"ش ر ك,B006"}. İp yere serilir, hayvan adımını atar, bacağı ilmeğe girer, çırpındıkça düğüm sıkılaşır. İkinci kelimenin kökü bu sahnenin devamını verir: {ar:أفك الظبي من الحبالة إذا وقع فيه ثم انفلت, tr:efekke'z-zabyu mine'l-hibâle, gloss:ceylan tuzağa düştükten sonra kurtulup çıktı, source:"ف ك ك,B002"}. Ayet bu ikisini olumsuzlukla bağlar: {ar:لَمْ يَكُنِ, tr:lem yekün, gloss:değillerdi, source:98:1} ... münfekkîn {ar:حَتَّىٰ تَأْتِيَهُمُ ٱلْبَيِّنَةُ, tr:hattâ te'tiyehümü'l-beyyine, gloss:apaçık kanıt kendilerine gelinceye kadar, source:98:1}. Düz anlam "ayrılacak değillerdi"dir; arka planda ise ilmeğe takılmış bir hayvan, kendi çabasıyla çözülemeyen bir düğüm duyulur. Çözülme dışarıdan gelecek bir şeye, kanıtın gelişine bağlanmıştır.

Beşinci ayet aynı sahneyi başka bir kökle kapatır. Emredilen, {ar:مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:muhlisîne lehü'd-dîn, gloss:dini yalnız O'na has kılarak, source:98:5} olmaktır ve bu kökün somut kullanımı yine tuzaktır: {ar:تخلص الظبي والطائر من الحبالة إذا أفلت منها, tr:tehallasa'z-zabyu ve't-tâiru mine'l-hibâle, gloss:ceylan ve kuş tuzaktan sıyrılıp kurtuldu, source:"خ ل ص,B002"}; {ar:كان قد نشب ثم نجا وسلم, tr:kâne kad neşibe sümme necâ ve selim, gloss:takılıp kalmıştı, sonra kurtulup selamete çıktı, source:"خ ل ص,B002"}. Üç kök, şirk, infikâk ve ihlâs, aynı ip üzerinde buluşur: hibâle kelimesi üçünün açıklamasında da geçer. Böylece birinci ayetteki "çözülmeyen" ile beşinci ayetteki "sıyrılıp çıkan" aynı hayvanın iki hâli olarak duyulur. Altıncı ayet ise ilmekten çıkamayanların nerede kaldığını söyler: aynı {ar:وَٱلْمُشْرِكِينَ, tr:ve'l-müşrikîn, gloss:ve ortak koşanlar, source:98:6} bu kez ateştedir.

Beşinci ayette bir ters yüz de vardır. Kılınması emredilen {ar:ٱلصَّلَوٰةَ, tr:es-salât, gloss:namaz, source:98:5} kelimesinin kökü av için kurulan kapanı da adlandırır: {ar:المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد, tr:el-mıslâtü en tensibe şerekan, gloss:mıslât, bir şeyin düşüp avlanması için şerek benzeri bir tuzak kurmaktır, source:"ص ل و,B004"}. Bu tanım, şirkin kökünü ve salâtın kökünü tek cümlede birleştirir; ama surenin kendi sözünde salât tuzağa düşüren değil, tuzaktan sıyrılmış olanların fiilidir.

Kur'an bu sıyrılmayı bir kuş sahnesiyle de gösterir. Hacc suresinde Allah, {ar:حُنَفَآءَ لِلَّهِ غَيْرَ مُشْرِكِينَ بِهِۦ, tr:hunefâe lillâhi gayra müşrikîne bih, gloss:Allah'a yönelmiş hanifler olarak, O'na ortak koşmadan, source:22:31} dedikten hemen sonra ortak koşanı gökten düşen, kuşların kaptığı ya da rüzgârın uzak bir yere savurduğu biri olarak resmeder: {ar:فَتَخْطَفُهُ ٱلطَّيْرُ, tr:fetahtafuhu't-tayr, gloss:kuşlar onu kapıverir, source:22:31}. Surenin beşinci ayetindeki hunefâ kelimesi orada da aynı yerde, şirkin karşısında durur. Tevbe suresinde ise müminlere müşrikler hakkında {ar:وَٱقْعُدُوا۟ لَهُمْ كُلَّ مَرْصَدٍۢ, tr:vak'udû lehüm külle marsad, gloss:her gözetleme yerinde onları bekleyin, source:9:5} denir; pusu kurulur, ardından serbest bırakma şartı gelir: {ar:فَإِن تَابُوا۟ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ فَخَلُّوا۟ سَبِيلَهُمْ, tr:fe-in tâbû ve ekâmu's-salâte ve âtevu'z-zekâte fe-hallû sebîlehüm, gloss:tövbe eder, namazı kılar, zekâtı verirlerse yollarını serbest bırakın, source:9:5}. Bırakılışı açan iki fiil, surenin beşinci ayetindeki iki fiilin aynısıdır. Zümer suresindeki temsil ise aynı karşıtlığı mülkiyet üzerinden kurar: {ar:رَجُلًۭا فِيهِ شُرَكَآءُ مُتَشَٰكِسُونَ وَرَجُلًۭا سَلَمًۭا لِّرَجُلٍ, tr:racülen fîhi şürekâu müteşâkisûne ve racülen selemen li-racül, gloss:birbiriyle çekişen ortakların elindeki bir adam ile yalnız bir adama ait olan bir adam, source:39:29}. Ortaklar arasında çekiştirilen ile tek sahibe teslim olan, ilmeğe dolanmış hayvan ile sıyrılıp kurtulmuş hayvanın insan dünyasındaki karşılığıdır.

Kaynaklar: 98:1 وَٱلْمُشْرِكِينَ ش ر ك B006; 98:6 وَٱلْمُشْرِكِينَ ش ر ك B006; 98:1 مُنفَكِّينَ ف ك ك B002; 98:5 مُخْلِصِينَ خ ل ص B002; 98:5 ٱلصَّلَوٰةَ ص ل و B004

## Mühürlü yazı: getirilir, açılır, okunur

Surenin belgeleri elle tutulur nesnelerdir. Kitap kelimesinin kökü bir şeyi bir şeye eklemek, dikmektir: {ar:أصل الكتب ضمك الشيء إلى الشيء, tr:aslü'l-ketbi dammüke'ş-şey'e ile'ş-şey', gloss:ketbin aslı bir şeyi bir şeye katıp birleştirmendir, source:"ك ت ب,B001"}; {ar:كتبت السقاء إذا خرزته, tr:ketebtü's-sikâe izâ harraztühû, gloss:su tulumunu diktim, source:"ك ت ب,B001"}. Yazı, harflerin deri parçaları gibi birbirine dikilmesidir: {ar:في التعارف ضم الحروف بعضها إلى بعض بالخط, tr:fi't-teâruf dammü'l-hurûf, gloss:yaygın kullanımda harfleri yazıyla birbirine katmak, source:"ك ت ب,B002"}. Sayfa kelimesi açılıp serilmiş bir yüzeydir: {ar:الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها, tr:es-suhuf vâhidetühâ sahîfe, gloss:suhuf, tekili sahîfe; üzerine yazılan beyaz deri ya da parşömen parçası, source:"ص ح ف,B002"}. Bu yapraklar iki kapak arasında toplanınca mushaf olur: {ar:جعل جامعا للصحف المكتوبة بين الدفتين, tr:cuile câmian li's-suhufi'l-mektûbe beyne'd-deffeteyn, gloss:yazılı yaprakları iki kapak arasında toplayan kılındı, source:"ص ح ف,B003"}.

İlk ayetteki münfekkîn kelimesinin kökü bu nesneye de uzanır: {ar:فككت الشيء فانفك ككتاب مختوم تفك خاتمه, tr:fekektü'ş-şey'e fenfekke ke-kitâbin mahtûmin tefükkü hâtemehû, gloss:şeyi çözdüm, o da çözüldü; mühürlü bir mektubun mührünü açman gibi, source:"ف ك ك,B001"}. Bu açıklama infikâkın köküyle kitabı tek cümlede birleştirir. Birinci ayetin düz anlamı ayrılmamaktır; arka planında ise kapalı bir mektup ve mührün henüz kırılmamış olması duyulur. Mühürü açacak olan şey ayetin sonunda gelir: {ar:ٱلْبَيِّنَةُ, tr:el-beyyine, gloss:apaçık kanıt, source:98:1}; kök anlamı {ar:البيان الكشف عن الشيء, tr:el-beyânü el-keşfü ani'ş-şey', gloss:beyan, bir şeyi açığa çıkarmaktır, source:"ب ي ن,B005"}.

İkinci ayet bu kanıtı bir taşıyıcı ve bir eylem olarak gösterir: {ar:رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ, tr:resûlün mina'llâhi yetlû suhufen mutahhera, gloss:Allah'tan, tertemiz sayfaları okuyan bir elçi, source:98:2}. Resûl hem taşınan söz hem taşıyandır: {ar:الرسول يقال للقول المتحمل وتارة لمتحمل القول, tr:er-resûlü yukâlü li'l-kavli'l-mütehammel, gloss:resûl, yüklenilen söze de sözü yüklenene de denir, source:"ر س ل,B002"}; aynı kök acele etmeden okumayı da adlandırır: {ar:على رسلك أي اتئد فيه وترسل في قراءته, tr:alâ rislik, gloss:yavaş ol, okuyuşunda ağır ve tane tane git, source:"ر س ل,B004"}. Tilâvet ise izlemektir: {ar:تلاوة القرآن لأنه يتبع آية بعد آية, tr:tilâvetü'l-Kur'ân li-ennehû yetbau âyeten ba'de âye, gloss:Kur'an'ın tilâveti, ayetin ayeti izlemesindendir, source:"ت ل و,B002"}. Mühür açıldıktan sonra okuyan, satırları birbiri ardınca izler. Yapraklar {ar:مُّطَهَّرَةًۭ, tr:mutahhera, gloss:arındırılmış, source:98:2} olarak nitelenir: {ar:أصل واحد صحيح يدل على نقاء وزوال دنس, tr:aslün vâhidün yedüllü alâ nekâin ve zevâli denes, gloss:temizliğe ve kirin gitmesine delalet eden tek kök, source:"ط ه ر,B001"}; beyaz derinin üstünde leke yoktur. Üçüncü ayet açılan yaprakların içine bakar: {ar:فِيهَا كُتُبٌۭ قَيِّمَةٌۭ, tr:fîhâ kütübün kayyime, gloss:içlerinde dosdoğru yazılar vardır, source:98:3}; dikilip birleştirilmiş yazılar dimdik durur, {ar:قومت الشيء فهو قويم أي مستقيم, tr:kavvemtü'ş-şey'e fehüve kavîm, gloss:şeyi doğrulttum, o da düzgün, dosdoğru oldu, source:"ق و م,B008"}.

Dördüncü ayet aynı aktarımı alanların tarafından görür: {ar:ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ, tr:ellezîne ûtu'l-kitâb, gloss:kendilerine kitap verilenler, source:98:4}. Gelmek, getirmek ve vermek tek köktür: {ar:آتاه إيتاء أي أعطاه وآتاه أيضا أي أتى به, tr:âtâhu îtâen, gloss:ona verdi; ayrıca onu getirdi, source:"ء ت ي,B001"}. Birinci ayetteki ta'tiyehüm ("onlara gelinceye kadar") ile dördüncü ayetteki ûtû ("verildi") aynı hareketin iki ucudur; ayetin sonundaki {ar:جَآءَتْهُمُ ٱلْبَيِّنَةُ, tr:câet'hümü'l-beyyine, gloss:apaçık kanıt onlara geldi, source:98:4} de bu getirişi tekrarlar: {ar:جاء بكذا: استحضره, tr:câe bi-kezâ, gloss:onu getirip hazır etti, source:"ج ي ء,B004"}.

Kur'an bu nesneyi başka yerlerde de sahneler. Abese suresinde Allah zikri {ar:فِى صُحُفٍۢ مُّكَرَّمَةٍۢ, tr:fî suhufin mükerreme, gloss:değerli sayfalarda, source:80:13}, {ar:مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ, tr:merfûatin mutahhera, gloss:yüceltilmiş, arındırılmış, source:80:14}, {ar:بِأَيْدِى سَفَرَةٍۢ, tr:bi-eydî sefera, gloss:yazıcıların ellerinde, source:80:15} diye anlatır; surenin ikinci ayetinin en yakın eşidir ve yaprakları tutan elleri de gösterir. Tâhâ suresinde inkârcılar "Rabbinden bize bir ayet getirmeli değil miydi" deyince cevap verilir: {ar:أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:e-ve lem te'tihim beyyinetü mâ fi's-suhufi'l-ûlâ, gloss:önceki sayfalarda olanın apaçık kanıtı onlara gelmedi mi, source:20:133}; gelmek, beyyine ve suhuf bir arada. Müddessir suresinde inkârcıların her biri sayfaların kendisine açılmış olarak teslim edilmesini ister: {ar:أَن يُؤْتَىٰ صُحُفًۭا مُّنَشَّرَةًۭ, tr:en yü'tâ suhufen müneşşera, gloss:kendisine açılıp serilmiş sayfalar verilmesini, source:74:52}. A'lâ suresi bu sayfaları adlarıyla anar: {ar:صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ, tr:suhufi İbrâhîme ve Mûsâ, gloss:İbrahim'in ve Musa'nın sayfaları, source:87:19}. Tûr suresi serilmiş parşömen üzerine yazılmış bir kitaba yemin eder {source:52:3}, Tekvîr suresi ise kıyamette sayfaların açılmasını haber verir: {ar:وَإِذَا ٱلصُّحُفُ نُشِرَتْ, tr:ve ize's-suhufu nüşirat, gloss:sayfalar açılıp serildiğinde, source:81:10}. Vâkıa suresi örtülü bir kitaptan ve temizliğin şartından söz eder: {ar:فِى كِتَٰبٍۢ مَّكْنُونٍۢ, tr:fî kitâbin meknûn, gloss:korunmuş, örtülü bir kitapta, source:56:78}, {ar:لَّا يَمَسُّهُۥٓ إِلَّا ٱلْمُطَهَّرُونَ, tr:lâ yemessühû ille'l-mutahharûn, gloss:ona ancak arındırılmışlar dokunur, source:56:79}. Okuyan elçi formülü Cuma suresinde aynen geçer: {ar:رَسُولًۭا مِّنْهُمْ يَتْلُوا۟ عَلَيْهِمْ ءَايَٰتِهِۦ وَيُزَكِّيهِمْ, tr:resûlen minhüm yetlû aleyhim âyâtihî ve yüzekkîhim, gloss:içlerinden, onlara ayetlerini okuyan ve onları arındıran bir elçi, source:62:2}; Bakara suresinde İbrahim aynı elçiyi dua ile ister {source:2:129}. Ankebût suresi ise okuyuşu elle yazmaktan ayırır: {ar:وَمَا كُنتَ تَتْلُوا۟ مِن قَبْلِهِۦ مِن كِتَٰبٍۢ وَلَا تَخُطُّهُۥ بِيَمِينِكَ, tr:ve mâ künte tetlû min kablihî min kitâbin ve lâ tehuttuhû bi-yemînik, gloss:bundan önce bir kitap okumuyordun, onu sağ elinle de yazmıyordun, source:29:48}. Müzzemmil suresindeki emir, {ar:وَرَتِّلِ ٱلْقُرْءَانَ تَرْتِيلًا, tr:ve rattili'l-Kur'âne tertîlâ, gloss:Kur'an'ı tane tane oku, source:73:4}, resûl kökündeki ağır okuyuşun yanına konabilir.

Kaynaklar: 98:1 مُنفَكِّينَ ف ك ك B001; 98:1 ٱلْكِتَٰبِ ك ت ب B001; 98:3 كُتُبٌ ك ت ب B002; 98:2 صُحُفًا ص ح ف B002 B003; 98:2 مُّطَهَّرَةً ط ه ر B001; 98:3 قَيِّمَةٌ ق و م B008; 98:2 يَتْلُوا۟ ت ل و B002; 98:2 رَسُولٌ ر س ل B002 B004; 98:1 تَأْتِيَهُمُ ء ت ي B001; 98:4 أُوتُوا۟ ء ت ي B001; 98:4 جَآءَتْهُمُ ج ي ء B004; 98:1 ٱلْبَيِّنَةُ ب ي ن B005

## Sıra hâlinde atlar: önde giden, ardından gelen

Tilâvetin kökündeki izleme, Arapçada bir yarış alanında da görülür: {ar:جاءت الخيل تتاليا أي متتابعة, tr:câeti'l-haylü tetâliyen, gloss:atlar birbiri ardınca geldi, source:"ت ل و,B001"}. Atlar ardışık bölükler hâlinde de gelir ve bu, resûl kökünün sözüdür: {ar:جاءت الخيل أرسالا قطيعا قطيعا, tr:câeti'l-haylü ersâlen, gloss:atlar bölük bölük geldi, source:"ر س ل,B005"}. Yarışta ikinci gelen atın adı ise namaz kelimesinin kökünden gelir: {ar:قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه, tr:kad sallâ ve câe musalliyen, gloss:ikinci geldi, çünkü başı önündeki atın sağrısını izliyordu, source:"ص ل و,B006"}; kısaca {ar:المصلى تالي السابق, tr:el-musallî tâli's-sâbık, gloss:musallî, öndekinin ardından gelendir, source:"ص ل و,B006"}. Burada tilâvetin kökü ile salâtın kökü tek cümlede birleşir: ikinci at başını birincinin sağrısına dayayarak onun izini sürer.

Bu sahne ikinci ayetteki {ar:يَتْلُوا۟, tr:yetlû, gloss:okuyor, source:98:2} kelimesine bir hareket verir: okuyuş, satırın satırı izlemesidir, tıpkı atın atı izlemesi gibi. Beşinci ayetteki {ar:وَيُقِيمُوا۟ ٱلصَّلَوٰةَ, tr:ve yükîmu's-salât, gloss:namazı kılsınlar, source:98:5} emri de arka planda bu izleme duygusunu taşır: önde gideni takip eden konum. Yarışın bir de bitiş çizgisi vardır ve bu ad gelmek kökündendir: {ar:الميتاء والميداء آخر الغاية حيث ينتهي إليه جري الخيل, tr:el-mîtâ' ve'l-mîdâ', gloss:mîtâ, atların koşusunun sona erdiği son hedef, source:"ء ت ي,B010"}. Bu tanım, birinci ayetteki ta'tiyehüm ile sekizinci ayetteki {ar:تَجْرِى, tr:tecrî, gloss:akar, source:98:8} kelimelerinin köklerini tek cümlede toplar; koşu fiilinin kendisi de atlar için kullanılır: {ar:الخيل تجري والرياح تجري, tr:el-haylü tecrî, gloss:atlar koşar, rüzgârlar eser, source:"ج ر ي,B001"}. Surenin sekizinci ayetinde akan şey nehirlerdir; atların koşusu yalnızca kökün arka planında duyulur.

Kur'an elçilerin ardışıklığını aynı izleme diliyle anlatır: {ar:ثُمَّ أَرْسَلْنَا رُسُلَنَا تَتْرَا, tr:sümme erselnâ rusulenâ tetrâ, gloss:sonra elçilerimizi birbiri ardınca gönderdik, source:23:44}; aynı ayette {ar:فَأَتْبَعْنَا بَعْضَهُم بَعْضًۭا, tr:fe-etba'nâ ba'dahum ba'dâ, gloss:onların bir kısmını bir kısmının ardından getirdik, source:23:44}. Mürselât suresi ardışık gönderilenlere yemin ederek açılır {source:77:1}, Sâffât suresi de okuyanlara: {ar:فَٱلتَّٰلِيَٰتِ ذِكْرًا, tr:fe't-tâliyâti zikrâ, gloss:zikri okuyanlara andolsun, source:37:3}. Vâkıa suresi kıyamette insanları sınıflarken öne geçenleri ayrı anar: {ar:وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ, tr:ve's-sâbikûne's-sâbikûn, gloss:öne geçenler, öne geçenlerdir, source:56:10}.

Kaynaklar: 98:2 يَتْلُوا۟ ت ل و B001; 98:2 رَسُولٌ ر س ل B005; 98:5 ٱلصَّلَوٰةَ ص ل و B006; 98:1 تَأْتِيَهُمُ ء ت ي B010; 98:8 تَجْرِى ج ر ي B001

## Kenet açılır, taraflar ayrılır

Bir şey birbirine geçmiştir: iki çene, kenetlenmiş iki parça. Sonra açılır ve parçalar ayrı düşer. {ar:كل مشتبكين فصلتهما فقد فككتهما, tr:küllü müştebikeyni fasaltehümâ fekad fekektehümâ, gloss:birbirine geçmiş iki şeyi ayırdığında onları çözmüş olursun, source:"ف ك ك,B001"}. Olumsuz kullanıldığında aynı kök bir hâlin kesintisiz sürmesini anlatır: {ar:ما انفك فلان قائما أي ما زال قائما, tr:me'nfekke fülânün kâimen, gloss:filan ayakta durmaktan geri kalmadı, source:"ف ك ك,B003"}. Birinci ayetin lem yekün ... münfekkîn ifadesi bu ikinci anlamı taşır: bir topluluk kendi kenetinde, kendi hâlinde durmaktadır.

Ayetin son kelimesi beyyine, kökünde hem ayrılığı hem bağı barındırır: {ar:البين الفراق, tr:el-beynü el-firâk, gloss:beyn, ayrılıktır, source:"ب ي ن,B001"}; {ar:البين الوصل, tr:el-beynü el-vasl, gloss:beyn, bağdır, source:"ب ي ن,B003"}. Kanıt, bir yandan iki şeyin arasını açan, öbür yandan aradaki bağı gösteren şeydir. Dördüncü ayet bu açılmanın ardından ne olduğunu söyler: {ar:وَمَا تَفَرَّقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ, tr:ve mâ teferraka'llezîne ûtu'l-kitâb, gloss:kitap verilenler ayrılığa düşmedi, source:98:4}. Teferruk, iki şeyin arasının açılıp ayrı düşmesidir: {ar:الفرق تفريق بين شيئين حتى يفترقا ويتفرقا, tr:el-farku tefrîkun beyne şey'eyn, gloss:fark, iki şeyin arasını ayırmaktır, ta ki ayrılıp dağılsınlar, source:"ف ر ق,B001"}; sonucu ötekilerden kopmuş bir bölüktür: {ar:الفريق الجماعة المتفرقة عن آخرين, tr:el-ferîk, gloss:ferîk, ötekilerden ayrılmış topluluk, source:"ف ر ق,B005"}. Aynı kök hakla batılı ayıran şeyin de adıdır: {ar:كل ما فرق به بين الحق والباطل فهو فرقان, tr:küllü mâ furrika bihî beyne'l-hakkı ve'l-bâtıl fehüve furkân, gloss:hakla batılın arası neyle ayrılırsa o furkândır, source:"ف ر ق,B003"}. Ayetin keskinliği buradadır: ayırıcı olarak gelen beyyine, topluluğu hakla batıl arasında değil, kendi içinde bölmüştür. Ayrılık {ar:مِنۢ بَعْدِ, tr:min ba'di, gloss:-den sonra, source:98:4} olur; bu kelimenin kökü uzaklıktır: {ar:البعد خلاف القرب, tr:el-bu'du hilâfü'l-kurb, gloss:uzaklık yakınlığın karşıtıdır, source:"ب ع د,B001"}. "Sonra" kelimesinin arka planında açılan bir mesafe duyulur.

Beşinci ayetteki birlik çağrısının karşısında da bu kökler durur. Ya'budû kelimesinin kökünden gelen bir çoğul dağınık bölükleri adlandırır: {ar:العباديد الفرق من الناس الذاهبون في كل وجه, tr:el-abâbîd, gloss:abâbîd, her yöne dağılan insan bölükleri, source:"ع ب د,B010"}; ibadet tek bir yöne toplanmayı isterken bu kelime her yöne savrulmayı gösterir. Altıncı ve yedinci ayetteki berîye kelimesinin kökü karşılıklı ayrılmayı, ortakların birbirini serbest bırakmasını da anlatır: {ar:بارأت المرأة صاحبها على المفارقة وبارأت شريكي, tr:bâraeti'l-mer'etü sâhibehâ ... ve bâra'tü şerîkî, gloss:kadın eşiyle ayrılık üzere anlaştı; ortağımla karşılıklı helalleştim, source:"ب ر ء,B004"}. Bu cümlede berîyenin köküyle müşriklerin kökü yan yanadır. Şirkin kendisi ise iki kişi arasında bölünmeden tutulan ortak maldır: {ar:الشركة أن يكون الشيء بين اثنين لا ينفرد به أحدهما, tr:eş-şirketü en yekûne'ş-şey'ü beyne's-neyn, gloss:ortaklık, bir şeyin iki kişi arasında olması, birinin onu tek başına almamasıdır, source:"ش ر ك,B001"}.

Kur'an, surenin dördüncü ayetinin sözlerini başka yerlerde neredeyse aynen tekrarlar. Âl-i İmrân suresinde müminlere {ar:وَلَا تَكُونُوا۟ كَٱلَّذِينَ تَفَرَّقُوا۟ وَٱخْتَلَفُوا۟ مِنۢ بَعْدِ مَا جَآءَهُمُ ٱلْبَيِّنَٰتُ, tr:ve lâ tekûnû ke'llezîne teferrakû vahtelefû min ba'di mâ câehümü'l-beyyinât, gloss:apaçık kanıtlar geldikten sonra ayrılığa düşüp anlaşmazlığa girenler gibi olmayın, source:3:105} denir; sahne birkaç ayet önce tek bir ipe tutunmayla başlar: {ar:وَٱعْتَصِمُوا۟ بِحَبْلِ ٱللَّهِ جَمِيعًۭا وَلَا تَفَرَّقُوا۟, tr:va'tasımû bi-habli'llâhi cemîan ve lâ teferrakû, gloss:hep birlikte Allah'ın ipine sımsıkı tutunun, ayrılmayın, source:3:103}. Aynı surede ayrılığın sebebi de beyn kelimesiyle verilir: {ar:وَمَا ٱخْتَلَفَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ إِلَّا مِنۢ بَعْدِ مَا جَآءَهُمُ ٱلْعِلْمُ بَغْيًۢا بَيْنَهُمْ, tr:ve mehtelefe'llezîne ûtu'l-kitâbe illâ min ba'di mâ câehümü'l-ilmü bagyen beynehüm, gloss:kitap verilenler, kendilerine bilgi geldikten sonra, aralarındaki haddi aşma yüzünden ayrılığa düştüler, source:3:19}. Şûrâ suresinde Nuh'a, İbrahim'e, Musa'ya ve İsa'ya verilen din için {ar:أَنْ أَقِيمُوا۟ ٱلدِّينَ وَلَا تَتَفَرَّقُوا۟ فِيهِ ۚ كَبُرَ عَلَى ٱلْمُشْرِكِينَ, tr:en ekîmu'd-dîne ve lâ tetefarrakû fîh, kebüra ale'l-müşrikîn, gloss:dini ayakta tutun ve onda ayrılığa düşmeyin; bu, müşriklere ağır geldi, source:42:13} denir, hemen ardından {ar:وَمَا تَفَرَّقُوٓا۟ إِلَّا مِنۢ بَعْدِ مَا جَآءَهُمُ ٱلْعِلْمُ بَغْيًۢا بَيْنَهُمْ, tr:ve mâ teferrakû illâ min ba'di mâ câehümü'l-ilm, gloss:onlar ancak bilgi geldikten sonra, aralarındaki haddi aşmadan dolayı ayrıldılar, source:42:14} gelir. Surenin beşinci ayetindeki yükîmû, dîn ve müşrikîn kelimeleri burada bir aradadır. Bakara suresi ayrılmadan önceki birliği de söyler: {ar:كَانَ ٱلنَّاسُ أُمَّةًۭ وَٰحِدَةًۭ, tr:kâne'n-nâsü ümmeten vâhide, gloss:insanlar tek bir ümmetti, source:2:213}. Rûm suresinde Peygamber'e ve müminlere {ar:مِنَ ٱلَّذِينَ فَرَّقُوا۟ دِينَهُمْ وَكَانُوا۟ شِيَعًۭا, tr:mine'llezîne ferrakû dînehüm ve kânû şiyeâ, gloss:dinlerini parçalayıp bölük bölük olanlardan, source:30:32} olmamaları söylenir; En'âm suresi aynı kişileri anar {source:6:159}. Kıyamet sahnesinde ortak koşulanlar için söylenen söz bağın kopuşudur: {ar:لَقَد تَّقَطَّعَ بَيْنَكُمْ, tr:lekad tekatta'a beynekum, gloss:aranızdaki bağ kesilip koptu, source:6:94}. Karşısında kopmayan bir tutamak durur: {ar:فَقَدِ ٱسْتَمْسَكَ بِٱلْعُرْوَةِ ٱلْوُثْقَىٰ لَا ٱنفِصَامَ لَهَا, tr:fekadi'stemseke bi'l-urveti'l-vüskâ le'nfisâme lehâ, gloss:kopması olmayan en sağlam kulpa tutunmuştur, source:2:256}.

Kaynaklar: 98:1 مُنفَكِّينَ ف ك ك B001 B003; 98:1 ٱلْبَيِّنَةُ ب ي ن B001 B003; 98:4 تَفَرَّقَ ف ر ق B001 B003 B005; 98:4 بَعْدِ ب ع د B001; 98:5 لِيَعْبُدُوا۟ ع ب د B010; 98:6 ٱلْبَرِيَّةِ ب ر ء B004; 98:1 وَٱلْمُشْرِكِينَ ش ر ك B001

## Yol ve binek: çiğnenmiş yol, işaret taşı, çatal, yumuşatılmış deve

Dördüncü ve beşinci ayetlerin birçok kelimesi bir güzergâhın parçalarını adlandırır. İbadet kelimesinin kökü çok yürünmekle düzleşmiş yoldur: {ar:الطريق المعبد وهو المسلوك المذلل, tr:et-tarîku'l-muabbed, gloss:muabbed yol, çok yürünmüş, ayak altında yumuşamış yoldur, source:"ع ب د,B005"}. Aynı kök, katranla sıvanıp uysallaştırılmış deveyi de adlandırır: {ar:البعير المعبد المهنوء بالقطران المذلل, tr:el-ba'îru'l-muabbed, gloss:katranla sıvanmış, yumuşatılmış deve, source:"ع ب د,B003"}; yol için de deve için de aynı kelime, müzellel, kullanılır. Kökün insana dönük anlamı da budur: {ar:العبودية إظهار التذلل والعبادة غاية التذلل, tr:el-ubûdiyyetü izhâru't-tezellül, gloss:kulluk boyun eğişi göstermek, ibadet boyun eğişin en ileri derecesidir, source:"ع ب د,B003"}. Din kelimesi de bu boyun eğişin bir türü olarak tanımlanır: {ar:جنس من الانقياد والذل, tr:cinsün mine'l-inkıyâdi ve'z-zül, gloss:bir tür itaat ve alçalış, source:"د ي ن,B001"}. Beşinci ayetin {ar:لِيَعْبُدُوا۟ ٱللَّهَ, tr:li-ya'budu'llâh, gloss:Allah'a kulluk etsinler diye, source:98:5} ifadesi arka planda hem çiğnenip düzleşen yolu hem dizgine uyan deveyi taşır.

Yolun üzerinde işaretler vardır. Emir kelimesinin kökü, çölde yolu gösteren küçük taş yığınlarını adlandırır: {ar:الأمر بالتحريك جمع أمرة وهي العلم الصغير من أعلام المفاوز من الحجارة, tr:el-emeru cem'u emera, gloss:emer, emara'nın çoğulu; çöllerdeki işaretlerden taştan küçük bir alamet, source:"ء م ر,B005"}. Ayetin {ar:وَمَآ أُمِرُوٓا۟, tr:ve mâ umirû, gloss:onlara emredilmedi, source:98:5} sözü, düz anlamında bir buyruktur; arka planında yolcunun gözünü diktiği taş işaretler duyulur. Yol bir noktada çatallanır: {ar:فرق له الطريق أي اتجه له طريقان, tr:feraka lehü't-tarîk, gloss:yol önünde ikiye ayrıldı, source:"ف ر ق,B006"}; dördüncü ayetteki teferruk bu çatal noktasında durur. Müşriklerin kökü yolun ana gövdesinden ayrılan küçük patikaları adlandırır: {ar:أم الطريق معظمه وبنياته أشراك صغار, tr:ümmü't-tarîki mu'zamuhû ve büneyyâtühû eşrâkün sıgâr, gloss:yolun anası ana gövdesidir, ondan ayrılan küçük yollar ise küçük şeraklardır, source:"ش ر ك,B005"}. Hanif kelimesi doğruya meyletmektir: {ar:الحنف ميل عن الضلال إلى الاستقامة, tr:el-hanefü meylün ani'd-dalâli ile'l-istikâme, gloss:hanef, sapkınlıktan doğruluğa meyletmektir, source:"ح ن ف,B003"}; {ar:حُنَفَآءَ, tr:hunefâ, gloss:hanifler olarak, source:98:5} yan patikadan dönüp ana yola sapanlardır. Ayetin sonu yolun kendisini adlandırır: {ar:وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ, tr:ve zâlike dînü'l-kayyime, gloss:işte dosdoğru din budur, source:98:5}; {ar:الاستقامة في الطريق الذي يكون على خط مستو, tr:el-istikâmetü fi't-tarîki'llezî yekûnü alâ hattin müstevin, gloss:istikamet, düz bir hat üzerindeki yolda olmaktır, source:"ق و م,B008"}. Beşinci ayet, yolun neredeyse bütün parçalarını tek cümlede toplar.

Altıncı ayetteki ateş kelimesinin kökü bile yolda bir işarettir: {ar:المنار: علم الطريق, tr:el-menâr alemü't-tarîk, gloss:menar, yolun işaretidir, source:"ن و ر,B005"}; insanlar yolu bulmak için ateş yakardı: {ar:كانوا ينورون في الجاهلية ليهتدى ويقتدى بها, tr:kânû yünevvirûn, gloss:yol bulunsun ve izlensin diye ateş yakarlardı, source:"ن و ر,B005"}. Surede ise ateş yolun sonunda düşülen yerdir. Yolun ters yönü sekizinci ayetteki bir kelimede saklıdır: {ar:عِندَ, tr:inde, gloss:yanında, source:98:8} kelimesinin kökü yoldan sapan deveyi ve dizgini çekip kaçanı anlatır: {ar:العاند البعير الذي يجور عن الطريق ويعدل عن القصد, tr:el-âniüd, gloss:yoldan sapıp hedeften dönen deve, source:"ع ن د,B002"}; {ar:استعند البعير إذا غلب قائده على الزمام, tr:ista'nede'l-ba'îr, gloss:deve dizginde yedeğindekine galip geldi, source:"ع ن د,B001"}. İnsana dönük anlamı bilerek reddetmektir: {ar:المعاندة أن يعرف الرجل الشيء ويأبى أن يقبله, tr:el-muâneda, gloss:inat, bir şeyi bilip kabul etmekten kaçınmaktır, source:"ع ن د,B001"}. Sekizinci ayetteki inde rabbihim varılan yerdir, sapma değil; ama kökün arka planı dördüncü ayetteki ayrılığa bir ad verir: kanıt geldikten, yol işaretlenip düzleştikten sonra dizgini çekip kaçmak.

Kur'an yolu bu parçalarla sahneler. En'âm suresindeki öğütte yol ve yan patikalar ve ayrı düşüş bir aradadır: {ar:وَأَنَّ هَٰذَا صِرَٰطِى مُسْتَقِيمًۭا فَٱتَّبِعُوهُ ۖ وَلَا تَتَّبِعُوا۟ ٱلسُّبُلَ فَتَفَرَّقَ بِكُمْ عَن سَبِيلِهِۦ, tr:ve enne hâzâ sırâtî müstakîmen fettebiûh, ve lâ tettebiu's-sübüle feteferraka biküm an sebîlih, gloss:bu benim dosdoğru yolumdur, ona uyun; başka yollara uymayın, sizi O'nun yolundan ayırıp dağıtır, source:6:153}. Aynı surede Peygamber'e şöyle demesi söylenir: {ar:هَدَىٰنِى رَبِّىٓ إِلَىٰ صِرَٰطٍۢ مُّسْتَقِيمٍۢ دِينًۭا قِيَمًۭا مِّلَّةَ إِبْرَٰهِيمَ حَنِيفًۭا ۚ وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ, tr:hedânî rabbî ilâ sırâtin müstakîmin dînen kıyemen millete İbrâhîme hanîfâ, ve mâ kâne mine'l-müşrikîn, gloss:Rabbim beni dosdoğru bir yola, dimdik bir dine, hanif İbrahim'in milletine iletti; o müşriklerden değildi, source:6:161}; yol, kayyim, hanif ve müşrik tek ayettedir. İbrahim'in kendi sözü de yön çevirmedir: {ar:إِنِّى وَجَّهْتُ وَجْهِىَ لِلَّذِى فَطَرَ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضَ حَنِيفًۭا, tr:innî veccehtü vechiye li'llezî fatara's-semâvâti ve'l-arda hanîfâ, gloss:ben yüzümü gökleri ve yeri yaratana hanif olarak çevirdim, source:6:79}. Âl-i İmrân ve Nahl sureleri İbrahim'i aynı karşıtlıkla anar: {ar:وَلَٰكِن كَانَ حَنِيفًۭا مُّسْلِمًۭا وَمَا كَانَ مِنَ ٱلْمُشْرِكِينَ, tr:ve lâkin kâne hanîfen müslimen ve mâ kâne mine'l-müşrikîn, gloss:o hanif bir müslümandı, müşriklerden değildi, source:3:67}; {source:16:120}. Rûm suresinde emir yüzü dine doğrultmaktır: {ar:فَأَقِمْ وَجْهَكَ لِلدِّينِ حَنِيفًۭا, tr:fe-ekım vecheke li'd-dîni hanîfâ, gloss:yüzünü hanif olarak dine doğrult, source:30:30}, ayet {ar:ذَٰلِكَ ٱلدِّينُ ٱلْقَيِّمُ, tr:zâlike'd-dînü'l-kayyim, gloss:dosdoğru din budur, source:30:30} diye biter. Nahl suresinde yolun doğrusu ve sapanı Allah'ın nimetleri arasında sayılır: {ar:وَعَلَى ٱللَّهِ قَصْدُ ٱلسَّبِيلِ وَمِنْهَا جَآئِرٌۭ, tr:ve ala'llâhi kasdü's-sebîli ve minhâ câir, gloss:yolun doğrusunu göstermek Allah'a aittir, yollardan sapan da vardır, source:16:9}; biraz sonra yol işaretleri anılır {source:16:16}. Gece yolculuğunda Musa bir ateş görür ve onda yol bulmayı umar: {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidü ale'n-nâri hüdâ, gloss:ya da ateşin başında bir yol gösteren bulurum, source:20:10}. Uysallaştırma da bir nimettir: Yâsîn suresinde hayvanlar için {ar:وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ, tr:ve zellelnâhâ lehüm fe-minhâ rakûbühüm, gloss:onları kendilerine boyun eğdirdik, bir kısmı binekleridir, source:36:72} denir; Mülk suresinde yer {ar:ذَلُولًۭا, tr:zelûlâ, gloss:boyun eğen, yürünmeye elverişli, source:67:15} kılınmıştır. Ters yüzü Kâf suresinde, cehenneme atılma emrindedir: {ar:أَلْقِيَا فِى جَهَنَّمَ كُلَّ كَفَّارٍ عَنِيدٍۢ, tr:elkıyâ fî cehenneme külle keffârin anîd, gloss:her inatçı nankörü cehenneme atın, source:50:24}; küfür ve inat kökleri bir arada. Tevbe suresi ise beşinci ayetin sözünü kitap ehli için tekrarlar: {ar:وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوٓا۟ إِلَٰهًۭا وَٰحِدًۭا, tr:ve mâ umirû illâ li-ya'budû ilâhen vâhidâ, gloss:onlara ancak tek bir ilaha kulluk etmeleri emredilmişti, source:9:31}.

Kaynaklar: 98:5 لِيَعْبُدُوا۟ ع ب د B003 B005; 98:5 ٱلدِّينَ د ي ن B001; 98:5 أُمِرُوٓا۟ ء م ر B005; 98:4 تَفَرَّقَ ف ر ق B006; 98:1 وَٱلْمُشْرِكِينَ ش ر ك B005; 98:5 حُنَفَآءَ ح ن ف B003; 98:5 ٱلْقَيِّمَةِ ق و م B008; 98:6 نَارِ ن و ر B005; 98:8 عِندَ ع ن د B001 B002

## Örten ve örtülen: tohum, su, bahçe

Surenin ilk eyleyenleri ve son mekânı aynı kök imgesini paylaşır: örtmek. Küfrün kökü {ar:كل شيء غطى شيئا فقد كفره, tr:küllü şey'in gattâ şey'en fekad keferahû, gloss:bir şeyi örten her şey onu kefr etmiştir, source:"ك ف ر,B001"} diye tanımlanır; inanç anlamı da buradan gelir: {ar:الكفر ضد الإيمان سمى لأنه تغطية الحق, tr:el-küfrü ziddü'l-îmân, gloss:küfür imanın karşıtıdır; hakkı örtmek olduğu için bu adı aldı, source:"ك ف ر,B003"}. Gece de bir örtücüdür: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylü kâfir, gloss:gece kâfirdir, çünkü karanlığıyla örter, source:"ك ف ر,B002"}. Cennet kelimesinin kökü de örtmektir ve aynı geceyi taşır: {ar:الجيم والنون أصل واحد وهو الستر والتستر, tr:el-cîm ve'n-nûn aslün vâhid, gloss:cim ve nun tek bir köktür, örtmek ve örtünmektir, source:"ج ن ن,B001"}; {ar:جن عليه الليل وأجنه الليل إذا أظلم حتى يستره بظلمته, tr:cenne aleyhi'l-leyl, gloss:gece onun üstüne karardı, karanlığıyla onu örttü, source:"ج ن ن,B002"}. Her iki kök kabri de adlandırır: {ar:الكفر أيضا القبر, tr:el-kefru eyden el-kabr, gloss:kefr kabir anlamına da gelir, source:"ك ف ر,B012"}; {ar:جننت الميت وأجننته أي واريته والجنن القبر, tr:cenentü'l-meyyit, gloss:ölüyü gömdüm; cenen kabirdir, source:"ج ن ن,B009"}.

Bu örtme bir tarlada somutlaşır. Küfrün kökü, tohumu toprakla örten çiftçiyi adlandırır: {ar:الكافر الزارع لأنه يغطي البذر بالتراب, tr:el-kâfiru ez-zâri', gloss:kâfir, ekincidir, çünkü tohumu toprakla örter, source:"ك ف ر,B008"}; hurma tomurcuğunu saran kını da: {ar:الكافور الطلع ووعاء طلع النخل, tr:el-kâfûr et-tal', gloss:kâfûr, hurmanın tomurcuğu ve onu saran kın, source:"ك ف ر,B010"}. Toprağa su getirilir: {ar:الأتي الجدول يؤتيه الرجل إلى أرضه, tr:el-etiyyü el-cedvel, gloss:etî, adamın toprağına getirdiği arktır, source:"ء ت ي,B004"}; bu, dördüncü ayetteki ûtû kelimesinin köküdür. Ekin büyür: {ar:زكا الزرع يزكو زكاء ازداد ونما, tr:zekâ'z-zer'u yezkû zekâen, gloss:ekin arttı ve büyüdü, source:"ز ك و,B001"}. Hurma ürün verir ve bu ürünün tanımı surenin iki kelimesini birden içerir: {ar:إتاء النخلة ريعها وزكاؤها وكثرة ثمارها, tr:itâu'n-nahleti rîuhâ ve zekâuhâ, gloss:hurmanın itâsı, getirisi, büyümesi ve meyvesinin bolluğudur, source:"ء ت ي,B007"}. Beşinci ayetteki {ar:وَيُؤْتُوا۟ ٱلزَّكَوٰةَ, tr:ve yü'tu'z-zekât, gloss:zekâtı versinler, source:98:5} sözü, düz anlamıyla bir vermedir; arka planında hurmanın büyüyüp ürününü vermesi duyulur. Emir kelimesinin kökü de artışı anlatır: {ar:الأمر النماء والبركة, tr:el-emeru en-nemâu ve'l-bereke, gloss:emer, büyüme ve bereket, source:"ء م ر,B004"}.

Sekizinci ayet bu ekimi tamamlar: {ar:جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ, tr:cennâtü adnin tecrî min tahtihe'l-enhâr, gloss:altlarından ırmaklar akan Adn cennetleri, source:98:8}. Cennet ağaçlarıyla toprağı örten bahçedir: {ar:كل بستان ذي شجر يستر بأشجاره الأرض, tr:küllü bustânin zî şecer, gloss:ağaçlarıyla toprağı örten her bahçe, source:"ج ن ن,B003"}; Araplar hurmalığa da cennet der: {ar:العرب تسمي النخيل جنة, tr:el-arabü tüsemmi'n-nahîle cenneten, gloss:Araplar hurma ağaçlarına cennet der, source:"ج ن ن,B003"}. Irmak toprağı yararak akar: {ar:سمي النهر لأنه ينهر الأرض أي يشقها, tr:sümmiye'n-nehru li-ennehû yenheru'l-ard, gloss:nehir, toprağı yardığı için bu adı aldı, source:"ن ه ر,B001"}. Su aşağıda, bahçe yukarıdadır. Rab kelimesinin kökü bitkiyi besleyen bulutu ve bir şeyi adım adım olgunluğa erdirmeyi de anlatır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb, gloss:rabâb buluttur, bitkiyi beslediği için bu adı aldı, source:"ر ب ب,B008"}; {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, gloss:terbiye, bir şeyi hâlden hâle olgunluk sınırına kadar geliştirmektir, source:"ر ب ب,B002"}. Ödülün kendisi de örtülüdür: {ar:الجنة… ثواب مستور عنهم اليوم, tr:el-cenne sevâbün mestûr, gloss:cennet, bugün onlardan örtülü olan karşılıktır, source:"ج ن ن,B004"}. Aynı ayetin son kelimesinin kökü ise kurumuş hurmayı da adlandırır: {ar:الخشو الحشف من التمر, tr:el-haşvü el-haşefü mine't-temr, gloss:haşv, hurmanın kurusu, işe yaramazı, source:"خ ش ي,B004"}; ayetin düz anlamı ise rabbinden korkmaktır.

Sure böylece örtenlerle açılır ve örtülü bahçeyle kapanır. Birinci ayetteki örtü hakkı gizler; sekizinci ayetteki örtü ödülü saklar ve gölge verir. Arka planda tohumu örten çiftçi ile ağaçlarıyla toprağı örten bahçe arasında bir süreç duyulur: örtülen tohum, getirilen su, büyüyen ekin, ürün veren hurma ve altından ırmak akan bahçe.

Kur'an bu imgeleri başka yerlerde açıkça sahneler. Hadîd suresinde dünya hayatının temsilinde {ar:كَمَثَلِ غَيْثٍ أَعْجَبَ ٱلْكُفَّارَ نَبَاتُهُۥ, tr:ke-meseli gaysin a'cebe'l-küffâra nebâtüh, gloss:bitkisi ekincileri hayran bırakan bir yağmur gibi, source:57:20} denir; burada küffâr ekincilerdir ve ekin sonra sararıp çer çöp olur. Fetih suresinde ekin {ar:يُعْجِبُ ٱلزُّرَّاعَ لِيَغِيظَ بِهِمُ ٱلْكُفَّارَ, tr:yu'cibü'z-zürrâa li-yağîza bihimü'l-küffâr, gloss:ekincileri hayran bırakır, onlarla kâfirleri öfkelendirir, source:48:29}; ayet surenin yedinci ayetinin sözüyle biter: {ar:وَعَدَ ٱللَّهُ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ, tr:ve aded'llâhü'llezîne âmenû ve amilu's-sâlihât, gloss:Allah iman edip salih ameller işleyenlere vaat etti, source:48:29}. Kehf suresindeki iki adam temsilinde {ar:كِلْتَا ٱلْجَنَّتَيْنِ ءَاتَتْ أُكُلَهَا, tr:kilte'l-cenneteyni âtet ukülehâ, gloss:iki bahçe de ürününü verdi, source:18:33} denir, aynı ayette aralarından bir ırmak fışkırtılır; itâ fiili ürün için kullanılmıştır. Bakara suresinde infak edenlerin temsili de {ar:فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ, tr:fe-âtet ukülehâ dı'feyn, gloss:ürününü iki kat verdi, source:2:265} der; İbrâhîm suresinde güzel ağaç {ar:تُؤْتِىٓ أُكُلَهَا كُلَّ حِينٍۭ بِإِذْنِ رَبِّهَا, tr:tü'tî ukülehâ külle hînin bi-izni rabbihâ, gloss:Rabbinin izniyle her zaman ürününü verir, source:14:25}. Bakara suresinin bir başka temsili surenin bahçesini ve ateşini tek sahnede toplar: {ar:جَنَّةٌۭ مِّن نَّخِيلٍۢ وَأَعْنَابٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ, tr:cennetün min nahîlin ve a'nâbin tecrî min tahtihe'l-enhâr, gloss:altından ırmaklar akan hurma ve üzüm bahçesi, source:2:266}, sonra {ar:فَأَصَابَهَآ إِعْصَارٌۭ فِيهِ نَارٌۭ فَٱحْتَرَقَتْ, tr:fe-esâbehâ i'sârun fîhi nârun fahtarakat, gloss:ona içinde ateş bulunan bir kasırga isabet etti ve yandı, source:2:266}. Tâhâ suresinde Firavun'un iman eden sihirbazları, surenin sekizinci ayetini zekâtın köküne bağlayan sözü söyler: {ar:جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَا ۚ وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:cennâtü adnin tecrî min tahtihe'l-enhâru hâlidîne fîhâ, ve zâlike cezâu men tezekkâ, gloss:altlarından ırmaklar akan, içinde temelli kalacakları Adn cennetleri; bu, arınanın karşılığıdır, source:20:76}. Örtünün geceye bakan yüzü İbrahim'in gecesindedir: {ar:فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ رَءَا كَوْكَبًۭا, tr:felemmâ cenne aleyhi'l-leylü raâ kevkebâ, gloss:gece üstüne çöküp onu örtünce bir yıldız gördü, source:6:76}. Gizli ödül Secde suresinde de karşılık adıyla anılır: {ar:فَلَا تَعْلَمُ نَفْسٌۭ مَّآ أُخْفِىَ لَهُم مِّن قُرَّةِ أَعْيُنٍۢ جَزَآءًۢ بِمَا كَانُوا۟ يَعْمَلُونَ, tr:felâ ta'lemü nefsün mâ uhfiye lehüm min kurrati a'yün, cezâen bimâ kânû ya'melûn, gloss:yaptıklarına karşılık olarak onlar için gizlenmiş göz aydınlığını hiç kimse bilmez, source:32:17}. İnsan suresinde iyilerin içtiği kâfûr da aynı kökün bahçedeki yüzüdür: {ar:يَشْرَبُونَ مِن كَأْسٍۢ كَانَ مِزَاجُهَا كَافُورًا, tr:yeşrabûne min ke'sin kâne mizâcühâ kâfûrâ, gloss:katkısı kâfur olan bir kadehten içerler, source:76:5}.

Kaynaklar: 98:1 كَفَرُوا۟ ك ف ر B001 B002 B003 B008 B010 B012; 98:8 جَنَّٰتُ ج ن ن B001 B002 B003 B004 B009; 98:4 أُوتُوا۟ ء ت ي B004; 98:5 وَيُؤْتُوا۟ ء ت ي B007; 98:5 ٱلزَّكَوٰةَ ز ك و B001; 98:5 أُمِرُوٓا۟ ء م ر B004; 98:8 ٱلْأَنْهَٰرُ ن ه ر B001; 98:8 رَبِّهِمْ ر ب ب B002 B008; 98:8 خَشِىَ خ ش ي B004

## Yerinde kalmak ve ayrılmamak

Sure, süren bir hâlle açılır: lem yekün ... münfekkîn, "ayrılıp geri kalmıyorlardı". {ar:لا ينفك يفعل ذلك بمعنى لا يزال, tr:lâ yenfekkü yef'alü zâlik, gloss:onu yapmaktan geri kalmaz, yani yapmayı sürdürür, source:"ف ك ك,B003"}. Sure süren bir yurtla kapanır: {ar:جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ, tr:cezâühüm inde rabbihim cennâtü adn, gloss:Rableri katındaki karşılıkları Adn cennetleridir, source:98:8} ve {ar:خَٰلِدِينَ فِيهَآ أَبَدًۭا, tr:hâlidîne fîhâ ebedâ, gloss:orada ebedî olarak kalacaklar, source:98:8}. Sekizinci ayetin birçok kökü bir yerde kalıp ondan ayrılmamak için aynı kullanımı paylaşır. Hulûd sebat ve bağlılıktır: {ar:أصل واحد يدل على الثبات والملازمة, tr:aslün vâhidün yedüllü ale's-sebâti ve'l-mülâzeme, gloss:sabit kalmaya ve ayrılmamaya delalet eden tek kök, source:"خ ل د,B001"}; {ar:أخلد بالمكان أقام به, tr:ahlede bi'l-mekân, gloss:o yerde kaldı, source:"خ ل د,B002"}. Ebed için de aynısı söylenir: {ar:أبدت بالمكان إذا أقمت به ولم تبرحه, tr:ebedtü bi'l-mekân, gloss:o yerde kaldım ve ondan ayrılmadım, source:"ء ب د,B006"}. Rab kelimesinin kökü de: {ar:أرب فلان بالمكان إذا أقام به فلم يبرحه, tr:erabbe fülânün bi'l-mekân, gloss:filan o yerde kaldı ve ondan ayrılmadı, source:"ر ب ب,B007"}. Adn kelimesinin kökü için Arapçada {ar:عدن بالمكان أقام به, tr:adene bi'l-mekân, gloss:o yerde yerleşip kaldı, source:"memory"} denir; aynı kökten gelen {ar:المعدن, tr:el-ma'din, gloss:bir şeyin kaynağı, çıktığı yer, source:"memory"} kelimesi de vardır. Beşinci ayetteki yükîmû fiilinin aynı kalıbı bir yerde ikamet etmeyi anlatır: {ar:أقمت بالمكان إقامة ومقاما, tr:ekamtü bi'l-mekân, gloss:o yerde ikamet ettim, source:"ق و م,B006"}. İnde yakınlıktır: {ar:عند لفظ موضوع للقرب, tr:inde lafzun mevdûun li'l-kurb, gloss:inde yakınlık için konmuş bir sözdür, source:"ع ن د,B004"}. Birinci ayetteki ehl kelimesi ise içinde sahipleri bulunan evi ve "hoş geldin" sözünü taşır: {ar:منزل آهل أي به أهله, tr:menzilün âhil, gloss:içinde ahalisi olan ev, source:"ء ه ل,B004"}; {ar:مرحبا وأهلا أي أتيت سعة وأتيت أهلا فاستأنس ولا تستوحش, tr:merhaben ve ehlen, gloss:genişliğe ve aileye geldin, ısın, yabancılık çekme, source:"ء ه ل,B005"}.

Bu kökler surenin hareketini bir yerleşme olarak duyurur. Birinci ayette bir topluluk kendi hâlinde sürüp gider; dördüncü ayette ayrılır ve aralarına mesafe girer; altıncı ve sekizinci ayetlerde aynı hâlidîne fîhâ iki farklı yere bağlanır: ateş ve bahçe. Ebed kelimesinin kökü ters yüzü de taşır: {ar:تأبد المنزل أي أقفر وألفته الوحوش, tr:teebbede'l-menzil, gloss:konak ıssızlaştı, yabani hayvanlar ona alıştı, source:"ء ب د,B003"}; {ar:تأبد البعير توحش, tr:teebbede'l-ba'îr, gloss:deve yabanileşti, source:"ء ب د,B002"}. İçinde ahalisi olan ev ile yabani hayvanlara kalmış ıssız konak aynı kökün iki ucudur; sekizinci ayetteki ebedâ, ahalisi içinde, Rableri katında sürüp giden bir oturuşu söyler.

Kur'an bu yerleşmeyi başka yerlerde de anlatır. Kehf suresinde iman edip salih amel işleyenler için firdevs cennetleri bir konuk ağırlaması olarak hazırlanır {source:18:107} ve oradakiler {ar:خَٰلِدِينَ فِيهَا لَا يَبْغُونَ عَنْهَا حِوَلًۭا, tr:hâlidîne fîhâ lâ yebğûne anhâ hivelâ, gloss:orada temelli kalırlar, oradan ayrılmak istemezler, source:18:108}. Fâtır suresinde Adn cennetlerine girenler {source:35:33} şöyle der: {ar:ٱلَّذِىٓ أَحَلَّنَا دَارَ ٱلْمُقَامَةِ مِن فَضْلِهِۦ, tr:ellezî ehallenâ dâra'l-mukâmeti min fadlih, gloss:lütfuyla bizi kalınacak yurda yerleştiren, source:35:35}; mukâme, yükîmû fiilinin köküdür. Duhân suresinde takva sahipleri {ar:فِى مَقَامٍ أَمِينٍۢ, tr:fî makâmin emîn, gloss:güvenli bir makamdadır, source:44:51}; Kamer suresinde {ar:فِى مَقْعَدِ صِدْقٍ عِندَ مَلِيكٍۢ مُّقْتَدِرٍۭ, tr:fî mak'adi sıdkın inde melîkin muktedir, gloss:güçlü bir hükümdarın yanında doğruluk oturağında, source:54:55}. Tevbe suresinde Allah müminlere {ar:وَمَسَٰكِنَ طَيِّبَةًۭ فِى جَنَّٰتِ عَدْنٍۢ, tr:ve mesâkine tayyibeten fî cennâti adn, gloss:Adn cennetlerinde güzel meskenler, source:9:72} vaat eder. Kâf suresinde cennet yakına getirilir: {ar:وَأُزْلِفَتِ ٱلْجَنَّةُ لِلْمُتَّقِينَ غَيْرَ بَعِيدٍۢ, tr:ve ü'zlifeti'l-cennetü li'l-müttekîne gayra ba'îd, gloss:cennet takva sahiplerine yaklaştırılır, uzak değildir, source:50:31}; dördüncü ayetteki uzaklığın tersidir. Yanlış bir kalış da vardır: A'râf suresinde ayetlerden yüz çeviren adam için {ar:وَلَٰكِنَّهُۥٓ أَخْلَدَ إِلَى ٱلْأَرْضِ, tr:ve lâkinnehû ahlede ile'l-ard, gloss:ama o yere yapışıp kaldı, source:7:176} denir. Muhammed suresi ise iki kalışı karşı karşıya koyar: ırmaklı cennet {ar:كَمَنْ هُوَ خَٰلِدٌۭ فِى ٱلنَّارِ, tr:ke-men hüve hâlidün fi'n-nâr, gloss:ateşte temelli kalan kimse gibi midir, source:47:15}.

Kaynaklar: 98:1 مُنفَكِّينَ ف ك ك B003; 98:5 وَيُقِيمُوا۟ ق و م B006; 98:6 خَٰلِدِينَ خ ل د B001; 98:8 خَٰلِدِينَ خ ل د B001 B002; 98:8 أَبَدًا ء ب د B002 B003 B006; 98:8 رَبِّهِمْ ر ب ب B007; 98:8 عَدْنٍ (memory); 98:8 عِندَ ع ن د B004; 98:1 أَهْلِ ء ه ل B004 B005

## Hesap: borç, rehin, kefil, ödeme ve ibra

Din kelimesi itaattir; borç vermek ve almak da bu köktedir: {ar:الدين وداينت فلانا إذا عاملته دينا إما أخذا وإما إعطاء, tr:ed-deyn ve dâyentü fülânen, gloss:deyn; filanla alarak ya da vererek borç alışverişi yaptım, source:"د ي ن,B003"}; ve din karşılığın kendisidir: {ar:الدين الجزاء والمكافأة, tr:ed-dînü el-cezâü ve'l-mükâfee, gloss:din, karşılık ve bedeldir, source:"د ي ن,B002"}. Ceza da borcun ödenmesi ve tahsilidir: {ar:جزيت فلانا حقه؛ جزيته قرضه, tr:cezeytü fülânen hakkahû, gloss:filana hakkını ödedim; borcunu ödedim, source:"ج ز ي,B002"}; {ar:تجازيت ديني على فلان إذا تقاضيته, tr:tecâzeytü deynî alâ fülân, gloss:filandaki alacağımı tahsil ettim, source:"ج ز ي,B003"}. Bu son cümle ceza ile din köklerini birleştirir. Karşılığın ölçüsü de verilir: {ar:الجزاء ما فيه الكفاية من المقابلة إن خيرا فخير وإن شرا فشر, tr:el-cezâü mâ fîhi'l-kifâyetü mine'l-mukâbele, in hayran fe-hayr ve in şerran fe-şer, gloss:ceza, karşılıkta yeterli olandır: iyilikse iyilik, kötülükse kötülük, source:"ج ز ي,B001"}. Bu tanım altıncı ve yedinci ayetlerdeki şerr ve hayr kelimelerini sekizinci ayetteki {ar:جَزَآؤُهُمْ, tr:cezâühüm, gloss:karşılıkları, source:98:8} kelimesine bağlar.

Hesabın diğer parçaları surenin başka kelimelerinde durur. İnfikâkın kökü rehnin çözülmesidir: {ar:فك الرقبة تخليصها من إسار الرق وفك الرهن وفكاكه تخليصه من غلق الرهن, tr:fekkü'r-rakabeti tahlîsuhâ min isâri'r-rıkk ve fekkü'r-rehn, gloss:boynu çözmek onu kölelik bağından kurtarmak, rehni çözmek onu rehin kilidinden kurtarmaktır, source:"ف ك ك,B002"}; açıklamada kurtarmak için kullanılan tahlîs, muhlisîn kelimesinin köküdür. Berîye kelimesinin kökü borçtan aklanmaktır: {ar:برئت من الديون, tr:beri'tü mine'd-düyûn, gloss:borçlardan kurtuldum, source:"ب ر ء,B004"}. Tilâvetin kökü borcun kalanını ve alacağın devrini anlatır: {ar:التلية بقية الدين, tr:et-tuliyyetü bakıyyetü'd-deyn, gloss:tuliyye, borcun kalanıdır, source:"ت ل و,B003"}. Kitabın kökü, kölenin bedelini taksitle ödeyip özgürlüğünü satın aldığı sözleşmedir: {ar:المكاتب العبد يكاتب على نفسه بثمنه فإذا سعى وأداه عتق, tr:el-mükâteb, gloss:mükâteb, kendi bedeli üzerine yazılı anlaşma yapan köledir; çalışıp ödeyince özgür olur, source:"ك ت ب,B005"}. Kayyime bir şeyin biçilen değeridir: {ar:القيمة ثمن الشيء بالتقويم, tr:el-kıymetü semenü'ş-şey'i bi't-takvîm, gloss:kıymet, değer biçmeyle belirlenen bedel, source:"ق و م,B010"}. Surenin üç kelimesi kefili adlandırır: {ar:كنت على فلان أكون كونا أي تكفلت به, tr:küntü alâ fülân, gloss:filana kefil oldum, source:"ك و ن,B003"}; {ar:الجري الضامن, tr:el-cerî ed-dâmin, gloss:cerî, kefildir, source:"ج ر ي,B003"}; {ar:الرضي المطيع والرضي المحب والرضي الضامن, tr:er-radiyy, gloss:radî, itaat eden, seven ve kefil olandır, source:"ر ض و,B006"}.

Ödemenin ters yönü de vardır. Gelmek kökü haracı adlandırır ve ceza köküyle eşitlenir: {ar:الإتاوة الخراج أو الجزية يؤديه القوم إلى الملك, tr:el-itâve el-harâc evi'l-cizye, gloss:itâve, bir topluluğun hükümdara ödediği harac ya da cizye, source:"ء ت ي,B008"}. Cizye de üzerindekini ödemektir: {ar:الجزية … سميت جزية لأنها قضاء منه لما عليه, tr:el-cizye, gloss:cizye, üzerindeki borcu ödemesi olduğu için bu adı aldı, source:"ج ز ي,B004"}. Gönüllü verişin de bir adı vardır: {ar:إلا من أعطى في رسلها أي بطيب نفس منه, tr:illâ men a'tâ fî rislihâ, gloss:gönül hoşluğuyla veren hariç, source:"ر س ل,B010"}; hayr da hibe ve maldır: {ar:الخير الهبة, tr:el-hayru el-hibe, gloss:hayır, bağıştır, source:"خ ي ر,B005"}. Zekât, insanın Allah hakkı olarak fakirlere çıkardığıdır: {ar:ما يخرج الإنسان من حق الله تعالى إلى الفقراء, tr:mâ yuhricü'l-insânu min hakkı'llâh, gloss:insanın Allah hakkından fakirlere çıkardığı, source:"ز ك و,B003"}.

Bu kelimelerle sure bir hesap olarak duyulur. Dördüncü ayette kitap verilir; beşinci ayette verilenlerden din, yani borç bilinciyle sürdürülen bir itaat ve zekâtın verilmesi istenir; altıncı ve yedinci ayetlerde hayr ve şerr tartılır; sekizinci ayette ödeme yapılır ve hesap Rableri katında, {ar:عِندَ رَبِّهِمْ, tr:inde rabbihim, gloss:Rableri katında, source:98:8}, emanet gibi saklanır. Hesap karşılıklı bir hoşnutlukla kapanır: {ar:رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ, tr:radıya'llâhü anhüm ve radû anh, gloss:Allah onlardan razı olmuş, onlar da O'ndan razı olmuşlardır, source:98:8}; {ar:المراضاة من اثنين, tr:el-murâdâtü mine'sneyn, gloss:murâdât iki taraf arasında olur, source:"ر ض و,B003"}. Alışverişin sonunda iki tarafın birbirinden razı olması gibi.

Kur'an borcu, yazıyı ve ödemeyi açıkça birleştirir. Bakara suresinde müminlere {ar:إِذَا تَدَايَنتُم بِدَيْنٍ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى فَٱكْتُبُوهُ, tr:izâ tedâyentüm bi-deynin ilâ ecelin müsemmen fektübûh, gloss:belirli bir süreye kadar borçlandığınızda onu yazın, source:2:282} denir. Müddessir suresinde {ar:كُلُّ نَفْسٍۭ بِمَا كَسَبَتْ رَهِينَةٌ, tr:küllü nefsin bimâ kesebet rehîne, gloss:her can kazandığına karşılık rehindir, source:74:38}; Beled suresinde sarp yokuş {ar:فَكُّ رَقَبَةٍ, tr:fekkü rakabe, gloss:bir boyun çözmek, source:90:13} diye açıklanır. Nûr suresinde özgürlük sözleşmesi yazıyla ve vermeyle kurulur: {ar:فَكَاتِبُوهُمْ إِنْ عَلِمْتُمْ فِيهِمْ خَيْرًۭا ۖ وَءَاتُوهُم مِّن مَّالِ ٱللَّهِ ٱلَّذِىٓ ءَاتَىٰكُمْ, tr:fe-kâtibûhüm in alimtüm fîhim hayrâ, ve âtûhüm min mâli'llâhi'llezî âtâküm, gloss:onlarda bir hayır görürseniz onlarla yazılı anlaşma yapın ve Allah'ın size verdiği maldan onlara verin, source:24:33}. Tevbe suresinde Allah müminlerden canlarını ve mallarını satın alır: {ar:بِأَنَّ لَهُمُ ٱلْجَنَّةَ, tr:bi-enne lehümü'l-cenne, gloss:karşılığında cennet onlarındır, source:9:111}. Karşılığın denkliği Nebe' suresinde {ar:جَزَآءًۭ وِفَاقًا, tr:cezâen vifâkâ, gloss:tam denk bir karşılık, source:78:26}, Rahmân suresinde iyilik için söylenir {source:55:60}. Lokmân suresinde o gün kimse kimsenin borcunu ödeyemez: {ar:وَٱخْشَوْا۟ يَوْمًۭا لَّا يَجْزِى وَالِدٌ عَن وَلَدِهِۦ, tr:vahşev yevmen lâ yeczî vâlidün an veledih, gloss:babanın evladı yerine ödeme yapamayacağı günden korkun, source:31:33}; sekizinci ayetin son kelimesindeki haşyet burada da vardır. Fâtiha'daki {ar:مَٰلِكِ يَوْمِ ٱلدِّينِ, tr:mâliki yevmi'd-dîn, gloss:din gününün sahibi, source:1:4} ve Bakara suresindeki aynı uyarı {source:2:48} bu hesabın gününü adlandırır. Tevbe suresi müşriklere bir ibra ilanıyla açılır: {ar:بَرَآءَةٌۭ مِّنَ ٱللَّهِ وَرَسُولِهِۦٓ إِلَى ٱلَّذِينَ عَٰهَدتُّم مِّنَ ٱلْمُشْرِكِينَ, tr:berâetün mina'llâhi ve resûlihî ile'llezîne âhedtüm mine'l-müşrikîn, gloss:Allah'tan ve elçisinden, antlaşma yaptığınız müşriklere bir ilişik kesme, source:9:1}. Aynı surede kitap verilenlerin cizyesi {ar:حَتَّىٰ يُعْطُوا۟ ٱلْجِزْيَةَ عَن يَدٍۢ, tr:hattâ yu'tu'l-cizyete an yed, gloss:cizyeyi elden verinceye kadar, source:9:29} diye anılır; muhataplar surenin dördüncü ayetindeki ûtu'l-kitâb'dır. Gönüllü veriş de aynı surededir: sadakalar fakirlere, toplayıcılara, boyunların çözülmesine ve borçlulara verilir {source:9:60}; namazı kılıp zekâtı verenler ise {ar:فَإِخْوَٰنُكُمْ فِى ٱلدِّينِ, tr:fe-ihvânüküm fi'd-dîn, gloss:dinde kardeşlerinizdir, source:9:11}. Karşılıklı hoşnutluk Tevbe suresinde surenin sekizinci ayetinin sözleriyle tekrarlanır: {ar:رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ وَأَعَدَّ لَهُمْ جَنَّٰتٍۢ تَجْرِى تَحْتَهَا ٱلْأَنْهَٰرُ, tr:radıya'llâhü anhüm ve radû anhü ve eadde lehüm cennâtin tecrî tahtehe'l-enhâr, gloss:Allah onlardan razı olmuş, onlar da O'ndan razı olmuşlardır; onlara altlarından ırmaklar akan cennetler hazırlamıştır, source:9:100}; Mâide suresinde de Allah'ın kıyamet günü sözüyle {source:5:119}. Fecr suresinde huzura kavuşmuş cana {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdıyeten mardıyye, gloss:Rabbine razı edici ve razı olunmuş olarak dön, source:89:28} denir.

Kaynaklar: 98:5 ٱلدِّينَ د ي ن B002 B003; 98:8 جَزَآؤُهُمْ ج ز ي B001 B002 B003 B004; 98:1 مُنفَكِّينَ ف ك ك B002; 98:6 ٱلْبَرِيَّةِ ب ر ء B004; 98:2 يَتْلُوا۟ ت ل و B003; 98:1 ٱلْكِتَٰبِ ك ت ب B005; 98:5 ٱلْقَيِّمَةِ ق و م B010; 98:1 يَكُنِ ك و ن B003; 98:8 تَجْرِى ج ر ي B003; 98:8 رَّضِىَ ر ض و B003 B006; 98:5 وَيُؤْتُوا۟ ء ت ي B008; 98:2 رَسُولٌ ر س ل B010; 98:7 خَيْرُ خ ي ر B005; 98:5 ٱلزَّكَوٰةَ ز ك و B003

## Buluşmalar

En yoğun buluşma beşinci ayetteki salât kelimesindedir. Kökü bir yandan ateşte ısıtılıp düzeltilen çubuğu, {ar:صليت العود بالنار, tr:salleytü'l-ûde bi'n-nâr, gloss:çubuğu ateşte ısıtıp yumuşattım, source:"ص ل و,B001"}, öbür yandan ateşe girip yanan kâfiri, {ar:صلى الكافر نارا, tr:sale'l-kâfiru nârâ, gloss:kâfir ateşe girip yandı, source:"ص ل و,B001"}, adlandırır. Aynı ateş iki iş görür: eğri olanı doğrultur ya da yakar. Beşinci ayette ateş bir doğrultma aletidir; altıncı ayette inkâr edenlerin kaldığı yerdir. Doğrultma ile ocak sahneleri böylece tek bir kökün iki işlemi olarak birleşir ve surenin ikiye ayrılan yolunu taşır: kanıttan sonra doğrulup ayağa kalkanlar ve ateşte kalanlar. Aynı kök tuzağı da adlandırır; ama surede salât tuzaktan sıyrılmış olanların fiilidir.

Münfekkîn kelimesi üç sahneyi bir noktada tutar. Kökü tuzaktan kurtulan ceylanı, mührü açılan mektubu ve çözülen rehni anlatır. Birinci ayette bu kelime olumsuzdur: ip çözülmemiş, mühür açılmamış, rehin kurtarılmamıştır, ve bütün bunlar kanıtın gelişine bağlıdır. Rehnin çözülmesini anlatan cümlede infikâkın ve ihlâsın kökü yan yanadır, tuzaktan kurtulmayı anlatan cümlelerde de; bu yüzden birinci ayetteki çözülmeme ile beşinci ayetteki muhlisîn, hem avın hem borçlunun kurtuluşu olarak duyulur. Yazı ile kenet de aynı kelimede buluşur: mühürlü mektubun açılması ile iki çenenin ayrılması tek cümlede verilir ve dördüncü ayette açılan yazının ardından gelen ayrılık bunun devamıdır.

Teferruk kelimesi kenet ile yol sahnesini birleştirir. En'âm suresinde yan yollara uyunca insanların yoldan ayrı düşmesi {source:6:153}, hem çatallanan yolu hem bölünen topluluğu tek cümlede gösterir. Müşriklerin kökü ana yoldan ayrılan küçük patikaları adlandırdığı için dördüncü ayetteki ayrılık arka planda bir çatal noktasına, beşinci ayetteki hunefâ ise yan patikadan ana yola dönüşe dönüşür. Yol ile binek sahnesi müzellel kelimesinde birleşir: yürünmekle düzleşen yol ile katranla uysallaşan deve aynı kelimeyle anlatılır ve inde kelimesinin kökü ikisinin de tersini, yoldan sapan ve dizgini çeken deveyi verir. Doğrultma ile yol da kayyime kelimesinde birleşir: dik duran beden ile düz hat üzerindeki yol aynı kökle anlatılır; En'âm suresinde Peygamber'e söyletilen söz {source:6:161} yolu, kayyim olanı, hanifi ve müşrikleri tek ayette toplar.

Arındırma ile ekim zekâtta birleşir. Zekât hem bir temizliktir hem ekinin büyümesi ve hurmanın ürünüdür. Tâhâ suresinde surenin sekizinci ayetinin bahçesi tam olarak bu kelimeyle bağlanır: Adn cennetleri {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76}. Beşinci ayetteki zekât, sekizinci ayetteki bahçenin tohumu gibi durur. Arındırma ile hesap da hayr ve şerr kelimelerinde buluşur: süzmenin iki ürünü, karşılığın iki ölçüsüne dönüşür, iyiliğe iyilik ve kötülüğe kötülük.

Örtü ile ocak da kesişir: küfrün kökü üstü örtülmüş külü adlandırır. Örtü ile ekim ise aynı kelimede, tohumu örten çiftçide buluşur. Bakara suresindeki temsil {source:2:266} bu sahnelerin üçünü birden tutar: altından ırmaklar akan hurma bahçesi ve onu yakan ateşli kasırga. Altıncı ve sekizinci ayetler aynı sözü, hâlidîne fîhâ, ateş ve bahçe için kullanır; hulûdun kökü bir yandan ateşin içinde kalan ocak taşlarını, öbür yandan bir yerde yerleşip kalmayı adlandırır. Kalmanın iki yeri böylece aynı kelimede yan yana durur.

Bu buluşmalar surenin hareketini taşır. Birinci ayette bir şey kapalıdır: ilmek düğümlü, mühür kırılmamış, topluluk kendi hâlinde. Kanıt bir elçinin elinde, arındırılmış sayfalar olarak gelir ve okunur. Dördüncü ayette topluluk bu kanıtın ardından bölünür. Beşinci ayet çıkış yolunu tek cümlede verir: işaretli, düzleşmiş, dosdoğru bir yol; katkısından süzülmüş bir din; ateşte doğrultulan bir beden; tuzaktan sıyrılış; ürün veren bir ekin. Altıncı ve yedinci ayetler sonucu iki uca ayırır. Sekizinci ayet bir yerleşmeyle biter: Rableri katında, örtülü bir bahçede, ebedî bir kalış ve iki tarafın birbirinden razı olduğu kapanmış bir hesap.

