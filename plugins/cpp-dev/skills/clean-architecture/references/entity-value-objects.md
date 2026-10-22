---
title: Use Value Objects for Domain Concepts
impact: HIGH
impactDescription: eliminates primitive obsession, enforces constraints
tags: entity, value-objects, domain, types
---

## Use Value Objects for Domain Concepts

Give domain values distinct types when confusing them would violate a real contract. Validate construction and offer value semantics; avoid wrappers for every primitive without a reason.

A valid value object does not establish authorization or every external identity constraint. Validate those requirements at their actual boundaries.

Reference: [Value Object Pattern](https://martinfowler.com/bliki/ValueObject.html)

Upstream rule: [entity-value-objects](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/entity-value-objects.md).
