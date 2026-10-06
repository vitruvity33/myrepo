#!/usr/bin/env python3
"""Rebuild every folder's log (01_RECORDS/INDEX.md) and the repo's catalog
(01_READ_FIRST/04_CATALOG.md) from the files actually in the repo.

Runs after every push to main (.github/workflows/catalog.yml), so the catalog
is complete whichever tool saved a file. Root AGENTS.md §Routing.

A line per saved file: date | title | kind | category | path. The category
comes from the header's context_type (decision → 06_DECISIONS, analysis →
04_MODELS …), else the folder type it sits in (15_CONCEPTS …), else 00_INBOX
for a record that isn't sorted yet. Each file is logged in the nearest folder
above any folder-type folder (a concept page in topic/15_CONCEPTS/ is in the
topic's log). Back-end files — AGENTS.md, README.md, FOCUS.md, 01_RECORDS/,
push-back, 90_TRACKING/, work/ — are not listed. A file is rewritten only when
its lines change.
"""

import datetime
import json
import os
import re
import subprocess

ROUTE = {
    "decision": "06_DECISIONS", "outcome": "06_DECISIONS",
    "assumption": "02_QUESTIONS", "known_issue": "02_QUESTIONS",
    "methodology": "03_REFERENCES", "definition": "03_REFERENCES", "evidence": "03_REFERENCES",
    "analysis": "04_MODELS",
}
SLOTTED = {"00_INBOX", "02_QUESTIONS", "03_REFERENCES", "04_MODELS", "06_DECISIONS"}
SETTINGS = "02_REFERENCES/REPO_SETTINGS.json"
CATALOG = "01_READ_FIRST/04_CATALOG.md"
NUM = re.compile(r"^\d+_")
RULES = {"AGENTS.md", "README.md", "FOCUS.md", "INDEX.md"}
MACHINERY = {"01_READ_FIRST", "02_REFERENCES"}
HEAD = "| Date | Title | Kind | Category | File |\n|---|---|---|---|---|"


def routes():
    """The repo's own kinds (repo ⚙ → Classifications) when it has them."""
    try:
        kinds = json.load(open(SETTINGS))["classifications"]
    except (OSError, ValueError, KeyError, TypeError):
        return ROUTE
    out = dict(ROUTE)
    for k in kinds:
        if isinstance(k, dict) and isinstance(k.get("type"), str) and k.get("slot") in SLOTTED:
            out[k["type"]] = k["slot"]
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


def backend(parts):
    return any(
        p.startswith(".") or p in ("01_RECORDS", "work")
        or re.match(r"^\d+_PUSH_BACK$", p, re.I) or re.match(r"^\d+_TRACKING$", p, re.I)
        for p in parts
    )


def log_folder(dirs):
    for i in range(1, len(dirs)):
        if NUM.match(dirs[i]):
            return "/".join(dirs[:i]), dirs[i]
    return "/".join(dirs), None


def cell(s):
    return re.sub(r"\s+", " ", s.replace("|", "\\|")).strip()


def lines():
    route = routes()
    files = subprocess.check_output(["git", "ls-files"], text=True).splitlines()
    rows = {}
    for f in files:
        p = f.split("/")
        if len(p) < 2 or not NUM.match(p[0]) or p[0] in MACHINERY or not re.search(r"\.(md|csv|tsv)$", f, re.I):
            continue
        # a page written as README.md in an item folder (topic/15_CONCEPTS/x/README.md) is content
        item_readme = p[-1] == "README.md" and any(NUM.match(x) for x in p[1:-2])
        if (p[-1] in RULES and not item_readme) or backend(p[:-1]) or not os.path.exists(f):
            continue
        meta, h1 = header(f) if f.lower().endswith(".md") else ({}, None)
        kind = meta.get("context_type", "").lower()
        folder, typed = log_folder(p[:-1])
        cat = route.get(kind) or typed or ("00_INBOX" if meta.get("kind") == "record" or kind else "—")
        m = re.match(r"^(\d{4}-\d{2}-\d{2})", p[-1])
        date = m.group(1) if m else next(
            (meta[k][:10] for k in ("date", "created", "last_verified") if re.match(r"^\d{4}-\d{2}-\d{2}", meta.get(k, ""))), "—")
        title = meta.get("title") or h1 or re.sub(r"\.[^.]+$", "", p[-1])
        k = f"`{kind}`" if kind else (f"`{meta['kind']}`" if meta.get("kind") else "—")
        rows.setdefault(folder, []).append((date, f, f"| {date} | {cell(title)} | {k} | {cat} | `{f}` |"))
    return rows


def write(path, title, intro, rows):
    body = f"# {title}\n\n{intro}\n\n{HEAD}\n" + "".join(r + "\n" for r in rows)
    if os.path.exists(path):
        old = open(path, encoding="utf-8").read()
        if old.endswith(body):
            return False
    today = datetime.date.today().isoformat()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as out:
        out.write(f"---\ntitle: {title.replace('`', '')}\nstatus: draft\nreviewed_by: none\nlast_verified: {today}\n---\n\n{body}")
    return True


def main():
    rows = lines()
    changed = []
    every = []
    for folder, rs in sorted(rows.items()):
        rs.sort()
        every += rs
        intro = ("What’s saved in this folder: one line per file — what kind of statement it is, its\n"
                 "category, and where it is. For agents and the back end; people browse the folder itself.\n"
                 "The whole repo’s: `01_READ_FIRST/04_CATALOG.md`. Rebuilt after every push. Root `AGENTS.md` §Routing.")
        if write(f"{folder}/01_RECORDS/INDEX.md", f"Log — `{folder}/`", intro, [r for _, _, r in rs]):
            changed.append(folder)
    every.sort(key=lambda r: r[1])
    intro = ("Every saved file in this repo, one line each — what kind of statement it is, its category\n"
             "and where it is. Read this first to find anything; each folder keeps the same lines in\n"
             "its own `01_RECORDS/INDEX.md`. Rebuilt after every push. Root `AGENTS.md` §Routing.")
    if write(CATALOG, "Catalog", intro, [r for _, _, r in every]):
        changed.append("catalog")
    print(f"{len(rows)} folder logs, {len(every)} files; updated: {', '.join(changed) or 'nothing'}")


if __name__ == "__main__":
    main()
