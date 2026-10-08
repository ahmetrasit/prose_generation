Focus: 96:3. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/96_3/D.r13/context.md =====
# 96:3 — focus

ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ

Anchor translation (canonical reading, reference only):

Oku; Rabbin en cömerttir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | ٱقْرَأْ | قَرَأَ | ق ر ء | V |
| 2 | وَرَبُّكَ | رَبّ | ر ب ب | REM;N;PRON |
| 3 | ٱلْأَكْرَمُ | أَكْرَم | ك ر م | DET;ADJ |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 96 — full text (context; no pericope)

- 96:1 ٱقْرَأْ بِٱسْمِ رَبِّكَ ٱلَّذِى خَلَقَ
- 96:2 خَلَقَ ٱلْإِنسَٰنَ مِنْ عَلَقٍ
- 96:3 ◀ focus ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ
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


===== _commentary/v16/work/96_3/D.r13/01_dictionary.md =====
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

## ر ب ب (root_000532) — identity root of وَرَبُّكَ (w2)

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

## ك ر م (root_001294) — identity root of ٱلْأَكْرَمُ (w3)

- **B001** övgüye değer soyluluk, eli açıklık ve onurlandırma — soyluluk, eli açıklık ve övgüye değer huy · soylu, eli açık, bağışlayıcı; kendi türünde seçkin · soylular; seçkin ve övgüye değer olanlar · onurlandırdı veya değerli kıldı · onurlandırma ve incitmeden değerli yarar sağlama · onurlandırma; saygınlık · ayıp ve utanç verici şeylerden uzak durdu · soylu ve değerli çocukları oldu · değerli bir bağ ya da varlık edindi · yumuşak ve saygılı söz · kendi alanında yararlı ve övgüye değer tür · içerdiği yol gösterme, açıklama, bilgi ve bilgelikle övgüye değer kitap · içeriği güzel, saygın ya da mühürlü yazı · en soylu ve en erdemli · güzel ve saygın giriş yeri
  شرف في الشيء في نفسه أو شرف في خلق من الأخلاق (maqayis)؛ الكريم الصفوح (maqayis;sihah)؛ الكرم شرف الرجل (ayn)؛ تكرم عن الشائنات أي تنزه (ayn;tahdhib)؛ الكرم ضد اللؤم (sihah)؛ أتى بأولاد كرام واستحدث علقا كريما (sihah)؛ الكثير الخير الجواد المنعم المفضل (tahdhib)؛ اسم جامع لكل ما يحمد (tahdhib)؛ الأخلاق والأفعال المحمودة (mufradat)؛ كل شيء شرف في بابه (mufradat)
- **B002** yağmur getirme ve toprağın verimli oluşu [kalıp] — bulut yağmur getirdi ve suyunu bolca verdi · bitkisi gür, toprağı iyi ve taşları ayıklanmış arazi · toprağı işlenip gübrelendikten sonra bitkisi gürleşti
  كرم السحاب أتى بالغيث (maqayis;sihah)؛ أرض مكرمة للنبات إذا كانت جيدة النبات (maqayis;sihah)؛ إذا جاد السحاب بغيثه قيل كرم (ayn)؛ أرض مثارة منقاة من الحجارة (ayn;tahdhib)؛ البقعة الطيبة التربة العذاة المنبت بقعة مكرمة (tahdhib)؛ كرمت أرض فلان إذا دملها فزكا نبتها (tahdhib)
- **B003** boyun kolyesi — boyna takılan kolye veya dizili süs · kolyeler
  الكَرْم وهي القلادة (maqayis)؛ الكَرْم القلادة (ayn;sihah)؛ رأيت في عنقها كَرْما حسنا من لؤلؤ (sihah)؛ الكروم القلائد واحدها كَرْم (tahdhib)
- **B004** üzüm ve asma — üzüm, asma veya asmanın meyvesi · tek asma sürgünü veya bir asma
  الكَرْم فالعنب أيضا لأنه مجتمع الشعب منظوم الحب (maqayis)؛ الكرمة طاقة من الكرم (ayn)؛ الكَرْم كرم العنب (sihah)؛ الكرمة الطاقة الواحدة من الكرم (tahdhib)؛ يسمى الكرم كرما لأنه وصف بكرم شجرته وثمرته (tahdhib)
