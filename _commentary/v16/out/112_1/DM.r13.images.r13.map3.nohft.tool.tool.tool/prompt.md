Focus: 112:1. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/112_1/D.r13/context.md =====
# 112:1 — focus

قُلْ هُوَ ٱللَّهُ أَحَدٌ

Anchor translation (canonical reading, reference only):

De ki: O, Allah'tır, birdir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | قُلْ | قَالَ | ق و ل | V |
| 2 | هُوَ |  |  | PRON |
| 3 | ٱللَّهُ | ٱللَّه | ء ل ه | PN |
| 4 | أَحَدٌ | أَحَد | ء ح د | N |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 112 — full text (context; no pericope)

- 112:1 ◀ focus قُلْ هُوَ ٱللَّهُ أَحَدٌ
- 112:2 ٱللَّهُ ٱلصَّمَدُ
- 112:3 لَمْ يَلِدْ وَلَمْ يُولَدْ
- 112:4 وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ


===== _commentary/v16/work/112_1/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق و ل (root_001272) — identity root of قُلْ (w1)

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

## ء ل ه (root_000047) — identity root of ٱللَّهُ (w3)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## ء ح د (root_000017) — identity root of أَحَدٌ (w4)

- **B001** tek ve eşi olmayan olma — bir tane; tek ve eşsiz · yalnız bir, yalnız bir
  أحد فرع والأصل الواو وحد (maqayis); أحد بمعنى الواحد وهو أول العدد (sihah); قل هو الله أحد (sihah;mufradat); يستعمل مطلقا وصفا في وصف الله تعالى وأصله وحد (mufradat); أحد أحد (sihah)
- **B002** hiç kimse — olumsuzlukta hiç kimse
  لا أحد في الدار؛ ما في الدار أحد (sihah); أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا (mufradat); فما منكم من أحد عنه حاجزين (sihah;mufradat)
- **B003** bir sayısı, onlu kuruluşları ve on bire çıkarma — saymanın başlangıcındaki bir · on bir, on bir dişil biçimi ve yirmi bir · onları on bire çıkarmak
  أحد واثنان وأحد عشر وإحدى عشرة (sihah); الواحد المضموم إلى العشرات نحو أحد عشر وأحد وعشرين (mufradat); فأحدهن أي صيرهن أحد عشر (sihah)
- **B004** iki kişiden biri, ilk olan ve haftanın ilk günü — ikinizden biri · Pazar günü · Pazar günleri
  أن يستعمل مضافا أو مضافا إليه بمعنى الأول (mufradat); أما أحدكما (mufradat); يوم الأحد أي يوم الأول (mufradat); يوم الأحد يجمع على آحاد (sihah)
- **B005** tek başına kalma ve birer birer gelme — tek başına kalmak; işi yalnız üstlenmek · birer birer, ayrı ayrı
  ما استأحدت بهذا الأمر أي ما انفردت به (maqayis); استأحد الرجل انفرد (sihah); جاءوا آحاد أحاد (sihah)
- **B006** Medine'deki belirli bir dağın özel adı — Medine'deki dağın özel adı
  أحد جبل بالمدينة (sihah)

## و ل ه (root_005296) — documented alternative for ٱللَّهُ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ECHO ق ل ل (root_001251) — for قُلْ (w1): withheld observed target; not identity

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

===== _commentary/v16/out/s112/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 112:1, and ## Buluşmalar) =====
## Birde duran sayı

Sure aynı kelimeyle açılır ve aynı kelimeyle kapanır. Birinci ayetin sonunda {ar:أَحَدٌ, tr:ehad, gloss:bir, source:112:1} olumlu bir sayı olarak durur; dördüncü ayetin sonunda {ar:أَحَدٌۢ, tr:ehad, gloss:hiç kimse, source:112:4} olumsuzluğun altında yeniden gelir. Bu iki kullanım arasında sure, bir ikincinin ortaya çıkabileceği her yolu tek tek kapatır. Bunu görmek için kelimenin nasıl işlediğine bakmak gerekir. Arapça bu kelimeyi sayının başlangıcı olarak tarif eder: {ar:أحد بمعنى الواحد وهو أول العدد, tr:ehad bi-ma'na'l-vâhid ve hüve evvelü'l-aded, gloss:ehad "bir" anlamındadır, sayının ilkidir, source:"ء ح د,B001"}. Sayı dizisinde bu birin arkasından hemen ikincisi gelir: {ar:أحد واثنان وأحد عشر, tr:ehad ve'snân ve ehad aşer, gloss:bir, iki, on bir, source:"ء ح د,B003"}. Kelime ayrıca bir çiftin üyesini anlatmak için de kullanılır: {ar:أما أحدكما, tr:emmâ ehadükümâ, gloss:ikinizden biri ise, source:"ء ح د,B004"}; burada "bir", iki kişilik bir bütünün parçasıdır. Aynı aile tek başına kalmayı da adlandırır: {ar:استأحد الرجل انفرد, tr:iste'hade'r-racül infarade, gloss:adam yalnız kaldı, tekleşti, source:"ء ح د,B005"}. Kelime nitelemesiz bir sıfat olarak yalnız Allah için kullanılır: {ar:يستعمل مطلقا وصفا في وصف الله تعالى, tr:yüsta'melü mutlakan vasfen fî vasfillâhi teâlâ, gloss:mutlak olarak yalnız Allah'ı niteleyen bir sıfattır, source:"ء ح د,B001"}. Kelimenin ailesinden gelen bir imge, o kelimenin ayetteki anlamının yanında duyulur, onun yerine geçmez. Birinci ayetteki "bir" her şeyden önce Allah'ın birliğini söyler; aile ise bu birin, sayılmaya başlayıp ikiye geçmeyen bir sayı olduğunu ve bir çiftin yarısı olmadığını duyurur.

