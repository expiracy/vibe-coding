---
title: Use Value Objects for Domain Concepts
impact: HIGH
impactDescription: eliminates primitive obsession, enforces constraints
tags: entity, value-objects, domain, types
---

## Use Value Objects for Domain Concepts

Give domain values distinct types when confusing them would violate a real contract. Validate construction and offer value semantics; avoid wrappers for every primitive without a reason.

**Incorrect:**

```cpp
#include <string>
void send_receipt(const std::string& customer_id, const std::string& order_id);
void swapped() { send_receipt("order-1", "customer-1"); }
```

**Better for this contract:**

```cpp
#include <string>
#include <stdexcept>
#include <utility>
class CustomerId {
    std::string value_;
public:
    explicit CustomerId(std::string value) : value_(std::move(value)) {
        if (value_.empty()) throw std::invalid_argument("empty customer id");
    }
    const std::string& value() const { return value_; }
    bool operator==(const CustomerId&) const = default;
};
struct OrderId { std::string value; };
void send_receipt(const CustomerId&, const OrderId&);
```

An empty-id check is only the illustrated invariant. External identity syntax and authorization still need validation at their actual boundaries.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Value Object Pattern](https://martinfowler.com/bliki/ValueObject.html)

Upstream rule: [entity-value-objects](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/entity-value-objects.md).
