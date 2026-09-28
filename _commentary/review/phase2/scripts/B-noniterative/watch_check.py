"""Evaluation only: are the ingredients each watch case needs present in the targeted supply (supply/<S_A>.md)?

Nothing here enters a prompt; the checks are generic string/section tests on the script-built supply.
Each check: (case, ingredient, section, regex). Result table printed and written to watch_check.txt.
"""
import re, os
import load

SUP = os.path.join(load.OUT, "supply")


def section(txt, name):
    m = re.search(rf"^## {re.escape(name)}.*?(?=^## |\Z)", txt, re.S | re.M)
    return m.group(0) if m else ""


CHECKS = [
    # 29:38 neighbour-activated rare branch
    ("29:38", "sabal eye-film branch shown with its early definition", "Branch index", r"^- س ب ل B010 .*نسج العنكبوت"),
    ("29:38", "zayyana's adorning branches in the same reader's view", "Branch index", r"^- ز ي ن B00[23] "),
    ("29:38", "seeing branches (mustabṣirīn) in the same view", "Branch index", r"^- ب ص ر B0\d\d "),
    ("29:38", "kohl branch of ṣadda (fa-ṣaddahum) in the same view", "Branch index", r"^- ص د د B\d+ .*كحل"),
    ("29:38", "join: eye-film definition -> ʿankabūt at 29:41", "Definitional", r"س ب ل B010 .*ع ن ك ب.*29:41"),
    ("29:38", "join: eye-film 'ghishāwa' -> 2:7 / 45:23 (sight covered)", "Definitional", r"س ب ل B010 .*غ ش و.*2:7.*45:23"),
    # 18:86 loaded word
    ("18:86", "ḥamaʾ concordance: 15:26, 15:28, 15:33 with ṣalṣāl", "Concordance", r"15:26:\d+ .*صَلْصَٰل[\s\S]*15:28:[\s\S]*15:33:"),
    ("18:86", "usage profile: ḥamaʾ with ṣalṣāl 3/.. and masnūn 3/..", "Usage profiles", r"ح م ء: .*س ن ن 3/6.*ص ل ص ل 3/6"),
    ("18:86", "ʿayn as sun disk branch", "Branch index", r"^- ع ي ن B008 .*الشمس"),
    ("18:86", "no inter-ayah relevance label anywhere in the supply", None, r"^(?![\s\S]*no value)"),
    # 18:96 loaded word
    ("18:96", "nafakha concordance (20 uses) incl. 15:29, 38:72, 32:9", "Concordance", r"ن ف خ \(20 occurrences\)[\s\S]*15:29[\s\S]*32:9[\s\S]*38:72"),
    ("18:96", "usage profile: nafakha with rūḥ 5/9 and ṣūr 6/8", "Usage profiles", r"ن ف خ: .*ص و ر 6/8.*ر و ح 5/9"),
    # 5:6 North Star example ingredients (contaminated case; evaluation only)
    ("5:6", "mirfaq leaning branch", "Branch index", r"^- ر ف ق B004 .*الاتكاء"),
    ("5:6", "kaʿb -> Kaʿba branch", "Branch index", r"^- ك ع ب B002 .*الكعبة"),
    ("5:6", "same-surah echoes: kaʿb at 5:95 and 5:97", "Same-surah", r"ك ع ب \(\d+\): .*5:95 .*5:97 "),
    ("5:6", "same-surah echoes: q-w-m at 5:8 and 5:97", "Same-surah", r"ق و م \(\d+\): .*5:8 .*5:97 "),
    # 4:34 guard + loaded words
    ("4:34", "ḍaraba B002 travel marked collocation, construction absent", "Branch index", r"^- ض ر ب B002 \[collocation\].*present in this ayah: no"),
    ("4:34", "husband's nushūz echo at 4:128", "Same-surah", r"ن ش ز \(\d+\): .*4:128 "),
    ("4:34", "qawwām echo at 4:135 and 4:5", "Same-surah", r"ق و م \(\d+\): .*4:5 .*4:135 "),
    # 1:6 (contaminated; evaluation only)
    ("1:6", "ṣirāṭ swallowing branch", "Branch index", r"^- ص ر ط B002 .*البلع"),
    ("1:6", "q-w-m well-frame branch", "Branch index", r"^- ق و م B012 .*بئر"),
]

rows = []
for ref, what, sec, rx in CHECKS:
    f = os.path.join(SUP, ref.replace(":", "_") + ".md")
    txt = open(f, encoding="utf-8").read()
    body = section(txt, sec) if sec else txt
    ok = bool(re.search(rx, body, re.M))
    rows.append((ref, what, sec or "whole supply", "present" if ok else "MISSING"))

out = ["case | ingredient | section | result", "---|---|---|---"] + [" | ".join(r) for r in rows]
out.append(f"\n{sum(r[3] == 'present' for r in rows)} of {len(rows)} ingredients present")
txt = "\n".join(out)
open(os.path.join(load.OUT, "watch_check.txt"), "w").write(txt + "\n")
print(txt)
