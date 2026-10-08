Focus: 91:7. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/91_7/D.r13/context.md =====
# 91:7 — focus

وَنَفْسٍۢ وَمَا سَوَّىٰهَا

Anchor translation (canonical reading, reference only):

Bir cana ve onu biçimlendirene,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَنَفْسٍ | نَفْس | ن ف س | CONJ;N |
| 2 | وَمَا | مَا |  | CONJ;REL |
| 3 | سَوَّىٰهَا | سَوَّىٰ | س و ي | V;PRON |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 91 — full text (context; no pericope)

- 91:1 وَٱلشَّمْسِ وَضُحَىٰهَا
- 91:2 وَٱلْقَمَرِ إِذَا تَلَىٰهَا
- 91:3 وَٱلنَّهَارِ إِذَا جَلَّىٰهَا
- 91:4 وَٱلَّيْلِ إِذَا يَغْشَىٰهَا
- 91:5 وَٱلسَّمَآءِ وَمَا بَنَىٰهَا
- 91:6 وَٱلْأَرْضِ وَمَا طَحَىٰهَا
- 91:7 ◀ focus وَنَفْسٍۢ وَمَا سَوَّىٰهَا
- 91:8 فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا
- 91:9 قَدْ أَفْلَحَ مَن زَكَّىٰهَا
- 91:10 وَقَدْ خَابَ مَن دَسَّىٰهَا
- 91:11 كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ
- 91:12 إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
- 91:13 فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا
- 91:14 فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا
- 91:15 وَلَا يَخَافُ عُقْبَٰهَا


===== _commentary/v16/work/91_7/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ن ف س (root_001533) — identity root of وَنَفْسٍ (w1)

- **B001** soluk alıp verme — soluk alıp verme · gövdeye girip çıkan hava; soluk · tek soluk ya da soluklanma arası · soluklar
  التنفس خروج النسيم من الجوف (maqayis;ayn); النفس واحد الأنفاس وكل ذي رئة متنفس (sihah); التنفس في الإناء وثلاثة أنفاس (tahdhib); النفس الريح الداخل والخارج في البدن من الفم والمنخر (mufradat)
- **B002** sıkıntıyı hafifletip ferahlatma — Tanrı onun sıkıntısını giderdi · beni sıkıntıdan kurtarıp rahatlat · Tanrı'nın sıkıntıdakilere ferahlık getiren esintisi ya da yardımı
  نفس الله كربته والنفس كل شيء يفرج به عن مكروب (maqayis); نفست عنه تنفيسا أي رفهت (sihah); اللهم نفس عني أي فرج عني والريح من نفس الرحمن (tahdhib;mufradat)
- **B003** kem gözle zarar verme — zarar verdiğine inanılan bakış · ona kem göz değdi · kem gözle zarar veren kişi
  يقال للعين نفس وأصابت فلانا نفس (maqayis); النفس العين ونفسته بنفس إذا أصبته بعين والنافس العائن (sihah); النفس العين التي تصيب المعين وإن فلانا لنفوس أي عيون (tahdhib)
- **B004** canlıdaki akışkan kan — kaybıyla yaşamın da yitirildiği kan · hayvandaki akışkan kan
  النفس الدم وإذا فقد الدم فقد نفسه (maqayis); النفس الدم وما ليس له نفس سائلة (sihah); النفس الدم وكل شيء له نفس سائلة أراد دما سائلا (tahdhib)
- **B005** doğum ve doğuma bağlı kadın-çocuk durumu — doğum yapmış ya da doğum sonrası kanaması olan kadın · doğum ve doğum sonrası kanama dönemi · yeni doğan çocuk · doğmadan önce
  الحائض تسمى النفساء والنفاس ولاد المرأة والولد منفوس (maqayis); النفاس ولادة المرأة فإذا وضعت كانت نفساء (ayn;mufradat); نفست المرأة غلاما والولد منفوس وورث قبل أن ينفس أي يولد (sihah); نفست المرأة إذا حاضت وأنفست أراد أحضت (tahdhib)
- **B006** soluk aralı içim ve bir içimlik yudum — bir solukta alınan yudum ya da içim · üç soluk arasıyla içme
  كرع في الإناء نفسا أو نفسين (maqayis); شربت الماء بنفس وثلاثة أنفاس وكل مستراح منه نفس (ayn); النفس الجرعة اكرع في الإناء نفسا أو نفسين (sihah); يشرب الماء وغيره بثلاث أنفاس (tahdhib)
- **B007** bir deri işlemeye yetecek sepi maddesi payı — deriyi bir kez işlemeye yetecek sepi maddesi · bir işlemelik sepi maddesi payı
  في الدباغ نفس قدر ما يدبغ به الإهاب مرة (maqayis); النفس قدر دبغة مما يدبغ به الأديم (sihah); النفس قدر دبغة أو دبغتين من الدباغ (tahdhib)
- **B008** yaşamı sürdüren, bol ve doyurucu su — yaşamı ayakta tutan su · bol ve susuzluğu gideren içecek · tadı kötü, bayat ve içimi güç içecek
  يقال للماء نفس ولأن قوام النفس به (maqayis); النفس الماء وشراب ذو نفس أي فيه سعة وري وشراب غير ذي نفس (tahdhib)
- **B009** kalıba bağlı yarılıp açılma ve genişleme [kalıp] — yay çatladı ya da yarıldı · sabah söktü, aydınlık yayıldı · gündüz uzayıp genişledi · ırmağın suyu artıp yayıldı
  تنفست القوس انشقت (maqayis); تنفس الصبح أي تبلج وتنفس النهار إذا زاد والموج إذا نضح الماء (sihah); إذا انشق الفجر وانفلق وتنفس دجلة إذا زاد ماؤها (tahdhib); تنفس النهار عبارة عن توسعه (mufradat)
- **B010** değerli ve uğrunda yarışılan şey — değerli, önemli ve arzulanan · bir şeyi elde etme ya da üstünlere benzeme yarışı · başkasına vermeye kıyamayıp esirgemek · sahip olduğu şey yüzünden onu kıskanmak
  شيء نفيس ذو نفس وخطر يتنافس به والتنافس يبرز كل واحد قوة نفسه (maqayis); شيء نفيس متنافس فيه ونفست به ضننت (ayn); نافست في الشيء إذا رغبت فيه وتنافسوا فيه ونفس به أي ضن أو حسد (sihah); مال نفيس ومنفس وكل شيء له خطر وقدر ونفس عليك أي حسدك (tahdhib); المنافسة مجاهدة النفس للتشبه بالأفاضل ونفست بكذا ضنت نفسي به وشيء نفيس (mufradat)
- **B011** bedene yaşam veren can — bedene yaşam veren can · insan ya da canlı birey
  النفس الروح الذي به حياة الجسد وكل إنسان نفس (ayn); النفس الروح يقال خرجت نفسه (sihah); خرجت نفس فلان أي روحه ونفس الحياة هي الروح (tahdhib); النفس الروح في قوله أخرجوا أنفسكم (mufradat)
- **B012** şeyin kendisi ve bütün öz varlığı [kalıp] — şeyin tam kendisi ve gerçeği · başkası aracılığıyla değil, bizzat kendisi
  كل شيء بعينه نفس (ayn); نفس الشيء عينه يؤكد به (sihah); معنى النفس حقيقة الشيء وجملته وذاته كلها وعين الشيء وكنهه وجوهره (tahdhib); نفسه ذاته (mufradat)
- **B013** iç düşünce, niyet ve ayırt etme gücü — onun içinden geçen düşünce ya da niyet · ayırt etmeyi sağlayan zihinsel güç
  نفس العقل التي يكون بها التمييز وفي نفس فلان أن يفعل أي في روعه وتعلم ما في نفسي أي ما عندي أو غيبك (tahdhib); يعلم ما في أنفسكم وتعلم ما في نفسي ولا أعلم ما في نفسك (mufradat)
- **B014** sağlam, cömert ve onurlu yaradılış — sağlam karakterli, dayanıklı ve cömert adam · büyüklük duygusu, onur, yüksek amaç ve kendine saygı
  رجل له نفس أي خلق وجلادة وسخاء (ayn); النفس العظمة والكبر والعزة والهمة والأنفة (tahdhib)
- **B015** uzaklık, genişlik ve zaman payı — işinde rahat hareket edecek genişlikte · ek süre ya da hareket alanı · daha uzak, daha uzun ya da daha geniş
  هذا المكان أنفس من ذاك أي أبعد شيئا (ayn); أنت في نفس من أمرك أي في سعة ولك في هذا الأمر نفسة أي مهلة (sihah); هذا المنزل أنفس أي أبعد وكتبت كتابا نفسا أي طويلا وزد في أجلي نفسا وبين الفريقين نفس أي متسع (tahdhib)
