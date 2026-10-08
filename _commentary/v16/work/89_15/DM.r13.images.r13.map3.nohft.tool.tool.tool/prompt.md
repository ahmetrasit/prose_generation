Focus: 89:15. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_15/D.r13/context.md =====
# 89:15 — focus

فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ

Anchor translation (canonical reading, reference only):

İnsana gelince, Rabbi onu sınayıp ona değer verdiğinde ve nimet sunduğunda, “Rabbim bana değer verdi” der.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَأَمَّا | أَمَّا |  | REM;EXL |
| 2 | ٱلْإِنسَٰنُ | إِنسَٰن | ء ن س | DET;N |
| 3 | إِذَا | إِذَا |  | T |
| 4 | مَا | مَا |  | SUP |
| 5 | ٱبْتَلَىٰهُ | ٱبْتَلَىٰٓ | ب ل و | V;PRON |
| 6 | رَبُّهُۥ | رَبّ | ر ب ب | N;PRON |
| 7 | فَأَكْرَمَهُۥ | أَكْرَمَ | ك ر م | CONJ;V;PRON |
| 8 | وَنَعَّمَهُۥ | نَعَّمَ | ن ع م | CONJ;V;PRON |
| 9 | فَيَقُولُ | قَالَ | ق و ل | RSLT;V |
| 10 | رَبِّىٓ | رَبّ | ر ب ب | N;PRON |
| 11 | أَكْرَمَنِ | أَكْرَمَ | ك ر م | V;PRON |


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
- 89:15 ◀ focus فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ
- 89:16 وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
- 89:17 كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ
- 89:18 وَلَا تَحَٰٓضُّونَ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
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


===== _commentary/v16/work/89_15/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء ن س (root_000059) — identity root of ٱلْإِنسَٰنُ (w2)

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

## ب ل و (root_000153) — identity root of ٱبْتَلَىٰهُ (w5)

- **B001** eskime ve yolculukta yıpranma — nesnenin ya da giysinin eskimesi ve yıpranması · eskime, yıpranma · yolculuğun yıprattığı binek · Güle güle eskit; Tanrı yerine yenisini versin
  بلي الشيء يبلى بلى فهو بال (ayn)؛ بلي الثوب يبلى بلى وبلاء (sihah;tahdhib;mufradat)؛ ناقة بلو سفر أبلاها السفر (ayn;sihah;tahdhib;mufradat)
- **B002** deneyerek sınama ve gerçek niteliği ortaya çıkarma — durumunu anlamak için denemek ve sınamak · bir insanı sınamak · iyilik veya güçlük yoluyla sınama · çetin sınama ve deneme · sınama
  بلي الإنسان وابتلي إذا امتحن (ayn)؛ بلوته بلوا جربته واختبرته (sihah)؛ بلاه يبلوه بلوا إذا جربه (tahdhib)؛ بلوته اختبرته وتبلوا كل نفس ما أسلفت أي تعرف حقيقة ما عملت (mufradat)
- **B003** iyilikte bulunma ve üstün çaba gösterme — ona iyilik etti · cömertlikte veya savaşta üstün çaba gösterdi · ona iyilik ettim
  والله يبلي العبد بلاء حسنا وبلاء سيئا (ayn)؛ أبلاه الله بلاء وأبلاه إبلاء حسنا وأبليته معروفا (sihah)؛ أبلاه الله يبليه إبلاء حسنا إذا صنع به صنيعا جميلا وأبلى فلان إذا اجتهد في صفة كرم أو حرب (tahdhib)؛ اختبار الله للعباد تارة بالمسار وتارة بالمضار وليبلي المؤمنين منه بلاء حسنا (mufradat)
- **B004** mazereti açıklama veya yeminle güven verme ya da sınama — ona mazeretimi açıklayıp kınanmayı giderdim · ona güven vermek için yemin ettim veya sınansın diye yemin sundum
  أبليت فلانا عذرا أي بينت فيما بيني وبينه ما لا لوم علي بعده (ayn)؛ أبليت فلانا يمينا إذا طيبت نفسه بها (sihah;tahdhib)؛ أبليت فلانا يمينا إذا عرضت عليه اليمين لتبلوه بها (mufradat)
- **B005** mezar başında ölüme bırakılan binek ve çevresindeki ağıtçılar — sahibinin mezarı yanında bağlanıp ölüme bırakılan binek · ölen kişinin bineği çevresinde ağıt yakan kadınlar
  البلية الدابة التي كانت تشد في الجاهلية على قبر صاحبها حتى تموت (ayn)؛ البلية أيضا الناقة التي كانت تعقل في الجاهلية عند قبر صاحبها (sihah)؛ البلية الناقة تعقل عند قبر صاحبها فلا تعلف حتى تموت (tahdhib)؛ قامت مبليات فلان ينحن عليه (sihah;tahdhib)
- **B006** olumsuz sözü tersine çeviren olumlu cevap — olumsuz sözü geri çevirip durumu doğrulayan cevap sözü
  بلى جواب استفهام فيه حرف نفي (ayn)؛ بلى جواب للتحقيق توجب ما يقال لك لأنها ترك للنفي (sihah)؛ بلى رد للنفي أو جواب لاستفهام مقترن بنفي (mufradat)
- **B007** önemsememe ve umursamama — onu umursamıyorum, ona önem vermiyorum · önemseme, umursama
  ما أباليه أي ما أكترث له ولم أبل (sihah)؛ بالى يبالي مبالاة (tahdhib)
- **B008** bir topluluk adı ve o topluluğa mensubiyet — Beli adlı boy veya kabile · Beli boyuna mensup, Belevi
  بلي حي والنسبة إليه بلوي (ayn)؛ بلى على فعيل قبيلة من قضاعة والنسبة إليهم بلوى (sihah)؛ بلي حي من اليمن والنسبة إليهم بلوي (tahdhib)
- **B009** belirli bir deyimde farklı yönlere dağılmış olma [kalıp] — her biri farklı bir yana dağılmış
  الناس بذي بلي وذي بلي أي متفرقون (ayn)

## ر ب ب (root_000532) — identity root of رَبُّهُۥ (w6)

- **B001** sahip olup yönetme — Tanrı; sahip, buyruğu geçen yönetici veya düzenleyici · bir şeyin sahibi · evin sahibi veya ev işlerini yöneten kadın · sahiplik, egemenlik ve yönetim yetkisi
  الرب: الله تبارك وتعالى؛ ورب كل شيء مالكه (jamhara); رب كل شئ: مالكه؛ وقد قالوه في الجاهلية للملك؛ رببت القوم: سستهم (sihah); يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح (tahdhib); الرب مصدر مستعار للفاعل؛ لا يقال الرب مطلقا إلا لله؛ رب الدار ورب الفرس (mufradat); فالرب المالك والخالق والصاحب؛ والله جل ثناؤه الرب (maqayis)
- **B002** adım adım yetiştirip tamamlama — yapılan iyiliği eksiksiz kılmak · mülkü gözetip iyileştirmek · çocuğunu yetiştirmek · bir şeyi aşama aşama olgunlaştırma · yetiştirme anlamındaki değişmeli söyleyiş
  رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها (jamhara); رب الضيعة أي أصلحها وأتمها؛ رب فلان ولده؛ رباه (sihah); رب الشيء أي أصلحه؛ رب فلان الصنيعة إذا أتمها وأصلحها (tahdhib); التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام؛ ربه ورباه ورببه (mufradat); رب فلان ضيعته إذا قام على إصلاحها؛ رببت الصبي أربه (maqayis); ربته تربيتا إذا رببه (maqayis-rbt)
- **B003** Tanrı bilgisiyle yetiştiren bilgin — Tanrı bilgisine sahip bilgin ve öğretici
  الرباني: المتأله العارف بالله تعالى (sihah); الرباني: العالم؛ العلماء بالحلال والحرام؛ حكماء علماء؛ العالم المعلم الذي يغذو الناس بصغار العلوم (tahdhib); الرباني... يرب العلم؛ يرب نفسه بالعلم؛ منسوب إلى الرب (mufradat); الربي العارف بالرب (maqayis)
- **B004** büyük insan topluluğu — büyük topluluk; on bin kişilik topluluk · tek birlik hâlinde birleşmiş beş kabile · insanları toplayan kişi veya toplanma yeri
  الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا (sihah); الربيون: الألوف؛ الربيون: الجماعات الكثيرة؛ الربة: عشرة آلاف؛ الربان: الجماعة (tahdhib); يجوز أن يضم الربرب إلى الباب الثالث لتجمعه (maqayis)
- **B005** bakımla kurulan üvey aile bağı — üvey oğul veya bakım altında yetişen erkek çocuk · üvey kız veya bakım altında yetişen kız çocuk · bakıcı kadın; evde sütü için beslenen dişi hayvan · çocuğun bakımını üstlenen üvey baba veya üvey anne
  الراب: زوج الأم؛ الرابة: امرأة الأب؛ ربيب الرجل: ابن امرأته من غيره؛ الربيبة: الحاضنة (sihah); الربيب: ابن امرأة الرجل من غيره؛ ربيبة الرجل: بنت امرأته من غيره؛ راب ورابة (tahdhib); الراب والرابة بأحد الزوجين إذا تولى تربية الولد؛ الربيب والربيبة بذلك الولد (mufradat); ربيب الرجل ابن امرأته؛ الراب الذي يقوم على أمر الربيب (maqayis)
- **B006** koyu öz veya yağ tortusu — koyu meyve özü veya yağ tortusu · koyu özle işlenmiş veya güçlendirilmiş · koyu meyve özüyle hazırlanmış yiyecekler
  رب السمن والزيت: ثفله الأسود؛ سقاء مربوب إذا أصلح بالرب (jamhara); الرب: الطلاء الخاثر؛ سقاء مربوب؛ المرببات الأنبجات (sihah); رب فلان نحيه إذا جعل فيه الرب ومتنه به؛ نحي مربوب (tahdhib); رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب (mufradat); هذا سقاء مربوب بالرب؛ الرب للعنب وغيره لأنه يرب به الشيء (maqayis)
- **B007** bir yerde kalıp sürme — bir yerde kalıp ayrılmamak · develerin sürekli kaldığı yer · bulut sürüp gitti · dişi deve erkeğe bağlandı · bir şeye yaklaşma
  رب بالمكان وأرب إذا أقام به (jamhara); مرب الإبل حيث لزمته؛ أربت الإبل؛ أربت الناقة؛ أربت الجنوب والسحابة أي دامت؛ الأرباب الدنو (sihah); أرب فلان بالمكان إذا أقام به فلم يبرحه؛ مرب الإبل أي حيث لزمته (tahdhib); أربت السحابة: دامت؛ أرب فلان بمكان كذا (mufradat); الأصل الآخر لزوم الشيء والإقامة عليه؛ أربت السحابة؛ الإرباب الدنو (maqayis)
- **B008** katmanlı asılı bulut kümesi — beyaz olabilen, katmanlı veya aşağıda asılı bulut
  الرباب: سحاب أبيض؛ الواحدة ربابة (sihah); الربابة: السحابة التي قد ركب بعضها بعضا؛ جمعها رباب (tahdhib); الرباب: السحاب، سمي بذلك لأنه يرب النبات (mufradat); سمي السحاب ربابا؛ السحاب المتعلق دون السحاب يكون أبيض ويكون أسود (maqayis)
- **B009** başlangıçtaki tazelik — yeni doğurmuş veya sütü için evde tutulan koyun · bir şeyin yeni ve taze dönemi · gençliğin ilk ve taze dönemi
  الربى: الشاة التي وضعت حديثا؛ قرب العهد بالولادة؛ بربانه أي بحدثانه وجدته وطراءته (sihah); الربى: أول الشباب؛ الربان من كل شيء: حدثانه؛ الشاة فهي ربى (tahdhib); الشاة الربي التي تحتبس في البيت للبن؛ التي وضعت حديثا (maqayis)
