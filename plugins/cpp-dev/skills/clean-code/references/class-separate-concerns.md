---
title: Separate Construction from Use
impact: MEDIUM
impactDescription: enables testing and reduces coupling
tags: class, construction, factories, separation
---

## Separate Construction from Use

The startup process of object construction is a separate concern from runtime logic. Applications should separate the main function (which builds objects) from the rest of the system (which uses them).

**Incorrect (construction mixed with use):**

```cpp
#include <string>

namespace example {
struct Order { int id; };
std::string smtpConfirmation(const Order& order) { return "smtp confirmation " + std::to_string(order.id); }


std::string processOrder(const Order& order) {
    // The business operation chooses its external destination.
    return smtpConfirmation(order);
}
}
```

**Correct (construction separated from use):**

```cpp
#include <functional>
#include <string>

namespace example {
struct Order { int id; };
std::string smtpConfirmation(const Order& order) { return "smtp confirmation " + std::to_string(order.id); }


class OrderProcessor {
    std::function<std::string(const Order&)> sendConfirmation;
public:
    explicit OrderProcessor(std::function<std::string(const Order&)> sender) : sendConfirmation(sender) {}
    std::string processOrder(const Order& order) const { return sendConfirmation(order); }
};
OrderProcessor buildApplication() { return OrderProcessor(smtpConfirmation); }
}
```

Use the existing application composition approach; no dependency-injection framework is required by this principle.

Reference: [Clean Code, Chapter 11: Systems](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [class-separate-concerns](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/class-separate-concerns.md).
