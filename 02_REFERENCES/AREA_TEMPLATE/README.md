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

A topic (a sub-area for one subject, practice or field) is laid out so a person
can browse it. First, which kind it is — tell from how the owner talks, or ask:

- **Study topic** — learned over time ("I want to learn…"). Gets the files below, then a shape.
- **Reference topic** — kept to look up and build with ("save this, I'll need
  it"). Gets the Reference shape and no study tracking; what matters is finding
  things fast and the trust label on each record (`evidence` with a source vs
  `analysis`). It becomes a study topic when the owner starts studying it.

Topics differ, so the layout is chosen per topic, from a short menu, and written
into the topic's `AGENTS.md` §Layout. The menu is set in MyRepo (repo ⚙ → Studying).

**In every study topic:**

| File | Holds |
|---|---|
| `RESOURCES.md` | Trusted reading — primary texts, books, papers, reference sources. Each with its link and what it contributes |
| `STUDY_TRACKING/` | `STUDY_QUEUE.md` (what's next) · `READING_QUEUE.md` · `PEOPLE_TO_EXPLORE.md` · `STUDIED.md` (what was actually studied — only the owner marks things done) |

**Then one shape:**

| Shape | Fits | Index files |
|---|---|---|
| Things in the world | architecture, anthropology, history | `PEOPLE.md` · `PLACES.md` · `WORKS.md` · `IDEAS.md` |
| Concepts and practice | philosophies, internal arts, awareness | `CONCEPTS.md` · `PRACTICES.md` · `PEOPLE.md` (teachers, lineages) |
| Progression | a skill: stretching, a language, an instrument | `FOUNDATIONS.md` · `TECHNIQUES.md` (in study order, each with a level, basic → advanced) |
| Method | a system that makes claims: a therapy, a framework | `METHODS.md` · `CONCEPTS.md` (incl. how to judge it) · `PEOPLE.md` |
| Reference | knowledge kept to look up: a technology, a field you build in | `CONCEPTS.md` · `SYSTEMS.md` (products, tools, implementations) · `PATTERNS.md` (reusable designs) |
| Its own | anything else | whatever fits — written down in the topic's `AGENTS.md` |

**How to choose:** when a topic is created — or once it holds a few files and
it's clear what it is — propose a shape with one line of why, and ask. Use the
names above so topics stay alike; add a kind only when the topic needs it.

**Many topics on one subject?** Make a group folder (`ai-infra/`) with one topic
per subject inside (`memory-and-context/`, `databases/`), not siblings sharing a
prefix (`ai-infra-chats/`, `ai-infra-dbs/`). Name a topic after what it is about,
not where the material came from.

**Start flat.** Each kind is one index file (a table) while the topic is small.
Give it a folder (`techniques/`, `people/`) once 3 or more entries need their
own pages; the index then links to them. Levels, favorites and queues are
fields and views, not folders — a technique that proves harder changes its
`level:`, it doesn't move.
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
- [ ] A topic: its shape proposed with a reason, chosen by the owner, and written in its `AGENTS.md` §Layout (§Topic layouts)
