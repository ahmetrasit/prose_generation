Focus: 96:8. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/96_8/D.r13/context.md =====
# 96:8 — focus

إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ

Anchor translation (canonical reading, reference only):

Dönüş kesinlikle Rabbinedir.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | إِنَّ | إِنّ |  | ACC |
| 2 | إِلَىٰ | إِلَىٰ |  | P |
| 3 | رَبِّكَ | رَبّ | ر ب ب | N;PRON |
| 4 | ٱلرُّجْعَىٰٓ | رُّجْعَىٰٓ | ر ج ع | DET;N |


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
- 96:3 ٱقْرَأْ وَرَبُّكَ ٱلْأَكْرَمُ
- 96:4 ٱلَّذِى عَلَّمَ بِٱلْقَلَمِ
- 96:5 عَلَّمَ ٱلْإِنسَٰنَ مَا لَمْ يَعْلَمْ
- 96:6 كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ
- 96:7 أَن رَّءَاهُ ٱسْتَغْنَىٰٓ
- 96:8 ◀ focus إِنَّ إِلَىٰ رَبِّكَ ٱلرُّجْعَىٰٓ
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


===== _commentary/v16/work/96_8/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

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

## ر ج ع (root_000544) — identity root of ٱلرُّجْعَىٰٓ (w4)

- **B001** geri dönmek veya geri döndürmek — kendiliğinden önceki yere veya duruma dönmek · birini ya da bir şeyi yerine geri göndermek · başkasını geri döndürmek
  أصل كبير مطرد منقاس يدل على رد وتكرار (maqayis)؛ رجعت رجوعا ورجعته يستوي فيه اللازم والمجاوز (ayn)؛ رجعته إلى أهله أي رددته إليهم (jamhara)؛ رجع بنفسه رجوعا ورجعة غيره رجعا (sihah)؛ رجعته رجعا فرجع رجوعا (tahdhib)؛ الرجوع العود إلى ما كان منه البدء والرجع الإعادة (mufradat)
- **B002** ölümden sonra dönüş ve yeniden diriliş — Tanrı'ya dönüş veya nihai varış · Tanrı'ya kaçınılmaz dönüş · ölümden sonra dünyaya yeniden gelme
  إلى الله عز وجل مرجعك ورجوعك ورجعاك (jamhara)؛ فلان يؤمن بالرجعة أي بالرجوع إلى الدنيا بعد الموت (sihah)؛ إنه على بعثه يوم القيامة لقادر (tahdhib)؛ إلى الله مرجعكم وإن إلى ربك الرجعى (mufradat)
- **B003** bir şeyden vazgeçip geri dönmek [kalıp] — bir işten vazgeçmek veya yanlış davranışı bırakmak
  رجعت عن كذا رجعا؛ يرجعون عن الذنب؛ حرمنا عليهم أن يتوبوا ويرجعوا عن الذنب (mufradat)
- **B004** boşama sonrası evlilik bağına geri alma — boşanan eşi geri alma hakkı · boşadığı eşini evlilik bağına geri almak · eşi öldükten veya boşandıktan sonra ailesine dönen kadın
  راجع الرجل امرأته وهي الرجعة (maqayis)؛ طلاقا يملك الرجعة والرجعة والرجعى (jamhara)؛ له على امرأته رجعة (sihah)؛ المراجع من النساء التي يموت زوجها أو يطلقها فترجع إلى أهلها (tahdhib)؛ الرجعة والرجعة في الطلاق (mufradat)
- **B005** iletiye dönen yanıt — mektubun veya iletinin yanıtı · geri dönen yanıt · cevabı sahibine geri iletmek
  المرجوع جواب الرسالة (maqayis)؛ رجعى رسالتي أي مرجوعها ورجعان الكتاب جوابه (sihah)؛ رجع الجواب ورجع الرشق في الرمي ما يرد عليه (tahdhib)؛ بم يرجع المرسلون فمن رجع الجواب (mufradat)
- **B006** yinelenen yağmur veya biriken su — yağmur veya yeniden biriken su · su birikintileri veya su toplayan vadi üstleri
  الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث (maqayis)؛ الرجع الغدير أو الماء يترقرق والرجع المطر (jamhara)؛ الرجع المطر والرجع الغدير (sihah)؛ ذات الرجع أي ذات المطر والرجع في كلام العرب الماء والرجعان أعالي التلاع (tahdhib)؛ والسماء ذات الرجع أي المطر وسمي الغدير رجعا (mufradat)
