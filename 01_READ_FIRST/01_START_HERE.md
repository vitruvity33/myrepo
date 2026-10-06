---
title: Start Here
status: draft
last_verified: 2026-09-29
---

# Start Here

**This repository is its owner's personal knowledge base — shared memory for every
AI tool they use.**

The problem it solves: conversations with ChatGPT, Claude, and other tools each
start from zero and end in a chat window. Decisions, research, preferences and
corrections evaporate. This repo is where they land instead — structured so any
tool can find them later, and so the *reasoning path* survives, not just the
conclusion.

## Read in this order

| # | File | What it gives you |
|---|---|---|
| 1 | This file | What the repo is |
| 2 | `01_READ_FIRST/02_AREA_MAP.md` | Which area owns which kind of thing — and the ownership rule |
| 3 | `01_READ_FIRST/03_HOW_TO_USE_WITH_AI.md` | How each class of tool reads and writes |
| 4 | `02_REFERENCES/CONTEXT_ITEM_SPEC.md` | The record format — the three questions |

## The shape

- **Areas** are numbered top-level folders — the domains that matter to the owner.
  Each has `AGENTS.md` (rules) + `README.md` (orientation) + `01_RECORDS/` (the log)
  (governed records).
- **Sub-areas** are unnumbered folders inside an area with the same shape —
  a company inside a job-search area, a person inside a people area.
- **Entities vs endeavors:** endeavors are time-boxed and archive; entities are
  permanent and get referenced. Full rule in root `AGENTS.md`.
- **`work/`** inside an area is unvalidated space — drafts and artifacts.

## Setting up your copy

This repo ships with the machinery only — `01_READ_FIRST/`, `02_REFERENCES/`,
`99_OTHER/`. Your areas are yours:

1. Create a numbered top-level folder per domain — see
   `02_REFERENCES/AREA_TEMPLATE/` for the shape and checklist.
2. Register each area's ID prefix in `02_REFERENCES/ID_REGISTRY.md`.
3. Add it to `01_READ_FIRST/02_AREA_MAP.md`.
4. Set the reviewer name in root `AGENTS.md`.

## Current state

- Everything in this repo is `status: draft` until the owner promotes it.
- Reserved numbers and areas not yet created: see `02_AREA_MAP.md`.
