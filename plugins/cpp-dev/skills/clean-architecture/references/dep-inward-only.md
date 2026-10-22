---
title: Source Dependencies Point Inward Only
impact: CRITICAL
impactDescription: prevents cascade failures across all layers
tags: dep, dependency-rule, layers, architecture
---

## Source Dependencies Point Inward Only

Source dependencies point toward policy. A domain operation changes domain state; an application use case coordinates storage through a contract it owns.

**Incorrect:**

```cpp
namespace infrastructure { void save_paid_order(int); }
namespace domain {
struct Order {
    int id;
    void mark_paid() { infrastructure::save_paid_order(id); }
};
}
```

**Better for this contract:**

```cpp
namespace domain { struct Order { int id; bool paid{}; void mark_paid() { paid = true; } }; }
namespace application {
struct Orders { virtual ~Orders() = default; virtual void save(const domain::Order&) = 0; };
void mark_paid(domain::Order& order, Orders& orders) {
    order.mark_paid();
    orders.save(order);
}
}
```

Saving can fail after an in-memory change. Define the required state/transaction guarantee separately; this example shows dependency direction, not atomicity.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [dep-inward-only](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/dep-inward-only.md).
