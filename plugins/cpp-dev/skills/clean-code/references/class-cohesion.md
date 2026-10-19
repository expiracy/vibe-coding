---
title: "Keep Classes Cohesive"
impact: MEDIUM
impactDescription: "Group state and operations around one concept or invariant"
tags: clean-code, class
---

## Keep Classes Cohesive

Group state and operations around one concept or invariant. Accessing the same fields is not sufficient evidence of cohesion if the methods serve unrelated responsibilities.

Extract an independent concept when one is present, but do not require every method to touch every field. Avoid duplicating state that the existing abstraction already represents.

Reference: [Clean Code, Chapter 10: Classes](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
