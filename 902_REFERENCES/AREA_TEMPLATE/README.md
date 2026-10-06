---
title: Area Template
status: draft
last_verified: 2026-10-02
---

# Area Template

**Copy this shape for every new area or sub-area.** Consistency is what makes the
repo navigable by an agent that cannot ask questions.

```
NN_AREA_NAME/                  your number (never starting with 9); sub-areas: optional
├── AGENTS.md                  REQUIRED. Scoped rules, ID prefix, what belongs here
├── README.md                  REQUIRED. Orientation for people
├── FOCUS.md                   optional. What the owner is after here — agents read it
│                              before suggesting anything (root AGENTS.md §Focus)
├── 910_RECORDS/               The back end — never the owner's content:
│   ├── INDEX.md               the log: every saved file, its category, where it is
│   ├── 911_GOALS/             00_GOALS.md — aligns_with: one level up
│   └── 915_PUSH_BACK/         disputes about this folder
├── 990_TRACKING/              back end — the AI's lists (queue, research, decisions needed)
├── YYYY-MM-DD_TOPIC.md        saved files live here, in the folder (or one inside it)
└── work/                      unvalidated space — drafts, artifacts-in-progress
```

## First-use area check

Use this template when creating a new area or sub-area (for example, a project,
research topic, person, or company endeavor). Read root and parent `AGENTS.md`
first. Create `AGENTS.md` and `README.md` in the new area in the same
change, then complete the checklist below.

Every folder for the owner's content inside it gets its own `AGENTS.md` +
`README.md` too, at any depth, in the same change (root `AGENTS.md` §Every folder
gets AGENTS.md + README.md). Only the back-end folders —
`910_RECORDS/`, `990_TRACKING/` and `work/` — don't.

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

## This folder's purpose (optional, in AGENTS.md)

When the owner and an AI work out how a folder should work — what it's for, how
to find things in it, how to talk with the owner there, its own stages — write it
into the folder's `AGENTS.md`, outside any MyRepo markers:

```markdown
## This folder's purpose
<One or two lines: what this folder is for, in the owner's words.>

- **How to work here:** …
- **Stages (instead of the queue):** …
- **Pages and folders:** …
```

