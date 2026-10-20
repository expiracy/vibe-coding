---
title: Avoid Horizontal Alignment
impact: MEDIUM
impactDescription: prevents alignment maintenance burden
tags: fmt, horizontal, alignment, whitespace
---

## Avoid Horizontal Alignment

Horizontal alignment of variable declarations or assignments looks nice but creates maintenance problems. When one line changes length, all aligned lines need reformatting.

**Incorrect (horizontal alignment):**

```cpp
#include <string>

namespace example {
struct ConnectionState {
    std::string    remoteHost;
    int            requestParsingTimeLimit{};
    int            requestProgress{};
};
}
```

**Correct (natural formatting):**

```cpp
#include <string>

namespace example {
struct ConnectionState {
    std::string remoteHost;
    int requestParsingTimeLimit{};
    int requestProgress{};
};
}
```

**Why avoid alignment?**
- Adding a longer variable name requires reformatting all lines
- Eyes are drawn to the wrong thing (the alignment, not the names)
- Most formatters don't preserve it anyway

Reference: [Clean Code, Chapter 5: Formatting](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [fmt-horizontal-alignment](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/fmt-horizontal-alignment.md).
