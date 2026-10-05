Focus: 88:5. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_5/D.r13/context.md =====
# 88:5 — focus

تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ

Anchor translation (canonical reading, reference only):

Kaynar bir kaynaktan içirilir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | تُسْقَىٰ | سَقَىٰ | س ق ي | V |
| 2 | مِنْ | مِن |  | P |
| 3 | عَيْنٍ | عَيْن | ع ي ن | N |
| 4 | ءَانِيَةٍ | ءَانِيَة | ء ن ي | ADJ |


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
- 88:5 ◀ focus تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
- 88:6 لَّيْسَ لَهُمْ طَعَامٌ إِلَّا مِن ضَرِيعٍۢ
- 88:7 لَّا يُسْمِنُ وَلَا يُغْنِى مِن جُوعٍۢ
- 88:8 وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ
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


===== _commentary/v16/work/88_5/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## س ق ي (root_000722) — identity root of تُسْقَىٰ (w1)

- **B001** içecek verme veya kaynaktan su alma — birine içecek vermek · içecek verme; içirme · nehirden ya da kuyudan su almak
  سقيته بيدي أسقيه سقيا (maqayis)؛ الاستقاء الأخذ من النهر والبئر (ayn)؛ سقيته لشفته (sihah)؛ فإذا سقاك ماء لشفتك قال سقاه (tahdhib)؛ السقي والسقيا أن يعطيه ما يشرب (mufradat)
- **B002** su kaynağı sağlamak — birine dilediğinde yararlanacağı su kaynağı sağlamak
  أسقيته إذا جعلت له سقيا (maqayis)؛ أسقينا فلانا نهرا أي جعلناه له سقيا (ayn)؛ أسقيته لماشيته وأرضه (sihah)؛ أسقيت فلانا نهرا أو ماء إذا جعلته له سقيا (tahdhib)؛ الإسقاء أن يجعل له ذلك حتى يتناوله كيف شاء (mufradat)
- **B003** tarımsal su payı, sulama düzeni ve ürün paylı bakım — arazinin su payı veya sulanması · küçük sulama kanalı · ürün payı karşılığında bağ veya hurma bahçesini sulayıp bakımını üstlenme sözleşmesi · düzenli sulamayla yaşayan ekin veya hurma
  كم سقى أرضك أي حظها من الشرب (maqayis;tahdhib)؛ الساقية من سواقي الزرع (ayn;tahdhib)؛ المسقوى من الزرع ما يسقى بالسيح (sihah)؛ وللأرض التي تسقى سقي (mufradat)؛ المساقاة في النخيل والكروم (tahdhib)
- **B004** su kabı, içme yeri, kap donanımı ve tulumluk deri verme — su veya süt tulumu · içecek sunulan yer veya su evi · hükümdarın içtiği ölçü kabı · testi ve kupaların asıldığı askılık · su tulumu yapılmak üzere deri vermek
  أسقيتك هذا الجلد أي وهبته لك تتخذه سقاء (maqayis)؛ السقاء القربة للماء واللبن (ayn;sihah;tahdhib)؛ السقاية الموضع الذي يتخذ فيه الشراب (maqayis;ayn;tahdhib)؛ السقاية الصواع (maqayis;ayn;tahdhib;mufradat)؛ المسقاة تتخذ للجرار والأكواز (ayn;tahdhib)
- **B005** karında veya doğum zarında biriken sıvı — karın yağında oluşan sarı sıvı veya sıvı kesecikleri · karnında hastalıklı sıvı birikmek · karında su toplanması hastalığına tutulmak · doğum zarı içindeki ve çocukla çıkan sıvı
  وسقى بطن فلان وذلك ماء أصفر يقع فيه (maqayis)؛ السقي ما يكون في نفافيخ بيض في شحم البطن (ayn;tahdhib)؛ سقى يسقي بطنه سقيا (ayn;tahdhib;sihah)؛ استسقى بطنه استسقاء والاسم السقي (tahdhib)؛ السقي الماء الذي يكون في المشيمة (tahdhib)
- **B006** su veya yağmur için dua etmek [kalıp] — Tanrı birine su veya yağmur versin diye dua etmek
  سقيت على فلان أي قلت سقاه الله (maqayis)؛ سقاه الله الغيث وأسقاه (sihah)؛ اللهم أسقنا إسقاء رواء (tahdhib)
- **B007** iri damlalı şiddetli yağmur bulutu — iri damlalı, şiddetli yağmur bulutu
  السقى على فعيل أيضا السحابة العظيمة القطر (maqayis)؛ السقي على فعيل السحابة العظيمة القطر الشديدة الوقع (sihah)؛ السقي والرقي على فعيل سحابتان عظيمتا القطر شديدتا الوقع (tahdhib)
- **B008** suyla beslenen yumuşak papirüs kamışı — sudan yoksun kalmayan papirüs kamışı · papirüs kamışının tek bir sapı
  والسقي البردى (maqayis)؛ السقي البردي الواحدة سقية لا يفوتها الماء (ayn)؛ السقي أيضا البردي (sihah)؛ السقي هو البردي الواحدة سقية (tahdhib)
- **B009** boyayı emdirerek kumaşı boyamak [kalıp] — boyayı emdirerek kumaşı boyamak
  يقال للثوب إذا صبغ سقيته منا من عصفر (ayn)؛ يقال للثوب إذا صبغته سقيته منا من عصفر ونحو ذلك (tahdhib)
- **B010** yineleyerek kalbe düşmanlık işlemek [kalıp] — hoşlanmadığı şeyi yineleyerek kalbine düşmanlık işlemek · birine hoşlanmadığı şeyi tekrar tekrar söylemek
  سقى فلان على فلان بما يكره إذا كرره عليه (maqayis)؛ سقي قلبه تسقية إذا كرر عليه ما يكره (ayn)؛ سقي قلبه بالعداوة تسقية (tahdhib)
- **B011** birinin arkasından ağır biçimde kötü konuşmak [kalıp] — birinin arkasından ağır biçimde kötü konuşmak
  أسقيت الرجل إذا اغتبته (maqayis;tahdhib)؛ يقال سقى زيد عمرا وأستقاه إذا اغتابه غيبة خبيثة (tahdhib)

## ع ي ن (root_001069) — identity root of عَيْنٍ (w3)

- **B001** gören göz — göz, görme organı
  العين الناظرة لكل ذي بصر (maqayis;ayn); العين: حاسة الرؤية (sihah); العين: التي يبصر بها الناظر (tahdhib); العين الجارحة (mufradat)
- **B002** gözle görüp kesin biçimde tanıma — gözle görerek, yüz yüze · yüz yüze görerek · bilerek, görüp emin olarak · gördükten sonra ayrıca iz aramam
  رأيت الشيء عيانا أي معاينة (maqayis); لا أطلب أثرا بعد عين أي بعد معاينة (ayn;sihah;tahdhib); عيانا أي مواجهة (tahdhib); فعلت ذلك عمد عين (sihah)
- **B003** koruyup gözetme — korumam altında, özenle gözeterek · gözümün önünde, korumam altında · gözetimimiz ve korumamız altında
  أنت على عيني، في الإكرام والحفظ جميعا (sihah); على عيني قصدت زيدا يريدون الإشفاق (tahdhib); فلان بعيني أي أحفظه وأراعيه (mufradat); بحيث نرى ونحفظ (mufradat)
