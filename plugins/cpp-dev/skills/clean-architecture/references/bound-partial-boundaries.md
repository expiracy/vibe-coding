---
title: Use Partial Boundaries When Full Separation is Premature
impact: MEDIUM-HIGH
impactDescription: prepares for future without over-engineering now
tags: bound, partial-boundaries, pragmatism, yagni
---

## Use Partial Boundaries When Full Separation is Premature

Where change pressure is real but a full component split is premature, start with a small contract in the current binary. Avoid speculative service boundaries and interface forests.

**Incorrect:**

```cpp
namespace sql { struct Database { int load_price(int); }; }
int quote(sql::Database& database, int id) { return database.load_price(id); }
```

**Better for this contract:**

```cpp
#include <functional>
int quote(int id, const std::function<int(int)>& price_for) { return price_for(id); }
// Composition can bind the current database operation without another service.
```

This callable is an illustration, not a requirement to type-erase every function. Use a template/direct function if that better fits the existing contract and performance constraints.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Partial Boundaries](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch24.xhtml)

Upstream rule: [bound-partial-boundaries](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/bound-partial-boundaries.md).
