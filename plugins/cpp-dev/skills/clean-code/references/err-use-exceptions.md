---
title: Separate Error Handling from Happy Path
impact: HIGH
impactDescription: makes success and failure contracts understandable
tags: err, exceptions, error-handling, separation, result-types
---

## Separate Error Handling from Happy Path

Error handling is important, but when it obscures logic, it's wrong. The core insight is separation: keep the happy path visible and error handling consolidated, regardless of which mechanism your language uses.

**Incorrect (error handling obscures business logic):**

```cpp
#include <string>

namespace example {
struct Page { bool exists{true}; bool reference{true}; bool configKey{true}; };


std::string deletePage(Page& page) {
    if (page.exists) {
        page.exists = false;
        if (page.reference) {
            page.reference = false;
            if (page.configKey) { page.configKey = false; return "page deleted"; }
            return "config key missing";
        }
        return "reference missing";
    }
    return "page missing";
}
}
```

**Correct (successful work separated from reporting):**

```cpp
#include <stdexcept>
#include <string>

namespace example {
struct Page { bool exists{true}; bool reference{true}; bool configKey{true}; };


void deletePageAndAllReferences(Page& page) {
    if (!page.exists) throw std::runtime_error("page missing");
    page.exists = false;
    if (!page.reference) throw std::runtime_error("reference missing");
    page.reference = false;
    if (!page.configKey) throw std::runtime_error("config key missing");
    page.configKey = false;
}
std::string deletePage(Page& page) {
    try {
        deletePageAndAllReferences(page);
        return "page deleted";
    } catch (const std::runtime_error& failure) {
        return failure.what();
    }
}
}
```

The principle is separation, not a mandate to change the project's error
mechanism. These examples illustrate an exception-enabled contract. Preserve
the existing failure and side-effect contract when adapting them. Expected
absence and operational failure can require different results.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/) and [Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [err-use-exceptions](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/err-use-exceptions.md).
