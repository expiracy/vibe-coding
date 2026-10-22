---
title: Presenters Format Data for the View
impact: MEDIUM
impactDescription: enables multiple view formats from same use case
tags: adapt, presenter, formatting, view-model
---

## Presenters Format Data for the View

Keep presentation decisions in a presenter or pure formatting function. Return view-shaped data where it simplifies the UI; do not preformat fields that a client needs as structured values.

**Incorrect:**

```cpp
struct Summary { bool overdue; };
struct Screen { void set_warning(bool); void set_text(const char*); };
void show(Screen& screen, Summary data) {
    screen.set_warning(data.overdue);
    screen.set_text(data.overdue ? "Overdue" : "Current");
}
```

**Better for this contract:**

```cpp
#include <string_view>
struct Summary { bool overdue; };
struct ViewModel { bool warning; std::string_view label; };
ViewModel present(Summary data) { return {data.overdue, data.overdue ? "Overdue" : "Current"}; }
struct Screen { void render(ViewModel); };
void show(Screen& screen, Summary data) { screen.render(present(data)); }
```

Labels here reference string literals. Localization, escaping and ownership of dynamically generated text need the appropriate adapter contracts.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Presenters and Humble Objects](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch23.xhtml)

Upstream rule: [adapt-presenter-formats](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/adapt-presenter-formats.md).
