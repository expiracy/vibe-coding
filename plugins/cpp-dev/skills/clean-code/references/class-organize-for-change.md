---
title: "Organize Around Real Reasons for Change"
impact: MEDIUM
impactDescription: "Protect stable application policy from details that actually vary"
tags: clean-code, class
---

## Organize Around Real Reasons for Change

Protect stable application policy from details that actually vary. An extension point is useful when it accommodates an existing or concrete expected variation.

For a small, closed set of alternatives, explicit cases can be clearer than an extensible hierarchy. Do not add speculative abstraction merely to satisfy the Open-Closed Principle; preserve and check current behavior when reorganizing code.

Reference: [Clean Code, Chapter 10: Classes](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
