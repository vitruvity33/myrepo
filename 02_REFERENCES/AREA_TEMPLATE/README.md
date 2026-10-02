---
title: Area Template
status: draft
last_verified: 2026-10-02
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
│   ├── 03_REFERENCES/         sourced facts (evidence), methods, definitions —
│   │                          what you can rely on
│   ├── 04_MODELS/             analysis: interpretations, proposed designs,
│   │                          comparisons, scenarios — not facts
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

<!-- myrepo:begin topic-layouts -->
## Topic layouts

Every topic (one subject, practice or field) is laid out the same way, so the owner
and every AI tool always know where to look. The list of kinds is set in MyRepo
(repo ⚙ → Studying); each topic's choice is in its `AGENTS.md` (folder ⚙ → Topic).
How agents work in a topic: root `AGENTS.md` §Working in a topic.

**What the topic is for** — tell from how the owner talks, or ask:

- **Explore** — curiosity: things the owner is drawn to and collects (architects, CEOs).
- **Study** — learning over time, in an order (a stretching method, a practice).
- **Reference** — kept to look up and build with (a technology).

**Every topic has:**

```
topic/
  STUDY_GUIDE.md        ← what to learn, in what order, how to judge it (any topic that has a method)
  LEARNING_PATH.md      ← how one question led to the next — sparse, one entry per turn
  HISTORY.md            ← how the field developed — links to its people, groups, works
  10_PEOPLE/            ← first-last/PROFILE.md + WORKS.md
  11_GROUPS/            ← one page per item
  12_PERIODS/           ← one page per item
  …                     ← only the kinds this topic holds; a folder appears with its first page
  90_TRACKING/          ← the owner’s progress: TO_EXPLORE.md, STUDIED.md, READING_QUEUE.md, FAVORITES.md
```

**The kinds** — one list for every topic; the number comes from the list order:

| Folder | Holds |
|---|---|
| `10_PEOPLE/` | a folder per person — PROFILE.md (who they are, their story, why they matter here) and WORKS.md |
| `11_GROUPS/` | schools, movements, organizations, lineages |
| `12_PERIODS/` | eras and events worth studying on their own |
| `13_WORKS/` | buildings, books, artworks — studied as objects in themselves |
| `14_PLACES/` | real locations |
| `15_CONCEPTS/` | ideas, principles and terms |
| `16_PRACTICES/` | techniques, methods, exercises — things you do (with a level when there is an order) |
| `17_SYSTEMS/` | products, tools and implementations (technology topics) |
| `18_PATTERNS/` | reusable designs (technology topics) |
| `19_RESOURCES/` | what you learn from — books, papers, courses, videos — each with its link and what it contributes |

**Rules:** a page exists only when there is substantive knowledge worth retrieving on
its own — something merely interesting is a row in `90_TRACKING/TO_EXPLORE.md`, something
mentioned in passing lives inside the page it belongs to (a building in its architect’s `WORKS.md`). No stubs, no
“not written yet”. A page grows into a folder only when it needs more than one file.
Pages hold no status: “queued”, “studied”, “favorite” live only in `90_TRACKING/`.
Concept pages mark their origin (`origin: established` or `origin: owner`). Historical
context of the field is `HISTORY.md`; the owner’s own path through the topic is `LEARNING_PATH.md`. Levels are a field
on a practice's page, never folders.

**Titles stay short inside a topic** — "People", "Reading queue", not
"People — Body Awareness".

**Many topics on one subject?** Make a group folder (`ai-infra/`) with one topic
per subject inside (`memory-and-context/`, `databases/`), not siblings sharing a
prefix (`ai-infra-chats/`, `ai-infra-dbs/`). Name a topic after what it is about,
not where the material came from.

**Areas, Research, Initiatives and Operations** are laid out differently — an area keeps
`OVERVIEW.md`, `DECISIONS.md` and `GAPS.md`; research starts with `QUESTION.md`; an initiative
with `OVERVIEW.md`; an operation with `PROCESS.md`. Root `AGENTS.md` §Folder contexts and
conversation modes has all of them.
<!-- myrepo:end topic-layouts -->

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
- [ ] A topic: what it is for and the kinds it holds, proposed with a reason, chosen by the owner, and recorded in its `AGENTS.md` (folder ⚙ → Topic; §Topic layouts)
