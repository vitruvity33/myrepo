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

Every topic (one subject, practice or field) is laid out the way
`50_LEARNING/architecture/` is: a folder for each kind of thing, a page for each
thing studied in depth, and lists that track them. The layout is set in MyRepo
(repo ⚙ → Studying) and the topic's choice in its `AGENTS.md` (folder ⚙ → Topic).

**What the topic is for** — tell from how the owner talks, or ask:

- **Explore** — curiosity: things the owner is drawn to and collects (architects, CEOs).
- **Study** — learning over time, in an order (a stretching method, a practice). Starts
  with `STUDY_GUIDE.md`, the overview read first.
- **Reference** — kept to look up and build with (a technology). Records carry trust
  labels (`evidence` with a source vs `analysis`).

**The test — pages or rows?** What grows by adding a *page per item* (an architect, a
technique, a concept gone into deeply) is a **folder**: `INDEX.md` lists the items, and
each studied item gets its page (`frei-otto/PROFILE.md`, `hold-relax.md`). What grows
by adding *rows* (a queue, favorites, what was studied) is a **file**. Every topic uses
the full layout from day one, however small — nothing is reorganized later.

**Every topic has** its kinds as numbered folders in reading order (`01_`, `02_` …), then:

| Folder | Holds |
|---|---|
| `NN_RESOURCES/` | `INDEX.md`: trusted reading — primary texts, books, papers, reference sources, each with its link and what it contributes. Notes on one source become a page |
| `NN_COLLECTIONS/` | `STUDIED.md` (what was actually studied — only the owner marks things done) · `TO_EXPLORE.md` · `FAVORITES.md` · plus `READING_QUEUE.md` or `PLACES_TO_VISIT.md` where they fit |

**The kinds come from its shape:**

| Shape | Fits | Kind folders |
|---|---|---|
| Things in the world | architecture, anthropology, history | `PEOPLE/` · `PLACES/` · `WORKS/` · `IDEAS/` |
| Concepts and practice | philosophies, internal arts, awareness | `CONCEPTS/` · `PRACTICES/` · `PEOPLE/` |
| Progression | a skill: stretching, a language, an instrument | `FOUNDATIONS/` · `TECHNIQUES/` · `PEOPLE/` |
| Method | a system that makes claims: a therapy, a framework | `METHODS/` · `CONCEPTS/` · `PEOPLE/` |
| Reference | knowledge kept to look up: a technology, a field you build in | `CONCEPTS/` · `SYSTEMS/` · `PATTERNS/` · `DECISIONS/` |
| Its own | anything else | whatever fits — written down in the topic's `AGENTS.md` |

**Studying one thing** = a page in its kind's folder + a row in its `INDEX.md` +
a row in `COLLECTIONS/STUDIED.md` (and `FAVORITES.md` if it resonated). A page starts
with a memory hook, then what it is, what the sources say (linked), what resonated,
and questions left. Levels and favorites are fields and lists, not folders — a
technique that proves harder changes its `level:`, it doesn't move.

**Titles stay short inside a topic** — "People", "Reading queue", not
"People — Body Awareness".

**Many topics on one subject?** Make a group folder (`ai-infra/`) with one topic
per subject inside (`memory-and-context/`, `databases/`), not siblings sharing a
prefix (`ai-infra-chats/`, `ai-infra-dbs/`). Name a topic after what it is about,
not where the material came from.
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
