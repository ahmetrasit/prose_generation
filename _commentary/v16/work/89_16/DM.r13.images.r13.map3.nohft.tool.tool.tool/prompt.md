Focus: 89:16. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/89_16/D.r13/context.md =====
# 89:16 — focus

وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ

Anchor translation (canonical reading, reference only):

Onu sınayıp geçimini daralttığında ise, “Rabbim beni aşağıladı” der.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَأَمَّآ | أَمَّا |  | CONJ;EXL |
| 2 | إِذَا | إِذَا |  | T |
| 3 | مَا | مَا |  | SUP |
| 4 | ٱبْتَلَىٰهُ | ٱبْتَلَىٰٓ | ب ل و | V;PRON |
| 5 | فَقَدَرَ | قَدَرَ | ق د ر | CONJ;V |
| 6 | عَلَيْهِ | عَلَىٰ |  | P;PRON |
| 7 | رِزْقَهُۥ | رِزْق | ر ز ق | N;PRON |
| 8 | فَيَقُولُ | قَالَ | ق و ل | RSLT;V |
| 9 | رَبِّىٓ | رَبّ | ر ب ب | N;PRON |
| 10 | أَهَٰنَنِ | أَهَٰنَ | ه و ن | V;PRON |


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
- 89:16 ◀ focus وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ عَلَيْهِ رِزْقَهُۥ فَيَقُولُ رَبِّىٓ أَهَٰنَنِ
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


===== _commentary/v16/work/89_16/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ب ل و (root_000153) — identity root of ٱبْتَلَىٰهُ (w4)

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

## ق د ر (root_001205) — identity root of فَقَدَرَ (w5)

- **B001** bir şeyin ölçüsü ve eriştiği sınır — bir şeyin ölçüsü, niceliği ve sınırı · belirlenmiş ölçü, sınır veya süre
  مبلغ الشيء وكنهه ونهايته (maqayis)؛ القدر مبلغ الشيء؛ لكل شيء مقدار وأجل (ayn)؛ قدر الشيء مبلغه (sihah)؛ المقدار هو الهنداز؛ ينزل المطر بمقدار (tahdhib)؛ القدر والتقدير تبيين كمية الشيء (mufradat)
- **B002** Tanrı'nın varlıkları ölçülü biçimde hükme bağlaması — Tanrı'nın varlıklar için belirlediği ölçülü hüküm · Tanrısal belirlemeyi reddetmekle anılan topluluk · belirli işlere ayrılmış özel gece
  قضاء الله تعالى الأشياء على مبالغها ونهاياتها (maqayis)؛ القدر القضاء الموفق؛ قدره الله تقديرا (ayn;tahdhib)؛ ما يقدره الله عزوجل من القضاء (sihah)؛ يجعلها على مقدار مخصوص ووجه مخصوص حسبما اقتضت الحكمة (mufradat)
- **B003** bir şeyi yapmaya veya ona egemen olmaya elveren güç — bir işi yapmaya elveren güç ve yetkinlik · gücü yeten ve yapabilen · dilediğini gerçekleştirecek ölçüde güçlü · gücü olan veya güç edinmiş · varlıklı ve geniş olanaklı
  قدرة الله تعالى على خليقته؛ رجل ذو قدرة وذو مقدرة أي يسار (maqayis)؛ قدر على الشيء قدرة أي ملك فهو قادر (ayn;tahdhib)؛ الاقتدار على الشيء القدرة عليه؛ رجل ذو قدرة أي ذو يسار (sihah)؛ القدرة إذا وصف بها الإنسان فاسم لهيئة له بها يتمكن (mufradat)
- **B004** birinin geçim payını kısmak [kalıp] — onun geçim payını kıstı · onu darlığa sokarız
  من قدر عليه رزقه فمعناه قتر (maqayis)؛ قدر على عياله مثل قتر؛ قدر على الإنسان رزقه مثل قتر (sihah)؛ نضيق عليه؛ ضيق عليه (tahdhib)؛ قدرت عليه الشيء ضيقته؛ ومن قدر عليه رزقه أي ضيق عليه (mufradat)
- **B005** ölçüp biçerek tasarlamak ve hazırlamak — ölçüsünü belirleyip hazırladı · ayın gün sayısını hesaplayıp otuza tamamlayın · örgülü işi düzgün ve sağlam kurdu · o şey onun için hazır duruma geldi
  اقتدرت الشيء جعلته قدرا؛ قدرت الشيء أي هيأته (ayn)؛ فاقدروا له أي أتموا ثلاثين؛ تقدر له الشيء أي تهيأ (sihah)؛ التروية والتفكير في تسوية أمر وتهيئته؛ نظرت فيه ودبرته وقايسته؛ قدر في السرد أي أحكمه (tahdhib)؛ التقدير من الإنسان التفكر في الأمر؛ فكر وقدر؛ قدر في السرد أي أحكمه (mufradat)
- **B006** söz öbeğine göre ölçüye uygun, orta veya yapıca ölçülü olma [kalıp] — ölçüsüne uydu ve tam denk geldi · orta büyüklükte eyer · orta boylu adam · kısa boyunlu veya kısa adam · arka ayaklarını ön ayak izlerine basan at · yol alması kolay gece
  جاء على قدره؛ المقتدر الوسط؛ سرج قدر أي وسط (ayn)؛ بين أرضك وأرض فلان ليلة قادرة؛ الأقدر القصير؛ الأقدار من الخيل (sihah)؛ كل شيء مقتدر فهو الوسط؛ القدر من الرحال والسروج الوسط؛ الأقدر من الرجال القصير العنق؛ الأقدر من الخيل (maqayis;tahdhib)؛ الأقدر القصير العنق؛ فرس أقدر (mufradat)
- **B007** pişirme kabı ve ona bağlı yemek, pişirme işi ve görevli sözleri — et veya yemek pişirme tenceresi · tencerede pişmiş et veya yemek · pişmiş çorba suyu · topluluk tencerede yemek pişirdi · hayvanı kesip etini pişiren kasap veya aşçı
  القدر وهي معروفة؛ القدير اللحم يطبخ في القدر؛ القدار الجزار ويقال الطباخ (maqayis)؛ القدير ما طبخ من اللحم؛ مرق مقدور؛ القدار الطباخ (ayn)؛ القدير المطبوخ في القدر؛ القدار الجزار ويقال الطباخ (sihah)؛ القدر مؤنثة؛ قدرت القدر إذا طبخت قدرا؛ القدار الجزار (tahdhib)؛ القدر اسم لما يطبخ فيه اللحم؛ قدرت اللحم طبخته؛ القدار الذي ينحر ويقدر (mufradat)

## ر ز ق (root_000560) — identity root of رِزْقَهُۥ (w7)

- **B001** yararlanılmak üzere verilen pay — yararlanılan pay veya sağlanan geçimlik · Tanrı ona yararlanacağı bir pay verdi · kendisine bilgi verildi · yararı sağlayan veya ulaşmasına aracılık eden · bütün varlıklara sürekli geçim payı sağlayan Tanrı için özel niteleme
  أصيل واحد يدل على عطاء لوقت ثم يحمل عليه غير الموقوت (maqayis)؛ الرزق عطاء الله (maqayis)؛ رزق الله يرزق العباد رزقا اعتمدوا عليه (ayn)؛ الرزق ما ينتفع به والرزق العطاء (sihah)؛ الرزق معروف (tahdhib)؛ الرزق يقال للعطاء الجاري وللنصيب (mufradat)؛ الرازق يقال لخالق الرزق ومعطيه والمسبب له والرزاق لا يقال إلا لله تعالى (mufradat)
- **B002** yenip beslenilen yiyecek — yenip bedeni besleyen yiyecek
  وجد عندها رزقا عنبا في غير حينه (tahdhib)؛ لما يصل إلى الجوف ويتغذى به (mufradat)؛ فليأتكم برزق منه أي بطعام يتغذى به (mufradat)؛ عني به الأغذية (mufradat)
- **B003** yağmur — yağmur; gökten inerek canlılığı sürdüren su
  وقد يسمى المطر رزقا (sihah)؛ في السماء رزقكم قال المطر (tahdhib)؛ في السماء رزقكم قيل عني به المطر الذي به حياة الحيوان (mufradat)
