---
title: ID Registry
status: draft
last_verified: 2026-09-29
---

# ID Registry

**One canonical owner per prefix.** Records mint IDs using the prefix of the area
they live in. **Never invent an ID** — if no registry entry exists for the
subject, use `subject_text:` and let the owner mint the ID.

## Area prefixes

| Prefix | Owner (folder) | Status |
|---|---|---|
| `RF-` | `901_READ_FIRST/` | active |
| `REF-` | `902_REFERENCES/` | active |
| `REV-` | `915_PUSH_BACK/` | reserved — create on first cross-area dispute |
| _(add each area's prefix here when you create it)_ | | |

## `subject:` kinds

Subjects in front-matter are `<kind>:<id>` pairs. Starter kinds — extend by
editing this table, not ad hoc in records:

| Kind | Example |
|---|---|
| `person` | `person:<name-slug>` |
| `organization` | `organization:<slug>` |
| `project` | `project:<slug>` |
| `topic` | `topic:quantum-physics` |
| `technology` | `technology:<slug>` |
| `product` | `product:<slug>` |
| `document` | `document:<id>` |

Mint new kinds by adding them to this table — not ad hoc in records.
