---
title: Write Learning Tests for Third-Party Code
impact: MEDIUM
impactDescription: makes dependency assumptions explicit
tags: bound, boundary, learning-tests, third-party, testing
---

## Write Learning Tests for Third-Party Code

When integrating a third-party library, write small tests that verify your understanding of how the API works. These tests serve double duty: they help you learn the API, and they act as a safety net when upgrading the library.

**Incorrect (learning by trial and error in production code):**

```cpp

namespace example {
// The example uses a stand-in to show test shape, not evidence about a vendor.
// Real learning tests must include and exercise the actual dependency.
struct VendorReading { int rawValue; bool present; };


int applicationReading(const VendorReading& reading) {
    return reading.rawValue; // Assumes units and ignores the missing-value contract.
}
}
```

**Correct (learning tests verify assumptions):**

```cpp
#include <stdexcept>

namespace example {
// The example uses a stand-in to show test shape, not evidence about a vendor.
// Real learning tests must include and exercise the actual dependency.
struct VendorReading { int rawValue; bool present; };


void readingContractIsDocumented(const VendorReading& reading) {
    if (!reading.present) throw std::logic_error("fixture must provide a reading");
    if (reading.rawValue != 420) throw std::logic_error("fixture contract changed");
}
void missingReadingIsDocumented(const VendorReading& reading) {
    if (reading.present) throw std::logic_error("fixture must represent absence");
}
}
```

The small dependency stand-in below illustrates test structure only. Real
learning tests must exercise the actual dependency; a stand-in is not evidence
of vendor behavior.

**Benefits:**
- Free education on the API's behavior
- When you upgrade the library, these tests break first — before your production code does
- Documents exactly which behaviors your code relies on
- Documents the assumptions these focused tests actually exercise

Reference: [Clean Code, Chapter 8: Boundaries](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [bound-learning-tests](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/bound-learning-tests.md).
