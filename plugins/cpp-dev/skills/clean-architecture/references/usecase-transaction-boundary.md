---
title: Use Case Defines the Transaction Boundary
impact: HIGH
impactDescription: ensures data consistency, prevents partial updates
tags: usecase, transactions, consistency, boundaries
---

## Use Case Defines the Transaction Boundary

The use case defines its consistency requirement. Infrastructure implements the actual local transaction. A local rollback cannot undo a remote payment or email.

**Incorrect:**

```cpp
struct Orders { void save_pending(int); };
struct Payments { void charge(int); };
void place(Orders& orders, Payments& payments, int id) {
    orders.save_pending(id); // Already committed if charge fails.
    payments.charge(id);
}
```

**Better for this contract:**

```cpp
#include <string_view>
struct PendingOrders {
    virtual ~PendingOrders() = default;
    // Contract: one local transaction commits BOTH records or neither.
    virtual void save_order_and_payment_outbox(int order_id, std::string_view operation_id) = 0;
};
void place(PendingOrders& orders, int id, std::string_view operation_id) {
    orders.save_order_and_payment_outbox(id, operation_id);
}
```

The outbox is one option when asynchronous payment fits the product. The adapter must really commit both records together; an interface name proves nothing. The worker needs durable identity, idempotency and uncertain-outcome recovery. Test real transaction rollback, restart and delivery behavior; compensation can fail too.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Unit of Work Pattern](https://martinfowler.com/eaaCatalog/unitOfWork.html)

Upstream rule: [usecase-transaction-boundary](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/usecase-transaction-boundary.md).
