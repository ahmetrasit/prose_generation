Focus: 88:8. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_8/D.r13/context.md =====
# 88:8 — focus

وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ

Anchor translation (canonical reading, reference only):

O gün yüzler rahattır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وُجُوهٌ | وَجْه | و ج ه | N |
| 2 | يَوْمَئِذٍ | يَوْمَئِذ |  | T |
| 3 | نَّاعِمَةٌ | نَّاعِمَة | ن ع م | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 88 — full text (context; no pericope)

- 88:1 هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ
- 88:2 وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ
- 88:3 عَامِلَةٌۭ نَّاصِبَةٌۭ
- 88:4 تَصْلَىٰ نَارًا حَامِيَةًۭ
- 88:5 تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
- 88:6 لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
- 88:7 لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
- 88:8 ◀ focus وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ
- 88:9 لِّسَعْيِهَا رَاضِيَةٌۭ
- 88:10 فِى جَنَّةٍ عَالِيَةٍۢ
- 88:11 لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ
- 88:12 فِيهَا عَيْنٌۭ جَارِيَةٌۭ
- 88:13 فِيهَا سُرُرٌۭ مَّرْفُوعَةٌۭ
- 88:14 وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ
- 88:15 وَنَمَارِقُ مَصْفُوفَةٌۭ
- 88:16 وَزَرَابِىُّ مَبْثُوثَةٌ
- 88:17 أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ
- 88:18 وَإِلَى ٱلسَّمَآءِ كَيْفَ رُفِعَتْ
- 88:19 وَإِلَى ٱلْجِبَالِ كَيْفَ نُصِبَتْ
- 88:20 وَإِلَى ٱلْأَرْضِ كَيْفَ سُطِحَتْ
- 88:21 فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ
- 88:22 لَّسْتَ عَلَيْهِم بِمُصَيْطِرٍ
- 88:23 إِلَّا مَن تَوَلَّىٰ وَكَفَرَ
- 88:24 فَيُعَذِّبُهُ ٱللَّهُ ٱلْعَذَابَ ٱلْأَكْبَرَ
- 88:25 إِنَّ إِلَيْنَآ إِيَابَهُمْ
- 88:26 ثُمَّ إِنَّ عَلَيْنَا حِسَابَهُم


===== _commentary/v16/work/88_8/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## و ج ه (root_001630) — identity root of وُجُوهٌ (w1)

- **B001** yüz ve bir şeyin öne bakan yanı — yüz; bir şeyin öne bakan veya görünen yanı · kötü bir yüz ifadesiyle bakmak
  الوجه مستقبل لكل شيء (maqayis); الوجه مستقبل كل شيء (ayn;tahdhib); وجه الإنسان وغيره معروف (jamhara); الوجه معروف (sihah); أصل الوجه الجارحة (mufradat)
- **B002** yön ve hedef; o yöne sevk etme veya yolu belli etme — yön, taraf · yönelinen yön veya hedef · bir şeyi belirli bir yöne çevirmek veya göndermek · tek bir yöne çevrilmiş · bir şeye doğru yönelmek · rüzgarın çakılı bir yöne sürüklemesi · yolu yürüyerek izini belirginleştirmek · perdeyi yırtacak bir yöne gitmek veya perdeyi yerinden kaldırmak
  الوجهة كل موضع استقبلته (maqayis); الجهة النحو (ayn;tahdhib); الوجهة القبلة وشبهها (ayn;tahdhib); ضل وجهة أمره إذا ضل قصده (jamhara); وجهته في حاجة ووجهت وجهي لله وتوجهت نحوك وإليك (sihah); وجهت الريح الحصا إذا ساقته ووجهوا للناس الطريق إذا وطئوه وسلكوه (tahdhib); للمقصد جهة ووجهة (mufradat)
- **B003** karşı karşıya gelme ve doğrudan yüzüne söyleme — birinin karşısına çıkmak, onunla yüz yüze gelmek · karşılaşma, yüzleşme · karşında, tam karşı tarafta
  واجهت فلانا جعلت وجهي تلقاء وجهه (maqayis;mufradat); الوجاه والتجاه ما استقبل شيء شيئا (ayn;tahdhib); المواجهة استقبالك الرجل بكلام (ayn;tahdhib); واجهت الرجل بكلام حسن أو قبيح (jamhara); المواجهة المقابلة وقعدت وجاهك أي قبالتك (sihah)
