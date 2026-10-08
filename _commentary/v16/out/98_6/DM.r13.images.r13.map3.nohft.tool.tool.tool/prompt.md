Focus: 98:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/98_6/D.r13/context.md =====
# 98:6 — focus

إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ

Anchor translation (canonical reading, reference only):

Kuşkusuz Kitap ehlinden inkâr edenler ve Allah'a ortak koşanlar cehennem ateşindedirler; orada sürekli kalacaklardır. İşte onlar yaratılmışların en kötüleridir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | إِنَّ | إِنّ |  | ACC |
| 2 | ٱلَّذِينَ | ٱلَّذِى |  | REL |
| 3 | كَفَرُوا۟ | كَفَرَ | ك ف ر | V;PRON |
| 4 | مِنْ | مِن |  | P |
| 5 | أَهْلِ | أَهْل | ء ه ل | N |
| 6 | ٱلْكِتَٰبِ | كِتَٰب | ك ت ب | DET;N |
| 7 | وَٱلْمُشْرِكِينَ | مُشْرِك | ش ر ك | CONJ;DET;N |
| 8 | فِى | فِى |  | P |
| 9 | نَارِ | نَار | ن و ر | N |
| 10 | جَهَنَّمَ | جَهَنَّم |  | PN |
| 11 | خَٰلِدِينَ | خَٰلِد | خ ل د | N |
| 12 | فِيهَآ | فِى |  | P;PRON |
| 13 | أُو۟لَٰٓئِكَ | أُولَٰٓئِك |  | DEM |
| 14 | هُمْ |  |  | PRON |
| 15 | شَرُّ | شَرّ | ش ر ر | N |
| 16 | ٱلْبَرِيَّةِ | بَرِيَّة | ب ر ء | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 98 — full text (context; no pericope)

- 98:1 لَمْ يَكُنِ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ مُنفَكِّينَ حَتَّىٰ تَأْتِيَهُمُ ٱلْبَيِّنَةُ
- 98:2 رَسُولٌۭ مِّنَ ٱللَّهِ يَتْلُوا۟ صُحُفًۭا مُّطَهَّرَةًۭ
- 98:3 فِيهَا كُتُبٌۭ قَيِّمَةٌۭ
- 98:4 وَمَا تَفَرَّقَ ٱلَّذِينَ أُوتُوا۟ ٱلْكِتَٰبَ إِلَّا مِنۢ بَعْدِ مَا جَآءَتْهُمُ ٱلْبَيِّنَةُ
- 98:5 وَمَآ أُمِرُوٓا۟ إِلَّا لِيَعْبُدُوا۟ ٱللَّهَ مُخْلِصِينَ لَهُ ٱلدِّينَ حُنَفَآءَ وَيُقِيمُوا۟ ٱلصَّلَوٰةَ وَيُؤْتُوا۟ ٱلزَّكَوٰةَ ۚ وَذَٰلِكَ دِينُ ٱلْقَيِّمَةِ
- 98:6 ◀ focus إِنَّ ٱلَّذِينَ كَفَرُوا۟ مِنْ أَهْلِ ٱلْكِتَٰبِ وَٱلْمُشْرِكِينَ فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ ۚ أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ
- 98:7 إِنَّ ٱلَّذِينَ ءَامَنُوا۟ وَعَمِلُوا۟ ٱلصَّٰلِحَٰتِ أُو۟لَٰٓئِكَ هُمْ خَيْرُ ٱلْبَرِيَّةِ
- 98:8 جَزَآؤُهُمْ عِندَ رَبِّهِمْ جَنَّٰتُ عَدْنٍۢ تَجْرِى مِن تَحْتِهَا ٱلْأَنْهَٰرُ خَٰلِدِينَ فِيهَآ أَبَدًۭا ۖ رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ ۚ ذَٰلِكَ لِمَنْ خَشِىَ رَبَّهُۥ


===== _commentary/v16/work/98_6/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ك ف ر (root_001307) — identity root of كَفَرُوا۟ (w3)

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

## ء ه ل (root_000064) — identity root of أَهْلِ (w5)

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

## ك ت ب (root_001283) — identity root of ٱلْكِتَٰبِ (w6)

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

## ش ر ك (root_000791) — identity root of وَٱلْمُشْرِكِينَ (w7)

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

## ن و ر (root_001564) — identity root of نَارِ (w9)

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

## خ ل د (root_000429) — identity root of خَٰلِدِينَ (w11)

- **B001** kalıcı olma ve durumunu koruma — kalmak; varlığını sürdürmek · kalıcılık; bulunduğu durumda kalma · kalıcılık; kalıcı yaşam yurdu · sonsuz yaşam bahçesi · ölümden sonraki kalıcı yaşam yurdu · kalıcı kılmak; kalacağına hükmetmek · yaşlandığı halde saçına ak düşmeyen · ön kesici dişleri, yan kesici dişleri çıkana kadar düşmeyen hayvan · yıkıntılar yok olduktan sonra kalan ocak taşları ve kayalar
  أصل واحد يدل على الثبات والملازمة (maqayis)؛ الخلود البقاء فيها (ayn)؛ دوام البقاء (jamhara;sihah)؛ دار الخلود والخلد الآخرة والجنة (jamhara)؛ بقاؤه على الحالة التي هو عليها (mufradat)؛ مخلد إذا أبطأ عنه الشيب (maqayis;jamhara;sihah;mufradat)؛ خوالد للأثافي والحجارة لطول مكثها (ayn;sihah;mufradat)
