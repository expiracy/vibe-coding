---
title: Defer Framework and Database Decisions
impact: MEDIUM-HIGH
impactDescription: preserves optionality, reduces early commitment risk
tags: bound, deferral, decisions, optionality
---

## Defer Framework and Database Decisions

Defer expensive vendor decisions only while doing so reduces uncertainty. A small in-memory implementation can exercise the application contract before the persistence choice is known.

**Incorrect:**

```cpp
namespace vendor { struct Database { void insert(int); }; }
struct Orders { vendor::Database database; void place(int id) { database.insert(id); } };
```

**Better for this contract:**

```cpp
#include <vector>
struct Orders { virtual ~Orders() = default; virtual void save(int) = 0; };
struct MemoryOrders final : Orders {
    std::vector<int> saved;
    void save(int id) override { saved.push_back(id); }
};
void place(Orders& orders, int id) { orders.save(id); }
```

An in-memory prototype does not establish durability, concurrency, query performance or transaction semantics. Investigate those early when they drive the architectural choice.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - The Database is a Detail](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch30.xhtml)

Upstream rule: [bound-defer-decisions](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/bound-defer-decisions.md).
