---
title: One Concept Per Test
impact: MEDIUM
impactDescription: enables precise failure diagnosis
tags: test, assert, concept, focus
---

## One Concept Per Test

Each test should verify a single concept or behavior. Multiple assertions are fine when they all verify different aspects of that one concept. What you want to avoid is testing unrelated concerns in a single test.

For a user-creation test, these checks describe one returned result. Use the
project's assertion API; the API names below are illustrative.

```cpp
const auto user = createUser("Bob", "bob@example.com");
CHECK(user.name == "Bob");
CHECK(user.email == "bob@example.com");
CHECK(user.active);
```

**When NOT to split tests:**
- When multiple assertions verify the same behavior from different angles (like checking all fields of a returned object), keep them together — splitting creates duplicate setup and slower test suites.
- When the operation under test has side effects (API calls, DB writes), avoid calling it multiple times just to isolate assertions.

Reference: [Clean Code, Chapter 9: Unit Tests](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [test-one-assert](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/test-one-assert.md).
