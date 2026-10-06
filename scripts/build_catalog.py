#!/usr/bin/env python3
"""Rebuild the catalog from the files actually in the repo, in three levels:
- 901_READ_FIRST/04_CATALOG.md — one line per area: what it holds, how many files,
  by category and type, and where its full list is. Agents read this first.
- <area>/910_RECORDS/CATALOG.csv — every saved file in that area.
- <folder>/910_RECORDS/INDEX.csv — every saved file in that folder.
The two lists are CSV: back-end data for agents and tools, one row per file, not pages
for people (older INDEX.md / CATALOG.md tables are replaced).
Only this script writes them (people and AI tools never do), so saves never collide.

Runs after every push to main (.github/workflows/catalog.yml), so the catalog
is complete whichever tool saved a file. Root AGENTS.md §Routing.

A row per saved file: id, date, title, description, kind, category, type, file.\n- id: YYYYMMDD-TTT-KKK-XXXX, stamped into the header the first time (or when it\n  duplicates another) and never changed after — so the job also commits those headers.\n- description: the header's subject_text.
- category: one per file, from the header's context_type (decision → 926_DECISIONS,
  analysis → 924_MODELS …); 920_UNSORTED for a record not sorted yet; — for pages
  that aren't statements (a profile, a concept page).
- type (People, Places, Sources …): the header's `type:`, else the older numbered
  folder it sits in (15_CONCEPTS → Concepts), else the one type its folder holds.
Each file is logged in the nearest folder
above any folder-type folder (a concept page in topic/15_CONCEPTS/ is in the
topic's log). Back-end files — AGENTS.md, README.md, FOCUS.md, and anything whose
name starts with 9 (910_RECORDS/, 990_TRACKING/ …), push-back, work/ — are not listed. A file is rewritten only when
its lines change.
"""

import csv
import datetime
import io
import json
import os
import re
import secrets
import subprocess

# The log's categories — back end, so they start with 9. Settings files store the older slot names.
CODE = {"00_INBOX": "920_UNSORTED", "02_QUESTIONS": "922_QUESTIONS", "03_REFERENCES": "923_REFERENCES",
        "04_MODELS": "924_MODELS", "06_DECISIONS": "926_DECISIONS"}
ROUTE = {
    "decision": "926_DECISIONS", "outcome": "926_DECISIONS",
    "assumption": "922_QUESTIONS", "known_issue": "922_QUESTIONS",
    "methodology": "923_REFERENCES", "definition": "923_REFERENCES", "evidence": "923_REFERENCES",
    "analysis": "924_MODELS",
}
SETTINGS = ("902_REFERENCES/REPO_SETTINGS.json", "02_REFERENCES/REPO_SETTINGS.json")
CATALOG = "901_READ_FIRST/04_CATALOG.md" if os.path.isdir("901_READ_FIRST") or not os.path.isdir("01_READ_FIRST") else "01_READ_FIRST/04_CATALOG.md"
NUM = re.compile(r"^\d+_")
RULES = {"AGENTS.md", "README.md", "FOCUS.md", "INDEX.md"}
MACHINERY = {"901_READ_FIRST", "902_REFERENCES", "01_READ_FIRST", "02_REFERENCES"}
COLUMNS = ["id", "date", "title", "description", "kind", "category", "type", "file"]


def routes():
    """The repo's own kinds (repo ⚙ → Classifications) when it has them."""
    kinds = None
    for path in SETTINGS:
        try:
            kinds = json.load(open(path))["classifications"]
            break
        except (OSError, ValueError, KeyError, TypeError):
            continue
    out = dict(ROUTE)
    for k in kinds or []:
        if isinstance(k, dict) and isinstance(k.get("type"), str) and k.get("slot") in CODE:
            out[k["type"]] = CODE[k["slot"]]
    return out


def header(path):
    text = open(path, encoding="utf-8", errors="replace").read().lstrip("﻿")
    meta = {}
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            for line in text[3:end].splitlines():
                m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
                if m:
                    meta[m.group(1).lower()] = m.group(2).strip().strip("'\"")
            text = text[end + 4:]
    h1 = re.search(r"^#\s+(.+)$", text, re.M)
    return meta, (h1.group(1).strip() if h1 else None)


