---
title: Agents
status: draft
last_verified: 2026-10-02
---

# AGENTS.md — MyRepo

**Entry point for any AI agent. Read this before answering questions or writing files.**

This repository is the owner's shared memory across AI tools — ChatGPT, Claude,
Devin, and any other tool that can read it. The tools do not talk to each other;
they read this repo and write back through the same conventions. **The repo is the
interface.**

> **This is a template.** Set the owner's name in §Reviewer, register your areas in
> `901_READ_FIRST/02_AREA_MAP.md`, and mint your ID prefixes in
> `902_REFERENCES/ID_REGISTRY.md` as areas are created.

---

## Read this before anything else

**Before working in an area or sub-area, read that area's `AGENTS.md`.**
Not every tool discovers nested instruction files — this rule makes them load-bearing.

Orientation: `901_READ_FIRST/01_START_HERE.md` → `901_READ_FIRST/02_AREA_MAP.md`.

---

## Focus — check it before you suggest anything

A folder may have a `FOCUS.md` next to its `AGENTS.md`: what the owner is after
there right now. **Before suggesting, researching, recommending or saving anything
in a folder, read its `FOCUS.md` and every parent folder's** (the root included) —
fresh each time, never from memory: the owner edits them, often from the MyRepo app.

Each `##` section is one focus, with four rails:

- **Looking for** — what to find and bring.
- **Not looking for** — never suggest these, not even as a contrast.
- **Already covered** — the owner knows these; don't repeat them.
- **Status** — `active` (apply it) · `paused` · `done` (ignore it).

If a request conflicts with an active focus, say so and ask — don't silently
follow either one. When the owner states a new interest or exclusion in
conversation ("I already know that story", "not that kind of person"), propose
adding it to that folder's `FOCUS.md` — a rail left only in a chat window is lost.

---

## A folder's purpose — found in conversation, then written down

