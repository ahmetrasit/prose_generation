Focus: 113:2. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/113_2/D.r13/context.md =====
# 113:2 — focus

مِن شَرِّ مَا خَلَقَ

Anchor translation (canonical reading, reference only):

yarattığı şeylerin kötülüğünden;

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | مِن | مِن |  | P |
| 2 | شَرِّ | شَرّ | ش ر ر | N |
| 3 | مَا | مَا |  | REL |
| 4 | خَلَقَ | خَلَقَ | خ ل ق | V |


# Fatiha (recited in every salah)
- 1:1 بِسْمِ ٱللَّهِ ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:2 ٱلْحَمْدُ لِلَّهِ رَبِّ ٱلْعَٰلَمِينَ
- 1:3 ٱلرَّحْمَٰنِ ٱلرَّحِيمِ
- 1:4 مَٰلِكِ يَوْمِ ٱلدِّينِ
- 1:5 إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ
- 1:6 ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ
- 1:7 صِرَٰطَ ٱلَّذِينَ أَنْعَمْتَ عَلَيْهِمْ غَيْرِ ٱلْمَغْضُوبِ عَلَيْهِمْ وَلَا ٱلضَّآلِّينَ

# Surah 113 — full text (context; no pericope)

- 113:1 قُلْ أَعُوذُ بِرَبِّ ٱلْفَلَقِ
- 113:2 ◀ focus مِن شَرِّ مَا خَلَقَ
- 113:3 وَمِن شَرِّ غَاسِقٍ إِذَا وَقَبَ
- 113:4 وَمِن شَرِّ ٱلنَّفَّٰثَٰتِ فِى ٱلْعُقَدِ
- 113:5 وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ


===== _commentary/v16/work/113_2/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ش ر ر (root_000787) — identity root of شَرِّ (w2)

- **B001** iyinin karşıtı olan kötülük — kötülük; iyinin karşıtı · kötülük etme veya kötü olma durumu · kötülüğü çok olan adam · kötü kimseler · birini kötülüğe bağladı; onu kötü saydı · kusur veya hoş karşılanmayan şey
  الشَّرّ خلاف الخير (maqayis;jamhara)؛ الشر السوء (ayn)؛ الشر نقيض الخير (sihah)؛ الشر الذي يرغب عنه الكل (mufradat)؛ رجل شرير كثير الشر (maqayis;jamhara;sihah;mufradat)؛ أشررت فلانا إذا نسبته إلى الشر (maqayis;sihah;mufradat)؛ الشُّرّ العيب (sihah)؛ الشر بالضم خص بالمكروه (mufradat)
- **B002** güneşe serip kurutmak — güneşe serip kuruttu · güneşte kuruması için serdi · kurutulacak şeylerin serildiği yaygı · süt ürünü veya tahıl kurutma yaygısı · kurutma yaygıları veya kurutulmuş et parçaları
  الشر بسطك الشيء في الشمس (maqayis;ayn)؛ شررت اللحم والثوب وأشررته إذا بسطته ليجف (jamhara)؛ شررت الثوب بسطته في الشمس (sihah)؛ شررت الأقط أشره إذا جعلته على خصفة ليجف (sihah)؛ الإشرارة ما يبسط عليه الشيء (maqayis)؛ الإشرار ما يبسط عليه الأقط والبر ليجف (ayn)؛ الأشارير قطع قديد (sihah)
- **B003** kıvılcım — ateşten sıçrayan kıvılcımlar · kıvılcımlar topluluğu · tek kıvılcım · tek kıvılcım
  الشرارة والجمع الشرار (maqayis)؛ الشرر ما تطاير من النار الواحدة شررة (maqayis)؛ الشرارة والشرر ما تطاير من النار (ayn)؛ شرار النار فيقال شررة وشرارة (jamhara)؛ الشرارة واحدة الشرار وهو ما يتطاير من النار وكذلك الشرر (sihah)؛ شرار النار ما تطاير منها (mufradat)
- **B004** kesip parçalamak — bir şeyi kesip yardı · kesip parçalama; ısırılan şeyi ağızdan silkeleyip çıkarma
  شرشر الشيء إذا قطعه (maqayis)؛ الشرشرة أن تنفض الشيء من فيك بعد عضك إياه (maqayis)؛ شرشره أي قطع شراشره (ayn)؛ شرشرة الشيء تشقيقه وتقطيعه (sihah)
- **B005** yağı damlayan pişmiş et [kalıp] — yağı damlayan pişmiş et · yağı damlayan pişmiş et
  الشواء الشرشار الذي يتقاطر دسمه (maqayis)؛ شواء شرشر يتقاطر دسمه (sihah)
- **B006** kuyrukların sarkan uçları veya ağırlıklar — kuyrukların sarkan ve salınan uçları · ağırlıklar
  شراشر الأذناب ذباذبها (maqayis;sihah)؛ الشراشر الأثقال الواحدة شرشرة (sihah)
- **B007** kendini bütün isteğiyle vermek — kendini, isteğini ve bütün ilgisini ona verdi
  ألقى عليه شراشره إذا ألقى عليه نفسه حرصا ومحبة (maqayis)؛ ألقى علي شراشره أي ألقى علي نفسه حرصا (ayn)؛ ألقى عليه شراشره أي نفسه حرصا ومحبة (sihah)؛ جمع ما انتشر من هممه لهذا الشيء وشغل همومه كلها به (maqayis)
- **B008** görünür kılmak — 
  أشررت الشيء إذا أبرزته وأظهرته (maqayis)؛ أشررت الشيء أظهرته (sihah)؛ يحتمل أنها نسبت الأصابع إلى الشر بالإشارة إليه (mufradat)
- **B009** yüz çevresinde dolaşan ısırmayan sivrisinek benzeri böcek — yüz çevresinde dolaşan, ısırmayan sivrisinek benzeri böcekler · bu türden tek böcek
  الشران شيء تسميه العرب الأذى شبه البعوض يغشى وجه الإنسان لا يعض الواحدة شرانة (ayn)؛ الشران شبيه بالبعوض يغشى وجه الإنسان ولا يعض وربما سموه الأذى (sihah)
- **B010** gençlik canlılığı ve atılganlığı [kalıp] — gençliğin canlılığı, güçlü isteği ve atılganlığı
  شرة الشباب نشاطه ولهذا باب تراه (jamhara)؛ شرة الشباب حرصه ونشاطه (sihah)
- **B011** çekişme — çekişme; ağız dalaşı
  المشارة المخاصمة (sihah)
- **B012** adı belirtilen bir bitki — kaynakta adı verilen bir bitki
  الشرشر نبت يقال له الشرشر بالكسر (sihah)

## خ ل ق (root_000434) — identity root of خَلَقَ (w4)

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

## ECHO ش ر ي (root_000792) — for شَرِّ (w2): withheld observed target; not identity

- **B001** bedel karşılığında alıp satma — satmak veya bedelini verip almak · satın almak · alış ve satış
  شريت الشيء واشتريته إذا أخذته من صاحبه بثمنه (maqayis); شرى يشري شرى وشراء وهو شار إذا باع (ayn); شريت الشيء إذا بعته وإذا اشتريته أيضا (sihah); الشراء والبيع يتلازمان (mufradat); شريت بمعنى بعت وشريت أي اشتريت (tahdhib)
- **B002** eş ve denk — benzeri ve dengi · eş ve benzer
  هذا شروى هذا أي مثله (maqayis); شرواها أي مثلها (maqayis); شروى الشيء مثله (sihah); هذا شرواه وشرية أي مثله (tahdhib)
- **B003** bir şeyin yanları ve uçları [kalıp] — bir şeyin yanları ve uçları · büyük nehrin yanı
  أشراء الشيء نواحيه الواحد شرى (maqayis); أشراء الحرم نواحيه الواحد شرى (sihah); أشراء الحرم نواحيه وشرى الفرات ناحيته (tahdhib)
- **B004** acı elma bitkisi veya çekirdekten yetişen palmiye — acı elma bitkisi veya bu bitkinin topluluğu · çekirdekten yetişen palmiye ağacı
  الشَّرى يقال إنه الحنظل (maqayis); الشرية النخلة التي تنبت من النواة (maqayis); الشري بالتسكين الحنظل (sihah); الشرى أيضا شجر الحنظل (sihah); الحنظل هو الشري واحدته شرية (tahdhib)
- **B005** çalılık ve aslanlarıyla tanınan yer — çalılığı ve aslanı bol yer veya yol · çalılık bölgenin aslanları
  الشرى موضع كثير الدغل والأسد (maqayis); الشرى طريق في سلمى كثير الأسد (sihah); ما هم إلا أسود الشرى (tahdhib); شرى مأسدة بعينها وبه غياض وآجام (tahdhib)
- **B006** yaylık ağaç veya atardamar — yay yapımında kullanılan ağaç veya odun · atan veya ince beden damarları
  الشريان من شجر القسى (maqayis); الشريان شجر يتخذ منه القسى (sihah); الشريان واحد الشرايين وهي العروق النابضة (sihah); الشريان من الشجر الذي يتخذ منه القسي (tahdhib); الشريانات عروق رقاق في جسد الإنسان (tahdhib)
- **B007** şimşeğin yayılıp art arda parlaması [kalıp] — şimşek buluta yayıldı veya art arda parladı · şimşek art arda parladı
  شرى البرق إذا استطار (maqayis); شري البرق في السحاب يشرى شرى إذا تفرق فيه (ayn); شرى البرق إذا كثر لمعانه (sihah); شري البرق إذا تفرق في وجه الغيم (tahdhib); شري البرق إذا تتابع لمعانه واستشرى مثله (tahdhib)