- **B004** kötü bakışla zarar verme — gözüyle zarar verdi · gözü değen kimse · göz değmiş kimse · gözü sık değen kimse
  عنت الرجل إذا أصبته بعينك (maqayis); عنت الشيء بعينه فأنا أعينه عينا وهو معيون (ayn); عنت الرجل: أصبته بعينى، فأنا عائن (sihah); عان الرجل فلانا يعينه عينا إذا ما أصابه بالعين (tahdhib); عنته: أصبته بعيني (mufradat)
- **B005** haber toplayan gizli gözcü — gizli gözcü veya öncü · gizli gözcü · bizim için çevreyi yoklayıp haber getirdi
  العين الذي تبعثه يتجسس الخبر (maqayis); العين الذي تبعثه لتجسس الخبر (ayn); العين: الديدبان، والجاسوس (sihah); بعثنا عينا أي طليعة (tahdhib); قيل للمتجسس عين (mufradat)
- **B006** akan su kaynağı — akan su kaynağı · göz önünde akan su · su aktı veya kaynağı ortaya çıktı
  العين الجارية النابعة من عيون الماء (maqayis); عين الماء (ayn;sihah); العين الينبوع الذي ينبع من الأرض ويجري (tahdhib); لمنبع الماء: عين (mufradat); ماء معين أي ظاهر للعيون (mufradat)
- **B007** su sızdıran ince delik — su kabındaki ince veya delik sızıntı yeri · incelip su tutamaz olmuş su kabı · dikiş delikleri kapansın diye kaba su döktü
  عين السقاء (maqayis); تعين السقاء أي بلي ورق منه مواضع (ayn); بالجلد عين، وهي دوائر رقيقة (sihah); سقاء عين إذا رق فلم يمسك الماء (tahdhib); الثقب في المزادة تشبيها بها في الهيئة وفي سيلان الماء (mufradat)
- **B008** güneş yuvarlağı — güneşin gövdesi veya yuvarlağı
  عين الشمس مشبه بعين الإنسان (maqayis); عين الشمس صيخدها (ayn); العين: عين الشمس (sihah); طلعت العين وغابت العين، أي الشمس (tahdhib)
- **B009** göze benzer çukur, yer veya eğim — dizin önündeki çukur · kuyunun kaynak yeri veya çukuru · terazideki küçük eğim veya dengesizlik · yayda merminin yerleştiği bölüm
  عين الركية وهما عينان كأنهما نقرتان في مقدمها (maqayis); عين الركبة (ayn;sihah;tahdhib); في الميزان عين إذا رجحت إحدى كفتيه (tahdhib); عين القوس التي يقع فيها البندق (tahdhib)
- **B010** belirli yönden gelen bulut veya dinmeyen yağmur — kıblenin sağından gelen bulut · günlerce dinmeyen yağmur
  العين السحاب ما جاء من ناحية القبلة (maqayis); العين من السحاب ما أقبل عن يمين القبلة (ayn); العين: ما عن يمين قبلة العراق (sihah;tahdhib); العين: مطر أيام لا يقلع (sihah;tahdhib)
- **B011** hemen elde bulunan para — elde hazır bulunan para · altın para, eldeki para
  العين وهو المال العتيد الحاضر (maqayis); عين غير دين أي مال حاضر (ayn); العين: الدينار؛ العين: المال الناض (sihah); العين: النقد (tahdhib); قيل للذهب: عين (mufradat)
- **B012** ertelenmiş ödemeli alımla para edinme — önceden verilen para veya para sağlamak için yapılan satış · malı ödemesi ertelenmiş olarak satın aldı
  العينة السلف (maqayis;ayn;sihah); تعين فلان من فلان عينة (ayn); اعتان الرجل، إذا اشترى الشئ بنسيئة (sihah); عين التاجر يعين تعيينا وعينة قبيحة (tahdhib); سميت عينة لحصول النقد لطالب العينة (tahdhib)
- **B013** şeyin bizzat kendisi ve belirlenmiş olanı — şeyin bizzat kendisi · tam kendisi, yerine başkası değil · bir şeyi topluluk içinden belirleyip ayırma
  عين الشيء نفسه (maqayis;sihah;tahdhib); خذ درهمك بعينه (maqayis); تعيين الشئ: تخصيصه من الجملة (sihah); دراهمك بأعيانها وهي أعيان دراهمك (tahdhib); ذات الشيء (mufradat)
- **B014** bir şeyin en iyi ve seçkin bölümü — bir şeyin en iyi ve seçkin bölümü
  عينة كل شيء خياره (maqayis); العينة: خيار الشيء (tahdhib); عين الشئ: خياره (sihah); عينة المال أيضا: خياره (sihah); العين تشبيها بها في كونها أفضل الجواهر (mufradat)
- **B015** önde gelen kişiler veya anne baba bir kardeşler — topluluğun önde gelen seçkin kişileri · anne baba bir kardeşler veya aynı kadının çocukları
  أعيان القوم أي أشرافهم (maqayis;sihah;tahdhib); هؤلاء أعيان إخوتهم (maqayis); الأعيان: الأخوة بنو أب واحد وأم واحدة (sihah); أعيان بني الأم يتوارثون (tahdhib); أعيان القوم لأفاضلهم، وأعيان الإخوة (mufradat)
- **B016** geniş ve güzel gözlü olma — geniş ve güzel gözlü · gözlerinin güzelliğiyle adlandırılan yaban sığırı · geniş ve güzel gözlü kadınlar · göz benzeri küçük kare desenli kumaş
  توصف البقرة بسعة العين فيقال بقرة عيناء (maqayis); العين بقر الوحش (ayn;sihah;tahdhib); العين عظم سواد العين في سعتها (ayn); رجل أعين واسع العين (sihah;tahdhib); قاصرات الطرف عين؛ وحور عين (mufradat)
- **B017** kimse veya orada bulunan insanlar — orada hiç kimse yok · ev halkı veya orada bulunanlar · bir topluluk içinde
  ما بها عين متحركة الياء تريد أحدا له عين (maqayis); ما بها عائن، وكذلك ما بها عين، أي أحد (sihah); العين، بالتحريك: أهل الدار (sihah); العين: أهل الدار (tahdhib); جاء فلان في عين، أي في جماعة (sihah)

## ء ن ي (root_000063) — identity root of ءَانِيَةٍ (w4)

- **B001** ağırdan alma ve geciktirme — ağırbaşlılık ve acele etmeme · bir işte acele etmemek, bekleyip yumuşak davranmak · işlerde duraklayıp acele etmeme · bir şeyi geciktirmek, bekletmek ve yavaşlatmak · birini aceleye sürmemek, onun için beklemek · acele etmeyen, ağırbaşlı kişi · ağırbaşlı kadın veya kalkarken gevşek davranan kadın
  الأناة الحلم والفعل منه تأنى وتأيا (maqayis)؛ التأني (maqayis)؛ آنيت يعني أخرت المجيء وأبطأت (maqayis)؛ الإيناء بمعنى الإبطاء وآنيت الشيء أي أخرته (ayn)؛ آناه يؤنيه إيناء أي أخره وحبسه وأبطأه (sihah)؛ الأناة التؤدة وتأنيت تأخرت (mufradat)
- **B002** gecenin zaman bölümleri — gecenin zaman bölümleri · gecenin tek bir zaman bölümü · ara sıra, zaman zaman
  الإني والأنى ساعة من ساعات الليل والجمع آناء (maqayis;ayn)؛ وآناء الليل واحدها إني وهي الساعة من الليل (jamhara)؛ آناء الليل ساعاته (sihah;tahdhib;mufradat)
