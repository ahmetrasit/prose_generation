#!/usr/bin/env python3
"""What the enrichment corpus holds and what it does not (user, 2026-10-05: "record what we have and what we don't
have"). Regenerate after any import:  python3 -B enrichment/v2/tools/source_status.py
Writes enrichment/v2/SOURCES_STATUS.md from every source.json, the index (corpus.sqlite) and groups.json, plus the
list below of works searched for and not held (kept by hand: each line says where it stands).
"""
from __future__ import annotations

import json
import sqlite3
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import corpus as C  # noqa: E402

OUT = C.PG / "enrichment" / "v2" / "SOURCES_STATUS.md"

# Works searched for (2026-10-05) and not held as text; a line per work: why, and what would unblock it.
NOT_HELD = [
    ("al-Khūlī, Manāhij tajdīd (1961)", "KHULI (pointer)", "scan only; OCR pilots (Luna, Sol, two-witness, crops) "
     "below preservation quality. Deferred by the user (method covered by Bint al-Shāṭiʾ's preface and two secondary "
     "studies). Unblock: a typed edition (Ktab/VitalSource: fixed layout, unverified) or human review of PDF 273–320."),
    ("Khalafallah, al-Fann al-qaṣaṣī fī al-Qurʾān", "—", "typed PDF (Muhammadanism.org) whose text layer reverses phrase "
     "order and uses «آ» as a space filler; archive OCR noisy. Unblock: OCR of the rendered PDF pages (clean type)."),
    ("Shukrī ʿAyyād, Min waṣf al-Qurʾān yawm al-dīn wa-l-ḥisāb", "—", "scan + archive OCR only "
     "(archive.org 20260313_20260313_0237)."),
    ("Bint al-Shāṭiʾ, al-Qurʾān wa-qaḍāyā al-insān; Maqāl fī al-insān", "—", "scans + archive OCR only."),
    ("al-Sāmarrāʾī, ʿAlā ṭarīq al-tafsīr al-bayānī (2 vols, incl. al-Fātiḥa)", "—", "701 image pages, not on Shamela."),
    ("al-Sāmarrāʾī, al-Taʿbīr al-qurʾānī; Asʾila bayāniyya; Balāghat al-kalima; Murāʿāt al-maqām", "—", "PDFs without "
     "usable text (no characters, garbled or reversed layers); archive OCR garbles the Qurʾān quotations. Overlap "
     "with Lamasāt and Asrār al-bayān, which are held."),
    ("Iṣlāḥī, Tadabbur-i Qurʾān surahs 1–5 and 9", "ISLAHI-TADABBUR (part)", "Urdu vols 1–2 and the English surah 9 "
     "file are scans without text: OCR_NEEDED.md."),
    ("ʿAbduh, Tafsīr Juzʾ ʿAmma; Muqātil, al-Ashbāh wa-l-naẓāʾir; Ibn Khālawayh, Mukhtaṣar; Farāhī, Niẓām al-Qurʾān; "
     "Badawi–Haleem Dictionary; TDK Tarama Sözlüğü", "pointers with scans", "scans downloaded, no usable text "
     "layer: OCR_NEEDED.md (the user handles OCR)."),
    ("Ambros, Concise Dictionary; Neuwirth, Der Koran 1; Farrin, Structure and Qur'anic Interpretation; "
     "M. Öztürk meal", "pointers", "not in the download batch (the user was checking them); the Farrin and Öztürk "
     "PDFs lie unregistered at the corpus root."),
]