- **B004** asker ödeneği — yönetici askerlere ödeneklerini verdi · askerlere tek seferde verilen ödeme · askerler ödeneklerini aldı
  إذا أخذ الجند أرزاقهم قيل ارتزقوا رزقة واحدة (ayn)؛ الرزقة بالفتح المرة الواحدة وهي أطماع الجند وارتزق الجند أي أخذوا أرزاقهم (sihah)؛ رزق الأمير جنده فارتزقوا ارتزاقا (tahdhib)؛ رزق الجند رزقة واحدة ورزقوا رزقتين (tahdhib)؛ ارتزق الجند أخذوا أرزاقهم والرزقة ما يعطونه دفعة واحدة (mufradat)
- **B005** iyiliğe gönül borcunu bildirme — size verilen iyiliğe karşılık yalanlamayı seçiyorsunuz · bana yaptığım iyilik için gönül borcunu bildirdin
  الرزق بلغة أزدشنوءة الشكر (maqayis)؛ فعلت ذلك لما رزقتني أي لما شكرتني (maqayis)؛ وتجعلون رزقكم أنكم تكذبون أي شكر رزقكم (sihah)؛ تجعلون شكر رزقكم التكذيب (tahdhib)؛ تجعلون نصيبكم من النعمة تحري الكذب (mufradat)
- **B006** iyi talih sahibi olma — talihli; payına iyi sonuçlar düşen
  رجل مرزوق أي مجدود (sihah)؛ تنبيه أن الحظوظ بالمقادير (mufradat)
- **B007** biçime bağlı adlandırmalar — beyaz keten giysiler · belirli bir üzüm çeşidi
  الرازقية ثياب كتان بيض (sihah)؛ الرازقية ثياب كتان بيض (tahdhib)؛ الرازقي من الأعناب هو الملاحي (tahdhib)

## ق و ل (root_001272) — identity root of فَيَقُولُ (w8)

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

## ر ب ب (root_000532) — identity root of رَبِّىٓ (w9)

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

## ه و ن (root_001608) — identity root of أَهَٰنَنِ (w10)

- **B001** yumuşak, ağırbaşlı sakinlik — sakinlik, ağırbaşlılık ve yumuşaklık · ağırbaşlı ve sakin yürümek · ölçülü ve aşırılığa kaçmadan · acele etmeden, sakince · uysal, sakin ve yumuşak huylu
  الهون مصدر الهين في معنى السكينة والوقار؛ هو يمشي هونا؛ تكلم على هينتك؛ رجل هين لين (ayn)؛ الهون: السكينة والوقار؛ يمشي على الأرض هونا؛ قوم هينون لينون؛ امش على هينتك أي على رسلك (sihah)؛ تذلل الإنسان في نفسه لما لا يلحق به غضاضة؛ يمشون على الأرض هونا؛ المؤمن هين لين (mufradat)؛ أصيل يدل على سكون أو سكينة أو ذل؛ الهون السكينة والوقار (maqayis)
- **B002** kolay ve hafif olma — kolaylık ve yükün hafifliği · birine kolay ve hafif gelmek · onun için kolaylaştırıp hafifletmek · kolay, hafif ve güç olmayan · daha kolay ve daha hafif
  الهون: مصدر هان عليه الشيء أي خف؛ هونه الله عليه أي سهله وخففه؛ شيء هين أي سهل (sihah)؛ هان الأمر على فلان: سهل؛ هو علي هين؛ وهو أهون عليه؛ وتحسبونه هينا (mufradat)؛ الهين: الأمر الهين وهو من الواو وقد مر (maqayis)
- **B003** küçümsenmeden doğan aşağılanma ve onur kaybı — aşağılanma, değersizlik ve güçsüzlük · küçümsenmeden doğan aşağılanma ve küçük düşürülme · değersizlik, küçük düşmüşlük ve güçsüzlük · insanlarca değersiz ve saygıya layık görülmeyen · onu aşağılayıp küçük düşürmek · onu hor görüp değersiz saymak · onu küçümseyerek önemsememek · aşağılayıcı ve küçük düşürücü ceza · aşağılayan ve küçük düşüren
  الهون هوان الشيء الحقير؛ الهين الذي لا كرامة له؛ أهنت فلانا وتهاونت به واستهنت به (ayn)؛ الهون بالضم: الهوان؛ أهانه: استخف به؛ الهوان والمهانة؛ ذل وضعف؛ استهان به وتهاون به: استحقره (sihah)؛ الهوان من جهة متسلط مستخف به؛ عذاب الهون؛ عذاب مهين؛ من يهن الله (mufradat)؛ الهون: الهوان (maqayis)
- **B004** içinde ya da kendisiyle dövme yapılan araç — içinde ya da kendisiyle dövme yapılan araç
  الهاون: الذي يدق فيه، معرب، وكان أصله هاوون (sihah)؛ الهاوون: فاعول من الهون، ولا يقال هارون (mufradat)؛ الهاوون للذي يدق به عربي صحيح كأنه فاعول من الهون (maqayis)

## ECHO ب ل ي (root_000154) — for ٱبْتَلَىٰهُ (w4): withheld observed target; not identity

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

## ECHO ق ل ل (root_001251) — for فَيَقُولُ (w8): withheld observed target; not identity

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

## ECHO ر ب و (root_000537) — for رَبِّىٓ (w9): withheld observed target; not identity

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

## ECHO م ه ن (root_001453) — for أَهَٰنَنِ (w10): withheld observed target; not identity

- **B001** değersizlik, güçsüzlük ve azlık — değersiz, güçsüz ve yetersiz · değersizlik ve azlık · güçsüz kimseler
  أصل صحيح يدل على احتقار وحقارة في الشيء (maqayis)؛ مهين أي حقير (maqayis;sihah)؛ رجل مهين أي حقير ضعيف (ayn;tahdhib)؛ المهانة الحقارة (maqayis)؛ المهانة وهي القلة (tahdhib)
- **B002** hizmet etme veya işte ustalık — hizmet; işte ustalık · onlara hizmet etti · hizmet eden kimse veya köle · kendi toprağında çalıştı · ailesine hizmet edip kendini onların işlerine verdi
  المهن الخدمة والمهنة (maqayis)؛ المهنة الخدمة (ayn;sihah;tahdhib)؛ المهنة الحذاقة في العمل ونحوه (ayn;tahdhib)؛ الماهن الخادم (maqayis;sihah)؛ الماهن العبد (ayn;tahdhib)؛ مهنهم أي خدمهم (ayn;tahdhib)؛ مهن القوم يمهنهم مهنة أي خدمهم (sihah)؛ إذا عمل في ضيعته (tahdhib)؛ هو في مهنة أهله وهو الخدمة والابتذال (tahdhib)
- **B003** giysiyi çekmek [kalıp] — giysiyi çekti · çekilmiş giysi
  مهنت الثوب جذبته وثوب ممهون (maqayis)
- **B004** develeri sağmak, özellikle dönüş vaktinde [kalıp] — develeri dönüş vaktinde sağdı
  مهنت الإبل حلبتها (maqayis)؛ مهنت الإبل أمهنها إذا جلبتها عند الصدر (ayn)؛ مهنت الإبل مهنة إذا حليتها عن الصدر (sihah)؛ مهنت الإبل مهنة إذا حلبها عند الصدر (tahdhib)
- **B005** kullanıma koşup yıpratma veya güçten düşürme — onu kullanıp değerden düşürdü · onu güçsüzleştirdi · kendini hizmet için kullandı · var olan koşu gücünü sonuna kadar kullandı ve tüketti · ailesine hizmet edip kendini onların işlerine verdi
  امتهنت الشئ ابتذلته (sihah)؛ أمهنته أضعفته (sihah)؛ امتهن نفسه أي مستخدم (tahdhib)؛ هو في مهنة أهله وهو الخدمة والابتذال (tahdhib)؛ أخرج ما عنده من العدو وابتذله (tahdhib)
- **B006** üreme sıvısı yetersiz olduğu için dölleyemeyen — üreme sıvısı az ve güçsüz olduğu için dölleyemeyen erkek hayvan
  للفحل من الإبل والغنم إذا لم يلقح من مائه مهين (tahdhib)؛ من ماء قليل ضعيف (tahdhib)

