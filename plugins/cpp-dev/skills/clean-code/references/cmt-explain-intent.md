---
title: Use Comments to Explain Intent
impact: HIGH
impactDescription: preserves decision rationale for future readers
tags: cmt, intent, why, rationale
---

## Use Comments to Explain Intent

Good comments explain WHY, not WHAT. The code already tells you what it does. Comments should explain the reasoning behind a decision that cannot be expressed in code.

**Incorrect (narrating the code):**

```cpp
#include <algorithm>
#include <vector>

namespace example {
struct Session { int createdAt{}; };


void sortSessions(std::vector<Session>& sessions) {
    // Sort the sessions.
    std::sort(sessions.begin(), sessions.end(),
        [](Session a, Session b) { return a.createdAt > b.createdAt; });
}
}
```

**Correct (explaining intent):**

```cpp
#include <algorithm>
#include <vector>

namespace example {
struct Session { int createdAt{}; };


void sortSessions(std::vector<Session>& sessions) {
    // In this example, users expect their newest sessions first.
    std::sort(sessions.begin(), sessions.end(),
        [](Session a, Session b) { return a.createdAt > b.createdAt; });
}
}
```

**Good comment situations:**
- Legal comments (copyright, license)
- Explanation of intent or rationale
- Clarification of obscure API behavior
- Warning of consequences
- TODO comments (temporary)

Reference: [Clean Code, Chapter 4: Comments](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [cmt-explain-intent](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/cmt-explain-intent.md).
