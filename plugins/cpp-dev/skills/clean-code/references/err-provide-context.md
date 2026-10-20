---
title: Provide Context with Exceptions
impact: HIGH
impactDescription: enables rapid root cause identification
tags: err, context, messages, debugging
---

## Provide Context with Exceptions

Each exception should provide enough context to determine the source and location of an error. Create informative error messages that describe the operation that failed and the type of failure.

**Incorrect (no context):**

```cpp
#include <stdexcept>
#include <string>

namespace example {
void requireUser(bool found, const std::string&) {
    if (!found) throw std::runtime_error("Not found");
}
}
```

**Correct (rich context):**

```cpp
#include <stdexcept>
#include <string>

namespace example {
void requireUser(bool found, const std::string& userId) {
    if (!found) throw std::runtime_error("Loading user " + userId + ": user not found");
}
}
```

**Include in exception messages:**
- What operation was being attempted
- What data was involved (IDs, names, quantities)
- Why it failed (the specific error condition)
- Preserve the original exception when wrapping

Reference: [Clean Code, Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [err-provide-context](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/err-provide-context.md).
