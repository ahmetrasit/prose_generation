Focus: 99:4. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/99_4/D.r13/context.md =====
# 99:4 — focus

يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا

Anchor translation (canonical reading, reference only):

O gün yer haberlerini anlatır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | يَوْمَئِذٍ | يَوْمَئِذ |  | T |
| 2 | تُحَدِّثُ | تُحَدِّثُ | ح د ث | V |
| 3 | أَخْبَارَهَا | أَخْبَار | خ ب ر | N;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 99 — full text (context; no pericope)

- 99:1 إِذَا زُلْزِلَتِ ٱلْأَرْضُ زِلْزَالَهَا
- 99:2 وَأَخْرَجَتِ ٱلْأَرْضُ أَثْقَالَهَا
- 99:3 وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا
- 99:4 ◀ focus يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا
- 99:5 بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
- 99:6 يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
- 99:7 فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
- 99:8 وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ


===== _commentary/v16/work/99_4/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ح د ث (root_000299) — identity root of تُحَدِّثُ (w2)

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

## خ ب ر (root_000387) — identity root of أَخْبَارَهَا (w3)

- **B001** bilgi edinme, bildirme ve deneyerek iç yüzü tanıma — bir olay veya durum hakkında edinilen ve aktarılan bilgi · bilgi vermek; bildirmek · bir konuyu sorup bilgi edinmek · sınama ve deneyimle kazanılan bilgi; iç yüzü tanıma · sınayıp deneyerek bilgi sahibi olmuş kişi · bilgili; bir işin iç yüzüne hakim · dış görünüşün karşısındaki iç yüz ve gerçek nitelik
  الخبر العلم بالشيء (maqayis)؛ الخبر النبأ (ayn)؛ الخبر معروف أخبرت بكذا (jamhara)؛ الاستخبار السؤال عن الخبر (sihah)؛ الخبرة الاختبار (ayn)؛ الخبرة المعرفة ببواطن الأمر (mufradat)؛ الخبير العالم (maqayis;ayn;sihah;mufradat)؛ المخبر خلاف المنظر (sihah)
- **B002** gevşek, alçak ve su tutan arazi veya su birikintisi — gevşek, yumuşak veya alçak olup su toplayan arazi · sıcak, ağaçlı ve suyu bol yer · akış yatağında oluşan geçilebilir su birikintisi
  الخبراء الأرض اللينة (maqayis)؛ الخبار أرض رخوة (ayn;sihah)؛ الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء (jamhara)؛ الخبار والخبراء الأرض اللينة (mufradat)؛ مكان خَبِر دفيء كثير الشجر والماء (maqayis)؛ الخبر من مناقع الماء (ayn)
- **B003** üründen pay karşılığı ortakçılık ve bunu yapan çiftçi — toprağı işleyen çiftçi · ürünün belirli bir payı karşılığında yapılan tarımsal ortakçılık
  الخبير الأكار (maqayis;ayn;sihah;mufradat)؛ المخابرة المزارعة بالنصف أو الثلث (maqayis)؛ الخبر والمخابرة أن تزرع على النصف أو الثلث (ayn)؛ المخابرة مزارعة الخبار بشيء معلوم (mufradat)؛ المزارعة ببعض ما يخرج من الأرض (sihah)
- **B004** büyük su tulumu ve bolluğuyla ona benzetilen dişi deve — büyük ve geniş su tulumu · bolluğu ve verimiyle büyük su tulumuna benzetilen dişi deve
  الخبر المزادة العظيمة (maqayis;sihah;mufradat)؛ المزادة العظيمة والجمع خبور (jamhara)؛ الناقة الغزيرة خَبْر (maqayis;jamhara)؛ تشبه بها الناقة في غزرها فتسمى خبراء (sihah)؛ شبهت بها الناقة فسميت خَبْرا (mufradat)
- **B005** yumuşak bitki, yün veya ince kıl ve deve ağzı köpüğü — kesilip yenebilen yumuşak bitki · yün veya ince hayvan kılı · devenin ağzında oluşan veya ağzından çıkan köpük
  الخبير النبات اللين (maqayis)؛ الخبير النبات (sihah)؛ الخبير الوبر (maqayis;sihah)؛ الخبير زبد أفواه الإبل (sihah)؛ الخبير الزبد الذي يلقيه البعير من فيه (jamhara)
- **B006** ortak alınıp kesilen koyun veya bölüşülen et-balık payı — ortaklaşa alınıp kesilen ve eti bölüşülen koyun · et veya balıktan alınan pay
  الخُبْرة الشاة يشتريها القوم يذبحونها ويقتسمون لحمها (maqayis)؛ تخبر القوم بينهم خبرة إذا اشتروا شاة فذبحوها واقتسموا لحمها (jamhara)؛ الخبرة النصيب تأخذه من سمك أو لحم (sihah)

===== _commentary/v16/out/s099/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 99:4, and ## Buluşmalar) =====
## Yerden bedene geçen sarsıntı

