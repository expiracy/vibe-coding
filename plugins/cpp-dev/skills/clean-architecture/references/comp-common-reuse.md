---
title: Avoid Forcing Clients to Depend on Unused Code
impact: HIGH
impactDescription: reduces unnecessary recompilation and deployment
tags: comp, common-reuse, dependencies, coupling
---

## Avoid Forcing Clients to Depend on Unused Code

A client should not need a heavy dependency for an unrelated utility. Split interfaces/targets where actual usage differs, rather than making every caller depend on an omnibus header or library.

Removing a heavy include does not necessarily remove its target dependency. Check target/public link requirements as well as includes.

Reference: [Clean Architecture - Common Reuse Principle](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch13.xhtml)

Upstream rule: [comp-common-reuse](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/comp-common-reuse.md).
