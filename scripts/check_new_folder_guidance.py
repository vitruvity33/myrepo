#!/usr/bin/env python3
"""Check what a push adds: new governed folders need their rules, new records a header.

Runs on every push to main and every pull request (.github/workflows/new-folder-guidance.yml).
Nothing here is hardcoded to this repo's areas — they are read from the tree:

1. Every new folder for the owner's content, at any depth (60_FINANCE/,
   10_Wedding/Costs/, 50_LEARNING/acoustics/30_SOURCES/ …), needs AGENTS.md and
   README.md in the same push. Back-end folders don't: 01_RECORDS and its slot
   folders (00_INBOX …), push-back folders, work, and anything outside the areas.
2. The owner's content lives in content folders, never inside 01_RECORDS/ (the
   back end): a new file in 01_RECORDS/00_INBOX, 02_QUESTIONS, 03_REFERENCES,
   04_MODELS or 06_DECISIONS fails. (The logs and the catalog are rebuilt after
   every push by scripts/build_catalog.py, so a missing line isn't a failure.)
   New push-back, goals and archive files need front-matter.
3. A new top-level area starts with a number nobody else uses. Numbers can be
   any length (60_, 620_, 0622_) and mean nothing on their own — they only
   keep areas in order. A new top-level folder with AGENTS.md or README.md but
   no number, or with a number another top-level folder already has, fails.
4. A dispute or correction goes in a push-back folder, and `evidence` must name
   its source in source_refs, for any saved file added or changed. The kinds
   come from 02_REFERENCES/REPO_SETTINGS.json (set in MyRepo → Classifications)
   when the repo has it; the template's defaults otherwise.
"""

import argparse
import json
import re
import subprocess
import sys

STRUCTURAL_NAMES = {
    "00_INBOX", "01_RECORDS", "01_GOALS", "02_QUESTIONS", "03_REFERENCES",
    "04_MODELS", "05_PUSH_BACK", "06_DECISIONS", "99_ARCHIVE", "work",
}
REPO_MACHINERY = {"01_READ_FIRST", "02_REFERENCES"}
RULES_FILES = {"README.md", "AGENTS.md", "FOCUS.md"}
RECORD_FOLDERS = STRUCTURAL_NAMES - {"work"}
NUMBERED = re.compile(r"^(\d+)_")


ROUTES = {
    "decision": "06_DECISIONS", "outcome": "06_DECISIONS",
    "assumption": "02_QUESTIONS", "known_issue": "02_QUESTIONS",
    "methodology": "03_REFERENCES", "definition": "03_REFERENCES", "evidence": "03_REFERENCES",
    "analysis": "04_MODELS",
    "dispute": "PUSH_BACK", "correction": "PUSH_BACK",
}
NEEDS_SOURCE = {"evidence"}
ROUTED_SLOTS = {"02_QUESTIONS", "03_REFERENCES", "04_MODELS", "06_DECISIONS"}
SETTINGS = "02_REFERENCES/REPO_SETTINGS.json"
CONTENT_SLOTS = {"00_INBOX", "02_QUESTIONS", "03_REFERENCES", "04_MODELS", "06_DECISIONS"}
PUSH_BACK = re.compile(r"^\d+_PUSH_BACK$", re.IGNORECASE)


def git(*args):
    return subprocess.check_output(["git", *args], text=True, stderr=subprocess.DEVNULL)


def tracked_files(ref):
    return set(git("ls-tree", "-r", "--name-only", ref).splitlines())


def directories(files):
    found = set()
    for filename in files:
        parts = filename.split("/")
        found.update("/".join(parts[:i]) for i in range(1, len(parts)))
    return found


def is_area(top):
    return bool(NUMBERED.match(top)) and top not in REPO_MACHINERY and not top.endswith("_PUSH_BACK")


def requires_local_guidance(path):
    parts = path.split("/")
    if any(p.startswith(".") or p in STRUCTURAL_NAMES or PUSH_BACK.match(p) for p in parts):
        return False
    return is_area(parts[0])


def number_of(name):
    found = NUMBERED.match(name)
    return found.group(1) if found else None


def top_level_problems(new_dirs, head_files):
    tops = {d for d in directories(head_files) if "/" not in d}
    problems = []
    for path in new_dirs:
        if "/" in path or path.startswith("."):
            continue
        num = number_of(path)
        if num is None:
            if f"{path}/AGENTS.md" in head_files or f"{path}/README.md" in head_files:
                problems.append(f"{path}/ — new top-level area without a number (e.g. 60_{path})")
            continue
        clash = sorted(t for t in tops if t != path and number_of(t) == num)
        if clash:
            problems.append(f"{path}/ — number {num} is already used by {', '.join(clash)}; pick an unused one")
    return problems


