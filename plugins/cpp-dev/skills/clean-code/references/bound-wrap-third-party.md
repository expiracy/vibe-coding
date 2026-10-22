---
title: Wrap Third-Party APIs
impact: HIGH
impactDescription: makes dependency assumptions explicit
tags: bound, boundary, wrapper, third-party, dependency
---

## Wrap Third-Party APIs

When you use a third-party API, wrap it in a class you control. This minimizes your dependency on the third party, makes testing easier, and gives you a single place to change when the API evolves.

**Benefits:**
- One place to change when the third-party API changes
- Tests can substitute the application-facing contract
- Freedom to switch vendors without rewriting the entire codebase
- Consistent exception hierarchy under your control

**When NOT to wrap:**
- Stable, widely-used standard library APIs (e.g., `std::vector`, `std::string`) do not need wrapping.
- If the wrapper would be a 1:1 passthrough with no value added, it's premature. Wait until you have a concrete reason (testing, migration, or simplification).

Reference: [Clean Code, Chapter 8: Boundaries](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [bound-wrap-third-party](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/bound-wrap-third-party.md).
