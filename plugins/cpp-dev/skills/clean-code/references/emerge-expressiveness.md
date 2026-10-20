---
title: Maximize Expressiveness
impact: MEDIUM-HIGH
impactDescription: helps remove unnecessary structure
tags: emerge, expressiveness, readability, maintenance
---

## Maximize Expressiveness

The majority of the cost of a software project is in long-term maintenance. Write code for the reader, not the writer. The clearer the author can make the code, the less time others will spend understanding it.

**Incorrect (clever but opaque):**

```cpp

namespace example {
bool qualifies(int s, int n) { return s == 2 && n >= 10; }
}
```

**Correct (clear and expressive):**

```cpp

namespace example {
enum class CustomerStatus { ordinary, premium };
bool qualifiesForVolumeDiscount(CustomerStatus status, int itemCount) {
    constexpr int minimumVolumeItems = 10;
    return status == CustomerStatus::premium && itemCount >= minimumVolumeItems;
}
}
```

**Techniques for expressiveness:**
- Choose good names (the single most effective technique)
- Keep functions and classes small and focused
- Use standard patterns and nomenclature — when you use the Strategy pattern, name the class with "Strategy" so readers recognize the intent
- Write well-crafted unit tests — tests are documentation by example

Reference: [Clean Code, Chapter 12: Emergence](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [emerge-expressiveness](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/emerge-expressiveness.md).
