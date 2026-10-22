---
title: Depend in the Direction of Stability
impact: HIGH
impactDescription: prevents unstable components from destabilizing dependents
tags: comp, stability, dependencies, direction
---

## Depend in the Direction of Stability

Protect widely depended-on policy from volatile adapters. Fan-in/fan-out can reveal expensive coupling; metrics are evidence to inspect, not numerical design quotas.

The upstream instability measure is outgoing/(incoming + outgoing), undefined when both are zero. Dependency counts alone do not measure semantic stability or require extra interfaces.

Reference: [Clean Architecture - Stable Dependencies Principle](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch14.xhtml)

Upstream rule: [comp-stable-dependencies](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/comp-stable-dependencies.md).
