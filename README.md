# SAA-C03 Notes & Quizzes

Free study notes, diagrams, quizzes and drills for the **AWS Certified Solutions Architect – Associate (SAA-C03)** exam.

Each section has:
- **Study notes**: comparison tables, diagrams, common traps, and an "on the exam" box that maps keywords to answers.
- **Quiz**: 20 random scenario questions, with an explanation for every option and a "retry missed" list.
- **Drills**: quick interactive rounds (this-or-that, match-up, sort into boxes, spot the keyword) for services that look alike.

A **mock exam** mixes 65 questions from every section, with an optional 130-minute timer, a score by section and a review of what you missed.

Three styles (Notebook, Blueprint, Terminal) with light and dark modes. Progress is saved in your browser only.

## Run it locally

```sh
python3 -m http.server 8000
# open http://localhost:8000
```

## Structure

```
index.html              the engine (UI, quiz, drills); no content inside
content/
  manifest.json         the section list and which sections are live
  <section>.json        notes + questions + drills for one section
  weakspots.json        topics that are easy to confuse
  corrections.json      common wrong or outdated statements, fixed
  diagrams/*.svg        diagrams, themed by the page's CSS
scripts/check.py        validates content (CI runs it on every PR)
docs/decisions/         why things are built this way
```

## Contributing

Found a mistake or an outdated fact? Open an issue or a PR. Run `python3 scripts/check.py` before opening a PR.
