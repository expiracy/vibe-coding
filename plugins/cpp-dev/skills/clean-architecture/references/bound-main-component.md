---
title: Treat Main as a Plugin to the Application
impact: MEDIUM-HIGH
impactDescription: enables multiple configurations, simplifies testing
tags: bound, main, composition-root, plugin
---

## Treat Main as a Plugin to the Application

Keep concrete wiring at startup or another outer composition point. The reusable application does not locate infrastructure through main, globals or a container.

**Incorrect:**

```cpp
struct SqlOrders { void save(int); };
void place_order(int id) { SqlOrders orders; orders.save(id); }
```

**Better for this contract:**

```cpp
struct Orders { virtual ~Orders() = default; virtual void save(int) = 0; };
void place_order(Orders& orders, int id) { orders.save(id); }
struct SqlOrders final : Orders { void save(int) override {} };
int main() { SqlOrders orders; place_order(orders, 7); }
```

The stub adapter only illustrates wiring. Production startup must handle configuration, dependency lifetimes and startup/shutdown failures.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - The Main Component](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch26.xhtml)

Upstream rule: [bound-main-component](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/bound-main-component.md).
