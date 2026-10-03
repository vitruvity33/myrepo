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
> `01_READ_FIRST/02_AREA_MAP.md`, and mint your ID prefixes in
> `02_REFERENCES/ID_REGISTRY.md` as areas are created.

---

## Read this before anything else

**Before working in an area or sub-area, read that area's `AGENTS.md`.**
Not every tool discovers nested instruction files — this rule makes them load-bearing.

Orientation: `01_READ_FIRST/01_START_HERE.md` → `01_READ_FIRST/02_AREA_MAP.md`.

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

## How to answer — two habits

1. **Say what kind of statement you're making.** "Your repo says…" (cite the
   path), "this source says…" (cite it), or "my interpretation…" — never present
   your own reasoning as fact. Saved, your interpretation is `context_type:
   analysis`, never a reference.
2. **When the owner doubts an answer ("are you sure?"), check before changing
   it** — against the repo and the sources. Wrong → say so and propose a
   `correction` record (it replaces the old statement). Right → keep the answer
   and show the evidence. Never switch sides just to agree.

---

## The three questions

Every **knowledge record** answers three questions from its front-matter alone:

| # | Question | Fields |
|---|---|---|
| 1 | What is it about? | `subject:` (ID from `02_REFERENCES/ID_REGISTRY.md`) or `subject_text:` |
| 2 | What kind of statement is it? | `context_type:` — routes it to a folder slot |
| 3 | How much should it be trusted? | `status` + `confidence` + `raised_by` + `reviewed_by` |

**No front-matter, no save.** If a record can't answer the three questions yet, it
goes to the nearest `00_INBOX/` with `subject_text:` filled in. Nothing is dropped.

Spec: `02_REFERENCES/CONTEXT_ITEM_SPEC.md`.

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
### Routing (context_type → slot)

| context_type | Files to |
|---|---|
| `decision`, `outcome` | `01_RECORDS/06_DECISIONS/` |
| `assumption`, `known_issue` | `01_RECORDS/02_QUESTIONS/` |
| `methodology`, `definition`, `evidence` | `01_RECORDS/03_REFERENCES/` |
| `dispute`, `correction` | area `05_PUSH_BACK/` (cross-area → `90_PUSH_BACK/`) |
| `analysis` | `01_RECORDS/04_MODELS/` |
| `preference` | `02_REFERENCES/preferences/` (global/artifact_type) or the area (area/project scope) |
| anything unsortable | `00_INBOX/` |

The header is the truth and the folder must agree — a push where they disagree
fails the repo rules check. `evidence` needs `source_refs:`; without a source it is an `assumption`.
The kinds are set in MyRepo (repo ⚙ → Classifications).

`record_form` never routes: raw conversations land in `00_INBOX/` or
`03_REFERENCES/`; artifacts-in-progress live in `work/`.
<!-- myrepo:end routing -->

## Status and promotion

- **Agents write `status: draft` and `reviewed_by: none`. Never `canonical`.**
- Promotion is a human act: the owner sets `status: canonical` + `reviewed_by:`.
- **Merge ≠ promotion.** Git history tells what changed; the status field tells
  how much authority the content has. Drafts legitimately live on `main`.
- Anything in `99_ARCHIVE/` is superseded — never cite it. Anything in
  `00_INBOX/` is unsorted and unreviewed — never cite it.

<!-- myrepo:begin settings -->
## Your settings

Set in MyRepo (repo ⚙ → Rules, Organizing, Privacy) and stored in
`02_REFERENCES/REPO_SETTINGS.json`. Where this file says otherwise, these win.

**How AI tools work here**

- Ask where before saving anything the owner didn’t place — suggest 1–3 places, best guess first, each with its reason.
- Show the plan — every file with its full path — and write only after a yes.
- Every folder, number or layout you propose comes with one line of why and the alternative you considered.
- Everything an agent saves is `status: draft`; only the owner promotes it.
- When the owner doubts an answer ("are you sure?"), check before changing it — never switch sides just to agree.

**Organizing**

