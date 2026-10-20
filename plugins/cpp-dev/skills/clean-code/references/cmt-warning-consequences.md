---
title: Use Warning Comments for Consequences
impact: MEDIUM
impactDescription: prevents costly mistakes by future maintainers
tags: cmt, warning, consequences, safety
---

## Use Warning Comments for Consequences

Comments that warn other programmers about certain consequences are valuable. They prevent others from making mistakes that have non-obvious impacts.

**Incorrect (no warning about hidden dangers):**

```cpp
#include <vector>

namespace example {
void removeSelectedRecords(std::vector<int>& records) { records.clear(); }
}
```

**Correct (warnings prevent mistakes):**

```cpp
#include <vector>

namespace example {
// WARNING: This operation permanently discards the records supplied to it.
// Copy them first if the caller needs an undo operation.
void removeSelectedRecords(std::vector<int>& records) { records.clear(); }
}
```

**Good warnings include:**
- Thread-safety concerns
- Performance implications
- External dependencies or side effects
- Security considerations

Reference: [Clean Code, Chapter 4: Comments](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [cmt-warning-consequences](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/cmt-warning-consequences.md).
