# 0002. One static engine, content as JSON, no build step

_Date: 2026-10-24 · Status: accepted_

## Context
The site started as a claude.ai Artifact and is now a public repo that should be easy to host, review and extend to 10+ sections. Content changes far more often than the UI.

## Options
1. **Single HTML file with everything inside** - simplest to host / every content change is a diff inside a 1,000+ line file, and contributors must touch UI code to fix a typo.
2. **Static site generator (Astro, Docusaurus, Next) with Markdown** - nicest authoring, plugins, search / a Node toolchain, a build step, dependency upgrades, and the interactive quiz and drills would need porting into components.
3. **One static `index.html` engine + JSON content + SVG diagrams** - zero dependencies, GitHub Pages serves it as is, the same files run as the Artifact, content diffs are small and reviewable, and a script can validate it / JSON with inline HTML strings is clunkier to write than Markdown.

## Decision
Option 3.

## Why
The interactive parts (quiz, drills, progress in localStorage) already exist in the engine, and most future work is adding content. A data format that a script can check (answer indexes, weak-spot coverage) protects quality better than Markdown would, and no build step means nothing to break or upgrade.

## Consequences
- Easier: adding a section is one JSON file + a manifest flag; CI is a Python script.
- Harder: long prose in JSON; no SEO for individual sections (single page, hash routes).
- Revisit if: authoring JSON slows contributors down (add a Markdown → JSON script), or search engines need to index sections (pre-render one HTML page per section).