- **B010** kura oklarını toplayan kap — kura oklarını bir arada tutan deri veya bez kap
  الربابة: قطعة من أدم تجمع فيها القداح (jamhara); الربابة شبيهة بالكنانة تجمع فيها سهام الميسر؛ جماعة السهام (sihah); الربابة: جماعة السهام؛ الجلدة التي تجمع فيها السهام (tahdhib); لما يجمع فيه القدح ربابة (mufradat); الخرقة التي يجعل فيها القداح ربابة (maqayis)
- **B011** bağlayıcı söz ve güvence — tarafları birleştiren bağlayıcı söz veya sözleşme · sözleşmeye bağlı taraflar · bağlayıcı söz; söz gibi bağlayıcı vergi payı
  الربابة: العهد والمعاهدون أربة (jamhara); الربابة: العهد والميثاق؛ الأربة أهل الميثاق (sihah); الرباب: العهد؛ الرباب: العشور (tahdhib); العقد في موالاة الغير: الربابة (mufradat); الربابة وهو العهد؛ للمعاهدين أربة؛ الرباب العشور (maqayis)
- **B012** belirli bir yeşil bitki türü — belirli bir bitki, yumuşak ot veya küçük ağaç türü
  الربة: ضرب من الشجر أو النبت (jamhara); الربة بالكسر: ضرب من النبت، والجمع الربب (sihah); الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف (tahdhib)
- **B013** bol ve toplanmış su — çok miktarda su; bazen bol tatlı su
  الربب، بالفتح: الماء الكثير، ويقال العذب (sihah); الربب وهو الماء الكثير سمي بذلك لاجتماعه (maqayis)
- **B014** yaban sığırı sürüsü — yaban sığırı sürüsü; bazen sığır veya deve topluluğu
  الربرب: القطيع من بقر الوحش (sihah); الربرب: جماعة البقر، وكذلك الإبل (tahdhib); الربرب القطيع من بقر الوحش؛ يجوز أن يضم إلى الباب الثالث لتجمعه (maqayis)
- **B015** azlık bildiren ilgeç — belirsiz adla azlık bildiren ilgeç; nice az · eylem önünde bazen veya kimi zaman · azlık ilgecinin sonuna ses eklenmiş ağız biçimi · belirsiz öğe eklenmiş azlık ilgeci biçimi
  رب: كلمة؛ ربما؛ ربت في معنى رب (jamhara); رب حرف خافض؛ ربما؛ ربت؛ ربه رجلا (sihah); رب من حروف المعاني؛ رب للتقليل؛ ربما؛ ربتما؛ تزيد في رب هاء (tahdhib); رب لاستقلال الشيء، ولما يكون وقتا بعد وقت، نحو ربما (mufradat); رب فكلمة تستعمل في الكلام لتقليل الشيء؛ ولا يعرف لها اشتقاق (maqayis)
- **B016** gereksinim, sıkı düğüm veya iyilik — gereksinim · sıkıca bağlanmış düğüm · iyilik ve başkasına yarar sağlama
  الربى: الحاجة؛ الربى: الرابة؛ الربى: العقدة المحكمة؛ الربى: النعمة والإحسان (tahdhib)
- **B017** gemicilerin başı — gemicilerin başı, kaptan
  رباني: رئيس الملاحين (tahdhib)

## ك ر م (root_001294) — identity root of فَأَكْرَمَهُۥ (w7)

- **B001** övgüye değer soyluluk, eli açıklık ve onurlandırma — soyluluk, eli açıklık ve övgüye değer huy · soylu, eli açık, bağışlayıcı; kendi türünde seçkin · soylular; seçkin ve övgüye değer olanlar · onurlandırdı veya değerli kıldı · onurlandırma ve incitmeden değerli yarar sağlama · onurlandırma; saygınlık · ayıp ve utanç verici şeylerden uzak durdu · soylu ve değerli çocukları oldu · değerli bir bağ ya da varlık edindi · yumuşak ve saygılı söz · kendi alanında yararlı ve övgüye değer tür · içerdiği yol gösterme, açıklama, bilgi ve bilgelikle övgüye değer kitap · içeriği güzel, saygın ya da mühürlü yazı · en soylu ve en erdemli · güzel ve saygın giriş yeri
  شرف في الشيء في نفسه أو شرف في خلق من الأخلاق (maqayis)؛ الكريم الصفوح (maqayis;sihah)؛ الكرم شرف الرجل (ayn)؛ تكرم عن الشائنات أي تنزه (ayn;tahdhib)؛ الكرم ضد اللؤم (sihah)؛ أتى بأولاد كرام واستحدث علقا كريما (sihah)؛ الكثير الخير الجواد المنعم المفضل (tahdhib)؛ اسم جامع لكل ما يحمد (tahdhib)؛ الأخلاق والأفعال المحمودة (mufradat)؛ كل شيء شرف في بابه (mufradat)
- **B002** yağmur getirme ve toprağın verimli oluşu [kalıp] — bulut yağmur getirdi ve suyunu bolca verdi · bitkisi gür, toprağı iyi ve taşları ayıklanmış arazi · toprağı işlenip gübrelendikten sonra bitkisi gürleşti
  كرم السحاب أتى بالغيث (maqayis;sihah)؛ أرض مكرمة للنبات إذا كانت جيدة النبات (maqayis;sihah)؛ إذا جاد السحاب بغيثه قيل كرم (ayn)؛ أرض مثارة منقاة من الحجارة (ayn;tahdhib)؛ البقعة الطيبة التربة العذاة المنبت بقعة مكرمة (tahdhib)؛ كرمت أرض فلان إذا دملها فزكا نبتها (tahdhib)
- **B003** boyun kolyesi — boyna takılan kolye veya dizili süs · kolyeler
  الكَرْم وهي القلادة (maqayis)؛ الكَرْم القلادة (ayn;sihah)؛ رأيت في عنقها كَرْما حسنا من لؤلؤ (sihah)؛ الكروم القلائد واحدها كَرْم (tahdhib)
- **B004** üzüm ve asma — üzüm, asma veya asmanın meyvesi · tek asma sürgünü veya bir asma
  الكَرْم فالعنب أيضا لأنه مجتمع الشعب منظوم الحب (maqayis)؛ الكرمة طاقة من الكرم (ayn)؛ الكَرْم كرم العنب (sihah)؛ الكرمة الطاقة الواحدة من الكرم (tahdhib)؛ يسمى الكرم كرما لأنه وصف بكرم شجرته وثمرته (tahdhib)
- **B005** kap ağzına konan tabak biçimli kapak — testi veya tencere ağzına konan tabak biçimli kapak
  الكرامة طبق يوضع على رأس الحب (ayn;sihah)؛ لطبق القدر والحب الكرامة (tahdhib)
- **B006** eli açıklıkta övünme yarışı ve üstün gelme — onunla eli açıklık konusunda övünme yarışına girdi · eli açıklıkta onu geçti
  كارمت الرجل إذا فاخرته في الكرم فكرمته إذا غلبته فيه (sihah)
- **B007** uyluk kemiğinin kalça yuvasındaki yuvarlak başı — uyluk kemiğinin kalça yuvasındaki yuvarlak başı
  الكرمة رأس الفخذ المستدير كأنه جوزة تدور في قلت الورك (sihah)
- **B008** karşılık bekleyerek sunma ve övgüyü ödüllendirme — karşılığında ödül almak için onu sundu · kendisine yöneltilen övgüyü ödüllendiren kişi
  أكارم بها يهود أي أهديها إليهم فيثيبوني عليها (tahdhib)؛ أخ مكارم أي يكافئني على مدحي إياه (tahdhib)
- **B009** memnuniyetle kabul ve saygı bildiren kalıp yanıt [kalıp] — evet, memnuniyetle ve seve seve · senin için seve seve; sana duyduğum saygıyla
  نعم وحبا وكرامة (sihah)؛ نعم وحبا وكرما وحبا وكرمة (sihah)؛ أفعل ذلك وكرمة لك وكرمى لك وكرامة لك وكرما لك وكرمة عين (tahdhib)
- **B010** değer verilen varlık ve topluluğun seçkin kişisi — senin için çok değerli olan kişi veya şey · topluluğun soylu, saygın ve seçkin kişisi
  كل شيء يكرم عليك فهو كريمك وكريمتك (tahdhib)؛ الكريمة الرجل الحسيب (tahdhib)؛ إذا أتاكم كريمة قوم فأكرموه أي كريم قوم (tahdhib)؛ لا تدخر عنه شيئا يكرم عليك (tahdhib)

## ن ع م (root_001525) — identity root of وَنَعَّمَهُۥ (w8)

- **B001** iyi yaşam durumu ve başkasına ulaştırılan iyilik — bağış, iyilik veya elverişli yaşam durumu · iyi durum ve esenlik · bolluk ve rahatlık · bol ve rahat yaşam · iyiliği başkasına ulaştırma
  أصل واحد يدل على ترفه وطيب عيش وصلاح (maqayis)؛ نعم ينعم نعمة فهو نعم ناعم (ayn;tahdhib)؛ النعمة اليد والصنيعة والمنة وما أنعم به عليك (sihah)؛ نعمة الله منه وعطاؤه (tahdhib)؛ النعمة الحالة الحسنة والإنعام إيصال الإحسان إلى الغير (mufradat)
- **B002** yumuşamak, rahat yaşamak veya rahat yaşatmak — yumuşamak · yumuşak; rahat yaşayan · rahat ve bolluk içinde yaşayan kadın · çocuklarını bolluk içinde yaşattı · rahat ve bolluk içindeki yaşam
  نعم الشيء صار ناعما لينا (sihah)؛ نعمة العيش حسنه وغضارته (tahdhib)؛ نعم فلان أولاده ترفهم (maqayis)؛ طعام ناعم وجارية ناعمة (mufradat)؛ فهو نعم ناعم بين المنعم (ayn)
- **B003** övgü ve beğeni bildirmek — ne güzel; övgü bildirir · bu ne güzel · öyleyse ne güzel, yerinde olur
  نعم ضد بئس (maqayis)؛ نعم وبئس فعلان ماضيان ... فنعم مدح وبئس ذم (sihah)؛ نعما ... المعنى نعم الشيء هي (tahdhib)؛ نعم كلمة تستعمل في المدح بإزاء بئس (mufradat)
- **B004** evet diyerek onaylamak veya söz vermek — evet; doğru; olur · ona evet dedi
  نعم جواب الواجب ضد لا (maqayis)؛ نعم عدة وتصديق وجواب الاستفهام (sihah)؛ نعم يكون تصديقا ويكون عدة (tahdhib)؛ نعم كلمة للإيجاب (mufradat)
- **B005** develer ve geniş anlamda otlayan evcil hayvanlar — develer; deve varlığı · deve, sığır ve koyun topluluğu
  النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم (maqayis)؛ النعم واحد الأنعام وهي المال الراعية وأكثر ما يقع هذا الاسم على الإبل (sihah)؛ النعم لم يريدوا بها إلا الإبل فإذا قالوا الأنعام أرادوا بها الإبل والبقر والغنم (tahdhib)؛ النعم مختص بالإبل وجمعه أنعام (mufradat)
- **B006** devekuşu — devekuşu; erkek veya dişi birey · devekuşu türü veya topluluğu
  النعامة معروفة لنعمة ريشها (maqayis)؛ النعامة من الطير يذكر ويؤنث والنعام اسم جنس (sihah)؛ النعام الظليم والنعامة الأنثى (tahdhib)؛ النعامة سميت تشبيها بالنعم في الخلقة (mufradat)