- **B004** yüzün varlığın kendisini temsil etmesi — 
  ربما عبر عن الذات بالوجه (maqayis); قيل ذاته وكل شيء هالك إلا هو (mufradat)
- **B005** amaç edinip yönelme; ibadette içtenlikle bağlanma — 
  وجهي إليك (maqayis); ضل وجهة أمره إذا ضل قصده (jamhara); وجهت وجهي لله سبحانه (sihah); الوجه الذي يؤتى منه وما أريد به الله وأخلصوا العبادة لله وأسلمت وجهي لله (mufradat)
- **B006** toplumsal itibar, yüksek mevki ve önde gelen kişi — topluluğun önderi · yerleşimin ileri gelenleri · itibarlı, yüksek mevkili · toplumsal itibar ve mevki · itibarlı ve yüksek mevkili olmak · onu itibarlı ve yüksek mevkili kılmak
  وجيه بين الجاه والجاه مقلوب (maqayis); وجوه القوم سادتهم ورجل وجيه عند السلطان (jamhara); صار وجيها أي ذا جاه وقدر ووجوه البلد أشرافه (sihah); جاه فيهم أي منزلة وقدر (tahdhib); فلان وجه القوم وفلان وجيه ذو جاه (mufradat)
- **B007** günün başı, ilk saatleri [kalıp] — günün başı, ilk saatleri
  وجه النهار أوله (jamhara); أتيته بوجه نهار وشباب نهار وصدر نهار أي في أوله (tahdhib); وجه النهار أي صدر النهار (mufradat)
- **B008** sözün veya işin doğru yönü ve ona uygun düzenleme — sözün amaçlanan yönü · doğru görüş · aklına bir görüş gelmek · bir şeyi doğru yolundan saptırmak · işi gerektiği gibi düzenleyip her şeyi yerine koymak · hiçbir işi doğru yapamayan ahmak; ayrıca tuvaletini yapmayı bile beceremeyen kişi
  وجه الكلام السبيل التي تقصدها به وصرفت الشيء عن وجهه أي عن سننه (jamhara); هذا وجه الرأي أي هو الرأي نفسه وأحمق ما يتوجه (sihah); دبر الأمر على وجهه الذي ينبغي وأحمق ما يتوجه أي ما يحسن أن يأتي الغائط (tahdhib); أحمق ما يتوجه أي لا يستقيم في أمر من الأمور (mufradat)
- **B009** yaşlanıp ömrünün son dönemine girmek — yaşlanıp ömrünün son dönemine girmek
  توجه الشيخ ولى وأدبر (maqayis); توجه الشيخ إذا ولى وكبر (sihah); إذا كبر سنه قد توجه (tahdhib)
- **B010** doğumda ellerin veya ön ayakların önce çıkması — elleri veya ön ayakları önce çıkan yavru · yavruyu elleri veya ön ayakları önce çıkacak biçimde doğurmak
  للمهر إذا خرجت يداه من الرحم وجيه (maqayis); للولد إذا خرجت يداه من الرحم أولا وجيه (sihah); أوجهت به أمه حين ولدته إذا خرج يداه أولا (tahdhib)
- **B011** kurucu uzun ünlü ile ana uyak harfi arasındaki harf — kurucu uzun ünlü ile ana uyak harfi arasındaki harf
  التوجيه هو الحرف الذي بين ألف التأسيس وبين القافية (sihah); الصاد توجيه بين التأسيس والقافية (tahdhib); التوجيه في الشعر الحرف الذي بين ألف التأسيس وحرف الروي (mufradat)
- **B012** hıyar veya kavunun altını kazıp yana yatırma — hıyar veya kavunun altını kazıp yana yatırma
  التوجيه أن تحفر تحت القثاءة أو البطيخة ثم تضجعها (maqayis)
- **B013** yüzüne vurma ve yüzüne vurulmuş olma — birinin yüzüne vurmak · yüzüne vurulmuş
  وجهت فلانا ضربت وجهه فهو موجوه (tahdhib)
- **B014** yanına gelen kişiyi geri çevirmek — yanına gelen kişiyi geri çevirmek
  أتى فلان فلانا فأوجهه وأوجأه إذا رده (tahdhib)
