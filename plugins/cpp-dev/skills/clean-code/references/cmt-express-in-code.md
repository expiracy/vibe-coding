---
title: Express Yourself in Code, Not Comments
impact: CRITICAL
impactDescription: eliminates stale comment risk
tags: cmt, self-documenting, refactoring, clarity
---

## Express Yourself in Code, Not Comments

In many cases, creating a function that says the same thing as the comment you wanted to write is better. Code can be refactored to be self-explanatory.

**Incorrect (comment explains obscure code):**

```cpp

namespace example {
struct Employee { unsigned flags{}; int age{}; };
bool check(const Employee& employee) {
    // Check eligibility for the example's full-benefits policy.
    return (employee.flags & 1u) != 0 && employee.age > 65;
}
}
```

**Correct (code expresses intent):**

```cpp

namespace example {
struct Employee {
    unsigned flags{};
    int age{};
    static constexpr unsigned HOURLY_FLAG = 1u;
    static constexpr int RETIREMENT_AGE = 65; // Illustrative policy, not a recommendation.
    bool isEligibleForFullBenefits() const {
        return (flags & HOURLY_FLAG) != 0 && age > RETIREMENT_AGE;
    }
};
}
```

**Benefits:**
- Function names are searchable
- Functions can be tested
- Code documents itself
- No risk of comment becoming stale

**When comments are still valuable:**
- **Why, not what:** Comments explaining *why* a decision was made (business rules, regulatory requirements, algorithm choices) cannot be replaced by code.
- **Warnings:** Thread-safety, performance implications, or non-obvious side effects deserve explicit comments.
- **Legal/license comments:** Required by policy and cannot be expressed as code.
- **Public API documentation:** Project-required API documentation for public APIs are expected and useful.

Reference: [Clean Code, Chapter 4: Comments](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [cmt-express-in-code](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/cmt-express-in-code.md).
