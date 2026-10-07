# Worked passage packet

Page ID: `example-1-6`. Assigned paragraphs: `p09`, `p12` only. This is a complete
three-perspective worked pass for these selected paragraphs, not a completed
scan of the entire commentary page. Paragraph numbering below is the blank-line
block position in the identified source; it is frozen for this fixture.

## Original commentary (unchanged)

Source, relative to repository root:
`_commentary/v16/out/1_6/D/1_6.reading.tr.md`.

### p09

Fiil kişiler arasında da ince bir yer değiştirme yapar. Beşinci ayette "sen" iki kez, cümlenin başına çekilerek vurgulanmıştı: iyyâke... iyyâke. Şimdi o "sen" hiç söylenmez, emir kipinin içine gizlenir. "Biz" ise fiile sesli bir ek olarak bağlanır: -nâ. Biçim bakımından bu bir emirdir. Ama kulun ağzından yukarıya yöneldiğinde Arapçada emir kipi yakarışa dönüşür. Namazı tek başına kılan da "bizi" der; "kulluk ederiz" ve "yardım isteriz" cümlelerindeki çoğul burada da sürer.

### p12

İkinci kelime {ar:ٱلصِّرَٰطَ, tr:es-sırât, gloss:yol} yol demektir; Râgıb onu özellikle "dosdoğru yol" diye tanımlar. Sözlükler kelimeyi üç söyleyişle kaydeder: sırât, sirât ve zırât. Kıraatler arasında da s ile okuyuş ve z'ye çalan bir okuyuş vardır.

Evidence scope:

- p09: focus 1:6, with ihdi and -nâ; comparison 1:5, with the two iyyâke expressions
  and the person marking in naʿbüdü/nestaʿîn. “Beşinci ayette” resolves to 1:5 in this
  Fatiha discussion; “şimdi” refers to the focus 1:6.
- p12: focus 1:6, with ṣirâṭ and its following adjective. The ṣ/s/z expressions are
  dictionary forms; their attribution to a Quranic reading needs separate evidence.

The following paragraph discusses an etymological proposal; it is outside this
fixture's assignment. No comparison with other ayat is needed for these two paragraphs.

## Local ayat

`Quran:1:5`: إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ

`Quran:1:6`: ٱهْدِنَا ٱلصِّرَٰطَ ٱلْمُسْتَقِيمَ

Exact text source: `../quran-data/data/text/quran-uthmani.tsv`.

## Morphological evidence

Source: `../quran-data/data/morphology/qac.sqlite.gz`, `qac_morphemes` table.
The following locators resolve directly to that table. These feature records
support morphology; by themselves they do not prove a rhetorical interpretation.

