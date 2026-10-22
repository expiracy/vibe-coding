---
title: Avoid Hybrid Data-Object Structures
impact: MEDIUM-HIGH
impactDescription: prevents worst-of-both-worlds maintenance burden
tags: obj, hybrid, structure, design
---

## Avoid Hybrid Data-Object Structures

Hybrids are half object, half data structure. They have functions that do significant things, AND they have public variables or accessors that expose internal structure. Avoid creating these monstrosities.

Hybrids make it hard to add new functions AND hard to add new data structures.

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [obj-avoid-hybrids](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/obj-avoid-hybrids.md).
