---
title: Use Intention-Revealing Names
impact: CRITICAL
impactDescription: eliminates mental mapping overhead
tags: name, intention, readability, clarity
---

## Use Intention-Revealing Names

Names should reveal intent. A name should tell you why something exists, what it does, and how it is used. If a name requires a comment, it does not reveal its intent.

**When short names are acceptable:**
- Loop counters (`i`, `j`, `k`) in small, tightly-scoped loops where the index has no domain meaning.
- Mathematical algorithms where `x`, `y`, `dx`, `dt` are conventional and understood by the target audience.
- Short parameters in a tiny predicate can be clear: `[](int x) { return x > 0; }`. Use a domain name when its meaning is not otherwise evident.

Reference: [Clean Code, Chapter 2: Meaningful Names](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [name-intention-revealing](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/name-intention-revealing.md).
