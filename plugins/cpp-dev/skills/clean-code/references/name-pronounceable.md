---
title: Use Pronounceable Names
impact: HIGH
impactDescription: enables verbal communication about code
tags: name, pronounceable, communication, readability
---

## Use Pronounceable Names

Use pronounceable names. If you cannot pronounce a name, you cannot discuss it without sounding foolish. Programming is a social activity; names should facilitate discussion.

**Incorrect (unpronounceable abbreviations):**

```cpp
#include <chrono>
#include <string>

namespace example {
struct DtaRcrd102 {
    std::chrono::system_clock::time_point genymdhms{};
    std::chrono::system_clock::time_point modymdhms{};
    std::string pszqint{"102"};
};
}
```

**Correct (pronounceable names):**

```cpp
#include <chrono>
#include <string>

namespace example {
struct Customer {
    std::chrono::system_clock::time_point generationTimestamp{};
    std::chrono::system_clock::time_point modificationTimestamp{};
    std::string recordId{"102"};
};
}
```

The pronounceable version enables natural conversation: "Hey, when did we modify this customer's generation timestamp?"

Reference: [Clean Code, Chapter 2: Meaningful Names](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [name-pronounceable](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/name-pronounceable.md).
