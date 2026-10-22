---
title: Isolate Classes from Change
impact: MEDIUM
impactDescription: enables testing and reduces coupling
tags: class, dip, interfaces, coupling
---

## Isolate Classes from Change

Depend on abstractions, not concretions. Classes should depend on interfaces rather than concrete implementations. This enables testing and reduces the impact of change.

**Dependency Inversion Principle (DIP):** High-level modules should not depend on low-level modules. Both should depend on abstractions.

Reference: [Clean Code, Chapter 10: Classes](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [class-isolate-from-change](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/class-isolate-from-change.md).
