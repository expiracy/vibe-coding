---
title: Domain Layer Has Zero Framework Dependencies
impact: MEDIUM
impactDescription: enables framework migration, pure unit tests
tags: frame, domain, purity, dependencies
---

## Domain Layer Has Zero Framework Dependencies

Keep domain headers free of delivery/persistence framework base classes and annotations. Standard library and suitable stable domain libraries can remain direct dependencies.

**Incorrect:**

```cpp
namespace orm { struct Entity { virtual ~Entity() = default; virtual void save() = 0; }; }
struct Order : orm::Entity { int quantity{}; void save() override {} };
```

**Better for this contract:**

```cpp
#include <stdexcept>
class Order {
    int quantity_;
public:
    explicit Order(int quantity) : quantity_(quantity) {
        if (quantity < 1) throw std::invalid_argument("invalid quantity");
    }
    int quantity() const { return quantity_; }
};
```

A domain target that compiles without infrastructure include paths supplies useful evidence. Text searches are a rough screen, not proof against transitive or generated dependencies.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Frameworks are Details](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [frame-domain-purity](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/frame-domain-purity.md).
