---
title: Express Yourself in Code, Not Comments
impact: CRITICAL
impactDescription: eliminates stale comment risk
tags: cmt, self-documenting, refactoring, clarity
---

## Express Yourself in Code, Not Comments

In many cases, creating a function that says the same thing as the comment you wanted to write is better. Code can be refactored to be self-explanatory.

**Incorrect (comment explains obscure code):**

```java
// Check to see if the employee is eligible for full benefits
if ((employee.flags & HOURLY_FLAG) != 0 && employee.age > 65) {
    // ...
}

// Add 30 days to the current date
Date newDate = new Date(currentDate.getTime() + (30L * 24 * 60 * 60 * 1000));

// Returns true if the string contains only digits
boolean result = str.matches("[0-9]+");
```

**Correct (code expresses intent):**

```java
if (employee.isEligibleForFullBenefits()) {
    // ...
}

// In Employee class:
public boolean isEligibleForFullBenefits() {
    return isHourlyWorker() && age > RETIREMENT_AGE;
}

// Here currentDate is a java.time.LocalDate.
java.time.LocalDate newDate = currentDate.plusDays(30);

// Alternatively, use the project's numeric-string helper.
// Or define your own:
boolean result = containsOnlyDigits(str);
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
- **Public API documentation:** Javadoc/docstrings for public APIs are expected and useful.

Reference: [Clean Code, Chapter 4: Comments](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [cmt-express-in-code](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/cmt-express-in-code.md).
