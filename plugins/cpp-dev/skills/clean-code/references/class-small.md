---
title: Keep Classes Small
impact: MEDIUM
impactDescription: enables comprehension and focused testing
tags: class, size, srp, cohesion
---

## Keep Classes Small

Classes should be small. With functions, we measure size by counting lines. With classes, we count responsibilities. A class should have only one reason to change.

**Incorrect (large class with multiple responsibilities):**

```cpp
#include <string>

namespace example {
struct SuperDashboard {
    std::string applicationVersion{"1.0"};
    int focusedWidget{};
    std::string getVersion() const { return applicationVersion; }
    void focusWidget(int widget) { focusedWidget = widget; }
};
}
```

**Correct (small focused classes):**

```cpp
#include <string>

namespace example {
struct Version {
    int major;
    int minor;
    std::string text() const { return std::to_string(major) + "." + std::to_string(minor); }
};
struct Dashboard {
    int focusedWidget{};
    void focusWidget(int widget) { focusedWidget = widget; }
};
}
```

**Single Responsibility Principle (SRP):** A class should have one, and only one, reason to change.

Reference: [Clean Code, Chapter 10: Classes](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [class-small](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/class-small.md).