- **B002** yönelip bağlanma, yapışma ya da ayrılmadan kalma [kalıp] — yere yapışmak veya ona bağlanmak · ona yönelmek ve ondan hoşnut olmak · o yerde kalmak · arkadaşının yanından ayrılmamak
  أخلد إلى الأرض إذا لصق بها (maqayis;jamhara)؛ أخلد إلى كذا أي ركن إليه ورضي به (ayn)؛ أخلدت إلى فلان أي ركنت إليه (sihah)؛ أخلد بالمكان أقام به وأخلد بصاحبه لزمه (sihah)؛ ركن إليها ظانا أنه يخلد فيها (mufradat)
- **B003** küpe; küpe veya bilezikle süslenmiş olma — küpe; bir tür kulak süsü
  ولدان مخلدون مقرطون (ayn;mufradat)؛ من الخلد والخلد جمع خلدة وهي القرط (maqayis)؛ مقرطون مشنفون (maqayis)؛ مسورون لغة يمانية (jamhara)
- **B004** akıl ve akla gelen düşünce — akıl; zihinde yer eden düşünce · aklıma geldi
  الخلد البال وسمي بذلك لأنه مستقر في القلب ثابت (maqayis)؛ ما يقع ذلك في خلدي (ayn)؛ وقع ذلك في خلدي أي في قلبي (jamhara)؛ وقع ذلك في خلدي أي في ورعي وقلبي (sihah)
- **B005** gözsüz faremsi küçük hayvan — gözleri olmayan, fareye veya sıçana benzeyen küçük hayvan
  الخلد ضرب من الجرذان عمي لم يخلق لها عيون (ayn)؛ الخلد دويبة تشبه الفأرة (jamhara)؛ ضرب من الجرذان أعمى (sihah)

## ش ر ر (root_000787) — identity root of شَرُّ (w15)

- **B001** iyinin karşıtı olan kötülük — kötülük; iyinin karşıtı · kötülük etme veya kötü olma durumu · kötülüğü çok olan adam · kötü kimseler · birini kötülüğe bağladı; onu kötü saydı · kusur veya hoş karşılanmayan şey
  الشَّرّ خلاف الخير (maqayis;jamhara)؛ الشر السوء (ayn)؛ الشر نقيض الخير (sihah)؛ الشر الذي يرغب عنه الكل (mufradat)؛ رجل شرير كثير الشر (maqayis;jamhara;sihah;mufradat)؛ أشررت فلانا إذا نسبته إلى الشر (maqayis;sihah;mufradat)؛ الشُّرّ العيب (sihah)؛ الشر بالضم خص بالمكروه (mufradat)
- **B002** güneşe serip kurutmak — güneşe serip kuruttu · güneşte kuruması için serdi · kurutulacak şeylerin serildiği yaygı · süt ürünü veya tahıl kurutma yaygısı · kurutma yaygıları veya kurutulmuş et parçaları
  الشر بسطك الشيء في الشمس (maqayis;ayn)؛ شررت اللحم والثوب وأشررته إذا بسطته ليجف (jamhara)؛ شررت الثوب بسطته في الشمس (sihah)؛ شررت الأقط أشره إذا جعلته على خصفة ليجف (sihah)؛ الإشرارة ما يبسط عليه الشيء (maqayis)؛ الإشرار ما يبسط عليه الأقط والبر ليجف (ayn)؛ الأشارير قطع قديد (sihah)
- **B003** kıvılcım — ateşten sıçrayan kıvılcımlar · kıvılcımlar topluluğu · tek kıvılcım · tek kıvılcım
  الشرارة والجمع الشرار (maqayis)؛ الشرر ما تطاير من النار الواحدة شررة (maqayis)؛ الشرارة والشرر ما تطاير من النار (ayn)؛ شرار النار فيقال شررة وشرارة (jamhara)؛ الشرارة واحدة الشرار وهو ما يتطاير من النار وكذلك الشرر (sihah)؛ شرار النار ما تطاير منها (mufradat)
- **B004** kesip parçalamak — bir şeyi kesip yardı · kesip parçalama; ısırılan şeyi ağızdan silkeleyip çıkarma
  شرشر الشيء إذا قطعه (maqayis)؛ الشرشرة أن تنفض الشيء من فيك بعد عضك إياه (maqayis)؛ شرشره أي قطع شراشره (ayn)؛ شرشرة الشيء تشقيقه وتقطيعه (sihah)
- **B005** yağı damlayan pişmiş et [kalıp] — yağı damlayan pişmiş et · yağı damlayan pişmiş et
  الشواء الشرشار الذي يتقاطر دسمه (maqayis)؛ شواء شرشر يتقاطر دسمه (sihah)
- **B006** kuyrukların sarkan uçları veya ağırlıklar — kuyrukların sarkan ve salınan uçları · ağırlıklar
  شراشر الأذناب ذباذبها (maqayis;sihah)؛ الشراشر الأثقال الواحدة شرشرة (sihah)
- **B007** kendini bütün isteğiyle vermek — kendini, isteğini ve bütün ilgisini ona verdi
  ألقى عليه شراشره إذا ألقى عليه نفسه حرصا ومحبة (maqayis)؛ ألقى علي شراشره أي ألقى علي نفسه حرصا (ayn)؛ ألقى عليه شراشره أي نفسه حرصا ومحبة (sihah)؛ جمع ما انتشر من هممه لهذا الشيء وشغل همومه كلها به (maqayis)
- **B008** görünür kılmak — 
  أشررت الشيء إذا أبرزته وأظهرته (maqayis)؛ أشررت الشيء أظهرته (sihah)؛ يحتمل أنها نسبت الأصابع إلى الشر بالإشارة إليه (mufradat)
