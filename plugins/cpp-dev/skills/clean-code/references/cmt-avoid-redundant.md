---
title: Avoid Redundant Comments
impact: HIGH
impactDescription: eliminates noise that obscures important information
tags: cmt, redundant, noise, clutter
---

## Avoid Redundant Comments

A comment that merely restates what the code does is worse than no comment. It adds clutter, becomes stale, and trains readers to ignore comments entirely.

**Incorrect (redundant comments):**

```cpp
#include <string>

namespace example {
class Account {
    // The name of the customer.
    std::string customerName;
public:
    // Default constructor.
    Account() = default;
    // Returns the name.
    std::string getName() const { return customerName; }
};
}
```

**Correct (comment only when necessary):**

```cpp
#include <string>

namespace example {
class Account {
    std::string customerName;
public:
    Account() = default;
    std::string getName() const { return customerName; }
};
// This example's legacy mail parser requires this date representation.
const std::string DATE_FORMAT = "EEE, dd MMM yyyy HH:mm:ss Z";
}
```

**Rule of thumb:** If the comment just repeats the code in English, delete it.

Reference: [Clean Code, Chapter 4: Comments](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [cmt-avoid-redundant](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/cmt-avoid-redundant.md).
