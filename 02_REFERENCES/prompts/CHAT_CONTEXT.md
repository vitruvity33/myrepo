---
title: Chat context block
status: draft
last_verified: 2026-09-29
---

# Paste-in context for tools that can't read the repo

Paste this at the start of a ChatGPT/claude.ai/Gemini conversation that will
touch repo knowledge. Keep it current — it's the tool's only view of the rules.
**Replace the placeholder area list with yours after setup** — regenerate this
block whenever `01_READ_FIRST/02_AREA_MAP.md` changes.

```
You are working inside my personal knowledge repo. You can't read it, so here
are the rules that matter:

STRUCTURE
- Areas: <list your areas — e.g. 10_GOVERNANCE, 30_PEOPLE, 40_PROJECTS,
  50_RESEARCH> plus 99_OTHER (catch-all).
- Each area has 01_RECORDS/ with slots: 00_INBOX, 01_GOALS, 02_QUESTIONS,
  03_REFERENCES, 04_MODELS, 05_PUSH_BACK, 06_DECISIONS, 99_ARCHIVE.
- Ownership rule: a folder owns what dies with it. Permanent things (people,
  research topics, preferences) live outside time-boxed endeavors.

WHEN I ASK YOU TO SAVE SOMETHING — any wording — emit a SAVE block:
  SAVE
  path: <full path>/YYYY-MM-DD_TOPIC.md
  ---
  <complete file>

Every record needs front-matter answering three questions:
  1. subject: or subject_text:   — what it's about
  2. context_type:               — decision|outcome|assumption|known_issue|
                                   methodology|definition|dispute|preference
     (context_type routes the folder; record_form:
     conversation|artifact|source_document|note describes the container)
  3. status: draft, confidence:, raised_by:, source:, reviewed_by: none

RULES
- status is ALWAYS draft; only I promote to canonical.
- If you disagree with something in the repo — or I say it's wrong — that's
  mandatory push-back: emit a SAVE block for the area's 05_PUSH_BACK/.
- If I correct your tone/format, also propose a SAVE to
  02_REFERENCES/preferences/ (scope: global or artifact_type) unless the
  correction is specific to one project.
- If you can't tell where it goes, SAVE to 99_OTHER/01_RECORDS/00_INBOX/
  with subject_text: filled in. Never drop it.
- End of a substantive conversation: propose what deserves saving.

MY QUESTION:
```
