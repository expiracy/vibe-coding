---
title: Design Failure Paths First
impact: HIGH
impactDescription: prevents missing error handling cases
tags: err, try-catch, tdd, boundaries
---

## Design Failure Paths First

Start by defining the caller-visible failure behavior, then organize success and reporting around that contract. Preserve the project's existing error policy; the illustration below uses exceptions without prescribing that mechanism for every project.

**Incorrect (error handling added as afterthought):**

```cpp
#include <fstream>
#include <string>

namespace example {
std::string retrieveSection(const std::string& sectionName) {
    std::ifstream stream(sectionName);
    std::string line;
    std::getline(stream, line);
    return line; // A missing file and an empty section look the same.
}
}
```

**Correct (missing-file and read-failure behavior are explicit):**

```cpp
#include <fstream>
#include <stdexcept>
#include <string>

namespace example {
std::string retrieveSection(const std::string& sectionName) {
    std::ifstream stream(sectionName);
    if (!stream) throw std::runtime_error("Cannot open section: " + sectionName);
    std::string line;
    if (!std::getline(stream, line)) {
        throw std::runtime_error("Cannot read section: " + sectionName);
    }
    return line;
}
// First add a test of the required missing-file behavior, then implement it.
void missingSectionIsReported(const std::string& knownMissingPath) {
    bool reported = false;
    try { (void)retrieveSection(knownMissingPath); }
    catch (const std::runtime_error&) { reported = true; }
    if (!reported) throw std::logic_error("missing section must be reported");
}
}
```

**Benefits:**
- Forces you to consider error cases first
- Makes partial-success and failure expectations explicit
- Failure scenarios become observable requirements

Reference: [Clean Code, Chapter 7: Error Handling](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [err-write-try-catch-first](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/err-write-try-catch-first.md).
