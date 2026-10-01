Focus: 107:4. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/OZTURK/_projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. No other command or tool is available.

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


===== _commentary/v16/work/107_4/D.r13/context.md =====
# 107:4 — focus

فَوَيْلٌۭ لِّلْمُصَلِّينَ

Anchor translation (canonical reading, reference only):

Vay namaz kılanların hâline!

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَوَيْلٌ | وَيْل |  | REM;N |
| 2 | لِّلْمُصَلِّينَ | مُصَلِّين | ص ل و | P;DET;N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 107 — full text (context; no pericope)

- 107:1 أَرَءَيْتَ ٱلَّذِى يُكَذِّبُ بِٱلدِّينِ
- 107:2 فَذَٰلِكَ ٱلَّذِى يَدُعُّ ٱلْيَتِيمَ
- 107:3 وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ
- 107:4 ◀ focus فَوَيْلٌۭ لِّلْمُصَلِّينَ
- 107:5 ٱلَّذِينَ هُمْ عَن صَلَاتِهِمْ سَاهُونَ
- 107:6 ٱلَّذِينَ هُمْ يُرَآءُونَ
- 107:7 وَيَمْنَعُونَ ٱلْمَاعُونَ


===== _commentary/v16/work/107_4/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ص ل و (root_000879) — identity root of لِّلْمُصَلِّينَ (w2)

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

## ECHO ص ل ي (root_000880) — for لِّلْمُصَلِّينَ (w2): withheld observed target; not identity

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

===== _commentary/v16/out/s107/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 107:4, and ## Buluşmalar) =====
## Ocak ve ateş

Namaz kılanları adlandıran kök, aynı harflerle ateşi de kaydeder: {ar:الصلا النار وصلى الكافر نارا, tr:es-salâ en-nâr, ve saliye'l-kâfiru nârâ, gloss:"salâ" ateştir; kâfir ateşe yaslandı, ateşi tattı, source:"ص ل و,B001"}. Bu ateş önce bir ocaktır: {ar:اصطليت بالنار, tr:ıstaleytu bi'n-nâr, gloss:ateşte ısındım, source:"ص ل و,B001"}; {ar:صليت اللحم شويته, tr:saleytü'l-lahme şeveytüh, gloss:eti ateşte pişirdim, kızarttım, source:"ص ل و,B001"}; {ar:الصلاء يقال للوقود وللشواء, tr:es-sılâu yukâlu li'l-vekûdi ve li'ş-şivâ’, gloss:"sılâ" hem yakacak hem kızartma için söylenir, source:"ص ل و,B001"}. Ateş eğriyi de düzeltir: {ar:صليت العود بالنار, tr:saleytü'l-ûde bi'n-nâr, gloss:değneği ateşe tutup düzelttim, source:"ص ل و,B001"}. Isıyla yumuşayan değnek elde doğrultulur. Kökün son yüzü ise yanmaya katlanmaktır: {ar:صلي بالأمر إذا قاسى حره وشدته, tr:saliye bi'l-emri izâ kâsâ harrahû ve şiddeteh, gloss:bir işin sıcağına ve şiddetine katlandığında "saliye bihî" denir, source:"ص ل و,B001"}. Yoksulun kökü de ocağı tanır: {ar:السكن النار التي يسكن بها, tr:es-sekenu'n-nâru'lletî yuskenu bihâ, gloss:"seken", yanında oturulup barınılan ateştir, source:"س ك ن,B004"}.