- **B007** devekuşuna benzetilerek ad verilen şeyler — devekuşuna benzetilen kuyu kirişi, gölgelik, beden bölümü veya yol · Ay'ın konak yerlerinden biri
  على معنى التشبيه النعامة وهي كالظلة تجعل على رءوس الجبل (maqayis)؛ النعامة الخشبة المعترضة على الزرنوقين والنعائم منزل من منازل القمر (sihah)؛ النعامة الخشبة المعترضة على الزرنوقين وابن النعامة عرق الرجل ومحجة الطريق (tahdhib)؛ النعامة المظلة في الجبل وعلى رأس البئر تشبيها بالنعامة في الهيئة والنعائم من منازل القمر (mufradat)
- **B008** bir topluluğun dağılıp gücünü yitirmesi [kalıp] — dağıldılar, ayrıldılar veya güçlerini yitirdiler · hızla yola koyulup gittiler · yenilip dağıldılar
  شالت نعامتهم إذا تفرقوا (maqayis)؛ للقوم إذا ارتحلوا أو تفرقوا قد شالت نعامتهم (sihah)؛ خفت نعامتهم أي استمر بهم السير وشالت نعامتهم إذا تفرقت كلمتهم أو ذهب عزهم (tahdhib)
- **B009** yumuşak esen nemli güney rüzgarı — yumuşak esen nemli güney rüzgarı
  النعامي الريح اللينة (maqayis)؛ النعامى ريح الجنوب لأنها أبل الرياح وأرطبها (sihah)؛ من أسماء الجنوب النعامى (tahdhib)؛ النعامى الريح الجنوب الناعمة الهبوب (mufradat)
- **B010** daha da artırmak veya ileri dereceye götürmek — artırdı; daha ileri götürdü · onu iyice ince öğüttü
  فعل كذا وأنعم أي زاد (sihah;mufradat)؛ أنعم أفضل وزاد وأنعما أي زادا على ذلك ودققت دواء فأنعمت دقه أي بالغت وزدت (tahdhib)
- **B011** bir yeri kendine uygun bulup orada kalmak [kalıp] — bir yere geldi, orayı uygun bulup kaldı
  أتيت أرض بني فلان فتنعمتني إذا وافقته (maqayis)؛ أتيت أرض فلان فتنعمتني إذا وافقته (sihah)؛ أتيت أرضا فنعمتني أي وافقتني وأقمت بها (tahdhib)
- **B012** birine yaya gitmek ve ayakları yürüyerek kullanmak [kalıp] — ona yaya gitti veya onu yürüyerek aradı · ayaklarını yürümekle eskitti; hafif yürüdü
  تنعمت زيدا طلبته كأنه أراد أعمل إليه نعامته وهي باطن قدمه (maqayis)؛ تنعمت فلانا أتيته على غير دابة وتنعم فلان قدميه أي ابتذلهما (tahdhib)؛ تنعم فلان إذا مشى مشيا خفيفا فمن النعمة (mufradat)
- **B013** birini göz sevinci saymak veya bunun için dua etmek [kalıp] — Tanrı seni gözlere sevinç kaynağı kılsın · göz sevinci ve hoşnutluğu
  نعم ونعمى عين ونعمة عين أي قرة عين (maqayis)؛ نعمة العين قرتها ونعم عين ونعام عين ونعامة عين ونعمة عين ونعمى عين كله بمعنى (sihah)؛ نعمك الله عينا ونعم الله بك عينا ونعمى عين ونعام عين (tahdhib)؛ نعم الله بك عينا ونعم ونعمة عين ونعمى عين ونَعام عين (mufradat)

## ق و ل (root_001272) — identity root of فَيَقُولُ (w9)

- **B001** söze dökme — sözü sesle dile getirmek · söylenmiş söz veya sözlü ifade · söylenmiş söz için kullanılan adlar
  القول من النطق (maqayis)؛ قال يقول قولا وقولة ومقالا ومقالة (sihah)؛ القول والقيل واحد (mufradat)؛ المركب من الحروف المبرز بالنطق (mufradat)؛ القيل من القول اسم (ayn)
- **B002** konuşma organı — konuşma organı olan dil
  المقول اللسان (maqayis;ayn;sihah)
- **B003** çok sözlü kişi — çok konuşan, dili güçlü kişi
  رجل قولة وقوال كثير القول (maqayis)؛ رجل تقوالة أي منطيق وقوال وقوالة أي كثير القول (ayn)؛ رجل مقول ومقوال وقولة وقوال وتقوالة أي لسن كثير القول (sihah)
- **B004** sözü geçen yönetici unvanı — sözü geçen yerel hükümdar unvanı · bu unvanın çoğul adları · bu unvanın kadın için kullanılan biçimi
  المقول بلغة أهل اليمن القيل وهم المقاولة والأقيال والأقوال والواحد القيل (ayn)؛ القيل ملك من ملوك حمير دون الملك الأعظم والمرأة قيلة (sihah)؛ كأنه الذي له قول أي ينفذ قوله (sihah)
- **B005** yalan söyleme veya isnat etme [kalıp] — olmayan bir şeyi söyledi · ona yalan isnat etti · bana söylemediğim şeyi yükledi
  تقول باطلا أي قال ما لم يكن (ayn)؛ قولتني ما لم أقل وأقولتني ما لم أقل أي ادعيته علي (sihah)؛ تقول عليه أي كذب عليه (sihah)
- **B006** sözü üzerine alma [kalıp] — iyi ya da kötü bir sözü kendi üzerine aldı
  اقتال قولا أي اجتر إلى نفسه قولا من خير أو شر (ayn)
- **B007** dolaşımdaki söz — hakkında iyi veya kötü söz yayıldı · insanlar arasında yayılmış söz · dedikodu ve çokça dönen laf
  انتشرت له قالة حسنة أو قبيحة في الناس (ayn)؛ القالة القول الفاشي في الناس (ayn)؛ كثر فيه القيل والقال (ayn)؛ كثرت قالة الناس (sihah)؛ كثر القيل والقال (sihah)
- **B008** oyun sopası — oyunda küçük parçaya vurulan tahta sopa
  القال الخشبة التي تضرب بها القلة (sihah)
- **B009** müzakere etme [kalıp] — bir iş hakkında karşılıklı görüştük
  قاولته في أمره وتقاولنا أي تفاوضنا (sihah)
- **B010** hükmünü dayatma [kalıp] — üzerinde hüküm yürüttü, tahakküm etti
  اقتال عليه تحكم (sihah)
- **B011** sanma işlevli söyleme — söyleme fiilini sanmak gibi kurmak
  العرب تجري تقول وحدها في الاستفهام مجرى تظن في العمل (sihah)؛ بنو سليم يجرون متصرف قلت في غير الاستفهام أيضا مجرى الظن (sihah)
- **B012** içte kalmış söz [kalıp] — içte tasarlanıp henüz söylenmemiş anlam
  المتصور في النفس قبل الإبراز باللفظ قول (mufradat)؛ في نفسي قول لم أظهره (mufradat)
- **B013** görüş benimseme [kalıp] — bir görüş veya mezhebi benimsedi
  للاعتقاد نحو فلان يقول بقول أبي حنيفة (mufradat)
- **B014** durumuyla belli etme [kalıp] — durumuyla yeter olduğunu belli etti
  للدلالة على الشيء نحو قول الشاعر امتلأ الحوض وقال قطني (mufradat)
- **B015** içten önemseme [kalıp] — bir şeye içten önem verdi
  للعناية الصادقة بالشيء كقولك فلان يقول بكذا (mufradat)
- **B016** teknik tanım [kalıp] — bir şeyin teknik tanımı
  يستعمله المنطقيون في معنى الحد فيقولون قول الجوهر كذا وقول العرض كذا أي حدهما (mufradat)
- **B017** içe doğan anlam — içe doğan anlamın söz diye adlandırılması
  في الإلهام فإن ذلك لم يكن بخطاب ورد عليه بل كان ذلك إلهاما فسماه قولا (mufradat)

## ECHO ب ل ي (root_000154) — for ٱبْتَلَىٰهُ (w5): withheld observed target; not identity

- **B001** kullanımla eskime ve yolculukta yıpranma — eskimek, kullanımdan yeniliğini yitirmek · eskime, yıpranma · eskimiş, yıpranmış · yolculuğun yıprattığı dişi deve ya da binek
  بلي الشيء يبلى بلى فهو بال (ayn)؛ بلي الثوب يبلى بلى وبلاء (sihah;tahdhib)؛ بلي الثوب بلى وبلاء أي خلق (mufradat)؛ ناقة بلو سفر وبلي سفر للتي قد أبلاها السفر (ayn;sihah;tahdhib;mufradat)
- **B002** iyi ya da kötü koşulla sınama — sınamak ve deneyip tanımak · sınanmak, bir sınamaya uğramak · iyi ya da kötü bir durumla sınanma
  بلي الإنسان وابتلي إذا امتحن (ayn;tahdhib)؛ بلوته بلوا جربته واختبرته (sihah;tahdhib;mufradat)؛ البلاء في الخير والشر (ayn;sihah;tahdhib)؛ المحنة والمنحة جميعا بلاء (mufradat)
- **B003** güzel bir iyilikte bulunma ve üstün çaba [kalıp] — iyilik etmek, güzel bir davranışta bulunmak · cömertlikte ya da savaşta yoğun çaba göstermek
  أبلاه الله إبلاء حسنا إذا صنع به صنيعا جميلا (tahdhib)؛ أبليته معروفا (sihah)؛ أبلى فلان إذا اجتهد في صفة كرم أو حرب (tahdhib)؛ ليبلي المؤمنين منه بلاء حسنا (mufradat)
- **B004** mazeretini açıklayarak kınanmayı kaldırma [kalıp] — mazeretini açıklayıp kınanmayı ortadan kaldırmak
  أبليت فلانا عذرا أي بينت فيما بيني وبينه ما لا لوم علي بعده (ayn)؛ أبليت فلانا عذرا أي بينت له وجه العذر لأزيل عني اللوم (tahdhib)
- **B005** rahatlatmak veya sınamak için yemin sunma [kalıp] — birine yemin ederek içini rahatlatmak veya sınamak üzere ona yemin sunmak
  أبليت فلانا يمينا إذا طيبت نفسه بها (sihah)؛ أبليت فلانا إذا حلفت له فطيبت بها نفسه (tahdhib)؛ أبليت فلانا يمينا إذا عرضت عليه اليمين لتبلوه بها (mufradat)
- **B006** mezar yanında bağlanıp ölüme bırakılan binek — mezar yanında bağlanıp beslenmeden ölüme bırakılan dişi deve ya da binek hayvanı
  البلية الدابة التي كانت تشد في الجاهلية على قبر صاحبها (ayn)؛ البلية أيضا الناقة التي كانت تعقل في الجاهلية عند قبر صاحبها (sihah)؛ البلية الناقة تعقل عند قبر صاحبها فلا تعلف حتى تموت (tahdhib)
- **B007** bir topluluk adı ve ona mensubiyet — belirli bir boyun ya da topluluğun adı · bu boya ya da topluluğa mensup olan
  بلي حي والنسبة إليه بلوي (ayn)؛ بلي قبيلة من العرب ينسب إليها بلوي (jamhara)؛ بلى على فعيل قبيلة من قضاعة والنسبة إليهم بلوى (sihah)؛ بلي حي من اليمين والنسبة إليهم بلوي (tahdhib)
- **B008** ayrı yerlere dağılmış olma [kalıp] — dağınık ve ayrı yerlere yayılmış olmak
  تقول الناس بذي بلي وذي بلي أي متفرقون (ayn)
- **B009** umursamama ve önem vermeme — umursamamak, önem vermemek · umursamama, önem vermeme
  ما أباليه أي ما أكترث له؛ لم أبل؛ ما أباليه بالة (sihah)
- **B010** olumsuzlamayı kaldıran doğrulama cevabı — olumsuzlananı doğrulayan cevap sözü
  بلى جواب استفهام فيه حرف نفي (ayn)؛ بلى جواب للتحقيق توجب ما يقال لك لأنها ترك للنفي (sihah)؛ بلى رد للنفي أو جواب لاستفهام مقترن بنفي (mufradat)