- **B008** taşkın biçimde sürme, yinelenme veya büyüme — öfkesinden çılgına döndü · bir işte inatla diretti ve ileri gitti · karşılıklı inatlaşma ve çekişme · yolunda hızlandı veya durmadan ilerledi · dişi devenin dizgini durmadan çırpındı · gözyaşları durmadan aktı · aralarındaki işler büyüyüp ağırlaştı
  شرى الرجل إذا استطير غضبا (maqayis); شرى البعير في سيره إذا أسرع (maqayis); استشرى الرجل إذا لج في الأمر (maqayis); شرى زمام الناقة إذا كثر اضطرابه (maqayis); شري فلان غضبا إذا استطار غضبا (sihah); استشرى أي لج في سننه (sihah); استشرى فلان في الغي إذا لج فيه (tahdhib); المشاراة الملاجة (tahdhib); شريت عينه بالدمع أي لجت وتابعت الهملان (tahdhib); استشرت أمور بينهم تفاقمت وعظمت (tahdhib); أشريته به فشري مثل أغريته به فغري (tahdhib)
- **B009** yakıcı küçük kırmızı deri kabarcıkları — yakıcı küçük kırmızı deri kabarcıklarıyla görülen hastalık · derisinde yakıcı küçük kabarcıklar çıktı
  شري جلده من الشرى وهي خراج صغار لها لذع شديد (sihah); الشري داء يأخذ في الرجل أحمر كهيئة الدراهم (tahdhib); شرى جلده شرى وهو شر (tahdhib)
- **B010** havuzu veya yemek kabını doldurmak [kalıp] — havuzu veya büyük yemek kabını doldurmak
  أشريت الحوض وأشريت الجفنة إذا ملأتهما (sihah); أشرى حوضه ملأه وأشرى جفانه إذا ملأها للضيفان (tahdhib)
- **B011** kendini Tanrı uğruna sattığını söyleyen topluluk — kendilerini Tanrı uğruna sattıklarını söyleyen ayrılıkçı topluluk · bu topluluğun bir üyesi · bu topluluğa katılmak
  الشراة الخوارج الواحد شار سموا بذلك لقولهم إنا شرينا أنفسنا في طاعة الله (sihah); الشراة الخوارج سموا أنفسهم شراة لأنهم أرادوا أنهم باعوا أنفسهم لله (tahdhib); يسمى الخوارج بالشراة متأولين فيه ومن الناس من يشري نفسه (mufradat)
- **B012** Tanrı seni sıkıntıya ve aşağılanmaya uğratsın [kalıp] — Tanrı seni sıkıntıya ve aşağılanmaya uğratsın
  لحاه الله وشراه (tahdhib); شراه الله وعظاه وأورمه وأرغمه (tahdhib)

