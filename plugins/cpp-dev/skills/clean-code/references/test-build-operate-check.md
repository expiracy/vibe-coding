---
title: Use Build-Operate-Check Pattern
impact: MEDIUM
impactDescription: makes behavior checks readable and repeatable
tags: test, boc, arrange-act-assert, structure
---

## Use Build-Operate-Check Pattern

Structure tests in three distinct phases: Build (arrange), Operate (act), Check (assert). This pattern makes tests easy to read and understand at a glance.

**Incorrect (mixed phases, unclear structure):**

```cpp
#include <stdexcept>
#include <string>
#include <vector>

namespace example {
void require(bool condition, const std::string& message) {
    if (!condition) throw std::logic_error(message);
}

struct Order {
    std::vector<int> itemPricesCents;
    void addItem(int price) { itemPricesCents.push_back(price); }
    int totalCents() const { int total = 0; for (int price : itemPricesCents) total += price; return total; }
};


void testsOrder() {
    Order order;
    order.addItem(999);
    require(order.totalCents() == 999, "one item");
    order.addItem(999);
    require(order.itemPricesCents.size() == 2, "second item");
    require(order.totalCents() == 1998, "two items");
}
}
```

**Correct (clear Build-Operate-Check):**

```cpp
#include <stdexcept>
#include <string>
#include <vector>

namespace example {
void require(bool condition, const std::string& message) {
    if (!condition) throw std::logic_error(message);
}

struct Order {
    std::vector<int> itemPricesCents;
    void addItem(int price) { itemPricesCents.push_back(price); }
    int totalCents() const { int total = 0; for (int price : itemPricesCents) total += price; return total; }
};


void addsAnItemToTheOrder() {
    // Build.
    Order order;
    order.addItem(999);

    // Operate.
    order.addItem(999);

    // Check.
    require(order.itemPricesCents.size() == 2, "item count");
    require(order.totalCents() == 1998, "total cents");
}
}
```

**Alias patterns:**
- Build-Operate-Check (BOC)
- Arrange-Act-Assert (AAA)
- Given-When-Then (BDD)

Reference: [Clean Code, Chapter 9: Unit Tests](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [test-build-operate-check](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/test-build-operate-check.md).