## ECHO ر ب و (root_000537) — for رَبُّهُۥ (w6): withheld observed target; not identity

- **B001** artmak veya yükselmek — bir şey arttı veya yükseldi · toprak suyla kabarıp arttı · yükselen veya fazla köpük · olağandan daha şiddetli yakalayış · onun üzerine çıktı veya üstünde bulundu
  ربا الجرح والأرض والمال وكل شيء يربو إذا زاد (ayn)؛ ربا الشيء يربو ربوا إذا ارتفع (jamhara)؛ ربا الشيء يربو ربوا أي زاد (sihah;tahdhib)؛ ربت أي زادت، وزبدا رابيا، وأخذة رابية (tahdhib;mufradat)؛ أربى عليه أي أشرف عليه (mufradat)
- **B002** yükselmiş arazi — yükselmiş arazi · çevresinden yüksek yer · arazideki yükselti
  الرابية ما ارتفع من الأرض، والربوة لغات أرض مرتفعة (ayn)؛ الربو والربوة والرباوة واحد وهو العلو من الأرض (jamhara)؛ الرابية الربو وهو ما ارتفع من الأرض، وكذلك الربوة (sihah)؛ الرباوة والرابية والرباة كل ذلك ما ارتفع من الأرض (tahdhib)؛ ربوة وربوة وربوة ورباوة، وسميت الربوة رابية (mufradat)
- **B003** belirli işlem biçimleriyle sınırlı anapara fazlalığı — belirli alışveriş veya borç biçimlerinde anaparayı aşan fazlalık · işlemdeki anapara fazlalığının özel adı veya bir söyleyiş biçimi · mal bu işlemde fazlalıkla arttı · anaparaya fazlalık eklenen işleme girdi
  ربا المال يربو في الربا أي يزداد، والربا في كتاب الله حرام، والربية هي الربا خاصة (ayn)؛ الربا في البيع، والربية لغة في الربا (sihah)؛ الربا ربوان، فالحرام كل قرض يؤخذ به أكثر منه (tahdhib)؛ الربا الزيادة على رأس المال، لكن خص في الشرع بالزيادة على وجه دون وجه (mufradat)
- **B004** soluğu yükselip sıkışmak — yüksek ve sıkışık soluma · soluğu sıkıştı · at koşu ya da ürkme yüzünden şişip soluksuz kaldı · soluğu yükselip tıkanmış
  ربا فلان أي أصابه نفس في جوفه ودابة بها ربو (ayn)؛ أصابه ربو من مشي أو عدو إذا علت أنفاسه (jamhara)؛ الربو النفس العالي، وربا الفرس إذا انتفخ من عدو أو فزع (sihah)؛ أخذها الربو وهو البهر (tahdhib)؛ الربو الانبهار سمي بذلك تصورا لتصعده (mufradat)
- **B005** besleyip büyütmek ve yetişmek — onu besleyip büyüttü · onların arasında yetişti · çocuğu besleyip büyüttü, çocuk gelişti
  ربيته وتربيته أي غذوته (ayn)؛ ربوت في بني فلان وربيت أي نشأت فيهم، وربيته تربية وتربيته أي غذوته، هذا لكل ما ينمي كالولد والزرع (sihah)؛ ربيت الولد فربا من هذا (mufradat)
- **B006** uyluk kökü ve iç yanlardaki iki çıkıntılı et parçası — uyluk kökü veya kasık eti · uyluk köklerinin iç yanlarındaki iki çıkıntılı et parçası
  الأربية أصل الفخذ، وهما أربيتان (sihah)؛ الأربيتان لحمتان ناتئتان في أصول الفخذين من باطن (mufradat)
- **B007** baba tarafından yakın hane halkının arasına gelmek [kalıp] — kendi topluluğundaki baba tarafından yakın hane halkının arasına geldi
  جاء فلان في أربية قومه، أي في أهل بيته من بني الأعمام ونحوهم، ولا تكون الأربية من غيرهم (sihah)

## ECHO ق ل ل (root_001251) — for فَيَقُولُ (w9): withheld observed target; not identity

- **B001** azlık — az şey; azlık · azlık ve yetersizlik; yoksulluk ve düşüklük · az; az sayıda veya az miktarda · azalmak; az olmak · gözünde az göstermek · yoksullaşmak · az saymak; az görmek · hiç; ne azı ne çoğu · pek seyrek; hemen hemen hiç · yoksulluğa ve aşağılanmaya uğrasın · hiç malı olmamak · kendisi de ailesi de tanınmayan adam
  القل القليل؛ رماه الله بالقل والذل أي بالقلة والذلة (jamhara)؛ شيء قليل وجمعه قلل؛ قل الشيء يقل قلة؛ قلله في عينه؛ أقل افتقر؛ استقله عده قليلا (sihah)؛ قل الشيء يقل قلة فهو قليل وقلال؛ القل من الرجال الخسيس الدنيء؛ قليلة ولا كثيرة؛ قليلا ما يؤمنون؛ قاللت لفلان؛ تقاللت ما أعطاني (tahdhib)؛ القلة والكثرة يستعملان في الأعداد؛ يكنى بالقلة عن الذلة؛ يكنى بها تارة عن العزة؛ قليل يعبر به عن النفي (mufradat)
- **B002** bir şeyin tepesi veya başı — dağın tepesi; doruk · bir şeyin tepesi veya başı · insanın başı · sap ucunda topuzu bulunan kılıç
  القلة قلة الجبل وهي القطعة تستدير في أعلاه وهي القنة (jamhara)؛ القلة أعلى الجبل؛ قلة كل شيء أعلاه؛ رأس الإنسان قلة (sihah)؛ قلة كل شيء رأسه؛ قلة الجبل أعلاه؛ قبيعة السيف قلته؛ سيف مقلل (tahdhib)؛ قلة الجبل شعفه (mufradat)
- **B003** büyük küp — büyük küp; iri kap · belirli bir bölgenin iri küpleri · iki büyük küp veya bunların aldığı miktar
  القلة التي جاءت في الحديث مثل قلال هجر هي جرار عظام (jamhara)؛ القلة إناء للعرب كالجرة الكبيرة؛ قلال هجر شبيهة بالحباب (sihah)؛ قلتين يعني هذه الحباب العظام واحدتها قلة؛ قلال هجر؛ القلة منها تأخذ مزادة من الماء (tahdhib)؛ القلة ما أقله الإنسان من جرة وحب (mufradat)
- **B004** yük kaldırma, yükselme ve yola koyulma — küpü taşıyabilmek · bir şeyi taşımak; yüklenmek · ağır bulutları taşımak · uçuşa kalkmak; havalanmak · yüklenip yola çıkmak · yükselmek
  أقل الجرة أطاق حملها؛ استقلت السماء ارتفعت؛ استقل القوم مضوا وارتحلوا (sihah)؛ أقل الرجل الشيء واستقله إذا احتمله؛ استقل الطائر إذا نهض للطيران؛ استقل النبات أناف؛ استقل القوم إذا احتملوا ظاعنين؛ أقلت سحابا ثقالا أي حملت؛ قل إذا رفع وقل إذا علا (tahdhib)؛ أقلت سحابا ثقالا أي احتملته؛ أقللت كذا وجدته قليل المحمل (mufradat)
- **B005** korku veya öfkeden titreme — korku veya öfkeden doğan titreme · korku veya öfkeden titremeye tutulmak · öfkeden titremek
  القل الرعدة والانتفاض؛ أخذ فلانا القل إذا أخذته رعدة من فزع (jamhara)؛ القل بالكسر شبه الرعدة؛ أخذه قل من الغضب (sihah)؛ القل الرعدة؛ أخذه قل إذا أرعد من الغضب؛ إذا غضب قد استقل (tahdhib)
- **B006** oynatma ve kararsızca sallanma — sallanma, yerinde duramama ve hareket sesi · sallayıp oynatmak · sallanmak; yerinde duramamak · çevik; hızlı
  قلقل أي صوت وهو حكاية؛ قلقله قلقلة وقلقالا فتقلقل أي حركه فتحرك واضطرب (sihah)؛ القلقلة والتقلقل قلة الثبوت في المكان؛ يتقلقل في موضعه؛ القلق ألا يستقر الشيء في مكان واحد (tahdhib)؛ تقلقل الشيء إذا اضطرب؛ تقلقل المسمار؛ القلقلة حكاية صوت الحركة (mufradat)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:15, and ## Buluşmalar) =====
## Su: fışkıran, taşan, yukarıdan dökülen

İlk kelimenin kökü, karanlıktan önce suyun yarılmasını anlatır: {ar:انفجر الماء انفجارا تفتح, tr:infecera'l-mâu'nficâran tefettah, gloss:su fışkırdı, önü açıldı, source:"ف ج ر,B001"}. Fışkırma şöyle tarif edilir: {ar:إذا انبعث سائلا, tr:ize'nbe'ase sâilen, gloss:akarak fırladığında, source:"ف ج ر,B001"}. Kaya ya da toprak bir noktada çatlar, içerideki su bastırarak dışarı fırlar ve akmaya başlar. Kur'an bu sahneyi taşın içinden kurar. İsrailoğullarına kalplerinin taştan da katı olduğu söylenirken bazı taşlardan ırmakların fışkırdığı hatırlatılır: {ar:وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ, tr:ve inne mine'l-hicârati lemâ yetefecceru minhu'l-enhâr, gloss:taşların öylesi var ki içinden ırmaklar fışkırır, source:2:74}. Nuh'un tufanında aynı fiil yeryüzünü kaynaklara çevirir ve su ölçüsü önceden belirlenmiş bir iş üzerinde buluşur: {ar:وَفَجَّرْنَا ٱلْأَرْضَ عُيُونًۭا فَٱلْتَقَى ٱلْمَآءُ عَلَىٰٓ أَمْرٍۢ قَدْ قُدِرَ, tr:ve feccernâ'l-arda uyûnen fe'lteka'l-mâu alâ emrin kad kudir, gloss:yeri kaynaklar hâlinde fışkırttık, su takdir edilmiş bir iş üzerinde buluştu, source:54:12}. Kıyamette denizler fışkırtılır: {ar:وَإِذَا ٱلْبِحَارُ فُجِّرَتْ, tr:ve ize'l-bihâru fuccirat, gloss:denizler fışkırtıldığında, source:82:3}. Mekke'de inkârcılar Peygamber'den, arasından ırmaklar fışkırttığı bir bahçe isterler {source:17:91}. Kur'an bu işi cennette Allah'ın kullarına verir: {ar:عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا, tr:aynen yeşrabu bihâ ibâdu'llâhi yufeccirûnehâ tefcîrâ, gloss:Allah'ın kullarının içtiği, dilediklerince fışkırttıkları bir kaynak, source:76:6}.

Aynı kök günahı da adlandırır: {ar:الانبعاث والتفتح في المعاصي فجورا, tr:el-inbi'âsu ve't-tefettuhu fi'l-me'âsî fucûrâ, gloss:günahlara atılmak ve açılmak, fücur, source:"ف ج ر,B004"}. Suyun önünü yarıp fırlaması ile insanın günaha açılıp atılması aynı kelimeyle söylenir. Bu yüzden surenin geçmiş kavimleri anlatan bölümü bir sel gibi duyulur.

