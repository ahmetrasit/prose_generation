Focus: 92:13. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/92_13/D.r13/context.md =====
# 92:13 — focus

وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ

Anchor translation (canonical reading, reference only):

Sonrası da öncesi de elbette bizimdir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَإِنَّ | إِنّ |  | CONJ;ACC |
| 2 | لَنَا |  |  | P;PRON |
| 3 | لَلْءَاخِرَةَ | آخِر | ء خ ر | EMPH;DET;N |
| 4 | وَٱلْأُولَىٰ | أَوَّل | ء و ل | CONJ;DET;N |


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
- 92:13 ◀ focus وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- 92:14 فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- 92:15 لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- 92:16 ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- 92:17 وَسَيُجَنَّبُهَا ٱلْأَتْقَى
- 92:18 ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- 92:19 وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- 92:20 إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- 92:21 وَلَسَوْفَ يَرْضَىٰ


===== _commentary/v16/work/92_13/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ء خ ر (root_000019) — identity root of لَلْءَاخِرَةَ (w3)

- **B001** sonraki ya da öteki olan — sonraki; öteki · sonraki veya öteki olan dişil öğe · başkaları; ötekiler · insanların son kesimleri · zamanın sonu · ardından hiçbir şey gelmeyen son
  الآخر نقيض المتقدم؛ الآخر تال للأول؛ أخر جماعة أخرى (maqayis); هذا آخر وهذه أخرى؛ الآخر والآخرة نقيض المتقدم والمتقدمة؛ الآخر الغائب؛ أخر جماعة أخرى (ayn); الآخر بعد الأول؛ الآخر أحد الشيئين؛ الجمع أواخر؛ أخريات الناس أي أواخرهم؛ أخرى القوم أي من كان في آخرهم؛ أبعد الله الاخر (sihah); معنى آخر شيء غير الأول الذي قبله؛ أخر جماعة أخرى؛ أخرى القوم أي في أواخرهم (tahdhib); آخر يقابل به الأول، وآخر يقابل به الواحد؛ أخر معدول (mufradat)
- **B002** geciktirme veya gecikme — geciktirme · geciktirmek; sonraya bırakmak · gecikmek; geride kalmak · geç vakitte; sonradan · vadeli satmak · ürünü hasadın sonuna kadar kalan hurma ağacı
  تأخر أخرا؛ بعتك بيعا بأخرة أي نظرة؛ ما عرفته إلا بأخرة (maqayis); بعته الشيء بأخرة أي بتأخير؛ تأخر أخرا؛ جاء فلان أخيرا أي بأخرة (ayn); أخرته فتأخر؛ واستأخر مثل تأخر؛ بعته بأخرة وبنظرة أي بنسيئة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (sihah); المستأخر نقيض المستقدم؛ بعته سلعة بأخرة أي بتأخير؛ بأخرة وبنظرة؛ المئخار النخلة التي يبقى حملها إلى آخر الصرام (tahdhib); التأخير مقابل للتقديم؛ إنما يؤخرهم؛ أخرنا إلى أجل قريب؛ بعته بأخرة أي بتأخير أجل (mufradat)
- **B003** arka bölüm — nesnenin arka bölümü · gözün şakağa yakın arka köşesi · binek semerinin arka dayanağı · semerin arka dayanağı için seyrek ve tartışmalı söyleyiş · arka tarafından; arkasından · dişi devenin iki arka yanı
  آخرة الرحل وقادمته ومؤخر الرحل ومقدمه؛ مؤخر العين ومقدم العين (maqayis); مقدم الشيء ومؤخره؛ آخرة الرجل وقادمته؛ مقدم العين ومؤخرها؛ مؤخر الشيء ومقدمه (ayn); شق ثوبه أخرا ومن أخر أي من مؤخره؛ مؤخر العين؛ مؤخرة الرحل؛ مؤخر الشئ بالتشديد نقيض مقدمه (sihah); آخرة الرحل وقادمته ومؤخر العين ومقدمها؛ مؤخر الشيء ومقدمه؛ نظر إلي بمؤخر عينه؛ شق ثوبه أخرا ومن أخر؛ للناقة آخران وقادمان؛ مؤخرة الرحل وآخرة الرحل (tahdhib)
- **B004** ölümden sonraki yaşam ve öteki dünya — ölümden sonraki yaşam; öteki dünya · öteki dünya
  يعبر بالدار الآخرة عن النشأة الثانية؛ الدار الآخرة؛ الآخرة؛ تقدير الإضافة دار الحياة الآخرة (mufradat)

## ء و ل (root_000067) — identity root of وَٱلْأُولَىٰ (w4)

- **B001** başlangıç ve öncelik — ilk; önde gelen · ilk olan kadın ya da dişil şey · ilkler; öncekiler · topluluğun önünde bulunma · sürünün önünde giden dişi ya da erkek deve · önceki yıl · her şeyden önce
  الأول وهو مبتدأ الشيء؛ ناقة أولة وجمل أول إذا تقدما الإبل (maqayis)؛ أول في اللغة على الحقيقة ابتداء الشيء؛ جاء فلان في أولية الناس إذا جاء في أولهم (tahdhib)
- **B002** sonuca dönme ve varma — geri dönmek; sonunda bir duruma varmak · hükmü sahiplerine geri vermek · bedeni zayıflamak · sözün sonucu veya anlamının açıklanması · açıklamak; anlamına döndürmek · onunla ilgili ödülü gözetmek ve aramak
  آل يؤول أى رجع؛ تأويل الكلام وهو عاقبته وما يؤول إليه (maqayis)؛ التأويل تفسير ما يؤول إليه الشئ؛ آل أي رجع (sihah)؛ آل يؤول أي رجع وعاد؛ التأويل المرجع والمصير (tahdhib)
- **B003** aile ve bağlı çevre — kişinin ailesi, ev halkı ve yakınları · onun izleyicileri ve bağlıları · kişinin sığındığı ev halkı · kişinin kökü ve bağlı olduğu aile
  آل الرجل أهل بيته؛ لأنه إليه مآلهم وإليهم مآله (maqayis)؛ آل الرجل أهله وقرابته (jamhara)؛ آل الرجل أهله وعياله؛ وآله أيضا أتباعه (sihah)؛ إلة الرجل أهل بيته؛ إيلة الرجل فهم أصله الذين يؤول إليهم (tahdhib)
- **B004** iyi yönetip düzene koyma — iyi yönetme ve gözetme · yöneticinin halkını iyi yönetip gözetmesi · malını düzeltip iyi yönetmek · düzeltme ve iyi yönetme · Tanrı işini toparlayıp düzeltsin
  الإيالة السياسة؛ آل الرجل رعيته يؤولها إذا أحسن سياستها (maqayis)؛ الايالة السياسة؛ آل الأمير رعيته يؤولها أولا وإيالا؛ آل ما له أي أصلحه وساسه (sihah)؛ ألت الشيء جمعته وأصلحته؛ أول الله عليك أمرك أي جمعه (tahdhib)
- **B005** koyulaşıp pıhtılaşma — sütün koyulaşıp pıhtılaşması · katranın veya balın koyulaşıp katılaşması · pıhtılaşmış süt
  آل اللبن أي خثر؛ لا يخثر إلا آخر أمره؛ آل القطران إذا خثر (maqayis)؛ آل القطران أو العسل إذا أعقد بالنار (jamhara)؛ آل القطران والعسل أي خثر؛ الآيل اللبن الخاثر (sihah)
- **B006** görünür siluet ve dış uçlar — görünür siluet; uzaktan beliren görüntü · adamın görünen silueti · dağın uçları ve yanları
  آل الرجل شخصه؛ آل كل شيء؛ آل الجبل أطرافه ونواحيه (maqayis)؛ الآل السراب؛ آل كل شيء شخصه (jamhara)؛ الآل الشخص؛ الآل الذي تراه في أول النهار وآخره كأنه يرفع الشخوص وليس هو السراب (sihah)
- **B007** içinde bulunulan durum — içinde bulunulan durum
  الآلة الحالة (maqayis)؛ والآلة الحالة (jamhara)؛ والآلة الحالة يقال هو بآلة سوء (sihah)
- **B008** araç ve taşıyıcı düzen — araç · çadır direkleri ve taşıyıcı ağaçları · cenaze veya ölüyü taşıyan sedye
  آل الخيمة العمد (maqayis)؛ الآلة الأداة؛ خشبات تبنى عليها الخيمة؛ الآلة الجنازة (sihah)
- **B009** erkek yabani dağ keçisi — erkek yabani dağ keçisi
  الأيل الذكر من الوعول؛ لأنه يؤول إلى الجبل يتحصن (maqayis)؛ الايل أيضا الذكر من الاوعال (sihah)
- **B010** içecek olgunlaştırma kabı — içecek olgunlaştırma kabı
  الإيال على فعال وعاء يجمع فيه الشراب اياما حتى يجود (maqayis)
- **B011** kumda yetişen yem bitkisi — kumda yetişen bir yem bitkisi
  التأويل نبت يعتلفه الحمار؛ التأويل اسم بقلة يولع بها بقر الوحش تنبت في الرمل (tahdhib)

## ECHO و ل ي (root_001684) — for وَٱلْأُولَىٰ (w4): withheld observed target; not identity

