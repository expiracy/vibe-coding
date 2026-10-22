---
title: Use Cases Own Application Rules and Orchestrate Entities
impact: HIGH
impactDescription: prevents rule duplication, maintains single source of truth
tags: usecase, orchestration, entities, delegation
---

## Use Cases Own Application Rules and Orchestrate Entities

Entities/domain functions own reusable rules; use cases own application-specific decisions and sequence the workflow. Do not move every business decision into the entity.

Keep channel-specific authorization and workflow decisions with the application. Persistence and remote effects need explicit failure semantics.

Reference: [Clean Architecture - Use Cases](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [usecase-orchestrates-not-implements](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/usecase-orchestrates-not-implements.md).
