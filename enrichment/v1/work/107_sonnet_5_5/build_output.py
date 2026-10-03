# -*- coding: utf-8 -*-
"""Build enrichment/v1/out/107/107_enriched.sonnet-5-5.md from the base file + blocks_a/blocks_b.

Writes only to the OUTPUT_MD path. The base file is read, never modified. All annotation lines are
serialised by one function so that the one-line flat grammar is guaranteed.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/Volumes/aro/projects/prose_generation")
BASE = ROOT / "_commentary/v16/out/s107/images.r13.map3.nohft.tool.tool/images.md"
OUT = ROOT / "enrichment/v1/out/107/107_enriched.sonnet-5-5.md"
WORK = ROOT / "enrichment/v1/work/107_sonnet_5_5"
BASE_SHA = "ffa9ec2329ee4a3578ae3272bba40f3d0114191d91553e15cf18809721e4be14"

sys.path.insert(0, str(WORK))
from blocks_a import A  # noqa: E402
from blocks_b import B  # noqa: E402

ENUM_KEYS = {"type", "tradition", "role", "relation", "status", "confidence", "historicity",
             "hadith_grade", "connection", "classical_attestation", "priority", "audience", "canonical"}
ORDER = ["id", "type", "tradition", "ayah", "role", "relation", "status", "confidence", "historicity",
         "hadith_grade", "connection", "classical_attestation", "checked_sources", "canonical",
         "priority", "audience", "scholar", "transmitter", "term", "scope", "source_ref", "origin",
         "attested_in", "reason", "note", "prose", "source"]


def fmt(block):
    unknown = set(block) - set(ORDER)
    assert not unknown, unknown
    parts = []
    for key in ORDER:
        if key not in block:
            continue
        val = block[key]
        if key in ENUM_KEYS:
            assert re.fullmatch(r"[A-Za-z_]+", val), (key, val)
            parts.append(f"{key}:{val}")
        else:
            parts.append(f"{key}:" + json.dumps(val, ensure_ascii=False))
    return "{" + ", ".join(parts) + "}"


HEADER = """<!-- annotation_schema_version:2.0 ; surah:107 ; ayah_scope:107:1-7 ; mode:comprehensive ; language:tr (base preserved) ; base_file:_commentary/v16/out/s107/images.r13.map3.nohft.tool.tool/images.md ; base_sha256:%s ; producer:sonnet-5-5 independent run ; date:2026-10-02 -->

### Okuma katmanları

Aşağıdaki metin, Mâûn Sûresi hakkındaki ana yorumun değiştirilmeden korunmuş hâlidir. Yorum paragraflarının arasına, satır başında süslü parantez ve id alanıyla başlayan tek satırlık bloklar eklenmiştir. Bu bloklar filtrelenebilir kanıt katmanlarıdır: klasik rivâyet ve dirâyet tefsiri, esbâb-ı nüzûl, hadis, kıraat, Mekkî-Medenî tarihi, tarihî bağlam, anlam tarihi, nazm, Kur’an içi paraleller, yöntem ve kaynak notları, projenin kendi sentezine ilişkin yenilik denetimi ve Türkçe meal incelemesi.

Meal incelemesi bloklarını görmek ya da gizlemek için kimliği S107-MEAL- ile başlayan blokları (veya scope alanı meal-review: ile başlayanları) süzün; bunlar klasik kanıt değildir, tradition:historical ve status:interpretive ya da inferred olarak ayrılmıştır. Yenilik denetimi blokları type:novelty ile, reddedilen adaylar role:rejected_candidate ile işaretlidir.

