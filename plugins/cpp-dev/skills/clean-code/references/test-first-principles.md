---
title: "Apply FIRST to Tests"
impact: MEDIUM
impactDescription: "Aim for tests that are fast, independent, repeatable, self-validating, and timely"
tags: clean-code, test
---

## Apply FIRST to Tests

Aim for tests that are fast, independent, repeatable, self-validating, and timely. Keep inputs and expected results explicit, avoid order-dependent state, and make success or failure observable without manual interpretation.

Use controlled fixtures for external dependencies. Integration coverage can have a real cost; place it deliberately instead of removing meaningful coverage to claim that every check is fast.

Reference: [Clean Code, Chapter 9: Unit Tests](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
