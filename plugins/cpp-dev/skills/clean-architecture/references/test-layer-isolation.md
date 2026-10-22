---
title: Test Each Layer in Isolation
impact: LOW-MEDIUM
impactDescription: fast feedback, precise failure location
tags: test, isolation, layers, unit
---

## Test Each Layer in Isolation

Test domain invariants directly and use case decisions through application contracts. Add real adapter and composition tests for behavior those direct checks cannot establish.

A test pyramid is a planning heuristic, not fixed percentages. A fake store cannot prove database mappings, durability or transaction atomicity.

Reference: [The Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)

Upstream rule: [test-layer-isolation](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/test-layer-isolation.md).
