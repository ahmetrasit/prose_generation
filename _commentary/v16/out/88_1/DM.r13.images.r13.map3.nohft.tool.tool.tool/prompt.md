Focus: 88:1. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/88_1/D.r13/context.md =====
# 88:1 — focus

هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ

Anchor translation (canonical reading, reference only):

Kaplayanın haberi sana geldi mi?

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | هَلْ | هَل |  | INTG |
| 2 | أَتَىٰكَ | أَتَى | ء ت ي | V;PRON |
| 3 | حَدِيثُ | حَدِيث | ح د ث | N |
| 4 | ٱلْغَٰشِيَةِ | غَٰشِيَة | غ ش و | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 88 — full text (context; no pericope)

- 88:1 ◀ focus هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ
- 88:2 وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ
- 88:3 عَامِلَةٌۭ نَّاصِبَةٌۭ
- 88:4 تَصْلَىٰ نَارًا حَامِيَةًۭ
- 88:5 تُسْقَىٰ مِنْ عَيْنٍ ءَانِيَةٍۢ
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


===== _commentary/v16/work/88_1/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء ت ي (root_000009) — identity root of أَتَىٰكَ (w2)

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

## ح د ث (root_000299) — identity root of حَدِيثُ (w3)

- **B001** yokken var olma, var etme veya gerçekleşme — sonradan var olma · var etmek, ortaya çıkarmak · bir iş gerçekleşti · sonradan var edilmiş şey · eskiden beri olanlarla sonradan gerçekleşenlerin tümü · inanç ve uygulamalara sonradan eklenen yenilikler
  كون الشيء لم يكن (maqayis)؛ الحديث نقيض القديم والحدوث كون شيء لم يكن وأحدثه الله فحدث وحدث أمر أي وقع (sihah)؛ الحدوث كون الشيء بعد أن لم يكن وإحداثه إيجاده والمحدث ما أوجد بعد أن لم يكن (mufradat)
- **B002** genç, yeni ya da taze olma — yeni · genç, yaşı küçük · yaşı genç · gençler, delikanlılar · gençliğin ilk çağı · daha başlangıcındayken · taze meyve · yakın zamanda yapılmış ya da söylenmiş
  الرجل الحدث الطري السن (maqayis)؛ شاب حدث وشابة حدثة فتية في السن والحديث الجديد من الأشياء (ayn)؛ رجل حدث السن وحديث السن (jamhara)؛ رجل حدث أي شاب وهؤلاء غلمان حدثان وأوله وطراءته (sihah)؛ شاب حدث فتي السن وحدثان شبابه وحديث شبابه (tahdhib)؛ الحديث الطري من الثمار ورجل حدث وحديث السن بمعنى (mufradat)
- **B003** söz, anlatım ve karşılıklı konuşma — söz, aktarılan bilgi · anlatılar, aktarılan sözler · düşte insana söylenenler · bilgi verme, anlatma · karşılıklı konuşma · güzel ya da çok konuşan adam · çok konuşan adam · kadınlarla konuşup görüşen kimse · hükümdarların konuşma ve gece oturma arkadaşı · güzel söz söyleme niteliği · tek bir anlatı veya konuşma konusu
  الحديث لأنه كلام يحدث منه الشيء بعد الشيء ورجل حدث حسن الحديث وحدث نساء (maqayis)؛ الأحدوثة الحديث نفسه ورجل حدث كثير الحديث (ayn)؛ رجل حدث حسن الحديث وحدث نساء (jamhara)؛ الحديث الخبر والمحادثة والتحدث والتحادث والتحديث معروفات ورجل حديث كثير الحديث (sihah)؛ الحديث ما يحدث به المحدث تحديثا ورجل حدث أي كثير الحديث والأحاديث في الفقه وغيره معروفة (tahdhib)؛ كل كلام يبلغ الإنسان من جهة السمع أو الوحي يقال له حديث وحادثته وحدثته وتحادثوا (mufradat)
- **B004** insanların dilinde anlatı konusu olma — hakkında konuşulan kişi, olay veya anlatı · insanların diline düşmek · onları dilden dile aktarılan örneklere çevirdik
  صار فلان أحدوثة أي كثروا فيه الأحاديث (ayn)؛ الأحدوثة ما يتحدث به (sihah)؛ صار فلان أحدوثة أي أكثروا فيه الأحاديث (tahdhib)؛ فجعلناهم أحاديث أي أخبارا يتمثل بهم وصار أحدوثة (mufradat)
- **B005** baş gösteren ağır olay — beklenmedik ağır olay · zamanın getirdiği sıkıntılı olaylar · ortaya çıkan ağır olay
  الحدث من أحداث الدهر شبه النازلة (ayn)؛ حدثان الدهر نوائبه (jamhara)؛ الحدث والحدثى والحادثة والحدثان كلها بمعنى (sihah)؛ حدثان الدهر حوادثه والحدثان إذا ألمت بنا (tahdhib)؛ الحادثة النازلة العارضة وجمعها حوادث (mufradat)
- **B006** ortaya koyma ve görünür kılma — ortaya koyma, görünür kılma
  الحدث الإبداء (ayn)؛ الحدث الإبداء (tahdhib)
- **B007** parlatıp arındırma — kılıcı parlatıp cilalama · adam kılıcını parlattı ve cilaladı · bu yürekleri öğütlerle arındırın
  محادثة السيف جلاؤه (sihah)؛ أحدث الرجل سيفه وحادثه إذا جلاه وحادثوا هذه القلوب أي اجلوها بالمواعظ (tahdhib)
- **B008** doğru sezişli, içine esin doğan kimse — doğru sezili veya içine doğru düşünce doğan kimse
  الرجل الصادق الظن محدث بفتح الدال مشددة (sihah)؛ إن يكن في هذه الأمة محدث فهو عمر وإنما يعني من يلقى في روعه من جهة الملإ الأعلى شيء (mufradat)

## غ ش و (root_001088) — identity root of ٱلْغَٰشِيَةِ (w4)

- **B001** örtme ve perdeleme — bir şeyin üstünü örtmek · örtü · gözü veya gönlü örten perde · göz perdesi · örtmek veya görüşü engellemek · giysisiyle örtünmek · giysisiyle örtünmek · eyer örtüsü
  أصل صحيح يدل على تغطية شيء بشيء (maqayis)؛ الغشاوة ما غشي القلب من رين الطبع (ayn)؛ الغشاء الغطاء وغشاوة أي غطاء وتغطيته واستغشى بثوبه (sihah)؛ الغشاوة ما غشي القلب من الطبع والغشاء الغطاء وغاشية السرج غطاؤه والرجل يستغشي ثوبه (tahdhib)؛ الغشاوة ما يغطى به الشيء واستغشوا ثيابهم (mufradat)
- **B002** her yanı saran büyük olay — dünyanın sonu ve hesap günü · herkesi kuşatan ağır karşılık veya bela · karnında ağır bir hastalığa tutuldu
  الغاشية القيامة لأنها تغشى الخلق بإفزاعها ورماه الله بغاشية وهو داء يأخذ كأنه يغشاه (maqayis)؛ الغاشية القيامة لأنها تغشى بإفزاعها ورماه الله بغاشية وهي داء يأخذ في الجوف (sihah)؛ غاشية من عذاب الله أي عقوبة مجللة تعمهم وغاشية اسم من أسماء القيامة وداء يأخذه في جوفه (tahdhib)؛ الغاشية كل ما يغطي الشيء ونائبة تغشاهم وتجللهم وكناية عن القيامة (mufradat)
- **B003** gelip uğrama — yanına gelmek · bir yere gelmek · bir kimsenin ziyaretçileri ve gelip gidenleri
  غشيه غشيانا أي جاءه (sihah)؛ الغاشية السؤال الذين يغشونك وغاشية الرجل من ينتابه من زواره وأصدقائه (tahdhib)؛ غشيت موضع كذا أتيته (mufradat)