def needs_header(path):
    parts = path.split("/")
    return (
        path.lower().endswith(".md")
        and len(parts) > 1
        and is_area(parts[0])
        and parts[-1] not in RULES_FILES
        and any(p in RECORD_FOLDERS for p in parts[:-1])
    )


def has_front_matter(path):
    try:
        head = git("show", f"HEAD:{path}")[:4]
    except subprocess.CalledProcessError:
        return True
    return head.lstrip("﻿").startswith("---")


def front_matter(path):
    try:
        text = git("show", f"HEAD:{path}").lstrip("\ufeff")
    except subprocess.CalledProcessError:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    return text[3:end] if end != -1 else None


def field(head, name):
    """A front-matter value, and whether a list under it has items."""
    lines = head.splitlines()
    for i, line in enumerate(lines):
        if line.startswith(f"{name}:"):
            value = line.split(":", 1)[1].split(" #")[0].strip().strip("'\"")
            items = False
            for nxt in lines[i + 1:]:
                if not nxt.startswith((" ", "-")):
                    break
                items = items or nxt.lstrip().startswith("- ")
            return value, items
    return None, False


def slot_of(path):
    for part in path.split("/")[:-1]:
        if PUSH_BACK.match(part):
            return "PUSH_BACK"
        if part.upper() in ROUTED_SLOTS:
            return part.upper()
    return None


def load_routes():
    """The repo's own kinds from its settings file — or the defaults above."""
    try:
        settings = json.loads(git("show", f"HEAD:{SETTINGS}"))
        kinds = settings["classifications"]
    except (subprocess.CalledProcessError, ValueError, KeyError, TypeError):
        return ROUTES, NEEDS_SOURCE
    routes, sourced = {}, set()
    for kind in kinds:
        if not isinstance(kind, dict) or not isinstance(kind.get("type"), str):
            continue
        slot = kind.get("slot")
        if slot == "05_PUSH_BACK":
            routes[kind["type"]] = "PUSH_BACK"
        elif slot in ROUTED_SLOTS:
            routes[kind["type"]] = slot
        if kind.get("needsSource") is True:
            sourced.add(kind["type"])
    return routes, sourced


def routing_problems(changed):
    routes, sourced = load_routes()
    problems = []
    for path in changed:
        if not path.lower().endswith(".md") or path.split("/")[-1] in RULES_FILES:
            continue
        head = front_matter(path)
        if head is None:
            continue
        kind, _ = field(head, "context_type")
        kind = (kind or "").lower()
        if routes.get(kind) == "PUSH_BACK" and slot_of(path) != "PUSH_BACK":
            problems.append(f"{path} — context_type: {kind} belongs in a push-back folder; move it or fix the header")
        if kind in sourced:
            value, items = field(head, "source_refs")
            if not items and value in (None, "", "[]"):
                problems.append(f"{path} — {kind} without source_refs; name the source, or call it an assumption")
    return problems


def in_content_slot(path):
    parts = path.split("/")[:-1]
    return any(p == "01_RECORDS" and i + 1 < len(parts) and parts[i + 1].upper() in CONTENT_SLOTS for i, p in enumerate(parts))


def saved_item_problems(added):
    """The owner's files stay out of the back end (the logs are rebuilt by build_catalog.py)."""
    problems = []
    for path in added:
        parts = path.split("/")
        if len(parts) < 2 or not is_area(parts[0]) or any(p.startswith(".") for p in parts):
            continue
        if in_content_slot(path):
            owner = "/".join(parts[:-1]).split("/01_RECORDS")[0]
            problems.append(f"{path} — saved inside 01_RECORDS/ (the back end); save it in {owner}/ instead")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", required=True, help="commit to compare against")
    args = parser.parse_args()
    base_files = tracked_files(args.base)
    head_files = tracked_files("HEAD")
    new_dirs = sorted(directories(head_files) - directories(base_files))

    problems = []
    for path in new_dirs:
        if requires_local_guidance(path):
            absent = [n for n in ("AGENTS.md", "README.md") if f"{path}/{n}" not in head_files]
            if absent:
                problems.append(f"{path}/ — new folder without {' and '.join(absent)}")
    problems.extend(top_level_problems(new_dirs, head_files))
    changed = git("diff", "--name-only", "--diff-filter=AMR", args.base, "HEAD").splitlines()
    problems.extend(routing_problems(changed))
    added = sorted(head_files - base_files)
    problems.extend(saved_item_problems(added))
    for path in added:
        if needs_header(path) and not in_content_slot(path) and not has_front_matter(path):
            problems.append(f"{path} — new record without a front-matter header (the three questions)")

    if problems:
        print("This push breaks the repo rules (root AGENTS.md):")
        for p in problems:
            print(f"  {p}")
        return 1
    print("Repo rules check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
