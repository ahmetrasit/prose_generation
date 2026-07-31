#!/usr/bin/env python3
"""Prepare quran-data detailed commentary for Turkish TTS.

This script is intentionally offline.  It reads finalized Markdown from
quran-data, converts inline Arabic/gloss annotations, and writes clean text,
chunk metadata, and Google TTS request JSON.  It never calls the TTS service.
"""

import argparse
from decimal import Decimal, InvalidOperation, ROUND_CEILING
import fcntl
import hashlib
import json
import os
import re
from pathlib import Path


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
QURAN_DATA_ROOT = WORKSPACE_ROOT.parent / "quran-data"
# Writing into quran-data is deliberate and therefore requires an explicit
# --out-root.  A bare invocation is safe and stays inside this repository.
DEFAULT_OUT_ROOT = WORKSPACE_ROOT / "_audio" / "audio"
UNKNOWN_REMOTE_OUTCOMES = {"in_flight", "unknown"}
INPUT_COST_PER_MILLION_CHARS = Decimal("1")
QURAN_TEXT_PATH = QURAN_DATA_ROOT / "data" / "text" / "quran-uthmani.tsv"

SURAH_DETAILED_PREFIX = ("data", "commentary", "surah", "detailed", "tr")
AYAH_DETAILED_PREFIX = ("data", "commentary", "ayah", "detailed", "tr")

SURAH_FILE_RE = re.compile(r"^(?P<surah>\d{1,3})\.surah-reading\.tr\.md$")
AYAH_FILE_RE = re.compile(
    r"^(?P<surah>\d{1,3})_(?P<ayah>\d+)\.prose\.tr\.md$"
)

# These are the Turkish display names used in spoken Ayah references.  They
# are intentionally separate from the English/transliterated names in the
# source Quran resources, because the TTS label is Turkish prose.
SURAH_NAMES_TR = {
    1: "Fatiha",
    2: "Bakara",
    3: "Âl-i İmrân",
    4: "Nisâ",
    5: "Mâide",
    6: "En'âm",
    7: "A'râf",
    8: "Enfâl",
    9: "Tevbe",
    10: "Yûnus",
    11: "Hûd",
    12: "Yûsuf",
    13: "Ra'd",
    14: "İbrâhîm",
    15: "Hicr",
    16: "Nahl",
    17: "İsrâ",
    18: "Kehf",
    19: "Meryem",
    20: "Tâhâ",
    21: "Enbiyâ",
    22: "Hac",
    23: "Mü'minûn",
    24: "Nûr",
    25: "Furkân",
    26: "Şuarâ",
    27: "Neml",
    28: "Kasas",
    29: "Ankebût",
    30: "Rûm",
    31: "Lokmân",
    32: "Secde",
    33: "Ahzâb",
    34: "Sebe",
    35: "Fâtır",
    36: "Yâsîn",
    37: "Sâffât",
    38: "Sâd",
    39: "Zümer",
    40: "Mü'min",
    41: "Fussilet",
    42: "Şûrâ",
    43: "Zuhruf",
    44: "Duhân",
    45: "Câsiye",
    46: "Ahkâf",
    47: "Muhammed",
    48: "Fetih",
    49: "Hucurât",
    50: "Kâf",
    51: "Zâriyât",
    52: "Tûr",
    53: "Necm",
    54: "Kamer",
    55: "Rahmân",
    56: "Vâkıa",
    57: "Hadîd",
    58: "Mücâdele",
    59: "Haşr",
    60: "Mümtehine",
    61: "Saf",
    62: "Cuma",
    63: "Münâfikûn",
    64: "Teğâbün",
    65: "Talâk",
    66: "Tahrîm",
    67: "Mülk",
    68: "Kalem",
    69: "Hâkka",
    70: "Meâric",
    71: "Nûh",
    72: "Cin",
    73: "Müzzemmil",
    74: "Müddessir",
    75: "Kıyâmet",
    76: "İnsan",
    77: "Mürselât",
    78: "Nebe",
    79: "Nâziât",
    80: "Abese",
    81: "Tekvîr",
    82: "İnfitar",
    83: "Mutaffifîn",
    84: "İnşikâk",
    85: "Bürûc",
    86: "Târık",
    87: "A'lâ",
    88: "Gâşiye",
    89: "Fecr",
    90: "Beled",
    91: "Şems",
    92: "Leyl",
    93: "Duhâ",
    94: "İnşirâh",
    95: "Tîn",
    96: "Alak",
    97: "Kadr",
    98: "Beyyine",
    99: "Zilzâl",
    100: "Âdiyât",
    101: "Kâria",
    102: "Tekâsür",
    103: "Asr",
    104: "Hümeze",
    105: "Fîl",
    106: "Kureyş",
    107: "Mâûn",
    108: "Kevser",
    109: "Kâfirûn",
    110: "Nasr",
    111: "Tebbet",
    112: "İhlâs",
    113: "Felak",
    114: "Nâs",
}

TURKISH_CARDINAL_UNITS = (
    "sıfır",
    "bir",
    "iki",
    "üç",
    "dört",
    "beş",
    "altı",
    "yedi",
    "sekiz",
    "dokuz",
)
TURKISH_CARDINAL_TENS = {
    10: "on",
    20: "yirmi",
    30: "otuz",
    40: "kırk",
    50: "elli",
    60: "altmış",
    70: "yetmiş",
    80: "seksen",
    90: "doksan",
}
TURKISH_ORDINAL_UNITS = {
    1: "birinci",
    2: "ikinci",
    3: "üçüncü",
    4: "dördüncü",
    5: "beşinci",
    6: "altıncı",
    7: "yedinci",
    8: "sekizinci",
    9: "dokuzuncu",
}
TURKISH_ORDINAL_TENS = {
    10: "onuncu",
    20: "yirminci",
    30: "otuzuncu",
    40: "kırkıncı",
    50: "ellinci",
    60: "altmışıncı",
    70: "yetmişinci",
    80: "sekseninci",
    90: "doksanıncı",
}