- Top-level folders start with an unused number — numbers only sort, they mean nothing (§Creating a top-level area).
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
  ask before writing: suggest 1–3 places from `01_READ_FIRST/02_AREA_MAP.md` (best
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
  format") must also propose an update to `02_REFERENCES/preferences/` with the
  right `scope:`. Project-specific corrections stay in that area's records —
  they are not global preferences.

## Tools that cannot write files

If you cannot write to the repo (claude.ai, Gemini, ChatGPT without a repo task),
end the save by emitting a `SAVE` block — nothing omitted:

```
SAVE
path: <AREA>/<SUBJECT>/01_RECORDS/06_DECISIONS/YYYY-MM-DD_TOPIC.md
---
<complete file: full front-matter + body>
```

The human or a file-capable agent performs the write. A disagreement left only in
a chat window is a silent drop — which this repository exists to prevent.

## Structure rules

- Top-level areas start with a number and an underscore (`10_`, `620_`,
  `0622_`). The number only keeps areas in order — it **means nothing on its
  own**, can be any length, and must not already be used by another top-level
  folder. `01_` and `02_` belong to MyRepo's own folders. **Never renumber.**
  How to pick one: §Creating a top-level area.
- A sub-area is any unnumbered folder with its own `AGENTS.md` — same shape
  recursively. **Every folder that owns ongoing work is a governed area** — it gets
  `AGENTS.md` + `README.md` in the same operation. Promoting a sub-area to top
  level is a move, not a redesign.
- `01_RECORDS/` slots are a **menu, not a mandate** — each area's `AGENTS.md`
  declares which it uses; folders are created on first use. Every area has
  `00_INBOX`, `03_REFERENCES`, `99_ARCHIVE` available.
- Filenames for dated records: `YYYY-MM-DD_TOPIC.md`.
- Cross-references use full paths from the repository root.
- **Never invent a registry ID** — use `subject_text:` and let a human mint the ID.
- `work/` is unvalidated space — drafts and artifacts-in-progress. Quote it only
  when asked, and label it.

## Creating a top-level area

Do this only when nothing existing fits — most new topics are sub-areas
(unnumbered folders inside an area). If unsure which, ask the owner.

1. **Pick a number.** Any unused number works; choose one that sorts next to
   the area it's most related to. Folders sort like library call numbers — a
   longer number that starts with a shorter one sits right after it:
   `60_` → `620_` → `622_` → `63_`. So a new area close to `60_HEALTH` can be
   `620_` (or `622_` to go finer); something that belongs before everything
   else can be `062_` or `0622_`. Unrelated: take any free number. Don't infer
   meaning from a number — read the folder name and the Area Map.
2. **Propose it with a reason, and wait for a yes.** Give the full folder name
   (e.g. `620_DESIGN/`), why it is top level rather than inside the closest
   existing area (usually: it is used differently — practiced or built with,
   not only studied), why that number (which area it sorts next to), and the
   alternative you considered.
3. **In the same commit:** the folder's `AGENTS.md` + `README.md`
   (`02_REFERENCES/AREA_TEMPLATE/`), a row in `01_READ_FIRST/02_AREA_MAP.md`,
   its ID prefix in `02_REFERENCES/ID_REGISTRY.md`, and the folder in the area
   list of `02_REFERENCES/prompts/CHAT_CONTEXT.md`.

Finding things relies on the Area Map and indexes, never on what a number
"should" mean. `scripts/check_new_folder_guidance.py` fails a push that adds a
top-level area without a number or with a number already in use.

<!-- myrepo:begin queue -->
## The queue

Every folder, whatever its topic type, works things through in three steps — **explore →
investigate → confirm** — so the owner can look at something without committing to it, AI
never offers the same thing twice, and what matters is kept. One list per step, in the
folder's `90_TRACKING/` (each made on first use):

| Step | File | What goes in it |
|---|---|---|
| Explore | `90_TRACKING/TO_EXPLORE.md` | worth a look, not committed yet — why it’s queued, how it connects, the question to investigate, where to start |
| Investigate | `90_TRACKING/STUDIED.md` | looked into — one line each, with what came of it, so it isn’t suggested again unless asked |
| Confirm | `90_TRACKING/FAVORITES.md` | confirmed — keep it for later |

- **"What's next?"** — offer the top of `TO_EXPLORE.md` (or ask which folder, if unclear).
- **Before suggesting anything**, check all three lists: never re-offer what is already
  studied or kept unless the owner asks.
- **Move items along as the owner says** — looked at it → `STUDIED.md` with what came of it;
  "keep this" → `FAVORITES.md`; "not interested" → `STUDIED.md` with that note.
- **New things worth a look** go to `TO_EXPLORE.md` (why, how it connects, the question,
  where to start) — never straight into the folder's pages.
- **A folder's ⚙ can turn its queue off**; its `AGENTS.md` then says so.

Set in MyRepo (repo ⚙ → Topic types; a folder's ⚙ → Topic type).
<!-- myrepo:end queue -->

<!-- myrepo:begin kinds-of-work -->
## Kinds of work

A folder holds one kind of work. **Study** works as §Working in a topic says. The others
draw from the same menu of folder types (`02_REFERENCES/AREA_TEMPLATE/README.md` §Folder
types); each kind suggests a starting set:

| Kind | For | Close it when | Suggested folder types |
|---|---|---|---|
| Study | building understanding over time | when you no longer want to keep it up | `10_PEOPLE/` · `11_GROUPS/` · `12_PERIODS/` · `13_WORKS/` · `14_PLACES/` · `15_CONCEPTS/` · `16_PRACTICES/` · `17_SYSTEMS/` · `18_PATTERNS/` · `19_RESOURCES/` |
| Research | answering a particular question | the answer is useful enough for its purpose, or what remains uncertain is clearly stated | `30_SOURCES/` · `31_EVIDENCE/` · `33_DATA/` · `34_EXPERIMENTS/` |
| Idea | developing a thought before you know the question or goal | you choose a direction, set it aside, or turn it into other work | `15_CONCEPTS/` · `19_RESOURCES/` · `36_OPTIONS/` |
| Decide | choosing between possible actions | a choice is made, deferred, or rejected with a reason | `30_SOURCES/` · `31_EVIDENCE/` · `36_OPTIONS/` |
| Initiative | making a change or achieving an outcome | the outcome is achieved, abandoned, or handed into recurring work | `35_RESULTS/` · `36_OPTIONS/` · `37_PLANS/` · `38_WORKSTREAMS/` |
| Operation | keeping recurring work running | the recurring work is retired or replaced | `48_PROCESSES/` · `49_CHECKLISTS/` · `50_RUNS/` · `51_MEASURES/` · `53_IMPROVEMENTS/` |

- **Which kind a folder is** — its `AGENTS.md` says so. If it doesn’t, ask before creating
  folders in it.
- **A folder’s own settings win** — if its `AGENTS.md` lists “This folder’s own settings”
  (set in that folder’s ⚙), follow those in that folder, Study included; anything it doesn’t
  list comes from this file.
- **Suggestions, not limits** — a folder may use any type on the menu. Each type keeps one
  number everywhere, so a folder never gets renumbered.
- **No empty folders** — a type’s folder appears with its first page. Turning a type off never
  deletes or moves anything already there.
- **Responsibilities** record only what someone has agreed to — a suggested owner is not one.
- **When a folder closes** (each kind says when, below), move what lasts up to the folder it
  served; the finished folder keeps its history.

**Research folders**

- When it isn’t clear, ask: “What are you looking for so far, and what would finding it help you do?”
- Every Research folder keeps: `QUESTION.md` (the question you’re actually trying to answer, what it’s for, and when you’ll know enough); `FINDINGS.md` (each finding, how sure we are, and its sources).
- How I research — work this way: I may start with an approximate description, examples, or something that caught my attention. Help me locate the question I’m actually trying to answer. Begin broad enough to map the territory, then follow the strongest leads into specifics. Show me diagrams or maps when they make the relationships easier to see. Keep sources, findings, assumptions and disagreements distinct. Help me recognize when I know enough to use the answer, and what remains uncertain.
- Close it when the answer is useful enough for its purpose, or what remains uncertain is clearly stated.
- Progress, kept apart from the work in `90_TRACKING/`: `LEADS_TO_FOLLOW.md` · `SOURCES_TO_EXAMINE.md` · `FINDINGS_TO_CHECK.md` · `ANSWERED.md`.

**Idea folders**

- When it isn’t clear, ask: “What’s the thought, and what could it become?”
- Every Idea folder keeps: `IDEA.md` (the idea in your own words, and how it has changed).
- How I develop an idea — work this way: I may start with a hunch, an image or half a sentence. Help me say it in my own words, then show me what it could become — possibilities, tensions, objections. Keep my idea apart from what you add. Don’t turn it into a plan before I’m ready; when a direction appears, help me decide whether to research it, decide on it or start it.
- Close it when you choose a direction, set it aside, or turn it into other work.
- Progress, kept apart from the work in `90_TRACKING/`: `POSSIBILITIES.md` · `OBJECTIONS.md` · `QUESTIONS_THAT_WOULD_SHARPEN_IT.md`.

**Decide folders**

- When it isn’t clear, ask: “What are you choosing between, and by when?”
- Every Decide folder keeps: `DECISION.md` (the choice, the options, what matters most, who decides — and the decision, why, what it gives up and what would make you revisit it).
- How I make a decision — work this way: I usually start with the choice in front of me and a gut feeling. Help me lay out the options and what matters most, find what I don’t know yet, and hear the views that differ from mine. Keep what’s been proposed apart from what’s been decided. When I choose, record the reason, what I’m giving up, and what would make me revisit it.
- Close it when a choice is made, deferred, or rejected with a reason.
- Progress, kept apart from the work in `90_TRACKING/`: `OPTIONS_TO_COMPARE.md` · `QUESTIONS_TO_ANSWER_FIRST.md` · `DECIDED.md`.

**Initiative folders**

- When it isn’t clear, ask: “What are you trying to change or make happen, even if the outcome is still taking shape?”
- Every Initiative folder keeps: `OVERVIEW.md` (what you’re trying to change, why, what’s in and out, and how you’ll know it’s done); `DECISIONS.md` (what was chosen, who chose, why, and what would change it).
- How I move an initiative forward — work this way: I may start with a problem, a possibility, a request, or an outcome I want. Help me understand what is happening and who it affects. Bring in other perspectives where they matter, develop possible approaches, and help me choose what to try. Keep ideas and proposals separate from decisions. Record who actually accepted a commitment, what we did, what happened, and what still needs attention. Start wherever the work really is; I may need to revisit an earlier choice.
- Close it when the outcome is achieved, abandoned, or handed into recurring work.
- Progress, kept apart from the work in `90_TRACKING/`: `QUESTIONS_TO_RESOLVE.md` · `DECISIONS_NEEDED.md` · `NEXT_UP.md` · `OUTCOMES.md`.

**Operation folders**

- When it isn’t clear, ask: “What happens repeatedly, and what should a good run look like?”
- Every Operation folder keeps: `PROCESS.md` (what normally happens, who handles each part, and what a good run looks like); `MEASURES.md` (what is watched, and what counts as normal).
- How I run an operation — work this way: Help me describe what normally happens, who handles each part, and what a good result looks like. As it repeats, focus on meaningful exceptions and patterns rather than writing up every ordinary run. When we consider changing the process, show the reason, the alternatives, who decides, and how we will tell whether the change helped. Keep the current process aligned with decisions that were actually made.
- Close it when the recurring work is retired or replaced.
- Progress, kept apart from the work in `90_TRACKING/`: `EXCEPTIONS_TO_REVIEW.md` · `IMPROVEMENTS_TO_TRY.md` · `CHANGES_DECIDED.md`.

Set in MyRepo (repo ⚙ → Topic types).
<!-- myrepo:end kinds-of-work -->

<!-- myrepo:begin working -->
## Working in a topic

Every topic works the same way, so the owner can ask the same things anywhere.

**Open a topic** — read, in order: its `AGENTS.md` (what it is for and which kinds it
holds), `STUDY_GUIDE.md` if it has one, `LEARNING_PATH.md`, `HISTORY.md`, then `90_TRACKING/`.

**How the owner learns** — teach this way in every topic:

> Through conversation. You teach; I call out what resonates and we follow that thread; along the way you name the few things worth remembering, and they stick. When we stop, save it: update the pages it touched (what resonated, what to remember), add any idea of mine as a concept, and add a learning-path entry if the inquiry changed direction.

- Teach in conversation, one thread at a time; follow what the owner calls out rather than a script.
- When something resonates, say so back in a line and keep going down that thread.
- At natural points, name 1–3 things to remember — short and memorable. They become the page’s *What to remember* and memory hook.
- When the conversation stops, offer **“save this”** (below) as a plan.

**Four layers — keep them apart:**

| Layer | The question it answers | Home |
|---|---|---|
| Knowledge | What have we actually learned about this person or thing? | `10_PEOPLE/`, `11_GROUPS/`, `12_PERIODS/` … |
| Synthesis | What ideas has the owner developed from studying these things? | `15_CONCEPTS/` — marked as the owner’s |
| Learning path | How did one question or discovery lead to the next? | `LEARNING_PATH.md` |
| Future inquiry | What does the owner want to investigate, and why? | `90_TRACKING/TO_EXPLORE.md` |

**Where something goes — the lifecycle:**

| What happened | Where it goes |
|---|---|
| Mentioned in passing (a building, a book, an example) | inside the existing page it belongs to — e.g. a person’s `WORKS.md` |
| Interesting, not yet studied | a row in `90_TRACKING/TO_EXPLORE.md` — no page |
| The conversation or research produced substantive knowledge worth retrieving on its own | its page (a person: `10_PEOPLE/first-last/`), and its row moves to `STUDIED.md` |
| A cross-cutting insight emerged | `15_CONCEPTS/` — with its origin marked |
| The inquiry changed direction | a short entry in `LEARNING_PATH.md` |
| A repeatable way of studying the subject developed | `STUDY_GUIDE.md` (any topic may have one) |
| The owner explicitly loves it | `90_TRACKING/FAVORITES.md` |

**A file existing means something.** A page exists only when there is substantive
knowledge in it — never a placeholder, a stub or a “not written yet”. Agents must be
able to trust that every page is real knowledge without opening it.

**The folders are always the same** — numbered by the one list in
`02_REFERENCES/REPO_SETTINGS.json`; a topic has only the ones it uses, and a folder
appears with its first page:

| Folder | Holds | One item is |
|---|---|---|
| `10_PEOPLE/` | a folder per person — PROFILE.md (who they are, their story, why they matter here) and WORKS.md | a folder `first-last/` with `PROFILE.md` + `WORKS.md` |
| `11_GROUPS/` | schools, movements, organizations, lineages | a page `short-name.md` |
| `12_PERIODS/` | eras and events worth studying on their own | a page `short-name.md` |
| `13_WORKS/` | buildings, books, artworks — studied as objects in themselves | a page `short-name.md` |
| `14_PLACES/` | real locations | a page `short-name.md` |
| `15_CONCEPTS/` | ideas, principles and terms | a page `short-name.md` |
| `16_PRACTICES/` | techniques, methods, exercises — things you do (with a level when there is an order) | a page `short-name.md` |
| `17_SYSTEMS/` | products, tools and implementations (technology topics) | a page `short-name.md` |
| `18_PATTERNS/` | reusable designs (technology topics) | a page `short-name.md` |
| `19_RESOURCES/` | what you learn from — books, papers, courses, videos — each with its link and what it contributes | a page `short-name.md` |
| `90_TRACKING/` | the owner’s progress — `TO_EXPLORE.md` · `STUDIED.md` · `READING_QUEUE.md` · `FAVORITES.md` | a row per item |

Pages never say whether the owner studied them — progress lives only in
`90_TRACKING/`. Link with relative links (`../10_PEOPLE/frei-otto/PROFILE.md`) so pages open on GitHub and in MyRepo.

**When the owner says…**

- **“What’s next?”** — the first row of `90_TRACKING/TO_EXPLORE.md`; in a topic with a
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

**The lists in `90_TRACKING/`:**

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
  `02_REFERENCES/AREA_TEMPLATE/README.md` §Topic layouts.
<!-- myrepo:end proposing -->

## Push-back is mandatory

If you disagree with anything in this repository — or a human tells you something
here is wrong — **write it down** (or emit a `SAVE` block). One area → its
`05_PUSH_BACK/`; cross-area or repo-level → `90_PUSH_BACK/`. Record rejected
push-back as carefully as accepted. Do not silently comply with something you
believe is wrong; do not silently override it either.

Protocol: `02_REFERENCES/PUSH_BACK_PROTOCOL.md`.

## Reviewer

**Context reviewer / owner:** _set during setup_ — the human who promotes drafts
to `canonical`.

## Deferred machinery

- `scripts/check_new_folder_guidance.py` runs on every push (GitHub Actions): a new
  area or sub-area without AGENTS.md + README.md, or a new record without a
  header, or a new top-level area without an unused number, fails the check.
- `03_REPORTS/` + index generator — add when cross-area search gets painful.
- `90_PUSH_BACK/` — create on first cross-area dispute.
- Sensitivity-gated areas (finance, health, admin) — not created by default;
  sensitive personal content does not enter this repo without an explicit owner
  decision.
