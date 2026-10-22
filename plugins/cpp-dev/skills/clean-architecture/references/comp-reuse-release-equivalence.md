---
title: Release Components as Cohesive Units
impact: HIGH
impactDescription: enables version tracking, supports parallel team development
tags: comp, release, versioning, cohesion
---

## Release Components as Cohesive Units

A reusable component should have a coherent public contract and release/versioning policy. Keep headers and binaries compatible as required by the project; do not create packages for every internal namespace.

Use the project package manager and versioning convention. Header-only distribution also has source compatibility and dependency costs.

Reference: [Clean Architecture - Reuse/Release Equivalence Principle](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch13.xhtml)

Upstream rule: [comp-reuse-release-equivalence](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/comp-reuse-release-equivalence.md).
