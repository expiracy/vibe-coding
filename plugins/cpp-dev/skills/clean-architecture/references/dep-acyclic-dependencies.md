---
title: Eliminate Cyclic Dependencies Between Components
impact: CRITICAL
impactDescription: prevents ripple effects, enables independent deployment
tags: dep, cycles, acyclic, components
---

## Eliminate Cyclic Dependencies Between Components

Keep the component dependency graph acyclic. Include guards stop repeated inclusion; they do not remove a component cycle. Break a cycle through consumer-owned contracts or a genuinely shared policy component.

**Incorrect:**

```text
orders -> notifications -> orders
// orders/order.hpp includes notifications/email.hpp
// notifications/email.hpp includes orders/service.hpp
```

**Better for this contract:**

```text
orders -> domain_events <- notifications
// domain_events/order_placed.hpp owns the event data.
// An outer composition point connects publication and handling.
// Neither component includes the other's implementation header.
```

Inspect both include dependencies and CMake target links. Runtime callbacks do not require reverse source dependencies.

The component/build layout is illustrative; use the project conventions and actual dependency graph.

Reference: [Clean Architecture - Acyclic Dependencies Principle](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch14.xhtml)

Upstream rule: [dep-acyclic-dependencies](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/dep-acyclic-dependencies.md).
