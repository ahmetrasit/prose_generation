Focus: 96:1. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/96_1/D.r13/context.md =====
# 96:1 — focus

ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ

Anchor translation (canonical reading, reference only):

Yaratan Rabbinin adıyla oku.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ٱقْرَأْ | قَرَأَ | ق ر ء | V |
| 2 | بِٱسْمِ | ٱسْم | س م و | P;N |
| 3 | رَبِّكَ | رَبّ | ر ب ب | N;PRON |
| 4 | ٱلَّذِى | ٱلَّذِى |  | REL |
| 5 | خَلَقَ | خَلَقَ | خ ل ق | V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 96 — full text (context; no pericope)

- 96:1 ◀ focus ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
- 96:2 خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
- 96:3 ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ
- 96:4 ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ
- 96:5 عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ
- 96:6 كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ
- 96:7 أَن رَّءَاهُ ٱسْتَغْنَىٰٓ
- 96:8 إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ
- 96:9 أَرَءَيْتَ ٱلَّذِى يَنْهَىٰ
- 96:10 عَبْدًا إِذَا صَلَّىٰٓ
- 96:11 أَرَءَيْتَ إِن كَانَ عَلَى ٱلْهُدَىٰٓ
- 96:12 أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ
- 96:13 أَرَءَيْتَ إِن كَذَّبَ وَتَوَلَّىٰٓ
- 96:14 أَلَمْ يَعْلَم بِأَنَّ ٱللَّهَ يَرَىٰ
- 96:15 كَلَّا لَئِن لَّمْ يَنتَهِ لَنَسْفَعًۢا بِٱلنَّاصِيَةِ
- 96:16 نَاصِيَةٍۢ كَٰذِبَةٍ خَاطِئَةٍۢ
- 96:17 فَلْيَدْعُ نَادِيَهُۥ
- 96:18 سَنَدْعُ ٱلزَّبَانِيَةَ
- 96:19 كَلَّا لَا تُطِعْهُ وَٱسْجُدْ وَٱقْتَرِب ۩


===== _commentary/v16/work/96_1/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق ر ء (root_001210) — identity root of ٱقْرَأْ (w1)

- **B001** toplamak ve bir araya getirmek — bir şeyi toplayıp parçalarını birleştirmek · insanların toplandığı yerleşim · konukların çevresinde toplandığı veya yiyeceğin toplandığı büyük kap · develerin su içmeye geldiği uzun yalak · sıkma düzeneğine benzeyen araç · kemiklerin birleştiği sırt · içindekileri toplayan kursak
  أصل صحيح يدل على جمع واجتماع (maqayis-v4;maqayis-v5)؛ قرأت الشيء قرآنا جمعته وضممت بعضه إلى بعض (sihah)؛ معنى قرآن معنى الجمع (tahdhib)؛ القراءة ضم الحروف والكلمات بعضها إلى بعض (mufradat)؛ الجرية أصلها قرية لأنها تقري الشيء أي تجمعه (maqayis-ibdal)
- **B002** okumak, okutmak ve birlikte okumak — kutsal metni, kitabı, şiiri veya anlatıyı okumak · düzenli ve güzel okuma · Kur'an; ayrıca okuma eylemi · okuyan kişi · ona Kur'an okumayı öğretmek veya okutmak · onunla karşılıklı okuyup çalışmak
  قرأت القرآن عن ظهر قلب أو نظرت فيه (ayn)؛ وقرأ فلان قراءة حسنة فالقرآن مقروء وأنا قارئ (ayn)؛ قرأت الكتاب قراءة وقرآنا ومنه سمي القرآن (sihah)؛ قرأت القرآن لفظت به مجموعا (tahdhib)؛ قرأت القرآن وأنا أقرؤه قرءا وقراءة وقرآنا (tahdhib)؛ أقرأت غيري أقرئه إقراء (tahdhib)؛ القراءة ضم الحروف والكلمات بعضها إلى بعض في الترتيل (mufradat)؛ قارأته دارسته (tahdhib;mufradat)
- **B003** aybaşı ya da arınma dönemi — aybaşı, arınma veya bunların dönemi · bekleme süresini belirleyen aybaşı ya da arınma dönemleri · kadının aybaşı olması, arınması veya döngü dönemine girmesi · kadının kanama görmesi veya aybaşı olması
  قرأت المرأة قرءا إذا رأت دما وأقرأت إذا حاضت (ayn)؛ القرء الحيض والقرء أيضا الطهر وهو من الأضداد (sihah)؛ القرء انقضاء الحيض وما بين الحيضتين (sihah)؛ الأقراء الحيض والأقراء الأطهار (tahdhib)؛ القرء اسم للوقت يصلح للحيض ويصلح للطهر (tahdhib)؛ اسم للدخول في الحيض عن طهر (mufradat)؛ القرء وقت يكون للطهر مرة وللحيض مرة (maqayis-v4;maqayis-v5)
- **B004** rahminde taşıyıp gebe olmak — dişi devenin rahminde yavru veya doğum artığı taşımak · dişi devenin gebe olması · gebe dişi deve
  فأما الناقة فإذا حملت قيل قرؤت قروءة (ayn)؛ القارئ الحامل (ayn)؛ ما قرأت هذه الناقة سلى قط وما قرأت جنينا (sihah)؛ لم تضم رحمها على ولد (sihah)؛ ما قرأت الناقة سلى قط وما قرأت ملقوحا قط (tahdhib)؛ لم تحمل علقة أي دما ولا جنينا (tahdhib)؛ ما قرأت هذه الناقة سلى كأنه يراد أنها ما حملت قط (maqayis-v4;maqayis-v5)
- **B005** vakit, yaklaşma veya gecikme — vakit · rüzgarların esme vakti · rüzgarın vaktine girmesi veya yıldızlara bağlanan yağmurun gecikmesi · ihtiyacın ya da işin yaklaşması veya gecikmesi · yolculuktan dönmek veya aileye yaklaşmak
  القارئ الوقت (sihah)؛ أقرأت الريح إذا دخلت في وقتها (sihah)؛ أقرأت النجوم إذا تأخر مطرها (sihah)؛ أقرأت حاجتك دنت (sihah)؛ هذا قارئ الرياح لوقت هبوبها (tahdhib)؛ أقرأت من سفري أي انصرفت وأقرأت من أهلي أي دنوت (tahdhib)؛ أقرأت حاجتك وأقرأ أمرك قال بعضهم دنا وقال بعضهم استأخر (tahdhib)؛ هبت الرياح لقارئها لوقتها (maqayis-v4;maqayis-v5)
- **B006** dindar okur; öğrenmeye yönelen kişi — dindar ve ibadete bağlı okur · ibadete bağlı okurlar veya çok dindar okur · kendini ibadete vermek, öğrenmek veya anlamak
  رجل قارئ عابد ناسك وفعله التقري والقراءة (ayn)؛ القراء الرجل المتنسك وقد تقرأ أي تنسك (sihah)؛ قرأت أي صرت قارئا ناسكا وتقرأت بهذا المعنى (tahdhib)؛ قال بعضهم تقرأت تفقهت (tahdhib)؛ تقرأت تفهمت (mufradat)
- **B007** esenlik dileğini iletmek [kalıp] — sana selamını iletti · sana selamını iletti; biçimin doğruluğu tartışmalıdır · selamımı alıp ilet
  فلان قرأ عليك السلام وأقراك السلام بمعنى (sihah)؛ اقرأ عليه السلام ولا يقال أقرئه السلام لأنه خطأ (tahdhib)؛ اقترئ مني السلام (tahdhib)
- **B008** yeni gelinen yöreye bağlı salgın etkisi [kalıp] — yeni gelinen yörenin zamanla geçen salgın etkisi
  القرأة بالكسر الوباء (sihah)؛ إذا قدمت بلادا فمكثت بها خمس عشرة فقد ذهبت عنك قرأة البلاد (sihah)؛ قرأة البلاد وأهل الحجاز يقولون قرة البلاد بغير همز (tahdhib)؛ إن مرضت بعد ذلك فليس من وباء البلاد (tahdhib)
- **B009** dişi devenin çiftleşme dönemi [kalıp] — erkek devenin, gebe kalıp kalmadığını anlamak için dişiyi bırakması · dişi devenin çiftleşme isteği veya dönemi
  استقرأ الجمل الناقة إذا تاركها لينظر ألقحت أم لا (sihah)؛ ضرب الفحل الناقة على غير قرء وقرء الناقة ضبعتها (tahdhib)؛ ما دامت الوديق في وداقها فهي في قرئها وإقرائها (tahdhib)
- **B010** biçime bağlı adlandırmalar — kadın köleyi aybaşı görene kadar gözetim altında tutmak · kadın kölenin gebe olmadığını aybaşı bekleyerek anlamak · onu hapsetmek
  دفع فلان جاريته إلى فلانة تقرئها أي تمسكها عندها حتى تحيض للاستبراء (sihah)؛ دفع فلان جاريته إلى فلانة تقرئها أي تمسكها عندها حتى تحيض للاستبراء (tahdhib)؛ قرأت الجارية استبرأتها بالقرء (mufradat)؛ أعتم فلان قراه وأقرأه أي حبسه (tahdhib)
- **B011** bir yolu veya örneği izlemek — tek bir yol, amaç veya izlenen yön · şiirin başka bir şiirin yöntem ve örneğine göre olması
  القرو كل شيء على طريقة واحدة (maqayis-v4;maqayis-v5)؛ رأيت القوم على قرو واحد (maqayis-v4;maqayis-v5)؛ القرو القصد تقول قروت وقريت إذا سلكت (maqayis-v4;maqayis-v5)؛ أقرأت في الشعر (tahdhib)؛ هذا الشعر على قرء هذا الشعر أي على طريقته ومثاله (tahdhib)
- **B012** bilgiyi toplayıp tanıklık eden kişi — tanık · yeryüzündeki tanıklar; bilgiyi toplayıp tanıklık edenler
  القارئة وهو الشاهد (maqayis-v4;maqayis-v5)؛ الناس قواري الله تعالى في الأرض هم الشهود (maqayis-v4;maqayis-v5)؛ ممكن أن يحمل هذا على ذلك القياس أي إنهم يقرون الأشياء حتى يجمعوها علما ثم يشهدون بها (maqayis-v4;maqayis-v5)
- **B013** hayvan varlığı veya bakmakla yükümlü olunanlar — deve ve küçükbaş hayvan varlığı veya bakmakla yükümlü olunan aile
  القرة المال من الإبل والغنم (maqayis-v4;maqayis-v5)؛ والقرة العيال (maqayis-v4;maqayis-v5)

## ق ر ء (root_001211) — identity root of ٱقْرَأْ (w1)

- **B001** biçime bağlı adlandırmalar — Kur'an; adı toplama anlamıyla ilişkilendirilmiş, fakat bu köken reddedilmiştir · Kur'an'ı sözlerini birleştirerek okumak · okuma ve sözleri söyleme · başkasına okutmak veya okumayı öğretmek · okuyan kişi · başkasına okutan veya okumayı öğreten kişi · dindar bir okur durumuna gelmek · dindar bir okur olmak veya öğrenmek · onunla karşılıklı okuyup çalışmak · birinden okumasını istemek; aktarımda açıklama verilmemiştir
  ومعنى قرآن معنى الجمع؛ قرأت القرآن لفظت به مجموعا؛ قرأت القرآن وأنا أقرؤه قرءا وقراءة وقرآنا؛ أقرأت غيري إقراء؛ قارأت فلانا مقارأة أي دارسته؛ تقرأت تفقهت
- **B002** özel adlandırma kümesi — aybaşı veya arınmanın gerçekleştiği dönem · aybaşı ve arınma dönemleri · kadının aybaşı veya arınma dönemine girmesi · rüzgarların esme vakti · dişi devenin çiftleşme isteği · yeni gelinen yörenin ilk günlerdeki salgın etkisi
  الأقراء الحيض والأطهار؛ القرء اسم للوقت؛ قارئ الرياح لوقت هبوبها؛ قرء الناقة ضبعتها؛ قرأة البلاد
- **B003** rahimde toplanıp taşınmak — kanın rahimde toplanması · dişi devenin doğum artığı taşımaması veya dışarı atmaması · yavruyu rahminde toplamamak, taşımamak veya dışarı atmamak · rahminde bir aybaşılık kan toplamamış olmak
  لم تجمع جنينا؛ لم تضطم رحمها على الجنين؛ لم تلقه؛ ما قرأت الناقة سلى قط أي ما طرحت وتأويله ما حملت؛ القرء اجتماع الدم في الرحم؛ ما ضمت رحمها على حيضة
- **B004** biçime bağlı adlandırmalar — 
  أقرأت من سفري أي انصرفت؛ أقرأت من أهلي أي دنوت؛ أقرأت حاجتك وأقرأ أمرك قال بعضهم دنا وقال بعضهم استأخر؛ أعتم فلان قراه وأقرأه أي حبسه
- **B005** şiiri başka bir şiirin örneğine göre kurmak — bu şiirin öteki şiirin yöntem ve örneğine göre olması · şiir bağlamında kullanmak; bağımsız anlamı açıklanmamıştır
  أقرأت في الشعر؛ هذا الشعر على قرء هذا الشعر أي على طريقته ومثاله؛ على قري هذا الشعر وغراره
- **B006** belirli kalıpla selam iletmek — ona selam ilet · selamımı alıp ilet · selam iletmek için yanlış sayılan biçim
  اقرأ عليه السلام ولا يقال أقرئه السلام؛ اقترىء مني السلام

## س م و (root_000745) — identity root of بِٱسْمِ (w2)

- **B001** fiziksel ya da toplumsal yükselme — yükselme, yücelme · yükselmek, yücelmek · bakışı yukarı yönelmek · toplumdaki yeri ve değeri yükselmiş olmak · gururla başını ve bakışını kaldırmak
  أصل يدل على العلو؛ سموت إذا علوت (maqayis)؛ سما الشيء يسمو سموا أي ارتفع (ayn)؛ السمو الارتفاع والعلو (sihah)؛ سما الشيء يسمو سموا وهو ارتفاعه، ويقال للحسيب والشريف قد سما (tahdhib)؛ أصله من السمو وهو الذي به رفع ذكر المسمى (mufradat)
- **B002** yükselerek uzaktan beliren görünüş — uzakta yükselip görünür olmak · bir şeyin yüksekte görünen gövdesi veya dış çizgisi · ayın ince yayının ufuktan yükselen görünüşü
  سما لي شخص ارتفع حتى استثبته؛ سماوة الهلال وكل شيء شخصه (maqayis)؛ سما لي شيء؛ سماوة الهلال شخصه إذا ارتفع عن الأفق شيئا (ayn)؛ سما لي شخص؛ سماوة كل شيء شخصه (sihah)؛ سما لي شيء؛ سماوته أي شخصه؛ سماوة الهلال شخصه (tahdhib)؛ السماوة الشخص العالي؛ وسما لي شخص (mufradat)