- **B003** zamanı gelip olgunluğa erişme — bir şeyin zamanı, olgunluğu veya erişme noktası · zamanı gelmek, olgunlaşmak ve erişmek · senin için zamanı gelmedi mi · yemeğin pişip olgunlaşmasını beklemek · ısısı doruğa varmış çok sıcak su · ısısı yükselmiş sıcak kaynak · olgunlaşmış ve erişmiş
  الإني إدراك الشيء (maqayis)؛ انتظرنا إنى الطعام أي إدراكه (maqayis;ayn)؛ ما أنى لك ولم يأن لك أي لم يحن (maqayis;ayn)؛ حميم آن قد انتهى حره وعين آنية (maqayis;ayn)؛ أنى الشيء يأنى إنى أي حان وأنى أيضا أدرك (sihah)؛ بلغ إناه من شدة الحر (mufradat)
- **B004** içine şey konan kap — içine bir şey konan kap · kaplar ve daha geniş çoğul biçimi
  الإناء ممدود من الآنية والأواني جمع جمع (maqayis)؛ الإناء معروف وجمعه آنية والأواني (sihah)؛ الإناء ما يوضع فيه الشيء وجمعه آنية (mufradat)
- **B005** nereden ve nasıl diye sorma sözü — nereden, hangi yönden, nasıl veya ne zaman · bu sana nereden ya da nasıl geldi · hangi yönden gelirsen, sana gelirim · nereye ya da nasıl yönelirse
  أنى معناها كيف ومن أين (ayn)؛ أنى معناه أين ومن أين ومن أي جهة وقد تكون بمعنى كيف (sihah)؛ أنى أداة لها معنيان متى ومن أين ويحتمل كيف (tahdhib)؛ أنى للبحث عن الحال والمكان (mufradat)

## ECHO س و ق (root_000762) — for تُسْقَىٰ (w1): withheld observed target; not identity

- **B001** sürüp götürme — sürüp götürmek · sürme ve götürme · sürücü · sürüp götürmek; sürülerek gitmek · sürülüp götürülen hayvan topluluğu · rüzgarın sürüklediği bulut · sürüp götürmesi için deve vermek · kadına evlilik ödemesini götürüp vermek · kadına götürülen evlilik ödemesi
  أصل واحد وهو حدو الشيء (maqayis)؛ ساقه يسوقه سوقا (maqayis)؛ سقته سوقا (ayn)؛ ساق الماشية يسوقها سوقا وسياقا (sihah)؛ سوق الإبل جلبها وطردها (mufradat)؛ السيقة ما استيق من الدواب (maqayis)؛ السيقة ما يساق من الدواب (mufradat)؛ السيق من السحاب ما طردته الريح (tahdhib)؛ أسقتك إبلا أي أعطيتك إبلا تسوقها (sihah)
- **B002** ölüm sancısı ve son varışa götürülüş — ölüm anında can çekişmek · ölüm sancısı, can çekişme · son varış ve oraya götürülüş · can çekişmek; ses değişmeli söyleyiş
  رأيته يسوق سياقا أي ينزع نزعا يعني الموت (ayn)؛ السياق نزع الروح (sihah)؛ فلان في السياق أي في النزع (tahdhib)؛ إلى ربك يومئذ المساق (mufradat)؛ يفوق بنفسه وهذا من باب الإبدال وإنما أصله يسوق (maqayis)
- **B003** bacak ya da taşıyıcı gövde — bacak; bitki gövdesi · ağaç gövdesi · bacaklar; gövdeler · iri ya da uzun bacaklı · bacağından vurmak veya yaralamak · uzun gövdeli bitki
  الساق لكل شجر وإنسان وطائر (ayn)؛ الساق ساق القدم والجمع سوق وسيقان وأسؤق (sihah)؛ ساق الشجرة جذعها (sihah)؛ الساق للإنسان وغيره والجمع سوق إنما سميت بذلك لأن الماشي ينساق عليها (maqayis)؛ فاستوى على سوقه هو جمع ساق (mufradat)؛ سقت الإنسان إذا أصبت ساقه (tahdhib)؛ امرأة سوقاء ورجل أسوق إذا كان عظيم الساق (maqayis)
- **B004** şiddetin açığa çıkması ve işe sıkı sarılma [kalıp] — şiddetin ve güçlüğün açığa çıkması · işe ciddiyetle ve hazırlıkla sarılmak · savaş iyice kızıştı
  يوم يكشف عن ساق أي عن شدة (sihah)؛ عن ساق عن شدة (tahdhib)؛ قيل للأمر الشديد ساق (tahdhib)؛ قام فلان على ساق إذا عني بالأمر وتحزم له (tahdhib)؛ كشفت الحرب عن ساقها (mufradat)
- **B005** pazar yeri — pazar yeri · alışveriş yapmak
  السوق موضع البياعات (ayn;tahdhib)؛ السوق مشتقة من هذا لما يساق إليها من كل شيء والجمع أسواق (maqayis)؛ تسوق القوم إذا باعوا واشتروا (sihah)؛ السوق الموضع الذي يجلب إليه المتاع للبيع (mufradat)
- **B006** savaşın en kızgın yeri [kalıp] — savaşın en kızgın yeri
  سوق الحرب حومة القتال (ayn;sihah;tahdhib)؛ سوق الحرب حومة القتال وهي مشتقة من الباب الأول (maqayis)
- **B007** sıradan halk ve yönetilenler — sıradan halk, yönetilenler
  السوقة أوساط الناس والجميع السوق (ayn)؛ السوقة خلاف الملك (sihah)؛ السوقة بمنزلة الرعية التي يسوسها الملك (tahdhib)
- **B008** erkek güvercin ya da kumru — erkek güvercin veya kumru · erkek kumru adı veya ses taklidi
  الساق الذكر من الحمام (ayn)؛ ساق حر ذكر القماري (sihah)؛ الساق الحمام الذكر (tahdhib)؛ ساق حر صوت القمري كأنه حكاية صوته (tahdhib)
- **B009** üzengi kayışı — üzengi kayışı
  الأساقة سير الركاب للسروج (ayn)؛ الإساقة سير الركاب للسروج (tahdhib)
- **B010** tekili kaydedilmemiş kolyeler — kolyeler; tekili kaydedilmemiş çoğul ad
  الأياسق القلائد ولم نسمع لها بواحد (tahdhib)
- **B011** güçlülükte övünme yarışına girmek — güçlülükte karşılıklı övünmek
  ومنه قولهم ساوقه أي فاخره أينا أشد (sihah)
- **B012** birbiri ardınca gelme — peş peşe ilerlemek · birbiri ardınca
  تساوقت الإبل إذا تتابعت (tahdhib)؛ ولدت فلانة ثلاثة بنين على ساق واحد أي بعضهم على إثر بعض (sihah;tahdhib)
- **B013** ordunun art bölümü [kalıp] — ordunun art bölümü
  ساقه الجبش مؤخره (sihah)
- **B014** tanımı verilmeyen bilinen bir ad — 
  السويق معروف (sihah;tahdhib)

## ECHO ء و ن (root_000068) — for ءَانِيَةٍ (w4): withheld observed target; not identity

- **B001** yumuşak ve rahat davranma — yumuşak davrandı · rahatlık, dinginlik ve yumuşak davranma · yolculukta kendini yorma, rahat git · yumuşak ve rahat davrandın · rahat ve dingin adam · rahat ve dingin geceler
  كلمة واحدة تدل على الرفق (maqayis); آن يؤون أونا إذا رفق (maqayis); الأون: الدعة والسكينة والرفق (sihah); أن على نفسك أي ارفق في السير واتدع (maqayis;sihah); رجل آئن (maqayis); رجل آين أي رافه وادع (sihah); ليال أوائن روافه وآينات وادعات (sihah)