def main() -> None:
    con = sqlite3.connect(C.INDEX)
    stats = {src: (n, ch, tied) for src, n, ch, tied in con.execute(
        "SELECT src, count(*), sum(length(text)), sum(s IS NOT NULL) FROM seg GROUP BY src")}
    cites = dict(con.execute("SELECT seg.src, count(DISTINCT ref.seg_id) FROM ref JOIN seg ON seg.id=ref.seg_id "
                             "GROUP BY seg.src"))
    groups = json.loads((C.PG / "enrichment" / "v2" / "groups.json").read_text())["groups"]
    member = {}
    for g in groups:
        for s in g["sources"]:
            member.setdefault(s, []).append(g["id"])
    srcs = [m for m in C.sources() if m.get("kind") != "intertext"]
    for m in srcs:
        if m.get("kind") in ("meal", "translation", "tafsir_tr") and m["id"] not in member:
            member[m["id"]] = ["meal (by kind)"] if m.get("kind") in ("meal", "translation") else []
    held = [m for m in srcs if m.get("access") != "hafiza"]
    pointers = [m for m in srcs if m.get("access") == "hafiza"]
    total_seg = sum(stats.get(m["id"], (0, 0, 0))[0] for m in held)
    total_ch = sum(stats.get(m["id"], (0, 0, 0))[1] or 0 for m in held)
    no_group = [m["id"] for m in held if not member.get(m["id"]) and m.get("kind") not in ("quran",)]
    lines = [
        "# Enrichment corpus: what we have and what we don't",
        "",
        f"Generated {date.today().isoformat()} by `enrichment/v2/tools/source_status.py` from every `source.json`, "
        "the index and `groups.json`. Regenerate after any import.",
        "",
        f"- **Held as text:** {len(held)} sources, {total_seg:,} segments, {total_ch:,} characters "
        f"(index {sum(v[0] for v in stats.values()):,} segments incl. intertext).",
        f"- **Pointers only (model memory):** {len(pointers)}.",
        f"- **Held but in no enrichment group yet:** {len(no_group)} (Task C1: the hybrid workflow reads by group).",
        "",
        "Status words: **typed** = born-digital or edition text; **typed, unchecked** = a digital edition not yet "
        "checked against the print; **OCR draft** = machine reading, do not quote; flags travel with every segment "
        "(`corpus.py` prints them).",
        "",
        "## Held as text, by kind",
        "",
    ]
    by_kind: dict[str, list] = {}
    for m in held:
        by_kind.setdefault(m.get("kind") or "?", []).append(m)
    for kind in sorted(by_kind, key=lambda k: (-len(by_kind[k]), k)):
        ms = sorted(by_kind[kind], key=lambda m: m["id"])
        if kind == "meal":
            n = sum(stats.get(m["id"], (0, 0, 0))[0] for m in ms)
            lines += [f"### meal ({len(ms)} Turkish translations, {n:,} segments)", "",
                      ", ".join(m["id"].replace("MEAL-", "") for m in ms), ""]
            new = [m for m in ms if (m.get("ingestion") or {}).get("date")]
            if new:
                lines += ["Imported from the user's downloads (2026-10-05): " + "; ".join(
                    f"{m['id']} ({(m.get('coverage') or '')[:40]})" for m in new), ""]
            continue
        lines += [f"### {kind} ({len(ms)})", "", "| Source | Work | Segments | Tied to ayat | Citing ayat | Status "
                  "| Group |", "|---|---|---:|---:|---:|---|---|"]
        for m in ms:
            n, ch, tied = stats.get(m["id"], (0, 0, 0))
            ing = m.get("ingestion") or {}
            status = ing.get("text_status") or ing.get("quality") or ""
            if not status:
                status = "typed" if not ing else "see ingestion"
            status = status.replace("|", "/")[:70]
            title = f"{(m.get('author') or '')[:28]}, {(m.get('title') or '')[:42]}".strip(", ")
            lines.append(f"| {m['id']} | {title} | {n:,} | {tied or 0:,} | {cites.get(m['id'], 0):,} | {status} | "
                         f"{', '.join(member.get(m['id'], [])) or '**none**'} |")
        lines.append("")
    lines += ["## Pointers only (no text held; anything cited is model memory)", "",
              "| Source | Work | Why | Group |", "|---|---|---|---|"]
    for m in sorted(pointers, key=lambda m: m["id"]):
        acq = (m.get("acquisition") or {}).get("state")
        why = "scan downloaded, no usable text (OCR_NEEDED.md)" if acq == "raw_downloaded" else "not acquired"
        if m["id"] == "KHULI":
            why = "scan held; deferred by the user (OCR below preservation quality)"
        lines.append(f"| {m['id']} | {(m.get('author') or '')[:28]}, {(m.get('title') or '')[:50]} | {why} | "
                     f"{', '.join(member.get(m['id'], [])) or '—'} |")
    lines += ["", "## Searched for and not held (or held only in part)", "", "| Work | Corpus ID | Where it stands |",
              "|---|---|---|"]
    lines += [f"| {w} | {i} | {s} |" for w, i, s in NOT_HELD]
    lines += ["", "## Held but in no enrichment group yet", "",
              "These are searchable (`corpus.py get/ayah/search/cites`) but the hybrid workflow (grup.py, Task C) "
              "reads by group, so a group must claim them before a run:", "", ", ".join(sorted(no_group)) or "none", ""]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(C.PG)}: {len(held)} held, {len(pointers)} pointers, {len(no_group)} in no group")


if __name__ == "__main__":
    main()
