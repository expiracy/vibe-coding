---
title: Make Meaningful Distinctions
impact: CRITICAL
impactDescription: eliminates ambiguity between similar concepts
tags: name, distinction, noise-words, clarity
---

## Make Meaningful Distinctions

If names must be different, then they should also mean something different. Avoid number-series naming and noise words that add no information.

**Incorrect (indistinguishable names):**

```cpp
#include <vector>

namespace example {
void copyChars(const std::vector<char>& a1, std::vector<char>& a2) { a2 = a1; }
struct Product {};
struct ProductInfo {};
struct ProductData {};
}
```

**Correct (meaningful distinctions):**

```cpp
#include <vector>

namespace example {
void copyChars(const std::vector<char>& source, std::vector<char>& destination) {
    destination = source;
}
struct Product {};
struct ProductDetails {};
struct ProductInventory {};
}
```

If you cannot distinguish what `ProductInfo` offers that `Product` does not, the names are noise.

Reference: [Clean Code, Chapter 2: Meaningful Names](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [name-meaningful-distinctions](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/name-meaningful-distinctions.md).
