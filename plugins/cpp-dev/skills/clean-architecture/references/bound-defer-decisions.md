---
title: Defer Framework and Database Decisions
impact: MEDIUM-HIGH
impactDescription: preserves optionality, reduces early commitment risk
tags: bound, deferral, decisions, optionality
---

## Defer Framework and Database Decisions

Defer expensive vendor decisions only while doing so reduces uncertainty. A small in-memory implementation can exercise the application contract before the persistence choice is known.

An in-memory prototype does not establish durability, concurrency, query performance or transaction semantics. Investigate those early when they drive the architectural choice.

Reference: [Clean Architecture - The Database is a Detail](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch30.xhtml)

Upstream rule: [bound-defer-decisions](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/bound-defer-decisions.md).
