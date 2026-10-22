---
title: Avoid Framework Imports in Inner Layers
impact: CRITICAL
impactDescription: makes policy boundaries and dependency tradeoffs clearer
tags: dep, frameworks, imports, isolation
---

## Avoid Framework Imports in Inner Layers

Keep HTTP, GUI and persistence framework types outside policy headers. Use standard or domain types for the application contract and translate in the adapter.

**Incorrect:**

```cpp
namespace web { struct Request { int quantity; }; }
namespace application { bool can_order(const web::Request& request) { return request.quantity > 0; } }
```

**Better for this contract:**

```cpp
namespace application {
struct OrderRequest { int quantity; };
bool can_order(const OrderRequest& request) { return request.quantity > 0; }
}
namespace web {
struct Request { int quantity; };
bool handle(const Request& request) { return application::can_order({request.quantity}); }
}
```

Isolate libraries that impose delivery or infrastructure policy. Stable domain-supporting libraries do not require wrappers solely because they are libraries.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Frameworks are Details](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [dep-no-framework-imports](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/dep-no-framework-imports.md).