## ECHO و ه ن (root_001687) — for أَهَٰنَنِ (w10): withheld observed target; not identity

- **B001** gücün veya kararlılığın azalması ya da azaltılması — güçsüzlük; zayıflık · güçsüzleşmek; zayıflamak · onu güçsüzleştirmek · gücünü azaltmak; zayıflatmak · güçsüzleştirme · güçsüz; gevşek · güçsüzleşmiş; bedence zayıflamış · güçsüzlük üstüne güçsüzlük; giderek artan güçsüzlük · düzenin etkisini kıran; düzeni zayıflatan
  وهن الشيء يهن وهنا: ضعف، وأوهنته أنا (maqayis)؛ الوهن الضعف في العمل وفي الأشياء وكذلك في العظم ونحوه (ayn;tahdhib)؛ الوهن: الضعف، وقد وهن الإنسان ووهنه غيره، يتعدى ولا يتعدى (sihah)؛ فما فتروا وما جبنوا عن قتال عدوهم (tahdhib)؛ الوهن: ضعف من حيث الخلق أو الخلق، موهن كيد الكافرين (mufradat)
- **B002** gecenin ortası dolaylarında geçen saat — gecenin ortası dolaylarında geçen saat · gecenin ortası dolaylarındaki saat · gecenin o saatine girdi veya o saatte yol aldı · ona gecenin o saatinde rastladım
  الوهن الموهن: ساعة تمضي من الليل، وأوهن الرجل: صار أو سار في تلك الساعة (maqayis)؛ الوهن: نحو من نصف الليل، والموهن مثله، هو حين يدبر الليل، وقد أوهنا: صرنا في تلك الساعة (sihah)؛ الموهن والوهن: نحو من نصف الليل، أوهن الرجل: دخل في ساعة من الليل (tahdhib)
- **B003** alt kaburga, omuz damarı ya da devenin köprücük kemiği — en kısa ya da en alttaki kaburga · omuz bağı altından omuza uzanan damar veya bölge · devenin iki köprücük kemiği
  الواهنة: القصيري من الأضلاع، وهي أسفلها (maqayis;sihah)؛ الواهن: عرق مستبطن حبل العاتق إلى الكتف (tahdhib)؛ الواهنتان: عظمان في ترقوة البعير، والترقوة من البعير: الواهنة (tahdhib)
- **B004** boyun yanı, üst kol veya omuz başındaki özel ağrı — boyun yanı, üst kol veya omuz başındaki özel ağrı · bu özel ağrıya tutulmuş · omuz çevresindeki özel ağrıdan etkilenmiş
  الواهنة: داء يصيب الإنسان في أخدعيه (maqayis)؛ الواهنة: مرض يأخذ في عضد الرجل (tahdhib)؛ به واهنة، وإنه ليشتكي واهنته، أوهنه الله فهو موهون (tahdhib)
- **B005** az hareketli, ağır ve ağırdan alan kadın — az hareketli, kalkıp oturması ağır, ağırdan alan ve işe üşenen kadın
  الوهنانة: المرأة القليلة الحركة، الثقيلة القيام والقعود (maqayis)؛ امرأة وهنانة: فيها فتور وأناة (sihah)؛ الوهنانة من النساء: الكسلى عن العمل تنعما، التي فيها فترة (tahdhib)
- **B006** yoğun deve topluluğu [kalıp] — yoğun deve topluluğu
  الوهن من الإبل: الكثيف (sihah)
- **B007** ücretli işçinin yanında durup onu çalışmaya teşvik eden kişi — ücretli işçinin yanında durup onu çalışmaya teşvik eden kişi
  الوهين بلغة أهل مضر: رجل يكون مع الأجير في العمل يحثه على العمل (tahdhib)
- **B008** mazeret için uydurulan boş söz [kalıp] — bahane olsun diye asılsız sözler söyledi
  كان وكان وهن بذي هنات، إذا قال كلاما باطلا يتعلل به (tahdhib)
- **B009** leş yiyip ağırlaşarak havalanamama [kalıp] — kuşun leş yiyip ağırlaşması ve havalanamaması
  يقال للطائر إذا ثقل من أكل الجيف فلم يقدر على النهوض: قد توهن توهنا (tahdhib)

===== _commentary/v16/out/s089/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 89:16, and ## Buluşmalar) =====
## Su: fışkıran, taşan, yukarıdan dökülen

İlk kelimenin kökü, karanlıktan önce suyun yarılmasını anlatır: {ar:انفجر الماء انفجارا تفتح, tr:infecera'l-mâu'nficâran tefettah, gloss:su fışkırdı, önü açıldı, source:"ف ج ر,B001"}. Fışkırma şöyle tarif edilir: {ar:إذا انبعث سائلا, tr:ize'nbe'ase sâilen, gloss:akarak fırladığında, source:"ف ج ر,B001"}. Kaya ya da toprak bir noktada çatlar, içerideki su bastırarak dışarı fırlar ve akmaya başlar. Kur'an bu sahneyi taşın içinden kurar. İsrailoğullarına kalplerinin taştan da katı olduğu söylenirken bazı taşlardan ırmakların fışkırdığı hatırlatılır: {ar:وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ, tr:ve inne mine'l-hicârati lemâ yetefecceru minhu'l-enhâr, gloss:taşların öylesi var ki içinden ırmaklar fışkırır, source:2:74}. Nuh'un tufanında aynı fiil yeryüzünü kaynaklara çevirir ve su ölçüsü önceden belirlenmiş bir iş üzerinde buluşur: {ar:وَفَجَّرْنَا ٱلْأَرْضَ عُيُونًۭا فَٱلْتَقَى ٱلْمَآءُ عَلَىٰٓ أَمْرٍۢ قَدْ قُدِرَ, tr:ve feccernâ'l-arda uyûnen fe'lteka'l-mâu alâ emrin kad kudir, gloss:yeri kaynaklar hâlinde fışkırttık, su takdir edilmiş bir iş üzerinde buluştu, source:54:12}. Kıyamette denizler fışkırtılır: {ar:وَإِذَا ٱلْبِحَارُ فُجِّرَتْ, tr:ve ize'l-bihâru fuccirat, gloss:denizler fışkırtıldığında, source:82:3}. Mekke'de inkârcılar Peygamber'den, arasından ırmaklar fışkırttığı bir bahçe isterler {source:17:91}. Kur'an bu işi cennette Allah'ın kullarına verir: {ar:عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا, tr:aynen yeşrabu bihâ ibâdu'llâhi yufeccirûnehâ tefcîrâ, gloss:Allah'ın kullarının içtiği, dilediklerince fışkırttıkları bir kaynak, source:76:6}.

Aynı kök günahı da adlandırır: {ar:الانبعاث والتفتح في المعاصي فجورا, tr:el-inbi'âsu ve't-tefettuhu fi'l-me'âsî fucûrâ, gloss:günahlara atılmak ve açılmak, fücur, source:"ف ج ر,B004"}. Suyun önünü yarıp fırlaması ile insanın günaha açılıp atılması aynı kelimeyle söylenir. Bu yüzden surenin geçmiş kavimleri anlatan bölümü bir sel gibi duyulur.

