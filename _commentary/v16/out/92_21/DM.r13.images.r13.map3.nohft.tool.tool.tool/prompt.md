Focus: 92:21. Follow the brief below (write.md) and its additions (additions.md) exactly. The evidence is context.md (the ayah, its words and anchor translation, the Fatiha, the whole surah) and 01_dictionary.md (every attested branch of every root of the ayah's words, with the classical dictionaries' source phrases) and images.md (an earlier reader's commentary on the surah's images, cut to the images whose sources include this ayah, and the section on where images meet; a proposal, not an authority. Develop here each image this ayah's words take part in, as write.md says; the shared scenes are the surah commentary's) and your own knowledge of Arabic and the Quran. Return the reader's prose and then the ledger, as write.md specifies.

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


===== _commentary/v16/work/92_21/D.r13/context.md =====
# 92:21 — focus

وَلَسَوْفَ يَرْضَىٰ

Anchor translation (canonical reading, reference only):

Ve elbette hoşnut olacaktır.

## Words (QAC; roots via quran-data gateway)

| w | surface | lemma | root | pos |
|---|---|---|---|---|
| 1 | وَلَسَوْفَ | سَوْف |  | CONJ;EMPH;FUT |
| 2 | يَرْضَىٰ | رَّضِىَ | ر ض و | V |


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
- 92:13 وَإِنَّ لَنَا لَلْءَاخِرَةَ وَٱلْأُولَىٰ
- 92:14 فَأَنذَرْتُكُمْ نَارًۭا تَلَظَّىٰ
- 92:15 لَا يَصْلَىٰهَآ إِلَّا ٱلْأَشْقَى
- 92:16 ٱلَّذِى كَذَّبَ وَتَوَلَّىٰ
- 92:17 وَسَيُجَنَّبُهَا ٱلْأَتْقَى
- 92:18 ٱلَّذِى يُؤْتِى مَالَهُۥ يَتَزَكَّىٰ
- 92:19 وَمَا لِأَحَدٍ عِندَهُۥ مِن نِّعْمَةٍۢ تُجْزَىٰٓ
- 92:20 إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ
- 92:21 ◀ focus وَلَسَوْفَ يَرْضَىٰ


===== _commentary/v16/work/92_21/D.r13/01_dictionary.md =====
# Dictionary: every branch of every focus root

One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression.
Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this
exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.

## ر ض و (root_000569) — identity root of يَرْضَىٰ (w2)

- **B001** hoşnut olma ve kabul etme — hoşnut olmak; kabul etmek · hoşnut · kabul edilmiş; kendisinden hoşnut olunan · kendisinden hoşnut olunan kişi · hoşnutluk · onu kabul edip uygun buldu · onu seçip uygun buldu · ondan hoşnut oldu; onu kabul etti · hoşnutluk adı · beğenilen bir yaşayış · onu arkadaş olarak kabul etti · ondan hoşnut oldu; onu uygun buldu · beğenilen; kabul edilen · kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması · Tanrı'nın kulu buyruğa uyan ve yasaktan kaçınan biri olarak görmesi
  أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضا مقصور (ayn)؛ رضيت الشيء وارتضيته فهو مرضي ومرضو ورضيت عنه رضا (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو ورضا العبد عن الله ورضا الله عن العبد (mufradat)
- **B002** hoşnutluk; yoğun hoşnutluk — hoşnutluk; yoğun hoşnutluk · hoşnutluk
  الرضوان اسم موضوع من الرضا (ayn)؛ الرضوان الرضا وكذلك الرضوان بالضم والمرضاة مثله (sihah)؛ الرضوان الرضا الكثير (mufradat)
- **B003** karşılıklı hoşnutluk ve kabul — karşılıklı hoşnutluk · birbiriyle hoşnutlaşma · birbirlerinden hoşnut olduklarını karşılıklı gösterdiler
  المراضاة من اثنين (ayn)؛ مصدر راضيته رضاء ومراضاة (sihah;tahdhib)؛ إذا تراضوا بينهم أي أظهر كل واحد منهم الرضا بصاحبه ورضيه (mufradat)
- **B004** başkasını hoşnut etme veya hoşnutluğunu isteme — onu kendimden hoşnut ettim · onu hoşnut ettim · uğraşarak onu hoşnut ettim · ondan hoşnutluk göstermesini istedim; o da beni hoşnut etti
  أرضيته عني ورضيته بالتشديد أيضا فرضي وترضيته أرضيته بعد جهد واسترضيته فأرضاني (sihah)
- **B005** karşılıklı çekişmede üstün gelme — karşılıklı çekişmede ona üstün geldim
  قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه لأنه من الواو (sihah)
- **B006** söz dinleyen, seven veya güvence veren — söz dinleyen; seven; güvence veren
  الرضي المطيع والرضي المحب والرضي الضامن (tahdhib)
- **B007** bir dağ adı ve kadın adları — bir dağ adı; bir kadın adı · o dağın adına bağlılık bildiren biçim · bir kadın adı
  رضوى جبل (maqayis;ayn;sihah)؛ ومن أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)