- **B015** iki yüzlü nesne; içiyle dışı uyuşmayan kişi [kalıp] — iki yüzü bulunan kumaş · içiyle dışı uyuşmayan iki yüzlü kimse
  كساء موجه له وجهان؛ رجل ذو وجهين إذا لقي بخلاف ما في قلبه (jamhara)

## ن ع م (root_001525) — identity root of نَّاعِمَةٌ (w3)

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

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:8, and ## Buluşmalar) =====
## Yüz: kurumuş toprak, yumuşamış toprak

İkinci ve sekizinci ayetler aynı iki kelimeyle başlar, "yüzler, o gün" der ve yalnızca bir sıfatta ayrılır. Birinci sıfat خاشعة'dır. Bu kelime alçalıp sinmeyi anlatır: {ar:أصل واحد يدل على التطامن, tr:aslun vâhidun yedullü ale't-tatâmün, gloss:alçalıp çökmeyi gösteren tek bir kök, source:"خ ش ع,B001"}. Araplar aynı kelimeyi toprak için de kullanır: {ar:بلدة خاشعة مغبرة, tr:beldetun hâşiatun muğberra, gloss:tozlu ve çökük bir yer, source:"خ ش ع,B002"}; {ar:إذا يبست الأرض ولم تمطر قيل قد خشعت, tr:izâ yebiseti'l-ardu ve lem tumtar kîle kad haşaat, gloss:yer kuruyup yağmur almayınca haşaat denir, source:"خ ش ع,B002"}; {ar:قف خاشع لاطئ بالأرض, tr:kuffun hâşiun lâtiun bi'l-ard, gloss:yere yapışmış alçak sırt, source:"خ ش ع,B002"}. Ayetin anlamı eğik ve ezik bir yüzdür. Yanında ise yağmur görmemiş, tozlanmış, yere yapışmış bir toprak duyulur.

Üçüncü ayet bu toprağın nasıl yorulduğunu gösterir: {ar:عَامِلَةٌۭ نَّاصِبَةٌۭ, tr:âmiletun nâsıba, gloss:çalışıp didinmiş ve bitkin, source:88:3}. Bitkinlik, ayakta durup çalışmaktan gelir: {ar:النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي, tr:en-nasabu'l-anâ ve ma'nâhu enne'l-insâne lâ yezâlü muntasiben hattâ yu'yî, gloss:yorgunluktur; insanın tükenene dek ayakta kalmasıdır, source:"ن ص ب,B004"}. Aynı kelime yüze çökmüş kederi de anlatır: {ar:الحزن إذا أثر فيه, tr:el-huznu izâ essera fîh, gloss:iz bırakan keder, source:"ن ص ب,B004"}. Beşinci ayette bu kurumuş yüz sulanır: {ar:تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:tuskâ min aynin âniye, gloss:kaynamış bir pınardan içirilir, source:88:5}. Sulamak, birine içecek vermektir: {ar:السقي والسقيا أن يعطيه ما يشرب, tr:es-sakyu ve's-sukyâ en yu'tıyehû mâ yeşrab, gloss:içecek vermek, source:"س ق ي,B001"}. Kuru toprağı diriltmesi gereken su burada yakan sudur. Toprağı canlandıran düzen tersine dönmüştür.

Kur'an kurumuş toprağın suyla dirilişini aynı kelimeyle anlatır. Allah ayetlerini sayarken şöyle der: {ar:تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:tera'l-arda hâşiaten fe-izâ enzelnâ aleyhe'l-mâe'htezzet ve rabet, gloss:yeri çökük görürsün; üstüne su indirince kıpırdar ve kabarır, source:41:39}. Aynı ayet hemen ardından {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39} der. Diriltilmekten şüphe edenlere de sahne aynı sözlerle kurulur: {ar:وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ, tr:ve tera'l-arda hâmideten, gloss:yeri kupkuru ve cansız görürsün, source:22:5}. Buradaki cansız toprak sıfatı, çökük toprağın tanımında geçen kelimedir: {ar:أرض خاشعة هامدة, tr:ardun hâşiatun hâmide, gloss:çökük ve cansız toprak, source:"خ ش ع,B002"}. Sağır edici çığlığın geldiği gün anlatılırken toz da yüzlere konar: {ar:فَإِذَا جَآءَتِ ٱلصَّآخَّةُ, tr:fe-izâ câeti's-sâhha, gloss:kulakları sağır eden geldiğinde, source:80:33}; {ar:وَوُجُوهٌۭ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌۭ, tr:ve vucûhun yevmeizin aleyhâ ğabera, gloss:o gün birtakım yüzlerin üstünde toz vardır, source:80:40}. Burada tozlu toprak ile tozlu yüz aynı resimde birleşir.

