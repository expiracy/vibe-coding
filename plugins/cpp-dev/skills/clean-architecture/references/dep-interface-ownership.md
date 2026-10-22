---
title: Interfaces Belong to Clients Not Implementers
impact: CRITICAL
impactDescription: enables true dependency inversion
tags: dep, interfaces, dependency-inversion, ownership
---

## Interfaces Belong to Clients Not Implementers

The policy consuming a capability owns its contract. An adapter includes that contract and implements it; the policy header should not include the adapter header.

```cpp
namespace application {
struct OrderStore { virtual ~OrderStore() = default; virtual void save(int id) = 0; };
void checkout(OrderStore& store) { store.save(7); }
}
namespace storage {
struct Database final : application::OrderStore { void save(int) override {} };
}
```

A callable or template contract can be appropriate for compile-time substitution. Runtime polymorphism is an option, not a universal requirement.

Reference: [Clean Architecture - Chapter 11: DIP](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch11.xhtml)

Upstream rule: [dep-interface-ownership](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/dep-interface-ownership.md).