Dokuzuncu ayette Semûd kayayı vadide oymuştur: {ar:بِٱلْوَادِ, tr:bi'l-vâd, gloss:vadide, source:89:9}. Vadi selin yoludur: {ar:كل مفرج بين جبال وآكام وتلال يكون مسلكا للسيل, tr:kullu mufracin beyne cibâlin ve âkâmin ve tilâlin yekûnu meslekan li's-seyl, gloss:dağlar, tepeler ve tümsekler arasında selin geçtiği her açıklık, source:"و د ي,B005"}. Kök akmayı adlandırır: {ar:ودى أي سال, tr:vedâ ey sâl, gloss:aktı, source:"و د ي,B001"}. Kaya evler suyun indiği yatağa kurulmuştur. Kur'an'ın sel benzetmesinde vadiler kendi ölçüleri kadar akar ve sel kabarık bir köpük taşır: {ar:فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا, tr:fe-sâlet evdiyetun bi-kaderihâ fahtemele's-seylu zebeden râbiyâ, gloss:vadiler ölçülerince aktı, sel kabarık bir köpük taşıdı, source:13:17}. Köpük gider, insanlara yarayan yerde kalır. Âd da vadilerine doğru gelen bulutu yağmur sanmıştır. Hûd'un Ahkâf'ta kavmini uyarmasıyla başlayan sahnede {source:46:21} bulutu görünce şöyle derler: {ar:قَالُوا۟ هَٰذَا عَارِضٌۭ مُّمْطِرُنَا ۚ بَلْ هُوَ مَا ٱسْتَعْجَلْتُم بِهِۦ ۖ رِيحٌۭ فِيهَا عَذَابٌ أَلِيمٌۭ, tr:kâlû hâzâ âridun mumtırunâ, bel huve me'sta'celtum bih, rîhun fîhâ azâbun elîm, gloss:"Bu bize yağmur getiren bir bulut" dediler. Hayır, o acele istediğiniz şeydir: içinde acı bir azap olan bir rüzgâr, source:46:24}.

On birinci ayetin fiili suyun taşmasıdır: {ar:ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ, tr:ellezîne tağav fi'l-bilâd, gloss:o ülkelerde azanlar, source:89:11}. Arapçada sel için {ar:طغى السيل إذا جاء بماء كثير, tr:tağa's-seylu izâ câe bi-mâin kesîr, gloss:sel bol suyla gelince "taştı" denir, source:"ط غ ي,B002"}, su için de {ar:طغى الماء خروجه عن المقدار, tr:tuğyânu'l-mâi hurûcuhû ani'l-mikdâr, gloss:suyun taşması ölçüsünden çıkmasıdır, source:"ط غ ي,B002"} denir. Ayette anlam azgınlıktır. Yanında ölçüsünden çıkan, yatağını aşan su duyulur. Kur'an kelimeyi tufan için doğrudan kullanır: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tağa'l-mâu hamelnâkum fi'l-câriye, gloss:su taştığında sizi akıp giden gemide taşıdık, source:69:11}. On ikinci ayet taşkının sonucunu verir: {ar:فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ, tr:fe-ekserû fîhe'l-fesâd, gloss:oralarda bozgunu çoğalttılar, source:89:12}. Çoğalmak {ar:الكثرة نماء العدد, tr:el-kesretu nemâu'l-aded, gloss:çokluk, sayının büyümesidir, source:"ك ث ر,B001"} demektir, bozulmak da {ar:الفساد خروج الشيء عن الاعتدال, tr:el-fesâdu hurûcu'ş-şey'i ani'l-i'tidâl, gloss:fesat, bir şeyin dengeden çıkmasıdır, source:"ف س د,B001"}. Hacim büyür ve şeyler dengelerinden çıkar. Bozgunun tarifindeki "çıkış" suyun ölçüden çıkışıyla aynı kelimedir. Kur'an'da bozgun karaya ve denize yayılır: {ar:ظَهَرَ ٱلْفَسَادُ فِى ٱلْبَرِّ وَٱلْبَحْرِ, tr:zahera'l-fesâdu fi'l-berri ve'l-bahr, gloss:karada ve denizde bozgun ortaya çıktı, source:30:41}. Salih de Semûd'a, Âd'dan sonra yerleştirildikleri yeryüzünde ovalardan saraylar edinip dağları ev diye oyduklarını hatırlatır ve sonra şöyle der: {ar:وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ, tr:ve lâ ta'sev fi'l-ardı mufsidîn, gloss:yeryüzünde bozguncular olarak dolaşmayın, source:7:74}.

On üçüncü ayet taşkına yukarıdan karşılık verir: {ar:فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ, tr:fe-sabbe aleyhim rabbuke savte azâb, gloss:Rabbin de üzerlerine azap kamçısı yağdırdı, source:89:13}. Sabb, suyun fiilidir: {ar:صب الماء إراقته من أعلى, tr:sabbu'l-mâi irâkatuhû min a'lâ, gloss:suyu dökmek, onu yukarıdan akıtmaktır, source:"ص ب ب,B001"}. Vadiye inmek de bu fiille söylenir: {ar:صب في الوادي إذا انحدر فيه, tr:sabbe fi'l-vâdî izenhadera fîh, gloss:vadiye indi, oraya doğru aktı, source:"ص ب ب,B002"}. Aşağıda yatağını taşan suya yukarıdan dökülen bir şey karşılık verir. Dökülenin adı azaptır ve bu kelimenin harfleri tatlı suyu da adlandırır: {ar:العذب ضد الملح وكل مستسيغ من طعام أو شراب, tr:el-azbu diddu'l-milhi ve kullu mustesâğin min taâmin ev şarâb, gloss:azb, tuzlunun zıddıdır; boğazdan rahat geçen her yiyecek ve içecek, source:"ع ذ ب,B001"}. Âd'ın yağmur sandığı rüzgâr bu iki yüzü tek sahnede gösterir: beklenen tatlı su, gelen ise azaptır {source:46:24}.

Aynı su sahnesi surenin ikinci yarısında rahmet olarak döner. Kur'an insana yemeğine bakmasını söyler: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:suyu bol bol döktük, source:80:25}, {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:summe şekakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26}. Fiil aynıdır, ama bu kez arkasından yarılan toprak ve biten yemek gelir. Surenin sınav sahnesindeki kelimeler bu yağmuru da taşır. İkram için {ar:كرم السحاب أتى بالغيث, tr:keruma's-sehâbu etâ bi'l-ğays, gloss:bulut cömert davrandı, yağmur getirdi, source:"ك ر م,B002"} denir. Rızık için {ar:وقد يسمى المطر رزقا, tr:ve kad yusemma'l-mataru rızkâ, gloss:yağmura da rızık denir, source:"ر ز ق,B003"} denir. Kur'an da şöyle der: {ar:وَفِى ٱلسَّمَآءِ رِزْقُكُمْ, tr:ve fi's-semâi rızkukum, gloss:rızkınız göktedir, source:51:22}. Ölçü için de {ar:ينزل المطر بمقدار, tr:yenzilu'l-mataru bi-mikdâr, gloss:yağmur ölçüyle iner, source:"ق د ر,B001"} denir. On altıncı ayette rızkın daraltılması, yağmurun ölçüyle inmesinin insanın gözünden görünen yüzüdür. Yirmi dördüncü ayetteki "hayatım" kelimesinin yanında yağmur duyulur: {ar:الحيا المطر لأنه يحيي الأرض بعد موتها, tr:el-hayâ el-mataru li-ennehû yuhyi'l-arda ba'de mevtihâ, gloss:hayâ yağmurdur, çünkü yeri ölümünden sonra diriltir, source:"ح ي ي,B002"}. Yirmi sekizinci ayetteki "dön" kelimesinin yanında da dökülüp yeniden gelen yağmur duyulur: {ar:الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث, tr:er-rec'u el-ğaysu ve huve'l-mataru li-ennehâ tuğîsu ve tasubbu summe terci'u fe-tuğîs, gloss:rec' yağmurdur, çünkü yağar, dökülür, sonra döner ve yine yağar, source:"ر ج ع,B006"}. Kur'an da göğe dönüşüyle yemin eder: {ar:وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ, tr:ve's-semâi zâti'r-rec', gloss:dönüp dönüp yağan göğe, source:86:11}. Ölü toprağa yağmur gönderilmesi, ölülerin çıkarılmasının örneğidir: {ar:كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:kezâlike nuhricu'l-mevtâ leallekum tezekkerûn, gloss:ölüleri de böyle çıkarırız; belki düşünüp hatırlarsınız, source:7:57}. Son kelime bu suyun ürününe varır: bahçeye ve bitkinin gürleşip çiçek açmasına: {ar:جن النبت جنونا إذا اشتد وخرج زهره, tr:cenne'n-nebtu cunûnen izeştedde ve harace zehruh, gloss:bitki gürleşip çiçeğini çıkarınca "cenne" denir, source:"ج ن ن,B011"}.

Surede suyun işleyişi bir ölçüye bağlanır. Ölçüsünde kalan su hayat verir, ölçüsünü aşan su süpürür. Âd, Semûd ve Firavun ölçüyü aşan taşkındır ve onlara yukarıdan azap dökülür. İnsana ölçülü rızık iner ve o, ölçünün kendisini aşağılanma sanır.

Kaynaklar: 89:1 وَٱلْفَجْرِ ف ج ر B001; 89:1 وَٱلْفَجْرِ ف ج ر B004; 89:9 بِٱلْوَادِ و د ي B001; 89:9 بِٱلْوَادِ و د ي B005; 89:11 طَغَوْا۟ ط غ ي B002; 89:12 فَأَكْثَرُوا۟ ك ث ر B001; 89:12 ٱلْفَسَادَ ف س د B001; 89:13 فَصَبَّ ص ب ب B001; 89:13 فَصَبَّ ص ب ب B002; 89:13 عَذَابٍ ع ذ ب B001; 89:15 فَأَكْرَمَهُۥ ك ر م B002; 89:16 فَقَدَرَ ق د ر B001; 89:16 رِزْقَهُۥ ر ز ق B003; 89:24 لِحَيَاتِى ح ي ي B002; 89:28 ٱرْجِعِىٓ ر ج ع B006; 89:30 جَنَّتِى ج ن ن B011

## Gözetleme yeri ve bakan göz

Altıncı ayet dinleyenin gözünü olup bitene çevirir: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِعَادٍ, tr:e-lem tera keyfe feale rabbuke bi-Âd, gloss:Rabbinin Âd'a ne yaptığını görmedin mi, source:89:6}. Görmek, gözle ya da kalple bakmaktır: {ar:نظر وإبصار بعين أو بصيرة, tr:nazarun ve ibsârun bi-aynin ev basîra, gloss:gözle ya da basiretle bakıp görmek, source:"ر ء ي,B001"}. Aynı kalıp Fil sahiplerinin akıbetini anlatırken de kullanılır: {ar:أَلَمْ تَرَ كَيْفَ فَعَلَ رَبُّكَ بِأَصْحَٰبِ ٱلْفِيلِ, tr:e-lem tera keyfe feale rabbuke bi-ashâbi'l-fîl, gloss:Rabbinin fil sahiplerine ne yaptığını görmedin mi, source:105:1}. Dinleyen, bir olayın gözlemcisi yapılır.

Gözlenen şey yolda olan insanlardır. Dördüncü ayetin fiili gece yürüyenleri de adlandırır: {ar:السارية للقوم الذين يسرون بالليل, tr:es-sâriye li'l-kavmi'llezîne yesrûne bi'l-leyl, gloss:sâriye, gece yol alan topluluktur, source:"س ر ي,B001"}. Dokuzuncu ayetteki fiilin yanında ülkeleri boydan boya geçmek duyulur: {ar:جبت البلاد أجوبها وأجيبها واجتبتها إذا قطعتها, tr:cubtu'l-bilâde ecûbuhâ ve ecîbuhâ ve'ctebtuhâ izâ kata'tuhâ, gloss:ülkeleri boydan boya geçtim, source:"ج و ب,B002"}. On birinci ayette bu yolcular ülkelerde sınırı aşar: {ar:مجاوزة الحد في العصيان, tr:mucâvezetu'l-haddi fi'l-isyân, gloss:isyanda sınırı geçmek, source:"ط غ ي,B001"}. Ayetlerin anlamı kazmak ve azmaktır. Yanında yol alan, ülke aşan ve sınırı geçen yolcular duyulur.

On dördüncü ayet yolun üzerindeki yeri adlandırır: {ar:إِنَّ رَبَّكَ لَبِٱلْمِرْصَادِ, tr:inne rabbeke le-bi'l-mirsâd, gloss:Rabbin elbette gözetleme yerindedir, source:89:14}. Mirsâd hem yolun kendisidir, {ar:المرصاد الطريق, tr:el-mirsâd et-tarîk, gloss:mirsâd yoldur, source:"ر ص د,B003"}, hem de gözcünün beklediği yer: {ar:المرصاد المكان الذي يرصد به الراصد, tr:el-mirsâdu'l-mekânu'llezî yersudu bihi'r-râsıd, gloss:mirsâd, gözcünün gözetlediği yerdir, source:"ر ص د,B003"}. Gözcü bir şeyi kollayan kişidir: {ar:الراصد للشئ المراقب له, tr:er-râsıdu li'ş-şey'i el-murâkıbu leh, gloss:râsıd, bir şeyi gözetleyendir, source:"ر ص د,B001"}. Aynı kök yolda pusu kuran yılana da ad verir: {ar:يقال للحية التي ترصد المارة على الطريق رصيد, tr:yukâlu li'l-hayyeti'lletî tersudu'l-mârrate ale't-tarîki rasîd, gloss:yolda geçenleri kollayan yılana rasîd denir, source:"ر ص د,B001"}. Bu düzenin işleyişi şöyledir: gözcü kimseyi kovalamaz, yolun geçtiği yerde bekler. Her yolcu oradan geçmek zorundadır. Bir önceki ayetteki dökme fiili bu yılanın hareketini de anlatır: {ar:صبت الحية عليه إذا ارتفعت فانصبت عليه من فوق, tr:sabbeti'l-hayyetu aleyhi izertefeat fensabbet aleyhi min fevk, gloss:yılan kalkıp yukarıdan üstüne çullandı, source:"ص ب ب,B008"}. Surenin sıralaması da bu düzene uyar. Önce darbe iner, gözetleme yeri ancak sonra adlandırılır. Yolcular gözcünün varlığını vuruldukları anda öğrenir.

Kur'an aynı yeri başka sahnelerde de kurar. Kıyamet anlatılırken cehennem için {ar:إِنَّ جَهَنَّمَ كَانَتْ مِرْصَادًۭا, tr:inne cehenneme kânet mirsâdâ, gloss:cehennem bir gözetleme yeridir, source:78:21} denir. Antlaşmayı bozanlara karşı verilen emir şöyledir: {ar:وَٱقْعُدُوا۟ لَهُمْ كُلَّ مَرْصَدٍۢ, tr:vak'udû lehum kulle marsad, gloss:onlar için her gözetleme yerinde oturun, source:9:5}. İblis de Allah'a şöyle der: {ar:لَأَقْعُدَنَّ لَهُمْ صِرَٰطَكَ ٱلْمُسْتَقِيمَ, tr:le-ek'udenne lehum sırâtake'l-mustekîm, gloss:onlar için senin dosdoğru yolunun üstünde oturacağım, source:7:16}. Şuayb kavmine yollarda pusu kurmamalarını söyler: {ar:وَلَا تَقْعُدُوا۟ بِكُلِّ صِرَٰطٍۢ تُوعِدُونَ, tr:ve lâ tak'udû bi-kulli sırâtin tûidûn, gloss:tehdit ederek her yolun başında oturmayın, source:7:86}. Cinler gökte kendilerini bekleyen bir alev bulur: {ar:يَجِدْ لَهُۥ شِهَابًۭا رَّصَدًۭا, tr:yecid lehû şihâben rasadâ, gloss:kendisini gözetleyen bir alev bulur, source:72:9}. Allah elçisinin önüne ve arkasına gözcüler koyar {source:72:27}. İnsanın söylediği her sözün yanında da hazır bir gözcü vardır: {ar:مَّا يَلْفِظُ مِن قَوْلٍ إِلَّا لَدَيْهِ رَقِيبٌ عَتِيدٌۭ, tr:mâ yelfızu min kavlin illâ ledeyhi rakîbun atîd, gloss:ağzından çıkan her sözün yanında hazır bir gözcü vardır, source:50:18}.