- **B002** yük yanı — yük kabının bir yanı; dengeli yük parçası · iki yanlı çıkın veya çift yanlı yük · eşeğin yiyip içince karnı ve iki yanı yük gibi doldu
  الأون: أحد جانبي الخرج (sihah); الأون: العدل (sihah); أون الحمار إذا أكل وشرب وامتلأ بطنه وامتدت خاصرتاه فصار مثل الأون (sihah)
- **B003** belirli zaman — belirli zaman · ayrı zamanlar, ara ara gelen vakitler · o işi ara sıra yapar ve ara sıra bırakır
  الأوان: الحين، والجمع آونة (sihah); فلان يصنع ذلك الأمر آونة إذا كان يصنعه مرارا ويدعه مرارا (sihah)
- **B004** büyük kemerli yapı bölümü — büyük kemerli yapı bölümü · büyük kemerli yapı bölümü; belirli saray örneğiyle de anılır · büyük kemerli yapı bölümü · büyük kemerli yapı bölümleri · büyük kemerli yapı bölümleri
  الأوان والإيوان: الصفة العظيمة كالأزج (sihah); إيوان كسرى (sihah); جمع الإوان أون وجمع الإيوان إيوانات وأواوين (sihah)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:5, and ## Buluşmalar) =====
## Yüz: kurumuş toprak, yumuşamış toprak

İkinci ve sekizinci ayetler aynı iki kelimeyle başlar, "yüzler, o gün" der ve yalnızca bir sıfatta ayrılır. Birinci sıfat خاشعة'dır. Bu kelime alçalıp sinmeyi anlatır: {ar:أصل واحد يدل على التطامن, tr:aslun vâhidun yedullü ale't-tatâmün, gloss:alçalıp çökmeyi gösteren tek bir kök, source:"خ ش ع,B001"}. Araplar aynı kelimeyi toprak için de kullanır: {ar:بلدة خاشعة مغبرة, tr:beldetun hâşiatun muğberra, gloss:tozlu ve çökük bir yer, source:"خ ش ع,B002"}; {ar:إذا يبست الأرض ولم تمطر قيل قد خشعت, tr:izâ yebiseti'l-ardu ve lem tumtar kîle kad haşaat, gloss:yer kuruyup yağmur almayınca haşaat denir, source:"خ ش ع,B002"}; {ar:قف خاشع لاطئ بالأرض, tr:kuffun hâşiun lâtiun bi'l-ard, gloss:yere yapışmış alçak sırt, source:"خ ش ع,B002"}. Ayetin anlamı eğik ve ezik bir yüzdür. Yanında ise yağmur görmemiş, tozlanmış, yere yapışmış bir toprak duyulur.

Üçüncü ayet bu toprağın nasıl yorulduğunu gösterir: {ar:عَامِلَةٌۭ نَّاصِبَةٌۭ, tr:âmiletun nâsıba, gloss:çalışıp didinmiş ve bitkin, source:88:3}. Bitkinlik, ayakta durup çalışmaktan gelir: {ar:النصب العناء ومعناه أن الإنسان لا يزال منتصبا حتى يعيي, tr:en-nasabu'l-anâ ve ma'nâhu enne'l-insâne lâ yezâlü muntasiben hattâ yu'yî, gloss:yorgunluktur; insanın tükenene dek ayakta kalmasıdır, source:"ن ص ب,B004"}. Aynı kelime yüze çökmüş kederi de anlatır: {ar:الحزن إذا أثر فيه, tr:el-huznu izâ essera fîh, gloss:iz bırakan keder, source:"ن ص ب,B004"}. Beşinci ayette bu kurumuş yüz sulanır: {ar:تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:tuskâ min aynin âniye, gloss:kaynamış bir pınardan içirilir, source:88:5}. Sulamak, birine içecek vermektir: {ar:السقي والسقيا أن يعطيه ما يشرب, tr:es-sakyu ve's-sukyâ en yu'tıyehû mâ yeşrab, gloss:içecek vermek, source:"س ق ي,B001"}. Kuru toprağı diriltmesi gereken su burada yakan sudur. Toprağı canlandıran düzen tersine dönmüştür.

Kur'an kurumuş toprağın suyla dirilişini aynı kelimeyle anlatır. Allah ayetlerini sayarken şöyle der: {ar:تَرَى ٱلْأَرْضَ خَٰشِعَةًۭ فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:tera'l-arda hâşiaten fe-izâ enzelnâ aleyhe'l-mâe'htezzet ve rabet, gloss:yeri çökük görürsün; üstüne su indirince kıpırdar ve kabarır, source:41:39}. Aynı ayet hemen ardından {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39} der. Diriltilmekten şüphe edenlere de sahne aynı sözlerle kurulur: {ar:وَتَرَى ٱلْأَرْضَ هَامِدَةًۭ, tr:ve tera'l-arda hâmideten, gloss:yeri kupkuru ve cansız görürsün, source:22:5}. Buradaki cansız toprak sıfatı, çökük toprağın tanımında geçen kelimedir: {ar:أرض خاشعة هامدة, tr:ardun hâşiatun hâmide, gloss:çökük ve cansız toprak, source:"خ ش ع,B002"}. Sağır edici çığlığın geldiği gün anlatılırken toz da yüzlere konar: {ar:فَإِذَا جَآءَتِ ٱلصَّآخَّةُ, tr:fe-izâ câeti's-sâhha, gloss:kulakları sağır eden geldiğinde, source:80:33}; {ar:وَوُجُوهٌۭ يَوْمَئِذٍ عَلَيْهَا غَبَرَةٌۭ, tr:ve vucûhun yevmeizin aleyhâ ğabera, gloss:o gün birtakım yüzlerin üstünde toz vardır, source:80:40}. Burada tozlu toprak ile tozlu yüz aynı resimde birleşir.

Altıncı ayetteki yiyecek, yüzün halini adında taşır. Yüzün eğikliği şöyle açıklanır: {ar:الخشوع الضراعة؛ إذا ضرع القلب خشعت الجوارح, tr:el-huşûu'd-darâa; izâ dara'a'l-kalbu haşaati'l-cevârih, gloss:huşu boyun eğmektir; kalp boyun eğince organlar da eğilir, source:"خ ش ع,B001"}. Bu açıklamadaki "boyun eğmek" kelimesi, yiyecek adı ضريع ile aynı köktendir: {ar:ضرع الرجل ضراعة إذا ذل, tr:dara'a'r-raculu darâaten izâ zell, gloss:adam alçalınca dara'a denir, source:"ض ر ع,B002"}. Aynı kök incelmiş bedeni de anlatır: {ar:لضارع الجسم أي نحيف ضعيف, tr:le-dâriu'l-cism ey nahîfun daîf, gloss:bedeni zayıf ve cılız, source:"ض ر ع,B003"}. Yiyecekle boyun eğme arasındaki bağ kök birliğinden gelir. Yüzün eğikliğine bağlanması ise kelimelerin açıklamasındandır.

