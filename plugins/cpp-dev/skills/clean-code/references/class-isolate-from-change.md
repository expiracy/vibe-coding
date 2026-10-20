---
title: Isolate Classes from Change
impact: MEDIUM
impactDescription: enables testing and reduces coupling
tags: class, dip, interfaces, coupling
---

## Isolate Classes from Change

Depend on abstractions, not concretions. Classes should depend on interfaces rather than concrete implementations. This enables testing and reduces the impact of change.

**Incorrect (depends on concrete implementation):**

```cpp
#include <map>
#include <string>

namespace example {
// Fixed small illustrative prices, not a production financial model.
struct NYSEStockExchange { int currentPrice(const std::string&) const { return 150; } };


struct Portfolio {
    NYSEStockExchange exchange;
    std::map<std::string, int> holdings;
    int value() const {
        int total = 0;
        for (const auto& holding : holdings) total += exchange.currentPrice(holding.first) * holding.second;
        return total;
    }
};
}
```

**Correct (depends on abstraction):**

```cpp
#include <functional>
#include <map>
#include <stdexcept>
#include <string>

namespace example {
// Fixed small illustrative prices, not a production financial model.
struct NYSEStockExchange { int currentPrice(const std::string&) const { return 150; } };


class Portfolio {
    std::function<int(const std::string&)> currentPrice;
    std::map<std::string, int> holdings;
public:
    explicit Portfolio(std::function<int(const std::string&)> price) : currentPrice(price) {}
    void add(const std::string& symbol, int quantity) { holdings[symbol] += quantity; }
    int value() const {
        int total = 0;
        for (const auto& holding : holdings) total += currentPrice(holding.first) * holding.second;
        return total;
    }
};
void portfolioValueShouldSumAllHoldings() {
    Portfolio portfolio([](const std::string&) { return 150; });
    portfolio.add("AAPL", 10);
    if (portfolio.value() != 1500) throw std::logic_error("portfolio value changed");
}
}
```

**Dependency Inversion Principle (DIP):** High-level modules should not depend on low-level modules. Both should depend on abstractions.

Reference: [Clean Code, Chapter 10: Classes](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [class-isolate-from-change](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/class-isolate-from-change.md).
