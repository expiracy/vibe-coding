---
title: Test Each Layer in Isolation
impact: LOW-MEDIUM
impactDescription: fast feedback, precise failure location
tags: test, isolation, layers, unit
---

## Test Each Layer in Isolation

Test domain invariants directly and use case decisions through application contracts. Add real adapter and composition tests for behavior those direct checks cannot establish.

**Incorrect:**

```cpp
struct HttpClient { int post_order(int); };
void domain_test(HttpClient& client) { (void)client.post_order(0); /* Requires HTTP just to check a domain rule. */ }
```

**Better for this contract:**

```cpp
#include <stdexcept>
bool valid_quantity(int quantity) { return quantity > 0; }
void domain_test() {
    if (valid_quantity(0)) throw std::runtime_error("zero must be rejected");
    if (!valid_quantity(1)) throw std::runtime_error("one must be accepted");
}
```

A test pyramid is a planning heuristic, not fixed percentages. A fake store cannot prove database mappings, durability or transaction atomicity.

C++20 examples are independent contextual translation units; declarations of fictional external APIs are illustrative. Compile for syntax separately; they are not complete integrations.

Reference: [The Test Pyramid](https://martinfowler.com/articles/practical-test-pyramid.html)

Upstream rule: [test-layer-isolation](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-architecture/references/test-layer-isolation.md).