Altıncı ayetteki yiyecek, yüzün halini adında taşır. Yüzün eğikliği şöyle açıklanır: {ar:الخشوع الضراعة؛ إذا ضرع القلب خشعت الجوارح, tr:el-huşûu'd-darâa; izâ dara'a'l-kalbu haşaati'l-cevârih, gloss:huşu boyun eğmektir; kalp boyun eğince organlar da eğilir, source:"خ ش ع,B001"}. Bu açıklamadaki "boyun eğmek" kelimesi, yiyecek adı ضريع ile aynı köktendir: {ar:ضرع الرجل ضراعة إذا ذل, tr:dara'a'r-raculu darâaten izâ zell, gloss:adam alçalınca dara'a denir, source:"ض ر ع,B002"}. Aynı kök incelmiş bedeni de anlatır: {ar:لضارع الجسم أي نحيف ضعيف, tr:le-dâriu'l-cism ey nahîfun daîf, gloss:bedeni zayıf ve cılız, source:"ض ر ع,B003"}. Yiyecekle boyun eğme arasındaki bağ kök birliğinden gelir. Yüzün eğikliğine bağlanması ise kelimelerin açıklamasındandır.

Sekizinci ayette öteki sıfat gelir: {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vucûhun yevmeizin nâime, gloss:o gün birtakım yüzler yumuşak ve mutlu, source:88:8}. Bu kelime yumuşamayı ve tazeliği anlatır: {ar:نعم الشيء صار ناعما لينا, tr:neime'ş-şey'u sâra nâimen leyyinâ, gloss:şey yumuşak ve esnek oldu, source:"ن ع م,B002"}; {ar:نعمة العيش حسنه وغضارته, tr:na'metü'l-ayşi husnühû ve ğadâratüh, gloss:yaşamın tazeliği ve güzelliği, source:"ن ع م,B002"}. Aynı kök rüzgârların en nemlisine de ad verir: {ar:النعامى ريح الجنوب لأنها أبل الرياح وأرطبها, tr:en-neâmâ rîhu'l-cenûb li-ennehâ eballü'r-riyâhi ve ertabuhâ, gloss:rüzgârların en ıslağı ve en nemlisi olan güney rüzgârı, source:"ن ع م,B009"}. Bu yüzün toprağında akan bir pınar vardır: {ar:العين الجارية النابعة من عيون الماء, tr:el-aynü'l-câriyetü'n-nâbiatü min uyûni'l-mâ', gloss:su gözelerinden kaynayıp akan pınar, source:"ع ي ن,B006"}. Dokuzuncu ayetteki hoşnutluk {ar:أصل واحد يدل على خلاف السخط, tr:aslun vâhidun yedullü alâ hılâfi's-saht, gloss:öfkenin karşıtını gösteren kök, source:"ر ض و,B001"} diye tanımlanır. On üçüncü ayetteki sedirler ise sevinçten adlandırılmıştır: {ar:السرير الذي يجلس عليه من السرور, tr:es-serîru'llezî yuclesu aleyhi mine's-surûr, gloss:üstüne oturulan sedir adını sevinçten alır, source:"س ر ر,B011"}; {ar:السرور أمر خال من الحزن, tr:es-surûru emrun hâlin mine'l-hazen, gloss:sevinç kederden boş bir haldir, source:"س ر ر,B010"}. Üçüncü ayetteki yorgunluk iz bırakan bir kederdi. Burada sedirin adı, kederden boş olan bir sevinçtir.

