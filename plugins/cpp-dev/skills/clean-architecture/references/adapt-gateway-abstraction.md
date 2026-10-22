---
title: Gateways Hide External System Details
impact: MEDIUM
impactDescription: enables vendor switching, simplifies testing
tags: adapt, gateway, external, abstraction
---

## Gateways Hide External System Details

Expose the external capability the application actually needs through its own contract. Keep vendor request types and protocol details in the adapter.

**Incorrect:**

```cpp
#include <string_view>
namespace vendor { struct RefundRequest { std::string_view charge; }; bool refund(RefundRequest); }
bool refund_order(std::string_view id) { return vendor::refund({id}); }
```

**Better for this contract:**

```cpp
#include <string_view>
struct Refunds {
    virtual ~Refunds() = default;
    virtual bool request(std::string_view payment_id, std::string_view operation_id) = 0;
};
bool refund_order(Refunds& refunds, std::string_view payment, std::string_view operation) {
    return refunds.request(payment, operation);
}
```

The bool result is deliberately limited illustration. A real gateway may need accepted, rejected and uncertain outcomes. Remote refunds and local saves are not atomic; define idempotency, retention and recovery explicitly.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Database Gateways](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch22.xhtml)

Upstream rule: [adapt-gateway-abstraction](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/adapt-gateway-abstraction.md).