""" % BASE_SHA

REGISTRY = {
    # classical sources
    "TAB-107": "al-Ṭabarī, *Jāmiʿ al-bayān*, Q 107:1-7. Okunan metin: quran.ksu.edu.sa/tafseer/tabary/sura107-aya1.html ... sura107-aya7.html sayfalarından alınmış önbellek metni (work/107_sonnet_5_5/sources/tabary_107_N.txt). Doğrudan alıntılanan yerler kaynak metinle karşılaştırıldı.",
    "TAB-51-11": "al-Ṭabarī, *Jāmiʿ al-bayān*, Q 51:11 (sâhûn fî ġamra). Önbellek metni sources/tabary_51_11.txt; özgün URL önbellek dosyasında kayıtlı değil.",
    "TAB-9-103": "al-Ṭabarī, *Jāmiʿ al-bayān*, Q 9:103 (salât/sekîne, salâteke–salavâtike okuyuşu). Önbellek metni sources/tabary_9_103.txt; özgün URL önbellek dosyasında kayıtlı değil.",
    "KATH-107": "Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*, Q 107:1-7. quran.ksu.edu.sa/tafseer/katheer/sura107-aya1.html ... sura107-aya7.html önbellek metni.",
    "SUY-107": "al-Suyūṭī, *al-Durr al-manthūr*, Q 107:1-7 (rivâyet derlemesi; derleyici adları Süyûtî’nin metnindeki gibi). quran-tafsir.net/seoty/sura107-aya1.html ... aya7 önbellek metni.",
    "KASH-107": "al-Zamakhsharī, *al-Kashshāf*, Q 107:1-7. quran-tafsir.net/zamakhshary/sura107-aya1.html ... aya7 önbellek metni.",
    "RAZI-107": "Fakhr al-Dīn al-Rāzī, *Mafātīḥ al-ghayb*, Q 107:1-7. quran-tafsir.net/alrazy/sura107-aya1.html ... aya7 önbellek metni.",
    "BAYD-107": "al-Bayḍāwī, *Anwār al-tanzīl*, Q 107:1-7. quran-tafsir.net/baidawy/sura107-aya1.html ... aya7 önbellek metni.",
    "BIQ-107": "al-Biqāʿī, *Naẓm al-durar*, Q 107:1-7. quran-tafsir.net/beqaay/sura107-aya1.html ... aya7 önbellek metni (sûre sonu bölümü dahil).",
    "BIQ-106-108": "al-Biqāʿī, *Naẓm al-durar*, Q 108:1 (ve 106:4 sayfasının sonu). Önbellek metinleri sources/beqaay_108_1.txt ve beqaay_106_4.txt; özgün URL önbellek dosyasında kayıtlı değil (aynı sitenin 107 sayfa kalıbı ile aynı olması muhtemeldir, doğrulanmadı).",
    "QURT-107": "al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, Q 107:1-7. quran.ksu.edu.sa/tafseer/qortobi/sura107-aya1.html ... aya7 önbellek metni.",
    "QURT-67-30": "al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*, Q 67:30 (maʿīn). Önbellek metni sources/qortobi_67_30.txt; özgün URL kayıtlı değil.",
    "ALUSI-107": "al-Ālūsī, *Rūḥ al-maʿānī*, yalnızca Q 107:1 ve Q 107:7 sayfaları okundu (sources/alusi_107_1.txt, alusi_107_7.txt); özgün URL önbellek dosyasında kayıtlı değil. Öbür ayet sayfaları okunmadı.",
    "IATIYYA-107": "Ibn ʿAṭiyya, *al-Muḥarrar al-wajīz*, yalnızca Q 107:1 sayfası okundu (sources/ibnatiyya_107_1.txt); özgün URL kayıtlı değil.",
    "WAH-107": "al-Wāḥidī, *Asbāb al-nuzūl*, Q 107:1-2 (3-7 için sayfada “bu kitapta tefsir yok” yazıyor). quranpedia.net/surah/1/107/book/2919 (önbellek: sources/wahidi_107.html).",
    "MAQ-SAHW": "Ibn Fāris, *Muʿjam maqāyīs al-lugha*, madde sahw (sehv, sehvet, suhâ). Önbellek metni sources/maqayis_سهو.txt; kaynak site önbellek dosyasında kayıtlı değil.",
    "MAQ-DAA": "Ibn Fāris, *Muʿjam maqāyīs al-lugha*, madde daʿʿ. Önbellek metni sources/maqayis_دع.txt.",
    "MAQ-HDD": "Ibn Fāris, *Muʿjam maqāyīs al-lugha*, madde ḥaḍḍ. Önbellek metni sources/maqayis_حض.txt.",
    "BASE-LEX": "Baz dosyanın kendi içindeki sözlük alıntıları ve etiketleri (Maqâyîs ve öbür sözlükler; “source:ر ء ي,B001” biçiminde). Bu çalışmada yeniden doğrulanmadı; yalnızca sehv, de‘, hadd maddeleri Maqâyîs’ten kontrol edildi.",
    "MUS-ANAS": "Ṣaḥīḥ Muslim, Kitâbü’l-mesâcid, “tilke salâtü’l-münâfık” hadisi (Enes b. Mâlik, Alâ b. Abdurrahman yoluyla). Birincil sayfa açılamadı (sunnah.com 403); koleksiyon etiketi ve metin özeti surahquran.com/Sharh-Hadith-1759.html sayfasından, Arapça lafız İbn Kesîr’in nakli üzerinden görüldü. Numara kaynaklara göre 622 ya da 623.",
    # meal aggregators
    "AGG-ACIK-107": "acikkuran.com/107/1 ... /107/7 (7 sayfa) ve acikkuran.com/maun-suresi/5-ayet-meali; 2 Ekim 2026’da WebFetch ile alındı. 18 Türkçe yazar listeler (Diyanet, Okuyan, Öztürk, Elmalılı özgün ve sadeleştirilmiş, Ateş, Bulaç, İslamoğlu, Esed, Çantay, Süleymaniye Vakfı, Onan vb.). Araç sayfa özeti döndürür; bu yüzden tek sayfalı alıntılar ikinci bir sayfayla karşılaştırıldı.",
    "AGG-KMEALI-107": "kuranmeali.com/AyetKarsilastirma.php?sure=107&ayet=1 ... 7 (7 sayfa); 2 Ekim 2026’da WebFetch ile alındı. Yaklaşık 48 Türkçe meal listeler (Diyanet Eski ve Yeni, Diyanet Vakfı, Bilmen, Gölpınarlı, Hayrat, Elmalılı, İzmirli vb.).",
    "WEB-DIYANET-107": "kuran.diyanet.gov.tr/mushaf/kuran-meal-2/maun-suresi-107/ayet-1/diyanet-isleri-baskanligi-meali-1 (resmî site; ilk deneme zaman aşımına uğradı, sonraki deneme metni döndürdü) ve hurriyet.com.tr’de Mâûn Suresi Diyanet meali sayfası; iki aggregator ile tutarlı.",
    "WEB-AYETBUL-YNO": "ayetbul.net/sure/107/maun-suresi/yasar-nuri-ozturk; Öztürk meâlinin acikkuran.com varyantını doğrular.",
    # meals
    "MEAL-DIY-107": "Diyanet İşleri Başkanlığı Meali (güncel), Mâûn 1-7; WEB-DIYANET-107 ile doğrulandı.",
    "MEAL-DIYOLD-107": "Diyanet İşleri Meali (Eski), kuranmeali.com’daki etiketle; yalnızca aggregator.",
    "MEAL-OKU-107": "Mehmet Okuyan, Kur’ân-ı Kerîm Meâli; acikkuran.com ve kuranmeali.com.",
    "MEAL-YNO-107": "Yaşar Nuri Öztürk meâli; acikkuran.com ve ayetbul.net bir varyantı, kuranmeali.com başka bir varyantı gösterir; basım ayrımı yapılamadı.",
    "MEAL-ELM-107": "Elmalılı Hamdi Yazır; özgün (“iter yetîmi”, “yardımlığı sakınır”) ve sadeleştirilmiş metin; iki aggregator bu iki metni farklı etiketlerle sunar.",
    "MEAL-BIL-107": "Ömer Nasuhi Bilmen; kuranmeali.com. (Bir arama özeti 2. ayet için farklı bir söz verdi; kullanılmadı.)",
    "MEAL-ATE-107": "Süleyman Ateş; acikkuran.com ve kuranmeali.com.",
    "MEAL-HAY-107": "Hayrat Neşriyat; kuranmeali.com (ayrıca bir arama özeti).",
    "MEAL-GOL-107": "Abdülbaki Gölpınarlı; kuranmeali.com.",
    "MEAL-BUL-107": "Ali Bulaç; acikkuran.com ve kuranmeali.com.",
    "MEAL-DVK-107": "Diyanet Vakfı Meali; kuranmeali.com.",
    "MEAL-SUL-107": "Süleymaniye Vakfı Meali; acikkuran.com ve kuranmeali.com (iki farklı metin varyantı; 107:4 için bir metin acikkuran.com’da “Eski” etiketli).",
    "MEAL-ISL-107": "Mustafa İslamoğlu; acikkuran.com ve kuranmeali.com (107:1 için iki varyant).",
    "MEAL-ESED-107": "Muhammed Esed’in Türkçe çevirisi (çevirmen adı sayfalarda görünmedi); acikkuran.com ve kuranmeali.com.",
    "MEAL-CAN-107": "Hasan Basri Çantay; acikkuran.com ve kuranmeali.com.",
    "MEAL-ONAN-107": "Gültekin Onan; acikkuran.com.",
    "MEAL-IZM-107": "İsmail Hakkı İzmirli; kuranmeali.com.",
    "MEAL-IKT-107": "acikkuran.com’da “İbni Kesir” etiketiyle sunulan Türkçe metin; hangi çeviriye ait olduğu sayfalarda belirtilmedi ve doğrulanmadı.",
    "MEAL-YUK-107": "Edip Yüksel; yalnızca bir arama sonucu özeti (sayfalar 403 ve 500 verdi); düşük güven; yalnızca teyit amaçlı.",
}

CRITIQUE = """### Kaynak-eleştiri notu