- **B001** aralıksız yakınlık — yakınlık ve bitişiklik · sana yakın veya yanında olan şey · bir eve bitişik olan ev
  أصل صحيح يدل على قرب؛ الولي القرب؛ جلس مما يليني أي يقاربني (maqayis)؛ دار فلان ولي دار فلان؛ الدار ولية أي قريبة (jamhara)؛ الولي القرب والدنو؛ كل مما يليك أي مما يقاربك (sihah)؛ الولي القرب (tahdhib)؛ الولاء والتوالي أن يحصل شيئان فصاعدا حصولا ليس بينهما ما ليس منهما؛ يستعار ذلك للقرب (mufradat)
- **B002** kesintisiz ardışıklık — kesintisiz sıra · araya kesinti girmeden peş peşe oluş · şeyleri veya işleri peş peşe getirme · iki şeyi peş peşe getirmek · peş peşe isabet eden üç ok
  يوالي بين رميتين أو فعلين؛ أصبته بثلاثة أسهم ولاء؛ على الولاء أي الشيء بعد الشيء (ayn)؛ واليت بين الشيئين؛ افعل هذا على الولاء أي مرتبا (maqayis)؛ واليت بين الشيئين موالاة وولاء (jamhara)؛ والى بينهما ولاء أي تابع؛ على الولاء أي متتابعة؛ توالى عليه شهران (sihah)؛ الموالاة المتابعة؛ بثلاثة أسهم ولاء أي تباعا؛ توالت إلي كتب فلان (tahdhib)؛ الولاء والتوالي أن يحصل شيئان فصاعدا حصولا ليس بينهما ما ليس منهما (mufradat)
- **B003** bir işi üstlenip yönetme — yönetim ve yetki alanı · bir yeri veya işi yöneten kişi · başkasının işlerinden sorumlu kişi · bir işi üstlenmek
  الولاية مصدر الوالي (ayn)؛ كل من ولى أمر آخر فهو وليه (maqayis)؛ الولاية الإمارة (jamhara)؛ ولي الوالي البلد؛ تولى العمل أي تقلد؛ الولاية بالكسر السلطان (sihah)؛ الولاية التي بمنزلة الإمارة؛ ولي اليتيم الذي يلي أمره؛ ولي المرأة؛ وليت فلانا عمل ناحيته؛ توليت الأمر توليا (tahdhib)؛ الولاية تولي الأمر؛ حقيقته تولي الأمر (mufradat)
- **B004** yakın durup destek olma — dost, seven veya destekleyen kişi · destekçi, anlaşmalı dost veya yakın yoldaş · birini sevip destekleme veya kayırma · birini sevmek, desteklemek veya kayırmak
  المولى الحليف والولي؛ الموالاة اتخاذ المولى (ayn)؛ المولى الصاحب والحليف والناصر؛ كل هؤلاء من الولي وهو القرب (maqayis)؛ الولي خلاف العدو (jamhara)؛ الولى ضد العدو؛ المولى الناصر والحليف؛ الموالاة ضد المعاداة (sihah)؛ الولي التابع المحب؛ الولاية من النصرة والنسب؛ الولاية على الإيمان؛ المولى في الدين؛ الناصر؛ والى فلان فلانا إذا أحبه؛ فيواليه أي يحابيه (tahdhib)؛ يستعار للقرب من حيث الدين والصداقة والنصرة والاعتقاد؛ الولاية النصرة (mufradat)
- **B005** özel yakınlık ve bağlılık bağı — özgür bırakan, özgür bırakılan, soy yakını veya komşu gibi bağlı kişi · özgür bırakma ilişkisine bağlı özel hak ve mensubiyet · soy yakınları veya özgür bırakma bağıyla bağlı kişiler · nimet veya özgür bırakma bağı kuran kişi
  الموالي بنو العم؛ المولى المعتق والحليف والولي؛ الولي ولي النعم (ayn)؛ المولى المعتق والمعتق والصاحب والحليف وابن العم والناصر والجار؛ الولاء ولاء المعتق (maqayis)؛ المولى المعتق والمعتق وابن العم والناصر والجار؛ الولي الصهر؛ بينهما ولاء أي قرابة؛ الولاء ولاء المعتق (sihah)؛ المولى العصبة؛ المولى الحليف؛ المولى المعتق؛ ابن العم والعم والأخ والابن والعصبات كلهم؛ مولى النعمة؛ المعتق؛ يجب عليك أن تنصره وترثه (tahdhib)
- **B006** yüzünü veya dikkatini yöneltme — yüzünü bir şeye çevirmek · yüzünü o yöne dönmüş veya ona uyan kişi · kulağını veya dikkatini bir şeye vermek
  موليها أي مستقبلها بوجهه (sihah)؛ التولية تكون إقبالا؛ فول وجهك أي وجه وجهك نحوه؛ هو مستقبلها؛ متوليها أي متبعها وراضيها (tahdhib)؛ وليت سمعي كذا ووليت عيني كذا ووليت وجهي كذا أقبلت به عليه (mufradat)
- **B007** dönüp yüz çevirme [kalıp] — arkasını dönüp kaçarak uzaklaşmak · birinden yüz çevirmek ve ilgiyi kesmek
  ولى الرجل أي أدبر (ayn)؛ تولى عنه أي أعرض؛ ولى هاربا أي أدبر (sihah)؛ التولية تكون انصرافا؛ وليتم مدبرين؛ التولي يكون بمعنى الإعراض (tahdhib)؛ إذا عدي بعن اقتضى معنى الإعراض وترك قربه؛ التولي قد يكون بالجسم وقد يكون بترك الإصغاء والائتمار (mufradat)
- **B008** daha uygun ve hak sahibi olma — bir şeye daha uygun, daha layık veya daha hak sahibi olmak · iki daha haklı veya daha uygun kişi
  فلان أولى بكذا أي أحرى به وأجدر (maqayis)؛ فلان أولى بكذا أي أحرى به وأجدر (sihah)؛ فلان أولى بهذا الأمر أي أحق به؛ الأوليان أي الأحقان (tahdhib)
- **B009** yaklaşan kötü sonuç tehdidi — tehdit ve uyarı sözü; sana kötü şey yaklaştı
  أولى تهدد ووعيد؛ معناه قاربه ما يهلكه؛ أولى تحسير له على ما فاته (maqayis)؛ أولى لك تهدد ووعيد؛ معناه قاربه ما يهلكه؛ قارب أن يزيد (sihah)؛ أولى لك تهدد ووعيد؛ قاربك ما تكره؛ يحسره على ما فاته (tahdhib)
- **B010** önceki yağmuru izleyen yağmur — önceki yağmurdan sonra gelen yağmur · erken mevsim yağmurunu izleyen yağmur adı · toprağa izleyen yağmurun yağması · iyilik ardından gelen yağmur veya iyilik
  الولي المطر الذي يكون بعد الوسمي؛ وليت الأرض وليا فهي مولية (ayn)؛ الولي المطر يجيء بعد الوسمي سمي بذلك لأنه يلي الوسمي (maqayis)؛ الولي المطرة بعد الوسمي؛ وليت الأرض فهي مولية (jamhara)؛ الولي المطر بعد الوسمي؛ وليت الأرض وليا (sihah)؛ الولي المطر الذي يأتي بعد المطر؛ وليت الأرض وليا؛ أمطرني ولية منك (tahdhib)
- **B011** deve sırtı alt örtüsü — deve sırtında semer altında kullanılan örtü · semer altı örtüleri
  الولية الحلس والولايا جمعه (ayn)؛ الولية شبيهة بالبرذعة تطرح على ظهر البعير؛ الجمع ولايا (jamhara)؛ الولية البرذعة؛ التي تكون تحت البرذعة؛ الجمع الولايا (sihah)؛ الولية البرذعة وجمعها الولايا؛ البرذعة التي تحت الرحل (tahdhib)
- **B012** ele geçirip hedefe ulaşma [kalıp] — bir şeyi ele geçirmek veya ona üstün gelmek · hedefe varmak veya ona önce ulaşmak
  استولى فلان على شيء إذا صار في يده؛ استولى الفرس على الغاية أي بلغها (ayn)؛ استولى على الأمد أي بلغ الغاية (sihah)؛ استولى أحدهما على الغاية إذا سبق الآخر إليها؛ استيلاؤه على الأمد أن يغلب عليه بسبقه؛ استولى فلان على مالي إذا غلب عليه (tahdhib)
- **B013** birine iyi ya da kötü şey yöneltme [kalıp] — birine iyilik yapmak veya bir şeyi ona ulaştırmak · birine iyilik veya kötülük yöneltmek
  أوليته الشيء فوليه؛ أوليته معروفا (sihah)؛ أوليت فلانا شرا وأوليته خيرا؛ أوليته معروفا أسديته إليه (tahdhib)
- **B014** aldığı fiyatla devretme — satın alınan malı bilinen aynı fiyatla başkasına devretme
  التولية في البيع أن تشتري سلعة بثمن معلوم ثم توليها رجلا آخر بذلك الثمن (tahdhib)
- **B015** küçük sürü hayvanlarını ayırma — küçük sürü hayvanlarını büyüklerinden ayırmak · yavru develeri analarından ayırıp alıştırma
  للموالاة معنى ثالث؛ والوا حواشي نعمكم من الجلة أي اعزلوا صغارها عن كبارها؛ توالي ربعي السقاب؛ تواليه أن يفصل عن أمه (tahdhib)
- **B016** taze hurmanın kurumaya dönmesi — taze hurmanın solup kurumaya başlaması · taze hurmadaki solgun kuruma rengi
  يقال للرطب إذا أخذ في الهيج قد ولى وتولى؛ توليه شهبته (tahdhib)