- **B016** eski bahis oyunundaki beşinci pay oku — eski bahis oyunundaki beşinci pay oku; bir aktarıma göre dördüncü ok
  النافس الخامس من القداح (ayn); النافس الخامس من سهام الميسر ويقال هو الرابع (sihah); النافس الخامس من قداح الميسر وفيه خمسة فروض (tahdhib)

## س و ي (root_000766) — identity root of سَوَّىٰهَا (w3)

- **B001** iki şeyi birbirine denk kılma veya denk sayma — bir şeyi ötekinin ölçüsüne ulaştırarak eşitlemek · iki şeyi ölçü, ağırlık, nicelik ya da nitelik bakımından eşitleme · bir işte aynı düzeyde ve eşit durumda · eş, benzer · ikisi de bir, ikisi eşit · özellikle, hele
  أصل يدل على استقامة واعتدال بين شيئين (maqayis)؛ لا يساوي كذا أي لا يعادله (maqayis;sihah;tahdhib)؛ المساواة والاستواء واحد (ayn)؛ السِيّ المثل من قولهم سِيّان أي مثلان (jamhara;maqayis;mufradat)؛ لا سِيّما أي لا مثل ما (maqayis)؛ هذا الثوب يساوي كذا (mufradat)
- **B002** kendi içinde düzgün ve tam duruma gelme — bir şeyi düzeltip düzgün ya da eksiksiz duruma getirmek · eğrilikten kurtulup doğrulmak · yapısı düzgün, eksiksiz ve sağlıklı · çocuklarımız ve hayvanlarımız iyi durumda · düz arazi
  سويت الشيء فاستوى (ayn;sihah)؛ استوى من اعوجاج (sihah;tahdhib)؛ السوي الذي سوى الله خلقه لا دمامة فيه ولا داء (ayn)؛ السوي فعيل في معنى مفتعل أي مستو (tahdhib)؛ السوي يقال فيما يصان عن الإفراط والتفريط (mufradat)؛ أولادنا وماشيتنا سوية صالحة (maqayis;tahdhib)
- **B003** üzerine çıkıp yerleşmek veya egemen olmak [kalıp] — bineğinin sırtına çıkıp yerleşmek · üzerine çıkmak ya da egemen olmak
  استوى على ظهر دابته أي علا واستقر (sihah)؛ استويت فوق الدابة وعلى ظهر الدابة أي علوته (tahdhib)؛ استوى أي استولى وظهر (sihah)؛ متى عدي بعلى اقتضى معنى الاستيلاء (mufradat)
- **B004** bir hedefe yönelip onu amaç edinmek [kalıp] — göğe yönelmek, ona varmak ya da ona yönelik işi düzenlemek
  استوى إلى السماء أي قصد (sihah)؛ استوى علي وإلي يشاتمني على معنى أقبل إلي وعلي (tahdhib)؛ ثم استوى إلى بلد معناه قصد بالاستواء إليه (tahdhib)؛ إذا عدي بإلى اقتضى معنى الانتهاء إليه إما بالذات أو بالتدبير (mufradat)
- **B005** gençlik olgunluğuna erişmek — gençliğinin sonuna erişip gücü ve kavrayışı olgunlaşmak
  استوى الرجل إذا انتهى شبابه (sihah)؛ بلغ أشده واستوى قيل بلغ الأربعين (tahdhib)؛ المستوي هو الذي تم شبابه (tahdhib)؛ فإذا استويت أنت (mufradat)
- **B006** iki yanın ortasında ve ikisine karşı yansız olma — orta; iki yana eşit ve yansız durum · iki yana eşit, ortada ve herkesçe bilinen yer · iki tarafın da hakkını gözeten ortak söz
  السواء ممدود وسط كل شيء (ayn)؛ مكانا سوى أي معلما قد علم القوم به (ayn;maqayis)؛ مكان سوى أي عدل ووسط (sihah)؛ السواء وسط الدار وغيرها (maqayis)؛ سواء بمعنى العدل والنصفة (tahdhib)؛ كلمة سواء أي عدل (tahdhib;mufradat)؛ في سواء الجحيم (maqayis;mufradat)
- **B007** başka ve ayrı olan — başka, öteki
  سوى مقصور إذا كان في موضع غير (ayn)؛ سواء الشيء غيره (sihah;tahdhib)؛ مررت برجل سواك أي غيرك (sihah)؛ هذا سوى ذلك أي غيره (maqayis)؛ يستعمل سوى وسواء بمعنى غير (mufradat)؛ عندي رجل سواك أي مكانك وبدلك (mufradat)
- **B008** birinin yöneldiği hedefe yönelmek [kalıp] — birinin tuttuğu yöne ya da hedefe yönelmek
  يقال قصدت سوى فلان كما يقال قصدت قصده (maqayis)؛ قصدت سوى فلان أي قصدت قصده (sihah)؛ فلأصرفن سوى حذيفة مدحتى (maqayis;sihah)؛ وقع المزار على سواهما أخطأهما (tahdhib)
- **B009** geniş ve açık arazi — geniş, açık ya da pürüzsüz arazi
  السِيّ الفضاء من الأرض الواسع (jamhara)؛ ومن الباب السِيّ الفضاء من الأرض (maqayis)؛ السِيّ موضع بالبادية أملس (ayn)؛ نزلنا في كلاء سِيّ وأنبط ماء سِيًّا أي كثيرا واسعا (tahdhib)
- **B010** devenin sırtına konan dolgulu binme örtüsü — devenin sırtına ya da hörgücü çevresine konan binme örtüsü
  السَّويّة قتب أعجمي للبعير والجميع السوايا (ayn;tahdhib)؛ السَّويّة كساء يلف ويجعل شبيها بالحوية يلقى على سنام البعير (jamhara)؛ السَّويّة كساء محشو بثمام ونحوه كالبرذعة (sihah)؛ كساء محشو بثمام أو ليف يجعل على ظهر البعير (tahdhib)
- **B011** atlayıp dışarıda bırakmak — atlamak, dışarıda bırakmak ve göz ardı etmek
  أسوى فلان حرفا من كتاب الله أي أسقط وأغفل (ayn)؛ أسويت الشيء أي تركته وأغفلته (sihah)؛ أسوى برزخا ثم رجع إليه (tahdhib)؛ أسوى يعني أسقط وأغفل (tahdhib)
- **B012** ayın on üçüncü gecesi — ayın dengeli göründüğü on üçüncü gece
  ليلة السواء ليلة ثلاث عشرة (sihah)؛ السواء ممدود ليلة ثلاث عشرة وفيها يستوي القمر (tahdhib)
- **B013** başına denk mal ve bolluk [kalıp] — başına denk sayılan mal miktarı ya da bolluk
  جاء فلان بسِيّ رأسه من المال أي ما يوازي رأسه (jamhara)؛ وقع فلان في سواء رأسه أي فيما ساوى رأسه من النعمة (tahdhib)؛ هو في سِيّ رأسه وسواء رأسه وهي النعمة (tahdhib)

===== _commentary/v16/out/s091/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 91:7, and ## Buluşmalar) =====
## Gökte el değiştiren ışık: açılan ve örtülen yüz

Arapçada kelimelerin çoğu üç harfli bir kökten türer. Aynı kökten gelen kelimeler birbirinden çok farklı şeylere ad olabilir, ama aralarında ortak bir sahne taşırlar. Aşağıda bir kelimenin ailesinden getirilen her imge, o kelimenin ayetteki anlamının yanında duyulur. İmge bu anlamın yerine geçmez.

