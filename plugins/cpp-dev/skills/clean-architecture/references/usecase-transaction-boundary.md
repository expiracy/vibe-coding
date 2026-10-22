---
title: Use Case Defines the Transaction Boundary
impact: HIGH
impactDescription: ensures data consistency, prevents partial updates
tags: usecase, transactions, consistency, boundaries
---

## Use Case Defines the Transaction Boundary

The use case defines its consistency requirement. Infrastructure implements the actual local transaction. A local rollback cannot undo a remote payment or email.

The outbox is one option when asynchronous payment fits the product. Commit the business change and its outbox record in one actual local transaction. The worker needs durable identity, idempotency and uncertain-outcome recovery. Test real transaction rollback, restart and delivery behavior; compensation can fail too.

Reference: [Unit of Work Pattern](https://martinfowler.com/eaaCatalog/unitOfWork.html)

Upstream rule: [usecase-transaction-boundary](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/usecase-transaction-boundary.md).
