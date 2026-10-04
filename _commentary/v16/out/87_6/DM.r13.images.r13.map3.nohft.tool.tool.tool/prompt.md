Focus: 87:6. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

To read a Quran passage's Arabic before you use it, run `python3 /Volumes/aro/projects/prose_generation/_commentary/v16/missing.py text <refs>` (up to 40 refs per call) as often as you need. No other command or tool is available.

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


===== _commentary/v16/work/87_6/D.r13/context.md =====
# 87:6 — focus

سَنُقْرِئُكَ فَلَا تَنسَىٰٓ

Anchor translation (canonical reading, reference only):

Sana okutacağız; böylece unutmayacaksın.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | سَنُقْرِئُكَ | نُقْرِئُ | ق ر ء | FUT;V;PRON |
| 2 | فَلَا | لَا |  | REM;NEG |
| 3 | تَنسَىٰٓ | نَسِىَ | ن س ي | V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 87 — full text (context; no pericope)

- 87:1 سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى
- 87:2 ٱلَّذِى خَلَقَ فَسَوَّىٰ
- 87:3 وَٱلَّذِى قَدَّرَ فَهَدَىٰ
- 87:4 وَٱلَّذِىٓ أَخْرَجَ ٱلْمَرْعَىٰ
- 87:5 فَجَعَلَهُۥ غُثَآءً أَحْوَىٰ
- 87:6 ◀ focus سَنُقْرِئُكَ فَلَا تَنسَىٰٓ
- 87:7 إِلَّا مَا شَآءَ ٱللَّهُ ۚ إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ
- 87:8 وَنُيَسِّرُكَ لِلْيُسْرَىٰ
- 87:9 فَذَكِّرْ إِن نَّفَعَتِ ٱلذِّكْرَىٰ
- 87:10 سَيَذَّكَّرُ مَن يَخْشَىٰ
- 87:11 وَيَتَجَنَّبُهَا ٱلْأَشْقَى
- 87:12 ٱلَّذِى يَصْلَى ٱلنَّارَ ٱلْكُبْرَىٰ
- 87:13 ثُمَّ لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ
- 87:14 قَدْ أَفْلَحَ مَن تَزَكَّىٰ
- 87:15 وَذَكَرَ ٱسْمَ رَبِّهِۦ فَصَلَّىٰ
- 87:16 بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا
- 87:17 وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ
- 87:18 إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ
- 87:19 صُحُفِ إِبْرَٰهِيمَ وَمُوسَىٰ


===== _commentary/v16/work/87_6/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ق ر ء (root_001210) — identity root of سَنُقْرِئُكَ (w1)

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

## ق ر ء (root_001211) — identity root of سَنُقْرِئُكَ (w1)

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

## ن س ي (root_001501) — identity root of تَنسَىٰٓ (w3)

- **B001** hatırdan çıkma veya akılda tutmayı bırakma — önceden bilinen bir şeyi unutmak · unutma; hatırda tutmanın karşıtı · çok unutkan · çok unutkan adam · birine bir şeyi unutturmak · unutmuş gibi davranmak
  نسي فلان شيئا كان يذكره وإنه لنسي أي كثير النسيان (ayn;tahdhib)؛ النسيان خلاف الذكر والحفظ ورجل نسيان كثير النسيان (sihah)؛ ترك الإنسان ضبط ما استودع إما لضعف قلبه وإما عن غفلة وإما عن قصد (mufradat)؛ نسيت الشيء إذا لم تذكره نسيانا (maqayis)
- **B002** bilerek bırakma ve yerine getirmeme — bir şeyi bırakmak veya savsaklamak · Tanrı'yı bıraktılar, O da karşılık olarak onları bıraktı
  النسيان الترك، نسوا الله فنسيهم (sihah)؛ النسيان على الترك نتركها فلا ننسخها، وبناسيها بتاركها (tahdhib)؛ إذا نسب ذلك إلى الله فهو تركه إياهم استهانة بهم ومجازاة لما تركوه (mufradat)؛ الثاني ترك شيء، فترك العهد (maqayis)
- **B003** unutulup atılmış değersiz şey — unutulmuş veya atılmış, önemsenmeyen şey · unutulup atılmış, yok sayılan şey · göç edenlerin geride bıraktığı değersiz ufak tefek eşya
  النسي الشيء المنسي الذي لا يذكر ويقال هو خرقة الحائض (ayn)؛ النسي والنسي ما تلقيه المرأة من خرق اعتلالها والنسي أيضا ما نسي وما سقط من رذال أمتعتهم (sihah)؛ الشيء المطروح لا يؤبه له، انظروا أنساءكم أي الشيء اليسير (tahdhib)؛ النسي ما يقل الاعتداد به وما من شأنه أن ينسى (mufradat)؛ النسي ما سقط من منازل المرتحلين من رذال أمتعتهم (maqayis)
- **B004** kalçadan bacağa uzanan damar — kalçadan veya uyluk ayrımından bacağa uzanan damar · bu damarın iki tanesi · bu damarın çoğulu · kalçadan bacağa uzanan damarı ağrımak · birinin bu damarına vurmak · bu damarı ağrıyan
  النسا عرق يأخذ من منشق ما بين الفخذين وهما نسيان وجمعه أنساء (ayn)؛ النسا عرق يخرج من الورك والجمع أنساء ويقال نسي الرجل إذا اشتكى نساه (sihah)؛ الذي يشتكي نساه نس ورجل أنسى وامرأة نسيا إذا اشتكيا عرق النسا (tahdhib)؛ النسا عرق وتثنيته نسيان وجمعه أنساء (mufradat)؛ ومما شذ عن الأصلين النسا عرق والجمع أنساء والاثنان نسيان (maqayis)
- **B005** sonraya bırakma ve süreyi uzatma — bir şeyi ertelemek veya uzak bir zamana bırakmak · kadının aybaşı gecikmek · ödemesi sonraya bırakılan satış · dokunulmaz ayın yerini sonraya kaydırma · develerin susuz kalacağı süreye bir iki gün eklemek · dökülmeden sonra geç çıkan deve tüyü
  معنى أنسيت أخرت (ayn)؛ ولا منسيها أي ولا مؤخرها من أنسأت الدين أي أخرته (tahdhib)؛ إذا همز تغير المعنى إلى تأخير الشيء، ونسئت المرأة تأخر حيضها، والنسيئة بيعك الشيء نساء، ونسأ الله في أجلك، والنسيء في كتاب الله التأخير، ونسأت الإبل في ظمئها، والنسء ما نبت من وبر الناقة بعد تساقط وبرها (maqayis)
- **B006** sopayla vurup itme veya sürme — bir şeyi itip uzaklaştırmaya yarayan sopa · deveyi itme sopasıyla vurup sürmek
  ونسأتها ضربتها بالمنسأة العصا لأن العصا كأنه يبعد بها الشيء ويدفع (maqayis)؛ المنساة العصا وأصله الهمز (sihah)
- **B007** üzerine su dökülmüş süt — üzerine su dökülmüş süt
  النسيء الحليب يصب عليه الماء وهو النسء أيضا (maqayis)؛ النسي بغير همز وهو كل ما نسى العقل وهو اللبن الحليب يصب عليه ماء (tahdhib)

===== _commentary/v16/out/s087/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 87:6, and ## Buluşmalar) =====
## Rahimde toplanan, düzene konan beden