Sarsıntı yerde kalmaz. Yer kelimesi bir bedenin titremesini de adlandırır {ar:الأرض الرعدة, tr:el-arzu er-ri‘de, gloss:arz, titremedir, source:"ء ر ض,B008"}; birinde {ar:بفلان أرض, tr:bi-fulânin arz, gloss:falancada titreme var, source:"ء ر ض,B008"} denir. Aynı kelimeyle başını ve gövdesini istemeden sarsan kişi de anılır {ar:الذي يحرك رأسه وجسده على غير عمد, tr:ellezî yuharriku re’sehû ve ceseduhû alâ gayri amd, gloss:başını ve bedenini istemeden oynatan, source:"ء ر ض,B012"}. Zelzele kökü de zamanın sıkıntılarına uzanır {ar:زلازل الدهر: شدائده, tr:zelâzilud-dehr: şedâiduh, gloss:zamanın zelzeleleri onun sıkıntılarıdır, source:"ز ل ز ل,B002"}; dördüncü ayetin fiilinin kökü de başa inen olayı, felaketi adlandırır {ar:الحادثة النازلة العارضة, tr:el-hâdisetu en-nâziletu el-ârıda, gloss:hadise, inip gelen musibettir, source:"ح د ث,B005"}.

Bu imgede birinci ayetteki sarsıntı, yerin üstünde duranın bedenine geçen tek bir titremedir. Üçüncü ayet etkisini gösterir: {ar:وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا, tr:ve kâlel-insânu mâ lehâ, gloss:ve insan "ona ne oluyor" der, source:99:3}. Söz, konuşmanın dile gelmesidir {ar:القول من النطق, tr:el-kavlu minen-nutk, gloss:söz konuşmadandır, source:"ق و ل,B001"}; burada sarsılmış insanın ağzından çıkan kısa bir soru. Soru iki kelimedir ve cevabı yoktur; yer ayağının altında oynarken insan yalnızca "ona ne oluyor" diyebilir.

Kur’an sarsıntıyı insanlar için de kullanır. Saatin sarsıntısının ardından {ar:وَتَرَى ٱلنَّاسَ سُكَٰرَىٰ وَمَا هُم بِسُكَٰرَىٰ, tr:ve teran-nâse sukârâ ve mâ hum bisukârâ, gloss:insanları sarhoş görürsün, oysa sarhoş değillerdir, source:22:2}: yerin sarsıntısı insanların sendelemesinde görünür. Önceki toplulukları müminlere anlatan ayette {ar:وَزُلْزِلُوا۟ حَتَّىٰ يَقُولَ ٱلرَّسُولُ, tr:ve zulzilû hattâ yekûler-resûl, gloss:öyle sarsıldılar ki elçi şöyle dedi, source:2:214}; burada da sarsıntı bir sözle, bir çığlıkla biter. Kuşatma anlatılırken surenin aynı ikilisi insanlara uygulanır: {ar:وَزُلْزِلُوا۟ زِلْزَالًا شَدِيدًا, tr:ve zulzilû zilzâlen şedîdâ, gloss:ve şiddetli bir sarsıntıyla sarsıldılar, source:33:11}. Saatte insanın sorusu da aynı biçimdedir: {ar:يَقُولُ ٱلْإِنسَٰنُ يَوْمَئِذٍ أَيْنَ ٱلْمَفَرُّ, tr:yekûlul-insânu yevmeizin eynel-mefer, gloss:insan o gün "kaçacak yer nerede" der, source:75:10}; kabirlerinden kalkanlar da {ar:يَٰوَيْلَنَا مَنۢ بَعَثَنَا مِن مَّرْقَدِنَا, tr:yâ veylenâ men beasenâ min merkadinâ, gloss:vay bize, bizi yattığımız yerden kim kaldırdı, source:36:52} diye sorar.

Kaynaklar: 99:1 ٱلْأَرْضُ ء ر ض B008; 99:1 ٱلْأَرْضُ ء ر ض B012; 99:1 زِلْزَالَهَا ز ل ز ل B001; 99:1 زِلْزَالَهَا ز ل ز ل B002; 99:4 تُحَدِّثُ ح د ث B005; 99:3 وَقَالَ ق و ل B001

## Konuşturulan yer: soru, gizli bildirim, haber

Üçüncü, dördüncü ve beşinci ayet üç adımlı bir konuşma kurar. İnsan sorar: {ar:مَا لَهَا, tr:mâ lehâ, gloss:ona ne oluyor, source:99:3}. Yer cevap verir: {ar:يَوْمَئِذٍ تُحَدِّثُ أَخْبَارَهَا, tr:yevmeizin tuhaddisu ahbârahâ, gloss:o gün haberlerini anlatır, source:99:4}. Cevabın kaynağı da söylenir: {ar:بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا, tr:bi-enne rabbeke evhâ lehâ, gloss:çünkü Rabbin ona vahyetmiştir, source:99:5}.

