---
title: Agents
status: draft
last_verified: 2026-09-29
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

- `context_type:` is the **function of the statement** — `dispute · known_issue ·
  methodology · definition · decision · outcome · assumption · preference`.
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
| `methodology`, `definition` | `01_RECORDS/03_REFERENCES/` |
| `dispute` | area `05_PUSH_BACK/` (cross-area → `90_PUSH_BACK/`) |
| `preference` | `02_REFERENCES/preferences/` (global/artifact_type) or the area (area/project scope) |
| anything unsortable | `00_INBOX/` |

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
- **Mandatory proposals** (agent proposes what, where, and whether it supersedes an
  existing record; writes after approval): a durable decision, a disagreement or
  correction, a preference. Exception: the user already asked to persist it.
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

- Top-level areas are numbered (`10_`, `20_` …) with gaps for insertion.
  **Never renumber.**
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

- `03_REPORTS/` + index generator — add when cross-area search gets painful.
- `90_PUSH_BACK/` — create on first cross-area dispute.
- Sensitivity-gated areas (finance, health, admin) — reserve a number when needed;
  sensitive personal content does not enter this repo without an explicit owner
  decision.