- **B005** kap ağzına konan tabak biçimli kapak — testi veya tencere ağzına konan tabak biçimli kapak
  الكرامة طبق يوضع على رأس الحب (ayn;sihah)؛ لطبق القدر والحب الكرامة (tahdhib)
- **B006** eli açıklıkta övünme yarışı ve üstün gelme — onunla eli açıklık konusunda övünme yarışına girdi · eli açıklıkta onu geçti
  كارمت الرجل إذا فاخرته في الكرم فكرمته إذا غلبته فيه (sihah)
- **B007** uyluk kemiğinin kalça yuvasındaki yuvarlak başı — uyluk kemiğinin kalça yuvasındaki yuvarlak başı
  الكرمة رأس الفخذ المستدير كأنه جوزة تدور في قلت الورك (sihah)
- **B008** karşılık bekleyerek sunma ve övgüyü ödüllendirme — karşılığında ödül almak için onu sundu · kendisine yöneltilen övgüyü ödüllendiren kişi
  أكارم بها يهود أي أهديها إليهم فيثيبوني عليها (tahdhib)؛ أخ مكارم أي يكافئني على مدحي إياه (tahdhib)
- **B009** memnuniyetle kabul ve saygı bildiren kalıp yanıt [kalıp] — evet, memnuniyetle ve seve seve · senin için seve seve; sana duyduğum saygıyla
  نعم وحبا وكرامة (sihah)؛ نعم وحبا وكرما وحبا وكرمة (sihah)؛ أفعل ذلك وكرمة لك وكرمى لك وكرامة لك وكرما لك وكرمة عين (tahdhib)
- **B010** değer verilen varlık ve topluluğun seçkin kişisi — senin için çok değerli olan kişi veya şey · topluluğun soylu, saygın ve seçkin kişisi
  كل شيء يكرم عليك فهو كريمك وكريمتك (tahdhib)؛ الكريمة الرجل الحسيب (tahdhib)؛ إذا أتاكم كريمة قوم فأكرموه أي كريم قوم (tahdhib)؛ لا تدخر عنه شيئا يكرم عليك (tahdhib)

## ECHO ر ب و (root_000537) — for وَرَبُّكَ (w2): withheld observed target; not identity

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

===== _commentary/v16/out/s096/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 96:3, and ## Buluşmalar) =====
## Harfleri toplamak: okuma, öğretme, kalem

Okumak, parçaları bir araya getirip bütün olarak söylemektir: {ar:قرأت الشيء قرآنا جمعته وضممت بعضه إلى بعض, tr:kara'tu'ş-şey'e kur'ânen: cemaʿtuhû ve damemtu baʿdahû ilâ baʿd, gloss:bir şeyi okudum, yani topladım ve parçalarını birbirine kattım, source:"ق ر ء,B001"}; {ar:القراءة ضم الحروف والكلمات بعضها إلى بعض, tr:el-kırâ'e: dammu'l-hurûfi ve'l-kelimât, gloss:okuma harfleri ve kelimeleri birbirine katmaktır, source:"ق ر ء,B001"}. Aynı kök, ezberden ya da sayfadan yüksek sesle söylemeyi ve başkasına okutmayı da kapsar: {ar:أقرأت غيري أقرئه إقراء, tr:akra'tu gayrî, gloss:başkasına okuttum, source:"ق ر ء,B002"}. Birinci ayetteki emir ile üçüncü ayetteki tekrarı bu toplama işini iki kez başlatır. Kurân aynı işi vahiy anında Peygamber'e anlatır: dilini acele ile oynatmamasını söyledikten sonra {ar:إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ, tr:inne ʿaleynâ cemʿahû ve kur'ânehû, gloss:onu toplamak ve okutmak bize aittir, source:75:17}, {ar:فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ, tr:fe izâ kara'nâhu fettebiʿ kur'ânehû, gloss:onu okuduğumuzda sen okunuşunu izle, source:75:18}. Toplamak ile okumak burada yan yana durur. Okutan da Allah'tır: {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:senukri'uke fe lâ tensâ, gloss:sana okutacağız, unutmayacaksın, source:87:6}. Kurân'ın parça parça okunmak üzere ayrıldığı da söylenir: {ar:وَقُرْءَانًا فَرَقْنَٰهُ لِتَقْرَأَهُۥ عَلَى ٱلنَّاسِ عَلَىٰ مُكْثٍ, tr:ve kur'ânen ferakna-hu li takra'ehû ʿale'n-nâsi ʿalâ muks, gloss:onu insanlara ağır ağır okuyasın diye bölümlere ayırdığımız bir Kurân, source:17:106}.