## ECHO ر ض ي (root_000570) — for يَرْضَىٰ (w2): withheld observed target; not identity

- **B001** hoşnut olup uygun bulma — hoşnut olmak; gönlüne uygun bulmak · hoşnut olan · beğenilmiş, uygun bulunmuş · kendisinden hoşnut olunan · uygun bulunmuş; eski kök yapısını koruyan biçim · kendisinden hoşnut olunan adam; eski kök yapısını koruyan söyleyiş · hoşnutluk; hoşnutsuzluğun karşıtı · hoşnutluğu bildiren uzatılmış ad biçimi · hoşnutluk; çok güçlü hoşnutluk · hoşnutluk bildiren ad · iki tarafın birbirini uygun bulması · birbirini uygun bulma ve karşılıklı anlaşma · şeyi beğenip uygun buldum · onu beğenip seçtim · ondan hoşnut oldum · onu arkadaş olarak uygun buldum · ondan ya da onunla olmaktan hoşnut oldum · beğenilen, hoşnutluk veren yaşayış · onu benden hoşnut ettim · onu hoşnut ettim · uğraştıktan sonra onu hoşnut ettim · onun gönlünü yapmaya çalıştım, sonunda benden hoşnut oldu · birbirlerini uygun bulup anlaştılar · kulun Tanrı'nın hükmünden hoşnutsuzluk duymaması · Tanrı'nın kulunu buyruklarına uyar ve yasaklarından kaçınır görmesi · beğenilmiş, uygun bulunmuş
  أصل واحد يدل على خلاف السخط (maqayis)؛ الرضا في الأصل من بنات الواو والرضوان من الرضا (ayn)؛ الرضوان الرضا والمرضاة مثله ورضيت الشيء وارتضيته (sihah)؛ رضي فلان يرضى رضى والرضي المرضي والرضا مقصور (tahdhib)؛ رضي يرضى رضا فهو مرضي ومرضو والرضوان الرضا الكثير (mufradat)
- **B002** çekişmede alt etme — o benimle çekişti, ben de onu o işte yendim
  قال أبو عبيد راضاني فلان فرضوته (maqayis)؛ راضاني فلان فرضوته أرضوه بالضم إذا غلبته فيه (sihah)
- **B003** dağ ve kadın adı ailesi — bir dağın ve bir kadının adı · söz konusu dağla ilgili veya o dağdan olan · bir kadın adı
  رضوى جبل (maqayis;ayn)؛ رضوى جبل بالمدينة والنسبة إليه رضوى (sihah)؛ من أسماء النساء رضيا وتكبيرهما رضوى وثروى (tahdhib)
- **B004** buyruğa uyan, seven veya güvence veren — buyruğa uyan, seven ya da güvence veren
  الرَّضِيّ المطيع؛ الرَّضِيّ المحب؛ الرَّضِيّ الضامن (tahdhib)