- **B003** erkek devenin dişi deve sürüsüne atılıp aralarına girmesi [kalıp] — erkek devenin dişi deve sürüsüne atılıp aralarına girmesi
  سما الفحل سطا على شوله سماوة (maqayis)؛ سما الفحل إذا تطاول على شوله (ayn;tahdhib)؛ سما الفحل إذا سطا على شوله سماوة (sihah)؛ سما الفحل على الشول سماوة لتخلله إياها (mufradat)
- **B004** üstteki gök veya örtü ve buna bağlı üstten gelen ya da üstte bulunan şeyler — gök, tavan veya bir şeyin üst yanı · yağmur · bulut · yağmurla çıkan veya yerden yükselen bitki · atın sırtı veya üst yanı · evin tavanı · her şeyin en üst yanı
  العرب تسمى السحاب سماء والمطر سماء؛ السماء سقف البيت وكل عال مطل سماء؛ يسموا النبات سماء (maqayis)؛ السماء كل ما علاك فأظلك؛ السماء المطر؛ السماء ظهر الفرس؛ سماوة البيت سقفه (sihah)؛ السماء سقف كل شيء وكل بيت؛ السماء السحاب؛ السماء المطر (tahdhib)؛ سماء كل شيء أعلاه؛ سمي المطر سماء؛ سمي النبات سماء (mufradat)
- **B005** ad, adlandırma ve ad ya da nitelik bakımından denklik — bir şeyi tanıtan ad · birine bir ad vermek veya onu o adla çağırmak · bir adı edinmek ve o adla anılmak · aynı adı taşıyan kişi, adaş · aynı adı veya niteliği hak eden denk · varlıkları tanıtan tekli veya birleşik sözler ve anlamlar
  أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى (maqayis)؛ الاسم أصل تأسيسه السمو؛ سميت وأسميت وتسميت (ayn)؛ سميت فلانا زيدا؛ هذا سمي فلان؛ الاسم مشتق من سموت لأنه تنويه ورفعة (sihah)؛ الاسم مشتق من السمو وهو الرفعة؛ تنويها على الدلالة على المعنى (tahdhib)؛ الاسم ما يعرف به ذات الشيء وأصله سمو؛ به رفع ذكر المسمى؛ سميا أي نظيرا له يستحق اسمه (mufradat)
- **B006** av için ıssız araziye çıkma ve buna bağlı avcı kullanımları — avlanmak için kır ve çöl arazisine çıkmak · avcılar · av hayvanını bulup avlamak üzere aramak · avcının sıcak zeminde beklerken giydiği koruyucu çorap
  خرج القوم للصيد في قفار الأرض وصحاريها قلت سموا وهم السماة أي الصيادون (ayn;tahdhib)؛ السماة الصيادون؛ سموا واستموا إذا خرجوا للصيد (sihah)؛ يستمي الوحش أي يطلبها؛ المسماة جورب الصياد (tahdhib)
- **B007** yarışma, övünerek boy ölçüşme ve karşı koyma — birbiriyle yarışmak ve karşı koymak · övünerek yarışma, boy ölçüşme ve karşı koyma · kimsenin kendisiyle yarışamadığı veya boy ölçüşemediği kişi
  فلان لا يسامى؛ تساموا أي تباروا؛ قد علا من ساماه (sihah)؛ معنى تساميها تباريها وتعارضها؛ المساماة المفاخرة (tahdhib)
- **B008** insanlar arasında yayılan iyi ün — insanlar arasında yayılan iyi ün veya iyi söz
  ذهب صيته في الناس وسماه، أي صوته في الخير لا في الشر (tahdhib)

## ر ب ب (root_000532) — identity root of رَبِّكَ (w3)

- **B001** sahip olup yönetme — Tanrı; sahip, buyruğu geçen yönetici veya düzenleyici · bir şeyin sahibi · evin sahibi veya ev işlerini yöneten kadın · sahiplik, egemenlik ve yönetim yetkisi
  الرب: الله تبارك وتعالى؛ ورب كل شيء مالكه (jamhara); رب كل شئ: مالكه؛ وقد قالوه في الجاهلية للملك؛ رببت القوم: سستهم (sihah); يكون الرب: المالك؛ ويكون الرب: السيد المطاع؛ ويكون الرب: المصلح (tahdhib); الرب مصدر مستعار للفاعل؛ لا يقال الرب مطلقا إلا لله؛ رب الدار ورب الفرس (mufradat); فالرب المالك والخالق والصاحب؛ والله جل ثناؤه الرب (maqayis)
- **B002** adım adım yetiştirip tamamlama — yapılan iyiliği eksiksiz kılmak · mülkü gözetip iyileştirmek · çocuğunu yetiştirmek · bir şeyi aşama aşama olgunlaştırma · yetiştirme anlamındaki değişmeli söyleyiş
  رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها (jamhara); رب الضيعة أي أصلحها وأتمها؛ رب فلان ولده؛ رباه (sihah); رب الشيء أي أصلحه؛ رب فلان الصنيعة إذا أتمها وأصلحها (tahdhib); التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام؛ ربه ورباه ورببه (mufradat); رب فلان ضيعته إذا قام على إصلاحها؛ رببت الصبي أربه (maqayis); ربته تربيتا إذا رببه (maqayis-rbt)
- **B003** Tanrı bilgisiyle yetiştiren bilgin — Tanrı bilgisine sahip bilgin ve öğretici
  الرباني: المتأله العارف بالله تعالى (sihah); الرباني: العالم؛ العلماء بالحلال والحرام؛ حكماء علماء؛ العالم المعلم الذي يغذو الناس بصغار العلوم (tahdhib); الرباني... يرب العلم؛ يرب نفسه بالعلم؛ منسوب إلى الرب (mufradat); الربي العارف بالرب (maqayis)
- **B004** büyük insan topluluğu — büyük topluluk; on bin kişilik topluluk · tek birlik hâlinde birleşmiş beş kabile · insanları toplayan kişi veya toplanma yeri
  الربي: واحد الربيين، وهم الألوف من الناس؛ الرباب خمس قبائل تجمعوا (sihah); الربيون: الألوف؛ الربيون: الجماعات الكثيرة؛ الربة: عشرة آلاف؛ الربان: الجماعة (tahdhib); يجوز أن يضم الربرب إلى الباب الثالث لتجمعه (maqayis)
- **B005** bakımla kurulan üvey aile bağı — üvey oğul veya bakım altında yetişen erkek çocuk · üvey kız veya bakım altında yetişen kız çocuk · bakıcı kadın; evde sütü için beslenen dişi hayvan · çocuğun bakımını üstlenen üvey baba veya üvey anne
  الراب: زوج الأم؛ الرابة: امرأة الأب؛ ربيب الرجل: ابن امرأته من غيره؛ الربيبة: الحاضنة (sihah); الربيب: ابن امرأة الرجل من غيره؛ ربيبة الرجل: بنت امرأته من غيره؛ راب ورابة (tahdhib); الراب والرابة بأحد الزوجين إذا تولى تربية الولد؛ الربيب والربيبة بذلك الولد (mufradat); ربيب الرجل ابن امرأته؛ الراب الذي يقوم على أمر الربيب (maqayis)
- **B006** koyu öz veya yağ tortusu — koyu meyve özü veya yağ tortusu · koyu özle işlenmiş veya güçlendirilmiş · koyu meyve özüyle hazırlanmış yiyecekler
  رب السمن والزيت: ثفله الأسود؛ سقاء مربوب إذا أصلح بالرب (jamhara); الرب: الطلاء الخاثر؛ سقاء مربوب؛ المرببات الأنبجات (sihah); رب فلان نحيه إذا جعل فيه الرب ومتنه به؛ نحي مربوب (tahdhib); رببت الأديم بالسمن، والدواء بالعسل، وسقاء مربوب (mufradat); هذا سقاء مربوب بالرب؛ الرب للعنب وغيره لأنه يرب به الشيء (maqayis)
- **B007** bir yerde kalıp sürme — bir yerde kalıp ayrılmamak · develerin sürekli kaldığı yer · bulut sürüp gitti · dişi deve erkeğe bağlandı · bir şeye yaklaşma
  رب بالمكان وأرب إذا أقام به (jamhara); مرب الإبل حيث لزمته؛ أربت الإبل؛ أربت الناقة؛ أربت الجنوب والسحابة أي دامت؛ الأرباب الدنو (sihah); أرب فلان بالمكان إذا أقام به فلم يبرحه؛ مرب الإبل أي حيث لزمته (tahdhib); أربت السحابة: دامت؛ أرب فلان بمكان كذا (mufradat); الأصل الآخر لزوم الشيء والإقامة عليه؛ أربت السحابة؛ الإرباب الدنو (maqayis)
- **B008** katmanlı asılı bulut kümesi — beyaz olabilen, katmanlı veya aşağıda asılı bulut
  الرباب: سحاب أبيض؛ الواحدة ربابة (sihah); الربابة: السحابة التي قد ركب بعضها بعضا؛ جمعها رباب (tahdhib); الرباب: السحاب، سمي بذلك لأنه يرب النبات (mufradat); سمي السحاب ربابا؛ السحاب المتعلق دون السحاب يكون أبيض ويكون أسود (maqayis)
- **B009** başlangıçtaki tazelik — yeni doğurmuş veya sütü için evde tutulan koyun · bir şeyin yeni ve taze dönemi · gençliğin ilk ve taze dönemi
  الربى: الشاة التي وضعت حديثا؛ قرب العهد بالولادة؛ بربانه أي بحدثانه وجدته وطراءته (sihah); الربى: أول الشباب؛ الربان من كل شيء: حدثانه؛ الشاة فهي ربى (tahdhib); الشاة الربي التي تحتبس في البيت للبن؛ التي وضعت حديثا (maqayis)
- **B010** kura oklarını toplayan kap — kura oklarını bir arada tutan deri veya bez kap
  الربابة: قطعة من أدم تجمع فيها القداح (jamhara); الربابة شبيهة بالكنانة تجمع فيها سهام الميسر؛ جماعة السهام (sihah); الربابة: جماعة السهام؛ الجلدة التي تجمع فيها السهام (tahdhib); لما يجمع فيه القدح ربابة (mufradat); الخرقة التي يجعل فيها القداح ربابة (maqayis)
- **B011** bağlayıcı söz ve güvence — tarafları birleştiren bağlayıcı söz veya sözleşme · sözleşmeye bağlı taraflar · bağlayıcı söz; söz gibi bağlayıcı vergi payı
  الربابة: العهد والمعاهدون أربة (jamhara); الربابة: العهد والميثاق؛ الأربة أهل الميثاق (sihah); الرباب: العهد؛ الرباب: العشور (tahdhib); العقد في موالاة الغير: الربابة (mufradat); الربابة وهو العهد؛ للمعاهدين أربة؛ الرباب العشور (maqayis)
- **B012** belirli bir yeşil bitki türü — belirli bir bitki, yumuşak ot veya küçük ağaç türü
  الربة: ضرب من الشجر أو النبت (jamhara); الربة بالكسر: ضرب من النبت، والجمع الربب (sihah); الربة: بقلة ناعمة؛ اسم لعدة من النبات لا تهيج في الصيف (tahdhib)
- **B013** bol ve toplanmış su — çok miktarda su; bazen bol tatlı su
  الربب، بالفتح: الماء الكثير، ويقال العذب (sihah); الربب وهو الماء الكثير سمي بذلك لاجتماعه (maqayis)
- **B014** yaban sığırı sürüsü — yaban sığırı sürüsü; bazen sığır veya deve topluluğu
  الربرب: القطيع من بقر الوحش (sihah); الربرب: جماعة البقر، وكذلك الإبل (tahdhib); الربرب القطيع من بقر الوحش؛ يجوز أن يضم إلى الباب الثالث لتجمعه (maqayis)
- **B015** azlık bildiren ilgeç — belirsiz adla azlık bildiren ilgeç; nice az · eylem önünde bazen veya kimi zaman · azlık ilgecinin sonuna ses eklenmiş ağız biçimi · belirsiz öğe eklenmiş azlık ilgeci biçimi
  رب: كلمة؛ ربما؛ ربت في معنى رب (jamhara); رب حرف خافض؛ ربما؛ ربت؛ ربه رجلا (sihah); رب من حروف المعاني؛ رب للتقليل؛ ربما؛ ربتما؛ تزيد في رب هاء (tahdhib); رب لاستقلال الشيء، ولما يكون وقتا بعد وقت، نحو ربما (mufradat); رب فكلمة تستعمل في الكلام لتقليل الشيء؛ ولا يعرف لها اشتقاق (maqayis)
- **B016** gereksinim, sıkı düğüm veya iyilik — gereksinim · sıkıca bağlanmış düğüm · iyilik ve başkasına yarar sağlama
  الربى: الحاجة؛ الربى: الرابة؛ الربى: العقدة المحكمة؛ الربى: النعمة والإحسان (tahdhib)
- **B017** gemicilerin başı — gemicilerin başı, kaptan
  رباني: رئيس الملاحين (tahdhib)

## خ ل ق (root_000434) — identity root of خَلَقَ (w5)

- **B001** ölçüp sınırlarını belirleme — ölçüp sınırlarını belirlemek · ölçüp biçme
  أحدهما تقدير الشيء؛ خلقت الأديم للسقاء إذا قدرته (maqayis)؛ خلقت الأديم قدرته (ayn)؛ خلقت الشيء إذا قدرته (jamhara)؛ الخلق: التقدير؛ خلقت الأديم إذا قدرته قبل القطع (sihah)؛ الخلق في كلام العرب على ضربين... والآخر التقدير؛ خلقت الأديم إذا قدرته وقسته (tahdhib)؛ الخلق أصله: التقدير المستقيم (mufradat)
- **B002** var etme ve ortaya çıkarma — yaratmak, var etmek · yaratan, var eden · yaratan, var eden; özellikle Tanrı için kullanılan ad · yaratılanlar, insanlar · yaratılmış varlık ya da varlıklar topluluğu
  الخالق الصانع (ayn)؛ الخلق مصدر خلق الله الخلق يخلقهم خلقا (jamhara)؛ هم خليقة الله (sihah)؛ الخالق والخلاق؛ الخلق ابتداع الشيء على مثال لم يسبق إليه (tahdhib)؛ يستعمل في إبداع الشيء من غير أصل ولا احتذاء؛ ويستعمل في إيجاد الشيء من الشيء (mufradat)
