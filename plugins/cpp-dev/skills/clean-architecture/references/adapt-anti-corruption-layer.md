---
title: Build Anti-Corruption Layers for External Systems
impact: MEDIUM
impactDescription: protects domain from external model pollution
tags: adapt, anti-corruption, external, isolation
---

## Build Anti-Corruption Layers for External Systems

Translate a vendor model into application concepts at the integration boundary. Reject unsupported values explicitly rather than scattering vendor status codes through domain code.

**Incorrect:**

```cpp
#include <string_view>
namespace vendor { struct Payment { std::string_view status; }; }
bool can_ship(const vendor::Payment& payment) { return payment.status == "SETTLED_V2"; }
```

**Better for this contract:**

```cpp
#include <string_view>
#include <stdexcept>
enum class PaymentState { pending, settled };
namespace vendor { struct Payment { std::string_view status; }; }
PaymentState translate(const vendor::Payment& payment) {
    if (payment.status == "SETTLED_V2") return PaymentState::settled;
    if (payment.status == "WAITING") return PaymentState::pending;
    throw std::invalid_argument("unsupported vendor payment state");
}
bool can_ship(PaymentState payment) { return payment == PaymentState::settled; }
```

The vendor is fictional. Verify its real status semantics and schema with contract/integration tests; do not silently assume future statuses mean failure or success.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Anti-Corruption Layer Pattern](https://docs.microsoft.com/en-us/azure/architecture/patterns/anti-corruption-layer)

Upstream rule: [adapt-anti-corruption-layer](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/adapt-anti-corruption-layer.md).
