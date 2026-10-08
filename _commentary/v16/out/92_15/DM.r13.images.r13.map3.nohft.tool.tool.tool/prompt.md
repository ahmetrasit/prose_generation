Focus: 92:15. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/92_15/D.r13/context.md =====
# 92:15 — focus

لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى

Anchor translation (canonical reading, reference only):

Onda en bahtsız olandan başkası yanmaz.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | لَا | لَا |  | NEG |
| 2 | يَصْلَىٰهَآ | يَصْلَى | ص ل ي | V;PRON |
| 3 | إِلَّا | إِلَّا |  | RES |
| 4 | ٱلْأَشْقَى | أَشْقَى | ش ق و | DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 92 — full text (context; no pericope)

- 92:1 وَٱلَّيْلِ إِذَا يَغْشَىٰ
- 92:2 وَٱلنَّهَارِ إِذَا تَجَلَّىٰ
- 92:3 وَمَا خَلَقَ ٱلذَّكَرَ وَٱلْأُنثَىٰٓ
- 92:4 إِنَّ سَعْيَكُمْ لَشَتَّىٰ
- 92:5 فَأَمَّا مَنْ أَعْطَىٰ وَٱتَّقَىٰ
- 92:6 وَصَدَّقَ بِٱلْحُسْنَىٰ
- 92:7 فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ
- 92:8 وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ
- 92:9 وَكَذَّبَ بِٱلْحُسْنَىٰ
- 92:10 فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ
- 92:11 وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ
- 92:12 إِنَّ عَلَيْنَا لَلْهُدَىٰ
- 92:13 وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- 92:14 فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- 92:15 ◀ focus لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- 92:16 ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- 92:17 وَسَيُجَنَّبُهَا ٱلْأَتْقَى
- 92:18 ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- 92:19 وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- 92:20 إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- 92:21 وَلَسَوْفَ يَرْضَىٰ


===== _commentary/v16/work/92_15/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ص ل ي (root_000880) — identity root of يَصْلَىٰهَآ (w2)

- **B001** ayakta durma, eğilme ve yere kapanmalı yükümlü tapınma — ayakta durma, eğilme ve yere kapanma bölümleri olan yükümlü tapınma
  الصلاة التي جاء بها الشرع من الركوع والسجود (maqayis)؛ الصلاة واحدة الصلوات المفروضة (sihah)؛ الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib)؛ الصلاة التي هي العبادة المخصوصة (mufradat)
- **B002** iyilik dileme; özneye göre esirgeme, övme veya aklama — iyilik dileme; özneye göre esirgeme, övme veya bağışlanma isteme · onun için iyilik dilemek, onu esirgemek ya da aklamak · Tanrı'nın kullarını esirgemesi, övmesi veya aklaması · göksel görevlilerin iyilik ve bağışlanma dilemesi · ölen kişi için iyilik dileme
  الصلاة وهي الدعاء (maqayis)؛ صلوات الرسول للمسلمين دعاؤه لهم وذكرهم (ayn)؛ الصلاة من الله تعالى الرحمة (sihah)؛ الصلاة من الملائكة دعاء واستغفار ومن الله سبحانه رحمة (tahdhib)؛ الصلاة الدعاء والتبريك والتمجيد (mufradat)
- **B003** ateşin veya benzer bir sıkıntının şiddetine uğramak; birini ateşe sokmak [kalıp] — ateşe girip yakıcı sıcağını çekmek · onu ateşe sokmak · ateşin başında ısınmak · bir işin ağır sıkıntısını çekmek · birinin kötülüğüne uğramak · onun sertliğini ve gücünü göze alamamak
  أحدهما النار وما أشبهها من الحمى (maqayis)؛ صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها (ayn)؛ صلي الرجل نارا إذا أدخلته النار (sihah)؛ من يصلى في النار أي يلزم النار (tahdhib)؛ صلي بالنار وبكذا أي بلي بها واصطلى بها (mufradat)
- **B004** ateş yakıtı; ateşte pişirme veya ısıyla düzeltme — ateşi tutuşturan ve başında ısınılan yakıt · ateşte pişirilmiş yiyecek · odun ya da ateş · eti ateşte pişirmek · ateşte pişmiş · değneği ateş üstünde döndürerek yumuşatıp doğrultmak · ateşin üstüne kurulan ocak taşları
  الصلاء ما يصطلى به وما يذكى به النار ويوقد (maqayis)؛ صليت اللحم صليا شويته (ayn;sihah;tahdhib)؛ صلى عصاه إذا أدارها على النار يثقفها (ayn;tahdhib)؛ الصلاء يقال للوقود وللشواء (mufradat)
- **B005** av yakalamak için kurulan kapan — av veya zararlı canlılar için kurulan kapanlar · av yakalamak için kurulan kapan · birini yok oluşa düşürecek bir düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis)؛ المصلاة أن تنصب شركا ونحوه (ayn)؛ المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib)
- **B006** sırtın ortası ve kuyruk dibinin iki yanı — sırtın ortası veya kuyruk dibi ile kuyruk sokumunun iki yanı · kuyruk dibinin iki yanı · doğumda kuyruk dibi bölgesinin açılması · devenin yavrusunun kuyruk dibi bölgesine inmesi ve doğumun yaklaşması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn)؛ انفرج صلاها (ayn)؛ الصلوين مكتنفا الذنب (tahdhib)؛ أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها (tahdhib)
- **B007** yarışta önderin hemen ardındaki ikinci at — yarışta önderin hemen ardındaki ikinci at · atın önder atın hemen ardından gelmesi
  أتى الفرس على أثر الفرس السابق قيل قد صلى وجاء مصليا (ayn)؛ المصلى تالي السابق (sihah)؛ السابق الأول والمصلي الثاني (tahdhib)
