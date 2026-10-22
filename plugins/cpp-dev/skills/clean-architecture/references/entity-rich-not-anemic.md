---
title: Build Rich Domain Models Not Anemic Data Structures
impact: HIGH
impactDescription: centralizes business logic, prevents scattered rules
tags: entity, domain-model, anemic, behavior
---

## Build Rich Domain Models Not Anemic Data Structures

Keep a state transition and its reusable validation together. Domain functions can provide the same cohesion as member functions; rich models do not require an object hierarchy.

Plain request/response records and independent data remain aggregates. Do not manufacture behavior for transfer objects.

Reference: [Anemic Domain Model Anti-pattern](https://martinfowler.com/bliki/AnemicDomainModel.html)

Upstream rule: [entity-rich-not-anemic](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/entity-rich-not-anemic.md).