===== _commentary/v16/out/s092/images.r13.map3.nohft.tool.tool/images.md (only the images that cite 92:21, and ## Buluşmalar) =====
## Yüzü çevirmek, sırtı dönmek

Yirminci ayet bir yöneliş anlatır: {ar:إِلَّا ٱبْتِغَآءَ وَجْهِ رَبِّهِ ٱلْأَعْلَىٰ, tr:ille'btiğâe vechi rabbihi'l-a'lâ, gloss:yalnızca en yüce Rabbinin yüzünü arayarak, source:92:20}. Arama fiili {ar:بغيت الشيء إذا طلبته, tr:beğaytü'ş-şey'e izâ talebtüh, gloss:bir şeyi istedim, aradım, source:"ب غ ي,B001"} demektir. Örnek sahnesi kaybolmuş bir devedir: {ar:بغى ضالته, tr:beğâ dâlleteh, gloss:kayıp devesini aradı, source:"ب غ ي,B001"}. Kalıbın kendine has yükü de şöyle söylenir: {ar:الابتغاء خص بالاجتهاد في الطلب, tr:el-ibtiğâu hussa bi'l-ictihâdi fi't-taleb, gloss:ibtiğâ aramada gayret göstermeye özgüdür, source:"ب غ ي,B001"}. Kayıp devesini arayan adam yerinde durmaz. Her tepeye çıkar, her izi okur, gözü hep bir yöne dönüktür. Yüz de bir şeyin önüdür: {ar:الوجه مستقبل لكل شيء, tr:el-vechu müstakbelü külli şey', gloss:yüz her şeyin karşıya bakan önüdür, source:"و ج ه,B001"}. Yüz bir yön de verir: {ar:الوجهة القبلة وشبهها, tr:el-vichetü'l-kıbletü ve şibhuhâ, gloss:vichet kıble ve benzeridir, source:"و ج ه,B002"}. Yüzü Allah'a çevirmek bir deyimdir: {ar:وجهت وجهي لله سبحانه, tr:vecchtü vechî li'llâhi sübhâneh, gloss:yüzümü Allah'a çevirdim, source:"و ج ه,B005"}. Yüz kişinin kendisi yerine de geçer: {ar:ربما عبر عن الذات بالوجه, tr:rubbemâ ubbira ani'z-zâti bi'l-vech, gloss:bazen zat yüzle anlatılır, source:"و ج ه,B004"}. Bu yüzden ayetteki Rabbin yüzü O'nun kendisidir ve aranan şey O'na yönelmenin kendisidir.

On altıncı ayetin fiili aynı hareketin iki yönünü birden taşır. Bu fiil bir şeye yönelmek olabilir: {ar:التولية تكون إقبالا؛ فول وجهك أي وجه وجهك نحوه, tr:et-tevliyetü tekûnü ikbâlen; fe-velli vecheke ey vecchih vecheke nahveh, gloss:tevliye yönelmek de olur; yüzünü çevir demek yüzünü ona doğru döndür demektir, source:"و ل ي,B006"}. Ondan dönüp gitmek de olabilir: {ar:التولية تكون انصرافا, tr:et-tevliyetü tekûnü insırâfâ, gloss:tevliye ayrılıp gitmek de olur, source:"و ل ي,B007"}. Dönüşün iki biçimi de vardır: {ar:التولي قد يكون بالجسم وقد يكون بترك الإصغاء والائتمار, tr:et-tevellî kad yekûnü bi'l-cismi ve kad yekûnü bi-terki'l-ısğâi ve'l-i'timâr, gloss:yüz çevirmek bedenle de olur, kulak vermemek ve buyruğa uymamakla da, source:"و ل ي,B007"}. On altıncı ayetteki kişi bu fiilin dönüp gitme yüzünü taşır. Yirminci ayetteki kişi ise aynı fiilin yönelme yüzünü, kendi fiili olmadan, "yüz" kelimesiyle yapar. İkisi tek bir dönüşün iki ucudur. Dokuzuncu ve on altıncı ayetlerin yalanlama fiili de bu sahnede bir hayvan hareketi olarak duyulur: {ar:كذب الوحشي إذا جرى شوطا ثم وقف لينظر ما وراءه, tr:kezebe'l-vahşiyyu izâ cerâ şavtan sümme vekafe li-yenzura mâ verâeh, gloss:yaban hayvanı bir parça koşup sonra durarak arkasına bakınca kezebe denir, source:"ك ذ ب,B007"}. Yalanlayan koşar ama yüzü hedefte değildir, durup geride bıraktığına bakar. Arayan ise kaybolmuş devesine doğru bakar ve aramayı bırakmaz. Son ayet bu aramanın sonunu verir: {ar:وَلَسَوْفَ يَرْضَىٰ, tr:ve le-sevfe yerdâ, gloss:o elbette hoşnut olacaktır, source:92:21}. Kök {ar:أصل واحد يدل على خلاف السخط, tr:aslun vâhidün yedüllü alâ hılâfi's-suht, gloss:öfkenin karşıtını gösteren tek kök, source:"ر ض و,B001"} demektir. Arama bulmakla, yüz yüzle karşılaşmakla biter.

Kur'an bu üç kelimeyi, yani dönmeyi, yüzü ve hoşnutluğu, tek ayette toplar. Allah Peygambere şöyle der: {ar:قَدْ نَرَىٰ تَقَلُّبَ وَجْهِكَ فِى ٱلسَّمَآءِ ۖ فَلَنُوَلِّيَنَّكَ قِبْلَةًۭ تَرْضَىٰهَا ۚ فَوَلِّ وَجْهَكَ شَطْرَ ٱلْمَسْجِدِ ٱلْحَرَامِ, tr:kad nerâ tekallübe vechike fi's-semâi fe-le-nüvelliyenneke kıbleten terdâhâ fe-velli vecheke şatra'l-mescidi'l-harâm, gloss:yüzünün göğe dönüp durduğunu görüyoruz; seni hoşnut olacağın bir kıbleye çevireceğiz; yüzünü Mescid-i Haram yönüne çevir, source:2:144}. Burada dönmek yönelmektir ve hoşnutlukla biter. Bir başka ayette {ar:فَأَيْنَمَا تُوَلُّوا۟ فَثَمَّ وَجْهُ ٱللَّهِ, tr:fe-eynemâ tüvellû fe-semme vechu'llâh, gloss:nereye dönerseniz Allah'ın yüzü oradadır, source:2:115} denir. Aynı ikili dönüp gitme yönünde de defalarca geçer. Musa ile Harun'a Firavun'a şöyle demeleri öğretilir: {ar:أَنَّ ٱلْعَذَابَ عَلَىٰ مَن كَذَّبَ وَتَوَلَّىٰ, tr:enne'l-azâbe alâ men kezzebe ve tevellâ, gloss:azap yalanlayıp yüz çevirenedir, source:20:48}. Can köprücük kemiğine dayandığında ölen adam için de {ar:فَلَا صَدَّقَ وَلَا صَلَّىٰ, tr:fe-lâ saddaka ve lâ sallâ, gloss:ne doğruladı ne namaz kıldı, source:75:31} ve {ar:وَلَٰكِن كَذَّبَ وَتَوَلَّىٰ, tr:ve lâkin kezzebe ve tevellâ, gloss:ama yalanladı ve yüz çevirdi, source:75:32} denir. Bu iki ayet surenin altıncı ve on altıncı ayetlerini karşı karşıya koyar. Namaz kılan bir kulu engelleyen adam için de aynı söz söylenir: {ar:أَرَءَيْتَ إِن كَذَّبَ وَتَوَلَّىٰٓ, tr:eraeyte in kezzebe ve tevellâ, gloss:ya yalanlar ve yüz çevirirse ne dersin, source:96:13}. Yüzü arayış ise vermeyle birlikte anılır. Allah Peygambere {ar:لَّيْسَ عَلَيْكَ هُدَىٰهُمْ, tr:leyse aleyke hüdâhüm, gloss:onları doğru yola getirmek sana düşmez, source:2:272} der ve aynı ayette müminler için {ar:وَمَا تُنفِقُونَ إِلَّا ٱبْتِغَآءَ وَجْهِ ٱللَّهِ, tr:ve mâ tünfikûne ille'btiğâe vechi'llâh, gloss:ancak Allah'ın yüzünü arayarak harcarsınız, source:2:272} der. Hidayetin kimin üzerine olduğu ile yüzün aranması surede olduğu gibi aynı ayette buluşur. Bir başka ayette sabredenler için {ar:صَبَرُوا۟ ٱبْتِغَآءَ وَجْهِ رَبِّهِمْ, tr:saberu'btiğâe vechi rabbihim, gloss:Rablerinin yüzünü arayarak sabrettiler, source:13:22} denir ve onların harcaması {ar:سِرًّۭا وَعَلَانِيَةًۭ, tr:sirran ve alâniyeten, gloss:gizli ve açık, source:13:22} diye anlatılır. Gizli ve açık, gecenin ve gündüzün işidir. Esirleri ve yoksulları doyuranlar şöyle der: {ar:إِنَّمَا نُطْعِمُكُمْ لِوَجْهِ ٱللَّهِ لَا نُرِيدُ مِنكُمْ جَزَآءًۭ وَلَا شُكُورًا, tr:innemâ nut'imüküm li-vechi'llâhi lâ nürîdü minküm cezâen ve lâ şükûrâ, gloss:sizi yalnızca Allah'ın yüzü için doyuruyoruz; sizden ne karşılık ne teşekkür istiyoruz, source:76:9}. Bu ayet on dokuzuncu ve yirminci ayetlerin hemen hemen aynısıdır: karşılık beklenmez ve yüz aranır. Rablerine sabah akşam dua edenler de {ar:يُرِيدُونَ وَجْهَهُۥ, tr:yürîdûne vecheh, gloss:O'nun yüzünü isterler, source:6:52} diye anılır. Aranan yüzün kalıcılığı da söylenir: {ar:وَيَبْقَىٰ وَجْهُ رَبِّكَ, tr:ve yebkâ vechu rabbik, gloss:Rabbinin yüzü kalır, source:55:27}. Arama ile hoşnutluk başka bir kişide de birleşir: {ar:وَمِنَ ٱلنَّاسِ مَن يَشْرِى نَفْسَهُ ٱبْتِغَآءَ مَرْضَاتِ ٱللَّهِ, tr:ve mine'n-nâsi men yeşrî nefsehü'btiğâe merdâti'llâh, gloss:insanlardan kimi Allah'ın hoşnutluğunu arayarak kendini satar, source:2:207}.

Kaynaklar: 92:9 وَكَذَّبَ ك ذ ب B007; 92:16 كَذَّبَ ك ذ ب B007; 92:16 وَتَوَلَّىٰ و ل ي B006; 92:16 وَتَوَلَّىٰ و ل ي B007; 92:20 ٱبْتِغَآءَ ب غ ي B001; 92:20 وَجْهِ و ج ه B001; 92:20 وَجْهِ و ج ه B002; 92:20 وَجْهِ و ج ه B004; 92:20 وَجْهِ و ج ه B005; 92:21 يَرْضَىٰ ر ض و B001

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

