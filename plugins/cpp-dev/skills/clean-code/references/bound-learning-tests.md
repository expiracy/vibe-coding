---
title: Write Learning Tests for Third-Party Code
impact: MEDIUM
impactDescription: makes dependency assumptions explicit
tags: bound, boundary, learning-tests, third-party, testing
---

## Write Learning Tests for Third-Party Code

When integrating a third-party library, write small tests that verify your understanding of how the API works. These tests serve double duty: they help you learn the API, and they act as a safety net when upgrading the library.

Exercise the actual dependency and configuration whose behavior matters. A
stand-in cannot establish vendor behavior.

**Benefits:**
- Free education on the API's behavior
- On an upgrade, run them to check the dependency assumptions they cover
- Documents exactly which behaviors your code relies on
- Documents the assumptions these focused tests actually exercise

Reference: [Clean Code, Chapter 8: Boundaries](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [bound-learning-tests](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/bound-learning-tests.md).
