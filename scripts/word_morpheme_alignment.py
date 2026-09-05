"""Conservative, ordered alignment of analytic words to canonical morphemes.

Only spans shared by every best whole-ayah alignment are returned. Source
wording and IDs stay unchanged; spelling equivalences affect matching only.
"""

from array import array
import re
import unicodedata


ARABIC_TAG = re.compile(r"\{\{ar:([^}]*)\}\}")
ALEF_FOLD = str.maketrans({"ٱ": "ا", "أ": "ا", "إ": "ا", "آ": "ا", "ى": "ي", "ئ": "ء", "ؤ": "ء"})
ALIGNMENT_VERSION = "ordered-morpheme-spans-v2"


def coverage(spans, unresolved, morphology, linguistic_source_ref=None):
    """Shared coverage for new generation and migration of stored bundles."""
    skips = [span["morpheme_skip_count"] for span in spans if span]
    histogram = {}
    for skip in skips:
        histogram[str(skip)] = histogram.get(str(skip), 0) + 1
    result = {
        "present": bool(morphology.get("present")) and bool(skips),
        "source_file": morphology.get("source_file"),
        "alignment_version": ALIGNMENT_VERSION,
        "words_total": len(spans),
        "words_resolved": len(skips),
        "words_unresolved": len(unresolved),
        "morpheme_skip_total": sum(skips),
        "morpheme_skip_max": max(skips, default=0),
        "morpheme_skip_histogram": histogram,
        "unresolved": unresolved,
        "morphemes_tsv": morphology,
        "note": (
            "Ordered surface alignment within canonical QAC words; only spans "
            "shared by all best alignments are joined. Upstream word-analysis "
            "identities and wording are preserved. Unresolved analytic units "
            "remain available for qualified reading; never infer their QAC "
            "identity from upstream numbering."
        ),
    }
    if linguistic_source_ref:
        result["linguistic_source_ref"] = linguistic_source_ref
    return result


def surface_forms(text, *, followed_by_suffix=False):
    """Preserve both written and expanded Quranic superscript-alif spellings."""
    forms = {""}
    normalized = unicodedata.normalize("NFC", text)
    for index, char in enumerate(normalized):
        if char in "أإآ":
            equivalents = {"ا", "ءا" if char == "آ" else "ء"}
            forms = {value + letter for value in forms for letter in equivalents}
        elif char == "ٰ":
            preceding = normalized[index - 1] if index else ""
            if preceding == "ى":
                # Medial maqsura can become alif (هُدَىٰها -> هداها), including
                # before a separately recorded suffix. Preserve final إلى/إلا.
                if followed_by_suffix or any(
                    "ء" <= letter <= "ي" and letter != "ـ"
                    for letter in normalized[index + 1:]
                ):
                    forms |= {value[:-1] + "ا" for value in forms if value.endswith("ى")}
                continue
            if preceding == "و":
                # Bare waw can be the Uthmani long-alif seat (صلوٰة).
                forms |= {value[:-1] + "ا" for value in forms if value.endswith("و")}
            else:
                # A vocalized consonantal waw is retained (وَٰحد != أحد).
                forms |= {value + "ا" for value in forms}
        elif char == "۟":
            # Quranic zero marks an orthographic letter as unpronounced.
            # Keep the written form as well as its annotation-derived reading.
            forms |= {value[:-1] for value in forms if value.endswith("ا")}
        elif char in "ۥۦ":
            forms |= {value + ("و" if char == "ۥ" else "ي") for value in forms}
        elif char in "ٕٔ":
            forms = {value + "ء" for value in forms}
        elif (unicodedata.category(char) in {"Mn", "Cf"} or char.isspace()
              or char == "ـ" or 0x06D6 <= ord(char) <= 0x06ED):
            continue
        else:
            forms = {value + char for value in forms}
    return {value.translate(ALEF_FOLD) for value in forms}


def _word_ref(row):
    return ":".join(row["qac_ref"].split(":")[:3])


