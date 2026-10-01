---
title: Area Template
status: draft
last_verified: 2026-10-01
---

# Area Template

**Copy this shape for every new area or sub-area.** Consistency is what makes the
repo navigable by an agent that cannot ask questions.

```
NN_AREA_NAME/                  top level: unused number, any length. Sub-area: no number
├── AGENTS.md                  REQUIRED. Scoped rules, ID prefix, slot menu
├── README.md                  REQUIRED. Orientation for people
├── FOCUS.md                   optional. What the owner is after here — agents read it
│                              before suggesting anything (root AGENTS.md §Focus)
├── 01_RECORDS/                The governed layer. Slots are a menu — create on
│   │                          first use; every area can use:
│   ├── 00_INBOX/              unsorted captures — never cite
│   ├── 01_GOALS/              goals with aligns_with: one level up
│   ├── 02_QUESTIONS/          assumptions, known issues
│   ├── 03_REFERENCES/         methods, definitions, source docs, conversations
│   ├── 04_MODELS/             scenarios, comparisons, projections
│   ├── 05_PUSH_BACK/          disputes about this area
│   ├── 06_DECISIONS/          decisions + outcomes
│   └── 99_ARCHIVE/            superseded — never cite
└── work/                      unvalidated space — drafts, artifacts-in-progress
```

## FOCUS.md (optional)

One `##` section per focus; a folder can have several. Applies to the folder and
everything under it.

```markdown
# Focus — <folder>

## <What I'm after>
<One line: why, or where this started.>

- **Looking for:** …
- **Not looking for:** …
- **Already covered:** …
- **Status:** active
```

## Numbering

- **Top-level areas start with a number** — any length, unused by another
  top-level folder, no fixed meaning (`10_`, `620_`, `0622_`). Pick one that
  sorts next to the most related area; add digits to refine (`60_` → `620_` →
  `622_`). `01_`/`02_` are MyRepo's. Full steps: root `AGENTS.md`
  §Creating a top-level area.
- **Sub-areas are unnumbered** folders with their own `AGENTS.md`.
- **Never renumber** — it breaks every cross-reference.

## Every area's AGENTS.md must contain

1. Area name and ID prefix
2. What belongs to this area (and what doesn't)
3. Which `01_RECORDS/` slots are in use and why
4. Rules specific to the area
5. Pointer to root `AGENTS.md` (full path from root)
6. Push-back section — `05_PUSH_BACK/`, `YYYY-MM-DD_TOPIC.md`
7. Context reviewer: the repo owner

## Checklist for a new area

- [ ] Folder created (top level: unused number, told to the owner first · sub-area: no number)
- [ ] `AGENTS.md` + `README.md` written **in the same operation**
- [ ] If goals exist: `01_RECORDS/01_GOALS/00_GOALS.md` with `aligns_with:` up one level
- [ ] ID prefix registered in `02_REFERENCES/ID_REGISTRY.md`
- [ ] Area added to `01_READ_FIRST/02_AREA_MAP.md`
- [ ] Top level: area added to the list in `02_REFERENCES/prompts/CHAT_CONTEXT.md`
- [ ] Other slots appear on first use — not before