A folder's purpose is often discovered while talking, not picked from a menu, and
it can be different in every folder. When a new purpose or way of working emerges —
how a folder should be organised, how to find things in it, how to talk with the
owner there, what stages things move through — **say so and propose writing it into
that folder's `AGENTS.md`** under `## This folder's purpose` (and one line in its
`README.md`). From then on every tool works that way there. Every content folder already has its
own `AGENTS.md` + `README.md` (§Every folder gets AGENTS.md + README.md) — write the
purpose there. When the same way of working shows up in several folders,
propose making it a topic type (MyRepo → repo ⚙ → Topic types).

**What a folder's own rules can change, and what they can't:**

- **Can change** — its purpose, how to navigate it, how to talk with the owner there,
  its own stages (instead of §The queue), its page types and folders.
- **Can't change** — asking before saving and showing the plan · record headers and
  routing · draft status · what never gets saved here · numbering · the repo rules
  check. These hold in every folder; if a folder's rules seem to conflict with them,
  these win — say so.

**MyRepo's sections.** Text between `<!-- myrepo:begin … -->` and
`<!-- myrepo:end … -->` is rewritten by MyRepo whenever the owner changes a setting.
Never write inside those markers; anything specific to the owner or a folder goes
outside them.

---

## The ownership rule

> **A folder owns what dies with it.**

- **Endeavors** — time-boxed campaigns (a job application, a project, a deployment).
  When they end, everything inside archives cleanly.
- **Entities** — permanent things reusable across endeavors (people, research
  topics, preferences, reusable documents). They never die; endeavors *reference*
  them via `subject:` tags — they never own them.

**Test question for anything new:** *will this matter in five years after its
context is gone?* Research for one project → inside that project. A durable skill
the project taught → promoted to a research/topic area before archiving. A contact
→ starts as a note inside the endeavor; promoted to a people area when the
relationship outlives the context. Fuzzy cases resolve by promotion, not perfect
classification.

## How to answer — three habits

1. **Say what kind of statement you're making.** "Your repo says…" (cite the
   path), "this source says…" (cite it), or "my interpretation…" — never present
   your own reasoning as fact. Saved, your interpretation is `context_type:
   analysis`, never a reference.
2. **When the owner doubts an answer ("are you sure?"), check before changing
   it** — against the repo and the sources. Wrong → say so and propose a
   `correction` record (it replaces the old statement). Right → keep the answer
   and show the evidence. Never switch sides just to agree.
3. **What the owner brings may be newer than you know.** Pasted articles, links
   and notes — especially on fast-moving subjects — are the source. Don't fill
   gaps from memory, say when something can't be verified, and date every
   observation (when it happened, and when it was added).

---

## The three questions

Every **knowledge record** answers three questions from its front-matter alone:

| # | Question | Fields |
|---|---|---|
| 1 | What is it about? | `subject:` (ID from `902_REFERENCES/ID_REGISTRY.md`) or `subject_text:` |
| 2 | What kind of statement is it? | `context_type:` — its category in the log |
| 3 | How much should it be trusted? | `status` + `confidence` + `raised_by` + `reviewed_by` |

**No front-matter, no save.** If a record can't answer the three questions yet, it is
saved with `subject_text:` filled in and no `context_type`, and logged as unsorted
(`920_UNSORTED`). Nothing is dropped.

Spec: `902_REFERENCES/CONTEXT_ITEM_SPEC.md`.

### Do not conflate the axes

- `context_type:` is the **function of the statement** — `dispute · correction ·
  analysis · known_issue · methodology · definition · evidence · decision · outcome ·
  assumption · preference`.
- `record_form:` is the **container** — `conversation | artifact | source_document
  | note`. It never determines meaning or routing. A conversation *contains*
  decisions; each extracted statement becomes its own record linked by
  `source_refs:`.
- `confidence:` — `confirmed | derived | working | hypothesis | unknown` only.
  `blocked`/`retired` are lifecycle → `status:`; `management_input` → `source_type:`.
- `scope:` on preferences — `global | artifact_type | area | project`.
- `sensitivity:` — `normal | private | restricted`. **This repo may be public, and
  every connected tool can read it** — flag `private`/`restricted` content *before*
  saving it, and treat `restricted` as "does not belong here."

<!-- myrepo:begin routing -->
### Routing (where a saved file goes, and its log)

**A saved file lives in the content folder it’s about** — the folder the owner picked,
or a content folder inside it — as `YYYY-MM-DD_TITLE.md`, where the owner sees it.
**Never save the owner’s content inside `910_RECORDS/`** — that is the back end, like
`AGENTS.md` and `README.md`.

**The catalog — three levels, written only by the repo’s catalog job.** After every push
`scripts/build_catalog.py` rebuilds them from the files themselves. **Never edit them** — just
save the file with its header (including `id:`); its row appears on its own.

1. `901_READ_FIRST/04_CATALOG.md` — one line per area: what it holds, how many saved files, by
   category and type, and where its full list is. **Start here to find anything.**
2. `<area>/910_RECORDS/CATALOG.csv` — every saved file in that area.
3. `<folder>/910_RECORDS/INDEX.csv` — every saved file in that folder.

Levels 2 and 3 are CSV — back-end data for agents and tools, one row per saved file
(people browse the folders, not these lists):

```csv
id,date,title,description,kind,category,type,file
20261005-SYS-ANA-7K2Q,2026-10-05,System design,How the parts fit together,analysis,924_MODELS,Systems,20_PROJECT/2026-10-05_SYSTEM-DESIGN.md
20261002-PEO-GEN-3MXA,2026-10-02,Jane Doe,Who she is and why she matters,,,People,30_TEAM/31_PEOPLE/jane-doe/PROFILE.md
```

Every saved file gets **one row**:

- **ID** — `YYYYMMDD-TTT-KKK-XXXX`: the date, its type and kind as three letters, four random
  characters. Put it in the header as `id:` the first time the file is saved and **never change
  it** — not when the file is renamed, moved or re-classified. Link to files by ID; the catalog
  says where each one is now. Read the current kind and type from the log, never from the ID.
  A file that already has an `id:` (older ones like `COG-002`) keeps it.
  Type codes: PEO People · GRO Groups · PER Periods · WOR Works · PLA Places · CON Concepts ·
  PRA Practices · SYS Systems · PAT Patterns · RES Resources · SOU Sources · EVI Evidence ·
  INT Interviews · DAT Data · EXP Experiments · RSL Results · OPT Options · PLN Plans ·
  WST Workstreams · TIM Timeline · RSP Responsibilities · DEP Dependencies · SCH Schedule ·
  RSR Research · DES Design · BLD Build · LAU Launch · REV Review · PRO Processes ·
  CHK Checklists · RUN Runs · MEA Measures · INC Incidents · IMP Improvements · GEN none.
  Kind codes: ANA analysis · ASM assumption · DEC decision · DEF definition · DIS dispute ·
  EVI evidence · KNI known_issue · MET methodology · OUT outcome · COR correction ·
  PRE preference · UNS not sorted yet. Any other type or kind: its first three letters.
- **Description** — what it is about, from the header’s `subject_text:`.
- **Kind** and its **one category** — a single 9-number. Pages that aren’t statements (a
  profile, a concept page) have no category.
- **Type** — what it is about, from the list of types (header `type:`, or the type its folder
  holds). The type lets an agent find every person or every source across the repo, whatever
  the owner named the folders.

The category comes from the header’s `context_type`:

| context_type | Category in the log |
|---|---|
| `decision`, `outcome` | `926_DECISIONS` |
| `assumption`, `known_issue` | `922_QUESTIONS` |
| `methodology`, `definition`, `evidence` | `923_REFERENCES` |
| `dispute`, `correction` | the file goes in the area’s `910_RECORDS/915_PUSH_BACK/` (cross-area → `915_PUSH_BACK/`) |
| `analysis` | `924_MODELS` |
| `preference` | the file goes in `902_REFERENCES/preferences/` (global/artifact_type) or the area (area/project scope) |
| not sure yet (no `context_type`) | `920_UNSORTED` |

The header is the truth; the log follows it. A push that saves the owner’s content inside
`910_RECORDS/` fails the repo rules check. `evidence` needs `source_refs:`; without a source it is an `assumption`.
The kinds are set in MyRepo (repo ⚙ → Classifications). Older repos may still have files
inside `01_RECORDS/00_INBOX/` … `06_DECISIONS/`: leave them, and save anything new in the folder.

`record_form` never routes: a raw conversation is saved and logged like anything else;
artifacts-in-progress live in `work/`.
<!-- myrepo:end routing -->

## Status and promotion

- **Agents write `status: draft` and `reviewed_by: none`. Never `canonical`.**
- Promotion is a human act: the owner sets `status: canonical` + `reviewed_by:`.
- **Merge ≠ promotion.** Git history tells what changed; the status field tells
  how much authority the content has. Drafts legitimately live on `main`.
- Anything with `status: superseded` (or in an `Archive/` or `99_ARCHIVE/` folder) is
  superseded — never cite it. Anything logged as unsorted (`920_UNSORTED`) is unreviewed —
  never cite it.
- **Superseding a saved file:** set `status: superseded`, move it into an `Archive/`
  folder inside its folder, and update its line in the log and the catalog.

<!-- myrepo:begin settings -->
## Your settings

Set in MyRepo (repo ⚙ → Rules, Organizing, Privacy) and stored in
`902_REFERENCES/REPO_SETTINGS.json`. Where this file says otherwise, these win.

**How AI tools work here**

- Ask where before saving anything the owner didn’t place — suggest 1–3 places, best guess first, each with its reason.
- Show the plan — every file with its full path — and write only after a yes.
- Every folder, number or layout you propose comes with one line of why and the alternative you considered.
- Everything an agent saves is `status: draft`; only the owner promotes it.
- When the owner doubts an answer ("are you sure?"), check before changing it — never switch sides just to agree.

**Organizing**

- Top-level folders start with an unused number — numbers only sort, they mean nothing, and never start with 9 (9 = back end; §Numbers).
- A new top-level folder needs the owner’s yes.
- Suggest grouping when 3 or more sibling folders share a theme.

**Never save here** — every connected tool can read this repo

- Passwords, API keys and other secrets
- Personal medical records — diagnoses, test results, treatment
- Financial account details
<!-- myrepo:end settings -->

## Saving — proposals, not auto-writes

- Any expression of "this should persist" — in any words — is a save event.
- **Ask where, then confirm.** When the owner asks to save and didn't say where,
  ask before writing: suggest 1–3 places from `901_READ_FIRST/02_AREA_MAP.md` (best
  guess first, with the reason) — the owner may not remember the folders. Then
  show the plan (every file, full path, and whether it updates or supersedes an
  existing record) and write only after a yes. Unsure where → ask; never default
  to the inbox unless the owner says to park it.
- **Mandatory proposals** (agent proposes what, where, and whether it supersedes an
  existing record; writes after approval): a durable decision, a disagreement or
  correction, a preference — even when the owner didn't ask to save.
- **Close-out:** at the end of a substantive conversation, propose what deserves
  filing. Nothing is written without a yes.
- **Correction loop:** durable style/format push-back ("that's cliché," "not my
  format") must also propose an update to `902_REFERENCES/preferences/` with the
  right `scope:`. Project-specific corrections stay in that area's records —
  they are not global preferences.

## Tools that cannot write files

If you cannot write to the repo (claude.ai, Gemini, ChatGPT without a repo task),
end the save by emitting a `SAVE` block — nothing omitted:

```
SAVE
path: <AREA>/<SUBJECT>/YYYY-MM-DD_TOPIC.md
---
<complete file: full front-matter (starting with id: YYYYMMDD-TTT-KKK-XXXX) + body>
```

The human or a file-capable agent performs the write. The logs and catalog update on
their own after the push — never write them. A disagreement left only in
a chat window is a silent drop — which this repository exists to prevent.

## Numbers — yours, and the back end's

There are two kinds of number, and they never mix.

- **Your numbers** put your folders in order, like a library shelf. Main areas take
  decades (`10_`, `20_`, `30_` …); something related takes a number inside its decade
  (`30_SPORTS` → `33_SOCCER`), and finer still adds a digit (`335_MENS_SOCCER`).
  Folders sort digit by digit, whatever their names say: `30_` → `33_` → `335_` → `34_`.
  A number places a folder on the shelf; what the folder is comes from its name and the
  Area Map. **Each added digit is a sub-category of the number before it**, at any
  depth: the area `30_SPORTS` holds `31_` … `39_` (`33_SOCCER`); inside `33_` come `331_` …
  `339_` (`335_MENS_SOCCER`); inside `335_` come `3351_` …. Never restart at `10_` or
  `20_` inside a folder — those are top-level numbers. Each of these folders has its own
  `AGENTS.md`, `README.md` and log. A sub-folder may also have no number. Folders for a kind of thing
  inside a topic are numbered the same way (`531_PEOPLE/`, `533_CONCEPTS/` inside
  `53_ARCHITECTURE/`); older repos may still have `10_PEOPLE/` or `15_CONCEPTS/` there —
  rename them only when the owner asks. **Your numbers never start with 9.**
- **Nine slots per level — plan ahead.** Each level holds `1` … `9`. When a subject
  clearly will have many sub-categories, give it room: a higher level (its own decade
  at the top, `70_`), or two neighbouring numbers (`41_` and `42_`). Suggest it to the
  owner before the slots run out; when a level fills, group its folders one level down.
- **The back end always starts with 9**, and each 9-number means one thing in every
  repo and every folder — so any AI tool, with no other context, knows where to look:

| Name | What it is | Where |
|---|---|---|
| `901_READ_FIRST/` | orientation, the Area Map, and `04_CATALOG.md` — every saved file | repo |
| `902_REFERENCES/` | rules machinery: record spec, push-back protocol, settings, prompts | repo |
| `910_RECORDS/` | the folder's log: `INDEX.csv` — every saved file, its category, where it is | every folder |
| `911_GOALS/` | goals, inside `910_RECORDS/` | every folder |
| `915_PUSH_BACK/` | disputes and corrections — in `910_RECORDS/`, or at the top for cross-area | folder · repo |
| `920_UNSORTED` · `922_QUESTIONS` · `923_REFERENCES` · `924_MODELS` · `926_DECISIONS` | categories in a log (labels in `INDEX.csv`, not folders) | — |
| `990_TRACKING/` | the AI's working lists — the queue, research and decisions needed | every folder |

The catch-all for unsorted captures is yours: `89_OTHER/`. **Never renumber** — it
breaks every link. Older repos used `01_RECORDS/`, `90_TRACKING/`, `01_READ_FIRST/`,
`02_REFERENCES/` and `99_OTHER/` for the same things.

## Structure rules

- Top-level areas start with one of your numbers (§Numbers) — unused by another
  top-level folder, never starting with 9. **Never renumber.** How to pick one:
  §Creating a top-level area.
- A sub-area is any unnumbered folder with its own `AGENTS.md` — same shape
  recursively. **Every folder for the owner's content gets its own** `AGENTS.md`
  + `README.md` in the same operation (§Every folder gets AGENTS.md + README.md). Never create a folder just by
  saving a file into it. Promoting a sub-area to top level is a move, not a redesign.
- `910_RECORDS/` is the **back end**, like `AGENTS.md` and `README.md`: the folder's log
  (`INDEX.csv` — every saved file, its category and where it is), its goals
  (`911_GOALS/`) and push-back (`915_PUSH_BACK/`). **The owner's content never goes in
  it** (§Routing). Older files already in `00_INBOX/` … `06_DECISIONS/` stay where they
  are; log them and save anything new in the folder.
- Filenames for dated records: `YYYY-MM-DD_TOPIC.md`.
- Cross-references use full paths from the repository root.
- **Never invent a registry ID** — use `subject_text:` and let a human mint the ID.
- `work/` is unvalidated space — drafts and artifacts-in-progress. Quote it only
  when asked, and label it.

## Every folder gets AGENTS.md + README.md

**Every folder that holds the owner's content — at any depth — is created together
with its own `AGENTS.md` and `README.md`, in the same change.** That includes:

- areas and sub-areas, and every folder inside them — the parts a folder is split
  into (for example `Location/`, `Things_To_Do/`, `Costs/`, `Design_Ideas/`), and the
  folders inside those;
- folders named for a type (`People/`, `Sources/`, or older ones like `30_SOURCES/`) and a
  person's folder.

`AGENTS.md` says what belongs in the folder and which rules apply (root and parent
`AGENTS.md`); `README.md` tells people what the folder is for and what's in it. This
is how every folder is found and navigated — **never decide that a folder can do
without them.** A folder still appears only when it has real content; never create
empty ones. Read the root and parent instructions first, and use
`902_REFERENCES/AREA_TEMPLATE/README.md` for an area or sub-area.

**A saved note is a file, never a folder.** When the owner asks to save a note, an
idea, a snippet or something they learned, write one `.md` file named for its subject
(for example `semiconductors-electrical-and-quantum-states.md`) in the folder it belongs
to, with its header (`topics:` lists what it's about). **`AGENTS.md` and `README.md`
are instructions and a folder description — never put the owner's notes or saved
content in them**, and never create a folder just to hold one note. A folder for one
item (a person, a work) only when it needs several files, and those files are named
for what they hold (`PROFILE.md`, `WORKS.md`). Notes saved as files show up on the
MyRepo website under their folder and open in the preview pane; text inside
`README.md` or `AGENTS.md` does not.

**Back end — never the owner's content, and no pair of their own:** `910_RECORDS/` (the
log, goals and push-back), `990_TRACKING/` (the queue and progress lists — notes for
agents on what's been looked at, what's next and what's kept) and `work/` follow their
folder's `AGENTS.md`; the repo's own machinery (`901_READ_FIRST/`, `902_REFERENCES/`,
`scripts/`) is described in this file. On the website the back end sits behind the cog.
In a folder named for a type the pair is notes for agents too — what the owner likes and
leaves out, where the conversation is heading.

Every saved file answers the three questions in its header, lives in the folder it's
about, and gets a line in its folder's log and the repo's catalog (§Routing).

Before completing a save, check each new folder has both files. An existing folder
missing them: add the pair the next time you work there, as part of the plan you show.

## Creating a top-level area

Do this only when nothing existing fits — most new topics are sub-areas
(unnumbered folders inside an area). If unsure which, ask the owner.

1. **Pick a number.** Any unused number works; choose one that sorts next to
   the area it's most related to. Folders sort like library call numbers — a
   longer number that starts with a shorter one sits right after it:
   `60_` → `620_` → `622_` → `63_`. So a new area close to `60_HEALTH` can be
   `620_` (or `622_` to go finer); something that belongs before everything
   else can be `062_` or `0622_`. Unrelated: take the next free decade. Never a number
   that starts with 9 — that's the back end. Don't infer
   meaning from a number — read the folder name and the Area Map.
2. **Propose it with a reason, and wait for a yes.** Give the full folder name
   (e.g. `620_DESIGN/`), why it is top level rather than inside the closest
   existing area (usually: it is used differently — practiced or built with,
   not only studied), why that number (which area it sorts next to), and the
   alternative you considered.
3. **In the same commit:** the folder's `AGENTS.md` + `README.md`
   (`902_REFERENCES/AREA_TEMPLATE/`), a row in `901_READ_FIRST/02_AREA_MAP.md`,
   its ID prefix in `902_REFERENCES/ID_REGISTRY.md`, and the folder in the area
   list of `902_REFERENCES/prompts/CHAT_CONTEXT.md`.

Finding things relies on the Area Map and indexes, never on what a number
"should" mean. `scripts/check_new_folder_guidance.py` fails a push that adds a
top-level area without a number, with a number already in use, or with one that
starts with 9.

<!-- myrepo:begin queue -->
## The queue

By default every folder, whatever its topic type, works things through in three steps — **explore →
investigate → confirm** — so the owner can look at something without committing to it, AI
never offers the same thing twice, and what matters is kept. One list per step, in the
folder's `990_TRACKING/` (each made on first use). `990_TRACKING/` is **back end**, like `910_RECORDS/` —
lists for agents (what was looked at, what’s next, what’s kept); the owner’s content never goes there.

| Step | File | What goes in it |
|---|---|---|
| Explore | `990_TRACKING/TO_EXPLORE.md` | worth a look, not committed yet — why it’s queued, how it connects, the question to investigate, where to start |
| Investigate | `990_TRACKING/STUDIED.md` | looked into — one line each, with what came of it, so it isn’t suggested again unless asked |
| Confirm | `990_TRACKING/FAVORITES.md` | confirmed — keep it for later |

- **"What's next?"** — offer the top of `TO_EXPLORE.md` (or ask which folder, if unclear).
- **Before suggesting anything**, check all three lists: never re-offer what is already
  studied or kept unless the owner asks.
- **Move items along as the owner says** — looked at it → `STUDIED.md` with what came of it;
  "keep this" → `FAVORITES.md`; "not interested" → `STUDIED.md` with that note.
- **New things worth a look** go to `TO_EXPLORE.md` (why, how it connects, the question,
  where to start) — never straight into the folder's pages.
- **These sit with the folder's progress lists** (Track progress, in its topic type's
  settings) — a folder that turns progress tracking off keeps no queue.
- **A folder may use its own stages instead** — when its `AGENTS.md` (§This folder's
  purpose) defines them, follow those there, kept in its `990_TRACKING/` the same way.
- **The owner’s view is in the folder itself.** `990_TRACKING/` is your working list. What the owner
  reads is a page in the folder, in plain words — `OVERVIEW.md`: where things stand, what
  they like and don’t, what’s still to explore, what’s been looked into and what came of it.
  As it grows, split it into pages by category (one per kind of thing being considered).
  Whenever the lists change in a way the owner would care about, update that page in the
  same change. (`README.md` is orientation and sits behind the cog on the website — not this.)

Set in MyRepo (repo ⚙ → Topic types; a folder's ⚙ → Topic type).
<!-- myrepo:end queue -->

<!-- myrepo:begin kinds-of-work -->
## Kinds of work

A folder holds one kind of work. **Study** works as §Working in a topic says. The others
draw from the same list of types (`902_REFERENCES/AREA_TEMPLATE/README.md` §Types); each
kind suggests a starting set:

| Kind | For | Close it when | Suggested types |
|---|---|---|---|
| Study | building understanding over time | when you no longer want to keep it up | People · Groups · Periods · Works · Places · Concepts · Practices · Systems · Patterns · Resources |
| Research | answering a particular question | the answer is useful enough for its purpose, or what remains uncertain is clearly stated | Sources · Evidence · Data · Experiments |
| Idea | developing a thought before you know the question or goal | you choose a direction, set it aside, or turn it into other work | Concepts · Resources · Options |
| Decide | choosing between possible actions | a choice is made, deferred, or rejected with a reason | Sources · Evidence · Options |
| Plan | finding a workable path to something you want | the path is clear enough to start (it becomes an Initiative, keeping PLAN.md), or the plan is dropped | Sources · Evidence · Data · Options |
| Initiative | making a change or achieving an outcome | the outcome is achieved, abandoned, or handed into recurring work | Results · Options · Plans · Workstreams |
| Operation | keeping recurring work running | the recurring work is retired or replaced | Processes · Checklists · Runs · Measures · Improvements |

- **Which kind a folder is** — its `AGENTS.md` says so. If it doesn’t, ask before creating
  folders in it.
- **A folder’s own settings win** — if its `AGENTS.md` lists “This folder’s own settings”
  (set in that folder’s ⚙), follow those in that folder, Study included; anything it doesn’t
  list comes from this file.
- **Types are labels, not folder names.** A type (People, Sources, Options, Timeline …) says
  what kind of thing a folder holds. The owner names the folders the way they want to find
  things (`Location/`, `Venues/`, `Buildings/`), numbered from their parent’s number (`31_` … `39_` inside
  `30_`, `331_` inside `33_`) or not at all; each
  folder’s `AGENTS.md` says which types it holds (“Holds: places, options”). Suggest names;
  never create a folder just because a type is on the list. A folder may be named after a
  type (`People/`) when that is how the owner wants it. Suggestions, not limits.
- **No empty folders** — a folder appears with its first page, together with its own
  `AGENTS.md` + `README.md`. Turning a type off never deletes or moves anything already there.
- **Responsibilities** record only what someone has agreed to — a suggested owner is not one.
- **When a folder closes** (each kind says when, below), move what lasts up to the folder it
  served; the finished folder keeps its history.

**Research folders**

- When it isn’t clear, ask: “What are you looking for so far, and what would finding it help you do?”
- Every Research folder keeps: `QUESTION.md` (the question you’re actually trying to answer, what it’s for, and when you’ll know enough); `FINDINGS.md` (each finding, how sure we are, and its sources).
- How I research — work this way: I may start with an approximate description, examples, or something that caught my attention. Help me locate the question I’m actually trying to answer. Begin broad enough to map the territory, then follow the strongest leads into specifics. Show me diagrams or maps when they make the relationships easier to see. Keep sources, findings, assumptions and disagreements distinct. Help me recognize when I know enough to use the answer, and what remains uncertain.
- Close it when the answer is useful enough for its purpose, or what remains uncertain is clearly stated.
- Progress, kept apart from the work in `990_TRACKING/`: `LEADS_TO_FOLLOW.md` · `SOURCES_TO_EXAMINE.md` · `FINDINGS_TO_CHECK.md` · `ANSWERED.md`.

**Idea folders**

- When it isn’t clear, ask: “What’s the thought, and what could it become?”
- Every Idea folder keeps: `IDEA.md` (the idea in your own words, and how it has changed).
- How I develop an idea — work this way: I may start with a hunch, an image or half a sentence. Help me say it in my own words, then show me what it could become — possibilities, tensions, objections. Keep my idea apart from what you add. Don’t turn it into a plan before I’m ready; when a direction appears, help me decide whether to research it, decide on it or start it.
- Close it when you choose a direction, set it aside, or turn it into other work.
- Progress, kept apart from the work in `990_TRACKING/`: `POSSIBILITIES.md` · `OBJECTIONS.md` · `QUESTIONS_THAT_WOULD_SHARPEN_IT.md`.

**Decide folders**

- When it isn’t clear, ask: “What are you choosing between, and by when?”
- Every Decide folder keeps: `DECISION.md` (the choice, the options, what matters most, who decides — and the decision, why, what it gives up and what would make you revisit it).
- How I make a decision — work this way: I usually start with the choice in front of me and a gut feeling. Help me lay out the options and what matters most, find what I don’t know yet, and hear the views that differ from mine. Keep what’s been proposed apart from what’s been decided. When I choose, record the reason, what I’m giving up, and what would make me revisit it.
- Close it when a choice is made, deferred, or rejected with a reason.
- Progress, kept apart from the work in `990_TRACKING/`: `OPTIONS_TO_COMPARE.md` · `QUESTIONS_TO_ANSWER_FIRST.md` · `DECIDED.md`.

**Plan folders**

- When it isn’t clear, ask: “What are you planning toward — even if it’s still fuzzy?”
- Every Plan folder keeps: `PLAN.md` (where you’re heading, what’s known, assumed and still open, the options, what’s chosen, and the path — order, timing, costs — with what would make you revisit it).
- How I plan — work this way: I may start with a fuzzy picture or with much already settled. See how far along it is and start there; don’t walk me through steps in order. Build the picture with me instead of asking for everything up front. Keep what’s known, assumed and decided apart. Ask the question that most changes the path next, and leave open what wouldn’t change it yet. Say when something needs research or a decision. When numbers depend on each other, like costs, keep them in a table I can check.
- Close it when the path is clear enough to start (it becomes an Initiative, keeping PLAN.md), or the plan is dropped.
- Progress, kept apart from the work in `990_TRACKING/`: `RESEARCH_NEEDED.md` · `DECISIONS_NEEDED.md` · `REVISIT_TRIGGERS.md`.
- A plan moves through framing, modelling, exploring, resolving, sequencing and adapting —
  ways of thinking, not steps. Never make the owner go through them in order; work on the
  open question that most affects the path.
- Use the repo’s confidence words for what’s assumed (hypothesis → working → confirmed). A
  choice is a decision record, and a decision can rest on assumptions that are still open.
- `PLAN.md` is a living picture, not a form: fill only the parts that are known so far.
- When the plan has calculations (costs, budgets, counts, dates that depend on each other), keep
  the numbers as CSV in the folder that holds Data (named by the owner, e.g. `Costs/`), with a
  short page saying how they relate. `PLAN.md` says what
  they mean and where they came from. No calculations, no table.
- Research and decisions stay as records here unless they grow into work of their own; then
  they become a folder inside this one.
- When it becomes an Initiative, `PLAN.md` stays as it was — it’s how the work started.

**Initiative folders**

- When it isn’t clear, ask: “What are you trying to change or make happen, even if the outcome is still taking shape?”
- Every Initiative folder keeps: `OVERVIEW.md` (what you’re trying to change, why, what’s in and out, and how you’ll know it’s done); `DECISIONS.md` (what was chosen, who chose, why, and what would change it).
- How I move an initiative forward — work this way: I may start with a problem, a possibility, a request, or an outcome I want. Help me understand what is happening and who it affects. Bring in other perspectives where they matter, develop possible approaches, and help me choose what to try. Keep ideas and proposals separate from decisions. Record who actually accepted a commitment, what we did, what happened, and what still needs attention. Start wherever the work really is; I may need to revisit an earlier choice.
- Close it when the outcome is achieved, abandoned, or handed into recurring work.
- Progress, kept apart from the work in `990_TRACKING/`: `QUESTIONS_TO_RESOLVE.md` · `DECISIONS_NEEDED.md` · `NEXT_UP.md` · `OUTCOMES.md`.

**Operation folders**

- When it isn’t clear, ask: “What happens repeatedly, and what should a good run look like?”
- Every Operation folder keeps: `PROCESS.md` (what normally happens, who handles each part, and what a good run looks like); `MEASURES.md` (what is watched, and what counts as normal).
- How I run an operation — work this way: Help me describe what normally happens, who handles each part, and what a good result looks like. As it repeats, focus on meaningful exceptions and patterns rather than writing up every ordinary run. When we consider changing the process, show the reason, the alternatives, who decides, and how we will tell whether the change helped. Keep the current process aligned with decisions that were actually made.
- Close it when the recurring work is retired or replaced.
- Progress, kept apart from the work in `990_TRACKING/`: `EXCEPTIONS_TO_REVIEW.md` · `IMPROVEMENTS_TO_TRY.md` · `CHANGES_DECIDED.md`.

Set in MyRepo (repo ⚙ → Topic types).
<!-- myrepo:end kinds-of-work -->

<!-- myrepo:begin working -->
## Working in a topic

Every topic works the same way, so the owner can ask the same things anywhere.

**Open a topic** — read, in order: its `AGENTS.md` (what it is for and which kinds it
holds), `STUDY_GUIDE.md` if it has one, `LEARNING_PATH.md`, `HISTORY.md`, then `990_TRACKING/`.

**How the owner learns** — teach this way in every topic:

> Through conversation. You teach; I call out what resonates and we follow that thread; along the way you name the few things worth remembering, and they stick. When we stop, save it: update the pages it touched (what resonated, what to remember), add any idea of mine as a concept, and add a learning-path entry if the inquiry changed direction.

- Teach in conversation, one thread at a time; follow what the owner calls out rather than a script.
- When something resonates, say so back in a line and keep going down that thread.
- At natural points, name 1–3 things to remember — short and memorable. They become the page’s *What to remember* and memory hook.
- When the conversation stops, offer **“save this”** (below) as a plan.

**Four layers — keep them apart:**

| Layer | The question it answers | Home |
|---|---|---|
| Knowledge | What have we actually learned about this person or thing? | the folders holding People, Groups, Periods … |
| Synthesis | What ideas has the owner developed from studying these things? | the folder holding Concepts — marked as the owner’s |
| Learning path | How did one question or discovery lead to the next? | `LEARNING_PATH.md` |
| Future inquiry | What does the owner want to investigate, and why? | `990_TRACKING/TO_EXPLORE.md` |

**Where something goes — the lifecycle:**

| What happened | Where it goes |
|---|---|
| Mentioned in passing (a building, a book, an example) | inside the existing page it belongs to — e.g. a person’s `WORKS.md` |
| Interesting, not yet studied | a row in `990_TRACKING/TO_EXPLORE.md` — no page |
| The conversation or research produced substantive knowledge worth retrieving on its own | its page, in the folder that holds its type (a person: `first-last/` in the folder holding People), and its row moves to `STUDIED.md` |
| A cross-cutting insight emerged | the folder holding Concepts — with its origin marked |
| The inquiry changed direction | a short entry in `LEARNING_PATH.md` |
| A repeatable way of studying the subject developed | `STUDY_GUIDE.md` (any topic may have one) |
| The owner explicitly loves it | `990_TRACKING/FAVORITES.md` |

**A file existing means something.** A page exists only when there is substantive
knowledge in it — never a placeholder, a stub or a “not written yet”. Agents must be
able to trust that every page is real knowledge without opening it.

**The folders are the owner’s.** Name them the way the owner wants to find things
(`People/`, `Buildings/`, `Timeline/` …), with the owner’s numbers or none — never create one
just because a type is on the list. The types below are labels from the one list in
`902_REFERENCES/REPO_SETTINGS.json`: each folder’s `AGENTS.md` says which it holds, a topic
holds only the types it uses, and a folder appears with its first page, together with its
own `AGENTS.md` + `README.md` (a person’s folder too):

| Type | Holds | One item is |
|---|---|---|
| People | a folder per person — PROFILE.md (who they are, their story, why they matter here) and WORKS.md | a folder `first-last/` with `PROFILE.md` + `WORKS.md` |
| Groups | schools, movements, organizations, lineages | a page `short-name.md` |
| Periods | eras and events worth studying on their own | a page `short-name.md` |
| Works | buildings, books, artworks — studied as objects in themselves | a page `short-name.md` |
| Places | real locations | a page `short-name.md` |
| Concepts | ideas, principles and terms | a page `short-name.md` |
| Practices | techniques, methods, exercises — things you do (with a level when there is an order) | a page `short-name.md` |
| Systems | products, tools and implementations (technology topics) | a page `short-name.md` |
| Patterns | reusable designs (technology topics) | a page `short-name.md` |
| Resources | what you learn from — books, papers, courses, videos — each with its link and what it contributes | a page `short-name.md` |
| `990_TRACKING/` (back end) | the owner’s progress — `TO_EXPLORE.md` · `STUDIED.md` · `READING_QUEUE.md` · `FAVORITES.md` | a row per item |

Pages never say whether the owner studied them — progress lives only in
`990_TRACKING/`. Link with relative links (`../People/frei-otto/PROFILE.md`) so pages open on GitHub and in MyRepo.

**When the owner says…**

- **“What’s next?”** — the first row of `990_TRACKING/TO_EXPLORE.md`; in a topic with a
  `STUDY_GUIDE.md`, follow its order. Teach from the row’s question and starting point.
- **“Tell me more about X”** — read X’s page if it has one (or its row), then go further.
  When the conversation produces substantive knowledge, offer to save it — as a plan.
- **“Add X”** — if it’s only worth exploring, add a row to `TO_EXPLORE.md`; if we’ve learned something
  substantive, create or update its page. Never invent facts.
- **“I studied X” / “done”** — turn its row into knowledge: write its page from what we learned,
  delete the row from `TO_EXPLORE.md` and add one to `STUDIED.md` with the date; `FAVORITES.md` only when the owner says so.
  Only the owner marks things studied — talking about something isn’t studying it.
- **“Another one we haven’t covered”** — anything not in `STUDIED.md`.
- **“Save this”** at the end of a study conversation — update the pages it touched (*What resonated*,
  *What to remember*), add any new concept, and add a `LEARNING_PATH.md` entry if the inquiry changed direction.

**The lists in `990_TRACKING/`:**

- `TO_EXPLORE.md` — a rich row, no page: `| # | Name | Kind | Why queued | Connection to the current inquiry | Question to investigate | Start with |`
- `STUDIED.md` — `| Date | [Name](link to its page) | Kind | favorite or not, and why — in the owner’s words |`
- `FAVORITES.md` — `| [Name](…) | Kind | why |` — only when the owner says so
- If an item already has a page, update it — never make a second one.