Dokuzuncu ayette Semûd kayayı vadide oymuştur: {ar:بِٱلْوَادِ, tr:bi'l-vâd, gloss:vadide, source:89:9}. Vadi selin yoludur: {ar:كل مفرج بين جبال وآكام وتلال يكون مسلكا للسيل, tr:kullu mufracin beyne cibâlin ve âkâmin ve tilâlin yekûnu meslekan li's-seyl, gloss:dağlar, tepeler ve tümsekler arasında selin geçtiği her açıklık, source:"و د ي,B005"}. Kök akmayı adlandırır: {ar:ودى أي سال, tr:vedâ ey sâl, gloss:aktı, source:"و د ي,B001"}. Kaya evler suyun indiği yatağa kurulmuştur. Kur'an'ın sel benzetmesinde vadiler kendi ölçüleri kadar akar ve sel kabarık bir köpük taşır: {ar:فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا فَٱحْتَمَلَ ٱلسَّيْلُ زَبَدًۭا رَّابِيًۭا, tr:fe-sâlet evdiyetun bi-kaderihâ fahtemele's-seylu zebeden râbiyâ, gloss:vadiler ölçülerince aktı, sel kabarık bir köpük taşıdı, source:13:17}. Köpük gider, insanlara yarayan yerde kalır. Âd da vadilerine doğru gelen bulutu yağmur sanmıştır. Hûd'un Ahkâf'ta kavmini uyarmasıyla başlayan sahnede {source:46:21} bulutu görünce şöyle derler: {ar:قَالُوا۟ هَٰذَا عَارِضٌۭ مُّمْطِرُنَا ۚ بَلْ هُوَ مَا ٱسْتَعْجَلْتُم بِهِۦ ۖ رِيحٌۭ فِيهَا عَذَابٌ أَلِيمٌۭ, tr:kâlû hâzâ âridun mumtırunâ, bel huve me'sta'celtum bih, rîhun fîhâ azâbun elîm, gloss:"Bu bize yağmur getiren bir bulut" dediler. Hayır, o acele istediğiniz şeydir: içinde acı bir azap olan bir rüzgâr, source:46:24}.

On birinci ayetin fiili suyun taşmasıdır: {ar:ٱلَّذِينَ طَغَوْا۟ فِى ٱلْبِلَٰدِ, tr:ellezîne tağav fi'l-bilâd, gloss:o ülkelerde azanlar, source:89:11}. Arapçada sel için {ar:طغى السيل إذا جاء بماء كثير, tr:tağa's-seylu izâ câe bi-mâin kesîr, gloss:sel bol suyla gelince "taştı" denir, source:"ط غ ي,B002"}, su için de {ar:طغى الماء خروجه عن المقدار, tr:tuğyânu'l-mâi hurûcuhû ani'l-mikdâr, gloss:suyun taşması ölçüsünden çıkmasıdır, source:"ط غ ي,B002"} denir. Ayette anlam azgınlıktır. Yanında ölçüsünden çıkan, yatağını aşan su duyulur. Kur'an kelimeyi tufan için doğrudan kullanır: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tağa'l-mâu hamelnâkum fi'l-câriye, gloss:su taştığında sizi akıp giden gemide taşıdık, source:69:11}. On ikinci ayet taşkının sonucunu verir: {ar:فَأَكْثَرُوا۟ فِيهَا ٱلْفَسَادَ, tr:fe-ekserû fîhe'l-fesâd, gloss:oralarda bozgunu çoğalttılar, source:89:12}. Çoğalmak {ar:الكثرة نماء العدد, tr:el-kesretu nemâu'l-aded, gloss:çokluk, sayının büyümesidir, source:"ك ث ر,B001"} demektir, bozulmak da {ar:الفساد خروج الشيء عن الاعتدال, tr:el-fesâdu hurûcu'ş-şey'i ani'l-i'tidâl, gloss:fesat, bir şeyin dengeden çıkmasıdır, source:"ف س د,B001"}. Hacim büyür ve şeyler dengelerinden çıkar. Bozgunun tarifindeki "çıkış" suyun ölçüden çıkışıyla aynı kelimedir. Kur'an'da bozgun karaya ve denize yayılır: {ar:ظَهَرَ ٱلْفَسَادُ فِى ٱلْبَرِّ وَٱلْبَحْرِ, tr:zahera'l-fesâdu fi'l-berri ve'l-bahr, gloss:karada ve denizde bozgun ortaya çıktı, source:30:41}. Salih de Semûd'a, Âd'dan sonra yerleştirildikleri yeryüzünde ovalardan saraylar edinip dağları ev diye oyduklarını hatırlatır ve sonra şöyle der: {ar:وَلَا تَعْثَوْا۟ فِى ٱلْأَرْضِ مُفْسِدِينَ, tr:ve lâ ta'sev fi'l-ardı mufsidîn, gloss:yeryüzünde bozguncular olarak dolaşmayın, source:7:74}.

On üçüncü ayet taşkına yukarıdan karşılık verir: {ar:فَصَبَّ عَلَيْهِمْ رَبُّكَ سَوْطَ عَذَابٍ, tr:fe-sabbe aleyhim rabbuke savte azâb, gloss:Rabbin de üzerlerine azap kamçısı yağdırdı, source:89:13}. Sabb, suyun fiilidir: {ar:صب الماء إراقته من أعلى, tr:sabbu'l-mâi irâkatuhû min a'lâ, gloss:suyu dökmek, onu yukarıdan akıtmaktır, source:"ص ب ب,B001"}. Vadiye inmek de bu fiille söylenir: {ar:صب في الوادي إذا انحدر فيه, tr:sabbe fi'l-vâdî izenhadera fîh, gloss:vadiye indi, oraya doğru aktı, source:"ص ب ب,B002"}. Aşağıda yatağını taşan suya yukarıdan dökülen bir şey karşılık verir. Dökülenin adı azaptır ve bu kelimenin harfleri tatlı suyu da adlandırır: {ar:العذب ضد الملح وكل مستسيغ من طعام أو شراب, tr:el-azbu diddu'l-milhi ve kullu mustesâğin min taâmin ev şarâb, gloss:azb, tuzlunun zıddıdır; boğazdan rahat geçen her yiyecek ve içecek, source:"ع ذ ب,B001"}. Âd'ın yağmur sandığı rüzgâr bu iki yüzü tek sahnede gösterir: beklenen tatlı su, gelen ise azaptır {source:46:24}.