- **B008** tapınma yeri, özellikle Yahudi tapınağı — Yahudi tapınakları veya genel olarak tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn)؛ الصلوات كنائس اليهود (tahdhib)؛ يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B009** üzerinde madde dövülen geniş taş — üzerinde koku maddesi veya başka maddeler dövülen geniş taş · üzerinde madde dövülen geniş taş
  الصلاية الفهر (sihah)؛ الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib)؛ الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B010** iri başaklı deve yemi bitkisi — iri başaklı, develere yem olan bitki · bu iri başaklı bitkinin yetiştiği yer
  الصليان نبت على فعلان ويقال فعليان له سنمة عظيمة (ayn)؛ الصليان نبت له سبطة عظيمة (tahdhib)؛ تسميها العرب خبزة الإبل (ayn;tahdhib)

## ش ق و (root_000808) — identity root of ٱلْأَشْقَى (w4)

- **B001** mutluluğun karşıtı olan mutsuzluk — mutsuzluk, bahtsızlık · mutsuz, bahtsız kimse · Tanrı onu mutsuzluğa düşürdü
  الشقوة خلاف السعادة (maqayis)؛ الشقاء والشقاوة بالفتح: نقيض السعادة (sihah)؛ الشقاوة: خلاف السعادة، والشقاوة الأخروية والدنيوية (mufradat)
- **B002** güçlük çekme ve zorluğa dayanma — güçlük, sıkıntı ve yorucu uğraş · bu işte yoruldum ve güçlük çektim · zorluğa katlanma, uğraşıp dayanma ve savaşta boğuşma · onunla uğraştım ve güçlüğüne katlandım · o işle uğraşıp güçlüğünü çektim
  أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (maqayis;sihah)؛ الشقاء: الشدة والعسر، وشاقيته أي صابرته، وشاقيت ذلك الأمر بمعنى عانيته، والمشاقاة: المعالجة في الحرب وغيرها (tahdhib)؛ يوضع الشقاء موضع التعب، وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)
- **B003** karşılıklı uğraşta ötekini yenme [kalıp] — benimle çekişti, ben de o işte onu yendim
  شاقاني فلان فشقوته أشقوه، أي غلبته فيه (sihah)
- **B004** uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı — uzun, kolay çıkılan ve oturmaya elverişli dağ sırtı; bu tür dağ sırtları
  الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)

## ECHO ص ل و (root_000879) — for يَصْلَىٰهَآ (w2): withheld observed target; not identity

- **B001** ateşin yakıcı sıcaklığına maruz kalma ve ateşle işleme — ateşe girip onun yakıcı sıcaklığını çekmek · ateşin yanında ısınmak · eti ateşte pişirmek · ateşte pişirilmiş · birini ateşe atıp yakmak · ateşi besleyen yakacak; ateşte pişirme · değneği ateşte yumuşatıp düzeltmek · bir işin güçlüğünü ve yorgunluğunu çekmek · onun sertliğine kimse yanaşamaz
  صليت العود بالنار (maqayis); اصطليت بالنار (maqayis;sihah); الصلا النار وصلى الكافر نارا (ayn); صليت اللحم شويته (ayn;sihah;tahdhib); الصلاء يقال للوقود وللشواء (mufradat); صلي بالأمر إذا قاسى حره وشدته (sihah;tahdhib)
- **B002** başkası için iyilik dileme; esirgeme, övme ve değer verme — başkası için iyilik ve esenlik dileme · biri için iyilik dilemek, onu övmek veya esirgenmesini istemek · Tanrı'nın esirgemesi, övmesi, bağışlaması ve değer vermesi · meleklerin bağışlanma ve iyilik dilemesi
  الصلاة وهي الدعاء (maqayis;sihah); صلوات الرسول للمسلمين دعاؤه لهم (ayn); الصلاة من الله تعالى الرحمة (maqayis;sihah;tahdhib); صلوات الله حسن ثنائه عليهم وقيل مغفرته لهم (ayn); صلاة الملائكة الاستغفار (ayn;tahdhib;mufradat); صلاة الله للمسلمين تزكيته إياهم (mufradat)
- **B003** ayakta durma, eğilme ve yere kapanma bölümleri olan kurallı tapınma — namaz · namazı bütün gerek ve koşullarını yerine getirerek kılmak
  الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة (maqayis); الصلاة واحدة الصلوات المفروضة (sihah); الصلاة من المخلوقين القيام والركوع والسجود والدعاء والتسبيح (tahdhib); الصلاة التي هي العبادة المخصوصة أصلها الدعاء (mufradat); إقامة الصلاة (mufradat)
- **B004** yakalamak için kurulan tuzak — av için kurulan tuzak · avı veya başka hedefleri yakalayan tuzaklar · birini yıkıma düşürmek için gizlice düzen kurmak
  مصالي هي الأشراك واحدتها مصلاة (maqayis); المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد (ayn); المصالي شبيهة بالشرك تنصب للطير وغيرها (tahdhib); صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة (tahdhib)
- **B005** sırtın ortası ve kuyruk kökünün iki yanı — sırtın orta bölümü veya kuyruk kökünün iki yanı · kuyruk kökünün iki yanı · doğum sırasında kuyruk kökü çevresinin açılması
  الصلا وسط الظهر لكل ذي أربع وللناس (ayn); كل أنثى إذا ولدت انفرج صلاها (ayn); الصلوين وهما مكتنفا الذنب من الناقة وغيرها (tahdhib); أصلت الناقة فهي مصلية إذا وقع ولدها في صلاها وقرب نتاجها (tahdhib)
- **B006** yarışta birincinin hemen ardındaki ikinci — yarışta birincinin ardından gelen ikinci · yarışta liderin hemen ardından ikinci gelmek
  قد صلى وجاء مصليا لأن رأسه يتلو الصلا الذي بين يديه (ayn); المصلى تالي السابق (sihah); السابق الأول والمصلي الثاني (tahdhib); يكون عند صلا الأول (tahdhib)
- **B007** tapınma yeri; kilise — Yahudilerin kiliseleri veya bir din topluluğunun tapınma yerleri · tapınma yeri
  صلوات اليهود كنائسهم واحدها صلاة (ayn); الصلوات كنائس اليهود (tahdhib); قيل إنها مواضع صلوات الصابئين (tahdhib); يسمى موضع العبادة الصلاة ولذلك سميت الكنائس صلوات (mufradat)