# IDs: YYYYMMDD-TTT-KKK-XXXX — stamped into the header once, never changed (root AGENTS.md §Routing).
TYPE_CODE = {
    "people": "PEO", "groups": "GRO", "periods": "PER", "works": "WOR", "places": "PLA", "concepts": "CON",
    "practices": "PRA", "systems": "SYS", "patterns": "PAT", "resources": "RES", "sources": "SOU",
    "evidence": "EVI", "interviews": "INT", "data": "DAT", "experiments": "EXP", "results": "RSL",
    "options": "OPT", "plans": "PLN", "workstreams": "WST", "timeline": "TIM", "responsibilities": "RSP",
    "dependencies": "DEP", "schedule": "SCH", "research": "RSR", "design": "DES", "build": "BLD",
    "launch": "LAU", "review": "REV", "processes": "PRO", "checklists": "CHK", "runs": "RUN",
    "measures": "MEA", "incidents": "INC", "improvements": "IMP",
}
KIND_CODE = {
    "analysis": "ANA", "assumption": "ASM", "decision": "DEC", "definition": "DEF", "dispute": "DIS",
    "evidence": "EVI", "known_issue": "KNI", "methodology": "MET", "outcome": "OUT", "correction": "COR",
    "preference": "PRE",
}
RANDOM = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
SLOT_NAMES = {"00_INBOX", "02_QUESTIONS", "03_REFERENCES", "04_MODELS", "06_DECISIONS", "99_ARCHIVE"}


def three(s):
    return (re.sub(r"[^A-Za-z]", "", s)[:3].upper() or "XXX").ljust(3, "X")


def make_id(date, typ, kind):
    t = TYPE_CODE.get(typ.lower(), three(typ)) if typ else "GEN"
    k = KIND_CODE.get(kind.lower(), three(kind)) if kind else "UNS"
    return f"{date.replace('-', '')}-{t}-{k}-" + "".join(secrets.choice(RANDOM) for _ in range(4))


def stamp(path, new_id):
    """Put id: first in the file's header (adds it, or replaces a duplicate)."""
    text = open(path, encoding="utf-8").read()
    m = re.match(r"(\ufeff?---\r?\n)([\s\S]*?)(\r?\n---[ \t]*(?:\r?\n|$))", text)
    if not m:
        return False
    body = re.sub(r"^id:.*\n?", "", m.group(2), flags=re.M)
    open(path, "w", encoding="utf-8").write(f"{m.group(1)}id: {new_id}\n{body}{m.group(3)}{text[m.end():]}")
    return True


def backend(parts):
    return any(
        p.startswith(".") or p in ("910_RECORDS", "01_RECORDS", "work") or re.match(r"^9\d*_", p)
        or re.match(r"^\d+_PUSH_BACK$", p, re.I) or re.match(r"^\d+_TRACKING$", p, re.I)
        for p in parts
    )


def held_type(folder):
    """The one type a folder's AGENTS.md says it holds ("**Holds:** People"), or None."""
    try:
        text = open(f"{folder}/AGENTS.md", encoding="utf-8").read()
    except OSError:
        return None
    m = re.search(r"\*\*Holds:\*\*\s*([^\n]+)", text)
    names = [x.strip() for x in m.group(1).split("·")] if m else []
    return names[0] if len(names) == 1 and names[0] else None


def type_name(folder):
    """A numbered type folder from older repos (15_CONCEPTS) → its type (Concepts)."""
    if not folder or folder.upper() in SLOT_NAMES:
        return None
    return folder.split("_", 1)[1].replace("_", " ").title()


def continues(parent, child):
    """Library numbers: each added digit is a sub-category of the number before it (40_ → 41_ → 411_)."""
    p, c = NUM.match(parent), NUM.match(child)
    if not p or not c:
        return False
    p, c = p.group(0)[:-1], c.group(0)[:-1]
    stem = p.rstrip("0") or p
    return c != p and not c.startswith("9") and len(c) > len(stem) and c.startswith(stem)


def log_folder(dirs):
    # a numbered folder that continues its parent's number (41_ in 40_) keeps its own log;
    # any other numbered folder (15_CONCEPTS/) is a type folder, logged by its parent
    for i in range(1, len(dirs)):
        if NUM.match(dirs[i]) and not continues(dirs[i - 1], dirs[i]):
            return "/".join(dirs[:i]), dirs[i]
    return "/".join(dirs), None


def cell(s):
    return re.sub(r"\s+", " ", s.replace("|", "\\|")).strip()


def flat(s):
    return re.sub(r"\s+", " ", s).strip()


