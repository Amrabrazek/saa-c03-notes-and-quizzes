# 0005: The mock exam is generated from the section question banks

Date: 2026-10-25 · Status: accepted

## Context
Section quizzes give away the topic: inside the Edge quiz the answer is probably CloudFront or Route 53. The real exam mixes every domain, and spotting which one a question belongs to is part of the skill. Amr asked for "general questions".

## Options
1. **Write a new set of general questions** as another extra (ADR 0003). More to write and check, and it overlaps Mix-ups and Big picture, which are already cross-section.
2. **Generate a mock exam from the existing banks.** No new content. 65 questions, picked round-robin so every section and extra gets an even share, optional 130-minute timer, answers shown at the end.
3. **Weight by the official exam domains** (Secure 30%, Resilient 26%, Performance 24%, Cost 20%). Our sections don't map cleanly onto domains, so the weights would be guesses.

## Decision
Option 2. The value is the mixing, not new questions. It is an engine feature (`#exam`), not a content file, so it doesn't fit the extras format.

## Consequences
- Every new question in any section shows up in the mock exam with no extra work.
- Exam misses are added to each section's own retry list, so the section quiz becomes the follow-up.
- Even shares mean Numbers & ports gets as many questions as Security. If that feels wrong, revisit option 3.