Surenin ilk dört ayeti dört ayrı şeye yemin ediyor gibi görünür: güneş, ay, gündüz, gece. Oysa dört ayetin de sonundaki "-hâ" zamiri hep aynı yere döner, yani güneşe. Birinci ayet güneşi kendi ışığıyla anar: {ar:وَٱلشَّمْسِ وَضُحَىٰهَا, tr:ve'ş-şemsi ve duhâhâ, gloss:güneşe ve kuşluğuna andolsun, source:91:1}. Güneş hem bir disktir hem de o diskten yayılan aydınlık: {ar:الشمس يقال للقرصة وللضوء المنتشر عنها, tr:eş-şemsu yukâlu li'l-kursati ve li'd-dav'i'l-munteşiri anhâ, gloss:güneş hem diske hem de ondan yayılan ışığa denir, source:"ش م س,B001"}. Kuşluk da o ışığın açılıp yayılmasıdır: {ar:الضحى انبساط الشمس وامتداد النهار, tr:ed-duhâ inbisâtu'ş-şemsi ve'mtidâdu'n-nehâr, gloss:kuşluk, güneşin yayılması ve gündüzün uzamasıdır, source:"ض ح و,B001"}. Bu yayılma ölçülü basamaklarla sayılır: {ar:ضحوة النهار بعد طلوع الشمس ثم بعده الضحى ثم بعده الضحاء, tr:dahvetu'n-nehâri ba'de tulû'i'ş-şems, summe ba'dehu'd-duhâ, summe ba'dehu'd-dahâ', gloss:güneş doğduktan sonra önce dahve, sonra duhâ, sonra dahâ gelir, source:"ض ح و,B001"}. Kısacası ilk ayette güneş kendi aydınlığını yayan bir kaynak olarak durur.

İkinci ayet ayı kendi ışığıyla değil, sırasıyla tanımlar: {ar:وَٱلْقَمَرِ إِذَا تَلَىٰهَا, tr:ve'l-kameri izâ telâhâ, gloss:onu izlediğinde aya andolsun, source:91:2}. Fiil bir peşinden gelmeyi anlatır: {ar:تلاه تبعه متابعة, tr:telâhu tebi'ahu mutâba'aten, gloss:onu izledi, ardı sıra peşinden gitti, source:"ت ل و,B001"}. Üçüncü ayette ilişki ters döner: {ar:وَٱلنَّهَارِ إِذَا جَلَّىٰهَا, tr:ve'n-nehâri izâ cellâhâ, gloss:onu açığa çıkardığında gündüze andolsun, source:91:3}. Gündüz, güneşin ışığından başka bir şey değildir: {ar:النهار ضياء ما بين طلوع الفجر إلى غروب الشمس, tr:en-nehâru diyâun mâ beyne tulû'i'l-fecri ilâ gurûbi'ş-şems, gloss:gündüz, tan yerinin ağarmasından güneşin batışına kadarki aydınlıktır, source:"ن ه ر,B002"}. Yine de güneşi görünür kılan, güneşten gelen bu aydınlıktır. Fiilin kökü örtünün kalkıp şeyin ortaya çıkmasını anlatır: {ar:انكشاف الشيء وبروزه, tr:inkişâfu'ş-şey'i ve burûzuhu, gloss:bir şeyin örtüsünün açılması ve ortaya çıkması, source:"ج ل و,B001"}. Arap dili bu ayeti de tam böyle okur: {ar:والنهار إذا جلاها إذا بين الشمس, tr:ve'n-nehâri izâ cellâhâ: izâ beyyene'ş-şemse, gloss:"gündüz onu açığa çıkardığında", yani güneşi belirgin kıldığında, source:"ج ل و,B007"}. Dördüncü ayette gece aynı yüzü kapatır: {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰهَا, tr:ve'l-leyli izâ yağşâhâ, gloss:onu örttüğünde geceye andolsun, source:91:4}. Kökün işi bir şeyi başka bir şeyle kaplamaktır: {ar:أصل صحيح يدل على تغطية شيء بشيء, tr:aslun sahîhun yedullu alâ tağtiyeti şey'in bi-şey', gloss:bir şeyin başka bir şeyle örtülmesini gösteren sağlam bir kök, source:"غ ش و,B001"}.

Düz bir anlatım "güneşe, aya, gündüze ve geceye andolsun" der ve geçer. Fiiller ise tek bir yüzün dört türlü ele alındığını gösterir: yayılır, izlenir, açılır, örtülür. Kur'an bu düzeni başka yerlerde de sahneler. Yâsîn Suresi'nde Allah işaretlerini sayarken hiçbir cismin sırasını bozmadığını söyler: {ar:لَا ٱلشَّمْسُ يَنۢبَغِى لَهَآ أَن تُدْرِكَ ٱلْقَمَرَ وَلَا ٱلَّيْلُ سَابِقُ ٱلنَّهَارِ, tr:le'ş-şemsu yenbağî lehâ en tudrike'l-kamera ve le'l-leylu sâbiku'n-nehâr, gloss:ne güneşin aya yetişmesi yaraşır ne de gece gündüzü geçebilir, source:36:40}. Göklerle yeri altı günde yaratan Rabbi anlatan ayette örtme işi bir kovalamacaya dönüşür: {ar:يُغْشِى ٱلَّيْلَ ٱلنَّهَارَ يَطْلُبُهُۥ حَثِيثًۭا, tr:yuğşi'l-leyle'n-nehâra yatlubuhu hasîsâ, gloss:geceyi, onu hızla kovalayan gündüzün üstüne örter, source:7:54}. Hemen ardından gelen sure aynı çifti iki yeminle açar: {ar:وَٱلَّيْلِ إِذَا يَغْشَىٰ, tr:ve'l-leyli izâ yağşâ, gloss:örttüğünde geceye andolsun, source:92:1} ve {ar:وَٱلنَّهَارِ إِذَا تَجَلَّىٰ, tr:ve'n-nehâri izâ tecellâ, gloss:açılıp parladığında gündüze andolsun, source:92:2}. Nâziât Suresi'nde Allah, dirilişi inkâr edenlere yaratılmalarının mı daha zor olduğunu, yoksa göğün mü olduğunu sorar. Orada kuşluk, gecenin içinden çıkarılan bir şey gibi anlatılır: {ar:وَأَغْطَشَ لَيْلَهَا وَأَخْرَجَ ضُحَىٰهَا, tr:ve ağtaşe leylehâ ve ahrace duhâhâ, gloss:gecesini karanlık kıldı, kuşluğunu çıkardı, source:79:29}.

Bu gök sahnesi dördüncü ayette bitmez. Surenin sonraki kelimeleri aynı gökten anlamlar taşır. Yedinci ayetteki "nefs" kelimesinin kökü sabahın nefes almasını da adlandırır: {ar:تنفس الصبح أي تبلج وتنفس النهار إذا زاد, tr:teneffese's-subhu ey teballece, ve teneffese'n-nehâru izâ zâde, gloss:sabah nefes aldı, yani ağardı; gündüz nefes aldı, yani uzadı, source:"ن ف س,B009"}. Kur'an aynı fiili bir yeminde kullanır: {ar:وَٱلصُّبْحِ إِذَا تَنَفَّسَ, tr:ve's-subhi izâ teneffes, gloss:nefes aldığında sabaha andolsun, source:81:18}. Yine yedinci ayetteki "sevvâhâ" fiilinin ailesinde ayın tamamlandığı gece vardır: {ar:السواء ممدود ليلة ثلاث عشرة وفيها يستوي القمر, tr:es-sevâ'u memdûdun, leyletu selâse aşrate ve fîhâ yestevi'l-kamer, gloss:sevâ', ayın on üçüncü gecesidir; o gece ay dolgunlaşır, source:"س و ي,B012"}. Kur'an da dolunaya yemin eder: {ar:وَٱلْقَمَرِ إِذَا ٱتَّسَقَ, tr:ve'l-kameri izâ't-tesak, gloss:dolunay olduğunda aya andolsun, source:84:18}. Altıncı ayetteki "tahâhâ" fiili de yükselmiş, ışığı yayılmış ayı adlandırır: {ar:القمر الطاحي أي المرتفع والطاحي أيضا المنبسط, tr:el-kameru't-tâhî, eyi'l-murtefi', ve't-tâhî eyzan el-munbesit, gloss:tâhî ay, yükselmiş ay demektir; tâhî yayılmış anlamına da gelir, source:"ط ح و,B008"}. Sekizinci ayetteki "fucûr" kelimesinin kökü şafağın adıdır: {ar:الفجر حمرة الشمس في سواد الليل وهما فجران, tr:el-fecru humretu'ş-şemsi fî sevâdi'l-leyl, ve humâ fecrân, gloss:fecr, gecenin karasındaki güneş kızıllığıdır; iki fecr vardır, source:"ف ج ر,B002"}. Şafak bu adı geceyi yardığı için alır: {ar:قيل للصبح فجر لكونه فجر الليل, tr:kîle li's-subhi fecrun li-kevnihî fecera'l-leyl, gloss:sabaha fecr denmesi, geceyi yarmış olmasındandır, source:"ف ج ر,B002"}. Kur'an Allah'ı bu yarışın sahibi olarak anar: {ar:فَالِقُ ٱلْإِصْبَاحِ, tr:fâliku'l-isbâh, gloss:sabahı yarıp çıkaran, source:6:96}. On beşinci ayetteki "ukbâhâ" kelimesinin ailesinde ise gece ile gündüzün nöbetleşmesi vardır: {ar:الليل والنهار يتعاقبان, tr:el-leylu ve'n-nehâru yeteâkabân, gloss:gece ile gündüz birbirini izler, source:"ع ق ب,B005"}. Kur'an bu nöbeti şöyle anlatır: {ar:جَعَلَ ٱلَّيْلَ وَٱلنَّهَارَ خِلْفَةًۭ, tr:ce'ale'l-leyle ve'n-nehâra hilfeten, gloss:geceyi ve gündüzü birbirinin ardınca gelen kıldı, source:25:62}. Böylece sure, gökte başlayan nöbetin sözcükleri içinde ilerler ve yine bir "ardınca gelme" kelimesiyle kapanır.

