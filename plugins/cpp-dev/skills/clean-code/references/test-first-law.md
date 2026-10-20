---
title: Follow the Three Laws of TDD
impact: MEDIUM
impactDescription: makes behavior checks readable and repeatable
tags: test, tdd, first, laws
---

## Follow the Three Laws of TDD

Test-Driven Development follows three rules: (1) Write a failing test before production code, (2) Write only enough test to fail, (3) Write only enough production code to pass. This cycle repeats.

**Incorrect (writing tests after code):**

```cpp
#include <stdexcept>
#include <string>

namespace example {
void require(bool condition, const std::string& message) {
    if (!condition) throw std::logic_error(message);
}


int divide(int numerator, int denominator) { return numerator / denominator; }
void testCalculator() { require(divide(6, 3) == 2, "division"); }
// A new zero-denominator requirement is not yet checked.
}
```

**Correct (TDD cycle):**

```cpp
#include <stdexcept>
#include <string>

namespace example {
void require(bool condition, const std::string& message) {
    if (!condition) throw std::logic_error(message);
}


int divide(int numerator, int denominator) {
    if (denominator == 0) throw std::invalid_argument("zero denominator");
    return numerator / denominator;
}
void dividesOrdinaryValues() { require(divide(6, 3) == 2, "ordinary division"); }
void rejectsZeroDenominator() {
    bool rejected = false;
    try { (void)divide(6, 0); }
    catch (const std::invalid_argument&) { rejected = true; }
    require(rejected, "zero denominator must be rejected");
}
// This is the final green state; run the new failing scenario before implementing it.
}
```

**Benefits:**
- Tests cover requirements, not implementation
- Edge cases discovered through test-first thinking
- Coverage depends on the scenarios selected and checked

Reference: [Clean Code, Chapter 9: Unit Tests](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [test-first-law](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/test-first-law.md).