# The canonical files use ``gloss:``, while the earlier workflow description
# also used ``:gloss:``.  Accept both spellings, but require all three fields
# and reject any unbalanced or unknown annotation content.
INLINE_TOKEN_RE = re.compile(
    r"\{\s*ar\s*:\s*(?P<arabic>[^{}\n]*?)\s*,\s*"
    r"tr\s*:\s*(?P<transliteration>[^{}\n]*?)\s*,\s*"
    r":?\s*gloss\s*:\s*(?P<gloss>[^{}\n]*?)\s*\}",
    re.IGNORECASE,
)
BRACE_CANDIDATE_RE = re.compile(r"\{[^{}\n]*\}")
UNKNOWN_GLOSS_FIELD_RE = re.compile(
    r",\s*:?\s*[A-Za-z_][A-Za-z0-9_-]*\s*:",
    re.IGNORECASE,
)


PROMPT = (
    "Speak as a warm, conversational Turkish narrator addressing one curious "
    "listener. Sound like a thoughtful person sharing a discovery as it becomes "
    "clear, with natural human cadence, varied sentence energy, and quiet "
    "curiosity. Let short reveal sentences land, then slow slightly for "
    "explanation. Use clear Istanbul Turkish diction and natural pauses. Avoid "
    "sermon, classroom lecture, documentary-announcer delivery, exaggerated "
    "drama, and a repeated rhetorical rise-and-fall. Do not give every section "
    "the same cadence. Pronounce Arabic Quranic words naturally as Arabic, then "
    "return smoothly to Turkish."
)

RECITATION_PROMPT = (
    "Read only the exact text in the text field. The text field is the complete "
    "script. Do not repeat, add, explain, translate, paraphrase, or continue it. "
    "Stop immediately after the final Arabic word. Say the Turkish surah label "
    "once, then recite the Arabic Quran text once, with a short natural pause "
    "after the colon."
)

AUDIO_CONFIG = {
    "audioEncoding": "LINEAR16",
    "pitch": 0,
    "speakingRate": 1,
}

VOICE = {
    "languageCode": "tr-TR",
    "modelName": "gemini-3.1-flash-tts-preview",
    "name": "Rasalgethi",
}


def normalize_surah_id(value):
    value_text = str(value).strip()
    match = re.search(r"(?:^|[/\\])s0*(\d{1,3})(?:[/\\]|$)", value_text, re.IGNORECASE)
    if not match:
        match = re.search(r"(?:^|[/\\])(?P<number>\d{1,3})[._]", value_text)
    if not match and re.fullmatch(r"s?0*\d{1,3}", value_text, re.IGNORECASE):
        match = re.match(r"s?0*(?P<number>\d{1,3})", value_text, re.IGNORECASE)
    if not match:
        raise ValueError(f"Could not infer surah id from: {value}")
    number = match.groupdict().get("number") or match.group(1)
    number = int(number)
    if not 1 <= number <= 114:
        raise ValueError(f"Surah number is outside 1..114: {number}")
    return f"S{number:03d}"


def turkish_cardinal(number):
    """Return a Turkish cardinal number for the Ayah range we support."""

    if type(number) is not int or not 0 <= number <= 999999:
        raise ValueError(f"Turkish cardinal number is outside 0..999999: {number}")
    if number < 10:
        return TURKISH_CARDINAL_UNITS[number]

    thousands, remainder = divmod(number, 1000)
    parts = []
    if thousands:
        parts.append("bin" if thousands == 1 else f"{turkish_cardinal(thousands)} bin")

    hundreds, remainder = divmod(remainder, 100)
    if hundreds:
        parts.append("yüz" if hundreds == 1 else f"{TURKISH_CARDINAL_UNITS[hundreds]} yüz")

    tens, units = divmod(remainder, 10)
    if tens:
        parts.append(TURKISH_CARDINAL_TENS[tens * 10])
    if units:
        parts.append(TURKISH_CARDINAL_UNITS[units])
    return " ".join(parts)


def turkish_ordinal(number):
    """Return a Turkish ordinal number, e.g. 5 -> ``beşinci``."""

    if type(number) is not int or not 1 <= number <= 999999:
        raise ValueError(f"Turkish ordinal number is outside 1..999999: {number}")
    if number < 10:
        return TURKISH_ORDINAL_UNITS[number]
    if number < 100 and number in TURKISH_ORDINAL_TENS:
        return TURKISH_ORDINAL_TENS[number]

    thousands, remainder = divmod(number, 1000)
    if remainder == 0:
        prefix = "" if thousands == 1 else f"{turkish_cardinal(thousands)} "
        return f"{prefix}bininci"

    hundreds, remainder = divmod(remainder, 100)
    prefix_parts = []
    if thousands:
        prefix_parts.append("bin" if thousands == 1 else f"{turkish_cardinal(thousands)} bin")
    if hundreds:
        if remainder == 0:
            hundred_prefix = "yüzüncü" if hundreds == 1 else f"{TURKISH_CARDINAL_UNITS[hundreds]} yüzüncü"
            return " ".join([*prefix_parts, hundred_prefix])
        prefix_parts.append("yüz" if hundreds == 1 else f"{TURKISH_CARDINAL_UNITS[hundreds]} yüz")
    prefix = " ".join(prefix_parts)

    if remainder in TURKISH_ORDINAL_TENS:
        ordinal = TURKISH_ORDINAL_TENS[remainder]
    elif remainder < 10:
        ordinal = TURKISH_ORDINAL_UNITS[remainder]
    else:
        tens, units = divmod(remainder, 10)
        ordinal = f"{TURKISH_CARDINAL_TENS[tens * 10]} {TURKISH_ORDINAL_UNITS[units]}"
    return f"{prefix} {ordinal}".strip()


