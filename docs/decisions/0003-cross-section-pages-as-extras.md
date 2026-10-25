# 0003: Cross-section pages are "extras" that reuse the section format

Date: 2026-10-25 · Status: accepted

## Context
The Mix-ups page compares services from many sections (GuardDuty vs Inspector vs Macie, SQS vs SNS vs Kinesis). It needs notes, a quiz and drills, the same as a section, but it isn't one of the 10 numbered exam sections.

## Options
1. **New page type with its own renderer and schema.** Max freedom, but it's a second renderer, a second schema and a second set of checks to keep working in 3 styles × 2 modes.
2. **An 11th numbered section.** No engine change, but it would mess up the numbering and the weak-spot and fix pages, which assume sections are exam domains.
3. **`extras` in `manifest.json` that use the section JSON format.** Small engine change: load them, list them in the menu and Contents, and show "Across sections" instead of a number. They get notes, quiz, drills and `check.py` for free.

## Decision
Option 3. Mix-ups is content, not a new feature, so it should reuse the format we already test.

## Consequences
- Adding another cross-section page (for example a "numbers to memorize" page) is just a JSON file plus one manifest entry.
- Extras don't appear on the weak-spots page, and weak spot and fix tags should stay on numbered sections.
- If an extra ever needs a layout the section format can't express, revisit option 1.