===== _commentary/v16/out/s092/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 92:13, and ## Buluşmalar) =====
## Dağılan koşu ve iki yol

Dördüncü ayetin ilk kelimesi bir harekettir. {ar:سَعْيَكُمْ, tr:sa'yeküm, gloss:koşunuz ve çabanız, source:92:4} kelimesinin kökü {ar:السعي المشي السريع وهو دون العدو, tr:es-sa'yu'l-meşyu's-serîu ve hüve dûne'l-adv, gloss:sa'y hızlı yürüyüştür ve koşudan biraz aşağıdır, source:"س ع ي,B001"} diye tanımlanır. Kök üç adımı birden kapsar: {ar:سعى إذا مشى وسعى إذا عدا وسعى إذا قصد, tr:seâ izâ meşâ ve seâ izâ adâ ve seâ izâ kasad, gloss:yürüdü de koştu da bir hedefe yöneldi de sa'y denir, source:"س ع ي,B001"}. Ayetteki anlam da bu dala yaslanır: {ar:كل عمل من خير أو شر فهو السعي, tr:küllü amelin min hayrin ev şerrin fehüve's-sa'y, gloss:iyi ya da kötü her iş sa'ydır, source:"س ع ي,B002"}. Ayetin ikinci kelimesi {ar:لَشَتَّىٰ, tr:leşettâ, gloss:elbette dağınıktır, source:92:4} bu koşuya ne olduğunu söyler. Kök {ar:أصل يدل على تفرق وتزيل, tr:aslun yedüllü alâ teferrukin ve tezeyyül, gloss:dağılmayı ve birbirinden kopmayı gösteren kök, source:"ش ت ت,B001"} demektir. Örnek sahnesi bir suvat başıdır: {ar:يصدر الناس أشتاتا أي متفرقين, tr:yasduru'n-nâsu eştâten ey müteferrikîn, gloss:insanlar sudan ayrı ayrı bölükler hâlinde dönerler, source:"ش ت ت,B001"}. Aradaki fark da {ar:شتان ما بينهما, tr:şettâne mâ beynehümâ, gloss:ikisinin arası ne kadar da açık, source:"ش ت ت,B003"} ile, yani {ar:ارتفاع الالتئام بينهما, tr:irtifâu'l-iltiâmi beynehümâ, gloss:aralarındaki bitişikliğin kalkması, source:"ش ت ت,B003"} ile anlatılır. Düz anlam "çabalarınız farklıdır" der. Görüntü ise ayrılış anını gösterir: herkes aynı sudan kalkar, her biri bir hedefe doğru hızlı adımlarla yürür ve bölükler arasındaki dikiş açılır.

Beşinci ayetten onuncuya kadar iki yol çizilir. Yedinci ayetin kökü yolun düzlenmesini anlatır: {ar:تيسر واستيسر أي تسهل وتهيأ, tr:teyessera ve'steysera ey tesehhele ve teheyyee, gloss:kolaylaştı yani düzlendi ve hazır hâle geldi, source:"ي س ر,B001"}. Onuncu ayetin kökü ise kıvrılan bir yoldur: {ar:العسرى الأمور التي تعسر ولا تتيسر, tr:el-usrâ el-umûru'lletî ta'suru ve lâ teteyesser, gloss:usrâ zorlaşan ve bir türlü kolaylaşmayan işlerdir, source:"ع س ر,B001"}. Aynı kökte {ar:العسر الخلاف والالتواء, tr:el-usru'l-hılâfu ve'l-iltivâ', gloss:usr ters gitmek ve kıvrılmaktır, source:"ع س ر,B004"} de denir. İki yolun fiili ise aynıdır: {ar:فَسَنُيَسِّرُهُۥ لِلْيُسْرَىٰ, tr:fe-senüyessiruhû li'l-yüsrâ, gloss:onu en kolaya kolaylaştıracağız, source:92:7} ve {ar:فَسَنُيَسِّرُهُۥ لِلْعُسْرَىٰ, tr:fe-senüyessiruhû li'l-usrâ, gloss:onu en zora kolaylaştıracağız, source:92:10}. Görüntü burada düz anlamın kaçırdığını gösterir. Kolaylaştırmak yolu düzleyip hazırlamaktır ve Allah her koşucunun yolunu onun koştuğu yönde düzler. Zora giden yol da yürüyene kolay gelir. Kıvrımlı yokuş aşağı bir yoldur, insan onda farkına varmadan hızlanır. On ikinci ayet bu iki yolun üstüne bir söz koyar: {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hüdâ, gloss:yol göstermek elbette bize düşer, source:92:12}. Kelimenin ailesinde yön anlamı vardır: {ar:هدية أمره أي جهة أمره, tr:hidyetü emrihî ey cihetü emrih, gloss:işinin hidyesi işinin yönüdür, source:"ه د ي,B002"}. Bir deyim yönü kıble, arka ve cephe ile yan yana sayar: {ar:ليس لهذا الأمر هدية ولا قبلة ولا دبرة ولا وجهة, tr:leyse li-hâze'l-emri hidyetün ve lâ kıbletün ve lâ debratün ve lâ vichetün, gloss:bu işin ne yönü ne kıblesi ne arkası ne cephesi var, source:"ه د ي,B002"}.

Kur'an iki yolu başka yerlerde de gösterir. İnsan için {ar:وَهَدَيْنَٰهُ ٱلنَّجْدَيْنِ, tr:ve hedeynâhü'n-necdeyn, gloss:ona iki yüksek yolu gösterdik, source:90:10} denir. Bir başka ayette {ar:إِنَّا هَدَيْنَٰهُ ٱلسَّبِيلَ إِمَّا شَاكِرًۭا وَإِمَّا كَفُورًا, tr:innâ hedeynâhü's-sebîle immâ şâkiran ve immâ kefûrâ, gloss:ona yolu gösterdik; ister şükreden olsun ister nankör, source:76:3} denir. On ikinci ayetin "üzerimize" bağı başka bir ayette de görünür: {ar:وَعَلَى ٱللَّهِ قَصْدُ ٱلسَّبِيلِ وَمِنْهَا جَآئِرٌۭ, tr:ve ala'llâhi kasdu's-sebîli ve minhâ câir, gloss:doğru yolu göstermek Allah'a düşer; yolların bazısı sapar, source:16:9}. Surenin "fe-emmâ ... ve emmâ" çerçevesi bir başka surede aynen kurulur: {ar:فَأَمَّا مَن طَغَىٰ, tr:fe-emmâ men tağâ, gloss:azana gelince, source:79:37} ve {ar:وَأَمَّا مَنْ خَافَ مَقَامَ رَبِّهِۦ, tr:ve emmâ men hâfe makâme rabbih, gloss:Rabbinin makamından korkana gelince, source:79:40}. Suvattan dağılan kalabalığın Kur'an'daki karşılığı Diriliş günüdür: {ar:يَوْمَئِذٍۢ يَصْدُرُ ٱلنَّاسُ أَشْتَاتًۭا لِّيُرَوْا۟ أَعْمَٰلَهُمْ, tr:yevmeizin yasduru'n-nâsu eştâten li-yurav a'mâlehüm, gloss:o gün insanlar yaptıkları kendilerine gösterilsin diye bölük bölük dönerler, source:99:6}. Fiil suvattan dönüşün fiilidir. Aynı gün için {ar:يَوْمَئِذٍۢ يَتَفَرَّقُونَ, tr:yevmeizin yeteferrakûn, gloss:o gün ayrılırlar, source:30:14} de denir. Dağınıklık yalnız yollarda değil gönüllerde de olabilir: {ar:تَحْسَبُهُمْ جَمِيعًۭا وَقُلُوبُهُمْ شَتَّىٰ, tr:tahsebühüm cemîan ve kulûbühüm şettâ, gloss:onları bir arada sanırsın ama kalpleri dağınıktır, source:59:14}. Koşunun sonu da bellidir: {ar:وَأَن لَّيْسَ لِلْإِنسَٰنِ إِلَّا مَا سَعَىٰ, tr:ve en leyse li'l-insâni illâ mâ seâ, gloss:insan için koştuğundan başkası yoktur, source:53:39}; {ar:وَأَنَّ سَعْيَهُۥ سَوْفَ يُرَىٰ, tr:ve enne sa'yehû sevfe yurâ, gloss:koşusu görülecektir, source:53:40}; {ar:ثُمَّ يُجْزَىٰهُ ٱلْجَزَآءَ ٱلْأَوْفَىٰ, tr:sümme yuczâhü'l-cezâe'l-evfâ, gloss:sonra karşılığı eksiksiz verilecektir, source:53:41}. Koşu görülür ve karşılık bulur. Surede de dördüncü ayetin koşusu on dokuzuncu ayetin karşılık kelimesine ve yirmi birincinin hoşnutluğuna varır. Kolay yol Peygambere de vaat edilir: {ar:وَنُيَسِّرُكَ لِلْيُسْرَىٰ, tr:ve nüyessiruke li'l-yüsrâ, gloss:seni en kolaya kolaylaştıracağız, source:87:8}. Zor yol ise bir günün adıdır: {ar:فَذَٰلِكَ يَوْمَئِذٍۢ يَوْمٌ عَسِيرٌ, tr:fe-zâlike yevmeizin yevmün asîr, gloss:işte o gün zor bir gündür, source:74:9}; {ar:عَلَى ٱلْكَٰفِرِينَ غَيْرُ يَسِيرٍۢ, tr:ale'l-kâfirîne ğayru yesîr, gloss:inkârcılar için hiç kolay değildir, source:74:10}.