Her adımın kelimesi kendi işleyişini taşır. Haber sormak bir kelimeyle söylenir {ar:الاستخبار السؤال عن الخبر, tr:el-istihbâr es-suâlu anil-haber, gloss:istihbar haberi sormaktır, source:"خ ب ر,B001"}; insanın "ona ne oluyor" sorusu tam da dördüncü ayetin vereceği şeyi ister. Haber ise işin içyüzüdür {ar:المخبر خلاف المنظر, tr:el-mahber hilâful-manzar, gloss:iç, dış görünüşün karşıtıdır, source:"خ ب ر,B001"}. Anlatmak, kulak yoluyla ya da vahiy yoluyla insana ulaşan sözdür {ar:كل كلام يبلغ الإنسان من جهة السمع أو الوحي يقال له حديث, tr:kullu kelâmin yeblugul-insâne min cihetis-sem‘i evil-vahyi yukâlu lehû hadîs, gloss:insana duyma ya da vahiy yoluyla ulaşan her söze hadis denir, source:"ح د ث,B003"}: bu tek tanım üçüncü ayetin insanını, dördüncünün anlatmasını ve beşincinin vahyini birleştirir. Aynı kök, daha önce olmayan bir şeyin olmasını da anlatır {ar:الحدوث كون الشيء بعد أن لم يكن, tr:el-hudûs kevnuş-şey’i ba‘de en lem yekun, gloss:hudus, bir şeyin yokken var olmasıdır, source:"ح د ث,B001"}: hiç konuşmamış yer şimdi konuşur.

Vahiy, bir bilginin gizlice başkasına bırakılmasıdır {ar:إعلام في خفاء, tr:i‘lâmun fî hafâ’, gloss:gizlice bildirmek, source:"و ح ي,B001"}; işaretle {ar:الوحي الإشارة, tr:el-vahyu el-işâra, gloss:vahy, işarettir, source:"و ح ي,B002"}, gök gürültüsünün uzun ve gizli sesi gibi bir sesle {ar:وحاة الرعد وهو صوته الممدود الخفي, tr:vahâtur-ra‘d ve huve savtuhul-memdûdul-hafiyy, gloss:gök gürültüsünün uzayan gizli sesi, source:"و ح ي,B005"}, ya da taşa yazarak {ar:وحى في الحجر إذا كتب فيه, tr:vahâ fil-hacer izâ ketebe fîh, gloss:taşa yazdığında "vahâ" denir, source:"و ح ي,B003"}. Bu son anlam sahneyi somutlaştırır: yer, üzerine yazılmış bir yüzeydir ve kendisine yazılanı okur. Söz kökünün bir kullanımı da dilsiz bir şeyin hâliyle "söylemesini" kaydeder {ar:امتلأ الحوض وقال قطني, tr:imtele’el-havdu ve kâle katnî, gloss:havuz doldu ve "yeter" dedi, source:"ق و ل,B014"}; insanın sorusunda geçen fiil, dili olmadan konuşan bir şeyi de adlandırabilir. Gönderen ise {ar:رَبَّكَ, tr:rabbeke, gloss:Rabbin, source:99:5}, sözü dinlenen sahiptir {ar:يكون الرب: السيد المطاع, tr:yekûnu’r-rabb: es-seyyidu’l-mutâ‘, gloss:rab, sözü dinlenen efendidir, source:"ر ب ب,B001"}.

Sade bir anlatım "yer olanları gösterir" der; ayetler ise sessiz bir maddenin gizli bir emirle dile geldiği, insanın da dinleyen olduğu bir konuşma kurar. Kur’an yerin Rabbine kulak verişini başka bir sahnede de gösterir: içindekini atıp boşaldıktan hemen sonra yer {ar:وَأَذِنَتْ لِرَبِّهَا وَحُقَّتْ, tr:ve ezinet li-rabbihâ ve hukkat, gloss:Rabbine kulak verdi ve buna layık kılındı, source:84:5}. Yaratılışta Allah göğe ve yere seslenir, yer de cevap verir: {ar:قَالَتَآ أَتَيْنَا طَآئِعِينَ, tr:kâletâ eteynâ tâiîn, gloss:ikisi "isteyerek geldik" dediler, source:41:11}; ardından {ar:وَأَوْحَىٰ فِى كُلِّ سَمَآءٍ أَمْرَهَا, tr:ve evhâ fî kulli semâin emrehâ, gloss:her göğe işini vahyetti, source:41:12}. Surenin ikilisi bir hayvana yönelik olarak da geçer: {ar:وَأَوْحَىٰ رَبُّكَ إِلَى ٱلنَّحْلِ, tr:ve evhâ rabbuke ilen-nahl, gloss:Rabbin bal arısına vahyetti, source:16:68}. Vahyin bir konuşma türü olduğunu da Kur’an söyler: Allah insanla {ar:إِلَّا وَحْيًا أَوْ مِن وَرَآئِ حِجَابٍ, tr:illâ vahyen ev min verâi hicâb, gloss:ancak vahiyle ya da perde arkasından, source:42:51} konuşur. Allah’ın vahyine ağır söz de denir: Peygambere {ar:إِنَّا سَنُلْقِى عَلَيْكَ قَوْلًا ثَقِيلًا, tr:innâ senulkî aleyke kavlen sakîlâ, gloss:sana ağır bir söz bırakacağız, source:73:5}.

