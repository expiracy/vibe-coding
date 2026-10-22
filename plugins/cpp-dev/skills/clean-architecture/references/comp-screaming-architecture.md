---
title: Structure Should Scream the Domain Not the Framework
impact: HIGH
impactDescription: enables understanding at a glance, reveals intent
tags: comp, screaming-architecture, structure, domain
---

## Structure Should Scream the Domain Not the Framework

Make business capabilities visible in component names. Preserve existing conventions unless a concrete change justifies a move; folders alone do not enforce architecture.

**Incorrect:**

```text
src/
  managers/
    manager.hpp
  helpers/
    helper.hpp
  services/
    service.hpp
```

**Better for this contract:**

```text
src/
  orders/
    domain/order.hpp
    application/place_order.hpp
    adapters/sql_orders.cpp
  shipping/
    application/dispatch_order.hpp
```

The tree is illustrative. A small C++ library may need fewer directories, and source layout need not match deployment units.

The component/build layout is illustrative; use the project conventions and actual dependency graph.

Reference: [Screaming Architecture](https://blog.cleancoder.com/uncle-bob/2011/09/30/Screaming-Architecture.html)

Upstream rule: [comp-screaming-architecture](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/comp-screaming-architecture.md).
