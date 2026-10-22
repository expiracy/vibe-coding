---
title: Use Humble Objects at Architectural Boundaries
impact: MEDIUM-HIGH
impactDescription: maximizes testable code, isolates hard-to-test parts
tags: bound, humble-object, testing, boundaries
---

## Use Humble Objects at Architectural Boundaries

Keep the hard-to-test device/UI/network edge small. Extract deterministic decisions into ordinary C++ operations; still test the real edge for its own contract.

**Incorrect:**

```cpp
struct Screen { void draw(const char*); };
void update(Screen& screen, bool overdue) {
    if (overdue) screen.draw("Overdue"); else screen.draw("Current");
}
```

**Better for this contract:**

```cpp
#include <string_view>
std::string_view status_label(bool overdue) { return overdue ? "Overdue" : "Current"; }
struct Screen { void draw(std::string_view); };
void update(Screen& screen, bool overdue) { screen.draw(status_label(overdue)); }
```

A direct status_label test establishes the decision only. Rendering, threading and device behavior need their own integration or UI checks.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Humble Object Pattern](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch23.xhtml)

Upstream rule: [bound-humble-object](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/bound-humble-object.md).
