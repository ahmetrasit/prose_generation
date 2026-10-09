Focus: 99:3. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/99_3/D.r13/context.md =====
# 99:3 — focus

وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا

Anchor translation (canonical reading, reference only):

Ve insan, 'Ona ne oluyor?' dediğinde,

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَقَالَ | قَالَ | ق و ل | CONJ;V |
| 2 | ٱلْإِنسَٰنُ | إِنسَٰن | ء ن س | DET;N |
| 3 | مَا | مَا |  | INTG |
| 4 | لَهَا |  |  | P;PRON |


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
- 99:3 ◀ focus وَقَالَ ٱلْإِنسَٰنُ مَا لَهَا
- 99:4 يَوْمَئِذٍۢ تُحَدِّثُ أَخْبَارَهَا
- 99:5 بِأَنَّ رَبَّكَ أَوْحَىٰ لَهَا
- 99:6 يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ
- 99:7 فَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍ خَيْرًۭا يَرَهُۥ
- 99:8 وَمَن يَعْمَلْ مِثْقَالَ ذَرَّةٍۢ شَرًّۭا يَرَهُۥ


===== _commentary/v16/work/99_3/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق و ل (root_001272) — identity root of وَقَالَ (w1)

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

## ECHO ق ل ل (root_001251) — for وَقَالَ (w1): withheld observed target; not identity

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

===== _commentary/v16/out/s099/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 99:3, and ## Buluşmalar) =====
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

## Buluşmalar

Surenin hareketi bir yönden ötekine geçer: içeriden dışarıya, ağırdan hafife, büyükten küçüğe, sessizden konuşana, gizliden görünene. İmgeler bu hareketin farklı yüzlerini taşır ve birkaç sahnede üst üste biner.

İlk buluşma yerin boşalmasıyla doğumdur. İkinci ayetin iki kelimesi, {ar:وَأَخْرَجَتِ, tr:ve ahracet, gloss:ve çıkardı, source:99:2} ile {ar:أَثْقَالَهَا, tr:eskâlehâ, gloss:ağırlıkları, source:99:2}, hem gömülü yükü atan yeri hem doğuran bedeni anlatır. Kur’an bu iki sahneyi aynı ayetlerde tutar: Saatin sarsıntısı {source:22:1} ve her gebenin yükünü bırakması {source:22:2}; rahimden çocuğu çıkarmak ve suyla titreyip kabaran toprak {source:22:5}. Aynı ayet bitki imgesini de içerir; böylece boşalan yer, doğuran beden ve filiz veren tarla tek bir dirilişin üç görünüşü olur. Ağır bulutlarla meyveyi ve ölüleri çıkaran ayet {source:7:57} ağırlık imgesini de bu sahneye bağlar.

İkinci buluşma boşalan yerle konuşan yerdir. İnşikak suresinde sıra surenin sırasıyla aynıdır: yer içindekini atar ve boşalır {source:84:4}, sonra Rabbine kulak verir {source:84:5}. İkinci ayette yer yükünü çıkarır, beşinci ayette Rabbinin vahyini alır. Arada üçüncü ayetin sarsılmış insanı vardır: sarsıntı bedenine geçmiş, ağzından {ar:مَا لَهَا, tr:mâ lehâ, gloss:ona ne oluyor, source:99:3} sorusu çıkmıştır. Bu soru, sarsıntı imgesini konuşma imgesine bağlar; çünkü yer ona cevap verecektir. Suçluların kitabın önündeki sorusu {source:18:49} aynı biçimdedir ve ardından yaptıklarını hazır bulurlar: soru, haber ve görme bir sahnede toplanır.

Üçüncü buluşma konuşmayla göstermedir. Dördüncü ayette yerin anlattığı haber, işin içyüzüdür; anlatmak açığa vurmak, kılıcı parlatmaktır. Yerin içindekilerini çıkarması ile haberlerini anlatması aynı işlemdir: içeride olanın dışarı verilmesi. Kur’an bu iki çıkarışı yan yana koyar: kabirlerdeki altüst edilir ve göğüslerdeki ortaya dökülür {source:100:9}, {source:100:10}; kıyamet günü kitap çıkarılır ve açılmış bulunur {source:17:13}.

Dördüncü buluşma altıncı ayetin kendisidir. Sudan dönen kalabalık bir yöne yürür ve ayet varış yerini söyler: {ar:لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:li-yurav a‘mâlehum, gloss:amelleri kendilerine gösterilsin diye, source:99:6}. Yolun sonunda tutulan ayna vardır. Aynı kalabalık bölüklere serpilir ve zerre imgesi başlar; bölükler arasındaki uzaklık da iki payın imgesini açar. Bir kelime, {ar:أَشْتَاتًا, tr:eştâtâ, gloss:bölük bölük, source:99:6}, üç imgeyi birden taşır: sudan dönüş, serpilme ve ak ile kara kadar uzak iki pay.

Son buluşma zerrede olur. {ar:ذَرَّةٍ, tr:zerratin, gloss:zerre, source:99:8} hem serpilmenin en küçük birimidir hem terazideki en küçük ağırlık; kötülük sözünün yanında ateşten kopan kıvılcım, toprağı yarıp çıkan filiz ve güneşte yayılan ince ışık da duyulur. Ağırlık kökü burada çemberi kapatır: sure yerin bütün ağırlıklarıyla açılmış, aynı kökten bir miskalle biter. Lokman’ın oğluna söylediği söz {source:31:16} bu iki ucu birleştirir: yerin içinde gizli bir küçük ağırlık getirilir ve sözü {ar:إِنَّ ٱللَّهَ لَطِيفٌ خَبِيرٌ, tr:innallâhe latîfun habîr, gloss:Allah en ince şeyi bilen, her şeyden haberdardır, source:31:16} diye biter. Haber kökü burada da durur: yerin anlattığı haberler, her şeyden haberdar olanın bildiğidir. Yer ağırlıklarını verir, haberlerini anlatır; insan da tek tek, en küçük ağırlığına kadar amelini görür.

