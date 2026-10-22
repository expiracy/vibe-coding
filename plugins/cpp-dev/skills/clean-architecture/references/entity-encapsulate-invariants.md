---
title: Encapsulate Business Invariants Within Entities
impact: CRITICAL
impactDescription: prevents invalid state, centralizes validation
tags: entity, invariants, validation, encapsulation
---

## Encapsulate Business Invariants Within Entities

Protect meaningful invariants at the domain operation that can violate them. Preserve the project error policy.

Check the complete valid input/state range for each transition. Currency, overdraft and concurrency guarantees need explicit contracts; encapsulation alone does not supply them.

Reference: [Domain-Driven Design - Aggregates](https://martinfowler.com/bliki/DDD_Aggregate.html)

Upstream rule: [entity-encapsulate-invariants](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/entity-encapsulate-invariants.md).