Dilsiz şeylerin konuşturulması ateş ehlinin sahnesinde açıkça kurulur. Kulakları, gözleri ve derileri onların aleyhine şahitlik eder {source:41:20}; onlar derilerine sorar, deriler cevap verir: {ar:قَالُوٓا۟ أَنطَقَنَا ٱللَّهُ ٱلَّذِىٓ أَنطَقَ كُلَّ شَىْءٍ, tr:kâlû entakanallâhullezî entaka kulle şey’, gloss:"her şeyi konuşturan Allah bizi konuşturdu" dediler, source:41:21}. Bu, üçüncü ve dördüncü ayetin soru ve cevap biçimidir. Aynı günde ağızlar mühürlenir ve eller konuşur {source:36:65}, diller, eller ve ayaklar yaptıklarına şahitlik eder {source:24:24}. Yazılı kayıt da konuşur: {ar:هَٰذَا كِتَٰبُنَا يَنطِقُ عَلَيْكُم بِٱلْحَقِّ, tr:hâzâ kitâbunâ yentıku aleykum bil-hakk, gloss:bu kitabımız aleyhinize gerçeği söyler, source:45:29}. Suçlular kitabın önünde surenin sorusunun biçimiyle sorar: {ar:مَالِ هَٰذَا ٱلْكِتَٰبِ لَا يُغَادِرُ صَغِيرَةً وَلَا كَبِيرَةً إِلَّآ أَحْصَىٰهَا, tr:mâli hâzel-kitâbi lâ yugâdiru sagîraten ve lâ kebîraten illâ ahsâhâ, gloss:bu kitaba ne oluyor, küçük büyük bırakmadan hepsini saymış, source:18:49}. Haberlerin insana ulaşması da aynı gündedir: {ar:يُنَبَّؤُا۟ ٱلْإِنسَٰنُ يَوْمَئِذٍۭ بِمَا قَدَّمَ وَأَخَّرَ, tr:yunebbeul-insânu yevmeizin bimâ kaddeme ve ahhar, gloss:o gün insana öne sürdüğü ve geride bıraktığı haber verilir, source:75:13}; altüst edilen kabirlerin sahnesi de haber köküyle kapanır: {ar:إِنَّ رَبَّهُم بِهِمْ يَوْمَئِذٍ لَّخَبِيرٌ, tr:inne rabbehum bihim yevmeizin le-habîr, gloss:Rableri o gün onlardan elbette haberdardır, source:100:11}. Yok edilen kavimler için söylenen {ar:وَجَعَلْنَٰهُمْ أَحَادِيثَ, tr:ve cealnâhum ehâdîs, gloss:onları anlatılan hikâyeler yaptık, source:23:44} sözü de anlatmanın ve haberin aynı şey olduğunu gösterir.

Kaynaklar: 99:3 وَقَالَ ق و ل B001; 99:3 وَقَالَ ق و ل B014; 99:4 أَخْبَارَهَا خ ب ر B001; 99:4 تُحَدِّثُ ح د ث B003; 99:4 تُحَدِّثُ ح د ث B001; 99:5 أَوْحَىٰ و ح ي B001; 99:5 أَوْحَىٰ و ح ي B002; 99:5 أَوْحَىٰ و ح ي B005; 99:5 أَوْحَىٰ و ح ي B003; 99:5 رَبَّكَ ر ب ب B001

## İçerinin çıkarılıp gösterilmesi

Sure boyunca içerdeki şeyler görünüre doğru hareket eder. Yerin ağırlıkları yer altındadır, hazineler göz önünden gömülüdür {source:"ث ق ل,B002"}. Çıkarmak, gizli olanı çekip almak, gömülü suyu yukarı çekmek gibidir {ar:الاستخراج كالاستنباط, tr:el-istihrâc kel-istinbât, gloss:çıkarıp almak, gizli suyu çekip çıkarmak gibidir, source:"خ ر ج,B002"}. Yerin haberleri işlerin içidir; anlatmak ise açığa çıkarmaktır {ar:الحدث الإبداء, tr:el-hadsu el-ibdâ’, gloss:açığa vurmak, source:"ح د ث,B006"}, hatta bir kılıcı cilalayıp donuk tabakasını gidermektir {ar:أحدث الرجل سيفه وحادثه إذا جلاه, tr:ahdeser-raculu seyfehû ve hâdesehû izâ celâh, gloss:kılıcını cilaladığında "ahdese" denir, source:"ح د ث,B007"}. Yer anlattıkça yüzeyi parlar ve altındaki görünür.