- **B003** tam ve dengeli dış biçim — dış görünüş ve beden yapısı · beden yapısı tam ve dengeli · yapısı tamamlanmış ve ölçülü · biçimi belirmiş ve oluşumu tamamlanmış
  رجل مختلق تام الخلق؛ المختلق من كل شيء ما اعتدل (maqayis)؛ رجل خليق أي تم خلقه؛ المختلق من كل شيء ما اعتدل (ayn)؛ رجل خليق ومختلق أي تام الخلق معتدل؛ مضغة مخلقة أي تامة الخلق (sihah)؛ رجل خليق إذا تم خلقه؛ مخلقة قد بدا خلقها وغير مخلقة لم تصور (tahdhib)؛ خص الخلق بالهيئات والأشكال والصور المدركة بالبصر (mufradat)
- **B004** huy ve iç karakter — huy, iç karakter · doğal huy ve yaradılıştan eğilim · iyi huyluluk ve iyi geçim · insanlarla huyuna göre geçinmek · bir huyu edinmeye veya öyle görünmeye çalışmak
  الخلق وهي السجية (maqayis)؛ الخليقة الخلق والخليقة الطبيعة (ayn)؛ الخلق: خلق الإنسان الذي طبع عليه؛ حسن الخلق؛ كريم الخليقة (jamhara)؛ الخليقة: الطبيعة؛ الخلقة: الفطرة؛ الخلق والخلق: السجية (sihah)؛ الطبيعة والخليقة والسليقة بمعنى واحد؛ خالق الناس بخلق حسن أي عاشرهم؛ الخلق الدين؛ الخلق المروءة (tahdhib)؛ خص الخلق بالقوى والسجايا المدركة بالبصيرة (mufradat)
- **B005** bir şeye yaraşır ve uygun olma — yaraşır, uygun · bunu yapması ne kadar beklenir · iyiliğe veya o işe çok uygun
  فلان خليق بكذا وأخلق به؛ هو ممن يقدر فيه ذلك (maqayis)؛ مخلقة للخير أي جدير به؛ خليق له أي جدير به؛ ما أخلقه أي ما أشبهه (ayn)؛ فلان خليق بكذا أي جدير به؛ مخلقة لذلك أي مجدرة له (sihah)؛ خليق بذاك أي حري؛ أخلق به أن يفعل؛ مخلقة للخير (tahdhib)؛ فلان خليق بكذا أي كأنه مخلوق فيه ذلك (mufradat)
- **B006** iyilikten düşen pay — pay, özellikle iyilikten düşen pay · iyilikten veya öte dünyadaki karşılıktan payı yok
  الخلاق النصيب لأنه قد قدر لكل أحد نصيبه (maqayis)؛ الخلاق النصيب من الحظ الصالح؛ ليس له خلاق أي ليس له رغبة في الخير ولا في الآخرة (ayn)؛ لا خلاق له أي لا نصيب له في الخير؛ الخلاق النصيب (jamhara)؛ الخلاق: النصيب؛ لا خلاق له في الآخرة (sihah)؛ الخلاق النصيب من الحظ الصالح؛ النصيب من الخير؛ الخلاق الدين (tahdhib)؛ الخلاق ما اكتسبه الإنسان من الفضيلة بخلقه (mufradat)
- **B007** uydurup yalan üretme — söz uydurmak ve çarpıtmak · zihninde yalan kurup ortaya atmak · yanlış kişiye bağlanmış, uydurma · uydurma öyküler ve asılsız anlatılar
  الخلق خلق الكذب وهو اختلاقه واختراعه وتقديره في النفس؛ وتخلقون إفكا (maqayis)؛ الخلق الكذب (ayn)؛ اختلق فلان كلاما إذا زوره؛ وتخلقون إفكا (jamhara)؛ خلق الإفك واختلقه وتخلقه أي افتراه؛ قصيدة مخلوقة أي منحولة (sihah)؛ تقدرون كذبا؛ أحاديث الخلق وهي الخرافات من الأحاديث المفتعلة؛ اختلاق (tahdhib)؛ كل موضع استعمل الخلق في وصف الكلام فالمراد به الكذب؛ إن هذا إلا اختلاق (mufradat)
- **B008** engebesiz ve düz olma — yüzeyini düzeltmek ve pürüzsüzleştirmek · engebesiz, düz ve yoğun · düz ve engebesiz kaya · alnın veya gözler arasının düz bölümü · yayılıp düzleşmek · düzeltilmiş ve yüzeyi engebesiz
  الأصل الثاني ملاسة الشيء؛ صخرة خلقاء أي ملساء؛ اخلولق السحاب استوى؛ رسم مخلولق إذا استوى بالأرض؛ السهم المصلح مخلق لأنه يصير أملس (maqayis)؛ الأخلق الأملس؛ صخرة خلقاء أي مصمتة؛ خليقاء الجبهة مستواها؛ خليقاء الغار الأعلى باطنه؛ اخلولق السحاب أي استوى (ayn)؛ خلقت الحبل والوتر وغيرهما تخليقا إذا ملسته؛ صخرة خلقاء ملساء؛ جبل أخلق؛ ضربه على خلقاء متنه (jamhara)؛ الأخلق الأملس المصمت؛ المخلق القدح إذا لين؛ صخرة خلقاء؛ اخلولق السحاب؛ اخلولق الرسم أي استوى بالأرض (sihah)؛ الأخلق الأملس من كل شيء؛ خليقاء الجبهة مستواها؛ خلقاء الغار الأعلى؛ سهم مخلق أملس مستو؛ الخلقة السحابة المستوية (tahdhib)
- **B009** kullanımdan yıpranıp eskime — kullanımdan yıpranıp tüyünü yitirmek · eski ve yıpranmış giysi · her yanı yıpranmış veya parçalanmış giysi · birine eski ve yıpranmış bir giysi vermek · istemekten yüzünü eskitmek
  أخلق الشيء وخلق إذا بلي؛ إذا أخلق املاس وذهب زئبره؛ ثوب خلق (maqayis)؛ خلق الثوب يخلق خلوقة أي بلي؛ أخلقني فلان ثوبه؛ ثوب أخلاق ممزق من جوانبه (ayn)؛ أخلق الثوب إخلاقا وخلق خلوقة وخلوقا فهو خلق؛ ثوب أخلاق (jamhara)؛ ملحفة خلق وثوب خلق أي بال؛ خلق الثوب أي بلى؛ أخلقته ثوبا إذا كسوته ثوبا خلقا؛ ثوب أخلاق (sihah)؛ خلق الثوب يخلق خلوقة وأخلق إخلاقا؛ أخلق فلان فلانا أي أعطاه ثوبا خلقا؛ ثوب أخلاق؛ جبة خلق (tahdhib)
- **B010** sürülen hoş koku karışımı — sürülen hoş koku karışımı · hoş koku karışımı sürmek veya sürünmek
  الخلوق معروف وهو الخلاق أيضا (maqayis)؛ الخلوق من الطيب؛ فعله التخليق والتخلق (ayn)؛ الخلوق ضرب من الطيب؛ خلقته أي طليته بالخلوق فتخلق به (sihah)؛ الخلوق من الطيب معروف؛ تخلقت المرأة بالخلوق وخلقت غيرها؛ خلق المسجد بالخلوق (tahdhib)
- **B011** su tutan kaya oyuğu veya yeni kuyu — su tutan kaya oyuğu veya yeni kuyu · yeni kazılmış kuyular
  الخلائق نقر في الصفا (ayn)؛ الخليقة نقر في صخرة يجتمع فيه ماء السماء (jamhara)؛ قلاتا تمسك ماء السحاب في صفاة خلقها الله فيها تسميها العرب الخلائق؛ دحلان خلقها الله في بطون الأرض؛ الخليقة البئر ساعة تحفر؛ الخلق الآبار الحديثات الحفر (tahdhib)
- **B012** kapalı üreme yolu — üreme yolu kapalı kadın
  امرأة خلقاء رتقاء لأنها مصمتة كالصفاة الخلقاء (ayn)؛ الخلق: المرأة الرتقاء (jamhara)؛ قيل للمرأة الرتقاء: خلقاء (sihah)؛ يقال للمرأة الرتقاء: خلقاء لأنها مصمتة كالصفاة الخلقاء (tahdhib)

## و س م (root_001650) — documented alternative for بِٱسْمِ: Kûfeli dilciler ve Sa‘leb; İbnü’l-Enbârî’nin aktarımı

- **B001** tanıtıcı fiziksel iz koyma, iz ve araç — bir şeyi tanıtıcı bir iz bırakarak işaretlemek · yakma veya kesme yoluyla bırakılmış tanıtıcı iz · tanınmayı sağlayan görünür işaret · üzerine tanıtıcı işaret konmuş · hayvan damgalamaya yarayan kızgın demir · kendine tanınacağı bir işaret edinmek · alt bölümü pirinçle süslenmiş zırh
  ووسمت الشيء وسما: أثرت فيه بسمة (maqayis;sihah)؛ الوسم أثر كي وبعير موسوم وسم بسمة يعرف بها من قطع أذن أو كي (ayn)؛ أثر كية، إما كية أو قطع في أذنه أو قرمة تكون علامة له (tahdhib)؛ الميسم المكواة أو الشيء الذي يوسم به الدواب (ayn;sihah;tahdhib)
- **B002** belirtiden karakter veya durum sezme — bir kimsede iyilik ya da kötülük belirtisi görüp niteliğini sezmek · duruma işaret eden belirtileri okuyup sonuç çıkaranlar · üzerinde iyilik ya da kötülük belirtisi bulunan
  الناظرين في السمة الدالة (maqayis)؛ توسمت فيه الخير والشر أي رأيت فيه أثرا (ayn)؛ فلان موسوم بالخير، وقد توسمت فيه الخير أي تفرست (sihah)؛ توسمت في فلان خيرا أي رأيت فيه أثرا منه، وتوسمت فيه الخير أي تفرست (tahdhib)
- **B003** toprağı bitkilendiren yılın ilk yağmuru — toprağı bitkilendiren yılın veya ilkbaharın ilk yağmuru · ilk yağmuru alıp etkisini taşıyan toprak · ilk yağmurun çıkardığı otu aramak
  الوسمى أول المطر لأنه يسم الأرض بالنبات (maqayis)؛ الوسمي أول مطر السنة يسم الأرض بالنبات، وأرض موسومة أصابها الوسمي (ayn)؛ الوسمي مطر الربيع الأول لأنه يسم الأرض بالنبات، والأرض موسومة (sihah)؛ سمي الوسمي من المطر وسميا لأنه يسم الأرض بالنبات فيصير فيها أثرا في أول السنة (tahdhib)
- **B004** belirlenmiş toplu buluşma zamanı ve yeri — kutsal ziyaret için belirlenmiş toplu buluşma zamanı ve yeri · eski Arap pazarlarının belirli toplanma zamanları ve yerleri · belirlenmiş toplu buluşmaya katılmak
  وسمى موسم الحاج موسما لأنه معلم يجتمع إليه الناس (maqayis)؛ موسم الحج موسما لأنه معلم يجتمع فيه وكذلك مواسم أسواق العرب (ayn;tahdhib)؛ موسم الحاج مجمعهم، سمي بذلك لأنه معلم يجتمع إليه (sihah)؛ وسم الناس: شهدوا الموسم (maqayis;sihah)
- **B005** kişide görünen yerleşik güzellik ve zarafet — güzellik; kişide görünen hoşluk · yüzü güzel ve hoş görünümlü · güzel ve hoş görünümlü kadın · üzerinde güzellik ve zarafet etkisi bulunan kadın · kişide görünen güzellik ve hoşluk · güzelleşmek ve hoş bir görünüş kazanmak · birini güzellikte geçmek
  فلانة ذات ميسم إذا كان عليها أثر الجمال، والوسامة الجمال (maqayis)؛ ذات ميسم وجمال وميسمها أثر الجمال فيها وهي وسيمة (ayn)؛ الميسم الجمال، وفلان وسيم أي حسن الوجه، ووسم الرجل وسامة ووساما (sihah)؛ فلانة لذات ميسم وميسمها أثر الجمال والعتق، والوسامة والميسم الحسن، والوسيم الثابت الحسن (tahdhib)
- **B006** yaprakları boya olarak kullanılan bitki — yaprakları boya olarak kullanılan bitki veya küçük ağaç
  الوسم والوسمة الواحدة شجرة ورقها خضاب (ayn;tahdhib)؛ الوسمة والعظلم يختضب به (sihah)

## ECHO ر ب و (root_000537) — for رَبِّكَ (w3): withheld observed target; not identity

- **B001** artmak veya yükselmek — bir şey arttı veya yükseldi · toprak suyla kabarıp arttı · yükselen veya fazla köpük · olağandan daha şiddetli yakalayış · onun üzerine çıktı veya üstünde bulundu
  ربا الجرح والأرض والمال وكل شيء يربو إذا زاد (ayn)؛ ربا الشيء يربو ربوا إذا ارتفع (jamhara)؛ ربا الشيء يربو ربوا أي زاد (sihah;tahdhib)؛ ربت أي زادت، وزبدا رابيا، وأخذة رابية (tahdhib;mufradat)؛ أربى عليه أي أشرف عليه (mufradat)
- **B002** yükselmiş arazi — yükselmiş arazi · çevresinden yüksek yer · arazideki yükselti
  الرابية ما ارتفع من الأرض، والربوة لغات أرض مرتفعة (ayn)؛ الربو والربوة والرباوة واحد وهو العلو من الأرض (jamhara)؛ الرابية الربو وهو ما ارتفع من الأرض، وكذلك الربوة (sihah)؛ الرباوة والرابية والرباة كل ذلك ما ارتفع من الأرض (tahdhib)؛ ربوة وربوة وربوة ورباوة، وسميت الربوة رابية (mufradat)
- **B003** belirli işlem biçimleriyle sınırlı anapara fazlalığı — belirli alışveriş veya borç biçimlerinde anaparayı aşan fazlalık · işlemdeki anapara fazlalığının özel adı veya bir söyleyiş biçimi · mal bu işlemde fazlalıkla arttı · anaparaya fazlalık eklenen işleme girdi
  ربا المال يربو في الربا أي يزداد، والربا في كتاب الله حرام، والربية هي الربا خاصة (ayn)؛ الربا في البيع، والربية لغة في الربا (sihah)؛ الربا ربوان، فالحرام كل قرض يؤخذ به أكثر منه (tahdhib)؛ الربا الزيادة على رأس المال، لكن خص في الشرع بالزيادة على وجه دون وجه (mufradat)