Bakmanın bir de insanın içindeki yüzü vardır. On beşinci ve yirmi üçüncü ayetlerdeki "insan" kelimesi göz bebeğindeki küçük sureti de adlandırır: {ar:إنسان العين المثال الذي يرى في السواد, tr:insânu'l-ayn el-misâlu'llezî yurâ fi's-sevâd, gloss:gözün insanı, gözbebeğinin karasında görünen küçük surettir, source:"ء ن س,B005"}. Bu tanımda misal ve görmek kelimeleri birlikte geçer. Sekizinci ayetin kökü sureti, {ar:التمثال الصورة, tr:et-timsâl es-sûra, gloss:timsal, surettir, source:"م ث ل,B008"}, ve görülerek alınan dersi de adlandırır: {ar:يكون المثل بمعنى العبرة, tr:yekûnu'l-meselu bi-ma'ne'l-ibra, gloss:mesel, ibret anlamına da gelir, source:"م ث ل,B011"}. Beşinci ayetin hicr kökü gözün çevresine de ad verir: {ar:ومحجر العين ما يدور بها, tr:ve mahcaru'l-ayni mâ yedûru bihâ, gloss:gözün mahceri, onu çevreleyen yerdir, source:"ح ج ر,B006"}. Üçüncü ayetteki çift kelimesi de bir tek şeyi iki gören gözü adlandırır: {ar:عين شافعة تنظر نظرين, tr:aynun şâfiatun tenzuru nazarayn, gloss:şâfia göz, iki bakışla bakan gözdür, source:"ش ف ع,B006"}. Sure insana Âd'ı, Semûd'u ve Firavun'u göstermiştir. İnsan ise hemen ardından kendi hâline bakar ve tek bir sınavı iki ayrı hüküm olarak okur: bolluğa ikram, darlığa aşağılanma der. Kur'an bu bakışın kendini nasıl gördüğünü söyler {source:96:7}. Âd'a da kulaklar, gözler ve gönüller verilmişti, ama onlara bir yararı olmadı: {ar:فَمَآ أَغْنَىٰ عَنْهُمْ سَمْعُهُمْ وَلَآ أَبْصَٰرُهُمْ, tr:fe-mâ ağnâ anhum sem'uhum ve lâ ebsâruhum, gloss:ne kulakları ne gözleri onlara bir yarar sağladı, source:46:26}. Kıyamet günü örtü kalkar: {ar:فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌۭ, tr:fe-keşefnâ anke ğitâeke fe-basaruke'l-yevme hadîd, gloss:örtünü üstünden kaldırdık, bugün gözün keskindir, source:50:22}.

Kaynaklar: 89:3 ٱلشَّفْعِ ش ف ع B006; 89:4 يَسْرِ س ر ي B001; 89:5 حِجْرٍ ح ج ر B006; 89:6 تَرَ ر ء ي B001; 89:8 مِثْلُهَا م ث ل B008; 89:8 مِثْلُهَا م ث ل B011; 89:9 جَابُوا۟ ج و ب B002; 89:11 طَغَوْا۟ ط غ ي B001; 89:13 فَصَبَّ ص ب ب B008; 89:14 لَبِٱلْمِرْصَادِ ر ص د B001; 89:14 لَبِٱلْمِرْصَادِ ر ص د B003; 89:15 ٱلْإِنسَٰنُ ء ن س B005

## Kucak, ikram ve yetim

On beşinci ayet bir sınavla açılır: {ar:فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ, tr:fe-emme'l-insânu izâ me'btelâhu rabbuhû fe-ekramehû ve na''amehû, gloss:insan ise Rabbi onu sınayıp ikram ettiğinde ve nimet verdiğinde, source:89:15}. İbtilâ denemektir: {ar:بلوته بلوا جربته واختبرته, tr:belevtuhû belven carrabtuhû ve'htebertuh, gloss:onu denedim, sınadım, source:"ب ل و,B002"}. Allah'ın sınaması iki yolla olur: {ar:اختبار الله للعباد تارة بالمسار وتارة بالمضار, tr:ihtibâru'llâhi li'l-ibâdi târeten bi'l-mesârri ve târeten bi'l-medârr, gloss:Allah kullarını bazen sevindiren, bazen zarar veren şeylerle sınar, source:"ب ل و,B003"}. Kur'an bunu açıkça söyler: {ar:وَنَبْلُوكُم بِٱلشَّرِّ وَٱلْخَيْرِ فِتْنَةًۭ, tr:ve nebluküm bi'ş-şerri ve'l-hayri fitneh, gloss:sizi deneme olarak kötülükle de iyilikle de sınarız, source:21:35}. İsrailoğulları da iyiliklerle ve kötülüklerle sınanmıştır, belki dönerler diye {ar:وَبَلَوْنَٰهُم بِٱلْحَسَنَٰتِ وَٱلسَّيِّـَٔاتِ لَعَلَّهُمْ يَرْجِعُونَ, tr:ve belevnâhum bi'l-hasenâti ve's-seyyiâti leallehum yerci'ûn, gloss:belki dönerler diye onları iyiliklerle ve kötülüklerle sınadık, source:7:168}.

Sınayan "Rabbi"dir. Rab kökü bir şeyi aşama aşama büyütmeyi anlatır: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi olgunluğuna erinceye kadar hâlden hâle geçirerek yetiştirmektir, source:"ر ب ب,B002"}. Aynı kök üvey çocuğu da adlandırır: {ar:ربيب الرجل ابن امرأته, tr:rabîbu'r-racul ibnu'mraetih, gloss:adamın rebîbi, karısının oğludur, source:"ر ب ب,B005"}. Nimet vermek de bir babanın çocuklarına davranışıyla söylenir: {ar:نعم فلان أولاده ترفهم, tr:na''ame fulânun evlâdehû tarrafehum, gloss:çocuklarını bolluk içinde, nazla büyüttü, source:"ن ع م,B002"}. İkram eden de şöyle tarif edilir: {ar:الكثير الخير الجواد المنعم المفضل, tr:el-kesîru'l-hayri'l-cevâdu'l-mun'imu'l-mufdıl, gloss:hayrı bol, cömert, nimet veren, lütfeden, source:"ك ر م,B001"}. Ayetin yanında bir aile sahnesi duyulur: bir çocuk kucakta büyütülür, nazla beslenir ve el üstünde tutulur. Beşinci ayetin hicr kelimesi bu kucağın kendisini de adlandırır: {ar:حجر المرأة وحجرها حضنها, tr:hicru'l-mer'eti ve hacruhâ hıdnuhâ, gloss:kadının hicri kucağıdır, source:"ح ج ر,B005"}. Kur'an rab kökünü ve kucak kelimesini bir hükümde bir araya getirir: {ar:وَرَبَٰٓئِبُكُمُ ٱلَّٰتِى فِى حُجُورِكُم, tr:ve rebâibukumu'llâtî fî hucûrikum, gloss:kucaklarınızda büyüyen üvey kızlarınız, source:4:23}. Büyümüş çocuk anne babası için şöyle dua eder: {ar:رَّبِّ ٱرْحَمْهُمَا كَمَا رَبَّيَانِى صَغِيرًۭا, tr:rabbi'rhamhumâ kemâ rabbeyânî sağîrâ, gloss:Rabbim, onlar beni küçükken nasıl büyüttülerse sen de onlara öyle merhamet et, source:17:24}. Firavun ise Musa'ya büyütme hakkıyla gelir: {ar:أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا, tr:e-lem nurabbike fînâ velîdâ, gloss:seni çocukken aramızda büyütmedik mi, source:26:18}.

İnsan bu bakımı bir rütbe olarak okur: {ar:فَيَقُولُ رَبِّىٓ أَكْرَمَنِ, tr:fe-yekûlu rabbî ekramen, gloss:"Rabbim bana ikram etti" der, source:89:15}. Darlıkta ise şöyle olur: {ar:فَقَدَرَ عَلَيْهِ رِزْقَهُۥ, tr:fe-kadera aleyhi rızkahû, gloss:rızkını daralttı, source:89:16}. Bu ifade şöyle açıklanır: {ar:ومن قدر عليه رزقه أي ضيق عليه, tr:ve men kudira aleyhi rızkuhû ey duyyika aleyh, gloss:rızkı daraltılan, yani darlığa sokulan, source:"ق د ر,B004"}. İnsan bu kez "Rabbim beni aşağıladı" der. Aşağılanmış kişi ikramdan yoksun olandır: {ar:الهين الذي لا كرامة له, tr:el-heyyinu'llezî lâ kerâmete leh, gloss:hîn, ikramı olmayandır, source:"ه و ن,B003"}. Aşağılanma bir otoritenin hor görmesiyle gelir: {ar:الهوان من جهة متسلط مستخف به, tr:el-hevânu min cihetin mutesallitin mustahiffin bih, gloss:hevân, onu hafife alan bir hükmedenden gelir, source:"ه و ن,B003"}. İnsan darlığı böyle okur, Rabbini kendisini hor gören bir efendi yerine koyar. Kur'an'da rızkın genişletilmesi ve daraltılması bir hüküm değil, Allah'ın dilemesidir. Bunu Kârûn'un yere geçirilişinden sonra, dün onun yerinde olmayı isteyenler söyler: {ar:وَيْكَأَنَّ ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ, tr:veykeenna'llâhe yebsutu'r-rızka li-men yeşâu min ibâdihî ve yakdir, gloss:demek ki Allah rızkı kullarından dilediğine genişletiyor ve daraltıyormuş, source:28:82}. Rızkı daraltılana verilen hüküm de, Allah'ın verdiğinden harcamasıdır {ar:وَمَن قُدِرَ عَلَيْهِ رِزْقُهُۥ فَلْيُنفِقْ مِمَّآ ءَاتَىٰهُ ٱللَّهُ, tr:ve men kudira aleyhi rızkuhû fe'l-yunfik mimmâ âtâhu'llâh, gloss:rızkı daraltılan, Allah'ın kendisine verdiğinden harcasın, source:65:7}. Nimeti kendi bilgisine bağlayan insana Kur'an şöyle cevap verir: {ar:بَلْ هِىَ فِتْنَةٌۭ, tr:bel hiye fitneh, gloss:hayır, o bir sınavdır, source:39:49}.

On yedinci ayet bu okumayı kökünden çevirir: {ar:كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ, tr:kellâ, bel lâ tukrimûne'l-yetîm, gloss:hayır, asıl siz yetime ikram etmiyorsunuz, source:89:17}. Az önce insanın kendine alınan bir sıfat sandığı ikram, burada başkasına yapılan bir iş olur. Arapçada ikram cömertlikte yarışmak ve o yarışta öne geçmektir: {ar:كارمت الرجل إذا فاخرته في الكرم فكرمته إذا غلبته فيه, tr:kâramtu'r-racule izâ fâhartuhû fi'l-kerem fe-keremtuhû izâ ğalebtuhû fîh, gloss:cömertlikte yarıştım ve onu cömertlikte geçtim, source:"ك ر م,B006"}. İnsan bu yarışa hiç girmez. Yetim tam bu yerde durur. O, kucağı kalmamış çocuktur: {ar:انقطاع الصبي عن أبيه قبل بلوغه, tr:inkıtâu's-sabiyyi an ebîhi kable bulûğih, gloss:çocuğun ergenliğe ermeden babasından kopması, source:"ي ت م,B001"}. Kelimenin iki yan anlamı da onun durumunu anlatır: {ar:أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره, tr:aslu'l-yutmi'l-ğafle, ve bihî yusemma'l-yetîmu li-ennehû yutegâfelu an birrih, gloss:yetimliğin aslı gaflettir; yetime bu ad verilir, çünkü ona iyilik etmek ihmal edilir, source:"ي ت م,B003"}, {ar:اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه, tr:el-yutmu'l-ibtâ', ve minhu ühıze'l-yetîmu li-enne'l-birra yubtıu anh, gloss:yutm gecikmedir; yetim adı buradan gelir, çünkü iyilik ona geç ulaşır, source:"ي ت م,B004"}. Rabbi tarafından nazla büyütülen insan, babasız çocuğa geç kalır. Kur'an Peygamber'e kendi yetimliğini hatırlatarak bu ilişkiyi kurar: {ar:أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ, tr:e-lem yecidke yetîmen fe-âvâ, gloss:seni yetim bulup barındırmadı mı, source:93:6}, {ar:فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ, tr:fe-emme'l-yetîme fe-lâ takhar, gloss:öyleyse yetimi ezme, source:93:9}. Barındırılmış olan barındırır. İkramın ölçüsü de verilir: {ar:إِنَّ أَكْرَمَكُمْ عِندَ ٱللَّهِ أَتْقَىٰكُمْ, tr:inne ekramekum inda'llâhi etkâkum, gloss:Allah katında en değerliniz, en takvalı olanınızdır, source:49:13}. Allah'ın aşağıladığını kimse yüceltemez: {ar:وَمَن يُهِنِ ٱللَّهُ فَمَا لَهُۥ مِن مُّكْرِمٍ, tr:ve men yuhini'llâhu fe-mâ lehû min mukrim, gloss:Allah kimi aşağılarsa onu yüceltecek kimse yoktur, source:22:18}. Cehennemdeki suçluya ise bu sıfat alay olarak söylenir: {ar:ذُقْ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْكَرِيمُ, tr:zuk inneke ente'l-azîzu'l-kerîm, gloss:tat bakalım, hani sen güçlüydün, değerliydin, source:44:49}.

Kaynaklar: 89:5 حِجْرٍ ح ج ر B005; 89:15 ٱبْتَلَىٰهُ ب ل و B002; 89:15 ٱبْتَلَىٰهُ ب ل و B003; 89:15 رَبُّهُۥ ر ب ب B002; 89:15 رَبُّهُۥ ر ب ب B005; 89:15 فَأَكْرَمَهُۥ ك ر م B001; 89:15 وَنَعَّمَهُۥ ن ع م B002; 89:16 فَقَدَرَ ق د ر B004; 89:16 أَهَٰنَنِ ه و ن B003; 89:17 تُكْرِمُونَ ك ر م B006; 89:17 ٱلْيَتِيمَ ي ت م B001; 89:17 ٱلْيَتِيمَ ي ت م B003; 89:17 ٱلْيَتِيمَ ي ت م B004

## Yol, binek ve dönüş

Surenin kelimeleri bir yolculuğun aşamalarını sırayla taşır. Dördüncü ayette gece yürüyüşü başlar: {ar:السرى سير الليل, tr:es-surâ seyru'l-leyl, gloss:gece yürüyüşü, source:"س ر ي,B001"}. Kur'an bu kökü kul ve gece kelimeleriyle aynı cümlede kullanır: {ar:سُبْحَٰنَ ٱلَّذِىٓ أَسْرَىٰ بِعَبْدِهِۦ لَيْلًۭا, tr:subhâna'llezî esrâ bi-abdihî leylen, gloss:kulunu geceleyin yürüten Allah'ı tesbih ederim, source:17:1}. Dokuzuncu ayetteki fiilin yanında ülke ülke dolaşan yolcu duyulur: {ar:رجل جواب إذا كان قطاعا للبلاد, tr:raculun cevvâbun izâ kâne kattâan li'l-bilâd, gloss:cevvâb, ülkeleri durmadan aşan adamdır, source:"ج و ب,B002"}. On beşinci ve on altıncı ayetlerdeki sınav fiilinin yanında da yolun bineği yıpratması duyulur: {ar:ناقة بلو سفر أبلاها السفر, tr:nâkatun ilvu seferin eblâhe's-sefer, gloss:yolculuğun yıprattığı dişi deve, source:"ب ل و,B001"}. Elbisenin eskimesi de aynı köktendir: {ar:بلي الثوب يبلى بلى وبلاء, tr:beliye's-sevbu yeblâ bilen ve belâ', gloss:elbise eskidi, yıprandı, source:"ب ل و,B001"}. Ayette anlam sınamaktır. Yanında kullanıldıkça yıpranan, yürüdükçe tükenen bir binek duyulur. Sınavın, insanın kendisine ait sandığı şeyi aşındırdığı da duyulur.

Yolculuğun karşısında yere yapışmak vardır. Yirminci ayetteki sevgi kelimesi bir şeye yapışıp kalmakla açıklanır: {ar:الحب والمحبة اشتقاقه من أحبه إذا لزمه, tr:el-hubbu ve'l-mahabbe iştikâkuhû min ehabbehû izâ lezimeh, gloss:sevgi kelimesi bir şeye yapışıp ondan ayrılmamaktan türer, source:"ح ب ب,B002"}. Aynı fiil inatla yerinden kalkmayan deveyi de anlatır: {ar:أحب البعير إذا حرن ولزم مكانه, tr:ehabbe'l-baîru izâ harana ve lezime mekâneh, gloss:deve inat edip yerinden kalkmayınca "ehabbe" denir, source:"ح ب ب,B005"}. Malı yapışarak seven insan çöküp kalmış bir bineğe benzer. Sekizinci ve on birinci ayetlerdeki "ülkeler" kelimesi de yerleşip kalmayı taşır: {ar:بلد بالمكان أقام به فهو بالد, tr:belede bi'l-mekâni ekâme bih, gloss:bir yerde kalıp yerleşti, source:"ب ل د,B009"}, {ar:بلد الرجل بالأرض إذا لزق بها, tr:belede'r-raculu bi'l-ardı izâ leziga bihâ, gloss:adam yere yapıştı, source:"ب ل د,B010"}. Devenin göğsünü yere koyup çökmesi de aynı köktendir: {ar:وضعت الناقة بلدتها بالأرض إذا بركت, tr:vedaati'n-nâkatu beldetehâ bi'l-ardı izâ berakat, gloss:deve göğsünü yere koyup çöktü, source:"ب ل د,B002"}. Yirmi birinci ayetteki yer kelimesinin kökü yere ağırlaşmayı da söyler: {ar:التأرض أيضا التثاقل إلى الأرض, tr:et-teerrudu eydan et-tesâkulu ile'l-ard, gloss:teerrud, yere doğru ağırlaşmaktır, source:"ء ر ض,B006"}. Onuncu ayetteki kazık ayağı yere çakar, yirmi altıncı ayetteki bağ ise bağlar. Kur'an bu ağırlığı bir çağrı sahnesinde adlandırır. Allah yolunda harekete geçmeye çağrılan müminlere şöyle seslenir: {ar:ٱثَّاقَلْتُمْ إِلَى ٱلْأَرْضِ ۚ أَرَضِيتُم بِٱلْحَيَوٰةِ ٱلدُّنْيَا مِنَ ٱلْءَاخِرَةِ, tr:issâkaltum ile'l-ard, e-radîtum bi'l-hayâti'd-dunyâ mine'l-âhira, gloss:yere çakılıp kaldınız; dünya hayatına ahiretten daha mı razı oldunuz, source:9:38}. Yer, razı olmak ve hayat: surenin sonundaki kelimeler burada ters yönde dizilmiştir. Ayetlerine rağmen yere saplanıp kalan adam da şöyle anlatılır: {ar:وَلَٰكِنَّهُۥٓ أَخْلَدَ إِلَى ٱلْأَرْضِ وَٱتَّبَعَ هَوَىٰهُ, tr:ve lâkinnehû ahlede ile'l-ardı ve'ttebea hevâh, gloss:ama o yere saplanıp kaldı ve hevesine uydu, source:7:176}.

Yolun sonu dönüştür. Altıncı ayette adı geçen Âd, Arapçada dönüş anlamındaki kökün altında sayılır: {ar:عاد قبيلة وهم قوم هود, tr:Âd kabîle, ve hum kavmu Hûd, gloss:Âd bir kabiledir, Hûd'un kavmidir, source:"ع و د,B012"}. Aynı kök varılacak yeri de adlandırır: {ar:المعاد المصير والمرجع, tr:el-meâd el-masîru ve'l-merci', gloss:meâd, varılacak ve dönülecek yerdir, source:"ع و د,B002"}. Âd bir özel addır ve bu anlamı taşımaz, yalnız harfleri dönüşü çağrıştırır. Kur'an Peygamber'e dönüş yerini vaat eder: {ar:لَرَآدُّكَ إِلَىٰ مَعَادٍۢ, tr:le-râdduke ilâ meâd, gloss:seni elbette dönüş yerine döndürecektir, source:28:85}. Yirmi yedinci ayet yolcuyu durulmuş olarak karşılar: {ar:يَٰٓأَيَّتُهَا ٱلنَّفْسُ ٱلْمُطْمَئِنَّةُ, tr:yâ eyyetuhe'n-nefsu'l-mutmainne, gloss:ey huzura kavuşmuş can, source:89:27}. Huzur, sarsıntıdan sonra gelen dinginliktir: {ar:الطمأنينة والاطمئنان السكون بعد الانزعاج, tr:et-tume'nîne ve'l-itmi'nân es-sukûnu ba'de'l-inzi'âc, gloss:itminan, sarsıntıdan sonraki dinginliktir, source:"ط م ء ن,B001"}. Kur'an bu dinginliğin kaynağını da söyler: {ar:أَلَا بِذِكْرِ ٱللَّهِ تَطْمَئِنُّ ٱلْقُلُوبُ, tr:elâ bi-zikri'llâhi tatmainnu'l-kulûb, gloss:bilin ki kalpler ancak Allah'ı anmakla huzura kavuşur, source:13:28}. Yirmi sekizinci ayetteki çağrı şöyledir: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ, tr:irciî ilâ rabbiki, gloss:Rabbine dön, source:89:28}. Dönmek, başlanılan yere geri gitmektir: {ar:الرجوع العود إلى ما كان منه البدء, tr:er-rucûu'l-avdu ilâ mâ kâne minhu'l-bed', gloss:rücû, başlangıç noktasına dönmektir, source:"ر ج ع,B001"}. Aynı kök, bir yolculuktan ötekine geri gönderilen yorgun hayvanı da adlandırır: {ar:الرجيع من الدواب ما رجعته من سفر إلى سفر وهو الكال, tr:er-recî' mine'd-devâbbi mâ raca'tehû min seferin ilâ sefer, ve huve'l-kâll, gloss:recî', bir yolculuktan ötekine döndürülen yorgun hayvandır, source:"ر ج ع,B014"}. Çağrılan can ise yeni bir yola gönderilmez. Yolun bittiği yere döndürülür. Kur'an insanın bütün çabasını bu yöne bağlar: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًۭا فَمُلَٰقِيهِ, tr:yâ eyyuhe'l-insânu inneke kâdihun ilâ rabbike kedhan fe-mulâkîh, gloss:ey insan, sen Rabbine doğru zahmetle çabalıyorsun ve O'na kavuşacaksın, source:84:6}. Varılacak yer de bir yerleşmedir: {ar:إِلَىٰ رَبِّكَ يَوْمَئِذٍ ٱلْمُسْتَقَرُّ, tr:ilâ rabbike yevmeizini'l-mustekarr, gloss:o gün varılıp karar kılınacak yer Rabbinin huzurudur, source:75:12}. Azan insana da aynı söz söylenir: {ar:إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ, tr:inne ilâ rabbike'r-ruc'â, gloss:dönüş Rabbinedir, source:96:8}. Sınanıp musibete uğrayanların sözü de dönüşle biter: {ar:إِنَّا لِلَّهِ وَإِنَّآ إِلَيْهِ رَٰجِعُونَ, tr:innâ li'llâhi ve innâ ileyhi râciûn, gloss:biz Allah'a aitiz ve O'na döneceğiz, source:2:156}. Yorgun binek imgesi ile dönüş çağrısı burada aynı insanda birleşir. Dönüşün tersi de Kur'an'dadır. Ölüm gelince inkârcı geri gönderilmeyi ister: {ar:رَبِّ ٱرْجِعُونِ, tr:rabbi'rciûn, gloss:Rabbim, beni geri gönderin, source:23:99}. Cevap ise surenin iki kez kullandığı kelimedir: {ar:كَلَّآ ۚ إِنَّهَا كَلِمَةٌ هُوَ قَآئِلُهَا, tr:kellâ, innehâ kelimetun huve kâiluhâ, gloss:hayır, bu yalnızca onun söylediği bir sözdür, source:23:100}. Yolun en son aşaması giriştir: {ar:فَٱدْخُلِى فِى عِبَٰدِى, tr:fedhulî fî ibâdî, gloss:kullarımın arasına gir, source:89:29}. Kur'an bu girişi kapılar açılırken bölük bölük sürülen bir kafile olarak da gösterir: {ar:وَسِيقَ ٱلَّذِينَ ٱتَّقَوْا۟ رَبَّهُمْ إِلَى ٱلْجَنَّةِ زُمَرًا, tr:ve sîka'llezîne'ttekav rabbehum ile'l-cenneti zumerâ, gloss:Rablerinden sakınanlar bölük bölük cennete sürülür, source:39:73}.

Kaynaklar: 89:4 يَسْرِ س ر ي B001; 89:6 بِعَادٍ ع و د B002; 89:6 بِعَادٍ ع و د B012; 89:8 ٱلْبِلَٰدِ ب ل د B002; 89:8 ٱلْبِلَٰدِ ب ل د B009; 89:11 ٱلْبِلَٰدِ ب ل د B010; 89:9 جَابُوا۟ ج و ب B002; 89:15 ٱبْتَلَىٰهُ ب ل و B001; 89:20 وَتُحِبُّونَ ح ب ب B002; 89:20 وَتُحِبُّونَ ح ب ب B005; 89:21 ٱلْأَرْضُ ء ر ض B006; 89:27 ٱلْمُطْمَئِنَّةُ ط م ء ن B001; 89:28 ٱرْجِعِىٓ ر ج ع B001; 89:28 ٱرْجِعِىٓ ر ج ع B014; 89:29 فَٱدْخُلِى د خ ل B001

## Buluşmalar

On üçüncü ayet üç imgeyi tek bir fiilde toplar. Dökme fiili suyun fiilidir, nesnesi kamçıdır ve yukarıdan çullanan yılanın hareketini de taşır. Hemen ardından gelen ayet gözetleme yerini adlandırır. Böylece bir önceki ayetteki taşkın, ölçüsünü aşan su olarak duyulur ve karşılığını yukarıdan inen bir kütle olarak alır. Bu karşılık bir pusu gibi, yolcuların geçmek zorunda olduğu yerden gelir. Âd'ın vadilerine doğru gelen bulut bu buluşmanın Kur'an'daki sahnesidir: göğe doğru bakılır, tatlı su beklenir, gelen ise azaptır {source:46:24}. Azap kelimesinin harfleri tatlı suyu ve kamçının ucunu birlikte adlandırdığı için tek bir kelime hem beklenen şeyi hem geleni söyler.

Yirmi birinci ve yirmi ikinci ayetler yıkım ile gelişi aynı zemine koyar. Sütunlar, kaya evler ve kazıklar dümdüz edilir. Saf saf gelen meleklerin durduğu yer de bu düzlüktür. Düzlüğün adı safsaf, saf kelimesinden türer {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, gloss:tek bir saf gibi dümdüz yer, source:"ص ف ف,B005"}. Kur'an da dağların savrulup dümdüz bir ova bırakılacağını söyler {source:20:106}. Yedinci ayetteki sütun sabahın ilk aydınlığının da adıdır: {ar:عمود الصبح ابتداء ضوئه, tr:amûdu's-subhi ibtidâu dav'ih, gloss:sabahın sütunu, ışığının başlangıcıdır, source:"ع م د,B007"}. Surenin başında dikilen tek şey bu ışık sütunuydu. Âd'ın taş sütunları yıkıldıktan sonra yerde dimdik duran tek şey meleklerin saflarıdır. Kur'an mal toplayıp sayanın sonunu da yine sütunlarla anlatır: {ar:فِى عَمَدٍۢ مُّمَدَّدَةٍۭ, tr:fî amedin mumeddede, gloss:uzatılmış sütunlar içinde, source:104:9}. Bu sahnede yığma imgesi ile dikme imgesi birleşir. Ağzına kadar doldurulan kap ile yükseltilen sütun aynı insanın elindedir ve ikisi de onu kurtarmaz {source:104:3}.

Surenin ilk kelimesi ile son kelimesi bir örtü üzerinde buluşur. Fecr karanlığın örtüsünü yarar, son kelime ise ağaçların örtüsüdür. Aradaki fücur, din örtüsünü yırtmaktır. Kur'an cennetin içinde suyun fışkırmasını da gösterir ve bu işi kullara verir {source:76:6}. Fecr kökünün su anlamı, kul kelimesi ve bahçe aynı yerde bir araya gelir. Yirmi dokuzuncu ve otuzuncu ayetlerde kullarının arasına ve bahçesine çağrılan can, böylece surenin ilk kelimesinin anlattığı fışkırmayı içeride bulur. Azgınların taşkını ölçüsünü aşmıştı. Bu fışkırma ise içenlerin dilediği ölçüde akar.

Yolculuk ile alçalma imgeleri yirmi yedinci ayette buluşur. Malı yapışarak seven kişi, yerinden kalkmayan bir deve gibi yere çökmüştür. Yer kelimesinin bir anlamı ağırlaşmaktır, ülkeler kelimesinin bir anlamı da yere yapışmaktır. Huzura kavuşmuş can da yerdedir, ama çakılmış ya da çökmüş değildir. Alçak bir yer gibi durulmuştur, sırtını eğmiştir ve sarsıntıdan sonra dinginleşmiştir. Çağrı ona yapılır. Kur'an yere çakılıp kalmakla dünya hayatına razı olmayı aynı ayette kınar {source:9:38}. Sure ise rızayı karşılıklı kılar ve bunu yere çakılı kalmanın tersi olan bir dönüşe bağlar: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:irciî ilâ rabbiki râdiyeten merdiyyeh, gloss:razı olmuş ve razı olunmuş olarak Rabbine dön, source:89:28}.

Çift-tek imgesi ile sofra imgesi yetimde buluşur. Yetim, yanına kimse geçmemiş tek kişidir. Ona ikram etmek, yanına geçip arka çıkmaktır. Mirası paylara ayırmadan silip süpüren ise başkalarının payını kendi payına katar ve tek başına bir yığın oluşturur. Kıyamette herkes tek gelir ve yanında arka çıkacak kimse görünmez {source:6:94}. Sure bu tekliğin karşısına bir topluluğa katılan canı koyar. İkram kelimesi de son kez Kur'an'ın bir başka sahnesinde, doğru yere oturmuş olarak duyulur. Elçilere uyulmasını öğütlediği için kavmince öldürülen adama cennete girmesi söylenir ve o da bir "keşke" söyler, ama bu keşke içeriden söylenir: {ar:قِيلَ ٱدْخُلِ ٱلْجَنَّةَ ۖ قَالَ يَٰلَيْتَ قَوْمِى يَعْلَمُونَ, tr:kîle'dhuli'l-cenneh, kâle yâ leyte kavmî ya'lemûn, gloss:"Cennete gir" denildi; "Keşke kavmim bilseydi" dedi, source:36:26}, {ar:بِمَا غَفَرَ لِى رَبِّى وَجَعَلَنِى مِنَ ٱلْمُكْرَمِينَ, tr:bimâ ğafera lî rabbî ve cealenî mine'l-mukramîn, gloss:Rabbimin beni bağışladığını ve ikram edilenlerden kıldığını, source:36:27}. On beşinci ayetteki insan "Rabbim bana ikram etti" derken malına bakıyordu. Bu adam aynı sözü bir girişin ardından, Rabbinin bağışlamasına bakarak söyler.