Koşu bir yarış olarak da duyulur. Kökün bir dalında {ar:السعي عدو ليس بشديد, tr:es-sa'yu advün leyse bi-şedîd, gloss:sa'y şiddetli olmayan koşudur, source:"س ع ي,B001"} denir, bir başka dalında da geçmek anlamı vardır: {ar:ساعانى فلان فسعيته أسعيه إذا غلبته فيه, tr:sâanî fülânün fe-seaytühû es'âhu izâ ğalebtühû fîh, gloss:biri benimle koşu yarışına girdi ve onu geçtim, source:"س ع ي,B008"}. On üçüncü ayetin iki kelimesi yarışın iki ucudur: {ar:الأول وهو مبتدأ الشيء, tr:el-evvelü ve hüve mübtedeü'ş-şey', gloss:evvel bir şeyin başlangıcıdır, source:"ء و ل,B001"} ve {ar:الآخر نقيض المتقدم, tr:el-âhiru nakîdu'l-mütekaddim, gloss:âhir öndekinin zıddıdır, source:"ء خ ر,B001"}. On altıncı ayetin fiili ayette yüz çevirmektir. Kökün bir yarış deyimi ise hedefe varmaktır: {ar:استولى الفرس على الغاية أي بلغها, tr:isteveli'l-ferasu ale'l-ğâye ey beleğahâ, gloss:at hedefe vardı, source:"و ل ي,B012"}. Aynı kökten biri hedefe varırken öteki yarıştan sırtını dönüp çıkar. On sekizinci ayetin fiili {ar:يُؤْتِى, tr:yü'tî, gloss:verir, source:92:18} ise ailesinde koşunun bittiği yeri adlandırır: {ar:الميتاء والميداء آخر الغاية حيث ينتهي إليه جري الخيل, tr:el-mîtâu ve'l-mîdâu âhiru'l-ğâyeti haysü yentehî ileyhi cerye'l-hayl, gloss:mîtâ atların koşusunun bittiği son hedeftir, source:"ء ت ي,B010"}. Malını veren, kelimenin ailesinde, varış çizgisine ulaşan atın yanında durur. On birinci ayetin fiili de ailesinde atın hızlanmasıdır: {ar:ردى الفرس أسرع, tr:radeye'l-ferasu esra', gloss:at hızlandı, source:"ر د ي,B002"}. Kur'an yarışı açıkça buyurur: {ar:وَلِكُلٍّۢ وِجْهَةٌ هُوَ مُوَلِّيهَا ۖ فَٱسْتَبِقُوا۟ ٱلْخَيْرَٰتِ, tr:ve li-küllin vichetün hüve müvellîhâ festebiku'l-hayrât, gloss:herkesin yöneldiği bir cephe vardır; hayırlarda yarışın, source:2:148}. Bu ayette yön, dönmek ve yarış aynı cümlededir. Ayrıca {ar:سَابِقُوٓا۟ إِلَىٰ مَغْفِرَةٍۢ مِّن رَّبِّكُمْ, tr:sâbikû ilâ mağfiretin min rabbiküm, gloss:Rabbinizden bir bağışlanmaya koşuşun, source:57:21} ve {ar:وَٱلسَّٰبِقُونَ ٱلسَّٰبِقُونَ, tr:ve's-sâbikûne's-sâbikûn, gloss:öne geçenler, öne geçenlerdir, source:56:10} denir. Koşunun hoşnutlukla bittiği yüzler de anılır: {ar:لِّسَعْيِهَا رَاضِيَةٌۭ, tr:li-sa'yihâ râdıye, gloss:koşularından hoşnutturlar, source:88:9}. Bu ayet surenin ilk eylem kelimesini son kelimesiyle tek cümlede birleştirir.

Kaynaklar: 92:4 سَعْيَكُمْ س ع ي B001; 92:4 سَعْيَكُمْ س ع ي B002; 92:4 سَعْيَكُمْ س ع ي B008; 92:4 لَشَتَّىٰ ش ت ت B001; 92:4 لَشَتَّىٰ ش ت ت B003; 92:7 لِلْيُسْرَىٰ ي س ر B001; 92:10 لِلْعُسْرَىٰ ع س ر B001; 92:10 لِلْعُسْرَىٰ ع س ر B004; 92:11 تَرَدَّىٰٓ ر د ي B002; 92:12 لَلْهُدَىٰ ه د ي B002; 92:13 لَلْءَاخِرَةَ ء خ ر B001; 92:13 وَٱلْأُولَىٰ ء و ل B001; 92:16 وَتَوَلَّىٰ و ل ي B012; 92:18 يُؤْتِى ء ت ي B010

## Yolu gösteren ateş, kervanın başı ve sonu

Ateş ile ışık aynı yerden adlandırılır: {ar:النور والنار سميا بذلك من طريقة الإضاءة, tr:en-nûru ve'n-nâru sümmiyâ bi-zâlike min tarîkati'l-idâe, gloss:nur ve nar bu adı aydınlatma yönünden almıştır, source:"ن و ر,B001"}. Ateşin yol göstermede eski bir işi vardır: {ar:كانوا ينورون في الجاهلية ليهتدى ويقتدى بها, tr:kânû yünevvirûne fi'l-câhiliyyeti li-yühtedâ ve yuktedâ bihâ, gloss:cahiliyede yol bulunsun ve izlensin diye ateş yakarlardı, source:"ن و ر,B005"}. Bu işin bir de işareti vardır: {ar:المنار: علم الطريق؛ ضرب المنار على طريقه ليهتدى بها, tr:el-menâr alemü't-tarîk; darabe'l-menâra alâ tarîkıhî li-yühtedâ bihâ, gloss:menâr yolun işaretidir; yolu bulunsun diye yolunun üstüne işaret dikti, source:"ن و ر,B005"}. Yolcu bu ateşi uzaktan görür ve ona yönelir: {ar:تنورت النار من بعيد: تبصرتها, tr:tenevvertü'n-nâra min baîd: tebassartühâ, gloss:ateşi uzaktan gözledim, source:"ن و ر,B003"}; {ar:تنورت نارا قصدت إليها, tr:tenevvertü nâran kasadtü ileyhâ, gloss:bir ateşe doğru yöneldim, source:"ن و ر,B003"}. Hidayet de tam bu işi adlandırır: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytühü't-tarîka ve'l-beyte hidâyeten ey arraftüh, gloss:ona yolu ve evi gösterdim yani tanıttım, source:"ه د ي,B001"}. Başka bir tanım {ar:الهداية دلالة بلطف؛ تعريف الطرق, tr:el-hidâyetü delâletün bi-lutf; ta'rîfü't-turuk, gloss:hidayet incelikle yol göstermektir; yolları tanıtmaktır, source:"ه د ي,B001"} der. Sahne şöyle işler: Karanlıkta yüksek bir yere ateş yakılır, yolcu onu uzaktan görür, yönünü ona göre düzeltir ve ateş yolun nerede olduğunu bildirmiş olur. Gündüzün yaygın ışığında yol zaten görünür. Gece ise yolu ancak böyle bir ateş gösterir.