Altıncı ayette yön insana döner: {ar:لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:li-yurav a‘mâlehum, gloss:amelleri kendilerine gösterilsin diye, source:99:6}. Fiil edilgendir: insanlar görmeye getirilir. Görme kökünün ettirgen kullanımı birine bir şeyi gösterip gördürmektir, birine ayna tutup bakmasını sağlamaktır {ar:رأيت الرجل ترئية إذا أمسكت له المرآة لينظر فيها, tr:ra’eytur-racule ter’iyeten izâ emsektu lehul-mir’âte li-yenzura fîhâ, gloss:adama bakması için ayna tuttuğumda "ra’eytuhu" derim, source:"ر ء ي,B012"}. Amel sahibinin önüne ayna gibi tutulur. Aynı kök, insanların görmesi için iş yapmayı da adlandırır {ar:أن يفعل شيئا ليراه الناس, tr:en yef‘ale şey’en li-yerâhun-nâs, gloss:bir şeyi insanlar görsün diye yapmak, source:"ر ء ي,B005"}; Kur’an münafıkları {ar:يُرَآءُونَ ٱلنَّاسَ, tr:yurâûnen-nâs, gloss:insanlara gösteriş yaparlar, source:4:142} diye anlatır. Surede yön tersine döner: herkes başkasına değil, kendi amelini görmeye getirilir. Yedinci ve sekizinci ayetin {ar:يَرَهُۥ, tr:yerahû, gloss:onu görür, source:99:8} fiili gözle ya da iç görüyle görmektir {ar:نظر وإبصار بعين أو بصيرة, tr:nazarun ve ibsârun bi-aynin ev basîra, gloss:gözle ya da basiretle bakış ve görüş, source:"ر ء ي,B001"}.

Sekizinci ayetin kötülük kelimesi de bu harekete katılır: aynı kök bir şeyi ortaya çıkarıp sergilemek anlamını taşır {ar:أشررت الشيء إذا أبرزته وأظهرته, tr:eşrartuş-şey’e izâ ebreztuhû ve azhartuh, gloss:bir şeyi ortaya çıkarıp gösterdiğimde "eşrartu" derim, source:"ش ر ر,B008"}, bir şeyi kurusun diye güneşe yaymak anlamını da {ar:الشر بسطك الشيء في الشمس, tr:eş-şerru bastukeş-şey’e fiş-şems, gloss:şerr, bir şeyi güneşe yaymandır, source:"ش ر ر,B002"}. Zerrenin kökü de güneşin doğuşunda yayılan ince ışığı adlandırır {ar:ذرت الشمس ذرورا إذا طلعت وهو ضوء لطيف منتشر, tr:zerratiş-şemsu zurûran izâ tala‘at ve huve dav’un latîfun munteşir, gloss:güneş doğup ince ışığını yaydı, source:"ذ ر ر,B004"}. Bu anlamlar kelimelerin ayetteki anlamını, iyilik ve kötülüğü, değiştirmez; yanlarında, en küçük kötülüğün bile güneşe serilmiş gibi açıkta olduğunu duyururlar. Gören de bu sahnededir: insan görünür olduğu için böyle adlandırılmıştır {ar:الإنس خلاف الجن وسموا لظهورهم, tr:el-insu hilâful-cinni ve summû li-zuhûrihim, gloss:ins cinnin karşıtıdır, görünür oldukları için böyle adlandırıldılar, source:"ء ن س,B001"}; göz bebeğinde görünen küçük suret {ar:إنسان العين المثال الذي يرى في السواد, tr:insânul-ayn el-misâlullezî yurâ fis-sevâd, gloss:göz bebeği, karalıkta görünen suret, source:"ء ن س,B005"} de aynı adı taşır; görmek ve duymak da bu köktendir {ar:آنست الشيء إذا رأيته وآنسته إذا سمعته, tr:ânestuş-şey’e izâ ra’eytuhû ve ânestuhû izâ semi‘tuh, gloss:bir şeyi gördüğümde ve duyduğumda "ânestu" derim, source:"ء ن س,B002"}. Üçüncü ayetin insanı sarsıntıyı görür, haberi duyar ve sonunda amelini görür.