Dördüncü ayet şöyledir: {ar:فَوَيْلٌۭ لِّلْمُصَلِّينَ, tr:fe-veylun li'l-musallîn, gloss:vay hâline o namaz kılanların, source:107:4}. Ayetin dediği "namaz kılanlar"dır. Ama bu adamları adlandıran kelimenin kökü ateşi de taşır ve imge bu anlamın yanında duyulur. "Veyl" kelimesi yıkımı bildiren bir felaket çığlığıdır {ar:وَيْل, tr:veyl, gloss:yıkım, vay hâli, source:"memory"}. Bu çığlık, ateşin sesini taşıyan bir adın üzerine düşer. Sahnenin işleyişi şudur: Evde ocak ısıtır, eti pişirir, çevresinde oturulur. Üçüncü ayette yoksulun kökü bu barınılan ateşi duyurur. Dördüncü ve beşinci ayetler ise aynı kökün öbür ucuna, ateşe katlanmaya geçer. Tencereyi ve kepçeyi esirgeyenler ocağı paylaşmaz; sonunda ocağın değil, ateşin karşısında dururlar.

Kuran bu geçişi surenin kendi kelimeleriyle kurar. Hâkka suresinde kitabı sol elinden verilen kişi, keşke kitabım verilmeseydi der {source:69:25}. Hakkında emir gelir: {ar:خُذُوهُ فَغُلُّوهُ, tr:huzûhu fe-ġullûh, gloss:tutun onu, bağlayın, source:69:30}, {ar:ثُمَّ ٱلْجَحِيمَ صَلُّوهُ, tr:summe'l-cahîme sallûh, gloss:sonra onu cehenneme sokup yakın, source:69:31}. Buradaki fiil, "musallîn" ile aynı harflerden kurulmuştur ve ateş anlamındadır. Sebep iki ayette verilir. İkincisi bu surenin üçüncü ayetiyle kelimesi kelimesine aynıdır: {ar:إِنَّهُۥ كَانَ لَا يُؤْمِنُ بِٱللَّهِ ٱلْعَظِيمِ, tr:innehû kâne lâ yü'minu bi'llâhi'l-azîm, gloss:çünkü o yüce Allah'a inanmazdı, source:69:33}, {ar:وَلَا يَحُضُّ عَلَىٰ طَعَامِ ٱلْمِسْكِينِ, tr:ve lâ yehuddu alâ ta‘âmi'l-miskîn, gloss:yoksulun yemeğine teşvik etmezdi, source:69:34}. Mutaffifîn suresi beddua kelimesini, yalanlamayı ve yanmayı bir araya getirir: {ar:وَيْلٌۭ يَوْمَئِذٍۢ لِّلْمُكَذِّبِينَ, tr:veylun yevmeizin li'l-mükezzibîn, gloss:o gün vay hâline yalanlayanların, source:83:10}, {ar:ٱلَّذِينَ يُكَذِّبُونَ بِيَوْمِ ٱلدِّينِ, tr:ellezîne yükezzibûne bi-yevmi'd-dîn, gloss:din gününü yalanlayanlar, source:83:11}, {ar:ثُمَّ إِنَّهُمْ لَصَالُوا۟ ٱلْجَحِيمِ, tr:summe innehum le-sâlu'l-cahîm, gloss:sonra onlar mutlaka cehenneme yaslanıp yanacaklar, source:83:16}, {ar:ثُمَّ يُقَالُ هَٰذَا ٱلَّذِى كُنتُم بِهِۦ تُكَذِّبُونَ, tr:summe yukâlu hâza'llezî kuntum bihî tükezzibûn, gloss:sonra denir: işte yalanladığınız şey budur, source:83:17}. Leyl suresinde Allah uyarır: {ar:فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ, tr:fe-enzertukum nâran telezzâ, gloss:sizi alev alev yanan bir ateşle uyardım, source:92:14}, {ar:لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى, tr:lâ yaslâhâ ille'l-eşkâ, gloss:ona en bedbahttan başkası girip yanmaz, source:92:15}, {ar:ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ, tr:ellezî kezzebe ve tevellâ, gloss:yalanlayan ve yüz çeviren, source:92:16}. Aynı sure bu yolun eli sıkılıkla başladığını önceden söylemiştir: {ar:وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ, tr:ve emmâ men bahile ve'staġnâ, gloss:cimrilik edip kendini muhtaç görmeyene gelince, source:92:8}. Nisâ suresi yetimin yemeğini ateşe çevirir: {ar:إِنَّمَا يَأْكُلُونَ فِى بُطُونِهِمْ نَارًۭا ۖ وَسَيَصْلَوْنَ سَعِيرًۭا, tr:innemâ ye'külûne fî butûnihim nârâ, ve se-yaslevne seîrâ, gloss:yetimlerin mallarını haksızca yiyenler karınlarına ancak ateş doldururlar ve alevli bir ateşe gireceklerdir, source:4:10}. Kâf suresinde esirgeyen el ateşe atılır: {ar:أَلْقِيَا فِى جَهَنَّمَ كُلَّ كَفَّارٍ عَنِيدٍۢ, tr:elkıyâ fî cehenneme külle keffârin anîd, gloss:atın cehenneme her inatçı nankörü, source:50:24}, {ar:مَّنَّاعٍۢ لِّلْخَيْرِ مُعْتَدٍۢ مُّرِيبٍ, tr:mennâ‘in li'l-hayri mu‘tedin murîb, gloss:hayrı hep engelleyeni, sınırı aşanı, kuşku içindekini, source:50:25}.

Kaynaklar: 107:4 لِّلْمُصَلِّينَ ص ل و B001; 107:5 صَلَاتِهِمْ ص ل و B001; 107:3 ٱلْمِسْكِينِ س ك ن B004

## Dışa dönük namaz: huzur veren dua

Namazın kökü iki yön taşır. Birincisi belirli sınırları olan bir ibadettir: {ar:الصلاة التي جاء بها الشرع من الركوع والسجود وسائر حدود الصلاة, tr:es-salâtu'lletî câe bihe'ş-şer‘u mine'r-rükû‘i ve's-sücûdi ve sâiri hudûdi's-salâh, gloss:şeriatın getirdiği namaz; rükû, secde ve namazın öteki sınırları, source:"ص ل و,B003"}. İkincisi bir insandan ötekine giden bir dilektir: {ar:الصلاة وهي الدعاء, tr:es-salâtu ve hiye'd-du‘â’, gloss:salât, yani dua, source:"ص ل و,B002"}; {ar:صلوات الرسول للمسلمين دعاؤه لهم, tr:salavâtu'r-resûli li'l-müslimîn du‘âuhû lehum, gloss:Peygamber'in Müslümanlar için salâtı, onlara duasıdır, source:"ص ل و,B002"}; {ar:صلاة الله للمسلمين تزكيته إياهم, tr:salâtu'llâhi li'l-müslimîn tezkiyetuhû iyyâhum, gloss:Allah'ın Müslümanlara salâtı, onları arındırmasıdır, source:"ص ل و,B002"}. Yoksulun kökünün bir kolu bu ikinci yönü bir ayetle birleştirir: {ar:إن صلواتك سكن لهم, tr:inne salavâtike sekenun lehum, gloss:senin duan onlar için bir huzurdur, source:"س ك ن,B004"}. Aynı kol huzuru da tanımlar: {ar:كل ما سكنت إليه من محبوب, tr:küllü mâ sekente ileyhi min mahbûb, gloss:sevilen şeylerden yanında huzur bulduğun her şey, source:"س ك ن,B004"}.

İşleyiş Tevbe suresinde tam bir döngü olarak verilir. Allah Peygamber'e şöyle der: {ar:خُذْ مِنْ أَمْوَٰلِهِمْ صَدَقَةًۭ تُطَهِّرُهُمْ وَتُزَكِّيهِم بِهَا وَصَلِّ عَلَيْهِمْ ۖ إِنَّ صَلَوٰتَكَ سَكَنٌۭ لَّهُمْ, tr:huz min emvâlihim sadakaten tutahhiruhum ve tüzekkîhim bihâ ve salli aleyhim, inne salâteke sekenun lehum, gloss:onların mallarından, kendilerini temizleyip arındıracağın bir sadaka al ve onlar için dua et; senin duan onlara huzur verir, source:9:103}. Maldan bir pay ayrılır, o pay vereni temizler, alan veren için dua eder ve dua verenin içini yatıştırır. Namaz, mal ve huzur tek bir hareketin halkalarıdır. Mâûnun zekât diye de açıklanması {source:"م ع ن,B005"} bu halkanın son ayetteki ucunu verir.

Surenin adamları bu halkayı ortasından koparır. Dördüncü ayet onlara namaz kılanlar der; görünen ibadet yerindedir. Beşinci ayet kalbin o ibadetten gittiğini söyler. Üçüncü ayetteki yoksulun kökü, namazın başkasına vermesi gereken huzuru duyurur. Bu huzur hiçbir yere ulaşmaz, çünkü yedinci ayette pay ayrılmaz. Namazın başkasına yönelen yüzü kapanmış, yalnızca seyirciye dönük yüzü kalmıştır.

Kuran bu iki şeyin birbirinden ayrılmadığını başka ağızlardan da söyletir. Şuayb'in kavmi ona alayla şöyle sorar: {ar:أَصَلَوٰتُكَ تَأْمُرُكَ أَن نَّتْرُكَ مَا يَعْبُدُ ءَابَآؤُنَآ أَوْ أَن نَّفْعَلَ فِىٓ أَمْوَٰلِنَا مَا نَشَٰٓؤُا۟, tr:e-salâtuke te'muruke en netruke mâ ya‘budu âbâunâ ev en nef‘ale fî emvâlinâ mâ neşâ’, gloss:namazın mı sana emrediyor, atalarımızın taptığını bırakmamızı ya da mallarımız hakkında dilediğimizi yapmaktan vazgeçmemizi, source:11:87}. Karşı çıkanlar bile namazın malın kullanılışına uzandığını görmektedir. Meryem suresinde beşikteki çocuk, yani Îsâ, kendisi hakkında şöyle der: {ar:وَأَوْصَٰنِى بِٱلصَّلَوٰةِ وَٱلزَّكَوٰةِ مَا دُمْتُ حَيًّۭا, tr:ve evsânî bi's-salâti ve'z-zekâti mâ dumtu hayyâ, gloss:yaşadıkça bana namazı ve zekâtı emretti, source:19:31}. Bakara suresinde İsrâiloğulları'ndan alınan söz bu surenin kişilerini sayar: anne baba, yakınlar, yetimler, yoksullar, güzel söz, namaz ve zekât. Ardından şu gelir: {ar:ثُمَّ تَوَلَّيْتُمْ إِلَّا قَلِيلًۭا مِّنكُمْ وَأَنتُم مُّعْرِضُونَ, tr:summe tevelleytum illâ kalîlen minkum ve entum mu‘ridûn, gloss:sonra pek azınız dışında yüz çevirdiniz; zaten dönüp gidenlersiniz, source:2:83}. Tevbe suresinde Allah münafıkların sadakalarının neden kabul edilmediğini açıklar: {ar:وَمَا مَنَعَهُمْ أَن تُقْبَلَ مِنْهُمْ نَفَقَٰتُهُمْ, tr:ve mâ mene‘ahum en tukbele minhum nefekâtuhum, gloss:harcamalarının kabul edilmesine engel olan şey, source:9:54}. Sebeplerden ikisi bu surenin ikilisidir: {ar:وَلَا يَأْتُونَ ٱلصَّلَوٰةَ إِلَّا وَهُمْ كُسَالَىٰ وَلَا يُنفِقُونَ إِلَّا وَهُمْ كَٰرِهُونَ, tr:ve lâ ye'tûne's-salâte illâ ve hum küsâlâ, ve lâ yünfikûne illâ ve hum kârihûn, gloss:namaza ancak üşenerek gelirler, ancak isteksizce harcarlar, source:9:54}. Ankebût suresi namazın insanın içinde nasıl iş gördüğünü söyler: {ar:إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ, tr:inne's-salâte tenhâ ani'l-fahşâi ve'l-münker, gloss:namaz hayâsızlıktan ve kötülükten alıkoyar, source:29:45}. Meryem suresi de bırakılan namazı anlatır: {ar:أَضَاعُوا۟ ٱلصَّلَوٰةَ وَٱتَّبَعُوا۟ ٱلشَّهَوَٰتِ, tr:edâu's-salâte ve'ttebeu'ş-şehevât, gloss:namazı yitirdiler ve arzularının peşine düştüler, source:19:59}.

Kaynaklar: 107:4 لِّلْمُصَلِّينَ ص ل و B003; 107:4 لِّلْمُصَلِّينَ ص ل و B002; 107:5 صَلَاتِهِمْ ص ل و B003; 107:5 صَلَاتِهِمْ ص ل و B002; 107:3 ٱلْمِسْكِينِ س ك ن B004; 107:7 ٱلْمَاعُونَ م ع ن B005

## Buluşmalar

Görme imgesi ile gözden kaçma imgesi tek bir cümlede buluşur: Suhâ yıldızı {ar:خفي جدا فيسهى عن رؤيته, tr:hafiyyun ciddâ fe-yushâ an ru'yetih, gloss:pek gizlidir, onu görmekten gaflet edilir, source:"س ه و,B005"}. Surenin beşinci ayetindeki kökle altıncı ayetindeki kök bu cümlede yan yana durur. Gözden kaçırmak ile göze görünmek tek bir görme alanının iki ucudur. Adamlar sönük olanı, yani yetimi, yoksulu ve kendi namazlarındaki kalbi atlar. Kendilerinin ise atlanmamasını isterler. Alak suresindeki sahne bu buluşmaya namazı ve yarıda kalan yolu ekler. Bir "gördün mü" ile açılır, namaz kılan bir kulu engelleyeni gösterir, onun yalanlayıp yüz çevirdiğini söyler ve görenin Allah olduğunu hatırlatarak kapanır {source:96:9} {source:96:13} {source:96:14}. Burada bakış imgesi ile yalanın yüzey ve yol imgesi birbirinin içindedir. İnsanların gözü için kılınan namaz, gözü hiç ayrılmayan birinin önünde kılınmaktadır.

İtiş ile ateş Tûr suresinde tek harekette birleşir. Yetimi iten, ateşe itilir {source:52:13}, ve ona yalanladığı ateşin bu olduğu söylenir {source:52:14}. Böylece birinci ve ikinci ayetin iki fiili, yalanlamak ve itmek, dördüncü ayetin ateşini taşıyan kökle bir araya gelir. Hâkka suresinde ateş fiili ile teşvik etmeme aynı kişinin hesabında yan yana yazılır {source:69:31} {source:69:34}. Bu kez evin ocağı ile zayıfın üstündeki eller birbirine bağlanır. Teşvik edilmeyen yemek, pişirilmeyen ocağın karşılığında ateşe katlanmaya dönüşür.

Bütün imgeleri tek bir ağızdan dile getiren sahne Müddessir suresindedir. Cennet halkı suçlulara sorar: {ar:مَا سَلَكَكُمْ فِى سَقَرَ, tr:mâ selekekum fî sakar, gloss:sizi Sakar'a ne soktu, source:74:42}. Cevap bu surenin kelime dizisini ateşin içinden verir: {ar:قَالُوا۟ لَمْ نَكُ مِنَ ٱلْمُصَلِّينَ, tr:kâlû lem neku mine'l-musallîn, gloss:dediler ki: namaz kılanlardan değildik, source:74:43}, {ar:وَلَمْ نَكُ نُطْعِمُ ٱلْمِسْكِينَ, tr:ve lem neku nut‘imu'l-miskîn, gloss:yoksulu doyurmazdık, source:74:44}, {ar:وَكُنَّا نَخُوضُ مَعَ ٱلْخَآئِضِينَ, tr:ve künnâ nehûdu ma‘a'l-hâidîn, gloss:dalıp gidenlerle birlikte biz de dalardık, source:74:45}, {ar:وَكُنَّا نُكَذِّبُ بِيَوْمِ ٱلدِّينِ, tr:ve künnâ nükezzibu bi-yevmi'd-dîn, gloss:din gününü yalanlardık, source:74:46}. Namaz, doyurmak, gaflete dalmak ve hesabı yalanlamak burada tek bir itirafta toplanır ve bu itiraf ateşin içinden yapılır. Bu suredeki boş namaz, kapalı kap, gözden kaçırılan yoksul ve inkâr edilen hesap, orada bir hikâyenin sırası olarak geri döner.

Ev, su ve borç imgeleri tek bir kelimede, mâûnda buluşur. Aynı ad tencereyi ve kovayı {source:"م ع ن,B005"}, vadiden akan suyu {source:"م ع ن,B001"} ve itaatle zekâtı {source:"م ع ن,B005"} taşır. Rafta duran kap, yataktan akan su ve ödenmesi gereken pay tek bir şeyin üç görünüşüdür. Barındırma fiili de bu buluşmayı Kuran'da iki kez kurar. Yetim için {source:93:6}, Meryem oğlu ve annesi için kullanılır; ikincisinde barınak yerleşme ile akan suyun bir arada olduğu yerdir {source:23:50}. İtişin kökü de evle ellerin buluştuğu yerdir. Aynı harfler bir adamın küçük çocuklarını {source:"د ع ع,B009"}, sarsılarak doldurulan tabağı {source:"د ع ع,B002"} ve kapıdan kovan itişi {source:"د ع ع,B001"} taşır. Esirgemenin kökü de eli sıkı adamı {source:"م ن ع,B001"} ve babasız çocuğun yitirdiği koruyucu halkayı {source:"م ن ع,B003"} birlikte taşır.

Borç imgesi ile dışa dönük namaz imgesi Meâric suresinde birlikte sahnelenir. Esirgeyen insan, namazını sürdürenler, malındaki bilinen hak ve din gününü doğrulamak aynı dizide yer alır {source:70:21} {source:70:24} {source:70:26}. Tevbe suresindeki döngüde de pay, dua ve huzur birbirine bağlanır {source:9:103}. Bu sure, aynı halkaların çözülmüş hâlidir.

Surenin hareketi bu buluşmalarla taşınır. Sure bir bakış emriyle ve yalanlanan bir hesapla başlar. Bakışı önce bir evin kapısına götürür: Yetimi iten el, yoksulun yemeği için açılmayan ağız. Sonra namaz yerine geçer ve orada ateşi de taşıyan bir ada beddua düşer. Ardından seyircinin gözüne, en sonunda yeniden evin rafındaki küçük kaplara döner. Bir uçta "gördün mü" ile gösteriş vardır, yani bakış ve bakılmak. Öbür uçta din ile mâûn vardır, yani hesap ve küçük borç. İki uç da itaatte buluşur. Ortadaki ad, namaz kılanlar, hem halkayı kuracak ibadeti hem de halka kopunca gelen ateşi kökünde taşır.

