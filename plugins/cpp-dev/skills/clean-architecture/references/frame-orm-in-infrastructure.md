---
title: Keep ORM Usage in Infrastructure Layer
impact: MEDIUM
impactDescription: isolates persistence complexity, enables ORM switching
tags: frame, orm, infrastructure, persistence
---

## Keep ORM Usage in Infrastructure Layer

Keep ORM queries, sessions and persistence mappings in the storage adapter. The application names the data capability it needs without accepting an ORM session.

Test actual mappings, nullability, transaction scope and connection behavior against the chosen storage implementation.

Reference: [Repository Pattern](https://martinfowler.com/eaaCatalog/repository.html)

Upstream rule: [frame-orm-in-infrastructure](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/frame-orm-in-infrastructure.md).
