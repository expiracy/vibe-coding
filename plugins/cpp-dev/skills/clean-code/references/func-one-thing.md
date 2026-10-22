---
title: Functions Should Do One Thing
impact: CRITICAL
impactDescription: enables understanding functions at a glance
tags: func, single-responsibility, cohesion, focus
---

## Functions Should Do One Thing

Functions should do one thing. They should do it well. They should do it only. If a function does multiple things, extract those things into separate functions.

**Test:** If you can extract another function from it with a name that is not merely a restatement of its implementation, the function is doing more than one thing.

**When NOT to split:**
- Avoid helpers whose names merely restate an obvious operation. A named domain policy such as `calculateTax` can clarify intent even when its implementation is short.
- Orchestration functions that call a sequence of steps at the same abstraction level are doing "one thing" — orchestrating. Don't try to extract the orchestration further.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [func-one-thing](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/func-one-thing.md).
