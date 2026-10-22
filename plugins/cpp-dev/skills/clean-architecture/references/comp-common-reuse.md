---
title: Avoid Forcing Clients to Depend on Unused Code
impact: HIGH
impactDescription: reduces unnecessary recompilation and deployment
tags: comp, common-reuse, dependencies, coupling
---

## Avoid Forcing Clients to Depend on Unused Code

A client should not need a heavy dependency for an unrelated utility. Split interfaces/targets where actual usage differs, rather than making every caller depend on an omnibus header or library.

**Incorrect:**

```cpp
#include <string_view>
namespace image_backend { struct Image {}; }
namespace utilities {
struct All { static bool valid_id(std::string_view); static image_backend::Image resize(); };
}
```

**Better for this contract:**

```cpp
#include <string_view>
namespace identifiers { bool valid_id(std::string_view); }
// identifiers.hpp has no image-backend include or link requirement.
// image_tools.hpp and its CMake target own the image dependency.
```

A source file that stops including the image header may still link the heavy target. Check target/public link requirements as well as includes.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Common Reuse Principle](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch13.xhtml)

Upstream rule: [comp-common-reuse](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/comp-common-reuse.md).
