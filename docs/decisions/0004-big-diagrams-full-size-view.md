# 0004: Big overview diagrams use a `big` flag and a full-size view

Date: 2026-10-25 · Status: accepted

## Context
Amr wanted the "everything connected" diagrams from his guide (full production architecture, full networking picture). They are about 1000 px wide with a lot of small text. The normal figure (min-width 560 px, scroll sideways) works for small diagrams but makes these unreadable on a 390 px phone.

## Options
1. **Per-section hero diagrams** with "you are here" highlighting. Good context while reading, but 10 near-copies of one big SVG to keep in sync, plus engine work.
2. **One "Big picture" extra page** (ADR 0003) with the big diagrams, and nothing else changed. Cheap, but the diagrams are hard to read on a phone.
3. **Option 2 + an opt-in `"big": true` on diagram blocks.** Big figures get a wider min-width and a "Full size" button that opens the SVG in a full-screen `<dialog>` where it can be scrolled and pinch-zoomed.

## Decision
Option 3. It reuses the extras format and keeps the engine change to one flag and one dialog.

## Consequences
- Any section can mark a diagram `"big": true` later; small diagrams are unchanged.
- The dialog renders the same inlined SVG, so `.dg-*` classes keep working in all styles and modes.
- If per-section maps are still wanted after using the page, revisit option 1.
