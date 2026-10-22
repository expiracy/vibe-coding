---
title: Use Cases Must Not Contain Presentation Logic
impact: HIGH
impactDescription: enables multiple UI implementations from same use case
tags: usecase, presentation, formatting, separation
---

## Use Cases Must Not Contain Presentation Logic

Return application data from the use case. Keep locale, labels, markup and view-specific visibility in the presenter unless formatting is itself the requested business capability.

**Incorrect:**

```cpp
#include <string>
std::string order_total(int cents) { return "<b>Total cents: " + std::to_string(cents) + "</b>"; }
```

**Better for this contract:**

```cpp
#include <string>
struct OrderSummary { int total_cents; };
OrderSummary summarize(int cents) { return {cents}; }
std::string present(const OrderSummary& summary) {
    return "Total cents: " + std::to_string(summary.total_cents);
}
```

The text example displays integer cents intentionally. Real currency, locale and escaping rules belong to an explicit presentation contract.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [Clean Architecture - Presenters](https://www.oreilly.com/library/view/clean-architecture-a/9780134494272/ch23.xhtml)

Upstream rule: [usecase-no-presentation-logic](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/usecase-no-presentation-logic.md).
