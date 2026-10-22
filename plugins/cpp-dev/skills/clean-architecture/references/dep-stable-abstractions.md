---
title: Depend on Stable Abstractions Not Volatile Concretions
impact: CRITICAL
impactDescription: makes policy boundaries and dependency tradeoffs clearer
tags: dep, stability, abstractions, volatility
---

## Depend on Stable Abstractions Not Volatile Concretions

Use a stable contract to isolate a volatile dependency. Do not add an interface around a stable value type or deterministic function merely to satisfy a pattern.

**Incorrect:**

```cpp
namespace vendor { struct PriceClient { int request_price(int); }; }
struct Checkout { vendor::PriceClient& client; int total(int id) { return client.request_price(id); } };
```

**Better for this contract:**

```cpp
struct Prices { virtual ~Prices() = default; virtual int price(int id) const = 0; };
struct Checkout { Prices& prices; int total(int id) const { return prices.price(id); } };
```

The contract must express the application need, including failure and freshness semantics. A renamed vendor API can still leak vendor policy.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Stable Abstractions Principle](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch11.xhtml)

Upstream rule: [dep-stable-abstractions](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/dep-stable-abstractions.md).
