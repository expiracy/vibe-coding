---
title: Understand Data/Object Anti-Symmetry
impact: MEDIUM-HIGH
impactDescription: clarifies data and behavior boundaries
tags: obj, asymmetry, procedural, polymorphism
---

## Understand Data/Object Anti-Symmetry

Objects and data structures are opposites. Objects hide data and expose behavior; data structures expose data and have no behavior. Choose based on what kind of changes you anticipate.

**Choose based on anticipated changes:**
- Adding new functions often? Use data structures (procedural)
- Adding new types often? Use objects (polymorphic)

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [obj-data-object-asymmetry](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/obj-data-object-asymmetry.md).