- **B008** üzerinde dövme yapılan geniş taş — üzerinde malzeme dövülen geniş taş · dövme taşı
  الصلاية الفهر (sihah); الصلاءة بالهمز مثله (sihah); الصلاية كل حجر عريض يدق عليه عطر أو هبيد (tahdhib); الصلاية سريحة خشنة غليظة من القف (tahdhib)
- **B009** iri başaklı, develerin otladığı bir bitki — iri başaklı, develerin otladığı bir bitki · bu bitkinin yetiştiği arazi
  الصليان نبت (ayn;tahdhib); له سنمة عظيمة كأنها رأس القصبة (ayn); له سبطة عظيمة كأنها رأس القصبة (tahdhib); تسميها العرب خبزة الإبل (ayn;tahdhib)

## ECHO ش ق ي (root_000809) — for ٱلْأَشْقَى (w4): withheld observed target; not identity

- **B001** bedbahtlık ve bedbaht duruma düşürme — bedbaht olmak · bedbahtlık · bedbahtlık · bu dünyada veya ölümden sonraki yaşamda bedbahtlık · onu bedbaht duruma düşürmek
  الشقوة خلاف السعادة (maqayis)؛ شقي شقاء وشقوة وأصل الشقاء والشقوة (ayn)؛ الشقاء والشقاوة نقيض السعادة وأشقاه الله (sihah)؛ شقي شقاء وشقاوة وشقوة (tahdhib)؛ الشقاوة خلاف السعادة (mufradat)
- **B002** zorluk ve yorucu uğraş — güçlük, zorluk ve yorucu sıkıntı · bir işte yorulmak veya güçlük çekmek · uğraşma, yaşayarak sürdürme ve katlanma · bir işle uğraşmak ve ona katlanmak
  أصل يدل على المعاناة وخلاف السهولة (maqayis)؛ المشاقاة المعاناة والممارسة (sihah)؛ الشقاء الشدة والعسر وشاقيت ذلك الأمر بمعنى عانيته (tahdhib)؛ يوضع الشقاء موضع التعب وكل شقاوة تعب وليس كل تعب شقاوة (mufradat)
- **B003** biriyle karşılıklı uğraşıp mücadele etme — biriyle ilişki kurup ona karşı direnmek veya onunla uğraşmak · benimle çekişti, ben de onu o işte yendim
  المشاقاة المعاناة والممارسة (maqayis;sihah)؛ شاقاني فلان فشقوته أي غلبته فيه (sihah)؛ شاقيت فلانا مشاقاة إذا عاشرته وعاشرك (tahdhib)؛ شاقيته أي صابرته والمشاقاة المعالجة في الحرب وغيرها (tahdhib)
- **B004** kolay çıkılan, oturmaya elverişli uzun dağ sırtı — kolay çıkılan ve oturmaya elverişli uzun dağ sırtı
  الشاقي من حيود الجبال الطالع الطويل ومع طوله أيسر صعودا وأقدر مقعدا للإنسان والجميع شاقيات وشواقي (ayn)

===== _commentary/v16/out/s092/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 92:15, and ## Buluşmalar) =====
## Kuyuya düşüş, yükseğe çağrı

