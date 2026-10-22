---
title: Source Dependencies Point Inward Only
impact: CRITICAL
impactDescription: prevents cascade failures across all layers
tags: dep, dependency-rule, layers, architecture
---

## Source Dependencies Point Inward Only

Source dependencies point toward policy. A domain operation changes domain state; an application use case coordinates storage through a contract it owns.

Saving can fail after an in-memory change. Define the required state/transaction guarantee separately. Dependency direction does not establish atomicity.

Reference: [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [dep-inward-only](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/dep-inward-only.md).
