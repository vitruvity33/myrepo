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

<!-- myrepo:begin modes -->
## Folder contexts and conversation modes

Six labels, each with one job. The first three describe the folder and stay put; the last
two change as you talk:

| Label | Where it comes from | What it tells you |
|---|---|---|
| **Function** | the area’s ⚙ (Leadership, Operations, Finance, People, Product or the owner’s own) | vocabulary, templates, who decides by default, what never to save |
| **Area** | the nearest folder up the tree marked “Area of” (June, Finance) | the ongoing home of the work — what lasts lives here |
| **Work type** | the work folder’s ⚙ — Study, Research, Initiative, Operation | how the work ends: keeps growing, gets answered, gets achieved, or repeats |
| **Folder name** | the folder | the specific subject (image-derived canvas, customer onboarding) |
| **Doing now** | the conversation — Explore, Learn, Investigate, Strategize, Decide, Plan, Coordinate, Execute, Monitor, Review, Communicate | how to help at this moment |
| **Save as** | each thing worth keeping — proposal, assumption, finding, decision, commitment, outcome … | what was actually established, and how far to trust it |

Find them in the `myrepo:begin topic` block of the folder’s `AGENTS.md` and the folders above it. A
folder that says nothing is Study (this repo’s default).

**How the people here work** — work this way:

> We think out loud. Brainstorming stays loose until someone argues for something — then it is that person’s position. Keep who said what; an agent’s suggestion is a proposal, never a decision. When we stop, save what was decided and why, what changed, who committed to what, and what is still open.

### Areas and work folders

- **An area** is a function’s ongoing home (June → Product; monthly finance → Finance). It keeps
  what lasts: `OVERVIEW.md` (what it is and how it works now), `DECISIONS.md` (decisions that still
  hold), `GAPS.md`. It never “finishes”.
- **A work folder** sits inside an area and has a work type:

| Work type | For | Ends | Starts with |
|---|---|---|---|
| Study | understanding a subject over time | never — understanding keeps growing | §Working in a topic — unchanged |
| Research | answering a question well enough to act on it | when the question is answered with stated confidence | `QUESTION.md` (incl. when we know enough to stop), `FINDINGS.md` |
| Initiative | achieving an outcome | when the outcome is achieved (or dropped) | `OVERVIEW.md` (outcome, why, scope, done when), `DECISIONS.md`, `GAPS.md` |
| Operation | running something that repeats | never — it runs on a cadence | `PROCESS.md` (cadence, owner, steps, handoffs), `DECISIONS.md`, `MEASURES.md` when something is watched |

- Research lists in `90_TRACKING/`: `OPEN_QUESTIONS.md` · `SOURCES_TO_READ.md`.
- Initiative lists in `90_TRACKING/`: `OPEN_QUESTIONS.md` · `NEXT_UP.md`.
- Operation lists in `90_TRACKING/`: `EXCEPTIONS_TO_REVIEW.md`.
- **Closing.** When an Initiative is achieved (or dropped), write its outcome at the top of its
  `OVERVIEW.md` and move what lasts **up to the area** — how things work now, decisions that still
  hold, open gaps. When Research is answered, its conclusion goes up to the folder it served.
  Nobody should need a finished folder to know how things work today.
- **Serves the folder above.** A folder that serves the one above narrows it (research for this
  initiative); it never silently replaces it, and its results must answer that folder’s need.
- **Templates.** A work folder may follow one of its function’s templates; its stage folders
  (`10_`, `20_` …) appear only when they have a page. Stages guide; they aren’t gates.
- **A file existing means something** — no placeholders, no empty stage folders.
- Every design, architecture or process page says `describes: current` (how it is),
  `describes: proposed` (what we want) or `describes: partial` (half-done).

**Functions** — set in Settings → Functions:

- **Leadership** — direction, priorities and cross-functional tradeoffs. Default decider: the CEO. Templates: Strategy cycle (Situation → Objectives → Options → Direction → Follow-through).
- **Operations** — processes, handoffs, service levels and exceptions. Default decider: the COO. Templates: Process change (Current process → Problem → Redesign → Rollout → Review); Recurring operation (Prepare → Run → Check → Exceptions → Improve).
- **Finance** — models, forecasts, actuals, controls and funding. Default decider: the CFO. Templates: Forecast (Assumptions → Model → Forecast → Actuals → Variance); Monthly close (Prepare → Reconcile → Review → Close → Report); Financing (Need → Options → Terms → Decision → Close). **Never save:** Bank, card and account numbers; Pay or compensation of named people.
- **People** — roles, hiring, policies and how people work together. Default decider: the head of People. Templates: Hiring cycle (Need → Role → Sourcing → Interviews → Offer → Onboarding); Policy (Need → Draft → Review → Approve → Communicate). **Never save:** Individual employee records; Salaries, performance reviews and complaints about named people; Health, leave or personal circumstances of anyone.
- **Product** — problems, users, experience, design and how it is built. Default decider: the product owner. Templates: Product build (Research → Product → Design → Architecture → Implementation); Experiment (Hypothesis → Design → Run → Results → Decision).

A default decider is a default, not an approval: a title alone never makes something decided.

### Doing now

Recognize what the conversation is doing; don’t make anyone pick from a list. Name a shift only
when it changes what you’ll produce (“We’ve moved from exploring options to choosing one”) —
not every small turn — and let them correct you. One challenge at a time.

**Explore** — *What could this be?*
- Listen for: the idea in the person’s own words; possibilities and tensions; which parts are theirs and which the agent suggested.
- Push back like: “Which part of that is yours, and which did I add?” · “Want to keep this as a possibility, or is it becoming a proposal?”
- Save: the original idea, in their words; possibilities worth returning to, and objections; how the thinking changed — never as a plan or decision.

**Learn** — *What am I trying to understand?*
- Listen for: what the person already knows; what resonates; a misconception; a connection to earlier material; the next useful question.
- Push back like: “What drew you to that?” · “That connects to X — follow that thread?” · “Is that the established view, or your own reading?”
- Save: what was learned, on the pages it touched; the person’s own ideas as concepts (origin: owner); what to explore next.

**Investigate** — *What are we trying to establish?*
- Listen for: the question and what the answer is for; “I think…” — an assumption, not evidence; the quality of a source; a contradiction; enough evidence to stop.
- Push back like: “What would this need to establish for you to decide?” · “That’s an assumption so far — what would make it a finding?” · Inside an initiative: “What does this tell us about it?”
- Save: findings with confidence and sources; assumptions still untested; what remains unknown.

**Strategize** — *Which direction, and what do we give up?*
- Listen for: the outcome that matters most; competing goals and constraints; what each path requires giving up.
- Push back like: “What are we choosing between?” · “What would we stop doing if we went this way?”
- Save: the chosen direction, rationale and rejected alternatives; assumptions that could change it, and when to revisit; the decisions and plans it leads to.

**Decide** — *What are we choosing, and who chooses?*
- Listen for: the decision question; options and criteria; positions — who holds each; who has authority here; an actual choice (“okay, let’s do B”).
- Push back like: “There are two positions here — record it as unresolved?” · “Who makes this call?” · “I’ll record B as decided by you, because X, accepting Y. What would make you revisit it?”
- Save: a decision: options, positions, decided_by, date, because, tradeoff, revisit_if; or the open decision with its positions — a proposal stays a proposal until the decider chooses.

**Plan** — *What has to happen, in what order?*
- Listen for: the agreed outcome; workstreams and sequence; dependencies and resources; a constraint that reopens the decision.
- Push back like: “What must happen first?” · “Who owns this part — have they agreed?” · “This plan needs X we don’t have — back to the decision?”
- Save: scope, sequence, milestones and dependencies; proposed owners (until they accept); changes to the plan and why.

**Coordinate** — *Who is doing what, and who is waiting on whom?*
- Listen for: commitments vs suggestions; handoffs; people understanding the work differently.
- Push back like: “Has X accepted that, or did we assign it?” · “Who needs to know?”
- Save: commitments — who accepted what, by when; handoff expectations; unresolved disagreements.

**Execute** — *What was authorized, and what happened?*
- Listen for: what was approved vs what is being done; what exists vs what was intended; an exception that needs a decision; what doing it exposed.
- Push back like: “Is that the approved change, or a new one that needs a decision?” · “The design and what we built disagree — which is right?”
- Save: what was done, by whom, when, linked to its decision or plan; deviations and what they revealed; never live task status — that belongs in a task tracker.

**Monitor** — *Is reality moving away from what we expected?*
- Listen for: the measure and its expected range; a change; normal variation vs a signal.
- Push back like: “Is that noise, or a signal we act on?” · “What range did we expect?”
- Save: measure definitions and thresholds; meaningful changes and why they did or didn’t lead to action.