On birinci ayetin fiili {ar:تَرَدَّىٰٓ, tr:teraddâ, gloss:yuvarlandı, helak oldu, source:92:11} bir düşüşü anlatır: {ar:ردى في البئر وتردى إذا سقط في بئر, tr:radiye fi'l-bi'ri ve teraddâ izâ sekata fî bi'r, gloss:kuyuya düştü, source:"ر د ي,B003"}. Düşüşün bir körlüğü de vardır: {ar:التردي هو التهور في مهواة, tr:et-teraddî hüve't-tehevvüru fî mehvâ, gloss:teraddî bir uçuruma gözü kapalı atılmaktır, source:"ر د ي,B003"}. Bir başka tanım {ar:الردى الهلاك والتردي التعرض للهلاك, tr:er-redâ'l-helâku ve't-teraddî't-tearrudu li'l-helâk, gloss:redâ helaktır; teraddî kendini helake maruz bırakmaktır, source:"ر د ي,B003"} der. Sahne bir kuyu ağzıdır: adam hızla yürür, önüne bakmaz ve boşluğa yuvarlanır. Ayet tam o anı seçer, malının ona {ar:وَمَا يُغْنِى عَنْهُ مَالُهُۥٓ إِذَا تَرَدَّىٰٓ, tr:ve mâ yuğnî anhü mâlühû izâ teraddâ, gloss:yuvarlandığında malı ona bir şey kazandırmaz, source:92:11} hükmüyle bir şey kazandırmadığı anı. Düşen adamın elinde ne olduğu düşüşü durdurmaz. On beşinci ayetin kökü de bir tuzağı adlandırır: {ar:مصالي هي الأشراك واحدتها مصلاة, tr:mesâlî hiye'l-eşrâk vâhidetühâ mıslât, gloss:mesâlî tuzaklardır; tekili mıslâttır, source:"ص ل ي,B005"}. Ayetteki anlam ateşe girip yanmaktır. Ailesinde ise ayağa geçen bir tuzak duyulur. On yedinci ayet bu düşüşün tersini verir: {ar:وجنبته الشيء أي نحيته عنه, tr:ve cenebtühü'ş-şey'e ey nahhaytühû anh, gloss:onu bir şeyden uzaklaştırdım, kenara çektim, source:"ج ن ب,B003"}. Sakınan kişi kuyunun ağzından kenara çekilir. Yirminci ayette ise çizgi yukarı döner: {ar:ٱلْأَعْلَىٰ, tr:el-a'lâ, gloss:en yüce, source:92:20}. Kök yüksekliğin kendisidir: {ar:العلو ضد السفل والعلو الارتفاع, tr:el-uluvvu diddü's-süfli ve'l-uluvvu'l-irtifâ', gloss:yükseklik alçaklığın zıddıdır, yükselmektir, source:"ع ل و,B001"}. Aynı kökten bir çağrı da doğar: {ar:تعال أصله أن يدعى الإنسان إلى مكان مرتفع, tr:teâle asluhû en yüd'a'l-insânu ilâ mekânin murtefi', gloss:teâl, yani gel, aslında insanın yüksek bir yere çağrılmasıdır, source:"ع ل و,B006"}. Sure böylece bir dikey eksen kurar. Bir adam aşağı yuvarlanır, öteki kenara çekilir ve yüzünü en yüceye çevirir. Düz anlam iki sonucu anlatır, görüntü ise iki yönü gösterir: biri aşağı, öteki yukarı.

Kur'an düşüşü sahneler. Düşerek ölen hayvan haram kılınanlar arasında sayılır: {ar:وَٱلْمُتَرَدِّيَةُ, tr:ve'l-müteraddiye, gloss:düşerek ölen hayvan, source:5:3}. Cennet ehlinden biri dünyadaki arkadaşını anar, aşağı bakar, onu cehennemin ortasında görür ve şöyle der: {ar:تَٱللَّهِ إِن كِدتَّ لَتُرْدِينِ, tr:ta'llâhi in kidte le-türdîn, gloss:Allah'a andolsun beni de neredeyse yuvarlayacaktın, source:37:56}. Yükseklikten aşağıya bakan bir göz ve kıl payı kurtulmuş bir ayak vardır. Musa'ya Saat hakkında şu uyarı yapılır: inanmayan ve hevesine uyan biri seni ondan alıkoymasın {ar:فَتَرْدَىٰ, tr:fe-terdâ, gloss:yoksa helak olursun, source:20:16}. Uçurum kenarındaki yapı da şöyle anlatılır: {ar:عَلَىٰ شَفَا جُرُفٍ هَارٍۢ فَٱنْهَارَ بِهِۦ فِى نَارِ جَهَنَّمَ, tr:alâ şefâ cürufin hârin fenhâra bihî fî nâri cehennem, gloss:çökmek üzere olan bir yarın kenarına; o da onunla birlikte cehennem ateşine yıkıldı, source:9:109}. Bunun karşısındaki yapı {ar:عَلَىٰ تَقْوَىٰ مِنَ ٱللَّهِ وَرِضْوَٰنٍ, tr:alâ takvâ mina'llâhi ve ridvân, gloss:Allah'tan sakınma ve hoşnutluk üzerine, source:9:109} kurulmuştur. Bu ayette surenin beşinci ve yirmi birinci ayetlerinin kökleri temeli oluşturur, düşüş ise ateşe varır. Müminlere de geçmişleri hatırlatılır: {ar:وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍۢ مِّنَ ٱلنَّارِ فَأَنقَذَكُم مِّنْهَا, tr:ve küntüm alâ şefâ hufratin mine'n-nâri fe-enkazeküm minhâ, gloss:ateşten bir çukurun kenarındaydınız; sizi oradan kurtardı, source:3:103}. Bir kenarda kulluk eden de anılır: sınandığında {ar:ٱنقَلَبَ عَلَىٰ وَجْهِهِۦ, tr:inkalebe alâ vechih, gloss:yüzüstü döndü, source:22:11}. Yüz ve düşüş tek harekette birleşir. Çıkış yönü de sahnelenir: {ar:فَلَا ٱقْتَحَمَ ٱلْعَقَبَةَ, tr:fe-le'ktehame'l-akabe, gloss:ama o sarp yokuşa atılmadı, source:90:11}. Yokuşun ne olduğu da söylenir: {ar:فَكُّ رَقَبَةٍ, tr:fekkü rakabe, gloss:bir boyunu çözmek, source:90:13}. Yükseğe çıkmak bir köleyi azat etmek ve aç doyurmaktır, yani malı vermektir. Yüceliğin sahibi de bellidir: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-a'lâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1}. Bunun sahte bir iddiası da vardır. Firavun şöyle der: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe-kâle ene rabbükümü'l-a'lâ, gloss:ben sizin en yüce rabbinizim dedi, source:79:24}. Hemen ardından {ar:فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ, tr:fe-ehazehu'llâhu nekâle'l-âhirati ve'l-ûlâ, gloss:Allah onu sonranın ve öncenin cezasıyla yakaladı, source:79:25} gelir. Yüksekliği kendine mal eden, surenin on üçüncü ayetinin iki kelimesiyle aşağı indirilir.

Kaynaklar: 92:11 تَرَدَّىٰٓ ر د ي B003; 92:15 يَصْلَىٰهَآ ص ل ي B005; 92:17 وَسَيُجَنَّبُهَا ج ن ب B003; 92:20 ٱلْأَعْلَىٰ ع ل و B001; 92:20 ٱلْأَعْلَىٰ ع ل و B006

## Uyarılan ateş ve araya konan siper