Sekizinci ayette öteki sıfat gelir: {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاعِمَةٌۭ, tr:vucûhun yevmeizin nâime, gloss:o gün birtakım yüzler yumuşak ve mutlu, source:88:8}. Bu kelime yumuşamayı ve tazeliği anlatır: {ar:نعم الشيء صار ناعما لينا, tr:neime'ş-şey'u sâra nâimen leyyinâ, gloss:şey yumuşak ve esnek oldu, source:"ن ع م,B002"}; {ar:نعمة العيش حسنه وغضارته, tr:na'metü'l-ayşi husnühû ve ğadâratüh, gloss:yaşamın tazeliği ve güzelliği, source:"ن ع م,B002"}. Aynı kök rüzgârların en nemlisine de ad verir: {ar:النعامى ريح الجنوب لأنها أبل الرياح وأرطبها, tr:en-neâmâ rîhu'l-cenûb li-ennehâ eballü'r-riyâhi ve ertabuhâ, gloss:rüzgârların en ıslağı ve en nemlisi olan güney rüzgârı, source:"ن ع م,B009"}. Bu yüzün toprağında akan bir pınar vardır: {ar:العين الجارية النابعة من عيون الماء, tr:el-aynü'l-câriyetü'n-nâbiatü min uyûni'l-mâ', gloss:su gözelerinden kaynayıp akan pınar, source:"ع ي ن,B006"}. Dokuzuncu ayetteki hoşnutluk {ar:أصل واحد يدل على خلاف السخط, tr:aslun vâhidun yedullü alâ hılâfi's-saht, gloss:öfkenin karşıtını gösteren kök, source:"ر ض و,B001"} diye tanımlanır. On üçüncü ayetteki sedirler ise sevinçten adlandırılmıştır: {ar:السرير الذي يجلس عليه من السرور, tr:es-serîru'llezî yuclesu aleyhi mine's-surûr, gloss:üstüne oturulan sedir adını sevinçten alır, source:"س ر ر,B011"}; {ar:السرور أمر خال من الحزن, tr:es-surûru emrun hâlin mine'l-hazen, gloss:sevinç kederden boş bir haldir, source:"س ر ر,B010"}. Üçüncü ayetteki yorgunluk iz bırakan bir kederdi. Burada sedirin adı, kederden boş olan bir sevinçtir.

Yirminci ayette göz toprağın kendisine çevrilir. Arapçada iyi toprağın sıfatı yumuşaklıktır: {ar:أرض أريضة لينة طيبة, tr:ardun erîdatun leyyinatun tayyibe, gloss:yumuşak ve verimli toprak, source:"ء ر ض,B002"}. Bu, nâime'nin tanımındaki yumuşaklığın aynısıdır. Göğe verilen adlardan biri de bulut ve yağmurdur: {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tüsemmi's-sehâbe semâen ve'l-matara semâ', gloss:Araplar buluta da yağmura da gök der, source:"س م و,B004"}. Böylece göğe ve yere yöneltilen bakış, iki yüzün farkını da gösterir: yere su iner ya da inmez.

Kur'an iki yüzü başka yerlerde de aynı sözlerle karşı karşıya koyar. Güzel davrananlar için {ar:وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌۭ وَلَا ذِلَّةٌ, tr:ve lâ yerhaku vucûhehum katerun ve lâ zille, gloss:yüzlerini ne toz ne aşağılanma bürür, source:10:26} denir. İyilerin yüzü için {ar:تَعْرِفُ فِى وُجُوهِهِمْ نَضْرَةَ ٱلنَّعِيمِ, tr:ta'rifu fî vucûhihim nadrate'n-naîm, gloss:yüzlerinde nimetin tazeliğini tanırsın, source:83:24} denir. Burada nimet kelimesi nâime ile aynı köktendir. O günün yüzleri {ar:وُجُوهٌۭ يَوْمَئِذٍۢ نَّاضِرَةٌ, tr:vucûhun yevmeizin nâdıra, gloss:o gün birtakım yüzler taptaze, source:75:22} ve {ar:وَوُجُوهٌۭ يَوْمَئِذٍۭ بَاسِرَةٌۭ, tr:ve vucûhun yevmeizin bâsira, gloss:birtakım yüzler de asık, source:75:24} diye ikiye ayrılır. Sabredenlere verilen karşılık da surenin iki kelimesini bir arada söyler: {ar:وَلَقَّىٰهُمْ نَضْرَةًۭ وَسُرُورًۭا, tr:ve lakkâhum nadraten ve surûrâ, gloss:onlara tazelik ve sevinç kavuşturdu, source:76:11}. Üçüncü ayetteki yorgunluk bahçede ortadan kaldırılır. Pınarlı bahçelerdeki takva sahipleri için {ar:لَا يَمَسُّهُمْ فِيهَا نَصَبٌۭ, tr:lâ yemessuhum fîhâ nasab, gloss:orada onlara yorgunluk dokunmaz, source:15:48} denir. Bahçe halkı da aynı sözü kendisi söyler: {ar:لَا يَمَسُّنَا فِيهَا نَصَبٌۭ وَلَا يَمَسُّنَا فِيهَا لُغُوبٌۭ, tr:lâ yemessunâ fîhâ nasabun ve lâ yemessunâ fîhâ luğûb, gloss:burada bize ne yorgunluk dokunur ne bitkinlik, source:35:35}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:2 خَٰشِعَةٌ خ ش ع B002; 88:3 نَّاصِبَةٌ ن ص ب B004; 88:5 تُسْقَىٰ س ق ي B001; 88:6 ضَرِيعٍ ض ر ع B002; 88:6 ضَرِيعٍ ض ر ع B003; 88:8 نَّاعِمَةٌ ن ع م B002; 88:8 نَّاعِمَةٌ ن ع م B009; 88:9 رَاضِيَةٌ ر ض و B001; 88:12 عَيْنٌ ع ي ن B006; 88:13 سُرُرٌ س ر ر B010; 88:13 سُرُرٌ س ر ر B011; 88:18 ٱلسَّمَآءِ س م و B004; 88:20 ٱلْأَرْضِ ء ر ض B002

## Ateş, kaynar su ve pişme

