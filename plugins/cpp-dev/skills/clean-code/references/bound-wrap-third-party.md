---
title: "Translate Dependencies at Useful Boundaries"
impact: HIGH
impactDescription: "Introduce a small boundary when it translates dependency-specific concepts, units, or failures into the application's contract"
tags: clean-code, bound
---

## Translate Dependencies at Useful Boundaries

Introduce a small boundary when it translates dependency-specific concepts, units, or failures into the application's contract. Keep vendor details out of callers that should not need to understand them.

A pass-through wrapper around an already suitable API adds little value. Adapt the actual dependency and preserve useful failure information; do not create an interface merely to demonstrate a pattern.

Reference: [Clean Code, Chapter 8: Boundaries](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)
