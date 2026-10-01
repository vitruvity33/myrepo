---
title: Agents
status: draft
last_verified: 2026-10-01
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

### Routing (context_type → slot)

| context_type | Files to |
|---|---|
| `decision`, `outcome` | `01_RECORDS/06_DECISIONS/` |
| `assumption`, `known_issue` | `01_RECORDS/02_QUESTIONS/` |
| `evidence`, `methodology`, `definition` | `01_RECORDS/03_REFERENCES/` |
| `dispute`, `correction` | area `05_PUSH_BACK/` (cross-area → `90_PUSH_BACK/`) |
| `analysis` | `01_RECORDS/04_MODELS/` |
| `preference` | `02_REFERENCES/preferences/` (global/artifact_type) or the area (area/project scope) |
| anything unsortable | `00_INBOX/` |

The header is the truth and the folder must agree — a push where they disagree
fails the repo rules check. `evidence` needs `source_refs:`; without a source it
is an `assumption`.

`record_form` never routes: raw conversations land in `00_INBOX/` or
`03_REFERENCES/`; artifacts-in-progress live in `work/`.

## Status and promotion

- **Agents write `status: draft` and `reviewed_by: none`. Never `canonical`.**
- Promotion is a human act: the owner sets `status: canonical` + `reviewed_by:`.
- **Merge ≠ promotion.** Git history tells what changed; the status field tells
  how much authority the content has. Drafts legitimately live on `main`.
- Anything in `99_ARCHIVE/` is superseded — never cite it. Anything in
  `00_INBOX/` is unsorted and unreviewed — never cite it.

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
2. **Tell the owner the full folder name before creating it** (e.g.
   `620_DESIGN/`) and wait for a yes.
3. **In the same commit:** the folder's `AGENTS.md` + `README.md`
   (`02_REFERENCES/AREA_TEMPLATE/`), a row in `01_READ_FIRST/02_AREA_MAP.md`,
   its ID prefix in `02_REFERENCES/ID_REGISTRY.md`, and the folder in the area
   list of `02_REFERENCES/prompts/CHAT_CONTEXT.md`.

Finding things relies on the Area Map and indexes, never on what a number
"should" mean. `scripts/check_new_folder_guidance.py` fails a push that adds a
top-level area without a number or with a number already in use.

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
