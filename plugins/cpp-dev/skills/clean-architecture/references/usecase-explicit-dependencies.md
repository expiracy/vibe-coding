---
title: Declare All Dependencies Explicitly in Constructor
impact: HIGH
impactDescription: enables testing, documents requirements, prevents hidden coupling
tags: usecase, dependencies, constructor, injection
---

## Declare All Dependencies Explicitly in Constructor

Make external behavior explicit through construction or function parameters. Avoid hidden mutable global services; pure deterministic functions and ordinary value construction need no injection seam.

Make dependency lifetimes explicit as well as their presence. Ownership and lifetime policy belong to cpp-guidelines; this rule makes coupling visible.

Reference: [Dependency Injection Principles](https://martinfowler.com/articles/injection.html)

Upstream rule: [usecase-explicit-dependencies](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/usecase-explicit-dependencies.md).