Yirminci ayette göz toprağın kendisine çevrilir. Arapçada iyi toprağın sıfatı yumuşaklıktır: {ar:أرض أريضة لينة طيبة, tr:ardun erîdatun leyyinatun tayyibe, gloss:yumuşak ve verimli toprak, source:"ء ر ض,B002"}. Bu, nâime'nin tanımındaki yumuşaklığın aynısıdır. Göğe verilen adlardan biri de bulut ve yağmurdur: {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tüsemmi's-sehâbe semâen ve'l-matara semâ', gloss:Araplar buluta da yağmura da gök der, source:"س م و,B004"}. Böylece göğe ve yere yöneltilen bakış, iki yüzün farkını da gösterir: yere su iner ya da inmez.

Kur'an iki yüzü başka yerlerde de aynı sözlerle karşı karşıya koyar. Güzel davrananlar için {ar:وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌۭ وَلَا ذِلَّةٌ, tr:ve lâ yerhaku vucûhehum katerun ve lâ zille, gloss:yüzlerini ne toz ne aşağılanma bürür, source:10:26} denir. İyilerin yüzü için {ar:تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ, tr:ta'rifu fî vucûhihim nadrate'n-naîm, gloss:yüzlerinde nimetin tazeliğini tanırsın, source:83:24} denir. Burada nimet kelimesi nâime ile aynı köktendir. O günün yüzleri {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ, tr:vucûhun yevmeizin nâdıra, gloss:o gün birtakım yüzler taptaze, source:75:22} ve {ar:وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ, tr:ve vucûhun yevmeizin bâsira, gloss:birtakım yüzler de asık, source:75:24} diye ikiye ayrılır. Sabredenlere verilen karşılık da surenin iki kelimesini bir arada söyler: {ar:وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا, tr:ve lakkâhum nadraten ve surûrâ, gloss:onlara tazelik ve sevinç kavuşturdu, source:76:11}. Üçüncü ayetteki yorgunluk bahçede ortadan kaldırılır. Pınarlı bahçelerdeki takva sahipleri için {ar:لَا يَمَسُّهُمْ فِيهَا نَصَبٌۭ, tr:lâ yemessuhum fîhâ nasab, gloss:orada onlara yorgunluk dokunmaz, source:15:48} denir. Bahçe halkı da aynı sözü kendisi söyler: {ar:لَا يَمَسُّنَا فِيهَا نَصَبٌۭ وَلَا يَمَسُّنَا فِيهَا لُغُوبٌۭ, tr:lâ yemessunâ fîhâ nasabun ve lâ yemessunâ fîhâ luğûb, gloss:burada bize ne yorgunluk dokunur ne bitkinlik, source:35:35}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:2 خَٰشِعَةٌ خ ش ع B002; 88:3 نَّاصِبَةٌ ن ص ب B004; 88:5 تُسْقَىٰ س ق ي B001; 88:6 ضَرِيعٍ ض ر ع B002; 88:6 ضَرِيعٍ ض ر ع B003; 88:8 نَّاعِمَةٌ ن ع م B002; 88:8 نَّاعِمَةٌ ن ع م B009; 88:9 رَاضِيَةٌ ر ض و B001; 88:12 عَيْنٌ ع ي ن B006; 88:13 سُرُرٌ س ر ر B010; 88:13 سُرُرٌ س ر ر B011; 88:18 ٱلسَّمَآءِ س م و B004; 88:20 ٱلْأَرْضِ ء ر ض B002

## Deve: sürü, süt ve yolculuk