**Concepts — mark the origin.** Every concept page’s header has `origin: established`
(a recognized idea, e.g. form-finding — cite sources) or `origin: owner` (the owner’s own
synthesis, e.g. “systems that generate form vs systems that impose it” — say which
comparisons it came from, `context_type: analysis`). Never let the owner’s interpretation
read as an established fact.

**`LEARNING_PATH.md`** — deliberately sparse: no transcripts, no session logs. One entry
each time the inquiry changes direction:

```
## 2026-09 — Frei Otto → Louis Kahn
<two or three sentences: what shifted, and why>
Led to: <concepts, people or questions — linked>
```

**Writing** — every page is written the same way, in every topic:

- Plain language; short titles inside a topic ("People", not "People — Architecture").
- Facts carry their source (linked); anything unsourced is marked as interpretation.
- Only write what resonated or what the owner thinks when they said it.

**Page template** — every page starts with a record header (`CONTEXT_ITEM_SPEC.md`),
then: a one-line memory hook · what it is · the story or how it works · what the
sources say (linked) · how it connects (links to people, concepts, works) · what
resonated with the owner (only what they said) · questions left. A topic’s `AGENTS.md`
may set its own sections (architecture: §Adding an architect).
A person’s `WORKS.md` is a table: work · where / when · what to study — works mentioned in passing live here.
<!-- myrepo:end working -->

