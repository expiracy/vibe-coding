---
title: Eliminate Cyclic Dependencies Between Components
impact: CRITICAL
impactDescription: prevents ripple effects, enables independent deployment
tags: dep, cycles, acyclic, components
---

## Eliminate Cyclic Dependencies Between Components

Keep the component dependency graph acyclic. Include guards stop repeated inclusion; they do not remove a component cycle. Break a cycle through consumer-owned contracts or a genuinely shared policy component.

```text
orders -> domain_events <- notifications
composition -> orders + notifications
```

Inspect both include dependencies and CMake target links. Runtime callbacks do not require reverse source dependencies.

Reference: [Clean Architecture - Acyclic Dependencies Principle](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch14.xhtml)

Upstream rule: [dep-acyclic-dependencies](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/dep-acyclic-dependencies.md).
