---
title: "Size Classes by Responsibility"
impact: MEDIUM
impactDescription: "Measure a class by the independent requirements that could make it change, rather than a fixed line count"
tags: clean-code, class
---

## Size Classes by Responsibility

Measure a class by the independent requirements that could make it change, rather than a fixed line count. Separate unrelated responsibilities when this makes the current design easier to understand.

A small responsibility does not automatically need its own class. Keep closely related behavior together when splitting it would add indirection without improving the design.

Reference: [Clean Code, Chapter 10: Classes](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
