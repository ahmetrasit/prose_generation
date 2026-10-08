Focus: 91:13. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/91_13/D.r13/context.md =====
# 91:13 — focus

فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا

Anchor translation (canonical reading, reference only):

Bunun üzerine Allah'ın elçisi onlara, "Allah'ın devesine ve onun su içme hakkına dokunmayın!" dedi.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | فَقَالَ | قَالَ | ق و ل | REM;V |
| 2 | لَهُمْ |  |  | P;PRON |
| 3 | رَسُولُ | رَسُول | ر س ل | N |
| 4 | ٱللَّهِ | ٱللَّه | ء ل ه | PN |
| 5 | نَاقَةَ | نَاقَة | ن و ق | N |
| 6 | ٱللَّهِ | ٱللَّه | ء ل ه | PN |
| 7 | وَسُقْيَٰهَا | سُقْيَٰ | س ق ي | CONJ;N;PRON |


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
- 91:7 وَنَفْسٍۢ وَمَا سَوَّىٰهَا
- 91:8 فَأَلْهَمَهَا فُجُورَهَا وَتَقْوَىٰهَا
- 91:9 قَدْ أَفْلَحَ مَن زَكَّىٰهَا
- 91:10 وَقَدْ خَابَ مَن دَسَّىٰهَا
- 91:11 كَذَّبَتْ ثَمُودُ بِطَغْوَىٰهَآ
- 91:12 إِذِ ٱنۢبَعَثَ أَشْقَىٰهَا
- 91:13 ◀ focus فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا
- 91:14 فَكَذَّبُوهُ فَعَقَرُوهَا فَدَمْدَمَ عَلَيْهِمْ رَبُّهُم بِذَنۢبِهِمْ فَسَوَّىٰهَا
- 91:15 وَلَا يَخَافُ عُقْبَٰهَا


===== _commentary/v16/work/91_13/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق و ل (root_001272) — identity root of فَقَالَ (w1)

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

## ر س ل (root_000563) — identity root of رَسُولُ (w3)

- **B001** bir şeyi gönderme veya serbest bırakma — göndermek veya salıvermek · gönderme, yöneltme veya serbest bırakma · gönderilmiş rüzgarlar veya görevlendirilmiş melekler
  أصل واحد يدل على الانبعاث والامتداد (maqayis)؛ أرسلت فلانا في رسالة والمرسلات الرياح ويقال الملائكة (sihah)؛ إرسال الله أنبياءه وإرسال الشياطين تخليتهم وإياهم (tahdhib)؛ الإرسال يقابل الإمساك (mufradat)
- **B002** haber taşıyıcısı veya taşınan haber — elçi veya haberci · taşınan ileti veya haber · ileti veya taşınan haber · iletiler veya taşınan haberler · elçiler veya haberciler
  الرسول معروف (maqayis)؛ الرسول بمعنى الرسالة والرسائل جمع الرسالة (ayn)؛ أرسلت فلانا في رسالة فهو مرسل ورسول والرسول أيضا الرسالة (sihah)؛ الرسول معناه الذي يتابع أخبار الذي بعثه (tahdhib)؛ الرسول يقال للقول المتحمل وتارة لمتحمل القول والرسالة (mufradat)
- **B003** harekette veya uzanışta yumuşak akıcılık — rahat ve yumuşak ilerleyiş · rahat yürüyen, bacakları ve eklemleri yumuşak dişi deve · rahat yürüyen deve · düz ve salık saç · saçın düzleşip salık duruma gelmesi · hızlı veya rahatça ilerleyen deve sürüleri · uzun ya da yumuşak ve rahat hareketli bacaklar
  فالرسل السير السهل وناقة رسلة لينة المفاصل وشعر رسل (maqayis)؛ ناقة رسلة القوائم سلسة لينة المفاصل (ayn)؛ شعر رسل وبعير رسل وناقة رسلة وإبل مراسيل (sihah)؛ الرسل الذي فيه لين واسترخاء وناقة مرسال رسلة القوائم (tahdhib)؛ ناقة رسلة سهلة السير وإبل مراسيل منبعثة انبعاثا سهلا (mufradat)
- **B004** acele etmeden ölçülü ilerleme — Acele etme; yavaş ve sakin ol · işte veya konuşmada sakin, ağırbaşlı ve temkinli davranma · metni acele etmeden açık seçik okuma
  على رسلك أي على هينتك (maqayis)؛ تكلم على رسلك والترسل في الأمر والمنطق كالتمهل والتوقر والتثبت (ayn)؛ على رسلك أي اتئد فيه وترسل في قراءته (sihah)؛ الترسل من الرسل في الأمور والمنطق كالتمهل والتوقر والتثبت والترسيل التحقيق بلا عجلة (tahdhib)؛ على رسلك إذا أمرته بالرفق (mufradat)
- **B005** peş peşe gelen topluluklar — deve, koyun veya başka varlıklardan oluşan sürü · gruplar halinde, birbirinin ardından
  الرسل ما أرسل من الغنم إلى الرعي وجاء القوم أرسالا يتبع بعضهم بعضا (maqayis)؛ الرسل القطيع من كل شيء وجمعه أرسال (ayn)؛ الرسل القطيع من الإبل والغنم وجاءت الخيل أرسالا قطيعا قطيعا (sihah)؛ جاءت الإبل أرسالا رسل بعد رسل والرسل قطيع من الإبل (tahdhib)؛ جاءوا أرسالا أي متتابعين (mufradat)
- **B006** bol ve sürekli gelen süt — süt; özellikle bol ve sürekli gelen süt · hayvanlarından süt elde eder duruma gelmek
  الرِّسل اللبن لأنه يترسل من الضرع (maqayis)؛ والرسل اللبن (ayn)؛ والرسل أيضا اللبن وقد أرسل القوم أي صار لهم اللبن (sihah)؛ كثر الرسل العام أي كثر اللبن (tahdhib)؛ الرسل اللبن الكثير المتتابع الدر (mufradat)
- **B007** ısınıp güvenerek açılma — birine veya bir şeye ısınıp güvenmek · sana güvenip yanında rahat davranan kimse
  استرسلت إلى الشيء إذا انبعثت نفسك إليه وأنست (maqayis)؛ الاسترسال إلى شيء كالاستئناس والطمأنينة (ayn)؛ استرسل إليه أي انبسط واستأنس (sihah)؛ الاسترسال إلى الإنسان كالاستئناس والطمأنينة (tahdhib)
- **B008** karşılıklı iletişim ve eşlik — karşılıklı haberleşmek veya birbirine ayak uydurmak · atışmada veya başka bir uğraşta eşlik eden kişi · şarkıda veya işte bir öncekinin ardından giden eşlikçi
  رسيل الرجل الذي يقف معه في نضال أو غيره (maqayis)؛ راسله مراسلة فهو مراسل ورسيل الرجل الذي يراسله في نضال أو غيره (sihah)؛ العرب تسمي المراسل في الغناء والعمل المتالي (tahdhib)
