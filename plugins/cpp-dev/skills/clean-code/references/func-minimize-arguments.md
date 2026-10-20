---
title: Minimize Function Arguments
impact: HIGH
impactDescription: reduces cognitive load and testing complexity
tags: func, arguments, parameters, simplicity
---

## Minimize Function Arguments

Review how many independent concepts a caller must supply. Group arguments that form a meaningful domain value, and reduce unrelated responsibilities where that simplifies the operation. Argument counts are prompts for review, not limits; preserve required public signatures and avoid wrappers that only hide parameters.

**Incorrect (too many arguments):**

```cpp

namespace example {
struct Circle { double x; double y; double radius; };
Circle makeCircle(double x, double y, double radius) { return {x, y, radius}; }
}
```

**Correct (minimized arguments):**

```cpp

namespace example {
struct Point { double x; double y; };
struct Circle { Point center; double radius; };
Circle makeCircle(Point center, double radius) { return {center, radius}; }
}
```

**Why fewer arguments?**
- Easier to understand
- Easier to test (fewer combinations)
- Less chance of argument order errors

**Acceptable monadic forms:**
- Asking a question: `bool fileExists(const std::string& path)`
- Transforming input: an operation that opens the named input
- Events: `void passwordAttemptFailed(int attempts)`

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [func-minimize-arguments](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/func-minimize-arguments.md).