Bakılacak dört şeyin ilki devedir. Gök, dağlar ve yer uzaktadır. Deve ise insanın yanındadır, insan onun üstündedir. Arapçada deve bir servettir: {ar:الإبل معروفة ورجل آبل ومال مؤبل, tr:el-ibilu ma'rûfetun ve racülün âbilün ve mâlün muebbel, gloss:deve bilinir; develi adam ve deveden oluşan mal, source:"ء ب ل,B001"}. Kökün bir kolu devenin suya muhtaç kalmadan yaşı otla yetinmesini anlatır: {ar:أبلت الإبل والوحش اجتزأت بالرطب عن الماء, tr:ebeleti'l-ibilu ve'l-vahşu'ctezeet bi'r-ratbi ani'l-mâ', gloss:develer ve yaban hayvanları sudan vazgeçip yaş otla yetindi, source:"ء ب ل,B002"}. Altıncı ve yedinci ayetlerde hiçbir şeyin yetmediği insanlar vardır. On yedinci ayette ise azla yetinen bir hayvana bakılması istenir.

Surenin önceki kelimelerinde de devenin bedeni yan anlam olarak duyulur. Nâime'nin kökü sürüye ad verir: {ar:النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم, tr:en-neamu'l-ibilu limâ fîhi mine'l-hayri ve'n-ni'meti ve'l-en'âmu'l-behâim, gloss:neam devedir; içindeki hayır ve nimetten dolayı; en'âm hayvanlardır, source:"ن ع م,B005"}. Hâşia, yorgun düşmüş bir devenin hörgücünü anlatır: {ar:خشع سنام البعير إذا أنضي فذهب شحمه وتطأطأ شرفه, tr:haşaa senâmü'l-baîri izâ undiye fe-zehebe şahmuhû ve teta'tae şerefuh, gloss:yorulan devenin hörgücünün yağı gidip tepesi çöktü, source:"خ ش ع,B004"}. Âmile, çalışmaya yatkın soylu dişi deveye ad verir: {ar:اليعملة الناقة النجيبة المطبوعة على العمل, tr:el-ya'meletü'n-nâkatü'n-necîbetü'l-matbûatu ale'l-amel, gloss:çalışmaya yaratılışça yatkın soylu dişi deve, source:"ع م ل,B008"}. Ateşe girme fiilinin kökü bir bitkiye de ad verir: {ar:تسميها العرب خبزة الإبل, tr:tüsemmîhe'l-arabu hubzete'l-ibil, gloss:Araplar ona develerin ekmeği der, source:"ص ل ي,B010"}. Yemek, yağ ve deve tek bir cümlede birleşir: {ar:المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن, tr:el-mut'imu mine'l-ibili'llezî yûcedu fî muhhihî ta'mu'ş-şahm ve şâtun taûmun fîhâ ba'du's-simen, gloss:iliğinde yağ tadı bulunan deve; biraz semizliği olan koyun, source:"ط ع م,B007"}. Mevdûa'nın kökü tuzlu otlakta yayılan develeri anlatır: {ar:الواضعات الإبل تأكل الخلة, tr:el-vâdiâtü'l-ibilu te'kulu'l-hulle, gloss:vâdiât hulle otunu yiyen develerdir, source:"و ض ع,B007"}. Masfûfe ise kurban için sıraya dizilen develeri anlatır: {ar:البدن الصواف التي تصفف ثم تنحر, tr:el-budnü's-savâffu'lletî tusaffefu summe tunhar, gloss:sıraya dizilip sonra kesilen kurbanlık develer, source:"ص ف ف,B001"}. Kur'an aynı kelimeyi kurbanlık develer için kullanır: {ar:فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ, tr:fezkurusmallâhi aleyhâ savâff, gloss:sıraya dizilmişken üzerlerine Allah'ın adını anın, source:22:36}. O ayette sıra, anma ve doyurma bir aradadır. Ayet ardından {ar:وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ, tr:ve at'imu'l-kânia ve'l-mu'terr, gloss:yetineni ve isteyeni doyurun, source:22:36} der.

Süt de aynı kelimelerden geçer. Darî'in kökü memedir: {ar:الضرع لكل ذات خف أو ظلف, tr:ed-dar'u li-külli zâti huffin ev zılf, gloss:dar' tabanlı ve tırnaklı her hayvanın memesidir, source:"ض ر ع,B001"}. Merfûa'nın kökü sütünü memesinde tutan deveye ad verir: {ar:ناقة رافع إذا رفعت اللبأ في ضرعها, tr:nâkatun râfiun izâ rafeati'l-lebee fî dar'ihâ, gloss:ağız sütünü memesinde tutan dişi deveye râfi' denir, source:"ر ف ع,B007"}. Masfûfe'nin kökü tek sağımda kadehleri sıra sıra dolduran deveye ad verir: {ar:ناقة صفوف للتي تصف أقداحا من لبنها, tr:nâkatun safûfun li'lletî tesuffu akdâhan min lebenihâ, gloss:sütünden kadehleri sıra sıra dolduran dişi deve, source:"ص ف ف,B002"}. On dördüncü ayetteki kevb de böyle bir kadehtir. Besleme kelimesinin kökü sütten çıkan yağa ad verir: {ar:السمن سلاء اللبن, tr:es-semnu sulâü'l-leben, gloss:semn sütten eritilen yağdır, source:"س م ن,B002"}. Sulamanın kökü ise hem su hem süt taşıyan kırbayı anlatır: {ar:السقاء القربة للماء واللبن, tr:es-sikâü'l-kırbetü li'l-mâi ve'l-leben, gloss:su ve süt için kırba, source:"س ق ي,B004"}. Kur'an bu içirmeyi bir ibret olarak anlatır: {ar:نُّسْقِيكُم مِّمَّا فِى بُطُونِهِۦ مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:nuskîkum mimmâ fî butûnihî min beyni fersin ve demin lebenen hâlisan sâiğan li'ş-şâribîn, gloss:karınlarındakinden; fışkı ile kan arasından içenlerin boğazından kolayca geçen arı bir süt içiririz, source:16:66}. Buradaki fiil, beşinci ayetteki "içirilir" fiiliyle aynıdır. Kolay yutulan süt, cehennemdeki içeceğin tersidir: {ar:يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ, tr:yetecerrauhû ve lâ yekâdu yusîğuh, gloss:yudum yudum içer ama yutamaz, source:14:17}. "Kolayca geçen" ve "yutamaz" aynı köktendir.

Yolculuk da aynı kelimelerden duyulur. Surenin ilk fiili, yürüyen bir devenin ön ayaklarının salınımını anlatır: {ar:ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير, tr:mâ ahsene etve yedey hâzihi'n-nâka ey rac'a yedeyhâ fi's-seyr, gloss:bu devenin ön ayaklarını yürürken geri atışı ne güzel, source:"ء ت ي,B009"}. Son ayetten bir önceki ayetteki dönüş kelimesi de aynı salınımı ve gün boyu yürüyüşü anlatır: {ar:الأوب سرعة تقليب اليدين والرجلين في السير والتأويب أن تسير النهار أجمع وتنزل الليل, tr:el-evbü sur'atü taklîbi'l-yedeyni ve'r-ricleyni fi's-seyr ve't-te'vîbü en tesîra'n-nehâra ecmea ve tenzile'l-leyl, gloss:yürüyüşte el ve ayakları çabuk oynatmak; bütün gün yürüyüp gece konmak, source:"ء و ب,B003"}; {ar:كل راجع مع الليل فهو آئب, tr:küllü râciin mea'l-leyli fe-huve âib, gloss:gece olunca dönen herkes âibdir, source:"ء و ب,B006"}. Aradaki kelimeler de yürüyüşün türlerini adlandırır: {ar:نصب القوم ساروا يومهم وهو سير لين, tr:nasaba'l-kavmu sârû yevmehum ve huve seyrun leyyin, gloss:topluluk bütün gün yumuşak bir yürüyüşle yürüdü, source:"ن ص ب,B010"}; {ar:السعي عدو ليس بشديد, tr:es-sa'yu adven leyse bi-şedîd, gloss:sa'y şiddetli olmayan koşudur, source:"س ع ي,B001"}; {ar:مرفوع الناقة في سيرها خلاف الموضوع, tr:merfûu'n-nâkati fî seyrihâ hılâfu'l-mevdû', gloss:devenin yürüyüşünde merfû mevdûun zıddıdır, source:"ر ف ع,B003"}; {ar:وضع البعير وغيره أي أسرع في سيره, tr:vadaa'l-baîru ve ğayruhû ey esraa fî seyrih, gloss:deve hızlandı, source:"و ض ع,B003"}. Bunlar yan anlamlardır ve ayetlerin anlamının yerine geçmez. Ama surenin "geldi mi" ile başlayıp "dönüşleri" ile biten yolu, deve sürücülerinin bir günlük yürüyüşü anlattığı kelimelerle kurulmuştur.

Kur'an deveyi yaratılmış ve insana boyun eğdirilmiş bir nimet olarak anlatır: {ar:وَٱلْأَنْعَٰمَ خَلَقَهَا ۗ لَكُمْ فِيهَا دِفْءٌۭ وَمَنَٰفِعُ وَمِنْهَا تَأْكُلُونَ, tr:ve'l-en'âme halakahâ lekum fîhâ dif'un ve menâfiu ve minhâ te'kulûn, gloss:hayvanları yarattı; onlarda sizin için ısınma ve faydalar vardır ve onlardan yersiniz, source:16:5}; {ar:وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ, tr:ve tahmilu eskâlekum ilâ beledin lem tekûnû bâliğîhi illâ bi-şıkkı'l-enfus, gloss:ancak canınızı tüketerek varabileceğiniz bir yere yüklerinizi taşırlar, source:16:7}. Başka bir ayette Allah'ın kendi işi anlatılır: {ar:أَوَلَمْ يَرَوْا۟ أَنَّا خَلَقْنَا لَهُم مِّمَّا عَمِلَتْ أَيْدِينَآ أَنْعَٰمًۭا, tr:e-ve-lem yerav ennâ halaknâ lehum mimmâ amilet eydînâ en'âmen, gloss:ellerimizin işinden onlar için hayvanlar yarattığımızı görmediler mi, source:36:71}; {ar:وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ وَمِنْهَا يَأْكُلُونَ, tr:ve zellelnâhâ lehum fe-minhâ rakûbuhum ve minhâ ye'kulûn, gloss:onları kendilerine boyun eğdirdik; bir kısmına biner bir kısmından yerler, source:36:72}. Bu ayetteki "iş" kelimesi, üçüncü ayetteki âmile ile aynı köktendir, ama burada iş Allah'ındır. Boyun eğdirme fiili de aşağılanma kelimesiyle aynı köktendir, ama burada bir lütuf olarak hayvana uygulanır. Deve, surenin döşediği odayı da döşer: {ar:وَجَعَلَ لَكُم مِّن جُلُودِ ٱلْأَنْعَٰمِ بُيُوتًۭا, tr:ve ceale lekum min cülûdi'l-en'âmi buyûten, gloss:hayvanların derilerinden size evler yaptı, source:16:80}; {ar:وَمِنْ أَصْوَافِهَا وَأَوْبَارِهَا وَأَشْعَارِهَآ أَثَٰثًۭا وَمَتَٰعًا, tr:ve min asvâfihâ ve evbârihâ ve eş'ârihâ esâsen ve metâan, gloss:yünlerinden yapağılarından ve kıllarından ev eşyası ve kullanılacak şeyler, source:16:80}. Allah İbrahim'e insanları hacca çağırmasını söylerken develer de gelişin aracıdır: {ar:يَأْتُوكَ رِجَالًۭا وَعَلَىٰ كُلِّ ضَامِرٍۢ يَأْتِينَ مِن كُلِّ فَجٍّ عَمِيقٍۢ, tr:ye'tûke ricâlen ve alâ külli dâmirin ye'tîne min külli feccin amîk, gloss:yaya olarak ve her uzak yoldan gelen arık develer üstünde sana gelsinler, source:22:27}. Bakmanın yiyeceğe yöneltildiği yerde de hayvanlar anılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bu bakış {ar:مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ, tr:metâan lekum ve li-en'âmikum, gloss:size ve hayvanlarınıza bir yararlanma olarak, source:80:32} diye biter.

Kaynaklar: 88:1 أَتَىٰكَ ء ت ي B009; 88:2 خَٰشِعَةٌ خ ش ع B004; 88:3 عَامِلَةٌ ع م ل B008; 88:3 نَّاصِبَةٌ ن ص ب B010; 88:4 تَصْلَىٰ ص ل ي B010; 88:5 تُسْقَىٰ س ق ي B004; 88:6 ضَرِيعٍ ض ر ع B001; 88:6 طَعَامٌ ط ع م B007; 88:7 يُسْمِنُ س م ن B002; 88:8 نَّاعِمَةٌ ن ع م B005; 88:9 لِّسَعْيِهَا س ع ي B001; 88:13 مَّرْفُوعَةٌ ر ف ع B003; 88:13 مَّرْفُوعَةٌ ر ف ع B007; 88:14 مَّوْضُوعَةٌ و ض ع B003; 88:14 مَّوْضُوعَةٌ و ض ع B007; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:15 مَصْفُوفَةٌ ص ف ف B002; 88:17 ٱلْإِبِلِ ء ب ل B001; 88:17 ٱلْإِبِلِ ء ب ل B002; 88:25 إِيَابَهُمْ ء و ب B003; 88:25 إِيَابَهُمْ ء و ب B006

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