def _source_spans(rows):
    indexed = {}
    forms = [surface_forms(row["surface_ar"], followed_by_suffix=(
        index + 1 < len(rows) and rows[index + 1].get("pos") == "PRON"
        and _word_ref(rows[index + 1]) == _word_ref(row)
        and bool(surface_forms(rows[index + 1]["surface_ar"]) - {""})
    )) for index, row in enumerate(rows)]
    for index, row in enumerate(rows):
        if row.get("pos") == "DET" and "ل" in forms[index]:
            forms[index].add("ال")  # contracted article after li-, still typed DET
        if row.get("pos") == "SUB" and row.get("lemma_ar"):
            forms[index] |= surface_forms(row["lemma_ar"])
        if row.get("pos") == "PRON" and "و" in forms[index]:
            forms[index].add("وا")  # plural suffix with/without orthographic alif
        if (index and row.get("pos") in {"PN", "REL"}
                and rows[index - 1].get("pos") == "P"
                and "ل" in forms[index - 1]
                and _word_ref(rows[index - 1]) == _word_ref(row)):
            lemma = surface_forms(row.get("lemma_ar", ""))
            forms[index] |= {value for value in lemma if value.startswith("ال")
                             and value[2:] in forms[index]}
            if row.get("pos") == "REL" and any(value.startswith("ال") for value in lemma):
                forms[index] |= {"ا" + value for value in forms[index] if value.startswith("ل")}
    for start in range(len(rows)):
        if not forms[start] - {""}:
            continue
        combined = {""}
        for end in range(start + 1, len(rows) + 1):
            if _word_ref(rows[end - 1]) != _word_ref(rows[start]):
                break
            combined = {left + right for left in combined for right in forms[end - 1]}
            # Elided/empty morphemes remain with their preceding surface, never
            # leak into a following substantive QAC word.
            if end < len(rows) and "" in forms[end] and _word_ref(rows[end]) == _word_ref(rows[start]):
                continue
            for form in combined - {""}:
                indexed.setdefault(form, set()).add((start, end))
    return indexed


def resolve(wa_record, rows):
    words = wa_record.get("words", []) or []
    surfaces = [ARABIC_TAG.search(word.get("surface_display") or "") for word in words]
    targets = [surface_forms(match[1]) - {""} if match else set() for match in surfaces]
    source = _source_spans(rows)
    matches = []
    for target in targets:
        by_start = {}
        for form in target:
            for start, end in source.get(form, ()):
                by_start.setdefault(start, set()).add(end)
        matches.append(by_start)

    n, m = len(words), len(rows)
    # Maximize matched analytic words, then their spelling length. Do not use
    # upstream word numbering or semantic importance to choose an occurrence.
    lengths = [min(map(len, forms), default=0) for forms in targets]
    base = sum(lengths) + 1
    rewards = [base + length for length in lengths]
    best = [array("i", [0]) * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            best[i][j] = max(best[i + 1][j], best[i][j + 1], *(
                rewards[i] + best[i + 1][end] for end in matches[i].get(j, ())
            ))

    options = [set() for _ in words]
    reachable = bytearray(m + 1)
    reachable[0] = 1
    for i in range(n):
        following = bytearray(m + 1)
        for j in range(m + 1):
            if not reachable[j]:
                continue
            if best[i][j] == best[i + 1][j]:
                options[i].add(None)
                following[j] = 1
            if j < m and best[i][j] == best[i][j + 1]:
                reachable[j + 1] = 1
            for end in matches[i].get(j, ()):
                if best[i][j] == rewards[i] + best[i + 1][end]:
                    options[i].add((j, end))
                    following[end] = 1
        reachable = following

    spans, unresolved = [], []
    previous_end = 0
    for index, choices in enumerate(options):
        if len(choices) != 1 or None in choices:
            spans.append(None)
            unresolved.append({
                "word_index": index,
                "surface_ar": surfaces[index][1] if surfaces[index] else "",
                "reason": (
                    "no Arabic surface in surface_display" if not targets[index]
                    else "ambiguous occurrence across best ordered source alignments" if len(choices) > 1
                    else "no compatible span in the best ordered source alignment"
                ),
            })
            continue
        start, end = next(iter(choices))
        selected = rows[start:end]
        spans.append({
            "word_index": index,
            "surface_ar": surfaces[index][1],
            "word_ids": sorted({row["word_id"] for row in selected}),
            "qac_refs": [row["qac_ref"] for row in selected],
            "morpheme_ids": [row["morpheme_id"] for row in selected],
            "aligned_qac_word_ref_upstream": words[index].get("aligned_qac_word_ref"),
            "morpheme_skip_count": start - previous_end,
        })
        previous_end = end
    return spans, unresolved