Surede on ikinci ayet {ar:إِنَّ عَلَيْنَا لَلْهُدَىٰ, tr:inne aleynâ le'l-hüdâ, gloss:yol göstermek elbette bize düşer, source:92:12} der. İki ayet sonra bir ateş yakılır: {ar:فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ, tr:fe-enzertüküm nâran telezzâ, gloss:sizi alev alev yanan bir ateşle uyardım, source:92:14}. Ayetteki anlam, kaçınılacak alevdir. Kelimenin ailesi ise aynı ateşin bir işaret ateşi olarak da duyulmasını sağlar: Uyarı ateşi yolun nerede bittiğini bildirerek yol gösterir. Yirminci ayetin yüzü de bu sahneye girer: {ar:الوجهة كل موضع استقبلته, tr:el-vichetü küllü mevdıın istakbeltehû, gloss:vicheti yöneldiğin her yerdir, source:"و ج ه,B002"}. Aynı dalda yolun ayakla açılması da anlatılır: {ar:وجهوا للناس الطريق إذا وطئوه وسلكوه, tr:vecchehû li'n-nâsi't-tarîka izâ vetıûhü ve selekûh, gloss:yolu çiğneyip yürüyerek insanlara açtılar, source:"و ج ه,B002"}. Rabbinin yüzünü arayan, o yüze dönük yürüyerek yolu belirgin kılar.

Kur'an bu sahneyi Musa ile kurar. Musa ailesiyle yolculuk ederken bir ateş görür ve onlara şöyle der: {ar:إِنِّىٓ ءَانَسْتُ نَارًۭا لَّعَلِّىٓ ءَاتِيكُم مِّنْهَا بِقَبَسٍ أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:innî ânestü nâran leallî âtîküm minhâ bi-kabesin ev ecidü ale'n-nâri hüdâ, gloss:bir ateş gördüm; belki size ondan bir kor getiririm ya da ateşin başında bir yol gösterici bulurum, source:20:10}. Ateş, yol bulma ve getirip vermek aynı cümlede durur. Başka bir anlatımda Musa süreyi doldurmuş, ailesiyle yola çıkmıştır ve ateşi {ar:ءَانَسَ مِن جَانِبِ ٱلطُّورِ نَارًۭا, tr:ânese min cânibi't-tûri nârâ, gloss:Tur'un yanından bir ateş gördü, source:28:29} diye görür. "Yan" kelimesi on yedinci ayetin köküdür. Üçüncü anlatımda ateşin bir başka işi söylenir: {ar:لَّعَلَّكُمْ تَصْطَلُونَ, tr:leallekum tastalûn, gloss:belki ısınırsınız, source:27:7}. Isınmak fiili on beşinci ayetteki {ar:يَصْلَىٰهَآ, tr:yaslâhâ, gloss:ona girip yanar, source:92:15} fiiliyle aynı köktendir. Musa'nın ateşi yanına yaklaşılan, ısıtan ve yol gösteren ateştir. Surenin ateşi ise içine girilen ateştir. Aynı kök iki mesafeyi ayırır. Gece yolculuğunda Kur'an başka işaretler de koyar: {ar:لِتَهْتَدُوا۟ بِهَا فِى ظُلُمَٰتِ ٱلْبَرِّ وَٱلْبَحْرِ, tr:li-tehtedû bihâ fî zulümâti'l-berri ve'l-bahr, gloss:karanın ve denizin karanlıklarında onlarla yol bulasınız diye, source:6:97}; {ar:وَعَلَٰمَٰتٍۢ ۚ وَبِٱلنَّجْمِ هُمْ يَهْتَدُونَ, tr:ve alâmâtin ve bi'n-necmi hüm yehtedûn, gloss:işaretler de koydu; onlar yıldızla yol bulurlar, source:16:16}.

Hidayetin ailesi yolu gösteren ateşin yanına bir yürüyüş düzeni de koyar. Öndeki şey hâdîdir: {ar:الهادي من كل شيء أوله, tr:el-hâdî min külli şey'in evveluh, gloss:her şeyin hâdîsi onun önüdür, source:"ه د ي,B003"}. Aynı tanım {ar:هوادي الخيل أعناقها أو أول رعيل, tr:hevâdi'l-hayli a'nâkuhâ ev evvelü raîl, gloss:atların hâdîleri boyunları ya da ilk bölüktür, source:"ه د ي,B003"} ve {ar:الدليل يسمى هاديا لتقدمه, tr:ed-delîlü yüsemmâ hâdiyen li-tekaddumih, gloss:kılavuza önde yürüdüğü için hâdî denir, source:"ه د ي,B003"} diye sürer. Sürünün önündeki deve için {ar:ناقة أولة وجمل أول إذا تقدما الإبل, tr:nâkatün evvelatün ve cemelün evvelü izâ tekaddeme'l-ibil, gloss:develerin önüne geçen dişi ve erkek deveye evvel denir, source:"ء و ل,B001"} denir. Arkada kalanlar için {ar:أخرى القوم أي من كان في آخرهم, tr:uhra'l-kavmi ey men kâne fî âhirihim, gloss:topluluğun sonu, en arkada olanlardır, source:"ء خ ر,B001"} denir. Semerin de bir ön ve bir arka direği vardır: {ar:آخرة الرحل وقادمته ومؤخر الرحل ومقدمه, tr:âhiratü'r-rahli ve kâdimetühû ve muahhiru'r-rahli ve mukaddimuh, gloss:semerin arka ve ön kaşı, source:"ء خ ر,B003"}. Gece ve gündüz yürüyüşün iki ayrı düzenidir: {ar:لست بليلي ولكني نهر أي أسير بالنهار ولا أطيق سرى الليل, tr:lestü bi-leyliyyin ve lâkinnî neharun ey esîru bi'n-nehâri ve lâ utîku sura'l-leyl, gloss:gececi değilim, gündüzcüyüm; gündüz yürürüm, gece yürüyüşüne dayanamam, source:"ل ي ل,B002"}; {ar:رجل نهر صاحب نهار, tr:racülün neharun sâhibu nehâr, gloss:gündüz adamı, source:"ن ه ر,B002"}. On ikinci ve on üçüncü ayet bu düzende birlikte işitilir: {ar:وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ, tr:ve inne lenâ le'l-âhirete ve'l-ûlâ, gloss:sonuncu da ilki de elbette bizimdir, source:92:13}. Kervanın önündeki kılavuzu Allah üstlenir, baştaki deveden en arkadaki yolcuya kadar bütün dizi de O'nundur. Kur'an böyle bir gece yürüyüşünü Lut'a gönderilen elçilerin ağzından anlatır: {ar:فَأَسْرِ بِأَهْلِكَ بِقِطْعٍۢ مِّنَ ٱلَّيْلِ وَٱتَّبِعْ أَدْبَٰرَهُمْ وَلَا يَلْتَفِتْ مِنكُمْ أَحَدٌۭ, tr:fe-esri bi-ehlike bi-kıt'ın mine'l-leyli ve't-tebi' edbârahüm ve lâ yeltefit minküm ehad, gloss:gecenin bir bölümünde ailenle yola çık; onların arkasından yürü; hiçbiriniz arkasına dönüp bakmasın, source:15:65}. Lut dizinin en arkasında yürür ve kimse dönüp bakmaz. Surenin yalanlayanı ise bir sonraki bölümde görüleceği gibi, tam da arkasına bakan hayvanın fiilini taşır.

Kaynaklar: 92:1 ٱلَّيْلِ ل ي ل B002; 92:2 ٱلنَّهَارِ ن ه ر B002; 92:12 لَلْهُدَىٰ ه د ي B001; 92:12 لَلْهُدَىٰ ه د ي B003; 92:13 لَلْءَاخِرَةَ ء خ ر B001; 92:13 لَلْءَاخِرَةَ ء خ ر B003; 92:13 وَٱلْأُولَىٰ ء و ل B001; 92:14 نَارًۭا ن و ر B001; 92:14 نَارًۭا ن و ر B003; 92:14 نَارًۭا ن و ر B005; 92:20 وَجْهِ و ج ه B002

## Kur'a okları, pay ve mülk

Kolaylık kelimesinin kökü bir kumarın da adıdır. Kumarı oynayanlara {ar:الأيسار: القوم يجتمعون على الميسر, tr:el-eysâr: el-kavmü yectemiûne ale'l-meysir, gloss:eysâr meysir için toplanan topluluktur, source:"ي س ر,B007"} denir. Kumarın işleyişi de bu köktendir: {ar:يسر القوم الجزور أي اجتزروها واقتسموا أعضاءها, tr:yesera'l-kavmü'l-cezûra ey ictezerûhâ ve'ktesemû a'dâehâ, gloss:topluluk deveyi kesti ve parçalarını paylaştı, source:"ي س ر,B007"}. Okların durduğu kılıf da Rab kelimesinin kökündendir: {ar:الربابة شبيهة بالكنانة تجمع فيها سهام الميسر, tr:er-rabâbetü şebîhetün bi'l-kinâneti tücmeu fîhâ sihâmü'l-meysir, gloss:rabâbe meysir oklarının toplandığı sadağa benzer bir kılıftır, source:"ر ب ب,B010"}. En değerli ok da yüceliğin kökündendir: {ar:المعلى السابع من القداح, tr:el-muallâ es-sâbiu mine'l-kıdâh, gloss:muallâ okların yedincisidir, source:"ع ل و,B009"}. Üçüncü ayetin yaratma kökü de pay anlamını taşır: {ar:الخلاق النصيب لأنه قد قدر لكل أحد نصيبه, tr:el-halâku'n-nasîbü li-ennehû kad kuddira li-külli ehadin nasîbüh, gloss:halâk paydır çünkü herkese payı ölçülmüştür, source:"خ ل ق,B006"}. Aynı kökte deri kesiminin ölçüsü de vardır: {ar:خلقت الأديم إذا قدرته قبل القطع, tr:halaktü'l-edîme izâ kaddertühû kable'l-kat', gloss:deriyi kesmeden önce ölçtüm, source:"خ ل ق,B001"}. Pay deyimi ayrıca on üçüncü ayetin kelimesiyle birleşir: {ar:الخلاق: النصيب؛ لا خلاق له في الآخرة, tr:el-halâk: en-nasîb; lâ halâka lehû fi'l-âhira, gloss:halâk paydır; onun âhirette payı yoktur, source:"خ ل ق,B006"}. Sahne bir paylaşma sahnesidir: topluluk bir deveyi keser, oklar kılıftan çekilir, yedinci ok en büyük payı alır ve herkes şansına düşeni götürür. Surenin kolaylık kelimeleri, ailelerinde, bu oyunun oyuncularının ve payının yanında durur. Sure ise kolaylığı bir okun düşüşüne bırakmaz, verip vermemeye bağlar. Yaratma kelimesi ölçülerek kesilmiş bir payı, son ayetlerdeki Rab ve en yüce kelimeleri de kılıfı ve en değerli oku hatırlatır. Ama onları kurayı yöneten değil, payı kendisi ölçen bir sahibe bağlar.

Kur'an bu oyunu harcamanın yanında anar: {ar:يَسْـَٔلُونَكَ عَنِ ٱلْخَمْرِ وَٱلْمَيْسِرِ, tr:yes'elûneke ani'l-hamri ve'l-meysir, gloss:sana içkiyi ve kumarı soruyorlar, source:2:219}. Aynı ayette ikinci bir soru gelir: {ar:وَيَسْـَٔلُونَكَ مَاذَا يُنفِقُونَ قُلِ ٱلْعَفْوَ, tr:ve yes'elûneke mâzâ yünfikûn kuli'l-afv, gloss:ne harcayacaklarını soruyorlar; de ki ihtiyaçtan artanı, source:2:219}. Kumarın payı ile harcamanın payı bir ayette karşılaşır. Kumarla ilgili bir başka buyrukta da {ar:فَٱجْتَنِبُوهُ, tr:fe'ctenibûh, gloss:ondan uzak durun, source:5:90} denir. Bu fiil on yedinci ayetin kökündendir. Fal oklarıyla pay aramak da haram kılınanlar arasındadır: {ar:وَأَن تَسْتَقْسِمُوا۟ بِٱلْأَزْلَٰمِ, tr:ve en testaksimû bi'l-ezlâm, gloss:fal oklarıyla kısmet aramanız, source:5:3}. Aynı ayet düşerek ölen hayvanı da sayar. Âhiretteki payı olmayan da anılır. Yalnızca dünya isteyen için {ar:وَمَا لَهُۥ فِى ٱلْءَاخِرَةِ مِنْ خَلَٰقٍۢ, tr:ve mâ lehû fi'l-âhirati min halâk, gloss:onun âhirette hiçbir payı yoktur, source:2:200} denir. Ahdini az bir bedele satanlar için {ar:أُو۟لَٰٓئِكَ لَا خَلَٰقَ لَهُمْ فِى ٱلْءَاخِرَةِ, tr:ülâike lâ halâka lehüm fi'l-âhira, gloss:onların âhirette payı yoktur, source:3:77} denir ve aynı ayette Allah'ın {ar:وَلَا يُزَكِّيهِمْ, tr:ve lâ yüzekkîhim, gloss:onları arındırmaz, source:3:77} olduğu da söylenir.

Payın kime ait olduğu sorusu mülkün sahnesine geçer. On birinci ve on sekizinci ayetler {ar:مَالُهُۥٓ, tr:mâlüh, gloss:onun malı, source:92:11} diye adamın malından söz eder. Kök edinmeyi anlatır: {ar:تمول الرجل اتخذ مالا, tr:temevvele'r-racülü'tteheze mâlen, gloss:adam mal edindi, source:"م و ل,B001"}; {ar:رجل مال أي ذو مال, tr:racülün mâlün ey zû mâl, gloss:mal adamı yani mal sahibi, source:"م و ل,B001"}. On ikinci ve on üçüncü ayetler ise "üzerimize" ve "bizimdir" der. Rabbin kelimesi de mülkü adlandırır: {ar:ورب كل شيء مالكه, tr:ve rabbü külli şey'in mâlikuh, gloss:her şeyin rabbi onun sahibidir, source:"ر ب ب,B001"}; {ar:فالرب المالك والخالق والصاحب, tr:fe'r-rabbü'l-mâlikü ve'l-hâlıku ve's-sâhib, gloss:rab sahip, yaratıcı ve dosttur, source:"ر ب ب,B001"}. Bu tanım yirminci ayetin Rabbini üçüncü ayetin yaratanına bağlar. On dokuzuncu ayetin "yanında" kelimesi de bir sahipliği gösterir: {ar:عند فحضور الشيء ودنوه, tr:inde fe-hudûru'ş-şey'i ve dünüvvüh, gloss:inde bir şeyin hazır ve yakın olmasıdır, source:"ع ن د,B004"}. Veren adamın yanında kimsenin bir alacağı yoktur. Adamın malı onundur ama son ve ilk Allah'ındır. Kur'an aynı sözü insanın temennisine karşı söyler: {ar:أَمْ لِلْإِنسَٰنِ مَا تَمَنَّىٰ, tr:em li'l-insâni mâ temennâ, gloss:yoksa insan her umduğuna mı sahip, source:53:24}; {ar:فَلِلَّهِ ٱلْءَاخِرَةُ وَٱلْأُولَىٰ, tr:fe-li'llâhi'l-âhiratü ve'l-ûlâ, gloss:son da ilk de Allah'ındır, source:53:25}. Bir başka ayette {ar:لَهُ ٱلْحَمْدُ فِى ٱلْأُولَىٰ وَٱلْءَاخِرَةِ, tr:lehü'l-hamdü fi'l-ûlâ ve'l-âhira, gloss:ilkte de sonda da övgü O'nundur, source:28:70} denir. Bir sonraki surede Peygambere {ar:وَلَلْءَاخِرَةُ خَيْرٌۭ لَّكَ مِنَ ٱلْأُولَىٰ, tr:ve le'l-âhiratü hayrun leke mine'l-ûlâ, gloss:son senin için ilkinden daha hayırlıdır, source:93:4} denir. Malın asıl sahibi de söylenir: {ar:وَأَنفِقُوا۟ مِمَّا جَعَلَكُم مُّسْتَخْلَفِينَ فِيهِ, tr:ve enfikû mimmâ cealeküm müstahlefîne fîh, gloss:sizi üzerinde halef kıldığı şeylerden harcayın, source:57:7}. Cimrilik ayetinin sonunda da {ar:وَلِلَّهِ مِيرَٰثُ ٱلسَّمَٰوَٰتِ وَٱلْأَرْضِ, tr:ve li'llâhi mîrâsü's-semâvâti ve'l-ard, gloss:göklerin ve yerin mirası Allah'ındır, source:3:180} denir. Tutulan malın son sahibi tutan değildir. Yaratmak, vermek ve yol göstermek de tek cümlede O'na bağlanır: {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî halaka fe-sevvâ, gloss:yaratıp düzenleyen, source:87:2}; {ar:وَٱلَّذِى قَدَّرَ فَهَدَىٰ, tr:vellezî kaddera fe-hedâ, gloss:ölçüp yol gösteren, source:87:3}. Ölçmek fiili payın ölçülmesiyle aynı işi görür.

Kaynaklar: 92:3 خَلَقَ خ ل ق B001; 92:3 خَلَقَ خ ل ق B006; 92:7 لِلْيُسْرَىٰ ي س ر B007; 92:11 مَالُهُۥٓ م و ل B001; 92:13 لَلْءَاخِرَةَ ء خ ر B001; 92:13 وَٱلْأُولَىٰ ء و ل B001; 92:19 عِندَهُۥ ع ن د B004; 92:20 رَبِّهِ ر ب ب B001; 92:20 رَبِّهِ ر ب ب B010; 92:20 ٱلْأَعْلَىٰ ع ل و B009

## Doğrulanan vaat: el-Hüsnâ

Altıncı ve dokuzuncu ayetler aynı nesneye zıt iki fiil yöneltir: {ar:وَصَدَّقَ بِٱلْحُسْنَىٰ, tr:ve saddaka bi'l-hüsnâ, gloss:en güzeli doğruladı, source:92:6} ve {ar:وَكَذَّبَ بِٱلْحُسْنَىٰ, tr:ve kezzebe bi'l-hüsnâ, gloss:en güzeli yalanladı, source:92:9}. En güzel, sonun en iyisidir: {ar:الحسنى هي الجنة وضد الحسنى السوءى, tr:el-hüsnâ hiye'l-cennetü ve diddü'l-hüsne's-sû'â, gloss:hüsnâ cennettir; zıddı sû'âdır, source:"ح س ن,B003"}. Bu anlam bir ayete dayanır: {ar:للذين أحسنوا الحسنى وزيادة أي الجنة وهي ضد السوءى, tr:li'llezîne ahsenu'l-hüsnâ ve ziyâdetün ey el-cennetü ve hiye diddü's-sû'â, gloss:güzel davrananlara en güzeli ve fazlası vardır; yani cennet; o kötünün zıddıdır, source:"ح س ن,B003"}. Doğrulama fiili, beklenen bir şeyin gerçekleşmesini de anlatır: {ar:صدق ظني, tr:sadaka zannî, gloss:tahminim doğru çıktı, source:"ص د ق,B004"}. Bir deyimde kökün bu işi açıkça görülür: {ar:لقد صدق عليهم إبليس ظنه أي حقق ظنه, tr:le-kad saddaka aleyhim iblîsü zannehû ey hakkaka zanneh, gloss:İblis onlar hakkındaki zannını doğru çıkardı yani gerçekleştirdi, source:"ص د ق,B004"}. Yalanlama ise birini yalana bağlamaktır: {ar:كذبت فلانا نسبته إلى الكذب وأكذبته وجدته كاذبا, tr:kezzebtü fülânen nesebtühû ile'l-kezib ve ekzebtühû vecedtühû kâzibâ, gloss:birini yalanladım yani onu yalana bağladım; ekzebtühû onu yalancı buldum demektir, source:"ك ذ ب,B002"}. Sahne bir vaatle başlar. Bir son önceden bildirilir. Biri bugün elindekini o son için verir ve böylece vaadi kendi eylemiyle doğru çıkarır. Öteki vaadi verene yalancı der ve elindekini tutar. Altıncı ayetin doğrulaması bir düşünce değil, beşinci ayetteki vermenin kendisidir. Dokuzuncu ayetin yalanlaması da sekizinci ayetteki tutmanın kendisidir.

Sonun nerede olduğunu on üçüncü ayet söyler: {ar:يعبر بالدار الآخرة عن النشأة الثانية, tr:yuabbaru bi'd-dâri'l-âhirati ani'n-neş'eti's-sâniye, gloss:son yurt ikinci yaratılışı anlatır, source:"ء خ ر,B004"}. On dokuzuncu ayetin karşılık fiili de iki yöne açıktır: {ar:الجزاء يكون ثوابا ويكون عقابا, tr:el-cezâu yekûnü sevâben ve yekûnü ıkâbâ, gloss:cezâ ödül de olur ceza da, source:"ج ز ي,B001"}. Veren adam insanlardan bir karşılık beklemez. Karşılığın kendisi ise ikinci yaratılışta, her iki yöne gidecek şekilde gelir. Yirmi birinci ayet sahneyi kapatır: {ar:وَلَسَوْفَ يَرْضَىٰ, tr:ve le-sevfe yerdâ, gloss:o elbette hoşnut olacaktır, source:92:21}. Hoşnutluk iki yönlüdür: {ar:رضا العبد عن الله ورضا الله عن العبد, tr:ridâ'l-abdi ani'llâhi ve ridâ'llâhi ani'l-abd, gloss:kulun Allah'tan hoşnutluğu ve Allah'ın kuldan hoşnutluğu, source:"ر ض و,B001"}. Bolluğu da vardır: {ar:الرضوان الرضا الكثير, tr:er-ridvânü'r-ridâ'l-kesîr, gloss:rıdvan çok hoşnutluktur, source:"ر ض و,B002"}. Doğrulanan vaat, doğrulayanın hoşnutluğunda tamamlanır.

Kur'an en güzeli ve onun karşıtını iki yüz olarak gösterir. Allah'ın esenlik yurduna çağırdığı söylendikten sonra şöyle denir: {ar:وَلَا يَرْهَقُ وُجُوهَهُمْ قَتَرٌۭ وَلَا ذِلَّةٌ, tr:ve lâ yerhaku vucûhehüm katerun ve lâ zille, gloss:yüzlerini ne toz ne aşağılanma kaplar, source:10:26}. Ötekilerin yüzleri ise gece parçalarıyla örtülür {source:10:27}. En güzel kendini yeterli görenin ağzında da geçer. Bir sıkıntıdan sonra rahmet tadan adam şöyle der: {ar:وَلَئِن رُّجِعْتُ إِلَىٰ رَبِّىٓ إِنَّ لِى عِندَهُۥ لَلْحُسْنَىٰ, tr:ve lein rucı'tü ilâ rabbî inne lî indehû le'l-hüsnâ, gloss:Rabbime döndürülsem bile onun yanında benim için elbette en güzel vardır, source:41:50}. Bu adam vaadi doğrulamaz, en güzeli kendine borç sayar. Surenin on dokuzuncu ayetindeki "yanında" kelimesi burada tersine işler. Allah'ın ölçüsü de söylenir: {ar:وَيَجْزِىَ ٱلَّذِينَ أَحْسَنُوا۟ بِٱلْحُسْنَى, tr:ve yecziye'llezîne ahsenû bi'l-hüsnâ, gloss:güzel davrananları en güzelle karşılamak için, source:53:31}. Zülkarneyn'e iki seçenek bırakılır ve o surenin çerçevesini kendi ağzıyla kurar: {ar:أَمَّا مَن ظَلَمَ فَسَوْفَ نُعَذِّبُهُۥ, tr:emmâ men zaleme fe-sevfe nuazzibuh, gloss:zulmedene gelince onu cezalandıracağız, source:18:87}. Ardından şöyle der: {ar:فَلَهُۥ جَزَآءً ٱلْحُسْنَىٰ ۖ وَسَنَقُولُ لَهُۥ مِنْ أَمْرِنَا يُسْرًۭا, tr:fe-lehû cezâeni'l-hüsnâ ve se-nekûlü lehû min emrinâ yüsrâ, gloss:onun için karşılık olarak en güzel vardır; ona işimizden kolay olanı söyleyeceğiz, source:18:88}. En güzel, karşılık ve kolaylık bu ayette yan yanadır. Son ayetin kalıbı bir sonraki surede Peygambere söylenen vaatte tekrarlanır: {ar:وَلَسَوْفَ يُعْطِيكَ رَبُّكَ فَتَرْضَىٰٓ, tr:ve le-sevfe yu'tîke rabbüke fe-terdâ, gloss:Rabbin sana verecek ve sen hoşnut olacaksın, source:93:5}. Bu surede veren insandı. Orada veren Rabdir ve hoşnutluk aynı fiille gelir. Hoşnutluğun iki yönü de söylenir: {ar:رَّضِىَ ٱللَّهُ عَنْهُمْ وَرَضُوا۟ عَنْهُ, tr:radiya'llâhu anhüm ve radû anh, gloss:Allah onlardan hoşnut oldu, onlar da O'ndan, source:98:8}. Dönüş çağrısı da aynı ikiliği taşır: {ar:ٱرْجِعِىٓ إِلَىٰ رَبِّكِ رَاضِيَةًۭ مَّرْضِيَّةًۭ, tr:ırci'î ilâ rabbiki râdıyeten mardıyye, gloss:Rabbine hoşnut ve hoşnut olunmuş olarak dön, source:89:28}.

Kaynaklar: 92:6 وَصَدَّقَ ص د ق B004; 92:6 بِٱلْحُسْنَىٰ ح س ن B003; 92:9 وَكَذَّبَ ك ذ ب B002; 92:9 بِٱلْحُسْنَىٰ ح س ن B003; 92:13 لَلْءَاخِرَةَ ء خ ر B004; 92:19 تُجْزَىٰٓ ج ز ي B001; 92:21 يَرْضَىٰ ر ض و B001; 92:21 يَرْضَىٰ ر ض و B002

## Buluşmalar

Görüntülerin en sık birleştiği yer, uçurum ile elin aynı sahnede durmasıdır. Cennet ehlinden biri dünyadaki arkadaşını anlatır. Arkadaşı ona alay ederek şöyle sormuştur: {ar:يَقُولُ أَءِنَّكَ لَمِنَ ٱلْمُصَدِّقِينَ, tr:yekûlü einneke le-mine'l-musaddikîn, gloss:sen de mi doğrulayanlardansın derdi, source:37:52}. Sonra adam aşağı bakar ve arkadaşını ateşin ortasında görür: {ar:فَٱطَّلَعَ فَرَءَاهُ فِى سَوَآءِ ٱلْجَحِيمِ, tr:fettalea fe-raâhu fî sevâi'l-cahîm, gloss:eğilip baktı ve onu cehennemin ortasında gördü, source:37:55}. Ona şöyle der: {ar:تَٱللَّهِ إِن كِدتَّ لَتُرْدِينِ, tr:ta'llâhi in kidte le-türdîn, gloss:Allah'a andolsun beni de neredeyse yuvarlayacaktın, source:37:56}. Ardından ekler: {ar:وَلَوْلَا نِعْمَةُ رَبِّى لَكُنتُ مِنَ ٱلْمُحْضَرِينَ, tr:ve levlâ ni'metü rabbî le-küntü mine'l-muhdarîn, gloss:Rabbimin nimeti olmasaydı ben de oraya getirilenlerden olurdum, source:37:57}. Bu sahnede doğrulama, yuvarlanma, yüksekten bakış ve bir nimet bir aradadır. Surenin on dokuzuncu ayeti verenin yanında kimsenin bir nimeti olmadığını söyler. Cennet ehli ise kurtuluşunu tek bir nimete, Rabbinin nimetine bağlar. İnsanlar arasında karşılığı ödenecek bir el yoktur, ama Rabbin eli her şeyi taşır. Bir başka ayet aynı birleşmeyi müminlere hatırlatma olarak kurar: Allah'ın nimetiyle kardeş olmuşlardır ve {ar:وَكُنتُمْ عَلَىٰ شَفَا حُفْرَةٍۢ مِّنَ ٱلنَّارِ فَأَنقَذَكُم مِّنْهَا, tr:ve küntüm alâ şefâ hufratin mine'n-nâri fe-enkazeküm minhâ, gloss:ateşten bir çukurun kenarındaydınız; sizi oradan kurtardı, source:3:103}. Ayet {ar:لَعَلَّكُمْ تَهْتَدُونَ, tr:leallekum tehtedûn, gloss:doğru yolu bulasınız diye, source:3:103} diye kapanır. Kuyunun kenarı, nimet ve yol gösterme tek ayettedir. Kenara çekilen, uyarı ateşini işaret ateşi olarak okuyandır.

İkinci büyük buluşma bir sarayda geçer. Musa ile Harun'a Firavun'a ne diyecekleri öğretilir: {ar:وَٱلسَّلَٰمُ عَلَىٰ مَنِ ٱتَّبَعَ ٱلْهُدَىٰٓ, tr:ve's-selâmü alâ meni't-tebea'l-hüdâ, gloss:esenlik yol göstericiye uyanadır, source:20:47}. Ardından {ar:أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ, tr:enne'l-azâbe alâ men kezzebe ve tevellâ, gloss:azap yalanlayıp yüz çevirenedir, source:20:48} gelir. Firavun {ar:قَالَ فَمَن رَّبُّكُمَا يَٰمُوسَىٰ, tr:kâle fe-men rabbükümâ yâ mûsâ, gloss:ey Musa, sizin Rabbiniz kim dedi, source:20:49} diye sorar. Musa şöyle cevap verir: {ar:قَالَ رَبُّنَا ٱلَّذِىٓ أَعْطَىٰ كُلَّ شَىْءٍ خَلْقَهُۥ ثُمَّ هَدَىٰ, tr:kâle rabbüne'llezî a'tâ külle şey'in halkahû sümme hedâ, gloss:Rabbimiz her şeye yaratılışını verip sonra yol gösterendir dedi, source:20:50}. Bu cevapta surenin üç fiili aynı cümlededir: üçüncü ayetin yaratması, beşinci ayetin vermesi ve on ikinci ayetin yol göstermesi. Bir ayet önce de on altıncı ayetin iki fiili geçmiştir. Aynı Firavun başka bir surede yüceliği kendine mal eder: {ar:فَقَالَ أَنَا۠ رَبُّكُمُ ٱلْأَعْلَىٰ, tr:fe-kâle ene rabbükümü'l-a'lâ, gloss:ben sizin en yüce rabbinizim dedi, source:79:24}. Ardından {ar:فَأَخَذَهُ ٱللَّهُ نَكَالَ ٱلْءَاخِرَةِ وَٱلْأُولَىٰٓ, tr:fe-ehazehu'llâhu nekâle'l-âhirati ve'l-ûlâ, gloss:Allah onu sonranın ve öncenin cezasıyla yakaladı, source:79:25} gelir. Elin, yolun, yüz çevirmenin, yüceliğin ve mülkün görüntüleri burada tek bir karşılaşmada birleşir. Veren Rab ile tutan kral karşı karşıya gelir. Yüceliği iddia eden kral, surenin "son da ilk de bizimdir" sözüyle düşürülür.

Yüz ile elin buluşması iyiliğin tanımında görülür. İyilik yüzü doğuya ya da batıya çevirmek değildir: {ar:لَّيْسَ ٱلْبِرَّ أَن تُوَلُّوا۟ وُجُوهَكُمْ قِبَلَ ٱلْمَشْرِقِ وَٱلْمَغْرِبِ, tr:leyse'l-birra en tüvellû vucûheküm kıbele'l-meşriki ve'l-mağrib, gloss:iyilik yüzlerinizi doğu ve batı yönüne çevirmeniz değildir, source:2:177}. Aynı ayet iyiliği şöyle sayar: {ar:وَءَاتَى ٱلْمَالَ عَلَىٰ حُبِّهِۦ, tr:ve âte'l-mâle alâ hubbih, gloss:malı sevmesine rağmen verdi, source:2:177}. Malın gittiği yerler arasında {ar:وَفِى ٱلرِّقَابِ, tr:ve fi'r-rikâb, gloss:boyunları çözmek için, source:2:177} de vardır. Ayet şöyle biter: {ar:أُو۟لَٰٓئِكَ ٱلَّذِينَ صَدَقُوا۟ ۖ وَأُو۟لَٰٓئِكَ هُمُ ٱلْمُتَّقُونَ, tr:ülâike'llezîne sadakû ve ülâike hümü'l-müttekûn, gloss:işte doğru olanlar onlardır ve sakınanlar da onlardır, source:2:177}. Yüzü çevirmek, malı vermek, boyun çözmek, hücumu sonuna kadar götüren doğruluk ve siper olan sakınma tek ayette bir araya gelir. Yüz çevirmek iyiliğin kendisi değildir, iyilik eldedir. Ama surenin yirminci ayeti eli tekrar yüze bağlar: veren el, aranan yüz için uzanır. Aynı bağ yoksulları doyuranların sözünde görülür: {ar:إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءًۭ وَلَا شُكُورًا, tr:innemâ nut'imüküm li-vechi'llâhi lâ nürîdü minküm cezâen ve lâ şükûrâ, gloss:sizi yalnızca Allah'ın yüzü için doyuruyoruz; sizden ne karşılık ne teşekkür istiyoruz, source:76:9}. Sözün sonunda {ar:إِنَّا نَخَافُ مِن رَّبِّنَا يَوْمًا عَبُوسًۭا قَمْطَرِيرًۭا, tr:innâ nehâfü min rabbinâ yevmen abûsen kamtarîrâ, gloss:biz Rabbimizden asık suratlı, çetin bir günden korkarız, source:76:10} derler. Sonra {ar:فَوَقَىٰهُمُ ٱللَّهُ شَرَّ ذَٰلِكَ ٱلْيَوْمِ, tr:fe-vekâhumu'llâhu şerra zâlike'l-yevm, gloss:Allah onları o günün kötülüğünden korudu, source:76:11} gelir. El, yüz, karşılığın reddi ve siper bu ayetlerde surenin sırasıyla dizilir. Bunun tam tersi de bir sahne olarak anlatılır. Bir adam Allah'a söz vermiştir: {ar:لَئِنْ ءَاتَىٰنَا مِن فَضْلِهِۦ لَنَصَّدَّقَنَّ, tr:lein âtânâ min fadlihî le-nessaddakanne, gloss:bize lütfundan verirse mutlaka sadaka vereceğiz, source:9:75}. Sonra şu olur: {ar:فَلَمَّآ ءَاتَىٰهُم مِّن فَضْلِهِۦ بَخِلُوا۟ بِهِۦ وَتَوَلَّوا۟ وَّهُم مُّعْرِضُونَ, tr:fe-lemmâ âtâhüm min fadlihî bahılû bihî ve tevellev ve hüm mu'ridûn, gloss:lütfundan verince cimrilik ettiler ve yüz çevirdiler; zaten dönüp gidiyorlardı, source:9:76}. Sıkan el ile dönülen sırt aynı kişidedir. Sekizinci ve on altıncı ayetler tek bir hikâyede birleşir.

Büyüme ile yükseklik, yüksekteki bahçede buluşur. Allah'ın hoşnutluğunu arayarak harcayanların durumu {ar:كَمَثَلِ جَنَّةٍۭ بِرَبْوَةٍ أَصَابَهَا وَابِلٌۭ فَـَٔاتَتْ أُكُلَهَا ضِعْفَيْنِ, tr:ke-meseli cennetin bi-rabvetin esâbehâ vâbilün fe-âtet ükulehâ dı'feyn, gloss:yüksekçe bir yerdeki bahçe gibidir; ona sağanak isabet eder ve ürününü iki kat verir, source:2:265} diye anlatılır. Bu bahçe kuyunun tam karşıtıdır. Aşağıda değil yüksektedir. Yağmur onu süpürmez, büyütür. Verme fiili de bahçenin kendi fiilidir. Aynı yükseklik ateşe dönük bir eğiklikle karşılaşır: Bir yanda takva ve hoşnutluk üzerine kurulmuş yapı, öbür yanda {ar:عَلَىٰ شَفَا جُرُفٍ هَارٍۢ فَٱنْهَارَ بِهِۦ فِى نَارِ جَهَنَّمَ, tr:alâ şefâ cürufin hârin fenhâra bihî fî nâri cehennem, gloss:çökmek üzere olan bir yarın kenarına kurulmuş, onunla birlikte cehennem ateşine yıkılmış yapı, source:9:109} vardır. Biri takva ve hoşnutluk üzerine kurulur, öteki çöküp ateşe düşer. Cimrinin malı da düştüğü yerde onun yanına yapışır: {ar:يَوْمَ يُحْمَىٰ عَلَيْهَا فِى نَارِ جَهَنَّمَ فَتُكْوَىٰ بِهَا جِبَاهُهُمْ وَجُنُوبُهُمْ وَظُهُورُهُمْ, tr:yevme yuhmâ aleyhâ fî nâri cehenneme fe-tukvâ bihâ cibâhühüm ve cünûbühüm ve zuhûruhüm, gloss:o gün onlar cehennem ateşinde kızdırılır ve alınları, yanları ve sırtları onlarla dağlanır, source:9:35}. Sakınanın yanında bir kalkan durur ve o yanından kötülükten uzak tutulur. Biriktirenin yanı ise biriktirdiğiyle dağlanır. Sırtı da yüz çevirdiği için dönmüş olan sırttır.

Musa'nın ateşi ise işaret ateşi ile yakan ateşi bir arada tutar. Musa ailesine {ar:أَوْ أَجِدُ عَلَى ٱلنَّارِ هُدًۭى, tr:ev ecidü ale'n-nâri hüdâ, gloss:ya da ateşin başında bir yol gösterici bulurum, source:20:10} der. Başka bir anlatımda {ar:لَّعَلَّكُمْ تَصْطَلُونَ, tr:leallekum tastalûn, gloss:belki ısınırsınız, source:27:7} der. Isınmak on beşinci ayetin yanmasıyla aynı köktendir. Yanına yaklaşılan ateş ısıtır ve yol gösterir. İçine girilen ateş ise yakar. Surenin hareketi bu iki mesafe arasında kurulur. İlk iki ayette gece serilir ve gün yarılır. Gece insanların koşusunu örter, gün o koşunun dağıldığını gösterir. Yol ayrılır ve her yol yürüyenine göre düzlenir. Biri verir, siper kurar ve vaadi kendi eliyle doğrular. Öteki malını tutar, ona cübbe gibi bürünür ve vaadi yalanlayıp sırtını döner. Sonra gece yolunda bir ateş yakılır ve bir ses "uyardım" der. Uyarıyı işaret olarak okuyan, dizgini tutulan bir binek gibi kenara çekilir. Yüzü kendisine bir nimet borcu olanlara değil, yüceliğe dönüktür. Uyarıyı duymayan, yuvarlandığı anda elindeki malın ona yetmediğini görür ve ateşin içine girer. Surenin son kelimesi, kayıp devesini arayan adamın onu bulduğu anın kelimesidir: hoşnutluk. Bu hoşnutluk, ilk ayetteki gecenin örtüsünden sonra gelen yüzün açılmasıdır.