- **B009** yüz çevresinde dolaşan ısırmayan sivrisinek benzeri böcek — yüz çevresinde dolaşan, ısırmayan sivrisinek benzeri böcekler · bu türden tek böcek
  الشران شيء تسميه العرب الأذى شبه البعوض يغشى وجه الإنسان لا يعض الواحدة شرانة (ayn)؛ الشران شبيه بالبعوض يغشى وجه الإنسان ولا يعض وربما سموه الأذى (sihah)
- **B010** gençlik canlılığı ve atılganlığı [kalıp] — gençliğin canlılığı, güçlü isteği ve atılganlığı
  شرة الشباب نشاطه ولهذا باب تراه (jamhara)؛ شرة الشباب حرصه ونشاطه (sihah)
- **B011** çekişme — çekişme; ağız dalaşı
  المشارة المخاصمة (sihah)
- **B012** adı belirtilen bir bitki — kaynakta adı verilen bir bitki
  الشرشر نبت يقال له الشرشر بالكسر (sihah)

## ب ر ء (root_000099) — identity root of ٱلْبَرِيَّةِ (w16)

- **B001** yaratıp var etme — Tanrı varlıkları yarattı ve ortaya çıkardı · yaratma anlamındaki ad · Tanrı için kullanılan yaratıcı nitelemesi · yaratılmış varlıklar topluluğu
  برأ الله الخلق يبرؤهم برءا (maqayis;ayn;sihah;tahdhib)؛ البارئ (maqayis;ayn;sihah;tahdhib;mufradat)؛ البرية الخلق (sihah;tahdhib;mufradat)
- **B002** ilişik kesip uzak durma — bir kimseden uzaklaşıp ilişiğini kesti · istenmeyen şeyden sakınıp uzak durdu · kusurdan ve istenmeyenden temiz olma · istenmeyen şeyden ayrılmış ve uzak duran · açık uyarı ve ilişik kesme bildirimi
  التباعد من الشيء ومزايلته (maqayis)؛ أصل البرء والبراء والتبري التقصي مما يكره مجاورته (mufradat)؛ برئت منك وبرئت من فلان وتبرأت (sihah;tahdhib;mufradat)؛ البراءة من العيب والمكروه (maqayis;ayn)؛ برآءة من الله ورسوله أي إعذار وإنذار (tahdhib)
- **B003** hastalıktan iyileşme — hastalıktan kurtulup iyileşti · hastalıktan kurtulup sağlığa dönme · hastalığından iyileşmiş · Tanrı hastalığını giderip iyileştirdi
  البرء السلامة من السقم (maqayis;ayn)؛ برأ من المرض برءا (jamhara;sihah;tahdhib)؛ أبرأه الله من مرضه إبراء (sihah;tahdhib)؛ برأت من المرض وبرئت من المرض (mufradat;tahdhib)
- **B004** hak veya borçtan salıverme — hakkımı sana bıraktım ve ondan çekildim · borç yükünden çıktı · kişiyi borç veya güvence yükünden salıverdi · onu üzerindeki haktan salıverdi · eş veya ortakla karşılıklı bağları çözerek ayrıldı
  برئت إليك من حقك (maqayis)؛ برئت من الديون (sihah)؛ أبرأت من الدين والضمان (maqayis;ayn)؛ أبرأته مما لي عليه وبرأته تبرئة (sihah)؛ بارأت المرأة صاحبها على المفارقة وبارأت شريكي (maqayis;sihah)؛ بارأت الرجل أي برئ إلي وبرئت إليه (ayn)
- **B005** boşluğu yoklayıp temizleme — boşluğu araştırıp güvenceye alma · satın alınan kadınla ilişki öncesi bekledi · elindeki şeyi yoklayıp arıttı · idrar sonrası organı temizleme
  الاستبراء أن يشتري الرجل جارية فلا يطأها حتى تحيض (maqayis;ayn)؛ استبرأت الجارية واستبرأت ما عندك (sihah)؛ الاستبراء إنقاء الذكر بعد البول (ayn)
- **B006** özel ay gecesi adı — ayın son gecesi için özel ad · ayın ilk gecesi için özel ad · istenmeyenden uzak sayılan uğurlu gün
  البراء آخر ليلة من الشهر (maqayis;tahdhib)؛ البراء أول ليلة من الشهر (sihah)؛ اليوم البراء السعد (maqayis)
- **B007** avcı gizlenme sığınağı — avcının gizlendiği sığınak veya örtülü yer · avcı gizlenme sığınakları
  برأة الصائد ناموسه وهي قترته والجمع برأ (maqayis)؛ البرأة بالهمز ناموس الصائد والجمع برأ (jamhara)؛ البرأة بالضم قترة الصائد والجمع برأ (sihah)

## ب ر ء (root_000100) — identity root of ٱلْبَرِيَّةِ (w16)

- **B001** yaratıp var etme — Tanrı varlıkları yarattı ve ortaya çıkardı · Tanrı için yaratıcı nitelemesi · yaratılmış varlıklar topluluğu
  برأ الله الخلق يبرؤهم برءا (maqayis;tahdhib)؛ البارئ الله جل ثناؤه (maqayis)؛ الله البارىء الذارىء (tahdhib)؛ البرية الخلق (tahdhib)
- **B002** ilişik kesip uzak durma — bir şeyden temiz, uzak ve kurtulmuş · muhataptan veya benimsenmeyen şeyden ilişik kesme bildirimi · açık uyarı ve ilişik kesme bildirimi · kusurdan ve istenmeyenden uzak olma
  التباعد من الشيء ومزايلته (maqayis)؛ البراءة من العيب والمكروه (maqayis)؛ برىء إذا تخلض وتنزه وتباعد (tahdhib)؛ برآءة من الله ورسوله أي إعذار وإنذار (tahdhib)؛ أنا براء منك (maqayis;tahdhib)
