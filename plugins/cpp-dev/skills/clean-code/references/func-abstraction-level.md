---
title: Maintain One Level of Abstraction
impact: CRITICAL
impactDescription: prevents jarring context switches
tags: func, abstraction, stepdown, readability
---

## Maintain One Level of Abstraction

Statements within a function should all be at the same level of abstraction. Mixing high-level concepts with low-level details is confusing. Code should read like a top-down narrative.

Read the code from top to bottom. Each function introduces the next level of abstraction.

**When mixing levels is acceptable:**
- Short utility functions (under 10 lines) that perform one task can mix levels without confusion. The overhead of extracting one-line helpers often exceeds the readability benefit.
- Test code frequently mixes setup (low-level) with assertions (high-level) — this is expected and follows the Arrange-Act-Assert pattern.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [func-abstraction-level](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/func-abstraction-level.md).
