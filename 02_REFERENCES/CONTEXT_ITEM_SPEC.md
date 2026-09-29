---
title: Context Item Spec
status: draft
last_verified: 2026-09-29
---

# Context Item Spec

**The shared record format for this repository.** Any tool or person saving
knowledge here uses this format.

> **One small claim per file.** Link long conversations as evidence via
> `source_refs:` — never paste transcripts in.

---

## The three questions every record must answer

Any tool must be able to answer these from the front-matter alone.

| # | Question | Fields | Why |
|---|---|---|---|
| 1 | **What is it about?** | `subject:` (IDs from `ID_REGISTRY.md`) or `subject_text:` when no ID exists. **Scope = the folder it sits in** | Finding knowledge by what it's about |
| 2 | **What kind of statement is it?** | `context_type:` | A decision, a dispute and an assumption are used differently |
| 3 | **How much should it be trusted?** | `status` + `confidence` + `raised_by` + `reviewed_by` (+ `resolution` for disputes) | A claim from one chat is a report, not a fact. Only reviewed items are canonical |

## `context_type` — function of the statement, and where it files

| `context_type` | Use when | File in |
|---|---|---|
| `decision` | A decision was made, with the evidence behind it | `01_RECORDS/06_DECISIONS/` |
| `outcome` | What happened after a decision | `01_RECORDS/06_DECISIONS/` |
| `assumption` | Taken as true, not yet tested | `01_RECORDS/02_QUESTIONS/` |
| `known_issue` | A confirmed, stable problem or limitation | `01_RECORDS/02_QUESTIONS/` |
| `methodology` | How something should be done or analyzed | `01_RECORDS/03_REFERENCES/` |
| `definition` | What a term means | `01_RECORDS/03_REFERENCES/` |
| `dispute` | Someone says a conclusion, number or record is wrong | area `05_PUSH_BACK/` · cross-area: `90_PUSH_BACK/` |
| `preference` | How the owner wants output produced | `02_REFERENCES/preferences/` (scope `global`/`artifact_type`) or the area (scope `area`/`project`) |
| *(unsure)* | Unsorted capture | `00_INBOX/` |

## `record_form` — the container, never the meaning

`record_form:` describes how the content arrived or is held — it does **not**
route the record:

| `record_form` | What it is |
|---|---|
| `conversation` | A chat/meeting transcript or summary. *Contains* statements — extract each into its own record and link back via `source_refs:` |
| `artifact` | A deliverable — document, deck, application |
| `source_document` | An intact external document — posting, article, PDF |
| `note` | A plain note or capture |

## Trust fields

| Field | Values |
|---|---|
| `status` | `draft` (agent-written default) · `canonical` (human-promoted) · `superseded` (+`superseded_by:`) · `blocked` (+`blocked_by:`) · `retired` |
| `confidence` | `confirmed` · `derived` · `working` · `hypothesis` · `unknown` |
| `raised_by` | person or role — usually the owner |
| `raised_via` | `chatgpt | claude | devin | meeting | email | other` |
| `source` | who authored the file — `gpt | claude | devin | human` |
| `source_type` | `user_statement | document | conversation | agent_inference` |
| `reviewed_by` | `none` until a human promotes it |
| `resolution` | disputes only: `accepted | rejected | partial | unresolved` |
| `scope` | preferences: `global | artifact_type | area | project` |
| `sensitivity` | `normal | private | restricted` — flag before saving anything sensitive; every connected tool can read this repo |

## Front-matter (flat `key: value`; inline lists `[a, b]` — no nested YAML)

```yaml
---
id: <PREFIX>-NNN                 # owning area's prefix; use subject_text if no ID exists
title: One line
kind: record                     # plan | record | reference | capture | decision | analysis
context_type: <from table above>
record_form: <conversation | artifact | source_document | note>
subject: [<kind>:<id>]           # e.g. [person:jane-doe, project:remodel]
subject_text: <the words used>
claim: <one sentence — what this record asserts>
status: draft
confidence: <confirmed | derived | working | hypothesis | unknown>
scope: <preferences only>
sensitivity: normal
raised_by: <owner>
raised_via: <chatgpt | claude | devin | meeting | email>
source: <gpt | claude | devin | human>
source_type: <user_statement | document | conversation | agent_inference>
source_refs: []                  # links/IDs of the conversation or doc this came from
contributors: []
reviewed_by: none
resolution:                      # disputes only
challenges: []                   # disputes: IDs of challenged records
references: []                   # IDs/paths this depends on
supersedes: []
superseded_by:
blocked_by: []
last_verified: YYYY-MM-DD
---
```

**Required:** `id` or `subject_text`, `title`, `kind`, `context_type`,
`record_form`, `status`, `confidence`, `raised_by`, `source`, `reviewed_by`,
`last_verified`. Disputes also require `resolution` and `challenges` (`[]` when
about data rather than a document).

**Body:** one short paragraph. Disputes use the push-back sections
(`PUSH_BACK_PROTOCOL.md`). No transcripts.

## File naming

`YYYY-MM-DD_SHORT-TOPIC.md` for dated records. `00_`, `01_`… prefixes for
ordered/reference docs.

## What NOT to record

- Ordinary questions, pleasantries, one-off passing mentions.
- Anything already recorded — **update or supersede it instead**.
- `private`/`restricted` content without flagging it first — every connected
  tool can read this repo.
