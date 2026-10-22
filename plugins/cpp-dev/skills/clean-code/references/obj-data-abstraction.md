---
title: Hide Data Behind Abstractions
impact: MEDIUM-HIGH
impactDescription: enables implementation changes without ripple effects
tags: obj, abstraction, encapsulation, data-hiding
---

## Hide Data Behind Abstractions

Objects hide their data behind abstractions and expose functions that operate on that data. Data structures expose their data and have no meaningful functions. Do not mix these concepts.

**Key insight:** The abstraction is not just about using getters/setters. It is about hiding the form of the data and exposing operations that work with the abstract concept. A clear value and mutability contract can simplify reasoning. A factory or the absence of setters does not by itself guarantee correct behavior or thread safety.

Reference: [Clean Code, Chapter 6: Objects and Data Structures](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [obj-data-abstraction](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/obj-data-abstraction.md).