- **B007** sesi yineleyip dalgalandırma — okuma veya söylemede sesi yineleyip dalgalandırma · namaza çağrıda tanıklık sözlerini tekrarlama · gök gürültüsünün yinelenen sesi
  الترجيع في الصوت ترديده (maqayis)؛ الترجيع تقارب ضروب الحركات في الصوت (ayn)؛ ترجيع الصوت ترديده في الحلق والترجيع في الأذان (sihah)؛ يقولون للرعد رجع والترجيع في الأذان (tahdhib)؛ الترجيع ترديد الصوت باللحن في القراءة وفي الغناء وتكرير قول مرتين فصاعدا (mufradat)
- **B008** hayvanın ön ayak adımı [kalıp] — hayvanın ön ayaklarını geri getirerek attığı adım · dişi devenin yürüyüş biçimini değiştirmesi
  الرجع رجع الدابة يديها في السير (maqayis)؛ الرجع ترجيع الدابة يدها في السير (ayn)؛ رجع الدابة يديها في السير خطوها (sihah)؛ الرجع الخطو وراجعت الناقة رجاعا إذا كانت في ضرب من السير فرجعت إلى سير سواه (tahdhib)
- **B009** çizgileri yeniden çekip karartmak [kalıp] — dövme çizgilerini yeniden çekmek veya karartmak
  ترجيع وشي النقش والوشم والكتابة خطوطها (ayn)؛ رجع الواشمة خطها (sihah)؛ رجع الوشم والنقوش وترجيعه أن يعاد عليه السواد مرة بعد أخرى (tahdhib)
- **B010** elini geriye uzatmak [kalıp] — elini geriye, ok kılıfına veya kılıca uzatmak
  أرجع الرجل يده في كنانته (maqayis)؛ أرجع يده إلى سيفه ليستله أو إلى كنانته ليأخذ سهما (jamhara)؛ أرجع الرجل إذا أهوى بيده إلى خلفه ليتناول شيئا (sihah)؛ أرجع الرجل يده إذا أهوى بها إلى كنانته (tahdhib)؛ أرجع يده إلى سيفه ليستله (mufradat)
- **B011** satış bedeliyle yerine mal almak — hayvanları satıp bedeliyle yerlerine başkalarını almak · satılanın bedeliyle alınan veya tahsilde yerine kabul edilen karşılık
  الراجعة الناقة تباع ويشترى بثمنها مثلها (maqayis)؛ ارتجع فلان إبلا إذا باع الذكور واشترى الإناث (jamhara)؛ الرجعة في الصدقة إذا أخذ المصدق مكانها أسنانا فوقها أو دونها (sihah)؛ الارتجاع أن يبيعها ثم يشتري بثمنها مثلها أو غيرها (tahdhib)؛ دابة لها مرجوع يمكن بيعها بعد الاستعمال وارتجع إبلا (mufradat)
- **B012** kuşların göçten geri dönüşü — kuşların mevsimsel geçişten sonra geri dönüşü
  الرجاع رجوع الطير بعد قطاعها (maqayis)؛ الرجاع رجوع الطير بعد قطاعها إذا رجعت من المواضع الحارة إلى المواضع الباردة (jamhara)؛ الرجاع أيضا رجوع الطير بعد قطاعها (sihah)؛ الرجاع مختص برجوع الطير بعد قطاعها (mufradat)
- **B013** gebeliğin oluşmaması veya çok erken sona ermesi [kalıp] — çiftleştiği halde gebe kalmayan veya gebe sanılıp boş çıkan dişi deve · yavrusu biçimlenmeden düşük yapmak
  ناقة راجع وهي التي يضربها الفحل فلا تلقح (jamhara)؛ أتان راجع وناقة راجع فيظن أن بها حملا ثم تخلف (sihah)؛ إذا ألقت الناقة حملها قبل أن يستبين خلقه قيل قد رجعت (tahdhib)؛ ناقة راجع ترد ماء الفحل فلا تقبله (mufradat)
- **B014** yolculukta yıpranma veya güçsüzlükten sonra toparlanma [kalıp] — bir yolculuktan ötekine sürülerek bitkin düşmüş hayvan · zayıflıktan sonra semirip iyi duruma gelmek · hastalıktan sonra kendini ve gücünü yeniden bulmak
  الرجيع من الدواب ما رجعته من سفر إلى سفر وأرجعت الإبل إذا كانت مهازيل فسمنت (maqayis)؛ بعير رجيع سفر مثل نضو سفر (jamhara)؛ الرجيع من الدواب ما رجعته من سفر إلى سفر وهو الكال (sihah)؛ يقال للمريض إذا ثابت إليه نفسه بعد تهوك من العلة راجع (tahdhib)؛ من الدابة ما رجعته من سفر إلى سفر ورجع سفر كناية عن النضو (mufradat)