Aynı su sahnesi surenin ikinci yarısında rahmet olarak döner. Kur'an insana yemeğine bakmasını söyler: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:suyu bol bol döktük, source:80:25}, {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:summe şekakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26}. Fiil aynıdır, ama bu kez arkasından yarılan toprak ve biten yemek gelir. Surenin sınav sahnesindeki kelimeler bu yağmuru da taşır. İkram için {ar:كرم السحاب أتى بالغيث, tr:keruma's-sehâbu etâ bi'l-ğays, gloss:bulut cömert davrandı, yağmur getirdi, source:"ك ر م,B002"} denir. Rızık için {ar:وقد يسمى المطر رزقا, tr:ve kad yusemma'l-mataru rızkâ, gloss:yağmura da rızık denir, source:"ر ز ق,B003"} denir. Kur'an da şöyle der: {ar:وَفِى ٱلسَّمَآءِ رِزْقُكُمْ, tr:ve fi's-semâi rızkukum, gloss:rızkınız göktedir, source:51:22}. Ölçü için de {ar:ينزل المطر بمقدار, tr:yenzilu'l-mataru bi-mikdâr, gloss:yağmur ölçüyle iner, source:"ق د ر,B001"} denir. On altıncı ayette rızkın daraltılması, yağmurun ölçüyle inmesinin insanın gözünden görünen yüzüdür. Yirmi dördüncü ayetteki "hayatım" kelimesinin yanında yağmur duyulur: {ar:الحيا المطر لأنه يحيي الأرض بعد موتها, tr:el-hayâ el-mataru li-ennehû yuhyi'l-arda ba'de mevtihâ, gloss:hayâ yağmurdur, çünkü yeri ölümünden sonra diriltir, source:"ح ي ي,B002"}. Yirmi sekizinci ayetteki "dön" kelimesinin yanında da dökülüp yeniden gelen yağmur duyulur: {ar:الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث, tr:er-rec'u el-ğaysu ve huve'l-mataru li-ennehâ tuğîsu ve tasubbu summe terci'u fe-tuğîs, gloss:rec' yağmurdur, çünkü yağar, dökülür, sonra döner ve yine yağar, source:"ر ج ع,B006"}. Kur'an da göğe dönüşüyle yemin eder: {ar:وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ, tr:ve's-semâi zâti'r-rec', gloss:dönüp dönüp yağan göğe, source:86:11}. Ölü toprağa yağmur gönderilmesi, ölülerin çıkarılmasının örneğidir: {ar:كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ لَعَلَّكُمْ تَذَكَّرُونَ, tr:kezâlike nuhricu'l-mevtâ leallekum tezekkerûn, gloss:ölüleri de böyle çıkarırız; belki düşünüp hatırlarsınız, source:7:57}. Son kelime bu suyun ürününe varır: bahçeye ve bitkinin gürleşip çiçek açmasına: {ar:جن النبت جنونا إذا اشتد وخرج زهره, tr:cenne'n-nebtu cunûnen izeştedde ve harace zehruh, gloss:bitki gürleşip çiçeğini çıkarınca "cenne" denir, source:"ج ن ن,B011"}.

Surede suyun işleyişi bir ölçüye bağlanır. Ölçüsünde kalan su hayat verir, ölçüsünü aşan su süpürür. Âd, Semûd ve Firavun ölçüyü aşan taşkındır ve onlara yukarıdan azap dökülür. İnsana ölçülü rızık iner ve o, ölçünün kendisini aşağılanma sanır.

Kaynaklar: 89:1 وَٱلْفَجْرِ ف ج ر B001; 89:1 وَٱلْفَجْرِ ف ج ر B004; 89:9 بِٱلْوَادِ و د ي B001; 89:9 بِٱلْوَادِ و د ي B005; 89:11 طَغَوْا۟ ط غ ي B002; 89:12 فَأَكْثَرُوا۟ ك ث ر B001; 89:12 ٱلْفَسَادَ ف س د B001; 89:13 فَصَبَّ ص ب ب B001; 89:13 فَصَبَّ ص ب ب B002; 89:13 عَذَابٍ ع ذ ب B001; 89:15 فَأَكْرَمَهُۥ ك ر م B002; 89:16 فَقَدَرَ ق د ر B001; 89:16 رِزْقَهُۥ ر ز ق B003; 89:24 لِحَيَاتِى ح ي ي B002; 89:28 ٱرْجِعِىٓ ر ج ع B006; 89:30 جَنَّتِى ج ن ن B011

## Dikilen, oyulan ve yerle bir edilen

Üç kavim yaptıkları yapılarla anılır. Âd'ın şehri şöyle anılır: {ar:إِرَمَ ذَاتِ ٱلْعِمَادِ, tr:İrame zâti'l-imâd, gloss:sütunlar sahibi İrem, source:89:7}. İmâd, yükün dayandığı şeydir: {ar:الشيء الذي يسند إليه عماد, tr:eş-şey'u'llezî yusnedu ileyhi imâd, gloss:bir şeyin dayandırıldığı nesne imâddır, source:"ع م د,B003"}. Mermer sütunlar da bu adı taşır: {ar:العمد أساطين الرخام, tr:el-amed esâtînu'r-ruhâm, gloss:amed, mermer sütunlardır, source:"ع م د,B003"}. Ayetin kendisi yükseklik ya da yüksek yapı diye açıklanır: {ar:ذات العماد أي ذات الطول وقيل ذات البناء الرفيع, tr:zâtu'l-imâd ey zâtu't-tûl, ve kîle zâtu'l-binâi'r-refî', gloss:zâtu'l-imâd, yani boyu uzun; yüksek yapılı da denmiştir, source:"ع م د,B005"}. Başka bir kullanımda imâd çadır direğidir: {ar:أهل عمود وأهل عماد أصحاب الأخبية لا ينزلون غيرها, tr:ehlu amûdin ve ehlu imâdin ashâbu'l-ahbiyeti lâ yenzilûne ğayrahâ, gloss:direk ehli, çadırdan başka yerde konaklamayanlardır, source:"ع م د,B004"}. Taş sütun da olsa çadır direği de olsa sahne aynıdır: dik duran ve üstündeki ağırlığı taşıyan bir gövde. İrem adı da dikili bir taşı çağırır, çünkü Arapçada bu kelime çölde yol işareti olarak dikilen taşlar için kullanılır: {ar:الإرم حجارة تنصب علما في المفازة, tr:el-irem hicâratun tunsabu aleman fi'l-mefâze, gloss:irem, çölde işaret olarak dikilen taşlardır, source:"memory"}. Kur'an Âd'ın bu dikme tutkusunu Hûd'un ağzından anlatır: {ar:أَتَبْنُونَ بِكُلِّ رِيعٍ ءَايَةًۭ تَعْبَثُونَ, tr:e-tebnûne bi-kulli rî'in âyeten ta'besûn, gloss:her yüksek yere oyun olsun diye bir nişan mı dikiyorsunuz, source:26:128}, {ar:وَتَتَّخِذُونَ مَصَانِعَ لَعَلَّكُمْ تَخْلُدُونَ, tr:ve tettehızûne mesânia leallekum tahludûn, gloss:sanki ölümsüz kalacakmışsınız gibi yapılar ediniyorsunuz, source:26:129}. Âd'ın kendi sözü de şuydu: {ar:مَنْ أَشَدُّ مِنَّا قُوَّةً, tr:men eşeddu minnâ kuvveh, gloss:bizden daha güçlü kim var, source:41:15}. Gökleri ise Allah sütunsuz yükseltir: {ar:ٱللَّهُ ٱلَّذِى رَفَعَ ٱلسَّمَٰوَٰتِ بِغَيْرِ عَمَدٍۢ تَرَوْنَهَا, tr:Allâhu'llezî refe'a's-semâvâti bi-ğayri amedin teravnehâ, gloss:Allah, gökleri görebileceğiniz sütunlar olmadan yükselten, source:13:2}. İnsanın yükselttiği şey sütuna muhtaçtır. Sütun yıkılınca yükseklik de gider.

Sekizinci ayet şöyledir: {ar:ٱلَّتِى لَمْ يُخْلَقْ مِثْلُهَا فِى ٱلْبِلَٰدِ, tr:elletî lem yuhlak misluhâ fi'l-bilâd, gloss:ülkelerde benzeri yaratılmamış olan, source:89:8}. Halk, önceden örneği olmayan bir şeyi meydana getirmektir: {ar:الخلق ابتداع الشيء على مثال لم يسبق إليه, tr:el-halku ibtidâu'ş-şey'i alâ misâlin lem yusbak ileyh, gloss:halk, bir şeyi daha önce yapılmamış bir örneğe göre ortaya koymaktır, source:"خ ل ق,B002"}. Zanaatçının dilinde ise deriyi kesmeden önce ölçüp biçmektir: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme izâ kadertuhû kable'l-kat', gloss:deriyi kesmeden önce ölçtüm, source:"خ ل ق,B001"}. Ayetteki "benzer" kelimesinin kökü iki zıt duruşu birden taşır. Biri {ar:مثل الرجل قائما انتصب, tr:mesele'r-raculu kâimen intesab, gloss:adam ayağa dikildi, source:"م ث ل,B005"}, öteki {ar:مثل أي لطأ بالأرض وهو من الأضداد, tr:mesele ey lati'e bi'l-ard, ve huve mine'l-addâd, gloss:yere yapıştı; bu, zıt anlamlı kelimelerdendir, source:"م ث ل,B006"}. Silinmiş iz de bu köktendir: {ar:الماثل الدارس, tr:el-mâsil ed-dâris, gloss:mâsil, silinip gitmiş olandır, source:"م ث ل,B006"}. Ayette anlam "benzeri"dir. Yanında, dikilip duran yapı ile yere serilmiş yıkıntı aynı harflerde duyulur. Halk kökü de yerle bir olmuş izi adlandırır: {ar:رسم مخلولق إذا استوى بالأرض, tr:resmun mahlevlik izestevâ bi'l-ard, gloss:yerle bir olmuş harabe izi, source:"خ ل ق,B008"}. Benzersiz diye anılan şehir, benzerliği anlatan kelimenin içinde hem ayakta hem yerde durur.

Dokuzuncu ayet Semûd'u bir oyma işiyle anar: {ar:وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ, tr:ve Semûde'llezîne câbu's-sahra bi'l-vâd, gloss:ve vadide kayaları oyan Semûd, source:89:9}. Cevb, oymak ve kazmaktır: {ar:اجتاب احتفر, tr:ictâbe ihtefer, gloss:oydu, kazdı, source:"ج و ب,B001"}. Ölçüsü bir gömleğin yaka deliğidir: {ar:قطعك الشيء كما يجاب الجيب, tr:kat'uke'ş-şey'e kemâ yucâbu'l-ceyb, gloss:bir şeyi, yaka deliği açar gibi kesmen, source:"ج و ب,B001"}. Kaya da sıradan bir taş değildir: {ar:الصخر عظام الحجارة وصلابها, tr:es-sahru izâmu'l-hicâreti ve sılâbuhâ, gloss:sahr, taşların iri ve sert olanlarıdır, source:"ص خ ر,B001"}. Kumaşa yaka açar gibi en sert kayaya kapı açmak: işin inceliği ile malzemenin sertliği aynı cümlede yer alır. Beşinci ayetteki hicr kelimesi burada ikinci kez duyulur: {ar:الحجر منازل ثمود, tr:el-hicru menâzilu Semûd, gloss:Hicr, Semûd'un yurdudur, source:"ح ج ر,B004"}. Aynı kelimenin bir anlamı da taşın kendisidir: {ar:الحجر الجوهر الصلب المعروف, tr:el-hacer el-cevheru's-sulbu'l-ma'rûf, gloss:hacer, bilinen sert maddedir, source:"ح ج ر,B003"}. Kur'an Hicr halkını, elçileri yalanlayan {source:15:80} ve dağlardan güven içinde ev oyan bir topluluk olarak anlatır: {ar:وَكَانُوا۟ يَنْحِتُونَ مِنَ ٱلْجِبَالِ بُيُوتًا ءَامِنِينَ, tr:ve kânû yenhitûne mine'l-cibâli buyûten âminîn, gloss:dağlardan güven içinde evler oyarlardı, source:15:82}. Sonları bir sabah vakti gelir: {ar:فَأَخَذَتْهُمُ ٱلصَّيْحَةُ مُصْبِحِينَ, tr:fe-ehazet'humu's-sayhatu musbihîn, gloss:sabaha girerlerken onları o korkunç ses yakaladı, source:15:83}. Salih'in Semûd'a sözü de aynı işi anar {source:7:74}. Semûd'un sonu, yurtlarında yere yapışıp kalmaktır: {ar:فَأَصْبَحُوا۟ فِى دَارِهِمْ جَٰثِمِينَ, tr:fe-asbehû fî dârihim câsimîn, gloss:yurtlarında diz üstü çökmüş olarak sabahladılar, source:7:78}.

Onuncu ayet şöyledir: {ar:وَفِرْعَوْنَ ذِى ٱلْأَوْتَادِ, tr:ve Fir'avne zi'l-evtâd, gloss:ve kazıklar sahibi Firavun, source:89:10}. Kazık, yere çakılıp bir şeyi yerinde tutan dikmedir. Kur'an Firavun'un bir başka yapısını da anlatır. Firavun Hâmân'dan çamuru ateşte pişirip kendisine bir kule yapmasını ister ki Musa'nın ilahına çıkıp baksın: {ar:فَأَوْقِدْ لِى يَٰهَٰمَٰنُ عَلَى ٱلطِّينِ فَٱجْعَل لِّى صَرْحًۭا, tr:fe-evkıd lî yâ Hâmânu ale't-tîni fec'al lî sarhâ, gloss:ey Hâmân, benim için çamurun üstünde ateş yak ve bana bir kule yap, source:28:38}. Kur'an Firavun'un kazıklarının karşısına kendi kazıklarını koyar: {ar:وَٱلْجِبَالَ أَوْتَادًۭا, tr:ve'l-cibâle evtâdâ, gloss:ve dağları kazıklar, source:78:7}. Firavun "kazıklar sahibi" sıfatıyla yalanlayan kavimler arasında da sayılır {source:38:12}.

On birinci ayetin fiili, sudan sonra yüksekliği de taşır: {ar:الطغية أعلى الجبل, tr:et-tağye a'le'l-cebel, gloss:tağye, dağın en yüksek yeridir, source:"ط غ ي,B005"}, {ar:كل مكان مرتفع طغوة, tr:kullu mekânin murtefiin tağve, gloss:her yüksek yer tağvedir, source:"ط غ ي,B005"}. Azgınlık, sınırın üstüne çıkmaktır. Kur'an bunu Firavun'da gösterir: {ar:إِنَّ فِرْعَوْنَ عَلَا فِى ٱلْأَرْضِ, tr:inne Fir'avne alâ fi'l-ard, gloss:Firavun yeryüzünde yükseldi, source:28:4}. Firavun'un iddiası da şudur: {ar:أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:ene rabbukumu'l-a'lâ, gloss:en yüce rabbiniz benim, source:79:24}. Aynı şeyi insanda da gösterir: {ar:كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ, tr:kellâ inne'l-insâne le-yatğâ, gloss:hayır, insan gerçekten azar, source:96:6}, {ar:أَن رَّءَاهُ ٱسْتَغْنَىٰٓ, tr:en raâhu'staşnâ, gloss:kendini ihtiyaçsız gördüğü için, source:96:7}.

Yirmi birinci ayet bütün bu dikili şeylere cevap verir: {ar:كَلَّآ إِذَا دُكَّتِ ٱلْأَرْضُ دَكًّۭا دَكًّۭا, tr:kellâ izâ dukketi'l-ardu dekken dekkâ, gloss:hayır, yer dövüldükçe dövülüp düzlendiğinde, source:89:21}. Dekk, bir duvarı ya da dağı kırmaktır: {ar:الدك كسر الحائط والجبل, tr:ed-dekku kesru'l-hâiti ve'l-cebel, gloss:dekk, duvarı ve dağı kırmaktır, source:"د ك ك,B001"}. Kırmanın ölçüsü de yerle aynı hizaya gelmektir: {ar:ضربته وكسرته حتى سويته بالأرض, tr:darabtuhû ve kesertuhû hattâ sevveytuhû bi'l-ard, gloss:onu vurup kırdım, sonunda yerle bir ettim, source:"د ك ك,B001"}. Sonunda yer, hörgücü olmayan bir deve gibi düzleşir: {ar:أرض دكاء مسواة وناقة دكاء لا سنام لها, tr:ardun dekkâu musevvâtun ve nâkatun dekkâu lâ senâme lehâ, gloss:dekkâ yer düzlenmiş yerdir; dekkâ deve hörgücü olmayan devedir, source:"د ك ك,B002"}. Kur'an bu fiili üç sahnede kullanır. Musa Rabbini görmek ister, Rabbi dağa tecelli eder ve onu dümdüz eder: {ar:جَعَلَهُۥ دَكًّۭا وَخَرَّ مُوسَىٰ صَعِقًۭا, tr:cealehû dekkan ve harra Mûsâ sa'ikâ, gloss:dağı dümdüz etti, Musa da bayılıp yere düştü, source:7:143}. Zülkarneyn demirden seddini bitirince bunun Rabbinden bir rahmet olduğunu, Rabbinin vaadi gelince onu dümdüz edeceğini söyler: {ar:فَإِذَا جَآءَ وَعْدُ رَبِّى جَعَلَهُۥ دَكَّآءَ, tr:fe-izâ câe va'du rabbî cealehû dekkâ', gloss:Rabbimin vaadi gelince onu dümdüz eder, source:18:98}. Kıyamette de yer ve dağlar kaldırılıp tek bir darbeyle ezilir: {ar:وَحُمِلَتِ ٱلْأَرْضُ وَٱلْجِبَالُ فَدُكَّتَا دَكَّةًۭ وَٰحِدَةًۭ, tr:ve humileti'l-ardu ve'l-cibâlu fe-dukketâ dekketen vâhideh, gloss:yer ve dağlar kaldırılıp tek bir darbeyle ezildiğinde, source:69:14}. Dağlar sorulduğunda verilen cevap, onların dümdüz bir alana çevrileceğidir: {ar:فَيَذَرُهَا قَاعًۭا صَفْصَفًۭا, tr:fe-yezeruhâ kâ'an safsafâ, gloss:yerlerini dümdüz bir ova olarak bırakır, source:20:106}, {ar:لَّا تَرَىٰ فِيهَا عِوَجًۭا وَلَآ أَمْتًۭا, tr:lâ terâ fîhâ ivecen ve lâ emtâ, gloss:orada ne bir çukur ne bir tümsek görürsün, source:20:107}. Sütunlar, kaya evler, kazıklar ve kuleler bu düzlükte ayrı ayrı durmaz. Hepsi dikildikleri zeminle bir olur. Kur'an Âd'ın sonunu devrilmiş hurma kütükleriyle gösterir: {ar:كَأَنَّهُمْ أَعْجَازُ نَخْلٍ خَاوِيَةٍۢ, tr:keennehum a'câzu nahlin hâviyeh, gloss:sanki içi boş hurma kütükleri gibi, source:69:7}. Sütun gibi dikilmiş gövdeler artık yerde yatmaktadır.

Yirmi ikinci ayetteki saf kelimesi bu düzlüğün adını verir: {ar:الصفصف المستوي من الأرض كأنه على صف واحد, tr:es-safsaf el-mustevî mine'l-ard, keennehû alâ saffin vâhid, gloss:safsaf, sanki tek bir saf üzerindeymiş gibi dümdüz olan yerdir, source:"ص ف ف,B005"}.

Alçalmanın iki yolu vardır. Yukarı çıkan zorla indirilir, ama surede kendiliğinden alçalan da vardır. On altıncı ayette insan şöyle der: {ar:رَبِّىٓ أَهَٰنَنِ, tr:rabbî ehânen, gloss:Rabbim beni aşağıladı, source:89:16}. Hevân, değersiz kılınmaktır: {ar:الهون هوان الشيء الحقير, tr:el-hûn hevânu'ş-şey'i'l-hakîr, gloss:hûn, değersiz şeyin düşüklüğüdür, source:"ه و ن,B003"}. Aynı kök yeryüzünde alçakgönüllü yürüyüşü de adlandırır: {ar:يمشي على الأرض هونا, tr:yemşî ale'l-ardı hevnâ, gloss:yeryüzünde yumuşak, alçakgönüllü yürür, source:"ه و ن,B001"}. Kur'an Rahman'ın kullarını böyle tanıtır: {ar:وَعِبَادُ ٱلرَّحْمَٰنِ ٱلَّذِينَ يَمْشُونَ عَلَى ٱلْأَرْضِ هَوْنًۭا, tr:ve ibâdu'r-rahmâni'llezîne yemşûne ale'l-ardı hevnâ, gloss:Rahman'ın kulları yeryüzünde alçakgönüllülükle yürüyenlerdir, source:25:63}. Yirmi yedinci ayetteki mutmainne kelimesi alçak yeri ve eğilmiş sırtı taşır: {ar:المطمئن من الأرض أرض منخفضة, tr:el-mutmainnu mine'l-ard ardun munhafida, gloss:yerin mutmain olanı, alçak yerdir, source:"ط م ء ن,B002"}, {ar:طامن ظهره إذا حناه, tr:tâmene zahrahû izâ henâh, gloss:sırtını eğdi, source:"ط م ء ن,B002"}. Yirmi dokuzuncu ayetteki kullar da çiğnenip düzleşmiş yolun köküyle anılır: {ar:الطريق المعبد وهو المسلوك المذلل, tr:et-tarîku'l-muabbed ve huve'l-meslûku'l-muzellel, gloss:muabbed yol, çok yürünüp düzleşmiş yoldur, source:"ع ب د,B005"}. Dümdüz edilen yer ile düzleşmiş yol arasındaki fark, düzlüğün nasıl geldiğindedir: biri kırılarak düzleşir, öteki yürünerek. Çağrı ikinciye yapılır.

Kaynaklar: 89:5 حِجْرٍ ح ج ر B003; 89:5 حِجْرٍ ح ج ر B004; 89:7 إِرَمَ ا ر م (memory); 89:7 ٱلْعِمَادِ ع م د B003; 89:7 ٱلْعِمَادِ ع م د B004; 89:7 ٱلْعِمَادِ ع م د B005; 89:8 يُخْلَقْ خ ل ق B001; 89:8 يُخْلَقْ خ ل ق B002; 89:8 يُخْلَقْ خ ل ق B008; 89:8 مِثْلُهَا م ث ل B005; 89:8 مِثْلُهَا م ث ل B006; 89:9 جَابُوا۟ ج و ب B001; 89:9 ٱلصَّخْرَ ص خ ر B001; 89:11 طَغَوْا۟ ط غ ي B005; 89:16 أَهَٰنَنِ ه و ن B001; 89:16 أَهَٰنَنِ ه و ن B003; 89:21 دُكَّتِ د ك ك B001; 89:21 دَكًّۭا د ك ك B002; 89:22 صَفًّۭا ص ف ف B005; 89:27 ٱلْمُطْمَئِنَّةُ ط م ء ن B002; 89:29 عِبَٰدِى ع ب د B005

## Kucak, ikram ve yetim

On beşinci ayet bir sınavla açılır: {ar:فَأَمَّا ٱلْإِنسَٰنُ إِذَا مَا ٱبْتَلَىٰهُ رَبُّهُۥ فَأَكْرَمَهُۥ وَنَعَّمَهُۥ, tr:fe-emme'l-insânu izâ me'btelâhu rabbuhû fe-ekramehû ve na''amehû, gloss:insan ise Rabbi onu sınayıp ikram ettiğinde ve nimet verdiğinde, source:89:15}. İbtilâ denemektir: {ar:بلوته بلوا جربته واختبرته, tr:belevtuhû belven carrabtuhû ve'htebertuh, gloss:onu denedim, sınadım, source:"ب ل و,B002"}. Allah'ın sınaması iki yolla olur: {ar:اختبار الله للعباد تارة بالمسار وتارة بالمضار, tr:ihtibâru'llâhi li'l-ibâdi târeten bi'l-mesârri ve târeten bi'l-medârr, gloss:Allah kullarını bazen sevindiren, bazen zarar veren şeylerle sınar, source:"ب ل و,B003"}. Kur'an bunu açıkça söyler: {ar:وَنَبْلُوكُم بِٱلشَّرِّ وَٱلْخَيْرِ فِتْنَةًۭ, tr:ve nebluküm bi'ş-şerri ve'l-hayri fitneh, gloss:sizi deneme olarak kötülükle de iyilikle de sınarız, source:21:35}. İsrailoğulları da iyiliklerle ve kötülüklerle sınanmıştır, belki dönerler diye {ar:وَبَلَوْنَٰهُم بِٱلْحَسَنَٰتِ وَٱلسَّيِّـَٔاتِ لَعَلَّهُمْ يَرْجِعُونَ, tr:ve belevnâhum bi'l-hasenâti ve's-seyyiâti leallehum yerci'ûn, gloss:belki dönerler diye onları iyiliklerle ve kötülüklerle sınadık, source:7:168}.

Sınayan "Rabbi"dir. Rab kökü bir şeyi aşama aşama büyütmeyi anlatır: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi olgunluğuna erinceye kadar hâlden hâle geçirerek yetiştirmektir, source:"ر ب ب,B002"}. Aynı kök üvey çocuğu da adlandırır: {ar:ربيب الرجل ابن امرأته, tr:rabîbu'r-racul ibnu'mraetih, gloss:adamın rebîbi, karısının oğludur, source:"ر ب ب,B005"}. Nimet vermek de bir babanın çocuklarına davranışıyla söylenir: {ar:نعم فلان أولاده ترفهم, tr:na''ame fulânun evlâdehû tarrafehum, gloss:çocuklarını bolluk içinde, nazla büyüttü, source:"ن ع م,B002"}. İkram eden de şöyle tarif edilir: {ar:الكثير الخير الجواد المنعم المفضل, tr:el-kesîru'l-hayri'l-cevâdu'l-mun'imu'l-mufdıl, gloss:hayrı bol, cömert, nimet veren, lütfeden, source:"ك ر م,B001"}. Ayetin yanında bir aile sahnesi duyulur: bir çocuk kucakta büyütülür, nazla beslenir ve el üstünde tutulur. Beşinci ayetin hicr kelimesi bu kucağın kendisini de adlandırır: {ar:حجر المرأة وحجرها حضنها, tr:hicru'l-mer'eti ve hacruhâ hıdnuhâ, gloss:kadının hicri kucağıdır, source:"ح ج ر,B005"}. Kur'an rab kökünü ve kucak kelimesini bir hükümde bir araya getirir: {ar:وَرَبَٰٓئِبُكُمُ ٱلَّٰتِى فِى حُجُورِكُم, tr:ve rebâibukumu'llâtî fî hucûrikum, gloss:kucaklarınızda büyüyen üvey kızlarınız, source:4:23}. Büyümüş çocuk anne babası için şöyle dua eder: {ar:رَّبِّ ٱرْحَمْهُمَا كَمَا رَبَّيَانِى صَغِيرًۭا, tr:rabbi'rhamhumâ kemâ rabbeyânî sağîrâ, gloss:Rabbim, onlar beni küçükken nasıl büyüttülerse sen de onlara öyle merhamet et, source:17:24}. Firavun ise Musa'ya büyütme hakkıyla gelir: {ar:أَلَمْ نُرَبِّكَ فِينَا وَلِيدًۭا, tr:e-lem nurabbike fînâ velîdâ, gloss:seni çocukken aramızda büyütmedik mi, source:26:18}.

İnsan bu bakımı bir rütbe olarak okur: {ar:فَيَقُولُ رَبِّىٓ أَكْرَمَنِ, tr:fe-yekûlu rabbî ekramen, gloss:"Rabbim bana ikram etti" der, source:89:15}. Darlıkta ise şöyle olur: {ar:فَقَدَرَ عَلَيْهِ رِزْقَهُۥ, tr:fe-kadera aleyhi rızkahû, gloss:rızkını daralttı, source:89:16}. Bu ifade şöyle açıklanır: {ar:ومن قدر عليه رزقه أي ضيق عليه, tr:ve men kudira aleyhi rızkuhû ey duyyika aleyh, gloss:rızkı daraltılan, yani darlığa sokulan, source:"ق د ر,B004"}. İnsan bu kez "Rabbim beni aşağıladı" der. Aşağılanmış kişi ikramdan yoksun olandır: {ar:الهين الذي لا كرامة له, tr:el-heyyinu'llezî lâ kerâmete leh, gloss:hîn, ikramı olmayandır, source:"ه و ن,B003"}. Aşağılanma bir otoritenin hor görmesiyle gelir: {ar:الهوان من جهة متسلط مستخف به, tr:el-hevânu min cihetin mutesallitin mustahiffin bih, gloss:hevân, onu hafife alan bir hükmedenden gelir, source:"ه و ن,B003"}. İnsan darlığı böyle okur, Rabbini kendisini hor gören bir efendi yerine koyar. Kur'an'da rızkın genişletilmesi ve daraltılması bir hüküm değil, Allah'ın dilemesidir. Bunu Kârûn'un yere geçirilişinden sonra, dün onun yerinde olmayı isteyenler söyler: {ar:وَيْكَأَنَّ ٱللَّهَ يَبْسُطُ ٱلرِّزْقَ لِمَن يَشَآءُ مِنْ عِبَادِهِۦ وَيَقْدِرُ, tr:veykeenna'llâhe yebsutu'r-rızka li-men yeşâu min ibâdihî ve yakdir, gloss:demek ki Allah rızkı kullarından dilediğine genişletiyor ve daraltıyormuş, source:28:82}. Rızkı daraltılana verilen hüküm de, Allah'ın verdiğinden harcamasıdır {ar:وَمَن قُدِرَ عَلَيْهِ رِزْقُهُۥ فَلْيُنفِقْ مِمَّآ ءَاتَىٰهُ ٱللَّهُ, tr:ve men kudira aleyhi rızkuhû fe'l-yunfik mimmâ âtâhu'llâh, gloss:rızkı daraltılan, Allah'ın kendisine verdiğinden harcasın, source:65:7}. Nimeti kendi bilgisine bağlayan insana Kur'an şöyle cevap verir: {ar:بَلْ هِىَ فِتْنَةٌۭ, tr:bel hiye fitneh, gloss:hayır, o bir sınavdır, source:39:49}.

On yedinci ayet bu okumayı kökünden çevirir: {ar:كَلَّا ۖ بَل لَّا تُكْرِمُونَ ٱلْيَتِيمَ, tr:kellâ, bel lâ tukrimûne'l-yetîm, gloss:hayır, asıl siz yetime ikram etmiyorsunuz, source:89:17}. Az önce insanın kendine alınan bir sıfat sandığı ikram, burada başkasına yapılan bir iş olur. Arapçada ikram cömertlikte yarışmak ve o yarışta öne geçmektir: {ar:كارمت الرجل إذا فاخرته في الكرم فكرمته إذا غلبته فيه, tr:kâramtu'r-racule izâ fâhartuhû fi'l-kerem fe-keremtuhû izâ ğalebtuhû fîh, gloss:cömertlikte yarıştım ve onu cömertlikte geçtim, source:"ك ر م,B006"}. İnsan bu yarışa hiç girmez. Yetim tam bu yerde durur. O, kucağı kalmamış çocuktur: {ar:انقطاع الصبي عن أبيه قبل بلوغه, tr:inkıtâu's-sabiyyi an ebîhi kable bulûğih, gloss:çocuğun ergenliğe ermeden babasından kopması, source:"ي ت م,B001"}. Kelimenin iki yan anlamı da onun durumunu anlatır: {ar:أصل اليتم الغفلة وبه يسمى اليتيم لأنه يتغافل عن بره, tr:aslu'l-yutmi'l-ğafle, ve bihî yusemma'l-yetîmu li-ennehû yutegâfelu an birrih, gloss:yetimliğin aslı gaflettir; yetime bu ad verilir, çünkü ona iyilik etmek ihmal edilir, source:"ي ت م,B003"}, {ar:اليتم الإبطاء ومنه أخذ اليتيم لأن البر يبطىء عنه, tr:el-yutmu'l-ibtâ', ve minhu ühıze'l-yetîmu li-enne'l-birra yubtıu anh, gloss:yutm gecikmedir; yetim adı buradan gelir, çünkü iyilik ona geç ulaşır, source:"ي ت م,B004"}. Rabbi tarafından nazla büyütülen insan, babasız çocuğa geç kalır. Kur'an Peygamber'e kendi yetimliğini hatırlatarak bu ilişkiyi kurar: {ar:أَلَمْ يَجِدْكَ يَتِيمًۭا فَـَٔاوَىٰ, tr:e-lem yecidke yetîmen fe-âvâ, gloss:seni yetim bulup barındırmadı mı, source:93:6}, {ar:فَأَمَّا ٱلْيَتِيمَ فَلَا تَقْهَرْ, tr:fe-emme'l-yetîme fe-lâ takhar, gloss:öyleyse yetimi ezme, source:93:9}. Barındırılmış olan barındırır. İkramın ölçüsü de verilir: {ar:إِنَّ أَكْرَمَكُمْ عِندَ ٱللَّهِ أَتْقَىٰكُمْ, tr:inne ekramekum inda'llâhi etkâkum, gloss:Allah katında en değerliniz, en takvalı olanınızdır, source:49:13}. Allah'ın aşağıladığını kimse yüceltemez: {ar:وَمَن يُهِنِ ٱللَّهُ فَمَا لَهُۥ مِن مُّكْرِمٍ, tr:ve men yuhini'llâhu fe-mâ lehû min mukrim, gloss:Allah kimi aşağılarsa onu yüceltecek kimse yoktur, source:22:18}. Cehennemdeki suçluya ise bu sıfat alay olarak söylenir: {ar:ذُقْ إِنَّكَ أَنتَ ٱلْعَزِيزُ ٱلْكَرِيمُ, tr:zuk inneke ente'l-azîzu'l-kerîm, gloss:tat bakalım, hani sen güçlüydün, değerliydin, source:44:49}.

Kaynaklar: 89:5 حِجْرٍ ح ج ر B005; 89:15 ٱبْتَلَىٰهُ ب ل و B002; 89:15 ٱبْتَلَىٰهُ ب ل و B003; 89:15 رَبُّهُۥ ر ب ب B002; 89:15 رَبُّهُۥ ر ب ب B005; 89:15 فَأَكْرَمَهُۥ ك ر م B001; 89:15 وَنَعَّمَهُۥ ن ع م B002; 89:16 فَقَدَرَ ق د ر B004; 89:16 أَهَٰنَنِ ه و ن B003; 89:17 تُكْرِمُونَ ك ر م B006; 89:17 ٱلْيَتِيمَ ي ت م B001; 89:17 ٱلْيَتِيمَ ي ت م B003; 89:17 ٱلْيَتِيمَ ي ت م B004

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

