---
title: Use Case Defines the Transaction Boundary
impact: HIGH
impactDescription: ensures data consistency, prevents partial updates
tags: usecase, transactions, consistency, boundaries
---

## Use Case Defines the Transaction Boundary

A use case defines the consistency it needs. Operations in one local transactional store can share a unit of work; the infrastructure implements that transaction. External payment, email and remote-service effects are not rolled back by a database transaction. Choose the actual consistency and failure contract before writing the workflow.

**Incorrect (transaction managed inside repository):**

```python
class OrderRepository:
    def save(self, order):
        with self.db.transaction():  # Transaction per operation
            self.db.insert('orders', order)

class InventoryRepository:
    def reserve(self, items):
        with self.db.transaction():  # Separate transaction
            for item in items:
                self.db.update('inventory', item.sku, decrement=item.qty)

class PlaceOrderUseCase:
    def execute(self, command):
        order = Order.create(command.items)
        self.orders.save(order)  # Commits
        self.inventory.reserve(command.items)  # If this fails, order is orphaned!
        self.payments.charge(order.total)  # If this fails, inventory is reserved but unpaid
```

**Correct (local transaction records the order and a payment request):**

```python
# Application-facing ports describe a local unit of work and its repositories.
# Infrastructure must bind orders and outbox to the SAME database transaction.
class PlaceOrderUseCase:
    def __init__(self, uow, orders, outbox):
        self.uow = uow
        self.orders = orders
        self.outbox = outbox

    def execute(self, command):
        with self.uow:  # Commit on successful exit; rollback on failure.
            order = Order.create_pending_payment(command.items)
            self.orders.save(order)
            self.outbox.add(PaymentRequested(
                order_id=order.id,
                amount=order.total,
                idempotency_key=order.payment_request_id,
            ))
        return order.id  # Accepted/pending, not a claim that payment succeeded.

# A separate worker delivers committed outbox messages to the payment provider.
# Use stable idempotency keys, record outcomes and reconcile uncertain results.
# Inventory or other remote effects need an explicit reservation/saga contract.
```

**Failure contract:** The local transaction commits the pending order and outbox message together. Delivery can be retried; a durable idempotency/reconciliation contract is still required for the remote effect. Test the real database/outbox atomicity and worker recovery. An in-memory test double does not prove these properties. Use compensation or an explicit saga where multiple services must coordinate; a compensation can fail too.

Reference: [Unit of Work Pattern](https://martinfowler.com/eaaCatalog/unitOfWork.html)

Upstream rule: [usecase-transaction-boundary](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/usecase-transaction-boundary.md).
