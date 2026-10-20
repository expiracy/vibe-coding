---
title: Follow Team Formatting Rules
impact: HIGH
impactDescription: eliminates style-related code review friction
tags: fmt, team, consistency, standards
---

## Follow Team Formatting Rules

A team of developers should agree upon a single formatting style. Every member should use that style. The goal is to make the software have a consistent style, as if written by one person.

**Incorrect (inconsistent styles mixed):**

```cpp

namespace example {
struct Task { bool valid{}; bool processed{}; };


void processOrder(Task& order){if(order.valid){order.processed=true;}}
void processPayment( Task& payment )
{
  if ( payment.valid ) { payment.processed = true; }
}
void processShipment(Task& shipment) {
 if(shipment.valid) { shipment.processed=true; }}
}
```

**Correct (consistent team style):**

```cpp

namespace example {
struct Task { bool valid{}; bool processed{}; };


void processOrder(Task& order) {
    if (order.valid) {
        order.processed = true;
    }
}
void processPayment(Task& payment) {
    if (payment.valid) {
        payment.processed = true;
    }
}
void processShipment(Task& shipment) {
    if (shipment.valid) {
        shipment.processed = true;
    }
}
}
```

**Implementation:**
- Document the team's coding standards
- Use the project's configured formatter
- Enforce in CI/CD pipelines
- Configure IDE to format on save

Your personal style preferences are less important than team consistency.

Reference: [Clean Code, Chapter 5: Formatting](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [fmt-team-rules](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/fmt-team-rules.md).