1. Klasik kaynak metinleri ayet sayfası düzeyinde okundu; tam ciltler ya da el yazması düzeyinde bir inceleme yapılmadı. Âlûsî, İbn Atıyye ve Vâhidî için okunan bölümler kısmidir (bkz. S107-SRC-001). Tekrarlayan nakiller (örneğin İbn Kesîr ve Kurtubî’nin Taberî’den, Kurtubî’nin Zemahşerî’den aldıkları) bağımsız tanık sayılmamış ve ayrı bloklarla çoğaltılmamıştır.
2. Hadis dereceleri yalnızca kaynaklardaki eleştirmen ifadesi varsa verilmiştir: Ebû Berze rivayeti için İbn Kesîr ve Süyûtî’nin zayıflık kaydı, Kurre b. Dı‘mûs rivayeti için İbn Kesîr’in kaydı; Sa‘d rivayetinin merfû‘ ve mevkûf biçimleri tartışmalı bırakılmış; Sahîh-i Müslim hadisi koleksiyon etiketine dayanır ve ayrıca derecelendirilmemiştir; öbürleri not_assessed’tır. Birincil hadis sayfalarına erişilemedi (sunnah.com 403).
3. Meal metinleri web’den, bir sayfa özetleme aracı üzerinden alınmıştır; bu yüzden küçük sapmalar olabilir. Bir söz yalnızca ikinci bir sayfada ya da resmî sitede doğrulandığında ya da iki sayfada tutarlı olduğunda kullanılmıştır. Öztürk ve Süleymaniye Vakfı için iki ayrı metin varyantı vardır; hangisinin hangi basım olduğu belirlenemedi. Celal Yıldırım bulunamadı ve ona söz atfedilmedi; Edip Yüksel yalnızca dolaylı kaynakla görüldü.
4. “Yenilik” bloklarındaki “bulunmadı” ifadeleri yalnızca taranan 107. sûre ayet sayfaları ve adı geçen birkaç ek sayfa için geçerlidir (checked_sources alanı). Başka klasik eserlerde paralel bulunabilir; kontrol edilen derlem genişledikçe sonuçlar değişebilir.
5. Baz metindeki sözlük alıntıları yeniden doğrulanmadı; yalnızca sehv, de‘ ve hadd maddeleri Maqâyîs’ten kontrol edildi ve iki nokta için not düşüldü (S107-MET-004, S107-MET-005). Baz metindeki “veyl” tanımı “memory” kaynak etiketi taşır; bu çalışma ona klasik dayanak (Taberî, Kurtubî, Râzî, Bikâî) sağlamıştır (S107-SEM-007) ve baz metne dokunmamıştır.
6. Çıkarım ya da yorum olan her blok bunu status alanıyla (inferred, interpretive) belirtir. Meal incelemesi hükümleri (“hata”, “yanıltıcı”, “savunulabilir daraltma”) Arapça metne ve toplanan klasik/lugat kanıtına dayanan editoryal değerlendirmelerdir; çevirmenlerin niyetini hükme bağlamaz.

