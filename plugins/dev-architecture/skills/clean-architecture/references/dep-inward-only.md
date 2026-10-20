---
title: Source Dependencies Point Inward Only
impact: CRITICAL
impactDescription: prevents cascade failures across all layers
tags: dep, dependency-rule, layers, architecture
---

## Source Dependencies Point Inward Only

The Dependency Rule states that source code dependencies can only point inward toward higher-level policies. Inner circles must never reference outer circles.

**Incorrect (inner layer imports from outer layer):**

```typescript
// domain/entities/Order.ts - ENTITY LAYER
import { OrderRepository } from '../../infrastructure/OrderRepository'
import { EmailService } from '../../infrastructure/EmailService'

export class Order {
  constructor(
    private repo: OrderRepository,  // Changes to repo implementation break Order
    private email: EmailService
  ) {}

  async complete() {
    await this.repo.save(this)
    await this.email.notify(this.customerId)  // Cannot test without email server
  }
}
```

**Correct (inner layer defines interface, outer layer implements):**

```typescript
// domain/entities/Order.ts - ENTITY LAYER
export class Order {
  private completed = false
  complete() { this.completed = true }
}

// application/CompleteOrder.ts - APPLICATION LAYER
import { Order } from '../domain/entities/Order'
export interface OrderPersistence {
  save(order: Order): Promise<void>
}
export class CompleteOrder {
  constructor(private orders: OrderPersistence) {}
  async execute(order: Order): Promise<void> {
    order.complete()
    await this.orders.save(order)
  }
}

// infrastructure/OrderRepository.ts - OUTER ADAPTER
import { Order } from '../domain/entities/Order'
import { OrderPersistence } from '../application/CompleteOrder'
export class OrderRepository implements OrderPersistence {
  async save(order: Order): Promise<void> { /* project persistence implementation */ }
}
```

The entity expresses its state change without knowing how to save or notify.
The use case owns persistence orchestration. This excerpt demonstrates dependency
direction; storage failure semantics and external notifications need their own
contracts.

**Benefits:**
- Inner layers remain stable when outer layers change
- Business rules can be tested without infrastructure
- Infrastructure can be swapped without touching domain code

Reference: [The Clean Architecture](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [dep-inward-only](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/dep-inward-only.md).