- **B004** soluğu yükselip sıkışmak — yüksek ve sıkışık soluma · soluğu sıkıştı · at koşu ya da ürkme yüzünden şişip soluksuz kaldı · soluğu yükselip tıkanmış
  ربا فلان أي أصابه نفس في جوفه ودابة بها ربو (ayn)؛ أصابه ربو من مشي أو عدو إذا علت أنفاسه (jamhara)؛ الربو النفس العالي، وربا الفرس إذا انتفخ من عدو أو فزع (sihah)؛ أخذها الربو وهو البهر (tahdhib)؛ الربو الانبهار سمي بذلك تصورا لتصعده (mufradat)
- **B005** besleyip büyütmek ve yetişmek — onu besleyip büyüttü · onların arasında yetişti · çocuğu besleyip büyüttü, çocuk gelişti
  ربيته وتربيته أي غذوته (ayn)؛ ربوت في بني فلان وربيت أي نشأت فيهم، وربيته تربية وتربيته أي غذوته، هذا لكل ما ينمي كالولد والزرع (sihah)؛ ربيت الولد فربا من هذا (mufradat)
- **B006** uyluk kökü ve iç yanlardaki iki çıkıntılı et parçası — uyluk kökü veya kasık eti · uyluk köklerinin iç yanlarındaki iki çıkıntılı et parçası
  الأربية أصل الفخذ، وهما أربيتان (sihah)؛ الأربيتان لحمتان ناتئتان في أصول الفخذين من باطن (mufradat)
- **B007** baba tarafından yakın hane halkının arasına gelmek [kalıp] — kendi topluluğundaki baba tarafından yakın hane halkının arasına geldi
  جاء فلان في أربية قومه، أي في أهل بيته من بني الأعمام ونحوهم، ولا تكون الأربية من غيرهم (sihah)

===== _commentary/v16/out/s096/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 96:1, and ## Buluşmalar) =====
## Rahimde toplanan, tutunan, biçim alan

Bu surenin kelimelerinin çoğu, ayetteki anlamlarının yanında aynı kök ailesinin başka bir sahnesini de duyurur. Bu aile imgesi kelimenin ayetteki anlamının yerine geçmez; onun yanında işitilir. Aşağıdaki her bölüm bu yan sahneleri ayetin kendi anlamına dayanarak okur.

İlk sahne bir rahimdir. Kan rahimde toplanır, rahim onun üzerine kapanır, toplanan şey tutunur ve gebelik kalıcı olur. Sonra biçim belirir, ardından doğum yaklaşır. Gebelik bazen de biçim belli olmadan düşer. Surenin ilk emri olan {ar:ٱقْرَأْ, tr:ikra, gloss:oku, source:96:1} kelimesinin kökü, okumanın yanında dişinin rahminde bir şey taşımasını da adlandırır: {ar:ما قرأت الناقة سلى قط … لم تحمل علقة أي دما ولا جنينا, tr:mâ kara'eti'n-nâkatu selan katt … lem tahmil ʿalakaten ey demen ve lâ cenînen, gloss:dişi deve hiç yavru zarı taşımadı … yani hiç kan pıhtısı ya da cenin taşımadı, source:"ق ر ء,B004"}. Bu söz okumanın kökünü, ikinci ayetin {ar:عَلَقٍ, tr:alak, gloss:tutunan pıhtı, source:96:2} kelimesiyle aynı cümlede birleştirir. Aynı kök, rahmin temizlik ve kanama dönemlerini de adlandırır: {ar:القرء الحيض والقرء أيضا الطهر, tr:el-kur'u'l-hayzu ve'l-kur'u eyzan et-tuhr, gloss:kur' hem âdet hem temizlik dönemidir, source:"ق ر ء,B003"}. Kurân bu kelimeyi tam bu anlamda kullanır ve hemen arkasından rahimde yaratılanı anar. Boşanmış kadınlar {ar:ثَلَٰثَةَ قُرُوٓءٍ, tr:selâsete kurû', gloss:üç dönem, source:2:228} bekler ve {ar:مَا خَلَقَ ٱللَّهُ فِىٓ أَرْحَامِهِنَّ, tr:mâ halaka'llâhu fî erhâmihinn, gloss:Allah'ın rahimlerinde yarattığını, source:2:228} gizlemezler. Böylece okumanın kökü ile yaratmanın fiili aynı ayette rahimde buluşur.

İkinci ayet bu sahnenin başlangıcını adlandırır. Alak hem donmuş kan parçasıdır, {ar:العلق الدم الجامد والقطعة منه علقة, tr:el-ʿalaku'd-demu'l-câmid, gloss:alak donmuş kandır, bir parçasına alaka denir, source:"ع ل ق,B003"}, hem de gebeliğin tutunmasıdır, {ar:علقت المرأة حبلت, tr:ʿalikati'l-mer'e: hebilet, gloss:kadın tutundu, yani gebe kaldı, source:"ع ل ق,B009"}. Birinci ve ikinci ayetlerdeki {ar:خَلَقَ, tr:halaka, gloss:yarattı, source:96:2} fiilinin ailesinde biçimi belirmiş cenin vardır: {ar:مخلقة قد بدا خلقها وغير مخلقة لم تصور, tr:muhallaka kad bedâ halkuhâ ve gayru muhallaka lem tusavver, gloss:biçimlenmiş, yani yaratılışı belirmiş; biçimlenmemiş, yani henüz şekil verilmemiş, source:"خ ل ق,B003"}. Kurân bu aşamaları yeniden diriliş için kanıt olarak sayar. Allah insanlara, dirilişten şüphe ediyorlarsa, onları {ar:مِنْ عَلَقَةٍ ثُمَّ مِن مُّضْغَةٍ مُّخَلَّقَةٍ وَغَيْرِ مُخَلَّقَةٍ, tr:min ʿalakatin summe min mudgatin muhallakatin ve gayri muhallaka, gloss:bir pıhtıdan, sonra biçimlenmiş ve biçimlenmemiş bir çiğnemlik etten, source:22:5} yarattığını söyler ve ekler: {ar:وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ, tr:ve nukirru fi'l-erhâmi mâ neşâ', gloss:dilediğimizi rahimlerde durdururuz, source:22:5}. Başka bir yerde aşamalar birbirine yaratma fiiliyle bağlanır: {ar:فَخَلَقْنَا ٱلْعَلَقَةَ مُضْغَةً, tr:fe halaknâ'l-ʿalakate mudga, gloss:pıhtıyı bir çiğnemlik et olarak yarattık, source:23:14}. Dirilişi inkâr eden insana da aynı soru sorulur: {ar:ثُمَّ كَانَ عَلَقَةً فَخَلَقَ فَسَوَّىٰ, tr:summe kâne ʿalakaten fe halaka fe sevvâ, gloss:sonra bir pıhtı oldu, O da yarattı ve düzenledi, source:75:38}. Biçimi verenin kim olduğu da açıkça söylenir: {ar:يُصَوِّرُكُمْ فِى ٱلْأَرْحَامِ, tr:yusavvirukum fi'l-erhâm, gloss:sizi rahimlerde biçimlendirir, source:3:6}.

Surenin üçüncü ve sekizinci ayetlerinde de geçen {ar:رَبِّكَ, tr:rabbike, gloss:Rabbin, source:96:1} kelimesinin ailesi bu sahneye bir işleyiş ekler: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye: inşâu'ş-şey'i hâlen fe hâlen ilâ haddi't-temâm, gloss:bir şeyi hal hal, tamamlanacağı sınıra kadar geliştirmek, source:"ر ب ب,B002"}. Yaratan Rab, pıhtıyı aşama aşama tamamlanmaya götürendir. Beşinci ayetin {ar:مَا لَمْ يَعْلَمْ, tr:mâ lem yaʿlem, gloss:bilmediğini, source:96:5} ifadesi bu doğuma bağlanır, çünkü doğan insan hiçbir şey bilmez: {ar:أَخْرَجَكُم مِّنۢ بُطُونِ أُمَّهَٰتِكُمْ لَا تَعْلَمُونَ شَيْـًٔا, tr:ahraceküm min butûni ummehâtikum lâ taʿlemûne şey'â, gloss:sizi annelerinizin karınlarından hiçbir şey bilmez halde çıkardı, source:16:78}. Sekizinci ayetin {ar:ٱلرُّجْعَىٰٓ, tr:er-ruc'â, gloss:dönüş, source:96:8} kelimesinin ailesinde ise sahnenin tersi vardır: {ar:إذا ألقت الناقة حملها قبل أن يستبين خلقه قيل قد رجعت, tr:izâ elkati'n-nâkatu hamlehâ kable en yestebîne halkuhû kîle kad racaʿat, gloss:dişi deve yükünü biçimi belli olmadan düşürünce "döndü" denir, source:"ر ج ع,B013"}. Bu kalıp ifade dönüşü ve biçimi tek cümlede birleştirir. Kurân yaratılış ile geri döndürmeyi bir sahnede birlikte anlatır. İnsan {ar:يَخْرُجُ مِنۢ بَيْنِ ٱلصُّلْبِ وَٱلتَّرَآئِبِ, tr:yahrucu min beyni's-sulbi ve't-terâ'ib, gloss:bel ile göğüs kemikleri arasından çıkan, source:86:7} bir sudan yaratılmıştır ve {ar:إِنَّهُۥ عَلَىٰ رَجْعِهِۦ لَقَادِرٌ, tr:innehû ʿalâ rac'ihî le kâdir, gloss:O onu geri döndürmeye elbette gücü yetendir, source:86:8}. Surenin sonundaki iki kelimenin ailesinde doğumun yaklaşması da vardır: onuncu ayetin fiili için {ar:أصلت الناقة … إذا وقع ولدها في صلاها وقرب نتاجها, tr:aslati'n-nâka … izâ vakaʿa veleduhâ fî salâhâ, gloss:dişi devenin yavrusu sağrısına indi ve doğumu yaklaştı, source:"ص ل و,B005"}, son ayetin emri için {ar:أقربت المرأة إذا قرب ولادها, tr:akrabeti'l-mer'e, gloss:kadının doğumu yaklaştı, source:"ق ر ب,B012"}. Bu iki aile anlamı uzak birer yankıdır, ama kuruluşları ortadadır.

Bu sahne, insanın düz bir anlatımla verilemeyecek bir yanını gösterir: okunması emredilen kişi, kendisi de toplanmış, tutunmuş ve biçimlendirilmiş bir varlıktır. Surenin dönüş ayeti, rahimden çıkan hayatı tekrar başladığı yere bağlar.

Kaynaklar: 96:1 ٱقْرَأْ ق ر ء B004; 96:1 ٱقْرَأْ ق ر ء B003; 96:2 عَلَقٍ ع ل ق B003; 96:2 عَلَقٍ ع ل ق B009; 96:1 خَلَقَ خ ل ق B003; 96:1 رَبِّكَ ر ب ب B002; 96:5 يَعْلَمْ ع ل م B001; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B013; 96:10 صَلَّىٰٓ ص ل و B005; 96:19 وَٱقْتَرِب ق ر ب B012

## Harfleri toplamak: okuma, öğretme, kalem

Okumak, parçaları bir araya getirip bütün olarak söylemektir: {ar:قرأت الشيء قرآنا جمعته وضممت بعضه إلى بعض, tr:kara'tu'ş-şey'e kur'ânen: cemaʿtuhû ve damemtu baʿdahû ilâ baʿd, gloss:bir şeyi okudum, yani topladım ve parçalarını birbirine kattım, source:"ق ر ء,B001"}; {ar:القراءة ضم الحروف والكلمات بعضها إلى بعض, tr:el-kırâ'e: dammu'l-hurûfi ve'l-kelimât, gloss:okuma harfleri ve kelimeleri birbirine katmaktır, source:"ق ر ء,B001"}. Aynı kök, ezberden ya da sayfadan yüksek sesle söylemeyi ve başkasına okutmayı da kapsar: {ar:أقرأت غيري أقرئه إقراء, tr:akra'tu gayrî, gloss:başkasına okuttum, source:"ق ر ء,B002"}. Birinci ayetteki emir ile üçüncü ayetteki tekrarı bu toplama işini iki kez başlatır. Kurân aynı işi vahiy anında Peygamber'e anlatır: dilini acele ile oynatmamasını söyledikten sonra {ar:إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ, tr:inne ʿaleynâ cemʿahû ve kur'ânehû, gloss:onu toplamak ve okutmak bize aittir, source:75:17}, {ar:فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ, tr:fe izâ kara'nâhu fettebiʿ kur'ânehû, gloss:onu okuduğumuzda sen okunuşunu izle, source:75:18}. Toplamak ile okumak burada yan yana durur. Okutan da Allah'tır: {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:senukri'uke fe lâ tensâ, gloss:sana okutacağız, unutmayacaksın, source:87:6}. Kurân'ın parça parça okunmak üzere ayrıldığı da söylenir: {ar:وَقُرْءَانًا فَرَقْنَٰهُ لِتَقْرَأَهُۥ عَلَى ٱلنَّاسِ عَلَىٰ مُكْثٍ, tr:ve kur'ânen ferakna-hu li takra'ehû ʿale'n-nâsi ʿalâ muks, gloss:onu insanlara ağır ağır okuyasın diye bölümlere ayırdığımız bir Kurân, source:17:106}.