Açma ve örtme işi gökte kalmaz. Kuşluk kelimesinin kendisi de açıkta durmayı anlatır: {ar:ضحا الطريق إذا بدا وظهر, tr:dahâ't-tarîku izâ bedâ ve zahara, gloss:yol göründüğünde ve ortaya çıktığında "dahâ" denir, source:"ض ح و,B002"}; {ar:فعل ذلك ضاحية أي ظاهرا بينا, tr:fe'ale zâlike dâhiyeten, ey zâhiren beyyinen, gloss:bunu dâhiye olarak yaptı, yani açıkça, göz önünde yaptı, source:"ض ح و,B002"}. Gecenin örtüsü de kalbe taşınır: {ar:الغشاوة ما غشي القلب من رين الطبع, tr:el-ğışâvetu mâ ğaşiye'l-kalbe min rayni't-tab', gloss:ğışâve, kalbi kaplayan mühür pasıdır, source:"غ ش و,B001"}. Kur'an inkârcılar için aynı kelimeyi kullanır: {ar:وَعَلَىٰٓ أَبْصَٰرِهِمْ غِشَٰوَةٌۭ, tr:ve alâ ebsârihim ğışâvetun, gloss:gözlerinin üstünde bir perde vardır, source:2:7}.

Sekizinci ayette bu iki iş nefsin içine yerleşir: {ar:فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا, tr:fe-elhemehâ fucûrahâ ve takvâhâ, gloss:ona hem yoldan çıkışını hem korunuşunu ilham etti, source:91:8}. Fucûr, şafağın geceyi yardığı kökten gelir. Ama burada yarılan şey karanlık değil, bir perdedir: {ar:الفجور شق ستر الديانة, tr:el-fucûru şakku sitri'd-diyâne, gloss:fucûr, din perdesini yırtmaktır, source:"ف ج ر,B004"}. Gökte yarılma ışık getirir; nefiste ise koruyucu örtüyü parçalar. Takvâ bunun karşısında yerinde tutulan bir örtüdür: {ar:كل ما وقى شيئا فهو وقاء له ووقاية, tr:kullu mâ vakâ şey'en fe-huve vikâun lehu ve vikâye, gloss:bir şeyi koruyan her şey onun için vikâ ve vikâyedir, source:"و ق ي,B001"}. Kökün en somut örneği, dış örtü ile saç arasında duran ince bezdir: {ar:وقاية المرأة وهي الخرقة التي بين جلبابها وشعرها, tr:vikâyetu'l-mer'e, ve hiye'l-hırkatu'lletî beyne cilbâbihâ ve şa'rihâ, gloss:kadının vikâyesi, cilbabı ile saçı arasındaki bez parçasıdır, source:"و ق ي,B001"}. Böylece surede iki tür örtü ve iki tür açılış belirir. Gecenin örtüsü düzenin parçasıdır, takvânın örtüsü korur. Gündüzün açması gösterir, fucûrun açması yırtar.

Dokuzuncu ve onuncu ayetler bu çifti nefsin kaderine bağlar: {ar:قَدْ أَفْلَحَ مَن زَكَّىٰهَا, tr:kad efleha men zekkâhâ, gloss:onu arındırıp büyüten kurtuluşa ermiştir, source:91:9}; {ar:وَقَدْ خَابَ مَن دَسَّىٰهَا, tr:ve kad hâbe men dessâhâ, gloss:onu gömüp gizleyen eli boş kalmıştır, source:91:10}. İkinci fiil gizlemektir: {ar:دساها أي أخفاها, tr:dessâhâ, ey ahfâhâ, gloss:dessâhâ, onu gizledi demektir, source:"د س و,B001"}. Gizleme burada kişinin kendine yöneliktir: {ar:دس فلان نفسه إذا أخفاها وأخملها, tr:dessâ fulânun nefsehu izâ ahfâhâ ve ahmelehâ, gloss:biri kendini gizleyip adını sönük bıraktığında bu fiil kullanılır, source:"د س و,B001"}. Fiil açıkça büyütmenin karşıtı olarak tanımlanır: {ar:وهو نقيض زكا يزكو زكاء وزكاة وهو داس لا زاك, tr:ve huve nakîdu zekâ yezkû zekâen ve zekâten, ve huve dâsin lâ zâk, gloss:bu, "zekâ" fiilinin zıddıdır; o kişi büyüyen değil, gizlenendir, source:"د س و,B002"}. Arap dilinde bu fiil, harflerden biri dönüşmüş bir "dessese" olarak da açıklanır: {ar:دسّسها, tr:dessesehâ, gloss:onu gömdü, toprağa itip gizledi, source:"memory"}. Bu, iki kökün aynı olduğunu göstermez. Yalnızca bir türeyiş yolunu gösterir. Kur'an, iki harfli bu ikinci kökün fiilini bir saklanma sahnesinde kullanır. Allah, kendisine kız çocuğu müjdelenen ve yüzü kararan bir babayı anlatır. Bu adam halktan gizlenir, {ar:يَتَوَٰرَىٰ مِنَ ٱلْقَوْمِ, tr:yetevârâ mine'l-kavm, gloss:halktan saklanır, source:16:59}, ve kendine sorar: {ar:أَمْ يَدُسُّهُۥ فِى ٱلتُّرَابِ, tr:em yedussuhû fi't-turâb, gloss:yoksa onu toprağa mı gömsün, source:16:59}. Kişinin kendini saklaması ile başkasını toprağa itmesi orada tek bir sahnede birleşir. Onuncu ayetteki nefis de böylece güneşin tersine götürülür: açıktan kuytuya, görünürden gömülüye.

Semûd'a gelince açılan şey bir işaret, kapanan şey de bir azaptır. Allah, Semûd'a verdiği dişi deveyi gözleri açan bir işaret olarak anar: {ar:وَءَاتَيْنَا ثَمُودَ ٱلنَّاقَةَ مُبْصِرَةًۭ, tr:ve âteynâ Semûde'n-nâkate mubsıraten, gloss:Semûd'a göz açan bir işaret olarak dişi deveyi verdik, source:17:59}. Onlar ise gündüzün değil gecenin tarafını seçtiler: {ar:فَٱسْتَحَبُّوا۟ ٱلْعَمَىٰ عَلَى ٱلْهُدَىٰ, tr:fe'stehabbu'l-amâ ale'l-hudâ, gloss:körlüğü doğru yola tercih ettiler, source:41:17}. Gecenin fiili bir halkın üstüne serilen cezanın da fiilidir: {ar:غاشية من عذاب الله أي عقوبة مجللة تعمهم, tr:ğâşiyetun min azâbi'llâh, ey ukûbetun mucellilatun teummuhum, gloss:Allah'ın azabından bir ğâşiye, yani onları baştan başa kaplayıp hepsini saran bir ceza, source:"غ ش و,B002"}. Kur'an kendini güvende sananlara aynı kelimeyle seslenir: {ar:أَن تَأْتِيَهُمْ غَٰشِيَةٌۭ مِّنْ عَذَابِ ٱللَّهِ, tr:en te'tiyehum ğâşiyetun min azâbi'llâh, gloss:Allah'ın azabından onları kaplayacak bir şeyin gelmesinden, source:12:107}. Necm Suresi'nde Allah helak ettiği toplulukları sayar: {ar:وَثَمُودَا۟ فَمَآ أَبْقَىٰ, tr:ve Semûde fe-mâ ebkâ, gloss:Semûd'u da geride hiçbir şey bırakmadı, source:53:51}. Aynı dizinin sonunda tersyüz edilmiş şehir için yine örtme fiili gelir: {ar:فَغَشَّىٰهَا مَا غَشَّىٰ, tr:fe-ğaşşâhâ mâ ğaşşâ, gloss:onu örten örttü, source:53:54}. On dördüncü ayetteki "demdeme aleyhim" sözü dilde yok etmeyi anlatır: {ar:الدَّمْدَمَة: الاستئصال, tr:ed-demdeme: el-isti'sâl, gloss:demdeme, kökünden kazımaktır, source:"د م د م,B001"}. Arap dili aynı fiili "üstlerine kapattı" diye de açıklar: {ar:أطبق عليهم, tr:etbaka aleyhim, gloss:üstlerine kapandı, source:"memory"}. Suçun fiili bile örtü taşır. Devenin ayaklarını kesmek anlamındaki "akr" kelimesi, güneşin gözünü örten bir bulutun da adıdır: {ar:العقر غيم ينشأ من قبل العين فيغشى عين الشمس, tr:el-ukru ğaymun yenşe'u min kıbeli'l-ayn, fe-yağşâ ayne'ş-şems, gloss:ukr, ufkun bir yönünden yükselip güneşin gözünü örten buluttur, source:"ع ق ر,B018"}.

Kaynaklar: 91:1 ٱلشَّمْسِ ش م س B001; 91:1 ضُحَىٰهَا ض ح و B001; 91:1 ضُحَىٰهَا ض ح و B002; 91:2 تَلَىٰهَا ت ل و B001; 91:3 ٱلنَّهَارِ ن ه ر B002; 91:3 جَلَّىٰهَا ج ل و B001; 91:3 جَلَّىٰهَا ج ل و B007; 91:4 يَغْشَىٰهَا غ ش و B001; 91:4 يَغْشَىٰهَا غ ش و B002; 91:6 طَحَىٰهَا ط ح و B008; 91:7 نَفْسٍۢ ن ف س B009; 91:7 سَوَّىٰهَا س و ي B012; 91:8 فُجُورَهَا ف ج ر B002; 91:8 فُجُورَهَا ف ج ر B004; 91:8 تَقْوَىٰهَا و ق ي B001; 91:10 دَسَّىٰهَا د س و B001; 91:10 دَسَّىٰهَا د س و B002; 91:14 فَدَمْدَمَ د م د م B001; 91:14 فَعَقَرُوهَا ع ق ر B018; 91:15 عُقْبَٰهَا ع ق ب B005

## Gök ve yerden kurulan ev, içindeki üçüncü yapı: nefis

Beşinci, altıncı ve yedinci ayetler tek bir inşa işini üç fiille anlatır: {ar:وَٱلسَّمَآءِ وَمَا بَنَىٰهَا, tr:ve's-semâi ve mâ benâhâ, gloss:göğe ve onu kurana andolsun, source:91:5}; {ar:وَٱلْأَرْضِ وَمَا طَحَىٰهَا, tr:ve'l-ardı ve mâ tahâhâ, gloss:yere ve onu yayana andolsun, source:91:6}; {ar:وَنَفْسٍۢ وَمَا سَوَّىٰهَا, tr:ve nefsin ve mâ sevvâhâ, gloss:nefse ve onu düzenleyip dengeleyene andolsun, source:91:7}.

İlk fiil parçaları birbirine katarak bir bütün kurmaktır: {ar:بناء الشيء بضم بعضه إلى بعض, tr:binâu'ş-şey'i bi-dammi ba'dihî ilâ ba'd, gloss:bir şeyi kurmak, parçalarını birbirine katmaktır, source:"ب ن ي,B001"}. Kurulan gök, evin tavanıdır: {ar:السماء سقف البيت وكل عال مطل سماء, tr:es-semâu sakfu'l-beyt, ve kullu âlin mutıllin semâ', gloss:semâ evin tavanıdır; yukarıda duran ve üstte sarkan her şey semâdır, source:"س م و,B004"}. Bir başka tanım da onun gölge veren yanını öne çıkarır: {ar:السماء كل ما علاك فأظلك, tr:es-semâu kullu mâ alâke fe-ezallek, gloss:semâ, üstüne yükselip seni gölgeleyen her şeydir, source:"س م و,B004"}. Kur'an göğe aynı adı verir: {ar:وَجَعَلْنَا ٱلسَّمَآءَ سَقْفًۭا مَّحْفُوظًۭا, tr:ve ce'alne's-semâe sakfen mahfûzâ, gloss:göğü korunmuş bir tavan yaptık, source:21:32}. Bir yeminde de onu böyle anar: {ar:وَٱلسَّقْفِ ٱلْمَرْفُوعِ, tr:ve's-sakfi'l-merfû', gloss:yükseltilmiş tavana andolsun, source:52:5}. Bina kökü yalnızca taş duvarı değil, deriden kurulan çadırı da adlandırır: {ar:المبناة قبة من أدم, tr:el-mebnâtu kubbetun min edem, gloss:mebnât, deriden yapılmış kubbeli çadırdır, source:"ب ن ي,B004"}. Aynı kök yere serilen bir deri sergiyi de anlatır: {ar:بسطنا له بناء أي نطعا, tr:basatnâ lehu binâen, ey nat'an, gloss:ona bir binâ serdik, yani deri bir sergi, source:"ب ن ي,B004"}.

Altıncı ayetteki yer, bu tavanın karşısındaki yüzdür: {ar:الأرض الجرم المقابل للسماء, tr:el-ardu'l-cirmu'l-mukâbilu li's-semâ', gloss:yer, göğün karşısındaki cisimdir, source:"ء ر ض,B001"}. Yerin kökü kalın bir yer döşemesini de adlandırır: {ar:الإراض بساط ضخم من وبر أو صوف, tr:el-irâdu bisâtun dahmun min veberin ev sûf, gloss:irâd, deve tüyünden ya da yünden kalın bir yaygıdır, source:"ء ر ض,B005"}. Yerin fiili de yaymaktır: {ar:الطحو كالدحو وهو البسط, tr:et-tahvu ke'd-dahv, ve huve'l-bast, gloss:tahv, dahv gibidir; yaymak demektir, source:"ط ح و,B001"}. Aynı kökte geniş bir gölgelik çadır da vardır: {ar:مظلة مطحوة ومطحية وطاحية وهو الضخم, tr:mizalletun mathuvvetun ve mathiyyetun ve tâhiyetun, ve huve'd-dahm, gloss:yayılmış, iri bir gölgelik çadır, source:"ط ح و,B005"}. Böylece iki ayet birlikte bir ev kurar: üstte kubbe gibi bir tavan, altta serilmiş bir yaygı.

Kur'an bu evi açıkça kurar. Allah bütün insanlara şöyle seslenir: {ar:جَعَلَ لَكُمُ ٱلْأَرْضَ فِرَٰشًۭا وَٱلسَّمَآءَ بِنَآءًۭ, tr:ce'ale lekumu'l-arda firâşen ve's-semâe binâen, gloss:yeri sizin için bir döşek, göğü bir bina yaptı, source:2:22}. Başka bir yerde aynı ikiliyi kendi ağzından anlatır: {ar:وَٱلسَّمَآءَ بَنَيْنَٰهَا بِأَيْي۟دٍۢ, tr:ve's-semâe beneynâhâ bi-eydin, gloss:göğü güçle kurduk, source:51:47}; {ar:وَٱلْأَرْضَ فَرَشْنَٰهَا فَنِعْمَ ٱلْمَٰهِدُونَ, tr:ve'l-arda ferasnâhâ fe-ni'me'l-mâhidûn, gloss:yeri döşedik; ne güzel döşeyicileriz, source:51:48}. Nûh kavmine yeri bir yaygı olarak hatırlatır: {ar:وَٱللَّهُ جَعَلَ لَكُمُ ٱلْأَرْضَ بِسَاطًۭا, tr:va'llâhu ce'ale lekumu'l-arda bisâtâ, gloss:Allah yeri sizin için bir yaygı yaptı, source:71:19}. Nebe' Suresi'ndeki iki ayet bu evi bir çadır gibi kurar: {ar:أَلَمْ نَجْعَلِ ٱلْأَرْضَ مِهَٰدًۭا, tr:e lem nec'ali'l-arda mihâdâ, gloss:yeri bir beşik döşeği yapmadık mı, source:78:6}; {ar:وَٱلْجِبَالَ أَوْتَادًۭا, tr:ve'l-cibâle evtâdâ, gloss:dağları da kazıklar, source:78:7}. Kazık, çadırı yere tutturan şeydir. İnkârcılara da bu tavanın kusursuzluğu gösterilir: {ar:كَيْفَ بَنَيْنَٰهَا وَزَيَّنَّٰهَا وَمَا لَهَا مِن فُرُوجٍۢ, tr:keyfe beneynâhâ ve zeyyennâhâ ve mâ lehâ min furûc, gloss:onu nasıl kurduk, nasıl süsledik; onda hiçbir yarık yok, source:50:6}. Nâziât Suresi'nde Allah dirilişi inkâr edenlere sorar ve bu surenin fiillerini aynı sırayla, aynı kafiyeyle dizer: {ar:ءَأَنتُمْ أَشَدُّ خَلْقًا أَمِ ٱلسَّمَآءُ ۚ بَنَىٰهَا, tr:e entum eşeddu halkan emi's-semâ', benâhâ, gloss:sizin yaratılışınız mı daha zor, yoksa göğün mü? Onu kurdu, source:79:27}; {ar:رَفَعَ سَمْكَهَا فَسَوَّىٰهَا, tr:rafe'a semkehâ fe-sevvâhâ, gloss:tavanını yükseltti ve onu düzenledi, source:79:28}; {ar:وَٱلْأَرْضَ بَعْدَ ذَٰلِكَ دَحَىٰهَآ, tr:ve'l-arda ba'de zâlike dehâhâ, gloss:yeri de ardından yaydı, source:79:30}.

Son satırda gök için kullanılan "sevvâhâ", bu surede yedinci ayette nefis için gelir. Bitirme işi şudur: {ar:سويت الشيء فاستوى, tr:sevveytu'ş-şey'e fe'stevâ, gloss:şeyi düzledim, o da düzgün hale geldi, source:"س و ي,B002"}. Sonuç kusursuz bir biçimdir: {ar:السوي الذي سوى الله خلقه لا دمامة فيه ولا داء, tr:es-seviyyu'llezî sevva'llâhu halkahu, lâ demâmete fîhi ve lâ dâ', gloss:seviyy, Allah'ın yaratılışını düzgün kıldığı kişidir; onda ne çirkinlik ne hastalık vardır, source:"س و ي,B002"}. Bu üçüncü yapı canlı bir nefistir: {ar:النفس الروح الذي به حياة الجسد وكل إنسان نفس, tr:en-nefsu'r-rûhu'llezî bihî hayâtu'l-cesed, ve kullu insânin nefs, gloss:nefs, bedenin kendisiyle yaşadığı ruhtur; her insan bir nefistir, source:"ن ف س,B011"}. Bina kökü de nefse uzanır. İnsanın yaratılıştan gelen yapısının adı bu kökten gelir: {ar:البنية الهيئة التي بني عليها, tr:el-binyetu'l-hey'etu'lletî buniye aleyhâ, gloss:binye, kişinin üzerine kurulduğu yapıdır, source:"ب ن ي,B002"}; {ar:فلان صحيح البنية أي الفطرة, tr:fulânun sahîhu'l-binye, eyi'l-fıtra, gloss:falanın binyesi sağlam, yani yaratılışı, source:"ب ن ي,B002"}. Göğüs kafesinin kaburgaları da bu kökle anılır ve evin direkleri gibi görülür: {ar:البواني أضلاع الزور, tr:el-bevânî edlâ'u'z-zevr, gloss:bevânî, göğüs kafesinin kaburgalarıdır, source:"ب ن ي,B009"}; {ar:البوائن جمع البوان وهو اسم كل عمود في البيت, tr:el-bevâinu cem'u'l-buvân, ve huve'smu kulli amûdin fi'l-beyt, gloss:bevâin, buvânın çoğuludur; çadırdaki her direğin adıdır, source:"ب ن ي,B009"}.

Kur'an insanı aynı fiille anlatır. Allah insana döner ve şöyle der: {ar:ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ, tr:ellezî halekake fe-sevvâke fe-adelek, gloss:seni yaratan, seni düzenleyen ve dengeli kılan, source:82:7}. İnsanın yaratılışı anlatılırken de aynı fiil gelir: {ar:ثُمَّ سَوَّىٰهُ وَنَفَخَ فِيهِ مِن رُّوحِهِۦ, tr:summe sevvâhu ve nefaha fîhi min rûhih, gloss:sonra onu düzenledi ve ona kendi ruhundan üfledi, source:32:9}. Düz bir anlatımda yemin gökten insana atlıyormuş gibi görünür. Fiiller ise atlamanın olmadığını gösterir. Aynı usta, aynı sırayla, aynı bitirme fiiliyle üçüncü bir yapı kurar. Nefis bu evin üçüncü odasıdır ve tavanın "sevvâhâ"sı onun da "sevvâhâ"sıdır.

Kaynaklar: 91:5 ٱلسَّمَآءِ س م و B004; 91:5 بَنَىٰهَا ب ن ي B001; 91:5 بَنَىٰهَا ب ن ي B002; 91:5 بَنَىٰهَا ب ن ي B004; 91:5 بَنَىٰهَا ب ن ي B009; 91:6 ٱلْأَرْضِ ء ر ض B001; 91:6 ٱلْأَرْضِ ء ر ض B005; 91:6 طَحَىٰهَا ط ح و B001; 91:6 طَحَىٰهَا ط ح و B005; 91:7 نَفْسٍۢ ن ف س B011; 91:7 سَوَّىٰهَا س و ي B002

## Düzlenen: dengelenmiş nefis, yere serilen kavim

Aynı fiil surede iki kez geçer. Yedinci ayette "sevvâhâ" bir nefsi düzgün bir biçime getirir. On dördüncü ayette "fe-sevvâhâ" bir kavmi yerle bir eder: {ar:فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا, tr:fe-kezzebûhu fe-akarûhâ fe-demdeme aleyhim rabbuhum bi-zenbihim fe-sevvâhâ, gloss:onu yalanladılar ve deveyi ayaklarından kestiler; Rableri de günahları yüzünden üstlerine yıkım indirdi ve onu dümdüz etti, source:91:14}. Kökün bir kolu geniş, düz araziyi adlandırır: {ar:السِيّ الفضاء من الأرض الواسع, tr:es-siyyu'l-fadâu mine'l-ardi'l-vâsi', gloss:siyy, geniş, açık düzlüktür, source:"س و ي,B009"}. Bir başka kolu ise eşitliği: {ar:السِيّ المثل من قولهم سِيّان أي مثلان, tr:es-siyyu'l-mislu, min kavlihim siyyân, ey meslân, gloss:siyy, denk demektir; "siyyân", yani iki eş sözünden, source:"س و ي,B001"}. Birinci anlamda kavim düz bir yer gibi serilir. İkincisinde hiçbiri ayrı tutulmaz, hepsi bir olur.

Altıncı ayetteki yayılmış yer, bu düzlenmenin önceden kurulmuş biçimidir. "Tahâ" fiili yaymanın yanında vurulup yere uzanmayı da anlatır: {ar:ضربه ضربة طحا منها أي امتد, tr:darabehû darbeten tahâ minhâ, ey imtedde, gloss:ona bir darbe vurdu, adam o darbeyle yere serildi, yani boylu boyunca uzandı, source:"ط ح و,B006"}. Yere yapışıp kalan bir deve de bu fiille anılır: {ar:وطحى البعير إلى الأرض أي لزق بها, tr:ve tahâ'l-ba'îru ile'l-ard, ey lezika bihâ, gloss:deve yere tahâ etti, yani yere yapıştı, source:"ط ح و,B006"}. Fiil helak olmayı da adlandırır: {ar:طحا إذا هلك, tr:tahâ izâ heleke, gloss:helak olduğunda "tahâ" denir, source:"ط ح و,B007"}. Yerin kendi kökünde ise yere doğru ağırlaşıp çökmek vardır: {ar:التأرض أيضا التثاقل إلى الأرض, tr:et-te'arrudu eyzan et-tesâkulu ile'l-ard, gloss:te'arrud, yere doğru ağırlaşıp çökmek anlamına da gelir, source:"ء ر ض,B006"}. Arada iki devirme olur. Birincisi devenindir: {ar:عقرت الفرس أي كسعت قوائمه بالسيف, tr:akartu'l-ferese, ey kese'tu kavâimehû bi's-seyf, gloss:atı akr ettim, yani ayaklarını kılıçla biçtim, source:"ع ق ر,B002"}. İkincisi kavmindir ve kökten kazımadır: {ar:الدَّمْدَمَة: الاستئصال, tr:ed-demdeme: el-isti'sâl, gloss:demdeme, kökünden kazımaktır, source:"د م د م,B001"}.

Kur'an bu düzlenmeyi Semûd için yerinde gösterir. Salih kavmine şunu hatırlatır: {ar:تَتَّخِذُونَ مِن سُهُولِهَا قُصُورًۭا وَتَنْحِتُونَ ٱلْجِبَالَ بُيُوتًۭا, tr:tettehızûne min suhûlihâ kusûran ve tenhitûne'l-cibâle buyûtâ, gloss:ovalarında saraylar ediniyor, dağları oyup evler yapıyorsunuz, source:7:74}. Bina kökü bu sarayları da adlandırır: {ar:بنى فلان بيتا من البنيان وبنى قصورا, tr:benâ fulânun beyten mine'l-bunyân ve benâ kusûran, gloss:falan bina olarak bir ev kurdu, saraylar kurdu, source:"ب ن ي,B001"}. "Tahâ" kökü de bu ovaların adıdır: {ar:والطحا المنبسط من الأرض, tr:ve't-tahâ el-munbesitu mine'l-ard, gloss:tahâ, yerin yayvan düzlüğüdür, source:"ط ح و,B001"}. Suçun fiili "akr", bir köyün sığındığı yüksek binanın da adıdır: {ar:العقر القصر الذي يكون معتمدا لأهل القرية يلجؤون إليه, tr:el-ukru'l-kasru'llezî yekûnu mu'temeden li-ehli'l-karye, yelce'ûne ileyh, gloss:ukr, köy halkının dayandığı ve sığındığı saraydır, source:"ع ق ر,B015"}. Daha genel olarak da: {ar:العقر كل بناء مرتفع, tr:el-ukru kullu binâin murtefi', gloss:ukr, yükseltilmiş her yapıdır, source:"ع ق ر,B015"}. Yurdun ortası da bu kökle anılır: {ar:عقر الدار محلة القوم, tr:ukru'd-dâri mahalletu'l-kavm, gloss:yurdun ortası, kavmin oturduğu yerdir, source:"ع ق ر,B013"}. Kur'an, Semûd'un kayaları oyan bir halk olduğunu söyler: {ar:وَثَمُودَ ٱلَّذِينَ جَابُوا۟ ٱلصَّخْرَ بِٱلْوَادِ, tr:ve Semûde'llezîne câbu's-sahra bi'l-vâd, gloss:vadide kayaları oyan Semûd, source:89:9}. Hicr halkı da bu evlerde kendini güvende sanmıştır: {ar:وَكَانُوا۟ يَنْحِتُونَ مِنَ ٱلْجِبَالِ بُيُوتًا ءَامِنِينَ, tr:ve kânû yenhitûne mine'l-cibâli buyûten âminîn, gloss:dağlardan güven içinde evler oyuyorlardı, source:15:82}.

Bu yapıların sonu düzlenmedir. Allah Semûd'un hikâyesini şöyle bitirir: {ar:فَأَصْبَحُوا۟ فِى دَارِهِمْ جَٰثِمِينَ, tr:fe-asbahû fî dârihim câsimîn, gloss:yurtlarında diz üstü çökmüş halde sabahladılar, source:7:78}; {ar:كَأَن لَّمْ يَغْنَوْا۟ فِيهَآ, tr:ke-en lem yağnev fîhâ, gloss:sanki orada hiç oturmamışlardı, source:11:68}. Bir başka anlatımda kuru ot gibi ezilirler: {ar:فَكَانُوا۟ كَهَشِيمِ ٱلْمُحْتَظِرِ, tr:fe-kânû ke-heşîmi'l-muhtezır, gloss:ağıl yapanın çiğnenmiş kuru otu gibi oldular, source:54:31}. Bir yerde de ayağa kalkamazlar: {ar:فَمَا ٱسْتَطَٰعُوا۟ مِن قِيَامٍۢ, tr:fe-mâ'steta'û min kıyâm, gloss:ayağa kalkmaya güçleri yetmedi, source:51:45}. Evleri boş kalır, yıkılır: {ar:فَتِلْكَ بُيُوتُهُمْ خَاوِيَةًۢ بِمَا ظَلَمُوٓا۟, tr:fe-tilke buyûtuhum hâviyeten bimâ zalemû, gloss:işte zulümleri yüzünden çökmüş, boş kalmış evleri, source:27:52}. Kur'an düzlemeyi dağlar için de sahneler. Kıyamette dağlar savrulur ve yer şöyle olur: {ar:فَيَذَرُهَا قَاعًۭا صَفْصَفًۭا, tr:fe-yezeruhâ kâ'an safsafâ, gloss:onları dümdüz bir alan olarak bırakır, source:20:106}; {ar:لَّا تَرَىٰ فِيهَا عِوَجًۭا وَلَآ أَمْتًۭا, tr:lâ terâ fîhâ ivecen ve lâ emtâ, gloss:orada ne bir eğrilik ne bir tümsek görürsün, source:20:107}. Aynı gün inkârcılar kendi üstlerine düzlenmeyi isterler: {ar:لَوْ تُسَوَّىٰ بِهِمُ ٱلْأَرْضُ, tr:lev tusevvâ bihimu'l-ard, gloss:keşke yer üstlerine düzlenseydi, source:4:42}. Fiil burada sevvâ fiilinin kendisidir.

Fiilin iki yüzü aynı kudrete aittir. Diriltmeyi inkâr edene Allah şunu söyler: {ar:بَلَىٰ قَٰدِرِينَ عَلَىٰٓ أَن نُّسَوِّىَ بَنَانَهُۥ, tr:belâ kâdirîne alâ en nusevviye benâneh, gloss:evet, parmak uçlarını bile yeniden düzenlemeye gücümüz yeter, source:75:4}. Ufacık bir şekli inceden inceye işleyen fiil, bir kavmi yere serer. Düz bir anlatım yalnızca "yok etti" der. Fiilin tekrarı ise yedinci ayetteki biçim verme ile on dördüncü ayetteki dümdüz etmeyi aynı elin iki işi olarak yan yana koyar. Ovaya saray, dağa ev kuran kavim, yaydığı yer kadar düz kalır.

Kaynaklar: 91:7 سَوَّىٰهَا س و ي B002; 91:14 فَسَوَّىٰهَا س و ي B009; 91:14 فَسَوَّىٰهَا س و ي B001; 91:6 طَحَىٰهَا ط ح و B001; 91:6 طَحَىٰهَا ط ح و B006; 91:6 طَحَىٰهَا ط ح و B007; 91:6 ٱلْأَرْضِ ء ر ض B006; 91:5 بَنَىٰهَا ب ن ي B001; 91:14 فَعَقَرُوهَا ع ق ر B002; 91:14 فَعَقَرُوهَا ع ق ر B013; 91:14 فَعَقَرُوهَا ع ق ر B015; 91:14 فَدَمْدَمَ د م د م B001

## Yutulan, içilen, payına düşen

Sekizinci ayetteki "elhemehâ" fiilinin ailesinde yutmak vardır: {ar:لهمت الشيء وقلما يقال إلا التهمت وهو ابتلاعه بمرة, tr:lehimtu'ş-şey'e, ve kallemâ yukâlu illâ iltehemtu, ve huve'btilâ'uhû bi-merre, gloss:bir şeyi lehimtu, ya da daha çok denildiği gibi iltehemtu: onu bir lokmada yuttum, source:"ل ه م,B001"}. Bunun en somut örneği emzikteki yavrudur: {ar:التهم الفصيل ما في ضرع أمه استوفاه, tr:iltehemel-fasîlu mâ fî dar'ı ummihî: istevfâh, gloss:sütten kesilmemiş yavru, annesinin memesindekini sonuna kadar emip tüketti, source:"ل ه م,B001"}. İlham bu yutuşun içe dönük biçimidir: {ar:الإلهام كأنه شيء ألقى في الروع فالتهمه, tr:el-ilhâmu ke-ennehû şey'un ulkıye fi'r-rav' fe'ltehemeh, gloss:ilham, gönle atılan ve gönlün yutuverdiği bir şey gibidir, source:"ل ه م,B002"}. Bu atış Allah'tan gelir: {ar:الإلهام إلقاء الشيء في الروع ويختص بما كان من جهة الله تعالى, tr:el-ilhâmu ilkâu'ş-şey'i fi'r-rav', ve yahtessu bimâ kâne min cihetillâhi teâlâ, gloss:ilham, bir şeyin gönle atılmasıdır ve Allah tarafından gelene mahsustur, source:"ل ه م,B002"}. Böylece ayet nefse iki lokma verir: fucûrunu ve takvâsını. Nefis ikisini de kendi içine alır.

Yedinci ayetteki "nefs" kelimesi de içmeye yakındır. Kök bir yudumu adlandırır: {ar:كرع في الإناء نفسا أو نفسين, tr:kera'a fi'l-inâi nefesen ev nefeseyn, gloss:kaptan bir ya da iki yudum içti, source:"ن ف س,B006"}. Suyun kendisini de: {ar:يقال للماء نفس ولأن قوام النفس به, tr:yukâlu li'l-mâi nefs, ve li-enne kıvâme'n-nefsi bih, gloss:suya da nefs denir, çünkü nefsin ayakta durması onunladır, source:"ن ف س,B008"}. Bu ses, nefsin bir kap gibi su aldığını duyurur.

On üçüncü ayette içilecek olan, devenin suyudur: {ar:فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا, tr:fe-kâle lehum rasûlu'llâhi nâkata'llâhi ve sukyâhâ, gloss:Allah'ın elçisi onlara dedi ki: Allah'ın dişi devesi ve onun su içmesi, source:91:13}. "Nâkata" ve "sukyâhâ" kelimelerindeki nasb hali Arapçada bir uyarıyı bildirir: bunlara dokunmayın, bunlardan sakının. Kur'an'daki diğer anlatım bu uyarıyı açıkça söyler. Salih'in sözüdür: {ar:هَٰذِهِۦ نَاقَةُ ٱللَّهِ لَكُمْ ءَايَةًۭ ۖ فَذَرُوهَا تَأْكُلْ فِىٓ أَرْضِ ٱللَّهِ ۖ وَلَا تَمَسُّوهَا بِسُوٓءٍۢ, tr:hâzihî nâkatu'llâhi lekum âyeten, fe-zerûhâ te'kul fî ardı'llâhi ve lâ temessûhâ bi-sû', gloss:işte bu, size bir işaret olarak Allah'ın devesi; bırakın Allah'ın yerinde otlasın ve ona kötülükle dokunmayın, source:7:73}. Sukyâ bir içirmedir: {ar:السقي والسقيا أن يعطيه ما يشرب, tr:es-sakyu ve's-sukyâ en yu'tıyehû mâ yeşrab, gloss:sakyi ve sukyâ, birine içecek bir şey vermektir, source:"س ق ي,B001"}. Kök, dilediği gibi alabileceği bir pay ayırmayı da anlatır: {ar:الإسقاء أن يجعل له ذلك حتى يتناوله كيف شاء, tr:el-iskâu en yec'ale lehû zâlike hattâ yetenâvelehû keyfe şâ', gloss:iskâ, ona bunu ayırmaktır ki istediği gibi alsın, source:"س ق ي,B002"}. Kur'an bu payı günlere böler. Salih Semûd'a şöyle der: {ar:هَٰذِهِۦ نَاقَةٌۭ لَّهَا شِرْبٌۭ وَلَكُمْ شِرْبُ يَوْمٍۢ مَّعْلُومٍۢ, tr:hâzihî nâkatun lehâ şirbun ve lekum şirbu yevmin ma'lûm, gloss:işte bir dişi deve; belli bir günde su içme hakkı onun, belli bir günde de sizin, source:26:155}. Allah'ın Salih'e verdiği talimatta da aynı bölüşüm vardır: {ar:وَنَبِّئْهُمْ أَنَّ ٱلْمَآءَ قِسْمَةٌۢ بَيْنَهُمْ ۖ كُلُّ شِرْبٍۢ مُّحْتَضَرٌۭ, tr:ve nebbi'hum enne'l-mâe kısmetun beynehum, kullu şirbin muhtadar, gloss:onlara suyun aralarında paylaştırıldığını haber ver; her içiş payına sahibi gelir, source:54:28}. Benzer bir paylaştırma Mûsâ kavminde de vardır. Taştan su fışkırır ve herkes kendi içme yerini bilir: {ar:فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ, tr:fe'nfecerat minhu'snetâ aşrate aynâ, kad alime kullu unâsin meşrabehum, gloss:ondan on iki pınar fışkırdı; her topluluk kendi içme yerini bildi, source:2:60}. Elçinin adı bile bu sahnede süt gibi akan bir bolluğu çağırır: {ar:الرسل اللبن الكثير المتتابع الدر, tr:er-reslu'l-lebenu'l-kesîru'l-mutetâbi'u'd-dirr, gloss:resl, ardı ardınca akan bol süttür, source:"ر س ل,B006"}.

Devenin payını çiğneyen kavim kendi payını alır. On dördüncü ayetteki "zenb" kelimesinin kökü, ağzına kadar dolu bir kovayı adlandırır: {ar:الذنوب الدلو الملأى ماء, tr:ez-zenûbu'd-delvu'l-mel'â mâen, gloss:zenûb, suyla dolu kovadır, source:"ذ ن ب,B007"}. Bu kova bir hisse anlamına da gelir: {ar:الذنوب في التنزيل هو النصيب, tr:ez-zenûbu fi't-tenzîli huve'n-nasîb, gloss:Kur'an'da zenûb, paydır, source:"ذ ن ب,B006"}. Kur'an bu kelimeyi zalimlerin cezası için kullanır: {ar:فَإِنَّ لِلَّذِينَ ظَلَمُوا۟ ذَنُوبًۭا مِّثْلَ ذَنُوبِ أَصْحَٰبِهِمْ, tr:fe-inne li'llezîne zalemû zenûben misle zenûbi ashâbihim, gloss:zulmedenlerin, öncekilerin payı gibi bir kova payı vardır, source:51:59}. Bu söz, Semûd'un da anıldığı helak edilmiş kavimler dizisinin hemen ardından gelir. Kova ile günah aynı kökten gelir. Düz bir anlatım "günahları yüzünden" der ve geçer. Kelimenin ailesi ise ölçüyü gösterir: devenin içme payını engelleyenler, kendi kovalarının tam payını alırlar.

Kaynaklar: 91:7 نَفْسٍۢ ن ف س B006; 91:7 نَفْسٍۢ ن ف س B008; 91:8 فَأَلْهَمَهَا ل ه م B001; 91:8 فَأَلْهَمَهَا ل ه م B002; 91:13 رَسُولُ ر س ل B006; 91:13 وَسُقْيَٰهَا س ق ي B001; 91:13 وَسُقْيَٰهَا س ق ي B002; 91:14 بِذَنۢبِهِمْ ذ ن ب B006; 91:14 بِذَنۢبِهِمْ ذ ن ب B007

## Buluşmalar

İlk buluşma sekizinci ayette olur. "Fucûr" kelimesi aynı kökten üç sahneyi bir arada tutar: geceyi yaran şafağı, bentten fırlayan suyu ve din perdesini yırtmayı. Gökte yarılma ışık getirir, nefiste ise koruyucu örtüyü yırtar ve bir taşkın başlatır. Takvâ aynı ayette hem bir örtüdür hem de bir settir. Tek bir kelime bu iki imgeyi birlikte taşır: örten ve alıkoyan. Böylece surenin başındaki düzenli nöbet nefsin içine taşınır. Gece güneşin üstünü sırası gelince örter ve sırası gelince açılır. Nefis ise ya kendi örtüsünü yerinde tutar ya da onu yırtıp taşar.

İkinci buluşma on ikinci ayetteki "inbe'ase" fiilindedir. Bu fiil üç imgeyi birden toplar. Fucûru tanımlayan atılıştır, deveyi köstekinden çözüp kaldırmanın sonucudur ve Allah'ın elçi gönderişinin eşi olan bir fiildir. Deve sürücüsünün dilinde biri kaldırır, deve kalkar. Bu ayette ise kaldıran yoktur. Adam kendi kendine, köstekinden kurtulmuş bir hayvan gibi kalkar ve Allah'ın gönderdiği deveye yönelir. Elçi gönderilmiştir, deve gönderilmiştir. Taşkın olan ise kendini gönderir.

Üçüncü buluşma, on dördüncü ayetten on beşinciye geçen bedenin arka ucudur. "Akr" topuk kirişini keser. O kirişin adı on beşinci ayetteki "ukbâ" kelimesinin kökündendir. Günahın adı olan "zenb" de hayvanın arka ucunun adıdır. Devenin imgesi ile suçun ardından gelen sonucun imgesi böylece aynı noktada birleşir. Kavim devenin arkasına vurur; karşılık da onların "arkalarından", yani günahlarının ardından gelir. Kova ile günahın aynı kökten gelmesi bunu ölçüye bağlar. Devenin su payını çiğneyenler kendi kova paylarını alırlar.

Dördüncü buluşma "sevvâ" fiilindedir. Bu fiil göğün ve nefsin bitirilişini Semûd'un yerle bir edilişine bağlar. Altıncı ayetteki yayılmış yer bu iki ucun arasında durur. Kavim ovaya saray kurmuştu. Yayılan yere kurulan sarayları yayılmış bir yer gibi dümdüz olur. Gökten yağan su, sürülen toprak ve büyüyen ekin bu yere bağlıdır. Hurmanın başını kesmeyi ve hiçbir şey bitirmeyen kumu anlatan "akr" fiili, kavmin tarlasını bir çorak yere çevirir.

Bu buluşmalar birlikte surenin hareketini taşır. Sure, her cismin yerini bildiği bir gökle başlar: ışık yayılır, ay onu izler, gündüz açar, gece örter. Ardından gök ve yerden bir ev kurulur ve aynı el nefsi bu evin üçüncü yapısı olarak düzenler. Nefse iki lokma yutturulur: hem yırtan ve taşan hem de örten ve alıkoyan. Dokuzuncu ve onuncu ayetler bu iki lokmanın sonucunu iki tarla gibi gösterir: biri sürülmüş ve büyümüş, öbürü gömülmüş. Semûd ise yanlış yolu seçer. Sınırı aşar, kendi en bedbahtının ardına düşer, gönderilen deveyi arkasından biçer. Karşılık gece gibi üstlerine kapanır ve evleri ile birlikte onları yayılmış bir yer gibi dümdüz eder. Sure, gece ile gündüzün nöbetleşmesini de adlandıran bir kelimeyle kapanır. Ama bu son nöbette, hükmün ardından gelecek ve onu geri çevirecek hiçbir şey yoktur.

