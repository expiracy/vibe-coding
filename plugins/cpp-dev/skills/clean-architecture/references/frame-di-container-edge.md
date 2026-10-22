---
title: Dependency Injection Containers Live at the Edge
impact: MEDIUM
impactDescription: prevents DI container coupling throughout codebase
tags: frame, dependency-injection, container, composition
---

## Dependency Injection Containers Live at the Edge

Use a DI container, if one exists, only at composition. Explicit function or constructor parameters expose dependencies without a service locator inside policy code.

**Incorrect:**

```cpp
struct Orders { void save(int); };
namespace container { Orders& resolve_orders(); }
void place(int id) { container::resolve_orders().save(id); }
```

**Better for this contract:**

```cpp
struct Orders { void save(int); };
void place(Orders& orders, int id) { orders.save(id); }
namespace container { Orders& resolve_orders(); }
void start() { place(container::resolve_orders(), 7); }
```

Ordinary C++ construction is often sufficient. Do not introduce a DI framework or an abstract interface solely for wiring.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Composition Root Pattern](https://blog.ploeh.dk/2011/07/28/CompositionRoot/)

Upstream rule: [frame-di-container-edge](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/frame-di-container-edge.md).
