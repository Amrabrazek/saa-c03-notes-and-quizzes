# SAA-C03 Notes & Quizzes

Free, public study notes + quizzes + drills for the AWS SAA-C03 exam, built from Amr's own study guide. Why and for whom: `docs/brief.md`.

## Commands
- Run locally: `python3 -m http.server 8000` then open http://localhost:8000 (needs a server; `fetch` fails on file://)
- Check content: `python3 scripts/check.py` (built sections) or `python3 scripts/check.py <id> ...`
- No build step, no dependencies. GitHub Pages serves the repo root.

## Where things live
- `index.html`: the whole engine (CSS + JS). Content never goes here.
- `content/manifest.json`: section list; a section shows when `"built": true, "file": "content/<id>.json"`.
- `content/<id>.json`: one section = `notes` blocks + `questions` + `drills`. `content/edge.json` is the reference.
- `content/weakspots.json`, `content/corrections.json`: Amr's weak spots and the fixes to his old guide.
- `content/diagrams/*.svg`: inlined at runtime; use the `.dg-*` classes so all 3 styles × 2 modes work.

## Content rules
- Exam-first and plain. Every topic ends with an `exam` block (keyword → answer).
- More than ~4 names in a sentence → a one-line rule + a table with a "why / do instead" column.
- No "weak spot" or "fix" labels inside sections. Sections show only the correct statement; tracking lives on the weak-spots page.
- 20 scenario questions per section, using qualifiers ("least overhead", "most cost-effective"). Wrong options are real confusions, and every option has a `why`.
- Every weak spot and fix for a section is tagged (`weak` / `fix`) on at least one question. `check.py` enforces this.
- Drills only where they fit: `thisorthat`, `match`, `buckets`, `keyword`.
- Check facts that may have changed (limits, renamed or retired services) and say when the exam answer differs from today's AWS.

## How we work
- Backlog is GitHub Issues. One section or fix per PR.
- Before a PR: `check.py` passes, and the page has no console errors at 390px and desktop width in all styles and modes.
- Non-obvious decisions get an ADR in `docs/decisions/`.

---
_When Claude makes the same mistake twice, add one line above. Delete lines that stop being true._