On dördüncü ayet bir alarmla başlar: {ar:فَأَنذَرْتُكُمْ, tr:fe-enzertüküm, gloss:sizi uyardım, source:92:14}. Kökün anlamı {ar:الإنذار الإبلاغ ولا يكاد يكون إلا في التخويف, tr:el-inzâru'l-iblâğu ve lâ yekâdü yekûnü illâ fi't-tahvîf, gloss:inzâr haber ulaştırmaktır ve neredeyse hep korkutmak için olur, source:"ن ذ ر,B001"} diye verilir. Örnek sahnesi bir düşman baskınıdır: {ar:أنذرت القوم مسير عدوهم إليهم فنذروا أي علموا فتحرزوا, tr:enzertü'l-kavme mesîra adüvvihim ileyhim fe-nezirû ey alimû fe-teharrazû, gloss:kavmi düşmanın üzerlerine yürüdüğüne karşı uyardım; öğrendiler ve tedbir aldılar, source:"ن ذ ر,B001"}. Uyarının en çıplak biçimi {ar:أنا النذير العريان, tr:ene'n-nezîru'l-uryân, gloss:ben çıplak uyarıcıyım, source:"ن ذ ر,B001"} sözüdür: Elbisesini sıyırıp sallayan adam, görenlerin uzaktan anlayacağı bir işaret verir. Uyarının işi bitmiş sayılmaz, uyarılanlar tedbir aldığında tamamlanır. Ayet uyarılan şeyi de adlandırır: {ar:نَارًۭا تَلَظَّىٰ, tr:nâran telezzâ, gloss:alev alev yanan bir ateş, source:92:14}. Ateşin adı titreyen ışıktır: {ar:ولأن ذلك يكون مضطربا سريع الحركة, tr:ve li-enne zâlike yekûnü muzdariben serîa'l-hareke, gloss:çünkü o çırpınan ve hızlı hareket eden bir şeydir, source:"ن و ر,B002"}. Fiil ise saf alevdir: {ar:اللظى اللهب الخالص, tr:el-lezâ'l-lehebü'l-hâlis, gloss:lezâ katışıksız alevdir, source:"ل ظ ي,B001"}. Bu ayetin kendisi de {ar:نارا تلظى أي تتوهج وتتوقد, tr:nâran telezzâ ey tetevehhecu ve tetevakkadu, gloss:alev alev yanan ateş yani parlayıp tutuşan ateş, source:"ل ظ ي,B001"} diye açıklanır. Aynı kelime cehennemin özel adıdır: {ar:لظى غير مصروفة اسم لجهنم, tr:lezâ ğayru masrûfetin ismün li-cehennem, gloss:Lezâ cehennemin adıdır, source:"ل ظ ي,B002"}. Ayrıca öfkeyle yanmayı da anlatır: {ar:فلان يتلظى على فلان تلظيا إذا توقد عليه من شدة الغضب, tr:fülânün yetelezzâ alâ fülânin telezziyen izâ tevakkade aleyhi min şiddeti'l-ğadab, gloss:biri öfkenin şiddetinden ötekine karşı tutuşursa ona yetelezzâ denir, source:"ل ظ ي,B003"}. Ateş yalnızca sıcak değil, kızgındır.

On beşinci ayet içeri girişi anlatır: {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girip yanmaz, source:92:15}. Fiil {ar:صلى الكافر نارا فهو يصلاها أي قاسى حرها وشدتها, tr:saliye'l-kâfiru nâran fehüve yaslâhâ ey kâsâ harrahâ ve şiddetehâ, gloss:inkârcı ateşe girdi yani onun sıcağına ve şiddetine katlandı, source:"ص ل ي,B003"} diye açıklanır. Ateşe girmek ve orada kalmak da anlatılır: {ar:صلي الرجل نارا إذا أدخلته النار, tr:suliye'r-racülü nâran izâ edhaltehü'n-nâr, gloss:adam ateşe sokuldu, source:"ص ل ي,B003"}; {ar:من يصلى في النار أي يلزم النار, tr:men yuslâ fi'n-nâri ey yelzemü'n-nâr, gloss:ateşe atılan, ateşten ayrılmayan, source:"ص ل ي,B003"}. Aynı kökün bir zanaat anlamı da vardır: {ar:صلى عصاه إذا أدارها على النار يثقفها, tr:salâ asâhü izâ edârahâ ale'n-nâri yüsakkıfuhâ, gloss:değneğini düzeltmek için ateşin üstünde çevirdi, source:"ص ل ي,B004"}. Et kızartmak da bu köktendir: {ar:صليت اللحم صليا شويته, tr:saleytü'l-lahme salyen şeveytüh, gloss:eti kızarttım, source:"ص ل ي,B004"}. Onuncu ayette yolun adı {ar:العسر الخلاف والالتواء, tr:el-usru'l-hılâfu ve'l-iltivâ', gloss:ters gitmek ve kıvrılmak, source:"ع س ر,B004"} idi. Ateşin yanındaki zanaatkâr ise eğri değneği ateşin üstünde çevirerek doğrultur. Kıvrık yolu seçen, eğrinin doğrultulduğu ateşe varır. Bu, iki kök arasında kurulan bir bağdır, aynı kökten gelen bir kimlik değildir. Yanan kişinin adı da sahneye girer: {ar:الشقوة خلاف السعادة, tr:eş-şıkvetü hılâfü's-saâde, gloss:bedbahtlık mutluluğun karşıtıdır, source:"ش ق و,B001"}. Kelimenin bir dalı onu doğrudan onuncu ayete bağlar: {ar:الشقاء: الشدة والعسر, tr:eş-şekâ': eş-şiddetü ve'l-usr, gloss:şekâ sıkıntı ve zorluktur, source:"ش ق و,B002"}. En bedbaht kişi, en zora kolaylaştırılan kişidir.

Karşı tarafta bir siper vardır. Beşinci ve on yedinci ayetlerin kökü {ar:دفع شيء عن شيء بغيره, tr:def'u şey'in an şey'in bi-ğayrih, gloss:bir şeyi bir şeyden başka bir şeyle savmak, source:"و ق ي,B001"} demektir. Sakınma bir ara katman kurmaktır: {ar:اتق الله توقه أي اجعل بينك وبينه كالوقاية, tr:itteki'llâhe tevakkahû ey ic'al beyneke ve beynehû ke'l-vikâye, gloss:Allah'tan sakın yani seninle O'nun arasına bir siper koy, source:"و ق ي,B002"}. Takva da {ar:التقوى جعل النفس في وقاية مما يخاف, tr:et-takvâ ca'lü'n-nefsi fî vikâyetin mimmâ yuhâf, gloss:takva insanın kendini korkulan şeye karşı bir siperin içine koymasıdır, source:"و ق ي,B002"} diye tanımlanır. On yedinci ayetin fiili ise başkasının yaptığı bir savmadır: {ar:جنبته عن كذا فاجتنب أي تجنبه وجنبته أي دفعت عنه مكروها, tr:cenebtühû an kezâ fe'ctenebe ey tecennebehû ve cenebtühû ey defa'tü anhü mekrûhâ, gloss:onu şundan uzaklaştırdım o da kaçındı; ondan kötülüğü savdım, source:"ج ن ب,B003"}. Savma fiili iki kökte de geçer: sakınan kişi kendi tarafında bir siper kurar ve Allah onun üzerinden kötülüğü savar. İnsanın yanında da bir kalkan durur, {ar:سمي الترس مجنبا لأنه إلى جنب الإنسان, tr:sümmiye't-tursu micnenben li-ennehû ilâ cenbi'l-insân, gloss:kalkana mıcneb denir çünkü insanın yanında durur, source:"ج ن ب,B011"}. Sahnenin sırası şöyledir. Beşinci ayette siper önceden kurulur. On dördüncü ayette alarm verilir. On beşinci ayette alarmı duymayan ateşe girer. On altıncı ayet onun alarmı nasıl karşıladığını söyler: yalanladı ve yüz çevirdi. Uyarı sahnesindeki "öğrendiler ve tedbir aldılar" adımını hiç atmadı. On yedinci ayette tedbir alan kenara çekilir. On ikinci ve on üçüncü ayetlerde "biz" diye konuşan ses, on dördüncü ayette "ben" der: alarmı veren tek bir sestir.

Kur'an bu sahnenin her parçasını başka yerlerde de kurar. Bir önceki surenin sonunda Semud kavmi peygamberini yalanlamıştır: {ar:إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا, tr:izi'nbease eşkâhâ, gloss:içlerinden en bedbahtı kalkıp gittiğinde, source:91:12}. Ardından {ar:فَكَذَّبُوهُ فَعَقَرُوهَا, tr:fe-kezzebûhu fe-akarûhâ, gloss:onu yalanladılar ve deveyi kestiler, source:91:14} gelir. En bedbahtın adı ve yalanlamanın fiili yan yanadır. Bir başka surede aynı kelimeler rolleri değişerek gelir: {ar:سَيَذَّكَّرُ مَن يَخْشَىٰ, tr:seyezzekkeru men yahşâ, gloss:korkan öğüt alacak, source:87:10}, {ar:وَيَتَجَنَّبُهَا ٱلْأَشْقَى, tr:ve yetecennebühe'l-eşkâ, gloss:en bedbaht ondan kaçınacak, source:87:11}, {ar:ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ, tr:ellezî yasla'n-nâra'l-kübrâ, gloss:o ki en büyük ateşe girecek, source:87:12}. Orada en bedbaht öğütten kaçınır. Bu surede ise en sakınan kişi ateşten uzak tutulur. Kaçınma fiili iki surede iki ayrı şeye yönelir. Lezâ'nın kimi çağırdığı da söylenir: {ar:كَلَّآ ۖ إِنَّهَا لَظَىٰ, tr:kellâ innehâ lezâ, gloss:hayır; o Lezâ'dır, source:70:15}, {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:ted'û men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}, {ar:وَجَمَعَ فَأَوْعَىٰٓ, tr:ve cemea fe-ev'â, gloss:ve toplayıp yığanı, source:70:18}. Ateşin öfkesi de anlatılır: {ar:تَكَادُ تَمَيَّزُ مِنَ ٱلْغَيْظِ ۖ كُلَّمَآ أُلْقِىَ فِيهَا فَوْجٌۭ سَأَلَهُمْ خَزَنَتُهَآ أَلَمْ يَأْتِكُمْ نَذِيرٌۭ, tr:tekâdü temeyyezü mine'l-ğayz küllemâ ulkıye fîhâ fevcün seelehüm hazenetühâ elem ye'tiküm nezîr, gloss:öfkeden neredeyse çatlayacaktır; içine her bölük atıldığında bekçileri onlara size bir uyarıcı gelmedi mi diye sorar, source:67:8}. Cevap şudur: {ar:قَالُوا۟ بَلَىٰ قَدْ جَآءَنَا نَذِيرٌۭ فَكَذَّبْنَا, tr:kâlû belâ kad câenâ nezîrun fe-kezzebnâ, gloss:evet bize bir uyarıcı geldi ama yalanladık dediler, source:67:9}. Uyarı, yalanlama ve ateş tek konuşmada durur. Siper de defalarca buyrulur: {ar:فَٱتَّقُوا۟ ٱلنَّارَ ٱلَّتِى وَقُودُهَا ٱلنَّاسُ وَٱلْحِجَارَةُ, tr:fe'ttekû'n-nâra'lletî vekûduhe'n-nâsu ve'l-hicâra, gloss:yakıtı insanlar ve taşlar olan ateşten sakının, source:2:24}; {ar:قُوٓا۟ أَنفُسَكُمْ وَأَهْلِيكُمْ نَارًۭا, tr:kû enfüseküm ve ehlîküm nârâ, gloss:kendinizi ve ailenizi bir ateşten koruyun, source:66:6}. Kenara çekilme ise bir kurtarmadır: {ar:ثُمَّ نُنَجِّى ٱلَّذِينَ ٱتَّقَوا۟, tr:sümme nünecci'llezîne't-tekav, gloss:sonra sakınanları kurtarırız, source:19:72}; {ar:فَمَن زُحْزِحَ عَنِ ٱلنَّارِ وَأُدْخِلَ ٱلْجَنَّةَ فَقَدْ فَازَ, tr:fe-men zuhziha ani'n-nâri ve udhıle'l-cennete fe-kad fâz, gloss:kim ateşten uzaklaştırılır ve cennete sokulursa kurtulmuştur, source:3:185}. Allah'ın yüzü için yedirenler de korunur: {ar:فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ, tr:fe-vekâhumu'llâhu şerra zâlike'l-yevm, gloss:Allah onları o günün kötülüğünden korudu, source:76:11}. Uyarıcının kendisi de konuşur. Peygambere şunu demesi buyrulur: {ar:إِنْ هُوَ إِلَّا نَذِيرٌۭ لَّكُم بَيْنَ يَدَىْ عَذَابٍۢ شَدِيدٍۢ, tr:in hüve illâ nezîrun leküm beyne yedey azâbin şedîd, gloss:o şiddetli bir azabın önünde sizin için bir uyarıcıdır yalnızca, source:34:46}. Surenin birinci tekil uyarısı da şöyle yankılanır: {ar:إِنَّآ أَنذَرْنَٰكُمْ عَذَابًۭا قَرِيبًۭا يَوْمَ يَنظُرُ ٱلْمَرْءُ مَا قَدَّمَتْ يَدَاهُ, tr:innâ enzernâküm azâben karîben yevme yenzuru'l-mer'ü mâ kaddemet yedâh, gloss:sizi yakın bir azaba karşı uyardık; o gün kişi ellerinin önden gönderdiğine bakar, source:78:40}.

Kaynaklar: 92:5 وَٱتَّقَىٰ و ق ي B001; 92:5 وَٱتَّقَىٰ و ق ي B002; 92:10 لِلْعُسْرَىٰ ع س ر B004; 92:14 فَأَنذَرْتُكُمْ ن ذ ر B001; 92:14 نَارًۭا ن و ر B002; 92:14 تَلَظَّىٰ ل ظ ي B001; 92:14 تَلَظَّىٰ ل ظ ي B002; 92:14 تَلَظَّىٰ ل ظ ي B003; 92:15 يَصْلَىٰهَآ ص ل ي B003; 92:15 يَصْلَىٰهَآ ص ل ي B004; 92:15 ٱلْأَشْقَى ش ق و B001; 92:15 ٱلْأَشْقَى ش ق و B002; 92:17 ٱلْأَتْقَى و ق ي B001; 92:17 ٱلْأَتْقَى و ق ي B002; 92:17 وَسَيُجَنَّبُهَا ج ن ب B003; 92:17 وَسَيُجَنَّبُهَا ج ن ب B011

## Buluşmalar

Görüntülerin en sık birleştiği yer, uçurum ile elin aynı sahnede durmasıdır. Cennet ehlinden biri dünyadaki arkadaşını anlatır. Arkadaşı ona alay ederek şöyle sormuştur: {ar:يَقُولُ أَءِنَّكَ لَمِنَ ٱلْمُصَدِّقِينَ, tr:yekûlü einneke le-mine'l-musaddikîn, gloss:sen de mi doğrulayanlardansın derdi, source:37:52}. Sonra adam aşağı bakar ve arkadaşını ateşin ortasında görür: {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettalea fe-raâhu fî sevâi'l-cahîm, gloss:eğilip baktı ve onu cehennemin ortasında gördü, source:37:55}. Ona şöyle der: {ar:تَٱللَّهِ إِن كِدتَّ لَتُرْدِينِ, tr:ta'llâhi in kidte le-türdîn, gloss:Allah'a andolsun beni de neredeyse yuvarlayacaktın, source:37:56}. Ardından ekler: {ar:وَلَوْلَا نِعْمَةُ رَبِّى لَكُنتُ مِنَ ٱلْمُحْضَرِينَ, tr:ve levlâ ni'metü rabbî le-küntü mine'l-muhdarîn, gloss:Rabbimin nimeti olmasaydı ben de oraya getirilenlerden olurdum, source:37:57}. Bu sahnede doğrulama, yuvarlanma, yüksekten bakış ve bir nimet bir aradadır. Surenin on dokuzuncu ayeti verenin yanında kimsenin bir nimeti olmadığını söyler. Cennet ehli ise kurtuluşunu tek bir nimete, Rabbinin nimetine bağlar. İnsanlar arasında karşılığı ödenecek bir el yoktur, ama Rabbin eli her şeyi taşır. Bir başka ayet aynı birleşmeyi müminlere hatırlatma olarak kurar: Allah'ın nimetiyle kardeş olmuşlardır ve {ar:وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍۢ مِّنَ ٱلنَّارِ فَأَنقَذَكُم مِّنْهَا, tr:ve küntüm alâ şefâ hufratin mine'n-nâri fe-enkazeküm minhâ, gloss:ateşten bir çukurun kenarındaydınız; sizi oradan kurtardı, source:3:103}. Ayet {ar:لَعَلَّكُمْ تَهْتَدُونَ, tr:leallekum tehtedûn, gloss:doğru yolu bulasınız diye, source:3:103} diye kapanır. Kuyunun kenarı, nimet ve yol gösterme tek ayettedir. Kenara çekilen, uyarı ateşini işaret ateşi olarak okuyandır.

İkinci büyük buluşma bir sarayda geçer. Musa ile Harun'a Firavun'a ne diyecekleri öğretilir: {ar:وَٱلسَّلَٰمُ عَلَىٰ مَنِ ٱتَّبَعَ ٱلْهُدَىٰٓ, tr:ve's-selâmü alâ meni't-tebea'l-hüdâ, gloss:esenlik yol göstericiye uyanadır, source:20:47}. Ardından {ar:أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ, tr:enne'l-azâbe alâ men kezzebe ve tevellâ, gloss:azap yalanlayıp yüz çevirenedir, source:20:48} gelir. Firavun {ar:قَالَ فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:kâle fe-men rabbükümâ yâ mûsâ, gloss:ey Musa, sizin Rabbiniz kim dedi, source:20:49} diye sorar. Musa şöyle cevap verir: {ar:قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:kâle rabbüne'llezî a'tâ külle şey'in halkahû sümme hedâ, gloss:Rabbimiz her şeye yaratılışını verip sonra yol gösterendir dedi, source:20:50}. Bu cevapta surenin üç fiili aynı cümlededir: üçüncü ayetin yaratması, beşinci ayetin vermesi ve on ikinci ayetin yol göstermesi. Bir ayet önce de on altıncı ayetin iki fiili geçmiştir. Aynı Firavun başka bir surede yüceliği kendine mal eder: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe-kâle ene rabbükümü'l-a'lâ, gloss:ben sizin en yüce rabbinizim dedi, source:79:24}. Ardından {ar:فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ, tr:fe-ehazehu'llâhu nekâle'l-âhirati ve'l-ûlâ, gloss:Allah onu sonranın ve öncenin cezasıyla yakaladı, source:79:25} gelir. Elin, yolun, yüz çevirmenin, yüceliğin ve mülkün görüntüleri burada tek bir karşılaşmada birleşir. Veren Rab ile tutan kral karşı karşıya gelir. Yüceliği iddia eden kral, surenin "son da ilk de bizimdir" sözüyle düşürülür.

Yüz ile elin buluşması iyiliğin tanımında görülür. İyilik yüzü doğuya ya da batıya çevirmek değildir: {ar:لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ, tr:leyse'l-birra en tüvellû vucûheküm kıbele'l-meşriki ve'l-mağrib, gloss:iyilik yüzlerinizi doğu ve batı yönüne çevirmeniz değildir, source:2:177}. Aynı ayet iyiliği şöyle sayar: {ar:وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ, tr:ve âte'l-mâle alâ hubbih, gloss:malı sevmesine rağmen verdi, source:2:177}. Malın gittiği yerler arasında {ar:وَفِى ٱلرِّقَابِ, tr:ve fi'r-rikâb, gloss:boyunları çözmek için, source:2:177} de vardır. Ayet şöyle biter: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ, tr:ülâike'llezîne sadakû ve ülâike hümü'l-müttekûn, gloss:işte doğru olanlar onlardır ve sakınanlar da onlardır, source:2:177}. Yüzü çevirmek, malı vermek, boyun çözmek, hücumu sonuna kadar götüren doğruluk ve siper olan sakınma tek ayette bir araya gelir. Yüz çevirmek iyiliğin kendisi değildir, iyilik eldedir. Ama surenin yirminci ayeti eli tekrar yüze bağlar: veren el, aranan yüz için uzanır. Aynı bağ yoksulları doyuranların sözünde görülür: {ar:إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءًۭ وَلَا شُكُورًا, tr:innemâ nut'imüküm li-vechi'llâhi lâ nürîdü minküm cezâen ve lâ şükûrâ, gloss:sizi yalnızca Allah'ın yüzü için doyuruyoruz; sizden ne karşılık ne teşekkür istiyoruz, source:76:9}. Sözün sonunda {ar:إِنَّا نَخَافُ مِن رَّبِّنَا يَوْمًا عَبُوسًۭا قَمْطَرِيرًۭا, tr:innâ nehâfü min rabbinâ yevmen abûsen kamtarîrâ, gloss:biz Rabbimizden asık suratlı, çetin bir günden korkarız, source:76:10} derler. Sonra {ar:فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ, tr:fe-vekâhumu'llâhu şerra zâlike'l-yevm, gloss:Allah onları o günün kötülüğünden korudu, source:76:11} gelir. El, yüz, karşılığın reddi ve siper bu ayetlerde surenin sırasıyla dizilir. Bunun tam tersi de bir sahne olarak anlatılır. Bir adam Allah'a söz vermiştir: {ar:لَئِنْ ءَاتَىٰنَا مِن فَضْلِهِۦ لَنَصَّدَّقَنَّ, tr:lein âtânâ min fadlihî le-nessaddakanne, gloss:bize lütfundan verirse mutlaka sadaka vereceğiz, source:9:75}. Sonra şu olur: {ar:فَلَمَّآ ءَاتَىٰهُم مِّن فَضْلِهِۦ بَخِلُوا۟ بِهِۦ وَتَوَلَّوا۟ وَّهُم مُّعْرِضُونَ, tr:fe-lemmâ âtâhüm min fadlihî bahılû bihî ve tevellev ve hüm mu'ridûn, gloss:lütfundan verince cimrilik ettiler ve yüz çevirdiler; zaten dönüp gidiyorlardı, source:9:76}. Sıkan el ile dönülen sırt aynı kişidedir. Sekizinci ve on altıncı ayetler tek bir hikâyede birleşir.