- **B015** geri çıkan veya yeniden işlenen şey — sindirimden sonra çıkan dışkı veya bağırsak artığı · hayvanın ağzına getirip yeniden çiğnediği geviş · sahibine geri çevrilen veya yinelenen söz · eskimiş veya sökülüp yeniden yapılmış giysi · soğuduktan sonra yeniden ısıtılmış yemek
  الرجيع الجرة لأنه يردد مضغها (maqayis)؛ الرجيع يكنى به عن ذي البطن وحبل رجيع وثوب رجيع (jamhara)؛ الرجيع الروث والبعر وذو البطن وكل شئ يردد فهو رجيع (sihah)؛ الرجيع يكون الروث والعذرة والرجيع العرق وكل طعام برد فأعيد على النار فهو رجيع (tahdhib)؛ الرجيع كناية عن أذى البطن وجبة رجيع أعيدت بعد نقضها (mufradat)

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

===== _commentary/v16/out/s096/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 96:8, and ## Buluşmalar) =====
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

## Ad, iz, işaret

Bir şey, üzerine yükseltilen ya da içine bastırılan bir işaretle tanınır. Sure {ar:بِٱسْمِ, tr:bismi, gloss:adıyla, source:96:1} diye başlar. Ad kelimesinin kökü yüksekliktir: {ar:أصل اسم سمو وهو من العلو لأنه تنويه ودلالة على المعنى, tr:aslu ismin sumuvvun ve huve mine'l-ʿuluvv, gloss:ismin aslı yükselmedir; çünkü anlamı ortaya çıkarır ve ona işaret eder, source:"س م و,B005"}. Kayıtlı bir başka türetmeye göre ise ad bir damgadır: {ar:ووسمت الشيء وسما: أثرت فيه بسمة, tr:ve vesemtu'ş-şey'e vesmen, gloss:bir şeye damga vurarak iz bıraktım, source:"و س م,B001"}. İlk anlamda ad, yükseğe kaldırılan bir işarettir; ikinci anlamda bir şeye bastırılan izdir. Kurân Rab'bin adını yükseklikle ve yaratmayla birlikte anar: {ar:سَبِّحِ ٱسْمَ رَبِّكَ ٱلْأَعْلَى, tr:sebbihi'sme rabbike'l-aʿlâ, gloss:en yüce Rabbinin adını tesbih et, source:87:1}, {ar:ٱلَّذِى خَلَقَ فَسَوَّىٰ, tr:ellezî halaka fe sevvâ, gloss:ki yarattı ve düzenledi, source:87:2}. Bu yapı surenin ilk ayetine çok yakındır. Adı anmak secdeye de bağlanır: {ar:وَٱذْكُرِ ٱسْمَ رَبِّكَ بُكْرَةً وَأَصِيلًا, tr:vezkuri'sme rabbike bukraten ve asîlâ, gloss:sabah akşam Rabbinin adını an, source:76:25}, {ar:وَمِنَ ٱلَّيْلِ فَٱسْجُدْ لَهُۥ, tr:ve mine'l-leyli fescud leh, gloss:gecenin bir kısmında O'na secde et, source:76:26}.

Öğretme kökü de işarettir: {ar:أصل صحيح واحد يدل على أثر بالشيء يتميز به عن غيره, tr:aslun sahîhun vâhidun yedullu ʿalâ eserin bi'ş-şey', gloss:bir şeyi diğerlerinden ayıran bir ize delalet eden tek bir asıl, source:"ع ل م,B002"}. Bu kök sancağı ve kumaşın kenar nakışını da adlandırır: {ar:العلم الراية, tr:el-ʿalemu'r-râye, gloss:alem sancaktır, source:"ع ل م,B002"}. Görme kökü de bu sancağa varır: {ar:الراية العلامة المنصوبة للرؤية, tr:er-râyetu'l-ʿalâmetu'l-mensûbetu li'r-ru'ye, gloss:sancak, görülmek için dikilmiş işarettir, source:"ر ء ي,B011"}. On ikinci ayetteki {ar:أَمَرَ, tr:emera, gloss:emretti, source:96:12} fiilinin ailesinde yol işareti vardır: {ar:الأمارة العلامة، والأمار أمار الطريق معالمه, tr:el-emâretu'l-ʿalâme, gloss:emâre işarettir; emâr, yolun belirtileridir, source:"ء م ر,B005"}. Sekizinci ayetin dönüş kelimesinin ailesinde, yazının çizgilerinin tekrar tekrar mürekkeplenmesi bulunur: {ar:أن يعاد عليه السواد مرة بعد أخرى, tr:en yuʿâde ʿaleyhi's-sevâdu merraten baʿde uhrâ, gloss:üzerine siyahın tekrar tekrar geçirilmesi, source:"ر ج ع,B009"}.

Sure bu işaretleri yüze taşır. On beşinci ayetin {ar:لَنَسْفَعًۢا, tr:le nesfaʿan, gloss:mutlaka yakalarız, source:96:15} fiilinin ailesinde koyu bir leke vardır: {ar:السفعة بالضم سواد مشرب حمرة, tr:es-sufʿa sevâdun uşribe humra, gloss:sufʿa, kırmızıya çalan siyahlıktır, source:"س ف ع,B002"}. Son ayetin secdesinin ailesinde ise alındaki iz vardır: {ar:المسجد بالفتح جبهة الرجل حيث يصيبه ندب السجود, tr:el-mesced cebhetu'r-racul, gloss:mesced, adamın secde izinin düştüğü alnıdır, source:"س ج د,B003"}. Kurân iki tarafın da yüzüne iz koyar. Müminler için {ar:سِيمَاهُمْ فِى وُجُوهِهِم مِّنْ أَثَرِ ٱلسُّجُودِ, tr:sîmâhum fî vucûhihim min eseri's-sucûd, gloss:secde izinden belirtileri yüzlerindedir, source:48:29} denir. Çok yemin eden iftiracı için {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16} denir. Suçlular da yüzlerindeki işaretle tanınır: {ar:يُعْرَفُ ٱلْمُجْرِمُونَ بِسِيمَٰهُمْ فَيُؤْخَذُ بِٱلنَّوَٰصِى وَٱلْأَقْدَامِ, tr:yuʿrafu'l-mucrimûne bi sîmâhum fe yu'hazu bi'n-nevâsî ve'l-akdâm, gloss:suçlular belirtilerinden tanınır, perçemlerinden ve ayaklarından yakalanırlar, source:55:41}. Yazılı kayıt da işaretlenmiştir: {ar:كِتَٰبٌ مَّرْقُومٌ, tr:kitâbun merkûm, gloss:işaretlenmiş bir kitap, source:83:20}, {ar:يَشْهَدُهُ ٱلْمُقَرَّبُونَ, tr:yeşheduhu'l-mukarrabûn, gloss:ona yakınlaştırılanlar şahit olur, source:83:21}.

Böylece sure Rab'bin adıyla başlar, işaret koyan bir araçla öğretir ve iki işaretli alınla biter: biri yakalanıp karartılan alın, öteki secdenin iz bıraktığı alın.

Kaynaklar: 96:1 بِٱسْمِ س م و B005; 96:1 بِٱسْمِ و س م B001; 96:4 عَلَّمَ ع ل م B002; 96:7 رَّءَاهُ ر ء ي B011; 96:12 أَمَرَ ء م ر B005; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B009; 96:15 لَنَسْفَعًۢا س ف ع B002; 96:19 وَٱسْجُدْ س ج د B003

## Su: bulut, yağmur, taşkın ve gölet

Bu sahne suyun bütün yolculuğunu izler. Bulut yağmur getirir, ilk yağmur yeri bitkiyle işaretler, ardından ikinci yağmur gelir, yağmur döne döne yağar. Bazı yerler ise atlanır. Su bazen ölçüsünü aşar, taşar ve her şeyi sürükler, sonra yolunun sonundaki gölete varır ve orada durulur.

Üçüncü ayetteki en cömert sıfatının ailesinde yağmur getiren bulut ve verimli toprak vardır: {ar:كرم السحاب أتى بالغيث, tr:kerume's-sehâb, gloss:bulut cömert oldu, yani yağmur getirdi, source:"ك ر م,B002"}; {ar:أرض مكرمة للنبات, tr:ardun mekrame li'n-nebât, gloss:bitkiye cömert toprak, source:"ك ر م,B002"}. Rab kelimesinin ailesinde bitkileri büyüten bulut vardır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb, gloss:rabâb buluttur; bitkiyi büyüttüğü için böyle adlandırılmıştır, source:"ر ب ب,B008"}. Bu, rahimdeki cenini aşama aşama büyüten aynı terbiye işidir. Kayıtlı bir türetmeye göre ad kelimesinin ailesinde de yılın ilk yağmuru vardır: {ar:الوسمي أول مطر السنة يسم الأرض بالنبات, tr:el-vesmiyyu evvelu matari's-sene, gloss:vesmî, yeri bitkiyle işaretleyen yılın ilk yağmurudur, source:"و س م,B003"}. On üçüncü ayetteki {ar:وَتَوَلَّىٰٓ, tr:ve tevellâ, gloss:ve yüz çevirdi, source:96:13} fiilinin kökünde bu yağmuru izleyen yağmur bulunur: {ar:الولي المطر يجيء بعد الوسمي سمي بذلك لأنه يلي الوسمي, tr:el-veliyy el-matar yecî'u baʿde'l-vesmî, gloss:veliy, vesmîden sonra gelen yağmurdur; onu izlediği için böyle denir, source:"و ل ي,B010"}. Bu iki aile anlamı birer yankıdır; ayetlerdeki anlamlar "ad" ve "yüz çevirme"dir. Sekizinci ayetteki dönüş kelimesinin ailesinde ise dönüp duran yağmur vardır: {ar:الرجع الغيث وهو المطر لأنها تغيث وتصب ثم ترجع فتغيث, tr:er-recʿu'l-gays, gloss:rec yağmurdur, çünkü yağar, sonra döner ve tekrar yağar, source:"ر ج ع,B006"}. Kurân göğe bu sıfatla yemin eder: {ar:وَٱلسَّمَآءِ ذَاتِ ٱلرَّجْعِ, tr:ve's-semâ'i zâti'r-recʿ, gloss:dönüp dönüp yağmur veren göğe andolsun, source:86:11}. On yedinci ayetin {ar:نَادِيَهُۥ, tr:nâdiyeh, gloss:meclisini, source:96:17} kelimesinin ailesinde nem ve cömertlik vardır: {ar:يعبر عن السخاء بالندى, tr:yuʿabbaru ʿani's-sehâ'i bi'n-nedâ, gloss:cömertlik "nem" ile ifade edilir, source:"ن د و,B004"}. On altıncı ayetin {ar:خَاطِئَةٍ, tr:hâti'e, gloss:günahkâr, source:96:16} kelimesinin ailesinde ise yağmurun atladığı toprak vardır: {ar:الخطيئة أرض يخطئها المطر ويصيب غيرها, tr:el-hatî'e ardun yuhti'uha'l-matar, gloss:hatîe, yağmurun ıskalayıp başka yere düştüğü topraktır, source:"خ ط ء,B003"}.

Kurân rahim ile yağmuru tek ayette birleştirir. Rahimdeki aşamalardan sonra {ar:وَتَرَى ٱلْأَرْضَ هَامِدَةً فَإِذَآ أَنزَلْنَا عَلَيْهَا ٱلْمَآءَ ٱهْتَزَّتْ وَرَبَتْ, tr:ve tera'l-arda hâmideten fe izâ enzelnâ ʿaleyhe'l-mâ'e'htezzet ve rabet, gloss:yeri kupkuru görürsün; üzerine suyu indirince harekete geçer ve kabarır, source:22:5} denir. Bu ayet canlanmayı yaratılışla aynı kanıta bağlar. Dünya hayatı da yağmurla büyüyüp biçilen bir ekin olarak anlatılır: {ar:كَأَن لَّمْ تَغْنَ بِٱلْأَمْسِ, tr:keen lem tegne bi'l-ems, gloss:sanki dün orada hiç yokmuş gibi, source:10:24}. Bu ifadede, yedinci ayetin yeterlilik köküyle aynı kökten bir fiil, yerleşik yaşamın bir gecede silinmesini anlatır.

Su ölçüsünü de aşabilir. Altıncı ayetin azma fiili için {ar:طغى الماء خروجه عن المقدار, tr:tagâ'l-mâ' hurûcuhû ʿani'l-mikdâr, gloss:suyun azması ölçüsünden çıkmasıdır, source:"ط غ ي,B002"} ve {ar:طغا البحر والماء إذا علا كل شيء فاجترفه, tr:tagâ'l-bahru ve'l-mâ', gloss:deniz ve su her şeyin üstüne çıkıp onu sürükledi, source:"ط غ ي,B002"} denir. Kök genel olarak ölçüyü aşmaktır: {ar:كل شيء جاوز القدر فقد طغا, tr:kullu şey'in câveze'l-kadr fe kad tagâ, gloss:ölçüyü aşan her şey azmıştır, source:"ط غ ي,B001"}. Kurân bunu Nuh'un tufanı için kullanır: {ar:إِنَّا لَمَّا طَغَا ٱلْمَآءُ حَمَلْنَٰكُمْ فِى ٱلْجَارِيَةِ, tr:innâ lemmâ tage'l-mâ'u hamelnâkum fi'l-câriye, gloss:su taştığında sizi akan gemide taşıdık, source:69:11}. Kuralı da teraziyle birlikte koyar: {ar:أَلَّا تَطْغَوْا۟ فِى ٱلْمِيزَانِ, tr:ellâ tatgav fi'l-mîzân, gloss:ölçüde aşırı gitmeyesiniz diye, source:55:8}. Böylece azma, yaratmanın ölçüsünün karşısına konur.

Taşkının sonu gölettir. On beşinci ayetin vazgeçme fiilinin ailesinde şu anlamlar bulunur: {ar:النهي والنهي الغدير لأن الماء ينتهي إليه, tr:en-nehy, el-gadîr, gloss:nehy göllenmiş sudur, çünkü su ona varıp durur, source:"ن ه ي,B004"}; {ar:تناهى الماء إذا وقف في الغدير وسكن, tr:tenâha'l-mâ', gloss:su gölette durup sakinleşti, source:"ن ه ي,B004"}. Dönüş kelimesinin ailesinde gölete de "rec" denir: {ar:سمي الغدير رجعا, tr:summiye'l-gadîru racʿan, gloss:gölete rec denmiştir, source:"ر ج ع,B006"}. Rab kelimesinin ailesinde de toplanmış bol su vardır: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabab el-mâ'u'l-kesîr, gloss:rabab, toplandığı için böyle denen bol sudur, source:"ر ب ب,B013"}. Böylece on beşinci ayetteki "vazgeçmezse" ifadesinin yanında, suyun durulduğu yerde durmaması da duyulur. Sekizinci ayet suyun varacağı yeri söyler. Kurân bunu ilahî adla birleştiren bir kardeş ayet içerir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Bu yapı sekizinci ayetle aynıdır; tek fark, dönüş yerine varış kökünün kullanılmasıdır.

Kaynaklar: 96:3 ٱلْأَكْرَمُ ك ر م B002; 96:1 رَبِّكَ ر ب ب B008; 96:1 بِٱسْمِ و س م B003; 96:13 وَتَوَلَّىٰٓ و ل ي B010; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B006; 96:17 نَادِيَهُۥ ن د و B004; 96:16 خَاطِئَةٍ خ ط ء B003; 96:6 لَيَطْغَىٰٓ ط غ ي B002; 96:6 لَيَطْغَىٰٓ ط غ ي B001; 96:15 يَنتَهِ ن ه ي B004; 96:8 رَبِّكَ ر ب ب B013

## Yol: doğru yolda olmak, sapmak, dönmek, yaklaşmak

Bir yolcu yoldadır. Hedefi ıskalayabilir, yönünden sapabilir ya da sırtını dönüp kaçabilir. Sonunda herkes başladığı yere döner ve yolun bir varış noktası vardır. On birinci ayetin {ar:عَلَى ٱلْهُدَىٰٓ, tr:ʿale'l-hudâ, gloss:doğru yol üzerinde, source:96:11} ifadesi yolcuyu yolun üzerinde gösterir: {ar:هديته الطريق والبيت هداية أي عرفته, tr:hedeytuhu't-tarîk, gloss:ona yolu ve evi gösterdim, yani tanıttım, source:"ه د ي,B001"}; {ar:الهداية دلالة بلطف, tr:el-hidâye delâletun bi lutf, gloss:hidayet, incelikle yol göstermektir, source:"ه د ي,B001"}. Kök sakin bir yürüyüşü de adlandırır: {ar:لم يسرع إسراع المنهزم ولكن على سكون وهدي حسن, tr:lem yusriʿ isrâʿa'l-munhezim, gloss:bozguna uğrayan gibi koşmadı, sükûnet ve güzel bir yürüyüşle gitti, source:"ه د ي,B010"}. Kurân yolcuları karşılaştırır: {ar:أَفَمَن يَمْشِى مُكِبًّا عَلَىٰ وَجْهِهِۦٓ أَهْدَىٰٓ أَمَّن يَمْشِى سَوِيًّا عَلَىٰ صِرَٰطٍ مُّسْتَقِيمٍ, tr:e fe men yemşî mukibben ʿalâ vechihî ehdâ em men yemşî seviyyen ʿalâ sırâtın mustakîm, gloss:yüzüstü kapanarak yürüyen mi daha doğru yoldadır, yoksa dosdoğru bir yolda dimdik yürüyen mi, source:67:22}. Bu ayette yüz, yolun karşısında bir yürüyüş biçimi olarak geçer; bu da perçem sahnesine yakındır.

On altıncı ayetin günahkâr kelimesi yönden sapmaktır: {ar:الخطأ العدول عن الجهة, tr:el-hata'u'l-ʿudûlu ʿani'l-cihe, gloss:hata yönden sapmaktır, source:"خ ط ء,B001"}. On üçüncü ayetin yüz çevirme fiili, bedenle ya da dinlememekle sırt dönmektir: {ar:التولي قد يكون بالجسم وقد يكون بترك الإصغاء والائتمار, tr:et-tevellî kad yekûnu bi'l-cism, gloss:yüz çevirmek bedenle de olur, dinlememek ve emre uymamakla da, source:"و ل ي,B007"}. Aynı kök kesintisiz yakınlığı da adlandırır: {ar:الولي القرب والدنو, tr:el-velyu'l-kurbu ve'd-dunuvv, gloss:vely yakınlık ve yaklaşmaktır, source:"و ل ي,B001"}. Böylece yüz çevirmek, yakınlığın tersine çevrilmiş halidir. Yalanlama fiilinin ailesinde saldırıda duraksamak da vardır: {ar:حمل فلان ثم كذب أي لم يصدق في الحملة, tr:hamele fulânun summe kezeb, gloss:falan saldırdı, sonra geri durdu, yani saldırısında sözünü tutmadı, source:"ك ذ ب,B004"}.

Sekizinci ayetin dönüşü başlangıca dönüştür: {ar:الرجوع العود إلى ما كان منه البدء, tr:er-rucûʿu'l-ʿavdu ilâ mâ kâne minhu'l-bed', gloss:dönüş, başlangıcın olduğu yere geri gelmektir, source:"ر ج ع,B001"}. Bu başlangıç, ilk iki ayetin yaratmasıdır. Kurân dönüşü yaratılışın başlangıcına bağlar: {ar:إِلَيْهِ مَرْجِعُكُمْ جَمِيعًا, tr:ileyhi merciʿukum cemîʿâ, gloss:hepinizin dönüşü O'nadır, source:10:4}, {ar:إِنَّهُۥ يَبْدَؤُا۟ ٱلْخَلْقَ ثُمَّ يُعِيدُهُۥ, tr:innehû yebde'u'l-halka summe yuʿîduh, gloss:O yaratmayı başlatır, sonra onu geri getirir, source:10:4}; {ar:كَمَا بَدَأَكُمْ تَعُودُونَ, tr:kemâ bede'ekum teʿûdûn, gloss:sizi başlattığı gibi döneceksiniz, source:7:29}. İnsanın yolu da Rab'be doğru bir uğraş olarak tanımlanır: {ar:يَٰٓأَيُّهَا ٱلْإِنسَٰنُ إِنَّكَ كَادِحٌ إِلَىٰ رَبِّكَ كَدْحًا فَمُلَٰقِيهِ, tr:yâ eyyuhe'l-insânu inneke kâdihun ilâ rabbike kedhan fe mulâkîh, gloss:ey insan, sen Rabbine doğru zahmetle çabalıyorsun ve O'na kavuşacaksın, source:84:6}. Dönmeyeceğini sanan kişi de anlatılır: {ar:إِنَّهُۥ ظَنَّ أَن لَّن يَحُورَ, tr:innehû zanne en len yahûr, gloss:o asla geri dönmeyeceğini sanmıştı, source:84:14}. Yedinci ayetin yeterlilik kökü bu sanıyı yere yerleşmekle de anlatır: {ar:غني القوم في دارهم أقاموا, tr:ganiye'l-kavmu fî dârihim, gloss:topluluk yurdunda yerleşip kaldı, source:"غ ن ي,B004"}. Dönüş kelimesinin ailesinde günahtan dönmek de vardır: {ar:يرجعون عن الذنب, tr:yarciʿûne ʿani'z-zenb, gloss:günahtan dönerler, source:"ر ج ع,B003"}. Bu, on beşinci ayetteki "vazgeçmezse" şartının açık bıraktığı yoldur.

Yolun bir son noktası vardır: {ar:النهاية الغاية حيث ينتهي إليه الشيء, tr:en-nihâyetu'l-gâye, gloss:nihâye, bir şeyin vardığı son noktadır, source:"ن ه ي,B002"}. Son ayetin emri ise yaklaşmaktır: {ar:القرب نقيض البعد والتقرب التدني إلى شيء والاقتراب الدنو, tr:el-kurbu nakîdu'l-buʿd, gloss:yakınlık uzaklığın zıddıdır; yaklaşmak bir şeye doğru alçalıp gelmektir, source:"ق ر ب,B001"}. On ikinci ayetin sakınma kökü yolda dikkatle yürüyen atı da adlandırır: {ar:فرس واق إذا كان يهاب المشي من وجع يجده في حافره, tr:ferasun vâk, gloss:toynağındaki ağrıdan ötürü yürümekten çekinen at, source:"و ق ي,B003"}. Sure böylece yolda olmayı, sapmayı, sırt dönmeyi ve sonunda yaklaşmayı tek bir yol üzerinde sıralar.

Kaynaklar: 96:11 ٱلْهُدَىٰٓ ه د ي B001; 96:11 ٱلْهُدَىٰٓ ه د ي B010; 96:16 خَاطِئَةٍ خ ط ء B001; 96:13 وَتَوَلَّىٰٓ و ل ي B007; 96:13 وَتَوَلَّىٰٓ و ل ي B001; 96:13 كَذَّبَ ك ذ ب B004; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B001; 96:8 ٱلرُّجْعَىٰٓ ر ج ع B003; 96:7 ٱسْتَغْنَىٰٓ غ ن ي B004; 96:15 يَنتَهِ ن ه ي B002; 96:19 وَٱقْتَرِب ق ر ب B001; 96:12 بِٱلتَّقْوَىٰٓ و ق ي B003

## Buluşmalar

İmgeler en açık şekilde baş sahnesinde buluşur. On beşinci ayetin fiili hem perçemden tutmak hem de yüzü karartmaktır. Böylece başın önü, avın yakalandığı yer, huysuz hayvanın tutulduğu yer ve ateşin yaladığı deri aynı noktada birleşir. Aynı alın son ayette yere konur ve secde izini taşır. İşaret imgesi buraya da uzanır: bir alın kararmış bir lekeyle işaretlenir, öteki secdenin iziyle. Kurân her iki tarafı da yüzlerindeki işaretle tanıtır: biri {ar:مِّنْ أَثَرِ ٱلسُّجُودِ, tr:min eseri's-sucûd, gloss:secdenin izinden, source:48:29}, öteki {ar:سَنَسِمُهُۥ عَلَى ٱلْخُرْطُومِ, tr:senesimuhû ʿale'l-hurtûm, gloss:onu burnunun üstünden damgalayacağız, source:68:16}. Sure ad ile başlar ve iki işaretli alınla biter.

Göz ile yeterlilik imgeleri yedinci ayette buluşur. Kendini aynada gören adam ile süse ihtiyaç duymayan güzel kadın aynı kelime çiftinde birleşir: kendini görmek ve yeterli saymak. Su imgesi de buna bağlanır. Azan insan ölçüsünü aşan bir taşkın gibidir; on beşinci ayette durması istenir. Kökün göletteki duruluşu adlandırdığı hatırlanırsa, sekizinci ayet bu suyun nereye varacağını söyler. Kurân'ın varış ayeti bu iki imgeyi aynı yapıda birleştirir: {ar:وَأَنَّ إِلَىٰ رَبِّكَ ٱلْمُنتَهَىٰ, tr:ve enne ilâ rabbike'l-muntehâ, gloss:varış Rabbinedir, source:53:42}. Yol imgesi de bu dönüşe katılır, çünkü dönüş başlangıca dönmektir ve bu başlangıç rahimdeki ilk tutunuştur.

Rahim ile okuma, surenin ilk kelimesinde buluşur. Okumanın kökü hem rahmin bir şeyi toplayıp tutmasını hem de harflerin toplanmasını adlandırır. Pıhtıyı tutan kökle sözü toplayan kök aynıdır. İnsanın yaratılışı ve öğretilmesi bu yüzden aynı işin iki yüzü olarak duyulur. Kurân'daki benzer sıra da bunu destekler: Kurân'ı öğretmek, insanı yaratmak ve ona açıklamayı öğretmek. Okuma ile secde de buluşur: okuyucu aynı zamanda kulluk edendir ve sure, ilk emri okumak, son emri secde etmek olan bir eğri çizer. Kurân bu ikisini, okunduğunda secde edenler ile etmeyenler üzerinden birleştirir.

Ateş ile çağrı imgeleri onuncu, on yedinci ve on sekizinci ayetlerde buluşur. Namaz hem çağrıdır hem de kökü ateşe girmeyi adlandırır. Adam meclisini çağırır, Allah ateşe iten bekçileri çağırır ve kul yakın meclise çağrılır. Ateşin kendisinin de çağırdığı söylenir: {ar:تَدْعُوا۟ مَنْ أَدْبَرَ وَتَوَلَّىٰ, tr:tedʿû men edbera ve tevellâ, gloss:arkasını dönüp yüz çevireni çağırır, source:70:17}. Bu yüz çevirme on üçüncü ayetin fiilidir.

İtaat ile hayvan imgeleri son ayette buluşur. Rab, itaat edilen efendidir; dizgine uyan at da itaatin bir figürüdür. Kul bu yüzden kendini rab ilan eden birine boyun eğmez, yakında tutulan ve değer gören at gibi yaklaşır. Yaratma ile uydurma da on altıncı ayette buluşur. Gerçek ölçüyle yaratan Rab'bin karşısında, yalanı içinde ölçen yalancı perçem durur.

Bu buluşmalar surenin hareketini taşır. Sure, rahimde toplanan ve tutunan bir varlıkla başlar; bu varlık sözü toplamayı ve kalemle yazmayı öğrenir. Sonra kendini aynada yeterli görür, taşkın su gibi ölçüsünü aşar, başını kaldırır ve namaz kılan kulu engellemeye çalışır. Dönüş ayeti ve Allah'ın görmesi bu yükselişin önüne bir sınır koyar. Yasaklayan perçeminden yakalanır, meclisi yerine bekçiler gelir. Kul ise yüz çevirmeden, başını yere koyarak, çağrılmış olduğu yakınlığa yürür.

