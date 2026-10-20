---
title: One Concept Per Test
impact: MEDIUM
impactDescription: enables precise failure diagnosis
tags: test, assert, concept, focus
---

## One Concept Per Test

Each test should verify a single concept or behavior. Multiple assertions are fine when they all verify different aspects of that one concept. What you want to avoid is testing unrelated concerns in a single test.

**Incorrect (multiple unrelated concepts in one test):**

```cpp
#include <stdexcept>
#include <string>
#include <vector>

namespace example {
void require(bool condition, const std::string& message) {
    if (!condition) throw std::logic_error(message);
}

struct User { std::string name; std::string email; bool active{}; std::vector<int> orders; };
User createUser(const std::string& name, const std::string& email) { return {name, email, true, {}}; }


void checksUnrelatedConcerns() {
    const auto user = createUser("Bob", "bob@example.com");
    require(user.name == "Bob", "user name");
    require(std::string("report.txt").size() == 10, "unrelated report formatting");
}
}
```

**Correct (one concept per test, multiple assertions are fine):**

```cpp
#include <stdexcept>
#include <string>
#include <vector>

namespace example {
void require(bool condition, const std::string& message) {
    if (!condition) throw std::logic_error(message);
}

struct User { std::string name; std::string email; bool active{}; std::vector<int> orders; };
User createUser(const std::string& name, const std::string& email) { return {name, email, true, {}}; }


void returnedUserHasTheSuppliedIdentity() {
    const auto user = createUser("Bob", "bob@example.com");
    require(user.name == "Bob", "name");
    require(user.email == "bob@example.com", "email");
    require(user.active, "active status");
}
}
```

The first test has three assertions — that's fine because they all verify a single concept: "the returned user object is correctly constructed." Each test can be understood from its name alone.

**When NOT to split tests:**
- When multiple assertions verify the same behavior from different angles (like checking all fields of a returned object), keep them together — splitting creates duplicate setup and slower test suites.
- When the operation under test has side effects (API calls, DB writes), avoid calling it multiple times just to isolate assertions.

Reference: [Clean Code, Chapter 9: Unit Tests](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [test-one-assert](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/test-one-assert.md).