<!-- myrepo:begin proposing -->
## Proposing folders and topic layouts

- **Say why.** Every folder, number or layout you propose comes with one line
  of reasoning and the alternative you considered. If the owner doesn't know
  where something goes, recommend — and when the content later shows a
  pattern, say so and propose the better home.
- **Group before adding.** Before creating a folder, check whether the subject
  fits inside an existing one. When 3 or more sibling folders share a
  theme, propose grouping them: in a group folder, or in a new top-level area
  if they are used differently (§Creating a top-level area).
- **Explore, investigate, confirm — per item, not per topic.** How committed the owner
  is to something lives in the queue (§The queue), never as a label on the topic.
- **A new topic** picks its kinds from the one list (§Working in a topic) — propose
  which, with reasons, ask, and record the choice in the topic's `AGENTS.md`.
- **Folders of the owner's own.** When the owner asks for a folder the list doesn't
  have (in one topic only), make it — numbered after the standard ones (`20_`, `21_` …)
  — and note it in that topic's `AGENTS.md` §Layout so every tool finds it. Don't invent
  one unasked: suggest it, or suggest adding a kind to the list for every topic
  (MyRepo → repo ⚙ → Topic types) when it would fit topics generally. Details:
  `902_REFERENCES/AREA_TEMPLATE/README.md` §Topic layouts.
