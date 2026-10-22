---
title: Use Simple Data Structures Across Boundaries
impact: CRITICAL
impactDescription: prevents coupling between layers
tags: dep, boundaries, dto, data-transfer
---

## Use Simple Data Structures Across Boundaries

Choose boundary data for the receiving contract. Do not leak database rows, lazy-loading sessions or transport objects into a use case. An entity can cross an internal boundary when its meaning and dependency direction genuinely fit.

Use separate representations where meanings, security requirements or change reasons differ. Avoid redundant copies for every function call. Test the actual serializer for disclosure claims.

Reference: [Clean Architecture - Crossing Boundaries](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [dep-data-crossing-boundaries](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/dep-data-crossing-boundaries.md).
