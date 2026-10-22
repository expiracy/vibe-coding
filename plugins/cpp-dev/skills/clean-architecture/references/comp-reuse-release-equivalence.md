---
title: Release Components as Cohesive Units
impact: HIGH
impactDescription: enables version tracking, supports parallel team development
tags: comp, release, versioning, cohesion
---

## Release Components as Cohesive Units

A reusable component should have a coherent public contract and release/versioning policy. Keep headers and binaries compatible as required by the project; do not create packages for every internal namespace.

**Incorrect:**

```text
misc-sdk/
  invoice.hpp
  experimental_image_codec.hpp
  internal_database_migrations.hpp
# Consumers must take one release for unrelated capabilities.
```

**Better for this contract:**

```text
billing-sdk/
  include/billing/invoice.hpp
  src/invoice.cpp
  tests/
  CMakeLists.txt
  CHANGELOG.md
# Public headers and binary are released/tested as one contract.
```

Use the project package manager and versioning convention. Header-only distribution also has source compatibility and dependency costs.

The component/build layout is illustrative; use the project conventions and actual dependency graph.

Reference: [Clean Architecture - Reuse/Release Equivalence Principle](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch13.xhtml)

Upstream rule: [comp-reuse-release-equivalence](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/comp-reuse-release-equivalence.md).