Kur’an bu açığa çıkarışı birçok yerde sahneler. Kabirlerdekiyle göğüslerdeki birlikte çıkarılır: {ar:وَحُصِّلَ مَا فِى ٱلصُّدُورِ, tr:ve hussıle mâ fis-sudûr, gloss:göğüslerde olan ortaya dökülür, source:100:10}. Altıncı ayetin fiili göğüs kelimesiyle aynı köktendir {source:"ص د ر,B001"}; bu bir kök ortaklığıdır, aynı anlam değildir, ama bu ayetin yanında duyulur. Gizliler o gün sınanır {source:86:9}; {ar:يَوْمَئِذٍ تُعْرَضُونَ لَا تَخْفَىٰ مِنكُمْ خَافِيَةٌ, tr:yevmeizin tu‘radûne lâ tahfâ minkum hâfiyeh, gloss:o gün arz olunursunuz, sizden hiçbir gizli kalmaz, source:69:18}. Çıkarma fiili kayıt için de kullanılır: {ar:وَنُخْرِجُ لَهُۥ يَوْمَ ٱلْقِيَٰمَةِ كِتَٰبًا يَلْقَىٰهُ مَنشُورًا, tr:ve nuhricu lehû yevmel-kıyâmeti kitâben yelkâhu menşûrâ, gloss:kıyamet günü onun için açılmış bulacağı bir kitap çıkarırız, source:17:13}; hemen ardından {ar:ٱقْرَأْ كِتَٰبَكَ, tr:ikra’ kitâbek, gloss:kitabını oku, source:17:14} denir. Sayfalar açılır {source:81:10}. Allah’ın uyarısında her nefis yaptığı iyiliği hazır bulur {ar:يَوْمَ تَجِدُ كُلُّ نَفْسٍ مَّا عَمِلَتْ مِنْ خَيْرٍ مُّحْضَرًا, tr:yevme tecidu kullu nefsin mâ amilet min hayrin muhdarâ, gloss:her nefsin yaptığı iyiliği hazır bulduğu gün, source:3:30}. Musa ve İbrahim’in sayfalarındaki söz surenin edilgen fiilini kullanır: {ar:وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ, tr:ve enne sa‘yehû sevfe yurâ, gloss:ve onun çabası görülecektir, source:53:40}. İnsana dirilişte {ar:فَكَشَفْنَا عَنكَ غِطَآءَكَ فَبَصَرُكَ ٱلْيَوْمَ حَدِيدٌ, tr:fekeşefnâ anke gitâeke fe-basarukel-yevme hadîd, gloss:örtünü üzerinden kaldırdık, bugün gözün keskindir, source:50:22} denir; herkes ellerinin öne sürdüğüne bakar {source:78:40}. Ve o gün yer, Rabbinin nuruyla aydınlanır, kitap konur {ar:وَأَشْرَقَتِ ٱلْأَرْضُ بِنُورِ رَبِّهَا وَوُضِعَ ٱلْكِتَٰبُ, tr:ve eşrakatil-arzu bi-nûri rabbihâ ve vudi‘al-kitâb, gloss:yer Rabbinin nuruyla parladı ve kitap kondu, source:39:69}.

Kaynaklar: 99:2 أَثْقَالَهَا ث ق ل B002; 99:2 وَأَخْرَجَتِ خ ر ج B002; 99:4 أَخْبَارَهَا خ ب ر B001; 99:4 تُحَدِّثُ ح د ث B006; 99:4 تُحَدِّثُ ح د ث B007; 99:6 لِّيُرَوْا۟ ر ء ي B012; 99:6 لِّيُرَوْا۟ ر ء ي B005; 99:7 يَرَهُۥ ر ء ي B001; 99:8 شَرًّا ش ر ر B008; 99:8 شَرًّا ش ر ر B002; 99:7 ذَرَّةٍ ذ ر ر B004; 99:3 ٱلْإِنسَٰنُ ء ن س B001; 99:3 ٱلْإِنسَٰنُ ء ن س B005; 99:3 ٱلْإِنسَٰنُ ء ن س B002; 99:6 يَصْدُرُ ص د ر B001

## Toprağın, bulutun ve suyun çıkardığı bitki

Kur’an dirilişi sürekli olarak yerden bitki çıkmasına benzetir: yağmur yağar, toprak kıpırdar ve kabarır, bitki çıkarılır, "işte siz de böyle çıkarılacaksınız". Surenin kelimeleri bu dizinin parçalarını kendi anlamlarında taşır. Yer, bitkinin kök saldığı yumuşak, verimli topraktır {ar:أرض أريضة لينة طيبة, tr:arzun erîdatun leyyinetun tayyibe, gloss:yumuşak, iyi, verimli toprak, source:"ء ر ض,B002"}. Çıkma kökü yerin bitkisini yer yer çıkarmasını {ar:أرض مخرجة نبتها في مكان دون مكان, tr:arzun muharracetun nebtuhâ fî mekânin dûne mekân, gloss:bitkisi bir yerde çıkıp bir yerde çıkmayan toprak, source:"خ ر ج,B007"}, ürünü {ar:الخراج الغلة, tr:el-harâcu el-galle, gloss:harac üründür, source:"خ ر ج,B003"} ve bulutun ilk belirişini {source:"خ ر ج,B005"} adlandırır. Haber kökü yağmur suyunu toplayan alçak, yumuşak toprağı {ar:الخبراء الأرض السهلة المنخفضة يجتمع فيها ماء السماء, tr:el-habrâ’ el-arzus-sehletul-munhafidatu yecteme‘u fîhâ mâus-semâ’, gloss:gök suyunun toplandığı alçak, düz toprak, source:"خ ب ر,B002"}, çiftçiyi ve yerden çıkanın bir kısmı karşılığında ortakçılığı {ar:المزارعة ببعض ما يخرج من الأرض, tr:el-muzâraa bi-ba‘dı mâ yahrucu minel-arz, gloss:yerden çıkanın bir kısmı karşılığında ortakçılık, source:"خ ب ر,B003"} ve körpe bitkiyi {source:"خ ب ر,B005"} adlandırır. Rab kökü üst üste binmiş bulutu, bitkiyi büyüttüğü için verilen adla anar {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb: es-sehâb, summiye bi-zâlike li-ennehû yerubbun-nebât, gloss:rabâb buluttur, bitkiyi büyüttüğü için böyle adlandırılmıştır, source:"ر ب ب,B008"}; terbiye de bir şeyi hâlden hâle tamamlanmaya kadar yetiştirmektir {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâuş-şey’i hâlen fe-hâlen ilâ haddit-temâm, gloss:terbiye, bir şeyi hâlden hâle tamamına kadar geliştirmektir, source:"ر ب ب,B002"}; çok ve toplanmış su da bu köktendir {source:"ر ب ب,B013"}. Zerre kökü de toprağı yarıp çıkan filizi adlandırır {ar:ذر البقل إذا طلع من الأرض, tr:zerral-baklu izâ tala‘a minel-arz, gloss:sebze yerden baş verdiğinde "zerra" denir, source:"ذ ر ر,B004"}.