- **B009** taliplerin haber gönderdiği dul veya ayrılmak üzere olan kadın [kalıp] — eşi ölmüş, boşanmış veya ayrılmak üzere olduğu için taliplerin haber gönderdiği kadın
  المرأة المراسل التي مات بعلها فالخطاب يراسلونها (maqayis)؛ امرأة مراسل كان لها زوج والخطاب يراسلونها الخطبة (ayn)؛ امرأة مراسل يموت زوجها أو أحست منه أنه يريد تطليقها (sihah)؛ امرأة مراسل وهي التي مات عنها زوجها أو طلقها (tahdhib)
- **B010** rahatlık ve gönül hoşluğuyla verme [kalıp] — sıkıntısında ve rahatlığında; gönül hoşluğuyla verirken
  النجدة الشدة والرسل الرخاء (maqayis)؛ في نجدتها ورسلها يريد الشدة والرخاء (sihah)؛ إلا من أعطى في رسلها أي بطيب نفس منه (tahdhib)
- **B011** özel adlandırma kümesi — kısa ok · iki damar · belirli bir topluluğun damızlık erkek devesi · aktarım zinciri kesintili söz · boncuklu kolye · başını henüz örtmeyen küçük kız
  الراسلان عرقان (maqayis)؛ المرسال سهم قصير (sihah)؛ هذا رسيل بني فلان أي فحل إبلهم وحديث مرسل والمرسلة القلادة وجارية رسل (tahdhib)

## ء ل ه (root_000047) — identity root of ٱللَّهِ (w4)

- **B001** tapınma ve tapınılan varlık — tapınmak · kendini tapınmaya vermek · tapınılır kılmak · tapınılan varlık, tanrı · tapınılan varlık · tanrılar, tapınılan nesneler · tapınma · kimi toplulukların tapındığı için bu adla anılan güneş · senin tapınman
  أصل واحد وهو التعبد، فالإله الله تعالى لأنه معبود، وتأله الرجل إذا تعبد، والإلاهة الشمس سميت بذلك لأن قوما كانوا يعبدونها (maqayis)؛ التأله التعبد (ayn)؛ أله بالفتح إلاهة أي عبد عبادة، مألوه أي معبود، الآلهة الأصنام، التأليه التعبيد، التأله التنسك والتعبد (sihah)؛ لا يكون إلاها حتى يكون معبودا، معبوداتهم من الأصنام والأوثان آلهة، الإلاهة الشمس، وإلاهتك وعبادتك (tahdhib)؛ إله اسما لكل معبود، أله فلان يأله الآلهة عبد، فالإله على هذا هو المعبود (mufradat)
- **B002** Yaratıcıya özgü ad ile seslenme ve ant biçimleri — Yaratıcıya özgü ad · Tanrı adına ant olsun, bunu yapmadım · ey Tanrı; yakarma seslenişi · ey Tanrı; doğrudan seslenme · Tanrı adına sen veya baban; şaşma ya da ant kalıbı · Tanrı adına, gerçekten sen veya biz; kısaltılmış ant kalıpları
  فالإله الله تعالى وسمي بذلك لأنه معبود (maqayis)؛ اسم الله الأكبر هو الله، الله ما فعلت ذاك تريد والله ما فعلته، لاه أنت أي لله أنت، لا هم اغفر لنا (ayn)؛ منه قولنا الله وأصله إلاه، يا ألله اغفر لي (sihah)؛ اسم الله الأكبر هو الله، الله ما فعلت تريد والله، اللهم بمعنى يا ألله، لاه أبوك، لهنك، لهنا، يا ألله اغفر لي (tahdhib)؛ الله قيل أصله إله فحذفت همزته وأدخل عليها الألف واللام فخص بالباري تعالى (mufradat)

## ن و ق (root_001567) — identity root of نَاقَةَ (w5)

- **B001** yükseklik ve dağın en yüksek yeri — dağın en yüksek yeri · dağların en yüksek yerleri
  أصل يدل على سمو وارتفاع (maqayis); أرفع موضع في الجبل نيق (maqayis); والنيق أرفع موضع في الجبل (sihah)
- **B002** dişi deve; dişi deve biçimindeki yıldız topluluğu — dişi deve · dişi develer · az sayıdaki dişi develer · dişi develer · dişi develer · dişi develer · dişi develer · dişi deve biçimindeki yıldız topluluğu
  ناقة ونوق (maqayis); الناقة تقديرها فعلة وجمعت على نوق (sihah); وقد تجمع الناقة على نياق (sihah); والناقة كواكب على هيئة الناقة (maqayis)
- **B003** erkek devenin dişi deveye dönüşmesi [kalıp] — erkek deve dişi deveye dönüştü · erkek deve dişi deveye dönüştü
  واستنوق الجمل تشبيه بها (maqayis); يضرب مثلا لمن ذل بعد عز (maqayis); استونق الجمل أي صار ناقة (sihah); ثم حوله إلى نعت ناقة فقال طرفة استنوق الجمل (sihah)
- **B004** deveyi uysallaştırma ve işleri düzene koyma — eğitilip uysallaştırılmış erkek deve · eğitilip uysallaştırılmış dişi deve · işleri yönetip düzelten adam
  بعير منوق أي مذلل مروض (sihah); وناقة منوقة (sihah); والنواق من الرجال الذي يروض الأمور ويصلحها (sihah)
- **B005** bir işte aşırı özenip incelik gösterme — bir işte aşırı özenip incelik göstermek · aşırı özen ve incelik · işi bilmeden bilgiçlik taslayıp ince eleyip sık dokuyan kişi
  تنوق في الأمر إذا بالغ فيه (maqayis); والنيقة لا تكون إلا من تنوق (maqayis); وتنوق في الأمر أي تأنق فيه (sihah); والاسم منه النيقة (sihah); خرقاء ذات نيقة (maqayis;sihah)
- **B006** seçip ayırma — seçip ayırma
  والانتياق مثل الانتقاء (sihah); مثل القياس انتاقها المنقى يعني القسي (sihah); وكان الكسائي يقول هو من النيقة (sihah)

## س ق ي (root_000722) — identity root of وَسُقْيَٰهَا (w7)

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

## و ل ه (root_005296) — documented alternative for ٱللَّهِ: Ebû’l-Heysem; Ezherî’nin Tehzîbü’l-luğa’daki aktarımı

- **B001** yoğun duygudan aklı karışma veya ayrılıktan özlem çekme — 
  أصل صحيح يدل على اضطراب شيء أو ذهابه (maqayis)؛ رجل واله وامرأة واله ووالهة (maqayis;sihah)؛ الوله ذهاب العقل والتحير من شدة الوجد (sihah)؛ ولهت إليه تله أن تحن إليه (tahdhib)؛ الوله يكون من الحزن والسرور مثل الطرب (tahdhib)؛ ناقة واله إذا اشتد وجدها على ولدها (sihah)؛ الجمل إذا فقد ألافه فحن إليها واله (tahdhib)؛ البلاد التي توله الإنسان أي تحيره (sihah)
