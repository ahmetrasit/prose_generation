#!/usr/bin/env python3
"""v16 dictionary: every branch of every focus root, with the early-source phrases whole (see DESIGN.md).

Same roots and order as v9/prepare.py section_dictionary (identity roots, documented alternatives, echo roots).
Per branch, only what the readings use or need:
  - the short Turkish gloss (a label to scan by);
  - the Turkish per-sense glosses (`lexical_glosses`), one per attested sense of the branch;
  - `[kalıp]` when the dictionary marks the branch collocation-bound (the source phrases show the construction);
  - the early-source phrases (`source_phrase_ar`) whole, with their source tags; never clipped.
Left out: the root summary, the Turkish definition and facets, the Arabic image and scope lines, the "not" boundary,
identity judgments, source synthesis, error profiles and neighbour distinctions (dictionary-building apparatus;
12 readings quoted none of them and shared no more Turkish phrasing with them than with fields they never saw).

No module state is patched and nothing is shared between calls except the read-only Sources object, so callers
must build in one thread (SQLite connections in Sources belong to the thread that opened them).

Usage: python3 _commentary/v16/dictionary.py 1:6 [...]   prints sizes against the v9 file; writes nothing
"""
from __future__ import annotations

import sys
from pathlib import Path

V9 = Path(__file__).resolve().parents[1] / "v9"
sys.path.insert(0, str(V9))
import prepare as P  # noqa: E402

_ROOTS_NOTE = ["Identity roots come from the quran-data gateway. Word-scoped alternatives are cited analyses of this",
               "exact word. **Echo roots** are observed but withheld mappings: sound-family candidates, not identity.", ""]
HEADERS = {
    # r1: as run for D, VD and DM (r1). Its claim about gloss order is wrong (REVIEW.md I8); kept for provenance.
    "r1": ["# Dictionary: every branch of every focus root", "",
           "One line per branch: Turkish label; the Turkish glosses of its senses, in the order of the source "
           "phrases; the classical dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, "
           "mufradat, jamhara). [kalıp] marks a sense the dictionaries attest only inside a fixed expression."]
          + _ROOTS_NOTE,
    "r2": ["# Dictionary: every branch of every focus root", "",
           "One entry per branch: a Turkish label and Turkish glosses of its attested senses, then the classical "
           "dictionaries' own phrases with their source tags (ayn, sihah, tahdhib, maqayis, mufradat, jamhara). "
           "[kalıp] marks a sense the dictionaries attest only inside a fixed expression."] + _ROOTS_NOTE,
}


def dict_lines(src: P.Sources, rid: str) -> list[str]:
    e = src.entry(rid)
    if not e:
        return [f"- ({rid}) no Turkish dictionary entry", ""]
    lines = []
    for b in e.get("branches", []):
        g = b.get("concept_gloss")
        g = (g.get("text") if isinstance(g, dict) else g) or ""
        senses = " · ".join(x.get("target_gloss", "") for x in b.get("lexical_glosses", []) if x.get("target_gloss"))
        kind = " [kalıp]" if (b.get("lexicalization_scope") or {}).get("branch_kind") == "collocation" else ""
        lines.append(f"- **{b['branch_ref'].split('/')[-1]}** {g}{kind} — {senses}\n  {b.get('source_phrase_ar', '')}")
    return lines + [""]


def section(src: P.Sources, ref: str, version: str = "r1") -> str:
    """One ayah: the same roots, order and headings as v9 section_dictionary, with v16 branch lines."""
    lines = list(HEADERS[version])
    done = set()
    analysed = [(w, src.word_roots(w)) for w in src.words(ref)]
    for w, r in analysed:
        for rid in r["identity"]:
            if rid not in done:
                done.add(rid)
                lines += [f"## {src.root_name.get(rid, rid)} ({rid}) — identity root of {w['surface']} (w{w['w']})", ""]
                lines += dict_lines(src, rid)
    for w, r in analysed:
        for rid, why in r["alternatives"]:
            if rid not in done:
                done.add(rid)
                lines += [f"## {src.root_name.get(rid, rid)} ({rid}) — documented alternative for {w['surface']}: "
                          f"{P.clip(why, 160)}", ""]
                lines += dict_lines(src, rid)
    for w, r in analysed:
        for rid, why in r["echo"]:
            if rid not in done:
                done.add(rid)
                lines += [f"## ECHO {src.root_name.get(rid, rid)} ({rid}) — for {w['surface']} (w{w['w']}): {why}; "
                          f"not identity", ""]
                lines += dict_lines(src, rid)
    return "\n".join(lines) + "\n"


def surah_section(src: P.Sources, refs: list[str], version: str = "r1") -> str:
    """Every root of every ayah in `refs`, each once, in order of first occurrence. A root's heading lists every
    word it serves under its strongest role (identity, then documented alternative, then echo)."""
    header = HEADERS[version]
    lines = header[:1] + ["", "Every root of the surah's words, each once, headed by the ayah and word where it first "
                          "occurs; it also serves the later words listed with it."] + header[2:]
    rank = {"identity": 0, "alternative": 1, "echo": 2}
    roles: dict[str, dict[str, list]] = {}
    for ref in refs:
        for w in src.words(ref):
            r = src.word_roots(w)
            kinds = [("identity", rid, "") for rid in r["identity"]]
            kinds += [("alternative", rid, why) for rid, why in r["alternatives"]]
            kinds += [("echo", rid, why) for rid, why in r["echo"]]
            for kind, rid, why in kinds:
                roles.setdefault(rid, {}).setdefault(kind, []).append((f"{ref} {w['surface']}", why))
    for rid, by_kind in roles.items():
        name = src.root_name.get(rid, rid)
        best = min(by_kind, key=rank.get)
        where = ", ".join(x for x, _ in by_kind[best])
        why = by_kind[best][0][1]
        head = {"identity": f"## {name} ({rid}): {where}",
                "alternative": f"## {name} ({rid}): documented alternative for {where}: {P.clip(why, 160)}",
                "echo": f"## ECHO {name} ({rid}): for {where}: {why}; not identity"}[best]
        others = [f"{k} for {', '.join(x for x, _ in v)}" for k, v in by_kind.items() if k != best]
        lines += [head + (f" (also {'; '.join(others)})" if others else ""), ""] + dict_lines(src, rid)
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    src = P.Sources()
    for ref in sys.argv[1:]:
        s, a = ref.split(":")
        old = (V9 / "input" / "v2" / f"s{int(s):03d}" / f"{s}_{a}" / "01_dictionary.md").read_text(encoding="utf-8")
        new = section(src, ref, "r2")
        print(f"{ref}: v9 {len(old):,} chars, v16 {len(new):,} chars ({100 * (len(new) - len(old)) / len(old):+.0f}%)")
