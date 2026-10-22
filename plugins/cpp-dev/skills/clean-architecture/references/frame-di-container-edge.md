---
title: Dependency Injection Containers Live at the Edge
impact: MEDIUM
impactDescription: prevents DI container coupling throughout codebase
tags: frame, dependency-injection, container, composition
---

## Dependency Injection Containers Live at the Edge

Use a DI container, if one exists, only at composition. Explicit function or constructor parameters expose dependencies without a service locator inside policy code.

Ordinary C++ construction is often sufficient. Do not introduce a DI framework or an abstract interface solely for wiring.

Reference: [Composition Root Pattern](https://blog.ploeh.dk/2011/07/28/CompositionRoot/)

Upstream rule: [frame-di-container-edge](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/frame-di-container-edge.md).