- **A way of working that repeats.** When the same purpose or stages show up in
  several folders' `AGENTS.md`, propose making it a topic type (MyRepo → repo ⚙ →
  Topic types) so any folder can pick it.
<!-- myrepo:end proposing -->

## Push-back is mandatory

If you disagree with anything in this repository — or a human tells you something
here is wrong — **write it down** (or emit a `SAVE` block). One area → its
`915_PUSH_BACK/`; cross-area or repo-level → `915_PUSH_BACK/`. Record rejected
push-back as carefully as accepted. Do not silently comply with something you
believe is wrong; do not silently override it either.

Protocol: `902_REFERENCES/PUSH_BACK_PROTOCOL.md`.

## Reviewer

**Context reviewer / owner:** _set during setup_ — the human who promotes drafts
to `canonical`.

## Deferred machinery

- `scripts/check_new_folder_guidance.py` runs on every push (GitHub Actions): a new
  area or sub-area without AGENTS.md + README.md, or a new record without a
  header, or a new top-level area without an unused number, fails the check.
- `03_REPORTS/` + index generator — add when cross-area search gets painful.
- `915_PUSH_BACK/` — create on first cross-area dispute.
- Sensitivity-gated areas (finance, health, admin) — not created by default;
  sensitive personal content does not enter this repo without an explicit owner
  decision.
