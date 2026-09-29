---
title: Website prototype — agent rules
status: draft
reviewed_by: none
last_verified: 2026-09-30
---

# AGENTS.md — `website/`

**Entry point for any agent working on the MyRepo website prototype.**
Read this before editing any file in this folder.

---

## What this is

The product website for MyRepo, being designed screen-by-screen from Excalidraw
drawings. **Prototype stage:** static HTML + one shared stylesheet, no build
step, no framework, no JavaScript. Serve locally:

```bash
python3 -m http.server 8000   # from this folder → http://localhost:8000
```

## Visual language — hand-drawn sketch

The prototype deliberately looks like the Excalidraw drawings it is built from:

- **Ink on paper.** `var(--ink)` strokes on `var(--paper)` — no gradients, no
  shadows, minimal color. `--accent` for links/primary actions only.
- **One stroke weight for structure.** `--stroke` (2px ink) is the default for
  anything that would be a drawn line in the sketch — rails, boxes, buttons,
  menu squares. `--stroke-thin` is for hairlines only; never mute structural
  borders to `--ink-muted` (the menu-button bug).
- **Sketch radius — subtle, not cartoon.** Irregular `--radius-sketch*` tokens
  (~8–24px wobble) read as hand-drawn. Never the giant 255px ellipses, and
  never uniform `border-radius: 8px` on product UI.
- **Hand font.** `--font-hand` (Patrick Hand — the Virgil stand-in) for
  headings, wordmark, drawn elements. `--font-ui` for everything else.

## Persistent shell

Every screen has the same frame (per the sketches). **"Global" always means
app-level** — the two side-bars. Everything inside `.canvas` belongs to the
active screen.

```
proto-bar (tooling — not product UI)
app-header:  wordmark left · optional .page-title centered
app-body:
  side-bar-left        Screens — Folders · Documents · Storage · Connections · Settings
  canvas               the active screen's workspace:
    top-menu-bar       the screen's modes — e.g. View · Edit · Outline
    tool-bar           tools of the ACTIVE mode
    panes              draggable viewing areas: .pane .pane .pane
  side-bar-right       Global Tools — act on whatever is on screen
```

- **`.side-bar-left` / `.side-bar-right`** — the two rails are **mirrors of
  each other**: same component, same style, siblings of `.canvas` inside
  `.app-body`. Never nest one inside the canvas.
- **Hidden, never removed.** Screens that don't show a rail (landing,
  sign-in) keep the markup and add `--hidden`
  (`.side-bar-left--hidden` / `.side-bar-right--hidden`) — the rail is
  invisible but holds its space, so the canvas is in the **exact same
  position** on every screen.
- **`.screen-btn` / `.global-btn`** — **88×88px squares** (`--sq-btn-size`),
  `var(--stroke)` border, `--radius-sketch-sm`. Screens in the left rail,
  global tools in the right rail. `.placeholder` = empty square.
- **`.top-menu-bar` + `.menu-btn`** — the screen's modes/functions
  (level 2 of the sketch).
- **`.tool-bar` + `.tool-btn`** — tools for the active mode (level 3).
  Navigation = `.nav-btn`.
- **Both strips are split into two zones.** Direct children align left;
  a trailing cluster wrapped in `.menu-bar-end` / `.tool-bar-end` aligns
  right (`margin-left: auto`). Modes/tools on the left; screen-level
  actions and navigation on the right.
- **`.panes` > `.pane`** — the viewing areas. Reorderable later; markup
  order is the display order for now.
- **`.canvas`** — the big rounded box; `.top-menu-bar`, `.tool-bar`, and
  `.panes` live inside it. The box IS the canvas — no inner frames.

## Design tokens — the swap layer

All visual values are CSS custom properties in `:root` at the top of
`styles.css`. **Never hardcode** a color, radius, font size, or spacing — use
or add a token:

| Prefix | Covers |
|---|---|
| `--paper`, `--ink*`, `--accent`, `--hover-fill`, `*-fill` | color |
| `--font-*`, `--text-*` | type |
| `--stroke*`, `--radius-*` | borders/shape |
| `--gap-*` | spacing |
| `--menu-row-*` | component sizing |
| `--sq-btn-size`, `--rail-width` | rails & rail squares |

**Sizing tokens.** Elements of the same kind are always identical —
`.menu-row` is exactly `--menu-row-width` × `--menu-row-height`;
`.screen-btn`/`.global-btn` are `--sq-btn-size` squares. Never hand-size a
row or button; if a new kind is needed, add a `--*-width` / `--*-height`
token pair.

**Hover is uniform.** Every interactive element — `.btn`, `.menu-row`,
`.screen-btn`, `.global-btn`, `.menu-btn`, `.tool-btn`, `.nav-btn`, any
clickable thing — lights up with `var(--hover-fill)`, ink text on the fill.
No per-element hover colors.

Swapping the real design later = replacing token values, not rewriting markup.

## Components — reuse, don't invent

| Class | Use |
|---|---|
| `.btn` | buttons/link actions; modifiers `--primary`, `--quiet` |
| `.card` | rounded sketch container |
| `.chip` | small labeled element (badges, tags, kinds) |
| `.menu-rows` + `.menu-row` (`.n` / `.t`) | **the center-menu rectangle** — numbered steps AND standalone actions; same size, centered, hover-fill |
| `.screen-btn` | square in `.side-bar-left` (a Screen) |
| `.global-btn` | square in `.side-bar-right` (a Global Tool) |
| `.menu-btn` / `.tool-btn` / `.nav-btn` | rectangle buttons in the two canvas strips |
| `.top-menu-bar`, `.tool-bar`, `.menu-bar-end`, `.tool-bar-end` | the two strips + right-aligned clusters |
| `.panes`, `.pane` | the draggable viewing areas |
| `.canvas-title` | centered screen title inside the canvas |

Naming convention: `.thing` + `.thing--modifier` (BEM-lite). New components go
in `styles.css` with token-backed styles — no inline styles, no per-page
`<style>` blocks. Screen-specific needs go below a `/* screen-name */` comment.

## File rules

- **One HTML file per screen**, numbered in journey order (`09-browser.html`).
  The proto-bar is **tooling** — stripped when the design is real.
- **200–500 lines per file.** Approaching 400 → refactor (extract shared
  markup or split). `styles.css` may exceed this; split into
  `tokens.css` / `components.css` when it does.
- **Per-screen element spec lives in an HTML comment** at the top of each
  file. Update it when the screen gets built — it records intent.
- **Every page links `styles.css` + the Patrick Hand font.** Copy an existing
  `<head>` when adding a screen.

## Data (when screens get real content)

| File | Contents | Committed? |
|---|---|---|
| `data.js` | Public-safe demo snapshot | yes |
| `data.local.js` | Full personal snapshot | **never** — gitignored |

Pages must degrade to `data.js` when `data.local.js` is absent.
**Never embed private data in HTML or `data.js`.** This repo is public.