Bu imgede birinci ve ikinci ayetin yeri bir tarladır; çıkarması onun ürünüdür. Beşinci ayetteki Rab, kelimenin anlamında efendi ve sahiptir; yanında, bitkiyi aşama aşama büyüten bulutun adı da duyulur. Diriliş korkunç bir yıkım olduğu kadar tanıdık bir yetişmedir.

Kur’an üç imgeyi tek ayette birleştirir: rüzgârlar {ar:حَتَّىٰٓ إِذَآ أَقَلَّتْ سَحَابًا ثِقَالًا سُقْنَٰهُ لِبَلَدٍ مَّيِّتٍ فَأَنزَلْنَا بِهِ ٱلْمَآءَ فَأَخْرَجْنَا بِهِۦ مِن كُلِّ ٱلثَّمَرَٰتِ كَذَٰلِكَ نُخْرِجُ ٱلْمَوْتَىٰ, tr:hattâ izâ ekallet sehâben sikâlen suknâhu li-beledin meyyitin fe-enzelnâ bihil-mâe fe-ahracnâ bihî min kullis-semerât, kezâlike nuhricul-mevtâ, gloss:ağır bulutları yüklendiklerinde onu ölü bir beldeye süreriz, oraya suyu indirir, onunla her türlü meyveyi çıkarırız; ölüleri de böyle çıkarırız, source:7:57}. Ağır bulut, çıkarılan meyve ve çıkarılan ölüler burada yan yanadır. Dirilişten şüphe edenlere gösterilen yer önce kupkurudur, su inince {ar:ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ, tr:ihtezzet ve rabet ve enbetet, gloss:titredi, kabardı ve bitirdi, source:22:5}; aynı söz Allah’ın ayetleri arasında da geçer ve {ar:إِنَّ ٱلَّذِىٓ أَحْيَاهَا لَمُحْىِ ٱلْمَوْتَىٰ, tr:innellezî ahyâhâ le-muhyil-mevtâ, gloss:onu dirilten elbette ölüleri de diriltir, source:41:39} sözüyle tamamlanır. Bulut sürülür ve yer diriltilir: {ar:كَذَٰلِكَ ٱلنُّشُورُ, tr:kezâliken-nuşûr, gloss:diriliş de böyledir, source:35:9}; dirilişi inkâr edenlere verilen cevapta {ar:كَذَٰلِكَ ٱلْخُرُوجُ, tr:kezâlikel-hurûc, gloss:çıkış da böyledir, source:50:11}; ve {ar:كَذَٰلِكَ تُخْرَجُونَ, tr:kezâlike tuhracûn, gloss:siz de böyle çıkarılırsınız, source:43:11}, {source:30:19}. Çıkarma fiili bitki için tekrar tekrar kullanılır {source:6:99}; yer de kendi suyunu ve otlağını verir {ar:أَخْرَجَ مِنْهَا مَآءَهَا وَمَرْعَىٰهَا, tr:ahrace minhâ mâehâ ve mer‘âhâ, gloss:ondan suyunu ve otlağını çıkardı, source:79:31}; Rabbin övüldüğü surede de {ar:وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ, tr:vellezî ahracel-mer‘â, gloss:otlağı çıkaran, source:87:4} denir. Nuh da insanları yerin bitkisi olarak anar: {ar:وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًا, tr:vallâhu enbetekum minel-ardı nebâtâ, gloss:Allah sizi yerden bir bitki gibi bitirdi, source:71:17}.

