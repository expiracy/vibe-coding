---
title: Design for Testability From the Start
impact: LOW-MEDIUM
impactDescription: enables comprehensive testing without test-induced damage
tags: test, testability, design, interfaces
---

## Design for Testability From the Start

Make uncertain external inputs, including time when relevant, controllable. Deterministic functions, value constructors and pure static operations can be tested directly without new interfaces.

**Incorrect:**

```cpp
#include <chrono>
bool expired(std::chrono::system_clock::time_point deadline) {
    return std::chrono::system_clock::now() >= deadline;
}
```

**Better for this contract:**

```cpp
#include <chrono>
#include <stdexcept>
bool expired(std::chrono::system_clock::time_point now, std::chrono::system_clock::time_point deadline) {
    return now >= deadline;
}
void test_expiry_boundary() {
    const auto deadline = std::chrono::system_clock::time_point{};
    if (!expired(deadline, deadline)) throw std::runtime_error("deadline should be expired");
}
```

Choose the clock according to the real contract: wall time and elapsed monotonic time are different. The example tests equality only; other relevant boundaries need coverage.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Growing Object-Oriented Software, Guided by Tests](http://www.growing-object-oriented-software.com/)

Upstream rule: [test-testable-design](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/test-testable-design.md).