**Novelty denetiminde taranan klasik derlem:** Tabari, İbn Kesîr, Süyûtî (ed-Durr), Zemahşerî, Râzî, Beyzâvî, Bikâî, Kurtubî, Âlûsî (107:1, 107:7), İbn Atıyye (107:1), Vâhidî (107:1-2); ek olarak ilgili yerlerde Taberî 9:103 ve 51:11, Kurtubî 67:30, Bikâî 106:4 ve 108:1, Maqâyîs.

Sürüm: annotation_schema_version 2.0; 2 Ekim 2026.
"""


def main():
    base_bytes = BASE.read_bytes()
    assert hashlib.sha256(base_bytes).hexdigest() == BASE_SHA, "base sha mismatch"
    base = base_bytes.decode("utf-8")
    lines = base.split("\n")
    # collect inserts keyed by anchor, preserving order within A then B (stable)
    inserts = {}
    for anchor, blk in A + B:
        inserts.setdefault(anchor, []).append(blk)
    out = [HEADER.rstrip("\n"), ""]
    # top blocks (anchor 0)
    for blk in inserts.get(0, []):
        out.append(fmt(blk))
    out.append("")
    # base with local inserts
    for idx, line in enumerate(lines, 1):
        out.append(line)
        if idx in inserts and idx != 0:
            out.append("")
            for blk in inserts[idx]:
                out.append(fmt(blk))
    text = "\n".join(out)
    if not text.endswith("\n"):
        text += "\n"
    text = text.rstrip("\n") + "\n\n## Kaynak kayıtları\n\n"
    for key, desc in REGISTRY.items():
        text += f"- **{key}** — {desc}\n"
    text += "\n" + CRITIQUE
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(text, encoding="utf-8")
    print("written", OUT, len(text))


if __name__ == "__main__":
    main()