===== _commentary/v16/out/s113/images.r13.map3.nochannels.hftbundle.tool.tool/images.md (only the images that cite 113:2, and ## Buluşmalar) =====
## Yarılıp dışarı çıkarılan: tohum, sabah, bütün yaratılmışlar

Felak yalnızca ayırmaz; ayırdığı şeyin içinden bir şey çıkarır ve onu görünür kılar. Tohum yarılır, filizi dışarı çıkar: {ar:والله يفلق الحب فينفلق عن نباته, tr:vallâhu yefliku'l-habbe fe-yenfeliku an nebâtih, gloss:Allah taneyi yarar, tane de yarılıp bitkisini çıkarır, source:"ف ل ق,B003"}. Aynı fiil eşya ölçeğinde de söylenir; çekirdeğinden kendiliğinden ayrılan bir şeftali türünün adı bu köktendir: {ar:الفليق ضرب من الخوخ يتفلق عن نواه, tr:el-felîku darbun mine'l-ḣavḣ yetefellaku an nevâh, gloss:felîk, çekirdeğinden yarılıp ayrılan bir şeftali türüdür, source:"ف ل ق,B001"}. Bu işlem bütün yaratılmışlara genişletilir: {ar:الفلق الخلق كله كأنه شيء فلق عنه شيء حتى أبرز وأظهر, tr:el-felaku'l-ḣalku kulluh, ke-ennehû şey'un fulika anhu şey'un hattâ ubrize ve uzhir, gloss:felak bütün yaratılmışlardır; her biri, kendisinden bir şeyin yarılıp ayrıldığı, sonunda dışarı çıkarılıp gösterildiği bir şey gibidir, source:"ف ل ق,B003"}.

Bu söz ilk ayetin sıfatını ikinci ayete bağlar: {ar:مِن شَرِّ مَا خَلَقَ, tr:min şerri mâ ḣalak, gloss:yarattığı şeylerin şerrinden, source:113:2}. Halk kökü yoktan var etmeyi de, bir şeyden bir şey var etmeyi de anlatır: {ar:ويستعمل في إيجاد الشيء من الشيء, tr:ve yustamelu fî îcâdi'ş-şey'i mine'ş-şey', gloss:bir şeyi bir şeyden var etmek için de kullanılır, source:"خ ل ق,B002"}. Biçimi ortaya çıkmış olanla henüz biçimlenmemiş olan da bu kökle ayrılır: {ar:مخلقة قد بدا خلقها وغير مخلقة لم تصور, tr:muḣallaka kad bedâ ḣalkuhâ ve ğayru muḣallaka lem tusavver, gloss:yaratılışı belirmiş olan ve henüz biçim almamış olan, source:"خ ل ق,B003"}. Böylece ikinci ayetin "yarattığı şeyler"i, ilk ayetin yarıp çıkardığı şeyler olarak duyulur: bir örtüden, bir kabuktan, bir karanlıktan ayrılıp gün ışığına konmuş her şey.

İkinci ayetin ilk kelimesi de aynı hareketin yanında durur. Şer kelimesi ayette kötülük ve zarardır; ama aynı kökün bir dalı "çıkarıp göstermek" demektir: {ar:أشررت الشيء إذا أبرزته وأظهرته, tr:eşrartu'ş-şey'e izâ ebraztuhû ve azhartuh, gloss:bir şeyi dışarı çıkarıp gösterdiğimde "eşrartu" derim, source:"ش ر ر,B008"}. Bu tanım, felakın bütün yaratılmışlara genişletildiği tanımla aynı iki fiille kurulur. İki ayrı kökün aynı işleme yaslanmasıdır bu; bir kök birliği değildir. Ama surenin sırasında anlamlı bir yakınlık kurar: Rab yarar ve gösterir, yarattığı şey dışarı çıkar, şer de o çıkmış şeyden çıkar. Sade bir anlam "yarattıklarının kötülüğünden" der ve kötülüğü yaratılmışların yanına konmuş ayrı bir şey gibi bırakır. Bu imgede zarar, açığa çıkarılmış olanın içinden açığa çıkar; sığınılan da her şeyi açığa çıkaran Rabdir. Kötülüğün kaynağı O'nun yarıp gösterdiği alanın içindedir, O'nun elinin dışında değildir.

Rab kelimesi bu çıkarılışın devamını taşır: {ar:التربية، وهو إنشاء الشيء حالا فحالا إلى حد التمام, tr:et-terbiye ve huve inşâu'ş-şey'i hâlen fe-hâlen ilâ haddi't-temâm, gloss:terbiye, bir şeyi hâlden hâle geçirerek tamamlanma sınırına kadar büyütmektir, source:"ر ب ب,B002"}. Yarılıp çıkarılan şey orada bırakılmaz; aşama aşama büyütülür. Emredilen söz de aynı hareketin bir örneğidir. Kavl, dil ile dışarı çıkarılmış harflerdir: {ar:المركب من الحروف المبرز بالنطق, tr:el-murekkebu mine'l-hurûfi'l-mubrazu bi'n-nutk, gloss:harflerden kurulup konuşmayla dışarı çıkarılan, source:"ق و ل,B001"}; dışarı çıkmadan önce de içeride tutulan bir sözdür: {ar:المتصور في النفس قبل الإبراز باللفظ قول, tr:el-mutesavveru fi'n-nefsi kable'l-ibrâzi bi'l-lafzı kavl, gloss:lafızla dışarı çıkarılmadan önce içte tasarlanan da söz sayılır, source:"ق و ل,B012"}. Böylece ilk kelime, {ar:قُلْ, tr:kul, gloss:de, source:113:1}, okuyanın kendi içindekini dışarı çıkarmasıdır: Rab yaratılmışları yarıp gösterir, kul da sığınmasını söze döküp ortaya koyar.

Kur'an bu çıkarılışı Allah'ın kendi anlatımıyla verir: {ar:إِنَّ ٱللَّهَ فَالِقُ ٱلْحَبِّ وَٱلنَّوَىٰ ۖ يُخْرِجُ ٱلْحَىَّ مِنَ ٱلْمَيِّتِ, tr:innallâhe fâliku'l-habbi ve'n-nevâ, yuḣricu'l-hayye mine'l-meyyit, gloss:Allah taneyi ve çekirdeği yarandır; diriyi ölüden çıkarır, source:6:95}. Yarma ile çıkarma aynı cümlede yan yanadır ve hemen ardından sabahı yaran gelir {source:6:96}. Tohumdan sabaha, sabahtan bütün diriye uzanan bu sıra, surenin ilk iki ayetini birbirine bağlayan hareketi Kur'an'ın içinde gösterir. İnsanın yiyeceğine bakmaya çağrıldığı yerde Allah aynı sahneyi adım adım anlatır: {ar:أَنَّا صَبَبْنَا ٱلْمَآءَ صَبًّۭا, tr:ennâ sabebne'l-mâe sabbâ, gloss:suyu bolca döktük, source:80:25}, {ar:ثُمَّ شَقَقْنَا ٱلْأَرْضَ شَقًّۭا, tr:summe şakakne'l-arda şakkâ, gloss:sonra toprağı iyice yardık, source:80:26}, {ar:فَأَنۢبَتْنَا فِيهَا حَبًّۭا, tr:fe-enbetnâ fîhâ habbâ, gloss:orada tane bitirdik, source:80:27}. Bir yeminde toprak çatlamasıyla anılır: {ar:وَٱلْأَرْضِ ذَاتِ ٱلصَّدْعِ, tr:ve'l-ardı zâti's-sad', gloss:çatlayan toprağa andolsun, source:86:12}. Allah İsrailoğullarına katılaşan kalplerini anlatırken taşın bile yarılıp su verdiğini söyler: {ar:وَإِنَّ مِنْهَا لَمَا يَشَّقَّقُ فَيَخْرُجُ مِنْهُ ٱلْمَآءُ, tr:ve inne minhâ le-mâ yeşşakkaku fe-yaḣrucu minhu'l-mâ', gloss:taşların kimi de yarılır, içinden su çıkar, source:2:74}. Yarılıp bir şey vermeyen, taştan katı olan kalptir. Diriltilmekten şüphe edenlere hitap eden ayette Allah biçimlenmiş cenini ve dışarı çıkarılan çocuğu aynı akışta anar: {ar:ثُمَّ مِن مُّضْغَةٍۢ مُّخَلَّقَةٍۢ وَغَيْرِ مُخَلَّقَةٍۢ, tr:summe min mudğatin muḣallakatin ve ğayri muḣallaka, gloss:sonra biçimlenmiş ve biçimlenmemiş bir et parçasından, source:22:5}, {ar:ثُمَّ نُخْرِجُكُمْ طِفْلًۭا, tr:summe nuḣricukum tıflâ, gloss:sonra sizi bir çocuk olarak çıkarırız, source:22:5}. Aynı ayetin sonunda su inince toprak kıpırdar ve kabarır: {ar:ٱهْتَزَّتْ وَرَبَتْ وَأَنۢبَتَتْ, tr:ihtezzet ve rabet ve enbetet, gloss:kıpırdadı, kabardı ve bitirdi, source:22:5}. Buradaki "rabet" fiili rab kelimesiyle aynı kökten değildir; ses benzerliği bir kök birliği kurmaz, yalnızca büyütmenin iki ayrı adının aynı sahnede buluşmasıdır.

Kaynaklar: 113:1 ٱلْفَلَقِ ف ل ق B003; 113:1 ٱلْفَلَقِ ف ل ق B001; 113:2 خَلَقَ خ ل ق B002; 113:2 خَلَقَ خ ل ق B003; 113:2 شَرِّ ش ر ر B008; 113:1 بِرَبِّ ر ب ب B002; 113:1 قُلْ ق و ل B001; 113:1 قُلْ ق و ل B012

## Bulut, yağmur ve kaya çukuru

Surenin kelimeleri, kök ailelerinden dinlendiğinde, bulutla başlayıp kayadaki bir çukurla biten bütün bir yağmur sahnesini taşır. Rab kelimesinin kökü alçakta asılı duran bulutun adıdır: {ar:الرباب: السحاب، سمي بذلك لأنه يرب النبات, tr:er-rabâb es-sehâb, summiye bi-zâlike li-ennehû yerubbu'n-nebât, gloss:rabâb buluttur; bitkiyi büyüttüğü için bu adı almıştır, source:"ر ب ب,B008"}; büyük bulutun altında sarkan, ak ya da kara bir buluttur bu: {ar:السحاب المتعلق دون السحاب يكون أبيض ويكون أسود, tr:es-sehâbu'l-muteallaku dûne's-sehâb yekûnu ebyada ve yekûnu esved, gloss:bulutun altında asılı duran bulut; ak da olur kara da, source:"ر ب ب,B008"}. Bulut yerinde durur: {ar:أربت السحابة: دامت, tr:erabbeti's-sehâbe: dâmet, gloss:bulut kalıcı oldu, source:"ر ب ب,B007"}. Halk kökü onun düzgünce yayılışını adlandırır: {ar:اخلولق السحاب استوى, tr:iḣlevlaka's-sehâbu'stevâ, gloss:bulut düzgünce yayıldı, source:"خ ل ق,B008"}. Ukad kökü yığılışını: {ar:تعقد السحاب إذا صار كأنه عقد مضروب مبني, tr:teakkade's-sehâbu izâ sâra ke-ennehû akdun madrûbun mebnî, gloss:bulut, kurulmuş bir kemer gibi olduğunda "teakkade" denir, source:"ع ق د,B008"}. Sonra felak kökü bulutun yağmurla yarılmasını söyler: {ar:فلق الأرض بالنبات والسحاب بالمطر, tr:felaka'l-arda bi'n-nebâti ve's-sehâbe bi'l-matar, gloss:toprağı bitkiyle, bulutu yağmurla yardı, source:"ف ل ق,B003"}. Gök çiseler ve gāsık "akan" olur: {ar:غسقت السماء أرشت, tr:ğasakati's-semâu erasşet, gloss:gök çiseledi, source:"غ س ق,B004"}, {ar:الغاسق بمعنى السائل, tr:el-ğāsiku bi-ma'ne's-sâil, gloss:gāsık, akan anlamındadır, source:"غ س ق,B004"}.

Su aşağı iner. Felak kökü iki tepe arasındaki alçak yerin de adıdır: {ar:الفلق المطمئن من الأرض بين الربوتين, tr:el-felaku'l-mutmainnu mine'l-ardı beyne'r-rabveteyn, gloss:felak, iki tümsek arasındaki çukur yerdir, source:"ف ل ق,B004"}. Su orada toplanır, dağdaki bir oyuğa dolar: {ar:الوقب في الجبل نقرة يجتمع فيها الماء, tr:el-vakbu fi'l-cebel nukratun yectemiu fîhe'l-mâ', gloss:vakb, dağda suyun toplandığı oyuktur, source:"و ق ب,B001"}. Vekab fiili de bu oyuğa girmektir: {ar:وقب الشيء دخل في وقبة, tr:vekabe'ş-şey'u dehale fî vakbe, gloss:şey bir oyuğa girdi, source:"و ق ب,B002"}. İkinci ayetin halk kökü aynı oyuğu neredeyse aynı sözle adlandırır: {ar:الخليقة نقر في صخرة يجتمع فيه ماء السماء, tr:el-ḣalîka nakrun fî sahratin yectemiu fîhi mâu's-semâ', gloss:halîka, kayada gök suyunun toplandığı oyuktur, source:"خ ل ق,B011"}; o oyukların bulunduğu kaya da bu kökle düzdür: {ar:صخرة خلقاء أي ملساء, tr:sahratun ḣalkâ' ey melsâ', gloss:halkâ kaya, yani pürüzsüz kaya, source:"خ ل ق,B008"}. Rab kökü toplanan bol suyun adıdır: {ar:الربب وهو الماء الكثير سمي بذلك لاجتماعه, tr:er-rabab ve huve'l-mâu'l-kesîr, summiye bi-zâlike li-ictimâih, gloss:rabab bol sudur; toplandığı için bu adı almıştır, source:"ر ب ب,B013"}. Sahnenin sonunda bir ters dönüş de vardır: {ar:إذا أطبق الوادي على قوم فأهلكهم عقد عليهم, tr:izâ etbaka'l-vâdî alâ kavmin fe-ehlekehum akade aleyhim, gloss:vadi bir topluluğun üstüne kapanıp onları helak ettiğinde "akade aleyhim" denir, source:"ع ق د,B016"}.

Bu imge üçüncü ayetin girişini başka bir duyuyla duyurur. Gecenin tepelere "döküldüğü" yukarıda görülmüştü; burada {ar:إِذَا وَقَبَ, tr:izâ vekab, gloss:içeri girdiğinde, source:113:3}, suyun kayadaki oyuğa girip onu doldurması gibi işitilir. Akan şey alçak olan her yeri bulur ve oraya yerleşir. Aynı su toprağı yarıp bitki çıkarır, oyukta toplanıp içilir, ama vadi bir topluluğun üstüne kapandığında öldürür. İkinci ayetin "yarattığı şeylerin şerri" bu sahnede kendi başına kötü bir madde olarak değil, hayat veren bir şeyin yön değiştirmesi olarak görünür. Kur'an da yağmuru bu iki yüzüyle sahneler. "Görmedin mi" diye başlayan bir işaret ayetinde Allah bulutun sürülüp birleştirilişini, yığılışını ve içinden yağmurun çıkışını anlatır: {ar:يُزْجِى سَحَابًۭا ثُمَّ يُؤَلِّفُ بَيْنَهُۥ ثُمَّ يَجْعَلُهُۥ رُكَامًۭا فَتَرَى ٱلْوَدْقَ يَخْرُجُ مِنْ خِلَٰلِهِۦ, tr:yuzcî sehâben summe yuellifu beynehû summe yec'aluhû rukâmen fe-tera'l-vedka yaḣrucu min ḣilâlih, gloss:bir bulutu sürer, sonra parçalarını birleştirir, sonra üst üste yığar; yağmurun aralarından çıktığını görürsün, source:24:43}. Aynı ayet dolunun kime ineceğini de söyler: {ar:فَيُصِيبُ بِهِۦ مَن يَشَآءُ وَيَصْرِفُهُۥ عَن مَّن يَشَآءُ, tr:fe-yusîbu bihî men yeşâu ve yasrifuhû an men yeşâ', gloss:onu dilediğine isabet ettirir, dilediğinden de çevirir, source:24:43}. Sığınmanın işleyişi buradadır: aynı bulutun zararı birine iner, birinden çevrilir; çeviren de bulutun Rabbidir. Hak ile batılın bir örneğinde gökten inen su vadileri ölçüleri kadar doldurur: {ar:أَنزَلَ مِنَ ٱلسَّمَآءِ مَآءًۭ فَسَالَتْ أَوْدِيَةٌۢ بِقَدَرِهَا, tr:enzele mine's-semâi mâen fe-sâlet evdiyetun bi-kaderihâ, gloss:gökten su indirdi, vadiler kendi ölçülerince aktı, source:13:17}; köpük gider, insanlara yarayan yerde kalır. Münafıkları anlatan bir örnekte de yağmur karanlığı birlikte getirir: {ar:أَوْ كَصَيِّبٍۢ مِّنَ ٱلسَّمَآءِ فِيهِ ظُلُمَٰتٌۭ وَرَعْدٌۭ وَبَرْقٌۭ, tr:ev ke-sayyibin mine's-semâi fîhi zulumâtun ve ra'dun ve berk, gloss:ya da gökten boşanan, içinde karanlıklar, gök gürültüsü ve şimşek bulunan bir sağanak gibi, source:2:19}. Gecenin dökülüşü ile yağmurun dökülüşü bu sahnede tek bir gökten iner.

Kaynaklar: 113:1 بِرَبِّ ر ب ب B008; 113:1 بِرَبِّ ر ب ب B007; 113:2 خَلَقَ خ ل ق B008; 113:4 ٱلْعُقَدِ ع ق د B008; 113:1 ٱلْفَلَقِ ف ل ق B003; 113:3 غَاسِقٍ غ س ق B004; 113:1 ٱلْفَلَقِ ف ل ق B004; 113:3 وَقَبَ و ق ب B001; 113:3 وَقَبَ و ق ب B002; 113:2 خَلَقَ خ ل ق B011; 113:2 خَلَقَ خ ل ق B008; 113:1 بِرَبِّ ر ب ب B013; 113:4 ٱلْعُقَدِ ع ق د B016

## Tamamlanan nimet ve gitmesi istenen nimet

Surenin iki ucu aynı şeyin, nimetin etrafında durur. Rab kökü bir nimeti tamamlamayı adlandırır: {ar:رب الرجل النعمة يربها ربا؛ ربابة أيضا إذا تممها, tr:rabbe'r-raculu'n-ni'mete yerubbuhâ rabben ve rabâbeten eyden izâ temmemehâ, gloss:adam nimeti tamamladığında "rabbe" denir, source:"ر ب ب,B002"}; {ar:رب فلان الصنيعة إذا أتمها وأصلحها, tr:rabbe fulânun es-sanîate izâ etemmehâ ve aslahahâ, gloss:biri bir iyiliği tamamlayıp düzene koyduğunda "rabbe" denir, source:"ر ب ب,B002"}. Aynı kök nimetin kendisinin de adıdır: {ar:الربى: النعمة والإحسان, tr:er-ribbâ: en-ni'metu ve'l-ihsân, gloss:ribbâ, nimet ve iyiliktir, source:"ر ب ب,B016"}. Beşinci ayetteki haset ise o nimetin gitmesini istemektir: {ar:الحسد أن يرى الإنسان لأخيه نعمة فيتمنى أن تزوى عنه وتكون له, tr:el-hasedu en yerâ'l-insânu li-eḣîhi ni'meten fe-yetemennâ en tuzvâ anhu ve tekûne leh, gloss:haset, insanın kardeşinde bir nimet görüp onun ondan alınmasını ve kendisinin olmasını istemesidir, source:"ح س د,B001"}.

Bu tanım bir işleyişi adım adım verir: önce görme, sonra istek, istenen şey de bir yer değiştirmedir; nimet ondan sökülecek, bana geçecek. Beşinci ayet bu işleyişin son adımını ayrıca adlandırır: {ar:وَمِن شَرِّ حَاسِدٍ إِذَا حَسَدَ, tr:ve min şerri hâsidin izâ hased, gloss:ve haset ettiğinde hasetçinin şerrinden, source:113:5}. Ayet önce haset eden birini anar, sonra onun haset ettiği anı. Tanımın sonu bu ayrımı söyler: {ar:تمني زوال نعمة من مستحق لها وربما كان مع ذلك سعي في إزالتها, tr:temennî zevâli ni'metin min mustehikkın lehâ, ve rubbemâ kâne mea zâlike sa'yun fî izâletihâ, gloss:bir nimetin hak edenden gitmesini istemek; bazen bununla birlikte onu gidermeye çalışmak da olur, source:"ح س د,B001"}. Zarar, istek bir çabaya dönüştüğü anda doğar. Bu isteğin yanında bir de zararsız bir istek vardır: {ar:الغبط أن يتمنى أن يكون له مثلها من غير أن تزوى عنه, tr:el-ğabtu en yetemennâ en yekûne lehû misluhâ min ğayri en tuzvâ anh, gloss:gıpta, ondan alınmaksızın onun bir benzerinin kendisinde olmasını istemektir, source:"ح س د,B002"}. Biri nimeti yerinde bırakıp çoğalmasını ister; öbürü onu yerinden söker.

Sade bir anlam "hasetçinin kötülüğünden" der. Bu imgede ise surenin iki ucu birbirine bakar: ilk ayetin Rabbi nimeti tamamlayıp düzene koyandır, beşinci ayetin hasetçisi O'nun tamamladığını sökmek isteyendir. Sığınan, tamamlayana sığınarak sökmek isteyenden korunur. İkinci ayetin kelimeleri bu karşılaşmayı genişletir. Halk kökü herkese ölçülüp verilen payı adlandırır: {ar:الخلاق النصيب لأنه قد قدر لكل أحد نصيبه, tr:el-ḣalâku'n-nasîb, li-ennehû kad kuddira li-kulli ehadin nasîbuh, gloss:halâk paydır, çünkü herkesin payı ölçülüp belirlenmiştir, source:"خ ل ق,B006"}; bu ölçünün aslı da doğru ölçmedir: {ar:الخلق أصله: التقدير المستقيم, tr:el-ḣalku asluhû et-takdîru'l-mustekîm, gloss:halkın aslı doğru ölçmedir, source:"خ ل ق,B001"}. Haset bu ölçüye itiraz eder. Şer kökünün bir dalı da hasetçinin bütün benliğini arzu ettiği şeyin üstüne atışını adlandırır: {ar:ألقى عليه شراشره إذا ألقى عليه نفسه حرصا ومحبة, tr:elkâ aleyhi şerâşirahû izâ elkâ aleyhi nefsehû hırsan ve mahabbe, gloss:hırs ve sevgiyle kendini bir şeyin üstüne attığında "şerâşirini onun üstüne attı" denir, source:"ش ر ر,B007"}; {ar:جمع ما انتشر من هممه لهذا الشيء وشغل همومه كلها به, tr:cemea mentesera min himemihî li-hâze'ş-şey'i ve şeğale humûmehû kullehâ bih, gloss:dağılmış bütün ilgisini bu şey için topladı, bütün kaygısını onunla meşgul etti, source:"ش ر ر,B007"}. Bu, ayetteki şerrin anlamı değil, yanında duyulan bir imgedir: başkasının payına bütün ilgisini toplayan bir göz.

Kur'an bu sahneyi Yusuf'un kıssasında baştan sona gösterir. Yusuf babasına on bir yıldızın, güneşin ve ayın kendisine secde ettiğini gördüğünü anlatır {source:12:4}. Yakup şöyle cevap verir: {ar:لَا تَقْصُصْ رُءْيَاكَ عَلَىٰٓ إِخْوَتِكَ فَيَكِيدُوا۟ لَكَ كَيْدًا, tr:lâ taksus ru'yâke alâ iḣvetike fe-yekîdû leke keydâ, gloss:rüyanı kardeşlerine anlatma, sonra sana bir tuzak kurarlar, source:12:5}; ve hemen ardından: {ar:وَيُتِمُّ نِعْمَتَهُۥ عَلَيْكَ, tr:ve yutimmu ni'metehû aleyk, gloss:ve nimetini sana tamamlayacak, source:12:6}. Rabbin tamamladığı nimet ile kardeşlerin kuracağı tuzak aynı konuşmanın içindedir. Kardeşler kendi aralarında konuşur: {ar:لَيُوسُفُ وَأَخُوهُ أَحَبُّ إِلَىٰٓ أَبِينَا مِنَّا, tr:le-yûsufu ve eḣûhu ehabbu ilâ ebînâ minnâ, gloss:Yusuf ile kardeşi babamıza bizden daha sevgilidir, source:12:8}; ve {ar:ٱقْتُلُوا۟ يُوسُفَ أَوِ ٱطْرَحُوهُ أَرْضًۭا يَخْلُ لَكُمْ وَجْهُ أَبِيكُمْ, tr:uktulû yûsufe evi'trahûhu ardan yaḣlu lekum vechu ebîkum, gloss:Yusuf'u öldürün ya da bir yere atın ki babanızın yüzü yalnız size kalsın, source:12:9}. Kıssada haset kelimesi geçmez; ama işleyiş tanımdaki gibidir: başkasında görülen bir yakınlık, onun ondan alınıp bize kalması isteği ve bu isteğin bir plana dönüşmesi.

Kur'an kelimenin kendisini de kullanır. Allah Kitap ehli hakkında {ar:أَمْ يَحْسُدُونَ ٱلنَّاسَ عَلَىٰ مَآ ءَاتَىٰهُمُ ٱللَّهُ مِن فَضْلِهِۦ, tr:em yahsudûne'n-nâse alâ mâ âtâhumullâhu min fadlih, gloss:yoksa Allah'ın lütfundan insanlara verdiği şey için onları kıskanıyorlar mı, source:4:54} der; hasedin hedefi, verilenin içinden verenin lütfudur. Başka bir yerde kıskanılan nimet imanın kendisidir: {ar:لَوْ يَرُدُّونَكُم مِّنۢ بَعْدِ إِيمَٰنِكُمْ كُفَّارًا حَسَدًۭا مِّنْ عِندِ أَنفُسِهِم, tr:lev yeruddûnekum min ba'di îmânikum kuffâran hasedan min indi enfusihim, gloss:içlerindeki hasetten ötürü, iman ettikten sonra sizi inkâra döndürmeyi isterler, source:2:109}; müminlere verilen cevap da {ar:فَٱعْفُوا۟ وَٱصْفَحُوا۟ حَتَّىٰ يَأْتِىَ ٱللَّهُ بِأَمْرِهِۦٓ, tr:fa'fû vasfahû hattâ ye'tiyallâhu bi-emrih, gloss:Allah emrini getirinceye kadar affedin, geçin, source:2:109} olur. Allah müminlere hasedin kapısını kapatan sözü de söyler: {ar:وَلَا تَتَمَنَّوْا۟ مَا فَضَّلَ ٱللَّهُ بِهِۦ بَعْضَكُمْ عَلَىٰ بَعْضٍۢ ۚ لِّلرِّجَالِ نَصِيبٌۭ مِّمَّا ٱكْتَسَبُوا۟, tr:ve lâ tetemennev mâ faddalallâhu bihî ba'dakum alâ ba'd, li'r-ricâli nasîbun mimme'ktesebû, gloss:Allah'ın kiminizi kiminize üstün kıldığı şeyi istemeyin; erkeklerin kazandıklarından bir payı vardır, source:4:32}. Hasedin tanımındaki istek ile payın tanımındaki pay aynı ayette durur; ayet de gıptanın yolunu gösterir: {ar:وَسْـَٔلُوا۟ ٱللَّهَ مِن فَضْلِهِۦٓ, tr:ves'elullâhe min fadlih, gloss:Allah'tan lütfunu isteyin, source:4:32}. Payları bölüştüren de Rabdir: {ar:نَحْنُ قَسَمْنَا بَيْنَهُم مَّعِيشَتَهُمْ فِى ٱلْحَيَوٰةِ ٱلدُّنْيَا, tr:nahnu kasemnâ beynehum maîşetehum fi'l-hayâti'd-dunyâ, gloss:dünya hayatında geçimlerini aralarında biz bölüştürdük, source:43:32}. Düşmanca yakınlar için Allah {ar:إِن تَمْسَسْكُمْ حَسَنَةٌۭ تَسُؤْهُمْ, tr:in temseskum hasenetun tesu'hum, gloss:size bir iyilik dokunsa onları üzer, source:3:120} der ve korumanın yolunu ekler: {ar:وَإِن تَصْبِرُوا۟ وَتَتَّقُوا۟ لَا يَضُرُّكُمْ كَيْدُهُمْ شَيْـًٔا, tr:ve in tasbirû ve tetteķû lâ yadurrukum keyduhum şey'â, gloss:sabreder ve sakınırsanız tuzakları size hiçbir zarar vermez, source:3:120}. Nimetin tamamlanmasını Allah kendisine nispet eder: {ar:وَأَتْمَمْتُ عَلَيْكُمْ نِعْمَتِى, tr:ve etmemtu aleykum ni'metî, gloss:nimetimi size tamamladım, source:5:3}. Hasedin tersini de Kur'an, kendilerine gelenleri yurtlarına kabul edenlerin göğsünde gösterir: {ar:وَلَا يَجِدُونَ فِى صُدُورِهِمْ حَاجَةًۭ مِّمَّآ أُوتُوا۟, tr:ve lâ yecidûne fî sudûrihim hâceten mimmâ ûtû, gloss:onlara verilen şeyden ötürü göğüslerinde bir istek duymazlar, source:59:9}.

Kaynaklar: 113:1 بِرَبِّ ر ب ب B002; 113:1 بِرَبِّ ر ب ب B016; 113:5 حَاسِدٍ ح س د B001; 113:5 حَسَدَ ح س د B001; 113:5 حَاسِدٍ ح س د B002; 113:2 شَرِّ ش ر ر B007; 113:2 خَلَقَ خ ل ق B006; 113:2 خَلَقَ خ ل ق B001

## İçeride tutulan, dışarı çıkan

Surenin birçok kelimesi, içeride tutulan bir şeyin dışarı çıkışını adlandırır. Üfleme kökü, göğsü sıkışan için bir zorunluluk söyler: {ar:لا بد للمصدور أن ينفث, tr:lâ budde li'l-masdûri en yenfus, gloss:göğsü dolan, mutlaka üfleyip boşaltır, source:"ن ف ث,B003"}. Yılan zehrini üfler: {ar:الحية تنفث السم, tr:el-hayyetu tenfusu's-semm, gloss:yılan zehir üfler, source:"ن ف ث,B001"}. Yara kanı dışarı verir: {ar:دم نفيث نفثه الجرح أي أظهره, tr:demun nefîsun nefesehu'l-curhu ey azharah, gloss:yaranın üfleyip çıkardığı, yani ortaya koyduğu kan, source:"ن ف ث,B002"}. Üçüncü ayetin kökü de yaranın akıntısını adlandırır: {ar:غسق الجرح غسقانا إذا سال منه ماء أصفر, tr:ğasaka'l-curhu ğasakânen izâ sâle minhu mâun asfar, gloss:yaradan sarı su aktığında "ğasaka" denir, source:"غ س ق,B004"}; ve ateşte olanların derisinden damlayanı: {ar:الغساق ما تقطر من جلود أهل النار, tr:el-ğassâku mâ tekattara min culûdi ehli'n-nâr, gloss:ğassâk, ateş ehlinin derilerinden damlayandır, source:"غ س ق,B002"}. Şer kökü ateşten uçuşan kıvılcımı: {ar:الشرر ما تطاير من النار الواحدة شررة, tr:eş-şeraru mâ tetâyera mine'n-nâr, el-vâhidetu şerara, gloss:şerar, ateşten uçuşandır; tekili şerara, source:"ش ر ر,B003"}; ve yukarıda görülen "çıkarıp göstermek" anlamını taşır: {ar:أشررت الشيء أظهرته, tr:eşrartu'ş-şey'e azhartuh, gloss:şeyi ortaya koydum, source:"ش ر ر,B008"}. Yaranın kanını "ortaya koyan" fiil ile bu fiil aynıdır.

Öfke de önce bağlanır, sonra çıkar: {ar:عقد ناصيته إذا غضب فتهيأ للشر, tr:akade nâsiyetehû izâ ğadibe fe-teheyyee li'ş-şerr, gloss:öfkelenip kötülüğe hazırlandığında perçemini düğümledi denir, source:"ع ق د,B012"}. Haset de bir istek olarak içeride durur, sonra bir çabaya dönüşür: {ar:وربما كان مع ذلك سعي في إزالتها, tr:ve rubbemâ kâne mea zâlike sa'yun fî izâletihâ, gloss:bazen bununla birlikte onu gidermeye çalışmak da olur, source:"ح س د,B001"}. Sözün de içeride tutulan bir hâli vardır: {ar:في نفسي قول لم أظهره, tr:fî nefsî kavlun lem uzhirh, gloss:içimde ortaya koymadığım bir söz var, source:"ق و ل,B012"}.

Bu imge surenin iki "izâ" cümlesine bir yön verir. Üçüncü ayette karanlık içeri girer: {ar:إِذَا وَقَبَ, tr:izâ vekab, gloss:içeri girdiğinde, source:113:3}. Beşinci ayette haset dışarı çıkar: {ar:إِذَا حَسَدَ, tr:izâ hased, gloss:haset ettiğinde, source:113:5}. Biri dışarıdan içeriye, öbürü içeriden dışarıya bir eşik geçişidir ve sığınma tam bu eşiklere yönelir. Karanlık henüz girmemişken, haset henüz çabaya dönmemişken zarar beklemededir; tehlike geçiş anındadır. Düğümlenen öfke ile düğüme üflenen nefes de aynı eşikte durur: tutulan şey bir yere bırakılır. Emredilen söz ise bunların karşısında konuşanın kendi çıkarışıdır. "Kul" emri, içeride duran sığınma sözünü dışarı çıkarır; zehir, irin ve kıvılcım dışarı çıkarken sığınan da kendi sözünü çıkarır.

Kur'an bu çıkışı düşmanca yakınlar hakkında Allah'ın müminlere uyarısında sahneler: {ar:قَدْ بَدَتِ ٱلْبَغْضَآءُ مِنْ أَفْوَٰهِهِمْ وَمَا تُخْفِى صُدُورُهُمْ أَكْبَرُ, tr:kad bedeti'l-bağdâu min efvâhihim ve mâ tuḣfî sudûruhum ekber, gloss:öfke ağızlarından taşmıştır; göğüslerinin sakladığı ise daha büyüktür, source:3:118}. Ağızdan çıkan, göğüste tutulanın bir parçasıdır. Ayetler devam eder: {ar:وَإِذَا خَلَوْا۟ عَضُّوا۟ عَلَيْكُمُ ٱلْأَنَامِلَ مِنَ ٱلْغَيْظِ ۚ قُلْ مُوتُوا۟ بِغَيْظِكُمْ, tr:ve izâ ḣalev addû aleykumu'l-enâmile mine'l-ğayz, kul mûtû bi-ğayzikum, gloss:yalnız kaldıklarında size karşı öfkeden parmak uçlarını ısırırlar; de ki: öfkenizle ölün, source:3:119}. Öfke içeride tutulur ve onun karşısına yine emredilen bir "de ki" konur. Hemen ardından gelen ayette ise iyiliğin onları üzdüğü söylenir {source:3:120}. Kıvılcım ve akıntı Kur'an'da ateşin sahnesine aittir. Ayırma Günü'nü anlatan ayetlerde ateş için {ar:إِنَّهَا تَرْمِى بِشَرَرٍۢ كَٱلْقَصْرِ, tr:innehâ termî bi-şerarin ke'l-kasr, gloss:o, saray gibi kıvılcımlar atar, source:77:32} denir; azgınların içeceği de {ar:هَٰذَا فَلْيَذُوقُوهُ حَمِيمٌۭ وَغَسَّاقٌۭ, tr:hâzâ fe'l-yezûkûhu hamîmun ve ğassâk, gloss:işte bu; tatsınlar onu: kaynar su ve irin, source:38:57} olur; başka bir yerde de yalnızca {ar:إِلَّا حَمِيمًۭا وَغَسَّاقًۭا, tr:illâ hamîmen ve ğassâkâ, gloss:kaynar su ve irinden başka, source:78:25}. Şer kelimesinin akrabası kıvılcım, gāsık kelimesinin akrabası irin, böylece ateşte dışarı atılanın adları olarak Kur'an'da geçer. Ayetteki şer de gāsık da bu anlamlarda değildir; ama aynı köklerden çıkan bu sözler, içeride tutulan zararın bir gün dışarı atılacağını yanlarında duyurur.

Kaynaklar: 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B003; 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B001; 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B002; 113:3 غَاسِقٍ غ س ق B004; 113:3 غَاسِقٍ غ س ق B002; 113:2 شَرِّ ش ر ر B003; 113:2 شَرِّ ش ر ر B008; 113:4 ٱلْعُقَدِ ع ق د B012; 113:5 حَسَدَ ح س د B001; 113:1 قُلْ ق و ل B012

## Yeni doğurmuş dişi ve yavrusu

Surenin ilk ayetindeki iki kelime, aynı hayvanı aynı anında adlandırır: yeni doğurmuş dişiyi. Sığınma kökü onu doğumdan sonraki ilk günleriyle anar: {ar:كل أنثى عائذ إذا وضعت مدة سبعة أيام, tr:kullu unsâ âizun izâ vada'at muddete seb'ati eyyâm, gloss:her dişi doğurduğunda yedi gün boyunca "âiz"dir, source:"ع و ذ,B003"}; {ar:العوذ الحديثات النتاج من الظباء والإبل والخيل واحدتها عائذ, tr:el-ûzu'l-hadîsâtu'n-nitâc mine'z-zıbâi ve'l-ibili ve'l-ḣayl, vâhidetuhâ âiz, gloss:ûz, ceylanlardan, develerden ve atlardan yeni doğurmuş olanlardır; tekili âizdir, source:"ع و ذ,B003"}. Rab kökü de yeni doğurmuş koyunu adlandırır: {ar:الربى: الشاة التي وضعت حديثا, tr:er-ubbâ: eş-şâtu'lletî vada'at hadîsen, gloss:rubbâ, yeni doğurmuş koyundur, source:"ر ب ب,B009"}; sütü için evde tutulan koyundur bu: {ar:الشاة الربي التي تحتبس في البيت للبن, tr:eş-şâtu'r-rubbâ elletî tuhtebesu fi'l-beyti li'l-leben, gloss:rubbâ koyun, sütü için evde alıkonulandır, source:"ر ب ب,B009"}.

Bu iki adın çevresinde köklerin geri kalanı bir doğum ve büyütme sürecini tamamlar. Düğüm kökü rahmin tohumu tutuşunu adlandırır: {ar:عقدت فم الرحم على الماء, tr:akadet feme'r-rahimi ale'l-mâ', gloss:rahmin ağzını suyun üzerine düğümledi, source:"ع ق د,B010"}. Halk kökü tamamlanmış ceninin adıdır: {ar:مضغة مخلقة أي تامة الخلق, tr:mudğatun muḣallaka ey tâmmetu'l-ḣalk, gloss:muhallak et parçası, yani yaratılışı tamamlanmış olan, source:"خ ل ق,B003"}. Rab kökü doğandan sonrasını üstlenir: çocuğu emziren ve bakan kadın, {ar:الربيبة: الحاضنة, tr:er-rabîbe: el-hâdına, gloss:rabîbe, çocuğa bakan kadındır, source:"ر ب ب,B005"}; üvey çocuğun işini üstlenen, {ar:الراب الذي يقوم على أمر الربيب, tr:er-râbbu'llezî yekûmu alâ emri'r-rabîb, gloss:râb, rabîbin işini üstlenendir, source:"ر ب ب,B005"}; ve çocuğu büyütmek: {ar:رب فلان ولده؛ رباه, tr:rabbe fulânun veledeh, rabbâh, gloss:biri çocuğunu büyüttü, source:"ر ب ب,B002"}.

İlk ayette sığınan ile sığınılan arasındaki ilişki bu sahnede bir doğumun hemen sonrası olarak duyulur. Doğumdan sonraki günlerde yavru en savunmasız hâlindedir ve büsbütün doğurana bağlıdır; doğuran da onu emzirip büyütmek için alıkonur. "Eûzu" ile "rab" kelimeleri ailelerinde bu iki tarafın adlarını taşır. Sade bir anlam "Rabbe sığınırım" der; bu imge sığınmayı yeni doğmuş bir canlının, onu dünyaya getiren ve büyüten varlığa duyduğu ihtiyaç kadar yakın kılar. Kelimelerin anlamı yine sığınmak ve Rabdir; doğum sahnesi bu anlamların yanında durur.

Kur'an bu sahnenin bütün adımlarını tek bir kıssada verir. İmran'ın karısı Rabbine şöyle seslenir: {ar:رَبِّ إِنِّى نَذَرْتُ لَكَ مَا فِى بَطْنِى مُحَرَّرًۭا, tr:rabbi innî nezertu leke mâ fî batnî muharraran, gloss:Rabbim, karnımdakini sana adanmış olarak adadım, source:3:35}. Doğum gelir: {ar:فَلَمَّا وَضَعَتْهَا, tr:fe-lemmâ vada'athâ, gloss:onu doğurunca, source:3:36}; ve doğurur doğurmaz annenin söylediği söz bir sığınmadır: {ar:وَإِنِّىٓ أُعِيذُهَا بِكَ وَذُرِّيَّتَهَا مِنَ ٱلشَّيْطَٰنِ ٱلرَّجِيمِ, tr:ve innî uîzuhâ bike ve zurriyyetehâ mine'ş-şeytâni'r-racîm, gloss:onu da soyunu da kovulmuş şeytandan sana sığındırırım, source:3:36}. Kökün yeni doğurmuş dişiyi adlandırdığı o günlerde anne, yavrusunu Rabbe sığındırır. Ardından Rab büyütmeyi üstlenir: {ar:فَتَقَبَّلَهَا رَبُّهَا بِقَبُولٍ حَسَنٍۢ وَأَنۢبَتَهَا نَبَاتًا حَسَنًۭا وَكَفَّلَهَا زَكَرِيَّا, tr:fe-tekabbelehâ rabbuhâ bi-kabûlin hasenin ve enbetehâ nebâten hasenen ve keffelehâ zekeriyyâ, gloss:Rabbi onu güzel bir kabulle kabul etti, güzel bir bitki gibi büyüttü ve Zekeriya'yı ona bakıcı yaptı, source:3:37}. Büyüme bir bitkinin büyümesi olarak söylenir ve çocuğun işini üstlenen bir bakıcı belirir. Rahim, doğum, Rabbe sığındırma ve Rabbin büyütmesi aynı sahnededir. Diriltilmekten şüphe edenlere hitap eden ayet de rahimdeki tutuluşu ve dışarı çıkarılışı birlikte anar: {ar:وَنُقِرُّ فِى ٱلْأَرْحَامِ مَا نَشَآءُ إِلَىٰٓ أَجَلٍۢ مُّسَمًّۭى, tr:ve nukırru fi'l-erhâmi mâ neşâu ilâ ecelin musemmâ, gloss:dilediğimizi belirli bir süreye kadar rahimlerde tutarız, source:22:5}.

Kaynaklar: 113:1 أَعُوذُ ع و ذ B003; 113:1 بِرَبِّ ر ب ب B009; 113:4 ٱلْعُقَدِ ع ق د B010; 113:2 خَلَقَ خ ل ق B003; 113:1 بِرَبِّ ر ب ب B005; 113:1 بِرَبِّ ر ب ب B002

## Savaş: korkulan ordu, öldürücü darbeden kurtuluş

İlk ayetin kelimeleri, aileleri içinden bir savaş sahnesi de taşır. Felak kökü korkunç bir orduyu adlandırır: {ar:الفيلق الكتيبة المنكرة الشديدة, tr:el-faylaku'l-katîbetu'l-munkeratu'ş-şedîde, gloss:faylak, korkunç ve çetin birliktir, source:"ف ل ق,B007"}; {ar:الفيلق الجيش والجمع الفيالق, tr:el-faylaku'l-ceyş ve'l-cem'u'l-fayâlık, gloss:faylak ordudur, çoğulu fayâlıktır, source:"ف ل ق,B007"}. Aynı kök savaşın felaketinin de adıdır: {ar:الفلق اسم الداهية من الحروب والكتائب وكل الدواهي, tr:el-felaku'smu'd-dâhiye mine'l-hurûbi ve'l-ketâib ve kulli'd-devâhî, gloss:felak, savaşların, birliklerin ve bütün felaketlerin belasının adıdır, source:"ف ل ق,B006"}. Sığınma kökü de bu savaşın içinde bir kurtuluşu adlandırır: {ar:أفلت منه فلان عوذا إذا خوفه ولم يضربه أو ضربه وهو يريد قتله فلم يقتله, tr:eflete minhu fulânun avzen izâ ḣavvefehû ve lem yadribhu ev darabehû ve huve yurîdu katlehû fe-lem yaktulh, gloss:biri onu korkutup vurmadığında ya da öldürmek isteyerek vurup öldüremediğinde, adam ondan "avzen" kurtuldu denir, source:"ع و ذ,B006"}. Savaşanların birbirine dayanması da bu köktendir: {ar:تعاوذ القوم في الحرب إذا تواكلوا وعاذ بعضهم ببعض, tr:teâveza'l-kavmu fi'l-harbi izâ tevâkelû ve âze ba'duhum bi-ba'd, gloss:savaşta topluluk birbirine dayanıp birbirine sığındığında "teâvezû" denir, source:"ع و ذ,B007"}. Rab kökü binlerce kişilik kalabalıkları adlandırır: {ar:الربيون: الألوف؛ الربيون: الجماعات الكثيرة, tr:er-ribbiyyûn: el-ulûf; er-ribbiyyûn: el-cemââtu'l-kesîra, gloss:ribbiyyûn binlerdir, kalabalık topluluklardır, source:"ر ب ب,B004"}; ve topluluğu yöneteni: {ar:رببت القوم: سستهم, tr:rabebtu'l-kavm: sustuhum, gloss:topluluğu yönettim, source:"ر ب ب,B001"}. Şer kökü de çekişmeyi adlandırır: {ar:المشارة المخاصمة, tr:el-muşârra el-muḣâsama, gloss:muşârra, çekişmedir, source:"ش ر ر,B011"}.

Bu sahnede ilk ayetin sığınması, öldürmek için inen bir darbeden sağ çıkmanın adını yanında taşır. Sığınmak burada bir tehlikenin ortasında hayatta kalmaktır; tehlike geçmiş değil, üstüne gelmiştir. Felak kökünün sabahı ve korkulan orduyu aynı köke toplaması, surenin ilk kelimesini iki yüzlü kılar; ama ayetteki anlam sabahtır, ordu yalnızca kök ailesinde yanında durur.

Kur'an bu kalabalıkların kelimesini kullanır. Bir savaşta uğranan sarsıntının ardından müminlere hitap eden ayetlerde Allah şöyle der: {ar:وَكَأَيِّن مِّن نَّبِىٍّۢ قَٰتَلَ مَعَهُۥ رِبِّيُّونَ كَثِيرٌۭ فَمَا وَهَنُوا۟ لِمَآ أَصَابَهُمْ فِى سَبِيلِ ٱللَّهِ, tr:ve keeyyin min nebiyyin kâtele meahû ribbiyyûne kesîrun fe-mâ vehenû li-mâ esâbehum fî sebîlillâh, gloss:nice peygamber vardır ki onunla birlikte pek çok topluluk savaştı; Allah yolunda başlarına gelenden ötürü gevşemediler, source:3:146}. Bu kelimenin ilk ayetteki rab ile aynı kökten olduğu, kökün kalabalık topluluk dalı üzerinden duyulur. Kur'an bir ordudan yarılan bir yolla kurtuluşu da Musa'nın kıssasında anlatır. Allah Musa'ya kullarını geceleyin yürütmesini vahyeder: {ar:أَنْ أَسْرِ بِعِبَادِىٓ إِنَّكُم مُّتَّبَعُونَ, tr:en esri bi-ibâdî innekum muttebaûn, gloss:kullarımı geceleyin yürüt, çünkü izleneceksiniz, source:26:52}. Firavun'un ordusu onları güneş doğarken yakalar {source:26:60}; iki topluluk birbirini görünce Musa'nın yanındakiler {ar:إِنَّا لَمُدْرَكُونَ, tr:innâ le-mudrakûn, gloss:yakalandık, source:26:61} der. Musa'nın cevabı bir sığınma cümlesidir: {ar:قَالَ كَلَّآ ۖ إِنَّ مَعِىَ رَبِّى سَيَهْدِينِ, tr:kâle kellâ, inne meiye rabbî se-yehdîn, gloss:hayır, Rabbim benimledir, bana yol gösterecek, source:26:62}. Sonra Allah denizi asayla vurmasını vahyeder: {ar:فَٱنفَلَقَ فَكَانَ كُلُّ فِرْقٍۢ كَٱلطَّوْدِ ٱلْعَظِيمِ, tr:fenfelaka fe-kâne kullu firkın ke't-tavdi'l-azîm, gloss:deniz yarıldı ve her parça büyük bir dağ gibi oldu, source:26:63}. Burada yarılan, felak kökünün fiiliyle yarılır. Yarılan denizin parçalarına verilen ad ise başka bir köktendir; ses yakınlığı bir kök birliği kurmaz.

Kaynaklar: 113:1 ٱلْفَلَقِ ف ل ق B007; 113:1 ٱلْفَلَقِ ف ل ق B006; 113:1 أَعُوذُ ع و ذ B006; 113:1 أَعُوذُ ع و ذ B007; 113:1 بِرَبِّ ر ب ب B004; 113:1 بِرَبِّ ر ب ب B001; 113:2 شَرِّ ش ر ر B011

## Uydurulan ve yayılan söz

Surenin söz ve yaratma kelimeleri, kök ailelerinde uydurulmuş sözü de adlandırır. "Kul" emrinin kökü olmamış bir şeyi söylemeyi anlatır: {ar:تقول باطلا أي قال ما لم يكن, tr:tekavvele bâtılen ey kâle mâ lem yekun, gloss:asılsız söz uydurdu, yani olmamış olanı söyledi, source:"ق و ل,B005"}; {ar:تقول عليه أي كذب عليه, tr:tekavvele aleyhi ey kezebe aleyh, gloss:onun hakkında söz uydurdu, yani onun adına yalan söyledi, source:"ق و ل,B005"}. Aynı kök insanlar arasında yayılan sözü de adlandırır: {ar:القالة القول الفاشي في الناس, tr:el-kâle el-kavlu'l-fâşî fi'n-nâs, gloss:kâle, insanlar arasında yayılan sözdür, source:"ق و ل,B007"}. İkinci ayetin halk kökü söz için kullanıldığında yalan demektir: {ar:خلق الإفك واختلقه وتخلقه أي افتراه, tr:ḣaleka'l-ifke vaḣtelekahû ve teḣallekahû ey efterâh, gloss:yalanı yarattı, uydurdu; yani onu düzdü, source:"خ ل ق,B007"}; {ar:كل موضع استعمل الخلق في وصف الكلام فالمراد به الكذب, tr:kullu mevdiin ustumile'l-ḣalku fî vasfi'l-kelâmi fe'l-murâdu bihi'l-kezib, gloss:halk kelimesinin söz için kullanıldığı her yerde kastedilen yalandır, source:"خ ل ق,B007"}. Dördüncü ayetin kelimeleri de söze uzanır: ağızdan üflenen söz {source:"ن ف ث,B005"} ve anlaşılmaz kılınmış, düğümlenmiş söz: {ar:كلام معقد أي مغمض, tr:kelâmun muakkad ey muğmad, gloss:düğümlü söz, yani kapalı söz, source:"ع ق د,B007"}. Şer kökü de birine kötülük isnat etmeyi adlandırır: {ar:أشررت فلانا إذا نسبته إلى الشر, tr:eşrartu fulânen izâ nesebtuhû ile'ş-şerr, gloss:birini kötülüğe nispet ettiğimde "eşrartu" derim, source:"ش ر ر,B001"}; arkasından da çekişme gelir {source:"ش ر ر,B011"}.

Bu ailede sözün bir zarar yolu belirir: olmamış bir şey söylenir, birine isnat edilir, dilden dile yayılır, anlaşılmaz kılınır ve sonunda birine kötülük yakıştırılıp çekişme doğar. İkinci ayetin anlamı Allah'ın yaratmasıdır ve bu yalan anlamı orada değildir; ama kök ailesinde yanında durarak yaratılmışların şerrinin bir türünü, insan ağzının uydurduğu şeyi akla getirir. Bu yolun karşısında surenin ilk kelimesi durur. "Kul", bir uydurma değil, emredilmiş bir sözdür; söyleyen onu kendinden düzmez, kendisine söylenmesi emredileni söyler ve onu bir insana değil, Rabbe yöneltir.

Kur'an emredilmiş söz ile uydurulmuş sözü aynı kökle karşı karşıya koyar. Allah Elçisinin doğruluğu hakkında şöyle der: {ar:وَلَوْ تَقَوَّلَ عَلَيْنَا بَعْضَ ٱلْأَقَاوِيلِ, tr:ve lev tekavvele aleynâ ba'da'l-ekâvîl, gloss:eğer o bize karşı bazı sözler uydurmuş olsaydı, source:69:44}. Uydurmanın fiili, "kul" emrinin kökünden gelir ve emredilen sözün tam karşıtıdır. İbrahim kavmine putlara tapınmalarını bu kökle anlatır: {ar:إِنَّمَا تَعْبُدُونَ مِن دُونِ ٱللَّهِ أَوْثَٰنًۭا وَتَخْلُقُونَ إِفْكًا, tr:innemâ ta'budûne min dûnillâhi evsânen ve taḣlukûne ifkâ, gloss:siz Allah'ı bırakıp yalnızca putlara tapıyor ve yalan uyduruyorsunuz, source:29:17}. Allah'ın yaratmasını anlatan fiil burada insanın yalan yaratmasını anlatır. Elçiye karşı çıkan ileri gelenler ise aynı suçlamayı tersine çevirir: {ar:إِنْ هَٰذَآ إِلَّا ٱخْتِلَٰقٌ, tr:in hâzâ ille'ḣtilâk, gloss:bu bir uydurmadan başka bir şey değil, source:38:7}. Bir iftiranın dilden dile geçişini de Allah müminlere hitap ederek gösterir: {ar:إِذْ تَلَقَّوْنَهُۥ بِأَلْسِنَتِكُمْ وَتَقُولُونَ بِأَفْوَاهِكُم مَّا لَيْسَ لَكُم بِهِۦ عِلْمٌۭ, tr:iz telakkavnehû bi-elsinetikum ve tekûlûne bi-efvâhikum mâ leyse lekum bihî ilm, gloss:onu dillerinizle birbirinizden alıyor, hakkında bilginiz olmayan şeyi ağızlarınızla söylüyordunuz, source:24:15}. Söz dilden alınır, ağızdan verilir; kökün "yayılan söz" dalının sahnesi budur. Yusuf'un kardeşlerinin hasedi de uydurulmuş bir anlatıya varır: {ar:فَأَكَلَهُ ٱلذِّئْبُ, tr:fe-ekelehu'z-zi'b, gloss:onu kurt yedi, source:12:17}, ve gömlekte sahte kan getirirler: {ar:وَجَآءُو عَلَىٰ قَمِيصِهِۦ بِدَمٍۢ كَذِبٍۢ, tr:ve câû alâ kamîsihî bi-demin kezib, gloss:gömleğinin üstünde yalan bir kanla geldiler, source:12:18}. Babanın cevabı Allah'tan yardım istemektir: {ar:وَٱللَّهُ ٱلْمُسْتَعَانُ عَلَىٰ مَا تَصِفُونَ, tr:vallâhu'l-musteânu alâ mâ tesıfûn, gloss:anlattığınız şeye karşı yardımı istenecek olan Allah'tır, source:12:18}. Uydurulan söze karşı da söylenecek söz, yönü Allah'a dönük bir sözdür.

Kaynaklar: 113:1 قُلْ ق و ل B005; 113:1 قُلْ ق و ل B007; 113:2 خَلَقَ خ ل ق B007; 113:4 ٱلنَّفَّٰثَٰتِ ن ف ث B005; 113:4 ٱلْعُقَدِ ع ق د B007; 113:2 شَرِّ ش ر ر B001; 113:2 شَرِّ ش ر ر B011

## Buluşmalar

Gece ile yarılıp çıkarılış ilk buluşmadır. Sabah, yarılıp çıkarılan şeylerin bir örneğidir: karanlık yarılır ve ışık açığa konur; tohum yarılır ve filiz çıkar. Göğün kuruluşunu anlatan ayet ikisini aynı fiille birleştirir; gece karartılır ve kuşluk dışarı çıkarılır {source:79:29}. Kur'an aynı çıkarılışı insanlar için de söyler: {ar:ٱللَّهُ وَلِىُّ ٱلَّذِينَ ءَامَنُوا۟ يُخْرِجُهُم مِّنَ ٱلظُّلُمَٰتِ إِلَى ٱلنُّورِ, tr:allâhu veliyyu'llezîne âmenû, yuḣricuhum mine'z-zulumâti ile'n-nûr, gloss:Allah inananların dostudur; onları karanlıklardan aydınlığa çıkarır, source:2:257}. Üçüncü ayetin karanlığına giren kişi, ilk ayetin Rabbine sığındığında bu çıkarılışın içine girer. Gece ile yağmur da birbirine dökülür: gece tepelere bir sıvı gibi boşalır, gök çiseler, ve aynı kök hem gecenin dökülüşünü hem göğün çiselemesini taşır. Felakın iki tepe arasındaki alçak yeri, gecenin döküldüğü tepelerin eteğidir; karanlık da su da oraya iner.

Şafağın iplikleri ile büyücünün iplikleri ikinci buluşmadır. Oruç ayetinde tan, beyaz ipliğin siyah iplikten ayrılmasıdır {source:2:187}; dördüncü ayette ise büyücüler ipliklere düğüm atar. Aynı malzeme iki zıt işleme uğrar: Rabbin sabahı iplikleri birbirinden ayırır, büyücünün eli iplikleri birbirine bağlar. Sure bu iki işlemi baştan ve sondan çerçeveler: ayıran Rab ilk ayettedir, bağlayan el dördüncüde. Musa'nın duasında da bir düğüm çözülür ve söz açığa çıkar {source:20:27} {source:20:28}; düğümü çözen Rab, sözü açılan kul. Böylece düğüm imgesi ile ağız imgesi aynı duada buluşur: dilin düğümü çözüldüğünde ağız konuşur, düğüme üfleyen ağız ise sözü bağlar.

Ağız ile ışık üçüncü buluşmadır. Namaz emrinde gecenin koyulaşmasının ardından sabahın okunuşu gelir {source:17:78}: karanlığın sonunda bir ağız okur. İnkâr edenler ise ağızlarıyla ışığa üfler: {ar:يُرِيدُونَ لِيُطْفِـُٔوا۟ نُورَ ٱللَّهِ بِأَفْوَٰهِهِمْ وَٱللَّهُ مُتِمُّ نُورِهِۦ, tr:yurîdûne li-yutfiû nûrallâhi bi-efvâhihim vallâhu mutimmu nûrih, gloss:Allah'ın nurunu ağızlarıyla söndürmek isterler; Allah ise nurunu tamamlayandır, source:61:8}. Bu ayette üç imge birden durur: ışığa karşı üfleyen ağızlar, söndürülmek istenen ışık ve o ışığı tamamlayan Allah. Düğüme üfleyen ağız ışığa karşı çalışır; emredilen ağız ışığın yanında durur. Işığı tamamlayan, nimeti tamamlayan Rabdir; hasetçinin sökmek istediği nimet ile inkârcının söndürmek istediği ışık aynı "tamamlama" fiiliyle korunur.

Musa'nın denizden geçişi dört imgeyi tek bir sahnede tutar. Gece yürüyüşü emredilir {source:26:52}; ordu güneş doğarken yetişir {source:26:60}; yanındakiler yakalandıklarını söyler {source:26:61}; Musa "Rabbim benimledir" der {source:26:62}; ve deniz felak kökünün fiiliyle yarılır {source:26:63}. Gece, korkulan ordu, Rabbe tutunan bir cümle ve yarılıp açılan bir yol aynı anlatıdadır. Sığınmanın bir uzaklaşma değil bir yakınlık olduğu da burada görünür: Musa'nın sözü "Rabbim benimledir"dir.

İmran'ın karısının kıssası doğum, sığınma ve büyüme imgelerini birleştirir. Rahimdekini adayan anne doğurur, doğurduğunu Rabbe sığındırır ve Rab onu bir bitki gibi büyütür {source:3:36} {source:3:37}. Burada sığınma kökü yeni doğurmuş dişinin adını taşırken, rab kökü hem doğan yavruyu büyütmeyi hem bir şeyi aşama aşama tamamlamayı taşır; tohumdan filiz çıkaran yarma da büyümenin ilk adımıdır. Rabbin bir çocuğu büyütmesi ile bir nimeti tamamlaması aynı köke aittir; Yakup'un Yusuf'a söylediği "nimetini sana tamamlayacak" sözü {source:12:6} bu yüzden doğumla başlayan büyütmenin sonucunu söyler.

Yusuf'un kıssası haset, göz ve uydurulmuş söz imgelerini birbirine bağlar. Bir rüya görülür ve anlatılmaması istenir, çünkü görülen bir nimet kardeşlerde tuzak doğurur {source:12:5}. Babanın yakınlığına bakan kardeşler o yakınlığın kendilerine kalmasını ister {source:12:9}; isteği bir plana, planı bir yalana dönüştürürler {source:12:18}. Hasedin sonucu bir babanın gözlerinde görünür {source:12:84}. Hasetçinin "haset ettiği an", gördüğü nimeti sökmek için harekete geçtiği andır ve bu an kendi arkasından uydurulan bir sözü getirir.

Surenin hareketi bu buluşmalarla görünür hâle gelir. İlk ayetin Rabbi yarar, açar ve çıkarır; ikinci ayette bu çıkarılmış şeylerin bütünü vardır. Üçüncü ayette karanlık dışarıdan içeri girer ve kapatır; dördüncü ayette bir el ipliğin uçlarını bağlar ve bir ağız onu nefesle mühürler; beşinci ayette içeride tutulan bir istek dışarı çıkar ve tamamlanmış bir nimeti sökmeye yönelir. Zarar her seferinde Rabbin işinin tersini yapar: O açarken karanlık kapatır, O ayırırken büyücü bağlar, O tamamlarken hasetçi söker. Sığınılan da sırf bu yüzden, her biri bu ters işlerden birinin karşısında duran "felakın Rabbi"dir. Kapsam da daralarak ilerler: önce bütün yaratılmışlar, sonra bir zaman olarak gece, sonra bir zanaatı olan kadınlar, en sonda tek bir hasetçi ve onun tek bir anı. Bu daralmanın karşısında ilk kelime sabit durur: emredilmiş bir söz, ağızdan çıkıp Rabbe yönelen ve söyleyeni O'na bağlayan bir sığınma.