def surah_name_tr(number):
    try:
        return SURAH_NAMES_TR[number]
    except KeyError as error:
        raise ValueError(f"No Turkish surah name is configured for: {number}") from error


def load_quran_text(path=QURAN_TEXT_PATH):
    """Load canonical Uthmani Arabic text keyed by ``surah:ayah``."""

    path = Path(path).expanduser().resolve()
    if not path.is_file():
        raise ValueError(f"Canonical Quran text file does not exist: {path}")

    verses = {}
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            reference, arabic = line.split("|", 1)
        except ValueError as error:
            raise ValueError(f"Malformed Quran text row at {path}:{line_number}") from error
        reference = reference.strip().lstrip("\ufeff")
        arabic = arabic.strip().lstrip("\ufeff")
        if not re.fullmatch(r"\d{1,3}:\d+", reference) or not arabic:
            raise ValueError(f"Malformed Quran text row at {path}:{line_number}")
        if reference in verses:
            raise ValueError(f"Duplicate Quran text reference at {path}:{line_number}: {reference}")
        verses[reference] = arabic
    if not verses:
        raise ValueError(f"Canonical Quran text file is empty: {path}")
    return verses


def source_reference(path):
    try:
        return path.resolve().relative_to(QURAN_DATA_ROOT).as_posix()
    except ValueError:
        return str(path.resolve())


def replace_inline_tokens(text, location="inline text"):
    """Replace {ar:..., tr:..., gloss:...} with Arabic (gloss).

    The transliteration is deliberately parsed and discarded.  Malformed or
    partially parsed annotation markers fail loudly instead of leaking into
    speech requests.
    """

    def replacement(match):
        token = match.group(0)
        parsed = INLINE_TOKEN_RE.fullmatch(token)
        if not parsed:
            raise ValueError(f"Malformed Arabic annotation in {location}: {token}")

        arabic = parsed.group("arabic").strip()
        transliteration = parsed.group("transliteration").strip()
        gloss = parsed.group("gloss").strip()
        if not arabic:
            raise ValueError(f"Empty Arabic field in {location}")
        if not transliteration:
            raise ValueError(f"Empty transliteration field in {location}")
        if not gloss:
            raise ValueError(f"Empty gloss field in {location}")
        if UNKNOWN_GLOSS_FIELD_RE.search(gloss):
            raise ValueError(f"Unknown field in Arabic annotation in {location}: {token}")
        return f"{arabic} ({gloss})"

    if "{" in text or "}" in text:
        if text.count("{") != text.count("}"):
            raise ValueError(f"Unbalanced Arabic annotation braces in {location}")
        candidates = list(BRACE_CANDIDATE_RE.finditer(text))
        if len(candidates) != text.count("{"):
            raise ValueError(f"Malformed or nested Arabic annotation in {location}")
        converted, count = BRACE_CANDIDATE_RE.subn(replacement, text)
        return converted, count
    return text, 0


def count_inline_tokens(text):
    return sum(1 for _ in INLINE_TOKEN_RE.finditer(text))


def clean_inline(text):
    text, _ = replace_inline_tokens(text)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = replace_rank_labels(text)
    text = text.replace("**", "")
    text = text.replace("__", "")
    text = re.sub(r"(?<!\*)\*(?!\*)", "", text)
    text = re.sub(r"(?<!_)_(?!_)", "", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = remove_inline_rank_strength(text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"\s+([,.;:!?])", r"\1", text)
    return text.strip()


def sentence_punctuate(text):
    text = text.strip()
    if text.endswith((".", "!", "?", ":", ";", "؛", "؟")):
        return text
    return f"{text}."


def section_title_text(text):
    text = clean_inline(text)
    return re.sub(r"[.!?;:؛؟]+$", "", text).strip()


def rank_label_title(content):
    if "—" in content:
        content = content.split("—", 1)[1]
    return re.sub(r"\s+", " ", content).strip()


def rank_label_text(content):
    return sentence_punctuate(rank_label_title(content))


def replace_rank_labels(text):
    def repl(match):
        content = match.group(1).strip()
        if not re.search(r"\b(GÜÇLÜ|ORTA|ZAYIF)\b", content):
            return match.group(0)
        return rank_label_text(content)

    return re.sub(r"\[([^\]\n]+)\]", repl, text)


def remove_inline_rank_strength(text):
    return re.sub(
        r"\b(?:GÜÇLÜ|ORTA|ZAYIF)\s*/\s*[A-Z](?:-[\wçğıöşüÇĞİÖŞÜ]+)?"
        r"(?:\s+düzeyinde(?:dir)?)?\b",
        "",
        text,
    )


def split_rank_labeled_paragraph(text):
    matches = list(re.finditer(r"\[([^\]\n]+)\]", text))
    rank_matches = [
        match
        for match in matches
        if re.search(r"\b(GÜÇLÜ|ORTA|ZAYIF)\b", match.group(1))
    ]
    if not rank_matches:
        cleaned = clean_inline(text)
        return [cleaned] if cleaned else []

    segments = []
    prefix = text[: rank_matches[0].start()].strip()
    if prefix:
        segments.append(prefix)

    for index, match in enumerate(rank_matches):
        end = rank_matches[index + 1].start() if index + 1 < len(rank_matches) else len(text)
        label = rank_label_text(match.group(1).strip())
        body = text[match.end() : end].strip()
        segments.append(f"{label} {body}".strip())

    cleaned_segments = []
    for segment in segments:
        cleaned = clean_inline(segment)
        if cleaned:
            cleaned_segments.append(cleaned)
    return cleaned_segments


def strip_list_marker(line):
    line = re.sub(r"^\s*[-+*]\s+", "", line)
    line = re.sub(r"^\s*\d+[.)]\s+", "", line)
    return line


def atomic_write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f".{path.name}.tmp")
    tmp_path.write_text(text, encoding="utf-8")
    os.replace(tmp_path, path)


