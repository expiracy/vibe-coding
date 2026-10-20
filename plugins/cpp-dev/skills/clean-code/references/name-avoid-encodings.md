---
title: Avoid Encodings in Names
impact: HIGH
impactDescription: reduces mental translation burden
tags: name, encoding, hungarian, prefixes
---

## Avoid Encodings in Names

Encoding type or scope information into names adds an extra burden of deciphering. Modern IDEs make Hungarian Notation and member prefixes unnecessary.

**Incorrect (encoded type and scope):**

```cpp
#include <string>

namespace example {
struct Person { std::string strName; int iAge{}; bool bIsActive{}; };
class Part {
    std::string m_dsc;
public:
    void setDescription(const std::string& dsc) { m_dsc = dsc; }
};
}
```

**Correct (no encodings):**

```cpp
#include <string>

namespace example {
struct Person { std::string name; int age{}; bool active{}; };
class Part {
    std::string description;
public:
    void setDescription(const std::string& value) { description = value; }
};
}
```

Readers learn to ignore prefixes. You end up seeing only the meaningful part of the name.

**Note:** `ShapeFactoryImpl` is a lesser evil than `IShapeFactory`, but `Impl` is still an encoding. When possible, name implementations by their distinguishing characteristic (protocol, storage mechanism, algorithm).

Reference: [Clean Code, Chapter 2: Meaningful Names](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [name-avoid-encodings](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/name-avoid-encodings.md).