- **B003** hastalıktan iyileşme — hastalıktan kurtulup iyileşme · hastalıktan kurtulup iyileşti · Tanrı hastalığını giderip iyileştirdi
  البرء وهو السلامة من السقم (maqayis)؛ برئت وبرأت (maqayis)؛ برأت من المرض برءا وبرئت أبرأ برءا (tahdhib)؛ أبرأه الله من مرضه إبراء (tahdhib)
- **B004** hak bağını çözme [kalıp] — borç yükünden kurtuldu · hakkımı sana bırakıp ondan çekildim · borç ve güvence yükünü düşürdü · eşinden karşılıklı bağ çözerek ayrıldı
  برئت إليك من حقك (maqayis)؛ أبرأت من الدين والضمان (maqayis)؛ بارأت المرأة صاحبها على المفارقة وبارأت شريكي (maqayis)؛ برئت من الدين (tahdhib)؛ برئت إليك من فلان (tahdhib)
- **B005** ilişki öncesi boşluk yoklama — satın alınan kadınla ilişki öncesi bekleyip kuşkudan boşluğu sağlama
  الاستبراء أن يشتري الرجل جارية فلا يطأها حتى تحيض (maqayis)؛ برئت من الريبة التي تمنع المشتري من مباشرتها (maqayis)
- **B006** ayın son gecesi adı — ayın son gecesi için özel ad · istenmeyenden uzak sayılan uğurlu gün
  البراء آخر ليلة من الشهر (maqayis;tahdhib)؛ يبرأ فيها القمر من الشمس (tahdhib)؛ اليوم البراء السعد (maqayis)
- **B007** avcı gizlenme sığınağı — avcının gizlendiği sığınak veya örtülü yer · avcı gizlenme sığınakları
  برأة الصائد ناموسه وهي قترته والجمع برأ (maqayis)؛ قد زايل إليها كل أحد (maqayis)

## ECHO ش ر ي (root_000792) — for شَرُّ (w15): withheld observed target; not identity

- **B001** bedel karşılığında alıp satma — satmak veya bedelini verip almak · satın almak · alış ve satış
  شريت الشيء واشتريته إذا أخذته من صاحبه بثمنه (maqayis); شرى يشري شرى وشراء وهو شار إذا باع (ayn); شريت الشيء إذا بعته وإذا اشتريته أيضا (sihah); الشراء والبيع يتلازمان (mufradat); شريت بمعنى بعت وشريت أي اشتريت (tahdhib)
- **B002** eş ve denk — benzeri ve dengi · eş ve benzer
  هذا شروى هذا أي مثله (maqayis); شرواها أي مثلها (maqayis); شروى الشيء مثله (sihah); هذا شرواه وشرية أي مثله (tahdhib)
- **B003** bir şeyin yanları ve uçları [kalıp] — bir şeyin yanları ve uçları · büyük nehrin yanı
  أشراء الشيء نواحيه الواحد شرى (maqayis); أشراء الحرم نواحيه الواحد شرى (sihah); أشراء الحرم نواحيه وشرى الفرات ناحيته (tahdhib)
- **B004** acı elma bitkisi veya çekirdekten yetişen palmiye — acı elma bitkisi veya bu bitkinin topluluğu · çekirdekten yetişen palmiye ağacı
  الشَّرى يقال إنه الحنظل (maqayis); الشرية النخلة التي تنبت من النواة (maqayis); الشري بالتسكين الحنظل (sihah); الشرى أيضا شجر الحنظل (sihah); الحنظل هو الشري واحدته شرية (tahdhib)
- **B005** çalılık ve aslanlarıyla tanınan yer — çalılığı ve aslanı bol yer veya yol · çalılık bölgenin aslanları
  الشرى موضع كثير الدغل والأسد (maqayis); الشرى طريق في سلمى كثير الأسد (sihah); ما هم إلا أسود الشرى (tahdhib); شرى مأسدة بعينها وبه غياض وآجام (tahdhib)
- **B006** yaylık ağaç veya atardamar — yay yapımında kullanılan ağaç veya odun · atan veya ince beden damarları
  الشريان من شجر القسى (maqayis); الشريان شجر يتخذ منه القسى (sihah); الشريان واحد الشرايين وهي العروق النابضة (sihah); الشريان من الشجر الذي يتخذ منه القسي (tahdhib); الشريانات عروق رقاق في جسد الإنسان (tahdhib)
- **B007** şimşeğin yayılıp art arda parlaması [kalıp] — şimşek buluta yayıldı veya art arda parladı · şimşek art arda parladı
  شرى البرق إذا استطار (maqayis); شري البرق في السحاب يشرى شرى إذا تفرق فيه (ayn); شرى البرق إذا كثر لمعانه (sihah); شري البرق إذا تفرق في وجه الغيم (tahdhib); شري البرق إذا تتابع لمعانه واستشرى مثله (tahdhib)