| Locator | Arabic | Root | Features |
|---|---|---|---|
| QAC:1:5:1:1 | إِيَّاكَ | — | STEM, POS:PRON, LEM:<iy~aA, 2MS |
| QAC:1:5:2:1 | نَعْبُدُ | ع ب د | STEM, POS:V, IMPF, LEM:Eabada, ROOT:Ebd, 1P |
| QAC:1:5:3:1 | وَ | — | PREFIX, w:CONJ+ |
| QAC:1:5:3:2 | إِيَّاكَ | — | STEM, POS:PRON, LEM:<iy~aA, 2MS |
| QAC:1:5:4:1 | نَسْتَعِينُ | ع و ن | STEM, POS:V, IMPF, (X), LEM:{sotaEiynu, ROOT:Ewn, 1P |
| QAC:1:6:1:1 | ٱهْدِ | ه د ي | STEM, POS:V, IMPV, LEM:hadaY, ROOT:hdy, 2MS |
| QAC:1:6:1:2 | نَا | — | SUFFIX, PRON:1P |
| QAC:1:6:2:1 | ٱل | — | PREFIX, Al+ |
| QAC:1:6:2:2 | صِّرَٰطَ | ص ر ط | STEM, POS:N, LEM:Sira`T, ROOT:SrT, M, ACC |
| QAC:1:6:3:1 | ٱلْ | — | PREFIX, Al+ |
| QAC:1:6:3:2 | مُسْتَقِيمَ | ق و م | STEM, POS:ADJ, ACT, PCPL, (X), LEM:m~usotaqiym, ROOT:qwm, M, ACC |

## Local construction and speaking context

`Construction:1:6`: ihdi is a second-person singular imperative and -nâ is the
first-person plural object suffix; the addressee is expressed by the imperative
form. The shared n- in naʿbüdü and nestaʿîn marks first-person plural in these
specific imperfect forms, not a shared root. The paragraph supplies the speaking
context: the reciter addresses God in a prayer.

`Construction:1:5`: each iyyâke is a separate object expression placed before its
own verb. This supports teaching object position and repetition. It does not, by
itself, establish a universal rule that all fronting means restriction.

`Attachment:1:6:2-3`: the dictionary entry's `occurrence_evidence.occurrences` row
with `qac_ref=1:6:2:2` records ṣirâṭ as a direct object and its link to the following
adjective. The QAC records both noun and adjective as masculine accusative, with
el- prefixes. Preserve these local relations without deriving a new path metaphor.

## Dictionary branch evidence

Selected branch: `root_000858/B001`. Its QAC occurrence record includes 1:6:2:2.
This is sufficient for the branch-level examples below. No unverified lexical-unit
ID is assigned to the occurrence.

The full entry for this fixture is the upstream entry named by the reviewed gloss
result's `source_entry.path`:
`../dictionary/v2/work/entry_creation/root_000858/tr/output/root_000858_entry.json`.
The reviewed gloss result is:
`../dictionary/v2/gloss_generation/results/tr/root_000858.json`.
Only semantic excerpts are copied here, without their build apparatus.

Locators of the form `Dictionary:root_000858/B001#field` refer to fields in the
selected entry branch. `Gloss:root_000858/B001#field` refers to the reviewed gloss
branch. `Reading:1:6:article` below is the supplied editorial reading note.

```json
{
  "branch_ref": "root_000858/B001",
  "identity_judgment": {
    "status": "qualified",
    "rationale": "Kaynak ifadesi bu dalın temel anlamını genel olarak yol diye verir; düz yol ise bu temel anlamın özellikle öne çıkan bir türüdür. Bu nedenle yalnızca düz yolla sınırlı bir dal kimliği kaynak ifadesini gereğinden fazla daraltır.",
    "boundary_note": "Dal, genel yol anlamını kapsar; düz yol anlamı bunun içinde özel olarak vurgulanan kullanımdır."
  },
  "lexicalization_scope": {
    "branch_kind": "bare",
    "note": "Tanım yalın dal anlamıyla sınırlıdır ve herhangi bir kalıba özgü ek anlamı genel anlama taşımaz."
  },
  "branch_image_ar": "الطريق المستقيم",
  "what_is_ar": "يدخل فيه الصراط والسراط والزراط بمعنى الطريق، وخاصة الطريق المستقيم",
  "what_is_not_ar": "لا يدخل فيه بلع الطعام ولا السيف القاطع إلا من جهة الاشتقاق أو الاشتراك في لفظ السراط عند مقاييس",
  "source_phrase_ar": "الصراط والسراط والزراط: الطريق (sihah)؛ الصراط: الطريق المستقيم؛ ويقال له سراط (mufradat)؛ صرط من باب الإبدال وقد ذكر في السين وهو الطريق (maqayis 2074)؛ بعض أهل العلم يقول السراط مشتق من ذلك لأن الذاهب فيه يغيب (maqayis 1774)",
  "sources": [
    "SI",
    "MU",
    "MQ"
  ],
  "concept_map": {
    "definition": "Bir yerden başka bir yere gitmeye yarayan yol; bu genel anlam içinde özellikle doğrultusu düzgün olan yol.",
    "facets": [
      {
        "facet_id": "F001",
        "role": "core",
        "statement": "Temel gönderim, üzerinde ilerlenen yoldur.",
        "claim_ids": [
          "bc_001"
        ]
      },
      {
        "facet_id": "F002",
        "role": "specialization",
        "statement": "Yolun düz ve sapmasız olması özellikle öne çıkarılabilir.",
        "claim_ids": [
          "bc_001"
        ]
      },
      {
        "facet_id": "F003",
        "role": "source_variant",
        "statement": "Aynı yol anlamı, kaynakta üç ayrı söyleniş biçimiyle tanıklanır.",
        "claim_ids": [
          "bc_001"
        ]
      }
    ]
  },
  "concept_gloss": {
    "text": "yol, özellikle düz yol",
    "applicability": "Genel yol anlamını ve kaynaklarda öne çıkan düz yol özelleşmesini birlikte karşılayan ana anlatımdır.",
    "error_profile": {
      "fit": "none",
      "preserves": "Hem genel yol çekirdeğini hem de düz yol özelleşmesini korur.",
      "loses": null,
      "adds": null,
      "collision": null
    },
    "facet_ids": [
      "F001",
      "F002"
    ]
  },
  "contextual_glosses": [
    {
      "text": "yol",
      "usage_role": "general",
      "applicability": "Bağlam yalnızca bir güzergahı gösteriyor ve yolun düzlüğünü ayrıca belirtmiyorsa doğal karşılıktır.",
      "error_profile": {
        "fit": "narrowing",
        "preserves": "Üzerinde ilerlenen yol çekirdeğini eksiksiz korur.",
        "loses": "Düz ve sapmasız yolun özellikle vurgulanmasını açıkça söylemez.",
        "adds": null,
        "collision": null
      },
      "facet_ids": [
        "F001"
      ]
    },
    {
      "text": "düz yol",
      "usage_role": "contextual",
      "applicability": "Bağlam yolun doğrultusunun düzgün olduğunu özellikle öne çıkarıyorsa uygun karşılıktır.",
      "error_profile": {
        "fit": "narrowing",
        "preserves": "Yol çekirdeğini ve düz olma özelliğini birlikte korur.",
        "loses": "Düzlük belirtilmeden kullanılan genel yol kapsamını dışarıda bırakır.",
        "adds": null,
        "collision": null
      },
      "facet_ids": [
        "F001",
        "F002"
      ]
    }
  ],
  "excluded_glosses": [
    {
      "text": "doğru yol",
      "category": "confusable",
      "error_profile": {
        "fit": "displacement",
        "preserves": "Düz ve sapmasız yol düşüncesini kısmen korur.",
        "loses": "Düzlük belirtilmeyen genel yol anlamını geri plana iter.",
        "adds": "Ahlakça veya düşüncece doğru olma yorumunu çağrıştırabilir.",
        "collision": "Fiziksel doğrultu ile değer yargısı anlamındaki doğruluk karışabilir."
      }
    }
  ]
}
```

Reviewed gloss excerpt:

```json
{
  "branch_ref": "root_000858/B001",
  "concept_gloss": {
    "text": "geçilen yol, düz yol",
    "facet_ids": [
      "F001",
      "F002",
      "F003"
    ],
    "error": {
      "fit": "none",
      "loses_facet_ids": [],
      "adds": null,
      "collision": null,
      "reason": null
    }
  },
  "contextual_glosses": [
    {
      "text": "üzerinde ilerlenen yol",
      "facet_ids": [
        "F001",
        "F003"
      ],
      "lexical_unit_ids": [
        "lu_001",
        "lu_002",
        "lu_003"
      ],
      "error": {
        "fit": "narrowing",
        "loses_facet_ids": [
          "F002"
        ],
        "adds": null,
        "collision": null,
        "reason": "Bu gloss, yolun düz ve sapmasız olma özelleşmesini açıkça taşımaz."
      }
    },
    {
      "text": "sapmasız düz yol",
      "facet_ids": [
        "F001",
        "F002",
        "F003"
      ],
      "lexical_unit_ids": [
        "lu_001",
        "lu_002"
      ],
      "error": {
        "fit": "none",
        "loses_facet_ids": [],
        "adds": null,
        "collision": null,
        "reason": null
      }
    }
  ]
}
```

## Reading note and open evidence

`Reading:1:6:article`: the written el- before ṣ in ṣirâṭ is pronounced with
assimilation, hence es-sırât in the paragraph's accessible Turkish spelling.
The verse's noun has an accusative ending; the paragraph's es-sırât is a lexical
or pause-style citation. For the local adjective connection show es-sırâta. Do not
attribute this ending difference to a different root or to the s/z variants.

The dictionary lists ṣ/s/z lexical variants, but this packet supplies no named
qiraat witness or attribution for their use in 1:6. Preserve the opportunity to
teach a *specific Quranic reading variant* in deferred; lexical variants alone
do not establish that attribution. Ordinary word/branch lessons can proceed.