İkinci ve üçüncü ayetteki fiillerin bedene ait anlamları da vardır. Altıncı ayetteki "okutacağız" fiilinin kökü, rahmin yavrunun üzerine kapanmasını anlatır. Bu anlam en açık haliyle olumsuz cümlelerde görülür: {ar:لم تضم رحمها على ولد, tr:lem tedumma rahimehâ alâ veled, gloss:rahmini bir yavrunun üzerine kapamadı, source:"ق ر ء,B004"}, {ar:ما قرأت الناقة سلى قط, tr:mâ karaeti'n-nâkatu selen katt, gloss:dişi deve hiç yavru zarı toplamadı, source:"ق ر ء,B004"}. خلق, biçimi ortaya çıkmış cenindir: {ar:مضغة مخلقة أي تامة الخلق, tr:mudğatun muhallakatun ey tâmmetu'l-halk, gloss:yaratılışı tamamlanmış et parçası, source:"خ ل ق,B003"}. Biçimi çıkmamış olan için {ar:غير مخلقة لم تصور, tr:ğayru muhallakatin lem tusavvar, gloss:biçimlenmemiş olan, source:"خ ل ق,B003"} denir. سوّى, kusursuz kılınmış bedendir: {ar:السوي الذي سوى الله خلقه لا دمامة فيه ولا داء, tr:es-seviyy elleẕî sevvallâhu halkahû lâ demâmete fîhi ve lâ dâ', gloss:seviyy Allah'ın yaratılışını düzgün kıldığı kişidir; onda ne çirkinlik ne hastalık vardır, source:"س و ي,B002"}. Aynı kök gençliğin doruğuna varmayı da anlatır: {ar:استوى الرجل إذا انتهى شبابه, tr:istevâ'r-raculu iẕe'ntehâ şebâbuh, gloss:adam gençliği tamamlanınca istevâ denir, source:"س و ي,B005"}. قدّر her şeyi kendi ölçüsüne koymaktır: {ar:يجعلها على مقدار مخصوص ووجه مخصوص حسبما اقتضت الحكمة, tr:yec'aluhâ alâ mikdârin mahsûsin ve vechin mahsûsin hasebe mekteḍati'l-hikme, gloss:onu hikmetin gerektirdiği özel bir miktara ve özel bir biçime koyar, source:"ق د ر,B002"}. Rab, çocuğu evre evre büyütendir: {ar:رببت الصبي أربه, tr:rabebtu's-sabiyye erubbuh, gloss:çocuğu büyüttüm, source:"ر ب ب,B002"}. On altıncı ayetteki الدنيا'nın kökü doğumun yaklaşmasını anlatır: {ar:أدنت الناقة إذا دنا نتاجها, tr:edneti'n-nâkatu iẕâ denâ nitâcuhâ, gloss:dişi devenin doğumu yaklaştı, source:"د ن و,B004"}. On ikinci ayetteki الكبرى'nın kökü de yaşlılığı verir: {ar:الكبر في السن وقد كبر الرجل أي أسن, tr:el-kiber fi's-sinn ve kad kebira'r-racul ey esenne, gloss:kiber yaştaki büyüklüktür; adam yaşlandı, source:"ك ب ر,B004"}. Bu kelimelerin hiçbiri ayetlerinde bedeni anlatmaz. Ama aileleri, surenin yaratma ve düzene koyma fiillerini bir insan ömrünün evreleri olarak da duyurur: rahimde toplanma, biçimlenme, düzgünleşme, olgunluk ve yaşlılık.

Kur'an ikinci ayetteki ikiliyi tam olarak cenin için kullanır. Allah insanın başıboş bırakılacağını sanmasını sorgulayan ayetlerde şöyle der: {ar:أَلَمْ يَكُ نُطْفَةًۭ مِّن مَّنِىٍّۢ يُمْنَىٰ, tr:e-lem yeku nutfeten min meniyyin yumnâ, gloss:o dökülen meniden bir damla değil miydi, source:75:37}, {ar:ثُمَّ كَانَ عَلَقَةًۭ فَخَلَقَ فَسَوَّىٰ, tr:ŝumme kâne alakaten fe-halaka fe-sevvâ, gloss:sonra bir alaka oldu; O da yarattı ve düzene koydu, source:75:38}. Bu kısa bölüm şu soruyla biter: {ar:أَلَيْسَ ذَٰلِكَ بِقَٰدِرٍ عَلَىٰٓ أَن يُحْۦِىَ ٱلْمَوْتَىٰ, tr:e-leyse ẕâlike bi-kâdirin alâ en yuhyiye'l-mevtâ, gloss:bunu yapan ölüleri diriltmeye kadir değil midir, source:75:40}. Üçüncü ayetteki "ölçmek" fiilinin kökü burada güç anlamıyla gelir, on üçüncü ayetteki "yaşamak" fiili de diriltme anlamıyla. Başka bir yerde insana {ar:ٱلَّذِى خَلَقَكَ فَسَوَّىٰكَ فَعَدَلَكَ, tr:elleẕî halakake fe-sevvâke fe-adeleke, gloss:seni yaratan ve düzene koyup dengeleyen, source:82:7} denir. Yeniden dirilişten şüphe edenlere ise Allah şöyle seslenir: {ar:ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ, tr:ŝumme min mudğatin muhallakatin ve ğayri muhallaka, gloss:sonra biçimlenmiş ve biçimlenmemiş bir et parçasından, source:22:5}. Aynı ayet bazılarının ömrün en düşkün çağına geri itildiğini söyler ve sonra toprağa döner: {ar:فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:fe-iẕâ enzelnâ aleyhe'l-mâe'htezzet ve rabet, gloss:üzerine suyu indirdiğimizde titreşip kabarır, source:22:5}. Beden ile otlak tek bir ayette yan yana gelir. İnsanın yaratılışı başka bir yerde {ar:ثُمَّ سَوَّىٰهُ وَنَفَخَ فِيهِ مِن رُّوحِهِۦ, tr:ŝumme sevvâhu ve nefaha fîhi min rûhih, gloss:sonra onu düzene koydu ve ona kendi ruhundan üfledi, source:32:9} diye anlatılır. İki bahçe benzetmesinde, bahçesine güvenen adama arkadaşı şöyle der: {ar:أَكَفَرْتَ بِٱلَّذِى خَلَقَكَ مِن تُرَابٍۢ ثُمَّ مِن نُّطْفَةٍۢ ثُمَّ سَوَّىٰكَ رَجُلًۭا, tr:e-kefarte billeẕî halakake min turâbin ŝumme min nutfetin ŝumme sevvâke racülâ, gloss:seni topraktan sonra bir damladan yaratan sonra seni bir adam olarak düzene koyanı mı inkâr ettin, source:18:37}. Bu sözlerden birkaç ayet sonra o bahçe yıkılır, hemen ardından da dünya hayatının kuruyan ot benzetmesi gelir. Düzene konmuş beden ile kuruyan otlak Kur'an'da aynı uyarının iki yüzüdür.

Kaynaklar: 87:6 سَنُقْرِئُكَ ق ر ء B004; 87:2 خَلَقَ خ ل ق B003; 87:2 فَسَوَّىٰ س و ي B002; 87:2 فَسَوَّىٰ س و ي B005; 87:3 قَدَّرَ ق د ر B002; 87:1 رَبِّ ر ب ب B002; 87:16 ٱلدُّنْيَا د ن و B004; 87:12 ٱلْكُبْرَىٰ ك ب ر B004

## Toplanan, tutulan, düşürülen: okuma, unutma ve sayfalar

Altıncı ayet {ar:سَنُقْرِئُكَ فَلَا تَنسَىٰٓ, tr:se-nukriuke fe-lâ tensâ, gloss:sana okutacağız da unutmayacaksın, source:87:6} der. Yedinci ayet buna bir istisna ekler: {ar:إِلَّا مَا شَآءَ ٱللَّهُ, tr:illâ mâ şâallâh, gloss:Allah'ın dilediği hariç, source:87:7}. Kelimelerin aileleri hafızayı bir kaplar dizisi olarak gösterir. قرأ toplamaktır: {ar:قرأت الشيء قرآنا جمعته وضممت بعضه إلى بعض, tr:karaeu'ş-şey'e kur'ânen ceme'tuhû ve damamtu ba'dahû ilâ ba'd, gloss:bir şeyi okudum yani onu toplayıp parçalarını birbirine kattım, source:"ق ر ء,B001"}. Okuma harfleri ve kelimeleri birbirine eklemektir: {ar:القراءة ضم الحروف والكلمات بعضها إلى بعض في الترتيل, tr:el-kırâe dammu'l-hurûfi ve'l-kelimâti ba'dihâ ilâ ba'din fi't-tertîl, gloss:okuma harfleri ve kelimeleri tertil içinde birbirine eklemektir, source:"ق ر ء,B001"}. Ayetteki fiil başkasına bu toplamayı vermektir: {ar:أقرأت غيري أقرئه إقراء, tr:akra'tu ğayrî ukriuhû ikrâen, gloss:başkasına okuttum, source:"ق ر ء,B002"}. Unutmak ise emanet edilmiş bir şeyi tutamamaktır: {ar:ترك الإنسان ضبط ما استودع إما لضعف قلبه وإما عن غفلة وإما عن قصد, tr:terku'l-insâni dabta mâ'stûdia immâ li-da'fi kalbihî ve immâ an ğafletin ve immâ an kasd, gloss:insanın kendisine emanet edileni tutmayı bırakmasıdır; ya kalbinin zayıflığından ya gaflettendir ya da kasıtla, source:"ن س ي,B001"}. {ar:النسيان خلاف الذكر والحفظ, tr:en-nisyân hilâfu'ẕ-ẕikri ve'l-hıfz, gloss:unutmak anmanın ve korumanın zıddıdır, source:"ن س ي,B001"}. Unutmak bırakmak da demektir: {ar:النسيان الترك، نسوا الله فنسيهم, tr:en-nisyânu't-terk nesullâhe fe-nesiyehum, gloss:unutmak bırakmaktır; Allah'ı unuttular o da onları unuttu, source:"ن س ي,B002"}. Ve göç edenlerin geride bıraktığı döküntüdür: {ar:النسي ما سقط من منازل المرتحلين من رذال أمتعتهم, tr:en-nisy mâ sekata min menâzili'l-murtehilîne min ruẕâli emtiatihim, gloss:nisy göç edenlerin konak yerlerinden düşen değersiz eşyadır, source:"ن س ي,B003"}.

Dokuzuncu, onuncu ve on beşinci ayetlerdeki ذكر kökü bu düşüşün karşıtıdır: {ar:ذكرت الشيء خلاف نسيته, tr:ẕekertu'ş-şey'e hilâfu nesîtuh, gloss:bir şeyi andım unuttumun zıddıdır, source:"ذ ك ر,B003"}. {ar:الذكر الحفظ للشيء وهو مني على ذكر, tr:eẕ-ẕikru'l-hıfzu li'ş-şey'i ve huve minnî alâ ẕikr, gloss:zikir bir şeyi korumaktır; o benim aklımdadır, source:"ذ ك ر,B003"}. {ar:والتذكر طلب ما فات, tr:ve't-teẕekkuru talebu mâ fât, gloss:tezekkür kaçanı aramaktır, source:"ذ ك ر,B003"}. Öğüt bir şeyi akla getiren araçtır: {ar:التذكرة ما تستذكر به الحاجة, tr:et-teẕkira mâ tusteẕkeru bihi'l-hâce, gloss:teẕkira bir ihtiyacın hatırlandığı şeydir, source:"ذ ك ر,B009"}. Bir peygamberin kitabının adı da aynı köktendir: {ar:الذكر الكتاب الذي فيه تفصيل الدين وكل كتاب من كتب الأنبياء ذكر, tr:eẕ-ẕikru'l-kitâbu'lleẕî fîhi tafsîlu'd-dîn ve kullu kitâbin min kutubi'l-enbiyâi ẕikr, gloss:zikir dinin ayrıntılarını içeren kitaptır ve peygamberlerin her kitabı bir zikirdir, source:"ذ ك ر,B006"}. Bu anlam dokuzuncu ayetteki öğüdü on sekizinci ve on dokuzuncu ayetlerdeki sayfalara bağlar. Sayfalar, üzerine yazı yazılan deri parçalarıdır: {ar:الصحف واحدتها صحيفة وهي القطعة من أدم أبيض أو رق يكتب فيها, tr:es-suhuf vâhidetuhâ sahîfe ve hiye'l-kıtatu min edemin ebyada ev rakkın yuktebu fîhâ, gloss:suhuf sahîfenin çoğuludur; sahîfe üzerine yazılan ak deri ya da parşömen parçasıdır, source:"ص ح ف,B002"}. Mushaf bu sayfaları bir araya toplayandır: {ar:المصحف ما جعل جامعا للصحف المكتوبة, tr:el-mushaf mâ cuile câmian li's-suhufi'l-mektûbe, gloss:mushaf yazılı sayfaları toplamak için yapılmış şeydir, source:"ص ح ف,B003"}. "İlk" kelimesi bir şeyin başlangıcıdır: {ar:الأول وهو مبتدأ الشيء, tr:el-evvel ve huve mubtedeu'ş-şey', gloss:evvel bir şeyin başlangıcıdır, source:"ء و ل,B001"}. On altıncı ayetteki tercih fiilinin kökü de söz aktarmayı verir: {ar:أثرت الحديث إذا ذكرته عن غيرك وحديث مأثور, tr:eŝertu'l-hadîŝe iẕâ ẕekertehû an ğayrike ve hadîŝun me'ŝûr, gloss:bir sözü başkasından naklettiğinde eŝertu denir; aktarılan söze me'ŝûr denir, source:"ء ث ر,B002"}.

Bu aileler altıncı ayetle son ayet arasında bir yol çizer. Okutulan söz toplanır ve birbirine eklenir. Unutulmayınca tutulur. Unutulursa göç yerindeki döküntü gibi geride kalır. Anılarak geri çağrılır. Sonunda deriye yazılıp sayfa olur, sayfalar da bir arada toplanır. On sekizinci ayetteki {ar:إِنَّ هَٰذَا لَفِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:inne hâẕâ le-fi's-suhufi'l-ûlâ, gloss:bu elbette ilk sayfalarda vardır, source:87:18} cümlesi, okutulan sözün yalnız Peygamber'in hafızasında değil, İbrahim'in ve Musa'nın sayfalarında da toplanmış olduğunu söyler. Düz bir anlatımda "unutmayacaksın" bir vaattir. Aile resmi ise bu vaadin işleyişini gösterir: toplayan Allah'tır, ve toplanan şey düşürülmez.

Kur'an toplama ile okumayı aynı cümlede verir. Allah Peygamber'e vahyi acele ile tekrarlamamasını söyler: {ar:لَا تُحَرِّكْ بِهِۦ لِسَانَكَ لِتَعْجَلَ بِهِۦٓ, tr:lâ tuharrik bihî lisâneke li-ta'cele bih, gloss:onu aceleyle almak için dilini kıpırdatma, source:75:16}, {ar:إِنَّ عَلَيْنَا جَمْعَهُۥ وَقُرْءَانَهُۥ, tr:inne aleynâ cem'ahû ve kur'ânah, gloss:onu toplamak ve okutmak bize düşer, source:75:17}, {ar:فَإِذَا قَرَأْنَٰهُ فَٱتَّبِعْ قُرْءَانَهُۥ, tr:fe-iẕâ kara'nâhu fettebi' kur'ânah, gloss:onu okuduğumuzda sen okunuşunu izle, source:75:18}. Başka bir yerde de {ar:وَلَا تَعْجَلْ بِٱلْقُرْءَانِ مِن قَبْلِ أَن يُقْضَىٰٓ إِلَيْكَ وَحْيُهُۥ ۖ وَقُل رَّبِّ زِدْنِى عِلْمًۭا, tr:ve lâ ta'cel bi'l-kur'âni min kabli en yukdâ ileyke vahyuh ve kul rabbi zidnî ilmâ, gloss:sana vahyi tamamlanmadan Kur'an'ı okumakta acele etme ve Rabbim ilmimi artır de, source:20:114} denir. Hemen ardından unutmanın ilk örneği gelir: {ar:وَلَقَدْ عَهِدْنَآ إِلَىٰٓ ءَادَمَ مِن قَبْلُ فَنَسِىَ وَلَمْ نَجِدْ لَهُۥ عَزْمًۭا, tr:ve lekad ahidnâ ilâ âdeme min kablu fe-nesiye ve lem necid lehû azmâ, gloss:andolsun daha önce Adem'e söz vermiştik; o unuttu ve onda bir kararlılık bulmadık, source:20:115}. Firavun Musa'ya {ar:فَمَا بَالُ ٱلْقُرُونِ ٱلْأُولَىٰ, tr:fe-mâ bâlu'l-kurûni'l-ûlâ, gloss:ya önceki nesillerin durumu ne olacak, source:20:51} diye sorduğunda Musa şöyle cevap verir: {ar:عِلْمُهَا عِندَ رَبِّى فِى كِتَٰبٍۢ ۖ لَّا يَضِلُّ رَبِّى وَلَا يَنسَى, tr:ilmuhâ inde rabbî fî kitâb lâ yadillu rabbî ve lâ yensâ, gloss:onların bilgisi Rabbimin katında bir kitaptadır; Rabbim ne yanılır ne unutur, source:20:52}. Bu cevapta "ilk" kelimesi, yazılı kitap ve unutmayan Rab bir aradadır. Unutmanın karşılığı da aynı kelimeyle verilir: {ar:كَذَٰلِكَ أَتَتْكَ ءَايَٰتُنَا فَنَسِيتَهَا ۖ وَكَذَٰلِكَ ٱلْيَوْمَ تُنسَىٰ, tr:keẕâlike etetke âyâtunâ fe-nesîtehâ ve keẕâlike'l-yevme tunsâ, gloss:ayetlerimiz sana geldi ama sen onları unuttun; bugün de sen öyle unutulursun, source:20:126}. Münafıklar için {ar:نَسُوا۟ ٱللَّهَ فَنَسِيَهُمْ, tr:nesullâhe fe-nesiyehum, gloss:Allah'ı unuttular o da onları unuttu, source:9:67} denir. Müminlere de {ar:وَلَا تَكُونُوا۟ كَٱلَّذِينَ نَسُوا۟ ٱللَّهَ فَأَنسَىٰهُمْ أَنفُسَهُمْ, tr:ve lâ tekûnû kelleẕîne nesullâhe fe-ensâhum enfusehum, gloss:Allah'ı unutan ve bu yüzden Allah'ın onlara kendilerini unutturduğu kimseler gibi olmayın, source:59:19} denir. Yedinci ayetteki istisnanın bir benzeri Peygamber'e verilen bir emirde de geçer: {ar:إِلَّآ أَن يَشَآءَ ٱللَّهُ ۚ وَٱذْكُر رَّبَّكَ إِذَا نَسِيتَ, tr:illâ en yeşâallâh veẕkur rabbeke iẕâ nesît, gloss:ancak Allah dilerse; unuttuğunda Rabbini an, source:18:24}. Unutmaya karşı çare anmaktır.

Sayfaların içeriği başka bir yerde kısmen verilir: {ar:أَمْ لَمْ يُنَبَّأْ بِمَا فِى صُحُفِ مُوسَىٰ, tr:em lem yunebbe' bi-mâ fî suhufi mûsâ, gloss:yoksa Musa'nın sayfalarındakiler ona haber verilmedi mi, source:53:36}, {ar:وَإِبْرَٰهِيمَ ٱلَّذِى وَفَّىٰٓ, tr:ve ibrâhîme'lleẕî veffâ, gloss:ve sözünü tam yerine getiren İbrahim'in sayfalarındakiler, source:53:37}. Sayfalarda yazanların ilki şudur: {ar:أَلَّا تَزِرُ وَازِرَةٌۭ وِزْرَ أُخْرَىٰ, tr:ellâ teziru vâziratun vizra uhrâ, gloss:hiçbir yük taşıyan başkasının yükünü taşımaz, source:53:38}. Ardından {ar:وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ, tr:ve en leyse li'l-insâni illâ mâ seâ, gloss:insan için kendi çabasından başkası yoktur, source:53:39} gelir, ve dizi şöyle biter: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Her kişinin kendi payını taşıması, bu surenin iki kişiye ayrılan ortasıyla aynı konudur. Delil isteyenlere de {ar:أَوَلَمْ تَأْتِهِم بَيِّنَةُ مَا فِى ٱلصُّحُفِ ٱلْأُولَىٰ, tr:e-ve lem te'tihim beyyinetu mâ fi's-suhufi'l-ûlâ, gloss:ilk sayfalardakinin açık delili onlara gelmedi mi, source:20:133} denir. Başka bir yerde öğüt ve sayfa birlikte anılır: {ar:كَلَّآ إِنَّهَا تَذْكِرَةٌۭ, tr:kellâ innehâ teẕkira, gloss:hayır bu bir öğüttür, source:80:11}, {ar:فَمَن شَآءَ ذَكَرَهُۥ, tr:fe-men şâe ẕekerah, gloss:dileyen onu anar, source:80:12}, {ar:فِى صُحُفٍۢ مُّكَرَّمَةٍۢ, tr:fî suhufin mukerrame, gloss:değerli sayfalardadır, source:80:13}, {ar:مَّرْفُوعَةٍۢ مُّطَهَّرَةٍۭ, tr:merfûatin mutahhara, gloss:yükseltilmiş ve arınmış, source:80:14}. Sayfalar yükseltilmiş ve arınmıştır. Bu iki sıfat surenin birinci ayetindeki yüksekliği ve on dördüncü ayetindeki arınmayı sayfalara taşır. Kur'an kendisi için de {ar:وَإِنَّهُۥ لَفِى زُبُرِ ٱلْأَوَّلِينَ, tr:ve innehû le-fî zuburi'l-evvelîn, gloss:o öncekilerin kitaplarında da vardır, source:26:196} der.

Kaynaklar: 87:6 سَنُقْرِئُكَ ق ر ء B001; 87:6 سَنُقْرِئُكَ ق ر ء B002; 87:6 تَنسَىٰٓ ن س ي B001; 87:6 تَنسَىٰٓ ن س ي B002; 87:6 تَنسَىٰٓ ن س ي B003; 87:9 ٱلذِّكْرَىٰ ذ ك ر B003; 87:10 يَذَّكَّرُ ذ ك ر B003; 87:9 ٱلذِّكْرَىٰ ذ ك ر B009; 87:9 ٱلذِّكْرَىٰ ذ ك ر B006; 87:18 ٱلصُّحُفِ ص ح ف B002; 87:19 صُحُفِ ص ح ف B003; 87:18 ٱلْأُولَىٰ ء و ل B001; 87:16 تُؤْثِرُونَ ء ث ر B002

## Açık ve gizli: ses ve örtüden çıkan

Yedinci ayetin sonu {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ وَمَا يَخْفَىٰ, tr:innehû ya'lemu'l-cehra ve mâ yahfâ, gloss:O açığa vurulanı da gizli kalanı da bilir, source:87:7} der. Bu cümle iki ayrı sahnede duyulur. Birincisi sestir. جهر sesi yükseltmektir: {ar:جهر بالقول رفع به صوته, tr:cehera bi'l-kavli rafea bihî savtah, gloss:sözü açıktan söyledi yani sesini yükseltti, source:"ج ه ر,B001"}. {ar:الجهر ضد السر, tr:el-cehru diddu's-sirr, gloss:cehr gizlinin zıddıdır, source:"ج ه ر,B001"}. Bu kök tek bir harfin söylenişine kadar iner: {ar:سمي الحرف مجهورا لأنه أشبع الاعتماد في موضعه ومنع النفس أن يجري معه, tr:sumiye'l-harfu mechûran li-ennehû eşbea'l-i'timâde fî mevdiihî ve menea'n-nefese en yecriye meah, gloss:harfe mechûr denir çünkü çıkış yerine tam dayanır ve nefesin onunla akmasını engeller, source:"ج ه ر,B011"}. خفي sesi kısmaktır: {ar:أخفيت الصوت إخفاء ... والخافية ضد العلانية ولقيته خفيا أي سرا, tr:ahfeytu's-savte ihfâen ve'l-hâfiyetu diddu'l-alâniye ve lekîtuhû hafiyyen ey sirran, gloss:sesi kıstım; hâfiye açıklığın zıddıdır; onunla gizlice karşılaştım, source:"خ ف ي,B001"}. On beşinci ayetteki anma iki yerde yaşar: {ar:ذكرته بلساني وبقلبي, tr:ẕekertuhû bi-lisânî ve bi-kalbî, gloss:onu dilimle ve kalbimle andım, source:"ذ ك ر,B004"}. Okuma da ezberden yapılır: {ar:قرأت القرآن عن ظهر قلب أو نظرت فيه, tr:kara'tu'l-kur'âne an zahri kalbin ev nazartu fîh, gloss:Kur'an'ı ezberden ya da bakarak okudum, source:"ق ر ء,B002"}. Bilmek de söylenenin farkında olmaktır: {ar:ما علمت بخبرك أي ما شعرت به, tr:mâ alimtu bi-haberike ey mâ şaartu bih, gloss:haberini bilmedim yani farkına varmadım, source:"ع ل م,B001"}. Bu sahnede yedinci ayet, altıncı ayetteki okumanın iki halini, yüksek sesle ve içten okumayı birlikte kucaklar. Okutulan söz dilde de olsa kalpte de olsa bilinir.

İkinci sahne örtüden çıkmaktır. "Gizli" kökü, Arapçada zıt anlamları birlikte taşıyan kelimelerden biridir: {ar:خفيت الشيء بغير ألف إذا أظهرته, tr:hafeytu'ş-şey'e bi-ğayri elifin iẕâ azhartah, gloss:elifsiz hafeytu bir şeyi açığa çıkardım demektir, source:"خ ف ي,B003"}. {ar:استخفيت الشئ أي استخرجته, tr:istahfeytu'ş-şey'e ey istahrectuh, gloss:bir şeyi çıkardım, source:"خ ف ي,B003"}. Bu ikinci açıklama dördüncü ayetin "çıkarmak" kökünü kullanır, ki o kökün temel anlamı şudur: {ar:خرج خروجا برز من مقره أو حاله, tr:harace hurûcen beraze min makarrihî ev hâlih, gloss:yerinden ya da halinden dışarı belirdi, source:"خ ر ج,B001"}. Örtülü olanın somut örnekleri de vardır: {ar:الخوافي سعفات يلين قلب النخلة, tr:el-havâfî saafâtun yelîne kalbe'n-nahle, gloss:havâfî hurmanın göbeğine yakın dallardır, source:"خ ف ي,B002"}. {ar:الخوافي جمع خافية وهي ما دون القوادم من الريش, tr:el-havâfî cem'u hâfiye ve hiye mâ dûne'l-kavâdimi mine'r-rîş, gloss:havâfî kanadın ön tüylerinin altında kalan tüylerdir, source:"خ ف ي,B002"}. Öbür uçta açık olan vardır: {ar:كل شيء بدا فقد جهر, tr:kullu şey'in bedâ fe-kad cehera, gloss:ortaya çıkan her şey açığa çıkmıştır, source:"ج ه ر,B002"}, ve temizlenip suyu görünen kuyu bu kökle anılır. Açıklığın bir tersi de vardır: {ar:العين الجهراء التي لا تبصر في الشمس, tr:el-aynu'l-cehrâ elletî lâ tubsiru fi'ş-şems, gloss:cehrâ göz güneşte göremeyen gözdür, source:"ج ه ر,B004"}. Fazla ışık da bir örtü olabilir. Dördüncü ayetle birlikte okununca yedinci ayetin ikilisi sabit iki durum olmaktan çıkar ve bir harekete dönüşür: yağmurla topraktan ot çıkar, deliklerden fareler çıkar. Gizli olan, Rabbin bildiği ve dilediğinde açığa çıkardığı şeydir.

Kur'an bu iki sahneyi açıkça kurar. Peygamber'e indirilen hitabın başında şöyle denir: {ar:وَإِن تَجْهَرْ بِٱلْقَوْلِ فَإِنَّهُۥ يَعْلَمُ ٱلسِّرَّ وَأَخْفَى, tr:ve in techer bi'l-kavli fe-innehû ya'lemu's-sirra ve ahfâ, gloss:sözü yüksek sesle söylesen de O gizliyi ve daha gizlisini bilir, source:20:7}. Bu, Musa'nın ateşi gördüğü sahneye geçmeden önceki ayetlerdendir. Aynı hikâyede ateşin başında {ar:إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ أَكَادُ أُخْفِيهَا, tr:inne's-sâate âtiyetun ekâdu uhfîhâ, gloss:o saat gelecektir; onu neredeyse gizli tutuyorum, source:20:15} denir. Sesin ölçüsü bir emirle verilir: {ar:وَلَا تَجْهَرْ بِصَلَاتِكَ وَلَا تُخَافِتْ بِهَا وَٱبْتَغِ بَيْنَ ذَٰلِكَ سَبِيلًۭا, tr:ve lâ techer bi-salâtike ve lâ tuhâfit bihâ vebteğı beyne ẕâlike sebîlâ, gloss:namazında sesini ne yükselt ne de kıs; ikisinin arasında bir yol tut, source:17:110}. Anmanın sesi de belirlenir: {ar:وَٱذْكُر رَّبَّكَ فِى نَفْسِكَ تَضَرُّعًۭا وَخِيفَةًۭ وَدُونَ ٱلْجَهْرِ مِنَ ٱلْقَوْلِ, tr:veẕkur rabbeke fî nefsike tedarruan ve hîfeten ve dûne'l-cehri mine'l-kavl, gloss:Rabbini içinden yalvararak ve korkarak ve yüksek olmayan bir sesle an, source:7:205}. Duanın sesi de: {ar:ٱدْعُوا۟ رَبَّكُمْ تَضَرُّعًۭا وَخُفْيَةً, tr:ud'û rabbekum tedarruan ve hufye, gloss:Rabbinize yalvararak ve gizlice dua edin, source:7:55}. Allah için {ar:إِنَّهُۥ يَعْلَمُ ٱلْجَهْرَ مِنَ ٱلْقَوْلِ وَيَعْلَمُ مَا تَكْتُمُونَ, tr:innehû ya'lemu'l-cehra mine'l-kavli ve ya'lemu mâ tektumûn, gloss:O sözün açığını da bilir gizlediğinizi de bilir, source:21:110} ve {ar:يَعْلَمُ سِرَّكُمْ وَجَهْرَكُمْ, tr:ya'lemu sirrakum ve cehrakum, gloss:gizlinizi de açığınızı da bilir, source:6:3} denir. Örtüden çıkarma sahnesini ise Süleyman'a haber getiren hüdhüd anlatır. Hüdhüd bir kavmin güneşe secde ettiğini, şeytanın onları yoldan çevirdiğini söyler ve şöyle ekler: {ar:أَلَّا يَسْجُدُوا۟ لِلَّهِ ٱلَّذِى يُخْرِجُ ٱلْخَبْءَ فِى ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ وَيَعْلَمُ مَا تُخْفُونَ وَمَا تُعْلِنُونَ, tr:ellâ yescudû lillâhi'lleẕî yuhricu'l-hab'e fi's-semâvâti ve'l-ardi ve ya'lemu mâ tuhfûne ve mâ tu'linûn, gloss:göklerde ve yerde saklı olanı çıkaran ve gizlediğinizi de açıkladığınızı da bilen Allah'a secde etmesinler diye, source:27:25}. Bu tek ayette dördüncü ayetteki "çıkarmak" ile yedinci ayetteki gizli ve açık bir arada bulunur.

Kaynaklar: 87:7 ٱلْجَهْرَ ج ه ر B001; 87:7 ٱلْجَهْرَ ج ه ر B011; 87:7 ٱلْجَهْرَ ج ه ر B002; 87:7 ٱلْجَهْرَ ج ه ر B004; 87:7 يَخْفَىٰ خ ف ي B001; 87:7 يَخْفَىٰ خ ف ي B003; 87:7 يَخْفَىٰ خ ف ي B002; 87:15 وَذَكَرَ ذ ك ر B004; 87:6 سَنُقْرِئُكَ ق ر ء B002; 87:7 يَعْلَمُ ع ل م B001; 87:4 أَخْرَجَ خ ر ج B001

## Seçmek: seçkin ve döküntü

On altıncı ayet {ar:بَلْ تُؤْثِرُونَ ٱلْحَيَوٰةَ ٱلدُّنْيَا, tr:bel tu'ŝirûne'l-hayâte'd-dunyâ, gloss:hayır; siz dünya hayatını tercih ediyorsunuz, source:87:16} der. On yedinci ayet buna şöyle karşılık verir: {ar:وَٱلْءَاخِرَةُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:ve'l-âhiratu hayrun ve ebkâ, gloss:oysa ahiret daha hayırlı ve daha kalıcıdır, source:87:17}. Tercih fiili, bir şeyi kayırıp kendine ayırmaktır. Kayırılan kişi {ar:الأثير الكريم عليك الذي تؤثره بفضلك وصلتك, tr:el-eŝîr el-kerîmu aleyke'lleẕî tu'ŝiruhû bi-fadlike ve sıletik, gloss:esîr senin için değerli olandır; ona iyiliğinle ve bağışınla öncelik verirsin, source:"ء ث ر,B005"}. Başkasını kendine tercih etmek de bu köktendir: {ar:آثرت فلانا على نفسي من الإيثار, tr:âŝertu fulânen alâ nefsî mine'l-îŝâr, gloss:falancayı kendime tercih ettim, source:"ء ث ر,B005"}. Kendine ayırmak da: {ar:استأثر الله بالبقاء أي انفرد بالبقاء, tr:ista'ŝerallâhu bi'l-bekâi ey infarada bi'l-bekâ, gloss:Allah kalıcılığı kendine ayırdı yani kalıcılıkta tek kaldı, source:"ء ث ر,B006"}. Bu ifade on altıncı ayetin fiilini on yedinci ayetin kalıcılığına bağlar. Seçmek daha iyiyi aramaktır: {ar:الاختيار طلب ما هو خير وفعله, tr:el-ihtiyâru talebu mâ huve hayrun ve fi'luh, gloss:seçmek daha hayırlı olanı arayıp yapmaktır, source:"خ ي ر,B003"}. Seçilmiş olan döküntü içermez: {ar:فيهن مختارات لا رذل فيهن, tr:fîhinne muhtârâtun lâ reẕle fîhinn, gloss:onların arasında seçkinler var; aralarında döküntü yok, source:"خ ي ر,B002"}. Mal ancak bol ve temiz kaynaklı olunca hayır diye anılmayı hak eder: {ar:لا يقال للمال خير حتى يكون كثيرا ومن مكان طيب, tr:lâ yukâlu li'l-mâli hayrun hattâ yekûne keŝîran ve min mekânin tayyib, gloss:mal bol olmadıkça ve temiz bir yerden gelmedikçe ona hayır denmez, source:"خ ي ر,B004"}.

Öbür kefede dünya kelimesinin kökünden gelen aşağılık vardır: {ar:خص الدنيء بالحقير القدر, tr:hussa'd-denîu bi'l-hakîri'l-kadr, gloss:denî değeri düşük olana özgü kılınmıştır, source:"د ن و,B003"}. {ar:الأدنى عن الأرذل, tr:el-ednâ ani'l-erẕel, gloss:ednâ en aşağılık olanı anlatır, source:"د ن و,B003"}. "Değer" diye çevrilen kelime üçüncü ayetteki ölçmek fiilinin köküdür. Beşinci ayetin döküntüsü insanlar için de kullanılır: {ar:يقال لسفلة الناس الغثاء تشبيها بالذي ذكرناه, tr:yukâlu li-sefeleti'n-nâsi'l-ğuŝâ teşbîhen bi'lleẕî ẕekernâh, gloss:insanların aşağısına da ona benzetilerek ğuŝâ denir, source:"غ ث و,B004"}. Göç yerinde düşürülen değersiz eşya da bu kefededir. Kalan şey ise hâlâ iyilik taşır: {ar:أولو بقية من دين قوم لهم بقية إذا كانت بهم مسكة وفيهم خير, tr:ulû bakıyyetin min dînin kavmun lehum bakıyyetun iẕâ kânet bihim misketun ve fîhim hayr, gloss:dinden bir bakıyye sahipleri; tutunacak bir şeyleri ve içlerinde iyilik bulunan topluluk, source:"ب ق ي,B002"}.

Bu ayrım surenin önceki imgelerini bir seçim olarak toplar. Beşinci ayetteki çerçöp, altıncı ayetteki unutulan döküntü ve on altıncı ayetteki aşağı olan bir kefededir. On yedinci ayetteki hayırlı ve kalıcı olan, seçilmiş ve döküntüsüz olan öbür kefededir. Düz bir anlatım "dünya" ile "ahiret" arasında bir tercih görür. Kök aileleri bu tercihin bir ayıklama olduğunu duyurur: seçkin olan alınır, döküntü bırakılır. Kınanan şey ise döküntüyü seçmektir.

Kur'an bu seçimi açıkça sahneler. Firavun'un en yüce rab olma iddiasının anlatıldığı surede hüküm şudur: {ar:فَإِنَّ ٱلْجَحِيمَ هِىَ ٱلْمَأْوَىٰ, tr:fe-inne'l-cahîme hiye'l-me'vâ, gloss:artık barınağı cehennemdir, source:79:39}. Karşı tarafta {ar:وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ وَنَهَى ٱلنَّفْسَ عَنِ ٱلْهَوَىٰ, tr:ve emmâ men hâfe makâme rabbihî ve nehe'n-nefse ani'l-hevâ, gloss:Rabbinin huzuruna çıkmaktan korkan ve nefsini hevesten alıkoyana gelince, source:79:40} vardır. Musa'nın karşısındaki sihirbazlar bu seçimi tehdit altında yapar: {ar:لَن نُّؤْثِرَكَ عَلَىٰ مَا جَآءَنَا مِنَ ٱلْبَيِّنَٰتِ وَٱلَّذِى فَطَرَنَا ۖ فَٱقْضِ مَآ أَنتَ قَاضٍ ۖ إِنَّمَا تَقْضِى هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:len nu'ŝirake alâ mâ câenâ mine'l-beyyinâti velleẕî fataranâ fakdı mâ ente kâd innemâ takdî hâẕihi'l-hayâte'd-dunyâ, gloss:bize gelen açık delillere ve bizi yaratana seni asla tercih etmeyiz; vereceğin hükmü ver; sen ancak bu dünya hayatında hüküm verebilirsin, source:20:72}. Sözlerini şöyle bitirirler: {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73}. Bu iki ayette surenin on altıncı ve on yedinci ayetlerinin dört kelimesi bulunur. Peygamber'e de {ar:وَلَا تَمُدَّنَّ عَيْنَيْكَ إِلَىٰ مَا مَتَّعْنَا بِهِۦٓ أَزْوَٰجًۭا مِّنْهُمْ زَهْرَةَ ٱلْحَيَوٰةِ ٱلدُّنْيَا, tr:ve lâ temuddenne ayneyke ilâ mâ metta'nâ bihî ezvâcen minhum zehrate'l-hayâti'd-dunyâ, gloss:onlardan bazılarına verdiğimiz dünya hayatının çiçeğine gözünü dikme, source:20:131} denir. Ayet {ar:وَرِزْقُ رَبِّكَ خَيْرٌۭ وَأَبْقَىٰ, tr:ve rızku rabbike hayrun ve ebkâ, gloss:Rabbinin rızkı daha hayırlı ve daha kalıcıdır, source:20:131} diye biter. Dünya hayatı burada bir çiçektir. Otlağın imgesi seçimin tam içindedir. Aynı karşıtlık başka yerlerde de geçer: {ar:وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰٓ ۚ أَفَلَا تَعْقِلُونَ, tr:ve mâ indallâhi hayrun ve ebkâ e-fe-lâ ta'kılûn, gloss:Allah katında olan daha hayırlı ve daha kalıcıdır; akıl etmez misiniz, source:28:60}, {ar:وَمَا عِندَ ٱللَّهِ خَيْرٌۭ وَأَبْقَىٰ لِلَّذِينَ ءَامَنُوا۟, tr:ve mâ indallâhi hayrun ve ebkâ li'lleẕîne âmenû, gloss:Allah katında olan iman edenler için daha hayırlı ve daha kalıcıdır, source:42:36}, {ar:مَا عِندَكُمْ يَنفَدُ ۖ وَمَا عِندَ ٱللَّهِ بَاقٍۢ, tr:mâ indekum yenfedu ve mâ indallâhi bâk, gloss:sizin yanınızdaki tükenir; Allah'ın katındaki ise kalır, source:16:96}. Kalıcılık kötü yönde de geçer: {ar:وَلَعَذَابُ ٱلْءَاخِرَةِ أَشَدُّ وَأَبْقَىٰٓ, tr:ve le-azâbu'l-âhirati eşeddu ve ebkâ, gloss:ahiret azabı ise elbette daha çetin ve daha kalıcıdır, source:20:127}. Tercih fiili Kur'an'da iyi yönde de kullanılır. Yusuf'un kardeşleri onu tanıdıklarında {ar:تَٱللَّهِ لَقَدْ ءَاثَرَكَ ٱللَّهُ عَلَيْنَا, tr:tallâhi lekad âŝerakallâhu aleynâ, gloss:Allah'a andolsun ki Allah seni bize üstün kıldı, source:12:91} derler. Hicret edenleri barındıranlar için de {ar:وَيُؤْثِرُونَ عَلَىٰٓ أَنفُسِهِمْ وَلَوْ كَانَ بِهِمْ خَصَاصَةٌۭ, tr:ve yu'ŝirûne alâ enfusihim ve lev kâne bihim hasâsa, gloss:kendileri ihtiyaç içinde olsalar bile onları kendilerine tercih ederler, source:59:9} denir. Bu ayet {ar:فَأُو۟لَٰٓئِكَ هُمُ ٱلْمُفْلِحُونَ, tr:fe-ulâike humu'l-muflihûn, gloss:işte kurtuluşa erenler onlardır, source:59:9} diye biter. Burada tercih ile kurtuluş, yani surenin on altıncı ve on dördüncü ayetlerinin fiilleri, doğru yönde birleşir. Kalanlar da şöyle anılır: {ar:فَلَوْلَا كَانَ مِنَ ٱلْقُرُونِ مِن قَبْلِكُمْ أُو۟لُوا۟ بَقِيَّةٍۢ يَنْهَوْنَ عَنِ ٱلْفَسَادِ فِى ٱلْأَرْضِ, tr:fe-lev lâ kâne mine'l-kurûni min kablikum ulû bakıyyetin yenhevne ani'l-fesâdi fi'l-ard, gloss:sizden önceki nesiller arasında yeryüzünde bozgunculuğu önleyecek bir kalıntı sahibi olsaydı ya, source:11:116}.

Kaynaklar: 87:16 تُؤْثِرُونَ ء ث ر B005; 87:16 تُؤْثِرُونَ ء ث ر B006; 87:17 خَيْرٌۭ خ ي ر B003; 87:17 خَيْرٌۭ خ ي ر B002; 87:17 خَيْرٌۭ خ ي ر B004; 87:16 ٱلدُّنْيَا د ن و B003; 87:5 غُثَآءً غ ث و B004; 87:6 تَنسَىٰٓ ن س ي B003; 87:17 أَبْقَىٰٓ ب ق ي B002

## Buluşmalar

İmgelerin çoğu, surenin son ayetinde adı geçen Musa'nın hikâyesinde buluşur. Musa uzakta bir ateş görür ve {ar:أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ecidu ale'n-nâri hudâ, gloss:ateşin başında bir yol gösteren bulurum, source:20:10} umuduyla ona yönelir. Uzaktan görülen ateşin sahnesi ile yol sahnesi burada aynı cümlededir. Ateşin başında önce seçim gelir: {ar:وَأَنَا ٱخْتَرْتُكَ, tr:ve ene'htertuk, gloss:seni ben seçtim, source:20:13}. Sonra namaz ve anma gelir: {ar:وَأَقِمِ ٱلصَّلَوٰةَ لِذِكْرِىٓ, tr:ve ekımi's-salâte li-ẕikrî, gloss:beni anmak için namazı kıl, source:20:14}. Sonra gizli olan gelir: {ar:أَكَادُ أُخْفِيهَا, tr:ekâdu uhfîhâ, gloss:onu neredeyse gizli tutuyorum, source:20:15}. Başka bir anlatımda ateşin başında tesbih söylenir: {ar:وَسُبْحَٰنَ ٱللَّهِ رَبِّ ٱلْعَٰلَمِينَ, tr:ve subhânallâhi rabbi'l-âlemîn, gloss:Âlemlerin Rabbi Allah her kusurdan arıdır, source:27:8}. Bu sahnede surenin on ikinci ve on beşinci ayetleri arasındaki karşıtlık bir kişinin yolculuğunda çözülür. Aynı ateşe yaklaşan biri onun içine sokulmaz. Ateş ona yol, seçilmişlik, namaz ve anma verir. Surede bu iki son iki ayrı kişiye düşer: on ikinci ayetteki kişi ateşe girer, on beşinci ayetteki kişi namaz kılar. Kelimelerin harf benzerliği bu ayrılığı kulakta da duyurur.

İkinci büyük buluşma selin sahnesidir. Gökten inen suyun vadilerde {ar:بِقَدَرِهَا, tr:bi-kaderihâ, gloss:kendi ölçülerince, source:13:17} akması, ölçüp biçme sahnesini çağırır. Selin taşıdığı köpük, otlağın vardığı döküntüdür. İnsanların {ar:وَمِمَّا يُوقِدُونَ عَلَيْهِ فِى ٱلنَّارِ, tr:ve mimmâ yûkıdûne aleyhi fi'n-nâr, gloss:ateşte üzerine yaktıkları şeyden, source:13:17} çıkan köpük ise ateşin sahnesine girer. Faydalı olanın yerde kalması da öğüdün ve kalıcılığın sahnesidir. Kurumuş otun tencerenin köpüğüyle aynı adı taşıması, bu iki köpüğün Arapçada zaten tek bir kelimede birleştiğini gösterir. Bu ayet surenin beşinci ayetinden on yedinci ayetine uzanan çizgiyi tek bir manzaraya sığdırır. Bir yanda giden döküntü, öbür yanda kalan fayda vardır.

Üçüncü buluşma, Musa'nın karşısındaki sihirbazların sahnesidir. Sihirbazlar secdeye kapanır. Firavun kendi azabının daha çetin ve {ar:وَأَبْقَىٰ, tr:ve ebkâ, gloss:ve daha kalıcı, source:20:71} olduğunu söyler. Sihirbazlar da onu {ar:لَن نُّؤْثِرَكَ, tr:len nu'ŝirak, gloss:seni asla tercih etmeyiz, source:20:72} diye reddeder, yalnızca {ar:هَٰذِهِ ٱلْحَيَوٰةَ ٱلدُّنْيَآ, tr:hâẕihi'l-hayâte'd-dunyâ, gloss:bu dünya hayatı, source:20:72} üzerinde hüküm verebileceğini söyler ve {ar:وَٱللَّهُ خَيْرٌۭ وَأَبْقَىٰٓ, tr:vallâhu hayrun ve ebkâ, gloss:Allah daha hayırlı ve daha kalıcıdır, source:20:73} der. Sonra suçlu için {ar:لَا يَمُوتُ فِيهَا وَلَا يَحْيَىٰ, tr:lâ yemûtu fîhâ ve lâ yahyâ, gloss:orada ne ölür ne yaşar, source:20:74} der, iman edenler için {ar:ٱلدَّرَجَٰتُ ٱلْعُلَىٰ, tr:ed-derecâtu'l-ulâ, gloss:en yüce dereceler, source:20:75} der, ve hepsini {ar:جَزَآءُ مَن تَزَكَّىٰ, tr:cezâu men tezekkâ, gloss:arınanın karşılığı, source:20:76} sözüyle bağlar. Bu birkaç ayette seçim, kalıcı hayat, yükseklik ve yarılan tarlanın kelimeleri birlikte konuşur. Firavun'un "en yüce" iddiası da başka bir anlatımda bu sahneye eklenir. Surenin ikinci yarısı, on üçüncü ayetten on yedinci ayete kadar, neredeyse kelimesi kelimesine Musa'nın hikâyesindeki bir topluluğun ağzından gelmiştir. Son ayetin Musa'nın sayfalarını anması da bu yüzden önem taşır.

Dördüncü buluşma ot ile seçimdir. Dünya hayatının kuruyan ota benzetildiği ayetin hemen ardından kalıcı iyi işlerin daha hayırlı olduğu söylenir. Dünya hayatı başka bir yerde bir {ar:زَهْرَةَ, tr:zehrate, gloss:çiçek, source:20:131} olarak anılır, ve aynı ayet {ar:خَيْرٌۭ وَأَبْقَىٰ, tr:hayrun ve ebkâ, gloss:daha hayırlı ve daha kalıcı, source:20:131} diye biter. Otlağın sahnesi seçimin sahnesine bu yolla girer. Beşinci ayetteki ot ile on altıncı ayetteki tercih edilen hayat aynı nesnedir. Kalıcı olan ise ayıklanıp seçilen şeydir. Tarlanın sahnesi bu iki uç arasında bir yol açar. Kalıcı iyilik anlamına gelen kurtuluş kelimesi on dördüncü ayette, toprağı yaran çiftçinin kelimesiyle söylenir. Yabani ot kendi haline kalınca kurur ve selle gider. İşlenen toprağın ürünü ise büyür, hakkı verilir ve geriye kalan bir pay bırakır. Biri dünya tarlası, öbürü ahiret tarlasıdır.

Beşinci buluşma, yaratma fiillerinde zanaat ile bedenin birleşmesidir. İkinci ayetteki ikili hem yontulmuş oku hem de ceninin biçimlenmesini anlatır. Rahimden başlayan ayetin toprağın yağmurla titreşmesiyle bitmesi, beden ile otlağı da birbirine bağlar. Aynı aile, üçüncü ayetteki ölçmeyi pay ölçmeye de taşır, ve on altıncı ayetteki tercih bir pay seçimine döner. Değneği ateşte doğrultmanın fiili on ikinci ayetin fiilidir. Bu fiil aynı ateşin düzelten bir işi ile içine düşenin katlandığı bir işi olduğunu duyurur. Bu son bağ dilin yankısıdır, ayetin sözü değildir.

Bu buluşmalar surenin hareketini taşır. Sure tesbih emriyle ve yükseklikle açılır. Ölçen, yontan ve yol gösteren Rabbin işiyle devam eder. Yağmurun çıkardığı ve selin götürdüğü ot ile sona gelen bir ömür gösterir. Sonra sözün toplanıp unutulmamasına, sunulan öğüde ve öğüt karşısında ikiye ayrılan insanlara geçer. Biri ateşe girer ve ne ölü ne diri kalır. Öbürü arınır, Rabbinin adını anar ve namaz kılar, yani surenin başındaki emri yerine getirir. Ardından seçim gelir: yakın olan öne konmuştur, ama arkadan gelen daha hayırlı ve daha kalıcıdır. Sure, bu sözün ilk sayfalarda, ateşin başında namaz ve anma emrini alan Musa'nın ve Rabbinden kendisini puttan uzak tutmasını isteyen İbrahim'in sayfalarında yazılı olduğunu söyleyerek kapanır.

