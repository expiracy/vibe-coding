---
title: Declare All Dependencies Explicitly in Constructor
impact: HIGH
impactDescription: enables testing, documents requirements, prevents hidden coupling
tags: usecase, dependencies, constructor, injection
---

## Declare All Dependencies Explicitly in Constructor

Make external behavior explicit through construction or function parameters. Avoid hidden mutable global services; pure deterministic functions and ordinary value construction need no injection seam.

**Incorrect:**

```cpp
struct Store { void save(int); };
Store& global_store();
void place_order(int id) { global_store().save(id); }
```

**Better for this contract:**

```cpp
struct Store { virtual ~Store() = default; virtual void save(int id) = 0; };
class PlaceOrder {
    Store& store_;
public:
    explicit PlaceOrder(Store& store) : store_(store) {}
    void execute(int id) { store_.save(id); }
};
```

The reference borrows a dependency that must outlive the use case. Ownership and lifetime policy belong to cpp-guidelines; this rule makes coupling visible.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Dependency Injection Principles](https://martinfowler.com/articles/injection.html)

Upstream rule: [usecase-explicit-dependencies](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/usecase-explicit-dependencies.md).
