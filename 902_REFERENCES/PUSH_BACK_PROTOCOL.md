---
title: Push-Back Protocol
status: draft
last_verified: 2026-09-29
---

# Push-Back Protocol

Push-back is **mandatory** — see root `AGENTS.md`.

## When to write a push-back record

- The owner **questions** an answer or a record — "are you sure?", "that doesn't
  sound right" — even without a counter-claim yet. Record it open, then check it
- Someone disagrees with a conclusion, number, or recommendation
- **Your analysis contradicts an existing record**
- An assumption is challenged
- **You are told you are wrong**
- **You believe the repository is wrong**
- A decision is reversed

## Where it goes

| Scope | Folder |
|---|---|
| One area or sub-area | `<AREA>/910_RECORDS/915_PUSH_BACK/` |
| Cross-area, or challenges the repo itself | `915_PUSH_BACK/` (create it on first use) |

Filename: `YYYY-MM-DD_SHORT-TOPIC.md`.

## Required body sections

1. **The claim being challenged** — quote it, cite the file
2. **The challenge** — what is asserted instead, and why
3. **Evidence** — links, records, `source_refs:` — never transcripts
4. **Proposed resolution** — what should change if accepted

Two kinds:

- **Question / dispute** — still open: `context_type: dispute`, `resolution: unresolved`
  until checked, then `accepted | rejected | partial`.
- **Correction** — it was wrong and this is the right version: `context_type:
  correction`, `supersedes: [<the old record>]`; mark the old record `status:
  superseded` + `superseded_by:` so it stops being cited.

Front-matter for a dispute: `context_type: dispute`, `resolution: unresolved`,
`challenges: [<IDs of challenged records>]` (`[]` if about data not a document).

## Rules

- **Record rejected push-back as carefully as accepted.** `resolution: rejected`
  means it was reviewed and not agreed — it stays findable so the same point
  isn't re-raised blind.
- Do not silently comply with something you believe is wrong.
- Do not silently override it either.
- A tool that cannot write files emits the entry as a `SAVE` block — the
  obligation to record travels even when the write capability doesn't.
- Style/format disagreement is *also* a correction-loop event: propose a
  `902_REFERENCES/preferences/` update when the correction is durable and
  scoped `global` or `artifact_type`. Project-specific push-back stays in the
  project's `915_PUSH_BACK/`.
