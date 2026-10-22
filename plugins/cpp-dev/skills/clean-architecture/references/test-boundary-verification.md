---
title: Verify Architectural Boundaries with Tests
impact: LOW-MEDIUM
impactDescription: prevents boundary erosion, enforces dependency rules
tags: test, boundaries, architecture, enforcement
---

## Verify Architectural Boundaries with Tests

Enforce useful compile/build boundaries in CI. Build domain/application targets without infrastructure include/link access, compile public headers in isolation, and inspect actual dependency information where available.

```cmake
add_library(domain domain/src/order.cpp)
target_include_directories(domain PUBLIC domain/include)
target_compile_features(domain PUBLIC cxx_std_20)
add_library(sql_orders adapters/sql_orders.cpp)
target_link_libraries(sql_orders PRIVATE domain)
# Domain sees only its own public headers and intended dependencies.
```

This is a contextual CMake excerpt, not a complete project. Compile a scratch translation unit that includes each changed public header first. Include/link checks do not prove semantic independence or correct runtime wiring.

Upstream rule: [test-boundary-verification](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/test-boundary-verification.md).