- **B002** anneyi yavrusundan ayırıp özleme düşürme — 
  التوليه أن يفرق بين المرأة وولدها (maqayis;sihah)؛ لا توله والدة عن ولدها (maqayis;tahdhib)؛ التوليه أن يفرق بينهما في البيع وكل أنثى فارقت ولدها فهي واله (tahdhib)؛ لا تجعل والها وذلك في السبايا (sihah)
- **B003** salınan suyun açık arazide akıp kaybolması — 
  عين مولهة إذا أرسل ماؤها فذهب في الصحارى (maqayis)؛ ماء موله وموله أرسل في الصحراء فذهب (sihah)

## ECHO ق ل ل (root_001251) — for فَقَالَ (w1): withheld observed target; not identity

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

## ECHO س و ق (root_000762) — for وَسُقْيَٰهَا (w7): withheld observed target; not identity

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

===== _commentary/v16/out/s091/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 91:13, and ## Buluşmalar) =====
## Tarla: yarılan, sulanan, büyüyen toprak ve hiçbir şey bitirmeyen kum

Altıncı ayette yayılan yerin ailesinde verimli toprak vardır. Bu toprak dokuzuncu ayetin fiiliyle anılır: {ar:أرض أريضة أي زكية, tr:ardun erîdatun, ey zekiyye, gloss:erîde bir toprak, yani bereketle büyüyen toprak, source:"ء ر ض,B002"}. Bitkinin toprakta kök salıp çoğalması da yerin kökünden bir fiildir: {ar:تأرض النبت تمكن على الأرض فكثر, tr:te'arrada'n-nebtu: temekkene ale'l-ardı fe-kesura, gloss:bitki yere tutundu ve çoğaldı, source:"ء ر ض,B002"}. "Tahâ" fiili de toprağın yüzüne yayılmış bitkiyi anlatır: {ar:والبقلة المطحية النابتة على وجه الأرض قد افترشتها, tr:ve'l-baklatu'l-mathiyyetu en-nâbitetu alâ vechi'l-ard, kad efteraşethâ, gloss:yerin yüzünde biten ve onu döşek gibi kaplayan yayvan sebze, source:"ط ح و,B006"}. Göğün adı ise yağmurun da bitkinin de adıdır: {ar:العرب تسمى السحاب سماء والمطر سماء, tr:el-arabu tusemmi's-sehâbe semâen ve'l-matara semâ', gloss:Araplar buluta da yağmura da semâ der, source:"س م و,B004"}; {ar:سمي النبات سماء, tr:summiye'n-nebâtu semâ', gloss:bitkiye de semâ denmiştir, source:"س م و,B004"}. Bu adlarla beşinci ve altıncı ayetlerdeki ev bir tarlaya dönüşür. Tavandan su iner, döşeme yeşerir.

Tarlanın işlemesi suyun yolunu açmakla başlar. Üçüncü ayetteki gündüz kelimesi, toprağı yaran ırmakla aynı köktendir: {ar:سمي النهر لأنه ينهر الأرض أي يشقها, tr:summiye'n-nehru li-ennehû yenheru'l-ard, ey yeşukkuhâ, gloss:ırmağa nehr denmesi, toprağı yarmasındandır, source:"ن ه ر,B001"}. Sekizinci ayetteki fucûrun kökü suyun açıldığı yeri adlandırır: {ar:الفجرة موضع تفتح الماء, tr:el-fecretu mevdı'u tefettuhi'l-mâ', gloss:fecre, suyun açılıp aktığı yerdir, source:"ف ج ر,B001"}. Dokuzuncu ayetteki "efleha" fiili saban işidir: {ar:فلحت الأرض شققتها, tr:felahtu'l-arda: şakaktuhâ, gloss:toprağı sürdüm, yani yardım, source:"ف ل ح,B001"}. Çiftçinin adı da buradan gelir: {ar:سمي الأكار فلاحا لأنه يشق الأرض, tr:summiye'l-ekkâru fellâhan li-ennehû yeşukku'l-ard, gloss:çiftçiye fellâh denmesi, toprağı yarmasındandır, source:"ف ل ح,B003"}. Aynı ayetteki "zekkâhâ" ekinin büyümesidir: {ar:زكا الزرع يزكو زكاء ممدود أي نما, tr:zekâ'z-zer'u yezkû zekâen, ey nemâ, gloss:ekin zekâ etti, yani büyüdü, source:"ز ك و,B001"}; {ar:أصل الزكاة النمو الحاصل عن بركة الله تعالى, tr:aslu'z-zekâti'n-nemuvvu'l-hâsılu an bereketi'llâhi teâlâ, gloss:zekâtın aslı, Allah'ın bereketinden gelen büyümedir, source:"ز ك و,B001"}. On üçüncü ayetteki "sukyâ" bir tarlanın sudaki payıdır: {ar:كم سقى أرضك أي حظها من الشرب, tr:kem sakyu ardık, ey hazzuhâ mine'ş-şirb, gloss:toprağının sakyı ne kadar, yani su payı ne kadar, source:"س ق ي,B003"}. On dördüncü ayetteki "zenb" kelimesinin ailesinde yamaçlardaki su yolları vardır: {ar:المذانب مذانب التلاع وهي مسايل الماء فيها, tr:el-mezânibu mezânibu't-tilâ', ve hiye mesâyilu'l-mâi fîhâ, gloss:mezânib, yamaçlardaki su yataklarıdır, source:"ذ ن ب,B004"}. Aynı ayetteki "Rab" kelimesinin ailesinde ise bitkiyi besleyen bulut vardır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb: es-sehâb, summiye bi-zâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi beslediği için bu adı almıştır, source:"ر ب ب,B008"}. Kökün temel işi de budur: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye, ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi adım adım olgunluğa erdirmektir, source:"ر ب ب,B002"}.

Tarlanın tersi de surenin kelimelerinde durur. Onuncu ayetteki fiil, Arap dilinin açıkladığı türeyişle "dessese"ye götürür: toprağa itip gömmek. Kur'an'daki karşılığı, yukarıda anılan, toprağa gömme sahnesidir: {ar:أَمْ يَدُسُّهُۥ فِى ٱلتُّرَابِ, tr:em yedussuhû fi't-turâb, gloss:yoksa onu toprağa mı gömsün, source:16:59}. Çok derine itilen tohum filizlenmez. Fiil de büyümenin tam zıddı olarak tanımlanır: {ar:وهو نقيض زكا يزكو زكاء وزكاة وهو داس لا زاك, tr:ve huve nakîdu zekâ yezkû zekâen ve zekâten, ve huve dâsin lâ zâk, gloss:bu, büyümenin zıddıdır; o gömen biridir, büyüten değil, source:"د س و,B002"}. On dördüncü ayetteki suç fiili "akr", hiçbir şey bitirmeyen kumun adıdır: {ar:العاقر من الرمل ما لا ينبت شيئا, tr:el-âkiru mine'r-ramli mâ lâ yunbitu şey'â, gloss:âkir kum, hiçbir şey bitirmeyen kumdur, source:"ع ق ر,B017"}. Aynı fiil hurmanın büyüme noktasını kesip atmayı da anlatır: {ar:عقرت النخلة إذا قطعت رأسها كله مع الجمار, tr:ukırati'n-nahletu izâ kutı'a ra'suhâ kulluhû ma'a'l-cumâr, gloss:hurmanın başı, özüyle birlikte tümden kesilince "ukırat" denir, source:"ع ق ر,B007"}.

Kur'an bu tarlayı açıkça sahneler. Abese Suresi'nde Allah insana yemeğine bakmasını söyler: {ar:فَلْيَنظُرِ ٱلْإِنسَٰنُ إِلَىٰ طَعَامِهِۦٓ, tr:fe'l-yenzuri'l-insânu ilâ taâmih, gloss:insan yemeğine bir baksın, source:80:24}. Ardından üç adım sayılır: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:suyu bol bol döktük, source:80:25}; {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:summe şakakne'l-arda şakkâ, gloss:sonra toprağı yardıkça yardık, source:80:26}; {ar:فَأَنۢبَتْنَا فِيهَا حَبًّۭا, tr:fe-enbetnâ fîhâ habbâ, gloss:orada tane bitirdik, source:80:27}. Dökmek, yarmak, bitirmek: dokuzuncu ayetteki sürme ve büyümenin adımları bunlardır. Nûh kavmine insanın kendisini bir bitki gibi anlatır: {ar:وَٱللَّهُ أَنۢبَتَكُم مِّنَ ٱلْأَرْضِ نَبَاتًۭا, tr:va'llâhu enbetekum mine'l-ardı nebâtâ, gloss:Allah sizi yerden bir bitki gibi bitirdi, source:71:17}. Bu yüzden nefsin büyütülmesi bir tarlanın büyümesiyle aynı işi görür. Kur'an iki toprağı yan yana koyar: {ar:وَٱلْبَلَدُ ٱلطَّيِّبُ يَخْرُجُ نَبَاتُهُۥ بِإِذْنِ رَبِّهِۦ, tr:ve'l-beledu't-tayyibu yahrucu nebâtuhû bi-izni rabbih, gloss:iyi toprağın bitkisi Rabbinin izniyle çıkar, source:7:58}; {ar:وَٱلَّذِى خَبُثَ لَا يَخْرُجُ إِلَّا نَكِدًۭا, tr:ve'llezî habuse lâ yahrucu illâ nekidâ, gloss:kötü topraktan ise ancak cılız bir şey çıkar, source:7:58}. Mallarını harcayanlar için de iki örnek verir. Biri tepedeki bahçedir: {ar:كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ, tr:ke-meseli cennetin bi-rabvetin esâbehâ vâbilun fe-âtet ukulehâ dı'feyn, gloss:tepedeki bir bahçe gibi; sağanak ona isabet edince ürününü iki kat verir, source:2:265}. Öteki üzerinde biraz toprak olan kayadır: {ar:كَمَثَلِ صَفْوَانٍ عَلَيْهِ تُرَابٌۭ فَأَصَابَهُۥ وَابِلٌۭ فَتَرَكَهُۥ صَلْدًۭا, tr:ke-meseli safvânin aleyhi turâbun fe-esâbehû vâbilun fe-terakehû saldâ, gloss:üstünde toprak bulunan düz bir kaya gibi; sağanak onu çıplak bırakır, source:2:264}. Aynı yağmur bir yerde büyütür, öteki yerde altındaki kayayı ortaya çıkarır.

Semûd da bir tarla halkıdır. Salih onlara bunu hatırlatır: {ar:هُوَ أَنشَأَكُم مِّنَ ٱلْأَرْضِ وَٱسْتَعْمَرَكُمْ فِيهَا, tr:huve enşeekum mine'l-ardı ve'ste'marakum fîhâ, gloss:sizi yerden O yetiştirdi ve sizi orada imar ettirdi, source:11:61}. Onlar bahçelerin ve kaynakların içindedir: {ar:فِى جَنَّٰتٍۢ وَعُيُونٍۢ, tr:fî cennâtin ve uyûn, gloss:bahçeler ve pınarlar içinde, source:26:147}; {ar:وَزُرُوعٍۢ وَنَخْلٍۢ طَلْعُهَا هَضِيمٌۭ, tr:ve zurû'in ve nahlin tal'uhâ hedîm, gloss:ekinler ve tomurcukları yumuşacık hurmalar içinde, source:26:148}. Hurmalık içinde yaşayan bir kavmin suç fiili, hurmanın başını kesip atan fiille aynıdır. Kur'an büyümenin karşılığını da su yollarıyla anlatır: {ar:وَذَٰلِكَ جَزَآءُ مَن تَزَكَّىٰ, tr:ve zâlike cezâu men tezekkâ, gloss:işte bu, arınıp büyüyenin karşılığıdır, source:20:76}. Bu söz, Firavun'un tehdidi karşısında iman eden sihirbazların ağzındadır ve altından ırmaklar akan bahçeleri anlatır. Kalbin taşa dönmesi bile bu dille anlatılır: {ar:وَإِنَّ مِنَ ٱلْحِجَارَةِ لَمَا يَتَفَجَّرُ مِنْهُ ٱلْأَنْهَٰرُ, tr:ve inne mine'l-hicârati lemâ yetefecceru minhu'l-enhâr, gloss:taşların öylesi vardır ki içinden ırmaklar fışkırır, source:2:74}. Bu sözler İsrailoğullarına, kalpleri bu taşlardan da katı olduğu için söylenir. Düz bir anlatım dokuzuncu ve onuncu ayeti "nefsini arındıran" ve "nefsini kirleten" diye geçer. Fiillerin ailesi ise iki tarlayı gösterir: biri sürülmüş, sulanmış ve yeşermiş; öbürü gömülmüş ya da kum.

Kaynaklar: 91:3 ٱلنَّهَارِ ن ه ر B001; 91:5 ٱلسَّمَآءِ س م و B004; 91:6 ٱلْأَرْضِ ء ر ض B002; 91:6 طَحَىٰهَا ط ح و B006; 91:8 فُجُورَهَا ف ج ر B001; 91:9 أَفْلَحَ ف ل ح B001; 91:9 أَفْلَحَ ف ل ح B003; 91:9 زَكَّىٰهَا ز ك و B001; 91:10 دَسَّىٰهَا د س و B002; 91:13 وَسُقْيَٰهَا س ق ي B003; 91:14 بِذَنۢبِهِمْ ذ ن ب B004; 91:14 رَبُّهُم ر ب ب B002; 91:14 رَبُّهُم ر ب ب B008; 91:14 فَعَقَرُوهَا ع ق ر B007; 91:14 فَعَقَرُوهَا ع ق ر B017

## Yutulan, içilen, payına düşen

Sekizinci ayetteki "elhemehâ" fiilinin ailesinde yutmak vardır: {ar:لهمت الشيء وقلما يقال إلا التهمت وهو ابتلاعه بمرة, tr:lehimtu'ş-şey'e, ve kallemâ yukâlu illâ iltehemtu, ve huve'btilâ'uhû bi-merre, gloss:bir şeyi lehimtu, ya da daha çok denildiği gibi iltehemtu: onu bir lokmada yuttum, source:"ل ه م,B001"}. Bunun en somut örneği emzikteki yavrudur: {ar:التهم الفصيل ما في ضرع أمه استوفاه, tr:iltehemel-fasîlu mâ fî dar'ı ummihî: istevfâh, gloss:sütten kesilmemiş yavru, annesinin memesindekini sonuna kadar emip tüketti, source:"ل ه م,B001"}. İlham bu yutuşun içe dönük biçimidir: {ar:الإلهام كأنه شيء ألقى في الروع فالتهمه, tr:el-ilhâmu ke-ennehû şey'un ulkıye fi'r-rav' fe'ltehemeh, gloss:ilham, gönle atılan ve gönlün yutuverdiği bir şey gibidir, source:"ل ه م,B002"}. Bu atış Allah'tan gelir: {ar:الإلهام إلقاء الشيء في الروع ويختص بما كان من جهة الله تعالى, tr:el-ilhâmu ilkâu'ş-şey'i fi'r-rav', ve yahtessu bimâ kâne min cihetillâhi teâlâ, gloss:ilham, bir şeyin gönle atılmasıdır ve Allah tarafından gelene mahsustur, source:"ل ه م,B002"}. Böylece ayet nefse iki lokma verir: fucûrunu ve takvâsını. Nefis ikisini de kendi içine alır.

Yedinci ayetteki "nefs" kelimesi de içmeye yakındır. Kök bir yudumu adlandırır: {ar:كرع في الإناء نفسا أو نفسين, tr:kera'a fi'l-inâi nefesen ev nefeseyn, gloss:kaptan bir ya da iki yudum içti, source:"ن ف س,B006"}. Suyun kendisini de: {ar:يقال للماء نفس ولأن قوام النفس به, tr:yukâlu li'l-mâi nefs, ve li-enne kıvâme'n-nefsi bih, gloss:suya da nefs denir, çünkü nefsin ayakta durması onunladır, source:"ن ف س,B008"}. Bu ses, nefsin bir kap gibi su aldığını duyurur.

On üçüncü ayette içilecek olan, devenin suyudur: {ar:فَقَالَ لَهُمْ رَسُولُ ٱللَّهِ نَاقَةَ ٱللَّهِ وَسُقْيَٰهَا, tr:fe-kâle lehum rasûlu'llâhi nâkata'llâhi ve sukyâhâ, gloss:Allah'ın elçisi onlara dedi ki: Allah'ın dişi devesi ve onun su içmesi, source:91:13}. "Nâkata" ve "sukyâhâ" kelimelerindeki nasb hali Arapçada bir uyarıyı bildirir: bunlara dokunmayın, bunlardan sakının. Kur'an'daki diğer anlatım bu uyarıyı açıkça söyler. Salih'in sözüdür: {ar:هَٰذِهِۦ نَاقَةُ ٱللَّهِ لَكُمْ ءَايَةًۭ ۖ فَذَرُوهَا تَأْكُلْ فِىٓ أَرْضِ ٱللَّهِ ۖ وَلَا تَمَسُّوهَا بِسُوٓءٍۢ, tr:hâzihî nâkatu'llâhi lekum âyeten, fe-zerûhâ te'kul fî ardı'llâhi ve lâ temessûhâ bi-sû', gloss:işte bu, size bir işaret olarak Allah'ın devesi; bırakın Allah'ın yerinde otlasın ve ona kötülükle dokunmayın, source:7:73}. Sukyâ bir içirmedir: {ar:السقي والسقيا أن يعطيه ما يشرب, tr:es-sakyu ve's-sukyâ en yu'tıyehû mâ yeşrab, gloss:sakyi ve sukyâ, birine içecek bir şey vermektir, source:"س ق ي,B001"}. Kök, dilediği gibi alabileceği bir pay ayırmayı da anlatır: {ar:الإسقاء أن يجعل له ذلك حتى يتناوله كيف شاء, tr:el-iskâu en yec'ale lehû zâlike hattâ yetenâvelehû keyfe şâ', gloss:iskâ, ona bunu ayırmaktır ki istediği gibi alsın, source:"س ق ي,B002"}. Kur'an bu payı günlere böler. Salih Semûd'a şöyle der: {ar:هَٰذِهِۦ نَاقَةٌۭ لَّهَا شِرْبٌۭ وَلَكُمْ شِرْبُ يَوْمٍۢ مَّعْلُومٍۢ, tr:hâzihî nâkatun lehâ şirbun ve lekum şirbu yevmin ma'lûm, gloss:işte bir dişi deve; belli bir günde su içme hakkı onun, belli bir günde de sizin, source:26:155}. Allah'ın Salih'e verdiği talimatta da aynı bölüşüm vardır: {ar:وَنَبِّئْهُمْ أَنَّ ٱلْمَآءَ قِسْمَةٌۢ بَيْنَهُمْ ۖ كُلُّ شِرْبٍۢ مُّحْتَضَرٌۭ, tr:ve nebbi'hum enne'l-mâe kısmetun beynehum, kullu şirbin muhtadar, gloss:onlara suyun aralarında paylaştırıldığını haber ver; her içiş payına sahibi gelir, source:54:28}. Benzer bir paylaştırma Mûsâ kavminde de vardır. Taştan su fışkırır ve herkes kendi içme yerini bilir: {ar:فَٱنفَجَرَتْ مِنْهُ ٱثْنَتَا عَشْرَةَ عَيْنًۭا ۖ قَدْ عَلِمَ كُلُّ أُنَاسٍۢ مَّشْرَبَهُمْ, tr:fe'nfecerat minhu'snetâ aşrate aynâ, kad alime kullu unâsin meşrabehum, gloss:ondan on iki pınar fışkırdı; her topluluk kendi içme yerini bildi, source:2:60}. Elçinin adı bile bu sahnede süt gibi akan bir bolluğu çağırır: {ar:الرسل اللبن الكثير المتتابع الدر, tr:er-reslu'l-lebenu'l-kesîru'l-mutetâbi'u'd-dirr, gloss:resl, ardı ardınca akan bol süttür, source:"ر س ل,B006"}.

Devenin payını çiğneyen kavim kendi payını alır. On dördüncü ayetteki "zenb" kelimesinin kökü, ağzına kadar dolu bir kovayı adlandırır: {ar:الذنوب الدلو الملأى ماء, tr:ez-zenûbu'd-delvu'l-mel'â mâen, gloss:zenûb, suyla dolu kovadır, source:"ذ ن ب,B007"}. Bu kova bir hisse anlamına da gelir: {ar:الذنوب في التنزيل هو النصيب, tr:ez-zenûbu fi't-tenzîli huve'n-nasîb, gloss:Kur'an'da zenûb, paydır, source:"ذ ن ب,B006"}. Kur'an bu kelimeyi zalimlerin cezası için kullanır: {ar:فَإِنَّ لِلَّذِينَ ظَلَمُوا۟ ذَنُوبًۭا مِّثْلَ ذَنُوبِ أَصْحَٰبِهِمْ, tr:fe-inne li'llezîne zalemû zenûben misle zenûbi ashâbihim, gloss:zulmedenlerin, öncekilerin payı gibi bir kova payı vardır, source:51:59}. Bu söz, Semûd'un da anıldığı helak edilmiş kavimler dizisinin hemen ardından gelir. Kova ile günah aynı kökten gelir. Düz bir anlatım "günahları yüzünden" der ve geçer. Kelimenin ailesi ise ölçüyü gösterir: devenin içme payını engelleyenler, kendi kovalarının tam payını alırlar.

Kaynaklar: 91:7 نَفْسٍۢ ن ف س B006; 91:7 نَفْسٍۢ ن ف س B008; 91:8 فَأَلْهَمَهَا ل ه م B001; 91:8 فَأَلْهَمَهَا ل ه م B002; 91:13 رَسُولُ ر س ل B006; 91:13 وَسُقْيَٰهَا س ق ي B001; 91:13 وَسُقْيَٰهَا س ق ي B002; 91:14 بِذَنۢبِهِمْ ذ ن ب B006; 91:14 بِذَنۢبِهِمْ ذ ن ب B007

## Dişi devenin bedeni

Surenin birçok kelimesi bir dişi deveyle uğraşmanın dilinden gelir. Merkezde devenin kendisi durur: {ar:ناقة ونوق, tr:nâkatun ve nûk, gloss:nâka, dişi deve; çoğulu nûk, source:"ن و ق,B002"}. On ikinci ayetin fiili de deve sürmenin dilindendir: {ar:بعثت الناقة إذا أثرتها, tr:ba'astu'n-nâkate izâ eseartuhâ, gloss:dişi deveyi kaldırdığımda "ba'astu" derim, source:"ب ع ث,B001"}. İşin tamamı şöyle anlatılır: {ar:بعثت البعير فانبعث إذا حللت عقاله وأرسلته لو كان باركا فأثرته, tr:ba'astu'l-ba'îra fe'nbe'ase izâ halaltu ıkâlehû ve erseltuh, ev kâne bârikan fe-esertuh, gloss:deveyi kaldırdım, o da kalktı; yani köstekini çözüp saldım ya da çökmüşse ayağa kaldırdım, source:"ب ع ث,B001"}. Deve sürücüsünün fiilinde iki taraf vardır: biri kaldırır, deve kalkar. On ikinci ayette ise kaldıran yoktur, yalnızca kalkan vardır. Köstekten kurtulan, en bedbaht adamdır ve kalkışı devenin üstüne yönelir.

İkinci ayetteki fiil, devenin ardından yürüyen yavruyu adlandırır: {ar:تلو الناقة ولدها الذي يتلوها, tr:tilvu'n-nâkati veleduhe'llezî yetlûhâ, gloss:devenin tilvu, onu izleyen yavrusudur, source:"ت ل و,B006"}. Ay güneşi, yavrunun anasını izlediği gibi izler. Elçinin adının kökü de devenin yürüyüşünü anlatır: {ar:ناقة رسلة لينة المفاصل, tr:nâkatun resletun leyyinetu'l-mefâsıl, gloss:resle deve, eklemleri yumuşak devedir, source:"ر س ل,B003"}; {ar:ناقة رسلة سهلة السير وإبل مراسيل منبعثة انبعاثا سهلا, tr:nâkatun resletun sehletu's-seyr, ve ibilun merâsîlu munbe'isetun inbi'âsen sehlen, gloss:resle deve, yürüyüşü kolay devedir; merâsîl develer, kolayca harekete geçen develerdir, source:"ر س ل,B003"}. Sekizinci ayetteki fiil memedeki yavruyu taşır, on üçüncü ayetteki kelime devenin suyunu. Bu sahne yukarıdaki iki imgede gösterildi.

On dördüncü ayette devenin bedenine yönelen fiil gelir. Bu fiil eşek arısı sokması gibi bir dokunuş değildir; ayağı biçmektir: {ar:عقر البعير كسف عرقوبه ثم جعل النحر عقرا, tr:akru'l-ba'îri kesfu urkûbih, summe cu'ile'n-nahru akran, gloss:deveyi akr etmek, topuk kirişini kesmektir; sonra boğazlamaya da akr denmiştir, source:"ع ق ر,B002"}. Kesilen kirişin adı on beşinci ayetteki kelimenin kökündendir: {ar:العرقوب عقب موتر خلف الكعبين والراء زائدة, tr:el-urkûbu akabun mûterun halfe'l-ka'beyn, ve'r-râu zâide, gloss:urkûb, iki aşık kemiğinin arkasında gerilmiş bir kiriştir; içindeki "r" harfi fazladan gelmiştir, source:"ع ق ب,B001"}; {ar:العقب العصب الذي تعمل منه الأوتار, tr:el-akabu'l-asabu'llezî tu'melu minhu'l-evtâr, gloss:akab, yay kirişlerinin yapıldığı sinirdir, source:"ع ق ب,B001"}. Topuğun kendisi de aynı köktendir: {ar:العقب مؤخر القدم, tr:el-akibu mu'ahharu'l-kadem, gloss:akib, ayağın arka ucudur, source:"ع ق ب,B002"}. On dördüncü ayetteki günah kelimesinin kökü de hayvanın arka tarafını adlandırır: {ar:ذنب وهو مؤخر الدواب, tr:zenebun, ve huve mu'ahharu'd-devâbb, gloss:zeneb, hayvanların arka ucudur, kuyruğudur, source:"ذ ن ب,B002"}. Ayakları biçen kılıç tam bu arka tarafa iner.

Kur'an devenin hikâyesini birkaç yerde anlatır. Allah Salih'e şöyle der: {ar:إِنَّا مُرْسِلُوا۟ ٱلنَّاقَةِ فِتْنَةًۭ لَّهُمْ فَٱرْتَقِبْهُمْ وَٱصْطَبِرْ, tr:innâ mursilu'n-nâkati fitneten lehum fe'rtakıbhum ve'stabir, gloss:onları sınamak için dişi deveyi gönderiyoruz; sen onları gözle ve sabret, source:54:27}. Burada deve "gönderilir", ve fiil elçinin adının köküyle kurulur. Ardından o tek adam bıçağa uzanır: {ar:فَنَادَوْا۟ صَاحِبَهُمْ فَتَعَاطَىٰ فَعَقَرَ, tr:fe-nâdev sâhibehum fe-teâtâ fe-akar, gloss:arkadaşlarını çağırdılar; o da eline aldı ve ayaklarını biçti, source:54:29}. Salih'in uyarısında devenin otlama hakkı da vardır, dokunma yasağı da: {ar:هَٰذِهِۦ نَاقَةُ ٱللَّهِ لَكُمْ ءَايَةًۭ ۖ فَذَرُوهَا تَأْكُلْ فِىٓ أَرْضِ ٱللَّهِ ۖ وَلَا تَمَسُّوهَا بِسُوٓءٍۢ, tr:hâzihî nâkatu'llâhi lekum âyeten, fe-zerûhâ te'kul fî ardı'llâhi ve lâ temessûhâ bi-sû', gloss:bu, size bir işaret olarak Allah'ın devesi; bırakın Allah'ın yerinde otlasın, ona kötülükle dokunmayın, source:7:73}. Şuarâ Suresi'nde ise devirmenin hemen ardından pişmanlık gelir: {ar:فَعَقَرُوهَا فَأَصْبَحُوا۟ نَٰدِمِينَ, tr:fe-akarûhâ fe-asbahû nâdimîn, gloss:ayaklarını biçtiler ve pişman oldular, source:26:157}. Düz bir anlatım "deveyi öldürdüler" der. Fiil ise işin yerini gösterir: önce topuğa, sonra yere yapılan bir iş. Kelimelerin dağılımı da bir sıra gösterir. Kaldırılan, izlenen, rahat yürüyen ve sulanan bir deve, sonunda arkasından biçilir. Bu ardından gelen kelimeler, son ayette suçun ardından gelecek olanı haber verir.

Kaynaklar: 91:2 تَلَىٰهَا ت ل و B006; 91:8 فَأَلْهَمَهَا ل ه م B001; 91:12 ٱنۢبَعَثَ ب ع ث B001; 91:13 نَاقَةَ ن و ق B002; 91:13 رَسُولُ ر س ل B003; 91:13 وَسُقْيَٰهَا س ق ي B001; 91:14 فَعَقَرُوهَا ع ق ر B002; 91:14 بِذَنۢبِهِمْ ذ ن ب B002; 91:15 عُقْبَٰهَا ع ق ب B001; 91:15 عُقْبَٰهَا ع ق ب B002

## Gönderilen ve peşine düşülen

Surenin başında doğru bir izleme vardır: ay güneşi izler. İzleme fiilinin bir kolu, vahyedilmiş kitabı izlemeyi anlatır: {ar:التلاوة تختص باتباع كتب الله المنزلة تارة بالقراءة وتارة بالارتسام, tr:et-tilâvetu tahtessu bi'ttibâ'i kutubi'llâhi'l-munzele, târeten bi'l-kırâe ve târeten bi'l-irtisâm, gloss:tilâvet, Allah'ın indirdiği kitapları izlemeye mahsustur; bazen okuyarak, bazen izine uyarak, source:"ت ل و,B002"}. İkinci ayetteki ayın işi, on üçüncü ayette elçinin getirdiği sözü izlemenin ölçüsü olur.

Elçinin adının kökü, salıvermeyi ve uzanmayı anlatır: {ar:أصل واحد يدل على الانبعاث والامتداد, tr:aslun vâhidun yedullu ale'l-inbi'âsi ve'l-imtidâd, gloss:harekete geçmeyi ve uzanmayı gösteren tek bir kök, source:"ر س ل,B001"}; {ar:الإرسال يقابل الإمساك, tr:el-irsâlu yukâbilu'l-imsâk, gloss:irsâl, tutmanın karşıtıdır, source:"ر س ل,B001"}. Elçi taşıdığı sözün adıyla da anılır: {ar:الرسول يقال للقول المتحمل وتارة لمتحمل القول والرسالة, tr:er-rasûlu yukâlu li'l-kavli'l-mutehammel, ve târeten li-mutehammili'l-kavli ve'r-risâle, gloss:resûl, taşınan söze de, sözü ve mesajı taşıyana da denir, source:"ر س ل,B002"}. Gönderme fiili ile on ikinci ayetin fiili aynı aileye bağlanır: {ar:ولقد بعثنا في كل أمة رسولا نحو أرسلنا رسلنا, tr:ve le-kad ba'asnâ fî kulli ummetin rasûlen, nahvu erselnâ rusulenâ, gloss:"her ümmete bir elçi ba'as ettik" sözü, "elçilerimizi irsâl ettik" gibidir, source:"ب ع ث,B002"}. Kur'an'daki karşılığı bir ayette göndermeyi, inkârı ve sonucu birlikte toplar: {ar:وَلَقَدْ بَعَثْنَا فِى كُلِّ أُمَّةٍۢ رَّسُولًا, tr:ve le-kad ba'asnâ fî kulli ummetin rasûlen, gloss:andolsun, her ümmete bir elçi gönderdik, source:16:36}. Aynı ayet şöyle biter: {ar:فَٱنظُرُوا۟ كَيْفَ كَانَ عَٰقِبَةُ ٱلْمُكَذِّبِينَ, tr:fe'nzurû keyfe kâne âkıbetu'l-mukezzibîn, gloss:yalanlayanların sonunun nasıl olduğuna bakın, source:16:36}. On ikinci ayette ise fiil, göndereni olmayan bir kalkış biçiminde gelir. Allah'ın göndermesine karşılık bir adam kendini gönderir.

Bu adam kavmin başındadır ve kavmin en bedbahtıdır: {ar:الشقوة خلاف السعادة, tr:eş-şikvetu hılâfu's-seâde, gloss:şikve, mutluluğun karşıtıdır, source:"ش ق و,B001"}. Kavim de onun peşine düşer. On dördüncü ayetteki "zenb" kelimesinin bir kolu bu izleyenlerin adıdır: {ar:ذنب الرجل أتباعه وأذناب القوم أتباع الرؤساء, tr:zenebu'r-raculi etbâ'uh, ve ezenâbu'l-kavmi etbâ'u'r-ruesâ', gloss:adamın kuyruğu, ona uyanlardır; kavmin kuyrukları, reislere uyanlardır, source:"ذ ن ب,B003"}. On beşinci ayetteki kelimenin kökü de birinin izinden gelmeyi anlatır: {ar:العاقب الذي يجيء في أثر صاحبه, tr:el-âkıbu'llezî yecîu fî eseri sâhibih, gloss:âkıb, arkadaşının izinden gelendir, source:"ع ق ب,B005"}. İzlenmesi gereken elçi ise yalanlanır: {ar:كذبته نسبته إلى الكذب, tr:kezzebtuhû: nesebtuhû ile'l-kezib, gloss:onu yalanladım, yani ona yalan isnat ettim, source:"ك ذ ب,B002"}. Kavmin elçiye cevabı söze karşı söz olarak gelir. Elçi "ve kâle", "dedi ki" diye konuşur: {ar:القول من النطق, tr:el-kavlu mine'n-nutk, gloss:kavl, konuşmadan gelir, source:"ق و ل,B001"}.

Kur'an Semûd'un bu reddini kendi sözleriyle aktarır. Bir insanı izlemeyi küçümserler: {ar:أَبَشَرًۭا مِّنَّا وَٰحِدًۭا نَّتَّبِعُهُۥٓ, tr:e beşeren minnâ vâhiden nettebi'uh, gloss:aramızdan tek bir insana mı uyacağız, source:54:24}. Ve onu yalancılıkla suçlarlar: {ar:بَلْ هُوَ كَذَّابٌ أَشِرٌۭ, tr:bel huve kezzâbun eşir, gloss:hayır, o şımarık bir yalancıdır, source:54:25}. Aynı sure, tek bir adamın ardına düşüldüğü sahneyle sürer: {ar:فَنَادَوْا۟ صَاحِبَهُمْ فَتَعَاطَىٰ فَعَقَرَ, tr:fe-nâdev sâhibehum fe-teâtâ fe-akar, gloss:arkadaşlarını çağırdılar; o da eline aldı ve ayaklarını biçti, source:54:29}. Elçiye uymayı reddedenler, kendi seçtikleri adamı izler. A'râf Suresi'nde de büyüklenen ileri gelenler müminlere sorar: {ar:أَتَعْلَمُونَ أَنَّ صَٰلِحًۭا مُّرْسَلٌۭ مِّن رَّبِّهِۦ, tr:e ta'lemûne enne Sâlihan murselun min rabbih, gloss:Salih'in Rabbi tarafından gönderildiğini mi biliyorsunuz, source:7:75}. Deveyi biçtikten sonra da alay ederler: {ar:إِن كُنتَ مِنَ ٱلْمُرْسَلِينَ, tr:in kunte mine'l-murselîn, gloss:eğer gönderilenlerdensen, source:7:77}. Şuarâ Suresi'nde de anlatım bir yalanlamayla açılır: {ar:كَذَّبَتْ ثَمُودُ ٱلْمُرْسَلِينَ, tr:kezzebet Semûdu'l-murselîn, gloss:Semûd gönderilenleri yalanladı, source:26:141}. Salih'in kendini tanıtması da şudur: {ar:إِنِّى لَكُمْ رَسُولٌ أَمِينٌۭ, tr:innî lekum rasûlun emîn, gloss:ben size gönderilmiş güvenilir bir elçiyim, source:26:143}. Neml Suresi bu izleyiciliğin içindeki bir çekirdekten bahseder: {ar:وَكَانَ فِى ٱلْمَدِينَةِ تِسْعَةُ رَهْطٍۢ, tr:ve kâne fi'l-medîneti tis'atu rahtin, gloss:şehirde dokuz kişilik bir çete vardı, source:27:48}. Elçinin son sözü, taşıdığı yükü teslim ettiğidir: {ar:لَقَدْ أَبْلَغْتُكُمْ رِسَالَةَ رَبِّى, tr:le-kad eblağtukum risâlete rabbî, gloss:Rabbimin mesajını size ulaştırdım, source:7:79}. Düz bir anlatım "yalanladılar" der. Bu imge ise iki izleme hattı çizer: biri gökte ve doğru, ay güneşin ardından gider; öteki yerde ve yanlış, kavim kendi en bedbahtının ardından gider. Birinde sıra korunur, ötekinde başa geçen, peşindekileri yıkıma götürür.

Kaynaklar: 91:2 تَلَىٰهَا ت ل و B001; 91:2 تَلَىٰهَا ت ل و B002; 91:11 كَذَّبَتْ ك ذ ب B002; 91:12 ٱنۢبَعَثَ ب ع ث B002; 91:12 أَشْقَىٰهَا ش ق و B001; 91:13 فَقَالَ ق و ل B001; 91:13 رَسُولُ ر س ل B001; 91:13 رَسُولُ ر س ل B002; 91:14 فَكَذَّبُوهُ ك ذ ب B002; 91:14 بِذَنۢبِهِمْ ذ ن ب B003; 91:15 عُقْبَٰهَا ع ق ب B005

## Buluşmalar

İlk buluşma sekizinci ayette olur. "Fucûr" kelimesi aynı kökten üç sahneyi bir arada tutar: geceyi yaran şafağı, bentten fırlayan suyu ve din perdesini yırtmayı. Gökte yarılma ışık getirir, nefiste ise koruyucu örtüyü yırtar ve bir taşkın başlatır. Takvâ aynı ayette hem bir örtüdür hem de bir settir. Tek bir kelime bu iki imgeyi birlikte taşır: örten ve alıkoyan. Böylece surenin başındaki düzenli nöbet nefsin içine taşınır. Gece güneşin üstünü sırası gelince örter ve sırası gelince açılır. Nefis ise ya kendi örtüsünü yerinde tutar ya da onu yırtıp taşar.

İkinci buluşma on ikinci ayetteki "inbe'ase" fiilindedir. Bu fiil üç imgeyi birden toplar. Fucûru tanımlayan atılıştır, deveyi köstekinden çözüp kaldırmanın sonucudur ve Allah'ın elçi gönderişinin eşi olan bir fiildir. Deve sürücüsünün dilinde biri kaldırır, deve kalkar. Bu ayette ise kaldıran yoktur. Adam kendi kendine, köstekinden kurtulmuş bir hayvan gibi kalkar ve Allah'ın gönderdiği deveye yönelir. Elçi gönderilmiştir, deve gönderilmiştir. Taşkın olan ise kendini gönderir.

Üçüncü buluşma, on dördüncü ayetten on beşinciye geçen bedenin arka ucudur. "Akr" topuk kirişini keser. O kirişin adı on beşinci ayetteki "ukbâ" kelimesinin kökündendir. Günahın adı olan "zenb" de hayvanın arka ucunun adıdır. Devenin imgesi ile suçun ardından gelen sonucun imgesi böylece aynı noktada birleşir. Kavim devenin arkasına vurur; karşılık da onların "arkalarından", yani günahlarının ardından gelir. Kova ile günahın aynı kökten gelmesi bunu ölçüye bağlar. Devenin su payını çiğneyenler kendi kova paylarını alırlar.

Dördüncü buluşma "sevvâ" fiilindedir. Bu fiil göğün ve nefsin bitirilişini Semûd'un yerle bir edilişine bağlar. Altıncı ayetteki yayılmış yer bu iki ucun arasında durur. Kavim ovaya saray kurmuştu. Yayılan yere kurulan sarayları yayılmış bir yer gibi dümdüz olur. Gökten yağan su, sürülen toprak ve büyüyen ekin bu yere bağlıdır. Hurmanın başını kesmeyi ve hiçbir şey bitirmeyen kumu anlatan "akr" fiili, kavmin tarlasını bir çorak yere çevirir.

Bu buluşmalar birlikte surenin hareketini taşır. Sure, her cismin yerini bildiği bir gökle başlar: ışık yayılır, ay onu izler, gündüz açar, gece örter. Ardından gök ve yerden bir ev kurulur ve aynı el nefsi bu evin üçüncü yapısı olarak düzenler. Nefse iki lokma yutturulur: hem yırtan ve taşan hem de örten ve alıkoyan. Dokuzuncu ve onuncu ayetler bu iki lokmanın sonucunu iki tarla gibi gösterir: biri sürülmüş ve büyümüş, öbürü gömülmüş. Semûd ise yanlış yolu seçer. Sınırı aşar, kendi en bedbahtının ardına düşer, gönderilen deveyi arkasından biçer. Karşılık gece gibi üstlerine kapanır ve evleri ile birlikte onları yayılmış bir yer gibi dümdüz eder. Sure, gece ile gündüzün nöbetleşmesini de adlandıran bir kelimeyle kapanır. Ama bu son nöbette, hükmün ardından gelecek ve onu geri çevirecek hiçbir şey yoktur.