Dördüncü ayet şöyledir: {ar:تَصْلَىٰ نَارًا حَامِيَةًۭ, tr:taslâ nâran hâmiye, gloss:kızgın bir ateşe girer, source:88:4}. Fiil, ateşin içine girip onun sıcaklığına katlanmayı anlatır: {ar:صلي الرجل نارا إذا أدخلته النار, tr:saliye'r-raculu nâran izâ edhaltehu'n-nâr, gloss:adamı ateşe soktuğunda saliye denir, source:"ص ل ي,B003"}. Fiili açıklayan cümlede, ateşe gireni surenin kendisi adlandırır: {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:salâ'l-kâfiru nâran fe-huve yaslâhâ ey kâsâ harrahâ ve şiddetehâ, gloss:kâfir ateşe girdi yani sıcaklığına ve şiddetine katlandı, source:"ص ل ي,B003"}. Dördüncü ayetteki fiil ile yirmi üçüncü ayetteki inkâr, bu cümlede birleşir. Ateşin sıfatı, demirin ateşte kızdırılmasını anlatan kelimedir: {ar:الحامية الحارة, tr:el-hâmiyetü'l-hârra, gloss:hâmiye sıcak olandır, source:"ح م ي,B001"}; {ar:أحميت الحديد في النار فهو محمى, tr:ahmeytü'l-hadîde fi'n-nâri fe-huve muhmâ, gloss:demiri ateşte kızdırdım; o kızgındır, source:"ح م ي,B001"}. Beşinci ayetteki pınarın sıfatı ise sıcaklığın en uç noktasıdır: {ar:حميم آن قد انتهى حره وعين آنية, tr:hamîmun ân kad intehâ harruhû ve aynun âniye, gloss:sıcaklığı son noktaya varmış kaynar su ve âniye pınar, source:"ء ن ي,B003"}; {ar:بلغ إناه من شدة الحر, tr:belağa inâhu min şiddeti'l-harr, gloss:sıcaklığın şiddetinden son noktasına vardı, source:"ء ن ي,B003"}. Surenin "âniye pınar" sözü, Arapçada böyle bir terkip olarak da kullanılır.

Bu kelimeler mutfakta da kullanılır ve o kullanım ayetin anlamının yanında duyulur. Ateşe girme fiili et kızartmayı da anlatır: {ar:صليت اللحم صليا شويته, tr:saleytü'l-lahme salyen şeveytüh, gloss:eti kızarttım, source:"ص ل ي,B004"}. Ateşin sıfatı kızmış fırın için de söylenir: {ar:حمى النهار وحمي التنور أي اشتد حره, tr:hamiye'n-nehâru ve hamiye't-tennûru ey iştedde harruh, gloss:gün ve tandır kızdı, sıcaklığı arttı, source:"ح م ي,B001"}. Pınarın sıfatının kökü yemeğin pişme anını adlandırır: {ar:انتظرنا إنى الطعام أي إدراكه, tr:intazarnâ inâ't-taâmi ey idrâkeh, gloss:yemeğin pişmesini bekledik, source:"ء ن ي,B003"}. Yiyecek adı ضريع'in kökü de tencerenin pişmek üzere olduğunu söyler: {ar:ضرعت القدر أي حان أن تدرك, tr:daraati'l-kıdru ey hâne en tudrik, gloss:tencerenin pişme vakti geldi, source:"ض ر ع,B007"}. Üçüncü ayetteki yorgunluk kelimesinin kökü de ocağın üstüne kurulan sacayağına ad verir: {ar:نصبت للقطاة شركا ونصبت للقدر نصبا, tr:nasabtü li'l-katâti şereken ve nasabtü li'l-kıdri nasbâ, gloss:bağırtlağa tuzak kurdum ve tencereye ayak kurdum, source:"ن ص ب,B001"}. Böylece dördüncü, beşinci ve altıncı ayetlerin kelimeleri bir mutfağın dilini konuşur: kızgın fırın, kızaran et, son kıvamına varan sıcaklık, pişmek üzere olan tencere. Kur'an bu dili ateş için açıkça kullanır: {ar:سَوْفَ نُصْلِيهِمْ نَارًۭا كُلَّمَا نَضِجَتْ جُلُودُهُم بَدَّلْنَٰهُمْ جُلُودًا غَيْرَهَا لِيَذُوقُوا۟ ٱلْعَذَابَ, tr:sevfe nuslîhim nâran küllemâ nadicet cülûduhum beddelnâhum cülûden ğayrahâ li-yezûku'l-azâb, gloss:onları ateşe sokacağız; derileri piştikçe azabı tatsınlar diye başka derilerle değiştireceğiz, source:4:56}. Bu ayette ateşe sokma fiili, pişme fiili ve tatma fiili bir aradadır. Mümin kıvamını beklemesin diye uyarılan yemeğin dili de aynıdır. Allah, müminlere Peygamber'in evlerine nasıl girileceğini öğretirken şöyle der: {ar:إِلَىٰ طَعَامٍ غَيْرَ نَٰظِرِينَ إِنَىٰهُ, tr:ilâ taâmin ğayra nâzırîne inâh, gloss:pişme vaktini gözetmeden bir yemeğe, source:33:53}. Bu tek ayette beşinci ayetteki pişme anının kökü, altıncı ayetteki yemek ve on yedinci ayetteki bakış kelimesi bir araya gelir.

Aynı iki komşu kelime, üçüncü ayetteki nâsıba ile dördüncü ayetteki taslâ, avcı dilinde de birbirine bağlanır. Kurmak fiili tuzak kurmayı anlatır, ve ateşe girme kökü tuzağın adıdır. Bu tuzak da kurmak fiiliyle tanımlanır: {ar:المصلاة أن تنصب شركا ونحوه, tr:el-maslâtü en tensibe şereken ve nahveh, gloss:maslât tuzak ve benzerini kurmaktır, source:"ص ل ي,B005"}. Bu yan anlamda emeğiyle yorulan yüz, kendi kurduğu tuzağa yürüyen kuş gibidir. Ayetteki anlam yine yorgunluk ve ateştir.

