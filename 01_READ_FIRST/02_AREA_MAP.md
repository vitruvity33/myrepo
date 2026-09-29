---
title: Area Map
status: draft
last_verified: 2026-09-29
---

# Area Map

**Which area owns which kind of thing.** Read this to route a save or find a record.

## The ownership rule

> **A folder owns what dies with it.** Endeavors are time-boxed and archive;
> entities are permanent and get referenced via `subject:` — never absorbed.

Test question: *will this matter in five years after its context is gone?*
If not, it belongs inside the endeavor it serves. If it outlives the context,
it belongs to an entity area.

## Areas

The shipped areas are machinery. The rows below them are **yours** — add each
numbered area as you create it.

| Folder | Owns | Kind | ID prefix | Status |
|---|---|---|---|---|
| `01_READ_FIRST/` | Orientation — which area answers which question | reference | `RF-` | active |
| `02_REFERENCES/` | Shared machinery: record spec, push-back protocol, ID registry, preferences, prompts | reference | `REF-` | active |
| `99_OTHER/` | Catch-all; `01_RECORDS/00_INBOX/` receives unsorted captures | — | — | active |
| _(your areas — `10_`, `20_`, `30_` …)_ | _one row per area you create_ | _endeavor / entity / governance_ | _`XXX-`_ | — |

## Reserved — not created

Materialize on first content. Numbers are held here so insertion never renumbers.
Reserve your own as needed — a few conventions worth keeping:

| Number | Intended use | Note |
|---|---|---|
| `90` | `90_PUSH_BACK` | Cross-area disputes only; create on first one |
| `03` | `03_REPORTS` | Generated index/views when search earns it |
| _(high numbers)_ | Sensitivity-gated areas | Finance, health, admin — only with an explicit owner decision; this repo may be public |

## Promotion paths

- **Contacts:** a note inside an endeavor's `03_REFERENCES/` → promoted to a
  people area when the relationship outlives the context.
- **Knowledge:** research inside an endeavor → distilled durable knowledge
  promoted to a research/topic area before the endeavor archives.
- **Sub-areas:** any unnumbered area may be promoted to a top-level number —
  a move, not a redesign.