def lines():
    route = routes()
    files = subprocess.check_output(["git", "ls-files"], text=True).splitlines()
    rows = {}
    seen = set()
    for f in sorted(files):
        p = f.split("/")
        if len(p) < 2 or not NUM.match(p[0]) or p[0] in MACHINERY or not re.search(r"\.(md|csv|tsv)$", f, re.I):
            continue
        if p[-1] in RULES or backend(p[:-1]) or not os.path.exists(f):
            continue
        meta, h1 = header(f) if f.lower().endswith(".md") else ({}, None)
        kind = meta.get("context_type", "").lower()
        folder, typed = log_folder(p[:-1])
        cat = route.get(kind) or ("920_UNSORTED" if meta.get("kind") == "record" or kind else "—")
        typ = meta.get("type") or type_name(typed) or held_type("/".join(p[:-1])) or "—"
        m = re.match(r"^(\d{4}-\d{2}-\d{2})", p[-1])
        date = m.group(1) if m else next(
            (meta[k][:10] for k in ("date", "created", "last_verified") if re.match(r"^\d{4}-\d{2}-\d{2}", meta.get(k, ""))), "—")
        title = meta.get("title") or h1 or re.sub(r"\.[^.]+$", "", p[-1])
        k = kind or meta.get("kind", "")
        rid = meta.get("id", "")
        if f.lower().endswith(".md") and (not rid or rid in seen):  # every saved file gets an ID, once
            rid = make_id(date if date != "—" else datetime.date.today().isoformat(), "" if typ == "—" else typ, kind)
            if not stamp(f, rid):
                rid = ""
        if rid:
            seen.add(rid)
        desc = (meta.get("subject_text") or meta.get("description") or "—")[:140]
        topics = meta.get("topics", "").strip("[] ")
        if topics:
            desc = f"{desc} — topics: {topics}" if desc != "—" else f"topics: {topics}"
        rows.setdefault(folder, []).append((date, f, [rid, "" if date == "—" else date, flat(title), "" if desc == "—" else flat(desc), k, "" if cat == "—" else cat, "" if typ == "—" else flat(typ), f], cat, typ))
    return rows


def write(path, rows):
    """The list as CSV. Replaces an older .md table of the same name. False when nothing changed."""
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(COLUMNS)
    w.writerows(rows)
    body = buf.getvalue()
    legacy = path[:-4] + ".md"
    gone = os.path.exists(legacy)
    if gone:
        os.remove(legacy)
    if os.path.exists(path) and open(path, encoding="utf-8").read() == body:
        return gone
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as out:
        out.write(body)
    return True


def summary(area):
    """The first real sentence of an area's README.md — what it is for."""
    try:
        text = open(f"{area}/README.md", encoding="utf-8").read()
    except OSError:
        return "—"
    if text.startswith("---"):
        end = text.find("\n---", 3)
        text = text[end + 4:] if end != -1 else text
    for para in re.split(r"\n\s*\n", text):
        para = " ".join(x.strip() for x in para.splitlines())
        if para and not para.startswith(("#", "_", "|", "```", "-", ">")):
            first = re.split(r"(?<=[.!?])\s", cell(para))[0]
            return first if len(first) <= 160 else first[:159].rsplit(" ", 1)[0] + " …"
    return "—"


def records_dir(folder):
    return "01_RECORDS" if os.path.isdir(f"{folder}/01_RECORDS") and not os.path.isdir(f"{folder}/910_RECORDS") else "910_RECORDS"


def counts(values):
    c = {}
    for v in values:
        if v and v != "—":
            c[v] = c.get(v, 0) + 1
    return " · ".join(f"{k} {n}" for k, n in sorted(c.items(), key=lambda x: (-x[1], x[0]))) or "—"


def main():
    rows = lines()
    changed = []
    areas = {}
    for folder, rs in sorted(rows.items()):
        rs.sort()
        for r in rs:
            areas.setdefault(r[1].split("/")[0], []).append(r)
        if write(f"{folder}/{records_dir(folder)}/INDEX.csv", [r[2] for r in rs]):
            changed.append(folder)
    # Level 2: one full list per top-level area
    summary_rows = []
    for area, rs in sorted(areas.items()):
        rs.sort(key=lambda r: r[1])
        path = f"{area}/{records_dir(area)}/CATALOG.csv"
        if write(path, [r[2] for r in rs]):
            changed.append(f"{area} catalog")
        summary_rows.append(f"| `{area}/` | {summary(area)} | {len(rs)} | {counts(r[3] for r in rs)} | {counts(r[4] for r in rs)} | `{path}` |")
    # Level 1: the areas, with counts — read this first, then the area's catalog
    intro = ("Start here to find anything. One line per area: what it holds, how many saved files, by\n"
             "category and by type, and where its full list is. Open that area’s catalog next, then the\n"
             "file. Rebuilt after every push — never edit by hand. Root `AGENTS.md` §Routing.")
    head = "| Area | What it holds | Files | Categories | Types | Full list |\n|---|---|---|---|---|---|"
    body = f"# Catalog\n\n{intro}\n\n{head}\n" + "".join(r + "\n" for r in summary_rows)
    old = open(CATALOG, encoding="utf-8").read() if os.path.exists(CATALOG) else ""
    if not old.endswith(body):
        os.makedirs(os.path.dirname(CATALOG), exist_ok=True)
        with open(CATALOG, "w", encoding="utf-8") as out:
            out.write(f"---\ntitle: Catalog\nstatus: draft\nreviewed_by: none\nlast_verified: {datetime.date.today().isoformat()}\n---\n\n{body}")
        changed.append("catalog")
    print(f"{len(rows)} folder logs, {len(areas)} areas, {sum(len(r) for r in areas.values())} files; updated: {', '.join(changed) or 'nothing'}")


if __name__ == "__main__":
    main()
