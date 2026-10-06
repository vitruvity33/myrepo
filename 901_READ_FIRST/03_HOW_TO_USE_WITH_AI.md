---
title: How To Use This Repository With AI
status: draft
last_verified: 2026-09-29
---

# How To Use This Repository With AI

## Tools that can read and write the repo

**Devin, Claude Code, Codex, ChatGPT Codex tasks** — point at the root.
It will find `AGENTS.md` automatically.

> "Read AGENTS.md and 901_READ_FIRST/02_AREA_MAP.md, then work inside the
> conventions there."

- ChatGPT sees the **GitHub remote** only — local files are invisible until pushed.
- Writes from ChatGPT arrive as a branch + PR; merging is a human act.

## Tools that cannot read files

**ChatGPT chat (without a repo task), claude.ai, Gemini** — paste the context
block from `902_REFERENCES/prompts/CHAT_CONTEXT.md` first. It carries the rules
the tool cannot read.

## The SAVE block

When a tool cannot write, it ends a save by emitting:

```
SAVE
path: <full path from repo root>/YYYY-MM-DD_TOPIC.md
---
<complete file: full front-matter + body>
```

The owner pastes it in, or hands it to a file-capable agent. **A `SAVE` block is a
fallback — not the primary workflow for tools with repo access.**

## Save triggers

- Any expression of "this should persist" — any words.
- **Mandatory proposals:** durable decisions, disagreements/corrections,
  preferences. The agent proposes (what, where, does it supersede?) and writes
  on approval — unless the owner already asked to persist.
- **Close-out:** end of a substantive conversation → propose what deserves filing.

## Correction loop

"That's cliché / not my format / not how I want it" is not just a fix to the
current output — it triggers a proposed update to `902_REFERENCES/preferences/`
with the right `scope:` (`global | artifact_type | area | project`). Corrections
become permanent rules; the owner should never repeat one.

## Status

Agents write `status: draft`. Promotion to `canonical` is a human act.
**Merge ≠ promotion.**
