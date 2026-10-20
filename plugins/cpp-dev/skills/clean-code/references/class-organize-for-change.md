---
title: Organize Classes for Change
impact: MEDIUM
impactDescription: minimizes modification risk when requirements change
tags: class, ocp, change, design
---

## Organize Classes for Change

Classes should be organized so that change is minimally invasive. Following the Open-Closed Principle (OCP): classes should be open for extension but closed for modification.

**Incorrect (must modify class for each new SQL type):**

```cpp
#include <string>

namespace example {
struct Sql {
    std::string table;
    std::string create() const { return "CREATE TABLE " + table; }
    std::string insert() const { return "INSERT INTO " + table; }
    // Another operation requires editing this class again.
};
}
```

**Correct (extend without modifying):**

```cpp
#include <string>

namespace example {
// Illustrative command generation; not a complete SQL construction API.
struct Sql {
    virtual std::string generate() const = 0;
    virtual ~Sql() = default;
};
struct CreateSql : Sql {
    std::string table;
    explicit CreateSql(std::string value) : table(value) {}
    std::string generate() const override { return "CREATE TABLE " + table; }
};
struct InsertSql : Sql {
    std::string table;
    explicit InsertSql(std::string value) : table(value) {}
    std::string generate() const override { return "INSERT INTO " + table; }
};
}
```

**Benefits:**
- Adding new SQL types = adding new classes
- Existing classes remain untouched
- Each class does one thing

This illustration assumes a real extension requirement. A small closed set of
alternatives may be clearer as explicit cases; do not add a hierarchy merely to
satisfy the principle.

Reference: [Clean Code, Chapter 10: Classes](https://www.oreilly.com/library/view/clean-code-a/9780136083238/)

Upstream rule: [class-organize-for-change](https://github.com/pproenca/dot-skills/blob/cf93c57cac89d6fc3e4194686000411567f5caf3/skills/.experimental/clean-code/references/class-organize-for-change.md).