Dördüncü ve beşinci ayetler öğretmeyi getirir. {ar:عَلَّمَ, tr:ʿalleme, gloss:öğretti, source:96:4} zihni anlamları kavramaya uyandırmaktır: {ar:التعليم تنبيه النفس لتصور المعاني, tr:et-taʿlîm tenbîhu'n-nefsi li tasavvuri'l-meʿânî, gloss:öğretmek, nefsi anlamları kavramaya uyandırmaktır, source:"ع ل م,B001"}. Öğretme {ar:بِٱلْقَلَمِ, tr:bi'l-kalem, gloss:kalemle, source:96:4} olur: {ar:القلم الذي يكتب به, tr:el-kalemu'llezî yuktebu bih, gloss:kalem, onunla yazılan şeydir, source:"ق ل م,B003"}. Kalem, toplanıp söyleneni kalıcı kılar. Kurân kaleme yemin eder: {ar:نٓ وَٱلْقَلَمِ وَمَا يَسْطُرُونَ, tr:nûn, ve'l-kalemi ve mâ yesturûn, gloss:Nun. Kaleme ve yazdıklarına andolsun, source:68:1}. Allah'ın yazmayı öğrettiği borç sözleşmesi ayetinde de söylenir: {ar:وَلَا يَأْبَ كَاتِبٌ أَن يَكْتُبَ كَمَا عَلَّمَهُ ٱللَّهُ, tr:ve lâ ye'be kâtibun en yektube kemâ ʿallemehu'llâh, gloss:yazıcı, Allah'ın ona öğrettiği gibi yazmaktan kaçınmasın, source:2:282}. Kalemin gücü, Allah'ın sözlerinin yanında küçülür: {ar:وَلَوْ أَنَّمَا فِى ٱلْأَرْضِ مِن شَجَرَةٍ أَقْلَٰمٌ, tr:ve lev ennemâ fi'l-ardı min şeceratin aklâm, gloss:yeryüzündeki ağaçlar kalem olsa, source:31:27}, deniz mürekkep olsa bile o sözler tükenmez.

Surenin ilk beş ayetindeki sıra Kurân'da bir kez daha geçer: {ar:عَلَّمَ ٱلْقُرْءَانَ, tr:ʿallemel-kur'ân, gloss:Kurân'ı öğretti, source:55:2}, {ar:خَلَقَ ٱلْإِنسَٰنَ, tr:halaka'l-insân, gloss:insanı yarattı, source:55:3}, {ar:عَلَّمَهُ ٱلْبَيَانَ, tr:ʿallemehu'l-beyân, gloss:ona açıklamayı öğretti, source:55:4}. Öğretilen şeyin insanın bilmediği şey olduğu da söylenir: {ar:وَيُعَلِّمُكُم مَّا لَمْ تَكُونُوا۟ تَعْلَمُونَ, tr:ve yuʿallimukum mâ lem tekûnû taʿlemûn, gloss:size bilmediğinizi öğretir, source:2:151}.

Rab kelimesinin ailesinde öğreten de vardır: {ar:الرباني… العالم المعلم الذي يغذو الناس بصغار العلوم, tr:er-rabbânî … el-ʿâlimu'l-muʿallim, gloss:rabbânî, insanları küçük bilgilerden başlayarak besleyen bilgin öğretmendir, source:"ر ب ب,B003"}. Üçüncü ayetin {ar:ٱلْأَكْرَمُ, tr:el-ekrem, gloss:en cömert, source:96:3} sıfatı da öğretme ile bağlantılıdır. Kurân bu kökü kendisi için kullanır: {ar:إِنَّهُۥ لَقُرْءَانٌ كَرِيمٌ, tr:innehû le kur'ânun kerîm, gloss:o elbette değerli bir Kurân'dır, source:56:77}; sayfaları {ar:فِى صُحُفٍ مُّكَرَّمَةٍ, tr:fî suhufin mukerrame, gloss:değerli sayfalardadır, source:80:13} ve {ar:كِرَامٍۭ بَرَرَةٍ, tr:kirâmin berara, gloss:değerli ve iyi, source:80:16} yazıcıların elindedir. Aynı köke, aldanmış insana sorulan soruda da rastlanır: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ مَا غَرَّكَ بِرَبِّكَ ٱلْكَرِيمِ, tr:yâ eyyuhe'l-insânu mâ garraka bi rabbike'l-kerîm, gloss:ey insan, seni cömert Rabbine karşı ne aldattı, source:82:6}.

Okuyucu, toplayan ve şahitlik edendir: {ar:يقرون الأشياء حتى يجمعوها علما ثم يشهدون بها, tr:yakrûne'l-eşyâ'e hattâ yecmeʿûhâ ʿilmen summe yeşhedûne bihâ, gloss:şeyleri bilgi olarak toplayana dek izlerler, sonra onlara şahitlik ederler, source:"ق ر ء,B012"}. Aynı kökte okuyucu kulluk edendir: {ar:رجل قارئ عابد ناسك, tr:raculun kâri'un ʿâbidun nâsik, gloss:okuyucu, kulluk eden, ibadet eden adam, source:"ق ر ء,B006"}. Bu, onuncu ayetteki {ar:عَبْدًا, tr:ʿabden, gloss:bir kulu, source:96:10} kelimesine ve son ayetin secdesine ulaşır. Kurân okumayı secdeyle birleştirir: inkârcılar için {ar:وَإِذَا قُرِئَ عَلَيْهِمُ ٱلْقُرْءَانُ لَا يَسْجُدُونَ, tr:ve izâ kuri'e ʿaleyhimu'l-kur'ânu lâ yescudûn, gloss:onlara Kurân okununca secde etmezler, source:84:21}; daha önce bilgi verilenler için {ar:إِذَا يُتْلَىٰ عَلَيْهِمْ يَخِرُّونَ لِلْأَذْقَانِ سُجَّدًا, tr:izâ yutlâ ʿaleyhim yahirrûne li'l-ezkâni succedâ, gloss:onlara okununca çeneleri üstüne secdeye kapanırlar, source:17:107}. Sekizinci ayetteki dönüş kelimesinin ailesinde okuyan sesin kendi üzerine dönmesi de vardır: {ar:الترجيع ترديد الصوت باللحن في القراءة, tr:et-terciʿ terdîdu's-savti bi'l-lahni fi'l-kırâ'e, gloss:tercî, okumada sesi ezgiyle tekrar tekrar döndürmektir, source:"ر ج ع,B007"}. Aynı ilk emir, hesap gününde her nefse kendi kaydı için verilir: {ar:ٱقْرَأْ كِتَٰبَكَ كَفَىٰ بِنَفْسِكَ ٱلْيَوْمَ عَلَيْكَ حَسِيبًا, tr:ikra' kitâbeke kefâ bi nefsike'l-yevme ʿaleyke hasîbâ, gloss:kitabını oku, bugün hesap sorucu olarak sana kendin yetersin, source:17:14}.

Bu sahne okumayı bir eylemler zinciri olarak gösterir: toplamak, söylemek, öğretmek, yazıyla sabitlemek ve sonunda secdeye varmak.

Kaynaklar: 96:1 ٱقْرَأْ ق ر ء B001; 96:1 ٱقْرَأْ ق ر ء B002; 96:1 ٱقْرَأْ ق ر ء B012; 96:1 ٱقْرَأْ ق ر ء B006; 96:4 عَلَّمَ ع ل م B001; 96:4 بِٱلْقَلَمِ ق ل م B003; 96:1 رَبِّكَ ر ب ب B003; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B007; 96:3 ٱلْأَكْرَمُ ك ر م B001

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

## Buluşmalar

İmgeler en açık şekilde baş sahnesinde buluşur. On beşinci ayetin fiili hem perçemden tutmak hem de yüzü karartmaktır. Böylece başın önü, avın yakalandığı yer, huysuz hayvanın tutulduğu yer ve ateşin yaladığı deri aynı noktada birleşir. Aynı alın son ayette yere konur ve secde izini taşır. İşaret imgesi buraya da uzanır: bir alın kararmış bir lekeyle işaretlenir, öteki secdenin iziyle. Kurân her iki tarafı da yüzlerindeki işaretle tanıtır: biri {ar:مِّنْ أَثَرِ ٱلسُّجُودِ, tr:min eseri's-sucûd, gloss:secdenin izinden, source:48:29}, öteki {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. Sure ad ile başlar ve iki işaretli alınla biter.

Göz ile yeterlilik imgeleri yedinci ayette buluşur. Kendini aynada gören adam ile süse ihtiyaç duymayan güzel kadın aynı kelime çiftinde birleşir: kendini görmek ve yeterli saymak. Su imgesi de buna bağlanır. Azan insan ölçüsünü aşan bir taşkın gibidir; on beşinci ayette durması istenir. Kökün göletteki duruluşu adlandırdığı hatırlanırsa, sekizinci ayet bu suyun nereye varacağını söyler. Kurân'ın varış ayeti bu iki imgeyi aynı yapıda birleştirir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Yol imgesi de bu dönüşe katılır, çünkü dönüş başlangıca dönmektir ve bu başlangıç rahimdeki ilk tutunuştur.

Rahim ile okuma, surenin ilk kelimesinde buluşur. Okumanın kökü hem rahmin bir şeyi toplayıp tutmasını hem de harflerin toplanmasını adlandırır. Pıhtıyı tutan kökle sözü toplayan kök aynıdır. İnsanın yaratılışı ve öğretilmesi bu yüzden aynı işin iki yüzü olarak duyulur. Kurân'daki benzer sıra da bunu destekler: Kurân'ı öğretmek, insanı yaratmak ve ona açıklamayı öğretmek. Okuma ile secde de buluşur: okuyucu aynı zamanda kulluk edendir ve sure, ilk emri okumak, son emri secde etmek olan bir eğri çizer. Kurân bu ikisini, okunduğunda secde edenler ile etmeyenler üzerinden birleştirir.

Ateş ile çağrı imgeleri onuncu, on yedinci ve on sekizinci ayetlerde buluşur. Namaz hem çağrıdır hem de kökü ateşe girmeyi adlandırır. Adam meclisini çağırır, Allah ateşe iten bekçileri çağırır ve kul yakın meclise çağrılır. Ateşin kendisinin de çağırdığı söylenir: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Bu yüz çevirme on üçüncü ayetin fiilidir.

İtaat ile hayvan imgeleri son ayette buluşur. Rab, itaat edilen efendidir; dizgine uyan at da itaatin bir figürüdür. Kul bu yüzden kendini rab ilan eden birine boyun eğmez, yakında tutulan ve değer gören at gibi yaklaşır. Yaratma ile uydurma da on altıncı ayette buluşur. Gerçek ölçüyle yaratan Rab'bin karşısında, yalanı içinde ölçen yalancı perçem durur.

Bu buluşmalar surenin hareketini taşır. Sure, rahimde toplanan ve tutunan bir varlıkla başlar; bu varlık sözü toplamayı ve kalemle yazmayı öğrenir. Sonra kendini aynada yeterli görür, taşkın su gibi ölçüsünü aşar, başını kaldırır ve namaz kılan kulu engellemeye çalışır. Dönüş ayeti ve Allah'ın görmesi bu yükselişin önüne bir sınır koyar. Yasaklayan perçeminden yakalanır, meclisi yerine bekçiler gelir. Kul ise yüz çevirmeden, başını yere koyarak, çağrılmış olduğu yakınlığa yürür.

