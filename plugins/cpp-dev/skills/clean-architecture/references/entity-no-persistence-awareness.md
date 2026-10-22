---
title: Entities Must Not Know How They Are Persisted
impact: CRITICAL
impactDescription: enables database migration without domain changes
tags: entity, persistence, database, ignorance
---

## Entities Must Not Know How They Are Persisted

A domain entity expresses its behavior without knowing SQL, ORM mappings or connection/session types. Infrastructure translates storage data into domain values.

A simple aggregate is appropriate when no invariant needs protection. Storage constraints still require integration checks at the adapter.

Reference: [Clean Architecture - Database is a Detail](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch30.xhtml)

Upstream rule: [entity-no-persistence-awareness](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/entity-no-persistence-awareness.md).
