"""Lossless, offline handover for v14. Presence checks are never semantic acceptance."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

RECORD = re.compile(r"^([FQAI]\d+)\s*\|")
REF = re.compile(r"(?<![\d:])(\d{1,3}:\d{1,3})(?![\d:])")
TAGGED = re.compile(r"(?<![\d:])(\d{1,3}:\d{1,3})(?![\d:])((?:\s*\[(?:staging|same-word)\])*)")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def records(text: str) -> dict[str, str]:
    """Keep wrapped records, including wrapped network fields; reject duplicate IDs."""
    result, current = {}, None
    for line in text.splitlines():
        if not line.strip():
            continue
        match = RECORD.match(line)
        if match:
            current = match[1]
            if current in result:
                raise ValueError(f"duplicate record {current}")
            result[current] = line.strip()
        elif line.startswith("unplaced:"):
            current = None  # all focus findings are retained independently below
        elif current:
            result[current] += " " + line.strip()
        elif not line.startswith("#"):
            raise ValueError(f"unparsed record text: {line[:100]}")
    return result


def field(line: str, name: str) -> str:
    for part in re.split(r"\s*\|\s*", line):
        if part.startswith(name + ":"):
            return part.partition(":")[2].strip()
    return ""


def passages(text: str) -> dict[str, list[str]]:
    """Both adjacent tags belong to the same reference; tags never select evidence."""
    result: dict[str, set[str]] = {}
    for ref, group in TAGGED.findall(text):
        result.setdefault(ref, set()).update(re.findall(r"\[(staging|same-word)\]", group))
    return {ref: sorted(tags) for ref, tags in result.items()}


def prose_passages(text: str) -> set[str]:
    """Read inline source tags and inclusive same-surah ranges without mistaking word IDs for ayat."""
    text = re.sub(r"\bsource:\s*", " ", text)
    pattern = re.compile(REF.pattern + r"(?:\s*[–—-]\s*(\d{1,3})(?::(\d{1,3}))?(?![\d:]))?")
    result = set()
    for match in pattern.finditer(text):
        result.add(match[1])
        if not match[2]:
            continue
        surah, start = map(int, match[1].split(":"))
        end_surah, end = (int(match[2]), int(match[3])) if match[3] else (surah, int(match[2]))
        result.add(f"{end_surah}:{end}")
        if end_surah == surah and start <= end <= 286:
            result.update(f"{surah}:{ayah}" for ayah in range(start, end + 1))
    return result


def roles(disclosure: str, ref: str) -> list[str]:
    # Accept both legacy `develop 2:3, 2:4` and `2:3 develop; 2:4 touch`.
    s, a = map(int, ref.split(":"))
    found = []
    for segment in disclosure.split(";"):
        role = None
        tokens = re.finditer(r"\b(meet|touch|develop|assemble)\b|(\d+:\d+)(?:\s*[–-]\s*(\d+:\d+|\d+))?", segment)
        pending = []
        for m in tokens:
            if m[1]:
                role = m[1]
                found.extend(role for hit in pending if hit)
                pending = []
            else:
                lo = tuple(map(int, m[2].split(":")))
                hi = tuple(map(int, m[3].split(":"))) if m[3] and ":" in m[3] else (lo[0], int(m[3])) if m[3] else lo
                hit = lo[0] == hi[0] == s and lo[1] <= a <= hi[1]
                if role and hit:
                    found.append(role)
                elif role is None:
                    pending.append(hit)
    return list(dict.fromkeys(found))


def focus_members(line: str, ref: str) -> list[str]:
    return [part.strip() for part in field(line, "members").split(";")
            if re.search(rf"(?<![\d:]){re.escape(ref)}:\d+", part)]


def inventory(ref: str, activation: str, qeq: str, network: str) -> dict:
    acts, annotations, images = records(activation), records(qeq), records(network)
    items, groups, all_passages = {}, [], {}
    for key, raw in acts.items():
        items[key] = {"kind": raw.split("|")[1].strip(), "text": raw}
    for key, raw in annotations.items():
        owner = "E_" + key if key.startswith("F") else key
        kind = raw.split("|")[1].strip()
        items[owner] = {"kind": kind, "text": raw, "finding": key if key.startswith("F") else None}
        # Q-record trigger fields carry S:A:W; plain S:A refs elsewhere are also kept.
        if key.startswith("F") or key.startswith("A"):
            cited = passages(raw.split("|", 3)[2])
        else:
            cited = passages(raw)
        items[owner]["passages"] = cited
        for passage, tags in cited.items():
            entry = all_passages.setdefault(passage, {"tags": [], "owners": []})
            entry["tags"] = sorted(set(entry["tags"]) | set(tags))
            entry["owners"].append(owner)
    for key, raw in images.items():
        members = focus_members(raw, ref)
        here_roles = roles(field(raw, "disclosure"), ref)
        meetings = [part.strip() for part in field(raw, "meets").split(";")
                    if re.search(rf"(?<![\d:]){re.escape(ref)}:\d+", part)]
        if not (members or here_roles or meetings):
            continue
        items[key] = {"kind": "image", "text": raw, "members_here": members,
                      "roles_here": here_roles or ["touch"], "meetings_here": meetings}
        linked = []
        # Read only findings explicitly scoped to this ayah; never confuse another ayah's F1.
        for match in re.finditer(rf"(?<![\d:]){re.escape(ref)}\s+(F\d+(?:\s+F\d+)*)", raw):
            linked += re.findall(r"F\d+", match[1])
        linked = [k for k in dict.fromkeys(linked) if k in items]
        linked += ["E_" + k for k in linked if "E_" + k in items]
        for qid, qraw in annotations.items():
            if qid.startswith("Q") and set(re.findall(r"F\d+", field(qraw, "with"))) & set(linked):
                linked.append(qid)
        meeting_ids = []
        for idx, meeting in enumerate(meetings, 1):
            mid = f"{key}_M{idx}"
            items[mid] = {"kind": "meeting", "text": meeting, "image": key}
            meeting_ids.append(mid)
        groups.append({"image": key, "items": [key, *linked, *meeting_ids]})
    return {"schema": 1, "ref": ref, "items": items, "groups": groups, "passages": all_passages}


def render(data: dict) -> str:
    lines = [f"# synthesis.md — evidence for {data['ref']}", "",
             "This is an evidence index, not an outline or a list to put into prose. Image groups overlap. "
             "Combine them into connected explanations where their relationships earn space. No item or tag is ranked.", "",
             "## Image connections (navigation only)"]
    for group in data["groups"]:
        image = data["items"][group["image"]]
        lines.append(f"- {group['image']}: {', '.join(group['items'])}; role here: {', '.join(image['roles_here'])}")
        lines += [f"  - This ayah's member: {member}" for member in image["members_here"]]
    lines += ["", "## Evidence (each source record appears once)"]
    for key, item in data["items"].items():
        lines.append(f"\n### {key} — {item['kind']}")
        if item["kind"] == "image":
            raw = item["text"]
            lines += [raw.split("|")[1].strip(), "Role here: " + ", ".join(item["roles_here"])]
            # Full assembly needs every member. A touch needs this ayah's actual contribution;
            # the complete source remains in synthesis.json and the frozen network.
            members = field(raw, "members") if set(item["roles_here"]) & {"develop", "assemble"} else "; ".join(item["members_here"])
            lines += ["Members for this treatment: " + members,
                      "Movement: " + field(raw, "movement"), "Purpose: " + field(raw, "purpose"),
                      "Disclosure: " + field(raw, "disclosure")]
        else:
            lines.append(item["text"])
    lines += ["", "QeQ tags describe evidence, not obligations. A same-word passage may provide a decisive definition; "
              "a staging passage may duplicate another. Preserve the explanatory job and real counter-evidence. "
              "The full source records above remain available even when a passage is not quoted."]
    return "\n".join(lines) + "\n"


def check_account(data: dict, prose: str, account: dict) -> dict:
    """Validate references and exact evidence, never whether an explanation is good."""
    items = data["items"]
    errors, decisions, bundles = [], {}, []
    if not isinstance(account, dict):
        account = {}
        errors.append("synthesis account must be a JSON object")
    version = account.get("schema", 1)
    if version not in (1, 2):
        errors.append("unsupported synthesis account schema")
    paragraphs = [p for p in prose.split("\n\n") if p.strip()]
    rows, deferred = account.get("bundles", []), account.get("deferred", [])
    if not isinstance(rows, list) or not isinstance(deferred, list):
        rows, deferred = [], []
        errors.append("bundles and deferred must be arrays")
    seen_bundles = set()
    for row in rows:
        if not isinstance(row, dict):
            errors.append("invalid bundle")
            continue
        bid = row.get("id", "")
        level = row.get("level")
        keys = row.get("items", [])
        evidence, payoff = row.get("evidence", ""), row.get("payoff", "")
        evidence_valid = isinstance(evidence, str) and len(evidence.strip()) >= 20 and evidence in prose
        resolved = evidence
        if version == 2:
            evidence_valid = (isinstance(evidence, list) and 1 <= len(evidence) <= 3
                              and all(isinstance(anchor, str) and 20 <= len(anchor.strip()) <= 240
                                      for anchor in evidence))
            matches = [[p for p in paragraphs if anchor in p] for anchor in evidence] if evidence_valid else []
            evidence_valid = evidence_valid and all(len(found) == 1 for found in matches)
            resolved = "\n\n".join(dict.fromkeys(p for found in matches for p in found))
        valid = (bool(re.fullmatch(r"B\d+", str(bid))) and bid not in seen_bundles
                 and level in ("mentioned", "explained", "connected")
                 and isinstance(keys, list) and bool(keys) and all(isinstance(k, str) and k in items for k in keys)
                 and evidence_valid and isinstance(payoff, str) and bool(payoff.strip())
                 and (version != 2 or len(payoff) <= 240))
        seen_bundles.add(str(bid))
        if not valid:
            errors.append(f"{bid or '?'}: invalid IDs, level, payoff or evidence (schema 2 needs short, unambiguous anchors)")
            continue
        for key in keys:
            if key in decisions:
                errors.append(f"{key}: duplicate disposition; join its explanations in one bundle")
            decisions[key] = {"level": level, "bundle": bid, "evidence": resolved, "payoff": payoff}
        bundles.append(dict(row, resolved_evidence=resolved) if version == 2 else row)
    # A single explicit remainder declaration avoids hundreds of bookkeeping lines.
    for row in deferred:
        if not isinstance(row, dict):
            errors.append("invalid deferral")
            continue
        keys = row.get("items")
        if keys == "remaining":
            keys = [key for key in items if key not in decisions]
        reason, destination = row.get("reason", ""), row.get("destination", "")
        if (not isinstance(keys, list) or not all(isinstance(k, str) and k in items for k in keys)
                or not isinstance(reason, str) or not reason.strip()
                or not isinstance(destination, str) or not destination.strip()):
            errors.append("deferral needs known IDs (or remaining), reason and destination")
            continue
        for key in keys:
            if key in decisions:
                errors.append(f"{key}: duplicate disposition")
                continue
            decisions[key] = {"level": "deferred", "reason": reason, "destination": destination}
    for key in items:
        if key not in decisions:
            decisions[key] = {"level": "unreported", "reason": "No valid disposition supplied", "destination": "review"}
    unresolved = [key for key, d in decisions.items() if d["level"] == "unreported"]
    prose_refs = prose_passages(prose)
    unused = {key: value for key, value in data["passages"].items() if key not in prose_refs}
    return {"schema": 1, "semantic_acceptance": "pending independent review", "errors": errors,
            "unreported": unresolved, "structurally_valid": not errors and not unresolved,
            "decisions": decisions, "bundles": bundles, "unused_passage_candidates": unused,
            "counter_evidence": [key for key, item in items.items() if item["kind"] == "contradicts"]}


def handforward(data: dict, check: dict) -> str:
    lines = [f"# Handforward — {data['ref']}", "",
             "Mentioned, deferred and unreported findings remain open. Explained/connected are writer claims "
             "until independent review. The source inventory is retained in full.", ""]
    for key, disposition in check["decisions"].items():
        if disposition["level"] in ("explained", "connected"):
            continue
        lines += [f"## {key}: {disposition['level']}", json.dumps(disposition, ensure_ascii=False),
                  data["items"][key]["text"], ""]
    lines += ["## Unquoted passage candidates (evidence, not missing explanations)", ""]
    for ref, detail in check["unused_passage_candidates"].items():
        lines.append(f"- {ref}: {', '.join(detail['owners'])}; tags: {', '.join(detail['tags']) or 'none'}")
    return "\n".join(lines) + "\n"