- **B008** taşkın biçimde sürme, yinelenme veya büyüme — öfkesinden çılgına döndü · bir işte inatla diretti ve ileri gitti · karşılıklı inatlaşma ve çekişme · yolunda hızlandı veya durmadan ilerledi · dişi devenin dizgini durmadan çırpındı · gözyaşları durmadan aktı · aralarındaki işler büyüyüp ağırlaştı
  شرى الرجل إذا استطير غضبا (maqayis); شرى البعير في سيره إذا أسرع (maqayis); استشرى الرجل إذا لج في الأمر (maqayis); شرى زمام الناقة إذا كثر اضطرابه (maqayis); شري فلان غضبا إذا استطار غضبا (sihah); استشرى أي لج في سننه (sihah); استشرى فلان في الغي إذا لج فيه (tahdhib); المشاراة الملاجة (tahdhib); شريت عينه بالدمع أي لجت وتابعت الهملان (tahdhib); استشرت أمور بينهم تفاقمت وعظمت (tahdhib); أشريته به فشري مثل أغريته به فغري (tahdhib)
- **B009** yakıcı küçük kırmızı deri kabarcıkları — yakıcı küçük kırmızı deri kabarcıklarıyla görülen hastalık · derisinde yakıcı küçük kabarcıklar çıktı
  شري جلده من الشرى وهي خراج صغار لها لذع شديد (sihah); الشري داء يأخذ في الرجل أحمر كهيئة الدراهم (tahdhib); شرى جلده شرى وهو شر (tahdhib)
- **B010** havuzu veya yemek kabını doldurmak [kalıp] — havuzu veya büyük yemek kabını doldurmak
  أشريت الحوض وأشريت الجفنة إذا ملأتهما (sihah); أشرى حوضه ملأه وأشرى جفانه إذا ملأها للضيفان (tahdhib)
- **B011** kendini Tanrı uğruna sattığını söyleyen topluluk — kendilerini Tanrı uğruna sattıklarını söyleyen ayrılıkçı topluluk · bu topluluğun bir üyesi · bu topluluğa katılmak
  الشراة الخوارج الواحد شار سموا بذلك لقولهم إنا شرينا أنفسنا في طاعة الله (sihah); الشراة الخوارج سموا أنفسهم شراة لأنهم أرادوا أنهم باعوا أنفسهم لله (tahdhib); يسمى الخوارج بالشراة متأولين فيه ومن الناس من يشري نفسه (mufradat)
- **B012** Tanrı seni sıkıntıya ve aşağılanmaya uğratsın [kalıp] — Tanrı seni sıkıntıya ve aşağılanmaya uğratsın
  لحاه الله وشراه (tahdhib); شراه الله وعظاه وأورمه وأرغمه (tahdhib)

===== _commentary/v16/out/s098/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 98:6, and ## Buluşmalar) =====
## Tuzak ve ondan sıyrılan av

Aşağıdaki imgelerin hepsi, kelimenin kendi ayetindeki anlamının yanında duyulur, o anlamın yerine geçmez: kök ailesinin taşıdığı sahne, ayetin söylediğini değiştirmez, ona arka plan verir.

Surenin ilk ayetinde iki kelime yan yana durur: {ar:وَٱلْمُشْرِكِينَ, tr:ve'l-müşrikîn, gloss:ve ortak koşanlar, source:98:1} ve {ar:مُنفَكِّينَ, tr:münfekkîn, gloss:ayrılıp çözülenler, source:98:1}. İlk kelimenin kökü avcının kurduğu ipi adlandırır: {ar:الشرك حبالة يرتبك فيها الصيد, tr:eş-şerek hibâletün yertebiku fîhe's-sayd, gloss:şerek, avın içinde dolanıp kaldığı tuzak ipidir, source:"ش ر ك,B006"}. İp yere serilir, hayvan adımını atar, bacağı ilmeğe girer, çırpındıkça düğüm sıkılaşır. İkinci kelimenin kökü bu sahnenin devamını verir: {ar:أفك الظبي من الحبالة إذا وقع فيه ثم انفلت, tr:efekke'z-zabyu mine'l-hibâle, gloss:ceylan tuzağa düştükten sonra kurtulup çıktı, source:"ف ك ك,B002"}. Ayet bu ikisini olumsuzlukla bağlar: {ar:لَمْ يَكُنِ, tr:lem yekün, gloss:değillerdi, source:98:1} ... münfekkîn {ar:حَتَّىٰ تَأْتِيَهُمُ ٱلْبَيِّنَةُ, tr:hattâ te'tiyehümü'l-beyyine, gloss:apaçık kanıt kendilerine gelinceye kadar, source:98:1}. Düz anlam "ayrılacak değillerdi"dir; arka planda ise ilmeğe takılmış bir hayvan, kendi çabasıyla çözülemeyen bir düğüm duyulur. Çözülme dışarıdan gelecek bir şeye, kanıtın gelişine bağlanmıştır.

Beşinci ayet aynı sahneyi başka bir kökle kapatır. Emredilen, {ar:مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:muhlisîne lehü'd-dîn, gloss:dini yalnız O'na has kılarak, source:98:5} olmaktır ve bu kökün somut kullanımı yine tuzaktır: {ar:تخلص الظبي والطائر من الحبالة إذا أفلت منها, tr:tehallasa'z-zabyu ve't-tâiru mine'l-hibâle, gloss:ceylan ve kuş tuzaktan sıyrılıp kurtuldu, source:"خ ل ص,B002"}; {ar:كان قد نشب ثم نجا وسلم, tr:kâne kad neşibe sümme necâ ve selim, gloss:takılıp kalmıştı, sonra kurtulup selamete çıktı, source:"خ ل ص,B002"}. Üç kök, şirk, infikâk ve ihlâs, aynı ip üzerinde buluşur: hibâle kelimesi üçünün açıklamasında da geçer. Böylece birinci ayetteki "çözülmeyen" ile beşinci ayetteki "sıyrılıp çıkan" aynı hayvanın iki hâli olarak duyulur. Altıncı ayet ise ilmekten çıkamayanların nerede kaldığını söyler: aynı {ar:وَٱلْمُشْرِكِينَ, tr:ve'l-müşrikîn, gloss:ve ortak koşanlar, source:98:6} bu kez ateştedir.