class CollectionLock:
    """Coordinate preparation with synthesis for one output collection."""

    def __init__(self, collection_dir):
        self.path = collection_dir / ".tts-generation.lock"
        self.handle = None

    def __enter__(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.is_symlink():
            raise ValueError(f"Refusing symlinked collection lock: {self.path}")
        self.handle = self.path.open("a+", encoding="utf-8")
        try:
            fcntl.flock(self.handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as error:
            self.handle.close()
            self.handle = None
            raise RuntimeError(f"Another TTS process holds the collection lock: {self.path}") from error
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.handle is not None:
            fcntl.flock(self.handle.fileno(), fcntl.LOCK_UN)
            self.handle.close()
            self.handle = None


def stable_json(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def reject_duplicate_json_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"Duplicate JSON object key: {key}")
        result[key] = value
    return result


def strict_json_loads(value):
    return json.loads(value, object_pairs_hook=reject_duplicate_json_keys)


def cleanup_unreferenced_files(paths):
    for directory, referenced in paths:
        if not directory.exists():
            continue
        referenced = {path.resolve() for path in referenced}
        for path in directory.glob("*"):
            if path.is_file() and path.resolve() not in referenced:
                path.unlink()


def ensure_paths_disjoint(source, output):
    source = source.resolve()
    output = output.resolve()
    try:
        source.relative_to(output)
        overlaps = True
    except ValueError:
        try:
            output.relative_to(source)
            overlaps = True
        except ValueError:
            overlaps = False
    if overlaps:
        raise ValueError(f"Source and output paths overlap: source={source} output={output}")


def ensure_output_within_root(root, output):
    root = root.resolve()
    output = output.resolve()
    try:
        output.relative_to(root)
    except ValueError as error:
        raise ValueError(f"Output collection escapes --out-root: {output}") from error


def reject_symlink_components(path, field):
    """Reject existing symlinks before resolving a path for output writes."""

    path = Path(path).expanduser()
    if not path.is_absolute():
        path = Path.cwd() / path
    current = Path(path.anchor)
    for part in path.parts[1:]:
        current /= part
        if current.is_symlink():
            raise ValueError(f"Refusing symlinked {field} component: {current}")


def reject_unresolved_remote_outcomes(out_dir):
    """Never overwrite a collection while a prior request may have been sent."""

    unresolved = []
    chunks_path = out_dir / "chunks.jsonl"
    manifest_path = out_dir / "manifest.json"
    for path in (chunks_path, manifest_path):
        if path.is_symlink():
            raise ValueError(f"Refusing symlinked existing artifact: {path}")

    if chunks_path.exists():
        try:
            for line_number, line in enumerate(
                chunks_path.read_text(encoding="utf-8").splitlines(), start=1
            ):
                if not line.strip():
                    continue
                record = strict_json_loads(line)
                if not isinstance(record, dict):
                    raise ValueError("chunk record is not an object")
                if record.get("remoteOutcome") in UNKNOWN_REMOTE_OUTCOMES:
                    unresolved.append(f"{chunks_path}:{line_number}")
        except (OSError, json.JSONDecodeError, ValueError) as error:
            raise ValueError(
                f"Cannot safely reprepare existing chunks file: {chunks_path}"
            ) from error

    def scan_manifest(value, location):
        if isinstance(value, dict):
            if value.get("remoteOutcome") in UNKNOWN_REMOTE_OUTCOMES:
                unresolved.append(location)
            for key, child in value.items():
                scan_manifest(child, f"{location}.{key}")
        elif isinstance(value, list):
            for index, child in enumerate(value):
                scan_manifest(child, f"{location}[{index}]")

    if manifest_path.exists():
        try:
            scan_manifest(
                strict_json_loads(manifest_path.read_text(encoding="utf-8")),
                str(manifest_path),
            )
        except (OSError, json.JSONDecodeError, ValueError) as error:
            raise ValueError(
                f"Cannot safely reprepare existing manifest: {manifest_path}"
            ) from error

    if unresolved:
        raise ValueError(
            "Refusing to overwrite a collection with unresolved remote outcomes: "
            + ", ".join(unresolved)
            + ". Reconcile the outcome explicitly before preparing again."
        )


def heading_text(line):
    return clean_inline(re.sub(r"^#{1,6}\s+", "", line).strip())


def bracket_tts_prefix(line):
    content = line.strip()[1:-1].strip()
    return rank_label_text(content)


def flush_paragraph(lines):
    text = " ".join(strip_list_marker(line).strip() for line in lines)
    return split_rank_labeled_paragraph(text)


def parse_markdown_publication(source):
    """Parse one detailed Markdown file into titled prose sections."""

    raw_lines = source.read_text(encoding="utf-8").splitlines()
    sections = []
    current = None
    paragraph_lines = []
    pending_subsection_title = None
    skip_fenced = False
    skip_html_comment = False
    in_frontmatter = raw_lines[:1] == ["---"]
    frontmatter_open = in_frontmatter

    def ensure_section(title):
        nonlocal current
        title = section_title_text(title)
        current = {"title": title, "paragraphs": []}
        current["paragraphs"].append({"kind": "section_title", "text": title})
        sections.append(current)

    def flush_into_current():
        nonlocal paragraph_lines, pending_subsection_title
        texts = flush_paragraph(paragraph_lines) if paragraph_lines else []
        paragraph_lines = []
        if pending_subsection_title:
            if texts:
                texts[0] = f"{pending_subsection_title} {texts[0]}".strip()
            pending_subsection_title = None
        for text in texts:
            if current is None:
                ensure_section("Anlatım")
            current["paragraphs"].append({"kind": "paragraph", "text": text})

    def start_subsection(title):
        nonlocal pending_subsection_title
        flush_into_current()
        pending_subsection_title = title

    for line in raw_lines:
        stripped = line.strip()

        if in_frontmatter:
            if frontmatter_open:
                frontmatter_open = False
                continue
            if stripped == "---":
                in_frontmatter = False
            continue

        if skip_html_comment:
            if "-->" in stripped:
                skip_html_comment = False
                stripped = stripped.split("-->", 1)[1].strip()
                if not stripped:
                    continue
            else:
                continue

        if stripped.startswith("<!--"):
            if "-->" not in stripped:
                skip_html_comment = True
                continue
            stripped = stripped.split("-->", 1)[1].strip()
            if not stripped:
                continue

        if stripped.startswith("```"):
            skip_fenced = not skip_fenced
            continue
        if skip_fenced:
            continue
        if not stripped:
            if not pending_subsection_title:
                flush_into_current()
            continue

        h_match = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if h_match:
            flush_into_current()
            title = heading_text(stripped)
            if title.casefold() in {
                "bulgular",
                "ana bulgular",
                "tamamlayıcı bulgular",
                "ince kayıtlar",
            }:
                continue
            if re.match(r"^\[[^\n]+\]$", title):
                start_subsection(bracket_tts_prefix(title))
                continue
            ensure_section(title)
            continue

        bold_match = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", stripped)
        if bold_match and re.match(
            r"^\[[^\]\n]*\b(GÜÇLÜ|ORTA|ZAYIF)\b[^\]\n]*\]$",
            bold_match.group(1).strip(),
        ):
            start_subsection(bracket_tts_prefix(bold_match.group(1).strip()))
            rest = bold_match.group(2).strip()
            if rest:
                paragraph_lines.append(rest)
            continue

        bold_prefixed_label_match = re.match(
            r"^\*\*[^*]+?\*\*\s*"
            r"(\[[^\]\n]*\b(?:GÜÇLÜ|ORTA|ZAYIF)\b[^\]\n]*\])\s*(.*)$",
            stripped,
        )
        if bold_prefixed_label_match:
            start_subsection(bracket_tts_prefix(bold_prefixed_label_match.group(1)))
            rest = bold_prefixed_label_match.group(2).strip()
            if rest:
                paragraph_lines.append(rest)
            continue

        if re.match(r"^\[[^\n]+\]$", stripped):
            start_subsection(bracket_tts_prefix(stripped))
            continue

        paragraph_lines.append(line)

    flush_into_current()
    return sections


def parse_ayah_paragraphs(source):
    """Flatten one ayah prose file to prose paragraphs, excluding its wrapper."""

    sections = parse_markdown_publication(source)
    paragraphs = []
    for section in sections:
        paragraphs.extend(
            paragraph
            for paragraph in section["paragraphs"]
            if paragraph["kind"] != "section_title"
        )
    if not paragraphs:
        raise ValueError(f"Ayah source has no prose paragraphs: {source}")
    return paragraphs


def infer_source_kind(source):
    try:
        relative = source.resolve().relative_to(QURAN_DATA_ROOT)
    except ValueError as error:
        raise ValueError(f"Source must be inside quran-data: {source}") from error

    if relative.parts[: len(SURAH_DETAILED_PREFIX)] == SURAH_DETAILED_PREFIX:
        return "surah"
    if relative.parts[: len(AYAH_DETAILED_PREFIX)] == AYAH_DETAILED_PREFIX:
        return "ayah"
    raise ValueError(
        f"Source must be under data/commentary/surah/detailed/tr or "
        f"data/commentary/ayah/detailed/tr: {source}"
    )


def validate_source_file(path, kind):
    if kind == "surah":
        if not SURAH_FILE_RE.match(path.name):
            raise ValueError(
                f"Surah detailed source must match <surah>.surah-reading.tr.md: {path}"
            )
    elif not AYAH_FILE_RE.match(path.name):
        raise ValueError(
            f"Ayah detailed source must match <surah>_<ayah>.prose.tr.md: {path}"
        )


def validate_source_identity(source, files, kind):
    expected_surah = int(normalize_surah_id(str(source))[1:])
    if source.is_dir() and not re.fullmatch(r"s0*\d{1,3}", source.name, re.IGNORECASE):
        raise ValueError(f"Source directory must be named sNNN: {source}")

    for path in files:
        if kind == "surah":
            actual_surah = int(SURAH_FILE_RE.match(path.name).group("surah"))
        else:
            actual_surah = int(AYAH_FILE_RE.match(path.name).group("surah"))
        if actual_surah != expected_surah:
            raise ValueError(
                f"Source filename surah {actual_surah} does not match "
                f"the source directory surah {expected_surah}: {path}"
            )


def collect_source_files(source, kind):
    source = source.expanduser().resolve()
    if not source.exists():
        raise ValueError(f"Source does not exist: {source}")
    if infer_source_kind(source) != kind:
        raise ValueError(f"Source kind mismatch for {source}: expected {kind}")

    if source.is_file():
        validate_source_file(source, kind)
        files = [source]
        validate_source_identity(source, files, kind)
        return files

    if source.name.casefold() == "tr":
        raise ValueError(
            f"Pass one surah directory (sNNN), not the entire locale directory: {source}"
        )

    if kind == "surah":
        files = sorted(
            path for path in source.iterdir() if path.is_file() and SURAH_FILE_RE.match(path.name)
        )
        if len(files) != 1:
            raise ValueError(
                f"Expected exactly one surah-reading source in {source}, found {len(files)}"
            )
    else:
        files = sorted(
            (path for path in source.iterdir() if path.is_file() and AYAH_FILE_RE.match(path.name)),
            key=lambda path: (
                int(AYAH_FILE_RE.match(path.name).group("surah")),
                int(AYAH_FILE_RE.match(path.name).group("ayah")),
            ),
        )
        if not files:
            raise ValueError(f"No ayah prose sources found in {source}")

    for path in files:
        validate_source_file(path, kind)
    validate_source_identity(source, files, kind)
    return files


def build_sections(source_files, kind, quran_text=None, collection=None):
    if kind == "surah":
        sections = parse_markdown_publication(source_files[0])
        for section in sections:
            section["kind"] = "surah_detailed"
            section["grades"] = []
        if not sections:
            raise ValueError(f"Surah source has no readable sections: {source_files[0]}")
        return sections

    if quran_text is None:
        quran_text = load_quran_text()
    sections = []
    for source in source_files:
        match = AYAH_FILE_RE.match(source.name)
        surah_number = int(match.group("surah"))
        ayah_number = int(match.group("ayah"))
        ayah_reference = f"{surah_number}:{ayah_number}"
        try:
            arabic_text = quran_text[ayah_reference]
        except KeyError as error:
            raise ValueError(
                f"Canonical Quran text has no entry for {ayah_reference}: {source}"
            ) from error
        title = (
            f"{surah_name_tr(surah_number)} {ayah_number}"
            if collection == "ayah-recitation"
            else f"{surah_name_tr(surah_number)} {turkish_ordinal(ayah_number)} ayet"
        )
        paragraphs = (
            [{"kind": "ayah_recitation", "text": arabic_text}]
            if collection == "ayah-recitation"
            else parse_ayah_paragraphs(source)
        )
        sections.append(
            {
                "title": title,
                "kind": "ayah_recitation" if collection == "ayah-recitation" else "ayah_detailed",
                "grades": [],
                "ayah": ayah_reference,
                "arabicText": arabic_text,
                "source": source_reference(source),
                "paragraphs": [
                    {"kind": "section_title", "text": title},
                    *paragraphs,
                ],
            }
        )
    return sections


def write_clean_markdown(path, sections):
    lines = []
    for index, section in enumerate(sections, start=1):
        heading = "#" if index == 1 else "##"
        lines.append(f"{heading} {section['title']}")
        lines.append("")
        for paragraph in section["paragraphs"]:
            if paragraph["kind"] == "section_title":
                continue
            lines.append(paragraph["text"])
            lines.append("")
    atomic_write_text(path, "\n".join(lines).rstrip() + "\n")


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_request(text, prompt=PROMPT):
    return {
        "audioConfig": AUDIO_CONFIG,
        "input": {
            "prompt": prompt,
            "text": text,
        },
        "voice": VOICE,
    }


def tts_text_for(paragraph):
    text = paragraph["text"]
    if paragraph["kind"] != "section_title":
        return text
    if text.endswith((".", "!", "?", ":", ";", "؛", "؟")):
        return text
    return f"{text}."


def audio_units_for(section):
    """Return source paragraphs and their spoken text.

    Surah headings are spoken as part of the first prose paragraph. Ayah
    commentary prose is emitted without a synthetic ayah label. Ayah
    recitation sections emit one joined label-and-Arabic unit.
    """

    if section.get("kind") == "ayah_recitation":
        references = [
            paragraph
            for paragraph in section["paragraphs"]
            if paragraph["kind"] == "ayah_recitation"
        ]
        if len(references) != 1:
            raise ValueError(
                f"Ayah recitation section must contain exactly one Arabic paragraph: "
                f"{section.get('ayah')}"
            )
        reference = references[0]
        return [(reference, f"{section['title']}: {reference['text']}", False)]

    if section.get("kind") == "ayah_detailed":
        prose = [
            paragraph
            for paragraph in section["paragraphs"]
            if paragraph["kind"] != "section_title"
        ]
        if not prose:
            raise ValueError(f"Ayah section has no analysis prose: {section.get('ayah')}")
        return [(paragraph, paragraph["text"], False) for paragraph in prose]

    prose = [
        paragraph
        for paragraph in section["paragraphs"]
        if paragraph["kind"] != "section_title"
    ]
    if not prose:
        return [
            (paragraph, tts_text_for(paragraph), False)
            for paragraph in section["paragraphs"]
        ]

    title_prefix = sentence_punctuate(section["title"])
    units = []
    for index, paragraph in enumerate(prose):
        tts_text = paragraph["text"]
        title_attached = index == 0
        if title_attached:
            tts_text = f"{title_prefix} {tts_text}"
        units.append((paragraph, tts_text, title_attached))
    return units


def request_hash(request):
    return sha256_text(stable_json(request))


def build_artifacts(source, kind, source_files, surah_id, out_root, collection):
    quran_text = load_quran_text() if kind == "ayah" else None
    sections = build_sections(
        source_files,
        kind,
        quran_text=quran_text,
        collection=collection,
    )
    raw_token_count = sum(
        count_inline_tokens(path.read_text(encoding="utf-8")) for path in source_files
    )
    reject_symlink_components(out_root, "--out-root")
    output_candidate = out_root / collection / surah_id
    reject_symlink_components(output_candidate, "output collection")
    out_dir = output_candidate.resolve()
    source_paths = [source_reference(path) for path in source_files]
    source_directory = source_reference(source if source.is_dir() else source.parent)

    chunks = []
    prompt = RECITATION_PROMPT if collection == "ayah-recitation" else PROMPT
    prompt_hash = sha256_text(prompt)
    for section_index, section in enumerate(sections, start=1):
        section_chunks = []
        for paragraph_index, (paragraph, tts_text, title_attached) in enumerate(
            audio_units_for(section), start=1
        ):
            chunk_id = f"sec-{section_index:03d}-p-{paragraph_index:03d}"
            request = build_request(tts_text, prompt=prompt)
            record = {
                "surahId": surah_id,
                "sourceKind": kind,
                "source": section.get("source", source_paths[0]),
                "chunkId": chunk_id,
                "sectionIndex": section_index,
                "paragraphIndex": paragraph_index,
                "kind": paragraph["kind"],
                "publicationKind": section.get("kind", kind),
                "grades": list(section.get("grades", [])),
                "sectionTitle": section["title"],
                "text": paragraph["text"],
                "ttsText": tts_text,
                "ttsCharCount": len(tts_text),
                "titleAttachedToFirstParagraph": title_attached,
                "request": f"requests/{chunk_id}.json",
                "response": f"responses/{chunk_id}.json",
                "wav": f"originals/wav/{chunk_id}.wav",
                "mp3": f"originals/mp3/{chunk_id}.mp3",
                "durationSeconds": None,
                "charCount": len(paragraph["text"]),
                "wordCount": len(paragraph["text"].split()),
                "textSha256": sha256_text(paragraph["text"]),
                "promptSha256": prompt_hash,
                "voiceSha256": sha256_text(stable_json(VOICE)),
                "audioConfigSha256": sha256_text(stable_json(AUDIO_CONFIG)),
                "requestSha256": request_hash(request),
            }
            chunks.append(record)
            section_chunks.append(record)
        section["chunks"] = section_chunks

    manifest = {
        "source": source_paths[0] if len(source_paths) == 1 else source_directory,
        "sources": source_paths,
        "sourceKind": kind,
        "sourceDirectory": source_directory,
        "surahId": surah_id,
        "collection": collection,
        "cleanMarkdown": f"{surah_id}.md",
        "chunksJsonl": "chunks.jsonl",
        "prompt": prompt,
        "promptSha256": prompt_hash,
        "voice": VOICE,
        "audioConfig": AUDIO_CONFIG,
        "inlineGlossTokenCount": raw_token_count,
        "inlineGlossConversion": (
            "Not applicable; recitation uses canonical Arabic text."
            if collection == "ayah-recitation"
            else "{ar, tr, gloss} -> Arabic (gloss); transliteration omitted"
        ),
        "arabicTextSource": source_reference(QURAN_TEXT_PATH) if kind == "ayah" else None,
        "ttsCharCount": sum(chunk["ttsCharCount"] for chunk in chunks),
        "titleHandling": (
            "Surah title is attached to the first prose ttsText and retained as the visible heading."
            if kind == "surah"
            else (
                "One joined ttsText per ayah: Turkish surah name, numeric ayah number, colon, and canonical Arabic text."
                if collection == "ayah-recitation"
                else "Ayah commentary prose is emitted without a synthetic ayah label."
            )
        ),
        "chunkCount": len(chunks),
        "sections": [
            {
                "sectionIndex": index,
                "title": section["title"],
                "kind": section.get("kind", kind),
                "grades": list(section.get("grades", [])),
                "ayah": section.get("ayah"),
                "arabicText": section.get("arabicText"),
                "wav": f"sections/wav/sec-{index:03d}.wav",
                "mp3": f"sections/mp3/sec-{index:03d}.mp3",
                "durationSeconds": None,
                "paragraphs": [
                    {
                        key: chunk[key]
                        for key in (
                            "paragraphIndex",
                            "kind",
                            "chunkId",
                            "text",
                            "ttsText",
                            "ttsCharCount",
                            "titleAttachedToFirstParagraph",
                            "request",
                            "response",
                            "wav",
                            "mp3",
                            "durationSeconds",
                        )
                    }
                    for chunk in section["chunks"]
                ],
            }
            for index, section in enumerate(sections, start=1)
        ],
    }
    return {
        "source": source,
        "sourceFiles": source_files,
        "sourceKind": kind,
        "surahId": surah_id,
        "outDir": out_dir,
        "sections": sections,
        "chunks": chunks,
        "manifest": manifest,
        "rawTokenCount": raw_token_count,
        "ttsCharCount": sum(chunk["ttsCharCount"] for chunk in chunks),
    }


def ensure_collection_replacement_is_explicit(out_dir, replace_existing, prune):
    if not out_dir.exists():
        return
    existing = [
        path
        for path in out_dir.iterdir()
        if path.name != ".tts-generation.lock"
    ]
    if not existing:
        return
    if not replace_existing:
        raise ValueError(
            f"Refusing to overwrite existing TTS collection: {out_dir}. "
            "Use --replace-existing --prune explicitly to replace it."
        )
    if not prune:
        raise ValueError(
            "Replacing an existing TTS collection requires --prune so stale "
            "requests and audio derivatives cannot remain: "
            f"{out_dir}"
        )


def write_artifacts(artifacts, prune=False, replace_existing=False):
    out_dir = artifacts["outDir"]
    reject_unresolved_remote_outcomes(out_dir)
    ensure_collection_replacement_is_explicit(out_dir, replace_existing, prune)
    requests_dir = out_dir / "requests"
    responses_dir = out_dir / "responses"
    originals_wav_dir = out_dir / "originals" / "wav"
    originals_mp3_dir = out_dir / "originals" / "mp3"
    sections_wav_dir = out_dir / "sections" / "wav"
    sections_mp3_dir = out_dir / "sections" / "mp3"

    for directory in (
        requests_dir,
        responses_dir,
        originals_wav_dir,
        originals_mp3_dir,
        sections_wav_dir,
        sections_mp3_dir,
    ):
        if directory.is_symlink():
            raise ValueError(f"Refusing symlinked artifact directory: {directory}")
        directory.mkdir(parents=True, exist_ok=True)

    write_clean_markdown(out_dir / artifacts["manifest"]["cleanMarkdown"], artifacts["sections"])
    for chunk in artifacts["chunks"]:
        request = build_request(chunk["ttsText"])
        atomic_write_text(
            out_dir / chunk["request"],
            json.dumps(request, ensure_ascii=False, indent=2) + "\n",
        )

    atomic_write_text(
        out_dir / "chunks.jsonl",
        "".join(json.dumps(chunk, ensure_ascii=False) + "\n" for chunk in artifacts["chunks"]),
    )
    atomic_write_text(
        out_dir / "manifest.json",
        json.dumps(artifacts["manifest"], ensure_ascii=False, indent=2) + "\n",
    )

    if prune:
        cleanup_unreferenced_files(
            [
                (requests_dir, [out_dir / chunk["request"] for chunk in artifacts["chunks"]]),
                (responses_dir, [out_dir / chunk["response"] for chunk in artifacts["chunks"]]),
                (originals_wav_dir, [out_dir / chunk["wav"] for chunk in artifacts["chunks"]]),
                (originals_mp3_dir, [out_dir / chunk["mp3"] for chunk in artifacts["chunks"]]),
                (
                    sections_wav_dir,
                    [out_dir / section["wav"] for section in artifacts["manifest"]["sections"]],
                ),
                (
                    sections_mp3_dir,
                    [out_dir / section["mp3"] for section in artifacts["manifest"]["sections"]],
                ),
            ]
        )


def cost_argument(value):
    try:
        number = Decimal(value)
    except (InvalidOperation, ValueError) as error:
        raise argparse.ArgumentTypeError(f"Invalid decimal: {value}") from error
    if not number.is_finite() or number <= 0:
        raise argparse.ArgumentTypeError("Cost rate must be finite and greater than zero")
    return number


def main():
    parser = argparse.ArgumentParser(
        description="Prepare quran-data detailed Markdown into offline TTS requests."
    )
    parser.add_argument(
        "source",
        type=Path,
        help="A surah Markdown file, a surah sNNN directory, an ayah prose file, or an ayah sNNN directory.",
    )
    parser.add_argument(
        "--source-kind",
        choices=("auto", "surah", "ayah"),
        default="auto",
        help="Override source detection when necessary (default: auto).",
    )
    parser.add_argument(
        "--out-root",
        type=Path,
        default=DEFAULT_OUT_ROOT,
        help=f"Artifact root (default: {DEFAULT_OUT_ROOT}).",
    )
    parser.add_argument(
        "--collection",
        choices=("surah", "ayah", "ayah-recitation"),
        help="Output collection name; defaults to the detected source kind.",
    )
    parser.add_argument("--surah-id", help="Override inferred S001-style surah id.")
    parser.add_argument(
        "--cost-per-million-chars",
        type=cost_argument,
        default=Decimal("20"),
        help="Estimate only: TTS price in USD per million spoken characters (default: 20).",
    )
    parser.add_argument(
        "--prune",
        action="store_true",
        help="Delete unreferenced files in this output collection after writing.",
    )
    parser.add_argument(
        "--replace-existing",
        action="store_true",
        help="Allow replacing an existing collection; requires --prune to remove stale artifacts.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Parse and validate, but do not write files and never call TTS.",
    )
    args = parser.parse_args()

    source = args.source.expanduser().resolve()
    detected_kind = infer_source_kind(source)
    kind = detected_kind if args.source_kind == "auto" else args.source_kind
    if kind != detected_kind:
        raise ValueError(f"Source kind {kind} does not match its quran-data path: {source}")
    source_files = collect_source_files(source, kind)
    inferred_surah_id = normalize_surah_id(str(source))
    surah_id = inferred_surah_id
    if args.surah_id:
        override_surah_id = normalize_surah_id(args.surah_id)
        if override_surah_id != inferred_surah_id:
            raise ValueError(
                f"--surah-id {override_surah_id} does not match source {inferred_surah_id}"
            )
    out_root_argument = args.out_root.expanduser()
    reject_symlink_components(out_root_argument, "--out-root")
    out_root = out_root_argument.resolve()
    collection = args.collection or kind
    if collection != kind and not (kind == "ayah" and collection == "ayah-recitation"):
        raise ValueError(f"Collection {collection} must match source kind {kind}")

    artifacts = build_artifacts(
        source,
        kind,
        source_files,
        surah_id,
        out_root,
        collection,
    )
    ensure_output_within_root(out_root, artifacts["outDir"])
    ensure_paths_disjoint(source, artifacts["outDir"])
    output_chars = artifacts["ttsCharCount"]
    prompt = artifacts["manifest"]["prompt"]
    input_chars = output_chars + len(prompt) * len(artifacts["chunks"])
    input_cost = (Decimal(input_chars) * INPUT_COST_PER_MILLION_CHARS / Decimal(1_000_000)).quantize(
        Decimal("0.000001"), rounding=ROUND_CEILING
    )
    output_cost = (
        Decimal(output_chars) * args.cost_per_million_chars / Decimal(1_000_000)
    ).quantize(Decimal("0.000001"), rounding=ROUND_CEILING)
    summary = {
        "dryRun": args.dry_run,
        "sourceKind": kind,
        "sources": [source_reference(path) for path in source_files],
        "outDir": str(artifacts["outDir"]),
        "sections": len(artifacts["sections"]),
        "chunks": len(artifacts["chunks"]),
        "inlineGlossTokens": artifacts["rawTokenCount"],
        "ttsChars": artifacts["ttsCharCount"],
        "inputChars": input_chars,
        "outputChars": output_chars,
        "inputCostUsd": str(input_cost),
        "outputCostUsd": str(output_cost),
        "estimatedCostUsd": str(input_cost + output_cost),
        "inputCostRateUsdPerMillionChars": str(INPUT_COST_PER_MILLION_CHARS),
        "outputCostRateUsdPerMillionChars": str(args.cost_per_million_chars),
        "ttsRequestsPrepared": len(artifacts["chunks"]),
        "prune": args.prune,
        "replaceExisting": args.replace_existing,
    }
    if artifacts["chunks"]:
        summary["firstTtsText"] = artifacts["chunks"][0]["ttsText"]
    if not args.dry_run:
        with CollectionLock(artifacts["outDir"]):
            write_artifacts(
                artifacts,
                prune=args.prune,
                replace_existing=args.replace_existing,
            )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
