---
title: Minimize Function Arguments
impact: HIGH
impactDescription: reduces cognitive load and testing complexity
tags: func, arguments, parameters, simplicity
---

## Minimize Function Arguments

Review how many independent concepts a caller must supply. Group arguments that form a meaningful domain value, and reduce unrelated responsibilities where that simplifies the operation. Argument counts are prompts for review, not limits; preserve required public signatures and avoid wrappers that only hide parameters.

**Incorrect (too many arguments):**

```java
// A mode flag may hide distinct operations; assess the existing contract
public void render(boolean isSuite) {}

// Four arguments - hard to remember order
public Circle makeCircle(double x, double y, double radius, String color) {}

// Order matters and is easy to confuse
public void assertExpectedEqualsActual(String expected, String actual) {}
```

**Correct (minimized arguments):**

```java
// Separate functions instead of flag
public void renderForSingleTest() {}
public void renderForSuite() {}

// Encapsulate related arguments in objects
public Circle makeCircle(Point center, double radius, Color color) {}

// A builder can help when many optional parameters justify it
Circle circle = Circle.builder()
    .center(new Point(0, 0))
    .radius(5.0)
    .color(Color.RED)
    .build();

// Self-documenting method name
assertThat(actual).isEqualTo(expected);
```

**Why fewer arguments?**
- Easier to understand
- Easier to test (fewer combinations)
- Less chance of argument order errors

**Acceptable monadic forms:**
- Asking a question: `boolean fileExists(String path)`
- Transforming input: `InputStream openFile(String path)`
- Events: `void passwordAttemptFailed(int attempts)`

Reference: [Clean Code, Chapter 3: Functions](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [func-minimize-arguments](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/func-minimize-arguments.md).