- **B004** kadınla cinsel ilişkiyi dolaylı anlatma — kadınla birlikte olmak; cinsel ilişkiyi dolaylı anlatır · eşiyle birlikte olmak; cinsel ilişkiyi dolaylı anlatır
  الغشيان غشيان الرجل المرأة (maqayis)؛ غشيها غشيانا جامعها (sihah)؛ الغشيان كناية عن إتيان الرجل المرأة وتغشى امرأته (tahdhib)؛ غشيت موضع كذا أتيته وكني بذلك عن الجماع وغشاها وتغشاها (mufradat)
- **B005** bilincini yitirip bayılma — bilincini yitirip bayılmak · baygınlık; ölüm baygınlığı · baygın, bilinci kapalı
  غشي عليه غشية وغشيا وغشيانا فهو مغشي عليه (sihah)؛ غشي عليه فهو مغشي عليه وهي الغشية وكذلك غشية الموت (tahdhib)؛ غشي على فلان إذا نابه ما غشي فهمه (mufradat)
- **B006** kamçı veya kılıçla vurma — bir kimseye kamçıyla vurmak · üzerine kamçı veya kılıç darbesi indirmek
  غشيت الرجل بالسوط ضربته (sihah)؛ غشيته سوطا أو سيفا ككسوته وعممته (mufradat)
- **B007** hayvanın başını veya yüzünü kaplayan aklık — başı bütünüyle ak at · yüzü bütünüyle ak keçi · keçinin yüzünü kaplayan aklık
  الأعشى من الخيل وغيرها ما ابيض رأسه كله وعنزة غشواء بينة الغشا (sihah)؛ الغشواء من المعزى التي يغشى وجهها كله بياض (tahdhib)

## ECHO غ ش ي (root_001089) — for ٱلْغَٰشِيَةِ (w4): withheld observed target; not identity

- **B001** örtüp kapatma ve örten şey — bir şeyin üstünü örtüp kapatmak · örtü; kaplayıcı tabaka · bir şeyi, gözü veya gönlü örten perde · görüşü kapatan perde · kılıcın ve yük semerinin örtüsü · eyer örtüsü · görmemek ve işitmemek için giysisine bürünmek · giysisine bürünmek · bir şeyi başka bir şeyin üstünü örter duruma getirmek · bir şeyi örten şey · üstten kaplayan örtüler
  يدل على تغطية شيء بشيء (maqayis)؛ الغشاء الغطاء (maqayis;sihah;tahdhib)؛ غاشية السيف والرحل غطاؤه (ayn)؛ غاشية السرج غطاؤه (tahdhib)؛ جعل على بصره غشوة وغشاوة أي غطاء (sihah)؛ يستغشي ثوبه كي لا يسمع ولا يرى (ayn;tahdhib)؛ الغشاوة ما يغطى به الشيء (mufradat)
- **B002** herkesi kuşatan son gün veya ağır yıkım — dünyanın son bulup herkesin yeniden diriltileceği gün · Tanrı'dan gelen, herkesi kuşatan ağır ceza
  الغاشية القيامة لأنها تغشى الخلق بإفزاعها (maqayis;sihah)؛ الغاشية القيامة (ayn)؛ الغاشية اسم من أسماء القيامة في القرآن (tahdhib)؛ غاشية من عذاب الله أي عقوبة مجللة تعمهم (tahdhib)؛ نائبة تغشاهم وتجللهم (mufradat)
- **B003** içini tutan hastalığa uğrama [kalıp] — kişinin içini tutan bir hastalığa uğraması
  رماه الله بغاشية وهو داء يأخذ كأنه يغشاه (maqayis)؛ رماه الله بغاشية وهي داء يأخذ في الجوف (sihah)؛ رماه الله بغاشية وهو داء يأخذه في جوفه (tahdhib)
- **B004** kadınla cinsel birleşmeyi örtmeceli anlatma — erkeğin kadınla cinsel birleşmesi · kadınla cinsel birleşmeye girmek · karısıyla cinsel birleşmeye girmek
  الغشيان غشيان الرجل المرأة (maqayis)؛ الغشيان إتيان الرجل المرأة (ayn)؛ غشيها غشيانا جامعها (sihah)؛ الغشيان كناية عن إتيان الرجل المرأة (tahdhib)؛ كني بذلك عن الجماع يقال غشاها وتغشاها (mufradat)
- **B005** birine veya bir yere gelme ve gelip gidenler — yanına gelmek · bir yere gelmek · iyilik umarak gelenler ve ziyaretçiler · bir kişinin ziyaretçileri ve dostları
  الغاشية الذين يغشونك يرجون فضلك (ayn)؛ غشيه غشيانا أي جاءه (sihah)؛ الغاشية السؤال الذين يغشونك يرجون فضلك ومعروفك (tahdhib)؛ غاشية الرجل من ينتابه من زواره وأصدقائه (tahdhib)؛ غشيت موضع كذا أتيته (mufradat)
- **B006** kırbaç veya kılıçla vurma [kalıp] — adama kırbaçla vurmak
  غشيت الرجل بالسوط ضربته (sihah)؛ غشيته سوطا أو سيفا ككسوته وعممته (mufradat)
- **B007** kavrayışı kapanıp bayılma — bilinci kapanıp bayılmak · baygınlık · baygın; bilinci kapalı · ölümü andıran baygınlık
  غشي عليه غشية وغشيا وغشيانا فهو مغشي عليه (sihah)؛ غشي عليه فهو مغشي عليه وهي الغشية وكذلك غشية الموت (tahdhib)؛ غشي على فلان إذا نابه ما غشي فهمه (mufradat)
- **B008** hayvanın yüzünü veya başını kaplayan beyazlık — yüzü bütünüyle beyaz keçi · başı bütünüyle beyaz, gövdesi başka renkte hayvan
  الأعشى من الخيل وغيرها ما ابيض رأسه كله من بين جسده (sihah)؛ عنز غشواء بينة الغشا (sihah)؛ الغشواء من المعزى التي يغشى وجهها كله بياض (tahdhib)

===== _commentary/v16/out/s088/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 88:1, and ## Buluşmalar) =====
## Örten: Gâşiye, bahçe ve örtüsünü yitiren

