"""Shared loaders for the D-knowledge-supply scripts (read-only on every repo)."""
import csv, json, re
from collections import defaultdict, Counter
from pathlib import Path
csv.field_size_limit(10**9)
HERE = Path(__file__).resolve().parent
D = HERE.parent
P = Path('/Volumes/OZTURK/_projects')
PG = P / 'prose_generation'
V9 = PG / '_commentary' / 'v9'
V15 = PG / '_commentary' / 'v15'
QURAN = P / 'quran-data' / 'data' / 'text' / 'quran-uthmani.tsv'

DIAC = re.compile(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]')
MAP = str.maketrans({'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ى': 'ي', 'ة': 'ه', 'ؤ': 'و', 'ئ': 'ي', 'ۥ': '', 'ۦ': ''})
AR = re.compile(r'[ء-يٱ-ۓؐ-ًؚ-ٰٟۖ-ۭـ]+')


def fold(s):
    return re.sub(r'\s+', ' ', re.sub(r'[^ء-ي ]', ' ', DIAC.sub('', s).translate(MAP))).strip()


def quran():
    """{(s,a): text} from quran-uthmani.tsv (format s|a|text)."""
    out = {}
    for line in QURAN.read_text(encoding='utf-8').splitlines():
        if '|' not in line:
            continue
        ref, text = line.split('|', 1)
        s, a = ref.split(':')
        out[(int(s), int(a))] = text.replace('\ufeff', '')
    return out


def branches():
    return [r for r in csv.DictReader(open(D / 'branches.tsv', encoding='utf-8'), delimiter='\t')]


def v15_words():
    return [r for r in csv.DictReader(open(V15 / 'data' / 'words.tsv', encoding='utf-8'), delimiter='\t')]


def v15_lemmas():
    return [r for r in csv.DictReader(open(V15 / 'data' / 'lemmas.tsv', encoding='utf-8'), delimiter='\t')]


def v15_branches():
    return [r for r in csv.DictReader(open(V15 / 'data' / 'branches.tsv', encoding='utf-8'), delimiter='\t')]


AR_CH = re.compile(r'[؀-ۿݐ-ݿࢠ-ࣿ]')


def est_tokens(text, a_ar=None, a_other=None):
    """Token estimate calibrated on billed v9 runs (see calib.py): tokens = a_ar*arabic_chars + a_other*other_chars."""
    cal = json.loads((HERE / 'calib.json').read_text()) if (HERE / 'calib.json').exists() else {'a_ar': 0.9, 'a_other': 0.3}
    a_ar = cal['a_ar'] if a_ar is None else a_ar
    a_other = cal['a_other'] if a_other is None else a_other
    n_ar = len(AR_CH.findall(text))
    return a_ar * n_ar + a_other * (len(text) - n_ar)