Üçüncü ayet, bir ikincinin doğabileceği en yakın yolu kapatır. Doğurmak da doğmak da bir çift gerektirir. Arapça anne ile babayı ikil (dual) kalıpta tek bir ad altında toplar: {ar:الوالد الأب والوالدة الأم وهما الوالدان, tr:el-vâlid el-eb ve'l-vâlide el-üm ve hümâ'l-vâlidân, gloss:vâlid baba, vâlide anne; ikisi birlikte vâlidân'dır, source:"و ل د,B002"}. Doğan kişinin de yanında onunla birlikte doğmuş bir yaşıtı olur ve bu da ikil kalıpta söylenir: {ar:لدة الرجل تربه؛ وهما لدان, tr:lidetü'r-racül tirbühû; ve hümâ lidân, gloss:adamın lidesi yaşıtıdır; ikisine lidân denir, source:"و ل د,B006"}. Böylece {ar:لَمْ يَلِدْ وَلَمْ يُولَدْ, tr:lem yelid ve lem yûled, gloss:doğurmadı ve doğurulmadı, source:112:3} sözü, her iki yönde de ikinciyi dışarıda bırakır: doğurmak yeni bir ikinci getirir, doğmak ise önceden var olan bir ikinciyi gerektirir. Dördüncü ayet son yolu kapatır. {ar:كُفُوًا, tr:küfüven, gloss:denk, source:112:4} "benzer" demektir: {ar:الكفء المثل, tr:el-küf' el-misl, gloss:küf', eş ve benzerdir, source:"ك ف ء,B001"}, {ar:كل شيء ساوى شيئا حتى يكون مثله فهو مكافئ له, tr:küllü şey'in sâvâ şey'en hattâ yekûne mislehû fe-hüve mükâfiün leh, gloss:bir şeye eşitlenip onun benzeri olan her şey ona denktir, source:"ك ف ء,B001"}. Denk, birinciyle aynı ölçüye gelen ikincidir. Sonra kelime olumsuzluğun altında geri döner ve o zaman bütün türü kapsar: {ar:أحد في النفي لاستغراق جنس الناطقين ولا واحد ولا اثنان فصاعدا, tr:ehad fi'n-nefyi li'stiğrâki cinsi'n-nâtıkîn ve lâ vâhid ve lâ'snân fe-sâiden, gloss:olumsuzlukta ehad konuşan varlıkların bütün türünü kuşatır: ne bir, ne iki, ne daha fazlası, source:"ء ح د,B002"}; tıpkı {ar:ما في الدار أحد, tr:mâ fi'd-dâri ehad, gloss:evde kimse yok, source:"ء ح د,B002"} sözünde olduğu gibi. Halka böyle kapanır: başta olumlu bir, ortada reddedilen çift, sonda içinde hiç kimse bulunmayan bir "hiç kimse".

Kur'an bu sayma işlemini açıkça sahneler. Allah, iki ilah edinmeyi yasaklarken sayıyı iki kez anar: {ar:لَا تَتَّخِذُوٓا۟ إِلَٰهَيْنِ ٱثْنَيْنِ ۖ إِنَّمَا هُوَ إِلَٰهٌۭ وَٰحِدٌۭ, tr:lâ tettehızû ilâheyni'sneyn, innemâ hüve ilâhün vâhid, gloss:iki ilah edinmeyin; O ancak tek bir ilahtır, source:16:51}. "Üç" diyenlere verilen cevapta sayı birin ötesine geçtiği anda reddedilir: {ar:وَمَا مِنْ إِلَٰهٍ إِلَّآ إِلَٰهٌۭ وَٰحِدٌۭ, tr:ve mâ min ilâhin illâ ilâhün vâhid, gloss:tek bir ilahtan başka ilah yoktur, source:5:73}. Allah kendini yaratıcı olarak anlattığı yerde insanlara ve hayvanlara eşler, yani çiftler yarattığını söyler ve hemen ardından kendisini bu düzenin dışına koyar: {ar:لَيْسَ كَمِثْلِهِۦ شَىْءٌۭ, tr:leyse ke-mislihî şey', gloss:O'nun benzeri gibi hiçbir şey yoktur, source:42:11}. Yaratılmışlar çift hâlinde var olur; O'nun bir benzeri yoktur. Peygambere yöneltilen soru da aynı denki arar ve bulamaz: {ar:هَلْ تَعْلَمُ لَهُۥ سَمِيًّۭا, tr:hel ta'lemü lehû semiyyâ, gloss:O'nun adaşı, dengi olan birini biliyor musun, source:19:65}. İnsanlara verilen buyruk da aynıdır: {ar:فَلَا تَجْعَلُوا۟ لِلَّهِ أَندَادًۭا, tr:fe-lâ tec'alû lillâhi endâdâ, gloss:Allah'a denkler koşmayın, source:2:22}.

