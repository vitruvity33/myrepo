---
title: MyRepo
status: draft
last_verified: 2026-09-29
---

# MyRepo

**Keep your context in a repo you own.**

A governed knowledge repository built so any AI tool — ChatGPT, Claude, Devin,
Codex — can pick up your context, do work, and save results without you
re-explaining anything. The tools don't talk to each other. **The repo is the
interface.**

## What this is

Every AI conversation starts from zero and ends in a chat window. Decisions,
research, preferences and corrections evaporate. This repo is where they land
instead — structured so any tool can find them later, and so the *reasoning path*
survives, not just the conclusion.

## The shape

- **Areas** are numbered top-level folders (`10_`, `20_` …) — the domains that
  matter to you. Each carries `AGENTS.md` (rules for agents) + `README.md`
  (orientation for people) + `01_RECORDS/` (the back-end log of what's saved).
- **Sub-areas** are unnumbered folders inside an area with the same shape —
  a person inside a people area, a topic inside a research area.
- **Every record answers three questions** from its front-matter: what it's about,
  what kind of statement it is, how much to trust it.
- **Agents write drafts. People promote.** Merge ≠ promotion.

## Adopt it

1. Clone this template into a repo you own.
2. Name your areas in `01_READ_FIRST/02_AREA_MAP.md` — start with few, add later.
   The shipped folders (`01_READ_FIRST`, `02_REFERENCES`, `99_OTHER`) are the
   machinery, not your taxonomy.
3. Set your name as context reviewer in `AGENTS.md`.
4. Connect your AI tools — see `01_READ_FIRST/03_HOW_TO_USE_WITH_AI.md`.

## For humans

Start at `01_READ_FIRST/01_START_HERE.md`.

## For AI agents

Read `AGENTS.md` at the root, then the `AGENTS.md` of whatever area you're
working in.

## The one rule to remember

**A folder owns what dies with it.** Endeavors (projects, applications) archive;
entities (people, research, preferences) are permanent and get referenced, not
absorbed.

---

Built on the governed-repository pattern — company → department → product,
person → area → subject. Same rules at every level.
