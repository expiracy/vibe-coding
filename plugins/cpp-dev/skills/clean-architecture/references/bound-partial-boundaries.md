---
title: Use Partial Boundaries When Full Separation is Premature
impact: MEDIUM-HIGH
impactDescription: prepares for future without over-engineering now
tags: bound, partial-boundaries, pragmatism, yagni
---

## Use Partial Boundaries When Full Separation is Premature

Where change pressure is real but a full component split is premature, start with a small contract in the current binary. Avoid speculative service boundaries and interface forests.

A direct function, template or callable may be enough. Do not type-erase every operation; preserve the existing contract and performance requirements.

Reference: [Clean Architecture - Partial Boundaries](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch24.xhtml)

Upstream rule: [bound-partial-boundaries](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/bound-partial-boundaries.md).
