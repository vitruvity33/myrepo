---
title: Preferences
status: draft
last_verified: 2026-09-29
---

# Preferences

**How the owner wants output produced — stored as governed records.**

A preference is a record with `context_type: preference` and a `scope:`:

| `scope` | Lives here | Example |
|---|---|---|
| `global` | this folder | voice and tone, general style |
| `artifact_type` | this folder | decks, emails — add `applies_to:` |
| `area`, `project` | the area itself, logged in its `910_RECORDS/INDEX.csv` | how one project wants reports |

## The correction loop

"That's cliché / not my format / not how I want it" is not just a fix to the
current output — it's a durable correction. Agents propose an update to this
folder when the scope is `global` or `artifact_type`; area- and project-scoped
corrections stay in that area's records. Corrections become permanent rules —
the owner should never repeat one.

## Empty by design

This folder ships empty. Preferences accumulate from correction — one record per
file, full front-matter per `902_REFERENCES/CONTEXT_ITEM_SPEC.md`, always
`status: draft` until the owner promotes.