Kur'an bu ateşi başka yerlerde de aynı kelimelerle anar. Kâria suresinde terazisi hafif gelen için {ar:نَارٌ حَامِيَةٌۢ, tr:nârun hâmiye, gloss:kızgın bir ateş, source:101:11} denir. Önceki surede hatırlatmadan kaçan bedbaht {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâre'l-kübrâ, gloss:en büyük ateşe girecek olan, source:87:12} diye anılır. Leyl suresi ateşe gireni surenin yirmi üçüncü ayetindeki fiille tanımlar: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girmez, source:92:15}; {ar:ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ, tr:ellezî kezzebe ve tevellâ, gloss:yalanlayıp yüz çeviren, source:92:16}. Kaynar su da başka yerlerde aynı sıfatla geçer: {ar:يَطُوفُونَ بَيْنَهَا وَبَيْنَ حَمِيمٍ ءَانٍۢ, tr:yetûfûne beynehâ ve beyne hamîmin ân, gloss:onunla son noktasına varmış kaynar su arasında dolaşırlar, source:55:44}. Kaynar sudan içirilenler için {ar:وَسُقُوا۟ مَآءً حَمِيمًۭا فَقَطَّعَ أَمْعَآءَهُمْ, tr:ve sukû mâen hamîmen fe-kattaa em'âehum, gloss:kaynar su içirilip bağırsakları parçalanır, source:47:15} denir. Allah Peygamber'e "hak Rabbinizdendir, dileyen inansın, dileyen inkâr etsin" demesini söyledikten sonra yardım isteyenlere verilecek suyu anlatır: {ar:بِمَآءٍۢ كَٱلْمُهْلِ يَشْوِى ٱلْوُجُوهَ, tr:bi-mâin ke'l-mühli yeşvi'l-vucûh, gloss:yüzleri kavuran erimiş maden gibi bir su, source:18:29}. Buradaki "kavurmak" fiili, eti kızartmanın açıklamasında geçen fiildir. Kaynar su yüze dökülür ve onu pişirir. Zakkum ağacı günahkârın yiyeceğidir: {ar:كَٱلْمُهْلِ يَغْلِى فِى ٱلْبُطُونِ, tr:ke'l-mühli yağlî fi'l-butûn, gloss:erimiş maden gibi karınlarda kaynar, source:44:45}; {ar:كَغَلْىِ ٱلْحَمِيمِ, tr:ke-ğalyi'l-hamîm, gloss:kaynar suyun kaynaması gibi, source:44:46}. Kur'an bunu içenlerin nasıl içtiğini de söyler: {ar:فَشَٰرِبُونَ شُرْبَ ٱلْهِيمِ, tr:fe-şâribûne şurbe'l-hîm, gloss:susuzluk hastalığına tutulmuş develer gibi içerler, source:56:55}.

Kaynaklar: 88:3 نَّاصِبَةٌ ن ص ب B001; 88:4 تَصْلَىٰ ص ل ي B003; 88:4 تَصْلَىٰ ص ل ي B004; 88:4 تَصْلَىٰ ص ل ي B005; 88:4 حَامِيَةً ح م ي B001; 88:5 ءَانِيَةٍ ء ن ي B003; 88:6 ضَرِيعٍ ض ر ع B007; 88:23 كَفَرَ ك ف ر B003

## İki pınar ve kaplar

Surede iki pınar vardır ve ikisi de aynı adı taşır. Beşincisi {ar:مِنْ عَيْنٍ ءَانِيَةٍۢ, tr:min aynin âniye, gloss:son noktasına varmış sıcak bir pınardan, source:88:5}, on ikincisi ise {ar:فِيهَا عَيْنٌۭ جَارِيَةٌۭ, tr:fîhâ aynun câriye, gloss:orada akan bir pınar vardır, source:88:12}. Ad aynıdır, değişen yalnızca sıfattır. Birinde su sıcaklığın sonuna varmıştır. Ötekinde hareket halindedir: {ar:جرى الماء يجري جرية وجريا وجريانا, tr:cera'l-mâu yecrî cireten ve ceryen ve cereyânâ, gloss:su aktı, source:"ج ر ي,B001"}. Kaynayan suyun durduğu bir yer vardır, ama akan su yenilenir. Kur'an bu iki pınarı aynı surede, birkaç ayet arayla yan yana koyar. Biri günahkârların dolaştığı {ar:حَمِيمٍ ءَانٍۢ, tr:hamîmin ân, gloss:son noktasına varmış kaynar su, source:55:44} ve diğeri Rabbinin makamından korkanların iki bahçesinde akan sudur: {ar:فِيهِمَا عَيْنَانِ تَجْرِيَانِ, tr:fîhimâ aynâni tecriyân, gloss:ikisinde de akan iki pınar vardır, source:55:50}.

Beşinci ayetteki sıfatın harfleri, Arapçada kap anlamına gelen kelimenin çoğuluyla da aynıdır: {ar:الإناء معروف وجمعه آنية والأواني, tr:el-inâu ma'rûfun ve cem'uhû âniyetun ve'l-evânî, gloss:kap bilinir; çoğulu âniye ve evânîdir, source:"ء ن ي,B004"}. Ayetteki anlam sıcaklıktır. Yanında ise kapların adı duyulur. On dördüncü ayet bu kapları bahçeye koyar: {ar:وَأَكْوَابٌۭ مَّوْضُوعَةٌۭ, tr:ve ekvâbun mevdûa, gloss:konmuş kadehler, source:88:14}. Kevb kulpsuz bir kadehtir: {ar:الكوب القدح لا عروة له, tr:el-kûbü'l-kadahu lâ urvete leh, gloss:kevb kulpsuz kadehtir, source:"ك و ب,B001"}. Konmuş olmak, kaldırılmışın karşıtıdır: {ar:وضعت الشيء أضعه وضعا وهو ضد رفعته, tr:vada'tü'ş-şey'e edauhû vad'an ve huve zıddü rafa'tüh, gloss:bir şeyi koydum; kaldırdım'ın zıddı, source:"و ض ع,B001"}. Kadehler el altında hazır durur, istenmeden önce oradadır. Kur'an aynı iki kelimeyi, yani kapların adını ve kadehleri, sabredenlerin karşılığını anlatırken yan yana getirir: {ar:وَيُطَافُ عَلَيْهِم بِـَٔانِيَةٍۢ مِّن فِضَّةٍۢ وَأَكْوَابٍۢ كَانَتْ قَوَارِيرَا۠, tr:ve yutâfu aleyhim bi-âniyetin min fiddatin ve ekvâbin kânet kavârîrâ, gloss:çevrelerinde gümüş kaplar ve billur kadehler dolaştırılır, source:76:15}. Aynı ses bir yerde kaynayan pınarın sıfatıdır, başka bir yerde bahçenin gümüş kapları.

Bahçe halkı da içirilir. Fiil iki tarafta da aynıdır, değişen kaynaktır: {ar:وَيُسْقَوْنَ فِيهَا كَأْسًۭا كَانَ مِزَاجُهَا زَنجَبِيلًا, tr:ve yuskavne fîhâ ke'sen kâne mizâcuhâ zencebîlâ, gloss:orada zencefil katkılı bir kadehten içirilirler, source:76:17}; {ar:عَيْنًۭا فِيهَا تُسَمَّىٰ سَلْسَبِيلًۭا, tr:aynen fîhâ tusemmâ selsebîlâ, gloss:orada Selsebil denen bir pınardan, source:76:18}; {ar:يُسْقَوْنَ مِن رَّحِيقٍۢ مَّخْتُومٍ, tr:yuskavne min rahîkın mahtûm, gloss:mühürlü saf bir içkiden içirilirler, source:83:25}. Bahçenin pınarı insanın elinde akar: {ar:عَيْنًۭا يَشْرَبُ بِهَا عِبَادُ ٱللَّهِ يُفَجِّرُونَهَا تَفْجِيرًۭا, tr:aynen yeşrabu bihâ ibâdullâhi yufeccirûnehâ tefcîrâ, gloss:Allah'ın kullarının içtiği ve diledikleri yere fışkırttıkları bir pınar, source:76:6}. Kadehler de bu pınardan doldurulur: {ar:بِأَكْوَابٍۢ وَأَبَارِيقَ وَكَأْسٍۢ مِّن مَّعِينٍۢ, tr:bi-ekvâbin ve ebârîka ve ke'sin min maîn, gloss:kadehler ibrikler ve akan pınardan doldurulmuş kâse ile, source:56:18}. Buradaki "maîn" kelimesi gözle görünen akar suyu anlatır: {ar:ماء معين أي ظاهر للعيون, tr:mâun maînun ey zâhirun li'l-uyûn, gloss:gözlere açık akan su, source:"ع ي ن,B006"}. Allah, Peygamber'e bu suyun kimden geldiğini sormasını söyler: {ar:قُلْ أَرَءَيْتُمْ إِنْ أَصْبَحَ مَآؤُكُمْ غَوْرًۭا فَمَن يَأْتِيكُم بِمَآءٍۢ مَّعِينٍۭ, tr:kul e-raeytum in asbaha mâukum ğavran fe-men ye'tîkum bi-mâin maîn, gloss:de ki suyunuz yere çekilse size akar suyu kim getirir, source:67:30}.

Arapçada içmek de beslenmenin bir parçası sayılır: {ar:أصل في تذوق الشيء والطعام هو المأكول والإطعام يقع حتى الماء, tr:aslun fî tezevvuki'ş-şey'i ve't-taâmu huve'l-me'kûlu ve'l-it'âmu yekau hatta'l-mâ', gloss:tatma kökü; yemek yenendir; doyurmak suya bile uzanır, source:"ط ع م,B001"}. Böylece beşinci ve altıncı ayetler tek bir sofradır: içecek kaynar sudur, yemek de ضريع. Son ayetlerdeki azap kelimesinin kökü ise tatlı suyu da adlandırır: {ar:عذب الماء عذوبة فهو عذب طيب, tr:azube'l-mâu uzûbeten fe-huve azbun tayyib, gloss:su tatlılaştı; o tatlı ve hoş sudur, source:"ع ذ ب,B001"}. Bu anlam ayetteki cezanın yanında duyulur. Aynı harfler bir yerde tatlı su, başka bir yerde azaptır. Tatlı suyu bekleyen yüz, kaynar suyla karşılaşır.

Kaynaklar: 88:5 تُسْقَىٰ س ق ي B001; 88:5 ءَانِيَةٍ ء ن ي B003; 88:5 ءَانِيَةٍ ء ن ي B004; 88:6 طَعَامٌ ط ع م B001; 88:12 عَيْنٌ ع ي ن B006; 88:12 جَارِيَةٌ ج ر ي B001; 88:14 أَكْوَابٌ ك و ب B001; 88:14 مَّوْضُوعَةٌ و ض ع B001; 88:24 ٱلْعَذَابَ ع ذ ب B001

## Göz: yere atılan bakış ve serbest bakış

İkinci ayetteki eğiklik önce gözdedir: {ar:الخشوع رميك ببصرك إلى الأرض, tr:el-huşûu remyüke bi-basarike ile'l-ard, gloss:huşu bakışını yere atmandır, source:"خ ش ع,B001"}; {ar:خشع ببصره إذا غضه, tr:haşaa bi-basarihî izâ ğaddah, gloss:gözünü indirdiğinde haşaa denir, source:"خ ش ع,B001"}. O gün yüz yukarı bakamaz, bakışı toprağa düşer. Kur'an bu bakışı birkaç sahnede gösterir. Mezarlardan çıkış için {ar:خُشَّعًا أَبْصَٰرُهُمْ يَخْرُجُونَ مِنَ ٱلْأَجْدَاثِ, tr:huşşean ebsâruhum yahrucûne mine'l-ecdâs, gloss:gözleri eğik halde kabirlerden çıkarlar, source:54:7} denir. Sarsıntı günü için {ar:أَبْصَٰرُهَا خَٰشِعَةٌۭ, tr:ebsâruhâ hâşia, gloss:gözleri eğiktir, source:79:9} denir. Ateşe sunulan zalimler için ise eğiklik ile bakış bir arada anılır: {ar:يَنظُرُونَ مِن طَرْفٍ خَفِىٍّۢ, tr:yenzurûne min tarfin hafiyy, gloss:gizli bir göz ucuyla bakarlar, source:42:45}.

İki pınarın adı da gözdür: {ar:العين الناظرة لكل ذي بصر, tr:el-aynü'n-nâzıratü li-külli zî basar, gloss:gören her canlının bakan gözü, source:"ع ي ن,B001"}. Bu, ayetteki pınar anlamının yanında duyulur. On ikinci ayetteki pınarın suyu da göze açıktır: {ar:ماء معين أي ظاهر للعيون, tr:mâun maînun ey zâhirun li'l-uyûn, gloss:gözlere açık akan su, source:"ع ي ن,B006"}.

On yedinci ayet ise bugünün gözüne serbest bir bakış ister: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Bakmak düşünerek bakmak demektir: {ar:تأمل الشيء ومعاينته, tr:teemmülü'ş-şey'i ve muâyenetüh, gloss:bir şeyi düşünerek göz önünde tutmak, source:"ن ظ ر,B001"}; {ar:تقليب البصر والبصيرة لإدراك الشيء ورؤيته, tr:taklîbü'l-basari ve'l-basîreti li-idrâki'ş-şey'i ve ru'yetih, gloss:bir şeyi kavrayıp görmek için gözü ve gönül gözünü çevirmek, source:"ن ظ ر,B001"}. Bakmanın bir de boş kalan biçimi vardır: {ar:ينظرون إليك وهم لا يبصرون, tr:yenzurûne ileyke ve hum lâ yubsırûn, gloss:sana bakarlar ama görmezler, source:"ن ظ ر,B012"}. Ayetteki soru bu boşluğa karşı sorulur. Bakış dört yöne gönderilir: el altındaki deveye, yukarıya, karşıya ve aşağıya. Gök her yanıyla üstte olandır: {ar:السماء كل ما علاك فأظلك, tr:es-semâu küllü mâ alâke fe-ezallek, gloss:gök seni aşıp gölgeleyen her şeydir, source:"س م و,B004"}. Yer ise aşağıda kalıp göğün karşısında durandır. İkinci ayetteki bakış yere düşmüştü ve kalkamıyordu. On yedinci ayetten yirminci ayete kadar bakış her yöne serbestçe döner. Sure, o gün eğilecek gözün bugün henüz bakabildiğini hatırlatır.

Kur'an aynı soruyu başka yerlerde de sorar. Bir uyarıcıya ve toprak olduktan sonra diriltilmeye şaşanlara şöyle denir: {ar:أَفَلَمْ يَنظُرُوٓا۟ إِلَى ٱلسَّمَآءِ فَوْقَهُمْ كَيْفَ بَنَيْنَٰهَا, tr:e-fe-lem yenzurû ile's-semâi fevkahum keyfe beneynâhâ, gloss:üstlerindeki göğe bakmadılar mı onu nasıl kurduk, source:50:6}. Başka bir soru bakışı habere bağlar: {ar:أَوَلَمْ يَنظُرُوا۟ فِى مَلَكُوتِ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:e-ve-lem yenzurû fî melekûti's-semâvâti ve'l-ard, gloss:göklerin ve yerin hükümranlığına bakmadılar mı, source:7:185}. Aynı ayet şöyle biter: {ar:فَبِأَىِّ حَدِيثٍۭ بَعْدَهُۥ يُؤْمِنُونَ, tr:fe-bi-eyyi hadîsin ba'dehû yu'minûn, gloss:bundan sonra hangi habere inanacaklar, source:7:185}. Dünyaya bakmak ile ilk ayetteki haber burada birleşir. Bakış diriltmeye de bağlanır: {ar:قُلْ سِيرُوا۟ فِى ٱلْأَرْضِ فَٱنظُرُوا۟ كَيْفَ بَدَأَ ٱلْخَلْقَ ۚ ثُمَّ ٱللَّهُ يُنشِئُ ٱلنَّشْأَةَ ٱلْءَاخِرَةَ, tr:kul sîrû fi'l-ardi fenzurû keyfe bedee'l-halka summallâhu yunşiu'n-neş'ete'l-âhira, gloss:de ki yeryüzünde gezin de yaratmayı nasıl başlattığına bakın; sonra Allah son yaratılışı yapacak, source:29:20}; {ar:فَٱنظُرْ إِلَىٰٓ ءَاثَٰرِ رَحْمَتِ ٱللَّهِ كَيْفَ يُحْىِ ٱلْأَرْضَ بَعْدَ مَوْتِهَآ, tr:fenzur ilâ âsâri rahmetillâhi keyfe yuhyi'l-arda ba'de mevtihâ, gloss:Allah'ın rahmetinin izlerine bak; yeri ölümünden sonra nasıl diriltir, source:30:50}. Bahçede ise bakış yükseltilmiş yerlerden yapılır: {ar:عَلَى ٱلْأَرَآئِكِ يَنظُرُونَ, tr:ale'l-erâiki yenzurûn, gloss:koltuklar üstünde bakarlar, source:83:23}. Bakışın varacağı en uç yer de şudur: {ar:إِلَىٰ رَبِّهَا نَاظِرَةٌۭ, tr:ilâ rabbihâ nâzıra, gloss:Rablerine bakan, source:75:23}.

Kaynaklar: 88:2 خَٰشِعَةٌ خ ش ع B001; 88:5 عَيْنٍ ع ي ن B001; 88:12 عَيْنٌ ع ي ن B001; 88:12 عَيْنٌ ع ي ن B006; 88:17 يَنظُرُونَ ن ظ ر B001; 88:17 يَنظُرُونَ ن ظ ر B012; 88:18 ٱلسَّمَآءِ س م و B004; 88:20 ٱلْأَرْضِ ء ر ض B001

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

