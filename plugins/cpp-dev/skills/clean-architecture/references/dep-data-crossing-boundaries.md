---
title: Use Simple Data Structures Across Boundaries
impact: CRITICAL
impactDescription: prevents coupling between layers
tags: dep, boundaries, dto, data-transfer
---

## Use Simple Data Structures Across Boundaries

Choose boundary data for the receiving contract. Do not leak database rows, lazy-loading sessions or transport objects into a use case. An entity can cross an internal boundary when its meaning and dependency direction genuinely fit.

**Incorrect:**

```cpp
#include <string>
namespace database { struct CustomerRow { std::string name; std::string password_hash; }; }
namespace application { database::CustomerRow customer_details(); }
```

**Better for this contract:**

```cpp
#include <string>
namespace application { struct CustomerDetails { std::string name; }; }
namespace database { struct CustomerRow { std::string name; std::string password_hash; }; }
application::CustomerDetails to_details(const database::CustomerRow& row) { return {row.name}; }
```

Use separate representations where meanings, security requirements or change reasons differ. Avoid redundant copies for every function call. Test the actual serializer for disclosure claims.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Crossing Boundaries](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html)

Upstream rule: [dep-data-crossing-boundaries](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/dep-data-crossing-boundaries.md).