Dördüncü ayetteki olumsuz "hiç kimse" Kur'an'da tekrar tekrar aynı işi görür. Kehf suresinin son ayetinde Peygambere, ilahın tek bir ilah olduğunu söylemesi emredilir ve ayet şu sözle kapanır: {ar:وَلَا يُشْرِكْ بِعِبَادَةِ رَبِّهِۦٓ أَحَدًۢا, tr:ve lâ yüşrik bi-ibâdeti rabbihî ehadâ, gloss:Rabbine kullukta hiç kimseyi ortak koşmasın, source:18:110}. Aynı surede Allah kendi hükmünden söz eder: {ar:وَلَا يُشْرِكُ فِى حُكْمِهِۦٓ أَحَدًۭا, tr:ve lâ yüşrikü fî hukmihî ehadâ, gloss:hükmüne hiç kimseyi ortak etmez, source:18:26}. Cin suresinde mescitlerin Allah'a ait olduğu söylenir: {ar:فَلَا تَدْعُوا۟ مَعَ ٱللَّهِ أَحَدًۭا, tr:fe-lâ ted'û maallâhi ehadâ, gloss:Allah'la birlikte hiç kimseye yalvarmayın, source:72:18}. Peygambere ise şunu söylemesi emredilir: {ar:وَلَآ أُشْرِكُ بِهِۦٓ أَحَدًۭا, tr:ve lâ üşrikü bihî ehadâ, gloss:O'na hiç kimseyi ortak koşmam, source:72:20}. Hemen ardından da şunu söylemesi emredilir: {ar:قُلْ إِنِّى لَن يُجِيرَنِى مِنَ ٱللَّهِ أَحَدٌۭ, tr:kul innî len yücîranî minallâhi ehad, gloss:de ki: beni Allah'a karşı hiç kimse koruyamaz, source:72:22}. Her birinde olumsuz ehad, birin karşısında durabilecek ikinci kişinin yerini boş bırakır.

Kaynaklar: 112:1 أَحَدٌ ء ح د B001; 112:1 أَحَدٌ ء ح د B003; 112:1 أَحَدٌ ء ح د B004; 112:1 أَحَدٌ ء ح د B005; 112:4 أَحَدٌۢ ء ح د B002; 112:3 يَلِدْ و ل د B002; 112:3 يُولَدْ و ل د B006; 112:4 كُفُوًا ك ف ء B001

## Kapısına gidilen efendi

Samed'in bir başka anlamı, tek bir tarifte hem bir hareketi hem de bir rütbeyi bir arada tutar: {ar:صمده يصمده صمدا أي قصده والصمد السيد لأنه يصمد إليه في الحوائج وبيت مصمد أي مقصود, tr:samedehû yasmüdühû samden ey kasadehû ve's-samed es-seyyid li-ennehû yusmedü ileyhi fi'l-havâic ve beytün musammed ey maksûd, gloss:samedehû, ona yöneldi demektir; Samed efendidir, çünkü ihtiyaçlarda ona yönelinir; beytün musammed, gidilen ev demektir, source:"ص م د,B001"}. Sahnede bir ev ve bir kapı vardır. İnsanlar ihtiyaçlarını alıp oraya giderler. Kapısına gidilen kişi efendidir ve efendiliği de tam olarak bu yönelişten gelir. Yöneliş bir dayanmayı da içerir: {ar:وصمده قصد معتمدا عليه قصده, tr:ve samedehû kasade mu'temiden aleyhi kasdehû, gloss:ona dayanarak yöneldi, source:"ص م د,B001"}. Bu efendinin efendiliği en son noktasına varmıştır: {ar:الصمد السيد الذي قد انتهى سؤدده, tr:es-samed es-seyyid ellezî kad inteha sü'dedüh, gloss:Samed, efendiliği son noktasına varmış efendidir, source:"ص م د,B001"}. Kendisine gelen işi gözetir ve onunla ilgilenir: {ar:إني على صمادة من أمر إذا أشرف عليه وحفلت به, tr:innî alâ samâdetin min emrin izâ eşrafe aleyhi ve hafeltü bih, gloss:bir işi gözetip onunla ilgilendiğimde "o işin samâdesi üzerindeyim" denir, source:"ص م د,B005"}.

Birinci ve ikinci ayetteki {ar:ٱللَّهُ, tr:Allah, gloss:Allah, source:112:2} adı da aynı yönelişi taşır. Kök kulluk etmeyi anlatır ve ilah, kulluk edilen olduğu için bu adı alır: {ar:أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود, tr:aslün vâhid ve hüve't-teabbüd, fe'l-ilâh Allâhu teâlâ li-ennehû ma'bûd, gloss:tek bir köktür, kulluk etmeyi anlatır; ilah, kulluk edilen olduğu için yüce Allah'tır, source:"ء ل ه,B001"}. Kulun bu yöneliş içindeki hâli de aynı köktendir: {ar:التأله التنسك والتعبد, tr:et-teellüh et-tenessük ve't-teabbüd, gloss:teellüh, kendini ibadete vermektir, source:"ء ل ه,B001"}. Ad, ihtiyacı olanın seslendiği addır: {ar:يا ألله اغفر لي, tr:yâ allâhu'ğfir lî, gloss:ey Allah, beni bağışla, source:"ء ل ه,B002"}. Yönelişin bir de tersi vardır. Aynı kök çok yöne dağılmış kulluğu da adlandırır: {ar:الآلهة الأصنام, tr:el-âlihe el-esnâm, gloss:âlihe putlardır, source:"ء ل ه,B001"}; bir kavim ona taptığı için güneşe bile bu kökten bir ad verilmiştir {source:"ء ل ه,B001"}. Dördüncü ayetteki denk kelimesinin kökü de yönelişi saptırmayı anlatır: {ar:كفأت القوم إذا صرفتهم إلى غيره, tr:kefe'tü'l-kavme izâ sarafthüm ilâ ğayrih, gloss:bir kavmi başka birine yönelttim, source:"ك ف ء,B002"}.

Kapısına gidilen efendinin çevresinde rütbeleri olan bir düzen vardır. Dördüncü ayetteki fiilin kökü konumu ve itibarı anlatır: {ar:المكانة المنزلة؛ مكين عند فلان بين المكانة, tr:el-mekâne el-menzile; mekînün inde fülânin beyyinü'l-mekâne, gloss:mekâne konum ve itibardır; falanın yanında itibarı açıkça yüksektir, source:"ك و ن,B002"}. Aynı kök birine kefil olmayı da anlatır: {ar:الكيانة الكفالة؛ كنت على فلان أكون كونا أي تكفلت به, tr:el-kiyâne el-kefâle; küntü alâ fülânin ekûnü kevnen ey tekeffeltü bih, gloss:kiyâne kefalettir; falana kefil oldum, source:"ك و ن,B003"}. Alttakilerin boyun eğişini de anlatır: {ar:الاستكانة الخضوع, tr:el-istikâne el-hudû', gloss:istikâne boyun eğmektir, source:"ك و ن,B004"}. Birinci ayetin ilk kelimesi olan {ar:قُلْ, tr:kul, gloss:de, source:112:1} fiilinin kökü de bu düzende bir hükümdarı adlandırır: {ar:القيل ملك من ملوك حمير دون الملك الأعظم, tr:el-kayl melikün min mülûki himyer dûne'l-meliki'l-a'zam, gloss:kayl, en büyük hükümdardan aşağı rütbedeki Himyer krallarından biridir, source:"ق و ل,B004"}. Bu adı, sözü yerine getirildiği için almıştır: {ar:كأنه الذي له قول أي ينفذ قوله, tr:ke-ennehû'llezî lehû kavlün ey yenfüzü kavlüh, gloss:sanki sözü olan, yani sözü yürüyen kişidir, source:"ق و ل,B004"}. Denk ise böyle bir düzende hükümdarın karşısına çıkabilecek tek kişidir. O, soyda, malda ve savaşta dengidir {source:"ك ف ء,B001"}; hükümdarın evine kız verebilir, onunla eşit şartlarda savaşabilir, iyiliğine aynısıyla karşılık verebilir: {ar:المكافأة مجازاة النعم, tr:el-mükâfee mücâzâtü'n-niam, gloss:mükâfee, nimetlere karşılık vermektir, source:"ك ف ء,B001"}. Kapıya ihtiyacıyla gelen kişi ise aldığına aynısıyla karşılık veremez. Dördüncü ayet bu düzenden yalnızca bir kişiyi çıkarır: zirvede efendiye denk olabilecek kişiyi. Kapıya gelenler, kefil olunanlar ve boyun eğenler yerlerinde kalır.

Kur'an kapıya gidişi insanın kendi hâli olarak gösterir. Allah insanlara, sahip oldukları her nimetin O'ndan geldiğini hatırlattıktan sonra şöyle der: {ar:ثُمَّ إِذَا مَسَّكُمُ ٱلضُّرُّ فَإِلَيْهِ تَجْـَٔرُونَ, tr:sümme izâ messekümü'd-durru fe-ileyhi tec'erûn, gloss:sonra size bir sıkıntı dokununca yalnız O'na yalvarırsınız, source:16:53}. Bir başka yerde aynı yöneliş bir soru hâlinde gelir: {ar:أَمَّن يُجِيبُ ٱلْمُضْطَرَّ إِذَا دَعَاهُ وَيَكْشِفُ ٱلسُّوٓءَ, tr:em men yücîbü'l-mudtarra izâ deâhü ve yekşifü's-sû', gloss:darda kalan kendisine yalvardığında ona karşılık veren ve sıkıntıyı gideren kimdir, source:27:62}. Hemen ardından da {ar:أَءِلَٰهٌۭ مَّعَ ٱللَّهِ, tr:e-ilâhün maallâh, gloss:Allah'la birlikte başka bir ilah mı var, source:27:62} diye sorulur. Kapıya gelenlerin sayısı varlığın tamamıdır: {ar:يَسْـَٔلُهُۥ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:yes'elühû men fi's-semâvâti ve'l-ard, gloss:göklerde ve yerde olan herkes O'ndan ister, source:55:29}. Kapıya gelenlerle efendi arasındaki fark da bir cümlede söylenir: {ar:أَنتُمُ ٱلْفُقَرَآءُ إِلَى ٱللَّهِ ۖ وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:entümü'l-fukarâü ilallâh, vallâhü hüve'l-ğaniyyü'l-hamîd, gloss:siz Allah'a muhtaçsınız; Allah ise zengin olandır, övülendir, source:35:15}. Kulun kendi sözü kulluğu ve dayanmayı aynı tek yöne çevirir: {ar:إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ, tr:iyyâke na'büdü ve iyyâke neste'în, gloss:yalnız sana kulluk eder, yalnız senden yardım isteriz, source:1:5}. Yönelişin saptırıldığı sahne de Kur'an'da vardır. Aracılar edinenler şöyle der: {ar:مَا نَعْبُدُهُمْ إِلَّا لِيُقَرِّبُونَآ إِلَى ٱللَّهِ زُلْفَىٰٓ, tr:mâ na'büdühüm illâ li-yukarribûnâ ilallâhi zülfâ, gloss:onlara, bizi Allah'a yaklaştırsınlar diye kulluk ediyoruz, source:39:3}. Yusuf da zindan arkadaşlarına şunu sorar: {ar:ءَأَرْبَابٌۭ مُّتَفَرِّقُونَ خَيْرٌ أَمِ ٱللَّهُ ٱلْوَٰحِدُ ٱلْقَهَّارُ, tr:e-erbâbün müteferrikûne hayrun emillâhü'l-vâhidü'l-kahhâr, gloss:birbirinden ayrı birçok rab mı daha iyidir, yoksa her şeye galip olan tek Allah mı, source:12:39}. Allah'tan başka ilahlar edinenler hakkında ise şu söylenir: {ar:لَّا يَخْلُقُونَ شَيْـًۭٔا وَهُمْ يُخْلَقُونَ, tr:lâ yahlukûne şey'en ve hüm yuhlakûn, gloss:hiçbir şey yaratmazlar, kendileri yaratılırlar, source:25:3}.

Zirvede bir denk bulunsaydı ne olacağı da sahnelenir. Peygambere surenin kalıbıyla örülmüş bir övgü emredilir: {ar:وَقُلِ ٱلْحَمْدُ لِلَّهِ ٱلَّذِى لَمْ يَتَّخِذْ وَلَدًۭا وَلَمْ يَكُن لَّهُۥ شَرِيكٌۭ فِى ٱلْمُلْكِ وَلَمْ يَكُن لَّهُۥ وَلِىٌّۭ مِّنَ ٱلذُّلِّ, tr:ve kuli'l-hamdü lillâhi'llezî lem yettehiz veleden ve lem yekün lehû şerîkün fi'l-mülki ve lem yekün lehû veliyyün mine'z-züll, gloss:de ki: övgü, çocuk edinmeyen, mülkte ortağı olmayan ve düşkünlükten ötürü bir koruyucuya ihtiyacı olmayan Allah'adır, source:17:111}. Ayette "kul", "veled" ve "lem yekün lehû" bir arada geçer ve bu kez mülke, yani hükümranlığa uygulanır. Allah, çocuğu ve yanında başka ilahları reddederken eşit rütbedekilerin ne yapacağını söyler: {ar:إِذًۭا لَّذَهَبَ كُلُّ إِلَٰهٍۭ بِمَا خَلَقَ وَلَعَلَا بَعْضُهُمْ عَلَىٰ بَعْضٍۢ, tr:izen le-zehebe küllü ilâhin bi-mâ halaka ve le-alâ ba'duhüm alâ ba'd, gloss:o zaman her ilah kendi yarattığını alıp giderdi ve biri öbürüne üstün gelmeye kalkardı, source:23:91}. Peygambere söylemesi emredilen sözde de aynı şey vardır: {ar:إِذًۭا لَّٱبْتَغَوْا۟ إِلَىٰ ذِى ٱلْعَرْشِ سَبِيلًۭا, tr:izen le'bteğav ilâ zi'l-arşi sebîlâ, gloss:o zaman Arş'ın sahibine bir yol ararlardı, source:17:42}. Savaşta denk olanın tarifi burada sahne olmuştur: eşit güçteki ikinci, tahtı ister. Sonuç da açıkça söylenir: {ar:لَوْ كَانَ فِيهِمَآ ءَالِهَةٌ إِلَّا ٱللَّهُ لَفَسَدَتَا, tr:lev kâne fîhimâ âlihetün illallâhü le-fesedetâ, gloss:yerde ve gökte Allah'tan başka ilahlar olsaydı ikisi de bozulurdu, source:21:22}.

Kaynaklar: 112:2 ٱلصَّمَدُ ص م د B001; 112:2 ٱلصَّمَدُ ص م د B005; 112:1 ٱللَّهُ ء ل ه B001; 112:1 ٱللَّهُ ء ل ه B002; 112:1 قُلْ ق و ل B004; 112:4 يَكُن ك و ن B002; 112:4 يَكُن ك و ن B003; 112:4 يَكُن ك و ن B004; 112:4 كُفُوًا ك ف ء B001; 112:4 كُفُوًا ك ف ء B002; 112:1 أَحَدٌ ء ح د B005

## Sözle var olmak, doğumla değil

Surenin fiilleri üç kökten gelir: kavl (söz), vilâde (doğum) ve kevn (olmak). Kur'an, şeylerin nasıl var olduğunu anlatan formülünde tam olarak bu üç kökten ikisini kullanır ve üçüncüsünü bu formülün karşısına koyar. Burada söz konusu olan bir aile imgesi değildir; Kur'an pasajlarında aynı köklerin yan yana gelmesidir. Formül şudur: Allah bir işe hükmedince {ar:فَإِنَّمَا يَقُولُ لَهُۥ كُن فَيَكُونُ, tr:fe-innemâ yekûlü lehû kün fe-yekûn, gloss:ona yalnızca "ol" der, o da olur, source:2:117}. Kevn kökü bu işlemi kendi tanımında taşır: {ar:كونه فتكون أحدثه فحدث, tr:kevvenehû fe-tekevvene ahdesehû fe-hadese, gloss:onu var etti, o da var oldu; meydana getirdi, o da meydana geldi, source:"ك و ن,B001"}. Söz, harflerden oluşup dile getirilerek ortaya çıkandır: {ar:المركب من الحروف المبرز بالنطق, tr:el-mürekkeb mine'l-hurûf el-mübraz bi'n-nutk, gloss:harflerden oluşan ve dile getirilerek ortaya çıkarılan, source:"ق و ل,B001"}. Doğum kökü ise bir şeyin var olmasının öbür yolunu adlandırır: tevellüd, bir şeyin başka bir şeyden çıkarak meydana gelmesidir {source:"و ل د,B005"}, ve doğum bir bedenin eylemidir {source:"و ل د,B003"}.

Kur'an bu iki yolu açıkça birbirinin karşısına koyar. Bakara suresinde Allah, O'nun bir çocuk edindiğini söyleyenlere cevap verir: {ar:وَقَالُوا۟ ٱتَّخَذَ ٱللَّهُ وَلَدًۭا ۗ سُبْحَٰنَهُۥ, tr:ve kâlü'ttehazallâhü veleden sübhâneh, gloss:Allah çocuk edindi dediler; O bundan münezzehtir, source:2:116}. Bir sonraki ayette, O'nun gökleri ve yeri yoktan var eden olduğu söylenir ve yukarıdaki formül gelir {source:2:117}. Söz, kavl kökünden; çocuk, veled kökünden; formül de kevn kökündendir. Çocuğun yerine söz konmuştur. Meryem suresinde İsa'nın doğumu anlatıldıktan sonra Allah aynı şeyi söyler: {ar:مَا كَانَ لِلَّهِ أَن يَتَّخِذَ مِن وَلَدٍۢ ۖ سُبْحَٰنَهُۥٓ, tr:mâ kâne lillâhi en yettehıze min veled, sübhâneh, gloss:Allah'ın çocuk edinmesi olacak şey değildir; O münezzehtir, source:19:35}. Aynı ayet de formülle devam eder {source:19:35}. Meryem'in kendisi de soruyu tam bu kelimelerle sorar: {ar:رَبِّ أَنَّىٰ يَكُونُ لِى وَلَدٌۭ وَلَمْ يَمْسَسْنِى بَشَرٌۭ, tr:rabbi ennâ yekûnü lî veledün ve lem yemsesnî beşer, gloss:Rabbim, bana hiçbir insan dokunmamışken benim nasıl çocuğum olur, source:3:47}. Aldığı cevap, aynı ayette yine formüldür {source:3:47}. Babasız bir doğum sözden gelir. İsa ile Âdem'in karşılaştırıldığı yerde de aynı şey söylenir: {ar:خَلَقَهُۥ مِن تُرَابٍۢ ثُمَّ قَالَ لَهُۥ كُن فَيَكُونُ, tr:halakahû min türâbin sümme kâle lehû kün fe-yekûn, gloss:onu topraktan yarattı, sonra ona "ol" dedi, o da oldu, source:3:59}. Kitap ehline hitap eden ayette İsa'nın kendisi bir söz olarak adlandırılır: {ar:وَكَلِمَتُهُۥٓ أَلْقَىٰهَآ إِلَىٰ مَرْيَمَ, tr:ve kelimetühû elkâhâ ilâ meryem, gloss:Meryem'e ulaştırdığı sözü, source:4:171}; aynı ayette {ar:سُبْحَٰنَهُۥٓ أَن يَكُونَ لَهُۥ وَلَدٌۭ, tr:sübhânehû en yekûne lehû veled, gloss:O, bir çocuğu olmaktan münezzehtir, source:4:171} denir. En’âm suresinde de her şeyi yaratmış olmak, çocuk sahibi olmanın karşısına konur: {ar:وَخَلَقَ كُلَّ شَىْءٍۢ, tr:ve halaka külle şey', gloss:ve her şeyi O yarattı, source:6:101}. Bir başka ayet de bu karşıtlığı mantıksal sonucuna götürür: {ar:لَّوْ أَرَادَ ٱللَّهُ أَن يَتَّخِذَ وَلَدًۭا لَّٱصْطَفَىٰ مِمَّا يَخْلُقُ مَا يَشَآءُ, tr:lev erâdallâhü en yettehıze veleden la'stafâ mimmâ yahluku mâ yeşâ', gloss:Allah çocuk edinmek isteseydi, yarattıklarından dilediğini seçerdi, source:39:4}. O'nun edinebileceği her şey zaten yarattıklarındandır.

Bu ışıkta okununca sure bir sözle açılır (kul), doğum yoluyla var olmayı iki yönde birden reddeder ve olumsuzlanmış kevn ile kapanır: {ar:وَلَمْ يَكُن لَّهُۥ كُفُوًا أَحَدٌۢ, tr:ve lem yekün lehû küfüven ehad, gloss:hiçbir şey O'na denk olmadı, source:112:4}. Surenin "kul" sözü Allah'ın Peygambere verdiği bir emirdir, yaratıcı söz değildir; bu bağ surenin kendi cümlesinde değil, köklerin Kur'an'daki buluşmasında kurulur. Bağın gösterdiği şudur: şeyler O'ndan doğarak değil, O'nun sözüyle var olur ve var olmuş hiçbir şey O'na denk olmamıştır.

Kaynaklar: 112:1 قُلْ ق و ل B001; 112:3 يَلِدْ و ل د B005; 112:3 يَلِدْ و ل د B003; 112:4 يَكُن ك و ن B001

## Emredilen söz ve uydurulan söz

Sure bir emirle açılır: {ar:قُلْ, tr:kul, gloss:de, source:112:1}. Söz, dil aracılığıyla dışarı çıkarılan şeydir; kökte dilin kendisi de bu adı taşır: {ar:المقول اللسان, tr:el-mikvel el-lisân, gloss:mikvel, dildir, source:"ق و ل,B002"}. "Söylemek" fiili bir görüşü benimseyip onu savunmak için de kullanılır {source:"ق و ل,B013"}. Bu yüzden emredilen söz, kişinin arkasında durduğu bir inançtır. Aynı kökün bir de sahte karşılığı vardır: tekavvül, olmamış bir şeyi söylemek ve onu birine yakıştırmaktır: {ar:تقول باطلا أي قال ما لم يكن, tr:tekavvele bâtılen ey kâle mâ lem yekün, gloss:bâtıl söz uydurdu, yani olmamış olanı söyledi, source:"ق و ل,B005"}, {ar:تقول عليه أي كذب عليه, tr:tekavvele aleyhi ey kezebe aleyh, gloss:onun adına söz uydurdu, yani ona yalan isnat etti, source:"ق و ل,B005"}. "Mâ lem yekün", yani "olmamış olan", dördüncü ayetin fiilini taşır. Kökte insanlar arasında yayılan söz de vardır: {ar:القالة القول الفاشي في الناس, tr:el-kâle el-kavlü'l-fâşî fi'n-nâs, gloss:kâle, insanlar arasında yayılan sözdür, source:"ق و ل,B007"}. Surenin doğum fiillerinin kökü ise uydurulmuş sözü kendi adıyla anar: {ar:كتاب مولد أي مفتعل؛ بينة مولدة وليست بمحققة, tr:kitâbün müvelled ey müfteal; beyyinetün müvelledetün ve leyset bi-muhakkaka, gloss:müvelled kitap uydurma kitaptır; müvelled delil, doğrulanmamış delildir, source:"و ل د,B005"}. Böylece sahne bir sözler yarışmasıdır. Allah'ın çocuğu olduğuna dair bir söz insanlar arasında dolaşmaktadır; bu söz O'na isnat edilmiş, uydurulmuş bir sözdür. Peygambere de doğru sözü karşılık olarak söylemesi emredilir. Arapçada uydurulmuş söz için kullanılan kelime de "doğurulmuş" anlamına gelen kökten türemiştir.

Kur'an bu yarışmayı birçok yerde sahneler. Kehf suresinin başında Allah, O'nun çocuk edindiğini söyleyenleri uyarır: {ar:كَبُرَتْ كَلِمَةًۭ تَخْرُجُ مِنْ أَفْوَٰهِهِمْ ۚ إِن يَقُولُونَ إِلَّا كَذِبًۭا, tr:keburet kelimeten tahrucü min efvâhihim, in yekûlûne illâ kezibâ, gloss:ağızlarından çıkan söz ne büyük bir sözdür; yalandan başka bir şey söylemiyorlar, source:18:5}. Söz ağızdan dışarı çıkar ve yalandır. Saffât suresinde, Mekkelilerin kızları Allah'a ayırması anlatıldıktan sonra söz, doğum ve yalan iki ayette bir araya gelir: {ar:أَلَآ إِنَّهُم مِّنْ إِفْكِهِمْ لَيَقُولُونَ, tr:elâ innehüm min ifkihim le-yekûlûn, gloss:dikkat edin, onlar uydurmalarından ötürü söylüyorlar, source:37:151}, {ar:وَلَدَ ٱللَّهُ وَإِنَّهُمْ لَكَٰذِبُونَ, tr:velede'llâhü ve innehüm le-kâzibûn, gloss:"Allah doğurdu" diyorlar; onlar elbette yalancıdır, source:37:152}. Yûnus suresinde iddiaya verilen cevap, Allah'ın hiçbir şeye ihtiyacı olmadığını söyler ve sözle biter: {ar:أَتَقُولُونَ عَلَى ٱللَّهِ مَا لَا تَعْلَمُونَ, tr:e-tekûlûne alallâhi mâ lâ ta'lemûn, gloss:Allah hakkında bilmediğiniz şeyi mi söylüyorsunuz, source:10:68}. Tevbe suresinde Allah, Yahudilerin ve Hristiyanların sözünü aktarır ve onu kendisinden önceki sözlerin bir kopyası olarak gösterir: {ar:ذَٰلِكَ قَوْلُهُم بِأَفْوَٰهِهِمْ ۖ يُضَٰهِـُٔونَ قَوْلَ ٱلَّذِينَ كَفَرُوا۟ مِن قَبْلُ, tr:zâlike kavlühüm bi-efvâhihim, yudâhiûne kavle'llezîne keferû min kabl, gloss:bu, ağızlarıyla söyledikleri sözdür; daha önce inkâr edenlerin sözüne benzetiyorlar, source:9:30}. Elden ele dolaşan söz budur. Allah'a kızlar isnat edenlere de şöyle denir: {ar:إِنَّكُمْ لَتَقُولُونَ قَوْلًا عَظِيمًۭا, tr:inneküm le-tekûlûne kavlen azîmâ, gloss:siz gerçekten çok büyük bir söz söylüyorsunuz, source:17:40}. Meryem suresinde sözün ağırlığı evrene yansır. İddia önce aktarılır: {ar:وَقَالُوا۟ ٱتَّخَذَ ٱلرَّحْمَٰنُ وَلَدًۭا, tr:ve kâlü'ttehaze'r-rahmânü veledâ, gloss:Rahman çocuk edindi dediler, source:19:88}. Ardından {ar:لَّقَدْ جِئْتُمْ شَيْـًٔا إِدًّۭا, tr:lekad ci'tüm şey'en iddâ, gloss:çok çirkin bir şey ortaya attınız, source:19:89} denir ve gökler bu sözden ötürü neredeyse yarılacak hâle gelir {source:19:90}, {ar:أَن دَعَوْا۟ لِلرَّحْمَٰنِ وَلَدًۭا, tr:en deav li'r-rahmâni veledâ, gloss:Rahman'a çocuk isnat ettikleri için, source:19:91}. Cinler de, eşi ve çocuğu reddettikten hemen sonra kendi içlerindeki beyinsizin sözünü anarlar: {ar:وَأَنَّهُۥ كَانَ يَقُولُ سَفِيهُنَا عَلَى ٱللَّهِ شَطَطًۭا, tr:ve ennehû kâne yekûlü sefîhunâ alallâhi şatatâ, gloss:bizim beyinsizimiz Allah hakkında saçma sözler söylüyordu, source:72:4}.

Sözle kurulan sahte akrabalık sahnesi Kur'an'da insan ilişkileri üzerinden de gösterilir ve bu sahnede doğum, sözün karşısında gerçeğin ölçüsü olarak durur. Karısına "sen bana annem gibisin" diyerek ondan uzaklaşanlar için şöyle denir: {ar:إِنْ أُمَّهَٰتُهُمْ إِلَّا ٱلَّٰٓـِٔى وَلَدْنَهُمْ ۚ وَإِنَّهُمْ لَيَقُولُونَ مُنكَرًۭا مِّنَ ٱلْقَوْلِ وَزُورًۭا, tr:in ümmehâtühüm ille'llâî velednehüm, ve innehüm le-yekûlûne münkeran mine'l-kavli ve zûrâ, gloss:anneleri ancak onları doğuranlardır; onlar gerçekten çirkin ve yalan bir söz söylüyorlar, source:58:2}. Evlatlıklar hakkında da şöyle denir: {ar:ذَٰلِكُمْ قَوْلُكُم بِأَفْوَٰهِكُمْ ۖ وَٱللَّهُ يَقُولُ ٱلْحَقَّ, tr:zâliküm kavlüküm bi-efvâhiküm, vallâhü yekûlü'l-hakk, gloss:bu sizin ağzınızla söylediğiniz sözdür; Allah ise doğruyu söyler, source:33:4}. Söz bir akrabalık iddia eder, gerçek ise ona uymaz. Sözün yanlışlıkla birine isnat edilmesi de sahnelenir. Kıyamet günü Allah İsa'ya, insanlara kendisini ve annesini iki ilah edinmelerini söyleyip söylemediğini sorar; İsa şöyle cevap verir: {ar:مَا يَكُونُ لِىٓ أَنْ أَقُولَ مَا لَيْسَ لِى بِحَقٍّ, tr:mâ yekûnü lî en ekûle mâ leyse lî bi-hakk, gloss:hakkım olmayan bir şeyi söylemem bana yakışmaz, source:5:116}. Tekavvül fiilinin kendisi de Peygamber hakkında söylenen bir sözde geçer: {ar:وَلَوْ تَقَوَّلَ عَلَيْنَا بَعْضَ ٱلْأَقَاوِيلِ, tr:ve lev tekavvele aleynâ ba'da'l-ekâvîl, gloss:eğer bize karşı bazı sözler uydurmuş olsaydı, source:69:44}. Birkaç ayet sonra olumsuz ehad da gelir: {ar:فَمَا مِنكُم مِّنْ أَحَدٍ عَنْهُ حَٰجِزِينَ, tr:fe-mâ minküm min ehadin anhü hâcizîn, gloss:hiçbiriniz buna engel olamazdınız, source:69:47}. Uydurulmuş söze karşı emredilen söz de Peygamberin ağzından çıkar: {ar:قُلْ إِن كَانَ لِلرَّحْمَٰنِ وَلَدٌۭ فَأَنَا۠ أَوَّلُ ٱلْعَٰبِدِينَ, tr:kul in kâne li'r-rahmâni veledün fe-ene evvelü'l-âbidîn, gloss:de ki: Rahman'ın bir çocuğu olsaydı, ona ilk kulluk eden ben olurdum, source:43:81}. Bir başka yerde de emredilen söz şudur: {ar:قُلْ إِنَّمَا هُوَ إِلَٰهٌۭ وَٰحِدٌۭ, tr:kul innemâ hüve ilâhün vâhid, gloss:de ki: O ancak tek bir ilahtır, source:6:19}. Meryem suresi, İsa'nın kendi sözlerinden sonra onu doğru söz olarak adlandırır: {ar:ذَٰلِكَ عِيسَى ٱبْنُ مَرْيَمَ ۚ قَوْلَ ٱلْحَقِّ ٱلَّذِى فِيهِ يَمْتَرُونَ, tr:zâlike îse'bnü meryem, kavle'l-hakkı'llezî fîhi yemterûn, gloss:işte Meryem oğlu İsa; hakkında şüpheye düştükleri doğru söz budur, source:19:34}. Surenin "kul" emri bu sahnede yerini bulur: dolaşan sözün karşısına söylenecek söz, ikinci, üçüncü ve dördüncü ayettir.

Kaynaklar: 112:1 قُلْ ق و ل B001; 112:1 قُلْ ق و ل B002; 112:1 قُلْ ق و ل B013; 112:1 قُلْ ق و ل B005; 112:1 قُلْ ق و ل B007; 112:3 يَلِدْ و ل د B005

## Buluşmalar

Birde duran sayı ile içi boş olmayan dolu beden aynı işlemin iki yüzüdür. İçi olan bir beden ikinci bir varlık doğurur; doğum bir şeyden başka bir şeyin çıkması, yani birin ikiye bölünmesidir. Samed'in dolu oluşu ile ehad'in ikiye geçmeyişi, üçüncü ayette tek bir cümleye dönüşür: içinden bir şey çıkmayan, ikincisi de olmayandır. En’âm suresindeki ayet bu iki imgeyi ve nesil zincirini bir arada tutar: {ar:أَنَّىٰ يَكُونُ لَهُۥ وَلَدٌۭ وَلَمْ تَكُن لَّهُۥ صَٰحِبَةٌۭ, tr:ennâ yekûnü lehû veledün ve lem tekün lehû sâhibeh, gloss:O'nun eşi olmamışken nasıl çocuğu olur, source:6:101}. Eş bir ikincidir, çocuk bir başka ikincidir; ikisi de olmayınca sayı birde kalır. Yaratılmışların çift hâlinde var olması ile O'nun benzerinin olmaması da Şûrâ suresinde aynı ayette durur {source:42:11}.

Samed kelimesinin iki anlamı, yani içi boş olmayan dolu beden ve yarattıkları yok olduktan sonra kalan daim varlık, üçüncü ayette birlikte karşılık bulur: O'nda doğuracak bir iç yoktur ve ölen bir zincirde yeri yoktur. Enbiyâ suresinde elçiler hakkında söylenen söz bu iki imgeyi tek bir sahnede birleştirir: {ar:وَمَا جَعَلْنَٰهُمْ جَسَدًۭا لَّا يَأْكُلُونَ ٱلطَّعَامَ وَمَا كَانُوا۟ خَٰلِدِينَ, tr:ve mâ cealnâhüm ceseden lâ ye'külûne't-taâme ve mâ kânû hâlidîn, gloss:onları yemek yemeyen bedenler kılmadık; ölümsüz de değillerdi, source:21:8}. Yemek yiyen beden, yani içi olan beden, ölen bedendir. Mesih ile annesinin birlikte yemek yediğini söyleyen ayet de {source:5:75} doğuran ile doğurulanı içi olan iki beden olarak gösterir.

Kapısına gidilen efendi ile nesil zinciri, Meryem suresinde birbirine bağlanır. Çocuk olduğu iddia edilenler kapıya gelen kullardır: {ar:إِن كُلُّ مَن فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ إِلَّآ ءَاتِى ٱلرَّحْمَٰنِ عَبْدًۭا, tr:in küllü men fi's-semâvâti ve'l-ardı illâ âti'r-rahmâni abdâ, gloss:göklerde ve yerde olan herkes Rahman'a ancak kul olarak gelecektir, source:19:93}. Hemen önceki ayette {ar:وَمَا يَنۢبَغِى لِلرَّحْمَٰنِ أَن يَتَّخِذَ وَلَدًا, tr:ve mâ yenbeğî li'r-rahmâni en yettehıze veledâ, gloss:çocuk edinmek Rahman'a yakışmaz, source:19:92} denmiştir. Aynı iddiaya bir başka yerde verilen cevap da aynıdır: {ar:بَلْ عِبَادٌۭ مُّكْرَمُونَ, tr:bel ibâdün mükramûn, gloss:hayır, onlar ikram edilmiş kullardır, source:21:26}. Mesih'in kendisi de beşikte ilk sözünü bu yönde söyler: {ar:إِنِّى عَبْدُ ٱللَّهِ, tr:innî abdullâh, gloss:ben Allah'ın kuluyum, source:19:30}. Zincirde çocuk yerine konmak istenen, efendinin kapısındaki kuldur.

Efendi imgesi ile birde duran sayı, zirvedeki denkte buluşur. Soyda, malda ve savaşta denk olan kişinin yokluğunu dördüncü ayet olumsuz ehad ile söyler. Eşit rütbede ikinci bir ilah olsaydı neler olacağını anlatan ayetler {source:23:91} {source:17:42}, savaşta denk olanın tarifini sahneye dönüştürür. İsrâ suresindeki övgü {source:17:111} da surenin kalıbını hükümranlığa uygular.

Söz imgelerinin ikisi Bakara suresinde iki ayet arasında karşılaşır. Uydurulmuş söz {ar:وَقَالُوا۟ ٱتَّخَذَ ٱللَّهُ وَلَدًۭا, tr:ve kâlü'ttehazallâhü veledâ, gloss:Allah çocuk edindi dediler, source:2:116} ile başlar, yaratıcı söz {ar:يَقُولُ لَهُۥ كُن فَيَكُونُ, tr:yekûlü lehû kün fe-yekûn, gloss:ona "ol" der, o da olur, source:2:117} ile biter. Her iki ayet de aynı soruya cevap verir: şeyler Allah'tan doğarak mı, yoksa O'nun sözüyle mi var olur? Ahzâb suresindeki ayet de iki sözü yan yana koyar; bir yanda ağızla söylenen söz, öbür yanda {ar:وَٱللَّهُ يَقُولُ ٱلْحَقَّ, tr:vallâhü yekûlü'l-hakk, gloss:Allah doğruyu söyler, source:33:4}. Doğum kökünün uydurulmuş söz için de kullanılması, sözler yarışmasını nesil zincirine bağlar: "Allah doğurdu" diyenlerin sözü {source:37:152}, kendisi de "doğurulmuş", yani uydurulmuş bir sözdür.

Bu buluşmalar surenin hareketini taşır. Birinci ayet bir sözle açılır ve sayıyı bire koyar. İkinci ayet bütün yönelişi, kapısına gidilen, içi boş olmayan ve her şey yok olduktan sonra kalan tek bir efendiye çevirir. Üçüncü ayet bu efendiden çıkışı da efendinin bir şeyden çıkışını da kapatır ve nesil zincirini, uydurulmuş "doğurdu" sözüyle birlikte dışarıda bırakır. Dördüncü ayet olumsuz kevn ile hiçbir dengin hiçbir zaman var olmadığını söyler ve sureyi başladığı kelimeyle, bu kez içinde hiç kimse bulunmayan ehad ile kapatır.

