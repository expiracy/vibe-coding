---
title: Build Rich Domain Models Not Anemic Data Structures
impact: HIGH
impactDescription: centralizes business logic, prevents scattered rules
tags: entity, domain-model, anemic, behavior
---

## Build Rich Domain Models Not Anemic Data Structures

Keep a state transition and its reusable validation together. Domain functions can provide the same cohesion as member functions; rich models do not require an object hierarchy.

**Incorrect:**

```cpp
struct Order { bool paid; bool shipped; };
void ship(Order& order) { order.shipped = true; }
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
```

Plain request/response records and independent data remain aggregates. Do not manufacture behavior for transfer objects.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Anemic Domain Model Anti-pattern](https://martinfowler.com/bliki/AnemicDomainModel.html)

Upstream rule: [entity-rich-not-anemic](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/entity-rich-not-anemic.md).
