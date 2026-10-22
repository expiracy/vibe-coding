---
title: Separate Construction from Use
impact: MEDIUM
impactDescription: enables testing and reduces coupling
tags: class, construction, factories, separation
---

## Separate Construction from Use

The startup process of object construction is a separate concern from runtime logic. Applications should separate the main function (which builds objects) from the rest of the system (which uses them).

Use the existing application composition approach; no dependency-injection framework is required by this principle.

Reference: [Clean Code, Chapter 11: Systems](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [class-separate-concerns](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/class-separate-concerns.md).
