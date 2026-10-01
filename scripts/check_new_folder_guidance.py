#!/usr/bin/env python3
"""Check what a push adds: new governed folders need their rules, new records a header.

Runs on every push to main and every pull request (.github/workflows/new-folder-guidance.yml).
Nothing here is hardcoded to this repo's areas — they are read from the tree:

1. A new numbered top-level area (e.g. 60_FINANCE/), or a new folder directly
   inside one (e.g. 50_LEARNING/acoustics/), needs AGENTS.md and README.md
   in the same push. Template slot folders (01_RECORDS, 00_INBOX …, work) and
   their contents inherit the area's rules.
2. A new record — a Markdown file inside 01_RECORDS/ or a template slot
   folder (00_INBOX … 06_DECISIONS, 99_ARCHIVE) — needs front-matter (--- … ---)
   so it can answer the three questions (root AGENTS.md). Lists, profiles and
   other views a topic defines in its own AGENTS.md are not records.
"""

import argparse
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
NUMBERED = re.compile(r"^\d{2}_")


def git(*args):
    return subprocess.check_output(["git", *args], text=True)


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
    if parts[-1] in STRUCTURAL_NAMES or parts[-1].startswith("."):
        return False
    if len(parts) == 1:
        return is_area(parts[0])
    return len(parts) == 2 and is_area(parts[0])


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
    for path in sorted(head_files - base_files):
        if needs_header(path) and not has_front_matter(path):
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