Kaynaklar: 99:1 ٱلْأَرْضُ ء ر ض B002; 99:2 وَأَخْرَجَتِ خ ر ج B007; 99:2 وَأَخْرَجَتِ خ ر ج B003; 99:2 وَأَخْرَجَتِ خ ر ج B005; 99:4 أَخْبَارَهَا خ ب ر B002; 99:4 أَخْبَارَهَا خ ب ر B003; 99:4 أَخْبَارَهَا خ ب ر B005; 99:5 رَبَّكَ ر ب ب B008; 99:5 رَبَّكَ ر ب ب B002; 99:5 رَبَّكَ ر ب ب B013; 99:7 ذَرَّةٍ ذ ر ر B004

## Buluşmalar

Surenin hareketi bir yönden ötekine geçer: içeriden dışarıya, ağırdan hafife, büyükten küçüğe, sessizden konuşana, gizliden görünene. İmgeler bu hareketin farklı yüzlerini taşır ve birkaç sahnede üst üste biner.

İlk buluşma yerin boşalmasıyla doğumdur. İkinci ayetin iki kelimesi, {ar:وَأَخْرَجَتِ, tr:ve ahracet, gloss:ve çıkardı, source:99:2} ile {ar:أَثْقَالَهَا, tr:eskâlehâ, gloss:ağırlıkları, source:99:2}, hem gömülü yükü atan yeri hem doğuran bedeni anlatır. Kur’an bu iki sahneyi aynı ayetlerde tutar: Saatin sarsıntısı {source:22:1} ve her gebenin yükünü bırakması {source:22:2}; rahimden çocuğu çıkarmak ve suyla titreyip kabaran toprak {source:22:5}. Aynı ayet bitki imgesini de içerir; böylece boşalan yer, doğuran beden ve filiz veren tarla tek bir dirilişin üç görünüşü olur. Ağır bulutlarla meyveyi ve ölüleri çıkaran ayet {source:7:57} ağırlık imgesini de bu sahneye bağlar.

İkinci buluşma boşalan yerle konuşan yerdir. İnşikak suresinde sıra surenin sırasıyla aynıdır: yer içindekini atar ve boşalır {source:84:4}, sonra Rabbine kulak verir {source:84:5}. İkinci ayette yer yükünü çıkarır, beşinci ayette Rabbinin vahyini alır. Arada üçüncü ayetin sarsılmış insanı vardır: sarsıntı bedenine geçmiş, ağzından {ar:مَا لَهَا, tr:mâ lehâ, gloss:ona ne oluyor, source:99:3} sorusu çıkmıştır. Bu soru, sarsıntı imgesini konuşma imgesine bağlar; çünkü yer ona cevap verecektir. Suçluların kitabın önündeki sorusu {source:18:49} aynı biçimdedir ve ardından yaptıklarını hazır bulurlar: soru, haber ve görme bir sahnede toplanır.

Üçüncü buluşma konuşmayla göstermedir. Dördüncü ayette yerin anlattığı haber, işin içyüzüdür; anlatmak açığa vurmak, kılıcı parlatmaktır. Yerin içindekilerini çıkarması ile haberlerini anlatması aynı işlemdir: içeride olanın dışarı verilmesi. Kur’an bu iki çıkarışı yan yana koyar: kabirlerdeki altüst edilir ve göğüslerdeki ortaya dökülür {source:100:9}, {source:100:10}; kıyamet günü kitap çıkarılır ve açılmış bulunur {source:17:13}.

Dördüncü buluşma altıncı ayetin kendisidir. Sudan dönen kalabalık bir yöne yürür ve ayet varış yerini söyler: {ar:لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:li-yurav a‘mâlehum, gloss:amelleri kendilerine gösterilsin diye, source:99:6}. Yolun sonunda tutulan ayna vardır. Aynı kalabalık bölüklere serpilir ve zerre imgesi başlar; bölükler arasındaki uzaklık da iki payın imgesini açar. Bir kelime, {ar:أَشْتَاتًا, tr:eştâtâ, gloss:bölük bölük, source:99:6}, üç imgeyi birden taşır: sudan dönüş, serpilme ve ak ile kara kadar uzak iki pay.

Son buluşma zerrede olur. {ar:ذَرَّةٍ, tr:zerratin, gloss:zerre, source:99:8} hem serpilmenin en küçük birimidir hem terazideki en küçük ağırlık; kötülük sözünün yanında ateşten kopan kıvılcım, toprağı yarıp çıkan filiz ve güneşte yayılan ince ışık da duyulur. Ağırlık kökü burada çemberi kapatır: sure yerin bütün ağırlıklarıyla açılmış, aynı kökten bir miskalle biter. Lokman’ın oğluna söylediği söz {source:31:16} bu iki ucu birleştirir: yerin içinde gizli bir küçük ağırlık getirilir ve sözü {ar:إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌ, tr:innallâhe latîfun habîr, gloss:Allah en ince şeyi bilen, her şeyden haberdardır, source:31:16} diye biter. Haber kökü burada da durur: yerin anlattığı haberler, her şeyden haberdar olanın bildiğidir. Yer ağırlıklarını verir, haberlerini anlatır; insan da tek tek, en küçük ağırlığına kadar amelini görür.