Büyüme ile yükseklik, yüksekteki bahçede buluşur. Allah'ın hoşnutluğunu arayarak harcayanların durumu {ar:كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ, tr:ke-meseli cennetin bi-rabvetin esâbehâ vâbilün fe-âtet ükulehâ dı'feyn, gloss:yüksekçe bir yerdeki bahçe gibidir; ona sağanak isabet eder ve ürününü iki kat verir, source:2:265} diye anlatılır. Bu bahçe kuyunun tam karşıtıdır. Aşağıda değil yüksektedir. Yağmur onu süpürmez, büyütür. Verme fiili de bahçenin kendi fiilidir. Aynı yükseklik ateşe dönük bir eğiklikle karşılaşır: Bir yanda takva ve hoşnutluk üzerine kurulmuş yapı, öbür yanda {ar:عَلَىٰ شَفَا جُرُفٍ هَارٍۢ فَٱنْهَارَ بِهِۦ فِى نَارِ جَهَنَّمَ, tr:alâ şefâ cürufin hârin fenhâra bihî fî nâri cehennem, gloss:çökmek üzere olan bir yarın kenarına kurulmuş, onunla birlikte cehennem ateşine yıkılmış yapı, source:9:109} vardır. Biri takva ve hoşnutluk üzerine kurulur, öteki çöküp ateşe düşer. Cimrinin malı da düştüğü yerde onun yanına yapışır: {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhühüm ve cünûbühüm ve zuhûruhüm, gloss:o gün onlar cehennem ateşinde kızdırılır ve alınları, yanları ve sırtları onlarla dağlanır, source:9:35}. Sakınanın yanında bir kalkan durur ve o yanından kötülükten uzak tutulur. Biriktirenin yanı ise biriktirdiğiyle dağlanır. Sırtı da yüz çevirdiği için dönmüş olan sırttır.