Beşinci ayette bir ters yüz de vardır. Kılınması emredilen {ar:ٱلصَّلَوٰةَ, tr:es-salât, gloss:namaz, source:98:5} kelimesinin kökü av için kurulan kapanı da adlandırır: {ar:المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد, tr:el-mıslâtü en tensibe şerekan, gloss:mıslât, bir şeyin düşüp avlanması için şerek benzeri bir tuzak kurmaktır, source:"ص ل و,B004"}. Bu tanım, şirkin kökünü ve salâtın kökünü tek cümlede birleştirir; ama surenin kendi sözünde salât tuzağa düşüren değil, tuzaktan sıyrılmış olanların fiilidir.

Kur'an bu sıyrılmayı bir kuş sahnesiyle de gösterir. Hacc suresinde Allah, {ar:حُنَفَآءَ لِلَّهِ غَيْرَ مُشْرِكِينَ بِهِۦ, tr:hunefâe lillâhi gayra müşrikîne bih, gloss:Allah'a yönelmiş hanifler olarak, O'na ortak koşmadan, source:22:31} dedikten hemen sonra ortak koşanı gökten düşen, kuşların kaptığı ya da rüzgârın uzak bir yere savurduğu biri olarak resmeder: {ar:فَتَخْطَفُهُ ٱلطَّيْرُ, tr:fetahtafuhu't-tayr, gloss:kuşlar onu kapıverir, source:22:31}. Surenin beşinci ayetindeki hunefâ kelimesi orada da aynı yerde, şirkin karşısında durur. Tevbe suresinde ise müminlere müşrikler hakkında {ar:وَٱقْعُدُوا۟ لَهُمْ كُلَّ مَرْصَدٍۢ, tr:vak'udû lehüm külle marsad, gloss:her gözetleme yerinde onları bekleyin, source:9:5} denir; pusu kurulur, ardından serbest bırakma şartı gelir: {ar:فَإِن تَابُوا۟ وَأَقَامُوا۟ ٱلصَّلَوٰةَ وَءَاتَوُا۟ ٱلزَّكَوٰةَ فَخَلُّوا۟ سَبِيلَهُمْ, tr:fe-in tâbû ve ekâmu's-salâte ve âtevu'z-zekâte fe-hallû sebîlehüm, gloss:tövbe eder, namazı kılar, zekâtı verirlerse yollarını serbest bırakın, source:9:5}. Bırakılışı açan iki fiil, surenin beşinci ayetindeki iki fiilin aynısıdır. Zümer suresindeki temsil ise aynı karşıtlığı mülkiyet üzerinden kurar: {ar:رَجُلًۭا فِيهِ شُرَكَآءُ مُتَشَٰكِسُونَ وَرَجُلًۭا سَلَمًۭا لِّرَجُلٍ, tr:racülen fîhi şürekâu müteşâkisûne ve racülen selemen li-racül, gloss:birbiriyle çekişen ortakların elindeki bir adam ile yalnız bir adama ait olan bir adam, source:39:29}. Ortaklar arasında çekiştirilen ile tek sahibe teslim olan, ilmeğe dolanmış hayvan ile sıyrılıp kurtulmuş hayvanın insan dünyasındaki karşılığıdır.

Kaynaklar: 98:1 وَٱلْمُشْرِكِينَ ش ر ك B006; 98:6 وَٱلْمُشْرِكِينَ ش ر ك B006; 98:1 مُنفَكِّينَ ف ك ك B002; 98:5 مُخْلِصِينَ خ ل ص B002; 98:5 ٱلصَّلَوٰةَ ص ل و B004

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

## Ateş ve ocak

Altıncı ayet inkâr edenleri {ar:فِى نَارِ جَهَنَّمَ خَٰلِدِينَ فِيهَآ, tr:fî nâri cehenneme hâlidîne fîhâ, gloss:içinde temelli kalacakları cehennem ateşinde, source:98:6} diye yerleştirir. Ateş kelimesi, ışığın kıpırdayan, hızla oynayan hâlinden adını alır: {ar:النور والنار سميا بذلك من طريقة الإضاءة ولأن ذلك يكون مضطربا سريع الحركة, tr:en-nûr ve'n-nâr, gloss:nur ve nâr, aydınlatma yolundan ve bunun kıpırdayan, hızlı hareket eden bir şey olmasından bu adı aldı, source:"ن و ر,B001"}. Beşinci ayetteki salâtın kökü ateşin sıcağına katlanmayı adlandırır ve kendi örneği şudur: {ar:الصلا النار وصلى الكافر نارا, tr:es-salâ en-nâr ve sale'l-kâfiru nârâ, gloss:salâ ateştir; kâfir ateşe girip yandı, source:"ص ل و,B001"}. Bu tek cümle surenin üç kelimesini birleştirir: salâtın kökü, keferû kelimesinin kökü ve nâr. Aynı kök eti ateşte kızartmayı da anlatır: {ar:صليت اللحم شويته, tr:saleytü'l-lahme şeveytühû, gloss:eti ateşte kızarttım, source:"ص ل و,B001"}; mecazen bir işin sıcağını ve şiddetini çekmeyi de: {ar:صلي بالأمر إذا قاسى حره وشدته, tr:saliye bi'l-emr, gloss:işin sıcağına ve şiddetine katlandı, source:"ص ل و,B001"}.

Altıncı ayetin diğer kelimeleri ocağın parçalarını tamamlar. Şerr kelimesinin kökü ateşten sıçrayan kıvılcımdır: {ar:الشرر ما تطاير من النار, tr:eş-şerer mâ tetâyera mine'n-nâr, gloss:şerer, ateşten uçuşan şeydir, source:"ش ر ر,B003"}. Hâlidîn kelimesinin kökü ocak taşlarını adlandırır: {ar:خوالد للأثافي والحجارة لطول مكثها, tr:havâlid li'l-esâfî, gloss:ocak taşlarına ve kayalara uzun süre yerlerinde kaldıkları için havâlid denir, source:"خ ل د,B001"}. Konak bozulup göç edildikten sonra da ocak taşları yerinde, ateşin izinin ortasında kalır. Keferû kelimesinin kökü üstü örtülmüş külü de anlatır: {ar:كفرت الشيء أي سترته ورماد مكفور, tr:kefertü'ş-şey'e ey satartühû ve ramâdün mekfûr, gloss:şeyi örttüm; üstü örtülmüş kül, source:"ك ف ر,B001"}. Böylece altıncı ayet bir ocak olarak duyulabilir: ateş, sıçrayan kıvılcımlar, kızartma, ateşin içinde kalan taşlar ve örtülmüş kül. Ayetin düz söylediği ise bir cezadır: inkâr edenler {ar:أُو۟لَٰٓئِكَ هُمْ شَرُّ ٱلْبَرِيَّةِ, tr:ülâike hüm şerru'l-beriyye, gloss:onlar yaratılmışların en kötüsüdür, source:98:6}. Cehennem kelimesinin kendisi için Arapçada {ar:بئر جهنام, tr:bi'rün cihinnâm, gloss:dibi çok derin kuyu, source:"memory"} ifadesi anılır; bu, ateşe bir derinlik katar.

Kur'an bu ocağı açıkça sahneler. Nisâ suresinde Allah'ın sözü, salâtın kökünü, küfrü ve ateşi bir arada tutar: {ar:إِنَّ ٱلَّذِينَ كَفَرُوا۟ بِـَٔايَٰتِنَا سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا, tr:inne'llezîne keferû bi-âyâtinâ sevfe nuslîhim nârâ, küllemâ nadicet cülûdühüm beddelnâhüm cülûden gayrahâ, gloss:ayetlerimizi inkâr edenleri ateşe sokacağız; derileri piştikçe onları başka derilerle değiştireceğiz, source:4:56}. Kızartmanın fiili burada pişmek olarak açıkça söylenir. A'lâ suresinde {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasle'n-nâra'l-kübrâ, gloss:en büyük ateşe girecek olan, source:87:12}, Gâşiye suresinde o gün yüzler için {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4} denir; Müddessir suresinde de {ar:سَأُصْلِيهِ سَقَرَ, tr:se-uslîhi sekar, gloss:onu sekara sokacağım, source:74:26}. Mürselât suresi kıvılcımı gösterir: {ar:إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ, tr:innehâ termî bi-şererin ke'l-kasr, gloss:o, saray gibi kıvılcımlar atar, source:77:32}, {ar:كَأَنَّهُۥ جِمَٰلَتٌۭ صُفْرٌۭ, tr:keennehû cimâletün sufr, gloss:sanki sarı develer, source:77:33}. Vâkıa suresinde ise ateş çöl yolcularının ocağıdır: Allah inkârcılara yaktıkları ateşi sorar {source:56:71} ve onu {ar:تَذْكِرَةًۭ وَمَتَٰعًۭا لِّلْمُقْوِينَ, tr:tezkiraten ve metâan li'l-mukvîn, gloss:bir hatırlatma ve çölde konaklayanlar için bir fayda, source:56:73} kıldığını söyler.

Kaynaklar: 98:6 نَارِ ن و ر B001; 98:5 ٱلصَّلَوٰةَ ص ل و B001; 98:6 شَرُّ ش ر ر B003; 98:6 خَٰلِدِينَ خ ل د B001; 98:6 كَفَرُوا۟ ك ف ر B001; 98:6 جَهَنَّمَ (memory)

## Katkıyı ayıklamak: yıkamak, süzmek, saf olanı ayırmak

İkinci ayette sayfalar arındırılmıştır; beşinci ayette kulluk edenlerden muhlis olmaları ve zekât vermeleri istenir; altıncı ve yedinci ayetler yaratılmışları iki uca ayırır. Bu kelimelerin altında somut işlemler vardır. Tahâret suyla yıkanmaktır: {ar:تطهرت بالماء, tr:tetahhartü bi'l-mâ', gloss:suyla temizlendim, source:"ط ه ر,B003"}; su kendisi temizdir ve temizler: {ar:الطهور الطاهر في نفسه المطهر لغيره, tr:et-tahûr et-tâhiru fî nefsihî el-mutahhiru li-gayrih, gloss:tahûr, kendisi temiz olan ve başkasını temizleyendir, source:"ط ه ر,B004"}. İhlâsın kökü katkıdan arınmış olandır: {ar:الخالص هو ما زال عنه شوبه بعد أن كان فيه, tr:el-hâlisu mâ zâle anhü şevbühû ba'de en kâne fîh, gloss:hâlis, içindeki karışım giderilmiş olandır, source:"خ ل ص,B001"}. İşlemin kendisi tereyağını süzmektir: {ar:خلاصة السمن ما ألقي فيه من تمر أو سويق ليخلص به, tr:hulâsatü's-semn, gloss:yağın hulâsası, arınsın diye içine atılan hurma ya da kavrulmuş undur, source:"خ ل ص,B008"}; dipte kalan tortunun da adı vardır: {ar:الثفل الذي يكون أسفل هو الخلوص, tr:es-süfl ellezî yekûnü esfel, gloss:dipteki tortu, source:"خ ل ص,B008"}. Yağ kaynatılır, içine hurma ya da un atılır, karışım dibe çöker, üstteki berrak kısım alınır. Surenin kendi ifadesi bu işlemle açıklanır: {ar:أخلصت لله ديني أمحضته, tr:ahlastü li'llâhi dînî emhadtühû, gloss:dinimi Allah'a halis kıldım, onu katışıksız yaptım, source:"خ ل ص,B005"}. {ar:مُخْلِصِينَ لَهُ ٱلدِّينَ, tr:muhlisîne lehü'd-dîn, gloss:dini O'na has kılarak, source:98:5} sözünün arka planında, tortusundan ayrılmış berrak yağ duyulur.

Zekât da arınmadır: {ar:زكاة لأنها طهارة, tr:zekâtün li-ennehâ tahâra, gloss:zekâttır, çünkü bir temizliktir, source:"ز ك و,B002"}; bu tanım zekâtı ikinci ayetteki mutahhera kelimesinin köküne bağlar. Sayfaların lekeden arınması ile dinin karışımdan arınması aynı işlemin iki yüzüdür. Berîye kelimesinin kökü de kusurdan ve hastalıktan kurtulmayı anlatır: {ar:البراءة من العيب والمكروه, tr:el-berâetü mine'l-ayb, gloss:kusurdan ve hoşa gitmeyenden uzak olmak, source:"ب ر ء,B002"}; {ar:البرء السلامة من السقم, tr:el-bur'u es-selâmetü mine's-sekam, gloss:iyileşmek, hastalıktan kurtulmak, source:"ب ر ء,B003"}. Ayıklamanın iki ucu altıncı ve yedinci ayettedir. Hayr herkesin istediği, her şeyin seçkin kısmıdır: {ar:الخير ما يرغب فيه الكل وضده الشر, tr:el-hayru mâ yerğabu fîhi'l-küll, gloss:hayır, herkesin rağbet ettiği şeydir, karşıtı şerdir, source:"خ ي ر,B001"}; {ar:الخيرات جمع خيرة وهي الفاضلة من كل شيء, tr:el-hayrât, gloss:her şeyin en üstünü, source:"خ ي ر,B002"}. Şerr ise {ar:الشر الذي يرغب عنه الكل, tr:eş-şerru ellezî yerğabu anhü'l-küll, gloss:herkesin yüz çevirdiği şey, source:"ش ر ر,B001"}. {ar:شَرُّ ٱلْبَرِيَّةِ, tr:şerru'l-beriyye, gloss:yaratılmışların en kötüsü, source:98:6} ile {ar:خَيْرُ ٱلْبَرِيَّةِ, tr:hayru'l-beriyye, gloss:yaratılmışların en hayırlısı, source:98:7} böylece süzmenin iki ürünü olarak duyulur: alınıp saklanan berrak kısım ve dibe çöküp atılan tortu.

Kur'an bu işlemleri yan yana koyar. Tevbe suresinde Peygamber'e {ar:خُذْ مِنْ أَمْوَٰلِهِمْ صَدَقَةًۭ تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا وَصَلِّ عَلَيْهِمْ, tr:huz min emvâlihim sadakaten tutahhiruhüm ve tüzekkîhim bihâ ve salli aleyhim, gloss:mallarından onları temizleyip arındıracak bir sadaka al ve onlar için dua et, source:9:103} denir; tahâret, zekât ve salât tek ayettedir. Nahl suresinde hayvanlardan çıkan süt, halisin tortudan ayrılmasını gösterir: {ar:مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:min beyni fersin ve demin lebenen hâlisan sâiğan li'ş-şâribîn, gloss:işkembedeki artıkla kan arasından, içenlere kolayca geçen halis bir süt, source:16:66}. Zümer suresinde Peygamber'e verilen emir surenin beşinci ayetine çok yakındır: {ar:فَٱعْبُدِ ٱللَّهَ مُخْلِصًۭا لَّهُ ٱلدِّينَ, tr:fa'budi'llâhe muhlisan lehü'd-dîn, gloss:dini yalnız O'na has kılarak Allah'a kulluk et, source:39:2}; ardından {ar:أَلَا لِلَّهِ ٱلدِّينُ ٱلْخَالِصُ, tr:elâ li'llâhi'd-dînü'l-hâlis, gloss:iyi bilin ki halis din Allah'ındır, source:39:3}. Nisâ suresi tövbe edenleri {ar:وَأَخْلَصُوا۟ دِينَهُمْ لِلَّهِ, tr:ve ahlasû dînehüm li'llâh, gloss:dinlerini Allah'a halis kıldılar, source:4:146} diye anar. Leyl suresinde arınmak için malını veren {ar:ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ, tr:ellezî yü'tî mâlehû yetezekkâ, gloss:arınmak için malını veren, source:92:18} anılır; Furkân suresinde gökten indirilen su {ar:مَآءًۭ طَهُورًۭا, tr:mâen tahûrâ, gloss:tertemiz ve temizleyici bir su, source:25:48} olarak Allah'ın ayetleri arasında sayılır.

Kaynaklar: 98:2 مُّطَهَّرَةً ط ه ر B003 B004; 98:5 مُخْلِصِينَ خ ل ص B001 B005 B008; 98:5 ٱلزَّكَوٰةَ ز ك و B002; 98:6 ٱلْبَرِيَّةِ ب ر ء B002 B003; 98:7 خَيْرُ خ ي ر B001 B002; 98:6 شَرُّ ش ر ر B001

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

