---
title: Avoid Returning and Passing Null
impact: HIGH
impactDescription: makes expected absence explicit to callers
tags: err, null, optional, null-object
---

## Avoid Returning and Passing Null

An ambiguous absent result creates work for callers. Make the outcome clear: an empty collection can mean there are no matching items, while an operational failure must keep its own error contract. Do not invent a dummy value to conceal failure.

**When null/nullable is acceptable:**
- Expected absence can be a legitimate part of a documented API. Keep the project's representation and distinguish an empty result from an operational failure.
- Existing APIs with an explicitly documented absence representation.

Reference: [Clean Code, Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [err-avoid-null](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/err-avoid-null.md).