Sure bir soruyla açılır: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. Gâşiye "üstüne gelip örten" demektir. Kökün temel işi, bir şeyi başka bir şeyle kaplamaktır: {ar:أصل صحيح يدل على تغطية شيء بشيء, tr:aslun sahîhun yedullü alâ tağtiyeti şey'in bi-şey', gloss:bir şeyin başka bir şeyle örtülmesini gösteren sağlam kök, source:"غ ش و,B001"}. Kelimenin elle tutulur bir karşılığı da vardır. Eyerin üstüne atılan örtüye de bu ad verilir: {ar:وغاشية السرج غطاؤه, tr:ve ğâşiyetü's-serci ğıtâuhû, gloss:eyerin gâşiyesi onun örtüsüdür, source:"غ ش و,B001"}. Böyle bir örtü yukarıdan atılır, eyeri her yanından sarar ve altında kalanı gözden saklar. Kıyamet bu adla anıldığında aynı hareket bütün yaratılmışlara uygulanmış olur: {ar:الغاشية القيامة لأنها تغشى الخلق بإفزاعها, tr:el-ğâşiyetü'l-kıyâmetü li-ennehâ tağşe'l-halka bi-ifzâıhâ, gloss:Gâşiye kıyamettir çünkü yaratılmışları dehşetiyle örter, source:"غ ش و,B002"}. Örtü dışarıda da kalmaz. Aynı fiil, başa gelen bir şeyin aklı kapatmasını, yani bayılmayı da anlatır: {ar:غشي على فلان إذا نابه ما غشي فهمه, tr:ğuşiye alâ fülânin izâ nâbehû mâ ğaşiye fehmehû, gloss:başına gelen şey anlayışını örtünce falan bayıldı denir, source:"غ ش و,B005"}. Demek ki ilk ayetteki tek kelimede bir örtü duyulur: dışarıdan iner, her yanı kuşatır ve içeriye, akla kadar işler. Kelimeyi yalnızca "kıyamet" diye karşılamak bu hareketi kaybettirir.

Bu yazı boyunca geçerli bir kural var: Bir kelimenin akrabalarından gelen resimler, o kelimenin ayetteki anlamının yerine geçmez, o anlamın yanında duyulur. Gâşiye burada o günün adıdır. Eyer örtüsü ve baygınlık yalnızca bu adın nasıl işlediğini gösterir.

Örtünün ilk indiği yer yüzlerdir: {ar:وُجُوهٌۭ يَوْمَئِذٍ خَٰشِعَةٌ, tr:vucûhun yevmeizin hâşia, gloss:o gün birtakım yüzler eğik ve ezik, source:88:2}. Yüz, bir şeyin karşıya dönük ön tarafıdır: {ar:الوجه مستقبل كل شيء, tr:el-vechu müstakbelü külli şey', gloss:yüz her şeyin karşıya bakan önüdür, source:"و ج ه,B001"}. Kur'an bu sahneyi başka yerlerde açıkça kurar. Suçluların o gün zincirlere vurulduğu anlatılırken şöyle denir: {ar:سَرَابِيلُهُم مِّن قَطِرَانٍۢ وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:serâbîluhum min katırânin ve tağşâ vucûhehumu'n-nâr, gloss:gömlekleri katrandandır ve yüzlerini ateş örter, source:14:50}. Kötülük kazananlar için başka bir yerde verilen benzetme, örtüyü gecenin kendisinden yapar: {ar:كَأَنَّمَآ أُغْشِيَتْ وُجُوهُهُمْ قِطَعًۭا مِّنَ ٱلَّيْلِ مُظْلِمًا, tr:keennemâ uğşiyet vucûhuhum kıtaan mine'l-leyli muzlimâ, gloss:sanki yüzlerine karanlık geceden parçalar örtülmüş, source:10:27}.

Surenin ilk ve son adları tek bir ayette bir araya gelir. Yusuf kıssasının sonunda Allah, Peygamber'e insanların çoğunun inanmadığını söyledikten sonra sorar: {ar:أَفَأَمِنُوٓا۟ أَن تَأْتِيَهُمْ غَٰشِيَةٌۭ مِّنْ عَذَابِ ٱللَّهِ, tr:e-fe-eminû en te'tiyehum ğâşiyetun min azâbillâh, gloss:Allah'ın azabından örten bir şeyin kendilerine gelmesinden emin mi oldular, source:12:107}. Bu ayette surenin ilk fiili (gelmek), ilk adı (örten) ve yirmi dördüncü ayetteki azap aynı cümlededir. Kelimenin açıklaması da bunu söyler: {ar:غاشية من عذاب الله أي عقوبة مجللة تعمهم, tr:ğâşiyetun min azâbillâh ey ukûbetun mücellele teummuhum, gloss:hepsini saran ve kapsayan bir ceza, source:"غ ش و,B002"}. Duhan suresinde Allah, Peygamber'e şüphe içinde oyalananları gösterir ve göğün apaçık bir duman getireceği günü beklemesini söyler. O duman için de şöyle denir: {ar:يَغْشَى ٱلنَّاسَ ۖ هَٰذَا عَذَابٌ أَلِيمٌۭ, tr:yağşe'n-nâs hâzâ azâbun elîm, gloss:insanları örter; bu acı bir azaptır, source:44:11}. Azabın çabuk gelmesini isteyenler için de örtü dört yandan tamamlanır: {ar:يَوْمَ يَغْشَىٰهُمُ ٱلْعَذَابُ مِن فَوْقِهِمْ وَمِن تَحْتِ أَرْجُلِهِمْ, tr:yevme yağşâhumu'l-azâbu min fevkıhim ve min tahti ercülihim, gloss:azabın onları üstlerinden ve ayaklarının altından örteceği gün, source:29:55}. Eyer örtüsü yalnızca üstten sarardı. Burada örtü alttan da kapanır.

Onuncu ayet ikinci bir örtü getirir: {ar:فِى جَنَّةٍ عَالِيَةٍۢ, tr:fî cennetin âliye, gloss:yüce bir bahçede, source:88:10}. Bu kökün aslı da örtmektir: {ar:أصل الجن ستر الشيء عن الحاسة, tr:aslu'l-cenni setru'ş-şey'i ani'l-hâsse, gloss:bir şeyi duyulardan gizlemek, source:"ج ن ن,B001"}. Bahçe adını ağaçlarının toprağı örtmesinden alır: {ar:كل بستان ذي شجر يستر بأشجاره الأرض, tr:küllü büstânin zî şecerin yesturu bi-eşcârihi'l-ard, gloss:ağaçlarıyla toprağı örten her bostan, source:"ج ن ن,B003"}. Ödül de bugün göze görünmeyen, örtülü bir şeydir: {ar:الجنة ما يصير إليه المسلمون في الآخرة وهو ثواب مستور عنهم اليوم, tr:el-cennetü mâ yasîru ileyhi'l-müslimûne fi'l-âhira ve huve sevâbun mestûrun anhumu'l-yevm, gloss:cennet bugün onlardan gizli olan ödüldür, source:"ج ن ن,B004"}. Aynı kökten kalkan da çıkar: {ar:المجن الترس والجنة الدرع وكل ما وقاك فهو جنتك, tr:el-micennu't-türsü ve'l-cünnetü'd-dir'u ve küllü mâ vakâke fe-huve cünnetük, gloss:seni koruyan her şey senin kalkanındır, source:"ج ن ن,B008"}. Böylece surede iki örtü karşı karşıya durur. Biri yukarıdan iner ve ezer. Öteki aşağıdan büyür, gölgeler ve korur. Bahçe halkı bu ikinci örtüyü birincisinden kurtuluş olarak anar. Birbirlerine dönüp ailelerinin arasındayken nasıl korku içinde yaşadıklarını hatırladıktan sonra şöyle derler: {ar:فَمَنَّ ٱللَّهُ عَلَيْنَا وَوَقَىٰنَا عَذَابَ ٱلسَّمُومِ, tr:fe-mennallâhu aleynâ ve vekânâ azâbe's-semûm, gloss:Allah bize lütfetti ve bizi kavurucu azaptan korudu, source:52:27}. Burada "korumak" fiili, kalkanın tanımındaki fiilin ta kendisidir. Dördüncü ayetteki ateş sıfatı حامية'nin kökü de başka kullanımında korunan yeri anlatır: {ar:الحمى موضع فيه كلأ يحمى من الناس أن يرعى, tr:el-himâ mevziun fîhi keleun yuhmâ mine'n-nâsi en yur'â, gloss:otlu olup insanların otlatmasından korunan yer, source:"ح م ي,B002"}. Bu anlam ayetteki kızgın ateşin yanında duyulur: aynı harflerin koruyan yüzü ateşe girenler için kapanmıştır.

Yirmi üçüncü ayetteki inkâr da bir örtme fiilidir: {ar:كل شيء غطى شيئا فقد كفره, tr:küllü şey'in ğattâ şey'en fe-kad keferahû, gloss:bir şeyi örten her şey onu kefr etmiştir, source:"ك ف ر,B001"}. Kelime imanın karşıtı olarak da bu yüzden kullanılır: {ar:الكفر ضد الإيمان سمى لأنه تغطية الحق, tr:el-küfru zıddü'l-îmân summiye li-ennehû tağtiyetü'l-hak, gloss:küfür imanın zıddıdır; hakkı örttüğü için bu adı almıştır, source:"ك ف ر,B003"}. Tohumu toprakla örten çiftçiye de bu ad verilir: {ar:الكافر الزارع لأنه يغطي البذر بالتراب, tr:el-kâfiru'z-zâriu li-ennehû yuğattı'l-bezra bi't-turâb, gloss:kâfir tohumu toprakla örten ekincidir, source:"ك ف ر,B008"}. Çiftçinin örtüsünden bir bahçe çıkabilir; hakkı örtenin örtüsünden hiçbir şey bitmez. Kur'an inkârla göz üstündeki örtüyü aynı ayette birleştirir. Uyarılsalar da uyarılmasalar da inanmayacakları söylenenler için şöyle denir: {ar:وَعَلَىٰٓ أَبْصَٰرِهِمْ غِشَٰوَةٌۭ ۖ وَلَهُمْ عَذَابٌ عَظِيمٌۭ, tr:ve alâ ebsârihim ğışâvetun ve lehum azâbun azîm, gloss:gözlerinin üstünde bir perde vardır ve onlar için büyük bir azap vardır, source:2:7}. Buradaki perde, Gâşiye ile aynı köktendir. Hakkı örten, sonunda kendi gözünün de örtüldüğünü görür. Gece de surenin üç ayrı kökünde örtü olarak anılır: {ar:الليل كافر لأنه ستر بظلمته, tr:el-leylü kâfirun li-ennehû setera bi-zulmetih, gloss:gece karanlığıyla örttüğü için kâfirdir, source:"ك ف ر,B002"}; {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰ, tr:ve'l-leyli izâ yağşâ, gloss:örttüğü zaman geceye andolsun, source:92:1}; İbrahim'in gece karşısındaki anında ise {ar:فَلَمَّا جَنَّ عَلَيْهِ ٱلَّيْلُ, tr:fe-lemmâ cenne aleyhi'l-leyl, gloss:gece onu örtünce, source:6:76}. Bunlar aynı kökten değildir. Üç ayrı kökün paylaştığı tek bir resimdir.

Son adım yirmi dördüncü ayettedir. Azap ceza demektir: {ar:العذاب العقوبة وقد عذبته تعذيبا, tr:el-azâbu'l-ukûbe ve kad azzebtühû ta'zîbâ, gloss:azap cezadır, source:"ع ذ ب,B005"}. Aynı kökün bir başka kolu ise örtüsüz kalmış insanı anlatır: {ar:العذوب الذي ليس بينه وبين السماء ستر وكذلك العاذب, tr:el-azûbu'llezî leyse beynehû ve beyne's-semâi sitr, gloss:kendisiyle gök arasında hiçbir örtü bulunmayan kimse, source:"ع ذ ب,B004"}. Bu anlam ayetteki cezanın yanında duyulduğunda resim tamamlanır. Azap gören hem ezici örtünün altında kalmış hem de kendisini koruyan bütün örtülerden soyulmuştur. Bahçedeki insanın üstünde ise ağaçlardan bir örtü vardır, onu ezen hiçbir şey yoktur.

Kaynaklar: 88:1 ٱلْغَٰشِيَةِ غ ش و B001; 88:1 ٱلْغَٰشِيَةِ غ ش و B002; 88:1 ٱلْغَٰشِيَةِ غ ش و B005; 88:2 وُجُوهٌ و ج ه B001; 88:4 حَامِيَةً ح م ي B002; 88:10 جَنَّةٍ ج ن ن B001; 88:10 جَنَّةٍ ج ن ن B003; 88:10 جَنَّةٍ ج ن ن B004; 88:10 جَنَّةٍ ج ن ن B008; 88:23 وَكَفَرَ ك ف ر B001; 88:23 وَكَفَرَ ك ف ر B002; 88:23 وَكَفَرَ ك ف ر B003; 88:23 وَكَفَرَ ك ف ر B008; 88:24 ٱلْعَذَابَ ع ذ ب B004; 88:24 ٱلْعَذَابَ ع ذ ب B005

## Kulağa gelen: haber, susan sesler, işitilmeyen söz

Sure göze değil kulağa seslenerek başlar. "Sana geldi mi" diye sorulan şey bir haberdir. Haber de kulaktan ulaşan sözdür: {ar:كل كلام يبلغ الإنسان من جهة السمع أو الوحي يقال له حديث, tr:küllü kelâmin yeblüğu'l-insâne min cihetí's-sem'i evi'l-vahyi yukâlü lehû hadîs, gloss:insana işitme ya da vahiy yoluyla ulaşan her söze hadîs denir, source:"ح د ث,B003"}. Kur'an aynı açılışı başka yerlerde de kullanır ve ardından her seferinde bir kıssa gelir: {ar:وَهَلْ أَتَىٰكَ حَدِيثُ مُوسَىٰٓ, tr:ve hel etâke hadîsü Mûsâ, gloss:Musa'nın haberi sana geldi mi, source:20:9}; {ar:هَلْ أَتَىٰكَ حَدِيثُ ضَيْفِ إِبْرَٰهِيمَ ٱلْمُكْرَمِينَ, tr:hel etâke hadîsü dayfi İbrâhîme'l-mükramîn, gloss:İbrahim'in ağırlanan misafirlerinin haberi sana geldi mi, source:51:24}; {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْجُنُودِ, tr:hel etâke hadîsü'l-cunûd, gloss:orduların haberi sana geldi mi, source:85:17}. Bunlarda anlatılan şey geçmişte kalmıştır. Bu surede ise henüz gelmemiş bir gün, gelmiş bir haber gibi anlatılır. Kelimenin bir kolu, haberlerde ibret olarak anlatılan insanlara da ad verir: {ar:فجعلناهم أحاديث أي أخبارا يتمثل بهم, tr:fe-cealnâhum ehâdîse ey ahbâran yütemesselü bihim, gloss:onları örnek gösterilen haberler yaptık, source:"ح د ث,B004"}. Bu anlam surenin haberinin yanında duyulur: haberi dinleyen, kendisi de bir haber olabilir.

İkinci ayetteki eğiklik sesleri de kapsar: {ar:خشعت الأصوات أي سكنت, tr:haşaati'l-asvâtu ey sekenet, gloss:sesler kısıldı yani dindi, source:"خ ش ع,B001"}. Kur'an bu susuşu Sur'a üfürülen günün sahnesinde gösterir. Herkes çağırıcının ardından sapmadan yürür: {ar:وَخَشَعَتِ ٱلْأَصْوَاتُ لِلرَّحْمَٰنِ فَلَا تَسْمَعُ إِلَّا هَمْسًۭا, tr:ve haşaati'l-asvâtu li'r-Rahmâni fe-lâ tesmeu illâ hemsâ, gloss:sesler Rahman'a karşı kısılır; bir fısıltıdan başkasını işitmezsin, source:20:108}. Bu ayetteki "işitmezsin" sözü, on birinci ayetteki ile harfi harfine aynıdır: {ar:لَّا تَسْمَعُ فِيهَا لَٰغِيَةًۭ, tr:lâ tesmeu fîhâ lâğiye, gloss:orada boş bir söz işitmezsin, source:88:11}. Böylece iki ayrı sessizlik ortaya çıkar. Birinde sesler korkudan kısılır. Ötekinde kulak çirkin sözden korunur. İşitmek, sesi kulakla yakalamaktır: {ar:إيناس الشيء بالأذن, tr:înâsu'ş-şey'i bi'l-üzün, gloss:bir şeyi kulakla fark etmek, source:"س م ع,B001"}. Bu kelime anlamayı ve söz dinlemeyi de içerir: {ar:تارة عن الفهم وتارة عن الطاعة, tr:târaten ani'l-fehmi ve târaten ani't-tâa, gloss:kimi zaman anlamayı kimi zaman itaati anlatır, source:"س م ع,B003"}. Bahçede işitilmeyen kelime de tek tek tanımlanır: {ar:لاغية كلمة قبيحة أو فاحشة, tr:lâğiyetun kelimetun kabîhatun ev fâhişe, gloss:çirkin ya da hayasız söz, source:"ل غ و,B002"}. Kökün bir kolu, anlamsız gürültüyü ve köpek havlamasını da anlatır: {ar:اللغا: الصوت مثل الوغا ونباح الكلب لغو أيضا, tr:el-leğâ es-savtu misle'l-vağâ ve nubâhu'l-kelbi lağvun eydan, gloss:gürültü; köpek havlaması da lağvdır, source:"ل غ و,B003"}. Kur'an bahçenin bu sessizliğini sık sık anlatır ve yerine konan sözü de söyler: {ar:لَّا يَسْمَعُونَ فِيهَا لَغْوًا إِلَّا سَلَٰمًۭا, tr:lâ yesmeûne fîhâ lağven illâ selâmâ, gloss:orada boş söz değil yalnız selam işitirler, source:19:62}; {ar:لَا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا تَأْثِيمًا, tr:lâ yesmeûne fîhâ lağven ve lâ te'sîmâ, gloss:orada ne boş söz işitirler ne günaha sokan söz, source:56:25}; {ar:إِلَّا قِيلًۭا سَلَٰمًۭا سَلَٰمًۭا, tr:illâ kîlen selâmen selâmâ, gloss:yalnızca selam selam diye bir söz, source:56:26}; {ar:لَّا يَسْمَعُونَ فِيهَا لَغْوًۭا وَلَا كِذَّٰبًۭا, tr:lâ yesmeûne fîhâ lağven ve lâ kizzâbâ, gloss:orada ne boş söz işitirler ne yalan, source:78:35}.

Yirmi birinci ayette haber çizgisi döner: {ar:فَذَكِّرْ إِنَّمَآ أَنتَ مُذَكِّرٌۭ, tr:fe-zekkir innemâ ente müzekkir, gloss:hatırlat; sen yalnızca hatırlatansın, source:88:21}. Hatırlatmak önce bir şeyi dile getirmektir: {ar:الذكر جري الشيء على لسانك, tr:ez-zikru ceryü'ş-şey'i alâ lisânik, gloss:zikir bir şeyin dilinden akmasıdır, source:"ذ ك ر,B004"}. Dinleyende ise unutmanın karşıtını uyandırmaktır: {ar:ذكرت الشيء خلاف نسيته, tr:zekertü'ş-şey'e hılâfe nesîtüh, gloss:hatırladım unuttum'un zıddıdır, source:"ذ ك ر,B003"}. Sure "sana geldi mi" diye başlamış, "sen hatırlatansın" diye bu çizgiyi kapatır. Habere ilk muhatap olan kişi, aynı haberi başkalarının kulağına ulaştıran olur.

Kaynaklar: 88:1 أَتَىٰكَ ء ت ي B001; 88:1 حَدِيثُ ح د ث B003; 88:1 حَدِيثُ ح د ث B004; 88:2 خَٰشِعَةٌ خ ش ع B001; 88:11 تَسْمَعُ س م ع B001; 88:11 تَسْمَعُ س م ع B003; 88:11 لَٰغِيَةً ل غ و B002; 88:11 لَٰغِيَةً ل غ و B003; 88:21 فَذَكِّرْ ذ ك ر B004; 88:21 مُذَكِّرٌ ذ ك ر B003

## Deve: sürü, süt ve yolculuk

Bakılacak dört şeyin ilki devedir. Gök, dağlar ve yer uzaktadır. Deve ise insanın yanındadır, insan onun üstündedir. Arapçada deve bir servettir: {ar:الإبل معروفة ورجل آبل ومال مؤبل, tr:el-ibilu ma'rûfetun ve racülün âbilün ve mâlün muebbel, gloss:deve bilinir; develi adam ve deveden oluşan mal, source:"ء ب ل,B001"}. Kökün bir kolu devenin suya muhtaç kalmadan yaşı otla yetinmesini anlatır: {ar:أبلت الإبل والوحش اجتزأت بالرطب عن الماء, tr:ebeleti'l-ibilu ve'l-vahşu'ctezeet bi'r-ratbi ani'l-mâ', gloss:develer ve yaban hayvanları sudan vazgeçip yaş otla yetindi, source:"ء ب ل,B002"}. Altıncı ve yedinci ayetlerde hiçbir şeyin yetmediği insanlar vardır. On yedinci ayette ise azla yetinen bir hayvana bakılması istenir.

Surenin önceki kelimelerinde de devenin bedeni yan anlam olarak duyulur. Nâime'nin kökü sürüye ad verir: {ar:النعم الإبل لما فيه من الخير والنعمة والأنعام البهائم, tr:en-neamu'l-ibilu limâ fîhi mine'l-hayri ve'n-ni'meti ve'l-en'âmu'l-behâim, gloss:neam devedir; içindeki hayır ve nimetten dolayı; en'âm hayvanlardır, source:"ن ع م,B005"}. Hâşia, yorgun düşmüş bir devenin hörgücünü anlatır: {ar:خشع سنام البعير إذا أنضي فذهب شحمه وتطأطأ شرفه, tr:haşaa senâmü'l-baîri izâ undiye fe-zehebe şahmuhû ve teta'tae şerefuh, gloss:yorulan devenin hörgücünün yağı gidip tepesi çöktü, source:"خ ش ع,B004"}. Âmile, çalışmaya yatkın soylu dişi deveye ad verir: {ar:اليعملة الناقة النجيبة المطبوعة على العمل, tr:el-ya'meletü'n-nâkatü'n-necîbetü'l-matbûatu ale'l-amel, gloss:çalışmaya yaratılışça yatkın soylu dişi deve, source:"ع م ل,B008"}. Ateşe girme fiilinin kökü bir bitkiye de ad verir: {ar:تسميها العرب خبزة الإبل, tr:tüsemmîhe'l-arabu hubzete'l-ibil, gloss:Araplar ona develerin ekmeği der, source:"ص ل ي,B010"}. Yemek, yağ ve deve tek bir cümlede birleşir: {ar:المطعم من الإبل الذي يوجد في مخه طعم الشحم وشاة طعوم فيها بعض السمن, tr:el-mut'imu mine'l-ibili'llezî yûcedu fî muhhihî ta'mu'ş-şahm ve şâtun taûmun fîhâ ba'du's-simen, gloss:iliğinde yağ tadı bulunan deve; biraz semizliği olan koyun, source:"ط ع م,B007"}. Mevdûa'nın kökü tuzlu otlakta yayılan develeri anlatır: {ar:الواضعات الإبل تأكل الخلة, tr:el-vâdiâtü'l-ibilu te'kulu'l-hulle, gloss:vâdiât hulle otunu yiyen develerdir, source:"و ض ع,B007"}. Masfûfe ise kurban için sıraya dizilen develeri anlatır: {ar:البدن الصواف التي تصفف ثم تنحر, tr:el-budnü's-savâffu'lletî tusaffefu summe tunhar, gloss:sıraya dizilip sonra kesilen kurbanlık develer, source:"ص ف ف,B001"}. Kur'an aynı kelimeyi kurbanlık develer için kullanır: {ar:فَٱذْكُرُوا۟ ٱسْمَ ٱللَّهِ عَلَيْهَا صَوَآفَّ, tr:fezkurusmallâhi aleyhâ savâff, gloss:sıraya dizilmişken üzerlerine Allah'ın adını anın, source:22:36}. O ayette sıra, anma ve doyurma bir aradadır. Ayet ardından {ar:وَأَطْعِمُوا۟ ٱلْقَانِعَ وَٱلْمُعْتَرَّ, tr:ve at'imu'l-kânia ve'l-mu'terr, gloss:yetineni ve isteyeni doyurun, source:22:36} der.

Süt de aynı kelimelerden geçer. Darî'in kökü memedir: {ar:الضرع لكل ذات خف أو ظلف, tr:ed-dar'u li-külli zâti huffin ev zılf, gloss:dar' tabanlı ve tırnaklı her hayvanın memesidir, source:"ض ر ع,B001"}. Merfûa'nın kökü sütünü memesinde tutan deveye ad verir: {ar:ناقة رافع إذا رفعت اللبأ في ضرعها, tr:nâkatun râfiun izâ rafeati'l-lebee fî dar'ihâ, gloss:ağız sütünü memesinde tutan dişi deveye râfi' denir, source:"ر ف ع,B007"}. Masfûfe'nin kökü tek sağımda kadehleri sıra sıra dolduran deveye ad verir: {ar:ناقة صفوف للتي تصف أقداحا من لبنها, tr:nâkatun safûfun li'lletî tesuffu akdâhan min lebenihâ, gloss:sütünden kadehleri sıra sıra dolduran dişi deve, source:"ص ف ف,B002"}. On dördüncü ayetteki kevb de böyle bir kadehtir. Besleme kelimesinin kökü sütten çıkan yağa ad verir: {ar:السمن سلاء اللبن, tr:es-semnu sulâü'l-leben, gloss:semn sütten eritilen yağdır, source:"س م ن,B002"}. Sulamanın kökü ise hem su hem süt taşıyan kırbayı anlatır: {ar:السقاء القربة للماء واللبن, tr:es-sikâü'l-kırbetü li'l-mâi ve'l-leben, gloss:su ve süt için kırba, source:"س ق ي,B004"}. Kur'an bu içirmeyi bir ibret olarak anlatır: {ar:نُّسْقِيكُم مِّمَّا فِى بُطُونِهِۦ مِنۢ بَيْنِ فَرْثٍۢ وَدَمٍۢ لَّبَنًا خَالِصًۭا سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:nuskîkum mimmâ fî butûnihî min beyni fersin ve demin lebenen hâlisan sâiğan li'ş-şâribîn, gloss:karınlarındakinden; fışkı ile kan arasından içenlerin boğazından kolayca geçen arı bir süt içiririz, source:16:66}. Buradaki fiil, beşinci ayetteki "içirilir" fiiliyle aynıdır. Kolay yutulan süt, cehennemdeki içeceğin tersidir: {ar:يَتَجَرَّعُهُۥ وَلَا يَكَادُ يُسِيغُهُۥ, tr:yetecerrauhû ve lâ yekâdu yusîğuh, gloss:yudum yudum içer ama yutamaz, source:14:17}. "Kolayca geçen" ve "yutamaz" aynı köktendir.

Yolculuk da aynı kelimelerden duyulur. Surenin ilk fiili, yürüyen bir devenin ön ayaklarının salınımını anlatır: {ar:ما أحسن أتو يدي هذه الناقة وأتي أيضا أي رجع يديها في السير, tr:mâ ahsene etve yedey hâzihi'n-nâka ey rac'a yedeyhâ fi's-seyr, gloss:bu devenin ön ayaklarını yürürken geri atışı ne güzel, source:"ء ت ي,B009"}. Son ayetten bir önceki ayetteki dönüş kelimesi de aynı salınımı ve gün boyu yürüyüşü anlatır: {ar:الأوب سرعة تقليب اليدين والرجلين في السير والتأويب أن تسير النهار أجمع وتنزل الليل, tr:el-evbü sur'atü taklîbi'l-yedeyni ve'r-ricleyni fi's-seyr ve't-te'vîbü en tesîra'n-nehâra ecmea ve tenzile'l-leyl, gloss:yürüyüşte el ve ayakları çabuk oynatmak; bütün gün yürüyüp gece konmak, source:"ء و ب,B003"}; {ar:كل راجع مع الليل فهو آئب, tr:küllü râciin mea'l-leyli fe-huve âib, gloss:gece olunca dönen herkes âibdir, source:"ء و ب,B006"}. Aradaki kelimeler de yürüyüşün türlerini adlandırır: {ar:نصب القوم ساروا يومهم وهو سير لين, tr:nasaba'l-kavmu sârû yevmehum ve huve seyrun leyyin, gloss:topluluk bütün gün yumuşak bir yürüyüşle yürüdü, source:"ن ص ب,B010"}; {ar:السعي عدو ليس بشديد, tr:es-sa'yu adven leyse bi-şedîd, gloss:sa'y şiddetli olmayan koşudur, source:"س ع ي,B001"}; {ar:مرفوع الناقة في سيرها خلاف الموضوع, tr:merfûu'n-nâkati fî seyrihâ hılâfu'l-mevdû', gloss:devenin yürüyüşünde merfû mevdûun zıddıdır, source:"ر ف ع,B003"}; {ar:وضع البعير وغيره أي أسرع في سيره, tr:vadaa'l-baîru ve ğayruhû ey esraa fî seyrih, gloss:deve hızlandı, source:"و ض ع,B003"}. Bunlar yan anlamlardır ve ayetlerin anlamının yerine geçmez. Ama surenin "geldi mi" ile başlayıp "dönüşleri" ile biten yolu, deve sürücülerinin bir günlük yürüyüşü anlattığı kelimelerle kurulmuştur.

Kur'an deveyi yaratılmış ve insana boyun eğdirilmiş bir nimet olarak anlatır: {ar:وَٱلْأَنْعَٰمَ خَلَقَهَا ۗ لَكُمْ فِيهَا دِفْءٌۭ وَمَنَٰفِعُ وَمِنْهَا تَأْكُلُونَ, tr:ve'l-en'âme halakahâ lekum fîhâ dif'un ve menâfiu ve minhâ te'kulûn, gloss:hayvanları yarattı; onlarda sizin için ısınma ve faydalar vardır ve onlardan yersiniz, source:16:5}; {ar:وَتَحْمِلُ أَثْقَالَكُمْ إِلَىٰ بَلَدٍۢ لَّمْ تَكُونُوا۟ بَٰلِغِيهِ إِلَّا بِشِقِّ ٱلْأَنفُسِ, tr:ve tahmilu eskâlekum ilâ beledin lem tekûnû bâliğîhi illâ bi-şıkkı'l-enfus, gloss:ancak canınızı tüketerek varabileceğiniz bir yere yüklerinizi taşırlar, source:16:7}. Başka bir ayette Allah'ın kendi işi anlatılır: {ar:أَوَلَمْ يَرَوْا۟ أَنَّا خَلَقْنَا لَهُم مِّمَّا عَمِلَتْ أَيْدِينَآ أَنْعَٰمًۭا, tr:e-ve-lem yerav ennâ halaknâ lehum mimmâ amilet eydînâ en'âmen, gloss:ellerimizin işinden onlar için hayvanlar yarattığımızı görmediler mi, source:36:71}; {ar:وَذَلَّلْنَٰهَا لَهُمْ فَمِنْهَا رَكُوبُهُمْ وَمِنْهَا يَأْكُلُونَ, tr:ve zellelnâhâ lehum fe-minhâ rakûbuhum ve minhâ ye'kulûn, gloss:onları kendilerine boyun eğdirdik; bir kısmına biner bir kısmından yerler, source:36:72}. Bu ayetteki "iş" kelimesi, üçüncü ayetteki âmile ile aynı köktendir, ama burada iş Allah'ındır. Boyun eğdirme fiili de aşağılanma kelimesiyle aynı köktendir, ama burada bir lütuf olarak hayvana uygulanır. Deve, surenin döşediği odayı da döşer: {ar:وَجَعَلَ لَكُم مِّن جُلُودِ ٱلْأَنْعَٰمِ بُيُوتًۭا, tr:ve ceale lekum min cülûdi'l-en'âmi buyûten, gloss:hayvanların derilerinden size evler yaptı, source:16:80}; {ar:وَمِنْ أَصْوَافِهَا وَأَوْبَارِهَا وَأَشْعَارِهَآ أَثَٰثًۭا وَمَتَٰعًا, tr:ve min asvâfihâ ve evbârihâ ve eş'ârihâ esâsen ve metâan, gloss:yünlerinden yapağılarından ve kıllarından ev eşyası ve kullanılacak şeyler, source:16:80}. Allah İbrahim'e insanları hacca çağırmasını söylerken develer de gelişin aracıdır: {ar:يَأْتُوكَ رِجَالًۭا وَعَلَىٰ كُلِّ ضَامِرٍۢ يَأْتِينَ مِن كُلِّ فَجٍّ عَمِيقٍۢ, tr:ye'tûke ricâlen ve alâ külli dâmirin ye'tîne min külli feccin amîk, gloss:yaya olarak ve her uzak yoldan gelen arık develer üstünde sana gelsinler, source:22:27}. Bakmanın yiyeceğe yöneltildiği yerde de hayvanlar anılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bu bakış {ar:مَّتَٰعًۭا لَّكُمْ وَلِأَنْعَٰمِكُمْ, tr:metâan lekum ve li-en'âmikum, gloss:size ve hayvanlarınıza bir yararlanma olarak, source:80:32} diye biter.

Kaynaklar: 88:1 أَتَىٰكَ ء ت ي B009; 88:2 خَٰشِعَةٌ خ ش ع B004; 88:3 عَامِلَةٌ ع م ل B008; 88:3 نَّاصِبَةٌ ن ص ب B010; 88:4 تَصْلَىٰ ص ل ي B010; 88:5 تُسْقَىٰ س ق ي B004; 88:6 ضَرِيعٍ ض ر ع B001; 88:6 طَعَامٌ ط ع م B007; 88:7 يُسْمِنُ س م ن B002; 88:8 نَّاعِمَةٌ ن ع م B005; 88:9 لِّسَعْيِهَا س ع ي B001; 88:13 مَّرْفُوعَةٌ ر ف ع B003; 88:13 مَّرْفُوعَةٌ ر ف ع B007; 88:14 مَّوْضُوعَةٌ و ض ع B003; 88:14 مَّوْضُوعَةٌ و ض ع B007; 88:15 مَصْفُوفَةٌ ص ف ف B001; 88:15 مَصْفُوفَةٌ ص ف ف B002; 88:17 ٱلْإِبِلِ ء ب ل B001; 88:17 ٱلْإِبِلِ ء ب ل B002; 88:25 إِيَابَهُمْ ء و ب B003; 88:25 إِيَابَهُمْ ء و ب B006

## Gelmek, sırt dönmek, dönüp varmak

Sure bir gelişle açılır. Gelmek, kolayca varmaktır: {ar:الإتيان مجيء بسهولة, tr:el-ityânu mecîun bi-suhûle, gloss:ityân kolayca gelmektir, source:"ء ت ي,B001"}. Bu geliş iyiliği de kötülüğü de getirebilir: {ar:الإتيان يقال في الخير وفي الشر, tr:el-ityânu yukâlü fi'l-hayri ve fi'ş-şerr, gloss:ityân hem hayır hem şer için söylenir, source:"ء ت ي,B011"}. İlk ayette iki geliş vardır. Haber gelir, haberin anlattığı şey de bir gelip örtmedir. Örtme fiili gelmek fiiliyle açıklanır: {ar:غشيت موضع كذا أتيته, tr:ğaşîtü mevdia kezâ eteytüh, gloss:falan yere ğaşîtü yani oraya geldim, source:"غ ش و,B003"}; {ar:غشيه غشيانا أي جاءه, tr:ğaşiyehû ğaşeyânen ey câeh, gloss:ona ğaşiye yani ona geldi, source:"غ ش و,B003"}. Böylece ilk ayetteki iki kelime birbirini açıklar. Kur'an iki gelişi aynı ayette yan yana koyar: {ar:أَوْ تَأْتِيَهُمُ ٱلسَّاعَةُ بَغْتَةًۭ وَهُمْ لَا يَشْعُرُونَ, tr:ev te'tiyehumu's-sââtu bağteten ve hum lâ yeş'urûn, gloss:ya da o saat onlar farkında değilken ansızın gelir, source:12:107}.

İkinci ayetteki yüz yönelimdir: {ar:الوجهة كل موضع استقبلته, tr:el-vichetü küllü mevdıin istakbeltehû, gloss:vichet yöneldiğin her yerdir, source:"و ج ه,B002"}. Yirmi üçüncü ayette ise yüz çevrilir ve sırt gösterilir. Fiil "-den" ile kullanıldığında yakınlığı terk edip yüz çevirmeyi anlatır: {ar:إذا عدي بعن اقتضى معنى الإعراض وترك قربه, tr:izâ uddiye bi-an iktedâ ma'na'l-i'râdi ve terke kurbih, gloss:-den ile kullanılınca yüz çevirmeyi ve yakınlığını bırakmayı gerektirir, source:"و ل ي,B007"}. Aynı fiilin bir yüzü yönelmektir: {ar:التولية تكون إقبالا, tr:et-tevliyetü tekûnu ikbâlen, gloss:tevliye yönelmek de olur, source:"و ل ي,B006"}. Kur'an yüz çevirmeyi azaba bağlar. Musa ve Harun'a Firavun'a şunu söylemeleri emredilir: {ar:إِنَّا قَدْ أُوحِىَ إِلَيْنَآ أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ, tr:innâ kad ûhiye ileynâ enne'l-azâbe alâ men kezzebe ve tevellâ, gloss:yalanlayan ve yüz çeviren için azap olduğu bize vahyedildi, source:20:48}.

Yirmi beşinci ayet, sırt dönenin bile nereye vardığını söyler. Dönüş, insanın yerleştiği yere geri gelmesidir: {ar:آب الرجل يؤوب إيابا إذا رجع إلى مستقره والمآب المرجع, tr:âbe'r-raculu yeûbu iyâben izâ raca'a ilâ mustakarrih ve'l-meâbu'l-merci', gloss:adam yerleştiği yere döndüğünde âbe denir; meâb dönülen yerdir, source:"ء و ب,B001"}; {ar:آب الغائب يؤوب أوبا أي رجع والمآب المرجع, tr:âbe'l-ğâibu yeûbu evben ey raca' ve'l-meâbu'l-merci', gloss:gaip olan döndü; meâb dönülen yerdir, source:"ء و ب,B001"}. Yüz çeviren adım adım yine "Bize" yürür. Yüz çevirmek gidilen yeri değiştirmez. Kökün bir kolu aynı dönüşün gönüllü yapılabileceğini gösterir: {ar:الأواب كالتواب وهو الراجع إلى الله تعالى, tr:el-evvâbu ke't-tevvâbi ve huve'r-râciu ilallâhi teâlâ, gloss:evvâb tövbekâr gibidir; Allah'a dönendir, source:"ء و ب,B002"}. Kur'an'da "en büyük azap" sözünün geçtiği öteki ayet de dönüşe bakar: {ar:لَعَلَّهُمْ يَرْجِعُونَ, tr:leallehum yerciûn, gloss:belki dönerler, source:32:21}. Yakın azap, dönüşün henüz insanın elinde olduğu bir zamana denk gelir.

Kur'an dönüşü başka yerlerde de anar. İnsanın kendini yeterli görüp azgınlaştığı söylendikten {source:96:7} sonra şöyle denir: {ar:إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ, tr:inne ilâ rabbike'r-ruc'â, gloss:dönüş şüphesiz Rabbinedir, source:96:8}. Başka bir ayette de {ar:وَإِلَيْنَا ٱلْمَصِيرُ, tr:ve ileyne'l-masîr, gloss:varış Bizedir, source:50:43} denir. Allah, Peygamber'e inkârcılar için üzülmemesini söylerken surenin son ayetlerinin sırasını izler: {ar:وَمَن كَفَرَ فَلَا يَحْزُنكَ كُفْرُهُۥٓ ۚ إِلَيْنَا مَرْجِعُهُمْ فَنُنَبِّئُهُم بِمَا عَمِلُوٓا۟, tr:ve men kefera fe-lâ yahzunke küfruhû ileynâ merciuhum fe-nunebbiuhum bimâ amilû, gloss:kim inkâr ederse inkârı seni üzmesin; dönüşleri Bizedir, yaptıklarını onlara haber veririz, source:31:23}; {ar:نُمَتِّعُهُمْ قَلِيلًۭا ثُمَّ نَضْطَرُّهُمْ إِلَىٰ عَذَابٍ غَلِيظٍۢ, tr:numettiuhum kalîlen summe nadtarruhum ilâ azâbin ğalîz, gloss:onları biraz yararlandırırız, sonra ağır bir azaba sürükleriz, source:31:24}. Burada inkâr, Bize dönüş, yapılan işin haberi ve azap sırayla gelir. Dönülen yer iki türlüdür: {ar:لِّلطَّٰغِينَ مَـَٔابًۭا, tr:li't-tâğîne meâbâ, gloss:azgınlar için bir dönüş yeri, source:78:22} ve {ar:فَمَن شَآءَ ٱتَّخَذَ إِلَىٰ رَبِّهِۦ مَـَٔابًا, tr:fe-men şâe'ttehaze ilâ rabbihî meâbâ, gloss:dileyen Rabbine bir dönüş yolu tutar, source:78:39}. Gönüllü dönüş, dokuzuncu ayetin hoşnutluğuyla yapılır: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:ırci'î ilâ rabbiki râdiyeten mardiyye, gloss:Rabbine hoşnut ve hoşnut edilmiş olarak dön, source:89:28}.

Kaynaklar: 88:1 أَتَىٰكَ ء ت ي B001; 88:1 أَتَىٰكَ ء ت ي B011; 88:1 ٱلْغَٰشِيَةِ غ ش و B003; 88:2 وُجُوهٌ و ج ه B002; 88:23 تَوَلَّىٰ و ل ي B006; 88:23 تَوَلَّىٰ و ل ي B007; 88:25 إِيَابَهُمْ ء و ب B001; 88:25 إِيَابَهُمْ ء و ب B002; 88:26 حِسَابَهُم ح س ب B001

## Buluşmalar

Surenin iki sorusu vardır ve imgeler bu iki soru arasında hareket eder. Birincisi kulağa yöneliktir: {ar:هَلْ أَتَىٰكَ حَدِيثُ ٱلْغَٰشِيَةِ, tr:hel etâke hadîsü'l-ğâşiye, gloss:Gâşiye'nin haberi sana geldi mi, source:88:1}. İkincisi göze yöneliktir: {ar:أَفَلَا يَنظُرُونَ إِلَى ٱلْإِبِلِ كَيْفَ خُلِقَتْ, tr:e-fe-lâ yenzurûne ile'l-ibili keyfe hulikat, gloss:deveye bakmazlar mı nasıl yaratılmış, source:88:17}. Aralarında yüzler vardır. Örtü bu yüzlerin üstüne iner, gözlerini yere indirir ve seslerini kısar. Kur'an'da örtü, yüz ve ateşin tek bir sahnede birleştiği yer şudur: {ar:وَتَغْشَىٰ وُجُوهَهُمُ ٱلنَّارُ, tr:ve tağşâ vucûhehumu'n-nâr, gloss:yüzlerini ateş örter, source:14:50}. Bu sahnede ilk ayetteki örtü, ikinci ayetteki yüz ve dördüncü ayetteki ateş birleşir. Ateş, kızgın bir fırın ve son kıvamına varmış bir su olarak anlatılır. Kavurucu suyun yüzü pişirdiği sahne de kurumuş yüz ile ateşi birleştirir: {ar:يَشْوِى ٱلْوُجُوهَ, tr:yeşvi'l-vucûh, gloss:yüzleri kavurur, source:18:29}. Kurumuş toprağı diriltmesi gereken su gelir, ama kaynar olarak gelir. Bu, yağmurun diriltmesinin tersidir.

Toprak resmi ile yaratma resmi, dünyaya bakışta buluşur. Yirminci ayetteki yer, ikinci ayetteki çökük yüzün de sekizinci ayetteki yumuşak yüzün de toprağıdır. Kuru toprağın suyla dirilişi, ölülerin dirilişinin kanıtıdır: {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰٓ, tr:innellezî ahyâhâ le-muhyi'l-mevtâ, gloss:onu dirilten ölüleri de diriltendir, source:41:39}. Böylece on yedinci ve yirminci ayetler arasındaki bakış, yalnızca dünyanın güzelliğine yöneltilmez. Bakış, ilk yarıda anlatılan günün mümkün olduğunu gösterir. Göğü kaldıran ve yeri düzleyen, sedirleri kaldırıp halıları sermeye de, yüzleri alçaltıp yükseltmeye de kadirdir. Bahçenin odası ile dünyanın çadırı aynı fiillerle kurulur. Dünyaya bakan göz, bahçenin odasını da önceden görmüş olur.

Deve ile oda da Kur'an'da tek bir ayette birleşir: develerin derilerinden evler, kıllarından eşya yapılır {source:16:80}. Bakılacak ilk nesne olan deve, bahçede sayılan döşemenin dünyadaki malzemesidir. Deve ile içecek de birleşir. Hayvanın karnından çıkan süt {ar:سَآئِغًۭا لِّلشَّٰرِبِينَ, tr:sâiğan li'ş-şâribîn, gloss:içenlerin boğazından kolayca geçen, source:16:66} diye anılırken, cehennemdeki içecek {ar:وَلَا يَكَادُ يُسِيغُهُۥ, tr:ve lâ yekâdu yusîğuh, gloss:yutmaya bir türlü yanaşamaz, source:14:17} diye anılır. Yemek ile bakış da birleşir. Darî'in adı doyurmaz, insan ise yemeğine bakmaya çağrılır: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:felyenzuri'l-insânu ilâ taâmih, gloss:insan yiyeceğine bir baksın, source:80:24}. Bakış, yemek ve pişme anı bir başka ayette yine birlikte geçer {source:33:53}. Ateşin mutfak dili ile gözün dili orada aynı cümlededir.

Emek ile sayım, işitme ile kayıt birleşir. On birinci ayetteki boş söz bahçede işitilmez. Aynı kelime hesaptan düşülen şeyi de adlandırır. Bu yüzden on birinci ayet ile yirmi altıncı ayet arasında bir bağ kurulur: değersiz olan ne kulağa girer ne de hesapta kalır. Hesabı tutan ve satırları dizen Peygamber değildir. Musaytır kelimesi ile kayıt kelimesi aynı köktendir {source:54:53}, ve sayım "Bize" aittir. Üçüncü ayetteki yüzün emeği yetmeyen bir şeyle karşılanmıştır. Hesap kökü ise "yeterli" anlamını taşır: {ar:حسبك هذا أي كفاك, tr:hasbüke hâzâ ey kefâk, gloss:bu sana yeter, source:"ح س ب,B003"}. Yedinci ayetteki "yetmez" ile son ayetteki hesap aynı ölçünün iki ucudur.

Eğilme ile dönüş de birleşir. İkinci ayetteki eğiklik ve dördüncü ayetteki fiil, ibadetin duruşlarını yan anlam olarak taşır. Yirmi üçüncü ayetteki yüz çevirme, namaz kılmamakla bir arada anılır {source:75:32}. Dünyada secdeye çağrılıp gelmeyenler o gün gözleri eğik halde gelir {source:68:43}. Gönüllü eğilmenin vakti geçince eğilme zorla gelir. Dönüş de iki yoldan yapılır: gönüllü dönen "evvâb" olur, sırt dönen de yine "Bize" döner.

Son olarak surenin başı ile sonu, kendi kelimeleriyle kapanan bir halka oluşturur. İlk ayetteki "geldi mi" ile son ayetten bir önceki ayetteki "dönüş", deve sürücülerinin dilinde ayakların ileri atılıp geri çekilmesidir. Böylece surede bir günlük yürüyüşün başlangıcı ve akşam konağı duyulur. İlk ayetteki örtü ile yirmi dördüncü ayetteki azap tek bir Kur'an ayetinde yan yana durur {source:12:107}. Arada gelen "sen yalnızca hatırlatansın" sözü, halkanın ortasında Peygamber'in yerini belirler. Haber ona gelmiştir ve o da bu haberi duyurur. Örtüyü indirmek, göğü kaldırmak, dönüşü karşılamak ve hesabı tutmak ise "Biz" diye konuşana aittir.

