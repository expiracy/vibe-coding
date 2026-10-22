---
title: Entities Contain Only Enterprise Business Rules
impact: CRITICAL
impactDescription: enables reuse across applications, prevents coupling
tags: entity, business-rules, domain, purity
---

## Entities Contain Only Enterprise Business Rules

Keep reusable domain rules independent of email, storage and delivery. Application-specific authorization and orchestration belong in the use case.

**Incorrect:**

```cpp
namespace mail { void send_order_paid(int); }
struct Order { int id; bool paid{}; void pay() { paid = true; mail::send_order_paid(id); } };
```

**Better for this contract:**

```cpp
struct Order { int id; bool paid{}; void pay() { paid = true; } };
struct Notifications { virtual ~Notifications() = default; virtual void paid(int id) = 0; };
void pay_order(Order& order, Notifications& notifications) {
    order.pay();
    notifications.paid(order.id);
}
```

Notification failure does not undo payment or domain state. Production orchestration needs an explicit consistency/recovery contract.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Entities](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [entity-pure-business-rules](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/entity-pure-business-rules.md).