It shapes the work in this folder and everything under it — never the root rules
(root `AGENTS.md` §A folder's purpose).

<!-- myrepo:begin topic-layouts -->
## Topic layouts

Every topic (one subject, practice or field) is laid out the same way, so the owner
and every AI tool always know where to look. The list of kinds is set in MyRepo
(repo ⚙ → Topic types); each topic's choice is in its `AGENTS.md` (folder ⚙ → Topic type).
How agents work in a topic: root `AGENTS.md` §Working in a topic.

**Explore → investigate → confirm** happens item by item, in the queue every folder keeps
(root `AGENTS.md` §The queue) — not by labelling the topic.

**Every topic has:**

```
topic/
  STUDY_GUIDE.md        ← what to learn, in what order, how to judge it (any topic that has a method)
  LEARNING_PATH.md      ← how one question led to the next — sparse, one entry per turn
  HISTORY.md            ← how the field developed — links to its people, groups, works
  10_PEOPLE/            ← first-last/PROFILE.md + WORKS.md
  11_GROUPS/            ← one page per item
  12_PERIODS/           ← one page per item
  …                     ← only the kinds this topic holds; each folder has its own AGENTS.md + README.md
  990_TRACKING/         ← the owner’s progress: TO_EXPLORE.md, STUDIED.md, READING_QUEUE.md, FAVORITES.md
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
its own — something merely interesting is a row in `990_TRACKING/TO_EXPLORE.md`, something
mentioned in passing lives inside the page it belongs to (a building in its architect’s `WORKS.md`). No stubs, no
“not written yet”. A page grows into a folder only when it needs more than one file.
Pages hold no status: “queued”, “studied”, “favorite” live only in `990_TRACKING/`.
Concept pages mark their origin (`origin: established` or `origin: owner`). Historical
context of the field is `HISTORY.md`; the owner’s own path through the topic is `LEARNING_PATH.md`. Levels are a field
on a practice's page, never folders.

**Titles stay short inside a topic** — "People", "Reading queue", not
"People — Body Awareness".

**Many topics on one subject?** Make a group folder (`ai-infra/`) with one topic
per subject inside (`memory-and-context/`, `databases/`), not siblings sharing a
prefix (`ai-infra-chats/`, `ai-infra-dbs/`). Name a topic after what it is about,
not where the material came from.
<!-- myrepo:end topic-layouts -->

<!-- myrepo:begin folder-types -->
## Folder types

One menu for every kind of work (Study, Research, Idea, Decide, Plan, Initiative, Operation). Each kind suggests
some types; any folder may use any of them. A type keeps the same number everywhere; its
folder appears with its first page, together with its own `AGENTS.md` + `README.md`.

| Folder | Holds | Suggested for |
|---|---|---|
| `10_PEOPLE/` | a folder per person — PROFILE.md (who they are, their story, why they matter here) and WORKS.md | Study |
| `11_GROUPS/` | schools, movements, organizations, lineages | Study |
| `12_PERIODS/` | eras and events worth studying on their own | Study |
| `13_WORKS/` | buildings, books, artworks — studied as objects in themselves | Study |
| `14_PLACES/` | real locations | Study |
| `15_CONCEPTS/` | ideas, principles and terms | Study, Idea |
| `16_PRACTICES/` | techniques, methods, exercises — things you do (with a level when there is an order) | Study |
| `17_SYSTEMS/` | products, tools and implementations (technology topics) | Study |
| `18_PATTERNS/` | reusable designs (technology topics) | Study |
| `19_RESOURCES/` | what you learn from — books, papers, courses, videos — each with its link and what it contributes | Study, Idea |
| `30_SOURCES/` | where information came from — reports, sites, documents — each with its link | Research, Decide, Plan |
| `31_EVIDENCE/` | facts that support or challenge a claim, each tied to its source | Research, Decide, Plan |
| `32_INTERVIEWS/` | conversations with people, and what was learned from each | — |
| `33_DATA/` | numbers and datasets, and where they came from | Research, Plan |
| `34_EXPERIMENTS/` | tests that were run — what was tried, how, and what happened | Research |
| `35_RESULTS/` | what came out of the work — outcomes, findings, numbers | Initiative |
| `36_OPTIONS/` | the choices on the table, side by side | Idea, Decide, Plan, Initiative |
| `37_PLANS/` | how something will get done — steps, order, who | Initiative |
| `38_WORKSTREAMS/` | parallel strands of the work, each with its own owner | Initiative |
| `39_TIMELINE/` | milestones and target dates | — |
| `40_RESPONSIBILITIES/` | who does each part, and who covers when they’re out — only what people have agreed to | — |
| `41_DEPENDENCIES/` | what this needs from other people or systems, and what relies on it | — |
| `42_SCHEDULE/` | how often something happens, deadlines and the calendar | — |
| `43_RESEARCH/` | what was looked into for this work (a folder type — not the Research kind of work) | — |
| `44_DESIGN/` | how it should look and work | — |
| `45_BUILD/` | how it is being made, and what exists so far | — |
| `46_LAUNCH/` | getting it out — rollout, announcements, first use | — |
| `47_REVIEW/` | looking back — what happened against what was expected (a folder type — not reviewing in conversation) | — |
| `48_PROCESSES/` | how something is done, step by step — a page per process | Operation |
| `49_CHECKLISTS/` | steps to run through each time | Operation |
| `50_RUNS/` | notes on a single run — only when something was unusual | Operation |
| `51_MEASURES/` | what is watched, and the range that counts as normal | Operation |
| `52_INCIDENTS/` | when something went wrong — what happened, the fix, what changes | — |
| `53_IMPROVEMENTS/` | changes worth trying to make it work better | Operation |


**Every folder also keeps a queue by default** — explore → investigate → confirm — in `990_TRACKING/`: `TO_EXPLORE.md` → `STUDIED.md` → `FAVORITES.md`, made on first use (root `AGENTS.md` §The queue); a folder may define its own stages instead. Ask “what's next?” in any chat.

Set in MyRepo (repo ⚙ → Topic types).
<!-- myrepo:end folder-types -->

## Numbering

- **Top-level areas start with a number** — any length, unused by another
  top-level folder, no fixed meaning (`10_`, `620_`, `0622_`). Pick one that
  sorts next to the most related area; add digits to refine (`60_` → `620_` →
  `622_`). Never start with 9 — that's MyRepo's back end (root `AGENTS.md`
  §Numbers). Full steps: root `AGENTS.md` §Creating a top-level area.
- **Sub-areas** may be unnumbered, or numbered the same way (`33_` → `335_`) — never with 9.
- **Never renumber** — it breaks every cross-reference.

## Every area's AGENTS.md must contain

1. Area name and ID prefix
2. What belongs to this area (and what doesn't)
3. What gets saved here, and how it's logged (`910_RECORDS/INDEX.md`)
4. Rules specific to the area
5. Pointer to root `AGENTS.md` (full path from root)
6. Push-back section — `915_PUSH_BACK/`, `YYYY-MM-DD_TOPIC.md`
7. Context reviewer: the repo owner

## Checklist for a new area

- [ ] Folder created (top level: unused number, told to the owner first · sub-area: no number)
- [ ] `AGENTS.md` + `README.md` written **in the same operation**
- [ ] If goals exist: `910_RECORDS/911_GOALS/00_GOALS.md` with `aligns_with:` up one level
- [ ] ID prefix registered in `902_REFERENCES/ID_REGISTRY.md`
- [ ] Area added to `901_READ_FIRST/02_AREA_MAP.md`
- [ ] Top level: area added to the list in `902_REFERENCES/prompts/CHAT_CONTEXT.md`
- [ ] Saved files go in the folder, each with a line in `910_RECORDS/INDEX.md` and `901_READ_FIRST/04_CATALOG.md`
- [ ] A topic: what it is for and the kinds it holds, proposed with a reason, chosen by the owner, and recorded in its `AGENTS.md` (folder ⚙ → Topic; §Topic layouts)