Dördüncü ve beşinci ayetler öğretmeyi getirir. {ar:عَلَّمَ, tr:ʿalleme, gloss:öğretti, source:96:4} zihni anlamları kavramaya uyandırmaktır: {ar:التعليم تنبيه النفس لتصور المعاني, tr:et-taʿlîm tenbîhu'n-nefsi li tasavvuri'l-meʿânî, gloss:öğretmek, nefsi anlamları kavramaya uyandırmaktır, source:"ع ل م,B001"}. Öğretme {ar:بِٱلْقَلَمِ, tr:bi'l-kalem, gloss:kalemle, source:96:4} olur: {ar:القلم الذي يكتب به, tr:el-kalemu'llezî yuktebu bih, gloss:kalem, onunla yazılan şeydir, source:"ق ل م,B003"}. Kalem, toplanıp söyleneni kalıcı kılar. Kurân kaleme yemin eder: {ar:نٓ وَٱلْقَلَمِ وَمَا يَسْطُرُونَ, tr:nûn, ve'l-kalemi ve mâ yesturûn, gloss:Nun. Kaleme ve yazdıklarına andolsun, source:68:1}. Allah'ın yazmayı öğrettiği borç sözleşmesi ayetinde de söylenir: {ar:وَلَا يَأْبَ كَاتِبٌ أَن يَكْتُبَ كَمَا عَلَّمَهُ ٱللَّهُ, tr:ve lâ ye'be kâtibun en yektube kemâ ʿallemehu'llâh, gloss:yazıcı, Allah'ın ona öğrettiği gibi yazmaktan kaçınmasın, source:2:282}. Kalemin gücü, Allah'ın sözlerinin yanında küçülür: {ar:وَلَوْ أَنَّمَا فِى ٱلْأَرْضِ مِن شَجَرَةٍ أَقْلَٰمٌ, tr:ve lev ennemâ fi'l-ardı min şeceratin aklâm, gloss:yeryüzündeki ağaçlar kalem olsa, source:31:27}, deniz mürekkep olsa bile o sözler tükenmez.

Surenin ilk beş ayetindeki sıra Kurân'da bir kez daha geçer: {ar:عَلَّمَ ٱلْقُرْءَانَ, tr:ʿallemel-kur'ân, gloss:Kurân'ı öğretti, source:55:2}, {ar:خَلَقَ ٱلْإِنسَٰنَ, tr:halaka'l-insân, gloss:insanı yarattı, source:55:3}, {ar:عَلَّمَهُ ٱلْبَيَانَ, tr:ʿallemehu'l-beyân, gloss:ona açıklamayı öğretti, source:55:4}. Öğretilen şeyin insanın bilmediği şey olduğu da söylenir: {ar:وَيُعَلِّمُكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ, tr:ve yuʿallimukum mâ lem tekûnû taʿlemûn, gloss:size bilmediğinizi öğretir, source:2:151}.

Rab kelimesinin ailesinde öğreten de vardır: {ar:الرباني… العالم المعلم الذي يغذو الناس بصغار العلوم, tr:er-rabbânî … el-ʿâlimu'l-muʿallim, gloss:rabbânî, insanları küçük bilgilerden başlayarak besleyen bilgin öğretmendir, source:"ر ب ب,B003"}. Üçüncü ayetin {ar:ٱلْأَكْرَمُ, tr:el-ekrem, gloss:en cömert, source:96:3} sıfatı da öğretme ile bağlantılıdır. Kurân bu kökü kendisi için kullanır: {ar:إِنَّهُۥ لَقُرْءَانٌ كَرِيمٌ, tr:innehû le kur'ânun kerîm, gloss:o elbette değerli bir Kurân'dır, source:56:77}; sayfaları {ar:فِى صُحُفٍ مُّكَرَّمَةٍ, tr:fî suhufin mukerrame, gloss:değerli sayfalardadır, source:80:13} ve {ar:كِرَامٍۭ بَرَرَةٍ, tr:kirâmin berara, gloss:değerli ve iyi, source:80:16} yazıcıların elindedir. Aynı köke, aldanmış insana sorulan soruda da rastlanır: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ مَا غَرَّكَ بِرَبِّكَ ٱلْكَرِيمِ, tr:yâ eyyuhe'l-insânu mâ garraka bi rabbike'l-kerîm, gloss:ey insan, seni cömert Rabbine karşı ne aldattı, source:82:6}.

Okuyucu, toplayan ve şahitlik edendir: {ar:يقرون الأشياء حتى يجمعوها علما ثم يشهدون بها, tr:yakrûne'l-eşyâ'e hattâ yecmeʿûhâ ʿilmen summe yeşhedûne bihâ, gloss:şeyleri bilgi olarak toplayana dek izlerler, sonra onlara şahitlik ederler, source:"ق ر ء,B012"}. Aynı kökte okuyucu kulluk edendir: {ar:رجل قارئ عابد ناسك, tr:raculun kâri'un ʿâbidun nâsik, gloss:okuyucu, kulluk eden, ibadet eden adam, source:"ق ر ء,B006"}. Bu, onuncu ayetteki {ar:عَبْدًا, tr:ʿabden, gloss:bir kulu, source:96:10} kelimesine ve son ayetin secdesine ulaşır. Kurân okumayı secdeyle birleştirir: inkârcılar için {ar:وَإِذَا قُرِئَ عَلَيْهِمُ ٱلْقُرْءَانُ لَا يَسْجُدُونَ, tr:ve izâ kuri'e ʿaleyhimu'l-kur'ânu lâ yescudûn, gloss:onlara Kurân okununca secde etmezler, source:84:21}; daha önce bilgi verilenler için {ar:إِذَا يُتْلَىٰ عَلَيْهِمْ يَخِرُّونَ لِلْأَذْقَانِ سُجَّدًا, tr:izâ yutlâ ʿaleyhim yahirrûne li'l-ezkâni succedâ, gloss:onlara okununca çeneleri üstüne secdeye kapanırlar, source:17:107}. Sekizinci ayetteki dönüş kelimesinin ailesinde okuyan sesin kendi üzerine dönmesi de vardır: {ar:الترجيع ترديد الصوت باللحن في القراءة, tr:et-terciʿ terdîdu's-savti bi'l-lahni fi'l-kırâ'e, gloss:tercî, okumada sesi ezgiyle tekrar tekrar döndürmektir, source:"ر ج ع,B007"}. Aynı ilk emir, hesap gününde her nefse kendi kaydı için verilir: {ar:ٱقْرَأْ كِتَٰبَكَ كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًا, tr:ikra' kitâbeke kefâ bi nefsike'l-yevme ʿaleyke hasîbâ, gloss:kitabını oku, bugün hesap sorucu olarak sana kendin yetersin, source:17:14}.

Bu sahne okumayı bir eylemler zinciri olarak gösterir: toplamak, söylemek, öğretmek, yazıyla sabitlemek ve sonunda secdeye varmak.

Kaynaklar: 96:1 ٱقْرَأْ ق ر ء B001; 96:1 ٱقْرَأْ ق ر ء B002; 96:1 ٱقْرَأْ ق ر ء B012; 96:1 ٱقْرَأْ ق ر ء B006; 96:4 عَلَّمَ ع ل م B001; 96:4 بِٱلْقَلَمِ ق ل م B003; 96:1 رَبِّكَ ر ب ب B003; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B007; 96:3 ٱلْأَكْرَمُ ك ر م B001

## Yontulan kamış, düzeltilen ok, kaygan kaya

Bu bölümdeki sahne sert malzeme üzerinde çalışan bir zanaatkârın sahnesidir. Zanaatkâr önce ölçer, sonra keser, yontar ve düzeltir. Birinci ve ikinci ayetlerdeki yaratma fiilinin kökü bu ilk adımı adlandırır: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktu'l-edîme izâ kaddertuhû kable'l-katʿ, gloss:deriyi kesmeden önce ölçtüğümde onu "halk" ettim, source:"خ ل ق,B001"}; {ar:الخلق أصله: التقدير المستقيم, tr:el-halku asluhu't-takdîru'l-mustakîm, gloss:halkın aslı doğru ölçmektir, source:"خ ل ق,B001"}. Kurân yaratmayı ölçmeyle yan yana koyar: {ar:مِن نُّطْفَةٍ خَلَقَهُۥ فَقَدَّرَهُۥ, tr:min nutfetin halakahû fe kaddarahû, gloss:onu bir damladan yarattı ve ölçüsünü verdi, source:80:19}.

Dördüncü ayetin kalemi, yontma işinden adını alır: {ar:أصل القلم القص من الشيء الصلب كالظفر وكعب الرمح والقصب, tr:aslu'l-kalemi'l-kassu mine'ş-şey'i's-sulb, gloss:kalemin aslı, tırnak, mızrak boğumu ve kamış gibi sert bir şeyden kesip almaktır, source:"ق ل م,B001"}; {ar:إنما سمي قلما لأنه قلم مرة بعد مرة, tr:innemâ summiye kalemen li ennehû kulime merraten baʿde merra, gloss:kalem denmesi, tekrar tekrar yontulduğu içindir, source:"ق ل م,B003"}. Öğreten Rab'bin aracı, defalarca yontulmuş bir kamıştır.

Yaratma kökü düzeltmeyi de adlandırır: {ar:السهم المصلح مخلق لأنه يصير أملس, tr:es-sehmu'l-muslahu muhallak, gloss:düzeltilmiş ok "muhallak"tır, çünkü pürüzsüz hale gelir, source:"خ ل ق,B008"}; {ar:المخلق القدح إذا لين, tr:el-muhallaku'l-kıdhu izâ luyyin, gloss:muhallak, yumuşatılmış kura okudur, source:"خ ل ق,B008"}. Kalem kökü de aynı nesneye varır: {ar:الأقلام ها هنا القداح جعلوا عليها علامات على جهة القرعة, tr:el-aklâmu hâhunâ el-kıdâh, gloss:buradaki kalemler, üzerine kura için işaret konmuş oklardır, source:"ق ل م,B004"}. Kurân bu nesneyi Meryem'in bakımı sahnesinde anar. Allah Peygamber'e, kendisinin orada olmadığı bir anı bildirir: {ar:إِذْ يُلْقُونَ أَقْلَٰمَهُمْ أَيُّهُمْ يَكْفُلُ مَرْيَمَ, tr:iz yulkûne aklâmehum eyyuhum yekfulu Meryem, gloss:Meryem'i hangisi üstlenecek diye kalemlerini atarlarken, source:3:44}. Cahiliye kura oklarıyla kısmet aramak ise yasaklanır: {ar:وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ ذَٰلِكُمْ فِسْقٌ, tr:ve en testaksimû bi'l-ezlâm, zâlikum fisk, gloss:fal oklarıyla pay aramanız da haram kılındı; bu yoldan çıkmaktır, source:5:3}. Bu okların toplandığı torbanın adı da rab kökündendir: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-rabâbe, gloss:rabâbe, kumar oklarının toplandığı sadağa benzer bir torbadır, source:"ر ب ب,B010"}.

Pürüzsüzleştirme sahnesinin bir de kaya hali vardır. Yaratma kökü kaygan kayayı adlandırır: {ar:صخرة خلقاء أي ملساء, tr:sahratun halkâ', gloss:halkâ kaya, yani kaygan kaya, source:"خ ل ق,B008"}. Altıncı ayetin {ar:لَيَطْغَىٰٓ, tr:le yatgâ, gloss:azar, source:96:6} fiilinin kökü de aynı kayayı adlandırır: {ar:الطغية الصفاة الملساء, tr:et-tugye es-safâtu'l-melsâ', gloss:tugye, kaygan kaya düzlüğüdür, source:"ط غ ي,B005"}. Kartalın pençesi bu kayada tutunamaz. Bu kayanın oyuklarında yağmur suyu birikir: {ar:الخليقة نقر في صخرة يجتمع فيه ماء السماء, tr:el-halîka nakrun fî sahra, gloss:halîka, kayada gök suyunun biriktiği oyuktur, source:"خ ل ق,B011"}. Böylece aynı kök hem ustaca işlenmiş nesneyi hem de üzerine tutunulamayan kayayı adlandırır. Azan insan, yontulup düzeltilmiş olduğunu unutup kendini hiçbir şeyin tutamadığı kaygan bir doruk sanır.

Kaynaklar: 96:1 خَلَقَ خ ل ق B001; 96:4 ٱلْقَلَمِ ق ل م B001; 96:4 ٱلْقَلَمِ ق ل م B003; 96:1 خَلَقَ خ ل ق B008; 96:4 ٱلْقَلَمِ ق ل م B004; 96:1 رَبِّكَ ر ب ب B010; 96:6 لَيَطْغَىٰٓ ط غ ي B005; 96:2 خَلَقَ خ ل ق B011

## Ad, iz, işaret

Bir şey, üzerine yükseltilen ya da içine bastırılan bir işaretle tanınır. Sure {ar:بِٱسْمِ, tr:bismi, gloss:adıyla, source:96:1} diye başlar. Ad kelimesinin kökü yüksekliktir: {ar:أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى, tr:aslu ismin sumuvvun ve huve mine'l-ʿuluvv, gloss:ismin aslı yükselmedir; çünkü anlamı ortaya çıkarır ve ona işaret eder, source:"س م و,B005"}. Kayıtlı bir başka türetmeye göre ise ad bir damgadır: {ar:ووسمت الشيء وسما: أثرت فيه بسمة, tr:ve vesemtu'ş-şey'e vesmen, gloss:bir şeye damga vurarak iz bıraktım, source:"و س م,B001"}. İlk anlamda ad, yükseğe kaldırılan bir işarettir; ikinci anlamda bir şeye bastırılan izdir. Kurân Rab'bin adını yükseklikle ve yaratmayla birlikte anar: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-aʿlâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1}, {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî halaka fe sevvâ, gloss:ki yarattı ve düzenledi, source:87:2}. Bu yapı surenin ilk ayetine çok yakındır. Adı anmak secdeye de bağlanır: {ar:وَٱذْكُرِ ٱسْمَ رَبِّكَ بُكْرَةً وَأَصِيلًا, tr:vezkuri'sme rabbike bukraten ve asîlâ, gloss:sabah akşam Rabbinin adını an, source:76:25}, {ar:وَمِنَ ٱلَّيْلِ فَٱسْجُدْ لَهُۥ, tr:ve mine'l-leyli fescud leh, gloss:gecenin bir kısmında O'na secde et, source:76:26}.

Öğretme kökü de işarettir: {ar:أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره, tr:aslun sahîhun vâhidun yedullu ʿalâ eserin bi'ş-şey', gloss:bir şeyi diğerlerinden ayıran bir ize delalet eden tek bir asıl, source:"ع ل م,B002"}. Bu kök sancağı ve kumaşın kenar nakışını da adlandırır: {ar:العلم الراية, tr:el-ʿalemu'r-râye, gloss:alem sancaktır, source:"ع ل م,B002"}. Görme kökü de bu sancağa varır: {ar:الراية العلامة المنصوبة للرؤية, tr:er-râyetu'l-ʿalâmetu'l-mensûbetu li'r-ru'ye, gloss:sancak, görülmek için dikilmiş işarettir, source:"ر ء ي,B011"}. On ikinci ayetteki {ar:أَمَرَ, tr:emera, gloss:emretti, source:96:12} fiilinin ailesinde yol işareti vardır: {ar:الأمارة العلامة، والأمار أمار الطريق معالمه, tr:el-emâretu'l-ʿalâme, gloss:emâre işarettir; emâr, yolun belirtileridir, source:"ء م ر,B005"}. Sekizinci ayetin dönüş kelimesinin ailesinde, yazının çizgilerinin tekrar tekrar mürekkeplenmesi bulunur: {ar:أن يعاد عليه السواد مرة بعد أخرى, tr:en yuʿâde ʿaleyhi's-sevâdu merraten baʿde uhrâ, gloss:üzerine siyahın tekrar tekrar geçirilmesi, source:"ر ج ع,B009"}.

Sure bu işaretleri yüze taşır. On beşinci ayetin {ar:لَنَسْفَعًۢا, tr:le nesfaʿan, gloss:mutlaka yakalarız, source:96:15} fiilinin ailesinde koyu bir leke vardır: {ar:السفعة بالضم سواد مشرب حمرة, tr:es-sufʿa sevâdun uşribe humra, gloss:sufʿa, kırmızıya çalan siyahlıktır, source:"س ف ع,B002"}. Son ayetin secdesinin ailesinde ise alındaki iz vardır: {ar:المسجد بالفتح جبهة الرجل حيث يصيبه ندب السجود, tr:el-mesced cebhetu'r-racul, gloss:mesced, adamın secde izinin düştüğü alnıdır, source:"س ج د,B003"}. Kurân iki tarafın da yüzüne iz koyar. Müminler için {ar:سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ, tr:sîmâhum fî vucûhihim min eseri's-sucûd, gloss:secde izinden belirtileri yüzlerindedir, source:48:29} denir. Çok yemin eden iftiracı için {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16} denir. Suçlular da yüzlerindeki işaretle tanınır: {ar:يُعْرَفُ ٱلْمُجْرِمُونَ بِسِيمَٰهُمْ فَيُؤْخَذُ بِٱلنَّوَٰصِى وَٱلْأَقْدَامِ, tr:yuʿrafu'l-mucrimûne bi sîmâhum fe yu'hazu bi'n-nevâsî ve'l-akdâm, gloss:suçlular belirtilerinden tanınır, perçemlerinden ve ayaklarından yakalanırlar, source:55:41}. Yazılı kayıt da işaretlenmiştir: {ar:كِتَٰبٌ مَّرْقُومٌ, tr:kitâbun merkûm, gloss:işaretlenmiş bir kitap, source:83:20}, {ar:يَشْهَدُهُ ٱلْمُقَرَّبُونَ, tr:yeşheduhu'l-mukarrabûn, gloss:ona yakınlaştırılanlar şahit olur, source:83:21}.

Böylece sure Rab'bin adıyla başlar, işaret koyan bir araçla öğretir ve iki işaretli alınla biter: biri yakalanıp karartılan alın, öteki secdenin iz bıraktığı alın.

Kaynaklar: 96:1 بِٱسْمِ س م و B005; 96:1 بِٱسْمِ و س م B001; 96:4 عَلَّمَ ع ل م B002; 96:7 رَّءَاهُ ر ء ي B011; 96:12 أَمَرَ ء م ر B005; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B009; 96:15 لَنَسْفَعًۢا س ف ع B002; 96:19 وَٱسْجُدْ س ج د B003

## Tutunmak ve kendini yeterli görmek

İnsan, tutunan bir şeyden yaratılmıştır. Alak kökü asılmayı ve yapışmayı adlandırır: {ar:يناط الشيء بالشيء العالي, tr:yunâtu'ş-şey'u bi'ş-şey'i'l-ʿâlî, gloss:bir şeyin yüksekteki bir şeye asılması, source:"ع ل ق,B001"}; {ar:علق بالشيء نشب به, tr:ʿalika bi'ş-şey'i neşibe bih, gloss:bir şeye takıldı, ona yapıştı, source:"ع ل ق,B001"}. Aynı kök suya yapışan sülüğü de adlandırır: {ar:دويبة في الماء تجمع على علق, tr:duveybetun fi'l-mâ', gloss:suda yaşayan küçük bir hayvan; çoğulu alaktır, source:"ع ل ق,B003"}. Ayrıca canı ayakta tutan en az lokmayı adlandırır: {ar:ما يأكل فلان إلا علقة أي ما يمسك نفسه, tr:mâ ye'kulu fulânun illâ ʿulka, gloss:falan ancak canını tutacak kadar yer, source:"ع ل ق,B006"}. İnsanın başlangıcı yüksekteki bir şeye asılı, tutunarak ve azla yaşayan bir şeydir.

Beşinci ayet bu eksik varlığa öğretilen şeyi anar: bilmediği şey ona verilir. Yedinci ayet sonra tersine döner: insan kendini {ar:ٱسْتَغْنَىٰٓ, tr:istagnâ, gloss:muhtaç olmayan, yeterli, source:96:7} görür. Kök ihtiyaçsızlığı adlandırır: {ar:عدم الحاجات وقلة الحاجات وكثرة القنيات, tr:ʿademu'l-hâcât ve killetu'l-hâcât ve kesretu'l-kunyât, gloss:ihtiyaçların olmaması, azlığı ve edinilmiş şeylerin çokluğu, source:"غ ن ي,B001"}. Aynı kök bir şeyin yetip yetmemesini de anlatır: {ar:ما يغني عنك هذا أي ما يجزئ وما ينفع, tr:mâ yugnî ʿanke hâzâ, gloss:bu sana yetmez, fayda vermez, source:"غ ن ي,B002"}. Kökte kendine bakışla yeterliliği tek figürde birleştiren bir kadın da vardır: {ar:الغانية المرأة واستغنت ببعلها أو بجمالها عن لبس الحلي, tr:el-gâniye, gloss:gâniye, kocası ya da güzelliği sayesinde süs takmaya ihtiyaç duymayan kadındır, source:"غ ن ي,B005"}. Yedinci ayetteki "kendini görmek" ile "yeterli olmak" bu figürde bir araya gelir.

Kurân bu kelimeyi birkaç sahnede inkârla birleştirir: {ar:وَأَمَّا مَنۢ بَخِلَ وَٱسْتَغْنَىٰ, tr:ve emmâ men bahile ve'stagnâ, gloss:cimrilik eden ve kendini muhtaç görmeyene gelince, source:92:8}, {ar:وَكَذَّبَ بِٱلْحُسْنَىٰ, tr:ve kezzebe bi'l-husnâ, gloss:ve en güzeli yalanlayan, source:92:9}. Peygamber'e, kendini yeterli gören zengin kişiye yönelmesi hatırlatılır: {ar:أَمَّا مَنِ ٱسْتَغْنَىٰ, tr:emmâ meni'stagnâ, gloss:kendini muhtaç görmeyene gelince, source:80:5}, {ar:فَأَنتَ لَهُۥ تَصَدَّىٰ, tr:fe ente lehû tesaddâ, gloss:sen ona yöneliyorsun, source:80:6}. Gerçek yeterliliğin kime ait olduğu da söylenir. Elçilerini reddedenler için {ar:فَكَفَرُوا۟ وَتَوَلَّوا۟ وَّٱسْتَغْنَى ٱللَّهُ, tr:fe keferû ve tevellev vestagna'llâh, gloss:inkâr ettiler ve yüz çevirdiler, Allah da onlara ihtiyaç duymadı, source:64:6} denir. Tüm insanlara da {ar:أَنتُمُ ٱلْفُقَرَآءُ إِلَى ٱللَّهِ وَٱللَّهُ هُوَ ٱلْغَنِىُّ ٱلْحَمِيدُ, tr:entumu'l-fukarâ'u ila'llâh, va'llâhu huve'l-ganiyyu'l-hamîd, gloss:Allah'a muhtaç olanlar sizsiniz, ihtiyaçsız ve övülmeye layık olan Allah'tır, source:35:15} denir. Hesap gününde ise yeterlilik iddiası kendi ağzından çöker: {ar:مَآ أَغْنَىٰ عَنِّى مَالِيَهْ, tr:mâ agnâ ʿannî mâliyeh, gloss:malım bana hiçbir yarar sağlamadı, source:69:28}.

Rab kelimesinin ailesinde ihtiyaç ile nimet tek kelimede birleşir: {ar:الربى: الحاجة؛ … الربى: النعمة والإحسان, tr:er-rubbâ: el-hâce … er-rubbâ: en-niʿmetu ve'l-ihsân, gloss:rubbâ ihtiyaçtır; rubbâ nimet ve iyiliktir da, source:"ر ب ب,B016"}. Üçüncü ayetteki en cömert sıfatı ihtiyacı gideren vericiyi anlatır: {ar:الكثير الخير الجواد المنعم المفضل, tr:el-kesîru'l-hayr el-cevâdu'l-munʿim, gloss:hayrı çok, cömert, nimet veren, lütfeden, source:"ك ر م,B001"}. Kurân insanın bu cömertliğe nasıl karşılık verdiğini anlatır: {ar:فَأَكْرَمَهُۥ وَنَعَّمَهُۥ فَيَقُولُ رَبِّىٓ أَكْرَمَنِ, tr:fe ekramehû ve naʿʿamehû fe yekûlu rabbî ekramen, gloss:Rabbi ona ikram edip nimet verince "Rabbim bana ikram etti" der, source:89:15}. Hemen ardından rızkı daraltılınca {ar:فَيَقُولُ رَبِّىٓ أَهَٰنَنِ, tr:fe yekûlu rabbî ehânen, gloss:"Rabbim beni aşağıladı" der, source:89:16}. Kısacası insan, ikramı kendi değerinin kanıtı sayar.

On beşinci ayetteki {ar:يَنتَهِ, tr:yentehi, gloss:vazgeçer, source:96:15} fiilinin ailesinde "yeter" anlamı vardır: {ar:فلان ناهيك من رجل… كما يقال حسبك, tr:fulânun nâhîke min racul, gloss:falan sana yeter bir adamdır, "hasbuk" dendiği gibi, source:"ن ه ي,B005"}. Onuncu ayetin kulu ise kendine ait bir şeyi olmayandır: {ar:العبد وهو المملوك, tr:el-ʿabdu ve huve'l-memlûk, gloss:kul, sahip olunandır, source:"ع ب د,B001"}. Sekizinci ayetteki dönüş, yeterlilik iddiasını geçersiz kılar: asılı başlayan varlık, asıl olduğu yere döner.

Kaynaklar: 96:2 عَلَقٍ ع ل ق B001; 96:2 عَلَقٍ ع ل ق B003; 96:2 عَلَقٍ ع ل ق B006; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B001; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B002; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B005; 96:1 رَبِّكَ ر ب ب B016; 96:3 ٱلْأَكْرَمُ ك ر م B001; 96:15 يَنتَهِ ن ه ي B005; 96:10 عَبْدًا ع ب د B001

## Su: bulut, yağmur, taşkın ve gölet

Bu sahne suyun bütün yolculuğunu izler. Bulut yağmur getirir, ilk yağmur yeri bitkiyle işaretler, ardından ikinci yağmur gelir, yağmur döne döne yağar. Bazı yerler ise atlanır. Su bazen ölçüsünü aşar, taşar ve her şeyi sürükler, sonra yolunun sonundaki gölete varır ve orada durulur.

Üçüncü ayetteki en cömert sıfatının ailesinde yağmur getiren bulut ve verimli toprak vardır: {ar:كرم السحاب أتى بالغيث, tr:kerume's-sehâb, gloss:bulut cömert oldu, yani yağmur getirdi, source:"ك ر م,B002"}; {ar:أرض مكرمة للنبات, tr:ardun mekrame li'n-nebât, gloss:bitkiye cömert toprak, source:"ك ر م,B002"}. Rab kelimesinin ailesinde bitkileri büyüten bulut vardır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb, gloss:rabâb buluttur; bitkiyi büyüttüğü için böyle adlandırılmıştır, source:"ر ب ب,B008"}. Bu, rahimdeki cenini aşama aşama büyüten aynı terbiye işidir. Kayıtlı bir türetmeye göre ad kelimesinin ailesinde de yılın ilk yağmuru vardır: {ar:الوسمي أول مطر السنة يسم الأرض بالنبات, tr:el-vesmiyyu evvelu matari's-sene, gloss:vesmî, yeri bitkiyle işaretleyen yılın ilk yağmurudur, source:"و س م,B003"}. On üçüncü ayetteki {ar:وَتَوَلَّىٰٓ, tr:ve tevellâ, gloss:ve yüz çevirdi, source:96:13} fiilinin kökünde bu yağmuru izleyen yağmur bulunur: {ar:الولي المطر يجيء بعد الوسمي سمي بذلك لأنه يلي الوسمي, tr:el-veliyy el-matar yecî'u baʿde'l-vesmî, gloss:veliy, vesmîden sonra gelen yağmurdur; onu izlediği için böyle denir, source:"و ل ي,B010"}. Bu iki aile anlamı birer yankıdır; ayetlerdeki anlamlar "ad" ve "yüz çevirme"dir. Sekizinci ayetteki dönüş kelimesinin ailesinde ise dönüp duran yağmur vardır: {ar:الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث, tr:er-recʿu'l-gays, gloss:rec yağmurdur, çünkü yağar, sonra döner ve tekrar yağar, source:"ر ج ع,B006"}. Kurân göğe bu sıfatla yemin eder: {ar:وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ, tr:ve's-semâ'i zâti'r-recʿ, gloss:dönüp dönüp yağmur veren göğe andolsun, source:86:11}. On yedinci ayetin {ar:نَادِيَهُۥ, tr:nâdiyeh, gloss:meclisini, source:96:17} kelimesinin ailesinde nem ve cömertlik vardır: {ar:يعبر عن السخاء بالندى, tr:yuʿabbaru ʿani's-sehâ'i bi'n-nedâ, gloss:cömertlik "nem" ile ifade edilir, source:"ن د و,B004"}. On altıncı ayetin {ar:خَاطِئَةٍ, tr:hâti'e, gloss:günahkâr, source:96:16} kelimesinin ailesinde ise yağmurun atladığı toprak vardır: {ar:الخطيئة أرض يخطئها المطر ويصيب غيرها, tr:el-hatî'e ardun yuhti'uha'l-matar, gloss:hatîe, yağmurun ıskalayıp başka yere düştüğü topraktır, source:"خ ط ء,B003"}.

Kurân rahim ile yağmuru tek ayette birleştirir. Rahimdeki aşamalardan sonra {ar:وَتَرَى ٱلْأَرْضَ هَامِدَةً فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:ve tera'l-arda hâmideten fe izâ enzelnâ ʿaleyhe'l-mâ'e'htezzet ve rabet, gloss:yeri kupkuru görürsün; üzerine suyu indirince harekete geçer ve kabarır, source:22:5} denir. Bu ayet canlanmayı yaratılışla aynı kanıta bağlar. Dünya hayatı da yağmurla büyüyüp biçilen bir ekin olarak anlatılır: {ar:كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:keen lem tegne bi'l-ems, gloss:sanki dün orada hiç yokmuş gibi, source:10:24}. Bu ifadede, yedinci ayetin yeterlilik köküyle aynı kökten bir fiil, yerleşik yaşamın bir gecede silinmesini anlatır.

Su ölçüsünü de aşabilir. Altıncı ayetin azma fiili için {ar:طغى الماء خروجه عن المقدار, tr:tagâ'l-mâ' hurûcuhû ʿani'l-mikdâr, gloss:suyun azması ölçüsünden çıkmasıdır, source:"ط غ ي,B002"} ve {ar:طغا البحر والماء إذا علا كل شيء فاجترفه, tr:tagâ'l-bahru ve'l-mâ', gloss:deniz ve su her şeyin üstüne çıkıp onu sürükledi, source:"ط غ ي,B002"} denir. Kök genel olarak ölçüyü aşmaktır: {ar:كل شيء جاوز القدر فقد طغا, tr:kullu şey'in câveze'l-kadr fe kad tagâ, gloss:ölçüyü aşan her şey azmıştır, source:"ط غ ي,B001"}. Kurân bunu Nuh'un tufanı için kullanır: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tage'l-mâ'u hamelnâkum fi'l-câriye, gloss:su taştığında sizi akan gemide taşıdık, source:69:11}. Kuralı da teraziyle birlikte koyar: {ar:أَلَّا تَطْغَوْا۟ فِى ٱلْمِيزَانِ, tr:ellâ tatgav fi'l-mîzân, gloss:ölçüde aşırı gitmeyesiniz diye, source:55:8}. Böylece azma, yaratmanın ölçüsünün karşısına konur.

Taşkının sonu gölettir. On beşinci ayetin vazgeçme fiilinin ailesinde şu anlamlar bulunur: {ar:النهي والنهي الغدير لأن الماء ينتهي إليه, tr:en-nehy, el-gadîr, gloss:nehy göllenmiş sudur, çünkü su ona varıp durur, source:"ن ه ي,B004"}; {ar:تناهى الماء إذا وقف في الغدير وسكن, tr:tenâha'l-mâ', gloss:su gölette durup sakinleşti, source:"ن ه ي,B004"}. Dönüş kelimesinin ailesinde gölete de "rec" denir: {ar:سمي الغدير رجعا, tr:summiye'l-gadîru racʿan, gloss:gölete rec denmiştir, source:"ر ج ع,B006"}. Rab kelimesinin ailesinde de toplanmış bol su vardır: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabab el-mâ'u'l-kesîr, gloss:rabab, toplandığı için böyle denen bol sudur, source:"ر ب ب,B013"}. Böylece on beşinci ayetteki "vazgeçmezse" ifadesinin yanında, suyun durulduğu yerde durmaması da duyulur. Sekizinci ayet suyun varacağı yeri söyler. Kurân bunu ilahî adla birleştiren bir kardeş ayet içerir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Bu yapı sekizinci ayetle aynıdır; tek fark, dönüş yerine varış kökünün kullanılmasıdır.

Kaynaklar: 96:3 ٱلْأَكْرَمُ ك ر م B002; 96:1 رَبِّكَ ر ب ب B008; 96:1 بِٱسْمِ و س م B003; 96:13 وَتَوَلَّىٰٓ و ل ي B010; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B006; 96:17 نَادِيَهُۥ ن د و B004; 96:16 خَاطِئَةٍ خ ط ء B003; 96:6 لَيَطْغَىٰٓ ط غ ي B002; 96:6 لَيَطْغَىٰٓ ط غ ي B001; 96:15 يَنتَهِ ن ه ي B004; 96:8 رَبِّكَ ر ب ب B013

## Başın önü: perçem, alın ve yer

Bu sahne başın ön kısmında geçer. Saç çizgisinde perçem çıkar, altında alnın düz yüzü vardır. Azan adam bu kısmı yukarı kaldırır, bu kısımdan yakalanır ve derisi kararır. Kul ise aynı kısmı yere koyar.

On beşinci ve on altıncı ayetlerin {ar:ٱلنَّاصِيَةِ, tr:en-nâsiye, gloss:perçem, alnın üstündeki saç, source:96:15} kelimesi önce bir yeri adlandırır: {ar:الناصية منبت الشعر في مقدم الرأس, tr:en-nâsiyetu menbitu'ş-şaʿr fî mukaddemi'r-re's, gloss:nâsiye, başın önünde saçın bittiği yerdir, source:"ن ص ي,B001"}. Sonra bir tutuşu adlandırır: {ar:آخذ بناصيتها أي متمكن منها, tr:âhizun bi nâsiyetihâ, gloss:perçeminden tutan, yani ona tam hâkim olan, source:"ن ص ي,B001"}. On beşinci ayetin fiili bu tutuşun kendisidir: {ar:سفعت الفرس إذا أخذت بمقدم رأسه وهي ناصيته, tr:sefaʿtu'l-feres, gloss:atı başının önünden, yani perçeminden tuttum, source:"س ف ع,B001"}. Bu kalıp hem fiili hem perçemi tek cümlede birleştirir. Aynı fiil yüzün kararmasını da anlatır: {ar:سفعته النار والسموم إذا لفحته لفحا يسيرا فغيرت لون البشرة, tr:sefaʿathu'n-nâru ve's-semûm, gloss:ateş ya da kızgın rüzgâr onu hafifçe yalayıp deri rengini değiştirdi, source:"س ف ع,B003"}. Öfkeden kararan yüz için de {ar:به سفعة غضب, tr:bihî sufʿatu gadab, gloss:yüzünde öfke karası var, source:"س ف ع,B002"} denir. Kurân perçemden tutmayı her canlıya genelleştirir. Hud kavmine şöyle der: {ar:مَّا مِن دَآبَّةٍ إِلَّا هُوَ ءَاخِذٌۢ بِنَاصِيَتِهَآ, tr:mâ min dâbbetin illâ huve âhizun bi nâsiyetihâ, gloss:O'nun perçeminden tutmadığı hiçbir canlı yoktur, source:11:56}. Kurân bunu suçlular için de söyler: {ar:فَيُؤْخَذُ بِٱلنَّوَٰصِى وَٱلْأَقْدَامِ, tr:fe yu'hazu bi'n-nevâsî ve'l-akdâm, gloss:perçemlerinden ve ayaklarından tutulurlar, source:55:41}. Yüzün ateşte sürüklenmesi de anlatılır: {ar:يَوْمَ يُسْحَبُونَ فِى ٱلنَّارِ عَلَىٰ وُجُوهِهِمْ, tr:yevme yushabûne fi'n-nâri ʿalâ vucûhihim, gloss:ateşte yüzüstü sürüklenecekleri gün, source:54:48}. Cehennemin deriyi yakması da: {ar:لَوَّاحَةٌ لِّلْبَشَرِ, tr:levvâhatun li'l-beşer, gloss:deriyi kavurup karartan, source:74:29}.

Perçem aynı zamanda kavmin başıdır: {ar:فلان ناصية قومه, tr:fulânun nâsiyetu kavmih, gloss:falan kavminin perçemidir, yani önderidir, source:"ن ص ي,B003"}. Bu yüzden on altıncı ayetteki {ar:نَاصِيَةٍ كَٰذِبَةٍ خَاطِئَةٍ, tr:nâsiyetin kâzibetin hâti'e, gloss:yalancı, günahkâr bir perçem, source:96:16} ifadesinde hem adamın kendisi hem de on yedinci ayette çağırdığı meclisin başı duyulur. Sıfatlar perçeme yalan ve kasıtlı günah yükler: {ar:الخاطئ هو القاصد للذنب, tr:el-hâti'u huve'l-kâsidu li'z-zenb, gloss:hâti, günaha kasteden kişidir, source:"خ ط ء,B002"}.

Başın yükseltilmesi altıncı ayetin fiilinde de görülür: {ar:الطغية أعلى الجبل, tr:et-tugye aʿle'l-cebel, gloss:tugye dağın en yüksek yeridir, source:"ط غ ي,B005"}. Alnın düz yüzü de yaratma kökünden adlandırılır: {ar:خليقاء الجبهة مستواها, tr:halîkâ'u'l-cebhe, gloss:halîkâ, alnın düz yüzüdür, source:"خ ل ق,B008"}. Kurân başını en yükseğe kaldıranı Firavun'da gösterir: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe kâle ene rabbukumu'l-aʿlâ, gloss:"ben sizin en yüce rabbinizim" dedi, source:79:24}. Arkasından da {ar:فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ, tr:fe ehazehu'llâhu nekâle'l-âhirati ve'l-ûlâ, gloss:Allah onu ahiret ve dünya cezasıyla yakaladı, source:79:25} denir.

Son ayetin secde emri bu sahnenin karşı yüzüdür: {ar:سجد: خضع ومنه سجود الصلاة وهو وضع الجبهة على الأرض, tr:secede: hadaʿa, gloss:secde etti, yani boyun eğdi; namazdaki secde alnı yere koymaktır, source:"س ج د,B001"}; {ar:أسجد الرجل إذا طأطأ رأسه وانحنى, tr:escede'r-racul, gloss:adam başını eğip öne büküldü, source:"س ج د,B004"}. Yukarı kaldırılan ve yakalanıp karartılan alın ile yere konup secde izi taşıyan alın aynı organdır. Sure bu organı iki şekilde gösterir ve iki yol arasındaki farkı başın konumu üzerinden anlatır.

Kaynaklar: 96:15 ٱلنَّاصِيَةِ ن ص ي B001; 96:15 لَنَسْفَعًۢا س ف ع B001; 96:15 لَنَسْفَعًۢا س ف ع B002; 96:15 لَنَسْفَعًۢا س ف ع B003; 96:16 نَاصِيَةٍ ن ص ي B003; 96:16 خَاطِئَةٍ خ ط ء B002; 96:6 لَيَطْغَىٰٓ ط غ ي B005; 96:1 خَلَقَ خ ل ق B008; 96:19 وَٱسْجُدْ س ج د B001; 96:19 وَٱسْجُدْ س ج د B004

## Tuzak ve av

Avcılar açık araziye çıkar, tuzak kurar; av ağa takılır. Yaban hayvanı bir süre koşar, sonra durup arkasına bakar. Bu sahnenin üyeleri surenin birçok kelimesine dağılmıştır. Onuncu ayetin namaz fiilinin ailesinde tuzak kurmak vardır: {ar:المصلاة أن تنصب شركا ونحوه ليقع فيه شيء فيصطاد, tr:el-maslât en tensibe şereken, gloss:maslât, bir şey düşsün de avlansın diye tuzak kurmaktır, source:"ص ل و,B004"}. Bu anlam mecaz olarak birinin yıkımına çalışmak için de kullanılır: {ar:صليت لفلان إذا عملت له في أمر تريد أن توقعه في هلكة, tr:salaytu li fulân, gloss:falana tuzak kurdum, yani onu helake düşürmek için uğraştım, source:"ص ل و,B004"}. İkinci ayetin alak kökünde ağa takılan ceylan vardır: {ar:علق الظبي في الحبالة يعلق إذا نشق فيها, tr:ʿalika'z-zabyu fi'l-hibâle, gloss:ceylan ağa takıldı, source:"ع ل ق,B011"}. Birinci ayetin ad kelimesinin kökünde avcılar vardır: {ar:خرج القوم للصيد في قفار الأرض وصحاريها قلت سموا وهم السماة أي الصيادون, tr:semev, ve humu's-sumât, gloss:topluluk ıssız yerlere ava çıktığında "semev" denir; onlar sumâttır, yani avcılar, source:"س م و,B006"}. On beşinci ayetin fiilinin ailesinde kovalamaca ve yırtıcı kuşun vuruşu bulunur: {ar:المسافعة كالمطاردة, tr:el-musâfaʿa ke'l-mutârade, gloss:müsâfaa kovalamaca gibidir, source:"س ف ع,B005"}; {ar:سفع الطائر ضريبته أي لطمه, tr:sefaʿa't-tâ'iru darîbeteh, gloss:kuş avına vurdu, source:"س ف ع,B004"}. On üçüncü ayetin yalanlama fiilinin ailesinde de kaçan hayvan vardır: {ar:كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه, tr:kezebe'l-vahşiyy, gloss:yaban hayvanı bir koşu koşup sonra arkasına bakmak için durdu, source:"ك ذ ب,B007"}.

Sahnenin işleyişi tersine döner. Kulun namazına engel olmak isteyen adam bir avcı gibi davranır. Ama yakalanan odur: perçeminden tutulur, tıpkı ağa takılan av gibi. Kurân Peygamber'e karşı kurulan tuzağı ve tuzağın sahibine dönüşünü anlatır: {ar:وَإِذْ يَمْكُرُ بِكَ ٱلَّذِينَ كَفَرُوا۟ لِيُثْبِتُوكَ أَوْ يَقْتُلُوكَ أَوْ يُخْرِجُوكَ, tr:ve iz yemkuru bike'llezîne keferû li yusbitûke ev yaktulûke ev yuhricûk, gloss:inkâr edenler seni tutup bağlamak, öldürmek ya da çıkarmak için tuzak kuruyorlardı, source:8:30}, {ar:وَيَمْكُرُونَ وَيَمْكُرُ ٱللَّهُ, tr:ve yemkurûne ve yemkuru'llâh, gloss:onlar tuzak kuruyordu, Allah da tuzak kuruyordu, source:8:30}. Bu sahne, avcının av olduğu bir çevrilmeyi yasaklayanın sonuna bağlar.

Kaynaklar: 96:10 صَلَّىٰٓ ص ل و B004; 96:2 عَلَقٍ ع ل ق B011; 96:1 بِٱسْمِ س م و B006; 96:15 لَنَسْفَعًۢا س ف ع B005; 96:15 لَنَسْفَعًۢا س ف ع B004; 96:13 كَذَّبَ ك ذ ب B007; 96:15 ٱلنَّاصِيَةِ ن ص ي B001

## Efendi, kul ve itaat

Bu sahnede bir sahip ve sahip olunan vardır. Rab kelimesi sahibi ve itaat edilen efendiyi adlandırır: {ar:يكون الرب: المالك؛ ويكون الرب: السيد المطاع, tr:yekûnu'r-rabb el-mâlik, ve yekûnu'r-rabb es-seyyidu'l-mutâʿ, gloss:rab sahip demektir; rab, itaat edilen efendi demektir de, source:"ر ب ب,B001"}. Bu tanım rabbi son ayetteki itaat fiiline bağlar. Onuncu ayetin kulu hem sahip olunandır hem de kulluğunu gösterendir: {ar:العبودية إظهار التذلل والعبادة غاية التذلل, tr:el-ʿubûdiyyetu izhâru't-tezellul, gloss:kulluk, alçakgönüllülüğü göstermektir; ibadet ise alçakgönüllülüğün en ileri derecesidir, source:"ع ب د,B003"}. Kulluk itaatle de birleşir: {ar:إياك نعبد إياك نطيع الطاعة التي نخضع معها, tr:iyyâke naʿbudu: iyyâke nutîʿ, gloss:"yalnız sana kulluk ederiz": yalnız sana, boyun eğerek itaat ederiz, source:"ع ب د,B003"}. Kökte çok yürünmüş, düzleşmiş yol da vardır: {ar:الطريق المعبد وهو المسلوك المذلل, tr:et-tarîku'l-muʿabbed, gloss:muabbed yol, çok yürünüp düzlenmiş yoldur, source:"ع ب د,B005"}.

Dokuzuncu ayetin {ar:يَنْهَىٰ, tr:yenhâ, gloss:men eder, source:96:9} fiili emrin zıddıdır: {ar:النهي خلاف الأمر, tr:en-nehyu hilâfu'l-emr, gloss:nehiy emrin zıddıdır, source:"ن ه ي,B001"}. On ikinci ayetin {ar:أَوْ أَمَرَ بِٱلتَّقْوَىٰٓ, tr:ev emera bi't-takvâ, gloss:ya da sakınmayı emrettiyse, source:96:12} ifadesi, aynı kişinin aslında emredebilecek olduğunu söyler: {ar:الأمر الذي هو نقيض النهي, tr:el-emru'llezî huve nakîdu'n-nehy, gloss:nehyin zıddı olan emir, source:"ء م ر,B002"}. Aynı kök aklı da adlandırır: {ar:النهية العقل لأنه ينهى عن قبيح الفعل, tr:en-nuhye el-ʿakl, gloss:nuhye akıldır, çünkü çirkin işten alıkoyar, source:"ن ه ي,B003"}. Namazı yasaklayan adam, kendi aklının görevini tersine çevirir. Kurân namazın kendisinin yasakladığını söyler: {ar:إِنَّ ٱلصَّلَوٰةَ تَنْهَىٰ عَنِ ٱلْفَحْشَآءِ وَٱلْمُنكَرِ, tr:inne's-salâte tenhâ ʿani'l-fahşâ'i ve'l-munker, gloss:namaz hayâsızlıktan ve kötülükten alıkoyar, source:29:45}. Doğru yasaklama da nefsin kendisine yöneltilir: {ar:وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve nehe'n-nefse ʿani'l-hevâ, gloss:nefsini keyfî istekten alıkoyan, source:79:40}. Allah'ın mescitlerinde adının anılmasını engelleyen de anılır: {ar:وَمَنْ أَظْلَمُ مِمَّن مَّنَعَ مَسَٰجِدَ ٱللَّهِ أَن يُذْكَرَ فِيهَا ٱسْمُهُۥ, tr:ve men azlemu mimmen menaʿa mesâcida'llâhi en yuzkera fîhe'smuh, gloss:Allah'ın mescitlerinde adının anılmasını engelleyenden daha zalim kim olabilir, source:2:114}. Bu ayet, adla başlayan ve secdeyle biten surenin yasaklayanına yakındır.

Altıncı ayetin azma fiili itaatte sınırı aşmaktır; kök sahte mabudu da adlandırır: {ar:الطاغوت… كل معبود من دون الله, tr:et-tâgût … kullu maʿbûdin min dûni'llâh, gloss:tâgût, Allah'tan başka tapılan her şeydir, source:"ط غ ي,B003"}. Kurân bunun en açık örneği olarak Firavun'u gösterir: {ar:ٱذْهَبْ إِلَىٰ فِرْعَوْنَ إِنَّهُۥ طَغَىٰ, tr:izheb ilâ firʿavne innehû tagâ, gloss:Firavun'a git, çünkü o azdı, source:79:17}. Firavun sonunda kendini rab ilan eder. On dördüncü ayetteki Allah adının kökü ise tapılanı adlandırır: {ar:إله اسما لكل معبود… فالإله على هذا هو المعبود, tr:ilâh … el-maʿbûd, gloss:ilah, tapılan her şeyin adıdır; buna göre ilah tapılandır, source:"ء ل ه,B001"}.

Son ayetin {ar:لَا تُطِعْهُ, tr:lâ tutiʿhu, gloss:ona boyun eğme, source:96:19} emri, isteyerek boyun eğmeyi yasaklar: {ar:الطوع نقيض الكره, tr:et-tavʿu nakîdu'l-kerh, gloss:tav, zorlamanın zıddıdır, source:"ط و ع,B001"}. Kurân aynı yasağı Peygamber'e başka yerlerde de verir: {ar:فَلَا تُطِعِ ٱلْمُكَذِّبِينَ, tr:fe lâ tutiʿi'l-mukezzibîn, gloss:yalanlayanlara boyun eğme, source:68:8}; {ar:وَلَا تُطِعْ كُلَّ حَلَّافٍ مَّهِينٍ, tr:ve lâ tutiʿ kulle hallâfin mehîn, gloss:çok yemin eden aşağılık kimseye boyun eğme, source:68:10}. Bir başka yerde bu yasak, adı anmak ve secde etmekle aynı yerde geçer: {ar:وَلَا تُطِعْ مِنْهُمْ ءَاثِمًا أَوْ كَفُورًا, tr:ve lâ tutiʿ minhum âsimen ev kefûrâ, gloss:onlardan hiçbir günahkâra ya da nanköre boyun eğme, source:76:24}. Bundan hemen sonra adı anmak ve gece secde etmek emredilir. Bu, surenin son ayetinin yapısıyla aynıdır. Sahne surenin sorusunu açıkça ortaya koyar: kul kime itaat edecek? Sahibi Rab olan kul, kendini rab yerine koyan adama boyun eğmez.

Kaynaklar: 96:1 رَبِّكَ ر ب ب B001; 96:10 عَبْدًا ع ب د B003; 96:10 عَبْدًا ع ب د B005; 96:9 يَنْهَىٰ ن ه ي B001; 96:12 أَمَرَ ء م ر B002; 96:9 يَنْهَىٰ ن ه ي B003; 96:6 لَيَطْغَىٰٓ ط غ ي B003; 96:14 ٱللَّهَ ء ل ه B001; 96:19 تُطِعْهُ ط و ع B001

## Ölçerek yaratmak ve uydurmak

Yaratmak doğru ölçmektir. Aynı kök uydurmayı da adlandırır: {ar:الخلق خلق الكذب وهو اختلاقه واختراعه وتقديره في النفس, tr:el-halku halku'l-kezib, gloss:halk, yalanı uydurmak, icat etmek ve onu nefiste ölçüp biçmektir, source:"خ ل ق,B007"}. Bu tanım yaratma kökünü yalan köküyle birleştirir. Rab gerçeği ölçerek yaratır; yalancı ise yalanı içinde ölçüp biçer. Kurân bu anlamı İbrahim'in kavmine söylediği sözde kullanır: {ar:إِنَّمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ أَوْثَٰنًا وَتَخْلُقُونَ إِفْكًا, tr:innemâ taʿbudûne min dûni'llâhi evsânen ve tahlukûne ifkâ, gloss:siz Allah'ı bırakıp putlara tapıyor ve yalan uyduruyorsunuz, source:29:17}. Mekkeli ileri gelenler de vahyi bu kelimeyle niteler: {ar:إِنْ هَٰذَآ إِلَّا ٱخْتِلَٰقٌ, tr:in hâzâ ille'htilâk, gloss:bu bir uydurmadan başka bir şey değil, source:38:7}. Gerçek yaratıcının övgüsü de aynı kökle yapılır: {ar:فَتَبَارَكَ ٱللَّهُ أَحْسَنُ ٱلْخَٰلِقِينَ, tr:fe tebâreka'llâhu ahsenu'l-hâlikîn, gloss:yaratanların en güzeli Allah ne yücedir, source:23:14}.

On üçüncü ayetin yalanlama fiili ile on altıncı ayetin yalancı sıfatı aynı köktendir: {ar:الكذب خلاف الصدق, tr:el-kezibu hilâfu's-sidk, gloss:yalan doğruluğun zıddıdır, source:"ك ذ ب,B001"}. Kökte görünüşüyle yalan söyleyen bir kumaş da vardır: {ar:الكذابة ثوب ينقش بلون صبغ كأنه موشى وذلك لأنه يكذب بحاله, tr:el-kezzâbe sevbun yunkaşu bi levni sıbg, gloss:kezzâbe, boyayla nakışlı gibi gösterilen kumaştır; çünkü haliyle yalan söyler, source:"ك ذ ب,B009"}. Öğretme kökündeki gerçek dokuma kenarı bunun karşısında durur: {ar:علم الثوب ورقمه في أطرافه, tr:ʿalemu's-sevb, gloss:kumaşın alemi, kenarlarındaki dokuma nakışıdır, source:"ع ل م,B002"}. Kökte beklenenden önce kesilen süt de yer alır: {ar:كذب لبن الناقة إذا ظن أن يدوم مدة فلم يدم, tr:kezebe lebenu'n-nâka, gloss:devenin sütü bir süre süreceği sanıldığı halde kesildi, source:"ك ذ ب,B006"}. Görüntü ile sürekliliğin çatıştığı bir figürdür bu. Yedinci ayetin görme kökünde güzel görünüş de vardır: {ar:الرواء حسن المنظر, tr:er-ruvâ' husnu'l-manzar, gloss:ruvâ, görünüş güzelliğidir, source:"ر ء ي,B006"}.

On altıncı ayetin sıfatı kasıtlı günahı seçer: {ar:الخطأ ما لم يتعمد … الخطيئة الذنب على عمد, tr:el-hata'u mâ lem yutaʿammad … el-hatî'etu'z-zenbu ʿalâ ʿamd, gloss:hata kasıtsız olandır; hatîe kasıtlı günahtır, source:"خ ط ء,B002"}. Kurân bu kelimeyi helak edilmiş toplumlar için kullanır: {ar:وَجَآءَ فِرْعَوْنُ وَمَن قَبْلَهُۥ وَٱلْمُؤْتَفِكَٰتُ بِٱلْخَاطِئَةِ, tr:ve câ'e firʿavnu ve men kablehû ve'l-mu'tefikâtu bi'l-hâti'e, gloss:Firavun, ondan öncekiler ve altı üstüne getirilen şehirler o günahı işlediler, source:69:9}, {ar:فَأَخَذَهُمْ أَخْذَةً رَّابِيَةً, tr:fe ehazehum ahzeten râbiye, gloss:O da onları şiddetli bir yakalayışla yakaladı, source:69:10}. Günahın ardından gelen yakalama, on beşinci ayetteki perçemden yakalamayla aynı yapıdadır.

Bu sahne şunu gösterir: on altıncı ayetteki yalancı perçem, olmadığı bir şeyi iddia eden yüksek baştır, boyanmış ama dokunmamış bir kumaş gibidir. Gerçek ölçüyü yaratan Rab'bin karşısında, uydurma bir ölçüyle kendini yeterli görür.

Kaynaklar: 96:1 خَلَقَ خ ل ق B001; 96:1 خَلَقَ خ ل ق B007; 96:13 كَذَّبَ ك ذ ب B001; 96:16 كَٰذِبَةٍ ك ذ ب B009; 96:16 كَٰذِبَةٍ ك ذ ب B006; 96:4 عَلَّمَ ع ل م B002; 96:7 رَّءَاهُ ر ء ي B006; 96:16 خَاطِئَةٍ خ ط ء B002

## Buluşmalar

İmgeler en açık şekilde baş sahnesinde buluşur. On beşinci ayetin fiili hem perçemden tutmak hem de yüzü karartmaktır. Böylece başın önü, avın yakalandığı yer, huysuz hayvanın tutulduğu yer ve ateşin yaladığı deri aynı noktada birleşir. Aynı alın son ayette yere konur ve secde izini taşır. İşaret imgesi buraya da uzanır: bir alın kararmış bir lekeyle işaretlenir, öteki secdenin iziyle. Kurân her iki tarafı da yüzlerindeki işaretle tanıtır: biri {ar:مِّنْ أَثَرِ ٱلسُّجُودِ, tr:min eseri's-sucûd, gloss:secdenin izinden, source:48:29}, öteki {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. Sure ad ile başlar ve iki işaretli alınla biter.

Göz ile yeterlilik imgeleri yedinci ayette buluşur. Kendini aynada gören adam ile süse ihtiyaç duymayan güzel kadın aynı kelime çiftinde birleşir: kendini görmek ve yeterli saymak. Su imgesi de buna bağlanır. Azan insan ölçüsünü aşan bir taşkın gibidir; on beşinci ayette durması istenir. Kökün göletteki duruluşu adlandırdığı hatırlanırsa, sekizinci ayet bu suyun nereye varacağını söyler. Kurân'ın varış ayeti bu iki imgeyi aynı yapıda birleştirir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Yol imgesi de bu dönüşe katılır, çünkü dönüş başlangıca dönmektir ve bu başlangıç rahimdeki ilk tutunuştur.

Rahim ile okuma, surenin ilk kelimesinde buluşur. Okumanın kökü hem rahmin bir şeyi toplayıp tutmasını hem de harflerin toplanmasını adlandırır. Pıhtıyı tutan kökle sözü toplayan kök aynıdır. İnsanın yaratılışı ve öğretilmesi bu yüzden aynı işin iki yüzü olarak duyulur. Kurân'daki benzer sıra da bunu destekler: Kurân'ı öğretmek, insanı yaratmak ve ona açıklamayı öğretmek. Okuma ile secde de buluşur: okuyucu aynı zamanda kulluk edendir ve sure, ilk emri okumak, son emri secde etmek olan bir eğri çizer. Kurân bu ikisini, okunduğunda secde edenler ile etmeyenler üzerinden birleştirir.

Ateş ile çağrı imgeleri onuncu, on yedinci ve on sekizinci ayetlerde buluşur. Namaz hem çağrıdır hem de kökü ateşe girmeyi adlandırır. Adam meclisini çağırır, Allah ateşe iten bekçileri çağırır ve kul yakın meclise çağrılır. Ateşin kendisinin de çağırdığı söylenir: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Bu yüz çevirme on üçüncü ayetin fiilidir.

İtaat ile hayvan imgeleri son ayette buluşur. Rab, itaat edilen efendidir; dizgine uyan at da itaatin bir figürüdür. Kul bu yüzden kendini rab ilan eden birine boyun eğmez, yakında tutulan ve değer gören at gibi yaklaşır. Yaratma ile uydurma da on altıncı ayette buluşur. Gerçek ölçüyle yaratan Rab'bin karşısında, yalanı içinde ölçen yalancı perçem durur.

Bu buluşmalar surenin hareketini taşır. Sure, rahimde toplanan ve tutunan bir varlıkla başlar; bu varlık sözü toplamayı ve kalemle yazmayı öğrenir. Sonra kendini aynada yeterli görür, taşkın su gibi ölçüsünü aşar, başını kaldırır ve namaz kılan kulu engellemeye çalışır. Dönüş ayeti ve Allah'ın görmesi bu yükselişin önüne bir sınır koyar. Yasaklayan perçeminden yakalanır, meclisi yerine bekçiler gelir. Kul ise yüz çevirmeden, başını yere koyarak, çağrılmış olduğu yakınlığa yürür.