**Review** — *What did we expect, what happened, and what changes?*
- Listen for: the original expectation; the actual outcome; why they differ.
- Push back like: “What did we expect when we decided this?” · “Is this a lesson, or a change we’re agreeing to make?”
- Save: outcomes and variance; corrected assumptions; agreed changes — linked to the original decision or plan.

**Communicate** — *Who needs to understand what?*
- Listen for: the audience and what they need to know or decide; evidence and tone; questions and objections that come back.
- Push back like: “Who is this for, and what should they do after reading it?”
- Save: the approved position and meaningful feedback — not every draft; promised follow-ups.

### Save as

What kind of thing it is and where it stands are two separate fields. Every row in
`DECISIONS.md`, `GAPS.md` and the lists, and every page header, says both where it applies:

| Type | What it is | Must carry |
|---|---|---|
| brainstorm | loose possibilities while thinking out loud | — **never saved as knowledge** |
| proposal | a specific option someone (or an agent) suggests | `proposed_by:` — stays a proposal until the decider chooses |
| position | someone is arguing for this | `held_by:` |
| assumption | the work depends on it being true, unproven | what would test it |
| evidence | something supported outside the conversation | its source (linked) |
| finding | a conclusion research supports | confidence and the evidence |
| question | something still to find out | why it matters |
| decision | an authorized choice | `decided_by:` (who actually chose), date, `because:`, `revisit_if:` |
| commitment | someone accepted responsibility | `owner:` (who accepted — not who was suggested), what, by when |
| outcome | what actually happened | what it changed or revealed, linked to its decision or plan |

States: `open` · `accepted` · `rejected` · `superseded` (link what replaced it — never delete it).
Live task status (who is doing what today) belongs in a task tracker, not here.

**Who said it.** Name the person behind every proposal, position, decision and commitment.
“Sam thinks X” and “we decided X” are different records — never collapse two positions into
one, and never write “decided” unless someone with the authority chose it. Unclear? Ask.

**Which record answers which question** — when records disagree, say so and cite both:

| Question | Answer from |
|---|---|
| What are we doing / what is the intent? | the area’s and initiative’s `OVERVIEW.md`, and `accepted` decisions |
| Why? | the decision’s `because:` and the findings behind it |
| How does it work today? | pages marked `describes: current`, an operation’s `PROCESS.md` |
| Who is doing it? | `accepted` commitments |
| What does someone think? | their proposals and positions |
| What is still uncertain? | open questions, assumptions and `GAPS.md` |

**Example**

| Moment | Function / area | Work type | Folder | Doing now | Save as |
|---|---|---|---|---|---|
| Canvas discussion | Product / June | Initiative | image-derived canvas | Explore | proposal |
| Canvas approach chosen | Product / June | Initiative | image-derived canvas | Decide | decision |
| COO fixes onboarding | Operations / customer onboarding | Operation | onboarding process | Execute | commitment, outcome |
| CFO checks runway | Finance / planning | Research | runway assumptions | Investigate | finding, assumption |
| CEO sets direction | Leadership / company strategy | Initiative | next-year priorities | Strategize | proposal, then decision |

Work types: Study, Research, Initiative, Operation — set in MyRepo (each folder’s ⚙; the default in Settings → Ways of working).
<!-- myrepo:end modes -->

<!-- myrepo:begin working -->
## Working in a topic

How a **Study** folder works (Research, Initiative, Operation and areas: §Folder contexts and conversation modes).
Every study topic works the same way, so the owner can ask the same things anywhere.

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
- **Explore, study, or keep?** A topic is for **exploring** (curiosity — things
  the owner is drawn to and collects), **studying** (learning over time, in an
  order) or **reference** (kept to look up and build with). Tell from how the
  owner talks; if unclear, ask that one question. A topic can change kind later.
- **A new topic** picks its kinds from the one list (§Working in a topic) — propose
  which, with reasons, ask, and record the choice in the topic's `AGENTS.md`.
- **Folders of the owner's own.** When the owner asks for a folder the list doesn't
  have (in one topic only), make it — numbered after the standard ones (`20_`, `21_` …)
  — and note it in that topic's `AGENTS.md` §Layout so every tool finds it. Don't invent
  one unasked: suggest it, or suggest adding a kind to the list for every topic
  (MyRepo → repo ⚙ → Studying) when it would fit topics generally. Details:
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
