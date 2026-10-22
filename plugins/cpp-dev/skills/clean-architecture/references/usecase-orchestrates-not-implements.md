---
title: Use Cases Own Application Rules and Orchestrate Entities
impact: HIGH
impactDescription: prevents rule duplication, maintains single source of truth
tags: usecase, orchestration, entities, delegation
---

## Use Cases Own Application Rules and Orchestrate Entities

Entities/domain functions own reusable rules; use cases own application-specific decisions and sequence the workflow. Do not move every business decision into the entity.

**Incorrect:**

```cpp
#include <stdexcept>
struct Order { bool paid; bool shipped; };
void ship_online(Order& order) {
    if (!order.paid) throw std::logic_error("payment required");
    order.shipped = true;
}
```

**Better for this contract:**

```cpp
#include <stdexcept>
class Order {
    bool paid_{};
    bool shipped_{};
public:
    void record_payment() { paid_ = true; }
    void ship() {
        if (!paid_) throw std::logic_error("payment required");
        shipped_ = true;
    }
    bool shipped() const { return shipped_; }
};
void ship_online(Order& order, bool verified_customer) {
    if (!verified_customer) throw std::runtime_error("online channel requires verification");
    order.ship();
}
```

Customer verification is the illustrated channel policy, not a universal shipping rule. Persistence and remote shipment need separate failure semantics.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Use Cases](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [usecase-orchestrates-not-implements](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/usecase-orchestrates-not-implements.md).
