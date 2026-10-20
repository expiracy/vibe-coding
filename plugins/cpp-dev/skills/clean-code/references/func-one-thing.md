---
title: Functions Should Do One Thing
impact: CRITICAL
impactDescription: enables understanding functions at a glance
tags: func, single-responsibility, cohesion, focus
---

## Functions Should Do One Thing

Functions should do one thing. They should do it well. They should do it only. If a function does multiple things, extract those things into separate functions.

**Incorrect (function does multiple things):**

```cpp
#include <stdexcept>
#include <string>

namespace example {
struct Employee {
    std::string name;
    int salary{};
    int tax{};
    bool saved{};
    bool welcomed{};
};


void processEmployee(Employee& employee) {
    if (employee.name.empty()) throw std::invalid_argument("Name required");
    if (employee.salary < 0) throw std::invalid_argument("Salary cannot be negative");
    employee.tax = employee.salary * 3 / 10; // Small illustrative amounts.
    employee.saved = true;   // Repository operation in the real application.
    employee.welcomed = true; // Notification operation in the real application.
}
}
```

**Correct (each function does one thing):**

```cpp
#include <stdexcept>
#include <string>

namespace example {
struct Employee {
    std::string name;
    int salary{};
    int tax{};
    bool saved{};
    bool welcomed{};
};


void validateEmployee(const Employee& employee) {
    if (employee.name.empty()) throw std::invalid_argument("Name required");
    if (employee.salary < 0) throw std::invalid_argument("Salary cannot be negative");
}
void calculateTax(Employee& employee) { employee.tax = employee.salary * 3 / 10; }
void saveEmployee(Employee& employee) { employee.saved = true; }
void sendWelcomeEmail(Employee& employee) { employee.welcomed = true; }
void processEmployee(Employee& employee) {
    validateEmployee(employee);
    calculateTax(employee);
    saveEmployee(employee);
    sendWelcomeEmail(employee);
}
}
```

**Test:** If you can extract another function from it with a name that is not merely a restatement of its implementation, the function is doing more than one thing.

**When NOT to split:**
- Avoid helpers whose names merely restate an obvious operation. A named domain policy such as `calculateTax` can clarify intent even when its implementation is short.
- Orchestration functions that call a sequence of steps at the same abstraction level (like `processEmployee` above) are doing "one thing" — orchestrating. Don't try to extract the orchestration further.

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [func-one-thing](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/func-one-thing.md).