Musa'nın ateşi ise işaret ateşi ile yakan ateşi bir arada tutar. Musa ailesine {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidü ale'n-nâri hüdâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10} der. Başka bir anlatımda {ar:لَّعَلَّكُمْ تَصْطَلُونَ, tr:leallekum tastalûn, gloss:belki ısınırsınız, source:27:7} der. Isınmak on beşinci ayetin yanmasıyla aynı köktendir. Yanına yaklaşılan ateş ısıtır ve yol gösterir. İçine girilen ateş ise yakar. Surenin hareketi bu iki mesafe arasında kurulur. İlk iki ayette gece serilir ve gün yarılır. Gece insanların koşusunu örter, gün o koşunun dağıldığını gösterir. Yol ayrılır ve her yol yürüyenine göre düzlenir. Biri verir, siper kurar ve vaadi kendi eliyle doğrular. Öteki malını tutar, ona cübbe gibi bürünür ve vaadi yalanlayıp sırtını döner. Sonra gece yolunda bir ateş yakılır ve bir ses "uyardım" der. Uyarıyı işaret olarak okuyan, dizgini tutulan bir binek gibi kenara çekilir. Yüzü kendisine bir nimet borcu olanlara değil, yüceliğe dönüktür. Uyarıyı duymayan, yuvarlandığı anda elindeki malın ona yetmediğini görür ve ateşin içine girer. Surenin son kelimesi, kayıp devesini arayan adamın onu bulduğu anın kelimesidir: hoşnutluk. Bu hoşnutluk, ilk ayetteki gecenin örtüsünden sonra gelen yüzün açılmasıdır.

