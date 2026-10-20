---
title: Follow FIRST Principles
impact: MEDIUM
impactDescription: makes behavior checks readable and repeatable
tags: test, first, fast, independent, repeatable
---

## Follow FIRST Principles

Clean tests follow FIRST: Fast, Independent, Repeatable, Self-Validating, and Timely. These properties ensure tests remain useful and maintainable.

**Incorrect (violating FIRST):**

```cpp
#include <stdexcept>
#include <string>
#include <vector>

namespace example {
void require(bool condition, const std::string& message) {
    if (!condition) throw std::logic_error(message);
}


struct Repository { std::vector<int> users; };
Repository sharedRepository;
void createsUser() { sharedRepository.users.push_back(1); }
void dependsOnPreviousTest() { require(sharedRepository.users.size() == 1, "previous test must run first"); }
}
```

**Correct (following FIRST):**

```cpp
#include <stdexcept>
#include <string>
#include <vector>

namespace example {
void require(bool condition, const std::string& message) {
    if (!condition) throw std::logic_error(message);
}


struct Repository { std::vector<int> users; };
void createsOneUserIndependently() {
    Repository repository;
    repository.users.push_back(1);
    require(repository.users.size() == 1, "one user created");
}
void emptyRepositoryIsIndependent() {
    Repository repository;
    require(repository.users.empty(), "fresh repository is empty");
}
}
```

Reference: [Clean Code, Chapter 9: Unit Tests](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [test-first-principles](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/test-first-principles.md).
