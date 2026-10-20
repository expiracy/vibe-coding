---
title: Respect Indentation Rules
impact: MEDIUM
impactDescription: preserves visual hierarchy for quick scanning
tags: fmt, indentation, hierarchy, structure
---

## Respect Indentation Rules

Indentation makes the scope hierarchy visible. Each level of indentation represents a nested scope. Never collapse short statements onto one line to save space.

**Incorrect (collapsed structure):**

```cpp
#include <string>
#include <vector>

namespace example {
struct CommentWidget {
std::string text;
std::string render() const { return text; }
};
int countValid(const std::vector<int>& values) { int count = 0; for (int value : values) { if (value > 0) { ++count; } } return count; }
}
```

**Correct (proper indentation):**

```cpp
#include <string>
#include <vector>

namespace example {
struct CommentWidget {
    std::string text;

    std::string render() const {
        return text;
    }
};
int countValid(const std::vector<int>& values) {
    int count = 0;
    for (int value : values) {
        if (value > 0) {
            ++count;
        }
    }
    return count;
}
}
```

**Why maintain indentation?**
- Visual scanning relies on indentation
- Structure is immediately apparent
- Debugging is easier when scope is visible
- Merges are cleaner with consistent formatting

Reference: [Clean Code, Chapter 5: Formatting](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [fmt-indentation](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/fmt-indentation.md).
