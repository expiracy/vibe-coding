---
title: Follow the Four Rules of Simple Design
impact: HIGH
impactDescription: prevents over-engineering while maintaining quality
tags: emerge, simple-design, kent-beck, refactoring
---

## Follow the Four Rules of Simple Design

The upstream guide presents these simple-design priorities:

1. **Passes all tests** — correctness is non-negotiable
2. **Reveals intent** — code is clear and expressive
3. **No duplication** — every concept has a single representation
4. **Fewest elements** — remove anything that doesn't serve the first three

**Rule 4 is the most overlooked:** After making code correct, expressive, and DRY, actively look for things to remove. Every class, method, and variable should justify its existence. If you have one implementation of an interface, question whether you need the interface. If a design pattern adds indirection without a current concrete benefit, remove it.

**When more structure is justified:**
- When you have 2+ implementations today (not hypothetically)
- When a framework requires it (e.g., dependency injection interfaces)
- When tests need seams for mocking external dependencies

Reference: [Clean Code, Chapter 12: Emergence](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [emerge-simple-design](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/emerge-simple-design.md).
